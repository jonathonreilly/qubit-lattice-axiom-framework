# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `delta_A1(center)-delta_A1(shell)=1/6` | Defines the E-center step | retained support | `TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md` | yes | yes | already supplied as support | allowed support |
| `K_R=(u_E,u_T,delta_A1 u_E,delta_A1 u_T)` | Restricted carrier | support-only definition | `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` | yes | yes | physical tensor-primitive bridge | support only |
| `P_R` channelwise readout form | Defines `alpha_E,beta_E` | exact support/no-go | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | derive endpoint triple | allowed support |
| T-side candidates | Conditional reduction to E row | conditional support | T-side and exact-readout notes | yes | yes | derive row selector | open import |
| E-center lift `15/8` | Missing target | unsupported import if assumed | no current non-color authority | yes | yes | derive E-center-sensitive primitive | open blocker |
| Inverse-square law `q_X proportional to w_X^-2` | Equivalent covariance route | unsupported import if assumed | no current non-color authority | yes | yes | derive nonlinear/source-weight theorem | open blocker |
| Measured calibration | Comparator only | computed lattice input | `QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md` | no | no | box/infinite-volume theorem | comparator only |
| Color/Rconn bridge | Excluded route for this block | support-only elsewhere | Rconn/source-domain notes | no | no | separate typed bridge theorem | out of scope |
