# Audit Queue

**Total pending:** 1378
**Ready (all deps already at retained-grade or metadata tiers):** 129

By criticality:
- `critical`: 273
- `high`: 305
- `medium`: 367
- `leaf`: 433

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `no_per_site_chirality_theorem_note_2026-05-02` | no_go | audit_in_progress | critical | 935 | 14.87 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/no_per_site_chirality_check.py` |
| 2 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 774 | 56.60 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 3 | `axiom_first_lattice_noether_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 261 | 14.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_lattice_noether_check.py` |
| 4 | `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` | bounded_theorem | unaudited | critical | 148 | 17.22 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_cpt_exact_real_anti_hermitian_d_exact_2026_05_10.py` |
| 5 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 971 | 15.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py` |
| 6 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 961 | 10.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 7 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 959 | 12.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 8 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 958 | 13.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 9 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 958 | 11.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 10 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 955 | 20.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 11 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 953 | 20.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 12 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 951 | 15.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 13 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 949 | 20.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 14 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 922 | 39.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 15 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 767 | 38.09 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 16 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 748 | 12.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 17 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 726 | 26.51 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 18 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 679 | 28.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 19 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 676 | 13.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 20 | `yt_boundary_theorem` | open_gate | unaudited | critical | 674 | 15.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 21 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 662 | 11.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 22 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 659 | 14.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 23 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 653 | 10.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 24 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 652 | 27.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 25 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 636 | 17.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 26 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 625 | 10.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 27 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 624 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 28 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 623 | 14.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 29 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 622 | 10.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 30 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 621 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 31 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 619 | 32.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 32 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 619 | 13.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 33 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 618 | 11.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 34 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 617 | 31.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |
| 35 | `ckm_atlas_triangle_right_angle_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 617 | 22.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_triangle_right_angle.py` |
| 36 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 617 | 12.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 37 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 616 | 14.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 38 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 614 | 12.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 39 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 614 | 12.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 40 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 610 | 11.26 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 41 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 610 | 10.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 42 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 609 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 43 | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 607 | 27.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_magnitudes_structural_counts.py` |
| 44 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 607 | 16.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 45 | `cl3_taste_generation_theorem` | bounded_theorem | unaudited | critical | 604 | 18.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/verify_cl3_sm_embedding.py` |
| 46 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 566 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 47 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 565 | 11.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 48 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 564 | 13.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 49 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 563 | 11.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 50 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 562 | 12.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |

Full queue lives in `data/audit_queue.json`.
