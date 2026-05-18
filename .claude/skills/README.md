# MagicDecks Claude Skills

This directory contains custom Claude Code skills for the MagicDecks project.

## Available Skills

### `/generate-deck` - Commander Deck Generator

Generates a 100-card Commander/EDH deck from your card collection. Works in two modes: **fresh build** or **precon/existing deck improvement**.

---

### Fresh Build

Build a new deck from scratch based on a theme, color identity, or specific commander.

**Usage Examples**:

```
/generate-deck elf tribal in green and white
/generate-deck Grixis control
/generate-deck with Atraxa as commander
/generate-deck mono-black aristocrats
/generate-deck Simic +1/+1 counters
```

---

### Precon / Existing Deck Improvement

Start from a preconstructed deck (`Precons/`) or an existing custom deck (`Custom Decks/`) and upgrade it. The skill retains cards that work well and replaces weaker ones with better options from your collection.

**Trigger phrases**: "improve", "upgrade", "fix", "based on", "starting from", "build from", or naming a known precon/deck.

**Usage Examples**:

```
/generate-deck improve CounterIntelligence precon
/generate-deck upgrade Bria deck
/generate-deck build from OtterLimits with a token strategy
/generate-deck fix the Inspirit deck
```

**When improving a deck, the output includes a "Cards Removed from Original" table** listing every card cut from the base deck, the reason it was removed, and what replaced it (if a direct swap was made).

---

### What the skill produces

- Reads your card collection from `moxfield_latest.csv`
- Analyzes card details from `card_details.md`
- Generates a legal 100-card Commander deck using only owned cards
- Validates Commander format rules (color identity, singleton, etc.)
- Creates a detailed markdown file in `Custom Decks/` with:
  - Strategy overview and intended play style
  - Lore blurb and suggested deck names
  - Cards grouped by category with explanations
  - Key synergies
  - **Cards Removed from Original** *(improvement mode only)*
  - Tokens generated table
  - Mana curve
  - Mulligan and play notes
  - Strengths/weaknesses analysis
  - Card Collection Origin table (which precon each card came from)
- Creates a Moxfield import file in `Custom Decks/Moxfield/`

**Requirements**:
- `moxfield_latest.csv` must exist (your Moxfield collection export)
- `card_details.md` must exist (run `generate_cards_md.py` to generate it)
- All cards in the deck must be in your collection

---

## Versioning

- **Draft** (working version): `Custom Decks/[Deck Name].md` — overwritten during iteration
- **Locked v1** (first approval): `Custom Decks/[Deck Name] v1.md` — preserved forever
- **Incremental updates**: `v1.1`, `v1.2`, etc. — each approval creates the next increment
- Say "lock this in" or "I'm happy with this" to promote a draft to a locked version

---

## Deck Iteration Workflow

1. **Generate initial deck**: `/generate-deck elf tribal`
   - Creates: `Custom Decks/Elf Tribal.md` (draft)

2. **Request changes**: "Add more removal" or "Replace X with Y"
   - Updates: `Custom Decks/Elf Tribal.md` (overwrites draft)

3. **Lock when satisfied**: "Lock this in" or "This looks great"
   - Renames to: `Custom Decks/Elf Tribal v1.md` (locked)

4. **Future changes**: "Update my elf deck to include more card draw"
   - Creates: `Custom Decks/Elf Tribal.md` (new draft)
   - Iterate until satisfied
   - Lock as: `Custom Decks/Elf Tribal v1.1.md` (preserves v1)

---

## How to Use Skills

In Claude Code, type `/generate-deck` followed by your request:

```
/generate-deck [your deck description here]
```
