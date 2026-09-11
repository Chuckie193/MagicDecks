# Limit Break — Precon Analysis & Suggested Changes

**Precon:** *Limit Break* (Commander: Final Fantasy, released June 13, 2025)
**Commanders:** Cloud, Ex-SOLDIER // Tifa, Martial Artist (Partner)
**Color Identity:** Naya (White / Red / Green)
**Strategy:** Equipment-matters go-wide aggro. Rather than stacking every piece of gear onto one Voltron threat, the deck wants **multiple equipped creatures attacking at once** — combat-damage triggers (Cloud's own ability, Buster Sword's free-spell trigger, Mask of Memory, Ohran Frostfang) all pay off per attacker, so spreading Equipment across the board out-values concentrating it on a single body.

This document is **analysis only** — it does not touch anything in `Custom Decks/`, `moxfield_latest.csv`, or any other repo file. Limit Break is not in this collection.

---

## Sourcing & Methodology (read this first)

Every direct deck-list host (Moxfield, MTGGoldfish, EDHREC, Archidekt, Playgroup.gg, Draftsim, Card Kingdom, Gathering Games UK, mtg.wtf, magicprecons.com, web.archive.org, etc.) was **network-blocked** in this environment — every fetch attempt returned `EGRESS_BLOCKED` or an equivalent refusal. It was not possible to pull the verbatim, official 100-card list.

Instead, this analysis is built from:
1. **Search-result snippets** naming specific cards and EDHREC's published "community cut rate" percentages for this precon. A card appearing with a cut rate is, by construction, confirmed to be in the real original decklist — you can't cut what isn't there.
2. **This repo's own reference material** — `Commander Staples/General Staples.md`, `Mono-White.md`, `Mono-Red.md`, `Mono-Green.md`, `White-Red.md`, `Red-Green.md`, `White-Green.md`, and `Archetypes/Equipment-Voltron.md` — for the "what to add" side.
3. **Cross-referencing two of this repo's own homebrew decks** that share two of Limit Break's three colors: `Custom Decks/Jacked_Rabbits_Deck.md` (Green/White) and `Custom Decks/Claws_for_Concern_Deck.md` (Red/Green), both of which independently run several of the same Equipment/protection pieces recommended below.

Community cut-rate percentages should be read as **directionally reliable, not exact** — they were relayed through search summaries rather than the live page.

---

## Review Process

Three independent review rounds were run against successive drafts (v1 → v2 → v3), each by a fresh reviewer with no memory of prior rounds' reasoning, specifically to stress-test calls rather than rubber-stamp them:

- **Round 1** caught that the v1 draft was about to cut **Mask of Memory** (a good on-theme card, not actually weak) and swap in a poor fit (**Xenagos, God of Revels** — single-target, not a "reward the wide board" card). It added **Puresteel Paladin** and **Lightning Greaves** from this repo's own `Equipment-Voltron.md`, which the draft had cited as a source but not actually mined fully.
- **Round 2** independently re-checked Round 1's calls and **reversed** the decision to keep **Skullclamp** — Round 1's "good in go-wide decks" logic was built on an aristocrats assumption this deck doesn't share. Round 2 also made the final call to keep **Harmonize** cut (the add list already covers card draw with three on-theme, attack-triggered sources) rather than leaving it an open question.
- **Round 3** gave final sign-off, sharpened the Skullclamp reasoning further (it actively fights **Ohran Frostfang** and **Puresteel Paladin**, which both need the equipped creature to *survive*), and flagged one advisory: the cut list removes four creatures (Barret Wallace, Heidegger, Cait Sith, Elena) while the add list — at that point — added none, which matters more than usual in a "win by attacking with many bodies" deck.

That last advisory is addressed below: **Bruenor Battlehammer** replaces **Beast Within** in the final add list (removal was redundant with Generous Gift; a creature that makes your first equip each turn free and pumps equipped creatures was a better use of the slot). Net creature count change is now −1 (four filler creatures out, three creatures in: Puresteel Paladin, Ardenn, Bruenor), not −4.

---

## Cards to Cut (17)

All independently confirmed via EDHREC's published "most commonly cut from this precon" data.

| Card | Community Cut Rate | Why it's weak here |
|---|---|---|
| Summon: Kujata | 79% | Expensive, clunky payoff unrelated to the equipment plan. |
| Furious Rise | 73% | Slow value engine that doesn't advance the go-wide attack plan. |
| Avalanche of Sector 7 | 72% | Narrow/situational; low impact per mana. |
| Heidegger, Shinra Executive | 70% | Filler body, no equipment synergy. |
| Hellkite Tyrant | 69% | A "steal one big thing" finisher — fights the deck's own "spread gear across many bodies" identity, the same way Skullclamp does. |
| Explorer's Scope | 63% | Weak scry-adjacent equipment with no real payoff. |
| Barret Wallace | 59% | Generically weak filler creature. |
| Skullclamp | ~59–65% (see note below) | Wants the wearer to die; directly contradicts Ohran Frostfang and Puresteel Paladin, both of which need the equipped creature alive and reconnecting. This deck is equip-and-attack, not aristocrats/sac-fodder. |
| Secret Rendezvous | 56% | Symmetrical draw that helps opponents just as much. |
| Ultimate Magic: Meteor | 55% | Clunky, high-cost payoff without enough backup. |
| SOLDIER Military Program | 55% | Filler value creature, no equipment tie-in. |
| Cait Sith, Fortune Teller | 54% | Generically weak filler creature. |
| Decimate | 51% | Needs a legal target in all four categories simultaneously — too conditional next to Swords to Plowshares/Generous Gift/Chaos Warp. |
| Harmonize | 47% | Sorcery-speed draw-3 costs a full turn's development in an aggro curve; the add list already covers card advantage with three attack-triggered sources that don't cost tempo (Mask of Memory, Ohran Frostfang, Puresteel Paladin). |
| Armory Automaton | 45% | Vanilla-ish artifact body, low impact. |
| Elena, Turk Recruit | 44% | Generically weak filler creature. |
| Bronze Guardian | 40% | Vanilla artifact beater, replaceable. |

### Explicitly kept despite a notable community cut rate
- **Mask of Memory** (42% community cut rate) — considered for the cut list, deliberately **kept**. The aggregate cut rate is dragged down by pilots running Cloud as a single-Voltron piece, where a second equipment slot competing for one attacker is marginal. This build's actual plan — gear spread across many attackers — gives Mask of Memory many more trigger opportunities per turn than the average build the community data is averaged over.

---

## Cards to Add (17)

Sourced from this repo's `Commander Staples/` files and cross-referenced against `Jacked_Rabbits_Deck.md` and `Claws_for_Concern_Deck.md`.

**Ramp & Fixing**
- **Sol Ring** — auto-include, `General Staples.md`.
- **Arcane Signet** — auto-include, `General Staples.md`.
- **Command Tower** — auto-include, `General Staples.md`.

**Removal**
- **Swords to Plowshares** — one-mana exile, `Mono-White.md`.
- **Generous Gift** — unconditional answer to any permanent, `Mono-White.md`.
- **Chaos Warp** — catch-all answer including things red normally can't touch, `Mono-Red.md` / `General Staples.md`.

**Equipment Package**
- **Hammer of Nazahn** — auto-attaches itself and every future Equipment for free; the single best fit for "get gear onto multiple bodies fast," `Equipment-Voltron.md`.
- **Ardenn, Intrepid Archaeologist** — moves any number of Equipment (and Auras) for free at combat start — directly enables redistributing gear across the team turn after turn instead of leaving it stacked on one creature, `Equipment-Voltron.md`.
- **Open the Armory** — tutors any Equipment or Aura to hand, `Equipment-Voltron.md` (also run in `Jacked_Rabbits_Deck.md`).
- **Puresteel Paladin** — free equip once you control 3+ artifacts, draws a card whenever Equipment enters, `Equipment-Voltron.md`.
- **Bruenor Battlehammer** — first equip each turn is free, and equipped creatures get +2/+0; a creature (not just support), addressing the round-3 advisory about net creature count, `Equipment-Voltron.md`.

**Protection** (meets `Equipment-Voltron.md`'s own "run at least three protection spells" rule)
- **Swiftfoot Boots** — equip 1, haste + hexproof, still targetable by you.
- **Lightning Greaves** — equip 0, haste + shroud, cheapest protection available.
- **Heroic Intervention** — hexproof + indestructible for the whole board; the answer to a wrath that would otherwise blow out a wide equipped attack.

**Payoffs**
- **Ohran Frostfang** — deathtouch + draw a card whenever the wearer deals combat damage to a player; `Red-Green.md` names this card specifically as the fix for RG's weakest axis (card advantage).
- **Blade of Selves** — Myriad copies an attacking creature once per opponent, multiplying every combat-damage trigger (Cloud's ability, Mask of Memory, Ohran Frostfang) across the copies. **Caveat: dead in true 1v1** (Myriad triggers "for each opponent other than the defending player," which is zero at 1v1) — this is a multiplayer-pod card, matching the precon's primary intended format. For a dedicated 1v1 build, swap in **Sword of Vengeance** instead (`Equipment-Voltron.md`).

**Land**
- **Kessig Wolf Run** — colorless mana-sink finisher land: pump and trample for any creature, scaling with mana invested, `Red-Green.md`.

---

## Net Summary

- **17 cards out**, all independently confirmed as the precon's weakest slots by community upgrade data.
- **17 cards in**, chosen specifically to reinforce "equip multiple creatures, attack wide, cash in combat-damage triggers" rather than generic goodstuff — every add either tutors/attaches Equipment, protects the board, or pays off combat damage from **multiple** attackers.
- Net creature count change: **−1** (four filler creatures cut; three creatures added back: Puresteel Paladin, Ardenn, Bruenor Battlehammer).
- Removal count held steady at three efficient, unconditional pieces (Swords to Plowshares, Generous Gift, Chaos Warp) rather than four with overlap, freeing the slot for Bruenor Battlehammer.

## Caveats

- The exact original 100-card list could not be verified verbatim due to network restrictions in this session — see **Sourcing & Methodology** above. Before actually building this, cross-check the real decklist (e.g. from the physical product or a deck-list site) against the cut list here to confirm each named cut card is genuinely present.
- This analysis does not check card ownership, `reserved_decks.md`, or `non_commander_cards.md` — Limit Break is not in this collection, so none of the repo's card-pool rules apply here.
