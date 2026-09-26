---
claim_id: round_four_synthesis_the_pure_ring_photon_from_energies_alone_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Finite floating-point recomputation of conditional moment, Hellmann-Feynman, charge-conservation and
  RK graph-Laplacian identities in supplied ring components. Summarizes corrected parent limitations. No excitation
  dispersion, soft-mode exclusion, confinement exclusion, physical photon or regulator equivalence is established.
upstream_dependencies:
- minimal_axioms
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
- ring_model_energy_only_photon_bounds_soften_from_the_pure_ring_point_to_the_rk_point_and_meet_uniform_ice_there_bounded_theorem_note_2026-09-25
- ring_model_static_test_charges_at_the_pure_ring_point_are_not_confined_on_the_small_tori_and_their_interaction_has_the_lattice_coulomb_shape_bounded_theorem_note_2026-09-25
- ring_model_in_a_region_bounded_by_records_the_energy_only_photon_bound_matches_the_torus_and_the_records_reduce_only_the_response_amplitude_bounded_theorem_note_2026-09-25
runner: scripts/round_four_synthesis_the_pure_ring_photon_from_energies_alone_2026_09_25.py
---

# Ring-component identities and limits of energy-only diagnostics

**Type:** bounded_theorem
**Status:** finite floating-point controls of supplied-model identities; unaudited.

## Actual scope

The four linked parents supply finite ring components, an RK potential, static divergence charges and regions with fixed records. Their Hamiltonians, boundary conditions, guides and Gaussian comparisons remain model inputs. This synthesis repeats small controls; it does not certify their large-system projector errors or promote their claims. Shared implementation ancestry means this runner is not an independent review of its parents.

For a centered positive spectral measure of an isolated ground branch with nonzero coupled weight, moments obey omega_min<=m0/m-1<=sqrt(m1/m-1)<=m1/m0 and m0²<=m1 m-1. The cyclic complex-mode ring identity at g=1 is m1=2u s². Relating real-field curvature to m-1=chi/2 requires the parent's momentum/symmetry conditions and a controlled h->0 limit.

Hellmann-Feynman dE/dV=<N_flip> holds on differentiable branches. At V=g>=0 each component Hamiltonian is a positive graph Laplacian, so its constant vector has zero energy, including charged components. Each plaquette conserves vertex divergence. For a diagonal standing-wave W, m1=<[W,[H,W]]>/2; its per-plaquette squared change c_p gives m1=-(dE/d epsilon)/2 when the ring coefficient is1+epsilon c_p. Finite differences retain O(epsilon²) error under smoothness.

## Recomputed controls

The table is the author's historical result; fresh stdout supplies current reproduction. The revised first control diagonalizes the entire864-state matrix instead of searching only40levels, and checks its residual/orthogonality and the response solve. Numerical nonzero-weight thresholds do not prove exact selection rules.

| Block | Identity recomputed | Result |
|---|---|---|
| 9236 | cyclic-triple f-sum average `= 2us²`; moment chain on the exact 2³ component | 3.008907 both sides; 2.5173 ≤ 2.7754 ≤ 2.8724 ≤ 2.9728 |
| 9239 | `∂E_0/∂V = ⟨N_flip⟩` at `V/g = 0.5`; zero RK ground energy | 9.006137 both sides; −2.3·10⁻¹⁵ |
| 9244 | a charge pair's component keeps its charges; zero RK ground energy | 508 states, charges `−2, 0, 2`; 1.6·10⁻¹⁵ |
| 9247 | Hellmann–Feynman first moment `=` double commutator in a region bounded by records | 3646 states; 1.424504 both |
| — | the register | nine entries |


## What the parent evidence supports

Finite energy estimates produce estimated upper moment bounds, not measured excitation frequencies. Positive lower control of chi and bounded u would be needed for a limiting linear upper bound; even then a softer weak-weight mode is allowed. The finite-field fits, shared-reference covariance, population/projection bias and disconnected components remain uncontrolled.

Static-pair energy fits on small tori do not exclude a positive asymptotic string tension or establish a Coulomb phase. Gaussian charge energy is relative to the zero-source minimum. Region/torus agreement of estimated upper bounds does not prove equal frequencies or an amplitude-only boundary effect; the region modes used in the parent are not the fundamental modes, and out-of-range torus interpolation is clamped.

Useful follow-up is estimator/component control, field extrapolation and stronger spectral information. No physical photon, phase, gaplessness, confinement verdict or regulator independence follows here.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite models and stated controls.
- **N2:** shared-code checks are not independent review.
- **N3:** no model clause or representation is adopted.
- **N4:** actual linked parent scopes govern.
- **N5:** floating-point controls and heuristic large-grid errors.
- **N6:** explicit open obligations above.
- **N7:** alternate sectors, weak spectral weight and estimator biases remain possible.
- **N8:** no retained grade or audit verdict.

## Actual inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_ENERGY_ONLY_PHOTON_BOUNDS_SOFTEN_FROM_THE_PURE_RING_POINT_TO_THE_RK_POINT_AND_MEET_UNIFORM_ICE_THERE_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUNDS_SOFTEN_FROM_THE_PURE_RING_POINT_TO_THE_RK_POINT_AND_MEET_UNIFORM_ICE_THERE_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_STATIC_TEST_CHARGES_AT_THE_PURE_RING_POINT_ARE_NOT_CONFINED_ON_THE_SMALL_TORI_AND_THEIR_INTERACTION_HAS_THE_LATTICE_COULOMB_SHAPE_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_STATIC_TEST_CHARGES_AT_THE_PURE_RING_POINT_ARE_NOT_CONFINED_ON_THE_SMALL_TORI_AND_THEIR_INTERACTION_HAS_THE_LATTICE_COULOMB_SHAPE_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_IN_A_REGION_BOUNDED_BY_RECORDS_THE_ENERGY_ONLY_PHOTON_BOUND_MATCHES_THE_TORUS_AND_THE_RECORDS_REDUCE_ONLY_THE_RESPONSE_AMPLITUDE_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_IN_A_REGION_BOUNDED_BY_RECORDS_THE_ENERGY_ONLY_PHOTON_BOUND_MATCHES_THE_TORUS_AND_THE_RECORDS_REDUCE_ONLY_THE_RESPONSE_AMPLITUDE_BOUNDED_THEOREM_NOTE_2026-09-25.md)
