# Handoff

This stacked branch repairs the character/path/channel weight packet.

What changed:

- dynamic measure-helper loading was replaced by a static import;
- the note and runner use the current 10-row map;
- `outputs/post_record_character_path_channel_weight_slice_2026_06_07.json`
  is checked by the runner;
- target cache was refreshed.

Verification:

```bash
python3 scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py,scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py,scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py --check-only --push-mode=none
git diff -- docs/audit | wc -c
```

Observed results:

- target runner: `SUMMARY: PASS=54 FAIL=0`;
- caches: all relevant caches fresh;
- audit diff size: `0`.

Next science action:

Pick one row in the 10-row inventory and try to derive its actual weight rule
or selector from retained premises.
