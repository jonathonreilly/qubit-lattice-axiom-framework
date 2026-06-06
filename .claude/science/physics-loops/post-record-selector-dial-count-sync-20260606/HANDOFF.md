# Handoff

This stacked PR repairs the count-drift blocker for
`post_record_selector_dial_bucket_subdivision_2026-06-06`.

Stack dependency:

- Base branch: `physics-loop/post-record-evidence-ladder-count-sync-20260606`
- Upstream PR: #2987

Changed source surface:

- `docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md`
  now records 241 selector/dial rows and sub-buckets 103/94/43/1.
- `scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py`
  now checks the repaired upstream evidence ladder count and exact current
  selector/dial sub-bucket counts.
- `logs/runner-cache/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.txt`
  is refreshed from the repaired runner.

Verification:

```text
python3 scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py
SUMMARY: PASS=28 FAIL=0

python3 scripts/cached_runner_output.py --refresh scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py --tail-chars 4000
refreshed green cache
```

Audit data was not edited. This is not a verdict update.
