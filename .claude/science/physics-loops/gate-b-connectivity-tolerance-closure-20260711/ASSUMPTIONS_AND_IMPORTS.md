# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Fixed forward stencil | Defines the fixed-adjacency rows | retained support | `GATE_B_LOCAL_STENCIL_CONNECTIVITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md` | yes | yes | already retained-bounded | linked dependency |
| Scalar `strength/(r+0.1)` | Declared finite algorithm input | explicit normalization/boundary condition | registered runner | yes, algorithmically | yes, only as an explicit definition | physical derivation excluded from claim | disclosed condition |
| Edge kernel and constants | Declared finite algorithm input | computed lattice input | registered runner | yes | yes, only as an explicit definition | physical selection excluded from claim | disclosed condition |
| Detector window and summaries | Defines the reported finite functionals | computed lattice input | note plus runner | yes | yes | definitions made exact and checked | internal definition |
| Physical source/readout/growth semantics | Would be required only for Gate B dynamics | unsupported import | none | no | no | separate future theorem | excluded from claim |

No measured values, fitted targets, literature values, or observational
comparators enter the bounded theorem.
