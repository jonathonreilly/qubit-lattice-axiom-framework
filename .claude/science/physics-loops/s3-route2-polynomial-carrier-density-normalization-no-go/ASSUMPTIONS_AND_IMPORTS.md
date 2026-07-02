# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `K_R=(u_E,u_T,delta u_E,delta u_T)` | tested carrier grammar | exact support / definition-only | `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` | yes | no, route pruning only | already defined | pruned as density-normalization source |
| endpoint carrier columns | finite exact test surface | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | derive map entry separately | carrier is channel-blind |
| channel weights `w_E=1/3`, `w_T=1/2` | required density primitive | exact support | `O_h`/Route-2 covariance notes | yes | yes | source/readout theorem | not in `K_R` |
| independent `P_R` coefficients | fit target if supplied | unsupported map entry | readout-map note | yes | yes | derive or no-go | remains free |

Forbidden inputs:

- observed quark masses or CKM/J targets;
- live endpoint proximity;
- fitted or nearest-rational selector;
- adopting channel-density normalization as an axiom;
- claiming a global no-go over all source/readout primitives.
