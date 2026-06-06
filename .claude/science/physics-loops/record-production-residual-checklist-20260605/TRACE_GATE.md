# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "dynamics and audit rows need to know whether they have a kernel, produced record, local observable record, or clocked rate"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use the checklist to classify future record-production and dynamics claims."
```

If true, this artifact supports audit classification. It does not close any
production, local-observability, or rate gate by itself.
