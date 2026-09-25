---
claim_id: ring_model_two_regulators_a_region_bounded_by_records_matches_the_torus_at_size_eight_and_the_walker_population_is_the_larger_regulator_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Compressed boundary identities and finite regulator diagnostics. Supplied
  finite-model identities and explicitly biased finite numerical diagnostics only;
  no phase, convergence certificate or new framework premise.
upstream_dependencies:
- ring_model_projector_monte_carlo_at_the_pure_ring_point_energies_below_variational_and_no_growth_of_plaquette_order_bounded_theorem_note_2026-09-24
- ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
- ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/ring_model_two_regulators_a_region_bounded_by_records_against_the_torus_and_the_walker_population_2026_09_25.py
---

# Compressed boundary identities and finite regulator diagnostics

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

Supply the link-qubit ice model, sigma-z projectors for fixed external links, the Gauss constraint and ring operators. A ring that flips a recorded link has P U_p P=P U_p† P=0. Hence the **compressed Hamiltonian PHP** contains only plaquettes whose links are unrecorded. This is a supplied restriction (or ideal projection model), not a deduction that finite-time autonomous evolution e^(-itH) never leaves P. In general P H(1-P) is nonzero and P e^(-itH)P differs from e^(-itPHP). The Record axiom alone does not choose these projectors or this dynamics.

For an interior slab, sum Gauss over its vertices: internal edges cancel. The interior plane-section flux equals minus the signed flux through the other boundary links, which are fixed. Thus each section flux is fixed by the supplied boundary values. This removes freely variable periodic winding fluxes in the box, but does not prove its configurations form one flip component or exclude other conserved labels.

The runner enumerates one 3646-state flip component in a 3³ interior, checks all its sections, and numerically diagonalizes its Hamiltonian. The reference ground state is of that component only. Residual and positive-eigenvector checks support the numerical result, not a rigorous enclosure. The finite projector comparison tests the stated observables for one frame and seed.

Two sampled boundary frames and two sizes do not establish boundary independence. Agreement within estimated errors is not an equivalence test or proof that the interior forgets its records. Box correlations subtract products of estimated local means; this plug-in connected estimator has finite-sample bias. The torus runner reports raw translation-averaged correlations: interpreting them as connected requires an ensemble with vanishing local means, not merely zero total winding in an arbitrary flip component. This assumption and the different estimands must be kept explicit in comparisons.

The walker-number scan is finite. Fits linear in 1/n_w are an extrapolation ansatz and do not establish the infinite-population limit or attribute every size drift to bias. A genuine finite-system energy density can vary with size. exp[-(dt*std E_L)²] is a static-guide, lognormal approximation to relative effective sample size, not an identity for the integrated branching weights. The observed size ratios do not prove a square-root scaling theorem.

Historical seven-run collections mix populations and other settings and are not iid repetitions at a common target distribution. Their scatter can combine stochastic error and bias; it neither calibrates a universal error multiplier nor proves monotonic ground-state size dependence. Those auxiliary averages are not recomputed by this runner. Fresh evidence consists of the component identities/control, stated scan, sampled boundary comparison and depth diagnostics; all retain population, lag, initialization and correlation uncertainty. No regulator-independent bulk limit, photon or phase is claimed.

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

- [RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9220, frozen head `3b655b7c876b67e354c61bbfb0ddee04bdd5f691`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/ring_model_two_regulators_a_region_bounded_by_records_against_the_torus_and_the_walker_population_2026_09_25.py
```
