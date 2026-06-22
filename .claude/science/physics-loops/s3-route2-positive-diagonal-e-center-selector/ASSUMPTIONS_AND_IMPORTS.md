# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Route-2 E-row endpoint algebra | Defines `q_E=1+rho_E/6` | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already gives target coordinate | accepted input |
| Positivity domain | Gives `rho_E>-6` but not a value | no-go / boundary | `ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md` | yes | yes | add distinguishing selector | unchanged |
| Positive-diagonal classifier | Route tested for E-center-sensitive selection | bounded support | `OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md` | yes | no | show classifier shape is value-blind | pruned as selector |
| Record finite additivity | Context for why additivity alone is insufficient | framework axiom boundary | `MINIMAL_AXIOMS_2026-06-05.md` | yes | yes | supply readout context/selector separately | unchanged |
| `rho_E=21/4` target | Value to be derived | unsupported import if used as proof input | target algebra only | no as proof input | yes as theorem target | still open |
