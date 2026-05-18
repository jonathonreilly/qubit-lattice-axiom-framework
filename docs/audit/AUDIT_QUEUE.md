# Audit Queue

**Total pending:** 1308
**Ready (all deps already at retained-grade or metadata tiers):** 6

By criticality:
- `critical`: 801
- `high`: 33
- `medium`: 155
- `leaf`: 319

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `poisson_exhaustive_uniqueness_note` | bounded_theorem | unaudited | critical | 889 | 14.80 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_poisson_exhaustive_uniqueness.py` |
| 2 | `poisson_self_gravity_born_audit_note` | bounded_theorem | unaudited | critical | 885 | 11.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/poisson_self_gravity_born_audit.py` |
| 3 | `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19` | bounded_theorem | unaudited | critical | 884 | 11.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py` |
| 4 | `dm_leptogenesis_dweh_even_split_transfer_layer_note_2026-04-19` | bounded_theorem | unaudited | critical | 882 | 10.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_dweh_even_split_transfer_layer.py` |
| 5 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1031 | 15.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 6 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1029 | 16.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 7 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1027 | 13.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 8 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1022 | 14.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 9 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1022 | 12.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 10 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1021 | 31.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 11 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 973 | 13.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 12 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 972 | 38.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 13 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 963 | 12.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 14 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 960 | 37.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 15 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 941 | 14.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 16 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 940 | 14.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 17 | `yt_boundary_theorem` | open_gate | unaudited | critical | 938 | 16.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 18 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 935 | 17.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 19 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 932 | 14.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 20 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 924 | 10.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 21 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 923 | 11.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 22 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 922 | 14.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 23 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 921 | 11.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 24 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 920 | 47.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 25 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 920 | 16.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 26 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 918 | 13.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 27 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 917 | 12.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 28 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 916 | 12.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 29 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 915 | 14.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 30 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 914 | 12.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 31 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 913 | 30.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 32 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 913 | 18.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 33 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 913 | 13.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 34 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 913 | 13.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 35 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 910 | 13.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 36 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 909 | 11.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 37 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 909 | 11.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 38 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 908 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 39 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 906 | 16.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 40 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 906 | 12.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 41 | `gate_b_nonlabel_connectivity_v1_distance_note` | bounded_theorem | unaudited | critical | 903 | 10.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_distance.py` |
| 42 | `gate_b_nonlabel_connectivity_v1_joint_note` | bounded_theorem | unaudited | critical | 903 | 10.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_joint.py` |
| 43 | `source_resolved_propagating_green_pocket_note` | positive_theorem | unaudited | critical | 903 | 10.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_propagating_green_pocket.py` |
| 44 | `minimal_absorbing_horizon_probe_note` | bounded_theorem | unaudited | critical | 902 | 11.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_absorbing_horizon_probe.py` |
| 45 | `source_resolved_wavefield_green_pocket_note` | positive_theorem | unaudited | critical | 902 | 10.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_wavefield_green_pocket.py` |
| 46 | `source_resolved_wavefield_escalation_note` | bounded_theorem | unaudited | critical | 901 | 13.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_wavefield_escalation.py` |
| 47 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 900 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 48 | `minimal_bidirectional_trapping_probe_note` | bounded_theorem | unaudited | critical | 900 | 10.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_bidirectional_trapping_probe.py` |
| 49 | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 899 | 12.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_per_site_hilbert_dim_two_check.py` |
| 50 | `retarded_field_delay_proxy_note` | bounded_theorem | unaudited | critical | 899 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/retarded_field_delay_proxy_probe.py` |

## Citation cycle break targets

189 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 894 | `coarse_grained_exterior_law_helper_note_2026-04-14` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 894 | `finite_rank_gravity_residual_helper_note_2026-04-14` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 893 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 891 | `one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 887 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 887 | `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 887 | `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | critical | unaudited |
| 8 | `cycle-0008` | 3 | 887 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 9 | `cycle-0009` | 3 | 887 | `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 885 | `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 885 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | critical | unaudited |
| 12 | `cycle-0012` | 2 | 885 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | critical | unaudited |
| 13 | `cycle-0013` | 2 | 884 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 883 | `scalar_trace_tensor_no_go_note` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 883 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | critical | unaudited |
| 16 | `cycle-0016` | 2 | 881 | `axiom_first_sm_anomaly_cancellation_complete_downstream_fix_note_2026-05-17` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 881 | `axiom_first_stefan_boltzmann_downstream_fix_note_2026-05-17` | critical | unaudited |
| 18 | `cycle-0018` | 2 | 881 | `bminusl_anomaly_freedom_downstream_fix_note_2026-05-17` | critical | unaudited |
| 19 | `cycle-0019` | 2 | 881 | `chronology_protection_downstream_fix_note_2026-05-17` | critical | unaudited |
| 20 | `cycle-0020` | 2 | 881 | `dm_leptogenesis_hrad_theorem_note_2026-04-16` | critical | unaudited |
| 21 | `cycle-0021` | 2 | 881 | `dm_pmns_cp_orientation_parity_reduction_note_2026-04-20` | critical | unaudited |
| 22 | `cycle-0022` | 2 | 881 | `graviton_mass_derived_note` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 881 | `higgs_mass_derived_note` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 881 | `neutrino_mass_reduction_to_dirac_note` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 881 | `s3_anomaly_spacetime_lift_downstream_fix_note_2026-05-17` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
