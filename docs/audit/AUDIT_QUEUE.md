# Audit Queue

**Total pending:** 1135
**Ready (all deps already at retained-grade or metadata tiers):** 3

By criticality:
- `critical`: 250
- `high`: 295
- `medium`: 297
- `leaf`: 293

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 922 | 27.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 2 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 913 | 11.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 3 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 912 | 16.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 4 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 910 | 19.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 5 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 910 | 12.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 6 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 909 | 13.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 7 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 908 | 20.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 8 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 903 | 13.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 9 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 901 | 18.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 10 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 883 | 39.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 11 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 734 | 38.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 12 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 715 | 12.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 13 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 690 | 26.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 14 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 644 | 28.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 15 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 644 | 13.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 16 | `yt_boundary_theorem` | open_gate | unaudited | critical | 642 | 15.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 17 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 631 | 11.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 18 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 628 | 14.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 19 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 622 | 10.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 20 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 621 | 27.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 21 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 605 | 17.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 22 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 594 | 10.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 23 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 593 | 11.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 24 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 592 | 14.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 25 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 591 | 10.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 26 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 590 | 15.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 27 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 588 | 32.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 28 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 588 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 29 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 587 | 11.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 30 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 586 | 31.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 31 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 586 | 22.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 32 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 586 | 12.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 33 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 585 | 14.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 34 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 583 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 35 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 583 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 36 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 579 | 11.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 37 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 579 | 10.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 38 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 578 | 11.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 39 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 576 | 27.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 40 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 576 | 16.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 41 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 573 | 18.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 42 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 537 | 10.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 43 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 536 | 11.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 44 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 535 | 13.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 45 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 534 | 11.06 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 46 | `s3_anomaly_spacetime_lift_note` | open_gate | unaudited | critical | 530 | 14.05 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 47 | `universal_gr_tensor_variational_candidate_note` | bounded_theorem | unaudited | critical | 530 | 13.55 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 48 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 530 | 11.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |
| 49 | `yt_p1_i_s_revision_verification_note_2026-04-17` | positive_theorem | unaudited | critical | 530 | 10.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_revision_verification.py` |
| 50 | `universal_gr_tensor_quotient_uniqueness_note` | bounded_theorem | unaudited | critical | 529 | 12.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_universal_gr_tensor_quotient_uniqueness.py` |

Full queue lives in `data/audit_queue.json`.
