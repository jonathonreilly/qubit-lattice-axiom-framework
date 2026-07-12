# Complex Determinant and Realification Determinant Power

**Date:** 2026-07-04; exact supplier repair 2026-07-11
**Claim type:** positive_theorem
**Status authority:** audit verdict authority remains with the independent
audit lane.
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
         exp(-sum_ij chibar_i K_ij chi_j)
  = det_C(K).
```

Here integration is the standard left Berezin derivative, normalized by
`integral d(theta) theta = 1`, with the rightmost differential acting first.

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

The result is real and nonnegative. Polynomiality extends the identity to
singular matrices.

## Berezin determinant power

Expand the Grassmann exponential. Terms beyond degree `2n` vanish. With the
displayed differential ordering and the minus sign in the exponent, the top
degree coefficient is the alternating sum over permutations of the matrix
entries, which is `det_C(K)`. The companion runner performs this exterior
algebra calculation directly for generic `1 x 1`, `2 x 2`, and `3 x 3`
kernels. The odd-dimensional checks certify the displayed sign convention
across both dimension parities.

## Exact checks

The runner verifies:

- the generic symbolic `2 x 2` realification identity;
- scalar, diagonal, singular, and exact `3 x 3` instances;
- first-power versus second-power scaling;
- generic `1 x 1`, `2 x 2`, and `3 x 3` Berezin Gaussian coefficients;
- the phase sensitivity of `det_C(K)` and phase blindness of
  `det_R R(K)`;
- source guards for the theorem domain and the separate physical AC(i)
  selector domain.

## Charged-lepton scope boundary

This theorem supplies the determinant-power fork used to state AC(i)
precisely. Its domain consists of the complex Gaussian, its realification, and
their exact determinant powers. Physical identification of the charged-lepton
matter carrier, K/CPT-orbit occupancy grain, path-integral measure, action,
registered-mass coordinate, phase, and R-eta readout belong to separate source
rows. The construction is constant over every supplied registered-mass ratio
`r`; `r` remains a free dial.

The two mathematical determinant constructions are both present in the
theorem. Their use as a charged-lepton occupancy rule is the domain of a
separate physical-carrier theorem.

## Verification

Run:

```bash
python3 scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py
```

Expected result: `PASS=18`, `FAIL=0`.
