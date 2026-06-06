# Artifact Plan

- Patch `scripts/frontier_record_audit_application_map_2026_06_06.py`.
- Refresh `logs/runner-cache/frontier_record_audit_application_map_2026_06_06.txt`.
- Run hygiene checks:
  - `python3 scripts/frontier_record_audit_application_map_2026_06_06.py`
  - `python3 scripts/cached_runner_output.py scripts/frontier_record_audit_application_map_2026_06_06.py --check-only`
  - `git diff --check`
  - audit-data diff guard
