# Referee: lightcone uniqueness region, a1

Author `w-jonathonsmac4f50-j715c` (claude-opus-5). Referee `w-macbookpro90c72-jbd67` (grok-4.6).

## Steps

1. **One-dimensional plan.** The mean of `z` is `A = coth κ − 1/κ`, so `(z−A)q` has mass zero and the positive and negative parts can be coupled. `ω'(x) = x e^x`, so each level is met twice. At `κ = 0` the cost is `∫_0^{1/4} 2√(1−4m) dm = 1/3`.

2. **Margin at the origin.** `8/135 − 1/45 = 1/27`. A trapezoid at `κ = 1/20` and `1/10` sits on `8/135` to `10^{-4}`. That is a quadrature, not a remainder bound.

3. **Fourteen couplings.** A right-endpoint Stieltjes sum, with the chord increasing in `ζ₊`, lies strictly below `A/κ` at each of the 14 values in `[1/10, 3]`. The gaps between those values are not filled.

4. **`A/κ` decreases.** `κA' − A` has the sign of `cosh x − 1 − x²/4 − (x/4) sinh x` at `x = 2κ`. Every Taylor coefficient of that function is `(2−m)/(4m(2m−1)!)`, hence non-positive. So `A/κ ≤ 1/3`.

5. **What is not proved.** Mixed directions are untouched, so the sitewise region stays `3/10`, not `3/7`. The conditional comparison `3/7 > √3/7` is only arithmetic. The scan logs were not re-read.

## Verdict

The parallel bound and the fourteen strict inequalities survive. The full directional lemma does not.

`HIT: confirmed`.
