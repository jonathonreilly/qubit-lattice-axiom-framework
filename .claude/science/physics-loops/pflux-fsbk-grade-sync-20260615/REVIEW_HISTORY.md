# Review History

## 2026-06-15 local verification

- `python3 scripts/p_flux_selection_via_fsb_k_check_2026_06_11.py`
  - `TOTAL: PASS=16 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/p_flux_selection_via_fsb_k_check_2026_06_11.py --force --push-mode none --allow-non-main`
  - `ok 1`, `nonzero_exit 0`
- `PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/p_flux_selection_via_fsb_k_check_2026_06_11.py --check-only --allow-non-main`
  - `fresh: 1`, `stale to refresh: 0`
