# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Fixed Schur-NNI tree edges `1-2`, `2-3` | Defines the boundary of the slot theorem | bounded support / parent-surface context | `QUARK_MASS_RATIO_FULL_SOLVE_NOTE_2026-04-18.md`, `QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md` | yes | yes, for this exact support statement | Keep theorem scoped to fixed tree | Used as explicit boundary, not derived here |
| Hermitian mass matrix completion | Makes determinant phase real and defines diagonal rephasing action | standard finite linear algebra | runner + note | yes | yes | Direct finite algebra | Proved/checkable in runner |
| Diagonal unitary rephasing | Removes tree phases and identifies cycle invariant | standard finite linear algebra | runner + note | yes | yes | Direct finite algebra | Proved/checkable in runner |
| Quark comparator targets | Parent numerical-match surface only | observational comparator | parent runner | no | no for this block | Derive in future or keep parent numerical-match | Forbidden as proof input here |
| `xi_u`, `xi_d` fitted values | Parent numerical-match coefficients | fitted input | parent runner | no | no for this block | Future theorem route | Not used |

No new axiom, primitive, Tier-A admission, audit status, or ledger row is
introduced.
