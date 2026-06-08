# Audit Queue

**Total pending:** 1335
**Ready (all deps already at retained-grade or metadata tiers):** 28

By criticality:
- `critical`: 327
- `high`: 250
- `medium`: 365
- `leaf`: 393

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1040 | 20.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 2 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 1031 | 12.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 3 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 1028 | 21.01 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 4 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1025 | 21.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 5 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 994 | 40.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 6 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 843 | 58.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 7 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 837 | 38.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 8 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 816 | 12.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 9 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 796 | 26.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 10 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 796 | 10.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 11 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 793 | 38.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 12 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 749 | 29.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 13 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 746 | 14.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 14 | `yt_boundary_theorem` | open_gate | unaudited | critical | 744 | 16.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 15 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 730 | 12.01 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 16 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 726 | 14.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 17 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 720 | 10.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 18 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 719 | 27.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 19 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 706 | 17.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 20 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 695 | 10.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 21 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 694 | 11.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 22 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 693 | 14.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 23 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 692 | 20.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 24 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 692 | 10.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 25 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 691 | 15.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 26 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 689 | 32.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 27 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 689 | 13.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 28 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 688 | 11.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 29 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 687 | 31.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 30 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 687 | 22.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 31 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 687 | 12.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 32 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 686 | 14.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 33 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 684 | 12.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 34 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 684 | 12.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 35 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 680 | 11.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 36 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 680 | 10.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 37 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 679 | 11.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 38 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 677 | 27.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 39 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 677 | 16.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 40 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 635 | 10.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 41 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 634 | 11.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 42 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 634 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 43 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 633 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 44 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 631 | 12.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |
| 45 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 628 | 11.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |
| 46 | `yt_p1_i_s_revision_verification_note_2026-04-17` | positive_theorem | unaudited | critical | 628 | 10.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_revision_verification.py` |
| 47 | `yt_p1_loop_geometric_bound_note_2026-04-17` | positive_theorem | unaudited | critical | 627 | 11.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_loop_geometric_bound.py` |
| 48 | `yt_p1_delta_r_master_assembly_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 626 | 13.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_r_master_assembly.py` |
| 49 | `yt_p1_delta_1_bz_computation_note_2026-04-17` | positive_theorem | unaudited | critical | 626 | 12.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_1_bz.py` |
| 50 | `yt_p1_delta_2_bz_computation_note_2026-04-17` | positive_theorem | unaudited | critical | 626 | 12.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_2_bz.py` |

## Citation cycle break targets

15 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 18 | `hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_note_2026-06-02` | medium | unaudited |
| 2 | `cycle-0002` | 2 | 11 | `beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30` | medium | unaudited |
| 3 | `cycle-0003` | 3 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 4 | `cycle-0004` | 3 | 9 | `beta6_plaquette_d9_coefficient_bounded_note_2026-06-04` | medium | unaudited |
| 5 | `cycle-0005` | 4 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 6 | `cycle-0006` | 4 | 9 | `beta6_plaquette_d8_coefficient_and_single_pair_verdict_bounded_note_2026-05-30` | medium | unaudited |
| 7 | `cycle-0007` | 5 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 8 | `cycle-0008` | 3 | 4 | `quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26` | medium | audited_conditional |
| 9 | `cycle-0009` | 2 | 2 | `chsh_tsirelson_lattice_qubits_bound_note_2026-05-20` | leaf | unaudited |
| 10 | `cycle-0010` | 2 | 2 | `dimension_selection_upper_bound_textbook_import_note_2026-05-17` | medium | unaudited |
| 11 | `cycle-0011` | 2 | 2 | `local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03` | leaf | unaudited |
| 12 | `cycle-0012` | 2 | 1 | `beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08` | leaf | unaudited |
| 13 | `cycle-0013` | 2 | 1 | `g_star_sm_content_at_leptogenesis_from_supplied_thermal_inventory_bounded_theorem_note_2026-05-28` | leaf | unaudited |
| 14 | `cycle-0014` | 2 | 1 | `generation_corner_hf_vq_screened_poisson_bridge_narrow_theorem_note_2026-06-07` | leaf | unaudited |
| 15 | `cycle-0015` | 2 | 1 | `yt_ward_ratio_tadpole_cancellation_narrow_theorem_note_2026-05-17` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
