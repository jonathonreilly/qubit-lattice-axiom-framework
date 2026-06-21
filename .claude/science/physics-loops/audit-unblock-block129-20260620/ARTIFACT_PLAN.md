# Artifact Plan

- Update `scripts/audit_runner_runtime_breakage_staleness_guard_2026_06_17.py`
  so it covers `missing_runner_file`, `nonzero_exit`, and `timeout` inventory
  rows.
- Canonicalize legacy runner references before checking repo-local script paths.
- Require every covered row to have a fresh SHA-pinned cache with `status=ok`
  and `exit_code=0`.
- Refresh the guard's runner-cache transcript.
- Run targeted source checks and open a PR.
