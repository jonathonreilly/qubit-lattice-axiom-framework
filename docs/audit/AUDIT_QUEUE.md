# Audit Queue

**Total pending:** 1331
**Ready (all deps already at retained-grade or metadata tiers):** 56

By criticality:
- `critical`: 319
- `high`: 258
- `medium`: 361
- `leaf`: 393

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | bounded_theorem | audit_in_progress | critical | 1003 | 19.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 2 | `eta_holonomy_base_flux_scope_boundary_note_2026-06-06` | positive_theorem | audit_in_progress | critical | 293 | 8.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_eta_holonomy_base_flux_scope_boundary_2026_06_06.py` |
| 3 | `g_bare_hilbert_schmidt_rigidity_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 275 | 22.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_hs_rigidity_narrow.py` |
| 4 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1012 | 20.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 5 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 1003 | 11.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 6 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 1000 | 20.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 7 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 998 | 20.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 8 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 967 | 40.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 9 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 821 | 58.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 10 | `observable_principle_positive_source_cone_p2_elimination_narrow_theorem_note_2026-06-06` | bounded_theorem | unaudited | critical | 821 | 10.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py` |
| 11 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 813 | 38.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 12 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 792 | 12.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 13 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 771 | 26.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 14 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 769 | 10.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 15 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 766 | 38.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 16 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 724 | 29.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 17 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 722 | 14.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 18 | `yt_boundary_theorem` | open_gate | unaudited | critical | 720 | 15.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 19 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 706 | 11.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 20 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 703 | 14.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 21 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 697 | 10.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 22 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 696 | 27.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 23 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 682 | 17.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 24 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 671 | 10.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 25 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 670 | 20.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 26 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 670 | 11.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 27 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 669 | 14.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 28 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 668 | 10.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 29 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 667 | 15.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 30 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 666 | 32.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 31 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 665 | 13.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 32 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 664 | 31.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 33 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 664 | 22.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 34 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 664 | 11.88 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 35 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 663 | 12.38 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 36 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 662 | 14.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 37 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 660 | 12.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 38 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 660 | 12.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 39 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 656 | 11.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 40 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 656 | 10.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 41 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 655 | 11.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 42 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 654 | 27.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 43 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 653 | 16.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 44 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 612 | 10.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 45 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 611 | 11.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 46 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 611 | 11.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 47 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 610 | 13.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 48 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 608 | 12.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |
| 49 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 605 | 11.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |
| 50 | `yt_p1_i_s_revision_verification_note_2026-04-17` | positive_theorem | unaudited | critical | 605 | 10.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_revision_verification.py` |

## Citation cycle break targets

9 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 821 | `observable_principle_from_axiom_note` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 294 | `staggered_dirac_chirality_parity_bridge_narrow_theorem_note_2026-06-06` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 18 | `hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_note_2026-06-02` | medium | unaudited |
| 4 | `cycle-0004` | 2 | 10 | `beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30` | medium | unaudited |
| 5 | `cycle-0005` | 2 | 2 | `chsh_tsirelson_lattice_qubits_bound_note_2026-05-20` | leaf | unaudited |
| 6 | `cycle-0006` | 2 | 2 | `local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03` | leaf | unaudited |
| 7 | `cycle-0007` | 2 | 1 | `g_star_sm_content_at_leptogenesis_from_supplied_thermal_inventory_bounded_theorem_note_2026-05-28` | leaf | unaudited |
| 8 | `cycle-0008` | 2 | 1 | `generation_dial_dynamics_stability_classifier_2026-06-05` | leaf | unaudited |
| 9 | `cycle-0009` | 2 | 1 | `yt_ward_ratio_tadpole_cancellation_narrow_theorem_note_2026-05-17` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
