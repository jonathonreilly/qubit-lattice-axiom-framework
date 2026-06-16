# Assumptions And Imports

## Allowed Inputs

- Current source note text in
  `docs/EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`.
- Existing symbolic checks in
  `scripts/frontier_ew_higgs_gauge_mass_diagonalization.py`.
- The audit-ledger hygiene note quoted in `TRACE_GATE.md`.

## Forbidden Inputs

- No electroweak pole masses, RGE values, or observed constants.
- No new axiom.
- No audit verdict, ledger status, or generated audit-output edit.

## Import Disposition

No new physics import is added. The only changed premise is the verifier's
surface-string expectation: it now checks the source note's current
one-doublet tree-level gauge-mass scope instead of an older stale phrase.
