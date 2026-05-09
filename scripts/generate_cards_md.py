r"""
generate_cards_md.py

Generate moxfield_cards.md from moxfield_latest.csv and Precons/*.txt.
Usage:
  python scripts/generate_cards_md.py \
    --csv moxfield_latest.csv \
    --precons Precons \
    --out moxfield_cards.md \
    --auto-threshold 0.90 \
    --ambiguous-threshold 0.75

Behavior:
- Parses Precons/*.txt (one card per line, optional leading quantity, optional first-line title)
- Supports alternative names in square brackets, e.g. "Main Name [Alt Name]"
- Normalizes names and matches exactly against CSV names, then applies fuzzy matching (difflib) for unmatched cards
- Produces a markdown with table columns: Name, Edition, Count, Precon, Duplicate, and per-precon summaries

"""

import argparse
import csv
import os
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from datetime import datetime, timezone
import json
import urllib.request
import urllib.parse
import time

RE_PAREN = re.compile(r"\s*\([^\)]*\)")
RE_NOT_ALNUM = re.compile(r"[^a-z0-9\s]")


def normalize_name(name: str) -> str:
    n = name or ""
    n = n.lower()
    n = RE_PAREN.sub("", n)
    n = RE_NOT_ALNUM.sub("", n)
    n = re.sub(r"\s+", " ", n)
    return n.strip()


def parse_deck_file(path: str):
    """Parse a deck file. Returns (precon_name, list of entries)

    Each entry is a dict: { name, norm, qty, alts } where alts is a list of alt normalized names.
    """
    lines = []
    with open(path, encoding="utf-8") as fh:
        for ln in fh:
            ln = ln.rstrip('\n').strip()
            if ln == "" or ln.startswith('#'):
                continue
            lines.append(ln)
    title = None
    if lines and lines[0].endswith(':'):
        title = lines[0].rstrip(':').strip()
        lines = lines[1:]
    name = title if title else os.path.splitext(os.path.basename(path))[0].replace('-', ' ').replace('_', ' ')
    cards = []
    for ln in lines:
        m = re.match(r"^(\d+)\s+(.+)$", ln)
        if m:
            qty = int(m.group(1))
            card_text = m.group(2).strip()
        else:
            qty = 1
            card_text = ln
        # detect alternative names in square brackets, e.g. "Main Name [Alt1; Alt2]"
        alt_names = []
        br = re.search(r"\[(.*?)\]", card_text)
        if br:
            alt_text = br.group(1)
            # split on common separators
            parts = re.split(r"[;,|]\s*", alt_text)
            alt_names = [p.strip() for p in parts if p.strip()]
            # remove bracketed part from the main card name
            main_name = re.sub(r"\s*\[.*?\]", "", card_text).strip()
        else:
            main_name = card_text
        # remove foil markers like *F* and (F) and stray ' F' markers first
        main_name = re.sub(r"\*F\*|\(F\)|\s+F\s*$", "", main_name).strip()
        # strip trailing set/collector info like "(SLD) 2099" or trailing numbers (handles cases where foil markers were present)
        main_name = re.sub(r"\s*\([A-Za-z0-9\-\s]*\)\s*\d+\s*$", "", main_name).strip()
        main_name = re.sub(r"\s+\d{2,5}\s*$", "", main_name).strip()
        norm = normalize_name(main_name)
        alt_norms = [normalize_name(a) for a in alt_names]
        cards.append({'name': main_name, 'norm': norm, 'qty': qty, 'alts': alt_norms, 'raw': ln})
    return name, cards


def read_precons(dirpath: str):
    decks = {}
    for fn in sorted(os.listdir(dirpath)):
        if not fn.lower().endswith('.txt'):
            continue
        full = os.path.join(dirpath, fn)
        if not os.path.isfile(full):
            continue
        precon_name, cards = parse_deck_file(full)
        # aggregate by normalized name, keep alt norms in list
        d = {}
        for entry in cards:
            norm = entry['norm']
            if norm in d:
                d[norm]['qty'] += entry['qty']
            else:
                d[norm] = {'name': entry['name'], 'norm': norm, 'qty': entry['qty'], 'alts': entry['alts']}
        decks[precon_name] = d
    return decks


def read_csv(csvpath: str):
    rows = []
    with open(csvpath, encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            rows.append(r)
    return rows


def levenshtein_ratio(a: str, b: str) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    # use SequenceMatcher ratio which is similar to normalized similarity
    return SequenceMatcher(None, a, b).ratio()


def assign_precons(decks, rows, auto_thresh=0.90, ambig_thresh=0.75):
    # build csv norm index -> list of row indices
    csv_index = defaultdict(list)
    for i, r in enumerate(rows):
        norm = normalize_name(r.get('Name', ''))
        csv_index[norm].append(i)
    csv_norms = list(csv_index.keys())

    # initial exact matches
    for i, r in enumerate(rows):
        r['Precon'] = ''
    for pre, cmap in decks.items():
        for norm, info in cmap.items():
            if norm in csv_index:
                for idx in csv_index[norm]:
                    if rows[idx]['Precon']:
                        rows[idx]['Precon'] += '; ' + pre
                    else:
                        rows[idx]['Precon'] = pre
            else:
                # if original norm not found, try exact match on alts
                for alt in info.get('alts', []):
                    if alt in csv_index:
                        for idx in csv_index[alt]:
                            append = pre + ' (alt)'
                            if rows[idx]['Precon']:
                                rows[idx]['Precon'] += '; ' + append
                            else:
                                rows[idx]['Precon'] = append
                        break

    heuristic = defaultdict(list)
    ambiguous = defaultdict(list)

    # fuzzy match for norms not in csv_index (only if not matched by alt exact)
    for pre, cmap in decks.items():
        for norm, info in cmap.items():
            # skip if already matched exactly or via alt
            already_matched = False
            if norm in csv_index:
                already_matched = True
            else:
                for alt in info.get('alts', []):
                    if alt in csv_index:
                        already_matched = True
                        break
            if already_matched:
                continue
            # find best fuzzy match among csv_norms
            best = None
            best_score = 0.0
            for cn in csv_norms:
                score = levenshtein_ratio(norm, cn)
                if score > best_score:
                    best_score = score
                    best = cn
            # if fuzzy fails on original, try fuzzy on alts (choose best alt fuzzy)
            if (not best or best_score < ambig_thresh) and info.get('alts'):
                for alt in info.get('alts', []):
                    for cn in csv_norms:
                        score = levenshtein_ratio(alt, cn)
                        if score > best_score:
                            best_score = score
                            best = cn
            if best and best_score >= auto_thresh:
                heuristic[pre].append((info['name'], norm, best, best_score))
                for idx in csv_index[best]:
                    append = f"{pre} (heuristic:{best_score:.2f})"
                    if rows[idx]['Precon']:
                        rows[idx]['Precon'] += '; ' + append
                    else:
                        rows[idx]['Precon'] = append
            elif best and best_score >= ambig_thresh:
                ambiguous[pre].append((info['name'], norm, best, best_score))
                for idx in csv_index[best]:
                    append = f"{pre} (ambiguous:{best_score:.2f})"
                    if rows[idx]['Precon']:
                        rows[idx]['Precon'] += '; ' + append
                    else:
                        rows[idx]['Precon'] = append
    return rows, heuristic, ambiguous


def write_md(outpath, rows, decks, heuristic, ambiguous):
    # compute duplicates
    dup_counts = defaultdict(int)
    for r in rows:
        key = f"{r.get('Name','')}|{r.get('Edition','')}"
        dup_counts[key] += 1

    with open(outpath, 'w', encoding='utf-8') as fh:
        fh.write(f"# Moxfield Latest — Cards with Precon Assignments (generated {datetime.now(timezone.utc).isoformat()}Z)\n\n")
        fh.write("## All cards (table)\n\n")
        fh.write("|Name|Edition|Count|Precon|Duplicate|\n")
        fh.write("|---|---|---:|---|---:|\n")
        for r in rows:
            name = r.get('Name','').replace('|','&#124;')
            edition = r.get('Edition','')
            count = r.get('Count','')
            precon = r.get('Precon','')
            dup = ''
            key = f"{r.get('Name','')}|{r.get('Edition','')}"
            if dup_counts.get(key,0) > 1:
                dup = f"Yes ({dup_counts[key]})"
            fh.write(f"|{name}|{edition}|{count}|{precon}|{dup}|\n")

        fh.write('\n## Cards not assigned to precons\n\n')
        unassigned = [r for r in rows if not r.get('Precon')]
        if not unassigned:
            fh.write('- None\n')
        else:
            for r in unassigned:
                fh.write(f"- {r.get('Name')} — Edition: {r.get('Edition')}\n")

        # per-precon
        for pre, cmap in decks.items():
            fh.write('\n---\n\n')
            fh.write(f"## Precon: {pre}\n")
            expected_total = sum(info['qty'] for info in cmap.values())
            fh.write(f"Expected total quantity (from decklist): {expected_total}\n")
            # matched total: exact matches + heuristics/ambiguous
            # count any CSV rows that were assigned this precon (exact, alt, heuristic, ambiguous)
            matched = 0
            for r in rows:
                assigned = r.get('Precon','') or ''
                if assigned and pre in assigned:
                    matched += int(r.get('Count',0) or 0)

            fh.write(f"Matched total quantity in CSV (exact + heuristics): {matched}\n\n")
            fh.write("### Heuristic matches (auto-assigned):\n")
            if not heuristic.get(pre):
                fh.write('- None\n')
            else:
                for item in heuristic.get(pre):
                    fh.write(f"- {item[0]} -> CSV normalized: {item[2]} (score: {item[3]:.3f})\n")
            fh.write('\n### Ambiguous matches:\n')
            if not ambiguous.get(pre):
                fh.write('- None\n')
            else:
                for item in ambiguous.get(pre):
                    fh.write(f"- {item[0]} -> CSV normalized: {item[2]} (score: {item[3]:.3f})\n")

            # missing after heuristics
            fh.write('\n### Missing cards (after heuristics):\n')
            missing = []
            for norm, info in cmap.items():
                found_qty = 0
                for r in rows:
                    if normalize_name(r.get('Name','')) == norm:
                        found_qty += int(r.get('Count',0) or 0)
                # add heuristic/ambiguous matches
                for item in heuristic.get(pre, []):
                    if item[1] == norm:
                        for r in rows:
                            if normalize_name(r.get('Name','')) == item[2]:
                                found_qty += int(r.get('Count',0) or 0)
                for item in ambiguous.get(pre, []):
                    if item[1] == norm:
                        for r in rows:
                            if normalize_name(r.get('Name','')) == item[2]:
                                found_qty += int(r.get('Count',0) or 0)
                if found_qty < info['qty']:
                    missing.append(f"{info['name']} (missing {info['qty'] - found_qty})")
            if not missing:
                fh.write('- None\n')
            else:
                for m in missing:
                    fh.write(f"- {m}\n")

            fh.write('\n### Extras (CSV rows attributed to this precon but not in decklist):\n')
            extras = []
            for r in rows:
                assigned = r.get('Precon','')
                if assigned and pre in assigned:
                    n = normalize_name(r.get('Name',''))
                    if n not in cmap:
                        extras.append(f"{r.get('Name')} — Edition: {r.get('Edition')}")
            if not extras:
                fh.write('- None\n')
            else:
                for e in extras:
                    fh.write(f"- {e}\n")


def mana_cost_to_text(mana_cost: str) -> str:
    # convert Scryfall mana cost like '{2}{U}{R}' to plain English
    if not mana_cost:
        return '0 (no mana cost)'
    tokens = re.findall(r"\{([^}]+)\}", mana_cost)
    parts = []
    generic = 0
    for t in tokens:
        if t.isdigit():
            generic += int(t)
        elif t.upper() == 'X':
            parts.append('X (variable)')
        else:
            # handle hybrid symbols like '2/R' or 'W/U' by splitting on '/'
            if '/' in t:
                subs = [symbol_to_word(s) for s in t.split('/')]
                parts.append('/'.join(subs))
            else:
                parts.append(symbol_to_word(t))
    if generic:
        parts.insert(0, f"{generic} generic")
    return ', '.join(parts) if parts else '0'


def symbol_to_word(sym: str) -> str:
    s = sym.strip().upper()
    mapping = {
        'W': 'White',
        'U': 'Blue',
        'B': 'Black',
        'R': 'Red',
        'G': 'Green',
        'C': 'Colorless',
        'S': 'Snow',
        'P': 'Phyrexian',
        'X': 'X (variable)',
        'T': 'Tap',
        'Q': 'Untap',
    }
    return mapping.get(s, s)


def colors_to_text(colors_list) -> str:
    if not colors_list:
        return 'Colorless or None'
    return ', '.join(symbol_to_word(c) for c in colors_list)


def convert_oracle_text(oracle_text: str) -> str:
    """Convert MTG symbols and newlines in oracle text to readable format."""
    if not oracle_text:
        return ''
    
    # Replace {SYMBOL} with [Keyword] for readability
    # Handle multi-char symbols like {2/R}, {W/U}, etc.
    def replace_symbol(match):
        content = match.group(1)
        # Split on / for hybrid mana
        if '/' in content:
            parts = [symbol_to_word(p.strip()) for p in content.split('/')]
            return '[' + '/'.join(parts) + ']'
        else:
            # Try to convert single symbol
            word = symbol_to_word(content)
            return '[' + word + ']'
    
    text = re.sub(r'\{([^}]+)\}', replace_symbol, oracle_text)
    # Replace literal \n with actual newlines
    text = text.replace('\\n', '\n')
    return text


def read_existing_card_details(path: str) -> set:
    names = set()
    if not os.path.isfile(path):
        return names
    with open(path, encoding='utf-8') as fh:
        for ln in fh:
            m = re.match(r"^##\s+(.*)", ln)
            if m:
                names.add(m.group(1).strip())
    return names


def read_successful_raw_responses(path: str) -> set:
    """Read card names with SUCCESS status from scryfall_raw_responses.md"""
    successful = set()
    if not os.path.isfile(path):
        return successful
    with open(path, encoding='utf-8') as fh:
        current_card = None
        for ln in fh:
            # detect card header
            m = re.match(r"^##\s+(.*)", ln)
            if m:
                current_card = m.group(1).strip()
            # check for success status
            elif current_card and re.match(r"^\*\*Status:\*\*\s+Success", ln):
                successful.add(current_card)
    return successful


def scryfall_lookup(name: str, cache: dict) -> tuple:
    # uses cache dict to avoid repeated network calls; returns (data, urls_info)
    if name in cache:
        entry = cache[name]
        if entry is None:
            return None, [{'url': None, 'success': False, 'status_code': None, 'error': 'cached-missing'}]
        if isinstance(entry, dict) and 'data' in entry:
            return entry.get('data'), entry.get('urls', [])
        # legacy raw cached response
        return entry, []
    attempted = []
    # build URL using fuzzy search only (one call per card)
    q_fuzzy = urllib.parse.quote(name, safe='')
    url = f"https://api.scryfall.com/cards/named?fuzzy={q_fuzzy}"
    headers = {'User-Agent': 'MagicDecks/1.0', 'Accept': 'application/json'}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            code = resp.getcode()
            if code != 200:
                raise Exception(f"HTTP {code}")
            data = json.load(resp)
        attempted.append({'url': url, 'success': True, 'status_code': code, 'error': None})
        cache[name] = {'data': data, 'urls': attempted}
        return data, attempted
    except Exception as e:
        attempted.append({'url': url, 'success': False, 'status_code': getattr(e, 'code', None), 'error': str(e)})
        cache[name] = {'data': None, 'urls': attempted}
        return None, attempted


def append_raw_response(path: str, name: str, data: dict, urls: list):
    """Append a single card's raw Scryfall response to a file as it comes back.
    Removes any existing entry for this card first to avoid duplicates."""
    
    # Read entire file and filter out the card if it exists
    existing_lines = []
    if os.path.isfile(path):
        with open(path, encoding='utf-8') as fh:
            lines = fh.readlines()
        in_card = False
        for line in lines:
            # Check if this is the start of our card section
            if re.match(rf"^##\s+{re.escape(name)}\s*$", line):
                in_card = True
                continue
            # Check if this is a new card section
            if in_card and re.match(r"^##\s+", line):
                in_card = False
            # Keep line if not in our card's section
            if not in_card:
                existing_lines.append(line)
    
    # Write back without the old card entry, then append new one
    with open(path, 'w', encoding='utf-8') as fh:
        # write header if new file
        if not existing_lines:
            fh.write('# Raw Scryfall API Responses\n\n')
        else:
            fh.writelines(existing_lines)
        
        fh.write(f"## {name}\n\n")
        
        if data:
            fh.write(f"**Status:** Success\n\n")
            fh.write(f"**Scryfall URI:** {data.get('scryfall_uri', 'N/A')}\n\n")
            fh.write(f"**Response JSON:**\n\n")
            fh.write("```json\n")
            fh.write(json.dumps(data, indent=2, ensure_ascii=False))
            fh.write("\n```\n\n")
        else:
            fh.write(f"**Status:** Failed or Not Found\n\n")
        
        if urls:
            fh.write(f"**Attempted URLs:**\n\n")
            for u in urls:
                url_str = u.get('url')
                succ = u.get('success')
                sc = u.get('status_code')
                err = u.get('error')
                if succ:
                    fh.write(f"- {url_str} → **Success** (HTTP {sc})\n")
                else:
                    fh.write(f"- {url_str} → **Failed** ({err})\n")
        fh.write('\n')


def append_card_details(path: str, cache_dict: dict, not_found: list):
    """
    Write a complete card_details.md file (overwrites) using the current cache dict.
    The file will contain a markdown table of found cards and a "Not found" list below.
    Also include per-card detailed sections with constructed URLs and tried URL results.
    """
    # always rewrite the file to keep table and details consistent
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('# Card details (fetched from Scryfall)\n\n')
        # table header
        fh.write('| Name | uri | scryfall_uri | mana_cost | type_line | oracle_text | power | toughness | colors | color_identity | Tried URLs |\n')
        fh.write('|---|---|---|---|---|---|---|---|---|---|---|\n')

        # populate table rows for entries that have data
        for name in sorted(cache_dict.keys()):
            entry = cache_dict.get(name)
            if not entry or not isinstance(entry, dict) or not entry.get('data'):
                continue
            data = entry.get('data')
            urls = entry.get('urls') or []
            # sanitize fields to avoid breaking table
            def s(x):
                if x is None:
                    return ''
                txt = str(x)
                txt = txt.replace('\n', ' ').replace('\r', ' ').replace('|', '\\|')
                return txt
            uri = s(data.get('uri'))
            scryfall_uri = s(data.get('scryfall_uri'))
            mana_cost = s(mana_cost_to_text(data.get('mana_cost','')))
            type_line = s(data.get('type_line',''))
            oracle_text = s(convert_oracle_text(data.get('oracle_text','')))
            power = s(data.get('power') or '')
            toughness = s(data.get('toughness') or '')
            colors = s(colors_to_text(data.get('colors',[])))
            color_identity = s(colors_to_text(data.get('color_identity',[])))
            # join tried URLs into a single cell
            tried = []
            for u in urls:
                url = u.get('url') or ''
                succ = u.get('success')
                sc = u.get('status_code')
                err = u.get('error')
                if succ:
                    tried.append(f"{url} (OK {sc})")
                else:
                    tried.append(f"{url} (ERR {err})")
            tried_cell = s('; '.join(tried))
            fh.write(f"| {s(name)} | {uri} | {scryfall_uri} | {mana_cost} | {type_line} | {oracle_text} | {power} | {toughness} | {colors} | {color_identity} | {tried_cell} |\n")

        # list not found below the table as requested
        if not_found:
            fh.write('\n# Not found or errors\n\n')
            for n in not_found:
                fh.write(f"- {n}\n")
            fh.write('\n')

        # append detailed per-card sections (constructed urls and tried urls)
        for name in sorted(cache_dict.keys()):
            entry = cache_dict.get(name)
            fh.write(f"## {name}\n\n")
            data = None
            urls = []
            if isinstance(entry, dict):
                data = entry.get('data')
                urls = entry.get('urls') or []
            else:
                data = entry
            if not data:
                fh.write('- Not found on Scryfall or error occurred.\n\n')
            else:
                uri = data.get('uri')
                scryfall_uri = data.get('scryfall_uri')
                mana_cost = mana_cost_to_text(data.get('mana_cost',''))
                type_line = data.get('type_line','')
                oracle_text = convert_oracle_text(data.get('oracle_text',''))
                power = data.get('power') or ''
                toughness = data.get('toughness') or ''
                colors = colors_to_text(data.get('colors',[]))
                color_identity = colors_to_text(data.get('color_identity',[]))
                fh.write(f"- uri: {uri}\n")
                fh.write(f"- scryfall_uri: {scryfall_uri}\n")
                fh.write(f"- mana_cost: {mana_cost}\n")
                fh.write(f"- type_line: {type_line}\n")
                fh.write(f"- oracle_text: {oracle_text}\n")
                if power or toughness:
                    fh.write(f"- power/toughness: {power}/{toughness}\n")
                fh.write(f"- colors: {colors}\n")
                fh.write(f"- color_identity: {color_identity}\n\n")

            # always show the constructed request URLs so it's clear what would be called
            try:
                q_exact = urllib.parse.quote(name, safe='')
                q_fuzzy = urllib.parse.quote(name, safe='')
                constructed = [f"https://api.scryfall.com/cards/named?exact={q_exact}", f"https://api.scryfall.com/cards/named?fuzzy={q_fuzzy}"]
                fh.write('### Constructed request URLs\n\n')
                for cu in constructed:
                    fh.write(f"- {cu}\n")
                fh.write('\n')
            except Exception:
                # fallback - shouldn't happen
                pass

            # write tried urls if present (show results of actual HTTP attempts)
            if urls:
                fh.write('### Tried URLs (results)\n\n')
                for u in urls:
                    url_str = u.get('url')
                    succ = u.get('success')
                    sc = u.get('status_code')
                    err = u.get('error')
                    if succ:
                        fh.write(f"- {url_str} -> success (HTTP {sc})\n")
                    else:
                        fh.write(f"- {url_str} -> failed ({err})\n")
                fh.write('\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate moxfield_cards.md from CSV and Precons')
    parser.add_argument('--csv', default='moxfield_latest.csv')
    parser.add_argument('--precons', default='Precons')
    parser.add_argument('--out', default='moxfield_cards.md')
    parser.add_argument('--auto-threshold', type=float, default=0.90)
    parser.add_argument('--ambiguous-threshold', type=float, default=0.75)
    parser.add_argument('--card-details', default='card_details.md')
    parser.add_argument('--cache', default='scripts/cache/cards_cache.json')
    args = parser.parse_args()

    if not os.path.isfile(args.csv):
        print(f"CSV not found: {args.csv}")
        sys.exit(1)
    if not os.path.isdir(args.precons):
        print(f"Precons directory not found: {args.precons}")
        sys.exit(1)

    decks = read_precons(args.precons)
    rows = read_csv(args.csv)
    rows, heuristic, ambiguous = assign_precons(decks, rows, auto_thresh=args.auto_threshold, ambig_thresh=args.ambiguous_threshold)
    write_md(args.out, rows, decks, heuristic, ambiguous)
    print(f"WROTE {args.out}")

    # fetch card details from Scryfall and write responses incrementally to a raw responses file
    card_details_path = args.card_details
    raw_responses_path = 'scripts/cache/scryfall_raw_responses.md'
    successful_in_raw = read_successful_raw_responses(raw_responses_path)
    cache = {}
    if os.path.isfile(args.cache):
        try:
            with open(args.cache, encoding='utf-8') as fh:
                cache = json.load(fh)
        except Exception:
            cache = {}
    unique_names = sorted({r.get('Name','') for r in rows})
    # fetch names that are new OR have failed (not in successful list)
    to_fetch = [n for n in unique_names if n not in successful_in_raw]
    not_found = []
    
    if to_fetch:
        print(f"Fetching {len(to_fetch)} cards from Scryfall (skipping {len(successful_in_raw)} with successful prior fetches)...")
        for idx, name in enumerate(to_fetch, 1):
            print(f"  [{idx}/{len(to_fetch)}] {name}...")
            data, urls = scryfall_lookup(name, cache)
            if data is None:
                not_found.append(name)
            # write response incrementally as it comes back
            append_raw_response(raw_responses_path, name, data, urls)
            # 1 second delay between requests to avoid rate limiting
            time.sleep(1.0)
        
        print(f"WROTE {raw_responses_path}")
    else:
        print("All cards already fetched successfully from Scryfall. Skipping fetch.")
    
    # save cache
    os.makedirs(os.path.dirname(args.cache), exist_ok=True)
    try:
        with open(args.cache, 'w', encoding='utf-8') as fh:
            json.dump(cache, fh, ensure_ascii=False, indent=2)
    except Exception:
        pass
    
    # now create card_details.md from the cache
    append_card_details(card_details_path, cache, not_found)
    print(f"WROTE/UPDATED {card_details_path}")
