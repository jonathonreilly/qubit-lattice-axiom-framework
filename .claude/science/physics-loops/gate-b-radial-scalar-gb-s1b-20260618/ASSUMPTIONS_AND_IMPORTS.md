# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Finite Gate B coordinate slab | Domain for scalar check | computed lattice input | `scripts/gate_b_connectivity_tolerance.py` | yes | yes for this bounded packet | runner theorem | used narrowly |
| Formula `strength/(r+0.1)` | Scalar under test | computed lattice input | runner helper `_field_for_mass` | yes | yes for this bounded packet | exact runner/log route | verified here |
| Regulator `epsilon=0.1` | Finite-core regularizer | admitted normalization | runner-local constant | yes | no for physical closure | theorem or accepted-premise route | left open as `GB-S1b-b` |
| Source strength | Overall scalar scale | admitted normalization | runner-local constant | yes | no for physical closure | theorem or accepted-premise route | left open as `GB-S1b-b` |
| Poisson/source equation and boundary condition | Physical scalar interpretation | unsupported import for full Gate B | not supplied by this theorem | no for this bounded packet; yes for full closure | theorem route | remains open |

No observed target value, fitted selector, new axiom, or audit verdict is used.
