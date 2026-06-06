trace_class: direct_blocker_closure
target_claim_id: post_record_dynamics_authority_stack_map_2026-06-06
target_blocker_text: "The runner output reports SUMMARY: PASS=46 FAIL=1 because the directed-certificate examples cached log does not contain the expected SUMMARY: PASS=59 FAIL=0."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Review this PR after or with PR #2957 so the upstream directed-certificate cache expected by the stack map is present."

# Trace Gate

The blocker is a stale upstream cache expectation. PR #2957 updates the directed-certificate examples cache to `SUMMARY: PASS=60 FAIL=0`; this stacked PR updates the stack map to require that current upstream cache and refreshes its own cache.

No audit verdict files are edited.
