# Artifact Plan

- Update the generation/Koide source note from 105+3=108 to 103+3=106.
- Update selector class expected counts in the runner.
- Refresh the runner cache.
- Run:
  - `python3 scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py`
  - `python3 scripts/cached_runner_output.py scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py --check-only`
  - `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py --check-only`
  - `git diff --check`
  - audit-data diff guard
