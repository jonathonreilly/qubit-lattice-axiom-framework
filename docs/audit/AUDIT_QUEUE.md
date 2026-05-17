# Audit Queue

**Total pending:** 1242
**Ready (all deps already at retained-grade or metadata tiers):** 24

By criticality:
- `critical`: 431
- `high`: 162
- `medium`: 320
- `leaf`: 329

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `neutrino_mass_reduction_to_dirac_note` | positive_theorem | unaudited | critical | 815 | 16.17 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_neutrino_mass_reduction_to_dirac.py` |
| 2 | `gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note` | positive_theorem | unaudited | critical | 963 | 14.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py` |
| 3 | `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note` | open_gate | unaudited | critical | 961 | 15.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py` |
| 4 | `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` | positive_theorem | unaudited | critical | 960 | 13.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py` |
| 5 | `gauge_vacuum_plaquette_bridge_support_note` | positive_theorem | unaudited | critical | 955 | 13.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py` |
| 6 | `gauge_vacuum_plaquette_susceptibility_flow_theorem_note` | bounded_theorem | unaudited | critical | 955 | 12.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py` |
| 7 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 954 | 30.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency.py` |
| 8 | `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | unaudited | critical | 906 | 13.82 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_qcd_low_energy_running_bridge.py` |
| 9 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 905 | 38.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 10 | `yt_vertex_power_derivation` | open_gate | unaudited | critical | 896 | 12.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 11 | `yt_ward_identity_derivation_theorem` | bounded_theorem | unaudited | critical | 893 | 36.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 12 | `yt_color_projection_correction_note` | bounded_theorem | unaudited | critical | 874 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_color_projection_correction.py` |
| 13 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 873 | 14.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 14 | `yt_boundary_theorem` | open_gate | unaudited | critical | 871 | 16.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 15 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 868 | 17.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 16 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 857 | 10.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 17 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 856 | 11.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 18 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 855 | 14.74 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 19 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 854 | 11.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 20 | `three_generation_observable_theorem_note` | bounded_theorem | unaudited | critical | 853 | 47.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_theorem.py` |
| 21 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 853 | 16.24 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 22 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 851 | 13.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 23 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 850 | 12.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 24 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 849 | 12.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 25 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 848 | 14.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 26 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 847 | 30.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 27 | `g_bare_structural_normalization_theorem_note_2026-04-18` | positive_theorem | unaudited | critical | 846 | 18.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_structural_normalization.py` |
| 28 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 846 | 13.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 29 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 846 | 13.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 30 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 842 | 11.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 31 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 842 | 11.22 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 32 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 841 | 11.72 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |
| 33 | `yt_exact_schur_normal_form_uniqueness_note` | bounded_theorem | unaudited | critical | 839 | 16.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_schur_normal_form_uniqueness.py` |
| 34 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | positive_theorem | unaudited | critical | 832 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 35 | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 832 | 12.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_per_site_hilbert_dim_two_check.py` |
| 36 | `yt_p2_taste_staircase_transport_note_2026-04-17` | open_gate | unaudited | critical | 831 | 11.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_transport.py` |
| 37 | `wilson_bz_corner_hamming_staircase_bounded_note_2026-05-08` | bounded_theorem | unaudited | critical | 830 | 14.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_wilson_bz_corner_hamming_staircase.py` |
| 38 | `uv_gauge_to_yukawa_bridge_sc_vs_pert_note` | positive_theorem | unaudited | critical | 830 | 12.70 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 39 | `yt_p2_v_matching_theorem_note_2026-04-17` | bounded_theorem | unaudited | critical | 830 | 12.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_v_matching.py` |
| 40 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 830 | 10.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 41 | `yt_p2_taste_staircase_beta_functions_note_2026-04-17` | no_go | unaudited | critical | 829 | 14.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p2_taste_staircase_beta.py` |
| 42 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 829 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 43 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 829 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 44 | `poisson_self_gravity_loop_note` | bounded_theorem | unaudited | critical | 828 | 13.20 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/poisson_self_gravity_loop.py` |
| 45 | `higgs_mass_from_axiom_note` | bounded_theorem | unaudited | critical | 827 | 25.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/higgs_tree_level_mean_field_runner_2026_05_03.py` |
| 46 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 827 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 47 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | positive_theorem | unaudited | critical | 827 | 12.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` |
| 48 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 825 | 25.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reflection_positivity_check.py` |
| 49 | `g_bare_hilbert_schmidt_rigidity_theorem_note_2026-05-07` | positive_theorem | unaudited | critical | 824 | 23.69 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_audit_residual_closure.py` |
| 50 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | positive_theorem | unaudited | critical | 824 | 12.19 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_h_unit_renormalization.py` |

## Citation cycle break targets

53 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 814 | `koide_a1_11_probe_campaign_bounded_admission_meta_note_2026-05-08` | critical | unaudited |
| 2 | `cycle-0002` | 2 | 814 | `koide_a1_11_probe_campaign_bounded_admission_meta_note_2026-05-08` | critical | unaudited |
| 3 | `cycle-0003` | 8 | 814 | `dm_leptogenesis_exact_kernel_closure_note_2026-04-15` | critical | unaudited |
| 4 | `cycle-0004` | 8 | 814 | `koide_brannen_phase_reduction_theorem_note_2026-04-20` | critical | unaudited |
| 5 | `cycle-0005` | 8 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |
| 6 | `cycle-0006` | 8 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |
| 7 | `cycle-0007` | 9 | 814 | `dm_leptogenesis_exact_kernel_closure_note_2026-04-15` | critical | unaudited |
| 8 | `cycle-0008` | 9 | 814 | `koide_brannen_phase_reduction_theorem_note_2026-04-20` | critical | unaudited |
| 9 | `cycle-0009` | 9 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |
| 10 | `cycle-0010` | 10 | 814 | `a3_option_c_brannen_rivero_physical_lattice_bounded_obstruction_note_2026-05-08_optc` | critical | unaudited |
| 11 | `cycle-0011` | 10 | 814 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | critical | unaudited |
| 12 | `cycle-0012` | 10 | 814 | `a3_route2_single_clock_c3_obstruction_note_2026-05-08_r2` | critical | unaudited |
| 13 | `cycle-0013` | 10 | 814 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 14 | `cycle-0014` | 10 | 814 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 15 | `cycle-0015` | 10 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |
| 16 | `cycle-0016` | 10 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |
| 17 | `cycle-0017` | 11 | 814 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 18 | `cycle-0018` | 11 | 814 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | critical | unaudited |
| 19 | `cycle-0019` | 11 | 814 | `a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5` | critical | unaudited |
| 20 | `cycle-0020` | 11 | 814 | `a3_r5_hostile_review_confirms_obstruction_note_2026-05-08_r5hr` | critical | unaudited |
| 21 | `cycle-0021` | 11 | 814 | `anomaly_forces_time_theorem` | critical | unaudited |
| 22 | `cycle-0022` | 11 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |
| 23 | `cycle-0023` | 11 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |
| 24 | `cycle-0024` | 11 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |
| 25 | `cycle-0025` | 11 | 814 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
