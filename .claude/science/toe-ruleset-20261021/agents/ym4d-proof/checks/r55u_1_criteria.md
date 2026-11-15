# checks/r55u_1_criteria.md — Opus 5.5 reviewer (REVIEW55_TUNIF), written 2026-10-28T22:40:03Z UTC, BEFORE r55u_1_nl1ramp.py exists

## What is tested
NLOC.md Lemma NL-1's spread-axial construction ("torus spread-axial gauge"), implemented from its text (Steps 1-3 run
direction by direction on nested sub-tori {y_1 = ... = y_{r-1} = 0}, each round's gauge independent of the earlier
coordinates; Step 4 subtract the torus mean), applied to explicit fields B on (Z/R)^d. Purpose: decide whether the
mechanism NLOC [NL-corr 1] (Theorem NL-3') relies on can give a sup bound of the form C·|B|_inf with C independent of the
torus side R when the curvature line sums are NOT small. Exact rational arithmetic (fractions.Fraction), plain python.

## Inputs (fixed here)
- d = 2 and d = 3; R in {4, 8, 16} (d = 2 also R = 32).
- TEST field ("half-line staggered"): B_1(y) = (-1)^{y_2} if y_1 < R/2 else 0; all other components 0. |B|_inf = 1.
- CONTROL field ("full-line staggered"): B_1(y) = (-1)^{y_2} for all y_1; others 0. |B|_inf = 1. Its curvature is
  uniform along direction 1, so the spreading in Step 1 removes it exactly; the construction's output must stay bounded.

## Pre-registered verdicts
- r55u_1-A (exactness of the implementation): for every run, d(B - dλ) = dB exactly (λ the constructed gauge), and the
  output's torus mean equals the input's. PASS iff zero discrepancies. FAIL voids the check.
- r55u_1-B (the claim under test): S(R) := max|B - dλ - h^B| for the TEST field. **PASS (= NL-1's representative is
  NOT bounded by C|B|_inf uniformly in R) iff S(R) >= R/4 for every R in the list** (expected exactly R/2 at d = 2 by my
  hand derivation; the gate only asks for linear growth). FAIL iff S(R) < R/4 for some R.
- r55u_1-C (designed-FAIL control for B): S_ctrl(R) for the CONTROL field. The control FIRES (as designed) iff
  S_ctrl(R) <= 1 for every R (no growth). If it does not fire, r55u_1-B is evidence-free.
- r55u_1-D (consistency with Lemma NL-1's own bound, reporting only): print S(R) / (4·d·R·|dB|_inf); must be <= 1.
