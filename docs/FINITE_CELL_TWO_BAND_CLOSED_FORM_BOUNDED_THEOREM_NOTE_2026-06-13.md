# Finite-Cell Two-Band Peierls Response Has an Exact Discrete Momentum Closed Form on the Q = 24, Ly = 2 Harper Cell

**Claim type:** bounded_theorem

**Status authority:** independent audit lane

**Scope.** Supplied free staggered two-band square-lattice model, finite Harper
cell `Q = 24, Ly = 2`, hopping `t = 1`, probe point `mu = 1.7086`, `T = 0.2`,
and the finite-cell Peierls `B^2` perturbation defined below. These parameters
are fixed inputs to the bounded calculation. This note does not claim an
interacting result, an all-gauge theorem, a continuum theorem, or an audited
replacement for the missing continuum-Moyal source artifact.

## Claim

On the supplied finite cell, the full two-band orbital response is exactly a
finite discrete momentum sum. For each boundary twist, the `B = 0` Hamiltonian
decomposes into `Q` two-band blocks

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

## Discriminators

The runner uses three non-tautological checks.

1. The finite discrete momentum sum is compared against a separately built real-space Harper `H0,H1,H2` perturbation calculation. The two agree at the fixed `1e-10` closed-form tolerance.
2. A finite-difference Peierls check at `m = 0.2` halves `B` from `5e-4` to `2.5e-4` and gates the observed convergence ratio toward the closed-form value.
3. The off-mass interband term is required to be nonzero, excluding a one-band or parity-proxy calculation.

## Moyal Comparator

The local worktree does not contain the named continuum-Moyal source artifact,
so the runner includes a bounded Moyal comparator rather than importing an
unavailable file. The comparator is the determinant-Hessian member of the
continuum two-band `B^2` density evaluated as midpoint finite-Q sums at
`Q = 24, 48, 96, 192`, with `Q = 384` used only as a high-resolution target
for a monotone convergence gate.

This comparator is used to check the discrete-to-continuum quadrature behavior
of the continuum expression. It is not used to force the finite-cell response,
and it is not claimed here as the complete audited continuum-Moyal formula.

## Residuals

The finite-cell theorem closes only the supplied finite-cell object: exact
finite momentum sum equals direct finite Harper perturbation on the stated
cell and parameters. The complete continuum-Moyal comparison remains bounded
to the local comparator implemented in the runner until the continuum-Moyal
source artifact is present in the worktree and can be mirrored directly.

Runner:

```text
python3 scripts/frontier_finite_cell_two_band_closed_form_2026_06_13.py
```

Runner cache:

```text
logs/runner-cache/frontier_finite_cell_two_band_closed_form_2026_06_13.txt
```
