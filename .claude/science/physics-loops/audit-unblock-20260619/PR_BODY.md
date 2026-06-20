# PR Body

## Summary

This PR unblocks the ready audit row for
`koide_q_delta_linking_relation_theorem_note_2026-04-20`.

On current `origin/main`, direct execution of
`scripts/frontier_koide_q_delta_formal_ratio_repair.py` failed its citation
firewall because the auto-generated `docs/repo/FRONT_DOOR_STATUS.md` queue
snapshot listed the ready row without a formal/open context marker. The runner
reported `TOTAL: PASS=107 FAIL=1` even though the committed cache was stale at
`TOTAL: PASS=106 FAIL=0`.

The fix keeps the bounded claim boundary narrow:

- `docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md` now states
  that generated queue snapshots are not source-claim citations for this
  firewall.
- `scripts/frontier_koide_q_delta_formal_ratio_repair.py` skips
  `docs/repo/FRONT_DOOR_STATUS.md`, matching the existing generated-surface
  exclusions.
- The target runner cache was refreshed and now records
  `TOTAL: PASS=106 FAIL=0`.

## Boundary

- No audit-loop run.
- No audit verdicts applied.
- No effective-status promotion.
- This is a source-side runner/firewall repair for an already-ready unaudited
  bounded row.

## Verification

- `python3 -m py_compile scripts/frontier_koide_q_delta_formal_ratio_repair.py`
- Direct runner before patch: `TOTAL: PASS=107 FAIL=1`
- Direct runner after patch: `TOTAL: PASS=106 FAIL=0`
- `bash docs/audit/scripts/run_pipeline.sh`: complete; strict lint reported 139 notices, 0 errors
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_q_delta_formal_ratio_repair.py --force --push-mode none --allow-non-main`: 1 ok, 0 failures
- `python3 scripts/audit_packet_script_deps.py`: 388 / 1582 pending helper-import claims
- `python3 docs/audit/scripts/audit_lint.py --strict`: 139 notices, 0 errors
- `git diff --check`
- post-commit generated-clean check: clean
