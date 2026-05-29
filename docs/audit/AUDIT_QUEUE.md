# Audit Queue

**Total pending:** 1209
**Ready (all deps already at retained-grade or metadata tiers):** 58

By criticality:
- `critical`: 254
- `high`: 319
- `medium`: 322
- `leaf`: 314

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem | audit_in_progress | critical | 909 | 13.33 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_per_site_hilbert_dim_two_check.py` |
| 2 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 900 | 10.81 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 3 | `no_per_site_chirality_theorem_note_2026-05-02` | no_go | unaudited | critical | 875 | 13.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/no_per_site_chirality_check.py` |
| 4 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 711 | 30.48 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_structure_narrow_spectrum.py` |
| 5 | `s3_general_r_derivation_note` | bounded_theorem | unaudited | critical | 709 | 18.47 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 6 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | positive_theorem | unaudited | critical | 525 | 12.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 7 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | bounded_theorem | unaudited | critical | 384 | 16.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 8 | `hw1_second_order_return_shape_theorem_note` | positive_theorem | unaudited | critical | 292 | 14.20 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hw1_second_order_return_shape_theorem.py` |
| 9 | `dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 255 | 10.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_equilibrium_conversion_theorem.py` |
| 10 | `omega_lambda_derivation_note` | bounded_theorem | audit_in_progress | critical | 253 | 13.99 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_omega_lambda_arithmetic_cascade.py` |
| 11 | `dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16` | bounded_theorem | unaudited | critical | 253 | 11.49 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py` |
| 12 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 907 | 15.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 13 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 899 | 17.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 14 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 899 | 11.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 15 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 898 | 10.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 16 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 897 | 11.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 17 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 896 | 15.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 18 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 896 | 14.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 19 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 896 | 12.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 20 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 895 | 16.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 21 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 895 | 13.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 22 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 894 | 19.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 23 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 892 | 20.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 24 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 889 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 25 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 887 | 18.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 26 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 869 | 39.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 27 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 723 | 38.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 28 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 703 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 29 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 677 | 26.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 30 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 633 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 31 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 631 | 27.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 32 | `yt_boundary_theorem` | open_gate | unaudited | critical | 631 | 15.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 33 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 620 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 34 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 617 | 14.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 35 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 611 | 10.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 36 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 610 | 27.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 37 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 594 | 17.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 38 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 583 | 10.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 39 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 582 | 11.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 40 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 581 | 14.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 41 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 580 | 10.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 42 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 579 | 15.68 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 43 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 577 | 32.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 44 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 577 | 13.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 45 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 576 | 11.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 46 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 575 | 31.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 47 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 575 | 22.67 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 48 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 575 | 12.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 49 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 574 | 14.17 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 50 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 572 | 12.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |

Full queue lives in `data/audit_queue.json`.
