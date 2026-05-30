# Audit Queue

**Total pending:** 1139
**Ready (all deps already at retained-grade or metadata tiers):** 4

By criticality:
- `critical`: 248
- `high`: 312
- `medium`: 294
- `leaf`: 285

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 896 | 20.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 2 | `abj_scale_free_chiral_u1_trace_surface_theorem_note_2026-05-30` | positive_theorem | unaudited | critical | 875 | 10.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_scale_free_chiral_u1_trace_surface.py` |
| 3 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | unaudited | critical | 874 | 10.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 4 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | positive_theorem | unaudited | critical | 796 | 10.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 5 | `abj_from_framework_action_u1_cubic_theorem_note_2026-05-30` | positive_theorem | unaudited | critical | 874 | 10.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_from_framework_action_u1_cubic.py` |
| 6 | `anomaly_forces_time_theorem` | positive_theorem | unaudited | critical | 873 | 40.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time_action_abj_closure.py` |
| 7 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 795 | 27.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 8 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 769 | 12.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 9 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 765 | 13.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 10 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 764 | 17.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 11 | `axiom_first_cpt_theorem_stretch_note_2026-04-29` | bounded_theorem | unaudited | critical | 742 | 11.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cpt_check.py` |
| 12 | `observable_principle_p1_p2_from_qubit_trace_note_2026-05-20` | bounded_theorem | unaudited | critical | 731 | 11.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_observable_principle_p1_p2_qubit_trace_2026_05_22.py` |
| 13 | `p2_phase_blindness_from_rp_transfer_trace_bridge_note_2026-05-28` | bounded_theorem | unaudited | critical | 730 | 10.01 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/p2_phase_blindness_rp_transfer_trace_bridge_2026_05_28.py` |
| 14 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 729 | 54.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 15 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 725 | 38.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 16 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 705 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 17 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 680 | 26.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 18 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 635 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 19 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 634 | 28.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 20 | `yt_boundary_theorem` | open_gate | unaudited | critical | 633 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 21 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 622 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 22 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 619 | 14.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 23 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 613 | 10.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 24 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 612 | 27.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 25 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 596 | 17.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 26 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 585 | 10.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 27 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 584 | 11.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 28 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 583 | 14.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 29 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 582 | 10.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 30 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 581 | 15.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 31 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 579 | 32.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 32 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 579 | 13.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 33 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 578 | 11.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 34 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 577 | 31.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 35 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 577 | 22.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 36 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 577 | 12.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 37 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 576 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 38 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 574 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 39 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 574 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 40 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 570 | 11.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 41 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 570 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 42 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 569 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 43 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 567 | 27.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 44 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 567 | 16.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 45 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 564 | 18.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 46 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 528 | 10.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 47 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 527 | 11.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 48 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 526 | 13.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 49 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 525 | 11.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 50 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 524 | 12.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |

Full queue lives in `data/audit_queue.json`.
