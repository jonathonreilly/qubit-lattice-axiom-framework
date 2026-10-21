# Wilson and heat-kernel leading short-time matching

**Date:** 2026-05-06; scope correction 2026-10-21
**Type:** bounded_theorem
**Status:** conditional leading Gaussian coefficient identity; exact finite-time and physical action selection open.
**Primary runner:** [companion](../scripts/probe_hk_time_derivation.py)

Supply Hermitian SU(3) generators `T_a=lambda_a/2` with
`Tr(T_a T_b)=delta_ab/2`, a positive Wilson parameter beta, and the
Wilson action `S_W=beta(1-Re Tr U/Nc)`. The Lie algebra tangent basis is
`iT_a`; use metric `<iX,iY>=2Tr(XY)` on anti-Hermitian tangents. Then
`U=exp(iX)` gives

```
Tr(X²)=|X|²/2,
S_W(exp(iX))=beta |X|²/(4Nc)+O(|X|^4).
```

For the nonpositive Laplace-Beltrami operator `Delta=sum_a E_a²`,
with `E_a` the invariant derivatives along `iT_a`, the Brownian generator
is `Delta/2`. Its heat-kernel character expansion is

```
p_t(U)=sum_R dim(R) exp(-t C2(R)/2) chi_R(U), t>0.
```

The leading *short-time* Gaussian exponential in a normal neighborhood is
`exp(-d(e,U)²/(2t))`. Radial distance satisfies `d(e,exp(iX))=|X|`
inside the injectivity neighborhood; the exponential map is not a local
Riemannian isometry. The full heat kernel includes a spatial Jacobian
amplitude and curvature terms. Their logarithms can contribute quadratic
terms in X. Therefore `S_HK=|X|²/(2t)+O(|X|^4)` is not the full
fixed-time Taylor expansion.

Matching only the leading short-time Gaussian coefficient to the Wilson
quadratic coefficient gives the exact conditional algebraic identity

```
beta/(4Nc)=1/(2 t_leading)  iff  t_leading=2Nc/beta.
```

Under the separately supplied convention `beta=2Nc/g²`, this formal
parameter is `g²`. At Nc3,beta6 its value is1. This substitution is not a
controlled small-time approximation at t1 and does not prove exact
finite-time matching. No physical beta or g is selected.

A useful check distinguishes the two statements. For SU3 let
`d_pq=(p+1)(q+1)(p+q+2)/2` and
`C_pq=(p²+pq+q²+3p+3q)/3`. Ad-invariance gives
`Tr_R(T_a²)=d_R C_R/8`. Thus the coefficient of x² in
`-log p_t(exp(ixT_a))` equals

```
[sum d_pq² C_pq exp(-t C_pq/2)] / [16 sum d_pq² exp(-t C_pq/2)].
```

At t1, truncated numerical sums with p,q<=20 and30 both give approximately
0.4375, not0.5. This is a converged numerical diagnostic, not an
infinite-tail certificate; the short-time proof boundary above does not
rely on turning it into an exact value.

For a *supplied* heat-kernel single-plaquette measure at t1, character
orthogonality gives `<Re Tr U/3>=exp(-2/3)≈0.5134171190`. Comparison with
Wilson single-plaquette or lattice-MC numbers compares different measures.
It supplies no evidence that the heat-kernel action is physically selected.

The runner checks the64 trace pairs, orthonormalization, the supplied
Wilson quadratic expression and Gaussian parameter substitutions. It does
not compute the exact heat-kernel Hessian or a thermodynamic limit.
The [canonical-normalization source](G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md)
and [normalization discussion](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md)
are context for the supplied conventions, not proofs of physical selection.

The original note and runner are recoverable at
`f24d17d97d372df977476e4a69674577f31af575` at the same paths, including
the withdrawn fixed-time proof and literature-convention assertions.
Those assertions are not used as authority here. Standard heat-kernel
machinery does not supply the missing action, finite-beta or physical bridge.
