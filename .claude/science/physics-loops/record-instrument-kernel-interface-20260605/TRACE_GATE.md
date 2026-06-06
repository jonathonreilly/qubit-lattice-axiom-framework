# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "conditional dynamics lanes need a typed interface from supplied instruments to record atoms/history without collapsing probability into the post-record site"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use this interface to audit whether a lane supplies an instrument, a probability kernel, a realized atom, or only post-record propagation."
```

If true, this artifact supports conditional audit lanes by giving them a
finite, typed kernel/record interface. It does not close the physical
instrument, Born/reference, local-observability, production, rate, or time gates.
