# Audit Queue

**Total pending:** 2992
**Ready (all deps at retained-grade/metadata tiers or supplied axioms/approved primitives):** 545

By criticality:
- `critical`: 642
- `high`: 367
- `medium`: 825
- `leaf`: 1158

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 1791 | 25.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem | non_terminal_conditional | critical | 1781 | 17.80 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | positive_theorem | non_terminal_conditional | critical | 1475 | 14.03 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 4 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1398 | 13.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 5 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | unaudited | critical | 1394 | 12.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 6 | `abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18` | bounded_theorem | non_terminal_conditional | critical | 1393 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py` |
| 7 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | non_terminal_failed | critical | 1298 | 18.84 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 8 | `s3_boundary_link_theorem_note` | bounded_theorem | unaudited | critical | 1222 | 14.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 9 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | positive_theorem | unaudited | critical | 1214 | 11.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 10 | `physical_lattice_necessity_note` | no_go | unaudited | critical | 1172 | 22.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_lattice_necessity.py` |
| 11 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | non_terminal_conditional | critical | 1138 | 13.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 12 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | non_terminal_conditional | critical | 1135 | 12.65 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 13 | `quark_route2_eta_floor_hf_boundary_note` | bounded_theorem | non_terminal_conditional | critical | 1106 | 11.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/quark_route2_eta_floor_hf_boundary_check.py` |
| 14 | `rconn_derived_note` | no_go | unaudited | critical | 1067 | 25.06 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rconn_matching_rule_nogo_certificate.py` |
| 15 | `hypercharge_identification_note` | bounded_theorem | non_terminal_conditional | critical | 1049 | 21.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hypercharge_identification_scope_repair_2026_07_04.py` |
| 16 | `yt_color_projection_correction_note` | no_go | unaudited | critical | 1048 | 18.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 17 | `yt_ew_color_projection_theorem` | no_go | unaudited | critical | 992 | 31.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_kappa_family_nogo_certificate.py` |
| 18 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | positive_theorem | non_terminal_failed | critical | 939 | 12.38 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 19 | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | positive_theorem | unaudited | critical | 923 | 26.35 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py` |
| 20 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | non_terminal_conditional | critical | 907 | 10.33 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 21 | `dm_neutrino_dirac_bridge_theorem_note_2026-04-15` | positive_theorem | unaudited | critical | 901 | 18.32 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_dirac_bridge_theorem.py` |
| 22 | `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 886 | 23.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py` |
| 23 | `yt_ew_m_residual_note_2026-05-02` | no_go | unaudited | critical | 884 | 11.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_m_residual_channel_check.py` |
| 24 | `gauge_vacuum_plaquette_finite_tensor_word_packet_bounded_note_2026-05-10` | bounded_theorem | unaudited | critical | 874 | 23.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_finite_tensor_word_packet.py` |
| 25 | `sm_relativistic_dof_count_import_note_2026-05-17` | bounded_theorem | non_terminal_conditional | critical | 872 | 15.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_relativistic_dof_finite_inventory.py` |
| 26 | `gauge_vacuum_plaquette_constant_lift_obstruction_note` | positive_theorem | unaudited | critical | 868 | 13.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_constant_lift_obstruction.py` |
| 27 | `gauge_vacuum_plaquette_perron_jacobi_underdetermination_note` | positive_theorem | unaudited | critical | 860 | 12.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py` |
| 28 | `dm_neutrino_cascade_geometry_note_2026-04-14` | bounded_theorem | non_terminal_conditional | critical | 853 | 12.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 29 | `axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05` | bounded_theorem | non_terminal_conditional | critical | 851 | 14.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py` |
| 30 | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | positive_theorem | unaudited | critical | 850 | 15.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py` |
| 31 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | bounded_theorem | unaudited | critical | 849 | 22.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 32 | `gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_theorem_note_2026-06-02` | bounded_theorem | non_terminal_conditional | critical | 837 | 10.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py` |
| 33 | `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | bounded_theorem | unaudited | critical | 836 | 26.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_z3_equivariant_anticommuting_no_go.py` |
| 34 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 825 | 12.19 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 35 | `cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09` | bounded_theorem | non_terminal_conditional | critical | 824 | 12.19 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cluster_decomposition_mass_gap_bridge_check.py` |
| 36 | `dm_neutrino_odd_circulant_z2_slot_theorem_note_2026-04-15` | positive_theorem | non_terminal_conditional | critical | 811 | 12.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py` |
| 37 | `su3_wigner_intertwiner_block1_theorem_note_2026-05-03` | positive_theorem | non_terminal_conditional | critical | 805 | 11.65 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_wigner_intertwiner_engine.py` |
| 38 | `dm_neutrino_z3_circulant_mass_basis_no_go_note_2026-04-15` | no_go | unaudited | critical | 801 | 11.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_z3_circulant_mass_basis_nogo.py` |
| 39 | `plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06` | bounded_theorem | non_terminal_conditional | critical | 800 | 13.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py` |
| 40 | `gate_b_poisson_self_gravity_note` | no_go | unaudited | critical | 790 | 12.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_poisson_self_gravity_probe.py` |
| 41 | `poisson_response_kernel_and_sign_normalization_finite_grid_bounded_note_2026-07-26` | bounded_theorem | unaudited | critical | 789 | 10.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py` |
| 42 | `pmns_oriented_cycle_channel_value_law_note` | bounded_theorem | unaudited | critical | 785 | 18.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_oriented_cycle_channel_value_law.py` |
| 43 | `pmns_graph_axis_to_active_lane_bridge_note` | bounded_theorem | non_terminal_failed | critical | 785 | 11.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_graph_axis_to_active_lane_bridge.py` |
| 44 | `su3_cube_index_graph_shortcut_open_gate_note_2026-05-03` | no_go | unaudited | critical | 780 | 10.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_cube_index_graph_shortcut_open_gate.py` |
| 45 | `pmns_uniform_scalar_deformation_boundary_note` | positive_theorem | non_terminal_conditional | critical | 779 | 12.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_uniform_scalar_deformation_boundary.py` |
| 46 | `pmns_hw1_source_transfer_boundary_note` | bounded_theorem | non_terminal_conditional | critical | 777 | 12.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_hw1_source_transfer_boundary.py` |
| 47 | `gravity_full_self_consistency_note` | bounded_theorem | non_terminal_conditional | critical | 776 | 14.10 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 48 | `koide_kappa_zd_action_circulant_character_decomposition_narrow_theorem_note_2026-06-05` | positive_theorem | non_terminal_failed | critical | 774 | 10.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_koide_kappa_zd_action_character_2026_06_05.py` |
| 49 | `lattice_greens_maradudin_asymptotic_accepted_premise_bridge_bounded_note_2026-05-27` | bounded_theorem | unaudited | critical | 774 | 10.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/lattice_greens_maradudin_asymptotic_accepted_premise_runner.py` |
| 50 | `record_history_order_time_rate_firewall_2026-06-05` | no_go | unaudited | critical | 771 | 17.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_record_history_time_rate_firewall_2026_06_05.py` |

## Citation cycle break targets

59 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 784 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 3 | 731 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 3 | `cycle-0003` | 5 | 731 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 731 | `strong_cp_theta_bar_structured_admission_2026-06-04` | critical | unaudited |
| 5 | `cycle-0005` | 6 | 731 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 6 | `cycle-0006` | 6 | 731 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 7 | `cycle-0007` | 7 | 731 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 8 | `cycle-0008` | 7 | 731 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 9 | `cycle-0009` | 7 | 731 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 10 | `cycle-0010` | 8 | 731 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 731 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 12 | `cycle-0012` | 8 | 731 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 13 | `cycle-0013` | 8 | 731 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 14 | `cycle-0014` | 9 | 731 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 9 | 731 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 16 | `cycle-0016` | 9 | 731 | `a3_r2_review_confirms_exhaustion_note_2026-05-08_r2hr` | critical | unaudited |
| 17 | `cycle-0017` | 9 | 731 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 18 | `cycle-0018` | 9 | 731 | `a3_r4_review_confirmed_note_2026-05-08_r4hr` | critical | unaudited |
| 19 | `cycle-0019` | 11 | 731 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 12 | 731 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 21 | `cycle-0021` | 12 | 731 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 22 | `cycle-0022` | 13 | 731 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 23 | `cycle-0023` | 13 | 731 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 24 | `cycle-0024` | 13 | 731 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 25 | `cycle-0025` | 13 | 731 | `a3_r5_review_confirms_obstruction_note_2026-05-08_r5hr` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
