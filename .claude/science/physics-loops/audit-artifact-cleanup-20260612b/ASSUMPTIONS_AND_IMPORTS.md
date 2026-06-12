# Assumptions And Imports

## Wilson-Corrected V_taste

The source note already has the corrected leading curvature coefficient:

```text
d^2 V^W / dm^2 |_{m=0} = -4/u_0^2 + 60 r^2/u_0^4 + O(r^4).
```

The runner executable checks already used `60`. This block only reconciles
stale docstring/comment text that still named `40`.

## Taste-Scalar CW Isotropy

Load-bearing input is the abstract binary taste block
`C^8 = (C^2)^{⊗3}` with commuting shift involutions. The physical
staggered-Dirac realization gate is kept visible as context only and is not a
proof input for the binary orthogonality identity.

This block also removes the runner's stale live-ledger expectation that the row
must remain unaudited; current main already has an audited conditional row.
