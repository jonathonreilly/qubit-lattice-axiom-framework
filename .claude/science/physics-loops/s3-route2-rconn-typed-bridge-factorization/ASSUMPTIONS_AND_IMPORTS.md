# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Exact SU(3) adjoint fraction `F_adj=8/9` | Provides the positive color scalar | retained support | `RCONN_DERIVED_NOTE.md` | yes | yes | already available exact support | used |
| Physical selector `kappa=0` | Turns `R_phys(kappa)` into `8/9` | unsupported import | Rconn repair packet | yes | yes | connected-current selector theorem | exposed |
| Endpoint orientation sign `sigma=-1` | Turns positive color scalar into negative `T/E` center ratio | unsupported import | Route-2 source-domain bridge | yes | yes | typed source-domain functor theorem | exposed |
| Conditional T-side values | Convert `c_TE=-8/9` into `rho_E=21/4` | conditional-support | Route-2 readout stack | yes | yes | separate T-side theorem or demotion | used as stretch premise |
| Observed endpoint closeness | Motivation only | observational comparator | live bounded endpoint data | no | no | forbidden as proof input | not used |

The block retires the shortcut that exact `R_conn=8/9` alone supplies the
typed center ratio.  The bridge requires two named switches.
