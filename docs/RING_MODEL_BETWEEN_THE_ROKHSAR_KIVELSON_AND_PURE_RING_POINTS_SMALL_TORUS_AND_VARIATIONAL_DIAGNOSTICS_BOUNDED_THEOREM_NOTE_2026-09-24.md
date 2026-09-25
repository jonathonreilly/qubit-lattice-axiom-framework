---
claim_id: ring_model_between_the_rokhsar_kivelson_and_pure_ring_points_small_torus_and_variational_diagnostics_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Finite flip spectra and a sampled variational family. Supplied finite-model
  identities and explicitly biased finite numerical diagnostics only; no phase, convergence
  certificate or new framework premise.
upstream_dependencies:
- dynamics_clause_the_covariant_plaquette_clause_annihilates_uniform_ice_exactly_at_the_rokhsar_kivelson_point_and_unrecorded_plaquettes_can_polarize_the_ice_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/ring_model_pure_ring_point_small_torus_and_variational_diagnostics_2026_09_24.py
---

# Finite flip spectra and a sampled variational family

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

Supply the finite cubic ice configuration space, plaquette adjacency A (including multiplicity), diagonal flippable count D, and H=V D-g A. At V=g>0, H is a graph Laplacian: its quadratic form is g/2 times the sum over directed edges of squared differences. Its kernel consists of vectors constant on each connected flip class. A uniform vector in one class is a ground state; arbitrary superpositions between classes are also ground states. This does not select a global uniform ensemble.

The runner enumerates the L=2 torus (9600 states, 937 classes, largest class 864), diagonalizes its components numerically, and samples the supplied positive trial amplitudes exp(alpha*N_flip). Its Rayleigh quotient is a variational upper bound in exact arithmetic on the chosen support. The reported alpha=0.14 is the minimum of a 101-point grid, not a proved continuous optimum. The larger-torus alpha=0.2 comparison is likewise a sampled-grid result, with Monte Carlo error and no mixing certificate. A finite family failing to improve an energy cannot rule out a phase or a different trial state.

The displayed plaquette statistic is the squared Fourier transform of n_p minus its **configuration-specific** mean, summed over plaquette orientations at their base vertices. Therefore q=0 is identically zero. It is not the ensemble-connected total-flippability variance. At nonzero reciprocal momenta the subtracted uniform term vanishes. Four momenta and three sizes do not establish absence of order or short-range correlations.

The directed first-repeat loop proposal admits reversal: keep the same nonrepeating tail, traverse the selected cycle in reverse after flipping it, and stop at the same repeated vertex. Tail and cycle interior are disjoint. Each vertex has three outgoing edges before and after, so the paired paths have the same probability. The Metropolis factor exp(2*alpha*Delta N_flip) therefore targets the squared trial amplitude on each reachable proposal component. Symmetry is not an irreducibility or finite-time equilibration proof.

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

- [DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9146, frozen head `51b884ccb663e487b5d8976b333c307832d3b1c7`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/ring_model_pure_ring_point_small_torus_and_variational_diagnostics_2026_09_24.py
```
