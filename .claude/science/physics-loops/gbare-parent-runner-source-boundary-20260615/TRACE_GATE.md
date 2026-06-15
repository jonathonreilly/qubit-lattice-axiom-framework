trace_class: direct_blocker_closure
target_claim_id: g_bare_derivation_note
target_blocker_text: "Section G: ledger visibility for the new theorem rows"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Reviewer/auditor should re-check the bounded parent row with the clean runner cache and without treating generated ledger status as source evidence."

## Notes

The previous runner emitted two bounded `FAIL` lines when the dependency rows
were not `unaudited`, even though audit generated those statuses. This branch
removes that source/audit-layer conflation.
