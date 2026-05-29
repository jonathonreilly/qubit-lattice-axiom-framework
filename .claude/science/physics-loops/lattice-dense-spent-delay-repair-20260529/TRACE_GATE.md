# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: lattice_3d_dense_spent_delay_note
target_blocker_text: "source note claimed z=2..6 attractive window but live runner only tested z=2..5"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should decide whether the dedicated endpoint packet repairs the old z=6 runner artifact blocker."
```

The new artifact does not retag the old ledger row. It gives the auditor a new, bounded positive packet with the missing endpoint computed and asserted.
