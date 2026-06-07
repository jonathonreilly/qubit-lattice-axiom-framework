# Review History

Local verification:

- `python3 scripts/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.py`
  -> `PASS=33 FAIL=0`
- `python3 scripts/frontier_thooft_center_vortex_scope_repair.py`
  -> `PASS=16 FAIL=0`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.py`
  -> cache refreshed
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_thooft_center_vortex_scope_repair.py`
  -> cache refreshed
- cache check-only for both runners -> fresh
