# Audit Queue

**Total pending:** 1307
**Ready (all deps already at retained-grade or metadata tiers):** 6

By criticality:
- `critical`: 881
- `high`: 21
- `medium`: 97
- `leaf`: 308

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `naive_lattice_fermion_two_power_d_species_count_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 1055 | 15.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_naive_lattice_fermion_two_power_d_species_count_narrow.py` |
| 2 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | bounded_theorem | audit_in_progress | critical | 1055 | 11.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 3 | `staggered_dirac_substep3_species_reduction_bridge_narrow_theorem_note_2026-05-16` | bounded_theorem | audit_in_progress | critical | 1053 | 11.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_species_reduction_bridge_2026_05_16.py` |
| 4 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1052 | 11.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 5 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1052 | 11.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 6 | `gauge_wilson_isotropy_boundary_note_2026-05-04` | no_go | unaudited | critical | 1051 | 10.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py` |
| 7 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1160 | 15.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 8 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1158 | 16.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 9 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1156 | 13.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 10 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1151 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 11 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1151 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 12 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1150 | 31.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 13 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 1121 | 14.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 14 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 1120 | 38.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 15 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 1111 | 18.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 16 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 1111 | 12.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 17 | `yt_ew_matching_rule_m_note_2026-05-02` | positive_theorem | unaudited | critical | 1111 | 12.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_matching_rule_m_stretch.py` |
| 18 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | bounded_theorem | unaudited | critical | 1111 | 10.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 19 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1110 | 38.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 20 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 1103 | 15.11 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 21 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 1102 | 14.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 22 | `yt_boundary_theorem` | open_gate | unaudited | critical | 1101 | 16.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 23 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 1100 | 14.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 24 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 1098 | 18.10 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 25 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 1088 | 11.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 26 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 1087 | 12.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 27 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 1086 | 15.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 28 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 1085 | 11.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 29 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 1084 | 16.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 30 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 1083 | 13.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 31 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 1082 | 14.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 32 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 1081 | 12.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 33 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 1080 | 13.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 34 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 1079 | 15.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 35 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 1079 | 13.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 36 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 1077 | 13.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 37 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 1077 | 13.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 38 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 1076 | 12.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 39 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 1073 | 11.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 40 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 1073 | 11.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 41 | `gate_b_nonlabel_connectivity_v1_distance_note` | bounded_theorem | unaudited | critical | 1073 | 11.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_distance.py` |
| 42 | `gate_b_nonlabel_connectivity_v1_joint_note` | bounded_theorem | unaudited | critical | 1073 | 11.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_joint.py` |
| 43 | `source_resolved_propagating_green_pocket_note` | positive_theorem | unaudited | critical | 1073 | 11.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_propagating_green_pocket.py` |
| 44 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 1072 | 12.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 45 | `minimal_absorbing_horizon_probe_note` | bounded_theorem | unaudited | critical | 1072 | 11.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_absorbing_horizon_probe.py` |
| 46 | `source_resolved_wavefield_green_pocket_note` | positive_theorem | unaudited | critical | 1072 | 11.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_wavefield_green_pocket.py` |
| 47 | `source_resolved_wavefield_escalation_note` | bounded_theorem | unaudited | critical | 1071 | 13.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_wavefield_escalation.py` |
| 48 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 1070 | 17.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 49 | `mesoscopic_surrogate_backreaction_note` | bounded_theorem | unaudited | critical | 1070 | 13.56 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/mesoscopic_surrogate_backreaction_harness.py` |
| 50 | `broad_surrogate_point_source_compare_note` | bounded_theorem | unaudited | critical | 1070 | 13.06 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/broad_surrogate_point_source_compare.py` |

## Citation cycle break targets

331 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 1111 | `rconn_derived_note` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 1111 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | critical | unaudited |
| 3 | `cycle-0003` | 4 | 1070 | `localized_source_response_sweep_note` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 1070 | `mesoscopic_surrogate_compact_floor_sweep_note` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 1064 | `coarse_grained_exterior_law_helper_note_2026-04-14` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 1064 | `finite_rank_gravity_residual_helper_note_2026-04-14` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 1061 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | critical | unaudited |
| 8 | `cycle-0008` | 2 | 1058 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 1057 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 1057 | `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 1057 | `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | critical | unaudited |
| 12 | `cycle-0012` | 3 | 1057 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 13 | `cycle-0013` | 3 | 1057 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 1055 | `koide_moment_ratio_uniformity_reduced_carrier_narrow_theorem_note_2026-05-17` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 1055 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | critical | unaudited |
| 16 | `cycle-0016` | 2 | 1055 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 1054 | `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | critical | unaudited |
| 18 | `cycle-0018` | 2 | 1054 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 19 | `cycle-0019` | 2 | 1053 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 2 | 1053 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |
| 21 | `cycle-0021` | 2 | 1053 | `scalar_trace_tensor_no_go_note` | critical | unaudited |
| 22 | `cycle-0022` | 2 | 1053 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 1051 | `axiom_first_sm_anomaly_cancellation_complete_note_2026-05-17` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 1051 | `axiom_first_stefan_boltzmann_note_2026-05-17` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 1051 | `bminusl_anomaly_freedom_note_2026-05-17` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
