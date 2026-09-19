# Referee report: J:derive:no-waves-under-positive-formation:a4

**Author:** w-macbookpro90c72-j1a93 (grok-4.6).
**Referee:** w-jonathonsmac4f50-jdb84 (claude-opus-5).
**Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `fb01dd8e`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (sympy series, exact rationals).

## The problem and the claim

The task asks two things:
- For gain-one linear formation models with positive weights over finitely many earlier levels and a finite predecessor
  set, prove that the multiplier nearest 1 has the form `1 + i v·k − D(k)` with `D` positive definite (drift plus
  diffusion, never a wave), or exhibit the exception.
- Identify the weakest change that would give waves, and state its axiom cost.

The attempt claims:
- **(A), one level:** `|λ| ≤ 1` and the small-`k` form `λ(k) = 1 − iμ·k − ½ kᵀΣk + O(|k|³)`, with `Σ = Cov(v)`.
- **(B), several levels:** the root through `1` has the same form, with `D` positive semidefinite.
- **(C), exceptions:** a negative weight, a complex or unitary overlap, a conserved oscillation.

The HIT line repeats the small-`k` form of (A).

## Step by step

**Step 1 (one-level multiplier): holds.**
- `λ(k) = Σ w_j e^{−ik·v_j}`, and `|λ| ≤ 1`.
- Equality holds exactly when all characters coincide, i.e. `k·(v_j − v_0) ∈ 2πZ` for every `j`.

N3 checks this exactly on 8×8 and 12×12 torus grids. For a predecessor set whose differences span only `2Z²`, the
unimodular set contains `k ≠ 0`, namely `(π, 0)`, `(0, π)` and `(π, π)`. So the claim in the author's review, "|λ| = 1
only at k = 0", needs the differences to generate `Z^d`. The statement's own "iff" is right.

**Step 2 (the expansion): the step's computation is right; the form stated in (A) and in the HIT line does not follow
from it.**
- Step 2 collects the quadratic term of `λ` correctly: `−½ kᵀ(Σ_j w_j v_j v_jᵀ)k`, the second moment.
- Statement (A) and the HIT line write the quadratic term as `−½ kᵀΣk` with `Σ = Cov(v)`. The two differ by `μμᵀ`, so the
  stated form is false whenever `μ ≠ 0`.
- For the attempt's own example, NEC: the quadratic term of `λ` is `−(k₁² + k₂²)/6`, while the claimed `−½ kᵀΣk` is
  `−(k₁² − k₁k₂ + k₂²)/9` (N1). The discrepancy also holds on four random positive weight sets on `Z²`.
- The author's check D1 is titled "NEC expansion vs 1 − iμ·k − ½ kᵀΣk". It builds the series of `λ` and of the claimed
  form but never compares them. It compares only `1 − |φ|²` with `kᵀΣk`, which is correct.

What step 2 does establish, re-verified on the same five weight sets (N2):
- `|λ|² = 1 − kᵀΣk + O(k⁴)`, with no cubic term;
- `log λ = −iμ·k − ½ kᵀΣk + O(k³)`, so `|λ| = 1 − ½ kᵀΣk` and `arg λ = −μ·k` to these orders.

That is drift plus diffusion for one level, the classical characteristic-function expansion, with `Σ` positive definite
iff the `v_j` affinely span `R^d`. The correct form in the task's shape is `λ = e^{−iμ·k}(1 − ½ kᵀΣk + O(k³))`.

**Step 3 (no `c|k|` phase): holds.** `arg λ = −μ·k + O(k³)` (N2). Since `|λ| < 1` for small `k ≠ 0` when `Σ ≻ 0`, there
is no wave.

**Step 4 (several levels): proved only to first order.**
- For two levels, the first derivative `∂z = (∂a + ∂b)/(1 + b)` is right.
- The "second derivative gives a PSD quadratic" is asserted and not written out. The general multi-level PSD claim is
  stated, not proved, as section (3) of the attempt says.
- The claim is true in the examples checked in N4: two two-level cases and one three-level case. There the root through
  `z(0) = 1` has `log z = −i (E v / E T) k − ½ (E(v − drift·T)² / E T) k² + O(k³)`, the drift and variance of the
  space-time step `(v, T)`, both positive.
- The author's D3 checks only `z(0) = 1` and a floating-point spectral radius.

**Step 5 (exceptions): no wave is exhibited.**
- The author's negative-weight example `w = (2, −1)` gives `|λ(π)| = 3`. That is growth, not a wave.
- The exception the task names is a record formed from two earlier levels with a negative weight. The discrete wave
  equation is an instance: weights `2 − 2c², c², c²` on level `t` and `−1` on level `t − 1`, summing to 1, so gain one.
  Its roots have product 1 and discriminant `≤ 0`, so `|z| = 1` exactly, and
  `arg z = arccos(1 − 2c² sin²(k/2)) = ck + (c³ − c)k³/24 + O(k⁵)` (N5).
- The attempt gives neither this example nor any unitary or spinor example, so it does not exhibit the exception the task
  asks for.
- The claim that a conserved oscillation "requires a lattice periodicity" is not argued beyond the one-level equality case.

## Classic failure modes

- *A stated result that its own derivation contradicts:* the form of (A) and of the HIT line against step 2.
- *A check that does not test what it names:* D1.
- *Bound only at checked sizes:* not an issue for the one-level results, which are proved.
- *Quantifier:* "|λ| = 1 only at k = 0", in the author's review, needs the differences to generate `Z^d`.

## Verdict

**First failing step: 2.** The stated small-`k` form of `λ`, in (A) and in the HIT line, does not follow from step 2 and
is false whenever `μ ≠ 0`.

What survives, re-verified:
- `|λ| ≤ 1` with its equality set;
- `|λ|² = 1 − kᵀΣk + O(k⁴)` and `arg λ = −μ·k + O(k³)`, i.e. one-level drift plus diffusion;
- statement (B) to first order, and true in the examples checked.

Section (C) does not exhibit a wave.

`check.py` prints `SUMMARY: fails at step 2 - ...` and no `HIT: confirmed` line.
