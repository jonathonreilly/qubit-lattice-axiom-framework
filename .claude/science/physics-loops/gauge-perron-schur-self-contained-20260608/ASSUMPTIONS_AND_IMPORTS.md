# Assumptions And Imports

## Retained Or Internal Inputs

- `c_(p,q)(6)` Bessel-determinant coefficient computation already used by the
  gauge Perron runner.
- `SU(3)` dominant-weight dimension formula.
- The existing source-sector operator `J`, local factor `D_6^loc`, and Perron
  solver in `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py`.

## New Internalized Calculation

- All-forward `L_s=2` PBC cube graph enumeration: 12 plaquettes, 24 directed
  links, 48 cyclic-index nodes, 48 identifications, 8 connected components.
- Raw-coefficient Schur rho:

```text
rho_(p,q) = ((d_(p,q) c_(p,q)(6) / c_(0,0)(6))^12)
            * d_(p,q)^(8 - 24)
```

After normalization this is `(c_(p,q)(6)/c_(0,0)(6))^12 d_(p,q)^(-4)`.

## Explicitly Not Imported

- The `0.429104996947` value is not imported from a sibling SU3 row; the
  edited runner recomputes it.
- Canonical `P(6)=0.5934` remains comparator/context only and is not used as a
  fit target or proof input.
- The physical 3D Wilson residual environment rho remains open.
