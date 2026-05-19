# Audit Queue

**Total pending:** 1366
**Ready (all deps already at retained-grade or metadata tiers):** 57

By criticality:
- `critical`: 885
- `high`: 27
- `medium`: 116
- `leaf`: 338

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `equivalence_principle_harness_note` | bounded_theorem | audit_in_progress | critical | 993 | 10.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/equivalence_principle_harness.py` |
| 2 | `action_power_scaling_sweep_note` | bounded_theorem | audit_in_progress | critical | 992 | 13.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/action_power_scaling_sweep.py` |
| 3 | `decoherence_action_independence_note` | bounded_theorem | audit_in_progress | critical | 990 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/decoherence_action_independence.py` |
| 4 | `gate_b_connectivity_tolerance_note` | bounded_theorem | audit_in_progress | critical | 989 | 15.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_connectivity_tolerance.py` |
| 5 | `pmns_graph_first_cycle_frame_support_note` | bounded_theorem | audit_in_progress | critical | 989 | 12.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_graph_first_cycle_frame_support.py` |
| 6 | `growing_graph_frontier_expansion_proxy_note` | positive_theorem | audit_in_progress | critical | 988 | 14.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/growing_graph_frontier_expansion.py` |
| 7 | `poisson_self_gravity_born_audit_note` | bounded_theorem | audit_in_progress | critical | 988 | 11.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/poisson_self_gravity_born_audit.py` |
| 8 | `h0125_scalable_scout_note` | no_go | audit_in_progress | critical | 987 | 14.45 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 9 | `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19` | bounded_theorem | unaudited | critical | 987 | 11.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py` |
| 10 | `atomic_rydberg_dependency_firewall_note_2026-04-27` | positive_theorem | audit_in_progress | critical | 986 | 12.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_atomic_rydberg_dependency_firewall.py` |
| 11 | `hubble_lane5_c1_a6_bilinear_active_block_support_boundary_note_2026-04-29` | positive_theorem | audit_in_progress | critical | 986 | 11.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a6_bilinear_active_block_support_boundary.py` |
| 12 | `hubble_lane5_c1_a1_grassmann_boundary_car_obstruction_note_2026-04-29` | no_go | audit_in_progress | critical | 986 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a1_grassmann_boundary_car_obstruction.py` |
| 13 | `hubble_lane5_c1_a4_parity_gate_car_boundary_note_2026-04-29` | positive_theorem | audit_in_progress | critical | 986 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a4_parity_gate_car_boundary.py` |
| 14 | `hubble_lane5_c1_a5_boolean_coframe_restriction_obstruction_note_2026-04-29` | positive_theorem | audit_in_progress | critical | 986 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hubble_lane5_c1_a5_boolean_coframe_restriction_obstruction.py` |
| 15 | `su3_low_rank_irrep_picard_fuchs_odes_note_2026-05-05` | bounded_theorem | unaudited | critical | 986 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_low_rank_picard_fuchs_odes_2026_05_05.py` |
| 16 | `h0125_wider_w4_note` | no_go | audit_in_progress | critical | 986 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/lattice_3d_l2_wide_h0125_w4.py` |
| 17 | `persistent_object_blended_readout_outer_transfer_sweep_note_2026-04-16` | bounded_theorem | unaudited | critical | 986 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/persistent_object_blended_readout_outer_transfer_sweep.py` |
| 18 | `staggered_newton_blocking_sensitivity_note_2026-04-11` | bounded_theorem | audit_in_progress | critical | 986 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_newton_blocking_sensitivity.py` |
| 19 | `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | bounded_theorem | unaudited | critical | 985 | 16.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_frobenius_isotype_split_uniqueness.py` |
| 20 | `neutrino_lane4_dirac_seesaw_fork_no_go_note_2026-04-27` | no_go | audit_in_progress | critical | 985 | 12.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_neutrino_lane4_dirac_seesaw_fork_no_go.py` |
| 21 | `weak_coupling_retention_note_2026-04-11` | bounded_theorem | audit_in_progress | critical | 985 | 11.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_weak_coupling_retained.py` |
| 22 | `dm_abcc_basin_finite_search_support_note_2026-04-30` | bounded_theorem | unaudited | critical | 985 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_abcc_basin_enumeration_completeness.py` |
| 23 | `dm_leptogenesis_dweh_even_split_transfer_layer_note_2026-04-19` | bounded_theorem | unaudited | critical | 985 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_dweh_even_split_transfer_layer.py` |
| 24 | `gauge_wilson_isotropy_boundary_note_2026-05-04` | no_go | audit_in_progress | critical | 985 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py` |
| 25 | `scalar_selector_reviewer_package_2026-04-20` | open_gate | unaudited | critical | 985 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py` |
| 26 | `wave_static_fixed_beam_boundary_sensitivity_note` | bounded_theorem | unaudited | critical | 985 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/wave_static_fixed_beam_boundary_sensitivity.py` |
| 27 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1103 | 15.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 28 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1101 | 16.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 29 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1099 | 13.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 30 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1094 | 14.10 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 31 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1094 | 12.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 32 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1093 | 31.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 33 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 1057 | 14.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 34 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 1056 | 38.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 35 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 1047 | 17.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 36 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 1047 | 12.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 37 | `yt_ew_matching_rule_m_stretch_attempt_note_2026-05-02` | positive_theorem | unaudited | critical | 1047 | 12.03 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_matching_rule_m_stretch.py` |
| 38 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | bounded_theorem | unaudited | critical | 1047 | 10.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 39 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1046 | 38.03 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 40 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 1037 | 15.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 41 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 1036 | 14.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 42 | `yt_boundary_theorem` | open_gate | unaudited | critical | 1035 | 16.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 43 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 1033 | 14.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 44 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 1032 | 18.01 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 45 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 1022 | 11.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 46 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 1021 | 12.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 47 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 1020 | 15.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 48 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 1019 | 11.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 49 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 1018 | 16.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 50 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 1016 | 13.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |

## Citation cycle break targets

297 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 1047 | `rconn_derived_note` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 1047 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | critical | unaudited |
| 3 | `cycle-0003` | 4 | 1003 | `localized_source_response_sweep_note` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 1003 | `mesoscopic_surrogate_compact_floor_sweep_note` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 997 | `coarse_grained_exterior_law_helper_note_2026-04-14` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 997 | `finite_rank_gravity_residual_helper_note_2026-04-14` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 994 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | critical | unaudited |
| 8 | `cycle-0008` | 2 | 991 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 990 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 990 | `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 990 | `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | critical | unaudited |
| 12 | `cycle-0012` | 3 | 990 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 13 | `cycle-0013` | 3 | 990 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 988 | `koide_moment_ratio_uniformity_reduced_carrier_narrow_theorem_note_2026-05-17` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 988 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | critical | unaudited |
| 16 | `cycle-0016` | 2 | 988 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 987 | `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | critical | unaudited |
| 18 | `cycle-0018` | 2 | 987 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 19 | `cycle-0019` | 2 | 986 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 20 | `cycle-0020` | 2 | 986 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |
| 21 | `cycle-0021` | 2 | 986 | `scalar_trace_tensor_no_go_note` | critical | unaudited |
| 22 | `cycle-0022` | 2 | 986 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 984 | `axiom_first_sm_anomaly_cancellation_complete_downstream_fix_note_2026-05-17` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 984 | `axiom_first_stefan_boltzmann_downstream_fix_note_2026-05-17` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 984 | `bminusl_anomaly_freedom_downstream_fix_note_2026-05-17` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
