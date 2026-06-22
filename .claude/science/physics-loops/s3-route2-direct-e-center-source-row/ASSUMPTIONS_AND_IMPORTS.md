# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Restricted Route-2 endpoint carrier and readout row algebra | Defines `q_E`, `rho_E`, `c_TE`, and the missing map entry | current support / exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already used as authority; do not recertify here | used as one-hop authority |
| Parent S3 theta-to-slice blocker | Downstream consumer and open endpoint triple | open gate | `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md` | yes | yes | derive endpoint triple upstream | target consumer |
| T-side values `rho_T=-1`, `s_TE=-2` | Converts row-degree ratio into `q_E`, `rho_E`, `c_TE` | conditional support / bounded attempt | `QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md` | yes | yes | derive T-row selector or keep conditional | supplied premise in this block |
| O_h weights `w_E=1/3`, `w_T=1/2` | Input weights for homogeneous source-row degree test | exact support | Block99-104 support chain | yes | yes | already exact for the row test; physical row degree still open | used |
| Homogeneous source-row degree `d=-2` | Decisive direct-row selector for `q_E=15/8` | unsupported import on current surface | this block isolates, but does not derive, the degree | yes | yes | derive from source/readout theorem, no-scale Hessian bridge, or new exact primitive | open blocker |
| Observed masses, fitted endpoint values, nearest-rational scans | Forbidden as proof inputs | forbidden import | prior no-go/candidate notes | no | no | keep as comparator only | excluded |
