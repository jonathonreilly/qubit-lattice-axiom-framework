# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: lattice_3d_dense_spent_delay_z2_z6_endpoint_note_2026-05-29
target_blocker_text: "The displayed runner output matches the source note's finite z=2..6 table and the primary runner does not itself print constants. However, nearly all load-bearing operations are opaque calls into scripts/lattice_3d_dense_10prop.py, including lattice generation, field construction, propagation, detector probabilities, and sign classification. Because that helper source is missing despite being transitive load-bearing code, the restricted packet is artifact-incomplete rather than cleanly auditable. The claim is also correctly bounded and does not overstate an asymptotic theorem."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Independent audit checks whether the source-packet manifest closes the packet-completeness blocker."
```

The artifact directly exposes the named transitive helper and verifies that the
endpoint and helper caches are SHA-fresh. It does not broaden the finite claim.
