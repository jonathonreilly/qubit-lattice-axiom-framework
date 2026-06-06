# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: color_mr_carrier_routing_split_2026-06-05
target_blocker_text: "MR_color is too coarse; split supported carrier content from link/readout/dynamics residuals"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use the split to target link-index routing directly or to triage rows that need only carrier block content."
```

If true, the artifact does not close physical color. It makes the residual
more attackable by showing which subpiece is already supported and which
subpieces remain open.
