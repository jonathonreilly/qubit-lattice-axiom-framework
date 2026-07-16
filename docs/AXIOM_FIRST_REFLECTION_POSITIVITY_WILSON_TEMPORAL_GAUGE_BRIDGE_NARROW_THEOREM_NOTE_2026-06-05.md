# Reflection positivity — finite-volume `SU(N)` Wilson temporal-gauge bridge by a direct representation-ring proof

**Date:** 2026-06-05
**Repaired:** 2026-07-16
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** proposed_retained
**Status authority:** independent audit lane only. This source note does not set,
apply, or predict an audit outcome. The labels above declare the proposed
source-side theorem boundary, not an effective repository status.
**Primary runner:**
[`scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py`](../scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py)
**Cached output:**
[`logs/runner-cache/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.txt`](../logs/runner-cache/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.txt)

## 0. Exact bounded claim

Consider the pure-gauge Wilson plaquette weight on one finite open temporal
slab with boundary slices `t ∈ {0,1}`, no periodic temporal identification,
finitely many spatial links, temporal-gauge data `U_0 = 1`, normalized product
Haar measure, and link reflection `θ:t ↦ 1-t`. The temporal gauge condition is part of this
explicit carrier definition; no global gauge-fixing theorem is used. On
plus-slice observables,

```text
Θ(F)(U) = overline(F(θU)).
```

Write the nonconstant Wilson Boltzmann exponent as

```text
B = B_+ + B_- + B_0,       B_- = Θ B_+,
S_W = -B + constant.
```

For the fundamental representation of `SU(N)`, `N ≥ 2`, and Wilson coupling
`β ≥ 0`, the straddling-link factor is

```text
k_beta(U,V)
  = exp[(β/N) Re Tr(U V^dagger)]
  = exp[(β/(2N))(χ_F(UV^dagger) + χ_Fbar(UV^dagger))].
```

The following finite-volume statements hold.

1. **Reflection split.** `B_0` is real and invariant under exchange of the two
   slices, while `B_- = ΘB_+`. The sign is the Boltzmann sign above:
   `exp(-S_W)` is proportional to `exp(B)`.
2. **Exact `SU(N)` character-coefficient positivity.** The character
   coefficients of `k_beta` are nonnegative. This follows directly from tensor
   powers of `F ⊕ Fbar`; no literature theorem and no sampled group integral is
   load-bearing.
3. **Positive plane kernel.** The resulting plane positive kernel has the
   following exact meaning: for every finite family `{U_i} ⊂ SU(N)`, the
   matrix `[k_beta(U_i,U_j)]` is positive semidefinite. Products of these
   kernels over finitely many spatial links are positive semidefinite.
4. **Integrated reflected Gram.** For every finite family of bounded measurable
   plus-slice observables `{F_i}`, including the named `A_+^(2)` algebra, the
   normalized two-slice pure-gauge form

   ```text
   G_ij = Z^(-1) ∫ exp(B) overline(F_i(c_0)) F_j(c_1) dc_0 dc_1
   ```

   is positive semidefinite.

Thus the Wilson-plane gauge-half norm-square bridge is proved directly for the
fundamental `SU(N)` Wilson weight on this finite two-slice carrier. The theorem
is stronger than the old `A_+^(2)`-only formulation in observable algebra, but
it remains deliberately bounded in time extent, volume, and sector.

## 1. Reflection split and sign

The dynamical variables are the spatial links `U_k(t)`, with
`k=1,...,L_s` and `t∈{0,1}`, on the open temporal slab just specified. The
symbol `B_+` denotes the bounded real sum of purely spatial Wilson plaquette
terms on the plus slice when the spatial lattice has such plaquettes. On the
runner's exact one-spatial-dimensional carrier there are no purely spatial
plaquettes, so `B_+=B_-=0`.

The plus-slice Wilson exponent `B_+(c_1)` is real and depends only on the
`t=1` links. Its reflected copy is

```text
B_-(c_0) = B_+(c_0) = (ΘB_+)(c_0).
```

A straddling temporal plaquette reduces to

```text
B_0(c_0,c_1)
  = (β/N) sum_k Re Tr[U_k(0) U_k(1)^dagger].
```

Since

```text
Tr[U_k(1)U_k(0)^dagger]
  = overline(Tr[U_k(0)U_k(1)^dagger]),
```

`B_0(c_0,c_1)=B_0(c_1,c_0)` and is real. The conventional Wilson action is
`S_W=-B+constant`, so the plane factor in the measure is `exp(B_0)`, not
`exp(-B_0)`. The runner checks the nontrivial sign and plane symmetry
symbolically and on finite `Z_N` carriers; its `1+1`-dimensional half exponent
vanishes exactly.

## 2. Direct representation-ring proof

The proof uses the following self-contained compact-group lemma.

> **Lemma.** Let `R` be a finite-dimensional unitary representation of a
> compact group `G`, and let `α ≥ 0`. Then
>
> ```text
> exp[α Re χ_R(g)] = sum_λ c_λ(α) χ_λ(g),
> c_λ(α) = sum_(n≥0) (α/2)^n/n! M_(λ,n) ≥ 0,
> ```
>
> where `M_(λ,n)` is the multiplicity of the irrep `λ` in
> `(R ⊕ Rbar)^tensor n`.

Unitarity gives

```text
Re χ_R = (χ_R + χ_Rbar)/2 = χ_(R ⊕ Rbar)/2.
```

The exponential series and multiplicativity of characters give

```text
exp[α Re χ_R]
  = sum_(n≥0) (α/2)^n/n! χ_((R ⊕ Rbar)^tensor n)
  = sum_(n≥0) (α/2)^n/n! sum_λ M_(λ,n) χ_λ.
```

Every tensor-product multiplicity `M_(λ,n)` is a nonnegative integer.
Self-contained complete reducibility follows because an invariant subspace of
a finite-dimensional unitary representation has an invariant orthogonal
complement. The
exchange of the `n` and `λ` sums is justified without importing an external
positivity theorem: if `d_R=dim R`, then

```text
sum_λ M_(λ,n) |χ_λ(g)|
  ≤ sum_λ M_(λ,n) dim(λ)
  = (2 d_R)^n.
```

After multiplication by `(α/2)^n/n!`, the uniform majorant sums to
`exp(α d_R)`. Hence the character series is uniformly absolutely convergent and
its coefficients are exactly the displayed nonnegative sums.

Apply the lemma to `G=SU(N)`, `R=F`, and `α=β/N`. This proves the Wilson-plane
coefficient signs for every `N≥2` and `β≥0`.

This is a **nonnegativity** theorem. It does not assert that every irrep occurs
or that every coefficient is strictly positive. Coefficients of irreps absent
from all relevant tensor powers remain zero.

## 3. Positive kernel and the integrated Gram

There is also a direct finite-Gram proof, independent of the irrep
decomposition. For any finite family `{U_i}`, the real matrix

```text
H_ij = Re Tr(U_i U_j^dagger)
```

is a Gram matrix for the matrices `U_i` viewed as vectors in the real inner
product `Re Tr(A B^dagger)`. Hence `H⪰0`. Every Hadamard power `H^(circ n)` is
positive semidefinite by repeated Schur products, and therefore

```text
[exp(α H_ij)] = sum_(n≥0) α^n/n! H^(circ n) ⪰ 0
```

for `α≥0`. This proves the Wilson kernel's positive type without character
theory and independently checks the sign-sensitive conclusion of §2.

The character route additionally identifies the coefficient signs. For an
irreducible unitary representation `λ`,

```text
χ_λ(UV^dagger)
  = sum_(a,b) D^λ_ab(U) overline(D^λ_ab(V)).
```

Therefore every finite restriction of this character kernel is a Gram matrix.
The uniformly convergent nonnegative character sum from §2 gives

```text
k_beta(U,V)
  = sum_(λ,a,b) c_λ(β/N)
      D^λ_ab(U) overline(D^λ_ab(V)),
```

so `k_beta` is a positive-semidefinite kernel. For `L_s` spatial links, the plane
kernel is

```text
K_L(c_0,c_1) = product_(k=1)^L_s k_beta(U_k(0),U_k(1)).
```

It is positive semidefinite either by tensoring the displayed feature maps or
by the Schur product theorem on each finite restriction.

Let

```text
H_i(c) = exp(B_+(c)) F_i(c).
```

Using `B_-=ΘB_+` and the antilinear reflection,

```text
G_ij
  = Z^(-1) ∫ overline(H_i(c_0)) K_L(c_0,c_1) H_j(c_1) dc_0 dc_1.
```

Insert the positive feature expansion
`K_L(c_0,c_1)=sum_A κ_A Φ_A(c_0) overline(Φ_A(c_1))`, `κ_A≥0`, and define

```text
W_i(A) = ∫ overline(H_i(c)) Φ_A(c) dc.
```

Then

```text
G_ij = Z^(-1) sum_A κ_A W_i(A) overline(W_j(A)),
G = Z^(-1) W diag(κ) W^dagger ⪰ 0.
```

For each irrep, Cauchy-Schwarz and unitarity give

```text
sum_(a,b) |D^λ_ab(U) overline(D^λ_ab(V))| ≤ d_λ.
```

Consequently,

```text
sum_(λ,a,b) c_λ
  |D^λ_ab(U) overline(D^λ_ab(V))|
  ≤ sum_λ c_λ d_λ
  = exp(α d_R).
```

This uniform absolute bound, its finite product over links, and the boundedness
of the `H_i` justify the feature expansion and termwise Haar integration by
dominated convergence.

On the compact finite-link configuration space, the Wilson half-weight and
every bounded `F_i` are integrable. The pointwise Boltzmann weight is strictly
positive, so `0<Z<∞`. Normalization preserves positive semidefiniteness.

The `A_+^(2)` plaquette and degree-at-most-two observables are bounded continuous
functions and therefore lie inside this proved observable algebra.

## 4. Independent proof frames and controls

The repair was tested against several logically distinct frames.

| frame | role | outcome |
|---|---|---|
| representation ring | Computes the character coefficients as tensor-power multiplicities. | Exact proof; adopted. |
| finite Gram / matrix coefficients | Proves kernel positivity directly from representation matrix entries. | Exact proof; agrees with the coefficient route. |
| integrated feature factorization | Converts the multi-link plane kernel and half-weights into `W diag(κ) W^dagger`. | Exact proof for bounded observables. |
| `Z_N` and `U(1)` reductions | Checks the construction against discrete Fourier and positive Bessel-series coefficients. | Exact or interval-certified checks. |
| `SU(3)` fusion recurrence | Builds `(3 ⊕ 3bar)^tensor n` through order eight and checks `sum M dim=6^n`. | Exact runner gate. |
| wrong-sign / wrong-reflection controls | Tests whether the sign and antilinearity are load-bearing. | Negative coupling or dropped conjugation produces a non-PSD control. |

These frames address the earlier weak routes:

- pointwise positivity of `k_beta` alone would not imply operator/kernel
  positivity;
- Peter-Weyl alone would give an expansion but not coefficient signs;
- a Monte Carlo `SU(2)` or `SU(3)` sample would be support, not a proof;
- a literature comparator would not be a self-contained derivation.

The representation-ring expansion closes the missing sign step directly.

## 5. Runner contract

Run:

```bash
python3 scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py
```

The runner checks:

- the reflection split and Wilson sign;
- the normalization map `alpha=beta/N`; legacy abelian and `SU(2)` diagnostic
  function arguments named `beta` are explicitly identified as the effective
  plane coupling `alpha`;
- exact finite `Z_N` coefficient reconstruction and reflected Grams;
- positive-series interval certificates for the `U(1)` coefficients;
- the manifest finite-carrier factorization `G=W diag(κ)W^dagger`;
- a sampled `SU(2)` reflected Gram, labeled numerical support;
- exact `SU(3)` fusion multiplicities, the dimension identity `6^n`, and
  nonnegative truncated coefficient sums;
- deterministic positive- and negative-coupling `SU(3)` kernel controls.

The runner prints `TOTAL: <N> PASS / <M> FAIL` and exits nonzero exactly when
`M>0`.

## 6. What this note does not claim

This theorem does not:

- add the fermion determinant or fermion-sector two-step transfer factor;
- prove reflection positivity on an arbitrary multi-slice lattice;
- construct a transfer matrix or Hamiltonian;
- prove a continuum, thermodynamic, or Osterwalder-Schrader reconstruction
  limit;
- prove a global temporal-gauge fixing theorem;
- assert positivity for negative Wilson coupling;
- assert strict positivity of every character coefficient;
- update the status of the axiom-first reflection-positivity row or any
  dependency;
- rely on a fitted, observed, `β=6`, `g_bare`, or lattice-Monte-Carlo value.

The exact result is the finite-volume, two-slice, pure-gauge Wilson plane and its
integrated bounded-observable reflected Gram.

## 7. Source boundary and non-load-bearing context

The proof above is self-contained and has no load-bearing repository
dependency. The abstract gauge-half structure in
`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`
and the fermion-sector separation in
`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md` are
historical context only, not premises of this theorem.

The determinant and fermion-transfer notes remain separate factors and are not
used in the pure-gauge proof. The later `SU(3)` plane-kernel note is
corroborating downstream work, not a dependency of this repaired source, so
the argument here is non-circular.

No external literature theorem is load-bearing. The proof uses only
finite-dimensional unitary representation identities, tensor-product
multiplicities, normalized Haar measure, and elementary absolute convergence.

**No-promotion statement:** this edit proposes a repaired bounded theorem for
independent review. It neither writes an audit verdict nor changes any durable
audit, ledger, queue, or effective-status surface.
