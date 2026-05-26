# Audit Queue

**Total pending:** 1288
**Ready (all deps already at retained-grade or metadata tiers):** 68

By criticality:
- `critical`: 268
- `high`: 359
- `medium`: 334
- `leaf`: 327

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `parity_operator_basis_dimension5_lv_no_go_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 889 | 10.30 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_parity_dim5_formal_sign_repair.py` |
| 2 | `axiom_first_reflection_positivity_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 887 | 26.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_reflection_positivity_check.py` |
| 3 | `strong_cp_theta_zero_note` | bounded_theorem | unaudited | critical | 879 | 19.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_strong_cp_theta_zero.py` |
| 4 | `assumption_derivation_ledger` | bounded_theorem | unaudited | critical | 879 | 13.78 | Y | fresh_context_or_stronger_with_cross_confirmation | - |
| 5 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 878 | 13.78 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py` |
| 6 | `g_bare_rigidity_theorem_note` | bounded_theorem | unaudited | critical | 875 | 13.28 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rigidity_theorem.py` |
| 7 | `plaquette_self_consistency_note` | bounded_theorem | unaudited | critical | 749 | 30.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py` |
| 8 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 723 | 53.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 9 | `pl_topology_infrastructure_textbook_import_note_2026-05-17` | bounded_theorem | unaudited | critical | 703 | 10.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pl_topology_finite_cone_cap_certificate.py` |
| 10 | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 696 | 19.45 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py` |
| 11 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 693 | 10.44 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |
| 12 | `hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25` | bounded_theorem | unaudited | critical | 630 | 9.80 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/hypercharge_alpha_third_normalization_runner.py` |
| 13 | `yt_ew_color_projection_theorem` | no_go | unaudited | critical | 554 | 34.12 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/yt_ew_kappa_family_nogo_certificate.py` |
| 14 | `higgs_mechanism_note` | bounded_theorem | unaudited | critical | 470 | 11.88 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_higgs_quartic_mechanism_algebra_repair.py` |
| 15 | `pmns_oriented_cycle_selection_structure_note` | bounded_theorem | unaudited | critical | 391 | 10.62 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_pmns_oriented_cycle_selection_structure.py` |
| 16 | `dm_leptogenesis_pmns_projector_interface_note_2026-04-16` | bounded_theorem | unaudited | critical | 375 | 16.55 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py` |
| 17 | `dm_leptogenesis_pmns_analytic_stationary_classification_theorem_note_2026-04-16` | bounded_theorem | unaudited | critical | 352 | 9.46 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_dm_pmns_he_parity_repair.py` |
| 18 | `charged_lepton_koide_note_2026-04-18` | open_gate | unaudited | critical | 283 | 15.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_charged_lepton_koide_two_gate_open_certificate.py` |
| 19 | `staggered_fermion_card_2026-04-11` | bounded_theorem | unaudited | critical | 280 | 11.63 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_17card_finite_scope_repair.py` |
| 20 | `g_bare_hilbert_schmidt_rigidity_theorem_note_2026-05-07` | positive_theorem | unaudited | critical | 207 | 21.70 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_audit_residual_closure.py` |
| 21 | `gate_b_farfield_note` | bounded_theorem | unaudited | critical | 122 | 14.44 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/gate_b_farfield_harness.py` |
| 22 | `emergent_lorentz_invariance_note` | bounded_theorem | unaudited | critical | 888 | 19.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_emergent_lorentz_invariance.py` |
| 23 | `lorentz_boost_covariance_2d_theorem_note` | positive_theorem | unaudited | critical | 885 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_2d.py` |
| 24 | `staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05` | positive_theorem | unaudited | critical | 878 | 10.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py` |
| 25 | `microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 877 | 11.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/microcausality_finite_range_h_bridge_2026_05_09.py` |
| 26 | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 876 | 17.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_cluster_decomposition_check.py` |
| 27 | `light_cone_crank_nicolson_lieb_robinson_bridge_note_2026-05-09` | bounded_theorem | unaudited | critical | 876 | 10.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_crank_nicolson_lr_2026_05_09.py` |
| 28 | `light_cone_framing_note` | positive_theorem | unaudited | critical | 875 | 11.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/light_cone_staggered_dispersion.py` |
| 29 | `axiom_first_spectrum_condition_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 874 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spectrum_condition_check.py` |
| 30 | `lorentz_boost_covariance_3plus1d_theorem_note` | positive_theorem | unaudited | critical | 874 | 14.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_boost_3plus1d.py` |
| 31 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem | unaudited | critical | 874 | 10.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_canonical_convention_narrow.py` |
| 32 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 873 | 15.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 33 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem | unaudited | critical | 873 | 13.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_two_ward_closure.py` |
| 34 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 872 | 19.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 35 | `axiom_first_spin_statistics_theorem_note_2026-04-29` | positive_theorem | unaudited | critical | 871 | 12.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_spin_statistics_check.py` |
| 36 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | positive_theorem | unaudited | critical | 870 | 19.27 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 37 | `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 866 | 13.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_grassmann_forcing_dependency_chain.py` |
| 38 | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 864 | 17.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_kawamoto_smit_phase_forcing.py` |
| 39 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 848 | 38.23 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 40 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 711 | 37.98 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_zero_import_chain.py` |
| 41 | `s3_cap_uniqueness_note` | bounded_theorem | unaudited | critical | 702 | 19.96 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 42 | `s3_general_r_derivation_note` | positive_theorem | unaudited | critical | 696 | 18.45 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_cap_uniqueness.py` |
| 43 | `three_generation_structure_note` | bounded_theorem | unaudited | critical | 693 | 30.44 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_generation_fermi_point.py` |
| 44 | `s3_time_theta_to_slice_coupling_note` | open_gate | unaudited | critical | 692 | 10.94 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 45 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 690 | 12.43 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 46 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 656 | 25.86 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 47 | `hypercharge_identification_note` | bounded_theorem | unaudited | critical | 629 | 18.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hypercharge_identification.py` |
| 48 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 621 | 13.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 49 | `yt_boundary_theorem` | open_gate | unaudited | critical | 619 | 15.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 50 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 615 | 27.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |

## Citation cycle break targets

3 citation cycles in the graph. Each cycle permanently blocks every member from `retained` until one node is re-audited with explicit cycle-break instructions or a 'see also' edge is stripped. Top 25 below; full list in `data/audit_queue.json` under `cycle_break_targets`.

| # | cycle_id | length | max_desc | primary break target | criticality | audit_status |
|---:|---|---:|---:|---|---|---|
| 1 | `cycle-0001` | 2 | 7 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |
| 2 | `cycle-0002` | 2 | 7 | `yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25` | medium | unaudited |
| 3 | `cycle-0003` | 3 | 7 | `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` | high | unaudited |

Full queue lives in `data/audit_queue.json`.
