# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Rows needing probability laws, Born weights, rates, stochastic kernels, typicality, or source/action dynamics must name a separate pre-record/instrument/probability bridge."
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Use this firewall when splitting post-record count support from probability/source/instrument lanes."
```

## Reachability

If true, the block prunes the route:

```text
post-record finite counts alone
  => probability law / Born weights / next-atom selector.
```

It preserves the positive route:

```text
post-record finite counts + supplied statistical model
  => empirical audit or parameter estimation under named assumptions.
```

