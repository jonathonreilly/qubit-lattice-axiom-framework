# The 1D Orbital Susceptibility Density Vanishes Identically — an Integration-by-Parts Identity, Confirmed Numerically at 10⁻¹⁶ Across the Entire Grid: the Finite-Ring Sign Structure Is Pure Finite-Size Effect, and the Screening Sign Needs d ≥ 2 (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (the named thermodynamic-extrapolation follow-on of the doped flux-response note, in review — cross-referenced, not cited as graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_susceptibility_density_identity_zero_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_susceptibility_density_identity_zero_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=22 FAIL=0`.

## The identity

The flux enters as `k → k + φ/N`, so `∂φ = (1/N)∂k` and the **total** response scales as
`Ω″(0) = (1/N²)Σₖ[…]`; the density object is `χ(N) = N·Ω″(0) → χ_∞ =
(1/2π)∮dk [f(E)·E″ + f′(E)·(E′)²]` (per band, both bands summed — the scaling stated, the
object declared). This `χ_∞` **vanishes identically for any periodic band at any filling
and temperature**: integrating the first term by parts over the closed Brillouin zone gives
`∮f·E″ = −∮f′·(E′)²` exactly (the boundary term cancels by periodicity; the `f′` sign and
both bands verified in-derivation). The runner confirms: every entry of the full grid (`μ_ch × m × T`, 63 entries)
is zero at `≤ 2.6×10⁻¹⁶` (quadrature cross-validated at `10⁻¹⁰` — a sanity check, not load-bearing; the identity is
analytic), and the finite-`N` sequences `N·Ω″(0)` converge to zero through `N = 40` on both
parity classes (likewise sanity).

## What this settles

The entire finite-ring sign structure — parity-resolved, alternating after averaging,
commensuration-structured under doping (the three in-review predecessors: the filling-resolved, parity-averaged, and doped notes — cross-references, not graded citations) — is **pure
finite-size/boundary effect with no bulk density counterpart in one dimension**. The matter
screening-sign question **cannot be posed on 1D ring densities at all**: orbital response
requires loops, i.e. `d ≥ 2` — converging exactly on the `d = 2` lane opened by the
checkerboard-decimation note. The β-formula import is used nowhere.

## Scope

Strict 1D staggered bands, exact; the identity is analytic (IBP) and the numerics confirm
at machine scale. Not claimed: `d ≥ 2` response values, `b₃`, the gauge self-energy (named
gap). No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
