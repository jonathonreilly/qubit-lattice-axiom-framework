---
claim_id: ring_model_on_16_cubed_a_longer_projection_leaves_the_energy_unchanged_and_moves_the_curvature_estimate_within_its_errors_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied finite ring component with the landed conditional moment identities; curvature estimate from E(0), E(H1), E(2 H1) (H1 = 0.15) on 16^3 at k = pi/8 from the fixed-population projector (960 walkers, resampling interval 0.015, a guide field per probe field 0.5 h, seeds 401 and 402). The standard estimate averages the mixed energy over projection times [7.5, 30); here the projection runs to 60 and the same walkers also give the window [30, 60). The energy per plaquette is 0.28676 and 0.28682 (difference 0.00006), and the curvature estimate 1.0043 +- 0.0381 and 1.0616 +- 0.0283 (difference +0.057, with the two seeds moving +0.124 and -0.009). So on 16^3 the standard window is converged in the energy: the offset of the 16^3 energy per plaquette from the 8^3 population-free value 0.2886 is not a projection-time effect. A projection-time shift of the curvature estimate is not resolved at this precision. Exact 2^3 control passes. No certified susceptibility, frequency, population convergence, limit or physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_16_cubed_curvature_projection_time_test_2026_09_28.py
---

# On 16³ a longer projection leaves the energy unchanged and moves the curvature estimate within its errors

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
`RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`.
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15` and a guide field per probe field (`0.5 h`), as in
`RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md`.

**Where the standard estimate averages.** It averages the mixed energy over
projection times `[7.5, 30)`: generations 500 to 2000 at resampling interval
0.015.

**Why that might not suffice.** The slowest mode the probe field excites is
the smallest-momentum transverse mode, and its energy falls with the torus.
If it has not relaxed by 7.5, the window could carry a projection-time error
that grows with the torus. That error could explain:
- the energy offsets of open PRs 9361 and 9365, which barely change with the
  population;
- part of their lower curvature estimate on 24³.

**The test.** This block runs 16³ to projection time 60. From the same walkers
it compares the standard window with a late window `[30, 60)`.

## Result

**16³ at `k = π/8`, a guide per field, 960 walkers, seeds 401 and 402.**

| window | `χ` (seeds) | `u` |
|---|---|---|
| `[7.5, 30)` | `1.0043 ± 0.0381` (`0.9662`, `1.0425`) | `0.28676` |
| `[30, 60)` | `1.0616 ± 0.0283` (`1.0899`, `1.0333`) | `0.28682` |
| late minus standard | `+0.057` | `+0.00006` |

What follows:
- **The energy is converged in the standard window.** The late window moves
  `u` by `0.00006`. So the offset of the 16³ energy per plaquette from the
  8³ population-free value `0.2886` (open PR 9352) is not a projection-time
  effect. Open PR 9358 found it moves by only `0.0004` over a fourfold
  population, so the offset remains unexplained.
- **The curvature estimate is not resolved.** It moves by `+0.057`, but one
  seed moves by `+0.124` and the other by `−0.009`. A projection-time shift
  of `χ` is not resolved on 16³ at this precision.
- **Consistency.** The standard-window value `1.004` agrees with the
  standard-setting values `1.039 ± 0.022` (open PR 9298) and `1.061 ± 0.036`
  (open PR 9358) within errors.
- **Next.** The smallest-momentum mode is slower on 24³, so the same test
  there is the sharper one; it is running as the next block.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin
  error, over two seeds.
- **Correlation.** The two windows come from the same walkers, so their
  difference is correlated. The seed spread of the difference is the honest
  measure.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 16³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block tests the projection time of their estimator on 16³.
- **N5:** finite estimates in two windows.
- **N6:** the 24³ test and the origin of the energy offset remain open.
- **N7:** other guides, populations, projection times and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_16_cubed_curvature_projection_time_test_2026_09_28.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about fifty minutes of computation.
