# Audit Queue

**Total pending:** 1234
**Ready (all deps already at retained-grade or metadata tiers):** 36

By criticality:
- `critical`: 757
- `high`: 35
- `medium`: 153
- `leaf`: 289

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `dimensional_gravity_table` | bounded_theorem | audit_in_progress | critical | 811 | 12.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/dimensional_gravity_table_certificate_runner_2026_05_03.py` |
| 2 | `lhcm_matter_assignment_from_su3_representation_note_2026-05-02` | positive_theorem | unaudited | critical | 810 | 11.66 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lhcm_matter_assignment.py` |
| 3 | `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 809 | 11.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cpt_exact_real_anti_hermitian_d_exact_2026_05_10.py` |
| 4 | `universal_gr_lorentzian_global_atlas_closure_note` | bounded_theorem | unaudited | critical | 808 | 20.16 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 5 | `poisson_self_gravity_loop_v3_note` | bounded_theorem | unaudited | critical | 808 | 11.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/poisson_self_gravity_loop_v3.py` |
| 6 | `su3_cubic_anomaly_cancellation_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 806 | 16.66 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 7 | `gravity_law_cleanup_note` | bounded_theorem | unaudited | critical | 805 | 11.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/gravity_distance_fixed_geometry.py` |
| 8 | `dm_abcc_signature_forcing_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 805 | 10.65 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_abcc_signature_forcing_theorem.py` |
| 9 | `wave_static_fixed_beam_boundary_sensitivity_note` | bounded_theorem | unaudited | critical | 805 | 10.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/wave_static_fixed_beam_boundary_sensitivity.py` |
| 10 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 946 | 15.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 11 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 946 | 14.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 12 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 945 | 13.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 13 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 940 | 13.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 14 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 940 | 12.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 15 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 939 | 30.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 16 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 892 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 17 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 891 | 37.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 18 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 886 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 19 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 885 | 34.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 20 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 863 | 14.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 21 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 862 | 17.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 22 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 862 | 16.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 23 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 862 | 16.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 24 | `yt_boundary_theorem` | open_gate | unaudited | critical | 862 | 16.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 25 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 862 | 15.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 26 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 862 | 14.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 27 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 862 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 28 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 862 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 29 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 862 | 13.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 30 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 862 | 13.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 31 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 862 | 12.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 32 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 862 | 12.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 33 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 862 | 12.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 34 | `yt_explicit_systematic_budget_note` | positive_theorem | unaudited | critical | 862 | 12.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_explicit_systematic_budget.py` |
| 35 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 862 | 11.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 36 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 862 | 11.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 37 | `yt_exact_interacting_bridge_transport_note` | bounded_theorem | unaudited | critical | 862 | 11.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_interacting_bridge_transport.py` |
| 38 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 862 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 39 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 862 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 40 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 862 | 10.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 41 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 853 | 13.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 42 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 839 | 46.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 43 | `gate_b_weak_connectivity_note` | bounded_theorem | unaudited | critical | 837 | 12.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_weak_connectivity_harness.py` |
| 44 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 834 | 30.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 45 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 833 | 18.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 46 | `gate_b_nonlabel_connectivity_v1_note` | bounded_theorem | unaudited | critical | 833 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_nonlabel_connectivity_v1.py` |
| 47 | `source_resolved_exact_green_pocket_note` | bounded_theorem | unaudited | critical | 830 | 12.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_pocket.py` |
| 48 | `source_resolved_exact_green_scaling_note` | bounded_theorem | unaudited | critical | 830 | 11.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_scaling.py` |
| 49 | `source_resolved_propagating_green_pocket_note` | positive_theorem | unaudited | critical | 830 | 11.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_propagating_green_pocket.py` |
| 50 | `source_resolved_exact_green_h025_pocket_note` | bounded_theorem | unaudited | critical | 830 | 10.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/source_resolved_exact_green_h025_pocket.py` |

## Citation cycle break targets

247 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 862 | `yt_bridge_action_invariant_note` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 862 | `yt_bridge_rearrangement_principle_note` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 862 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 862 | `yt_ew_coupling_bridge_note` | critical | unaudited |
| 5 | `cycle-0005` | 3 | 862 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 6 | `cycle-0006` | 3 | 862 | `yt_bridge_moment_closure_note` | critical | unaudited |
| 7 | `cycle-0007` | 3 | 862 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 8 | `cycle-0008` | 4 | 862 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 9 | `cycle-0009` | 4 | 862 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 10 | `cycle-0010` | 4 | 862 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 862 | `yt_boundary_theorem` | critical | unaudited |
| 12 | `cycle-0012` | 2 | 830 | `source_resolved_exact_green_h025_pocket_note` | critical | unaudited |
| 13 | `cycle-0013` | 2 | 830 | `source_resolved_exact_green_pocket_note` | critical | unaudited |
| 14 | `cycle-0014` | 3 | 830 | `source_resolved_exact_green_h025_pocket_note` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 822 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 16 | `cycle-0016` | 4 | 822 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 17 | `cycle-0017` | 6 | 822 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 18 | `cycle-0018` | 7 | 822 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 19 | `cycle-0019` | 8 | 822 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 20 | `cycle-0020` | 9 | 822 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 21 | `cycle-0021` | 9 | 822 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 22 | `cycle-0022` | 10 | 822 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 816 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 24 | `cycle-0024` | 2 | 807 | `lensing_finite_path_explanation_note` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 806 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
