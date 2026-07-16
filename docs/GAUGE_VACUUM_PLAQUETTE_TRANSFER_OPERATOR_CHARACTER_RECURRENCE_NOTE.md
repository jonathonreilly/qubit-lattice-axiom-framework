# Gauge-Vacuum Plaquette Transfer-Operator / Character-Recurrence Theorem

**Date:** 2026-07-16
**Type:** positive_theorem
**Status:** proposed_retained exact finite-volume positive-transfer theorem;
independent audit ratification required
**Script:** `scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py`

## Question

Can the finite Wilson transfer kernel be proved positive in the
quadratic-form sense, and can the marked plaquette observable be related
exactly to the local `SU(3)` character recurrence without assuming that a
source-cyclic subspace is transfer invariant?

## Answer

Yes, with two scope restrictions.

First, for `beta >= 0` and finite spatial volume, the one-link Wilson class
function

`w_beta(g) = exp[(beta/3) Re Tr(g)]`

has nonnegative Peter-Weyl character coefficients. This makes linkwise
Wilson convolution positive semidefinite. After the finite-volume gauge
projector and the spatial half weights are inserted, the exact transfer
operator has the Gram factorization

`T_beta = M_beta Q_beta M_beta
        = (Q_beta^(1/2) M_beta)^* (Q_beta^(1/2) M_beta) >= 0`.

Thus the finite Wilson identity

`Z_(L_s,L_t)(beta) = Tr[T_(L_s,beta)^(L_t)]`

does use a positive self-adjoint transfer operator `T_(L_s,beta)`.

Second, a marked **spatial** plaquette on one time slice is the multiplication
operator

`A_p = (1/3) Re Tr(U_p)`.

Its local class-function algebra is exactly intertwined with multiplication
by

`X = (chi_(1,0) + chi_(0,1)) / 6`

on `L^2_class(SU(3))`. The six-neighbor character recurrence therefore gives
an exact operator presentation of that spatial source algebra. No claim is
made that this local class-function subspace is invariant under `T_beta`, or
that a local recurrence eigenvalue is an eigenvalue of the full transfer
operator.

A mixed temporal plaquette is different: it is an insertion into the
two-slice kernel `Q_beta`, not automatically a one-slice multiplication
operator.

## Finite-volume setup

Let `E` be the oriented spatial links and `V` the spatial vertices of a finite
periodic lattice with `L_s >= 2`. Put

`H = L^2(SU(3)^E, dU)`.

All Haar measures below are normalized. For
`h = (h_x)_(x in V)`, the time-independent gauge action is

`(h . U)_e = h_(s(e)) U_e h_(t(e))^(-1)`.

Let the induced unitary action be

`(Gamma_h psi)(U) = psi(h^(-1) . U)`,

and let

`P_G = integral dh Gamma_h`

be the orthogonal projector onto the gauge-invariant Hilbert space `H_G`.
This is the gauge-invariant spatial Hilbert space used below.

Define the one-link convolution and its finite-link product by

`(C_(e,beta) psi)(U'_e)
 = integral dU_e w_beta(U'_e U_e^(-1)) psi(U_e)`,

`C_beta = tensor_(e in E) C_(e,beta)`.

The spatial half-weight is the bounded positive multiplication operator

`(M_beta psi)(U)
 = exp[(beta/6) sum_(p spatial) Re Tr(U_p)] psi(U)`.

Finally set

`Q_beta = C_beta P_G = P_G C_beta`,

`T_beta = M_beta Q_beta M_beta`.

Because `M_beta` is gauge invariant, it commutes with `P_G`; hence `T_beta`
restricts to `H_G` and vanishes on its orthogonal complement.

## Theorem 1: nonnegative Wilson character coefficients

For every `beta >= 0`, the character expansion

`w_beta(g) = sum_lambda c_lambda(beta) chi_lambda(g)`

has

`c_lambda(beta) >= 0`

for every irreducible representation `lambda` of `SU(3)`.

### Proof

Write `t = beta/6` and `R = 3 direct_sum 3bar`. Then

`w_beta(g)
 = exp[t (chi_3(g) + chi_3bar(g))]
 = sum_(n>=0) t^n/n! chi_(R^(tensor n))(g)`.

For each `n`,

`chi_(R^(tensor n))
 = sum_lambda m_(lambda,n) chi_lambda`

with the tensor-product multiplicities
`m_(lambda,n)` nonnegative integers. Since `|chi_R(g)| <= dim(R) = 6`,
the exponential series is uniformly absolutely convergent, so it may be
projected term by term onto any character. Therefore

`c_lambda(beta)
 = sum_(n>=0) t^n/n! m_(lambda,n) >= 0`.

Moreover,

`sum_lambda d_lambda c_lambda(beta)
 = sum_(n>=0) t^n/n! dim(R)^n
 = exp(beta)`.

Thus the character expansion is absolutely and uniformly controlled by its
value at the identity.

This proves nonnegativity. Strict positivity of every coefficient is not
needed and is not asserted.

There is also a direct finite-Gram check of the same sign. For any points
`g_1,...,g_N`, the matrix

`K_(i,j) = chi_R(g_i g_j^(-1))`

is a Gram matrix of representation matrix entries and is positive
semidefinite. Every entrywise power `K^(circle n)` is positive semidefinite by
the Schur product identity. Therefore

`[w_beta(g_i g_j^(-1))]_(i,j)
 = sum_(n>=0) t^n/n! K^(circle n) >= 0`.

This is an equivalent positive-type proof and does not use pointwise
positivity as a substitute for quadratic-form positivity.

## Theorem 2: exact positive finite-volume transfer operator

For `beta >= 0`, `T_beta` is positive, self-adjoint, and trace class. Its
kernel is exactly the temporal-gauge one-step Wilson kernel with half of the
spatial action on each boundary slice.

### Proof

For a unitary matrix realization `D^lambda`, Schur orthogonality gives

`integral dU chi_mu(U' U^(-1)) D^lambda_(i,j)(U)
 = sum_(a,b) D^mu_(a,b)(U')
   integral dU conjugate(D^mu_(a,b)(U)) D^lambda_(i,j)(U)
 = delta_(mu,lambda) D^lambda_(i,j)(U') / d_lambda`.

Inserting the character expansion of `w_beta` shows that convolution acts on
the `lambda` matrix-element sector with scalar

`c_lambda(beta) / d_lambda`.

Theorem 1 makes every such scalar nonnegative, so each `C_(e,beta)` and their
finite tensor product `C_beta` are positive semidefinite.

For a simultaneous gauge transformation of both arguments, each link
difference changes by conjugation at its source:

`(h . U')_e (h . U)_e^(-1)
 = h_(s(e)) U'_e U_e^(-1) h_(s(e))^(-1)`.

Centrality of `w_beta` therefore makes the kernel of `C_beta` invariant, so
`C_beta` commutes with `P_G`. The product of the commuting positive operator
`C_beta` and orthogonal projector `P_G` is therefore positive:

`Q_beta = C_beta P_G = P_G C_beta >= 0`.

Consequently

`T_beta
 = M_beta Q_beta M_beta
 = (Q_beta^(1/2) M_beta)^* (Q_beta^(1/2) M_beta) >= 0`.

Self-adjointness follows from the same factorization. For one link,

`Tr(C_(e,beta)) = sum_lambda d_lambda c_lambda(beta) = exp(beta)`.

Thus `C_beta` is positive trace class at finite `|E|`; multiplication by the
bounded `M_beta` and insertion of `P_G` preserve trace class.

It remains to identify the kernel. Acting on `psi` and writing the intermediate
spatial configuration as `X`,

`(C_beta P_G psi)(U')
 = integral dX product_e w_beta(U'_e X_e^(-1))
   integral dh psi(h^(-1) . X)`.

Set `U = h^(-1) . X`, so `X = h . U`. Since product Haar measure is gauge
invariant,

`(C_beta P_G psi)(U')
 = integral dU dh
   product_e w_beta(U'_e h_(t(e)) U_e^(-1) h_(s(e))^(-1))
   psi(U)`.

Orienting each `V_x` from the later boundary slice to the earlier boundary
slice and renaming `h_x` as `V_x` gives

`Q_beta(U',U)
 = integral product_(x in V) dV_x
   product_(e in E)
   w_beta(U'_e V_(t(e)) U_e^(-1) V_(s(e))^(-1))`.

Each factor is the Wilson weight of the mixed plaquette joining link `e` on
the two consecutive slices. Multiplication by `M_beta` on the left and right
adds half the spatial Wilson action of each boundary slice. Therefore
`T_beta(U',U)` is the exact one-step Wilson kernel.

Taking the periodic trace of `T_beta^(L_t)` integrates each spatial slice and
each intervening temporal link once. The two adjacent half weights combine
to one full spatial weight on every slice, proving

`Z_(L_s,L_t)(beta) = Tr[T_(L_s,beta)^(L_t)]`.

## Theorem 3: exact marked spatial-plaquette source algebra

Fix a spatial plaquette `p` and set

`X(W) = (1/3) Re Tr(W)
      = (chi_(1,0)(W) + chi_(0,1)(W)) / 6`.

Let `A_p` be multiplication by `X(U_p)` on `H_G`, and let `J` be
multiplication by `X(W)` on `L^2_class(SU(3), dW)`.

The map

`(I_p phi)(U) = phi(U_p)`

is an isometry from `L^2_class(SU(3))` into `H_G`, and

`A_p I_p = I_p J`.

More generally, bounded Borel functional calculus obeys

`f(A_p) I_p = I_p f(J)`.

### Proof

The plaquette holonomy transforms by conjugation at its base point, so
`I_p phi` is gauge invariant for class functions `phi`. Because `L_s >= 2`,
one may integrate one of the four plaquette links last. Haar invariance makes
`U_p` Haar distributed after the other links are fixed. Hence

`<I_p phi, I_p psi>_H
 = integral_(SU(3)) dW conjugate(phi(W)) psi(W)`.

This proves isometry. The intertwining identity is then the pointwise
identity

`X(U_p) phi(U_p) = (X phi)(U_p)`.

The standard tensor-product rules give

`chi_(1,0) chi_(p,q)
 = chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)`,

`chi_(0,1) chi_(p,q)
 = chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q)`,

where negative labels are omitted. Therefore

`J chi_(p,q)
 = (1/6) [ chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
         + chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q) ]`.

Since `X` is real and takes values in `[-1/2,1]`, `J` is bounded
self-adjoint with spectrum in that interval.

## Corollary 1: positive transfer state for one marked spatial plaquette

For `Z = Tr(T_beta^(L_t)) > 0`, define

`omega_beta(B) = Tr[T_beta^(L_t) B] / Z`.

This is a positive normalized state. For every bounded Borel `f`,

`<f(X_p)>_(beta,L_s,L_t)
 = omega_beta(f(A_p))
 = Tr[T_beta^(L_t) f(A_p)] / Tr[T_beta^(L_t)]`.

The multiplication representation

`Phi_p: f(J) -> f(A_p)`

is well defined: equality of two functions of `J` is Haar-almost-everywhere
equality as functions of `X(W)`, and the plaquette-Haar identity above gives
the same equality after composition with `U_p`. Pulling `omega_beta` back
through `Phi_p` gives a positive state on the commutative operator algebra
generated by the explicit recurrence operator `J`.
Equivalently, the marked spatial-plaquette law is the spectral measure of
`J` in this pulled-back state.

This statement does not require, and does not imply,

`T_beta Range(I_p) subset Range(I_p)`.

No transfer-sector eigenvalue identification is claimed.

## Corollary 2: single-slice and repeated spatial sources

A source on one marked spatial plaquette of one selected slice gives

`Z_single(h) = Tr[T_beta^(L_t) exp(h A_p)]`.

A source on the corresponding spatial plaquette on every time slice is
represented by the symmetric sandwich

`T_beta(h)
 = exp(h A_p/2) T_beta exp(h A_p/2)`.

For real `h`,

`T_beta(h) >= 0`,

and

`Z_repeated(h) = Tr[T_beta(h)^(L_t)]`

is exactly the repeated-source Wilson path integral. Positivity follows from

`T_beta(h)
 = (Q_beta^(1/2) M_beta exp(h A_p/2))^*
   (Q_beta^(1/2) M_beta exp(h A_p/2))`,

using the commutativity of the multiplication operators `M_beta` and
`exp(h A_p/2)`.

In the periodic kernel product, the two adjacent source half weights at every
slice multiply to `exp(h X(U_p))`, which proves the repeated-source identity
without a transfer-invariant source-sector assumption.

## Scope boundary for temporal plaquettes

The multiplication formulas above apply to spatial plaquettes lying inside a
single time slice. A mixed temporal plaquette depends on two spatial slices
and the intervening temporal link. Marking it changes one factor in the
kernel of `Q_beta`; it is not, without an additional construction, a
one-slice multiplication insertion.

This note does not supply such a temporal-source construction.

## What this closes

- a self-contained positive-type proof for the one-link `SU(3)` Wilson weight
  at `beta >= 0`
- an exact positive-semidefinite finite-volume transfer operator, not merely
  a pointwise positive symmetric kernel
- the finite Wilson transfer-trace identity on the gauge-invariant spatial
  Hilbert space
- the exact marked spatial-plaquette multiplication formula in the positive
  transfer state
- the exact local `SU(3)` six-neighbor character recurrence and its
  multiplication-algebra intertwiner
- positive symmetric-sandwich transfer operators for repeated real spatial
  sources

## What this does not close

- a one-slice multiplication representation for a mixed temporal plaquette
- transfer invariance of the local plaquette class-function subspace
- equality between recurrence eigenvalues and full-transfer eigenvalues
- explicit transfer-state identification at `beta = 6` still open
- explicit Perron or thermal data at `beta = 6`
- analytic closure of canonical `P(6)`
- repo-wide authority or status repinning

## Verification

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py
```

The runner independently checks:

- exact low-order representation-ring multiplicities for
  `(3 direct_sum 3bar)^(tensor n)`
- sampled positive-type Gram matrices of the `SU(3)` Wilson class function
- the six-neighbor `SU(3)` character recurrence
- an exhaustive finite nonabelian model of convolution, gauge projection,
  Gram factorization, transfer trace, marked insertion, and repeated symmetric
  source
- a negative control showing that pointwise positivity plus symmetry alone
  does not imply positive-semidefinite quadratic-form positivity

Expected summary:

- `THEOREM PASS=6 SUPPORT=10 FAIL=0`
