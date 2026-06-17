# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20
target_blocker_text: "critical queue row has runner_path=null for the U4 qubit-reframe source note"
source_of_blocker_text: audit_queue_selector
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Rebuild graph/queue after review so the new runner path is visible to audit tooling."
```

If accepted, this should move the row from missing-runner blocked to
runner-backed/auditable. It does not retag downstream staggered rows.

