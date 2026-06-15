# Handoff

This PR repairs the Planck-time minimum-step audited-conditional row after its
direct tick/edge companion moved to `retained_bounded`.

Source-side changes:

- The note now consumes the companion as `audited_clean` /
  `retained_bounded`, instead of preserving the old `audited_renaming`
  boundary.
- The runner checks the current companion status, verifies the companion cache
  is fresh, and recomputes `l_P / c = t_P`.
- The note keeps the physical-`c` statement as an explicit SI
  unit-normalization certificate and does not claim a derivation of `c`.

Verification:

- `python3 scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py`
  - `TOTAL: PASS=14 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py --allow-non-main --push-mode none`
  - `ok=1`, `timeout=0`, `nonzero_exit=0`
- `bash docs/audit/scripts/run_pipeline.sh`
  - passed with existing notices only; generated view reports
    `re-audit required: 1` and ready rows include this Planck-time packet.
- `python3 docs/audit/scripts/audit_lint.py --strict`
  - passed with existing notices only.

No audit verdicts, generated audit data, rendered ledgers, queues, or
publication effective-status files should be committed.
