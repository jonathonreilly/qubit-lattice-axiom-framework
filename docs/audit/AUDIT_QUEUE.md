# Audit Queue

**Total pending:** 1355
**Ready (all deps already at retained-grade or metadata tiers):** 111

By criticality:
- `critical`: 282
- `high`: 303
- `medium`: 356
- `leaf`: 414

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1026 | 38.00 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 2 | `staggered_dirac_realization_gate_note_2026-05-03` | open_gate | unaudited | critical | 990 | 35.95 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 3 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | bounded_theorem | unaudited | critical | 963 | 13.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 4 | `rp_p2_gauge_extension_and_realization_residual_note_2026-05-28` | bounded_theorem | unaudited | critical | 962 | 12.41 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py` |
| 5 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | positive_theorem | unaudited | critical | 956 | 12.40 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 6 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 953 | 18.40 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 7 | `no_per_site_chirality_theorem_note_2026-05-02` | no_go | unaudited | critical | 927 | 14.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/no_per_site_chirality_check.py` |
| 8 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 771 | 56.09 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 9 | `axiom_first_lattice_noether_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 261 | 14.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_lattice_noether_check.py` |
| 10 | `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 145 | 16.69 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cpt_exact_real_anti_hermitian_d_exact_2026_05_10.py` |
| 11 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 963 | 15.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py` |
| 12 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 959 | 29.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 13 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 953 | 10.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 14 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 951 | 12.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 15 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 951 | 11.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 16 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 950 | 19.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 17 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 950 | 13.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 18 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 950 | 11.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 19 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 947 | 20.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 20 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 945 | 20.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 21 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 943 | 15.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 22 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 941 | 20.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 23 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 914 | 39.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 24 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 764 | 38.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 25 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 745 | 12.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 26 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 719 | 26.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 27 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 674 | 13.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 28 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 672 | 28.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 29 | `yt_boundary_theorem` | open_gate | unaudited | critical | 672 | 15.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 30 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 659 | 11.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 31 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 656 | 14.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 32 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 650 | 10.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 33 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 649 | 27.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 34 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 634 | 17.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 35 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 623 | 10.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 36 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 622 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 37 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 621 | 14.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 38 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 620 | 10.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 39 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 619 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 40 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 617 | 13.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 41 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 616 | 32.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 42 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 616 | 11.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 43 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 615 | 12.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 44 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 614 | 31.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 45 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 614 | 22.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 46 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 614 | 14.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 47 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 612 | 12.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 48 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 612 | 12.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 49 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 608 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 50 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 608 | 10.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |

Full queue lives in `data/audit_queue.json`.
