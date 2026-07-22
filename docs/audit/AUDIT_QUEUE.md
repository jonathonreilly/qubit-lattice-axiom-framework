# Audit Queue

**Total pending:** 3048
**Ready (all deps at retained-grade/metadata tiers or supplied axioms/approved primitives):** 637

By criticality:
- `critical`: 648
- `high`: 372
- `medium`: 839
- `leaf`: 1189

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | positive_theorem | non_terminal_failed | critical | 1767 | 25.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem | non_terminal_conditional | critical | 1757 | 17.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | positive_theorem | non_terminal_conditional | critical | 1460 | 14.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 4 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | bounded_theorem | non_terminal_conditional | critical | 1382 | 13.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 5 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | unaudited | critical | 1378 | 12.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 6 | `abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18` | bounded_theorem | non_terminal_conditional | critical | 1377 | 10.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py` |
| 7 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | non_terminal_conditional | critical | 1283 | 18.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 8 | `s3_boundary_link_theorem_note` | bounded_theorem | non_terminal_conditional | critical | 1206 | 14.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 9 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | bounded_theorem | non_terminal_conditional | critical | 1199 | 11.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 10 | `physical_lattice_necessity_note` | no_go | unaudited | critical | 1157 | 22.18 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_lattice_necessity.py` |
| 11 | `staggered_dirac_substep4_ac_phi_trace_equipartition_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | unaudited | critical | 1143 | 10.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_phi_trace_equipartition_bridge_2026_05_17.py` |
| 12 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 1123 | 13.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 13 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | non_terminal_conditional | critical | 1119 | 12.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 14 | `tensor_support_center_excess_law_note` | bounded_theorem | non_terminal_conditional | critical | 1091 | 19.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_tensor_support_center_excess_law.py` |
| 15 | `rconn_derived_note` | no_go | unaudited | critical | 1053 | 25.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rconn_matching_rule_nogo_certificate.py` |
| 16 | `hypercharge_identification_note` | bounded_theorem | non_terminal_conditional | critical | 1034 | 20.52 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hypercharge_identification_scope_repair_2026_07_04.py` |
| 17 | `yt_color_projection_correction_note` | no_go | unaudited | critical | 1033 | 18.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 18 | `yt_ew_color_projection_theorem` | no_go | unaudited | critical | 978 | 31.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_kappa_family_nogo_certificate.py` |
| 19 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 925 | 12.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 20 | `hierarchy_matsubara_decomposition_note` | positive_theorem | non_terminal_conditional | critical | 912 | 15.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 21 | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | positive_theorem | non_terminal_conditional | critical | 909 | 26.33 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py` |
| 22 | `wilson_small_a_matching_beta_gbare_narrow_theorem_note_2026-06-07` | positive_theorem | unaudited | critical | 902 | 12.82 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py` |
| 23 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | non_terminal_conditional | critical | 893 | 10.30 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 24 | `dm_neutrino_dirac_bridge_theorem_note_2026-04-15` | positive_theorem | non_terminal_conditional | critical | 887 | 18.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_dirac_bridge_theorem.py` |
| 25 | `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 872 | 23.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py` |
| 26 | `yt_ew_m_residual_note_2026-05-02` | no_go | unaudited | critical | 870 | 11.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_m_residual_channel_check.py` |
| 27 | `gauge_vacuum_plaquette_finite_tensor_word_packet_bounded_note_2026-05-10` | bounded_theorem | non_terminal_conditional | critical | 860 | 23.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_finite_tensor_word_packet.py` |
| 28 | `sm_relativistic_dof_count_import_note_2026-05-17` | bounded_theorem | unaudited | critical | 858 | 15.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_relativistic_dof_finite_inventory.py` |
| 29 | `gauge_vacuum_plaquette_constant_lift_obstruction_note` | positive_theorem | unaudited | critical | 857 | 13.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_constant_lift_obstruction.py` |
| 30 | `gauge_vacuum_plaquette_perron_jacobi_underdetermination_note` | positive_theorem | non_terminal_conditional | critical | 846 | 12.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py` |
| 31 | `dm_neutrino_cascade_geometry_note_2026-04-14` | bounded_theorem | non_terminal_conditional | critical | 839 | 12.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 32 | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | positive_theorem | non_terminal_failed | critical | 836 | 15.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py` |
| 33 | `axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05` | bounded_theorem | non_terminal_conditional | critical | 836 | 14.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py` |
| 34 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | bounded_theorem | non_terminal_failed | critical | 834 | 22.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 35 | `rp_p2_gauge_extension_and_realization_residual_note_2026-05-28` | bounded_theorem | unaudited | critical | 825 | 15.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py` |
| 36 | `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | bounded_theorem | unaudited | critical | 822 | 26.68 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_z3_equivariant_anticommuting_no_go.py` |
| 37 | `gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_theorem_note_2026-06-02` | bounded_theorem | non_terminal_conditional | critical | 822 | 10.19 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py` |
| 38 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 810 | 12.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 39 | `cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09` | bounded_theorem | non_terminal_conditional | critical | 809 | 12.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cluster_decomposition_mass_gap_bridge_check.py` |
| 40 | `dm_neutrino_odd_circulant_z2_slot_theorem_note_2026-04-15` | positive_theorem | non_terminal_conditional | critical | 797 | 12.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py` |
| 41 | `gstar_thermal_seven_eighths_stefan_boltzmann_bridge_narrow_theorem_note_2026-06-06` | bounded_theorem | audit_in_progress | critical | 797 | 12.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py` |
| 42 | `su3_wigner_intertwiner_block1_theorem_note_2026-05-03` | positive_theorem | audit_in_progress | critical | 791 | 11.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_wigner_intertwiner_engine.py` |
| 43 | `dm_neutrino_z3_circulant_mass_basis_no_go_note_2026-04-15` | no_go | unaudited | critical | 787 | 11.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_z3_circulant_mass_basis_nogo.py` |
| 44 | `plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06` | bounded_theorem | non_terminal_conditional | critical | 786 | 13.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py` |
| 45 | `gate_b_poisson_self_gravity_note` | no_go | unaudited | critical | 775 | 12.60 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_poisson_self_gravity_probe.py` |
| 46 | `pmns_oriented_cycle_channel_value_law_note` | bounded_theorem | unaudited | critical | 771 | 18.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_oriented_cycle_channel_value_law.py` |
| 47 | `self_consistency_forces_poisson_note` | bounded_theorem | non_terminal_conditional | critical | 771 | 18.09 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_self_consistent_field_equation.py` |
| 48 | `poisson_self_gravity_loop_v3_note` | bounded_theorem | non_terminal_conditional | critical | 771 | 11.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/poisson_self_gravity_loop_v3.py` |
| 49 | `pmns_graph_axis_to_active_lane_bridge_note` | bounded_theorem | unaudited | critical | 771 | 11.09 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_graph_axis_to_active_lane_bridge.py` |
| 50 | `su3_cube_index_graph_shortcut_open_gate_note_2026-05-03` | no_go | unaudited | critical | 766 | 10.08 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_cube_index_graph_shortcut_open_gate.py` |

## Citation cycle break targets

59 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 770 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 3 | 717 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 3 | `cycle-0003` | 5 | 717 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 717 | `strong_cp_theta_bar_structured_admission_2026-06-04` | critical | unaudited |
| 5 | `cycle-0005` | 6 | 717 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 6 | `cycle-0006` | 6 | 717 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 7 | `cycle-0007` | 7 | 717 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 8 | `cycle-0008` | 7 | 717 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 9 | `cycle-0009` | 7 | 717 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 10 | `cycle-0010` | 8 | 717 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 717 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 12 | `cycle-0012` | 8 | 717 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 13 | `cycle-0013` | 8 | 717 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 14 | `cycle-0014` | 9 | 717 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 9 | 717 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 16 | `cycle-0016` | 9 | 717 | `a3_r2_review_confirms_exhaustion_note_2026-05-08_r2hr` | critical | unaudited |
| 17 | `cycle-0017` | 9 | 717 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 18 | `cycle-0018` | 9 | 717 | `a3_r4_review_confirmed_note_2026-05-08_r4hr` | critical | unaudited |
| 19 | `cycle-0019` | 11 | 717 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 12 | 717 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 21 | `cycle-0021` | 12 | 717 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 22 | `cycle-0022` | 13 | 717 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 23 | `cycle-0023` | 13 | 717 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 24 | `cycle-0024` | 13 | 717 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 25 | `cycle-0025` | 13 | 717 | `a3_r5_review_confirms_obstruction_note_2026-05-08_r5hr` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
