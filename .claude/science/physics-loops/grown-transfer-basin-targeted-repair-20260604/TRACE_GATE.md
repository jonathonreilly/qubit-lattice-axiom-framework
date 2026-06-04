trace_class: direct_blocker_closure
target_claim_id: grown_transfer_basin_note
target_blocker_text: "`scripts/GROWN_TRANSFER_BASIN_TARGETED.py` still requires `abs(row.action_gamma0) < 1e-12`, the exact complex-action survival criterion that the source note says is wrong."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Reviewer/auditor should inspect whether the repaired same-row predicate plus refreshed caches are sufficient to re-audit the narrow basin as a live packet."

The branch directly repairs the named executable mismatch. It does not decide
the audit verdict and does not edit `docs/audit/**`.

