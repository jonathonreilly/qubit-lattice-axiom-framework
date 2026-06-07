# Handoff

This branch repairs the current post-record selector packet after ledger drift.

Current counts:

- row-bucketing scans `1374` scoped rows and touches `288`;
- selector/dial bucket is `248 = 104 + 97 + 45 + 2`;
- measure/weight bucket is `45 = 10 + 6 + 7 + 15 + 7`;
- stability/dynamics bucket is `97 = 60 + 37`.

Blockers addressed:

- measure/weight now has static helper-source visibility and an exact
  `outputs/post_record_measure_weight_normalization_slice_2026_06_07.json`
  export checked by the runner;
- stability/dynamics now has static helper-source visibility and an exact
  `outputs/post_record_stability_dynamics_selector_slice_2026_06_07.json`
  export checked by the runner.

Verification:

```bash
python3 scripts/frontier_post_record_audit_evidence_ladder_row_bucketing_2026_06_06.py
python3 scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py
python3 scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py
python3 scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_audit_evidence_ladder_row_bucketing_2026_06_06.py,scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py,scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py,scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py --check-only --push-mode=none
git diff -- docs/audit | wc -c
```

Observed results:

- row-bucketing: `SUMMARY: PASS=44 FAIL=0`;
- selector/dial: `SUMMARY: PASS=28 FAIL=0`;
- measure/weight: `SUMMARY: PASS=53 FAIL=0`;
- stability/dynamics: `SUMMARY: PASS=37 FAIL=0`;
- caches: all relevant caches fresh;
- audit diff size: `0`.

Next science action:

Pick a concrete row from the refreshed selector/tangent or flow/thermal queue
and attempt a real retained-premise bridge.
