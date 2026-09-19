# Hoard Mentality — Rakdos Dragons & Treasure Commander

Commander: Smaug the Impenetrable ({5}{B}{R}, Black/Red)

## Overview
- **Strategy**: Smaug is an 8/7 flying, **indestructible**, hasty Dragon who turns every point of *noncombat* damage he takes into a Treasure token. Because he survives damage that kills everything else, the deck aims damage at its own commander on purpose: **Blasphemous Act** deals 13 to every creature, wipes the pod's board, and hands you thirteen Treasures to rebuild with while everyone else is empty. Eleven cards can put noncombat damage on him, so this is the main line, not a lucky one. The Treasures cast the Dragons; **Exsanguinate** turns a surplus hoard into simultaneous damage to all three opponents; and **Perforating Artist** drains 9 a turn in the background as long as Smaug keeps attacking.
- **Ceiling**: **Dawnsire, Sunstar Dreadnought** is the best-case upgrade rather than the plan — a 1-of you'll see in roughly 20–30% of games (Hoarding Dragon can tutor it). When it lands it converts the one-shot Treasure burst into a repeating one at 100 a combat. Only it and Coretapper care that it exists; nothing else in the deck is built around it.
- **Intended for**: Multiplayer pod — three real sweepers, per-opponent drain, a repeatable edict, and a commander who survives damage-based wraths.
- **Card pool**: Full collection (`moxfield_latest.csv`), **plus Dawnsire, Sunstar Dreadnought**, which the user is acquiring and which does not appear in the collection export.

## Lore

Spears glance off. Arrows shatter. The mountain's king barely stirs — every wound they open only buries him deeper in gold. He yawns, and the valley learns what a bad investment looks like. *Try again, little thieves.*

---

## Decklist (100 cards)

### Commander (1)
- **Smaug the Impenetrable** — {5}{B}{R} 8/7, flying, indestructible, haste. **Whenever he is dealt noncombat damage, create that many Treasure tokens.** Indestructible stops destruction and lethal damage, so damage-based wraths leave him standing and pay you for the privilege. It does **not** stop -X/-X, exile, or sacrifice effects.

### Creatures (23)
- **Dragonmaster Outcast** — {R} 1/1 that makes a 5/5 flying Dragon every upkeep once you control six or more lands.
- **Coretapper** — {2} 1/1 Myr. `{T}`: charge counter on target artifact; sacrifice it for two. It accelerates **Dawnsire** to its 10+ threshold and **Lux Cannon** to its destroy mode.
- **Dragonlord's Servant** — {1}{R}. Dragon spells cost {1} less — including Smaug himself.
- **Academy Manufactor** — {3}. Every Clue, Food or Treasure you would create becomes one of each. This triples the **token count**, not the mana: you still get one Treasure per Treasure, but each now also brings a Clue and a Food for Idol of Oblivion, Storm-Kiln Artist and Deadly Dispute.
- **Perforating Artist** — {1}{B}{R} Devil with deathtouch. **Raid** — at the beginning of your end step, if you attacked this turn, each opponent loses 3 life unless they sacrifice a nonland permanent. Smaug has haste and attacks every turn, so raid is always on: **9 life or 3 permanents per turn** across the pod. It is simultaneously the deck's repeatable reach and its only recurring edict, which is how you answer a hexproof or indestructible threat.
- **Dori, Bearer of Friends** — {2}{R} 3/3 trample that brings a Treasure with it.
- **Firespitter Whelp** — {2}{R} 2/2 flying Dragon that pings **each opponent** whenever you cast a noncreature *or* Dragon spell — 54 of the 62 nonland cards, the best-supported trigger in the deck.
- **Midnight Reaper** — {2}{B}. A card every time a nontoken creature you control dies; it deals you 1 each time.
- **Morbid Opportunist** — {2}{B}. Draws once each turn that one or more **other** creatures die. Its own death to your sweeper draws nothing.
- **Ill-Tempered Loner // Howlpack Avenger** — {2}{R}{R} 3/3. **"Whenever this creature is dealt damage, it deals that much damage to any target."** Every sweeper now hits twice: Blasphemous Act deals it 13, and it throws 13 at a face or back at Smaug for 13 more Treasures. The night face, Howlpack Avenger, upgrades this to *any permanent you control* being damaged.
- **Immersturm Predator** — {2}{B}{R} flying Vampire Dragon. Grows whenever it becomes tapped, and sacrificing **another** creature makes it indestructible and taps it — re-triggering its own counter. Survives your own Blasphemous Act.
- **Manaform Hellkite** — {2}{R}{R} 4/4 flying Dragon. Every noncreature spell makes an X/X flying hasty Dragon token where X is the mana spent, exiled at the next end step. Treasures make X large, and you can Station the token before it disappears.
- **Smaug the Magnificent** — {2}{R}{R} 4/3 flying haste. A Treasure every upkeep, and on attack deals damage equal to your Treasure count to **any target** — the only *repeatable* way to damage your own Smaug before Dawnsire arrives.
- **Solemn Simulacrum** — {4}. Ramp on entry, a card on death.
- **Storm-Kiln Artist** — {3}{R}. A Treasure per instant or sorcery cast **or copied**, and +1/+0 per artifact. With eight Treasures out it is a 10/2 that Stations Dawnsire to 10 by itself.
- **Goldspan Dragon** — {3}{R}{R} 4/4 flying haste. A Treasure on attack *and* whenever it becomes the target of a **spell** — abilities like Dawnsire's don't count. Your Treasures tap for two mana instead of one.
- **Hoarding Dragon** — {3}{R}{R} 4/4 flier that tutors an artifact to exile and returns it to hand on death. Finds Dawnsire, Sol Ring or Gilded Lotus, and it *wants* to die to your own sweeper.
- **Rapacious Dragon** — {4}{R} 3/3 flier that arrives with **two** Treasures — six tokens with Academy Manufactor.
- **Smaug, Wicked Worm** — {3}{B}{R} 5/5 flier. Creates X **tapped** Treasures where X is your opponents' artifact count, then draws a card **and loses you 1 life** whenever you cast a spell with Treasure mana. On a big Treasure turn that life adds up.
- **Lathliss, Dragon Queen** — {4}{R}{R} 6/6 flier. Every other **nontoken Dragon you control** that enters brings a 5/5 flying Dragon; `{1}{R}` pumps **your Dragons** +1/+0.
- **Steel Hellkite** — {6} colourless artifact Dragon. `{X}` destroys each nonland permanent of mana value X controlled by a player it dealt **combat** damage to this turn — so it must connect. Once per turn. `{2}: +1/+0` is repeatable, so six Treasures makes it an 11-power Station tap.
- **Smaug, the Great Calamity // Spew Flame** — {5}{R}{R} 5/5 flier with an Adventure: **Spew Flame** ({4}{R}) deals 5 damage to target creature. Aim it at your own Smaug for **five Treasures**, then cast the Dragon from exile later.
- **Terror of Mount Velus** — {5}{R}{R} 5/5 flying double strike that gives your board double strike as it enters. A double-striking 8/7 Smaug swings for **16**; two connections is lethal commander damage.

### Enchantments (5)
- **Vampiric Rites** — {B} enchantment; the outlet costs `{1}{B}, sacrifice a creature: gain 1 life, draw a card`. Budget two mana per creature when saving them from a wipe.
- **Impact Tremors** — {1}{R}. Every creature **you control** that enters deals 1 to each opponent.
- **Bastion of Remembrance** — {2}{B}. Arrives with a 1/1 Human Soldier; every creature **you control** that dies drains each opponent for 1 and gains you 1.
- **The Misty Mountains Cold** — {2}{R}. A Treasure per chapter, but it checks after **each** one: the moment you control four or more Treasures it sacrifices itself for a 6/6 red flying Dragon. With Treasures already out it often ends on chapter II.
- **Burn, Burn, Tree and Fern** — {3}{R} Saga: 6 damage to a creature **an opponent controls**, then destroy an **artifact** an opponent controls, then two chapters of {R}. Both targeted chapters are opponent-only, so chapter I cannot feed Smaug — and it answers artifacts, not enchantments.

### Artifacts & Mana (17)
- **Everflowing Chalice** — {0}, multikicker {2}. Two mana on turn two or six late.
- **Sol Ring** — {1}. Fastest ramp in the format.
- **Arcane Signet** — {2}. Two-mana fixing on colour identity.
- **Fellwar Stone** — {2}. In a pod, somebody is producing your colours.
- **Idol of Oblivion** — {2}. `{T}`: draw a card, if you created a token this turn. **One card per turn**, however many tokens you made — but it is live every turn here.
- **Mazemind Tome** — {2}. Scry for `{T}` or draw for `{2},{T}`, four times, then it exiles itself and gains you **4 life**.
- **Swiftfoot Boots** — {2}. Smaug already has haste and indestructible; **hexproof** is the gap — it stops a Swords to Plowshares or a Pongify. It does **not** stop an edict or a sacrifice effect, which don't target. *(You own three copies. The Secret Lair "Air Shoes" printing is the one sleeved in Full Deployment, so use one of the two plain printings.)*
- **Thrór's Map** — {2}. Fetches a basic to **hand** (not the battlefield), then loots for `{2},{T}`.
- **Carnelian Orb of Dragonkind** — {2}{R}. Taps for {R}; that mana gives a Dragon haste.
- **Chromatic Lantern** — {3}. **Every land you control taps for any colour.** The best fixing available in the collection, and the fix for a deck whose pips run 3:1 red but which still needs {B}{B} on curve.
- **The Black Arrow** — {3} flash Equipment. 1 damage to any target on entry, **destroying it if it is a Dragon** — instant-speed removal for an opposing Dragon. Aimed at your own indestructible Smaug the destroy clause simply fails and you keep the Treasure. Then +1/+1 and reach.
- **Knuckles's Gloves (The Reaver Cleaver)** — {2}{R}, **equip {3}**. +1/+1, trample, and "whenever this creature deals combat damage to a player or planeswalker, create that many Treasure tokens." On Smaug that is a 9/8 flier — **nine** Treasures a connection.
- **Hedron Archive** — {4}. Two mana now, two cards later.
- **Lux Cannon** — {4}. `{T}`: charge counter. `{T}`, remove three: **destroy target permanent**. Repeatable, unconditional removal that answers enchantments, problem commanders and anything else Rakdos cannot touch. Coretapper halves the wind-up.
- **Dawnsire, Sunstar Dreadnought** — *the deck's best draw, not its plan.* {5} Legendary Artifact — Spacecraft, 20/20. **Station** (tap another creature you control: add charge counters equal to its power; sorcery speed, and tapping as a cost ignores summoning sickness). At **10+**: *whenever you attack*, it deals **100 damage** to up to one target creature — aim it at your indestructible commander for **100 Treasures every combat**, which Exsanguinate then turns into a kill. The trigger is "whenever *you* attack", not whenever Dawnsire attacks, so one attacker turns it on. **Deliberately stop between 10 and 19 counters**: below 20 it is not a creature, so it dodges your own Blasphemous Act and every piece of creature removal in the pod.
- **Gilded Lotus** — {5}. Three mana of one colour.
- **Pyromancer's Goggles** — {5}. Copies red instants and sorceries cast with its mana. Copying Blasphemous Act is 26 damage to Smaug and **26 Treasures**; copying Fuel the Flames is a clean 4-damage sweep. It is **not** a double wipe with Chain Reaction — the copy resolves first and empties the board, so the original recalculates X against the survivors.

### Instants (10)
- **Abrade** — {1}{R}. 3 damage to a creature, or destroy an artifact. The creature mode can be aimed at your own Smaug for three Treasures.
- **Deadly Dispute** — {1}{B}. Sacrifice an artifact — a Treasure works — draw two, make a Treasure back.
- **Infernal Grasp** — {1}{B}. Unconditional creature kill, at the cost of 2 life.
- **Scorching Dragonfire** — {1}{R}. 3 damage to a creature or planeswalker, exiling it if it would die. On Smaug it is three Treasures and the exile clause never fires.
- **Chaos Warp** — {2}{R}. The deck's only **instant-speed** answer to a resolved enchantment or any problem permanent. Against a commander it is tempo only — they may send it to the command zone — and the flip can hand them a free permanent.
- **Fiery Annihilation** — {2}{R}. 5 damage to a creature, exiling it if it would die, plus exile an Equipment attached to it. Premium removal, or **five Treasures for three mana** at instant speed.
- **Fuel the Flames** — {2}{R}. 2 damage to each creature; two Treasures on Smaug, and it cycles for {2} when it's dead.
- **Hero's Downfall** — {1}{B}{B}. Instant-speed creature or planeswalker removal.
- **Big Score** — {3}{R}. Discard one, draw two, make two Treasures.
- **Unexpected Windfall** — {2}{R}{R}. A second Big Score at a colour-heavier cost.

### Sorceries (7)
- **Exsanguinate** — {X}{B}{B}. **Each opponent loses X life; you gain that much.** The deck's mana sink and its answer to "what do I spend 100 Treasures on" — it wins through a stalled board with no combat, no targets and no creatures required.
- **Feed the Swarm** — {1}{B}. Black removal that hits an **enchantment** — a genuine Rakdos gap-filler.
- **Seize the Spoils** — {2}{R}. Discard one, draw two, make a Treasure.
- **Zombify** — {3}{B}. Return a creature from your graveyard to the battlefield. The deck previously had **zero** recursion; this rebuys Goldspan Dragon, Lathliss or Terror of Mount Velus after a wipe.
- **Chain Reaction** — {2}{R}{R}. X damage to each creature where X is the **total** creature count on the battlefield. Against three big-creature decks that is often only 5–7; it is a genuine wipe against token boards and a Treasure engine either way.
- **Season of the Bold** — {3}{R}{R}. Spend up to five **paw prints** across three repeatable modes (no life is paid — it is a paw print, not Phyrexian mana): {P} a tapped Treasure, {P}{P} impulse-draw two, {P}{P}{P} *"whenever you cast a spell, deal 2 damage to up to one target creature"* until the end of your next turn. That third mode aimed at Smaug turns every spell into two more Treasures.
- **Blasphemous Act** — {8}{R}, **{1} cheaper per creature on the battlefield** — in a developed pod it costs {R}. 13 damage to each creature: the table is wiped, Smaug lives, thirteen Treasures.

### Lands (37)
- **Command Tower** — Perfect fixing.
- **Path of Ancestry** — Both colours plus a scry on every Dragon you cast.
- **Temple of Malice** (scry), **Bloodfell Caves** (1 life), **Rakdos Guildgate** — three B/R duals, all enter tapped.
- **Thriving Bluff** — Enters tapped; taps for {R} or a chosen second colour (name black).
- **Exotic Orchard** — In a pod, usually both your colours.
- **Spire of Industry** — Any colour for 1 life while you control an artifact — on from turn one thanks to Great Furnace.
- **Great Furnace** — An **untapped** red source that is also an artifact: it fuels Spire of Industry, Storm-Kiln Artist's power and Deadly Dispute. *(Type line is "Artifact Land"; it is counted and listed as a land.)*
- **Secluded Courtyard** — Name Dragon; casts creature spells of that type only.
- **The Lonely Mountain** — A Mountain that makes 2/2 Dwarves. Enters tapped unless you control an Equipment (the deck runs three).
- **Rogue's Passage** — Makes Smaug unblockable for the kill.
- **Bojuka Bog** — Free graveyard hate against one opponent.
- **Evolving Wilds**, **Fabled Passage** — Fix the base and thin.
- **Mountain** (×13), **Swamp** (×9) — Red-weighted; the pips run roughly 3:1 red to black.

---

## Key Synergies

- **Smaug + Blasphemous Act / Chain Reaction / Fuel the Flames** — the core line. Wipe the pod, keep your commander, and bank the damage as Treasures to rebuild with. Available in most games: three sweepers plus eight other ways to damage your own commander.
- **Ill-Tempered Loner + any sweeper** — the Loner takes the damage and throws it again at any target: at a face for reach, or at Smaug for a second helping of Treasures. Blasphemous Act becomes 13 to the table, 13 Treasures, and 13 more damage wherever you want it.
- **Exsanguinate + any Treasure pile** — the kill. It scales off whatever the hoard happens to be, so it converts a 13-Treasure Blasphemous Act turn just as happily as a Dawnsire one.
- **Perforating Artist + a hasty commander** — Smaug attacks every turn, so raid is permanently on: 9 life across the pod per turn, or three opponents shedding permanents. The sacrifice clause is also the deck's only answer to hexproof and indestructible threats.
- **Dawnsire + Smaug** *(when you draw it)* — Station to 10+ (Smaug's 8 power plus any second creature does it in two taps), attack, and deal 100 noncombat damage to your own indestructible commander for **100 Treasures** a combat. Stop short of 20 counters so Dawnsire stays a non-creature and can't be removed. A ceiling-raiser, not a prerequisite.
- **Pyromancer's Goggles + Blasphemous Act** — 26 damage to Smaug, 26 Treasures. (Not Chain Reaction — see that entry.)
- **Lux Cannon + Coretapper** — Coretapper's sacrifice puts two counters on the Cannon, bringing repeatable "destroy target permanent" online early. The same Coretapper can instead push Dawnsire over its threshold.

## Changes in This Revision

Applied after a five-angle review (synergy, rules accuracy, mana base, multiplayer viability, card-pool sweep). All additions verified owned and within Black/Red/colourless identity, except Dawnsire, which is user-supplied.

| Cut | Reason | Added |
|-----|--------|-------|
| Seismic Rupture | Spares fliers, so it deals **Smaug zero damage and makes zero Treasures**, while killing five of your own ground creatures | **Dawnsire, Sunstar Dreadnought** |
| Requiem Monolith | Its granted trigger is **mandatory** — with Dawnsire's 100 damage it would draw 100 cards and cost 100 life. A trap that loses the game | **Lux Cannon** |
| Decree of Pain | 8 mana, *destroys* rather than damages so Smaug makes nothing, and {B}{B} is unreliable off ~18 black sources | **Chromatic Lantern** |
| Purifying Dragon | Its ping targets "a creature **defending player controls**" — it can never be aimed at your own Smaug | **Ill-Tempered Loner // Howlpack Avenger** |
| Dragon Mage | Hands each of three opponents a fresh seven cards when you are the player ahead on resources | **Exsanguinate** |
| Mirrorwing Dragon | Only copies instants and sorceries targeting **only** it, which opponents simply decline | **Fiery Annihilation** |
| Gratuitous Violence | {2}{R}{R}{R} needs ~30 red sources and the deck has ~22; it also doubles **none** of the sweepers, which are non-creature sources | **Coretapper** |
| Wishclaw Talisman | You get **one** search, then an opponent gains control of it *and* the two remaining counters | **Perforating Artist** |
| Maskwood Nexus | A 4-mana do-nothing whose only payoff needs Lathliss plus one of seven non-Dragon creatures | **Zombify** |
| Flamekin Village | The deck runs **zero Elementals**, so it always enters tapped, for a haste ability Smaug doesn't need | **Great Furnace** |
| Opal Palace | `{1},{T}: add one mana` is net zero, and +1/+1 counters are irrelevant on an indestructible 8/7 | **Rakdos Guildgate** |
| Unclaimed Territory | Casts creature spells only — dead for 25 of the deck's noncreature cards | **Thriving Bluff** |
| Terramorphic Expanse | A third tapped basic-fetch was one too many | 13th **Mountain** |

## Tokens Generated

| Token | P/T | Color | Type | Abilities | Created By |
|-------|-----|-------|------|-----------|------------|
| Treasure | — | Colorless | Artifact — Treasure | "{T}, Sacrifice: Add one mana of any color" | Smaug the Impenetrable; Smaug the Magnificent; Smaug, Wicked Worm; Goldspan Dragon; Rapacious Dragon; Dori, Bearer of Friends; Storm-Kiln Artist; The Misty Mountains Cold; Knuckles's Gloves (The Reaver Cleaver); Deadly Dispute; Big Score; Unexpected Windfall; Seize the Spoils; Season of the Bold |
| Clue | — | Colorless | Artifact — Clue | "{2}, Sacrifice: Draw a card" | Academy Manufactor (replacement effect — creates no token on its own) |
| Food | — | Colorless | Artifact — Food | "{2}, {T}, Sacrifice: Gain 3 life" | Academy Manufactor (replacement effect) |
| Dragon | 5/5 | Red | Creature — Dragon | Flying | Lathliss, Dragon Queen; Dragonmaster Outcast |
| Dragon | 6/6 | Red | Creature — Dragon | Flying | The Misty Mountains Cold |
| Dragon Illusion | X/X | Red | Creature — Dragon Illusion | Flying, haste; exiled at the next end step | Manaform Hellkite |
| Human Soldier | 1/1 | White | Creature — Human Soldier | — | Bastion of Remembrance |
| Dwarf | 2/2 | Red | Creature — Dwarf | — | The Lonely Mountain |
| Eldrazi | 10/10 | Colorless | Creature — Eldrazi | — | Idol of Oblivion |

## Mana Curve

62 non-land, non-commander spells. **Average mana value 3.39** (was 3.60 before this revision).

- 0 CMC: 1 card — `█`
- 1 CMC: 3 cards — `███`
- 2 CMC: 16 cards — `████████████████`
- 3 CMC: 17 cards — `█████████████████`
- 4 CMC: 12 cards — `████████████`
- 5 CMC: 8 cards — `████████`
- 6 CMC: 2 cards — `██`
- 7+ CMC: 3 cards — `███`

Blasphemous Act is counted at 9 but reliably costs {R} in a real pod. Exsanguinate is counted at 2 and is meant to be cast for far more.

## Short Mulligan and Play Notes

- **Early game (turns 1–4)**: Keep hands with two lands and a rock, or three lands and a cost reducer. Dragonlord's Servant, Sol Ring and Chromatic Lantern make a turn-five Smaug realistic. Ship one-landers — the commander costs seven.
- **Mid game (turns 5–8)**: Land Smaug and attack; haste means he threatens damage the turn he arrives. If Dawnsire is out, Station it rather than swinging with everything — one attacker is all the 10+ trigger needs, and Stationing costs you an attack only once or twice.
- **Late game**: The standard kill is sweeper → Treasures → redeploy while the pod is empty, with Perforating Artist draining 9 a turn in the background and Exsanguinate finishing whatever is left. If Dawnsire happens to be out, the same plan runs on 100 Treasures instead of 13.
- **Key interactions**:
  - Smaug's trigger is **noncombat** damage only — blockers make no Treasures.
  - Swiftfoot Boots grants hexproof, which stops *opponents'* targeting only, so Spew Flame, The Black Arrow, Abrade and Dawnsire can all still hit your own Smaug. Hexproof does **not** stop edicts.
  - Indestructible does not save Smaug from -X/-X, exile or sacrifice. Toxic Deluge-style effects still kill him.
  - Keep Dawnsire between 10 and 19 counters. At 20 it becomes a creature and starts dying to removal and to your own Blasphemous Act.

## Why These Choices (Summary)

- **The engine is damage aimed inward**: ten-plus cards can put noncombat damage on your own commander, counting Abrade and Scorching Dragonfire. Dawnsire converts that from a one-shot trick into a repeating one.
- **Sweepers are ramp here**, but only those that deal damage *and* can hit a flier — which is why Decree of Pain and Seismic Rupture were cut and the count settled at three.
- **Treasures finally have somewhere to go.** The previous draft generated a hoard with nothing to spend it on. Exsanguinate, Lux Cannon, Steel Hellkite's {X} and Dawnsire's Station are the sinks.
- **Fixing over raw land count**: pips run 3:1 red to black but the deck still needs {B}{B} on curve, and the collection contains **no untapped Rakdos dual at all**. Chromatic Lantern is the only real answer available.

## Analysis

**Strengths**:
- A commander immune to damage-based wipes, damage-based removal and combat, who profits from your own sweepers.
- Multiple independent win conditions: Exsanguinate off any hoard, Perforating Artist's per-turn drain, commander damage in the air, and Lathliss going wide. None of them require a specific card to be drawn.
- Explosive recovery: you are the only player whose board wipe leaves them with mana and threats.
- A high ceiling when Dawnsire shows up — a repeatable mana engine the pod largely cannot interact with, since below 20 counters it is not a creature — without the deck depending on it.

**Weaknesses/Missing Staples**:
- **Dragon tribal support**: a full sweep of the eligible pool confirms the collection holds **no additional Dragon creatures and no Dragon tribal payoffs at all** — no Dragon Tempest, Scourge of Valkas, Herald's Horn, Dragon's Hoard or Vanquisher's Banner. Every playable Dragon you own is already here. A hard collection ceiling.
- **Protection is one card.** Swiftfoot Boots is the only piece, and the pool contains no second hexproof or ward source and no answer to exile. Smaug is a single point of failure for roughly a dozen cards.
- **Mass artifact/enchantment removal does not exist in the pool** — no Vandalblast, no By Force. Lux Cannon and Chaos Warp answer one permanent at a time.
- **Colour consistency**: roughly 22 red and 18 black sources against fourteen {R}{R} cards. Chromatic Lantern papers over this; a Rakdos dual would fix it, and none exists in the collection.
- **Graveyard hate is thin**: Bojuka Bog hits one player once.

## Next Steps (Optional Suggestions)

- **Massacre Wurm** ({3}{B}{B}{B}) is the biggest single upgrade left — a one-sided -2/-2 across three opponents plus 2 life drained per creature that dies. Held back only because triple black is unreliable off ~18 sources; revisit once Chromatic Lantern proves itself.
- **Mana Geyser** ({3}{R}{R}) routinely makes 9–15 mana in a developed pod — a candidate over Seize the Spoils.
- **Meteor Golem** ({7}) destroys any nonland permanent an opponent controls and is an artifact, so Hoarding Dragon tutors it.
- **Pinnacle Kill-Ship** ({7}, ETB 10 damage to a creature) is a second Spacecraft and a 10-Treasure burst if you want redundancy on the Dawnsire plan.
- **Soul-Guide Lantern** ({1}, 2 owned) exiles *each opponent's* graveyard on sacrifice — better pod graveyard hate than Bojuka Bog.

---

## Suggested Deck Names

- **Hoard Mentality** — A pun on "herd mentality" that describes both Smaug's psychology and the Treasure pile. Current working title.
- **Smaug Screen** — "Smoke screen", and what thirteen damage to every other creature on the table actually is.
- **Impenetrable Assets** — The commander's name crossed with a balance sheet; the deck turns being damaged into liquidity.
- **Sitting on It** — Two words, what dragons famously do with gold, and a fair description of a board nobody can profitably attack.

---
Deck created from cards in your moxfield collection (moxfield_latest.csv & card_details.md), plus Dawnsire, Sunstar Dreadnought, which is not in the collection export.

**Version**: Draft | **Status**: Working version — revised after a five-angle review
**Generated**: 2026-09-18

---

## Card Collection Origin

The **Precon(s)** column lists precon sources from `moxfield_cards.md`. Dawnsire shows `—` because it is not in the collection.

| Card | Mana Cost | Category | Precon(s) |
|------|-----------|----------|-----------|
| Smaug the Impenetrable | {5}{B}{R} | Commander | — |
| Bastion of Remembrance | {2}{B} | Enchantment | — |
| Deadly Dispute | {1}{B} | Instant | — |
| Exsanguinate | {X}{B}{B} | Sorcery | — |
| Feed the Swarm | {1}{B} | Sorcery | — |
| Hero's Downfall | {1}{B}{B} | Instant | — |
| Infernal Grasp | {1}{B} | Instant | — |
| Midnight Reaper | {2}{B} | Creature | — |
| Morbid Opportunist | {2}{B} | Creature | — |
| Vampiric Rites | {B} | Enchantment | — |
| Zombify | {3}{B} | Sorcery | — |
| Abrade | {1}{R} | Instant | — |
| Big Score | {3}{R} | Instant | — |
| Blasphemous Act | {8}{R} | Sorcery | — |
| Burn, Burn, Tree and Fern | {3}{R} | Enchantment | — |
| Carnelian Orb of Dragonkind | {2}{R} | Artifact | — |
| Chain Reaction | {2}{R}{R} | Sorcery | — |
| Chaos Warp | {2}{R} | Instant | — |
| Dori, Bearer of Friends | {2}{R} | Legendary Creature | — |
| Dragonlord's Servant | {1}{R} | Creature | — |
| Dragonmaster Outcast | {R} | Creature | — |
| Fiery Annihilation | {2}{R} | Instant | — |
| Firespitter Whelp | {2}{R} | Creature | Foundations Beginner Box |
| Fuel the Flames | {2}{R} | Instant | — |
| Goldspan Dragon | {3}{R}{R} | Creature | — |
| Hoarding Dragon | {3}{R}{R} | Creature | — |
| Ill-Tempered Loner // Howlpack Avenger | {2}{R}{R} | Creature | — |
| Impact Tremors | {1}{R} | Enchantment | — |
| Knuckles's Gloves (The Reaver Cleaver) | {2}{R} | Legendary Artifact | Sonic the Hedgehog: Turbo Gear |
| Lathliss, Dragon Queen | {4}{R}{R} | Legendary Creature | — |
| Manaform Hellkite | {2}{R}{R} | Creature | — |
| Rapacious Dragon | {4}{R} | Creature | — |
| Scorching Dragonfire | {1}{R} | Instant | — |
| Season of the Bold | {3}{R}{R} | Sorcery | — |
| Seize the Spoils | {2}{R} | Sorcery | — |
| Smaug the Magnificent | {2}{R}{R} | Legendary Creature | — |
| Smaug, the Great Calamity // Spew Flame | {5}{R}{R} | Legendary Creature | — |
| Storm-Kiln Artist | {3}{R} | Creature | — |
| Terror of Mount Velus | {5}{R}{R} | Creature | — |
| The Misty Mountains Cold | {2}{R} | Enchantment | — |
| Unexpected Windfall | {2}{R}{R} | Instant | — |
| Academy Manufactor | {3} | Artifact Creature | — |
| Arcane Signet | {2} | Artifact | — |
| Bloodfell Caves | — | Land | — |
| Bojuka Bog | — | Land | — |
| Chromatic Lantern | {3} | Artifact | — |
| Command Tower | — | Land | — |
| Coretapper | {2} | Artifact Creature | — |
| Dawnsire, Sunstar Dreadnought | {5} | Legendary Artifact | — |
| Everflowing Chalice | {0} | Artifact | — |
| Evolving Wilds | — | Land | — |
| Exotic Orchard | — | Land | — |
| Fabled Passage | — | Land | — |
| Fellwar Stone | {2} | Artifact | — |
| Gilded Lotus | {5} | Artifact | — |
| Great Furnace | — | Artifact Land | — |
| Hedron Archive | {4} | Artifact | — |
| Idol of Oblivion | {2} | Artifact | — |
| Lux Cannon | {4} | Artifact | — |
| Mazemind Tome | {2} | Artifact | — |
| Mountain (×13) | — | Basic Land | — |
| Path of Ancestry | — | Land | — |
| Pyromancer's Goggles | {5} | Legendary Artifact | — |
| Rakdos Guildgate | — | Land | — |
| Rogue's Passage | — | Land | — |
| Secluded Courtyard | — | Land | — |
| Sol Ring | {1} | Artifact | — |
| Solemn Simulacrum | {4} | Artifact Creature | — |
| Spire of Industry | — | Land | — |
| Steel Hellkite | {6} | Artifact Creature | — |
| Swamp (×9) | — | Basic Land | — |
| Swiftfoot Boots | {2} | Artifact | Sonic the Hedgehog: Turbo Gear |
| Temple of Malice | — | Land | — |
| The Black Arrow | {3} | Legendary Artifact | — |
| The Lonely Mountain | — | Land | — |
| Thriving Bluff | — | Land | — |
| Thrór's Map | {2} | Legendary Artifact | — |
| Immersturm Predator | {2}{B}{R} | Creature | — |
| Perforating Artist | {1}{B}{R} | Creature | — |
| Smaug, Wicked Worm | {3}{B}{R} | Legendary Creature | — |
