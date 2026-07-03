trace_class: direct_blocker_closure
target_claim_id: nonlabel_grown_basin_note
target_blocker_text: "runner_artifact_issue: provide the completed SHA-pinned live recompute runner source and cache output, or a cached --recompute run for the primary runner, and correct or justify the displayed charge-exponent entries."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Submit for review/re-audit; no audit-ledger edits."

## Trace Explanation

The primary runner now validates the completed live recompute cache as SHA-fresh and passing, then prints the exact live row values. The source note table now matches those live recompute values and no longer displays stale charge-exponent precision.
