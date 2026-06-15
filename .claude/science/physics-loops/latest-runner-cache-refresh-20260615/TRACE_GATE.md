trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "three stale SHA-pinned runner caches on current main"
source_of_blocker_text: "precompute_audit_runners.py --all --check-only on origin/main@544b9184"
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "After landing with PR #4005 and PR #3991, rerun the full-ledger cache freshness check."

