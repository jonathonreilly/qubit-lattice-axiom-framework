# The two charges of the curvature member — attempt a2

Worker `w-jonathonsmac4f50-j1c5e`, model `claude-opus-5-5`.

**Provenance.**
- Block 110 was written by the supervisor, the same model family (Claude).
- T2, which part (c) checks, was first derived in the probes by `bound-bodies-and-the-two-far-fields` a1 (another machine) and a2 (`w-jonathonsmac4f50-ja0f7`, this machine, the same family).
- This attempt re-derives T3 and T4 by routes of its own and builds its own box examples.
- No prior attempt on this problem was printed at claim time.
- The referee should come from another family.

**Sources, as landed on main.**
- Block 110: `docs/ADMISSIBILITY_RULE_AROUND_A_BODY_..._2026-09-24.md`, landed after PR #8960 was closed.
- Block 60: `docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_..._2026-09-21.md`.
- Where the task paraphrases, the landed wording is used.
- The ray model is block 110's declared long-wave model `E = (w/ℓ)|k|` in the continuum exterior, which is conditional as landed. No lattice statement is made.

## 1. Statements attempted

**S1 (every order).**
- Setting: an index `n(u)`, `u = 1/r`, analytic at `u = 0` with `n(0) = 1`.
- Let `u(w)` be the root of `u = w n(u)` with `u(0) = 0`, and let `R` be the radius of convergence of `g(w) = log n(u(w))`.
- For `1/b < R`, the turn of the rays is
  `χ(b) = Σ_{k≥1} m_k [u^k] n(u)^k b^{−k}`, with `m_k = √π Γ((k+1)/2)/Γ(k/2 + 1)` (2, π/2, 4/3, 3π/8, 16/15, 5π/16, …).
- The series converges for `1/b < R` and diverges for `1/b > R`.

**S2 (the member).** For `n = (1 + au)³/(1 − pu)`:
- `[u^k] n^k = Σ_{j=0}^{k} C(3k, k−j) C(k+j−1, j) a^{k−j} p^j`.
- This gives block 110 T4's four listed coefficients and T5's tree series.
- At `a = p = M/2` it gives `4, 15π/4, 128/3, 3465π/64, 3584/5, 255255π/256` for `k = 1..6`.
- At a fixed first-order turn (`3a + p = 2M`, `ρ = p/a`) it gives the third-order term `(64/3)(42 + 54ρ + 27ρ² + 5ρ³)/(3 + ρ)³ (M/b)³`.

**S3 (capture, by the discriminant).**
- The turning points are the roots in `(0, 1/p)` of `E_b(u) = (1 + au)³ − b u (1 − pu)`.
- The capture threshold is the root of `Disc_u E_b` at which the smallest positive root becomes double, at `u* = 1/r*`, `r* = a + p + √(a² + ap + p²)`.
- It equals block 110 T3's closed form.

**S4 (the radius, answering (b)).** For `a, p ≥ 0`, not both zero, the turn series in `M/b` has radius exactly `M/b_c` at every charge ratio `ρ ∈ [0, ∞]`. It converges for `b > b_c` and diverges for `b < b_c`.

**S5 (answering (c)).** On exact 7×7×7 boxes, T2's charge formulas hold, and so do the global identities of T2(e) for content away from the walls. Specifically:
- a balanced content with positive rest parts has `P = Q` exactly;
- strong sources force clocks below 1/3, and balance then needs negative rest parts;
- one content bond into a held wall breaks both global identities, as T2(e)'s hypothesis says.

## 2. Steps

1. **PROVED — the orbit integral.**
   - Bouguer's invariant `r n sin ψ = b` (block 110 T1 as landed) with `tan ψ = r dφ/dr` gives `(dr/dφ)² = r²(r²n²/b² − 1)`.
   - With `u = 1/r`, this is `(du/dφ)² = n²/b² − u²`.
   - A ray from infinity that turns at `u0` sweeps `2∫_0^{u0} du/√(n²/b² − u²)`. So the turn is `χ + π = 2∫_0^{u0} du/√(n(u)²/b² − u²)`.
2. **CHECKED (A1, A2) — the direct expansion, the task's route.**
   - Scale `u = εx`, with `ε = 1/b` and `x = x0 v`, where `x0` is the exact turning point: `n(εx0)² = x0²`, a series in ε.
   - Since `n(εx0)² = x0²`, subtracting it from `n(εx0v)²` makes both terms carry the factor `(1 − v)`:
     `n(εx0v)² − x0²v² = (1 − v) x0² [(1 + v) − T(v)]`, with `T(v) = Σ_k c_k ε^k x0^{k−2}(1 + v + … + v^{k−1})` and `n² = Σ c_k u^k`.
   - So `χ + π = 2∫_0^1 (1 − v²)^{−1/2} (1 − T/(1+v))^{−1/2} dv`.
   - Expanded in ε, every term is `∫_0^1 v^m (1+v)^{−j}(1 − v²)^{−1/2} dv`. With `v = cos θ`, `t = tan(θ/2)` this is `∫_0^1 2^{1−j}(1 − t²)^m (1 + t²)^{j−m−1} dt`, a rational integral done exactly.
   - With a generic index `n = 1 + ν₁u + … + ν₅u⁵`, the coefficients of `ε^1..ε^5` are exactly `m_k [u^k] n^k` (A1). Orders 1–3 are block 110 T4's (A2).
   - New at orders 4 and 5:
     - `(3π/8)(ν₁⁴ + 12ν₁²ν₂ + 12ν₁ν₃ + 6ν₂² + 4ν₄)`;
     - `(16/15)(ν₁⁵ + 20ν₁³ν₂ + 30ν₁²ν₃ + 30ν₁ν₂² + 20ν₁ν₄ + 20ν₂ν₃ + 5ν₅)`.
3. **PROVED — the closed form: the pattern of step 2 at every order.**
   - On the outer branch set `w = u/n(u) = 1/(r n)`. `w` increases on `[0, u0]`, because `u0` is the first root of `w = 1/b` and `w(0) = 0`.
   - Then `n²/b² − u² = n²(1/b² − w²)` and `du/n = w d(log u)`.
   - With `log u = log w + g(w)`, `g(w) = log n(u(w))`:
     `χ + π = 2∫_0^{1/b} w (1/w + g'(w)) dw/√(1/b² − w²) = π + 2∫_0^{1/b} w g'(w) dw/√(1/b² − w²)`.
4. **ASSUMED (one standard lemma) and CHECKED (A4) — Lagrange–Bürmann at the scope used.**
   - The lemma (formal residues under a change of variable): for formal Laurent series `f` and `u(w) = w + O(w²)`, `res_w f(u(w)) u'(w) = res_u f(u)`.
   - With it:
     `[w^k] H(u(w)) = (1/k) res_w H'(u(w))u'(w) w^{−k} = (1/k) res_u H'(u) n(u)^k u^{−k} = (1/k)[u^{k−1}] H'(u) n(u)^k`.
   - For `H = log n`: `H' n^k = n' n^{k−1} = (1/k)(n^k)'`, so `[w^k] g = (1/k)[u^k] n^k`.
   - Checked exactly to order 12 on five random rational indices and on the member at `(a, p) = (2/7, 3/5)` (A4).
5. **PROVED — term-by-term integration.**
   - For `1/b < R`, `w g'(w) = Σ_k k λ_k w^k`, with `λ_k = (1/k)[u^k] n^k`, converges uniformly on `[0, 1/b]`.
   - `2∫_0^{1/b} w^k dw/√(1/b² − w²) = b^{−k} 2∫_0^1 y^k (1 − y²)^{−1/2} dy = b^{−k} m_k`.
   - The Beta integral `2∫_0^1 y^k(1−y²)^{−1/2}dy = B((k+1)/2, 1/2)` is ASSUMED as standard and CHECKED for `k ≤ 6` (A3).
   - This gives S1's formula for `1/b < R`.
   - Divergence for `1/b > R`: `m_k ~ √(2π/k)` is subexponential, so `limsup |m_k k λ_k|^{1/k} = 1/R`.
6. **PROVED and CHECKED (A5–A10) — the member.**
   - `n^k = (1 + au)^{3k}(1 − pu)^{−k}`. Cauchy's product of the two binomial series gives S2's sum (A5, `k ≤ 8`).
   - It reproduces block 110 T4's four listed coefficients (A6), the equal-charge series to `k = 6` (A7), and T5's `c_n` for `n = e^{κu}` (A8), since `[u^k] e^{kκu} = (kκ)^k/k!`.
   - It gives T4's second-order term `6π(5 + 4ρ + ρ²)/(3 + ρ)²` (A9).
   - The third-order term at a fixed first-order turn is new (A10): `(64/3)(42 + 54ρ + 27ρ² + 5ρ³)/(3 + ρ)³`. That is `896/27` as `ρ → 0`, `128/3` at `ρ = 1`, and `320/3` as `ρ → ∞`.
7. **PROVED and CHECKED (B1–B4) — capture by the discriminant.**
   - A turning point is a root of `n(u)/b = u` in `(0, 1/p)`, where `N > 0`. That is, `(1 + au)³ = b u (1 − pu)`, a cubic `E_b(u)`.
   - As `b` decreases from `∞`, the smallest positive root `u0(b)` moves continuously until it collides with another root. The first collision is where `E_b` has a double root, a zero of `Disc_u E_b`.
   - Exactly, `Disc_u E_b = −b² [27a²(a + p)² + (4p³ + 6ap² − 6a²p − 4a³) b − p² b²]`.
     - For `p > 0` the bracket is a quadratic in `b` whose roots have product `−27a²(a + p)²/p² < 0`, so it has exactly one positive root: that root is `b_c`.
     - For `p = 0` the bracket is linear in `b`, with root `27a/4`.
   - Block 110 T3's closed form `b_c/M = 2(ρ + s + 2)³/((ρ + 3)(s + 1)(ρ + s + 1))`, with `s² = ρ² + ρ + 1`, is that root: B1 reduces the bracket at the closed form, with `s² = ρ² + ρ + 1`, to exactly 0.
   - At that `b` the double root is `u* = 1/(a + p + √(a² + ap + p²))`, which lies inside `(0, 1/p)` (B2).
   - Values `9/2, 4√7 − 40/7, 3√3, (70 + 26√13)/27` at `ρ = 0, 1/2, 1, 3` (B3), and the limit 8 (B4).
   - Monotonicity was **not re-proved** by this route. The envelope derivative `d(max_u w)/dρ` is negative at 44 grid points in `[0, 1000]` (B5, an exact expression evaluated numerically). Block 110's derivative argument stands as the proof.
8. **PROVED, with CHECKED ingredients (C1–C4) — the radius, S4.**
   - `u(w)` is the branch of the algebraic curve `F(u, w) = w(1 + au)³ − u(1 − pu) = 0` with `u(0) = 0`. It is a simple root at `w = 0`, since `∂_u F(0, 0) = −1`.
   - **The finite branch points** solve `F = ∂_u F = 0`, which is equivalent to `w'(u) = 0` for `w(u) = u(1−pu)/(1+au)³`.
     - `w'(u) = (1 − 2(a+p)u + apu²)/(1 + au)⁴` (C1).
     - The critical points are `u* = 1/(a + p + S)` and `u₋ = 1/(a + p − S)`, with `S = √(a² + ap + p²)`.
     - `u = −1/a` is not a solution of `F = 0` at finite `w`.
     - So the critical values are `w* = 1/b_c > 0` and `w₋ = w(u₋) < 0`, with `u₋ > 1/p` (C2).
   - **The negative axis.** On `(−1/a, 0]`, `1 − 2(a+p)u + apu² > 0` term by term, so `w` increases there from `−∞` to 0 (C3).
     - The principal branch is therefore analytic along the whole negative real axis.
     - At `w₋` it takes a value in `(−1/a, 0)`, a simple root. The sheet that meets `u₋` at `w₋` is a different sheet.
   - **Inside the disk `|w| < w*`.** The only candidate singular point is `w₋`, and only when `|w₋| < w*`.
     - The principal germ continued along the segment `[w₋, 0]` is a simple root at `w₋`.
     - It is therefore analytic in a neighbourhood of `w₋`, with no monodromy.
     - So `u(w)` is single-valued and analytic in the whole disk.
   - **`n` stays finite and nonzero.**
     - `n(u(w)) = 0` needs `u = −1/a`, which is `w = ∞`.
     - `n = ∞` needs `u = 1/p`, which is reached only at `w = 0` by the other sheet.
     - So `g = log n(u(w))` is analytic in the disk.
   - **At `w*`.**
     - `w''(u*) = Q'(u*)/(1 + au*)⁴`, with `Q'(u*) = −2(a + p − apu*) < 0`, because `apu* < a + p`. So `u(w) − u* ~ −c √(w* − w)`, with `c > 0`.
     - `d log n/du = 3a/(1 + au) + p/(1 − pu) > 0` on `[0, 1/p)` (C4). So `g` has a genuine square-root singularity at `w*`.
     - Hence `R = w* = 1/b_c`, and by step 5 the radius of the turn series in `1/b` is `1/b_c`.
   - **Edge cases.** For `a = 0` the curve is the quadratic `w = u(1 − pu)`. For `p = 0` it is `w = u/(1 + au)³`. The same argument applies (`b_c = 4p` and `27a/4`).
   - This matches the refereed probes result for `e^{A/r}` (radius = capture threshold).
9. **CHECKED, floating-point evidence only (C5).** The exact coefficients `[u^k] n^k` up to `k = 160`, at `ρ = 1/2, 1, 3`, give Richardson-extrapolated ratio estimates of the radius that match `b_c/M` to `2·10⁻⁵` relative (the check requires `2·10⁻³`).
10. **CHECKED (D1–D6) — exact boxes for (c).**
    - **Construction.**
      - 7×7×7 box, 125 interior sites, walls held at `χ = N = 1`, `8K = 1`.
      - A source `s > 0` on content sites fixes `χ` by `Δχ = −s`, exact rationals.
      - Content bond energies `B` fix `τ`.
      - The linear system `ΔN + N Δχ/χ = 2τ/(8Kχ)` gives `N` exactly.
      - Then `e = −8K N Δχ` and the rest parts are `e − τ`.
      - This imposes block 110 T2(a)'s site equations by construction. What the box checks is everything downstream.
    - **D1 (generic content).** The wall fluxes `Q`, `P` equal `Σ e/(8Kwχ)` and `Σ (e + 2τ)/(8Kχ)`. `P − Q` equals the site sum. `8KQ = H + F` and `4K(P + Q) = H_rest + 2H_hop` hold exactly.
    - **D2 (a balanced example).** `P` is affine in the bond energy. The exact rational root `B* ≈ 0.10238` gives `P = Q = 5/6` exactly, with:
      - positive rest parts 0.3834 and 0.2451;
      - clocks 0.7657 and 0.8033;
      - `F = H_hop` exactly.
    - **D3.** T2(d)'s weighted bound holds on D2.
    - **D4 (too compact).** Sources 3 and 3 give clocks 0.0683 and 0.0710 at `P = Q`. Balance there needs rest parts −2.226 and −2.212, both negative.
    - **D5 (the wall hypothesis).** One content bond from a site next to a wall into the wall.
      - The site equations and charge formulas still hold.
      - `8KQ − (H + F) = −1/20` and `4K(P + Q) − (H_rest + 2H_hop) = −1/10`, exactly.
      - So T2(e) needs content away from the walls, as block 110 states.
    - **D6.** One body at rest (source 1/2) gives `P = w₀Q` exactly, with `w₀ = 0.8137` (block 60).

## 3. Where a route fails

- No step of (a)–(c) fails.
- The monotonicity of `b_c(ρ)` was not re-derived by the discriminant route (step 7). Block 110's own derivative argument covers it.

## 4. What would finish it, and what is left

- **A referee of another family** for steps 3–5 (the Lagrange form), 7 (the discriminant) and 8 (the radius).
- **The same argument for other indices.** Step 8 extends to any rational index. The radius of the turn series is the modulus of the nearest critical value of `w = 1/(r n)` on the principal sheet, or of a zero or pole of `n` that the principal branch reaches.
  - For the member it is the capture threshold.
  - An index with a complex critical value closer to 0 than the capture threshold would have a radius smaller than capture. None occurs here.
- **Not addressed:** lattice corrections to the exterior, and finite wave numbers (block 110 N1).
