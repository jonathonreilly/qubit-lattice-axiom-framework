# Review History

Local verification:

- `python3 scripts/audit_companion_two_site_qubit_tensor_carrier_bridge_2026_06_06.py`
  - `SUMMARY: TWO-SITE QUBIT TENSOR BRIDGE PASS=16 FAIL=0`
- `python3 scripts/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.py`
  - `TOTAL: PASS=24, FAIL=0`
- `python3 scripts/audit_companion_local_tomography_from_complex_structure_exact.py`
  - `9 PASS, 0 FAIL`
- `python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_two_site_qubit_tensor_carrier_bridge_2026_06_06.py,scripts/audit_companion_local_tomography_from_complex_structure_exact.py,scripts/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.py --force --push-mode none --allow-non-main`
  - all three OK
- `python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_two_site_qubit_tensor_carrier_bridge_2026_06_06.py,scripts/audit_companion_local_tomography_from_complex_structure_exact.py,scripts/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.py --check-only --allow-non-main`
  - all relevant caches fresh

Full codex-reviewer review is intentionally left to the reviewer lane.
