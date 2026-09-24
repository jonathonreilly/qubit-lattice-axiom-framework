# The persistent-record threshold in 3D: the density branch is real on every coordinate plane, and in the long-memory limit it first leaves the real line on the body diagonals

Attempt 2 of 2. Worker `w-macbookpro9927a-j59b0` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory; they run in about 3 s.
- The exact parts are sympy identities and exact signs.
- Three items are marked as floating point. They are evidence only, not proof.

## Sources, provenance and route

**Sources.**
- Block 96 (#8866, head `111143f765`), T2: `M(k) = E(k)T`, `E = diag(e^{−ik·d})` over `d = ±e_j`, `T = pI + q(J − I)`, `q = (1 − p)/5`; the line threshold; conjugation symmetry.
- Attempt 1 (`w-jonathonsmac4f50-j0e93`, another machine, same model family, not refereed): the axes and the body diagonal.

Check family Q confirms 7 quoted lines verbatim.

**Attempt 1's results.**
- On the axes the density branch is real and leading for every `κ`.
- On the body diagonal the branch is non-real iff `|sin κ| > 3(1 − p)/(3p + 2)`.
- It lists three open items: general directions, with the face diagonal only scanned in floating point; whether the body diagonal is extremal; and `p ≤ 1/6`.

**This attempt's route.** I formed my plan before opening attempt 1's files and did not build on them, since they are not refereed. I take the open directions.
- An exact reformulation of the secular equation as a sum of Poisson kernels.
- A proof covering every direction in the three coordinate planes, which includes the face diagonal.
- The long-memory limit in every direction, with the body diagonal proved extremal.
- One exact fact about the zone corner of the face diagonal.

The body-diagonal threshold falls out of the Poisson form in one line, as a cross-check of attempt 1.

I have no earlier unit on this problem.

## (1) Statement

Take `p ∈ (1/6, 1)`, and set `a = p − q = (6p − 1)/5 > 0` and `r = a/λ`. The claims are:

- **T0 (Poisson form).**
  - A real `λ > a` is a multiplier iff `F(r) := Σ_{j=1}^{3} P(r, κ_j) = (2 + 3p)/(1 − p)`, where `P(r, κ) = (1 − r²)/(1 − 2r cos κ + r²)` is the Poisson kernel.
  - The level `(2 + 3p)/(1 − p)` exceeds 3, and `F(0) = 3`.
- **T1 (every coordinate plane).**
  - Suppose one component of `k` is `0 (mod 2π)`. This covers the axes, the face diagonals and every direction between them.
  - Then for every such `k` and every `p ∈ (1/6, 1)` the density branch is the unique real multiplier above `a`, and it is simple.
  - It never leaves the real line.
- **T2 (body diagonal, from T0).**
  - `F = 3P(r, κ)` and `max_r P = 1/|sin κ|` when `cos κ > 0`.
  - So the branch is real iff `|sin κ| ≤ 3(1 − p)/(3p + 2)`, which is attempt 1's threshold.
- **T3 (long memory, every direction).** Let `ε = 1 − p → 0` with `k = εK n̂`.
  - The secular equation tends to `g_n(σ) := Σ_j 2σ/(σ² + n_j²) = 5K`.
  - The density branch is real iff `5K ≤ m_o(n)`, the value of `g_n` at its outermost local maximum. The boundary is infinite (never reached) on the coordinate planes.
  - `K*(n) = m_o(n)/5 ≥ 3√3/5`, with equality only on the body diagonals.
  - So in the long-memory limit the density branch first leaves the real line on the body diagonals. The memory length is anisotropic, and is infinite in the planes.
- **T4 (zone corner of the face diagonal, `k = (π, π, 0)`).**
  - The cubic there is `(λ + a)(λ² + 2qλ − a² − 6qa)`.
  - Its negative root exceeds the density root in modulus by exactly `2q`.
  - So near the corner the leading multiplier is not the density branch. There it can be non-real while the density branch is real (floating point).

## (2) Steps

**S0 — ASSUMED.** Block 96's T2 objects as supplied, and `p ∈ (1/6, 1)`. Nothing else.

**S1 — T0 — PROVED, CHECKED (L).**
- `T = aI + qJ`, with `a + 6q = 1`.
- `det(λ − E(aI + qJ)) = Π_d(λ − ae_d)·(1 − qΣ_d e_d/(λ − ae_d))`. This is an exact identity for six free `e_d` (the rank-one determinant formula).
- For real `λ > a`, no `ae_d` equals `λ`, since `|ae_d| = a`. So `λ` is a multiplier iff `1 = qΣ_d e_d/(λ − ae_d)`.
- A pair `e_{±e_j} = e^{∓iκ_j}` contributes `(2λc − 2a)/(λ² − 2aλc + a²)`, which equals `(P(a/λ, κ_j) − 1)/a`.
- The equation becomes `Σ_j P = 3 + a/q = (2 + 3p)/(1 − p)`, which is `> 3` iff `p > 1/6`.

**S2 — T1 — PROVED, CHECKED (I).**
- `dP/dr = P(AP − B)/(rA)`, with `A = 1 − r²` and `B = 1 + r²`. This depends on `P` and `r` only.
- So `F′ = Σ_j ψ(P_j)/(rA)`, with `ψ(x) = Ax² − Bx` convex.
- Let `κ_3 = 0`, so `P_3 = P₀ = (1 + r)/(1 − r)` and `ψ(P₀) = 2rP₀`.
- Convexity gives `ψ(P_1) + ψ(P_2) ≥ 2ψ(S/2)`, where `S = F − P₀`. So `Σψ ≥ Q(S) = 2rP₀ + AS²/2 − BS`.
- If `F ≥ 3`, then `S ≥ X := 3 − P₀ = (2 − 4r)/(1 − r)`.
- **Case `r ≥ 1/4`.**
  - The `S`-discriminant of `Q` is `ω(r) = r⁴ − 4r³ − 6r² − 4r + 1`.
  - `ω(1/4) = −111/256`, and `ω` decreases on `[0, 1]`, since `ω′ = 4r³ − 12r² − 12r − 4 < 0` there.
  - So `Q > 0` for every `S`.
- **Case `r ≤ 1/4`.**
  - `Q(X) = 12r³/(1 − r) > 0`.
  - `X` lies above the vertex `B/A`, because `(X − B/A)(1 − r²) = 1 − 2r − 5r²`, which is `3/16 > 0` at `r = 1/4` and decreasing.
  - So `Q(S) ≥ Q(X) > 0` for `S ≥ X`.
- Hence for `r ∈ (0, 1)`, `F(r) ≥ 3` implies `F′(r) > 0`.
- Now use `F(0) = 3`, `F → ∞` as `r → 1` (from the `P₀` term) and a level `L > 3`. The level is crossed exactly once, where `F′ > 0`. Once `F` reaches `L`, it can never return to 3 without a point where `F ≥ 3` and `F′ ≤ 0`.
- The corresponding `λ = a/r` is the unique real multiplier above `a`. It is simple, because `dF/dλ = −(a/λ²)F′ ≠ 0` and `Π(λ − ae_d) ≠ 0` there. By continuity from `λ = 1` at `k = 0`, it is the density branch.
- Floating point: on a grid, the minimum of `F′` where `F ≥ 3` is `> 0`.

**S3 — T2 — PROVED, CHECKED (B).**
- `∂_r P = 0` at `r* = (1 − |sin κ|)/cos κ`, where `P = 1/|sin κ|`.
- For `cos κ ≤ 0`, `P ≤ 1`, so `F ≤ 3 < L` and there is no real root above `a`.
- The density branch, the first crossing of the unimodal `3P`, exists iff `3/|sin κ| ≥ (2 + 3p)/(1 − p)`.

**S4 — T3, the limit — PROVED, CHECKED (S).**
- Put `λ = 1 − εΛ`, `a = 1 − 6ε/5`, `q = ε/5` and `e_d = e^{−iεK n·d}`.
- Each pair of the secular sum tends exactly to `(1/5)·2s/(s² + K²n_j²)`, with `s = 6/5 − Λ` (a symbolic limit).
- With `σ = s/K`, the limit equation is `g_n(σ) = 5K`.
- At `K → 0` the density root is at `σ → ∞`. It follows the outer decreasing branch of `g_n` until `5K` reaches the value at the outermost critical point, where it merges with its neighbour and leaves the real line.

**S5 — T3, the coordinate planes — PROVED, CHECKED (S).**
- In the variable `t = n_j²`, each term has `∂_σ[2σ/(σ² + t)] ≤ 1/(2σ²)`, because `1/(2σ²) − ∂_σ[…] = ((t − σ²)² + 4σ⁴)/(2σ²(σ² + t)²) > 0`. The `t = 0` term gives `−2/σ²`.
- With one `t_j = 0`: `g_n′ ≤ −1/σ² < 0`.
- So `g_n` is strictly decreasing, and the level `5K` is crossed once, simply, for every `K`.

**S6 — T3, the body diagonal is extremal — PROVED, CHECKED (S).**
- Critical points of `g_n` solve `h(v) = Σ_j f(t_j) = 0`, with `f(t) = (t − v)/(v + t)²` and `v = σ²`.
- `f″(t) = −(10v − 2t)/(v + t)⁴ < 0` for `t < 5v`. For `v ≥ 1/3` this covers all `t ∈ [0, 1]`.
- Jensen (concave, `Σt_j = 1`) then gives `h(v) ≤ 3f(1/3) = 3(1/3 − v)/(v + 1/3)² ≤ 0`, with equality only at `v = 1/3` on the diagonal. So every critical point has `σ² ≤ 1/3`: `σ_o ≤ 1/√3 = σ_d`.
- `g_n` decreases on `(σ_o, ∞)`, and `σ_d ≥ σ_o`. So `m_o = g_n(σ_o) ≥ g_n(σ_d)`.
- `t ↦ 2σ/(σ² + t)` is convex (second derivative `4σ/(σ² + t)³`). Jensen gives `g_n(σ_d) ≥ g_diag(σ_d) = 3√3`, with equality iff `t = (1/3, 1/3, 1/3)`.
- So `K* ≥ 3√3/5`, with equality only on the body diagonals. `3√3/5` is the scaled version of attempt 1's leading term `κ* ≈ (3/5)(1 − p)` for `|k| = √3 κ`.
- Floating point: the limiting `K*` over 400 random directions is never below `3√3/5`.

**S7 — T4 — PROVED, CHECKED (C).**
- On the face diagonal the cubic is `(λ − a)D − 2q[2(λc − a)(λ − a) + D]`, with `D = λ² − 2aλc + a²`.
- At `c = −1` it factors as stated.
- The roots are `−a` and `λ_± = −q ± √(q² + a² + 6qa)`, with `λ_+ + λ_− = −2q`.
- Floating point, `p = 9/10`: along the face diagonal near the corner, the leading multiplier is a non-real pair while the density branch (the unique real multiplier above `a`) is real.

## (3) Where the route stops

- **T3 concerns the limiting equation.** That the finite-`p` thresholds divided by `ε` converge to `K*(n)` is the usual continuity at a simple fold. It is not proved here; attempt 1's body-diagonal series agrees with it.
- **Finite `p` off the planes.** An exact threshold surface for general off-plane directions is not given; it is the first local maximum of `F` reaching the level. At finite `p` the body diagonal's extremality is only floating-point evidence (block 96's grid, attempt 1, my scans).
- **Leading versus density near the zone corner.** On the face diagonal the leading multiplier is a different branch and can be non-real. Its exact interval is not computed. It is the set where the negative pair is complex and the density root `r < a^{2/3}`, because the cubic's roots multiply to `a²`.
- **`p ≤ 1/6`** is not treated. `T0`'s level is then `≤ 3` and `a ≤ 0`.

## (4) What would finish it

1. **The finite-`p` extremality of the body diagonal.** Prove that the first local maximum of `F_n(r)` on `(0, 1)` is at least `max_r F_diag(r)` at equal `|k|`. The convexity of `P` in `cos κ` and of `cos(K√t)` in `t` gives `F_n ≥ F_diag` pointwise. What is missing is the location of `F_n`'s first local maximum.
2. **The exact interval near the face-diagonal corner** where the leading multiplier is non-real. It is two polynomial conditions in `(cos κ, p)`.
3. **The convergence of the finite-`p` boundary** to the `K*(n)` surface.
