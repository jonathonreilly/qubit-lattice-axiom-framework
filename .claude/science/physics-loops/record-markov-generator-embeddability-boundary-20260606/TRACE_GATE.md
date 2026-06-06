# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Can a discrete record-production kernel be treated as a continuous-time rate law without an embeddability/generator/clock gate?"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Require explicit generator, embeddability, and clock-rate normalization for continuous record-production dynamics claims."
```

This block prunes the route that treats a stochastic transition matrix as a
physical rate law without checking generator embeddability and clock
normalization.
