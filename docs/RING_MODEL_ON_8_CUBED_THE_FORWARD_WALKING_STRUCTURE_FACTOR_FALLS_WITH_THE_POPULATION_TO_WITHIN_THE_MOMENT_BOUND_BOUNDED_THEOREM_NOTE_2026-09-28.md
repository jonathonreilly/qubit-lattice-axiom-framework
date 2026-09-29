---
claim_id: ring_model_on_8_cubed_the_forward_walking_structure_factor_falls_with_the_population_to_within_the_moment_bound_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_forward_walking_structure_factor_population_series_2026_09_28.py
---

# Recorded 8³ forward-walking diagnostics: structure-factor means decrease over the tested populations

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes `O_a` and conditional
moment identities of the landed ring-component note
[RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md):
- `m₁ = 2us²`, `χ = 2m₋₁` and `S = m₀`;
- `ω_min ≤ m₀/m₋₁ ≤ √(m₁/m₋₁) ≤ m₁/m₀`, hence `S ≤ s√(uχ)`.

**The tension this block addresses.** That note compared its energy-only
bound with forward-walking values of `S` from 120-walker runs, including those
of the landed note
[RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md).
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
   establish a controlled estimate of the pure `S`. The landed 120-walker 16³ value `0.591` is of this
   kind.

## What follows

- **The finite 8³ discrepancy decreases at the tested populations.** The forward-walking values that
  exceeded the moment bound on 8³ fall with the population. At 7680
  walkers they lie within the bound, so the energy-curvature susceptibility
  and the moment identities are consistent there.
- **The plug-in moment means are close on 8³.** The ratio `0.963 ± 0.034` is
  one within errors, and the three weighted mean frequencies differ by
  less than 8 percent. Read with the landed identities, these noisy plug-in values neither reconstruct the spectral density nor
  prove concentration. Conditionally, `m₀/m₋₁` gives the estimated bound
  `ω_min ≲ 0.77`. A second mode carrying a small weight is not excluded.
- **Larger tori need another pure estimator.** On 16³ the forward-walking coverage is poor
  at these populations, with few surviving lineages. The large-torus values above the bound do not supply controlled pure-state
  estimates. Few surviving ancestors diagnose poor coverage but alone do not
  prove every value is biased or quantify its error.

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

The cited 8³ susceptibility pools four 480-walker and four 1920-walker
runs, with its energy taken from the lower population, as the current parent
explains. It is not eight identical-setting repetitions or a population-free
value. Near-equality of noisy moment estimates does not certify single-mode
saturation or reconstruct the spectral measure.

## Review boundary and evidence provenance

These are recorded finite-run diagnostics of supplied models. The full original
runner and its content-pinned successful output are retained; the long simulations
were not repeated during this landing review. Independent controls check the
rate algebra, normalization, reduction formulas and printed comparisons. Original
console labels and introductory runner prose are historical descriptions; this
note's corrected scope governs their interpretation.

Seed/bin errors and printed sigma ratios are descriptive, not calibrated coverage
or hypothesis tests. Shared fields, seeds, initialized populations and time
windows can induce covariance; unpaired quadrature errors do not estimate that
covariance. Matching two guides, populations, intervals or windows does not prove
convergence or absence of common bias. Cross-size energy differences cannot by
themselves isolate population error. Removing walker populations from reptation
does not remove finite-path, equilibration or component uncertainty.

The parent's energy-response symmetries, selected-component condition and centered
positive spectral measure remain necessary. The three-field curvature removes
the quartic term under an even response assumption but has residual field error.
Numerical plug-ins in exact moment inequalities are not certified excitation
frequencies, gaps, structure factors, phase or physical-particle statements.

## Compared source measurements


[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

- [PR9352 finite reptation comparison](RING_MODEL_THE_GUIDE_SCHEME_SPLIT_OF_THE_CURVATURE_ESTIMATE_GROWS_WITH_THE_TORUS_AND_ON_8_CUBED_IS_ABOUT_0_05_WITH_OR_WITHOUT_A_WALKER_POPULATION_BOUNDED_THEOREM_NOTE_2026-09-26.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
