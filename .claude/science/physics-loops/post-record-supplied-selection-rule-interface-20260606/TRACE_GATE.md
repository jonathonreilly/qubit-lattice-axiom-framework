# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Stable dial or model locations are available under supplied finite scores and selection rules; they are not forced by Record alone."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use this interface when a downstream row supplies candidate scores and a rule, especially for stable dial-location claims with a positive margin."
```

## Reachability

If this artifact is true, it supports conditional model/dial selection once
the missing score and rule inputs are supplied. It does not promote any row that
lacks those inputs.
