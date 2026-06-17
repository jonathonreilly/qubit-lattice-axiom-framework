# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: universal_qg_support_chain_missing_runner_batch
target_blocker_text: "queue rows have runner_path=null for existing Universal QG source notes"
source_of_blocker_text: audit_queue_selector
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Rebuild graph/queue after review so the registered runner paths are visible to audit tooling."
```

If accepted, this should move the twelve rows from missing-runner blocked to
runner-backed/auditable, subject to dependency and audit-lane judgment.

