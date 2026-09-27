---
claim_id: ring_model_on_12_cubed_the_per_field_guide_curvature_estimate_holds_under_a_fourfold_population_while_the_one_guide_estimate_falls_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied finite ring component with the landed conditional moment identities; curvature estimate from E(0), E(H1), E(2 H1) (H1 = 0.15) on 12^3 at k = pi/6 from the fixed-population projector (projection 30, resampling interval 0.015, seeds 401 and 402). With a guide field per probe field (0.5 h) the estimate is 1.0690 +- 0.0257, 1.0721 +- 0.0176 and 1.0573 +- 0.0129 at 960, 1920 and 3840 walkers (the 960 value from open PR 9352); a linear fit in 1/N_w gives 1.0551 +- 0.0189 with slope 18 +- 36. With one guide field for the three probe fields (0.5 H1) it is 1.2520 +- 0.0221, 1.2159 +- 0.0304 and 1.1924 +- 0.0220, fitted intercept 1.1737 +- 0.0282 with slope 76 +- 39. The scheme difference falls from -0.183 to -0.135 and the fitted intercepts still differ by -0.119 +- 0.034 (3.5 standard errors). The per-field energy per plaquette is 0.28798 and 0.28807 at 1920 and 3840 walkers, against 0.28733 and 0.28763 with one guide. So over a fourfold population the per-field estimate and energy hold within errors while the one-guide estimate falls without reaching them; a 1/N_w extrapolation over this range does not remove the one-guide scheme's error. Exact 2^3 control passes. No population-free value on 12^3, certified susceptibility, frequency, population convergence, limit or physical reading."
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
`RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`.
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15`. The landed notes, including
`RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md`,
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
  `1/N_w` extrapolation over this range does not remove that scheme's
  error.
- **Reading.** With the 8³ reptation agreement (open PR 9352), this supports
  the per-field values that the landed notes use as the population-stable
  estimate on these tori. It does not provide a population-free value on
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
- **N4:** the landed parents' scopes govern; this block qualifies which guide scheme's estimate is population-stable on 12³.
- **N5:** finite estimates at three populations; the population dependence is the result.
- **N6:** a population-free value on 12³ and larger tori remains open.
- **N7:** other guides, populations and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_12_cubed_curvature_population_series_in_both_guide_schemes_2026_09_26.py
```

Four checks; prints `TOTAL: PASS=4 FAIL=0` in about two and a quarter hours of computation.
