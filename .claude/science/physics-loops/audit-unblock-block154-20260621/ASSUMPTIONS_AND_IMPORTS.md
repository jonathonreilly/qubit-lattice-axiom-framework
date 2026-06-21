# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Proxy budget rows | Supply one source geometry, signed scaling map, and proxy-budget estimate | bounded proxy support | `scripts/diamond_signal_budget_hardening.py` | yes | yes for bounded row | independent audit of this row | Wrapper checks geometry, null row, sign change, and transfer gap |
| Phase-ramp bridge rows | Supply normalized proxy phase-ramp card | bounded proxy support | `scripts/diamond_phase_ramp_bridge_card.py` | yes | yes for bounded row | independent audit of this row | Wrapper checks strength rows, monotone ramp slope, and R^2 floor |
| Ideal lock-in detector map | Supplies detector-map assertions | bounded support | [`DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](../../../../docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md) | yes | yes for bounded row | independent audit of detector theorem row | Delegated by wrapper |
| Source-to-NV transfer coefficient | Needed for calibrated lab signal | unsupported import / open bridge | not present | no for bounded proxy card; yes for closed signal budget | future physical coupling theorem | Remains open |
| Lab noise floor / amplitude budget | Needed for detectability | unsupported import / open bridge | not present | no for bounded proxy card; yes for closed signal budget | future calibrated signal-budget runner | Remains open |
