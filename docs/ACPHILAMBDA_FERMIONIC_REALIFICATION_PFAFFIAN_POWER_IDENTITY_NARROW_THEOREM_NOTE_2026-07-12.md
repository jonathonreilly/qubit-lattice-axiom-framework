# Fermionic Realification and Pfaffian Determinant Power

**Date:** 2026-07-12
**Claim type:** positive_theorem
**Status authority:** independent audit lane. This source proposal does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/acphilambda_fermionic_realification_pfaffian_power_identity_2026_07_12.py`](../scripts/acphilambda_fermionic_realification_pfaffian_power_identity_2026_07_12.py)
**Cached output:**
[`logs/runner-cache/acphilambda_fermionic_realification_pfaffian_power_identity_2026_07_12.txt`](../logs/runner-cache/acphilambda_fermionic_realification_pfaffian_power_identity_2026_07_12.txt)

## Exact theorem

Let `K` be an `n x n` complex matrix and introduce independent Grassmann
columns `chibar` and `chi`. In the ordered column

```text
Psi = (chibar_1,...,chibar_n,chi_1,...,chi_n)^T
```

define the antisymmetric kernel

```text
A_K = [[0, K],
       [-K^T, 0]].
```

Then

```text
(1/2) Psi^T A_K Psi = chibar^T K chi,

Pf(A_K) = (-1)^(n(n-1)/2) det_C(K).
```

Let the left Berezin derivatives act from the rightmost differential first,
and define the measure orientation explicitly by

```text
D(Psi) = (-1)^(n(n+1)/2) d(Psi_2n)...d(Psi_1).
```

The top coefficient of `exp(-(1/2)Psi^T A_K Psi)` in the ordered monomial
`Psi_1...Psi_2n` is `(-1)^(n(n+1)/2) det_C(K)`. The displayed orientation
therefore gives the complex-fermion Gaussian with determinant power one:

```text
integral D(Psi) exp(-(1/2) Psi^T A_K Psi) = det_C(K).
```

This remains true when `chibar,chi` are reorganized into Majorana-paired
Grassmann coordinates: an invertible linear coordinate change transforms the
kernel by congruence and the Berezin measure by the inverse Jacobian, leaving
the Gaussian value unchanged. No physical Majorana reality condition is used.

By contrast, adjoin an independent conjugate sector and order the direct-sum
variables by concatenating the `A_K` block before the `A_conjugate(K)` block.
Then Pfaffian direct-sum multiplicativity gives exactly

```text
Pf(A_K direct_sum A_conjugate(K))
  = det_C(K) det_C(conjugate(K))
  = |det_C(K)|^2
```

The same scalar equals
`det_R R(K)` for the ordinary realification

```text
R(K) = [[Re K,-Im K],
        [Im K, Re K]].
```

Therefore `det_R R(K)=|det_C(K)|^2` has the same scalar determinant as the
displayed conjugate-paired Pfaffian product. This scalar equality does not
identify the ordinary realification with that doubled Grassmann carrier. In
particular, it is not the result of merely writing one complex fermionic
Gaussian in real Grassmann coordinates. The matrix `R(K)` need not be
antisymmetric and therefore need not itself be the quadratic kernel of the
displayed single Majorana Gaussian.

## Proof

Grassmann anticommutation gives

```text
(1/2)(chibar^T K chi - chi^T K^T chibar)
  = chibar^T K chi.
```

The standard block-Pfaffian identity

```text
Pf([[0,K],[-K^T,0]]) = (-1)^(n(n-1)/2) det(K)
```

follows by expanding the Pfaffian: every nonzero perfect matching pairs a
`chibar` index with a `chi` index, and the resulting signed permutation sum
is the determinant. It is a polynomial identity, so singular matrices are
included.

For an invertible coordinate change `Psi=M Xi`, the kernel becomes
`M^T A_K M`. Pfaffians and Berezin measures transform as

```text
Pf(M^T A_K M) = det(M) Pf(A_K),
D(Psi) = det(M)^(-1) D(Xi)
```

for the paired orientation convention. The factors cancel in the Gaussian.
Thus a complex-to-Majorana coordinate change cannot alter the determinant
power. A second power arises after the independent conjugate block is
adjoined.

The equality between the conjugate product and the realification determinant
is the retained finite-matrix identity proved in
[`ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md`](ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md).
Its complexified similarity decomposition is
`R(K) ~ diag(K,conjugate(K))`.

## Exact checks

The runner verifies:

- antisymmetry and the block-Pfaffian identity for generic ranks 1, 2, and 3;
- the Grassmann quadratic-form identity at generic rank 2;
- covariance under generic congruence and cancellation with its Berezin
  Jacobian;
- direct exterior-algebra checks of the negative-exponent Gaussian and its
  stated measure orientation at ranks 1, 2, and 3;
- the direct-sum product with the conjugate block;
- agreement of that product with the ordinary realification determinant;
- phase sensitivity of the single-sector Pfaffian and phase cancellation in
  the conjugate-paired construction;
- a singular example and an explicit non-antisymmetric realification;
- source guards preserving the charged-lepton scope boundary.

## Charged-lepton scope boundary

This theorem corrects the interpretation of the determinant-power fork. It
shows that a Majorana-paired Grassmann presentation of a supplied single
complex fermionic Gaussian preserves the first determinant power. The
coordinate statement does not impose a physical reality condition. Within the
displayed Grassmann-Gaussian construction, obtaining the modulus square instead
uses a supplied conjugate sector or conjugate-paired readout.

It does not derive from the four axioms that the charged-lepton carrier has
the displayed Grassmann action, Berezin measure, global CAR structure, or a
single-sector physical readout. It does not select a K/CPT-orbit occupancy
grain, register or predict `r`, force `r=1/2`, derive `delta`, or supply the
R-eta readout license. Those physical identifications require separately
audited retained support.

## Verification

Run:

```bash
python3 scripts/acphilambda_fermionic_realification_pfaffian_power_identity_2026_07_12.py
```

Expected result: `PASS=32`, `FAIL=0`.
