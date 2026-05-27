# Review History

Local checks:

- `python3 scripts/gate_b_grown_joint_package.py` passed and printed the
  replay self-check.
- `python3 scripts/precompute_audit_runners.py --runners scripts/gate_b_grown_joint_package.py --force --allow-non-main --push-mode none`
  refreshed the cache.
- `python3 scripts/vocab_lint.py --report-only docs/GATE_B_GROWN_JOINT_PACKAGE_NOTE.md`
  reported zero violations.
- `bash docs/audit/scripts/run_pipeline.sh` completed with no audit-lint
  errors.
- `git diff --check` passed.
