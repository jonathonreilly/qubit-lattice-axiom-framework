# Review History

## 2026-06-06 local pre-PR review

Disposition: `pass_pending_codex_reviewer`.

Checks run:

- `python3 -m py_compile scripts/frontier_sm_gstar_i12_nur_thermal_exclusion_2026_05_29.py`
- `PYTHONPATH=scripts python3 scripts/frontier_sm_gstar_i12_nur_thermal_exclusion_2026_05_29.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_sm_gstar_i12_nur_thermal_exclusion_2026_05_29.py --force --allow-non-main --push-mode none`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_sm_gstar_i12_nur_thermal_exclusion_2026_05_29.py --check-only --allow-non-main --push-mode none`
- `git diff --check`
- `git diff -- docs/audit --exit-code`

Result:

- Runner: `PASS=66 FAIL=0`.
- Cache fresh.
- No audit-file diff.

Remaining reviewer focus:

- Confirm the threshold route phrasing is preferred over the previous O(1)-only
  shorthand.
- Confirm the block should remain bounded-support because the small-neutrino
  mass input remains empirical.
