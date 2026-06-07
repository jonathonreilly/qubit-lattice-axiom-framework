trace_class: direct_blocker_closure
target_claim_id: post_record_flow_thermal_stable_setting_certificate_2026-06-06
target_blocker_text: "runner_artifact_issue: include scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py and its transitive helpers, if any, in the restricted packet, then re-audit the current row-map computation."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Re-audit using the refreshed cache, which checks and prints the full current 59-row flow/thermal ledger slice."

The old 56-row count is not preserved because the latest ledger snapshot now
computes 59 rows. The repair is to make the current slice explicit.
