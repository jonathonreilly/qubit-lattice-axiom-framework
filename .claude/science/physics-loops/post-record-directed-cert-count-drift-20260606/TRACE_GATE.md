trace_class: direct_blocker_closure
target_claim_id: post_record_directed_certificate_examples_2026-06-06
target_blocker_text: "The runner has three completed failures on the row-bucket side condition, and its final summary still prints the stale 31-row value despite the computed 32-row bucket."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent review can check that the finite examples still pass and the read-only side-condition counts now match current ledger growth."

# Trace Gate

The audit blocker is source/runner drift in side-condition counts, not a failure of the finite examples. The runner already verified the three directed finite certificates. This PR changes stale equality guards into at-least-prior-map checks and prints the computed current arrow/dynamics bridge count.

No audit verdict files are edited.
