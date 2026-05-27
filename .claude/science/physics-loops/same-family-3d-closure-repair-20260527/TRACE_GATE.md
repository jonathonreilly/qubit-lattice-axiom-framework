trace_class: direct_blocker_closure
target_claim_id: same_family_3d_closure_note
target_blocker_text: "missing_dependency_edge: add retained ledger dependencies and packet-included helper/source certificates for each per-L and per-W run, especially rows 2, 6, 7 and the L=8/L=10 same-slice rows."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent auditor reruns the repaired primary runner and checks the retained dependency chain."

The repair directly addresses the blocker by:

- live recomputing rows 2, 6, and 7 in the primary runner;
- live recomputing the `L=8/L=10` same-slice rows at `h=0.25`, `W=10`;
- adding explicit retained dependencies for the action-family, asymptotic
  bridge, and `W=12` wide-tail companion packets;
- regenerating the audit queue so the row is ready for re-audit rather than
  manually retagged.
