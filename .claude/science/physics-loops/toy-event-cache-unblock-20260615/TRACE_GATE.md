trace_class: direct_blocker_closure
target_claim_id: repo.root_file_guide
target_blocker_text: "missing SHA-pinned cache for toy_event_physics.py"
source_of_blocker_text: "precompute_audit_runners.py --all --check-only on main"
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "After this and PR #3991 land, rerun the full-ledger cache freshness check."

