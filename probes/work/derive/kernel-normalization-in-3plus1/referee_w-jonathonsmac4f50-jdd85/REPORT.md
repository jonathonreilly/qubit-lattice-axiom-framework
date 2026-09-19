# Referee report: J:derive:kernel-normalization-in-3plus1:a2

- **Author:** w-macbookpro90c72-j01ee (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jdd85 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `c9f4afbf`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (exact rationals, and an exact real DFT on
`(Z/2)³`).

## The claim

The attempt makes three claims:
- **The sum rule.** Since `|s| = 1`, `2C(0) + ⟨s_z²⟩ = 1`, so `C(0) ≤ (1 − |m|²)/2`.
- **Parseval.** `C(0) = V^{−1} Σ_k S_0(k)`.
- **The weighted average.** `R_avg = C(0)/(σ²G_V) ≤ (1 − |m|²)/(2σ²G_V)`, the `G`-weighted average of
  `R(k) = S_0(k)(1 − |φ|²)/σ²` over `k ≠ 0`. This average does not determine `R(k → 0)`.

It also states `G_4 = 1913/1344`, with weights in `[1, 8/3]`.

## Step by step

**Step 1 (unit-vector sum rule): holds.** W1 checks it on 300 random six-axis configurations.

**Step 2 (Parseval): holds.** `Σ_k |FFT f|²/V = Σ_x f_x²` for all 6561 fields `f ∈ {−1, 0, 1}⁸` on `(Z/2)³` (W2).

**Step 3 (the weighted-average identity): the equality does not follow; the inequality survives.**
- `R_avg` is an average over `k ≠ 0`. So `σ²G_V R_avg = V^{−1} Σ_{k≠0} S_0(k) = C(0) − S_0(0)/V`, where `C(0)` is the full
  Parseval sum of Step 2.
- The zero-mode term is `S_0(0)/V = E[(plane average of s_x)²]`. It is positive whenever the plane average of the
  transverse components fluctuates, even when `E s_x = 0`.
- In the simulator (`probes/lib/formation_levelplane.py`), `S_0` is computed in a fixed lab frame and keeps `k = 0`. The
  code itself removes the zero mode only when it forms "C(r) without the zero mode".
- W3 gives an exact example: one tilted site on `(Z/2)³` has `C(0) = 1/8`, `V^{−1} Σ_{k≠0} S_0 = 7/64` and
  `S_0(0)/V = 1/64`.
- So `R_avg = C(0)/(σ²G_V)` fails in general. What holds is `R_avg ≤ C(0)/(σ²G_V) ≤ (1 − |m|²)/(2σ²G_V)`.
- The attempt's conclusion survives: the sum rule constrains a weighted average, not `R(k → 0)`.

**Step 4 (the weights): holds.** `G_4 = 1913/1344`, both by the exact Fourier sum on `(Z/4)³` and by the real-space
Lyapunov solve. The weights `1/(1 − |φ|²)` range over `[1, 8/3]` (W4).

## Classic failure modes

- *A dropped term.* The zero mode in Step 3's equality.
- *Scope.* The route to the coefficient `a` is correctly reported as not closing.

## Verdict

**First failing step: 3.** The stated equality omits the zero mode. The inequality, the attempt's conclusion and Steps 1, 2
and 4 survive, re-verified.

`check.py` prints `SUMMARY: fails at step 3 - ...` and no `HIT: confirmed` line.
