# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: dm_leptogenesis_pmns_projector_interface_note_2026-04-16
target_blocker_text: "The raw fixed-eigenvector algebra closes, but the note also claims a simple-spectrum intrinsic-to-the-pair projector packet without specifying the eigenvalue label/order convention needed to fix rows and columns. Simple spectra leave independent row/column permutation freedom."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem_and_runner_certificate
next_trace_action: independent audit should verify whether the explicit ascending-eigenvalue labels close the conditional row
```

The repair acts directly on the quoted blocker: it adds the missing label
convention and checks the exact permutation freedom that remains without it.
