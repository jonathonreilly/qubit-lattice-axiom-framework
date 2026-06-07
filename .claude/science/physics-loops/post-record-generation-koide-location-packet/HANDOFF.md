# Handoff

This stacked branch repairs the generation/Koide stable-location index packet.

What changed:

- dynamic helper loads were replaced by static imports;
- the current index is `104` selector rows plus `4` stable-feature rows, total
  `108`;
- all four stable-feature authority notes are source-anchored;
- `outputs/post_record_generation_koide_stable_location_index_slice_2026_06_07.json`
  is checked by the runner.

Verification:

```bash
python3 scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py,scripts/frontier_post_record_flow_thermal_stable_setting_certificate_2026_06_06.py,scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py --check-only --push-mode=none
git diff -- docs/audit | wc -c
```

Observed results:

- target runner: `SUMMARY: PASS=78 FAIL=0`;
- caches: all relevant caches fresh;
- audit diff size: `0`.

Next science action:

Pick one indexed row and try to derive its selector or stable-rule premise from
retained authority.
