# Audit Queue

**Total pending:** 1326
**Ready (all deps already at retained-grade or metadata tiers):** 34

By criticality:
- `critical`: 418
- `high`: 223
- `medium`: 348
- `leaf`: 337

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `staggered_dirac_realization_gate_note_2026-05-03` | open_gate | unaudited | critical | 959 | 29.41 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 2 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 887 | 11.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 3 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | bounded_theorem | unaudited | critical | 692 | 10.44 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 4 | `universal_gr_curvature_localization_blocker_note` | positive_theorem | unaudited | critical | 506 | 10.49 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 5 | `higgs_mechanism_note` | bounded_theorem | unaudited | critical | 465 | 11.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_higgs_mass_derived.py` |
| 6 | `su3_casimir_fundamental_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 331 | 16.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/su3_casimir_fundamental_check.py` |
| 7 | `cl3_quark_antiquark_color_singlet_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 303 | 9.25 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_quark_antiquark_color_singlet_check.py` |
| 8 | `dm_leptogenesis_pmns_relative_action_stationarity_theorem_note_2026-04-16` | bounded_theorem | unaudited | critical | 295 | 10.21 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py` |
| 9 | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | bounded_theorem | unaudited | critical | 291 | 9.19 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 10 | `sm_relativistic_dof_count_import_note_2026-05-17` | bounded_theorem | unaudited | critical | 289 | 9.18 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 11 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1026 | 15.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 12 | `g_bare_derivation_note` | positive_theorem | unaudited | critical | 1025 | 19.00 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 13 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1024 | 16.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 14 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1022 | 13.50 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 15 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 1017 | 13.99 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 16 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 1017 | 12.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 17 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 1016 | 31.49 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 18 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 964 | 13.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 19 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 963 | 38.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 20 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 955 | 17.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 21 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 954 | 12.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 22 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 951 | 37.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 23 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 914 | 47.84 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 24 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 907 | 18.33 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 25 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 893 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 26 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 891 | 13.80 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 27 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 888 | 10.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 28 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 887 | 13.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 29 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 886 | 26.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reflection_positivity_check.py` |
| 30 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 885 | 12.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 31 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 880 | 13.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 32 | `fermion_parity_z2_grading_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 879 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/fermion_parity_z2_grading_check.py` |
| 33 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 878 | 17.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 34 | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | bounded_theorem | unaudited | critical | 878 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py` |
| 35 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 876 | 18.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 36 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 875 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 37 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 874 | 11.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 38 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 873 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 39 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 873 | 10.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 40 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 872 | 11.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 41 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 871 | 38.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 42 | `planck_primitive_coframe_boundary_carrier_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 871 | 20.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_primitive_coframe_boundary_carrier.py` |
| 43 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 871 | 19.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 44 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 871 | 19.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 45 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 871 | 19.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 46 | `planck_target3_clifford_phase_bridge_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 871 | 18.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_target3_clifford_phase_bridge.py` |
| 47 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 871 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 48 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 871 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 49 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 871 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 50 | `planck_link_local_first_variation_p_a_forcing_theorem_note_2026-04-30` | positive_theorem | unaudited | critical | 871 | 13.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_link_local_first_variation_p_a_forcing.py` |

## Citation cycle break targets

30 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 6 | 871 | `anomaly_forces_time_theorem` | critical | unaudited |
| 2 | `cycle-0002` | 7 | 871 | `anomaly_forces_time_theorem` | critical | unaudited |
| 3 | `cycle-0003` | 8 | 871 | `anomaly_forces_time_theorem` | critical | unaudited |
| 4 | `cycle-0004` | 8 | 391 | `dm_leptogenesis_exact_kernel_closure_note_2026-04-15` | critical | unaudited |
| 5 | `cycle-0005` | 9 | 391 | `dm_leptogenesis_exact_kernel_closure_note_2026-04-15` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 298 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 7 | `cycle-0007` | 10 | 287 | `axiom_first_stefan_boltzmann_theorem_note_2026-05-01` | critical | unaudited |
| 8 | `cycle-0008` | 16 | 287 | `c3_symmetry_preserved_interpretation_note_2026-05-08` | critical | unaudited |
| 9 | `cycle-0009` | 16 | 287 | `dm_effective_parent_one_clock_transfer_boundary_theorem_note_2026-04-18` | critical | unaudited |
| 10 | `cycle-0010` | 17 | 287 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 11 | `cycle-0011` | 17 | 287 | `dm_effective_parent_one_clock_transfer_boundary_theorem_note_2026-04-18` | critical | unaudited |
| 12 | `cycle-0012` | 18 | 287 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 13 | `cycle-0013` | 18 | 287 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 14 | `cycle-0014` | 19 | 287 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 15 | `cycle-0015` | 22 | 287 | `dm_effective_parent_one_clock_transfer_boundary_theorem_note_2026-04-18` | critical | unaudited |
| 16 | `cycle-0016` | 23 | 287 | `dm_effective_parent_one_clock_transfer_boundary_theorem_note_2026-04-18` | critical | unaudited |
| 17 | `cycle-0017` | 2 | 82 | `cosmological_constant_spectral_gap_identity_theorem_note` | critical | unaudited |
| 18 | `cycle-0018` | 3 | 82 | `cosmological_constant_spectral_gap_identity_theorem_note` | critical | unaudited |
| 19 | `cycle-0019` | 3 | 21 | `wave_direct_dm_h025_fam2_seed0_control_note` | high | unaudited |
| 20 | `cycle-0020` | 4 | 16 | `wave_direct_dm_h025_fam1_seed0_control_note` | medium | unaudited |
| 21 | `cycle-0021` | 2 | 14 | `lattice_3d_inverse_square_kernel_helper_note_2026-04-04` | medium | unaudited |
| 22 | `cycle-0022` | 2 | 6 | `nn_lattice_rescaled_c_arm_alpha_constrained_refit_note_2026-05-10` | medium | unaudited |
| 23 | `cycle-0023` | 3 | 6 | `nn_lattice_rescaled_c2_derivation_note_2026-05-10` | medium | unaudited |
| 24 | `cycle-0024` | 2 | 4 | `chiral_walk_synthesis_2026-04-09` | medium | unaudited |
| 25 | `cycle-0025` | 2 | 3 | `fractional_instanton_dilute_gas_condensate_external_narrow_theorem_note_2026-05-16` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
