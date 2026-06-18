# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Spin-1/2 qubit support | Supplies comparator input | retained support | `per_site_su2_spin_half`, `AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md` | yes | yes | already retained/bounded support | consumed |
| Fermion parity grading | Supplies existing Z2 sectors | retained support | `FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md` | support only | no | already retained | context |
| Link-B realization-gate/external-spacetime identification | Identifies abstract Cl(3) with physical spatial axes | unsupported import / open gate | `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` | yes | yes | theorem or accepted-premise registration | open |
| Emergent Lorentz/positivity/microcausality | Supplies QFT spin-statistics hypotheses | support-only / conditional | `EMERGENT_LORENTZ_INVARIANCE_NOTE.md` and related surfaces | yes | yes | retained bridge theorem | open |
| Reconstruction `R` | Non-circular OS-to-Wightman route | unsupported import | `free_field_os_wightman_reconstruction` not provided in packet | yes | yes | construct/audit reconstruction without presupposing FS | open |
| Spin-statistics literature engine | Comparator for forced sign under QFT hypotheses | literature theorem / comparator | Pauli, Streater-Wightman context in note | yes under supplied hypotheses | yes for comparator only | framework-native bridge still required | comparator |
| Multi-loop graph-braid cocycle witness | Static-route pruning | computed finite witness | runner block 3 | yes for negative static opening | no for FS closure | already checked locally | retained as stress-test only |
