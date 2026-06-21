# Assumptions And Imports

## Minimal Allowed Premises

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Reduced readout family `P(rho_E)` | Defines rho-dependence | exact support / no-go boundary | exact readout map note | yes | yes | exact runner/log route | Used directly |
| Conditional slice family `Xi_P(t;c)` | Propagates source factor to slice | exact support | exact time-coupling note | yes | yes | exact runner/log route | Used directly |
| Parent theta-to-slice open gate | Downstream consumer surface | open gate | theta-to-slice note | yes | yes | upstream endpoint theorem | Remains open |
| Target `rho_E=21/4` | Comparison target | named target only | exact readout map note | no proof role | yes | derive upstream | Not used as proof input |

## Forbidden Inputs

- Observed quark masses, CKM/J target minimization, or PDG data.
- Nearest-rational selection from live endpoint values.
- Treating `rho_E=21/4` as adopted.
- Promoting rho-independent direct consumers to a unique theta-to-slice theorem.

## Newly Isolated Dependency

Direct consumers are independent exactly when their restricted carrier has

```text
delta_E = 0.
```

All nonzero `delta_E` consumers inherit the unresolved scalar source factor.
