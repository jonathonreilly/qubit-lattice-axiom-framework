# Audit Queue

**Total pending:** 1252
**Ready (all deps already at retained-grade or metadata tiers):** 24

By criticality:
- `critical`: 256
- `high`: 349
- `medium`: 331
- `leaf`: 316

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 895 | 16.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 2 | `planck_target3_clifford_phase_bridge_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 882 | 18.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_target3_clifford_phase_bridge.py` |
| 3 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 880 | 26.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reflection_positivity_check.py` |
| 4 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 871 | 13.77 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 5 | `yt_ew_color_projection_theorem` | bounded_theorem | unaudited | critical | 550 | 34.11 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 6 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 881 | 19.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 7 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 878 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 8 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 872 | 13.77 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 9 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 871 | 11.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 10 | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | bounded_theorem | unaudited | critical | 871 | 10.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py` |
| 11 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 871 | 10.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 12 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 870 | 11.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 13 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 869 | 17.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 14 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 869 | 10.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 15 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 868 | 11.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 16 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 867 | 14.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 17 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 867 | 14.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 18 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 867 | 10.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 19 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 866 | 15.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 20 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 866 | 13.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 21 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 865 | 19.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 22 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 864 | 12.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 23 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 863 | 19.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 24 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 859 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 25 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 857 | 17.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 26 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 841 | 38.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 27 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 707 | 37.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 28 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 698 | 19.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 29 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 692 | 18.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 30 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 689 | 10.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |
| 31 | `s3_time_theta_to_slice_coupling_note` | open_gate | unaudited | critical | 688 | 10.93 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 32 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 686 | 30.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 33 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 686 | 12.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 34 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 649 | 25.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 35 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 617 | 13.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 36 | `yt_boundary_theorem` | open_gate | unaudited | critical | 615 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 37 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 608 | 27.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 38 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 604 | 11.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 39 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 601 | 14.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 40 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 595 | 10.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 41 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 594 | 27.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 42 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 578 | 17.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 43 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 567 | 10.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 44 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 566 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 45 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 565 | 14.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 46 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 564 | 10.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 47 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 563 | 15.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 48 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 561 | 32.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 49 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 561 | 13.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 50 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 560 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |

Full queue lives in `data/audit_queue.json`.
