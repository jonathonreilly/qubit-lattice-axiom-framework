# Audit Queue

**Total pending:** 1241
**Ready (all deps already at retained-grade or metadata tiers):** 62

By criticality:
- `critical`: 248
- `high`: 338
- `medium`: 333
- `leaf`: 322

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `planck_target3_clifford_phase_bridge_theorem_note_2026-04-25` | bounded_theorem | unaudited | critical | 898 | 18.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_target3_conditional_clifford_carrier_repair.py` |
| 2 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 895 | 27.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_spin_basis_single_step_psd_failure.py` |
| 3 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 889 | 13.80 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 4 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 887 | 10.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 5 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 727 | 53.51 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 6 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 705 | 19.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 7 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 700 | 30.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_structure_narrow_spectrum.py` |
| 8 | `yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26` | bounded_theorem | unaudited | critical | 520 | 9.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_declared_anchor_bounded_subchain.py` |
| 9 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | positive_theorem | unaudited | critical | 516 | 12.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 10 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | bounded_theorem | unaudited | critical | 377 | 16.56 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 11 | `gravity_clean_derivation_note` | bounded_theorem | unaudited | critical | 280 | 17.63 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 12 | `sm_relativistic_dof_count_import_note_2026-05-17` | bounded_theorem | audit_in_progress | critical | 251 | 9.48 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_relativistic_dof_finite_inventory.py` |
| 13 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 897 | 19.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 14 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 894 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 15 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 886 | 11.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 16 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 885 | 10.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 17 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 884 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 18 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 883 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 19 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 883 | 14.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 20 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 882 | 16.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 21 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 881 | 19.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 22 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 881 | 13.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 23 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 879 | 20.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 24 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 876 | 13.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 25 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 874 | 18.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 26 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 856 | 39.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 27 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 714 | 37.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 28 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 699 | 18.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 29 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 693 | 12.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 30 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 662 | 25.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 31 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 624 | 13.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 32 | `yt_boundary_theorem` | open_gate | unaudited | critical | 622 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 33 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 621 | 27.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 34 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 611 | 11.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 35 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 608 | 14.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 36 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 602 | 10.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 37 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 601 | 27.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 38 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 585 | 17.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 39 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 574 | 10.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 40 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 573 | 11.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 41 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 572 | 14.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 42 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 571 | 10.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 43 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 570 | 15.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 44 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 568 | 32.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 45 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 568 | 13.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 46 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 567 | 11.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 47 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 566 | 31.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 48 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 566 | 22.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 49 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 566 | 12.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 50 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 565 | 14.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |

## Citation cycle break targets

4 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 10 | `wave_direct_dm_h025_fam2_seed1_followup_note` | medium | unaudited |
| 2 | `cycle-0002` | 2 | 7 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |
| 3 | `cycle-0003` | 2 | 7 | `yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25` | medium | unaudited |
| 4 | `cycle-0004` | 3 | 7 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |

Full queue lives in `data/audit_queue.json`.
