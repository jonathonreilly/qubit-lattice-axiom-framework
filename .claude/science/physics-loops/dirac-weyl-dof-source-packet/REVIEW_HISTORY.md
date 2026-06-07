# Review History

Local checks before PR:

- `PYTHONPATH=scripts python3 scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py` -> `TOTAL: PASS=107 FAIL=0`
- runner cache refreshed with `scripts/precompute_audit_runners.py`
- `python3 -m py_compile scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py` -> pass
- `git diff --check` -> pass
- no `docs/audit/**` changes in the worktree

External review remains pending.
