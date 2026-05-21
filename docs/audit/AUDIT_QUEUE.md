# Audit Queue

**Total pending:** 1326
**Ready (all deps already at retained-grade or metadata tiers):** 22

By criticality:
- `critical`: 870
- `high`: 27
- `medium`: 109
- `leaf`: 320

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 1000 | 17.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cl3_faithful_irrep_dim_two_exact_2026_05_10.py` |
| 2 | `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29` | bounded_theorem | audit_in_progress | critical | 991 | 19.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cl3_per_site_uniqueness_check.py` |
| 3 | `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19` | bounded_theorem | unaudited | critical | 972 | 11.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py` |
| 4 | `hubble_lane5_c1_a1_grassmann_boundary_car_obstruction_note_2026-04-29` | no_go | audit_in_progress | critical | 971 | 10.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a1_grassmann_boundary_car_obstruction.py` |
| 5 | `hubble_lane5_c1_a4_parity_gate_car_boundary_note_2026-04-29` | positive_theorem | audit_in_progress | critical | 971 | 10.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a4_parity_gate_car_boundary.py` |
| 6 | `hubble_lane5_c1_a5_boolean_coframe_restriction_obstruction_note_2026-04-29` | positive_theorem | audit_in_progress | critical | 971 | 10.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a5_boolean_coframe_restriction_obstruction.py` |
| 7 | `su3_low_rank_irrep_picard_fuchs_odes_note_2026-05-05` | bounded_theorem | audit_in_progress | critical | 971 | 10.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_low_rank_picard_fuchs_odes_2026_05_05.py` |
| 8 | `h0125_wider_replay_note` | no_go | audit_in_progress | critical | 971 | 10.43 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/lattice_3d_l2_wide_h0125_replay.py` |
| 9 | `neutrino_lane4_dirac_seesaw_fork_no_go_note_2026-04-27` | no_go | audit_in_progress | critical | 970 | 12.42 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_neutrino_lane4_dirac_seesaw_fork_no_go.py` |
| 10 | `weak_coupling_retention_note_2026-04-11` | bounded_theorem | audit_in_progress | critical | 970 | 11.42 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_weak_coupling_retained.py` |
| 11 | `dm_leptogenesis_dweh_even_split_transfer_layer_note_2026-04-19` | bounded_theorem | unaudited | critical | 970 | 10.42 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_dweh_even_split_transfer_layer.py` |
| 12 | `gauge_wilson_isotropy_boundary_note_2026-05-04` | no_go | audit_in_progress | critical | 970 | 10.42 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py` |
| 13 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1102 | 15.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 14 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1100 | 16.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 15 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1098 | 13.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 16 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1093 | 14.10 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 17 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1093 | 12.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 18 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1092 | 31.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 19 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 1045 | 14.03 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 20 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 1044 | 38.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 21 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 1036 | 18.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 22 | `yt_ew_matching_rule_m_note_2026-05-02` | positive_theorem | unaudited | critical | 1036 | 12.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_matching_rule_m_stretch.py` |
| 23 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | bounded_theorem | unaudited | critical | 1036 | 10.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 24 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 1035 | 12.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 25 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1034 | 38.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 26 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 1023 | 15.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 27 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 1022 | 14.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 28 | `yt_boundary_theorem` | open_gate | unaudited | critical | 1021 | 16.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 29 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 1018 | 17.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 30 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 1018 | 14.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 31 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 1008 | 10.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 32 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 1007 | 11.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 33 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 1006 | 14.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 34 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 1005 | 11.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 35 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 1004 | 16.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 36 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 1002 | 13.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 37 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 1001 | 12.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 38 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 1001 | 12.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 39 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 1000 | 12.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 40 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 999 | 14.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 41 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 998 | 47.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 42 | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 997 | 19.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py` |
| 43 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 997 | 13.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 44 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 997 | 13.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 45 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 997 | 13.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 46 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 995 | 30.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 47 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 994 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 48 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 993 | 11.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 49 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 993 | 11.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 50 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 992 | 11.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |

## Citation cycle break targets

294 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 1036 | `rconn_derived_note` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 1036 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | critical | unaudited |
| 3 | `cycle-0003` | 4 | 988 | `localized_source_response_sweep_note` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 988 | `mesoscopic_surrogate_compact_floor_sweep_note` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 982 | `coarse_grained_exterior_law_helper_note_2026-04-14` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 982 | `finite_rank_gravity_residual_helper_note_2026-04-14` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 979 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | critical | unaudited |
| 8 | `cycle-0008` | 2 | 978 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 975 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 975 | `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 975 | `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | critical | unaudited |
| 12 | `cycle-0012` | 3 | 975 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 13 | `cycle-0013` | 3 | 975 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 973 | `koide_moment_ratio_uniformity_reduced_carrier_narrow_theorem_note_2026-05-17` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 973 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | critical | unaudited |
| 16 | `cycle-0016` | 2 | 973 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 972 | `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | critical | unaudited |
| 18 | `cycle-0018` | 2 | 972 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 19 | `cycle-0019` | 2 | 972 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 20 | `cycle-0020` | 2 | 971 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |
| 21 | `cycle-0021` | 2 | 971 | `scalar_trace_tensor_no_go_note` | critical | unaudited |
| 22 | `cycle-0022` | 2 | 971 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 969 | `axiom_first_sm_anomaly_cancellation_complete_note_2026-05-17` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 969 | `axiom_first_stefan_boltzmann_note_2026-05-17` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 969 | `bminusl_anomaly_freedom_note_2026-05-17` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
