---
claim_id: ring_model_energy_only_photon_bounds_soften_from_the_pure_ring_point_to_the_rk_point_and_meet_uniform_ice_there_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Supplied finite ring model H=-sum R+V sum n. Differentiable selected-component ground energies give
  u=-(E-V Eprime)/Np. The diagonal potential leaves the centered real-ground cyclic f-sum unchanged. At V=1 uniform
  component ground states satisfy the positive-measure susceptibility floor. The six-point L=8 finite-population
  sweep and loop samples are biased diagnostics, not exact spectral bounds, continuous trends, saturation, dispersion,
  velocity or phase determinations.
upstream_dependencies:
- minimal_axioms
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
- ring_model_from_the_rk_point_to_the_pure_ring_point_the_transverse_weight_moves_to_the_zone_corner_continuously_bounded_theorem_note_2026-09-24
- ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_energy_only_photon_bounds_from_the_pure_ring_point_to_the_rk_point_2026_09_25.py
---

# Finite energy-curvature sweep and conditional RK susceptibility floor

**Type:** bounded_theorem
**Status:** exact conditional identities and finite numerical diagnostics; unaudited.

## Theorem — energy derivative and positive spectral moments

Supply link-qubit ice and `H(V)=-sum_p R_p+V sum_p n_p`, g=1, on a finite torus. On a selected connected flip component the real ground vector is unique. Where its normalized ground eigenpair is differentiable, differentiating `H psi=E psi` and pairing with psi gives `Eprime=<sum n_p>`. Thus `u=<sum R_p>/Np=-(E-V Eprime)/Np`. A finite difference of estimated energies is not this exact derivative.

Use the cyclic triple, centered modes and positive excited-state measure of the companion energy-bound note. The diagonal V term commutes with the diagonal modes. The triple averaged first moment therefore remains `m1=2u s²`, s²=2-2cos k, without requiring cubic rotational symmetry of the real ground vector. With `S=m0`, `chi=2m_(-1)` and nonzero spectral weight, the positive-measure inequality `m0²<=m1 m_(-1)` gives `S<=s sqrt(u chi)` and `omega_min<=2s sqrt(u/chi)`. These are upper bounds on the mode-coupled gap, not measured dispersion or speed.

At V=1 each plaquette contributes the positive matrix [[1,-1],[-1,1]] on its active pair. The kernel is constant within each connected flip component. For that normalized uniform vector, `u=n_f`; consequently `chi>=S²/(n_f s²)`. Center modes against the entire ground space if more than one component is present. Frozen zero-weight components and zero modes do not satisfy divisions by positive spectral weight. Equality in the moment inequality requires spectral concentration; closeness of biased estimates does not establish it.

## Numerical experiment

The primary runner retains the full original six-point sweep V=0,0.25,0.5,0.75,0.9,1 on L=8, modes pi/4 and pi/2, three seeds, 480 walkers and projection 30. It uses field pairs h,2h with h=0.15,0.06,0.02 in the stated V ranges, the guide exp[0.2(1-V)N_flip+hF/2], and a backward V step 0.03. It separately samples 2000 loop sweeps at V=1. Fresh stdout is the executed numerical result; original tables remain recoverable from PR #9239.

The energy fit assumes the companion note's translation, momentum-sector and F-to-minus-F symmetry conditions. Loop initialization preserves winding, not a proved single flip component. Loop and projector ensembles can weight components differently, so their agreement is a diagnostic rather than an exact common-state comparison. Uniform stationary weights at V=1 do not prove finite equilibration. Zero local energy at V=1,h=0 is an exact generator identity for the uniform guide, even away from stationarity; it does not certify susceptibility accuracy.

The backward difference has step bias, and for an exact differentiable concave component ground energy it lies above the endpoint derivative. Hence for V>0 it biases the derived u upward before sampling errors are considered. At V=0 the negative-V auxiliary energy is only a derivative diagnostic. Finite population, projection, guide, component and field-fit biases remain uncontrolled. Shared zero-field energies and common samples correlate momenta and u; quoted errors omit u uncertainty, finite differences and those systematic errors. Nominal three-error tolerances and relative errors do not have proved coverage.

The finite grid does not prove continuous or monotone behavior between sampled values. Fitting an exponent to estimated upper bounds does not determine a photon speed, quadratic dispersion or a vanishing velocity. A two-momentum ansatz cannot remove that logical gap. The RK energy and uniform component ground state are exact, but a quadratic dynamical mode has not been established by this note. Six-mode historical comparisons require additional cubic symmetry to identify them with the cyclic triple.

## No-Go Discipline Gate

- **N1:** finite supplied components, differentiable ground branch, centered nonzero spectral measure and explicit response symmetries.
- **N2:** independent exact controls are separate from primary stochastic reproduction.
- **N3:** ring, potential, sampling and probes are supplied.
- **N4:** current narrowed parent scopes control.
- **N5:** finite simulations and nominal errors are not rigorous enclosures or hypothesis exclusions.
- **N6:** component, population, projection, field-size and derivative-step limits remain open.
- **N7:** low-weight soft modes, multiple components, spectral mixtures and finite-size bias remain possible.
- **N8:** retain conditional identities and the finite grid; no new physical selection, phase or audit verdict.

## Verification

Run the primary script without --dry for the full grid. Original source, tables and cache are frozen at PR #9239 head d8e4a65264dcb826b5655933cd830cd93cb29daa. Historical titles do not enlarge this note's scope.

## Inputs

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_FROM_THE_RK_POINT_TO_THE_PURE_RING_POINT_THE_TRANSVERSE_WEIGHT_MOVES_TO_THE_ZONE_CORNER_CONTINUOUSLY_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_FROM_THE_RK_POINT_TO_THE_PURE_RING_POINT_THE_TRANSVERSE_WEIGHT_MOVES_TO_THE_ZONE_CORNER_CONTINUOUSLY_BOUNDED_THEOREM_NOTE_2026-09-24.md)
