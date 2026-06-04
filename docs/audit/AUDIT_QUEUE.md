# Audit Queue

**Total pending:** 1270
**Ready (all deps already at retained-grade or metadata tiers):** 58

By criticality:
- `critical`: 269
- `high`: 301
- `medium`: 325
- `leaf`: 375

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 996 | 37.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 2 | `staggered_dirac_realization_gate_note_2026-05-03` | open_gate | unaudited | critical | 965 | 32.42 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 3 | `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` | bounded_theorem | unaudited | critical | 941 | 13.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 4 | `rp_p2_gauge_extension_and_realization_residual_note_2026-05-28` | bounded_theorem | unaudited | critical | 940 | 12.38 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py` |
| 5 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | positive_theorem | unaudited | critical | 933 | 11.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 6 | `no_per_site_chirality_theorem_note_2026-05-02` | no_go | unaudited | critical | 905 | 14.82 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/no_per_site_chirality_check.py` |
| 7 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 751 | 55.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 8 | `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 135 | 16.09 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cpt_exact_real_anti_hermitian_d_exact_2026_05_10.py` |
| 9 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 937 | 29.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 10 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 936 | 14.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py` |
| 11 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 929 | 11.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 12 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 929 | 10.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 13 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 928 | 19.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 14 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 928 | 12.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 15 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 928 | 11.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 16 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 927 | 13.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 17 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 925 | 20.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 18 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 923 | 20.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 19 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 920 | 14.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 20 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 918 | 19.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 21 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 892 | 39.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 22 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 743 | 38.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 23 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 725 | 12.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 24 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 699 | 26.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 25 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 653 | 13.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 26 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 652 | 28.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 27 | `yt_boundary_theorem` | open_gate | unaudited | critical | 651 | 15.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 28 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 640 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 29 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 637 | 14.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 30 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 631 | 10.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 31 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 630 | 27.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 32 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 614 | 17.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 33 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 603 | 10.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 34 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 602 | 11.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 35 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 601 | 14.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 36 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 600 | 10.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 37 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 599 | 15.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 38 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 597 | 32.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 39 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 597 | 13.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 40 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 596 | 11.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 41 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 595 | 31.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 42 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 595 | 22.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 43 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 595 | 12.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 44 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 594 | 14.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 45 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 592 | 12.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 46 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 592 | 12.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 47 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 588 | 11.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 48 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 588 | 10.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 49 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 587 | 11.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 50 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 585 | 27.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |

## Citation cycle break targets

1 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 26 | `admitted_input_registry_tier_a_note_2026-05-23` | high | unaudited |

Full queue lives in `data/audit_queue.json`.
