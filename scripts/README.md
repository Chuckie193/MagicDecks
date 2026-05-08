generate_cards_md.py — usage

## What it does
1. Parses `moxfield_latest.csv` and Precon deck files
2. Matches cards to precons (exact, alt-name, fuzzy matching)
3. Generates `moxfield_cards.md` with card table + per-precon reports
4. Fetches card details from Scryfall API (incremental, skips already-fetched)
5. Writes raw Scryfall JSON to `scryfall_raw_responses.md` as responses arrive
6. Generates `card_details.md` with a summary table (name, URI, mana cost in plain English, type, colors, etc.)
7. Caches all Scryfall responses locally in `scripts/cards_cache.json` to avoid redundant API calls

## Prerequisites
- Python 3.8 or newer (no external packages required — script uses only the standard library)

## Files expected
- `moxfield_latest.csv` (default: repo root). Use `--csv` to specify a different path.
- `Precons/` (directory of .txt files). Each .txt: one card per line, optional leading quantity (e.g., "2 Island"), optional first line ending with ":" to set the deck title. Supports alt names in square brackets, e.g., `Card Name [Alt Name]`

## Run (from repo root)
```
py -3 .\scripts\generate_cards_md.py --csv moxfield_latest.csv --precons Precons --out moxfield_cards.md --card-details card_details.md --cache scripts/cards_cache.json
```

Or with python on PATH:
```
python scripts\generate_cards_md.py --csv moxfield_latest.csv --precons Precons --out moxfield_cards.md --card-details card_details.md --cache scripts/cards_cache.json
```

## Options
- `--csv PATH` (default: moxfield_latest.csv)
- `--precons PATH` (default: Precons)
- `--out PATH` (default: moxfield_cards.md) — precon mapping table
- `--card-details PATH` (default: card_details.md) — Scryfall data summary table
- `--cache PATH` (default: scripts/cards_cache.json) — local Scryfall response cache
- `--auto-threshold FLOAT` (default: 0.90) — similarity above this auto-assigns heuristics
- `--ambiguous-threshold FLOAT` (default: 0.75) — similarity between this and auto is marked ambiguous

## Output files
- **moxfield_cards.md** — Card table (Name, Edition, Count, Precon, Duplicate) + per-precon reports
- **scryfall_raw_responses.md** — Full raw JSON responses from Scryfall API for each card (incremental writes, with attempted URLs and success/fail status)
- **card_details.md** — Summary markdown table with Scryfall data formatted in plain English:
  - Mana cost (e.g., "1 generic, Blue, Red")
  - Colors/color identity (e.g., "Blue, Red")
  - Type line, oracle text, power/toughness
  - URI and Scryfall URI
- **scripts/cards_cache.json** — Local cache of Scryfall responses (avoids redundant API calls)

## Caching & skipping
- Cards already in `card_details.md` or `scryfall_raw_responses.md` are skipped on subsequent runs
- All Scryfall responses are cached locally; re-running the script will only fetch new cards
- This helps avoid HTTP 429 (rate limit) errors

## Troubleshooting
- **"python" or "py" not found:** Install Python from https://python.org or use the Microsoft Store on Windows.
- **Encoding errors:** Script uses UTF-8. In PowerShell, set: `$env:PYTHONIOENCODING='utf-8'` before running.
- **HTTP 429 (rate limit) errors:** Scryfall has request limits. The script includes sleep delays between requests. If you see 429s, re-run later or wait a few hours before a fresh fetch.
- **Card not found on Scryfall:** Some cards (especially Secret Lair custom or localized versions) may not be in Scryfall. These are listed in the "Not found or errors" section at the bottom of `card_details.md`.

## Git workflow
```
git add moxfield_cards.md scryfall_raw_responses.md card_details.md scripts/cards_cache.json
git commit -m "Update card details and Scryfall responses"
```
Or skip the cache if you prefer not to commit it:
```
git add moxfield_cards.md scryfall_raw_responses.md card_details.md
git commit -m "Update card details and Scryfall responses"
```