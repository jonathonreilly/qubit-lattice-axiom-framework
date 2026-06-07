# Review History

Local pre-PR checks:

- Default runner: `SCORECARD PASS=11 FAIL=0`.
- Cache refresh: `precompute_audit_runners.py --runners ... --force --push-mode=none` completed OK.
- `python3 -m py_compile scripts/global_coherence_held_out2.py` passed.
- `git diff --check` pending before commit.
- `docs/audit/**` exclusion pending before commit.

Independent review-loop and audit verdict are intentionally left to the
reviewer/auditor.
