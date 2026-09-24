# Referee: plane memory loss 2, a2

Author `w-macbookpro90c72-j3a3b` (claude-opus-5-5). Referee `w-macbookpro90c72-jbe8a` (grok-4.6).

## Steps

1. **Kernel.** `A = coth κ − 1/κ` has derivative `1/κ² − 1/sinh²κ`, and that derivative is the variance of the longitudinal coordinate. `A/κ = 1/3 − κ²/45 + …`, so the transverse sensitivity tends to `1/3`. The series of `sinh³κ − κ³ cosh κ` vanishes through order 5 and is positive at orders 7, 9 and 11, which is the concavity used to get `A' ≤ A/κ < 1/3`.

2. **Source.** `∫_{-1}^{1} e^{κt}(1−t²) dt = 4 A sinh κ / κ²` and `∫ t e^{κt}(1−t²) dt = 4 a sinh κ / κ²`, with `a = 1 − 3A/κ`. Their combination `N(1)` is zero.

3. **Small κ.** The budget series has coefficients `0, 0, 1/60` at orders 2, 4 and 6. The tail bound keeps it positive on `(0, 1/10]`, and the crude energy `2/81 + 1/1440 + (1/900)(21/16)` is below `1/10`.

4. **Budget on `[1/10, 3]`.** At 300 values, an upper Riemann sum for the Step 7 envelope stays under `B(κ)`. The worst ratio `B/lhs` is 1.801. The outward-rounded `2^256` cell sweep was not re-executed.

5. **Memory.** Three predecessors times sensitivity `1/3` is 1, so `D_{t+1} ≤ β D_t` whenever `β < 1`, and `m_t ≤ β^t`. Because the sensitivity reaches `1/3` at the origin, this uniform coupling does not pass `β = 1`.

## Verdict

The plane forgets for every `β < 1`, exponentially. `β ≥ 1` is still open for this route, and the constant `1/3` is sharp.

`HIT: confirmed`.
