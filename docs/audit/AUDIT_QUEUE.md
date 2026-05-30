# Audit Queue

**Total pending:** 1227
**Ready (all deps already at retained-grade or metadata tiers):** 81

By criticality:
- `critical`: 259
- `high`: 303
- `medium`: 312
- `leaf`: 353

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 914 | 17.84 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 2 | `lorentz_boost_covariance_3plus1d_theorem_note` | bounded_theorem | unaudited | critical | 911 | 14.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 3 | `no_per_site_chirality_theorem_note_2026-05-02` | no_go | unaudited | critical | 888 | 13.80 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/no_per_site_chirality_check.py` |
| 4 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 738 | 54.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 5 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | bounded_theorem | unaudited | critical | 536 | 12.07 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py` |
| 6 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | bounded_theorem | unaudited | critical | 395 | 16.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 7 | `koide_cl3_selector_gap_note_2026-04-19` | open_gate | audit_in_progress | critical | 254 | 9.49 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 8 | `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | no_go | audit_in_progress | critical | 115 | 14.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_frobenius_isotype_split_uniqueness.py` |
| 9 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 921 | 27.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 10 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 912 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 11 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 911 | 16.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 12 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 910 | 16.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 13 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 909 | 19.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 14 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 909 | 12.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 15 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 908 | 13.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 16 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 907 | 20.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 17 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 902 | 13.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 18 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 900 | 18.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 19 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 882 | 39.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 20 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 734 | 38.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 21 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 714 | 12.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 22 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 690 | 26.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 23 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 644 | 28.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 24 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 644 | 13.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 25 | `yt_boundary_theorem` | open_gate | unaudited | critical | 642 | 15.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 26 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 631 | 11.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 27 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 628 | 14.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 28 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 622 | 10.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 29 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 621 | 27.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 30 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 605 | 17.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 31 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 594 | 10.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 32 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 593 | 11.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 33 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 592 | 14.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 34 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 591 | 10.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 35 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 590 | 15.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 36 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 588 | 32.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 37 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 588 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 38 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 587 | 11.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 39 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 586 | 31.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 40 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 586 | 22.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 41 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 586 | 12.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 42 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 585 | 14.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 43 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 583 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 44 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 583 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 45 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 579 | 11.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 46 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 579 | 10.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 47 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 578 | 11.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 48 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 576 | 27.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 49 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 576 | 16.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 50 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 573 | 18.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |

Full queue lives in `data/audit_queue.json`.
