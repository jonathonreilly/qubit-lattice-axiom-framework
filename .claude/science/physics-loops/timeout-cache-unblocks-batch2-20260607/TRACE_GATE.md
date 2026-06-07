trace_class: direct_blocker_closure
target_claim_id: lattice_3d_l2_tail_stats_note
target_blocker_text: "register a primary runner or cached/reduced reproduction that emits the width-8 tail table and fit within the audit cap, or explicitly mark it as a slow runner with justification"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Independent auditor/reviewer should re-audit the L2 tail row from the repaired packet."

Secondary target: `fm_transfer_note` and `persistent_record_matched_compare_note`
timeout-cache hygiene. These are already audited rows; the PR improves
replayability but does not ask for status change.
