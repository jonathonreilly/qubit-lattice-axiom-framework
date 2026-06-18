# Audit Queue

**Total pending:** 1646
**Ready (all deps at retained-grade/metadata tiers or accepted premises: axiom/primitive nodes and Tier-A admitted derivation targets):** 161

By criticality:
- `critical`: 314
- `high`: 289
- `medium`: 474
- `leaf`: 569

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `axiom_first_kms_condition_theorem_note_2026-05-01` | positive_theorem | audit_in_progress | critical | 373 | 13.05 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_kms_condition_check.py` |
| 2 | `su3_casimir_fundamental_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 352 | 17.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/su3_casimir_fundamental_check.py` |
| 3 | `koide_q_delta_linking_relation_theorem_note_2026-04-20` | bounded_theorem | unaudited | critical | 321 | 13.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_q_delta_formal_ratio_repair.py` |
| 4 | `cl3_quark_antiquark_color_singlet_theorem_note_2026-05-02` | decoration | unaudited | critical | 308 | 10.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_quark_antiquark_color_singlet_check.py` |
| 5 | `poisson_exhaustive_uniqueness_note` | bounded_theorem | unaudited | critical | 292 | 14.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_poisson_exhaustive_uniqueness.py` |
| 6 | `hierarchy_formula_honest_status_note_2026-05-10` | bounded_theorem | unaudited | critical | 261 | 17.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_formula_honest_status.py` |
| 7 | `hierarchy_effective_potential_endpoint_note` | bounded_theorem | unaudited | critical | 251 | 13.48 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_effective_potential_endpoint.py` |
| 8 | `koide_kappa_block_total_frobenius_measure_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 238 | 20.90 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_kappa_block_total_frobenius_measure_theorem.py` |
| 9 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 1083 | 40.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 10 | `staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10` | bounded_theorem | unaudited | critical | 1054 | 14.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py` |
| 11 | `axiom_first_lattice_noether_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 958 | 19.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_lattice_noether_check.py` |
| 12 | `staggered_dirac_physical_species_direct_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 922 | 15.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_three_states_direct_derivation.py` |
| 13 | `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac` | bounded_theorem | unaudited | critical | 921 | 44.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_staggered_dirac_substep4_ac_check_2026_05_07_substep4ac.py` |
| 14 | `staggered_dirac_substep4_labeling_no_go_note_2026-05-17` | no_go | unaudited | critical | 912 | 15.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_labeling_no_go_2026_05_17.py` |
| 15 | `staggered_dirac_gate_closure_synthesis_theorem_note_2026-05-17` | bounded_theorem | unaudited | critical | 910 | 15.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_dirac_gate_closure_synthesis_2026_05_17.py` |
| 16 | `staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem | unaudited | critical | 908 | 13.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_runner.py` |
| 17 | `yt_vertex_power_derivation` | bounded_theorem | unaudited | critical | 908 | 11.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 18 | `staggered_dirac_realization_gate_note_2026-05-03` | bounded_theorem | unaudited | critical | 907 | 38.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_realization_gate_synthesis_check_2026_06_09.py` |
| 19 | `yt_vertex_power_operator_counting_lemma_note_2026-05-17` | bounded_theorem | unaudited | critical | 904 | 11.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_vertex_power_operator_counting_lemma.py` |
| 20 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 901 | 38.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_s_derived_bounded_chain.py` |
| 21 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 879 | 12.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 22 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 876 | 16.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 23 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 876 | 12.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 24 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 876 | 12.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |
| 25 | `s3_time_theta_to_slice_coupling_note` | open_gate | unaudited | critical | 876 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 26 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 859 | 26.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 27 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 813 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 28 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 812 | 29.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 29 | `yt_boundary_theorem` | open_gate | unaudited | critical | 811 | 16.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 30 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 801 | 17.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 31 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 788 | 10.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 32 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 787 | 11.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 33 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 786 | 14.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 34 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 785 | 11.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 35 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 784 | 16.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 36 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 782 | 13.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 37 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 781 | 12.11 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 38 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 780 | 12.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 39 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 779 | 14.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 40 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 777 | 13.10 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 41 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 777 | 13.10 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 42 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 773 | 11.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 43 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 773 | 11.10 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 44 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 772 | 11.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 45 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 770 | 17.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 46 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 765 | 10.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 47 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 764 | 29.08 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 48 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 734 | 33.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 49 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 731 | 31.52 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 50 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 731 | 23.02 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |

## Citation cycle break targets

7 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 4 | 876 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | critical | unaudited |
| 2 | `cycle-0002` | 3 | 629 | `ckm_down_type_scale_convention_support_note_2026-04-22` | critical | unaudited |
| 3 | `cycle-0003` | 4 | 629 | `ckm_down_type_scale_convention_support_note_2026-04-22` | critical | unaudited |
| 4 | `cycle-0004` | 4 | 629 | `ckm_down_type_scale_convention_support_note_2026-04-22` | critical | unaudited |
| 5 | `cycle-0005` | 5 | 629 | `ckm_down_type_scale_convention_support_note_2026-04-22` | critical | unaudited |
| 6 | `cycle-0006` | 6 | 629 | `ckm_down_type_scale_convention_support_note_2026-04-22` | critical | unaudited |
| 7 | `cycle-0007` | 2 | 83 | `koide_q_reduced_carrier_physical_identification_obstruction_note_2026-06-12` | medium | unaudited |

Full queue lives in `data/audit_queue.json`.
