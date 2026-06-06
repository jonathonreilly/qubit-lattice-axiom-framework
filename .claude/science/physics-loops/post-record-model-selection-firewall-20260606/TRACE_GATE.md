# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Do not use post-record likelihood or p-value scores as a canonical model/dial selector without supplied selection rules."
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Use this firewall when downstream dynamics or dial rows try to convert finite scores into canonical model selection without named priors/losses/thresholds/tie/admissibility rules."
```

## Reachability

If this artifact is true, it prunes a common overclaim route. It does not block
conditional model selection once the missing selection rules are supplied.
