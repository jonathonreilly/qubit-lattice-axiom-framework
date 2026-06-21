# Handoff

Block35 tests the color-complement seven-eighths candidate:

```text
(dim(adj)-1)/dim(adj) = 7/8.
```

Expected result: route-specific no-go. The SU(3) adjoint has no invariant
one-dimensional line and no invariant rank-seven projector, so current
Fierz/Rconn color data cannot source `route2_e_E_7_8` by removing one adjoint
direction.

Current status: verification passed. PR creation pending.

Checks:

- block35 runner: `PASS=51 FAIL=0`
- Rconn typed bridge parent: `PASS=62 FAIL=0`
- S3-time theta-to-slice parent: `PASS=12 FAIL=0`
- EW Fierz parent: `PASS=31 FAIL=0`
- Route-2 exact readout parent: `PASS=11 FAIL=0`
- new runner py_compile: pass
- branch-local overclaim scan: no matches

Next exact action after PR: pivot to measured-calibration box-size
parameterization or the hierarchy/APBC seven-eighths bridge.
