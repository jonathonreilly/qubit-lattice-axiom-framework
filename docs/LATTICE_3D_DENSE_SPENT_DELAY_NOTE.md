# 3D Dense Spent-Delay Finite Card Live Packet

**Date:** 2026-04-05; live-source repair 2026-06-08
**Status:** bounded-support finite card; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/lattice_3d_dense_10prop.py`](../scripts/lattice_3d_dense_10prop.py)
**Primary runner cache:** [`logs/runner-cache/lattice_3d_dense_10prop.txt`](../logs/runner-cache/lattice_3d_dense_10prop.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`lattice_3d_dense_spent_delay_note`. The archived note failed because it claimed
a distance window through `z=6`, while the live runner checks only `z=2,3,4,5`.

This repaired note keeps the executable finite card and removes the unsupported
`z=6` endpoint.

## Live Claim

For the canonical dense 3D spent-delay card,

```text
49 edges/node, spent-delay, s=5e-05
L=12, W=6, h=1.0, nodes=2197
```

the live runner reports:

```text
Born |I3|/P = 7.37e-16  [PASS]
d_TV = 0.3785  [PASS]
k=0 = 0.000000  [PASS]
F∝M alpha = 0.34  [PASS]
Gravity N=10: -0.009546 (AWAY)
Gravity N=12: +0.001941 (TOWARD)
Gravity N=15: +0.016972 (TOWARD)
Grows with N: YES  [PASS]
Decoherence = 13.5%  [PASS]
MI = 0.1414 bits  [PASS]
k=0 control = 0.000000  [PASS]
```

The live distance check is exactly:

```text
z=2: centroid=+0.003101, P_near=+0.001469, bias=+0.107097 [ATTRACTIVE]
z=3: centroid=+0.001941, P_near=+0.000374, bias=+0.176381 [ATTRACTIVE]
z=4: centroid=+0.001157, P_near=+0.000626, bias=+0.113676 [ATTRACTIVE]
z=5: centroid=+0.000693, P_near=+0.000715, bias=+0.048601 [ATTRACTIVE]
Hierarchy-aligned support: 4/4 points, b^(-1.62), R²=0.976
```

## Boundary

This row claims only the finite runner card above. It does not claim a `z=2..6`
window, an asymptotic distance law, a continuum attraction theorem, or effective
retained status before independent audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/lattice-dense-spent-delay-window-salvage-2026-04-30/LATTICE_3D_DENSE_SPENT_DELAY_NOTE.md`](../archive_unlanded/lattice-dense-spent-delay-window-salvage-2026-04-30/LATTICE_3D_DENSE_SPENT_DELAY_NOTE.md).
