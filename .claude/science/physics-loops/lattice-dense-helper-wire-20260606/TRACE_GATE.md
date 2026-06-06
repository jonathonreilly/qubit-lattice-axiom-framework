# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: lattice_3d_dense_spent_delay_z2_z6_endpoint_note_2026-05-29
target_blocker_text: "runner_artifact_issue: include the full scripts/lattice_3d_dense_10prop.py helper source in the restricted packet and ensure helper_runner_paths detects it, then rerun the audit."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Reviewer/auditor can re-audit after the packet builder sees scripts/lattice_3d_dense_10prop.py in helper_runner_paths."
```

This block does not change the finite z=2..6 endpoint claim. It repairs the
restricted-packet helper exposure and cache evidence.

