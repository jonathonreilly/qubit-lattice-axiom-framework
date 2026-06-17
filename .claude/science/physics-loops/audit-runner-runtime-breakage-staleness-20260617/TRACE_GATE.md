trace_class: methodology
target_claim_id: null
target_blocker_text: "runner_breakage_inventory lists timeout/nonzero_exit rows as broken even though current source-side caches may be fresh"
source_of_blocker_text: audit_ledger
reachability_to_target: supports
artifact_role: tooling
next_trace_action: "Use the guard output to separate stale runtime-runner inventory labels from live audit compute blockers."

This artifact does not promote or retain a science claim. It supports audit
unblocking by making stale runtime-runner breakage labels mechanically visible.
