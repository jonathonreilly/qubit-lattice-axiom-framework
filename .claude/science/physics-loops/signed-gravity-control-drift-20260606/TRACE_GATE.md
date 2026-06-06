trace_class: direct_blocker_closure
target_claim_id: signed_gravity_aps_locked_source_action_proposal_note
target_blocker_text: "There is also minor source-runner drift in displayed Born/norm control numbers: the note lists I3=1.794e-43 and max drift=2.887e-15, while the cached runner reports I3=5.381e-43 and max drift=3.331e-15."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: tooling
next_trace_action: "Re-audit the source-runner drift repair; the source-action premise remains open."

This branch only aligns displayed control telemetry with the existing runner
output. It does not change the action ansatz or its open-gate status.
