# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `w_E=1/3`, `w_T=1/2` | Channel weights for exponent-cone test | exact support | covariance Schur note / finite-star projector algebra | yes | yes | already exact support | used |
| Positive finite source/readout cone | Defined test class for block47 | branch-local definition | this packet | yes | no, only for no-go scope | broaden or replace by future nonlinear class | scoped |
| Net exponent lower bound `p >= -1` | Defines "at most one inverse-volume power" | branch-local definition | this packet | yes | no, only for no-go scope | supply p=-2 density-square primitive | scoped |
| T-side values `q_T=5/6`, shell T/E `=-2` | Converts covariance bound to endpoint bound | conditional support | exact readout-map and T-side notes | yes | yes | derive row selector | conditional only |
| Signed cancellation absence | Positivity assumption | branch-local scope | this packet | yes | no, only for no-go scope | derive signed source/readout rule | exposed escape |
