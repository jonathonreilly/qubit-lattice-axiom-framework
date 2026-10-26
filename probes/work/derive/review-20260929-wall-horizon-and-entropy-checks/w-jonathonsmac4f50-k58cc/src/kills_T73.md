# Kill check on T73

Checker: Claude Sonnet 5.5, same vendor family as attacker and supervisor (Opus 5.5); a same-family check, not an independent referee. Read: axioms memo, registry check, L15-W2, attack, probe 19, formation-order note. Scratch: `kills/T73_scratch/`.

## Outcome verdict
**WEAKENED.** PRICED stands for record-ensemble entropies; three plain-language claims outrun the test. Nothing overturns it. All scripts reproduce the attack's output; an independent rewrite matches N, S1, the seed-law entropies and the cycle-MIS counts. No numeric bug.

## Route verdicts
| Route | Verdict | Reason |
|---|---|---|
| R1 Hartley | wounded (agree) | Additivity was cut (`MINIMAL_AXIOMS:148-151`); exclusion supports do not multiply across regions. |
| R2 Edwards | dead (agree; reason incomplete) | The landed reason: the realized-state primitive supplies no measure (`ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md:55-70`). The indifference reading of "A law privileges no states" (`MINIMAL_AXIOMS:94`) was not considered; it fails because the distribution "varies with" conditions. |
| R3 misframed | survives; "equivalent" overclaimed | Fits T2. Holds only if BH entropy is a record-ensemble functional, the attack's own hidden premise, tested only by a suggested typing. |

## Errors found
1. **Plain verdict overclaims.** "Choosing among the five cannot fix an area law; the measure does" was tested only for candidates (b), (c). Entanglement (d) gets its area-type law from Widom and Wald (e) is A*c by construction, independent of the record measure. They wait on other gates (`:180`, `:187`). "Two gates" holds for record-ensemble S only.
2. **"Class changes: log, surface, volume."** The log and surface laws are the two the attacker concedes are not translation covariant. Both are near-trivial: 8L^2 seeds cap S at ln 8L^2. The ring's S = P/4 is `solve_w` fitted to that target, with two roots (0.385, and above 1 for P>=12; `ringcheck.py`): a dial, and a restatement of the landed p* Schmidt-tuning no-go. For local covariant sequential laws the class stayed volume: 1D, L=10-22, w=0.01 to 100, dS1/dL from 0.067 to 0.28 against flat 0.281 (`oneD_w.py`).
3. **"0.29-0.97 of S0 at L=5" is not a coefficient.** It is an odd-L artifact: at L=6 the range is 0.48-0.97 (`w6_*.out`); for w=0.1, S1/S0 over L=3-6 is 0.19, 0.56, 0.29, 0.48. The 2D spread is real; no asymptotic 2D coefficient is shown. The 1D slopes are the robust evidence.
4. **Pre-registration.** The 0.95 threshold is arbitrary. In 1D, S1/S0 = 0.954 passes the canon threshold while KL grows linearly in L, so the readings do not separate there.
5. **Prior art.** "No note defines a record entropy" is too strong: `FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_..._2026-06-15.md` uses a 2-sector record entropy (pre-reset, not BH).
6. **Price naming.** DEFERRED_DECISIONS section 1 is odds for record content, not site, order or rate. With T2 the price is predecessor structure (T01), kernels (parked bridge) and partition.

## Corrected plain-language verdict
For entropies built from the record ensemble, T73 is priced at two open gates: a formation law (predecessor structure and odds) and a rule for what counts as "the same". On one set of allowed frozen boxes, local covariant formation laws all give volume-growing entropy with a law-dependent coefficient (1D checked, 2D toy); a surface or log law appears only if formation may be non-covariant. Entanglement and Wald entropies need other gates, so the measure alone does not settle the choice among the five.
