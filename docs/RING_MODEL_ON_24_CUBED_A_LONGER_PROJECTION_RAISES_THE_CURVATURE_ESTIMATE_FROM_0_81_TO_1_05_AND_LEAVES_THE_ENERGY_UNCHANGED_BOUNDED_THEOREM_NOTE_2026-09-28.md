---
claim_id: ring_model_on_24_cubed_a_longer_projection_raises_the_curvature_estimate_from_0_81_to_1_05_and_leaves_the_energy_unchanged_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_24_cubed_curvature_projection_time_test_2026_09_28.py
---

# Recorded 24³ projection-window diagnostics: curvature mean rises from 0.81 to 1.05

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

**The question.** Open PRs 9298, 9361 and 9365 found the 24³ estimate at
`k = π/12` near `0.85`, below the 16³ and 20³ values, and stable over a
doubled population. Those estimates average the mixed energy over projection
times `[7.5, 30)`. A slow probe response is a possible explanation, but its spectral
gap and equilibration time are not independently controlled here. If
it has not relaxed by 7.5, the window could carry a projection-time error. On 16³
a longer projection moved the estimate by `+0.057`, which was not resolved
there (open PR 9369).

**The test.** This block runs 24³ to projection time 60 at the same population and interval as PR 9298, but with seeds 603 and 604
(the original PR 9298 uses 601 and 602, and these runs also use a +7 seed offset). From the same walkers it compares the
standard window with a late window `[30, 60)`.

## Result

**24³ at `k = π/12`, a guide per field, 960 walkers, seeds 603 and 604.**

| window | `χ` (seeds) | `u` |
|---|---|---|
| `[7.5, 30)` | `0.8118 ± 0.0369` (`0.8288`, `0.7949`) | `0.28509` |
| `[30, 60)` | `1.0490 ± 0.0145` (`1.0611`, `1.0368`) | `0.28505` |
| late minus standard | `+0.237` (seeds `+0.232`, `+0.242`) | `−0.00004` |

What follows:
- **The standard window gives smaller sampled curvature estimates on 24³.** Both seeds move up by
  about `0.24` between the windows. The standard-window value agrees with the
  earlier 24³ values `0.856 ± 0.042` (four seeds, open PR 9361) and
  `0.843 ± 0.041` (1920 walkers, open PR 9365). These runs demonstrate window dependence of the sample means; they
  do not determine the converged estimate or attribute all earlier differences
  to a unique cause. The tested doubled population gave a similar smaller sample mean,
  which is why it looked stable within rough errors over the tested populations.
- **The two finite late-window estimates agree within rough errors.** The late-window value `1.049 ±
  0.015` agrees with the 16³ late-window value `1.062 ± 0.028` at `k = π/8`
  (open PR 9369), 0.4 standard errors apart.
- **The measured energy changes little between these windows.** It moves by
  `0.00004`, as on 16³. The offset of the 24³ energy per plaquette from the
  8³ finite reptation estimate `0.2886` (open PR 9352) is not explained by this comparison; projection convergence, finite-size
  effects and estimator bias all remain open.
- **Moment inequalities.** With `s = 2 sin(π/24)`, the late-window values
  give estimated upper bounds of `0.272 = 1.043 s` on the lowest transverse
  excitation at `k = π/12` and `0.143 = 0.547 s` on the structure factor. The
  standard window gives `0.309 = 1.185 s` and `0.126 = 0.481 s`. These are
  estimated bounds, not certified frequencies.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin
  error, over two seeds.
- **Correlation.** The two windows come from the same walkers, so their
  difference is correlated; the agreement of the two seeds' differences is
  the measure used here.
- **Convergence of the late window.** Not tested. A later window or longer
  projection would test it.
- **Other estimates.** Other standard-window estimates on large tori may
  carry the same error. They are not rerun here.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 24³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block tests the projection time of their estimator on 24³.
- **N5:** finite estimates in two windows; the seed-level shift is the result.
- **N6:** convergence of the late window and the origin of the energy offset remain open.
- **N7:** other guides, populations, projection times and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_24_cubed_curvature_projection_time_test_2026_09_28.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about four and a half hours of computation.

## Seed provenance correction

PR 9298's actual production call uses labels 601 and 602, yielding the
printed 0.908 and 0.754 values. References in the original runner labels to
603 and 604 for that earlier run are incorrect. Later 603/604 runs are distinct
realizations; they are not a matched-seed rerun of PR 9298.

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
- [PR 9361 finite source](RING_MODEL_ON_24_CUBED_FOUR_SEEDS_PUT_THE_PER_FIELD_CURVATURE_ESTIMATE_AT_0_86_BELOW_THE_16_AND_20_CUBED_VALUES_BOUNDED_THEOREM_NOTE_2026-09-27.md).
- [PR 9365 finite source](RING_MODEL_ON_24_CUBED_THE_PER_FIELD_CURVATURE_ESTIMATE_HOLDS_WHEN_THE_POPULATION_DOUBLES_BOUNDED_THEOREM_NOTE_2026-09-27.md).
- [PR 9369 finite source](RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28.md).

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
