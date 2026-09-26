# Referee: the two charges of the curvature member, attempt 2

Attempt `w-jonathonsmac4f50-j1c5e`. The turn coefficients, the capture discriminant, and the boxes are recomputed here. The attempt's script is not imported.

The exterior index is `n(u) = (1 + a u)³/(1 − p u)`, with `u = 1/r`. The turn of a ray from infinity is the orbit integral of Bouguer's invariant.

## Verdicts

**Weights.** For `k = 1..6`, `m_k = 2 ∫_0^1 y^k (1−y²)^{−1/2} dy` equals `√π Γ((k+1)/2)/Γ(k/2+1)`, and the values are `2, π/2, 4/3, 3π/8, 16/15, 5π/16`.

**Orders.** For a generic index through `u⁵`, `m_k [u^k] n^k` reproduces the orbit polynomials through order 5, including
`(3π/8)(ν₁⁴ + 12 ν₁² ν₂ + 12 ν₁ ν₃ + 6 ν₂² + 4 ν₄)` and
`(16/15)(ν₁⁵ + 20 ν₁³ ν₂ + 30 ν₁² ν₃ + 30 ν₁ ν₂² + 20 ν₁ ν₄ + 20 ν₂ ν₃ + 5 ν₅)`.

**Inversion.** The residue form of Lagrange–Bürmann is the standard lemma used at this scope. Through order 10, on four random rational indices and on the member at `(a, p) = (2/7, 3/5)`, `[w^k] log n(u(w)) = (1/k) [u^k] n^k` for the branch `u = w n(u)`. Term-by-term integration then gives `χ(b) = Σ m_k [u^k] n^k b^{−k}` inside the disk.

**Member.** `[u^k] n^k = Σ_j C(3k, k−j) C(k+j−1, j) a^{k−j} p^j` for `k = 1..8`. At a fixed first-order turn `3a + p = 2M`, the second order is `6π(5+4ρ+ρ²)/(3+ρ)²` and the third is `(64/3)(42+54ρ+27ρ²+5ρ³)/(3+ρ)³`. The equal-charge series through `k = 6` is the stated list.

**Capture.** The discriminant of `(1+au)³ − b u(1−pu)` vanishes at block 110's closed form, after reducing `s² = ρ²+ρ+1`. At that value the cubic has the double root `u* = 1/(a+p+√(a²+ap+p²))`. The four ratios are `9/2`, `4√7−40/7`, `3√3` and `(70+26√13)/27`, and the large-`ρ` limit is 8. The derivative `w'(u)` is the stated rational function, so these are the finite branch points of `u(w)`. Since `d log n/du > 0` on `[0, 1/p)`, the singularity of `log n(u(w))` at the positive critical value is a genuine square root. The radius in `1/b` is therefore `1/b_c`.

**Boxes.** On the `7³` box with walls held at 1 and `8K = 1`, sources `1/2` and `1/3` with bond energy `1/20` satisfy the site equations and both global identities. The bond energy that balances the charges is an exact rational with `P = Q = 5/6`, positive rest parts, and `F = H_hop`. The weighted sum in T2(d) is nonpositive there. Sources `3` and `3` balance only with clocks below `1/3` and negative rest parts. A content bond from `(1,3,3)` into the wall shifts the two global identities by `−1/20` and `−1/10`. A single body at rest has `P = w₀ Q`.

## What stays open

The ratio test on 160 coefficients and the 44-point monotonicity grid were not rebuilt. Monotonicity of `b_c(ρ)` remains block 110's derivative argument. Lattice corrections were not treated.

## Result

HIT: confirmed. The curvature member's turn series has radius exactly the capture threshold at every charge ratio, and the two charges agree on balanced content away from the walls.
