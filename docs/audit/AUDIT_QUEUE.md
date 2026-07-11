# Audit Queue

**Total pending:** 2891
**Ready (all deps at retained-grade/metadata tiers or supplied axioms/approved primitives):** 600

By criticality:
- `critical`: 652
- `high`: 334
- `medium`: 756
- `leaf`: 1149

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem | non_terminal_conditional | critical | 1682 | 18.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 2 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | non_terminal_failed | critical | 1552 | 19.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 3 | `hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25` | bounded_theorem | non_terminal_conditional | critical | 1320 | 11.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/hypercharge_alpha_third_normalization_runner.py` |
| 4 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 1317 | 14.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 5 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | audit_in_progress | critical | 1315 | 12.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 6 | `abj_p_comp_scale_free_singlet_completion_classification_note_2026-06-18` | bounded_theorem | audit_in_progress | critical | 1312 | 11.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py` |
| 7 | `abj_p_rec_spintaste_clifford_core_bridge_note_2026-06-18` | bounded_theorem | audit_in_progress | critical | 1312 | 11.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_prec_spintaste_clifford_core_bridge_2026_06_18.py` |
| 8 | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 1293 | 24.34 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py` |
| 9 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1192 | 18.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 10 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1186 | 15.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 11 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | positive_theorem | unaudited | critical | 1171 | 18.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 12 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1154 | 15.67 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 13 | `oh_schur_boundary_action_note` | positive_theorem | unaudited | critical | 1144 | 19.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_oh_schur_boundary_action.py` |
| 14 | `s3_boundary_link_theorem_note` | bounded_theorem | non_terminal_conditional | critical | 1141 | 14.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 15 | `koide_circulant_character_bridge_narrow_theorem_note_2026-05-09` | positive_theorem | unaudited | critical | 1105 | 25.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_character_bridge_narrow.py` |
| 16 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 1102 | 18.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 17 | `staggered_os0_supplied_action_ks_blocking_four_taste_module_narrow_theorem_note_2026-07-11` | bounded_theorem | non_terminal_conditional | critical | 1089 | 10.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py` |
| 18 | `physical_lattice_necessity_note` | no_go | unaudited | critical | 1082 | 22.58 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_lattice_necessity.py` |
| 19 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | unaudited | critical | 1050 | 12.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 20 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 895 | 20.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_taste_abstract_c8_orbit_scope_2026_06_12.py` |
| 21 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | positive_theorem | audit_in_progress | critical | 829 | 12.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 22 | `hierarchy_matsubara_decomposition_note` | bounded_theorem | non_terminal_conditional | critical | 826 | 15.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 23 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | unaudited | critical | 803 | 10.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 24 | `dm_neutrino_dirac_bridge_theorem_note_2026-04-15` | positive_theorem | audit_in_progress | critical | 797 | 18.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_dirac_bridge_theorem.py` |
| 25 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | bounded_theorem | non_terminal_conditional | critical | 797 | 13.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py` |
| 26 | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | open_gate | non_terminal_conditional | critical | 775 | 14.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py` |
| 27 | `higgs_mechanism_note` | bounded_theorem | unaudited | critical | 757 | 12.57 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_higgs_quartic_mechanism_algebra_repair.py` |
| 28 | `dm_neutrino_cascade_geometry_note_2026-04-14` | bounded_theorem | non_terminal_conditional | critical | 747 | 12.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 29 | `charged_lepton_two_higgs_canonical_reduction_note` | positive_theorem | non_terminal_conditional | critical | 734 | 16.52 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_charged_lepton_two_higgs_canonical_reduction.py` |
| 30 | `cpt_exact_note` | positive_theorem | non_terminal_failed | critical | 725 | 31.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cpt_exact.py` |
| 31 | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 702 | 17.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_three_generation_hw1_distinct_characters_exact.py` |
| 32 | `dm_neutrino_z3_circulant_mass_basis_no_go_note_2026-04-15` | no_go | unaudited | critical | 694 | 10.94 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_z3_circulant_mass_basis_nogo.py` |
| 33 | `pmns_uniform_scalar_deformation_boundary_note` | no_go | non_terminal_conditional | critical | 668 | 12.39 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_uniform_scalar_deformation_boundary.py` |
| 34 | `pmns_hw1_source_transfer_boundary_note` | bounded_theorem | unaudited | critical | 666 | 11.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_hw1_source_transfer_boundary.py` |
| 35 | `dm_leptogenesis_flavor_column_functional_theorem_note_2026-04-16` | bounded_theorem | unaudited | critical | 660 | 12.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py` |
| 36 | `rp_p2_gauge_extension_and_realization_residual_note_2026-05-28` | bounded_theorem | non_terminal_conditional | critical | 639 | 15.82 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py` |
| 37 | `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10` | positive_theorem | non_terminal_failed | critical | 636 | 14.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow.py` |
| 38 | `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | bounded_theorem | unaudited | critical | 633 | 11.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep1_u4_conditional_single_module_2026_05_17.py` |
| 39 | `gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_theorem_note_2026-06-02` | bounded_theorem | audit_in_progress | critical | 622 | 11.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py` |
| 40 | `yt_ew_m_residual_note_2026-05-02` | no_go | non_terminal_conditional | critical | 622 | 10.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_m_residual_channel_check.py` |
| 41 | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | positive_theorem | non_terminal_failed | critical | 619 | 26.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py` |
| 42 | `cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09` | bounded_theorem | non_terminal_conditional | critical | 615 | 11.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cluster_decomposition_mass_gap_bridge_check.py` |
| 43 | `axiom_first_spectrum_condition_blocked_time_normalization_bridge_narrow_theorem_note_2026-06-05` | bounded_theorem | non_terminal_conditional | critical | 602 | 11.74 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spectrum_condition_blocked_time_normalization_2026_06_05.py` |
| 44 | `gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note` | bounded_theorem | non_terminal_failed | critical | 598 | 23.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py` |
| 45 | `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 580 | 22.18 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py` |
| 46 | `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | no_go | unaudited | critical | 580 | 14.18 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_dirac_substep1_statistics_agnostic_no_forcing_discriminator.py` |
| 47 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem | audit_in_progress | critical | 574 | 13.17 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py` |
| 48 | `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 567 | 30.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_q_two_thirds_algebraic_narrow.py` |
| 49 | `gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_note_2026-06-07` | positive_theorem | audit_in_progress | critical | 567 | 10.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_2026_06_07.py` |
| 50 | `gauge_vacuum_plaquette_constant_lift_obstruction_note` | no_go | audit_in_progress | critical | 564 | 13.64 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_constant_lift_obstruction.py` |

## Citation cycle break targets

49 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 510 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 2 | 468 | `bridge_gap_hk_cube_perron_note_2026-05-06` | critical | unaudited |
| 3 | `cycle-0003` | 3 | 468 | `bridge_gap_action_form_uniqueness_no_go_note_2026-05-06` | critical | unaudited |
| 4 | `cycle-0004` | 3 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 5 | `cycle-0005` | 11 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 6 | `cycle-0006` | 12 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 7 | `cycle-0007` | 13 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 8 | `cycle-0008` | 13 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 9 | `cycle-0009` | 13 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 10 | `cycle-0010` | 13 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 11 | `cycle-0011` | 13 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 12 | `cycle-0012` | 13 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 13 | `cycle-0013` | 13 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 14 | `cycle-0014` | 14 | 422 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 14 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 16 | `cycle-0016` | 14 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 17 | `cycle-0017` | 14 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 18 | `cycle-0018` | 14 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 19 | `cycle-0019` | 15 | 422 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 20 | `cycle-0020` | 15 | 422 | `a3_route2_single_clock_c3_obstruction_note_2026-05-08_r2` | critical | unaudited |
| 21 | `cycle-0021` | 15 | 422 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 22 | `cycle-0022` | 15 | 422 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 23 | `cycle-0023` | 15 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 24 | `cycle-0024` | 15 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 25 | `cycle-0025` | 15 | 422 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
