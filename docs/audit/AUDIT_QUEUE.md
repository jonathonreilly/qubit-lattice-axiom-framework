# Audit Queue

**Total pending:** 1294
**Ready (all deps already at retained-grade or metadata tiers):** 22

By criticality:
- `critical`: 315
- `high`: 310
- `medium`: 340
- `leaf`: 329

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `staggered_dirac_realization_gate_note_2026-05-03` | open_gate | unaudited | critical | 1006 | 29.98 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 2 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 870 | 25.77 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reflection_positivity_check.py` |
| 3 | `reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10` | bounded_theorem | audit_in_progress | critical | 865 | 14.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_reflection_positivity_gauge_half_cauchy_schwarz_exact_2026_05_10.py` |
| 4 | `staggered_only_det_positivity_case_a_note_2026-05-17` | positive_theorem | audit_in_progress | critical | 864 | 10.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_only_det_positivity_case_a_2026-05-17.py` |
| 5 | `strong_cp_operator_basis_and_mass_orientation_theorem_note_2026-05-19` | bounded_theorem | unaudited | critical | 863 | 10.76 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py` |
| 6 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 862 | 10.75 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 7 | `dm_leptogenesis_pmns_analytic_stationary_classification_theorem_note_2026-04-16` | bounded_theorem | audit_in_progress | critical | 360 | 9.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_analytic_stationary_classification_theorem.py` |
| 8 | `dm_leptogenesis_pmns_minimum_information_source_law_note_2026-04-16` | bounded_theorem | unaudited | critical | 359 | 12.99 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py` |
| 9 | `dm_leptogenesis_pmns_relative_action_stationarity_theorem_note_2026-04-16` | bounded_theorem | unaudited | critical | 294 | 10.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py` |
| 10 | `koide_mru_weight_class_obstruction_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 143 | 15.67 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_mru_weight_class_obstruction_theorem.py` |
| 11 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1003 | 15.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 12 | `g_bare_derivation_note` | positive_theorem | unaudited | critical | 1002 | 18.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 13 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1001 | 16.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 14 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 999 | 13.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 15 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 994 | 13.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 16 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 994 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 17 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 993 | 31.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 18 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 935 | 13.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 19 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 934 | 38.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 20 | `left_handed_charge_matching_note` | bounded_theorem | unaudited | critical | 932 | 28.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_graph_first_su3_integration.py` |
| 21 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 925 | 12.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 22 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 922 | 37.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 23 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 891 | 47.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 24 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 886 | 16.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 25 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 884 | 18.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 26 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 872 | 19.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 27 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 869 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 28 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 863 | 13.76 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 29 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 862 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 30 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 862 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 31 | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | bounded_theorem | unaudited | critical | 862 | 10.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py` |
| 32 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 861 | 11.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 33 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 860 | 17.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 34 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 860 | 10.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 35 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 859 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 36 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 858 | 14.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 37 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 858 | 14.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 38 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 858 | 10.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 39 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 857 | 15.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 40 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 857 | 13.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 41 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 856 | 19.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 42 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 855 | 12.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 43 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 854 | 19.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 44 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 850 | 13.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 45 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 849 | 11.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 46 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 848 | 17.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 47 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 832 | 38.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 48 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 693 | 19.94 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 49 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 688 | 18.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 50 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 685 | 10.42 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |

## Citation cycle break targets

17 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 4 | 503 | `universal_gr_a1_invariant_section_note` | critical | unaudited |
| 2 | `cycle-0002` | 4 | 503 | `universal_gr_a1_invariant_section_note` | critical | unaudited |
| 3 | `cycle-0003` | 10 | 286 | `axiom_first_stefan_boltzmann_theorem_note_2026-05-01` | critical | unaudited |
| 4 | `cycle-0004` | 8 | 214 | `koide_brannen_phase_reduction_theorem_note_2026-04-20` | high | unaudited |
| 5 | `cycle-0005` | 9 | 214 | `koide_brannen_phase_reduction_theorem_note_2026-04-20` | high | unaudited |
| 6 | `cycle-0006` | 2 | 176 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | high | unaudited |
| 7 | `cycle-0007` | 2 | 82 | `cosmological_constant_spectral_gap_identity_theorem_note` | critical | unaudited |
| 8 | `cycle-0008` | 3 | 82 | `cosmological_constant_spectral_gap_identity_theorem_note` | critical | unaudited |
| 9 | `cycle-0009` | 2 | 21 | `wave_direct_dm_h025_fam2_seed1_control_note` | high | unaudited |
| 10 | `cycle-0010` | 4 | 16 | `wave_direct_dm_h025_fam1_seed0_control_note` | medium | unaudited |
| 11 | `cycle-0011` | 2 | 6 | `nn_lattice_rescaled_c_arm_alpha_constrained_refit_note_2026-05-10` | medium | unaudited |
| 12 | `cycle-0012` | 3 | 6 | `nn_lattice_rescaled_c2_derivation_note_2026-05-10` | medium | unaudited |
| 13 | `cycle-0013` | 2 | 3 | `fractional_instanton_dilute_gas_condensate_external_narrow_theorem_note_2026-05-16` | leaf | unaudited |
| 14 | `cycle-0014` | 2 | 3 | `instanton_4d_action_8pi2_over_g2_external_narrow_theorem_note_2026-05-16` | leaf | unaudited |
| 15 | `cycle-0015` | 2 | 3 | `meron_half_instanton_4pi2_over_g2_external_narrow_theorem_note_2026-05-16` | leaf | unaudited |
| 16 | `cycle-0016` | 2 | 2 | `dimension_selection_note` | medium | unaudited |
| 17 | `cycle-0017` | 2 | 2 | `dt1_time_dimension_proof_walk_lattice_independence_bounded_note_2026-05-08` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
