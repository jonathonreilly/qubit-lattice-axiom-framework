# Handoff

This stacked PR repairs the stale row map for
`post_record_generation_koide_stable_location_index_2026-06-06`.

Stack dependency:

- Base branch: `physics-loop/post-record-selector-dial-count-sync-20260606`
- Upstream PRs: #2984, #2987, and #2989
- Included dependency commit: `8ad479dd9 repair post-record flow thermal count sync`

Changed source surface:

- `docs/POST_RECORD_GENERATION_KOIDE_STABLE_LOCATION_INDEX_2026-06-06.md`
  now records 103 Koide/generation selector rows, 4 stable-feature rows, and
  107 combined index rows.
- `scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py`
  now checks the repaired selector count, repaired flow/thermal stable-feature
  count, exact selector class counts, and the fourth stable-feature id.
- `logs/runner-cache/frontier_post_record_generation_koide_stable_location_index_2026_06_06.txt`
  is refreshed from the repaired runner.

Verification:

```text
python3 scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py
SUMMARY: PASS=60 FAIL=0

python3 scripts/cached_runner_output.py --refresh scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py --tail-chars 4000
refreshed green cache
```

Audit data was not edited. This is not a verdict update.
