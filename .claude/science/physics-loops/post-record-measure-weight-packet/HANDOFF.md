# Handoff

This branch repairs the post-record measure/weight source packet.

Key facts for review:

- The target runner no longer uses `importlib` to hide the selector/dial helper
  from the static citation graph.
- The row-slice certificate is written to
  `outputs/post_record_measure_weight_normalization_slice_2026_06_07.json`.
- The current ledger snapshot has 45 measure/weight rows, not the previously
  recorded 44, because newer audited rows now classify into this bucket.
- The branch does not edit `docs/audit/**` and does not apply audit verdicts.

Suggested reviewer checks:

```bash
python3 scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py
python3 scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py,scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py --check-only --push-mode=none
git diff -- docs/audit | wc -c
```

