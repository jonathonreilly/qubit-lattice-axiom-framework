# Audit Queue

**Total pending:** 2990
**Ready (all deps at retained-grade/metadata tiers or supplied axioms/approved primitives):** 635

By criticality:
- `critical`: 665
- `high`: 357
- `medium`: 791
- `leaf`: 1177

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 1727 | 25.25 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 1717 | 17.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 1588 | 18.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 4 | `z2_hw1_mass_matrix_parametrization_note` | positive_theorem | unaudited | critical | 1432 | 19.98 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z2_hw1_mass_matrix_parametrization.py` |
| 5 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | positive_theorem | unaudited | critical | 1427 | 13.98 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 6 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1349 | 13.90 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 7 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | unaudited | critical | 1345 | 12.39 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 8 | `abj_p_comp_scale_free_singlet_completion_classification_note_2026-06-18` | bounded_theorem | unaudited | critical | 1344 | 10.89 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py` |
| 9 | `abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18` | bounded_theorem | non_terminal_conditional | critical | 1344 | 10.89 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py` |
| 10 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | unaudited | critical | 1250 | 18.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 11 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | unaudited | critical | 1244 | 15.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 12 | `s3_boundary_link_theorem_note` | bounded_theorem | unaudited | critical | 1173 | 14.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 13 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | bounded_theorem | unaudited | critical | 1166 | 11.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 14 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 1164 | 18.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 15 | `physical_lattice_necessity_note` | no_go | unaudited | critical | 1124 | 22.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_lattice_necessity.py` |
| 16 | `staggered_dirac_substep4_ac_phi_trace_equipartition_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | unaudited | critical | 1110 | 10.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_phi_trace_equipartition_bridge_2026_05_17.py` |
| 17 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 1090 | 13.09 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 18 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | unaudited | critical | 1086 | 12.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 19 | `tensor_support_center_excess_law_note` | bounded_theorem | unaudited | critical | 1058 | 19.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_tensor_support_center_excess_law.py` |
| 20 | `rconn_derived_note` | no_go | unaudited | critical | 1020 | 25.00 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rconn_matching_rule_nogo_certificate.py` |
| 21 | `hypercharge_identification_note` | bounded_theorem | non_terminal_conditional | critical | 1001 | 20.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hypercharge_identification_scope_repair_2026_07_04.py` |
| 22 | `yt_color_projection_correction_note` | no_go | unaudited | critical | 1000 | 17.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 23 | `yt_ew_color_projection_theorem` | no_go | unaudited | critical | 945 | 31.89 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_kappa_family_nogo_certificate.py` |
| 24 | `gauge_vacuum_plaquette_reduction_existence_theorem_note` | bounded_theorem | unaudited | critical | 934 | 14.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_reduction_existence_theorem.py` |
| 25 | `hierarchy_matsubara_decomposition_note` | positive_theorem | unaudited | critical | 879 | 15.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 26 | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | positive_theorem | unaudited | critical | 876 | 26.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py` |
| 27 | `wilson_small_a_matching_beta_gbare_narrow_theorem_note_2026-06-07` | positive_theorem | unaudited | critical | 869 | 12.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py` |
| 28 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | non_terminal_conditional | critical | 860 | 10.25 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 29 | `dm_neutrino_dirac_bridge_theorem_note_2026-04-15` | positive_theorem | unaudited | critical | 854 | 18.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_dirac_bridge_theorem.py` |
| 30 | `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 839 | 23.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py` |
| 31 | `yt_ew_m_residual_note_2026-05-02` | no_go | unaudited | critical | 837 | 11.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_m_residual_channel_check.py` |
| 32 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem | unaudited | critical | 834 | 13.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py` |
| 33 | `gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note` | positive_theorem | unaudited | critical | 828 | 19.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py` |
| 34 | `sm_relativistic_dof_count_import_note_2026-05-17` | bounded_theorem | non_terminal_conditional | critical | 825 | 15.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_relativistic_dof_finite_inventory.py` |
| 35 | `gauge_vacuum_plaquette_constant_lift_obstruction_note` | positive_theorem | unaudited | critical | 824 | 13.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_constant_lift_obstruction.py` |
| 36 | `gauge_vacuum_plaquette_perron_jacobi_underdetermination_note` | positive_theorem | unaudited | critical | 813 | 12.67 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py` |
| 37 | `dm_neutrino_cascade_geometry_note_2026-04-14` | bounded_theorem | non_terminal_conditional | critical | 806 | 12.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 38 | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | positive_theorem | unaudited | critical | 803 | 15.65 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py` |
| 39 | `axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 800 | 14.65 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py` |
| 40 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | bounded_theorem | unaudited | critical | 798 | 22.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 41 | `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | bounded_theorem | unaudited | critical | 789 | 26.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_z3_equivariant_anticommuting_no_go.py` |
| 42 | `rp_p2_gauge_extension_and_realization_residual_note_2026-05-28` | bounded_theorem | non_terminal_conditional | critical | 789 | 15.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py` |
| 43 | `gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_theorem_note_2026-06-02` | bounded_theorem | unaudited | critical | 786 | 10.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py` |
| 44 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 774 | 12.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 45 | `cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 773 | 12.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cluster_decomposition_mass_gap_bridge_check.py` |
| 46 | `dm_neutrino_odd_circulant_z2_slot_theorem_note_2026-04-15` | bounded_theorem | unaudited | critical | 764 | 12.08 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py` |
| 47 | `gstar_thermal_seven_eighths_stefan_boltzmann_bridge_narrow_theorem_note_2026-06-06` | bounded_theorem | audit_in_progress | critical | 764 | 12.08 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py` |
| 48 | `su3_wigner_intertwiner_block1_theorem_note_2026-05-03` | positive_theorem | audit_in_progress | critical | 758 | 11.57 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_wigner_intertwiner_engine.py` |
| 49 | `dm_neutrino_z3_circulant_mass_basis_no_go_note_2026-04-15` | no_go | unaudited | critical | 754 | 11.06 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_z3_circulant_mass_basis_nogo.py` |
| 50 | `plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06` | bounded_theorem | unaudited | critical | 753 | 13.06 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py` |

## Citation cycle break targets

59 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 737 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 3 | 684 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 3 | `cycle-0003` | 5 | 684 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 684 | `strong_cp_theta_bar_structured_admission_2026-06-04` | critical | unaudited |
| 5 | `cycle-0005` | 6 | 684 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 6 | `cycle-0006` | 6 | 684 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 7 | `cycle-0007` | 7 | 684 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 8 | `cycle-0008` | 7 | 684 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 9 | `cycle-0009` | 7 | 684 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 10 | `cycle-0010` | 8 | 684 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 684 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 12 | `cycle-0012` | 8 | 684 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 13 | `cycle-0013` | 8 | 684 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 14 | `cycle-0014` | 9 | 684 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 9 | 684 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 16 | `cycle-0016` | 9 | 684 | `a3_r2_review_confirms_exhaustion_note_2026-05-08_r2hr` | critical | unaudited |
| 17 | `cycle-0017` | 9 | 684 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 18 | `cycle-0018` | 9 | 684 | `a3_r4_review_confirmed_note_2026-05-08_r4hr` | critical | unaudited |
| 19 | `cycle-0019` | 11 | 684 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 12 | 684 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 21 | `cycle-0021` | 12 | 684 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 22 | `cycle-0022` | 13 | 684 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 23 | `cycle-0023` | 13 | 684 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 24 | `cycle-0024` | 13 | 684 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 25 | `cycle-0025` | 13 | 684 | `a3_r5_review_confirms_obstruction_note_2026-05-08_r5hr` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
