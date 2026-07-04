# No-Go Ledger

| Route | Verdict | Reason |
|---|---|---|
| Record additivity plus C3 covariance | no-go | Forces equality of cell coefficients only; leaves `alpha` free. |
| Fixed-locus arithmetic | no-go for h-class | Supplies `L3(1,2)=2/9` inside the fixed-locus class, not the physical class selection. |
| Supplied finite context / W2 | no-go for h-class | Supplies finite registrable context; leaves physical carrier realization and `A_R-eta` admitted. |
| Holonomy normal form | no-go for h-class | Rewrites the wall as `Phi(c)=c S_sum`; does not derive the value/readout equation. |
| Approved primitive registry | no-go | Contains no h-class, R-eta, physical-observable bridge, event law, or selector. |
| h-unit shortcut | out of scope | Block44 separately shows h-unit is not supplied by approved axioms/primitives. |
| owner primitive | governance, not derivation | Not imported in this block. |

## Exact Witness

The runner solves the C3 covariance constraints for a finite additive scalar
on a three-cell orbit and obtains the one-parameter family:

```text
I_alpha(x0, x1, x2) = alpha (x0 + x1 + x2).
```

On `(1,1,1)`, the fixed-locus-density member is selected only by
`alpha = 2/27`. Multiple other alpha values satisfy the same formal
constraints and give different values.
