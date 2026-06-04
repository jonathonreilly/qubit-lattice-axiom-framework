# Audit Queue

**Total pending:** 1230
**Ready (all deps already at retained-grade or metadata tiers):** 31

By criticality:
- `critical`: 265
- `high`: 300
- `medium`: 319
- `leaf`: 346

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 994 | 37.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 2 | `staggered_dirac_realization_gate_note_2026-05-03` | open_gate | unaudited | critical | 963 | 32.41 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 3 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | positive_theorem | unaudited | critical | 931 | 11.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 4 | `no_per_site_chirality_theorem_note_2026-05-02` | no_go | unaudited | critical | 903 | 14.82 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/no_per_site_chirality_check.py` |
| 5 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 749 | 55.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 6 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 935 | 29.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 7 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 934 | 14.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py` |
| 8 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 927 | 11.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 9 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 927 | 10.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 10 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 926 | 19.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 11 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 926 | 12.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 12 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 926 | 11.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 13 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 925 | 13.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 14 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 923 | 20.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 15 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 921 | 20.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 16 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 918 | 14.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 17 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 916 | 19.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 18 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 890 | 39.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 19 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 741 | 38.03 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 20 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 723 | 12.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 21 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 697 | 26.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 22 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 651 | 13.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 23 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 650 | 28.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 24 | `yt_boundary_theorem` | open_gate | unaudited | critical | 649 | 15.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 25 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 638 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 26 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 635 | 14.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 27 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 629 | 10.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 28 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 628 | 27.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 29 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 612 | 17.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 30 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 601 | 10.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 31 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 600 | 11.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 32 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 599 | 14.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 33 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 598 | 10.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 34 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 597 | 15.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 35 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 595 | 32.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 36 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 595 | 13.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 37 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 594 | 11.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 38 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 593 | 31.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 39 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 593 | 22.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 40 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 593 | 12.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 41 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 592 | 14.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 42 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 590 | 12.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 43 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 590 | 12.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 44 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 586 | 11.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 45 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 586 | 10.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 46 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 585 | 11.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 47 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 583 | 27.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 48 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 583 | 16.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 49 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 580 | 18.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 50 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 544 | 10.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |

## Citation cycle break targets

1 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 24 | `admitted_input_registry_tier_a_note_2026-05-23` | high | unaudited |

Full queue lives in `data/audit_queue.json`.
