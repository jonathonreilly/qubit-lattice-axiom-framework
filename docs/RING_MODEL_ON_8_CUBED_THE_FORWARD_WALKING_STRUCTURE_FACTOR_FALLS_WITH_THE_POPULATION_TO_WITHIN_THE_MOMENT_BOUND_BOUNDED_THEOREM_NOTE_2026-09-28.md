---
claim_id: ring_model_on_8_cubed_the_forward_walking_structure_factor_falls_with_the_population_to_within_the_moment_bound_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied finite ring component with the landed cyclic transverse modes and conditional moment identities (m1 = 2 u s^2, chi = 2 m_-1, S = m0, omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0, so S <= s sqrt(u chi)). Forward-walking (pure) S from the fixed-population projector (guide exp(0.2 N_flip), resampling interval 0.015, projection 60, second-half averages) at projection lags up to 8, with the fraction of distinct ancestors at each lag. Exact 2^3 control at k = pi: lags 1, 2, 4 within 0.3 standard errors of the exact 1.01215. On 8^3 at k = pi/4, S at lag 4 falls with the population: 0.564 at 120 walkers (landed), 0.445 at 960, 0.403 at 3840, 0.415 and 0.413 at 7680 (two seeds); at 7680 walkers S is flat over lags 2 to 8 at 0.408 +- 0.014, with about two percent distinct ancestors at lag 2. This lies within the moment ceiling s sqrt(u chi) = 0.424 from the landed chi = 1.064 +- 0.008; the ratio is 0.963 +- 0.034, and the three weighted mean frequencies m0/m_-1, sqrt(m1/m_-1), m1/m0 are 1.003 s, 1.042 s, 1.082 s. So the landed 120-walker values that exceeded the bound on 8^3 are a population effect of the forward-walking estimator. On 16^3 at k = pi/8, at 960 and 3840 walkers fewer than one percent of the ancestors at lag 1 are distinct, so the forward-walking average there does not estimate the pure S, and the landed 120-walker 16^3 value is of this kind. No certified structure factor, frequency, single-mode statement, population convergence, limit or physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_forward_walking_structure_factor_population_series_2026_09_28.py
---

# On 8³ the forward-walking structure factor falls with the population to within the moment bound

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes `O_a` and conditional
moment identities of the landed ring-component note
`RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`:
- `m₁ = 2us²`, `χ = 2m₋₁` and `S = m₀`;
- `ω_min ≤ m₀/m₋₁ ≤ √(m₁/m₋₁) ≤ m₁/m₀`, hence `S ≤ s√(uχ)`.

**The tension this block addresses.** That note compared its energy-only
bound with forward-walking values of `S` from 120-walker runs, including those
of the landed note
`RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md`.
Those values lay above the bound on 8³ and larger tori, by up to ten
standard errors on 16³. The bound is a Cauchy–Schwarz inequality, so either
the forward-walking values or the susceptibility estimates were off.

**The estimator.** The pure `S` is estimated by forward walking in the
fixed-population projector:
- guide `exp(0.2 N_flip)`, resampling interval `0.015`, projection to 60,
  averages over the second half;
- each walker's `|O_a|²` is weighted by its descendants' weight a lag later,
  for lags up to 8 in projection time;
- the runner reports the fraction of distinct ancestors at each lag, which
  measures how many lineages carry the average.

## Result

1. **Exact 2³ control at `k = π`.** Four independent 400-walker runs give
   `S = 1.0115`, `1.0128` and `1.0099` at lags 1, 2 and 4, against the exact
   `1.01215`, all within 0.3 standard errors.
2. **8³ at `k = π/4`: S falls with the population.**

   | walkers | lag 0 (mixed) | lag 1 | lag 2 | lag 4 | lag 8 | distinct at lag 2 |
   |---|---|---|---|---|---|---|
   | 120 (landed) | | `0.572` | `0.575` | `0.564` | | |
   | 960 | `0.574` | `0.476` | `0.468` | `0.445` | `0.430` | `0.026` |
   | 3840 | `0.565` | `0.448` | `0.428` | `0.403` | `0.353` | `0.022` |
   | 7680 (seed 3) | `0.556` | `0.427` | `0.402` | `0.415` | `0.395` | `0.021` |
   | 7680 (seed 4) | `0.564` | `0.440` | `0.413` | `0.413` | `0.410` | `0.022` |

   - The landed 120-walker values sit at the level of the mixed estimate.
   - At 7680 walkers `S` is flat over lags 2 to 8, at `0.4058` and `0.4110`
     for the two seeds, combined **`S = 0.408 ± 0.014`**.
3. **Within the moment bound.** With the landed `χ = 1.064 ± 0.008` (8³,
   `k = π/4`, eight runs) and `u = 0.2888`:
   - the ceiling is `s√(uχ) = 0.424`, and the ratio is
     `S/ceiling = 0.963 ± 0.034`;
   - the three weighted mean frequencies are `m₀/m₋₁ = 0.768 = 1.003 s`,
     `√(m₁/m₋₁) = 0.798 = 1.042 s` and `m₁/m₀ = 0.829 = 1.082 s`, with
     `s = 2 sin(π/8)`.
4. **16³ at `k = π/8`: the lineages collapse.** At 960 and 3840 walkers the
   fraction of distinct ancestors is `0.005` and `0.002` at lag 1, and
   `0.001` or less beyond. The average is then carried by a handful of
   lineages. The values (0.43 to 0.63, with errors near 0.05 to 0.09) do not
   estimate the pure `S`. The landed 120-walker 16³ value `0.591` is of this
   kind.

## What follows

- **The 8³ tension is a population effect.** The forward-walking values that
  exceeded the moment bound on 8³ fall with the population. At 7680
  walkers they lie within the bound, so the energy-curvature susceptibility
  and the moment identities are consistent there.
- **The weight sits near one frequency on 8³.** The ratio `0.963 ± 0.034` is
  one within errors, and the three weighted mean frequencies differ by
  less than 8 percent. Read with the landed identities, this is an estimated
  statement: at `k = π/4` on 8³ the transverse spectral weight is
  concentrated near `ω ≈ s`, and `m₀/m₋₁` gives the estimated bound
  `ω_min ≲ 0.77`. A second mode carrying a small weight is not excluded.
- **Larger tori need another pure estimator.** On 16³ forward walking fails
  by lineage collapse at these populations. The landed large-torus values
  above the bound carry no information about the pure `S`.

## Estimator and reproduction boundary

- **Errors.** Bin errors over ten blocks. The lags share walkers, so the
  plateau error is the mean single-lag error, not reduced by the number of
  lags. The two 7680-walker seeds are combined with the larger of their
  mean error over `√2` and half their difference.
- **Population convergence.** Not shown. `S` falls from 960 to 3840 walkers
  and is stable from 3840 to 7680 at lags 2 to 4. At lag 8 with 3840
  walkers the lineages thin (0.001) and the value drops to 0.353.
- **Susceptibility.** The landed `χ` is used as stated there.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³, 8³ and 16³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' identities and susceptibility are used as stated there; this block revisits their forward-walking comparison.
- **N5:** finite estimates; the population series and the distinct-ancestor fractions are the result.
- **N6:** a pure `S` on 16³ and larger tori remains open.
- **N7:** other guides, populations, lags and pure estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_forward_walking_structure_factor_population_series_2026_09_28.py
```

Four checks; prints `TOTAL: PASS=4 FAIL=0` in about fifty minutes of computation.
