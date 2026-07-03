# The d=2 Sign Boundary Shows a Bounded Mass Collapse: μ*(m,T)² = m² + ε*(T)² Within 2% Across the Sampled Masses, With a Small Systematic Monotone m-Trend Disclosed (Bounded)

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. This note does not
set or predict an audit outcome.
**Primary runner:** [scripts/frontier_d2_sign_boundary_mass_collapse_2026_06_12.py](../scripts/frontier_d2_sign_boundary_mass_collapse_2026_06_12.py)
**Runner cache:** [logs/runner-cache/frontier_d2_sign_boundary_mass_collapse_2026_06_12.txt](../logs/runner-cache/frontier_d2_sign_boundary_mass_collapse_2026_06_12.txt)
(SCORECARD: PASS=92, FAIL=0)

GL quadrature was raised to 160/224 after the 96-point pair proved unconverged
for `χ` differences. The first-pass "non-collapse" verdict is therefore treated
as a quadrature-error repair record, not as physics evidence.

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

## Dependencies

- [D2_ORBITAL_SUSCEPTIBILITY_SIGN_REGIONS_BOUNDED_THEOREM_NOTE_2026-06-12.md](D2_ORBITAL_SUSCEPTIBILITY_SIGN_REGIONS_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the sampled sign-bearing plaquette-field response surface.
- [D2_SIGN_BOUNDARY_BISECTION_BETWEEN_LANDMARKS_BOUNDED_THEOREM_NOTE_2026-06-12.md](D2_SIGN_BOUNDARY_BISECTION_BETWEEN_LANDMARKS_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the bisection-located sign-boundary setup this note mass-varies.
