# Complex Determinant and Realification Determinant Power

**Date:** 2026-07-04; exact supplier repair 2026-07-11
**Claim type:** positive_theorem
**Status authority:** independent audit lane. This source proposal does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py`](../scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.txt`](../logs/runner-cache/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.txt)

## Exact theorem

Let `K=X+iY` be an `n x n` complex matrix, with `X` and `Y` real, and let

```text
R(K) = [[X,-Y],
        [Y, X]]
```

be its realification. Then

```text
det_R R(K)
  = det_C(K) det_C(conjugate(K))
  = |det_C(K)|^2.
```

With the displayed Berezin ordering convention, the holomorphic Gaussian on
independent Grassmann variables satisfies

```text
integral d(chibar_n)d(chi_n)...d(chibar_1)d(chi_1)
         exp(sum_ij chibar_i K_ij chi_j)
  = det_C(K).
```

Thus a complex Gaussian determinant and the determinant of its realification
carry first and second determinant powers, respectively.

## Proof of the realification identity

Complexify the real `2n`-dimensional representation. The invertible complex
change of basis

```text
S = [[I, iI],
     [I,-iI]]
```

intertwines `R(K)` with the block diagonal matrix

```text
diag(K,conjugate(K)).
```

Determinant is invariant under similarity, so

```text
det_R R(K)
  = det_C K det_C(conjugate(K))
  = det_C K conjugate(det_C K).
```

The result is real and nonnegative. No invertibility assumption is needed;
the identity is polynomial and includes singular matrices.

## Berezin determinant power

Expand the Grassmann exponential. Terms beyond degree `2n` vanish. The top
degree coefficient is the alternating sum over permutations of the matrix
entries, which is `det_C(K)`. The displayed integration ordering extracts that
coefficient with positive sign. The companion runner performs this exterior
algebra calculation directly for a generic `2 x 2` kernel.

## Exact checks

The runner verifies:

- the generic symbolic `2 x 2` realification identity;
- scalar, diagonal, singular, and exact `3 x 3` instances;
- first-power versus second-power scaling;
- the generic `2 x 2` Berezin Gaussian coefficient;
- the phase sensitivity of `det_C(K)` and phase blindness of
  `det_R R(K)`;
- source guards that keep the physical AC(i) selector and `r` outside this
  theorem.

## Charged-lepton scope boundary

This theorem supplies the determinant-power fork used to state AC(i)
precisely. It does not identify the physical charged-lepton matter carrier
with the complex Gaussian or its realification. It does not select a
K/CPT-orbit occupancy grain, establish a path-integral measure, choose a
physical action, register or predict `r`, force `r=1/2`, derive `delta`, or
supply the R-eta readout license.

The two mathematical determinant constructions are both present in the
theorem. A separate physical carrier theorem or an explicitly governed premise
is required before either construction can be used as the charged-lepton
occupancy rule.

## Verification

Run:

```bash
python3 scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py
```

Expected result: `PASS=16`, `FAIL=0`.
