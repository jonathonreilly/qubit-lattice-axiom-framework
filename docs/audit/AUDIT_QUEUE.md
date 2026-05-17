# Audit Queue

**Total pending:** 1211
**Ready (all deps already at retained-grade or metadata tiers):** 9

By criticality:
- `critical`: 757
- `high`: 35
- `medium`: 150
- `leaf`: 269

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `left_handed_charge_matching_note` | bounded_theorem | unaudited | critical | 889 | 28.30 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_graph_first_su3_integration.py` |
| 2 | `su3_casimir_fundamental_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 830 | 18.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/su3_casimir_fundamental_check.py` |
| 3 | `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 828 | 19.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cl3_per_site_uniqueness_check.py` |
| 4 | `plaquette_v1_picard_fuchs_ode_note_2026-05-05` | bounded_theorem | unaudited | critical | 813 | 13.17 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py` |
| 5 | `wave_static_direct_probe_fine_note` | positive_theorem | unaudited | critical | 800 | 10.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/wave_static_direct_probe.py` |
| 6 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 940 | 15.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 7 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 940 | 14.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 8 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 939 | 13.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 9 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 934 | 13.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 10 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 934 | 12.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 11 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 933 | 29.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 12 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 886 | 13.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 13 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 885 | 37.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 14 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 880 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 15 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 879 | 34.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 16 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 857 | 14.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 17 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 856 | 17.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 18 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 856 | 16.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 19 | `yt_boundary_theorem` | open_gate | unaudited | critical | 856 | 16.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 20 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 856 | 16.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 21 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 856 | 15.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 22 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 856 | 14.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 23 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 856 | 13.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 24 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 856 | 13.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 25 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 856 | 13.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 26 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 856 | 13.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 27 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 856 | 12.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 28 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 856 | 12.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 29 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 856 | 12.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 30 | `yt_explicit_systematic_budget_note` | positive_theorem | unaudited | critical | 856 | 12.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_explicit_systematic_budget.py` |
| 31 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 856 | 11.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 32 | `yt_exact_interacting_bridge_transport_note` | bounded_theorem | unaudited | critical | 856 | 11.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_interacting_bridge_transport.py` |
| 33 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 856 | 11.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 34 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 856 | 11.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 35 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 856 | 11.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 36 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 856 | 10.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 37 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 848 | 13.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 38 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 834 | 46.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 39 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 832 | 12.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 40 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 829 | 30.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 41 | `g_bare_rigidity_theorem_note` | positive_theorem | unaudited | critical | 829 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 42 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 828 | 18.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 43 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 828 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 44 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 825 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 45 | `source_resolved_exact_green_scaling_note` | bounded_theorem | unaudited | critical | 825 | 11.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_scaling.py` |
| 46 | `source_resolved_propagating_green_pocket_note` | positive_theorem | unaudited | critical | 825 | 11.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_propagating_green_pocket.py` |
| 47 | `source_resolved_exact_green_h025_pocket_note` | bounded_theorem | unaudited | critical | 825 | 10.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_h025_pocket.py` |
| 48 | `gate_b_nonlabel_connectivity_v1_distance_note` | bounded_theorem | unaudited | critical | 821 | 10.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_distance.py` |
| 49 | `gate_b_nonlabel_connectivity_v1_joint_note` | bounded_theorem | unaudited | critical | 821 | 10.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_joint.py` |
| 50 | `minimal_absorbing_horizon_probe_note` | bounded_theorem | unaudited | critical | 820 | 11.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_absorbing_horizon_probe.py` |

## Citation cycle break targets

247 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 856 | `yt_bridge_action_invariant_note` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 856 | `yt_bridge_rearrangement_principle_note` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 856 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 856 | `yt_ew_coupling_bridge_note` | critical | unaudited |
| 5 | `cycle-0005` | 3 | 856 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 6 | `cycle-0006` | 3 | 856 | `yt_bridge_moment_closure_note` | critical | unaudited |
| 7 | `cycle-0007` | 3 | 856 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 8 | `cycle-0008` | 4 | 856 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 9 | `cycle-0009` | 4 | 856 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 10 | `cycle-0010` | 4 | 856 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 856 | `yt_boundary_theorem` | critical | unaudited |
| 12 | `cycle-0012` | 2 | 825 | `source_resolved_exact_green_h025_pocket_note` | critical | unaudited |
| 13 | `cycle-0013` | 2 | 825 | `source_resolved_exact_green_pocket_note` | critical | unaudited |
| 14 | `cycle-0014` | 3 | 825 | `source_resolved_exact_green_h025_pocket_note` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 817 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 16 | `cycle-0016` | 4 | 817 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 17 | `cycle-0017` | 6 | 817 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 18 | `cycle-0018` | 7 | 817 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 19 | `cycle-0019` | 8 | 817 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 20 | `cycle-0020` | 9 | 817 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 21 | `cycle-0021` | 9 | 817 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 22 | `cycle-0022` | 10 | 817 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 811 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 802 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 801 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
