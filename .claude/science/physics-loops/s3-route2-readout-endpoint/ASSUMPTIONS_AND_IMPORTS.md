# Assumptions And Imports

## Minimal Allowed Premises

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Reduced Route-2 readout family | Supplies `rho_E` residual | retained support / exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | exact runner/log route | Used directly |
| Positive projective E-row family | Selection surface `rho_E>-6` | bounded support | `QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md` | yes | yes | exact support/no-go route | Used as reduced surface |
| Same-domain `kappa=3/2` | Candidate leverage value | computed lattice input | kappa covariance note | yes | yes | theorem route for bridge | Used as candidate selector input |
| Target rationals | Comparison target | named target only | exact readout map note | yes as target, not proof | yes | derive from selector theorem | Not used as proof input |
| Inverse-square rule | Lands target if selected | unsupported import on current surface | coefficient boundary | yes | yes | derive coefficient-selection theorem | Remains open |

## Forbidden Inputs

- Observed quark masses, CKM/J target minimization, or PDG data.
- Nearest-rational selection from live endpoint values.
- Treating `rho_E=21/4`, `q_E=15/8`, or `lambda=9/4` as adopted.
- Hiding the target inside a variational coefficient ratio.
- Promoting inverse-square weighting to an adopted primitive.

## Newly Exposed Dependency

The coefficient-selection route lands only if it derives one of:

```text
lambda = kappa^2,
q_E = 15/8,
B/A = -15/4,
n = 2 in lambda = kappa^n.
```

The current surface does not derive any of these as a selector.
