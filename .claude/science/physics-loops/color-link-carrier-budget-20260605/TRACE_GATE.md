# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: color_link_index_routing_carrier_budget_2026-06-05
target_blocker_text: "base-SU(3) link-index routing needs a carrier budget and cannot use a single primitive qubit endpoint"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Attempt graph-canonical two-qubit endpoint projection or demote one-qubit color-link rows to open routing imports."
```

If true, the artifact closes the one-qubit link-color route and gives a
minimal carrier target for future constructive work.
