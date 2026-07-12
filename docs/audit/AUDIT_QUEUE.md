# Audit Queue

**Total pending:** 2970
**Ready (all deps at retained-grade/metadata tiers or supplied axioms/approved primitives):** 616

By criticality:
- `critical`: 672
- `high`: 352
- `medium`: 775
- `leaf`: 1171

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_complexification_split_narrow_theorem_note_2026-05-10` | positive_theorem | unaudited | critical | 1696 | 25.73 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_complexification_split_exact_2026_05_10.py` |
| 2 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1686 | 18.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_pauli_irrep_uniqueness_exact_2026_05_10.py` |
| 3 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 1554 | 19.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 4 | `z2_hw1_mass_matrix_parametrization_note` | positive_theorem | unaudited | critical | 1382 | 19.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z2_hw1_mass_matrix_parametrization.py` |
| 5 | `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | positive_theorem | audit_in_progress | critical | 1377 | 14.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_mass_matrix_no_go.py` |
| 6 | `hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25` | bounded_theorem | unaudited | critical | 1322 | 11.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/hypercharge_alpha_third_normalization_runner.py` |
| 7 | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1319 | 14.37 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_clifford_volume_chirality_even_dimension_exact.py` |
| 8 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | unaudited | critical | 1317 | 12.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 9 | `abj_p_comp_scale_free_singlet_completion_classification_note_2026-06-18` | bounded_theorem | unaudited | critical | 1310 | 10.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py` |
| 10 | `abj_p_rec_spintaste_clifford_core_bridge_note_2026-06-18` | bounded_theorem | unaudited | critical | 1310 | 10.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_prec_spintaste_clifford_core_bridge_2026_06_18.py` |
| 11 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | unaudited | critical | 1191 | 18.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 12 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | unaudited | critical | 1185 | 15.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 13 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | positive_theorem | unaudited | critical | 1170 | 18.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 14 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1168 | 50.19 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py` |
| 15 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 1153 | 15.67 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 16 | `oh_schur_boundary_action_note` | positive_theorem | unaudited | critical | 1143 | 19.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_oh_schur_boundary_action.py` |
| 17 | `s3_boundary_link_theorem_note` | bounded_theorem | unaudited | critical | 1140 | 14.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_boundary_link_theorem.py` |
| 18 | `flavor_carrier_momentum_type_from_translation_theorem_note_2026-06-15` | bounded_theorem | unaudited | critical | 1108 | 11.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py` |
| 19 | `koide_circulant_character_bridge_narrow_theorem_note_2026-05-09` | positive_theorem | unaudited | critical | 1104 | 25.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_circulant_character_bridge_narrow.py` |
| 20 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 1101 | 18.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 21 | `staggered_os0_supplied_action_ks_blocking_four_taste_module_narrow_theorem_note_2026-07-11` | bounded_theorem | unaudited | critical | 1088 | 10.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py` |
| 22 | `physical_lattice_necessity_note` | no_go | unaudited | critical | 1081 | 22.08 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_lattice_necessity.py` |
| 23 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | unaudited | critical | 1049 | 12.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 24 | `tensor_support_center_excess_law_note` | bounded_theorem | unaudited | critical | 1021 | 19.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_tensor_support_center_excess_law.py` |
| 25 | `rconn_derived_note` | no_go | unaudited | critical | 961 | 24.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rconn_matching_rule_nogo_certificate.py` |
| 26 | `yt_color_projection_correction_note` | no_go | unaudited | critical | 941 | 17.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 27 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 894 | 20.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_taste_abstract_c8_orbit_scope_2026_06_12.py` |
| 28 | `yt_ew_color_projection_theorem` | no_go | unaudited | critical | 883 | 32.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_kappa_family_nogo_certificate.py` |
| 29 | `alpha_lm_geometric_mean_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 835 | 24.71 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_lm_geometric_mean_identity.py` |
| 30 | `unit_singlet_overlap_narrow_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 828 | 12.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_unit_singlet_overlap_narrow.py` |
| 31 | `hierarchy_matsubara_decomposition_note` | positive_theorem | unaudited | critical | 825 | 15.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_matsubara_decomposition.py` |
| 32 | `ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26` | bounded_theorem | unaudited | critical | 822 | 22.18 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ew_higgs_gauge_mass_diagonalization.py` |
| 33 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | unaudited | critical | 802 | 10.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 34 | `dm_neutrino_weak_vector_theorem_note_2026-04-15` | bounded_theorem | unaudited | critical | 797 | 10.64 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_weak_vector_theorem.py` |
| 35 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | bounded_theorem | unaudited | critical | 796 | 13.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py` |
| 36 | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | open_gate | unaudited | critical | 774 | 14.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py` |
| 37 | `higgs_mechanism_note` | bounded_theorem | unaudited | critical | 756 | 12.56 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_higgs_quartic_mechanism_algebra_repair.py` |
| 38 | `dm_neutrino_cascade_geometry_note_2026-04-14` | positive_theorem | unaudited | critical | 746 | 12.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_cascade_geometry.py` |
| 39 | `charged_lepton_two_higgs_canonical_reduction_note` | positive_theorem | unaudited | critical | 733 | 16.52 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_charged_lepton_two_higgs_canonical_reduction.py` |
| 40 | `cpt_exact_note` | positive_theorem | unaudited | critical | 724 | 31.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cpt_exact.py` |
| 41 | `wilson_small_a_matching_beta_gbare_narrow_theorem_note_2026-06-07` | bounded_theorem | unaudited | critical | 706 | 13.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py` |
| 42 | `dm_neutrino_odd_circulant_z2_slot_theorem_note_2026-04-15` | positive_theorem | unaudited | critical | 705 | 11.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py` |
| 43 | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 701 | 17.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_three_generation_hw1_distinct_characters_exact.py` |
| 44 | `strong_cp_theta_zero_note` | bounded_theorem | unaudited | critical | 694 | 24.44 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_strong_cp_theta_zero.py` |
| 45 | `dm_neutrino_z3_circulant_mass_basis_no_go_note_2026-04-15` | no_go | unaudited | critical | 693 | 10.94 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_neutrino_z3_circulant_mass_basis_nogo.py` |
| 46 | `pmns_oriented_cycle_channel_value_law_note` | positive_theorem | unaudited | critical | 674 | 18.40 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_oriented_cycle_channel_value_law.py` |
| 47 | `pmns_uniform_scalar_deformation_boundary_note` | positive_theorem | unaudited | critical | 667 | 12.38 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_uniform_scalar_deformation_boundary.py` |
| 48 | `pmns_hw1_source_transfer_boundary_note` | bounded_theorem | unaudited | critical | 665 | 11.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_hw1_source_transfer_boundary.py` |
| 49 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | bounded_theorem | unaudited | critical | 663 | 17.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 50 | `dm_leptogenesis_flavor_column_functional_theorem_note_2026-04-16` | bounded_theorem | unaudited | critical | 659 | 12.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py` |

## Citation cycle break targets

49 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 509 | `quark_cp_carrier_completion_note_2026-04-18` | critical | audited_numerical_match |
| 2 | `cycle-0002` | 2 | 467 | `bridge_gap_hk_cube_perron_note_2026-05-06` | critical | unaudited |
| 3 | `cycle-0003` | 3 | 467 | `bridge_gap_action_form_uniqueness_no_go_note_2026-05-06` | critical | unaudited |
| 4 | `cycle-0004` | 3 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 5 | `cycle-0005` | 11 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 6 | `cycle-0006` | 12 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 7 | `cycle-0007` | 13 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 8 | `cycle-0008` | 13 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 9 | `cycle-0009` | 13 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 10 | `cycle-0010` | 13 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 11 | `cycle-0011` | 13 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 12 | `cycle-0012` | 13 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 13 | `cycle-0013` | 13 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 14 | `cycle-0014` | 14 | 421 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 14 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 16 | `cycle-0016` | 14 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 17 | `cycle-0017` | 14 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 18 | `cycle-0018` | 14 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 19 | `cycle-0019` | 15 | 421 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 20 | `cycle-0020` | 15 | 421 | `a3_route2_single_clock_c3_obstruction_note_2026-05-08_r2` | critical | unaudited |
| 21 | `cycle-0021` | 15 | 421 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 22 | `cycle-0022` | 15 | 421 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 23 | `cycle-0023` | 15 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 24 | `cycle-0024` | 15 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |
| 25 | `cycle-0025` | 15 | 421 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
