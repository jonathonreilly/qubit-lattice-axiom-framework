# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Restricted Route-2 carrier columns | Supplies E-shell, E-center, T-shell, T-center columns | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`; `frontier_quark_route2_exact_readout_map.py` | yes | yes | Already checked by parent runner | Used as source support |
| Reduced readout family `P(rho_E)` | Source-side family being varied | exact support | same readout-map note and runner | yes | yes | Derive endpoint selector upstream | Used as family, not closure |
| T-side candidates `rho_T=-1`, `mu=-2` | Collapses residual to E-side selector | conditional support | readout-map note section 4 | yes | yes | Derive T-side entries or replace with stronger theorem | Granted only for this narrowed family |
| `rho_E = 21/4` | Endpoint selector under test | unsupported import | user target and readout-map target triple | yes | yes | First-principles readout selector theorem | Not derived here |
| Exact slice backbone `Lambda_R`, `T_R`, `V_R(t)` | Shared time-coupling dynamics | exact support | `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`; `frontier_quark_route2_exact_time_coupling.py` | yes | yes | Parent exact time-coupling checks | Imported as shared backbone |
| Nonzero `V_R(t)` on checked times | Shows source ambiguity cannot cancel inside same slice law | computed lattice input | new runner plus time-coupling helper | yes | yes | Extend checked time set if needed | Verified for finite controls |

## Import Boundary

This block does not use observed quark endpoint values or fitted selectors.
It grants the same reduced exact family already used by the readout-map note
and asks where the remaining `rho_E` ambiguity lands downstream.
