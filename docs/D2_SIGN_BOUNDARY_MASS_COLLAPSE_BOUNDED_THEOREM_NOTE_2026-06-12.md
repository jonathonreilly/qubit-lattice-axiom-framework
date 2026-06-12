# The d=2 Sign Boundary Shows a Bounded Mass Collapse: μ*(m,T)² = m² + ε*(T)² Within 2% Across the Sampled Masses, With a Small Systematic Monotone m-Trend Disclosed (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (the landmark follow-on of the sign-boundary note, in review — cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_d2_sign_boundary_mass_collapse_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_d2_sign_boundary_mass_collapse_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=92 FAIL=0` — GL quadrature raised to 160/224 after the 96-point pair proved unconverged for `χ` differences (the repair is part of the record: the first-pass "non-collapse" verdict was quadrature error).

## Findings

Bisection-located boundaries at `T = 0.2` across `m ∈ {0.2, 0.35, 0.5, 0.8}` give
`ε*_m = √(μ*² − m²)` with **relative spread 1.45% < 2% (fixed gate)** — a bounded
collapse, **with a small systematic residual**: ε* decreases monotonically with `m`
(`1.697 → 1.690 → 1.681 → 1.657`, gated as the disclosed m-trend). To the stated
tolerance the staggered mass enters through `μ*² = m² + ε*(T)²`; the residual trend
is the named follow-on, not noise. The `m = 0` direct anchor
agrees (gated); `ε*(T)` increases with `T` (fixed-direction gate); per-iteration
bracket invariants, endpoint-sign recomputation, doubling (`10⁻⁶` absolute on `χ`),
and the `q = 32` spot probe all gated.

## Scope

Sampled instances; the collapse relation at the stated tolerance is the datum; the
`ε*(T)` curve's own interpretation (what the spinless boundary tracks) is the named
follow-on. No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
