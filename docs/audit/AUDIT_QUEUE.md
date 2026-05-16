# Audit Queue

**Total pending:** 1206
**Ready (all deps already at retained-grade or metadata tiers):** 10

By criticality:
- `critical`: 749
- `high`: 34
- `medium`: 154
- `leaf`: 269

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `dark_energy_eos_note` | decoration | unaudited | critical | 788 | 11.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dark_energy_eos.py` |
| 2 | `koide_delta_marked_relative_cobordism_no_go_note_2026-04-24` | no_go | audit_in_progress | critical | 788 | 11.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_delta_marked_relative_cobordism_no_go.py` |
| 3 | `koide_q_bridge_single_primitive_note_2026-04-22` | positive_theorem | unaudited | critical | 788 | 10.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_q_bridge_single_primitive.py` |
| 4 | `dm_leptogenesis_pmns_relative_action_stationarity_theorem_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 788 | 10.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py` |
| 5 | `hadron_lane1_b2_dynamical_screening_boundary_note_2026-04-29` | no_go | audit_in_progress | critical | 788 | 10.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hadron_lane1_b2_dynamical_screening_boundary.py` |
| 6 | `nonlinear_born_gravity_note` | bounded_theorem | unaudited | critical | 788 | 10.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_nonlinear_born_gravity.py` |
| 7 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 928 | 14.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 8 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 927 | 13.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 9 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 922 | 13.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 10 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 922 | 12.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 11 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 921 | 29.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 12 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 874 | 13.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 13 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 873 | 37.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 14 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 868 | 11.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 15 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 867 | 34.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 16 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 845 | 14.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 17 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 844 | 17.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 18 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 844 | 16.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 19 | `yt_boundary_theorem` | open_gate | unaudited | critical | 844 | 16.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 20 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 844 | 16.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 21 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 844 | 15.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 22 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 844 | 14.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 23 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 844 | 13.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 24 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 844 | 13.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 25 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 844 | 13.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 26 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 844 | 13.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 27 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 844 | 12.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 28 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 844 | 12.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 29 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 844 | 12.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 30 | `yt_explicit_systematic_budget_note` | positive_theorem | unaudited | critical | 844 | 12.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_explicit_systematic_budget.py` |
| 31 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 844 | 11.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 32 | `yt_exact_interacting_bridge_transport_note` | bounded_theorem | unaudited | critical | 844 | 11.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_interacting_bridge_transport.py` |
| 33 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 844 | 11.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 34 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 844 | 11.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 35 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 844 | 11.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 36 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 844 | 10.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 37 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 836 | 13.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 38 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 822 | 46.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 39 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 820 | 12.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 40 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 817 | 30.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 41 | `g_bare_rigidity_theorem_note` | positive_theorem | unaudited | critical | 817 | 13.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 42 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 816 | 18.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 43 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 816 | 13.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 44 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 813 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 45 | `source_resolved_exact_green_scaling_note` | bounded_theorem | unaudited | critical | 813 | 11.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_scaling.py` |
| 46 | `source_resolved_propagating_green_pocket_note` | positive_theorem | unaudited | critical | 813 | 11.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_propagating_green_pocket.py` |
| 47 | `source_resolved_exact_green_h025_pocket_note` | bounded_theorem | unaudited | critical | 813 | 10.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_h025_pocket.py` |
| 48 | `gate_b_nonlabel_connectivity_v1_distance_note` | bounded_theorem | unaudited | critical | 809 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_distance.py` |
| 49 | `gate_b_nonlabel_connectivity_v1_joint_note` | bounded_theorem | unaudited | critical | 809 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1_joint.py` |
| 50 | `minimal_absorbing_horizon_probe_note` | bounded_theorem | unaudited | critical | 808 | 11.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/minimal_absorbing_horizon_probe.py` |

## Citation cycle break targets

242 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 844 | `yt_bridge_action_invariant_note` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 844 | `yt_bridge_rearrangement_principle_note` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 844 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 844 | `yt_ew_coupling_bridge_note` | critical | unaudited |
| 5 | `cycle-0005` | 3 | 844 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 6 | `cycle-0006` | 3 | 844 | `yt_bridge_moment_closure_note` | critical | unaudited |
| 7 | `cycle-0007` | 3 | 844 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 8 | `cycle-0008` | 4 | 844 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 9 | `cycle-0009` | 4 | 844 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 10 | `cycle-0010` | 4 | 844 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 844 | `yt_boundary_theorem` | critical | unaudited |
| 12 | `cycle-0012` | 2 | 813 | `source_resolved_exact_green_h025_pocket_note` | critical | unaudited |
| 13 | `cycle-0013` | 2 | 813 | `source_resolved_exact_green_pocket_note` | critical | unaudited |
| 14 | `cycle-0014` | 3 | 813 | `source_resolved_exact_green_h025_pocket_note` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 16 | `cycle-0016` | 4 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 17 | `cycle-0017` | 6 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 18 | `cycle-0018` | 7 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 19 | `cycle-0019` | 8 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 20 | `cycle-0020` | 9 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 21 | `cycle-0021` | 9 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 22 | `cycle-0022` | 10 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 799 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | audited_conditional |
| 24 | `cycle-0024` | 2 | 794 | `pmns_active_four_real_source_from_transport_note` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 790 | `lensing_finite_path_explanation_note` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
