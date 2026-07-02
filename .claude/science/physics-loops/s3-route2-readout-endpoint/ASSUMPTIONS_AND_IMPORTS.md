# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Route-2 center-excess denominator `6` | Converts `rho_E` to `e_E=rho_E/6` | exact support | `TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`, exact readout-map notes | yes | yes | already present as support-side endpoint step | used |
| T-side granted entries `rho_T=-1`, `alpha_T/alpha_E=-2` | Equivalence from `q_E=15/8` to `c_TE=-8/9` | granted route condition | S3/Route-2 gate notes | yes for center-ratio equivalence | yes if using `c_TE` route | derive or separately certify T-side entries | carried as granted route condition |
| Existing hierarchy `7/8` anchor | Candidate same-rational source | exact support, untyped for Route-2 | hierarchy seven-eighths note/runner | no | only if bridged | prove typed edge to `route2_e_E_7_8` | untyped candidate |
| Existing thermal `7/8` anchor | Candidate same-rational source | bounded/exact thermal support, untyped for Route-2 | gstar thermal bridge note/runner | no | only if bridged | prove thermal-to-Route-2 readout role bridge | untyped candidate |
| APBC/radian `7/8` inventory | Candidate same-rational source | contextual support, untyped for Route-2 | radian bridge inventory | no | only if bridged | prove APBC-to-E-center source bridge | untyped candidate |
| Color complement `(N_c^2-2)/(N_c^2-1)=7/8` | New candidate arithmetic | exact arithmetic only | block34 runner/note | no | only if bridged | prove why connected-adjoint denominator supplies E-center excess | candidate only |
| Typed bridge `existing_7_8_anchor -> route2_e_E_7_8` | Would compute the missing E-side datum | missing theorem | none found | yes for positive closure | yes | new source/readout theorem | open blocker |
