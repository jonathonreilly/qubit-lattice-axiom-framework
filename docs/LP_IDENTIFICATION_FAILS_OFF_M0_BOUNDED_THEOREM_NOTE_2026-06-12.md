# The Landau–Peierls Identification Does Not Extend Off m = 0: Measured Deviations 0.042 → 0.20 (m = 0.5) Between the Full-Field Boundary and the Staggered LP Sign Change — the Identification Is an m = 0 Statement (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_lp_identification_fails_off_m0_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_lp_identification_fails_off_m0_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=44 FAIL=0` — anchor reproduced (`μ*(0.2, 0.2)`); the staggered LP kernel derived symbolically with its `m → 0` reduction control (`10⁻¹⁰`).

## Findings

With the two-band staggered LP kernel (`det Hess(E±)` via the chain rule through
`√(m² + ε²)`, closed form, controls gated), the full-field boundary and the LP sign
change **separate as `m` grows**: deviations `0.042` (`m = 0.2, T = 0.2`), `0.046`
(`m = 0.2, T = 0.4`), `0.201` (`m = 0.5, T = 0.2`) — all far beyond the `2×10⁻²`
identification tolerance that held at `m = 0` (deviation values gated as frozen
regression constants, labeled; the claim is the measured table). **The intraband-LP identification is an `m = 0` statement**: at finite staggered
mass the exact finite-`B` response departs from the **intraband band-curvature-
determinant form tested here** (the kernel's chain-rule mass term is included and
panel-verified; what is NOT tested is a corrected two-band orbital formula with
interband/geometric contributions, nor the strict `B → 0` limit — both named
follow-ons). The closed-form boundary-surface candidate is therefore
**not** LP-complete (the motivation from the collapse note is correspondingly
bounded); the corrected two-band analytic candidate (interband/geometric terms) is the named follow-on.

## Scope

Staggered `d = 2`, sampled `(m, T)`, finite `B = 2π/24` vs `B → 0` LP caveat stated;
the deviation table is the datum. No new axiom/primitive/measure/weight; `r`
untouched. The audit lane grades.
