# Audit Queue

**Total pending:** 1149
**Ready (all deps already at retained-grade or metadata tiers):** 22

By criticality:
- `critical`: 243
- `high`: 319
- `medium`: 310
- `leaf`: 277

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 903 | 27.82 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 2 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 894 | 10.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 3 | `s3_general_r_derivation_note` | bounded_theorem | unaudited | critical | 703 | 18.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 4 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | positive_theorem | unaudited | critical | 520 | 12.03 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 5 | `higgs_mass_from_axiom_note` | bounded_theorem | unaudited | critical | 490 | 24.94 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/higgs_tree_level_mean_field_runner_2026_05_03.py` |
| 6 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | bounded_theorem | unaudited | critical | 381 | 16.58 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 7 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 252 | 10.48 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_equilibrium_conversion_theorem.py` |
| 8 | `omega_lambda_derivation_note` | bounded_theorem | audit_in_progress | critical | 250 | 13.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_omega_lambda_arithmetic_cascade.py` |
| 9 | `dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 250 | 11.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py` |
| 10 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 901 | 15.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 11 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 893 | 11.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 12 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 892 | 10.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 13 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 891 | 11.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 14 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 890 | 15.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 15 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 890 | 14.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 16 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 889 | 16.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 17 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 889 | 13.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 18 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 888 | 19.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 19 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 886 | 20.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 20 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 883 | 13.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 21 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 881 | 18.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 22 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 863 | 39.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 23 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 718 | 37.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 24 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 697 | 12.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 25 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 672 | 26.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 26 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 628 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 27 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 626 | 27.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 28 | `yt_boundary_theorem` | open_gate | unaudited | critical | 626 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 29 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 615 | 11.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 30 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 612 | 14.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 31 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 606 | 10.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 32 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 605 | 27.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 33 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 589 | 17.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 34 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 578 | 10.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 35 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 577 | 11.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 36 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 576 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 37 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 575 | 10.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 38 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 574 | 15.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 39 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 572 | 32.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 40 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 572 | 13.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 41 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 571 | 11.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 42 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 570 | 31.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 43 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 570 | 22.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 44 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 570 | 12.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 45 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 569 | 14.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 46 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 567 | 12.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 47 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 567 | 12.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 48 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 563 | 11.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 49 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 563 | 10.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 50 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 562 | 11.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |

Full queue lives in `data/audit_queue.json`.
