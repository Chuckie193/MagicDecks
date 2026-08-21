# Commander Staples (Reference Only)

A **personal reference library** of well-known Commander/EDH staple cards, organized by color and by deck archetype. It exists purely as a quick lookup for when building or upgrading a [`Custom Decks`](../Custom%20Decks) list — it is **not** a source of truth for what's owned, and it is **not** wired into `/generate-deck` or any script.

## What's here

| File(s) | Contents |
|---|---|
| `General Staples.md` | Colorless/universal staples that slot into almost any deck. |
| `Mono-White.md`, `Mono-Blue.md`, `Mono-Black.md`, `Mono-Red.md`, `Mono-Green.md` | Single-color staples. Where the bulk of each color's iconic cards live. |
| `White-Blue.md` … `Red-Green.md` (10 files) | One per two-color combination — **gold (multicolor) cards and that pair's mana fixing only**. Mono-colored cards are not repeated here; check the two relevant mono files as well. |
| `Archetypes/` | Staples grouped by deck strategy (tokens, +1/+1 counters, counterspells/control, sacrifice, reanimator, spellslinger, equipment/voltron, artifacts, lifegain, landfall). |

Files are named and labeled by their **colors** (e.g. "Blue-Black"), not by guild name (e.g. "Dimir").

## Price legend

Every card lists its mana cost in plain English and an approximate EUR price:

| Marker | Meaning |
|---|---|
| `€1.21 ✓` | **Exact** price, pulled from `scripts/cache/cards_cache.json` (the printing owned, as of the last cache refresh). |
| `~€4 💛` | **Estimated** price — no cached data, figure is a rough guess. |
| 💚 | Budget — under €3 |
| 💛 | Mid — €3–€10 |
| 🔴 | Premium — over €10. These carry a **Cheaper alternatives** note. |

> [!IMPORTANT]
> Only figures marked ✓ are real. Everything else is an **estimate** and should be verified before buying — MTG prices move constantly and reprints can crater a card overnight.

### Refreshing prices with real data

This environment can't reach Scryfall, so most prices here are estimates. Run this **locally** to replace every estimate with a live EUR figure and re-tier the 🔴 cards:

```bash
python scripts/add_staple_prices.py
```

It reads each `Commander Staples/**/*.md`, looks up every card in the local Scryfall cache (falling back to the Scryfall API for cache misses, cheapest non-foil printing), rewrites the Price column in place, and updates the cache so repeat runs are fast. Pass `--dry-run` to preview changes.

## Important caveats

- **Not a shopping list and not a collection check.** A card appearing here says nothing about whether it's owned, reserved in a physically-assembled deck, or locked in a Commander precon. Always cross-reference `moxfield_latest.csv`, `reserved_decks.md`, and `non_commander_cards.md` per the card-pool rules in `CLAUDE.md` before adding one of these to a deck.
- **Curated, not exhaustive.** A starting point for "what should I consider," not a complete power ranking. Prune and extend over time.
- **Color-pair files are gold-only.** Building White-Blue? Read `White-Blue.md` *plus* `Mono-White.md` and `Mono-Blue.md`.
