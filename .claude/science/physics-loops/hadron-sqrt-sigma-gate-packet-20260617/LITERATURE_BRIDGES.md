# Literature Bridges

The parent row already uses standard lattice-QCD/Sommer-scale constants as bounded bridge inputs. This PR does not add a new literature import or treat those constants as framework-native derivations.

The runner replays the currently declared constants only:

- `r0 = 0.472 fm`
- `r0/a = 5.37`
- `sigma a^2 = 0.0465`
- rough screening factor `0.96`

The next science move would be replacing this rough B2 bridge or validating B5 framework-side.
