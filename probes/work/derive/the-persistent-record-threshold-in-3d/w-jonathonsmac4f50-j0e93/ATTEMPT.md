# The persistent-record threshold in 3D — attempt 1

Worker `w-jonathonsmac4f50-j0e93`, model `claude-opus-5-5`. Block 96 (#8866) was written by the campaign supervisor, who is from the same model family (Claude). A referee from another family should check the steps. No prior attempt was printed at claim time.

## 1. Statement

The setting is block 96 T2. A record keeps its direction with probability `p` and otherwise turns to one of the other five directions.

- **Mode matrix.** `M(k) = E(k) T`, with `E = diag(e^{−ik·d})` over the six directions `d = ±e_j` and `T = pI + q(J − I)`.
- **Constants.** `q = (1−p)/5` and `a = p − q = (6p−1)/5`.
- **Useful form.** `T = aI + qJ`, and `a + 6q = 1`.

Let `p ∈ (1/6, 1)`, so that `a ∈ (0, 1)`.

**(a) Body diagonal, `k = κ(1,1,1)`.**
- The density branch is the multiplier that equals 1 at `k = 0`.
- It is also the leading multiplier.
- It is non-real exactly when `|sin κ| > 3(1−p)/(3p+2)`.
- Compare the line (block 96 T2.1), where the condition is `|sin k| > (1−p)/p`.

**(a) Axes, `k = (κ,0,0)` and its images.**
- For every `κ ∈ [0, π]` the density branch is real and simple, and it is the unique multiplier above `a`.
- The leading multiplier is real for every `κ`.
- So there is no threshold on the axes.

**(b) Small `1 − p`.**
- `κ* = arcsin(3(1−p)/(3p+2)) = (3/5)(1−p) + (9/25)(1−p)² + O((1−p)³)`.
- The memory length per coordinate is therefore `≈ 5/(3(1−p))`, and `|k*| ≈ 3√3(1−p)/5`.

## 2. Steps

**0 (CHECKED).**
- `T = aI + qJ` and `a + 6q = 1`.
- Hence `M = aE + q e 1ᵀ`, where `e = E1`: a diagonal matrix plus rank one.
- If `λ` is not one of the `a e_d`, it is an eigenvalue iff `1 = q Σ_d e_d/(λ − a e_d) = q Σ_d 1/(λ ē_d − a)`, which is the secular equation.

**A1 (CHECKED).** On the axis the full characteristic polynomial factorises exactly (with `z = e^{−iκ}` as a symbol) as `det(λ − M) = (λ − a)³ P(λ)`.
- The factor `(λ − a)³` comes from the vectors that are supported on the four transverse directions and sum to zero.
- `P` is the cubic `λ³ − ((10cp + 2p + 3)/5)λ² + (6p−1)(2cp + 8c + 4p + 1)λ/25 − (6p−1)²/25`, with `c = cos κ`.

**A2 (PROVED, CHECKED).**
- `P = (λ − a) D (1 − qG)`, where `D = λ² − 2aλc + a² = |λe^{iκ} − a|²`.
- Here `G(λ) = 4/(λ − a) + 2 Re 1/(λe^{iκ} − a)` is the secular function for real `λ`.
- `D = (λ − a)² + 2aλ(1 − c)`, so `D ≥ (λ − a)² > 0` for `λ > a > 0`.

**A3 (PROVED, CHECKED): G is strictly decreasing on (a, ∞).**
- `G′ = −4/(λ − a)² − 2N/D²`, where `N = λ²c − 2aλ + a²c = Re[e^{−iκ}(λe^{iκ} − a)²]`.
- `D² − N² = (1 − c²)(λ² − a²)² ≥ 0`, so `|N| ≤ D`.
- Hence `|2N/D²| ≤ 2/D ≤ 2/(λ − a)²`, and `G′ ≤ −2/(λ − a)² < 0` on `(a, ∞)`.

**A4 (PROVED, CHECKED): one root above a, and it is the density branch.**

*Behaviour of `G` on `(a, ∞)`.*
- As `λ → a⁺`, `G → +∞`: the pair term has the finite limit `−1/a` when `c ≠ 1`.
- As `λ → ∞`, `G → 0`.

*Consequences.*
- Since `1/q > 0`, `G = 1/q` has exactly one solution `r(κ)` in `(a, ∞)`. It is simple because `G′ ≠ 0`.
- The prefactor `(λ − a)D` is positive there, so `r(κ)` is the unique root of `P` in `(a, ∞)`, and it is simple.
- Also `P(a) = −8qa²(1 − c) < 0`.

*Identification with the density branch.*
- At `κ = 0` this root is 1, the density branch.
- A simple root depends continuously on the coefficients.
- So the density branch is `r(κ)` for all `κ ∈ [0, π]`: real, simple, and `> a`.

**A5 (PROVED, CHECKED): the leading multiplier on the axis is real.** Write `a = t³` with `t ∈ (0, 1)`.

*Sign of `P(t²)`.*
- `P(t²) = (t⁴/5)[t(2cp + 8c + 4p + 1) − (10cp + 2p + 3)]`.
- The bracket is linear in `c`.
- At `c = 1` it equals `5(t−1)³(t+1)`.
- At `c = −1` it equals `(5/3)(t−1)(t+1)(t² + 4t + 1)`.
- Both are negative for `t ∈ (0, 1)`, so `P(t²) < 0` for all `c ∈ [−1, 1]`.

*Consequences.*
- `P < 0` on `(a, r)` and `t² = a^{2/3} > a`, so `r > a^{2/3}`.
- Suppose the other two roots `z, z̄` of `P` are non-real. The product of the roots is `a²`, so `|z|² = a²/r < a^{4/3} < r²`, i.e. `|z| < r`.
- The multiplier `a` (three times) is below `r`.
- So when the pair is non-real, the leading multiplier is `r`, which is real. When all three roots of `P` are real, the leading multiplier is real anyway.

**A6 (CHECKED): agreement with block 96's executed statement.** At `(π/2, 0, 0)` with `p = 9/10`:
- `P(9/10) < 0 < P(1)`;
- the discriminant is negative;
- so there is one real root, in `(9/10, 1)`, and two non-real ones.

**A7 (CHECKED): where the other pair becomes real.** At `κ = π` the discriminant of `P` is `64(1−p)²(6p−1)²(p² + 28p − 4)/15625`. This is positive for `p > 10√2 − 14 ≈ 0.142`, so near the zone edge all three roots are real. The pair that starts at the double root `a` (at `κ = 0`) returns to the real line there. The density root stays the only root above `a`.

**B1 (CHECKED).** On the diagonal the characteristic polynomial factorises exactly as `det(λ − M) = (λ − az)²(λ − a/z)² Q(λ)`, with `Q = λ² − 2λc(3p+2)/5 + (6p−1)/5`.
- The first factors come from the sum-zero vectors inside the two triples `{+e_j}` and `{−e_j}`.
- At `κ = 0` the roots of `Q` are 1 (the density branch) and `a`.

**B2 (PROVED, CHECKED): the threshold.** The quarter-discriminant of `Q` is `[9(1−p)² − sin²κ (3p+2)²]/25`, using `(3p+2)² − 5(6p−1) = 9(1−p)²`. So the density branch is non-real iff `|sin κ| > 3(1−p)/(3p+2)`. The threshold lies below the zone edge iff `p > 1/6`.

**B3 (PROVED, CHECKED): the leading multiplier leaves the real line exactly there.**
- Where the roots of `Q` are non-real, their modulus is `√a`, since the product is `a`. This exceeds the modulus `a` of the other four multipliers `a e^{±iκ}`.
- Where they are real, the larger root is at least `√a > a`.

**B4 (CHECKED): scaling.**
- `κ* = arcsin(3ε/(5 − 3ε))` with `ε = 1 − p`.
- Its series is `3ε/5 + 9ε²/25 + 63ε³/250 + …`.

**B5 (CHECKED): agreement with block 96 W2's 24³ grid.** The diagonal grid points are `κ = nπ/12`.
- At `p = 9/10` and `99/100` the first point, with `|k| = 0.453`, is already past the threshold. This matches "non-real from |k| = 0.45".
- At `p = 1/2` the first point is real and the second, with `|k| = 0.907`, is not. This matches "real for |k| < 0.8".

**C (CHECKED).** The line's discriminant reproduces block 96 T2.1.

## 3. First failing step

None.

## 4. Not claimed, and what would finish it

1. **General directions.** Along the face diagonal, a floating-point scan finds the density branch real for all `κ`, at `p = 0.5, 0.9, 0.99`. The axis proof does not apply there, because the pair term has weight 4 against weight 2. This is executed only, not claimed.
2. **Is the body diagonal extremal?** Whether it gives the smallest `|k*|` over all directions is open, as is the shape of the region where the leading multiplier is non-real.
3. **`p ≤ 1/6`.** On the diagonal all multipliers of `Q` are real, because the discriminant is `≥ 0` when `a ≤ 0`. The axis argument needs `a > 0`, so the axes are not covered there.

ASSUMED: nothing. Only block 96's definitions are used.
