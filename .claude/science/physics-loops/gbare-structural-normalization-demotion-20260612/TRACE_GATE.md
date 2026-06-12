trace_class: direct_blocker_closure
target_claim_id: g_bare_structural_normalization_theorem_note_2026-04-18
target_blocker_text: "supply a theorem deriving the Wilson action coefficient or physical connection normalization, rather than defining g = 1 as the unrescaled coordinate choice; also correct the trace-vs-component factor wording."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: demotion
next_trace_action: "Reviewer/auditor can accept this as source-boundary repair/demotion, or require a future positive coefficient-normalization theorem for retained-positive status."

This PR does not derive physical `g = 1`. It removes that overclaim and
preserves the exact structural part: fixed canonical `su(3)` trace Gram,
no scalar generator dilation, and supplied Wilson relation
`beta = 2 N_c / g^2`.
