# Opportunity Queue

Current block:

1. `axiom_first_cluster_decomposition_theorem_note_2026-04-29`
   - Status in this branch: Step 3 LR tail repaired; L2 remains conditional.
   - Next action: review/audit.

Provisional next candidates after this PR:

1. Scan current audit ledger for rows newly marked `audited_conditional` or
   `audited_failed` and not already covered by open PRs.
2. Prefer runner-artifact or proof-step rows where a direct proof repair can
   remove a bounded/conditional import without adding axioms.
3. Defer rows whose only route is a new axiom, observational fit, or human
   judgment premise.
