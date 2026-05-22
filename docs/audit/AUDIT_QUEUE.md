# Audit Queue

**Total pending:** 1356
**Ready (all deps already at retained-grade or metadata tiers):** 16

By criticality:
- `critical`: 909
- `high`: 23
- `medium`: 99
- `leaf`: 325

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `ew_current_fierz_channel_decomposition_note_2026-05-01` | positive_theorem | audit_in_progress | critical | 1189 | 17.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ew_current_fierz_channel_decomposition.py` |
| 2 | `lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 1123 | 13.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lh_doublet_traceless_abelian_ratio.py` |
| 3 | `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 1061 | 20.05 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cl3_per_site_uniqueness_check.py` |
| 4 | `naive_lattice_fermion_two_power_d_species_count_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 1056 | 15.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_naive_lattice_fermion_two_power_d_species_count_narrow.py` |
| 5 | `g_bare_canonical_convention_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 1056 | 13.05 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 6 | `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` | bounded_theorem | audit_in_progress | critical | 1056 | 11.05 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py` |
| 7 | `pmns_graph_first_cycle_frame_support_note` | bounded_theorem | unaudited | critical | 1055 | 12.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_graph_first_cycle_frame_support.py` |
| 8 | `pmns_graph_axis_to_active_lane_bridge_note` | bounded_theorem | unaudited | critical | 1055 | 10.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_graph_axis_to_active_lane_bridge.py` |
| 9 | `staggered_dirac_substep3_species_reduction_bridge_narrow_theorem_note_2026-05-16` | bounded_theorem | audit_in_progress | critical | 1054 | 11.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_species_reduction_bridge_2026_05_16.py` |
| 10 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 1053 | 14.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 11 | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1053 | 11.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_2026_05_17.py` |
| 12 | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 1053 | 11.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep3_bz_corner_hamming_orbit_2026_05_17.py` |
| 13 | `gauge_wilson_isotropy_boundary_note_2026-05-04` | no_go | unaudited | critical | 1052 | 10.54 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py` |
| 14 | `ew_current_matching_rule_open_gate_note_2026-05-03` | no_go | unaudited | critical | 1185 | 17.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ew_current_matching_rule_no_go.py` |
| 15 | `cl3_color_automorphism_theorem` | bounded_theorem | unaudited | critical | 1171 | 29.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 16 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1161 | 15.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 17 | `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1161 | 14.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 18 | `g_bare_constraint_vs_convention_theorem_note_2026-05-03` | bounded_theorem | unaudited | critical | 1161 | 12.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 19 | `g_bare_derivation_note` | positive_theorem | unaudited | critical | 1160 | 19.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 20 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1159 | 16.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 21 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1157 | 13.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 22 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1152 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 23 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1152 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 24 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1151 | 31.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 25 | `yt_ew_color_projection_theorem` | positive_theorem | unaudited | critical | 1130 | 35.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 26 | `yukawa_color_projection_theorem` | positive_theorem | unaudited | critical | 1125 | 17.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ew_current_fierz_channel_decomposition.py` |
| 27 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 1122 | 14.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 28 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 1121 | 38.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 29 | `left_handed_charge_matching_note` | bounded_theorem | unaudited | critical | 1119 | 28.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_graph_first_su3_integration.py` |
| 30 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 1112 | 18.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 31 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 1112 | 12.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 32 | `yt_ew_matching_rule_m_note_2026-05-02` | positive_theorem | unaudited | critical | 1112 | 12.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_matching_rule_m_stretch.py` |
| 33 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | bounded_theorem | unaudited | critical | 1112 | 10.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 34 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1111 | 38.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 35 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 1104 | 15.11 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 36 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 1103 | 14.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 37 | `yt_boundary_theorem` | open_gate | unaudited | critical | 1102 | 16.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 38 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 1101 | 14.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 39 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 1099 | 18.10 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 40 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 1089 | 11.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 41 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 1088 | 12.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 42 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 1087 | 15.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 43 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 1086 | 11.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 44 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 1085 | 16.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 45 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 1084 | 13.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 46 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 1083 | 14.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 47 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 1082 | 12.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 48 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 1081 | 13.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 49 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 1080 | 15.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 50 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 1080 | 13.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |

## Citation cycle break targets

331 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 1112 | `rconn_derived_note` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 1112 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | critical | unaudited |
| 3 | `cycle-0003` | 4 | 1071 | `localized_source_response_sweep_note` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 1071 | `mesoscopic_surrogate_compact_floor_sweep_note` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 1065 | `coarse_grained_exterior_law_helper_note_2026-04-14` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 1065 | `finite_rank_gravity_residual_helper_note_2026-04-14` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 1062 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | critical | unaudited |
| 8 | `cycle-0008` | 2 | 1059 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 1058 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 1058 | `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 1058 | `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | critical | unaudited |
| 12 | `cycle-0012` | 3 | 1058 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 13 | `cycle-0013` | 3 | 1058 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 1056 | `koide_moment_ratio_uniformity_reduced_carrier_narrow_theorem_note_2026-05-17` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 1056 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | critical | unaudited |
| 16 | `cycle-0016` | 2 | 1056 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 1055 | `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | critical | unaudited |
| 18 | `cycle-0018` | 2 | 1055 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 19 | `cycle-0019` | 2 | 1054 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 2 | 1054 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |
| 21 | `cycle-0021` | 2 | 1054 | `scalar_trace_tensor_no_go_note` | critical | unaudited |
| 22 | `cycle-0022` | 2 | 1054 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 1052 | `axiom_first_sm_anomaly_cancellation_complete_note_2026-05-17` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 1052 | `axiom_first_stefan_boltzmann_note_2026-05-17` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 1052 | `bminusl_anomaly_freedom_note_2026-05-17` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
