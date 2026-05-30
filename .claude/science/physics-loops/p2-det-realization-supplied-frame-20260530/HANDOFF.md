# Handoff

This PR repairs the P2 determinant-realization bridge by converting hidden premises into explicit supplied frame data.

Review focus:

- Confirm no exact dependency remains on the conditional substep-2 or same-day sibling rows.
- Confirm `D=M_KS` and AC relabeling are explicit premises, not derived claims.
- Confirm runner output still passes all finite algebra checks.
- Confirm the row is reset to `unaudited` and audit queue ready.

Pipeline result:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `effective_status_reason`: `awaiting_audit`
- audit queue: ready leaf entry
