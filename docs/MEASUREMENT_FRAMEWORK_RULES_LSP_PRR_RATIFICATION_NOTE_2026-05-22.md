# Measurement Framework-Rule Ratifications: LSP + PRR (2026-05-22)

**Date:** 2026-05-22
**Type:** meta (framework-rule ratification, paired with re-audit dispatch manifest)
**Status:** source-side ratification; independent audit lane owns each downstream re-audit verdict
**Companion to:** `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening II" (R1 ratification, PR #1656); `R1_REAUDIT_MANIFEST_NOTE_2026-05-22.md` (PR #1657)

## Purpose

PR #1656 + #1657 ratified the **per-site k = 1 selection (R1)** as load-bearing axiom content under A1 and queued the associated re-audits. Two parallel ratifications are needed on the measurement / record side of the framework to unlock the Born derivation chain:

1. **LSP — Lüders Sequential-Product instrument selection.** The framework's measurement instrument for projective measurement of `P` is the Lüders Kraus operator `K_P := P`.
2. **PRR — Pre-Record Reference inner-unitary invariance.** The pre-record reference state `ρ_ref|_Λ` on every finite region is fixed by every inner unitary automorphism `U ρ_ref|_Λ U† = ρ_ref|_Λ`.

Both rules have **landed conditional bridges** that derive everything *given* the rule (PR #1651 for LSP via the Lüders sequential-product conditional bridge with 39/0 runner; PR #1635-salvage for PRR via the inner-aut tracial conditional theorem with 24/0 runner). What's missing is the explicit framework-rule recording so the audit lane reads them as load-bearing rather than as separate admissions to be re-litigated per-row.

This note ratifies both rules and ships the dispatch manifests so the items don't get lost while the audit-dispatch infrastructure (reviewer-owned) lands.

## Ratification 1 — LSP (Lüders Sequential-Product instrument selection)

### Clause

> **(R2) Lüders Sequential-Product (LSP) instrument selection.** For projective measurement of an orthogonal projection `P ∈ A_Λ` on a finite qubit-lattice region, the framework's measurement instrument is the **Lüders Kraus operator** `K_P := P`. Sequential composition of "outcome `P` then effect `E`" is then `M_{P, E} := K_P† E K_P = P E P` (the standard PEP composition).

### Why this is a framework rule, not a theorem

The literature explicitly shows the sequential product on the effect algebra `E(H)` is **not unique** (Gudder counterexamples in arXiv:0905.0596; broader landscape in arXiv:math/0211033). PR #1626 (Greechie/Gudder uniqueness route) was rejected by the review-loop on exactly this ground. The framework's salvage path was to ratify LSP as an explicit instrument-selection rule, which PR #1651 (conditional Lüders bridge with worked counterexample) prepared.

The runner-verified counterexample T5 in PR #1651 makes the load-bearing role visible: an alternative Kraus `K_P^twist := H · P` (Hadamard-twisted) also satisfies `K_P† K_P = P` but gives a **different** sequential composition. Selecting `K_P = P` is therefore a framework-rule commitment, not a derivable theorem.

### Status

LSP is recorded as an **explicit framework rule** on the same authority surface as the A1 per-site qubit commitment. It is load-bearing, not derivable from operator-algebra structure alone, and approved as a strengthening of the framework's measurement-instrument commitment.

## Ratification 2 — PRR (Pre-Record Reference inner-unitary invariance)

### Clause

> **(R3) Pre-Record Reference (PRR) inner-unitary invariance.** For every finite region `Λ ⊂ Z³`, the pre-record reference state `ρ_ref|_Λ` is invariant under every inner unitary automorphism: `U ρ_ref|_Λ U† = ρ_ref|_Λ` for every unitary `U ∈ U(A_Λ)`.

### Why this is a framework rule, not a theorem

"Pre-record" means "before any record formation has occurred"; the reference state has no information about preferred basis / direction / eigenstate. The framework's commitment is that this no-information state is symmetric under all inner unitary frame rotations on every finite region — equivalent to the standard quantum-information "maximally mixed" reading. This is a principled framework commitment, not a theorem on A1+A2 alone.

The conditional inner-aut tracial theorem (the salvaged PR #1635, runner PASS=24) derives `ρ_ref|_Λ = I_d / d` from PRR by Schur's lemma. The framework-rule status of PRR is what makes the parent `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20` audited_conditional verdict closeable on re-audit.

### Status

PRR is recorded as an **explicit framework rule** on the same authority surface as the A1 per-site qubit commitment. It is load-bearing, not derivable from A1+A2 alone, and approved as the framework's commitment to a no-information pre-record reference.

## Dispatch manifests

### LSP dispatch (re-audit candidates under (R2))

| Row | Current verdict | (R2) effect |
|---|---|---|
| `luders_rule_from_composition_consistency_note_2026-05-20` | `audited_conditional`, `missing_bridge_theorem` on `M_{P,E} = P E P` | Step-1 sequential-effect composition `M_{P,E} = P E P` becomes the load-bearing consequence of (R2); the missing-bridge admission is supplied as framework rule |
| `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` (PR #1651, in flight) | unaudited | Eligible for audit as conditional support **plus** explicit (R2) ratification; the conditional becomes unconditional under (R2) |

### PRR dispatch (re-audit candidates under (R3))

| Row | Current verdict | (R3) effect |
|---|---|---|
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` | `audited_conditional`, `missing_bridge_theorem` on the no-extra-structure identification | (R3) supplies the explicit framework rule replacing the open premise; identification with the unique tracial state is the load-bearing consequence |
| `inner_automorphism_invariance_tracial_identification_narrow_theorem_note_2026-05-20` (salvaged PR #1635) | unaudited | Currently a *conditional* bounded theorem on PRR; (R3) approves the premise, so the conditional becomes unconditional |

### Downstream-of-Born consumers (eligible after LSP + PRR + R1 retain their respective parents)

These rows depend on the Born / measurement chain that LSP + PRR + R1 collectively unlock:

| Row | Current verdict | Path to unlock |
|---|---|---|
| `persistent_record_as_kraus_operator_note_2026-05-20` | `audited_conditional`, `missing_bridge_theorem` | PR #1650 (landed Stinespring V construction with 29/0 runner) supplies the bridge; re-audit on retained inputs |
| `born_rule_from_gleason_busch_derivation_note_2026-05-20` | unaudited | Retains once Gleason + Busch + Stinespring + Kraus-Choi + LSP + PRR are all retained-grade |

## Reviewer ask

Confirm with the audit lane that, on land:

1. **(R2) LSP** is recorded as a load-bearing framework rule for measurement-instrument selection, on the same authority surface as A1
2. **(R3) PRR** is recorded as a load-bearing framework rule for the pre-record reference state, on the same authority surface as A1
3. The LSP + PRR dispatch manifests above should be picked up by the audit-loop's normal re-audit cadence (or via the reviewer's audit-dispatch infrastructure once it lands)

Same pattern as PR #1656 (R1) + #1657 (R1 manifest). No new content beyond what's already encoded in the landed conditional bridges; this PR just promotes the conditionals to ratified framework rules and surfaces the dispatch items.

## Honest scope

This note **does not**:

- Derive (R2) or (R3) from A1+A2 — both are explicit framework-rule strengthenings
- Re-audit any row — verdicts remain audit-lane-owned
- Re-derive Lüders or Schur-Tomita-Takesaki content — both are cited via landed conditional bridges
- Replace the audit-dispatch infrastructure (reviewer-owned; this note just records the items so they're not lost)
- Add numerical, empirical, or dynamical commitments beyond the measurement / record framing
- Promote the Born derivation parent — needs the whole chain retained

This note **does**:

- Ratify LSP and PRR as load-bearing framework rules on the measurement / record surface
- List the dispatch items each ratification enables
- Cross-link to the landed conditional bridges (PR #1651 LSP, PR #1635 PRR) that exhibit the conditional algebra and counterexamples

## Citation-graph note

Plain-text pointer references (NOT load-bearing deps; this note is a meta ratification + manifest):

- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening II" — sibling R1 ratification this note pattern-matches
- `R1_REAUDIT_MANIFEST_NOTE_2026-05-22.md` — sibling R1 dispatch manifest this note pattern-matches
- `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md` — Lüders parent whose missing-bridge (R2) supplies
- `LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` (PR #1651) — landed conditional bridge for (R2)
- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` — pre-record tracial parent whose missing-bridge (R3) supplies
- `INNER_AUTOMORPHISM_INVARIANCE_TRACIAL_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-20.md` (salvaged PR #1635) — landed conditional bridge for (R3)
- `PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md` (PR #1650, landed) — Stinespring V construction relevant to downstream Born chain
- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream Born derivation that retains once the chain is closed
- `MINIMAL_AXIOMS_2026-05-20.md` — canonical axiom doc; LSP and PRR are framework rules, not new axioms

## What this file is not

- Not a re-axiomatization (LSP and PRR are framework rules, not new axioms)
- Not a derivation
- Not a runner-bearing claim (the runners live on the landed conditional bridges)
- Not the audit-dispatch infrastructure itself (reviewer-owned)
- Not an automatic promotion of any audited_conditional row
- Not a numerical-prediction change
