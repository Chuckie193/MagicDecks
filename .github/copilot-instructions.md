# Copilot instructions for MagicDecks

Purpose
- Describe repository contents and signals useful to Copilot sessions.

Build / Test / Lint
- No build, test, or lint scripts detected in the repository root.
- There is no package.json, pyproject.toml, or other language project file. This repo currently contains a single data export: `moxfield_latest.csv`.
- If code/tests are added later, include standard scripts (e.g., `npm test`, `pytest`, `dotnet test`) and update this file.

High-level architecture
- Single CSV dataset exported from Moxfield (file: `moxfield_latest.csv`).
- Primary columns (header row):
  - Count — number of copies owned (integer string)
  - Tradelist Count — tradelist copies (integer string)
  - Name — card name (string, may include "/" and punctuation)
  - Edition — short edition code (e.g., soc, fdn, blc, eoc)
  - Condition — text like "Near Mint"
  - Language — language string (English)
  - Foil — either blank or the string "foil"
  - Tags — freeform tags (often empty)
  - Last Modified — timestamp (YYYY-MM-DD HH:MM:SS.ffffff)
  - Collector Number — numeric-ish string
  - Alter — boolean-like string ("False"/"True")
  - Proxy — boolean-like string ("False"/"True")
  - Purchase Price — numeric string or empty
- Expect duplicates of Name across different Edition values; treat each row as one card entry.

Key conventions / notes for Copilot
- CSV is double-quoted and comma-separated; preserve quoting when parsing.
- Boolean fields are stored as string literals "False"/"True" — do not assume native booleans until converted.
- Empty cells are represented by an empty string between quotes.
- Timestamps include microseconds; parse as UTC/local depending on downstream code.
- Edition codes are short lowercase strings; map to readable edition names externally if needed.
- Price values are strings that may be empty; coerce to float only after checking non-empty.

Files of interest
- moxfield_latest.csv — main dataset. No other source code or configs were detected.

AI / Assistant config checks
- No existing Copilot/Claude/Cursor/Aider/etc. assistant rules or AI config files found (CLAUDE.md, .cursorrules, CONVENTIONS.md, etc.).

Suggested Copilot prompts (examples)
- "List top 20 cards by Purchase Price from moxfield_latest.csv"
- "Convert moxfield_latest.csv to JSON with fields: name, edition, count, price"
- "Find cards with Foil==\"foil\" and Purchase Price > 0.1"

When adding code
- Place production code under a top-level `src/` and tests under `tests/` or language-appropriate layout; add project metadata so Copilot can infer build/test commands.

---
Last updated: 2026-05-07
