# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Projector weights `w_E=1/3`, `w_T1=1/2` | Determines reciprocal-degree algebra | computed lattice input | block11 runner | yes | yes | exact runner/log route | verified |
| Endpoint algebra after T-side candidates | Converts total degree two to endpoint target | computed lattice input / granted local target premise | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | upstream theorem route | used as algebra, not as proof of `rho_E` |
| Product factorization `Q_X=S_X R_X` | Defines the source/readout split under test | zero-input structural | block11 note/runner | yes | yes | theorem route | checked |
| Channelwise factorization gauge | Shows product data cannot identify leg attribution | zero-input structural | block11 note/runner | yes | yes | theorem route | checked |
| Leg-level factorization primitive | Would fix source/readout gauges and certify independent legs | unsupported import on current surface | not present in current Route-2 notes | yes | yes | derive primitive theorem or no-go | remains open |
| Observed/live endpoint numerics | Comparator only | observational comparator / forbidden proof input | not consumed | no | no | none | excluded |

## Forbidden-Import Result

The block11 runner uses no observed masses, fitted target values, PDG values,
nearest-rational selection, or live endpoint fit.
