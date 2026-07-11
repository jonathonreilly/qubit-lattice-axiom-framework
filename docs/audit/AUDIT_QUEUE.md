# Audit Queue

**Total pending:** 2895
**Ready (all deps at retained-grade/metadata tiers or accepted premises: axiom/primitive nodes, owner-governed residual premises, and Tier-A admitted derivation targets):** 599

By criticality:
- `critical`: 672
- `high`: 332
- `medium`: 760
- `leaf`: 1131

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem | non_terminal_conditional | critical | 1685 | 18.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 2 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | non_terminal_failed | critical | 1555 | 19.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 3 | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 1341 | 24.89 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py` |
| 4 | `hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25` | bounded_theorem | non_terminal_conditional | critical | 1323 | 11.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/hypercharge_alpha_third_normalization_runner.py` |
| 5 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 1320 | 14.37 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 6 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | audit_in_progress | critical | 1318 | 12.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 7 | `abj_p_comp_scale_free_singlet_completion_classification_note_2026-06-18` | bounded_theorem | audit_in_progress | critical | 1315 | 11.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py` |
| 8 | `abj_p_rec_spintaste_clifford_core_bridge_note_2026-06-18` | bounded_theorem | audit_in_progress | critical | 1315 | 11.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_prec_spintaste_clifford_core_bridge_2026_06_18.py` |
| 9 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1236 | 18.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 10 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1230 | 15.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 11 | `s3_boundary_link_theorem_note` | bounded_theorem | non_terminal_conditional | critical | 1207 | 14.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 12 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | positive_theorem | unaudited | critical | 1174 | 18.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 13 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1157 | 15.68 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 14 | `oh_schur_boundary_action_note` | positive_theorem | unaudited | critical | 1147 | 19.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_oh_schur_boundary_action.py` |
| 15 | `koide_circulant_character_bridge_narrow_theorem_note_2026-05-09` | positive_theorem | unaudited | critical | 1108 | 25.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_character_bridge_narrow.py` |
| 16 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 1105 | 18.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 17 | `staggered_dirac_substep3_species_reduction_bridge_narrow_theorem_note_2026-05-16` | bounded_theorem | non_terminal_conditional | critical | 1091 | 13.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_species_reduction_bridge_2026_05_16.py` |
| 18 | `physical_lattice_necessity_note` | no_go | unaudited | critical | 1085 | 22.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_lattice_necessity.py` |
| 19 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | non_terminal_conditional | critical | 1053 | 12.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 20 | `rconn_derived_note` | no_go | audit_in_progress | critical | 965 | 25.92 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rconn_matching_rule_nogo_certificate.py` |
| 21 | `yt_color_projection_correction_note` | no_go | audit_in_progress | critical | 945 | 17.89 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 22 | `cl3_taste_generation_theorem` | bounded_theorem | audit_in_progress | critical | 898 | 20.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_taste_abstract_c8_orbit_scope_2026_06_12.py` |
| 23 | `yt_ew_color_projection_theorem` | no_go | audit_in_progress | critical | 887 | 33.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_kappa_family_nogo_certificate.py` |
| 24 | `hierarchy_matsubara_decomposition_note` | bounded_theorem | non_terminal_conditional | critical | 884 | 15.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 25 | `alpha_lm_geometric_mean_identity_theorem_note_2026-04-24` | positive_theorem | audit_in_progress | critical | 839 | 24.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_lm_geometric_mean_identity.py` |
| 26 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | positive_theorem | audit_in_progress | critical | 832 | 12.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 27 | `ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26` | bounded_theorem | audit_in_progress | critical | 826 | 22.19 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ew_higgs_gauge_mass_diagonalization.py` |
| 28 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | unaudited | critical | 806 | 10.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 29 | `dm_neutrino_weak_vector_theorem_note_2026-04-15` | bounded_theorem | unaudited | critical | 801 | 10.65 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_weak_vector_theorem.py` |
| 30 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | bounded_theorem | unaudited | critical | 800 | 13.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py` |
| 31 | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | open_gate | unaudited | critical | 778 | 14.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py` |
| 32 | `higgs_mechanism_note` | bounded_theorem | unaudited | critical | 760 | 12.57 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_higgs_quartic_mechanism_algebra_repair.py` |
| 33 | `dm_neutrino_cascade_geometry_note_2026-04-14` | positive_theorem | unaudited | critical | 750 | 12.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 34 | `charged_lepton_two_higgs_canonical_reduction_note` | positive_theorem | unaudited | critical | 737 | 16.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_charged_lepton_two_higgs_canonical_reduction.py` |
| 35 | `physical_hermitian_hamiltonian_and_sme_bridge_note_2026-04-30` | bounded_theorem | unaudited | critical | 729 | 12.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_hermitian_hamiltonian_and_sme_bridge.py` |
| 36 | `wilson_small_a_matching_beta_gbare_narrow_theorem_note_2026-06-07` | bounded_theorem | unaudited | critical | 710 | 13.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py` |
| 37 | `dm_neutrino_odd_circulant_z2_slot_theorem_note_2026-04-15` | positive_theorem | unaudited | critical | 709 | 11.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py` |
| 38 | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 705 | 17.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_three_generation_hw1_distinct_characters_exact.py` |
| 39 | `strong_cp_theta_zero_note` | bounded_theorem | unaudited | critical | 698 | 24.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_strong_cp_theta_zero.py` |
| 40 | `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 698 | 14.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow.py` |
| 41 | `dm_neutrino_z3_circulant_mass_basis_no_go_note_2026-04-15` | no_go | unaudited | critical | 697 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_z3_circulant_mass_basis_nogo.py` |
| 42 | `pmns_oriented_cycle_channel_value_law_note` | positive_theorem | unaudited | critical | 678 | 18.41 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_oriented_cycle_channel_value_law.py` |
| 43 | `pmns_graph_axis_to_active_lane_bridge_note` | bounded_theorem | unaudited | critical | 678 | 10.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_graph_axis_to_active_lane_bridge.py` |
| 44 | `pmns_oriented_cycle_selection_structure_note` | bounded_theorem | audit_in_progress | critical | 674 | 11.40 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_oriented_cycle_selection_structure.py` |
| 45 | `pmns_uniform_scalar_deformation_boundary_note` | positive_theorem | unaudited | critical | 671 | 12.39 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_uniform_scalar_deformation_boundary.py` |
| 46 | `pmns_twisted_flux_transfer_holonomy_boundary_note` | bounded_theorem | unaudited | critical | 671 | 10.39 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_twisted_flux_transfer_holonomy_boundary.py` |
| 47 | `pmns_hw1_source_transfer_boundary_note` | bounded_theorem | unaudited | critical | 669 | 11.89 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_hw1_source_transfer_boundary.py` |
| 48 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | bounded_theorem | unaudited | critical | 667 | 17.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 49 | `dm_leptogenesis_flavor_column_functional_theorem_note_2026-04-16` | bounded_theorem | unaudited | critical | 663 | 12.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py` |
| 50 | `dm_leptogenesis_pmns_analytic_stationary_classification_theorem_note_2026-04-16` | bounded_theorem | unaudited | critical | 643 | 10.33 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_pmns_he_parity_repair.py` |

## Citation cycle break targets

49 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 512 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 2 | 470 | `bridge_gap_hk_cube_perron_note_2026-05-06` | critical | unaudited |
| 3 | `cycle-0003` | 3 | 470 | `bridge_gap_action_form_uniqueness_no_go_note_2026-05-06` | critical | unaudited |
| 4 | `cycle-0004` | 3 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 5 | `cycle-0005` | 11 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 6 | `cycle-0006` | 12 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 7 | `cycle-0007` | 13 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 8 | `cycle-0008` | 13 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 9 | `cycle-0009` | 13 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 10 | `cycle-0010` | 13 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 11 | `cycle-0011` | 13 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 12 | `cycle-0012` | 13 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 13 | `cycle-0013` | 13 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 14 | `cycle-0014` | 14 | 424 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 14 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 16 | `cycle-0016` | 14 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 17 | `cycle-0017` | 14 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 18 | `cycle-0018` | 14 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 19 | `cycle-0019` | 15 | 424 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 20 | `cycle-0020` | 15 | 424 | `a3_route2_single_clock_c3_obstruction_note_2026-05-08_r2` | critical | unaudited |
| 21 | `cycle-0021` | 15 | 424 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 22 | `cycle-0022` | 15 | 424 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 23 | `cycle-0023` | 15 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 24 | `cycle-0024` | 15 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 25 | `cycle-0025` | 15 | 424 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
