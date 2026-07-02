# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Restricted Route-2 endpoint columns | Defines the carrier geometry and missing E-center direction | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already exact on parent surface | used |
| Granted T-side endpoint data `beta_T/alpha_T=-1`, `alpha_T/alpha_E=-2` | Reduces the live residual to `rho_E` | conditional support | exact readout/naturality notes | yes | yes | separate positive theorem or explicit admission | explicit conditional premise |
| Reduced family `P(rho_E)` | One-parameter readout family under the T-side grant | framework-derived from parent exact algebra | exact readout map note | yes | yes | derive the full endpoint triple | used |
| Finite tensor-polynomial closure | Defines the route family pruned by this block | standard algebraic closure | branch-local definition | yes | no for parent closure | none needed; it is the tested class | used |
| Universal time factor `V_R(t)` | Confirms the time/right factor does not supply `rho_E` | exact support | factor-rigidity note | yes | no | parent already supplies scope | used |
| E-center lift `q_E=15/8` | Positive selector that would force `rho_E=21/4` | unsupported import on current surface | E-center blindness/naturality notes | no, except as comparator | yes for positive closure | derive a nonblind E-center primitive | exposed as open blocker |
| Observed/live endpoint values | Forbidden target comparator | observational comparator/fitted input if used | not used | no | no | keep forbidden | excluded |

No literature values, observed masses, CKM/`J` fits, nearest-rational target
selection, or hidden source-domain weights are proof inputs.
