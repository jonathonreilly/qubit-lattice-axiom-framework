# Assumptions And Imports

| Item | Role | Status |
| --- | --- | --- |
| Per-layer 2D Poisson equation | Supplies the transverse equation solved by the runner | supplied, not derived |
| Point source and source strength | Defines the right-hand side | supplied |
| Zero transverse boundary | Defines the finite-grid problem | supplied |
| Gauss-Seidel iteration count | Defines the finite numerical branch | bounded numerical choice |
| Longitudinal `1/(dx+0.1)` factor | Gives the layer falloff | imposed |
| Centroid readout as gravity proxy | Interprets TOWARD/AWAY in the runner | supplied diagnostic |
| Physical gravity interpretation | Would connect the branch to a gravity law | not claimed |

No new axiom is introduced. The repair is a source-boundary split around an
existing supplied branch.
