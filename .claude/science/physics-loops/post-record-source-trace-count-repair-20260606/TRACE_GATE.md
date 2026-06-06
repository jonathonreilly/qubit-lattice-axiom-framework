trace_class: direct_blocker_closure
target_claim_id: post_record_source_measure_trace_normalization_prototype_2026-06-06
target_blocker_text: "Update the source note and expected lane counts to the current measure/weight subdivision snapshot, or add the three missing trace_normalization_reference rows and rerun the primary runner."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Route this stacked repair for re-audit after the measure/weight subdivision repair in PR #2966 is handled."

# Trace Explanation

The blocker was a stale expected count, not a missing RN theorem. The current
measure/weight subdivision snapshot has 14 source-measure/RN rows and 7
trace-normalization rows. This PR updates the source-measure trace note and
runner to that snapshot and refreshes the cache.
