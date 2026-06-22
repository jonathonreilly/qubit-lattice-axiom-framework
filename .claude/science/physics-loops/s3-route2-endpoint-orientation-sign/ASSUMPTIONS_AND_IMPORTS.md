# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Endpoint algebra `c_TE=s_TE*q_T/q_E` | Forces sign relation | retained support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already available exact support | used |
| Conditional shell orientation `s_TE=-2` | Supplies negative sign | conditional-support | Route-2 T-side stretch premise | yes | yes | T-side theorem or demotion | explicit premise |
| Positive `q_T` and `q_E` | Prevent sign flip | conditional-support | endpoint positivity premise | yes | yes | positivity theorem or scoped condition | explicit premise |
| Connected selector `kappa=0` | Supplies magnitude `8/9` | unsupported import | Rconn packet | yes | yes | connected-current selector theorem | still open |

The block supports the orientation sign only under explicit endpoint
orientation/positivity premises.  It does not derive the endpoint magnitude.
