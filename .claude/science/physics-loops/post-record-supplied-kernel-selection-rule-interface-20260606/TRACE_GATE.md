# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "after the kernel-selection no-go, positive kernel choice requires a supplied selection rule"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "Use this supplied-rule interface only when a row explicitly supplies the candidate family and rule."
```

## Reachability answer

If true, this artifact supports dynamics rows that explicitly supply a finite
candidate family and rule. It does not derive the rule, candidates, or physical
kernel from Record.
