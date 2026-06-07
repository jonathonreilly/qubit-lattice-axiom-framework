# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id:
  - post_record_stability_dynamics_selector_subdivision_2026-06-06
  - post_record_measure_weight_normalization_subdivision_2026-06-06
target_blocker_text:
  - "runner_artifact_issue: include the full source for scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py and a bounded ledger-row export for the 90 selected rows, then independently enumerate the regex split."
  - "runner_artifact_issue: include the full selector/dial helper source and the exact ledger slice used by measure_rows(), then independently recheck the 44-row and lane-count table."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent audit can re-check the refreshed 97-row stability slice and 45-row measure slice with the static helper graph visible."
```

The quoted blocker text contains stale row counts from the prior ledger
snapshot. Current `main` recomputation gives `97` stability/dynamics rows and
`45` measure/weight rows; this branch records and verifies those current
counts.
