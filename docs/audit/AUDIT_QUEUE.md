# Audit Queue

**Total pending:** 1293
**Ready (all deps already at retained-grade or metadata tiers):** 28

By criticality:
- `critical`: 779
- `high`: 34
- `medium`: 159
- `leaf`: 321

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `gauge_vacuum_plaquette_spatial_environment_tensor_transfer_theorem_note` | bounded_theorem | unaudited | critical | 1020 | 15.00 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_tensor_transfer.py` |
| 2 | `g_bare_constraint_vs_convention_theorem_note_2026-05-03` | bounded_theorem | unaudited | critical | 1020 | 11.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 3 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 951 | 17.39 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 4 | `gate_b_farfield_note` | bounded_theorem | unaudited | critical | 921 | 17.35 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_farfield_harness.py` |
| 5 | `minimal_source_driven_field_probe_note` | bounded_theorem | unaudited | critical | 909 | 12.33 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_source_driven_field_probe.py` |
| 6 | `causal_field_portability_note` | bounded_theorem | unaudited | critical | 885 | 13.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/causal_field_portability_probe.py` |
| 7 | `plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06` | bounded_theorem | unaudited | critical | 882 | 12.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py` |
| 8 | `physical_hermitian_hamiltonian_and_sme_bridge_note_2026-04-30` | bounded_theorem | unaudited | critical | 882 | 11.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_physical_hermitian_hamiltonian_and_sme_bridge.py` |
| 9 | `finite_rank_source_to_metric_theorem_note` | bounded_theorem | unaudited | critical | 877 | 11.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_finite_rank_source_to_metric_theorem.py` |
| 10 | `one_parameter_reduced_shell_law_note` | bounded_theorem | unaudited | critical | 877 | 11.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_one_parameter_reduced_shell_law.py` |
| 11 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 874 | 18.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 12 | `bh_entropy_rt_ratio_widom_no_go_note` | bounded_theorem | unaudited | critical | 872 | 14.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_bh_entropy_rt_ratio_widom.py` |
| 13 | `emergent_geometry_growth_note_2026-04-10` | bounded_theorem | unaudited | critical | 872 | 10.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_geometry.py` |
| 14 | `pmns_oriented_cycle_selection_structure_note` | bounded_theorem | unaudited | critical | 871 | 11.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_oriented_cycle_selection_structure.py` |
| 15 | `gauge_vacuum_plaquette_u1_density_sign_alternation_narrow_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 871 | 11.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.py` |
| 16 | `scalar_trace_tensor_no_go_note` | bounded_theorem | unaudited | critical | 871 | 11.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_scalar_trace_tensor_nogo.py` |
| 17 | `dm_leptogenesis_pmns_multistart_selector_support_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 871 | 10.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_multistart_selector_support.py` |
| 18 | `dm_abcc_basin_finite_search_support_note_2026-04-30` | bounded_theorem | unaudited | critical | 871 | 10.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_abcc_basin_enumeration_completeness.py` |
| 19 | `koide_a1_loop_final_status_2026-04-22` | bounded_theorem | unaudited | critical | 871 | 10.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_a1_quartic_potential_derivation.py` |
| 20 | `wave_static_fixed_beam_boundary_sensitivity_note` | bounded_theorem | unaudited | critical | 871 | 10.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/wave_static_fixed_beam_boundary_sensitivity.py` |
| 21 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1019 | 14.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 22 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1017 | 15.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 23 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1016 | 13.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 24 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1011 | 13.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 25 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1011 | 12.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 26 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1010 | 30.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 27 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 962 | 13.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 28 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 961 | 38.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 29 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 952 | 12.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 30 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 949 | 37.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 31 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 930 | 14.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 32 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 929 | 14.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 33 | `yt_boundary_theorem` | open_gate | unaudited | critical | 927 | 16.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 34 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 924 | 17.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 35 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 919 | 13.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 36 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 913 | 10.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 37 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 912 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 38 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 911 | 14.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 39 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 910 | 11.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 40 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 909 | 47.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 41 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 909 | 16.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 42 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 907 | 13.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 43 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 906 | 12.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 44 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 905 | 12.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 45 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 904 | 14.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 46 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 903 | 12.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 47 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 902 | 30.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 48 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 902 | 18.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 49 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 902 | 13.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 50 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 902 | 13.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |

## Citation cycle break targets

160 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 882 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 874 | `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 874 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 873 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 870 | `axiom_first_sm_anomaly_cancellation_complete_downstream_fix_note_2026-05-17` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 870 | `bminusl_anomaly_freedom_downstream_fix_note_2026-05-17` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 870 | `chronology_protection_downstream_fix_note_2026-05-17` | critical | unaudited |
| 8 | `cycle-0008` | 2 | 870 | `graviton_mass_derived_note` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 870 | `higgs_mass_derived_note` | critical | unaudited |
| 10 | `cycle-0010` | 2 | 870 | `neutrino_mass_reduction_to_dirac_note` | critical | unaudited |
| 11 | `cycle-0011` | 2 | 870 | `s3_anomaly_spacetime_lift_downstream_fix_note_2026-05-17` | critical | unaudited |
| 12 | `cycle-0012` | 2 | 870 | `s3_time_spacetime_tensor_primitive_downstream_fix_note_2026-05-17` | critical | unaudited |
| 13 | `cycle-0013` | 2 | 870 | `s3_time_tensorized_schur_primitive_downstream_fix_note_2026-05-17` | critical | unaudited |
| 14 | `cycle-0014` | 2 | 870 | `s3_time_transfer_matrix_bridge_downstream_fix_note_2026-05-17` | critical | unaudited |
| 15 | `cycle-0015` | 3 | 870 | `cosmological_constant_result_2026-04-12` | critical | unaudited |
| 16 | `cycle-0016` | 3 | 870 | `cosmological_constant_result_2026-04-12` | critical | unaudited |
| 17 | `cycle-0017` | 3 | 870 | `lepton_single_higgs_pmns_triviality_note` | critical | unaudited |
| 18 | `cycle-0018` | 3 | 870 | `neutrino_mass_reduction_to_dirac_note` | critical | unaudited |
| 19 | `cycle-0019` | 3 | 870 | `lh_anomaly_trace_catalog_theorem_note_2026-04-25` | critical | unaudited |
| 20 | `cycle-0020` | 4 | 870 | `cosmological_constant_result_2026-04-12` | critical | unaudited |
| 21 | `cycle-0021` | 4 | 870 | `koide_q_background_zero_z_erasure_criterion_theorem_note_2026-04-25` | critical | unaudited |
| 22 | `cycle-0022` | 4 | 870 | `lepton_single_higgs_pmns_triviality_note` | critical | unaudited |
| 23 | `cycle-0023` | 5 | 870 | `koide_q_background_zero_z_erasure_criterion_theorem_note_2026-04-25` | critical | unaudited |
| 24 | `cycle-0024` | 5 | 870 | `neutrino_mass_reduction_to_dirac_note` | critical | unaudited |
| 25 | `cycle-0025` | 5 | 870 | `lepton_single_higgs_pmns_triviality_note` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
