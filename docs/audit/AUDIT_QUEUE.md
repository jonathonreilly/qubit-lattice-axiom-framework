# Audit Queue

**Total pending:** 1369
**Ready (all deps already at retained-grade or metadata tiers):** 12

By criticality:
- `critical`: 284
- `high`: 278
- `medium`: 397
- `leaf`: 410

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 1230 | 13.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 2 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1217 | 23.25 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 3 | `abj_epsilon_index_square_block_no_go_note_2026-05-30` | no_go | audit_in_progress | critical | 1014 | 11.49 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_abj_epsilon_index_square_block_no_go.py` |
| 4 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 948 | 15.89 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 5 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 1225 | 21.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 6 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1222 | 21.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 7 | `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem | unaudited | critical | 1011 | 10.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py` |
| 8 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 1009 | 40.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 9 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 926 | 15.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 10 | `staggered_dirac_bz_corner_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 918 | 31.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_bz_corner_decomposition.py` |
| 11 | `axiom_first_reeh_schlieder_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 917 | 13.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reeh_schlieder_check.py` |
| 12 | `staggered_dirac_physical_species_direct_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 916 | 12.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_three_states_direct_derivation.py` |
| 13 | `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac` | bounded_theorem | unaudited | critical | 915 | 41.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_staggered_dirac_substep4_ac_check_2026_05_07_substep4ac.py` |
| 14 | `staggered_dirac_substep4_labeling_no_go_note_2026-05-17` | no_go | unaudited | critical | 911 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_labeling_no_go_2026_05_17.py` |
| 15 | `staggered_dirac_gate_closure_synthesis_theorem_note_2026-05-17` | bounded_theorem | unaudited | critical | 909 | 12.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_dirac_gate_closure_synthesis_2026_05_17.py` |
| 16 | `staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem | unaudited | critical | 908 | 10.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_runner.py` |
| 17 | `staggered_dirac_realization_gate_note_2026-05-03` | bounded_theorem | unaudited | critical | 907 | 39.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_realization_gate_synthesis_check_2026_06_09.py` |
| 18 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 852 | 38.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_s_derived_bounded_chain.py` |
| 19 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 851 | 57.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 20 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 825 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 21 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 804 | 26.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 22 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 762 | 10.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 23 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 760 | 38.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 24 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 757 | 29.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 25 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 757 | 14.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 26 | `yt_boundary_theorem` | open_gate | unaudited | critical | 755 | 16.06 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 27 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 739 | 12.03 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 28 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 734 | 15.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 29 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 728 | 10.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 30 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 727 | 28.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 31 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 717 | 17.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 32 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 713 | 20.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 33 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 706 | 10.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 34 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 705 | 11.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 35 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 704 | 14.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 36 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 703 | 10.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 37 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 702 | 15.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 38 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 700 | 13.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 39 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 699 | 11.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 40 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 698 | 12.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 41 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 697 | 14.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 42 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 696 | 32.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 43 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 695 | 12.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 44 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 695 | 12.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 45 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 693 | 31.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 46 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 693 | 22.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 47 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 691 | 11.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 48 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 691 | 10.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 49 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 690 | 11.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 50 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 688 | 16.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |

Full queue lives in `data/audit_queue.json`.
