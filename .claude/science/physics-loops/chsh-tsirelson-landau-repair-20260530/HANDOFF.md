# Handoff

This PR repairs `chsh_tsirelson_lattice_qubits_bound_note_2026-05-20`.

The previous audit failure was caused by a false displayed square identity in
equation (4). The note now derives the correct Landau/Tsirelson identity for
the plus/plus/plus/minus CHSH convention:

```text
C^2 = 4I - [A_1,A_2] tensor [B_1,B_2].
```

The new runner reports `TOTAL: PASS=24, FAIL=0`, including a negative control
showing that the old plus-sign identity is not equal to the displayed square.

After `bash docs/audit/scripts/run_pipeline.sh`, the target row is:

- `audit_status: unaudited`
- `effective_status: unaudited`
- `effective_status_reason: awaiting_audit`
- queue `ready: true`
- `open_dependency_paths: []`

Independent audit remains required before any retained/bounded verdict is
applied.
