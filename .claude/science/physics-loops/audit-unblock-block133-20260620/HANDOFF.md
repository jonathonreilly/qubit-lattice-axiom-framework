# Handoff

## Summary

Block133 fixes stale absolute runner-path canonicalization for nested
`scripts/...` paths.

Before this fix, all three canonicalizers returned the stale absolute path for:

```text
/tmp/old-worktree/scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py
```

After the fix, all three return:

```text
scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py
```

## Boundary

This is methodology/tooling only. It does not audit claims, apply verdicts,
edit ledger rows, or assert retained status.

## Verification

- `python3 scripts/audit_runner_path_canonicalization_guard_2026_06_17.py` -> OK.
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> OK, 3 tests.
- `python3 scripts/precompute_audit_runners.py --runners scripts/audit_runner_path_canonicalization_guard_2026_06_17.py --force --push-mode none --allow-non-main` -> OK, refreshed guard cache.
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/physics-loop/audit-unblock-block132-20260620 --check-only --allow-non-main` -> OK.
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 80 tests passed.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, notices only.
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/audit_packet_script_deps.py scripts/codex_audit_runner.py scripts/audit_runner_path_canonicalization_guard_2026_06_17.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK.
- `git diff --check` -> OK.

## Next Exact Action

Monitor PR #4503 audit-lane check, then continue to the next audit-unblock
target.

## PR

- https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4503
