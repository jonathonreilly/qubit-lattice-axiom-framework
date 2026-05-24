# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 16
**Ready entries:** 15
**Resolved/invalid entries:** 35
**Retired entries:** 5

Source sidecars:
- `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-23.json`
- `docs/audit/data/lsp_projective_reaudit_queue_2026-05-22.json`
- `docs/audit/data/promotion_reaudit_queue_2026-05-22.json`
- `docs/audit/data/provenance_reaudit_queue_2026-05-23.json`
- `docs/audit/data/r1_qubit_k1_reaudit_queue_2026-05-22.json`

## Live Dispatch Entries

| # | ready | group | claim_id | current | source note | audit question |
|---:|:---:|---|---|---|---|---|
| 1 | Y | `lsp_projective_direct_luders` | `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` | bounded_theorem / unaudited / unaudited | `docs/LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` | With LSP-projective ratified for ideal unrefined projective measurements, does the conditional K_P=P bridge become clean scoped support, or does an upstream dependency/status issue still block it? |
| 2 | Y | `legacy_weak_independence_clean_rows` | `chiral_3plus1d_coupled_coin_note` | bounded_theorem / audited_clean / retained_bounded | `docs/CHIRAL_3PLUS1D_COUPLED_COIN_NOTE.md` | Fresh-context provenance re-audit: the current clean verdict has independence=weak. Re-audit the bounded claim under current independence and reasoning-effort requirements. |
| 3 | Y | `legacy_weak_independence_clean_rows` | `packet_memory_note` | bounded_theorem / audited_clean / retained_bounded | `docs/PACKET_MEMORY_NOTE.md` | Fresh-context provenance re-audit: the current clean verdict has independence=weak. Re-audit the bounded claim under current independence and reasoning-effort requirements. |
| 4 | Y | `legacy_weak_independence_clean_rows` | `weak_coupling_sign_sensitivity_note_2026-04-11` | bounded_theorem / audited_clean / retained_bounded | `docs/WEAK_COUPLING_SIGN_SENSITIVITY_NOTE_2026-04-11.md` | Fresh-context provenance re-audit: the current clean verdict has independence=weak. Re-audit the bounded claim under current independence and reasoning-effort requirements. |
| 5 | Y | `legacy_weak_independence_terminal_no_go_rows` | `cl4c_carrier_axiom_consequence_map_note_2026-04-28` | no_go / audited_failed / retained_no_go | `archive_unlanded/stale-frames-2026-04-30/CL4C_CARRIER_AXIOM_CONSEQUENCE_MAP_NOTE_2026-04-28.md` | Fresh-context provenance re-audit: this archived no-go row has a terminal verdict recorded with independence=weak. Re-audit the no-go boundary under current independence and no-go-discipline requirements, or confirm it should remain archived/non-authority. |
| 6 | Y | `legacy_weak_independence_terminal_no_go_rows` | `hubble_lane5_c1_a5_minimal_carrier_axiom_audit_note_2026-04-28` | no_go / audited_failed / retained_no_go | `archive_unlanded/stale-frames-2026-04-30/HUBBLE_LANE5_C1_A5_MINIMAL_CARRIER_AXIOM_AUDIT_NOTE_2026-04-28.md` | Fresh-context provenance re-audit: this archived no-go row has a terminal verdict recorded with independence=weak. Re-audit the no-go boundary under current independence and no-go-discipline requirements, or confirm it should remain archived/non-authority. |
| 7 | Y | `legacy_weak_independence_terminal_no_go_rows` | `hubble_lane5_c1_stuck_fanout_synthesis_note_2026-04-28` | no_go / audited_failed / retained_no_go | `archive_unlanded/stale-frames-2026-04-30/HUBBLE_LANE5_C1_STUCK_FANOUT_SYNTHESIS_NOTE_2026-04-28.md` | Fresh-context provenance re-audit: this archived no-go row has a terminal verdict recorded with independence=weak. Re-audit the no-go boundary under current independence and no-go-discipline requirements, or confirm it should remain archived/non-authority. |
| 8 | Y | `claude_only_clean_needs_non_claude_confirmation` | `continuum_limit_note` | bounded_theorem / audited_clean / retained_bounded | `docs/CONTINUUM_LIMIT_NOTE.md` | Fresh-context provenance re-audit: the current clean verdict is Claude-only but recorded as cross_family without non-Claude confirmation. Re-audit the bounded claim under current auditor-independence requirements. |
| 9 | Y | `claude_only_clean_needs_non_claude_confirmation` | `hermitian_lift_theta_h_pk_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `docs/HERMITIAN_LIFT_THETA_H_PK_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md` | Fresh-context provenance re-audit: the current clean verdict is Claude-only but recorded as cross_family without non-Claude confirmation. Re-audit the bounded claim under current auditor-independence requirements. |
| 10 | Y | `claude_only_clean_needs_non_claude_confirmation` | `linear_response_second_order_kubo_note` | bounded_theorem / audited_clean / retained_pending_chain | `docs/LINEAR_RESPONSE_SECOND_ORDER_KUBO_NOTE.md` | Fresh-context provenance re-audit: the current clean verdict is Claude-only but recorded as cross_family without non-Claude confirmation. Re-audit the bounded claim and dependency chain under current auditor-independence requirements. |
| 11 | Y | `claude_only_clean_needs_non_claude_confirmation` | `observable_principle_p1_bridge_connes_nc_spectral_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `docs/OBSERVABLE_PRINCIPLE_P1_BRIDGE_CONNES_NC_SPECTRAL_NARROW_NOTE_2026-05-21.md` | Fresh-context provenance re-audit: the current clean no-go verdict is Claude-only but recorded as cross_family without non-Claude confirmation. Re-audit the no-go boundary under current auditor-independence and no-go-discipline requirements. |
| 12 | Y | `claude_only_clean_needs_non_claude_confirmation` | `observable_principle_p1_bridge_jones_index_subfactor_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `docs/OBSERVABLE_PRINCIPLE_P1_BRIDGE_JONES_INDEX_SUBFACTOR_NARROW_NOTE_2026-05-21.md` | Fresh-context provenance re-audit: the current clean no-go verdict is Claude-only but recorded as cross_family without non-Claude confirmation. Re-audit the no-go boundary under current auditor-independence and no-go-discipline requirements. |
| 13 | Y | `claude_only_clean_needs_non_claude_confirmation` | `observable_principle_p1_bridge_structural_reframing_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `docs/OBSERVABLE_PRINCIPLE_P1_BRIDGE_STRUCTURAL_REFRAMING_NARROW_NOTE_2026-05-21.md` | Fresh-context provenance re-audit: the current clean no-go verdict is Claude-only but recorded as cross_family without non-Claude confirmation. Re-audit the no-go boundary under current auditor-independence and no-go-discipline requirements. |
| 14 | Y | `claude_only_clean_needs_non_claude_confirmation` | `observable_principle_p1_bridge_tomita_gibbs_modular_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `docs/OBSERVABLE_PRINCIPLE_P1_BRIDGE_TOMITA_GIBBS_MODULAR_NARROW_NOTE_2026-05-21.md` | Fresh-context provenance re-audit: the current clean no-go verdict is Claude-only but recorded as cross_family without non-Claude confirmation. Re-audit the no-go boundary under current auditor-independence and no-go-discipline requirements. |
| 15 | Y | `claude_only_clean_needs_non_claude_confirmation` | `staggered_hamiltonian_direction_decomposition_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `docs/STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md` | Fresh-context provenance re-audit: the current clean verdict is Claude-only but recorded as cross_family without non-Claude confirmation. Re-audit the bounded claim under current auditor-independence requirements. |
| 16 |  | `lsp_projective_born_chain` | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | bounded_theorem / unaudited / unaudited | `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | After the direct Lüders/projective rows are resolved, does the Born derivation still have remaining blockers, or is the projective-measurement part of the chain now closed? |

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
| 9 | resolved_or_superseded | `gauge_vacuum_plaquette_distinct_shell_theorem_note` | bounded_theorem / unaudited / unaudited |
| 10 | resolved_or_superseded | `su3_wigner_intertwiner_block2_theorem_note_2026-05-03` | positive_theorem / audited_clean / retained |
| 11 | resolved_or_superseded | `s3_taste_cube_decomposition_note` | positive_theorem / audited_clean / retained |
| 12 | resolved_or_superseded | `luders_rule_from_composition_consistency_note_2026-05-20` | bounded_theorem / audited_clean / retained_bounded |
| 13 | resolved_or_superseded | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 14 | resolved_or_superseded | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 15 | resolved_or_superseded | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 16 | resolved_or_superseded | `graph_first_selector_derivation_note` | positive_theorem / audited_clean / retained |
| 17 | resolved_or_superseded | `graph_first_su3_integration_note` | positive_theorem / audited_clean / retained |
| 18 | resolved_or_superseded | `cl3_color_automorphism_theorem` | positive_theorem / audited_clean / retained |
| 19 | resolved_or_superseded | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | decoration / audited_decoration / decoration_under_cl3_color_automorphism_theorem |
| 20 | resolved_or_superseded | `su3_dabc_symmetric_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional |
| 21 | resolved_or_superseded | `ew_current_fierz_channel_decomposition_note_2026-05-01` | decoration / audited_decoration / decoration_under_graph_first_su3_integration_note |
| 22 | resolved_or_superseded | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited |
| 23 | resolved_or_superseded | `action_normalization_note` | bounded_theorem / audited_conditional / audited_conditional |
| 24 | resolved_or_superseded | `sigma_mnu_f3_stuck_fanout_synthesis_note_2026-04-28` | no_go / audited_conditional / audited_conditional |
| 25 | resolved_or_superseded | `work_history.yt.yt_unbounded_program_note` | open_gate / unaudited / unaudited |
| 26 | resolved_or_superseded | `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20` | positive_theorem / audited_renaming / audited_renaming |
| 27 | resolved_or_superseded | `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded |
| 28 | resolved_or_superseded | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | bounded_theorem / audited_clean / retained_bounded |
| 29 | resolved_or_superseded | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | decoration / audited_decoration / retained_pending_chain |
| 30 | resolved_or_superseded | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |
| 31 | resolved_or_superseded | `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | no_go / audited_clean / retained_no_go |
| 32 | resolved_or_superseded | `no_per_site_chirality_theorem_note_2026-05-02` | no_go / audited_clean / retained_no_go |
| 33 | resolved_or_superseded | `pauli_group_order_theorem_note_2026-05-02` | bounded_theorem / audited_clean / retained_bounded |
| 34 | resolved_or_superseded | `q_integer_spectrum_theorem_note_2026-05-02` | bounded_theorem / audited_clean / retained_bounded |
| 35 | resolved_or_superseded | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |

## Retired Dispatch Targets

| # | claim_id | current | reason |
|---:|---|---|---|
| 1 | `higgs_from_lattice_note` | bounded_theorem / audited_clean / retained_bounded | not_a_direct_promotion_candidate |
| 2 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem / audited_clean / retained_bounded | not_a_direct_promotion_candidate |
| 3 | `generation_axiom_boundary_note` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the claim. |
| 4 | `native_gauge_closure_note` | positive_theorem / audited_clean / retained | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the structural gauge-closure claim. |
| 5 | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; current source scope is a finite projection lemma and does not close the kappa_EW matching-rule identification. Positive-theorem promotion remains conditional on a future source repair that closes that identification. |

Full machine-readable queue lives in `data/audit_dispatch_queue.json`.
