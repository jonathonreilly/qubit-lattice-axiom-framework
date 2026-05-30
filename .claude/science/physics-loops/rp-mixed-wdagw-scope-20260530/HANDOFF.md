# Handoff

This PR repairs the RP mixed-observable row by scoping it to the pure finite-carrier `W^dag W` lemma.

Review focus:

- Confirm Wilson-boundary compact-group positivity is only a supplied premise/diagnostic.
- Confirm mixed OS representation is only a supplied premise.
- Confirm runner output still passes all six checks.
- Confirm the row is reset to `unaudited` and audit queue ready.

Pipeline result:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `effective_status_reason`: `awaiting_audit`
- audit queue: ready leaf entry
