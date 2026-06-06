# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "expected post-record frequency => concentration / p-value / audit verdict"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Use supplied finite-law enumeration or supplied concentration hypotheses for any future calibrated audit lane."
```

## Reachability answer

If true, this artifact prunes one route: it blocks treating expected
post-record count formulas as concentration, finite p-values, or audit
calibration.

It does not close a retained lane and does not demote any conditional
concentration result. It says that calibration must come from additional
structure: a finite law, a transition kernel with enough dependence control, or
an explicit concentration theorem with its hypotheses declared.
