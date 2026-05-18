# Audit Queue

**Total pending:** 1260
**Ready (all deps already at retained-grade or metadata tiers):** 5

By criticality:
- `critical`: 752
- `high`: 34
- `medium`: 156
- `leaf`: 318

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `gauge_vacuum_plaquette_u1_density_sign_alternation_narrow_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 868 | 11.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.py` |
| 2 | `dm_leptogenesis_pmns_multistart_selector_support_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 868 | 10.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_multistart_selector_support.py` |
| 3 | `wave_static_fixed_beam_boundary_sensitivity_note` | bounded_theorem | unaudited | critical | 868 | 10.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/wave_static_fixed_beam_boundary_sensitivity.py` |
| 4 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1016 | 14.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 5 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1014 | 15.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 6 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1013 | 13.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 7 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1008 | 13.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 8 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1008 | 12.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 9 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1007 | 30.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 10 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 959 | 13.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 11 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 958 | 38.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 12 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 949 | 12.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 13 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 946 | 37.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 14 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 927 | 14.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 15 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 926 | 14.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 16 | `yt_boundary_theorem` | open_gate | unaudited | critical | 924 | 16.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 17 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 921 | 17.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 18 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 916 | 13.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 19 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 910 | 10.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 20 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 909 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 21 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 908 | 14.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 22 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 907 | 11.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 23 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 906 | 47.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 24 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 906 | 16.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 25 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 904 | 13.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 26 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 903 | 12.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 27 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 902 | 12.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 28 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 901 | 14.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 29 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 900 | 12.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 30 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 899 | 30.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 31 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 899 | 18.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 32 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 899 | 13.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 33 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 899 | 13.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 34 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 896 | 13.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 35 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 895 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 36 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 895 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 37 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 894 | 11.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 38 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 892 | 16.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 39 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 892 | 12.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 40 | `gate_b_nonlabel_connectivity_v1_distance_note` | bounded_theorem | unaudited | critical | 889 | 10.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_distance.py` |
| 41 | `gate_b_nonlabel_connectivity_v1_joint_note` | bounded_theorem | unaudited | critical | 889 | 10.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_joint.py` |
| 42 | `source_resolved_propagating_green_pocket_note` | positive_theorem | unaudited | critical | 889 | 10.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_propagating_green_pocket.py` |
| 43 | `minimal_absorbing_horizon_probe_note` | bounded_theorem | unaudited | critical | 888 | 11.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_absorbing_horizon_probe.py` |
| 44 | `source_resolved_wavefield_green_pocket_note` | positive_theorem | unaudited | critical | 888 | 10.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_wavefield_green_pocket.py` |
| 45 | `source_resolved_wavefield_escalation_note` | bounded_theorem | unaudited | critical | 887 | 13.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_wavefield_escalation.py` |
| 46 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 886 | 13.79 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 47 | `minimal_bidirectional_trapping_probe_note` | bounded_theorem | unaudited | critical | 886 | 10.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_bidirectional_trapping_probe.py` |
| 48 | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 885 | 12.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_per_site_hilbert_dim_two_check.py` |
| 49 | `retarded_field_delay_proxy_note` | bounded_theorem | unaudited | critical | 885 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/retarded_field_delay_proxy_probe.py` |
| 50 | `gauge_vacuum_plaquette_spatial_environment_transfer_underdetermination_note_2026-04-17` | no_go | unaudited | critical | 885 | 10.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py` |

## Citation cycle break targets

157 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 879 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 870 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 867 | `axiom_first_sm_anomaly_cancellation_complete_downstream_fix_note_2026-05-17` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 867 | `bminusl_anomaly_freedom_downstream_fix_note_2026-05-17` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 867 | `chronology_protection_downstream_fix_note_2026-05-17` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 867 | `graviton_mass_derived_note` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 867 | `neutrino_mass_reduction_to_dirac_note` | critical | unaudited |
| 8 | `cycle-0008` | 2 | 867 | `s3_anomaly_spacetime_lift_downstream_fix_note_2026-05-17` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 867 | `s3_time_spacetime_tensor_primitive_downstream_fix_note_2026-05-17` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 867 | `s3_time_tensorized_schur_primitive_downstream_fix_note_2026-05-17` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 867 | `s3_time_transfer_matrix_bridge_downstream_fix_note_2026-05-17` | critical | unaudited |
| 12 | `cycle-0012` | 3 | 867 | `cosmological_constant_result_2026-04-12` | critical | unaudited |
| 13 | `cycle-0013` | 3 | 867 | `cosmological_constant_result_2026-04-12` | critical | unaudited |
| 14 | `cycle-0014` | 3 | 867 | `lepton_single_higgs_pmns_triviality_note` | critical | unaudited |
| 15 | `cycle-0015` | 3 | 867 | `neutrino_mass_reduction_to_dirac_note` | critical | unaudited |
| 16 | `cycle-0016` | 3 | 867 | `lh_anomaly_trace_catalog_theorem_note_2026-04-25` | critical | unaudited |
| 17 | `cycle-0017` | 4 | 867 | `cosmological_constant_result_2026-04-12` | critical | unaudited |
| 18 | `cycle-0018` | 4 | 867 | `koide_q_background_zero_z_erasure_criterion_theorem_note_2026-04-25` | critical | unaudited |
| 19 | `cycle-0019` | 4 | 867 | `lepton_single_higgs_pmns_triviality_note` | critical | unaudited |
| 20 | `cycle-0020` | 5 | 867 | `koide_q_background_zero_z_erasure_criterion_theorem_note_2026-04-25` | critical | unaudited |
| 21 | `cycle-0021` | 5 | 867 | `neutrino_mass_reduction_to_dirac_note` | critical | unaudited |
| 22 | `cycle-0022` | 5 | 867 | `lepton_single_higgs_pmns_triviality_note` | critical | unaudited |
| 23 | `cycle-0023` | 5 | 867 | `universal_gr_a1_invariant_section_note` | critical | unaudited |
| 24 | `cycle-0024` | 6 | 867 | `lepton_single_higgs_pmns_triviality_note` | critical | unaudited |
| 25 | `cycle-0025` | 6 | 867 | `lepton_single_higgs_pmns_triviality_note` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
