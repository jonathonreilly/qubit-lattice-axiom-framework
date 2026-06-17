# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: universal_gr_tensor_variational_candidate_note
target_blocker_text: "queue row has runner_path=null even though scripts/frontier_universal_gr_tensor_variational_candidate.py exists"
source_of_blocker_text: audit_queue_selector
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Rebuild graph/queue after review so the primary runner path is visible to audit tooling."
```

If this source repair is accepted, it should turn the row from missing-runner
blocked to runner-backed/auditable. It does not assert that the claim is
retained or that the GR route is closed.
