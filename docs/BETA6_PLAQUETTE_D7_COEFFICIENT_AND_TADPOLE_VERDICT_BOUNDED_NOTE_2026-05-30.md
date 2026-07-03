# Beta=6 SU(3) Plaquette D7 Coefficient and Geometric-Ratio Verdict

**Date:** 2026-05-30
**Type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. Review-loop does not set audit verdicts or
generated status fields.
**Primary runner:** [`frontier_beta6_d7_maxorder7_packet_2026_06_05.py`](../scripts/frontier_beta6_d7_maxorder7_packet_2026_06_05.py)
**Delegated full-source runner:** [`frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)
**Maxorder-7 packet cache:** [`frontier_beta6_d7_maxorder7_packet_2026_06_05.txt`](../logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt)
**D9 cross-certificate runner:** [`frontier_beta6_d9_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d9_coefficient_2026_06_04.py)
**D9 cross-certificate cache:** [`frontier_beta6_d9_coefficient_2026_06_04.txt`](../logs/runner-cache/frontier_beta6_d9_coefficient_2026_06_04.txt)
**Source-packet verifier:** [`frontier_beta6_d7_source_packet_manifest_2026_06_05.py`](../scripts/frontier_beta6_d7_source_packet_manifest_2026_06_05.py)
**Source-packet verifier cache:** [`frontier_beta6_d7_source_packet_manifest_2026_06_05.txt`](../logs/runner-cache/frontier_beta6_d7_source_packet_manifest_2026_06_05.txt)
**Source-packet verifier JSON:** [`frontier_beta6_d7_source_packet_manifest_2026_06_05.json`](../outputs/frontier_beta6_d7_source_packet_manifest_2026_06_05.json)

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

The `2026-06-05` source packet makes that path cache-addressable for the audit
runner. The delegated full-source runner still accepts `maxorder` as an argv
argument, while the cache system invokes runners without argv; therefore the
primary packet runner `scripts/frontier_beta6_d7_maxorder7_packet_2026_06_05.py`
delegates to
`scripts/frontier_beta6_connected_coefficient_2026_05_30.py 7` and pins the
completed output, including the primary runner SHA-256 printed inside the
cache. The later `frontier_beta6_d9_coefficient_2026_06_04.py`
cache is also linked as an independent cross-certificate: before its order-9
work, it reproduces `d_7 = 5/17006112` and checks that the cube-sector closed
form reproduces direct-engine `d_5`, `d_6`, `d_7`, and `d_8`.

The source-packet verifier checks note links, primary-source markers, wrapper
delegation markers, wrapper/cache SHA freshness, primary-source SHA pinning,
and the required `d_7` snippets. It does not assign an audit verdict.

## Boundary

This is not a `P(beta=6)` derivation, not an `alpha_s` derivation, and not a
closed boosting form. It only proves one exact coefficient and rules out one
specific geometric continuation pattern for the connected coefficients.

The truncated forward value through `d_7` is a sensitivity datum, not a
derivation of the Monte-Carlo comparator. With the geometric continuation
falsified, beta=6 closure still requires a separate dynamical input or
resummation source; this note does not supply one.
