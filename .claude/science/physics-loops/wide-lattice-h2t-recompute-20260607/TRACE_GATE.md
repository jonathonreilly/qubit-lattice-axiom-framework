trace_class: direct_blocker_closure
target_claim_id: wide_lattice_h2t_distance_law_note
target_blocker_text: "runner_artifact_issue: include a completed --recompute cache or the full SHA-pinned frozen replay log with all distance and F~M rows, plus an independent tail-fit check from those raw deltas."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Submit review PR; independent audit can inspect the repaired verifier/cache."

The runner now recomputes distance-tail and F~M fits from parsed frozen rows.
