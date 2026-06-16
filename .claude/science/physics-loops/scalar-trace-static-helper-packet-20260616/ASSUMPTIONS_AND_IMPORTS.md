# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Scalar boundary functional | Defines the scalar-only data being factored through | imported helper authority | `frontier_tensorial_einstein_regge_completion.py` via static import | yes | yes | static helper packet plus cache; stronger status requires independent audit | exposed |
| O_h probe family | Exact local witness family | imported helper authority | `frontier_same_source_metric_ansatz_scan.py` via static import | yes | yes | helper cache added in this PR | exposed |
| Finite-rank probe family | Robustness witness family | imported helper authority | `frontier_coarse_grained_exterior_law.py` via static import | yes | yes | helper cache already present, rechecked | exposed |
| Einstein residual evaluator | Shows tensor channels differ while scalar data are fixed | imported helper authority | `frontier_tensorial_einstein_regge_completion.py` via static import | yes | yes | helper cache already present, rechecked | exposed |

No new axiom is introduced. This branch does not claim the helper authorities
are retained; it only removes the restricted-packet opacity.
