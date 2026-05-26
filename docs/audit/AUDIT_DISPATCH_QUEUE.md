# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 3
**Ready entries:** 2
**Resolved (post-manifest re-audit) entries:** 13
**Resolved/invalid entries:** 35
**Retired entries:** 5

Source sidecars:
- `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-23.json`
- `docs/audit/data/lsp_projective_reaudit_queue_2026-05-22.json`
- `docs/audit/data/promotion_reaudit_queue_2026-05-22.json`
- `docs/audit/data/provenance_reaudit_queue_2026-05-23.json`
- `docs/audit/data/r1_qubit_k1_reaudit_queue_2026-05-22.json`

## Live Dispatch Entries

| # | ready | group | claim_id | current | source note | audit question | ready_blocker |
|---:|:---:|---|---|---|---|---|---|
| 1 | Y | `legacy_weak_independence_clean_rows` | `packet_memory_note` | bounded_theorem / audited_clean / retained_bounded | `docs/PACKET_MEMORY_NOTE.md` | Fresh-context provenance re-audit: the current clean verdict has independence=weak. Re-audit the bounded claim under current independence and reasoning-effort requirements. |  |
| 2 | Y | `legacy_weak_independence_terminal_no_go_rows` | `cl4c_carrier_axiom_consequence_map_note_2026-04-28` | no_go / audited_failed / retained_no_go | `archive_unlanded/stale-frames-2026-04-30/CL4C_CARRIER_AXIOM_CONSEQUENCE_MAP_NOTE_2026-04-28.md` | Fresh-context provenance re-audit: this archived no-go row has a terminal verdict recorded with independence=weak. Re-audit the no-go boundary under current independence and no-go-discipline requirements, or confirm it should remain archived/non-authority. |  |
| 3 |  | `lsp_projective_born_chain` | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | bounded_theorem / unaudited / unaudited | `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | After the direct Lüders/projective rows are resolved, does the Born derivation still have remaining blockers, or is the projective-measurement part of the chain now closed? | blocked_by_dependency:pre_record_reference_state_tracial_derivation_note_2026-05-20:unaudited |

## Resolved By Post-Manifest Re-Audit

These dispatch targets have been re-audited after their manifest's `generated_date` with non-weak independence. They are no longer in the live queue, but kept here for provenance.

| # | claim_id | current | resolution_reason | re-audit date | independence | auditor |
|---:|---|---|---|---|---|---|
| 1 | `chiral_3plus1d_coupled_coin_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T17:58:15.439009+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T175755Z-ec176ca3-chiral_3plus1d_coupled_c-01 |
| 2 | `weak_coupling_sign_sensitivity_note_2026-04-11` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:02:48.474160+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T180225Z-2f0c69c0-weak_coupling_sign_sensi-01 |
| 3 | `gauge_vacuum_plaquette_distinct_shell_theorem_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-24T20:26:55.357946+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260524T202502Z-b2d2be46-gauge_vacuum_plaquette_d-02 |
| 4 | `hubble_lane5_c1_a5_minimal_carrier_axiom_audit_note_2026-04-28` | no_go / audited_failed / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-25T23:18:17.990826+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260525T231643Z-abb4e2b9-hubble_lane5_c1_a5_minim-01 |
| 5 | `hubble_lane5_c1_stuck_fanout_synthesis_note_2026-04-28` | no_go / audited_failed / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:12:47.204219+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T181126Z-623cf5b5-hubble_lane5_c1_stuck_fa-01 |
| 6 | `continuum_limit_note` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:13:56.019683+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T181334Z-742480ea-continuum_limit_note-01 |
| 7 | `hermitian_lift_theta_h_pk_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:16:42.496617+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T181535Z-d414d33e-hermitian_lift_theta_h_p-01 |
| 8 | `linear_response_second_order_kubo_note` | bounded_theorem / audited_clean / retained_pending_chain | `bounded_terminal_after_reaudit` | 2026-05-23T18:20:01.804656+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T181743Z-fb17a8f8-linear_response_second_o-01 |
| 9 | `observable_principle_p1_bridge_connes_nc_spectral_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:23:17.872453+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T182224Z-af104ef5-observable_principle_p1_-01 |
| 10 | `observable_principle_p1_bridge_jones_index_subfactor_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:27:21.287498+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T182555Z-1ec5390a-observable_principle_p1_-01 |
| 11 | `observable_principle_p1_bridge_structural_reframing_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:29:20.227225+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T182816Z-85745dea-observable_principle_p1_-01 |
| 12 | `observable_principle_p1_bridge_tomita_gibbs_modular_narrow_note_2026-05-21` | no_go / audited_clean / retained_no_go | `same_status_fresh_context_reaudit_after_manifest` | 2026-05-23T18:32:39.949021+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T183104Z-20b5e4cf-observable_principle_p1_-01 |
| 13 | `staggered_hamiltonian_direction_decomposition_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `bounded_terminal_after_reaudit` | 2026-05-23T18:36:40.690502+00:00 | fresh_context | codex-cli-gpt-5.5-per-site-k1-20260523T183621Z-944d0bf3-staggered_hamiltonian_di-01 |

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
| 11 | resolved_or_superseded | `luders_rule_from_composition_consistency_note_2026-05-20` | bounded_theorem / audited_clean / retained_bounded |
| 12 | resolved_or_superseded | `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` | bounded_theorem / audited_clean / retained_bounded |
| 13 | resolved_or_superseded | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 14 | resolved_or_superseded | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 15 | resolved_or_superseded | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 16 | resolved_or_superseded | `graph_first_selector_derivation_note` | positive_theorem / audited_clean / retained |
| 17 | resolved_or_superseded | `graph_first_su3_integration_note` | positive_theorem / audited_clean / retained |
| 18 | resolved_or_superseded | `cl3_color_automorphism_theorem` | positive_theorem / audited_clean / retained |
| 19 | resolved_or_superseded | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | decoration / audited_decoration / decoration_under_cl3_color_automorphism_theorem |
| 20 | resolved_or_superseded | `su3_dabc_symmetric_theorem_note_2026-05-02` | bounded_theorem / unaudited / unaudited |
| 21 | resolved_or_superseded | `ew_current_fierz_channel_decomposition_note_2026-05-01` | decoration / audited_decoration / decoration_under_graph_first_su3_integration_note |
| 22 | resolved_or_superseded | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited |
| 23 | resolved_or_superseded | `action_normalization_note` | no_go / unaudited / unaudited |
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
