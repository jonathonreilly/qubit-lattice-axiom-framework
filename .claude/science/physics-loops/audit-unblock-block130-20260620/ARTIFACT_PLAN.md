# Artifact Plan

## Source Change

- Add `cache_header_runner_exists(cache_path)` to
  `scripts/precompute_audit_runners.py`.
- Call it from `cleanup_orphans()` before the legacy shallow
  `scripts/<stem>.py` fallback.

## Regression Test

- Add `PrecomputeAuditRunnersTest` to
  `docs/audit/scripts/tests/test_audit_pipeline.py`.
- Fixture: a cache file named by stem whose header points at an existing
  nested runner under `scripts/corrections/`.
- Expected result: dry-run and real cleanup keep the valid nested-runner cache
  and only report/delete the synthetic missing-runner cache.

## Verification

- Focused unit test.
- Full audit pipeline unit suite.
- Cleanup dry run over the full ledger with `--check-only`.
- Strict audit lint.
- Python compile check.
- `git diff --check`.
