trace_class: direct_blocker_closure
target_claim_id: post_record_stability_dynamics_selector_subdivision_2026-06-06
target_blocker_text: "runner_artifact_issue: include the full source for scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py and a bounded ledger-row export for the 90 selected rows, then independently enumerate the regex split."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Re-audit using the refreshed caches, which print the full current 248-row selector/dial slice and full current 97-row stability/dynamics slice."

The old 90-row stability/dynamics count is not preserved because latest main
now computes 97 rows. The repair is to make the current slice explicit.
