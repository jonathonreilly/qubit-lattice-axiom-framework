# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 7
**Ready entries:** 2
**Resolved (post-manifest re-audit) entries:** 4
**Resolved/invalid entries:** 54
**Retired entries:** 19

Source sidecars:
- `docs/audit/data/anomaly_forces_time_reaudit_queue_2026-06-21.json`
- `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-23.json`
- `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-28.json`
- `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-29.json`
- `docs/audit/data/causal_field_live_reaudit_queue_2026-06-18.json`
- `docs/audit/data/lsp_projective_reaudit_queue_2026-05-22.json`
- `docs/audit/data/promotion_reaudit_queue_2026-05-22.json`
- `docs/audit/data/provenance_reaudit_queue_2026-05-23.json`
- `docs/audit/data/r1_qubit_k1_reaudit_queue_2026-05-22.json`
- `docs/audit/data/universal_gr_picurv_parent_reaudit_queue_2026-06-18.json`

## Live Dispatch Entries

| # | ready | group | claim_id | current | source note | audit question | ready_blocker |
|---:|:---:|---|---|---|---|---|---|
| 1 | Y | `r1_substep1_chain` | `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20` | positive_theorem / unaudited / unaudited | `docs/U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md` | Under the ratified k=1 qubit-per-site clause now on the canonical axiom surface, does the U4 closure row qualify as audited_decoration under cl3_complexification_split (as the prior audit verdict explicitly named), or does it require a different category? |  |
| 2 | Y | `r1_substep1_chain` | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited | `docs/STAGGERED_DIRAC_SUBSTEP1_JW_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md` | With the k=1 qubit-per-site clause ratified on the axiom surface and the substep-1 dependency chain routed through the retained cl3_complexification_split parent, does the Jordan-Wigner substep-1 bridge close under the qubit-per-site reading, or does another blocker remain? |  |
| 3 |  | `anomaly_forces_time_bridge_fresh_context` | `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem / unaudited / unaudited | `docs/ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md` | Fresh-context re-audit target: under the current dependency-edge repair and premise manifest, does the anomaly-forces-time ABJ bridge validate as a bounded_theorem over explicit premises P-ABJ, P-HY, P-COMP, and P-REC without crediting native_gauge_closure for hypercharge, abelian values, or matter completion? | blocked_by_dependency:abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18:audit_in_progress,hypercharge_identification_note:unaudited,abj_p_comp_scale_free_singlet_completion_classification_note_2026-06-18:unaudited,abj_p_rec_spintaste_clifford_core_bridge_note_2026-06-18:unaudited,clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10:unaudited,no_per_site_chirality_theorem_note_2026-05-02:unaudited,staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07:unaudited |
| 4 |  | `universal_gr_picurv_parent_reaudit` | `universal_gr_polarization_frame_bundle_blocker_note` | bounded_theorem / unaudited / unaudited | `docs/UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md` | Fresh-context review target: does UNIVERSAL_GR_PICURV_ROUTE_EXHAUSTION_NO_GO_NOTE_2026-06-18.md supply the route-exhaustion gate requested for UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md without overclaiming absolute GR impossibility or demoting positive A1/Casimir/Regge/spin-2 routes? | blocked_by_dependency:observable_principle_from_axiom_note:unaudited,s3_anomaly_spacetime_lift_note:unaudited,universal_gr_tensor_variational_candidate_note:unaudited,universal_gr_tensor_quotient_uniqueness_note:unaudited |
| 5 |  | `lsp_projective_direct_luders` | `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` | bounded_theorem / unaudited / unaudited | `docs/LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` | With LSP-projective ratified for ideal unrefined projective measurements, does the conditional K_P=P bridge become clean scoped support, or does an upstream dependency/status issue still block it? | blocked_by_dependency:kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20:audit_in_progress,lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22:unaudited |
| 6 |  | `anomaly_forces_time_parent_after_bridge` | `anomaly_forces_time_theorem` | bounded_theorem / unaudited / unaudited | `docs/ANOMALY_FORCES_TIME_THEOREM.md` | Fresh-context audit target after the bridge resolves: does ANOMALY_FORCES_TIME_THEOREM.md close only the d_t odd/parity result under its explicit bridge and retained dependencies, while leaving the d_t = 1 single-generator cap to the emergent-dynamics open gate? | blocked_by_live_group:anomaly_forces_time_bridge_fresh_context |
| 7 |  | `lsp_projective_born_chain` | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | bounded_theorem / unaudited / unaudited | `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | After the direct Lüders/projective rows are resolved, does the Born derivation still have remaining blockers, or is the projective-measurement part of the chain now closed? | blocked_by_live_group:lsp_projective_direct_luders |

## Resolved By Post-Manifest Re-Audit

These dispatch targets have been re-audited after their manifest's `generated_date` with non-weak independence. They are no longer in the live queue, but kept here for provenance.

| # | claim_id | current | resolution_reason | re-audit date | independence | auditor |
|---:|---|---|---|---|---|---|
| 1 | `causal_propagating_field_live_packet_note_2026-06-05` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-06-21T05:47:30.165796+00:00 | fresh_context | codex-cli-gpt-5.5-20260621-054531-f51f6887-causal_propagating_field_live_packet_note_2026-06-05-reaudit |
| 2 | `s3_cap_uniqueness_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-28T01:33:46.485182+00:00 | fresh_context | codex-audit-loop-fresh-context-s3-cap-20260527-r2 |
| 3 | `chiral_3plus1d_coupled_coin_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T17:58:15.439009+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T175755Z-ec176ca3-chiral_3plus1d_coupled_c-01 |
| 4 | `continuum_limit_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:13:56.019683+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T181334Z-742480ea-continuum_limit_note-01 |

## Resolved Or Invalid

| # | state | claim_id | current |
|---:|---|---|---|
| 1 | resolved_or_superseded | `native_gauge_closure_note` | positive_theorem / audited_clean / retained |
| 2 | resolved_or_superseded | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | positive_theorem / unaudited / unaudited |
| 3 | resolved_or_superseded | `gauge_scalar_temporal_completion_theorem_note` | positive_theorem / audited_clean / retained |
| 4 | resolved_or_superseded | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | positive_theorem / unaudited / unaudited |
| 5 | resolved_or_superseded | `gauge_vacuum_plaquette_reduction_existence_theorem_note` | bounded_theorem / unaudited / unaudited |
| 6 | resolved_or_superseded | `scalar_3plus1_temporal_ratio_note` | positive_theorem / audited_clean / retained |
| 7 | resolved_or_superseded | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | open_gate / unaudited / unaudited |
| 8 | resolved_or_superseded | `gauge_vacuum_plaquette_spectral_measure_theorem_note` | bounded_theorem / unaudited / unaudited |
| 9 | resolved_or_superseded | `gauge_vacuum_plaquette_distinct_shell_theorem_note` | bounded_theorem / unaudited / unaudited |
| 10 | resolved_or_superseded | `su3_wigner_intertwiner_block2_theorem_note_2026-05-03` | positive_theorem / audited_clean / retained |
| 11 | resolved_or_superseded | `s3_taste_cube_decomposition_note` | positive_theorem / audited_clean / retained |
| 12 | resolved_or_superseded | `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29` | bounded_theorem / unaudited / unaudited |
| 13 | resolved_or_superseded | `three_generation_observable_theorem_note` | bounded_theorem / unaudited / unaudited |
| 14 | resolved_or_superseded | `reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 15 | resolved_or_superseded | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | bounded_theorem / unaudited / unaudited |
| 16 | resolved_or_superseded | `oh_schur_boundary_action_note` | positive_theorem / unaudited / unaudited |
| 17 | resolved_or_superseded | `three_generation_structure_note` | bounded_theorem / unaudited / unaudited |
| 18 | resolved_or_superseded | `cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09` | bounded_theorem / unaudited / unaudited |
| 19 | resolved_or_superseded | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | positive_theorem / audited_clean / retained |
| 20 | resolved_or_superseded | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem / unaudited / unaudited |
| 21 | resolved_or_superseded | `luders_rule_from_composition_consistency_note_2026-05-20` | bounded_theorem / unaudited / unaudited |
| 22 | resolved_or_superseded | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem / audited_conditional / audited_conditional |
| 23 | resolved_or_superseded | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | bounded_theorem / unaudited / unaudited |
| 24 | resolved_or_superseded | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | bounded_theorem / unaudited / unaudited |
| 25 | resolved_or_superseded | `graph_first_selector_derivation_note` | positive_theorem / audited_clean / retained |
| 26 | resolved_or_superseded | `graph_first_su3_integration_note` | positive_theorem / audited_clean / retained |
| 27 | resolved_or_superseded | `cl3_color_automorphism_theorem` | bounded_theorem / unaudited / unaudited |
| 28 | resolved_or_superseded | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | positive_theorem / unaudited / unaudited |
| 29 | resolved_or_superseded | `su3_dabc_symmetric_theorem_note_2026-05-02` | bounded_theorem / unaudited / unaudited |
| 30 | resolved_or_superseded | `ew_current_fierz_channel_decomposition_note_2026-05-01` | decoration / audited_decoration / decoration_under_graph_first_su3_integration_note |
| 31 | resolved_or_superseded | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited |
| 32 | resolved_or_superseded | `action_normalization_note` | no_go / unaudited / unaudited |
| 33 | resolved_or_superseded | `packet_memory_note` | bounded_theorem / unaudited / unaudited |
| 34 | resolved_or_superseded | `sigma_mnu_f3_stuck_fanout_synthesis_note_2026-04-28` | no_go / unaudited / unaudited |
| 35 | resolved_or_superseded | `weak_coupling_sign_sensitivity_note_2026-04-11` | open_gate / unaudited / unaudited |
| 36 | resolved_or_superseded | `work_history.yt.yt_unbounded_program_note` | open_gate / unaudited / unaudited |
| 37 | invalid_missing_claim_id | `cl4c_carrier_axiom_consequence_map_note_2026-04-28` | None / None / None |
| 38 | invalid_missing_claim_id | `hubble_lane5_c1_a5_minimal_carrier_axiom_audit_note_2026-04-28` | None / None / None |
| 39 | invalid_missing_claim_id | `hubble_lane5_c1_stuck_fanout_synthesis_note_2026-04-28` | None / None / None |
| 40 | resolved_or_superseded | `hermitian_lift_theta_h_pk_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited |
| 41 | resolved_or_superseded | `linear_response_second_order_kubo_note` | bounded_theorem / unaudited / unaudited |
| 42 | resolved_or_superseded | `observable_principle_p1_bridge_connes_nc_spectral_narrow_note_2026-05-21` | no_go / unaudited / unaudited |
| 43 | resolved_or_superseded | `observable_principle_p1_bridge_jones_index_subfactor_narrow_note_2026-05-21` | no_go / unaudited / unaudited |
| 44 | resolved_or_superseded | `observable_principle_p1_bridge_structural_reframing_narrow_note_2026-05-21` | no_go / unaudited / unaudited |
| 45 | resolved_or_superseded | `observable_principle_p1_bridge_tomita_gibbs_modular_narrow_note_2026-05-21` | no_go / unaudited / unaudited |
| 46 | resolved_or_superseded | `staggered_hamiltonian_direction_decomposition_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited |
| 47 | resolved_or_superseded | `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | positive_theorem / unaudited / unaudited |
| 48 | resolved_or_superseded | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | positive_theorem / unaudited / unaudited |
| 49 | resolved_or_superseded | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem / unaudited / unaudited |
| 50 | resolved_or_superseded | `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | no_go / unaudited / unaudited |
| 51 | resolved_or_superseded | `no_per_site_chirality_theorem_note_2026-05-02` | no_go / unaudited / unaudited |
| 52 | resolved_or_superseded | `pauli_group_order_theorem_note_2026-05-02` | positive_theorem / unaudited / unaudited |
| 53 | resolved_or_superseded | `q_integer_spectrum_theorem_note_2026-05-02` | positive_theorem / unaudited / unaudited |
| 54 | resolved_or_superseded | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem / unaudited / unaudited |

## Retired Dispatch Targets

| # | claim_id | current | reason |
|---:|---|---|---|
| 1 | `higgs_from_lattice_note` | bounded_theorem / unaudited / unaudited | not_a_direct_promotion_candidate |
| 2 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem / unaudited / unaudited | not_a_direct_promotion_candidate |
| 3 | `yt_ward_identity_derivation_theorem` | bounded_theorem / unaudited / unaudited | deferred_normalization_convention |
| 4 | `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 5 | `g_bare_constraint_vs_convention_theorem_note_2026-05-03` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 6 | `g_bare_derivation_note` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 7 | `g_bare_structural_normalization_theorem_note_2026-04-18` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 8 | `g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 9 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 10 | `g_bare_rigidity_theorem_note` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 11 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 12 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 13 | `wilson_bz_corner_hamming_staircase_bounded_note_2026-05-08` | bounded_theorem / unaudited / unaudited | exact_content_already_lifted_in_companion |
| 14 | `g_bare_rigidity_theorem_note` | bounded_theorem / unaudited / unaudited | load_bearing_in_open_g_bare_closure |
| 15 | `koide_circulant_wilson_target_note_2026-04-18` | positive_theorem / unaudited / unaudited | assembler_not_source_of_exact_statement |
| 16 | `r_base_group_theory_derivation_theorem_note_2026-04-24` | bounded_theorem / unaudited / unaudited | exact_arithmetic_conditional_on_admitted_normalization |
| 17 | `generation_axiom_boundary_note` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the claim. |
| 18 | `native_gauge_closure_note` | positive_theorem / audited_clean / retained | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the structural gauge-closure claim. |
| 19 | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited | bounded_terminal_after_dispatch_audit; current source scope is a finite projection lemma and does not close the kappa_EW matching-rule identification. Positive-theorem promotion remains conditional on a future source repair that closes that identification. |

Full machine-readable queue lives in `data/audit_dispatch_queue.json`.
