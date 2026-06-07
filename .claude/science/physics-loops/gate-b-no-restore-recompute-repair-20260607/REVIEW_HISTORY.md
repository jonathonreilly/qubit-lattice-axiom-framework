# Review History

Local pre-PR checks:

- Live recompute with certificate completed.
- Default runner: `SCORECARD PASS=8 FAIL=0`.
- Cache refresh: `precompute_audit_runners.py --runners ... --force --push-mode=none` completed OK.
- `python3 -m py_compile scripts/gate_b_no_restore_joint_package.py` passed.
- `git diff --check` pending before commit.
- `docs/audit/**` exclusion pending before commit.

Independent review-loop and audit verdict are intentionally left to the
reviewer/auditor.
