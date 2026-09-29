---
claim_id: ring_model_on_16_cubed_a_threefold_finer_resampling_interval_leaves_the_energy_and_the_curvature_estimate_unchanged_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_16_cubed_resampling_interval_test_2026_09_28.py
---

# Recorded 16³ resampling-interval diagnostics: small energy and curvature changes

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
[RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md).
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15` and a guide field per probe field (`0.5 h`), as in
[RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md).

**The open offset.** The 16³ energy per plaquette `u = 0.2868` lies `0.0018`
below the 8³ finite reptation estimate `0.2886` (open PR 9352). Several checks
leave the offset in place:
- a fourfold population moves it by `0.0004` (open PR 9358);
- a longer projection moves it by `0.00006` (open PR 9369; the same holds on
  24³ in open PR 9372).

**The test.** The projector resamples its fixed population every `0.015` of
projection time, and that interval enters the population-control error
independently of the walker count. This block cuts it to `0.005`, keeping the
projection window `[7.5, 30)`, the population (960 walkers) and the seeds
(401, 402) of open PR 9369.

## Result

**16³ at `k = π/8`, a guide per field, 960 walkers, window `[7.5, 30)`.**

| resampling interval | `χ` (seeds) | `u` (seeds) |
|---|---|---|
| `0.015` (open PR 9369) | `1.0043 ± 0.0381` (`0.9662`, `1.0425`) | `0.28676` |
| `0.005` | `1.0647 ± 0.0276` (`1.0583`, `1.0711`) | `0.28670` (`0.28675`, `0.28666`) |

What follows:
- **A small energy change is observed at these two intervals.** `u` moves by
  `−0.00006`. This comparison does not establish interval independence or explain the
  cross-torus offset from `0.2886`.
- **The curvature estimate is consistent.** The two values differ by
  `0.060`, which is 1.3 combined standard errors. The finer interval agrees
  with the standard-setting values `1.039 ± 0.022` (open PR 9298) and
  `1.061 ± 0.036` (open PR 9358), and with the 16³ late-window value
  `1.062 ± 0.028` (open PR 9369).

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin
  error, over two seeds.
- **Other settings.** Other intervals, populations and windows are not
  tested in combination.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 16³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block tests the resampling interval of their estimator on 16³.
- **N5:** finite estimates at two intervals.
- **N6:** the origin of the energy offset remains open.
- **N7:** other guides, populations, intervals and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_16_cubed_resampling_interval_test_2026_09_28.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about forty-five minutes of computation.

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

- [PR 9298 finite source](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_ON_THE_24_CUBED_TORUS_THE_TRANSVERSE_SUSCEPTIBILITY_AT_K_PI_OVER_12_STAYS_FINITE_WITH_A_SOFTENING_NOT_RESOLVED_BOUNDED_THEOREM_NOTE_2026-09-26.md).
- [PR 9352 finite source](RING_MODEL_THE_GUIDE_SCHEME_SPLIT_OF_THE_CURVATURE_ESTIMATE_GROWS_WITH_THE_TORUS_AND_ON_8_CUBED_IS_ABOUT_0_05_WITH_OR_WITHOUT_A_WALKER_POPULATION_BOUNDED_THEOREM_NOTE_2026-09-26.md).
- [PR 9358 finite source](RING_MODEL_ON_16_CUBED_THE_PER_FIELD_GUIDE_CURVATURE_ESTIMATE_HOLDS_UNDER_A_FOURFOLD_POPULATION_BOUNDED_THEOREM_NOTE_2026-09-27.md).
- [PR 9369 finite source](RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28.md).
- [PR 9372 finite source](RING_MODEL_ON_24_CUBED_A_LONGER_PROJECTION_RAISES_THE_CURVATURE_ESTIMATE_FROM_0_81_TO_1_05_AND_LEAVES_THE_ENERGY_UNCHANGED_BOUNDED_THEOREM_NOTE_2026-09-28.md).

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
