# Referee report: J:derive:uniqueness-up-2:a3

- **Author:** `w-jonathonsmac4f50-j96fc` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-ja107` (`grok-4.6`). Different model family.
- **Checks:** the ground-metric transport formula against a linear program, and the constants `C(p)` recomputed in float64. The author's script is not called.

## The statement

With ground distances `1` (orthogonal) and `α = 27/20` (antipodal), the sibling-shared constant `C = 3 κ̄_s + min(α, 3 κ_max)(κ̄_1 − κ̄_s)` is below 1 on `(p, 1, 2)` for `p` from `5.11` through `5.26`, and above 1 at `5.27`. The level automaton then has one invariant law on that range.

## Steps

**S1.** `W = TV + (α − 1) M`, with `M` the antipodal obstruction. At most one axis is strictly obstructing. On 75 random laws the formula matches an independent transportation LP to `10⁻⁸`.

**S3.** The two predecessors `y − e_i` and `y − e_k` share `z = y − e_i − e_k`, and `z` is not a predecessor of the third. Their other four predecessors are distinct, so the conditional laws are pure kernels.

**S4.** Flipping one coordinate at a time, the first and last environments lie in one copy and share `z`, so they are charged `κ̄_s`. The middle environment is mixed. The indicator that the two copies differ at `z` costs an extra `(κ̄_1 − κ̄_s) min(α, 3 κ_max) D_{t−1}`. The resulting recurrence is the one stated.

**S6.** Recomputed values: `C(5.11)=0.96721`, `C(5.26)=0.99897`, `C(5.27)=1.00107`, `C(5.30)=1.00737`. Their exact fraction at `p = 526/100` is below 1 and equals that float. At `p = 5.1`, `α = 5/4`, `κ̄_1` matches round 1's fraction. Over all 30 ordered pairs the shared constant takes one antipodal value and one orthogonal value.

**S7.** If `a, b ≥ 0` and `a + b < 1`, the larger root of `λ² = aλ + b` is below 1, so the distance decays and two invariant laws must agree.

## Verdict

The partial result survives. One invariant law is certified through `p = 5.26`, and not by this constant at `5.27`.
