# Route Portfolio

## Chosen Route: Weighted Path LR

For a path of `n` finite-range hops, `d(x,y) <= n R_int`. Therefore for
`mu > 0`,

```text
1 <= exp(-mu d(x,y)) exp(mu n R_int)
```

in every contributing path term. Inserting this weight before summing the
finite path series gives

```text
2 ||A|| ||B|| exp(-mu d) sum_n (2 J_* D_int exp(mu R_int) |t|)^n / n!
```

Taking `mu=1/R_int` yields the stated
`v_LR = 2 e J_* D_int R_int`.

## Rejected Route: Direct Poisson Tail

The old display tried to recover the LR exponent from a truncated
Poisson tail. The recorded audit objection identified the load-bearing
inequality as false for the stated constants, so this branch does not
salvage that route.

## Deferred Route: Spatial Clustering

Spatial/static clustering still needs an independent retained gap-plus-LR
or transfer-matrix theorem. This branch does not attempt that promotion.
