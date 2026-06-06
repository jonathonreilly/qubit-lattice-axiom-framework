# Handoff

This stacked PR repairs the count-drift blocker for
`post_record_source_measure_trace_normalization_prototype_2026-06-06`.

Stack dependency:

- Base branch: `physics-loop/post-record-measure-weight-count-sync-20260606`
- Upstream PRs: #2987, #2989, and #2991

Changed source surface:

- `docs/POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md`
  now records 21 covered rows and lane counts 14/7.
- `scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py`
  now checks the repaired upstream measure/weight counts and exact current
  source/trace prototype counts.
- `logs/runner-cache/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.txt`
  is refreshed from the repaired runner.

Verification:

```text
python3 scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py
SUMMARY: PASS=49 FAIL=0

python3 scripts/cached_runner_output.py --refresh scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py --tail-chars 4000
refreshed green cache
```

Audit data was not edited. This is not a verdict update.
