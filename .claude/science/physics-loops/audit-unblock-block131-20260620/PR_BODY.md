## Summary

Makes runner-cache orphan cleanup preserve cache files that are still
referenced elsewhere in the repository. This prevents cleanup from creating
broken evidence links.

After block130, cleanup dry run reported 9 candidates. One still had a live
note reference:

- `docs/CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`
- `logs/runner-cache/chsh_structural_bound_narrow_2026_05_17.txt`

After this PR, cleanup dry run reports 8 candidates and preserves that linked
cache file.

## Boundary

This PR does not audit claims, apply verdicts, delete cache files, or assert
retained/proposed-retained status. It only narrows the cleanup deletion guard.

## Artifacts

- `scripts/precompute_audit_runners.py`
- `docs/audit/scripts/tests/test_audit_pipeline.py`
- `.claude/science/physics-loops/audit-unblock-block131-20260620/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block131-20260620/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block131-20260620/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-block131-20260620/REVIEW_HISTORY.md`

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> 2 tests passed
- `python3 scripts/precompute_audit_runners.py --cleanup-orphans-dry-run --all --check-only --allow-non-main` -> `Would delete 8 orphan cache file(s)`, `fresh: 3050`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 79 tests passed
- `git diff --check` -> OK

This branch is stacked on PR #4500, whose base includes the refreshed
full-ledger cache baseline from PR #4498.
