# Audit Queue

**Total pending:** 3095
**Ready (dependencies and deterministic forensic evidence):** 501
**Dependency-ready:** 583
**Forensic-evidence-ready:** 2613

By criticality:
- `critical`: 664
- `high`: 382
- `medium`: 857
- `leaf`: 1192

By work kind:
- `fresh_scientific_audit`: 2608
- `legacy_packet_upgrade`: 5
- `evidence_repair_required`: 482

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | work kind | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | legacy_packet_upgrade | positive_theorem | unaudited | critical | 1796 | 25.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_complexification_exclusion_stress_2026_07_13.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 1786 | 17.80 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1648 | 18.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 4 | `z2_hw1_mass_matrix_parametrization_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1483 | 20.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z2_hw1_mass_matrix_parametrization.py` |
| 5 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 1478 | 14.03 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 6 | `abj_p_rec_spintaste_clifford_core_bridge_note_2026-06-18` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1405 | 11.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_prec_spintaste_clifford_core_bridge_2026_06_18.py` |
| 7 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 1403 | 13.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 8 | `abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 1398 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py` |
| 9 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | fresh_scientific_audit | positive_theorem | non_terminal_failed | critical | 1301 | 18.85 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 10 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | fresh_scientific_audit | positive_theorem | unaudited | critical | 1295 | 15.34 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 11 | `plaquette_self_consistency_note` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1266 | 49.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py` |
| 12 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1262 | 15.80 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 13 | `s3_boundary_link_theorem_note` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 1227 | 14.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 14 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 1217 | 11.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 15 | `qcd_low_energy_running_bridge_note_2026-05-01` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 1141 | 13.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 16 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 1140 | 12.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 17 | `quark_route2_eta_floor_hf_boundary_note` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 1109 | 11.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/quark_route2_eta_floor_hf_boundary_check.py` |
| 18 | `hypercharge_identification_note` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 1052 | 21.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hypercharge_identification_scope_repair_2026_07_04.py` |
| 19 | `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10` | fresh_scientific_audit | positive_theorem | unaudited | critical | 968 | 14.92 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow.py` |
| 20 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | fresh_scientific_audit | positive_theorem | unaudited | critical | 942 | 12.38 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 21 | `cpt_exact_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 932 | 31.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cpt_exact.py` |
| 22 | `hierarchy_matsubara_decomposition_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 929 | 15.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 23 | `gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note` | fresh_scientific_audit | positive_theorem | unaudited | critical | 923 | 20.35 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py` |
| 24 | `wilson_small_a_matching_beta_gbare_narrow_theorem_note_2026-06-07` | fresh_scientific_audit | positive_theorem | unaudited | critical | 919 | 12.85 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py` |
| 25 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 910 | 10.33 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 26 | `dm_neutrino_dirac_bridge_theorem_note_2026-04-15` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 904 | 18.32 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_dirac_bridge_theorem.py` |
| 27 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 884 | 13.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py` |
| 28 | `dm_neutrino_cascade_geometry_note_2026-04-14` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 856 | 12.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 29 | `axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 854 | 14.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py` |
| 30 | `gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification_narrow_theorem_note_2026-05-17` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 854 | 13.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py` |
| 31 | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 853 | 15.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_mixed_cumulant_audit.py` |
| 32 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 852 | 22.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 33 | `rp_p2_gauge_extension_and_realization_residual_note_2026-05-28` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 843 | 15.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py` |
| 34 | `gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_theorem_note_2026-06-02` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 840 | 10.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py` |
| 35 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 828 | 12.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 36 | `cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 827 | 12.19 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cluster_decomposition_mass_gap_bridge_check.py` |
| 37 | `su3_wigner_intertwiner_block1_theorem_note_2026-05-03` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 808 | 11.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_wigner_intertwiner_engine.py` |
| 38 | `plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 803 | 13.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py` |
| 39 | `staggered_dirac_chirality_parity_bridge_narrow_theorem_note_2026-06-06` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 793 | 10.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_chirality_parity_bridge_2026_06_06.py` |
| 40 | `eta_holonomy_base_flux_scope_boundary_note_2026-06-06` | fresh_scientific_audit | positive_theorem | unaudited | critical | 792 | 10.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_eta_holonomy_base_flux_scope_boundary_2026_06_06.py` |
| 41 | `poisson_response_kernel_and_sign_normalization_finite_grid_bounded_note_2026-07-26` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 792 | 10.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py` |
| 42 | `pmns_oriented_cycle_channel_value_law_note` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 788 | 18.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_oriented_cycle_channel_value_law.py` |
| 43 | `pmns_uniform_scalar_deformation_boundary_note` | fresh_scientific_audit | positive_theorem | non_terminal_conditional | critical | 782 | 12.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_uniform_scalar_deformation_boundary.py` |
| 44 | `pmns_hw1_source_transfer_boundary_note` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 780 | 12.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_hw1_source_transfer_boundary.py` |
| 45 | `gravity_full_self_consistency_note` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 779 | 14.11 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 46 | `staggered_fermion_card_2026-04-11` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 778 | 13.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_17card_finite_scope_repair.py` |
| 47 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | fresh_scientific_audit | bounded_theorem | unaudited | critical | 777 | 18.60 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 48 | `koide_kappa_zd_action_circulant_character_decomposition_narrow_theorem_note_2026-06-05` | fresh_scientific_audit | positive_theorem | non_terminal_failed | critical | 777 | 10.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_koide_kappa_zd_action_character_2026_06_05.py` |
| 49 | `dm_leptogenesis_flavor_column_functional_theorem_note_2026-04-16` | fresh_scientific_audit | bounded_theorem | non_terminal_conditional | critical | 774 | 13.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py` |
| 50 | `ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26` | fresh_scientific_audit | positive_theorem | unaudited | critical | 765 | 18.58 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ew_higgs_gauge_mass_diagonalization.py` |

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
