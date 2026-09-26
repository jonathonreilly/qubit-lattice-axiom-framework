---
claim_id: round_five_synthesis_one_exact_identity_per_block_of_the_third_campaign_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: 'Five finite floating-point controls for supplied projected quadratic comparators and ring components:
  selected8-site spectral agreement, singular-value bound, section-flux conservation, and cyclic f-sums with finite-difference
  checks. Projection is not a proved spin operator map; no class completeness, thermodynamic spectrum, physical
  field or guide-independent trend follows.'
upstream_dependencies:
- minimal_axioms
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
- composite_site_network_spin_model_ground_state_is_locally_flux_free_on_the_clusters_searched_with_the_projection_exact_bounded_theorem_note_2026-09-25
- ring_model_winding_sector_energies_give_an_electric_coupling_that_agrees_with_the_transverse_susceptibility_on_8_cubed_and_the_comparator_coupling_constant_bounded_theorem_note_2026-09-25
- ring_model_with_single_link_charge_hopping_changes_rapidly_between_weak_and_strong_hopping_and_its_moment_bound_stays_finite_at_small_momentum_bounded_theorem_note_2026-09-25
- composite_site_network_flux_free_sector_lowest_pair_excitation_falls_as_one_over_l_to_4000_sites_and_the_odd_term_thins_the_low_levels_bounded_theorem_note_2026-09-25
- ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
- ring_model_single_link_charge_hopping_link_expectation_from_fixed_guide_grids_depends_on_the_guide_penalty_on_6_cubed_bounded_theorem_note_2026-09-26
runner: scripts/round_five_synthesis_one_exact_identity_per_block_of_the_third_campaign_2026_09_25.py
---

# Finite controls across projected-comparator and ring-model blocks

**Type:** bounded_theorem
**Status:** supplied-model identities with floating-point controls; unaudited.

## Scope and proof boundaries

All model clauses, networks, representations and matching rules are supplied. The linked parents define the actual inputs. The runner recomputes five small controls with shared code ancestry; it does not independently certify its parents or reproduce their large numerical grids. Draft work is excluded from the landing and from the evidence here.

For the connected supplied six-Majorana comparator, local projection has squared norm2^(1-N) when the global constraint product is+1 and zero otherwise, using orthogonality of distinct bond-sign sectors. When a nonzero unprojected gap exists, opposite parity costs the smallest one-flavour level; zero modes require separate degeneracy handling. Small-cluster spectral agreement is not a spin-to-Majorana operator map: the parent sign convention has an unresolved mapping discrepancy identified by an independent Clifford control. The numerical comparator remains a supplied object.

At kappa=0, the z matching has every singular value5 and the x,y parts have norm2, so sigma_min(A)>=5-2-2=1 for any such sign assignment. This bounds absolute eigenvalues of iA, not all signed levels. Eight chosen cut-twisted representatives are tested; completeness of local-flux-free gauge classes is not proved. A fixed-sign-sector two-flavour excitation costs2 epsilon_min when the ground has the allowed parity; this is not a proof of the full spin gap across sectors.

Ice divergence telescopes to equal section fluxes, and a plaquette preserves them. These facts do not make every winding sector a connected flip component. For the chosen real ring ground, the cyclic averaged commutator gives m1=2u s² at g=1. Adding link flips contributes(2t/(3N))sum_l <sigma_x_l> over the active links, since the diagonal charge term commutes with the probe. Centered ground spectral measures and the parent curvature hypotheses govern moment bounds. Hellmann-Feynman finite differences approximate expectation values with a truncation remainder; the reported1percent comparison is a finite control.

## Recomputed controls

These are the author's tabulated values; fresh stdout is the reproduction record. Diagonalization and determinant/SVD calculations are floating-point, not exact arithmetic certificates.

| block | identity recomputed here | value |
|---|---|---|
| open PR 9255 | the projection rule's lowest projected-comparator energy over the 32 sectors of the 8-site cluster equals the exact ground energy of the 16-qubit spin model | `−35.66888833` at `J = (1, 1, 2.5)`, `−23.61311995` at `(0.4, 1, 1.6)`; differences `1.4 × 10⁻¹⁴`, `9.9 × 10⁻¹⁴` |
| open PR 9264 | at `J_z = 2.5`, `κ = 0` on 256 sites the z-bond part has every singular value 5 and the x- and y-bond parts norm 2, so each singular value in the eight chosen cut-twisted representatives is at least1 | singular values `5.000000000000`; norms `2.000000000000`; lowest level `1.000000000000` |
| open PR 9258 | on 2³ the section flux is the same through every plane for each of the 9600 ice states and is conserved by all 49920 plaquette flips | exact sector grounds `−9.026721` (880 states) and `−7.399111` (464 states); comparator reading `L [E(1) − E(0)] / 2 = 1.62761` |
| open PR 9265 (bound of open PR 9236) | the cyclic-triple first moment on the exact 2³ component equals `2 u s²` for the chosen real ground state (no spatial symmetry required for the averaged commutator) | `3.008906971` for both, each mode `3.008907` |
| PR9263 (supplied six-link control) | with the single-link term on the six links at one vertex of 2³ (184320 states), the averaged first moment equals `2 u s² + (2t/3N) Σ ⟨σ^x⟩`; central differences of the energy estimate `Σ ⟨σ^x⟩` | `3.053953358` at `(t, M) = (0.8, 1.5)` and `3.023601331` at `(0.4, 2)`, differences below `10⁻¹⁴`; `Σ ⟨σ^x⟩ = 0.918975` at `t = 0.4` against `0.919318` and `0.920343` from steps `0.05` and `0.1` |


## Limits of the larger diagnostics

The Gaussian winding and susceptibility routes are conditional comparator identities. Their ring-model estimates have correlated reference energies, guide/population/projection bias and unproved component coverage. Neither approximate agreement nor finite chi establishes a limiting coupling, dispersion or phase. A bound with a momentum-independent numerator also needs control of chi to have a finite limit.

Fixed-guide hopping grids retain t-dependent estimator bias. Guide sensitivity prevents interpreting the reported rapid changes or size differences as ground-state trends. No unreviewed draft result is used to fill this gap. Network searches at large sizes inspect chosen minima and sampled bond flips, not every flux sector; pooled low-level counts across representatives are not one physical density of states. Finite1/L trends and heuristic errors do not establish an asymptotic nodal geometry.

Open work is population/projection and component control, a verified operator/sign map, gauge-class completeness and broader sector comparisons. No new premise, physical-field identification or audit status is supplied.

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
- [COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25](COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_WITH_SINGLE_LINK_CHARGE_HOPPING_CHANGES_RAPIDLY_BETWEEN_WEAK_AND_STRONG_HOPPING_AND_ITS_MOMENT_BOUND_STAYS_FINITE_AT_SMALL_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_WITH_SINGLE_LINK_CHARGE_HOPPING_CHANGES_RAPIDLY_BETWEEN_WEAK_AND_STRONG_HOPPING_AND_ITS_MOMENT_BOUND_STAYS_FINITE_AT_SMALL_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [COMPOSITE_SITE_NETWORK_FLUX_FREE_SECTOR_LOWEST_PAIR_EXCITATION_FALLS_AS_ONE_OVER_L_TO_4000_SITES_AND_THE_ODD_TERM_THINS_THE_LOW_LEVELS_BOUNDED_THEOREM_NOTE_2026-09-25](COMPOSITE_SITE_NETWORK_FLUX_FREE_SECTOR_LOWEST_PAIR_EXCITATION_FALLS_AS_ONE_OVER_L_TO_4000_SITES_AND_THE_ODD_TERM_THINS_THE_LOW_LEVELS_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_SINGLE_LINK_CHARGE_HOPPING_LINK_EXPECTATION_FROM_FIXED_GUIDE_GRIDS_DEPENDS_ON_THE_GUIDE_PENALTY_ON_6_CUBED_BOUNDED_THEOREM_NOTE_2026-09-26](RING_MODEL_SINGLE_LINK_CHARGE_HOPPING_LINK_EXPECTATION_FROM_FIXED_GUIDE_GRIDS_DEPENDS_ON_THE_GUIDE_PENALTY_ON_6_CUBED_BOUNDED_THEOREM_NOTE_2026-09-26.md)
