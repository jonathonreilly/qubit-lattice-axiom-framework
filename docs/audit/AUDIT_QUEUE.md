# Audit Queue

**Total pending:** 2983
**Ready (all deps at retained-grade/metadata tiers or supplied axioms/approved primitives):** 611

By criticality:
- `critical`: 722
- `high`: 330
- `medium`: 762
- `leaf`: 1169

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 1729 | 25.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | bounded_theorem | non_terminal_conditional | critical | 1719 | 18.25 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | non_terminal_failed | critical | 1600 | 19.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 4 | `z2_hw1_mass_matrix_parametrization_note` | positive_theorem | non_terminal_failed | critical | 1448 | 20.00 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z2_hw1_mass_matrix_parametrization.py` |
| 5 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | positive_theorem | audit_in_progress | critical | 1443 | 14.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 6 | `hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25` | bounded_theorem | non_terminal_conditional | critical | 1369 | 11.92 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/hypercharge_alpha_third_normalization_runner.py` |
| 7 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1366 | 14.42 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 8 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | unaudited | critical | 1364 | 12.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 9 | `abj_p_comp_scale_free_singlet_completion_classification_note_2026-06-18` | bounded_theorem | unaudited | critical | 1357 | 10.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py` |
| 10 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | unaudited | critical | 1263 | 18.80 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 11 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | non_terminal_conditional | critical | 1257 | 15.30 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 12 | `plaquette_self_consistency_note` | bounded_theorem | audit_in_progress | critical | 1230 | 50.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py` |
| 13 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | positive_theorem | unaudited | critical | 1225 | 18.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 14 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | bounded_theorem | audit_in_progress | critical | 1210 | 15.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 15 | `s3_boundary_link_theorem_note` | bounded_theorem | unaudited | critical | 1192 | 14.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 16 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | bounded_theorem | audit_in_progress | critical | 1180 | 11.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 17 | `koide_circulant_character_bridge_narrow_theorem_note_2026-05-09` | positive_theorem | audit_in_progress | critical | 1178 | 25.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_character_bridge_narrow.py` |
| 18 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 1177 | 18.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 19 | `staggered_os0_supplied_action_ks_blocking_four_taste_module_narrow_theorem_note_2026-07-11` | bounded_theorem | non_terminal_conditional | critical | 1155 | 10.68 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py` |
| 20 | `physical_lattice_necessity_note` | no_go | unaudited | critical | 1144 | 22.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_lattice_necessity.py` |
| 21 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | non_terminal_conditional | critical | 1104 | 12.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 22 | `tensor_support_center_excess_law_note` | bounded_theorem | unaudited | critical | 1079 | 19.58 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_tensor_support_center_excess_law.py` |
| 23 | `rconn_derived_note` | no_go | unaudited | critical | 1020 | 25.00 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rconn_matching_rule_nogo_certificate.py` |
| 24 | `yt_color_projection_correction_note` | no_go | unaudited | critical | 1019 | 17.99 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 25 | `yt_ew_color_projection_theorem` | no_go | unaudited | critical | 960 | 32.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_kappa_family_nogo_certificate.py` |
| 26 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | positive_theorem | audit_in_progress | critical | 906 | 12.32 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 27 | `ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26` | bounded_theorem | non_terminal_conditional | critical | 901 | 22.32 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ew_higgs_gauge_mass_diagonalization.py` |
| 28 | `hierarchy_matsubara_decomposition_note` | positive_theorem | unaudited | critical | 899 | 15.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 29 | `wilson_small_a_matching_beta_gbare_narrow_theorem_note_2026-06-07` | bounded_theorem | non_terminal_conditional | critical | 887 | 13.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py` |
| 30 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | unaudited | critical | 880 | 10.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 31 | `cpt_exact_note` | positive_theorem | non_terminal_failed | critical | 875 | 31.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cpt_exact.py` |
| 32 | `dm_neutrino_weak_vector_theorem_note_2026-04-15` | bounded_theorem | unaudited | critical | 875 | 10.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_weak_vector_theorem.py` |
| 33 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | bounded_theorem | non_terminal_conditional | critical | 874 | 13.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py` |
| 34 | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | positive_theorem | unaudited | critical | 871 | 27.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py` |
| 35 | `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 856 | 22.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py` |
| 36 | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | open_gate | unaudited | critical | 853 | 14.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py` |
| 37 | `yt_ew_m_residual_note_2026-05-02` | no_go | unaudited | critical | 853 | 11.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_m_residual_channel_check.py` |
| 38 | `gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note` | positive_theorem | unaudited | critical | 852 | 24.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py` |
| 39 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem | unaudited | critical | 850 | 13.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py` |
| 40 | `gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_note_2026-06-07` | positive_theorem | unaudited | critical | 843 | 10.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_2026_06_07.py` |
| 41 | `gauge_vacuum_plaquette_constant_lift_obstruction_note` | positive_theorem | unaudited | critical | 840 | 14.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_constant_lift_obstruction.py` |
| 42 | `higgs_mechanism_note` | bounded_theorem | unaudited | critical | 835 | 12.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_higgs_quartic_mechanism_algebra_repair.py` |
| 43 | `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 831 | 30.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_q_two_thirds_algebraic_narrow.py` |
| 44 | `dm_neutrino_cascade_geometry_note_2026-04-14` | positive_theorem | unaudited | critical | 826 | 12.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 45 | `charged_lepton_two_higgs_canonical_reduction_note` | positive_theorem | non_terminal_conditional | critical | 813 | 16.67 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_charged_lepton_two_higgs_canonical_reduction.py` |
| 46 | `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | bounded_theorem | unaudited | critical | 806 | 26.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_z3_equivariant_anticommuting_no_go.py` |
| 47 | `gauge_vacuum_plaquette_perron_jacobi_underdetermination_note` | positive_theorem | unaudited | critical | 797 | 13.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py` |
| 48 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | bounded_theorem | unaudited | critical | 795 | 22.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 49 | `gauge_vacuum_plaquette_framework_point_underdetermination_note` | positive_theorem | unaudited | critical | 791 | 14.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_framework_point_underdetermination.py` |
| 50 | `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 790 | 15.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow.py` |

## Citation cycle break targets

93 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 759 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 2 | 745 | `bridge_gap_hk_cube_perron_note_2026-05-06` | critical | audited_conditional |
| 3 | `cycle-0003` | 3 | 745 | `bridge_gap_action_form_uniqueness_no_go_note_2026-05-06` | critical | unaudited |
| 4 | `cycle-0004` | 3 | 706 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 5 | `cycle-0005` | 5 | 706 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 6 | `cycle-0006` | 5 | 706 | `strong_cp_theta_bar_structured_admission_2026-06-04` | critical | unaudited |
| 7 | `cycle-0007` | 6 | 706 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 8 | `cycle-0008` | 6 | 706 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 9 | `cycle-0009` | 7 | 706 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 10 | `cycle-0010` | 7 | 706 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 11 | `cycle-0011` | 7 | 706 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 12 | `cycle-0012` | 8 | 706 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 13 | `cycle-0013` | 8 | 706 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 14 | `cycle-0014` | 8 | 706 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 15 | `cycle-0015` | 8 | 706 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 16 | `cycle-0016` | 9 | 706 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 17 | `cycle-0017` | 9 | 706 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 18 | `cycle-0018` | 9 | 706 | `a3_r2_review_confirms_exhaustion_note_2026-05-08_r2hr` | critical | unaudited |
| 19 | `cycle-0019` | 9 | 706 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 20 | `cycle-0020` | 9 | 706 | `a3_r4_review_confirmed_note_2026-05-08_r4hr` | critical | unaudited |
| 21 | `cycle-0021` | 11 | 706 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 22 | `cycle-0022` | 12 | 706 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 23 | `cycle-0023` | 13 | 706 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 24 | `cycle-0024` | 13 | 706 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 25 | `cycle-0025` | 13 | 706 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
