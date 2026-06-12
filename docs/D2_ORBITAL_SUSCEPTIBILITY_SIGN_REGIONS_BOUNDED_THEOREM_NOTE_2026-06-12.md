# The d=2 Orbital Flux-Response Curvature Has Sampled-Grid-Resolved Signs: Ω″-Negative Across μ_ch ∈ [0, 1.5], Ω″-Positive at the μ_ch = 2.0 Sample — the First Sign Datum the 1D Program Provably Could Not Supply (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the d≥2 follow-on of the 1D vanishing-identity note; cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_d2_orbital_susceptibility_sign_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_d2_orbital_susceptibility_sign_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=35 FAIL=0` — exact Harper/Bloch spectra + Gauss–Legendre quadrature (doubling-gated at the measured `3×10⁻⁹` floor set by `T = 0.2` Fermi sharpness).

## Findings

- **Handle-flux corollary**: the torus-cycle flux density vanishes with `L` (the same
  per-cycle integration-by-parts identity as 1D — the cycle object carries no bulk sign
  in any `d`; gated).
- **The plaquette-field response is the sign-bearing object**: uniform `B = 2π/q`
  (Landau gauge, even-`q` magnetic cells compatible with the staggered mass),
  `χ(q) = 2[Ω(B_q) − Ω(0)]/B_q²` with `q ∈ {16, 24, 32}` Richardson-gated.
- **The sign table, region-resolved and gated with margins**: **diamagnetic
  (`χ < 0`) across the sampled band interior** (`μ_ch ∈ [0, 1.5]`, both masses, both
  temperatures) and **paramagnetic (`χ > 0`) at the sampled band-edge region**
  (`μ_ch = 2.0`) — the matter loop's orbital sign exists in `d = 2` and is
  doping-region-structured, exactly as the 1D identity demanded it must be sought here.
- Controls: `B = 0` consistency (`10⁻¹²`), Landau-gauge-origin invariance (`10⁻¹⁰`),
  `T = 50` kills the response.

## Scope

Free staggered square lattice, exact spectra, sampled `(μ_ch, m, T)` grid and
`B → 0` through rational fluxes — finite-grid statements; no continuum-QFT claim; the
β-formula import unused; the gauge self-energy remains the named gap. No new
axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
