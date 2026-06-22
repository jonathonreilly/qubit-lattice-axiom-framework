# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Route-2 needs a same-source product/readout primitive that makes the disconnected singlet line the one-point product for the same source."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Construct the Route-2 same-source one-point product theorem E[X]E[Y]=1/9, or prove it cannot be supplied from current physical source/readout structure."
```

Support route:

```text
same-source X,Y with E[XY]=1 and E[X]E[Y]=1/9
-> P-cal connected subtraction
-> connected response 8/9
-> kappa=0.
```

Boundary:

```text
This support avoids the binary/log-odds selector, but it still requires a
Route-2 same-source one-point product theorem.
```
