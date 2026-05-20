"""
generate_commanders_md.py

Scan the Scryfall cards cache for all Legendary Creatures and Legendary
Spacecraft (which use the Station mechanic), download their card images
from Scryfall, and produce a Commanders.md gallery with inline images.

Usage:
  python scripts/generate_commanders_md.py \
    --cache scripts/cache/cards_cache.json \
    --images-dir images/commanders \
    --out Commanders.md
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request


def sanitize_filename(name: str) -> str:
    s = re.sub(r"[^\w\s-]", "", name)
    s = re.sub(r"[\s-]+", "_", s)
    return s.strip("_") + ".jpg"


def get_image_uri(data: dict) -> str | None:
    """Return the normal-size image URI from cached Scryfall card data."""
    if not data:
        return None
    if "image_uris" in data:
        return data["image_uris"].get("normal")
    # double-faced cards — use front face
    faces = data.get("card_faces")
    if faces:
        return faces[0].get("image_uris", {}).get("normal")
    return None


def get_api_image_url(data: dict) -> str | None:
    """Return a Scryfall API URL that serves the card image directly."""
    uri = data.get("uri") if data else None
    if not uri:
        return None
    return uri + "?format=image&version=normal"


def is_commander_candidate(data: dict) -> bool:
    if not data:
        return False
    type_line = data.get("type_line", "")
    if "Legendary" not in type_line:
        return False
    if "Creature" in type_line:
        return True
    # Spacecraft with Station mechanic (e.g. Inspirit, Flagship Vessel)
    if "Spacecraft" in type_line:
        oracle = data.get("oracle_text", "") or ""
        if "Station" in oracle:
            return True
    return False


def color_identity_str(data: dict) -> str:
    ci = data.get("color_identity", [])
    names = {"W": "White", "U": "Blue", "B": "Black", "R": "Red", "G": "Green"}
    return ", ".join(names.get(c, c) for c in ci) if ci else "Colorless"


def download_image(url: str, dest: str) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "MagicDecks/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
        with open(dest, "wb") as fh:
            fh.write(raw)
        return True
    except Exception as e:
        print(f"    ERROR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="scripts/cache/cards_cache.json")
    parser.add_argument("--images-dir", default="images/commanders")
    parser.add_argument("--out", default="Commanders.md")
    args = parser.parse_args()

    if not os.path.isfile(args.cache):
        print(f"Cache not found: {args.cache}")
        sys.exit(1)

    with open(args.cache, encoding="utf-8") as fh:
        cache = json.load(fh)

    # Collect unique commander candidates, sorted by name
    commanders = {}
    for name, entry in cache.items():
        if not isinstance(entry, dict):
            continue
        data = entry.get("data")
        if is_commander_candidate(data):
            commanders[name] = data

    if not commanders:
        print("No Legendary Creatures or Station Spacecraft found in cache.")
        sys.exit(0)

    print(f"Found {len(commanders)} commander candidates.")
    os.makedirs(args.images_dir, exist_ok=True)

    # Download images (skip if already on disk); fall back to CDN URL if blocked
    image_paths = {}   # name -> (local_rel_path | cdn_url | None)
    image_is_local = {}  # name -> bool
    total = len(commanders)
    for idx, name in enumerate(sorted(commanders), 1):
        data = commanders[name]
        filename = sanitize_filename(name)
        dest = os.path.join(args.images_dir, filename)
        rel = args.images_dir.replace(os.sep, "/") + "/" + filename

        if os.path.isfile(dest):
            print(f"  [{idx}/{total}] {name} — already downloaded")
            image_paths[name] = rel
            image_is_local[name] = True
            continue

        cdn_url = get_image_uri(data)
        if not cdn_url:
            print(f"  [{idx}/{total}] {name} — no image URL in cache")
            image_paths[name] = None
            image_is_local[name] = False
            continue

        print(f"  [{idx}/{total}] {name} — downloading...")
        ok = download_image(cdn_url, dest)
        if ok:
            image_paths[name] = rel
            image_is_local[name] = True
            time.sleep(0.15)
        else:
            # Network blocked — embed the CDN URL directly so browsers can render it
            print(f"           ^ download failed; will use CDN URL in markdown")
            image_paths[name] = cdn_url
            image_is_local[name] = False

    # Write Commanders.md — one row per card: image on left, details on right
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("# Potential Commanders\n\n")
        fh.write(
            f"All Legendary Creatures and Legendary Spacecraft (Station mechanic) "
            f"in your collection — **{len(commanders)} cards**.\n\n"
        )
        fh.write("---\n\n")

        # Group by color identity for easier browsing
        by_ci = {}
        for name in sorted(commanders):
            data = commanders[name]
            ci_key = color_identity_str(data)
            by_ci.setdefault(ci_key, []).append(name)

        ci_order = ["Colorless", "White", "Blue", "Black", "Red", "Green",
                    "White, Blue", "White, Black", "White, Red", "White, Green",
                    "Blue, Black", "Blue, Red", "Blue, Green", "Black, Red",
                    "Black, Green", "Red, Green"]
        # append any multi-color combos not in the predefined order
        for ci in sorted(by_ci):
            if ci not in ci_order:
                ci_order.append(ci)

        for ci in ci_order:
            if ci not in by_ci:
                continue
            fh.write(f"## {ci}\n\n")
            fh.write("| Card | Name | Type |\n")
            fh.write("|------|------|------|\n")
            for name in by_ci[ci]:
                data = commanders[name]
                type_line = data.get("type_line", "").replace("|", "\\|")
                safe_name = name.replace("|", "\\|")
                img_src = image_paths.get(name)
                if img_src:
                    # use <img> so we can cap the width — card images are large
                    img_cell = f'<img src="{img_src}" alt="{safe_name}" width="200">'
                else:
                    img_cell = "*(no image)*"
                fh.write(f"| {img_cell} | **{safe_name}** | {type_line} |\n")
            fh.write("\n")

    local_count = sum(1 for v in image_is_local.values() if v)
    cdn_count = sum(1 for name, v in image_is_local.items() if not v and image_paths.get(name))
    missing_count = sum(1 for p in image_paths.values() if p is None)

    print(f"\nWROTE {args.out}")
    if local_count:
        print(f"  {local_count} images downloaded locally → {args.images_dir}/")
    if cdn_count:
        print(f"  {cdn_count} images embedded as CDN URLs (will render in browser but not locally)")
    if missing_count:
        print(f"  {missing_count} images missing entirely")


if __name__ == "__main__":
    main()
