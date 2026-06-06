# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: chirality_record_typing_interface_2026-06-05
target_blocker_text: "record typing must not turn signed post-record readout into carrier chirality"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Use this interface to separate signed-label audit rows from rows needing chirality/CAR/readout-selection bridges."
```

If true, the artifact prunes signed-readout and post-record-count shortcuts to
chirality while preserving the open carrier routes.
