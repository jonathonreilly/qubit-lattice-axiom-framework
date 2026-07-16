# Gauge-Vacuum Plaquette Perron-State Reduction Theorem

**Date:** 2026-04-16
**Type:** positive_theorem
**Claim boundary:** exact Perron and Jacobi-data reduction for the finite
periodic cubic `SU(3)` Wilson carrier with `L_s >= 2`, normalized Haar measure,
`beta > 0`, and periodic derived time, conditional on the paired positive
Wilson transfer theorem; explicit Perron / Jacobi data at `beta = 6` remain
open.
**Status authority:** independent audit lane only. This source note does not
set, apply, or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_gauge_vacuum_plaquette_perron_reduction_theorem.py`](../scripts/frontier_gauge_vacuum_plaquette_perron_reduction_theorem.py)
**Runner cache:**
[`logs/runner-cache/frontier_gauge_vacuum_plaquette_perron_reduction_theorem.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_perron_reduction_theorem.txt)

## Question

After making the plaquette generating object explicit at the operator level, can
the remaining `beta = 6` state-identification problem be reduced exactly to a
smaller object?

## Answer

Yes.

On every finite Wilson `L_s^3 x L_t` source surface with `beta > 0`, the exact
one-clock transfer operator `T_(L_s,beta)` has a strictly positive symmetric
kernel on the compact gauge-invariant spatial configuration space.

Therefore:

- `T_(L_s,beta)` is compact and self-adjoint,
- `T_(L_s,beta)` is positivity-improving,
- its spectral radius `lambda_0(L_s,beta)` is simple,
- there is one unique normalized strictly positive Perron vector
  `psi_0(L_s,beta)`.

For every bounded Borel function `f` of the spatial plaquette multiplication
operator `A_p` on the gauge-invariant Hilbert space, the exact transfer-state
law satisfies

`lim_(L_t -> infty)
 Tr[T_(L_s,beta)^(L_t) f(A_p)] / Tr[T_(L_s,beta)^(L_t)]
 = <psi_0(L_s,beta), f(A_p) psi_0(L_s,beta)>`.

So the framework-point plaquette problem is no longer:

- identify an abstract spectral measure,
- or identify a full thermal trace state.

It is now exactly:

> identify the Perron vector `psi_0(L_s,6)` for the full transfer state; for
> the plaquette-observable law alone, identify the spectral measure or Jacobi
> data of `A_p` in that Perron state.

That is the right reduced target.

## Setup

From the paired
[Wilson transfer / character-recurrence theorem](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md):

- the finite Wilson partition function factors as
  `Z_(L_s,L_t)(beta) = Tr[T_(L_s,beta)^(L_t)]`,
- `T_(L_s,beta)` is a positive self-adjoint one-clock transfer operator,
- the local spatial plaquette source on the full gauge-invariant Hilbert space
  is the bounded self-adjoint multiplication operator
  `(A_p psi)(U) = X(U_p) psi(U)`,
- on `L^2_class(SU(3))`, the explicit class-function multiplication operator
  `J = (chi_(1,0) + chi_(0,1)) / 6` is related by the isometric pullback
  `(I_p phi)(U) = phi(U_p)` through
  `A_p I_p = I_p J`.

The transfer theorem does not assert that `Range(I_p)` is invariant under
`T_(L_s,beta)`. Thus `J` is not inserted directly into a full transfer trace;
the trace insertion is `A_p`, and `J` represents the same local multiplication
algebra only through the pullback.

## Theorem 1: exact Perron reduction of the transfer state

For `beta > 0`, the kernel of `T_(L_s,beta)` is pointwise strictly positive.
Because the spatial configuration space is compact and the kernel is continuous,
`T_(L_s,beta)` is Hilbert-Schmidt and therefore compact.

By symmetry of the kernel, `T_(L_s,beta)` is self-adjoint.

By positivity improvement and the compact self-adjoint Perron-Jentzsch theorem:

- the spectral radius `lambda_0(L_s,beta)` is an eigenvalue,
- that eigenvalue is simple,
- the corresponding normalized eigenvector `psi_0(L_s,beta)` can be chosen
  strictly positive and is then unique up to sign.

So there is one exact Perron state for the finite Wilson transfer problem.

## Corollary 1: exact zero-temperature / large-derived-time reduction

Let

`rho_(L_s,L_t,beta)(f)
 = Tr[T_(L_s,beta)^(L_t) f(A_p)] / Tr[T_(L_s,beta)^(L_t)]`.

Using the spectral decomposition of `T_(L_s,beta)` and simplicity of
`lambda_0`, one gets

`rho_(L_s,L_t,beta)(f)
 -> <psi_0(L_s,beta), f(A_p) psi_0(L_s,beta)>`

as `L_t -> infty` for every bounded Borel `f`.

Therefore the transfer-state identification problem reduces exactly to the
Perron vector.

## Theorem 2: exact symmetry reduction of the Perron state

Any unitary symmetry `S` that commutes with `T_(L_s,beta)` must preserve the
one-dimensional Perron eigenspace. If, in addition, `S` preserves positivity,
then it fixes the normalized positive Perron vector.

Hence

`S psi_0(L_s,beta) = c_S psi_0(L_s,beta)`

for some phase `c_S`.

But `psi_0(L_s,beta)` is strictly positive and `S` preserves positivity, so
`c_S = 1`.

Therefore the Perron state is exactly invariant under every positivity-preserving
symmetry commuting with the transfer operator.

This statement applies only after such a symmetry has been defined on the full
gauge Hilbert space and proved to commute with `T_(L_s,beta)`. The local
`(p,q) <-> (q,p)` action of `J` is not by itself such a full-space lift.

## Corollary 2: exact Jacobi-data reduction

Let `mu_(L_s,beta)^P` be the spectral measure of `A_p` in the Perron vector:

`mu_(L_s,beta)^P(B) = <psi_0(L_s,beta), E_(A_p)(B) psi_0(L_s,beta)>`.

Then

`<psi_0(L_s,beta), A_p^n psi_0(L_s,beta)>
 = integral x^n dmu_(L_s,beta)^P(x)`

for all `n >= 0`.

By the spectral theorem and orthogonal-polynomial construction, this measure is
equivalent to one unique Jacobi operator on the cyclic subspace generated by
`psi_0` under repeated application of `A_p`.

Equivalently, define the pulled-back state on the local class-function
multiplication algebra by

`omega_tilde_(L_s,beta)(f(J))
 = <psi_0(L_s,beta), f(A_p) psi_0(L_s,beta)>`.

The intertwiner `A_p I_p = I_p J` identifies the local multiplication rule,
including the six-neighbor character recurrence. It does not place
`psi_0` in `L^2_class(SU(3))` or make `Range(I_p)` transfer invariant.

Thus the framework-point plaquette-observable law is equivalent to explicit
framework-point Jacobi data:

- diagonal coefficients `a_n(6)`,
- off-diagonal coefficients `b_n(6)`,
- or equivalently the Perron moments of `A_p`, represented locally by the
  multiplication operator `J`.

## What this closes

- exact reduction of the transfer-state problem to one unique strictly positive
  Perron vector on each finite Wilson `3+1` source surface
- exact large-derived-time reduction from thermal trace state to Perron state
- exact invariance of that Perron state under every separately established
  full-space positivity-preserving symmetry commuting with the transfer
- exact reformulation of the remaining `beta = 6` plaquette-observable problem
  as Jacobi data for `A_p`, with the local multiplication rule represented by
  `J`

## What this does not close

- explicit construction of `psi_0(L_s,6)`
- explicit Jacobi coefficients at `beta = 6`
- transfer invariance of `Range(I_p)`
- identification of the full gauge-invariant Hilbert space with
  `L^2_class(SU(3))`
- reconstruction of the full Perron vector from the one-observable Jacobi data
- explicit infinite-volume control in `L_s`
- analytic closure of canonical `P(6)`
- repo-wide repinning of the canonical plaquette

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_perron_reduction_theorem.py
```

Expected summary:

```text
SUMMARY: THEOREM PASS=0 SUPPORT=10 FAIL=0
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

The conditional verdict flagged a missing cited retained dependency for the exact transfer-operator / character-recurrence theorem proving strict positivity of `T_(L_s,beta)`. That authority is supplied by:

- [gauge_vacuum_plaquette_transfer_operator_character_recurrence_note](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)
