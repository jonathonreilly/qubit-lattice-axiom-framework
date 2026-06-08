# Audit Queue

**Total pending:** 1334
**Ready (all deps already at retained-grade or metadata tiers):** 23

By criticality:
- `critical`: 334
- `high`: 250
- `medium`: 360
- `leaf`: 390

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 1041 | 32.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 2 | `rp_wilson_temporal_gauge_bridge_sign_and_positivity_repair_note_2026-06-06` | bounded_theorem | unaudited | critical | 1041 | 10.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.py` |
| 3 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1037 | 20.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 4 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 1028 | 12.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 5 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 1025 | 21.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 6 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1022 | 21.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 7 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 994 | 40.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 8 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 843 | 58.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 9 | `observable_principle_positive_source_cone_p2_elimination_narrow_theorem_note_2026-06-06` | bounded_theorem | unaudited | critical | 843 | 10.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py` |
| 10 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 838 | 38.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 11 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 817 | 12.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 12 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 796 | 26.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 13 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 793 | 10.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 14 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 790 | 38.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 15 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 749 | 29.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 16 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 747 | 14.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 17 | `yt_boundary_theorem` | open_gate | unaudited | critical | 745 | 16.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 18 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 731 | 12.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 19 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 727 | 14.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 20 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 721 | 10.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 21 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 720 | 27.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 22 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 707 | 17.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 23 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 696 | 10.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 24 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 695 | 11.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 25 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 694 | 14.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 26 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 693 | 20.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 27 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 693 | 10.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 28 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 692 | 15.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 29 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 690 | 32.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 30 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 690 | 13.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 31 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 689 | 11.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 32 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 688 | 31.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 33 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 688 | 22.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 34 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 688 | 12.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 35 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 687 | 14.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 36 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 685 | 12.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 37 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 685 | 12.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 38 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 681 | 11.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 39 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 681 | 10.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 40 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 680 | 11.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 41 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 678 | 27.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 42 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 678 | 16.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 43 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 636 | 10.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 44 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 635 | 11.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 45 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 635 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 46 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 634 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 47 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 632 | 12.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |
| 48 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 629 | 11.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |
| 49 | `yt_p1_i_s_revision_verification_note_2026-04-17` | positive_theorem | unaudited | critical | 629 | 10.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_revision_verification.py` |
| 50 | `yt_p1_loop_geometric_bound_note_2026-04-17` | positive_theorem | unaudited | critical | 628 | 11.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_loop_geometric_bound.py` |

## Citation cycle break targets

20 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 1041 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 843 | `observable_principle_from_axiom_note` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 316 | `staggered_dirac_chirality_parity_bridge_narrow_theorem_note_2026-06-06` | critical | unaudited |
| 4 | `cycle-0004` | 4 | 33 | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | medium | unaudited |
| 5 | `cycle-0005` | 2 | 18 | `hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_note_2026-06-02` | medium | unaudited |
| 6 | `cycle-0006` | 2 | 11 | `beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30` | medium | unaudited |
| 7 | `cycle-0007` | 3 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 8 | `cycle-0008` | 3 | 9 | `beta6_plaquette_d9_coefficient_bounded_note_2026-06-04` | medium | unaudited |
| 9 | `cycle-0009` | 4 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 10 | `cycle-0010` | 4 | 9 | `beta6_plaquette_d8_coefficient_and_single_pair_verdict_bounded_note_2026-05-30` | medium | unaudited |
| 11 | `cycle-0011` | 5 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 12 | `cycle-0012` | 3 | 4 | `quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26` | medium | audited_conditional |
| 13 | `cycle-0013` | 2 | 2 | `chsh_tsirelson_lattice_qubits_bound_note_2026-05-20` | leaf | unaudited |
| 14 | `cycle-0014` | 2 | 2 | `dimension_selection_upper_bound_textbook_import_note_2026-05-17` | medium | unaudited |
| 15 | `cycle-0015` | 2 | 2 | `generation_dial_dynamics_stability_classifier_2026-06-05` | medium | unaudited |
| 16 | `cycle-0016` | 2 | 2 | `local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03` | leaf | unaudited |
| 17 | `cycle-0017` | 2 | 1 | `beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08` | leaf | unaudited |
| 18 | `cycle-0018` | 2 | 1 | `g_star_sm_content_at_leptogenesis_from_supplied_thermal_inventory_bounded_theorem_note_2026-05-28` | leaf | unaudited |
| 19 | `cycle-0019` | 2 | 1 | `generation_corner_hf_vq_screened_poisson_bridge_narrow_theorem_note_2026-06-07` | leaf | unaudited |
| 20 | `cycle-0020` | 2 | 1 | `yt_ward_ratio_tadpole_cancellation_narrow_theorem_note_2026-05-17` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
