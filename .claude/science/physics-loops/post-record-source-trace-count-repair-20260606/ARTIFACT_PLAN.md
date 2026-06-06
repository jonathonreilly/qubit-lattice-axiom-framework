# Artifact Plan

- Update the source-measure trace note from 14+10=24 to 14+7=21.
- Update the runner expectations and source anchors.
- Refresh the source-measure trace runner cache.
- Run:
  - `python3 scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py`
  - `python3 scripts/cached_runner_output.py scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py --check-only`
  - `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py --check-only`
  - `git diff --check`
  - audit-data diff guard
