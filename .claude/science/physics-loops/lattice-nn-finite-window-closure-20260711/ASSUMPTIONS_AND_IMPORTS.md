# Assumptions and Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Raw three-forward-edge lattice and fixed constants | Defines the tested family | computed lattice input | `scripts/lattice_nn_continuum.py` | yes | yes | exact runner/log | frozen in the claim scope |
| Four spacings in `H_finite` | Finite domain of the proposition | computed lattice input | runner constant | yes | yes | exhaustive runner certificate | closed |
| Born tolerance `1e-10` | Numerical acceptance predicate | admitted normalization | existing note, runner, and audit scope | yes | yes | state explicitly and test | closed as the inherited audit predicate, not a derived residual |
| Exact `k=0` equality | Structural control predicate | computed lattice input | runner certificate | yes | yes | check equality directly | closed without a tolerance |
| Observed or fitted target values | None | fitted input | none | no | no | not applicable | forbidden |
| `h = 0.125` or continuum convergence | Outside the theorem | unsupported import if used | none | no | no | separate future route | excluded |

No literature theorem, observational comparator, fitted selector, or external
physical target is load-bearing for the bounded proposition.
