# Flavor Corner-Coupling Ratio Bound and Hilbert-Schmidt Characterization

**Date:** 2026-05-30
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not quote, set, or predict audit outcomes.
**Primary runner:** [`scripts/flavor_ba_ratio_bound_hs_equipartition_2026_05_30.py`](../scripts/flavor_ba_ratio_bound_hs_equipartition_2026_05_30.py)

## 0. Scope

This note records two finite facts about the symmetric corner-coupling form

```text
Y = a I + b (J - I)
```

on the three generation labels. It does not derive the physical value of `b/a`.

## 1. Positivity Bound

The eigenvalues of `Y` are

```text
a + 2b    (singlet),
a - b     (doublet).
```

For `a > 0`, positive semidefiniteness gives

```text
a + 2b >= 0,    a - b >= 0
=> -1/2 <= b/a <= 1.
```

The value `b/a = 1/sqrt(2)` is a strict interior point of this positivity window;
the positivity bound contains it but does not pin it.

## 2. Hilbert-Schmidt Equipartition Characterization

The diagonal and off-diagonal basis elements have Hilbert-Schmidt norms

```text
Tr(I^2) = 3,
Tr((J-I)^2) = 6.
```

Equal Hilbert-Schmidt contribution from `aI` and `b(J-I)` means

```text
3 a^2 = 6 b^2
=> (b/a)^2 = 1/2.
```

Equivalently, under the formal Gaussian density `exp(-Tr(Y^2)/2)` on this
two-coordinate subspace, the coordinate variances satisfy

```text
<b^2>/<a^2> = (1/6)/(1/3) = 1/2.
```

Combined with the symmetric-form identity

```text
Q = 1/3 + (2/3)(b/a)^2,
```

Hilbert-Schmidt equipartition gives `Q=2/3`. This is a characterization of the
ratio, not a derivation that the framework chooses the Hilbert-Schmidt measure.

## 3. What This Claims

- Positive semidefiniteness of `aI+b(J-I)` with `a>0` bounds
  `b/a` to `[-1/2, 1]`.
- Hilbert-Schmidt equipartition between the diagonal and off-diagonal basis
  directions is equivalent to `(b/a)^2 = 1/2`.
- Inside the symmetric two-parameter form, that ratio is equivalent to `Q=2/3`.

## 4. What This Does Not Claim

- It does not prove the physical measure is Hilbert-Schmidt.
- It does not derive the charged-lepton Koide value.
- It does not use observed masses, a fitted circulant amplitude, or a new axiom.
- It does not decide between Hilbert-Schmidt, dimension-weighted, or dynamical
  weighting in the actual matter-sector measure.

## 5. Runner

```bash
python3 scripts/flavor_ba_ratio_bound_hs_equipartition_2026_05_30.py
```

Expected result: `SCORECARD PASS=4 FAIL=0`.
