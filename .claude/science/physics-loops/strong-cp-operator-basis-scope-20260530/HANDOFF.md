# Handoff

This PR repairs the strong-CP operator-basis support row by exposing the supplied action-surface premises and removing non-load-bearing parent dependencies.

Review focus:

- Confirm no exact dependency remains on the strong-CP theta-zero parent row.
- Confirm no exact dependency remains on the broader reflection-positivity parent row.
- Confirm the runner still passes all gates.
- Confirm the row is reset to `unaudited` and audit queue ready.

Pipeline result:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `effective_status_reason`: `awaiting_audit`
- audit queue: ready leaf entry

Remaining science:

- Derive/register the real-positive Wilson selector.
- Derive/register the scalar-mass-only action-class boundary.
