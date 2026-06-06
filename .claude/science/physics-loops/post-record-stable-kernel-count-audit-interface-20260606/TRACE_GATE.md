# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Finite count-statistic p-values are exact under supplied kernels, but kernel/statistic/threshold/verdict remain separate inputs."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use this interface when a downstream row supplies a finite kernel and count statistic and needs exact finite p-value calibration."
```

## Reachability

If this artifact is true, it supports exact finite audit calibration under
supplied kernels. It does not apply audit verdicts.
