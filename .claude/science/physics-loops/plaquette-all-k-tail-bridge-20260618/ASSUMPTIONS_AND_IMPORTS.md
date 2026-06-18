# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Finite word-count packet | Defines tensor/source boxes and eta boundary | retained support | Existing plaquette word-count packet notes/runners | yes | yes | already present on main | reused |
| `theta`, `alpha`, `sigma_slice` | Tail coordinates and scale split | computed lattice input | Existing theta and all-k runners | yes | yes | recomputed by new runner | reused |
| High-precision eigensolve | Avoids double cancellation for tail rows | computed lattice input | New rescaled tail support runner | yes | support only | runner/cache | supplied in PR |
| Analytic monotone/Neumann tail theorem | Would control every later k | unsupported import | not yet present | yes for all-k bridge completion | constructive theorem | open |

No literature value, observed comparator, fitted selector, or new axiom is used.
