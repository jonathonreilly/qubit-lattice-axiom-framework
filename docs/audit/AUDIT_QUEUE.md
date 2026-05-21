# Audit Queue

**Total pending:** 1318
**Ready (all deps already at retained-grade or metadata tiers):** 12

By criticality:
- `critical`: 867
- `high`: 27
- `medium`: 109
- `leaf`: 315

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19` | bounded_theorem | unaudited | critical | 975 | 11.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py` |
| 2 | `hubble_lane5_c1_a4_parity_gate_car_boundary_note_2026-04-29` | positive_theorem | audit_in_progress | critical | 974 | 10.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a4_parity_gate_car_boundary.py` |
| 3 | `hubble_lane5_c1_a5_boolean_coframe_restriction_obstruction_note_2026-04-29` | positive_theorem | audit_in_progress | critical | 974 | 10.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a5_boolean_coframe_restriction_obstruction.py` |
| 4 | `su3_low_rank_irrep_picard_fuchs_odes_note_2026-05-05` | bounded_theorem | audit_in_progress | critical | 974 | 10.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_low_rank_picard_fuchs_odes_2026_05_05.py` |
| 5 | `h0125_wider_replay_note` | no_go | audit_in_progress | critical | 974 | 10.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/lattice_3d_l2_wide_h0125_replay.py` |
| 6 | `neutrino_lane4_dirac_seesaw_fork_no_go_note_2026-04-27` | no_go | audit_in_progress | critical | 973 | 12.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_neutrino_lane4_dirac_seesaw_fork_no_go.py` |
| 7 | `weak_coupling_retention_note_2026-04-11` | bounded_theorem | audit_in_progress | critical | 973 | 11.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_weak_coupling_retained.py` |
| 8 | `dm_leptogenesis_dweh_even_split_transfer_layer_note_2026-04-19` | bounded_theorem | unaudited | critical | 973 | 10.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_dweh_even_split_transfer_layer.py` |
| 9 | `gauge_wilson_isotropy_boundary_note_2026-05-04` | no_go | audit_in_progress | critical | 973 | 10.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py` |
| 10 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1105 | 15.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 11 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1103 | 16.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 12 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1101 | 13.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 13 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1096 | 14.10 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 14 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1096 | 12.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 15 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1095 | 31.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 16 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 1048 | 14.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 17 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 1047 | 38.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 18 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 1039 | 18.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 19 | `yt_ew_matching_rule_m_note_2026-05-02` | positive_theorem | unaudited | critical | 1039 | 12.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_matching_rule_m_stretch.py` |
| 20 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | bounded_theorem | unaudited | critical | 1039 | 10.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 21 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 1038 | 12.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 22 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1037 | 38.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 23 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 1026 | 15.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 24 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 1025 | 14.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 25 | `yt_boundary_theorem` | open_gate | unaudited | critical | 1024 | 16.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 26 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 1021 | 18.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 27 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 1021 | 14.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 28 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 1011 | 10.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 29 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 1010 | 11.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 30 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 1009 | 14.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 31 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 1008 | 11.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 32 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 1007 | 16.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 33 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 1005 | 13.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 34 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 1004 | 12.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 35 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 1004 | 12.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 36 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 1003 | 12.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 37 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 1002 | 14.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 38 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 1001 | 47.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 39 | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 1000 | 19.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py` |
| 40 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 1000 | 13.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 41 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 1000 | 13.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 42 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 1000 | 13.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 43 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 998 | 30.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 44 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 997 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 45 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 996 | 11.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 46 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 996 | 11.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 47 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 995 | 11.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 48 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 994 | 18.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 49 | `gate_b_nonlabel_connectivity_v1_distance_note` | bounded_theorem | unaudited | critical | 994 | 10.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_distance.py` |
| 50 | `gate_b_nonlabel_connectivity_v1_joint_note` | bounded_theorem | unaudited | critical | 994 | 10.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_joint.py` |

## Citation cycle break targets

294 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 1039 | `rconn_derived_note` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 1039 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | critical | unaudited |
| 3 | `cycle-0003` | 4 | 991 | `localized_source_response_sweep_note` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 991 | `mesoscopic_surrogate_compact_floor_sweep_note` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 985 | `coarse_grained_exterior_law_helper_note_2026-04-14` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 985 | `finite_rank_gravity_residual_helper_note_2026-04-14` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 982 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | critical | unaudited |
| 8 | `cycle-0008` | 2 | 981 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 978 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 978 | `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 978 | `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | critical | unaudited |
| 12 | `cycle-0012` | 3 | 978 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 13 | `cycle-0013` | 3 | 978 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 976 | `koide_moment_ratio_uniformity_reduced_carrier_narrow_theorem_note_2026-05-17` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 976 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | critical | unaudited |
| 16 | `cycle-0016` | 2 | 976 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 975 | `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | critical | unaudited |
| 18 | `cycle-0018` | 2 | 975 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 19 | `cycle-0019` | 2 | 975 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 20 | `cycle-0020` | 2 | 974 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |
| 21 | `cycle-0021` | 2 | 974 | `scalar_trace_tensor_no_go_note` | critical | unaudited |
| 22 | `cycle-0022` | 2 | 974 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 972 | `axiom_first_sm_anomaly_cancellation_complete_note_2026-05-17` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 972 | `axiom_first_stefan_boltzmann_note_2026-05-17` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 972 | `bminusl_anomaly_freedom_note_2026-05-17` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
