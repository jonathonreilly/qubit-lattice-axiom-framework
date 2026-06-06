# Assumptions And Imports

## Repo Inputs

- `docs/repo/ACTIVE_REVIEW_QUEUE.md` supplies the old sign-bridge queue item.
- `docs/audit/data/audit_ledger.json` supplies current row statuses and the
  parent-row artifact issue.
- `docs/DIMENSION_SELECTION_NOTE.md` supplies the parent row and source-packet
  repair text.
- Existing D3 runners, caches, and verifier outputs are current-main inputs.

## Forbidden Imports

- No observed physical dimension is used.
- No framework-baseline rewrite is assumed.
- No full all-d potential derivation or upper-bound theorem is assumed.
- No audit-ledger verdict is edited or applied by this branch.

## Open Imports

- Independent audit must decide whether the parent row's conditional artifact
  issue is closed.
- Full D=3 selection still needs upper-bound and all-d potential/source
  authority if pursued.

