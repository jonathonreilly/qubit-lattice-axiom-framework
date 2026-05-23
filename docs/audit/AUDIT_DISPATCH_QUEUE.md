# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 2
**Ready entries:** 1
**Resolved/invalid entries:** 32
**Retired entries:** 5

Source sidecars:
- `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-23.json`
- `docs/audit/data/lsp_projective_reaudit_queue_2026-05-22.json`
- `docs/audit/data/promotion_reaudit_queue_2026-05-22.json`
- `docs/audit/data/r1_qubit_k1_reaudit_queue_2026-05-22.json`

## Live Dispatch Entries

| # | ready | group | claim_id | current | source note | audit question |
|---:|:---:|---|---|---|---|---|
| 1 | Y | `su3_toolkit_algebra` | `cl3_color_automorphism_theorem` | bounded_theorem / audited_clean / retained_bounded | `docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md` | Does the algebraic SU(3) embedding/channel-count scope qualify as positive_theorem, excluding physical color and EW readout? |
| 2 |  | `lsp_projective_born_chain` | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | bounded_theorem / unaudited / unaudited | `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | After the direct Lüders/projective rows are resolved, does the Born derivation still have remaining blockers, or is the projective-measurement part of the chain now closed? |

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
| 9 | resolved_or_superseded | `gauge_vacuum_plaquette_distinct_shell_theorem_note` | bounded_theorem / audited_conditional / audited_conditional |
| 10 | resolved_or_superseded | `su3_wigner_intertwiner_block2_theorem_note_2026-05-03` | positive_theorem / audited_clean / retained |
| 11 | resolved_or_superseded | `s3_taste_cube_decomposition_note` | positive_theorem / audited_clean / retained |
| 12 | resolved_or_superseded | `luders_rule_from_composition_consistency_note_2026-05-20` | bounded_theorem / audited_clean / retained_bounded |
| 13 | resolved_or_superseded | `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` | bounded_theorem / audited_conditional / audited_conditional |
| 14 | resolved_or_superseded | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 15 | resolved_or_superseded | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 16 | resolved_or_superseded | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 17 | resolved_or_superseded | `graph_first_selector_derivation_note` | positive_theorem / audited_clean / retained |
| 18 | resolved_or_superseded | `graph_first_su3_integration_note` | positive_theorem / audited_clean / retained |
| 19 | resolved_or_superseded | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | decoration / audited_decoration / decoration_under_cl3_color_automorphism_theorem |
| 20 | resolved_or_superseded | `su3_dabc_symmetric_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional |
| 21 | resolved_or_superseded | `ew_current_fierz_channel_decomposition_note_2026-05-01` | decoration / audited_decoration / decoration_under_graph_first_su3_integration_note |
| 22 | resolved_or_superseded | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited |
| 23 | resolved_or_superseded | `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20` | positive_theorem / audited_renaming / audited_renaming |
| 24 | resolved_or_superseded | `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded |
| 25 | resolved_or_superseded | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | bounded_theorem / audited_clean / retained_bounded |
| 26 | resolved_or_superseded | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | decoration / audited_decoration / retained_pending_chain |
| 27 | resolved_or_superseded | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |
| 28 | resolved_or_superseded | `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | no_go / audited_clean / retained_no_go |
| 29 | resolved_or_superseded | `no_per_site_chirality_theorem_note_2026-05-02` | no_go / audited_clean / retained_no_go |
| 30 | resolved_or_superseded | `pauli_group_order_theorem_note_2026-05-02` | bounded_theorem / audited_clean / retained_bounded |
| 31 | resolved_or_superseded | `q_integer_spectrum_theorem_note_2026-05-02` | bounded_theorem / audited_clean / retained_bounded |
| 32 | resolved_or_superseded | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |

## Retired Dispatch Targets

| # | claim_id | current | reason |
|---:|---|---|---|
| 1 | `higgs_from_lattice_note` | bounded_theorem / audited_clean / retained_bounded | not_a_direct_promotion_candidate |
| 2 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem / audited_clean / retained_bounded | not_a_direct_promotion_candidate |
| 3 | `generation_axiom_boundary_note` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the claim. |
| 4 | `native_gauge_closure_note` | positive_theorem / audited_clean / retained | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the structural gauge-closure claim. |
| 5 | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited | bounded_terminal_after_dispatch_audit; current source scope is a finite projection lemma and does not close the kappa_EW matching-rule identification. Positive-theorem promotion remains conditional on a future source repair that closes that identification. |

Full machine-readable queue lives in `data/audit_dispatch_queue.json`.
