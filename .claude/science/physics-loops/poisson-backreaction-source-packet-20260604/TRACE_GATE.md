trace_class: direct_blocker_closure
target_claim_id: poisson_backreaction_live_threshold_packet_note_2026-05-29
target_blocker_text: "the runner imports scripts/backreaction_poisson.py for the actual build, propagation, detector, and self-field functions, and that helper source is absent from the restricted packet"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Reviewer/auditor should re-audit the bounded finite-grid packet with the helper source and helper cache exposed."

This branch repairs packet completeness only. It does not edit `docs/audit/**`
or assign an audit verdict.

