# Assumptions And Imports

## Binding Inputs

| Input | Role | Status |
|---|---|---|
| `dm_leptogenesis_exact_common.exact_package()` | Fixed source/projection/coherent-kernel constants | Existing package helper |
| `solve_normalized_transport` | Direct Boltzmann ODE solve for supplied `E_H(z)` | Existing executable transport solver |
| Equilibrium factors `S_OVER_NGAMMA_EXACT`, `C_SPH`, `D_THERMAL_EXACT` | Convert ODE yield into `eta[H]` | Existing package constants |

## Open Inputs

| Input | Why still open |
|---|---|
| Audit ratification of `DM_LEPTOGENESIS_HRAD_THEOREM_NOTE_2026-04-16.md` | This row can test a supplied `E_H`; it does not certify the radiation theorem. |
| Full DM flagship closure | Requires separate microscopic selector closure. |
| Observed `eta` match | Not claimed; radiation-branch readout is below `eta_obs`. |
