# Audit Queue

**Total pending:** 1303
**Ready (all deps already at retained-grade or metadata tiers):** 45

By criticality:
- `critical`: 273
- `high`: 349
- `medium`: 339
- `leaf`: 342

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 994 | 12.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 2 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 870 | 25.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reflection_positivity_check.py` |
| 3 | `reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10` | bounded_theorem | audit_in_progress | critical | 865 | 14.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_reflection_positivity_gauge_half_cauchy_schwarz_exact_2026_05_10.py` |
| 4 | `staggered_only_det_positivity_case_a_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 864 | 10.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_only_det_positivity_case_a_2026-05-17.py` |
| 5 | `strong_cp_operator_basis_and_mass_orientation_theorem_note_2026-05-19` | bounded_theorem | unaudited | critical | 863 | 10.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py` |
| 6 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 862 | 10.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 7 | `yt_color_projection_correction_note` | no_go | unaudited | critical | 603 | 15.24 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 8 | `dm_leptogenesis_pmns_analytic_stationary_classification_theorem_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 347 | 9.44 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_analytic_stationary_classification_theorem.py` |
| 9 | `dm_leptogenesis_pmns_minimum_information_source_law_note_2026-04-16` | bounded_theorem | unaudited | critical | 346 | 12.94 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py` |
| 10 | `koide_mru_weight_class_obstruction_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 143 | 15.67 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_mru_weight_class_obstruction_theorem.py` |
| 11 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 999 | 13.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 12 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 994 | 13.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 13 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 993 | 31.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 14 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 935 | 13.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 15 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 934 | 38.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 16 | `left_handed_charge_matching_note` | bounded_theorem | unaudited | critical | 932 | 28.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_graph_first_su3_integration.py` |
| 17 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 925 | 12.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 18 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 922 | 37.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 19 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 891 | 47.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 20 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 886 | 16.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 21 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 884 | 18.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 22 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 872 | 19.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 23 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 869 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 24 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 863 | 13.76 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 25 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 862 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 26 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 862 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 27 | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | bounded_theorem | unaudited | critical | 862 | 10.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py` |
| 28 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 861 | 11.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 29 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 860 | 17.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 30 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 860 | 10.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 31 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 859 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 32 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 858 | 14.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 33 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 858 | 14.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 34 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 858 | 10.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 35 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 857 | 15.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 36 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 857 | 13.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 37 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 856 | 19.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 38 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 855 | 12.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 39 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 854 | 19.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 40 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 850 | 13.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 41 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 849 | 11.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 42 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 848 | 17.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 43 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 832 | 38.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 44 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 688 | 19.93 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 45 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 683 | 18.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 46 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 680 | 10.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |
| 47 | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 679 | 18.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py` |
| 48 | `s3_time_theta_to_slice_coupling_note` | open_gate | unaudited | critical | 679 | 10.91 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 49 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 677 | 30.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 50 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 677 | 12.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |

Full queue lives in `data/audit_queue.json`.
