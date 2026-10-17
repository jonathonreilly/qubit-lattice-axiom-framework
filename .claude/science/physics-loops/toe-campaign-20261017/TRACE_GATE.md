# Trace gate

## C1 — one-qubit NN stabilizer rules
```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "done in C2 (two qubits per site); remaining escapes: blocks, non-Pauli projectors, unsoldered two-qubit sites"
```

## C2 — two qubits per site
```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "test the escapes the theorem leaves open: two qubits per site (soldered spin x flavour), block rules, non-Pauli commuting projectors"
```

## Scope carried into next work
C1 retains elementary immobility and nonzero-charge translation rank <= 2, including lineons and planons. C2 concerns free-single-site-variable-preserving operators, not computed decoherence. C3 retains its odd-L rank-growth argument. C4 unsoldered evidence is a finite 36-rule, same-site, radius-1 tube search at stride 4 in a radius-5 box. No general nearest-neighbour fermion exclusion, physical electric charge or forced time dynamics follows. D2 localization remains open; a single species with an internal doublet is not excluded.
