---
claim_id: ring_model_on_16_cubed_the_pair_guide_energy_also_rises_with_the_population_by_about_half_the_old_guide_rise_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Recorded finite fixed-population projector diagnostics for the supplied pure ring Hamiltonian H = -sum_p (U_p + U_p^dag) (V = 0) on the canonical zero-winding flip component of the 16^3 torus, with the positive pair guide psi = exp(0.35 N_flip - 0.049 N_pair) (N_pair = adjacent pairs of flippable plaquettes), seed 1, 2000 generations, at N_w = 240, 480, 960. Checked: the pair guide's local energy, rates and incremental pair counts against brute force on random 4^3 states (machine precision; integer counts exact). Recorded: u(Lc=0) = 0.28723 +- 0.00008, 0.28726 +- 0.00006, 0.28757 +- 0.00005 (rise from 240 to 960 walkers +0.00034); u(Lc=40) = 0.28769, 0.28763, 0.28777; effective population N_eff = 8.9, 12.0, 23.9; ESS/N_w 0.966-0.964. The 960-walker value reproduces an earlier independent realisation of the same settings (0.28755 +- 0.00007) within 0.2 combined bin errors. Beside the old guide exp(0.2 N_flip) series of the same seed and settings (0.28606, 0.28662, 0.28664 at 240, 480, 960 walkers; rise +0.00058), the pair-guide rise over the same populations is 0.58 of the old-guide rise. Neither series is population-converged at these sizes; the converged value is not determined. One seed; 10-bin errors (lower bounds under autocorrelation). No certified energy, convergence law, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_on_16_cubed_a_longer_projection_leaves_the_energy_unchanged_and_moves_the_curvature_estimate_within_its_errors_bounded_theorem_note_2026-09-28
runner: scripts/ring_model_16_cubed_pair_guide_population_series_2026_10_01.py
---

# Recorded 16³ diagnostics: the pair-guide energy also rises with the population, by about half the old-guide rise

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** recorded finite Monte Carlo diagnostics for a supplied model; unaudited.

## Supplied setting

The model is the pure ring Hamiltonian at `V = 0` on the canonical zero-winding flip
component of the 16³ torus. The landed setting is the one in
`RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28.md`.

- **Projector.** Fixed-population and continuous-time, with resampling every `Δτ = 0.015`.
- **Run.** 2000 generations, seed 1.
- **Guide.** The positive pair guide `ψ = exp(0.35 N_flip − 0.049 N_pair)`, where
  `N_pair` counts adjacent pairs of flippable plaquettes.

## Check

On random 4³ states, the pair guide's local energy and rates agree with brute force
to `7·10⁻¹⁵`. The incremental typed pair counts agree exactly.

## Recorded diagnostics

| `N_w` | `u(Lc = 0)` | `u(Lc = 40)` | `N_eff` | distinct ancestors, lag 2 |
|---|---|---|---|---|
| 240 | `0.28723 ± 0.00008` | `0.28769` | 8.9 | 0.0053 |
| 480 | `0.28726 ± 0.00006` | `0.28763` | 12.0 | 0.0036 |
| 960 | `0.28757 ± 0.00005` | `0.28777` | 23.9 | 0.0017 |

- **Reproducibility.** The 960-walker value matches an earlier independent
  realisation of the same settings, `0.28755 ± 0.00007`, within 0.2 combined bin errors.
- **Comparison with the old guide.** The old guide `exp(0.2 N_flip)` was run with the
  same seed and settings: `0.28606`, `0.28662`, `0.28664` at 240, 480 and 960
  walkers, and `0.28699` at 1920.
  - From 240 to 960 walkers, the pair-guide energy rises by `+0.00034` and the
    old-guide energy by `+0.00058`, a ratio of 0.58.
  - At every population the pair-guide value lies above the old-guide value.

## Reading

These are recorded finite diagnostics.
- Both guides' energies rise with the population over 240–960 walkers. The pair
  guide's rise is about half the old guide's.
- The effective population grows from 9 to 24 while the walker count grows fourfold.
- Neither series is population-converged at these sizes, and the converged value
  is not determined. The data are consistent with a converged value at or above
  the largest values recorded, but they do not establish it.

## What this does not establish

- No certified energy.
- No convergence law.
- No physical identification.
- No audit verdict.

The run uses one seed, and errors are 10-bin errors.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied model; 16³, one seed, the stated populations.
- **N2:** no phase or no-go wall is imported.
- **N3:** the Hamiltonian, component and guide remain supplied.
- **N4:** the landed component and estimator are used as stated there.
- **N5:** recorded Monte Carlo diagnostics with a brute-force implementation check.
- **N6:** converged values remain open.
- **N7:** other guides, seeds and populations remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_16_cubed_pair_guide_population_series_2026_10_01.py
```

Four checks; prints `TOTAL: PASS=4 FAIL=0` in about 23 minutes (single thread).
