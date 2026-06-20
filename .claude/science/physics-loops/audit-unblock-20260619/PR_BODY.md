# PR Body

## Summary

This PR unblocks the ready audit row for
`one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13`.

On current `origin/main`, direct execution of
`scripts/frontier_one_parameter_reduced_shell_law.py` failed its
source-boundary firewall: the auto-generated `docs/repo/FRONT_DOOR_STATUS.md`
queue snapshot listed the ready row without the helper-wrapper qualifier, so
the runner reported `PASS=16 FAIL=1` even though the committed runner cache was
stale at `PASS=17 FAIL=0`.

The fix keeps the claim boundary narrow:

- `docs/ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md`
  now states that generated queue snapshots are not source-claim citations for
  this firewall.
- `scripts/frontier_one_parameter_reduced_shell_law.py` skips
  `docs/repo/FRONT_DOOR_STATUS.md`, matching the existing skip for generated
  audit/publication surfaces.
- The target runner cache was refreshed and now records
  `PASS=17 FAIL=0 TOTAL=17`.

## Boundary

- No audit-loop run.
- No audit verdicts applied.
- No effective-status promotion.
- This is a source-side runner/firewall repair for an already-ready unaudited
  bounded row.
- Generated audit/publication/front-door artifacts are pipeline outputs from
  current main state.

## Verification

- `python3 -m py_compile scripts/frontier_one_parameter_reduced_shell_law.py`
- Direct runner before patch: `PASS=16 FAIL=1`
- Direct runner after patch: `PASS=17 FAIL=0 TOTAL=17`
- `bash docs/audit/scripts/run_pipeline.sh`: complete; strict lint reported 139 notices, 0 errors
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_one_parameter_reduced_shell_law.py --force --push-mode none --allow-non-main`: 1 ok, 0 failures
- `python3 scripts/audit_packet_script_deps.py`: 388 / 1582 pending helper-import claims
- `python3 docs/audit/scripts/audit_lint.py --strict`: 139 notices, 0 errors
- `git diff --check`
- post-commit generated-clean check: clean
