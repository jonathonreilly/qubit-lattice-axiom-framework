# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `c_cell = 4/16 = 1/4` | Action-side primitive coefficient | computed lattice input | `PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM` | yes | yes | audit cited theorem, not rederive here | imported with conditional surface |
| Boundary-density extension | Patch additivity for action coefficient | retained support candidate / conditional | `PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM` | yes | yes | audit cited theorem | imported with conditional surface |
| Simple-fiber Widom no-go | Negative half of coefficient-gap synthesis | computed lattice input | `frontier_area_law_quarter_broader_no_go.py` | yes | yes | source-packet cache and independent audit | runner-backed |
| Primitive parity-gate carrier | Conditional positive `1/4` route | computed lattice input | `frontier_area_law_primitive_parity_gate_carrier.py` | yes | yes | source-packet cache and independent audit | runner-backed conditional |
| Primitive-CAR edge identification / CIP | Remaining physical bridge premise | unsupported import until accepted/derived | `AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM` and native-CAR tightening runner | yes | yes | derive/accept Clifford-Majorana edge semantics or keep conditional | explicit open premise |
| Audit verdict | Authority status of this row | independent audit | `docs/audit/data/audit_ledger.json` | yes | yes | reviewer/auditor only | not modified in this PR |
