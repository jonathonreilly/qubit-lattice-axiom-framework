# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: dm_neutrino_weak_triplet_coefficient_axiom_boundary_note_2026-04-15
target_blocker_text: "replace stale absolute-path reads with repository-local retained dependencies and rerun the coefficient-normalization checks end to end"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Reviewer should extract the runner/cache repair and send the archived row through re-audit; no audit verdict is applied by this PR."
```

The PR repairs reproducibility of the coefficient-boundary verifier. It does
not close the source-amplitude or benchmark lane.
