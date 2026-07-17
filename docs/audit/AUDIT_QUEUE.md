# Audit Queue

**Total pending:** 2990
**Ready (all deps at retained-grade/metadata tiers or supplied axioms/approved primitives):** 616

By criticality:
- `critical`: 680
- `high`: 352
- `medium`: 776
- `leaf`: 1182

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 1712 | 25.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 1702 | 18.23 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 1573 | 19.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 4 | `z2_hw1_mass_matrix_parametrization_note` | positive_theorem | audit_in_progress | critical | 1415 | 20.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z2_hw1_mass_matrix_parametrization.py` |
| 5 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | positive_theorem | audit_in_progress | critical | 1410 | 14.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 6 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1339 | 14.39 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 7 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | unaudited | critical | 1335 | 12.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 8 | `abj_p_comp_scale_free_singlet_completion_classification_note_2026-06-18` | bounded_theorem | unaudited | critical | 1330 | 10.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py` |
| 9 | `abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18` | bounded_theorem | non_terminal_conditional | critical | 1330 | 10.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py` |
| 10 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | unaudited | critical | 1229 | 18.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 11 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1223 | 15.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 12 | `plaquette_self_consistency_note` | bounded_theorem | audit_in_progress | critical | 1194 | 49.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py` |
| 13 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | bounded_theorem | audit_in_progress | critical | 1191 | 15.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 14 | `s3_boundary_link_theorem_note` | bounded_theorem | unaudited | critical | 1158 | 14.18 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 15 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | bounded_theorem | audit_in_progress | critical | 1146 | 11.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 16 | `koide_circulant_character_bridge_narrow_theorem_note_2026-05-09` | positive_theorem | audit_in_progress | critical | 1144 | 25.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_character_bridge_narrow.py` |
| 17 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 1143 | 18.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 18 | `staggered_os0_supplied_action_ks_blocking_four_taste_module_narrow_theorem_note_2026-07-11` | bounded_theorem | audit_in_progress | critical | 1129 | 10.64 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py` |
| 19 | `physical_lattice_necessity_note` | no_go | unaudited | critical | 1109 | 22.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_lattice_necessity.py` |
| 20 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | non_terminal_failed | critical | 1075 | 13.57 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 21 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | audit_in_progress | critical | 1071 | 12.57 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 22 | `tensor_support_center_excess_law_note` | bounded_theorem | audit_in_progress | critical | 1043 | 19.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_tensor_support_center_excess_law.py` |
| 23 | `rconn_derived_note` | no_go | unaudited | critical | 986 | 24.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rconn_matching_rule_nogo_certificate.py` |
| 24 | `hypercharge_identification_note` | bounded_theorem | unaudited | critical | 986 | 20.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hypercharge_identification_scope_repair_2026_07_04.py` |
| 25 | `yt_color_projection_correction_note` | no_go | unaudited | critical | 985 | 17.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 26 | `yt_ew_color_projection_theorem` | no_go | unaudited | critical | 924 | 31.85 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_kappa_family_nogo_certificate.py` |
| 27 | `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 898 | 14.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow.py` |
| 28 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | positive_theorem | audit_in_progress | critical | 871 | 12.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 29 | `cpt_exact_note` | positive_theorem | unaudited | critical | 864 | 31.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cpt_exact.py` |
| 30 | `hierarchy_matsubara_decomposition_note` | positive_theorem | unaudited | critical | 864 | 15.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 31 | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | positive_theorem | unaudited | critical | 855 | 26.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py` |
| 32 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | non_terminal_conditional | critical | 845 | 10.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 33 | `dm_neutrino_weak_vector_theorem_note_2026-04-15` | bounded_theorem | unaudited | critical | 840 | 10.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_weak_vector_theorem.py` |
| 34 | `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10` | positive_theorem | non_terminal_conditional | critical | 820 | 23.18 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py` |
| 35 | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | open_gate | unaudited | critical | 818 | 13.68 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py` |
| 36 | `yt_ew_m_residual_note_2026-05-02` | no_go | unaudited | critical | 818 | 11.18 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_m_residual_channel_check.py` |
| 37 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem | non_terminal_conditional | critical | 815 | 13.67 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py` |
| 38 | `gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note` | positive_theorem | unaudited | critical | 809 | 19.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py` |
| 39 | `gauge_vacuum_plaquette_constant_lift_obstruction_note` | positive_theorem | unaudited | critical | 805 | 13.65 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_constant_lift_obstruction.py` |
| 40 | `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 796 | 30.64 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_q_two_thirds_algebraic_narrow.py` |
| 41 | `gauge_vacuum_plaquette_perron_jacobi_underdetermination_note` | positive_theorem | unaudited | critical | 792 | 12.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py` |
| 42 | `dm_neutrino_cascade_geometry_note_2026-04-14` | positive_theorem | unaudited | critical | 791 | 12.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 43 | `gauge_vacuum_plaquette_framework_point_underdetermination_note` | positive_theorem | unaudited | critical | 786 | 14.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_framework_point_underdetermination.py` |
| 44 | `axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 785 | 14.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py` |
| 45 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | bounded_theorem | unaudited | critical | 783 | 22.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 46 | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | positive_theorem | unaudited | critical | 783 | 16.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py` |
| 47 | `rp_p2_gauge_extension_and_realization_residual_note_2026-05-28` | bounded_theorem | unaudited | critical | 774 | 15.60 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py` |
| 48 | `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | bounded_theorem | unaudited | critical | 771 | 26.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_z3_equivariant_anticommuting_no_go.py` |
| 49 | `gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_theorem_note_2026-06-02` | bounded_theorem | unaudited | critical | 771 | 10.09 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py` |
| 50 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 759 | 12.07 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |

## Citation cycle break targets

62 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 724 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 3 | 671 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 3 | `cycle-0003` | 5 | 671 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 671 | `strong_cp_theta_bar_structured_admission_2026-06-04` | critical | unaudited |
| 5 | `cycle-0005` | 6 | 671 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 6 | `cycle-0006` | 6 | 671 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 7 | `cycle-0007` | 7 | 671 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 8 | `cycle-0008` | 7 | 671 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 9 | `cycle-0009` | 7 | 671 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 10 | `cycle-0010` | 8 | 671 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 671 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 12 | `cycle-0012` | 8 | 671 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 13 | `cycle-0013` | 8 | 671 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 14 | `cycle-0014` | 9 | 671 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 9 | 671 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 16 | `cycle-0016` | 9 | 671 | `a3_r2_review_confirms_exhaustion_note_2026-05-08_r2hr` | critical | unaudited |
| 17 | `cycle-0017` | 9 | 671 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 18 | `cycle-0018` | 9 | 671 | `a3_r4_review_confirmed_note_2026-05-08_r4hr` | critical | unaudited |
| 19 | `cycle-0019` | 11 | 671 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 12 | 671 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 21 | `cycle-0021` | 12 | 671 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 22 | `cycle-0022` | 12 | 671 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 23 | `cycle-0023` | 12 | 671 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 24 | `cycle-0024` | 13 | 671 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 25 | `cycle-0025` | 13 | 671 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
