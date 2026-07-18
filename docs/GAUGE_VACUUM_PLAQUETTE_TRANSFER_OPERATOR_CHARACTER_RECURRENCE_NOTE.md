# Gauge-Vacuum Wilson Transfer / Character-Recurrence Theorem

**Date:** 2026-07-16
**Type:** positive_theorem
**Claim boundary:** exact finite-volume pure-gauge `SU(N)` Wilson transfer
construction for `N >= 2`, `beta >= 0`, a finite open or periodic spatial
carrier, and periodic derived time; exact spatial-plaquette multiplication
insertions; exact mixed-plaquette two-slice source kernels; and the `SU(3)`
six-neighbor character recurrence.
**Status authority:** independent audit lane only. This source note does not
set, apply, or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py`](../scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py)
**Runner cache:**
[`logs/runner-cache/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.txt)

## Question

Can the Wilson one-step object be proved positive in the quadratic-form sense,
can spatial and mixed marked plaquettes be inserted with the correct
one-slice/two-slice grammar, and can the `SU(3)` spatial plaquette observable be
related exactly to the six-neighbor character recurrence without identifying
the full gauge Hilbert space with a one-plaquette class-function space?

## Answer

Yes.

The load-bearing sign input is proved self-containedly in Section 2:

```text
w_beta(g) = exp[(beta/N) Re Tr_F(g)]
```

has nonnegative character coefficients and is a positive-type class function
for `SU(N)`, `N >= 2`, `beta >= 0`. The earlier open-slab note
`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
gives a non-load-bearing independent check on an explicit finite open
temporal-gauge slab. It does not construct the periodic transfer operator,
gauge projector, or marked plaquette insertions proved here.

This note performs those additional steps. On the finite spatial gauge Hilbert
space it defines

```text
Q_beta = C_beta P_G = P_G C_beta,
T_beta = M_beta Q_beta M_beta,
```

and proves

```text
T_beta
 = (Q_beta^(1/2) M_beta)^* (Q_beta^(1/2) M_beta) >= 0.
```

The physical carrier is the gauge-invariant spatial Hilbert space `H_G`.
On the periodic cubic carrier, this is the positive self-adjoint transfer operator `T_(L_s,beta)`
used by downstream finite-volume notes.

With the downstream reduced-partition shorthand
`Z_(L_s,L_t)(beta) := Z_+(beta)`, the exact one-clock law is
`Z_(L_s,L_t)(beta) = Tr[T_(L_s,beta)^(L_t)]`. The canonical Wilson partition
retains the scalar normalization stated in Section 1.

For periodic derived time,

```text
Z_+(beta) = Tr[T_beta^L_t]
```

is the reduced Wilson partition function with all field-independent
`exp(-beta)` plaquette factors removed.

A spatial plaquette on a boundary slice is multiplication by

```text
A_p(U) = X(U_p),                 X(g) = (1/N) Re Tr_F(g).
```

A mixed plaquette is marked by changing one factor in the two-slice kernel.
Its source derivatives have the positive-type Schur-power form

```text
H^(circle m) circle exp(gamma H),        gamma >= 0.
```

For `SU(3)`,

```text
X(W) = (chi_(1,0)(W) + chi_(0,1)(W)) / 6,
```

and multiplication by `X` obeys the exact six-neighbor recurrence. The
plaquette-holonomy pullback is an isometry and intertwines this local
class-function operator with `A_p`; it is not an identification of the full
gauge-invariant Hilbert space with the one-plaquette class-function space.

Equivalently, in the literal downstream notation,
`X = (chi_(1,0) + chi_(0,1)) / 6` and `X(W) = (1/3) Re Tr W`.

## 1. Finite carrier and normalization

Let the spatial carrier be a finite connected oriented lattice cell complex
`Lambda` with:

- vertices `V`;
- one positively stored orientation for every spatial link, collected in `E`;
- elementary spatial plaquettes `P_s`.

The spatial carrier may be a finite open box or a finite periodic lattice.
For the marked-plaquette pullback below, the marked plaquette is assumed
simple: one may choose a boundary link that occurs exactly once in its
oriented boundary word. The periodic cubic `L_s^3` carrier with `L_s >= 2`
satisfies this condition.

Let

```text
H = L^2(SU(N)^E, dU),
```

with normalized product Haar measure. For `h = (h_x)_(x in V)`, define

```text
(h . U)_e = h_(s(e)) U_e h_(t(e))^(-1),
(Gamma_h psi)(U) = psi(h^(-1) . U),
P_G = integral dh Gamma_h.
```

Then `P_G` is the orthogonal projector onto the gauge-invariant spatial
Hilbert space `H_G`.

Write

```text
X(g) = (1/N) Re Tr_F(g),
w_beta(g) = exp[beta X(g)].
```

The canonical Wilson action is

```text
S_W[U; beta] = beta sum_P (1 - X(U_P)).
```

One time step contains:

- `|P_s|` spatial plaquettes;
- `|E|` mixed plaquettes, one for every spatial link.

Thus

```text
N_step = |P_s| + |E|,
N_P = L_t N_step
```

on a periodic `L_t`-step lattice. Define the reduced partition function

```text
Z_+(beta) = exp(beta N_P) Z_W(beta).
```

The field-independent scalar is restored at the operator level by

```text
T_beta^W = exp(-beta N_step) T_beta,
Z_W(beta) = Tr[(T_beta^W)^L_t].
```

For the periodic cubic carrier,

```text
|P_s| = |E| = 3 L_s^3,
N_step = 6 L_s^3.
```

The scalar rescaling preserves positivity and cancels from normalized
expectations.

## 2. Exact Wilson positive-type input

For `SU(N)`, `N >= 2`, `beta >= 0`, the required character expansion is

```text
w_beta(g) = sum_lambda a_lambda(beta) chi_lambda(g),
a_lambda(beta) >= 0.
```

Its self-contained representation-ring proof is short. With `F` the
fundamental representation,

```text
w_beta(g)
 = exp[(beta/(2N))(chi_F(g) + chi_Fbar(g))]
 = sum_(n>=0) (beta/(2N))^n / n!
     chi_((F direct_sum Fbar)^(tensor n))(g).
```

Every irreducible coefficient is a sum of nonnegative tensor-product
multiplicities. The series is uniformly absolutely convergent because the
dimension sum at order `n` is `(2N)^n`.

Equivalently, for any finite family `{g_i}`, the matrix

```text
H_ij = X(g_i g_j^(-1))
```

is positive semidefinite: it is the Gram matrix of the matrices `g_i` in the
real inner product `Re Tr(A B^dagger)/N`. Therefore

```text
[w_beta(g_i g_j^(-1))]
 = exp(circle)(beta H)
 = sum_(n>=0) beta^n/n! H^(circle n) >= 0.
```

This is the exact positive-type statement used below. Pointwise positivity is
not used as a substitute for quadratic-form positivity.

For non-load-bearing comparison, the earlier open-slab note named above also
proves an integrated Gram on its finite open temporal-gauge slab carrier after
multiplying by bounded spatial half weights. The periodic trace and source
identities below are derived separately.

## 3. Positive gauge-projected transfer operator

For each spatial link, define the convolution operator

```text
(C_(e,beta) psi)(U'_e)
 = integral dU_e w_beta(U'_e U_e^(-1)) psi(U_e),
```

and set

```text
C_beta = tensor_(e in E) C_(e,beta).
```

The spatial half-weight is the bounded positive multiplication operator

```text
(M_beta psi)(U)
 = exp[(beta/2) sum_(p in P_s) X(U_p)] psi(U).
```

Finally define

```text
Q_beta = C_beta P_G,
T_beta = M_beta Q_beta M_beta.
```

### Theorem 1: `Q_beta` and `T_beta` are positive

For `N >= 2`, `beta >= 0`, both `Q_beta` and `T_beta` are positive
self-adjoint trace-class operators. They preserve `H_G`, and `T_beta`
vanishes on `H_G^perp`.

### Proof

If

```text
w_beta = sum_lambda a_lambda chi_lambda,
```

Schur orthogonality gives

```text
integral dU chi_mu(U' U^(-1)) D^lambda_(i,j)(U)
 = delta_(mu,lambda) D^lambda_(i,j)(U') / d_lambda.
```

Thus `C_(e,beta)` acts on the `lambda` matrix-element sector with eigenvalue

```text
a_lambda(beta) / d_lambda >= 0.
```

Each one-link convolution and their finite tensor product `C_beta` are
positive.

Under a simultaneous spatial gauge transformation of both kernel arguments,

```text
(h . U')_e (h . U)_e^(-1)
 = h_(s(e)) U'_e U_e^(-1) h_(s(e))^(-1).
```

Centrality of `w_beta` implies

```text
C_beta P_G = P_G C_beta.
```

The product of the commuting positive operator `C_beta` and the orthogonal
projector `P_G` is positive:

```text
Q_beta = C_beta P_G = P_G C_beta >= 0.
```

Therefore

```text
T_beta
 = M_beta Q_beta M_beta
 = (Q_beta^(1/2) M_beta)^* (Q_beta^(1/2) M_beta) >= 0.
```

For one link,

```text
Tr(C_(e,beta))
 = sum_lambda d_lambda a_lambda(beta)
 = w_beta(1)
 = exp(beta).
```

Hence `C_beta` is trace class at finite `|E|`; bounded multiplication and
orthogonal projection preserve trace class.

Because `M_beta` is gauge invariant, it commutes with `P_G`. This proves the
claimed invariant-subspace and zero-on-`H_G^perp` statements.

## 4. Kernel and periodic transfer trace

Acting on `psi`,

```text
(C_beta P_G psi)(U')
 = integral dX product_(e in E) w_beta(U'_e X_e^(-1))
   integral dh psi(h^(-1) . X).
```

Set `U = h^(-1) . X`. Product Haar invariance gives

```text
(C_beta P_G psi)(U')
 = integral dU dh
   product_(e in E)
   w_beta(U'_e h_(t(e)) U_e^(-1) h_(s(e))^(-1))
   psi(U).
```

Rename `h_x` as the temporal link `V_x` oriented from the later boundary slice
to the earlier boundary slice. Then

```text
Q_beta(U',U)
 = integral product_(x in V) dV_x
   product_(e in E)
   w_beta(U'_e V_(t(e)) U_e^(-1) V_(s(e))^(-1)).
```

Each factor is the reduced Wilson weight of the mixed plaquette associated
with spatial link `e`. Left and right multiplication by `M_beta` supplies half
of every spatial plaquette weight on each boundary slice.

### Theorem 2: periodic trace identity

For periodic derived time of length `L_t >= 1`,

```text
Z_+(beta) = Tr[T_beta^L_t].
```

### Proof

Expand the trace as the cyclic integral over spatial configurations
`U_0,...,U_(L_t-1)`. Each one-step kernel supplies:

- all `|E|` mixed plaquette factors between `U_t` and `U_(t+1)`;
- half the spatial plaquette weight on `U_t`;
- half the spatial plaquette weight on `U_(t+1)`.

The two adjacent half weights multiply to one full spatial weight on every
slice. Every spatial configuration and every intervening temporal link is
integrated once with normalized Haar measure. The result is exactly the
reduced periodic Wilson path integral.

Restoring the `exp(-beta)` factor for each of the `N_P` plaquettes gives the
canonical `Z_W` formula in Section 1.

This is the periodic theorem. The cited reflection-positivity note proves the
corresponding open one-step slab Gram, not this cyclic trace identity.

## 5. Marked spatial plaquette

Fix a simple spatial plaquette `p in P_s`. Let

```text
(A_p psi)(U) = X(U_p) psi(U)
```

on `H_G`.

### Theorem 3: selected-slice multiplication insertion

If a source `h` is placed on plaquette `p` on one selected boundary slice,

```text
Z_spatial,selected(h)
 = Tr[T_beta^L_t exp(h A_p)].
```

Consequently,

```text
<X(U_p)^m>
 = Tr[T_beta^L_t A_p^m] / Tr[T_beta^L_t].
```

### Proof and slice convention

In the cyclic kernel product, choose the selected slice to be `U_0`. The
source multiplies the path weight by

```text
exp[h X((U_0)_p)].
```

That is exactly the diagonal multiplication operator `exp(h A_p)` inserted at
the `U_0` integration. Cyclicity of the trace makes the numerical answer
independent of the label assigned to the selected slice.

The convention is one full selected-slice factor. It is not:

- one half source placed on only one adjacent transfer;
- one full source placed on both adjacent transfers;
- a source repeated on every slice.

Those are different path integrals.

### Corollary 1: repeated spatial source and positivity

If the same spatial plaquette is sourced on every time slice, define

```text
T_spatial(h)
 = exp(h A_p/2) T_beta exp(h A_p/2).
```

Then

```text
Z_spatial,repeated(h)
 = Tr[T_spatial(h)^L_t].
```

For every real `h`,

```text
T_spatial(h) >= 0.
```

Indeed, `exp(h A_p/2)` is a bounded positive multiplication operator and

```text
T_spatial(h)
 = (Q_beta^(1/2) M_beta exp(h A_p/2))^*
   (Q_beta^(1/2) M_beta exp(h A_p/2)).
```

In the periodic product, the two adjacent source half factors combine to
`exp[h X(U_p)]` once on every slice.

The canonical Wilson scalar remains `exp(-beta N_P)`: the marked observable
source changes the `X` factor, not the field-independent Wilson constant.

## 6. Exact `SU(3)` relation to the recurrence operator

Now specialize only this section to `SU(3)`. For one plaquette holonomy `W`,

```text
X(W)
 = (1/3) Re Tr W
 = (chi_(1,0)(W) + chi_(0,1)(W)) / 6.
```

Let `J` be multiplication by `X(W)` on
`L^2_class(SU(3), dW)`.

Define the plaquette-holonomy pullback

```text
(I_p phi)(U) = phi(U_p).
```

### Theorem 4: isometric pullback and intertwiner

`I_p` is an isometry from `L^2_class(SU(3))` into `H_G`, and

```text
A_p I_p = I_p J.
```

For every bounded Borel `f`,

```text
f(A_p) I_p = I_p f(J).
```

### Proof

The plaquette holonomy transforms by conjugation at its base point, so the
pullback of a class function is gauge invariant.

Choose a boundary link of the simple plaquette that occurs exactly once.
After all other link variables are fixed, normalized Haar invariance makes the
plaquette holonomy Haar distributed when that last link is integrated.
Therefore

```text
<I_p phi, I_p psi>_H
 = integral_(SU(3)) dW conjugate(phi(W)) psi(W).
```

The intertwining identity is the pointwise equality

```text
X(U_p) phi(U_p) = (X phi)(U_p).
```

### Exact `SU(3)` dominant-weight recurrence

The `SU(3)` tensor-product rules are

```text
chi_(1,0) chi_(p,q)
 = chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1),

chi_(0,1) chi_(p,q)
 = chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q),
```

with every negative label omitted. Hence

```text
J chi_(p,q)
 = (1/6) [
     chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
   + chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q)
   ].
```

Since `X` is real and takes values in `[-1/2,1]`, `J` is bounded
self-adjoint with spectrum in that interval.

### Scope firewall

The exact relationship is the isometric intertwiner

```text
L^2_class(SU(3)) --I_p--> H_G.
```

It is not an identification

```text
H_G = L^2_class(SU(3)).
```

This theorem does not assert

```text
T_beta Range(I_p) subset Range(I_p),
```

does not equate eigenvalues of `J` with eigenvalues of `T_beta`, and does not
identify a source-sector compression with the full transfer operator.

Define the plaquette-algebra pullback of the positive transfer state by

```text
omega_beta,L_t^(p)(f(J))
 = Tr[T_beta^L_t f(A_p)] / Tr[T_beta^L_t].
```

This is the pullback along the multiplication-algebra map
`f(J) -> f(A_p)`, not a vector state of `psi` in
`L^2_class(SU(3))` and not a transfer-invariant-subspace theorem.

## 7. Marked mixed plaquette as a two-slice source

Fix one spatial link `e` and one selected time step. Its mixed plaquette
holonomy is

```text
W_e(U',U,V)
 = U'_e V_(t(e)) U_e^(-1) V_(s(e))^(-1).
```

A source `h` for that one mixed plaquette replaces one factor

```text
w_beta(W_e)
```

by

```text
w_beta(W_e) exp[h X(W_e)]
 = exp[(beta+h) X(W_e)].
```

The field-independent canonical Wilson scalar remains the one fixed by
`beta`; this is an observable source, not a replacement of the whole Wilson
coupling.

Let `C_(e,beta+h)` be the one-link convolution with this modified factor,
while every other spatial link keeps `C_(f,beta)`. Define

```text
C_beta,e(h)
 = C_(e,beta+h) tensor_(f != e) C_(f,beta),

Q_beta,e(h) = C_beta,e(h) P_G,

T_beta,e(h) = M_beta Q_beta,e(h) M_beta.
```

### Theorem 5: mixed-source transfer formula

If

```text
gamma = beta + h >= 0,
```

then

```text
T_beta,e(h) >= 0.
```

For one selected mixed plaquette on one selected step,

```text
Z_mixed,selected(h)
 = Tr[T_beta^(L_t-1) T_beta,e(h)].
```

For the corresponding mixed plaquette sourced on every step,

```text
Z_mixed,repeated(h)
 = Tr[T_beta,e(h)^L_t].
```

The ordering in the selected formula records which one of the cyclic
two-slice kernels is modified. Cyclicity permits a relabeling of the selected
step.

### Proof of positivity

The Section 2 positive-type proof applies to the marked link with effective
coupling `gamma >= 0`. All unmarked link convolutions remain positive at
`beta >= 0`. Their tensor product commutes with `P_G`, so

```text
Q_beta,e(h) >= 0,
T_beta,e(h)
 = (Q_beta,e(h)^(1/2) M_beta)^*
   (Q_beta,e(h)^(1/2) M_beta) >= 0.
```

The marked one-link convolution is positive trace class. The same
Peter-Weyl diagonal argument as in Section 3 gives

```text
Tr(C_(e,gamma)) = w_gamma(1) = exp(gamma).
```

The finite tensor product, gauge projection, and bounded spatial sandwiches
therefore make `T_beta,e(h)` trace class.

The trace formulas follow by expanding the cyclic kernel product: exactly one
mixed plaquette factor is modified in the selected formula, while one factor
per time step is modified in the repeated formula.

### Theorem 6: Schur-power source derivatives

For every integer `m >= 0` and every `gamma = beta+h >= 0`, define the
one-link source-derivative kernel

```text
k_gamma^[m](g',g)
 = partial_gamma^m w_gamma(g' g^(-1))
 = X(g' g^(-1))^m exp[gamma X(g' g^(-1))]
```

Then `k_gamma^[m]` is positive type.

### Proof

For any finite family `{g_i}`, set

```text
H_ij = X(g_i g_j^(-1)).
```

As in Section 2, `H >= 0`. The finite restriction of the derivative kernel is

```text
[k_gamma^[m](g_i,g_j)]
 = H^(circle m) circle exp(circle)(gamma H).
```

Here `H^(circle 0)` means the all-ones matrix. Repeated Schur products give

```text
H^(circle m) >= 0.
```

The positive-type Wilson theorem gives

```text
exp(circle)(gamma H) >= 0.
```

Their Schur product is positive semidefinite. Since this holds for every finite
family, the derivative kernel is positive type.

The kernel is central. Hence its convolution commutes with `P_G`. It is also
positive trace class; since `X(1) = 1`, the Peter-Weyl trace is

```text
Tr(C_(e,gamma)^[m]) = k_gamma^[m](1,1) = exp(gamma).
```

Let

```text
C_(e,gamma)^[m]
 = partial_gamma^m C_(e,gamma)
```

denote this convolution operator and define

```text
D_beta,e,m(h)
 = M_beta [
     C_(e,gamma)^[m]
     tensor_(f != e) C_(f,beta)
     P_G
   ] M_beta.
```

Then

```text
D_beta,e,m(h)
 = partial_h^m T_beta,e(h) >= 0,
```

and `D_beta,e,m(h)` is trace class. Because `X` is bounded and the finite
carrier is compact, dominated
convergence justifies differentiating the kernel/path integral and passing
`partial_h^m` through the selected trace:

```text
partial_h^m Z_mixed,selected(h)
 = Tr[T_beta^(L_t-1) D_beta,e,m(h)].
```

At `h=0`, the moment of one selected mixed plaquette is

```text
<X(W_e)^m>
 = Tr[T_beta^(L_t-1) D_beta,e,m(0)]
   / Tr[T_beta^L_t].
```

This is the genuine mixed-plaquette insertion formula.

### Established mixed insertion

For the selected mixed plaquette, the established insertion is the operator
`D_beta,e,m(h)` obtained by differentiating the marked two-slice kernel. Its
kernel contains the marked-link factor

```text
X(W_e)^m exp[gamma X(W_e)]
```

inside the temporal-link integral, with the unmarked link factors and the two
spatial half weights unchanged. The selected and repeated trace formulas above
are the insertion statements proved here.

## 8. Positive transfer state

Because every Wilson link factor and spatial half weight is strictly positive,
the one-step integral kernel is strictly positive; in particular `T_beta` is
nonzero. Since it is also positive trace class,

```text
Z_+(beta) = Tr[T_beta^L_t] > 0.
```

Therefore

```text
omega_beta,L_t(B)
 = Tr[T_beta^L_t B] / Tr[T_beta^L_t]
```

is a positive normalized state on bounded one-slice operators. Spatial
plaquette moments use `B = f(A_p)`. Mixed plaquette moments use the
selected-step two-slice insertion `D_beta,e,m(0)` displayed in Section 7.

## 9. Exact scope and exclusions

This note proves:

- exact Wilson positive transfer on a finite open or periodic spatial carrier
  with periodic derived time;
- exact gauge projection and temporal-link kernel;
- exact transfer-trace normalization in both reduced and canonical Wilson
  conventions;
- exact selected and repeated spatial-plaquette source formulas;
- exact `SU(3)` plaquette-holonomy pullback and six-neighbor recurrence;
- exact selected and repeated mixed-plaquette source-kernel formulas;
- exact positive-type Schur-power formula for every repeated derivative of a
  marked mixed factor at nonnegative effective coupling.

This note does not prove:

- transfer invariance of the plaquette-holonomy pullback range;
- equality between recurrence eigenvalues and full-transfer eigenvalues;
- a source-sector compression or Perron eigenvalue preservation theorem;
- explicit transfer-state identification at `beta = 6` still open;
- explicit `beta = 6` Perron or thermal data;
- analytic closure of canonical `P(6)`;
- an infinite-volume, continuum, or Hamiltonian reconstruction theorem;
- repo-wide status repinning.

## 10. Verification

Run:

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_transfer_operator_character_recurrence.py
```

The runner independently checks:

- exact low-order `SU(3)` tensor multiplicities and dimension sums;
- the exact fundamental, antifundamental, and six-neighbor recurrence;
- a sampled `SU(3)` Wilson positive-type Gram, labeled support;
- a genuine finite `S_3` one-plaquette spatial lattice with four links and
  four gauge vertices;
- gauge-projected transfer positivity and Gram factorization;
- temporal-link integration versus projected convolution;
- transfer trace/path sum and selected/repeated spatial insertions;
- mixed selected-step and repeated-step sources and the
  `H^(circle m) circle exp(gamma H)` derivative form;
- dominant-weight boundary omissions in the `SU(3)` recurrence;
- hostile controls for pointwise-positive indefinite kernels, a wrong
  plaquette word, selected-versus-repeated slice placement, doubled spatial
  half weights, missing spatial half weights, missing normalized Haar factors,
  and negative effective mixed coupling.

The finite-group and sampled matrix results are support only. The exact
`SU(N)` proof is the analytic argument in this note; the earlier open-slab
theorem is non-load-bearing corroborating comparison only.

Expected summary:

```text
SUMMARY: THEOREM PASS=0 SUPPORT=21 FAIL=0
```
