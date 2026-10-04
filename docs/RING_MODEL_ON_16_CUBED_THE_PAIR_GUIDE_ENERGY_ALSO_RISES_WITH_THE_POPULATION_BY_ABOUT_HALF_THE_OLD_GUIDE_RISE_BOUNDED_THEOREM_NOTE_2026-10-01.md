---
claim_id: ring_model_on_16_cubed_the_pair_guide_energy_also_rises_with_the_population_by_about_half_the_old_guide_rise_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Recorded finite seeded sampler results for the supplied ring model and the full settings in the body. Numerical matrix controls and nominal bin/seed errors only; no certified spectrum, bias, convergence, component connectivity, physical identification or audit verdict."
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

The model is the pure ring Hamiltonian at `V = 0` with the intended reference of the canonical zero-winding flip component of the 16³ torus; the actual loop-prepared banks have the component qualification below. The landed setting is the one in
[RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28](RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28.md).

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

- **Reproducibility.** The 960-walker value matches an earlier different consumed random stream
  at the same seed of the same settings, `0.28755 ± 0.00007`, within 0.2 combined bin errors.
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
- Neither series supplies a population-convergence certificate. A limit, monotonicity beyond the sampled settings, and a bound above or below the largest recorded value are all undetermined. Sharing a seed does not establish statistical independence of the two consumed random streams.

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

## Reviewed interpretation and preparation boundary

The larger-torus initial banks are prepared by zero-winding loop moves from a canonical start. Such loop moves preserve Gauss law and winding but have not been proved to remain in the canonical plaquette-flip component; every subsequent plaquette trajectory stays in its own component. The frozen-family theorem in this batch demonstrates why zero winding alone is insufficient. No all-start or 16³ component certificate is imported. Ideal selected-component ground-state identities remain conditional, with response symmetry and centered positive measure required by the current moment parent.

All numerical matrix eigenvalues are floating-point references, not rigorous enclosures. Bin/seed errors and their quadrature sums are nominal diagnostics; field, window and guide covariance and mixing are not certified. A variance-ratio labelled N_eff is not a number of independent samples. Finite-path motion in reptation does not bound equilibrium or path-length error. Population-free sampling removes walker resampling only. The tables report captured seeded means; they supply no convergence certificate or causal attribution. Historical runner introductory prose and console labels must be read within this corrected scope.

Original source and captured evidence remain recoverable through [PR #9443](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9443) at frozen head `1e4c87a6fdfb5441ad4346d56cd596d298f4a82e`. Review grants no audit status.

## Actual source dependencies

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_ON_16_CUBED_THE_PROJECTOR_ENERGY_DEPENDS_ON_THE_GUIDE_BY_SIX_STANDARD_ERRORS_AND_THE_EFFECTIVE_POPULATION_STAYS_BELOW_TWENTY_FIVE_BOUNDED_THEOREM_NOTE_2026-10-01](RING_MODEL_ON_16_CUBED_THE_PROJECTOR_ENERGY_DEPENDS_ON_THE_GUIDE_BY_SIX_STANDARD_ERRORS_AND_THE_EFFECTIVE_POPULATION_STAYS_BELOW_TWENTY_FIVE_BOUNDED_THEOREM_NOTE_2026-10-01.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01](RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md): conditional definitions or the recorded finite comparison only.
