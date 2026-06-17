# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Delayed sinusoidal source history `A_z cos(omega(t - tau_z))` | Input to ideal detector map | admitted detector-test input | `DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md` | yes | yes, for bounded support | not retired; explicitly scoped | admitted only for detector-map theorem |
| Integer-cycle lock-in definitions | Defines `X`, `Y`, `phi` | detector idealization | new theorem note and runner | yes | yes | explicit theorem and runner | retained as bounded lab idealization |
| Trigonometric cycle averages | Evaluates lock-in channels | framework-applied math | `scripts/diamond_ideal_lockin_detector_theorem.py` | yes | yes | direct numerical cycle-average checks plus closed formulas | hidden textbook import retired |
| Retarded/wavefield source candidates | Motivate delayed source histories | source-candidate context | Diamond notes cite existing repo notes | no for detector theorem; yes for later physical prediction | no for this bounded support block | future source-to-field bridge | kept contextual, ledger-owned status not reprinted |
| NV transfer coefficient / Hamiltonian coupling | Maps proxy field to lab readout | open physical bridge | none closed in this branch | no | no | new source-to-NV theorem or lab calibration | remains open |
| Absolute amplitude/noise budget | Detectability | open calibration | none closed in this branch | no | no | lab geometry plus transfer coefficient | remains open |
