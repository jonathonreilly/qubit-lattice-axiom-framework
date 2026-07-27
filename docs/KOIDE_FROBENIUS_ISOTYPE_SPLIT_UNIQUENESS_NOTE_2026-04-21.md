# Koide Frobenius Isotype-Weight Freedom No-Go

**Date:** 2026-04-21; narrowed 2026-05-26
**Claim type:** no_go
**Claim scope:** Within the family of symmetric bilinear forms
`B_{alpha,beta}` on `Herm(3)`, positive-definiteness, unitary
Ad-invariance, and scalar/traceless orthogonality leave a free relative
isotype weight and therefore do not force `beta = 0`.
**Status:** bounded no-go. Positive-definiteness, Ad-invariance, and
scalar/traceless isotype orthogonality do not force the Frobenius
normalization `beta = 0`.
**Runner:** [`scripts/frontier_koide_frobenius_isotype_split_uniqueness.py`](../scripts/frontier_koide_frobenius_isotype_split_uniqueness.py)

## Purpose

The prior row was a conditional AM-GM packet: if the trace-Frobenius
normalization is admitted, then the block-energy AM-GM extremum gives
`kappa = 2` and `Q = 2/3`. The audit blocker was the missing bridge that
would force that normalization.

This repair keeps the stronger, unconditional finite result:

> the proposed one-step bridge cannot work. The accepted linear-algebra
> conditions leave a real scalar/traceless isotype-weight freedom, so they do
> not force `beta = 0`.

## Exact No-Go Statement

For real `alpha,beta`, consider the real symmetric bilinear form on `Herm(3)`

```text
B_{alpha,beta}(A,B) = alpha Tr(AB) + beta tr(A) tr(B).
```

It is unitary Ad-invariant. Indeed, for every unitary `U`, cyclicity of the
trace gives

```text
tr(UAU^dagger) = tr(A),
Tr[(UAU^dagger)(UBU^dagger)] = Tr(UABU^dagger) = Tr(AB).
```

On the scalar/traceless decomposition

```text
A = A_s + A_t,
A_s = tr(A) I / 3,
tr(A_t) = 0,
```

and likewise for `B`, the full bilinear form, not only its quadratic
restriction, is block diagonal:

```text
B_{alpha,beta}(A,B)
  = (alpha + 3 beta) Tr(A_s B_s) + alpha Tr(A_t B_t).
```

The mixed terms vanish for every `alpha,beta`, so scalar/traceless
orthogonality cannot select a relative block weight. The quadratic form is

```text
B_{alpha,beta}(A,A)
  = (alpha + 3 beta) Tr(A_s^2) + alpha Tr(A_t^2).
```

It is positive definite exactly when

```text
alpha > 0,
alpha + 3 beta > 0.
```

Sufficiency follows because the Frobenius quadratic form is positive on each
Hermitian block. Necessity follows by testing a nonzero traceless matrix, for
example `diag(1,-1,0)`, and the scalar matrix `I`, respectively.

The Frobenius normalization is the point `beta = 0`, where the scalar and
traceless weights are equal. But the positive-definite region contains many
points with `beta != 0`. More explicitly, the family `B_{1,lambda}` is
positive definite for every `lambda > -1/3` and has the scale-invariant
isotype-weight ratio

```text
w_scalar / w_traceless = 1 + 3 lambda.
```

Overall rescaling therefore does not remove the freedom. For example,
`lambda = 1` has scalar weight `4`, traceless weight `1`, is positive
definite, is Ad-invariant, preserves scalar/traceless orthogonality, and
differs from Frobenius on trace-bearing matrices:

```text
A = diag(1,1,2),
B_{1,0}(A,A) = 6,
B_{1,1}(A,A) = 22.
```

Therefore PD + Ad-invariance + scalar/traceless orthogonality cannot derive
the Frobenius isotype-weight ratio `w_scalar / w_traceless = 1`.

## Why The AM-GM Step Does Not Remove The Freedom

The same free parameter survives after restriction to
`Herm_circ(3)`. For

```text
M = a I + b C + conjugate(b) C^2,
```

the `B_{1,lambda}` block energies are

```text
E_plus(lambda) = 3 (1 + 3 lambda) a^2,
E_perp(lambda) = 6 |b|^2.
```

At fixed `B_{1,lambda}(M,M)`, AM-GM still uniquely selects equal *weighted*
block energies, but that condition now gives

```text
E_plus(lambda) = E_perp(lambda)
  => kappa(lambda) := a^2 / |b|^2 = 2 / (1 + 3 lambda).
```

Thus the extremization is unique only after the metric weight `lambda` is
fixed. It returns `kappa = 2` precisely at the separately chosen Frobenius
point `lambda = 0`; AM-GM itself does not select that point.

## Conditional Corollary Kept Out Of Scope

If a separate authority supplies `beta = 0`, then the familiar AM-GM algebra
on `Herm_circ(3)` gives

```text
E_plus = 3 a^2,
E_perp = 6 |b|^2,
E_plus = E_perp  =>  a^2 / |b|^2 = 2,
Q = (1 + 2/kappa)/3 = 2/3.
```

That conditional AM-GM chain is not the binding claim of this row. The binding
claim is the no-go above: the available linear-algebra premises do not force
the needed normalization.

## Boundary

This row does not claim:

- a derivation of `Q = 2/3` from the current framework;
- a derivation of the physical charged-lepton Koide relation;
- uniqueness of the Frobenius normalization;
- a physical charged-lepton mass-spectrum theorem;
- any new axiom or audit verdict.

Future positive work must supply an independent premise or derivation that
fixes the scalar/traceless isotype-weight ratio to `1`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_frobenius_isotype_split_uniqueness.py
```
