# Artifact Plan

- Update the source note from supplied family-lift authority to finite ladder
  compatibility.
- Update runner firewall flags and cache output.
- Run:
  - `python3 scripts/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.py`
  - `python3 scripts/cached_runner_output.py scripts/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.py --check-only`
  - `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.py --check-only`
  - `git diff --check`
  - audit-data diff guard
