# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `t(6)=1` | HK Brownian time normalization | computed lattice input | `probe_hk_time_derivation.py` | yes | yes | independent audit of Block 01 | runner-backed |
| `exp(-2/3)` single plaquette | Block 02 closed-form input | computed lattice input | `probe_hk_plaquette_closed_form.py` | yes | yes | independent audit of Block 02 | runner-backed |
| Multi-plaquette HK factorization | Block 03 structural content | literature/theorem bridge plus source derivation | Block 03 note | yes | yes | audit source packet | explicit |
| L_s=2 HK cube value | Completed finite-volume Path A comparator | computed lattice input | `probe_hk_cube_perron_l2_2026_05_06.py` | no for thermodynamic closure | yes for this packet's currency | audit Block 06 | runner-backed comparator |
| Cluster-decomposition / exponential-clustering estimate | Thermodynamic-limit closure premise | unsupported import | not present in retained primitives | yes | yes | derive theorem or keep row open | explicit blocker |
| Audit verdict | Authority status of this row | independent audit | audit ledger | yes | yes | reviewer/auditor only | not modified |
