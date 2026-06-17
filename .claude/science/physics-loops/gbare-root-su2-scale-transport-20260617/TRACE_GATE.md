trace_class: direct_blocker_closure
target_claim_id: g_bare per-site-to-gauge SU2 scale-transport subclaim
target_blocker_text: "The only non-circular route to forcing N_F is to make the per-site spin-double-cover normalization propagate to the gauge su(3) trace surface by derivation rather than by bridge admission."
source_of_blocker_text: audit_strategy_panel
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Reviewer/auditor should decide whether this finite root-SU2 bridge is admissible as the scale-transport input for the downstream g_bare parent chain."

## Trace Notes

This block directly addresses the finite scale part of the blocker by proving
that every coordinate root `SU(2)` subgroup inside graph-first `V_3` gauge
`SU(3)` carries the same Pauli/2 bracket, trace Gram, spectrum, and primitive
spin period as the per-site spin double cover.

It does not close the parent `g_bare` route by itself. The remaining action is
to recheck downstream consumption by the Wilson/Ward `g_bare` chain.
