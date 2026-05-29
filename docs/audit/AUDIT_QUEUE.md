# Audit Queue

**Total pending:** 1136
**Ready (all deps already at retained-grade or metadata tiers):** 2

By criticality:
- `critical`: 242
- `high`: 315
- `medium`: 297
- `leaf`: 282

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 908 | 15.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 2 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 900 | 17.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 3 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 900 | 11.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 4 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 899 | 10.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 5 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 898 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 6 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 897 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 7 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 897 | 14.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 8 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 897 | 12.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 9 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 896 | 16.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 10 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 896 | 13.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 11 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 895 | 19.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 12 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 893 | 20.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 13 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 890 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 14 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 888 | 18.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 15 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 870 | 39.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 16 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 724 | 38.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 17 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 704 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 18 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 678 | 26.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 19 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 634 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 20 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 632 | 27.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 21 | `yt_boundary_theorem` | open_gate | unaudited | critical | 632 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 22 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 621 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 23 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 618 | 14.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 24 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 612 | 10.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 25 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 611 | 27.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 26 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 595 | 17.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 27 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 584 | 10.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 28 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 583 | 11.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 29 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 582 | 14.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 30 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 581 | 10.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 31 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 580 | 15.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 32 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 578 | 32.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 33 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 578 | 13.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 34 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 577 | 11.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 35 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 576 | 31.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 36 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 576 | 22.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 37 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 576 | 12.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 38 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 575 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 39 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 573 | 12.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 40 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 573 | 12.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 41 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 569 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 42 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 569 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 43 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 568 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 44 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 566 | 27.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 45 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 566 | 16.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 46 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 563 | 18.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 47 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 527 | 10.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 48 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 526 | 11.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 49 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 525 | 13.54 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 50 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 524 | 11.04 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |

## Citation cycle break targets

1 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 496 | `higgs_channel_effective_ntaste_boundary_bounded_note_2026-05-08` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
