# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Exact Route-2 readout reduction | Defines the missing map entry `beta_E/alpha_E` | retained support / exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already supplies the reduced target, not the value | accepted input |
| S3 primitive-chain owner row | Names the consumer gate and forbidden downstream overuse | open gate | `S3_TIME_PRIMITIVE_CHAIN_NOTE.md` | yes | yes | derive fixed-carrier E-center primitive | accepted input |
| Measured `N=15` calibration | Supplies finite-box comparator that motivated bulk-limit route | bounded support | `QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md` | yes for this pruning route | no for endpoint closure | box-size scan | pruned as closure route |
| Box-size scan cache | Evidence that the tested stack functional does not approach `15/8` in the tested limits | computed lattice input | `logs/runner-cache/frontier_quark_route2_qe_box_size_scan_2026_06_10.txt` | yes | no for endpoint closure | fresh cache and note verification | accepted for route pruning |
| Naturality no-go | Standing fixed-carrier non-selection boundary | exact negative boundary | `QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md` | yes | yes | add independent E-center/source/readout primitive | unchanged |
| `rho_E=21/4` target | Endpoint value to be derived | unsupported import if used as proof input | target algebra only | no as proof input | yes as theorem target | derive from independent primitive | still open |
| Observed quark masses / fitted endpoint selection | Forbidden hidden selector | forbidden | none | no | no | exclude from route | not used |
