# Handoff

This branch repairs the current-main cache chain behind two latest audit failures:

- `post_record_dynamics_campaign_closeout_index_2026-06-06`
- `post_record_dynamics_family_lift_closeout_index_2026-06-06`

It includes the already-open child repairs for the directed examples and stack-map cache drift, then updates the closeout runners to consume the repaired directed summary `SUMMARY: PASS=60 FAIL=0`.

Verification to rerun:

```text
python3 scripts/cached_runner_output.py scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py --check-only
python3 scripts/cached_runner_output.py scripts/frontier_post_record_dynamics_authority_stack_map_2026_06_06.py --check-only
python3 scripts/cached_runner_output.py scripts/frontier_post_record_dynamics_campaign_closeout_index_2026_06_06.py --check-only
python3 scripts/cached_runner_output.py scripts/frontier_post_record_dynamics_family_lift_closeout_index_2026_06_06.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py scripts/frontier_post_record_dynamics_authority_stack_map_2026_06_06.py scripts/frontier_post_record_dynamics_campaign_closeout_index_2026_06_06.py scripts/frontier_post_record_dynamics_family_lift_closeout_index_2026_06_06.py --check-only
git diff --check
git diff --name-only origin/main | rg '^docs/audit/' || true
```

No audit results are applied here. The reviewer/auditor owns any status movement.
