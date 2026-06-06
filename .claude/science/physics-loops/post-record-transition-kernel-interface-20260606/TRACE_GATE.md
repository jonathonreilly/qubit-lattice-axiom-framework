# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional dynamics rows can use post-record counts with a supplied finite transition kernel, but rows that need the kernel itself still need a separate bridge."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use this interface when a downstream row supplies a finite transition law and needs exact record-history/count consequences."
```

## Reachability

If true, the block supports:

```text
supplied finite kernel
  + post-record append/count algebra
    => finite-history probabilities and expected count dynamics.
```

It does not support:

```text
Record alone => transition kernel.
```

