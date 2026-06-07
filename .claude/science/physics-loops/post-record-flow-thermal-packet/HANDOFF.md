# Handoff

This stacked branch repairs the flow/thermal stable-setting certificate packet.

What changed:

- static import replaces the dynamic stability helper load;
- the target helper graph now includes the stability helper and transitive
  selector helper;
- the note and runner use the current 60-row flow/thermal map:
  `18 + 3 + 4 + 14 + 21`;
- `outputs/post_record_flow_thermal_stable_setting_slice_2026_06_07.json`
  is checked by the runner.

Verification:

```bash
python3 scripts/frontier_post_record_flow_thermal_stable_setting_certificate_2026_06_06.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_flow_thermal_stable_setting_certificate_2026_06_06.py,scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py,scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py --check-only --push-mode=none
git diff -- docs/audit | wc -c
```

Observed results:

- target runner: `SUMMARY: PASS=55 FAIL=0`;
- caches: all relevant caches fresh;
- audit diff size: `0`.

Next science action:

Pick one `thermal_or_score_stable_feature` or `flow_or_records_stable_feature`
row and try to derive its supplied rule from retained premises.
