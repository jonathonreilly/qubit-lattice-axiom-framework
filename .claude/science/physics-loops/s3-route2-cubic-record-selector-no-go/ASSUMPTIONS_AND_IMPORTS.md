# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Lattice axiom | Supplies `Z^3` cubic adjacency only | zero-input structural | `docs/MINIMAL_AXIOMS_2026-06-05.md` | yes | yes | already framework axiom | allowed |
| Quantum axiom | Supplies one-site qubit / `Cl(3,0)` carrier only | zero-input structural | `docs/MINIMAL_AXIOMS_2026-06-05.md` | yes | yes | already framework axiom | allowed |
| Record axiom | Supplies durable finite additive scalar record only | zero-input structural | `docs/MINIMAL_AXIOMS_2026-06-05.md` | yes | yes | already framework axiom | allowed |
| Uniform three-axis law | Strongest fair model for cubic axis occupancy `1/3` | support-only | Block152 toy models | yes for positive shortcut | yes for positive shortcut | prove as typed source theorem | not supplied by minimal axioms |
| Selected axis / one-vs-two signed collapse | Converts axis occupancy into signed mean `+/-1/3` and raw moment `1` | unsupported import if asserted | Block152 toy models | yes | yes | prove Route-2 cubic-axis readout identification theorem | open |
| Physical `P_R/E-T` same-source variables `X,Y` | Makes the finite readout the actual Route-2 source/readout | unsupported import if asserted | Blocks147-150 | yes | yes | construct `Omega_R`, `P_0`, `P_h`, and typed readouts | open |
| Connected-subtraction typing | Consumes `E[XY]-E[X]E[Y]` rather than a raw or unrelated moment | unsupported import if asserted | Blocks147-148 | yes | yes | same-source typed cumulant theorem | open |
| Source/readout unit `mu=1` | Converts internal connected selector to physical center-ratio magnitude | unsupported import if asserted | Block126 / Block150 | yes downstream | yes for signed endpoint bridge | prove unit calibration theorem | open |
| Orientation sign | Supplies post-selector sign after `kappa=0` | retained support context only | Block68 / Block148 context | yes downstream | yes for signed endpoint bridge | consume only after selector fixed | separated, not used here |
| Endpoint values | Forbidden derivation inputs | unsupported import | n/a | no | no | not used | excluded |
