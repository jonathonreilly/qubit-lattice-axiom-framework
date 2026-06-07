# Review History

## 2026-06-07 Local Checks

- `python3 -m py_compile scripts/interaction_asymmetry_delta_occupation_curvature_runner.py` passed.
- `PYTHONPATH=scripts python3 scripts/interaction_asymmetry_delta_occupation_curvature_runner.py` passed with `TOTAL: PASS=13 FAIL=0`.
- `python3 scripts/precompute_audit_runners.py --runners scripts/interaction_asymmetry_delta_occupation_curvature_runner.py --force --push-mode=none` passed.
- `python3 scripts/precompute_audit_runners.py --runners scripts/interaction_asymmetry_delta_occupation_curvature_runner.py --check-only --push-mode=none` passed.
- Static scan found regime-qualified `sign(K_off)` language and no remaining global `sign(|K|)=sign(U)` theorem wording in the edited note/runner.
- `git diff -- docs/audit` is empty.

Disposition: local checks pass; reviewer/auditor still owns PR extraction and
audit status.
