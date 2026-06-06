# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "bounded/conditional audit rows need an evidence sufficiency ladder after Record typing"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use the ladder to bucket rows before any audit-lane re-audit or status migration."
```

## Reachability answer

If true, this artifact supports bounded and conditional audit lanes by
preventing evidence-type conflation.

It does not close a specific row, but it tells later audit work which missing
piece a row has: count support, finite law, concentration certificate,
simulation-only support, selector rule, production bridge, or independent
audit result.
