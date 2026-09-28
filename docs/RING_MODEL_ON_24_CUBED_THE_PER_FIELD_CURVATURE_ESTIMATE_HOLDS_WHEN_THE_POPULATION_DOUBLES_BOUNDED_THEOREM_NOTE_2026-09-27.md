---
claim_id: ring_model_on_24_cubed_the_per_field_curvature_estimate_holds_when_the_population_doubles_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied finite ring component with the landed conditional moment identities; curvature estimate from E(0), E(H1), E(2 H1) (H1 = 0.15) on 24^3 at k = pi/12 from the fixed-population projector (projection 30, resampling interval 0.015) with a guide field per probe field (0.5 h). Seeds 603 and 604 at 1920 walkers give 0.8752 and 0.8113, chi = 0.843 +- 0.041; the same seeds at 960 walkers gave 0.908 and 0.754 (open PR 9298), mean 0.831, and four seeds at 960 walkers give 0.856 +- 0.042 (open PR 9361). So the 24^3 estimate does not move when the population doubles, as on 12^3 and 16^3 (open PRs 9356, 9358), and remains below 20^3 (0.990 +- 0.032 at pi/10) and 16^3 (1.061 +- 0.036 at pi/8). The energy per plaquette rises only from 0.28502 to 0.28537, still 0.0032 below the 8^3 population-free value 0.2886; that offset is not explained here. Exact 2^3 control passes. No certified susceptibility, frequency, soft-mode claim, population convergence, limit or physical reading."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_24_cubed_per_field_curvature_doubled_population_2026_09_27.py
---

# On 24³ the per-field curvature estimate holds when the population doubles

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

Open PR 9361 put the 24³ estimate at `k = π/12` at `0.856 ± 0.042` from four
seeds at 960 walkers, below the 20³ and 16³ values. Its 24³ energy per
plaquette lay `0.0036` below the 8³ population-free value, so a population
error could not be excluded. This block reruns seeds 603 and 604 at 1920
walkers (projection 30, resampling interval 0.015).

## Result

**24³ at `k = π/12`, a guide per field.**

| population | seeds | `χ` | energy per plaquette |
|---|---|---|---|
| 960 (open PR 9298) | 603, 604: `0.908`, `0.754` | mean `0.831` | — |
| 960 (open PR 9361) | four seeds | `0.856 ± 0.042` | `0.28502` (seeds 605, 606) |
| 1920 (this block) | 603, 604: `0.8752`, `0.8113` | `0.843 ± 0.041` | `0.28537` |

What follows:
- **The estimate holds.** Doubling the population moves the two-seed
  estimate by `+0.012`, within its errors, as on 12³ and 16³ (open PRs 9356,
  9358). Over this range the low 24³ value is not a population effect of the
  per-field estimate.
- **The decrease stands.** Per field, the estimates are `1.061 ± 0.036` on
  16³ (`π/8`), `0.990 ± 0.032` on 20³ (`π/10`) and about `0.85` on 24³
  (`π/12`).
- **Open question.** The energy per plaquette rises by only `0.0004` and
  stays `0.0032` below the 8³ population-free value `0.2886`. This block does
  not explain that offset, and it leaves open whether the decrease comes from
  the momentum or from the torus. A 24³ value at `k = π/6`, the smallest
  momentum of 12³, would separate the two; that run is queued as backlog
  work.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin error,
  over two seeds, so they are rough.
- **Seeds.** The 960-walker values come from other runs with the same
  settings.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 24³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block tests the population dependence of the 24³ estimate.
- **N5:** finite estimates at two populations; the stability and the unexplained energy offset are the result.
- **N6:** a fixed-momentum comparison and a population-free value on 24³ remain open.
- **N7:** other guides, populations and estimators remain available.
- **N8:** no physical identification, soft-mode claim, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_24_cubed_per_field_curvature_doubled_population_2026_09_27.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about six hours of computation on a shared machine.
