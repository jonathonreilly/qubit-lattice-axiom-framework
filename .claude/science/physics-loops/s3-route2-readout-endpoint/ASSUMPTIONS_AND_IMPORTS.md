# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Exact restricted carrier columns `(u_E,u_T,delta_E,delta_T)` | Domain for the local split | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already exact on the source surface | imported as exact carrier/readout reduction |
| Reduced family `P(rho_E)` after T-side normalization | Object being split | exact support/open boundary | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | derive a readout/source primitive selecting one `rho_E` | open; block20 does not select it |
| Route-2 slice backbone `Lambda_R`, `T_R`, `V_R(t)` | Time-channel support | exact support | `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md` | yes for time statements | no for primitive selection | none needed for block20; already supplied | imported as slice authority |
| Factor-rigidity theorem F1-F5 | Safe consumer side | exact support | `S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md` | yes | no for endpoint selection | keep scoped to time-channel statements | reused only inside its scope |
| Eta-floor affine readout | Comparator for bridge assessment | support-only / endpoint-fitted | `S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md` | no for block20 proof | no | separate theorem or convention could select it | explicitly not a primitive-selection input |
| Endpoint triple `(-1,-2,21/4)` | Target value being protected from overclaim | open target | exact readout/time notes | no as proof input | yes for final endpoint target | derive readout primitive or E-center source rule | not used as proof input except as contrast in exact-family checks |
