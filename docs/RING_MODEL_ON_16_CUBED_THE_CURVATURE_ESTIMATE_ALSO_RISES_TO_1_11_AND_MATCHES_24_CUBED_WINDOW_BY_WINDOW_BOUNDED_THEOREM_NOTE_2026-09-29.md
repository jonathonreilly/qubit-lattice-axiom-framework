---
claim_id: ring_model_on_16_cubed_the_curvature_estimate_also_rises_to_1_11_and_matches_24_cubed_window_by_window_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_16_cubed_curvature_projection_to_90_2026_09_29.py
---

# Recorded 16³ projection-window diagnostics and finite comparison with 24³

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
[RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md).
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15` and a guide field per probe field (`0.5 h`), as in
[RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md).

**Where this starts.** Two open PRs ran the smallest-momentum estimate to
long projection times:
- open PR 9369 ran 16³ to projection 60, giving `1.004` in `[7.5, 30)` and
  `1.062` in `[30, 60)`;
- open PR 9391 ran 24³ to projection 90 with three windows, giving `0.83`,
  `1.07` and `1.11`, so the estimate there was still rising in the last
  window.

**The test.** This block runs 16³ with the seeds of open PR 9369 (401, 402)
to projection time 90, with the same three windows. The zero-field run
repeats open PR 9369's walkers over the first 60, so its energies are
identical. The field runs are fresh realizations, because the longer
zero-field run uses more random numbers before them.

## Result

**16³ at `k = π/8` beside 24³ at `k = π/12` (open PR 9391), 960 walkers.**

| window | 16³ `χ` (seeds) | 16³ `u` | 24³ `χ` |
|---|---|---|---|
| `[7.5, 30)` | `1.0264 ± 0.0252` (`1.0167`, `1.0361`) | `0.28676` | `0.8320 ± 0.0451` |
| `[30, 60)` | `1.0579 ± 0.0173` (`1.0649`, `1.0509`) | `0.28682` | `1.0670 ± 0.0250` |
| `[60, 90)` | `1.1130 ± 0.0212` (`1.0917`, `1.1342`) | `0.28670` | `1.1141 ± 0.0097` |

What follows:
- **The two tori agree window by window at late times.** In `[30, 60)` and
  `[60, 90)` the 16³ and 24³ estimates differ by 0.3 and 0.05 standard
  errors. Compared at equal projection windows the estimates agree within the reported errors,
  near `1.06` and then `1.11`. This agreement of finite late-window means does not prove equal
  converged susceptibilities. The different standard-window means may reflect
  response or sampler transients, whose cause is not established.
- **A slow drift common to both tori.** On 16³ the estimate rises by
  `0.032` and then `0.055` between successive windows, with the energy
  flat. No independently controlled lower spectral gap or equilibration time is
  available to exclude a slow response mode. An excitation upper bound does
  not provide such a lower gap. On 24³ the late rise is
  `0.047`. A slow drift of similar size on both tori is present. Its source
  (a slow physical component of the response, or the sampler) is not
  identified here.
- **Moment inequalities.** With `s = 2 sin(π/16)`, the `[60, 90)` value
  gives estimated upper bounds of `0.396 = 1.015 s` on the lowest
  transverse excitation and `0.221 = 0.565 s` on the structure factor. These
  are estimated bounds, not certified frequencies.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin
  error, over two seeds.
- **Correlation.** The windows come from the same walkers, so differences
  between them are correlated.
- **Convergence.** Not established on either torus. The drift makes the absolute
  value time-dependent at the level of `0.05` per 30 units of projection;
  agreement of the finite sample means at equal windows is the observation.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 16³ with the stated settings, compared with 24³ from open PR 9391.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block extends open PR 9369's projection and compares with open PR 9391.
- **N5:** finite estimates in three windows; the window-by-window agreement is the result.
- **N6:** the converged values and the source of the slow drift remain open.
- **N7:** other guides, populations, projection times and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_16_cubed_curvature_projection_to_90_2026_09_29.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about seventy-five minutes of computation.

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

- [PR 9369 finite source](RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28.md).
- [PR 9391 finite source](RING_MODEL_ON_24_CUBED_FRESH_SEEDS_REPRODUCE_THE_PROJECTION_TIME_RISE_AND_A_THIRD_WINDOW_PUTS_THE_CURVATURE_ESTIMATE_AT_1_11_BOUNDED_THEOREM_NOTE_2026-09-29.md).

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
