# Audit Queue

**Total pending:** 1142
**Ready (all deps already at retained-grade or metadata tiers):** 8

By criticality:
- `critical`: 246
- `high`: 311
- `medium`: 294
- `leaf`: 291

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | bounded_theorem | unaudited | critical | 951 | 10.39 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 2 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 950 | 27.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 3 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 943 | 17.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 4 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 938 | 12.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 5 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 937 | 13.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 6 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 902 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 7 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 901 | 10.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 8 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 900 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 9 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 899 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 10 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 898 | 16.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 11 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 897 | 19.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 12 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 895 | 20.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 13 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 892 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 14 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 890 | 18.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 15 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 872 | 39.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 16 | `axiom_first_cpt_theorem_stretch_note_2026-04-29` | bounded_theorem | unaudited | critical | 742 | 11.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cpt_check.py` |
| 17 | `observable_principle_p1_p2_from_qubit_trace_note_2026-05-20` | bounded_theorem | unaudited | critical | 731 | 11.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_observable_principle_p1_p2_qubit_trace_2026_05_22.py` |
| 18 | `p2_phase_blindness_from_rp_transfer_trace_bridge_note_2026-05-28` | bounded_theorem | unaudited | critical | 730 | 10.01 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/p2_phase_blindness_rp_transfer_trace_bridge_2026_05_28.py` |
| 19 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 729 | 54.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 20 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 725 | 38.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 21 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 705 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 22 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 680 | 26.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 23 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 635 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 24 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 634 | 28.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 25 | `yt_boundary_theorem` | open_gate | unaudited | critical | 633 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 26 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 622 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 27 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 619 | 14.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 28 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 613 | 10.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 29 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 612 | 27.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 30 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 596 | 17.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 31 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 585 | 10.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 32 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 584 | 11.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 33 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 583 | 14.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 34 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 582 | 10.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 35 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 581 | 15.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 36 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 579 | 32.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 37 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 579 | 13.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 38 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 578 | 11.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 39 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 577 | 31.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 40 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 577 | 22.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 41 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 577 | 12.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 42 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 576 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 43 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 574 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 44 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 574 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 45 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 570 | 11.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 46 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 570 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 47 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 569 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 48 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 567 | 27.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 49 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 567 | 16.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 50 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 564 | 18.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |

Full queue lives in `data/audit_queue.json`.
