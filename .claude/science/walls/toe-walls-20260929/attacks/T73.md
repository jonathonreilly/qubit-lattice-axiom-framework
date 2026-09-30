# Attack on T73: The axioms define no entropy; five candidates disagree

Attacker: Claude Sonnet 5.5, same vendor family as the supervisor (Opus 5.5); same-family checks, not independent referees.

Read: `docs/MINIMAL_AXIOMS_2026-06-29.md` and `PRIMITIVE_REGISTRY_CHECK.md`, both in full. Also L15 W1-W3; probes 19 and 7 (#9363); the 2026-09-20 formation-order note (T1, T2; `ADMISSIBILITY_RULE_HOW_RECORDS_FORM_STATIC_LAW_OUTSIDE_THE_HULL_...`); AREA_LAW no-go; BP probe; DEFERRED_DECISIONS.

## Verdict in plain words
Real, but a symptom of two open gates, not a separate obstruction. A record entropy needs a law for how records form (order, rate, neighbours already written) and a rule for what counts as "the same" from outside. With both, the flat count and the process entropy are defined and ordered. Without them, one set of allowed frozen boxes carries entropies growing like the log, the surface or the volume, with any coefficient (checked). Choosing among the five cannot fix an area law; the measure does.

## The wall (checked)
- Plain: The axioms give permanent records but no odds for whole patterns and no "macroscopically the same". Entropy needs both. The notes use five "entropies": a rank fraction, a count of frozen patterns, that count weighted by likelihood, entanglement of matter, and a gravity-action charge. Until one is fixed, "S = area/4" is undefined.
- Precise: Target: a functional S of record configurations (`MINIMAL_AXIOMS:92`) fixed by the axioms plus registered primitives. Pass: derive or rule out a unique S, or give a class where candidates agree. Naming one is not a pass.
- Real? Core yes: no note, archive or open PR (36 checked) defines a record entropy. Misstated: the rank fraction is not an entropy (`PLANCK_ANCHOR_BP_DERIVATION_PROBE_2026-06-05.md:87-101`); flat and weighted counts are ordered, S1 <= S0, not rivals; entanglement needs a wave state, Wald an action.

## Load-bearing premises
| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |
|---|---|---|---|---|---|
| State = record configuration, no wave | axiom | MINIMAL_AXIOMS:92 | state entropies native | probe 7 | none |
| Odds' form, formation order/rate open; no measure in `realized_state_primitive` | axiom, gate, primitive | :57-73, :183-184, :210-212; REGISTRY_CHECK:103-114 | weighted entropy defined | formation-order note | fix a predecessor structure |
| No additive scalar functional | axiom (cut 08-13) | :148-151, :220-225 | Hartley ln N native | no | owner decision |
| No coarse-graining; observability open | axiom, gate | :47, :82-84, :185-186 | Boltzmann entropy vs partition | probe 19 counts occupations only | fix a readable layer, recount |
| One BH entropy is a functional of the record ensemble | hidden | L15-W2 target | types differ | this attack | type-check |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |
|---|---|---|---|---|---|---|---|
| R1 support only | Hartley/Renyi: a monotone additive support functional is c ln N (Hartley, BSTJ 7:535, 1928; Erdos, Ann. Math. 47:1, 1946) | measure | additivity returns; support map supplied | S1 <= S0; test A | small | T74, T76 | wounded: additivity cut; S0 is volume law for crowding rules (probe 19 C): names S, returns failure to T76 |
| R2 jamming | Edwards flat measure on blocked states, justified by tapping (Edwards-Oakeshott, Physica A 157:1080, 1989; Evans, RMP 65:1281, 1993) | measure, by hypothesis | permanence allows exploration | flat vs sequential measure | small | T05 | dead: permanence forbids tapping; measures differ (test A); static law outside formation hull (T1, six-axis rule) |
| R3 misframed | Ask "which predecessor structure, kernels, partition?" then compute S (T2: order, rates drop out) | single-S premise | one question suffices | test B | small | T01, T05, T10, T74, T76 | survives; blocked-equivalent to T01's open choice |

## Test run
- Pre-registered (`T73_scratch/PREREGISTER.md`): canonical if uniform-sequential S1/S0 >= 0.95 and a weight family moves it < 5%; else measure-driven. Scripts `T73_scratch/test_T73.py`, `test_T73_extra.py`; support: maximal independent sets (probe 19, m = 0).
- Result: N matches probe 19. Uniform sequential S1/S0 = 0.918, 0.910, 0.914 (L = 4-6); S1/L^2 = 0.215, 0.214, 0.214, 0.213 (L = 3-6). 1D: S1/S0 -> 0.954; density 0.4323 (exact sequential value) vs flat 0.4115; KL 0.0128 nats/site. Weights w = 0.1, 0.3, 1, 3, 10 (L = 5): S1/S0 = 0.29, 0.63, 0.91, 0.97, 0.90. Three laws, one support, outputs verified maximal (L <= 7): volume (S1/L^2 flat); seed (raster from a random start) 1.74 to 4.78 for L = 3-10, below ln 8L^2; ring (random boundary ring, raster interior) S = P/4 at one bias w* = 0.385 (L >= 6), P = 4(L-1).
- Reading: measure-driven. 1D passes the canonical threshold narrowly; 2D and the family fail. The ring's tunable 1/4 is the kind of selector p* = 0.0686 is (`AREA_LAW_PRIMITIVE_EDGE_ENTROPY_SELECTOR_NO_GO:55-80`). Caveats: seed and ring use a global sweep or the box boundary (not translation covariant); for w != 1 sizes are too small to classify; volume growth is shown only at w = 1.

## Outcome
**PRICED.** T73 is equivalent to two named gates: the formation measure (`MINIMAL_AXIOMS:181-184`; parked as `DEFERRED_DECISIONS:21-48`) and the observability partition (`:185-186`). With both, S1 and S0 are defined. Without a measure only Hartley's ln N remains, needing additivity (cut) and a support map (unspecified). Necessity suggested; toy checked.

## Claims and labels
- Candidates are different types (count-trace, ensemble, state, action): suggested.
- S1 <= S0, equality iff flat: proved (Jensen); checked in every row.
- On one support the measure changes the coefficient (0.29-0.97 of S0 at L = 5) and the class (log, surface, volume): checked, toy. Sequential measure exponentially far from flat: checked, 1D.
- Hartley uniqueness, Edwards route: templates from memory.
- Replica unification of entanglement and Wald (Lewkowycz-Maldacena, JHEP 08:090, 2013) needs the log-det gate (`:180`): suggested. Siblings moved: T01, T05, T10, T74, T76.
