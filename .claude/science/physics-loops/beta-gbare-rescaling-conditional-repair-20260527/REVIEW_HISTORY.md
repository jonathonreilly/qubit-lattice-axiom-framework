# Review History

Local checks:

- `python3 scripts/frontier_beta_gbare_squared_rescaling_invariance.py`
  passed with `TOTAL: PASS=151 FAIL=0`.
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_beta_gbare_squared_rescaling_invariance.py --force --allow-non-main --push-mode none`
  refreshed the cache.
- `python3 scripts/vocab_lint.py --report-only docs/BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md`
  reported zero violations.
- `bash docs/audit/scripts/run_pipeline.sh` completed with no audit-lint
  errors.
