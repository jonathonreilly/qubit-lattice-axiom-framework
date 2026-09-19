# Referee report: J:derive:no-waves-under-positive-formation:a3

- **Author:** w-macbookpro90c72-j2425 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j40e2 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `e4bcf539`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code: sympy series and exact rationals.

## The claim

The claim covers a gain-one linear formation law on one earlier level, with a finite nonnegative predecessor measure:
- `|λ| ≤ 1`;
- `λ = 1 − i m·k − ½ kᵀMk + O(|k|³)`, with `M` the second moment;
- `|λ|² = 1 − kᵀ Cov k + O(|k|⁴)`.

So with `Cov` positive definite the mode nearest 1 is drift plus diffusion and never a wave.

Examples and exceptions:
- NEC: Hessian `−2 Cov`, with entries `−4/9` and `2/9`.
- The 7-stencil: `λ = 1 − E/7`.
- Collinear support and a singleton are the exceptions.
- Step 5 says what would give waves.

The multi-level case is stated as not done.

## Step by step

**Step 1 (triangle inequality): holds.** V1 checks it exactly on `8×8` and `12×12` grids. Equality occurs exactly where
the characters coincide.

**Step 2 (expansion): holds.**
- The quadratic term of `λ` is `−½ kᵀMk`, with `M` the second moment. This is the correct form. Attempt a4 of the same
  problem failed on exactly this point.
- `|λ|² = 1 − kᵀ Cov k + O(k⁴)` holds, with no cubic term.
- V1 checks both with exact series on NEC and on three random positive sets.
- For NEC (V2): mean `(−1/3, −1/3)` and `det Cov = 1/27`. The Hessian of `|λ|²` at 0 is `[[−4/9, 2/9], [2/9, −4/9]] = −2 Cov`,
  with determinant `4/27`.

**Step 3 (7-stencil): holds.**
- `λ = 1 − E/7` identically.
- On `(−π, π]³ ∖ {0}`, `λ ∈ [−5/7, 1)`, so `|λ| < 1`.
- The Hessian is `−(4/7) I`.
- V3 checks these, the range on a `π/6` grid.

**Step 4 (exceptions): holds, and more strongly than stated.** For collinear support, `det Cov = 0`, and `|λ| = 1`
*identically* along the transverse direction (V4). The attempt says "to this order"; in fact it holds to all orders. A
singleton gives a pure phase.

**Step 5 (what would give waves): a reading, not a proof, as marked.**
- The negative-weight example `(2, −1)` gives `|λ(π)| = 3`. That is growth, not a wave.
- The exception the task names is a record formed from two earlier levels with a negative weight. The discrete wave
  equation, with weight `−1` on the earlier level, is gain-one and has `|z| = 1` and `arg z = ck + O(k³)` (V5). The attempt
  does not exhibit it.

## Classic failure modes

None in the one-level statement.
- *Scope.* The task's "finitely many earlier levels" is addressed only for one level, and section (3) says the multi-level
  expansion is not written out.
- *Step 5.* Qualitative, as labelled.

## Verdict

The one-level statement survives, re-derived independently, with no failing step. Two caveats:
- the multi-level case is not covered;
- Step 5 lists the routes to waves without exhibiting one, and its example is growth.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
