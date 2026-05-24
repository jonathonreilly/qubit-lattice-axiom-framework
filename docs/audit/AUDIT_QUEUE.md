# Audit Queue

**Total pending:** 1246
**Ready (all deps already at retained-grade or metadata tiers):** 6

By criticality:
- `critical`: 258
- `high`: 342
- `medium`: 328
- `leaf`: 318

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1020 | 31.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 2 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 971 | 13.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 3 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 970 | 38.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 4 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 961 | 12.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 5 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 958 | 37.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 6 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 910 | 18.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 7 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 899 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 8 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 897 | 13.81 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 9 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 894 | 10.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 10 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 893 | 13.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 11 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 891 | 12.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 12 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 886 | 13.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 13 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 885 | 11.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 14 | `strong_cp_operator_basis_and_mass_orientation_theorem_note_2026-05-19` | bounded_theorem | unaudited | critical | 885 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py` |
| 15 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 884 | 17.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 16 | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | bounded_theorem | unaudited | critical | 884 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py` |
| 17 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 881 | 17.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 18 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 881 | 11.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 19 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 880 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 20 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 879 | 14.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 21 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 879 | 10.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 22 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 878 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 23 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 877 | 38.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 24 | `planck_primitive_coframe_boundary_carrier_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 877 | 20.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_primitive_coframe_boundary_carrier.py` |
| 25 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 877 | 19.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 26 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 877 | 19.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 27 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 877 | 19.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 28 | `planck_target3_clifford_phase_bridge_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 877 | 18.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_target3_clifford_phase_bridge.py` |
| 29 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 877 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 30 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 877 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 31 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 877 | 14.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 32 | `planck_link_local_first_variation_p_a_forcing_theorem_note_2026-04-30` | positive_theorem | unaudited | critical | 877 | 13.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_link_local_first_variation_p_a_forcing.py` |
| 33 | `planck_primitive_clifford_majorana_edge_derivation_theorem_note_2026-04-30` | bounded_theorem | unaudited | critical | 877 | 13.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_primitive_clifford_majorana_edge_derivation.py` |
| 34 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 692 | 19.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 35 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 687 | 18.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 36 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 684 | 10.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |
| 37 | `s3_time_theta_to_slice_coupling_note` | open_gate | unaudited | critical | 683 | 10.92 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 38 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 681 | 30.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 39 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 681 | 12.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 40 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 644 | 25.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 41 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 607 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 42 | `yt_boundary_theorem` | open_gate | unaudited | critical | 605 | 15.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 43 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 598 | 27.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 44 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 594 | 11.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 45 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 591 | 14.21 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 46 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 585 | 10.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 47 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 584 | 27.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 48 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 568 | 17.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 49 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 557 | 10.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 50 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 556 | 11.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |

## Citation cycle break targets

3 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 6 | 877 | `anomaly_forces_time_theorem` | critical | unaudited |
| 2 | `cycle-0002` | 7 | 877 | `anomaly_forces_time_theorem` | critical | unaudited |
| 3 | `cycle-0003` | 8 | 877 | `anomaly_forces_time_theorem` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
