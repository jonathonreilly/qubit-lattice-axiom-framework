# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Six-arm `O_h` star projector split | Supplies `A1/E/T1` projectors and ranks | computed lattice input | runner recomputation | yes | yes | exact runner/log route | verified in block10 runner |
| Per-arm weights `w_A1=1/6`, `w_E=1/3`, `w_T1=1/2` | Determines reciprocal-degree ratios | computed lattice input | runner recomputation; prior Route-2 support notes | yes | yes | exact runner/log route | verified in block10 runner |
| Finite-frame Riesz dual lemma | Shows one local dual-normalized leg gives one reciprocal factor | zero-input structural | finite-dimensional Hilbert algebra in block10 note/runner | yes | yes | theorem route | proved in block10 note and checked numerically/exactly |
| Route-2 endpoint algebra with `q_T=5/6` and shell ratio `-2` | Converts `lambda=9/4` to `rho_E=21/4` and center ratio `-8/9` | computed lattice input / granted local target premise | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | upstream theorem route for the T-side entries and E-side entry | used as endpoint algebra, not as proof of `rho_E` |
| Independent source and readout dual-normalized legs | Would supply total reciprocal degree 2 | unsupported import on current surface | not derived in current Route-2 tensor/readout notes | yes | yes | derive a source/readout primitive theorem or equivalent degree-2 primitive | named as remaining license gap |
| Physical tensor primitive bridge | Needed to treat the dual legs as physical Route-2 readout structure | unsupported import on current surface | `S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md`, `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` | yes | yes | exact tensor primitive theorem | remains open |
| Observed/live endpoint numerics | Comparator only | observational comparator / forbidden proof input | not consumed | no | no | none | excluded |

## Forbidden-Import Result

The block10 runner uses no observed masses, fitted target values, PDG values,
nearest-rational selection, or live endpoint fit. The rational endpoint values
appear only as the exact algebraic target already named by the current Route-2
readout-map obstruction.
