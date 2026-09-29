---
claim_id: ring_model_on_24_cubed_fresh_seeds_reproduce_the_projection_time_rise_and_a_third_window_puts_the_curvature_estimate_at_1_11_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_24_cubed_curvature_projection_to_90_fresh_seeds_2026_09_29.py
---

# Recorded 24³ projection-window diagnostics with fresh seeds

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

**What open PR 9372 found.** With seeds 603 and 604, the 24³ estimate at
`k = π/12` is `0.81` in the standard window of projection times `[7.5, 30)`
and `1.05` in the late window `[30, 60)`, with the energy unchanged. That
block left two questions:
- whether other seeds reproduce the rise;
- whether the late window is converged.

**The test.** Two fresh seeds (605, 606) run to projection time 90, with the
settings of open PR 9372 otherwise. The same walkers give the three windows
`[7.5, 30)`, `[30, 60)` and `[60, 90)`.

## Result

**24³ at `k = π/12`, a guide per field, 960 walkers, seeds 605 and 606.**

| window | `χ` (seeds) | `u` |
|---|---|---|
| `[7.5, 30)` | `0.8320 ± 0.0451` (`0.8403`, `0.8237`) | `0.28515` |
| `[30, 60)` | `1.0670 ± 0.0250` (`1.0420`, `1.0920`) | `0.28508` |
| `[60, 90)` | `1.1141 ± 0.0097` (`1.1119`, `1.1164`) | `0.28509` |

What follows:
- **The rise reproduces.** The first two windows agree with open PR 9372
  (`0.8118 ± 0.0369` and `1.0490 ± 0.0145`) within 0.4 and 0.6 standard
  errors. The estimate rises by `0.235` from the standard to the late
  window, and the energy per plaquette stays within `0.00007`.
- **Convergence of the late window is not established.** From `[30, 60)` to
  `[60, 90)` the estimate rises again, by `0.070` and `0.024` in the two
  seeds (`0.047` on average). That is a fifth of the first rise, while the
  energy moves by `0.00001`. The sampled means rise, but their limit, direction of asymptotic approach
  and remaining bias are not bounded. On 24³ at `k = π/12` it stands at `1.114` at the latest window, and
  the limit is not determined here.
- **Moment inequalities.** With `s = 2 sin(π/24)`, the `[60, 90)` value gives
  estimated upper bounds of `0.264 = 1.012 s` on the lowest transverse
  excitation and `0.147 = 0.564 s` on the structure factor. These are
  estimated bounds, not certified frequencies. A larger converged `χ` would
  lower the first bound further.
- **For other large-torus estimates.** On 16³ the late window `[30, 60)`
  gave `1.062` (open PR 9369). The slow approach seen here suggests it may
  also be short of its limit; that is not tested here.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin
  error, over two seeds.
- **Correlation.** The three windows come from the same walkers, so their
  differences are correlated; the agreement in sign of the two seeds'
  differences is the measure used here.
- **Convergence.** Not established. The rise between the second and third
  windows is smaller than between the first and second, but a later window
  or longer projection would be needed to bound what remains.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 24³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block replicates open PR 9372 and extends its projection.
- **N5:** finite estimates in three windows; the seed-level rises are the result.
- **N6:** the converged 24³ value and the convergence of other large-torus late windows remain open.
- **N7:** other guides, populations, projection times and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_24_cubed_curvature_projection_to_90_fresh_seeds_2026_09_29.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about six and a half hours of computation.

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
- [PR 9372 finite source](RING_MODEL_ON_24_CUBED_A_LONGER_PROJECTION_RAISES_THE_CURVATURE_ESTIMATE_FROM_0_81_TO_1_05_AND_LEAVES_THE_ENERGY_UNCHANGED_BOUNDED_THEOREM_NOTE_2026-09-28.md).

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
