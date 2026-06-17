trace_class: direct_blocker_closure
target_claim_id: s3_anomaly_spacetime_lift_note
target_blocker_text: "critical unaudited S3 anomaly spacetime-lift row has a stale failing primary runner and no registered runner path in the current queue"
source_of_blocker_text: audit_ledger
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "Use the repaired primary-runner cache when auditing or re-extracting this row."

This branch supports audit readiness; it does not close the missing dynamics
bridge.
