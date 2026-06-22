# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Six-arm Schur weights `w_E=1/3`, `w_T=1/2` | Same-domain frame data | framework-derived support | Route-2 Schur runners and conditional block | yes | yes | exact runner route | reused and rechecked |
| `q_T=5/6` | T-side normalization for endpoint controls | conditional input | exact readout map / prior Route-2 blocks | yes | yes | derive T-side endpoint independently | treated as conditional control |
| Factorized source/readout law | Minimal direct-dualization test surface | new test ansatz | Block63 runner | yes | no for route no-go | replace with stronger theorem | tested and found underdetermined |
| Source/readout exchange symmetry | Candidate selector for split charges | support-only | first-principles stretch attempt | yes | no for route no-go | prove stronger unit-dual theorem | insufficient; leaves charge free |
| Endpoint ratio `q_E/q_T=9/4` | Comparator only | target comparator | exact endpoint algebra | no | yes | derive from source/readout theorem | forbidden as proof input |
| Two unit canonical-dual charges | Positive premise that would fix `p=2` | unsupported import / new premise | Block61 conditional theorem | no for no-go | yes for closure | constructive theorem route | remains open |
