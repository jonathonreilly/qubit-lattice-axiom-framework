# GOAL — Axiom-Update Proposals (block01, 2026-06-20)

**Date:** 2026-06-20
**Slug:** `axiom-update-proposals`
**Branch:** `physics-loop/axiom-update-proposals-block01-20260620`
**Mode:** axiom-update-proposal (owner-authorized to go beyond the no-new-axiom rule)
**Target:** best-honest-status — deliver **either** new no-new-axiom derivations
(cracks, higher value) **or** candidate axiom-update PROPOSALS for the walled
high-fanout bridges.

## Goal

The owner authorized: "don't believe the no-gos; keep working until we have a set
of new derivations or update proposals for the axioms." For each walled
high/medium-fanout bridge from the single-clock (B-AXIS), anomaly (ABJ), Koide,
and observable-principle campaigns:

1. run a **genuine skeptical no-new-axiom re-attack FIRST** (could the campaign
   no_go be over-strong, like the two B-AXIS no_gos already corrected?);
2. only where the wall **survives**, design the **weakest sufficient** candidate
   axiom/primitive that discharges it, and build a **conditional** derivation
   (runner + `hypothetical_axiom_status`) showing the walled bridge follows;
3. prefer the WEAKEST sufficient addition; **maximize fanout-unlocked per unit of
   axiom strength**;
4. build REAL runners (numpy/sympy) with `TOTAL: PASS=.. FAIL=..`, captured to
   `logs/runner-cache/`; **no empirical imports**.

## Status discipline (binding — physics-loop SKILL.md / AXIOM_MINIMALITY_POLICY.md)

- Every consequence of an UNADOPTED candidate axiom carries
  `hypothetical_axiom_status: "conditional on accepted new axiom; not retained on
  the actual current surface."`
- **No bare `retained` / `promoted`.** Labeling a consequence "conditional" does
  **not** promote the axiom — only an external owner/governance decision can.
- `proposal_allowed = false`: the owner makes the governance decision; this lane
  only **requests** it (records each candidate as an "unmade science-level
  decision" per policy §1/§4; approval routes through §6).
- The independent audit lane / owner is the **sole** status authority. This lane
  sets no audit verdict and edits no axiom registry.
- **READ-ONLY** on `docs/audit/data/`. No git checkout/commit/push/fetch
  (orchestrator owns git).

## This block's deliverable (SYNTHESIS author)

Consolidate the three cluster proposals into one governance-facing set:

- `docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md` — the minimal axiom-
  update proposal SET (the ~3 candidate axioms), each with precise statement,
  walls discharged (+ fanout), conditional derivation + runner PASS/FAIL,
  minimality, falsifiers, tensions/consistency with retained no-gos; a ranked
  coverage map (proposal -> total fanout unlocked) + grand total; and the
  no-new-axiom CRACKS a skeptical re-attack found (flagged as new derivations).
- pack files: `CLAIM_STATUS_CERTIFICATE_block01.md`, `STATE.yaml`, `GOAL.md`.
- `vocab_lint --fix`; verify no forbidden file touched.

## The three candidate axioms (the minimal set)

| Cluster | Candidate | Gate (open per MINIMAL_AXIOMS_2026-06-05.md) | Strength |
|---|---|---|---|
| **C1** | **RP-DYN** record-production / decoherence dynamics | arrow / measurement / decoherence / record-production dynamics | weak |
| **C2** | **READOUT-MEASURE** readout-context / objectivity / sector-measure | readout context / sector measure / objectivity / occupancy | weak-medium |
| **C3** | **PIN-GAUGE-CONTENT** gauge-content / particle-content | gauge group / particle content / species (+ source/action via FS) | heavy |

Fanout-per-unit-strength: **C2 ≈ C1 > C3.** Recommended owner sequence: C1 then
C2 (weak, high-leverage); defer C3 until the SK-2 (and SK-1/SK-3) no-new-axiom
cracks are attempted.

## Out of scope

- Adopting any candidate; setting any audit verdict; editing any axiom file or
  `docs/audit/data/`.
- Deriving any kernel / rate / weight / value: the arrow's **sign** (past
  hypothesis), Born weights, the dimensionful tick `2a_τ` (SK-1), `n_color`,
  generation count, mixing angles, CP phase `δ`, masses, couplings.
- Re-deriving content already retained (the non-abelian gauge content; the
  determinant FORM, which is already a no-new-axiom theorem — SK-3).

## Stop conditions

- synthesis delivered and pack written (this block's completion);
- queue exhausted (all walls either cracked, escalated to a weakest-sufficient
  proposal, or shown to survive the re-attack and depend on owner judgment);
- worktree externally changes.

A wall that survives the skeptical re-attack is **not** a stop — it is escalated
to a weakest-sufficient candidate proposal and recorded for the owner. A
no-new-axiom **crack** retires the corresponding proposal and is reported as the
higher-value outcome.
