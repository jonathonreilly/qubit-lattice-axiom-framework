# Audit Queue

**Total pending:** 1298
**Ready (all deps already at retained-grade or metadata tiers):** 38

By criticality:
- `critical`: 313
- `high`: 255
- `medium`: 354
- `leaf`: 376

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 1093 | 10.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 2 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 1092 | 39.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 3 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 1028 | 15.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py` |
| 4 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 1018 | 10.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 5 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 1016 | 12.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 6 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 1015 | 13.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 7 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1008 | 15.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 8 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1006 | 20.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 9 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 998 | 11.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 10 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 995 | 20.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 11 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 993 | 20.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 12 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 962 | 40.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 13 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 816 | 58.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 14 | `observable_principle_positive_source_cone_p2_elimination_narrow_theorem_note_2026-06-06` | bounded_theorem | unaudited | critical | 816 | 10.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py` |
| 15 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 807 | 38.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 16 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 787 | 12.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 17 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 766 | 26.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 18 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 719 | 28.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 19 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 714 | 13.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 20 | `yt_boundary_theorem` | open_gate | unaudited | critical | 712 | 15.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 21 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 701 | 11.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 22 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 698 | 14.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 23 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 692 | 10.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 24 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 691 | 27.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 25 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 674 | 17.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 26 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 663 | 10.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 27 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 662 | 20.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 28 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 662 | 11.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 29 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 661 | 14.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 30 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 660 | 10.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 31 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 659 | 15.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 32 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 658 | 32.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 33 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 657 | 13.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 34 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 656 | 31.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 35 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 656 | 22.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 36 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 656 | 11.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 37 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 655 | 12.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 38 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 654 | 14.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 39 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 652 | 12.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 40 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 652 | 12.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 41 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 648 | 11.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 42 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 648 | 10.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 43 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 647 | 11.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 44 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 646 | 27.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 45 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 645 | 16.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 46 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 604 | 10.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 47 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 603 | 11.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 48 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 602 | 13.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 49 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 602 | 11.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 50 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 600 | 12.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |

## Citation cycle break targets

6 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 816 | `observable_principle_from_axiom_note` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 10 | `beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30` | medium | unaudited |
| 3 | `cycle-0003` | 2 | 2 | `chsh_tsirelson_lattice_qubits_bound_note_2026-05-20` | leaf | unaudited |
| 4 | `cycle-0004` | 2 | 2 | `local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03` | leaf | unaudited |
| 5 | `cycle-0005` | 2 | 1 | `g_star_sm_content_at_leptogenesis_from_supplied_thermal_inventory_bounded_theorem_note_2026-05-28` | leaf | unaudited |
| 6 | `cycle-0006` | 2 | 1 | `generation_dial_dynamics_stability_classifier_2026-06-05` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
