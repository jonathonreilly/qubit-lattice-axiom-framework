# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: source_resolved_transverse_propagating_green_note
target_blocker_text: "Current output gives transverse - same = -2.30e-05, -4.60e-05, -9.23e-05, -1.86e-04, not the positive values frozen in the note; support-fraction delta is 0.000e+00; and the printed trans/same column is actually trans_delta / inst_delta."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should evaluate the new corrected boundary row as a fresh bounded packet, not as a retag of the archived failed row."
```

The artifact directly closes the repair target by computing and labeling the
contested ratios separately, then asserting the actual finite boundary.
