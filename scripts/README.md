generate_cards_md.py — usage

Prerequisites
- Python 3.8 or newer (no external packages required — script uses only the standard library).

Files expected
- moxfield_latest.csv (default: repo root). Use --csv to specify a different path.
- Precons/ (directory of .txt files). Each .txt: one card per line, optional leading quantity (e.g., "2 Island"), optional first line ending with ":" to set the deck title.

Run (from repo root)
- Windows (PowerShell or CMD):
  py -3 .\scripts\generate_cards_md.py --csv moxfield_latest.csv --precons Precons --out moxfield_cards.md
- Or with python on PATH:
  python scripts\generate_cards_md.py --csv moxfield_latest.csv --precons Precons --out moxfield_cards.md

Options
- --auto-threshold FLOAT  (default 0.90)  # similarity above this auto-assigns heuristics
- --ambiguous-threshold FLOAT (default 0.75)  # similarity between this and auto is marked ambiguous

Output
- Overwrites (or creates) the specified output markdown file (default: moxfield_cards.md). The file contains a table (Name, Edition, Count, Precon, Duplicate) and per-precon reports.

Troubleshooting
- If "python" or "py" not found, install Python from https://python.org or use the Microsoft Store on Windows.
- Script uses UTF-8. In PowerShell, you can set: $env:PYTHONIOENCODING='utf-8' before running if you see encoding errors.

Git
- After generating: git add moxfield_cards.md && git commit -m "Regenerate moxfield_cards.md"

Questions
- Want this as a committed README or a short wiki entry instead?  