# Audit Queue

**Total pending:** 1214
**Ready (all deps already at retained-grade or metadata tiers):** 48

By criticality:
- `critical`: 243
- `high`: 336
- `medium`: 326
- `leaf`: 309

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `planck_target3_clifford_phase_bridge_theorem_note_2026-04-25` | bounded_theorem | unaudited | critical | 891 | 18.30 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_target3_conditional_clifford_carrier_repair.py` |
| 2 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 880 | 10.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 3 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 703 | 19.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 4 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 694 | 30.44 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_structure_narrow_spectrum.py` |
| 5 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | unaudited | critical | 518 | 9.52 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 6 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | positive_theorem | unaudited | critical | 514 | 12.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 7 | `sm_relativistic_dof_count_import_note_2026-05-17` | bounded_theorem | audit_in_progress | critical | 250 | 9.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_relativistic_dof_finite_inventory.py` |
| 8 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 890 | 19.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 9 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 887 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 10 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 879 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 11 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 878 | 10.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 12 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 877 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 13 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 876 | 15.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 14 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 876 | 14.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 15 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 875 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 16 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 874 | 19.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 17 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 872 | 19.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 18 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 872 | 12.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 19 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 867 | 13.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 20 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 865 | 17.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 21 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 849 | 38.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 22 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 712 | 37.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 23 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 697 | 18.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 24 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 691 | 12.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 25 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 657 | 25.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 26 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 622 | 13.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 27 | `yt_boundary_theorem` | open_gate | unaudited | critical | 620 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 28 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 616 | 27.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 29 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 609 | 11.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 30 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 606 | 14.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 31 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 600 | 10.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 32 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 599 | 27.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 33 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 583 | 17.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 34 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 572 | 10.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 35 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 571 | 11.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 36 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 570 | 14.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 37 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 569 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 38 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 568 | 15.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 39 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 566 | 32.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 40 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 566 | 13.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 41 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 565 | 11.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 42 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 564 | 31.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 43 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 564 | 22.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 44 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 564 | 12.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 45 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 563 | 14.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 46 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 561 | 12.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 47 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 561 | 12.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 48 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 557 | 11.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 49 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 557 | 10.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 50 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 556 | 11.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |

## Citation cycle break targets

4 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 10 | `wave_direct_dm_h025_fam2_seed1_followup_note` | medium | unaudited |
| 2 | `cycle-0002` | 2 | 7 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |
| 3 | `cycle-0003` | 2 | 7 | `yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25` | medium | unaudited |
| 4 | `cycle-0004` | 3 | 7 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |

Full queue lives in `data/audit_queue.json`.
