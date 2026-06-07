trace_class: direct_blocker_closure
target_claim_id: gate_b_no_restore_joint_package_note
target_blocker_text: "runner_artifact_issue: add a completed --recompute output or a cached recompute certificate and have the verifier compare each frozen row against those computed values."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent auditor should re-audit the row using the recompute certificate and refreshed default runner cache."

This block adds the completed recompute certificate, refreshes stale Born
residual rows exposed by that recompute, and modifies the default runner to
compare the source log against the certificate.
