# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 12
**Ready entries:** 11
**Resolved/invalid entries:** 22
**Retired entries:** 5

Source sidecars:
- `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-23.json`
- `docs/audit/data/lsp_projective_reaudit_queue_2026-05-22.json`
- `docs/audit/data/promotion_reaudit_queue_2026-05-22.json`
- `docs/audit/data/r1_qubit_k1_reaudit_queue_2026-05-22.json`

## Live Dispatch Entries

| # | ready | group | claim_id | current | source note | audit question |
|---:|:---:|---|---|---|---|---|
| 1 | Y | `nonabelian_gauge_split_candidate` | `native_gauge_closure_note` | bounded_theorem / audited_clean / retained_bounded | `docs/NATIVE_GAUGE_CLOSURE_NOTE.md` | Can the exact native cubic Cl(3)/SU(2) plus retained graph-first structural SU(3) closure in this aggregator be reclassified as positive_theorem if the abelian/hypercharge-like surface and downstream phenomenology remain explicitly excluded? |
| 2 | Y | `wilson_exact_local_chain` | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md` | Can the exact transfer-operator / character-recurrence realization of the finite Wilson plaquette generating object be reclassified as positive_theorem while leaving explicit beta=6 transfer-state and Perron/thermal data closure open? |
| 3 | Y | `wilson_exact_local_chain` | `gauge_scalar_temporal_completion_theorem_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md` | Can the exact universal temporal completion law for the accepted Wilson nearest-neighbor local bosonic scalar gauge-source class be reclassified as positive_theorem without claiming unrelated source classes or downstream phenomenology? |
| 4 | Y | `wilson_exact_local_chain` | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md` | Can the exact first nonlinear coefficient / onset theorem for the Wilson plaquette reduction law be reclassified as positive_theorem while leaving full analytic beta=6 plaquette closure open? |
| 5 | Y | `wilson_exact_local_chain` | `gauge_vacuum_plaquette_reduction_existence_theorem_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md` | Can the exact existence and uniqueness of the implicit finite Wilson reduction law be reclassified as positive_theorem while leaving explicit nonperturbative beta=6 characterization open? |
| 6 | Y | `wilson_exact_local_chain` | `scalar_3plus1_temporal_ratio_note` | bounded_theorem / audited_clean / retained_bounded | `docs/SCALAR_3PLUS1_TEMPORAL_RATIO_NOTE.md` | Can the exact scalar bridge endpoint ratio A_inf / A_2 = 2 / sqrt(3) on the minimal APBC 3+1 block be reclassified as positive_theorem while keeping dimension-4 observable insertion support-only? |
| 7 | Y | `wilson_exact_local_chain` | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md` | Can the exact connected plaquette cumulant hierarchy on the finite Wilson source surface be reclassified as positive_theorem while leaving explicit nonperturbative beta_eff closure open? |
| 8 | Y | `wilson_exact_local_chain` | `gauge_vacuum_plaquette_spectral_measure_theorem_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GAUGE_VACUUM_PLAQUETTE_SPECTRAL_MEASURE_THEOREM_NOTE.md` | Can the exact compact positive spectral-measure equivalence for the finite Wilson connected plaquette hierarchy be reclassified as positive_theorem while leaving explicit beta=6 spectral-measure identification open? |
| 9 | Y | `wilson_exact_local_chain` | `gauge_vacuum_plaquette_distinct_shell_theorem_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md` | Can the exact minimal distinct-shell geometry around a marked plaquette on the accepted Wilson 3+1 surface be reclassified as positive_theorem while leaving full reduction-law and beta=6 continuation open? |
| 10 | Y | `finite_representation_theory` | `su3_wigner_intertwiner_block2_theorem_note_2026-05-03` | bounded_theorem / audited_clean / retained_bounded | `docs/SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md` | Can the exact finite-rank SU(3) projector construction for (1,1)^4 / C^4096 be reclassified as positive_theorem without promoting the broader cube-closure campaign? |
| 11 | Y | `finite_representation_theory` | `s3_taste_cube_decomposition_note` | bounded_theorem / audited_clean / retained_bounded | `docs/S3_TASTE_CUBE_DECOMPOSITION_NOTE.md` | Can the abstract S3 representation theorem on C^8 = (C^2)^3 under tensor-position permutations be reclassified as positive_theorem while leaving the framework taste-cube carrier interpretation and physical flavor claims gated? |
| 12 |  | `lsp_projective_born_chain` | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | bounded_theorem / unaudited / unaudited | `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | After the direct Lüders/projective rows are resolved, does the Born derivation still have remaining blockers, or is the projective-measurement part of the chain now closed? |

## Resolved Or Invalid

| # | state | claim_id | current |
|---:|---|---|---|
| 1 | resolved_or_superseded | `luders_rule_from_composition_consistency_note_2026-05-20` | bounded_theorem / audited_clean / retained_bounded |
| 2 | resolved_or_superseded | `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` | bounded_theorem / audited_conditional / audited_conditional |
| 3 | resolved_or_superseded | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 4 | resolved_or_superseded | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 5 | resolved_or_superseded | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 6 | resolved_or_superseded | `graph_first_selector_derivation_note` | positive_theorem / audited_clean / retained |
| 7 | resolved_or_superseded | `graph_first_su3_integration_note` | positive_theorem / audited_clean / retained |
| 8 | resolved_or_superseded | `cl3_color_automorphism_theorem` | positive_theorem / audited_clean / retained |
| 9 | resolved_or_superseded | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | decoration / audited_decoration / decoration_under_cl3_color_automorphism_theorem |
| 10 | resolved_or_superseded | `su3_dabc_symmetric_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional |
| 11 | resolved_or_superseded | `ew_current_fierz_channel_decomposition_note_2026-05-01` | positive_theorem / audited_clean / retained |
| 12 | resolved_or_superseded | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited |
| 13 | resolved_or_superseded | `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20` | positive_theorem / audited_renaming / audited_renaming |
| 14 | resolved_or_superseded | `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded |
| 15 | resolved_or_superseded | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | bounded_theorem / audited_clean / retained_bounded |
| 16 | resolved_or_superseded | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | decoration / audited_decoration / retained_pending_chain |
| 17 | resolved_or_superseded | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |
| 18 | resolved_or_superseded | `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | no_go / audited_clean / retained_no_go |
| 19 | resolved_or_superseded | `no_per_site_chirality_theorem_note_2026-05-02` | no_go / audited_clean / retained_no_go |
| 20 | resolved_or_superseded | `pauli_group_order_theorem_note_2026-05-02` | bounded_theorem / audited_clean / retained_bounded |
| 21 | resolved_or_superseded | `q_integer_spectrum_theorem_note_2026-05-02` | bounded_theorem / audited_clean / retained_bounded |
| 22 | resolved_or_superseded | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |

## Retired Dispatch Targets

| # | claim_id | current | reason |
|---:|---|---|---|
| 1 | `higgs_from_lattice_note` | bounded_theorem / audited_clean / retained_bounded | not_a_direct_promotion_candidate |
| 2 | `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09` | bounded_theorem / audited_clean / retained_bounded | not_a_direct_promotion_candidate |
| 3 | `generation_axiom_boundary_note` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the claim. |
| 4 | `native_gauge_closure_note` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the structural gauge-closure claim. |
| 5 | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; current source scope is a finite projection lemma and does not close the kappa_EW matching-rule identification. Positive-theorem promotion remains conditional on a future source repair that closes that identification. |

Full machine-readable queue lives in `data/audit_dispatch_queue.json`.
