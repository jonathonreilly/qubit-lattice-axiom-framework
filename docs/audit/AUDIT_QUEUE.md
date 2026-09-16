# Audit Queue

**Total pending:** 4504
**Ready (dependencies and deterministic forensic evidence):** 1668
**Dependency-ready:** 1748
**Forensic-evidence-ready:** 4082

By criticality:
- `critical`: 716
- `high`: 322
- `medium`: 1127
- `leaf`: 2339

By work kind:
- `fresh_scientific_audit`: 4082
- `legacy_packet_upgrade`: 0
- `evidence_repair_required`: 422

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | work kind | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1709 | 25.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1702 | 17.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `graph_first_su3_integration_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1532 | 52.08 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_graph_first_su3_integration.py` |
| 4 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1499 | 18.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 5 | `z2_hw1_mass_matrix_parametrization_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1368 | 16.42 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z2_hw1_mass_matrix_parametrization.py` |
| 6 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1363 | 11.41 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 7 | `site_phase_cube_shift_intertwiner_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1360 | 20.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_site_phase_cube_shift_intertwiner.py` |
| 8 | `s3_taste_cube_decomposition_note` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1354 | 15.40 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_action_taste_cube_decomposition.py` |
| 9 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1238 | 18.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 10 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1220 | 15.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 11 | `plaquette_self_consistency_note` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1208 | 47.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py` |
| 12 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1191 | 19.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 13 | `abj_p_rec_spintaste_clifford_core_bridge_note_2026-06-18` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1190 | 11.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_prec_spintaste_clifford_core_bridge_2026_06_18.py` |
| 14 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1188 | 13.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 15 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1184 | 15.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 16 | `abj_p_comp_scale_free_singlet_completion_classification_note_2026-06-18` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1183 | 10.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py` |
| 17 | `abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1183 | 10.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py` |
| 18 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1114 | 11.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 19 | `naive_lattice_fermion_two_power_d_species_count_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1070 | 16.07 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_naive_lattice_fermion_two_power_d_species_count_narrow.py` |
| 20 | `staggered_os0_supplied_action_ks_blocking_four_taste_module_narrow_theorem_note_2026-07-11` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1063 | 11.05 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py` |
| 21 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1037 | 12.02 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pl_topology_finite_cone_cap_certificate.py` |
| 22 | `koide_circulant_character_bridge_narrow_theorem_note_2026-05-09` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1027 | 25.51 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_character_bridge_narrow.py` |
| 23 | `finite_rank_gravity_residual_helper_note_2026-04-14` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1024 | 11.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_finite_rank_gravity_residual.py` |
| 24 | `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1018 | 13.49 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_s_tadpole_improvement_vertex_power_narrow.py` |
| 25 | `s3_boundary_link_theorem_note` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1013 | 12.99 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 26 | `qcd_low_energy_running_bridge_note_2026-05-01` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1009 | 12.98 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 27 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1007 | 12.48 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 28 | `gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 957 | 24.90 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow.py` |
| 29 | `gauge_vacuum_plaquette_reduction_existence_theorem_note` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 951 | 13.89 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_reduction_existence_theorem.py` |
| 30 | `beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 932 | 11.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_beta_gbare_rescaling_abstract_identity_narrow.py` |
| 31 | `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 930 | 14.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow.py` |
| 32 | `quark_route2_eta_floor_hf_boundary_note` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 900 | 10.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/quark_route2_eta_floor_hf_boundary_check.py` |
| 33 | `gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 899 | 18.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py` |
| 34 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | fresh_scientific_audit | positive_theorem | unaudited | critical | 898 | 11.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 35 | `cpt_exact_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 894 | 28.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cpt_exact.py` |
| 36 | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 887 | 25.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py` |
| 37 | `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 866 | 24.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py` |
| 38 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 848 | 13.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py` |
| 39 | `gauge_scalar_temporal_completion_theorem_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 823 | 16.19 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_scalar_temporal_completion_theorem.py` |
| 40 | `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 822 | 29.68 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_q_two_thirds_algebraic_narrow.py` |
| 41 | `alpha_lm_geometric_mean_identity_theorem_note_2026-04-24` | fresh_scientific_audit | positive_theorem | unaudited | critical | 822 | 20.68 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_lm_geometric_mean_identity.py` |
| 42 | `wilson_small_a_matching_beta_gbare_narrow_theorem_note_2026-06-07` | fresh_scientific_audit | positive_theorem | unaudited | critical | 813 | 12.67 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py` |
| 43 | `hierarchy_matsubara_decomposition_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 809 | 14.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 44 | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 808 | 14.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py` |
| 45 | `staggered_only_det_positivity_case_a_note_2026-05-17` | fresh_scientific_audit | positive_theorem | unaudited | critical | 796 | 21.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_only_det_positivity_case_a_2026-05-17.py` |
| 46 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 789 | 10.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 47 | `dm_neutrino_dirac_bridge_theorem_note_2026-04-15` | fresh_scientific_audit | positive_theorem | unaudited | critical | 783 | 18.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_dirac_bridge_theorem.py` |
| 48 | `plaquette_v1_picard_fuchs_ode_note_2026-05-05` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 770 | 15.09 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py` |
| 49 | `su3_wigner_intertwiner_block1_theorem_note_2026-05-03` | fresh_scientific_audit | positive_theorem | unaudited | critical | 767 | 11.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_wigner_intertwiner_engine.py` |
| 50 | `staggered_dirac_chirality_parity_bridge_narrow_theorem_note_2026-06-06` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 758 | 10.57 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_chirality_parity_bridge_2026_06_06.py` |

## Citation cycle break targets

63 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 657 | `quark_cp_carrier_completion_note_2026-04-18` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 616 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 3 | `cycle-0003` | 5 | 616 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 616 | `strong_cp_theta_bar_structured_admission_2026-06-04` | critical | unaudited |
| 5 | `cycle-0005` | 6 | 616 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 6 | `cycle-0006` | 6 | 616 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 7 | `cycle-0007` | 7 | 616 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 8 | `cycle-0008` | 7 | 616 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 9 | `cycle-0009` | 7 | 616 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 10 | `cycle-0010` | 8 | 616 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 616 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 12 | `cycle-0012` | 8 | 616 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 13 | `cycle-0013` | 8 | 616 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 14 | `cycle-0014` | 9 | 616 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 9 | 616 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 16 | `cycle-0016` | 9 | 616 | `a3_r2_review_confirms_exhaustion_note_2026-05-08_r2hr` | critical | unaudited |
| 17 | `cycle-0017` | 9 | 616 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 18 | `cycle-0018` | 9 | 616 | `a3_r4_review_confirmed_note_2026-05-08_r4hr` | critical | unaudited |
| 19 | `cycle-0019` | 11 | 616 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 12 | 616 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 21 | `cycle-0021` | 12 | 616 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 22 | `cycle-0022` | 13 | 616 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 23 | `cycle-0023` | 13 | 616 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 24 | `cycle-0024` | 13 | 616 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 25 | `cycle-0025` | 13 | 616 | `a3_r5_review_confirms_obstruction_note_2026-05-08_r5hr` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
