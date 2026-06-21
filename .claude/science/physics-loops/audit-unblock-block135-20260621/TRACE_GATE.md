# Trace Gate

```yaml
trace_class: methodology
target_claim_id: null
target_blocker_text: "citation cycles in docs/audit/data/audit_queue.json require source-graph repair before affected rows can leave retained_pending_chain"
source_of_blocker_text: audit_ledger
reachability_to_target: supports
artifact_role: tooling
next_trace_action: "Use the enabled apply path in a follow-up source-note repair PR after support-refresh churn is isolated."
```

If a follow-up source-note PR applies the repair and regenerates the pipeline,
the expected trace is cycle-count reduction. This block only enables the
mechanism.
