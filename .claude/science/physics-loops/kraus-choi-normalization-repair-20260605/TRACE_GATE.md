# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20
target_blocker_text: "The source is not clean as written because its Choi normalization conventions conflict: the theorem statement defines |Omega> without 1/sqrt(d), Step 1 defines it with 1/sqrt(d), and the displayed inverse map lacks the corresponding factor d for the normalized convention."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Independent audit decides whether the repaired convention and finite runner close the row or whether standard theorem imports still need packet authority."
```

The artifact directly closes the normalization-conflict blocker. It does not
re-prove the standard Kraus/Choi theorems.
