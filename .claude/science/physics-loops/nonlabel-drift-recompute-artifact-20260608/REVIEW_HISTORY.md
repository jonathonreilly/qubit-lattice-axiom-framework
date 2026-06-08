# Review History

Local verification before PR:

- `python3 scripts/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py --timeout-sec 420`
- `python3 scripts/cached_runner_output.py --refresh scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py`
- `python3 scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py`
- `python3 -m py_compile scripts/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py`
- `git diff --check`
- `git diff --name-only -- docs/audit`
