trace_class: direct_blocker_closure
target_claim_id: shapiro_five_family_portability_note
target_blocker_text: "fix the zero-control computation and labeling, restore a frozen log, add PASS/FAIL assertions for zero controls and family spread"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Independent audit decides the effective status of the corrected boundary packet."

The branch directly addresses the executable blocker: the zero-control gate is now a same-source-strength `s=0` instantaneous-vs-finite-c comparison, while the previous nonzero source-off comparison is explicitly labeled as diagnostic.
