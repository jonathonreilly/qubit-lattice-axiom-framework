# Audit Queue

**Total pending:** 1229
**Ready (all deps already at retained-grade or metadata tiers):** 30

By criticality:
- `critical`: 310
- `high`: 256
- `medium`: 317
- `leaf`: 346

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1016 | 37.49 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 2 | `staggered_dirac_realization_gate_note_2026-05-03` | open_gate | unaudited | critical | 994 | 32.46 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 3 | `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | positive_theorem | unaudited | critical | 972 | 11.93 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/tensor_product_translation_fermion_operator_bridge_check_2026_05_25.py` |
| 4 | `no_per_site_chirality_theorem_note_2026-05-02` | no_go | unaudited | critical | 944 | 14.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/no_per_site_chirality_check.py` |
| 5 | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 767 | 15.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/per_site_su2_spin_half_check.py` |
| 6 | `axiom_first_z_n_equivariant_spectral_asymmetry_narrow_theorem_note_2026-05-26` | bounded_theorem | unaudited | critical | 755 | 13.56 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py` |
| 7 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 973 | 29.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 8 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 973 | 14.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py` |
| 9 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 968 | 11.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 10 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 967 | 19.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 11 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 967 | 11.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 12 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 966 | 10.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 13 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 965 | 12.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 14 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 964 | 20.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 15 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 964 | 13.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 16 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 962 | 20.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 17 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 957 | 14.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 18 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 956 | 19.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 19 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 932 | 39.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 20 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 872 | 38.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 21 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 850 | 26.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 22 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 837 | 28.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 23 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 814 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 24 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 814 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 25 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 814 | 12.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 26 | `yt_boundary_theorem` | open_gate | unaudited | critical | 812 | 16.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 27 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 812 | 14.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 28 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 809 | 17.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 29 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 808 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 30 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 807 | 11.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 31 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 806 | 14.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 32 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 806 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 33 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 805 | 28.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 34 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 805 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 35 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 804 | 16.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 36 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 802 | 13.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 37 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 801 | 12.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 38 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 800 | 12.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 39 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 799 | 14.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 40 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 797 | 13.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 41 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 797 | 13.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 42 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 793 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 43 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 793 | 11.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 44 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 792 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 45 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 791 | 17.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 46 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 785 | 32.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 47 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 783 | 31.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 48 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 783 | 23.11 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 49 | `yt_explicit_systematic_budget_note` | positive_theorem | unaudited | critical | 781 | 11.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_explicit_systematic_budget.py` |
| 50 | `cl3_sm_embedding_theorem` | positive_theorem | unaudited | critical | 779 | 27.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |

## Citation cycle break targets

29 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 2 | `cycle-0002` | 7 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 3 | `cycle-0003` | 9 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 4 | `cycle-0004` | 14 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 5 | `cycle-0005` | 14 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 6 | `cycle-0006` | 14 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 7 | `cycle-0007` | 15 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 8 | `cycle-0008` | 17 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 9 | `cycle-0009` | 18 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 10 | `cycle-0010` | 18 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 11 | `cycle-0011` | 19 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 12 | `cycle-0012` | 19 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 13 | `cycle-0013` | 19 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 14 | `cycle-0014` | 20 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 15 | `cycle-0015` | 20 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 16 | `cycle-0016` | 20 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 17 | `cycle-0017` | 20 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 18 | `cycle-0018` | 21 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 19 | `cycle-0019` | 21 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 20 | `cycle-0020` | 21 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 21 | `cycle-0021` | 21 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 22 | `cycle-0022` | 21 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 23 | `cycle-0023` | 21 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 24 | `cycle-0024` | 22 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 25 | `cycle-0025` | 23 | 748 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
