# Review History

- `2026-06-18`: Self-check only. Per user instruction, the Codex reviewer will
  handle the review loop and extract/clean science as needed. No audit loop was
  run and no audit verdict was applied.

Local checks:

- `python3 scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
- `python3 -m py_compile scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/audit_companion_koide_r_half_not_symmetry_protected_exact.py`
