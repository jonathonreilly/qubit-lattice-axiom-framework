---
claim_id: ring_model_on_16_cubed_the_curvature_estimate_also_rises_to_1_11_and_matches_24_cubed_window_by_window_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Supplied finite ring component with the landed conditional moment identities; curvature estimate from E(0), E(H1), E(2 H1) (H1 = 0.15) on 16^3 at k = pi/8 from the fixed-population projector (960 walkers, resampling interval 0.015, a guide field per probe field 0.5 h, seeds 401 and 402), projection to 90. The same walkers give three windows of projection time. [7.5, 30): 1.0264 +- 0.0252 (seeds 1.0167, 1.0361); [30, 60): 1.0579 +- 0.0173 (seeds 1.0649, 1.0509); [60, 90): 1.1130 +- 0.0212 (seeds 1.0917, 1.1342). The energy per plaquette is 0.28676, 0.28682, 0.28670 (the zero-field run repeats open PR 9369's walkers; the field runs are fresh realizations). In the two late windows 16^3 at k = pi/8 agrees with 24^3 at k = pi/12 (open PR 9391: 1.0670 and 1.1141) within 0.3 and 0.05 standard errors. So compared at equal projection windows the two tori give the same curvature estimate, near 1.06 in [30, 60) and 1.11 in [60, 90). On 16^3 the estimate rises by 0.032 and then 0.055 between successive windows, which the relaxation of the smallest-momentum mode does not account for; a slow drift common to both tori is not identified. With the [60, 90) value the landed moment inequalities give estimated upper bounds 0.396 = 1.015 s on the lowest transverse excitation and 0.221 = 0.565 s on the structure factor, s = 2 sin(pi/16). Exact 2^3 control passes. No converged, certified susceptibility, frequency, population convergence, limit or physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_16_cubed_curvature_projection_to_90_2026_09_29.py
---

# On 16³ the curvature estimate also rises to 1.11 and matches 24³ window by window

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
`RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`.
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15` and a guide field per probe field (`0.5 h`), as in
`RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md`.

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
  errors. Compared at equal projection windows they give the same value,
  near `1.06` and then `1.11`. The curvature estimate therefore does not
  fall between `k = π/8` on 16³ and `k = π/12` on 24³. The standard window
  differs between them because the 24³ smallest-momentum mode relaxes more
  slowly.
- **A slow drift common to both tori.** On 16³ the estimate rises by
  `0.032` and then `0.055` between successive windows, with the energy
  flat. The smallest-momentum mode on 16³ should have relaxed long before
  projection 30, so this rise is not its relaxation. On 24³ the late rise is
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
- **Convergence.** Not reached on either torus. The drift makes the absolute
  value time-dependent at the level of `0.05` per 30 units of projection;
  the equality of the two tori at equal windows is the robust statement.

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
