# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "record history/order support must not be read as physical time, rates, or a continuous generator"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Use this firewall when reviewing dynamics lanes that cite record histories, counts, or per-step kernels."
```

If true, this artifact prunes time/rate overclaims from record history and
per-step-kernel support. It does not block a future clocked production theorem.
