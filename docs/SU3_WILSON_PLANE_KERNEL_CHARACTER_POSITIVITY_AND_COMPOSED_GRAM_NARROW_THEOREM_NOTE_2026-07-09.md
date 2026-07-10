# SU(3) Wilson plane-kernel character positivity and composed two-slice Gram — narrow theorem note

**Date:** 2026-07-09
**Type:** positive_theorem
**Primary runner:** [`scripts/su3_wilson_plane_kernel_character_positivity_composed_gram_2026_07_09.py`](../scripts/su3_wilson_plane_kernel_character_positivity_composed_gram_2026_07_09.py)
**Cached output:** [`logs/runner-cache/su3_wilson_plane_kernel_character_positivity_composed_gram_2026_07_09.txt`](../logs/runner-cache/su3_wilson_plane_kernel_character_positivity_composed_gram_2026_07_09.txt)

## 0. Statement and scope

This note proves a positive narrow theorem: the fundamental `SU(3)` Wilson
plane kernel has nonnegative character coefficients obtained directly as
tensor-power multiplicities, its associated convolution kernel is positive
semidefinite exactly when those coefficients are nonnegative, and the resulting
two-slice temporal-gauge composed form is a positive-semidefinite Gram form.

The claim is limited to the pure-gauge Wilson plane kernel for `SU(3)` with
fundamental `rho = 3`, the two-slice temporal-gauge composed form, and any finite
`L_s`; the numerics exercise `L_s = 2`. It includes no fermions and no continuum
or thermodynamic limit.

## 1. Claims

**Multiplicity-series character positivity.** Let `G` be a compact
group and `rho` a finite-dimensional unitary representation. For `beta >= 0`,

```text
k_beta(W) = exp(beta Re chi_rho(W)) = sum_lambda c_lambda(beta) chi_lambda(W),
c_lambda(beta) = sum_{n>=0} (beta/2)^n / n! M_{lambda,n},
```

where `M_{lambda,n}` is the multiplicity of `lambda` in
`(rho oplus rhobar)^{tensor n}`. Every `M_{lambda,n}` is a nonnegative integer,
so every `c_lambda(beta)` is nonnegative. For the `SU(3)` fundamental,
`k_beta(W) = exp(beta Re tr W)` is the Wilson plane-kernel factor.

**Wilson-plane supplier theorem.** For every `beta >= 0` the `SU(3)` fundamental
Wilson plane kernel `exp(beta Re tr W)` has nonnegative character coefficients
`c_lambda(beta) = sum_n (beta/2)^n / n! * M_{lambda,n}`, with `M_{lambda,n}` the
nonnegative integer multiplicity of `lambda` in `(3 ⊕ 3bar)^{⊗n}`. Hence the
reflection-plane kernel and the integrated two-slice temporal-gauge Gram on the
stated `A_+^(2)` surface are positive semidefinite at any finite `L_s`.

**Kernel criterion and integrated Gram.** Suppose the character series for
`k` is absolutely convergent. The kernel `K(U,V) = k(U V^dagger)` is positive
semidefinite if and only if every character coefficient is nonnegative. With the
multiplicity series supplying the `SU(3)` plane-kernel coefficients, the
group-independent factorization in the bridge yields the integrated two-slice
Gram positive semidefinite on its `A_+^(2)` surface for every finite spatial size
`L_s`.

**Bounded plus-slice observable extension.** In the two-slice
temporal-gauge composed form, let

```text
w = exp(B_+) exp(B_-) product_k k_beta(U_k(0) U_k(1)^dagger),
B_- = B_+ circ theta,
```

with `B_+` bounded, measurable, real, and supported on the plus slice. Then the
normalizing integral satisfies `0 < Z = integral w < infinity`. For any finite
family of bounded measurable plus-slice observables `{F_i}`, the normalized form
`G_ij = Z^(-1) integral w conj(F_i(c_0)) F_j(c_1)` is positive semidefinite. The
bridge's `A_+^(2)` surface is the stated special case.

**Exact reductions and cross-anchors.** For `U(1)` of charge one, the
multiplicity construction reduces exactly to the positive Bessel series. For
`SU(2)`, the same construction reduces on the one-variable torus to exact
integer multiplicities. These reductions independently anchor the general
series.

## 2. Proof of multiplicity-series positivity and exact reductions

Unitarity gives

```text
Re chi_rho = (chi_rho + chi_rhobar)/2
           = chi_(rho oplus rhobar)/2.
```

Expanding the exponential and using multiplicativity of characters under tensor
products gives

```text
exp(beta Re chi_rho)
  = sum_{n>=0} (beta/2)^n / n! chi_(rho oplus rhobar)^{tensor n}
  = sum_{n>=0} (beta/2)^n / n! sum_lambda M_{lambda,n} chi_lambda.
```

Finite-dimensional representation theory gives
`M_{lambda,n} in Z_{>=0}`. Moreover,
`sum_lambda M_{lambda,n} d_lambda = (2 d_rho)^n` and
`|chi_lambda| <= d_lambda`. The resulting absolute majorant is
`exp(beta d_rho)`, equal to `exp(3 beta)` for the `SU(3)` fundamental. Absolute
convergence therefore permits interchange of the two sums and proves the
multiplicity-series statement.

For `U(1)`, the multiplicity of charge `n` in `(1 oplus -1)^{tensor k}` is
`C(k,(k+n)/2)` when `k` and `n` have the same parity, and is zero otherwise.
For `n >= 0`, make the explicit substitution `k = n + 2m`:

```text
c_n(beta)
 = sum_k (beta/2)^k / k! C(k,(k+n)/2) [k = n mod 2]
 = sum_m (beta/2)^(n+2m) / (m! (n+m)!)
 = I_n(beta).
```

This is exactly the Bessel positive series certified by
`bessel_i_positive_series_interval`. Negative charges follow by conjugation.
For `SU(2)`, the same torus multiplication, Weyl density, and character inner
product produce nonnegative integer tensor-power multiplicities; no floating
proxy enters that reduction.

## 3. Proof of the kernel criterion and bounded-observable extension

For an irreducible unitary matrix representation,

```text
chi_lambda(U V^dagger)
  = sum_{a,b} D^lambda_ab(U) conj(D^lambda_ab(V)).
```

Every finite restriction of this kernel is therefore a Gram matrix. An
absolutely convergent nonnegative combination of these kernels is positive
semidefinite, proving that nonnegative coefficients imply a positive-semidefinite
kernel.

Conversely, test `K` with `f = D^mu_ab`. Schur orthogonality gives

```text
integral integral conj(f(U)) K(U,V) f(V) dU dV = c_mu / d_mu^2.
```

Positive semidefiniteness forces this quantity, and hence every `c_mu`, to be
nonnegative. This proves the converse implication.

For the bounded-observable extension, absorb `exp(B_+)` into each plus-slice
observable and absorb `exp(B_-)` symmetrically into its reflected factor. Each
link kernel is positive semidefinite by the multiplicity-series result and the
kernel criterion. A pointwise product of positive-semidefinite kernels is
positive semidefinite by the Schur product theorem on every finite restriction,
so the product over spatial links is a positive kernel on the product group. The
integrated bilinear form is consequently a Gram form for every finite family of
bounded measurable plus-slice observables. Boundedness on the compact finite-link
configuration space also gives `0 < Z < infinity`, and division by `Z` preserves
positive semidefiniteness.

The bridge's integrated factorization is group-independent once its plane-kernel
positivity input is supplied. Applying the preceding result supplies that input
for the `SU(3)` fundamental and gives its integrated two-slice Gram on the
`A_+^(2)` surface for every finite `L_s`.

## 4. Relation to the bridge note's named gap

The bridge states:

> Peter-Weyl supplies the character *expansion* of a class function, but positivity of a class function does **not** by itself imply nonnegative character coefficients on a nonabelian group (it does on abelian groups, where the irreducible characters are one-dimensional), so §3's mechanism does not carry to `SU(N≥3)` on its own.

We do not argue from positivity of `k`; we exhibit the character coefficients of the Wilson plane kernel as manifestly nonnegative combinatorial data of the exponential series itself.

Thus this note supplies natively the `SU(3)` ingredient that the bridge names as
comparator-only. Osterwalder–Seiler remains a comparator and is not used in the
derivation.

## 5. Runner contract

The runner is
`su3_wilson_plane_kernel_character_positivity_composed_gram_2026_07_09.py`.

- The exact-character checks construct `SU(3)` character and multiplicity tables,
  perform independent torus quadrature, reject a deliberately wrong kernel, and
  check the exact `U(1)` and `SU(2)` reductions.
- The representation-matrix checks cover the irreducibles appearing through
  tensor order two, including unitarity, composition, character ties, and the
  spectral kernel identity.
- The composed-form checks evaluate the actual `L_s = 2` composed integral, its
  truncated-kernel factorization, the no-conjugation control, and the exact
  zero-coupling anchor.

The runner prints a final line of the exact form `TOTAL: PASS=<N> FAIL=<M>` and
exits zero if and only if `M = 0`.

## 6. What this note does NOT claim

- no claim about the standing of `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md` or any other note;
- no full Osterwalder–Seiler reconstruction and no transfer-matrix/Hamiltonian construction here;
- no continuum or thermodynamic limit;
- no fermionic or determinant factors — pure-gauge plane kernel and composed two-slice bosonic form only;
- the theorem is stated for any finite `L_s`; the numerics exercise `L_s = 2`;
- this note by itself upgrades nothing else; how it is consumed is a matter for its consumers.

## 7. Dependencies

[AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)

Context mentions without dependency edges:
`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`,
`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`,
and `audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py`.

## 8. Source-note boundary

**Hypothesis set used:** the pure-gauge fundamental `SU(3)` Wilson plane kernel;
finite-dimensional unitary representation theory and normalized Haar measure;
the two-slice temporal-gauge link reflection with antilinear observable
reflection; and a finite spatial size `L_s`. The numerical surface fixes
`L_s = 2`; the multiplicity and kernel proofs do not.

**Source boundary:** this note introduces no new axiom or primitive. Its inputs
are the Wilson plane factor and standard Peter–Weyl, Schur, Jacobi–Trudi, Weyl,
Bessel, and Haar mathematics. No fitted or measured value is a derivation input.

**Status authority:** independent audit lane only. This source note does not set
or predict an outcome. The positive narrow theorem label is a source-side claim
boundary, not a verdict.
