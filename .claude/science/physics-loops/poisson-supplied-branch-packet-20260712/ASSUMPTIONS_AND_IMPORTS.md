# Assumptions and Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Per-layer 2D Poisson equation, source, zero boundary, normalization, longitudinal factor, and centroid readout | Defines the narrow branch | explicit normalization/boundary condition | target note | yes | yes | excluded from framework-native claim | supplied explicitly |
| `scripts/poisson_self_field.py` | Implements constants, lattice growth, field solve, propagation, and readouts | computed lattice input | complete helper source plus SHA-pinned cache | yes | yes | restricted-packet inclusion | retired as hidden import |
| Primary certificate runner | Independently checks finite residual, sign, scaling, Born cancellation, and null branch | computed lattice input | primary source plus fresh cache | yes | yes | exact runner/log route | closed |
| Physical interpretation as gravity | Outside the theorem | unsupported import | none | no | no | separate future derivation | excluded |

No observed target value, fitted selector, literature constant, or admitted
physical unit convention is used to prove the finite branch consequences.
