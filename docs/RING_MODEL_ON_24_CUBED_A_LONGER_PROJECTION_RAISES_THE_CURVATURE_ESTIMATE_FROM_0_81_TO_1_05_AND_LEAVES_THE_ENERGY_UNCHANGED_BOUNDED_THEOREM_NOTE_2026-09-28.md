---
claim_id: ring_model_on_24_cubed_a_longer_projection_raises_the_curvature_estimate_from_0_81_to_1_05_and_leaves_the_energy_unchanged_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied finite ring component with the landed conditional moment identities; curvature estimate from E(0), E(H1), E(2 H1) (H1 = 0.15) on 24^3 at k = pi/12 from the fixed-population projector (960 walkers, resampling interval 0.015, a guide field per probe field 0.5 h, seeds 603 and 604). The standard estimate averages the mixed energy over projection times [7.5, 30); here the projection runs to 60 and the same walkers also give the window [30, 60). The curvature estimate is 0.8118 +- 0.0369 in the standard window (seeds 0.8288, 0.7949) and 1.0490 +- 0.0145 in the late window (seeds 1.0611, 1.0368): both seeds move up, by 0.232 and 0.242. The energy per plaquette is 0.28509 and 0.28505. So on 24^3 the standard window underestimates the curvature estimate by about 0.24 while the energy is converged in it; the 24^3 values 0.83 to 0.86 of open PRs 9298, 9361 and 9365 carry this projection-time error. The late-window value agrees with the 16^3 late-window value 1.0616 +- 0.0283 (open PR 9369), and gives estimated upper bounds 0.272 = 1.043 s on the lowest transverse excitation and 0.143 = 0.547 s on the structure factor at k = pi/12, s = 2 sin(pi/24). Exact 2^3 control passes. Convergence of the late window is not tested. No certified susceptibility, frequency, population convergence, limit or physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_24_cubed_curvature_projection_time_test_2026_09_28.py
---

# On 24³ a longer projection raises the curvature estimate from 0.81 to 1.05 and leaves the energy unchanged

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

**The question.** Open PRs 9298, 9361 and 9365 found the 24³ estimate at
`k = π/12` near `0.85`, below the 16³ and 20³ values, and stable over a
doubled population. Those estimates average the mixed energy over projection
times `[7.5, 30)`. The slowest mode the probe field excites is the
smallest-momentum transverse mode, which is slowest on the largest torus. If
it has not relaxed by 7.5, the window carries a projection-time error. On 16³
a longer projection moved the estimate by `+0.057`, which was not resolved
there (open PR 9369).

**The test.** This block runs 24³ to projection time 60 with the settings of
open PR 9298 (seeds 603 and 604). From the same walkers it compares the
standard window with a late window `[30, 60)`.

## Result

**24³ at `k = π/12`, a guide per field, 960 walkers, seeds 603 and 604.**

| window | `χ` (seeds) | `u` |
|---|---|---|
| `[7.5, 30)` | `0.8118 ± 0.0369` (`0.8288`, `0.7949`) | `0.28509` |
| `[30, 60)` | `1.0490 ± 0.0145` (`1.0611`, `1.0368`) | `0.28505` |
| late minus standard | `+0.237` (seeds `+0.232`, `+0.242`) | `−0.00004` |

What follows:
- **The standard window underestimates `χ` on 24³.** Both seeds move up by
  about `0.24` between the windows. The standard-window value agrees with the
  earlier 24³ values `0.856 ± 0.042` (four seeds, open PR 9361) and
  `0.843 ± 0.041` (1920 walkers, open PR 9365). So the decrease those blocks
  report is a projection-time error of the standard window, not a property of
  the converged estimate. Doubling the population could not remove it,
  which is why it looked population-stable.
- **The late window is flat across tori.** The late-window value `1.049 ±
  0.015` agrees with the 16³ late-window value `1.062 ± 0.028` at `k = π/8`
  (open PR 9369), 0.4 standard errors apart.
- **The energy is converged in the standard window.** It moves by
  `0.00004`, as on 16³. The offset of the 24³ energy per plaquette from the
  8³ population-free value `0.2886` (open PR 9352) is therefore not a
  projection-time effect and remains open.
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
