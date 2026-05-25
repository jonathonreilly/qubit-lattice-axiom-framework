# Audit Queue

**Total pending:** 1230
**Ready (all deps already at retained-grade or metadata tiers):** 2

By criticality:
- `critical`: 255
- `high`: 341
- `medium`: 328
- `leaf`: 306

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 904 | 13.82 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 2 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 899 | 10.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 3 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 898 | 13.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 4 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 896 | 12.81 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 5 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 891 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 6 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 889 | 17.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 7 | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | bounded_theorem | unaudited | critical | 888 | 10.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py` |
| 8 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 886 | 17.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 9 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 886 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 10 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 886 | 10.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 11 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 885 | 11.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 12 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 884 | 14.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 13 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 884 | 10.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 14 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 883 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 15 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 882 | 38.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 16 | `planck_primitive_coframe_boundary_carrier_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 882 | 20.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_primitive_coframe_boundary_carrier.py` |
| 17 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 882 | 19.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 18 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 882 | 19.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 19 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 882 | 19.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 20 | `planck_target3_clifford_phase_bridge_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 882 | 18.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_target3_clifford_phase_bridge.py` |
| 21 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 882 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 22 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 882 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 23 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 882 | 14.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 24 | `planck_link_local_first_variation_p_a_forcing_theorem_note_2026-04-30` | positive_theorem | unaudited | critical | 882 | 13.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_link_local_first_variation_p_a_forcing.py` |
| 25 | `planck_primitive_clifford_majorana_edge_derivation_theorem_note_2026-04-30` | bounded_theorem | unaudited | critical | 882 | 13.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_primitive_clifford_majorana_edge_derivation.py` |
| 26 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 707 | 37.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 27 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 698 | 19.95 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 28 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 692 | 18.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 29 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 689 | 10.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |
| 30 | `s3_time_theta_to_slice_coupling_note` | open_gate | unaudited | critical | 688 | 10.93 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 31 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 686 | 30.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 32 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 686 | 12.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 33 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 649 | 25.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 34 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 617 | 13.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 35 | `yt_boundary_theorem` | open_gate | unaudited | critical | 615 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 36 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 608 | 27.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 37 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 604 | 11.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 38 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 601 | 14.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 39 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 595 | 10.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 40 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 594 | 27.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 41 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 578 | 17.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 42 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 567 | 10.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 43 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 566 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 44 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 565 | 14.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 45 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 564 | 10.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 46 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 563 | 15.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 47 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 561 | 32.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_cp_phase_structural_identity.py` |
| 48 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 561 | 13.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 49 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 560 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 50 | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 559 | 31.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wolfenstein_lambda_a_structural_identities.py` |

## Citation cycle break targets

8 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 6 | 882 | `anomaly_forces_time_theorem` | critical | unaudited |
| 2 | `cycle-0002` | 7 | 882 | `anomaly_forces_time_theorem` | critical | unaudited |
| 3 | `cycle-0003` | 8 | 882 | `anomaly_forces_time_theorem` | critical | unaudited |
| 4 | `cycle-0004` | 2 | 415 | `charged_lepton_ue_identity_via_z3_trichotomy_note_2026-04-17` | critical | unaudited |
| 5 | `cycle-0005` | 2 | 5 | `nn_lattice_rescaled_c_arm_derivation_note_2026-05-10` | high | unaudited |
| 6 | `cycle-0006` | 3 | 5 | `nn_lattice_rescaled_c_arm_alpha_constrained_refit_note_2026-05-10` | medium | unaudited |
| 7 | `cycle-0007` | 3 | 5 | `nn_lattice_rescaled_c_arm_derivation_note_2026-05-10` | high | unaudited |
| 8 | `cycle-0008` | 2 | 2 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | medium | unaudited |

Full queue lives in `data/audit_queue.json`.
