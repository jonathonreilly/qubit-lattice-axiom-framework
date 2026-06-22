# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Route-2 needs a same-source product/readout primitive that gives E[X]E[Y]=1/9."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Construct the Route-2 same-source color-marginal product theorem, or prove current P_R/E-T readout cannot supply it."
```

Support route:

```text
SU3 rank-one color marginal <P_i> = 1/3
-> disconnected product <P_i><P_j> = 1/9
-> P-cal connected subtraction
-> kappa=0, if Route-2 supplies the same-source transfer and raw moment.
```

Boundary:

```text
The color-marginal product is exact upstream support. Current Route-2 P_R/E-T
readout is not yet typed as that same-source color-marginal readout.
```
