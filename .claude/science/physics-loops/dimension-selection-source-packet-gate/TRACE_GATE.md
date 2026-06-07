trace_class: direct_blocker_closure
target_claim_id: dimension_selection_note
target_blocker_text: "runner_artifact_issue: include scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py, scripts/frontier_dimension_selection.py, logs/runner-cache/frontier_dimension_selection.txt, and the source-packet verifier/cache so the finite-k replay and displayed beta/I_3 table can be checked from code."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Re-audit using the source-packet gate cache reporting SCORECARD: PASS=58 FAIL=0."

The artifact closes only the packet exposure issue. It does not prove full
dimension selection.
