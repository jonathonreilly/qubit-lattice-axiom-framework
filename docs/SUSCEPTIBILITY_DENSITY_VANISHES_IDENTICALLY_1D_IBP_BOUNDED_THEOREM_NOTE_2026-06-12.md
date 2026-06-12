# The 1D Orbital Susceptibility Density Vanishes Identically — an Integration-by-Parts Identity, Confirmed Numerically at 10⁻¹⁶ Across the Entire Grid: the Finite-Ring Sign Structure Is Pure Finite-Size Effect, and the Screening Sign Needs d ≥ 2 (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_susceptibility_density_identity_zero_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_susceptibility_density_identity_zero_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=23 FAIL=0`.

## The identity

The flux enters as `k → k + φ/N`, so `∂φ = (1/N)∂k` and the **total** response scales as
`Ω″(0) = (1/N²)Σₖ[…]`; the density object is `χ(N) = N·Ω″(0) → χ_∞ =
(1/2π)∮dk [f(E)·E″ + f′(E)·(E′)²]` (per band, both bands summed — the scaling stated, the
object declared). This `χ_∞` **vanishes identically for any smooth periodic band with a
smooth occupation function** (in particular, positive-temperature Fermi weights): integrating
the first term by parts over the closed Brillouin zone gives
`∮f·E″ = −∮f′·(E′)²` exactly (the boundary term cancels by periodicity; the `f′` sign and
both bands verified in-derivation). The runner symbolically verifies the total-derivative
identity; it also confirms every entry of the full grid (`μ_ch × m × T`, 63 entries) is
zero at `≤ 2.6×10⁻¹⁶` (quadrature cross-validated at `10⁻¹⁰` — a sanity check), and the
finite-`N` sequences `N·Ω″(0)` converge to zero through `N = 40` on both parity classes
(likewise sanity).

## What this settles

The entire finite-ring sign structure — parity-resolved, alternating after averaging,
commensuration-structured under doping (the filling-resolved, parity-averaged, and doped
finite-ring predecessors are context only, not graded citations) — has **no 1D bulk-density
counterpart under this smooth periodic-band density limit**. The matter screening-sign question
is not decided by 1D ring densities: a nontrivial orbital loop response needs `d ≥ 2`, matching
the `d = 2` lane opened by the checkerboard-decimation note. The β-formula import is used nowhere.

## No-Go Discipline Gate

This is a 1D smooth-periodic-density identity, not a broad orbital-response no-go.

- **N1 alternatives.** Finite-ring sign survival, boundary-term leakage, non-smooth
  occupation, open/nonperiodic bands, and higher-dimensional loop response are separate
  routes; only the smooth periodic 1D density route is closed here.
- **N2 wall independence.** Periodicity, smooth occupation, density scaling, flux-as-shift,
  and one-dimensionality are independent scope walls.
- **N3 hidden-wall scan.** "Any band" means smooth periodic one-dimensional band; finite
  rings, open boundaries, zero-temperature singular occupations, and `d >= 2` loops are
  outside the proof.
- **N4 residual matching.** The residual closed here is exactly the 1D bulk density
  counterpart of the finite-ring signs, not finite-size response and not higher-dimensional
  screening.
- **N5 rhetoric audit.** "Pure finite-size/boundary effect" means no smooth 1D
  thermodynamic-density counterpart; it does not say finite rings have no response.
- **N6 partial closure.** The `d = 2` lane remains the legitimate route for a nonzero bulk
  orbital response.
- **N7 steelman.** A sharp reviewer can still use nonsmooth occupations, boundaries,
  disorder, interactions, or higher-dimensional loops; none are closed by this identity.
- **N8 echo.** This preserves the recent finite-ring sign packets as finite data while
  preventing them from being promoted to a 1D bulk screening sign.

Gate outcome: PASS for the stated smooth periodic 1D density identity only.

## Scope

Strict 1D staggered bands and, more generally, smooth periodic 1D bands with smooth
occupations; exact IBP identity, with numerics as machine-scale confirmation. Not claimed:
finite-ring sign erasure, zero-temperature singular occupations, open/nonperiodic bands,
`d ≥ 2` response values, `b₃`, or the gauge self-energy (named gap). No new
axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
