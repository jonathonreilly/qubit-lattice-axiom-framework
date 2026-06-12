trace_class: methodology
target_claim_id: post_record_selector_tangent_readout_weight_prototype_2026-06-06
target_blocker_text: "Runner/source-snapshot drift: selector/tangent row count expected 8 while latest ledger enumerates 10."
source_of_blocker_text: audit_ledger
reachability_to_target: supports
artifact_role: tooling
next_trace_action: "Independent audit can rerun the supplied-support packet without a stale row-count failure."

The repair refreshes only read-only scanner snapshots and the bounded exported
slice. It does not close the missing selector/tangent/readout bridge theorem.

