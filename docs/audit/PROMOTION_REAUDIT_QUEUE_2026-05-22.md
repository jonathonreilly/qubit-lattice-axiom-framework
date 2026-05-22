# Promotion Re-Audit Queue

**Date:** 2026-05-22
**Status:** dispatcher-only queue for fresh-context audit. This file is not
an audit verdict, does not retag the ledger, and must not be cited as proof
that any row is `retained`.

## Purpose

The rows below are already `audited_clean / retained_bounded`. They do not
enter the live mechanical audit queue, because that queue only pulls pending
or backfill rows. This manifest records a targeted re-audit request: a
fresh-context auditor should decide whether the clarified A1/A2 axiom packet
allows each listed row to remain exactly scoped while changing
`claim_type` from `bounded_theorem` to `positive_theorem`.

The dispatcher may use this file to select claim IDs. The auditor's restricted
packet should not include this file, the review-packet PR text, prior assistant
discussion, prior audit rationales, or publication-facing retained summaries.

## Allowed Context For Each Audit

- The source note for the selected `claim_id`.
- One-hop dependencies from `docs/audit/data/audit_ledger.json`.
- The runner and current runner output, if the row has a runner.
- `docs/audit/README.md`.
- `docs/audit/FRESH_LOOK_REQUIREMENTS.md`.
- `docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md`.
- `docs/audit/ALGEBRAIC_DECORATION_POLICY.md`.
- `docs/MINIMAL_AXIOMS_2026-05-20.md`.
- `docs/QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md`.
- `docs/A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md`, for governance
  boundaries around non-automatic row shifts.

## Dispatch Order

| order | group | rule |
|---:|---|---|
| 1 | local Clifford algebra | Independent first pass. |
| 2 | generation local algebra | Independent finite-algebra pass. |
| 3 | graph-first gauge structure | Run after the local-algebra pass; split any mixed structural/physical row before retagging. |
| 4 | SU(3) toolkit algebra | Run only after the graph-first structural carrier is retained or split cleanly. |

## Target Rows

| group | claim_id | source note | current status | audit question |
|---|---|---|---|---|
| local Clifford algebra | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` | `docs/CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the exact local `Cl(3,0)`/Pauli representation scope qualify as `positive_theorem` under clarified A1? |
| local Clifford algebra | `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | `docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the finite Clifford volume-chirality parity theorem qualify as `positive_theorem` under clarified A1/A2? |
| generation local algebra | `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | `docs/THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the exact translation-character/projector algebra qualify as `positive_theorem` without promoting physical generation claims? |
| generation local algebra | `generation_axiom_boundary_note` | `docs/GENERATION_AXIOM_BOUNDARY_NOTE.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the finite `H_hw=1` translation-character algebra qualify as `positive_theorem`, or does the row need a split first? |
| graph-first gauge structure | `graph_first_selector_derivation_note` | `docs/GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the exact graph-first selector result qualify as `positive_theorem` while leaving downstream abelian interpretation open? |
| graph-first gauge structure | `graph_first_su3_integration_note` | `docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the selected-axis finite-cube structural `su(3)` construction qualify as `positive_theorem` without promoting hypercharge or EW matching? |
| graph-first gauge structure | `native_gauge_closure_note` | `docs/NATIVE_GAUGE_CLOSURE_NOTE.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the structural native gauge-closure scope qualify as `positive_theorem`, or does the row need a structural/physical split first? |
| SU(3) toolkit algebra | `cl3_color_automorphism_theorem` | `docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the algebraic `SU(3)` embedding/channel-count scope qualify as `positive_theorem`, excluding physical color and EW readout? |
| SU(3) toolkit algebra | `su3_casimir_fundamental_algebraic_k1_k3_narrow_proof_walk_bounded_note_2026-05-10` | `docs/SU3_CASIMIR_FUNDAMENTAL_ALGEBRAIC_K1_K3_NARROW_PROOF_WALK_BOUNDED_NOTE_2026-05-10.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the standard fundamental-carrier `SU(3)` Casimir identity qualify as `positive_theorem` on retained algebraic inputs? |
| SU(3) toolkit algebra | `su3_dabc_symmetric_theorem_note_2026-05-02` | `docs/SU3_DABC_SYMMETRIC_THEOREM_NOTE_2026-05-02.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the Gell-Mann-carrier `d^{abc}` algebra qualify as `positive_theorem` on retained algebraic inputs? |
| SU(3) toolkit algebra | `ew_current_fierz_channel_decomposition_note_2026-05-01` | `docs/EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the exact `SU(N_c)` Fierz/channel-count identity qualify as `positive_theorem` without promoting the EW matching rule? |
| SU(3) toolkit algebra | `rconn_vertex_color_singlet_projection_bounded_narrow_theorem_note_2026-05-17` | `docs/RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the finite Hilbert-Schmidt color projection identity qualify as `positive_theorem` without promoting `kappa_EW` matching? |
| SU(3) toolkit algebra | `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | `docs/RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL_NARROW_THEOREM_NOTE_2026-05-17.md` | `bounded_theorem` / `audited_clean` / `retained_bounded` | Does the conjugate-representation cubic-anomaly index identity qualify as `positive_theorem` without promoting matter-existence or chirality claims? |

## Guardrails

- Do not edit `docs/audit/data/audit_ledger.json` from this queue PR.
- Do not change any row to `audit_in_progress` solely to force mechanical
  queue inclusion.
- Do not pass the review-packet PRs as audit evidence. They are operator
  triage only.
- If a fresh auditor finds that a row mixes exact algebra with physical
  interpretation, split the source row first and audit the split algebraic
  row separately.
- If a fresh auditor returns a clean retag recommendation, apply it only
  through `docs/audit/scripts/apply_audit.py` in the audit lane.
