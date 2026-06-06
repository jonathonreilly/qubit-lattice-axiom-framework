Verification commands run:

```text
python3 -m py_compile scripts/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.py
python3 scripts/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.py
python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_chsh_tsirelson_lattice_qubits_bound_2026_05_20.py --check-only --allow-non-main --push-mode none
```

Observed result:

- companion runner: `TOTAL: PASS=24, FAIL=0`
- cache reported fresh
