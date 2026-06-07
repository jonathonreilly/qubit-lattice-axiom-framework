# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Can multi-loop graded-net cocycle consistency force CAR and hence supply the staggered anticommutation filter?"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Pivot to the canonical orientation/source-section theorem route."
```

## Reachability

If this artifact is true, it prunes one route to the staggered chirality
selector:

```text
multi-loop exchange consistency
  -> uniform q in {+1,-1}
  -/-> q=-1
  -/-> CAR
  -/-> {D,gamma5}=0
```

It does not close chirality or spin-statistics globally.  It prevents this
specific route from being reused as if it supplied the missing selector.
