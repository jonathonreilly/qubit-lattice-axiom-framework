trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "Two latest-main audited_conditional rows had no open PR touching their source paths: g_bare_rescaling_freedom_removal_theorem_note_2026-05-03 and higgs_channel_effective_ntaste_boundary_bounded_note_2026-05-08."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Submit both source repairs to review/audit. Audit lane owns any verdict or effective-status change."

# Trace Gate

This branch targets the two uncovered `audited_conditional` rows found on
`origin/main` after checking open PR file coverage:

- `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03`
- `higgs_channel_effective_ntaste_boundary_bounded_note_2026-05-08`

The g_bare repair addresses the auditor's missing action-surface step. The
source now distinguishes fixed-`g_bare` Wilson matching, where beta is
unchanged, from the explicitly scoped counter-rescaled-coupling action
surface, where `g_bare,new^2 = g_bare,old^2 / c^2` and WM gives
`beta_new = c^2 beta_old`.

The Higgs repair addresses the auditor's overstatement finding. The source
now says five single-class assignments yield three distinct values because
`k = 0/4` and `k = 1/3` are binomial-degenerate, while no assignment equals
the uniform-16 readout.

This branch does not edit audit output or retag any row.
