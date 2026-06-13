# Finite-Cell Two-Band Peierls Response Has an Exact Discrete Momentum Closed Form on the Q = 24, Ly = 2 Harper Cell

**Claim type:** bounded_theorem

**Status authority:** independent audit lane

**Scope.** Free staggered two-band square-lattice model, finite Harper cell `Q = 24, Ly = 2`, hopping `t = 1`, probe point `mu = 1.7086`, `T = 0.2`, and the finite-cell Peierls `B^2` perturbation used by the #3743 machinery. This note does not claim an interacting result, an all-gauge theorem, or an audited replacement for the missing N1 branch artifact.

## Claim

On the #3743 finite cell, the full two-band orbital response is exactly a finite discrete momentum sum.  For each boundary twist, the `B = 0` Hamiltonian decomposes into `Q` two-band blocks

```text
H_n = [[epsilon_n, m],
       [m,        -epsilon_n]],
epsilon_n = -2 (cos((kx + 2 pi n)/Q) + cos(ky/2)).
```

The Peierls variations are not fitted constants. They are the exact finite Fourier sums

```text
X_nm  = (1/Q) sum_x x   exp(i 2 pi (m-n)x/Q),
X2_nm = (1/Q) sum_x x^2 exp(i 2 pi (m-n)x/Q),
```

inserted into the standard finite-dimensional divided-difference formula for the grand potential. This gives the same object as the direct real-space Harper perturbation calculation, but as a finite discrete momentum sum over the `Q` momenta and the two sublattice bands.

## Frozen Anchors

The runner recomputes the finite sum first, then gates against the exact external #3743 anchors:

| mass | #3743 anchor |
| ---: | ---: |
| `0` | `0.042933687517` |
| `0.2` | `0.041273318495` |
| `0.3` | `0.039175811591` |
| `0.5` | `0.030744459999` |

The anchor values are comparison targets only. They are not used to construct the response, tune a prefactor, or round intermediate values.

## Discriminators

The runner uses three non-tautological checks.

1. The finite discrete momentum sum is compared against a separately built real-space Harper `H0,H1,H2` perturbation calculation. The two agree at the fixed `1e-10` closed-form tolerance.
2. A finite-difference Peierls check at `m = 0.2` halves `B` from `5e-4` to `2.5e-4` and gates the observed convergence ratio toward the closed-form value.
3. The off-mass interband term is required to be nonzero, excluding a one-band or parity-proxy calculation.

## Moyal Comparator

The local worktree does not contain the named N1 branch artifact, so the runner includes a bounded Moyal comparator rather than importing an unavailable file. The comparator is the determinant-Hessian member of the continuum two-band `B^2` density evaluated as midpoint finite-Q sums at `Q = 24, 48, 96, 192`, with `Q = 384` used only as a high-resolution target for a monotone convergence gate.

This comparator is used to check the discrete-to-continuum quadrature behavior of the continuum expression. It is not used to force the finite-cell anchors, and it is not claimed here as the complete audited N1 formula.

## Residuals

The finite-cell theorem closes only the #3743 finite-cell object: exact finite momentum sum equals direct finite Harper perturbation and reproduces the four external anchors. The complete continuum-Moyal comparison remains bounded to the local comparator implemented in the runner until the N1 source artifact is present in the worktree and can be mirrored directly.

Runner:

```text
python3 scripts/frontier_finite_cell_two_band_closed_form_2026_06_13.py
```
