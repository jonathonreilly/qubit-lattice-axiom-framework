---
claim_id: ring_model_on_16_cubed_the_per_field_guide_curvature_estimate_holds_under_a_fourfold_population_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied finite ring component with the landed conditional moment identities; curvature estimate from E(0), E(H1), E(2 H1) (H1 = 0.15) on 16^3 at k = pi/8 from the fixed-population projector (projection 30, resampling interval 0.015, seeds 401 and 402) with a guide field per probe field (0.5 h), the scheme of the landed notes. The estimate is 1.039 +- 0.022 at 960 walkers (open PR 9298), 1.0698 +- 0.0446 at 1920 and 1.0506 +- 0.0284 at 3840; a linear fit in 1/N_w gives 1.0608 +- 0.0361 with slope -19 +- 45, and the energy per plaquette is 0.28680, 0.28689 and 0.28717. So on 16^3, where the two guide schemes differ most at 960 walkers (one guide 1.307 +- 0.029, open PR 9328), the per-field estimate holds within errors over a fourfold population, as on 12^3 (open PR 9356). Exact 2^3 control passes. No one-guide population series on 16^3, population-free value, certified susceptibility, frequency, population convergence, limit or physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_16_cubed_per_field_curvature_population_series_2026_09_27.py
---

# On 16³ the per-field-guide curvature estimate holds under a fourfold population

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
`RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`.
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15` and a guide field per probe field (`0.5 h`), the scheme of
`RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md`.

The one-guide scheme differs from this one by `0.268` at 960 walkers on 16³,
its largest recorded split (open PR 9328). On 12³ open PR 9356 found the
per-field estimate stable from 960 to 3840 walkers while the one-guide
estimate fell. This block repeats the per-field population series on 16³.

## Result

**16³ at `k = π/8`, a guide per field.** Projection 30, resampling interval
0.015, seeds 401 and 402.

| walkers | `χ` | `u` |
|---|---|---|
| 960 (open PR 9298) | `1.039 ± 0.022` | `0.28680` |
| 1920 | `1.0698 ± 0.0446` (seeds `1.0252`, `1.1144`) | `0.28689` |
| 3840 | `1.0506 ± 0.0284` (seeds `1.0222`, `1.0790`) | `0.28717` |
| fit `a + b/N_w` | `a = 1.0608 ± 0.0361`, `b = −19 ± 45` | |

What follows:
- **The per-field scheme holds on 16³.** Its estimate stays at 1.04–1.07
  over a fourfold population, with a slope consistent with zero, as on 12³
  (open PR 9356).
- **Contrast with the other scheme.** At 960 walkers the one-guide estimate
  on 16³ is `1.307 ± 0.029` (open PR 9328).
- **Reading.** The per-field values that the landed notes use are the
  population-stable ones on 12³ and 16³ over this range.
- **Energy.** The energy per plaquette rises by `0.0004` from 960 to 3840
  walkers; the curvature estimate does not move beyond its errors.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin error,
  over two seeds per point, so they are rough.
- **Fit model.** The `1/N_w` form is an assumption, and three points test it
  weakly.
- **Seeds.** The 960-walker value comes from a different run with the same
  seeds and settings.
- **Scope.** No one-guide series on 16³ is run here.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 16³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block qualifies the population stability of their scheme on 16³.
- **N5:** finite estimates at three populations.
- **N6:** population-free values on 12³ and larger tori remain open.
- **N7:** other guides, populations and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_16_cubed_per_field_curvature_population_series_2026_09_27.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about four hours of computation on a shared machine.
