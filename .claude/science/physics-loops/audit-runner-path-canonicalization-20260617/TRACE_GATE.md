trace_class: methodology
target_claim_id: null
target_blocker_text: "runner_breakage_inventory.json reports missing_runner_file entries whose basenames exist under scripts/"
source_of_blocker_text: audit_ledger
reachability_to_target: supports
artifact_role: tooling
next_trace_action: "Re-run runner precompute/audit packet rendering so stale absolute and bare runner refs resolve to repo-local scripts."

This PR does not audit any row and does not edit audit verdict data. It fixes
source-side audit tooling so existing row runner paths that are bare filenames
or stale absolute worktree paths resolve to the checked-in runner before source
is embedded in the auditor prompt.
