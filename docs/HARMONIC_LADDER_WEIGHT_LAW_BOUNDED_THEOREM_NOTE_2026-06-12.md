# Harmonic Ladder Weight Law: Single-Sideband Refutation and Laurent Determinant Corrected Law

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:** [`scripts/frontier_harmonic_ladder_weight_law_2026_06_12.py`](../scripts/frontier_harmonic_ladder_weight_law_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_harmonic_ladder_weight_law_2026_06_12.txt`](../logs/runner-cache/frontier_harmonic_ladder_weight_law_2026_06_12.txt)
**No-promotion statement:** This source note records a bounded finite-state
claim only; it creates no promotion, no registry edit, and no audit verdict.

## Scope

Exact finite `L=3` realized states only:

| state | seed |
| --- | ---: |
| `K=3` | `391` |
| `K=4` | `99` |
| `K=5` | `99` |
| `K=6` | `466` |

The runner mirrors the landed determinant-polar site-`0/1` machinery with
`tau=0.35`, `T=256`, Hankel window `64`, and a base-angle harmonic readout on
`4096` samples.

## Anchors

The anchor gates run first. They recompute the landed data and compare against
frozen constants:

| state | gap set | capture4 | `w2` |
| --- | --- | ---: | ---: |
| `K=3` | `(-3,0,+3)` | `0.898130088565` | `0.553095718694` |
| `K=4` | `(-3,0,+3)` | `0.777619557343` | `0.039738951671` |
| `K=5` | `(-3,0,+3)` | `0.899155545493` | `0.235902871426` |
| `K=6` | `(-3,0,+3)` | `0.994936516891` | `0.031142737014` |

The raw FFT reconstruction error is gated below `1e-12`, and the nonzero `k=2`
weight in every state is the anti-fabrication gate.

## Single-Sideband Test

For a single carrier plus one sideband, normalized to the fundamental,

```text
w2 / w1 = rho^2 / 4
```

so the direct extraction is `rho_12 = 2*sqrt(w2/w1)`.

| state | `rho_12` |
| --- | ---: |
| `K=3` | `5.242979872041` |
| `K=4` | `1.050456917487` |
| `K=5` | `1.323527082623` |
| `K=6` | `0.360499078290` |

Thus the proposed `|B| < |A|` single-sideband law is refuted on the realized
surface: `K=3,4,5` require `rho_12 >= 1`.

## Corrected Law

Let `q = exp(i theta)` and let `B_s(theta)` be the state-specific raw
site-`0/1` block before polar projection. Since the coupled gap set is exactly
`(-3,0,+3)`, the determinant is a degree-3 Laurent polynomial:

```text
F_s(q) = det B_s(theta) = sum_{n=-3}^{3} c_{s,n} q^n.
```

The corrected realized law is the principal-branch determinant phase increment

```text
g_s(theta) = Arg(F_s(e^{i(theta+delta)}) / F_s(e^{i theta})) - mean,
delta = 3*tau = 1.05.
```

The paired ladder weights `w_k` are the normalized Fourier powers of `g_s`.
This finite Laurent law includes the branch wrapping visible in `K=4`; the
unwrapped root-power formula alone misses that state.

The corrected root datum reported by the runner is

```text
rho_* = max( |r| for determinant roots |r|<1, 1/|r| for roots |r|>1 ).
```

| state | root split `(inside,outside)` | `rho_*` |
| --- | ---: | ---: |
| `K=3` | `(3,3)` | `0.991954900521` |
| `K=4` | `(4,2)` | `0.893042465934` |
| `K=5` | `(3,3)` | `0.991107064261` |
| `K=6` | `(2,4)` | `0.761907797708` |

All `rho_*` values are strictly in `(0,1)`, and the Laurent polynomial
reconstructs held-out determinant samples below `1e-12`.

## Weights and Tails

The corrected law predicts `w2,w3,w4` with max relative deviation below
`1e-10`.

| state | `w1` | `w2` | `w3` | `w4` |
| --- | ---: | ---: | ---: | ---: |
| `K=3` | `0.080482953834` | `0.553095718694` | `0.224756200523` | `0.078559324624` |
| `K=4` | `0.144052203784` | `0.039738951671` | `0.243850615756` | `0.046251924783` |
| `K=5` | `0.538675909484` | `0.235902871426` | `0.078440233399` | `0.067069470589` |
| `K=6` | `0.958536052775` | `0.031142737014` | `0.005115793421` | `0.002228063336` |

The full nonfundamental tail `T_ge2 = sum_{k>=2} w_k` is reproduced by the
corrected law but does **not** reproduce the landed depth order:

| state | `T_ge2` |
| --- | ---: |
| `K=3` | `0.919517036237` |
| `K=4` | `0.855947795669` |
| `K=5` | `0.461324082129` |
| `K=6` | `0.041463947067` |

Ascending order: `K6,K5,K4,K3`.

After separating the nonzero `k=2` sideband, the higher tail
`T_ge3 = sum_{k>=3} w_k` is the depth-ordered tail:

| state | `T_ge3` |
| --- | ---: |
| `K=3` | `0.366421317544` |
| `K=4` | `0.816208843998` |
| `K=5` | `0.225421210704` |
| `K=6` | `0.010321210053` |

Ascending order: `K6,K5,K3,K4`, matching the landed capture-depth order.

## Claim Boundary

The bounded source claim is restricted to these realized `L=3` states: the
ladder weights follow the finite Laurent determinant principal-Arg law above.
The single carrier/single-sideband law is refuted on this surface. The full
`k>=2` tail is not the depth tail; the depth-ordering statement is restricted
to the higher `k>=3` tail after the separately gated nonzero `k=2` sideband is
removed.
