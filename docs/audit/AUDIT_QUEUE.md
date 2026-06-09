# Audit Queue

**Total pending:** 1344
**Ready (all deps already at retained-grade or metadata tiers):** 30

By criticality:
- `critical`: 327
- `high`: 252
- `medium`: 365
- `leaf`: 400

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1052 | 20.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 2 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 1040 | 21.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 3 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1037 | 21.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 4 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 1005 | 40.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 5 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 853 | 58.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 6 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 848 | 38.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 7 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 827 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 8 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 807 | 26.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 9 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 806 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 10 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 803 | 38.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 11 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 760 | 29.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 12 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 756 | 14.06 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 13 | `yt_boundary_theorem` | open_gate | unaudited | critical | 754 | 16.06 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 14 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 741 | 12.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 15 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 737 | 15.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 16 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 731 | 10.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 17 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 730 | 28.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 18 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 716 | 17.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 19 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 705 | 10.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 20 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 704 | 11.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 21 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 703 | 20.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 22 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 703 | 14.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 23 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 702 | 10.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 24 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 701 | 15.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 25 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 700 | 32.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 26 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 699 | 13.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 27 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 698 | 11.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 28 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 697 | 31.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 29 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 697 | 22.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 30 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 697 | 12.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 31 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 696 | 14.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 32 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 694 | 12.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 33 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 694 | 12.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 34 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 690 | 11.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 35 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 690 | 10.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 36 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 689 | 11.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 37 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 687 | 27.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 38 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 687 | 16.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 39 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 645 | 10.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 40 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 644 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 41 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 644 | 11.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 42 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 643 | 13.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 43 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 641 | 12.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |
| 44 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 638 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |
| 45 | `yt_p1_i_s_revision_verification_note_2026-04-17` | positive_theorem | unaudited | critical | 638 | 10.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_revision_verification.py` |
| 46 | `yt_p1_loop_geometric_bound_note_2026-04-17` | positive_theorem | unaudited | critical | 637 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_loop_geometric_bound.py` |
| 47 | `yt_p1_delta_r_master_assembly_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 636 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_r_master_assembly.py` |
| 48 | `yt_p1_delta_1_bz_computation_note_2026-04-17` | positive_theorem | unaudited | critical | 636 | 12.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_1_bz.py` |
| 49 | `yt_p1_delta_2_bz_computation_note_2026-04-17` | positive_theorem | unaudited | critical | 636 | 12.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_2_bz.py` |
| 50 | `yt_p1_delta_3_bz_computation_note_2026-04-17` | positive_theorem | unaudited | critical | 636 | 12.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_delta_3_bz.py` |

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
