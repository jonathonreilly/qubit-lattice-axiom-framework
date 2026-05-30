# Audit Queue

**Total pending:** 1138
**Ready (all deps already at retained-grade or metadata tiers):** 2

By criticality:
- `critical`: 250
- `high`: 311
- `medium`: 294
- `leaf`: 283

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `single_clock_root_audit_unblock_packet_note_2026-05-30` | bounded_theorem | unaudited | critical | 898 | 10.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_single_clock_root_audit_unblock_packet.py` |
| 2 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | unaudited | critical | 875 | 11.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 3 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 952 | 27.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 4 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 945 | 17.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 5 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 940 | 12.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 6 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 939 | 13.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 7 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 904 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 8 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 903 | 10.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 9 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 902 | 11.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 10 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 901 | 15.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 11 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 900 | 16.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 12 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 899 | 19.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 13 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 897 | 20.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 14 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 894 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 15 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 892 | 18.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 16 | `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem | unaudited | critical | 876 | 10.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py` |
| 17 | `anomaly_forces_time_theorem` | positive_theorem | unaudited | critical | 874 | 40.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time_action_abj_closure.py` |
| 18 | `abj_from_framework_action_u1_cubic_theorem_note_2026-05-30` | positive_theorem | unaudited | critical | 874 | 10.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_from_framework_action_u1_cubic.py` |
| 19 | `abj_standard_theorem_bridge_for_anomaly_forces_time_note_2026-05-30` | bounded_theorem | unaudited | critical | 874 | 10.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_standard_theorem_bridge_for_anomaly_forces_time.py` |
| 20 | `axiom_first_cpt_theorem_stretch_note_2026-04-29` | bounded_theorem | unaudited | critical | 742 | 11.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cpt_check.py` |
| 21 | `observable_principle_p1_p2_from_qubit_trace_note_2026-05-20` | bounded_theorem | unaudited | critical | 731 | 11.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_observable_principle_p1_p2_qubit_trace_2026_05_22.py` |
| 22 | `p2_phase_blindness_from_rp_transfer_trace_bridge_note_2026-05-28` | bounded_theorem | unaudited | critical | 730 | 10.01 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/p2_phase_blindness_rp_transfer_trace_bridge_2026_05_28.py` |
| 23 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 729 | 54.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 24 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 725 | 38.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 25 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 705 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 26 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 680 | 26.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 27 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 635 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 28 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 634 | 28.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 29 | `yt_boundary_theorem` | open_gate | unaudited | critical | 633 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 30 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 622 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 31 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 619 | 14.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 32 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 613 | 10.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 33 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 612 | 27.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 34 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 596 | 17.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 35 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 585 | 10.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 36 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 584 | 11.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 37 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 583 | 14.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 38 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 582 | 10.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 39 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 581 | 15.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 40 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 579 | 32.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 41 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 579 | 13.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 42 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 578 | 11.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 43 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 577 | 31.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 44 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 577 | 22.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 45 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 577 | 12.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 46 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 576 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 47 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 574 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 48 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 574 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 49 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 570 | 11.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 50 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 570 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |

## Citation cycle break targets

2 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 874 | `abj_from_framework_action_u1_cubic_theorem_note_2026-05-30` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 874 | `abj_from_framework_action_u1_cubic_theorem_note_2026-05-30` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
