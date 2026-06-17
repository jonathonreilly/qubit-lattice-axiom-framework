# Artifact Plan

Artifacts:

- Update the Koide toy note to split A5 into `A5-num` and `A5-transfer`.
- Update the companion runner and closeout labels.
- Refresh the runner cache.
- Add this loop pack.

Verification:

- `python3 scripts/audit_companion_koide_dimensionless_objection_toy_conditional_algebraic_checks.py`
- `python3 -m py_compile scripts/audit_companion_koide_dimensionless_objection_toy_conditional_algebraic_checks.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/audit_companion_koide_dimensionless_objection_toy_conditional_algebraic_checks.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_koide_dimensionless_objection_toy_conditional_algebraic_checks.py`
- `git diff --check`
