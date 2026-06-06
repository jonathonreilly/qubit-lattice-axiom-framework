# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "supplied kernel-selection rule must not hide Record-derived target vectors or weights"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Keep any future model-selection lane explicit about supplied targets and weights."
```

## Reachability answer

If true, this artifact prunes the route from post-record data to implicit
selection-rule targets or weights. It preserves supplied-rule scoring as a
conditional exact interface.
