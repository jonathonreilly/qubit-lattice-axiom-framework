# Assumptions And Imports

## Consumed Inputs

- Existing CKM/SU2 source notes and runners.
- Current `docs/audit/data/audit_ledger.json` read-only status lookups from the
  runners.

## Open Inputs

- `LEFT_HANDED_CHARGE_MATCHING_NOTE.md` is not closure-grade for these packets
  on the current effective surface.
- `ONE_GENERATION_MATTER_CLOSURE_NOTE.md` is unaudited in the current ledger.
- `CKM_MAGNITUDES_STRUCTURAL_COUNTS...` is unaudited in the current ledger.
- Several supporting status/literal checks remain open rather than closure
  premises.

## Import Handling

The branch does not retire these imports. It exposes them as blockers and keeps
the algebra conditional.
