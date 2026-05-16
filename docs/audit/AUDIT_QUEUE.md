# Audit Queue

**Total pending:** 1217
**Ready (all deps already at retained-grade or metadata tiers):** 21

By criticality:
- `critical`: 762
- `high`: 34
- `medium`: 152
- `leaf`: 269

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | bounded_theorem | audit_in_progress | critical | 797 | 10.14 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_three_generation_hw1_distinct_characters_exact.py` |
| 2 | `pmns_corner_transport_active_block_note` | bounded_theorem | unaudited | critical | 796 | 11.64 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_corner_transport_active_block.py` |
| 3 | `quark_route2_e_channel_readout_naturality_no_go_note_2026-04-28` | no_go | audit_in_progress | critical | 792 | 10.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py` |
| 4 | `koide_mru_weight_class_obstruction_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 790 | 18.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_mru_weight_class_obstruction_theorem.py` |
| 5 | `quark_e_channel_endpoint_quotient_law_note_2026-04-19` | bounded_theorem | unaudited | critical | 790 | 12.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_e_channel_endpoint_quotient_law.py` |
| 6 | `quark_endpoint_ratio_chain_law_note_2026-04-19` | bounded_theorem | unaudited | critical | 790 | 12.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_endpoint_ratio_chain_law.py` |
| 7 | `work_history.ckm.cabibbo_bound_note` | bounded_theorem | unaudited | critical | 790 | 11.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_mass_basis_nni.py` |
| 8 | `koide_moment_ratio_uniformity_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 790 | 11.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_moment_ratio_uniformity_theorem.py` |
| 9 | `koide_retained_wilson_aps_scalar_action_on_rank_two_multiplicity_bridge_narrow_theorem_note_2026-05-16` | positive_theorem | unaudited | critical | 789 | 10.13 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_retained_wilson_aps_scalar_action_on_rank_two_multiplicity_bridge_narrow.py` |
| 10 | `ckm_down_type_scale_convention_support_note_2026-04-22` | bounded_theorem | unaudited | critical | 788 | 12.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_down_type_scale_convention_support.py` |
| 11 | `dm_leptogenesis_pmns_minimum_information_source_law_note_2026-04-16` | bounded_theorem | unaudited | critical | 788 | 12.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py` |
| 12 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | positive_theorem | unaudited | critical | 788 | 12.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py` |
| 13 | `monopole_derived_note` | bounded_theorem | unaudited | critical | 788 | 12.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_monopole_derived.py` |
| 14 | `dark_energy_eos_note` | decoration | unaudited | critical | 788 | 11.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dark_energy_eos.py` |
| 15 | `koide_q_bridge_single_primitive_note_2026-04-22` | positive_theorem | unaudited | critical | 788 | 10.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_q_bridge_single_primitive.py` |
| 16 | `dm_leptogenesis_pmns_relative_action_stationarity_theorem_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 788 | 10.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py` |
| 17 | `hadron_lane1_b2_dynamical_screening_boundary_note_2026-04-29` | no_go | audit_in_progress | critical | 788 | 10.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hadron_lane1_b2_dynamical_screening_boundary.py` |
| 18 | `nonlinear_born_gravity_note` | bounded_theorem | unaudited | critical | 788 | 10.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_nonlinear_born_gravity.py` |
| 19 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 928 | 14.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 20 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 927 | 13.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 21 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 922 | 13.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 22 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 922 | 12.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 23 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 921 | 29.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 24 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 874 | 13.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 25 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 873 | 37.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 26 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 868 | 11.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 27 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 867 | 34.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 28 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 845 | 14.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 29 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 844 | 17.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 30 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 844 | 16.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 31 | `yt_boundary_theorem` | open_gate | unaudited | critical | 844 | 16.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 32 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 844 | 16.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 33 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 844 | 15.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 34 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 844 | 14.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 35 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 844 | 13.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 36 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 844 | 13.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 37 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 844 | 13.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 38 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 844 | 13.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 39 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 844 | 12.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 40 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 844 | 12.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 41 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 844 | 12.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 42 | `yt_explicit_systematic_budget_note` | positive_theorem | unaudited | critical | 844 | 12.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_explicit_systematic_budget.py` |
| 43 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 844 | 11.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 44 | `yt_exact_interacting_bridge_transport_note` | bounded_theorem | unaudited | critical | 844 | 11.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_interacting_bridge_transport.py` |
| 45 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 844 | 11.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 46 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 844 | 11.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 47 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 844 | 11.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 48 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 844 | 10.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 49 | `gate_b_grown_joint_package_note` | bounded_theorem | unaudited | critical | 836 | 13.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_grown_joint_package.py` |
| 50 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 822 | 46.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |

## Citation cycle break targets

242 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 844 | `yt_bridge_action_invariant_note` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 844 | `yt_bridge_rearrangement_principle_note` | critical | unaudited |
| 3 | `cycle-0003` | 2 | 844 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 844 | `yt_ew_coupling_bridge_note` | critical | unaudited |
| 5 | `cycle-0005` | 3 | 844 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 6 | `cycle-0006` | 3 | 844 | `yt_bridge_moment_closure_note` | critical | unaudited |
| 7 | `cycle-0007` | 3 | 844 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 8 | `cycle-0008` | 4 | 844 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 9 | `cycle-0009` | 4 | 844 | `yt_bridge_hessian_selector_note` | critical | unaudited |
| 10 | `cycle-0010` | 4 | 844 | `yt_bridge_operator_closure_note` | critical | unaudited |
| 11 | `cycle-0011` | 8 | 844 | `yt_boundary_theorem` | critical | unaudited |
| 12 | `cycle-0012` | 2 | 813 | `source_resolved_exact_green_h025_pocket_note` | critical | unaudited |
| 13 | `cycle-0013` | 2 | 813 | `source_resolved_exact_green_pocket_note` | critical | unaudited |
| 14 | `cycle-0014` | 3 | 813 | `source_resolved_exact_green_h025_pocket_note` | critical | unaudited |
| 15 | `cycle-0015` | 2 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 16 | `cycle-0016` | 4 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 17 | `cycle-0017` | 6 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 18 | `cycle-0018` | 7 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 19 | `cycle-0019` | 8 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 20 | `cycle-0020` | 9 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 21 | `cycle-0021` | 9 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 22 | `cycle-0022` | 10 | 805 | `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17` | critical | unaudited |
| 23 | `cycle-0023` | 2 | 799 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | audited_conditional |
| 24 | `cycle-0024` | 2 | 794 | `pmns_active_four_real_source_from_transport_note` | critical | unaudited |
| 25 | `cycle-0025` | 2 | 790 | `lensing_finite_path_explanation_note` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
