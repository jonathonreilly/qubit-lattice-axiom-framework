# Artifact Plan

- Update the source note status and boundaries to the finite supplied-rule
  witness.
- Add the clean supplied selection-rule interface as an explicit source anchor.
- Refresh the runner cache.
- Run:
  - `python3 scripts/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.py`
  - `python3 scripts/cached_runner_output.py scripts/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.py --check-only`
  - `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.py --check-only`
  - `git diff --check`
  - audit-data diff guard
