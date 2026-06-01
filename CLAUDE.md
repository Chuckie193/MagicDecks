# MagicDecks Project Instructions

## Repo Overview

See `.claude/REPO_GUIDE.md` for the full repo structure, file descriptions, workflow, and data sources. The sections below cover only what the guide doesn't.

---

## Card Pool

Two tiers of precon exist in this repo:

- **`Precons/Commander Precons/`** — Commander format precon decklists. Cards here may or may not be available for custom decks depending on what the user wants — always ask. When the user wants to preserve their Commander precons, use `non_commander_cards.md` as the eligible pool. When the user is happy to draw from everything, use `moxfield_latest.csv`.
- **`Precons/*.txt`** — Non-Commander precons and Secret Lair drops. Cards from these are always freely available and are already included in `non_commander_cards.md`.

---

## After Any Custom Deck Change

Whenever you make any change to a file in `Custom Decks/*.md` (adding, removing, or swapping cards; updating card descriptions; editing any section), run the following verification checks before reporting the task complete.

### 1. Decklist ↔ Card Collection Origin Table Sync

- Build the full card set from the decklist (Commander + all sections). Basic lands count as one entry (e.g., "Island", not "Island ×2").
- Build the card set from the Card Collection Origin table rows (strip copy-count suffixes, e.g., "Island (×2)" → "Island").
- Every card in the decklist must have a row in the table. Report and fix any missing.
- Every row in the table must correspond to a card in the decklist. Report and fix any extras.

### 2. Category Column Accuracy

Each card's **Category** in the table must show all supertypes and types from its `type_line` in `card_details.md` (omit subtypes — the part after the em-dash). Examples:
- `Artifact Creature — Thopter` → `Artifact Creature`
- `Legendary Artifact` → `Legendary Artifact`
- `Artifact — Vehicle` → `Artifact Vehicle`

### 3. Section Placement

Every non-land card must be in the correct deck section based on its `type_line` (use `card_details.md`). Priority order:

| Section | Rule |
|---|---|
| Creatures | `type_line` contains "Creature", "Vehicle", or "Space Station" |
| Enchantments | `type_line` contains "Enchantment" but NOT "Creature" |
| Artifacts & Mana | `type_line` contains "Artifact" but NOT "Creature", "Vehicle", "Space Station", or "Enchantment" |
| Instants | `type_line` contains "Instant" — never "Sorcery" |
| Sorceries | `type_line` contains "Sorcery" — never "Instant" |
| Planeswalkers | `type_line` contains "Planeswalker" |

Fix any card whose section contradicts its type_line before finishing.

### 4. Moxfield Export Sync

After every change to a `Custom Decks/*.md` file, update the corresponding `Custom Decks/Moxfield/*.txt` file to match. The `.txt` file must reflect the exact same 100-card list.

- Use the **alt name** for any card that has one (check the `Alt Name(s)` column in `moxfield_cards.md`) — e.g., use `Air Shoes` not `Swiftfoot Boots`. If no alt name exists, use the real card name.

### 5. Card Count and Format Rules

- The deck must contain **exactly 100 cards** at all times (1 commander + 99 others). Any swap must be 1-for-1.
- **No duplicate non-basic cards** — every non-basic card must appear exactly once (singleton format).
- **Color identity compliance** — every card added must be within the commander's color identity. Check `color_identity` in `card_details.md` if unsure.

### 6. Card Collection Origin Table Sort Order

The table must remain sorted correctly after any change:
- **Group by precon**: order groups by how many deck cards each precon contributes (largest first). Cards with no precon (`—`) form the final group.
- **Within each group, sort by card type** in this order: Creature → Enchantment → Artifact → Instant → Sorcery → Planeswalker → Land.
- **Within the same type, sort alphabetically** (by alt name if one exists, otherwise by card name).
- The Commander row is always first, before all groups.

### 7. Versioning

Do **not** increment the deck version (Draft → v1, v1 → v1.1, etc.) unless the user explicitly asks to lock or approve the deck. During iteration, keep overwriting the draft file.

### 8. Ignore Old Folders

Never read, reference, or suggest cards from any file inside a folder named `Old` (e.g., `Custom Decks/Old/`). Treat these files as if they do not exist.
