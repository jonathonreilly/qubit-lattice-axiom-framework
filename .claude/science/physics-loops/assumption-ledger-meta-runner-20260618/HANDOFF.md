# Handoff

## What moved

`docs/ASSUMPTION_DERIVATION_LEDGER.md` now explicitly points to
`scripts/assumption_derivation_ledger_meta_check.py` as its primary runner.
The runner now verifies 16 source-boundary checks, including the metadata-only
classification, no current-status table, R_conn/F_adj narrowing, conditional
physical selector boundary, and out-of-scope theorem-grade wiring.

## What did not move

- No audit results, ledger JSON, queue, publication effective-status files,
  front-door status, lane registry, or active review queue were edited.
- No ingredient row is promoted, demoted, retained, or bounded by this PR.
- No new axiom or science import is introduced.

## Reviewer/auditor next action

Treat this as source-side audit tooling/support for the critical metadata row.
If accepted, the audit lane should have an explicit runner surface for the
assumption ledger's metadata-only boundary.
