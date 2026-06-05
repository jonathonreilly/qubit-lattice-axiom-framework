# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: charged_lepton_generation_dynamics_arrow_measure_gate
target_blocker_text: "Why should charged-lepton record dynamics use equal record-letter/block-count weighting rather than dimension/Born weighting?"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Audit the gamma-prior classifier, then attack physical derivation of gamma=0."
```

## Reachability

This theorem reduces the arrow/measure gate to one scalar:

```text
gamma=0 -> record-letter/block-count -> Q=2/3
gamma=1 -> dimension/Born            -> Q=1
```

It does not derive which gamma is physical. Therefore it supports, but does
not close, charged-lepton value selection.
