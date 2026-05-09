# MagicDecks Claude Skills

This directory contains custom Claude Code skills for the MagicDecks project.

## Available Skills

### `/generate-deck` - Commander Deck Generator

Generates a 100-card Commander/EDH deck from your card collection based on themes, colors, or a specific commander.

**Usage Examples**:

```
/generate-deck elf tribal in green and white
/generate-deck Grixis control
/generate-deck with Atraxa as commander
/generate-deck mono-black aristocrats
/generate-deck Simic +1/+1 counters
```

**What it does**:
- Reads your card collection from `moxfield_latest.csv`
- Analyzes card details from `card_details.md`
- Generates a legal 100-card Commander deck
- Validates Commander format rules
- Creates detailed markdown file with:
  - Strategy explanation
  - Card synergies
  - Mana curve analysis
  - Cards grouped by category
  - Strengths/weaknesses analysis
  - Missing staples warnings

**Output**: Saves deck to `Custom Decks/[deck-name].md`

**Versioning**:
- Draft decks (working versions): `[Deck Name].md`
- Locked v1 (approved): `[Deck Name] v1.md`
- Incremental updates: `[Deck Name] v1.1.md`, `[Deck Name] v1.2.md`
- During iteration, the draft is overwritten until you say "lock this in" or "I'm happy with this"
- Locked versions are preserved and won't be modified

**Requirements**:
- Must have `moxfield_latest.csv` with your card collection
- Must have run `generate_cards_md.py` to populate `card_details.md`
- Deck uses ONLY cards from your collection

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

## How to Use Skills

In Claude Code, simply type `/generate-deck` followed by your deck request:

```
/generate-deck [your deck description here]
```

The skill will automatically read your collection and generate an appropriate deck.
