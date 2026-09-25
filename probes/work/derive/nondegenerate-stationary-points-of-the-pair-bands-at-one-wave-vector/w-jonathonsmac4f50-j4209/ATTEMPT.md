# Certifying (A'): nondegenerate stationary points of the pair bands at one total wave vector — attempt a2

Worker `w-jonathonsmac4f50-j4209`, model `claude-opus-5-5`.

**Provenance.**
- Block 143 (PR #9229, open) is the supervisor's own derivation, the same model family, and is not refereed by another family.
- This attempt certifies only its assumption (A'). It uses nothing else from block 143.
- No prior attempt was printed at claim time. The referee should be of another family.

## 1. Statement attempted

**(A') at one `K₀`.** Take `ε(k) = (Σ_a sin² k_a)^{1/2}` and the four band functions
`E(q) = s₁ε(K₀/2 + q) + s₂ε(K₀/2 − q)`, `s₁, s₂ = ±1`.
At one `K₀` with rational half-angle tangents, every stationary point of each band function on the torus, away from the cone points where `ε` vanishes, is nondegenerate.

**Reduction.**
- Stationary points solve `∇ε(k₁) = σ∇ε(k₂)`, with `k₁ = K₀/2 + q`, `k₂ = K₀ − k₁` and `σ = s₁s₂`.
- The pairs `(s₁, s₂)` and `(−s₁, −s₂)` give `E` and `−E`, so there are two systems, `σ = ±1`.

**Result.**
- **Z²**, at `K₀ = (2 atan(1/3), 2 atan(2/3))`: **16** nondegenerate stationary points for `σ = +1` (bands `(+,+)`, `(−,−)`) and **8** for `σ = −1` (bands `(+,−)`, `(−,+)`). There are no other stationary points away from the cone points.
- **Z³**, at `K₀ = (2 atan(1/3), 2 atan(2/3), 2 atan(1/4))`: **64** nondegenerate stationary points for `σ = +1` and **48** for `σ = −1`, with no others away from the cone points.

## 2. Steps

1. **PROVED — reduction.**
   - `∇_q E = s₁∇ε(k₁) − s₂∇ε(k₂)`, with `∇ε(k) = (sin k_a cos k_a/ε)_a`. Stationarity is `∇ε(k₁) = σ∇ε(k₂)`.
   - `Hess_q E = s₁ Hess ε(k₁) + s₂ Hess ε(k₂)`, which is `s₁` times the Jacobian of `G := ∇ε(k₁) − σ∇ε(k₂)` with respect to `k₁`.
2. **PROVED — charts.**
   - Each coordinate of `k₁` is covered by `t = tan(k/2) ∈ [−1, 1]` (`k ∈ [−π/2, π/2]`) and `u = cot(k/2) ∈ [−1, 1]` (`k ∈ [π/2, 3π/2]`). There are `2^d` chart boxes.
   - `sin k = 2t/(1+t²)`, `cos k = ±(1 − t²)/(1+t²)`, and `sin(K₀ − k)`, `cos(K₀ − k)` are rational in `t`, because `tan(K₀,a/2)` is rational.
   - Each chart map is a diffeomorphism, with `dk/dt = 2/(1+t²)` and `dk/du = −2/(1+u²)`. So `det(∂G/∂t) ≠ 0` iff `det Hess_q E ≠ 0`.
3. **CHECKED — exact interval arithmetic.**
   - Intervals are pairs of Fractions, with every operation rounded outward to the grid `2^−96`.
   - Square roots are enclosed by integer square roots.
   - Forward-mode derivatives carry interval gradients, which gives an interval Jacobian `∂G/∂t` on any box.
   - No floating-point number enters a certified inequality. Floating-point Newton iteration is used only to seed the root boxes.
4. **CHECKED — each root: a Krawczyk test.**
   - Around each numerically found root, a box of radius `2⁻¹⁴` in chart coordinates is used, in every chart that contains the root.
   - `K(X) = x̃ − Y G(x̃) + (I − Y J(X))(X − x̃)` lies strictly inside `X`, with `Y` a rational approximate inverse. So `X` contains exactly one zero.
   - The interval determinant of `J(X)` excludes 0, so that zero is nondegenerate.
   - The root boxes within each chart are pairwise disjoint.
5. **CHECKED — elsewhere: exclusion by subdivision.** Each chart box `[−1, 1]^d` is bisected until every sub-box is either:
   - contained in a root box; or
   - cleared because some component of `G` excludes 0; or
   - cleared by a **division-free magnitude test** near the cone points.
   - The magnitude test: `|∇ε(k)|² = 1 − Σ sin⁴k_a/Σ sin²k_a` lies in `[1 − max_a sin²k_a, 1 − ε²/d]`, by Cauchy–Schwarz.
     - If `1 − max sin²(k₁) > 1 − ε(k₂)²/d` on the box (or the same with 1 and 2 exchanged), then `|∇ε(k₁)| ≠ |∇ε(k₂)|`, so there is no solution there.
     - This clears neighbourhoods of the cone points, where `G` is undefined.
     - `k₁` and `k₂ = K₀ − k₁` are never both cone points, because `K₀ ∉ {0, π}^d`.
   - Zero boxes remained uncleared at the stopping width `2⁻⁴⁰`.
6. **CHECKED (C1) — Z².**
   - 16 roots for `σ = +1`: smallest `|det ∂G/∂t|` lower bound 1.55.
   - 8 roots for `σ = −1`: smallest bound 3.28.
   - Exclusion used 14 420 and 2 932 boxes. About 25 s.
   - This agrees with the task's floating-point search (16, 8, 8, 16 at another `K₀`).
7. **CHECKED (C2) — Z³.** The same certificate at `K₀ = (2 atan(1/3), 2 atan(2/3), 2 atan(1/4))`, with 8 chart boxes and 3×3 Krawczyk tests:
   - 64 roots for `σ = +1` (smallest determinant lower bound 1.03) and 48 roots for `σ = −1` (2.90);
   - 252 040 and 160 712 exclusion boxes, none uncleared;
   - about 19 minutes;
   - the counts agree with the task's floating-point search (64, 48, 48, 64 at another `K₀`).

## 3. First failing step

None, for the stated certificate.

**Scope.**
- (A') at the one `K₀` above. Persistence to a neighbourhood of `K₀` is the standard fact that nondegenerate zeros persist, which block 143 invokes. It is not re-checked here.
- The cone points themselves are excluded, as (A') states.

## 4. What would finish it

Block 143's T5 needs (A') at some `K₀`; this supplies it on Z² and on Z³.

A referee should check:
- the chart covering;
- the magnitude bounds;
- the Krawczyk inclusion argument;
- that the interval arithmetic rounds outward in every operation, including the integer-square-root enclosures.
