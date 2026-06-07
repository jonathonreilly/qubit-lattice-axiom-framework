trace_class: direct_blocker_closure
target_claim_id: post_record_measure_weight_normalization_subdivision_2026-06-06
target_blocker_text: "runner_artifact_issue: include the full selector/dial helper source and the exact ledger slice used by measure_rows(), then independently recheck the 44-row and lane-count table."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Re-audit using the refreshed cache, which prints the full current 45-row slice."

The old 44-row count is not preserved because the latest ledger snapshot now
computes 45 rows. The repair is to make the current slice explicit.
