# Refuting pass — block 14 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block14_rate_laws.py`, refuting pass `specs/supervisor_control_block14_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the plaquette laws under four rate laws (R2, R4) | a history dynamic program over (order, values) | per-order closed forms — path orders `(1/6) Π K / K_2(closed diagonal)`, diagonal-first orders `(1/36) Π K / K_2²` — with the order probabilities read off the rate functions causally | equal on all 1296 patterns for all four laws |
| the uniform distance on `2×3` (R2) | mixture by multiset classes | the census runner's own pinned cache on `main` (a different implementation; it prints `0.029104037152`) | agrees with the exact rational's decimal expansion |
| the plaquette types (R4) | a stored table of corner diagonals | the sign of the dot product with the vector to the opposite corner computed from coordinates | equal on all `6⁴` patterns |
| the tree theorem (R3) | total variation of the seeded law to the static law | structural: every seeded-charged order on the path and the star gives every site after the first exactly one recorded neighbour | holds for every charged order |
| the general identity (R4, E2) | symbolic identities in `(p_in, p_out, p, q, r)` | direct evaluation at 200 random rational points, including the sign | equal; strictly positive unless `p = q` (resp. `p = q = r`) |

Findings:
- **F1 (fixed).** The runner's first symbolic positivity test for E2 expanded the cofactor of `(d_anti − d_same)` in the variable `1 − p` and saw negative coefficients; the proof's own form — the cofactor is a convex combination of `1/6` and `(d_anti + d_same)/36` — is what the runner now checks, together with the two gap identities `d_anti − d_same = Z_1²(p−q)²/(K_2^{anti} K_2^{same})` and `d_orth − d_same = Z_1²((p−r)² + (q−r)²)/(K_2^{orth} K_2^{same})`.
- **F2 (noted).** The census runner prints the uniform distance as a decimal; the exact rational is in the census note's text (checked by A3). The refuting pass compares the decimal.

Attempts to refute (nothing refuted): the plaquette argument was re-read for a rate law that depends on the *window* (the rate is a lattice function; the window only sets which sites can form, so the 90° and 180° rotations used are symmetries of the process); for a rate law whose diagonal candidate's rate depends on the *adjacent* candidates' geometry (it enters only through the sum `λ_a + λ_b`, which is invariant under the diagonal-axis rotation); and for the claim that value-dependent decisions in the path class drop out (both diagonals carry the same `d` on the comparison patterns, so whichever diagonal is closed the weight is `(1/6) Π K d`). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
