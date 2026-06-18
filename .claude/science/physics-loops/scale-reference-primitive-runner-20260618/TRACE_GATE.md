trace_class: direct_blocker_closure
target_claim_id: scale_reference_primitive
target_blocker_text: "runner_path is null for the high-load meta primitive row on current main"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Reviewer/auditor can re-audit the primitive using the primary runner and cached output; no ledger retagging is performed in this PR."
