# Beta=6 SU(3) Plaquette D7 Coefficient and Geometric-Ratio Verdict

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. The independent audit lane sets audit and
effective status.
**Primary runner:** [`frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)
**Order-7 cache wrapper:** [`frontier_beta6_connected_coefficient_2026_05_30_order7_cache.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30_order7_cache.py)

## Scope

This note extends the exact strong-coupling coefficient calculation from
[`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md).
Write

```text
Delta(beta) = P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n.
```

The prior note established

```text
d_5 = 1/472392,
d_6 = 7/5668704,
```

and reduced the order-`beta^7` support search to the four elementary cube
shells through the marked plaquette. This note supplies the exact order-7
multiplicity sum.

## Result

The exact order-`beta^7` connected coefficient is

```text
d_7 = 5/17006112.
```

Equivalently, each of the four cube shells contributes `5/68024448`.
The contiguous ratios are therefore

```text
d_6 / d_5 = 7/12,
d_7 / d_6 = 5/21.
```

They are not equal. Thus the specific single-ratio geometric/tadpole ansatz
that predicts

```text
d_7^pred = (d_6 / d_5) d_6 = 49/68024448
```

is falsified by the exact order-7 coefficient:

```text
d_7^exact = 5/17006112.
```

The relative miss is about `0.592` against the prediction, or `1.45` against
the exact value, far outside the existing 5% support window used by the
resummation test harness.

## How The Runner Computes It

The runner keeps the prior linked-cluster/cumulant structure and adds an
optimized exact contraction for the order-7 cube-shell multiplicity terms:

- the distinct-support side is still the GF(3) cycle-space certificate: no
  color-closable size-6 or size-7 distinct support through the marked plaquette
  exists, so only the four cube shells contribute through order 7;
- the SU(3) single-link integral is still the invariant-projector integral, but
  the order-7 path builds the per-link tensor sparsely from the invariant-basis
  supports instead of scanning a dense `3^(2(p+q))` grid;
- the contraction is exact `Fraction` arithmetic with variable elimination;
- the optimized engine reproduces the sympy engine's `d_5` and `d_6` exactly
  before computing `d_7`.

The review-loop run reproduced the runner's `maxorder=7` path:

```text
d_5 = 1/472392
d_6 = 7/5668704
d_7 = 5/17006112
PASS=22 FAIL=0
```

Because `scripts/cached_runner_output.py` caches by runner path and not argv,
the paired order-7 cache is generated through
`scripts/frontier_beta6_connected_coefficient_2026_05_30_order7_cache.py`.
That wrapper invokes the primary runner exactly as
`python3 scripts/frontier_beta6_connected_coefficient_2026_05_30.py 7` and
prints the SHA-256 of the full primary runner source before executing.

## Boundary

This is not a `P(beta=6)` derivation, not an `alpha_s` derivation, and not a
closed boosting form. It only proves one exact coefficient and rules out one
specific geometric continuation pattern for the connected coefficients.

The truncated forward value through `d_7` is a sensitivity datum, not a
derivation of the Monte-Carlo comparator. With the geometric continuation
falsified, beta=6 closure still requires a separate dynamical input or
resummation authority; this note does not supply one.
