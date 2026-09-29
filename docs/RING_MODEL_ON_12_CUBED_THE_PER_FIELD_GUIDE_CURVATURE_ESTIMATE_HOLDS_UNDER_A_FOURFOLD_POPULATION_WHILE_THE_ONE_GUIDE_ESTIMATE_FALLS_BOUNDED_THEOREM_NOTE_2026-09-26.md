---
claim_id: ring_model_on_12_cubed_the_per_field_guide_curvature_estimate_holds_under_a_fourfold_population_while_the_one_guide_estimate_falls_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_12_cubed_curvature_population_series_in_both_guide_schemes_2026_09_26.py
---

# On 12³ the per-field-guide curvature estimate holds under a fourfold population while the one-guide estimate falls

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
[RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md).
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15`. The landed notes, including
[RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md),
use a guide field per probe field (`0.5 h`).

Open PR 9328 found that one guide field shared by the three probe fields
(`0.5 H₁`) gives a different estimate. Open PR 9352 showed that this scheme
difference grows with the torus at 960 walkers (−0.058, −0.183 and −0.268 on
8³, 12³ and 16³). On 8³ a population-free reptation estimate, 1.04–1.09,
agrees with both schemes. This block doubles and quadruples the walker
population on 12³ to see which scheme moves.

## Result

**12³ at `k = π/6`.** Projection 30, resampling interval 0.015, seeds 401 and
402; the 960-walker values are from open PR 9352.

| walkers | a guide per field | one guide for the three fields | difference |
|---|---|---|---|
| 960 | `1.0690 ± 0.0257` | `1.2520 ± 0.0221` | `−0.183 ± 0.034` |
| 1920 | `1.0721 ± 0.0176` (`u = 0.28798`) | `1.2159 ± 0.0304` (`u = 0.28733`) | `−0.144 ± 0.035` |
| 3840 | `1.0573 ± 0.0129` (`u = 0.28807`) | `1.1924 ± 0.0220` (`u = 0.28763`) | `−0.135 ± 0.026` |
| fit `a + b/N_w` | `a = 1.0551 ± 0.0189`, `b = 18 ± 36` | `a = 1.1737 ± 0.0282`, `b = 76 ± 39` | `−0.119 ± 0.034` (3.5σ) |

What follows:
- **The per-field scheme holds.** Its estimate stays at 1.06–1.07 over a
  fourfold population, with a slope consistent with zero, and its energy
  per plaquette moves by `0.0001`.
- **The one-guide scheme moves.** Its estimate falls by `0.06` and its energy
  per plaquette rises by `0.0003` toward the per-field value.
- **The extrapolation does not close the gap.** The one-guide intercept
  still lies 3.5 standard errors above the per-field value, so a linear
  `1/N_w` extrapolation over this range does not close the difference between these fitted intercepts; it does
  not identify either scheme's bias against an independently controlled value.
- **Reading.** With the 8³ reptation agreement (open PR 9352), this supports
  the per-field values that the landed notes use as estimates stable within rough errors over the tested populations on these tori. It does not provide a population-free value on
  12³.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin error,
  over two seeds per point, so they are rough.
- **Fit model.** The `1/N_w` form is an assumption. With three points and
  two parameters, its `χ²` (0.26 and 0.01 on one degree of freedom) does
  not test it strongly.
- **Seeds.** The 960-walker values come from a different run with the same
  seeds and settings.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 12³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guides and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block qualifies which guide scheme's estimate is stable within rough errors over the tested populations on 12³.
- **N5:** finite estimates at three populations; the population dependence is the result.
- **N6:** a population-free value on 12³ and larger tori remains open.
- **N7:** other guides, populations and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_12_cubed_curvature_population_series_in_both_guide_schemes_2026_09_26.py
```

Four checks; prints `TOTAL: PASS=4 FAIL=0` in about two and a quarter hours of computation.

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

- [PR 9328 finite source](RING_MODEL_ENERGY_CURVATURE_ESTIMATES_DEPEND_ON_THE_GUIDE_SCHEME_BY_ABOUT_A_QUARTER_ON_16_AND_24_CUBED_BOUNDED_THEOREM_NOTE_2026-09-26.md).
- [PR 9352 finite source](RING_MODEL_THE_GUIDE_SCHEME_SPLIT_OF_THE_CURVATURE_ESTIMATE_GROWS_WITH_THE_TORUS_AND_ON_8_CUBED_IS_ABOUT_0_05_WITH_OR_WITHOUT_A_WALKER_POPULATION_BOUNDED_THEOREM_NOTE_2026-09-26.md).

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
