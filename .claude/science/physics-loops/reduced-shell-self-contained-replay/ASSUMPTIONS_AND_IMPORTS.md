# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Finite Dirichlet negative Laplacian on the 15^3 box | Builds point-Green columns and source-family fields | framework-local finite operator | Self-contained runner | yes | yes | Inlined exact sparse construction | retired for this artifact |
| Star-support source class | Seven unit point-Green columns | framework-local finite source class | Self-contained runner | yes | yes | Inlined coordinates and solves | retired for this artifact |
| Exact local O_h source-family constructor | Source-family replay | computed lattice input | Self-contained runner | yes | yes | Inlined commutant/source law | retired for this artifact |
| Finite-rank source-family constructor | Source-family replay | computed lattice input | Self-contained runner | yes | yes | Inlined Woodbury finite-rank setup | retired for this artifact |
| Reduced R=4 shell surface | Boundary of the current theorem | bounded support | Existing source note | yes | yes | Requires later retained shell-stress/junction theorem for full gravity closure | still bounded |
| Nonlinear shell-stress / junction lift | Full gravity interpretation | unsupported import for closure | Out of scope | no for this repair | yes for full gravity | New theorem route | open |
