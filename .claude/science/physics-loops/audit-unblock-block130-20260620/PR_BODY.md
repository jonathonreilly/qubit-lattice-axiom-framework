## Summary

Makes runner-cache orphan cleanup header-aware so valid nested-runner caches
are not treated as deletable just because `scripts/<stem>.py` is absent.

Before this PR, cleanup dry run reported 11 orphan candidates. Two were false
positives whose cache headers point at existing runners under
`scripts/corrections/`:

- `logs/runner-cache/yt_p1_delta_r_corrected_bound_memsafe.txt`
- `logs/runner-cache/yt_p1_fermion_regulator_verification_memsafe.txt`

After this PR, cleanup dry run reports 9 candidates and preserves those nested
runner caches.

## Boundary

This PR does not audit claims, apply verdicts, delete cache files, or assert
retained/proposed-retained status. It only narrows the cleanup deletion guard.

## Artifacts

- `scripts/precompute_audit_runners.py`
- `docs/audit/scripts/tests/test_audit_pipeline.py`
- `.claude/science/physics-loops/audit-unblock-block130-20260620/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block130-20260620/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block130-20260620/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-block130-20260620/REVIEW_HISTORY.md`

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> OK
- `python3 scripts/precompute_audit_runners.py --cleanup-orphans-dry-run --all --check-only --allow-non-main` -> `Would delete 9 orphan cache file(s)`, `fresh: 3120`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 78 tests passed
- `python3 docs/audit/scripts/audit_lint.py --strict` -> `OK: no errors` with notices only
- `git diff --check` -> OK
