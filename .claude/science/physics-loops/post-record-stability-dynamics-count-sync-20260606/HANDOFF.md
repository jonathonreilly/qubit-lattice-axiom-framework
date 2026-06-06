# Handoff

This stacked PR repairs the count-drift blocker for
`post_record_stability_dynamics_selector_subdivision_2026-06-06`.

Stack dependency:

- Base branch: `physics-loop/post-record-selector-dial-count-sync-20260606`
- Upstream PRs: #2987 and #2989

Changed source surface:

- `docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md`
  now records 94 stability/dynamics rows and sub-buckets 58/36.
- `scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py`
  now checks the repaired upstream selector/dial count and exact current
  stability/dynamics sub-bucket counts.
- `logs/runner-cache/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.txt`
  is refreshed from the repaired runner.

Verification:

```text
python3 scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py
SUMMARY: PASS=25 FAIL=0

python3 scripts/cached_runner_output.py --refresh scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py --tail-chars 4000
refreshed green cache
```

Audit data was not edited. This is not a verdict update.
