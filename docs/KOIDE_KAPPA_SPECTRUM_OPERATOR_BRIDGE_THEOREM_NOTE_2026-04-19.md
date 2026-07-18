# Abstract Hermitian-Circulant Fourier Invariant Theorem

**Date:** 2026-04-19
**Type:** positive_theorem
**Claim type:** positive_theorem
**Scope:** exact finite algebra on `Herm_circ(3)` after the matrix variables are
defined; no physical carrier or observable interpretation is asserted.
**Status authority:** independent audit only. This source note does not assign
or predict an audit result.
**Primary runner:**
[`scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py`](../scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_kappa_spectrum_operator_bridge_theorem.txt`](../logs/runner-cache/frontier_koide_kappa_spectrum_operator_bridge_theorem.txt)

## The algebra and orientation

Fix

```text
C = [[0,1,0], [0,0,1], [1,0,0]],
omega = exp(2 pi i / 3),
f_k = (1, omega^k, omega^(2k))^T / sqrt(3),   k = 0,1,2.
```

Then `C^3=I`, `C^dagger=C^2`, and, with this orientation,

```text
C f_k = omega^k f_k.
```

Every complex circulant `3 x 3` matrix is a unique linear combination of
`I,C,C^2`. Hermiticity therefore gives the exact real form

```text
Herm_circ(3)
  = { H(a,b) = a I + b C + conjugate(b) C^2 : a in R, b in C }.
```

Writing `b=x+iy`, the three eigenvalues in the ordered basis
`(f_0,f_1,f_2)` are

```text
lambda_k = a + b omega^k + conjugate(b) omega^(-k),

lambda_0 = a + 2x,
lambda_1 = a - x - sqrt(3)y,
lambda_2 = a - x + sqrt(3)y.
```

They are real for all `a in R` and `b in C`.

## Normalized Fourier coordinates

For this ordered real eigenvalue triple, define

```text
a_0 = (lambda_0 + lambda_1 + lambda_2) / sqrt(3),
z   = (lambda_0 + omega^(-1) lambda_1 + omega^(-2) lambda_2) / sqrt(3)
    = (lambda_0 + conjugate(omega) lambda_1 + omega lambda_2) / sqrt(3).
```

The opposite nontrivial Fourier coefficient is `conjugate(z)` because the
`lambda_k` are real. The roots-of-unity sums

```text
sum_k omega^k = 0,
sum_k omega^(-k) omega^k = 3,
sum_k omega^(-k) omega^(-k) = 0
```

give the exact coordinate identities

```text
a_0 = sqrt(3) a,
z   = sqrt(3) b,
|z|^2 = 3 |b|^2.
```

An independent real-coordinate check in the same displayed orientation uses

```text
[ a_0  ]   [ 1/sqrt(3)   1/sqrt(3)      1/sqrt(3)    ] [lambda_0]
[ Re z ] = [ 1/sqrt(3)  -1/(2sqrt(3))  -1/(2sqrt(3)) ] [lambda_1]
[ Im z ]   [ 0          -1/2             1/2          ] [lambda_2].
```

The weighted Gram identity `R^T diag(1,2,2) R=I` yields the normalized
Parseval formula

```text
lambda_0^2 + lambda_1^2 + lambda_2^2 = a_0^2 + 2|z|^2.
```

## Theorem and global zero locus

**Theorem.** For every `a in R` and `b in C`, the normalized Fourier
coordinates above satisfy

```text
a_0^2 - 2|z|^2 = 3(a^2 - 2|b|^2).                 (1)
```

Consequently the two polynomial residuals have exactly the same zero locus:

```text
a_0^2 - 2|z|^2 = 0  <=>  a^2 - 2|b|^2 = 0.       (2)
```

This is a global polynomial statement, including `b=0`. On that boundary,
the residual is `3a^2`, so the zero locus meets `b=0` only at `a=0`.

If the shorthand

```text
kappa = a^2 / |b|^2
```

is used, its domain is explicitly `b != 0`. Only on that domain does (2)
become equivalently `kappa=2`. There is no ratio extension at `b=0`; in
particular, the origin belongs to the polynomial zero locus while the ratio
is undefined there.

**Proof.** Substitute `a_0=sqrt(3)a` and `|z|^2=3|b|^2` into the left side
of (1). The result is `3a^2-6|b|^2`, proving (1). Multiplication by the
nonzero scalar `3` preserves the zero locus, proving (2). The `b=0` statement
follows by direct substitution. QED.

## Characteristic polynomial and cubic trace

The same finite algebra gives

```text
det(tI-H)
  = (t-a)^3 - 3|b|^2(t-a) - (b^3 + conjugate(b)^3),

tr(H)   = 3a,
tr(H^2) = 3a^2 + 6|b|^2,
tr(H^3) = 3a^3 + 18a|b|^2 + 3(b^3 + conjugate(b)^3).    (3)
```

For (3), put `X=bC+conjugate(b)C^2`. The relations `C^3=I` and
`tr(C)=tr(C^2)=0` give

```text
tr(X)=0,
tr(X^2)=6|b|^2,
tr(X^3)=3(b^3+conjugate(b)^3).
```

Expanding `tr((aI+X)^3)` proves (3). This phase-sensitive cubic trace is an
abstract circulant invariant only.

## Executable verification

The primary runner has three separately callable modes:

```bash
python3 scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py --mode normal
python3 scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py --mode independent
python3 scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py --mode hostile
```

- `normal` verifies the stated shift/DFT orientation, diagonalization,
  coordinate identities, global polynomial identity, `b=0` boundary, ratio
  domain, and cubic trace.
- `independent` reconstructs the result without calling the normal route: it
  starts from the explicit matrix, characteristic polynomial, traces, the
  three real roots, and the explicit real DFT matrix.
- `hostile` requires wrong orientation, wrong normalization, missing
  conjugation, inverse cyclic shift, wrong `3/2` factors, a global `b=0`
  ratio claim, and wrong cubic-trace coefficients to leave nonzero exact
  residues or an explicit domain counterexample.

With no `--mode` argument, the runner executes all three modes so the single
canonical SHA-pinned cache records every evidence path.

No theorem count is awarded for prose presence, a literal boolean, an
external numerical comparator, or a target-value match.

## Exact boundary

This theorem is solely about the abstract matrix algebra
`Herm_circ(3)` and the stated normalized Fourier transform. It does not:

- identify any `lambda_k` with a mass or square root of a mass;
- derive a charged-lepton, generation, or other physical carrier;
- supply P1, a cyclic-compression physical identification, or a physical
  selector/readout;
- predict a physical `Q=2/3` condition or a physical `kappa` value;
- establish an MRU principle, scalar measure, axiom-cost conclusion, or
  physical closure.

Any such interpretation requires separate authority. None is imported here,
and this row has no theorem dependencies.
