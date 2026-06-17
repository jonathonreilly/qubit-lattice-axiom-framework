trace_class: methodology
target_claim_id: universal_qg_optional_textbook_comparison_note
target_blocker_text: "zero-authority optional textbook-comparison metadata row needs explicit runner/cache replay wiring"
source_of_blocker_text: repo_scan
reachability_to_target: supports
artifact_role: tooling
next_trace_action: "Independent audit/review can replay the metadata runner and decide whether the row is now properly discoverable."

## Boundary

This PR supports audit replay/discovery only. It does not add physics content,
does not promote the row, and does not change universal-QG theorem authority.
