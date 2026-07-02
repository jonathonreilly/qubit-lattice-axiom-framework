# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Route-2 endpoint triple `(-1,-2,21/4)` | Defines the active obstruction | computed lattice input / open gate | `S3_TIME_PRIMITIVE_CHAIN_NOTE.md` | yes | yes | derive missing E-side entry or demote route | open |
| Exact restricted carrier/readout reduction | Reduces problem to `beta_E/alpha_E` after T-side entries | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already available; keep boundary honest | used |
| Naturality no-go leaves `rho_E` free | Names missing primitive class | exact negative boundary | `QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md` | yes | yes | supply E-center/source/readout primitive | still binding |
| `N=15` measured q_E near `15/8` | Motivates box-path rescue | computed lattice input | measured-calibration note and runner | yes for this route only | no for retained-grade target | box-size/path stress test | stress-tested |
| June 10 q_E box-size observable | Provides metric/Ricci functional and endpoints | computed lattice input | `frontier_quark_route2_qe_box_size_scan_2026_06_10.py` | yes | no | reuse verbatim and bound scope | used |
| Radius-scaling family `r_N(p)=4.25*((N-2)/13)^p` | Candidate smooth interpolation rescue | new branch-local construction | block36 runner | yes for block36 | no for full target | finite p-grid no-go/support boundary | pruned on sampled grid |
| Comparator values `q_E=15/8`, `q_T=5/6` | Measure distance to target chain | observational comparator inside open gate | Route-2 endpoint algebra | no proof input | no | keep comparator-only | guarded |
| Source-domain or stronger readout-map primitive | Would actually derive `rho_E` | unsupported import | not supplied | yes for closure | yes | future theorem route | open blocker |
