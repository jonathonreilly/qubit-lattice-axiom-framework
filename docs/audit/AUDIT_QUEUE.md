# Audit Queue

**Total pending:** 1319
**Ready (all deps already at retained-grade or metadata tiers):** 32

By criticality:
- `critical`: 328
- `high`: 312
- `medium`: 344
- `leaf`: 335

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `su3_wigner_intertwiner_block3_theorem_note_2026-05-03` | bounded_theorem | audit_in_progress | critical | 1007 | 10.98 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_wigner_l3_cube_geometry.py` |
| 2 | `gauge_vacuum_plaquette_local_environment_factorization_theorem_note` | bounded_theorem | unaudited | critical | 1005 | 14.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_local_environment_factorization.py` |
| 3 | `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 1005 | 13.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 4 | `g_bare_constraint_vs_convention_theorem_note_2026-05-03` | bounded_theorem | unaudited | critical | 1005 | 11.97 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 5 | `gauge_vacuum_plaquette_hierarchy_obstruction_lemmas_bounded_note_2026-05-10` | bounded_theorem | unaudited | critical | 998 | 10.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_hierarchy_obstruction_lemmas.py` |
| 6 | `gauge_vacuum_plaquette_perron_reduction_theorem_note` | positive_theorem | unaudited | critical | 996 | 12.96 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_perron_reduction_theorem.py` |
| 7 | `gauge_vacuum_plaquette_distinct_shell_theorem_note` | bounded_theorem | unaudited | critical | 996 | 12.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_distinct_shell_theorem.py` |
| 8 | `yt_ew_color_projection_theorem` | positive_theorem | unaudited | critical | 943 | 34.38 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 9 | `yukawa_color_projection_theorem` | positive_theorem | unaudited | critical | 941 | 16.38 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ew_current_fierz_channel_decomposition.py` |
| 10 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 887 | 13.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 11 | `planck_target3_clifford_phase_bridge_theorem_note_2026-04-25` | positive_theorem | unaudited | critical | 872 | 18.27 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_planck_target3_clifford_phase_bridge.py` |
| 12 | `yt_color_projection_correction_note` | no_go | unaudited | critical | 608 | 14.25 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 13 | `su3_casimir_fundamental_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 216 | 16.26 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/su3_casimir_fundamental_check.py` |
| 14 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 1005 | 15.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 15 | `su3_wigner_intertwiner_block4_block5_theorem_note_2026-05-03` | bounded_theorem | unaudited | critical | 1005 | 13.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_su3_wigner_l3_cube_partition.py` |
| 16 | `g_bare_derivation_note` | positive_theorem | unaudited | critical | 1004 | 18.97 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_derivation.py` |
| 17 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 1003 | 16.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 18 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 1001 | 13.47 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 19 | `gauge_vacuum_plaquette_infinite_hierarchy_obstruction_note` | open_gate | unaudited | critical | 997 | 12.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_infinite_hierarchy_obstruction.py` |
| 20 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 996 | 13.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 21 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 996 | 12.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 22 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 995 | 31.46 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 23 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 934 | 13.87 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 24 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 933 | 38.37 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 25 | `left_handed_charge_matching_note` | bounded_theorem | unaudited | critical | 931 | 28.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_graph_first_su3_integration.py` |
| 26 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 924 | 12.35 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 27 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 921 | 37.85 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 28 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 893 | 47.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 29 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 886 | 18.29 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 30 | `rconn_derived_note` | bounded_theorem | unaudited | critical | 885 | 16.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_color_projection_mc.py` |
| 31 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 873 | 26.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reflection_positivity_check.py` |
| 32 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 873 | 11.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 33 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 871 | 19.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 34 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 868 | 15.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 35 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 862 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 36 | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | bounded_theorem | unaudited | critical | 862 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py` |
| 37 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 861 | 13.75 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 38 | `hopping_bilinear_hermiticity_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 861 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/hopping_bilinear_hermiticity_check.py` |
| 39 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 860 | 18.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 40 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 860 | 11.75 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 41 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 859 | 10.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 42 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 858 | 11.25 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 43 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 857 | 14.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 44 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 857 | 14.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 45 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 857 | 10.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 46 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 856 | 15.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 47 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 856 | 13.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 48 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 855 | 19.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 49 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 854 | 12.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 50 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 853 | 19.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |

## Citation cycle break targets

24 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 873 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | critical | unaudited |
| 2 | `cycle-0002` | 4 | 502 | `universal_gr_a1_invariant_section_note` | critical | unaudited |
| 3 | `cycle-0003` | 4 | 502 | `universal_gr_a1_invariant_section_note` | critical | unaudited |
| 4 | `cycle-0004` | 4 | 502 | `universal_gr_constraint_action_stationarity_note` | critical | unaudited |
| 5 | `cycle-0005` | 5 | 502 | `universal_gr_a1_invariant_section_note` | critical | unaudited |
| 6 | `cycle-0006` | 2 | 294 | `dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16` | critical | unaudited |
| 7 | `cycle-0007` | 10 | 286 | `axiom_first_stefan_boltzmann_theorem_note_2026-05-01` | critical | unaudited |
| 8 | `cycle-0008` | 8 | 214 | `koide_brannen_phase_reduction_theorem_note_2026-04-20` | high | unaudited |
| 9 | `cycle-0009` | 9 | 214 | `koide_brannen_phase_reduction_theorem_note_2026-04-20` | high | unaudited |
| 10 | `cycle-0010` | 2 | 176 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | high | unaudited |
| 11 | `cycle-0011` | 2 | 82 | `cosmological_constant_spectral_gap_identity_theorem_note` | critical | unaudited |
| 12 | `cycle-0012` | 3 | 82 | `cosmological_constant_spectral_gap_identity_theorem_note` | critical | unaudited |
| 13 | `cycle-0013` | 3 | 21 | `wave_direct_dm_h025_fam2_seed0_control_note` | high | unaudited |
| 14 | `cycle-0014` | 4 | 16 | `wave_direct_dm_h025_fam1_seed0_control_note` | medium | unaudited |
| 15 | `cycle-0015` | 2 | 14 | `lattice_3d_inverse_square_kernel_helper_note_2026-04-04` | medium | unaudited |
| 16 | `cycle-0016` | 2 | 6 | `nn_lattice_rescaled_c_arm_alpha_constrained_refit_note_2026-05-10` | medium | unaudited |
| 17 | `cycle-0017` | 3 | 6 | `nn_lattice_rescaled_c2_derivation_note_2026-05-10` | medium | unaudited |
| 18 | `cycle-0018` | 2 | 4 | `chiral_walk_synthesis_2026-04-09` | medium | unaudited |
| 19 | `cycle-0019` | 2 | 3 | `fractional_instanton_dilute_gas_condensate_external_narrow_theorem_note_2026-05-16` | leaf | unaudited |
| 20 | `cycle-0020` | 2 | 3 | `instanton_4d_action_8pi2_over_g2_external_narrow_theorem_note_2026-05-16` | leaf | unaudited |
| 21 | `cycle-0021` | 2 | 3 | `meron_half_instanton_4pi2_over_g2_external_narrow_theorem_note_2026-05-16` | leaf | unaudited |
| 22 | `cycle-0022` | 2 | 2 | `dimension_selection_note` | medium | unaudited |
| 23 | `cycle-0023` | 2 | 2 | `dt1_time_dimension_proof_walk_lattice_independence_bounded_note_2026-05-08` | leaf | unaudited |
| 24 | `cycle-0024` | 2 | 2 | `teleportation_poisson_resource_sweep_note` | leaf | unaudited |

Full queue lives in `data/audit_queue.json`.
