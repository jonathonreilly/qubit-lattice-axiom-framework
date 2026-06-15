trace_class: direct_blocker_closure
target_claim_id: "seven audited-clean retained_pending_chain rows"
target_blocker_text: "effective_status_reason='chain_waiting_on:key_terminology'"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: methodology
next_trace_action: "Re-audit the seven hash-changed rows; no generated verdicts are part of this PR."

The repair removes a non-load-bearing glossary dependency edge from source
notes. It does not claim the rows are retained; it queues them for direct
audit on their real dependencies.
