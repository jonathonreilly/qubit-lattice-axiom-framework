# Audit Queue

**Total pending:** 1236
**Ready (all deps already at retained-grade or metadata tiers):** 90

By criticality:
- `critical`: 315
- `high`: 247
- `medium`: 303
- `leaf`: 371

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | bounded_theorem | audit_in_progress | critical | 768 | 20.59 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_z3_equivariant_anticommuting_no_go.py` |
| 2 | `generation_degeneracy_minimal_symmetry_breaking_narrow_theorem_note_2026-05-23` | bounded_theorem | audit_in_progress | critical | 763 | 13.58 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_degeneracy_minimal_breaking_discriminator.py` |
| 3 | `charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 762 | 17.58 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_charged_lepton_koide_cone_algebraic.py` |
| 4 | `parity_violation_does_not_reach_generation_triplet_narrow_theorem_note_2026-05-23` | bounded_theorem | audit_in_progress | critical | 762 | 14.58 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_parity_violation_vs_generation_triplet_discriminator.py` |
| 5 | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem | audit_in_progress | critical | 759 | 18.57 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/per_site_su2_spin_half_check.py` |
| 6 | `new_parity_is_circulant_phase_narrow_theorem_note_2026-05-23` | bounded_theorem | audit_in_progress | critical | 754 | 15.06 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_new_parity_is_circulant_phase_discriminator.py` |
| 7 | `axiom_first_z_n_equivariant_spectral_asymmetry_narrow_theorem_note_2026-05-26` | bounded_theorem | audit_in_progress | critical | 752 | 13.56 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py` |
| 8 | `three_generation_observable_m3c_burnside_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 751 | 15.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_generation_observable_m3c_burnside_narrow.py` |
| 9 | `koide_aps_block_by_block_forcing_note_2026-04-21` | bounded_theorem | audit_in_progress | critical | 748 | 13.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_aps_block_by_block_forcing.py` |
| 10 | `flavor_r_half_is_the_records_flow_separatrix_2026-06-02` | bounded_theorem | unaudited | critical | 748 | 11.05 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_r_half_is_the_records_flow_separatrix_2026_06_02.py` |
| 11 | `flavor_r_half_stable_under_thermalizing_arrow_2026-06-02` | bounded_theorem | unaudited | critical | 748 | 11.05 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_r_half_stable_under_thermalizing_arrow_2026_06_02.py` |
| 12 | `flavor_carrier_from_axioms_momentum_forced_2026-05-31` | bounded_theorem | unaudited | critical | 746 | 10.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_carrier_from_axioms_momentum_forced_2026_05_31.py` |
| 13 | `flavor_r_half_is_a_stationary_point_not_forced_2026-06-02` | bounded_theorem | unaudited | critical | 746 | 10.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/flavor_r_half_is_a_stationary_point_not_forced_2026_06_02.py` |
| 14 | `koide_kappa_two_orbit_dimension_factorization_note_2026-04-19` | bounded_theorem | audit_in_progress | critical | 746 | 10.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_kappa_two_orbit_dimension_factorization.py` |
| 15 | `lepton_brannen_bae_delta_two_ninths_open_gate_note_2026-05-26` | open_gate | audit_in_progress | critical | 746 | 10.04 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.py` |
| 16 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 970 | 29.92 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py` |
| 17 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 964 | 19.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 18 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 964 | 11.91 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 19 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 961 | 20.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 20 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 959 | 20.41 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 21 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 958 | 12.90 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 22 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 957 | 13.40 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 23 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 951 | 14.39 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 24 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 946 | 18.89 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 25 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 929 | 39.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 26 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 869 | 38.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 27 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 847 | 26.73 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 28 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 834 | 28.71 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 29 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 811 | 14.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 30 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 811 | 12.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 31 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 811 | 12.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 32 | `yt_boundary_theorem` | open_gate | unaudited | critical | 809 | 16.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 33 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 809 | 14.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 34 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 806 | 17.66 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 35 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 805 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 36 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 804 | 11.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 37 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 803 | 14.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 38 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 803 | 10.65 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 39 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 802 | 28.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 40 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 802 | 11.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 41 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 801 | 16.15 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |
| 42 | `yt_bridge_rearrangement_principle_note` | bounded_theorem | unaudited | critical | 799 | 13.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_rearrangement_principle.py` |
| 43 | `yt_bridge_action_invariant_note` | bounded_theorem | unaudited | critical | 798 | 12.14 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_action_invariant.py` |
| 44 | `yt_bridge_moment_closure_note` | bounded_theorem | unaudited | critical | 797 | 12.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_moment_closure.py` |
| 45 | `yt_bridge_hessian_selector_note` | bounded_theorem | unaudited | critical | 796 | 14.64 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_hessian_selector.py` |
| 46 | `yt_bridge_higher_order_corrections_note` | bounded_theorem | unaudited | critical | 794 | 13.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_higher_order_corrections.py` |
| 47 | `yt_bridge_nonlocal_corrections_note` | bounded_theorem | unaudited | critical | 794 | 13.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_nonlocal_corrections.py` |
| 48 | `yt_bridge_endpoint_shift_bound_note` | bounded_theorem | unaudited | critical | 790 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_endpoint_shift_bound.py` |
| 49 | `yt_bridge_uv_class_uniqueness_note` | bounded_theorem | unaudited | critical | 790 | 11.13 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_uv_class_uniqueness.py` |
| 50 | `yt_exact_coarse_grained_bridge_operator_note` | bounded_theorem | unaudited | critical | 789 | 11.63 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_exact_coarse_grained_bridge_operator.py` |

## Citation cycle break targets

29 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 2 | `cycle-0002` | 7 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 3 | `cycle-0003` | 9 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 4 | `cycle-0004` | 14 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 5 | `cycle-0005` | 14 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 6 | `cycle-0006` | 14 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 7 | `cycle-0007` | 15 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 8 | `cycle-0008` | 17 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 9 | `cycle-0009` | 18 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 10 | `cycle-0010` | 18 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 11 | `cycle-0011` | 19 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 12 | `cycle-0012` | 19 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 13 | `cycle-0013` | 19 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 14 | `cycle-0014` | 20 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 15 | `cycle-0015` | 20 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 16 | `cycle-0016` | 20 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 17 | `cycle-0017` | 20 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 18 | `cycle-0018` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 19 | `cycle-0019` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 20 | `cycle-0020` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 21 | `cycle-0021` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 22 | `cycle-0022` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 23 | `cycle-0023` | 21 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 24 | `cycle-0024` | 22 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |
| 25 | `cycle-0025` | 23 | 745 | `admitted_input_registry_tier_a_note_2026-05-23` | critical | unaudited |

Full queue lives in `data/audit_queue.json`.
