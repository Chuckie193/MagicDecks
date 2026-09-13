# Claws for Concern — Gruul Werewolf Tribal Commander

Commander: Tovolar, Dire Overlord // Tovolar, the Midnight Scourge (2RG, Red/Green)

## Overview
- **Strategy**: A werewolf/wolf tribal aggro deck. Cheap creatures flood the board and transform into bigger night-side threats; anthem effects (Immerwolf, Nightpack Ambusher, Howlpack Resurgence, and the night sides of Mayor of Avabruck and Kessig Naturalist) pump the team, and Tovolar rewards every werewolf/wolf connection with a card. **Tovolar's upkeep trigger is the engine**: it forces night — which auto-flips all 14 daybound werewolves — *and* separately transforms your old-border Human Werewolves, so one trigger can flip the whole board at once. Immerwolf then locks the non-Humans on their bigger side, and Village Watch's night side lets every Wolf token attack the turn it arrives. Wilderland Scrounger and Beorn the Fierce grow the board permanently, either half of the Zopandrel / Unnatural Growth pair doubles it at every combat, and Second Harvest can double the *token* half of that board again on demand. This revision leans the whole plan toward a full table: Scurry of Squirrels' double myriad and Lasting Tarfire's per-opponent burn both get better with more opponents, Toski and Shamanic Revelation keep the hand and life total stocked for a long pod game, and Volcanic Torrent gives the deck its first sweeper that only ever hits someone else's board.
- **Intended for**: Multiple opponents (multiplayer pod). This revision is a deliberate pivot away from the previous "Both" build — the curve moved slightly higher (average CMC ~3.17 non-land, exc. commander, 24 of 64 spells at 1–2 mana) to make room for cards that scale with opponent count rather than 1v1 efficiency. Zopandrel's every-combat doubling (opponents' combats included), Scurry of Squirrels' double myriad, and Lasting Tarfire and Volcanic Torrent both hitting *every* opponent all get strictly better as more players sit down; none of them lose anything in a duel, but none of them are built for one either.
- **Card pool**: Avoid reserved decks — the whole collection **minus** Full Deployment (custom) and Dance of the Elements (precon). **Squirreled Away remains listed in `reserved_decks.md` as physically assembled**, but the user granted a one-time exception to draw from it for this specific build, so its cards are treated as available here even though the reserved-decks file itself was not edited — see the caveat under Next Steps before you sleeve this deck in paper. Spare copies of reserved cards were still used where the collection has them (Sol Ring, Command Tower, Path of Ancestry and Raging Ravine all survived on second copies), and a spare Volcanic Torrent turned up already unreserved in the Prismari Artistry precon, which is not on the reserved list. The Bark Ages — this deck's own base precon — is **not** reserved, so the werewolf core is intact.

## Lore

Tovolar howls and the treeline answers — bark splits into limbs, a bear-king shoulders through, and something with far too many teeth doubles every jaw in the pack. Dawn is a rumour. *Fence accordingly.*

---

## Decklist (100 cards)

### Commander (1)
- **Tovolar, Dire Overlord // Tovolar, the Midnight Scourge** — Draws a card whenever a Werewolf or Wolf you control deals combat damage to a player. At your upkeep with three or more Wolves/Werewolves it becomes night (flipping every daybound werewolf automatically) **and then** transforms any number of your old-border Human Werewolves — the one card that reliably turns the whole board on. Night side is a 4/4 with `{X}{R}{G}: target Wolf or Werewolf gets +X/+0 and trample`.

### Creatures (39)
- **Ascendant Packleader** — A 1-drop Wolf that grows a +1/+1 counter every time you cast a 4-plus mana value spell.
- **Barkform Harvester** — Changeling, so it *is* a Wolf and a Werewolf: it fills a body for Tovolar's night trigger, picks up Immerwolf's and Kessig Naturalist's anthems, and takes Mayor of Avabruck's Human anthem too. It also has **reach**, and — being a Bear as well — it turns Beorn on a combat early. Its `{2}: put a card from your graveyard on the bottom of your library` is *not* real recursion in a 100-card singleton deck; treat it as a tribal reach blocker that happens to have a button.
- **Beorn the Fierce** — A 6/6 trampler that turns one creature into a Bear every combat, **permanently**, handing it a trample counter and Beorn's own "other Bears get +2/+2" — so a 2/2 Wolf becomes a 4/4 trampler for good. At three Bears he draws **two cards a turn**; with Barkform Harvester already a Bear by changeling, that can be his *first* combat.
- **Burly Breaker // Dire-Strain Demolisher** — A 6/5 ward {1} that becomes an 8/7 with ward {3} at night. The most removal-resistant body in the deck.
- **Child of the Pack // Savage Packmate** — Daybound werewolf that can pay {2}{R}{G} for a 2/2 Wolf; night side is a trampler that anthems the team +1/+0.
- **Daybreak Ranger // Nightfall Predator** — Old-border werewolf; pings fliers by day, becomes a repeatable fight machine by night.
- **Duskwatch Recruiter // Krallenhorde Howler** — Digs three deep for a creature by day; makes creature spells cost **{1}** less at night. Premium card selection and a fine mulligan keep.
- **Elvish Regrower** — A 4/3 for four that returns **any permanent card** from your graveyard to your **hand** — the deck's only real recursion, and its answer to a sweeper.
- **Fangblade Brigand // Fangblade Eviscerator** — Daybound firebreathing/first-strike werewolf that can pump the whole team once it flips.
- **Hermit of the Natterknolls // Lone Wolf of the Natterknolls** *(new)* — Old-border Werewolf. Draws a card whenever an opponent casts a spell **during your turn**; the night side draws **two**. Excellent in a pod, where three opponents hold up removal and instants constantly.
- **Hound Tamer // Untamed Pup** — Trampler with a {3}{G} counter sink (which also draws off Terrasymbiosis); night side gives all Wolves and Werewolves trample.
- **Howlpack Piper // Wildsong Howler** — Uncounterable; cheats creatures into play from hand and untaps if the creature is a Wolf or Werewolf.
- **Huntmaster of the Fells // Ravager of the Fells** — Makes a Wolf and gains 2 life on every flip back to day, burns a creature and its controller on every flip to night. Note Immerwolf shuts the flip-back half off permanently.
- **Ill-Tempered Loner // Howlpack Avenger** — Daybound damage-reflector; night side turns every point of damage your permanents take into direct damage anywhere.
- **Immerwolf** — Anthem for Wolves/Werewolves (+1/+1, intimidate) that locks non-Human Werewolves from transforming back to day. With Cult of the Waxing Moon gone, its only remaining cost is that it permanently switches off Huntmaster of the Fells' flip-back-to-day Wolf-and-2-life trigger — a small price, so here it is close to an auto-include.
- **Instigator Gang // Wildblood Pack** — +1/+0 to attackers by day, +3/+0 and trample by night. The single biggest damage swing in the deck.
- **Kessig Naturalist // Lord of the Ulvenwald** — Adds a mana when it attacks by day; becomes a Wolf/Werewolf lord at night.
- **Kruin Outlaw // Terror of Kruin Pass** — First strike by day; double strike at night, and **Werewolves** you control gain menace (your Wolf tokens do not).
- **Llanowar Elves** *(new)* — Turn-one acceleration into a turn-two three-drop, and this deck has seventeen three-drops. Also a body: a Beorn conversion target, a Zopandrel doubling target and a chump blocker. Straight upgrade on the three-mana ramp aura it replaces.
- **Mayor of Avabruck // Howlpack Alpha** — Anthem for Humans by day (which includes Barkform Harvester), anthem plus an end-step Wolf token by night.
- **Migloz, Maze Crusher** — A three-mana 4/4 with five oil counters that spends them on vigilance and menace, +2/+2, or destroying an artifact or enchantment — removal stapled to a non-Human body.
- **Nightpack Ambusher** — Flash lord that makes a 2/2 Wolf at every end step you didn't cast a spell — and casting nothing on your own turn is also the only *free* way to reach night without Tovolar (Unnatural Moonrise still costs mana).
- **Outland Liberator // Frenzied Trapbreaker** — Cheap artifact/enchantment removal stapled to a body; night side grinds down opposing artifacts on attack.
- **Packsong Pup** — Puts a +1/+1 counter on itself at every combat if you control another Wolf/Werewolf — the most reliable recurring Terrasymbiosis trigger in the deck.
- **Reckless Stormseeker // Storm-Charged Slasher** — Grants a creature +1/+0 and haste each combat by day, +2/+0 and trample by night.
- **Sage of Ancient Lore // Werewolf of Ancient Hunger** — Draws on ETB and is as big as your hand; night side is a vigilant trampler as big as **the total cards in all players' hands**, which is usually much bigger.
- **Scorned Villager // Moonscarred Werewolf** — Mana dork by day, two-mana vigilant dork by night.
- **Scurry of Squirrels** *(new)* — **Double myriad**: attacking creates a tapped, attacking token copy of itself against **every other opponent**, then does it again — one green body turns into an attack across the whole pod. Each hit also drops a +1/+1 counter on a creature you control, a free Terrasymbiosis trigger every combat it connects anywhere.
- **Silverfur Partisan** — A 2/2 **trampler, not a lord** — it has no anthem clause. It mints a 2/2 Wolf every time a Wolf/Werewolf you control becomes the target of an **instant or sorcery spell**: in this deck, five cards you'd actually aim at your own creature — Bite Down, Snakeskin Veil, Unnatural Moonrise, Warg Tactics and Wolf Strike.
- **Toski, Bearer of Secrets** *(new)* — Indestructible and uncounterable, and it draws a card whenever **any** creature you control deals combat damage to a player, not just itself. With 39 creatures and several token generators, that's close to a guaranteed draw every combat, and it dodges the removal a full pod can throw at it.
- **Tovolar's Huntmaster // Tovolar's Packleader** — Two Wolves on ETB; at night it makes two more every time it attacks, and `{2}{G}{G}` makes another Wolf/Werewolf **fight** an opposing creature (it's removal, not a pump).
- **Village Messenger // Moonrise Intruder** — Hasty 1-drop that becomes a menacing 2/2 at night.
- **Village Watch // Village Reavers** *(new)* — Old-border Werewolf, hasty by day. **The night side gives every Wolf and Werewolf you control haste** — the only mass-haste effect available to this deck. Every token from Tovolar's Packleader, Ranger Class and Nightpack Ambusher can attack the turn it arrives, and it's what makes Second Harvest a same-turn alpha strike rather than a board built for next turn.
- **Volatile Arsonist // Dire-Strain Anarchist** — Menace/haste pinger that machine-guns a creature, a player and a planeswalker on attack, harder at night.
- **Wargling** — A two-mana 2/2 **Wolf** that grants **all your creatures trample** whenever it attacks while you *control* a 4-power creature — note the big creature does **not** have to attack, so it can stay home and block. Zopandrel makes that condition self-satisfying — it doubles Wargling to 4/4 at the beginning of combat, so Wargling turns itself on. One of the best cards in the constrained pool.
- **Weaver of Blossoms // Blossom-Clad Werewolf** — Any-colour mana dork by day; night side is a 3/4 that taps for two.
- **Wilderland Scrounger** *(new)* — A 3/6 **Wolf** — so it counts for Tovolar, Immerwolf, Nightpack Ambusher, Howlpack Resurgence and both night-side lords — whose ferocious trigger puts a **permanent +1/+1 counter on every creature you control** each time it attacks while you *control* a 4-power creature — again, that creature needn't attack, so Scrounger can swing alone while a doubled Zopandrel holds the fort. A repeatable, permanent version of the one-shot pump spell it replaces, on a body that actually blocks, and it feeds Terrasymbiosis every attack.
- **Wolfkin Outcast // Wedding Crasher** — Costs {2} less with a Wolf/Werewolf out; night side draws a card whenever any Wolf or Werewolf you control dies.
- **Zopandrel, Hunger Dominus** — A 4/6 **reach** body that **doubles the power and toughness of each creature you control** — and it triggers at the beginning of *every* combat phase in the turn cycle, opponents' included, so your board is doubled on defence too (it only ever doubles *your* creatures, never theirs). On eight Wolves that's a lethal swing; on defence it's a wall nobody attacks into. The deck's finisher and its best card in a pod.

### Enchantments (6)
- **Howlpack Resurgence** — Flash anthem: Wolves *and* Werewolves get +1/+1 and trample — a combat trick or a wrath-dodge, and unlike Full Moon's Rise it covers the tokens.
- **Hunter's Talent** — Enters as a Rabid Bite, levels into an attack-trigger trample pump, then into "draw a card each end step if you control a 4-power creature." Note the ETB is a triggered ability of an enchantment, so it does **not** trigger Silverfur Partisan.
- **Lasting Tarfire** *(new)* — One mana, and at the end of **each** end step where you put a counter on a creature this turn, it deals 2 damage to **each opponent**. Packsong Pup, Ranger Class L2 and Wilderland Scrounger all place a counter nearly every combat, so this fires close to every turn — and unlike a single-target burn spell, it hits the whole pod at once: 2 damage to each of three opponents is 6 damage from a card that cost one mana and asked nothing extra of the deck.
- **Ranger Class** — Makes a Wolf on ETB, then a +1/+1 counter on an attacker at Level 2 (a Terrasymbiosis trigger every combat), then casts creatures off the top at Level 3.
- **Terrasymbiosis** — Draws a card whenever you put +1/+1 counters on a creature, once each turn. Nearly every enabler is **repeatable**: Packsong Pup (every combat, free), Ranger Class L2 (every attack), Wilderland Scrounger (every attack), Ascendant Packleader (every one of the deck's twenty MV-4-plus spells), Hound Tamer's `{3}{G}` (unlimited activations), Arlinn the Pack's Hope's +1 (every creature that enters, for a turn) and an animated Raging Ravine (a counter every time it attacks). Only Snakeskin Veil and Warg Tactics are genuine one-shots. **Beorn's trample counter is a keyword counter, not a +1/+1 counter, and does not trigger it.**
- **Unnatural Growth** *(new)* — `{1}{G}{G}{G}{G}`: **doubles the power and toughness of each creature you control at the beginning of each combat** — the exact text on Zopandrel, on an enchantment, for two less mana. Two things make it worth a slot alongside Zopandrel rather than instead of it: it is **not a creature**, so it survives the board wipes this deck otherwise folds to and immediately makes the rebuilt board lethal; and if both resolve, the doublings stack for **quadruple** power. The real cost is `{G}{G}{G}{G}` — only **21** of the 35 lands produce green (plus a conditional Exotic Orchard), rising to **25 green producers** once Arcane Signet, Llanowar Elves, Scorned Villager and Weaver of Blossoms are counted. Even so it is a turn-six card in practice, not a turn-five one, and it is the single hardest cast in the deck.

### Artifacts & Mana (4)
- **Arcane Signet** — Untapped two-mana fixing that always produces exactly the colour you need.
- **Mind Stone** — Two-mana ramp that cracks for a card once mana is no longer needed.
- **Power Sneakers (Lightning Greaves)** — Haste and shroud for {2} with a **{0} equip**. It is the only protection in the pool for the deck's single point of failure, so it is worth the cost — but the cost is large. **Shroud stops your own targeting too**, and this deck targets its own creatures constantly: Bite Down, Wolf Strike, Snakeskin Veil, Warg Tactics, Unnatural Moonrise, Hunter's Talent, Beorn's combat trigger, Ranger Class L2, Hound Tamer's {3}{G}, Reckless Stormseeker's combat trigger, Arlinn Kord's +1, Tovolar's own {X}{R}{G}, and Kessig Wolf Run all fail on the equipped creature. Equip is sorcery-speed, so you cannot dodge this at instant speed. Its real job is carrying Tovolar safely to your next upkeep trigger — he draws off *any* wolf connecting, so he doesn't need to attack himself.
- **Sol Ring** — The best ramp piece in Commander; accelerates into Tovolar and the rest of the curve.

### Instants (10)
- **Abrade** — Flexible removal: 3 damage to a creature or destroy an artifact.
- **Bite Down** — Free-ish fight spell using your creature's own power as removal; hits planeswalkers, and targets your own Wolf for a Silverfur token.
- **Broken Wings** — Destroys an artifact, an enchantment, **or a creature with flying**.
- **Chaos Warp** — Catch-all answer to any permanent, including the ones red-green removal can't touch.
- **Moonlight Hunt** — Every Wolf/Werewolf you control damages a single target — a one-sided blowout against a key blocker. Its only target is a creature you *don't* control, so it does **not** trigger Silverfur Partisan.
- **Moonmist** — `{1}{G}` instant. **A one-sided fog**: it prevents all combat damage from creatures *other than* Wolves and Werewolves, so your 33 tribal bodies and every token connect normally while the opposing board deals **zero**. Blanks a lethal alpha strike, or turns your own attack into a blowout where their blockers die and deal nothing back. It also transforms all Humans — but daybound permanents can't be transformed, so that half only reaches the 11 old-border werewolves. Cast it for the fog, not the flip.
- **Second Harvest** *(new)* — Instant: for each token you control, create a token copy of it. Cast it after Village Watch has flipped and your board is covered in Wolf tokens, and every fresh copy has haste — a wide board becomes a lethal alpha strike in one card. Being an instant, it also doubles back a board a wipe just thinned.
- **Snakeskin Veil** — Protects a key threat, leaves a permanent +1/+1 counter, draws off Terrasymbiosis and mints a Silverfur Wolf. Four jobs for one mana.
- **Warg Tactics** *(new)* — Modal: **destroy a creature with flying**, or +1/+1 counter plus trample and hexproof on your own creature. Either mode is live in almost every game — it's flier removal when you need it and a protection trick that triggers both Terrasymbiosis and Silverfur when you don't.
- **Wolf Strike** — Pumps a creature (more at night) then fights — removal and a trick in one, and it targets your own Wolf for Silverfur Partisan.

### Sorceries (3)
- **Shamanic Revelation** *(new)* — Draw a card for each creature you control, plus gain 4 life for each creature with power 4 or greater (Zopandrel and any Beorn conversion qualify easily). In a long pod game, this is both the card-advantage and the life-total cushion the deck was missing — a wide board turns straight into a refuel.
- **Unnatural Moonrise** — Forces night, and turns a creature into a trampling card-draw threat; target your own Wolf and it also mints a Silverfur token. Flashback makes it a two-for-one, and it is the deck's only *proactive* night-forcer besides Tovolar.
- **Volcanic Torrent** *(new)* — Cascade into a free spell, then deals X damage to each creature **and planeswalker your opponents control**, X being your spells cast this turn (2, counting Volcanic Torrent and its cascade hit) — the deck's first real sweeper, and it never touches a single permanent you control. Safe to fire into a wide multiplayer board at any point.

### Planeswalkers (2)
- **Arlinn Kord // Arlinn, Embraced by the Moon** — Haste and pump or a 2/2 Wolf by day; anthem, 3 damage and a permanent haste-and-ping emblem by night.
- **Arlinn, the Pack's Hope // Arlinn, the Moon's Fury** — Day: +1 gives your creatures flash and an **extra +1/+1 counter as they enter** (a Terrasymbiosis trigger on every Wolf token), −3 makes two Wolves. Night: `+2: Add {R}{G}`, and `0:` turns her into a 5/5 **Werewolf** with trample, indestructible and haste — which also counts toward Tovolar's three-body threshold.

### Lands (35)
- **Command Tower** — Taps for Red or Green with no downside. *(Second copy — the first is in a reserved precon.)*
- **Exotic Orchard** — Enters **untapped** and taps for any colour an opponent's lands could make. Reliable against green or red opponents; it can whiff entirely against mono-blue or mono-white.
- **Forest** (x13) — Green basics (55 available after reservations).
- **Gongaga, Reactor Town** — Tapped Gruul dual, clean fixing.
- **Kessig Wolf Run** — Untapped finisher land: pump and trample for any creature, scaling with mana invested.
- **Mountain** (x12) — Red basics (down one copy to make room for Oran-Rief, the Vastwood; still 62 available after reservations).
- **Oran-Rief, the Vastwood** *(new)* — Tapped green source whose second ability puts a +1/+1 counter — a real Terrasymbiosis trigger — on each green creature that entered the battlefield this turn. Pairs with Llanowar Elves, Scorned Villager, Weaver of Blossoms and any token wave from Wilderland Scrounger, Ranger Class or Second Harvest. A straight upgrade on a 13th Mountain.
- **Path of Ancestry** — Gruul dual with a scry trigger when casting a creature sharing a type with Tovolar. *(Second copy.)*
- **Raging Ravine** — Tapped Gruul dual that becomes a self-growing 3/3 attacker — a threat that dodges sorcery-speed wraths. *(Second copy.)*
- **Rugged Highlands** — Tapped Gruul dual with 1 life attached. Reinstated purely on availability.
- **Sheltered Thicket** — Tapped Gruul dual with cycling when you're flooded.
- **Temple of Abandon** — Tapped Gruul dual with a scry trigger.

*10 nonbasic lands, of which **7 enter tapped** (Gongaga, Oran-Rief the Vastwood, Path of Ancestry, Raging Ravine, Rugged Highlands, Sheltered Thicket, Temple of Abandon). Command Tower, Exotic Orchard and Kessig Wolf Run are the untapped three. Bristling Backwoods — the deck's own previously-flagged weakest land — was cut this revision to make room for Shamanic Revelation as a 65th spell rather than a 36th land.*

---

## Key Synergies

- **Tovolar's upkeep trigger flips both werewolf groups at once**: it makes it night, which auto-flips all 14 daybound werewolves (Tovolar included), *and then* transforms any number of your old-border Human Werewolves, which the day/night cycle doesn't touch. One trigger can turn the entire board on.
- **Zopandrel, Hunger Dominus + Wargling**: Zopandrel doubles your whole board at the beginning of *each* combat, which pushes Wargling to 4/4 — satisfying Wargling's own ferocious condition, so it hands the doubled board trample. Two cards, and eight 2/2 Wolves become eight 4/4 tramplers.
- **Unnatural Growth + Zopandrel, Hunger Dominus — the doublings stack**: both read "at the beginning of each combat, double the power and toughness of each creature you control," and two independent doubling effects apply one after the other, so a 2/2 Wolf token attacks as an **8/8**. You rarely need both to win — the point is that they are redundant *copies of the same win condition* which fail to different answers, since the wipe that kills Zopandrel leaves an enchantment untouched. Drawing both is upside, not the plan.
- **Doubling timing — sequence your pump around it**: both trigger at the **beginning of combat**, *before* attackers are declared, and each locks in X as the creature's power at the moment it resolves (CR 701.9b). So everything already applied gets doubled — including static anthems and existing +1/+1 counters. A 2/2 Wolf under Immerwolf and Nightpack Ambusher is a 4/4, which becomes 8/8 and then **16/16** with both doublers. What comes *after* splits in two:
  - **Never doubleable** — attack triggers resolve after the beginning-of-combat step no matter what you do, so Wilderland Scrounger's trigger, Ranger Class L2, Hunter's Talent L2 and Wargling's +1/+0 are always added at face value. Wolf tokens created *during* combat (Tovolar's Packleader, a Silverfur token) get no doubling at all.
  - **Doubleable if you sequence it** — Kessig Wolf Run and Tovolar's `{X}{R}{G}` are activated abilities usable at instant speed. Use them **while the doubling trigger is still on the stack** and the doubler sees the pumped power. A 4/4 with Kessig Wolf Run for X=3 is a 7/4 that doubles to **14/8**; pump after the trigger resolves instead and the same mana gets you 8/8 +3 = 11/8. Three damage, purely from sequencing.

  **Practical rule: with a doubler out, use everything you can at instant speed while the doubling trigger is on the stack, not after it resolves.** That covers Howlpack Resurgence, Kessig Wolf Run, Tovolar's ability, Snakeskin Veil and Warg Tactics in one habit — and waiting until the trigger is visible gives you more information than acting a step early.
- **Wilderland Scrounger + Terrasymbiosis + Beorn the Fierce**: three permanents that all convert combat into permanent board growth. Scrounger counters up every creature each attack (and draws off Terrasymbiosis), Beorn converts one creature into a +2/+2 trampling Bear each combat and draws two once three Bears are out. None of them is a combo — they're independent engines that stack.
- **Barkform Harvester's changeling**: it counts as a Wolf *and* a Werewolf (Tovolar's threshold, Immerwolf, Howlpack Resurgence, Moonmist's fog clause), as a **Human** for Mayor of Avabruck's day anthem, and as a **Bear** for Beorn — one colourless three-drop touching four different tribal lines, on a reach body.
- **Silverfur Partisan + your five targeting spells**: Bite Down, Snakeskin Veil, Unnatural Moonrise, Warg Tactics and Wolf Strike each target a Wolf or Werewolf you control, so each one also mints a free 2/2 Wolf. Moonlight Hunt does *not* — it only ever targets a creature you don't control.
- **Village Watch + Second Harvest**: at night, Village Watch gives every Wolf and Werewolf haste; cast Second Harvest right after and every token you control — Tovolar's Packleader's Wolves, Ranger Class's Wolf, every Nightpack Ambusher end-step Wolf — doubles, and every fresh copy can swing that same turn. A wide board becomes a lethal alpha strike in one instant.
- **Scurry of Squirrels' double myriad, against a full pod**: attacking creates a tapped, attacking token copy of itself against **every other opponent** — twice over — so one green body turns a normal combat into an attack on the whole table, and each hit also drops a Terrasymbiosis-triggering +1/+1 counter.
- **Lasting Tarfire + the deck's counter engines**: Packsong Pup, Wilderland Scrounger and Ranger Class L2 all place a +1/+1 counter nearly every combat; Lasting Tarfire turns that same trigger into 2 damage to **every opponent** at end of turn — in a four-player pod that's 6 damage across the table for one mana, off triggers the deck already generates for free.
- **Volcanic Torrent — a sweeper that only ever hits someone else's board**: it deals damage only to creatures and planeswalkers your **opponents** control, so it's safe to fire into a wide multiplayer table without setting your own plan back, and Cascade often refunds a second spell.
- **Toski, Bearer of Secrets + a wide board**: indestructible, uncounterable, and it draws off **any** creature you control connecting, not just itself — with 39 creatures plus token generators, that's close to a guaranteed draw every combat it isn't fully blocked out.
- **Elvish Regrower / Shamanic Revelation / Second Harvest + a board wipe**: the deck still has no sweeper insurance for *your own* board (Volcanic Torrent only ever hits opponents), so the real plan against a wrath is recovery: Elvish Regrower rebuys the best piece to hand, Shamanic Revelation refuels the hand and life total off whatever survived, and Second Harvest explosively doubles whatever token board you manage to rebuild.

---

## Cards Removed from Original

Base deck: the previous **Claws for Concern** draft (2026-09-05, itself built avoiding Full Deployment, Squirreled Away and Dance of the Elements). **Every cut in this revision is on merit, not forced by availability** — the user pivoted the "Intended for" target from Both to **Multiple opponents (pod)** and granted a one-time exception to draw from Squirreled Away, and both changes opened up strictly better options for the slots below.

| Card Removed | Reason | Replaced By |
|-------------|--------|-------------|
| Breakneck Rider // Neck Breaker | Its night side (+1/+0 and trample to attackers) is the weakest of the deck's four overlapping team-pump effects — Instigator Gang alone already gives +3/+0 and trample at night | Second Harvest |
| Geier Reach Bandit // Vildin-Pack Alpha | Narrow flip clause (transforms old-border werewolves only) on a day-side body the deck has plenty of; doesn't scale with opponent count | Scurry of Squirrels |
| Runebound Wolf | Four mana for single-target damage to **one** opponent — the weakest card specifically at a full pod table, where a single-opponent outlet does the least relative work | Lasting Tarfire |
| The Celestus | Backup ramp/night-forcer that nets zero mana the turn it flips day/night; ramp is already covered by Sol Ring, Arcane Signet, Mind Stone and three dorks | Volcanic Torrent |
| Werewolf Pack Leader | Single-faced (never transforms), and its draw trigger needs 6+ power connecting; Toski draws off **any** connecting creature and is both indestructible and uncounterable | Toski, Bearer of Secrets |

*Bristling Backwoods — the deck's own previously-flagged weakest land — was also cut, not to make room for one specific spell but to convert a 36th land into a 65th spell slot, which is what actually created room for Shamanic Revelation. Mountain drops from 13 to 12 copies for a straight land-for-land swap into Oran-Rief, the Vastwood.*

**If you dismantle Squirreled Away for real** (see the caveat under Next Steps), this pool of five cards is also worth a second look: Beastmaster Ascension, Oran-Rief the Vastwood (now included above), Shamanic Revelation (now included above), Toski, Bearer of Secrets (now included above) and Wolfwillow Haven all became available.

<details>
<summary>Previously removed (2026-09-05 revision and earlier)</summary>

Base deck for the 2026-09-05 revision: the previous **Claws for Concern** draft (2026-08-19), which was built from the **full** collection.

**Fourteen of the seventeen cuts below were forced by card availability, not by card quality.** Since that draft was written, `reserved_decks.md` gained Squirreled Away and Dance of the Elements, and those two precons plus Full Deployment physically hold the only copy of fourteen cards in the list. The three exceptions are Arlinn, Voice of the Pack (cut on merit for a card that only became visible after the collection was re-synced), and Cult of the Waxing Moon and Full Moon's Rise, both cut on merit to make room for two Werewolves after comparing this list against the wider field — see below.

| Card Removed | Reason | Replaced By |
|-------------|--------|-------------|
| Air Shoes (Swiftfoot Boots) | **Reserved** — the only copy is sleeved in Full Deployment | Power Sneakers (Lightning Greaves) |
| Ancient Ziggurat | **Reserved** — Dance of the Elements | Rugged Highlands |
| Cult of the Waxing Moon | *Not reserved* — cut on merit. A 5-mana **off-tribe** Human Shaman; Village Watch competes for the slot, is a Werewolf, and fills a gap Cult doesn't. Also resolves the Immerwolf tension, since Immerwolf capped Cult's output | Village Watch // Village Reavers |
| Full Moon's Rise | *Not reserved* — cut on merit. Pumps and regenerates **Werewolves only**, missing all 8 non-Werewolf Wolves and every token; Howlpack Resurgence does the same job and covers both types | Hermit of the Natterknolls // Lone Wolf of the Natterknolls |
| Arlinn, Voice of the Pack | *Not reserved* — cut on merit. Six mana for a slow token engine, and the softest card in the deck against a pod that can attack a planeswalker | Unnatural Growth |
| Beastmaster Ascension | **Reserved** — Squirreled Away | Zopandrel, Hunger Dominus |
| Cavalier of Thorns | **Reserved** — Dance of the Elements | Elvish Regrower |
| Cultivate | **Reserved** — Dance of the Elements | Warg Tactics (ramp slot converted to interaction) |
| Garruk's Uprising | **Reserved** — Dance of the Elements | Terrasymbiosis |
| Oran-Rief, the Vastwood | **Reserved** — Squirreled Away | Mountain (13th basic) |
| Realmwalker | **Reserved** — Dance of the Elements | Barkform Harvester |
| Return of the Wildspeaker | **Reserved** — Dance of the Elements | Wilderland Scrounger |
| Secluded Courtyard | **Reserved** — Dance of the Elements | Exotic Orchard |
| Shamanic Revelation | **Reserved** — Squirreled Away | Beorn the Fierce |
| Toski, Bearer of Secrets | **Reserved** — Squirreled Away | Wargling |
| Unclaimed Territory | **Reserved** — Dance of the Elements | Forest (13th basic) |
| Wolfwillow Haven | **Reserved** — Squirreled Away | Llanowar Elves |

**If you dismantle Dance of the Elements or Squirreled Away, revisit this deck** — eight and five of these cuts respectively become available again immediately.

<details>
<summary>Previously removed (earlier revisions)</summary>

Cut in the 2026-08-19 revision, on card quality, from the full collection:

| Card Removed | Reason | Replaced By |
|-------------|--------|-------------|
| Afflicted Deserter // Werewolf Ransacker | Four mana for a 3/2; narrow night-side artifact destruction | Broken Wings |
| Decimate | Requires legal artifact, creature, enchantment *and* land targets to cast at all | Migloz, Maze Crusher |
| Hermit of the Natterknolls | Draw trigger depends entirely on opponents acting on your turn | Realmwalker |
| Into the Night | Four mana for a loot; cheaper night-forcers already exist | Shamanic Revelation |
| Kessig Forgemaster // Flameheart Werewolf | Lowest-impact body in the deck | Arcane Signet |
| Rampant Growth | Ramps to a *tapped* land on an aggressive curve | Arcane Signet (slot consolidated) |
| Rugged Highlands | Tapped dual whose only upside is 1 life | Ancient Ziggurat |
| Savage Mansion | Tapped dual with a four-mana surveil 1 | Secluded Courtyard |
| Thrill of Possibility | Card filtering, not card advantage | Toski, Bearer of Secrets |
| Village Watch // Village Reavers | Five mana for haste the deck already supplies more cheaply | Cavalier of Thorns |

*(Rugged Highlands has returned — the card that displaced it is reserved. Rampant Growth briefly returned this revision and was cut again for the same reason it was cut originally.)*

Cut in the original build, from the user-supplied werewolf list:

| Card Removed | Reason | Replaced By |
|-------------|--------|-------------|
| Ancient Grudge | Artifact-only removal is redundant | Burly Breaker // Dire-Strain Demolisher |
| Friendly Rivalry | Needs a second legendary creature for full value | Return of the Wildspeaker |
| Gruul Guildgate | Not in the owned collection | Bristling Backwoods |
| Gruul Turf | Not in the owned collection | Gongaga, Reactor Town |
| Heirloom Blade | Three mana plus equip on a deck that wants to deploy threats | Air Shoes (Swiftfoot Boots) |
| Horrid Vigor | Narrow one-shot trick; deathtouch is near-worthless here | Hunter's Talent |
| Mossfire Valley | Not in the owned collection | Raging Ravine |
| Omashu City | Not in the owned collection | Unclaimed Territory |
| Ominous Cemetery | Colorless utility land whose ability costs six mana | Oran-Rief, the Vastwood |
| Ruinous Intrusion | Four mana for narrow artifact/enchantment exile | Garruk's Uprising |
| Temple of the False God | Produces no coloured mana; dead before five lands | Cultivate |
| Uncaged Fury | Win-more combat trick that does nothing on an empty board | Wolfwillow Haven |

</details>

</details>

---

## Tokens Generated

| Token | P/T | Color | Type | Abilities | Created By |
|-------|-----|-------|------|-----------|------------|
| Wolf | 2/2 | Green | Creature — Wolf | — | Child of the Pack // Savage Packmate; Huntmaster of the Fells // Ravager of the Fells; Mayor of Avabruck // Howlpack Alpha; Nightpack Ambusher; Ranger Class; Silverfur Partisan; Tovolar's Huntmaster // Tovolar's Packleader; Arlinn Kord // Arlinn, Embraced by the Moon; Arlinn, the Pack's Hope // Arlinn, the Moon's Fury |
| Squirrel Scout (copy) | 2/2 | Green | Creature — Squirrel Scout | Myriad, myriad | Scurry of Squirrels |
| Emblem — Arlinn Kord | — | — | Emblem | Creatures you control have haste and "{T}: This creature deals damage equal to its power to any target." | Arlinn Kord // Arlinn, Embraced by the Moon |

*Raging Ravine animates itself into a 3/3 red and green Elemental, and Arlinn, the Moon's Fury turns herself into a 5/5 Werewolf — both are permanents changing type, not tokens. Beorn the Fierce grants trample counters, not tokens. Second Harvest doesn't create a fixed token type of its own — it copies every token you already control, so it doubles whichever rows in this table are on the battlefield when you cast it, most often the Wolf row.*

---

## Mana Curve

- 0 CMC: 0 cards
- 1 CMC: 5 cards  | █████ (5)
- 2 CMC: 19 cards | ███████████████████ (19)
- 3 CMC: 17 cards | █████████████████ (17) *(includes Tovolar, Dire Overlord)*
- 4 CMC: 12 cards | ████████████ (12)
- 5 CMC: 9 cards  | █████████ (9)
- 6 CMC: 2 cards  | ██ (2)
- 7+ CMC: 1 card  | █ (1) *(Zopandrel, Hunger Dominus)*

Average CMC (non-land, exc. commander): ~3.17 — 24 of 64 spells cost one or two. The curve moved slightly higher than the previous revision (~3.06) on purpose: Toski, Second Harvest, Volcanic Torrent and Shamanic Revelation all land at 4–5 mana, trading a touch of early speed for cards that scale with a full pod rather than a duel.

---

## Short Mulligan and Play Notes

- **Mulligan to *deploy and protect* Tovolar, not to find him.** He is always available from the command zone, so he is never the card you are digging for. What you need in an opening hand is the mana to cast him on turn 3–4, two or three cheap Wolf/Werewolf bodies to switch on his three-permanent threshold, and ideally Power Sneakers to carry him to your next upkeep. Keep 3–4 lands with two cheap bodies. Duskwatch Recruiter earns a keep as a *body*-finder — it cannot find Tovolar, and neither can Howlpack Piper, which only puts a creature from your **hand** onto the battlefield.
- **Early game (turns 1–3)**: Llanowar Elves or Sol Ring on turn 1 into a three-drop on turn 2. Cheap werewolves (Village Messenger, Ascendant Packleader, Scorned Villager), then Immerwolf, Duskwatch Recruiter, Barkform Harvester, Wargling, Hunter's Talent, Terrasymbiosis or Ranger Class.
- **Mid game (turns 4–6)**: Land Tovolar behind Sol Ring or Power Sneakers once three-plus Wolves/Werewolves are out so the upkeep trigger comes online next turn. Beorn and Wilderland Scrounger both start compounding from the combat after they land. Deploy Nightpack Ambusher or Toski on an opponent's end step, then hold up Howlpack Resurgence, Warg Tactics or Broken Wings. Scurry of Squirrels is worth deploying even into an empty board — its double myriad only gets better once opponents are down to fewer blockers.
- **Late game (turn 7+)**: Zopandrel is the button — cast him into a wide board and the next combat is usually lethal, and he blanks opposing attacks in the meantime. If a wrath has already hit, Shamanic Revelation refuels off whatever's left and Second Harvest doubles it back up the moment Village Watch is online. Volcanic Torrent clears a path through the opponent with the scariest board without ever touching yours. Kessig Wolf Run closes games combat can't, and Raging Ravine gives you a threat that survives a wrath.
- **Day/night, stated correctly**: it becomes night when a player casts **zero** spells during their own turn. Casting exactly one spell changes nothing. It becomes day again when a player casts **two or more** spells during their own turn. Because a 39-creature deck never wants to skip a turn of development, **Tovolar's upkeep trigger is your real night button** — the other routes (casting nothing, Unnatural Moonrise) are backups.
- **Key interactions**: Daybound permanents cannot be transformed by anything except the day/night cycle — so Vildin-Pack Alpha only flips the 11 old-border werewolves, and Tovolar's own transform clause targets that same group. Power Sneakers' shroud blocks about thirteen of your own effects on the equipped creature and equip is sorcery-speed; put them on Tovolar to keep him alive, not to enable him. **The Immerwolf call is the deck's biggest piloting decision** — Immerwolf refuses the day-flip, Cult of the Waxing Moon taxes it, and the two cancel each other out (see Key Synergies). Play Immerwolf when you are ahead and want the stats locked; hold it while Cult and Huntmaster are profiting from the oscillation. Nightpack Ambusher wants you to cast *nothing* on your own turn, which pairs naturally with holding up instants.

---

## Why These Choices (Summary)

- **This revision is a pod-focus pivot, not another forced-availability rebuild.** All five swaps are on merit, made possible by two one-off finds: a user-granted exception to draw from Squirreled Away (5 cards) and a previously-overlooked spare Volcanic Torrent sitting in the already-unreserved Prismari Artistry precon. Every incoming card was chosen specifically because it scales better with more opponents at the table than the card it replaced.
- **The deck's two glaring pod weaknesses got direct answers.** "No sweeper" became "one one-sided sweeper" (Volcanic Torrent), and "no catch-up mechanism" became Shamanic Revelation's draw-and-lifegain refuel. Neither is a complete fix — see Analysis — but both were the top-flagged gaps in the previous revision.
- **Single-target effects lost value, multi-target effects gained it.** Runebound Wolf (damage to one opponent) and Geier Reach Bandit (a narrow one-player flip clause) are exactly the shape of card that's worse at a four-player table; Lasting Tarfire (damage to every opponent) and Scurry of Squirrels (an attack on every opponent) are exactly the shape that's better.
- **Redundant pump lost to card advantage.** Breakneck Rider's night side (+1/+0 and trample) was the weakest of four overlapping team-pump effects already in the deck; Toski's card draw and Second Harvest's finisher potential do more per slot than a fifth copy of "attackers get bigger."
- **The curve moved up slightly on purpose.** Average CMC rose from ~3.06 to ~3.17 (24 of 64 spells still cost 1–2). Pod games run longer than duels, so a touch of early speed was worth trading for cards that come online at 4–5 mana and keep paying off turn after turn.
- **Every card is verified available**: all 100 checked against `owned − (Full Deployment + Dance of the Elements)`, with the Squirreled Away exception applied and alt names (Air Shoes, Power Sneakers) resolved before subtracting.

---

## Analysis

**Strengths**:
- **Two independent one-card win conditions on the same effect.** Zopandrel and Unnatural Growth both double the board every combat, and they fail to *different* answers — Zopandrel to creature removal and wraths, Unnatural Growth to enchantment removal, which is far rarer at this bracket. In a deck with zero tutors that redundancy is what makes the plan reliable. Zopandrel also stonewalls opposing attacks, and both "each combat" clauses make them *better* in a pod, not worse
- **A genuine one-sided sweeper and a per-opponent damage engine that both scale up, not down, as the pod gets bigger.** Volcanic Torrent hits only opponents' creatures and planeswalkers, and Lasting Tarfire and Scurry of Squirrels both do more work with three opponents than with one
- Three independent permanent-based engines (Beorn, Wilderland Scrounger, Terrasymbiosis) that convert combat into permanent board growth
- Trample spread across five sources (Wargling, Beorn's counters, Howlpack Resurgence, Untamed Pup, Kessig Wolf Run) rather than one enchantment, so it survives targeted removal
- Reach on Barkform Harvester and Zopandrel, plus Daybreak Ranger, Broken Wings and Warg Tactics — flying defence is genuinely covered now
- A resilient, hard-to-answer card-advantage engine in Toski (indestructible, uncounterable, draws off any connecting creature) alongside Shamanic Revelation's one-shot refuel for the long games a pod produces

**Weaknesses/Missing Staples**:
- **The night plan is almost entirely commander-dependent — this is the deck's defining weakness.** Of the three routes to night, casting zero spells is something a 39-creature deck never volunteers for. That leaves Tovolar's upkeep trigger and one Unnatural Moonrise as routes you'd actually plan around. Without Tovolar you are a pile of below-rate day-side 2/2s and 3/3s, and Immerwolf — the only "stay at night" card — is a singleton whose lock costs you the Cult and Huntmaster loops.
- **Wrath exposure remains real — Volcanic Torrent doesn't fix it.** It only ever hits opponents' boards, so it does nothing to protect *your* 39 creatures and 2 planeswalkers from someone else's wrath. Elvish Regrower rebuying one card, Shamanic Revelation refueling the hand off whatever's left, and Second Harvest re-doubling a rebuilt token board are the recovery plan, not prevention. **Heroic Intervention (€7.99) or Wrap in Vigor (€1.13) is still the highest-value fix on the buy list for this.**
- **Board wipes**: one, and it's one-sided. Chain Reaction (owned, 2 copies, unreserved) remains on the bench — it's symmetric and would kill more of your own wide board than any single opponent's.
- **Recursion**: Elvish Regrower only. Barkform Harvester's ability puts cards on the *bottom of your library*, which is not recursion in a 100-card singleton deck.
- **Counterspells / stack interaction**: none, as is normal for Gruul — a combo opponent has to be raced or removed at sorcery speed.
- **Mana base**: 7 of 10 nonbasics enter tapped, and Exotic Orchard can whiff entirely against mono-blue or mono-white. Purely an availability problem.
- **Power Sneakers' shroud** blocks roughly thirteen of the deck's own effects on the equipped creature, and equip is sorcery-speed.

**Power level**: **Bracket 2** — a well-tuned casual deck. No tutors, no fast mana beyond Sol Ring, no combo, no stax, a five/seven-mana pair among the finishers and 7 of 10 nonbasics entering tapped. It beats precons and trades with other upgraded precons; it is not close to a bracket 4 table. This build is now tuned specifically for a **multiplayer pod**, not a duel: Zopandrel's every-combat doubling (opponents' combats included), Volcanic Torrent's one-sided sweep, Scurry of Squirrels' and Lasting Tarfire's per-opponent scaling, and Toski/Shamanic Revelation's card advantage all get better as more players join the game. If you need a 1v1-focused variant later, Volcanic Torrent and Lasting Tarfire are the first cards to cut back out.

---

## Next Steps (Optional Suggestions)

- **Read this before you sleeve the deck in paper.** This build assumes Toski, Shamanic Revelation, Scurry of Squirrels, Second Harvest and Oran-Rief, the Vastwood are pulled physically out of **Squirreled Away** — but `reserved_decks.md` still lists that precon as assembled, and it was *not* edited, since the user granted only a one-time exception for this build rather than confirming the precon is being dismantled. If Squirreled Away is staying sleeved, those five slots revert to the 2026-09-05 list (Zopandrel, Beorn the Fierce, Wargling, Llanowar Elves and a 13th Mountain are already in the deck and don't need to come back — only Oran-Rief needs to become a 13th Mountain again). If you *are* dismantling it for real, say so and this session can update `reserved_decks.md` to match, which also frees up Beastmaster Ascension and Wolfwillow Haven for a future revision.
- **The highest-value change is not a card, it's a decision**: if Dance of the Elements is not actually staying assembled, dismantling it returns Garruk's Uprising, Return of the Wildspeaker, Realmwalker, Cavalier of Thorns, Cultivate and three untapped tribal lands in one go — that alone puts the deck back above the previous draft
- **Immerwolf is now close to an auto-include.** With Cult of the Waxing Moon cut, its only cost is Huntmaster's flip-back loop — play it on curve rather than holding it
- **Beastmaster Ascension** (also Squirreled Away, not included this revision) is a third doubling-adjacent finisher — creatures get +5/+5 once it hits seven quest counters, which a wide token board reaches in a couple of turns of attacking — worth a look if you want to push even further into the go-wide plan
- **Cards surfaced by the 2026-09-05 collection re-sync but deliberately not included**: **Tireless Hauler // Dire-Strain Brawler** (a real Werewolf, 4/5 → 6/6 vigilance, but vanilla and the five-slot is the deck's most crowded), **Lambholt Harrier** (2-mana Wolf with `{3}{R}: target creature can't block`), **Tapping at the Window**, **Stolen Vitality** and **Stuffed Bear**. Also note **Suspicious Stowaway // Seafaring Werewolf** is a werewolf you own but it is blue-green, so it is outside Tovolar's colour identity and can never be played here
- Harvesttide Infiltrator and Tavern Ruffian (both owned and free) are the remaining unused werewolf bodies if you want a higher tribal count — but at 39 creatures you are not short of bodies
- Thrashing Brontodon or Cankerbloom (both owned, free) would add a second sacrificeable artifact/enchantment answer if your meta is enchantment-heavy
- If the collection expands, a sweeper that also protects **your** board (Heroic Intervention, Wrap in Vigor) or any untapped Gruul dual would close the two real remaining gaps

---

## Suggested Deck Names

- **Claws for Concern** — A pun on "cause for concern"; the deck presents an escalating board state that only gets scarier at night *(current working title)*
- **Bark Worse Than Bite** — Works twice over: the deck leans on Barkform Harvester and a bear-king for its value, and the joke is that the bite is in fact considerably worse
- **Pack Mentality** — Captures the tribal anthem-stacking plan where every wolf makes every other wolf better
- **Double or Nothing** — Zopandrel doubles the whole board every combat; the deck either converts that into a kill or it has spent seven mana on a 4/6

---
Deck upgraded from the previous draft using cards in your Moxfield collection (moxfield_latest.csv & card_details.md), excluding cards reserved by Full Deployment and Dance of the Elements — Squirreled Away's reservation was waived for this build only, per user request (see Next Steps).

**Version**: Draft | **Status**: Working version — multiplayer pod focus, pending confirmation on Squirreled Away
**Generated**: 2026-09-13

---

## Card Collection Origin

| Card | Category | Precon(s) |
|------|----------|-----------|
| Tovolar, Dire Overlord // Tovolar, the Midnight Scourge | Commander | The Bark Ages |
| Ascendant Packleader | Creature | The Bark Ages |
| Child of the Pack // Savage Packmate | Creature | The Bark Ages |
| Daybreak Ranger // Nightfall Predator | Creature | The Bark Ages |
| Duskwatch Recruiter // Krallenhorde Howler | Creature | The Bark Ages |
| Fangblade Brigand // Fangblade Eviscerator | Creature | The Bark Ages |
| Hermit of the Natterknolls // Lone Wolf of the Natterknolls | Creature | The Bark Ages |
| Hound Tamer // Untamed Pup | Creature | The Bark Ages |
| Howlpack Piper // Wildsong Howler | Creature | The Bark Ages |
| Huntmaster of the Fells // Ravager of the Fells | Creature | The Bark Ages |
| Ill-Tempered Loner // Howlpack Avenger | Creature | The Bark Ages |
| Immerwolf | Creature | The Bark Ages |
| Instigator Gang // Wildblood Pack | Creature | The Bark Ages |
| Kessig Naturalist // Lord of the Ulvenwald | Creature | The Bark Ages |
| Kruin Outlaw // Terror of Kruin Pass | Creature | The Bark Ages |
| Mayor of Avabruck // Howlpack Alpha | Creature | The Bark Ages |
| Nightpack Ambusher | Creature | The Bark Ages |
| Outland Liberator // Frenzied Trapbreaker | Creature | The Bark Ages |
| Packsong Pup | Creature | The Bark Ages |
| Reckless Stormseeker // Storm-Charged Slasher | Creature | The Bark Ages |
| Sage of Ancient Lore // Werewolf of Ancient Hunger | Creature | The Bark Ages |
| Scorned Villager // Moonscarred Werewolf | Creature | The Bark Ages |
| Silverfur Partisan | Creature | The Bark Ages |
| Tovolar's Huntmaster // Tovolar's Packleader | Creature | The Bark Ages |
| Village Messenger // Moonrise Intruder | Creature | The Bark Ages |
| Village Watch // Village Reavers | Creature | The Bark Ages |
| Volatile Arsonist // Dire-Strain Anarchist | Creature | The Bark Ages |
| Weaver of Blossoms // Blossom-Clad Werewolf | Creature | The Bark Ages |
| Wolfkin Outcast // Wedding Crasher | Creature | The Bark Ages |
| Howlpack Resurgence | Enchantment | The Bark Ages |
| Ranger Class | Enchantment | The Bark Ages |
| Sol Ring | Artifact | Counter Intelligence; Dance of the Elements; Prismari Artistry; Sonic the Hedgehog: Chasing Adventure; Squirreled Away; The Bark Ages |
| Abrade | Instant | Prismari Artistry; The Bark Ages |
| Bite Down | Instant | Foundations Beginner Box; The Bark Ages |
| Chaos Warp | Instant | Counter Intelligence; Prismari Artistry; The Bark Ages |
| Moonlight Hunt | Instant | The Bark Ages |
| Moonmist | Instant | The Bark Ages |
| Snakeskin Veil | Instant | Foundations Beginner Box; The Bark Ages |
| Wolf Strike | Instant | The Bark Ages |
| Unnatural Moonrise | Sorcery | The Bark Ages |
| Arlinn Kord // Arlinn, Embraced by the Moon | Legendary Planeswalker | The Bark Ages |
| Arlinn, the Pack's Hope // Arlinn, the Moon's Fury | Legendary Planeswalker | The Bark Ages |
| Command Tower | Land | Counter Intelligence; Dance of the Elements; Prismari Artistry; Squirreled Away; The Bark Ages |
| Forest (x13) | Basic Land | Dance of the Elements; Foundations Beginner Box; Hare Raising; Squirreled Away; The Bark Ages |
| Gongaga, Reactor Town | Land | The Bark Ages |
| Kessig Wolf Run | Land | The Bark Ages |
| Mountain (x12) | Basic Land | Counter Intelligence; Dance of the Elements; Foundations Beginner Box; Otter Limits; Prismari Artistry; The Bark Ages |
| Path of Ancestry | Land | Dance of the Elements; Prismari Artistry; Squirreled Away; The Bark Ages |
| Raging Ravine | Land | Dance of the Elements; The Bark Ages |
| Rugged Highlands | Land | The Bark Ages |
| Sheltered Thicket | Land | The Bark Ages |
| Temple of Abandon | Land | The Bark Ages |
| Scurry of Squirrels | Creature | Squirreled Away |
| Toski, Bearer of Secrets | Legendary Creature | Squirreled Away |
| Second Harvest | Instant | Squirreled Away |
| Shamanic Revelation | Sorcery | Squirreled Away |
| Oran-Rief, the Vastwood | Land | Squirreled Away |
| Arcane Signet | Artifact | Counter Intelligence; Dance of the Elements; Prismari Artistry; Squirreled Away |
| Power Sneakers (Lightning Greaves) | Artifact | Prismari Artistry; Sonic the Hedgehog: Turbo Gear |
| Volcanic Torrent | Sorcery | Prismari Artistry |
| Exotic Orchard | Land | Counter Intelligence; Dance of the Elements; Prismari Artistry; Squirreled Away |
| Elvish Regrower | Creature | Foundations Beginner Box |
| Llanowar Elves | Creature | Foundations Beginner Box |
| Broken Wings | Instant | Foundations Beginner Box |
| Barkform Harvester | Artifact Creature | — |
| Beorn the Fierce | Legendary Creature | — |
| Burly Breaker // Dire-Strain Demolisher | Creature | — |
| Migloz, Maze Crusher | Legendary Creature | — |
| Wargling | Creature | — |
| Wilderland Scrounger | Creature | — |
| Zopandrel, Hunger Dominus | Legendary Creature | — |
| Hunter's Talent | Enchantment | — |
| Lasting Tarfire | Enchantment | — |
| Terrasymbiosis | Enchantment | — |
| Unnatural Growth | Enchantment | — |
| Mind Stone | Artifact | — |
| Warg Tactics | Instant | — |
