trace_class: direct_blocker_closure
target_claim_id: scalar_trace_tensor_no_go_note
target_blocker_text: "include full load-bearing source and cached outputs for scripts/frontier_tensorial_einstein_regge_completion.py, scripts/frontier_same_source_metric_ansatz_scan.py, and scripts/frontier_coarse_grained_exterior_law.py, or inline the scalar functional, probe-family, and Einstein-residual constructions directly in the no-go runner."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Reviewer/auditor should inspect whether static helper edges and helper caches are sufficient for the restricted packet; independent audit still owns the verdict."

## Repair Route

This branch takes the first audit-suggested route: keep the helper modules as
bounded imported authorities, make them ordinary static imports in the no-go
runner, and add the missing `frontier_same_source_metric_ansatz_scan.py` cache.
