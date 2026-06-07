# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: dimension_selection_note
target_blocker_text: "runner_artifact_issue: include scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py, scripts/frontier_dimension_selection.py, logs/runner-cache/frontier_dimension_selection.txt, and the source-packet verifier/cache so the finite-k replay and displayed beta/I_3 table can be checked from code."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should rebuild helper_runner_paths from scripts/frontier_dimension_selection_lower_bound_parent_repair.py and verify parent/source-packet caches."
```

The branch repairs packet reachability only. The parent runner now statically
imports the original dimension runner, finite-k bridge runner, and source-packet
manifest runner. The parent cache checks original/bridge cache freshness and
exposes the manifest source; the manifest cache independently checks the parent,
original, and bridge caches plus the generated JSON.
