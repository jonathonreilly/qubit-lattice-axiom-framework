# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Two-channel Rconn packet | Defines adjoint and singlet channels | retained support | `RCONN_DERIVED_NOTE.md` | yes | yes | already available exact support | used |
| Adjoint normalization | Fixes adjoint coefficient to one | admitted normalization | Rconn matching packet | yes | yes | exact convention | used |
| Projector idempotence | Narrows `kappa` to roots of `kappa^2=kappa` | conditional-support | current-projector premise | yes | yes | connected-current theorem | conditional |
| Strict singlet suppression | Selects `kappa=0` among idempotents | unsupported import | current surface | yes | yes | singlet-annihilation theorem | exposed |

This block gives bounded support: idempotence narrows the selector to a binary
choice, but does not itself derive the connected endpoint.
