# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `Z^3` sites and one-qubit algebra | finite carrier and register algebra | zero-input structural | `docs/MINIMAL_AXIOMS_2026-06-29.md` | yes | yes | already registered as `minimal_axioms` | allowed premise |
| Bell bits `(z,x)=(1,1)` | explicit record payload | support-only | runner fixture | yes | yes for this finite branch | derive physical record formation in a separate row | disclosed; keeps broader closure open |
| `|Phi+>` Bell resource | ordinary teleportation resource | support-only | runner fixture | yes | yes for the teleportation identity | retained resource-preparation bridge | disclosed; not derived here |
| Ideal Bell projection and Pauli correction | branch and correction machinery | standard correction | runner matrix algebra | yes | yes | physical measurement/apparatus bridge | disclosed ideal operation |
| Shape `(8,6,5)`, endpoints, Manhattan metric, unit speed | finite test geometry | explicit normalization/boundary condition | runner fixture | yes for reported values | yes for this finite computation | parameter-family widening | scoped fixture |
| Downstream audit statuses | status telemetry only | support-only | eleven tracked ledger shards | no | no | independent downstream repairs | reported; not a premise |

No approved framework primitive beyond `minimal_axioms` is used. In
particular, the scale-reference, kinetic-isotropy, and realized-state
primitives supply no load-bearing content to this runner.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| Manhattan locality is the only useful metric | diagonal motion may be permitted | Chebyshev metric using the existing CLI | checks portability of the causal construction | live | 1 |
| Unit speed is essential | several sites may be traversed per tick | positive integer `--speed` values | checks the ceiling-distance rule | live | 1 |
| Downstream retained-grade status must gate this row | downstream rows may be scientifically independent successors | preserve their full status report but remove backward exit-code propagation | repairs dependency direction without weakening telemetry | live and selected | 3 |
| The supplied Bell resource can be silently treated as derived | the resource is not available from this row | keep it explicit and leave physical preparation open | prevents unconditional overclaim | forced | 0 |

The selected counterfactual is the only one that directly retires the named
runner artifact issue. Metric and speed widening are valid future controls but
are outside this focused repair.
