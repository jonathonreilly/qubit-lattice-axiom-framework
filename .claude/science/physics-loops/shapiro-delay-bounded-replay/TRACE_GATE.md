trace_class: direct_blocker_closure
target_claim_id: shapiro_delay_note
target_blocker_text: "hard-coded replay and retained/lab-bridge overclaim prevented bounded source audit"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Reviewer should decide whether the computed bounded replay can be queued for re-audit."

This block closes the hard-coded-runner and stale-dependency part of the source
blocker. It does not close physical Shapiro-law, uniqueness, or lab-bridge
claims.
