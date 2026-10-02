# Table Manners — Golgari Food Aristocrats Commander

Commander: Ygra, Eater of All (3 generic, Black, Green — Black/Green)

## Overview
- **Strategy**: Ygra turns *every other creature on the battlefield* — yours and your opponents' — into a Food artifact. That does three things at once: every creature death anywhere on the table puts two +1/+1 counters on her, every "destroy target artifact" card in the deck becomes creature removal, and every "sacrifice a Food" cost becomes "sacrifice any creature you control" — any creature *but Ygra*, since she grants the type to **other** creatures and is not a Food herself. Grind the pod down with aristocrats drain while Ygra balloons, then convert her size into a kill with Garruk's Uprising trample and Unnatural Growth doubling her.
- **Intended for**: Multiplayer pod
- **Card pool**: Avoid reserved decks — Full Deployment, Claws for Concern and Dance of the Elements excluded. Table Manners *is* the rebuilt Squirreled Away precon, so it replaces that row in `reserved_decks.md`
- **This revision (2026-10-02)**: Master of the Wild Hunt moved to Claws for Concern, and you own only one copy. Hazel of the Rootbloom takes its slot as the repeatable token engine. A sweep of the cards added since 2026-09-17 also turned up Lich's Relic, which replaces Supper for Spiders. See *Cards Removed from Original*.

## Lore

Ygra yawns, and the battlefield becomes a buffet. Heroes, horrors, whole armies — all just *snacks* with delusions of grandeur. Her pack clears every plate, and she only grows hungrier. Bon appétit: you're the *main course*.

## Decklist (100 cards)

### Commander (1)
- **Ygra, Eater of All** — Makes every *other* creature a Food artifact **in addition to its other types** (they stay creatures — this matters, see the play notes), with a built-in sacrifice ability, and grows +2/+2 whenever **any** Food hits a graveyard from the battlefield, including your opponents'. She is **not** a Food herself, so she survives artifact wipes and does not trigger on her own death.

### Creatures (29)
- **Gilded Goose** — One-mana Food engine. Its mana ability *converts a Food into one mana* rather than adding mana from nothing, and replacement Food costs {1}{G} — so it is not acceleration when you keep a hand on it. Once Ygra is out it quietly becomes something better: `{T}, Sacrifice a Food` reads "sacrifice **any other creature you control** for one mana of any colour", making it a second free sacrifice outlet that fixes colours. Once per turn, and not the turn it lands.
- **Llanowar Elves** — Turn-one acceleration into a turn-three or turn-four Ygra.
- **Ravenous Squirrel** — Grows on every artifact or creature you sacrifice; its {1}{B}{G} outlet gains 1 life and draws a card (it drains nobody) and is a late-game mana sink, not an early one.
- **Cankerbloom** — {1}, sacrifice: destroy target artifact. Under Ygra that reads "destroy any creature on the table."
- **Outland Liberator // Frenzied Trapbreaker** — The same {1} sacrifice trick on a 2/2, which is the reason it is here. The night face adds an attack trigger, but it only hits the **defending player's** permanents, and flipping requires casting no spells during your own turn — do not plan around it.
- **Reassembling Skeleton** — Returns from the graveyard for {1}{B}, forever. With a free outlet it is a mana sink that converts spare mana into Ygra counters and drain triggers at *every* opponent, and it never runs out or gets blown out by removal.
- **Zulaport Cutthroat** — The core drain: every creature of yours that dies hits **all** opponents.
- **Vinereap Mentor** — Makes Food on entry *and* on death, so it pays Ygra twice across its life.
- **Twitching Doll** — Two-mana mana dork that taps for **any colour**, which is what actually casts Unnatural Growth's {G}{G}{G}{G} and Massacre Wurm's {B}{B}{B}. Every tap banks a nest counter, and `{T}, Sacrifice this creature: Create a 2/2 green Spider with reach for each counter` cashes the whole thing in for a pile of bodies — Foods under Ygra, doubled into Squirrels by Chatterfang, and live Mirkwood targets. Sorcery-speed cash-out, and it cannot tap the turn it lands.
- **Thornvault Forager** — `{T}, Forage: Add two mana in any combination of colors`, and forage means *sacrifice a Food* — which under Ygra means **sacrifice any creature you control**. So it is a sacrifice that costs no mana and in fact produces two. The **{T} is in the cost**, so it is once per turn and not at all the turn it lands. Forage offers a choice of "exile three cards from your graveyard *or* sacrifice a Food" — always take the Food; the graveyard mode fights Woe Strider's escape cost and Hazel's Nocturne.
- **Rat King, Verminister** — At your end step, if any permanent left the battlefield under your control that turn, it makes a 1/1 Rat and grows. In this deck that condition is met essentially every turn, so it is a free body per turn on a two-drop. Its `{T}, Sacrifice three Rats` ability returns "target creature card **and all other cards with the same name**" — in a singleton deck that is exactly **one** creature, so treat it as an expensive single reanimation, not a mass one.
- **Chatterfang, Squirrel General** — Every token you create arrives with a 1/1 Squirrel beside it, so Academy Manufactor makes six permanents instead of three and every landfall, Goat, Rat and Wolf brings a free body. Under Ygra each Squirrel is a Food, so token count converts directly into counters and drain. Its second ability — `{B}, Sacrifice X Squirrels: Target creature gets +X/-X` — is repeatable instant-speed removal for one black mana. It eats **Squirrels only**, not creatures generally, so it is not a general-purpose sacrifice outlet however many Squirrels you have.
- **Nadier's Nightblade** — Drains **every** opponent whenever a *token* you control leaves the battlefield. Zulaport and Bastion only see creature deaths; this covers the Foods, Treasures and Clues you crack every turn.
- **Thrashing Brontodon** — `{1}, Sacrifice this creature: Destroy target artifact or enchantment`. It sacrifices only **itself**, so it is a removal spell on a 3/4 body, not a sacrifice outlet for the rest of your board. Alongside Seedship Impact it is one of two answers you can hold up.
- **Woe Strider** — The best outlet in the deck: sacrificing costs **nothing**, so it converts a board into drain triggers in one turn. Escapes from the graveyard later.
- **Morbid Opportunist** — Draws a card on every turn creatures die, which in a pod is every turn.
- **Academy Manufactor** — Turns any Clue, Food or Treasure you would create into one of each. It triples your **token** output, not specifically your Food count.
- **Tireless Provisioner** — Landfall Food or Treasure every turn you hit a land drop.
- **Plaguecrafter** — Edicts every opponent at once — and it takes a creature **or planeswalker** — while you happily feed it your worst creature.
- **Wood Elves** — Fetches a Forest **onto the battlefield untapped**: real ramp, real fixing, later Food.
- **Poison-Tip Archer** — Reach and deathtouch to hold the ground, plus a drain trigger on every creature death.
- **Marauding Blight-Priest** *(new)* — `Whenever you gain life, each opponent loses 1 life.` The deck gains life constantly and almost none of it was doing anything: Zulaport Cutthroat, Bastion of Remembrance, Moldervine Reclamation, Vampiric Rites, Hazel's Nocturne, Ravenous Squirrel, Skyfisher Spider, Jungle Hollow, Illegitimate Business and every Food cracked. Each of those now also drains **each** opponent. It effectively doubles Zulaport and Bastion on the sacrifice turn, and it shares a trigger with Gourmand's Talent, so the same lifegain that makes the Raccoon also drains the table.
- **Hazel of the Rootbloom** *(new)* — `At the beginning of your end step, create a token that's a copy of target token you control. If that token is a Squirrel, instead create two tokens that are copies of it.` Squirreled Away's own commander, and the strongest repeatable fodder left in the pool now that Master of the Wild Hunt has gone to Claws for Concern. Copying a Squirrel makes two, and Chatterfang adds a Squirrel for each, so with both out that is **four bodies every turn** — four Foods under Ygra. It can copy a Treasure, Food or Clue instead when you need mana or cards more than bodies. Her `{T}, Pay 2 life, Tap X untapped tokens: Add X mana in any combination of colors` turns that board into **any-colour** mana. Tapping tokens is not a `{T}` cost, so summoning-sick ones count. That is the deck's best fix for Massacre Wurm's {B}{B}{B} and Unnatural Growth's {G}{G}{G}{G}. She needs a token to target, which almost every turn of this deck provides. Her own `{T}` means the mana arrives the turn after she lands.
- **Hungry Ghoul** *(new)* — `{1}, Sacrifice another creature: Put a +1/+1 counter on this creature.` A one-mana-per-activation repeatable outlet stapled to a 2/2, and the cheapest one in the pool after Woe Strider. This is the card that fixes the problem you actually hit in play: the deck was reaching turn 6 with a board and only a ~54% chance of any repeatable way to convert it. Each counter is also a Terrasymbiosis draw.
- **Skyfisher Spider** — Sacrifices a creature to destroy any nonland permanent, and on death converts your graveyard into life. Also a Spider, which matters for Mirkwood.
- **Chittering Witch** — One Rat per opponent, so it scales with pod size and doubles to two bodies per opponent with Chatterfang out. Its `{1}{B}, Sacrifice a creature: -2/-2` is repeatable instant-speed removal.
- **Arasta of the Endless Web** — A free 1/2 reach Spider every time an **opponent** casts an instant or sorcery, which in a three-opponent pod is several a round. Free fodder that costs nothing after it lands, plus a 3/5 reach blocker the deck was short on. Despite the Enchantment in its type line it **is a creature**, so board wipes kill it.
- **Ogre Slumlord** — Rats on every nontoken death, and gives all your Rats deathtouch.
- **Massacre Wurm** *(new)* — The sweeper this deck has never had. `Creatures your opponents control get -2/-2 until end of turn` wipes the pod's small creatures and leaves **your** board untouched; then `whenever a creature an opponent controls dies, that player loses 2 life` drains for the rest of the game. Across three opponents it routinely kills five or six creatures — every one of them a Food under Ygra, so it is **+10/+10 to +12/+12 on her** and **10–12 life** off the table on the turn it lands (2 per opponent creature that dies, not 2 per opponent). The cost is real: {3}{B}{B}{B} off 21 direct black sources, so it is a card you cast on curve only with a rock or Twitching Doll out.

### Enchantments (11)
- **Vampiric Rites** *(new)* — `{1}{B}, Sacrifice a creature: You gain 1 life and draw a card.` A one-mana **enchantment** that is a repeatable sacrifice outlet *and* a repeatable draw engine, and it survives every board wipe in the format. The deck's stated bottleneck was free repeatable outlets; this is the cheapest permanent one available and it turns the post-wipe graveyard-fodder plan into card advantage. It also pairs with Gourmand's Talent — the 1 life it gains is the lifegain trigger that makes the Raccoon.
- **Gourmand's Talent** — During your turn your artifacts are Foods too. The 3/3 Raccoon on your first lifegain each turn is **Level 2, which costs a further {2}{G}** — so budget 4 mana total for the mode you actually want, not the {G} on the card. One lifegain trigger a turn is all it needs after that, and the drain package supplies that many times over.
- **Squirrel Nest** — A 1/1 Squirrel every turn for the cost of tapping the enchanted land, which under Ygra is a free Food per turn: +2/+2 on her and a drain trigger, forever. It survives *creature* wipes — but it is an Aura, so enchantment removal and land destruction both answer it, and it dies with its land.
- **Bastion of Remembrance** — Non-creature drain anthem that survives board wipes.
- **Terrasymbiosis** — Draw equal to the counters placed, once each turn. Ygra puts **two** counters on herself per Food death, and "once each turn" means once per *player* turn — so up to four triggers a round in a pod, drawing two cards each.
- **Ninja Teen** — `Whenever a creature you control leaves the battlefield, each opponent loses 1 life.` **Leaves**, not dies, so it catches exile, bounce and tuck as well as sacrifice — and it is an enchantment, so a board wipe that kills your whole team triggers it once per creature and then survives.
- **Garruk's Uprising** *(new)* — Three mana for the trample Aggressive Mammoth used to supply at six, on a permanent a creature wipe cannot touch. It also draws a card as it enters if you already control a power-4 creature, and again on `whenever a creature you control with power 4 or greater **enters**`. The two clauses work differently. The **enters-the-battlefield** draw checks your board's *current* power, so a Ravenous Squirrel that has grown to 4 does turn that one on. The **ongoing** trigger checks power *as the creature enters*, so essentially only Ygra (6/6), Massacre Wurm (6/5) and an escaped Woe Strider (3/2 returning as a **5/4**) pay it — a token can qualify if Chitterspitter's acorn counters or Ninja Teen's Level 2 have already pushed it to power 4. Treat the recurring draw as a bonus on three cards, not an engine. Trample is the real reason it is here: it converts a 20/20 commander into lethal damage rather than a chump-block. *Spare copy: one of the two lives in Dance of the Elements, the other is free.*
- **Hunter's Talent** *(new)* — Level 1 is removal: `target creature you control deals damage equal to its power to target creature you don't control` — one-way damage, not a fight, so nothing hits you back, and you pick any creature you control. Point Ygra at something and it is almost always a kill *and* a Food death. **Level 2 ({1}{G}) is the real reason it is here** — `Whenever you attack, target attacking creature gets +1/+0 and gains trample`, repeatable, on an enchantment that survives creature wipes. Ygra has no evasion of her own and Garruk's Uprising was the only trample source in the deck; a 30/30 with no trample is a wall that any 1/1 chump-blocks.
- **Binding the Old Gods** — Chapter I destroys *any* nonland permanent an opponent controls — creature, artifact, enchantment, planeswalker — and it **destroys** rather than exiles, so Ygra collects. Chapter II fetches a Forest onto the battlefield **tapped**, and III hands the team deathtouch for a lethal alpha strike. A three-for-one at four mana.
- **Moldervine Reclamation** — Draw and life on every death; the long-game engine.
- **Unnatural Growth** — Doubles the power and toughness of your whole board at **each** combat — including your opponents' turns, which turns every blocker into a wall — and it survives creature wipes. With Zopandrel cut, this is the deck's only power doubler, so treat it as the finisher enabler rather than a value card. The {G}{G}{G}{G} is real: 22 lands tap for green directly (24 counting Evolving Wilds and Terramorphic Expanse), so it is castable — but treat it as a turn-six card.

### Artifacts & Mana (8)
- **Sol Ring** — Fastest ramp in the format.
- **Skullclamp** — Equip a 1/1, it dies, draw two — and under Ygra that death is also +2/+2 and a drain trigger. Chatterfang, Squirrel Nest and Rat King supply an endless stream of 1/1s to clamp.
- **Arcane Signet** — Two-mana fixing on colour identity.
- **Golgari Signet** — Fixes and filters into exactly BG.
- **Talisman of Resilience** — Two-mana rock for both colours.
- **Chitterspitter** *(new)* — `{G}, {T}: Create a 1/1 green Squirrel creature token.` It is an **artifact**, which is the whole point: it has no summoning sickness so it makes a Squirrel the turn it lands, and it survives every creature wipe in the format including your own cycled Decree of Pain. Its optional upkeep `sacrifice a token` is a free Ygra trigger and a free drain trigger with no outlet needed. With Chatterfang each activation is two bodies.
- **Swiftfoot Boots** *(new)* — The deck's only *permanent* answer to targeted removal on the commander. Hexproof stops opponents pointing spells at Ygra while blocking **none** of your own — Snakeskin Veil, Overprotect and Undying Malice all still work on her. Haste matters too: she is frequently recast, and the boots let a freshly-recast Ygra attack the turn she lands. **Use a plain printing, not Air Shoes.** You own four copies: `tdc` #328, two of `fdn` #355, and the Secret Lair `sld` #2096. The Secret Lair copy *is* Air Shoes and is sleeved in Full Deployment. Claws for Concern takes one plain copy and this deck another, which leaves one spare. The alt name does not apply to this deck even though `moxfield_cards.md` labels every row with it.
- **Lich's Relic** *(new)* — `When this Equipment enters, you may pay {2}. When you do, for each opponent, destroy up to one target creature or planeswalker that player controls.` Three mana for **three** kills in a pod, all destroy rather than exile, so it is up to +6/+6 on Ygra in one card. It hits planeswalkers too, which only Windgrace's Judgment and Maelstrom Pulse otherwise cover. Equipped creature gets +2/+1 afterwards (equip {2}), a small bonus on a sacrifice fodder token or on Ygra. Unlike most of the deck's removal it needs no help from Ygra, so it is live when she is not on the battlefield.

### Instants (9)
- **Snakeskin Veil** — One mana: a +1/+1 counter (which draws off Terrasymbiosis) plus hexproof for the commander the plan depends on.
- **Undying Malice** — Saves a creature from removal, or re-buys a sacrificed one with a counter attached.
- **Overprotect** — +3/+3 with trample, hexproof *and* indestructible: protection spell and finisher in one card.
- **Deadly Dispute** — Sacrifice a creature, draw two and make a Treasure.
- **Infernal Grasp** — Unconditional two-mana creature kill, and with Seedship Impact one of only two instant-speed answers under three mana.
- **Plumb the Forbidden** — Instant-speed answer to a board wipe: sacrifice the board in response and refill your hand.
- **Seedship Impact** *(new)* — `Destroy target artifact or enchantment` at **instant speed** for two mana, which under Ygra is "kill any creature on the table, at instant speed, for two mana". This is the card that closes the gap the deck has flagged since it was built: it now has two cheap instant answers instead of one. It destroys rather than exiles, so Ygra still collects, and the Lander rider (if the target's mana value was 2 or less) is live off opposing mana rocks and most Ygra-fied two-drops — a spare artifact that ramps, or feeds Deadly Dispute and Ravenous Squirrel.
- **Hazel's Nocturne** — Returns two creature cards from the graveyard, drains **each** opponent for 2 and gains you 2 life.
- **Windgrace's Judgment** — Destroys a nonland permanent from *each* opponent at instant speed; premium pod removal and the deck's best answer to a resolved planeswalker.

### Sorceries (5)
- **Wear Down** — Destroy target artifact or enchantment; promise an opponent a card and it destroys **two** instead. Under Ygra that is a two-mana sorcery that kills two creatures and puts four counters on her. The gifted card is a real cost in a pod — it is still the best rate in the deck.
- **Deadly Brew** *(new)* — `Each player sacrifices a creature or planeswalker of their choice. If you sacrificed a permanent this way, you may return another permanent card from your graveyard to your hand.` Two mana, and in a four-player pod it is **four Food deaths** — +8/+8 on Ygra and a Zulaport/Nadier/Ninja Teen trigger off your own — plus a permanent back from the yard. Note it is **one** Terrasymbiosis draw, not four: that enchantment fires only once each turn and all four deaths happen on yours. Two real caveats the rate can hide: **you are a player too**, so with Ygra as your only creature this makes you sacrifice *her*; and each opponent picks a creature **of their choice**, so expect their worst token, not their commander — this is a pump-and-value spell that happens to be an edict, not removal you can point.
- **Maelstrom Pulse** — Answers any nonland permanent, planeswalkers included, and sweeps token armies in one shot.
- **Shamanic Revelation** — Draws a card per creature. The ferocious lifegain needs creatures with **power 4 or greater** — Ygra (6/6) and Massacre Wurm (6/5) qualify with no help, so expect 4–12 life, and far more with Unnatural Growth up.
- **Decree of Pain** — **Cast it for the cycling cost, not the mana cost.** Hard-casting {6}{B}{B} is realistically a turn-9-or-later play off this mana base; `Cycling {3}{B}{B}` at five mana draws a card *and* gives **all creatures -2/-2 until end of turn**, which is the mode you will actually use. That sweep kills the pod's small creatures and your own token board — and every one of those is a Food, so it is a pile of counters on Ygra plus a drain trigger per token off Zulaport, Bastion, Nadier's and Ninja Teen. Ygra herself survives at 6/6. The hard cast destroys **all** creatures, Ygra included, so protect her first if you ever do pay full price (see the play notes).

### Planeswalkers (1)
- **Garruk, Cursed Huntsman** — Two Wolves per activation (four permanents with Chatterfang), removal on demand, and a game-ending +3/+3 trample emblem. The Wolves are also live Mirkwood targets.

### Lands (36)
- **Command Tower** — Perfect dual.
- **Exotic Orchard** — Usually any colour in a multicolour pod.
- **Woodland Cemetery** — Untapped dual once you have a basic.
- **Twilight Mire** — Taps for {C} on its own; its {B/G} filter into two coloured mana needs another source first. Best on double-costed spells — and it is how you get to {B}{B}{B} for Massacre Wurm a turn early.
- **Llanowar Wastes** — Painless for colourless, pays 1 for coloured.
- **Tainted Wood** — Both colours as long as you hold a Swamp.
- **Temple of Malady** — Tapped dual with a scry.
- **Jungle Hollow** — Tapped dual with a life buffer.
- **Haunted Mire** — Tapped Swamp Forest, so it switches on Woodland Cemetery and Tainted Wood.
- **Illegitimate Business** — Tapped B/G dual that gains 1 life on entry.
- **Necroblossom Snarl** — Enters untapped if you reveal a Swamp or Forest.
- **Titan's Grave** — Tapped dual with a late-game surveil sink.
- **Viridescent Bog** — `{1}, {T}: Add {B}{G}`. It does not appear in the direct-source count below because it cannot be tapped for mana on its own — but the {1} is **generic**, payable from any land you have, which makes it the best *fixer* in the deck: it launders a Forest, Twilight Mire or Hall of Oracles into black, and covers a black and a green pip in one activation. That is why it beats a plain tapped dual here despite the worse raw count.
- **Bojuka Bog** — Graveyard hate stapled to a land; near-free in a three-opponent pod, and the deck's only permanent answer to a graveyard.
- **Oran-Rief, the Vastwood** — Counters on green creatures that entered this turn, and every counter is a Terrasymbiosis trigger.
- **Mirkwood** — Tapped B/G dual. Its `{2}{B}{G}, {T}, Sacrifice: two +1/+1 counters` only targets a **Bear, Spider or Wolf** — Arasta, its Spider tokens, Skyfisher Spider and Garruk's Wolves keep it live.
- **Hall of Oracles** — Fixes for {1}. Its +1/+1 counter ability is sorcery-speed **and** requires that you have cast an instant or sorcery this turn, so it is occasional value, not a repeatable Terrasymbiosis engine.
- **Evolving Wilds** — Fixing and a shuffle.
- **Terramorphic Expanse** — Fixing and a shuffle.
- **Forest** (x9) — 82 available in collection.
- **Swamp** (x8) — 69 available in collection.

## Key Synergies
- **Ygra turns green artifact removal into creature removal**: she grants every *other* creature the artifact type **in addition to** its other types, so Cankerbloom, Outland Liberator, Thrashing Brontodon, **Seedship Impact** and Wear Down all become "destroy any creature" — **five** cards. Wear Down is the standout — two mana, two creatures, four counters on Ygra. The one thing this does **not** unlock is Haywire Mite-style effects that specify *noncreature* artifacts; creatures keep their creature type, so those can never target them.
- **Massacre Wurm + Ygra**: -2/-2 across three opponents' boards kills the mana dorks, the tokens and the utility creatures all at once. Every one of those is a Food when it dies, so the Wurm is simultaneously a one-sided sweeper, a ten-point swing on Ygra's stats, and a 10–12 life drain. Lich's Relic does the same job in a smaller way for three mana: one kill per opponent, every one a Food death.
- **Chatterfang + every token maker in the deck**: Academy Manufactor's three tokens become six permanents, Chittering Witch makes two bodies per opponent, Squirrel Nest and Rat King each make two a turn, Woe Strider's Goat brings a friend. **Hazel of the Rootbloom** is the best partner of all: her end-step copy of a Squirrel makes two, Chatterfang adds two more, and the next turn Hazel taps those four for four mana of any colour. Under Ygra every Squirrel is a Food, so each is +2/+2 on her and a drain when it leaves. Then {B} and a pile of Squirrels is instant-speed removal.
- **Ygra + Terrasymbiosis**: two counters per Food death, and Terrasymbiosis fires once per *player* turn — in a pod where creatures die every turn, a three-mana enchantment can draw you **two cards on each of the four turns in a round**.
- **The sacrifice turn**: with **Woe Strider** — the only outlet with no tap and no mana cost — plus Zulaport Cutthroat, Bastion of Remembrance, Poison-Tip Archer, Nadier's Nightblade and Ninja Teen out, every token creature you sacrifice drains **each** opponent up to five times over and puts two counters on Ygra. **Vampiric Rites** turns the same board into cards at {1}{B} apiece when you would rather draw than drain.
- **Ygra + Garruk's Uprising + Unnatural Growth**: Uprising gives Ygra trample for three mana and draws a card as she enters; Unnatural Growth doubles her at the beginning of each combat. A 12/12 Ygra becomes a 24/24 trampler, and neither piece dies to a creature wipe.
- **Skullclamp + any 1-toughness creature**: equip for {1}, it dies immediately, you draw two — and that death is simultaneously an Ygra trigger, a drain trigger and a Morbid Opportunist trigger.
- **Ygra's ward is not a real tax — except when it is**: "Sacrifice a Food" means an opponent targeting her must sacrifice one of their own creatures, **which then triggers Ygra for +2/+2 anyway**. The exception is worth knowing: an opponent who controls **no** creature and no Food simply cannot pay, and their spell is countered outright. Swiftfoot Boots make the whole question moot — they cannot target her at all.

## Cards Removed from Original

Compared against the previous Table Manners draft (2026-09-17). *(The twelve swaps made in that revision, and the 15 cuts made when the deck was first built from the Squirreled Away shell, are in the file's git history at commits `198a4b2` and `4b54348`.)*

| Card Removed | Reason | Replaced By |
|-------------|--------|-------------|
| Master of the Wild Hunt | **Forced by availability.** You own one copy and it is now sleeved in Claws for Concern | Hazel of the Rootbloom |
| Supper for Spiders | The narrowest card in the deck. The Foods it steals are *not creatures*, so most of the sacrifice outlets and every drain payoff ignore them. It also needed a wipe on the same turn to do anything | Lich's Relic |

*Availability note: every card in the deck is verified against `owned − reserved`, with Full Deployment, Claws for Concern and Dance of the Elements subtracted and alt names resolved first. Three cards share copies with reserved decks and have **none left over**: Garruk's Uprising (3 owned: Dance of the Elements, Claws for Concern and this deck), Unnatural Growth and Outland Liberator (2 owned each: Claws for Concern and this deck).*

*Printing note: the Swiftfoot Boots copy reserved by Full Deployment is the Secret Lair **Air Shoes** (`sld` #2096). The other three are plain printings (`tdc` #328 and two `fdn` #355): one is in Claws for Concern, one is here and one is spare. That is why this deck lists the card under its real name. `moxfield_cards.md` stamps the `Air Shoes` alt name on all three rows because `generate_cards_md.py` matches by card name rather than by printing — following the alt-name convention mechanically here would point you at the one copy you cannot use. The Precon(s) column below still shows `SonictheHedgehog TurboGear` for the same reason; treat it as provenance of the *name*, not of the copy in this deck.*

*Corrected after review: an earlier version of this revision also swapped **Viridescent Bog** for Golgari Guildgate on the stated grounds that the Bog "produces no coloured mana on its own". That was wrong — the Bog's {1} is **generic**, payable from any land, so it functions as a fixer that upgrades any source into a black and a green pip. Simulation put the Bog ahead of the Guildgate by ~2 points on Massacre Wurm and ~2.6 on Casualties of War, so the swap has been reverted and the Bog is back in the deck.*

## Tokens Generated

| Token | P/T | Color | Type | Abilities | Created By |
|-------|-----|-------|------|-----------|------------|
| Squirrel | 1/1 | Green | Creature — Squirrel | — | Chatterfang, Squirrel General (alongside *every* token you create); Squirrel Nest; Chitterspitter |
| Food | — | Colorless | Artifact — Food | "{2}, {T}, Sacrifice this token: You gain 3 life." | Gilded Goose; Vinereap Mentor; Academy Manufactor; Tireless Provisioner |
| Treasure | — | Colorless | Artifact — Treasure | "{T}, Sacrifice this token: Add one mana of any color." | Academy Manufactor; Tireless Provisioner; Deadly Dispute |
| Lander | — | Colorless | Artifact — Lander | "{2}, {T}, Sacrifice this token: Search your library for a basic land card, put it onto the battlefield tapped, then shuffle." | Seedship Impact (only if the destroyed permanent's mana value was 2 or less) |
| Clue | — | Colorless | Artifact — Clue | "{2}, Sacrifice this token: Draw a card." | Academy Manufactor |
| Spider | 1/2 | Green | Creature — Spider | Reach | Arasta of the Endless Web |
| Spider | 2/2 | Green | Creature — Spider | Reach | Twitching Doll (one per counter on it — nest counters *and* any +1/+1 counters) |
| Goat | 0/1 | White | Creature — Goat | — | Woe Strider |
| Rat | 1/1 | Black | Creature — Rat | — (gains deathtouch while Ogre Slumlord is out) | Chittering Witch; Ogre Slumlord; Rat King, Verminister |
| Raccoon | 3/3 | Green | Creature — Raccoon | — | Gourmand's Talent (level 2) |
| Human Soldier | 1/1 | White | Creature — Human Soldier | — | Bastion of Remembrance |
| Wolf | 2/2 | Black and Green | Creature — Wolf | "When this token dies, put a loyalty counter on each Garruk you control." | Garruk, Cursed Huntsman |
| Copy of a token | As copied | As copied | As copied | As copied | Hazel of the Rootbloom (one copy each end step, or two if it copies a Squirrel) |
| Emblem — Garruk, Cursed Huntsman | — | — | Emblem | "Creatures you control get +3/+3 and have trample." | Garruk, Cursed Huntsman |

## Mana Curve
- 0 CMC: 0 cards
- 1 CMC: 10 cards
- 2 CMC: 21 cards
- 3 CMC: 17 cards
- 4 CMC: 7 cards
- 5 CMC: 5 cards
- 6 CMC: 2 cards
- 7+ CMC: 1 card

```
0  │ (0)
1  │ ██████████ (10)
2  │ █████████████████████ (21)
3  │ █████████████████ (17)
4  │ ███████ (7)
5  │ █████ (5)
6  │ ██ (2)
7+ │ █ (1)
```
*(63 non-land cards; commander excluded. 31 of the 63 cost 2 or less. The top end is now two 6-drops and one 8, down from five cards at 6+ in the 2026-09-13 draft. Cutting Casualties of War removes the {2}{B}{B}{G}{G} cost, but **Unnatural Growth's {1}{G}{G}{G}{G} is still the deck's most colour-strained card**.)*

## Short Mulligan and Play Notes
- **Early game (turns 1–4)**: Keep hands with two lands and real acceleration — Llanowar Elves, Sol Ring, Arcane Signet, Golgari Signet, Talisman of Resilience, Twitching Doll or Wood Elves. Gilded Goose is **not** acceleration; it trades a Food for a mana, so do not count it as your ramp when deciding whether to keep. Vampiric Rites, Squirrel Nest or Rat King on turn one to three is an excellent keep even without her: Squirrel Nest and Rat King build a board for free, and Vampiric Rites converts it into cards for {1}{B} a time. Do not over-commit creatures before you have a sacrifice outlet.
- **Mid game (turns 5–8)**: Land Ygra, then find an outlet and one drain payoff. **Woe Strider** is the only outlet that can dump a whole board in one turn. **Vampiric Rites** is the one that survives the wipe and converts the rebuild into cards. **Thornvault Forager** and **Gilded Goose** both read "sacrifice a Food", which under Ygra is any other creature you control, and both add mana — but both tap, so each is one sacrifice per turn. **Chittering Witch** at {1}{B} is the cheap repeatable backup; Chatterfang's {B} ability is removal that eats **Squirrels only**, so do not count it as a general outlet. Once she is online, **let the table fight** — every creature that dies anywhere grows her.
- **Casting Massacre Wurm**: {3}{B}{B}{B} off 21 direct black sources is the deck's hardest cost. Realistically you need Sol Ring, a signet, Twitching Doll, Thornvault Forager or Twilight Mire alongside your lands — plan a turn ahead rather than holding it and hoping. Hazel of the Rootbloom is the easiest way: with three tokens on the board she pays all three black pips by herself.
- **Late game**: Two routes. Grind the pod out with Zulaport Cutthroat, Bastion of Remembrance, Poison-Tip Archer, Nadier's Nightblade and Ninja Teen by sacrificing your board at instant speed, or set up the combat kill: Garruk's Uprising for trample, Unnatural Growth to double her, swing for 21+ commander damage. Swiftfoot Boots make the second plan far harder to disrupt.
- **"In addition to their other types" is the most important line on your commander**: opponents' creatures become Food artifacts but stay creatures. That is why Cankerbloom, Seedship Impact, Wear Down and Thrashing Brontodon can hit them, and why any effect worded *noncreature artifact* cannot. Check the wording before you count something as removal.
- **Destroy vs. exile**: the deck still has **no** exile-based removal at all. Everything destroys, which means the victim becomes a Food in a graveyard: two counters on Ygra and a Terrasymbiosis draw. The cost of that consistency is in Weaknesses below.
- **Decree of Pain: cycle it, don't cast it.** `Cycling {3}{B}{B}` for -2/-2 on all creatures plus a card is the realistic mode — the hard cast at eight is a turn-9 play at best. If you ever do hard-cast it, it destroys all creatures including Ygra, so give her indestructible **first** with Overprotect in response to your own spell. Swiftfoot Boots do **not** help — hexproof does not stop a sweeper that does not target. If she dies alongside the board her triggers still go on the stack but resolve doing nothing, so you get no counters and no Terrasymbiosis draw.
- **Key interactions**: the sacrifice ability Ygra grants costs `{2}, {T}`, so a summoning-sick or tapped creature cannot use it to dodge your removal. Chatterfang's replacement effect applies to *your* tokens only, but to every source. Arasta is a creature despite the enchantment in its type line, so it dies to your own Decree of Pain. Seedship Impact is an instant, so hold it for an opponent's attack or a commander they just recast rather than using it on your own turn.

## Why These Choices (Summary)
- **Ygra converts narrow cards into premium ones**: five pieces of artifact removal double as creature removal, which is how this deck answers threats in a colour pair with almost no sweepers. The flip side is that those five are **dead against a creature board when she is not out**, and an opponent who removes her in response makes the target illegal and fizzles the spell. Wear Down is the clearest case — a two-mana sorcery that kills two creatures.
- **The sweeper hole is finally filled**: Massacre Wurm is one-sided, drains for the rest of the game, and hands Ygra ten counters in a pod. It is the single biggest change in this revision and it cost the deck nothing it was actually using — Zopandrel was redundant with Unnatural Growth.
- **Every drain now scales with the pod**: Zulaport Cutthroat, Bastion of Remembrance, Poison-Tip Archer, Nadier's Nightblade, Ninja Teen and Marauding Blight-Priest all hit **all** opponents, across three different events — a creature you control dying or otherwise leaving, a token you control leaving, and any life you gain. Cutting The Sackville-Bagginses removed the only one that drained a single opponent, so there is no longer a weak link in the package.
- **Free, repeatable fodder beats one-shot fodder**: Squirrel Nest, Rat King and Reassembling Skeleton each produce sacrifice material for zero or near-zero mana every turn. Arasta does the same off opponents' spells. Hazel of the Rootbloom replaces Master of the Wild Hunt as the biggest of these engines. She makes two to four bodies a turn instead of one, but she needs a token already on the board to copy, and she does not give you Master's Wolf-pack fight removal.
- **Outlets got cheaper and more resilient**: Vampiric Rites is a one-mana enchantment that is an outlet *and* a draw engine *and* survives wipes, which Ecstatic Awakener — a one-shot that disabled itself — never was. Woe Strider is still the only unlimited free one.
- **Curve came down while the top end got better**: 31 of 63 non-land cards cost two or less, and the 7-drop is gone. Trample moved from a 6-mana creature to a 3-mana enchantment, and the freed mana went into interaction.
- **Fixing beats raw source count**: Viridescent Bog is back over a plain tapped dual. It does not tap for mana alone, so it scores worse on a source count — but its {1} is generic, so it upgrades *any* land into a black and a green pip at once. Simulated over 30k hands it is worth roughly +2 points on Massacre Wurm and +2.6 on Casualties of War versus the Guildgate, and almost all of that is the fixing rather than the untapped entry. Grim Backwoods became a Swamp for the same reason: it tapped for {C} only, and its {2}{B}{G}-plus-tap outlet was strictly worse than the Vampiric Rites now in the deck.

## Analysis

**Strengths**:
- Ygra profits from other players' removal and combat — in a four-player pod she grows without you spending a card.
- She unlocks a removal suite Golgari cannot normally access, which compensates for the thin sweeper pool.
- Chatterfang roughly doubles the deck's token throughput, and every token is simultaneously a Food, a drain trigger and Skullclamp fodder.
- Six pod-wide drain effects keyed to four different events, so almost nothing leaving the battlefield — or any life you gain — is wasted.
- Two independent win conditions (aristocrats drain and commander damage) sharing one board state, and both halves of the combat kill — Garruk's Uprising and Unnatural Growth — are now wipe-proof enchantments.
- One genuinely one-sided sweeper that is also a drain engine and a ten-counter swing on the commander.

**Weaknesses/Missing Staples**:
- **No exile effects whatsoever.** Bojuka Bog only touches graveyards. Any recursive threat — a commander that keeps returning, anything with "when this dies, return it" — can only be answered temporarily. This is the direct cost of pointing all the removal at destroy effects to feed Ygra, and it is a real trade, not a free win.
- **Most of the payoffs are blind to most of the fuel.** Ygra reads "whenever **a** Food is put into a graveyard" — so roughly 70% of her counters come from *opponents'* creatures dying. But only **four** payoffs can see those deaths: Poison-Tip Archer (`whenever another creature dies`), Ogre Slumlord (`another nontoken creature dies`), Morbid Opportunist (`one or more other creatures die`) and Massacre Wurm (`a creature an opponent controls dies`). Against them, **five** read **"you control"** and see none of it — Zulaport Cutthroat, Bastion of Remembrance, Nadier's Nightblade, Ninja Teen and Moldervine Reclamation — and Marauding Blight-Priest is downstream of their lifegain, so it is effectively a sixth. The deck's fuel comes from the table and most of its payoffs read only your own board. This is close to unfixable: a sweep of the whole collection turned up just two more cards with an unrestricted creature-death trigger, Great Fierce Bee (scry 1) and Moonstone Eulogist (a Blood token), and neither is worth a slot.
- **The engine is outlet-bound, not body-bound.** Simulated across 100k hands, the chance of having *no* creatures is only 8% on turn 4 and 4% on turn 5 — but the chance of having a repeatable sacrifice outlet in play plateaus at about **54% by turn 6**, and 29% of games never assemble Ygra + an outlet + two spare bodies by turn 7 even with no opponent interaction modelled. Ygra's granted `{2}, {T}` ability means you are never *fully* without an outlet, but paying two mana and a tap per body is a tax, not an engine. Hungry Ghoul was added to answer exactly this.
- **Ygra's type-granting is symmetrical, and it cuts against you.** Every creature you control except her is an artifact, so **every opponent's cheap artifact removal is creature removal pointed at your board**, and any mass artifact destruction — Vandalblast, Bane of Progress, Meltdown — is a **one-sided board wipe against you** that leaves their non-artifact permanents alone. Bane of Progress in particular would kill every creature on the table except Ygra *and* your eleven enchantments and eight artifacts, Garruk's Uprising and Unnatural Growth included; the "both halves of the combat kill are wipe-proof enchantments" claim above holds against creature wipes only. Ygra does collect an enormous pile of counters on the way down.
- **Commander-dependent**: much of the deck's power is Ygra's type-changing ability. Against heavy commander hate the artifact-removal package gets much worse. Swiftfoot Boots plus three protection spells (Snakeskin Veil, Undying Malice, Overprotect) now cover targeted removal, but **none of them stop exile or a sweeper**.
- **Double- and triple-pip costs against a 36-land mana base**: counting only lands that tap for the colour without help, the deck has **21 black and 22 green sources** (23 and 24 counting Evolving Wilds and Terramorphic Expanse). Three lands are excluded from that count and two of them are still useful — Viridescent Bog launders any mana into {B}{G} and Twilight Mire converts a coloured mana into two, while Hall of Oracles needs {1} for any colour. Massacre Wurm wants {B}{B}{B}, Unnatural Growth {G}{G}{G}{G} and Decree of Pain {B}{B} (cycled or cast). Six mana rocks and dorks carry more weight than the land count suggests, and Hazel of the Rootbloom adds a seventh source of any-colour mana once a token board is out. **Measured, the strained cost is not Massacre Wurm but Unnatural Growth**: {G}{G}{G}{G} at five mana is roughly 47% on turn 5 and carries an ~19-point colour tax against a single-pip spell of the same cost, where the Wurm's tax is about 5 points. *(This also corrects the previous draft's stated 23/25, which counted filter lands that cannot produce coloured mana unaided.)*
- **Only one instant-speed removal spell under three mana** (Infernal Grasp, joined now by Seedship Impact). Windgrace's Judgment is the next at five. Chatterfang's {B} and Chittering Witch's {1}{B} activated abilities partly cover this, but a cheap instant answer is genuinely absent — a deliberate trade made to keep engine slots.
- **Lost a burst finisher.** Second Harvest could double a ten-token board at instant speed and end the game on the spot. Deadly Brew is the steadier card but has no ceiling like that; if testing shows the go-wide plan beating the grind plan, Harvest is the first card to bring back.
- **The top end is still clunky when the mana is bad.** Decree of Pain at eight and two 6-drops means a slow hand can be genuinely stuck, and Decree still kills Ygra without setup.

## Next Steps (Optional Suggestions)
- **Test Massacre Wurm's castability hard.** If it sits in hand across three games, the fix is not to cut it but to swap a land for a Swamp — and the right land is **Hall of Oracles**, not Titan's Grave or Mirkwood. Hall is one of the three lands excluded from the colour counts (its fixing costs {1}, strictly worse than Viridescent Bog's {1} for two pips) and its +1/+1 ability is sorcery-speed *and* gated on having cast an instant or sorcery that turn, which is near-dead at 15 instants and sorceries. Titan's Grave and Mirkwood at least tap for {B} or {G} unaided and count toward the 21/22.
- Newly in the pool and worth a look if the metagame shifts: **Feed the Swarm** ({1}{B} sorcery, destroys a creature **or enchantment** an opponent controls — black enchantment removal is rare and the deck has none outside Ygra's artifact trick) and **Tribute to Hunger** ({2}{B} instant edict with lifegain, which answers hexproof commanders at instant speed).
- From the 2026-09-25 collection update, two more cards are worth testing. **Corpseberry Cultivator** ({1}{B/G}{B/G}) forages at the start of each of your combats. Under Ygra that is a **free sacrifice of any creature**, once per turn, so it helps the outlet shortage described in Weaknesses. **Break Under Pressure** ({2}{B} instant) makes an opponent sacrifice their highest-mana-value creature or planeswalker, which usually means their commander, and it gets past hexproof. Supper for Spiders is back in the pool too if you ever want it.
- **Deep Forest Hermit** (four Squirrels, eight with Chatterfang, and vanishing sacrifices it for you) remains the best fodder burst in the pool if the go-wide plan proves stronger than the grind.
- Two more sweepers sit in the pool and were **deliberately** passed over; both are worth revisiting only under specific conditions. **The Last Ronin** ({4}{B}{G} Saga) has chapter I *"Destroy all creatures"* — which kills Ygra, on a Saga you cannot hold back. **Swarmyard Massacre** ({3}{B}{B}) makes two Squirrels, then gives -1/-1 per Insect/Rat/Spider/Squirrel you control to each creature that **isn't** one — so it is heavily asymmetric on a wide Squirrel-and-Rat board, but it is *not* one-sided: it also hits Ygra (an Elemental Cat), Massacre Wurm, Academy Manufactor, Woe Strider, Zulaport Cutthroat, Poison-Tip Archer and Wood Elves. Bring it in only if the board reliably skews to the four tribes.
- Dismantling Full Deployment would return **The Ozolith** to the pool — it banks Ygra's counters when she dies, which is the single best answer to the "she gets exiled or wiped" failure mode.

---

## Deck Name

**Table Manners** — In Commander "the table" is the pod, and Ygra has none of these.

*Other candidates considered:*

- **Food Chain** — Punchy two-worder and a double meaning: the deck literally runs on Food tokens, and Ygra sits at the top of the food chain eating everything below her.
- **Bone Appétit** — A pun that captures both halves of the deck: fine dining and a graveyard full of the guests.
- **Clean Plate Club** — She does not stop until the board is empty, which is exactly how the sacrifice-everything turn plays out.

---
Deck created from cards in your moxfield collection (moxfield_latest.csv & card_details.md), excluding cards reserved by Full Deployment, Claws for Concern and Dance of the Elements. Table Manners is the rebuilt Squirreled Away, so it replaces that precon's row in the reserved list.

**Version**: Draft | **Status**: Working version
**Generated**: 2026-10-02

---

## Card Collection Origin

| Card | Mana Cost | Category | Precon(s) |
|------|-----------|----------|-----------|
| Ygra, Eater of All | {3}{B}{G} | Commander | — |
| Academy Manufactor | {3} | Artifact Creature | Squirreled Away |
| Arasta of the Endless Web | {2}{G}{G} | Legendary Enchantment Creature | Squirreled Away |
| Chatterfang, Squirrel General | {2}{G} | Legendary Creature | Squirreled Away |
| Chittering Witch | {3}{B} | Creature | Squirreled Away |
| Gilded Goose | {G} | Creature | Squirreled Away |
| Hazel of the Rootbloom | {2}{B}{G} | Legendary Creature | Squirreled Away |
| Morbid Opportunist | {2}{B} | Creature | Squirreled Away |
| Nadier's Nightblade | {2}{B} | Creature | Squirreled Away |
| Ogre Slumlord | {3}{B}{B} | Creature | Squirreled Away |
| Plaguecrafter | {2}{B} | Creature | Squirreled Away |
| Poison-Tip Archer | {2}{B}{G} | Creature | Squirreled Away |
| Ravenous Squirrel | {B/G} | Creature | Squirreled Away |
| Skyfisher Spider | {2}{B}{G} | Creature | Squirreled Away |
| Tireless Provisioner | {2}{G} | Creature | Squirreled Away |
| Woe Strider | {2}{B} | Creature | Squirreled Away |
| Zulaport Cutthroat | {1}{B} | Creature | Squirreled Away |
| Bastion of Remembrance | {2}{B} | Enchantment | Squirreled Away |
| Binding the Old Gods | {2}{B}{G} | Enchantment | Squirreled Away |
| Gourmand's Talent | {G} | Enchantment | Squirreled Away |
| Moldervine Reclamation | {3}{B}{G} | Enchantment | Squirreled Away |
| Squirrel Nest | {1}{G}{G} | Enchantment | Squirreled Away |
| Arcane Signet | {2} | Artifact | Counter Intelligence; Dance of the Elements; Prismari Artistry; Squirreled Away |
| Chitterspitter | {2}{G} | Artifact | Squirreled Away |
| Golgari Signet | {2} | Artifact | Squirreled Away |
| Skullclamp | {1} | Artifact | Squirreled Away |
| Sol Ring | {1} | Artifact | Counter Intelligence; Dance of the Elements; Prismari Artistry; SonictheHedgehog ChasingAdventure; Squirreled Away; The Bark Ages |
| Talisman of Resilience | {2} | Artifact | Squirreled Away |
| Deadly Dispute | {1}{B} | Instant | SonictheHedgehog ChasingAdventure; Squirreled Away |
| Plumb the Forbidden | {1}{B} | Instant | Squirreled Away |
| Windgrace's Judgment | {3}{B}{G} | Instant | Squirreled Away |
| Decree of Pain | {6}{B}{B} | Sorcery | Squirreled Away |
| Maelstrom Pulse | {1}{B}{G} | Sorcery | Squirreled Away |
| Shamanic Revelation | {3}{G}{G} | Sorcery | Squirreled Away |
| Garruk, Cursed Huntsman | {4}{B}{G} | Legendary Planeswalker | Squirreled Away |
| Bojuka Bog | — | Land | Squirreled Away |
| Command Tower | — | Land | Counter Intelligence; Dance of the Elements; Prismari Artistry; Squirreled Away; The Bark Ages |
| Evolving Wilds | — | Land | Counter Intelligence; Squirreled Away |
| Exotic Orchard | — | Land | Counter Intelligence; Dance of the Elements; Prismari Artistry; Squirreled Away |
| Forest (x9) | — | Basic Land | Dance of the Elements; Foundations Beginner Box; Hare Raising; Squirreled Away; The Bark Ages |
| Haunted Mire | — | Land | Squirreled Away |
| Jungle Hollow | — | Land | Squirreled Away |
| Llanowar Wastes | — | Land | Squirreled Away |
| Necroblossom Snarl | — | Land | Squirreled Away |
| Oran-Rief, the Vastwood | — | Land | Squirreled Away |
| Swamp (x8) | — | Basic Land | Dance of the Elements; Foundations Beginner Box; Squirreled Away |
| Tainted Wood | — | Land | Squirreled Away |
| Temple of Malady | — | Land | Squirreled Away |
| Terramorphic Expanse | — | Land | Prismari Artistry; Squirreled Away |
| Twilight Mire | — | Land | Squirreled Away |
| Viridescent Bog | — | Land | Squirreled Away |
| Woodland Cemetery | — | Land | Squirreled Away |
| Garruk's Uprising | {2}{G} | Enchantment | Dance of the Elements |
| Hall of Oracles | — | Land | Prismari Artistry |
| Snakeskin Veil | {G} | Instant | Foundations Beginner Box; The Bark Ages |
| Hazel's Nocturne | {3}{B} | Instant | — |
| Hungry Ghoul | {1}{B} | Creature | Foundations Beginner Box |
| Infernal Grasp | {1}{B} | Instant | — |
| Lich's Relic | {B} | Artifact | — |
| Marauding Blight-Priest | {2}{B} | Creature | — |
| Massacre Wurm | {3}{B}{B}{B} | Creature | — |
| Ninja Teen | {2}{B} | Enchantment | — |
| Rat King, Verminister | {1}{B} | Legendary Creature | — |
| Reassembling Skeleton | {1}{B} | Creature | Foundations Beginner Box |
| Undying Malice | {B} | Instant | Foundations Beginner Box |
| Vampiric Rites | {B} | Enchantment | — |
| Cankerbloom | {1}{G} | Creature | — |
| Hunter's Talent | {1}{G} | Enchantment | — |
| Llanowar Elves | {G} | Creature | Foundations Beginner Box |
| Outland Liberator // Frenzied Trapbreaker | {1}{G} | Creature | — |
| Overprotect | {1}{G} | Instant | — |
| Seedship Impact | {1}{G} | Instant | — |
| Terrasymbiosis | {2}{G} | Enchantment | — |
| Thornvault Forager | {1}{G} | Creature | — |
| Thrashing Brontodon | {1}{G}{G} | Creature | Foundations Beginner Box |
| Twitching Doll | {1}{G} | Artifact Creature | — |
| Unnatural Growth | {1}{G}{G}{G}{G} | Enchantment | — |
| Wear Down | {1}{G} | Sorcery | — |
| Wood Elves | {2}{G} | Creature | — |
| Illegitimate Business | — | Land | — |
| Mirkwood | — | Land | — |
| Swiftfoot Boots | {2} | Artifact | SonictheHedgehog TurboGear |
| Titan's Grave | — | Land | — |
| Deadly Brew | {B}{G} | Sorcery | — |
| Vinereap Mentor | {B}{G} | Creature | — |
