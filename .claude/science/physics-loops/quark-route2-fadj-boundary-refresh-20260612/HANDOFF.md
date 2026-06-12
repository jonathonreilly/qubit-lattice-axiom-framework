# Quark Route-2 F_adj Boundary Refresh Handoff

## What changed

- Updated the Route-2 obstruction note to distinguish exact SU(3) adjoint
  fraction support `F_adj = 8/9` from underived physical connected-trace
  `R_conn` readout.
- Updated the runner source-anchor check to match the repaired
  `RCONN_DERIVED_NOTE.md` wording.
- Preserved the obstruction: `gamma_T(center)/gamma_E(center) = -F_adj` remains
  the missing typed source-domain bridge.

## Verification

```text
python3 scripts/frontier_quark_route2_rconn_center_ratio_bridge_obstruction.py
```

Result: `TOTAL: PASS=26, FAIL=0`.

## Boundaries

No audit data was edited. This branch does not derive the physical `R_conn`
readout, does not close the Route-2 endpoint bridge, and does not promote quark
mass claims.

