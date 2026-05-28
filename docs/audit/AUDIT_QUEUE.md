# Audit Queue

**Total pending:** 1174
**Ready (all deps already at retained-grade or metadata tiers):** 42

By criticality:
- `critical`: 245
- `high`: 318
- `medium`: 316
- `leaf`: 295

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 909 | 19.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 2 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 908 | 27.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 3 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 899 | 10.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 4 | `s3_general_r_derivation_note` | bounded_theorem | unaudited | critical | 708 | 18.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 5 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | positive_theorem | unaudited | critical | 524 | 12.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 6 | `higgs_mass_from_axiom_note` | bounded_theorem | unaudited | critical | 494 | 24.95 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/higgs_tree_level_mean_field_runner_2026_05_03.py` |
| 7 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | bounded_theorem | unaudited | critical | 383 | 16.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 8 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 254 | 10.49 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_equilibrium_conversion_theorem.py` |
| 9 | `omega_lambda_derivation_note` | bounded_theorem | audit_in_progress | critical | 252 | 13.98 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_omega_lambda_arithmetic_cascade.py` |
| 10 | `dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 252 | 11.48 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py` |
| 11 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 906 | 15.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 12 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 898 | 11.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 13 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 897 | 10.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 14 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 896 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 15 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 895 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 16 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 895 | 14.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 17 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 894 | 16.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 18 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 894 | 13.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 19 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 893 | 19.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 20 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 891 | 20.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 21 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 888 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 22 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 886 | 18.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 23 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 868 | 39.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 24 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 722 | 38.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 25 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 702 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 26 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 676 | 26.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 27 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 632 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 28 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 630 | 27.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 29 | `yt_boundary_theorem` | open_gate | unaudited | critical | 630 | 15.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 30 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 619 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 31 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 616 | 14.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 32 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 610 | 10.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 33 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 609 | 27.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 34 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 593 | 17.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 35 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 582 | 10.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 36 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 581 | 11.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 37 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 580 | 14.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 38 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 579 | 10.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 39 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 578 | 15.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 40 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 576 | 32.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 41 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 576 | 13.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 42 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 575 | 11.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 43 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 574 | 31.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 44 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 574 | 22.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 45 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 574 | 12.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 46 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 573 | 14.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 47 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 571 | 12.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 48 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 571 | 12.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 49 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 567 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 50 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 567 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |

Full queue lives in `data/audit_queue.json`.
