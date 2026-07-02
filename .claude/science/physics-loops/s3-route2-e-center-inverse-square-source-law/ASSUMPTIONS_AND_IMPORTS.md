# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Restricted Route-2 readout form | Defines `alpha_E`, `beta_E`, `q_E`, and `rho_E` | retained support / exact current-bank input | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already available as support | used |
| Center-excess denominator `6` | Converts `rho_E` to `q_E` | retained-bounded support | `TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md` | yes | yes | already available as support | used |
| T-side values | Conditional reduction to the E-center residual | conditional support | T-side endpoint attempt notes and readout algebra | yes | yes | derive in separate T-side theorem | granted only for reduction |
| `O_h` weights `w_E=1/3`, `w_T1=1/2` | Supplies `kappa=3/2` and the inverse-square target value | exact support | `OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md` | yes | yes | already exact support | used |
| Inverse-square source/readout law | Would derive `q_E=15/8` | unsupported import | no current source surface | yes | yes | theorem route or explicit convention | open blocker |
| Live measured E-center proximity | Comparator only | observational/computed comparator | measured calibration and box scan notes | no | no | not used as proof | forbidden as proof input |
| Typed color/support bridge | Alternate route to `c_TE=-8/9` | unsupported import | source-domain bridge no-go | yes if color route used | yes if color route used | typed bridge theorem | open blocker |
