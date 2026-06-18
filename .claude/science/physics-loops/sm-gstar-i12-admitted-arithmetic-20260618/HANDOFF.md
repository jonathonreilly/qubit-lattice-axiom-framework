# Handoff

Branch: `codex/sm-gstar-i12-admitted-arithmetic-20260618`

This source-side repair follows the audit's explicit fallback path: it narrows
the row to arithmetic over admitted premises A1-A4 instead of trying to derive
neutrino masses or thermalization rates.

Verification:

- `PYTHONPATH=scripts python3 scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py`
  -> `TOTAL: PASS=41 FAIL=0`
- `python3 scripts/cached_runner_output.py --refresh scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py`

No audit outputs, ledger files, publication matrices, review queues, or status
boards were edited.
