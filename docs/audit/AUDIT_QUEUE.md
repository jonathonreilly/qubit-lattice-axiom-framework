# Audit Queue

**Total pending:** 3105
**Ready (dependencies and deterministic forensic evidence):** 170
**Dependency-ready:** 592
**Forensic-evidence-ready:** 877

By criticality:
- `critical`: 667
- `high`: 383
- `medium`: 860
- `leaf`: 1195

By work kind:
- `fresh_scientific_audit`: 873
- `legacy_packet_upgrade`: 4
- `evidence_repair_required`: 2228

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | work kind | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | legacy_packet_upgrade | positive_theorem | unaudited | critical | 1796 | 25.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1786 | 17.80 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1648 | 18.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 4 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 1478 | 14.03 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 5 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1403 | 13.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 6 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1217 | 11.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 7 | `qcd_low_energy_running_bridge_note_2026-05-01` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1141 | 13.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 8 | `hypercharge_identification_note` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 1052 | 21.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hypercharge_identification_scope_repair_2026_07_04.py` |
| 9 | `axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 854 | 14.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py` |
| 10 | `gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_theorem_note_2026-06-02` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 840 | 10.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py` |
| 11 | `su3_wigner_intertwiner_block1_theorem_note_2026-05-03` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 808 | 11.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_wigner_intertwiner_engine.py` |
| 12 | `pmns_uniform_scalar_deformation_boundary_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 782 | 12.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_uniform_scalar_deformation_boundary.py` |
| 13 | `koide_kappa_zd_action_circulant_character_decomposition_narrow_theorem_note_2026-06-05` | fresh_scientific_audit | positive_theorem | non_terminal_failed | critical | 777 | 10.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_koide_kappa_zd_action_character_2026_06_05.py` |
| 14 | `koide_q_readout_factorization_theorem_2026-04-22` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 762 | 14.08 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_q_readout_factorization_theorem.py` |
| 15 | `clifford_chirality_dimension_narrow_theorem_note_2026-05-10` | legacy_packet_upgrade | positive_theorem | unaudited | critical | 745 | 10.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_clifford_chirality_dimension_narrow.py` |
| 16 | `koide_cyclic_wilson_descendant_law_note_2026-04-18` | fresh_scientific_audit | positive_theorem | unaudited | critical | 744 | 14.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_cyclic_wilson_descendant_law.py` |
| 17 | `lattice_nn_light_cone_note` | legacy_packet_upgrade | positive_theorem | unaudited | critical | 742 | 12.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/lattice_nn_topological_causal_bound_check.py` |
| 18 | `charged_lepton_registered_mass_dft_coordinate_theorem_note_2026-07-11` | fresh_scientific_audit | positive_theorem | audit_in_progress | critical | 741 | 10.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/charged_lepton_registered_mass_dft_coordinate_theorem_2026_07_11.py` |
| 19 | `self_gravity_backreaction_closure_note` | fresh_scientific_audit | no_go | unaudited | critical | 737 | 11.03 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/poisson_self_gravity_loop_v3.py` |
| 20 | `observable_principle_record_scalar_map_no_go_note_2026-06-05` | legacy_packet_upgrade | no_go | unaudited | critical | 736 | 12.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_observable_principle_record_scalar_map_no_go_2026_06_05.py` |
| 21 | `quantum_local_algebra_does_not_force_boost_action_faith_no_go_note_2026-06-02` | fresh_scientific_audit | no_go | unaudited | critical | 736 | 12.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/quantum_local_algebra_boost_action_faith_no_go_2026_06_02.py` |
| 22 | `post_record_finite_to_unbounded_family_lift_no_go_2026-06-06` | fresh_scientific_audit | no_go | unaudited | critical | 736 | 11.03 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_post_record_finite_to_unbounded_family_lift_nogo_2026_06_06.py` |
| 23 | `planck_boundary_orientation_incidence_no_go_note_2026-04-30` | fresh_scientific_audit | no_go | unaudited | critical | 735 | 12.52 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_boundary_orientation_incidence_no_go.py` |
| 24 | `post_record_count_probability_firewall_2026-06-06` | fresh_scientific_audit | no_go | unaudited | critical | 735 | 12.52 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_post_record_count_probability_firewall_2026_06_06.py` |
| 25 | `koide_a1_loop_final_status_2026-04-22` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 735 | 10.02 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_a1_ansatz_algebra_certificate.py` |
| 26 | `flavor_r_half_is_the_records_flow_separatrix_2026-06-02` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 109 | 15.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_r_half_is_the_records_flow_separatrix_2026_06_02.py` |
| 27 | `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29` | evidence_repair_required | bounded_theorem | unaudited | critical | 1771 | 20.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cl3_per_site_uniqueness_check.py` |
| 28 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | evidence_repair_required | bounded_theorem | unaudited | critical | 1584 | 29.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 29 | `z2_hw1_mass_matrix_parametrization_note` | evidence_repair_required | positive_theorem | unaudited | critical | 1483 | 20.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z2_hw1_mass_matrix_parametrization.py` |
| 30 | `s3_mass_matrix_no_go_note` | evidence_repair_required | open_gate | unaudited | critical | 1477 | 14.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 31 | `no_per_site_chirality_theorem_note_2026-05-02` | evidence_repair_required | no_go | unaudited | critical | 1412 | 15.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/no_per_site_chirality_check.py` |
| 32 | `abj_p_rec_spintaste_clifford_core_bridge_note_2026-06-18` | evidence_repair_required | bounded_theorem | unaudited | critical | 1405 | 11.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_prec_spintaste_clifford_core_bridge_2026_06_18.py` |
| 33 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | evidence_repair_required | no_go | unaudited | critical | 1399 | 12.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 34 | `abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18` | evidence_repair_required | bounded_theorem | non_terminal_conditional | critical | 1398 | 10.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py` |
| 35 | `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` | evidence_repair_required | bounded_theorem | unaudited | critical | 1397 | 12.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py` |
| 36 | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1395 | 23.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py` |
| 37 | `anomaly_forces_time_theorem` | evidence_repair_required | bounded_theorem | unaudited | critical | 1393 | 39.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 38 | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1359 | 18.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_per_site_hilbert_dim_two_check.py` |
| 39 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | evidence_repair_required | positive_theorem | non_terminal_failed | critical | 1301 | 18.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 40 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | evidence_repair_required | positive_theorem | unaudited | critical | 1295 | 15.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 41 | `three_generation_observable_theorem_note` | evidence_repair_required | bounded_theorem | unaudited | critical | 1291 | 62.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 42 | `plaquette_self_consistency_note` | evidence_repair_required | bounded_theorem | unaudited | critical | 1266 | 49.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py` |
| 43 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | evidence_repair_required | bounded_theorem | unaudited | critical | 1262 | 15.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 44 | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | evidence_repair_required | positive_theorem | unaudited | critical | 1256 | 28.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep1_grassmann_forcing_bridge_2026_05_16.py` |
| 45 | `cl3_oh_cubic_lift_faithful_narrow_theorem_note_2026-05-26` | evidence_repair_required | bounded_theorem | unaudited | critical | 1246 | 12.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_oh_cubic_lift_faithful_runner.py` |
| 46 | `lattice_laplacian_shell_localization_identity_bounded_theorem_note_2026-06-16` | evidence_repair_required | bounded_theorem | unaudited | critical | 1243 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/lattice_laplacian_shell_localization_2026_06_16.py` |
| 47 | `coarse_grained_exterior_law_helper_note_2026-04-14` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1240 | 12.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_coarse_grained_exterior_law.py` |
| 48 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | evidence_repair_required | bounded_theorem | unaudited | critical | 1239 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_one_parameter_reduced_shell_law.py` |
| 49 | `oh_schur_independent_boundary_source_bridge_theorem_note_2026-07-25` | evidence_repair_required | bounded_theorem | unaudited | critical | 1231 | 10.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_oh_schur_independent_boundary_source_bridge.py` |
| 50 | `oh_schur_boundary_action_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1230 | 19.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_oh_schur_boundary_action.py` |

## Citation cycle break targets

60 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 787 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 3 | 734 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 3 | `cycle-0003` | 5 | 734 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 734 | `strong_cp_theta_bar_structured_admission_2026-06-04` | critical | unaudited |
| 5 | `cycle-0005` | 6 | 734 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 6 | `cycle-0006` | 6 | 734 | `strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07` | critical | unaudited |
| 7 | `cycle-0007` | 7 | 734 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 8 | `cycle-0008` | 7 | 734 | `newphysics_np_strong_cp_theta_note_2026-05-10_npcp` | critical | unaudited |
| 9 | `cycle-0009` | 7 | 734 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 10 | `cycle-0010` | 8 | 734 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 734 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 12 | `cycle-0012` | 8 | 734 | `ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10` | critical | unaudited |
| 13 | `cycle-0013` | 8 | 734 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 14 | `cycle-0014` | 9 | 734 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 9 | 734 | `a3_r1_review_confirms_obstruction_note_2026-05-08_r1hr` | critical | unaudited |
| 16 | `cycle-0016` | 9 | 734 | `a3_r2_review_confirms_exhaustion_note_2026-05-08_r2hr` | critical | unaudited |
| 17 | `cycle-0017` | 9 | 734 | `a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr` | critical | unaudited |
| 18 | `cycle-0018` | 9 | 734 | `a3_r4_review_confirmed_note_2026-05-08_r4hr` | critical | unaudited |
| 19 | `cycle-0019` | 11 | 734 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 12 | 734 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 21 | `cycle-0021` | 12 | 734 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 22 | `cycle-0022` | 13 | 734 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 23 | `cycle-0023` | 13 | 734 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 24 | `cycle-0024` | 13 | 734 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 25 | `cycle-0025` | 13 | 734 | `a3_r5_review_confirms_obstruction_note_2026-05-08_r5hr` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
