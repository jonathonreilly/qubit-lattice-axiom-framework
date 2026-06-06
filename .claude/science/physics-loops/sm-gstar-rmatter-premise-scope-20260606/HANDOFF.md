# Handoff

Branch:
`physics-loop/sm-gstar-rmatter-premise-scope-20260606`

Repair:
The `R-MATTER` packet still checks the exact arithmetic
`15 * 2 * 3 = 90` and `g_* = 427/4`, but no longer says every count input is
retained-sourced. It explicitly names:

- `P_RH_inventory`
- `P_Weyl_thermal_dof`
- I12
- R-SPIN
- neutral-singlet branch convention

Verification:

- `python3 -m py_compile scripts/frontier_sm_gstar_r_matter_reduction_2026_05_29.py`
- `PYTHONPATH=scripts python3 scripts/frontier_sm_gstar_r_matter_reduction_2026_05_29.py`
  returned `PASS=98 FAIL=0`.

Audit discipline:
No files under `docs/audit/` were edited.
