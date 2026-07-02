# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Exact slice backbone `Lambda_R` | common time/slice transport | retained support | `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md` | yes | no, only for route pruning | already supplied | ratio-preserving input |
| Exact conditional family `Xi_P(t;c)` | tested theta-to-slice route | exact support | `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md` | yes | no, only for route pruning | already supplied | pruned as source of normalization |
| Restricted readout family `P_R` | source-side ambiguity | exact support / open map entry | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | derive missing readout map entry | remains open |
| Channel-density normalization `D_X=A_X/w_X` | missing primitive | unsupported import | none on current surface | yes | yes | source/readout theorem or no-go | not supplied by theta-slice route |
| Endpoint values `(-1,-2,21/4)` | comparison target | target statement | Route-2 endpoint notes | yes | yes | derive from source/readout primitive | not used as fitted input |

Forbidden inputs:

- observed quark masses or CKM/J targets;
- live endpoint proximity;
- fitted or nearest-rational selector;
- adopting channel-density normalization as an axiom;
- claiming a global no-go over source/readout primitives.
