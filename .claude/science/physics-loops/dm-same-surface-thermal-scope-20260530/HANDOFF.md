# Handoff

This PR repairs the DM same-surface thermal row by exposing the live-DM premise packet as supplied and preserving the local interval theorem.

Review focus:

- Confirm the note no longer claims full same-surface DM closure from this row alone.
- Confirm the runner still checks the same endpoint/range/root intervals.
- Confirm the row is reset to `unaudited` and ready in the audit queue.

Pipeline result:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `effective_status_reason`: `awaiting_audit`
- audit queue: ready medium-criticality entry

Remaining science:

- Derive the 64:1 channel-weight bridge.
- Derive/register the live-DM constants.
- Prove packet completeness and selector boundary.
