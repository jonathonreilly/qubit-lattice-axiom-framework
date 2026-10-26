# Attack on T76: The frozen-box black hole (no formation rule, volume not area, clause C1, no holography)

Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md`, `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`; also lane entries, probe 19 note and runner, viability map, July frozen-region note, b53 note. Claude Sonnet 5.5, same vendor family as the supervisor; checks are same-family.

## Verdict in plain words
The wall bundles three questions: which rule, which entropy, where 1/4 comes from. In 2D, every "form if k recorded neighbours is in A" rule except one has a local switch, so its frozen count is volume-law. The exception, rule E ("form unless exactly one neighbour is recorded"), looked boundary-determined to L = 10, then gains interior swaps of about 40 sites from L = 11. No supplied rule gives an area-law count, and record contents may add volume to any. The wall stands; fixing the entropy first is cheaper.

## The wall (checked)
- Plain: A box fills with permanent records until nothing more can form; the owner reads that as a black hole. Black-hole entropy grows with surface area, but the number of ways to fill a box is one, or grows with volume, for the simple rules tried. The axioms give no rule, entropy or 1/4.
- Precise: Target: a formation rule and an entropy S on the reachable frozen states of a sealed box, S proportional to area with coefficient 1/4 at a = l_P. Passing needs the rule, a proved scaling and an identified S.
- Real? Yes, corrected. L15-W8 and L01-W13 are one wall; L15-W9 is downstream. L14-W19 belongs with T11: July record-time is a count halting by permanence (`archive/notes/docs/FROZEN_REGION_…_2026-07-03.md:184-207`), C1 is a rate; in b53's log-linear model (`docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_…:26`) log w stays finite, so no zero-rate region occurs (suggested). No open PR (36 scanned) or archive note solves it.

## Load-bearing premises
AX = minimal axioms; p19 = probe 19; MAP = viability map.

| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |
|---|---|---|---|---|---|
| Count-threshold rule | supplied | p19:101-105; AX:65-73,183-184 | other rules escape | 2 families + E | classification below |
| S = flat count of occupation sets | supplied | p19:107-109,198-206 | weights, contents, entanglement change scaling | no | scale each candidate S |
| Contents left out | hidden | AX:57-61,70-73,79,92 | a menu of 2+ gives volume | no | is the menu a singleton on E's states? |
| Sealed box, outside unrecorded | supplied | p19:98-99 | real exterior is active | no | recount E, recorded wall |
| a = l_P, quarter imported; frozen = black hole | gap; reading | PRIMITIVE_REGISTRY_CHECK:50-52; MAP:284-306 | no coefficient or content | no | moot until scaling proved |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |
|---|---|---|---|---|---|---|---|
| R1 rigid rule | Lane: E has no sealed switch at any window size | "every rule has a switch" | E's swaps cannot repeat independently | two independent swaps near L = 24 | 1 day | a non-volume member | nearly dead: shell-determination fails from L = 11 |
| R2 count the surface | Outside: loop-gas entropy is (\|∂A\|-1) ln 2 though configurations number 2^V (Hamma-Ionicioiu-Zanardi, PRA 71, 022315); horizon punctures (Ashtekar et al., PRL 80, 904) | S = interior count | contents obey an order-independent constraint | a confluent content rule on E | days | coefficient tuned, not derived | wounded: needs record-to-amplitude bridge (T03/T05) |
| R3 misframed | Jammed-pack counts are Edwards entropy, extensive by design (Edwards-Oakeshott, Physica A 157, 1080). Cheaper question: is the contents menu a singleton on frozen states; if not, is the exterior-visible shell count the entropy? | flat-count target | the exterior sees the shell | the singleton check | hours | one yes/no replaces the wall | survives as a question |

## Test run
- Pre-registered (`T76_scratch/PREREGISTRATION.md`; scripts alongside): PASS-A if a non-trivial rule has no sealed gadget; PASS-B if its count is boundary-like (ln N/L stable, ln N/L² falling over three sizes), strong only with an upper bound.
- Result:
  - Probe 19's block lemma holds with "sealed" for "crowding": 16-64 built combinations in 5 cases (2D {0,3}, {0,3,4}, {0,1}; 3D {0,1,4}, {0,3,5}), all distinct and frozen.
  - 2D: 14 of 15 non-trivial rules with 0 in A have a gadget ({0,3}, {0,3,4} need 5x5); E has none. 3D: 36 of 63; 27 open, including E3 and the referee's {0,3,4,5,6}.
  - E reproduces probe 19 (1, 7, 13, 27); N(6..13) = 17, 69, 87, 171, 217, 615, 1039, 2399. ln N/L is 0.54-0.60 and ln N/L² falls 0.086 to 0.046, yet a quadratic fits better (SSE 0.10 against 0.28).
  - Given the outermost shell, reachable E states have one completion for L ≤ 10, two for L = 11-13; ambiguous shells number 1, 4, 16, each pair differing on 40 interior sites (L = 12). Two-deep shells suffice to L = 12, not 13.
  - 3D E3: 11, 10, 26 for L = 2-4; L = 5 not finished.
- Reading: PASS-A met; PASS-B a weak fit, contradicted by the shell result.

## Outcome
STANDS. Best route: R3's singleton check first (hours); if contents are free, R1 is moot.

## Claims and labels
- Sealed-gadget volume law: checked by construction; proof as probe 19 lemma C, unrefereed.
- E has no sealed gadget; each empty component of a frozen E state meets the outer layer: suggested (extremal-site argument), checked for L ≤ 10.
- E counts and shell results: checked (own code, matching probe 19 for L ≤ 5). E's asymptotics and 3D: open.
- Contents add volume unless the menu is a singleton: suggested (AX:70-73). Edwards reading: reading. Citations from memory, templates only.
