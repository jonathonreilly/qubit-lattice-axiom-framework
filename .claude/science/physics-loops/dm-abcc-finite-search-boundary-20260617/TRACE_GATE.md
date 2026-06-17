# Trace Gate

## Required Checks

- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/frontier_dm_abcc_basin_enumeration_completeness.py --refresh --timeout-sec 600`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/frontier_dm_abcc_basin_enumeration_completeness.py --check-only`
- `python3 -m py_compile scripts/frontier_dm_abcc_basin_enumeration_completeness.py`
- `git diff --check`
- Confirm no changes under `docs/audit`, `docs/publication`, or
  `docs/repo/FRONT_DOOR_STATUS.md`.

## Expected Terminal Boundary

```text
VERDICT: FINITE MULTISTART BASIN SCAN BOUNDARY VERIFIED
THEOREM-GRADE EXHAUSTIVENESS: NOT CLAIMED
```
