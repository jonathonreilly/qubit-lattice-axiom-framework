# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: lensing_finite_path_explanation_note
target_blocker_text: "runner_artifact_issue: include scripts/lensing_long_path_test.py and its fresh runner cache/output so the T_phys=7.5 measured slope -1.4356 and finite-path prediction -1.7336 can be verified within the restricted packet."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should rebuild helper_runner_paths from scripts/lensing_analytical_finite_path.py and verify the long-path companion packet in the refreshed analytical cache."
```

The branch repairs packet reachability only. The primary analytical runner now
imports `lensing_long_path_test.py`, causing the audit helper resolver to include
the long-path source. The runner also checks that the long-path cache is fresh
against the current source and contains the measured/predicted short-path slope
snippets named by the blocker.
