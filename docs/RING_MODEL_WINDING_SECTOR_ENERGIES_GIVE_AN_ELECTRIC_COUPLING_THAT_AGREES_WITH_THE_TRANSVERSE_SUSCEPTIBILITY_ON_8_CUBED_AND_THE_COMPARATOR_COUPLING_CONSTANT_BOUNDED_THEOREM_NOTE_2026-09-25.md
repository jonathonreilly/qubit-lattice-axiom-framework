---
claim_id: ring_model_winding_sector_energies_give_an_electric_coupling_that_agrees_with_the_transverse_susceptibility_on_8_cubed_and_the_comparator_coupling_constant_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Exact uniform-flux, transverse-response and source-energy relations in a supplied positive Gaussian
  comparator. Finite selected-component projector estimates on4/6/8tori define diagnostic U_W and inverse susceptibility
  values. Shared-reference covariance, finite-field, finite projection, guide and population biases are uncontrolled;
  no coupling equality, convergence, phase or physical-field identification follows.
upstream_dependencies:
- minimal_axioms
- ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
- gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
- ring_model_static_test_charges_at_the_pure_ring_point_are_not_confined_on_the_small_tori_and_their_interaction_has_the_lattice_coulomb_shape_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_electric_coupling_from_winding_sector_energies_and_the_comparator_coupling_constant_2026_09_25.py
---

# Gaussian-comparator identities and finite winding-energy diagnostics

**Type:** bounded_theorem
**Status:** supplied comparator and finite estimates; unaudited.

## Scope

Supply the link-qubit ring Hamiltonian and conserved section fluxes W=(2q,0,0), with the string/loop initializations and projector settings in the runner. A winding sector can contain disconnected flip components; the side2 q=2 counterexample below shows the initializer can miss its sector ground state. Larger-torus connectivity and sampling are unproved. Energies below are estimates for the reached support, not certified unrestricted sector minima.

## Comparator identities

Separately supply noncompact Gaussian H=(U/2)sum E²+(K/2)sum(curl A)² with U,K>0, fixed uniform flux and unchanged transverse oscillator domain. Cauchy-Schwarz on each section and Gauss conservation give sum E²>=W²/L, attained by uniform E_x=W/L². Orthogonal harmonic/transverse decomposition leaves the same oscillator zero-point term, hence E(W)-E(0)=UW²/(2L). For W=2q this yields U_W=L[E(1)-E(0)]/2=U and the q=2 toq=1 difference ratio4. Completing a transverse oscillator square gives chi=1/U in the parent's normalization.

Minimizing the electric quadratic form subject to divergence charges gives source energy (U/2)rho^T Laplacian^+ rho. For charges +/-2 this is4U[G(0)-G(d)] on the torus with the zero mode removed. The -U/(pi d) tail belongs to the infinite-lattice long-distance comparison; it is not the exact finite-torus potential. With the separately supplied matching K=4u, c_G=sqrt(4uU) and alpha_G=sqrt(U/u)/(2pi). These statements do not identify the ring model or physical electromagnetism with this comparator.

## Diagnostic limitations

The tables record the author's finite settings and are compared with fresh stdout. Sector differences share E(0), so fitted coefficients and ratios are correlated; diagonal error propagation omits this covariance. The q²+q⁴ fit is an ansatz and the side4 fit has zero residual degrees of freedom. Susceptibility fields have truncation error; population, projection and component bias are uncontrolled. u uncertainty and correlations are omitted in the printed alpha_G errors. Agreement within these heuristic errors does not prove equality, convergence or a physical coupling.

## Diagnostic 1 — exact control on 2³

On the `2³` torus every ice state is enumerated. The sector `q = 0` has 880
states, of which the seed's flip component holds 864; the sector `q = 1`
has 464 states, all in one component. Loop moves that keep the flux,
started from the seed, sample each sector, and the projector started from
those samples gives `−9.03006 ± 0.00685` and `−7.40135 ± 0.00299` against the
exact sector ground energies `−9.026721` and `−7.399111`. The sector `q = 2`
is the control's caveat: its seed is a frozen one-state component, the
flux-preserving loop moves cannot leave it on this torus, and the sector's
ground `−5.656854` lies in its other 55 states. On the larger tori the loop
samples of each sector are not checked for this; their energies are those
of the part of the sector the samples reach.

## Diagnostic 2 — the sector energies

Energies in units of `g`; `u = −E(0)/N_p`.

| torus | `E(0)` | `E(1) − E(0)` | `E(2) − E(0)` | `E(3) − E(0)` | `U_W`, `q = 1` | `U_W`, fit `A q² + B q⁴` | `[E(2) − E(0)] / [E(1) − E(0)]` |
|---|---|---|---|---|---|---|---|
| 4³ (four seeds) | −56.2820 ± 0.0069 | 0.7315 ± 0.0084 | 2.1900 ± 0.0083 | — | 1.463 ± 0.017 | 1.586 ± 0.023 | 2.99 ± 0.04 |
| 6³ (six seeds) | −187.4349 ± 0.0145 | 0.3699 ± 0.0198 | 1.3671 ± 0.0179 | 2.9497 ± 0.0203 | 1.110 ± 0.059 | 1.067 ± 0.023 | 3.70 ± 0.20 |
| 8³ (eight seeds) | −443.3635 ± 0.0311 | 0.1685 ± 0.0443 | 0.9381 ± 0.0452 | 2.1575 ± 0.0433 | 0.674 ± 0.177 | 0.880 ± 0.077 | 5.57 ± 1.49 |

On 4³ the fit uses two sector differences for two parameters, so it has no
freedom left; the `A q² + B q⁴` form is an ansatz throughout.

## Diagnostic 3 — the two routes on the same tori

The transverse susceptibility is re-measured here at the smallest momentum
of each torus with the probe of open PR 9236 (480 walkers, four seeds).

| torus | `k` | `χ̄` | `1/χ̄` | `U_W`, `q = 1` | `U_W`, fit |
|---|---|---|---|---|---|
| 4³ | π/2 | 0.868 ± 0.025 | 1.152 ± 0.033 | 1.463 (+8.5 σ) | 1.586 (+10.9 σ) |
| 6³ | π/3 | 1.060 ± 0.013 | 0.944 ± 0.012 | 1.110 (+2.7 σ) | 1.067 (+4.7 σ) |
| 8³ | π/4 | 1.072 ± 0.014 | 0.933 ± 0.012 | 0.674 (−1.5 σ) | 0.880 (−0.7 σ) |

The susceptibilities agree with open PR 9236's (0.888, 1.071, 1.064).

## Diagnostic 4 — the comparator's dimensionless coupling

| torus | route | `U` | `c_G = (4uU)^{1/2}` | `α_G` |
|---|---|---|---|---|
| 4³ | `1/χ̄` | 1.152 | 1.162 | 0.3155 ± 0.0045 |
| 4³ | flux sectors | 1.586 | 1.364 | 0.3702 ± 0.0026 |
| 6³ | `1/χ̄` | 0.944 | 1.045 | 0.2875 ± 0.0018 |
| 6³ | flux sectors | 1.067 | 1.111 | 0.3057 ± 0.0033 |
| 8³ | `1/χ̄` | 0.933 | 1.038 | 0.2861 ± 0.0019 |
| 8³ | flux sectors | 0.880 | 1.008 | 0.2779 ± 0.0121 |
| 8³ | static pair through the core (open PR 9244) | 1.48 ± 0.20 | — | 0.360 |

`c_G` is the comparator's velocity with the matching rule `K = 4u`. Open PR
9236 bounded the lowest transverse excitation of the supplied model by
`c_G s(k)` with `U = 1/χ̄` on these tori. A physical velocity is not determined by an upper moment bound; no empirical coupling bound follows.


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
- [RING_MODEL_STATIC_TEST_CHARGES_AT_THE_PURE_RING_POINT_ARE_NOT_CONFINED_ON_THE_SMALL_TORI_AND_THEIR_INTERACTION_HAS_THE_LATTICE_COULOMB_SHAPE_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_STATIC_TEST_CHARGES_AT_THE_PURE_RING_POINT_ARE_NOT_CONFINED_ON_THE_SMALL_TORI_AND_THEIR_INTERACTION_HAS_THE_LATTICE_COULOMB_SHAPE_BOUNDED_THEOREM_NOTE_2026-09-25.md)
