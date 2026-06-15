# Trace Gate

trace_class: direct_blocker_closure
target_claim_id: cl3_su3_symmetric_base_commutant_gell_mann_embedding_narrow_theorem_note_2026-05-27
target_blocker_text: "Correct the two normalization formulas, then re-audit the same bounded algebraic embedding packet."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Independent audit re-runs on the corrected source formulas and refreshed runner cache."

## Repair

The source now distinguishes:

- `T_F = 1/2` on the 3D symmetric block;
- `delta_ab` for the 8D embedded trace after the fiber trace;
- structure constants computed using `t=lambda/2`, not bare `lambda`.

The companion runner now checks the full 64-pair 8D Gram matrix and emits:

```text
TOTAL: PASS=110, FAIL=0
```

## Audit Discipline

No generated audit ledgers, queues, publication effective-status mirrors, or
front-door status files are edited.
