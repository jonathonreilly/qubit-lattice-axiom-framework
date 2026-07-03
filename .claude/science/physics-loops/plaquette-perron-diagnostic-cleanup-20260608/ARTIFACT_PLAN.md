# Artifact Plan

## Implemented

- Corrected one-plaquette diagnostic function to return `c_(0,0)(beta)`.
- Changed `P_1plaq` to finite-difference `d/d beta log c_(0,0)(beta)`.
- Added runner support check that `P_1plaq` agrees with `a_(1,0)` on the audited surface.
- Tightened endpoint language in note and runner output.
- Refreshed the runner cache.

## Not Implemented

- No audit ledger edits.
- No physical 3D spatial Wilson environment solve.
- No canonical plaquette-value closure.
