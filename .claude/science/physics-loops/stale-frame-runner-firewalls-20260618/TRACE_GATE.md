# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id:
  - cl4c_carrier_axiom_consequence_map_note_2026-04-28
  - hubble_lane5_c1_a5_minimal_carrier_axiom_audit_note_2026-04-28
  - hubble_lane5_c1_stuck_fanout_synthesis_note_2026-04-28
target_blocker_text: "Registered runners still asserted stale positive closure/minimality/exhaustion behavior for archived failed notes."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: tooling
next_trace_action: "Reviewer/auditor can re-check these rows with runners that witness archive boundaries rather than stale positive claims."
```

This does not propose retained status. It removes a source-side contradiction
that made the failed archived rows harder to process cleanly.
