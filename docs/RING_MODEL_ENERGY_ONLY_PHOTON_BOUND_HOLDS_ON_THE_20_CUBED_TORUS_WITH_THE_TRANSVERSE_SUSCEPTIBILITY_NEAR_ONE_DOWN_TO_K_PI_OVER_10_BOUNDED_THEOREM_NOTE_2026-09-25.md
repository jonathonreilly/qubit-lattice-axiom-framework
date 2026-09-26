---
claim_id: ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Restated conditional moment identities of a supplied finite ring component, plus finite-projector energy
  diagnostics on16/20tori with two seeds. Curvature estimates require ground-component symmetries and vanishing-field
  control; the resulting numbers are estimated upper bounds, not certified excitation frequencies, soft-mode exclusions,
  population convergence or a limit.
upstream_dependencies:
- minimal_axioms
- ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
- gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
- ring_model_winding_sector_energies_give_an_electric_coupling_that_agrees_with_the_transverse_susceptibility_on_8_cubed_and_the_comparator_coupling_constant_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_energy_only_photon_bound_on_the_20_cubed_torus_2026_09_25.py
---

# Finite energy-curvature diagnostics on sixteen- and twenty-side tori

**Type:** bounded_theorem
**Status:** conditional moment identities and finite estimates; unaudited.

## Supplied setting and exact boundary

Use the linked ring-component note's supplied Hamiltonian, cyclic transverse modes and exact identities m1=2u s², m-1=chi/2 and m0=S. For the centered positive spectral measure with nonzero weight, log-convexity gives omega_min<=2s sqrt(u/chi) and S<=s sqrt(u chi). These refer to the lowest coupled excitation of the selected component. The real-field curvature extraction additionally needs the translation/momentum and field-reversal hypotheses stated in that parent; winding-preserving loop sampling alone does not prove them for the sampled mixture.

A finite-grid chi does not establish its small-momentum limit. Even a controlled asymptotic linear upper bound would require bounded u and a positive lower bound on chi, and would not exclude a softer mode with small spectral weight. No photon, velocity, phase, residual-structure-factor exclusion or quadratic-mode exclusion follows from these runs.

## Estimator and reproduction boundary

The runner uses960walkers, projection30, resampling interval0.02, two seeds per large torus and fields0.15/0.30. Reduced resampling interval does not establish removal of population bias or independent lineages. The quoted effective-sample-size formula is a heuristic, not a proved error bound. Shared E(0) correlates momenta; u errors, field truncation, guide, finite projection and component effects are not included in seed/bin errors. Comparison with interval0.05 also changes population and seeds, so it is not an isolated resampling-effect experiment.

The previous failed single-run control and later additional samples are part of the author's history, not proof that bias vanishes. The present fixed eight-run control is reproduced as specified; a statistical miss cannot by itself distinguish bias from noise. Tables below are author-run diagnostics, with fresh stdout serving as the reproduction record.

## Diagnostic 1 — the exact 2³ control at `dτ = 0.02`

On the exact 2³ component (864 states), eight independent runs per probe
field (400 walkers, 4000 generations each) give `−9.02489 ± 0.00252`,
`−9.22726 ± 0.00248` and `−9.86469 ± 0.00264` at `h = 0`, `0.15` and `0.30`,
against the exact `−9.026721`, `−9.227240` and `−9.869211` (`+0.7`, `−0.0`
and `+1.7` standard errors). The run-to-run scatter, `0.0070`–`0.0075`, is
about 15 per cent above the mean 10-bin error of a single run. A first
certifying run used one run per field with its 10-bin
error and missed at `h = 0.15` by 3.5 of those errors. Outside the runner,
24 independent runs per field at `dτ = 0.02` put the mean within 1.3
standard errors of exact diagonalization at `h = 0.15` and `0.30`: that additional experiment does not by itself separate bias from uncertainty in the error estimate. The
control now uses independent runs, and the 16³ and 20³ runs, which use the
same seeds, reproduce the first run's values to every printed digit.

## Diagnostic 2 — the susceptibility and the bounds

960 walkers, projection 30, probe fields 0.15 and 0.30, two seeds; `u` from
the plain energy of each torus; `s = 2 sin(k/2)`.

| torus | `k` | `χ̄` (seeds) | bound on `ω_min` | bound / `s` | bound on `S̄_T` | bound / `s` | `(1/(χ̄u))^{1/2}/(2π)` |
|---|---|---|---|---|---|---|---|
| 16³ | π/8 | 1.022 ± 0.059 | — | — | — | — | — |
| 20³ | π/10 | 0.990 ± 0.032 (1.016, 0.964) | 0.3361 | 1.074 | 0.1665 | 0.532 | 0.2991 |
| 20³ | π/5 | 1.096 ± 0.038 (1.134, 1.058) | 0.6311 | 1.021 | 0.3459 | 0.560 | 0.2843 |

`u` is `0.28671` on 16³ and `0.28579` on 20³. The projector costs 7.9 and
18.7 ms per walker and unit of imaginary time on 16³ and 20³.


## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring/comparator models and stated grid.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and comparator remain supplied.
- **N4:** actual linked parent scopes govern.
- **N5:** finite estimates and heuristic errors are not certified enclosures.
- **N6:** population/projection, component, small-field and limiting control remain open.
- **N7:** soft modes with weak weight and alternative components remain possible.
- **N8:** no physical identification, new premise or audit verdict.

## Actual inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24](GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25.md)
