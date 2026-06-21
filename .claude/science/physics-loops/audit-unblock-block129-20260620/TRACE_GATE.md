trace_class: methodology
target_claim_id: null
target_blocker_text: "runner_breakage_inventory.json reports missing_runner_file/path-resolution blockers that can mislead audit packet selection even when current tooling resolves the runners."
source_of_blocker_text: audit_ledger
reachability_to_target: supports
artifact_role: tooling
next_trace_action: "Use the expanded guard output to treat stale missing-runner inventory rows as source/cache evidence cleanup, not claim-truth blockers."

# Notes

This block does not close or promote a scientific claim. It makes an audit
tooling blocker inspectable: all 94 covered inventory entries now must resolve
to fresh OK cache evidence before the guard passes.
