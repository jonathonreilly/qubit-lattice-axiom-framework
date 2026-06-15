# The d=2 Sign Boundary Tracks the Landau–Peierls Curvature-Determinant Sign Change Within 2×10⁻² at Every Sampled Temperature (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the landmark boundary-comparison datum; the collapse note is in review — its needed anchor recomputed here, not cited as graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_lp_boundary_identification_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_lp_boundary_identification_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=21 FAIL=0`.

## Findings

Two independently-bisected boundaries at `m = 0`, `T ∈ {0.2, 0.3, 0.4}`:

- the **full finite-field boundary** `ε*(T)` (Harper `χ(q=24)`, converged quadrature,
  bracket-gated), and
- the **Landau–Peierls candidate** `μ_LP(T)`: the sign change of
  `−∫d²k f′(ε−μ)·[ε_xx ε_yy − ε_xy²]` — for the square lattice exactly
  `−∫d²k f′ · 4t² cos kx cos ky` (quadrature-doubling gated; the far-below-band
  limit control verified).

**They agree within `2×10⁻²` at every sampled `T` (gated)**: the sign boundary of
the exact finite-field matter flux response **tracks the Landau–Peierls curvature-
determinant sign change** at these sampled temperatures (`B = 2π/24` — the full
boundary is a finite-field object, the LP is `B → 0`; the finite-`B` agreement within
the stated tolerance is the bounded datum).

## Scope

`m = 0` square lattice, sampled `T`, finite `B` disclosed; agreement with the
Landau–Peierls sign-change root at the stated tolerance is the datum. No new
axiom/primitive/measure/weight; `r` untouched.
The audit lane grades.
