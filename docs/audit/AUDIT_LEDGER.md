# Audit Ledger

**Source of truth:** `data/audit_ledger.json`
**Schema:** see [README.md](README.md), [FRESH_LOOK_REQUIREMENTS.md](FRESH_LOOK_REQUIREMENTS.md), and [ALGEBRAIC_DECORATION_POLICY.md](ALGEBRAIC_DECORATION_POLICY.md); archival handling: [STALE_NARRATIVE_POLICY.md](STALE_NARRATIVE_POLICY.md).

This file is auto-generated. Do not edit by hand. Apply audits via `scripts/apply_audit.py`, then re-run `scripts/compute_effective_status.py` and `scripts/render_audit_ledger.py`.

## Reading rule

- **Bold** = audit-ratified retained grade (`retained`, `retained_no_go`, `retained_bounded`).
- _Italic_ = clean but waiting on retained-grade chain closure (`retained_pending_chain`).
- ~~Strikethrough~~ = audit returned a non-retained verdict (`audited_failed`, `audited_conditional`, etc.). Archived failures remain non-authoritative history and cannot satisfy a live dependency chain.
- Plain = `open_gate`, `unaudited`, `audit_in_progress`, or `meta`.

Publication-facing tables MUST read `effective_status`; `claim_type` is the auditor-owned classification field.

## Summary

| effective_status | count |
|---|---:|
| **retained** | 76 |
| **retained_bounded** | 303 |
| _retained_pending_chain_ | 1 |
| open_gate | 2 |
| unaudited | 2958 |
| audit_in_progress | 1 |
| meta | 351 |
| ~~audited_numerical_match~~ | 5 |
| ~~audited_renaming~~ | 14 |
| ~~audited_conditional~~ | 25 |
| ~~audited_failed~~ | 2 |
| `decoration_under_beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10` | 1 |
| `decoration_under_cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | 1 |
| `decoration_under_d3_truncation_commensuration_criterion_bounded_theorem_note_2026-06-12` | 1 |
| `decoration_under_graph_first_su3_integration_note` | 8 |
| `decoration_under_koide_dweh_cyclic_compression_note_2026-04-18` | 1 |
| `decoration_under_lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | 1 |
| `decoration_under_linear_response_true_kubo_note` | 1 |
| `decoration_under_native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23` | 1 |

| audit_status | count |
|---|---:|
| `audit_in_progress` | 1 |
| `audited_clean` | 381 |
| `audited_conditional` | 25 |
| `audited_decoration` | 16 |
| `audited_failed` | 2 |
| `audited_numerical_match` | 5 |
| `audited_renaming` | 14 |
| `unaudited` | 3309 |

| claim_type | count |
|---|---:|
| `bounded_theorem` | 2061 |
| `decoration` | 19 |
| `meta` | 358 |
| `no_go` | 440 |
| `open_gate` | 201 |
| `positive_theorem` | 674 |

| criticality | count |
|---|---:|
| `critical` | 747 |
| `high` | 401 |
| `medium` | 960 |
| `leaf` | 1645 |

- **Retained pending chain closure:** 1
- **Citation cycles detected:** 10

### Runner classification (static heuristic)

- runners classified: 3420
- runners with (C) first-principles compute hits: 1799
- runners with (D) external comparator hits: 1102
- decoration candidates (no C, no D): 729

## Top 25 by load-bearing score (topology only)

Criticality and load-bearing score are computed from the citation graph alone. The audit lane intentionally does not use author-declared flagship status — that would let unratified framing drive audit cost on upstream support claims.

| # | claim_id | claim_type | criticality | desc | score | audit_status | effective |
|---:|---|---|---|---:|---:|---|---|
| 1 | `minimal_axioms` | meta | critical | 1989 | 231.96 | `unaudited` | meta |
| 2 | `graph_first_su3_integration_note` | positive_theorem | critical | 1612 | 64.66 | `audited_clean` | **retained** |
| 3 | `three_generation_observable_theorem_note` | bounded_theorem | critical | 1194 | 62.22 | `unaudited` | unaudited |
| 4 | `quark_route2_exact_readout_map_note_2026-04-19` | positive_theorem | critical | 197 | 61.63 | `unaudited` | unaudited |
| 5 | `observable_principle_from_axiom_note` | bounded_theorem | critical | 1054 | 61.54 | `unaudited` | unaudited |
| 6 | `plaquette_self_consistency_note` | bounded_theorem | critical | 1180 | 50.21 | `unaudited` | unaudited |
| 7 | `minimal_axioms_2026-05-03` | meta | critical | 1080 | 45.08 | `unaudited` | meta |
| 8 | `key_terminology` | meta | critical | 1202 | 44.23 | `unaudited` | meta |
| 9 | `yt_ward_identity_derivation_theorem` | bounded_theorem | critical | 953 | 39.90 | `unaudited` | unaudited |
| 10 | `anomaly_forces_time_theorem` | bounded_theorem | critical | 1319 | 39.87 | `unaudited` | unaudited |
| 11 | `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac` | bounded_theorem | critical | 432 | 39.76 | `unaudited` | unaudited |
| 12 | `alpha_s_derived_note` | bounded_theorem | critical | 1058 | 38.05 | `unaudited` | unaudited |
| 13 | `staggered_dirac_realization_gate_note_2026-05-03` | bounded_theorem | critical | 1064 | 37.56 | `unaudited` | unaudited |
| 14 | `native_gauge_closure_note` | positive_theorem | critical | 1565 | 37.11 | `audited_clean` | **retained** |
| 15 | `cl3_color_automorphism_theorem` | bounded_theorem | critical | 622 | 36.28 | `unaudited` | unaudited |
| 16 | `s3_time_theta_to_slice_coupling_note` | open_gate | critical | 124 | 35.97 | `unaudited` | unaudited |
| 17 | `koide_circulant_character_derivation_note_2026-04-18` | bounded_theorem | critical | 444 | 35.30 | `unaudited` | unaudited |
| 18 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | critical | 628 | 33.80 | `unaudited` | unaudited |
| 19 | `kinetic_isotropy_primitive` | meta | critical | 497 | 33.46 | `unaudited` | meta |
| 20 | `yt_ew_color_projection_theorem` | no_go | critical | 895 | 32.81 | `unaudited` | unaudited |
| 21 | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` | positive_theorem | critical | 874 | 32.27 | `unaudited` | unaudited |
| 22 | `cpt_exact_note` | positive_theorem | critical | 736 | 31.53 | `unaudited` | unaudited |
| 23 | `charged_lepton_koide_cone_algebraic_equivalence_note` | positive_theorem | critical | 475 | 31.39 | `unaudited` | unaudited |
| 24 | `three_generation_structure_note` | bounded_theorem | critical | 1051 | 31.04 | `unaudited` | unaudited |
| 25 | `s3_time_bilinear_tensor_primitive_note` | open_gate | critical | 1027 | 31.01 | `unaudited` | unaudited |


## Applied audits

| claim_id | claim_type | audit_status | effective | independence | auditor_family | load-bearing class | decoration parent |
|---|---|---|---|---|---|---|---|
| `s3_mass_matrix_conditional_degeneracy_note_2026-07-11` | positive_theorem | audit_in_progress | audit_in_progress | - | - | - | - |
| `acphilambda_c3_resolvent_determinant_holonomy_coupling_narrow_theorem_note_2026-07-12` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.6 | A | - |
| `acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.6 | A | - |
| `acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.6 | A | - |
| `action_crossover_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | judicial_review | codex-gpt-5.5 | C | - |
| `action_geometry_bridge_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `action_power_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `action_power_scaling_sweep_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | judicial_review | codex-gpt-5.5 | C | - |
| `action_uniqueness_audit_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | C | - |
| `affine_imaginary_slot_invariance_narrow_theorem_note_2026-05-02` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `alt_connectivity_family_basin_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `alt_connectivity_family_failure_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | B | - |
| `alt_connectivity_family_fm_transfer_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `alt_connectivity_family_sign_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `alternative_coupled_field_probe_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `anderson_phase_mu2_0001_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `architecture_portability_live_reaudit_bridge_note_2026-06-18` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | B | - |
| `architecture_portability_sweep_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `asymmetry_persistence_born_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `asymmetry_persistence_collapse_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | D | - |
| `asymmetry_persistence_joint_card_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `asymmetry_persistence_mass_scaling_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `asymmetry_persistence_mass_window_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `asymmetry_persistence_pilot_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `axiom_first_lattice_noether_abstract_bilinear_continuity_narrow_theorem_note_2026-06-06` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | A | - |
| `background_independence_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | C | - |
| `backreaction_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `bbs_rg_banach_contraction_external_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `bell_inequality_derived_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `block_gaussian_schur_marginalization_narrow_theorem_note_2026-05-02` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `bmv_entanglement_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `bmv_threebody_note_2026-04-11` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5 | C | - |
| `born_lane_comparison_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `bougerol_lacroix_oseledets_met_external_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | B | - |
| `bound_state_selection_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | judicial_review | codex-gpt-5.5 | C | - |
| `branch_entanglement_robustness_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `branching_slack_rate_projective_limit_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `broad_gravity_derivation_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | A | - |
| `causal_escape_window_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `causal_propagating_field_live_packet_note_2026-06-05` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `central_band_born_dense_sweep_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_born_largen_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_collapse_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_collapse_strength_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_dense_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_dense_joint_highn_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_dense_joint_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_dense_largen_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_layernorm_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `central_band_mass_window_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `charged_lepton_registered_mass_dft_coordinate_theorem_note_2026-07-11` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.6 | A | - |
| `chiral_3plus1d_boundary_phase_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `chiral_3plus1d_coupled_coin_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `chiral_3plus1d_recurrence_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `circulant_parity_cp_tensor_narrow_theorem_note_2026-05-02` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `circulant_response_master_identity_narrow_theorem_note_2026-05-02` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `claude_complex_action_carryover_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `claude_complex_action_grown_companion_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | positive_theorem | ~~audited_clean~~ | **retained** | judicial_review | codex-gpt-5.5 | A | - |
| `commensuration_unconditional_period_parity_lemma_narrow_theorem_note_2026-06-12` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | A | - |
| `connes_kreimer_birkhoff_factorization_external_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `continuum_limit_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `critical_exponents_topology_live_scout_note_2026-06-04` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `critical_exponents_topology_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `cross_family_universality_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `cubic_coxeter_regge_deficit_vanishing_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `cycle_battery_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `cycle_battery_scaled_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `cycle_break_frontier_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `cycle_break_slice_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `cyclic_dft_uniform_magnitude_bounded_note_2026-05-26` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `cyclic_projector_compression_narrow_theorem_note_2026-05-02` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | A | - |
| `d2_orbital_susceptibility_sign_regions_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `d2_sign_boundary_bisection_between_landmarks_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `d2_sign_boundary_mass_collapse_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `d2_sign_boundary_tracks_landau_peierls_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `d2_truncated_flow_frozen_ratio_accumulated_budget_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | C | - |
| `d3_checkerboard_step1_closed_form_parity_lemma_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | C | - |
| `d3_staggered_two_band_orbital_bounded_theorem_note_2026-06-13` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `d3_step2_range_growth_period_class_dichotomy_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `d3_truncated_closure_recurs_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `d3_truncation_commensuration_criterion_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | C | - |
| `dense_prune_guard_seed_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `depth_laurent_root_closed_form_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | C | - |
| `det_phase_harmonic_depth_state_dependent_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | C | - |
| `dimensional_gravity_table` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | B | - |
| `dirac_core_card_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `dirac_decoherence_probe_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `dirac_observable_panel_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `dirac_weak_coupling_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | C | - |
| `directional_b_density_stencil_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `dispersion_high_p_tiebreaker_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `dm_abcc_basin_finite_search_support_note_2026-04-30` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `dm_full_closure_same_surface_converged_thermal_selector_support_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | D | - |
| `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `dm_full_closure_same_surface_thermal_selector_sensitivity_boundary_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `dm_lepton_synthesis_note_2026-04-19` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5 | C | - |
| `dm_thermal_average_sommerfeld_textbook_import_note_2026-05-17` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `edge_deletion_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `edge_deletion_boundary_sweep_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `eigenvalue_anderson_phase_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `electrostatics_card_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | C | - |
| `electrostatics_superposition_proxy_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | C | - |
| `em_gravity_coexistence_2x2_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `emergent_geometry_growth_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `emergent_product_law_audit_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `emergent_product_law_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `energy_channel_induced_kernel_route_a_note_2026-07-08` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | C | - |
| `energy_covariant_rg_collapse_shifted_coupling_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `epsstar_coefficient_richardson_moff0_bounded_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `evolving_network_prototype_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `evolving_network_prototype_v2_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `evolving_network_prototype_v4_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `evolving_network_prototype_v5_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `fermion_parity_pauli_tensor_involution_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `fifth_family_complex_boundary_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `fifth_family_complex_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `fifth_family_radial_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `fifth_family_radial_fm_transfer_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `fifth_family_radial_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `fifth_family_radial_repaired_positive_packet_note_2026-05-29` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `fine_h_family_universality_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `finite_cell_two_band_closed_form_bounded_theorem_note_2026-06-13` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `finite_rank_gravity_residual_helper_note_2026-04-14` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `finite_rank_source_to_metric_theorem_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `fixed_field_complex_grown_basin_v2_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `fixed_field_family_unification_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `fixed_field_grown_transfer_scout_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `flavor_center_trace_closed_capstone_note_2026-05-30` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `flavor_doublet_metric_default_is_detr_2026-06-02` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `flavor_r_half_is_a_stationary_point_not_forced_2026-06-02` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `flavor_spin_statistics_forces_modulo_reconstruction_2026-05-31` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | A | - |
| `fm_transfer_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5 | C | - |
| `fourth_family_quadrant_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `g_bare_constraint_vs_convention_restatement_abstract_identity_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | A | - |
| `g_bare_forced_by_ward_rep_b_independence_abstract_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | A | - |
| `gate_b_grown_distance_law_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `gate_b_grown_trapping_frontier_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `gate_b_grown_trapping_frontier_v2_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `gate_b_grown_trapping_frontier_v3_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `gate_b_grown_trapping_transport_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `gate_b_local_stencil_connectivity_bridge_bounded_theorem_note_2026-06-18` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-current | A | - |
| `gate_b_no_restore_joint_package_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `gate_b_nonlabel_sign_grown_transfer_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `gauge_scalar_temporal_completion_theorem_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_exact_solve_doublet_theorem_note_2026-04-20` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_note_2026-04-19` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `gauge_vacuum_plaquette_spatial_environment_tensor_transfer_one_word_packet_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | A | - |
| `gauge_vacuum_plaquette_su3_full_slice_product_fubini_factorization_note_2026-06-06` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `generation_axiom_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `generation_dial_local_stability_grammar_2026-06-05` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.6 | A | - |
| `geometry_lane_head_to_head_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `geometry_superposition_dag_ensemble_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `global_coherence_off_scaffold_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | D | - |
| `global_coherence_predictor_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `graph_first_selector_derivation_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `graph_first_su3_integration_note` | positive_theorem | ~~audited_clean~~ | **retained** | judicial_review | codex-gpt-5.5 | A | - |
| `graph_laplacian_core_card_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `graph_scalar_plus_spinor_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `graph_true_kg_vs_cn_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `gravitational_entanglement_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5 | C | - |
| `gravitational_memory_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `gravity_observable_hierarchy_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `growing_graph_expansion_card_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `h2t_h0125_narrow_bridge_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `hard_geometry_gravity_window_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `hard_geometry_local_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | D | - |
| `harmonic_ladder_weight_law_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-current | C | - |
| `hierarchy_spatial_bc_and_u0_scaling_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `higgs_mean_field_determinant_apbc_taste_bridge_note_2026-06-06` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | A | - |
| `higher_symmetry_gravity_probe_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `hkd_correspondence_general_charts_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `hkd_entry_sum_full_l_closure_narrow_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `holographic_probe_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `i3_zero_exact_theorem_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5 | A | - |
| `independent_generators_heldout_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5 | C | - |
| `inverse_problem_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `k_dependence_review_safe_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `koide_anticommuting_operator_derivation_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.6 | A | - |
| `koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.6 | C | - |
| `koide_cone_completing_root_narrow_theorem_note_2026-05-02` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5 | A | - |
| `koide_cone_three_form_equivalence_narrow_theorem_note_2026-05-02` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5 | A | - |
| `koide_cyclic_projector_block_democracy_note_2026-04-18` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `koide_dweh_cyclic_compression_note_2026-04-18` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5 | A | - |
| `koide_gamma_axis_covariant_full_cube_orbit_law_note_2026-04-18` | positive_theorem | ~~audited_clean~~ | **retained** | judicial_review | codex-gpt-5.5 | A | - |
| `koide_gamma_orbit_cyclic_return_candidate_note_2026-04-18` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `koide_gamma_orbit_selector_bridge_note_2026-04-18` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `kraus_choi_representation_normalization_reconciled_narrow_theorem_note_2026-06-05` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.6 | A | - |
| `landau_peierls_prefactor_native_derivation_bounded_theorem_note_2026-06-13` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `lattice_3d_dense_spent_delay_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `lattice_3d_dense_spent_delay_z2_z6_endpoint_note_2026-05-29` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `lattice_3d_dense_window_extension_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `lattice_3d_l2_numpy_h0125_audit_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `lattice_3d_l2_numpy_h0125_bridge_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `lattice_3d_nyquist_diffraction_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `lattice_complementarity_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `lattice_distance_law_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `lattice_kernel_transfer_norm_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `lattice_nn_continuum_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `lattice_nn_deterministic_rescale_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `lattice_nn_distance_law_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `lattice_nn_light_cone_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.6 | A | - |
| `lattice_nn_rg_alpha_sweep_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `lensing_adjoint_kernel_reduced_model_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `lensing_deflection_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | A | - |
| `lensing_k_sweep_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `lieb_robinson_equal_time_tensor_locality_narrow_theorem_note_2026-05-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `linear_response_derivation_note` | open_gate | ~~audited_clean~~ | open_gate | cross_family | codex-gpt-5.6 | A | - |
| `linear_response_true_kubo_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | A | - |
| `literature_backmatch_live_scan_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | D | - |
| `lsp_projective_canonical_kp_equals_p_narrow_theorem_note_2026-06-05` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.6 | A | - |
| `luders_sequential_effect_composition_pep_bridge_narrow_theorem_note_2026-06-05` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.6 | A | - |
| `main_open_cubic_validation_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `matched_2d_4d_decoherence_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `memory_decay_diagnosis_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `memory_mu2_geometry_sweep_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `mesoscopic_surrogate_localization_sweep_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | B | - |
| `mirror_2d_gravity_law_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `mirror_2d_validation_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `mirror_grown_combined_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `mirror_mutual_information_canonical_families_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `moving_source_cross_family_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `moving_source_retarded_portability_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `multipole_tidal_response_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5 | C | - |
| `naive_lattice_fermion_two_power_d_species_count_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `native_gauge_closure_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `newtonian_distance_law_confirmed` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `nonlabel_grown_basin_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `nonlabel_grown_drift_basin_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `nspt_high_order_lattice_alpha_n_coefficient_external_narrow_theorem_note_2026-05-16` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | A | - |
| `ollivier_einstein_proxy_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `ordered_lattice_quasi_persistent_relaunch_2d_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `persistent_object_blended_readout_outer_transfer_sweep_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `persistent_object_blended_readout_transfer_sweep_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `persistent_object_compact_inertial_probe_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `persistent_object_exact_lattice_park_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | B | - |
| `persistent_object_green_scout_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `persistent_object_inward_boundary_floor_diagnosis_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | judicial_review | codex-gpt-5.5 | C | - |
| `persistent_object_multistage_floor_sweep_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `persistent_object_readout_localization_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `persistent_object_top3_multistage_probe_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `persistent_object_top4_multistage_outer_transfer_sweep_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `persistent_object_top4_multistage_transfer_sweep_note_2026-04-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | judicial_review | codex-gpt-5.5 | C | - |
| `persistent_record_matched_compare_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `persistent_record_overlap_kernel_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `physical_hermitian_hamiltonian_and_sme_bridge_note_2026-04-30` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.6 | A | - |
| `pl_topology_infrastructure_textbook_import_note_2026-05-17` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `plaquette_v1_picard_fuchs_ode_note_2026-05-05` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `pmns_oriented_cycle_selection_structure_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.6 | A | - |
| `pmns_tm2_magnitudes_conditional_bounded_note_2026-05-26` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.6 | A | - |
| `pmns_tm2_residual_consequence_bounded_note_2026-05-26` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | A | - |
| `poisson_backreaction_live_threshold_packet_note_2026-05-29` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `qcd_low_energy_running_bridge_note_2026-05-01` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `qnm_control_hardening_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | A | - |
| `radial_scaling_protected_angle_narrow_theorem_note_2026-05-02` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `record_conditional_law_period_scaling_l3_to_l4_bounded_theorem_note_2026-06-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `record_conditional_law_three_point_period_series_bounded_theorem_note_2026-06-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | judicial_review | codex-gpt-5.5 | A | - |
| `relative_orientation_fusion_state_selection_pointer_frame_one_vacuous_quotient_bounded_theorem_note_2026-06-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `replay_environment_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5 | B | - |
| `retardation_discriminator_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `retarded_field_causality_probe_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `retarded_field_compact_refinement_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `s3_cap_uniqueness_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `s3_endpoint_fiber_uniform_lift_support_2026-06-27` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-current | A | - |
| `s3_taste_cube_decomposition_note` | positive_theorem | ~~audited_clean~~ | **retained** | judicial_review | codex-gpt-5.5 | A | - |
| `scalar_3plus1_temporal_ratio_note` | positive_theorem | ~~audited_clean~~ | **retained** | judicial_review | codex-gpt-5.5 | A | - |
| `scalar_kg_rerun_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `second_grown_family_complex_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | C | - |
| `second_grown_family_sign_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `self_consistency_structured_null_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `self_gravity_scaling_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | B | - |
| `seventh_family_diagonal_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `shapiro_five_family_portability_corrected_boundary_note_2026-06-06` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `sharp_record_fisher_tangent_space_narrow_theorem_note_2026-06-06` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `sign_portability_invariant_family_second_grown_derivation_theorem_note_2026-05-09` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | B | - |
| `signed_gravity_interface_kodd_pfaffian_line_bundle_label_narrow_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `site_phase_cube_shift_intertwiner_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5 | A | - |
| `sixth_family_sheared_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | B | - |
| `sixth_family_sheared_fm_transfer_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | B | - |
| `sixth_family_sheared_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | B | - |
| `source_driven_field_recovery_h025_pocket_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `source_field_static_law_classification_bounded_note_2026-07-08` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.6 | A | - |
| `source_measure_pcal_cumulant_mobius_theorem_note_2026-05-30` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `source_resolved_exact_green_scaling_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `source_resolved_generated_architecture_bridge_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `source_resolved_generated_discriminator_probe_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `source_resolved_generated_new_family_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `source_resolved_generated_support_recovery_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `source_resolved_generated_wavefield_bridge_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `source_resolved_retarded_green_corrected_packet_note_2026-05-29` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `source_resolved_retarded_green_pocket_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `source_resolved_support_localization_split_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `source_resolved_transverse_green_corrected_boundary_note_2026-05-29` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `source_resolved_wavefield_v2_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `spectral_closure_2026-04-09` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `stable_post_record_dial_location_certificate_2026-06-06` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `staggered_backreaction_capture_closure_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_backreaction_iterative_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_backreaction_live_capture_packet_note_2026-05-29` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_backreaction_nonlocal_closure_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_backreaction_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_backreaction_results_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_backreaction_shell_spectral_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_dag_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `staggered_fermion_card_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `staggered_geometry_superposition_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `staggered_graph_failure_map_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | B | - |
| `staggered_graph_gauge_closure_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | C | - |
| `staggered_graph_gauge_closure_results_2026-04-10` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | C | - |
| `staggered_graph_portability_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_graph_portability_stress_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_layered_backreaction_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `staggered_layered_gauge_engineering_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_layered_gauge_phase_diagram_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_layered_loop_threshold_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `staggered_newton_blocking_sensitivity_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `staggered_newton_reproduction_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `staggered_only_det_positivity_case_a_note_2026-05-17` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `staggered_scalar_parity_lapse_coupling_external_narrow_theorem_note_2026-05-16` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `staggered_test_mass_companion_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `structured_mirror_reconciliation_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `structureless_dag_gravity_harness_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `structureless_dag_gravity_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `symmetry_generated_paired_chokepoint_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `symmetry_spectrum_mirror_compare_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `taste_scalar_isotropy_theorem_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5 | A | - |
| `teleportation_3d_operator_consistent_end_to_end_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `teleportation_3d_resource_probe_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `teleportation_adiabatic_time_evolution_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `teleportation_causal_channel_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `teleportation_dynamical_resource_generation_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | C | - |
| `teleportation_logical_readout_audit` | open_gate | ~~audited_clean~~ | open_gate | fresh_context | codex-gpt-5 | B | - |
| `teleportation_no_signaling_audit` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5 | B | - |
| `teleportation_poisson_finite_extraction_core_bounded_note_2026-06-18` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `teleportation_poisson_resource_sweep_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `teleportation_retained_axis_operator_algebra_closure_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `three_generation_observable_m3c_burnside_narrow_theorem_note_2026-05-10` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.6 | A | - |
| `two_field_retarded_family_closure_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `two_field_retarded_probe_note_2026-04-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `unification_basin_failure_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `universal_gr_bd_congruence_invariance_bounded_note_2026-05-10` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | A | - |
| `universal_gr_cubic_ward_finite_scaling_diagnostic_bounded_theorem_note_2026-06-08` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `universal_gr_quartic_diffeo_ward_continuum_closure_bounded_theorem_note_2026-06-08` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `universal_gr_quintic_diffeo_ward_closure_bounded_theorem_note_2026-06-08` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `universal_gr_supermetric_normal_form_note` | positive_theorem | ~~audited_clean~~ | **retained** | fresh_context | codex-gpt-5.5 | A | - |
| `valley_linear_action_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `valley_linear_asymptotic_bridge_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `valley_linear_mirror_transfer_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `valley_linear_repro_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `valley_linear_robustness_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `valley_linear_wide_tail_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wave_amplification_near_horizon_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `wave_direct_dm_family_scout_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wave_direct_dm_h025_fam1_seed0_control_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `wave_direct_dm_h025_fam1_seed1_control_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wave_direct_dm_h025_fam2_seed1_control_note` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | C | - |
| `wave_direct_dm_h025_feasibility_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wave_direct_dm_h025_high_band_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wave_direct_dm_h025_low_band_retention_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wave_direct_dm_h025_two_point_synthesis_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | B | - |
| `wave_equation_gravity_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `wave_equation_self_field_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `wave_poisson_cinf_bridge_theorem_note_2026-05-28` | positive_theorem | ~~audited_clean~~ | **retained** | cross_family | codex-gpt-5.5 | A | - |
| `wave_radiation_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | judicial_review | codex-gpt-5 | C | - |
| `wave_static_boundary_sensitivity_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `wave_static_matrixfree_fixed_beam_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | fresh_context | codex-gpt-5.5 | C | - |
| `wave_static_matrixfree_moving_source_fixed_beam_boundary_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5 | C | - |
| `wave_static_matrixfree_shared_geometry_compare_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `weak_coupling_retention_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wide_lattice_h2t_distance_law_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wide_lattice_h2t_skeptic_audit_note` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | A | - |
| `wigner_mode_low_d_sublattice_theorem_note_2026-05-02` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wilson_two_body_open_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `wilson_two_body_open_refined_note_2026-04-11` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `within_sector_ess_adequacy_conclusion_survives_bounded_theorem_note_2026-06-12` | bounded_theorem | ~~audited_clean~~ | **retained_bounded** | cross_family | codex-gpt-5.5 | C | - |
| `ac_reta_hclass_hunit_readout_derivation_obligation` | open_gate | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.6 | F | - |
| `alpha_s_heavy_threshold_matching_kernel_theorem_note_2026-06-18` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.6 | A | - |
| `alpha_s_universal_two_loop_beta_kernel_theorem_note_2026-06-18` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.6 | A | - |
| `area_law_native_car_semantics_tightening_note_2026-04-25` | positive_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `area_law_primitive_car_edge_identification_theorem_note_2026-04-25` | positive_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_bounded_note_2026-05-28` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `bridge_gap_hk_cube_perron_note_2026-05-06` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | C | - |
| `dm_leptogenesis_pmns_sole_axiom_boundary_note_2026-04-16` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | weak | codex-gpt-5.6 | A | - |
| `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_full_packet_no_go_theorem_note_2026-04-20` | no_go | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `graded_constraint_menu_uniformity_contextuality_and_c3_zero_information_point_bounded_theorem_note_2026-07-11` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | fresh_context | codex-gpt-5.6 | A | - |
| `koide_dimensionless_objection_toy_conditional_algebraic_checks_narrow_theorem_note_2026-05-16` | open_gate | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `koide_first_order_section_tie_vs_outcome_label_residual_localization_bounded_theorem_note_2026-07-11` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | fresh_context | codex-gpt-5.6 | A | - |
| `koide_generation_weight_dial_shape_forced_value_unfixed_qualification_bounded_theorem_note_2026-07-11` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | fresh_context | codex-gpt-5.6 | A | - |
| `koide_kappa_bookkeeping_flow_class_fixed_point_inversion_and_lane_scoping_bounded_theorem_note_2026-07-11` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | fresh_context | codex-gpt-5.6 | A | - |
| `koide_occupancy_from_locked_record_outcomes_bounded_note_2026-07-03` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | fresh_context | codex-gpt-5.6 | A | - |
| `lorentz_violation_derived_note` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | weak | codex-gpt-5.6 | A | - |
| `post_record_character_path_channel_weight_prototype_2026-06-06` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.6 | A | - |
| `post_record_directed_certificate_examples_2026-06-06` | positive_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.6 | A | - |
| `post_record_persistent_record_production_bridge_prototype_2026-06-06` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `post_record_source_measure_trace_normalization_prototype_2026-06-06` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `quark_cp_small_correction_boundary_note_2026-06-17` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `quark_route2_double_local_projector_normalization_bridge_conditional_note_2026-06-21` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | weak | codex-current | A | - |
| `record_permanence_forces_fresh_site_double_registration_and_agreement_survival_bounded_theorem_note_2026-07-11` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | fresh_context | codex-gpt-5.6 | C | - |
| `universal_qg_uv_finite_partition_note` | positive_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | A | - |
| `yt_boundary_bc_transfer_uniqueness_narrow_theorem_note_2026-05-17` | bounded_theorem | ~~audited_conditional~~ | ~~audited_conditional~~ | cross_family | codex-gpt-5.5 | D | - |
| `abj_scale_free_native_abelian_anomaly_core_boundary_note_2026-06-18` | decoration | ~~audited_decoration~~ | `decoration_under_native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23` | cross_family | codex-gpt-5.5 | A | `native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23` |
| `beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08` | decoration | ~~audited_decoration~~ | `decoration_under_beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10` | cross_family | codex-gpt-5.5 | A | `beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10` |
| `ckm_atlas_closure_formula_algebra_narrow_theorem_note_2026-05-10` | decoration | ~~audited_decoration~~ | _retained_pending_chain_ | fresh_context | codex-gpt-5.5 | A | `ckm_atlas_axiom_closure_note` |
| `cluster_decomposition_delta_x_finite_lambda_axis_permutation_narrow_note_2026-06-02` | decoration | ~~audited_decoration~~ | `decoration_under_cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | cross_family | codex-gpt-5.5 | A | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` |
| `commensuration_general_lemma_period_parity_bounded_theorem_note_2026-06-12` | decoration | ~~audited_decoration~~ | `decoration_under_d3_truncation_commensuration_criterion_bounded_theorem_note_2026-06-12` | cross_family | codex-gpt-5.6 | A | `d3_truncation_commensuration_criterion_bounded_theorem_note_2026-06-12` |
| `ew_current_fierz_channel_decomposition_note_2026-05-01` | decoration | ~~audited_decoration~~ | `decoration_under_graph_first_su3_integration_note` | judicial_review | codex-gpt-5.5 | A | `graph_first_su3_integration_note` |
| `koide_cyclic_wilson_3_response_narrow_theorem_note_2026-05-02` | decoration | ~~audited_decoration~~ | `decoration_under_koide_dweh_cyclic_compression_note_2026-04-18` | cross_family | codex-gpt-5.5 | A | `koide_dweh_cyclic_compression_note_2026-04-18` |
| `kubo_range_of_validity_note` | decoration | ~~audited_decoration~~ | `decoration_under_linear_response_true_kubo_note` | cross_family | codex-gpt-5.5 | A | `linear_response_true_kubo_note` |
| `left_handed_charge_matching_note` | decoration | ~~audited_decoration~~ | `decoration_under_graph_first_su3_integration_note` | cross_family | codex-gpt-5.5 | A | `graph_first_su3_integration_note` |
| `lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02` | decoration | ~~audited_decoration~~ | `decoration_under_graph_first_su3_integration_note` | cross_family | codex-gpt-5.5 | A | `graph_first_su3_integration_note` |
| `lhcm_matter_assignment_block_proof_walk_lattice_independence_bounded_note_2026-05-10` | decoration | ~~audited_decoration~~ | `decoration_under_graph_first_su3_integration_note` | cross_family | codex-gpt-5.5 | A | `graph_first_su3_integration_note` |
| `lhcm_matter_assignment_from_su3_representation_note_2026-05-02` | decoration | ~~audited_decoration~~ | `decoration_under_graph_first_su3_integration_note` | cross_family | codex-gpt-5.5 | A | `graph_first_su3_integration_note` |
| `lhcm_matter_assignment_su3_block_representation_narrow_theorem_note_2026-05-17` | decoration | ~~audited_decoration~~ | `decoration_under_graph_first_su3_integration_note` | cross_family | codex-gpt-5.6 | A | `graph_first_su3_integration_note` |
| `native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23` | decoration | ~~audited_decoration~~ | `decoration_under_graph_first_su3_integration_note` | cross_family | codex-gpt-5.5 | A | `graph_first_su3_integration_note` |
| `newton_law_derived_note` | decoration | ~~audited_decoration~~ | `decoration_under_lattice_greens_function_maradudin_textbook_import_note_2026-05-18` | cross_family | codex-gpt-5.6 | A | `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` |
| `yukawa_color_projection_theorem` | decoration | ~~audited_decoration~~ | `decoration_under_graph_first_su3_integration_note` | judicial_review | codex-gpt-5.5 | A | `graph_first_su3_integration_note` |
| `source_resolved_geometry_rule_repair_note` | bounded_theorem | ~~audited_failed~~ | ~~audited_failed~~ | cross_family | codex-gpt-5.6 | C | - |
| `structured_mirror_bornsafe_scan_note` | bounded_theorem | ~~audited_failed~~ | ~~audited_failed~~ | cross_family | codex-gpt-5.6 | C | - |
| `ckm_five_sixths_bridge_support_note` | bounded_theorem | ~~audited_numerical_match~~ | ~~audited_numerical_match~~ | cross_family | codex-gpt-5.6 | G | - |
| `distance_law_definitive_note` | bounded_theorem | ~~audited_numerical_match~~ | ~~audited_numerical_match~~ | cross_family | codex-gpt-5.5 | G | - |
| `koide_gamma_orbit_exponential_value_law_candidate_note_2026-04-18` | positive_theorem | ~~audited_numerical_match~~ | ~~audited_numerical_match~~ | cross_family | codex-gpt-5.5 | G | - |
| `quark_cp_carrier_completion_note_2026-04-18` | bounded_theorem | ~~audited_numerical_match~~ | ~~audited_numerical_match~~ | cross_family | codex-gpt-5.5 | G | - |
| `source_resolved_exact_green_self_consistent_note` | bounded_theorem | ~~audited_numerical_match~~ | ~~audited_numerical_match~~ | cross_family | codex-gpt-5.5 | G | - |
| `ac_orbit_occupancy_statistical_grain_derivation_obligation` | open_gate | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.6 | E | - |
| `ai_methodology.raw.canonical_framing_paragraph` | meta | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |
| `flavor_readout_gate_equals_carrier_identification_2026-05-31` | open_gate | ~~audited_renaming~~ | ~~audited_renaming~~ | fresh_context | codex-gpt-5.5 | F | - |
| `gauge_scalar_temporal_observable_bridge_implicit_flow_theorem_note_2026-05-03` | bounded_theorem | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |
| `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19` | bounded_theorem | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |
| `lattice_3d_inverse_square_kernel_helper_note_2026-04-04` | bounded_theorem | ~~audited_renaming~~ | ~~audited_renaming~~ | fresh_context | codex-gpt-5.5 | E | - |
| `post_record_conditional_audit_evidence_ladder_2026-06-06` | meta | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |
| `post_record_flow_thermal_stable_setting_certificate_2026-06-06` | meta | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.6 | E | - |
| `post_record_production_dynamics_needed_row_map_2026-06-06` | meta | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |
| `post_record_retained_unbounded_dynamics_gate_2026-06-06` | meta | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |
| `record_axiom_audit_application_map_2026-06-06` | meta | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.6 | E | - |
| `record_markov_generator_premise_classifier_2026-06-06` | meta | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |
| `teleportation_conclusion_boundary_note` | open_gate | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |
| `thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow_theorem_note_2026-05-16` | open_gate | ~~audited_renaming~~ | ~~audited_renaming~~ | cross_family | codex-gpt-5.5 | E | - |


## Audit findings (full)

### `abj_scale_free_native_abelian_anomaly_core_boundary_note_2026-06-18`

- **Note:** [`ABJ_SCALE_FREE_NATIVE_ABELIAN_ANOMALY_CORE_BOUNDARY_NOTE_2026-06-18.md`](../../docs/ABJ_SCALE_FREE_NATIVE_ABELIAN_ANOMALY_CORE_BOUNDARY_NOTE_2026-06-18.md)
- **claim_type:** `decoration`
- **claim_scope:** Scale-free algebraic anomaly identities and the displayed SU(2)-singlet cancellation witness on the retained graph-first 6+2 left-handed abelian surface, excluding physical U(1) gauging and downstream bridge claims.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-20260621-054531-f51f6887-abj_scale_free_native_abelian_anomaly_core_boundary_note_2026-06-18-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Using the 6 and 2 multiplicities with charges a and -3a gives Tr[Y_a]=0, Tr[Y_a^3]=-48a^3, Tr[SU(3)^2Y_a]=a, Tr[SU(2)^2Y_a]=0, and substituting (4a,-2a,-6a,0) gives matching opposite-chirality anomalies.  _(class `A`)_
- **chain closes:** True — The cited parent supplies the 6/2 split and 1:-3 traceless abelian ratio; the audited note only rescales that ratio and evaluates standard finite anomaly sums. The completion branch is an explicit algebraic witness whose displayed traces match the left-handed values with the stated opposite-chirality sign.
- **rationale:** The load-bearing work is exact algebra over the single retained-grade decorated parent and standard T(F)=1/2 normalization. The runner source performs symbolic and rational arithmetic for the anomaly identities and witness, while the remaining PASS checks are source-firewall string checks rather than independent physics derivations. No external comparator, fitted normalization, or tuned scale is used. Because the chain is a class-A corollary of one upstream surface rather than a new first-principles computation, the conservative verdict is audited_decoration.
- **decoration parent:** `native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23`
- **auditor confidence:** high

### `ac_orbit_occupancy_statistical_grain_derivation_obligation`

- **Note:** [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](../../docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md)
- **claim_type:** `open_gate`
- **claim_scope:** The note records, but does not discharge, the obligation to derive the physical charged-lepton determinant-counting grain.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00346-ac_orbit_occupancy_statistic`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** A closing theorem must derive the physical matter action and its measure, then distinguish the count-once det_C/holomorphic realization from the count-twice |det_C|^2/realified realization.  _(class `E`)_
- **chain closes:** False — The source specifies the theorem required for closure but supplies neither the physical matter action and measure nor an argument selecting one determinant realization.
- **rationale:** The source honestly defines an open derivation obligation and expressly selects neither counting horn. It contains no derivation from the framework premises, cited authority, or computational certificate. With no runner source available, the classification rests on the note text alone.
- **auditor confidence:** high

### `ac_reta_hclass_hunit_readout_derivation_obligation`

- **Note:** [`AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`](../../docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md)
- **claim_type:** `open_gate`
- **claim_scope:** Whether the restricted packet derives the physical identity between fixed-locus h-density and the eta-angle readout without an additional normalization, transport, or clock-rate factor.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00344-ac_reta_hclass_hunit_readout`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** The physical charged-lepton readout is the fixed-locus density class h, identity-read in h-units as the eta angle, with no extra clock-rate, transport, or normalization factor.  _(class `F`)_
- **chain closes:** False — The note correctly presents the identity as an open obligation, but supplies no carrier/source-action bridge or normalization theorem deriving it. The physical density-to-angle identification therefore remains unclosed.
- **rationale:** Issue: the target equates an h-density class with the physical eta-angle readout, but the restricted packet contains no derivation of that map. Why this blocks: Record additivity and the approved primitives do not themselves determine the carrier, source action, or dimensionless readout normalization. Repair target: supply an independently audited carrier/source-action theorem together with either a native eta/holonomy identity or an inhomogeneous Record-facing normalization theorem. Claim boundary until fixed: the identification and all results using it remain conditional or pending-chain.
- **auditor confidence:** high

### `acphilambda_c3_resolvent_determinant_holonomy_coupling_narrow_theorem_note_2026-07-12`

- **Note:** [`ACPHILAMBDA_C3_RESOLVENT_DETERMINANT_HOLONOMY_COUPLING_NARROW_THEOREM_NOTE_2026-07-12.md`](../../docs/ACPHILAMBDA_C3_RESOLVENT_DETERMINANT_HOLONOMY_COUPLING_NARROW_THEOREM_NOTE_2026-07-12.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Finite algebra of the supplied C3 normal action: exact resolvents, the h-trace identity, scalar exponential determinant and root phases, supplied determinant-power cases, and integer determinant-character weights within the stated principal-lift domain.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt-5.6-sol-xhigh-c3-final-chain-fresh-context-20260712`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** From the exact resolvents R1+R2=I, hence B=I/3; therefore E=exp(iB/3) satisfies E^3=U1 and arg det(E)=2/9=h.  _(class `A`)_
- **chain closes:** True — Direct rational 2x2 inversion independently gives R1+R2=I, B=I/3, h=2/9, and tr(B)=3h. The retained determinant-power identity then supplies the stated single-sector, coordinate-rewrite, conjugate-pair, and realification consequences, while the remaining phase and character formulas follow exactly from scalar exponentiation.
- **rationale:** The restricted packet closes as exact finite algebra over two retained dependencies. Independent Fraction-based matrix inversion reproduced R1, R2, B, h, and tr(B); a separate complex check reproduced the determinant/root phases, conjugate cancellation, oriented rank-two Pfaffian determinant power, and character kernels. Residual risk is confined to later physical carrier, normalization, readout, occupancy, and r-selection targets that the source places outside this theorem scope.
- **auditor confidence:** high

### `acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12`

- **Note:** [`ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md`](../../docs/ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For a supplied finite complex matrix K, ordered independent Grassmann variables, and the stated Berezin orientation, the audited theorem covers the block-Pfaffian determinant identity, coordinate-congruence invariance of the single-sector Gaussian value, the conjugate-sector direct-sum modulus square, and equality with the ordinary realification determinant.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt56sol-fresh-pfaffian-20260712-rf1`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** Pf(A_K)=(-1)^(n(n-1)/2) det_C(K), while congruence of A_K and the inverse Berezin Jacobian preserve the oriented Gaussian value under invertible coordinate changes.  _(class `A`)_
- **chain closes:** True — The block-Pfaffian expansion, Berezin top-form sign, and congruence/Jacobian factors give determinant power one for the supplied single sector; direct-sum multiplicativity together with the retained realification identity gives the modulus square for the supplied conjugate pair.
- **rationale:** All load-bearing formulas close as exact finite-dimensional algebra, including signs and measure orientation, for singular as well as invertible K where applicable. Manual permutation and top-form derivations independently reproduce the runner, whose SHA-pinned cache reports 32 algebraic checks. Physical carrier and charged-lepton applications remain separate from this finite theorem domain.
- **auditor confidence:** high

### `acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04`

- **Note:** [`ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md`](../../docs/ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For every finite complex matrix K, the displayed realification has determinant |det_C(K)|^2 and the displayed ordered holomorphic Berezin Gaussian equals det_C(K); no physical carrier or occupancy-rule identification is included.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt-5.6-sol-xhigh-ac-det-fresh`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** With the displayed Berezin ordering, the holomorphic Gaussian equals det_C(K), while det_R R(K) equals det_C(K) det_C(conjugate(K)) = |det_C(K)|^2.  _(class `A`)_
- **chain closes:** True — Direct block similarity proves the realification identity, and an independent permutation-sign expansion proves the Berezin identity under the stated left-derivative ordering. The note has no dependency imports and explicitly excludes the physical charged-lepton selector bridge.
- **rationale:** The theorem is exact and self-contained. Direct multiplication gives S R(K) = diag(K, conjugate(K)) S with det(S) = (-2i)^n nonzero, so the determinant identity holds for singular as well as nonsingular K without imported physics. Independently, only permutation monomials survive in the top degree of exp(sum_ij K_ij chi_j chibar_i); the n! multiplicity cancels the factorial and reordering has sign sgn(permutation), yielding det_C(K), with an exhaustive independent sign check through n=8. Residual risk is limited to changing the explicitly stated Berezin convention; all physical charged-lepton carrier and occupancy identifications lie outside the audited scope.
- **auditor confidence:** high

### `action_crossover_note`

- **Note:** [`ACTION_CROSSOVER_NOTE.md`](../../docs/ACTION_CROSSOVER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The scoped runner reproduces the finite DAG-slice crossover table for spent-delay versus valley-linear at regularities 0.0, 0.2, 0.4, 0.6, 0.8, and 0.95, with best observed valley-minus-spent delta at regularity 0.40.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-judicial-gpt-5.5-20260511-231406-action_crossover_note-008`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** The tested DAG family shows that the better-performing action switches from spent-delay to valley-linear as graph geometry becomes more regular.  _(class `C`)_
- **chain closes:** True — The included runner source performs an actual deterministic sweep: it generates the DAGs, propagates both action formulas, counts TOWARD outcomes, and prints values matching the note. The affirmative claim is explicitly bounded to the tested DAG slice and disclaims a universal bridge theorem or closed action derivation. Under that narrowed scope, the open axiom-level interpretation is not load-bearing, so the finite computational replay closes.
- **rationale:** The included runner source performs an actual deterministic sweep: it generates the DAGs, propagates both action formulas, counts TOWARD outcomes, and prints values matching the note. The affirmative claim is explicitly bounded to the tested DAG slice and disclaims a universal bridge theorem or closed action derivation. Under that narrowed scope, the open axiom-level interpretation is not load-bearing, so the finite computational replay closes.
- **auditor confidence:** high

### `action_geometry_bridge_note`

- **Note:** [`ACTION_GEOMETRY_BRIDGE_NOTE.md`](../../docs/ACTION_GEOMETRY_BRIDGE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite replay of the supplied Python DAG probe showing sign-changing valley-linear versus spent-delay toward-rate differences across the frozen regularity grid.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e131c-5ad1-7bb2-ac9d-7c58c1fb334f`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The action preference does shift with regularity on the tested family, is not cleanly monotonic on this slice, and the safest label is mixed bridge.  _(class `C`)_
- **chain closes:** True — The supplied runner source actually generates the DAGs, propagates both actions, and computes the reported table rather than printing fixed constants. The source note's safe interpretation is limited to the tested scripted slice and matches the completed stdout.
- **rationale:** Clean for the bounded computational claim only: the note freezes the parameters, the runner computes the finite replay, and the stdout supports a mixed, non-monotonic shift in the scripted readout. The result does not rely on unlisted dependencies or external comparators, and the note explicitly does not claim a universal action unification or continuum theorem. Residual risk is scope creep if later citations treat this as a physical bridge beyond the frozen generated-DAG experiment.
- **auditor confidence:** medium

### `action_power_note`

- **Note:** [`ACTION_POWER_NOTE.md`](../../docs/ACTION_POWER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fixed finite-output audit of scripts/action_power_canonical_harness.py for the action-power p=0.5 versus spent-delay 2D/3D NN harness values reported in docs/ACTION_POWER_NOTE.md.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-lambert`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The action-power branch is a bounded axiom-fork whose fixed canonical harness gives the reported 2D comparison, 3D close-slit barrier card, and 3D no-barrier distance/mass companion, while not closing same-harness 3D attraction.  _(class `C`)_
- **chain closes:** True — The current self-contained runner completed and reproduced the note's canonical harness numbers, including the 3D power Born=2.63e-16, k=0=0, MI=0.6712, d_TV=0.8116, gravity=-0.000076, distance exponent=-1.84, and F proportional to M=1.00. The clean verdict is bounded to this finite canonical harness output and does not audit separate gravity-sign sweep claims beyond the named runner.
- **rationale:** Within the scoped finite harness, the runner computes the reported values from the stated action fork and fixed lattice setup rather than importing an external comparator or renaming a target observable. The note also states the relevant limits: no inherited spent-delay claims, no continuum or robustness closure, and no same-harness 3D Newtonian attraction closure.
- **auditor confidence:** medium

### `action_power_scaling_sweep_note`

- **Note:** [`ACTION_POWER_SCALING_SWEEP_NOTE.md`](../../docs/ACTION_POWER_SCALING_SWEEP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded replay on the fixed 3D ordered dense lattice with h=0.5, W=10, L=12, kernel 1/L^2 with h^2 measure, field s/r, and S=L(1-f^p), showing F∝M=p for p in {0.5, 0.75, 1.0, 1.5, 2.0} and monotonic tail steepening without promoting a universal tail law.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519T214237Z-7e8580f6-action_power_scaling_sweep_note-panel-majority`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** On this fixed family, the mass-scaling law is clean: F∝M = p across the tested sweep.  _(class `C`)_
- **chain closes:** True — Five-judge panel majority ratified the first audit tuple (audited_clean, bounded_theorem, class C). Vote breakdown: J1: first / audited_clean / bounded_theorem / class C; J2: first / audited_clean / bounded_theorem / class C; J3: first / audited_clean / bounded_theorem / class C; J4: first / audited_clean / bounded_theorem / class C; J5: first / audited_clean / bounded_theorem / class C. Majority rationale: J1: The source note makes only a bounded fixed-family finite replay claim, and the cached runner output exactly reproduces the frozen table: Born is machine-clean, all rows are 7/7 TOWARD, F~M equals each tested p, and the note explicitly withholds universal tail-law and p=1 derivation claims. Within that scoped claim there is no unresolved external dependency or promoted physical bridge requiring a conditional verdict. | J2: The restricted note claims only a fixed-family finite replay: for the specified lattice, powers, kernel, field, and action family, the cached runner exactly reproduces the frozen table with F~M equal to each tested p, Born machine-clean, and no promoted universal tail law. That closes as a bounded computational theorem/class-C replay, not a conditional claim. | J3: The source note makes only a fixed-family finite replay claim: for the stated lattice/action family and tested p values, the cached runner output reproduces Born, 7/7 TOWARD, F~M=p, and monotonic tail steepening while explicitly withholding any universal tail theorem. No unaudited dependency, open gate, or unratified bridge is needed for that bounded computational claim. | J4: The source note makes only a bounded fixed-family replay claim, and the cached runner output exactly reproduces the frozen table: Born values, 7/7 TOWARD rows, F~M=p for all five tested powers, and tail steepening while explicitly declining any universal tail law. No unclosed external comparator or promoted exact tail theorem is load-bearing. | J5: The restricted claim is a finite fixed-family replay, and the cached runner exits cleanly while reproducing the note's load-bearing table: Born stays machine-clean, all rows are 7/7 TOWARD, and F~M equals each tested p. The note explicitly limits the result to this fixed family and does not promote a universal tail law or derivation of p=1, so the chain closes for the bounded claim.
- **rationale:** Five-judge panel majority ratified the first audit tuple (audited_clean, bounded_theorem, class C). Vote breakdown: J1: first / audited_clean / bounded_theorem / class C; J2: first / audited_clean / bounded_theorem / class C; J3: first / audited_clean / bounded_theorem / class C; J4: first / audited_clean / bounded_theorem / class C; J5: first / audited_clean / bounded_theorem / class C. Majority rationale: J1: The source note makes only a bounded fixed-family finite replay claim, and the cached runner output exactly reproduces the frozen table: Born is machine-clean, all rows are 7/7 TOWARD, F~M equals each tested p, and the note explicitly withholds universal tail-law and p=1 derivation claims. Within that scoped claim there is no unresolved external dependency or promoted physical bridge requiring a conditional verdict. | J2: The restricted note claims only a fixed-family finite replay: for the specified lattice, powers, kernel, field, and action family, the cached runner exactly reproduces the frozen table with F~M equal to each tested p, Born machine-clean, and no promoted universal tail law. That closes as a bounded computational theorem/class-C replay, not a conditional claim. | J3: The source note makes only a fixed-family finite replay claim: for the stated lattice/action family and tested p values, the cached runner output reproduces Born, 7/7 TOWARD, F~M=p, and monotonic tail steepening while explicitly withholding any universal tail theorem. No unaudited dependency, open gate, or unratified bridge is needed for that bounded computational claim. | J4: The source note makes only a bounded fixed-family replay claim, and the cached runner output exactly reproduces the frozen table: Born values, 7/7 TOWARD rows, F~M=p for all five tested powers, and tail steepening while explicitly declining any universal tail law. No unclosed external comparator or promoted exact tail theorem is load-bearing. | J5: The restricted claim is a finite fixed-family replay, and the cached runner exits cleanly while reproducing the note's load-bearing table: Born stays machine-clean, all rows are 7/7 TOWARD, and F~M equals each tested p. The note explicitly limits the result to this fixed family and does not promote a universal tail law or derivation of p=1, so the chain closes for the bounded claim.
- **auditor confidence:** judicial_panel_majority

### `action_uniqueness_audit_2026-04-11`

- **Note:** [`ACTION_UNIQUENESS_AUDIT_2026-04-11.md`](../../docs/ACTION_UNIQUENESS_AUDIT_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** On the specified 3D ordered nearest-neighbor lattice setup (h=0.5, W=8, L=12, f=s/r) and its weak-field continuum power-family model, weak-field-linear valley actions share Newtonian-regime F proportional to M behavior; no architecture-independent uniqueness is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T015154Z-1f0c3329-00366-action_uniqueness_audit_2026`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** On the tested 3D ordered nearest-neighbor lattice family, weak-field-linear phase-valley actions produce the same leading Newtonian-regime response, including deflection proportional to source mass.  _(class `C`)_
- **chain closes:** True — The runner genuinely propagates amplitudes for several independently implemented weak-field-linear actions and computes their mass-response exponents, then independently evaluates the continuum power-family integrals. These calculations close the stated bounded family law but not the runner's broader uniqueness rhetoric.
- **rationale:** The source note confines its operative conclusion to the tested ordered-lattice family and expressly rejects universal action uniqueness. The runner computes, rather than hard-codes, the lattice centroid responses and continuum scaling, and the alternative weak-field-linear actions agree at leading order as claimed. The evidence establishes first-order equivalence within the stated model family while leaving higher-order action freedom and architecture dependence outside scope.
- **auditor confidence:** high

### `affine_imaginary_slot_invariance_narrow_theorem_note_2026-05-02`

- **Note:** [`AFFINE_IMAGINARY_SLOT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/AFFINE_IMAGINARY_SLOT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The audited claim is the standalone Herm(3) linear-algebra statement that the three explicit real symmetric generators are linearly independent, give Tr(H)=Tr(H_base)+m, and do not change any imaginary matrix entry under the stated real affine parameters.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-affine_imaginary_slot_in-020`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Since T_m, T_delta, and T_q are all real, their imaginary parts vanish entrywise, so Im(H(m, delta, q_+)_{ij}) = Im(H_base_{ij}) for all entries.  _(class `A`)_
- **chain closes:** True — The conclusions follow directly from the explicitly given matrices and ordinary matrix algebra. No cited upstream authority, physical identification, fitted value, or external comparator is needed.
- **rationale:** The load-bearing step is a genuine algebraic identity over the explicit real matrices supplied in the note. The runner source performs symbolic/exact checks of symmetry, rank, traces, trace dependence, and entrywise imaginary-part invariance rather than merely printing constants. The framework instance is only a specialization of the same algebraic closure and does not import a contested external premise.
- **auditor confidence:** high

### `ai_methodology.raw.canonical_framing_paragraph`

- **Note:** [`ai_methodology/raw/canonical_framing_paragraph.md`](../../docs/ai_methodology/raw/canonical_framing_paragraph.md)
- **claim_type:** `meta`
- **claim_scope:** Audited only the source note's registration of a canonical paper-facing AI-disclosure/accountability paragraph and its stated methodology-only boundary.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-ai_methodology.raw.canonical_framing_paragraph-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** This paragraph is the canonical version and may be cited for manuscript disclosure language and methodology framing, but not as a retained physics theorem, runner-backed derivation, or audit result.  _(class `E`)_
- **chain closes:** True — Within the declared meta scope, the note closes by adoption/definition: it designates the quoted paragraph as canonical disclosure language and explicitly excludes physics-theorem use. No physics derivation or runner-backed scientific claim is established by this packet.
- **rationale:** The load-bearing act is a definition/adoption of canonical disclosure text, not a derivation from framework premises. The source note itself correctly scopes the artifact as methodology/canonical-text registration only and forbids citation as a retained physics theorem or audit result. Thus the meta registration closes, but any positive-theorem interpretation would be only a definition substitution rather than a scientific derivation.
- **auditor confidence:** high

### `alpha_s_heavy_threshold_matching_kernel_theorem_note_2026-06-18`

- **Note:** [`ALPHA_S_HEAVY_THRESHOLD_MATCHING_KERNEL_THEOREM_NOTE_2026-06-18.md`](../../docs/ALPHA_S_HEAVY_THRESHOLD_MATCHING_KERNEL_THEOREM_NOTE_2026-06-18.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The one-loop SU(3) Lambda-parameter transition and finite multi-threshold inverse-coupling composition, conditional on coupling continuity at each abstract one-flavor threshold.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T031137Z-0d389f16-00045-alpha_s_heavy_threshold_matc`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Imposing x_hi(M) = x_lo(M) on the one-loop solutions yields Lambda_lo = M * (Lambda_hi / M) ** [b0(n_f_hi) / b0(n_f_lo)].  _(class `A`)_
- **chain closes:** False — The runner correctly verifies the Lambda transition and piecewise composition after copying x across each threshold. The unrestricted chain does not close because the LO no-jump matching condition is neither derived nor supplied by a retained or explicitly accepted-premise authority.
- **rationale:** Issue: The runner sets x_below equal to x_above at every threshold, so it assumes rather than derives the load-bearing LO no-jump matching condition. Why this blocks: The Lambda transition and piecewise map are valid algebraic consequences, but the restricted packet provides no retained or accepted-premise authority for physical threshold continuity. Repair target: Supply and cite a retained derivation or explicitly approved-premise registration of alpha_s^hi(M) = alpha_s^lo(M). Claim boundary until fixed: Only the conditional one-loop algebraic kernel, not an unconditional heavy-threshold matching theorem or downstream alpha_s(M_Z), is supported.
- **auditor confidence:** high

### `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10`

- **Note:** [`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The abstract R^+ algebraic identities T1-T6 relating alpha_bare, u_0, alpha_LM, alpha_s(v), and the optional positive substitution u_0=P^(1/4), with no physical plaquette, normalization, gauge-group, running, or numerical target import.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260611-131132-b94d3acc1d-alpha_s_tadpole_improvement_`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** From the definitions alpha_LM := alpha_bare/u_0 and alpha_s(v) := alpha_bare/u_0^2, the stated identities follow by direct algebra over positive reals.  _(class `A`)_
- **chain closes:** True — The conclusions are algebraic consequences of the two displayed definitions with positivity supplying division, square-root uniqueness, and logarithm domains. No cited authority or hidden numerical input is needed for the audited abstract scope.
- **rationale:** Independent symbolic checking confirms T1-T6: the vertex-power identities, geometric-mean/log form, constant-ratio chain, u_0=1 boundary, unique positive inverse, and P^(1/4) substitution all reduce to zero residuals under the stated positivity assumptions. The runner source performs genuine symbolic and numerical algebra checks rather than hard-coding a contested physical value, and its documentary scope guards do not enter the load-bearing proof. The verdict is clean only for the narrow abstract algebraic theorem, not for any parent alpha_s(M_Z), plaquette, Wilson-action, or bare-normalization claim.
- **auditor confidence:** high

### `alpha_s_universal_two_loop_beta_kernel_theorem_note_2026-06-18`

- **Note:** [`ALPHA_S_UNIVERSAL_TWO_LOOP_BETA_KERNEL_THEOREM_NOTE_2026-06-18.md`](../../docs/ALPHA_S_UNIVERSAL_TWO_LOOP_BETA_KERNEL_THEOREM_NOTE_2026-06-18.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Exact SU(3) substitution, active-flavor evaluation, and coupling-convention normalization conditional on the supplied universal beta_0 and beta_1 coefficient templates.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T031137Z-0d389f16-00017-alpha_s_universal_two_loop_b`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Conditional on the supplied beta_0 and beta_1 templates, substituting C_F = 4/3, C_A = 3, and T_F = 1/2 gives beta_0(n_f) = 11 - 2n_f/3 and beta_1(n_f) = 102 - 38n_f/3, with the stated coupling-convention conversions.  _(class `A`)_
- **chain closes:** False — The algebraic substitution and convention conversion close exactly, but the load-bearing beta_0 and beta_1 templates are imported without a cited retained derivation or an explicitly flagged accepted premise.
- **rationale:** The runner genuinely performs exact rational substitutions, active-flavor evaluations, structural checks, and coupling-convention conversions rather than merely printing the expected values. Those calculations support the note's bounded conditional conclusions. However, the universal beta_0 and beta_1 coefficient templates are the indispensable input and are neither derived from an axiom nor supplied through a retained or explicitly accepted-premise authority in this packet.
- **auditor confidence:** high

### `alt_connectivity_family_basin_note`

- **Note:** [`ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md`](../../docs/ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite bounded sweep showing that the parity-rotated sector-transition alternative connectivity family has 32/45 passing rows over the stated 9 drift values and 5 seeds on the no-restore grown slice, with no claim of seed-wide, geometry-generic, or unique-family closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-second-alt_connectivity_family_basin_note-20260505`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Sweep summary: tested drifts 0.0 through 0.5 over seeds 0 through 4, with passing rows 32/45 and clean zero, neutral, sign-orientation, and near-linear charge-scaling controls on passing rows.  _(class `C`)_
- **chain closes:** True — The dependency is retained_bounded and supplies the alternative family/sign setup; the basin runner extends it over the explicitly listed finite drift/seed grid and computes the row outcomes. The source note's bounded, non-universal safe read follows from the cached runner output.
- **rationale:** The load-bearing result is a finite deterministic sweep, not a generic physics bridge, and the note correctly limits the claim to a bounded basin rather than universal closure. The cached runner completes successfully and computes the 32/45 row count from the grown geometries, alternative connectivity construction, propagated source fields, and explicit ok gate; it does not use an external comparator or import the 32/45 result as an input. Residual risk is that the runner's final mean-exponent summary appears to index the neutral column rather than the exponent column, but the row-level exponents and ok predicate still support the source note's near-linear scaling statement.
- **auditor confidence:** high

### `alt_connectivity_family_failure_note`

- **Note:** [`ALT_CONNECTIVITY_FAMILY_FAILURE_NOTE.md`](../../docs/ALT_CONNECTIVITY_FAMILY_FAILURE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Diagnosis that the 13 failing rows in the tested alternative connectivity basin fail by sign-orientation reversal, not by zero leakage, neutral leakage, or weak-scaling failure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-alt_connectivity_family_-047`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The misses are a pure sign-orientation boundary: zero-control leakage 0, neutral-cancellation leakage 0, sign-orientation failures 13, scaling failures 0.  _(class `B`)_
- **chain closes:** True — The cited authorities establish a retained_bounded alternative family and basin, and the provided runner sweeps the same drift/seed grid, calls the basin measurement routine, and classifies failed rows by zero, neutral, orientation, and scaling criteria. Within the restricted packet, the diagnostic conclusion follows for the tested basin rows.
- **rationale:** The load-bearing step is a bounded diagnostic check over a retained_bounded upstream basin, not a universal family theorem. The runner does not merely print constants: it iterates over imported DRIFTS and SEEDS, calls _measure, skips passing rows, and counts concrete failure reasons from returned zero/plus/minus/neutral/exponent values. Because the cited authorities are retained_bounded and the conclusion is scoped to the tested failing rows, no open dependency or external comparator is needed for this diagnostic claim.
- **auditor confidence:** medium

### `alt_connectivity_family_fm_transfer_note`

- **Note:** [`ALT_CONNECTIVITY_FAMILY_FM_TRANSFER_NOTE.md`](../../docs/ALT_CONNECTIVITY_FAMILY_FM_TRANSFER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Weak-field mass-scaling F~M was audited for the parity-rotated sector-transition alternative connectivity family on the no-restore grown slice over drifts 0.0, 0.1, 0.2, 0.3, 0.5 and seeds 0, 1, 2.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-alt_connectivity_family_-048`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner reports that all 15 drift/seed rows pass the weak-field F~M test with mean F~M = 0.999994, so the alternative family preserves weak-field linearity on the tested no-restore grown slice.  _(class `C`)_
- **chain closes:** True — The cited authorities are retained_bounded and the supplied runner source computes the F~M exponent from generated geometries, propagated fields, and centroid shifts rather than printing constants or importing the contested result. The conclusion closes only for the finite tested drift/seed slice, not as a family-wide theorem.
- **rationale:** The load-bearing computation is a direct runner calculation across the stated finite sweep, with all 15 rows passing the stated tolerance. The runner source constructs the alternative connectivity, propagates fields at two weak source strengths, and computes the log-slope F~M value, so stdout is supported by actual computation. The upstream sign and basin authorities are retained_bounded, and the audited claim is limited to the tested no-restore grown slice.
- **auditor confidence:** high

### `alt_connectivity_family_sign_note`

- **Note:** [`ALT_CONNECTIVITY_FAMILY_SIGN_NOTE.md`](../../docs/ALT_CONNECTIVITY_FAMILY_SIGN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded numerical-computational audit of the parity-rotated sector-transition connectivity family on the no-restore grown slice for drifts 0.0, 0.1, 0.2, 0.3, 0.5 and seeds 0, 1, 2.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260504-232946-c1a20bdf-alt_connectivity_family_-006`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The runner's 15-row sweep reports 10/15 passing rows with exact zero/neutral controls, correct sign orientation on retained rows, and near-linear charge response across all tested drift values.  _(class `C`)_
- **chain closes:** True — The included runner source constructs the alternative connectivity rule, propagates fields through the generated slice, and computes the reported zero, neutral, sign, and scaling checks rather than printing constants. The note's conclusion is explicitly bounded to the tested rows and rejects family-wide closure.
- **rationale:** The load-bearing step is a direct bounded computational sweep, and the runner source performs a nontrivial calculation of geometry, connectivity, source fields, propagation, centroids, and pass/fail gates. The note's quantitative claims match the cached stdout: 10/15 rows pass, passing rows cover all listed drifts, and the mean exponent among passes is 1.000035. The safe read does not overclaim all seeds, generic geometry closure, or family-wide validity.
- **auditor confidence:** medium

### `alternative_coupled_field_probe_note`

- **Note:** [`ALTERNATIVE_COUPLED_FIELD_PROBE_NOTE.md`](../../docs/ALTERNATIVE_COUPLED_FIELD_PROBE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the bounded numerical claim that the specified edge-carried transport rule on the stated exact 3D lattice recovers free propagation at zero source and preserves positive weak-field deflection with near-linear source-strength scaling for s=0.001 to 0.008.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-141901-30b1a9aa-alternative_coupled_fiel-054`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner computes that the edge-carried forward-transport field has zero-source dynamic shift +0.000000e+00, positive edge-carried deflection in all four source-strength rows, and fitted edge-carried F~M exponent 0.98 on the exact 3D lattice.  _(class `C`)_
- **chain closes:** True — Within the stated bounded scope, the included runner and helper source instantiate the lattice, build the edge-carried field, propagate amplitudes, and compute detector shifts rather than printing hard-coded expected values. The arbitrary transport parameters and weak-field calibration limit the scope, but they are explicit premises of the audited family rather than hidden downstream dependencies.
- **rationale:** The primary runner source and helper source are present, and the load-bearing readout is computed from the provided lattice propagation code. The zero-source case follows because a zero source builds an all-zero edge field, and the sign/scaling rows are computed by propagating with constructed field layers over the stated sweep. No cited authority is missing or non-retained, and no external comparator is used. The verdict is clean only for the explicitly parameterized bounded family, not for a general coupled-field theory.
- **auditor confidence:** high

### `anderson_phase_mu2_0001_note_2026-04-11`

- **Note:** [`ANDERSON_PHASE_MU2_0001_NOTE_2026-04-11.md`](../../docs/ANDERSON_PHASE_MU2_0001_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-bottomup-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** At mu2 = 0.001, the unscreened corrected periodic phase-map replay strengthens the boundary-law separation and changes the interpretation qualitatively.  _(class `C`)_
- **chain closes:** True — Yes. The claim is a bounded companion replay on a fixed corrected harness, and the registered runner completed successfully for that finite phase-map check.
- **rationale:** The note makes a bounded finite-harness claim, not a universal theorem. The current runner completed successfully and supports the replay surface classified as {'A': 0, 'B': 0, 'C': 6, 'D': 0, 'total_pass': 6}. Residual risk is generalization outside the stated mu2 and periodic-torus setup.
- **auditor confidence:** high

### `architecture_portability_live_reaudit_bridge_note_2026-06-18`

- **Note:** [`ARCHITECTURE_PORTABILITY_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md`](../../docs/ARCHITECTURE_PORTABILITY_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Source-side bridge establishing that the old April 11 architecture-portability packet remains failed historical evidence while the live sweep is an executable bounded finite source-mass and attraction portability companion over the four configured rows, with Born I_3 only for ordered and staggered rows.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-architecture_portability_live_reaudit_bridge_note_2026-06-18-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The live packet repairs the archived audit blocker at the source-artifact level by supplying a bounded configured sweep, cached runner output, per-architecture measurements, and explicit finite-scope boundaries.  _(class `B`)_
- **chain closes:** True — The cited Architecture Portability Sweep authority is retained_bounded and states exactly the finite scope, measurements, gates, and exclusions used by the bridge. The bridge runner verifies the archive boundary, live-note boundary, cache status, runner SHA, and scoped cache results rather than asserting stronger Newton, Wilson Born-rule, or effective-status claims.
- **rationale:** The claim is clean only as a source-side bridge: it does not independently rederive the architecture-portability physics, and it does not claim full Newton closure or retained effective status. The load-bearing work is cross-artifact verification against a retained_bounded cited sweep plus SHA-pinned cache output, so class B is the right classification rather than first-principles class C. Within that narrowed scope, the cache, boundary language, and exclusions match the source note and no open dependency is imported.
- **auditor confidence:** high

### `architecture_portability_sweep_note`

- **Note:** [`ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md`](../../docs/ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite runner-backed portability sweep for source-mass scaling and attraction sign on the four specified small architectures, with Born-rule I_3 checked only on ordered and staggered 3D lattices; not a Newton-law or distance-law closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-architecture_portability_sweep_note-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner varies source amplitude across five values, fits |displacement| versus source mass, and reports beta within 10%, attraction on all four architectures, and I_3 < 1e-6 where measured.  _(class `C`)_
- **chain closes:** True — Within the stated finite protocol, the runner constructs the lattices, Poisson solves, Hamiltonians, evolutions, free controls, fits, and Sorkin I_3 checks rather than printing hard-coded target values. The conclusion closes only for the bounded sweep described in the note.
- **rationale:** The runner source genuinely computes the load-bearing numerical checks from the specified finite lattice systems and its cached stdout matches the source note to rounding. The note's own boundary correctly excludes standalone Newton closure, Wilson Born-rule closure, random-geometric distance-law comparability, and large-volume/asymptotic claims. Residual risk is confined to the stated modeling choices and finite-size protocol, not to a missing computation inside the audited scope.
- **auditor confidence:** medium

### `area_law_native_car_semantics_tightening_note_2026-04-25`

- **Note:** [`AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md`](../../docs/AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited the conditional algebraic equivalence between an irreducible local Cl_4(C)/Majorana edge algebra on the rank-four primitive block and the two-mode complex CAR carrier, plus the claim that rank four alone underdetermines the carrier semantics.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260505-225305-c0ea7096-area_law_native_car_sema-019`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Assume the rank-four active block is generated by four Hermitian odd Clifford-Majorana operators obeying {gamma_i,gamma_j}=2 delta_ij I_K; then c_1=(gamma_1+i gamma_2)/2 and c_2=(gamma_3+i gamma_4)/2 obey the two-mode CAR.  _(class `A`)_
- **chain closes:** False — The algebraic implication from an assumed irreducible Clifford-Majorana edge response to two-mode CAR closes. The broader native Target 2 carrier derivation does not close because the restricted packet explicitly leaves the substrate-to-P_A/coframe-response forcing step open.
- **rationale:** The runner performs genuine finite-dimensional algebra checks of CAR, Majorana/Clifford relations, full M_4(C) generation, parity, and rank-alone underdetermination. However, the load-bearing Clifford-Majorana response is an explicit premise rather than a consequence of retained substrate content, and the cited upstream authority is marked unaudited/audited_renaming with the same missing substrate-to-packet forcing step. Therefore the note is audit-clean only as a conditional algebraic tightening, not as an unconditional positive theorem deriving native CAR horizon physics.
- **open / conditional deps cited:**
  - `PLANCK_PRIMITIVE_CLIFFORD_MAJORANA_EDGE_DERIVATION_THEOREM_NOTE_2026-04-30.md`
- **auditor confidence:** high

### `area_law_primitive_car_edge_identification_theorem_note_2026-04-25`

- **Note:** [`AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md`](../../docs/AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited the conditional primitive-CAR carrier claim: assuming a rank-four minimal complex CAR edge block with one normal channel and the self-dual tangent-Laplacian response, the Widom coefficient equals the primitive trace, c_Widom=c_cell=1/4.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260505-225305-c0ea7096-area_law_primitive_car_e-020`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The self-dual tangent Laplacian sheet has Haar measure exactly 1/2, so the required normal mode plus the tangent-gated mode gives <N_x>=2+2*(1/2)=3 and c_Widom=3/12=1/4.  _(class `A`)_
- **chain closes:** False — The algebraic coefficient computation closes inside the stated primitive-CAR axioms. The full chain does not close from the restricted cited inputs because the primitive Clifford/CAR coframe response and substrate-to-P_A forcing remain explicit open premises.
- **rationale:** Issue: the runner verifies exact algebra and finite-grid half-zone checks after the primitive-CAR carrier, normal channel, and tangent-response selector are already assumed. Why this blocks: the cited authorities are unaudited or explicitly conditional, and the 2026-04-30 authority says the substrate action has not been shown to preserve P_A and induce the Cl_4/CAR carrier. Repair target: prove or retain a substrate-to-P_A/first-order boundary theorem that forces the primitive Clifford/CAR coframe response without adding it as a carrier premise. Claim boundary until fixed: the 1/4 result is valid as a conditional theorem inside the primitive-CAR edge axioms.
- **open / conditional deps cited:**
  - `AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md`
  - `PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md`
  - `PLANCK_PRIMITIVE_CLIFFORD_MAJORANA_EDGE_DERIVATION_THEOREM_NOTE_2026-04-30.md`
- **auditor confidence:** high

### `asymmetry_persistence_born_note`

- **Note:** [`ASYMMETRY_PERSISTENCE_BORN_NOTE.md`](../../docs/ASYMMETRY_PERSISTENCE_BORN_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Narrow dense Born calibration for generated asymmetry-persistence graphs at N=100, npl=60, thresholds 0.10 and 0.20, 2 seeds and 4 realizations, including linear, persistence, persistence+LN, and persistence+LN+collapse columns.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-audit-ready-20260529-asymmetry_persistence_bo`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The corrected Sorkin |I3|/P magnitudes in the table are reproducible from the registered runner at the narrow N=100, npl=60, thresholds=[0.1,0.2], 2-seed, 4-realization default configuration, and every column is far below 1e-10.  _(class `C`)_
- **chain closes:** True — The restricted packet includes the primary runner, its cache, and all named helper sources; the runner builds the graphs, propagates amplitudes, computes the corrected Sorkin I3 with -P(empty), and reproduces the note table without hard-coded expected values. The conclusion is limited to the stated narrow density-limited probe and does not assert broader-N or asymptotic closure.
- **rationale:** The load-bearing result is a direct deterministic computation from the included graph-generation, propagation, collapse, and Sorkin-metric code, not a definition, renaming, external comparator, or numerical fit to imported constants. The cached stdout matches the source-note table and records status ok within the audit timeout. The cited authorities are retained_bounded and the note explicitly confines itself to the narrow N=100 calibration rather than relying on the open broader sweep.
- **auditor confidence:** high

### `asymmetry_persistence_collapse_note`

- **Note:** [`ASYMMETRY_PERSISTENCE_COLLAPSE_NOTE.md`](../../docs/ASYMMETRY_PERSISTENCE_COLLAPSE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Narrow qualitative observation from the completed N=80 configured runner output only: asymmetry-persistence lowers the unitary pur_min readout at the nonzero thresholds, while the stochastic-collapse readout does not show a uniform lowering relative to the unpruned baseline; N=100 rows and any collapse-pocket claim are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At N=80 and thresholds 0.10/0.20, pers_pmin is 0.981 versus base_pmin 0.998 and pers_LN is 0.889/0.881 versus base_LN 0.954, while pers_col is 0.286/0.281 versus base_col 0.264 and persCol_LN is 0.235/0.236 versus col_LN 0.235.  _(class `D`)_
- **chain closes:** True — The current source scope is only the qualitative N=80 runner-output comparison; the cached stdout contains the required N=80 rows, and the helper sources show the configured graph generation, propagation, collapse, and purity readouts used for that comparison.
- **rationale:** Within the narrowed scope, the completed N=80 stdout supports both qualitative statements: nonzero asymmetry-persistence thresholds lower the unitary pur_min readout, including the layernorm variant, and the stochastic-collapse columns do not show a generic lowering relative to baseline. The verdict does not use the runner's N=100 rows, does not assert a quantitative threshold row, does not assert a collapse pocket, and does not promote the helper model to a physical mechanism beyond this configured bounded simulation surface.
- **auditor confidence:** medium

### `asymmetry_persistence_joint_card_note`

- **Note:** [`ASYMMETRY_PERSISTENCE_JOINT_CARD_NOTE.md`](../../docs/ASYMMETRY_PERSISTENCE_JOINT_CARD_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Dense 3D generated same-graph joint card for N=80 with npl=50 and N=100 with npl=60, 8 matched seeds, thresholds 0.00/0.10/0.20, measuring pur_cl, pur_min, gravity delta, and corrected Born |I3|/P under linear and layer-normalized propagation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-132018-20260517T132018Z-063678e3-asymmetry_persistence_jo-targeted`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The binding evidence is exactly the N=80 and N=100 joint card rows from the cached runner log, showing same-graph pur_cl, pur_min, gravity, and corrected Born |I3|/P for matched-seed dense 3D generated graphs.  _(class `C`)_
- **chain closes:** True — The cached runner output matches the note's retained N=80/100 tables and the provided runner source performs graph generation, propagation, purity, gravity, and corrected Sorkin/Born calculations rather than printing fixed constants. The note explicitly demotes the N=120 probe and central-band comparison outside the binding audited scope.
- **rationale:** Within the narrowed N=80/100 scope, the claim is supported by a completed cached runner with matching parameters, exit_code 0, and table values matching the note. The runner source computes the listed metrics on generated same-graph instances and includes the corrected -P(empty) Born term, so the load-bearing step is a bounded first-principles compute rather than a definition, renaming, or tuned external comparison. The gravity language is appropriately limited: the retained result is primarily a decoherence and Born-clean coexistence claim, not a robust gravity win across the broader lane.
- **auditor confidence:** medium

### `asymmetry_persistence_mass_scaling_note`

- **Note:** [`ASYMMETRY_PERSISTENCE_MASS_SCALING_NOTE.md`](../../docs/ASYMMETRY_PERSISTENCE_MASS_SCALING_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Finite N=100, npl=60, eight-seed generated 3D graph sweep showing positive sublinear gravity-delta mass fits for M={2,3,5,8}, with persistence improving the mass-response window relative to the baseline generated lane.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-210412-0eef0b89-asymmetry_persistence_ma-005`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Generated persistence turns the flat baseline linear response into a clearer positive sublinear mass window, with the cleanest retained row at threshold 0.10 in the layernorm lane.  _(class `C`)_
- **chain closes:** True — The SHA-pinned cached run completes and reproduces the note's fit coefficients, exponents, and R^2 values. The primary runner and bundled helpers compute these values from seeded graph generation, propagation, gravity-delta measurement, and log-log fitting without importing or hard-coding the contested fit results.
- **rationale:** The runner constructs the generated 3D DAGs, applies the asymmetry-persistence threshold, varies fixed-prefix mass nodes, computes detector y-shift deltas under linear and layernorm propagation, and fits the declared mass window. The helper sources are present and expose the load-bearing graph, field, propagation, and fitting machinery; no helper hard-codes the claimed numerical outcomes. The clean result is limited to the finite generated-graph protocol and does not establish exact F proportional M or a Newtonian mass law.
- **auditor confidence:** high

### `asymmetry_persistence_mass_window_note`

- **Note:** [`ASYMMETRY_PERSISTENCE_MASS_WINDOW_NOTE.md`](../../docs/ASYMMETRY_PERSISTENCE_MASS_WINDOW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded N=100 dense generated-family mass-response window for thresholds 0.10 and 0.20 under the layer-normalized propagator, with M in {1,2,3,5,8,12} and fits over {2,3,5,8}.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-152136-02e6f5c5-asymmetry_persistence_ma-023`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The threshold-0.10 and threshold-0.20 LN power-law fits and R^2 values are reproducible from the cited runner cache as direct stdout of scripts/asymmetry_persistence_mass_scaling.py, supporting a bounded mass-response window on the generated family.  _(class `C`)_
- **chain closes:** True — The restricted packet includes the runner stdout, primary runner source, and transitive helper sources needed to verify that the quoted LN fits are computed from generated graphs and propagated amplitudes rather than printed constants. The conclusion is bounded to this generated-family setup and does not assert an asymptotic gravity law.
- **rationale:** The runner constructs graphs, selects mass nodes, computes fields and linear/layernorm gravity deltas, then performs log-log power-law fits; the quoted threshold 0.10 and 0.20 LN coefficients, exponents, and R^2 values match the provided cache. The helper chain for graph generation, propagation, field computation, and fitting is included and contains no hard-coded contested fit values. The audited result is a bounded computational theorem for this parameter window only.
- **auditor confidence:** high

### `asymmetry_persistence_pilot_note`

- **Note:** [`ASYMMETRY_PERSISTENCE_PILOT_NOTE.md`](../../docs/ASYMMETRY_PERSISTENCE_PILOT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the sparse npl=30, xyz_range=12.0, connect_radius=4.0, 16-seed primary-runner results for N=40, N=60, and sparse N=80 failure using the included gap_topological_asymmetry readout source.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-141901-30b1a9aa-asymmetry_persistence_pi-044`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** During layer-by-layer generation, low-asymmetry post-barrier candidate nodes are rejected, and the primary runner reproduces the sparse N=40/N=60 baseline-vs-threshold rows plus the N=80 sparse failure entry.  _(class `C`)_
- **chain closes:** True — The primary runner and included helper source compute the graph generation, asymmetry persistence rule, propagation, binning, purity, S_norm, and gravity readouts without hard-coded result tables. Dense N=80/N=100 and layernorm-stacking rows are explicitly outside this audited scope.
- **rationale:** Within the narrowed scope, the cached stdout matches the sparse rows quoted in the note, and the runner source shows those rows are produced by deterministic seeded computation rather than by printing constants. The transitive helper source is included and supplies the load-bearing readout implementation, so the earlier packet-completeness defect is repaired for the sparse table. The dense and layernorm sections remain scientific context only and do not affect this scoped verdict.
- **auditor confidence:** high

### `axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29`

- **Note:** [`AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md`](../../docs/AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The audited claim is only the periodic lattice IR-sum threshold for E_k = 2 sum_mu(1-cos k_mu): d <= 2 is IR-divergent and d >= 3 is IR-finite in the continuum scaling proxy, with finite lattice enumerations matching this threshold for d in {1,2,3,4}.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260531-001401-d06e664a-axiom_first_coleman_merm`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Near k=0, E_k ~ |k|^2, so I_d(L) has the continuum scaling proxy integral_{1/L}^1 r^{d-3} dr, giving linear/log divergences for d=1,2 and finite behavior for d>=3.  _(class `A`)_
- **chain closes:** True — The small-k expansion 2(1-cos k_mu) ~ k_mu^2 and the radial integral test give the stated threshold. The finite table entries are actually computed by the runner and independently match the displayed values; no Ward normalization, no-SSB theorem, D9 kernel authority, or substrate-minimality conclusion is imported.
- **rationale:** The narrowed claim is a mathematical IR-sum scaling statement from the displayed lattice dispersion and standard integral comparison, not an external Coleman-Mermin-Wagner theorem. The runner source enumerates the lattice sums rather than printing constants, and its E0-E3 checks all pass. The formula inventory check finds the displayed small-k scaling, radial exponent, divergence classes, and quantitative table entries consistent with the note's definitions. The explicit non-claims prevent the earlier Ward/SSB/D9/substrate-minimality gaps from being load-bearing here.
- **auditor confidence:** high

### `axiom_first_lattice_noether_abstract_bilinear_continuity_narrow_theorem_note_2026-06-06`

- **Note:** [`AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md`](../../docs/AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Finite matrix-unit algebra identity: an arbitrary bilinear H has the stated local density continuity equation, global charge conservation, orientation antisymmetry, and coefficient-support current envelope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-000243-c1df28ac20-axiom_first_lattice_noether_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Using [E_ij,E_pp] = delta_jp E_ip - delta_pi E_pj, the expansion i[H,rho_p] = i sum_i c_ip E_ip - i sum_j c_pj E_pj equals sum_{q != p} i(c_qp E_qp - c_pq E_pq) after the q=p term cancels.  _(class `A`)_
- **chain closes:** True — The commutator identity directly gives the local continuity equation for arbitrary finite I, and summing over p cancels every oriented pair. The support-envelope and antisymmetry claims follow immediately from the displayed definition of J_{p<-q}.
- **rationale:** The load-bearing step is a genuine algebraic closure from the stated matrix-unit commutator, not a definition substitution or imported physical bridge. An independent manual expansion verifies the sign, the q=p cancellation, global cancellation, and the dependence only on c_pq and c_qp. The runner source performs actual symbolic dictionary algebra and concrete matrix-unit checks without external comparators, hard-coded contested values, or helper opacity. The note explicitly excludes the staggered carrier and physical density bridge, so no open carrier-specific dependency is imported into this scoped claim.
- **auditor confidence:** high

### `background_independence_note`

- **Note:** [`BACKGROUND_INDEPENDENCE_NOTE.md`](../../docs/BACKGROUND_INDEPENDENCE_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For the N=20 fixed cubic lattice runner with Poisson-sourced field, k=1, and M=5, the computed propagator weights, Green-function distances, spectral dimension estimates, and two-mass perturbation measurements differ between flat and sourced configurations.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-background_independence_-021`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Although the graph topology is fixed, the effective geometry, as measured by propagator Green's functions, spectral dimension, and connectivity, changes in response to the gravitational field.  _(class `C`)_
- **chain closes:** True — The runner constructs the Poisson field, weighted lattice Laplacian, Green function column, random-walk transition matrices, and two-mass variants directly from the stated lattice setup. No upstream note or external comparator is imported for the audited numerical claims.
- **rationale:** The runner source performs substantive first-principles computations rather than printing constants: it solves the lattice Poisson problem, builds position-dependent edge weights and Laplacians, solves Green-function systems, estimates heat-kernel spectral dimension, and compares two-mass configurations. The stdout numbers match the note's qualitative and quantitative support at the level needed for the claim that effective propagator geometry changes while topology remains fixed. The conclusion is limited to this finite lattice model and these definitions of effective geometry, not full physical background independence in a broader continuum-gravity sense.
- **auditor confidence:** high

### `backreaction_note`

- **Note:** [`BACKREACTION_NOTE.md`](../../docs/BACKREACTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The audited scope is only the current finite Poisson harness grid: all listed deltas are TOWARD and the first listed escape value below one is at G=0.050, with no continuum threshold, monotone law, or physical Schrodinger-Newton closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-122907-2e5b87e159-backreaction_note`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the declared finite Poisson self-gravity G grid, the live runner certifies a positive baseline delta, first sub-unit escape at G=0.050, and TOWARD deflection through G=0.100.  _(class `C`)_
- **chain closes:** True — The primary runner and helper source instantiate the finite lattice, external field, self-field iteration, propagation, escape ratio, and centroid delta rather than printing the contested output constants. An independent read of the displayed table confirms the bounded conclusions: escape remains above one through G=0.020, falls below one at G=0.050, and all listed deltas are positive.
- **rationale:** The one-hop cited authority is marked retained_bounded, which is retained-grade for this bounded dependency check. The runner does not import or hard-code the stale G_crit ~= 0.011 premise; it computes the finite grid from the exposed Poisson helper and asserts only the live bounded facts. The source note’s displayed summary matches the supplied cache and stays within the stated boundary exclusions, so the chain closes for the bounded finite-grid claim only.
- **auditor confidence:** high

### `bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_bounded_note_2026-05-28`

- **Note:** [`BBN_ETA10_TO_OMEGA_B_H2_COEFFICIENT_ADMISSION_BRIDGE_BOUNDED_NOTE_2026-05-28.md`](../../docs/BBN_ETA10_TO_OMEGA_B_H2_COEFFICIENT_ADMISSION_BRIDGE_BOUNDED_NOTE_2026-05-28.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Conditional admission bridge for the BBN eta_10 to Omega_b h^2 coefficient: the audited content is deterministic arithmetic from the analytic Planck photon-density factor plus explicitly admitted P1-P4 physical/comparator inputs.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_bounded_note_2026-05-28-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Given P1-P4, the Planck photon-density factor and unit-conversion arithmetic give Omega_b h^2 / eta_10 = 3.65541980072764e-3 with S_raw=1, within 0.107% of 3.6515e-3, and exact equality only after admitting S_Cyburt_exact.  _(class `A`)_
- **chain closes:** True — The arithmetic chain closes on its stated conditional scope: the runner source computes the Planck-series factor, present photon density, critical-density unit, raw coefficient, and residual. It does not close as a retained framework derivation because P1-P4 remain supplied premises.
- **rationale:** Issue: the bridge imports P1-P4, including proton mass, CMB temperature, H_100/G/metrology inputs, and the Cyburt residual normalization. Why this blocks: the restricted packet verifies the arithmetic but supplies no retained derivation of those physical and comparator premises. Repair target: derive or explicitly accepted-premise-register the P1-P4 packet, especially S_Cyburt_exact, then re-audit promotion beyond conditional arithmetic. Claim boundary until fixed: the bounded conditional arithmetic bridge is valid given P1-P4, but the Cyburt coefficient is not derived from retained framework inputs.
- **auditor confidence:** high

### `bbs_rg_banach_contraction_external_narrow_theorem_note_2026-05-10`

- **Note:** [`BBS_RG_BANACH_CONTRACTION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/BBS_RG_BANACH_CONTRACTION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** External functional-analysis theorem: bounded linear operators with norm at most kappa<1 obey geometric iterate and composition bounds; strict metric contractions obey the standard fixed-point iterate error bound; and the geometric tail identity holds. No CL3, RG bridge, physical-scale, or numerical-observation claim is audited or made.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e143d-97d9-7b53-9f06-a1586d4121a4`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** If T: B -> B is a bounded linear operator with ||T||_op <= kappa and 0 <= kappa < 1, then ||T^N x0|| <= kappa^N ||x0||; similarly compositions multiply operator-norm bounds, Banach contraction iterates satisfy d(T^N x0,x_*) <= kappa^N d(x0,x_*), and sum_{k>=N} kappa^k = kappa^N/(1-kappa).  _(class `A`)_
- **chain closes:** True — The scoped result is standard functional analysis and elementary algebra: submultiplicativity of operator norm gives the iterate and composition bounds, Banach's contraction theorem gives the fixed-point estimate, and the tail formula is the ordinary geometric series identity. The note explicitly excludes framework blocking/coarse-graining, project couplings, hierarchy formulae, physical scales, and observational comparisons, so no CL3 or physics bridge is required for this narrow claim.
- **rationale:** The claim closes exactly within the stated external-mathematics boundary. There are no hidden project-specific imports, no renaming of physical quantities, and no assertion that a BBS/RG hypothesis holds for any framework map. The BBS/Brydges-Slade material is only cited as context where such estimates are used, not as a load-bearing bridge claim.
- **auditor confidence:** high

### `bell_inequality_derived_note`

- **Note:** [`BELL_INEQUALITY_DERIVED_NOTE.md`](../../docs/BELL_INEQUALITY_DERIVED_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-model CHSH violation on the stated small periodic lattices, with the listed selected G couplings, two distinguishable C^N tensor factors, periodic-Poisson density coupling, and explicit Cl(3) taste-operator checks.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260605-170356-8e35764148-bell_inequality_derived_note`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** For the explicitly defined finite Hamiltonian H = H1⊗I + I⊗H1 + G Σ_ij V(i,j)|i><i|⊗|j><j|, the Horodecki CHSH computation gives |S| > 2 at the listed nonzero G values and |S| = 2 at G = 0.  _(class `C`)_
- **chain closes:** True — The packet defines the finite lattice operators, Poisson pseudoinverse, tensor-product Hamiltonian, and CHSH/taste operators directly, and the runner source computes the displayed values rather than reading or hard-coding them. The closure is only for the bounded model surface, not for physical gravitational normalization or framework-native registration of the two-species/D5 interpretation.
- **rationale:** The load-bearing step is class C for the narrowed finite model: the runner constructs the lattice, Clifford/taste operators, Poisson kernel, Hamiltonian, eigenstates, and CHSH matrix from the stated inputs. The displayed taste identities follow algebraically from x_mu = 2X_mu + eta_mu, and independent spot recomputation reproduces representative 1D, 2D, and 3D CHSH entries. The selected G values are part of the bounded model claim rather than an imported calibrated external comparator, so this is not class G on the audited scope. No broader physical or framework-native Bell theorem is ratified here.
- **auditor confidence:** high

### `beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10`

- **Note:** [`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The standalone rational-function algebra identity β(g,N)=2N/g^2 under g↦g/c, the invariant product βg^2=2N, and the associated positive-rational orbit/injectivity statements for β-values in the image.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260606-162502-9946b4d81b-beta_gbare_rescaling_abstrac`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Direct substitution gives β(g/c,N)=2N/(g/c)^2=2Nc^2/g^2=c^2β(g,N).  _(class `A`)_
- **chain closes:** True — The conclusions follow from direct algebraic substitution and cancellation with g,c nonzero. T3 follows because c>0 and c≠1 imply c^2≠1, and the map g↦2N0/g^2 is injective on positive g when N0≠0.
- **rationale:** The load-bearing step is a genuine class A algebraic identity over the stated variables, with no cited upstream authority or physical import needed. The runner source actually computes the symbolic residuals with sympy and exact rational checks rather than merely printing expected results. The note’s Wilson, Cl(3), SU(Nc), and g_bare language is explicitly non-load-bearing for this narrow claim.
- **auditor confidence:** high

### `beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08`

- **Note:** [`BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md`](../../docs/BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md)
- **claim_type:** `decoration`
- **claim_scope:** Pure algebraic invariance of beta(g,N) g^2 = 2N under the abstract joint rescaling (g,beta)->(g/c,c^2 beta), specialized only by the symbolic names (g,N)=(g_bare,N_c).
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Under the abstract joint rescaling (g, beta) -> (g/c, c^2 beta), (c^2 beta)(g^2/c^2)=beta g^2=2N, with (g,N) only symbolically relabeled as (g_bare,N_c).  _(class `A`)_
- **chain closes:** True — The product cancellation follows directly from the retained upstream abstract identity and ordinary rational algebra. The row adds symbolic naming and boundary clauses, so it closes only as an algebraic corollary of the parent, not as an independent Wilson-surface result.
- **rationale:** The cited upstream authority is retained and already proves the abstract beta(g/c,N)=c^2 beta(g,N) identity and product invariance. The present note repeats that exact algebra with the variable names (g_bare,N_c) and expressly keeps any physical Wilson action-surface interpretation outside the audited scope. With zero comparator checks and no independent physical computation, the row is an algebraic decoration of the retained parent rather than an independent clean theorem.
- **decoration parent:** `beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10`
- **auditor confidence:** high

### `block_gaussian_schur_marginalization_narrow_theorem_note_2026-05-02`

- **Note:** [`BLOCK_GAUSSIAN_SCHUR_MARGINALIZATION_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/BLOCK_GAUSSIAN_SCHUR_MARGINALIZATION_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Standalone real symmetric positive-definite block-matrix Schur marginalization formula, including K_eff, J_eff, symmetry/positivity of K_eff, determinant identity, and stated sequential-marginalization associativity.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-block_gaussian_schur_mar-022`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Completing the square in q_F at fixed q_U gives q_F^*(q_U)=C^{-1}(xi-B^T q_U), and substituting yields K_eff=A-B C^{-1}B^T and J_eff=eta-B C^{-1}xi.  _(class `A`)_
- **chain closes:** True — The main marginalization, source update, symmetry, positivity, and determinant identity follow by direct block algebra from the stated PD block-matrix hypotheses. The associativity statement is only sketched as classical, but it is an algebraic property of iterated Schur complements under the same invertibility/PD hypotheses and introduces no external premise.
- **rationale:** The load-bearing step is a genuine algebraic identity over the stated real symmetric PD block matrix and source, with no cited upstream authorities or imported physical assumptions. The runner performs exact SymPy checks of the Schur complement, source update, determinant identity, and completing-square residual rather than merely printing constants. The runner does not separately test sequential marginalization associativity, so that point rests on the note's standard algebraic assertion, but it does not create an open dependency or renaming.
- **auditor confidence:** high

### `bmv_entanglement_note_2026-04-11`

- **Note:** [`BMV_ENTANGLEMENT_NOTE_2026-04-11.md`](../../docs/BMV_ENTANGLEMENT_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop:medium-sweep-2026-04-30-01`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On a fixed externally imposed geometry-branch superposition, the runner computes delta_S > 0 for every tested coupling and S_quantum saturates near ln(2).  _(class `C`)_
- **chain closes:** True — The source is explicitly bounded to the externally imposed two-branch protocol, and the current runner recomputes the overlaps, entropy values, positive delta_S table, and norm conservation without one-hop dependencies.
- **rationale:** The note's claim is narrow and matches the current runner output: a finite staggered-lattice protocol with an externally imposed source branch gives positive branch-mediated entanglement beyond the corresponding classical mixture. The note does not claim a full BMV witness or dynamically generated gravitational branch, so the main hidden-premise failure mode is already excluded by the source boundary. Residual risk is limited to the finite protocol and implementation assumptions, which are inside the declared bounded scope.
- **auditor confidence:** high

### `bmv_threebody_note_2026-04-11`

- **Note:** [`BMV_THREEBODY_NOTE_2026-04-11.md`](../../docs/BMV_THREEBODY_NOTE_2026-04-11.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop:medium-sweep-2026-04-30-02`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The note demotes the standalone GHZ-like runner and bases the support claim on the robustness harness: 25/25 configurations are W or W-asym with tau_3 = 0 for the fixed two-branch protocol.  _(class `C`)_
- **chain closes:** True — The source is support-tier and explicitly bounded to externally imposed two-branch tripartite entanglement. The current robustness runner recomputes the source/coupling surface and prints tau_3 = 0, W/W-asym classification in 25/25 configurations, and positive bipartite entropies.
- **rationale:** The load-bearing support claim closes because the note clearly makes the later robustness harness, not the historical standalone heuristic runner, the canonical interpretation surface. That canonical runner reproduces the stated W-type result and the note keeps the boundary narrow: fixed adjacency, externally imposed branch, not a full three-body BMV witness or topology-superposition claim. The historical runner's GHZ-like rows are not a contradiction because both the source note and that runner label them as non-canonical heuristic output.
- **auditor confidence:** high

### `born_lane_comparison_note`

- **Note:** [`BORN_LANE_COMPARISON_NOTE.md`](../../docs/BORN_LANE_COMPARISON_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded comparison that the modular gap + LN and central-band |y| removal + LN lanes are Born-clean on the corrected Sorkin harness for N=25,40,60 with the stated seeds and parameters.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T174655Z-7e9951db-born_lane_comparison_not-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Both best LN lanes are Born-clean on the corrected harness at machine precision, with all |I3|/P entries at order 1e-16 to 1e-15.  _(class `C`)_
- **chain closes:** True — The runner constructs the two graph families, applies the layer-normalized propagator, computes corrected Sorkin I3 including -P(empty), and reports machine-precision ratios. The helper sources are present and implement graph generation, field computation, and propagation rather than importing or hard-coding the contested result.
- **rationale:** The source note's qualitative claims are bounded to the displayed runner configuration and are supported by a completed cached run. The runner source genuinely computes the amplitudes and corrected Born ratios from generated DAGs and helper primitives; it does not merely print constants or compare against an imported target. The note's table values are stale relative to the included stdout, but the mismatch does not change the audited conclusion because the current stdout still places both lanes at 1e-16 to 1e-15 and preserves the stated non-monotone ordering/no-winner summary.
- **auditor confidence:** medium

### `bougerol_lacroix_oseledets_met_external_narrow_theorem_note_2026-05-10`

- **Note:** [`BOUGEROL_LACROIX_OSELEDETS_MET_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/BOUGEROL_LACROIX_OSELEDETS_MET_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** External narrow MET statement for i.i.d. invertible finite-dimensional real or complex matrix products assuming finite E log^+ ||A_0|| and finite E log^+ ||A_0^{-1}||, with no finite-N rate, spectral-gap, projective-action, or framework bridge claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e14ae-cbd9-7383-87d2-276fd52b4460`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Under the stated integrability hypotheses, Oseledets' multiplicative ergodic theorem gives deterministic Lyapunov exponents and an invariant filtration with almost-sure vector growth limits.  _(class `B`)_
- **chain closes:** True — Within the stated boundary, the note only records the standard Oseledets MET consequence under its hypotheses and explicitly excludes framework and spectral-gap extrapolations. The runner does not prove the external theorem, but it checks consistency examples and boundary hygiene without introducing an overclaim.
- **rationale:** The scoped claim is a narrow external theorem statement, not a project-specific derivation or physical bridge. The load-bearing theorem is standardly cited in the note, the assumptions are stated, and the boundary excludes the common invalid extensions that would require additional retained inputs.
- **auditor confidence:** high

### `bound_state_selection_note`

- **Note:** [`BOUND_STATE_SELECTION_NOTE.md`](../../docs/BOUND_STATE_SELECTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite regularized lattice diagnostic for d=2,3,4,5 on the listed grid sizes and couplings: the runner-built sparse Hamiltonians reproduce the printed negative-eigenvalue counts, ground-state energies, IPR/localization diagnostics, propagation ratios, and d=4/d=5 coupling-scan trends. This excludes any retained continuum bridge to atomic chemistry, anthropic dimension selection, exclusion of d=2, or a theorem that d>=4 falls to center under the implemented IPR threshold.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-judicial-gpt-5.5-20260511-231510-bound_state_selection_no-011`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** The lattice Hamiltonian on the listed grid sizes reproduces the dimension-dependent bound-state diagnostic in the printed bands of the Results table, while any promotion to d=3 stable-atom selection is bridge-conditional.  _(class `C`)_
- **chain closes:** True — The restricted packet contains runner source that constructs sparse finite-dimensional lattice Hamiltonians, Coulomb potentials, eigenvalue solves, localization diagnostics, and coupling scans rather than merely printing constants or importing the contested result. Under the note's explicitly narrowed perimeter, the audited claim is only the finite-N regularized numerical diagnostic, not the continuum stable-matter or anthropic selection statement. That bounded finite computation closes from the specified numerical setup and completed runner output, so the hostile-review result matches the first audit tuple.
- **rationale:** The restricted packet contains runner source that constructs sparse finite-dimensional lattice Hamiltonians, Coulomb potentials, eigenvalue solves, localization diagnostics, and coupling scans rather than merely printing constants or importing the contested result. Under the note's explicitly narrowed perimeter, the audited claim is only the finite-N regularized numerical diagnostic, not the continuum stable-matter or anthropic selection statement. That bounded finite computation closes from the specified numerical setup and completed runner output, so the hostile-review result matches the first audit tuple.
- **auditor confidence:** high

### `branch_entanglement_robustness_note_2026-04-11`

- **Note:** [`BRANCH_ENTANGLEMENT_ROBUSTNESS_NOTE_2026-04-11.md`](../../docs/BRANCH_ENTANGLEMENT_ROBUSTNESS_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded robustness replay on an externally imposed fixed-adjacency two-branch staggered-lattice protocol: 2-body branch-entanglement delta_S remains positive across the stated sweeps, and the 3-body surface is W-type rather than GHZ-type on the stated configurations.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-aquinas-3rd-019debbe-8c91-7a01-a66d-f059d559c070`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The robustness runner recomputes the fixed-adjacency two-branch staggered-lattice protocol and reports 2-body delta_S > 0 in 60/60 audited configurations plus 3-body tau_3 = 0 with W/W-asym classification in 25/25 configurations.  _(class `C`)_
- **chain closes:** True — The one-hop dependencies are now retained-grade and support the bounded 2-body branch-entanglement interpretation and corrected 3-body W-type interpretation. The current source note and runner output close the scoped robustness claim without relying on full BMV witness status or an external comparator.
- **rationale:** The clean verdict applies only to the bounded numerical protocol theorem stated in the note. The load-bearing runner output gives positive 2-body delta_S across all audited sweeps and confirms the corrected 3-body W-type, non-GHZ interpretation with tau_3 = 0 and positive bipartite entropies. The prior dependency block is resolved because both cited one-hop dependencies now have retained-grade status. Plot generation failed due to missing matplotlib, but that does not affect the load-bearing numerical checks.
- **auditor confidence:** medium

### `branching_slack_rate_projective_limit_bounded_theorem_note_2026-06-12`

- **Note:** [`BRANCHING_SLACK_RATE_PROJECTIVE_LIMIT_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/BRANCHING_SLACK_RATE_PROJECTIVE_LIMIT_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Exact broadcast plus weak-measurement trees for NFRAG in {3,4,5}, eps in {0.3,0.6,0.9,0.95,0.99}, thresholds {0.3,0.5,0.7}, with eps=0/1 and |0>-pointer controls.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260613-003651-9a1e09f496-branching_slack_rate_project`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The exact finite-tree computation gives the printed weighted slack/rate tables and verifies R_b <= NFRAG - B_b, strict slack increase on eps=0.3/0.6/0.9, and the sampled near-projective rate trend.  _(class `C`)_
- **chain closes:** True — The runner constructs the branch state vectors from CNOT broadcasts and weak Kraus factors, then computes weights, connected-correlator records, blanks, entropy, and slack without opaque helpers or hard-coded contested outputs. Independently, each branch reduces to two amplitudes A^k B^(N-k) and B^k A^(N-k), giving C=4p(1-p) and reproducing the displayed slack/rate and threshold tables.
- **rationale:** The claim is bounded to a finite sampled model and does not rely on external comparator data or cross-note numerical imports. The runner source genuinely computes the finite model rather than merely printing expected values, and the independent combinatorial check confirms the load-bearing table entries, inequalities, controls, and trend values. The eps=1 statement is clean only in the scoped sense stated in the note: pointer-eigenstate/zero-record control, not an unscoped asymptotic or generic-state theorem.
- **auditor confidence:** high

### `bridge_gap_hk_cube_perron_note_2026-05-06`

- **Note:** [`BRIDGE_GAP_HK_CUBE_PERRON_NOTE_2026-05-06.md`](../../docs/BRIDGE_GAP_HK_CUBE_PERRON_NOTE_2026-05-06.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fixed L_s=2 heat-kernel cube Perron computation at t=1 using the stated candidate-rho ansatz and finite NMAX convergence, not a thermodynamic-limit or action-uniqueness claim.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-hygiene-cycle-break-20260707-193821-5b3b16-bridge_gap_hk_cube_perron_note_2-03`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Substituting heat-kernel character coefficients into the L_s=2 candidate-rho Perron transfer operator gives P_cube_HK(L_s=2,t=1)=0.5223243151, stable across NMAX.  _(class `C`)_
- **chain closes:** False — The runner genuinely computes the stated finite Perron value from the provided formulas, but the candidate-rho/Perron machinery and Casimir/time/action premises are imported from cited authorities that are not retained-grade in this packet. The co-cycle citation bridge_gap_hk_thermodynamic_stretch_note_2026-05-06 is treated as informational and not used as chain support.
- **rationale:** The primary runner source is substantive: it defines SU(3) dimensions, Casimirs, HK coefficients, candidate rho, the recurrence operator, local HK factor, and symmetric Perron solve, and its cached output matches the note's numerical claim. However, the load-bearing candidate-rho/Perron ansatz is inherited from docs/SU3_CUBE_FULL_RHO_PERRON_2026-05-04.md and the Casimir/HK premises are cited through unaudited authorities, so the chain is conditional under the rubric. The co-cycle link docs/BRIDGE_GAP_HK_THERMODYNAMIC_STRETCH_NOTE_2026-05-06.md is non-load-bearing/informational for this re-audit, but source-graph repair is still needed to strip or rewrite those markdown links before effective_status can leave retained_pending_chain.
- **open / conditional deps cited:**
  - `SU3_CUBE_FULL_RHO_PERRON_2026-05-04.md`
  - `BRIDGE_GAP_HK_PLAQUETTE_CLOSED_FORM_NOTE_2026-05-06.md`
  - `BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md`
  - `SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md`
- **auditor confidence:** high

### `broad_gravity_derivation_note`

- **Note:** [`BROAD_GRAVITY_DERIVATION_NOTE.md`](../../docs/BROAD_GRAVITY_DERIVATION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Algebraic k-cancellation for stationary paths and phase-rate ratios under the explicitly supplied weak-field action and readout forms, without certifying their physical gravity interpretation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T130312Z-96c5c841-00242-broad_gravity_derivation_not`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** For nonzero k, the common multiplicative factor k cancels from both the stationary equation delta S = k delta F = 0 and the supplied phase-rate ratio.  _(class `A`)_
- **chain closes:** True — For k != 0, delta S = 0 is equivalent to delta F = 0, and k cancels from omega(x1)/omega(x2) wherever the ratio is defined. These conclusions require only the supplied formulas and standard algebra.
- **rationale:** The source confines its conclusion to algebra over explicitly supplied action and phase-rate forms. The runner performs the relevant symbolic cancellations and verifies that the note excludes the former physical-gravity promotions. Within the audited bounded scope, the stated conclusions follow directly.
- **auditor confidence:** high

### `causal_escape_window_note`

- **Note:** [`CAUSAL_ESCAPE_WINDOW_NOTE.md`](../../docs/CAUSAL_ESCAPE_WINDOW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite runner-bounded diagnostic for the specified propagation/trap model, parameters, families, and seeds showing an escape window and its exposure-matched static comparator within the imposed simulation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-causal-escape-B`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** At eta=20, s=0.004, c=0.25, the instantaneous field traps while the dynamic causal field escapes, with forward-only static not escaping and exposure-matched static also escaping.  _(class `C`)_
- **chain closes:** True — The current runner computes the headline window, exposure-matched static proxy, c/eta/s tables, portability checks, and four-seed gate rather than merely asserting them in prose. Closure is only for this finite diagnostic and does not establish black-hole escape physics, self-consistent field closure, or an irreducible cone-geometry mechanism.
- **rationale:** The repaired runner constructs the lattice-like propagation model, evaluates the field variants, and computes escape ratios from the stated finite setup; the target values are not hard-coded as expected constants. The completed cache exits successfully and includes the previously missing exposure-matched static, c/eta/s, portability, and four-seed robustness evidence. The clean verdict is bounded to the runner-defined diagnostic, while stale conditional labels and broader causal-gravity prose in the note are not promoted.
- **auditor confidence:** high

### `causal_propagating_field_live_packet_note_2026-06-05`

- **Note:** [`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](../../docs/CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite configured replay for drift=0.20, restore=0.70, seeds 0-5, source layer 8, strengths 1e-5/5e-5/1e-4, and zero/instantaneous/forward-only/dynamic c=1.0/c=0.5 field cases.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260621-054531-f51f6887-causal_propagating_field_live_packet_note_2026-06-05-reaudit`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** In this configured center-family runner, finite cone fields produce stable strength-independent proxy ratios, and the archived 0.45 dynamic row is stale.  _(class `C`)_
- **chain closes:** True — Within the declared configured-family scope, the runner constructs the structured-growth family, computes the field cases, propagates amplitudes, and measures centroid ratio readouts. The current live ratios are computed rather than imported or hard-coded; the archived 0.45 value is used only as a rejected stale comparator.
- **rationale:** The primary runner and helper source are included and the load-bearing path genuinely computes the finite replay from the configured growth, field, propagation, and centroid routines. The stdout values match the note's narrowed safe read, and the code does not claim a physical wave speed, derived carrier, self-consistent retarded field, or cross-family portability law. The conclusion therefore closes only as a bounded configured-runner fact, not as the archived 0.63/0.45 positive table or a broader physics theorem.
- **auditor confidence:** high

### `central_band_born_dense_sweep_note`

- **Note:** [`CENTRAL_BAND_BORN_DENSE_SWEEP_NOTE.md`](../../docs/CENTRAL_BAND_BORN_DENSE_SWEEP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite valid-graph dense-pocket result for the central-band corrected-Born sweep at npl = 60, limited to the six retained LN+|y| and LN+|y|+collapse rows for N = 25, 40, 60 in the cached runner output.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260518-120032-569b3ebd-central_band_born_dense_-033`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At npl = 60, both LN + |y| and LN + |y| + collapse stay Born-clean to machine precision across N = 25, 40, 60.  _(class `C`)_
- **chain closes:** True — The restricted packet includes the primary runner and its helper, and the code actually constructs the graphs, propagates amplitudes, computes the corrected three-slit I3 with -P(empty), and reports the six bounded rows. The broad hard-geometry-enabling interpretation is explicitly out of load-bearing scope.
- **rationale:** The load-bearing narrowed claim is a bounded computational result, not the broader interpretation hypothesis. The runner source does not merely print constants or import a contested result; it builds the graph instances, applies the stated modes, computes total probabilities for slit subsets, and forms I3 with the empty term. The cached stdout supports all six in-scope npl = 60 rows as PASS with maxima below 1e-15, although the note's displayed table contains stale numeric entries that should be reconciled against the cache.
- **auditor confidence:** high

### `central_band_born_largen_note`

- **Note:** [`CENTRAL_BAND_BORN_LARGEN_NOTE.md`](../../docs/CENTRAL_BAND_BORN_LARGEN_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited the restricted-packet claim that the provided large-N chokepoint runner and helper compute corrected three-slit |I3|/P for N=80,100, npl=60 under LN+|y| and LN+|y|+collapse, and find PASS-level machine-precision values.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-151715-a5e2dcef-central_band_born_largen-008`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The dense central-band Born pocket survives at N = 80 and N = 100 for both LN + |y| and LN + |y| + collapse, with corrected |I3|/P at machine precision.  _(class `C`)_
- **chain closes:** True — The primary runner calls helper code that constructs random 3D chokepoint DAGs, applies post-barrier central-band removal, propagates amplitudes exactly, and evaluates the corrected Sorkin metric with the -P(empty) term. No cited upstream authority is required beyond the provided computation, and the completed run supports the qualitative survival/PASS claim.
- **rationale:** The runner source is substantive rather than a print-only or hard-coded expected-value check: it builds the graph, computes amplitudes for each slit subset, and forms |I3|/P directly. The completed runner output gives PASS for all four retained rows in the audited scope: N=80 and N=100 for LN+|y| and LN+|y|+collapse. The note's N=80 table values are stale relative to the supplied runner output, but the discrepancy does not change the load-bearing conclusion because all reported maxima remain far below the stated machine-precision gate of 1e-10. A second auditor should re-check whether the note should be updated to the current cached numbers and should note that only 3 seeds at N=80 and 1 seed at N=100 produced usable rows despite 4 attempted seeds.
- **auditor confidence:** high

### `central_band_collapse_note`

- **Note:** [`CENTRAL_BAND_COLLAPSE_NOTE.md`](../../docs/CENTRAL_BAND_COLLAPSE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded matched-seed computational card for N = 25, 40, 60 central-band removal with p = 0.2 stochastic collapse, using the provided primary runner and helper sources.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T174804Z-5d888ef6-central_band_collapse_no-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The best supported joint row on this card is N = 60, LN + |y| + collapse, which keeps positive gravity and the lowest purity on the N = 60 rows.  _(class `C`)_
- **chain closes:** True — The provided runner constructs the graphs, applies central-band pruning, computes deterministic purity/gravity and Monte Carlo collapse purity/gravity, and its cached stdout matches the note's reported rows. The conclusion is bounded to this finite runner configuration and does not claim asymptotic closure.
- **rationale:** The primary runner and helpers do not simply print constants or import the contested numbers; they generate matched random DAG instances and compute the reported metrics from the implemented propagation, pruning, field, and collapse rules. The note's numerical rows match the cached successful runner output. The clean verdict is limited to the bounded computational claim at the stated seeds, graph parameters, and collapse settings, not to a general asymptotic gravity law.
- **auditor confidence:** high

### `central_band_collapse_strength_note`

- **Note:** [`CENTRAL_BAND_COLLAPSE_STRENGTH_NOTE.md`](../../docs/CENTRAL_BAND_COLLAPSE_STRENGTH_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite runner-backed calibration that, for the stated central-band chokepoint harness, seeds, realizations, N values, and collapse probabilities, the corrected Sorkin `|I3|/P` maxima for `LN+|y|+collapse` are below `1e-10`.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T174907Z-d49a884c-central_band_collapse_st-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** All six `LN + |y| + collapse` rows in the swept `p in {0.05, 0.10, 0.20}` by `N in {40, 60}` grid sit below the `1e-10` machine-precision threshold on the corrected `I3 / P` metric.  _(class `C`)_
- **chain closes:** True — The primary runner and included helper construct the graph, apply the stated central-band removal, propagate amplitudes, generate collapse phases, and compute corrected `I3 = P_abc - P_ab - P_ac - P_bc + P_a + P_b + P_c - P_empty`. The cached stdout matches the note's retained rows and there is no hard-coded expected value, imported contested premise, or external comparator in the load-bearing path.
- **rationale:** The note's conclusion is narrow and bounded to the completed finite sweep, not a broader mechanism or monotone optimization claim. The supplied runner source genuinely computes the stated metric through the helper chain, and the cached output supports every numeric row quoted in the note. Seed accounting and the non-monotone p-ordering are explicitly scoped and do not create an unclosed dependency.
- **auditor confidence:** high

### `central_band_dense_boundary_note`

- **Note:** [`CENTRAL_BAND_DENSE_BOUNDARY_NOTE.md`](../../docs/CENTRAL_BAND_DENSE_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite runner-backed sweep at N = 80, 100 with npl = 60, y_cut = 2.0, connect_radius = 2.8..3.4, seeds [3, 10, 17, 24], 8 realizations, evaluating only the stated P1/P2 operational sharp-boundary predicates.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T175048Z-61b88ef0-central_band_dense_bound-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At N = 100, LN+|y| gravity changes from -0.044 at r = 3.0 to +5.210 at r = 3.2, and purity drops from 1.000 to 0.750, so P1 and P2 both fire at r = 3.2 while N = 80 has no mean-gravity sign flip.  _(class `C`)_
- **chain closes:** True — The cached runner output matches the note's tables, and the supplied primary and helper sources compute graph construction, Born metric, purity, and gravity from deterministic seeded procedures rather than hard-coded expected values. The conclusion follows only for the stated finite configuration and operational mean-sign/purity-drop predicates.
- **rationale:** The runner and helper chain is complete in the packet and performs the load-bearing computation instead of importing a contested result from another note or external comparator. The P1/P2 evaluations are numerically consistent with the cached stdout: N = 100 passes both predicates at r = 3.2, while N = 80 has no mean-gravity sign flip in the swept window. The note also preserves the necessary finite-scope limitation and does not generalize the boundary claim beyond the stated sweep.
- **auditor confidence:** high

### `central_band_dense_joint_highn_note`

- **Note:** [`CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md`](../../docs/CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded high-N dense central-band scan for N=80,100 over npl=60,70,80 using the provided same-graph Born, purity, and gravity runner chain.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-151813-a5e2dcef-central_band_dense_joint-009`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Born-safe dense central-band coexistence survives at N=80 and N=100 only inside a narrow density window, with strongest retained N=80 at npl=80 and N=100 at npl=70.  _(class `C`)_
- **chain closes:** True — The primary runner and included helpers construct the graph family, propagate amplitudes, compute corrected Born I3/P, purity, and gravity deltas directly from the restricted code path. The note's retained rows match the completed runner output and the exclusions are consistent with Born violation or weak/noisy gravity within the stated bounded scope.
- **rationale:** The load-bearing result is a bounded computational theorem over a specified graph family and parameter grid, not a definition, renaming, external comparator, or tuned match to an outside number. The primary runner imports only helper functions included in the packet, and those helpers instantiate the graph generation, propagation, Born metric, purity, collapse, and gravity calculations rather than hard-coding the reported rows. The runner output supports the note's narrowed claim: N=80 npl=80 remains Born-clean with positive noisy gravity, N=100 npl=70 is the strongest retained Born-clean positive row, and N=100 npl=80 is not retained because Born |I3|/P is 0.250.
- **auditor confidence:** high

### `central_band_dense_joint_note`

- **Note:** [`CENTRAL_BAND_DENSE_JOINT_NOTE.md`](../../docs/CENTRAL_BAND_DENSE_JOINT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the fixed-parameter runner-backed claim for N=40 and N=60 dense central-band graphs with 4 seeds, npl=60, yz_range=12.0, connect_radius=3.0, y_cut=2.0, and 8 collapse realizations, limited to the printed mean±SE rows.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-141901-30b1a9aa-central_band_dense_joint-049`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The dense central-band pocket is Born-clean as a bounded mean±SE statement, and at N=60 the same graph family retains positive gravity while collapse lowers the purity floor.  _(class `C`)_
- **chain closes:** True — The runner source and included helpers generate the graph family, propagate amplitudes, compute the corrected Born metric, purity, and gravity delta, and print values matching the note. The narrowed claim does not assert the high-precision per-row max |I3|/P threshold, so the missing threshold check is outside the audited scope.
- **rationale:** The note's current load-bearing claim is bounded to the runner's actual outputs: rounded Born mean±SE, same-graph purity, and gravity rows for the stated finite setup. The primary runner is not a constant printer and does not import the contested values from another note; it calls included helper code that constructs the graphs and computes the reported observables. The cached stdout matches the note's retained rows, including the repaired N=40 and N=60 collapse values. The open high-precision max-threshold assertion is explicitly excluded from the present claim.
- **auditor confidence:** high

### `central_band_dense_largen_note`

- **Note:** [`CENTRAL_BAND_DENSE_LARGEN_NOTE.md`](../../docs/CENTRAL_BAND_DENSE_LARGEN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the fixed-geometry large-N dense central-band same-graph runner at defaults: N=80,100; npl=60; y_cut=2.0; yz_range=12.0; connect_radius=3.0; four matched seeds; eight collapse realizations.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T175319Z-76bbad40-central_band_dense_large-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The current runner stdout at declared defaults reports Born |I3|/P = 0.000±0.000 for the surviving N=80 and N=100 dense central-band rows, with gravity negative at N=80 and single-seed near-zero/small-negative at N=100.  _(class `C`)_
- **chain closes:** True — The primary runner and included helpers build the graphs, compute Born metrics, purity/decoherence readouts, and same-graph gravity deltas directly rather than importing or hard-coding the contested table values. The note's narrow bounded conclusion matches the cached stdout, including the one-seed limitation at N=100.
- **rationale:** The runner source is present with transitive helper sources and performs actual graph generation, propagation, collapse-phase averaging, Born I3 calculation, purity, and gravity readout computation. The stdout matches the note's table and the note explicitly limits the N=100 gravity interpretation because only one seed survives. No upstream support note, external comparator, tuned empirical constant, or symbol renaming is used in the load-bearing step. The result is clean only as a bounded computational claim at the declared defaults, not as a universal large-N law.
- **auditor confidence:** high

### `central_band_layernorm_note`

- **Note:** [`CENTRAL_BAND_LAYERNORM_NOTE.md`](../../docs/CENTRAL_BAND_LAYERNORM_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite matched-seed runner audit of central-band removal with layernorm for N=25,40,60,80,100, y_cut in {1,2,3}, plus in-packet comparison to the modular-gap=2 + layernorm row.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260521-215638-bb10cae5-central_band_layernorm_n-024`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Using the decoherence-optimal y_cut = 2 layernorm row, the central-band fit is (1 - pur_min) = 4.81 * N^(-0.813) and it is competitive with, but does not dominate, modular gap=2 + layernorm.  _(class `C`)_
- **chain closes:** True — The primary runner and helper sources compute the central-band graph generation, pruning, propagation, purity, gravity, and standard-error summaries directly rather than printing constants. The modular-gap comparison row and fit are inlined, and the one-hop cited authority is retained_bounded.
- **rationale:** The central-band numerical table is supported by completed runner stdout whose values match the note, and the runner source performs the graph construction, pruning rule, propagation, purity, and gravity computations without hard-coded expected outputs. The scaling fit and threshold comparisons are algebraic summaries over the computed row and the inlined modular-gap row. The conclusion is bounded and appropriately cautious: central-band removal is competitive through the finite sweep but not a universal winner.
- **auditor confidence:** high

### `central_band_mass_window_note`

- **Note:** [`CENTRAL_BAND_MASS_WINDOW_NOTE.md`](../../docs/CENTRAL_BAND_MASS_WINDOW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded runner-backed comparison of plain versus central-band-pruned gravity delta mass-window power-law fits at N = 60, 80, 100 with 16 matched seeds and fit window M in {2,3,5,8}.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T173751Z-a3b3f0a3-central_band_mass_window-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the densest slice N = 100, both pruned rows fit cleaner power laws than either plain mode, with pruned LN R^2 = 0.994 and pruned linear R^2 = 0.825 versus plain linear R^2 = 0.634 and plain LN R^2 = 0.248.  _(class `C`)_
- **chain closes:** True — The provided runner and helper sources actually generate matched graphs, compute gravity deltas for the declared modes and mass counts, and fit the declared positive window without hard-coded target values. The cached stdout matches the note's numerical claims and supports the bounded, mixed conclusion.
- **rationale:** The source note makes a narrow bounded claim about the runner's computed mass-window fits, not a full gravity-law rescue. The runner source and helper chain compute the graph, pruning, propagation, deltas, and log-log fits directly from the declared simulation setup, and the reported R^2 comparisons are reproduced in the provided stdout. No cited non-retained authority, external comparator, renaming, or tuned imported value is load-bearing in this packet.
- **auditor confidence:** high

### `charged_lepton_registered_mass_dft_coordinate_theorem_note_2026-07-11`

- **Note:** [`CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md`](../../docs/CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For any supplied positive real mass triple, the normalized C3 DFT gives exact reconstruction, a symmetric scale- and permutation-invariant r coordinate, Q = 1/3 + 2r/3 with r unselected, and an S3-invariant folded phase for the unordered triple, including the c = 0 boundary.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt-5.6-sol-xhigh-fresh-registered-mass-repaired-retry-2026-07-12`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** Parseval in the stated normalization gives sum_j z_j^2 = 3(a^2 + 2|c|^2), hence Q = 1/3 + 2r/3, while the S3 action on c folds phi to an unordered-triple invariant.  _(class `A`)_
- **chain closes:** True — Root-of-unity orthogonality and real conjugacy close the result directly, and an independent exact Q(omega) calculation confirms every displayed identity. Positivity supplies a > 0 and in fact restricts the coordinate to 0 <= r < 1, while the theorem asserts the weaker r >= 0 and leaves its value unselected.
- **rationale:** Direct expansion in Q(omega), using omega^2 + omega + 1 = 0, independently reproduces the inverse transform, the 6|c|^2 variance identity, Parseval, and Q = 1/3 + 2r/3. The S3 action phi -> +/-phi + 2pi k/3 proves folded-phase invariance and unordered reconstruction, including the c = 0 limit. The scope starts from a supplied positive triple; physical functional construction and empirical comparison are explicitly outside scope, and r remains unselected.
- **auditor confidence:** high

### `chiral_3plus1d_boundary_phase_note`

- **Note:** [`CHIRAL_3PLUS1D_BOUNDARY_PHASE_NOTE.md`](../../docs/CHIRAL_3PLUS1D_BOUNDARY_PHASE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite boundary-condition phase scan for periodic, reflecting, and open boundaries across coherent, classical, and phase-kill modes on the declared 5x5 (lambda, delta) grid at n=21 and n=31; recurrence-artifact interpretation excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-152125-a5e2dcef-chiral_3plus1d_boundary_-011`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The binding evidence is exactly the finite-scan tabulated results from the boundary classes, propagation modes, and (lambda, delta) cells at n in {21,31}, with the recurrence-artifact interpretation out of scope.  _(class `C`)_
- **chain closes:** True — The runner source genuinely constructs the lattice walk, boundary shifts, observables, and aggregation over the declared grid rather than printing hard-coded expected values. The provided stdout matches the note's bounded finite-scan claims.
- **rationale:** After the 2026-05-17 scope narrowing, the audited claim is only the finite scan record, not the physical interpretation that periodic AWAY windows are recurrence artifacts. The runner computes the stated grid directly from fixed model operators and boundary rules, with no helper imports or cited upstream premises. The tabulated output supports the note's reported AWAY cells, reflecting/open behavior, and zero periodic torus-sensitive cells within the finite grid.
- **auditor confidence:** high

### `chiral_3plus1d_coupled_coin_note`

- **Note:** [`CHIRAL_3PLUS1D_COUPLED_COIN_NOTE.md`](../../docs/CHIRAL_3PLUS1D_COUPLED_COIN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the explicitly defined 3+1D six-component coupled-coin scan at n=17, theta0=0.3, strength=5e-4, and mix in {0,0.125,...,1}, the computed metrics show improved gauge-loop visibility and KG-fit R^2 relative to the factorized mix=0 baseline, but no clean isotropic 3D KG law.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T175755Z-ec176ca3-chiral_3plus1d_coupled_c-01`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Cross-axis coupling materially improves both observables relative to the factorized baseline, with loop response rising from zero at mix=0 to strong modulation near the coupled end while dispersion remains only moderate.  _(class `C`)_
- **chain closes:** True — The runner source directly constructs the coin, shift, dispersion, and loop-response observables and produces the values reported in the note without importing another note or hard-coding the contested results. The closure is bounded to this scan family, parameter grid, and observable definitions.
- **rationale:** The note is scoped as an exploratory bounded computational claim, not as a broad 3+1D transport theorem. Within that bounded scope, the completed runner output matches the note and the source computes the reported scan metrics from the locally defined lattice walk rather than printing constants or reading upstream results. The interpretation that coupling helps but is insufficient for a clean isotropic KG law follows from the reported improvement in R^2 and gauge visibility together with the still-moderate dispersion quality.
- **auditor confidence:** high

### `chiral_3plus1d_recurrence_note`

- **Note:** [`CHIRAL_3PLUS1D_RECURRENCE_NOTE.md`](../../docs/CHIRAL_3PLUS1D_RECURRENCE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite periodic 3+1D chiral recurrence diagnostic for theta0=0.3, strength=5e-4, mass offset 3, n in {15,21,23,25,31}, L in {12,14,16,18,20,28}; audits the asserted AWAY-window table and arithmetic lambda=L/n wrap observations, not a closed-form recurrence law for arbitrary n,L.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-2026-05-11`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner enforces the AWAY-window sets below as explicit assert checks, and the observed windows are then expressed as finite-volume ratios lambda=L/n and delta=3/n.  _(class `C`)_
- **chain closes:** True — The cached runner computes and asserts the coherent, classical, and phase-kill AWAY-window sets used in the note. The lambda and delta columns are direct arithmetic from the asserted finite table, while the note explicitly withholds a universal recurrence law.
- **rationale:** The bounded finite-volume recurrence diagnostic closes from the runner-backed AWAY-window sets and arithmetic ratios. The note's qualitative wrap/recurrence reading is limited to clustering observations on the audited grid and explicitly states that no closed-form recurrence-scale law for arbitrary (n,L) is derived. Residual risk is only the out-of-scope predictive law, not the finite table.
- **auditor confidence:** high

### `circulant_parity_cp_tensor_narrow_theorem_note_2026-05-02`

- **Note:** [`CIRCULANT_PARITY_CP_TENSOR_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/CIRCULANT_PARITY_CP_TENSOR_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact 3x3 linear-algebra identities for the specified S, P_{23}, and K(d,c_even,c_odd), including the residual-Z_2 parity split and Im[(K_{01})^2]=2 c_even c_odd.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T015248Z-18603752-circulant_parity_cp_tens-01`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Using S_{01}=1 and (S^2)_{01}=0 gives K_{01}=c_even+i c_odd, hence Im[(K_{01})^2]=2 c_even c_odd; similarly P_{23}SP_{23}=S^2 gives the parity split.  _(class `A`)_
- **chain closes:** True — The claim closes from the explicit matrix definitions in the note. No cited authorities, external comparators, physical bridge premises, or hidden numerical inputs are needed.
- **rationale:** The proof is an exact algebraic calculation over explicitly defined 3x3 matrices. The runner source constructs S, P_{23}, K symbolically in SymPy and verifies the stated identities directly; it does not import helper modules or hard-code the contested result as an input. Although the runner labels its passes as class C, substantively these checks are class A algebraic identity checks, which are sufficient here because there are no upstream dependencies.
- **auditor confidence:** high

### `circulant_response_master_identity_narrow_theorem_note_2026-05-02`

- **Note:** [`CIRCULANT_RESPONSE_MASTER_IDENTITY_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/CIRCULANT_RESPONSE_MASTER_IDENTITY_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Standalone exact linear-algebra identity for the Hermitian-circulant family G(g_0,g_1) and cyclic basis B_0,B_1,B_2, including the global cone reduction and nonzero-domain kappa reformulation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-circulant_response_maste-023`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The direct trace computation gives r_0=3g_0, r_1=6 Re(g_1), r_2=6 Im(g_1), so substitution yields 2 r_0^2-(r_1^2+r_2^2)=18(g_0^2-2|g_1|^2).  _(class `A`)_
- **chain closes:** True — The trace identities for C and C^2 determine the three responses exactly, and the master identity follows by direct substitution. Since 18 is nonzero, the cone equation is equivalent to g_0^2=2|g_1|^2 globally, with kappa only defined when g_1 != 0.
- **rationale:** The claim is a self-contained algebraic identity over explicitly defined 3x3 matrices and scalar parameters. The runner source constructs the matrices and computes the responses symbolically with Sympy rather than importing a physical premise or external comparator. There are no cited dependencies, tuned numerical inputs, or parent-claim reductions needed for the narrow statement.
- **auditor confidence:** high

### `ckm_atlas_closure_formula_algebra_narrow_theorem_note_2026-05-10`

- **Note:** [`CKM_ATLAS_CLOSURE_FORMULA_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/CKM_ATLAS_CLOSURE_FORMULA_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `decoration`
- **claim_scope:** Audited only the scoped algebraic consequences (U1)-(U3), IS2 parametrically, IS1/IS3/IS4 at framework counts (2,3,6), and BM1/BM2 plus the framework Bernoulli table under the stated input identities and count constraints.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** _retained_pending_chain_  (reason: `decoration_waiting_on:ckm_atlas_axiom_closure_note`)
- **auditor:** `codex-audit-loop-019e14b5-5ad6-7860-9c7f-eceea18219de`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Given the parametric input identities, the count constraint, the imported off-diagonal magnitudes, and the row-sum tautologies, the three closure blocks (U), (IS), and (BM) are forced closed-form expressions by algebraic substitution.  _(class `A`)_
- **chain closes:** True — The symbolic and rational checks close the stated algebra: the disputed expressions are direct substitutions or framework-count specialisations of the hypotheses. No external physical bridge, alpha_s value, PDG comparator, or atlas authority is needed inside the narrowed scope.
- **rationale:** Issue: the packet proves real algebraic consequences of already-stated CKM atlas input identities, but it adds no independent observable, comparator, first-principles computation, or compression beyond the parent closure package. Why this blocks: under the Algebraic Decoration Policy, exact algebraic restatements with zero D-class checks should not stand as separate retained theorem rows even when the algebra is correct. Repair target: either box this under the CKM atlas closure/input-identity corollary inventory, or attach a new retained comparator/structural compression that is load-bearing outside the parent algebra. Claim boundary until fixed: valid as a scoped algebraic corollary, not as an independent retained theorem surface.
- **decoration parent:** `ckm_atlas_axiom_closure_note`
- **auditor confidence:** high

### `ckm_five_sixths_bridge_support_note`

- **Note:** [`CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md`](../../docs/CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The claimed numerical support for the assumed five-sixths CKM–mass bridge on the threshold-local mixed/self-scale comparator, including its one-loop transport and deviation decomposition.
- **audit_status:** ~~audited_numerical_match~~
- **effective_status:** ~~audited_numerical_match~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T164715Z-1ebf2b3d-00002-ckm_five_sixths_bridge_suppo`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** The assumed bridge |V_cb| = (m_s/m_b)^(5/6) is applied at alpha_s(v) = 0.103303816122 and judged by its +0.20% match to m_s(2 GeV)/m_b(m_b).  _(class `G`)_
- **chain closes:** False — The arithmetic closes after assuming the bridge and supplied numerical inputs, but neither the bridge nor the selection of the mixed-scale comparator is derived from the restricted packet.
- **rationale:** Issue: the runner assumes the contested five-sixths bridge by evaluating v_cb**(6/5), imports alpha_s(v) from a helper rooted in the hard-coded CANONICAL_PLAQUETTE = 0.5934, and uses mixed-scale PDG values as the close comparator. Why this blocks: it verifies algebra and a scale-dependent numerical coincidence rather than deriving the bridge or scale-selection rule from framework premises. Repair target: independently derive both the bridge and comparator-scale selection, then make the runner construct them without hard-coding the contested inputs. Claim boundary until fixed: the SU(3) identity, one-loop transport exponent, and conditional numerical decompositions are supported, but the claimed physical preference for the mixed/self-scale surface is not.
- **auditor confidence:** high

### `claude_complex_action_carryover_note`

- **Note:** [`CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE.md`](../../docs/CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A narrow exact ordered 3D lattice replay for one frozen instantaneous field family and one gamma sweep, checking gamma=0 reduction, Born cleanliness, and crossover behavior.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-040942-beec6e04-claude_complex_action_ca-001`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Exact-lattice replay at h = 0.5, W = 6, L = 30, s = 0.1, z_src = 3 gives gamma=0 reduction, machine-clean Born ratios, and a TOWARD->AWAY crossover between gamma=0.05 and 0.10.  _(class `C`)_
- **chain closes:** True — The provided runner source computes the lattice propagation, detector probabilities, centroids, Born I3 ratio, and gamma sweep from the specified lattice/action setup rather than printing hard-coded expected values. The exact Born ratios in the note are stale relative to the runner output, but the load-bearing qualitative claim of machine-clean Born behavior and the crossover interval is preserved.
- **rationale:** The runner performs an actual bounded numerical computation for the specified exact-lattice setup and produces the gamma=0 reduction, near-machine-zero Born ratios, and TOWARD-to-AWAY crossover. No cited upstream authority is required in the restricted packet, and the note explicitly avoids broader geometry-generic or continuum claims. The only caveat is that the note's Born-test numeric entries do not exactly match the current cached runner stdout, so those specific frozen values should be refreshed even though the audited narrow conclusion still follows.
- **auditor confidence:** medium

### `claude_complex_action_grown_companion_note`

- **Note:** [`CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md`](../../docs/CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Runner-defined grown row only: drift=0.2, restore=0.7, seeds 0 and 1, with the listed gamma sweep and no geometry-generic, continuum, or self-gravity extension.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260511-224519-a7679e61-claude_complex_action_gr-009`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The live runner computes the retained grown-row replay at drift=0.2, restore=0.7, seeds 0 and 1, preserving exact gamma=0 reduction, machine-clean Born proxy, F~M=1.000, and a gamma crossover from TOWARD to AWAY.  _(class `C`)_
- **chain closes:** True — The runner source performs an actual amplitude propagation, detector probability, centroid, Born-proxy, weak-source scaling, and gamma sweep computation rather than printing constants. Within the explicitly bounded runner-defined row, the stdout reproduces the note's load-bearing numerical claims up to the stated machine-precision Born-proxy variation.
- **rationale:** The claim is narrow enough to match the evidence: it asserts only survival on the runner-defined grown row at fixed drift, restore, and seeds. The runner code computes the reported quantities from generated geometry and propagation rules, and the completed runner output supports exact gamma=0 reduction, machine-clean Born proxy, weak-field F~M near 1, and the TOWARD-to-AWAY crossover. No external comparator, cross-note input, or definitional renaming is load-bearing for the scoped conclusion.
- **auditor confidence:** medium

### `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19`

- **Note:** [`CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md`](../../docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Finite connected spatial Lambda with fixed tau>0 and beta>0, pure-Wilson SU(3) heat-kernel transfer operator T_W on L2(SU(3)^E, dU_Haar) only: simple dominant eigenvalue and strict finite-volume transfer gap Delta_T(Lambda)>0. No T_full/Leg A, thermodynamic limit, continuum limit, uniform-in-Lambda bound, Yang-Mills mass gap, or spatial-clustering claim is ratified.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-five-judge-panel-majority-20260529-cluster-delta-t-finite-lambda`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** K_tau is strictly positive and smooth on connected compact SU(3); hence T_W has a real symmetric smooth strictly positive kernel on compact Conf(Lambda)^2, is compact/trace-class and positivity-improving, and Perron-Jentzsch/Krein-Rutman gives a simple positive spectral radius with all other spectral values strictly below it in modulus.  _(class `A`)_
- **chain closes:** True — The five-judge panel unanimously sided with the second audit. The pure-Wilson finite-Lambda core closes by standard heat-kernel positivity and compact positive-operator theory: on compact SU(3)^E, heat-kernel positivity plus the positive Wilson factor gives a strictly positive smooth kernel; compactness/trace-class and positivity improvement let Perron-Jentzsch/Krein-Rutman produce a simple top eigenvalue and strict finite-volume spectral separation. The finite-Lambda, fixed-parameter, no-thermodynamic-limit, no-continuum, no-Yang-Mills, and no-spatial-clustering clauses are scope boundaries, not live admissions. Leg A appears only in the conditional T_full extension and is excluded from the ratified scope; runner PASS=8 supports the analytic checks but sampled Leg A/T_full checks are not load-bearing.
- **rationale:** The five-judge panel unanimously sided with the second audit. The pure-Wilson finite-Lambda core closes by standard heat-kernel positivity and compact positive-operator theory: on compact SU(3)^E, heat-kernel positivity plus the positive Wilson factor gives a strictly positive smooth kernel; compactness/trace-class and positivity improvement let Perron-Jentzsch/Krein-Rutman produce a simple top eigenvalue and strict finite-volume spectral separation. The finite-Lambda, fixed-parameter, no-thermodynamic-limit, no-continuum, no-Yang-Mills, and no-spatial-clustering clauses are scope boundaries, not live admissions. Leg A appears only in the conditional T_full extension and is excluded from the ratified scope; runner PASS=8 supports the analytic checks but sampled Leg A/T_full checks are not load-bearing.
- **auditor confidence:** high

### `cluster_decomposition_delta_x_finite_lambda_axis_permutation_narrow_note_2026-06-02`

- **Note:** [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md`](../../docs/CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md)
- **claim_type:** `decoration`
- **claim_scope:** Finite-Lambda pure-Wilson spatial-axis transfer-operator gap, audited only as an axis-permutation decoration under the retained finite-Lambda temporal-axis T_W gap theorem; no thermodynamic-limit, Yang-Mills mass-gap, fermion-factor, or downstream bridge-lift claim.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-20260603-020712-ca523a15-cluster_decomposition_de`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Relabeling the transfer coordinate as x_mu for any mu in {1,2,3} carries every load-bearing temporal-axis step through without modification on the finite Wilson kernel surface.  _(class `A`)_
- **chain closes:** True — The one-hop upstream temporal-axis parent is marked retained, and the source note's load-bearing move only permutes finite product SU(3) link labels in the same Wilson heat-kernel construction. Within that narrowed finite-Lambda pure-Wilson scope, no additional open upstream premise is required.
- **rationale:** The claimed spatial gap is not an independent first-principles computation; the SU(3) heat-kernel positivity, trace-class property, and Perron-Jentzsch gap are all imported from the retained temporal-axis parent. The new step is a finite-kernel axis-label permutation, which is a class-A algebraic decoration of that parent under the note's own pure-Wilson definitions. The runner reports 18 passes, but its sampled positivity check uses an approximate character surrogate, so the runner should be treated as non-load-bearing sanity support rather than a class-C proof.
- **decoration parent:** `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19`
- **auditor confidence:** medium

### `commensuration_general_lemma_period_parity_bounded_theorem_note_2026-06-12`

- **Note:** [`COMMENSURATION_GENERAL_LEMMA_PERIOD_PARITY_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/COMMENSURATION_GENERAL_LEMMA_PERIOD_PARITY_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `decoration`
- **claim_scope:** For the specified d=3 step-2 chart family with K-periods (L/2, L, L/2), the minimal-vector d^2 mod 2 parity correspondence holds for even L >= 8 exactly when L = 0 mod 4; the Hamiltonian tie is audited only at L=8 and L=10.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_d3_truncation_commensuration_criterion_bounded_theorem_note_2026-06-12`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T015154Z-1f0c3329-00388-commensuration_general_lemma`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** If a period is even, replacing a residue difference by its minimal representative does not change parity; if it is odd, wrapping flips parity, so correspondence holds exactly when all periods (L/2, L, L/2) are even, equivalently L = 0 mod 4.  _(class `A`)_
- **chain closes:** False — The residue-parity conclusion follows algebraically on the supplied chart family, but it is not an independent physics closure: it is a standard mod-2 consequence of the single retained-bounded commensuration parent. The broader Hamiltonian equivalence is not established beyond the two stated anchors.
- **rationale:** The load-bearing argument is elementary residue-class parity algebra applied to the chart periods supplied by one retained-bounded parent. The runner genuinely computes the symbolic case split and finite combinatorial correspondence, while its frozen L=8 and L=10 values serve only as parent-anchor checks. With no external comparator and no new framework-level physics derivation, the result is algebraic decoration of the upstream commensuration criterion.
- **decoration parent:** `d3_truncation_commensuration_criterion_bounded_theorem_note_2026-06-12`
- **auditor confidence:** high

### `commensuration_unconditional_period_parity_lemma_narrow_theorem_note_2026-06-12`

- **Note:** [`COMMENSURATION_UNCONDITIONAL_PERIOD_PARITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md`](../../docs/COMMENSURATION_UNCONDITIONAL_PERIOD_PARITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Under the centered minimal_delta convention for chart periods q_i >= 2, d^2 mod 2 agrees with chart parity for all 3D chart cosets iff all q_i are even; for (L/2,L,L/2) with even L and periods >= 2 this is L = 0 mod 4.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-023644-3b04cce6-commensuration_unconditional_period_parity_lemma_narrow_theorem_note_2026-06-12-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Since delta_i^2 = delta_i mod 2, d^2 = sum_i delta_i mod 2, so chart parity sum_i a_i is preserved for all cosets iff every q_i is even, with an odd-period witness a_i=(q_i+1)/2.  _(class `A`)_
- **chain closes:** True — The congruence delta_i-a_i=-q_i k_i makes every even-q_i axis parity-preserving, while every odd q_i >= 3 has the stated residue with k_i=1 and hence a parity flip. Summing axes is valid because n^2 is congruent to n modulo 2.
- **rationale:** The load-bearing step is exact modular arithmetic under the stated centered representative convention. The runner source performs actual residue, symbolic, numeric sweep, and selected full-coset checks rather than merely printing pass counts, although several regression targets are frozen as expected values. No cited dependency, physical bridge, comparator value, or tuned numerical input is needed for this narrow theorem.
- **auditor confidence:** high

### `connes_kreimer_birkhoff_factorization_external_narrow_theorem_note_2026-05-10`

- **Note:** [`CONNES_KREIMER_BIRKHOFF_FACTORIZATION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/CONNES_KREIMER_BIRKHOFF_FACTORIZATION_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** External mathematical theorem: characters of the Connes-Kreimer rooted-tree Hopf algebra with values in a commutative unital Rota-Baxter target algebra admit the stated recursive convolution Birkhoff factorization; no CL3/framework or physics bridge is audited or claimed.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e143a-7f81-7030-8a69-e52ecd10b000`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** For every non-empty tree t, prepared_phi(t) = phi(t) + sum_c phi_-(P^c(t)) phi(R^c(t)), phi_-(t) = -T(prepared_phi(t)), and phi_+(t) = (id - T)(prepared_phi(t)), giving unique characters with phi = phi_-^{*-1} * phi_+.  _(class `A`)_
- **chain closes:** True — The cited Connes-Kreimer authority excerpt contains the same recursive counterterm formula C(X) = -T(U(X) + sum C(X')U(X'')), the Rota-Baxter identity used to prove multiplicativity, and the convolution relation R = C * U giving the Birkhoff decomposition. The note's boundary explicitly confines the claim to this external Hopf-algebra theorem and excludes project-framework and physics uses.
- **rationale:** The source note cleanly states the external theorem and does not import or assert any CL3 operator, perturbation expansion, hierarchy closure, numerical prediction, or physics bridge. The runner is not a proof of the theorem, but it appropriately spot-checks the coproduct, convolution, Rota-Baxter identity, low-depth recursion, unit identities, and no-framework boundary. Given the narrow theorem scope and cited external theorem, the chain closes without requiring a new framework bridge.
- **auditor confidence:** high

### `continuum_limit_note`

- **Note:** [`CONTINUUM_LIMIT_NOTE.md`](../../docs/CONTINUUM_LIMIT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-h cached h^2+T lattice trend table for h in {1.0, 0.5, 0.25, 0.125}, including transfer norms, TOWARD gravity rows, F~M exponents near 1, and 2.7% weak-field deflection change from h=0.25 to h=0.125; no audited h -> 0 convergence theorem.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T181334Z-742480ea-continuum_limit_note-01`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The binding evidence of this note is exactly the finite-h trend table on the cached size sweep h in {1.0, 0.5, 0.25, 0.125}, including the 2.7% weak-field deflection change between h=0.25 and h=0.125 and the F~M exponent table bracketing 1.000.  _(class `C`)_
- **chain closes:** True — The narrowed finite-h claim follows from the completed cached runner output, and the runner source genuinely computes the reported lattice propagation quantities rather than printing constants or importing a contested premise. The strict h -> 0 continuum-limit statement is explicitly excluded from the audited scope.
- **rationale:** The source note narrows the binding claim to a finite-resolution numerical trend, and the cached output matches the displayed h values, transfer norms, weak-field deflections, and F~M values. The runner source constructs offsets, fields, propagates amplitudes, computes centroids, Born ratios, and mass-scaling fits directly with fixed parameters; it does not hard-code the contested table. Because the h -> 0 convergence language is demoted to diagnostic-only, the missing convergence theorem does not block this bounded finite-h audit.
- **auditor confidence:** high

### `critical_exponents_topology_live_scout_note_2026-06-04`

- **Note:** [`CRITICAL_EXPONENTS_TOPOLOGY_LIVE_SCOUT_NOTE_2026-06-04.md`](../../docs/CRITICAL_EXPONENTS_TOPOLOGY_LIVE_SCOUT_NOTE_2026-06-04.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded finite-size scout over six configured graph representatives, auditing only the reported admissible fits, degenerate rows, R^2 threshold, finite saturation readouts, and beta-spread statement, with no asymptotic universality or multi-seed robustness claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260605-201830-d6981135ff-critical_exponents_topology_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** In this finite configured scout, three graph representatives have admissible onset fits with fitted beta values 0.7328, 0.3675, and 0.3348, while three representatives are degenerate; the fitted beta spread is evidence that topology affects this finite-size onset diagnostic.  _(class `C`)_
- **chain closes:** True — The runner source constructs the six graph representatives, evolves the stated finite diagnostic, fits onset curves from computed arrays, labels rows by finite R^2 criteria, and checks the reported bounded assertions. Independently from the runner assertions, the displayed fit betas have spread 0.7328 - 0.3348 = 0.3980, exceeding 0.35, and the three degenerate rows show non-finite beta and R^2 as claimed.
- **rationale:** The restricted packet contains the source note, cached output, and full primary runner source, with no missing helper imports or cited upstream dependencies. The code is not a trivial printout: it builds graph families, solves the finite evolution and field equations, performs curve fits, and computes the table values before checking the bounded assertion surface. The hard-coded expected label sets are used as regression assertions against computed rows, not as the source of the fitted beta values. The audited conclusion is limited to topology-dependent finite-size onset behavior in this configured scout, so it closes without importing an asymptotic exponent, universality class, or external comparator.
- **auditor confidence:** high

### `critical_exponents_topology_note_2026-04-10`

- **Note:** [`CRITICAL_EXPONENTS_TOPOLOGY_NOTE_2026-04-10.md`](../../docs/CRITICAL_EXPONENTS_TOPOLOGY_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-size scout over the six configured graph families in scripts/frontier_critical_exponents.py, limited to the displayed fitted/degenerate labels, beta spread, R^2 thresholds, and finite saturation readouts.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-124229-7733b4f72b-critical_exponents_topology_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Three nondegenerate fitted rows have different beta values, and three configured rows are degenerate under the runner's criteria.  _(class `C`)_
- **chain closes:** True — The supplied runner source computes the six graph instances, finite evolution, fitted beta/R^2 values, and row labels rather than importing them from another note. The displayed table predicates also check directly from the packet values, including beta spread 0.7328 - 0.3348 = 0.3980 > 0.35.
- **rationale:** The claim is correctly bounded to the finite runner scout and expressly disclaims universality-class, asymptotic exponent, continuum-limit, and retained-status conclusions. The runner is not a constant-printing script: it builds the graph families, performs the sparse finite evolution, fits the post-critical order proxy, and then asserts finite predicates matching the note and cache. The quantitative inventory in the restricted packet is internally consistent: six rows, three finite fits with R^2 >= 0.90, three degenerate rows with nonfinite beta/R^2, finite phi_sat values, and beta spread above 0.35. No cited authority or external comparator is needed for this scoped finite-computation claim.
- **auditor confidence:** high

### `cross_family_universality_note`

- **Note:** [`CROSS_FAMILY_UNIVERSALITY_NOTE.md`](../../docs/CROSS_FAMILY_UNIVERSALITY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Dispersion-only finite-runner consistency at H=0.5 across the three specified grown-DAG parameter families, using five seeds per family and seed-mean omega(p) fits.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260518-120032-569b3ebd-cross_family_universalit-034`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At H=0.5, the dispersion runner computes seed-mean omega(p) for Fam1/Fam2/Fam3 and finds Schrödinger/KG R² gaps below 0.01 with m_eff values 5.98, 5.90, and 5.88.  _(class `C`)_
- **chain closes:** True — The provided runner source constructs each grown DAG from the stated family parameters, propagates plane waves, measures omega(p), fits the seed-mean dispersion curves, and prints the claimed R² gaps and m_eff values. This closes only the narrowed dispersion finite-runner claim, not the non-load-bearing lensing or fine-H universality language.
- **rationale:** The live runner output matches the narrowed dispersion claims: all three families have Δ(Schrödinger-KG) below 0.01 and seed-mean effective masses within the stated 1.7% spread. The runner source performs an actual simulation and fit from fixed generator parameters and seeds, with no helper imports or hard-coded expected output values. The clean verdict is limited to the finite H=0.5 dispersion-runner result; the note's older lensing and broader universality wording is explicitly non-load-bearing or out of scope.
- **auditor confidence:** high

### `cubic_coxeter_regge_deficit_vanishing_narrow_theorem_note_2026-05-10`

- **Note:** [`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The flat Euclidean six-tetrahedra Coxeter triangulation of Z^3 has zero Regge deficit on axis, face-diagonal, and body-diagonal interior edges, with the six tetrahedra partitioning each cube.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260522-030935-7e12d739-cubic_coxeter_regge_defi-005`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Summing dihedral contributions across all tetrahedra in T(Z^3) containing a given interior edge gives sum_{T containing e} alpha_T(e) = 2*pi for every axis, face-diagonal, and body-diagonal edge.  _(class `A`)_
- **chain closes:** True — The source note derives the canonical tetrahedron dihedral table and then checks the finite edge-star sums for the three edge classes. The corrected axis-edge enumeration is explicit enough, and the runner source performs genuine symbolic/numerical Euclidean geometry rather than importing a contested premise.
- **rationale:** This is a standalone Euclidean algebra claim over the stipulated flat Coxeter triangulation, with no cited upstream authorities or physical bridge imports. The runner computes volumes, dihedral angles, and representative edge-star sums directly from vertex coordinates using sympy/numpy; it is not merely printing constants or reading another note. The repaired axis-edge proof replaces the earlier uniform-incidence shortcut with the correct finite-star accounting, preserving the zero-deficit conclusion.
- **auditor confidence:** high

### `cycle_battery_note_2026-04-10`

- **Note:** [`CYCLE_BATTERY_NOTE_2026-04-10.md`](../../docs/CYCLE_BATTERY_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-current-ca82-fresh`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The staggered fermion plus parity-coupled potential-gravity architecture passes the 9-row cycle battery on the random-geometric, growing, and layered-cycle bipartite graph families, with the listed caveats.  _(class `C`)_
- **chain closes:** True — For the bounded claim actually stated, the runner constructs the three graph families and verifies the reported source, force-proxy, norm, gauge, and gap-characterization rows. The note explicitly limits the force rows to shell-radial proxies and does not claim exact lattice-coordinate gravitational direction.
- **rationale:** The runner output matches the note: all three families score 9/9, and the note carries the necessary caveats about shell-force proxies, two-sign nonselectivity, and graph-dependent force scale. Residual risk is that this remains a bounded harness result rather than a physical attraction theorem, but that boundary is stated in the source note.
- **auditor confidence:** medium

### `cycle_battery_scaled_note_2026-04-10`

- **Note:** [`CYCLE_BATTERY_SCALED_NOTE_2026-04-10.md`](../../docs/CYCLE_BATTERY_SCALED_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The larger-size sibling harness for the retained cycle-bearing graph battery passes the inherited B1-B9 checks for random geometric, growing, and layered cycle graph families through side 12, with force treated as the primary observable and B9 as characterization only.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-mcclintock-3rd-019debc0-eab9-7e42-85c9-8da3000a319d`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The scaled runner reports that all nine family/size cases, spanning random geometric, growing, and layered cycle graphs at side 8, 10, and 12, score 9/9 under the inherited cycle-battery protocol.  _(class `C`)_
- **chain closes:** True — The one-hop dependency is now retained_bounded and supplies the row semantics and caveats. The provided scaled runner output directly covers the larger side sweep without invoking an external comparator, a hidden physical identification, or a new semantic standard.
- **rationale:** The scoped bounded claim closes as a retained scaled computation: the base battery semantics are clean, and the scaled runner output reports 9/9 scores for all nine family/size cases. The clean verdict is limited to the stated battery protocol and inherits the base-note caveats: irregular-graph force is a shell-radial proxy, two-sign behavior narrows sign interpretation, and B9 is characterization rather than a gate. This does not establish a full gravity-selection theorem or exact lattice-coordinate force result.
- **auditor confidence:** medium

### `cycle_break_frontier_note_2026-04-10`

- **Note:** [`CYCLE_BREAK_FRONTIER_NOTE_2026-04-10.md`](../../docs/CYCLE_BREAK_FRONTIER_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded computational frontier claim: within the stated staggered cycle-battery runner protocol and inherited battery caveats, raw size through side 18 does not break the retained rows on the three tested families, while random_geometric side=18 extra=5 is the first reported dense-shortcut gauge/current-collapse boundary among the tested cases.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-leibniz-3rd-019debcd-ae93-78c0-b737-02a5e9d58cb0`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The runner computes the larger retained sweep and dense-shortcut boundary, finding all side 14/16/18 family rows at 9/9 except random_geometric side=18 extra=5, which drops to 8/9 with gauge FAIL and J_span below threshold.  _(class `C`)_
- **chain closes:** True — The one-hop dependencies are now retained_bounded and the provided runner output directly supplies the larger sweep rows and dense-shortcut failure boundary. The closure is bounded to the stated graph families, sides, shortcut parameters, and inherited shell-radial force proxy interpretation.
- **rationale:** The scoped bounded claim closes from the supplied note, retained one-hop dependencies, and primary runner output: the larger sweep rows pass, and the named random_geometric side=18 extra=5 boundary is reproduced as 8/9 with native gauge failure and collapsed J_span. This is not promoted beyond the tested protocol: irregular-graph force remains a shell-radial proxy, two-sign behavior limits sign interpretation, and B9 remains characterization only. No external comparator, renaming identity, hidden physical identification, or tuned numerical match is needed for the bounded frontier statement.
- **auditor confidence:** medium

### `cycle_break_slice_note_2026-04-10`

- **Note:** [`CYCLE_BREAK_SLICE_NOTE_2026-04-10.md`](../../docs/CYCLE_BREAK_SLICE_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-bottomup-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The matched frontier slice around the first larger-graph cycle-battery break records the stated finite replay boundary.  _(class `C`)_
- **chain closes:** True — Yes. The registered runner completed successfully and checks the finite slice described by the source note.
- **rationale:** The clean content is the finite cycle-break slice, not a universal repair. The runner completed successfully and the classified check surface is {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'total_pass': 0}. Residual risk is generalization outside the matched slice.
- **auditor confidence:** medium

### `cyclic_dft_uniform_magnitude_bounded_note_2026-05-26`

- **Note:** [`CYCLIC_DFT_UNIFORM_MAGNITUDE_BOUNDED_NOTE_2026-05-26.md`](../../docs/CYCLIC_DFT_UNIFORM_MAGNITUDE_BOUNDED_NOTE_2026-05-26.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite cyclic-character algebra theorem: for the normalized DFT/character table of Z_N, with N a positive cyclic-group order, every entry F_N[j,k]=exp(2*pi*i*j*k/N)/sqrt(N) has magnitude-squared 1/N; in particular all Z_3 entry overlap magnitudes are 1/3. PMNS/residual-symmetry, dynamics-lane, K-theory, empirical, and framework-bridge interpretations are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-gpt-5.5-xhigh-2026-05-28-cyclic-dft-uniform-magnitude`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Each omega_N^(j k) is a unit complex number, so |omega_N^(j k)/sqrt(N)|^2 = 1/N for every j,k.  _(class `A`)_
- **chain closes:** True — The independent check is the exact modulus identity |exp(i theta)|=1 combined with the normalized 1/sqrt(N) factor, giving |F_N[j,k]|^2=1/N for all indices. Character orthogonality is the standard finite cyclic character-table form and no physical identification is used.
- **rationale:** The row closes as a bounded finite-group algebra statement. The source's proof uses only the unit modulus of cyclic characters and the normalized DFT factor, and the runner corroborates sampled N values plus all Z_3 entries with PASS=19 FAIL=0. Residual risk is downstream overuse: this verdict does not identify any PMNS column, residual symmetry, K-theory object, dynamics invariant, or framework carrier with the cyclic DFT table.
- **auditor confidence:** high

### `cyclic_projector_compression_narrow_theorem_note_2026-05-02`

- **Note:** [`CYCLIC_PROJECTOR_COMPRESSION_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/CYCLIC_PROJECTOR_COMPRESSION_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Standalone exact linear-algebra / Z_3 representation-theory identity on Herm(3), limited to the cyclic projector, its invariant basis, basis-level action, and generic Hermitian compression formula; no physical Koide, DM-neutrino, charged-lepton source-response, numerical, fitted, or unit-convention claims are included.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-cyclic-projector-compression-auditor`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** Exact cyclic-group averaging over the explicitly defined 3-cycle C is self-adjoint and idempotent under the Frobenius inner product, so it projects Herm(3) onto the C-fixed subspace; direct exact basis enumeration identifies that subspace as span_R{I, C+C^2, i(C-C^2)} and gives the stated coefficient formula.  _(class `A`)_
- **chain closes:** True — The theorem closes from the explicit definition of C and P_cyc plus exact finite-dimensional algebra. The parent-row context line is not load-bearing: the row has no dependencies, defines C directly, and the asserted conclusions are independently checkable symbolic identities.
- **rationale:** The source note is narrowly scoped and the exact runner output reports 26 algebraic checks with no failures, covering the group facts, Hermiticity, idempotence and fixed basis, basis action, and generic compression formula. The generated classifier's decoration-candidate signal arises from the parent-row context check rather than from the theorem's proof obligations, so it does not convert this independent helper theorem into decoration. Residual risk is downstream misuse: later rows must not treat B0/B1/B2 as physical response channels without a separate audited bridge.
- **auditor confidence:** high

### `d2_orbital_susceptibility_sign_regions_bounded_theorem_note_2026-06-12`

- **Note:** [`D2_ORBITAL_SUSCEPTIBILITY_SIGN_REGIONS_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D2_ORBITAL_SUSCEPTIBILITY_SIGN_REGIONS_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite sampled-grid statement for the free staggered square-lattice model: m∈{0.2,0.5}, T∈{0.2,0.4}, μ_ch∈{0.0,0.5,1.0,1.5,2.0}, rational fluxes q∈{16,24,32}, exact Harper spectra, and Gauss-Legendre quadrature; no continuum, unsampled-interval, or continuum-QFT claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260613-014443-a1bd84b022-d2_orbital_susceptibility_si`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The plaquette-field susceptibility χ(q)=2[Ω(B_q)-Ω(0)]/B_q² with B_q=2π/q, q∈{16,24,32}, Richardson-extrapolates to negative χ on the sampled μ_ch grid {0.0,0.5,1.0,1.5} and positive χ at μ_ch=2.0 for both sampled masses and temperatures.  _(class `C`)_
- **chain closes:** True — The runner source constructs the Harper Hamiltonian, the independent folded B=0 spectrum, the grand-potential integral, χ normalization, and the B² Richardson extrapolation directly rather than importing or hard-coding the asserted signs. The audited conclusion follows for the sampled grid only.
- **rationale:** The load-bearing signs are produced by first-principles spectral computation inside the runner, not by a numerical table copied from the note or another authority. The formula inventory checks out on the restricted packet: χ=2ΔΩ/B² is the Ω″ normalization, the q=24,32 Richardson formula cancels a leading B² error term, and the B=0/gauge-origin controls test the relevant normalizations. All asserted sampled signs are resolved with margins far above the stated eps floors, and there are no cited non-retained dependencies or external comparator inputs. The clean verdict is limited to the bounded sampled-grid claim.
- **auditor confidence:** high

### `d2_sign_boundary_bisection_between_landmarks_bounded_theorem_note_2026-06-12`

- **Note:** [`D2_SIGN_BOUNDARY_BISECTION_BETWEEN_LANDMARKS_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D2_SIGN_BOUNDARY_BISECTION_BETWEEN_LANDMARKS_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Sampled finite-q sign-boundary roots at q=24 for (m,T)=(0.2,0.2),(0.5,0.2),(0.2,0.4), with quadrature doubling gates, q=32 size probes, fixed ordering checks, and strict between-landmarks inequalities; no continuum or landmark-identification claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260614-012405-67fb9fe741-d2_sign_boundary_bisection_b`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The finite-Harper flux-response curvature sign-change boundary is bisection-located to 1e-3 at the three sampled (m,T) instances, with q=32 size probes and each sampled mu* strictly between |m| and sqrt(m^2+16).  _(class `C`)_
- **chain closes:** True — The runner constructs the finite Harper matrices and zero-field spectra, computes chi from the spectra, and uses sign-preserving bisection rather than importing the displayed roots. Independent arithmetic confirms the bisection widths imply <=1e-3 midpoint localization, the two stated monotone orderings hold, and all three roots lie strictly between |m| and sqrt(m^2+16).
- **rationale:** The load-bearing step is a first-principles finite numerical computation from the stated lattice operator, not a renaming, comparator match, or cross-note value import. The sole cited authority is retained_bounded, and the present note keeps the conclusion bounded to sampled finite-field instances. The explicit open landmark-identification language is not used as a premise for a stronger identification; the audited claim is only strict between-ness and non-anchoring at the sampled points.
- **auditor confidence:** high

### `d2_sign_boundary_mass_collapse_bounded_theorem_note_2026-06-12`

- **Note:** [`D2_SIGN_BOUNDARY_MASS_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D2_SIGN_BOUNDARY_MASS_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Sampled finite-lattice d=2 staggered square-lattice sign-boundary collapse at q=24, GL=160 for T=0.2 and m in {0.2,0.35,0.5,0.8}, with m=0, T-direction, quadrature, endpoint-recompute, and q=32 spot controls; no continuum or interpretive epsilon-curve claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260614-022404-9a85a98de5-d2_sign_boundary_mass_collap`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Bisection-located boundaries at T=0.2 across m in {0.2, 0.35, 0.5, 0.8} give eps*_m = sqrt(mu*^2 - m^2) with relative spread 1.45% < 2%, with the monotone residual m-trend separately disclosed.  _(class `C`)_
- **chain closes:** True — The runner constructs the Harper matrices, spectra, grand potentials, chi values, sign brackets, bisection roots, eps values, and spread directly rather than importing the contested numbers. Independent arithmetic from the reported roots verifies eps=sqrt(mu*^2-m^2), mean_eps=1.681175930933, relative_spread=0.0144923716, and the m=0 anchor relative deviation, while the upstream open landmark/interpretive questions are outside this scoped claim.
- **rationale:** The load-bearing step is a first-principles finite numerical computation in the runner, not a definition, renaming, external comparator, or numerical match to an imported calibrated value. The runner source contains no hard-coded expected collapse values and no helper imports; it computes the spectra and gates the brackets, spread, monotone trend, quadrature doubling, endpoint recomputation, and q=32 spot probe. Both cited authorities are retained_bounded, and the claim stays within sampled bounded scope rather than using their named open identifications.
- **auditor confidence:** high

### `d2_sign_boundary_tracks_landau_peierls_bounded_theorem_note_2026-06-12`

- **Note:** [`D2_SIGN_BOUNDARY_TRACKS_LANDAU_PEIERLS_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D2_SIGN_BOUNDARY_TRACKS_LANDAU_PEIERLS_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** m=0 square-lattice tight-binding model at T=0.2, 0.3, 0.4; finite-field boundary at B=2*pi/24 compared with the B -> 0 Landau-Peierls curvature-determinant root within tolerance 2e-2.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260614-022638-2a153bc5ec-d2_sign_boundary_tracks_land`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The full finite-field sign boundary eps*(T) and the Landau-Peierls curvature-determinant sign-change root mu_LP(T) agree within 2e-2 at each sampled T in {0.2, 0.3, 0.4}.  _(class `C`)_
- **chain closes:** True — The runner constructs the q=24 Harper finite-field spectrum, the zero-field square-band spectrum, and the LP curvature-determinant integrand directly, then independently brackets and bisects the two sign roots. The reported deviations are all below 2e-2, and the displayed square-band Hessian determinant and Fermi-slope sign conventions check internally.
- **rationale:** The load-bearing numerical agreement is produced by an actual spectral/quadrature computation rather than by hard-coded target roots or a cross-note import. The source note's displayed identities are consistent: for eps=-2t(cos kx+cos ky), eps_xx eps_yy - eps_xy^2 = 4t^2 cos kx cos ky, and f'(0,T) has the stated negative sign. The clean verdict is bounded to the disclosed sampled temperatures and finite B=2*pi/24 comparison; it does not establish a continuum-B or all-temperature theorem.
- **auditor confidence:** high

### `d2_truncated_flow_frozen_ratio_accumulated_budget_bounded_theorem_note_2026-06-12`

- **Note:** [`D2_TRUNCATED_FLOW_FROZEN_RATIO_ACCUMULATED_BUDGET_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D2_TRUNCATED_FLOW_FROZEN_RATIO_ACCUMULATED_BUDGET_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite d=2, E=0 free-quadratic checkerboard Schur trajectory at L=16 with d2={4,8} truncation for four steps, together with the stated L=12/L=16 retained-block resolvent-budget stability probe.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00406-d2_truncated_flow_frozen_rat`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** For the specified finite truncated trajectory, the post-step-2 kept/drop block has H_kd = 0, so subsequent Schur steps leave the retained diagonal and d2=4 coupling invariant.  _(class `C`)_
- **chain closes:** True — The runner constructs the finite lattice matrices, performs the Schur complements and shell truncations, and directly computes the closure, error ordering, resolvent budgets, stability ratio, and identity control. Once the computed H_kd block vanishes, invariance under the following Schur step follows algebraically.
- **rationale:** The runner is not a print-only or target-matching certificate: it explicitly builds the operator and computes the claimed finite-matrix quantities without importing a contested result or external comparator. The hard-coded 3.21e-2 ceiling and 1% stability tolerance are openly labeled regression criteria, while the measured values tested against them are computed at runtime. The verdict is restricted to the stated finite trajectory and probe; it does not establish a validated RG flow, an all-L limit, or a continuum fixed point.
- **auditor confidence:** high

### `d3_checkerboard_step1_closed_form_parity_lemma_bounded_theorem_note_2026-06-12`

- **Note:** [`D3_CHECKERBOARD_STEP1_CLOSED_FORM_PARITY_LEMMA_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D3_CHECKERBOARD_STEP1_CLOSED_FORM_PARITY_LEMMA_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The supplied free one-orbital nearest-neighbor scalar Hamiltonian on periodic simple-cubic Z³ lattices L ∈ {6,8}, audited for its step-1 parity Schur complement at E=0, one E=0.3 covariance probe, retained-site resolvent equality, and the stated integer parity lemma.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00388-d3_checkerboard_step1_closed`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Because the odd-parity block is h_oo = μI, its exact Schur complement is determined by two-step path counts: 6 on-site, 2 at face diagonals, 1 at axial d²=4, and 0 beyond those shells.  _(class `C`)_
- **chain closes:** True — The accepted Lattice axiom supplies cubic Z³ nearest-neighbor adjacency, while the bounded note supplies the free scalar Hamiltonian under study. Direct construction and two-step path counting yield the stated signed coefficients and support, and the parity and resolvent statements follow algebraically.
- **rationale:** The runner genuinely constructs the finite cubic Hamiltonians, forms their parity blocks and Schur complements, and computes path counts and resolvents rather than merely printing expected results. Its independently generated matrices confirm the signed shell coefficients, absence of farther step-1 couplings, wraparound stability, energy shift, and resolvent identity. The elementary parity identity establishes the checkerboard preservation statement within the explicitly bounded scope; no external comparator or non-accepted authority is used.
- **auditor confidence:** high

### `d3_staggered_two_band_orbital_bounded_theorem_note_2026-06-13`

- **Note:** [`D3_STAGGERED_TWO_BAND_ORBITAL_BOUNDED_THEOREM_NOTE_2026-06-13.md`](../../docs/D3_STAGGERED_TWO_BAND_ORBITAL_BOUNDED_THEOREM_NOTE_2026-06-13.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite free cubic two-band model at L=8, mu=0.4, T=1.0, m in {0,0.3,0.6}, using the quantized finite-torus Peierls reference and fixed 1/L^2 magnetic-area normalization, with only the sampled sign table over mu in {0,0.4,1.0,2.0}.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-d3_staggered_two_band_orbital_bounded_theorem_note_2026-06-13-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** With the fixed magnetic-area normalization `1/L^2`, the full `chi_intra + chi_inter` split tracks the exact finite-torus reference to the frozen `12%` relative gate on the mass grid.  _(class `C`)_
- **chain closes:** True — The runner constructs the stated finite Hamiltonian, verifies the B=0 Bloch spectrum, diagonalizes the Peierls torus reference, computes the B=0 perturbative split, and cross-checks the perturbative curvature by an independent finite-difference limit. No cited upstream authority or calibrated external value is imported, and the conclusion is explicitly bounded to the tested finite-cell regime.
- **rationale:** The load-bearing step is a first-principles finite-lattice computation from the stated Hamiltonian and normalization, not a definition substitution or numerical match to an imported target. The runner source does not merely print expected constants; it computes spectra, curvature, LP-only failure, interband cancellation, residual size, and sampled sign tracking, with all 20 gates passing. The note avoids thermodynamic-limit overclaim by naming the finite-cell/finite-flux residual and reporting the lack of L convergence at L <= 8.
- **auditor confidence:** high

### `d3_step2_range_growth_period_class_dichotomy_bounded_theorem_note_2026-06-12`

- **Note:** [`D3_STEP2_RANGE_GROWTH_PERIOD_CLASS_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D3_STEP2_RANGE_GROWTH_PERIOD_CLASS_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** d=3 free E=0 finite periodic boxes L=8,10,12,14 with t=1, mu=5: step-2 shell range growth, L=12/14 near-shell convergence, L=8 box limitation, and even-d2 truncation behavior of the next-checkerboard block.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260614-013317-bbdb6c901d-d3_step2_range_growth_period`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** After the step-2 Schur complement, truncating to even d2 shells leaves the next-checkerboard H_kd zero for L=8,12 but nonzero for L=10,14, because the K-chart periods (L/2,L,L/2) determine whether minimal-vector d2 parity tracks chart parity.  _(class `C`)_
- **chain closes:** True — The runner builds the finite torus Hamiltonian, derives the step-1 closed form by the diagonal eliminated block and two-hop path counts, then computes the step-2 Schur complement and shell/truncation tables. An independent parity check confirms that when all K-periods are even, d2 parity equals chart-parity difference for opposite checkerboards; when L/2 is odd this parity protection is not well-defined, and the L=10,14 nonzero survivors are finite Schur-complement outputs rather than asserted constants.
- **rationale:** The runner source performs actual finite-matrix computation from the declared free nearest-neighbor Hamiltonian and Schur complements; the contested shell values and H_kd_after values are not hard-coded expected outputs. The numeric gates in the source note match the completed runner output, including 0.312% L=12/14 near-shell drift, the disclosed 8% L=8 box delta, and the L=10/14 post-truncation failures above 0.5. The clean verdict is for the bounded finite-box scope above, not for an asymptotic or all-L amplitude theorem beyond the tested representatives.
- **auditor confidence:** high

### `d3_truncated_closure_recurs_bounded_theorem_note_2026-06-12`

- **Note:** [`D3_TRUNCATED_CLOSURE_RECURS_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D3_TRUNCATED_CLOSURE_RECURS_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite L=8 and L=12, d=3 cubic lattice, E=0 free checkerboard decimation with the even-d² {2,4} truncation, through three truncated steps, including the stated retained-block Schur/resolvent budgets and no asymptotic flow claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260614-023238-a1c852cb6a-d3_truncated_closure_recurs_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** After projecting the step-1 retained operator to the even-d² {2,4} stencil, that stencil has zero kept-to-decimated block by parity, so the Schur correction vanishes on later truncated steps and the landed couplings recur unchanged.  _(class `C`)_
- **chain closes:** True — The supplied runner constructs the finite cubic Laplacian, performs the checkerboard Schur step, projects to the d²=0,2,4 stencil, and verifies zero truncated H_kd and recurrence. Independently, H_dd=6I at step 1 gives correction coefficients 1, 1/3, and 1/6 on shells d²=0,2,4, yielding diag=5, c2=-1/3, c4=-1/6; those displacements preserve checkerboard parity, so later H_kd=0 exactly.
- **rationale:** The load-bearing closure is not just a printed PASS line: the runner computes the Schur complement from the finite lattice operator rather than importing another note, and the parity argument independently forces the later Schur updates to vanish after truncation. The hard-coded expected constants are used as gates, but the same constants follow by direct shell counting from the initial Laplacian: per kept row the step-1 correction has squared RMS 1 + 12/9 + 6/36 = 5/2, giving the reported 1.58113883008419 budget, with zero later correction. No cited authority or open bridge is needed within the stated finite-L bounded scope.
- **auditor confidence:** high

### `d3_truncation_commensuration_criterion_bounded_theorem_note_2026-06-12`

- **Note:** [`D3_TRUNCATION_COMMENSURATION_CRITERION_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/D3_TRUNCATION_COMMENSURATION_CRITERION_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-dimensional d=3, E=0, t=1, mu=5 synthetic step-2 K-chart family with periods (L/2,L,L/2) on L={8,10,12,14,16,18}, testing equivalence among all-even periods, parity correspondence, and truncation protection.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00408-d3_truncation_commensuration`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** The full step-2 Schur computation verifies that, on the tested grid, parity correspondence holds if and only if the even-d2-truncated next-checkerboard block satisfies H_kd_after < 1e-14.  _(class `C`)_
- **chain closes:** True — The runner constructs the cubic Hamiltonian and both Schur steps, exhaustively checks K-chart parity correspondence, and directly computes H_kd_before and H_kd_after for all six lattice sizes. These computations establish the stated finite-grid equivalence from the retained-bounded authorities and declared test setup.
- **rationale:** The runner is not a print-only or constant-replay harness: it builds the finite operators, performs the Schur complements, enumerates all relevant chart pairs, and computes the protected and unprotected branches. The hard-coded L=10 and L=14 wave-8 values are two cross-note consistency gates, not the load-bearing support for the full-grid criterion or the computed L=16/L=18 extension. Both cited authorities are retained_bounded, and the conclusion remains explicitly limited to the tested grid and synthetic chart family.
- **auditor confidence:** high

### `dense_prune_guard_seed_note`

- **Note:** [`DENSE_PRUNE_GUARD_SEED_NOTE.md`](../../docs/DENSE_PRUNE_GUARD_SEED_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Aggregate behavior of scripts/channel_count_guarded_prune.py over seed in range(16), across the four printed (n_layers, npl) configurations with valid n as printed.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T115618Z-bd4287f9-dense_prune_guard_seed_n-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The channel-count guard is not a no-op on the runner's seed-range loop: aggregate eff_ch and aggregate flip count both move under the guard relative to plain pruning.  _(class `C`)_
- **chain closes:** True — The provided runner source and helper sources compute the graph generation, pruning, guarded pruning, gravity, purity, effective channel count, and flip aggregation directly rather than printing hard-coded expected values. The cached stdout supports the narrowed aggregate claim: eff_p changes under the guard in every printed configuration and total flips drop from 7 unguarded to 3 guarded across the four aggregate rows.
- **rationale:** The source note has been narrowed to exactly the cached runner's aggregate seed-range surface, and the runner output is present with exit_code 0. The primary runner imports helpers that are included in the packet and uses them in the load-bearing path; no helper appears to import the contested conclusion, hard-code the printed aggregate values, or substitute a definition for the claim. The aggregate flip reduction is true in the summed printed rows, although not in every individual configuration, which is acceptable under the narrowed aggregate scope.
- **auditor confidence:** high

### `depth_laurent_root_closed_form_bounded_theorem_note_2026-06-12`

- **Note:** [`DEPTH_LAURENT_ROOT_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/DEPTH_LAURENT_ROOT_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the supplied zB L=3 K3-K6 state fixtures, the tested scalar root-moduli formula is numerically refuted and the principal-branch determinant phase law reproduces the measured depth tails and ordering.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T015154Z-1f0c3329-00396-depth_laurent_root_closed_fo`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** For the supplied L=3 K3-K6 states, the per-root principal-branch Laurent phase sum reproduces the measured ladder weights, whereas the scalar root-moduli expression has large residuals and the wrong ordering.  _(class `C`)_
- **chain closes:** True — The runner constructs each finite state, computes the determinant phase increments, reconstructs and factors the Laurent determinant, and independently evaluates both the measured tails and scalar-form residuals. These computations establish the stated finite-fixture refutation and ordering.
- **rationale:** The source is not a printout-only matcher: it constructs the Hamiltonian and state projectors, evaluates determinant phases, validates the Laurent reconstruction on held-out angles, factors the roots, and computes harmonic weights, residuals, and orderings. Hard-coded landed values and expected orderings serve as cross-check anchors, while the scalar-form refutation is independently recomputed from the finite state fixtures. The verdict is limited to the supplied L=3 K3-K6 evaluations and makes no all-L or universal scalar-invariant claim.
- **auditor confidence:** high

### `det_phase_harmonic_depth_state_dependent_bounded_theorem_note_2026-06-12`

- **Note:** [`DET_PHASE_HARMONIC_DEPTH_STATE_DEPENDENT_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/DET_PHASE_HARMONIC_DEPTH_STATE_DEPENDENT_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The five explicitly seeded free-sector L=3 trajectories with tau=0.35 and T=256, projected onto nested signed-gap exact-tone spans through order 8.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00380-det_phase_harmonic_depth_sta`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** The K=6 state reaches the 0.99 capture threshold at order 4 with capture 0.995, whereas the other supplied states do not reach 0.99 through order 8.  _(class `C`)_
- **chain closes:** True — The runner constructs the finite free-sector trajectories and exact-tone bases, then computes the capture fractions without importing or hard-coding the resulting values. Its table directly establishes the mixed threshold-crossing pattern within the stated finite scope.
- **rationale:** The load-bearing result is a genuine finite first-principles computation: the capture values and saturation orders arise from constructed projectors, unitary evolution, determinant-phase increments, and exact-tone least-squares projections. Rank, nonzero-signal, basis-span, threshold, and monotonicity gates all pass, and no external comparator or tuned target value is used. The accepted realized-state primitive is used correctly to classify the differing pointwise results as supplied-state data, without asserting selection, weighting, typicality, or behavior beyond the tested family.
- **auditor confidence:** high

### `dimensional_gravity_table`

- **Note:** [`DIMENSIONAL_GRAVITY_TABLE.md`](../../docs/DIMENSIONAL_GRAVITY_TABLE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Cache-backed finite inventory for the d=3 and d=4 rows only: Born, F∝M, distance-tail/TOWARD entries as recorded in the registered runner caches/logs; d=2 and asymptotic 4D distance-law closure are out of binding scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-124123-20260517T124123Z-6877bb67-dimensional_gravity_tabl-targeted`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The binding d=3 and d=4 table entries are exactly the cache-backed rows asserted by the certificate runner against registered cached artifacts.  _(class `B`)_
- **chain closes:** True — Within the narrowed scope, the source note only claims that the displayed d=3/d=4 finite-entry numerics match registered cached artifacts, and the provided runner source verifies SHA-fresh caches/logs and asserts those quoted values. The chain does not establish first-principles lattice convergence or the open asymptotic 4D distance law, but those are explicitly outside the binding claim.
- **rationale:** The repaired note has narrowed the claim to a bounded cache-backed inventory rather than a universal dimensional-gravity theorem. The runner source is not a first-principles compute runner; it performs structural algebraic checks plus cache/log verification, so the load-bearing step is class B. Because the binding claim is only that the cache-backed d=3/d=4 entries are registered and internally matched, and the d=2 plus asymptotic 4D distance-law claims are demoted out of scope, the narrowed chain closes on its own terms.
- **auditor confidence:** high

### `dirac_core_card_note`

- **Note:** [`DIRAC_CORE_CARD_NOTE.md`](../../docs/DIRAC_CORE_CARD_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-round2-20260430-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The integrated DIR-3D core-card runner reports a bounded 12/16 result, with twelve retained positives and four named failures that remain the gravity/isotropy/k-achromaticity blockers.  _(class `C`)_
- **chain closes:** True — The note's bounded scorecard matches the registered runner: C1-C8, C12, and C14-C16 pass, while C9-C11 and C13 fail. The note explicitly carries forward those failures instead of promoting the lane to full 3+1D closure.
- **rationale:** The prior infrastructure blocker is resolved because the runner emits classified C-class PASS lines. The bounded inventory closes on its own terms: the runner reproduces the stated 12/16 integrated core-card score and the same four failures named by the note. This clean audit is limited to the scorecard/inventory claim and does not promote the Dirac lane beyond the note's bounded status because monotone gravity growth, distance law, strict isotropy, and fixed-theta k-achromaticity remain unresolved.
- **auditor confidence:** high

### `dirac_decoherence_probe_note`

- **Note:** [`DIRAC_DECOHERENCE_PROBE_NOTE.md`](../../docs/DIRAC_DECOHERENCE_PROBE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite numerical record produced by scripts/frontier_dirac_walk_3plus1d_decoherence_probe.py for the declared 4-component Dirac double-slit geometry at n=17 and n=21.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-152336-a5e2dcef-dirac_decoherence_probe_-013`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The registered runner computes, for the declared n=17 and n=21 Dirac double-slit cases, detector proxies near 0.06-0.07, record-mixture purity near 0.500, and clean-vs-record L1 residuals near 0.91-0.94.  _(class `C`)_
- **chain closes:** True — The runner source is self-contained, instantiates the Dirac algebra, walk, slit masks, propagation channels, and metrics directly, and its stdout matches the note's recorded numbers. No cited upstream authority or missing helper is needed for the narrowed finite-runner fact.
- **rationale:** For the narrowed scope, the note is a bounded numerical runner fact and the provided runner genuinely computes the reported observables rather than printing hard-coded target values. The reported n=17 and n=21 values in the note match the supplied runner output to the shown precision. This clean verdict does not ratify the broader harness-mismatch-versus-architecture diagnosis, which the note explicitly removes from binding scope.
- **auditor confidence:** high

### `dirac_observable_panel_note`

- **Note:** [`DIRAC_OBSERVABLE_PANEL_NOTE.md`](../../docs/DIRAC_OBSERVABLE_PANEL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded methodological panel claim that the Dirac 3+1D observable runner computes centroid, peak, first-arrival, early shell accumulation, current, and shell imbalance on the default sweep and records the resulting readout split without asserting a locked gravity sign.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T120421Z-5fc3513c-dirac_observable_panel_n-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The panel runner was executed on the stated default sweep, produced all six readouts for each layer count, and records an ALL/MIX readout split rather than a sign-locked gravity claim.  _(class `C`)_
- **chain closes:** True — The runner source genuinely evolves free and gravity Dirac states using imported gamma/projector split-step primitives, computes the listed observables, and the cached stdout matches the note's excerpt and summary. The only cited authority is retained_bounded, and the note does not rely on it to assert a stronger sign claim.
- **rationale:** The restricted packet includes the primary runner source, cached successful stdout, and the load-bearing helper source used for gamma matrices, split-step evolution, probability density, and torus distance. The primary runner does not merely print constants or import the contested panel conclusion; it computes the panel rows from the framework primitives and reports the mixed observable signs. The note's conclusion is bounded to methodological registration and reproducibility, and it explicitly avoids promoting a sign-locked gravity claim.
- **auditor confidence:** high

### `dirac_weak_coupling_note`

- **Note:** [`DIRAC_WEAK_COUPLING_NOTE.md`](../../docs/DIRAC_WEAK_COUPLING_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Within the supplied periodic 3+1D Dirac v4 scan grid, weakening strength from 5.0e-04 to 5.0e-05 leaves sign-stability totals unchanged, while larger lambda improves only the reported |bias| fit.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T015154Z-1f0c3329-00401-dirac_weak_coupling_note`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Across all four strengths the sign-stability totals remain unchanged, while increasing lambda improves the fitted |bias| magnitude law without restoring a signed delta-law fit.  _(class `C`)_
- **chain closes:** True — The primary runner calls a supplied helper that explicitly constructs the Dirac walk, evolves field and free cases, computes their bias difference, classifies signs, and fits the reported laws. Its completed output supports the scoped totals and lambda-dependent magnitude-fit behavior.
- **rationale:** The runner does not hard-code the contested totals or fitted exponents; it computes them from explicit lattice evolution and then performs transparent aggregation and regression. The completed summary matches the source note’s cross-strength invariance, absence of signed fits, and larger-lambda |bias| improvement. Clean status is limited to this configured finite scan and does not establish a continuum, universal gravity, or general coupling theorem.
- **auditor confidence:** high

### `directional_b_density_stencil_note`

- **Note:** [`DIRECTIONAL_B_DENSITY_STENCIL_NOTE.md`](../../docs/DIRECTIONAL_B_DENSITY_STENCIL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded runner audit of the deterministic generated reference, tree-control, and center-biased midlayer samples using frozen dense-reference 3-NN and 4-NN density-load thresholds.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-141901-30b1a9aa-directional_b_density_st-047`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Once the center-biased midlayer sentinel is added to the reference+tree sample, the frozen 3-NN density-load rule has higher extended-sample accuracy than the frozen 4-NN rule: 0.9126 versus 0.8932.  _(class `C`)_
- **chain closes:** True — The primary runner rebuilds the rows, computes the dense-reference thresholds with _best_rule, applies them without refit, and computes the reported accuracy and miss-mode tables. The transitive helper sources needed for generated rows, density features, overlap labels, and threshold evaluation are present in the packet.
- **rationale:** The runner is not a constant printer: it constructs the dense reference rows, tree rows, and midlayer rows from the included generators and evaluates the rules from computed row features. The contested 3-NN versus 4-NN preference reversal follows from those computed rows and frozen thresholds within the stated bounded sample. No cited upstream authority is required for the restricted claim, and no helper path listed as load-bearing is missing from the packet.
- **auditor confidence:** high

### `dispersion_high_p_tiebreaker_note`

- **Note:** [`DISPERSION_HIGH_P_TIEBREAKER_NOTE.md`](../../docs/DISPERSION_HIGH_P_TIEBREAKER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the runner-backed bounded numerical table and narrowed comparator-scope conclusion for the p=0–6 Fam1 dispersion sweep, not the split lensing/eikonal follow-ups or any KG-elimination claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-141901-30b1a9aa-dispersion_high_p_tiebre-057`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Extending the dispersion measurement to p=0–6 tabulates four fit variants: Schrödinger and Linear are tied in ω-space, linearized KG reports lower R² in ω²-space but is not directly comparable, and the dispersion shows dropout/curvature structure at high p.  _(class `C`)_
- **chain closes:** True — The included runner source genuinely grows the stated DAGs, propagates the plane-wave amplitudes, measures phase slopes, filters clean modes, and fits the reported models rather than printing fixed constants. The note's narrowed conclusion tracks the runner output while explicitly withholding the stronger same-dependent-variable KG-elimination inference.
- **rationale:** The load-bearing claim is a bounded computational result from the provided runner, and the code performs the numerical construction from its stated lattice/propagation rules without importing another note or hard-coding the contested fit outcomes. The note correctly repairs the runner's misleading stdout phrase “TIE BROKEN” by narrowing the scientific conclusion to an apples-to-apples Schrödinger/Linear ω-space tie and an incomparable linearized-KG ω²-space result. The lensing and eikonal implications are explicitly split out as open follow-ups and are outside the audited claim scope.
- **auditor confidence:** high

### `distance_law_definitive_note`

- **Note:** [`DISTANCE_LAW_DEFINITIVE_NOTE.md`](../../docs/DISTANCE_LAW_DEFINITIVE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite ordered-cubic Dirichlet Poisson/path-sum diagnostic table for N=31..96, the selected scaled-window N>=56 weighted mean, and the N=64 mass-independence check.
- **audit_status:** ~~audited_numerical_match~~
- **effective_status:** ~~audited_numerical_match~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-distance_law_definitive_note-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the selected N >= 56 scaled-window weighted-mean diagnostic, the exponent is numerically consistent with alpha = -1 at 0.1% precision.  _(class `G`)_
- **chain closes:** False — The runner genuinely computes the finite Dirichlet Poisson/path-sum table and the N=64 mass-independence check, and the quoted numbers match the cache. The inverse-square conclusion does not close because the selected N>=56 scaled-window weighted mean is not independently selected over extrapolation families in the same output that miss -1 by several percent.
- **rationale:** Issue: the 0.1% agreement comes from the selected scaled-window N>=56 weighted mean, not from a theorem selecting that estimator. Why this blocks: other reported extrapolations give alpha_inf values several percent away from -1, so the inverse-square interpretation depends on the chosen estimator. Repair target: provide an independent estimator-selection theorem or a pre-registered protocol selecting this window before seeing the result. Claim boundary until fixed: finite-table numerical support for the stated ordered-cubic Dirichlet diagnostic only.
- **auditor confidence:** high

### `dm_abcc_basin_finite_search_support_note_2026-04-30`

- **Note:** [`DM_ABCC_BASIN_FINITE_SEARCH_SUPPORT_NOTE_2026-04-30.md`](../../docs/DM_ABCC_BASIN_FINITE_SEARCH_SUPPORT_NOTE_2026-04-30.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Deterministic finite-scan support certificate on the active A-BCC chamber only: the registered runner, without importing the archived basin coordinate chart, solves the live Hermitian-pencil PMNS-angle residual equations over the declared coordinate box [-50,50]^3, retained sigma set, active chamber inequality, and three deterministic seed families; it reproduces exactly three active-chamber representatives and their one-C_base/two-C_neg determinant split. No interval/root-isolation exhaustiveness, global no-missed-basin theorem, out-of-chamber chart closure, or complete A-BCC selector theorem is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-dm-abcc-basin-finite-search-20260528-r1`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The SHA-pinned runner cache reports PASS=16 FAIL=0: source-input firewall leaks=[], endpoint/midpoint/Chebyshev families each derive the same three active-chamber roots, residuals are <=4.91e-15, all representatives are inside the coordinate box and chamber, local residual Jacobians are full rank with min singular value 4.049e-04, and determinant components are one C_base plus two C_neg.  _(class `C`)_
- **chain closes:** True — The row has no one-hop dependencies; the repaired live runner is the registered primary evidence and supports only the finite active-chamber scan surface stated in the source. The archived exhaustive wrapper remains historical provenance and is not promoted.
- **rationale:** Clean bounded retention is appropriate for the repaired finite-scan support claim. The runner firewall confirms the active representatives are derived from the live equations rather than copied from the archived coordinate chart, and all three seed families agree on the same three in-chamber roots. The result is not exhaustive: the source and runner both disclaim interval/root-isolation and global no-missed-basin authority. The finite representative set, residual norms, chamber membership, local full-rank checks, and C_base/C_neg split are nevertheless reproducible runner facts on the declared scan surface.
- **auditor confidence:** medium

### `dm_full_closure_same_surface_converged_thermal_selector_support_note_2026-04-16`

- **Note:** [`DM_FULL_CLOSURE_SAME_SURFACE_CONVERGED_THERMAL_SELECTOR_SUPPORT_NOTE_2026-04-16.md`](../../docs/DM_FULL_CLOSURE_SAME_SURFACE_CONVERGED_THERMAL_SELECTOR_SUPPORT_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-round2-20260430-03`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Using the corrected high-precision continuum thermal evaluator on the admitted same-surface one-scalar DM family gives a unique interior closure crossing at sigma_conv = 0.145077095756643 and Omega_DM = 0.268.  _(class `D`)_
- **chain closes:** True — The note states a bounded admitted-family convergence claim, and the runner recomputes the interior crossing, matches the quoted Omega_DM comparator, and verifies material drift away from the coarse and 9/62 values.
- **rationale:** The bounded support claim closes on its own terms: the runner recomputes the converged same-surface selector, verifies the observed Omega_DM comparator on the admitted one-scalar family, and checks that the coarse grid and 9/62 clue are not stable. The source note explicitly keeps current-bank selector closure open, so this clean audit is limited to the convergence/sanity-check surface and does not ratify a theorem-grade DM selector law. Residual risk is downstream misuse of the admitted-family crossing as a first-principles current-bank closure.
- **auditor confidence:** high

### `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16`

- **Note:** [`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md`](../../docs/DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded same-surface thermal integral representation at the declared freeze-out slice x_f=25: using the retained Maxwell-Boltzmann/Sommerfeld normalization certificate, the thermal average can be written as <S>=(2/sqrt(pi))*int_0^infty S(alpha_eff*sqrt(a)/sqrt(t))*sqrt(t)*exp(-t) dt with a=25/4 and sqrt(a)=5/2, and the low-order moments are <1/v>=5/sqrt(pi), <1/v^2>=25/2. No DM selector closure, Sommerfeld-factor derivation, freeze-out derivation, relic-abundance theorem, or evaluation/bound of the remaining integral family is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-dm-thermal-integral-representation-20260528-r1`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The cached runner and direct rerun pass five checks: exact denominator, t-prefactor 2/sqrt(pi), <1/v>=5/sqrt(pi), <1/v^2>=25/2, and reduction of the former grid-average object to one continuum integral target. An independent symbolic substitution t=a v^2 gives normalized t-weight 2*sqrt(t)*exp(-t)/sqrt(pi) and sqrt(a)=5/2 at x_f=25.  _(class `A`)_
- **chain closes:** True — The sole one-hop dependency is retained-bounded and supplies the normalization constants and Sommerfeld argument convention. The row's runner and independent symbolic check verify only the integral representation and moment identities; the open selector/integral-evaluation problem remains outside the audited closure.
- **rationale:** Clean bounded retention is appropriate after strict scope narrowing. The title says full closure, but the body and runner only close an exact integral representation and low-order moments on the declared same-surface slice. The independent change-of-variables audit confirms the normalized MB measure transforms to (2/sqrt(pi))*sqrt(t)*exp(-t) dt and the Sommerfeld argument becomes alpha_eff*sqrt(a/t). The source explicitly states current-bank selector closure remains open, so no downstream DM closure or Sommerfeld physics is smuggled into the verdict.
- **auditor confidence:** high

### `dm_full_closure_same_surface_thermal_selector_sensitivity_boundary_note_2026-04-16`

- **Note:** [`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SELECTOR_SENSITIVITY_BOUNDARY_NOTE_2026-04-16.md`](../../docs/DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SELECTOR_SENSITIVITY_BOUNDARY_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-round2-20260430-04`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Refining the same-surface thermal quadrature shifts the admitted-family selector root by far more than the apparent 9/62 residual, so the structural 9/62 collapse is not stable.  _(class `C`)_
- **chain closes:** True — The note's bounded negative claim is exactly reproduced by the runner: it computes the coarse apparent match, then recomputes refined roots at 4000, 8000, and 16000 points and shows material drift away from 9/62.
- **rationale:** The bounded sensitivity boundary closes on its own terms: the runner reproduces the coarse near-match to 9/62 and then verifies that quadrature refinement shifts the selector root by a much larger amount. The conclusion is negative and scoped correctly: 9/62 must not be promoted as a DM selector law from this thermal surface. Residual risk is only downstream reuse of the coarse coincidence after this explicit instability result.
- **auditor confidence:** high

### `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17`

- **Note:** [`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SERIES_TAIL_SUPPORT_NOTE_2026-04-17.md`](../../docs/DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SERIES_TAIL_SUPPORT_NOTE_2026-04-17.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Pure x_f=25 same-surface thermal-kernel series/tail certificate: positive series identities, J1/J2 Meijer-G term integrals, and exact tail enclosures, with live-DM sample constants treated only as conditional exhibits.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260615-231309-9b1a78cd22-dm_full_closure_same_surface`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The same-surface thermal factors have positive geometric-series expansions, and their truncation tails are bounded by (1+y)e^{-Ny} and (1+y)e^{-(N+1)y}, reducing the remainders to J1/J2 integrals.  _(class `A`)_
- **chain closes:** True — For y>0 the series identities are geometric, the tail inequalities follow from e^y >= 1+y, and the J1/J2 Meijer-G representations check against independent quadrature of the stated integrals. The conditional alpha/eta/omega sample definitions are not needed for the pure thermal-kernel certificate.
- **rationale:** The audited core is algebraic over the cited retained-bounded thermal-normalization inputs. The runner's seven PASS checks are class-A checks and several are hard-coded assertions, so stdout alone would not be enough, but independent formula checks verify the signs, factors, normalizations, Meijer-G forms, and displayed interval numerics. The six live-slice SUPPORT checks rely on conditional helper-defined sample constants and observational conversion helpers, but the source note explicitly excludes those from the load-bearing theorem scope.
- **auditor confidence:** high

### `dm_leptogenesis_pmns_sole_axiom_boundary_note_2026-04-16`

- **Note:** [`DM_LEPTOGENESIS_PMNS_SOLE_AXIOM_BOUNDARY_NOTE_2026-04-16.md`](../../docs/DM_LEPTOGENESIS_PMNS_SOLE_AXIOM_BOUNDARY_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Whether, on the stated current branch, the sole axiom and native seed pair fail to determine a unique active five-real off-seed source and PMNS-assisted eta value.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-20260712-203012-f022c5b2-f022c5b261b5414d8df3d4656cedda20-dm_leptogenesis_pmns_sol-001`  (codex-gpt-5.6; independence=weak)
- **load-bearing step:** Two exact active microscopic points can share the same native seed pair while carrying different off-seed five-real source data.  _(class `A`)_
- **chain closes:** False — The supplied arrays establish non-injectivity of the seed-average map and different downstream outputs, but the packet never derives that both active points are admissible consequences of Cl(3) on Z^3 or that the seed pair exhausts the axiom-fixed information.
- **rationale:** Issue: the runner proves only that two hand-chosen arrays have equal means but different source coordinates and transport outputs. Why this blocks: several decisive conclusions are checked with literal True, while the transport chain imports chosen physical constants and a hard-coded canonical eta target, so it does not establish the claimed sole-axiom boundary. Repair target: derive the admissible active-source family from Cl(3) on Z^3 and exhibit two axiom-compatible points, or restrict the claim to the finite supplied-sample map. Claim boundary until fixed: the examples support algebraic seed-map nonuniqueness and differing downstream numerical outputs conditional on the imported model.
- **auditor confidence:** high

### `dm_lepton_synthesis_note_2026-04-19`

- **Note:** [`DM_LEPTON_SYNTHESIS_NOTE_2026-04-19.md`](../../docs/DM_LEPTON_SYNTHESIS_NOTE_2026-04-19.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-resweep-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** This note synthesises all derived results for dark matter candidates and  _(class `C`)_
- **chain closes:** True — Yes. The registered runner exits cleanly and exposes 9 classified A/B/C/D checks for this leaf claim with no non-retained one-hop dependencies.
- **rationale:** The restricted packet closes on its declared support scope: the source note has no non-retained one-hop dependencies and the registered runner passes with classified C-dominant checks. This audit ratifies only that bounded/support leaf surface, not any stronger retained-tier conclusion unless the source note is separately re-tiered. Residual risk: the audit relies on the registered runner as the executable witness and does not import broader publication framing.
- **auditor confidence:** high

### `dm_thermal_average_sommerfeld_textbook_import_note_2026-05-17`

- **Note:** [`DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`](../../docs/DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded Maxwell-Boltzmann/Sommerfeld normalization algebra at the explicit benchmark slice x_f=25, with a=x_f/4=25/4: verifies the normalized MB denominator, <1/v>=5/sqrt(pi), <1/v^2>=25/2, the substitution t=a v^2 giving alpha_eff/v=alpha_eff*sqrt(a/t), and the thermal-average t-measure prefactor 2/sqrt(pi). No framework derivation of the Maxwell-Boltzmann distribution, freeze-out value x_f=25, Sommerfeld enhancement law, relic-abundance dynamics, or downstream DM thermal closure is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-dm-thermal-average-sommerfeld-normalization-20260528-r1`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The cached runner and direct rerun pass the finite formulas: integral v^2 exp(-a v^2) dv = sqrt(pi)/(4 a^(3/2)); <1/v>=2 sqrt(a)/sqrt(pi)=5/sqrt(pi) at a=25/4; <1/v^2>=2a=25/2; alpha_eff/v transforms to alpha_eff sqrt(a/t); and 1/Gamma(3/2)=2/sqrt(pi).  _(class `A`)_
- **chain closes:** True — The row has no one-hop dependencies, the registered runner is fresh and passes, and the independent symbolic integration verifies the same finite normalization identities. The declared physics inputs are explicitly outside the audited closure and are not promoted.
- **rationale:** Clean bounded retention is appropriate because the claim is only finite normalization algebra over declared inputs. Independent symbolic checks give denom=sqrt(pi)/(4*a^(3/2)), <1/v>=2*sqrt(a)/sqrt(pi), <1/v^2>=2*a, x_f=25 values 5/sqrt(pi) and 25/2, alpha/v -> alpha*sqrt(a/t), and 1/Gamma(3/2)=2/sqrt(pi), matching the runner. The bounded-wall scan finds the MB distribution, x_f=25, and Sommerfeld factor are all explicit declared inputs and explicitly excluded from derivation, so there is no hidden textbook import in the audited scope.
- **auditor confidence:** high

### `edge_deletion_boundary_note`

- **Note:** [`EDGE_DELETION_BOUNDARY_NOTE.md`](../../docs/EDGE_DELETION_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded runner-backed sweep of the retained 3D valley-linear family at h=0.5, W=8, L=12, max_d=3, keep fractions 1.00 to 0.75, and seeds 20260404..20260415, checking TOWARD sign and mean delta plus representative controls.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T175712Z-3dfb1fc0-edge_deletion_boundary_n-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On this family, in this swept retention range, the gravity sign stays TOWARD at every tested keep fraction and every tested seed.  _(class `C`)_
- **chain closes:** True — The primary runner constructs the graph lattice, field, slit blocking, propagation, detector centroid, and per-seed deltas, then summarizes the exact keep-fraction rows reported in the note. The helper source supplies the computational primitives and constants rather than importing the contested table values.
- **rationale:** The note's table matches the completed runner output, and the runner source performs an actual bounded sweep over keep fractions and seeds rather than printing constants. The helper import is load-bearing but implements lattice construction, field generation, propagation, Born ratio, and controls directly; its hard-coded assertions are in the helper's own main path and are not used by the primary runner's load-bearing computation. The conclusion is properly caveated to this family, parameter range, and seed set, so it does not overclaim a universal graph theorem.
- **auditor confidence:** high

### `edge_deletion_boundary_sweep_note`

- **Note:** [`EDGE_DELETION_BOUNDARY_SWEEP_NOTE.md`](../../docs/EDGE_DELETION_BOUNDARY_SWEEP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded multi-seed edge-deletion sweep on the retained 3D valley-linear family for h=0.5, W=8, L=12, max_d=3, keep fractions 1.00 to 0.75, and seeds 20260404..20260415.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e0d77-2287-7010-b1fd-77ed392fecf1`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The sweep table reports TOWARD 12/12 with positive mean delta at every tested keep fraction from 1.00 down to 0.75.  _(class `C`)_
- **chain closes:** True — Within the restricted claim scope, the runner directly constructs the listed lattice instances, measures gravity_delta for each keep fraction and seed, and the stdout matches the frozen table. The conclusion is explicitly bounded to absence of a sign flip in this tested range, not a universal graph theorem.
- **rationale:** The load-bearing result is a bounded computational sweep, and the runner source does not merely print constants: it builds GraphLattice3D cases, deletes edges by keep fraction and seed, propagates free and field amplitudes, and computes centroid deltas. The note's claim boundary is already narrow: sign stability through 25% edge deletion on this retained family and seed set, with no claimed threshold transition or universal theorem. A second auditor should only re-check that the imported GraphLattice3D family implementation is the intended retained family, but that is outside the supplied packet and not needed for this bounded replay verdict.
- **auditor confidence:** medium

### `eigenvalue_anderson_phase_note_2026-04-11`

- **Note:** [`EIGENVALUE_ANDERSON_PHASE_NOTE_2026-04-11.md`](../../docs/EIGENVALUE_ANDERSON_PHASE_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-resweep-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** 2. an Anderson-vs-gravity phase map on the boundary-law coefficient  _(class `C`)_
- **chain closes:** True — Yes. The registered runner exits cleanly and exposes 6 classified A/B/C/D checks for this leaf claim with no non-retained one-hop dependencies.
- **rationale:** The restricted packet closes on its declared bounded scope: the source note has no non-retained one-hop dependencies and the registered runner passes with classified C-dominant checks. This audit ratifies only that bounded/support leaf surface, not any stronger retained-tier conclusion unless the source note is separately re-tiered. Residual risk: the audit relies on the registered runner as the executable witness and does not import broader publication framing.
- **auditor confidence:** high

### `electrostatics_card_note`

- **Note:** [`ELECTROSTATICS_CARD_NOTE.md`](../../docs/ELECTROSTATICS_CARD_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** A narrow scalar sign-coupled electrostatic-like response was audited on the fixed retained 3D ordered-lattice family using the provided runner and cached stdout, excluding any claim of full electromagnetism.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260504-234846-c679ece8-electrostatics_card_note-006`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The same ordered-lattice machinery can support an electrostatic-like scalar sign law in which like charges repel, unlike charges attract, null superpositions cancel, dipoles flip sign, response scales linearly, and screening attenuates.  _(class `C`)_
- **chain closes:** True — The runner explicitly instantiates the 3D ordered lattice, constructs scalar source fields, propagates charged test packets, and computes the reported centroid shifts rather than printing constants. The audited conclusion is limited to the constructed scalar sign-law probe and does not require Maxwell, gauge, magnetic, or radiative structure.
- **rationale:** The provided source code performs an internal numerical computation over the lattice machinery and derives the sign antisymmetry, null cancellation, dipole flip, charge-scaling exponent, and screening attenuation values shown in stdout. The reported numbers are not hard-coded expected outputs, and no external comparator or cross-note value is imported. The clean verdict applies only to the narrow scalar sign-coupled construction as stated, not to any broader electromagnetic theory.
- **auditor confidence:** high

### `electrostatics_superposition_proxy_note`

- **Note:** [`ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE.md`](../../docs/ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** A narrow numerical proxy: within the specified ordered lattice harness and sign-coupled weak-field propagator, multiple source fields are linearly combined and the detector centroid shifts show cancellation, reinforcement, dipole reduction, and approximate doubling.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260504-234846-c679ece8-electrostatics_superposi-009`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The same weak-field sign-coupled propagator supports linear source superposition, so same-point opposite charges cancel, like charges reinforce, and dipole/double-source cases give the reported signed centroid shifts.  _(class `C`)_
- **chain closes:** True — The provided runner constructs the lattice, sums source fields linearly, propagates a test charge, and computes centroid shifts rather than printing fixed expected constants. The audited conclusion is limited to this proxy harness and does not establish Maxwell theory or full electromagnetism.
- **rationale:** The note's load-bearing claims are qualitative consequences of the completed runner output and the runner source shows actual computation of the tested cases. There are no cited upstream authorities to propagate, and no external comparator or calibrated input is used for the contested conclusion. The result is clean only at the explicitly narrow proxy scope: linear field summation inside the imported retained weak-field propagator harness.
- **auditor confidence:** medium

### `em_gravity_coexistence_2x2_note`

- **Note:** [`EM_GRAVITY_COEXISTENCE_2X2_NOTE.md`](../../docs/EM_GRAVITY_COEXISTENCE_2X2_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the explicitly defined finite path-sum ray propagator with additive gravity and EM action terms, the 2x2 mixed residual and charge-sign cancellations vanish to floating-point tolerance.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e1372-176a-7531-8f49-25b16dbf0418`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** By linearity of action accumulation, S(Hg+Hem) = k(1-f) + qV and S(Hg) + S(Hem) - S(H0) = k(1-f) + qV, so R_GE = 0 exactly.  _(class `A`)_
- **chain closes:** True — The four-cell action definitions are supplied in the note, and accumulated phase plus finite-difference deflection are linear operations, so the mixed residual cancels identically. No broader Hamiltonian, gauge, magnetic-sector, or backreaction coexistence claim is needed for this bounded scope.
- **rationale:** The load-bearing claim is an algebraic closure inside the defined ray-sum model, and the runner computes the four cells before checking the mixed residual and charge-sign cancellations rather than importing an external target. The clean result is bounded to additive kinematic action accumulation only; the source note explicitly excludes dynamical wave-packet, gauge-invariant, magnetic-sector, and nonlinear/backreaction coexistence.
- **auditor confidence:** high

### `emergent_geometry_growth_note_2026-04-10`

- **Note:** [`EMERGENT_GEOMETRY_GROWTH_NOTE_2026-04-10.md`](../../docs/EMERGENT_GEOMETRY_GROWTH_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Single-seed qualitative comparison from scripts/frontier_emergent_geometry.py between matter-coupled growth and the uniform-growth control, using the cached runner output and included source.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260518-123911-c0b36f0f-emergent_geometry_growth-006`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** On seed 42, the primary runner's matter-coupled growth rule produces a grown graph with higher effective dimension and much higher peak shell-bin density than the uniform-growth control.  _(class `C`)_
- **chain closes:** True — The included runner source actually constructs both graphs, evolves the matter field for the coupled case, applies the |psi|^2-biased parent selection, and computes the reported shell-volume and density metrics. The cached output supports the narrowed qualitative claim on this seed.
- **rationale:** The narrowed load-bearing claim is not the broader multi-seed or gravitational-closure story; it is the single-seed primary-runner comparison. The runner does not merely print constants or import the contested conclusion: it computes the grown graph and control from fixed rules and reports d_eff = 1.64 versus 1.55 and peak shell-bin density about 72 versus 11. The broader companion-runner claims are explicitly scoped as support diagnostics and are not needed for this audited claim.
- **auditor confidence:** high

### `emergent_product_law_audit_2026-04-11`

- **Note:** [`EMERGENT_PRODUCT_LAW_AUDIT_2026-04-11.md`](../../docs/EMERGENT_PRODUCT_LAW_AUDIT_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite mass-sweep magnitude scaling on the side=14, G=50, mu^2=0.001 open 3D staggered cross-field Poisson surface with frozen-source control.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e1373-c4a4-79f0-9de6-0a131f8296e6`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** On the audited open 3D staggered cross-field Poisson surface (`side=14`, `G=50`, `mu^2=0.001`), two-orbital Hartree dynamics produces `|F| ~ M_A^1.0146 M_B^0.9863` with `R^2 = 0.999993`, and the frozen-source control gives `|F| ~ M_A^1.0081 M_B^0.9919` with `R^2 = 0.999998`.  _(class `C`)_
- **chain closes:** True — The completed runner source and stdout compute the stated exponents on the stated finite surface, and the note confines the interpretation to bounded |F| product-law scaling from field linearity. No unlisted dependency is needed for that scoped numerical claim.
- **rationale:** The runner builds the lattice, solves Poisson fields from rho=M|psi|^2, evolves cross-field Hamiltonians, measures F=-M<grad phi>, and fits the mass sweep; the stdout matches the retained numbers. The separate source and test mass factors are explicit model definitions, so the clean result is only a bounded field-linearity/magnitude theorem on this one surface. The sign diagnostic would block attraction wording, but not the retained |F| scaling claim.
- **auditor confidence:** high

### `emergent_product_law_note`

- **Note:** [`EMERGENT_PRODUCT_LAW_NOTE.md`](../../docs/EMERGENT_PRODUCT_LAW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-resweep-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** **Frozen-source control:** Poisson fields computed once from initial densities and  _(class `C`)_
- **chain closes:** True — Yes. The registered runner exits cleanly and exposes 3 classified A/B/C/D checks for this leaf claim with no non-retained one-hop dependencies.
- **rationale:** The restricted packet closes on its declared bounded scope: the source note has no non-retained one-hop dependencies and the registered runner passes with classified C-dominant checks. This audit ratifies only that bounded/support leaf surface, not any stronger retained-tier conclusion unless the source note is separately re-tiered. Residual risk: the audit relies on the registered runner as the executable witness and does not import broader publication framing.
- **auditor confidence:** high

### `energy_channel_induced_kernel_route_a_note_2026-07-08`

- **Note:** [`ENERGY_CHANNEL_INDUCED_KERNEL_ROUTE_A_NOTE_2026-07-08.md`](../../docs/ENERGY_CHANNEL_INDUCED_KERNEL_ROUTE_A_NOTE_2026-07-08.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the defined free d=1, N=256 staggered-fermion comparator and local-energy convention, the positive background Lehmann susceptibility has a numerically vanishing q=0 value, the reported four-point Aq^2+Bq^4 fits, and the checked continuity residuals.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-20260710-131002-abb23e4d-energy_channel_induced_k-002`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Diagonalizing the declared N=256 comparator and evaluating the displayed Lehmann sum and current matrix elements yields the reported zero mode, finite-momentum fit coefficients, and continuity residuals.  _(class `C`)_
- **chain closes:** True — The runner constructs and diagonalizes the declared Hamiltonian rather than importing the reported values. Summing the local densities gives H, while the local-density commutator algebra supplies the stated continuity factor and its Lehmann-kernel consequence.
- **rationale:** The runner genuinely computes the susceptibility, fit coefficients, and continuity residuals from the declared finite-lattice operators and contains no hard-coded expected numerical results. Independently, sum_n h_n=H forces the occupied-to-empty q=0 block to vanish, and the nearest-neighbor density commutators give the displayed continuity factor and kernel relation with the correct powers of the energy denominator. The reported numbers agree with the completed cache, and the note confines them to the finite comparator and stated fit window.
- **auditor confidence:** high

### `energy_covariant_rg_collapse_shifted_coupling_bounded_theorem_note_2026-06-12`

- **Note:** [`ENERGY_COVARIANT_RG_COLLAPSE_SHIFTED_COUPLING_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/ENERGY_COVARIANT_RG_COLLAPSE_SHIFTED_COUPLING_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Free 1D uniform nearest-neighbor chain under nondegenerate b=2 odd-sublattice Schur decimation, with mu != E and chart |h| < 1/sqrt(2), proving the E-independent shifted quotient map h' = h^2/(1 - 2h^2).
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260613-015451-1cde157482-energy_covariant_rg_collapse`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Since H_oo - E I = (mu - E)I, the Schur complement gives mu' = mu - 2t^2/(mu - E) and t' = t^2/(mu - E), hence mu' - E = (mu - E)(1 - 2h^2) and h' = h^2/(1 - 2h^2).  _(class `A`)_
- **chain closes:** True — The independent Schur-complement calculation gives the stated diagonal and nearest-neighbor effective parameters with the correct signs and factors. The singular gate mu = E and the displayed-map pole at h^2 = 1/2 are excluded by the stated domain/chart.
- **rationale:** The load-bearing step is a direct algebraic closure, not a definition, renaming, tuned numerical match, or external comparator. The runner source genuinely constructs finite-ring Hamiltonians, performs the Schur complement, and checks the formula, singular gate, threshold covariance, length diagnostic, sign quotient, and chart boundary without importing a contested premise. No cited authority or open bridge is needed for this bounded free-chain statement.
- **auditor confidence:** high

### `epsstar_coefficient_richardson_moff0_bounded_note_2026-06-12`

- **Note:** [`EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md`](../../docs/EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite Harper/PT one-particle computation for Q=24, Ly=2, N=48, GL=20, branch bracket [1.2,2.4], fixed etas {0.08,0.04,0.02,0.01}, at m=0 and m=0.2 only.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-epsstar_coefficient_richardson_moff0_bounded_note_2026-06-12-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner separately computes the fixed-eta PT response fit chi(mu0,eta)/eta^2 = a + b eta^2 and the finite-T mu*(T)^2 root-locus slope, then compares the extrapolated alpha and m=0.2 kernel split against the stated gaps and sign-flip inequalities.  _(class `C`)_
- **chain closes:** True — The included runner constructs the finite Harper/PT matrices, diagonalizes the GL grid, computes the T=0 branch, eta-sequence Richardson fit, finite-T root-locus slope, and m=0.2 split directly. The frozen constants are used as post-computation gates rather than as inputs to the extrapolant or slope calculation.
- **rationale:** The source and runner agree on the bounded finite-cell scope, and the runner performs the load-bearing computations rather than printing or importing the contested values. The eta^2 fit arithmetic, residual bound, gap comparison, and sign inequalities are internally consistent with the packet values. No cited authority or unclosed primitive is needed for the restricted finite-cell statement, and the note explicitly avoids continuum, full-surface, or gauge-self-energy claims.
- **auditor confidence:** high

### `evolving_network_prototype_note`

- **Note:** [`EVOLVING_NETWORK_PROTOTYPE_NOTE.md`](../../docs/EVOLVING_NETWORK_PROTOTYPE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded computational claim that `scripts/evolving_network_prototype_v2.py`, with its included helper, runs a generated hard-gap pruning rule and a same-budget imposed control on the same 3D DAG family and supports only the note's cautious prototype interpretation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-152638-a5e2dcef-evolving_network_prototy-016`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The generated hard-gap rule produces measurable gap growth, while the imposed same-budget control often makes the purity comparison undefined, so the result is only a bounded prototype signal rather than a clean Gate B win.  _(class `C`)_
- **chain closes:** True — The restricted packet includes the primary runner and its transitive helper, and the runner genuinely constructs random 3D DAGs, applies the pruning/control rules, and computes purity and gap metrics rather than printing fixed target constants. The note's cautious conclusion follows from the provided cached run, though the control is explicitly not a fair final discriminator.
- **rationale:** The note does not promote a decisive physics theorem; it retains only the bounded claim that this prototype shows generated gap growth while the comparator leaves purity undefined or unusable. The runner source and helper source are complete in the restricted packet and compute the relevant graph, pruning, purity, and gap quantities without hard-coded contested values. There is a text/code inconsistency around whether the imposed control is random removal or a center-band control, but that weakens only any stronger baseline-fairness claim, which the note explicitly withholds.
- **auditor confidence:** medium

### `evolving_network_prototype_v2_note`

- **Note:** [`EVOLVING_NETWORK_PROTOTYPE_V2_NOTE.md`](../../docs/EVOLVING_NETWORK_PROTOTYPE_V2_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The cached finite sweep reports positive generated_gap, conv=0.00, and imposed_pur=nan across the printed rows; same-budget generated-vs-imposed and baseline-gap conclusions are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T173506Z-bc1c240f-evolving_network_prototy-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Within the tested parameter sweep, the runner reports a positive generated_gap, no convergence (conv = 0.00), and an undefined imposed_pur (nan).  _(class `C`)_
- **chain closes:** True — The provided runner source genuinely generates DAG instances, applies the pruning/control procedures, and computes the printed metrics through the included helper, rather than hard-coding the table. The cached stdout directly supports the narrowed readout, while the unsupported same-budget and baseline-gap claims are explicitly withdrawn.
- **rationale:** For the narrowed claim, every printed generated_gap is positive, every printed conv value is 0.00, and every printed imposed_pur is nan. The helper source is present, so the runner chain is not opaque, and no external comparator or tuned measured value is imported. The verdict does not ratify the withdrawn same-budget comparator, imposed-control purity comparison, or baseline-gap separation.
- **auditor confidence:** high

### `evolving_network_prototype_v4_note`

- **Note:** [`EVOLVING_NETWORK_PROTOTYPE_V4_NOTE.md`](../../docs/EVOLVING_NETWORK_PROTOTYPE_V4_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite v4 prototype result for scripts/evolving_network_prototype_v4.py at current constants/seeds: fixed-offset crystal connectivity ties KNN on toward count and slightly improves mean_delta and alpha, without proving a general Gate B dynamics theorem.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-evolving-network-v4`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The frozen replay lands as a mixed bounded result: ordered 0.0/9 mean_delta -0.000058 alpha 0.00, crystal 2.0/9 mean_delta -0.000037 alpha 0.83, and KNN control 2.0/9 mean_delta -0.000050 alpha 0.66; crystal improves mean_delta/alpha but does not clearly beat KNN on toward count.  _(class `C`)_
- **chain closes:** True — The runner explicitly constructs the ordered, crystal fixed-offset, and KNN-on-same-positions families, computes the stated metrics, and current stdout reproduces the note's frozen table. There are no known upstream dependencies; closure is only for this finite prototype comparison.
- **rationale:** The note's load-bearing numerical table matches the current runner output, and the prose substantially bounds the result as a prototype rather than a solved dynamics theorem. The main signal is correctly described as mixed: crystal does not beat KNN on toward count, but it slightly improves mean_delta and alpha. Residual risk is only scope risk: broader claims such as a general connectivity bottleneck are not audited here beyond this finite replay.
- **auditor confidence:** high

### `evolving_network_prototype_v5_note`

- **Note:** [`EVOLVING_NETWORK_PROTOTYPE_V5_NOTE.md`](../../docs/EVOLVING_NETWORK_PROTOTYPE_V5_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the fixed v5 runner parameters and seeds, cross growth beats the recomputed KNN control on toward fraction and F~M, trails it on mean_delta, and therefore remains a mixed bounded prototype rather than a Gate B win.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-evolving-network-v5`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The frozen replay reports cross growth at 77.8% toward and F~M = 0.76 versus KNN at 66.7% toward and F~M = 0.66, while cross growth trails KNN on mean_delta by 0.000001.  _(class `C`)_
- **chain closes:** True — The note has no known dependencies, and the runner directly constructs the ordered, cross-growth, and KNN-control families from explicit constants and recomputes the reported metrics. The audit only closes the finite replay claim, not any broad Gate B dynamics theorem or independent comparison to v4.
- **rationale:** The current runner completed cleanly and reproduced the note's frozen table and pairwise read: cross growth improves toward fraction and F~M relative to KNN, but not mean_delta. The note's safe interpretation matches that output and explicitly avoids claiming a Gate B win. Residual risk is limited to the bounded prototype framing: it is a finite scripted replay over fixed parameters and seeds, not a general theorem about the dynamics.
- **auditor confidence:** high

### `ew_current_fierz_channel_decomposition_note_2026-05-01`

- **Note:** [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](../../docs/EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
- **claim_type:** `decoration`
- **claim_scope:** Algebraic SU(3) group-theory corollary: a fundamental-antifundamental pair decomposes as singlet plus adjoint, so the adjoint-channel dimension fraction is exactly 8/9 at N_c = 3; the EW matching rule (M) and full 9/8 correction are not ratified as derived.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_graph_first_su3_integration_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-judicial-panel-per-site-k1-20260523T142512Z-ew_current_fierz_channel_decomposition_n-majority`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** The adjoint-channel dimension fraction of the q-qbar Hilbert space is dim(adj)/dim(N_c tensor N_c-bar) = (N_c^2 - 1)/N_c^2, giving 8/9 at N_c = 3.  _(class `A`)_
- **chain closes:** False — Five-judge panel majority 4/5 ratified the second tuple (audited_decoration, decoration, class A). Vote breakdown: J1: second / audited_decoration / decoration / class A; J2: second / audited_decoration / decoration / class A; J3: first / audited_clean / positive_theorem / class A; J4: second / audited_decoration / decoration / class A; J5: second / audited_decoration / decoration / class A. Majority rationale: The load-bearing step is exact class-A representation algebra over the retained SU(3)/N_c = 3 input, with no external comparator and no tuned numerical input. The runner checks real SU(N) generator normalization, Fierz completeness, dimension counting, and citation hygiene, but it does not turn the algebraic corollary into an independent physical theorem. Under the rubric's clean-vs-decoration tie-break, the closed content is decoration of the retained SU(3) parent, while the matching rule (M) remains explicitly outside the audit scope. | The scoped claim is exact class-A algebra: Fierz completeness and the 1 plus adjoint decomposition over the retained SU(3) color structure. There are no external comparators or tuned inputs, and the note explicitly excludes the matching rule (M), so the physical 9/8 EW correction is not closed here. Under the tie-break rule, because the closed content reduces to standard mathematics applied to a single retained SU(3) parent, the proper terminal tuple is decoration rather than an independent positive-theorem clean result. | The load-bearing step is a standard algebraic representation-dimension identity over the retained SU(3) parent, with no external comparator and no tuned numerical input. The runner checks real SU(N) algebra, Fierz completeness, and the exact Fraction(8,9), but it does not make this an independent physical theorem. Because the note explicitly excludes deriving matching rule (M) and the closed content is only the algebraic channel fraction, the decoration verdict is the applicable tuple. | Both audits correctly identify the load-bearing step as class A and agree that the scoped channel-fraction claim closes while matching rule (M) remains outside the result. Under the rubric's tie-breaker, a zero-comparator algebraic corollary that reduces to retained SU(3) structure plus standard Fierz/representation algebra is decoration rather than a new positive theorem. The runner supports the algebra and citation hygiene but does not turn the standard dimension-count corollary into an independent first-principles computation.
- **rationale:** Five-judge panel majority 4/5 ratified the second tuple (audited_decoration, decoration, class A). Vote breakdown: J1: second / audited_decoration / decoration / class A; J2: second / audited_decoration / decoration / class A; J3: first / audited_clean / positive_theorem / class A; J4: second / audited_decoration / decoration / class A; J5: second / audited_decoration / decoration / class A. Majority rationale: The load-bearing step is exact class-A representation algebra over the retained SU(3)/N_c = 3 input, with no external comparator and no tuned numerical input. The runner checks real SU(N) generator normalization, Fierz completeness, dimension counting, and citation hygiene, but it does not turn the algebraic corollary into an independent physical theorem. Under the rubric's clean-vs-decoration tie-break, the closed content is decoration of the retained SU(3) parent, while the matching rule (M) remains explicitly outside the audit scope. | The scoped claim is exact class-A algebra: Fierz completeness and the 1 plus adjoint decomposition over the retained SU(3) color structure. There are no external comparators or tuned inputs, and the note explicitly excludes the matching rule (M), so the physical 9/8 EW correction is not closed here. Under the tie-break rule, because the closed content reduces to standard mathematics applied to a single retained SU(3) parent, the proper terminal tuple is decoration rather than an independent positive-theorem clean result. | The load-bearing step is a standard algebraic representation-dimension identity over the retained SU(3) parent, with no external comparator and no tuned numerical input. The runner checks real SU(N) algebra, Fierz completeness, and the exact Fraction(8,9), but it does not make this an independent physical theorem. Because the note explicitly excludes deriving matching rule (M) and the closed content is only the algebraic channel fraction, the decoration verdict is the applicable tuple. | Both audits correctly identify the load-bearing step as class A and agree that the scoped channel-fraction claim closes while matching rule (M) remains outside the result. Under the rubric's tie-breaker, a zero-comparator algebraic corollary that reduces to retained SU(3) structure plus standard Fierz/representation algebra is decoration rather than a new positive theorem. The runner supports the algebra and citation hygiene but does not turn the standard dimension-count corollary into an independent first-principles computation.
- **decoration parent:** `graph_first_su3_integration_note`
- **auditor confidence:** judicial_panel_majority

### `fermion_parity_pauli_tensor_involution_narrow_theorem_note_2026-05-10`

- **Note:** [`FERMION_PARITY_PAULI_TENSOR_INVOLUTION_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/FERMION_PARITY_PAULI_TENSOR_INVOLUTION_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The finite positive-N Pauli tensor-product identity that F=⊗_x σ_3^{(x)} is Hermitian unitary, involutive, has ±1 parity eigenspaces of dimension 2^{N-1}, anticommutes with one-site ladder operators, and commutes with number operators and σ_+^{(x)}σ_-^{(y)} bilinears.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e14bd-0dee-7c13-99cd-81a89a4afce1`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Given n̂_x=(I-σ_3^{(x)})/2 on H=⊗_{x=1}^N C², the tensor product F=⊗_x σ_3^{(x)} acts on each occupation basis state as (-1)^{∑_x ν_x}=exp(iπQ̂_total).  _(class `A`)_
- **chain closes:** True — The stated results follow directly from per-site Pauli algebra, tensor-product factorization, and the elementary even/odd binary-string count. No Hamiltonian, Noether conservation, physical fermion realization, or external comparator is imported inside the audited scope.
- **rationale:** The scoped theorem is a closed finite-dimensional Pauli-algebra identity. The runner checks the load-bearing identities exactly in the N=3 representative case and includes finite-N combinatorial spot checks; the general proof supplies the symbolic tensor-factor argument. Minor wording around deriving [F,n̂_x]=0 from the bilinear clause is harmless because the same Z_2-even conjugation applies directly to σ_-^{(x)}σ_+^{(x)}.
- **auditor confidence:** high

### `fifth_family_complex_boundary_note`

- **Note:** [`FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](../../docs/FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** On the finite sampled radial-shell fifth-family slice with drifts {0.05, 0.20, 0.30} and seeds {0, 1}, all six rows pass the Born/F~M gates and exactly the two drift=0.20 rows show TOWARD -> AWAY crossover.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260610-032427-c6e34d142c-fifth_family_complex_boundar`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner now computes Born/F~M gates for all six sampled rows and fails unless the sampled complex-companion set is exactly the drift-0.20 pair {(0.20, 0), (0.20, 1)}.  _(class `C`)_
- **chain closes:** True — The primary runner and included helpers construct the sampled geometry, radial-shell connectivity, source field, complex propagation, Born proxy, F~M gates, and crossover predicates directly. The cached output matches the note's table and there are no cited open dependencies or external comparators in the restricted packet.
- **rationale:** The runner source performs the load-bearing finite computation rather than merely printing constants: each row is measured from grow(), radial connectivity, source-field propagation, Born inclusion-exclusion, weak-source scaling, and sign crossover tests. The displayed table is consistent with the cached stdout: all Born values are below threshold, all F~M exponents lie within the stated gate, and only the two drift=0.20 rows have t01=1 and t05=0. The hard-coded expected companion set is used as a final assertion target after computing the rows, not as an input to produce the row values. The conclusion is correctly scoped to the sampled grid and does not claim family-wide closure.
- **auditor confidence:** high

### `fifth_family_complex_note`

- **Note:** [`FIFTH_FAMILY_COMPLEX_NOTE.md`](../../docs/FIFTH_FAMILY_COMPLEX_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the finite sampled claim that, on drifts [0.05, 0.20, 0.30] and seeds [0, 1], exactly rows (0.20, 0) and (0.20, 1) pass the Born/F~M gates and TOWARD -> AWAY crossover gate.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260611-141120-523f0f60de-fifth_family_complex_note`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The complex-action targeted runner computes Born/F~M gates and the TOWARD -> AWAY crossover on all six sampled radial-shell rows and finds exactly the drift-0.20 seed pair survives.  _(class `C`)_
- **chain closes:** True — The provided runner source builds the sampled grown geometry, radial-shell connectivity, source field, propagation amplitudes, Born proxy, F~M scaling proxies, and crossover flags rather than merely printing constants. The cached output matches the stated six-row table and assertion gate for the bounded sampled claim.
- **rationale:** The load-bearing step is a bounded first-principles computation within the provided framework runner and helper chain, not a renaming, external comparator, or tuned numerical match. The runner source includes the contested gates and asserts the exact companion set {(0.20, 0), (0.20, 1)} from computed row data. The cited radial authority is retained_bounded and the boundary authority is marked retained, so the restricted packet supplies retained-grade upstream support for the bounded sampled scope. No primitive-registry issue is relevant to this claim.
- **auditor confidence:** high

### `fifth_family_radial_boundary_note`

- **Note:** [`FIFTH_FAMILY_RADIAL_BOUNDARY_NOTE.md`](../../docs/FIFTH_FAMILY_RADIAL_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded certificate for the radial-shell family at drift=0.20, seed=0: exact zero-source and neutral cancellations plus the local plus/minus sign-orientation boundary; no wider radial-basin theorem is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260610-030715-d8cff47a7b-fifth_family_radial_boundary`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At drift=0.20, seed=0, the radial-shell row has exact zero/neutral controls but flips sign orientation with plus < 0, minus > 0, and a negative first-order orientation slope.  _(class `C`)_
- **chain closes:** True — The runner source constructs the deterministic grown row, radial-shell connectivity, source field, propagation, and detector-centroid observable, then computes the claimed signs. The separate certificate closes the zero/neutral exactness algebraically from field linearity and verifies the negative first-order orientation coefficient by differentiating the propagation recurrence.
- **rationale:** The primary runner is not print-only and does not hard-code the contested values; it computes the finite row from the supplied framework operators and asserts the local boundary signs. The helper certificate no longer depends on stdout substring replay: it imports the source-level certificate computation, checks exact zero/neutral cancellations, and computes the negative variational slope with finite plus/minus signs matching. The result is clean only at the bounded row/window stated in the note; the note correctly excludes a wider basin or corrected positive-orientation variant.
- **auditor confidence:** high

### `fifth_family_radial_fm_transfer_note`

- **Note:** [`FIFTH_FAMILY_RADIAL_FM_TRANSFER_NOTE.md`](../../docs/FIFTH_FAMILY_RADIAL_FM_TRANSFER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite two-row weak-field source-strength doubling check for the radial-shell fifth-family no-restore grown-slice rows (drift=0.05, seed=0) and (drift=0.30, seed=1).
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-125354-bf31ccd960-fifth_family_radial_fm_trans`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the two historically cited positive radial-shell rows, drift=0.05 seed=0 and drift=0.30 seed=1, the live weak-field mass-scaling replay gives near-unit F~M with passed rows 2/2 and mean F~M 0.999439.  _(class `C`)_
- **chain closes:** True — The runner source builds the no-restore grown slice, applies the radial-shell connectivity helper, propagates the free field and two positive source strengths, and computes the log2 centroid-shift exponent rather than reading the claimed F~M values. The one-hop radial packet is marked retained_bounded, and the note confines the conclusion to the sampled rows.
- **rationale:** The displayed source-note values match the completed cached runner output, and the provided source code shows an actual finite numerical computation rather than a print-only certificate or cross-note value import. The hard-coded target rows and tolerance define the bounded sampled scope; they do not hard-code the contested F~M results. The cited upstream authorities are retained-grade for audit purposes, and the note explicitly avoids family-wide, continuum, or physical mass-observable claims.
- **auditor confidence:** high

### `fifth_family_radial_note`

- **Note:** [`FIFTH_FAMILY_RADIAL_NOTE.md`](../../docs/FIFTH_FAMILY_RADIAL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite sampled radial-shell sweep for targets (0.05,0), (0.20,0), and (0.30,1) in scripts/FIFTH_FAMILY_RADIAL_SWEEP.py.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-120903-e9fa138c12-fifth_family_radial_note`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** In the no-restore grown-slice harness, the radial-shell fifth-family connectivity rule has two sampled rows, drift=0.05 seed=0 and drift=0.30 seed=1, satisfying the declared finite gates, with drift=0.20 seed=0 only an orientation boundary.  _(class `C`)_
- **chain closes:** True — The primary runner and helper sources construct the no-restore grown slice, radial-shell connectivity, source fields, propagation, and centroid readout, then compute the row gates rather than printing constants. Independent table arithmetic confirms two passing rows, drift coverage [0.05, 0.3], and the 0.20/0 boundary sign flip with zero and neutral controls clean.
- **rationale:** The load-bearing claim is bounded to three sampled rows and is directly supported by the completed cached run with source and transitive helper code present. The helper chain contains fixed harness parameters and target samples, but no external comparator, imported fitted value, or hard-coded contested output; the final assertions depend on computed gate values. The one-hop cited basin authority is marked retained_bounded, which is retained-grade under the rubric, and it is not needed to broaden the audited scope beyond the finite sweep.
- **auditor confidence:** high

### `fifth_family_radial_repaired_positive_packet_note_2026-05-29`

- **Note:** [`FIFTH_FAMILY_RADIAL_REPAIRED_POSITIVE_PACKET_NOTE_2026-05-29.md`](../../docs/FIFTH_FAMILY_RADIAL_REPAIRED_POSITIVE_PACKET_NOTE_2026-05-29.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite sampled audit of the repaired radial-shell fifth-family rule on drifts [0.05, 0.10, 0.20, 0.30, 0.40] and seeds [0, 1], plus F~M transfer on targets (0.05, 0) and (0.30, 1).
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-174909-156aa9a25b-fifth_family_radial_repaired`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** In the live no-restore grown-slice harness, the repaired radial-shell fifth-family connectivity rule has four sampled rows satisfying the declared finite controls and sign-orientation gates, and the two historically cited positive rows satisfy the dedicated F~M transfer check.  _(class `C`)_
- **chain closes:** True — The primary runner deterministically builds the no-restore grown slice, constructs radial-shell connectivity, propagates the declared weak source fields, and computes the zero, neutral, sign, and exponent gates for all ten rows. The companion F~M runner source computes the weak-field log-slope on the two target rows and asserts failure unless both pass.
- **rationale:** The restricted packet contains the primary runner source, transitive helper sources, and a completed status-ok cache whose reported pass set matches the note's bounded claim. The load-bearing computation is not a definition, renaming, external comparator, or tuned numerical match: it instantiates the declared harness and computes the sampled row outcomes from the supplied code path. Independent formula checks on the displayed gate logic confirm that zero-source and neutral cancellation are structurally exact, the four positive rows have the required plus/minus orientation and exponent tolerance, and the cited boundary row is a sign-orientation miss rather than a control leak.
- **auditor confidence:** high

### `fine_h_family_universality_note`

- **Note:** [`FINE_H_FAMILY_UNIVERSALITY_NOTE.md`](../../docs/FINE_H_FAMILY_UNIVERSALITY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite H=0.25 replay over Fam1/Fam2/Fam3 seeds 0-4 gives all 15 slope fits in [-1.474,-1.353], family means -1.399/-1.429/-1.385, grand mean -1.404, population sigma 0.036, and Fam2-vs-Fam3 t=2.375.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The fine-H lensing slope is portable across three DAG families within the -1.38 to -1.43 band, with a possible residual Fam2/Fam3 offset (t=2.37) that needs more seeds to resolve.  _(class `C`)_
- **chain closes:** True — The source note has no upstream dependencies, and the registered runner cache now replays the full 3-family x 5-seed finite computation with the same slopes, family summaries, and pairwise t-statistics. The audited scope is the bounded finite replay only, not geometry-independence or an independent eikonal-baseline derivation.
- **rationale:** The runner constructs the three fixed drift/restore DAG families, evaluates seeds 0-4 at H=0.25 and b in {3,4,5,6}, computes the Kubo readout, fits the per-seed and seed-mean power laws, and emits the same family means, grand mean, population sigma, and Fam2-vs-Fam3 t-statistic reported in the note. The note's retained boundary is explicitly three-family portability with a borderline residual family offset, not universality or kernel-independence. Within that bounded finite scope there is no hidden dependency, stale number, timeout, or imported comparator needed for closure.
- **auditor confidence:** high

### `finite_cell_two_band_closed_form_bounded_theorem_note_2026-06-13`

- **Note:** [`FINITE_CELL_TWO_BAND_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-13.md`](../../docs/FINITE_CELL_TWO_BAND_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-13.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fixed supplied free staggered two-band Harper cell Q=24, Ly=2, t=1, mu=1.7086, T=0.2, with the implemented finite-cell Peierls B^2 perturbation; the audited claim is equality of the finite momentum closed form and direct finite real-space Harper perturbation, not a continuum-Moyal theorem.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-023644-3b04cce6-finite_cell_two_band_closed_form_bounded_theorem_note_2026-06-13-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The Peierls variations are the exact finite Fourier sums X_nm and X2_nm inserted into the finite-dimensional divided-difference formula, giving the same B^2 response as the direct real-space Harper perturbation calculation on the fixed cell.  _(class `C`)_
- **chain closes:** True — The runner source constructs the closed-form block calculation from explicit finite Fourier sums and separately constructs real-space Harper H0,H1,H2 perturbation matrices, with no hard-coded response constants. The completed cache shows agreement to 1e-10, a B-halving finite-difference discriminator, nonzero massive interband terms, and the Moyal comparator is explicitly non-load-bearing.
- **rationale:** The bounded finite-cell theorem closes within the supplied model and fixed parameters: the load-bearing response is computed from the finite Hamiltonian and Peierls perturbation rather than imported from another note or fitted to stored expected values. The direct real-space perturbation path is an independent implementation of the same finite object, and the finite-difference check tests the B^2 response behavior. The continuum-Moyal material is scoped as a bounded comparator and residual, so it does not broaden the audited conclusion.
- **auditor confidence:** high

### `finite_rank_gravity_residual_helper_note_2026-04-14`

- **Note:** [`FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md`](../../docs/FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Exact finite-rank Woodbury/Dyson source renormalization and exterior-field construction for supplied finite-rank lattice data H_0, P, and W, with no audit of the origin of P,W or downstream 3+1 gravity closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-023644-3b04cce6-finite_rank_gravity_residual_helper_note_2026-04-14-second`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The exact Woodbury/Dyson identity gives G_W P = G_0 P (I - W G_S)^(-1), hence q_eff = (I - W G_S)^(-1)m and phi = G_0 P q_eff.  _(class `A`)_
- **chain closes:** True — The Woodbury identity follows algebraically for the supplied finite-dimensional operator data when the displayed inverses exist. The runner genuinely constructs the matrices and checks the column identity, compressed source formula, and exterior harmonicity rather than hard-coding the contested result.
- **rationale:** The load-bearing step is a standard algebraic finite-rank resolvent identity over the stated inputs, and the note explicitly bounds away from deriving the support structure or full gravity theorem. The primary runner independently builds the lattice Laplacian, support projector, finite-rank W, and verifies the exact identities to numerical precision, with additional bounded diagnostic residual tests. The current runner residual values differ from the prose's quoted historical residual, so a second auditor should treat that quote as a non-load-bearing stale verification detail rather than part of the theorem closure.
- **auditor confidence:** high

### `finite_rank_source_to_metric_theorem_note`

- **Note:** [`FINITE_RANK_SOURCE_TO_METRIC_THEOREM_NOTE.md`](../../docs/FINITE_RANK_SOURCE_TO_METRIC_THEOREM_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fixed 15^3 Dirichlet finite-lattice certificate for the runner-defined seven-site finite-rank source, exterior harmonic/Schur boundary algebra, shell-averaged radial harmonic projection, and bounded static isotropic residual reduction.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-gpt-5.5-fresh-2026-05-27-darwin-2nd`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** On the fixed 15^3 Dirichlet lattice, with the seven-site support and finite-rank matrix defined in the runner, the finite-rank source reproduces the exterior field and its shell-averaged radial harmonic projection gives a bounded static isotropic residual reduction.  _(class `C`)_
- **chain closes:** True — The runner locally constructs the Laplacian, support projector, Woodbury finite-rank solve, Schur DtN matrix, radial projection, and finite-difference static isotropic residual diagnostic without helper imports or dependencies. The META pass lines are excluded from the scientific chain because they only check transient audit ledger/queue state and are not load-bearing physics.
- **rationale:** Within the explicitly bounded scope, the conclusion follows from the self-contained finite computation: the finite-rank identities close to machine precision, exterior harmonicity and Schur stationarity are computed directly, and the radial harmonic projection produces the stated residual reduction. The note explicitly excludes full nonlinear GR, continuum limits, universal source-to-metric claims, tensorial 3+1 matching, and derivation of the support choice, so those unclosed extensions are not part of the audited claim. The 8 META lines are a non-load-bearing runner artifact to ignore for scientific closure, not a blocker.
- **auditor confidence:** high

### `fixed_field_complex_grown_basin_v2_note`

- **Note:** [`FIXED_FIELD_COMPLEX_GROWN_BASIN_V2_NOTE.md`](../../docs/FIXED_FIELD_COMPLEX_GROWN_BASIN_V2_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited only the runner-defined two-row tiny basin: center drift=0.20 restore=0.70 with retained companion support, plus neighbor drift=0.20 restore=0.60 for seed 0 crossover and weak-field F~M checks.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260512-000558-b0c4bc75-fixed_field_complex_grow-015`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The row-table runner shows the center row remains clean and the immediate neighbor at drift=0.20, restore=0.60 keeps TOWARD at gamma=0.1, AWAY at gamma=0.5, and weak-field F~M=1.000.  _(class `C`)_
- **chain closes:** True — The cited companion authority is retained-bounded for the center row, and the provided runner computes the neighbor row directly using the grown-geometry propagation machinery rather than printing fixed constants. Within the stated seed-0, two-row scope, the row table supports the selective tiny-basin positive claim.
- **rationale:** The load-bearing neighbor result is a direct runner computation from the framework functions, with selected rows and seed fixed in advance by the note. The center-row exact reduction is explicitly delegated to a retained-bounded cited authority, while the current runner verifies the center Born/F~M checks and the nearby crossover/F~M survival. The claim is narrow and does not assert family-wide transfer, continuum closure, or self-gravity.
- **auditor confidence:** high

### `fixed_field_family_unification_note`

- **Note:** [`FIXED_FIELD_FAMILY_UNIFICATION_NOTE.md`](../../docs/FIXED_FIELD_FAMILY_UNIFICATION_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Seed-0 fixed-field comparison on the retained grown row drift=0.2, restore=0.7, h=0.5: signed-source zero/neutral/linear sign response and complex-action gamma=0, gamma=0.2, and gamma=0.5 metrics on the same connectivity family, with no geometry-generic or continuum claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T115723Z-a7653ed2-fixed_field_family_unifi-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The same retained grown row supports both the signed-source companion and the exact gamma=0 complex-action companion under the same fixed-field connectivity slice.  _(class `C`)_
- **chain closes:** True — Both cited authorities are retained-grade, and the included runner source recomputes both branches from the same grow(drift=0.2, restore=0.7, seed=0) geometry rather than hard-coding the reported values. The cached runner output matches the source note's frozen table and stays within the note's stated narrow scope.
- **rationale:** The primary runner instantiates the grown geometry and propagation rules, then computes the signed-source and complex-action summaries on the same row. The helper sources are included and do not import contested numeric conclusions or print constants as proof. The conclusion is only the compact same-row unification of two retained narrow companions, not a geometry-generic theorem.
- **auditor confidence:** high

### `fixed_field_grown_transfer_scout_note`

- **Note:** [`FIXED_FIELD_GROWN_TRANSFER_SCOUT_NOTE.md`](../../docs/FIXED_FIELD_GROWN_TRANSFER_SCOUT_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited only the runner-defined retained grown row at drift=0.2, restore=0.7, seed=0, fixed-field propagation with the listed signed-source cases and zero/neutral controls.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260512-000558-b0c4bc75-fixed_field_grown_transf-016`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The retained grown row preserves a bounded signed-source response in the fixed-field scout while zero-source and neutral same-point controls reduce to printed zero and the +2 source is approximately linear in the +1 source.  _(class `C`)_
- **chain closes:** True — The supplied runner actually constructs fields from sources, propagates amplitudes on the grown graph, computes detector centroids, and reproduces the frozen sign, zero-control, and linearity outputs. The cited grown-geometry companion is retained_bounded and is used only to support the narrow retained-row context, not to broaden the result.
- **rationale:** The load-bearing result is a live numerical computation over the runner-defined grown row, not a printed constant, renaming, or imported external comparator. The zero-source and neutral same-point cancellations are algebraic/numerical controls, while the signed single-source, pair, dipole, and double-source cases are computed by the propagation code. The claim is narrow enough to match the evidence: it does not assert geometry-generic electromagnetism or continuum closure.
- **auditor confidence:** high

### `flavor_center_trace_closed_capstone_note_2026-05-30`

- **Note:** [`FLAVOR_CENTER_TRACE_CLOSED_CAPSTONE_NOTE_2026-05-30.md`](../../docs/FLAVOR_CENTER_TRACE_CLOSED_CAPSTONE_NOTE_2026-05-30.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Reduced exact-support packet for the finite D3+C3 algebra, invariant coordinate subsets, tracial singlet/doublet populations, dephasing preservation, and non-restoration of the historical center-trace closure claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-175321-643bdc3cac-flavor_center_trace_closed_c`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The coordinate projectors together with the C3 cycle generate M3(C), so the tracial carrier rho=I3/3 gives singlet/doublet populations 1/3 and 2/3 while equal central-atom weighting would be an extra selector.  _(class `A`)_
- **chain closes:** True — Independently, P_i C^k P_j gives matrix units, so the generated algebra is M3(C) and the only C3-invariant coordinate subsets are empty/full. Since Ps has rank 1 and Pd rank 2, rho=I3/3 gives weights 1/3 and 2/3, and block dephasing preserves those traces; the physical observable-algebra bridge is explicitly outside scope.
- **rationale:** The load-bearing step is finite-dimensional algebra and trace bookkeeping, not a definition, renaming, numerical match, or external comparator check. The runner source actually computes the projector, generation, invariant-subset, trace, and dephasing checks, while its remaining checks are ledger/cache consistency checks. This clean verdict applies only to the narrowed exact-support packet and does not restore the old center-trace route closure or upgrade the retained_bounded pre-record identification.
- **open / conditional deps cited:**
  - `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`
- **auditor confidence:** high

### `flavor_doublet_metric_default_is_detr_2026-06-02`

- **Note:** [`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`](../../docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite C3 circulant HS metric calculation on (a, Re b, Im b), with conditional det_R/det_C arithmetic and two narrow route-pruning checks.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260606-233523-9c86a8a511-flavor_doublet_metric_defaul`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the C3 circulant coefficient surface (a, Re b, Im b), the Hilbert-Schmidt/coherent-state metric is diag(3,6,6), and the metric is reading-neutral.  _(class `C`)_
- **chain closes:** True — Using C^3=I, C†=C^2, tr(C)=tr(C^2)=0, the independent trace calculation gives <I,I>=3 and <C+C^2,C+C^2>=<i(C-C^2),i(C-C^2)>=6 with zero cross terms. The det_R/det_C arithmetic and the two stated obstructions then follow algebraically within the packet's bounded scope.
- **rationale:** The runner source genuinely instantiates the C3 shift matrix and computes the HS Gram matrix rather than merely printing expected constants. An independent trace audit confirms the displayed diag(3,6,6), the conditional r and Q readings, the Hermitian-observable obstruction for multiplication by i, and the discrete-only rephasing condition e^{3i alpha}=1. The note does not promote a det_R default, exclude all field-space complex structures, or claim a physical mass readout theorem, so the bounded conclusion closes as stated.
- **auditor confidence:** high

### `flavor_r_half_is_a_stationary_point_not_forced_2026-06-02`

- **Note:** [`FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md`](../../docs/FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Given the displayed r-family definitions and Q(r)=1/3+(2/3)r, r=1/2 is the sector-entropy maximum, imbalance trough, and r->1-r fixed point, with r=0,1/2,1 mapping to Q=1/3,2/3,1 respectively.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260603-011524-d1f74344-flavor_r_half_is_a_stati`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The sector-power entropy S(r) with p_singlet=1/(1+2r) and p_doublet=2r/(1+2r) is maximized at r=1/2, equivalently the singlet-doublet imbalance is zero there.  _(class `A`)_
- **chain closes:** True — The entropy statement reduces to the binary entropy maximum at equal sector weights, which gives 1/(1+2r)=2r/(1+2r) and hence r=1/2. The Q-table entries and imbalance/fixed-point claims are direct algebraic substitutions; the broader lane-assignment dynamics is explicitly outside the audited scope.
- **rationale:** The displayed closed-form identities check out under the note's own definitions: S(r) has its unique interior maximum at r=1/2, the imbalance |3-6r| vanishes there, and the listed Q values follow by substitution. The per-DOF caveat is also consistent with equal per-DOF weights giving r=1. This is a bounded algebraic/calculus closure, not a derivation of the physical lane assignment or charged-lepton sector selection.
- **auditor confidence:** high

### `flavor_readout_gate_equals_carrier_identification_2026-05-31`

- **Note:** [`FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md`](../../docs/FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md)
- **claim_type:** `open_gate`
- **claim_scope:** Audited only the finite C3 algebra support and the bookkeeping identification that the readout, carrier, and basepoint choices are one open gate; not a derivation of the physical charged-lepton flavor observable.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-hygiene-cycle-break-20260707-193821-5b3b16-flavor_readout_gate_equals_carri-16`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The readout gate, generation-carrier identification, and zero-section/basepoint pick are the same single remaining physical carrier/basepoint premise, not an independently derived closure.  _(class `F`)_
- **chain closes:** False — The finite algebraic negatives close, including the fixed-line result and J_cs silence on r. The asserted equality of the three gates is an identification/renaming of open premises, and the packet does not derive the physical carrier/basepoint premise from baseline plus retained inputs.
- **rationale:** The runner performs real finite algebra checks, but the row's load-bearing disposition is not a first-principles derivation of the observable. Its central move is to identify three named unresolved choices as one remaining gate, which is class F rather than class C. The note correctly scopes itself as open_gate and forbids retained-derivation use, so the proper audit disposition is renaming/open-gate bookkeeping rather than clean closure.
- **open / conditional deps cited:**
  - `FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md`
- **auditor confidence:** high

### `flavor_spin_statistics_forces_modulo_reconstruction_2026-05-31`

- **Note:** [`FLAVOR_SPIN_STATISTICS_FORCES_MODULO_RECONSTRUCTION_2026-05-31.md`](../../docs/FLAVOR_SPIN_STATISTICS_FORCES_MODULO_RECONSTRUCTION_2026-05-31.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The supplied finite spinor construction has bounded CAR occupation and an indefinitely descending wrong-Bose energy direction, while the tested kernel and two-site qubit carrier do not themselves select cross-site CAR.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T015154Z-1f0c3329-00429-flavor_spin_statistics_force`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Ordinary two-site qubit ladders commute, Jordan-Wigner-dressed generators anticommute only after a generator/string choice, and the checked free kernel does not encode that statistics choice.  _(class `A`)_
- **chain closes:** True — The runner directly computes the stated finite spectra and matrix relations, and its explicit occupation formula establishes the descending Bose direction for arbitrary truncation. These results close the deliberately bounded construction and statistics-selection statement, without asserting a reconstruction of P1 from the full framework.
- **rationale:** The runner performs genuine finite algebra rather than printing expected constants: it constructs the occupation spectra, taste tensor product, kernel identity, two-site ladder relations, and Pauli Casimir. The source accurately limits the conclusion to those constructions and to route pruning; it expressly withholds a reconstruction theorem and any promotion of P1/CAR. Within that bounded scope, the conclusions follow from the displayed algebra.
- **auditor confidence:** high

### `fm_transfer_note`

- **Note:** [`FM_TRANSFER_NOTE.md`](../../docs/FM_TRANSFER_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** Mass-law transfer agrees within uncertainty on the retained grown-row neighborhood (drift=0.2, restore=0.7).  _(class `C`)_
- **chain closes:** True — The live runner recomputes the fixed-lattice F~M exponent, six grown-seed F~M exponents at drift=0.2 and restore=0.7, their mean/spread, and the fixed-grown sigma comparison. The note explicitly excludes geometry-generic transfer, other drift/restore values, and other observables.
- **rationale:** The claim is a bounded numerical computation, not a broad universality theorem: the current runner reproduces the frozen fixed exponent, all six grown-seed exponents, the grown aggregate, and the 0.3 sigma fixed-grown comparison. The source note keeps the conclusion on the specified grown row and explicitly does not claim other geometries, drift/restore values, or observables. Residual boundary: the quoted uncertainty is the finite six-seed grown spread used by the runner, so the retained content is only this finite transfer check.
- **auditor confidence:** high

### `fourth_family_quadrant_note`

- **Note:** [`FOURTH_FAMILY_QUADRANT_NOTE.md`](../../docs/FOURTH_FAMILY_QUADRANT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite quadrant-reflection connectivity sweeps on the grown slice exhibit a nonempty but seed/drift-limited signed-source basin with zero-source, neutral-cancellation, sign-orientation, and near-linear charge-scaling controls.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-second-fourth_family_quadrant_note-20260505`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The quick diagnostic sweep gives a real but narrow basin, not a family-wide closure.  _(class `C`)_
- **chain closes:** True — The cached current runner completes and computes the quadrant-reflection connectivity, source propagation, detector centroid shifts, and row gate rather than printing preset outcomes. It confirms a nonempty narrow basin: the note's quick subset has 5/9 passing rows and the current full default sweep has 23/45 passing rows, so the bounded non-universal claim closes.
- **rationale:** The load-bearing claim is bounded to existence of a narrow computational basin, not family-wide or geometry-generic closure. The runner constructs the quadrant-reflection adjacency rule, evaluates zero, plus, minus, neutral, and double-source responses, and counts passing rows under explicit gates; it does not hard-code the pass count or target response signs. The note overstates the representative drift=0.50 quick row as mostly passing, but that wording is not needed for the audited bounded conclusion and the current runner output still supports the stated safe read. Residual risk is limited to the unexpanded imported grown-slice generator, which was not a listed one-hop note in the restricted packet.
- **auditor confidence:** medium

### `g_bare_constraint_vs_convention_restatement_abstract_identity_narrow_theorem_note_2026-05-10`

- **Note:** [`G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Standalone polynomial-algebra theorem over positive real abstract variables (g, beta, K) satisfying beta*g^2 = K: the zero-, one-, and two-axis admission cases have respectively two, one, and zero free parameters, so constraint-vs-convention status depends on admission rank. No physical bare-coupling, Wilson-action, Cl(3), SU(N_c), Gell-Mann normalization, comparator, or framework-specific admission-rank claim is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The constraint-vs-convention status of g or beta is a function of the admission rank r: with r = 1 the remaining variables lie on a one-parameter convention curve, while with r = 2 the remaining variable is uniquely forced by beta*g^2 = K.  _(class `A`)_
- **chain closes:** True — The proof is elementary algebra over R_{>0}: solve beta*g^2=K under each admission specialization and count the resulting free parameters. The runner verifies the symbolic identities and exact rational witnesses with PASS=52, FAIL=0, and the note has no load-bearing dependencies.
- **rationale:** The scoped theorem closes because every claimed case follows directly from the single relation beta*g^2=K over positive reals: K alone leaves a one-parameter curve, fixed K and beta or fixed K and g gives a unique positive solution for the third variable, and no admissions leave a two-parameter surface. The runner checks the symbolic substitutions, exact rational samples, dimension count, round trips, and negative examples without importing any physical interpretation. Residual risk is scope drift only: this audit does not ratify any physical claim that g_bare=1 is forced in the lattice gauge setting.
- **auditor confidence:** high

### `g_bare_forced_by_ward_rep_b_independence_abstract_narrow_theorem_note_2026-05-10`

- **Note:** [`G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_ABSTRACT_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_ABSTRACT_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Standalone polynomial-algebra forcing identity over abstract variables (F, g, N, c0): simultaneous constraints F^2=c0 and F^2=g^2/(2N) imply g^2=2Nc0, with unique positive branch g=sqrt(2Nc0) for c0>0; the (N,c0)=(3,1/6) case yields g=1 and alternative pairs yield different values. No Ward identity, lattice gauge theory, Wilson action, Cl(3), Z^3 substrate, SU(N_c), physical bare-coupling identification, comparator, or framework-specific premise is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Equating the two abstract constraints F^2 = c0 and F^2 = g^2/(2N) gives g^2 = 2 N c0, so on the positive branch g = sqrt(2 N c0) when c0 > 0.  _(class `A`)_
- **chain closes:** True — The theorem follows by direct substitution and multiplication by 2N over the stated positive-real domain, with the c0=0 boundary explicitly excluded by g>0. The runner verifies the symbolic identity, positive branch, rational instances, non-unit counterexamples, and scope disclaimers with PASS=39, FAIL=0.
- **rationale:** The scoped claim closes as pure algebra: the two hypotheses give c0 = g^2/(2N), hence g^2 = 2Nc0, and the positive branch is unique for c0>0. The specific g=1 result is correctly limited to pairs satisfying 2Nc0=1, with the note and runner showing that other pairs such as (N,c0)=(1,1) force different values. This audit does not ratify the physical Ward-route premises or any claim that those abstract variables are fixed by Cl(3), Wilson, or SU(N_c) structure.
- **auditor confidence:** high

### `gate_b_grown_distance_law_note`

- **Note:** [`GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](../../docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded replay of the exact-grid versus moderate-drift grown-geometry distance-law tail on the runner-defined h=0.5, W=10, L=12, four-seed, z=3..7 family.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-005357-f2a031da-gate_b_grown_distance_la-002`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The frozen log reports that exact grid and grown drift=0.2 both give 20/20 TOWARD tails with comparable declining fits, b^(-0.90) and b^(-0.83), over z=3..7.  _(class `C`)_
- **chain closes:** True — The provided runner source directly constructs the exact and grown geometries, propagates amplitudes, computes mean detector shifts, fits the positive post-peak tail, and emits the numbers cited in the note. Within the narrow runner-defined family, no cited upstream authority is needed.
- **rationale:** The source note makes a bounded numerical claim about a specific harness result, and the included runner code is not a constant-printing script or cross-note value import. It performs the geometry growth, propagation, field perturbation, delta aggregation, and log-log tail fit that its stdout reports. The conclusion is therefore clean only for the stated finite tested family, not for broader Gate B closure or all generated-geometry parameter space.
- **auditor confidence:** high

### `gate_b_grown_trapping_frontier_note`

- **Note:** [`GATE_B_GROWN_TRAPPING_FRONTIER_NOTE.md`](../../docs/GATE_B_GROWN_TRAPPING_FRONTIER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** the detector-layer frontier bias rises steadily with eta while eta = 0 reproduces the grown baseline exactly, so the trap is doing more than simple attenuation on the tested row.  _(class `C`)_
- **chain closes:** True — The live runner recomputes the declared eta sweep on the drift=0.2, restore=0.7 row, including exact eta=0 reduction, falling escape, and monotone frontier-bias increase. The note explicitly limits the result to a bounded transport observable and excludes horizon theory, bidirectional field equations, and generated-family transfer.
- **rationale:** The finite bounded positive closes through the current runner: eta=0 is the baseline by construction, escape falls monotonically from 0.919 to 0.557 over the nonzero eta sweep, and frontier_bias rises monotonically from +0.0227 to +0.1509. The source does not claim a horizon theory, generated-family transfer, or general field equation, so the retained content is only this transport/frontier observable on the specified grown row. Residual boundary: the frozen log path named in the note is missing from the repo, but the live runner fully recomputes the table and is the load-bearing artifact here.
- **auditor confidence:** high

### `gate_b_grown_trapping_frontier_v2_note`

- **Note:** [`GATE_B_GROWN_TRAPPING_FRONTIER_V2_NOTE.md`](../../docs/GATE_B_GROWN_TRAPPING_FRONTIER_V2_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** the escape ratio falls steadily as eta grows while frontier_radius_shift rises steadily, so surviving detector mass is pushed outward on the detector shell.  _(class `C`)_
- **chain closes:** True — The live runner recomputes the eta sweep on the declared grown row, including exact eta=0 reduction, monotone escape attenuation, and monotone outward frontier-radius shift. The source note limits the result to a bounded transport/frontier probe and excludes horizon theory, bidirectional field equations, and generated-family transfer.
- **rationale:** The bounded positive closes through the current runner: eta=0 reproduces the baseline, escape decreases from 0.919 to 0.557 over the nonzero eta sweep, and frontier_radius_shift increases from +0.0684 to +0.4480. The note keeps the claim on this finite transport/frontier observable and does not promote a horizon theory or generated-family transfer. Residual boundary: the frozen log path named in the note is missing, but the live runner fully recomputes the table and is the load-bearing artifact here.
- **auditor confidence:** high

### `gate_b_grown_trapping_frontier_v3_note`

- **Note:** [`GATE_B_GROWN_TRAPPING_FRONTIER_V3_NOTE.md`](../../docs/GATE_B_GROWN_TRAPPING_FRONTIER_V3_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The new structural target is the shell-contrast shift, and it also rises steadily with trap coupling while eta = 0 reproduces the retained grown baseline exactly.  _(class `C`)_
- **chain closes:** True — The live runner recomputes the declared eta sweep on the grown row, including the exact eta=0 reduction, monotone escape attenuation, positive frontier-radius shift, and monotone frontier-shell-contrast shift. The note limits the result to this bounded frontier probe and excludes horizon theory, generated-family transfer, bidirectional field equations, and force-law claims.
- **rationale:** The bounded positive closes through the current runner: eta=0 reproduces the baseline, escape decreases monotonically across the nonzero eta sweep, frontier_radius_shift remains positive and rising, and frontier_shell_contrast_shift rises monotonically. The promoted observable in the note is the same detector-layer shell-contrast observable computed by the runner. The claim is not promoted beyond this finite shell-structure probe, and the note explicitly declines horizon theory, generated-family transfer, and force-law claims. Residual boundary: the frozen log path named in the note is missing, but the live runner fully recomputes the table and is the load-bearing artifact here.
- **auditor confidence:** high

### `gate_b_grown_trapping_transport_note`

- **Note:** [`GATE_B_GROWN_TRAPPING_TRANSPORT_NOTE.md`](../../docs/GATE_B_GROWN_TRAPPING_TRANSPORT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The exact zero-coupling reduction passes, and the escape observable is bounded and monotone in the tested sweep.  _(class `C`)_
- **chain closes:** True — The live runner recomputes the declared grown-row eta sweep, reproducing eta=0 escape exactly and the monotone fall in detector escape across the five nonzero trap couplings. The source note limits the result to a bounded trap-sensitive transport probe and explicitly excludes horizon theory, a general bidirectional field equation, and generated-family transfer.
- **rationale:** The bounded positive closes through the current runner and frozen log: eta=0 returns escape=1.000, while the aggregate escape ratio falls monotonically from 0.799 at eta=0.05 to 0.205 at eta=0.50 on the declared grown row and trap slab. The note promotes only the detector escape ratio, which is exactly the observable computed by the runner. No cited dependency is needed for this finite computation, and the note does not claim a horizon theory, generated-family transfer, or general field equation. Residual boundary: the result remains a bounded transport probe for this row, static field, trap geometry, seeds, and eta sweep.
- **auditor confidence:** high

### `gate_b_local_stencil_connectivity_bridge_bounded_theorem_note_2026-06-18`

- **Note:** [`GATE_B_LOCAL_STENCIL_CONNECTIVITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md`](../../docs/GATE_B_LOCAL_STENCIL_CONNECTIVITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-runner theorem that `GB-S3a` closes as a finite-range local forward stencil on the supplied finite Z^3 Gate B slab, exactly matching `gate_b_connectivity_tolerance._build_fixed_connectivity`, with one-layer advancement, transverse offsets in {-1,0,1}^2, interior translation covariance, and boundary clipping only; no physical growth dynamics, KNN/generated graph selection, scalar normalization, propagation/readout semantics, TOWARD/F~M physical readout, Gate B dynamics closure, or physical gravity theorem is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-2026-07-09-gate-b-local-stencil`  (codex-current; independence=cross_family)
- **load-bearing step:** The fixed Gate B forward adjacency is exactly the finite stencil S={(1,dy,dz): dy,dz in {-1,0,1}} clipped to the finite Z^3 slab, and it matches the helper runner adjacency.  _(class `A`)_
- **chain closes:** True — The primary verifier independently reconstructs the theorem adjacency and compares it exactly to the declared helper runner's fixed connectivity. The runner's historical axiom-wording check is not load-bearing for the finite adjacency equality; current scope is the explicit finite Z^3 stencil algebra.
- **rationale:** The primary runner returns TOTAL PASS=13 FAIL=0 and verifies exact equality between the theorem stencil and helper adjacency, finite graph-distance range, one-layer forward foliation, bounded out-degree, translation-covariant interior offsets, and boundary clipping. The helper source required by the note is present and inspectable, and the source/parent boundary checks preserve the `GB-S3a`/`GB-S3b` split. The result is a clean finite adjacency theorem only; physical selection or dynamical generation of the stencil remains open.
- **auditor confidence:** high

### `gate_b_no_restore_joint_package_note`

- **Note:** [`GATE_B_NO_RESTORE_JOINT_PACKAGE_NOTE.md`](../../docs/GATE_B_NO_RESTORE_JOINT_PACKAGE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Single-seed bounded replay of the runner-defined exact-grid and restore=0 grown-geometry rows at drift values 0.0, 0.2, and 0.5 for Born I3, d_TV, MI, and CL-bath decoherence.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260608-110739-a0f830a382-gate_b_no_restore_joint_pack`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The one-seed replay reports the exact-grid row and no-restore drift rows at 0.0, 0.2, and 0.5 with the listed Born, d_TV, MI, and decoherence values, showing exact-grid reproduction at zero drift and sensitivity at nonzero drift.  _(class `C`)_
- **chain closes:** True — The runner source constructs the finite geometry from fixed parameters and seed, propagates amplitudes, computes the four metrics, and the verifier compares every rounded frozen row against the completed recompute certificate. Independent checks of the displayed table confirm the exact-grid/no-restore-zero identity, the stated tolerances, and the bounded metric ranges.
- **rationale:** The source is scoped as a bounded one-seed replay, not a general generated-geometry closure. The runner is not a constant printer: its recompute path builds the lattice, applies the propagation rule, and computes the reported metrics without importing a cited contested value or external comparator. The frozen values match the recomputed rows within the stated tolerances, and the safe interpretation is limited to the displayed drift rows.
- **auditor confidence:** high

### `gate_b_nonlabel_sign_grown_transfer_note`

- **Note:** [`GATE_B_NONLABEL_SIGN_GROWN_TRANSFER_NOTE.md`](../../docs/GATE_B_NONLABEL_SIGN_GROWN_TRANSFER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Seed-0 finite-runner transfer test for label-grown control and position-based geometry-sector candidate on the retained-bounded grown row with drift=0.2, restore=0.7, h=0.5.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T113119Z-61456fef-gate_b_nonlabel_sign_gro-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Both the label-grown control family and the geometry-sector candidate family satisfy the zero/neutral, antisymmetry, nonzero signal, sign-orientation, and charge-linearity PASS/FAIL checks on the retained-bounded grown row.  _(class `C`)_
- **chain closes:** True — The cited grown-distance-law authority is retained_bounded and supplies the bounded grown row. The primary runner and included helper source instantiate the grown geometry, source field, propagation, detector centroid, and transfer checks directly rather than replaying hard-coded expected values.
- **rationale:** The load-bearing evidence is the completed runner output with PASS=14 FAIL=0, supported by source code that actually computes the quantities under test. The only one-hop cited authority is retained_bounded and is used narrowly to identify the grown-row construction and parameters. The claim remains bounded to this seed-0 finite-runner row and does not establish a family-wide replacement or general geometry-sector theory.
- **auditor confidence:** high

### `gauge_scalar_temporal_completion_theorem_note`

- **Note:** [`GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md`](../../docs/GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact temporal-completion ratio for the accepted Wilson nearest-neighbor local bosonic scalar gauge-source class with one uniform plaquette weight on the minimal APBC 3 spatial + 1 derived-time block.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T133506Z-79b61050-gauge_scalar_temporal_co-01`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Every accepted source reduces exactly to K_O(omega) = 3w (3 + sin^2 omega), so the normalization cancels and A_O(inf) / A_O(2) = 2 / sqrt(3).  _(class `A`)_
- **chain closes:** True — Within the stated Wilson nearest-neighbor source grammar, the six plaquette orientations induce equal directional weights and the minimal APBC spatial cube gives three unit spatial gaps, yielding K_O(omega) = 3w(3 + sin^2 omega). The endpoint ratio then follows algebraically from the Lt=2 sum and the standard infinite-time trigonometric average; no downstream plaquette-observable closure is claimed.
- **rationale:** The audited claim is narrow: universality only inside the accepted Wilson nearest-neighbor scalar gauge-source grammar, excluding anisotropic terms, site terms, unrelated source classes, and the interacting plaquette expectation. The load-bearing step is a combinatorial/algebraic reduction of that scoped grammar, not a definition substitution or external numerical match. The runner checks the Wilson orientation count, induced directional equality, minimal-cube kernel reduction, normalization independence, and sensitivity to forbidden deformations; it uses no external comparators.
- **auditor confidence:** high

### `gauge_scalar_temporal_observable_bridge_implicit_flow_theorem_note_2026-05-03`

- **Note:** [`GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_IMPLICIT_FLOW_THEOREM_NOTE_2026-05-03.md`](../../docs/GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_IMPLICIT_FLOW_THEOREM_NOTE_2026-05-03.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-volume implicit response-coordinate identity and susceptibility-flow law under the stated monotonicity and in-range premises; not an evaluated beta=6 plaquette or independent parent bridge derivation.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-gauge_scalar_temporal_observable_bridge_implicit_flow_theorem_note_2026-05-03-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** beta_eff,Lambda(beta) := R_O^(-1)(P_Lambda(beta)); substituting the definition gives P_Lambda(beta) = R_O(beta_eff,Lambda(beta)).  _(class `E`)_
- **chain closes:** True — The formal coordinate identity closes because beta_eff is defined as the inverse response coordinate of P_Lambda, and the note gives premises intended to make that inverse well posed. This is tautological coordinate closure, not an independent derivation of <P>_full or beta_eff(6).
- **rationale:** Issue: The proof's load-bearing move is the definition beta_eff := R_O^(-1)(P_Lambda(beta)); the displayed bridge then follows by substitution. Why this blocks: this establishes a response coordinate once P_Lambda is already known, but it does not independently derive the full plaquette or completed coupling from retained primitives. Repair target: derive P_Lambda(beta) or beta_eff(beta) without using the inverse-definition as input. Claim boundary until fixed: a valid implicit-coordinate restatement with stated existence premises, not a retained observable-bridge derivation.
- **auditor confidence:** high

### `gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10`

- **Note:** [`GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact temporal-gauge factorization of the one-step mixed Wilson kernel into independent spatial-link convolution factors, with Peter-Weyl per-link eigenvalues and marked/non-marked compression for fixed tensor-product irrep sectors.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260606-224828-69cf823565-gauge_temporal_gauge_mixed_k`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** In temporal gauge the mixed plaquette holonomy reduces linkwise to U_(tau+1)(x,mu) U_tau(x,mu)^-1, so the mixed kernel is a product over spatial links and Schur orthogonality gives convolution eigenvalue c_lambda(beta)/d_lambda on each matrix coefficient.  _(class `A`)_
- **chain closes:** True — The temporal-gauge plaquette reduction and product Haar measure give the tensor product kernel, and compact-group Schur orthogonality gives the stated c_lambda/d_lambda factor. The marked-link formula follows by applying the per-link identity to the fixed Peter-Weyl tensor factors and the trivial character on unmarked links.
- **rationale:** The load-bearing mathematics is compact-group convolution algebra plus the temporal-gauge Wilson plaquette identity, not a numerical comparator, renaming, or imported framework-specific premise. Independent inspection of the displayed formulas confirms the c_lambda/d_lambda normalization, the a_0=1 trivial-channel normalization, and the c_0 contribution from unmarked links. The runner performs finite-group Z_N checks consistent with the algebra and does not import SU(3), beta=6, PDG data, or a downstream marked-plaquette premise.
- **auditor confidence:** high

### `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_full_packet_no_go_theorem_note_2026-04-20`

- **Note:** [`GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_FULL_PACKET_NO_GO_THEOREM_NOTE_2026-04-20.md`](../../docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_FULL_PACKET_NO_GO_THEOREM_NOTE_2026-04-20.md)
- **claim_type:** `no_go`
- **claim_scope:** Audited the linear-algebra no-go that the supplied full sparse-face target 3x3 Hermitian block cannot be a 3d compression of the selected retained 4x4 Wilson block because its eigenvalues violate Cauchy interlacing.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-hygiene-cycle-break-20260707-193821-5b3b16-gauge_vacuum_plaquette_first_sec-14`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The full sparse-face target Hermitian block violates compression interlacing against the selected retained 4x4 Wilson block, so no real or complex 3d compression of that retained ambient can reproduce the full target packet exactly.  _(class `A`)_
- **chain closes:** True — Conditioned on the supplied retained Wilson block and sparse-face target block, the interlacing obstruction is a standard algebraic closure and the runner verifies the needed eigenvalue inequalities. Retained-grade dependency closure is not established because the cited reduced-packet selector authority is marked unaudited.
- **rationale:** The no-go step itself is an algebraic Cauchy-interlacing check over the supplied matrices, and the primary runner computes the relevant spectra rather than merely printing constants. However, the source cites the reduced-packet complex-Givens selector theorem with effective_status unaudited, which triggers the rubric's dependency-not-retained downgrade. The additional no-go-discipline gate also blocks clean wall status as presented because the packet supplies one decisive interlacing route, not five distinct attack routes against the negative claim.
- **open / conditional deps cited:**
  - `GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_REDUCED_PACKET_COMPLEX_GIVENS_SELECTOR_THEOREM_NOTE_2026-04-20.md`
- **auditor confidence:** high

### `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_exact_solve_doublet_theorem_note_2026-04-20`

- **Note:** [`GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_EXACT_SOLVE_DOUBLET_THEOREM_NOTE_2026-04-20.md`](../../docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_EXACT_SOLVE_DOUBLET_THEOREM_NOTE_2026-04-20.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the empirical dense-search certificate: 3660 seeded solves on the selected bounded positive-angle chart find two observed root clusters with small residuals and nondegenerate finite-difference Jacobians; global symbolic exhaustiveness is not claimed.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T234713Z-d6cd597c-gauge_vacuum_plaquette_f-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Dense Monte-Carlo plus structured-grid seeding over the bounded positive-angle chart runs least_squares from 3660 seeds and every converged seed clusters onto exactly the same two observed roots, with no additional cluster emerging.  _(class `C`)_
- **chain closes:** True — The runner source genuinely computes the live residual from the retained transfer/block helpers, launches the documented structured plus random seed bath, clusters converged roots, and reports two nondegenerate clusters. The note has narrowed the conclusion to that empirical dense-search observation rather than a global exact root-count theorem.
- **rationale:** The scoped claim matches the runner output and source: two distinct observed clusters, all converged seeds assigned to them, well-separated projective lines, and local nondegeneracy. The code is not a print-only certificate or hard-coded count; it recomputes least-squares roots from the live residual equation. The open global exhaustiveness theorem is explicitly deferred, so it does not block this bounded empirical claim.
- **auditor confidence:** high

### `gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19`

- **Note:** [`GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_HELPER_NOTE_2026-04-19.md`](../../docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_HELPER_NOTE_2026-04-19.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Helper-interface registration in the named module: constants, line normalization and positive-angle parameterization, ordered projection/compression, and projector-distance routines only.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The load-bearing move is helper registration: fixed weights, line normalization/parameterization, ordered projection/compression, and projector-distance routines.  _(class `E`)_
- **chain closes:** True — The runner/source verify the advertised helper contracts and citation firewall. This closes only as interface registration; it does not derive the complement-line frame, selected_line selector, boundary-first weights, or downstream theorem closure.
- **rationale:** Issue: the load-bearing content is the module's own registration of constants and helper routines, not a derivation from cited physics inputs. Why this blocks stronger status: the runner smoke-checks implementation properties and firewall wording, but the note explicitly forbids using it as a derivation of the frame, selector, weights, or downstream closure. Repair target: a separate theorem deriving those choices; claim boundary until fixed is citeable helper-interface authority only.
- **auditor confidence:** high

### `gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_note_2026-04-19`

- **Note:** [`GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_RANK_ONE_FACTORIZED_CLASS_BOUNDARY_NOTE_2026-04-19.md`](../../docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_RANK_ONE_FACTORIZED_CLASS_BOUNDARY_NOTE_2026-04-19.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Within the four-weight first-sector finite packet, the explicitly constructed positive rank-one transfer T_min satisfying T_min^3 e_0 = v_min is not representable as exp(3J) D exp(3J) with diagonal conjugation-symmetric D.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-131604-1ba84b11dc-gauge_vacuum_plaquette_first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner forms the unique pullback D_back = M^{-1} T_min M^{-1}; since M is invertible and D_back is not diagonal, the explicit T_min is not in the diagonal subfamily T = M D M.  _(class `C`)_
- **chain closes:** True — The rank-one propagation identity follows algebraically from T_min = lambda vv^T with lambda^3 v_0 ||v||^4 = 1. Independently recomputing the finite matrices gives det(M)=1, ||offdiag(D_back)||_F=0.250338180104, and reconstruction error at numerical precision, so the diagonal-subfamily exclusion follows.
- **rationale:** The source and helpers compute the finite objects from the displayed SU(3)/recurrence definitions rather than importing a contested premise or merely printing constants. The load-bearing membership exclusion is stronger than the optimizer residual: invertibility of M makes the pullback unique, and the independently recomputed pullback is plainly non-diagonal. The helper notes contain broader open Wilson-environment language, but the audited claim explicitly stays within the finite diagonal factorized-class packet and does not rely on closing that broader identification.
- **auditor confidence:** high

### `gauge_vacuum_plaquette_spatial_environment_tensor_transfer_one_word_packet_narrow_theorem_note_2026-05-10`

- **Note:** [`GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_ONE_WORD_PACKET_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_ONE_WORD_PACKET_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Standalone finite-linear-algebra theorem on an abstract finite dominant-weight box: positive conjugation-symmetric D and swap-related nonnegative integer matrices N_f,N_fbar imply T=DMDM^TD has entry-wise nonnegativity, conjugation-swap symmetry, and nonnegative/strictly positive trivial-channel readout under the stated row-support condition. The N=4 beta=6 Wilson/Pieri instance is only a runner witness for the hypotheses; no Wilson environment slicing, z_(p,q)^env boundary identity, Perron readout, untruncated tensor transfer, or physical spatial-environment operator identification is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Given a positive conjugation-symmetric diagonal D and swap-related nonnegative matrices N_fbar = S N_f S on a finite dominant-weight box, the assembled matrix T = D M D M^T D with M=N_f+N_fbar is entry-wise nonnegative, commutes with S, and gives a nonnegative trivial readout r=T e_(0,0) with positive trivial-channel amplitude when the (0,0) row of M is nonzero.  _(class `A`)_
- **chain closes:** True — The proof is finite matrix algebra: nonnegative factors give T_ab>=0, the hypotheses S D=D S and S M=M S give S T=T S, and the readout formula follows from multiplying T by e_(0,0). The runner verifies the abstract identities, a Wilson/Pieri reference instance, an arbitrary symmetric-positive diagonal instance, and a symmetry-breaking negative control with PASS=19, FAIL=0.
- **rationale:** The scoped theorem closes because all conclusions are direct consequences of the stated finite-matrix hypotheses, and the negative control confirms that conjugation symmetry of D is a real load-bearing assumption. The runner's beta=6 Wilson/Pieri instantiation is only evidence that one concrete finite packet satisfies the abstract hypotheses; the theorem itself is not claiming a physical spatial-environment transfer identity. Residual risk is scope drift into the parent Wilson boundary-character/Perron/untruncated construction, which this audit does not ratify.
- **auditor confidence:** high

### `gauge_vacuum_plaquette_su3_full_slice_product_fubini_factorization_note_2026-06-06`

- **Note:** [`GAUGE_VACUUM_PLAQUETTE_SU3_FULL_SLICE_PRODUCT_FUBINI_FACTORIZATION_NOTE_2026-06-06.md`](../../docs/GAUGE_VACUUM_PLAQUETTE_SU3_FULL_SLICE_PRODUCT_FUBINI_FACTORIZATION_NOTE_2026-06-06.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For a supplied finite SU(3) rim/far support partition with no mixed rim/far plaquettes, the product-Haar full-slice marginal factorizes into fixed, rim, and far factors; the W-independent far factor pulls through the marked class projection.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-160113-bfd08704fd-gauge_vacuum_plaquette_su3_f`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Given the support-separated action and finite product Haar measure, Fubini/Tonelli factors the full-slice integral into the fixed scalar, rim integral, and far integral.  _(class `A`)_
- **chain closes:** True — The integrand separates as exp((beta/3)A^0) exp((beta/3)A^rim) exp((beta/3)A^far) on a finite product Haar space, and compactness/continuity gives bounded measurability, so the product integral factors. For the projection statement, only the W-independent far factor is pulled through P_cls; the W-dependent A^0 factor must be treated as part of the marked/rim factor.
- **rationale:** The audited theorem is a standard finite product-measure factorization under an explicitly supplied support-separation hypothesis, not a derivation of the physical support partition. No cited upstream authority is needed for this bounded mathematical step, and the displayed beta/3 normalization cancels consistently through the separated exponential factors. The runner supports the claim with exact finite product and scalar-projection checks plus artifact checks, but the clean closure rests on the independent product-measure argument. The verdict does not cover the temporal-gauge compression bridge, the actual Wilson-slab rim/far partition, or beta-six numerical plaquette evaluation.
- **auditor confidence:** high

### `generation_axiom_boundary_note`

- **Note:** [`GENERATION_AXIOM_BOUNDARY_NOTE.md`](../../docs/GENERATION_AXIOM_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-dimensional algebra check that the supplied H_hw=1 translation-character projectors and C3 cycle generator generate M_3(C) with scalar commutant; physical-species, substrate, and historical-memo claims are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260522T152037Z-7ff9b833-generation_axiom_boundar-01`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The supplied translation-character projectors and C3 cycle generator generate the full nine-dimensional M_3(C) observable algebra on H_hw=1 and have scalar commutant.  _(class `A`)_
- **chain closes:** True — Within the bounded scope, the runner constructs the stated 3x3 generators, computes the generated algebra dimension, and computes the commutant dimension. The conclusion follows for those supplied generators without using the out-of-scope physical bridges.
- **rationale:** The runner performs actual finite-dimensional linear algebra rather than printing constants: it constructs the translation-sign matrices, the C3 permutation, projectors, algebra span, and commutant constraints. All four checks are algebraic identity/closure checks on the supplied local generators. Because the source note already bounds the claim to this local H_hw=1 M_3(C) reconstruction and explicitly excludes physical-species and substrate conclusions, no split is needed before audit; it should remain a bounded_theorem, not a positive_theorem.
- **auditor confidence:** high

### `generation_dial_local_stability_grammar_2026-06-05`

- **Note:** [`GENERATION_DIAL_LOCAL_STABILITY_GRAMMAR_2026-06-05.md`](../../docs/GENERATION_DIAL_LOCAL_STABILITY_GRAMMAR_2026-06-05.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For r > 0, s = 1 + log(r)/log(2) is a smooth monotone coordinate equivalent to r for local one-dimensional map and flow stability, and the named maps become s' = 2s and s' = s/2.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00393-generation_dial_local_stabil`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** By the chain rule at a fixed point, the derivatives of the inverse coordinate maps cancel, so the conjugated map has multiplier F'(s*) = G'(r*) and the transformed flow has the same linearization coefficient.  _(class `A`)_
- **chain closes:** True — The inverse-coordinate identities, derivative cancellation, and named-map transformations follow directly from elementary algebra and the chain rule. No external datum, fitted value, physical selector, or uncited bridge is needed for the scoped local-stability theorem.
- **rationale:** The claim is a self-contained algebraic and calculus result about a smooth positive-coordinate reparametrization. The runner performs substantive symbolic checks of the inverse identities, map and flow linearizations, and the two named maps, with no imported measurements or tuned constants. The tautological S1.2 definition check is not load-bearing, and the source correctly confines the result to local stability classification without asserting physical selection.
- **auditor confidence:** high

### `geometry_lane_head_to_head_note`

- **Note:** [`GEOMETRY_LANE_HEAD_TO_HEAD_NOTE.md`](../../docs/GEOMETRY_LANE_HEAD_TO_HEAD_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite four-configuration runner table for modular gap=2, modular gap=4, central |y-center|<1, and central |y-center|<2 on N=25,40,60,80,100 with 16 matched seeds, npl=25, y_range=12, connect_radius=3.0, and the stated layernorm pur_min/gravity readouts.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-153537-a5e2dcef-geometry_lane_head_to_he-020`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The binding evidence of this note is exactly the finite four-configuration runner table from scripts/geometry_lane_head_to_head.py on the declared 16 matched-seed grid.  _(class `C`)_
- **chain closes:** True — Within the narrowed scope, the runner genuinely constructs the four graph/readout configurations and computes the reported finite table from generated DAGs, propagation, purity, gravity, and removal-fraction calculations. The note explicitly excludes top-lane promotion, asymptotic claims, and same-readout implementation as binding conclusions.
- **rationale:** The source note's binding claim is no longer a broad dominance or lane-selection theorem; it is the finite runner table itself plus conservative interpretation of that table. The provided primary runner and helper sources do not merely print constants or import a contested result: they generate the modular and central-band graphs, apply the shared propagation/readout routines, and aggregate the matched-seed outputs. The runner stdout matches the table-level claims in the note, including the absence of a universal winner and the N-specific tradeoffs. The demoted top-lane-selection and same-readout-implementation interpretations are outside the audited scope rather than hidden load-bearing premises.
- **auditor confidence:** high

### `geometry_superposition_dag_ensemble_note_2026-04-11`

- **Note:** [`GEOMETRY_SUPERPOSITION_DAG_ENSEMBLE_NOTE_2026-04-11.md`](../../docs/GEOMETRY_SUPERPOSITION_DAG_ENSEMBLE_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded exploratory path-sum computation on the registered older toy_event_physics DAG ensemble only: five specified DAG geometry variants at WIDTH=20, HEIGHT=8, SOURCE=(0,0), SEED=42, RulePostulates(k=4.0,p=1.0), equal-weight normalized-psi coherent/incoherent comparison, reporting the current 3.93% normalized contrast, 0.057445 centroid shift, 0.021137 width change, and approximately 0.3225 rad maximum peak-bin phase separation. No staggered-fermion result, BMV/gravity-entanglement closure, old TV=0.37/TVq=0.079/dphi=1.87 headline, or general geometry-superposition theorem is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The registered toy-DAG ensemble runner reports normalized coherent-vs-incoherent contrast 0.0393, centroid shift 0.057445, width change 0.021137, and peak-bin pairwise phase differences up to about 0.3225 rad, so coherent summation over the specified DAG geometries is distinguishable from the incoherent mixture in this bounded ensemble.  _(class `C`)_
- **chain closes:** True — The live runner deterministically constructs the five specified DAG variants, including the repaired added-edge variant, propagates the toy path-sum amplitudes, normalizes each geometry's detector wavefunction, and reproduces the note's bounded contrast, centroid, width, and phase-difference values. The source note explicitly confines the claim to this older DAG-ensemble probe and excludes staggered/headline claims.
- **rationale:** The bounded computation closes because the current runner output matches the scoped numerical rows and the note has narrowed away the prior inflated normalization headline and any staggered-fermion interpretation. The runner does not emit classified PASS lines, but its deterministic output directly provides the audited observables and its branch would stop claiming confirmation if normalized contrast fell below the stated 1% threshold. Residual risk is citation drift: this result is only a toy_event_physics DAG-ensemble lead, not a retained staggered or gravity-entanglement claim.
- **auditor confidence:** high

### `global_coherence_off_scaffold_note`

- **Note:** [`GLOBAL_COHERENCE_OFF_SCAFFOLD_NOTE.md`](../../docs/GLOBAL_COHERENCE_OFF_SCAFFOLD_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-ca82-singer-fresh-2026-04-30`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** On nine off-scaffold generators, the frozen free_coh >= 7.96e-04 rule scores 5/9, matching the old two-property rule on the same batch.  _(class `D`)_
- **chain closes:** True — The current runner reproduces the finite off-scaffold table, L2 accuracy 5/9, old-rule accuracy 5/9, and pre-committed structural baseline 8/9. This closes the finite bounded negative, not a universal simple-classifier exclusion theorem.
- **rationale:** The finite off-scaffold comparison closes from the source note and current runner output. The safe claim is bounded to this nine-generator hand-specified batch, one frozen free_coh threshold, and one old two-property comparator. Residual risk is only scope drift: the result should not be read as excluding all scalar metrics or all simple classifiers.
- **auditor confidence:** high

### `global_coherence_predictor_note`

- **Note:** [`GLOBAL_COHERENCE_PREDICTOR_NOTE.md`](../../docs/GLOBAL_COHERENCE_PREDICTOR_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Historical scaffolded global-coherence finite replay: free_coh >= 7.9597e-04 gives 7/9 scaffolded held-out accuracy versus 6/9 for the old two-property rule, with the retained off-scaffold dependency limiting this to scaffold-specific evidence and closing the classifier lane.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The live replay asserts the archived scaffolded 7/9 free_coh result against the old 6/9 two-property rule, while the source note's 2026-04-07 update and dependency restrict that result to scaffold-specific historical evidence.  _(class `C`)_
- **chain closes:** True — The primary runner completes and asserts the bounded archived scaffolded numbers, and the direct dependency is retained-bounded for the off-scaffold reversal. The clean scope excludes any generator-agnostic predictor or simple-classifier exhaustion theorem.
- **rationale:** The source note has been narrowed to historical finite evidence, and the runner cache reproduces the archived 7/9 versus 6/9 scaffolded result. The retained off-scaffold dependency supplies the reversal that prevents this from being promoted as a generator-agnostic law or live classifier program. Residual risk is ordinary finite-sample/scaffold specificity; broader metric-search closure or analytic path-sum derivation is not audited here.
- **auditor confidence:** high

### `graded_constraint_menu_uniformity_contextuality_and_c3_zero_information_point_bounded_theorem_note_2026-07-11`

- **Note:** [`GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md`](../../docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The conditional menu-refinement contradiction, full-symmetry zero-information point, and unequal-rank obstruction on the proposed C3 generation context.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** Uniformity on both {P_s,P_d} and {P_s,P_1,P_2} assigns incompatible values to the shared projector, while full qutrit Weyl symmetry forces rho=I/3 and hence r=1 rather than r=1/2.  _(class `A`)_
- **chain closes:** False — The matrix and menu algebra closes conditionally, but the graded core and canonical context are proposed/unapproved, while the Born-form and occupancy parents are unaudited.
- **rationale:** Issue: the refinement contradiction, Weyl-commutant calculation, Born-weight traces, DFT tie, and rank obstruction are correct, but the graded core and context naming are proposed rather than approved and two scientific direct parents are unaudited. Why this blocks: the computed r=1 and r=1/2 points remain consequences of supplied menu, Born-form, symmetry, and dictionary hypotheses rather than retained framework results. Repair target: retain the Born and occupancy parents and provide approved or retained law-domain certificates for menu eligibility, lattice-motion covariance, and record-decidable weighting. Claim boundary until fixed: A-C are exact conditional boundary facts on the explicitly supplied qutrit projection menus only.
- **open / conditional deps cited:**
  - `BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`
  - `KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md`
- **auditor confidence:** high
- **No-Go Discipline:** `PASS`

### `graph_first_selector_derivation_note`

- **Note:** [`GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md`](../../docs/GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited the algebraic derivation of the graph-native weak-axis selector from the canonical one-step shifts on the 8-vertex taste cube, including its normalized axis-minimum and residual Z2 structure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260522T153215Z-b31fe630-graph_first_selector_der-02`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** For H(phi) = sum_i phi_i S_i, V_sel(phi) = Tr H(phi)^4 - (1/8)(Tr H(phi)^2)^2 = 32 sum_{i<j} phi_i^2 phi_j^2, which normalizes to the pairwise-overlap potential with axis minima.  _(class `A`)_
- **chain closes:** True — The selector identity follows algebraically from the explicitly defined commuting involutive cube shifts, and the simplex minima follow from nonnegativity of the pairwise-overlap potential. No SU(3) bridge, abelian identification, or downstream phenomenology is needed for this scoped selector claim.
- **rationale:** The runner constructs the canonical Pauli-x cube shifts directly and verifies their algebraic properties, trace identities, normalized overlap form, axis minima, and residual stabilizers. Its checks are internal algebra over the stated graph-shift surface, with no external comparator, tuned numerical scale, or imported physical bridge. The cited SU(3) integration note is not load-bearing for this selector derivation, and the source note explicitly bounds away downstream abelian or phenomenological claims.
- **auditor confidence:** high

### `graph_first_su3_integration_note`

- **Note:** [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](../../docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For the finite taste cube with a given selected axis, the graph-native weak su(2) fiber action plus complementary-axis swap has joint commutant gl(3) plus gl(1), whose compact semisimple part is su(3), without auditing physical hypercharge or electroweak matching.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-judicial-panel-per-site-k1-20260522T153010Z-graph_first_su3_integration_note-majority`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** Imposing the residual complementary-axis swap on the weak-su(2) commutant restricts the base algebra to the 3+1 split, giving Comm(su(2)_weak, tau) isomorphic to gl(3) plus gl(1) with compact semisimple part su(3).  _(class `A`)_
- **chain closes:** True — Five-judge panel majority 5/5 ratified the second tuple (audited_clean, positive_theorem, class A). Vote breakdown: J1: second / audited_clean / positive_theorem / class A; J2: second / audited_clean / positive_theorem / class A; J3: second / audited_clean / positive_theorem / class A; J4: second / audited_clean / positive_theorem / class A; J5: second / audited_clean / positive_theorem / class A. Majority rationale: The restricted packet supports the narrowed selected-axis finite-cube theorem by explicit finite-dimensional linear algebra, and the runner constructs and checks the relevant operators rather than printing constants. The load-bearing step is an algebraic commutant calculation over the defined cube operators, so class A is more accurate than class C. The result is clean as a positive structural theorem only at this narrowed scope; selector derivation, color-carrier interpretation, anomaly completion, and electroweak matching are outside the ratified claim. | The second audit gives the applyable scoped tuple: the restricted packet supports a finite-dimensional algebraic commutant theorem once a selected axis is given. The runner source constructs the cube shift, parity, residual swap, commutant basis, projectors, and embedded su(3) generators directly, with no external comparator, tuned numerical input, or physical hypercharge promotion. The first audit’s clean verdict is compatible, but its class C overstates the step as first-principles framework computation rather than an algebraic closure on explicitly defined finite-cube operators. | The restricted packet supports a clean finite-dimensional algebra theorem once the selected axis is taken as the scoped input. The runner constructs the cube shift, parity, swap, commutant, projectors, and embedded su(3) generators and checks the identities for all three axes, so the load-bearing step is an algebraic closure check rather than a first-principles physical computation. The second audit correctly narrows away the upstream selector derivation and any physical hypercharge or electroweak identification. | The restricted packet supports a clean finite-dimensional algebraic theorem on the selected-axis cube surface. The runner constructs the cube shift, parity, residual swap, commutant, projectors, and embedded su(3) generators for all three axes, so this is an algebraic closure check rather than a first-principles numerical compute from the full Cl(3) on Z^3 axiom surface. The clean verdict applies only to the structural selected-axis commutant statement and does not promote hypercharge, anomaly completion, electroweak matching, or the upstream selector derivation. | The restricted packet supports the narrowed finite-cube structural theorem by explicit finite-dimensional linear algebra for all three selected axes. The load-bearing step is an algebraic commutant calculation, so class A is more accurate than class C because no new first-principles physical number is computed from Cl(3) on Z^3. The second audit correctly scopes out the upstream selector derivation and any physical color, hypercharge, anomaly-completion, or EW matching interpretation.
- **rationale:** Five-judge panel majority 5/5 ratified the second tuple (audited_clean, positive_theorem, class A). Vote breakdown: J1: second / audited_clean / positive_theorem / class A; J2: second / audited_clean / positive_theorem / class A; J3: second / audited_clean / positive_theorem / class A; J4: second / audited_clean / positive_theorem / class A; J5: second / audited_clean / positive_theorem / class A. Majority rationale: The restricted packet supports the narrowed selected-axis finite-cube theorem by explicit finite-dimensional linear algebra, and the runner constructs and checks the relevant operators rather than printing constants. The load-bearing step is an algebraic commutant calculation over the defined cube operators, so class A is more accurate than class C. The result is clean as a positive structural theorem only at this narrowed scope; selector derivation, color-carrier interpretation, anomaly completion, and electroweak matching are outside the ratified claim. | The second audit gives the applyable scoped tuple: the restricted packet supports a finite-dimensional algebraic commutant theorem once a selected axis is given. The runner source constructs the cube shift, parity, residual swap, commutant basis, projectors, and embedded su(3) generators directly, with no external comparator, tuned numerical input, or physical hypercharge promotion. The first audit’s clean verdict is compatible, but its class C overstates the step as first-principles framework computation rather than an algebraic closure on explicitly defined finite-cube operators. | The restricted packet supports a clean finite-dimensional algebra theorem once the selected axis is taken as the scoped input. The runner constructs the cube shift, parity, swap, commutant, projectors, and embedded su(3) generators and checks the identities for all three axes, so the load-bearing step is an algebraic closure check rather than a first-principles physical computation. The second audit correctly narrows away the upstream selector derivation and any physical hypercharge or electroweak identification. | The restricted packet supports a clean finite-dimensional algebraic theorem on the selected-axis cube surface. The runner constructs the cube shift, parity, residual swap, commutant, projectors, and embedded su(3) generators for all three axes, so this is an algebraic closure check rather than a first-principles numerical compute from the full Cl(3) on Z^3 axiom surface. The clean verdict applies only to the structural selected-axis commutant statement and does not promote hypercharge, anomaly completion, electroweak matching, or the upstream selector derivation. | The restricted packet supports the narrowed finite-cube structural theorem by explicit finite-dimensional linear algebra for all three selected axes. The load-bearing step is an algebraic commutant calculation, so class A is more accurate than class C because no new first-principles physical number is computed from Cl(3) on Z^3. The second audit correctly scopes out the upstream selector derivation and any physical color, hypercharge, anomaly-completion, or EW matching interpretation.
- **auditor confidence:** judicial_panel_majority

### `graph_laplacian_core_card_note`

- **Note:** [`GRAPH_LAPLACIAN_CORE_CARD_NOTE.md`](../../docs/GRAPH_LAPLACIAN_CORE_CARD_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The audited claim is the fixed-parameter checked-in graph-Laplacian KG core-card result: 13/16 on the listed C1-C16 runner rows, not a perfect card or full physical-retention theorem.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e0941-0247-7cc2-8a46-04206737b691`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Rerunning scripts/frontier_graph_kg_16card.py gives SCORE: 13/16, with C1, C13, and C14 failing and the other thirteen rows passing.  _(class `C`)_
- **chain closes:** True — For this bounded script-card claim, the runner source actually constructs the finite graph-Laplacian/leapfrog model and computes the listed row outcomes rather than merely printing constants. The stdout matches the note's 13/16 result and the stated failing rows.
- **rationale:** The narrow bounded claim closes: the note reports the corrected runner result, and the included source reproduces the same 13 pass / 3 fail card without hard-coding the final score. The clean verdict is only for that fixed-parameter card readout and its listed corrections. It does not promote the graph-Laplacian lane to a retained physical derivation; C12 is still labeled a proxy and the note itself preserves the Born, carrier-k, and mass/gravity split failures as open carry-forward items.
- **auditor confidence:** high

### `graph_scalar_plus_spinor_note`

- **Note:** [`GRAPH_SCALAR_PLUS_SPINOR_NOTE.md`](../../docs/GRAPH_SCALAR_PLUS_SPINOR_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-resweep-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** - the lane is therefore a one-way proof of concept, not a closed two-field theory  _(class `C`)_
- **chain closes:** True — Yes. The registered runner exits cleanly and exposes 5 classified A/B/C/D checks for this leaf claim with no non-retained one-hop dependencies.
- **rationale:** The restricted packet closes on its declared bounded scope: the source note has no non-retained one-hop dependencies and the registered runner passes with classified C-dominant checks. This audit ratifies only that bounded/support leaf surface, not any stronger retained-tier conclusion unless the source note is separately re-tiered. Residual risk: the audit relies on the registered runner as the executable witness and does not import broader publication framing.
- **auditor confidence:** high

### `graph_true_kg_vs_cn_note`

- **Note:** [`GRAPH_TRUE_KG_VS_CN_NOTE.md`](../../docs/GRAPH_TRUE_KG_VS_CN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-resweep-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** This is the decisive result. The free modal laws are not the same theory.  _(class `C`)_
- **chain closes:** True — Yes. The registered runner exits cleanly and exposes 9 classified A/B/C/D checks for this leaf claim with no non-retained one-hop dependencies.
- **rationale:** The restricted packet closes on its declared bounded scope: the source note has no non-retained one-hop dependencies and the registered runner passes with classified C-dominant checks. This audit ratifies only that bounded/support leaf surface, not any stronger retained-tier conclusion unless the source note is separately re-tiered. Residual risk: the audit relies on the registered runner as the executable witness and does not import broader publication framing.
- **auditor confidence:** high

### `gravitational_entanglement_note`

- **Note:** [`GRAVITATIONAL_ENTANGLEMENT_NOTE.md`](../../docs/GRAVITATIONAL_ENTANGLEMENT_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-resweep-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** Correlation-matrix formalism for free fermions: the joint state is tracked via a 2N x 2N one-body density matrix. Time evolution uses Trotter steps with self-consistent Poisson coupling at each step. Cross-correlations between A and B are computed via the RPA (random phase approximation): the static density-density susceptibility chi = C(1-C) mediates gravit  _(class `C`)_
- **chain closes:** True — Yes. The registered runner exits cleanly and exposes 6 classified A/B/C/D checks for this leaf claim with no non-retained one-hop dependencies.
- **rationale:** The restricted packet closes on its declared support scope: the source note has no non-retained one-hop dependencies and the registered runner passes with classified C-dominant checks. This audit ratifies only that bounded/support leaf surface, not any stronger retained-tier conclusion unless the source note is separately re-tiered. Residual risk: the audit relies on the registered runner as the executable witness and does not import broader publication framing.
- **auditor confidence:** high

### `gravitational_memory_note_2026-04-11`

- **Note:** [`GRAVITATIONAL_MEMORY_NOTE_2026-04-11.md`](../../docs/GRAVITATIONAL_MEMORY_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the narrow N=61 ring runner claim: the specified toy protocol produces the reported small permanent marker-separation shift and amplitude-response pattern, while not establishing a stable graph-family or GR memory observable.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T175818Z-d760945f-gravitational_memory_not-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On this 1D ring protocol, a transient retarded field pulse produces a small but repeatable permanent shift in marker separation after the pulse has passed, with weak-pulse approximate linearity and strong-pulse nonlinearity.  _(class `C`)_
- **chain closes:** True — The included runner source actually evolves the field and marker wavepackets and computes the reported separations rather than printing hard-coded constants. The broader Yukawa-screening interpretation is not load-bearing for the narrowed bounded claim and is explicitly caveated by the cited robustness notes.
- **rationale:** The runner output matches the source note's narrow numerical table and summary for the N=61 protocol, and the source code performs a genuine simulation from the stated toy equations. The cited retained_bounded authorities support restricting the claim away from a graph-family or publication-grade positive memory result. The note's wording about Yukawa screening as the likely cause is weaker than the current cited authorities allow, but the audited claim is bounded to the reproduced narrow-ring signal and the instability under robustness checks.
- **auditor confidence:** high

### `gravity_observable_hierarchy_note`

- **Note:** [`GRAVITY_OBSERVABLE_HIERARCHY_NOTE.md`](../../docs/GRAVITY_OBSERVABLE_HIERARCHY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded sign-classification hierarchy for the supplied runner-computed rows: 2D ultra-weak, 2D strong-field depletion, 3D power-action barrier, and 3D dense spent-delay z=3 and z=5 only.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e12e4-6fd1-77c1-90b0-eef6c721671b`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The second row is the only case where a negative centroid should be treated as something other than ordinary "away" behavior, with the current retained 3D dense scope narrowed to runner-computed z=3 and z=5 rows.  _(class `A`)_
- **chain closes:** True — Within the narrowed scope, the runner stdout matches the note's signs and classifications for every ratified row. The z=2, z=4, z=6, and z=7 dense rows are explicitly outside the audited scope and are not ratified here.
- **rationale:** The scoped claim is an algebraic sign-interpretation over runner-computed observables, and the supplied runner computes the relevant rows rather than printing fixed classifications. No one-hop authorities are listed, so no dependency-retention blocker is available inside the restricted packet. Clean status applies only to the narrowed z=3 and z=5 dense rows plus the other printed runner rows; the broader z=2..6 dense table is not part of this verdict.
- **auditor confidence:** medium

### `growing_graph_expansion_card_note`

- **Note:** [`GROWING_GRAPH_EXPANSION_CARD_NOTE.md`](../../docs/GROWING_GRAPH_EXPANSION_CARD_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded toy-graph statement that the specified seed strip and frontier-growth rule produce strong spreading proxies relative to the static seed control over 16 steps.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e0d7c-c172-74a2-ab82-65b4f95e2e33`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The runner applies the stated frontier-growing graph rule for 16 steps and computes that node count, frontier size, mean radius, and max radius grow strongly while the static control remains fixed.  _(class `C`)_
- **chain closes:** True — The note makes only a bounded analog-proxy claim, and the runner directly constructs the seed, applies the growth rule, computes the reported graph statistics, and compares them to the static control. No external physical bridge or cosmology derivation is required for this narrowed scope.
- **rationale:** The load-bearing result is an internal computation from the specified toy growth rule, not an imported comparator or a symbolic relabeling. The source explicitly limits the claim to a de Sitter-like spreading proxy and disclaims proof of de Sitter spacetime, inflation, or real cosmological data. Within that boundary, the runner source actually grows the graph and recomputes the reported counts, radii, slopes, and static-control quantities.
- **auditor confidence:** high

### `h2t_h0125_narrow_bridge_note`

- **Note:** [`H2T_H0125_NARROW_BRIDGE_NOTE.md`](../../docs/H2T_H0125_NARROW_BRIDGE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded audit of the current dense 3D numpy 1/L^2 + h^2 family at h=0.125 for Born cleanliness, gravity sign, and weak-field F~M closure on the stated fixed boxes.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T195015Z-3e6824e0-h2t_h0125_narrow_bridge_-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At h=0.125 the reduced fixed family has clean Born and TOWARD sign, but F~M alpha remains about 0.50 rather than the Newtonian approx 1 bar, so the narrow retained bridge claim fails.  _(class `C`)_
- **chain closes:** True — The supplied runner and helper sources instantiate the lattice, field, propagation, detector readouts, and log-log F~M fit rather than importing the contested exponent. The computed reduced-family h=0.125 result supports the note's bounded negative conclusion that this family does not deliver F~M approx 1.
- **rationale:** The cited authority is retained_bounded, which is retained-grade under the rubric, and it independently agrees that the bridge-family F~M readout is about 0.50 rather than a Newtonian closure. The primary runner plus included helpers perform first-principles numerical computation within the framework and do not hard-code the contested h=0.125 F~M outcome. The source note's conclusion is negative and bounded, so the observed failure to reach the stated F~M bar closes the audited claim on its own terms.
- **auditor confidence:** high

### `hard_geometry_gravity_window_note`

- **Note:** [`HARD_GEOMETRY_GRAVITY_WINDOW_NOTE.md`](../../docs/HARD_GEOMETRY_GRAVITY_WINDOW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded primary-runner direct-gravity window only: in the cached hard_geometry_gravity_window.py sweep over N=60/80/100, central y-cuts, asymmetry thresholds, field scales, and six seeds, the largest Born-safe layer-normalized gravity mean is the generated-asymmetry row family=asym, threshold=0.05, scale=1.0, N=100, with the printed finite-window metrics; not a mass-response theorem, universal hard-geometry law, or asymptotic claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-gpt-5.5-2026-05-27`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** In the cached primary-runner sweep, the strongest Born-safe layer-normalized direct gravity pocket is family=asym, threshold=0.05, scale=1.0, N=100, with grav_ln=+2.297 +/- 0.486, grav_lin=+2.480, pur_min=0.937, born_max=6.66e-16, and ok=6.  _(class `C`)_
- **chain closes:** True — The registered runner constructs the central-band and generated-asymmetry graph windows, computes linear and layer-normalized propagation, Born controls, purity, and gravity metrics, filters Born-safe rows, and selects the row with maximal layer-normalized gravity mean. The source note has narrowed the claim to exactly that finite primary-runner maximum and explicitly excludes mass-response ranking, carrier theorem, universal law, and asymptotic promotion.
- **rationale:** The bounded claim closes because the source note's load-bearing best-pocket sentence matches the current SHA-pinned runner cache and stays within the primary-runner finite-window scope. The runner and helper sources compute the graph families, propagation, Born metric, purity, and gravity values from declared inputs rather than printing the target row or importing it from the note. Residual boundary: downstream use must not cite this as a physical hard-geometry carrier theorem, mass-response ranking, or asymptotic gravity law.
- **auditor confidence:** high

### `hard_geometry_local_note`

- **Note:** [`HARD_GEOMETRY_LOCAL_NOTE.md`](../../docs/HARD_GEOMETRY_LOCAL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop:leaf-resweep-2026-04-30`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** This note records the local hard-geometry pilot that asked whether a  _(class `D`)_
- **chain closes:** True — Yes. The registered runner exits cleanly and exposes 2 classified A/B/C/D checks for this leaf claim with no non-retained one-hop dependencies.
- **rationale:** The restricted packet closes on its declared bounded scope: the source note has no non-retained one-hop dependencies and the registered runner passes with classified D-dominant checks. This audit ratifies only that bounded/support leaf surface, not any stronger retained-tier conclusion unless the source note is separately re-tiered. Residual risk: the audit relies on the registered runner as the executable witness and does not import broader publication framing.
- **auditor confidence:** high

### `harmonic_ladder_weight_law_bounded_theorem_note_2026-06-12`

- **Note:** [`HARMONIC_LADDER_WEIGHT_LAW_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/HARMONIC_LADDER_WEIGHT_LAW_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Exact finite L=3 realized states K=3,4,5,6 with listed seeds: the single-sideband law is refuted, and the finite Laurent determinant principal-Arg law reproduces ladder weights and bounded tail-order statements.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-fresh-harmonic-sieve-20260709`  (codex-current; independence=fresh_context)
- **load-bearing step:** g_s(theta) = Arg(F_s(e^{i(theta+delta)}) / F_s(e^{i theta})) - mean with delta = 3*tau = 1.05, and paired ladder weights w_k are normalized Fourier powers of g_s.  _(class `C`)_
- **chain closes:** True — The runner constructs the finite L=3 realized states, determinant Laurent coefficients, principal-branch phase increments, Fourier weights, root data, single-sideband refutation, and tail orders within the restricted packet. No upstream dependency or external comparator is needed for the bounded finite-state claim.
- **rationale:** The bounded finite claim closes inside the restricted packet: the runner recomputes the determinant-root and Laurent-Arg machinery rather than merely printing the headline result. Frozen tables act as regression and staleness gates, while the load-bearing Laurent-law comparison is computed from the determinant construction. Residual risk is numerical scope only: this is double-precision finite-state verification, not a symbolic proof or a generalization beyond the four listed realized states.
- **auditor confidence:** high

### `hierarchy_spatial_bc_and_u0_scaling_note`

- **Note:** [`HIERARCHY_SPATIAL_BC_AND_U0_SCALING_NOTE.md`](../../docs/HIERARCHY_SPATIAL_BC_AND_U0_SCALING_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Exact minimal L_s=2 hierarchy-block statements: temporal-APBC determinant formulas for spatial PBC/APBC, BC-independent zero-mass u0^(8Lt) power, APBC-only finite intensive small-m coefficient limit, and local m/u0 homogeneity of the free-energy density.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-second-hierarchy_spatial_bc_and_u0_scaling_note-20260505`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Spatial APBC is not selected by exponent counting; it is selected by the existence of a finite intensive 3+1 order-parameter limit on the minimal hierarchy block, while the exact local observable depends on u0 only through m/u0.  _(class `C`)_
- **chain closes:** True — Within the bounded minimal-block scope, the determinant formulas, coefficient asymptotics, and u0 homogeneity follow from the explicit finite Dirac operator and exact formulas checked by the runner. The note explicitly excludes the broader physical electroweak order-parameter selection theorem from the closed claim.
- **rationale:** The runner constructs the minimal L_s=2 Dirac matrix, compares direct determinants against the stated closed formulas for both spatial BCs, verifies the BC-independent zero-mass u0 power, and checks the exact homogeneity and small-m coefficient consequences with zero failures. The source note does not overclaim the full hierarchy theorem: it confines closure to the spatial-BC and u0-scaling objections and explicitly leaves the physical intensive order-parameter selection as open. Residual risk is limited to not treating this bounded theorem as the missing physical bridge.
- **auditor confidence:** high

### `higgs_mean_field_determinant_apbc_taste_bridge_note_2026-06-06`

- **Note:** [`HIGGS_MEAN_FIELD_DETERMINANT_APBC_TASTE_BRIDGE_NOTE_2026-06-06.md`](../../docs/HIGGS_MEAN_FIELD_DETERMINANT_APBC_TASTE_BRIDGE_NOTE_2026-06-06.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Finite Clifford/APBC spin-taste/color mean-field determinant identity showing the per-mode source curvature equals 4/(u_0^2 N_taste) for N_taste = 16 under the declared U -> u_0 I truncation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-003805-591b5e401f-higgs_mean_field_determinant`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** With D_mf^dag D_mf = 4 u_0^2 I_48, the trace-log reduces to W(J) = (48/2) log(J^2 + 4 u_0^2), giving W''(0)/48 = 1/(4 u_0^2) = 4/(u_0^2 * 16).  _(class `A`)_
- **chain closes:** True — The Clifford anticommutation gives (sum_mu gamma_mu)^2 = 4 I_4, and Hermitian tensor/color lifts preserve D^dag D as 4 u_0^2 I_48. The trace-log derivative then gives W''(0)/48 = 1/(4 u_0^2), matching 4/(u_0^2 N_taste) at N_taste = 16.
- **rationale:** The restricted packet presents a finite algebraic determinant calculation, not a physical Higgs-mass identification or full gauge-theory claim. Independent checking of the displayed dimensions, Clifford square, tensor/color lift, determinant trace factor, and J-curvature confirms the factors 4, 16, 48, 1/2, and 1/(4 u_0^2). The runner source performs actual finite matrix and symbolic derivative checks rather than importing an external calibrated value or merely printing constants.
- **auditor confidence:** high

### `higher_symmetry_gravity_probe_note`

- **Note:** [`HIGHER_SYMMETRY_GRAVITY_PROBE_NOTE.md`](../../docs/HIGHER_SYMMETRY_GRAVITY_PROBE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** On the default dense Z2xZ2 runner surface N={80,100,120}, 16 seeds, z2z2_quarter=16, connect_radius=5.2, anchor_b=5.0, mass_count=4, the SHA-matched completed runner produces the stated finite mass-window rows, positive-row subfits inside M={2,3,5,8}, and positive but weak fixed-distance sweep rows; it does not establish rowwise/global gravity positivity, Born safety, or a gravity law.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-higher-symmetry-gravity-probe-audit-1-2026-05-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Inside the declared fit window M in {2,3,5,8}, the dense Z2 x Z2 extension shows a positive-row mass-bump fit, with in-window negative rows disclosed and excluded by the runner's delta > 0 guard.  _(class `C`)_
- **chain closes:** True — The source note's scoped numerical statements match the completed SHA-pinned cache, and the runner source computes the Z2xZ2 DAG rows and applies the declared delta > 0 fit filter rather than hard-coding the stated coefficients. The disclosed negative rows keep the claim bounded to the positive-row subfit and weak distance-sweep observations.
- **rationale:** The clean result is limited to the exact finite runner surface and the explicitly narrowed positive-row subfit/distance-sweep facts. Residual risk is that the fit window and positive-row filter are analysis choices and do not by themselves imply a physical gravity law, rowwise positivity, Born safety, or upstream coexistence closure; those broader readings are outside the audited scope.
- **auditor confidence:** high

### `hkd_correspondence_general_charts_bounded_theorem_note_2026-06-12`

- **Note:** [`HKD_CORRESPONDENCE_GENERAL_CHARTS_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/HKD_CORRESPONDENCE_GENERAL_CHARTS_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-chart audit of the listed anchor and S1 charts under the fixed dense nearest-neighbor Hamiltonian, E=-0.6 Schur decimation on axes 0 and 2, and even-d2 truncation convention.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-hkd_correspondence_general_charts_bounded_theorem_note_2026-06-12-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** For the listed checked charts, the runner-computed real Schur H_kd_after vanishes exactly when the independently counted misaligned survivors vanish, and exactly when all chart periods are even.  _(class `C`)_
- **chain closes:** True — The runner source actually constructs the finite Hamiltonian, performs the two Schur complements, truncates by even periodic d2, measures H_kd_after, and separately enumerates the parity misalignment count. Within the explicitly bounded checked-chart scope, no cited upstream or external bridge is needed.
- **rationale:** The claim is scoped to a fixed finite list of checked charts and a fixed numerical convention, not to an all-period or continuum theorem. The runner computes the Schur quantities from the stated finite Hamiltonian and computes the parity diagnostic separately, so the three-way coincidence is not merely a symbol renaming or printed constant. The frozen anchor values are used as regression gates, but the load-bearing chart classification is recomputed within the packet and no external comparator or open dependency is imported.
- **auditor confidence:** high

### `hkd_entry_sum_full_l_closure_narrow_theorem_note_2026-06-12`

- **Note:** [`HKD_ENTRY_SUM_FULL_L_CLOSURE_NARROW_THEOREM_NOTE_2026-06-12.md`](../../docs/HKD_ENTRY_SUM_FULL_L_CLOSURE_NARROW_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the d=3 step-2 chart family K-periods=(L/2,L,L/2), the combinatorial kept-decimated support existence criterion is audited for even L >= 8, with dense Schur/H_kd anchor agreement only for L in {8,10,12,14,16,18}.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-hkd_entry_sum_full_l_closure_narrow_theorem_note_2026-06-12-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Since d2 = sum_i delta_i^2 = sum_i delta_i mod 2, a misaligned survivor exists exactly when some chart period is odd; for (L/2,L,L/2) with even L this is exactly L != 0 mod 4.  _(class `A`)_
- **chain closes:** True — The retained cited period-parity lemma gives parity preservation iff all periods are even, and this family has all periods even exactly when L = 0 mod 4. The runner source genuinely computes the dense finite anchors and exact combinatorial support counts; frozen values are used as regression gates, not as the sole computation.
- **rationale:** The full-L part is an algebraic parity closure over a retained upstream lemma, and the bounded dense-anchor bridge is computed self-contained from the stated Hamiltonian/Schur construction for the finite anchor grid. No external comparator, tuned empirical value, open bridge, or non-retained dependency is used. The theorem’s scope is correctly bounded: it does not claim dense Hamiltonian magnitude closure beyond the listed anchors.
- **auditor confidence:** high

### `holographic_probe_note_2026-04-11`

- **Note:** [`HOLOGRAPHIC_PROBE_NOTE_2026-04-11.md`](../../docs/HOLOGRAPHIC_PROBE_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Within the fixed finite 2D periodic staggered-lattice Dirac-sea correlation-matrix probe for sides 8, 10, 12, and 14, entropy and Schmidt rank fit boundary size better than volume for G=0 and G=10, with the G=10 boundary coefficient about 12.0% lower than the free coefficient.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-holographic-boundary-auditor-2026-05-03`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The current runner computes the stated correlation-matrix entropies/ranks and reports boundary-fit R^2 exceeding volume-fit R^2 for both G=0 and G=10 globally and per side, with boundary slopes 0.186053 and 0.211399 giving ratio 0.8801.  _(class `C`)_
- **chain closes:** True — The finite-model computation directly evaluates the claimed observable and fit comparison under the stated parameters; the conclusion is only the bounded numerical boundary-preference statement and coefficient shift.
- **rationale:** The audited claim is tightly bounded to the finite-lattice runner's fixed model, observable, regions, and fit criterion. The provided runner output matches the note's numerical values, including global entropy fits, rank fits, per-side boundary preference, and the gravity/free coefficient ratio. No stronger holographic, continuum, Bekenstein-Hawking, AdS/CFT, or quantum-gravity conclusion is needed for the scoped statement.
- **auditor confidence:** high

### `i3_zero_exact_theorem_note`

- **Note:** [`I3_ZERO_EXACT_THEOREM_NOTE.md`](../../docs/I3_ZERO_EXACT_THEOREM_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Given linearly additive disjoint-path amplitudes and quadratic Hilbert-surface probabilities P_S=|A_S|^2, the Sorkin third-order interference parameter I_3 vanishes identically by inclusion-exclusion.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-fresh-agent-2026-05-03-i3-zero-exact-independent-2`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** inclusion-exclusion then cancels all terms of degree higher than two; therefore I_3 = 0 exactly  _(class `A`)_
- **chain closes:** True — The conclusion follows from expanding |A+B+C|^2, |A+B|^2, |A+C|^2, and |B+C|^2 and applying the Sorkin inclusion-exclusion signs; all degree-one and degree-two terms cancel. There are no dependency notes in the restricted packet, and none are needed for the scoped algebraic statement.
- **rationale:** The scoped claim is an algebraic theorem over explicitly assumed Hilbert-surface inputs: linear amplitude composition and P=|A|^2. The source note expressly does not claim a standalone Born-rule derivation, so the hidden-physics risk is excluded from the audited scope. The runner verifies the relevant algebra and lattice examples, but its broader 'Born rule from Hilbert space' wording should not be allowed to expand the claim beyond the source note's safe scope.
- **auditor confidence:** high

### `independent_generators_heldout_note`

- **Note:** [`INDEPENDENT_GENERATORS_HELDOUT_NOTE.md`](../../docs/INDEPENDENT_GENERATORS_HELDOUT_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The in-sample classifier rule (avg_deg >= 10.415 and reach_frac >= 0.859) is applied without refit to nine scripted independent generator families, yielding only 2/9 full-battery passes, 4/9 hard-coded prediction accuracy, and 6/9 no-refit rule accuracy.  _(class `C`)_
- **chain closes:** True — The live runner rebuilds the nine named generator families, applies the same five-condition battery and frozen rule, and reproduces the negative table: only E1_er_p005 and E2_er_p020 pass, hard-coded predictions score 4/9, and the no-refit classifier rule scores 6/9.
- **rationale:** The finite negative result closes on its own terms: the checked-in runner contains the nine generator constructors, the hard-coded prediction dictionary, the five-condition battery, and the frozen avg_deg/reach_frac rule, and live replay matches the source note's pass/fail and accuracy claims. The decisive rule failures R1, R3, and X1 all satisfy the frozen structural thresholds but fail the actual battery, while only the two Erdős-Rényi families pass the full package. This clean verdict is narrow: it certifies this deterministic nine-family held-out replay and the checked-in prediction table, not an exhaustive statistical theorem over all independent generator laws or independent timestamp proof beyond the artifact chain.
- **auditor confidence:** high

### `inverse_problem_note`

- **Note:** [`INVERSE_PROBLEM_NOTE.md`](../../docs/INVERSE_PROBLEM_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded inverse-problem graph-perturbation replay on the specified 3D valley-linear harness, where Born is clean for all five variants, TOWARD holds for baseline/asym/jitter/sparse, heavy_delete_70 is AWAY, and k=0/no-field controls are zero.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the specified h=0.5, W=8, L=12, max_d=3 harness, Born holds across all five variants while TOWARD holds for the four non-heavy-delete variants and fails for heavy_delete_70.  _(class `C`)_
- **chain closes:** True — The runner constructs the five graph variants, computes Born, gravity sign, k=0, and no-field controls, and asserts the narrowed table stated in the note. The audited conclusion is explicitly bounded to this harness and does not claim universal graph-structure irrelevance.
- **rationale:** The current cache reproduces the narrowed table exactly, including the heavy_delete_70 AWAY counterexample that retracts the older universal-robustness framing. The note's safe conclusion follows from the finite runner output and its assertions, with no hidden dependency needed for the bounded harness statement. Residual risk is the ordinary finite-sample limitation: different graph perturbations, strengths, phases, or lattice parameters are outside this audit.
- **auditor confidence:** high

### `k_dependence_review_safe_note`

- **Note:** [`K_DEPENDENCE_REVIEW_SAFE_NOTE.md`](../../docs/K_DEPENDENCE_REVIEW_SAFE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Within the provided generative causal DAG runner family, for N=[25,30,40,60,80], 16 shared seeds, and k in [1,2,3,5,7,10,15], the audited result is that fitted k-dependent ceiling behavior is present but not a clean or window-robust universal alpha(k) claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T175957Z-7a52dc92-k_dependence_review_safe-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The fixed-window rerun shows negative per-seed exponents with strongly overlapping bootstrap confidence intervals across k, and a late-N window materially shifts the fitted seed_alpha values, so the evidence is fit-window-sensitive and does not support a universal alpha(k) law.  _(class `C`)_
- **chain closes:** True — The primary runner computes pur_min values through the included helper chain, fits per-seed log-log slopes, bootstraps the mean slopes, and performs a second-window comparison. The conclusion is bounded to this runner-defined graph family and fit protocol, and the included code/output support that bounded statement.
- **rationale:** The runner source is not a mere printout: it constructs the seed x k x N table from pur_min_single_k, computes per-seed slopes and bootstrap intervals, and then validates the frozen note values. The helper chain is included and contains the load-bearing graph generation, field propagation, density normalization, and purity calculation rather than importing the contested result from another note. The result is only a bounded computational theorem about this graph family and fit protocol, not a universal physical alpha(k) law.
- **auditor confidence:** high

### `koide_anticommuting_operator_derivation_theorem_note_2026-05-10`

- **Note:** [`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md`](../../docs/KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For real symmetric H on R^3 satisfying {H, Γ_χ} = 0, every nonzero-eigenvalue eigenvector obeys ⟨v|Γ_χ|v⟩ = 0 and hence Q(v) = 2/3 and the stated Fourier norm split.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T165623Z-ba1d1130-00003-koide_anticommuting_operator`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Hermiticity, anti-commutation, and Hv = λv imply λ⟨v|Γ_χ|v⟩ = −λ⟨v|Γ_χ|v⟩, so ⟨v|Γ_χ|v⟩ = 0 when λ ≠ 0.  _(class `A`)_
- **chain closes:** True — The implication follows directly from Hermiticity, anti-commutation, and the nonzero eigenvalue hypothesis. Expanding Γ_χ = (2/3)J − I then gives the Koide relation, while orthogonal Fourier decomposition gives the norm split.
- **rationale:** The load-bearing argument is a valid standalone algebraic closure and imports no empirical value, open authority, or framework realization. The supplied runner performs genuine symbolic matrix checks and explicit eigenvector tests rather than merely printing expected constants. The note correctly confines its conclusion to the conditional theorem and does not claim that the required H exists in the framework.
- **auditor confidence:** high

### `koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05`

- **Note:** [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](../../docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For the supplied 2*pi/3 proper cubic rotation about the (1,1,1) body diagonal, each nonidentity C3 element has real normal-plane determinant det(I-g)=3 and the defined inverse-normal-determinant group average is 2/9.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt-5.6-sol-xhigh-c3-fixed-locus-second-seat-2026-07-12`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** For k=1,2 the real normal determinants det_R(I-P^k|_N) are both 3, so the defined group average is (1/3)(1/3+1/3)=2/9.  _(class `C`)_
- **chain closes:** True — The Lattice axiom supplies the proper cubic body-diagonal rotation, and exact two-dimensional linear algebra computes both nonidentity normal determinants without any additional physical bridge. Substitution into the explicitly defined finite group average gives 2/9.
- **rationale:** In the displayed integer basis, independent recomputation gives N=[[0,-1],[1,-1]], N^2=[[-1,1],[-1,0]], and det(I-N)=det(I-N^2)=3; independently, the invariant rotation formula det(I-R_theta)=2-2*cos(theta) gives 3 at theta=+/-2*pi/3. Averaging the two inverse determinants with the stated 1/|C3| factor gives exactly 2/9. The source explicitly excludes physical-axis selection and all APS, charged-lepton, readout, probability, and global-identification bridges, so no such bridge is being ratified; residual risk is confined to downstream uses that exceed this narrow scope.
- **auditor confidence:** high

### `koide_cone_completing_root_narrow_theorem_note_2026-05-02`

- **Note:** [`KOIDE_CONE_COMPLETING_ROOT_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/KOIDE_CONE_COMPLETING_ROOT_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For arbitrary positive real v,w, the explicit u_small and u_large are exactly the two roots placing (u,v,w) on the stated Koide cone; they satisfy the cone identity, Vieta identities, the u_small ratio identity, and the stated u_small positivity criterion.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-fresh-koide-cone-completing-root-narrow-20260505`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** Rearranging the Koide cone as u^2 - 4(v+w)u + (v^2+w^2-4vw)=0 gives discriminant 12(v^2+4vw+w^2), hence roots u=2(v+w) ± sqrt(3(v^2+4vw+w^2)).  _(class `A`)_
- **chain closes:** True — The scoped claim is pure polynomial algebra over positive real v,w. The quadratic-formula derivation, substitution identities, Vieta relations, ratio equivalence, and positivity inequality close without cited authorities or physical observable bridges.
- **rationale:** Clean within the note's stated narrow algebra-only boundary. The load-bearing step is an elementary quadratic-formula identity, and the cached runner completes with nine class-A exact algebra checks covering the roots, cone identities, Vieta relations, ratio identity, and representative concrete cases. Residual risk is only downstream scope drift: this audit does not ratify any charged-lepton, sqrt-mass, selected-line, or physical-point identification.
- **auditor confidence:** high

### `koide_cone_three_form_equivalence_narrow_theorem_note_2026-05-02`

- **Note:** [`KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Standalone polynomial-algebra equivalence over real triples between the orbit-slot quadratic, the explicit cyclic linear-map quadratic, the polynomial ratio form, and the divided ratio form when u+v+w is nonzero, plus non-emptiness by explicit examples.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-fresh-koide-cone-three-form-equivalence-narrow-20260505`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** Direct expansion shows 2 r0^2 - r1^2 - r2^2 = 2 [4(uv + uw + vw) - (u^2 + v^2 + w^2)], and 3(u^2+v^2+w^2)-2(u+v+w)^2 = -F_orbit.  _(class `A`)_
- **chain closes:** True — The claim closes as elementary algebra over explicitly defined real variables: F_cyclic = 2 F_orbit and F_ratio' = -F_orbit. The divided ratio form is correctly scoped to u+v+w != 0, and no physical Koide, mass-amplitude, or Gamma-orbit identification is imported.
- **rationale:** The load-bearing step is exact polynomial expansion under an explicit linear definition of r0, r1, and r2. The cached runner completes and independently checks the symbolic identities, the ratio restriction, non-empty cone examples, and the off-cone uniform triple, all as class A algebra. Residual risk is only scope creep if downstream users treat this as a physical charged-lepton theorem, which this note explicitly does not claim.
- **auditor confidence:** high

### `koide_cyclic_projector_block_democracy_note_2026-04-18`

- **Note:** [`KOIDE_CYCLIC_PROJECTOR_BLOCK_DEMOCRACY_NOTE_2026-04-18.md`](../../docs/KOIDE_CYCLIC_PROJECTOR_BLOCK_DEMOCRACY_NOTE_2026-04-18.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded algebraic claim that, on the stated cyclic Hermitian image with the given real-trace norms, equal scalar-line and traceless-plane block power is exactly the response-space Koide equation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-koide_cyclic_projector_b-025`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Demanding equal block power E_+ = E_perp gives r0^2/3 = (r1^2 + r2^2)/6, equivalently 2 r0^2 = r1^2 + r2^2.  _(class `A`)_
- **chain closes:** True — The runner symbolically verifies the block powers from the displayed basis and trace metric, and the equivalence to 2 r0^2 = r1^2 + r2^2 is direct algebra. The note explicitly leaves the dynamical reason for imposing equal block power outside scope.
- **rationale:** Within its bounded scope, the claim closes as an algebraic identity over the stated cyclic basis, coefficients, and real-trace metric. The runner source performs actual numeric and symbolic computations of the Gram matrix, block powers, and equation equivalences rather than merely printing constants. The observed charged-lepton section is only an external witness check and is not needed for the algebraic selector equivalence.
- **auditor confidence:** high

### `koide_cyclic_wilson_3_response_narrow_theorem_note_2026-05-02`

- **Note:** [`KOIDE_CYCLIC_WILSON_3_RESPONSE_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/KOIDE_CYCLIC_WILSON_3_RESPONSE_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `decoration`
- **claim_scope:** Conditional algebraic reconstruction of the cyclic Hermitian descendant from three response coordinates, assuming the cited cyclic-compression basis and the existence of the local Wilson first-variation.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_koide_dweh_cyclic_compression_note_2026-04-18`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-koide_cyclic_wilson_3_re-050`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Given the cyclic Hermitian basis, the Frobenius-dual reconstruction H_cyc = (r0/3) B0 + (r1/6) B1 + (r2/6) B2 recovers the three responses r_i = dW(B_i).  _(class `A`)_
- **chain closes:** True — The algebraic reconstruction closes over the retained cited cyclic-compression input and standard Frobenius duality. It does not close physical existence or Koide identification claims, which the note explicitly leaves out of scope.
- **rationale:** The load-bearing step is a class A basis-and-dual-pairing calculation. The runner source performs exact rational checks of the cyclic basis, orthogonality, and reconstruction, while the one runner failure is an audit-ledger status expectation rather than a mathematical failure. Because the chain reduces to a single upstream retained cyclic-compression claim plus standard algebra and contains no external comparator checks, the rubric classifies it as audited_decoration rather than audited_clean.
- **decoration parent:** `koide_dweh_cyclic_compression_note_2026-04-18`
- **auditor confidence:** high

### `koide_dimensionless_objection_toy_conditional_algebraic_checks_narrow_theorem_note_2026-05-16`

- **Note:** [`KOIDE_DIMENSIONLESS_OBJECTION_TOY_CONDITIONAL_ALGEBRAIC_CHECKS_NARROW_THEOREM_NOTE_2026-05-16.md`](../../docs/KOIDE_DIMENSIONLESS_OBJECTION_TOY_CONDITIONAL_ALGEBRAIC_CHECKS_NARROW_THEOREM_NOTE_2026-05-16.md)
- **claim_type:** `open_gate`
- **claim_scope:** Conditional exact rational identities T1-T9 inside A_TOY=(A1,A2,A3,A4,A5), including the in-toy Q and delta admission-counting statements, with no retained-grade propagation.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-koide_dimensionless_objection_toy_conditional_algebraic_checks_narrow_theorem_note_2026-05-16-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Each identity has the strict form '(A_subset) entails (T_k)' and reduces, under that subset, to direct rational arithmetic in Q.  _(class `A`)_
- **chain closes:** False — The in-toy arithmetic closes once A1-A5 are assumed, and the runner source genuinely uses exact Fraction arithmetic for those identities. The restricted packet does not derive A1-A5 from retained authorities, so retained-grade closure is missing.
- **rationale:** Issue: The source note explicitly admits A1-A5, including the two-channel carrier, central Z label, endpoint algebra/section, and eta_APS=2/9. Why this blocks: the algebraic checks are correct under those assumptions, but no cited retained authority in the restricted packet derives the admissions. Repair target: provide a bridge theorem deriving or citing retained-grade support for A1-A5, or keep the row as a conditional toy certificate. Claim boundary until fixed: T1-T9 hold only as exact in-toy rational identities under the named admissions, with no retained Koide, delta, or no-go propagation.
- **auditor confidence:** high

### `koide_dweh_cyclic_compression_note_2026-04-18`

- **Note:** [`KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md`](../../docs/KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact algebraic cyclic compression of a given Hermitian charged block H_e in Herm(3) to the C-invariant three-real subspace span_R{I, C+C^2, i(C-C^2)}, including the response reconstruction formula.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-fresh-second-koide_dweh_cyclic_compression_note-20260505`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** H_e -> H_cyc := P_cyc(H_e), with P_cyc(X)=(1/3) sum_{k=0}^2 C^k X C^{-k}, has image span_R{B0,B1,B2} and is reconstructed from r0,r1,r2 by H_cyc=(r0/3)B0+(r1/6)B1+(r2/6)B2.  _(class `A`)_
- **chain closes:** True — The audited scope is a finite-dimensional linear-algebra theorem: cyclic group averaging is a canonical projector, its image is the stated circulant Hermitian basis, and the trace responses reconstruct the projected component. This does not audit the upstream microscopic source law, Koide selector principle, or charged-lepton readout, which the note explicitly leaves open.
- **rationale:** Within the bounded algebraic scope, the load-bearing step closes: the note states the projector, the basis-level action, the generic coefficient formula, and the response reconstruction, and the cached runner confirms all algebraic identities with PASS=11 FAIL=0. The two D-class checks are only witness/comparator checks for the observed amplitude target and are not needed to prove the compression theorem. This clean verdict must not be read as closing the microscopic source law for (r0,r1,r2), the selector principle, or the final charged-lepton readout, all of which remain explicitly outside this claim scope.
- **auditor confidence:** high

### `koide_first_order_section_tie_vs_outcome_label_residual_localization_bounded_theorem_note_2026-07-11`

- **Note:** [`KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`](../../docs/KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The finite first-order determinant calculation, tied-versus-untied section identity, and localization of the still-open physical stage/readout residual.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** A finite Grassmann calculation gives det(M) to first order, while imposing c=conjugate(b) only after the holomorphic calculation introduces the mixed derivative -3a without selecting the physical weight or outcome stage.  _(class `A`)_
- **chain closes:** False — The local determinant and section algebra close, but the stage choice, energy/readout law, and OS realization are supplied or open, and seven scientific direct parents remain unaudited.
- **rationale:** Issue: the independent Berezin/determinant calculation confirms first-power det(M), holomorphy before restriction, the tied mixed derivative -3a, the modulus-squared block determinant, and the site/link-center parity comparison, but none of these calculations selects when K-reality is imposed or supplies the physical energy/readout law. Why this blocks: all seven scientific one-hop parents are unaudited and the declared OS/stage domain lacks a retained lattice-motion-covariant, record-decidable certificate, so the residual localization cannot become an unconditional physical selection theorem. Repair target: retain the determinant, channel-holomorphy, realization, custody, and no-go parents; then provide the explicit OS reconstruction and stage/readout certificate. Claim boundary until fixed: on the supplied finite first-order Grassmann surface, tying before or after the untied holomorphic calculation agrees pointwise after restriction but does not choose the physical stage or Koide weight.
- **open / conditional deps cited:**
  - `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`
  - `KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  - `KOIDE_GENERATION_CHANNEL_SPACE_HOLOMORPHY_CHANNEL_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  - `KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md`
  - `KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`
  - `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
  - `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`
- **auditor confidence:** high
- **No-Go Discipline:** `PASS`

### `koide_gamma_axis_covariant_full_cube_orbit_law_note_2026-04-18`

- **Note:** [`KOIDE_GAMMA_AXIS_COVARIANT_FULL_CUBE_ORBIT_LAW_NOTE_2026-04-18.md`](../../docs/KOIDE_GAMMA_AXIS_COVARIANT_FULL_CUBE_ORBIT_LAW_NOTE_2026-04-18.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact finite-matrix orbit identity for the runner-defined JW Gamma_i family, T1 species basis, full-cube C3 bit-cycle, and transported full-cube template W1(u,v,w,z), including nullity of the fourth slot in axis-matched returns.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-judicial-019e1256-fd1f-79b2-ba3e-71b35dc8c1e0`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** The axis-matched second-order returns D_i = P_{T_1} Gamma_i W_i Gamma_i P_{T_1}|_{species} obey D_1 = diag(u,v,w), D_2 = diag(w,u,v), and D_3 = diag(v,w,u).  _(class `A`)_
- **chain closes:** True — The runner directly constructs the finite matrices, projectors, bit-cycle, and template slots, then verifies exact slot images whose arbitrary-template result follows by linearity. Under the audit rubric this is an algebraic identity check over explicitly defined inputs, not a class C first-principles computation producing a new physical number from the axiom. The clean verdict is therefore ratified with the second audit's narrower A-class scope.
- **rationale:** The runner directly constructs the finite matrices, projectors, bit-cycle, and template slots, then verifies exact slot images whose arbitrary-template result follows by linearity. Under the audit rubric this is an algebraic identity check over explicitly defined inputs, not a class C first-principles computation producing a new physical number from the axiom. The clean verdict is therefore ratified with the second audit's narrower A-class scope.
- **auditor confidence:** high

### `koide_gamma_orbit_cyclic_return_candidate_note_2026-04-18`

- **Note:** [`KOIDE_GAMMA_ORBIT_CYCLIC_RETURN_CANDIDATE_NOTE_2026-04-18.md`](../../docs/KOIDE_GAMMA_ORBIT_CYCLIC_RETURN_CANDIDATE_NOTE_2026-04-18.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact algebraic reduction of the local Gamma_1 three-slot return, with cited full-cube cyclic transport, to the Hermitian circulant Koide carrier; excludes derivation of the microscopic values or selector law.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e12a2-cc4c-7ab2-bcee-ced41d166332`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The exact retained Gamma_1 second-order return gives R_{Gamma_1}(W_1) = diag(u, v, w), and Fourier transport gives H_Gamma = F diag(u, v, w) F^dagger = (r0/3)B0 + (r1/6)B1 + (r2/6)B2 with r0 = u + v + w, r1 = 2u - v - w, r2 = sqrt(3)(v - w).  _(class `A`)_
- **chain closes:** True — Within the scoped claim, the chain closes by finite matrix/projector algebra plus symbolic Fourier transport, and the cited retained full-cube orbit-law authority supplies the cross-axis cyclic family. The source note explicitly leaves the value law for (u, v, w) and the selector mechanism open.
- **rationale:** The load-bearing step is exact linear algebra on an already specified three-slot return object, and the runner computes the finite Gamma/projector shape and symbolic circulant decomposition rather than deriving a hidden fitted parameter. The one-hop axis-covariant authority is retained-grade and closes the cross-axis basis step that the runner still labels as candidate. The observed charged-lepton witness imports measured amplitudes, but it is not used to claim a value-law or selector derivation, which the note correctly marks as open.
- **auditor confidence:** high

### `koide_gamma_orbit_exponential_value_law_candidate_note_2026-04-18`

- **Note:** [`KOIDE_GAMMA_ORBIT_EXPONENTIAL_VALUE_LAW_CANDIDATE_NOTE_2026-04-18.md`](../../docs/KOIDE_GAMMA_ORBIT_EXPONENTIAL_VALUE_LAW_CANDIDATE_NOTE_2026-04-18.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited the restricted claim that the imported neutrino-sector H_* exponential family, with the Koide-cone small branch and an optimized beta, gives a calibrated charged-lepton amplitude-direction witness inside the exact Gamma/full-cube three-slot template.
- **audit_status:** ~~audited_numerical_match~~
- **effective_status:** ~~audited_numerical_match~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-koide_gamma_orbit_exponential_value_law_candidate_note_2026-04-18-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At beta_* ~= 0.6335716, the small-root branch of u(beta)=2(v+w)-sqrt(3(v^2+4vw+w^2)) with v,w read from exp(beta H_*) matches the PDG sqrt(m) direction essentially exactly.  _(class `G`)_
- **chain closes:** True — The algebraic cone root formula and positivity of exp(beta H_*) close for the stated family, and the runner computes the reported optimized numerical match. The closure is only at calibrated-witness scope; H_*, the small-root branch choice, and beta_* are not derived from retained charged-lepton dynamics.
- **rationale:** Issue: the load-bearing match uses an observationally pinned H_* from the helper, selects the small-root branch, and optimizes beta against hard-coded PDG sqrt(m) comparators. Why this blocks: those choices make the result a tuned calibrated witness rather than a first-principles charged-lepton value-law derivation. Repair target: derive H_*, the branch, and beta selection from retained charged-lepton microscopic dynamics without PDG fitting. Claim boundary until fixed: a sharp one-parameter numerical witness in the exact semigroup/template class.
- **auditor confidence:** high

### `koide_gamma_orbit_selector_bridge_note_2026-04-18`

- **Note:** [`KOIDE_GAMMA_ORBIT_SELECTOR_BRIDGE_NOTE_2026-04-18.md`](../../docs/KOIDE_GAMMA_ORBIT_SELECTOR_BRIDGE_NOTE_2026-04-18.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Given the stated linear map from (u,v,w) to (r0,r1,r2), the cyclic Koide selector 2r0^2 = r1^2 + r2^2 is exactly equivalent to u^2 + v^2 + w^2 = 4(uv + uw + vw), and for positive amplitudes to Q = 2/3.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e1250-6c2d-7422-99c3-d0876e8adefb`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Using r0 = u + v + w, r1 = 2u - v - w, and r2 = sqrt(3)(v - w), the note asserts 2 r0^2 - r1^2 - r2^2 = 2 [4(uv + uw + vw) - (u^2 + v^2 + w^2)].  _(class `A`)_
- **chain closes:** True — The polynomial pullback and the equivalence to the standard sqrt(m) Koide form follow by direct algebra from the displayed map. The physical derivation of the Gamma orbit slots, the value law for (u,v,w), and the dynamical reason for the selector are explicitly outside this audited scope.
- **rationale:** The load-bearing result is an exact algebraic identity, and the runner verifies the same symbolic expansion plus the algebraic equivalence to Q = 2/3. The two numeric checks only witness the usual charged-lepton Koide proximity and are not needed for theorem closure. This clean verdict covers the selector pullback under the stated map only; it does not audit or close the Gamma orbit value law or dynamical selector derivation.
- **auditor confidence:** high

### `koide_generation_weight_dial_shape_forced_value_unfixed_qualification_bounded_theorem_note_2026-07-11`

- **Note:** [`KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`](../../docs/KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The invariant density-state dial shape under the supplied C3 and antiunitary context, and the exhibited nonselection of its singlet-doublet coordinate.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** C3 invariance makes rho character-diagonal and the supplied antiunitary exchanges the two nontrivial characters, forcing rho=diag(p_s,p_d/2,p_d/2) while unequal cell ranks leave p_s/p_d free.  _(class `A`)_
- **chain closes:** False — The representation algebra closes, but the density form, canonical context, and antiunitary are supplied, and three scientific direct parents remain unaudited.
- **rationale:** Issue: the commutant, antiunitary-exchange, invariant-state, rank/orbit, and two-point calculations are correct, but the density/Born form and readout context are supplied and the K/CPT and two no-go parents are unaudited. Why this blocks: the one-parameter dial is only a conditional classification and the Qualification cannot by itself make the registered point into derivation output. Repair target: retain the context/no-go parents and derive a density-weight/readout bridge with a lattice-motion-covariant, record-decidable domain. Claim boundary until fixed: within the supplied density-state and invariance class, doublet equality is forced while the singlet-doublet ratio remains free.
- **open / conditional deps cited:**
  - `KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md`
  - `KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`
  - `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`
- **auditor confidence:** high
- **No-Go Discipline:** `PASS`

### `koide_kappa_bookkeeping_flow_class_fixed_point_inversion_and_lane_scoping_bounded_theorem_note_2026-07-11`

- **Note:** [`KOIDE_KAPPA_BOOKKEEPING_FLOW_CLASS_FIXED_POINT_INVERSION_AND_LANE_SCOPING_BOUNDED_THEOREM_NOTE_2026-07-11.md`](../../docs/KOIDE_KAPPA_BOOKKEEPING_FLOW_CLASS_FIXED_POINT_INVERSION_AND_LANE_SCOPING_BOUNDED_THEOREM_NOTE_2026-07-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The positive-kappa bookkeeping flow class, its fixed set and conjugacy, the kappa=1,2 evaluations, and conditional fixed-point inversion with report-only comparators.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** With x=p_d/p_s=kappa r, independent agreement conditioning sends x to x^2 and therefore induces f_kappa(r)=kappa r^2, whose positive fixed point is 1/kappa.  _(class `A`)_
- **chain closes:** False — The algebra closes, but independent agreement conditioning and physical bookkeeping are supplied, and all three direct scientific dependencies remain unaudited.
- **rationale:** Issue: the odds-map, fixed-point, projective-chart, conjugacy, inversion, and comparator arithmetic are correct, but independent agreement conditioning and physical kappa identification have no retained certificates and all three direct parents are unaudited. Why this blocks: the exact map class cannot select a physical lane coefficient or support any comparator inference. Repair target: retain the parents and derive a lattice-motion-covariant, record-decidable agreement/readout law that fixes kappa. Claim boundary until fixed: kappa is only a supplied positive bookkeeping coefficient and the displayed decimal table is report-only arithmetic.
- **open / conditional deps cited:**
  - `RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`
  - `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`
  - `FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md`
- **auditor confidence:** high
- **No-Go Discipline:** `PASS`

### `koide_occupancy_from_locked_record_outcomes_bounded_note_2026-07-03`

- **Note:** [`KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md`](../../docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The four-channel K-real determinant localization and the conditional one-locked-possibility statistical-slot comparison on the explicitly enumerated local surface.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** The four determinant localizations are exact, while one locked record content can determine two component readouts and only the supplied one-possibility/one-slot rule creates the one-versus-two slot mismatch.  _(class `A`)_
- **chain closes:** False — The local formulas close, but the statistical-slot rule and K/CPT outcome context are supplied conditions and all three scientific direct dependencies remain unaudited.
- **rationale:** Issue: the local determinant, Gaussian, Record-countermodel, and endpoint algebra is correct, but the statistical-slot equality lacks a retained certificate and the three direct scientific parents are unaudited. Why this blocks: neither physical slotting nor the current-source nonselection boundary can propagate at retained grade. Repair target: retain the three named parents and supply a record-decidable, lattice-motion-covariant law-domain theorem for the one-possibility/one-slot rule. Claim boundary until fixed: the four displayed matrices and the explicitly supplied one-slot and aggregate-energy laws have only the stated conditional local consequences.
- **open / conditional deps cited:**
  - `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`
  - `KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`
  - `KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`
- **auditor confidence:** high
- **No-Go Discipline:** `PASS`

### `kraus_choi_representation_normalization_reconciled_narrow_theorem_note_2026-06-05`

- **Note:** [`KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md`](../../docs/KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Finite-dimensional Kraus–Choi correspondence on finite qubit-region matrix algebras, using the unnormalized Choi convention consistently for reconstruction, Kraus extraction, CP/TP conditions, and the two stated mixed-convention scaling failures.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00349-kraus_choi_representation_no`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** Under the unnormalized maximally entangled-vector convention, expanding the Choi matrix in matrix units gives exactly Φ(ρ)=Tr₁[(ρᵀ⊗𝟙)C_Φ] and K_a=√λ_a·reshape(v_a)ᵀ, with no additional d-factor.  _(class `A`)_
- **chain closes:** True — Direct matrix-unit expansion proves the reconstruction and partial-trace identities for arbitrary finite d, while spectral decomposition of a positive Choi matrix gives the stated Kraus operators and operator-sum map. The accepted Qubit premise supplies the finite-region matrix-algebra substrate without adding an open physical bridge.
- **rationale:** The formulas are a genuine algebraic normalization closure, not a definition, tuned numerical match, or external-comparator inference. The runner source performs substantive symbolic and numerical calculations, including exact M₂ reconstruction, d=2 and d=4 round trips, named channels, a non-CP boundary example, and both mixed-convention scaling defects; it does not hard-code the conclusions. Although the finite tests alone would not establish the universal theorem, the all-d result follows directly from the displayed matrix-unit and spectral-decomposition algebra.
- **auditor confidence:** high

### `kubo_range_of_validity_note`

- **Note:** [`KUBO_RANGE_OF_VALIDITY_NOTE.md`](../../docs/KUBO_RANGE_OF_VALIDITY_NOTE.md)
- **claim_type:** `decoration`
- **claim_scope:** Algebraic corollary, with the provided runner's finite-family accounting, that families selected by the measured Kubo-linearity ratio have F~M near 1.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_linear_response_true_kubo_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-kubo_range_of_validity_n-028`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** First-order linear response gives delta_z(s) approximately equal to kubo_true * s, so |delta_z(s)| is proportional to s^1 and the log-log F~M slope is exactly 1.  _(class `A`)_
- **chain closes:** True — The implication from linear response to F~M = 1 closes as standard log-log slope algebra once the upstream Kubo coefficient and the runner's selected linearity subset are accepted. It does not establish an independent positive theorem because the F~M result is forced by the same measured linearity condition used to define the subset.
- **rationale:** Issue: the decisive step is the algebraic identity that a response proportional to s has log-log slope 1. Why this blocks: the runner's headline 15/41 subset is selected by measured linearity ratios across the same strengths used to fit F~M, so the near-1 F~M result is a corollary of the subset definition rather than an independent derivation of a new battery condition. Repair target: present this as a bounded range-of-validity diagnostic under the true-Kubo parent, or add an independent criterion that does not mathematically enforce the F~M slope. Claim boundary until fixed: the runner supports that its selected linearity-regime families have the reported F~M statistics, conditional on the upstream Kubo coefficient.
- **decoration parent:** `linear_response_true_kubo_note`
- **auditor confidence:** high

### `landau_peierls_prefactor_native_derivation_bounded_theorem_note_2026-06-13`

- **Note:** [`LANDAU_PEIERLS_PREFACTOR_NATIVE_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-13.md`](../../docs/LANDAU_PEIERLS_PREFACTOR_NATIVE_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-13.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Within the stated smooth one-band 2D magnetic Peierls/Moyal star-product expansion on a periodic Brillouin torus, the Landau-Peierls response prefactor -1/12 is derived and checked against non-fitted square-lattice Peierls diagonalization.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-landau_peierls_prefactor_native_derivation_bounded_theorem_note_2026-06-13-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The magnetic star-power recursion gives the local B^2 density, and the checked periodic divergence identity converts the G'''(E)Q term into -2 G''(E) det Hess(E), yielding c2=-(1/24) integral G''(E) det Hess(E) and chi=2c2=-(1/12) integral f'(E) det Hess(E).  _(class `C`)_
- **chain closes:** True — The source explicitly scopes the theorem to the supplied magnetic star product, and the runner computes the B^2 coefficient by symbolic star-power recursion plus a separately verified divergence identity. The finite-lattice Hofstadter diagonalization is independent of the LP formula and supports the sign/factor convention rather than supplying a fitted prefactor.
- **rationale:** The runner source does not hard-code the contested -1/12 as an input; it derives the prefactor from the symbolic B^2 star expansion and checks that a nearby wrong prefactor leaves a residual. The periodic-torus reduction of the Q term is explicitly verified symbolically, and the direct Peierls diagonalization is a separate finite-lattice comparator within the stated convention. This clean verdict is bounded to the supplied one-band Peierls/Moyal expansion and does not audit derivation of that expansion from broader framework axioms or a universal thermodynamic-limit theorem.
- **auditor confidence:** high

### `lattice_3d_dense_spent_delay_note`

- **Note:** [`LATTICE_3D_DENSE_SPENT_DELAY_NOTE.md`](../../docs/LATTICE_3D_DENSE_SPENT_DELAY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite executable runner-card claim for scripts/lattice_3d_dense_10prop.py at the stated dense 3D spent-delay parameters, including only the z=2,3,4,5 distance window and excluding z=6, asymptotic, continuum, or effective-retained claims.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-133545-f10859e3a5-lattice_3d_dense_spent_delay`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** For the canonical dense 3D spent-delay card with L=12, W=6, h=1.0, s=5e-05, the live runner reports the listed 10-property finite card and z=2..5 hierarchy-aligned support.  _(class `C`)_
- **chain closes:** True — The runner source constructs the finite Z^3 lattice, slit mask, field, propagation rule, controls, and distance fit directly from card parameters and does not import helper data, cited-note values, or hard-coded expected outputs. Independent arithmetic on the displayed distance table gives slope -1.6165 and R²=0.97597, matching the stated b^(-1.62), R²=0.976 support.
- **rationale:** The note's repaired scope is exactly the finite live runner card, and the included cache output matches that scope with no stale z=6 endpoint. The source code performs actual finite computation rather than printing constants or comparing to external calibrated measurements. The displayed node count, interior edge count, distance signs, hierarchy support count, and distance-law fit check out from the packet values. No cited open authority or hidden helper dependency appears in the restricted packet.
- **auditor confidence:** medium

### `lattice_3d_dense_spent_delay_z2_z6_endpoint_note_2026-05-29`

- **Note:** [`LATTICE_3D_DENSE_SPENT_DELAY_Z2_Z6_ENDPOINT_NOTE_2026-05-29.md`](../../docs/LATTICE_3D_DENSE_SPENT_DELAY_Z2_Z6_ENDPOINT_NOTE_2026-05-29.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite 3D dense spent-delay harness endpoint check with L=12, W=6, h=1.0, max_d=3, and z_mass=2..6; only the printed finite centroid, P_near, and side-bias sign support is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260606-183847-c4f56e694b-lattice_3d_dense_spent_delay`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The finite z=2..6 endpoint scan in the existing dense spent-delay harness has hierarchy-aligned attractive support at every tested point, including z=6 positive on centroid shift, near-window probability gain, and side-bias.  _(class `C`)_
- **chain closes:** True — The primary runner calls the exposed dense helper to generate the lattice, slits, field, propagation, detector probabilities, and three sign metrics for z=2..6, then asserts the exact bounded endpoint condition claimed. The helper source contains actual finite propagation code rather than hard-coded endpoint values or imported comparator constants, and the displayed signs/regression are consistent with the printed table.
- **rationale:** The load-bearing step is a first-principles finite computation inside the supplied harness, with the transitive helper source exposed. The endpoint checker does not read a prior z=6 value or assert equality to a cached constant; it computes flat and mass detector distributions and classifies the signs from those distributions. The claim is properly bounded to the finite z=2..6 support surface and explicitly avoids asymptotic or physical-gravity overclaiming.
- **auditor confidence:** high

### `lattice_3d_dense_window_extension_note`

- **Note:** [`LATTICE_3D_DENSE_WINDOW_EXTENSION_NOTE.md`](../../docs/LATTICE_3D_DENSE_WINDOW_EXTENSION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On the ordered 3D dense spent-delay family, the live sweep shows z = 2 through 6 remain attractive, z = 7 is mixed/signal-free, detector-window widening preserves z = 6's sign, and wider slit thresholds do not extend the window further.  _(class `C`)_
- **chain closes:** True — The live script reproduces the source table and decision on the same declared family, action, geometry, slit threshold, detector-window scan, and z range; the source keeps the conclusion bounded and does not promote an all-distance or new-action theorem.
- **rationale:** The source claim is a bounded computational extension, and the live artifact reproduces the canonical z sweep, detector-window sensitivity rows, slit-threshold spot checks, Born companion value, MI/decoherence values, and final bounded-extension decision. The conclusion is limited to the ordered 3D dense spent-delay family with the declared geometry and explicitly excludes all-distance, 4D, NN, and action-law claims, so the runner checks the load-bearing step without hidden promotion. Residual risk is only ordinary finite-sweep scope: this clean audit does not say anything beyond the tested family and parameter grid.
- **auditor confidence:** high

### `lattice_3d_inverse_square_kernel_helper_note_2026-04-04`

- **Note:** [`LATTICE_3D_INVERSE_SQUARE_KERNEL_HELPER_NOTE_2026-04-04.md`](../../docs/LATTICE_3D_INVERSE_SQUARE_KERNEL_HELPER_NOTE_2026-04-04.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the wrapper/interface boundary for the 3D inverse-square kernel helper module and the provided runner source's corresponding constants, helper functions, and w/L^2 propagation expression.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-hygiene-cycle-break-20260707-193821-5b3b16-lattice_3d_inverse_square_kernel-18`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The note records only the helper-module interface: width-6 comparator constants and the build_family/barrier_metrics/no_barrier_distance/fit_power helper names, with no derivation of the inverse-square kernel or downstream tail law.  _(class `E`)_
- **chain closes:** True — Within the wrapper-only scope, the provided runner source declares the documented constants and helper functions and uses w/(L*L) while preserving the spent-delay action expression. The chain would not close for any stronger claim deriving the inverse-square kernel or tail law, but the note explicitly excludes those claims.
- **rationale:** The source note's operative move is definitional/interface documentation, not a first-principles physics derivation. The runner source supports that the named constants and helpers exist and that the implementation contains the advertised inverse-square attenuation, but this is an implementation/interface check rather than class (C) closure from framework axioms. Because the note itself narrows the boundary to wrapper support and forbids citation as a derivation or downstream theorem, the restricted claim closes only as a bounded definition-style wrapper.
- **auditor confidence:** high

### `lattice_3d_l2_numpy_h0125_audit_note`

- **Note:** [`LATTICE_3D_L2_NUMPY_H0125_AUDIT_NOTE.md`](../../docs/LATTICE_3D_L2_NUMPY_H0125_AUDIT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded numerical audit of the reduced dense 3D 1/L^2 + h^2 numpy family at h = 1.0, 0.5, 0.25, 0.125 with phys_l = 4, phys_w = 1.5, max_d_phys = 3, strength = 5e-5, and on-lattice active source z = 1.0.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T201254Z-b3e07f43-lattice_3d_l2_numpy_h012-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The reduced 3D dense 1/L^2 + h^2 numpy family runs through h = 0.125 and, with z_mass_active = 1.0 on-lattice, preserves Born from h = 0.5 down plus TOWARD weak-field gravity and F~M alpha approximately 0.5 at the finer spacings.  _(class `C`)_
- **chain closes:** True — The provided runner and helper source generate the lattice, field, slit setup, propagation, Born check, gravity response, F~M fit, decoherence, and MI directly from the fixed numerical family rather than printing cached target constants. The conclusion is explicitly bounded to that reduced family and excludes the empty distance-law sweep and full 3D closure.
- **rationale:** The load-bearing evidence is a completed cached run whose source instantiates the dense lattice and 1/L^2 propagation path, including the repaired on-lattice active source. The helper code does not import a contested premise or hard-code the reported observables; it computes them from the fixed parameters. The note's claimed scope is narrow enough to match the runner output, including the h = 1.0 coarse-grid limitation and the absence of a distance-law fit.
- **auditor confidence:** high

### `lattice_3d_l2_numpy_h0125_bridge_note`

- **Note:** [`LATTICE_3D_L2_NUMPY_H0125_BRIDGE_NOTE.md`](../../docs/LATTICE_3D_L2_NUMPY_H0125_BRIDGE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite fixed-family 3D dense 1/L^2+h^2 bridge evidence at phys_l=6, phys_w=3 through h=0.125, with Born/k=0 clean, TOWARD bridge sign in the completed cache, and F~M near 0.50 rather than Newtonian closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The current fixed-family artifact chain supports a completed h=0.125 row, machine-clean Born/k=0 behavior, TOWARD bridge sign, and F~M remaining about 0.50 rather than 1.00.  _(class `C`)_
- **chain closes:** True — The primary bridge cache completes the four-row fixed-family replay through h=0.125 and the focused single-row log independently supports the decisive h=0.125 row. The audited scope is only the bounded finite evidence and explicit non-Newtonian limitation, not a continuum-limit or Newtonian bridge theorem.
- **rationale:** The runner instantiates the dense 3D fixed-family lattice replay rather than printing the target conclusion, and the completed cache supports the source note's safe read: Born/k=0 remain clean, the retained-family sign is TOWARD at h=0.5, h=0.25, and h=0.125, and F~M stays about 0.50. The small difference between the focused single-row Born residue and the current bridge-cache residue is immaterial to the scoped claim because both are machine-clean and the exact residue is not used as a physical prediction. Residual risk is limited to the stated bounded finite family; no continuum or Newtonian closure is audited here.
- **auditor confidence:** high

### `lattice_3d_nyquist_diffraction_note`

- **Note:** [`LATTICE_3D_NYQUIST_DIFFRACTION_NOTE.md`](../../docs/LATTICE_3D_NYQUIST_DIFFRACTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite ordered-lattice valley-linear probe showing that, for h=0.5 and h=0.25 at strengths 1e-4 and 1e-2, the first positive-to-negative gravity-side centroid-shift flip occurs near pi/h and scales with the lattice spacing.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-lattice_3d_nyquist_diffraction_note-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The first gravity sign flip tracks the lattice Nyquist scale, stays field-independent to the tested order of magnitude, and moves with h rather than staying at a fixed continuum scale.  _(class `C`)_
- **chain closes:** True — The primary runner constructs the lattice, field, slit geometry, propagates amplitudes, scans k, computes centroid shifts, and interpolates the first sign flip without hard-coding the reported flip values. The cited retained_bounded authority supplies the finite valley-linear lattice family context, and no open external comparator or continuum bridge is needed for this bounded lattice-artifact claim.
- **rationale:** The runner source and helper source implement the load-bearing computation directly from the finite lattice propagator, action, kernel, field, and detector geometry, then compare the computed flips to pi/h. The stdout values match the source note: both spacings show the first positive-to-negative flip near the corresponding Nyquist scale, and the flip scale roughly doubles when h halves. The clean result is bounded to the stated finite scan and does not establish a continuum theorem or exact aliasing proof.
- **auditor confidence:** high

### `lattice_complementarity_note`

- **Note:** [`LATTICE_COMPLEMENTARITY_NOTE.md`](../../docs/LATTICE_COMPLEMENTARITY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded ordered-lattice tradeoff claim for N=40, half_width=20, gap=1..7, standard linear propagator, final-layer centroid shift, far-field b>=7 fit, companion Born audit, and the declared sweet-spot guard.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-lattice_complementarity_-029`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The canonical sweep shows a continuous tradeoff between decoherence/which-slit structure and distance-law quality, with only gap = 2 clearing the declared bounded-balance guard.  _(class `C`)_
- **chain closes:** True — The runner source constructs the ordered lattice, slit cards, propagations, observables, distance fits, Born companion audit, and guard directly rather than printing constants. Within the restricted packet, the note's bounded conclusion follows from that computation and explicitly excludes same-card attractive gravity or full unification.
- **rationale:** The load-bearing step is a first-principles computation over the stated ordered-lattice setup, producing the MI, d_TV, decoherence, distance-fit, gravity-sign, Born, and k=0 sweep values. The source code does not import cited authorities or hard-code expected table values; it computes the rows from lattice generation, propagation, field evaluation, and fitting helpers. The promoted claim is carefully bounded to a tradeoff curve with a sweet spot and does not claim same-card attractive gravity or one-family unification.
- **auditor confidence:** high

### `lattice_distance_law_note`

- **Note:** [`LATTICE_DISTANCE_LAW_NOTE.md`](../../docs/LATTICE_DISTANCE_LAW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite N=40, half_width=20, k=5.0, strength=0.1 no-barrier ordered-lattice centroid-shift computation over B_VALUES = [3,5,7,10,13,16,19], including the declared b >= 7 |delta| fit and k=0 control.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-205918-0eef0b89-lattice_distance_law_not-002`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the N=40 no-barrier ordered lattice, the far-field window b >= 7 fits |delta| ~= 23.5071 * b^(-1.052) with R^2 = 0.9850.  _(class `C`)_
- **chain closes:** True — The primary runner constructs the lattice, field, propagation, centroid readout, seven b rows, k=0 control, and b >= 7 power-law fit from code rather than printing hard-coded target values. The helper source is included and supplies the load-bearing lattice generation, field, and propagation routines, so the bounded N=40 numerical claim closes on its own stated harness.
- **rationale:** The runner stdout matches the note's table, k=0 control, coefficient, exponent, and R^2, and the provided source shows these are computed from the declared ordered-lattice harness. No cited upstream authority is required for this bounded finite computation, and no helper hard-codes the contested fit. The clean verdict is limited to the stated N=40 no-barrier numerical fit, not to a universal asymptotic distance law or signed attractive deflection theorem.
- **auditor confidence:** high

### `lattice_greens_function_maradudin_textbook_import_note_2026-05-18`

- **Note:** [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](../../docs/LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the nearest-neighbor graph Laplacian (-Delta_lat) on Z^3 with unit lattice spacing, the infinite-volume Green kernel has leading asymptotic normalization G(x) ~ 1/(4 pi |x|).
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260610-023044-a64d1566bc-lattice_greens_function_mara`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Because the graph-Laplacian symbol satisfies lambda(k)=|k|^2+O(|k|^4) at the only singular mode, the leading Green kernel is the inverse Fourier transform of 1/|k|^2, namely 1/(4 pi |x|).  _(class `C`)_
- **chain closes:** True — The stated stencil gives lambda(k)=sum_i k_i^2-(1/12)sum_i k_i^4+O(|k|^6), so the singular Fourier coefficient is exactly the continuum |k|^-2 one under the packet's transform convention. Independently, the axis residual of 1/(4 pi r) scales as 7/(8 pi) r^-5, matching the runner's coefficient and confirming the stated lower-order lattice-harmonic behavior away from the source.
- **rationale:** The load-bearing coefficient is not imported from the listed textbook authorities; it follows from the exact framework stencil's small-k symbol and the standard continuum Fourier normalization. The runner source genuinely evaluates the stencil symbol, continuum flux convention, and discrete residual, with no helper imports or external comparator data. The runner does hard-code the candidate continuum kernel for the flux/residual checks, but the independent Taylor/Fourier check closes the normalization from the stated operator rather than relying on that printout alone.
- **auditor confidence:** high

### `lattice_kernel_transfer_norm_note`

- **Note:** [`LATTICE_KERNEL_TRANSFER_NORM_NOTE.md`](../../docs/LATTICE_KERNEL_TRANSFER_NORM_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite local 3D ordered-lattice transfer-norm sweep for p in {1.5, 2.0, 2.5, 3.0} over h in {1.0, 0.5, 0.25, 0.125}, with h^2 normalization, showing p = 1.5 has the smallest measured-slope magnitude.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-dyson`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** Using the measured norm with h^2 normalization, p = 1.5 is closest to stable across h = 1.0, 0.5, 0.25, 0.125.  _(class `C`)_
- **chain closes:** True — The current runner, invoked with the note's four h values, reproduces the stated measured slopes: +0.102, -0.204, -0.598, and -1.046, ranking p = 1.5 closest to marginal. The note explicitly bounds the result away from branch promotion, same-harness propagation, and continuum-limit claims.
- **rationale:** The load-bearing claim is a bounded numerical computation inside a specified local harness, not a physical promotion claim. The runner computes the relevant outgoing transfer norms and log-log measured slopes directly, and the scoped note does not import dependencies or overstate the result beyond the finite discriminator.
- **auditor confidence:** high

### `lattice_nn_continuum_note`

- **Note:** [`LATTICE_NN_CONTINUUM_NOTE.md`](../../docs/LATTICE_NN_CONTINUUM_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-spacing computational claim for the raw nearest-neighbor harness on H_finite = {2.0, 1.0, 0.5, 0.25}: finite gravity, k=0, MI, classical purity, total-variation, and Born rows, with Born residual < 1e-10 and h = 0.125/continuum explicitly outside the claimed window.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-lattice-nn-continuum-audit-1-2026-05-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The supplied raw nearest-neighbor runner defines the finite lattice family and measurement harness, prints finite rows for h = 2.0, 1.0, 0.5, and 0.25 with Born residuals below 1e-10 and k=0 equal to 0, then prints FAIL for h = 0.125; the note scopes its conclusion exactly to that completed finite window and excludes the finer-spacing/continuum question.  _(class `C`)_
- **chain closes:** True — Within the restricted packet, the runner source actually constructs the raw 3-forward-edge nearest-neighbor lattice, applies one fixed measurement procedure across the requested spacings, computes the listed observables without a fitted external comparator, and the completed stdout matches the table and safe claim. The note does not promote the failed h = 0.125 row or any continuum inference into the claimed result, so the bounded finite-window implication closes.
- **rationale:** The scoped claim is narrow enough for the supplied completed runner output: all four finite-window rows are present and finite, k=0 is reported as +0.00e+00, the worst Born residual is 6.02e-16 below the 1e-10 tolerance, and h = 0.125 is treated only as an unresolved gate. There is no cited authority, external physical identification, tuned observed target, or continuum extrapolation required for the bounded statement.
- **auditor confidence:** high

### `lattice_nn_deterministic_rescale_note`

- **Note:** [`LATTICE_NN_DETERMINISTIC_RESCALE_NOTE.md`](../../docs/LATTICE_NN_DETERMINISTIC_RESCALE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite computational claim only: for the exact supplied runner, constants, lattice geometry, slit construction, propagation rule, and tested spacings down to h=0.0625, the deterministic geometry-only rescale schedule keeps the Born diagnostic machine-clean and yields the printed observable rows. It does not establish a continuum theory or physical interpretation beyond this finite tested surface.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-lattice-nn-deterministic-rescale-audit-2-2026-05-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The supplied runner explicitly evaluates the fixed h grid {1.0, 0.5, 0.25, 0.125, 0.0625} on the raw three-edge nearest-neighbor lattice using a deterministic per-edge scale factor spacing/sqrt(3), then computes the displayed Born |I3|/P, k=0, MI, 1-purity, d_TV, and gravity rows; the completed stdout shows machine-scale Born residuals at every tested spacing including the sub-0.25 rows.  _(class `C`)_
- **chain closes:** True — Within the bounded scope, the packet contains the note, the complete runner source, and completed runner stdout. The source implements the asserted fixed schedule and finite h list, and the stdout supplies the rows on which the conclusion rests. No external authority, hidden dependency, or long-running missing computation is needed for the finite claim.
- **rationale:** The bounded conclusion is supported on its own terms: the runner is deterministic for the stated constants, applies step_scale = spacing/sqrt(3) independent of amplitudes and blocked-set configuration, completes for all claimed spacings, and reports Born residuals of order 1e-16 through h=0.0625. The note also explicitly limits the conclusion and warns against continuum overstatement. The phrase about smooth convergence is acceptable only as a finite-row trend inside this scope, not as an asymptotic theorem.
- **auditor confidence:** high

### `lattice_nn_distance_law_note`

- **Note:** [`LATTICE_NN_DISTANCE_LAW_NOTE.md`](../../docs/LATTICE_NN_DISTANCE_LAW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded barrier-harness distance-law claim for raw nearest-neighbor h={1.0,0.5,0.25}, b={3,5,7,10,13,16,19}: signed centroid shifts and far-field |delta| power-law fits for fixed strength and alpha=1.5, inheriting Born-clean finite-window support from lattice_nn_continuum_note.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-lattice-nn-distance-law-audit-1-2026-05-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** On the raw NN barrier refinement path, refined h=0.5 and h=0.25 retain a positive far-field distance signal with fixed-strength decay slopes near -1, while alpha=1.5 preserves but flattens the decay.  _(class `C`)_
- **chain closes:** True — The current runner completed and reproduces the source note's distance rows, signs, slopes, and R^2 values. The cited one-hop dependency is now retained_bounded/audited_clean for the same raw NN finite window including h=1.0,0.5,0.25, so the prior upstream Born/k=0 bridge is closed within the restricted packet.
- **rationale:** The claim is bounded to the barrier harness and finite h,b grid actually executed by the runner. The live output supports the far-field sign statements, fixed-strength near-1/b decay through h=0.25, and alpha=1.5 flattening comparison, while the audited-clean continuum note supplies the raw NN finite-window Born/k=0 controls. No continuum, universal attraction, or no-barrier branch claim is needed for closure.
- **auditor confidence:** high

### `lattice_nn_light_cone_note`

- **Note:** [`LATTICE_NN_LIGHT_CONE_NOTE.md`](../../docs/LATTICE_NN_LIGHT_CONE_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For a finite dependency graph and a fixed R-local update rule, differences initially confined to S remain confined at tick t to the cumulative forward-reachability neighborhood C_t(S), with shared external randomness when applicable.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T165623Z-ba1d1130-00020-lattice_nn_light_cone_note`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** For any vertex outside C_{t+1}(S), every predecessor used by its local update lies outside C_t(S), so all update inputs agree between the two histories and the vertex values remain equal.  _(class `A`)_
- **chain closes:** True — The induction follows directly from R-locality and the recursive definition of C_t(S). No metric, continuum, Lorentzian, or physical-speed conclusion is needed.
- **rationale:** The universal claim is established by a valid induction over update ticks: a vertex outside C_{t+1}(S) has no predecessor in C_t(S), so locality forces equal outputs when the predecessor values agree. The runner independently computes dependency supports and reachability on four finite graph families and performs 678 genuine set-containment or equality checks, although these finite cases are supplementary rather than the proof of universality. The note expressly excludes physical-spacetime, Lorentz-invariance, metric-speed, and distance-law interpretations.
- **auditor confidence:** high

### `lattice_nn_rg_alpha_sweep_note`

- **Note:** [`LATTICE_NN_RG_ALPHA_SWEEP_NOTE.md`](../../docs/LATTICE_NN_RG_ALPHA_SWEEP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite computational scan only: exact supplied deterministic NN lattice/rescale runner, h values 1.0, 0.5, 0.25, alpha values 0.0, 0.5, 1.0, 1.5, with the comparison focused on gravity at h=0.5 versus h=0.25 and Born-safe behavior inherited only on the audited finite deterministic path. No optimized exponent, continuum renormalization, physical fixed point, or extension beyond the scanned grid is established.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-lattice-nn-rg-alpha-sweep-audit-1-2026-05-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The supplied runner computes the finite alpha-by-h grid for the deterministic nearest-neighbor lattice path, derives g(0.25)/g(0.5) and pair exponent for each alpha, and the live completed stdout matches the source-note gravity values, ratios, exponents, k=0 zeros, and machine-clean Born conclusion; alpha=1.5 is the least h-sensitive measured point on the scanned grid with ratio 0.858.  _(class `C`)_
- **chain closes:** True — The one-hop dependency is audited clean for the finite deterministic Born-safe path, and the supplied runner source summary plus live completed stdout compute the asserted bounded scan rows without external comparator data or target fitting. The cache Born-residual triplet discrepancy does not break closure because the live runner matches the note for the listed rows and the discrepant cache values preserve the only load-bearing Born assertion, namely machine-clean residuals; exact alternate cache residuals are not needed for the alpha-stability conclusion. The note explicitly caveats the result as a scan-edge fixed-point-style probe rather than a renormalization theorem.
- **rationale:** Under the bounded scope, the claim follows from the supplied completed runner and audited finite dependency: alpha=1.5 is the strongest checked alpha, gives the highest measured h=0.25/h=0.5 gravity ratio of 0.858, and the note avoids claiming a solved RG fixed point or continuum theory. The cache mismatch is non-load-bearing because it changes only sub-femtoscale Born residual numerics while preserving the machine-clean conclusion and not altering gravity values, ratios, exponents, or k=0 behavior.
- **auditor confidence:** high

### `left_handed_charge_matching_note`

- **Note:** [`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`](../../docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md)
- **claim_type:** `decoration`
- **claim_scope:** Scale-free eigenvalue ratio α : β = 1 : (-3) on the selected-axis (2,3) and (2,1) LH-doublet blocks, using only the 6+2 multiplicities and tracelessness; no absolute normalization, SM hypercharge identification, charge formula, or anomaly closure audited.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_graph_first_su3_integration_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T203338Z-005ca289-left_handed_charge_match-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Tracelessness on the LH-doublet multiplicities gives 6α + 2β = 0, hence β = -3α and α : β = 1 : (-3).  _(class `A`)_
- **chain closes:** True — The retained graph-first SU(3) integration authority supplies the selected-axis weak-fiber/base decomposition and the 6 and 2 block multiplicities. The stated ratio then follows by the displayed tracelessness equation, while the +1/3,-1 normalization and SM-Y labeling are explicitly outside the load-bearing claim.
- **rationale:** The audited load-bearing content is a class-A algebraic corollary of the graph-first selected-axis commutant decomposition: once the 6-state and 2-state blocks are supplied, tracelessness uniquely fixes the scale-free ratio. The runner substantively verifies the graph-first decomposition and related finite-dimensional algebra, with no external comparator checks. The note does not close a new physical identification beyond the upstream graph-first SU(3) parent and explicitly demotes the absolute hypercharge-like pattern to a convention-fixed, non-load-bearing corollary.
- **decoration parent:** `graph_first_su3_integration_note`
- **auditor confidence:** high

### `lensing_adjoint_kernel_reduced_model_note`

- **Note:** [`LENSING_ADJOINT_KERNEL_REDUCED_MODEL_NOTE.md`](../../docs/LENSING_ADJOINT_KERNEL_REDUCED_MODEL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The one-term-per-layer reduction fails badly while the exact edge replay matches the first-order observable at the stated H=0.35 setup.  _(class `C`)_
- **chain closes:** True — The source makes only a bounded negative claim about the first reduced surrogate. The live H=0.35 runner reproduces the archived exact-edge/full-harness spot-check and the layer_signed/layer_abs failures against the exact edge series, with no cited dependencies needed.
- **rationale:** The retained content is a bounded negative inside the stated harness, not a derivation of the reference lensing slope or a continuum physics claim. The live runner with --h 0.35 reproduces true_kubo=+5.972756 and exact_edge=+5.972756 at b=3 with |Delta|=4.228e-13, then shows the signed and absolute one-term-per-layer reductions miss the b=3..6 exact-edge series by about 98-100%. Because the note explicitly keeps the exact edge factorization as the reference object and rejects only the first reduced surrogate, the claim closes on its own terms.
- **auditor confidence:** high

### `lensing_deflection_note`

- **Note:** [`LENSING_DEFLECTION_NOTE.md`](../../docs/LENSING_DEFLECTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded arithmetic verification that the supplied H=0.25 Fam1 kubo_true values at b ∈ {3,4,5,6} have log-log slope −1.433549, R² 0.998404, and are not consistent with an exponent of −1 under the stated 0.1 margin.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T130312Z-96c5c841-00241-lensing_deflection_note`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** For the H=0.25 values at b ∈ {3,4,5,6}, the log-log fit gives kubo_true slope −1.433549 and R² 0.998404, with |slope−(−1)| > 0.1.  _(class `A`)_
- **chain closes:** True — The certificate verifies the four cached inputs against the parsed artifact and combined-runner table, then independently evaluates the stated regression and non-1/b inequality. This closes only the fixed four-point numerical claim, not a first-principles recomputation, continuum exponent, or physical lensing theorem.
- **rationale:** The load-bearing result is a genuine arithmetic closure over four explicitly bounded numerical inputs: the displayed regression values follow from the supplied b and kubo_true arrays. Although the runner uses hard-coded expected arrays for the fit, it first checks those arrays against the parsed fine-H artifact, so that implementation choice does not break the narrow implication. The evidence does not support broader claims of first-principles generation, continuum stability, family portability, large-b asymptotics, or Newton/Einstein lensing, all of which the note expressly excludes.
- **auditor confidence:** high

### `lensing_k_sweep_note`

- **Note:** [`LENSING_K_SWEEP_NOTE.md`](../../docs/LENSING_K_SWEEP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded to the SHA-pinned scripts/lensing_k_sweep.py finite internal Kubo/centroid-response sweep on Fam1, H=0.25, seeds 0-2, kH in {0.5,1.0,1.5,2.0,2.5,3.0,4.0,5.0}, and b in {3,4,5,6}; excludes wave-interference mechanism, period inference, eikonal authority, physical gravitational-lensing bridge, and framework-level generalization.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-lensing-k-sweep-auditor-20260507-f161-b`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The bounded table reports a total slope range of about 2.02, from +0.58 to -1.43, across the enumerated kH sweep, so the fitted internal slope is strongly k-dependent on this setup.  _(class `C`)_
- **chain closes:** True — The current cache is SHA-pinned to the runner, completed with exit_code=0, and its stdout reproduces the source slope table and kH=5.0 fit failures. The runner computes the finite DAG propagation/Kubo values and log-log fits over the enumerated grid rather than importing the reported slopes; closure is only for that bounded internal numerical sweep.
- **rationale:** The finite numerical artifact closes: the source table matches the completed cache, and the runner source constructs the Fam1 DAGs, sweeps kH/seeds/b, computes Kubo responses, and fits slopes without hard-coding the table values. I count the runner as a C-style bounded computation rather than the mechanical D label because the scoped claim is internal runner output, not an external comparator match. Clean status is granted only under the narrowed scope; the source's mechanism, periodicity, eikonal, and physical gravitational-response language remains outside the audited claim.
- **auditor confidence:** high

### `lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02`

- **Note:** [`LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `decoration`
- **claim_scope:** Exact structural eigenvalue ratio 1:(-3) on the Sym² and Anti² LH-doublet sub-decompositions under the graph-first selected-axis commutant decomposition, excluding normalization, SM hypercharge identification, charge formula, and anomaly claims.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_graph_first_su3_integration_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260522T160429Z-28597505-lh_doublet_traceless_abe-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Using the retained 6-state Sym² and 2-state Anti² multiplicities, tracelessness gives 6·α + 2·β = 0, hence β = -3α and the Sym²:Anti² eigenvalue ratio is 1:(-3).  _(class `A`)_
- **chain closes:** True — The algebraic ratio follows immediately from the cited retained-grade 6 and 2 multiplicities plus tracelessness. No SM identification, normalization, external comparator, or phenomenological readout is needed for the audited narrow scope.
- **rationale:** The load-bearing work is a class A algebraic identity over retained-grade inputs. The primary runner source confirms it checks note scope, hard-coded retained multiplicities, exact Fraction algebra, and retained-grade ledger status, with no external comparator or first-principles operator computation. Because the theorem reduces to a narrow algebraic corollary of the graph-first SU3 integration parent plus standard tracelessness arithmetic, it fits the decoration policy rather than a new independent theorem.
- **decoration parent:** `graph_first_su3_integration_note`
- **auditor confidence:** high

### `lhcm_matter_assignment_block_proof_walk_lattice_independence_bounded_note_2026-05-10`

- **Note:** [`LHCM_MATTER_ASSIGNMENT_BLOCK_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-10.md`](../../docs/LHCM_MATTER_ASSIGNMENT_BLOCK_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-10.md)
- **claim_type:** `decoration`
- **claim_scope:** Audited the bounded proof-walk that the Sym²/Anti² block identification and LH-doublet (2,3) ⊕ (2,1) decomposition rest only on graph_first_su3_integration_note plus standard algebra, not on staggered-Dirac realization machinery.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_graph_first_su3_integration_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T210201Z-fafd3323-lhcm_matter_assignment_b-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The six-step proof-walk obtains C² ⊗ (Sym² ⊕ Anti²) = (2,3) ⊕ (2,1) from the graph-first τ eigenspace split 3 ⊕ 1 plus standard SU(3) representation theory and tensor distributivity, with no lattice-action or staggered-Dirac input in the load-bearing rows.  _(class `A`)_
- **chain closes:** True — The algebraic chain closes from the retained graph-first SU(3) integration authority and standard SU(3)/tensor facts; the historical LHCM matter-assignment note is not used as a load-bearing premise. The result is nevertheless a corollary/proof-walk over that parent rather than an independent theorem.
- **rationale:** The runner performs exact τ eigenspace, tensor-dimension, and Gell-Mann algebra checks, and it verifies the proof-walk text excludes lattice-action and staggered-Dirac quantities as load-bearing inputs. The cited retained graph-first SU(3) integration note already supplies the 3 ⊕ 1 split and su(3) block structure, while the remaining steps are standard mathematics. Because the chain has zero external comparator checks and reduces to a single retained parent plus standard algebra, the decoration tie-breaker applies rather than audited_clean.
- **decoration parent:** `graph_first_su3_integration_note`
- **auditor confidence:** high

### `lhcm_matter_assignment_from_su3_representation_note_2026-05-02`

- **Note:** [`LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md`](../../docs/LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md)
- **claim_type:** `decoration`
- **claim_scope:** Algebraic corollary that the graph-first selected-axis SU(3) representation content splits the LH-doublet sector into an SU(3)-fundamental (2,3) block and SU(3)-singlet (2,1) block, with quark/lepton names applied only by the stated SM-definition convention.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_graph_first_su3_integration_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T204628Z-01253e41-lhcm_matter_assignment_f-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The retained graph-first SU(3) integration gives a residual C^4 = Sym^2 ⊕ Anti^2 = C^3 ⊕ C^1 split with structural SU(3) acting as the 3-dimensional fundamental on Sym^2 and trivially on the 1-dimensional Anti^2 block, so the LH doublet sector is (2,3) ⊕ (2,1).  _(class `A`)_
- **chain closes:** True — The representation split follows from the retained graph-first SU(3) integration authority plus standard finite-dimensional SU(3) representation facts. The quark/lepton labels are explicitly conventional and are not used as a derived physics step.
- **rationale:** All load-bearing checks are class-A algebra over the already retained graph-first SU(3) selected-axis package: the runner verifies the swap decomposition, standard SU(3) fundamental matrices on the 3-block, triviality on the 1-block, and the tensor dimensions. The runner does not import external comparators or tuned numerical inputs. Because the claim reduces to a direct algebraic corollary of the graph-first SU(3) integration parent plus standard representation terminology, it is a decoration rather than an independent positive theorem.
- **decoration parent:** `graph_first_su3_integration_note`
- **auditor confidence:** high

### `lhcm_matter_assignment_su3_block_representation_narrow_theorem_note_2026-05-17`

- **Note:** [`LHCM_MATTER_ASSIGNMENT_SU3_BLOCK_REPRESENTATION_NARROW_THEOREM_NOTE_2026-05-17.md`](../../docs/LHCM_MATTER_ASSIGNMENT_SU3_BLOCK_REPRESENTATION_NARROW_THEOREM_NOTE_2026-05-17.md)
- **claim_type:** `decoration`
- **claim_scope:** The algebraic SU(2)×SU(3) decomposition of the selected-axis LH-doublet sector into dimensions 6 and 2, conditional only on the retained graph-first commutant construction.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_graph_first_su3_integration_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T031137Z-0d389f16-00010-lhcm_matter_assignment_su3_b`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Given the retained 3⊕1 block split and embedded su(3) action on the 3-dimensional block, standard SU(3) representation theory yields the fundamental 3 (up to conjugation) on Sym², the trivial representation on Anti², and hence (2,3)⊕(2,1).  _(class `A`)_
- **chain closes:** True — The retained integration authority supplies the 3⊕1 decomposition and embedded su(3) action; standard representation theory and tensor-product distributivity then establish (B1)–(B3). The selector authority fixes the construction's canonical scope but adds no independent load-bearing representation-theoretic step.
- **rationale:** The result is a correct class-(A) algebraic unpacking of the single retained graph-first SU(3) integration theorem using standard mathematics, with no external-comparator checks. The exact-symbolic runner supports the block ranks, standard Gell-Mann representation, irrep dimensions, and tensor-product multiplicities, but it does not constitute an independent class-(C) derivation. Under the single-parent algebraic-decoration rule, this is decoration-grade rather than a new bounded theorem.
- **decoration parent:** `graph_first_su3_integration_note`
- **auditor confidence:** high

### `lieb_robinson_equal_time_tensor_locality_narrow_theorem_note_2026-05-10`

- **Note:** [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Raw equal-time commutation and tensor-factorization for finite-dimensional Hilbert-space tensor factors at distinct lattice sites, including the raw Pauli-ladder illustration but excluding Lieb-Robinson dynamics, continuum microcausality, graded/Jordan-Wigner structure, and physical per-site realization claims.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-audit-ready-20260529-second-lieb_robinson_equal_time`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Embedded operators supported on distinct tensor factors commute because each acts as the identity on the other's factor, so O_x O_y = O_y O_x.  _(class `A`)_
- **chain closes:** True — The conclusions follow directly from the stipulated tensor-product Hilbert space and disjoint-factor embeddings. No upstream physical bridge, numerical comparator, or dynamical authority is needed for L1-L3.
- **rationale:** The load-bearing step is a standard algebraic identity over tensor-product operators with disjoint support. The source note explicitly rescopes away the prior physical per-site realization clause, Lieb-Robinson time evolution, continuum microcausality, and fermionic graded tensor-product claims. The provided runner genuinely constructs symbolic and Pauli tensor-product operators and checks the claimed commutators and factorization, with no hard-coded numerical target or external comparator. The ledger visibility check is non-load-bearing and does not affect closure.
- **auditor confidence:** high

### `linear_response_derivation_note`

- **Note:** [`LINEAR_RESPONSE_DERIVATION_NOTE.md`](../../docs/LINEAR_RESPONSE_DERIVATION_NOTE.md)
- **claim_type:** `open_gate`
- **claim_scope:** Frozen 44-family detector-only linear-response heuristic record: r=0.5605 overall, r=0.7248 off-scaffold, 36/44 no-fit sign agreement, the explicitly fitted 35/44 threshold result, and the firewall excluding literal first-order Kubo or closed-derivation reuse.
- **audit_status:** ~~audited_clean~~
- **effective_status:** open_gate  (reason: `audited_open_gate`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00425-linear_response_derivation_n`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** The frozen-log verifier parses the 44 family rows and recomputes the overall and groupwise Pearson correlations, 36/44 sign agreement, fitted threshold result, and measured-response ceiling.  _(class `A`)_
- **chain closes:** True — For this archival open-gate scope, the SHA-pinned runner genuinely parses the frozen rows and independently recomputes the reported statistics. It does not establish a literal Kubo derivation, which the audited scope expressly excludes.
- **rationale:** The runner performs statistical and consistency checks over the frozen dataset rather than merely printing expected constants, and all 15 checks pass. The source preserves the essential no-fit versus in-sample-tuned distinction and explicitly forbids treating the detector reweighting as the literal first-order Kubo expression. The clean verdict therefore applies only to the narrowed open-gate heuristic record, not to broader first-principles or compact-principle language elsewhere in the note.
- **auditor confidence:** high

### `linear_response_true_kubo_note`

- **Note:** [`LINEAR_RESPONSE_TRUE_KUBO_NOTE.md`](../../docs/LINEAR_RESPONSE_TRUE_KUBO_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the specified finite path-sum propagator exp(i k L(1 - s/r_edge)) times the stated weights, the parallel perturbation recurrence computes the exact first derivative d(cz)/ds at s = 0 for the stated detector centroid observable.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-second-linear_response_true_kubo_note-20260505`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** B_j = Σ_{i→j} [B_i exp(i k L_ij) + A_i (-i k L_ij / r_edge_ij) exp(i k L_ij)] w_ij h²/L_ij², followed by d(cz)/ds = (1/T) Σ_j (z_j - cz_free) 2 Re[A_j* B_j].  _(class `A`)_
- **chain closes:** True — The B recurrence follows by direct Leibniz/chain-rule differentiation of each edge factor in the finite path product, and the centroid formula follows by differentiating the quotient N/T. Closure is bounded to the specified propagator, regularized 1/r_edge field, finite DAG-style propagation, detector readout, and s = 0 linear-response regime.
- **rationale:** The bounded analytic claim closes: the note's load-bearing recurrence is not a fitted definition or renaming, but the exact first derivative of the stated path-sum propagator, and the d(cz)/ds expression is the standard quotient derivative written in centered form. The cached runner completed successfully and independently recomputes the stated 44-family correlation/sign evidence, but that evidence is supportive rather than needed for the algebraic closure. This clean verdict does not promote broader claims about nonlinear response, F~M scaling, PASS/FAIL thresholds, physical gravity strength, or a compact-principle theorem beyond the specified first-order propagator/field/readout.
- **auditor confidence:** high

### `literature_backmatch_live_scan_note`

- **Note:** [`LITERATURE_BACKMATCH_LIVE_SCAN_NOTE.md`](../../docs/LITERATURE_BACKMATCH_LIVE_SCAN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** A published widefield diamond NV lock-in microscopy result with per-pixel I/Q readout and dynamic imaging is a credible retrospective analog/backmatch candidate, but not validation of the retained prediction.  _(class `D`)_
- **chain closes:** True — The cited paper's abstract-level record supports the note's narrow factual predicates: widefield NV magnetometry, lock-in PL detection over multiple pixels, in-phase/quadrature image formation, and sub-second dynamic magnetic imaging. The note explicitly limits the conclusion to analog-platform resemblance and denies validation of the framework's target observables.
- **rationale:** The external source check closes the bounded backmatch claim: the paper is in the same diamond NV lock-in/quadrature/dynamic-imaging measurement family described by the note. The note does not overclaim this as evidence for the retained gravitational or causal-field observables, and it correctly preserves the distinction between resemblance and validation. Residual risk is only that this is a single retrospective analog candidate, not a prediction test.
- **auditor confidence:** high

### `lorentz_violation_derived_note`

- **Note:** [`LORENTZ_VIOLATION_DERIVED_NOTE.md`](../../docs/LORENTZ_VIOLATION_DERIVED_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Conditional Taylor expansion, normalized cubic-harmonic decomposition, and directional anisotropy of the supplied nearest-neighbor cubic kinetic symbol.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-20260713-004850-7f5ed483-7f5ed4832cd94204946dc71b5b3be732-lorentz_violation_derive-001`  (codex-gpt-5.6; independence=weak)
- **load-bearing step:** Expanding the supplied symbol K_i = (4/a^2) sin^2(p_i a/2) gives K_i = p_i^2 - (a^2/12)p_i^4 + O(a^4p_i^6), and summing over spatial directions yields the stated cubic-anisotropic dispersion correction.  _(class `A`)_
- **chain closes:** False — The algebra closes once the fixed kinetic symbol, spacing, and relativistic-dispersion interpretation are supplied. No cited authority derives or retains those model inputs from the accepted framework premises.
- **rationale:** Issue: the Taylor and normalized cubic-harmonic identities are mathematically consistent, but the kinetic action and carrier interpretation are supplied rather than derived; the note also says the runner constructs all 48 O_h elements although the included code contains no such group construction. Why this blocks: the computation verifies a selected model surface, not a consequence of the accepted framework premises, and part of the advertised runner coverage is absent. Repair target: add a retained theorem selecting the kinetic operator and carrier and add executable O_h order/invariance assertions. Claim boundary until fixed: the p_i^4 coefficient, normalized l=4 identity, and factor-of-three anisotropy remain valid conditional algebra for the explicitly supplied symbol.
- **auditor confidence:** high

### `lsp_projective_canonical_kp_equals_p_narrow_theorem_note_2026-06-05`

- **Note:** [`LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md`](../../docs/LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-dimensional projective measurements with nonzero displayed outcome projectors and fixed canonical apparatus preparation/readout: K_r=P_r; outcome phases and permutations preserve the instrument up to phase or relabeling; label-mixing apparatus rows change the corresponding POVM element.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00350-lsp_projective_canonical_kp_`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** From K_r=Σ_s⟨r|V_A|s⟩P_s and P_sP_{s'}=δ_{ss'}P_s, one obtains K_r†K_r=Σ_s|⟨r|V_A|s⟩|²P_s, with the canonical case giving K_r=P_r.  _(class `A`)_
- **chain closes:** True — The conclusions follow directly from projection orthogonality, completeness, and the stated apparatus contraction. The accepted finite-carrier premise supplies the setting, while no measurement-probability rule, fitted value, or open physical-selection bridge is used.
- **rationale:** The load-bearing identities are genuine finite-dimensional algebraic consequences of the stated hypotheses. The runner constructs the projectors, isometry, Kraus contractions, phase/permutation twists, mixing examples, and zero-projector cases rather than printing or importing the conclusions; all 53 checks pass. The necessity statement is correctly limited to nonzero displayed sectors, and the note does not claim instrument uniqueness or derive physical measurement semantics.
- **auditor confidence:** high

### `luders_sequential_effect_composition_pep_bridge_narrow_theorem_note_2026-06-05`

- **Note:** [`LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](../../docs/LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-dimensional matrix theorem: for the stated projections, effects, and density operator, PEP is a supported effect and satisfies the trace, boundary, and nested-compression identities, without any Lüders-update, Born-rule, or probability interpretation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00351-luders_sequential_effect_com`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** Congruence preserves positivity and finite-dimensional trace cyclicity gives 0 <= PEP <= P <= I, Tr(rho PEP) = Tr(P rho P E), and P(QFQ)P = (QP)^*F(QP).  _(class `A`)_
- **chain closes:** True — Each conclusion follows directly from the stated finite-matrix hypotheses by positivity under congruence, projection order, adjoints, and trace cyclicity. No measurement-side bridge is used.
- **rationale:** The source is correctly narrowed to finite matrix algebra and explicitly excludes measurement and probability semantics. The runner substantively performs exact symbolic and randomized checks, including a Jordan-symmetrization guard, rather than printing constants or importing a contested premise. The cited minimal-axiom authority is an accepted premise used only for matrix-carrier context, while the theorem itself closes from its explicit hypotheses.
- **auditor confidence:** high

### `main_open_cubic_validation_2026-04-11`

- **Note:** [`MAIN_OPEN_CUBIC_VALIDATION_2026-04-11.md`](../../docs/MAIN_OPEN_CUBIC_VALIDATION_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The newly promoted open-cubic staggered subset is scientifically consistent on main, supporting only the bounded external-source d^-2 reproduction, blocking-sensitivity, and 3D sign-split surfaces stated in the note.  _(class `C`)_
- **chain closes:** True — The current outputs of the three listed scripts reproduce the note's exact-force, blocked-trajectory, blocking-sensitivity, and 3D contraction/sign-split summaries within print precision. The note explicitly excludes broader staggered both-masses or self-consistent two-body closure.
- **rationale:** The validation claim closes for its bounded scope: all three referenced reruns match the frozen note summaries, including the global exponents, per-side blocked fits, blocking-scheme sensitivity, width ratios, core excess values, and 20/20 vs 0/20 field-side sign split. The note does not overstate these checks into broader Newton closure or two-body closure. Residual risk is limited to the promoted upstream notes' own scopes, not to stale validation output here.
- **auditor confidence:** high

### `matched_2d_4d_decoherence_note`

- **Note:** [`MATCHED_2D_4D_DECOHERENCE_NOTE.md`](../../docs/MATCHED_2D_4D_DECOHERENCE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Pinned matched 2D-vs-4D decoherence replay for the named generator routines and default arguments, showing the reported pur_min/<k>/r4 table and alpha delta do not support 4D exponent flattening in this bounded pocket.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The matched comparison does not support a clean '4D flattens the ceiling' claim under the pinned 2D/4D generator definitions, degree matching, seeds, k-band, and pur_min metric.  _(class `C`)_
- **chain closes:** True — The runner constructs both graph families from the named generator routines, computes the matched pur_min and degree table, fits per-seed exponents, and asserts the source note's table within explicit tolerances. The note's claim is bounded to those generator definitions and default arguments, so no outside modular-universality authority is needed.
- **rationale:** The source note and runner agree on the bounded table, alpha estimates, and conclusion that this matched pocket does not support a dimensional exponent-flattening theorem. The runner computes the graph samples and metrics before checking the pinned values, rather than importing a retained theorem or relying on author prose. Residual risk is limited to the named generator routines, seed count, radius grid, and default harness settings; broader 2D/4D modular universality is explicitly outside the audited scope.
- **auditor confidence:** high

### `memory_decay_diagnosis_2026-04-11`

- **Note:** [`MEMORY_DECAY_DIAGNOSIS_2026-04-11.md`](../../docs/MEMORY_DECAY_DIAGNOSIS_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** At the current parameters of scripts/frontier_memory_mu2_size_sweep.py, the toy runner's measured memory varies by more than 10x across N in both relative and fixed geometry slices, with fixed-vs-relative disagreement for N=81, 101, and 121.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T174300Z-02605cb9-memory_decay_diagnosis_2-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Both slices vary by more than an order of magnitude as N changes, and the two slices disagree sharply for the same N; the measured memory is not geometry-invariant or N-invariant at this runner's parameters.  _(class `C`)_
- **chain closes:** True — The runner source genuinely computes the field/matter evolution and derives the memory values from simulated separations rather than hard-coding the table. The cached stdout matches the note's load-bearing values and supports the narrowed geometry- and N-sensitivity claim within the stated runner boundary.
- **rationale:** The narrowed claim is only about this toy runner at specified parameters, not the historical Yukawa-screening interpretation. The provided source builds the ring operators, evolves the system, and computes memory values without importing prior note data or expected outputs. The output supports more-than-order-of-magnitude variation in both slices and strong fixed-vs-relative disagreement for N=81, 101, and 121; N=61 coincides because the fixed geometry matches the relative geometry there.
- **auditor confidence:** high

### `memory_mu2_geometry_sweep_note_2026-04-11`

- **Note:** [`MEMORY_MU2_GEOMETRY_SWEEP_NOTE_2026-04-11.md`](../../docs/MEMORY_MU2_GEOMETRY_SWEEP_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The memory failure is not primarily a Yukawa-range artifact: mu^2 matters, but geometry scaling matters more, and the old screening-alone diagnosis is too strong.  _(class `C`)_
- **chain closes:** True — The registered runner exits 0 and reproduces the scaled-geometry decay and fixed-geometry survival/strengthening tables exactly, including the mu^2=0 and mu^2=0.22 anchor values quoted in the note.
- **rationale:** The bounded diagnosis closes against scripts/frontier_memory_mu2_size_sweep.py. The current output matches the note's scaled-geometry rows, including N=61 mu2=0 memory +0.020854 vs mu2=0.22 +0.016780 and N=121 mu2=0 +0.001767 vs mu2=0.22 +0.000865, and it matches the fixed-geometry rows, including N=81 mu2=0 +0.231199 vs mu2=0.22 +0.244260 and N=121 mu2=0 +2.580905 vs mu2=0.22 +2.599619. The note does not promote a publication-grade memory claim; it only narrows the failure mode.
- **auditor confidence:** high

### `mesoscopic_surrogate_localization_sweep_note`

- **Note:** [`MESOSCOPIC_SURROGATE_LOCALIZATION_SWEEP_NOTE.md`](../../docs/MESOSCOPIC_SURROGATE_LOCALIZATION_SWEEP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-sweep benchmark only: this runner, this cached table, this explicit mesoscopic benchmark predicate, and the stated fixed 3D ordered-lattice mesoscopic-source setup. This does not certify retained source-control authority, framework-wide optimality, or a least-bad source theorem.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-gpt-5.5-fresh-2026-05-27-jason-2nd`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The runner's asserted benchmark predicate separates passing broad top-N rows from failing square/Gaussian rows using support, capture, score, and width-ratio thresholds.  _(class `B`)_
- **chain closes:** True — The claim closes at the finite-table level: the cache facts, benchmark predicate, passing top-N rows, failing square/Gaussian rows, and assertion-gated runner output all align with the narrowed source claim. The row does not rely on treating the benchmark or ordered-lattice setup as retained framework machinery.
- **rationale:** The bounded claim is audit-clean because the branch-local benchmark is explicitly scoped as a finite runner/table predicate rather than a retained framework principle. The negative statement is limited to the finite sweep: no square/Gaussian row passes this explicit benchmark here, while broad top-N rows do. Residual boundary: downstream citations must not generalize this into source-control authority, physical validity of the ordered-lattice setup, or a theorem over all possible localized families.
- **auditor confidence:** high

### `mirror_2d_gravity_law_note`

- **Note:** [`MIRROR_2D_GRAVITY_LAW_NOTE.md`](../../docs/MIRROR_2D_GRAVITY_LAW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded null-result that the supplied exact 2D mirror primary runner and in-packet helper source compute weak gravity-side mass-window and distance-tail fits on the stated searched windows.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T193958Z-fecbeaaf-mirror_2d_gravity_law_no-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The primary-runner cache reports weak gravity-side fits on the exact 2D mirror family: gravity scaling R^2=0.015, fixed-anchor mass-window R^2=0.167, and distance-tail R^2=0.075, so no clean promoted mass or distance law is supported on the searched windows.  _(class `C`)_
- **chain closes:** True — The primary runner genuinely constructs the mirror/random graph families, calls the supplied linear propagator/helper generator, computes detector statistics and power-law fits, and its cached stdout matches the weak-fit rows quoted in the note. The conclusion is bounded to those runner windows and does not depend on the diagnostic cleanup sweep.
- **rationale:** The load-bearing evidence is a first-principles numerical computation within the supplied runner chain, not a copied value, renaming, external comparator, or hard-coded printout. The helper source needed to verify `gen_2d_mirror` and `propagate_LINEAR` is included, and the primary runner uses those functions directly in the load-bearing path. The cached output supports the bounded negative claim because all relevant gravity-side fits are far below a clean-law threshold and the note explicitly scopes the conclusion to the searched primary-runner windows.
- **auditor confidence:** high

### `mirror_2d_validation_note`

- **Note:** [`MIRROR_2D_VALIDATION_NOTE.md`](../../docs/MIRROR_2D_VALIDATION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded exact 2D mirror coexistence pocket for N in {25,40,60,80,100}, npl_half=12, yr=10.0, connect_radius=2.5, 8 seeds, and k-band [3,5,7], with no promoted mass-law or distance-law claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260526T020122Z-7b7b8c26-mirror_2d_validation_not-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The exact 2D mirror family, using the registered linear propagator and stated parameter sweep, yields the retained Born, MI, decoherence, d_TV, and positive gravity rows, strongest at N = 60.  _(class `C`)_
- **chain closes:** True — The primary runner source computes the mirror and random-family rows from the supplied generator, linear propagator, slit selection, field model, and summary statistics rather than printing hard-coded constants. The helper source containing gen_2d_mirror and propagate_LINEAR is included, so the imported load-bearing functions are inspectable in the restricted packet.
- **rationale:** The retained table values in the note match the cached stdout from scripts/mirror_2d_validation.py, and the runner source genuinely computes those quantities over the stated finite sweep. The transitive helper scripts/mirror_born_audit.py is present and supplies an inspectable strictly linear propagator and exact 2D mirror generator, with no normalization or hard-coded contested result in the load-bearing path. The note also correctly limits the gravity follow-up to weak fits and does not promote a mass or distance law.
- **auditor confidence:** high

### `mirror_grown_combined_note`

- **Note:** [`MIRROR_GROWN_COMBINED_NOTE.md`](../../docs/MIRROR_GROWN_COMBINED_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the frozen cached stdout table for scripts/mirror_grown_combined.py at runner_sha256 b296de555272c4ccbc8fce2356c08497a478848415300c82c38d53089e6e8e0c, not any cross-lane comparison claim or live deterministic rerun claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260518-120032-569b3ebd-mirror_grown_combined_no-039`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The grown mirror scout produces the finite table in the registered runner cache, with small 1 - pur_min and weak gravity across d_growth in {2,3} and n_layers in {18,25,30,40}.  _(class `C`)_
- **chain closes:** True — The note's narrowed conclusion follows from the included cached stdout and runner source: the table values match the cache, and the source computes them by growing seeded mirror DAGs and propagating amplitudes rather than printing constants. The broader mirror/Z2xZ2 comparison is explicitly out of scope.
- **rationale:** The current note has narrowed the load-bearing claim to a frozen cache-only historical negative-control readout, and the supplied cache directly contains every row in the table. The runner source performs a stochastic seeded computation over grown mirror DAGs and does not hard-code the reported table or import comparator premises. Because the note explicitly excludes live deterministic reproducibility and cross-lane comparison from load-bearing scope, the finite cached-table claim closes on the restricted packet.
- **auditor confidence:** high

### `mirror_mutual_information_canonical_families_note`

- **Note:** [`MIRROR_MUTUAL_INFORMATION_CANONICAL_FAMILIES_NOTE.md`](../../docs/MIRROR_MUTUAL_INFORMATION_CANONICAL_FAMILIES_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** S4 mirror is the strongest scalable MI lane in this extension, while the exact chokepoint MI chain remains the synthesis-grade retained result.  _(class `C`)_
- **chain closes:** True — The registered runner exits 0 and reproduces the note's S4 mirror, S4 random, strict-mirror, and original-mirror MI tables, including the corrected N=80 S4 mirror value and the caveat that this extension is broader rather than more canonical.
- **rationale:** The bounded MI extension closes against scripts/mirror_mutual_information_canonical_families.py. Current output matches the note's S4 mirror values N=25 0.7213±0.073, N=40 0.5956±0.067, N=60 0.5248±0.067, N=80 0.2559±0.047; matched S4 random is lower at each retained row; strict mirror reproduces N=15 0.9196±0.033 and N=25 0.6578±0.091 before failing at larger N. The note keeps the exact chokepoint chain as the synthesis-grade result and treats this as a bounded extension.
- **auditor confidence:** high

### `moving_source_cross_family_note`

- **Note:** [`MOVING_SOURCE_CROSS_FAMILY_NOTE.md`](../../docs/MOVING_SOURCE_CROSS_FAMILY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded moving-source centroid-y directional observable was audited on two specified portable grown families under zero-source and v=0 static controls, using the provided runner output and source.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-040942-beec6e04-moving_source_cross_fami-282`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The moving-source centroid bias keeps the same signed response pattern on the second family, so the effect is not just a one-family artifact.  _(class `C`)_
- **chain closes:** True — The runner genuinely computes the two-family rows from generated geometries, fields, propagation, centroid readout, and seed summaries rather than printing hard-coded expected values. The cited first-family authority is retained_bounded, and the second-family result is computed directly in the supplied runner packet.
- **rationale:** The load-bearing step is a first-principles computational replay over two parameterized grown families with exact zero-source and matched static controls. The source code computes the field schedule, propagation, centroid differences, phase lag, and seed statistics; the contested signed response is not imported from the cited authority or hard-coded as a numerical target. The conclusion remains narrow: it establishes persistence across the two tested families, not a universal wave or continuum theorem.
- **auditor confidence:** high

### `moving_source_retarded_portability_note`

- **Note:** [`MOVING_SOURCE_RETARDED_PORTABILITY_NOTE.md`](../../docs/MOVING_SOURCE_RETARDED_PORTABILITY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded numerical probe on one portable grown row, drift=0.2 and restore=0.7, with six seeds, exact zero-source baseline, matched v=0 static control, and signed moving-source centroid-y shifts.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260504-232946-c1a20bdf-moving_source_retarded_p-007`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The moving-source rows do not collapse into static replay, because the centroid y bias flips sign with v after the exact zero baseline and matched static control.  _(class `C`)_
- **chain closes:** True — Within the restricted packet, the runner computes the zero baseline, static control, moving fields, final-layer centroid shifts, and phase residuals from the generated grown geometry rather than printing hard-coded expected values. The audited conclusion is only the bounded signed observable on this specific row and parameter schedule.
- **rationale:** The load-bearing claim is supported by a completed runner whose source constructs the field for each signed velocity, propagates amplitudes, and measures centroid differences against a matched static v=0 control. The numerical values in the note match the provided runner output, including the exact zero baseline and sign flip of delta_y vs static with v. No external comparator, renaming, or upstream support-only authority is used, and the note keeps the scope bounded to a moving-source proxy on one portable grown row.
- **auditor confidence:** medium

### `multipole_tidal_response_note`

- **Note:** [`MULTIPOLE_TIDAL_RESPONSE_NOTE.md`](../../docs/MULTIPOLE_TIDAL_RESPONSE_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The centered quadrupole keeps the centroid essentially pinned but opens a real width/tidal channel, and the width response grows with quadrupole separation.  _(class `C`)_
- **chain closes:** True — The live probe reproduces the frozen controls and finite quadrupole rows: same-site and neutral controls are zero, the dipole mainly shifts centroid, and the centered quadrupoles give near-zero centroid change with positive width response at a = 1.0 and a = 2.0. The source explicitly excludes full tensor gravity and a general multipole theory.
- **rationale:** The retained content is a narrow finite-runner claim, not a physical tidal-field theorem: the current runner recomputes the same-site cancellation, q_test = 0 inert control, dipole baseline, and two centered quadrupole width responses. The quadrupole rows support the stated shape-sensitive width channel while the note explicitly disclaims full tensor gravity, relativistic tidal fields, and a general multipole expansion. Residual risk is only finite-configuration scope, plus a harmless rounded-ratio mismatch where the prose says 1.969 and the live runner prints +1.968; the audit does not retain anything beyond the tested ordered-lattice configuration.
- **auditor confidence:** high

### `naive_lattice_fermion_two_power_d_species_count_narrow_theorem_note_2026-05-10`

- **Note:** [`NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact zero-locus and 2^d species count for the defined standard naive lattice Dirac operator on a hypercubic lattice, with d=4 count 16.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260522T161305Z-60a3a215-naive_lattice_fermion_tw-01`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Using the gamma anticommutator, (-i a D_naive(k))^2 = (sum_mu sin^2(k_mu a)) I, so D_naive(k)=0 iff every sin(k_mu a)=0.  _(class `A`)_
- **chain closes:** True — The conclusion follows by algebra from the explicitly defined operator and Clifford anticommutation relation, plus the elementary zeros of sine on the stated Brillouin-zone domain. No project-specific bridge or regulator-independent claim is used.
- **rationale:** The load-bearing step is a genuine algebraic identity check on the operator defined in the note, not a renaming, tuned numerical match, or external comparator. The runner source performs symbolic corner checks, finite d count checks, the d=4 arithmetic, and boundary-context checks; it does not merely print constants for the contested zero-locus result. The Wilson, staggered, and regulator-count rows are contextual safeguards rather than load-bearing inputs.
- **auditor confidence:** high

### `native_gauge_closure_note`

- **Note:** [`NATIVE_GAUGE_CLOSURE_NOTE.md`](../../docs/NATIVE_GAUGE_CLOSURE_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact native cubic Cl(3) taste algebra, native Clifford-bivector su(2), finite open-block cubic parity/chiral anticommutation, plus retained graph-first selected-axis structural su(3), with abelian/electroweak/matter/Wilson/phenomenology claims excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T141319Z-8376c0c3-native_gauge_closure_not-02`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Combining the directly checked native Cl(3), Clifford-bivector su(2), and cubic parity anticommutation with the two retained graph-first selector/SU(3) inputs gives the claimed nonabelian gauge-structure surface, excluding the abelian and phenomenological surfaces.  _(class `A`)_
- **chain closes:** True — The native pieces are finite matrix and finite graph algebra checked directly by the runner, and the graph-first selector and SU(3) integration are provided as retained positive-theorem authorities. The note does not rely on the abelian eigenvalue surface that remains bounded elsewhere.
- **rationale:** The runner source genuinely constructs the displayed Clifford generators, bivectors, finite-block hopping operator, and parity matrix, then checks the stated identities rather than printing constants. The remaining nonabelian SU(3) component is imported only through two cited authorities that are explicitly marked retained positive-theorem inputs in the packet. No external comparator, tuned numerical value, or symbol-renaming step is load-bearing, and the abelian surface is expressly outside scope.
- **auditor confidence:** high

### `native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23`

- **Note:** [`NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`](../../docs/NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md)
- **claim_type:** `decoration`
- **claim_scope:** For each selected axis of the graph-first C^8 taste cube, the complementary-axis swap defines projectors with ranks 6 and 2 and a traceless hypercharge-like left-handed abelian eigenvalue surface with spectrum +1/3^6 and -1^2.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_graph_first_su3_integration_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T154602Z-3c9084c9-native_gauge_left_handed-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The residual swap tau is an involution, so Pi_+ and Pi_- are complementary projectors with doubled symmetric/antisymmetric ranks 6 and 2, making Y_like traceless with eigenvalues +1/3 and -1 on those blocks.  _(class `A`)_
- **chain closes:** True — The cited graph-first SU3 integration note already supplies the selected-axis residual swap, the 3 plus 1 base split, and the doubled 6 plus 2 abelian eigenvalue surface. The present note only isolates that finite-dimensional algebraic consequence with the stated phenomenological exclusions.
- **rationale:** The runner genuinely constructs the residual swap on the eight cube vertices for all three selected axes, forms the projectors, and checks ranks, trace, Hermiticity, and eigenvalue multiplicities. The dependency checks are ledger/status checks rather than physics derivations, while the load-bearing eigenvalue calculation is algebraic over the retained graph-first SU3 integration parent. Because the same abelian eigenvalue surface is already explicitly contained in that parent and this note deliberately narrows scope rather than adding a new theorem, the appropriate conservative verdict is decoration, not a new bounded theorem.
- **decoration parent:** `graph_first_su3_integration_note`
- **auditor confidence:** high

### `newton_law_derived_note`

- **Note:** [`NEWTON_LAW_DERIVED_NOTE.md`](../../docs/NEWTON_LAW_DERIVED_NOTE.md)
- **claim_type:** `decoration`
- **claim_scope:** Algebraic differentiation of the continuum-leading radial kernel supplied by the retained-bounded Z^3 lattice Green-kernel parent, with no physical force-law conclusion.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_lattice_greens_function_maradudin_textbook_import_note_2026-05-18`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T130312Z-96c5c841-00221-newton_law_derived_note`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Differentiating phi(r) = M/(4 pi r) gives d phi/dr = -M/(4 pi r^2), hence |grad phi| = M/(4 pi r^2).  _(class `A`)_
- **chain closes:** False — The calculus is correct over the retained-bounded parent input, but the row adds only standard differentiation and source scaling to that single upstream claim. Under the decoration policy it is not an independent theorem closure.
- **rationale:** The runner genuinely verifies the symbolic derivative, scope restrictions, and live retained-grade dependency edge. The result contains no first-principles computation or external comparison and reduces to one retained-bounded Green-kernel parent plus elementary calculus. It therefore qualifies as an algebraic decoration rather than a separate bounded theorem or Newton force-law derivation.
- **decoration parent:** `lattice_greens_function_maradudin_textbook_import_note_2026-05-18`
- **auditor confidence:** high

### `newtonian_distance_law_confirmed`

- **Note:** [`NEWTONIAN_DISTANCE_LAW_CONFIRMED.md`](../../docs/NEWTONIAN_DISTANCE_LAW_CONFIRMED.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the finite W=12, h=0.25 3D valley-linear replay claim that the supplied no-barrier raw rows fit a z >= 5 far-tail exponent near b^(-1.17), not a universal Newtonian distance law.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260608-205223-acca9518e7-newtonian_distance_law_confi`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The supplied raw distance rows have peak row z=4 and, on the z >= 5 far-tail window, a log-log fit with slope -1.1685 and R^2 = 0.9972, recorded as b^(-1.17).  _(class `A`)_
- **chain closes:** True — The restricted packet provides the raw rows, retained_bounded upstream note, runner source, and successful frozen-log verifier output. An independent log-log least-squares check of the listed rows confirms peak z=4, far-tail slope -1.1685, R^2=0.9972, n=6.
- **rationale:** The default runner is a frozen-log/raw-row verifier rather than a first-principles recompute, so the load-bearing closure is class A over supplied retained-grade bounded inputs. The note's safe wording is explicitly finite-window and rejects the universal-law overclaim. Within that bounded scope, the raw-row inventory, SHA-pinned verifier, and independent fit check agree.
- **auditor confidence:** high

### `nonlabel_grown_basin_note`

- **Note:** [`NONLABEL_GROWN_BASIN_NOTE.md`](../../docs/NONLABEL_GROWN_BASIN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite deterministic audit of the grown geometry-sector signed-source transfer for seed 0, drift 0.2, and restore values 0.60, 0.70, and 0.80 only.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260608-195834-929ed8236e-nonlabel_grown_basin_note`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The three live recompute rows at drift = 0.2 and restore = 0.60, 0.70, 0.80 have exact zero-source and neutral controls, opposite signed single-source responses, negative double-source responses, and charge exponents within the linear tolerance.  _(class `C`)_
- **chain closes:** True — The provided primary runner source contains a genuine recompute path: it builds the grown geometry, constructs geometry-sector adjacency, applies the signed source field, propagates amplitudes, and measures detector centroid shifts. The provided helper's hard-coded replay constants are not used on this load-bearing path.
- **rationale:** The bounded conclusion follows for exactly the three stated restore rows and does not rely on an external comparator or tuned empirical input. Independent checks of the restricted packet confirm the exact zero-source and same-point neutral cancellations by code identity, and the displayed charge exponents match log2(|double/plus|) for the recompute rows. The runner source's load-bearing computation is not a print-only or hard-coded expected-value path, and the helper's expected replay table is not on the relevant path. No cited non-retained authority or open bridge is present in the restricted packet.
- **auditor confidence:** medium

### `nonlabel_grown_drift_basin_note`

- **Note:** [`NONLABEL_GROWN_DRIFT_BASIN_NOTE.md`](../../docs/NONLABEL_GROWN_DRIFT_BASIN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite sweep over drift = {0.15, 0.20, 0.25} and seed = {0, 1, 2} at fixed restore = 0.70 for the grown-row geometry-sector non-label signed-source transfer.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-134905-48f224cbbe-nonlabel_grown_drift_basin_n`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The geometry-sector / non-label architecture survives the nearest drift grid at fixed restore = 0.7 with zero and neutral gates exactly zero, correct single-source sign orientation, negative double-charge response, and charge exponents within tolerance for all nine drift/seed rows.  _(class `C`)_
- **chain closes:** True — Within the stated finite grid, the included runner source and helper instantiate the grown geometry, sector adjacency, signed source field, propagation, and centroid readout rather than merely printing constants. Independent arithmetic on the displayed rows verifies the zero/neutral gates, sign orientation, double-charge sign, and log2 charge exponents within the stated tolerance.
- **rationale:** The load-bearing step is a bounded first-principles numerical replay inside the framework, not a renaming or an external comparator match. The cited upstream basin note is retained_bounded, which is retained-grade under the rubric, and the current claim adds a finite drift/seed sweep rather than importing an open bridge. The helper's hard-coded expected replay constants are not on the parent runner's load-bearing path for this claim. The clean verdict applies only to the stated finite grid at restore = 0.70, not to an unbounded drift basin.
- **auditor confidence:** high

### `nspt_high_order_lattice_alpha_n_coefficient_external_narrow_theorem_note_2026-05-16`

- **Note:** [`NSPT_HIGH_ORDER_LATTICE_ALPHA_N_COEFFICIENT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`](../../docs/NSPT_HIGH_ORDER_LATTICE_ALPHA_N_COEFFICIENT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Pure toy formal-series algebra over Fraction rationals, including finite partial sums, α=1/10 scalar powers, Cauchy products, a geometric surrogate truncation, and Fraction-preserving truncated update structure; no physical NSPT or SU(3) Wilson-plaquette claim was audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T122426Z-b7063501-nspt_high_order_lattice_-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On Fraction-coefficient formal power series, finite partial sums, scalar powers, Cauchy products, geometric truncation errors, and the toy truncated Langevin update close order-by-order in Fraction arithmetic.  _(class `A`)_
- **chain closes:** True — The narrowed conclusion follows from standard finite Fraction arithmetic and polynomial/Cauchy-product algebra as exercised by the runner. The note explicitly excludes the physics claims that would require external NSPT or lattice-gauge authorities.
- **rationale:** The operative claim is narrowed to elementary algebra over rational formal series, not a physical NSPT computation. The runner source performs finite Fraction arithmetic, Cauchy products, a geometric truncation calculation, and boundary-text checks; it does not import contested external constants or rely on a calibrated numerical match. Hard-coded expected values are used only as elementary algebraic test expectations for worked examples, not as imported premises for a broader physical conclusion.
- **auditor confidence:** high

### `ollivier_einstein_proxy_note_2026-04-11`

- **Note:** [`OLLIVIER_EINSTEIN_PROXY_NOTE_2026-04-11.md`](../../docs/OLLIVIER_EINSTEIN_PROXY_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On the audited periodic staggered torus, the potential-weighted Ollivier curvature proxy tracks G*T strongly and beats random/shuffled controls, but remains a bounded structured-curvature proxy rather than an Einstein-equation derivation.  _(class `C`)_
- **chain closes:** True — The primary runner reproduces the screened potential-weighted mean R²=0.9728 while density and combined definitions remain weak. The companion control runner reproduces the screened and low-screening control claims, including random/shuffled collapse and the low-screening shell-averaged near-match that limits the interpretation to a structured proxy.
- **rationale:** The note's bounded claim is supported by current runners: the potential-weighted construction gives strong R² against G*T, random and shuffled controls collapse, and the low-screening rerun survives. The same current output also supports the caveat that shell-averaged structured fields reproduce almost all of the low-screening signal, so dynamic backreaction and Einstein-equation closure are not established. Residual risk is the declared method-specific observable choice and missing open-boundary/Wilson comparison, both already outside the safe claim.
- **auditor confidence:** high

### `ordered_lattice_quasi_persistent_relaunch_2d_note`

- **Note:** [`ORDERED_LATTICE_QUASI_PERSISTENT_RELAUNCH_2D_NOTE.md`](../../docs/ORDERED_LATTICE_QUASI_PERSISTENT_RELAUNCH_2D_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded numerical replay of the six-row metric table for one fixed 2D ordered-lattice harness and one fixed Gaussian/top-k packet recipe.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-141901-30b1a9aa-ordered_lattice_quasi_pe-001`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** On the fixed h=0.5, W=12, L=20 ordered-lattice harness, the runner deterministically reproduces the six reported capture/carry/shift/relaunch/width metric rows within tight tolerances.  _(class `C`)_
- **chain closes:** True — The primary runner constructs the fixed lattice, packet, field, propagation, detector profiles, top-k reidentification, and metrics directly from included code, then checks the displayed table against computed values. No cited authority or external comparator is needed for the narrowed replay claim.
- **rationale:** The narrowed note does not claim persistent mass, family genericity, or an acceptance theorem; it claims only deterministic reproduction of a six-row numerical table on a fixed harness. The runner source performs the metric computation before comparing against pinned expected display values, and the helper source exposes the lattice generator and constants used in that path. Given the restricted scope, the chain closes as a bounded computational replay.
- **auditor confidence:** high

### `persistent_object_blended_readout_outer_transfer_sweep_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_BLENDED_READOUT_OUTER_TRANSFER_SWEEP_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_BLENDED_READOUT_OUTER_TRANSFER_SWEEP_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fixed exact-lattice h=0.25, blend=0.25 outer second-ring sweep: top3 passes 4/5 cases and top2 passes 1/5, with source1.0 closed; the uncached inward-source boundary row pattern is not audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-152136-02e6f5c5-persistent_object_blende-016`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Outer second-ring totals are top3 admissible on 4/5 cases and top2 admissible on 1/5 cases, with the only outer miss at source_z = 1.0.  _(class `C`)_
- **chain closes:** True — The cached primary runner and included helper sources compute the lattice propagation, source update, blended readout, alpha, overlap, and drift gates for the five outer cases, and the stdout matches the outer totals. The source note explicitly narrows the restricted-packet claim so the missing inward-source boundary stdout is not load-bearing.
- **rationale:** The primary runner does not merely print expected constants: it loops over the five specified cases and calls _run_mode for top2 and top3, while the provided helper sources instantiate the lattice, field, propagation, readout, and admissibility tests. The completed runner cache supports the stated outer second-ring top3 4/5 and top2 1/5 counts, including source1.0 as the sole outer closed case. This clean verdict applies only to the narrowed outer-sweep claim, not to the historical frozen inward-boundary pattern whose runner stdout is absent.
- **auditor confidence:** high

### `persistent_object_blended_readout_transfer_sweep_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_BLENDED_READOUT_TRANSFER_SWEEP_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_BLENDED_READOUT_TRANSFER_SWEEP_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The audited packet supports only the sliced four-case boundary probe for `top3` at fixed `blend=0.25`: baseline, source1.5, width4, and length7 under the stated gates.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260512-002551-332e8573-persistent_object_blende-006`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** `top3` with the fixed blended readout is admissible on each of the four boundary-probe cases at `blend = 0.25`.  _(class `C`)_
- **chain closes:** True — The provided runner output reports `adm=True` for `blend=0.25` on all four stated cases, and the runner source performs an actual lattice/source/readout computation rather than printing constants. The broader six-case, top2, readout-invariant, or inertial-mass closure framings are explicitly outside the audited scope.
- **rationale:** Within the narrowed sliced certificate, the claim matches the completed runner cache: all four named boundary cases pass for `top3` at `blend=0.25`. The runner source constructs the cases, computes Green-like fields, repeated top-k updates, detector probabilities, blended readout metrics, exponents, and drift gates; it does not hard-code the contested pass table. This is a bounded computational certificate, not support for the preserved broader original framing.
- **auditor confidence:** high

### `persistent_object_compact_inertial_probe_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_COMPACT_INERTIAL_PROBE_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_COMPACT_INERTIAL_PROBE_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded finite-run claim that the top3 compact exact-lattice object carries a stable weak-field response across the four specified nearby cases when allowing the passing broad or adaptive readout per case; not a single-readout, readout-invariant, persistent inertial-mass, or matter-closure claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-persistent_object_compact_inertial_probe_note-20260505`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** For top3, broad and adaptive readouts are each admissible on 3/4 cases, with complementary misses, so every one of the four tested nearby cases has at least one passing retained readout.  _(class `C`)_
- **chain closes:** True — The cached runner completed successfully and reproduces the note's pass map: top3 broad passes baseline, width4, and length7, while top3 adaptive passes baseline, source1.5, and width4, so the union covers all four cases under the stated gates. The note explicitly narrows the result to readout-dependent bounded response and excludes persistent inertial mass, matter closure, and readout-invariant law.
- **rationale:** The load-bearing claim is a bounded computational theorem over four enumerated exact-lattice cases, not a universal physical closure. The runner constructs the cases, source updates, broad/adaptive readouts, F~M exponents, kappa drifts, and admissibility gates, and the cached output matches the source note's table and stated complementary misses without hard-coding the top3 pass map. No one-hop dependencies are listed, and no external comparator or hidden retained dependency is needed for this scoped finite-run result. Residual risk is limited to the imported helper implementations behind the runner-defined lattice/readout machinery, so this clean verdict should not be cited beyond the bounded runner-defined scope.
- **auditor confidence:** high

### `persistent_object_exact_lattice_park_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_EXACT_LATTICE_PARK_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_EXACT_LATTICE_PARK_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the park note's bounded synthesis of the provided retained_bounded upstream exact-lattice persistent-object notes and the compact-update runner output, not an independent recomputation of all upstream sweeps.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-153947-c8646410-persistent_object_exact_-001`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The exact-lattice branch now supports a compact repeated-update object, weak-field response, retained blended readout, self-maintaining top4 multistage floor, widened-pocket 11/13 transfer, and beyond-pocket 4/5 transfer, while the inward-source rows remain closed.  _(class `B`)_
- **chain closes:** True — The conclusion is a conservative cross-note synthesis of the cited retained_bounded authorities: each component positive and the inward-source boundary are explicitly present in the restricted packet. The note does not claim persistent inertial-mass closure and preserves the stated limitations.
- **rationale:** The park note's load-bearing work is cross-note verification over retained_bounded inputs, plus the included compact-update runner source/output for the initial compact object step. All cited authorities in the restricted packet are retained_bounded and the final claim is scoped to a bounded beyond-pocket object-plus-response regime with a persistent inward-source boundary. No missing upstream note, open bridge, or unsupported promotion to closure-grade inertial mass is needed for the stated conclusion.
- **auditor confidence:** high

### `persistent_object_green_scout_note`

- **Note:** [`PERSISTENT_OBJECT_GREEN_SCOUT_NOTE.md`](../../docs/PERSISTENT_OBJECT_GREEN_SCOUT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The repeated self-consistent Green-like source object survives three updates with positive weak-field response and F~M=1.00 while remaining broad rather than sharply localized.  _(class `C`)_
- **chain closes:** True — The registered runner reproduces the zero-source reduction and frozen scout table: source N_eff stays about 4.788, detector N_eff stays about 497, all deltas are positive, and each update step has F~M=1.00 with 4/4 TOWARD. The note correctly keeps the claim at bounded quasi-persistent source-object scope.
- **rationale:** The bounded Green-scout claim is current with the primary runner and the output supports repeated source-object survival plus weak-field linear response. The object remains broad, with source N_eff near 4.788 out of 5 and detector response still broad, so the note does not claim a persistent inertial object or mass theorem. Residual risk is limited to the stated minimal exact-lattice loop rather than a hidden closure claim.
- **auditor confidence:** high

### `persistent_object_inward_boundary_floor_diagnosis_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_INWARD_BOUNDARY_FLOOR_DIAGNOSIS_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_INWARD_BOUNDARY_FLOOR_DIAGNOSIS_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite exact-lattice inward-source floor-width diagnosis with h=0.25, blend=0.25, three updates per segment, three chained segments, inward rows source0p75/source1p00/source1p25/source1p50, and top_keep in {4,5,6,8}; the ratified claim is the reported 2/4 admissible split at every width, with source0p75/source1p00 closed and source1p25/source1p50 open, excluding full local-pocket universality, beyond-pocket transfer, inertial-mass closure, and matter closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-judicial-20260512-persistent-object-inward-boundary-floor-diagnosis`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** The retained top4 cache gives the 2/4 inward split at top_keep=4, and the supplied top5/top6/top8 inward-source cache artifacts rerun the same deterministic runner on the same four inward rows and reproduce the same closed/open pattern at each widened floor.  _(class `C`)_
- **chain closes:** True — The bounded finite claim closes. The one-hop top4 dependency is already retained_bounded, the current top4 runner cache is status ok and reports source0p75/source1p00 inadmissible with source1p25/source1p50 admissible, and the top5, top6, and top8 inward-source artifacts all complete with exit-code-equivalent captured output showing the identical 2/4 split on the four cited inward rows. The note's broad physical claims remain explicitly excluded; within the scoped statement, the runner artifacts compute the load-bearing rows rather than hard-code the verdict. Residual risk is limited to the stated finite exact-lattice setup and does not extend to local-pocket universality, beyond-pocket transfer, inertial-mass closure, or matter closure.
- **rationale:** The bounded finite claim closes. The one-hop top4 dependency is already retained_bounded, the current top4 runner cache is status ok and reports source0p75/source1p00 inadmissible with source1p25/source1p50 admissible, and the top5, top6, and top8 inward-source artifacts all complete with exit-code-equivalent captured output showing the identical 2/4 split on the four cited inward rows. The note's broad physical claims remain explicitly excluded; within the scoped statement, the runner artifacts compute the load-bearing rows rather than hard-code the verdict. Residual risk is limited to the stated finite exact-lattice setup and does not extend to local-pocket universality, beyond-pocket transfer, inertial-mass closure, or matter closure.
- **auditor confidence:** high

### `persistent_object_multistage_floor_sweep_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_MULTISTAGE_FLOOR_SWEEP_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_MULTISTAGE_FLOOR_SWEEP_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Within the fixed exact-lattice setup h=0.25, blend=0.25, four source strengths, three updates per segment, three chained segments, and the same five stable widened-regime rows, top4 is the first configured multistage-admissible object width among top3/top4/top5/top6; top6 is only the exact five-source-node identity with top5.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-persistent-object-multistage-floor-audit-2-2026-05-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The bounded floor comparison reports top3: 0/5, top4: 5/5, top5: 5/5, top6: 5/5, so the first honest self-maintaining floor on this exact-lattice branch is top4, not top3.  _(class `C`)_
- **chain closes:** True — The bounded finite certificate closes from the packet: the primary runner verifies fresh SHA-pinned top3/top4 caches, parses the completed top5 log, checks the same five stable widened-regime rows, and derives top6 only from the five-node source-cardinality cap. The note does not claim full-pocket transfer, persistent inertial-mass closure, or matter closure as proved by this certificate.
- **rationale:** The clean result is bounded to the five-row configured floor certificate only. Top4 uses the same five stable widened-regime rows as the top3/top5 comparison, and top6 is correctly treated as an identity with top5 rather than independent extra evidence. The source note explicitly excludes full widened-pocket transfer, persistent inertial-mass closure, and matter closure, so the note does not overreach beyond the packet-supported bounded theorem.
- **auditor confidence:** high

### `persistent_object_readout_localization_note`

- **Note:** [`PERSISTENT_OBJECT_READOUT_LOCALIZATION_NOTE.md`](../../docs/PERSISTENT_OBJECT_READOUT_LOCALIZATION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The peak-centered localized detector readout sharply reduces detector effective support but fails to preserve the weak-field mass-scaling class: broad readout has F~M exponents near 1, while localized readout has exponents near 0 and only about 3.8% capture.  _(class `C`)_
- **chain closes:** True — The registered runner reproduces the zero-source reduction, broad readout N_eff=497.319 with step-wise F~M exponents 1.00,1.00,1.00, and localized readout N_eff=8.992 with exponents -0.00,-0.00,-0.00 and capture 0.038.
- **rationale:** Clean within the declared bounded-negative scope. The note does not claim detector/readout localization succeeds; it claims the tested peak-centered 3x3 window shrinks support but loses the weak-field mass law and captures too little detector mass. The current runner computes the broad and localized readouts from the exact lattice setup and reproduces the frozen reduction check, support sizes, TOWARD counts, capture fraction, and F~M exponents. Residual risk is only the note's stated narrow setup: one lattice family, one top3 repeated-update source object, and one peak-centered localization rule.
- **auditor confidence:** high

### `persistent_object_top3_multistage_probe_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_TOP3_MULTISTAGE_PROBE_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_TOP3_MULTISTAGE_PROBE_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The widened exact-lattice top3 branch fails the three-segment multistage persistence bar on all five stable widened rows, specifically because later-stage mean update overlap falls below 0.90 while compressed carry and kappa drift remain clean.  _(class `C`)_
- **chain closes:** True — The current top_keep=3 runner execution reproduced the note's 0/5 admissible summary and the row-level overlap/carry/drift pattern: baseline, source1.5, source2.75, width5, and length8 all fail by sub-threshold stage overlap with carry_mean=1.000 and max_kappa_drift=0.000%.
- **rationale:** Clean within the declared bounded-negative scope. The note does not claim persistent inertial-mass closure; it claims the top3 branch is compression-stabilized but not self-maintaining under the retained multistage persistence gate. The current registered runner computes the five stable widened-regime rows and reproduces the frozen 0/5 result, with the failure localized to stage-2/stage-3 overlap below 0.90 while TOWARD, F~M, carry, and kappa drift remain stable. Residual risk is the note's stated limitation: this is a diagnosis of the top3 exact-lattice branch, not a proof about other object architectures or broader floors.
- **auditor confidence:** high

### `persistent_object_top4_multistage_outer_transfer_sweep_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_TOP4_MULTISTAGE_OUTER_TRANSFER_SWEEP_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_TOP4_MULTISTAGE_OUTER_TRANSFER_SWEEP_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded claim that the retained exact-lattice `top4` multistage floor transfers on 4 of 5 specified one-ring-farther cases and preserves an inward-source boundary.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260512-003453-653c9554-persistent_object_top4_m-002`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The exact-lattice `top4` floor leaves the widened pocket because the completed one-ring-farther sweep is admissible on 4/5 cases, with only `source0.50` closed.  _(class `C`)_
- **chain closes:** True — The cited upstream authorities are retained_bounded and the provided runner cache completed successfully with stdout matching the note's 4/5 split. The primary runner defines the five outer cases and calls the shared `_run_case` computation rather than printing the contested result as a constant.
- **rationale:** The load-bearing result is a bounded first-principles compute over specified exact-lattice cases, not a definition, renaming, external comparator, or tuned numerical match. The completed cache reports exit code 0 and reproduces the exact case-level pattern claimed in the note. The conclusion is properly scoped as bounded beyond-pocket transfer with a persistent inward-source boundary, and the note explicitly disclaims direction-independent transfer, inertial-mass closure, and matter closure.
- **auditor confidence:** medium

### `persistent_object_top4_multistage_transfer_sweep_note_2026-04-16`

- **Note:** [`PERSISTENT_OBJECT_TOP4_MULTISTAGE_TRANSFER_SWEEP_NOTE_2026-04-16.md`](../../docs/PERSISTENT_OBJECT_TOP4_MULTISTAGE_TRANSFER_SWEEP_NOTE_2026-04-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite exact-lattice top4 multistage transfer sweep with h=0.25, blend=0.25, top_keep=4, three updates per segment, three chained segments, and exactly the 13 listed widened-pocket cases; support is the reported 11/13 admissible cases with failures at source0p75 and source1p00, excluding full local-pocket universality, persistent inertial-mass closure, and matter closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-persistent-object-top4-transfer-judicial-2026-05-07`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** The exact-lattice branch has a self-maintaining multistage top4 floor that transfers across most of the widened local pocket, with only a residual inward-source boundary between source_z=1.00 and source_z=1.25.  _(class `C`)_
- **chain closes:** True — The restricted packet supports the first audit. The source note is explicitly bounded and its exclusions match the audited scope. The primary runner enumerates the 13 listed cases, fixes top_keep=4 by default, delegates the admissibility computation to _run_case, and the imported computation fixes h=0.25, blend=0.25, N_UPDATES=3, N_STAGES=3, and gates overlap, direction, alpha band, kappa drift, and stage carry. The completed cache status is ok, its primary runner SHA matches the current file, and stdout reports 11/13 admissible with failures only at source0p75 and source1p00. The now-complete packet includes scripts/persistent_object_adaptive_readout_probe.py, resolving the second auditor's missing-file objection; inspection shows the adaptive readout functions used by _blended_probs are available in-packet and compute detector weights/centroids rather than hard-code the 11/13 outcome.
- **rationale:** The restricted packet supports the first audit. The source note is explicitly bounded and its exclusions match the audited scope. The primary runner enumerates the 13 listed cases, fixes top_keep=4 by default, delegates the admissibility computation to _run_case, and the imported computation fixes h=0.25, blend=0.25, N_UPDATES=3, N_STAGES=3, and gates overlap, direction, alpha band, kappa drift, and stage carry. The completed cache status is ok, its primary runner SHA matches the current file, and stdout reports 11/13 admissible with failures only at source0p75 and source1p00. The now-complete packet includes scripts/persistent_object_adaptive_readout_probe.py, resolving the second auditor's missing-file objection; inspection shows the adaptive readout functions used by _blended_probs are available in-packet and compute detector weights/centroids rather than hard-code the 11/13 outcome.
- **auditor confidence:** high

### `persistent_record_matched_compare_note`

- **Note:** [`PERSISTENT_RECORD_MATCHED_COMPARE_NOTE.md`](../../docs/PERSISTENT_RECORD_MATCHED_COMPARE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On matched generated DAGs, seeds, k-band, and post-barrier setup, the persistent-record lane is competitive and beats the entangling-env lane, but it is not the raw purity winner over node-label or graph-memory scars on the tested bounded slice.  _(class `C`)_
- **chain closes:** True — Fresh runner executions reproduced both matched tables: the full N=8,12 two-seed comparison including scar and the fast N=8,12,18 two-seed comparison without scar. The reported purity rankings and persistent-record gamma rows match the source note.
- **rationale:** Clean within the note's bounded comparison scope. The note explicitly rejects the strong raw-purity-winner claim and keeps the safe claim to matched small-slice competitiveness plus explicit residual branch-overlap structure. Current runner output reproduces the full N=8,12 table and the fast N=8,12,18 table, including node-label beating persistent records at N=12 and N=18 while persistent trace/gamma=1.0 remain materially better than the entangling-env row. Residual risk is the declared bounded slice: two seeds, selected N values, selected k band, and no asymptotic or closure claim.
- **auditor confidence:** high

### `persistent_record_overlap_kernel_note`

- **Note:** [`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`](../../docs/PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The mesoscopic persistent-record overlap kernel produces the reported bounded N=8,12,18 purity and detector-weighted overlap table, showing a live residual branch-connection lane but not asymptotic closure.  _(class `C`)_
- **chain closes:** True — The registered default runner reproduces the source note's mean purities, mean overlaps, and power-law fits for N=8,12,18 with three seeds and gamma=0.25,1.0.
- **rationale:** Clean within the note's bounded pilot scope. The note does not claim asymptotic solution or closure; it claims the persistent-record overlap-kernel lane is scientifically live on the N=8,12,18 probe while retaining nonzero branch overlap. The current runner reproduces the exact reported table and fit summary, including the N=18 rebound that prevents a stronger claim. Residual risk is the declared small-N bounded setup and the absence of broader seed or asymptotic stress testing.
- **auditor confidence:** high

### `physical_hermitian_hamiltonian_and_sme_bridge_note_2026-04-30`

- **Note:** [`PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md`](../../docs/PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Conditional algebraic free-staggered theorem: for real anti-Hermitian D satisfying P D P = -D, H=iD is Hermitian, Theta_H=P K preserves H, and the full Theta_H-odd Hamiltonian proxy vanishes; the runner additionally verifies direction-resolved proxies at L=4 and L=6. No SME operator-basis completeness or physical SME-coefficient conclusion was audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00050-physical_hermitian_hamiltoni`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** Because D is real and P D P = -D, the antiunitary Theta_H = P K sends H = iD to P(-iD)P = iD, so its Theta_H-odd projection vanishes.  _(class `A`)_
- **chain closes:** True — The antiunitary conjugation follows exactly from D being real, P D P=-D, and K(i)=-i; the odd projection then vanishes by substitution. The narrowed claim does not require the missing dictionary from this lattice proxy to every CPT-odd SME bilinear coefficient.
- **rationale:** The runner constructs D, C, P, H, and the direction-resolved hopping matrices and evaluates the claimed identities rather than printing constants or importing a contested result. Its L=4 and L=6 checks agree exactly with the load-bearing antiunitary algebra. Clean status applies only to the explicitly narrowed Hamiltonian-proxy statement, not to the withdrawn inference that all CPT-odd SME bilinear coefficients vanish.
- **auditor confidence:** high

### `pl_topology_infrastructure_textbook_import_note_2026-05-17`

- **Note:** [`PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`](../../docs/PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite cone-cap construction certificate for the explicit cubical-boundary family at R = 2, 3, 4 only; no arbitrary PL cap, S^3, homogeneity, or physical-closure claim is audited here.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-fresh-pl-topology-cone-cap-second-C75Ktt-2026-05-26`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** For each checked radius R = 2, 3, 4, the runner constructs the declared cubical boundary triangulation and cone-cap complex and verifies the five listed finite combinatorial properties.  _(class `A`)_
- **chain closes:** True — The note's narrowed claim is exactly the finite construction checked by the runner. There are no direct dependencies, and the runner constructs the finite complexes from R, counts the relevant faces/edges/tetrahedra, checks the apex link and Euler characteristics, and also checks that the note boundary withdraws the prior external PL-topology and physical-closure imports.
- **rationale:** The current note no longer imports PL Schoenflies, homogeneity, every-cap-homeomorphic closure, S^3 compactification, or physical closure as load-bearing conclusions. The executable evidence is bounded to R = 2, 3, 4 and verifies only finite combinatorial identities for the declared cubical-boundary cone-cap construction. This is clean as a bounded finite certificate, but it must not be cited as a general PL topology theorem or as a physical compactification theorem.
- **auditor confidence:** high

### `plaquette_v1_picard_fuchs_ode_note_2026-05-05`

- **Note:** [`PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md`](../../docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-runner certificate only: truncated Taylor-series ODE residual through the runner window, finite numerical agreement at beta=2,4,6,8,10, and the beta=6 logarithmic-derivative readout; no all-order Picard-Fuchs or all-order branch-identification claim was audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260608-185205-cec7d7f62a-plaquette_v1_picard_fuchs_od`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The finite runner verifies that the displayed third-order ODE annihilates the J(beta) Taylor series through the tested truncation and that its Frobenius branch agrees with direct Weyl integration at beta in {2,4,6,8,10}, yielding J'(6)/J(6)=0.422531739650.  _(class `C`)_
- **chain closes:** True — The restricted packet includes the primary runner source and completed output, and the code performs nontrivial symbolic series construction, ODE residual testing, ODE evolution, and direct Weyl quadrature rather than merely printing PASS. An independent Weyl constant-term coefficient check verified the listed Taylor coefficients, recurrence, indicial roots, and residual through degree 21, and an independent Gauss-Legendre Weyl quadrature matched the ODE Frobenius-branch values at the five sample points.
- **rationale:** The claim is explicitly narrowed to a finite certificate, and the supplied runner output supports exactly that bounded scope. There are no cited upstream authorities or open dependency paths in the packet, and the all-order Picard-Fuchs and Frobenius-branch assertions are excluded from scope. The beta=6 decimal is hard-coded as a displayed-value tolerance check in the runner, but it is also recomputed by direct Weyl integration and independently reproduced, so the bounded result does not reduce to an external numerical match.
- **auditor confidence:** high

### `pmns_oriented_cycle_selection_structure_note`

- **Note:** [`PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md`](../../docs/PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Only the three displayed finite 3 x 3 matrix identities for C, I_3, P_23, A_fwd(c), and the prescribed map S(A)=P_23 A^dagger P_23; no physical carrier, observable law, graph-derived interpretation, or PMNS prediction.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00056-pmns_oriented_cycle_selectio`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** Direct multiplication gives C A_fwd(c) C^dagger = A_fwd(c_2,c_3,c_1) and S(A_fwd(c)) = A_fwd(conjugate(c_3),conjugate(c_2),conjugate(c_1)), from which the stated fixed loci follow.  _(class `A`)_
- **chain closes:** True — The identities follow directly from the displayed matrix definitions: cyclic conjugation fixes exactly equal coefficient triples, I_3 has zero entries in the three forward-cycle slots, and the swap-conjugation fixed equation is equivalent to c_1=conjugate(c_3) with c_2 real.
- **rationale:** The source has narrowed the claim to dependency-free finite matrix algebra and explicitly excludes every physical or graph-derived bridge previously responsible for conditional verdicts. The runner constructs the displayed matrices and performs genuine matrix operations rather than importing or printing contested values; its eleven firewall checks and eight algebraic checks all pass. Although the runner demonstrates the fixed families through representative checks rather than symbolically proving exhaustiveness, the componentwise map displayed by its definitions makes the exact fixed-locus conclusions immediate.
- **auditor confidence:** high

### `pmns_tm2_magnitudes_conditional_bounded_note_2026-05-26`

- **Note:** [`PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md`](../../docs/PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Conditional algebraic determination of the PMNS magnitudes-squared matrix from a trimaximal second column, mu-tau equal moduli, doubly stochastic sums, and the supplied parameter s^2 = |U_e3|^2.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T130312Z-96c5c841-00072-pmns_tm2_magnitudes_conditio`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** The electron-row sum fixes |U_e1|^2 = 2/3 - s^2, while the first- and third-column sums together with mu-tau equality fix the remaining paired entries as 1/6 + s^2/2 and (1 - s^2)/2.  _(class `A`)_
- **chain closes:** True — The displayed entries follow uniquely from the stated row and column sums and mu-tau equality. Nonnegativity on 0 <= s^2 <= 2/3 follows directly from the resulting affine entries.
- **rationale:** The claim is a correct finite-dimensional algebraic theorem within its explicitly conditional scope and does not purport to derive the PMNS residual assumptions or a value of s^2. The runner exactly verifies 41 algebraic instances and structural checks, although it encodes the displayed matrix and samples finitely many parameter values; the general closure therefore rests on the note's direct symbolic proof. No empirical comparator, tuned input, renaming, or unclosed cited authority enters the audited conclusion.
- **auditor confidence:** high

### `pmns_tm2_residual_consequence_bounded_note_2026-05-26`

- **Note:** [`PMNS_TM2_RESIDUAL_CONSEQUENCE_BOUNDED_NOTE_2026-05-26.md`](../../docs/PMNS_TM2_RESIDUAL_CONSEQUENCE_BOUNDED_NOTE_2026-05-26.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The finite algebraic implication from stipulated trimaximal-second-column and mu-tau-modulus hypotheses to the TM2 sum rule, maximal atmospheric mixing, and maximal CP on the stated nonsingular phase chamber.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-20260709-225957-eb48eb29-pmns_tm2_residual_conseq-020`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Substituting the TM2 sum rule into the second-column modulus equation makes its phase-independent part exactly 2/3, leaving 2 c12 s12 s13 cos(delta_CP) = 0.  _(class `A`)_
- **chain closes:** True — The conclusions follow algebraically from the explicitly stipulated residual hypotheses and standard PMNS parametrization. The nonzero phase factor is stated as a hypothesis, and the excluded endpoint is handled correctly.
- **rationale:** The proof is a genuine class-A algebraic closure within its expressly bounded conditional scope and does not claim to derive the stipulated residuals from the framework. The runner performs the stated exact identities and endpoint checks rather than merely printing a verdict or importing external values. No cited open authority or unclosed bridge is required for the audited implication itself.
- **auditor confidence:** high

### `poisson_backreaction_live_threshold_packet_note_2026-05-29`

- **Note:** [`POISSON_BACKREACTION_LIVE_THRESHOLD_PACKET_NOTE_2026-05-29.md`](../../docs/POISSON_BACKREACTION_LIVE_THRESHOLD_PACKET_NOTE_2026-05-29.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite live assertion for scripts/backreaction_poisson_live_threshold_check.py on the declared G grid only: positive final deflection for every listed G and first listed escape < 1 at G=0.050.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260606-184414-8c422a67bc-poisson_backreaction_live_th`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** In the current finite Poisson self-gravity harness, TOWARD deflection is preserved on the tested G grid and detector escape crosses below one between G=0.020 and G=0.050; the first sub-unit escape point in the declared grid is G=0.050.  _(class `C`)_
- **chain closes:** True — The primary runner constructs the grid, calls the included Poisson helper functions to build fields and propagate amplitudes, and asserts the finite sign and escape inequalities reported in stdout. The helper source is included and does not import a contested threshold or hard-code the table values.
- **rationale:** The audited claim is explicitly bounded to the current finite harness and declared G grid, not to the archived G_crit claim or a continuum physical threshold. The runner computes the rows from the included propagation and self-field routines, then checks positive delta, escape > 1 at 0.011, 0.012, and 0.020, escape < 1 at 0.050, and first_subunit == 0.050. The provided stdout matches those inequalities, and the code path is computational rather than a mere printout or cross-note value import. The conclusion therefore closes at the bounded harness level.
- **auditor confidence:** high

### `post_record_character_path_channel_weight_prototype_2026-06-06`

- **Note:** [`POST_RECORD_CHARACTER_PATH_CHANNEL_WEIGHT_PROTOTYPE_2026-06-06.md`](../../docs/POST_RECORD_CHARACTER_PATH_CHANNEL_WEIGHT_PROTOTYPE_2026-06-06.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Exact normalization and multiplicative composition of finite hand-supplied path, channel, and character weights, together with a read-only scan reporting 21 current character/path/channel ledger rows.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T031137Z-0d389f16-00083-post_record_character_path_c`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** A supplied finite carrier with nonnegative local weights of positive total can be normalized exactly, with path weights composing multiplicatively, to form a finite path/channel/character weight packet.  _(class `A`)_
- **chain closes:** False — The finite arithmetic implication closes for the supplied examples, but no restricted authority derives the carrier, weights, or physical selector from Record. The note also claims coverage of 10 rows while the completed runner certifies 21, leaving its stated coverage certificate inconsistent.
- **rationale:** The Fraction-based normalization and path-product calculations are genuine class-A checks, not a first-principles framework computation. The carrier and weights are supplied inputs, while the firewall conclusions are hard-coded false flags and do not derive a physical measure or rule. The 10-versus-21 row-count mismatch is additional evidence that the source certificate is stale, although the bounded finite arithmetic remains valid.
- **auditor confidence:** high

### `post_record_conditional_audit_evidence_ladder_2026-06-06`

- **Note:** [`POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md`](../../docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md)
- **claim_type:** `meta`
- **claim_scope:** Branch-local audit-methodology classifier mapping supplied finite evidence patterns to allowed audit-lane readings, without applying audit verdicts or deriving physics laws.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-post_record_conditional_audit_evidence_ladder_2026-06-06-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The ladder is a finite classifier for what a bounded or conditional row is allowed to claim from the evidence it supplies.  _(class `E`)_
- **chain closes:** True — The restricted packet supports the classifier as a definition with internal consistency checks. It does not close as a first-principles derivation of the evidence rungs from axioms, and the note explicitly disclaims that stronger reading.
- **rationale:** Issue: the load-bearing step introduces the audit evidence ladder and its category map rather than deriving those categories from retained physics or axiom content. Why this blocks: the runner implements and checks the same finite rule table, including source-anchor text checks, so it verifies internal consistency but not independent theorem closure. Repair target: supply a retained audit-policy theorem deriving the sufficiency/blocked rungs, or keep this row scoped as a methodological definition. Claim boundary until fixed: branch-local classifier support only.
- **auditor confidence:** high

### `post_record_directed_certificate_examples_2026-06-06`

- **Note:** [`POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md`](../../docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Three finite directed-certificate examples under stipulated law, orientation, clock, and kernel data, including their exact expectations, probabilities, reversal-invariant count pushforwards, and accompanying row-bucket certificate.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-20260710-011703-de39c93e-post_record_directed_cer-090`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Exact enumeration of three explicitly supplied finite laws under forward and reverse orientations yields orientation-sensitive directed statistics while leaving count pushforwards invariant.  _(class `A`)_
- **chain closes:** False — The finite enumerations close algebraically on their stipulated inputs, but the chain from the framework baseline does not derive the supplied law/orientation/clock/kernel bridges. The note also claims 34 arrow-or-dynamics rows, whereas the completed primary and helper runners report 63.
- **rationale:** Issue: the directed-certificate arithmetic is exact, but its physical bridge inputs are stipulated, and the note's 34-row certificate contradicts the completed 63-row result. Why this blocks: the packet establishes conditional finite examples, not an axiom-derived orientation or dynamics bridge, and one stated runner certificate is stale. Repair target: derive the required bridge data in a retained theorem and correct the source-note count to 63 before rerunning. Claim boundary until fixed: the three supplied-input examples remain valid, while the eleven firewall PASS lines merely test locally initialized false flags and provide no derivation.
- **auditor confidence:** high

### `post_record_flow_thermal_stable_setting_certificate_2026-06-06`

- **Note:** [`POST_RECORD_FLOW_THERMAL_STABLE_SETTING_CERTIFICATE_2026-06-06.md`](../../docs/POST_RECORD_FLOW_THERMAL_STABLE_SETTING_CERTIFICATE_2026-06-06.md)
- **claim_type:** `meta`
- **claim_scope:** The audit covers only the introduced stable-setting classification interface, its supplied-rule toy checks, and the ledger bucketing; it does not establish physical selection, derive the supplied rules, or identify a stable setting with a selected dial.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T031137Z-0d389f16-00084-post_record_flow_thermal_sta`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** A supplied dial domain, supplied flow/score/thermal rule, supplied stability predicate, and exact check are defined to imply stable-setting support under that supplied rule.  _(class `E`)_
- **chain closes:** True — The restricted claim closes on its own terms as an explicit interface definition, and the runner correctly checks several finite examples under supplied rules. It does not close as a first-principles theorem because the stable-setting semantics are introduced rather than derived.
- **rationale:** The load-bearing implication is implemented by `stable_setting_status` as a definition over four Boolean inputs; it is not derived from an axiom or retained-grade authority. The score, fixed-point/separatrix, and thermal-root calculations are genuine elementary checks, but they only instantiate supplied examples and do not derive the general certificate semantics. The remaining runner checks largely verify text anchors, regex-based ledger classifications, hard-coded snapshot counts, exports, and hard-coded false firewall flags.
- **auditor confidence:** high

### `post_record_persistent_record_production_bridge_prototype_2026-06-06`

- **Note:** [`POST_RECORD_PERSISTENT_RECORD_PRODUCTION_BRIDGE_PROTOTYPE_2026-06-06.md`](../../docs/POST_RECORD_PERSISTENT_RECORD_PRODUCTION_BRIDGE_PROTOTYPE_2026-06-06.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite supplied pre-record/post-record bridge prototype for the three persistent_record_production_overlap rows, including exact pushforward and overlap arithmetic, not a derivation of the production law or kernel.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-post_record_persistent_record_production_bridge_prototype_2026-06-06-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** supplied pre-record word law + supplied record-writing update + supplied persistence rule + supplied overlap kernel on post-record states + exact pushforward/enumeration => law-scoped post-record distribution and overlap certificate  _(class `A`)_
- **chain closes:** False — The runner's finite arithmetic closes: the supplied law is normalized, the monotone update yields post-record tuples without internal probabilities, and the supplied kernel gives expected overlap 169/320. The chain does not close as a derived production bridge because the word law, record-writing update/persistence rule, and overlap kernel are supplied rather than derived from any cited retained authority or registered primitive.
- **rationale:** Issue: the finite pushforward and overlap arithmetic are valid for the runner's supplied word law, update, persistence rule, and kernel, but those bridge inputs are assumed rather than derived from the axiom packet. Why this blocks: with no cited retained authority or primitive supplying those inputs, the claim cannot close as a production-record bridge beyond the supplied finite witness. Repair target: a retained theorem deriving or explicitly admitting the record-writing law, persistence/readout rule, and overlap-kernel/production-time bridge. Claim boundary until fixed: the safe result is an exact finite supplied-bridge prototype with law-scoped expected overlap 169/320 and no internal probability field in realized post-record tuples.
- **auditor confidence:** high

### `post_record_production_dynamics_needed_row_map_2026-06-06`

- **Note:** [`POST_RECORD_PRODUCTION_DYNAMICS_NEEDED_ROW_MAP_2026-06-06.md`](../../docs/POST_RECORD_PRODUCTION_DYNAMICS_NEEDED_ROW_MAP_2026-06-06.md)
- **claim_type:** `meta`
- **claim_scope:** Read-only audit-companion taxonomy: six current `production_dynamics_needed` rows are mapped into three lanes with bridge-import lists and firewalls against deriving dynamics or promoting rows.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-post_record_production_dynamics_needed_row_map_2026-06-06-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The note hard-codes a table mapping the six current `production_dynamics_needed` rows into three lanes and lists the supplied bridge imports still needed for each lane.  _(class `E`)_
- **chain closes:** True — Under the narrowed meta scope, the explicit table/ROW_MAP and runner checks support that the six rows are mapped and that no dynamics claim is made. The chain does not close as a positive theorem because the lane and bridge classes are stipulated rather than derived.
- **rationale:** Issue: the load-bearing map is a hard-coded ROW_MAP/table, and the note explicitly says the production-dynamics import classes are not derived from Record or retained physics primitives. Why this blocks: the runner verifies anchor text, finite counts, and firewall flags, but it cannot turn the taxonomy into a retained production-dynamics theorem. Repair target: derive or cite retained bridge theorems for the lane and bridge assignments if the desired claim is theorem status rather than a read-only audit map. Claim boundary until fixed: the source supports only a meta/read-only map of six current rows to bridge-import classes.
- **auditor confidence:** high

### `post_record_retained_unbounded_dynamics_gate_2026-06-06`

- **Note:** [`POST_RECORD_RETAINED_UNBOUNDED_DYNAMICS_GATE_2026-06-06.md`](../../docs/POST_RECORD_RETAINED_UNBOUNDED_DYNAMICS_GATE_2026-06-06.md)
- **claim_type:** `meta`
- **claim_scope:** The packet was audited only as a branch-local finite gate map that records bounded finite-certificate discipline and names open retained/unbounded-family gates, not as a retained or unbounded dynamics theorem.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-101136-c6f729f5-post_record_retained_unbounded_dynamics_gate_2026-06-06-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Exact enumeration over finite objects does not by itself provide a law over an unbounded family, so the unbounded move is a separate gate requiring a supplied or derived family principle.  _(class `E`)_
- **chain closes:** True — The note and runner consistently define and check the finite gate-map/firewall declarations. The closure is definitional rather than a derivation of the upstream dynamics rows or an unbounded-family principle.
- **rationale:** Issue: the runner hard-codes the gate rows, statuses, and firewall booleans, then checks document presence and consistency. Why this blocks: that verifies a declared methodology/gate map, but it does not derive any retained status, physical dynamics bridge, production kernel, dial selection, probability law, or unbounded-family lift. Repair target: if a theorem is intended, provide retained upstream authorities or a runner that derives the relevant bridge/family principle rather than defining gate rows. Claim boundary until fixed: cite only the finite gate discipline and the explicitly open unbounded/effective-retained gates.
- **auditor confidence:** high

### `post_record_source_measure_trace_normalization_prototype_2026-06-06`

- **Note:** [`POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md`](../../docs/POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Supplied finite source weights and positive finite trace/reference weights normalize to exact RN densities satisfying finite expectation and composition identities, with the claimed 16/10/26 source/trace row coverage also in scope.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-post_record_source_measure_trace_normalization_prototype_2026-06-06-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** supplied finite carrier + supplied positive reference trace measure + supplied nonnegative source weights with positive total + exact Radon-Nikodym density => normalized source measure and trace/RN expectation identity  _(class `A`)_
- **chain closes:** False — The finite normalization/RN algebra closes from supplied finite weights by direct exact Fraction arithmetic. The full scoped claim does not close because the 16/10/26 row coverage is delegated to dynamically imported `scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py`, whose source/cache are absent from the restricted packet despite being imported by the primary runner.
- **rationale:** Issue: the primary runner dynamically imports the measure-weight subdivision runner for row enumeration and lane classification, but that helper source is not included while the packet says no helper imports were detected. Why this blocks: stdout alone is not authoritative for the claimed 16 source-measure/RN rows, 10 trace-normalization rows, and total 26-row coverage. Repair target: include the helper runner source and SHA-pinned cache, or inline an independently auditable row enumeration in the packet. Claim boundary until fixed: the supplied finite RN/trace normalization identity is exact, but row-coverage certification remains runner-artifact-conditional.
- **auditor confidence:** medium

### `qcd_low_energy_running_bridge_note_2026-05-01`

- **Note:** [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](../../docs/QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded alpha_s(v) -> alpha_s(M_Z) transfer-map kernel under the declared SM RGE, scale, threshold, and auxiliary-tuple imports on D = [0.085, 0.130]; PDG comparisons are appendix-only.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260621-054531-f51f6887-qcd_low_energy_running_bridge_note_2026-05-01-second`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The exact 1-loop map satisfies 1/T_1(a) = 1/a - L with the stated threshold constant, and the 2-loop matched map T_2 is grid-certified on D for well-definedness, monotonicity, expansivity, and center inverse round-trip.  _(class `A`)_
- **chain closes:** True — Within the declared bounded scope, the runner computes the SU(3) group factors, derives b0 and L, checks the exact T_1 formula independently against integration, and numerically certifies the stated T_2 grid properties. No preferred alpha_s(v) boundary value or PDG comparison is load-bearing.
- **rationale:** The claim is not a first-principles derivation of alpha_s or the SM RGE; it is a bounded theorem about the transfer map defined by declared imports. The runner source does real computation rather than merely printing constants: it recomputes SU(3) factors, integrates the 1-loop and 2-loop systems, checks independent integrator agreement, and separates the two PDG comparator checks as class D appendix material. The historical boundary value 0.103304 is not used in the load-bearing K1-K5 theorem surface, so the repaired claim is not a tuned numerical match.
- **auditor confidence:** high

### `qnm_control_hardening_note`

- **Note:** [`QNM_CONTROL_HARDENING_NOTE.md`](../../docs/QNM_CONTROL_HARDENING_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** It does not promote a quasi-normal mode result; it only freezes the control program that would be required before any QNM-style escape-spectrum claim could be reviewed safely.  _(class `A`)_
- **chain closes:** True — The note's claim is a scope restriction and control checklist, not a positive spectral theorem. It explicitly denies a QNM/escape-spectrum result and therefore closes as a bounded control-program note without needing a numerical runner.
- **rationale:** The source note is audit-clean only for its narrow boundary: QNM remains a hardening target and no quasi-normal-mode or escape-spectrum result is asserted. It does not attempt to derive or validate any spectral observable, and its listed five controls are stated as future prerequisites rather than achieved results. Residual risk is that this clean verdict must not be reused as evidence for a positive QNM lane; it ratifies only the bounded control-program framing.
- **auditor confidence:** high

### `quark_cp_carrier_completion_note_2026-04-18`

- **Note:** [`QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md`](../../docs/QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded existence-of-fit claim that one complex determinant-neutral 1-3 carrier per quark sector can numerically fit the imported quark/CKM comparator surface while preserving determinant phase closure.
- **audit_status:** ~~audited_numerical_match~~
- **effective_status:** ~~audited_numerical_match~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-hygiene-cycle-break-20260707-193821-5b3b16-quark_cp_carrier_completion_note-02`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Given imported comparator targets, two complex carrier coefficients xi_u and xi_d are solved numerically to reproduce the quark mass-ratio and CKM/J surface to about 1% or better while keeping arg det(M_u M_d)=0 mod 2pi.  _(class `G`)_
- **chain closes:** True — The restricted packet supports the bounded numerical-fit statement: the runner builds Hermitian mass matrices, optimizes xi_u and xi_d plus mass ratios, computes CKM observables and determinant phase, and passes the stated checks. It does not derive xi_u, xi_d, or the comparator targets from retained primitives.
- **rationale:** The load-bearing step is explicitly a tuned numerical completion against imported observation/atlas comparator targets, so it is class G. The primary runner is substantive rather than a trivial printout: it computes the matrices, diagonalizes them, forms CKM observables, and checks determinant phase closure. The co-cycle citation to docs/QUARK_CP_CARRIER_SLOT_MINIMALITY_THEOREM_NOTE_2026-06-17.md is non-load-bearing/informational for this bounded fit verdict; source-graph repair is still needed to remove or rewrite that markdown link before effective_status can leave retained_pending_chain. The result closes only as a bounded numerical match, not as a first-principles retained derivation.
- **auditor confidence:** high

### `quark_cp_small_correction_boundary_note_2026-06-17`

- **Note:** [`QUARK_CP_SMALL_CORRECTION_BOUNDARY_NOTE_2026-06-17.md`](../../docs/QUARK_CP_SMALL_CORRECTION_BOUNDARY_NOTE_2026-06-17.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the current shipped quark CP carrier fit, the fitted 1-3 carriers are 101.908728437 and 6.643337509 Schur-base units, so common caps R <= 5 exclude that fit; the capped scan is only bounded numerical evidence on the same parent slice.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-quark_cp_small_correction_boundary_note_2026-06-17-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Any sectorwise cap |xi_s| <= R_s |c13_s(base)| that contains the shipped solution must have R_u >= 101.908728437 and R_d >= 6.643337509, hence any common cap needs R >= 101.908728437.  _(class `A`)_
- **chain closes:** False — The cap inequalities themselves follow algebraically once the parent fitted xi pair and Schur-base terms are accepted. The chain does not close from axiom/retained inputs because the packet does not derive the fitted carriers, comparator/readout targets, or a framework-native normalization for the non-perturbative carrier.
- **rationale:** The primary runner computes the parent solution through helper routines and then evaluates the claimed ratios, so it is not merely printing the note's constants. The exact small-correction boundary is a valid algebraic consequence of the supplied parent fitted solution. However, the load-bearing inputs are the fitted xi carriers and target surface of a bounded parent completion, and the note explicitly leaves their derivation, readout bridge, and non-perturbative normalization open. The row therefore supports only a conditional boundary on the current parent slice, not a retained-grade closure.
- **open / conditional deps cited:**
  - `QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md`
- **auditor confidence:** high

### `quark_route2_double_local_projector_normalization_bridge_conditional_note_2026-06-21`

- **Note:** [`QUARK_ROUTE2_DOUBLE_LOCAL_PROJECTOR_NORMALIZATION_BRIDGE_CONDITIONAL_NOTE_2026-06-21.md`](../../docs/QUARK_ROUTE2_DOUBLE_LOCAL_PROJECTOR_NORMALIZATION_BRIDGE_CONDITIONAL_NOTE_2026-06-21.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Conditional bounded bridge: if q_X is supplied as proportional to w_X^-2, then lambda=9/4, q_E=15/8, rho_E=21/4, and nearby monomial laws fail.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-gpt-5-fresh-context-route2-2026-07-09`  (codex-current; independence=weak)
- **load-bearing step:** If a future proof derives the double-local projector normalization, then lambda=(w_E/w_T1)^-2=9/4 and the endpoint chain closes.  _(class `A`)_
- **chain closes:** None — The endpoint algebra closes only after supplying the double reciprocal local projector-normalization law q_X proportional to w_X^-2; that bridge is an explicit primitive/premise in the packet, not a derived result.
- **rationale:** Issue: the double reciprocal local projector-normalization law q_X proportional to w_X^-2 is not derived from packet inputs; it is the named missing primitive. Why this blocks: the endpoint rho_E=21/4 follows only after that normalization bridge is admitted. Repair target: derive the double-local normalization from Route-2 source/tensor/readout structure, with a runner that computes the bridge rather than selecting p=-2 against lambda=9/4. Claim boundary until fixed: the note cleanly isolates the conditional algebra and falsifies nearby monomial laws, but it is not a current-surface derivation.

### `radial_scaling_protected_angle_narrow_theorem_note_2026-05-02`

- **Note:** [`RADIAL_SCALING_PROTECTED_ANGLE_NARROW_THEOREM_NOTE_2026-05-02.md`](../../docs/RADIAL_SCALING_PROTECTED_ANGLE_NARROW_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Standalone exact Euclidean-geometry theorem that positive radial scaling (rho, eta) -> (mu rho, mu eta) in the open first quadrant preserves the origin slope, origin angle, doubled angle, scales radius by mu, and does not preserve the finite tangent readout from (1,0) except at mu = 1 on the guarded subdomain rho != 1 and mu*rho != 1.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-radial-scaling-protected-angle-audit-2-2026-05-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** eta_bar / rho_bar = (mu eta) / (mu rho) = eta / rho, since mu > 0 cancels; the origin angle and doubled-angle identities then depend only on this preserved slope, and the (1,0)-based finite tangent difference factors as eta*(mu - 1)/((1 - mu*rho)*(1 - rho)).  _(class `A`)_
- **chain closes:** True — The scoped claim is pure algebra and elementary plane geometry over abstract positive real symbols with no cited dependencies. The note explicitly guards the finite-tangent exclusions needed for T4, so the factorization proves the iff condition on its stated domain.
- **rationale:** The load-bearing step is a direct algebraic cancellation under positive radial scaling, with standard arctan and double-angle consequences, and the runner independently verifies the symbolic slope, origin-angle, doubled-angle, radius, and finite-tangent factorization checks. Residual risk is limited to scope control: this clean verdict covers only the abstract Euclidean radial-scaling theorem and does not ratify any CKM-specific assignment, physical observable bridge, or upstream parent framing.
- **auditor confidence:** high

### `record_axiom_audit_application_map_2026-06-06`

- **Note:** [`RECORD_AXIOM_AUDIT_APPLICATION_MAP_2026-06-06.md`](../../docs/RECORD_AXIOM_AUDIT_APPLICATION_MAP_2026-06-06.md)
- **claim_type:** `meta`
- **claim_scope:** The finite classifier assigning seven record-sensitive lane shapes to gates declared supported or still missing under the Record schema, without promoting downstream claims or applying audit verdicts.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260710T031137Z-0d389f16-00091-record_axiom_audit_applicati`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** Record supports durable realized outcomes, finite additive scalar readout, arbitrary finite-prefix count/readout schemas, and post-record label consumption.  _(class `E`)_
- **chain closes:** False — The runner computes set differences only after hard-coding both the Record-supported gate set and every lane's required gates. Neither the Record axiom content nor a derivation of those gate assignments is included, so the substantive classification is assumed rather than established.
- **rationale:** The runner genuinely checks file existence, anchor phrases, and internal set consistency, but its load-bearing support map is introduced as a constant. Its 39 passing checks therefore validate a stipulated classifier rather than derive the classifier from the Record axiom. The result is useful as bounded audit metadata, but it is definition-grade rather than theorem-grade.
- **auditor confidence:** high

### `record_conditional_law_period_scaling_l3_to_l4_bounded_theorem_note_2026-06-11`

- **Note:** [`RECORD_CONDITIONAL_LAW_PERIOD_SCALING_L3_TO_L4_BOUNDED_THEOREM_NOTE_2026-06-11.md`](../../docs/RECORD_CONDITIONAL_LAW_PERIOD_SCALING_L3_TO_L4_BOUNDED_THEOREM_NOTE_2026-06-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite runner-defined diagnostic for the stated L=3 and L=4 ring events, occupancies, seeds, depths, sparse Fock evolution, SVD-polar determinant readout, and fixed seeded 300-draw label-permutation null protocol.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-023644-3b04cce6-record_conditional_law_period_scaling_l3_to_l4_bounded_theorem_note_2026-06-11-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** For the stated L=3/L=4 events, occupancies, seeds, depth choices, and fixed seeded 300-draw sampled-null protocol, the L=4 tested profiles are monotone and their sampled-null diagnostic gaps are comparable-or-larger by the displayed median comparison.  _(class `C`)_
- **chain closes:** True — The runner source constructs the finite Fock operators, evolves the stated seeded samples, computes determinant phases, fixed-prefix statistics, sampled-null p95 values, monotonicity, and median gap comparison rather than reading or hard-coding the contested numerical outputs. The note confines the conclusion to that finite diagnostic and explicitly forbids promotion to an exhaustive null theorem, period law, or upstream framework law.
- **rationale:** The load-bearing step is a bounded first-principles finite computation over the runner-defined objects, with no cited one-hop authority or external comparator required for the scoped claim. The runner code is not a constant-printing or numerical-match artifact: it builds the sparse/dense evolution machinery, computes the profiles and sampled-null diagnostics, and checks the relevant inequalities. The clean verdict applies only to the explicitly scoped finite sampled-null diagnostic, not to gap-growth laws, exhaustive permutation-null clearance, physical U(1) gauge identification, or L>=5/Z^3 behavior.
- **auditor confidence:** high

### `record_conditional_law_three_point_period_series_bounded_theorem_note_2026-06-11`

- **Note:** [`RECORD_CONDITIONAL_LAW_THREE_POINT_PERIOD_SERIES_BOUNDED_THEOREM_NOTE_2026-06-11.md`](../../docs/RECORD_CONDITIONAL_LAW_THREE_POINT_PERIOD_SERIES_BOUNDED_THEOREM_NOTE_2026-06-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the stated L=3, L=4, and L=5 ring events, occupancies, seeds, depths, sparse Fock evolution/SVD-polar determinant readout, and fixed seeded 300-draw sampled-null protocol, the displayed min-gain ledger, sampled-null gaps, and non-monotone gap-median series are audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260618-023644-3b04cce6-record_conditional_law_three_point_period_series_bounded_theorem_note_2026-06-11-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** For the stated L=3/L=4/L=5 events, occupancies, seeds, depth choices, and fixed 300-permutation sampled-null protocol, the three-point min-gain ledger and sampled-null gap series have the displayed values.  _(class `C`)_
- **chain closes:** True — The runner source constructs the finite sparse Fock systems, evolves them with expm_multiply, computes determinant phases, prefix statistics, sampled-null p95 values, min-gains, and medians, and its cached output matches the source note. The closure is only for the explicitly scoped finite diagnostic, not an exhaustive permutation null, asymptotic law, or physical U(1) gauge-field claim.
- **rationale:** The load-bearing numbers are computed directly by the provided runner rather than imported from the cited authority or hard-coded as a print-only result. The one-hop authority is retained_bounded, which is retained-grade under the rubric, and the source note explicitly confines load-bearing content to the runner-defined finite objects. The negative conclusion is scoped to the displayed finite period series and does not overclaim an all-permutation null, asymptotic behavior, L>=6 behavior, or a physical gauge interpretation.
- **auditor confidence:** high

### `record_markov_generator_premise_classifier_2026-06-06`

- **Note:** [`RECORD_MARKOV_GENERATOR_PREMISE_CLASSIFIER_2026-06-06.md`](../../docs/RECORD_MARKOV_GENERATOR_PREMISE_CLASSIFIER_2026-06-06.md)
- **claim_type:** `meta`
- **claim_scope:** Audited the stated premise taxonomy and the finite two-state stochasticity, determinant-obstruction, generator, and semigroup checks for the record Markov-generator classifier.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-record_markov_generator_premise_classifier_2026-06-06-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner classifies dynamics claims into four premise levels separating post-record information, production kernels, Markov semigroups, and physical-rate models.  _(class `E`)_
- **chain closes:** False — The finite matrix checks close exactly, but the classifier gates themselves are stipulated as a premise map. No cited authority or first-principles axiom derivation is provided showing that this taxonomy follows rather than being defined.
- **rationale:** Issue: the load-bearing classifier levels and gates are introduced by definition, not derived from retained inputs or first-principles framework dynamics. Why this blocks: the note can support a reusable taxonomy and exact finite examples, but not a retained derivation of a dynamics law, kernel, bridge, clock, or rate normalization. Repair target: supply a theorem deriving the gate structure from accepted axioms or split the finite algebraic checks from the stipulated classifier surface. Claim boundary until fixed: cite only the premise discipline and the checked two-state examples.
- **auditor confidence:** high

### `record_permanence_forces_fresh_site_double_registration_and_agreement_survival_bounded_theorem_note_2026-07-11`

- **Note:** [`RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md`](../../docs/RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fresh-site necessity in the explicit monotone site-tagged history, plus fixed-orbit and finite-horizon consequences of the supplied agreement-conditioned map.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.6; independence=fresh_context)
- **load-bearing step:** For events already represented as formation of new site-tagged records, coexistence at a reused site violates one-record-per-site while overwrite violates permanence; the supplied map then has constant orbits exactly at its fixed points.  _(class `C`)_
- **chain closes:** False — The Record-clause and map algebra closes on the supplied representation, but the agreement-conditioned parent is unaudited and the physical formation, readout, outcome-independence, and multiplicity conditions remain supplied.
- **rationale:** Issue: the site-history theorem and exact map/escape algebra are correct, but the agreement-conditioned parent is unaudited and the physical formation, common-readout, outcome-independence, and flow-class conditions have no retained law-domain certificates. Why this blocks: the exact local implications cannot be promoted into a physical durability/self-composition bridge. Repair target: retain the anatomy parent and derive the supplied formation/readout/filter conditions with lattice-motion-covariant, record-decidable certificates. Claim boundary until fixed: only the explicit site-tagged monotone histories and the supplied scalar map have the stated necessary and finite-horizon consequences.
- **open / conditional deps cited:**
  - `RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`
- **auditor confidence:** high
- **No-Go Discipline:** `PASS`

### `reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10`

- **Note:** [`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For finite or compact measured spaces with measure-preserving involution Theta, real Theta-invariant S_+, reflection-Hermitian F, and psi^2 F in L2 where psi^2=exp(-S_+), the reflected integral equals ||psi^2 F||_2^2 >= 0 and induces the weighted L2 Hermitian positive semidefinite form. Full Wilson plaquette RP, fermion determinant positivity, combined gauge+fermion RP, transfer-matrix normalization/vacuum subtraction, physical Hilbert-space identification, and framework-action satisfaction of the hypotheses are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-five-judge-panel-majority-20260529-rp-gauge-half-cs`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** Using S_+(Theta x)=S_+(x) and F(Theta x)=overline{F(x)}, the integrand exp(-S_+(x)) exp(-S_+(Theta x)) F(Theta x) F(x) becomes exp(-2S_+(x)) |F(x)|^2 = |psi^2(x) F(x)|^2.  _(class `A`)_
- **chain closes:** True — Five-judge panel result: 5/5 judges sided with the fresh positive-theorem retag. The restricted source proves a direct pointwise algebraic identity followed by integration: exp(-S_+(x)) exp(-S_+(Theta x)) F(Theta x) F(x) = exp(-2S_+(x)) |F(x)|^2 = |psi^2 F|^2, so the reflected integral is a real nonnegative weighted-L2 norm square and the associated form is Hermitian PSD. The runner exits cleanly with PASS=27 FAIL=0, all class-A checks, but the proof does not depend on the runner. The ratified claim is the exact conditional mathematical theorem under stated hypotheses; it does not assert that the framework Wilson/gauge/fermion action satisfies those hypotheses.
- **rationale:** Five-judge panel result: 5/5 judges sided with the fresh positive-theorem retag. The restricted source proves a direct pointwise algebraic identity followed by integration: exp(-S_+(x)) exp(-S_+(Theta x)) F(Theta x) F(x) = exp(-2S_+(x)) |F(x)|^2 = |psi^2 F|^2, so the reflected integral is a real nonnegative weighted-L2 norm square and the associated form is Hermitian PSD. The runner exits cleanly with PASS=27 FAIL=0, all class-A checks, but the proof does not depend on the runner. The ratified claim is the exact conditional mathematical theorem under stated hypotheses; it does not assert that the framework Wilson/gauge/fermion action satisfies those hypotheses.
- **auditor confidence:** high

### `relative_orientation_fusion_state_selection_pointer_frame_one_vacuous_quotient_bounded_theorem_note_2026-06-10`

- **Note:** [`RELATIVE_ORIENTATION_FUSION_STATE_SELECTION_POINTER_FRAME_ONE_VACUOUS_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-06-10.md`](../../docs/RELATIVE_ORIENTATION_FUSION_STATE_SELECTION_POINTER_FRAME_ONE_VACUOUS_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-06-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the supplied C^3 color carrier and the named frame-naming/color-blind instrument classes, the joint state/frame global SU(3) orientation has one shared vacuous diagonal quotient while state spectra, instrument class, and relative orientation remain distinct registrable data; local ADM-1 frame roots, weights, and r are not touched.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260610-212719-57b0292243-relative_orientation_fusion_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Trace cyclicity makes all tested record consequences invariant under the simultaneous rotation (rho,u)->(g rho g†,g u), and the rank/tomography check shows the only nontrivial absolute-orientation quotient is the 8-dimensional diagonal SU(3) direction, with the remaining kernel directions being the 2 state stabilizers.  _(class `A`)_
- **chain closes:** True — The diagonal invariance follows directly from covariant projector conjugation and trace cyclicity. Independently, dim SU(3)=8 and a generic 3-level density matrix has a 2-dimensional stabilizer, so the 16 state/frame orientation directions can have rank 6 with a 10-dimensional kernel exactly as claimed.
- **rationale:** The runner source performs actual finite-dimensional linear algebra and Fock-space computation rather than printing constants or importing a contested premise. The cited graph-first SU(3) authority is marked retained, and the claim does not rely on an unretained one-hop dependency. The theorem is properly bounded to the supplied carrier, named instruments, and global rotations; it explicitly avoids discharging the local frame root or assigning weights.
- **auditor confidence:** high

### `replay_environment_note`

- **Note:** [`REPLAY_ENVIRONMENT_NOTE.md`](../../docs/REPLAY_ENVIRONMENT_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-fresh-agent-019de5de`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The provided runner implements the stated convention by doing nothing when numpy is importable, re-execing the target script under /usr/bin/python3 when numpy is missing and the current interpreter is different, and otherwise exiting with a clear local error; current inspection confirms the helper loads and numpy is importable under the declared system path, with several retained replay scripts calling the helper.  _(class `B`)_
- **chain closes:** True — Within the restricted inputs, the note's operational claims close: the runner script matches the documented bootstrap behavior, the current inspection output supports that the helper is present and importable, and the usage search supports the claim that relevant retained numpy replay lanes call it. The note also explicitly limits its scope to local operational reproducibility and disclaims CI enforcement, scientific promotion, and generalization beyond this host.
- **rationale:** The support note is internally accurate against the provided runner and inspection output. Its load-bearing operational convention is implemented by the bootstrap helper and reflected in listed script usages. Because the claim boundary is explicitly local, non-scientific, and non-CI-enforced, no hidden premise is needed for the stated support-level claim.
- **auditor confidence:** high

### `retardation_discriminator_note`

- **Note:** [`RETARDATION_DISCRIMINATOR_NOTE.md`](../../docs/RETARDATION_DISCRIMINATOR_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite toy-harness assertion-gated result for the frozen graph families, fixed source setup, exact nulls, delay-5 difference curve, delay-law checks, global-delay residual, family/seed robustness, and phase-sensitivity slice.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T200423Z-48dc42e1-retardation_discriminato-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Within the stated graph family and imposed oscillating-source setup, the delay-difference curve distinguishes finite-propagation response from the instantaneous response to the same imposed source.  _(class `C`)_
- **chain closes:** True — The runner source constructs the finite toy graph and propagation amplitudes from fixed parameters, computes instantaneous and retarded phases, and assertion-gates the reported observable surface. The broader no-instantaneous-emulator theorem is explicitly out of binding scope, so it is not needed for this audited claim.
- **rationale:** The binding claim has been narrowed to a finite deterministic toy-harness computation, not gravitational-wave detection or a general exclusion theorem. The supplied runner source performs the graph growth, propagation, phase extraction, and residual checks rather than merely printing constants; the hard-coded values are used as assertion gates against computed quantities. The cached run exits 0 with 31 passing checks and no helper imports or upstream dependencies are missing.
- **auditor confidence:** high

### `retarded_field_causality_probe_note`

- **Note:** [`RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md`](../../docs/RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded numerical probe comparing detector centroid shift under instantaneous versus retarded imposed fields on a four-seed compact generated 3D DAG family.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260504-232946-c1a20bdf-retarded_field_causality-005`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Finite propagation speed changes the detector deflection on this retained compact generated DAG family, while c = inf returns the instantaneous limit.  _(class `C`)_
- **chain closes:** True — Within the restricted packet, the runner constructs generated DAG instances, computes instantaneous and retarded imposed fields, propagates amplitudes, and reports a nonzero finite-c delta with exact c = inf reduction. The conclusion is limited to this field-scheduling proxy and does not claim a self-consistent wave theory.
- **rationale:** The note's bounded conclusion matches the runner's computed rows: finite c changes the centroid-shift observable, and c = inf reproduces the instantaneous baseline. The runner does not merely print constants or compare to an external fitted value; it builds the compact family, applies the retarded scheduling rule, and computes the observable. The claim is narrow and explicitly preserves the limitation that this is an imposed field-scheduling proxy rather than a full dynamical gravitational wave theory.
- **auditor confidence:** medium

### `retarded_field_compact_refinement_note`

- **Note:** [`RETARDED_FIELD_COMPACT_REFINEMENT_NOTE.md`](../../docs/RETARDED_FIELD_COMPACT_REFINEMENT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Two-family compact/refined retarded-field smoke probe showing the retarded and instantaneous detector-centroid rows remain different on both families, with nonzero mean split but row-sign-dependent behavior rather than uniform suppression.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The compact and refined families have mean inst-ret splits of -1.669200e-02 and -4.352319e-02, with retarded below instantaneous on 0/5 and 3/5 b-rows respectively, so the split survives but is not uniformly directional.  _(class `C`)_
- **chain closes:** True — The registered runner cache is complete and matches the source note's two-family table and safe-read boundary. The audited result is only the finite smoke-probe noncollapse/partial-survival statement, not a universal retarded-gravity law or refinement-stability theorem.
- **rationale:** The current cache supports the note's bounded table exactly: the retarded field differs from the instantaneous field on both compact and refined families, but the sign/direction is row-dependent. The source already confines the claim to a causality/scheduling smoke probe and disclaims a full wave theory or universal law. Residual risk is limited to the small two-family sample and lack of assertion gates, which does not block the audited finite readout.
- **auditor confidence:** high

### `s3_cap_uniqueness_note`

- **Note:** [`S3_CAP_UNIQUENESS_NOTE.md`](../../docs/S3_CAP_UNIQUENESS_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite cone-cap construction certificate for the explicit cubical-ball boundary family at R=2,3,4,5: finite boundary, cone, link, face-pairing, and Euler-characteristic checks only. No global cap uniqueness, physical closure, arbitrary PL cap classification, or PL S^3 compactification claim is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-fresh-context-s3-cap-20260527-r2`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** For the explicit cubical-ball family constructed by the runner at R=2,3,4,5, the checker constructs the boundary triangulation and cone complex and verifies the listed finite incidence, link, boundary, and Euler facts.  _(class `A`)_
- **chain closes:** True — Fresh-context independent check confirmed this is finite combinatorics over the declared runner family: edge-degree two and vertex-link cycle checks make the boundary a closed triangulated 2-manifold in the checked cases; coning gives apex link equal to the base triangulation, paired non-base cone faces, and chi_cap=1. The source excludes global uniqueness and PL S^3 conclusions.
- **rationale:** The second audit agrees that the narrowed bounded certificate closes only for the explicit finite construction. The runner directly constructs the cubical balls, boundary triangulations, and cone complexes for R=2,3,4,5, while the source explicitly removes global PL cap uniqueness, physical closure, Schoenflies/Alexander/Perelman/Moise imports, and PL S^3 identification.
- **auditor confidence:** high

### `s3_endpoint_fiber_uniform_lift_support_2026-06-27`

- **Note:** [`S3_ENDPOINT_FIBER_UNIFORM_LIFT_SUPPORT_2026-06-27.md`](../../docs/S3_ENDPOINT_FIBER_UNIFORM_LIFT_SUPPORT_2026-06-27.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite theorem: for any stated total surjective four-label-to-three-axis quotient with uniform axis law, fiber-uniform lift, and E/T-channel symmetry, the endpoint weights are exactly the shell-pair or center-pair 1/6,1/3 laws; no physical endpoint quotient, same-source readout, or calibration closure is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-context-s3-endpoint-auditor-2026-07-09`  (codex-current; independence=fresh_context)
- **load-bearing step:** If the lifted law is also E/T-channel symmetric, then the two-label fiber must pair same-radial labels, leaving exactly the shell-pair and center-pair lifted laws with radial 1:2 or 2:1 weights.  _(class `A`)_
- **chain closes:** True — The finite enumerative consequence closes under the stated quotient-lift premises; the note names physical quotient, same-source readout, and calibration bridges as out-of-scope future targets rather than consuming them.
- **rationale:** The finite claim closes as an exact algebraic/enumerative consequence of the stated quotient-lift premises. The note explicitly does not claim the physical four-to-three quotient, physical fiber-uniform lift, same-source readout, or typing/calibration bridges; those are named as remaining theorem targets rather than silently imported. A physical endpoint-use claim would be conditional, but the audited bounded support theorem is scoped only to the algebraic consequence under those premises.
- **auditor confidence:** high

### `s3_taste_cube_decomposition_note`

- **Note:** [`S3_TASTE_CUBE_DECOMPOSITION_NOTE.md`](../../docs/S3_TASTE_CUBE_DECOMPOSITION_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Abstract finite-group representation theorem for the tensor-position permutation action of S_3 on C^8 = (C^2)^{\otimes 3}; no framework taste-cube carrier or physical flavor interpretation is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-judicial-panel-per-site-k1-20260523T141038Z-s3_taste_cube_decomposition_note-majority`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** Under tensor-position permutations of S_3 on C^8 = (C^2)^{\otimes 3}, the class character is chi(e)=8, chi(2-cycle)=4, chi(3-cycle)=2, giving C^8 ~= 4 A_1 + 2 E with no A_2 summand.  _(class `A`)_
- **chain closes:** True — Five-judge panel majority 5/5 ratified the second tuple (audited_clean, positive_theorem, class A). Vote breakdown: J1: second / audited_clean / positive_theorem / class A; J2: second / audited_clean / positive_theorem / class A; J3: second / audited_clean / positive_theorem / class A; J4: second / audited_clean / positive_theorem / class A; J5: second / audited_clean / positive_theorem / class A. Majority rationale: The restricted packet cleanly separates the abstract finite-dimensional S_3 representation statement from the open framework-carrier interpretation. For the abstract theorem, the runner constructs the permutation matrices, computes the characters, and applies standard S_3 character multiplicity formulas, so the load-bearing step is class A and the chain closes without the staggered-Dirac gate. The open gate blocks only the taste-cube/physical-flavor reading, not the standalone abstract representation theorem; positive_theorem is therefore the correct claim_type for the narrowed audited scope. | The restricted packet supports the abstract finite-dimensional representation theorem directly by standard S_3 character algebra and by a runner that constructs the permutation matrices and computes the characters and multiplicities. The open staggered-Dirac/taste-cube carrier identification is explicitly excluded from the audited scope, so it should not force the abstract theorem to remain bounded. Reclassification to positive_theorem is correct only for the abstract S_3-on-C^8 statement; any framework-carrier or physical flavor use remains gated. | The restricted packet cleanly proves the abstract finite-dimensional S_3 representation statement by constructing the tensor-position permutation representation, computing its class characters, and applying standard S_3 character theory. The open staggered-Dirac/taste-cube carrier interpretation is explicitly excluded from the audited scope, so it does not force the abstract theorem to remain bounded. The first audit correctly found class A and audited_clean but kept claim_type as bounded_theorem despite the narrowed abstract theorem having no open dependency inside scope. The second audit gives the internally consistent applyable tuple for the targeted reclassification. | The restricted packet cleanly supports the abstract finite-dimensional representation theorem by direct algebraic computation and standard S_3 character theory. The runner constructs the permutation matrices, computes traces, verifies sector decomposition, and contains no external comparator, tuned input, or import of the open staggered-Dirac carrier identification. Because the ratified scope explicitly excludes the framework taste-cube and physical flavor readings, the open staggered-Dirac gate does not force the abstract theorem to remain bounded. | The narrowed audited claim is a finite-dimensional representation-theoretic statement over an explicitly defined S_3 action, and it closes by ordinary character algebra plus the provided runner computation. The open staggered-Dirac realization gate affects only the framework-carrier interpretation of this C^8 and downstream physical flavor claims, which the ratified scope excludes. Therefore the abstract theorem can be clean and positive while the carrier/physics reading remains gated.
- **rationale:** Five-judge panel majority 5/5 ratified the second tuple (audited_clean, positive_theorem, class A). Vote breakdown: J1: second / audited_clean / positive_theorem / class A; J2: second / audited_clean / positive_theorem / class A; J3: second / audited_clean / positive_theorem / class A; J4: second / audited_clean / positive_theorem / class A; J5: second / audited_clean / positive_theorem / class A. Majority rationale: The restricted packet cleanly separates the abstract finite-dimensional S_3 representation statement from the open framework-carrier interpretation. For the abstract theorem, the runner constructs the permutation matrices, computes the characters, and applies standard S_3 character multiplicity formulas, so the load-bearing step is class A and the chain closes without the staggered-Dirac gate. The open gate blocks only the taste-cube/physical-flavor reading, not the standalone abstract representation theorem; positive_theorem is therefore the correct claim_type for the narrowed audited scope. | The restricted packet supports the abstract finite-dimensional representation theorem directly by standard S_3 character algebra and by a runner that constructs the permutation matrices and computes the characters and multiplicities. The open staggered-Dirac/taste-cube carrier identification is explicitly excluded from the audited scope, so it should not force the abstract theorem to remain bounded. Reclassification to positive_theorem is correct only for the abstract S_3-on-C^8 statement; any framework-carrier or physical flavor use remains gated. | The restricted packet cleanly proves the abstract finite-dimensional S_3 representation statement by constructing the tensor-position permutation representation, computing its class characters, and applying standard S_3 character theory. The open staggered-Dirac/taste-cube carrier interpretation is explicitly excluded from the audited scope, so it does not force the abstract theorem to remain bounded. The first audit correctly found class A and audited_clean but kept claim_type as bounded_theorem despite the narrowed abstract theorem having no open dependency inside scope. The second audit gives the internally consistent applyable tuple for the targeted reclassification. | The restricted packet cleanly supports the abstract finite-dimensional representation theorem by direct algebraic computation and standard S_3 character theory. The runner constructs the permutation matrices, computes traces, verifies sector decomposition, and contains no external comparator, tuned input, or import of the open staggered-Dirac carrier identification. Because the ratified scope explicitly excludes the framework taste-cube and physical flavor readings, the open staggered-Dirac gate does not force the abstract theorem to remain bounded. | The narrowed audited claim is a finite-dimensional representation-theoretic statement over an explicitly defined S_3 action, and it closes by ordinary character algebra plus the provided runner computation. The open staggered-Dirac realization gate affects only the framework-carrier interpretation of this C^8 and downstream physical flavor claims, which the ratified scope excludes. Therefore the abstract theorem can be clean and positive while the carrier/physics reading remains gated.
- **auditor confidence:** judicial_panel_majority

### `scalar_3plus1_temporal_ratio_note`

- **Note:** [`SCALAR_3PLUS1_TEMPORAL_RATIO_NOTE.md`](../../docs/SCALAR_3PLUS1_TEMPORAL_RATIO_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact evaluation of A_inf/A_2=2/sqrt(3) for the specified minimal APBC 3+1 scalar bridge kernel, excluding observable-level dimension-4 insertion.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-judicial-panel-per-site-k1-20260523T135419Z-scalar_3plus1_temporal_ratio_note-majority`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** From K_sc(omega)=3+sin^2(omega) and A(L_t)=(1/(2L_t)) sum_omega 1/(3+sin^2 omega), A_2=1/8 and A_inf=1/(4sqrt(3)), so A_inf/A_2=2/sqrt(3).  _(class `A`)_
- **chain closes:** True — Five-judge panel majority 5/5 ratified the second tuple (audited_clean, positive_theorem, class A). Vote breakdown: J1: second / audited_clean / positive_theorem / class A; J2: second / audited_clean / positive_theorem / class A; J3: second / audited_clean / positive_theorem / class A; J4: second / audited_clean / positive_theorem / class A; J5: second / audited_clean / positive_theorem / class A. Majority rationale: The closed statement is the endpoint ratio for the specified scalar kernel, and the endpoint values follow by ordinary finite-sum algebra and the standard temporal-average integral. The source note explicitly does not promote the fourth-root dimension-4 factor into a physical observable insertion theorem, so that support-only material does not broaden the audited scope. The runner checks the same algebraic surface and does not use an external comparator or calibrated empirical input. The second audit supplies the current applyable positive_theorem scope while preserving the support boundary. | The clean theorem is the endpoint ratio for the specified scalar bridge kernel, not a claim that the fourth-root factor is physically inserted into a plaquette or other observable. Within that scoped kernel, the endpoint values and ratio are standard algebra/calculus checks, so class A is the right classification. The runner supports this by computing the APBC sums and checking the stated identities, with no external comparator or tuned empirical input. The second audit provides the current-schema claim_type and scope and correctly preserves the observable insertion as support-only. | The applyable tuple should use the second audit because it supplies the required claim_type, scoped theorem statement, runner breakdown, and support-only boundary for the fourth-root observable insertion. Within that restricted scalar-kernel scope, the load-bearing step is an algebraic endpoint evaluation rather than a new physical bridge, external comparator, renaming, or tuned numerical match. The note does not promote the dimension-4 insertion into a specific observable, so that support corollary does not broaden the retained theorem scope. | The closed object is a specified scalar-kernel endpoint calculation, and the endpoint ratio follows by ordinary algebra/calculus once that kernel and APBC temporal averaging are fixed. The source note explicitly keeps the dimension-4 fourth-root insertion at support level, so the clean theorem does not assert closure for a plaquette or other physical observable. The runner computes the APBC frequencies and scalar averages and checks the stated endpoint identities without an external comparator or tuned empirical input. The second audit supplies the current applyable claim_type and scope, so it is the tuple to ratify. | The closed claim is an exact evaluation of a specified scalar bridge kernel, and the endpoint ratio follows by algebraic evaluation of the finite APBC sum and temporal limiting average. The note explicitly does not promote the fourth-root dimension-4 factor to an observable-level theorem, so that support-only material does not broaden the retained scope. The runner performs the same APBC scalar-average checks and contains no external comparator, tuned empirical input, or imported open dependency for the ratio itself.
- **rationale:** Five-judge panel majority 5/5 ratified the second tuple (audited_clean, positive_theorem, class A). Vote breakdown: J1: second / audited_clean / positive_theorem / class A; J2: second / audited_clean / positive_theorem / class A; J3: second / audited_clean / positive_theorem / class A; J4: second / audited_clean / positive_theorem / class A; J5: second / audited_clean / positive_theorem / class A. Majority rationale: The closed statement is the endpoint ratio for the specified scalar kernel, and the endpoint values follow by ordinary finite-sum algebra and the standard temporal-average integral. The source note explicitly does not promote the fourth-root dimension-4 factor into a physical observable insertion theorem, so that support-only material does not broaden the audited scope. The runner checks the same algebraic surface and does not use an external comparator or calibrated empirical input. The second audit supplies the current applyable positive_theorem scope while preserving the support boundary. | The clean theorem is the endpoint ratio for the specified scalar bridge kernel, not a claim that the fourth-root factor is physically inserted into a plaquette or other observable. Within that scoped kernel, the endpoint values and ratio are standard algebra/calculus checks, so class A is the right classification. The runner supports this by computing the APBC sums and checking the stated identities, with no external comparator or tuned empirical input. The second audit provides the current-schema claim_type and scope and correctly preserves the observable insertion as support-only. | The applyable tuple should use the second audit because it supplies the required claim_type, scoped theorem statement, runner breakdown, and support-only boundary for the fourth-root observable insertion. Within that restricted scalar-kernel scope, the load-bearing step is an algebraic endpoint evaluation rather than a new physical bridge, external comparator, renaming, or tuned numerical match. The note does not promote the dimension-4 insertion into a specific observable, so that support corollary does not broaden the retained theorem scope. | The closed object is a specified scalar-kernel endpoint calculation, and the endpoint ratio follows by ordinary algebra/calculus once that kernel and APBC temporal averaging are fixed. The source note explicitly keeps the dimension-4 fourth-root insertion at support level, so the clean theorem does not assert closure for a plaquette or other physical observable. The runner computes the APBC frequencies and scalar averages and checks the stated endpoint identities without an external comparator or tuned empirical input. The second audit supplies the current applyable claim_type and scope, so it is the tuple to ratify. | The closed claim is an exact evaluation of a specified scalar bridge kernel, and the endpoint ratio follows by algebraic evaluation of the finite APBC sum and temporal limiting average. The note explicitly does not promote the fourth-root dimension-4 factor to an observable-level theorem, so that support-only material does not broaden the retained scope. The runner performs the same APBC scalar-average checks and contains no external comparator, tuned empirical input, or imported open dependency for the ratio itself.
- **auditor confidence:** judicial_panel_majority

### `scalar_kg_rerun_note_2026-04-10`

- **Note:** [`SCALAR_KG_RERUN_NOTE_2026-04-10.md`](../../docs/SCALAR_KG_RERUN_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The note records the current scalar-KG rerun state: frontier_scalar_kg_16card_v2.py returns 13/16 with C12-C14 failing, while frontier_scalar_kg_full_suite.py returns 28/38 applicable measures and 20 N/A, so scalar KG is a bounded reference architecture rather than a literal 16/16 axiom-derived closure.  _(class `C`)_
- **chain closes:** True — The note's measured rerun claims close against the current scripts, and its safe interpretation matches the runner outputs.
- **rationale:** The current primary runner reproduces the note's 13/16 result and the named C12-C14 failures, and the secondary full-suite runner reproduces the stated 28/38 applicable score with 20 N/A measures. The note does not promote scalar KG as an axiom-derived theorem; it explicitly frames the lane as a reference architecture/ceiling test and preserves the strict-card failures. Residual risk is limited to the bounded/reference status and the usual runner-output formatting, not the claim boundary being audited.

### `second_grown_family_complex_note`

- **Note:** [`SECOND_GROWN_FAMILY_COMPLEX_NOTE.md`](../../docs/SECOND_GROWN_FAMILY_COMPLEX_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Narrow anchor-row positive: drift=0.20 on the no-restore Gate B grown geometry with geometry-sector stencil satisfies the runner's Born-proxy, weak-field F~M, and TOWARD@0.1 to AWAY@0.5 complex-action gates over the tested seeds.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e12c5-4d99-7bf3-bd38-447aae1f1250`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The probe passed the retained safety gates on the anchor row and showed the expected narrow crossover pattern.  _(class `C`)_
- **chain closes:** True — The cited authority is retained_bounded for the second no-restore geometry-sector family, and the current runner separately computes the complex-action gate outcomes for the anchor row. The source note's safe read is explicitly limited to that anchor row and does not assert family-wide closure.
- **rationale:** The audited claim is operational and narrow: the runner builds the grown geometry slice, applies the geometry-sector stencil, computes propagation/Born-proxy/centroid/probability observables, and gates the anchor-row result without hard-coded target row outputs. The one-hop dependency is retained-grade and supplies only the second-family slice, while the runner supplies the complex-action companion evidence. The note stays within the tested anchor-row boundary and explicitly denies family-wide generalization.
- **auditor confidence:** medium

### `second_grown_family_sign_note`

- **Note:** [`SECOND_GROWN_FAMILY_SIGN_NOTE.md`](../../docs/SECOND_GROWN_FAMILY_SIGN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The audited packet supports that the signed-source fixed-field diagnostics pass on the tested no-restore geometry-sector grown-family slice for the listed drifts and seeds.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260506-024729-44a0cde4-second_grown_family_sign-002`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The sweep passed on all tested rows: drift values 0.0, 0.1, 0.2, 0.3, 0.5 across seeds 0, 1, 2, for 15/15 rows passed.  _(class `C`)_
- **chain closes:** True — The included runner performs an actual parameter sweep, constructs the no-restore family and geometry-sector connectivity, propagates fields for zero, plus, minus, neutral, and double sources, and checks the stated pass criteria. The conclusion is bounded to the tested rows and does not require broader geometry-generic closure.
- **rationale:** The runner is not a print-only artifact and does not hard-code the reported row values; it computes source fields, propagates amplitudes, measures detector centroid shifts, and applies explicit pass criteria. The note's conclusion is narrow and matches the completed runner output: 15/15 tested drift-seed rows pass, with exact zero and neutral baselines and near-linear charge scaling. No cited upstream authority is imported, and no external comparator or tuned observational value is used.
- **auditor confidence:** medium

### `self_consistency_structured_null_note_2026-04-11`

- **Note:** [`SELF_CONSISTENCY_STRUCTURED_NULL_NOTE_2026-04-11.md`](../../docs/SELF_CONSISTENCY_STRUCTURED_NULL_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On the corrected 10x10 periodic staggered torus, iterative backreaction is distinguished from matched static structured nulls, with the cleanest surviving separation in width contraction.  _(class `C`)_
- **chain closes:** True — The registered runner exits 0 and reproduces the note's SelfConsist, StaticInit, ShiftedNull, and PhaseNull sign-margin, width-ratio, boundary-alpha, and sigma-separation values; the source keeps the conclusion fixed-surface and non-universal.
- **rationale:** The bounded structured-null claim closes against scripts/frontier_self_consistency_test.py. Current output matches SelfConsist sign margin +30, width 0.3554, alpha 0.145434; StaticInit +40, 0.3563, 0.159548; ShiftedNull +11, 0.4847, 0.134795; PhaseNull +21.4+/-31.1, 0.4012+/-0.0186, 0.131728+/-0.011976; and the stated width/alpha separations. The note explicitly limits the result to a fixed 10x10 periodic surface and does not claim architecture-wide closure. Plot generation failed locally due missing matplotlib, but the numerical runner output needed for the audit completed.
- **auditor confidence:** high

### `self_gravity_scaling_note_2026-04-10`

- **Note:** [`SELF_GRAVITY_SCALING_NOTE_2026-04-10.md`](../../docs/SELF_GRAVITY_SCALING_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** Across the three prescribed staggered graph families, every reported size case has final width ratio below 1, force 20/20 toward with zero flips, and machine-level norm drift, so the corrected parity-coupled self-gravity probe is a bounded scaling probe rather than a universal contraction claim.  _(class `B`)_
- **chain closes:** True — The runner recomputes the twelve table rows and family summaries in the note: all width ratios are below unity, force stability is 20/20 TW with zero flips, and maximum norm drift stays below 9e-16. The note limits the result to the prescribed admissible graph families and corrected parity coupling, so the bounded claim closes without asserting a derived universal self-gravity law.
- **rationale:** The numerical table and trend claims are current with the runner output. The load-bearing claim is bounded to this exact model sweep: no external comparator or universal contraction theorem is asserted, and the readout explicitly says this is a genuine scaling probe rather than a universal contraction claim. Residual risk is only interpretive use of the phrase self-gravity; within the stated prescribed-coupling model, the audit closes cleanly at bounded tier.
- **auditor confidence:** high

### `seventh_family_diagonal_boundary_note`

- **Note:** [`SEVENTH_FAMILY_DIAGONAL_BOUNDARY_NOTE.md`](../../docs/SEVENTH_FAMILY_DIAGONAL_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the frozen diagonal-stripe seventh-family sweep log verifier for the stated 6 drift by 3 seed grid and its seed-selective boundary interpretation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-190016-ab31de4094-seventh_family_diagonal_boun`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The explicit frozen row grid has seven sign-gate passing rows out of eighteen while exact zero-source and neutral gates survive on every tested row, so the honest read is a seed-selective boundary pocket rather than broad seventh-family closure.  _(class `A`)_
- **chain closes:** True — The restricted packet includes the source note, runner output, primary runner source, and the imported helper used to generate the geometry. The row list independently supports 7 PASS rows, exact zero and neutral cancellation on all 18 rows, and sign-orientation failure on the remaining rows.
- **rationale:** The audited claim is deliberately bounded to the frozen explicit row grid and the boundary-pocket interpretation, not a family-wide theorem. Independently reading the displayed rows gives PASS at drift 0.00 seeds 0,1,2; drift 0.20 seed 2; drift 0.30 seeds 1,2; and drift 0.50 seed 1, totaling 7/18, with zero and neutral entries exactly displayed as +0.000e+00 throughout. The runner source verifies the frozen log by parsing the row grid and checking grid order, stale 6/18 legacy marker, gates, coverage, and boundary text; it does not import a contested external comparator. For this scoped frozen-log consistency claim, the algebraic/table check closes.
- **auditor confidence:** high

### `shapiro_five_family_portability_corrected_boundary_note_2026-06-06`

- **Note:** [`SHAPIRO_FIVE_FAMILY_PORTABILITY_CORRECTED_BOUNDARY_NOTE_2026-06-06.md`](../../docs/SHAPIRO_FIVE_FAMILY_PORTABILITY_CORRECTED_BOUNDARY_NOTE_2026-06-06.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the sampled proxy statement for the three restored grown-family samples plus the named quadrant and radial rows at c={2.0,1.0,0.5,0.25}, with corrected zero-source control and milliradian-scale cross-family spread.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-190114-87a882c3dd-shapiro_five_family_portabil`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The corrected runner gates show zero-source finite-c control below 1e-12, nonzero source-off diagnostics, positive monotone finite-c detector phases as c decreases, and five-family sampled spread below 0.003 rad at each tested c.  _(class `C`)_
- **chain closes:** True — The primary runner constructs the sampled geometries/connectivities and computes the instantaneous and finite-c propagations directly; the included helpers cover the load-bearing quadrant and radial builders. Independent arithmetic checks of the displayed table confirm the asserted spreads and monotonicity, and the s=0 zero-source identity follows from the field term vanishing for both instantaneous and finite-c propagation.
- **rationale:** The claim is explicitly bounded to sampled rows and does not import an external calibration, observational comparator, or family-wide theorem. The runner source is not a print-only or expected-value matcher on the load-bearing path; it computes the phase observable from deterministic lattice samples and included connectivity builders. The four assertion gates in the completed runner output match the source note and support exactly the stated bounded scope.
- **auditor confidence:** high

### `sharp_record_fisher_tangent_space_narrow_theorem_note_2026-06-06`

- **Note:** [`SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md`](../../docs/SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Finite sharp-record probability/Radon-Nikodym/Fisher tangent identities, including the normalized exponential chart and the uniform two-outcome signed-record unit score, with no physical source semantics.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260613-224128-594c8f6299-sharp_record_fisher_tangent_`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Using the path-origin convention P_h|_{h=0}=P_0, R'_0(i)=dp_i/p_i, so s_i=dp_i/p_i and E_0[s^2]=sum_i dp_i^2/p_i; the exponential normalizer W(h)=log E_0 exp(hO) gives origin score O when E_0[O]=0.  _(class `A`)_
- **chain closes:** True — All displayed quantitative identities reduce to finite-sum algebra: normalization gives sum_i dp_i=0, the RN coordinate derivative gives the Fisher quadratic form, W'(0)=E_0[O]=0, and the two-outcome uniform record has mean 0 and second moment 1. No cited authority, primitive, bridge, or external comparator is needed.
- **rationale:** The independent formula inventory checks the RN score identity, Fisher quadratic form, exponential-chart normalization and derivative, and the two-outcome epsilon arithmetic directly from finite probability definitions. The runner source performs symbolic finite-probability checks rather than importing fitted values or hard-coding a contested physical premise. The claim is narrow and explicitly excludes the broader physical source, closure, and Standard Model matching assertions, so the audited theorem closes as standard finite probability geometry.
- **auditor confidence:** high

### `sign_portability_invariant_family_second_grown_derivation_theorem_note_2026-05-09`

- **Note:** [`SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md`](../../docs/SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite cached-output certificate that SIGN_PORTABILITY_INVARIANT_COMPARE reports runner-defined G1/G2/G3/G4 gate passes for the recorded derivation subset, five core family logs, and one holdout family under the stated tolerances.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-fresh-sign-portability-gate-certificate-2026-05-26`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** In logs/runner-cache/SIGN_PORTABILITY_INVARIANT_COMPARE.txt, the runner reports the second-grown gate block PASS, all listed core and holdout families as G1G2G3G4=PPPP, configured thresholds, and OVERALL PASS.  _(class `B`)_
- **chain closes:** True — The narrowed claim follows from the SHA-pinned cached runner output and the inspected runner source: the runner recomputes a two-row second-grown subset and then checks the same thresholds against registered family logs. This closes only the bounded diagnostic/cache certificate, not a unit-slope theorem, row-wise lower-bound theorem, physical sign-law derivation, or cross-family proof.
- **rationale:** The cross-log dependence is load-bearing, so the step is class B rather than a first-principles derivation; however the source note has been narrowed to exactly that finite cached gate-certificate claim. The runner source and cache output support the stated PASS lines and thresholds, and the note explicitly excludes the broader theorem and physical-derivation readings. The decoration heuristic is not controlling here because the note is not an algebraic corollary of a single parent claim; it is a bounded runner diagnostic over recorded artifacts.

### `signed_gravity_interface_kodd_pfaffian_line_bundle_label_narrow_theorem_note_2026-06-12`

- **Note:** [`SIGNED_GRAVITY_INTERFACE_KODD_PFAFFIAN_LINE_BUNDLE_LABEL_NARROW_THEOREM_NOTE_2026-06-12.md`](../../docs/SIGNED_GRAVITY_INTERFACE_KODD_PFAFFIAN_LINE_BUNDLE_LABEL_NARROW_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite dense K_odd staggered-cylinder calculation on the 63-point theta grid 0.05, 0.10, ..., 3.10, pi for the stated 20x30 and 28x44 step/smooth profiles, with relative singular-support cutoff s_j/s_0>0.05 and transported Pfaffian frames.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260613-010727-82f490b1e0-signed_gravity_interface_kod`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Using the relative gap-defined support frame s_j/s_0 > 0.05 and Procrustes frame transport, the measured native K_odd interface carrier has Pf(theta)/Pf(0.05)=+1 for all 63 tested theta points and an empty crossing set.  _(class `C`)_
- **chain closes:** True — The runner source constructs the stated lattice operator, O-real basis, relative support frames, transport alignment, and Pfaffian signs directly, with no helper imports or external comparators. The closure is for the measured finite grids only; it does not prove a continuum-in-theta no-crossing theorem between sampled points.
- **rationale:** The load-bearing result is a first-principles finite computation of the stated matrix family, not a definition substitution or tuned external numerical match. The source code computes the spectra, ranks, transported frames, and Pfaffian signs rather than hard-coding the empty flip set; the hard-coded absolute-cutoff ranks are only a trap-control check and are not used as the label. The displayed main-line and marginal smooth-control numbers are consistent with the executable construction and the stated bounded scope.
- **auditor confidence:** high

### `site_phase_cube_shift_intertwiner_note`

- **Note:** [`SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md`](../../docs/SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Exact intertwining of cube-shift operators on C^8 with lattice site-phase operators restricted to the eight BZ-corner subspace, including the induced Hadamard joint eigensystem.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop:fresh-2026-05-02-site-phase-galileo`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** On the eight BZ-corner basis with Phi|alpha>=|X_alpha>, lattice site phases P_mu act as alpha -> alpha xor e_mu, so Phi^dagger P_mu Phi is the cube-shift S_mu and the joint eigensystem is the Z_2^3 Hadamard character basis.  _(class `A`)_
- **chain closes:** True — The stated result is finite-dimensional algebra on the explicitly restricted eight-corner support. It does not require a physical generation identification or any cited external authority beyond the defined Fourier/character action.
- **rationale:** Issue checked: whether the lattice site-phase operators and abstract cube shifts are exactly intertwined on the restricted BZ-corner support. The runner directly checks the bit-flip law, the isometry, pulled-back operators, and all joint eigenstates with zero reported discrepancies. The note explicitly avoids identifying the support with physical generations, so the scoped theorem closes as exact algebra rather than an unratified physical bridge.
- **auditor confidence:** high

### `sixth_family_sheared_boundary_note`

- **Note:** [`SIXTH_FAMILY_SHEARED_BOUNDARY_NOTE.md`](../../docs/SIXTH_FAMILY_SHEARED_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The sheared-shell sweep shows a narrow basin: exact zero and neutral controls remain clean where measured, but drift=0.50 has no passing rows and several mid-drift rows fail by sign-orientation flip, so the family does not widen into family-wide closure.  _(class `B`)_
- **chain closes:** True — The current SIXTH_FAMILY_SHEARED_SWEEP.py output reports 12/21 passing rows, exact zero and neutral rows throughout, no drift=0.50 passes, and failures driven by plus/minus sign inversion rather than control leakage. This directly supports the note's bounded boundary language.
- **rationale:** The note is a bounded boundary diagnosis and its material claims match the current sweep. It does not overclaim family-wide closure: it identifies the drift=0.50 sign-flip edge and preserves the narrower basin read. Residual risk is only that the ledger row has no primary runner attached; scripts/SIXTH_FAMILY_SHEARED_SWEEP.py is the matching evidence surface.
- **auditor confidence:** high

### `sixth_family_sheared_fm_transfer_note`

- **Note:** [`SIXTH_FAMILY_SHEARED_FM_TRANSFER_NOTE.md`](../../docs/SIXTH_FAMILY_SHEARED_FM_TRANSFER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On the sixth-family sheared-shell rows that pass the exact zero/neutral/sign gate, the sweep reports mean weak-field exponent 0.999895 across drift coverage 0.0 through 0.3, so F~M-style transfer survives only on the basin rows.  _(class `B`)_
- **chain closes:** True — The current SIXTH_FAMILY_SHEARED_SWEEP.py output reports 12/21 passing rows with drift coverage [0.0, 0.05, 0.1, 0.15, 0.2, 0.3] and mean exponent 0.999895. That is exactly the note's bounded weak-field transfer claim, with no family-wide closure implied.
- **rationale:** The note's narrow weak-field transfer statement is current with the sweep output. It limits the claim to rows that already pass the exact gates and does not claim universal connectivity behavior. Residual risk is only the missing ledger runner attachment; the local sweep script is the direct evidence surface.
- **auditor confidence:** high

### `sixth_family_sheared_note`

- **Note:** [`SIXTH_FAMILY_SHEARED_NOTE.md`](../../docs/SIXTH_FAMILY_SHEARED_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The parity-sheared shell sweep passes 12/21 sampled rows, with exact zero-source and neutral controls, sign orientation on the passing subset, drift coverage [0.0, 0.05, 0.1, 0.15, 0.2, 0.3], and mean exponent 0.999895, so the construction is a narrow sixth-family basin rather than a generic theorem.  _(class `B`)_
- **chain closes:** True — SIXTH_FAMILY_SHEARED_SWEEP.py currently reproduces the note's pass count, drift coverage, exact zero/neutral controls, and mean weak-field exponent. The note's conclusion is bounded and selective, matching the data rather than claiming family-wide closure.
- **rationale:** The sheared basin note closes at bounded tier: the runner verifies the exact pass/fail structure and the note states the correct narrow interpretation. It neither expands the result into a universal connectivity theorem nor hides the failed rows. Residual risk is only missing ledger runner attachment; the local sweep script is the direct evidence surface.
- **auditor confidence:** high

### `source_driven_field_recovery_h025_pocket_note`

- **Note:** [`SOURCE_DRIVEN_FIELD_RECOVERY_H025_POCKET_NOTE.md`](../../docs/SOURCE_DRIVEN_FIELD_RECOVERY_H025_POCKET_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The refinement step preserves exact zero-source reduction, the dynamic pocket keeps all rows TOWARD, and the dynamic mass exponent stays essentially linear.  _(class `C`)_
- **chain closes:** True — For the declared exact lattice, source-driven field rule, calibration target, and source strengths, the runner recomputes the frozen zero-source check, table, and fitted exponents exactly. There are no cited dependencies or external comparator claims to import.
- **rationale:** The source note makes a narrow bounded numerical claim, not a retained physical bridge: refinement to h=0.25 preserves zero-source reduction, positive deflection sign, and near-linear dynamic mass scaling under the declared parameters. The runner output matches the frozen table and exposes the same amplitude limitation, with mean dynamic/instantaneous ratio 0.055. Residual risk is that this remains calibration- and architecture-specific, but that limitation is explicitly inside the claim boundary.
- **auditor confidence:** high

### `source_field_static_law_classification_bounded_note_2026-07-08`

- **Note:** [`SOURCE_FIELD_STATIC_LAW_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md`](../../docs/SOURCE_FIELD_STATIC_LAW_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Exact zero-mode, mean-subtracted pseudoinverse, and lattice screening identities for the declared nearest-neighbor periodic operator, plus the stated finite-lattice numerical checks.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-20260710-131002-abb23e4d-source_field_static_law_-005`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** For the symbol λ(k)=sum_i 2(1-cos(k_i)), every term is nonnegative and all terms vanish only at k=0, yielding the unique constant zero mode and the mean-zero solvability condition.  _(class `A`)_
- **chain closes:** True — The structural conclusions follow algebraically from the fully specified Fourier symbol. The runner constructs that symbol, performs the FFT inversions and finite-volume comparisons, and reproduces all five reported checks without importing or hard-coding a contested result.
- **rationale:** The theorem is correctly bounded to a declared operator class and makes no uniqueness or physical-field identification. Its exact claims follow from elementary Fourier algebra, while the supplied runner genuinely computes the finite-lattice residuals, Green-function profiles, and screened decay fits. The output agrees with the note, and no open authority or external calibrated input is load-bearing.
- **auditor confidence:** high

### `source_measure_pcal_cumulant_mobius_theorem_note_2026-05-30`

- **Note:** [`SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md`](../../docs/SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For a finite sharp-record moment generator M[J], connected source responses defined by partition-lattice Mobius cumulants are generated by K[J] = log M[J], with p-scaling fixed to p = 1 under unit connected two-point normalization.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260531-134249-e9ea9f06-source_measure_pcal_cumu`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The standard exponential formula for set partitions says that the generating function for connected components is the logarithm: K[J] = log M[J].  _(class `A`)_
- **chain closes:** True — The Mobius cumulant formula, the log moment-generating function identity, the n=3 cumulant formula, independence cancellation, and the p-scale two-point normalization all close algebraically. The downstream physical identification of the scalar P-cal response with connected source response is explicitly outside this scoped theorem.
- **rationale:** The load-bearing step is a standard algebraic Mobius/exponential-formula identity, not a numerical fit, external comparator, or symbol renaming. The runner source materially computes the partition-lattice n=3 Mobius formula, verifies independence cancellation, differentiates log moment generators, and checks the p-scale normalization; it does not import a contested constant or hidden comparator. The displayed closed-form formulas in the packet are consistent under the note's finite-record cumulant conventions. The clean verdict applies only to the bounded exact-support theorem, not to unbounded retained Y_T closure or the physical connected-response identification.
- **auditor confidence:** high

### `source_resolved_exact_green_scaling_note`

- **Note:** [`SOURCE_RESOLVED_EXACT_GREEN_SCALING_NOTE.md`](../../docs/SOURCE_RESOLVED_EXACT_GREEN_SCALING_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fixed-parameter finite-lattice replay of the stated source-resolved Green kernel on the h=0.5, W=3, L=24 exact lattice, including zero-source reduction, TOWARD rows, linear source-strength scaling, and reported Green/instantaneous ratios.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260517-144003-bc2044d8-source_resolved_exact_gr-002`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** For the fixed h=0.5, W=3, L=24 source-resolved Green-kernel configuration, the runner computes zero-source shift +0.000000e+00, four positive Green deflections, F~M exponent 1.01, and mean |green/inst| = 1.111.  _(class `C`)_
- **chain closes:** True — The primary runner and included helper build the lattice, fields, propagation, centroid readout, ratios, and power fits from the stated constants; the reported values are computed rather than hard-coded. The closure is limited to the stated finite lattice, kernel, calibration target, source cluster, and readout.
- **rationale:** The runner source is substantive: it constructs the finite lattice, computes the source-resolved Green-like field, propagates amplitudes, and derives the centroid shifts and fitted exponents without importing prior note outputs or asserting the table constants. The cached stdout matches the note's frozen readout, including exact zero-source reduction and all four TOWARD rows. This clean verdict applies only to the bounded fixed-configuration computation, not to a full self-consistent field theory or generated-geometry transfer.
- **auditor confidence:** high

### `source_resolved_exact_green_self_consistent_note`

- **Note:** [`SOURCE_RESOLVED_EXACT_GREEN_SELF_CONSISTENT_NOTE.md`](../../docs/SOURCE_RESOLVED_EXACT_GREEN_SELF_CONSISTENT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the declared h=0.25 compact lattice, clipped cross5 source cluster, fixed Green-like kernel, calibrated gain, and one source-weight update, the runner-backed pocket reproduces the frozen numerical table, zero-source reduction, TOWARD sign, and near-linear source scaling.
- **audit_status:** ~~audited_numerical_match~~
- **effective_status:** ~~audited_numerical_match~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-source_resolved_exact_green_self_consistent_note-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The frozen pocket uses the selected compact lattice, boundary-clipped source cluster, Green-like kernel, calibrated gain input, and one self-consistency update to reproduce the stated table, TOWARD sign, zero-source reduction, and linear scaling.  _(class `G`)_
- **chain closes:** True — The included runner and helper compute the bounded finite-lattice update and reproduce all six stated checks. Closure is only within the declared calibrated setup; the gain, normalization, source geometry, and fully converged dynamics are not derived.
- **rationale:** Issue: the load-bearing result depends on the hard-coded calibrated gain and fixed compact setup, with frozen table values used as regression targets. Why this blocks: the packet supports a calibrated finite numerical pocket, not an independently derived amplitude or full self-consistent field theorem. Repair target: derive the gain and normalization from retained dynamics and replace the one-update pocket with a converged self-consistent dynamics theorem. Claim boundary until fixed: the stated table and hard gates hold for the declared calibrated setup only.
- **auditor confidence:** high

### `source_resolved_generated_architecture_bridge_note`

- **Note:** [`SOURCE_RESOLVED_GENERATED_ARCHITECTURE_BRIDGE_NOTE.md`](../../docs/SOURCE_RESOLVED_GENERATED_ARCHITECTURE_BRIDGE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** Support recovery plus a causal parent-averaged field is better, but the weak-field mass law improves without fully closing.  _(class `C`)_
- **chain closes:** True — The registered runner exits 0 and reproduces the note's exact zero-source, TOWARD-count, N_eff, and fitted-exponent table; the source note keeps the result bounded and does not claim generated-family closure.
- **rationale:** The bounded bridge claim closes against the current runner. scripts/source_resolved_generated_architecture_bridge.py reproduces baseline/static 4/16 TOWARD, F~M=0.199, N_eff=2.69; baseline/causal 3/16, -0.308, 2.50; tweak/static 9/16, -0.316, 5.31; and tweak/causal 9/16, 0.444, 5.67, with all zero-source shifts at 0. The note's limitation that the weak-field mass law does not cleanly close is explicit, so the clean audit only certifies the bounded bridge result.
- **auditor confidence:** high

### `source_resolved_generated_discriminator_probe_note`

- **Note:** [`SOURCE_RESOLVED_GENERATED_DISCRIMINATOR_PROBE_NOTE.md`](../../docs/SOURCE_RESOLVED_GENERATED_DISCRIMINATOR_PROBE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The support-rescue static Green variant beats the wavefield bridge on both sign count and detector effective support, giving delta_TOWARD = -3, delta_N_eff = -0.18, and a geometry-limited bottleneck label.  _(class `C`)_
- **chain closes:** True — The runner recomputes the exact summary stated in the note over seeds 0..3 and the retained source ladder. The note keeps the result bounded as a discriminator rather than claiming generated-family closure.
- **rationale:** The current runner output matches the frozen note: both variants have zero-source shift 0, support rescue gives 9/16 TOWARD with N_eff 5.31, wavefield gives 6/16 with N_eff 5.14, and the derived discriminator is delta_TOWARD=-3, delta_N_eff=-0.18, bottleneck=geometry-limited. The claim boundary is narrow and explicit: this is a generated-family bottleneck discriminator, not a closure theorem. Residual risk is limited to the chosen compact family, seeds, kNN-floor bridge, and two bridge variants.
- **auditor confidence:** high

### `source_resolved_generated_new_family_note`

- **Note:** [`SOURCE_RESOLVED_GENERATED_NEW_FAMILY_NOTE.md`](../../docs/SOURCE_RESOLVED_GENERATED_NEW_FAMILY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The split-shell generated family widens detector support relative to the compact bridge and modestly improves the wavefield fit, but it still does not restore a clean weak-field linear class.  _(class `C`)_
- **chain closes:** True — The runner reproduces the note's aggregate table and geometry deltas for the bridge and split-shell families over seeds 0..3. The note explicitly keeps the result as a bounded bridge reopening rather than a generated-family closure theorem.
- **rationale:** The current runner output matches the frozen result: zero-source shifts are 0, bridge/static is 9/16 with F~M=-0.316 and N_eff=5.31, bridge/wavefield is 6/16 with F~M=0.098 and N_eff=5.14, split/static is 9/16 with F~M=0.304 and N_eff=8.38, and split/wavefield is 8/16 with F~M=0.381 and N_eff=8.30. The derived geometry deltas also match. The claim boundary is correctly bounded: the new geometry is a real support-widening bridge, not weak-field closure.
- **auditor confidence:** high

### `source_resolved_generated_support_recovery_note`

- **Note:** [`SOURCE_RESOLVED_GENERATED_SUPPORT_RECOVERY_NOTE.md`](../../docs/SOURCE_RESOLVED_GENERATED_SUPPORT_RECOVERY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The kNN-floor connectivity tweak broadens detector support and moves the aggregated centroid sign from AWAY to TOWARD, but the detector distribution remains localized enough that this is only partial recovery.  _(class `C`)_
- **chain closes:** True — The runner reproduces the note's zero-source checks, detector support table, and sign counts for the declared compact generated family and kNN-floor tweak. The note keeps the claim bounded and does not promote it to generated-family transfer closure.
- **rationale:** The current runner output matches all frozen values: baseline shift -4.357340e-02 with N_eff 2.77, support fraction 0.311, peak share 0.234, and 1/4 TOWARD; kNN floor shift +3.850909e-01 with N_eff 6.00, support fraction 0.458, peak share 0.439, and 3/4 TOWARD. The note's limitation is explicit: support and sign improve, but localization remains strong. Residual risk is limited to the single source strength and compact generated-family tweak under test.
- **auditor confidence:** high

### `source_resolved_generated_wavefield_bridge_note`

- **Note:** [`SOURCE_RESOLVED_GENERATED_WAVEFIELD_BRIDGE_NOTE.md`](../../docs/SOURCE_RESOLVED_GENERATED_WAVEFIELD_BRIDGE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The wavefield update is distinguishable from static and causal smoothing, but on the compact generated family it remains a bridge result rather than stable weak-field transfer or closure.  _(class `C`)_
- **chain closes:** True — The artifact-chain runner reproduces every frozen summary row and wavefield-vs-static gain in the note. The source note explicitly keeps the result bounded and does not claim generated-family closure.
- **rationale:** The current script output matches the note: zero-source reduction is 0 across rows, baseline/static is 4/16 with F~M=0.199 and N_eff=2.69, baseline/causal is 3/16 with F~M=-0.308 and N_eff=2.50, baseline/wavefield is 0/16 with F~M=0.655 and N_eff=2.53, tweak/static is 9/16 with F~M=-0.316 and N_eff=5.31, tweak/causal is 9/16 with F~M=0.444 and N_eff=5.67, and tweak/wavefield is 6/16 with F~M=0.098 and N_eff=5.14. The wavefield-vs-static deltas also match and are negative for aggregate centroid gain. Residual risk is that the ledger runner_path is unset even though the note's artifact chain names the script; the audit result is clean for the bounded claim as written, not for metadata completeness or closure.
- **auditor confidence:** high

### `source_resolved_geometry_rule_repair_note`

- **Note:** [`SOURCE_RESOLVED_GEOMETRY_RULE_REPAIR_NOTE.md`](../../docs/SOURCE_RESOLVED_GEOMETRY_RULE_REPAIR_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The finite seeds 0..3 comparison of the stated kNN-floor baseline against the claimed additive adaptive-sector-fan repair under the fixed static Green-kernel fixture.
- **audit_status:** ~~audited_failed~~
- **effective_status:** ~~audited_failed~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00441-source_resolved_geometry_rul`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** The repair changes the aggregate result from 7/16 TOWARD, N_eff=5.06, and alpha=0.058 to 8/16 TOWARD, N_eff=2.80, and alpha=0.335, so it is a mixed partial improvement rather than the intended support-broadening repair.  _(class `C`)_
- **chain closes:** False — The reported arithmetic is reproduced by genuine computation, but the runner tests a different geometry transformation from the one stated. `_augment_sector_repair` constructs a fresh sector/floor adjacency list and assigns `adj[src] = selected`, discarding baseline edges not reselected instead of adding the sector fan to the retained kNN-floor bridge.
- **rationale:** The cached values agree with the runner's computation, including zero shifts, sign counts, exponents, and support metrics. However, the source note's candidate is the retained kNN-floor bridge plus an adaptive sector fan, while the implementation replaces each source's adjacency with a newly selected sector/floor list. Consequently, the numerical result cannot establish the bounded claim for the geometry repair actually described.
- **auditor confidence:** high

### `source_resolved_retarded_green_corrected_packet_note_2026-05-29`

- **Note:** [`SOURCE_RESOLVED_RETARDED_GREEN_CORRECTED_PACKET_NOTE_2026-05-29.md`](../../docs/SOURCE_RESOLVED_RETARDED_GREEN_CORRECTED_PACKET_NOTE_2026-05-29.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the fixed h=0.25 finite-lag source-resolved Green pocket with the stated source cluster, source strengths, same-site memory control, and retarded-like update; no full retarded field equation or support-fraction broadening claim is covered.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260601-205010-1b419cfb-source_resolved_retarded`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The corrected live runner directly computes same-site and finite-lag retarded-like centroid shifts on the fixed h=0.25 source-resolved lattice pocket and finds retarded-like shift larger than same-site memory for all four source strengths, with mean ret/same about 1.026.  _(class `C`)_
- **chain closes:** True — The primary runner and included helpers construct the lattice, fields, propagation, centroid shifts, support metrics, ratios, and exponents directly from code-path computations rather than importing a prior note value or external comparator. The corrected ret/same ratio is computed from ret and same values in the primary runner, so the old helper-main ret/inst label drift is not load-bearing.
- **rationale:** The supplied runner source genuinely computes the bounded lattice pocket quantities and asserts the finite claims reported in the source note. The quantitative readout is consistent with the displayed rows: ret/same averages to about 1.026, ret-same is positive in all four rows, zero-source fields reduce to free propagation, and the fitted responses are near linear. No cited non-retained authority, external calibrated value, hard-coded contested numerical result, or definition-only substitution is used for the load-bearing step.
- **auditor confidence:** high

### `source_resolved_retarded_green_pocket_note`

- **Note:** [`SOURCE_RESOLVED_RETARDED_GREEN_POCKET_NOTE.md`](../../docs/SOURCE_RESOLVED_RETARDED_GREEN_POCKET_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fixed-parameter finite-lag source-resolved Green pocket on the h=0.25, W=3, L=6 exact lattice for the four listed source strengths.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-141800-d9ffea2b8d-source_resolved_retarded_gre`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the compact exact h=0.25, W=3, L=6 lattice with the fixed source cluster and strengths 0.001, 0.002, 0.004, 0.008, the retarded-like finite-lag rule has zero-source reductions, TOWARD retarded rows, approximately linear source-strength exponents, positive ret-same, true ret/same about 1.026, unchanged support fraction, and slightly increased detector N_eff.  _(class `C`)_
- **chain closes:** True — The primary runner and included helper instantiate the lattice, source cluster, Green fields, same-site memory field, finite-lag retarded-like field, propagation, centroid shifts, and support metrics without importing contested output values. Independent arithmetic from the displayed table confirms the ret/same ratios, ret-same signs, ret/inst ratios, and fitted exponents within the stated rounded bounds.
- **rationale:** The source claim is narrowly bounded to a fixed compact lattice and fixed update rule, and the runner source genuinely computes the stated quantities rather than printing or matching hard-coded expected rows. The cached stdout is consistent with the runner assertions, and table-level independent checks reproduce ret/same near 1.026, positive ret-same values, and source-strength exponents approximately equal to one. The note does not claim continuum behavior, a full retarded field equation, or support-fraction broadening, so the conclusion follows within the stated bounded scope.
- **auditor confidence:** high

### `source_resolved_support_localization_split_note`

- **Note:** [`SOURCE_RESOLVED_SUPPORT_LOCALIZATION_SPLIT_NOTE.md`](../../docs/SOURCE_RESOLVED_SUPPORT_LOCALIZATION_SPLIT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** Treat this as a real mechanistic split: exact support is broad and stable under the clipping control, generated support is sharply localized, and the retained Green/self-consistent pocket likely depends on broad downstream connectivity support that the generated family does not provide.  _(class `C`)_
- **chain closes:** True — The runner directly compares exact clipped, exact centered, and generated-family self-consistent Green cases using detector support metrics, and its current output matches the frozen table. The bounded mechanistic split closes because the exact controls have nearly identical broad support while the generated mean is sharply localized.
- **rationale:** The note makes a bounded mechanism-discriminator claim rather than a full causal theorem. The current runner recomputes the exact clipped/interior controls and generated-family mean, matching the frozen centroid, N_eff, N_eff/N_det, top-10 fraction, 1% support, and peak-share values. Residual risk is that this identifies consistency with detector/connectivity localization rather than proving it as the only causal mechanism, and the note states that limitation.
- **auditor confidence:** high

### `source_resolved_transverse_green_corrected_boundary_note_2026-05-29`

- **Note:** [`SOURCE_RESOLVED_TRANSVERSE_GREEN_CORRECTED_BOUNDARY_NOTE_2026-05-29.md`](../../docs/SOURCE_RESOLVED_TRANSVERSE_GREEN_CORRECTED_BOUNDARY_NOTE_2026-05-29.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Corrected finite boundary facts for the fixed h=0.25 source-resolved transverse Green runner; no positive same-site centroid correction, support-fraction broadening, full field equation, generated-family transfer, or physical gravitational closure is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260601-205652-b4c2f0c5-source_resolved_transver`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the fixed h=0.25 lattice pocket, the corrected runner finds mean trans/inst about 1.162, corrected mean trans/same about 0.990, negative trans-same centroid shift in every row, unchanged support fraction, slight N_eff broadening, linear exponents, and 4/4 TOWARD rows.  _(class `C`)_
- **chain closes:** True — The primary runner and included helpers build the fixed lattice fields, propagate amplitudes, compute centroid/support/N_eff observables, and assert the listed finite bounds. No cited authority or external comparator is imported, and the quantitative note claims match the completed runner output and independent arithmetic checks on the displayed table.
- **rationale:** The runner source genuinely computes the finite rows from lattice propagation, Green fields, same-site memory, and transverse smoothing rather than printing constants or reading a contested premise. The displayed ratios, means, signs, support deltas, N_eff mean, and near-unit exponents are consistent with the runner cache and independent arithmetic over the table. The source note keeps the conclusion bounded to the finite corrected boundary packet and explicitly blocks the stale positive same-site correction headline.
- **auditor confidence:** high

### `source_resolved_wavefield_v2_note`

- **Note:** [`SOURCE_RESOLVED_WAVEFIELD_V2_NOTE.md`](../../docs/SOURCE_RESOLVED_WAVEFIELD_V2_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-lattice numerical claim that scripts/source_resolved_wavefield_v2.py, on the stated h=0.25, W=4, L=8 source family and five source strengths, produces exact zero-source same-site and wavefield reduction, positive wavefield deflections for all five rows, near-unit centroid mass-scaling exponents, and near-unit detector phase-ramp slope/span exponents.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-fresh-second-source_resolved_wavefield_v2_note-20260505`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The Frozen Result reports zero-source same-site and wavefield shifts of +0.000000e+00, positive wavefield deflections for s=0.0005 through 0.0080, and fitted exponents 1.00, 1.00, 0.99, 1.02, and 1.01 for instantaneous, same-site, wavefield, phase-ramp slope, and phase-ramp span scaling.  _(class `C`)_
- **chain closes:** True — The fresh cached run for runner SHA bb0f86c1bca9d547eba476212a3c43bd39192823a69c7919705c5a48a65bbebe exits 0 and its stdout matches the note's reductions, row table, TOWARD count, and fitted exponents. The visible runner computes the finite-lattice fields, propagation, centroid shifts, phase-ramp metrics, and power fits rather than printing the frozen table as constants; this closes only the bounded runner-output claim.
- **rationale:** The scoped claim is exactly the finite computation printed by the current cache: both zero-source shifts are zero, all five wavefield centroid shifts are positive, and the fitted exponents are near unity for the centroid and detector phase-ramp observables. No external comparator, continuum limit, generated-geometry transfer, or experimental-amplitude bridge is needed for this bounded scope. The clean verdict should not be read as validating any broader continuum or physical-source theorem beyond the stated finite runner family.
- **auditor confidence:** high

### `spectral_closure_2026-04-09`

- **Note:** [`SPECTRAL_CLOSURE_2026-04-09.md`](../../docs/SPECTRAL_CLOSURE_2026-04-09.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** Broadband attraction does not survive under any source-defined spectral control; detector-equalization is a post-hoc artifact rather than a physical source spectrum.  _(class `C`)_
- **chain closes:** True — The primary retained-lattice runner and the explicitly named spectral-control runners compute the raw, Lorentzian, detector-equalized, and source-side weighting cases. Their current outputs support the bounded conclusion that broad/flat source-defined spectra remain AWAY and only detector-output reweighting flips selected comparisons.
- **rationale:** The note is clean as a bounded negative for broadband attraction under the tested source-defined spectral controls. The current artifacts reproduce the stated pattern: raw broad/flat spectra are AWAY, source-coupled and source-equalized controls do not rescue broadband TOWARD, and detector-equalized TOWARD behavior is explicitly framed as an output-dependent diagnostic rather than a source model. Residual risk is that this does not rule out a later physical k-selection mechanism, but the note lists that as open work.
- **auditor confidence:** medium

### `stable_post_record_dial_location_certificate_2026-06-06`

- **Note:** [`STABLE_POST_RECORD_DIAL_LOCATION_CERTIFICATE_2026-06-06.md`](../../docs/STABLE_POST_RECORD_DIAL_LOCATION_CERTIFICATE_2026-06-06.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Given the supplied two-atom target u, affine reset map Phi_alpha, and generation dial formulas, s=0/r=1/2/Q=2/3 is a stable equal-letter fixed-point location; no dial-selection, Koide, or physical-value theorem was audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260606-203801-d2b527cad9-stable_post_record_dial_loca`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Phi_alpha(p)-u=(1-alpha)(p-u), so for 0<alpha<1 the supplied equal-letter target u=(1/2,1/2) is a stationary attracting fixed point, and substituting s=0 in the supplied dial gives r=1/2 and Q=2/3.  _(class `A`)_
- **chain closes:** True — The affine contraction identity follows by direct subtraction, and 0<alpha<1 gives attraction. Substitution into pi_s, r(s), and Q(s) gives (1/2,1/2), 1/2, and 2/3 at s=0, with the table's s=1 entries also checking algebraically.
- **rationale:** The audited claim is deliberately bounded to stability under a supplied affine reset map and a supplied dial parametrization, not selection of that map or a physical dial value. Independent algebra confirms the contraction, stationarity, and displayed dial substitutions without using the runner implementation path. The runner contains many documentation and sibling-note string checks, but the source note's load-bearing mathematical claim closes from the displayed definitions and standard algebra.
- **auditor confidence:** high

### `staggered_backreaction_capture_closure_note`

- **Note:** [`STAGGERED_BACKREACTION_CAPTURE_CLOSURE_NOTE.md`](../../docs/STAGGERED_BACKREACTION_CAPTURE_CLOSURE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the fixed current runner closure lap_selfmix50_capture3o2 on two cycle-bearing graphs and one layered holdout, the audited facts are the stated battery scores and approximately twofold force-gap reductions, not near-capture or full self-gravity closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-142750-7881c49679-staggered_backreaction_captu`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The current capture-closure harness preserves both cycle-bearing 9/9 batteries and improves the cycle and holdout force gaps by about a factor of two.  _(class `C`)_
- **chain closes:** True — The primary runner and included helpers compute source densities, graph Poisson fields, Crank-Nicolson evolutions, shell forces, external-control gaps, and summary ratios from fixed runner definitions rather than importing or printing the note's asserted numbers. Independent arithmetic checks give 0.9828/0.4734 = 2.076 and 0.9191/0.4559 = 2.016, matching the stated 2.08x and 2.02x.
- **rationale:** The load-bearing claim is bounded to the current finite runner output, and the runner source performs the closure computation rather than hard-coding the source-note numbers. The closure loop updates gain from capture and does not use the external-kernel force in the load-bearing closure path; the external kernel is used afterward as the fixed gap control. The source note's boundary language correctly excludes the archived near-capture and full self-gravity claims.
- **auditor confidence:** high

### `staggered_backreaction_iterative_note`

- **Note:** [`STAGGERED_BACKREACTION_ITERATIVE_NOTE.md`](../../docs/STAGGERED_BACKREACTION_ITERATIVE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite current-runner scan of linear Laplacian-sharpened and inverse-heat source mappings for the included staggered backreaction graph families.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-143242-cf81418aca-staggered_backreaction_itera`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The best current map is `invheat_b3p00`, with best cycle-bearing mean gap `4.314e-01`, improvement factor `2.23x`, and best-map self-gap mean `1.581e+01` while TOWARD and norm-stability remain intact.  _(class `C`)_
- **chain closes:** True — The primary runner and helper source actually construct the graph families, apply the source maps, solve the screened graph Poisson field, evolve the Hamiltonian, and compute the force/self-gap diagnostics rather than printing hard-coded asserted values. The closure is only for the finite implemented scan, not for a general no-closure theorem over all possible maps.
- **rationale:** The note is scoped to the current finite runner and explicitly says this is not a closure theorem. The runner source has no load-bearing import of a contested premise or hard-coded expected result; it computes the quantities from the specified graph/source/field/evolution pipeline. Independent arithmetic on the displayed `invheat_b3p00` rows gives cycle-bearing mean gap `4.314e-01`, self-gap mean `1.581e+01`, and improvement factor about `2.23x`, matching the asserted facts. No cited support/open authority is imported.
- **auditor confidence:** high

### `staggered_backreaction_live_capture_packet_note_2026-05-29`

- **Note:** [`STAGGERED_BACKREACTION_LIVE_CAPTURE_PACKET_NOTE_2026-05-29.md`](../../docs/STAGGERED_BACKREACTION_LIVE_CAPTURE_PACKET_NOTE_2026-05-29.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite bounded comparison on the current staggered capture-closure runner for the hard-coded lap_selfmix50_capture3o2 closure on two cycle-bearing graph families and one layered holdout.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-190925-f2097ecfa4-staggered_backreaction_live_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner imports the current capture-closure harness and asserts that both cycle-bearing batteries score 9/9 while the cycle and layered holdout gaps improve by about 2x with the zero-source, TOWARD, linearity, additivity, and norm guardrails surviving.  _(class `C`)_
- **chain closes:** True — The primary runner calls the exposed helper chain to build the graphs, solve the screened graph Poisson field, evolve the staggered Hamiltonian, and compute the reported force/gap/readout quantities rather than printing fixed expected values. Independent arithmetic on the displayed output checks the mean R2, cycle gap ratio, and holdout gap ratio within the stated precision.
- **rationale:** Within the stated bounded scope, the load-bearing result is a first-principles finite computation over the supplied runner definitions and transitive helper sources. The helper chain contains real graph construction, Laplacian/Poisson solves, Hamiltonian evolution, force readout, closure iteration, and guardrail checks; the contested summary values are not hard-coded as expected outputs. The external-kernel row is an internally defined finite comparator for gap characterization, not an empirical PDG/lattice/observation import, and the note explicitly disclaims physical or continuum closure.
- **auditor confidence:** high

### `staggered_backreaction_nonlocal_closure_note`

- **Note:** [`STAGGERED_BACKREACTION_NONLOCAL_CLOSURE_NOTE.md`](../../docs/STAGGERED_BACKREACTION_NONLOCAL_CLOSURE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For the provided current runner and fixed graph/control battery, alpha=0.40 reduces the calibrated cycle-bearing force gap from 3.881e-02 to 1.620e-02 while the stated diagnostics remain bounded and the layered/spectral readouts remain poor.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-143534-e6acaaa908-staggered_backreaction_nonlo`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The fractional-Green source sector improves the calibrated cycle-bearing rows at alpha=0.40 while preserving TOWARD, linearity, additivity, and norm checks, with poor layered holdout and low-mode bias remaining.  _(class `C`)_
- **chain closes:** True — The primary and helper runner sources compute the graph Laplacian, fractional Green field, CN evolution, force readout, gain sweep, and diagnostics rather than printing constants. Independent arithmetic from the displayed table checks the load-bearing numbers, including the cycle-gap means and 2.40x ratio.
- **rationale:** The runner source genuinely computes the finite current-runner quantities from included framework code, with no cited open authority or hard-coded contested value. The displayed output supports the bounded claim: the best cycle-bearing calibrated gap occurs at alpha=0.40, the preservation diagnostics remain within the stated tolerances, and the layered holdout plus shell-fit readouts remain non-closing. The note explicitly disclaims a nonlocal closure theorem, so the audited scope is limited to the finite runner result.
- **auditor confidence:** high

### `staggered_backreaction_note`

- **Note:** [`STAGGERED_BACKREACTION_NOTE.md`](../../docs/STAGGERED_BACKREACTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite three-family staggered backreaction prototype readout only: bipartite random geometric n=36, bipartite growing n=48, and layered bipartite DAG-compatible n=36 under the named runner parameters; verifies exact zero-source reduction, source-response table, two-body additivity, TOWARD force signs, one-step endogenous TOWARD response, and norm stability, excluding lattice-size stability sweep and self-gravity closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the three listed retained graph families, the source-generated screened-Poisson Phi run has exact zero-source reduction, R^2 >= 0.983 source response, machine-precision two-body additivity, TOWARD force on all families, one-step endogenous TOWARD response, and norm drift at machine precision.  _(class `C`)_
- **chain closes:** True — The named prototype runner recomputes the same three-family table shown in the source note and cache. The audited scope is narrowed to that finite numerical readout and explicitly excludes the broader required-control language about modest lattice-size stability and any claim that backreaction/self-gravity is solved.
- **rationale:** The bounded numerical readout closes because the live runner reproduces the fixed table: zero-source reduction is exact for 3/3 families, source-response R^2 is at least 0.983, two-body residuals are machine precision, force and one-step self-force are TOWARD in every family, and norm drift is machine-scale. The note's broader controls are not silently promoted: no modest lattice-size sweep, full self-gravity closure, cosmology, Hawking, or replacement of the retained staggered card is included in the audited scope. Residual risk is therefore only the narrow finite-prototype scope and the absence of an assertion wrapper, not a missing computation for the scoped table.
- **auditor confidence:** high

### `staggered_backreaction_results_2026-04-10`

- **Note:** [`STAGGERED_BACKREACTION_RESULTS_2026-04-10.md`](../../docs/STAGGERED_BACKREACTION_RESULTS_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Fixed-runner bounded prototype facts for the three generated graph families: zero-source force/norm, Poisson-source additivity, solved/source force sign, one-step self-sourced force sign, and reported force/self-update gaps.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-143840-d5de8ded62-staggered_backreaction_resul`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The live prototype supports zero-source reduction, two-body additivity, TOWARD force sign, and one-step endogenous TOWARD behavior across the three tested graph families as certified by the current runner cache.  _(class `C`)_
- **chain closes:** True — The primary runner constructs the three graph families with fixed seeds, solves the screened graph Poisson system, evolves the state, and computes the reported signs, residuals, gaps, and summary counts rather than reading them from another note or printing constants. The conclusion closes only for this current-runner prototype packet and not for self-gravity closure or external-kernel scale agreement.
- **rationale:** The cache values quoted in the note match the completed runner output, and the runner source performs genuine finite numerical computation of the Poisson solve, Crank-Nicolson evolution, shell force, additivity residuals, and self-update force. Zero-source reduction and Poisson additivity also follow structurally from the zero-density branch and linear screened Poisson solve. The large force-scale gaps and failed all-family linearity are explicitly retained as boundaries, so the audited claim does not overstate those results. No cited upstream authority or external comparator is used.
- **auditor confidence:** high

### `staggered_backreaction_shell_spectral_note`

- **Note:** [`STAGGERED_BACKREACTION_SHELL_SPECTRAL_NOTE.md`](../../docs/STAGGERED_BACKREACTION_SHELL_SPECTRAL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite n=36 shell/spectral diagnostic for the bipartite_random_geometric and layered_bipartite_dag families: phi_solved is flatter than phi_ext with shell span ratios 0.123 and 0.229 and solved/external low-mode fractions 0.958/0.453 and 0.809/0.355; stale force columns are not part of the retained scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The force-scale gap is a structural over-smoothing of the source-to-field map: rho is localized, phi_solved is smoother and more low-mode dominated, phi_ext stays steeper in depth, and force remains positive but too weak.  _(class `C`)_
- **chain closes:** True — The runner constructs the two graph families, source density, screened graph-Poisson solve, external-kernel field, shell profiles, and Laplacian spectra directly, and its live output reproduces the audited shell-span and low-mode diagnostics. The chain closes only as a finite diagnostic of these two fixed families, not as a general endogenous-gravity closure theorem.
- **rationale:** The load-bearing structural diagnosis is computed rather than defined: the live runner reproduces the shell span ratios 0.123 and 0.229 and the solved/external low-mode fractions 0.958/0.453 and 0.809/0.355 from the stated graph families. The source note's force readouts are stale against live output, but the note explicitly quarantines those columns as non-load-bearing finite-snapshot values, and the qualitative positive-but-too-weak force direction remains. Residual risk is limited to future runner drift or treating this bounded diagnostic as a universal source-to-field theorem.
- **auditor confidence:** high

### `staggered_dag_note_2026-04-10`

- **Note:** [`STAGGERED_DAG_NOTE_2026-04-10.md`](../../docs/STAGGERED_DAG_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The staggered force-first lane is not confined to periodic cubic lattices; it survives a narrow layered acyclic template with forward-depth bias, machine-clean norm/Born, and stable inward proxy response under the prescribed attractive sign, even though the live transport operator is still symmetrized rather than truly directed.  _(class `C`)_
- **chain closes:** True — The runner directly evaluates the three layered DAG-derived configurations and reproduces the load-bearing 6/6 score surface, TOWARD forces, N-stability, Born linearity, forward-depth fraction, and state-family robustness. The small norm-row roundoff difference remains at machine precision and does not affect the bounded compatibility claim.
- **rationale:** The source note is narrowly framed as a compatibility control, not a proof of truly directed DAG Hamiltonian transport. The current runner gives 6/6 on all three configurations, with TOWARD force, 14/14 N-stability, machine-clean norm/Born behavior, forward-depth fraction 0.1266, and 3/3 state families. Residual risk is limited to the symmetrized-adjacency scope boundary, which the note states explicitly.
- **auditor confidence:** high

### `staggered_fermion_card_2026-04-10`

- **Note:** [`STAGGERED_FERMION_CARD_2026-04-10.md`](../../docs/STAGGERED_FERMION_CARD_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite repo-local reproduction of the force-based staggered-fermion 17-card at mass=0.3, g=50.0, S=5e-4, dt=0.15 for 1D n=61 and 3D n=9/11/13, including the explicit C17 4/6-family qualifier for 3D n>9.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-staggered-fermion-card`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The current retained harness reproduces the force-based staggered card surface: 1D n=61 and 3D n=9/11/13 all score 17/17, with the documented n>9 C17 family-coverage gate.  _(class `C`)_
- **chain closes:** True — The source note scopes the result to the force-based card and states the weaker row semantics and family-coverage caveats. The repo-local runner completed and reproduced the stated 17/17 outputs without external imports or stale numerical mismatch.
- **rationale:** The load-bearing claim is bounded to a fixed finite runner and operating point, not a repo-wide centroid-gravity claim or a universal physical theorem. The runner computes the card rows and reproduces the note's listed values for 1D n=61 and 3D n=9/11/13, including the documented C17 limitation at n=11 and n=13. Residual risk is scope leakage: this clean verdict should not be read as validating centroid-based card semantics, dynamic/cosmological extensions, or full six-family 3D coverage above n=9.
- **auditor confidence:** high

### `staggered_geometry_superposition_note_2026-04-11`

- **Note:** [`STAGGERED_GEOMETRY_SUPERPOSITION_NOTE_2026-04-11.md`](../../docs/STAGGERED_GEOMETRY_SUPERPOSITION_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** For a fixed periodic 2D staggered lattice, comparing the flat branch against the screened-field branch gives detector-resolved coherent-vs-mixture differences at the documented operating points while leaving topology/adjacency fixed.  _(class `C`)_
- **chain closes:** True — The registered harness recomputes the phase, branch overlap, detector probabilities, total variation distances, and coherent-vs-mixture detector TVq for the stated 1D and 2D cases, and the current output matches the note's frozen table within the claim's bounded scope.
- **rationale:** The note is explicitly bounded to a fixed periodic lattice with no topology superposition and only claims detector-resolved interference between flat and screened-field branches. The registered runner recomputes the load-bearing observables rather than relying on a prose assertion, and its current output matches every frozen row in the note. Residual risk is limited to the model's stated toy-lattice assumptions and not to stale numerics or an unregistered runner.
- **auditor confidence:** high

### `staggered_graph_failure_map_note`

- **Note:** [`STAGGERED_GRAPH_FAILURE_MAP_NOTE.md`](../../docs/STAGGERED_GRAPH_FAILURE_MAP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audit of the stated adversarial graph failure classification for the staggered graph lane using the cited portability note and the provided failure-map runner output/source.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-staggered_graph_failure_-054`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Odd-cycle defects and parity wrap inconsistencies are structural breaks, while dense shortcuts and high-degree contamination are graceful degradations as long as the retained force battery stays intact.  _(class `B`)_
- **chain closes:** True — The cited portability note is retained and supplies the retained force-battery baseline. The provided runner constructs the adversarial graph cases, measures the portability battery through the upstream runner, detects same-color/parity defects and graph irregularity metrics, and classifies the cases according to the note's stated boundary-map rule.
- **rationale:** The claim is not a first-principles physics derivation; it is a bounded computational boundary-map claim over a retained upstream battery. The runner source does more than print constants: it constructs modified graph families, computes defect counts, long-edge fraction, max degree, retained-battery pass counts, force observables, and gauge status, then classifies the cases. The upstream authority is retained, and no open or non-retained dependency is present in the restricted packet.
- **auditor confidence:** medium

### `staggered_graph_gauge_closure_note`

- **Note:** [`STAGGERED_GRAPH_GAUGE_CLOSURE_NOTE.md`](../../docs/STAGGERED_GRAPH_GAUGE_CLOSURE_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited whether the provided gauge-closure runner computes a native flux-threaded persistent-current response on cycle-bearing staggered graph families and reports periodic closure without 1D helpers or proxy rows.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-gpt55-xhigh-019e0584-7515-7f02-97fa-a42166b11c33`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The closure condition is that a cycle-bearing family shows nontrivial current span under threaded flux and periodic closure at phi=0 and phi=2pi, with the runner selecting the best geometry/operator/observable from that frozen run.  _(class `C`)_
- **chain closes:** True — The cited portability authority is retained, and the included runner constructs flux-threaded Hamiltonians, diagonalizes them, computes ground-state current spans and endpoint residuals, and reports multiple cycle-bearing PASS cases. No missing bridge is apparent within the restricted packet for this scoped native graph-current closure probe.
- **rationale:** The load-bearing computation is not a hard-coded numerical match: the runner builds a flux-threaded Hamiltonian for each graph, diagonalizes it over phi in [0, 2pi], and computes current span and periodic residual from the ground-state vector. The retained upstream portability note supplies the staggered transport law and prior retained side battery, and the current observable is separately scored on cycle-bearing graphs while acyclic graphs are N/A. One cycle-bearing layered stress case fails, but the note's stated closure criterion only requires a cycle-bearing family with nontrivial span and periodic closure, which the frozen runner output provides.
- **auditor confidence:** medium

### `staggered_graph_gauge_closure_results_2026-04-10`

- **Note:** [`STAGGERED_GRAPH_GAUGE_CLOSURE_RESULTS_2026-04-10.md`](../../docs/STAGGERED_GRAPH_GAUGE_CLOSURE_RESULTS_2026-04-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The frozen runner computes native flux-threaded persistent-current closure for the listed staggered graph stress/layered families, with stress cycles passing and one layered cycle failing.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-audit-loop-gpt55-xhigh-019e0587-81ae-7c12-97ed-89a8438a168a`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Native gauge/current closes on the cycle-bearing stress families because the flux-threaded staggered Hamiltonian yields nontrivial ground-state persistent-current span with periodic residual below threshold.  _(class `C`)_
- **chain closes:** True — The cited gauge note supplies the closure criterion and the retained portability note supplies the staggered transport context; the runner then constructs flux-threaded Hamiltonians and computes current spans/residuals for the frozen graph families. The note's qualitative closure claim matches the completed runner despite minor stale table numerics.
- **rationale:** The load-bearing result is not a mere definition or upstream restatement: the runner computes eigensystems of flux-threaded native staggered Hamiltonians and derives current spans/residuals not present as input constants. Both cited authorities are retained, and the source note explicitly includes the operator, observable, closure rule, positive stress-family results, DAG N/A handling, and the negative layered-cycle case. The table values are slightly stale relative to stdout, but the pass/fail pattern, best family, operator, and observable are unchanged.
- **auditor confidence:** medium

### `staggered_graph_portability_note`

- **Note:** [`STAGGERED_GRAPH_PORTABILITY_NOTE.md`](../../docs/STAGGERED_GRAPH_PORTABILITY_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The provided runner computes the stated battery on three fixed finite bipartite graph families with the stated parity-coupled scalar potential and reports passing rows.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-040942-beec6e04-staggered_graph_portabil-251`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The retained staggered force battery survives on all three graph families.  _(class `C`)_
- **chain closes:** True — The runner constructs the graphs, Hamiltonian, probe states, force observable, robustness checks, and cycle-gauge response directly rather than printing constants or importing prior note values. Within this narrow fixed-run portability scope, the reported conclusion follows from the included runner output and source.
- **rationale:** The load-bearing claim is a narrow computational portability statement, not a broad universal graph theorem. The runner source performs actual finite-graph calculations and the cached output matches the note's table, including skipped gauge scoring for the cycle-free DAG-compatible family. No cited upstream authority is present, but the restricted packet includes the concrete computational construction needed for this checkpoint. The clean verdict is limited to the three fixed graph families and parameter choices in the runner.
- **auditor confidence:** medium

### `staggered_graph_portability_stress_note`

- **Note:** [`STAGGERED_GRAPH_PORTABILITY_STRESS_NOTE.md`](../../docs/STAGGERED_GRAPH_PORTABILITY_STRESS_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The cached stress runner supports pass/N/A survival of the retained staggered force battery on the four named larger bipartite stress graph families.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-staggered_graph_portabil-055`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The retained staggered force battery survives the larger, more irregular bipartite families, with gauge response on cycle-bearing stress families and no retained-row failures.  _(class `C`)_
- **chain closes:** True — The cached runner output reports no retained-row failures across the four stress families, and the sole cited authority is retained and supplies the baseline portability battery. The chain closes for the pass/fail stress-survival claim, not for treating the stress note as a new canonical card.
- **rationale:** The runner constructs the four stress graph families, checks their graph statistics and cycle status, and delegates measurement to the retained portability battery rather than merely printing constants. All retained rows pass or are correctly N/A for the acyclic gauge case, with no external comparator or tuned calibrated input used. The source note's gauge magnitudes differ slightly in low-order digits from cached stdout, so cache/table synchronization should be rechecked, but the audited pass/fail conclusion is unchanged.
- **auditor confidence:** medium

### `staggered_layered_backreaction_note`

- **Note:** [`STAGGERED_LAYERED_BACKREACTION_NOTE.md`](../../docs/STAGGERED_LAYERED_BACKREACTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded numerical bridge: for layered_bipartite_dag_s13_n36 and layered_bipartite_dag_s29_n55 under the stated screened-Poisson point-source runner, the retained observable F=-<dPhi/dd> passes zero-source, source-on, linearity, residual, norm, and robustness checks, while not claiming gauge closure or self-gravity closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-Newton-019deb2e-c7d6-74b2-ab93-fe2468cde9ac`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** On the two named layered graph families, solving screened-Poisson Phi on the same graph gives exact zero-source force, TOWARD source-on force, R^2 > 0.99 source-linearity, machine-small residual/norm drift, and robustness 3/3, with gauge closure only N/A/FAIL as caveated.  _(class `C`)_
- **chain closes:** True — The runner output directly supplies the metrics asserted in the note, and the note's blockers exclude the unresolved gauge/current and fully endogenous density-fed backreaction claims from scope.
- **rationale:** The audited claim is narrow and matches the runner output: two fixed graph families, a screened-Poisson point-source Phi, and force-based retained metrics. The runner has no assertion wrapper, but it computes and reports the load-bearing quantities, all of which satisfy the thresholds stated in the note. Claim boundary: this does not audit a self-gravity closure, evolving density-fed source sector, larger-family persistence, or gauge/current closure.
- **auditor confidence:** high

### `staggered_layered_gauge_engineering_note`

- **Note:** [`STAGGERED_LAYERED_GAUGE_ENGINEERING_NOTE.md`](../../docs/STAGGERED_LAYERED_GAUGE_ENGINEERING_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The restricted packet audits whether the provided runner constructs layered brickwall cycle geometries and computes a native flux-threaded staggered-Hamiltonian current span above threshold while retaining the staggered force battery.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-staggered_layered_gauge_-046`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The engineered layered plaquette geometries close the native gauge/current probe cleanly.  _(class `C`)_
- **chain closes:** True — The cited portability authority is retained, and the runner source builds new layered brickwall graphs, threads flux through detected cycle edges, diagonalizes the Hamiltonian, and computes current spans and residuals rather than printing constants. The completed runner output supports PASS results for both engineered brickwall geometries.
- **rationale:** The load-bearing result is a numerical first-principles computation inside the provided staggered graph harness: the runner constructs the geometries, detects cycle edges, applies flux in the Hamiltonian, diagonalizes it, and measures persistent-current span. The upstream portability note is explicitly retained in the packet, and no external comparator or calibrated input value is used. The note table has small numerical drift from the cached runner output for the sparse holdout and brickwall rows, but the pass/fail pattern and conclusion are unchanged.
- **auditor confidence:** medium

### `staggered_layered_gauge_phase_diagram_note`

- **Note:** [`STAGGERED_LAYERED_GAUGE_PHASE_DIAGRAM_NOTE.md`](../../docs/STAGGERED_LAYERED_GAUGE_PHASE_DIAGRAM_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** On the fixed layered graph sweep implemented by scripts/frontier_staggered_layered_gauge_phase_diagram.py, the current runner computes 15 gauge-current PASS rows, 10 FAIL rows, and 1 N/A row, with nearest-neighbor brickwall and defect step-1 cases passing, step-2 cases failing throughout, step-3 cases mixed, the sparse holdout failing, and the acyclic DAG control marked N/A.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-20260505`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The practical pass/fail boundary is PASS for nearest-neighbor layered brickwall/plaquette graphs, FAIL for the sparse layered holdout and most long-shift layered loop geometries, and N/A for acyclic layered DAG controls.  _(class `C`)_
- **chain closes:** True — Both one-hop dependencies are retained positive staggered graph and layered-gauge engineering probes. The runner builds the swept layered graph families, computes the native staggered Hamiltonian persistent-current span, reuses the retained force-side battery, and prints the pass/fail/N/A phase diagram directly.
- **rationale:** The current cached output supports the bounded phase-diagram classification: PASS=15, FAIL=10, N/A=1, with the same nearest-neighbor brickwall, long-shift, sparse-holdout, defect, and acyclic-control boundary described by the note. Several row-level J-span numerals in the source table have drifted from the current cache, so the clean claim is the current runner's pass/fail/N/A boundary and qualitative geometry criterion, not those stale exact span values. No external comparator or unretained bridge is needed for that finite graph sweep.
- **auditor confidence:** high

### `staggered_layered_loop_threshold_note`

- **Note:** [`STAGGERED_LAYERED_LOOP_THRESHOLD_NOTE.md`](../../docs/STAGGERED_LAYERED_LOOP_THRESHOLD_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded computational threshold result for the specified seed=13, layers=8, width=5 layered construction and six one-plaquette adjacent-layer windows, with stated gauge thresholds and structural guardrails.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-Mill-019deb31-42b9-7981-98c6-cf2c2bbb9b79`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** Within the seed=13 layered family, adding exactly one local K2,2 plaquette to the two-rail corridor makes all six tested loop windows retain 8/8 force rows and pass strict native gauge/current closure while controls do not.  _(class `C`)_
- **chain closes:** True — The runner output directly reports the retained rows, force signs, gauge spans/residuals, cycle status, and structural guardrails needed for the bounded claim. The claim closes only as a bounded harness result, not as a universal minimality theorem over all nearby layered graph geometries.
- **rationale:** The load-bearing bounded comparison is checked explicitly by the runner output: the DAG and no-loop controls have gauge=N/A, the sparse-cycle control has gauge=FAIL, and all six single-plaquette cases have retained=8/8 with J_span above 1e-4 and residual below 1e-8. The source note's qualitative decision is supported under the stated harness constraints. Claim boundary: the result is only for the seeded layered construction and tested plaquette windows; the note should not be read as proving global minimality across all possible nearby graph edits. Minor stale numeric discrepancies exist between the note table and runner output for some J values, but they do not change any pass/fail or threshold conclusion.
- **auditor confidence:** high

### `staggered_newton_blocking_sensitivity_note_2026-04-11`

- **Note:** [`STAGGERED_NEWTON_BLOCKING_SENSITIVITY_NOTE_2026-04-11.md`](../../docs/STAGGERED_NEWTON_BLOCKING_SENSITIVITY_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-run blocking-sensitivity result for open 3D cubic staggered external-source trajectories with sides 12, 14, 16; distances 3-6; mass 0.30; G 50.0; source_strength 5e-4; dt 0.10; N_steps 12; sigma 1.30; and readouts raw, z2, cube2, cube4.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260519-141901-30b1a9aa-staggered_newton_blockin-028`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the open-cubic external-source staggered surface, the Newton-compatible exponent survives raw, z2, and 2x2x2 trajectory readouts and fails only under over-coarse 4x4x4 blocking.  _(class `C`)_
- **chain closes:** True — The provided runner directly instantiates the open staggered 3D lattice Hamiltonian, external source potential, Gaussian packet, Crank-Nicolson evolution, blocked z-centroid readouts, acceleration fits, and distance-law fits. Its computed stdout matches the note's numerical claims within the stated bounded finite surface.
- **rationale:** The load-bearing result is not imported from another note or asserted by definition; it is computed by the included runner from the specified lattice dynamics and readout definitions. The runner source contains no helper imports, no hard-coded expected fitted exponents, and no external comparator calibration. The conclusion is clean only in the bounded finite-surface sense stated by the note, not as a general staggered two-body or asymptotic law.
- **auditor confidence:** high

### `staggered_newton_reproduction_note_2026-04-11`

- **Note:** [`STAGGERED_NEWTON_REPRODUCTION_NOTE_2026-04-11.md`](../../docs/STAGGERED_NEWTON_REPRODUCTION_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Open 3D staggered cubic lattices with sides 12, 14, and 16, imposed external V~-1/r source, mass 0.30, sigma 1.30, d=3..6, dt 0.10, 12 steps, and 2x2x2 blocked-centroid trajectory readout.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260506-024729-44a0cde4-staggered_newton_reprodu-004`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The computed 2x2x2 blocked-centroid acceleration follows an approximately inverse-square distance law on the audited d=3..6 surface, with per-side exponents near -2 and global exponent -1.982.  _(class `C`)_
- **chain closes:** True — The included runner builds the stated staggered Hamiltonian, potential, free and gravitating evolutions, raw and blocked centroids, and distance-law fits; its cached output matches the note. The closure is bounded to the stated external source, open boundaries, calibration window, and blocked observable.
- **rationale:** The runner is not a print-only or hard-coded numerical-match artifact: it computes the finite staggered-lattice evolution and fitted blocked-trajectory exponent from the stated operators and parameters. The note's load-bearing numerical claims match the completed runner output. The result is clean only as a bounded finite-surface computation; it does not establish self-consistent two-body closure, both-masses scaling, irregular-graph transfer, or a general staggered trajectory theorem.
- **auditor confidence:** high

### `staggered_only_det_positivity_case_a_note_2026-05-17`

- **Note:** [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](../../docs/STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For a balanced even staggered lattice with canonical anti-Hermitian M_KS off-diagonal under ε and real m>0, det(M_KS+mI)=∏(m²+σ_i²)>0 for every SU(3) link configuration.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T190702Z-758351f8-staggered_only_det_posit-01`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Equation (16) and (18): det(M)=∏_{i=1}^{n/2}(m²+σ_i²)>0 after the det(γ₅)=(-1)^{n/2} sign cancels the sign in det(γ₅M).  _(class `A`)_
- **chain closes:** True — Given the stated off-diagonal anti-Hermitian block form M_KS=[[0,K],[-K†,0]] with equal ε-sublattice dimensions, the SVD of K reduces γ₅M to independent 2x2 blocks. The determinant sign from γ₅ is explicitly counted and cancels, leaving a strictly positive product because m>0 and σ_i²≥0.
- **rationale:** The proof is a genuine closed-form algebraic determinant factorization over the stated staggered block decomposition, not a renaming or numerical fit. The runner source actually constructs finite canonical staggered SU(3) operators and recomputes the block structure, γ₅-Hermiticity, sign reconciliation, and positivity scan; it does not hard-code the contested determinant value or import an opaque helper. The finite runner is only supporting evidence; the audit verdict rests on the exact SVD/block determinant argument.
- **auditor confidence:** high

### `staggered_scalar_parity_lapse_coupling_external_narrow_theorem_note_2026-05-16`

- **Note:** [`STAGGERED_SCALAR_PARITY_LAPSE_COUPLING_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`](../../docs/STAGGERED_SCALAR_PARITY_LAPSE_COUPLING_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded algebraic certificate for the displayed staggered parity, identity, and lapse operator forms on finite sites/rational test profiles; excludes external literature correctness, uniqueness, framework derivation, continuum/GR consequences, and gate closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-fresh-staggered-scalar-parity-lapse-2026-05-26`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Given the displayed definitions of epsilon(x), P, I, and L, the note claims only the resulting finite algebraic identities and distinctions, including P-I = Phi(x)(epsilon(x)-1) and Hermiticity of sqrt(N) H_flat sqrt(N) for real diagonal sqrt(N).  _(class `A`)_
- **chain closes:** True — Within the narrowed scope, the conclusions follow from the stated definitions and elementary finite algebra. The missing external authority/derivation bridge is explicitly outside the audited claim rather than a hidden premise.
- **rationale:** The source note has successfully narrowed the claim to an if-given-these-operator-forms algebraic certificate. This is not a definition-only external bridge claim, because the audited conclusion is not that P or L is forced or externally correct, but that the displayed forms have the stated algebraic consequences. It is not decoration under the policy because there is no single retained parent claim being expanded into corollaries; the row is self-contained bounded algebra rather than a boxed corollary cluster.

### `staggered_test_mass_companion_note_2026-04-11`

- **Note:** [`STAGGERED_TEST_MASS_COMPANION_NOTE_2026-04-11.md`](../../docs/STAGGERED_TEST_MASS_COMPANION_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On the primary open-cubic staggered architecture, a weak-field static-source companion gives exact source-mass scaling in the force observable and near-linear source-mass scaling in the blocked-envelope trajectory observable, across a bounded side-and-separation surface.  _(class `C`)_
- **chain closes:** True — The runner directly computes the static source packet, normalized test packet, source-only Poisson field, exact inward force, and blocked-envelope acceleration. Its current output reproduces the load-bearing 45/45 inward rows, source-mass exponent tables, representative rows, and max weak-field phi_peak bound.
- **rationale:** The note is explicit that this is a bounded source-only test-mass lane, not both-masses or self-consistent mass-law closure. The current runner reproduces the exact-force source-mass exponent range 1.0000..1.0001, blocked-accel exponent range 1.0093..1.0197, 45/45 inward force rows, 45/45 inward blocked-accel rows, and the representative values used in the note. Residual risk is limited to the bounded open-cubic static-source surface and to a stale non-load-bearing lower phi_peak range bound; the max weak-field bound remains current.
- **auditor confidence:** high

### `structured_mirror_bornsafe_scan_note`

- **Note:** [`STRUCTURED_MIRROR_BORNSAFE_SCAN_NOTE.md`](../../docs/STRUCTURED_MIRROR_BORNSAFE_SCAN_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Whether the registered 32-configuration sliced runner establishes that its tested structured-mirror configurations fail the corrected three-slit Born threshold.
- **audit_status:** ~~audited_failed~~
- **effective_status:** ~~audited_failed~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260711T170149Z-ee259212-00296-structured_mirror_bornsafe_s`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** On the registered 32-config sliced runner, no structured-mirror configuration reaches the corrected Born-safety threshold of 1e-14.  _(class `C`)_
- **chain closes:** False — The runner computes a seven-term inclusion-exclusion statistic without the required empty-slit probability. Because the graph connects each layer to the preceding two layers, paths can bypass the barrier, so the omitted background term can generate the reported nonzero values even under strictly linear propagation.
- **rationale:** Issue: `sorkin_born` evaluates P(ABC)-P(AB)-P(AC)-P(BC)+P(A)+P(B)+P(C) but omits -P(empty), despite the structured-mirror graph permitting paths that skip the barrier layer. Why this blocks: the computed residual is therefore not the corrected third-order Born interference statistic claimed by the note, and may simply measure bypass-background probability. Repair target: compute and subtract the all-barrier-nodes-blocked probability, or eliminate barrier-bypassing edges, then rerun the complete registered slice while requiring valid results for all six seeds. Claim boundary until fixed: the runner establishes only that its current seven-term statistic exceeds 1e-14 on the valid sampled runs.
- **auditor confidence:** high

### `structured_mirror_reconciliation_note`

- **Note:** [`STRUCTURED_MIRROR_RECONCILIATION_NOTE.md`](../../docs/STRUCTURED_MIRROR_RECONCILIATION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded claim that structured-growth mirror geometry is not Born-clean under the retained canonical linear threshold-slit/mass-field harness for the N=25,30,40 comparison shown by the runner.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-019e0d6a-7153-7a83-9582-477f8ac79cec`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The dedicated runner compares canonical threshold-slit/mass-field and alternate top-K/flat-field harnesses and finds the canonical structured-growth Born ratio remains O(1e-1), so the earlier 8e-17 clean result is a harness discrepancy rather than a canonical structured-growth result.  _(class `C`)_
- **chain closes:** True — The runner source constructs the structured-growth geometry, propagates amplitudes, computes Sorkin |I3|/P ratios under four harness choices, and the completed stdout reports canonical values about 7.8e-2 to 1.0e-1. That closes the bounded negative conclusion that the canonical structured-growth lane is not machine Born-clean within the audited scope.
- **rationale:** The load-bearing issue is whether the claimed clean structured-growth Born number survives the canonical harness. The provided runner does not merely print constants; it builds graphs, selects slits, applies field choices, propagates amplitudes, and computes the Born ratios, with canonical outputs remaining O(1e-1). This supports the bounded claim that structured-growth is not Born-clean on the canonical linear validator. Claim boundary: this audit does not independently ratify contextual statements about the exact 2D mirror lane or unprovided structured-growth implementation internals.
- **auditor confidence:** medium

### `structureless_dag_gravity_harness_note`

- **Note:** [`STRUCTURELESS_DAG_GRAVITY_HARNESS_NOTE.md`](../../docs/STRUCTURELESS_DAG_GRAVITY_HARNESS_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On this bounded random-causal-DAG pocket, valley-linear propagation produces TOWARD shifts in the majority of seeds, and the TOWARD rows retain approximately linear mass scaling (F~M ~= 1.0).  _(class `C`)_
- **chain closes:** True — The matching harness script constructs the random causal DAG pocket, source/mass/detector roles, valley-linear propagator, and seed sweep directly, and a fresh run reproduces the note's 28/32, 21/32, combined 49/64, F~M ~= 1.00, R^2 ~= 1.000, and no-field zero readouts. The note's stated boundary is narrow and does not claim graph universality.
- **rationale:** The load-bearing bounded result is reproduced by the current harness for both tested sizes and the note states the correct caveats: sign is seed-sensitive, the 1000-node unstable pocket is excluded, and no graph-universality theorem is claimed. The only residual process risk is that the ledger has no registered runner path even though scripts/structureless_dag_gravity_harness.py exists and matches the note.
- **auditor confidence:** high

### `structureless_dag_gravity_note`

- **Note:** [`STRUCTURELESS_DAG_GRAVITY_NOTE.md`](../../docs/STRUCTURELESS_DAG_GRAVITY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded random x-ordered 3D DAG harness at n=200 and n=500, radius 0.35, strengths [0.001, 0.002, 0.005, 0.01]: TOWARD rows occur in a majority of tested rows and positive-shift rows have seed-local F~M near 1.0.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-Descartes-019deb34-7d52-7bc1-9c06-e10e85086337`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The safe read is that structureless causal DAGs can show TOWARD rows, and when they do the source-strength response stays close to linear on this pocket.  _(class `C`)_
- **chain closes:** True — The runner directly constructs the stated random DAG pocket, propagates with the stated valley-linear field and kernel, and reports the TOWARD counts, local power-law fits, and no-field controls. No external dependency or graph-universality claim is needed for the narrowed harness-level statement.
- **rationale:** The bounded claim closes as a direct numerical harness result: n=200 gives 28/32 TOWARD rows and n=500 gives 21/32 TOWARD rows, with F~M median 1.00 and zero no-field controls in both reported sizes. The source note's n=500 table value is stale relative to current runner output, but this does not change the load-bearing majority-TOWARD and near-linear positive-row conclusion. Exact-count citation should use the current runner values until the note table is refreshed.
- **auditor confidence:** high

### `symmetry_generated_paired_chokepoint_note`

- **Note:** [`SYMMETRY_GENERATED_PAIRED_CHOKEPOINT_NOTE.md`](../../docs/SYMMETRY_GENERATED_PAIRED_CHOKEPOINT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** At the density optimum, the generated paired scaffold is still Born-clean where it runs and recovers a modest subset of the mirror gap at N=25 and N=40, but it loses retention by N=60.  _(class `C`)_
- **chain closes:** True — Running the registered script with the note's density-optimum parameters reproduces the saved log and the note's key table: paired-generated noise values have Born=0 where they run at N=25/40 and all paired-generated N=60 rows fail. The note keeps the conclusion bounded and does not promote the generated scaffold.
- **rationale:** The load-bearing bounded negative conclusion matches the current runner when invoked with the note's explicit density-optimum parameters and is consistent with the archived log. The note states the correct boundary: the generated scaffold has a small viable pocket, does not consistently beat exact mirror, and does not survive to N=60. Residual process risk is that the runner defaults now run a different all-FAIL window, so future readers need the note/log command rather than the default invocation.
- **auditor confidence:** high

### `symmetry_spectrum_mirror_compare_note`

- **Note:** [`SYMMETRY_SPECTRUM_MIRROR_COMPARE_NOTE.md`](../../docs/SYMMETRY_SPECTRUM_MIRROR_COMPARE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** Mirror symmetry can produce a genuine near-rank-2 signature, but only in the strict chokepoint pocket and only at small N; outside that pocket, the rank story is heuristic rather than a retained large-N mechanism.  _(class `C`)_
- **chain closes:** True — Running the registered script with the note's stated N=15,25 and 16-seed setup reproduces the table: original mirror has lower s2/s1 than random-2layer at both sizes, while mirror-chokepoint has high s2/s1, effective rank near 2, and Born zero at machine precision in the small-N pocket.
- **rationale:** The current runner reproduces the note's diagnostic table under the stated setup, and the note's conclusion stays bounded: support exists for a strict small-N mirror-chokepoint rank signature, not for a scalable large-N rank-protected architecture. The default runner window tests larger N and is not the note's quoted table, but it reinforces the same non-scalability boundary rather than contradicting the bounded claim.
- **auditor confidence:** high

### `taste_scalar_isotropy_theorem_note`

- **Note:** [`TASTE_SCALAR_ISOTROPY_THEOREM_NOTE.md`](../../docs/TASTE_SCALAR_ISOTROPY_THEOREM_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** For H(phi)=sum_i phi_i S_i on C^8 with three commuting sigma_x taste-shift involutions and V_f(phi)=sum_s f(lambda_s(phi)^2) for a common smooth f, the fermion Coleman-Weinberg Hessian at phi=(v,0,0) is proportional to delta_ij; bounded gauge-split and thermal-cubic estimates are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-fresh-second-taste_scalar_isotropy_theorem_note-20260505`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The Hessian therefore reduces to the binary orthogonality sum sum_s (-1)^{s_i} (-1)^{s_j}, which is 8 for i=j and 0 for i!=j.  _(class `A`)_
- **chain closes:** True — The simultaneous eigenvalue formula lambda_s(phi)=sum_i phi_i (-1)^{s_i} gives, by the chain rule, a common coefficient 2 f'(v^2)+4 v^2 f''(v^2) multiplying (-1)^{s_i}(-1)^{s_j} at phi=(v,0,0). Summing over the eight binary signs gives a Hessian proportional to delta_ij with no dependency or bounded companion estimate needed.
- **rationale:** The proposed positive_theorem type is correct for the scoped exact Hessian-isotropy statement. The source note's proof sketch compresses the derivative step, but the displayed eigenvalue formula plus standard chain rule make the Hessian coefficient common across all sign sectors at the axis, leaving exactly the binary orthogonality identity. The cached runner output for SHA 519c1d8d830ea43f8cdcd866565184a4d2d1c8d4c9b0318557fe22df5f35c59b reports THEOREM PASS=30 and FAIL=0, checking the shift algebra, eigenvalue sign sum, binary orthogonality, and finite-difference Hessian isotropy for representative smooth functions. The six bounded gauge/thermal passes are outside this audited scope and are not used for closure.
- **auditor confidence:** high

### `teleportation_3d_operator_consistent_end_to_end_note`

- **Note:** [`TELEPORTATION_3D_OPERATOR_CONSISTENT_END_TO_END_NOTE.md`](../../docs/TELEPORTATION_3D_OPERATOR_CONSISTENT_END_TO_END_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite 3D side=2, mass=0, G=1000 Poisson resource under the retained-last-taste-axis convention and ideal retained-logical Bell/feed-forward operations; the framed Psi+->Phi+ row reaches Bell*=0.997724 and F_avg=0.998483 while raw xi_5 controls reject and no-signaling/causal-record guards pass.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-Carson-019deb43-dd0e-7a20-85e3-2f9141cbbd29`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The default 3D positive Poisson case lands in the Psi+ Bell frame, and a known Bob-side retained logical X frame followed by standard retained-axis Z^z X^x feed-forward maps the resource to Phi+ and passes.  _(class `C`)_
- **chain closes:** True — The scoped conclusion follows from the supplied runner output: retained-axis Z/X factorization passes, raw xi_5 controls fail as intended, null and fixed-Phi+ controls do not pass, and the non-null framed row passes all acceptance gates. Closure is bounded to the stated finite side=2 resource and ideal logical operations.
- **rationale:** Within the note's explicit boundary, the runner computes the finite-resource bridge rather than merely asserting a Bell-frame label: it reports the raw best Bell state, applies the known Bob-side retained-axis frame, and checks exact/sample/branch fidelities, no-record independence, outcome coverage, and causal-record behavior. The note does not promote raw xi_5 as a retained readout and does not claim hardware teleportation, matter transport, larger 3D surfaces, or faster-than-light signaling.
- **auditor confidence:** medium

### `teleportation_3d_resource_probe_note`

- **Note:** [`TELEPORTATION_3D_RESOURCE_PROBE_NOTE.md`](../../docs/TELEPORTATION_3D_RESOURCE_PROBE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite numerical 3D side=2 teleportation-resource probe only: for the dense two-species N=8/H2_dim=64 Poisson-backed ground-state construction at mass=0 and G in {0,100,500,1000}, using retained last-taste-axis logical extraction and ideal ordinary two-qubit teleportation diagnostics, the null row stays non-resource, the G=500 and G=1000 rows are high Bell-frame resources in the Psi+ frame, Bob pre-message pairwise no-record input distance is at machine precision, and fixed Phi+ teleportation is poor unless the Bell frame is tracked. This excludes matter, mass, charge, energy, object, or faster-than-light transport; excludes physical preparation/readout workflow, side>2 scaling, dense side=4 claims, and unconditional teleportation-lane closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Dense finite-state computation of the 3D side=2 two-species ground state, reduction to a retained-axis two-qubit resource, Bell-frame overlap/fidelity diagnostics, and no-record input-independence checks.  _(class `C`)_
- **chain closes:** True — The row is explicitly bounded to the smallest exact 3D side=2 numerical artifact with no ledger dependencies. The live runner reproduced the refreshed table and all acceptance gates: null non-resource, at least one non-null high Bell-frame resource, clean Bob pre-message input-independence, retained-axis extraction, and no side>2 scaling claim.
- **rationale:** The source note's quantitative table matches the live runner modulo harmless last-digit ordering in no-signaling distances. The runner constructs the finite Hamiltonian, traces to the retained-axis logical two-qubit resource, applies standard ideal teleportation diagnostics, and reports the expected Psi+ Bell-frame boundary. The note is careful not to claim physical object transport, preparation/readout closure, or larger-surface scaling, so the bounded numerical readout is supported.
- **auditor confidence:** high

### `teleportation_adiabatic_time_evolution_note`

- **Note:** [`TELEPORTATION_ADIABATIC_TIME_EVOLUTION_NOTE.md`](../../docs/TELEPORTATION_ADIABATIC_TIME_EVOLUTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** On the small ideal 2D 4x4 Poisson ramp, midpoint piecewise-unitary smoothstep evolution at T=40 yields an ordinary taste-qubit teleportation resource with Favg=0.980291, Phi+=0.970437, ground overlap=0.999985, and sampled pre-message input-independence.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-Singer-the-2nd-019deb55-df2c-7bf2-80c4-5eb99d413fc9`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The finite-time closed-system simulation shows that a smooth endpoint schedule can reach the target logical Bell-resource quality with small full-state diabatic loss on the default 2D 4x4 surface.  _(class `C`)_
- **chain closes:** True — Within the stated small closed-system model, the source-note numbers match the live runner output and the runner computes the finite-time evolution, logical trace, teleportation fidelity, null control, and no-message checks. The closure is only for the bounded diagnostic, not for scalable or physical hardware preparation.
- **rationale:** The scoped claim is a bounded numerical diagnostic, not the hinted open gate or a physical preparation theorem. The live runner output supports the finite-time candidate, the null non-resource control, and Bob pre-message input-independence under the stated ideal protocol boundary. No hidden matter-transfer, FTL, scaling, or hardware-readout claim is needed for the audited statement.
- **auditor confidence:** high

### `teleportation_causal_channel_note`

- **Note:** [`TELEPORTATION_CAUSAL_CHANNEL_NOTE.md`](../../docs/TELEPORTATION_CAUSAL_CHANNEL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A narrow model harness shows that an explicit classical Bell-measurement record can be carried on a positive-latency directed lattice channel without deriving the record bits or enabling pre-delivery signaling.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-Hegel-the-2nd-019deb5a-bdd5-78e0-87c0-ddf419a2b445`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** The harness checks that an explicit two-bit Bell record is scheduled on a finite directed lattice/DAG with positive latency, no early or duplicate delivery, and Bob pre-delivery no-signaling.  _(class `C`)_
- **chain closes:** True — The source note limits the claim to a causal classical-record channel, and the runner directly checks the scheduling, delivery, wrong/delayed controls, post-delivery correction, and pre-delivery Bob no-signaling properties. No cited dependencies or external physical identifications are needed for that bounded model claim.
- **rationale:** The scoped claim closes because the runner constructs the channel and teleportation-control harness directly, then verifies the stated causal and no-signaling properties within the declared boundary. The note explicitly excludes FTL signaling, matter/mass/charge transfer, Bell-record derivation from the DAG, and CHSH/Poisson derivation, so the clean verdict does not ratify those stronger claims. Residual risk is limited to this being a first-artifact model harness rather than a broader physical derivation.
- **auditor confidence:** high

### `teleportation_conclusion_boundary_note`

- **Note:** [`TELEPORTATION_CONCLUSION_BOUNDARY_NOTE.md`](../../docs/TELEPORTATION_CONCLUSION_BOUNDARY_NOTE.md)
- **claim_type:** `open_gate`
- **claim_scope:** Audited only as an ordinary quantum-state teleportation planning boundary that records unresolved selector, scaling, and hardware obligations and forbids nature-grade promotion.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-teleportation_conclusion_boundary_note-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The current lane status is `planning_closed = True`, `unconditional_closed = False`, `promote_to_nature_grade = False`, with retained status `planning closed as conditional theory; nature-grade closure HOLD`.  _(class `E`)_
- **chain closes:** False — The chain does not close as a derivation: no cited authority derives the selector residuals, side-12 scaling certificate, side-14 blocker, or hardware evidence status. The runner sets those fields as constants and checks that the resulting boundary flags remain HOLD.
- **rationale:** Issue: The load-bearing lane status is introduced as fixed boundary data, and the runner hard-codes the selector, scaling, and hardware fields rather than deriving them from an axiom or cited authority. Why this blocks: with no cited authorities, the restricted packet cannot substantively verify the underlying selector residuals, finite certificate, side-14 blocker, or hardware evidence status. Repair target: add and audit direct dependency notes or a runner that actually derives the underlying selector, scaling, and hardware facts. Claim boundary until fixed: it may be cited only as a planning HOLD/open-gate boundary for ordinary state teleportation, not as theorem evidence.
- **auditor confidence:** high

### `teleportation_dynamical_resource_generation_note`

- **Note:** [`TELEPORTATION_DYNAMICAL_RESOURCE_GENERATION_NOTE.md`](../../docs/TELEPORTATION_DYNAMICAL_RESOURCE_GENERATION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Default 1D N=8 exact-diagonalization product-state scans under H = H1 x I + I x H1 + G V_Poisson find useful but low-fidelity logical taste-qubit teleportation resources for interacting cases, no Bell-overlap >= 0.90 windows, non-useful G=0 controls, and input-independent Bob no-record states.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-Hubble-the-2nd-019deb60-0b7b-7d63-b378-7dbadcbd7cc4`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** No high-fidelity Bell-resource window appears in this bounded product-state scan at the 0.90 Bell-overlap threshold, while interacting cases open only useful low-fidelity windows after fixed Bell-frame alignment.  _(class `C`)_
- **chain closes:** True — The runner directly computes the stated finite model, extraction, Bell overlaps, teleportation fidelity estimates, null control, and Bob no-record input-independence for the default bounded cases. The note keeps the claim within ordinary quantum state teleportation and explicitly states the small-surface, sampled-time, ideal-logical-operation limits.
- **rationale:** The scoped result is a bounded finite/model computation, not a no-go theorem and not merely an open obligation. The live output supports the note's numerical boundary: interacting cases exceed the useful Bell-overlap threshold but remain far below the 0.90 high-fidelity threshold, with null and no-signaling diagnostics passing. No hidden carrier, matter-transfer, FTL, or protocol-readout claim is needed for the bounded statement.
- **auditor confidence:** high

### `teleportation_logical_readout_audit`

- **Note:** [`TELEPORTATION_LOGICAL_READOUT_AUDIT.md`](../../docs/TELEPORTATION_LOGICAL_READOUT_AUDIT.md)
- **claim_type:** `open_gate`
- **claim_scope:** The audit validates reduced logical trace extraction for taste-only observables in the audited Poisson/CHSH cases, while identifying operational retained-taste readout/control as still unestablished.
- **audit_status:** ~~audited_clean~~
- **effective_status:** open_gate  (reason: `audited_open_gate`)
- **auditor:** `fresh-teleportation-logical-readout-auditor`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** Cells and spectators can be ignored only if preparation, Bell measurement, correction, and readout are proven to factor as logical taste operators tensor identity on the environment, or an explicit blind/heralded environment workflow is supplied.  _(class `B`)_
- **chain closes:** True — The scoped open gate closes: the runner establishes trace validity and input-independent Bob no-record behavior, but also shows fixed-environment branch variation and no supplied apparatus/control model. The missing operational step is native retained-taste preparation, measurement, feed-forward, and correction that is blind to cells and spectator tastes, or an explicit heralded branch protocol.
- **rationale:** This row is best treated as a clean open_gate rather than a theorem claim. The note does establish the mathematical reduced-density diagnostic for taste-only observables, but its citeable load-bearing content is the blocker: trace extraction alone is not an operational logical readout primitive. The runner output directly supports that distinction and does not rely on one-hop cited authorities.
- **open / conditional deps cited:**
  - `TELEPORTATION_LOGICAL_READOUT_AUDIT.md`
- **auditor confidence:** high

### `teleportation_no_signaling_audit`

- **Note:** [`TELEPORTATION_NO_SIGNALING_AUDIT.md`](../../docs/TELEPORTATION_NO_SIGNALING_AUDIT.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** No-signaling for the ideal encoded taste-qubit teleportation protocol only: before receipt of Alice's two classical Bell bits, Bob's local reduced state is independent of Alice's unknown input state.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `fresh-agent-James-the-2nd-019deb78-27fb-70c0-97f4-c96ffdddd24f`  (codex-gpt-5; independence=fresh_context)
- **load-bearing step:** For the ideal three-register encoded taste-qubit protocol |psi>_A tensor |Phi+>_RB with Alice Bell measurement on A,R, Bob's reduced state is I/2 before measurement and remains sum_zx p_zx rho_B|zx = I/2 after Alice's measurement when the Bell outcome record is inaccessible.  _(class `B`)_
- **chain closes:** True — The scoped claim closes as finite-dimensional teleportation algebra over the explicitly constructed encoded qubit, Bell projectors, partial trace, outcome averaging, and positive-latency classical record. The runner numerically exercises the finite protocol to machine precision and the note explicitly excludes matter transport, FTL signaling, measurement-foundation, durable-record, and Bell-resource-origin claims.
- **rationale:** The load-bearing no-signaling statement is not a physical-carrier identification or CHSH-to-teleportation bridge; it is the standard reduced-density-matrix statement inside the explicitly bounded encoded two-level protocol. The runner constructs the logical taste Pauli operators, Bell projectors, random input states, pre-measurement Bob partial trace, post-measurement outcome-averaged Bob state, pairwise input-independence check, and delayed two-bit record channel, all passing at machine precision. Residual risk is limited to the stated ideal-protocol boundary: this audit does not certify matter teleportation, mass/charge/energy transfer, FTL communication, a measurement theory, durable classical records, or derivation of the Bell resource from another lane.
- **auditor confidence:** high

### `teleportation_poisson_finite_extraction_core_bounded_note_2026-06-18`

- **Note:** [`TELEPORTATION_POISSON_FINITE_EXTRACTION_CORE_BOUNDED_NOTE_2026-06-18.md`](../../docs/TELEPORTATION_POISSON_FINITE_EXTRACTION_CORE_BOUNDED_NOTE_2026-06-18.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite offline extraction on 1D N=8, G=1000 and 2D 4x4, G=1000 Poisson/CHSH cases, with 1D N=8, G=0 null separation, using RALA last-taste logical carriers.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260619-203739-0fd17364-teleportation_poisson_finite_extraction_core_bounded_note_2026-06-18-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Tracing cells and spectator tastes while keeping the last retained taste bit per species yields a deterministic high-fidelity logical Bell resource on the two Poisson/CHSH finite cases, while the G=0 null control fails.  _(class `C`)_
- **chain closes:** True — The runner and helpers construct the finite Hamiltonians, compute ground states, factor sites into logical/environment labels, trace the environment, and evaluate Bell overlap, negativity, CHSH, and teleportation fidelity. The cited RALA authority is retained-grade for the logical-operator algebra used by the extraction.
- **rationale:** The load-bearing finite-resource extraction is computed from the framework primitives in the included helper chain rather than read from a note or hard-coded as an expected value. The primary runner’s PASS output is backed by source that calls the Hamiltonian construction, eigensolve, KS factorization, logical partial trace, and teleportation-statistics routines. The theorem is clean only at the declared finite offline scope; the source explicitly keeps native physical preparation/readout outside this claim.
- **auditor confidence:** high

### `teleportation_poisson_resource_sweep_note`

- **Note:** [`TELEPORTATION_POISSON_RESOURCE_SWEEP_NOTE.md`](../../docs/TELEPORTATION_POISSON_RESOURCE_SWEEP_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded numerical sweep of deterministic traced encoded two-qubit teleportation resources on 1d_N8 and 2d_4x4 Poisson-coupled lattices over the stated mass and coupling grid.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T200222Z-9b320dba-teleportation_poisson_re-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** High coupling and low mass produce deterministic high-fidelity encoded Bell resources on the audited 1D N=8 and 2D 4x4 surfaces.  _(class `C`)_
- **chain closes:** True — The runner constructs the Poisson-coupled two-species Hamiltonian, solves the ground state, traces to the logical taste qubits, and computes Bell overlap, fixed-protocol teleportation fidelity, CHSH, purity, and negativity rather than reading those quantities from another note. Within the explicitly bounded grid and ordinary quantum-state teleportation scope, the reported parameter-window conclusion follows.
- **rationale:** The source note makes a bounded, non-uniform numerical claim and the supplied runner performs the load-bearing computation from instantiated lattice, Poisson, Hamiltonian, ground-state, partial-trace, and teleportation-resource calculations. The code does not merely print constants, import the contested result from another note, or tune against an external comparator. The clean verdict is limited to the stated small sweep and does not promote matter transport, FTL signaling, or a uniform theorem over all parameters.
- **auditor confidence:** medium

### `teleportation_retained_axis_operator_algebra_closure_note`

- **Note:** [`TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md`](../../docs/TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-grid algebraic closure of RALA(a) for dims 1,2,3, sides 2,4, all retained axes, including axis Pauli/Bell membership, native-Z and fixed-X membership conditions, base/fiber commutation, Pauli XOR composition, and ideal logical teleportation closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260607-162127-f0bf5d12e1-teleportation_retained_axis_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** After reordering into |b>_logical x |e>_env, the retained-axis Pauli and Bell operators factor as standard logical qubit operators tensored with I_env, so the ideal protocol reduces to ordinary two-qubit teleportation on the logical factor.  _(class `A`)_
- **chain closes:** True — The stated KS block decomposition directly gives O_logical x I_env for retained-axis operators, spectator-sign cancellation for native-Z when d>1, and environment flipping for fixed-X when a != d-1. The Bell projector and teleportation claims then reduce to standard two-qubit Pauli/Bell algebra on the logical factor.
- **rationale:** The theorem is self-contained in the restricted packet and closes by finite block-matrix algebra. Independent formula checks confirm the Bell-projector signs, the 1/4 normalization, the native-Z spectator average to zero for d>1, the fixed-X iff a=d-1 condition, and the correction/fidelity identity up to irrelevant branch phase. The runner genuinely constructs the relevant operators and verifies 96 algebraic cases without hidden helper imports or external comparators, while explicitly leaving physical apparatus, noise, preparation, and durable record gates outside scope.
- **auditor confidence:** high

### `thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow_theorem_note_2026-05-16`

- **Note:** [`THOOFT_1981_DUAL_SUPERCONDUCTOR_CENTER_VORTEX_CONFINEMENT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`](../../docs/THOOFT_1981_DUAL_SUPERCONDUCTOR_CENTER_VORTEX_CONFINEMENT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md)
- **claim_type:** `open_gate`
- **claim_scope:** Pure syntactic registration of external confinement-mechanism vocabulary as an open gate; no monopole/vortex condensation, Wilson-loop area law, string-tension derivation, or framework observable bridge is audited as proved.
- **audit_status:** ~~audited_renaming~~
- **effective_status:** ~~audited_renaming~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260618-112229-b3680374-thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow_theorem_note_2026-05-16-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The row's load-bearing packet is only P_THOOFT_REG: a pure syntactic vocabulary registration and open-gate boundary for abelian-projection, monopole/dual-superconductor, center-vortex, symbolic action-form, and Wilson-loop area-law notation.  _(class `E`)_
- **chain closes:** True — The restricted packet closes only the definitional registration and boundary disclaimer. It does not close any physical confinement mechanism or framework bridge, and the note explicitly excludes those conclusions.
- **rationale:** Issue: the load-bearing move is the definition/registration of P_THOOFT_REG plus boundary disclaimers, while the runner verifies text presence and tautological symbolic identities. Why this blocks: no retained authority or derivation establishes monopole condensation, center-vortex percolation, Wilson-loop area law, positive string tension, or a framework observable bridge. Repair target: add retained one-hop authorities or retained bridge theorems before using this row as theorem input. Claim boundary until fixed: pure syntactic open-gate vocabulary catalogue.
- **auditor confidence:** high

### `three_generation_observable_m3c_burnside_narrow_theorem_note_2026-05-10`

- **Note:** [`THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md`](../../docs/THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** The specified cyclic permutation and three diagonal involutions on abstract C^3 generate M_3(C), implying irreducibility and the stated Burnside corollary.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.6-sol-parallel-20260712T130312Z-96c5c841-00237-three_generation_observable_`  (codex-gpt-5.6; independence=cross_family)
- **load-bearing step:** The explicit identities E_ij = P_i C^((i-j) mod 3) P_j place all nine matrix units in A, so A = M_3(C).  _(class `A`)_
- **chain closes:** True — The projector formulas select the three coordinate lines, and the cyclic permutation connects every ordered pair of those lines, yielding every matrix unit. The conclusions then follow by elementary finite-dimensional linear algebra without physical or numerical imports.
- **rationale:** The load-bearing matrix-unit construction is a genuine algebraic closure over the matrices explicitly defined in the note. The runner source performs exact symbolic calculations rather than printing hard-coded expected results, and its 50 successful checks support the stated projector, spanning, irreducibility, and rank-one conclusions. Two displayed scalar-factor annotations in the P_1 calculations are typographical errors, but the resulting projector actions and the load-bearing derivation remain correct.
- **auditor confidence:** high

### `two_field_retarded_family_closure_note_2026-04-10`

- **Note:** [`TWO_FIELD_RETARDED_FAMILY_CLOSURE_NOTE_2026-04-10.md`](../../docs/TWO_FIELD_RETARDED_FAMILY_CLOSURE_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The family-closure loop preserves the retarded battery on the cycle-bearing families and extends the same operating-point closure to the layered DAG-derived control (8/9, with gauge structurally N/A).  _(class `C`)_
- **chain closes:** True — The source note states a bounded graph-battery diagnostic rather than a retained attraction theorem, and the registered runner recomputes the force, stability, norm, family-closure, gauge, and gap rows from the stated retarded/hybrid law. The note's measurement caveat keeps the irregular sign rows at the field-profile diagnostic level, which matches what the runner checks.
- **rationale:** The current runner output matches the note's battery table: the three cycle-bearing families score 9/9 and the layered DAG-derived control scores 8/9 only because native gauge is structurally unavailable without a cycle. The load-bearing claim is bounded to a family-conditioned closure diagnostic, and the note explicitly avoids using the irregular force rows as proof that attraction is dynamically chosen. Residual risk is that this remains a conditioned sibling harness rather than a single retained canonical theorem.
- **auditor confidence:** high

### `two_field_retarded_probe_note_2026-04-10`

- **Note:** [`TWO_FIELD_RETARDED_PROBE_NOTE_2026-04-10.md`](../../docs/TWO_FIELD_RETARDED_PROBE_NOTE_2026-04-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** The retarded memory channel preserves the core force battery on admissible graph families, but it does not yet close the family-robustness row across all initial-state sectors.  _(class `C`)_
- **chain closes:** True — The source note is bounded to a retarded/hybrid field-law battery and explicitly records the R7 family failures and the diagnostic-only status of R9. The registered runner recomputes the same rows and reproduces the note's 7/8, 8/8, 7/8 scored outcomes with the same sector failures.
- **rationale:** The current runner output matches the source note's table: zero-source, linearity, additivity, main force, iterative stability, norm, and gauge rows pass as reported, while R7 fails on color-0 for random geometric and color-1 for layered cycle. The note does not promote those irregular sign rows to an attraction theorem and explicitly treats them as field-profile diagnostics under the parity-coupled proxy. Residual risk is confined to the note's own boundary: this is a viable bounded candidate battery with sector robustness still open, not a retained canonical closure.
- **auditor confidence:** high

### `unification_basin_failure_note`

- **Note:** [`UNIFICATION_BASIN_FAILURE_NOTE.md`](../../docs/UNIFICATION_BASIN_FAILURE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite audit of the two listed shared rows, drift = 0.20 with restore = 0.60 and 0.70, under the provided fixed-field geometry-sector runner: signed-source gates pass, complex-action crossover does not, and unified survival is 0/2.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260608-212214-0afd84f823-unification_basin_failure_no`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the two shared off-center rows, gamma = 0 remains positive but gamma = 0.2 and gamma = 0.5 are both absorptive, so the TOWARD -> AWAY complex-action crossover is lost while the signed-source gates still pass.  _(class `C`)_
- **chain closes:** True — The cited upstream authorities are retained-grade or retained_bounded, and the provided runner/helper sources instantiate the grown geometry, geometry-sector adjacency, source fields, propagation, centroid readout, and survivor predicates rather than importing the contested row values. The cached output matches the source table and reports sign-law survivors 2/2, complex-action survivors 0/2, and unified survivors 0/2.
- **rationale:** The audited statement is bounded to the two listed rows and the supplied fixed-field sector-family computation. The load-bearing negative result is computed directly: zero and neutral sign controls vanish, plus/minus signs are correctly oriented with exponent near one, while delta@0.2 and delta@0.5 are negative on both rows, eliminating the crossover required for unified survival. No cited authority is below retained-grade, and no external comparator, tuned numerical match, or missing bridge is needed for this bounded failure diagnosis.
- **auditor confidence:** medium

### `universal_gr_bd_congruence_invariance_bounded_note_2026-05-10`

- **Note:** [`UNIVERSAL_GR_BD_CONGRUENCE_INVARIANCE_BOUNDED_NOTE_2026-05-10.md`](../../docs/UNIVERSAL_GR_BD_CONGRUENCE_INVARIANCE_BOUNDED_NOTE_2026-05-10.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Pure finite-dimensional real matrix trace identity only: with D and S invertible and B_D(h,k)=-Tr(D^{-1} h D^{-1} k), the full congruence transformation D'=S^T D S, h'=S^T h S, k'=S^T k S satisfies B_{D'}(h',k')=B_D(h,k), using only bounded textbook matrix algebra (cyclic trace and inverse-of-product). This excludes the parent universal-GR global atlas bookkeeping consequence, atlas/cocycle/nondegeneracy/pairing-covariance hypotheses, physical Cl(3)/Z^3 derivation of linear algebra, and any unconditional global stationary-section closure.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Cyclic-trace and inverse-of-product reduction of B_{D'}(h',k') to B_D(h,k), with live runner checking multiple finite dimensions, symmetric inputs, and partial-transformation failure mode.  _(class `A`)_
- **chain closes:** True — The note is explicitly split to the pure trace identity and admits only bounded textbook finite-dimensional matrix algebra. The live runner reproduced PASS=70, FAIL=0 and confirms the note boundaries, imported modules, invariance checks, and non-claimed parent consequences.
- **rationale:** The algebraic identity is correct by direct substitution: (S^T D S)^{-1}=S^{-1}D^{-1}(S^T)^{-1}, adjacent inverse factors cancel, and cyclicity removes the outer S^{-1}/S pair. The source note accurately excludes the parent's global stationary-section claim and the parent admitted-context hypotheses, so the bounded row closes cleanly on BA-1 alone.
- **auditor confidence:** high

### `universal_gr_cubic_ward_finite_scaling_diagnostic_bounded_theorem_note_2026-06-08`

- **Note:** [`UNIVERSAL_GR_CUBIC_WARD_FINITE_SCALING_DIAGNOSTIC_BOUNDED_THEOREM_NOTE_2026-06-08.md`](../../docs/UNIVERSAL_GR_CUBIC_WARD_FINITE_SCALING_DIAGNOSTIC_BOUNDED_THEOREM_NOTE_2026-06-08.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite runner-defined cubic Ward residual scaling diagnostic on L=6,8,10,12, including monotone resid/amplitude/k^2 behavior and finite-range candidate C near 0.047..0.050.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260610-055746-c71665923a-universal_gr_cubic_ward_fini`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner computes the a2*a3 cubic Ward residual cross term for L=6,8,10,12 and finds finite data compatible with resid/amplitude ~ C k^2, with simple extrapolants giving C near 0.047..0.050.  _(class `C`)_
- **chain closes:** True — The runner source constructs the lattice operators and diffeomorphism variation and computes the residual/amplitude data without importing or hard-coding the contested coefficient. Independent arithmetic from the displayed data confirms the monotonic normalized ratios, shrinking increments, approximately constant amplitude*k^2 spread under 15%, and the stated Richardson/geometric extrapolants.
- **rationale:** The source note is explicitly bounded to the finite runner-defined diagnostic and does not claim an analytic continuum theorem, physical normalization, irrelevant-operator identification, or all-order Ward closure. The included runner genuinely computes the finite lattice quantities from its defined operators, has no helper imports, and does not just print expected constants. The numerical claims in the table and extrapolants check out up to ordinary rounding, so the bounded finite diagnostic closes on the restricted packet.
- **auditor confidence:** high

### `universal_gr_quartic_diffeo_ward_continuum_closure_bounded_theorem_note_2026-06-08`

- **Note:** [`UNIVERSAL_GR_QUARTIC_DIFFEO_WARD_CONTINUUM_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-08.md`](../../docs/UNIVERSAL_GR_QUARTIC_DIFFEO_WARD_CONTINUUM_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-08.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-lattice quartic diffeomorphism Ward diagnostic for the explicitly defined Dcons operator, with conserved L=6,8,10 monotone scaling and naive C1 controls at L=6,8.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260610-044227-86596b9e3e-universal_gr_quartic_diffeo_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The conserved D(P_eff)+sqrt(g) quartic Ward residual normalized by the gauge amplitude decreases monotonically over L=6,8,10 (0.203, 0.164, 0.143, about k^0.69), while the naive C1 control is much flatter and larger at the shared momenta.  _(class `C`)_
- **chain closes:** True — The runner source explicitly builds the finite Z^3 lattice operators, Pauli blocks, densitized-vielbein coupling, lattice diffeomorphism variation, and a2*a3*a4 cross extraction, with no helper imports or upstream numerical inputs. Independent arithmetic checks k=2*pi/L, the reported exponents, monotonicity, and conserved-vs-naive comparisons from the displayed values.
- **rationale:** The load-bearing result is a first-principles finite-lattice computation from the stated operator definition, not a renaming, external comparator match, or copied upstream value. The runner has hard-coded prose in its final summary, but the PASS checks compute the residual ratios and exponents before testing them. The clean scope is bounded to the runner-supported diagnostic; the naive comparison is established at the two shared momenta reported by the runner, not as an independent all-L naive continuum extrapolation.
- **auditor confidence:** high

### `universal_gr_quintic_diffeo_ward_closure_bounded_theorem_note_2026-06-08`

- **Note:** [`UNIVERSAL_GR_QUINTIC_DIFFEO_WARD_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-08.md`](../../docs/UNIVERSAL_GR_QUINTIC_DIFFEO_WARD_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-08.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** The audited claim is the finite-lattice quintic Ward diagnostic for the specified four non-collinear TT graviton modes and gauge field: conserved D(P_eff)+sqrt(g) has about 20-33x smaller normalized residual than the naive control and decreases from L=6 to L=8, without claiming all-order closure or a fitted continuum exponent.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260610-060757-31c51a5c6c-universal_gr_quintic_diffeo_`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** For the runner-defined four-fold a2*a3*a4*a5 cross term of dW/depsilon, the conserved D(P_eff)+sqrt(g) coupling gives a quintic resid/amplitude far below the naive coupling, remains amplitude-stable, and decreases from L=6 to L=8 while the naive residual stays flat.  _(class `C`)_
- **chain closes:** True — The runner source constructs the lattice operators, conserved and naive Dirac operators, TT modes, lattice diffeomorphism variation, finite-difference dW/depsilon, and 16-point fourth cross term directly; it does not read or hard-code the contested residuals. Manual checks of the sine-expansion coefficients, cross-stencil normalization, TT transversality/tracelessness, and momentum closure match the stated bounded diagnostic.
- **rationale:** The load-bearing step is a first-principles finite computation from the framework baseline, not a definition, renaming, external comparator, or tuned numerical match. The included source computes the residuals from instantiated lattice matrices and asserts three bounded checks: conserved-vs-naive contrast at L=6, amplitude robustness at amp 0.04 and 0.09, and conserved decrease from L=6 to L=8 with naive flatness. There are no cited non-retained authorities or missing helper imports in the restricted packet. The clean verdict is limited to the bounded runner-defined quintic diagnostic, not an all-order Einstein-Hilbert closure claim.
- **auditor confidence:** high

### `universal_gr_supermetric_normal_form_note`

- **Note:** [`UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md`](../../docs/UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Given W[J]=log det(D+J)-log det D and positive invariant background D=diag(a,b,b,b), the local Hessian on symmetric 3+1 perturbations equals the inverse-metric contraction and has the stated canonical diagonal normal form.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-gpt-5.5-xhigh-universal-gr-supermetric-audit-2-2026-05-07`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** For symmetric perturbations h,k on D=diag(a,b,b,b), B_D(h,k)=D^2W[0](h,k)=-Tr(D^-1 h D^-1 k), and in the canonical lapse/shift/trace/shear basis this has weights diag(-a^-2, -(ab)^-1 x3, -b^-2 x6).  _(class `A`)_
- **chain closes:** True — The audited claim is explicitly bounded to the local algebraic Hessian once the log-det generator and invariant background are assumed. Jacobi's formula, the inverse-variation identity, cyclicity of trace, and the displayed orthonormal canonical basis suffice to derive the formula and diagonal weights without importing the excluded scalar-generator selection or Einstein/Regge gluing premises.
- **rationale:** The load-bearing step is a closed matrix-calculus identity over explicitly stated local inputs, and the note's claim boundary excludes the unproved physical selection and dynamical gluing steps. The runner source directly differentiates the symbolic log determinant for general symmetric h,k, checks the canonical Gram matrix symbolically, and numerically replays the same algebra; it does not hard-code an external comparator or tune a scale. Residual risk is only scope leakage by downstream users: this clean verdict covers the local Hessian normal form, not the route-wide scalar-generator selection premise or full GR/Regge dynamics.
- **auditor confidence:** high

### `universal_qg_uv_finite_partition_note`

- **Note:** [`UNIVERSAL_QG_UV_FINITE_PARTITION_NOTE.md`](../../docs/UNIVERSAL_QG_UV_FINITE_PARTITION_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited the restricted-packet claim that the direct-universal positive-background discrete GR operator yields a finite Euclidean Gaussian partition density whose mean/stationary sector equals the discrete GR stationary field on finite charts and patches as a density across the finite atlas.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260505-225305-c0ea7096-universal_qg_uv_finite_p-095`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Because K_GR(D) is symmetric positive definite on each finite chart, the finite-dimensional Gaussian integral Z_GR(D,J) exists with the stated determinant formula and mean K_GR(D)^-1 J.  _(class `A`)_
- **chain closes:** False — The Gaussian conclusion follows algebraically from a finite-dimensional symmetric positive definite K_GR(D), but that SPD positive-background local closure theorem is imported rather than provided as a retained-grade cited authority. In addition, the supplied cited authorities are audited_conditional and unaudited, so retained-grade closure does not propagate.
- **rationale:** The load-bearing Gaussian finiteness and mean-field statements are standard class-A consequences once finite-dimensional SPD K_GR(D) is granted. The restricted packet does not independently close the required positive-background SPD/local GR theorem, and one cited authority is explicitly audited_conditional while another is unaudited. Therefore the theorem is conditional on upstream retained-grade closure of those inputs rather than clean within this packet.
- **open / conditional deps cited:**
  - `UNIVERSAL_GR_LORENTZIAN_GLOBAL_ATLAS_CLOSURE_NOTE.md`
  - `UNIVERSAL_QG_PROJECTIVE_SCHUR_CLOSURE_NOTE.md`
  - `UNIVERSAL_GR_POSITIVE_BACKGROUND_LOCAL_CLOSURE_NOTE.md`
- **auditor confidence:** high

### `valley_linear_action_note`

- **Note:** [`VALLEY_LINEAR_ACTION_NOTE.md`](../../docs/VALLEY_LINEAR_ACTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded same-harness comparison of spent-delay versus valley-linear S=L(1-f) on the fixed 3D ordered dense lattice 1/L^2 family at h=0.25 with the stated slit geometry, detector readout, and field shape.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260511-224519-a7679e61-valley_linear_action_not-012`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The same-harness comparison table reports that, with only the action law changed, valley-linear has Born 4.20e-15, k=0 +0.00e+00, F~M alpha 1.00, TOWARD 8/8, and tail slope -0.93 versus spent-delay alpha 0.50 and tail slope -0.52.  _(class `C`)_
- **chain closes:** True — The supplied runner source instantiates the lattice, propagation rule, two action laws, field, slit setup, and fitted diagnostics directly, and the cached runner output matches the note's table. The conclusion is limited to that fixed computational harness and does not require an unstated upstream note.
- **rationale:** The load-bearing evidence is a completed first-principles compute inside the restricted packet, not a copied upstream value or a printed constant. The runner computes both actions under the same lattice and readout parameters and produces the reported Born, k=0, mass-law exponent, gravity sign/count, and tail slope diagnostics. The note's own language keeps the claim bounded and explicitly excludes convergence, derivation from axioms, and Newtonian-gravity promotion.
- **auditor confidence:** high

### `valley_linear_asymptotic_bridge_note`

- **Note:** [`VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md`](../../docs/VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded finite-lattice claim that the provided valley-linear 3D runner computes TOWARD sign persistence, near-linear mass scaling, and slice-dependent far-tail exponents for h=0.5,W=8; h=0.25,W=10; and h=0.25,W=12.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260511-235357-9cb095b6-valley_linear_asymptotic-001`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The replay table shows TOWARD persistence and F~M=1.00 across the tested h/W ladder while the far-tail exponent changes with h and W, so the result is a near-Newtonian finite-lattice bridge rather than a stabilized universal -1.00 theorem.  _(class `C`)_
- **chain closes:** True — Within the restricted packet, the runner performs numerical lattice propagations over the stated checkpoint ladder and fits the resulting mass and distance laws rather than printing fixed constants. The conclusion is bounded to the tested finite slices and does not assert a continuum theorem.
- **rationale:** The note's conclusion is conservative and matches the completed runner output: the tested slices remain TOWARD, preserve F~M near 1.00, and show far-tail slopes that vary across h/W choices. The runner source is not a trivial constant printer; it constructs lattice checkpoints, propagates fields, computes Born/k=0/gravity/mass-scaling/distance-law quantities, and fits power laws. No external comparator or imported calibrated measurement is used, and the claimed scope stays bounded to this finite replay.
- **auditor confidence:** medium

### `valley_linear_mirror_transfer_note`

- **Note:** [`VALLEY_LINEAR_MIRROR_TRANSFER_NOTE.md`](../../docs/VALLEY_LINEAR_MIRROR_TRANSFER_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** Valley-linear improves the random-DAG family relative to spent-delay, but spent-delay still has the edge on the mirror family, so the result is a transfer diagnostic rather than a unification theorem.  _(class `C`)_
- **chain closes:** True — The registered runner recomputes the random and mirror DAG comparison and reproduces the note's four-row table exactly. The source note remains bounded and explicitly denies a universal action-replacement theorem.
- **rationale:** The current output matches the frozen replay: random spent-delay 11/36 with mean -0.770064, random valley-linear 18/36 with +0.000155, mirror spent-delay 24/36 with +0.545083, and mirror valley-linear 23/36 with +0.036664. The note's safe read is exactly the runner's conclusion: branch-specific transfer, not a unification theorem. Residual risk is limited to the finite generator/seed scope declared in the note.
- **auditor confidence:** high

### `valley_linear_repro_note`

- **Note:** [`VALLEY_LINEAR_REPRO_NOTE.md`](../../docs/VALLEY_LINEAR_REPRO_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** This note exists so a skeptical reader can replay the valley-linear lane without mistaking it for a flagship theorem or for the broader 3D kernel story.  _(class `C`)_
- **chain closes:** True — The registered reproduction harness runs successfully with --valley-linear, prints the canonical retained comparison, and then runs the bounded same-family valley-linear replay. The note is an entry-point/replay note and explicitly does not certify derivation, convergence, or replacement of the spent-delay flagship.
- **rationale:** The current harness passed and produced the expected bounded replay: spent-delay Born 4.20e-15, k=0 zero, F~M 0.50, gravity +0.045346, TOWARD 8/8, tail -0.52; valley-linear Born 4.20e-15, k=0 zero, F~M 1.00, gravity +0.000224, TOWARD 8/8, tail -0.93. The note's claim is not a physics theorem; it is that this is the reproducible skeptical-reader entry point for the valley-linear fork, with limits stated. Residual risk is only the long runtime of the optional valley-linear replay.
- **auditor confidence:** high

### `valley_linear_robustness_note`

- **Note:** [`VALLEY_LINEAR_ROBUSTNESS_NOTE.md`](../../docs/VALLEY_LINEAR_ROBUSTNESS_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded replay of scripts/valley_linear_robustness_sweep.py for S = L(1-f), kernel 1/L^2 with h^2 measure, h = 0.5, on the tested 3D ordered-lattice width, connectivity, and length slices.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260512-002551-332e8573-valley_linear_robustness-003`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The strongest safe summary is that the valley-linear action is robust on the tested 3D ordered-lattice slices, with Born machine-clean, F~M = 1.00, and gravity TOWARD throughout the tested rows.  _(class `C`)_
- **chain closes:** True — The provided runner source constructs the lattice, propagates amplitudes under the stated action and kernel, and computes the reported observables rather than printing hard-coded expected values. The conclusions are explicitly limited to the tested slices and match the completed runner output.
- **rationale:** The note’s bounded tables are directly reproduced by a completed runner whose source performs the relevant numerical computation from the stated lattice/action setup. The runner does not import the contested table values from another note and does not use external comparator data. The claim is carefully scoped: it does not assert universality, a continuum theorem, or a settled derivation of the action law.
- **auditor confidence:** high

### `valley_linear_wide_tail_note`

- **Note:** [`VALLEY_LINEAR_WIDE_TAIL_NOTE.md`](../../docs/VALLEY_LINEAR_WIDE_TAIL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-lattice replay for the 3D ordered-lattice valley-linear branch at h=0.25, W=12, with the 1/L^2 kernel and h^2 measure, establishing the reported toward support and tail fits on the tested z=2..10 window.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260608-104410-c0e243ec85-valley_linear_wide_tail_note`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The verifier parses the nine raw no-barrier distance rows, finds peak_z=4, and recomputes the z>=5 far-tail fit as slope=-1.1685 with R^2=0.9972.  _(class `C`)_
- **chain closes:** True — The runner source contains a first-principles replay path that instantiates the stated lattice, field, propagator, action, kernel, and detector readout, and the registered verifier checks a SHA-pinned frozen replay log while recomputing the peak and log-log tail fits from parsed rows. The note’s conclusion is explicitly bounded to this finite replay window and does not claim asymptotic or dimensional universality.
- **rationale:** The load-bearing numerical result is not a definition, renaming, or external comparator match; it is a bounded framework computation with a frozen-row verifier that recomputes the contested peak and tail regressions rather than merely accepting prose. The helper source supplies the actual lattice construction, valley-linear propagation, h^2/L^2 weighting, field source, slit setup, and log-log fit used by the parent runner. The note scopes the result conservatively as a finite-lattice replay and explicitly excludes universal continuum or all-dimension claims.
- **auditor confidence:** high

### `wave_amplification_near_horizon_note`

- **Note:** [`WAVE_AMPLIFICATION_NEAR_HORIZON_NOTE.md`](../../docs/WAVE_AMPLIFICATION_NEAR_HORIZON_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** On the retained exact-lattice harness, the oscillating-source/static-source ratio stays close to 1x, with largest ratio 1.012 at alpha = 0.50.  _(class `C`)_
- **chain closes:** True — The live runner reproduces every frozen alpha row and the best-ratio summary. The source note limits the conclusion to this exact-lattice absorber sweep and explicitly rejects the broader near-horizon amplification headline.
- **rationale:** The claim is not a broad physical amplification theorem; it is a bounded negative result on one exact-lattice replay. The runner computes the static and oscillating retarded-source deflections for the five stated absorber strengths and reproduces the frozen table, including the largest ratio of 1.012 at alpha = 0.50. Because the note keeps the conclusion within that harness and reports the raw denominator, the chain closes on its own terms.
- **auditor confidence:** high

### `wave_direct_dm_family_scout_note`

- **Note:** [`WAVE_DIRECT_DM_FAMILY_SCOUT_NOTE.md`](../../docs/WAVE_DIRECT_DM_FAMILY_SCOUT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Exploratory one-seed, one-strength direct-dM family scout: for Fam1/Fam2/Fam3 at H=0.5 and H=0.35 with seed=0 and s=0.004, R_hist is negative in all six rows with values -43.59%, -42.36%, -42.33%, -37.73%, -44.29%, and -41.82%; no portability, multi-seed, null-stack, weak-sweep, or continuum-stability claim is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Holding seed=0, strength=0.004, H=0.5/0.35, and the matched direct-dM schedule fixed, all Fam1/Fam2/Fam3 rows keep the same negative R_hist sign and material magnitude.  _(class `C`)_
- **chain closes:** True — The exact scoped runner invocation constructs the three retained families, two H values, and matched early/late schedules, then reproduces the six quoted R_hist and delta_hist rows. The chain closes only for the explicitly one-seed, one-strength scout boundary.
- **rationale:** The exact all-family scout command reproduces the frozen result table: every family/H row has negative R_hist and a material magnitude in the stated -37.73% to -44.29% band. The note explicitly rejects portability, multi-seed, full control-stack, and continuum-stability interpretations, so the retained claim is only the bounded scout table. Residual risk is limited to future runner drift or downstream citations treating this scout as the full portability batch.
- **auditor confidence:** high

### `wave_direct_dm_h025_fam1_seed0_control_note`

- **Note:** [`WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md`](../../docs/WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Runner-defined Fam1, seed 0, H=0.25 control replay only: exact S=0 null, common negative weak-field sign across S=0.002/0.004/0.008, and approximately linear weak-field scaling with R_hist around -20% to -21%. No Fam1 seed1, Fam2, cross-family, or general H=0.25 portability claim.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-gpt-5.5-fresh-2026-05-27-hilbert-2nd`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The self-contained deterministic runner evaluates Fam1 seed0 at H=0.25 for S=0, 0.002, 0.004, and 0.008, producing an exact null at S=0, negative delta_hist for all nonzero strengths, R_hist near -20% to -21%, and |delta_hist/s| spread of 7.77%.  _(class `C`)_
- **chain closes:** True — Within the restricted packet, the note's numeric table and summary match the cached self-contained deterministic runner output. The bounded claim is limited to the computed Fam1 seed0 H=0.25 control replay and does not require an additional physical/readout bridge beyond the runner-defined quantities.
- **rationale:** The scoped computational claim closes from the packet: the cached deterministic runner output directly supports the exact null, stable negative sign pattern, and approximate weak-field scaling asserted in the note. The note explicitly excludes broader family, seed, cross-family, and portability claims, so no unclosed dependency is needed for the retained bounded scope.
- **auditor confidence:** high

### `wave_direct_dm_h025_fam1_seed1_control_note`

- **Note:** [`WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md`](../../docs/WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded numerical control-ladder claim for Fam1, seed 1, H=0.25 over S=0, 0.002, 0.004, and 0.008, including exact null, common negative sign, low scaled spread, and R_hist near -30%.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260522T233213Z-aae32cd8-wave_direct_dm_h025_fam1-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** `Fam1`, seed `1`, `H = 0.25` is now a controlled fine-`H` replay with exact null, stable sign, and approximately linear weak-field scaling at `R_hist ~ -30%`.  _(class `C`)_
- **chain closes:** True — The supplied runner cache matches the table and summary in the note, and the primary runner fixes the claimed family, seed, H, and strength ladder before calling the shared compute path. Within the restricted packet, the claim remains bounded to this family/seed/H control replay and does not require a portability law.
- **rationale:** The runner output reports an exact S=0 null, negative delta_hist at all three nonzero strengths, R_hist values from -29.02% to -30.37%, and a 5.22% scaled-magnitude spread, matching the source note. The runner source is not a constant printer: it delegates to measure_dm after pinning the CLI arguments to Fam1, seed 1, H=0.25, and the included helper path constructs the lattice, histories, wave field, and beam response rather than importing the contested table from another note. The note's conclusion is appropriately bounded and explicitly avoids promoting a portability law.
- **auditor confidence:** medium

### `wave_direct_dm_h025_fam2_seed1_control_note`

- **Note:** [`WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md`](../../docs/WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited only the reported same-resolution Fam2 seed 1 H=0.25 direct-dM control ladder at S = 0, 0.002, 0.004, and 0.008, with the note's bounded interpretation.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260523T193922Z-380f8539-wave_direct_dm_h025_fam2-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The retained Fam2, seed 1, H = 0.25 point has an exact S = 0 null, common negative weak-field sign, low |delta_hist/s| spread, and stable normalized magnitude around -35%.  _(class `C`)_
- **chain closes:** True — The primary runner calls measure_dm over the stated strengths and prints values matching the note; the helper path shown instantiates the lattice growth, wave solve, beam propagation, and history comparison rather than importing the contested conclusion. Within the restricted packet, the stated null, sign pattern, and weak-field scaling summary follow from the completed runner output.
- **rationale:** The source note's load-bearing numerical claim is supported by a completed runner with exit code 0, and the printed rows match the note's table and summary. The primary runner does not hard-code the contested output values; it delegates to measure_dm and computes null size, sign pattern, and scaled spread from returned rows. No cited upstream authority is needed for this bounded control-ladder claim, and the note explicitly avoids broader family-pair portability claims.
- **auditor confidence:** medium

### `wave_direct_dm_h025_feasibility_note`

- **Note:** [`WAVE_DIRECT_DM_H025_FEASIBILITY_NOTE.md`](../../docs/WAVE_DIRECT_DM_H025_FEASIBILITY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded operational/numerical artifact: the Fam1 seed0 direct-dM matched-history harness at H=0.25 and S=0.004 completes within the declared 1800 s audit budget and emits dM(early)=+0.004989, dM(late)=+0.006246, delta_hist=-0.001256, R_hist=-20.12%, with the result interpreted only as a single-point feasibility/high-band-boundary datum. Portability, mechanism, coarse-to-fine law, and family-wide claims are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-gpt-5.5-xhigh-2026-05-28-wave-h025-feasibility`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The primary runner calls measure_dm(0.25, S_PHYS, Fam1, drift=0.20, restore=0.70, seed=0), completes under AUDIT_TIMEOUT_SEC=1800, and reports the H=0.25 seed0 direct-dM values used by the source note.  _(class `C`)_
- **chain closes:** True — The cached runner output matches the source's load-bearing point values: dM(early)=+0.004989, dM(late)=+0.006246, delta_hist=-0.001256, and R_hist=-20.12%. A manual arithmetic check confirms the sign and normalized magnitude from the printed dM values, and the one-hop H=0.25 boundary/synthesis dependencies are retained-bounded for the narrowed interpretation.
- **rationale:** The row is clean only as a bounded single-run feasibility and boundary datum. The runner computes the stated H=0.25 Fam1 seed0 point through the shared matched-history harness rather than importing the output constants, and the printed values agree with the source's scientific numbers. Residual risk is scope, not arithmetic: runtime/RSS are machine- and cache-dependent operational metadata, and this row does not establish portability, a mechanism, or a refinement-stable amplitude law.
- **auditor confidence:** high

### `wave_direct_dm_h025_high_band_boundary_note`

- **Note:** [`WAVE_DIRECT_DM_H025_HIGH_BAND_BOUNDARY_NOTE.md`](../../docs/WAVE_DIRECT_DM_H025_HIGH_BAND_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded Fam1 seed0 H=0.25, S=0.004 direct-dM point: dM(early)=+0.004989, dM(late)=+0.006246, delta_hist=-0.001256, R_hist=-20.12%, with the retained fine-pair synthesis establishing that seed 1 has the larger-magnitude negative R_hist at the same H and strength. Coarse H=0.5/0.35 provenance, coarse-to-fine reversal framing, mechanism claims, and portability claims are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-wave-direct-dm-h025-high-band-2026-05-28`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At H=0.25 for Fam1 seed0, the runner reports dM(early)=+0.004989, dM(late)=+0.006246, delta_hist=-0.001256, and R_hist=-20.12%, while the retained fine-pair synthesis says seed1 has the larger-magnitude negative R_hist at the same H and strength.  _(class `C`)_
- **chain closes:** True — The primary runner pins Fam1, seed 0, H=0.25, S=0.004 and computes the single fine-H point through the included wave/direct-dM helper path. Independent arithmetic from the printed values gives delta_hist=-0.001257, R_hist=-20.12%, and late gain +0.001257, and the retained two-point synthesis supplies the same seed0/seed1 fine-pair comparison without retaining coarse-band provenance.
- **rationale:** Clean only under the narrowed bounded fine-H scope. The runner cache completes and matches the source's seed0 H=0.25 row, and the one-hop retained_bounded synthesis supports the limited statement that seed1 is larger magnitude than seed0 in the controlled H=0.25 fine pair. The older H=0.5/H=0.35 high-band history, coarse-to-fine reversal language, and mechanism/portability interpretations are excluded because the retained synthesis explicitly removes those broader claims from scope.
- **auditor confidence:** high

### `wave_direct_dm_h025_low_band_retention_note`

- **Note:** [`WAVE_DIRECT_DM_H025_LOW_BAND_RETENTION_NOTE.md`](../../docs/WAVE_DIRECT_DM_H025_LOW_BAND_RETENTION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded seed-1 Fam1 H=0.25 direct-dM controlled replay: exact S=0 null, negative delta_hist for S=0.002/0.004/0.008, R_hist near -29% to -30%, and low scaled-spread in the pinned control-ladder runner. Coarse H=0.5/0.35 continuity rows, cross-seed ordering, downstream synthesis, and portability claims are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-wave-direct-dm-h025-low-band-2026-05-28`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The seed-1 control runner is the load-bearing H=0.25 point and reproduces the S=0.004 row with dM_early=+0.004411, dM_late=+0.006255, delta_hist=-0.001843, and R_hist=-29.47%, hardened by the S=0 null and S=0.002/0.004/0.008 ladder.  _(class `C`)_
- **chain closes:** True — The one-hop dependency is retained_bounded for the same Fam1 seed-1 H=0.25 control ladder, and the primary no-argument wrapper pins exactly family=Fam1, seed=1, H=0.25 before delegating to the included computation helpers. The cached runner output matches the source row and summary; independent arithmetic from the printed values confirms the negative signs, R_hist scale, and approximately 5.2% scaled-spread.
- **rationale:** Clean within the stated bounded scope. The runner is not a constant-printer: the wrapper pins the intended Fam1/seed1/H=0.25 arguments, the helper constructs source histories and wave/beam responses, and the cache completes under the declared 1800 s budget. The note also correctly demotes the H=0.5/H=0.35 comparison rows and broader cross-seed/portability discussion to non-load-bearing context.
- **auditor confidence:** high

### `wave_direct_dm_h025_two_point_synthesis_note`

- **Note:** [`WAVE_DIRECT_DM_H025_TWO_POINT_SYNTHESIS_NOTE.md`](../../docs/WAVE_DIRECT_DM_H025_TWO_POINT_SYNTHESIS_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Controlled Fam1 H=0.25, S=0.004 seed0/seed1 fine-pair synthesis: both seeds have negative matched-history delta after exact null controls, and seed 1 has the larger-magnitude negative R_hist in the two-point pair; no coarse-band reversal, mechanism, portability, or family-wide law is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop-wave-direct-dm-h025-two-point-20260528-r1`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The synthesis table combines the retained seed0 and seed1 control ladders at Fam1, H=0.25, S=0.004 and asserts common negative delta_hist with seed 1 having the larger-magnitude negative R_hist.  _(class `B`)_
- **chain closes:** True — Both one-hop control notes are retained-bounded, the direct runner completes in this worktree with PASS=39 FAIL=0, and independent arithmetic on the frozen logs confirms delta_hist = dM(early)-dM(late), negative signs for both seeds, and |R_hist(seed1)| > |R_hist(seed0)| at S=0.004.
- **rationale:** The source has been narrowed to the retained-core fine-pair comparison and explicitly excludes the older coarse-band reversal/mechanism claims. The runner checks source boundaries, reads only the two Fam1 seed-control logs, verifies exact nulls/sign patterns/spread summaries, and matches the S=0.004 table values. A separate log arithmetic check reproduces the negative deltas and R_hist ordering within rounding. Residual risk is limited to the finite logged control-ladder setup; no family-wide, portability, mechanism, or coarse-band conclusion is retained.
- **auditor confidence:** high

### `wave_equation_gravity_note`

- **Note:** [`WAVE_EQUATION_GRAVITY_NOTE.md`](../../docs/WAVE_EQUATION_GRAVITY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded claim that the provided lattice wave-equation runner supports only the narrowed kinematic upgrade claims and does not establish the two explicitly excluded stronger claims.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-wave_equation_gravity_no-033`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** The d'Alembertian wave-equation runner establishes finite-speed propagation, static-limit Poisson recovery, qualitative retardation, propagator mass linearity, and wave/Poisson agreement while explicitly failing 1/r radiation and Newton-like propagator distance law.  _(class `C`)_
- **chain closes:** True — The provided source code genuinely evolves a 3D lattice wave equation, solves/computes Poisson comparison data, fits exponents, and classifies each asserted subclaim against explicit thresholds. The note's narrowed conclusion follows from those computed pass/fail results within the finite-box numerical scope.
- **rationale:** The note no longer claims the two failed stronger results: strict 1/r radiation and Newton-like propagator distance law are both marked not established, matching the runner output. The retained positive assertions are computed directly by the supplied runner rather than imported from cited authorities or hard-coded as output constants. The audit is clean only for the bounded finite-lattice numerical theorem stated in the narrowed note, not for continuum gravitational radiation or a continuum Newtonian propagator law.
- **auditor confidence:** high

### `wave_equation_self_field_note`

- **Note:** [`WAVE_EQUATION_SELF_FIELD_NOTE.md`](../../docs/WAVE_EQUATION_SELF_FIELD_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the finite-lattice runner claim that the specified explicit wave-equation stencil, source, grid size, constants, and path-sum harness produce the reported static profile, F~M slopes, Born/null checks, gravity sign, and pulse retardation table.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260505-110856-be71e5c1-wave_equation_self_field-034`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Solving the stated discrete wave equation with a static source gives the Poisson-like field used by the path-sum tests, and a single-layer pulse gives first-arrival time equal to lattice offset.  _(class `C`)_
- **chain closes:** True — Within the bounded numerical scope, the runner directly evolves the discrete local wave equation and then computes the reported observables from that field. No cited upstream authority or external comparator is needed for the finite-run claim.
- **rationale:** The runner source performs actual numerical evolution of the stated second-order stencil and propagates amplitudes through the generated field; it does not merely print constants or import the contested results. The static, F~M, Born, null, gravity-sign, and retardation outputs are computed internally from the specified finite lattice setup. The clean verdict is bounded to this runner-level numerical theorem, not to broader physical equivalence with GR or untested multi-source/backreaction claims.
- **auditor confidence:** medium

### `wave_poisson_cinf_bridge_theorem_note_2026-05-28`

- **Note:** [`WAVE_POISSON_CINF_BRIDGE_THEOREM_NOTE_2026-05-28.md`](../../docs/WAVE_POISSON_CINF_BRIDGE_THEOREM_NOTE_2026-05-28.md)
- **claim_type:** `positive_theorem`
- **claim_scope:** Audited the self-contained discrete linear-algebra bridge that the Dirichlet 5-point Poisson solve is the unique static fixed point of the stated leapfrog wave operator, and that the finite-time undamped frozen-source snapshot tested by the harness is a transient-contaminated comparator rather than f*.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained**  (reason: `self`)
- **auditor:** `codex-cli-audit-ready-20260529-wave_poisson_cinf_bridge`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Setting f_next = f_curr = f_prev = f* in the leapfrog update gives 0 = h2(L f* + src), hence L f* = -src, and L is symmetric negative-definite so this solution is unique.  _(class `A`)_
- **chain closes:** True — The fixed-point identity follows algebraically from the stated update, and the note proves invertibility by negative-definiteness of the Dirichlet stencil. The modal analysis and runner source support the snapshot negative control without importing an unclosed external premise.
- **rationale:** The load-bearing step is a genuine algebraic closure over the operator stated in the packet, not a renaming or numerical match. The runner source actually constructs the Dirichlet Laplacian, solves the Poisson system, checks eigenvalues/residuals, simulates the damped and undamped recurrences, and verifies the modal closed form and harness snapshot gap. There are no upstream cited authorities whose retained status could downgrade the chain, and the numerical certificate is corroborative rather than the sole premise.
- **auditor confidence:** high

### `wave_radiation_note`

- **Note:** [`WAVE_RADIATION_NOTE.md`](../../docs/WAVE_RADIATION_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** For scripts/wave_radiation.py on NL=60, W=12, S0=0.04 and the stated offsets/frequencies, the finite-difference 2+1D scalar wave run produces nonzero detector peaks with log-log slope -0.469, drive-frequency DFT dominance at f=0.10, zero f=0 peak reference, and exact S0=0 beam null.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-judicial-third-wave-radiation-note-20260505`  (codex-gpt-5; independence=judicial_review)
- **load-bearing step:** Peak amplitudes over r = 2,4,6,8,10,12 give log-log slope = -0.469, with DFT peak at drive f = 0.10 and exact S0 = 0 null.  _(class `C`)_
- **chain closes:** True — The runner constructs the field by an explicit local finite-difference update with a sinusoidal monopole source and computes the detector peaks, slope, DFT magnitudes, and null cases from the simulated histories. The clean result is bounded to that finite numerical experiment; it does not ratify the note's broader asymptotic or full-classical-wave framing.
- **rationale:** The cached run completes with current output matching the note's peak table and slope -0.469; f=0.10 is the largest DFT magnitude at every listed detector; the f=0 reference peaks are zero; and the S0=0 beam null is exactly zero. The code computes these quantities from the finite-difference evolution rather than hard-coding the reported slope or detector amplitudes. Under hostile review this is a clean bounded theorem, not a positive theorem, because the evidence is for a fixed lattice size, finite time window, chosen source, offsets, and trial frequencies, and because no independent proof of the general far-field PDE asymptotic is in the restricted packet.
- **auditor confidence:** high

### `wave_static_boundary_sensitivity_note`

- **Note:** [`WAVE_STATIC_BOUNDARY_SENSITIVITY_NOTE.md`](../../docs/WAVE_STATIC_BOUNDARY_SENSITIVITY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded computational claim that, for the off-center frozen-source case H = 0.5 and z_phys = 3.0, increasing PW from 6.0 to 9.0 makes dS and rel_MS move by more than 5%.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260511-224519-a7679e61-wave_static_boundary_sen-023`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** Enlarging PW from 6.0 to 9.0 at shared H = 0.5 changes dS by 17.54% and rel_MS by 88.41%, so they are not preserved within 5%.  _(class `C`)_
- **chain closes:** True — The runner performs a finite-grid static Poisson solve and retarded/static propagation comparison at the stated H, source position, and PW values, then computes the relative moves reported in the note. The conclusion follows for this bounded computational case.
- **rationale:** The note makes a bounded negative stability claim, and the provided runner output matches the reported dS, rel_MS, residuals, and boundary-move percentages. The runner source does not merely print constants; it constructs the static solve, calls the wave/beam machinery, computes dM and dS, and derives rel_MS and relative moves from those values. No cited upstream authority is required for the narrow statement that this particular computation shows material finite-box sensitivity.
- **auditor confidence:** medium

### `wave_static_matrixfree_fixed_beam_boundary_note`

- **Note:** [`WAVE_STATIC_MATRIXFREE_FIXED_BEAM_BOUNDARY_NOTE.md`](../../docs/WAVE_STATIC_MATRIXFREE_FIXED_BEAM_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited the bounded computational claim that the provided matrix-free fixed-beam runner reports material static field-box sensitivity at H = 0.35 for field PW 6.0 versus 9.0 with fixed beam geometry.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260511-224519-a7679e61-wave_static_matrixfree_f-024`  (codex-gpt-5.5; independence=fresh_context)
- **load-bearing step:** At shared H = 0.35 with fixed beam PW = 6.0, enlarging only the field/static solve box from about 6.0 to 9.0 moves dS by 26.21% and rel_MS by 46.52% while dM moves only 0.57%.  _(class `C`)_
- **chain closes:** True — The runner source performs a matrix-free Poisson solve, crops the enlarged static field to the fixed beam box, computes wave/static beam responses, and reports the same movement figures quoted in the note. Within the restricted packet, the bounded conclusion follows from this completed run.
- **rationale:** The load-bearing result is a bounded first-principles computation over the provided discrete runner, not a definition, renaming, or external comparator match. The source code does not hard-code the quoted dM, dS, or rel_MS values; it computes them from the configured lattice parameters and solver path, and the cached stdout matches the note. The conclusion is scoped only to the stated H = 0.35 run, which the note explicitly acknowledges.
- **auditor confidence:** medium

### `wave_static_matrixfree_moving_source_fixed_beam_boundary_note`

- **Note:** [`WAVE_STATIC_MATRIXFREE_MOVING_SOURCE_FIXED_BEAM_BOUNDARY_NOTE.md`](../../docs/WAVE_STATIC_MATRIXFREE_MOVING_SOURCE_FIXED_BEAM_BOUNDARY_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Legacy audit row backfilled during scope-aware classification migration; re-audit may narrow this scope.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5; independence=cross_family)
- **load-bearing step:** At H = 0.35 with fixed beam geometry, the moving-source exact static comparator remains field-box sensitive, but the 9.0 -> 12.0 large-box branch shows low rel_MS and smaller dS movement without meeting the strict stability bar.  _(class `C`)_
- **chain closes:** True — The live runner reproduces both source-note comparisons: field PW 6.0 -> 9.0 and 9.0 -> 12.0. The note keeps the conclusion mixed and bounded, explicitly withholding continuum-quality promotion.
- **rationale:** The note accurately preserves both sides of the runner output. The 6.0 -> 9.0 comparison is still materially box-dependent, with dS move 20.84% and rel_MS move 86.21%, while dM is stable; the 9.0 -> 12.0 comparison improves to dS move 5.52% and rel_MS 3.18% -> 2.42% but still does not pass a strict stability criterion. This closes only the stated mixed diagnostic: no boundary-stable moving-source comparator is retained yet, but the medium-H large-box branch remains a plausible stabilization candidate.
- **auditor confidence:** high

### `wave_static_matrixfree_shared_geometry_compare_note`

- **Note:** [`WAVE_STATIC_MATRIXFREE_SHARED_GEOMETRY_COMPARE_NOTE.md`](../../docs/WAVE_STATIC_MATRIXFREE_SHARED_GEOMETRY_COMPARE_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Audited only the bounded finite-table engine comparison between the direct static Poisson solver and the matrix-free static solver at H=0.35 and H=0.25 with z_phys=3.0.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T210853Z-107330f9-wave_static_matrixfree_s-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner computes direct and matrix-free finite-grid static fields on the same shared geometries and reports max field mismatch and propagated beam-response mismatch showing close finite-table agreement, while explicitly not asserting identity or residual-tied equivalence.  _(class `C`)_
- **chain closes:** True — The primary runner genuinely computes both static fields and the beam-side propagated responses, then validates the quoted frozen rows within explicit tolerances. The note's narrowed conclusion is only close finite-table agreement, not a formal drop-in replacement theorem.
- **rationale:** The source note no longer overclaims algorithmic identity or a residual-tied drop-in replacement theorem. The runner source instantiates the finite grid, solves the direct and matrix-free static Poisson problems, propagates both through the same beam setup, and checks the recorded H=0.35 and H=0.25 rows against frozen expected values. The remaining large rel_MS mismatch is correctly scoped as comparator science rather than engine equivalence.
- **auditor confidence:** medium

### `weak_coupling_retention_note_2026-04-11`

- **Note:** [`WEAK_COUPLING_RETENTION_NOTE_2026-04-11.md`](../../docs/WEAK_COUPLING_RETENTION_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Frozen finite 60-run audit surface over random geometric, growing, and layered cycle graph families at the listed sizes, seeds 42..46, and G=5,10, checking shell-margin and norm-conservation counts only.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260525T113653Z-566a2aee-weak_coupling_retention_-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** At weak coupling (G=5,10), on the declared finite audit surface, attractive parity coupling has tw_a - tw_r >= 10 on 60/60 audited runs and exact norm conservation on 60/60 runs.  _(class `C`)_
- **chain closes:** True — The supplied runner source genuinely constructs the declared graph instances, evolves attractive, repulsive, and free cases, computes shell TOWARD counts and norms, and the cached stdout reports shell margin >= 10 and norm conserved on 60/60 runs. The note explicitly excludes broader graph-family, coordinate-force, and stable spectral-gap inferences from binding scope.
- **rationale:** For the narrowed claim, the load-bearing evidence is a bounded finite computation, not a theorem over all admissible irregular graphs. The runner source does not hard-code the retained counts or import them from another note; it computes the graph instances, evolution, shell-force counts, and norm checks directly on the declared surface. The live-stale spectral-gap row and wrong registered runner path are acknowledged as out of scope, so they do not block the narrowed shell-margin/norm finite-surface claim.
- **auditor confidence:** high

### `wide_lattice_h2t_distance_law_note`

- **Note:** [`WIDE_LATTICE_H2T_DISTANCE_LAW_NOTE.md`](../../docs/WIDE_LATTICE_H2T_DISTANCE_LAW_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Bounded finite-slice replay for the ordered 3D 1/L^2 wide lattice at h=0.25, W=12, L=12, with valley-linear action, showing attractive distance rows, near-Newtonian far tail, and linear source-strength scaling.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260608-200219-9f2938ffdc-wide_lattice_h2t_distance_la`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Independent wide replay at h = 0.25, W = 12, L = 12 gives 10/10 TOWARD distance support, far-tail slope near -1, and F~M exponent 1.000.  _(class `C`)_
- **chain closes:** True — The runner source contains a genuine lattice replay path for the stated geometry/action/kernel, and the default verifier SHA-pins the frozen replay log, parses all raw rows, and checks their inclusion in the note. An independent log-log regression from the embedded rows reproduces the advertised peak-tail, far-tail, and F~M exponents.
- **rationale:** The scoped claim is finite and bounded, not a continuum or universal distance-law theorem. The exposed raw distance and F~M rows support the stated signs and fitted exponents, and the primary/helper runner source does not merely print constants or import the contested conclusion. No cited authority, external comparator, or open bridge is needed for this narrow replay claim.
- **auditor confidence:** high

### `wide_lattice_h2t_skeptic_audit_note`

- **Note:** [`WIDE_LATTICE_H2T_SKEPTIC_AUDIT_NOTE.md`](../../docs/WIDE_LATTICE_H2T_SKEPTIC_AUDIT_NOTE.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** A bounded W=12, h=0.25 ordered 3D 1/L^2 wide-lattice h^2+T replay with positive distance rows, near-Newtonian far-tail fit, and linear F~M sweep, without continuum or universal-asymptotic promotion.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260608-213932-5a01ac8cb2-wide_lattice_h2t_skeptic_aud`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The replay is genuinely clean on the tested wide slice, which is enough to retain it only as a finite-lattice replay and not as a universal distance law.  _(class `A`)_
- **chain closes:** True — The raw distance and F~M rows in the retained_bounded cited authority algebraically reproduce the reported signs, counts, far-tail slope, R^2, and mass-scaling exponent. The source note explicitly limits the result to the tested finite-lattice slice.
- **rationale:** The load-bearing audit math is an algebraic closure over retained-grade packet inputs: row sign counts and independent log-log fits reproduce the displayed numerical claims. The cited upstream note is marked retained_bounded, which is retained-grade under the rubric. The source note does not import the missing continuum, width-independence, detector-window, or geometry-generic controls as conclusions.
- **auditor confidence:** high

### `wigner_mode_low_d_sublattice_theorem_note_2026-05-02`

- **Note:** [`WIGNER_MODE_LOW_D_SUBLATTICE_THEOREM_NOTE_2026-05-02.md`](../../docs/WIGNER_MODE_LOW_D_SUBLATTICE_THEOREM_NOTE_2026-05-02.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite charge-commutation and Gibbs-state commutation in the generated symmetric Hamiltonian, plus finite L=16 to L=32 IR-sum increase for the stated nearest-neighbor dispersion in d=1 and d=2; no no-SSB or Noether bridge is audited.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260609-114701-877d26d67a-wigner_mode_low_d_sublattice`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The source-side retained-eligible content is only the finite algebra and finite IR-growth diagnostics that the runner computes directly.  _(class `C`)_
- **chain closes:** True — For the scoped finite claim, the runner constructs Q diagonal by occupation number and H only within equal-charge blocks, so [Q,H]=0 and exp(-beta H)/Tr exp(-beta H) preserves the same sectors. An independent check using omega=4 sum sin^2(pi n/L) reproduces the quoted IR values and strict growth from L=16 to L=32 in d=1 and d=2.
- **rationale:** The displayed matrix identities and finite numerical table entries match both the runner source and an independent recomputation: I_1 gives 1.328125 and 2.6640625, and I_2 gives approximately 0.4899245 and 0.6003262. The runner does not hard-code the contested outputs or import a cross-note premise; it constructs the finite symmetric block Hamiltonian and directly computes the Gibbs commutator and lattice sums. The stronger low-dimensional no-SSB and Noether-current bridges are explicitly excluded as non-claims, so the bounded conclusion does not depend on those open bridges.
- **auditor confidence:** high

### `wilson_two_body_open_note_2026-04-11`

- **Note:** [`WILSON_TWO_BODY_OPEN_NOTE_2026-04-11.md`](../../docs/WILSON_TWO_BODY_OPEN_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite open-boundary Wilson two-orbital Hartree simulations at side=11,13, G=5, mu^2=0.22, d=3..6, plus the in-packet post-selected distance/partner-source law fits and side=13 screening-mass alpha sweep; periodic and both-masses Newton-closure rows are excluded.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-per-site-k1-20260524T172711Z-cd15ba56-wilson_two_body_open_not-01`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** Open-boundary Wilson two-orbital Hartree dynamics produces a robust mutual attraction channel on the audited G=5, mu^2=0.22 surface, with a post-selected screened falloff |a_mut| ~ d^-3.4, sublinear partner-source scaling |a_mut| ~ m_B^0.48, and screening-mass softening toward Newton-compatible exponents.  _(class `C`)_
- **chain closes:** True — The supplied runner source constructs the open lattice, Poisson solve, Wilson Hamiltonian, mode controls, acceleration readout, and screening alpha fits directly, and the supplied helper source/cache computes the post-selected distance and partner-source characterizations from the same base runner. This closes only the bounded finite-surface attraction and characterization claim, not a full Newton or action-reaction theorem.
- **rationale:** For the narrowed scope, the computation is first-principles within the packet rather than a definition substitution or external numerical comparator. The primary runner reports all 8 open-boundary rows attractive and clean, and its screening sweep passes 11/11 checks with no failures. The inlined law helper computes the quoted post-selected power-law and partner-source fits through base.run_config/base.label. The note explicitly prevents promoting the periodic-box and both-masses diagnostics into load-bearing Newton closure.
- **auditor confidence:** high

### `wilson_two_body_open_refined_note_2026-04-11`

- **Note:** [`WILSON_TWO_BODY_OPEN_REFINED_NOTE_2026-04-11.md`](../../docs/WILSON_TWO_BODY_OPEN_REFINED_NOTE_2026-04-11.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Registered open-boundary Wilson two-body refined sweep for sides 11,13,15,17,19 at fixed G=5 and mu^2=0.22, using the declared clean-attractive subset fit: 25/25 ATTRACT+CLEAN, global exponent -3.669 with R^2=0.9896, per-side exponents -3.139,-3.313,-3.500,-3.671,-3.837; excludes universal law claims, unscreened/Newtonian crossover claims, and blind-law estimation over rejected rows.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-audit-loop`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** On the clean attractive subset of the fixed G=5, mu^2=0.22 open-boundary Wilson two-orbital sweep, all 25 configurations are ATTRACT and CLEAN and the global fit is |a_mut| ~ d^-3.669 with R^2=0.9896.  _(class `C`)_
- **chain closes:** True — The runner recomputes all 25 configurations and asserts the aggregate counts, global exponent/R^2, per-side exponents, and steeper-than-Newton fixed-surface check against the note's quoted values. The note's screening addendum correctly prevents reading this as a screening-independent universality class.
- **rationale:** The bounded claim closes because the live runner and SHA-pinned cache reproduce the 25-run fixed-surface sweep and assert every quoted fit used by the note. The note explicitly labels the fit as post-selected on clean attractive rows and narrows interpretation with the later screening addendum, so no hidden universal Newton-law or screening-independent claim is being retained. Residual risk is limited to future misuse outside fixed G=5, mu^2=0.22 or outside the declared post-selected methodology.
- **auditor confidence:** high

### `within_sector_ess_adequacy_conclusion_survives_bounded_theorem_note_2026-06-12`

- **Note:** [`WITHIN_SECTOR_ESS_ADEQUACY_CONCLUSION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-06-12.md`](../../docs/WITHIN_SECTOR_ESS_ADEQUACY_CONCLUSION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite L=3, k=3 prefix-sector ESS adequacy for seeds 4242@9, 99@7, and 7@4, with ESS >= 8 and a fixed seeded 300-draw permutation-null p95 diagnostic for delta = |ch2| - |ch1|^4.
- **audit_status:** ~~audited_clean~~
- **effective_status:** **retained_bounded**  (reason: `self`)
- **auditor:** `codex-cli-gpt-5.5-20260614-011046-d4a50e0aeb-within_sector_ess_adequacy_c`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** With ESS = (sum w)^2/sum w^2 and ESS >= 8, 16/24 sectors survive, seed 7 is untested, and the two surviving seeded records stay below their fixed 300-draw permutation-null p95 diagnostics.  _(class `C`)_
- **chain closes:** True — The runner source constructs the finite operator system, branch weights, sector moments, ESS values, and permutation-null diagnostics directly rather than reading the contested numbers from another note. Independent arithmetic checks on the displayed table support the 16/24 adequacy count and the two record-versus-null inequalities within the stated finite diagnostic scope.
- **rationale:** The load-bearing result is a bounded first-principles finite computation, not a renaming or external comparator match. The hard-coded constants fix the experiment, seeds, depths, ESS threshold, and null draw count; the adequacy pattern, weighted records, and p95 diagnostics are computed from the finite branch data. The conclusion is clean only in the stated bounded sense: it does not prove an all-permutations null theorem or a broader unseeded within-sector claim.
- **auditor confidence:** high

### `yt_boundary_bc_transfer_uniqueness_narrow_theorem_note_2026-05-17`

- **Note:** [`YT_BOUNDARY_BC_TRANSFER_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17.md`](../../docs/YT_BOUNDARY_BC_TRANSFER_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17.md)
- **claim_type:** `bounded_theorem`
- **claim_scope:** Finite-grid numerical diagnostics T1-T5 for the coded backward-RGE map on X in [0.5,1.2], conditional on admitted implementation inputs I1-I5.
- **audit_status:** ~~audited_conditional~~
- **effective_status:** ~~audited_conditional~~  (reason: `terminal_audit`)
- **auditor:** `codex-cli-gpt-5.5-20260621-095023-923e9318-yt_boundary_bc_transfer_uniqueness_narrow_theorem_note_2026-05-17-first`  (codex-gpt-5.5; independence=cross_family)
- **load-bearing step:** The runner integrates the coded two-loop SM RGE map Phi(X)=y_t(M_Pl) and verifies finite trajectories, 33-point grid monotonicity, finite observed slopes, bracketed brentq root stability, and extension-scan onset on X in [0.5,1.2].  _(class `D`)_
- **chain closes:** False — The runner source does perform the stated finite-grid solve_ivp/brentq checks and the cache reports 31 PASS, 0 FAIL. The retained chain does not close because the plaquette constants, Ward target, RGE/threshold procedure, fixed thresholds, and EW initial-condition surface are admitted inputs rather than derived or supplied by retained authorities in the restricted packet.
- **rationale:** Issue: the audited result is a reproducible finite-grid diagnostic over admitted implementation inputs, not a derivation of those inputs. Why this blocks: without retained derivations or dependency edges for I1-I5, the row cannot be promoted to a retained boundary-transfer theorem even though the narrow computation appears internally consistent. Repair target: add retained-grade authorities or self-contained derivations for the plaquette constants, Ward target, RGE normalization/threshold procedure, threshold scales, and EW surface. Claim boundary until fixed: the safe statement is the conditional finite-grid runner diagnostic only.
- **auditor confidence:** high

### `yukawa_color_projection_theorem`

- **Note:** [`YUKAWA_COLOR_PROJECTION_THEOREM.md`](../../docs/YUKAWA_COLOR_PROJECTION_THEOREM.md)
- **claim_type:** `decoration`
- **claim_scope:** Pure SU(N_c) representation channel counting: N_c tensor N_c-bar decomposes as singlet plus adjoint, giving f_adj,dim = (N_c^2 - 1)/N_c^2 and 8/9 at N_c = 3, with no dynamical trace or physical Yukawa matching claim.
- **audit_status:** ~~audited_decoration~~
- **effective_status:** `decoration_under_graph_first_su3_integration_note`  (reason: `decoration_parent_retained`)
- **auditor:** `codex-judicial-panel-per-site-k1-20260525T101849Z-yukawa_color_projection_theorem-majority`  (codex-gpt-5.5; independence=judicial_review)
- **load-bearing step:** The color bilinear representation decomposes as N_c tensor N_c-bar = 1 plus adj, so the adjoint representation-dimension fraction is (N_c^2 - 1)/N_c^2 and equals 8/9 at N_c = 3.  _(class `A`)_
- **chain closes:** False — Five-judge panel majority 5/5 ratified the second tuple (audited_decoration, decoration, class A). Vote breakdown: J1: second / audited_decoration / decoration / class A; J2: second / audited_decoration / decoration / class A; J3: second / audited_decoration / decoration / class A; J4: second / audited_decoration / decoration / class A; J5: second / audited_decoration / decoration / class A. Majority rationale: The load-bearing step is a genuine class A algebraic identity and dimension count, and the runner source checks real SU(N) generator normalization, Fierz completeness, exact fractions, and the narrowed non-physical boundary. There are zero external comparator checks and no imported open physical matching bridge inside the scoped claim. Under the rubric's clean-vs-decoration tie-breaker, this is better classified as audited_decoration because the audited content is a standard-math channel-counting consequence over the retained graph-first SU(3) color substrate, not a new physical theorem. | The load-bearing step is class A finite-dimensional SU(N_c) representation algebra and dimension counting. The scoped claim closes because the retained graph-first SU(3) surface supplies N_c = 3, while the Fierz authority's open EW matching rule is explicitly outside the claim boundary. Under the rubric's clean-vs-decoration tie-break, this is best treated as an algebraic decoration: there are no external comparator checks, no new physical matching theorem, and the row packages a standard mathematical corollary under the retained SU(3) color substrate. | The load-bearing step is standard finite-dimensional SU(N_c) representation algebra and dimension counting, with zero external comparator checks and no physical matching bridge imported. The only framework-specific input needed for the scoped numerical value is the retained graph-first SU(3) color surface supplying N_c = 3; the Fierz authority's open EW matching rule is explicitly outside this row's scope. Under the clean-vs-decoration tie-break, this is better classified as an algebraic decoration than as a new positive theorem. | The load-bearing step is class A: standard SU(N_c) representation decomposition plus dimension counting, with N_c = 3 supplied by the retained graph-first SU(3) surface. The packet contains no external comparator checks and no physical matching step; the note explicitly excludes dynamical trace, Higgs normalization, Yukawa correction, and top-mass claims. Under the tie-break rule, a zero-D algebraic consequence of a retained parent plus standard mathematics is audited_decoration rather than audited_clean. | The load-bearing step is a standard algebraic SU(N_c) representation decomposition and dimension count, and the runner performs real generator-normalization, Fierz, and rational fraction checks with zero external comparator checks. The only framework-specific retained input needed for the scoped numerical specialization is the graph-first SU(3) / N_c = 3 surface; the open EW matching rule is explicitly excluded from the claim. Under the rubric tie-break, this is an algebraic decoration rather than a new positive physical theorem.
- **rationale:** Five-judge panel majority 5/5 ratified the second tuple (audited_decoration, decoration, class A). Vote breakdown: J1: second / audited_decoration / decoration / class A; J2: second / audited_decoration / decoration / class A; J3: second / audited_decoration / decoration / class A; J4: second / audited_decoration / decoration / class A; J5: second / audited_decoration / decoration / class A. Majority rationale: The load-bearing step is a genuine class A algebraic identity and dimension count, and the runner source checks real SU(N) generator normalization, Fierz completeness, exact fractions, and the narrowed non-physical boundary. There are zero external comparator checks and no imported open physical matching bridge inside the scoped claim. Under the rubric's clean-vs-decoration tie-breaker, this is better classified as audited_decoration because the audited content is a standard-math channel-counting consequence over the retained graph-first SU(3) color substrate, not a new physical theorem. | The load-bearing step is class A finite-dimensional SU(N_c) representation algebra and dimension counting. The scoped claim closes because the retained graph-first SU(3) surface supplies N_c = 3, while the Fierz authority's open EW matching rule is explicitly outside the claim boundary. Under the rubric's clean-vs-decoration tie-break, this is best treated as an algebraic decoration: there are no external comparator checks, no new physical matching theorem, and the row packages a standard mathematical corollary under the retained SU(3) color substrate. | The load-bearing step is standard finite-dimensional SU(N_c) representation algebra and dimension counting, with zero external comparator checks and no physical matching bridge imported. The only framework-specific input needed for the scoped numerical value is the retained graph-first SU(3) color surface supplying N_c = 3; the Fierz authority's open EW matching rule is explicitly outside this row's scope. Under the clean-vs-decoration tie-break, this is better classified as an algebraic decoration than as a new positive theorem. | The load-bearing step is class A: standard SU(N_c) representation decomposition plus dimension counting, with N_c = 3 supplied by the retained graph-first SU(3) surface. The packet contains no external comparator checks and no physical matching step; the note explicitly excludes dynamical trace, Higgs normalization, Yukawa correction, and top-mass claims. Under the tie-break rule, a zero-D algebraic consequence of a retained parent plus standard mathematics is audited_decoration rather than audited_clean. | The load-bearing step is a standard algebraic SU(N_c) representation decomposition and dimension count, and the runner performs real generator-normalization, Fierz, and rational fraction checks with zero external comparator checks. The only framework-specific retained input needed for the scoped numerical specialization is the graph-first SU(3) / N_c = 3 surface; the open EW matching rule is explicitly excluded from the claim. Under the rubric tie-break, this is an algebraic decoration rather than a new positive physical theorem.
- **decoration parent:** `graph_first_su3_integration_note`
- **auditor confidence:** judicial_panel_majority
