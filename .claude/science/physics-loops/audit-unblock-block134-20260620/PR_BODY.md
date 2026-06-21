## Summary

Refreshes `docs/audit/data/audit_packet_script_deps.json` and the paired
runner cache after the latest ledger/main updates and the runner-path
canonicalization fixes.

Also fixes null runner-path canonicalization: `runner_path: null` now stays an
empty/no-runner path instead of becoming the literal string `"None"`.

Refreshed packet-deps summary:

- total claims in ledger: 3445
- pending audits in queue: 1535
- claims with runner path: 3168
- claims with no runner declared: 277
- claims whose runner file is missing: 0
- pending claims with helper imports: 355 / 1421

## Boundary

This PR does not audit claims, apply verdicts, hand-edit ledger rows, or assert
retained/proposed-retained status. It only repairs and refreshes audit packet
assembly support data.

## Artifacts

- `scripts/codex_audit_runner.py`
- `scripts/audit_packet_script_deps.py`
- `scripts/precompute_audit_runners.py`
- `scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
- `docs/audit/data/audit_packet_script_deps.json`
- `docs/audit/scripts/tests/test_audit_pipeline.py`
- `logs/runner-cache/audit_packet_script_deps.txt`
- `logs/runner-cache/audit_runner_path_canonicalization_guard_2026_06_17.txt`

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/audit_runner_path_canonicalization_guard_2026_06_17.py,scripts/audit_packet_script_deps.py --force --push-mode none --allow-non-main` -> 2 OK
- `python3 scripts/audit_runner_path_canonicalization_guard_2026_06_17.py` -> OK
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> 4 tests passed
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/physics-loop/audit-unblock-block133-20260620 --check-only --allow-non-main` -> `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 81 tests passed
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py scripts/audit_packet_script_deps.py scripts/codex_audit_runner.py scripts/audit_runner_path_canonicalization_guard_2026_06_17.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK
- `git diff --check` -> OK
