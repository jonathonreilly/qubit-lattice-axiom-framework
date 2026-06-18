# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Gate B ordered lattice-resolution sweep | Tests first Cauchy axis | computed lattice input | `scripts/gate_b_operator_cauchy.py` | yes | yes | runner/log route | retained as tested-axis negative evidence |
| Gate B jittered ensemble-refinement sweep | Tests second Cauchy axis | computed lattice input | `scripts/gate_b_operator_cauchy.py` | yes | yes | runner/log route | retained as tested-axis negative evidence |
| Restricted strong-field finite-box closure | Method-mismatch comparison surface | cited bounded theorem surface | `docs/RESTRICTED_STRONG_FIELD_CLOSURE_NOTE.md` | yes | yes | source comparison route | kept as method mismatch only |
| N1-N8 family exhaustion | Would support family-level no-go | unsupported import if claimed | absent | no in repaired claim | no | separate theorem required | explicitly excluded |
| Audit acceptance | Authority status | independent audit judgment | audit lane, not this PR | yes | yes | reviewer/auditor process | not performed here |
