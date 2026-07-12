# Assumptions and Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| finite Harper matrix and PT trace formula | defines the computed response | retained_bounded | `LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md` | yes | yes | direct dependency plus local reconstruction | linked and recomputed |
| `Q=24`, `Ly=2`, `GL=20`, `m=0`, `t=1` | finite protocol coordinates | explicit boundary conditions | source note and runner | yes | yes | scope to exactly this finite protocol | disclosed |
| bracket `[1.2,2.4]`, 60 bisections | root-reading protocol | explicit boundary condition | source note and runner | yes | yes | no physical-selector claim | disclosed |
| `eta=T_q=0.05`, `h=0.02` | regularized proxy and finite quotient coordinates | explicit boundary conditions | source note and runner | yes | yes | no regulator/derivative limit claim | disclosed |
| `T={0.10,0.15,0.20,0.25}` | regression grid | explicit boundary condition | source note and runner | yes | yes | characterize only this grid | disclosed |
| comparison band `0.15` | internal comparison threshold | explicit normalization/boundary condition | source note and runner | no; reported arithmetic survives without it | no | label as non-error band | disclosed |
| Richardson fixed sequence | shows the packet does not supply an asymptotic reading of the quotient | retained_bounded | `EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md` | yes, for claim boundary | yes | direct dependency | linked |
| observed or fitted physical target | none | not imported | none | no | no | not applicable | excluded |

The minimal axioms do not select this Hamiltonian, response, branch, or
regulator.  They are therefore not cited as a load-bearing dependency.
