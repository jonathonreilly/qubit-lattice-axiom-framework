# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 7
**Ready entries:** 5
**Resolved/invalid entries:** 17
**Retired entries:** 2

Source sidecars:
- `docs/audit/data/lsp_projective_reaudit_queue_2026-05-22.json`
- `docs/audit/data/promotion_reaudit_queue_2026-05-22.json`
- `docs/audit/data/r1_qubit_k1_reaudit_queue_2026-05-22.json`

## Live Dispatch Entries

| # | ready | group | claim_id | current | source note | audit question |
|---:|:---:|---|---|---|---|---|
| 1 | Y | `r1_per_site_dim_two_consumers` | `pauli_group_order_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional | `docs/PAULI_GROUP_ORDER_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site reading plus retained per-site-uniqueness, does the Pauli group order theorem close on the bounded per-site scope, or does another blocker remain? |
| 2 | Y | `r1_per_site_dim_two_consumers` | `q_integer_spectrum_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional | `docs/Q_INTEGER_SPECTRUM_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site reading plus retained per-site-uniqueness, does the Q-integer-spectrum result close on the bounded per-site scope, or does the staggered-Dirac/Grassmann bridge admission remain load-bearing? |
| 3 | Y | `r1_per_site_dim_two_consumers` | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional | `docs/PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site reading plus retained per-site-uniqueness, does the per-site su(2) spin-half identification close, or does the missing physical-Hilbert bridge remain? |
| 4 | Y | `su3_toolkit_algebra` | `cl3_color_automorphism_theorem` | bounded_theorem / audited_clean / retained_bounded | `docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md` | Does the algebraic SU(3) embedding/channel-count scope qualify as positive_theorem, excluding physical color and EW readout? |
| 5 | Y | `su3_toolkit_algebra` | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `docs/RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md` | Does the finite Hilbert-Schmidt color projection identity qualify as positive_theorem without promoting kappa_EW matching? |
| 6 |  | `lsp_projective_direct_luders` | `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` | bounded_theorem / unaudited / unaudited | `docs/LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` | With LSP-projective ratified for ideal unrefined projective measurements, does the conditional K_P=P bridge become clean scoped support, or does an upstream dependency/status issue still block it? |
| 7 |  | `lsp_projective_born_chain` | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | bounded_theorem / unaudited / unaudited | `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | After the direct Lüders/projective rows are resolved, does the Born derivation still have remaining blockers, or is the projective-measurement part of the chain now closed? |

## Resolved Or Invalid

| # | state | claim_id | current |
|---:|---|---|---|
| 1 | resolved_or_superseded | `luders_rule_from_composition_consistency_note_2026-05-20` | bounded_theorem / audited_clean / retained_pending_chain |
| 2 | resolved_or_superseded | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 3 | resolved_or_superseded | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 4 | resolved_or_superseded | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | positive_theorem / audited_clean / retained |
| 5 | resolved_or_superseded | `graph_first_selector_derivation_note` | positive_theorem / audited_clean / retained |
| 6 | resolved_or_superseded | `graph_first_su3_integration_note` | positive_theorem / audited_clean / retained |
| 7 | resolved_or_superseded | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | decoration / audited_decoration / decoration_under_cl3_color_automorphism_theorem |
| 8 | resolved_or_superseded | `su3_dabc_symmetric_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional |
| 9 | resolved_or_superseded | `ew_current_fierz_channel_decomposition_note_2026-05-01` | positive_theorem / audited_clean / retained |
| 10 | resolved_or_superseded | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited |
| 11 | resolved_or_superseded | `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20` | decoration / audited_decoration / decoration_under_cl3_complexification_split_narrow_theorem_note_2026-05-10 |
| 12 | resolved_or_superseded | `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded |
| 13 | resolved_or_superseded | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | bounded_theorem / audited_clean / retained_bounded |
| 14 | resolved_or_superseded | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded |
| 15 | resolved_or_superseded | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem / audited_clean / retained |
| 16 | resolved_or_superseded | `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | no_go / audited_clean / retained_no_go |
| 17 | resolved_or_superseded | `no_per_site_chirality_theorem_note_2026-05-02` | no_go / audit_in_progress / audit_in_progress |

## Retired Dispatch Targets

| # | claim_id | current | reason |
|---:|---|---|---|
| 1 | `generation_axiom_boundary_note` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the claim. |
| 2 | `native_gauge_closure_note` | bounded_theorem / audited_clean / retained_bounded | bounded_terminal_after_dispatch_audit; positive_theorem promotion is not supported by current source scope. Future promotion requires a source PR that splits or strengthens the structural gauge-closure claim. |

Full machine-readable queue lives in `data/audit_dispatch_queue.json`.
