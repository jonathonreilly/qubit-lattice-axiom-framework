# SU(2) gauge-aligned response lane: the five primary notes

This folder holds the five primary notes of the SU(2) gauge-aligned response
lane of the mass-gap program (PR #10149). The lane wrote them under `docs/`.
They were moved here on 2026-11-13 with no change to their text.

**This is a research record, not framework science.** No axiom of this
repository enters these notes. They have no rows in the audit ledger and no
audit status. Words inside the notes such as `Status: proposed_retained`,
`bounded_theorem` and `bounded-support` are the lane's own working labels,
kept as written. They grant nothing here.

**No mass gap is proved.** Each note states a finite two-step result for a
supplied SU(2) model. The newest note says what is open: "Inherited-action
closure, unbounded blocking depth, physical-scale limits, continuum QFT
construction and a positive physical Yang-Mills gap remain open."

## Why the notes are here

The owner decided on 2026-11-07 (PR #10141) that Yang–Mills mathematics with
no framework axiom lands as its own research section, not through the
framework science pipeline. The section of the mass-gap program is
`research/mass-gap/`. The owner confirmed that place for these notes on
2026-11-13. The notes give written proofs and have no runner.

## The notes

| Note | Title |
|---|---|
| [Coercivity](SU2_TWO_PLAQUETTE_MARGINAL_COERCIVITY_BOUNDED_THEOREM_NOTE_2026-11-09.md) | Compact coercivity of the two-plaquette SU(2) marginal |
| [Regional and chart estimates](SU2_MARGINAL_REGIONAL_AND_CHART_ESTIMATES_BOUNDED_THEOREM_NOTE_2026-11-09.md) | Regional and nonlinear chart estimates for the two-plaquette SU(2) marginal |
| [Marginal connected response](SU2_MARGINAL_CONNECTED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-09.md) | Compact connected response of the two-plaquette SU(2) marginal |
| [Connected four-response](SU2_CONNECTED_FOUR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-09.md) | Connected four-insertion response of the compact two-step SU(2) posterior |
| [Nonidentity compact control](SU2_NONIDENTITY_COMPACT_CONTROL_BOUNDED_THEOREM_NOTE_2026-11-09.md) | Compact control of the SU(2) marginal at small nonidentity backgrounds. The newest note |

## Proofs, checks and sources

The proofs, the lane's research check records and its source searches are in
the lane's working folder. Start with
[PROOF_TREE.md](../../../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/PROOF_TREE.md),
[HANDOFF.md](../../../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/HANDOFF.md)
and
[REVIEW_HISTORY.md](../../../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/REVIEW_HISTORY.md).
The handoff records that the owner re-pointed this lane to the main gap
program on 2026-11-11, and that nothing in the lane's record is withdrawn.

## Verification

None yet. No note here names a compute check or a Lean file. That is an open
obligation under the row "Proof verification" of
`docs/ai_methodology/SETTINGS.md`: each of the five results needs a check that
could show it wrong, which means finite instances of its bound and a control
that fails when the statement is perturbed, or a Lean certificate.

## Links and hashes

The notes are unchanged byte for byte, so the SHA-256 values that the lane's
check records give for them still match. The cost is in the links:

- Links inside the notes were written for `docs/`. A link that starts with
  `../.claude/` points to `.claude/` at the repository root.
- Files in the working folder name the notes by their old path,
  `docs/<file name>`. Read that as
  `research/mass-gap/su2-aligned-response/<file name>`.
