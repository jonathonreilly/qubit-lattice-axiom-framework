# ASSUMPTIONS_AND_IMPORTS

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| finite architecture configurations | configured sweep domain | computed lattice input | `scripts/frontier_architecture_portability_sweep.py` | yes | yes | runner/cache | explicit |
| source-mass scaling beta | measured bounded observable | computed lattice input | runner/cache | yes | yes | runner/cache | checked 4/4 |
| attraction sign | measured bounded observable | computed lattice input | runner/cache | yes | yes | runner/cache | checked 4/4 |
| Born `I_3` | measured only where barrier implementation exists | computed lattice input | ordered/staggered rows in runner/cache | yes for measured rows | yes for measured scope | runner/cache | checked; Wilson/random marked `n/a` |
| distance-law closure | excluded stronger claim | unsupported for this bridge | boundary text | no | no | separate family-specific distance-law rows | not claimed |
| both-masses closure | excluded stronger claim | unsupported for this bridge | boundary text | no | no | separate theorem/runner | not claimed |

No observed comparators, fitted target values, or new axioms are used by this
bridge.
