# Audit Queue

**Total pending:** 1418
**Ready (all deps already at retained-grade or metadata tiers):** 52

By criticality:
- `critical`: 339
- `high`: 242
- `medium`: 394
- `leaf`: 443

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `su3_cube_index_graph_shortcut_open_gate_note_2026-05-03` | no_go | audit_in_progress | critical | 256 | 9.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_cube_index_graph_shortcut_open_gate.py` |
| 2 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1071 | 21.57 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 3 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 1053 | 21.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 4 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1050 | 21.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 5 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 1016 | 40.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 6 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 860 | 58.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 7 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 858 | 38.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 8 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 834 | 12.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 9 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 813 | 26.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 10 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 813 | 10.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 11 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 811 | 38.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 12 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 766 | 29.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 13 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 764 | 14.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 14 | `yt_boundary_theorem` | open_gate | unaudited | critical | 762 | 16.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 15 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 748 | 12.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 16 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 743 | 15.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 17 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 737 | 10.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 18 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 736 | 28.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 19 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 724 | 17.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 20 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 717 | 20.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 21 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 713 | 10.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 22 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 712 | 11.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 23 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 711 | 14.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 24 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 710 | 10.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 25 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 709 | 15.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 26 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 707 | 13.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 27 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 706 | 11.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 28 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 705 | 32.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 29 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 705 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 30 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 704 | 14.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 31 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 702 | 31.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 32 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 702 | 22.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 33 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 702 | 12.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 34 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 702 | 12.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 35 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 698 | 11.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 36 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 698 | 10.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 37 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 697 | 11.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 38 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 695 | 16.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 39 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 692 | 27.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 40 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 650 | 10.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 41 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 649 | 11.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 42 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 649 | 11.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 43 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 648 | 13.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 44 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 646 | 12.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |
| 45 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 643 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |
| 46 | `yt_p1_i_s_revision_verification_note_2026-04-17` | positive_theorem | unaudited | critical | 643 | 10.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_revision_verification.py` |
| 47 | `yt_p1_loop_geometric_bound_note_2026-04-17` | positive_theorem | unaudited | critical | 642 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_loop_geometric_bound.py` |
| 48 | `yt_p1_delta_r_master_assembly_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 641 | 13.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_r_master_assembly.py` |
| 49 | `yt_p1_delta_1_bz_computation_note_2026-04-17` | positive_theorem | unaudited | critical | 641 | 12.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_1_bz.py` |
| 50 | `yt_p1_delta_2_bz_computation_note_2026-04-17` | positive_theorem | unaudited | critical | 641 | 12.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_2_bz.py` |

Full queue lives in `data/audit_queue.json`.
