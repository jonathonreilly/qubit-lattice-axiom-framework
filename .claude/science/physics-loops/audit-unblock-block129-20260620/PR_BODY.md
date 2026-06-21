## Summary

This is a source-side audit-unblock PR. It expands
`scripts/audit_runner_runtime_breakage_staleness_guard_2026_06_17.py` so the
guard covers all actionable runner-breakage inventory reason classes:
`missing_runner_file`, `nonzero_exit`, and `timeout`.

The refreshed transcript shows:

- 94 covered inventory rows checked
- 55 `missing_runner_file`
- 3 `nonzero_exit`
- 36 `timeout`
- 94 fresh OK cache entries

No audit verdicts or claim-status rows are edited.

## Base Note

This PR is now rebased directly on `main` at `dea100014`. It does not depend on
block128 / PR #4498.

## Artifacts

- `.claude/science/physics-loops/audit-unblock-block129-20260620/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block129-20260620/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block129-20260620/CLAIM_STATUS_CERTIFICATE.md`
- `scripts/audit_runner_runtime_breakage_staleness_guard_2026_06_17.py`
- `logs/runner-cache/audit_runner_runtime_breakage_staleness_guard_2026_06_17.txt`

## Verification

```bash
python3 scripts/audit_runner_runtime_breakage_staleness_guard_2026_06_17.py
python3 scripts/precompute_audit_runners.py --runners scripts/audit_runner_runtime_breakage_staleness_guard_2026_06_17.py --check-only --allow-non-main
python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main
python3 scripts/audit_runner_path_canonicalization_guard_2026_06_17.py
python3 -m py_compile scripts/audit_runner_runtime_breakage_staleness_guard_2026_06_17.py scripts/runner_cache.py
python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Post-rebase results: the guard, cache freshness checks, path canonicalization
guard, py-compile, unittest suite, and `git diff --check` pass. Strict
`audit_lint.py --strict` currently fails on the same current-main baseline
drift in a clean `origin/main` worktree: 3 stale-dispatch warnings and 30
retained-row `note_hash` drift errors. This PR does not edit those audit rows or
apply any audit verdicts.
