# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "The form-class is constrained; the member of the class is not selected by record-preservation/locality/Hermiticity alone."
source_of_blocker_text: source_note
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Use this firewall when a downstream dynamics row treats allowed-class membership as action/coupling/truncation selection."
```

## Reachability

If true, the block prunes the route:

```text
record-preservation/gauge-local form constraints
  => selected nonzero Hamiltonian/action/couplings/truncation.
```

It preserves the positive route:

```text
supplied Hamiltonian/action candidate
  -> check allowed-class membership.
```

