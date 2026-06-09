```yaml
trace_class: direct_blocker_closure
target_claim_id: lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07
target_blocker_text: "runner_artifact_issue: include scripts/frontier_lensing_h025_edge_kernel_certificate_2026_06_08.py, its transitive helpers, logs/runner-cache/frontier_lensing_h025_edge_kernel_certificate_2026_06_08.txt, and outputs/lensing_h025_edge_kernel_certificate_2026_06_08.json, then re-audit the fine-H mechanism."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_artifact_repair
next_trace_action: "Submit the branch for reviewer extraction and independent re-audit; do not edit docs/audit."
```

The branch adds a lightweight manifest runner that verifies the H=0.25 runner,
local helper scripts, fresh cache, source slope certificate, and structured JSON
output without rerunning the heavy edge-kernel computation.
