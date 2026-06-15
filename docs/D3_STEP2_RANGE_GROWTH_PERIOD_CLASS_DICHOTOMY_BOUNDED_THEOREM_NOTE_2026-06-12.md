# d=3 Step 2 Grows the Range (Box-Disciplined: L=12/14 Converged Sub-1%, L=8 Disclosed as Box-Limited); Truncation Protection Is a Period-Class Dichotomy — Holds at L ≡ 0 mod 4, Fails at L ≡ 2 mod 4 (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the d=3 step-2 follow-on; cross-refs in-review, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_d3_step2_range_growth_period_class_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_d3_step2_range_growth_period_class_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=21 FAIL=0`.

## Findings

The second checkerboard's eliminated block carries internal couplings (closure ends at
step 1, as in `d = 2` — gated); the exact step-2 shell tables grow beyond the step-1
family with band-wise magnitude decay (fixed gates), **with the box discipline built
in from the start**: near shells converge on the `L = 12` vs `14` pair at `0.3%`
(gated `≤ 2%`), while the `L = 8` table deviates `8%` — box-limited and disclosed (the
`d = 2` lesson applied prospectively). The synthetic chart reassignment is stated.
**The truncation protection at step 2 is a period-class dichotomy, both branches
gated**: the next-checkerboard `H_kd` is nonzero before even-`d²` truncation (anti-
fabrication gate), and after truncation it vanishes at `10⁻¹⁴` for `L ≡ 0 mod 4`
(`L = 8, 12`) but **fails** for `L ≡ 2 mod 4` (`L = 10: 0.748`, `L = 14: 0.747`,
gated `> 0.5`) — there the second chart's `K`-periods `(L/2, L, L/2)` have odd
components, so minimal-vector `d²` parity no longer matches chart parity. The parity
lemma's protection is **commensuration-conditional**, not generic.

## Scope

Free, `E = 0`; range behavior + the period-class dichotomy are the data; no flow claims.
No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
