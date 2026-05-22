# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 16
**Ready entries:** 12
**Resolved/invalid entries:** 10

Source sidecars:
- `docs/audit/data/lsp_projective_reaudit_queue_2026-05-22.json`
- `docs/audit/data/promotion_reaudit_queue_2026-05-22.json`
- `docs/audit/data/r1_qubit_k1_reaudit_queue_2026-05-22.json`

## Live Dispatch Entries

| # | ready | group | claim_id | current | source note | audit question |
|---:|:---:|---|---|---|---|---|
| 1 | Y | `r1_substep1_chain` | `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20` | positive_theorem / unaudited / unaudited | `docs/U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md` | Under the ratified k=1 qubit-per-site clause now on the canonical axiom surface, does the U4 closure row qualify as audited_decoration under cl3_complexification_split (as the prior audit verdict explicitly named), or does it require a different category? |
| 2 | Y | `r1_substep1_chain` | `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17` | bounded_theorem / unaudited / unaudited | `docs/STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md` | With the k=1 qubit-per-site clause ratified on the axiom surface, does the substep-1 U4 conditional sub-claim (k=1 implies dim_C H_x = 2) close under the qubit-per-site reading, or does another blocker remain? |
| 3 | Y | `r1_substep1_chain` | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | bounded_theorem / unaudited / unaudited | `docs/STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md` | With the k=1 qubit-per-site clause ratified on the axiom surface and the substep-1 dependency chain routed through the retained cl3_complexification_split parent, does the Grassmann-forcing substep-1 bridge close under the qubit-per-site reading, or does another blocker remain? |
| 4 | Y | `r1_substep1_chain` | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | bounded_theorem / unaudited / unaudited | `docs/STAGGERED_DIRAC_SUBSTEP1_JW_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md` | With the k=1 qubit-per-site clause ratified on the axiom surface and the substep-1 dependency chain routed through the retained cl3_complexification_split parent, does the Jordan-Wigner substep-1 bridge close under the qubit-per-site reading, or does another blocker remain? |
| 5 | Y | `generation_local_algebra` | `generation_axiom_boundary_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GENERATION_AXIOM_BOUNDARY_NOTE.md` | Does the finite H_hw=1 translation-character algebra qualify as positive_theorem, or does the row need a split first? |
| 6 | Y | `r1_per_site_dim_two_consumers` | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional | `docs/CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site axiom-content reading plus the retained axiom_first_cl3_per_site_uniqueness chain, does the per-site Hilbert dim-two theorem close cleanly, or does the missing physical-Hilbert bridge remain? |
| 7 | Y | `r1_per_site_dim_two_consumers` | `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional | `docs/NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site reading plus retained per-site-uniqueness, does the no-per-site-bosonic-CCR trace obstruction close (finite-dim trace + dim_C H_x = 2 forces no CCR rep), or does another blocker remain? |
| 8 | Y | `r1_per_site_dim_two_consumers` | `no_per_site_chirality_theorem_note_2026-05-02` | no_go / audited_conditional / audited_conditional | `docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site reading plus retained per-site-uniqueness, does the no-per-site-chirality result close, or does the missing physical-Hilbert-to-Pauli bridge remain? |
| 9 | Y | `r1_per_site_dim_two_consumers` | `pauli_group_order_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional | `docs/PAULI_GROUP_ORDER_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site reading plus retained per-site-uniqueness, does the Pauli group order theorem close on the bounded per-site scope, or does another blocker remain? |
| 10 | Y | `r1_per_site_dim_two_consumers` | `q_integer_spectrum_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional | `docs/Q_INTEGER_SPECTRUM_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site reading plus retained per-site-uniqueness, does the Q-integer-spectrum result close on the bounded per-site scope, or does the staggered-Dirac/Grassmann bridge admission remain load-bearing? |
| 11 | Y | `r1_per_site_dim_two_consumers` | `per_site_su2_spin_half_theorem_note_2026-05-02` | positive_theorem / audited_conditional / audited_conditional | `docs/PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md` | Under the k=1 qubit-per-site reading plus retained per-site-uniqueness, does the per-site su(2) spin-half identification close, or does the missing physical-Hilbert bridge remain? |
| 12 | Y | `graph_first_gauge_structure` | `native_gauge_closure_note` | bounded_theorem / audited_clean / retained_bounded | `docs/NATIVE_GAUGE_CLOSURE_NOTE.md` | Does the structural native gauge-closure scope qualify as positive_theorem, or does the row need a structural/physical split first? |
| 13 |  | `lsp_projective_direct_luders` | `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` | bounded_theorem / unaudited / unaudited | `docs/LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` | With LSP-projective ratified for ideal unrefined projective measurements, does the conditional K_P=P bridge become clean scoped support, or does an upstream dependency/status issue still block it? |
| 14 |  | `lsp_projective_born_chain` | `born_rule_from_gleason_busch_derivation_note_2026-05-20` | bounded_theorem / unaudited / unaudited | `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | After the direct Lüders/projective rows are resolved, does the Born derivation still have remaining blockers, or is the projective-measurement part of the chain now closed? |
| 15 |  | `su3_toolkit_algebra` | `cl3_color_automorphism_theorem` | bounded_theorem / audited_clean / retained_bounded | `docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md` | Does the algebraic SU(3) embedding/channel-count scope qualify as positive_theorem, excluding physical color and EW readout? |
| 16 |  | `su3_toolkit_algebra` | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `docs/RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md` | Does the finite Hilbert-Schmidt color projection identity qualify as positive_theorem without promoting kappa_EW matching? |

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

Full machine-readable queue lives in `data/audit_dispatch_queue.json`.
