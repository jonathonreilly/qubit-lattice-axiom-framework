# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Exact readout algebra `c_TE = s_TE q_T/q_E` and `rho_E = 6(q_E-1)` | Converts bridge data into `rho_E` | retained support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | Already exact support; parent runner rechecked | used |
| T-side values `q_T=5/6`, `s_TE=-2` | Gives negative numerator `s_TE q_T=-5/3` | conditional support | Route-2 stretch notes and source-domain bridge no-go | yes | yes | Direct T-side derivation remains separate campaign target | used with status caveat |
| Positivity bound `rho_E > -6` / `q_E > 0` | Forces the sign of `c_TE` under a magnitude bridge | retained support/no-go boundary | `ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md` | yes | yes, for sign reduction | Parent positivity runner; no endpoint selection claimed | partially retires sign import |
| Exact color fraction `F_adj=8/9` at `N_c=3` | Supplies the scalar magnitude candidate | exact support | `RCONN_DERIVED_NOTE.md` | yes | yes | Need typed map into Route-2 center readout | used as scalar only |
| Typed magnitude bridge `|gamma_T(center)/gamma_E(center)|=R_conn` | Would connect color scalar to Route-2 center ratio | unsupported import | Not in current support bank | yes | yes | Prove a source-domain theorem or produce no-go packet | open blocker |
| Observed quark masses / fitted endpoints | Not used | forbidden input | n/a | no | no | Keep out of proof | excluded |
| Nearest-rational endpoint matching | Comparator only, not proof | observational comparator | endpoint quotient lane | no | no | Not used by runner | excluded |
