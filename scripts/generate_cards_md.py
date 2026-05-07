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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate moxfield_cards.md from CSV and Precons')
    parser.add_argument('--csv', default='moxfield_latest.csv')
    parser.add_argument('--precons', default='Precons')
    parser.add_argument('--out', default='moxfield_cards.md')
    parser.add_argument('--auto-threshold', type=float, default=0.90)
    parser.add_argument('--ambiguous-threshold', type=float, default=0.75)
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
