# Audit Queue

**Total pending:** 1244
**Ready (all deps already at retained-grade or metadata tiers):** 20

By criticality:
- `critical`: 250
- `high`: 344
- `medium`: 324
- `leaf`: 326

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 883 | 19.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 2 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 880 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 3 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 874 | 13.77 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 4 | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | bounded_theorem | unaudited | critical | 873 | 10.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py` |
| 5 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 873 | 10.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 6 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 872 | 11.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 7 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 871 | 17.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 8 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 871 | 10.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 9 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 870 | 11.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 10 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 869 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 11 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 869 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 12 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 869 | 10.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 13 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 868 | 15.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 14 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 868 | 13.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 15 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 867 | 19.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 16 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 866 | 12.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 17 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 865 | 19.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 18 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 861 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 19 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 859 | 17.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 20 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 843 | 38.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 21 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 707 | 37.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 22 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 698 | 19.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 23 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 692 | 18.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 24 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 689 | 10.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |
| 25 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 688 | 30.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 26 | `s3_time_theta_to_slice_coupling_note` | open_gate | unaudited | critical | 688 | 10.93 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 27 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 686 | 12.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 28 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 651 | 25.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 29 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 617 | 13.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 30 | `yt_boundary_theorem` | open_gate | unaudited | critical | 615 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 31 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 610 | 27.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 32 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 604 | 11.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 33 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 601 | 14.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 34 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 595 | 10.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 35 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 594 | 27.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 36 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 578 | 17.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 37 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 567 | 10.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 38 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 566 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 39 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 565 | 14.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 40 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 564 | 10.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 41 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 563 | 15.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 42 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 561 | 32.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 43 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 561 | 13.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 44 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 560 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 45 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 559 | 31.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 46 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 559 | 22.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 47 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 559 | 12.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 48 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 558 | 14.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 49 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 556 | 12.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 50 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 556 | 12.62 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |

## Citation cycle break targets

3 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 5 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |
| 2 | `cycle-0002` | 2 | 5 | `yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25` | medium | unaudited |
| 3 | `cycle-0003` | 3 | 5 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |

Full queue lives in `data/audit_queue.json`.
