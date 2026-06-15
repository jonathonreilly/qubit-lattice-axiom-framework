# The d=2 Orbital Sign-Change Boundary Located by Bisection (μ* to 10⁻³, q-Size-Checked): It Lies Strictly Between the Van Hove Energy and the Band Edge, Anchored to Neither (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (sign-boundary follow-on of the d=2 orbital sign note; cross-referenced source proposal, not graded here)
**Claim type:** bounded_theorem
**Related source:** [D2_ORBITAL_SUSCEPTIBILITY_SIGN_REGIONS_BOUNDED_THEOREM_NOTE_2026-06-12.md](D2_ORBITAL_SUSCEPTIBILITY_SIGN_REGIONS_BOUNDED_THEOREM_NOTE_2026-06-12.md)
**Script:** [scripts/frontier_d2_sign_boundary_bisection_2026_06_12.py](../scripts/frontier_d2_sign_boundary_bisection_2026_06_12.py)
**Cache:** [logs/runner-cache/frontier_d2_sign_boundary_bisection_2026_06_12.txt](../logs/runner-cache/frontier_d2_sign_boundary_bisection_2026_06_12.txt)
**Status:** source proposal; the audit lane grades. Runner `PASS=154 FAIL=0` — finite Harper-matrix computation, every bisection iteration's bracket invariants gated.

## Findings

The flux-response curvature's sign-change boundary located to `10⁻³`:

```
mu*(m=0.2, T=0.2, q=24) = 1.708008  chi=1.776554079231e-06  bracket_width=1.953125000000e-03
mu*(m=0.5, T=0.2, q=24) = 1.753466  chi=-1.864182924607e-06  bracket_width=1.230835896533e-03
mu*(m=0.2, T=0.4, q=24) = 1.794413  chi=-8.120573906920e-06  bracket_width=1.222329387663e-03
```

with the `q = 32` size probe agreeing within `0.14%`, quadrature doubling gated, and
the **fixed-direction gates**: μ* increases with `m` (at `T = 0.2`) and with `T` (at
`m = 0.2`) — observed orderings gated as fixed inequalities; `q = 32` agreement is
gated at 5% and observed at `0.14%` (output, not a gate claim). **The honest
anchor**: at every sampled instance μ* lies strictly **between** the analytic van Hove
energy `|m|` and the upper band edge `√(m²+16)` — anchored to **neither** (distance
comparisons are vacuous here; the landmark identification stays open, named).

## Scope

Sampled `(m, T)` instances, bisection-bracketed at fixed small `B = 2π/q`; no continuum
claim; the β-formula import unused. No new axiom/primitive/probability measure/record
weight; numerical quadrature weights are only integration weights. `r` untouched. The
audit lane grades.
