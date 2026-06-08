# Audit Queue

**Total pending:** 1347
**Ready (all deps already at retained-grade or metadata tiers):** 24

By criticality:
- `critical`: 328
- `high`: 255
- `medium`: 375
- `leaf`: 389

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 1040 | 32.52 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 2 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | unaudited | critical | 840 | 10.72 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 3 | `staggered_dirac_chirality_parity_bridge_narrow_theorem_note_2026-06-06` | bounded_theorem | unaudited | critical | 305 | 9.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_chirality_parity_bridge_2026_06_06.py` |
| 4 | `plaquette_v1_picard_fuchs_ode_note_2026-05-05` | bounded_theorem | unaudited | critical | 250 | 13.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py` |
| 5 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1035 | 20.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 6 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 1026 | 12.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 7 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 1023 | 21.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 8 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1020 | 21.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 9 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 989 | 40.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 10 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 838 | 58.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 11 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 832 | 38.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 12 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 811 | 12.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 13 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 791 | 26.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 14 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 791 | 10.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 15 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 788 | 38.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 16 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 744 | 29.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 17 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 741 | 14.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 18 | `yt_boundary_theorem` | open_gate | unaudited | critical | 739 | 16.03 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 19 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 725 | 12.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 20 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 721 | 14.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 21 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 715 | 10.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 22 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 714 | 27.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 23 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 701 | 17.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 24 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 690 | 10.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 25 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 689 | 11.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 26 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 688 | 14.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 27 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 687 | 20.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 28 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 687 | 10.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 29 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 686 | 15.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 30 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 684 | 32.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 31 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 684 | 13.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 32 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 683 | 11.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 33 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 682 | 31.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 34 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 682 | 22.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 35 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 682 | 12.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 36 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 681 | 14.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 37 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 679 | 12.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 38 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 679 | 12.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 39 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 675 | 11.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 40 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 675 | 10.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 41 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 674 | 11.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 42 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 672 | 27.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 43 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 672 | 16.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 44 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 630 | 10.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 45 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 629 | 11.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 46 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 629 | 11.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 47 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 628 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 48 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 626 | 12.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |
| 49 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 623 | 11.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |
| 50 | `yt_p1_i_s_revision_verification_note_2026-04-17` | positive_theorem | unaudited | critical | 623 | 10.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_revision_verification.py` |

## Citation cycle break targets

16 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

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
| 11 | `cycle-0011` | 2 | 2 | `generation_dial_dynamics_stability_classifier_2026-06-05` | medium | unaudited |
| 12 | `cycle-0012` | 2 | 2 | `local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03` | leaf | unaudited |
| 13 | `cycle-0013` | 2 | 1 | `beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08` | leaf | unaudited |
| 14 | `cycle-0014` | 2 | 1 | `g_star_sm_content_at_leptogenesis_from_supplied_thermal_inventory_bounded_theorem_note_2026-05-28` | leaf | unaudited |
| 15 | `cycle-0015` | 2 | 1 | `generation_corner_hf_vq_screened_poisson_bridge_narrow_theorem_note_2026-06-07` | leaf | unaudited |
| 16 | `cycle-0016` | 2 | 1 | `yt_ward_ratio_tadpole_cancellation_narrow_theorem_note_2026-05-17` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
