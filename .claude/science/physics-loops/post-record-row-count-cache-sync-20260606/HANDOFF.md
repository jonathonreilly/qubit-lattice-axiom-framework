# Handoff

This branch repairs the post-record current-snapshot row-count/cache chain:

- Base row bucketing now passes at `SCOPED_ROWS=1353`, `TOUCHED_ROWS=276`.
- Selector/dial subdivision now passes at `SELECTOR_DIAL_ROWS=237`.
- Measure/weight subdivision now passes at
  `MEASURE_WEIGHT_NORMALIZATION_ROWS=43`.
- Stability/dynamics subdivision now passes at
  `STABILITY_DYNAMICS_SELECTOR_ROWS=90`.
- Flow/thermal stable-setting certificate now passes at
  `FLOW_OR_THERMAL_STABILITY_ROWS=56`.
- Directed certificate examples now pass at
  `ARROW_OR_DYNAMICS_BRIDGE_ROWS=34`.
- Selector/tangent/readout prototype now passes at
  `SELECTOR_TANGENT_READOUT_WEIGHT_ROWS=7`.
- Dynamics stack and closeout indexes now pass against refreshed cached
  summaries.

Verification command:

```text
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_audit_evidence_ladder_row_bucketing_2026_06_06.py,scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py,scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py,scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py,scripts/frontier_post_record_flow_thermal_stable_setting_certificate_2026_06_06.py,scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py,scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py,scripts/frontier_post_record_dynamics_authority_stack_map_2026_06_06.py,scripts/frontier_post_record_dynamics_campaign_closeout_index_2026_06_06.py,scripts/frontier_post_record_dynamics_family_lift_closeout_index_2026_06_06.py --check-only
```

Next action after reviewer handoff: rescan remaining `audited_conditional`
rows for independent science-fix opportunities.
