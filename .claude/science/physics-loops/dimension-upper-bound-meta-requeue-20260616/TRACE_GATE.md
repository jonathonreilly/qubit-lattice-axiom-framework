trace_class: direct_blocker_closure
target_claim_id: dimension_upper_bound_dependency_edge_repair_note_2026-06-08
target_blocker_text: "retag/requeue this row as a meta dependency-edge certificate"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: demotion
next_trace_action: "Independent audit/requeue decides the row type; separate parent theorem work remains outside this packet."

Explanation: This PR repairs the source-side classification only. It does not
edit the audit ledger or queue.
