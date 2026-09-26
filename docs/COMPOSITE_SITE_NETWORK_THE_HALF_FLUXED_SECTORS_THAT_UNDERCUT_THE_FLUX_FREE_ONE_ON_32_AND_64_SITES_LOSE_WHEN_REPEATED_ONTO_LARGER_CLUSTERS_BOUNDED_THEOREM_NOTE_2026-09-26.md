---
claim_id: composite_site_network_the_half_fluxed_sectors_that_undercut_the_flux_free_one_on_32_and_64_sites_lose_when_repeated_onto_larger_clusters_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: Supplied quadratic Majorana comparator with the parent parity-selection convention, isotropic
  bonds and finite periodic clusters. Exhaustive cotree assignments for fluxed32-site candidates, selected
  free-energy annealing minima, and periodic repetitions compared against eight chosen cut representatives.
  Numerical projected-comparator energies only; no proof of complete flux-free classification, lowest
  spin-Hamiltonian sector, global numerical minimum, thermodynamic persistence, band topology, phase or
  physical identification.
upstream_dependencies:
- minimal_axioms
- the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
- composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
- composite_site_network_spin_model_ground_state_is_locally_flux_free_on_the_clusters_searched_with_the_projection_exact_bounded_theorem_note_2026-09-25
- composite_site_network_flux_free_sector_lowest_pair_excitation_falls_as_one_over_l_to_4000_sites_and_the_odd_term_thins_the_low_levels_bounded_theorem_note_2026-09-25
- composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_small_cluster_flux_exceptions_repeated_onto_larger_clusters_2026_09_26.py
---

# Selected small-cluster flux patterns under periodic repetition

**Type:** bounded_theorem
**Status:** finite numerical search and repetition diagnostics for a supplied comparator; unaudited.

## Model and scope inherited from the reviewed parents

Use the explicitly supplied antisymmetric quadratic hopping matrix, with three identical Majorana copies, and the linked parent's parity-selection convention. The parent review found that equality to the named positive-J spin Hamiltonian is not established in this sign convention. Energies here are therefore projected **comparator** energies, not verified spin-model ground energies. The band-touching parent retains exact matrix algebra and finite searches; it does not certify a global two-to-six node count or continuum topological charges.

For a connected colored graph with even N, the parent supplies the gauge-stabilizer parity condition. In a nonsingular quadratic sector its lowest allowed energy is the free three-copy energy, with one lowest single-particle excitation added if the free vacuum has forbidden total parity. A zero mode changes the degeneracy; the runner treats levels below1e-9 as zero numerically. Floating Schur and eigenvalue calculations do not give a certified exact energy enclosure or exact zero-mode decision. Orthogonal-determinant and parity-modulus guards reject invalid numerical signs.

The comparison baseline is the minimum over **eight chosen cut representatives** obtained from u=+1 by sign reversals across periodic boundary cuts. Completeness as all locally flux-free gauge classes is not proved here. Calling this a baseline does not prove global sector selection.

## Finite results reproduced by the primary

- On the32-site (4,4,4) coordinate torus at kappa=0.3, the spanning tree has31 edges and the cotree17, giving2^17=131072 gauge-inequivalent assignments. The loop enumerates all assignments but evaluates energies only for assignments with a negative ten-loop flux. Its lowest such candidate is about-85.641, with16 of32 ten-loops negative, versus the eight-representative baseline about-84.817 (difference-0.824). It does not compute every possible locally flux-free assignment's energy.
- The selected32-site bond pattern, repeated onto64,128,256-site tori and minimized over its eight cut modifications, lies approximately0.587,2.894,5.508 above the respective baseline. This tests one selected small pattern and these repetitions; it does not exclude other patterns or boundary choices.
- On64 sites at kappa=0.45 and0.6, annealing in the **free** energy from six random starts and a baseline representative retains a configuration whose projected energy is approximately1.435 and1.248 below the baseline, respectively. Each has32 of64 ten-loops negative. The selected patterns' repetitions onto128 and256 sites lie1.824 and3.037 above at0.45, and3.216 and5.228 above at0.6.
- On128 and256 sites, annealing starts from a baseline representative, two random configurations and the carried64-site pattern. The four retained free-energy minima have projected energies no lower than the baseline at kappa=0.45 and0.6. The runner does **not** minimize projected energy over all visited configurations. A visited configuration with a higher free energy can have a lower projected energy because its parity penalty differs, so even this visited-set stronger claim is not established.

These are results of the seeded finite searches. They neither prove that all small-cluster exceptions disappear on larger tori nor establish the baseline as a true larger-cluster ground sector. The sign of the tested repetition costs and the existence of the small-cluster comparator exceptions are the retained outcomes.

## Repetition map and checks

All target coordinate periods are multiples of the smaller torus periods and preserve the network's site/color rules and bipartite orientation. A larger oriented bond inherits the smaller bond value obtained by reducing its infinite-network endpoints modulo the smaller periods, retaining the wrap vector. Each repeated pattern is compared under all eight chosen cut modifications. This is a specified map, not a search over all embeddings or all larger sectors.

The primary keeps the full131072 assignment loop, all submitted starts,4000 annealing steps on64 sites,6000 on128 and4000 on256. It reports three finite checks. Independent controls verify periodic bond coverage, gauge equivariance of repetition and the matrix, projected-energy gauge invariance, connected-tree size and cut preservation of the enumerated local fluxes. The parent's independent Clifford/parity check and unresolved spin-map sign limitation remain in force.

## Boundary

No complete flux-free-class theorem, exhaustive projected-energy search on large clusters, controlled thermodynamic trend, ground-sector phase, certified band topology, physical identification or audit verdict. Annealing outcomes are finite candidate comparisons; fixed seeds aid reproducibility but do not certify completeness. Historical filenames and the submitted phrase “physical energy” do not broaden this scope.

## Inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24](COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25](COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [COMPOSITE_SITE_NETWORK_FLUX_FREE_SECTOR_LOWEST_PAIR_EXCITATION_FALLS_AS_ONE_OVER_L_TO_4000_SITES_AND_THE_ODD_TERM_THINS_THE_LOW_LEVELS_BOUNDED_THEOREM_NOTE_2026-09-25](COMPOSITE_SITE_NETWORK_FLUX_FREE_SECTOR_LOWEST_PAIR_EXCITATION_FALLS_AS_ONE_OVER_L_TO_4000_SITES_AND_THE_ODD_TERM_THINS_THE_LOW_LEVELS_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26](COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md)
