# Audit Queue

**Total pending:** 1540
**Ready (all deps at retained-grade/metadata tiers or accepted premises: axiom/primitive nodes and Tier-A admitted derivation targets):** 92

By criticality:
- `critical`: 305
- `high`: 287
- `medium`: 466
- `leaf`: 482

Auditor (current best Codex GPT model at maximum reasoning by default) should pull from the top of this list. Critical claims require cross-confirmation by a second independent clean-room auditor before `audited_clean` lands.

## Top 50

| # | claim_id | claim_type | reason | criticality | desc | score | ready | indep required | runner |
|---:|---|---|---|---|---:|---:|:---:|---|---|
| 1 | `g_bare_constraint_vs_convention_theorem_note_2026-05-03` | bounded_theorem | unaudited | critical | 963 | 16.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_constraint_surface_check.py` |
| 2 | `p_flux_selection_via_fsb_k_and_z_certificate_conditional_theorem_note_2026-06-11` | bounded_theorem | unaudited | critical | 929 | 14.86 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/p_flux_selection_via_fsb_k_check_2026_06_11.py` |
| 3 | `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | bounded_theorem | unaudited | critical | 926 | 26.36 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_single_clock_codimension1_evolution_check.py` |
| 4 | `lorentz_kernel_positive_closure_note` | positive_theorem | unaudited | critical | 912 | 19.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_lorentz_kernel_positive_closure.py` |
| 5 | `real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08` | bounded_theorem | unaudited | critical | 902 | 16.32 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py` |
| 6 | `staggered_dirac_bz_corner_forcing_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 894 | 36.31 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_bz_corner_decomposition.py` |
| 7 | `quark_route2_exact_time_coupling_note_2026-04-19` | positive_theorem | unaudited | critical | 887 | 20.79 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_exact_time_coupling.py` |
| 8 | `yt_p1_i_s_lattice_pt_citation_note_2026-04-17` | bounded_theorem | unaudited | critical | 680 | 16.91 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_p1_i_s_reaudit_packet_2026_06_12.py` |
| 9 | `higgs_channel_effective_ntaste_boundary_bounded_note_2026-05-08` | bounded_theorem | unaudited | critical | 641 | 16.83 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_higgs_channel_effective_ntaste_boundary.py` |
| 10 | `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` | bounded_theorem | unaudited | critical | 512 | 18.50 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_g_bare_rescaling_conditional_algebra_check.py` |
| 11 | `axiom_first_kms_condition_theorem_note_2026-05-01` | positive_theorem | unaudited | critical | 379 | 16.57 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_kms_condition_check.py` |
| 12 | `su3_casimir_fundamental_theorem_note_2026-05-02` | bounded_theorem | unaudited | critical | 357 | 20.98 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/su3_casimir_fundamental_check.py` |
| 13 | `cl3_quark_antiquark_color_singlet_theorem_note_2026-05-02` | positive_theorem | unaudited | critical | 313 | 14.29 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_quark_antiquark_color_singlet_check.py` |
| 14 | `higgs_mass_from_axiom_status_correction_audit_note_2026-05-02` | open_gate | unaudited | critical | 284 | 15.15 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_higgs_mass_status_audit.py` |
| 15 | `hierarchy_formula_honest_status_note_2026-05-10` | bounded_theorem | unaudited | critical | 261 | 21.53 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_formula_honest_status.py` |
| 16 | `u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17` | bounded_theorem | audit_in_progress | critical | 260 | 14.03 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_u0_plaquette_quartic_derivation.py` |
| 17 | `clifford_chirality_dimension_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | critical | 257 | 13.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_clifford_chirality_dimension_narrow.py` |
| 18 | `higgs_lattice_taste_count_and_wj_form_bridge_narrow_theorem_note_2026-06-05` | bounded_theorem | audit_in_progress | critical | 256 | 13.01 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_higgs_lattice_taste_count_wj_form_2026_06_05.py` |
| 19 | `koide_mru_weight_class_obstruction_theorem_note_2026-04-19` | bounded_theorem | unaudited | critical | 238 | 20.40 | Y | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_koide_mru_weight_class_obstruction_theorem.py` |
| 20 | `anomaly_forces_time_theorem` | bounded_theorem | unaudited | critical | 1080 | 44.58 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_anomaly_forces_time.py` |
| 21 | `staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10` | bounded_theorem | unaudited | critical | 1059 | 15.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py` |
| 22 | `axiom_first_lattice_noether_theorem_note_2026-04-29` | bounded_theorem | unaudited | critical | 928 | 20.36 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_lattice_noether_check.py` |
| 23 | `yt_vertex_power_derivation` | bounded_theorem | unaudited | critical | 909 | 15.83 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_vertex_power.py` |
| 24 | `yt_vertex_power_operator_counting_lemma_note_2026-05-17` | bounded_theorem | unaudited | critical | 906 | 15.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_vertex_power_operator_counting_lemma.py` |
| 25 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | bounded_theorem | unaudited | critical | 905 | 23.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/axiom_first_microcausality_check.py` |
| 26 | `alpha_s_derived_note` | bounded_theorem | unaudited | critical | 903 | 42.32 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_alpha_s_derived_bounded_chain.py` |
| 27 | `observable_principle_from_axiom_note` | bounded_theorem | unaudited | critical | 899 | 63.31 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_hierarchy_observable_principle_from_axiom.py` |
| 28 | `staggered_dirac_physical_species_direct_theorem_note_2026-05-07` | bounded_theorem | unaudited | critical | 892 | 16.80 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/probe_three_states_direct_derivation.py` |
| 29 | `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac` | bounded_theorem | unaudited | critical | 891 | 45.30 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/cl3_staggered_dirac_substep4_ac_check_2026_05_07_substep4ac.py` |
| 30 | `staggered_dirac_substep4_labeling_no_go_note_2026-05-17` | no_go | unaudited | critical | 882 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/audit_companion_staggered_dirac_substep4_labeling_no_go_2026_05_17.py` |
| 31 | `quark_route2_source_domain_bridge_no_go_note_2026-04-28` | no_go | unaudited | critical | 881 | 15.79 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_quark_route2_source_domain_bridge_no_go.py` |
| 32 | `staggered_dirac_gate_closure_synthesis_theorem_note_2026-05-17` | bounded_theorem | unaudited | critical | 880 | 16.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_staggered_dirac_gate_closure_synthesis_2026_05_17.py` |
| 33 | `staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem | unaudited | critical | 878 | 14.28 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_runner.py` |
| 34 | `staggered_dirac_realization_gate_note_2026-05-03` | bounded_theorem | unaudited | critical | 877 | 39.78 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/staggered_dirac_realization_gate_synthesis_check_2026_06_09.py` |
| 35 | `s3_time_theta_to_slice_coupling_note` | open_gate | unaudited | critical | 875 | 15.28 |  | fresh_context_or_stronger_with_cross_confirmation | - |
| 36 | `s3_time_spacetime_tensor_primitive_note` | bounded_theorem | unaudited | critical | 873 | 16.77 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_spacetime_tensor_primitive.py` |
| 37 | `one_generation_matter_closure_note` | bounded_theorem | unaudited | critical | 864 | 30.76 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_right_handed_sector.py` |
| 38 | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | positive_theorem | unaudited | critical | 817 | 33.18 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_sm_hypercharge_uniqueness.py` |
| 39 | `yt_zero_import_authority_note` | positive_theorem | unaudited | critical | 807 | 18.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ward_identity_derivation.py` |
| 40 | `yt_boundary_theorem` | open_gate | unaudited | critical | 805 | 20.16 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_boundary_consistency.py` |
| 41 | `s3_time_transfer_matrix_bridge_note` | bounded_theorem | unaudited | critical | 785 | 16.12 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_transfer_matrix_bridge.py` |
| 42 | `s3_time_bilinear_tensor_primitive_note` | open_gate | unaudited | critical | 780 | 20.11 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_primitive.py` |
| 43 | `s3_time_bilinear_tensor_action_note` | open_gate | unaudited | critical | 771 | 14.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_s3_time_bilinear_tensor_action.py` |
| 44 | `ckm_atlas_axiom_closure_note` | positive_theorem | unaudited | critical | 770 | 32.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_ckm_atlas_axiom_closure.py` |
| 45 | `yt_qfp_insensitivity_support_note` | bounded_theorem | unaudited | critical | 767 | 21.59 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_qfp_insensitivity.py` |
| 46 | `yt_eft_bridge_theorem` | open_gate | unaudited | critical | 753 | 14.56 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_eft_bridge.py` |
| 47 | `yt_ew_coupling_bridge_note` | bounded_theorem | unaudited | critical | 752 | 15.56 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_ew_coupling_derivation.py` |
| 48 | `yt_interacting_bridge_locality_note` | bounded_theorem | unaudited | critical | 751 | 18.55 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_interacting_bridge_locality.py` |
| 49 | `yt_bridge_operator_closure_note` | bounded_theorem | unaudited | critical | 750 | 15.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_bridge_operator_closure.py` |
| 50 | `yt_constructive_uv_bridge_note` | bounded_theorem | unaudited | critical | 749 | 20.05 |  | fresh_context_or_stronger_with_cross_confirmation | `scripts/frontier_yt_constructive_uv_bridge.py` |

Full queue lives in `data/audit_queue.json`.
