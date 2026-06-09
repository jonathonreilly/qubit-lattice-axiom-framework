# Audit Queue

**Total pending:** 1386
**Ready (all deps already at retained-grade or metadata tiers):** 34

By criticality:
- `critical`: 333
- `high`: 254
- `medium`: 373
- `leaf`: 426

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 1052 | 13.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 2 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | bounded_theorem | audit_in_progress | critical | 284 | 18.16 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/lattice_greens_z3_asymptotic_normalization_certificate.py` |
| 3 | `lattice_greens_maradudin_asymptotic_accepted_premise_bridge_bounded_note_2026-05-27` | bounded_theorem | unaudited | critical | 275 | 12.61 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/lattice_greens_maradudin_asymptotic_accepted_premise_runner.py` |
| 4 | `yt_ew_matching_rule_m_note_2026-05-02` | no_go | audit_in_progress | critical | 250 | 9.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_matching_rule_m_current_packet_boundary.py` |
| 5 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 1060 | 20.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 6 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 1048 | 21.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 7 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1045 | 21.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 8 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 1011 | 40.48 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 9 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 856 | 58.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 10 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 854 | 38.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 11 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 830 | 12.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 12 | `yt_ward_identity_dependencies_registered_bound_narrow_theorem_note_2026-06-05` | bounded_theorem | unaudited | critical | 811 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py` |
| 13 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 809 | 26.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 14 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 808 | 38.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 15 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 762 | 29.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 16 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 761 | 14.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 17 | `yt_boundary_theorem` | open_gate | unaudited | critical | 759 | 16.07 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 18 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 744 | 12.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 19 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 740 | 15.53 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 20 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 734 | 10.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 21 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 733 | 28.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 22 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 721 | 17.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 23 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 710 | 10.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 24 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 709 | 11.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 25 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 708 | 14.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 26 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 707 | 20.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 27 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 707 | 10.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 28 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 706 | 15.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 29 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 704 | 13.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 30 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 703 | 11.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 31 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 702 | 32.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 32 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 702 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 33 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 701 | 14.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 34 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 699 | 31.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 35 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 699 | 22.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 36 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 699 | 12.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 37 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 699 | 12.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 38 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 695 | 11.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 39 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 695 | 10.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 40 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 694 | 11.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 41 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 692 | 16.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 42 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 689 | 27.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 43 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 647 | 10.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 44 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 646 | 11.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 45 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 646 | 11.34 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 46 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 645 | 13.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 47 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 643 | 12.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |
| 48 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 640 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |
| 49 | `yt_p1_i_s_revision_verification_note_2026-04-17` | positive_theorem | unaudited | critical | 640 | 10.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_revision_verification.py` |
| 50 | `yt_p1_loop_geometric_bound_note_2026-04-17` | positive_theorem | unaudited | critical | 639 | 11.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_loop_geometric_bound.py` |

## Citation cycle break targets

18 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 63 | `g_newton_born_as_source_positive_theorem_note_2026-05-10_gnewtong2` | high | unaudited |
| 2 | `cycle-0002` | 2 | 18 | `hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_note_2026-06-02` | medium | unaudited |
| 3 | `cycle-0003` | 2 | 11 | `beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30` | medium | unaudited |
| 4 | `cycle-0004` | 3 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 5 | `cycle-0005` | 3 | 9 | `beta6_plaquette_d9_coefficient_bounded_note_2026-06-04` | medium | unaudited |
| 6 | `cycle-0006` | 4 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 7 | `cycle-0007` | 4 | 9 | `beta6_plaquette_d8_coefficient_and_single_pair_verdict_bounded_note_2026-05-30` | medium | unaudited |
| 8 | `cycle-0008` | 5 | 9 | `beta6_delta_analytic_class_frontier_note_2026-05-30` | medium | unaudited |
| 9 | `cycle-0009` | 2 | 7 | `emergent_lorentz_radiative_stability_discrete_tick_b4_bounded_theorem_note_2026-06-08` | medium | unaudited |
| 10 | `cycle-0010` | 3 | 4 | `quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26` | medium | audited_conditional |
| 11 | `cycle-0011` | 2 | 2 | `chsh_tsirelson_lattice_qubits_bound_note_2026-05-20` | leaf | unaudited |
| 12 | `cycle-0012` | 2 | 2 | `dimension_selection_upper_bound_textbook_import_note_2026-05-17` | medium | unaudited |
| 13 | `cycle-0013` | 2 | 2 | `local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03` | leaf | unaudited |
| 14 | `cycle-0014` | 2 | 2 | `universal_gr_degenerate_supermetric_graviton_sign_no_go_bounded_theorem_note_2026-06-08` | medium | unaudited |
| 15 | `cycle-0015` | 2 | 1 | `beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08` | leaf | unaudited |
| 16 | `cycle-0016` | 2 | 1 | `g_star_sm_content_at_leptogenesis_from_supplied_thermal_inventory_bounded_theorem_note_2026-05-28` | leaf | unaudited |
| 17 | `cycle-0017` | 2 | 1 | `generation_corner_hf_vq_screened_poisson_bridge_narrow_theorem_note_2026-06-07` | leaf | unaudited |
| 18 | `cycle-0018` | 2 | 1 | `yt_ward_ratio_tadpole_cancellation_narrow_theorem_note_2026-05-17` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
