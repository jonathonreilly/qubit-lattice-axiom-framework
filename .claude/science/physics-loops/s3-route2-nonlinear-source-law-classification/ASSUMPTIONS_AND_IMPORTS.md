# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Six-arm Schur weights `w_E=1/3`, `w_T=1/2` | Same-domain frame data | framework-derived support | Route-2 Schur runners | yes | yes | exact runner route | reused and rechecked |
| Endpoint ratio `q_E/q_T=9/4` | Comparator for classification | target comparator | exact endpoint algebra | no | yes | derive from source/readout theorem | forbidden as proof selector |
| Power-law covariance | Nonlinear family constraint | support-only | Block64 runner | yes | no for route no-go | add exponent selector | leaves exponent free |
| Two-bin monomial grammar | Complement-factor escape test | support-only | Block64 runner | yes | no for route no-go | derive physical grammar and selector | collapses to inverse-square when target imposed |
| Free coefficients | Interpolation control | unsupported import | Block62 / Block64 runners | yes | no for route no-go | coefficient theorem route | underdetermined |
