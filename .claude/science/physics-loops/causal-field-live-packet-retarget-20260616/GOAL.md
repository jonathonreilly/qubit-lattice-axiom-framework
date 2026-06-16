# Goal

Repair stale source references from the archived failed
`CAUSAL_PROPAGATING_FIELD_NOTE.md` packet to the live finite-replay packet.

This block does not re-audit the causal-field lane, alter ledger fields, or
promote any physical field-speed claim. It prevents live downstream docs and
note-generating scripts from treating the archived `0.63 / 0.45` table as
current evidence.
