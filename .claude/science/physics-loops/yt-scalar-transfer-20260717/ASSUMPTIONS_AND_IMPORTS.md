# Assumptions And Imports

## Target theorem

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---:|---:|---|---|
| `a in C([t0,T], R)` | universally quantified coefficient history | zero-input structural | theorem definition | yes | yes | none needed | keep universal |
| `b > 0` | universally quantified cubic coefficient | zero-input structural | theorem definition | yes | yes | none needed | keep universal |
| `t0 < T`, `X > 0`, `Y > 0` | theorem domain | zero-input structural | theorem definition | yes | yes | none needed | keep universal |
| elementary differentiation, integration factor, limits | proof rules | zero-input structural | self-contained proof | yes | yes | self-contained | proved in note and runner |

## Former implementation inputs

| Item | Former role | Current class | Load-bearing after pivot? | Disposition |
|---|---|---|---:|---|
| I1 canonical lattice constants | fixed numerical surface | unsupported import for a clean theorem | no | removed |
| I2 fixed boundary target | selected endpoint value | unsupported import for a clean theorem | no | replaced by universal `Y > 0` |
| I3 coupled multi-loop coefficients/procedure | fixed physical transport model | unsupported import for a clean theorem | no | removed from claim |
| I4 threshold scales | numerical seeds | observational/standard inputs | no | removed |
| I5 electroweak initial surface | numerical seeds | observational/standard inputs | no | removed |

The symbolic Yukawa corollary quantifies over every continuous gauge-history
triple. It fixes no history, scale, target, or physical interpretation and is
outside the load-bearing theorem scope.
