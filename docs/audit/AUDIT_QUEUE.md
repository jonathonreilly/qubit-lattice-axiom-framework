# Audit Queue

**Total pending:** 1436
**Ready (all deps at retained-grade/metadata tiers or accepted premises: axiom/primitive nodes and Tier-A admitted derivation targets):** 45

By criticality:
- `critical`: 292
- `high`: 284
- `medium`: 421
- `leaf`: 439

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_reeh_schlieder_theorem_note_2026-05-01` | bounded_theorem | audit_in_progress | critical | 940 | 13.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reeh_schlieder_check.py` |
| 2 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 861 | 38.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_s_derived_bounded_chain.py` |
| 3 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 775 | 11.10 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 4 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 726 | 21.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 5 | `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 655 | 15.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_s_tadpole_improvement_vertex_power_narrow.py` |
| 6 | `higgs_mass_from_axiom_note` | bounded_theorem | unaudited | critical | 643 | 25.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/higgs_tree_level_mean_field_runner_2026_05_03.py` |
| 7 | `pmns_twisted_flux_transfer_holonomy_boundary_note` | bounded_theorem | unaudited | critical | 510 | 10.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_twisted_flux_transfer_holonomy_boundary.py` |
| 8 | `axiom_first_cpt_theorem_stretch_note_2026-04-29` | bounded_theorem | unaudited | critical | 364 | 11.51 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cpt_check.py` |
| 9 | `koide_full_lattice_schur_inheritance_note_2026-04-18` | bounded_theorem | unaudited | critical | 277 | 11.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_full_lattice_schur_inheritance.py` |
| 10 | `gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11` | bounded_theorem | unaudited | critical | 272 | 8.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gravity_weak_field_source_response_bridge_2026_06_11.py` |
| 11 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1238 | 24.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 12 | `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem | unaudited | critical | 1023 | 11.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py` |
| 13 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 1021 | 40.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 14 | `axiom_first_lattice_noether_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 973 | 15.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_lattice_noether_check.py` |
| 15 | `staggered_dirac_substep2_kahler_dirac_equivalence_narrow_theorem_note_2026-05-17` | bounded_theorem | unaudited | critical | 965 | 15.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep2_kahler_dirac_equivalence_exact_2026_05_17.py` |
| 16 | `staggered_dirac_substep1_statistics_gl_f_conditional_discriminator_bounded_theorem_note_2026-06-10` | bounded_theorem | unaudited | critical | 953 | 11.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_substep1_statistics_selection_check_2026_06_10.py` |
| 17 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 949 | 15.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 18 | `staggered_dirac_bz_corner_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 941 | 31.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_bz_corner_decomposition.py` |
| 19 | `staggered_dirac_physical_species_direct_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 939 | 12.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_three_states_direct_derivation.py` |
| 20 | `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac` | bounded_theorem | unaudited | critical | 938 | 41.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_staggered_dirac_substep4_ac_check_2026_05_07_substep4ac.py` |
| 21 | `staggered_dirac_substep4_labeling_no_go_note_2026-05-17` | no_go | unaudited | critical | 934 | 11.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_labeling_no_go_2026_05_17.py` |
| 22 | `staggered_dirac_gate_closure_synthesis_theorem_note_2026-05-17` | bounded_theorem | unaudited | critical | 932 | 12.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_dirac_gate_closure_synthesis_2026_05_17.py` |
| 23 | `staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem | unaudited | critical | 931 | 10.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_runner.py` |
| 24 | `staggered_dirac_realization_gate_note_2026-05-03` | bounded_theorem | unaudited | critical | 930 | 39.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_realization_gate_synthesis_check_2026_06_09.py` |
| 25 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 862 | 59.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 26 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 836 | 12.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 27 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 814 | 26.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 28 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 772 | 38.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 29 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 768 | 14.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 30 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 767 | 29.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 31 | `yt_boundary_theorem` | open_gate | unaudited | critical | 766 | 16.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 32 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 750 | 12.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 33 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 745 | 15.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 34 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 739 | 10.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 35 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 738 | 28.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 36 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 728 | 17.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 37 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 717 | 10.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 38 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 716 | 11.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 39 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 715 | 14.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 40 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 714 | 10.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 41 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 713 | 15.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 42 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 711 | 13.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 43 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 710 | 11.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 44 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 709 | 12.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 45 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 708 | 14.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 46 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 707 | 32.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 47 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 706 | 12.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 48 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 706 | 12.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 49 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 704 | 31.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 50 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 704 | 22.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |

Full queue lives in `data/audit_queue.json`.
