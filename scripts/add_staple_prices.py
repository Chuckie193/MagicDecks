r"""
add_staple_prices.py

Refresh the Price column in Commander Staples/**/*.md with real EUR prices.

Usage:
  python scripts/add_staple_prices.py                 # update every staples file in place
  python scripts/add_staple_prices.py --dry-run       # show what would change, write nothing
  python scripts/add_staple_prices.py --offline       # use the local cache only, no network

Why this exists:
  The staples files are hand-curated and most of their prices are ESTIMATES,
  because the environment they were written in could not reach Scryfall. This
  script replaces every estimate with a real EUR figure.

Behavior:
  - Walks Commander Staples/**/*.md and finds markdown table rows.
  - Column 1 is the card name, and the Price column is located by its header.
  - Looks each card up in scripts/cache/cards_cache.json first. On a miss it
    queries the Scryfall API (unless --offline) and writes the result back to
    the cache, so repeat runs are fast and network-light.
  - Prices come from the CHEAPEST non-foil printing (Scryfall `prints_search_uri`),
    which is what matters when buying a card to play with. This can differ from
    the price in cards_cache.json, which reflects the specific printing owned.
  - Rewrites the Price cell as "EUR X.XX ✓ <tier>" and re-tiers the card:
        under EUR 3     -> budget marker
        EUR 3 to EUR 10 -> mid marker
        over EUR 10     -> premium marker
  - Any existing "Cheaper alternatives:" note in the Notes column is left alone,
    but the script REPORTS cards whose tier changed so they can be reviewed --
    a card that fell below EUR 10 no longer needs alternatives, and one that rose
    above EUR 10 now does.

Rows skipped on purpose:
  - Rows whose name cell holds two cards joined by "/" (e.g. "Ponder / Preordain")
    or a slash-separated land cycle: these are priced as a range by hand.
  - Rows whose Price cell is "--" or empty.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAPLES_DIR = os.path.join(REPO_ROOT, "Commander Staples")
CACHE_PATH = os.path.join(REPO_ROOT, "scripts", "cache", "cards_cache.json")

HEADERS = {"User-Agent": "MagicDecks/1.0", "Accept": "application/json"}
REQUEST_DELAY = 0.1  # Scryfall asks for 50-100ms between requests

BUDGET = "\U0001F49A"   # green heart  - under EUR 3
MID = "\U0001F49B"      # yellow heart - EUR 3 to EUR 10
PREMIUM = "\U0001F534"  # red circle   - over EUR 10

PREMIUM_THRESHOLD = 10.0
BUDGET_THRESHOLD = 3.0

# Matches the price cell we write, plus the hand-written estimate forms
# ("~EUR 4", "*not cached*", "~EUR 0.20-3").
TIER_MARKERS = f"{BUDGET}{MID}{PREMIUM}"


def tier_for(eur: float) -> str:
    if eur > PREMIUM_THRESHOLD:
        return PREMIUM
    if eur >= BUDGET_THRESHOLD:
        return MID
    return BUDGET


def load_cache() -> dict:
    if not os.path.exists(CACHE_PATH):
        return {}
    try:
        with open(CACHE_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError) as exc:
        print(f"warning: could not read cache ({exc}); starting empty", file=sys.stderr)
        return {}


def save_cache(cache: dict) -> None:
    # Match generate_cards_md.py's dump convention exactly (no sort_keys), so a
    # run that adds nothing new leaves the file byte-identical instead of
    # producing a whole-file reformatting diff.
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    with open(CACHE_PATH, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, ensure_ascii=False, indent=2)


def fetch_json(url: str):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def cheapest_eur_from_prints(prints_uri: str):
    """Return the lowest non-foil EUR price across all printings, or None."""
    best = None
    url = prints_uri
    while url:
        data = fetch_json(url)
        for card in data.get("data", []):
            raw = (card.get("prices") or {}).get("eur")
            if not raw:
                continue
            try:
                val = float(raw)
            except ValueError:
                continue
            if best is None or val < best:
                best = val
        url = data.get("next_page") if data.get("has_more") else None
        if url:
            time.sleep(REQUEST_DELAY)
    return best


def lookup_price(name: str, cache: dict, offline: bool):
    """Return (eur_float_or_None, source_str)."""
    entry = cache.get(name)
    if entry:
        data = entry.get("data") or {}
        cached_prints = entry.get("cheapest_eur")
        if cached_prints is not None:
            return cached_prints, "cache"
        raw = (data.get("prices") or {}).get("eur")
        if raw and offline:
            try:
                return float(raw), "cache(owned-printing)"
            except ValueError:
                pass

    if offline:
        return None, "offline-miss"

    try:
        q = urllib.parse.quote(name)
        data = fetch_json(f"https://api.scryfall.com/cards/named?exact={q}")
        time.sleep(REQUEST_DELAY)
        prints_uri = data.get("prints_search_uri")
        eur = cheapest_eur_from_prints(prints_uri) if prints_uri else None
        if eur is None:
            raw = (data.get("prices") or {}).get("eur")
            eur = float(raw) if raw else None
        # Persist so the next run is fast.
        entry = cache.setdefault(name, {"data": data, "urls": []})
        entry["data"] = data
        entry["cheapest_eur"] = eur
        return eur, "scryfall"
    except Exception as exc:  # network, 404, malformed payload
        print(f"  ! {name}: lookup failed ({exc})", file=sys.stderr)
        return None, "error"


def split_row(line: str):
    """Split a markdown table row into cells. Returns None if not a table row."""
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return stripped[1:-1].split("|")


def is_separator(cells) -> bool:
    return all(re.fullmatch(r"\s*:?-{2,}:?\s*", c) for c in cells)


def clean_name(cell: str) -> str:
    """Strip markdown emphasis and links from a name cell."""
    text = cell.strip()
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # [x](y) -> x
    text = text.replace("**", "").replace("*", "").strip()
    return text


def skip_name(name: str) -> bool:
    # Slash-joined pairs/cycles are priced as a hand-written range.
    return "/" in name or name.startswith("(") or not name


def process_file(path: str, cache: dict, offline: bool, dry_run: bool):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    name_idx = price_idx = None
    changed = 0
    retiers = []

    for i, line in enumerate(lines):
        cells = split_row(line)
        if cells is None:
            name_idx = price_idx = None  # left the table
            continue
        if is_separator(cells):
            continue

        headers = [c.strip().lower() for c in cells]
        if "price" in headers and ("card" in headers or "name" in headers):
            price_idx = headers.index("price")
            name_idx = headers.index("card") if "card" in headers else headers.index("name")
            continue

        if name_idx is None or price_idx is None:
            continue
        if price_idx >= len(cells) or name_idx >= len(cells):
            continue

        name = clean_name(cells[name_idx])
        if skip_name(name):
            continue

        old_cell = cells[price_idx].strip()
        if old_cell in ("", "--", "—"):
            continue

        eur, source = lookup_price(name, cache, offline)
        if eur is None:
            continue

        old_tier = next((m for m in TIER_MARKERS if m in old_cell), None)
        new_tier = tier_for(eur)
        new_cell = f" €{eur:.2f} ✓ {new_tier} "

        if cells[price_idx] != new_cell:
            cells[price_idx] = new_cell
            lines[i] = "|" + "|".join(cells) + "|"
            changed += 1
            print(f"  {name}: {old_cell.strip()} -> €{eur:.2f} {new_tier}  [{source}]")

        if old_tier and old_tier != new_tier:
            retiers.append((name, old_tier, new_tier, eur))

    if changed and not dry_run:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))

    return changed, retiers


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="report changes without writing files")
    ap.add_argument("--offline", action="store_true", help="use the local cache only, never hit the network")
    ap.add_argument("--dir", default=STAPLES_DIR, help="staples directory (default: Commander Staples)")
    args = ap.parse_args()

    if not os.path.isdir(args.dir):
        print(f"error: no such directory: {args.dir}", file=sys.stderr)
        return 1

    cache = load_cache()
    md_files = []
    for root, _dirs, files in os.walk(args.dir):
        for fn in sorted(files):
            if fn.endswith(".md") and fn != "README.md":
                md_files.append(os.path.join(root, fn))

    total_changed = 0
    all_retiers = []
    for path in sorted(md_files):
        rel = os.path.relpath(path, REPO_ROOT)
        print(f"\n{rel}")
        changed, retiers = process_file(path, cache, args.offline, args.dry_run)
        total_changed += changed
        all_retiers.extend(retiers)
        if not changed:
            print("  (no changes)")

    if not args.dry_run:
        save_cache(cache)

    print(f"\n{'Would update' if args.dry_run else 'Updated'} {total_changed} price cell(s) "
          f"across {len(md_files)} file(s).")

    if all_retiers:
        print("\nTier changes -- review the 'Cheaper alternatives' notes on these rows:")
        for name, old, new, eur in all_retiers:
            note = ""
            if new == PREMIUM:
                note = "  <- now premium, ADD alternatives"
            elif old == PREMIUM:
                note = "  <- no longer premium, alternatives can be dropped"
            print(f"  {name}: {old} -> {new} (€{eur:.2f}){note}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
