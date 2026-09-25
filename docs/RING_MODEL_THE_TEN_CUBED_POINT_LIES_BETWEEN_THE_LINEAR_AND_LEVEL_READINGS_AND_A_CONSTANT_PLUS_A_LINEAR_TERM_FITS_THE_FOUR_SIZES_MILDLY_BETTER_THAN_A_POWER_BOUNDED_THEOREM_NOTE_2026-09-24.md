---
claim_id: ring_model_the_ten_cubed_point_lies_between_the_linear_and_level_readings_and_a_constant_plus_a_linear_term_fits_the_four_sizes_mildly_better_than_a_power_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Ten-cubed estimator and descriptive four-size fits. Supplied finite-model
  identities and explicitly biased finite numerical diagnostics only; no phase, convergence
  certificate or new framework premise.
upstream_dependencies:
- ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
- gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/ring_model_pure_structure_factor_on_the_ten_cubed_torus_and_the_four_size_series_at_the_smallest_momentum_2026_09_24.py
---

# Ten-cubed estimator and descriptive four-size fits

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

The runner supplies the same ring model and zero-winding guide as the previous finite projector diagnostics. It executes one L=10 run with 100 walkers, finite projection, and forward lags 0,1,2,4,6. Its transverse structure factors, mixed energy and time correlations are finite estimator outputs. A plateau within noisy, correlated lag estimates does not exclude lag bias, population bias or insufficient initial projection.

Similar effective rates on three windows do not imply one excitation or determine the lowest coupled gap. The positive spectral-measure inequalities belong to the exact ground-state correlation, not arbitrary noisy estimates. Plugging finite energy and S into the conditional f-sum quotient does not give a certified numerical upper bound. Rate error propagation ignores covariance; quotient error propagation omits energy uncertainty.

The four-size fit combines the fresh L=10 result with **stored historical** L=4,6,8 values from the earlier run. The power fit minimizes weighted log residuals; its printed original-scale residual sum is a descriptive statistic, not the objective minimized. The constant-plus-linear fit minimizes original-scale weighted residuals. Their formal errors assume supplied independent weights that have not been calibrated, and a small difference of residual sums does not establish model preference.

The comparison labelled linear in historical code means an affine-in-|s| fit, not a pure linear photon dispersion. A constant term persisting at low k changes the f-sum quotient to quadratic; conversely an approximately linear static structure factor is not by itself proof of a photon. Historical auxiliary 12³/16³ runs and averages are not reproduced or certified by this runner and are excluded from the retained quantitative claims. Different-population run scatter in the later regulator note motivates uncertainty controls; it does not justify a universal factor-two error correction. Larger-torus convergence, a gap and a phase remain unresolved.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the explicit supplied finite models, supports, boundaries and estimator settings above.
- **N2 — Independence:** primary reproduction is not independent verification; the combined review receipt records separate structural controls.
- **N3 — Imports:** link qubits, Gauss law, ring Hamiltonian, initial ensembles, projection and Gaussian comparators are supplied, not adopted framework premises.
- **N4 — Dependencies:** corrected parent scopes govern; filenames are historical identifiers, not stronger claims.
- **N5 — Resolution:** floating-point eigensystems and finite Monte Carlo are observations, not certified enclosures or limit theorems. Bin errors lack proved coverage or mixing bounds.
- **N6 — Deferred:** component connectivity, population/lag/projection convergence and infinite-volume physics require additional science.
- **N7 — Counterroutes:** alternative sectors, non-Gaussian states, finite-size effects and correlated estimator error remain available.
- **N8 — Boundary:** ordinary source review only; no audit verdict, retained grade or assembly decision.

## Falsifiers and verification

A counterexample satisfying the exact hypotheses refutes the corresponding identity. Failed numerical controls must be investigated and not relabelled as a new phase. The runner's numerical thresholds describe only its finite experiment. Successful fresh execution has exit zero and FAIL=0; its cache binds this source and its declared inputs.

## Inputs

- [RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24](GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9171, frozen head `07a595e9a1d789dbb1c8a29b571566bb48cf92f8`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/ring_model_pure_structure_factor_on_the_ten_cubed_torus_and_the_four_size_series_at_the_smallest_momentum_2026_09_24.py
```
