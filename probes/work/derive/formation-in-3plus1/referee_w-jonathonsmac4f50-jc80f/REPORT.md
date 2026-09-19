# Referee report: J:derive:formation-in-3plus1:a5

- **Author:** w-macbookpro90c72-jd7c3 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jc80f (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jd7c3__3851a780__20260919T014507Z`.

**Disclosure.** This referee's model family has already refereed other attempts of this problem:

| Attempt | Referee directory | Outcome |
|---|---|---|
| a1 | `…-j9163` | confirmed |
| a2 | `…-j8735` | confirmed |
| a3 | `…-jff50` | — |
| a4 | `…-j5d38` | confirmed |
| a6 | `…-j223e` | confirmed |

`check.py` here is independent sympy code.

## The claim

The claim covers task (d) only.
- **The DAG.** The backward 4-predecessor relation is a DAG.
- **At `k = (π/2,0,0)`.** `φ = (3+i)/4`, `|φ|² = 5/8`, the covariance symbol `C = 8/3`, and the causal static response `R = 2(1+i)`. So
  `R/C = (3/4)(1+i)` is not real.
- **The general statement.** `R` is a real multiple of `C` iff `φ` is real.
- **The contrast.** The symmetric 7-stencil gives the real `R/C = 12/7 = 1 + φ_s`.
- **The small-`k` behaviour.** The drift is `(1,1,1)/4`, and "the causal response is `O(1/|k|)`, covariance `O(1/k²)`".

Sphere LRO and bounds on `S(k)` are not claimed.

## Step by step

**Step 1 (DAG): holds.** V1 enumerates a `3⁴` box: there are no 2-cycles, and every edge lowers the level by 1.

**Step 2 (`φ` not real; cosine identity): holds.** V2 confirms `φ(π/2,0,0) = 3/4 + i/4` and `|φ|² = 5/8`. The identity
`|φ|² = (2 + Σ cos k_j + Σ_{i<j} cos(k_i − k_j))/8` holds symbolically.

**Step 3 (FDT mismatch): holds.**
- V2 gives `C = 8/3`, `R = 2 + 2i` and `R/C = 3/4 + 3i/4`.
- **The iff.** The argument `R/C = (1 − |φ|²)/(1 − φ)` is real iff `φ` is real is correct. V3 checks it on all 215 eligible modes of
  `(2π/6)Z³`, with no mismatch.

**Step 4 (drift and small-`k` order): the drift holds, but the order claim is too strong.**
- V5 gives `∇φ(0) = i(1,1,1)/4` and `∇(1 − |φ|²)(0) = 0`.
- **Where "`R = O(1/|k|)`" fails.** On the plane `k₁ + k₂ + k₃ = 0`, the linear term of `1 − φ` vanishes. Along `t(1,−1,0)/√2`, V6
  finds:
  - `1 − φ = t²/8 + O(t³)`, so `|R| ~ 8/t²`;
  - `1 − |φ|² = t²/4`, so `R/C → 2`, which is real.

  So the causal response is `O(1/|k|)` only off that plane. Along `(1,1,1)`, `|R| ~ 1/t` as stated. The attempt's HIT line does not use the
  order claim.

**Step 5 (symmetric contrast): holds.** V4 gives `φ_s = 5/7`, `R_s = 7/2`, `C_s = 49/24` and `R_s/C_s = 12/7 = 1 + φ_s`.

**Step 6 (LRO): not attempted, as the attempt says.**

## Verdict

**The task-(d) partial survives, re-derived exactly.** It covers:
- the DAG;
- the mismatch at `(π/2,0,0)` and the iff criterion on 215 modes;
- the symmetric contrast;
- the drift.

One correction: the claim "causal response `O(1/|k|)`" depends on direction. On `k₁ + k₂ + k₃ = 0` it is `O(1/|k|²)`, with `R/C → 2`.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
