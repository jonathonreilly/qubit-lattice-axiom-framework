---
claim_id: ring_model_on_16_cubed_a_doubled_population_reproduces_the_slow_late_rise_of_the_curvature_estimate_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Recorded finite seeded sampler results for the supplied ring model and the full settings in the body. Numerical matrix controls and nominal bin/seed errors only; no certified spectrum, bias, convergence, component connectivity, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_on_16_cubed_the_curvature_estimate_also_rises_to_1_11_and_matches_24_cubed_window_by_window_bounded_theorem_note_2026-09-29
runner: scripts/ring_model_16_cubed_curvature_late_drift_population_test_2026_10_01.py
---

# On 16³ a doubled population reproduces the slow late rise of the curvature estimate

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
[RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md).
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15` and a guide field per probe field.

**What the landed note found.** The landed note
[RING_MODEL_ON_16_CUBED_THE_CURVATURE_ESTIMATE_ALSO_RISES_TO_1_11_AND_MATCHES_24_CUBED_WINDOW_BY_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-29](RING_MODEL_ON_16_CUBED_THE_CURVATURE_ESTIMATE_ALSO_RISES_TO_1_11_AND_MATCHES_24_CUBED_WINDOW_BY_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-29.md)
used 960 walkers. In the projection windows `[7.5, 30)`, `[30, 60)` and
`[60, 90)` it found:
- the 16³ estimate rises slowly, `1.026`, `1.058`, `1.113`, with the energy
  flat;
- no controlled lower gap or equilibration time excludes a slow response;
- the source of the rise was left open.

**The test.** Population dependence is one diagnostic; a sampler effect can remain similar at both tested populations. This block doubles the population to 1920 walkers, with fresh seeds 411 and 412,
and repeats the three windows.

## Result

**16³ at `k = π/8`, a guide per field, projection to 90.**

| window | `χ`, 1920 walkers (seeds) | `χ`, 960 walkers (landed) | difference | `u`, 1920 / 960 |
|---|---|---|---|---|
| `[7.5, 30)` | `1.0209 ± 0.0223` (`1.0127`, `1.0292`) | `1.0264 ± 0.0252` | `−0.0055` (0.2σ) | `0.28708 / 0.28676` |
| `[30, 60)` | `1.0856 ± 0.0436` (`1.0419`, `1.1292`) | `1.0579 ± 0.0173` | `+0.0277` (0.6σ) | `0.28698 / 0.28682` |
| `[60, 90)` | `1.1047 ± 0.0138` (`1.1095`, `1.1000`) | `1.1130 ± 0.0212` | `−0.0083` (0.3σ) | `0.28690 / 0.28670` |

What follows:
- **The two tested populations give similar recorded window means.** Window by window the
  two populations agree within 0.6 combined standard errors. The rise from
  the first to the last window is `0.084` at 1920 walkers and `0.087` at 960.
  These finite observations do not exclude common population bias or certify population independence.
- **The source remains open.** It could be a slow component of the response,
  or a property of the sampler that does not change with the walker count.
- **The energy does depend on the population.** It is higher by `0.0002` to
  `0.0003` at 1920 walkers. Neither the sign of the bias nor its cause is established.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin
  error, over two seeds.
- **Correlation.** The windows come from the same walkers, so differences
  between them are correlated.
- **Range of the test.** A factor of two in the population is tested; larger
  factors are not.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 16³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block repeats the landed 16³ projection-to-90 test at a doubled population.
- **N5:** finite estimates in three windows at two populations.
- **N6:** the source of the late rise and the converged values remain open.
- **N7:** other guides, populations, projection times and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_16_cubed_curvature_late_drift_population_test_2026_10_01.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about three hours of computation.

## Reviewed interpretation and preparation boundary

The larger-torus initial banks are prepared by zero-winding loop moves from a canonical start. Such loop moves preserve Gauss law and winding but have not been proved to remain in the canonical plaquette-flip component; every subsequent plaquette trajectory stays in its own component. The frozen-family theorem in this batch demonstrates why zero winding alone is insufficient. No all-start or 16³ component certificate is imported. Ideal selected-component ground-state identities remain conditional, with response symmetry and centered positive measure required by the current moment parent.

All numerical matrix eigenvalues are floating-point references, not rigorous enclosures. Bin/seed errors and their quadrature sums are nominal diagnostics; field, window and guide covariance and mixing are not certified. A variance-ratio labelled N_eff is not a number of independent samples. Finite-path motion in reptation does not bound equilibrium or path-length error. Population-free sampling removes walker resampling only. The tables report captured seeded means; they supply no convergence certificate or causal attribution. Historical runner introductory prose and console labels must be read within this corrected scope.

Original source and captured evidence remain recoverable through [PR #9424](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9424) at frozen head `93ad64b48abb7a72f213194b75ddef9797c22eef`. Review grants no audit status.

## Actual source dependencies

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01](RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md): conditional definitions or the recorded finite comparison only.
