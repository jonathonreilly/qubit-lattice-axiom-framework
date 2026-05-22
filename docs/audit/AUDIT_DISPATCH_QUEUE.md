# Audit Dispatch Queue

This queue is generated from machine-readable dispatcher manifests. It is a target-selection surface only: dispatcher manifests must not be passed to auditors as evidence.

**Live entries:** 13
**Ready entries:** 4
**Resolved/invalid entries:** 0

Source sidecars:
- `docs/audit/data/promotion_reaudit_queue_2026-05-22.json`

## Live Dispatch Entries

| # | ready | group | claim_id | current | source note | audit question |
|---:|:---:|---|---|---|---|---|
| 1 | Y | `local_clifford_algebra` | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | bounded_theorem / audited_clean / retained_bounded | `docs/CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md` | Does the exact local Cl(3,0)/Pauli representation scope qualify as positive_theorem under clarified A1? |
| 2 | Y | `local_clifford_algebra` | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | bounded_theorem / audited_clean / retained_bounded | `docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md` | Does the finite Clifford volume-chirality parity theorem qualify as positive_theorem under clarified A1/A2? |
| 3 | Y | `generation_local_algebra` | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | bounded_theorem / audited_clean / retained_bounded | `docs/THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md` | Does the exact translation-character/projector algebra qualify as positive_theorem without promoting physical generation claims? |
| 4 | Y | `generation_local_algebra` | `generation_axiom_boundary_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GENERATION_AXIOM_BOUNDARY_NOTE.md` | Does the finite H_hw=1 translation-character algebra qualify as positive_theorem, or does the row need a split first? |
| 5 |  | `graph_first_gauge_structure` | `graph_first_selector_derivation_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md` | Does the exact graph-first selector result qualify as positive_theorem while leaving downstream abelian interpretation open? |
| 6 |  | `graph_first_gauge_structure` | `graph_first_su3_integration_note` | bounded_theorem / audited_clean / retained_bounded | `docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` | Does the selected-axis finite-cube structural su(3) construction qualify as positive_theorem without promoting hypercharge or EW matching? |
| 7 |  | `graph_first_gauge_structure` | `native_gauge_closure_note` | bounded_theorem / audited_clean / retained_bounded | `docs/NATIVE_GAUGE_CLOSURE_NOTE.md` | Does the structural native gauge-closure scope qualify as positive_theorem, or does the row need a structural/physical split first? |
| 8 |  | `su3_toolkit_algebra` | `cl3_color_automorphism_theorem` | bounded_theorem / audited_clean / retained_bounded | `docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md` | Does the algebraic SU(3) embedding/channel-count scope qualify as positive_theorem, excluding physical color and EW readout? |
| 9 |  | `su3_toolkit_algebra` | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | bounded_theorem / audited_clean / retained_bounded | `docs/SU3_CASIMIR_FUNDAMENTAL_ALGEBRAIC_K1_K3_NARROW_PROOF_WALK_BOUNDED_NOTE_2026-05-10.md` | Does the standard fundamental-carrier SU(3) Casimir identity qualify as positive_theorem on retained algebraic inputs? |
| 10 |  | `su3_toolkit_algebra` | `su3_dabc_symmetric_theorem_note_2026-05-02` | bounded_theorem / audited_clean / retained_bounded | `docs/SU3_DABC_SYMMETRIC_THEOREM_NOTE_2026-05-02.md` | Does the Gell-Mann-carrier d^{abc} algebra qualify as positive_theorem on retained algebraic inputs? |
| 11 |  | `su3_toolkit_algebra` | `ew_current_fierz_channel_decomposition_note_2026-05-01` | bounded_theorem / audited_clean / retained_bounded | `docs/EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md` | Does the exact SU(N_c) Fierz/channel-count identity qualify as positive_theorem without promoting the EW matching rule? |
| 12 |  | `su3_toolkit_algebra` | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `docs/RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md` | Does the finite Hilbert-Schmidt color projection identity qualify as positive_theorem without promoting kappa_EW matching? |
| 13 |  | `su3_toolkit_algebra` | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | bounded_theorem / audited_clean / retained_bounded | `docs/RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL_NARROW_THEOREM_NOTE_2026-05-17.md` | Does the conjugate-representation cubic-anomaly index identity qualify as positive_theorem without promoting matter-existence or chirality claims? |

Full machine-readable queue lives in `data/audit_dispatch_queue.json`.
