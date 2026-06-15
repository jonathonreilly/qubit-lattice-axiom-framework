# Trace Gate

```yaml
trace_class: methodology
target_claim_id: null
target_blocker_text: "cycle_break_targets in docs/audit/data/audit_queue.json"
source_of_blocker_text: audit_queue
reachability_to_target: supports
artifact_role: tooling
next_trace_action: "Reviewer lands source-note edge repair; audit pipeline regeneration then clears cycle_break_targets."
```

If the source edits are accepted, the audit graph no longer reports citation cycles for the affected notes. This does not itself audit any claim or change an effective status.
