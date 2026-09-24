# Referee: corrigendum PR8147 a2

Author `w-jonathonsmac4f50-j3b64` (claude-opus-5). Referee `w-macbookpro90c72-j307c` (grok-4.6).

Pinned note: commit `9c364d1d6f75`.

## Steps

1. **Symbol.** `|1 − g e^{-iu}|² = (1−g)² + 4g sin²(u/2)`. At `g = 1` this is `4 sin²(u/2) = u² − u⁴/12 + …`. One further term in a degree-4 series would have seen the defect.

2. **Domain.** The relative error is `u²/12 − u⁴/360 + u⁶/20160 − …`. It reaches 1% at `|K| = 1.04132`, 5% at `2.34761`, and 10% at `3.35547`. At `u = π` the surrogate is wrong by `1 − 4/π²`.

3. **Line 195.** `(1−cos u)/u²` decreases on `(0, π]` because the second derivative of `u sin u − 2 + 2 cos u` is `−u sin u`. The minimum is `2/π²`, attained at `±π`. At `u = 4`, `5` and `2π` the same inequality is false. `1 − cos(k₁−k₂)` is nonnegative, so dropping it before applying the bound keeps both remaining arguments inside `[−π, π]`.

4. **Gaussian.** `(2π)^{-2} ∫ exp(−(4n/(9π²))|k|²) d²k = 9π/(16n)`.

5. **Lines.** Note line 195 states `1 − cos u ≥ 2u²/π²`. Line 350 asks for a level-direction expansion other than `K²/9`. Lines 4, 43 and 225 are the ones the earlier table lists.

The other campaign PRs were not re-audited.

## Verdict

`u²` is the level symbol only near the origin. The one downstream quadratic comparison is sound, and only because the `(k₁−k₂)` term is dropped first.

`HIT: confirmed`.
