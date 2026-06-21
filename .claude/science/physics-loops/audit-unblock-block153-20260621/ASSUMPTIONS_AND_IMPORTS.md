# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Ideal lock-in detector map | Supplies `X`, `Y`, `phi`, controls, and widefield phase-slope map | bounded support | [`DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](../../../../docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md) plus `scripts/diamond_ideal_lockin_detector_theorem.py` | yes | yes for bounded protocol row | independent audit of ideal detector theorem row | Delegated by wrapper and passes |
| Protocol qualitative ordering | Defines low/mid/high drive and near/far scan expectations | bounded protocol card | `scripts/diamond_sensor_protocol_probe.py` | yes | yes for this row | wrapper assertions over `SCAN_CLASSES` and card text | Passes |
| Source-to-NV coupling map | Needed for real NV signal strength | unsupported import / open bridge | not present | no for bounded protocol registration; yes for closed prediction | future physical coupling theorem | Remains open |
| Absolute amplitude/noise budget | Needed for lab detectability | unsupported import / open bridge | not present | no for bounded protocol registration; yes for closed prediction | future calibrated signal-budget runner | Remains open |
