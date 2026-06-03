# Audit Queue

**Total pending:** 1178
**Ready (all deps already at retained-grade or metadata tiers):** 26

By criticality:
- `critical`: 300
- `high`: 247
- `medium`: 300
- `leaf`: 331

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 970 | 29.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 2 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 964 | 19.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 3 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 964 | 11.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 4 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 961 | 20.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 5 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 959 | 20.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 6 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 958 | 12.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 7 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 957 | 13.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 8 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 951 | 14.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 9 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 946 | 18.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 10 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 929 | 39.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 11 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 869 | 38.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 12 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 847 | 26.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 13 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 834 | 28.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 14 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 811 | 14.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 15 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 811 | 12.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 16 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 811 | 12.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 17 | `yt_boundary_theorem` | open_gate | unaudited | critical | 809 | 16.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 18 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 809 | 14.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 19 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 806 | 17.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 20 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 805 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 21 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 804 | 11.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 22 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 803 | 14.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 23 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 803 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 24 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 802 | 28.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 25 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 802 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 26 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 801 | 16.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 27 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 799 | 13.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 28 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 798 | 12.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 29 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 797 | 12.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 30 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 796 | 14.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 31 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 794 | 13.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 32 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 794 | 13.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 33 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 790 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 34 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 790 | 11.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 35 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 789 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 36 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 788 | 17.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 37 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 782 | 32.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 38 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 780 | 31.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 39 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 780 | 23.11 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 40 | `yt_explicit_systematic_budget_note` | positive_theorem | unaudited | critical | 778 | 11.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_explicit_systematic_budget.py` |
| 41 | `cl3_sm_embedding_theorem` | positive_theorem | unaudited | critical | 776 | 27.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 42 | `bminusl_anomaly_freedom_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 772 | 17.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_bminusl_anomaly_freedom.py` |
| 43 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 770 | 28.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 44 | `quark_projector_ray_phase_completion_note_2026-04-18` | bounded_theorem | unaudited | critical | 767 | 15.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_projector_ray_phase_completion.py` |
| 45 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 766 | 19.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 46 | `quark_projector_parameter_audit_note_2026-04-19` | bounded_theorem | unaudited | critical | 765 | 20.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_projector_parameter_audit.py` |
| 47 | `ckm_nlo_barred_triangle_protected_gamma_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 762 | 23.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_nlo_barred_triangle_protected_gamma.py` |
| 48 | `axiom_first_cpt_theorem_stretch_note_2026-04-29` | bounded_theorem | unaudited | critical | 757 | 11.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cpt_check.py` |
| 49 | `neutrino_majorana_operator_axiom_first_note` | positive_theorem | unaudited | critical | 753 | 17.56 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_neutrino_majorana_operator.py` |
| 50 | `axiom_first_kms_condition_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 753 | 14.06 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_kms_condition_check.py` |

## Citation cycle break targets

29 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 2 | `cycle-0002` | 7 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 3 | `cycle-0003` | 9 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 4 | `cycle-0004` | 14 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 5 | `cycle-0005` | 14 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 6 | `cycle-0006` | 14 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 7 | `cycle-0007` | 15 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 8 | `cycle-0008` | 17 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 9 | `cycle-0009` | 18 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 10 | `cycle-0010` | 18 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 11 | `cycle-0011` | 19 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 12 | `cycle-0012` | 19 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 13 | `cycle-0013` | 19 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 14 | `cycle-0014` | 20 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 15 | `cycle-0015` | 20 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 16 | `cycle-0016` | 20 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 17 | `cycle-0017` | 20 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 18 | `cycle-0018` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 19 | `cycle-0019` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 20 | `cycle-0020` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 21 | `cycle-0021` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 22 | `cycle-0022` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 23 | `cycle-0023` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 24 | `cycle-0024` | 22 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 25 | `cycle-0025` | 23 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
