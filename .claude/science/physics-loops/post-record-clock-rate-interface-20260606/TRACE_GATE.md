# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Rows that report rates must identify the clock denominator and cannot cite append/count algebra as a clock or transition-rate derivation."
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Use this interface when splitting event-indexed record dynamics from clocked physical dynamics."
```

## Reachability

If true, the block prunes the route:

```text
post-record event counts alone
  => physical clock / transition rate / Hamiltonian time step.
```

It preserves the positive route:

```text
post-record event stream + supplied clock map
  => conditional empirical rates.
```

