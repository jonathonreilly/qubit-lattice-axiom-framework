# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id:
  - gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_note_2026-04-19
  - gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_note_2026-04-19
target_blocker_text: "declared runner path absent from worktree"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should rerun the restored scripts and decide whether the rows move."
```

## Reachability

The audit blocker was not a missing theorem search; it was a missing executable
artifact.  This branch restores the exact declared script paths and provides
fresh SHA-pinned cache logs.

The branch does not decide the final audit status.  It only removes the local
missing-runner obstruction.
