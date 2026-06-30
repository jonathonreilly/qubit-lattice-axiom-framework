# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 5
**Ready entries:** 1
**Resolved (post-manifest re-audit) entries:** 18
**Resolved/invalid entries:** 42
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
| 2 |  | `anomaly_forces_time_bridge_fresh_context` | `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` | bounded_theorem / unaudited / unaudited | `docs/ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md` | Fresh-context re-audit target: under the current dependency-edge repair and premise manifest, does the anomaly-forces-time ABJ bridge validate as a bounded_theorem over explicit premises P-ABJ, P-HY, P-COMP, and P-REC without crediting native_gauge_closure for hypercharge, abelian values, or matter completion? | blocked_by_dependency:abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18:unaudited,hypercharge_identification_note:audited_conditional,no_per_site_chirality_theorem_note_2026-05-02:unaudited |
| 3 |  | `universal_gr_picurv_parent_reaudit` | `universal_gr_polarization_frame_bundle_blocker_note` | bounded_theorem / unaudited / unaudited | `docs/UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md` | Fresh-context review target: does UNIVERSAL_GR_PICURV_ROUTE_EXHAUSTION_NO_GO_NOTE_2026-06-18.md supply the route-exhaustion gate requested for UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md without overclaiming absolute GR impossibility or demoting positive A1/Casimir/Regge/spin-2 routes? | blocked_by_dependency:observable_principle_from_axiom_note:unaudited,s3_anomaly_spacetime_lift_note:unaudited,universal_gr_tensor_variational_candidate_note:unaudited,universal_gr_tensor_quotient_uniqueness_note:unaudited |
| 4 |  | `lsp_projective_direct_luders` | `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` | bounded_theorem / unaudited / unaudited | `docs/LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` | With LSP-projective ratified for ideal unrefined projective measurements, does the conditional K_P=P bridge become clean scoped support, or does an upstream dependency/status issue still block it? | blocked_by_dependency:kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20:unaudited,lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22:unaudited |
| 5 |  | `anomaly_forces_time_parent_after_bridge` | `anomaly_forces_time_theorem` | bounded_theorem / unaudited / unaudited | `docs/ANOMALY_FORCES_TIME_THEOREM.md` | Fresh-context audit target after the bridge resolves: does ANOMALY_FORCES_TIME_THEOREM.md close only the d_t odd/parity result under its explicit bridge and retained dependencies, while leaving the d_t = 1 single-generator cap to the emergent-dynamics open gate? | blocked_by_live_group:anomaly_forces_time_bridge_fresh_context |

## Resolved By Post-Manifest Re-Audit

These dispatch targets have been re-audited after their manifest's `generated_date` with non-weak independence. They are no longer in the live queue, but kept here for provenance.

| # | claim_id | current | resolution_reason | re-audit date | independence | auditor |
|---:|---|---|---|---|---|---|
| 1 | `causal_propagating_field_live_packet_note_2026-06-05` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-06-21T05:47:30.165796+00:00 | fresh_context | codex-cli-gpt-5.5-20260621-054531-f51f6887-causal_propagating_field_live_packet_note_2026-06-05-reaudit |
| 2 | `oh_schur_boundary_action_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-29T01:38:37.745835+00:00 | judicial_review | codex-gpt-5.5-five-judge-panel-majority-20260529-oh-schur-boundary |
| 3 | `s3_cap_uniqueness_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-28T01:33:46.485182+00:00 | fresh_context | codex-audit-loop-fresh-context-s3-cap-20260527-r2 |
| 4 | `three_generation_structure_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-29T03:10:19.348385+00:00 | fresh_context | codex_fresh_three_gen_structure_second_pass_2026_05_29 |
| 5 | `chiral_3plus1d_coupled_coin_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T17:58:15.439009+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T175755Z-ec176ca3-chiral_3plus1d_coupled_c-01 |
| 6 | `packet_memory_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-06-08T21:02:46.164959+00:00 | cross_family | codex-cli-gpt-5.5-20260608-205745-10378e1cab-packet_memory_note |
| 7 | `weak_coupling_sign_sensitivity_note_2026-04-11` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:02:48.474160+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T180225Z-2f0c69c0-weak_coupling_sign_sensi-01 |
| 8 | `cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-30T22:30:24.031778+00:00 | fresh_context | codex-cli-gpt-5.5-20260530-222822-4f97992e-cluster_decomposition_ma |
| 9 | `gauge_vacuum_plaquette_distinct_shell_theorem_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-29T21:20:05.982098+00:00 | cross_family | codex-cli-audit-ready-20260529-gauge_vacuum_plaquette_d |
| 10 | `cl3_color_automorphism_theorem` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-06-15T19:14:15.319586+00:00 | judicial_review | codex-gpt-5.5-five-judge-panel-majority-20260615T191415Z-cl3_color_automorphism_theorem |
| 11 | `continuum_limit_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:13:56.019683+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T181334Z-742480ea-continuum_limit_note-01 |
| 12 | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-06-19T20:51:36.034920+00:00 | fresh_context | codex-cli-gpt-5.5-20260619-203739-0fd17364-rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17-second |
| 13 | `hermitian_lift_theta_h_pk_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:16:42.496617+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T181535Z-d414d33e-hermitian_lift_theta_h_p-01 |
| 14 | `observable_principle_p1_bridge_connes_nc_spectral_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:23:17.872453+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T182224Z-af104ef5-observable_principle_p1_-01 |
| 15 | `observable_principle_p1_bridge_jones_index_subfactor_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:27:21.287498+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T182555Z-1ec5390a-observable_principle_p1_-01 |
| 16 | `observable_principle_p1_bridge_structural_reframing_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:29:20.227225+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T182816Z-85745dea-observable_principle_p1_-01 |
| 17 | `observable_principle_p1_bridge_tomita_gibbs_modular_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:32:39.949021+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T183104Z-20b5e4cf-observable_principle_p1_-01 |
| 18 | `staggered_hamiltonian_direction_decomposition_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:36:40.690502+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T183621Z-944d0bf3-staggered_hamiltonian_di-01 |

## Resolved Or Invalid

| # | state | claim_id | current |
|---:|---|---|---|
| 1 | resolved_or_superseded | `native_gauge_closure_note` | positive_theorem / audited_clean / retained |
| 2 | resolved_or_superseded | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | positive_theorem / audited_clean / retained |
| 3 | resolved_or_superseded | `gauge_scalar_temporal_completion_theorem_note` | positive_theorem / audited_clean / retained |
| 4 | resolved_or_superseded | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | positive_theorem / audited_clean / retained |
| 5 | resolved_or_superseded | `gauge_vacuum_plaquette_reduction_existence_theorem_note` | positive_theorem / audited_clean / retained |
| 6 | resolved_or_superseded | `scalar_3plus1_temporal_ratio_note` | positive_theorem / audited_clean / retained |
| 7 | resolved_or_superseded | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | positive_theorem / audited_clean / retained |
| 8 | resolved_or_superseded | `gauge_vacuum_plaquette_spectral_measure_theorem_note` | positive_theorem / audited_clean / retained |
| 9 | resolved_or_superseded | `su3_wigner_intertwiner_block2_theorem_note_2026-05-03` | positive_theorem / audited_clean / retained |
| 10 | resolved_or_superseded | `s3_taste_cube_decomposition_note` | positive_theorem / audited_clean / retained |
| 11 | resolved_or_superseded | `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29` | positive_theorem / audited_clean / retained |
| 12 | resolved_or_superseded | `three_generation_observable_theorem_note` | positive_theorem / audited_clean / retained |
| 13 | resolved_or_superseded | `reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 14 | resolved_or_superseded | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |
| 15 | resolved_or_superseded | `cluster_decomposition_delta_t_finite_lambda_operator_real_note_2026-05-19` | positive_theorem / audited_clean / retained |
| 16 | resolved_or_superseded | `axiom_first_cluster_decomposition_theorem_note_2026-04-29` | bounded_theorem / unaudited / unaudited |
| 17 | resolved_or_superseded | `luders_rule_from_composition_consistency_note_2026-05-20` | bounded_theorem / unaudited / unaudited |
| 18 | resolved_or_superseded | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | positive_theorem / unaudited / unaudited |
| 19 | resolved_or_superseded | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 20 | resolved_or_superseded | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 21 | resolved_or_superseded | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 22 | resolved_or_superseded | `graph_first_selector_derivation_note` | positive_theorem / audited_clean / retained |
| 23 | resolved_or_superseded | `graph_first_su3_integration_note` | positive_theorem / audited_clean / retained |
| 24 | resolved_or_superseded | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | decoration / audited_decoration / decoration_under_cl3_color_automorphism_theorem |
| 25 | resolved_or_superseded | `su3_dabc_symmetric_theorem_note_2026-05-02` | decoration / audited_decoration / decoration_under_cl3_color_automorphism_theorem |
| 26 | resolved_or_superseded | `ew_current_fierz_channel_decomposition_note_2026-05-01` | decoration / audited_decoration / decoration_under_graph_first_su3_integration_note |
| 27 | resolved_or_superseded | `action_normalization_note` | no_go / audited_clean / retained_no_go |
| 28 | resolved_or_superseded | `sigma_mnu_f3_stuck_fanout_synthesis_note_2026-04-28` | no_go / unaudited / unaudited |
| 29 | resolved_or_superseded | `work_history.yt.yt_unbounded_program_note` | open_gate / unaudited / unaudited |
| 30 | invalid_missing_claim_id | `cl4c_carrier_axiom_consequence_map_note_2026-04-28` | None / None / None |
| 31 | invalid_missing_claim_id | `hubble_lane5_c1_a5_minimal_carrier_axiom_audit_note_2026-04-28` | None / None / None |
| 32 | invalid_missing_claim_id | `hubble_lane5_c1_stuck_fanout_synthesis_note_2026-04-28` | None / None / None |
| 33 | resolved_or_superseded | `linear_response_second_order_kubo_note` | bounded_theorem / audited_clean / retained_bounded |
| 34 | resolved_or_superseded | `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | positive_theorem / unaudited / unaudited |
| 35 | resolved_or_superseded | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | positive_theorem / unaudited / unaudited |
| 36 | resolved_or_superseded | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | decoration / audited_decoration / decoration_under_cl3_complexification_split_narrow_theorem_note_2026-05-10 |
| 37 | resolved_or_superseded | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |
| 38 | resolved_or_superseded | `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | no_go / unaudited / unaudited |
| 39 | resolved_or_superseded | `no_per_site_chirality_theorem_note_2026-05-02` | no_go / unaudited / unaudited |
| 40 | resolved_or_superseded | `pauli_group_order_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |
| 41 | resolved_or_superseded | `q_integer_spectrum_theorem_note_2026-05-02` | positive_theorem / unaudited / unaudited |
| 42 | resolved_or_superseded | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem / unaudited / unaudited |

## Retired Dispatch Targets

| # | claim_id | current | reason |
|---:|---|---|---|
| 1 | `higgs_from_lattice_note` | bounded_theorem / unaudited / unaudited | not_a_direct_promotion_candidate |
| 2 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem / audited_clean / retained_bounded | not_a_direct_promotion_candidate |
| 3 | `yt_ward_identity_derivation_theorem` | bounded_theorem / unaudited / unaudited | deferred_normalization_convention |
| 4 | `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` | decoration / audited_decoration / decoration_under_cl3_color_automorphism_theorem | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 5 | `g_bare_constraint_vs_convention_theorem_note_2026-05-03` | bounded_theorem / audited_clean / retained_bounded | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 6 | `g_bare_derivation_note` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 7 | `g_bare_structural_normalization_theorem_note_2026-04-18` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 8 | `g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19` | bounded_theorem / audited_clean / retained_bounded | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 9 | `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 10 | `g_bare_rigidity_theorem_note` | bounded_theorem / audited_clean / retained_bounded | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 11 | `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` | bounded_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 12 | `g_bare_two_ward_closure_note_2026-04-18` | positive_theorem / unaudited / unaudited | blocked_convention_see_G_BARE_PROMOTION_PANEL_FINDING_2026-05-28 |
| 13 | `wilson_bz_corner_hamming_staircase_bounded_note_2026-05-08` | bounded_theorem / audited_clean / retained_bounded | exact_content_already_lifted_in_companion |
| 14 | `g_bare_rigidity_theorem_note` | bounded_theorem / audited_clean / retained_bounded | load_bearing_in_open_g_bare_closure |
| 15 | `koide_circulant_wilson_target_note_2026-04-18` | bounded_theorem / audited_clean / retained_bounded | assembler_not_source_of_exact_statement |
| 16 | `r_base_group_theory_derivation_theorem_note_2026-04-24` | bounded_theorem / unaudited / unaudited | exact_arithmetic_conditional_on_admitted_normalization |
| 17 | `generation_axiom_boundary_note` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the claim. |
| 18 | `native_gauge_closure_note` | positive_theorem / audited_clean / retained | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the structural gauge-closure claim. |
| 19 | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; current source scope is a finite projection lemma and does not close the kappa_EW matching-rule identification. Positive-theorem promotion remains conditional on a future source repair that closes that identification. |

Full machine-readable queue lives in `data/audit_dispatch_queue.json`.
