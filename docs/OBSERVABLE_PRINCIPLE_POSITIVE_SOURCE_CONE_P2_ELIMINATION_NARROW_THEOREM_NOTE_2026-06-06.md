# Observable Principle Positive Source Cone P2 Elimination Narrow Theorem Note

**Date:** 2026-06-06
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py`](../scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py)
**Cached output:**
[`logs/runner-cache/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.txt`](../logs/runner-cache/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.txt)

## Claim

On the finite real staggered source surface consumed by
[`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md),
the global P2 phase-blindness premise is not load-bearing. The finite
Dirac block is real antisymmetric and the scalar sources used for the
parent's source-response theorem are real diagonal. On the positive
diagonal source cone, and on a small real local-source patch around any
invertible zero-source block, `det(D + J)` is real-positive. Therefore

```text
log det(D + J) = Re Log det(D + J) = log |det(D + J)|
```

on the in-scope branch. Phase-sensitive and phase-blind scalar-generator
candidates have identical values and identical source derivatives there.
P2 is eliminated on this consumed source surface; it is not promoted to a
new axiom and is not solved globally.

## Proof

### 1. Positive diagonal source cone

Let `D^T = -D` be a real antisymmetric finite matrix and let `S` be a
positive diagonal matrix. Then

```text
S + D = S^(1/2) (I + S^(-1/2) D S^(-1/2)) S^(1/2).
```

The middle factor is `I + B` with `B^T = -B` real antisymmetric. The
eigenvalues of `B` are `0` or conjugate pairs `± i lambda_k`, so

```text
det(I + B) = product_k (1 + lambda_k^2) > 0.
```

Since `det S > 0`, `det(S + D) > 0`. Thus a positive real diagonal scalar
source has no determinant phase.

### 2. Local derivative patch

For the local source-derivative formulas in the parent, one works on a
finite block where `D` is invertible. Then `det D > 0` because a real
antisymmetric invertible matrix has paired eigenvalues `± i lambda_k`.
If a real diagonal source `J` satisfies `||D^{-1} J|| < 1`, the path
`D + tJ`, `t in [0,1]`, is invertible by the Neumann bound. Along this
path the real determinant cannot cross zero, so its sign remains the
positive sign of `det D`. Hence `det(D + J) in R_{>0}` on a concrete
finite local-source neighborhood of the origin.

This is the source patch needed for the parent's derivative identities:
inside it `log det`, `Re Log det`, and `log|det|` are the same real
analytic branch, so all local source derivatives agree.

### 3. Record additivity selects the logarithm on `R_{>0}`

On the phase-free source surface, the amplitude is a positive real
multiplicative scalar. For independent block sums,

```text
det((D_1 + J_1) direct_sum (D_2 + J_2))
  = det(D_1 + J_1) det(D_2 + J_2).
```

Record supplies finite scalar additivity for disjoint record collections.
Together with finite-block continuity on `R_{>0}`, the
multiplicative-to-additive Cauchy equation forces the generator family
`W_c = c log det`. The parent uses the conventional representative
`c = 1` and zero-source subtraction.

### 4. Off-sector guard

For a generic complex determinant with nonzero phase, a phase-sensitive
candidate such as `log|Z| + b arg Z` differs from `log|Z|`. This note
does not derive global phase-blindness on that off-sector surface. It
only shows that the global P2 premise is unnecessary on the finite
real-positive source surface that the parent note consumes.

## Runner

The companion runner verifies:

- `det(S + D) in R_{>0}` for 300 random real-skew matrices and positive
  diagonal sources;
- the homogeneous consumed line `D + jI` has zero phase;
- phase-sensitive and phase-blind candidates coincide when `arg det = 0`;
- a small real local-source patch around an invertible block stays
  real-positive;
- determinant multiplicativity and logarithmic additivity on independent
  source blocks;
- an off-sector complex example where phase-sensitive candidates differ,
  preventing any hidden global-P2 overclaim.

## Boundary

This note does not retag `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`. It
does not close the `AC_phi_lambda`/Berezin determinant-identification
gate, does not derive measurement/Born/source-action physics, and does
not add a fourth axiom. Its role is to remove the separate P2
phase-blindness import from the finite real-positive source sector that
the parent actually differentiates.
