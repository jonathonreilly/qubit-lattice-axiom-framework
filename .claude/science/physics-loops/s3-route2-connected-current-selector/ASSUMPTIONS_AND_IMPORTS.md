# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Exact `F_adj=8/9` and singlet `1/9` | Defines the two-channel packet | retained support | `RCONN_DERIVED_NOTE.md` | yes | yes | already available exact support | used |
| Adjoint normalization | Fixes adjoint coefficient | admitted normalization | Rconn matching-rule packet | yes | yes | exact normalization convention | used |
| CMT scale invariance | Tests scale controls | support-only | Rconn matching-rule packet | yes | no | no-go route | shown insufficient |
| OZI-size control | Bounds singlet contribution | support-only | Rconn matching-rule packet | yes | no | no-go route | shown insufficient |
| Connected-current projector | Would set `kappa=0` exactly | unsupported import | current surface | yes | yes | connected-current theorem | exposed as open |

The block forbids using endpoint target matching as the selector.  It exposes
`kappa=0` as exactly the singlet-annihilation premise.
