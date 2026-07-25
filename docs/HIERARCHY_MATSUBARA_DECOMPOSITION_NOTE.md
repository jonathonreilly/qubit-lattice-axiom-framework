# Hierarchy Matsubara Decomposition Note

**Date:** 2026-04-13  
**Script:** `scripts/frontier_hierarchy_matsubara_decomposition.py`

## Question

Can the hierarchy determinant and condensate be written in an exact temporal
mode decomposition on the minimal APBC hypercube, so that the remaining Part 3
gap becomes a precise temporal-averaging problem rather than a vague prefactor?

## Exact result

Yes.

For the full staggered Dirac operator with mass `m` on the minimal spatial APBC
block `L_s = 2`, at every temporal extent `L_t`:

`|det(D + m)| = prod_omega [m^2 + u_0^2 (3 + sin^2 omega)]^4`

with `omega_n = (2n+1) pi / L_t`, `n = 0, ..., L_t - 1`.

The five steps below derive this as an operator identity, symbolically and for
general `L_t`, rather than reading it off a sampled momentum grid. In particular
the exponent `4` is derived, not observed.

### Step 1 — the operator splits as space (x) time

Writing the site index as `a * L_t + t`, with `a` running over the 8 spatial
sites of the `L_s = 2` block, the staggered operator is exactly

`D(m) = m Id + u_0 (B (x) Id_t) + u_0 (eta_4 (x) S)`

where `B` is the 8x8 sum of the three spatial staggered hops,
`eta_4 = diag((-1)^(x_1+x_2+x_3))` is the fourth staggered sign, and `S` is the
`L_t x L_t` antisymmetric temporal hop. `B` and `eta_4` are read out of the
assembled matrix rather than posited; they come out identical for
`L_t = 2,3,4,5,6,8`, and substituting `Id_8` for `eta_4` fails to reproduce the
matrix.

### Step 2 — the two-site antiperiodic ring is an operator identity

On a two-site antiperiodic ring the shift `T_i` obeys `T_i^2 = -Id`, and the
antisymmetric hop `(T_i - T_i^(-1))/2` collapses onto `T_i` itself: forward and
backward hops connect the same pair of sites, and the antiperiodic wrap flips
the sign of exactly one of them, so they add rather than cancel. Each spatial
direction therefore contributes a single `+-1` matrix `A_i` with

`A_i^2 = -Id_8`,   `A_i A_j + A_j A_i = 0`  for `i != j`

and hence, for `B = A_1 + A_2 + A_3`,

`B^2 = -3 Id_8`,  `tr B = 0`,  `eta_4^2 = Id_8`,  `tr eta_4 = 0`,
`B eta_4 + eta_4 B = 0`

all in exact integer arithmetic. This is what fixes the spatial contribution to
the constant `3` at every temporal mode and every `L_t`. The momentum-space
reading — all spatial momenta sitting at Brillouin-zone corners, so
`sin^2(k_i) = 1` — returns the same number, but only as a property of a sampled
grid; the identity `A_i^2 = -Id_8` is what carries the derivation, and it needs
no momentum labels at all.

### Step 3 — the temporal factor diagonalizes at every `L_t`

The temporal hop is `S = (T - T^(-1))/2` for the antiperiodic shift `T`. Cofactor
expansion of `det(lam Id - T)` leaves only the diagonal product and the single
full cycle, whose antiperiodic wrap contributes one factor `-1`, so

`charpoly(T) = lam^(L_t) + 1`

at every `L_t` (checked symbolically for `L_t = 2..16`). That polynomial is
squarefree, so `T` is diagonalizable with `L_t` simple eigenvalues
`z_n = exp(i omega_n)`, `omega_n = (2n+1) pi / L_t`, and on the eigenvector
`v(z) = [1, z, ..., z^(L_t - 1)]`

`S v(z) = (1/2)(z - 1/z) v(z) = i sin(omega) v(z)`

So the APBC Matsubara frequencies are an output of the temporal algebra, not an
input to it.

### Step 4 — multiplicity four, forced by tracelessness

In the temporal eigenbasis `D(m)` is block-diagonal, one 8x8 block per mode:

`D(m)|_omega = m Id_8 + K(omega)`,  `K(omega) = u_0 (B + i sin(omega) eta_4)`

Using only the Step 2 relations,

`K^2 = u_0^2 [B^2 + i sin(omega) (B eta_4 + eta_4 B) - sin^2(omega) eta_4^2]
     = -u_0^2 (3 + sin^2 omega) Id_8`

`tr K = u_0 [tr B + i sin(omega) tr eta_4] = 0`

A traceless operator on an 8-dimensional space whose square is `-c Id` with
`c > 0` can only have the eigenvalues `+- i u_0 sqrt(3 + sin^2 omega)`, and
tracelessness forces them to occur with equal multiplicity, `4` and `4`. Hence

`charpoly K(omega) = (lam^2 + u_0^2 (3 + sin^2 omega))^4`

`det(m Id_8 + K(omega)) = [m^2 + u_0^2 (3 + sin^2 omega)]^4`

The exponent `4` is exactly that `4 + 4` eigenvalue split on the 8-dimensional
spatial block. It is not fitted, and not read off the tested grid.

### Step 5 — general `L_t`

Step 4 is carried out once symbolically in `(theta, u_0, m)` with `theta` a free
symbol, so it covers every temporal mode of every `L_t` at once: `L_t` enters
only through the substitution `theta -> omega_n`. Multiplying the `L_t` blocks
returns the displayed product formula at every `L_t`, not only on the tested
grid. The paired runner also rejects the exponents `3` and `5` and the spatial
constant `2 + sin^2 theta`, and chains symbolic block determinant -> product
formula -> direct numerical determinant.

This is an exact closed form on the `L_s = 2` APBC hypercube.

## Consequences

### 1. The determinant is no longer mysterious

The old numerical factorization

`det(D_{2n}) = det(D_2)^n * C_n`

is now explained exactly: it is just the product over the APBC Matsubara
frequencies.

### 2. The intensive observables are also exact

The free-energy density difference is:

`Delta f = (1 / (2 L_t)) sum_omega ln(1 + m^2 / [u_0^2 (3 + sin^2 omega)])`

and the condensate density is:

`(1/N) Tr[(D+m)^(-1)] = (m / L_t) sum_omega 1 / [m^2 + u_0^2 (3 + sin^2 omega)]`

Both formulas match the direct matrix computation to machine precision.

### 3. The remaining theorem is now sharply stated

The open question is no longer:

> what is the prefactor?

It is:

> which temporal averaging of this exact Matsubara formula is the physical
> EWSB order parameter?

That is a much better problem.

## UV endpoint picture

`L_t = 2` is the unique APBC endpoint where every temporal mode has
`sin^2 omega = 1`: the mode closest to zero sits at `omega_0 = pi / L_t`, which
reaches `pi/2` only at `L_t = 2`, so every larger extent carries at least one
mode with `sin^2 omega < 1`. This is checked exactly over `L_t = 2..16`.

So the one-block hierarchy route is the **maximal temporal-gap endpoint** of
the exact Matsubara family, not an arbitrary guess.

Larger `L_t` values average in lower-gap temporal modes. The exact condensate
density ratio between `L_t = 10` and `L_t = 2` at `u_0 = 0.9`, `m = 10^-2` is:

`R ~= 1.15469`

The crucial compression result is:

- `R^(-1/16) ~= 0.99105`  (too small to explain the observed `254.64 -> 246.22` gap)
- `R^(-1/4)  ~= 0.96468`  (in the right few-percent range)

So the exact Matsubara formulas support the interpretation that the final
normalization problem is much more naturally a **dimension-4 effective-potential
density** issue than a direct sixteenth-root correction to the scale.

## Honest conclusion

This still does **not** close the hierarchy theorem.

What it settles is the temporal algebra:

- determinant formula: exact
- free-energy density formula: exact
- condensate density formula: exact

What remains open:

1. why the physical electroweak order parameter is the `L_t = 2` UV endpoint,
   or an explicitly derived function of the exact Matsubara average
2. why the corresponding normalization lands on the observed
   `C_obs ~= 0.96692`
3. the spatial APBC issue on even `L = 2`
4. the framework-native derivation of `alpha_LM`

But Part 3 is now much tighter:

> the final theorem is an order-parameter selection / normalization theorem on
> top of an already-exact temporal mode decomposition.
