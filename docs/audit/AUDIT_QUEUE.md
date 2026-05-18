# Audit Queue

**Total pending:** 1316
**Ready (all deps already at retained-grade or metadata tiers):** 20

By criticality:
- `critical`: 801
- `high`: 33
- `medium`: 157
- `leaf`: 325

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `evolving_network_prototype_v6_note` | bounded_theorem | audit_in_progress | critical | 895 | 10.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/evolving_network_prototype_v6.py` |
| 2 | `causal_field_portability_note` | bounded_theorem | unaudited | critical | 893 | 13.30 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/causal_field_portability_probe.py` |
| 3 | `staggered_scalar_parity_lapse_coupling_external_narrow_theorem_note_2026-05-16` | bounded_theorem | unaudited | critical | 885 | 10.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_scalar_parity_lapse_coupling_external_narrow.py` |
| 4 | `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19` | bounded_theorem | unaudited | critical | 881 | 11.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py` |
| 5 | `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 881 | 11.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow.py` |
| 6 | `dm_pmns_chamber_spectral_completeness_krawczyk_certificate_note_2026-05-16` | bounded_theorem | audit_in_progress | critical | 879 | 13.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_pmns_chamber_spectral_completeness_krawczyk_certificate_2026_05_16.py` |
| 7 | `gauge_vacuum_plaquette_u1_density_sign_alternation_narrow_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 879 | 11.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.py` |
| 8 | `dm_leptogenesis_pmns_multistart_selector_support_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 879 | 10.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_multistart_selector_support.py` |
| 9 | `dm_leptogenesis_dweh_even_split_transfer_layer_note_2026-04-19` | bounded_theorem | unaudited | critical | 879 | 10.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_dweh_even_split_transfer_layer.py` |
| 10 | `wave_static_fixed_beam_boundary_sensitivity_note` | bounded_theorem | unaudited | critical | 879 | 10.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/wave_static_fixed_beam_boundary_sensitivity.py` |
| 11 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1028 | 15.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 12 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1026 | 16.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 13 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1024 | 13.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 14 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1019 | 13.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 15 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1019 | 12.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 16 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1018 | 30.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 17 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 970 | 13.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 18 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 969 | 38.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 19 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 960 | 12.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 20 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 957 | 37.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 21 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 938 | 14.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 22 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 937 | 14.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 23 | `yt_boundary_theorem` | open_gate | unaudited | critical | 935 | 16.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 24 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 932 | 17.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 25 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 929 | 14.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 26 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 921 | 10.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 27 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 920 | 11.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 28 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 919 | 14.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 29 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 918 | 11.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 30 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 917 | 47.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 31 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 917 | 16.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 32 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 915 | 13.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 33 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 914 | 12.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 34 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 913 | 12.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 35 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 912 | 14.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 36 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 911 | 12.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 37 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 910 | 30.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 38 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 910 | 18.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 39 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 910 | 13.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 40 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 910 | 13.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 41 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 907 | 13.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 42 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 906 | 11.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 43 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 906 | 11.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 44 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 905 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 45 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 903 | 16.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 46 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 903 | 12.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 47 | `gate_b_nonlabel_connectivity_v1_distance_note` | bounded_theorem | unaudited | critical | 900 | 10.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_distance.py` |
| 48 | `gate_b_nonlabel_connectivity_v1_joint_note` | bounded_theorem | unaudited | critical | 900 | 10.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_joint.py` |
| 49 | `source_resolved_propagating_green_pocket_note` | positive_theorem | unaudited | critical | 900 | 10.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_propagating_green_pocket.py` |
| 50 | `minimal_absorbing_horizon_probe_note` | bounded_theorem | unaudited | critical | 899 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_absorbing_horizon_probe.py` |

## Citation cycle break targets

186 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 891 | `coarse_grained_exterior_law_helper_note_2026-04-14` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 891 | `finite_rank_gravity_residual_helper_note_2026-04-14` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 890 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 888 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 884 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 884 | `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 884 | `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | critical | unaudited |
| 8 | `cycle-0008` | 3 | 884 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 9 | `cycle-0009` | 3 | 884 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 882 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 881 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 12 | `cycle-0012` | 2 | 880 | `scalar_trace_tensor_no_go_note` | critical | unaudited |
| 13 | `cycle-0013` | 2 | 880 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 878 | `axiom_first_sm_anomaly_cancellation_complete_downstream_fix_note_2026-05-17` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 878 | `axiom_first_stefan_boltzmann_downstream_fix_note_2026-05-17` | critical | unaudited |
| 16 | `cycle-0016` | 2 | 878 | `bminusl_anomaly_freedom_downstream_fix_note_2026-05-17` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 878 | `chronology_protection_downstream_fix_note_2026-05-17` | critical | unaudited |
| 18 | `cycle-0018` | 2 | 878 | `dm_leptogenesis_hrad_theorem_note_2026-04-16` | critical | unaudited |
| 19 | `cycle-0019` | 2 | 878 | `dm_pmns_cp_orientation_parity_reduction_note_2026-04-20` | critical | unaudited |
| 20 | `cycle-0020` | 2 | 878 | `graviton_mass_derived_note` | critical | unaudited |
| 21 | `cycle-0021` | 2 | 878 | `neutrino_mass_reduction_to_dirac_note` | critical | unaudited |
| 22 | `cycle-0022` | 2 | 878 | `s3_anomaly_spacetime_lift_downstream_fix_note_2026-05-17` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 878 | `s3_time_spacetime_tensor_primitive_downstream_fix_note_2026-05-17` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 878 | `s3_time_tensorized_schur_primitive_downstream_fix_note_2026-05-17` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 878 | `s3_time_transfer_matrix_bridge_downstream_fix_note_2026-05-17` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
