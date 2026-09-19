# Shadowfax, Lord of Horses — Horse & Unicorn Cavalry

**Commander:** Shadowfax, Lord of Horses — `{3}{R}{W}` — Legendary Creature — Horse — 4/4
**Colour identity:** Boros (R/W)
**Format:** Commander, built for **multiplayer (3–4 opponents)**
**Card pool:** Every card in Magic — *not* built from the local collection. This is a buy/proxy list.
**Approximate cost:** ~$520 at market. See **Budget swaps** — eight cards carry ~$350 of that, and all eight have working substitutes.
**Status:** Draft — reviewed against EDHREC (2,189 Shadowfax decks) and revised across six specialist review passes and a final cohesion pass.

> **Format note:** this deck is not sourced from `moxfield_latest.csv`, so it has no *Card Collection Origin* table and no `Custom Decks/Moxfield/` export. It lives at the repo root alongside the other whole-pool lists. Every mana cost and category below was generated directly from Scryfall data, not typed by hand.

---

## ⚠️ Read this first — two of the five cards can't go in

| Card | Colour identity | Legal under Shadowfax? |
|---|---|---|
| **Valorous Steed** | `{W}` | ✅ In the deck |
| **Ronom Unicorn** | `{W}` | ✅ In the deck |
| **Diamond Mare** | Colourless | ✅ In the deck |
| **Emiel the Blessed** | `{G}{W}` | ❌ **Illegal** |
| **Lathiel, the Bounteous Dawn** | `{G}{W}` | ❌ **Illegal** |

Shadowfax is **red-white**, not green. Commander legality is by colour identity, so any card with a green mana symbol — in its cost, its rules text, or a hybrid activation — cannot be in a Shadowfax deck.

Emiel the Blessed costs `{2}{W}{W}`, so it *looks* castable, but its blink ability costs `{G/W}` — that hybrid green pip puts it at G/W identity. Lathiel is G/W outright. Both are Unicorns, and both are out.

If your friend would rather keep those two, the deck has to change colours:

- **Keep Shadowfax** (this list). Haste, the cheat-in trigger, Calamity, Hellrider, Purphoros, Shared Animosity — but no Emiel, no Lathiel.
- **Lathiel, the Bounteous Dawn as commander** (G/W). Emiel fits in the 99 and it's still a Unicorn lifegain deck, but you lose Shadowfax and the whole red half of this list.

I built the Shadowfax version because that's what was asked for. Say the word and I'll build the Lathiel one instead.

---

## How the deck wins

**Shadowfax does two things.** *Horses you control have haste* — including himself, so he attacks the turn he lands. And *whenever Shadowfax attacks, you may put a creature card with lesser power from your hand onto the battlefield tapped and attacking.*

"Lesser power" means lesser than **Shadowfax's current power** (confirmed by official ruling), so every anthem widens what you can cheat in:

| Shadowfax's power | You can drop a creature with power… |
|---|---|
| 4 (base) | 3 or less — **26 of the 32 creatures in this deck** |
| 5 (Flowering of the White Tree, Icon of Ancestry naming Horse) | 4 or less — adds Calamity, Roaming Throne |
| 6+ (Balefire Liege, Door of Destinies, Keleth's counters) | 5 or less — adds **both Sunmares** |

Be honest about what this ability is: at base power it's a **consistent value engine**, not a way to cheat in bombs. It drops a one- to three-drop for free every combat — and because the creature enters the battlefield normally, that's a free Purphoros trigger, a free Cathars' Crusade trigger, a free Soul Warden trigger. The actual bombs only come online once an anthem has Shadowfax at 6+ power.

One rules note: the cheated-in creature enters **tapped and attacking** but was never *declared* as an attacker, so it won't trigger its own "whenever this attacks" abilities. It does trigger everything that cares about entering the battlefield.

**Crested Sunmare is the multiplayer payoff.** *At the beginning of **each** end step, if you gained life this turn, create a 5/5 white Horse.* In a four-player game that's **up to four 5/5s per turn cycle**, not one. It also gives every *other* Horse indestructible — note it does **not** protect itself, so Swiftfoot Boots on the Sunmare is often the right play.

The deck runs cheap lifegain purely to keep that condition switched on:

- **Soul Warden** is the best of them — it triggers on *any* creature entering, including your opponents' on their own turns. That's what keeps the Sunmare live during other people's end steps. (Impassioned Orator-style effects only count your own; Soul Warden has no such restriction.)
- **Balefire Liege** gains you 3 life on every white spell you cast, which is far more reliable than connecting with a lifelinker.
- Mesa Unicorn, Splendor Mare, Shield Mare, Celestial Unicorn, Diamond Mare and Thurid fill in the rest.

**Then you close.** Shared Animosity converts a wide board into lethal across the table; Hellrider and Purphoros drain all three opponents regardless of blockers; Akroma's Will and Kindred Charge finish.

**Roaming Throne, naming Horse, is the best non-commander card in the deck.** It doubles Shadowfax's attack trigger (two free creatures per combat) *and* Crested Sunmare's end-step trigger (two 5/5s per end step — up to eight per round in a four-player pod).

**Thurid, Mare of Destiny** copies every **Pegasus, Unicorn or Horse** creature spell you cast and pumps all three tribes. Worth knowing: her own type line is `Legendary Creature — Pegasus` only, so she is **not** a Horse or a Unicorn. She misses Cavern of Souls, Path of Ancestry, Shared Animosity's type-sharing and every "name a type" anthem. She earns her slot on cast triggers alone.

---

## Decklist (100)

### Commander (1)

| Card | Mana Cost | Category | Role |
|---|---|---|---|
| Shadowfax, Lord of Horses | {3}{R}{W} | Legendary Creature | Haste for all Horses; cheats a creature in per attack |

### Creatures (32)

| Card | Mana Cost | Category | Role |
|---|---|---|---|
| Soul Warden | {W} | Creature | Lifegain on ANY creature entering - keys Crested Sunmare on opponents' turns |
| Capashen Unicorn | {1}{W} | Creature | Sacrifice: destroy an artifact or enchantment |
| Diamond Mare | {2} | Artifact Creature | **Friend's pick** - repeatable lifegain on your chosen colour |
| Gilded Ghoda | {1}{R} | Creature | Mount; Treasure on attack while saddled |
| Keleth, Sunmane Familiar | {1}{W} | Legendary Creature | +1/+1 counter on Shadowfax each attack - raises the cheat threshold |
| Mesa Unicorn | {1}{W} | Creature | Cheap lifelink Unicorn |
| Metallic Mimic | {2} | Artifact Creature | Name Horse; counters land on Sunmare's tokens too |
| Regal Bunnicorn | {1}{W} | Creature | Power/toughness = your nonland permanents; often huge |
| Ronom Unicorn | {1}{W} | Creature | **Friend's pick** - sacrifice to destroy an enchantment |
| Bloodline Pretender | {3} | Artifact Creature | Changeling; grows when your chosen type enters |
| Celestial Unicorn | {2}{W} | Creature | Grows on every lifegain trigger |
| Mentor of the Meek | {2}{W} | Creature | Pay {1} to draw whenever a power-2-or-less creature enters |
| Mirror Entity | {2}{W} | Creature | Changeling; {X} makes your team X/X with ALL creature types |
| Shield Mare | {1}{W}{W} | Creature | Gain 3 on entry and when an opponent targets it; unblockable by red |
| Splendor Mare | {2}{W} | Creature | Lifelink, or cycle it away |
| Summon: Ixion | {2}{W} | Enchantment Creature | Saga Unicorn - exiles a creature, then hands out counters |
| Taurean Mauler | {2}{R} | Creature | Changeling (Horse AND Unicorn); grows off opponents' spells |
| Welcoming Vampire | {2}{W} | Creature | Draws once per turn off your small creatures entering |
| Bill the Pony | {3}{W} | Legendary Creature | Two Food tokens = 6 life on demand, feeding Crested Sunmare; power 1, so always cheatable |
| Excava, the Risen Past | {2}{R}{W} | Legendary Creature | Flying haste; returns a permanent of MV 3 or less each attack |
| Hellrider | {2}{R}{R} | Creature | 1 damage per attacker straight to the defending player |
| Inspiring Unicorn | {2}{W}{W} | Creature | Team +1/+1 on every attack |
| Irregular Cohort | {2}{W}{W} | Creature | Changeling that brings a second changeling token |
| Loyal Unicorn | {3}{W} | Creature | Prevents all combat damage to your team - on YOUR turn, with Shadowfax out |
| Purphoros, God of the Forge | {3}{R} | Legendary Enchantment Creature | 2 damage to EACH opponent per creature entering; dodges most wipes |
| Roaming Throne | {4} | Artifact Creature | Name Horse - **doubles** Shadowfax's attack trigger and Sunmare's end-step trigger |
| Thurid, Mare of Destiny | {2}{W}{W} | Legendary Creature | Lord for Horses/Unicorns/Pegasi AND copies those creature spells |
| Balefire Liege | {2}{R/W}{R/W}{R/W} | Creature | Shadowfax is red AND white, so he gets both anthems (+2/+2); 3 life per white spell |
| Crested Sunmare | {3}{W}{W} | Creature | 5/5 Horse each end step you gained life; other Horses indestructible |
| Guardian Sunmare | {3}{W}{W} | Creature | Mount; tutors a permanent of MV 3 or less onto the battlefield |
| Valorous Steed | {4}{W} | Creature | **Friend's pick** - 3/3 vigilance plus a 2/2 Knight |
| Calamity, Galloping Inferno | {4}{R}{R} | Legendary Creature | Mount; copies its saddlers, tapped and attacking |

### Artifacts & Mana (13)

| Card | Mana Cost | Category | Role |
|---|---|---|---|
| Sol Ring | {1} | Artifact | Ramp |
| Arcane Signet | {2} | Artifact | Ramp |
| Boros Signet | {2} | Artifact | Ramp |
| Fellwar Stone | {2} | Artifact | Ramp |
| Strionic Resonator | {2} | Artifact | Copy a triggered ability - a second cheat-in or a second Sunmare token |
| Swiftfoot Boots | {2} | Artifact | Hexproof for Shadowfax or Crested Sunmare |
| Sword of the Animist | {2} | Legendary Artifact | Fetches a basic land on attack |
| Talisman of Conviction | {2} | Artifact | Ramp; adds a red source |
| Herald's Horn | {3} | Artifact | Name Unicorn - cost reduction plus free cards off the top |
| Icon of Ancestry | {3} | Artifact | Name Horse - anthem that also pumps Shadowfax |
| Door of Destinies | {4} | Artifact | Name Horse - snowballing anthem, compounds the cheat threshold |
| Maskwood Nexus | {4} | Artifact | Your creatures are EVERY type - dissolves the Horse/Unicorn split |
| Vanquisher's Banner | {5} | Artifact | Name Unicorn - anthem plus draw on every Unicorn you cast |

### Enchantments (6)

| Card | Mana Cost | Category | Role |
|---|---|---|---|
| Reconnaissance | {W} | Enchantment | {0}: pull an attacker out of combat and untap it - survives the crack-back |
| Flowering of the White Tree | {W}{W} | Legendary Enchantment | +1/+1 to the team, +2/+1 and ward {1} to your six legends |
| Aggravated Assault | {2}{R} | Enchantment | Repeatable extra combats = repeatable free creatures |
| Ghostly Prison | {2}{W} | Enchantment | Taxes attacks against you - blunts the archenemy problem |
| Shared Animosity | {2}{R} | Enchantment | The finisher - scales with every shared creature type |
| Cathars' Crusade | {3}{W}{W} | Enchantment | +1/+1 counters on everything, every time a creature enters |

### Instants (9)

| Card | Mana Cost | Category | Role |
|---|---|---|---|
| Path to Exile | {W} | Instant | Removal |
| Swords to Plowshares | {W} | Instant | Removal |
| Boros Charm | {R}{W} | Instant | Team indestructible, 4 damage, or double strike |
| Chaos Warp | {2}{R} | Instant | Red's answer to any permanent |
| Deflecting Swat | {2}{R} | Instant | Free redirect of removal or a key trigger |
| Flawless Maneuver | {2}{W} | Instant | **Free** team indestructible while you control a commander |
| Generous Gift | {2}{W} | Instant | Catch-all removal |
| Teferi's Protection | {2}{W} | Instant | The only card here that beats exile and -X/-X wipes |
| Akroma's Will | {3}{W} | Instant | Double strike + protection, or both - usually lethal |

### Sorceries (3)

| Card | Mana Cost | Category | Role |
|---|---|---|---|
| Vandalblast | {R} | Sorcery | Overload wrecks the table's artifacts, not yours |
| Seize the Day | {3}{R} | Sorcery | Extra combat; with Loyal Unicorn's vigilance, untapping Shadowfax is enough |
| Kindred Charge | {4}{R}{R} | Sorcery | Copies every creature of ONE chosen type, with haste |

### Lands (36)

| Card | Mana Cost | Category | Role |
|---|---|---|---|
| Arena of Glory | &mdash; | Land | Haste outlet for non-Horses |
| Arid Mesa | &mdash; | Land | Fetches a dual |
| Battlefield Forge | &mdash; | Land | Untapped dual |
| Boros Garrison | &mdash; | Land | Bounce dual |
| Cavern of Souls | &mdash; | Land | Name Horse - uncounterable Shadowfax and Sunmare |
| Clifftop Retreat | &mdash; | Land | Dual |
| Command Tower | &mdash; | Land | Dual |
| Exotic Orchard | &mdash; | Land | Fixing |
| Furycalm Snarl | &mdash; | Land | Dual |
| Inspiring Vantage | &mdash; | Land | Early untapped dual |
| Mountain (x7) | &mdash; | Basic Land | - |
| Path of Ancestry | &mdash; | Land | Horse-locked (Shadowfax's only type); scry on every Horse |
| Plains (x10) | &mdash; | Basic Land | - |
| Rugged Prairie | &mdash; | Land | Filter land |
| Sacred Foundry | &mdash; | Land | Shock dual |
| Secluded Courtyard | &mdash; | Land | Name Unicorn - also pays for activated abilities |
| Spectator Seating | &mdash; | Land | Untapped with 2+ opponents |
| Sunbaked Canyon | &mdash; | Land | Untapped dual; cantrips late |
| Sundown Pass | &mdash; | Land | Dual |
| Temple of Triumph | &mdash; | Land | Scry dual |
| Three Tree City | &mdash; | Legendary Land | Name Horse - scales with Sunmare tokens |
**Counts:** 1 commander + 32 creatures + 13 artifacts + 6 enchantments + 9 instants + 3 sorceries + 36 lands = **100**.

---

## Naming the creature type

Ten cards make you pick **one** creature type. The deck's census, counted from type lines: **9 Horses** (including Shadowfax), **10 Unicorns**, **4 changelings** (which count as both), 9 that are neither, and 2 more — Metallic Mimic and Roaming Throne — that adopt whichever type you name. Note those two are *not* changelings; they become one chosen type only.

| Card | Name | Why |
|---|---|---|
| Icon of Ancestry | **Horse** | Its anthem pumps Shadowfax himself, widening the cheat threshold |
| Door of Destinies | **Horse** | Each Horse cast grows Shadowfax, which compounds the cheat threshold again |
| Metallic Mimic | **Horse** | Counters land on Crested Sunmare's 5/5 tokens as they enter, making them 6/6 |
| Roaming Throne | **Horse** | Doubles Shadowfax's attack trigger and the Sunmare's end-step trigger |
| Cavern of Souls | **Horse** | Making Shadowfax and Crested Sunmare uncounterable matters most |
| Three Tree City | **Horse** | Its mana scales with board count, and Sunmare tokens flood the board late |
| Herald's Horn | **Unicorn** | The Unicorns are the cheap half you actually cast from hand |
| Vanquisher's Banner | **Unicorn** | Its draw fires on *cast* spells only — Sunmare's tokens never trigger it |
| Secluded Courtyard | **Unicorn** | Unlike Cavern, it also pays for activated abilities, and the Unicorns have them |
| Kindred Charge | **At the table** | Copy whichever type is wider that turn — usually Horse, once tokens pile up |

**Path of Ancestry is not a choice.** It triggers on creatures sharing a type with your commander, and Shadowfax's only type is Horse — so it is permanently Horse-locked.

**The changelings are the real fix.** Taurean Mauler, Mirror Entity, Irregular Cohort and Bloodline Pretender are every creature type at once, so they benefit from every card above regardless of what you named. **Maskwood Nexus** makes your whole board every type while it's out, and **Mirror Entity**'s activation does the same for one turn.

> **Mirror Entity caveat:** its ability *rebases* power and toughness to X/X — it doesn't add. If X is lower than your Crested Sunmare's or Purphoros's power, you will shrink your own best creatures. Only activate for X greater than your biggest body.

---

## Budget swaps

The list runs about **$520**. These eight cards are ~$350 of it, and none are load-bearing:

| Cut (approx.) | Swap in | Cost |
|---|---|---|
| Deflecting Swat (~$71) | Wear // Tear | ~$1 |
| Roaming Throne (~$53) | Patchwork Banner | ~$3 |
| Cavern of Souls (~$51) | Unclaimed Territory | ~$1 |
| Teferi's Protection (~$50) | Unbreakable Formation | ~$0.30 |
| Aggravated Assault (~$36) | Relentless Assault | ~$2 |
| Three Tree City (~$31) | Plains | — |
| Purphoros, God of the Forge (~$30) | Impact Tremors | ~$1 |
| Arid Mesa (~$28) | Evolving Wilds | ~$0.25 |

That brings the deck to roughly **$180** while keeping the engine intact. Two honest caveats: **Unbreakable Formation only grants indestructible**, so the budget build has no answer to exile wipes at all; and **Roaming Throne's trigger-doubling has no cheap equivalent** — Patchwork Banner is an anthem, not a replacement for the effect.

---

## Known weak points

Three things the review passes flagged that are worth saying out loud rather than hiding:

**1. The mana is stretched, and red is the weaker half.** Reliable sources come to roughly **25 white and 23 red** against 36 lands and five rocks. Frank Karsten's guidance wants ~29 sources to cast a double pip on curve, so all of the double-costed cards are slightly under-supported — Hellrider `{2}{R}{R}`, Calamity `{4}{R}{R}` and Kindred Charge `{4}{R}{R}` most of all. They're late enough in the game that you'll usually have seen the sources, but expect the occasional awkward hand. This is why Aurelia, the Warleader (`{2}{R}{R}{W}{W}`) is deliberately *not* in the list despite being an excellent Shadowfax card.

**2. Board wipes are the deck's worst outcome, and the protection is thinner than it looks.** Boros Charm, Flawless Maneuver and Akroma's Will all grant **indestructible only**. That beats Wrath of God and Blasphemous Act. It does **nothing** against exile wipes (Farewell) or toughness-reduction wipes (Toxic Deluge) — indestructible doesn't save a creature from dying at zero toughness. **Teferi's Protection is the only card in the deck that beats everything**, because phasing out sidesteps the whole category. Purphoros quietly dodges most wipes too: it's indestructible and usually isn't even a creature while your red devotion is below five.

**3. This deck makes you the archenemy.** Purphoros and Hellrider hit every opponent every turn, with no regard for blockers. That's the deck's real power, and it also paints a target on you by about turn six. **Ghostly Prison** is in the list specifically to buy back the time that costs you. If the pod is very casual, consider cutting Hellrider for a fourth piece of interaction — it's the most generically powerful card in the deck and the least tied to the Horse/Unicorn plan.

---

## Things worth knowing at the table

- **Shadowfax's trigger is a "may," and it's on attack, not on damage.** Declare attackers, let the trigger resolve, then pick the creature. It must come from **hand** — not the graveyard, not exile.
- **Crested Sunmare checks "if you gained life this turn" at each end step.** That's an intervening-if clause, so the lifegain must already have happened when the end step begins. Attacking with a lifelinker covers your own turn; Soul Warden covers everyone else's.
- **An extra combat does not give you a second Sunmare token.** Aggravated Assault and Seize the Day add combat and main phases, not end steps — so there's still only one end-step check per turn. What they *do* give you is a second Shadowfax cheat-in and a second Shared Animosity count.
- **Loyal Unicorn only protects on your own turn**, at the beginning of combat, and only while Shadowfax is on the battlefield. It does nothing on opponents' turns.
- **Reconnaissance is best used at end of combat, not before blockers.** Activate it after damage and your creature has already dealt its damage (lifelink included, feeding the Sunmare) and *then* untaps — so it can still block on the crack-back.
- **Kindred Charge copies one chosen type only.** Purphoros, Hellrider, Soul Warden, Welcoming Vampire and Mentor of the Meek are not Horses or Unicorns and will not be copied. Changelings will be.
- **Mounts (Gilded Ghoda, Guardian Sunmare, Calamity)** must be saddled at sorcery speed *before* combat, and the creatures that saddle become tapped — so they can't attack or block afterwards. Saddle with creatures you weren't attacking with anyway.
- **Guardian Sunmare's Saddle 4 is a real cost, not just a number.** Tapping four power of creatures before combat removes them from the attack — which directly shrinks Shared Animosity's per-attacker bonus and Hellrider's per-attacker damage on the very turn you're deploying it. Gilded Ghoda and Calamity are only Saddle 1, so they don't have this problem.
- **Coat of Arms is deliberately not in this deck.** It pumps *every* creature on the battlefield, opponents' included; in a four-player pod that often helps the table more than it helps you. Maskwood Nexus does the job safely.
- **Thundermare is also deliberately absent** despite being a hasty Horse: it taps *all other* creatures, including your own, so casting it precombat turns off your own attack. It's a trap in a go-wide deck.
