## Summary

Fixes runner-path canonicalization for stale absolute paths that include a
nested `scripts/...` subpath.

Before this PR, these tools left
`/tmp/old-worktree/scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py`
as an absolute stale path:

- `scripts/codex_audit_runner.py`
- `scripts/audit_packet_script_deps.py`
- `scripts/precompute_audit_runners.py`

After this PR, all three map it to the checked-out repo path:

```text
scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py
```

## Boundary

This PR does not audit claims, apply verdicts, edit ledger rows, or assert
retained/proposed-retained status. It only repairs source-side runner path
canonicalization.

## Artifacts

- `scripts/codex_audit_runner.py`
- `scripts/audit_packet_script_deps.py`
- `scripts/precompute_audit_runners.py`
- `scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
- `logs/runner-cache/audit_runner_path_canonicalization_guard_2026_06_17.txt`
- `docs/audit/scripts/tests/test_audit_pipeline.py`
- `.claude/science/physics-loops/audit-unblock-block133-20260620/HANDOFF.md`

## Verification

- `python3 scripts/audit_runner_path_canonicalization_guard_2026_06_17.py` -> OK
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> 3 tests passed
- `python3 scripts/precompute_audit_runners.py --runners scripts/audit_runner_path_canonicalization_guard_2026_06_17.py --check-only --allow-non-main` -> `fresh: 1`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/physics-loop/audit-unblock-block132-20260620 --check-only --allow-non-main` -> `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 80 tests passed
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py scripts/audit_packet_script_deps.py scripts/codex_audit_runner.py scripts/audit_runner_path_canonicalization_guard_2026_06_17.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK
- `git diff --check` -> OK
