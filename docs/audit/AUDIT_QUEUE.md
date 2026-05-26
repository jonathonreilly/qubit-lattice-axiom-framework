# Audit Queue

**Total pending:** 1258
**Ready (all deps already at retained-grade or metadata tiers):** 69

By criticality:
- `critical`: 238
- `high`: 359
- `medium`: 334
- `leaf`: 327

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `r_base_group_theory_derivation_theorem_note_2026-04-24` | bounded_theorem | unaudited | critical | 255 | 18.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_r_base_group_theory_derivation.py` |
| 2 | `g_bare_hilbert_schmidt_rigidity_theorem_note_2026-05-07` | positive_theorem | unaudited | critical | 207 | 21.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_audit_residual_closure.py` |
| 3 | `gate_b_farfield_note` | bounded_theorem | unaudited | critical | 122 | 14.44 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_farfield_harness.py` |
| 4 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 888 | 19.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 5 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 885 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 6 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 878 | 10.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 7 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 877 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 8 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 876 | 10.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 9 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 875 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 10 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 874 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 11 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 874 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 12 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 873 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 13 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 872 | 19.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 14 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 871 | 12.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 15 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 870 | 19.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 16 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 866 | 13.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 17 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 864 | 17.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 18 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 848 | 38.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 19 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 711 | 37.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 20 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 696 | 18.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 21 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 690 | 12.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 22 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 656 | 25.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 23 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 621 | 13.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 24 | `yt_boundary_theorem` | open_gate | unaudited | critical | 619 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 25 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 615 | 27.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 26 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 608 | 11.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 27 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 605 | 14.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 28 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 599 | 10.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 29 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 598 | 27.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 30 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 582 | 17.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 31 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 571 | 10.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 32 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 570 | 11.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 33 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 569 | 14.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 34 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 568 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 35 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 567 | 15.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 36 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 565 | 32.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 37 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 565 | 13.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 38 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 564 | 11.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 39 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 563 | 31.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 40 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 563 | 22.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 41 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 563 | 12.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 42 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 562 | 14.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 43 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 560 | 12.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 44 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 560 | 12.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 45 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 556 | 11.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 46 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 556 | 10.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 47 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 555 | 11.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 48 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 553 | 27.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 49 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 553 | 16.61 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 50 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 548 | 17.60 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |

## Citation cycle break targets

3 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 7 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |
| 2 | `cycle-0002` | 2 | 7 | `yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25` | medium | unaudited |
| 3 | `cycle-0003` | 3 | 7 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |

Full queue lives in `data/audit_queue.json`.
