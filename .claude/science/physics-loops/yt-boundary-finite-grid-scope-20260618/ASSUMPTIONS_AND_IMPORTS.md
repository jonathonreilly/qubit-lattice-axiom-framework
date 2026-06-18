# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Finite runner implementation | Defines the sampled diagnostic surface | computed lattice input | `scripts/frontier_yt_boundary_bc_transfer_uniqueness.py` | yes | yes | already explicit | retained only as runner-local evidence |
| Canonical plaquette constants | Numerical implementation inputs | admitted implementation input | `scripts/canonical_plaquette_surface.py` | yes for runner replay | yes for replay, not proof authority | retained/accepted plaquette authority | kept as declared input |
| Ward target | Boundary value for the root check | admitted implementation input | runner constant | yes for runner replay | yes for replay, not proof authority | retained Ward theorem | kept as declared input |
| Two-loop SM RGE normalization | Evolves the five-channel system | standard/imported implementation input | runner code | yes for runner replay | yes for replay, not proof authority | framework-native or accepted RGE authority | kept as declared input |
| Threshold seeds | Numerical RGE seeds | admitted implementation input | runner constants | yes for runner replay | yes for replay, not proof authority | accepted threshold-seed authority | kept as declared input |
| EW initial-condition surface | Initial couplings for the replay | admitted implementation input | runner constants | yes for runner replay | yes for replay, not proof authority | retained/accepted EW initial surface | kept as declared input |
| Continuum uniqueness theorem | Would upgrade grid replay to exact theorem | unsupported import | audit blocker text | no | yes for stronger theorem | interval/validated-numerics proof | excluded from claim |
