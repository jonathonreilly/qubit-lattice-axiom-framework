# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Class-A `K_R` carrier formula | Object under test | computed lattice input / definition-only | `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` | yes | yes | exact runner/log route | factored exactly in block12 |
| Endpoint `delta_A1` values | Checks live endpoint columns | computed lattice input | current support helpers | yes | yes | exact runner/log route | verified |
| Projector weights `w_E=1/3`, `w_T1=1/2` | Determines degree comparison | computed lattice input | block12 runner | yes | yes | exact runner/log route | verified |
| Endpoint algebra after T-side candidates | Converts degree-zero and degree-two consequences | computed lattice input / granted local target premise | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | upstream theorem route | used as algebra, not endpoint proof |
| Additional leg-level normalization primitive | Would supply nonzero reciprocal degree | unsupported import on current surface | not present in current `K_R` carrier | yes | yes | derive primitive theorem or no-go | remains open |
| Physical tensor primitive bridge | Needed to make any carrier primitive physical | unsupported import on current surface | current bilinear note says open | yes | yes | theorem route | remains open |
| Observed/live endpoint numerics | Comparator only | observational comparator / forbidden proof input | not consumed | no | no | none | excluded |

## Forbidden-Import Result

The block12 runner uses no observed masses, fitted target values, PDG values,
nearest-rational selection, live endpoint fit, or physical-primitive bridge as
proof input.
