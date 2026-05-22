# Audit Queue

**Total pending:** 1305
**Ready (all deps already at retained-grade or metadata tiers):** 7

By criticality:
- `critical`: 850
- `high`: 28
- `medium`: 111
- `leaf`: 316

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `multisite_pauli_group_theorem_note_2026-05-02` | positive_theorem | audit_in_progress | critical | 988 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/multisite_pauli_group_check.py` |
| 2 | `q_integer_spectrum_theorem_note_2026-05-02` | positive_theorem | audit_in_progress | critical | 988 | 10.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/q_integer_spectrum_check.py` |
| 3 | `pauli_group_order_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 988 | 10.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/pauli_group_order_check.py` |
| 4 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1120 | 15.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 5 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1118 | 16.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 6 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1116 | 13.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 7 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1111 | 14.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 8 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1111 | 12.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 9 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1110 | 31.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 10 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 1063 | 14.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 11 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 1062 | 38.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 12 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 1054 | 18.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 13 | `yt_ew_matching_rule_m_note_2026-05-02` | positive_theorem | unaudited | critical | 1054 | 12.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_matching_rule_m_stretch.py` |
| 14 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | bounded_theorem | unaudited | critical | 1054 | 10.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 15 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 1053 | 12.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 16 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1052 | 38.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 17 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 1041 | 15.03 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 18 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 1040 | 14.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 19 | `yt_boundary_theorem` | open_gate | unaudited | critical | 1039 | 16.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 20 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 1036 | 18.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 21 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 1036 | 14.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 22 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 1026 | 11.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 23 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 1025 | 12.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 24 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 1024 | 15.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 25 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 1023 | 11.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 26 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 1022 | 16.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 27 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 1020 | 14.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 28 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 1019 | 12.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 29 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 1019 | 12.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 30 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 1018 | 12.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 31 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 1017 | 14.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 32 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 1016 | 47.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 33 | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 1015 | 19.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py` |
| 34 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 1015 | 13.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 35 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 1015 | 13.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 36 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 1015 | 13.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 37 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 1013 | 30.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 38 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 1012 | 12.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 39 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 1011 | 11.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 40 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 1011 | 11.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 41 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 1010 | 11.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 42 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 1009 | 18.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 43 | `gate_b_nonlabel_connectivity_v1_distance_note` | bounded_theorem | unaudited | critical | 1009 | 10.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_distance.py` |
| 44 | `gate_b_nonlabel_connectivity_v1_joint_note` | bounded_theorem | unaudited | critical | 1009 | 10.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_joint.py` |
| 45 | `source_resolved_propagating_green_pocket_note` | positive_theorem | unaudited | critical | 1009 | 10.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_propagating_green_pocket.py` |
| 46 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 1008 | 16.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 47 | `minimal_absorbing_horizon_probe_note` | bounded_theorem | unaudited | critical | 1008 | 11.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_absorbing_horizon_probe.py` |
| 48 | `source_resolved_wavefield_green_pocket_note` | positive_theorem | unaudited | critical | 1008 | 10.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_wavefield_green_pocket.py` |
| 49 | `source_resolved_wavefield_escalation_note` | bounded_theorem | unaudited | critical | 1007 | 13.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_wavefield_escalation.py` |
| 50 | `mesoscopic_surrogate_backreaction_note` | bounded_theorem | unaudited | critical | 1006 | 13.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/mesoscopic_surrogate_backreaction_harness.py` |

## Citation cycle break targets

294 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 1054 | `rconn_derived_note` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 1054 | `ew_current_matching_ozi_suppression_theorem_note_2026-04-27` | critical | unaudited |
| 3 | `cycle-0003` | 4 | 1006 | `localized_source_response_sweep_note` | critical | unaudited |
| 4 | `cycle-0004` | 5 | 1006 | `mesoscopic_surrogate_compact_floor_sweep_note` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 1000 | `coarse_grained_exterior_law_helper_note_2026-04-14` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 1000 | `finite_rank_gravity_residual_helper_note_2026-04-14` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 997 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | critical | unaudited |
| 8 | `cycle-0008` | 2 | 996 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 993 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 993 | `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 993 | `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | critical | unaudited |
| 12 | `cycle-0012` | 3 | 993 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 13 | `cycle-0013` | 3 | 993 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 991 | `koide_moment_ratio_uniformity_reduced_carrier_narrow_theorem_note_2026-05-17` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 991 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | critical | unaudited |
| 16 | `cycle-0016` | 2 | 991 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 990 | `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | critical | unaudited |
| 18 | `cycle-0018` | 2 | 990 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | critical | unaudited |
| 19 | `cycle-0019` | 2 | 990 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 20 | `cycle-0020` | 2 | 989 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |
| 21 | `cycle-0021` | 2 | 989 | `scalar_trace_tensor_no_go_note` | critical | unaudited |
| 22 | `cycle-0022` | 2 | 989 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 987 | `axiom_first_sm_anomaly_cancellation_complete_note_2026-05-17` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 987 | `axiom_first_stefan_boltzmann_note_2026-05-17` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 987 | `bminusl_anomaly_freedom_note_2026-05-17` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
