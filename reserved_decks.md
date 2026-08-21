# Reserved Decks

Decks that are **physically assembled and sleeved right now**. Their cards are in use and must not be pulled into a new build.

This is the source of truth for the "Avoid reserved decks" card-pool option in the `/generate-deck` skill. Edit it by hand whenever you build or dismantle a deck — nothing generates it.

## Currently reserved

| Deck | List file | Notes |
|------|-----------|-------|
| Full Deployment | `Custom Decks/Moxfield/Full_Deployment_Deck.txt` | Custom deck — Inspirit, Flagship Vessel |
| Squirreled Away | `Precons/Commander Precons/SquirreledAway.txt` | Commander precon — Hazel of the Rootbloom |
| Dance of the Elements | `Precons/Commander Precons/DanceOfTheElements.txt` | Commander precon — Ashling, the Limitless |

---

## How to use this file

**Spare copies are still available.** Reserving a deck reserves *the physical copies that deck uses*, not the card name. If you own three Sol Rings and one is in a reserved deck, two remain available.

Compute the eligible pool as a per-card-name subtraction:

```
available[card] = total owned in moxfield_latest.csv
                − sum of counts for that card across every reserved list above
```

Keep only cards where `available > 0`, and never use more copies of a card than `available`.

**Rules when doing the subtraction:**

- **Resolve alt names first.** Custom-deck exports use the alt name where one exists (e.g. `Air Shoes` for Swiftfoot Boots, `Power Sneakers` for Lightning Greaves). Map them back to the real card name via the `Alt Name(s)` column in `moxfield_cards.md` before subtracting, or the reservation will silently miss.
- **Strip set codes and foil markers** from precon lines — `1 Sol Ring (BLC) 129` and `1 Hazel of the Rootbloom (BLC) 2 *F*` are both one copy.
- **Basic lands subtract too**, and precon files often list them across several rows (`5 Forest`, `4 Forest`) — sum them.
- **A reserved custom deck's `.txt` in `Custom Decks/Moxfield/` is the authoritative list**, not its `.md`, since the `.txt` is the exact 100-card import list. If a reserved custom deck has no `.txt` export, parse its `.md` decklist sections and say so.
- **A reserved Commander precon's `.txt` is what the precon shipped with.** If it has since been upgraded in paper, the list is stale — worth flagging rather than assuming.
- **Sanity check**: after parsing, any reserved card name that does not appear in `moxfield_latest.csv` means a parsing or alt-name failure, not a genuinely missing card. Investigate before trusting the pool.

### `non_commander_cards.md` does not know about this file

The two filters are independent and must be **composed**, not chosen between:

| Pool option | Formula |
|---|---|
| No Commander-precon cards | `min(non_commander_cards.md Copies, owned − reserved)` |
| Avoid reserved decks | `owned − reserved` |
| Full collection | `owned` |

`non_commander_cards.md` excludes cards committed to a Commander precon and nothing else — it will happily list a card that is physically sleeved in a reserved *custom* deck. As of 2026-08-20, **13 of its entries are copies living in Full Deployment, 12 of them with zero free copies** (Swiftfoot Boots, The Ozolith, Sami's Ship's Engineer, Palladium Myr, Fabricate, Cryogen Relic, Galvanizing Sawship, Frontline War-Rager, Starport Security, The Seriema, Raugrin Triome, Seachrome Coast; Banishing Light is listed at 3 with only 2 free).

So the strictest-*sounding* option is not automatically the strictest. Always apply the reserved subtraction on top.

## When a deck is dismantled

Delete its row from the table above. Its cards immediately become available again, and any deck built while it was reserved may be worth revisiting — a deck file's "Cards Removed from Original" table records what was cut for availability rather than for power.
