# Assumptions And Imports

## Allowed Inputs

- Current `docs/audit/data/audit_ledger.json` as read-only data.
- Existing post-record selector, stability, flow, evidence-ladder, and stable-feature notes.
- Existing helper runners and SHA-pinned caches.

## Retired Import

- The target row no longer asks the auditor to trust dynamically imported helper runners without a packet certificate. The target runner now checks source existence, source SHA, cache freshness where the cache has a standard header, and required cache stdout markers.

## Still Open

- This remains an exact-support audit-readiness repair, not a selected-dial theorem.
- Independent audit must decide any ledger movement.
