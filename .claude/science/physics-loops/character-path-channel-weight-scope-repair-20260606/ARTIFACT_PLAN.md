# Artifact Plan

- Update source-note type, claim type, and status certificate to bounded
  supplied-normalization semantics.
- Add a runner source-anchor check for the bounded witness wording.
- Refresh the cache.
- Run:
  - `python3 scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py`
  - `python3 scripts/cached_runner_output.py scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py --check-only`
  - `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py --check-only`
  - `git diff --check`
  - audit-data diff guard
