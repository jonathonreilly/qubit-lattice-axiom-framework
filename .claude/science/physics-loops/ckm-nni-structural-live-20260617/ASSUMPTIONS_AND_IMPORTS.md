# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Positive ordered masses `0 < m_1 < m_2 < m_3` | Domain for T1-T4 | zero-input structural | New structural note | yes | yes | Already explicit domain | Kept |
| Positive NNI coefficients `c_12, c_23` | Domain for T2-T4 | zero-input structural | New structural note | yes | yes | Already explicit domain | Kept |
| `c_13^geom = c_12 c_23` | Structural NNI closure being checked | framework-local definition | New structural note and runner | yes | yes | Symbolic proof and exact controls | Proved in scope |
| `Phi_ij(c) = c sqrt(m_i/m_j)` | Normalization map used by older route | admitted local map | New structural note | yes | yes | Algebraic closure under T1 | Proved as map identity, not physical CKM closure |
| Quark masses | Calibrated Cabibbo illustration | observational/imported comparator | Legacy runner only | no for T1-T4; yes for `|V_us|` number | no for exact-support target | Separate mass derivation needed | Left bounded |
| Fitted NNI coefficients | Calibrated Cabibbo illustration | fitted input | Legacy runner only | no for T1-T4; yes for `|V_us|` number | no for exact-support target | Separate coefficient derivation needed | Left bounded |
| PDG CKM comparators | Numerical comparison | observational comparator | Legacy runner only | no for T1-T4 | no | Not a proof input | Left comparator-only |
