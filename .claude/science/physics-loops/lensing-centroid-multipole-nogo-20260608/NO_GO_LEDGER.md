# No-Go Ledger

## Nonnegative scalar-potential path/layer reduction for `kubo_true`

Status: no-go on the fixed finite harness.

Reason: the exact detector-centroid response is

```text
alpha(b) = sum_e c_e / r_e(b)
```

with signed adjoint coefficients.  Its scalar-potential monopole cancels to
`|M0|/sum|c| = 1.293740e-04`, while the signed dipole remains nonzero.  A
nonzero nonnegative scalar-potential path sum has `M0=sum w_e>0` and therefore
cannot be the same observable.

Scope: this does not rule out signed adjoint reductions, full wave/Kubo
derivations, or separate geometric lensing observables.
