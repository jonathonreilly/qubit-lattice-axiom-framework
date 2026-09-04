# LSP-Projective Ratification Re-Audit Request Manifest

**Date:** 2026-05-22
**Type:** meta (audit-request navigation doc)
**Status:** source-side request; independent audit lane owns each re-audit verdict
**Companion to:** [`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md`](QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md) section "Hardening III: LSP-projective instrument selection"
**Axiom surface:** [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) Axiom 1 and LSP-projective ratification clause
**Depends on:** landed commit `886ce7effc73430c07953e9f1db39cea5f4ee0d1`, which ratifies LSP-projective on the canonical framework hardening surface

## Purpose

Commit `886ce7effc73430c07953e9f1db39cea5f4ee0d1` ratifies
**LSP-projective** as the framework rule for ideal unrefined sharp
projective measurements: for projection `P`, the projective-measurement
instrument is `K_P = P`, and sequential composition with effect `E` is
`P E P`.

This manifest catalogs rows whose current status may be affected by
that ratification. It asks the independent audit lane to re-check those
rows against the updated framework surface.

This doc does **not**:

- Re-audit any row (auditor-owned verdicts)
- Promote any row (status authority remains with the audit lane)
- Modify any existing source note's theorem content
- Predict a new verdict for any candidate

This doc **does**:

- Identify the current Lüders/projective rows whose present blockers
  cite the missing `K_P = P` / `M_{P,E} = P E P` bridge
- Identify the downstream Born-chain row that may become eligible only
  after the direct Lüders/projective rows are resolved
- Provide a single place for the audit lane to drive targeted re-audit
  under the updated LSP-projective ratification
- Carry graph-visible links to the landed framework authority documents
  for audit discoverability; this meta note is not itself theorem
  authority

## Re-audit candidates under LSP-projective

Each row below currently has a non-retained or unreviewed status that
the LSP-projective ratification may address if independent audit
accepts it as load-bearing framework-rule authority. All ledger
statuses were verified against `docs/audit/data/audit_ledger.json` on
2026-05-22 after commit `886ce7effc73430c07953e9f1db39cea5f4ee0d1`.

### A. Direct Lüders/projective rows

#### A.1 `luders_rule_from_composition_consistency_note_2026-05-20`

- **Current:** `audited_conditional`
- **Current blocker:** the row's audit status records a missing bridge
  for using `M_{P,E} = P E P` as framework authority.
- **Ratification effect to test:** LSP-projective now supplies the
  ideal unrefined sharp-projective instrument selection `K_P = P`.
- **Re-audit question:** Does the parent Lüders sequential-composition
  row close for the ideal projective scope under the ratified
  LSP-projective rule, or does another blocker remain?

#### A.2 `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22`

- **Current:** `unaudited`
- **Runner:** registered on the bridge row in the audit ledger
- **Ratification effect to test:** The conditional bridge's antecedent
  `K_P = P` is now supplied by the LSP-projective ratification for the
  ideal unrefined projective scope.
- **Re-audit question:** Does the conditional bridge become a standard
  audited support theorem for the projective-P case, or does an
  upstream dependency/status issue still block it?

### B. Downstream Born-chain candidate

#### B.1 `born_rule_from_gleason_busch_derivation_note_2026-05-20`

- **Current:** `unaudited`
- **Ratification effect to test:** LSP-projective may remove one
  projective-measurement blocker only after the direct Lüders/projective
  rows are independently resolved.
- **Re-audit question:** After the direct Lüders/projective rows settle,
  does the Born derivation still have remaining blockers, or is the
  projective-measurement part of the chain now closed?

## Reviewer ask

This manifest is the framework's request to the audit lane to
**targeted-re-audit the rows in sections A and B above** with
LSP-projective cited as the updated framework-rule authority.
Specifically:

1. Confirm the LSP-projective ratification from commit
   `886ce7effc73430c07953e9f1db39cea5f4ee0d1` is now in effect on the
   canonical framework hardening surface.
2. Re-evaluate the direct Lüders/projective rows under that ratification.
3. Revisit the Born-chain row only after the direct
   Lüders/projective rows are resolved, and only for the blocker this
   ratification can actually address.
4. Record any re-audit verdicts in the standard audit ledger format.

The framework does **not** propose specific new verdicts; the manifest
only identifies which rows are eligible for re-audit and which
verdict-text clauses the LSP-projective ratification may address.

## What this PR is not

- **Not a self-promotion** of any row. All status changes are audit-lane
  decisions.
- **Not a derivation.** LSP-projective is a load-bearing framework-rule
  selection recorded in commit `886ce7effc73430c07953e9f1db39cea5f4ee0d1`;
  this manifest only catalogs possible downstream audit questions.
- **Not a new axiom.** The two-axiom framework remains Axiom 1
  (one qubit per `Z^3` site) plus Axiom 2 (`Z^3` spatial substrate).
  LSP-projective is an explicitly ratified projective-measurement rule
  on that qubit-lattice surface.
- **Not theorem authority.** This is a navigation / audit-request doc.
  Graph-visible links below are present so the audit pipeline can
  discover the landed framework authority; they do not make this meta
  note a premise for the candidate rows.

## Pointer references

- [`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md`](QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md) — landed ratification doc carrying LSP-projective in section "Hardening III"
- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — canonical axiom doc with inline LSP-projective clause
- `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md` — audited_conditional parent whose blocker is targeted by this ratification
- `LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` — runner-backed conditional bridge for `K_P = P`
- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream Born-chain candidate; still independently audited

## What independent audit ownership means here

The audit lane retains sole authority over each re-audit verdict. This
manifest is the framework's audit-request artifact: it identifies
eligibility under the updated LSP-projective reading. The audit lane
evaluates the ratification on its own terms, applies its standard
verdict rules, and records whatever outcome those rules produce. The
manifest does not predict, prescribe, or constrain that outcome.
