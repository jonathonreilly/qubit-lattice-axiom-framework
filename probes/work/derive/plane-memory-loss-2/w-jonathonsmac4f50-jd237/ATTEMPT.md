# plane-memory-loss-2: derivation attempt 1 of 4

Worker `w-jonathonsmac4f50-jd237` (claude-opus-5), unit `J-derive-plane-memory-loss-2-a1`.

Definitions are from block 26's note (PR #8170, head `f9e11770`):
- L83: space-time, levels `τ(x) = x₁ + x₂ + x₃`, predecessors `x − e_j`, records drawn independently across a level given the previous one;
- L84: the kernel `K_β(ds | S) ∝ e^{β s·S}`, the von Mises–Fisher law `vMF(βS)`, and `A(κ) = coth κ − 1/κ`;
- L85: the magnetization `m_t = E[s_x·e]` from the aligned plane;
- L70: the open item;
- L176 (N1.4): the static-twist attempt.

In plane coordinates, `(x, t) ↔ X = (i, j, t − i − j)` and the predecessors of `X` are `X − e_a`. `check.py` verifies every finite claim exactly. One Monte Carlo is labelled as numerical.

**Provenance and independence.** GIVEN (2) of this round comes from my own referee report on round-1 attempt a3 (`probes/work/derive/plane-memory-loss/referee_w-jonathonsmac4f50-j8129`, claude-opus-5, same model family and machine). That report named a second, order-one "spread" part of the twist cost. It left open "whether some space-time twist makes both parts small". This attempt answers that question for every deterministic site-wise rotation twist, so it is not independent of that report. The round-1 attempts were grok-4.6.

## 1. The statement attempted

**The task:** `m_t → 0` on the infinite plane for every `β`.

**Route A (as posed):**
1. Take a space-time twist `θ(x, t) = θ₀ g_T(x, t)`.
2. **A2:** bound the path-space relative entropy by `C β θ₀²/Σ_{k<T} P_k`.
3. Conclude by the entropy inequality.

What this attempt proves is that step A2 is false.

**Theorem N (site-wise twists have path cost bounded below).**
- Fix `β > 0`, `T ≥ 1` and `p = (0, T)`.
- Let `C(p)` be the backward cone of `p`: the sites at levels `1..T` from which `p` is reached by successor steps. In `Z³` coordinates these are `p − n`, with `n ∈ Z³_{≥0}` and `|n|₁ < T`. `C(p)` together with its level-0 base is closed under taking predecessors.
- Let `θ` be a function on `C(p)` and level 0, with `θ = 0` on level 0 and `θ(p) = θ₀ ∈ [−π, π]`.
- `P` is the formation law from the aligned plane `e = e₃`.
- `P^θ` is the law of `(R_{θ(x,t)} s_{x,t})` with `s ~ P`, where `R_φ` is the rotation by `φ` about `e₁`.
- The space-time XY energy of the twist is `X(θ) := Σ_{(x,t)∈C(p)} Σ_{y ∈ pred(x)} sin²((θ(x, t) − θ(y, t−1))/2)`.

Then:
- **(i)** `c_β X(θ) ≤ H(P^θ|_{C(p)} ‖ P|_{C(p)}) ≤ 2β² X(θ)`, with `c_β = 2β² A'(3β) (A(3β)/(3β) + A'(3β))`.
  - For large `β`, `c_β ≈ 2/(27β)`; for small `β`, `c_β ≈ 4β²/9`.
  - Values: `0.0658`, `0.0247`, `0.0123`, `0.00309` at `β = 1, 3, 6, 24`.
- **(ii)** `X(θ) ≥ θ₀²/(π² E_T)`. Here `E_T ≤ 2T/(T + 1) < 2` is the energy of the Pólya-urn flow from `p` to level 0 inside `C(p)`.
- Hence `H ≥ c_β θ₀²/(2π²)` for every `T`. Since `Σ_{k<T} P_k → ∞` (GIVEN (1)), the bound `C β θ₀²/Σ_{k<T} P_k` fails for every `C` once `Σ_{k<T} P_k > 2π² C β/c_β`. So step A2 is false.
- **(iii)** The lower bound `H ≥ c_β θ₀²/(π² E_T)` extends to every deterministic field `R : C(p) ∪ level 0 → SO(3)` with `R = I` on level 0. There `θ₀ := ∠(R_p e₃, e₃)` is the tilt the twist gives the record at `p`.
  - Restricting to a sub-σ-field lowers relative entropy, so the bound also holds for twists defined on the whole plane.

**Scope.** The theorem covers deterministic site-wise rotations. It does not cover configuration-dependent maps or transformations of the noise. `m_t → 0` itself is not decided here.

## 2. Steps

**S1 (PROVED; CHECKED `F1`, `F4`).**
- `∫_{S²} e^{η·s} ds = 4π sinh κ/κ` with `κ = |η|`, so `ψ(η) := log ∫ e^{η·s} ds = log 4π + f(κ)`, where `f = log(sinh κ/κ)`, `f' = A` and `f'' = A'`.
- For a radial function, `∇ψ = f'(κ) η̂` and `∇²ψ = f''(κ) η̂η̂ᵀ + (f'(κ)/κ)(I − η̂η̂ᵀ)`. So `Cov_{vMF(η)}(s)` has eigenvalue `A'(κ)` along `η̂` and `A(κ)/κ` (twice) across it.
- With densities `e^{η·s − ψ(η)}`, `KL(vMF(a) ‖ vMF(b)) = E_a[(a − b)·s] − ψ(a) + ψ(b) = ψ(b) − ψ(a) − ∇ψ(a)·(b − a)`, a Bregman divergence. Hence `KL = ∫₀¹ (1 − u)(b − a)ᵀ ∇²ψ(a + u(b − a))(b − a) du`.
- When `|a| = |b| = κ`, this gives `κA(κ)(1 − â·b̂)` (GIVEN (3); checked).

**S2 (PROVED; CHECKED `F2`). `A(κ)/κ` decreases from `1/3`.**
- `(A/κ)'` has the sign of `2 sinh²κ − κ² − κ sinh κ cosh κ`.
- With `u = 2κ`, that expression is `g(u) = cosh u − 1 − u²/4 − (u/4) sinh u`.
- The `u^{2m}` coefficient of `g` is `0` at `m = 1` and `(1/(2m − 1)!)(1/(2m) − 1/4) < 0` for `m ≥ 2`; the odd coefficients vanish.
- Consequences:
  - `A' ≤ A/κ` (the sign statement);
  - `A(κ) ≤ κ/3` (the limit at `0`);
  - `λ_max(Cov) = A/κ ≤ 1/3`;
  - `λ_min(Cov) = A'`.

**S3 (PROVED; CHECKED `F3`). `A'` decreases from `1/3`.**
- `A'' = 2(κ³ cosh κ − sinh³κ)/(κ³ sinh³κ)`.
- `sinh³κ = (sinh 3κ − 3 sinh κ)/4`, so `sinh³κ − κ³ cosh κ = Σ_m c_m κ^{2m+1}` with `c_m = (3^{2m+1} − 3)/(4(2m + 1)!) − 1/(2m − 2)!`.
- `c_1 = c_2 = 0`, and `c_m > 0` for `m ≥ 3`. Equivalently `3^{2m+1} − 3 ≥ q(m) := 4(2m + 1)(2m)(2m − 1)`, by induction:
  - base: `m = 3`, where `2184 ≥ 840`;
  - step: `3^{2m+3} − 3 ≥ 9(3^{2m+1} − 3)` and `9q(m) − q(m + 1) = 4(2m + 1)(32m² − 28m − 6) > 0`.
- Consequences for `|η| ≤ 3β`:
  - `λ_min(∇²ψ(η)) = A'(|η|) ≥ A'(3β)`.
  - For every 2-plane `Π`, `tr(Π Cov_η Π) ≥ A(3β)/(3β) + A'(3β)`. Proof: `Π` meets `η̂^⊥` in a line, on which the variance is `A/κ`. The orthogonal direction inside `Π` has variance at least `A'`. Both are at least their values at `κ = 3β` by S2 and S3.

**S4 (PROVED). Chain rule.**
- `C(p)` with its level-0 base is closed under taking predecessors, and records of a level are conditionally independent given the previous level (L83).
- So `H(P^θ|_{C(p)} ‖ P|_{C(p)}) = Σ_{x∈C(p)} E_{P^θ}[KL(Q_x ‖ P_x)]`, with `Q_x` and `P_x` the site conditionals at the same past.
- Write the twisted past as `s̃ = R_θ s`:
  - `Q_x = vMF(β R_{θ_x} Σ_y R_{−θ_y} s̃_y) = vMF(β R_{θ_x} S_x)`, where `S_x = Σ_y s_y`;
  - `P_x = vMF(β Σ_y s̃_y) = vMF(β Σ_y R_{θ_y} s_y)`.
- Hence `H = Σ_x E_P[KL(vMF(a_x) ‖ vMF(b_x))]`, with `a_x = β R_{θ_x} S_x` and `b_x = β Σ_y R_{θ_y} s_y`. Here `|a_x|, |b_x| ≤ 3β`.

**S5 (PROVED). Level 1.**
- The predecessors are `e₃` exactly, so `a = 3β R_{θ_x} e₃`, `b = 3β e₃`, and `KL = 3βA(3β)(1 − cos θ_x) = 2βA(3β) Σ_y sin²((θ_x − 0)/2)`.
- **Upper:** `2βA(3β) ≤ 2β²` by S2.
- **Lower:** `c_β ≤ 2β² (A/κ)(2A/κ) = (4/9) A(3β)² ≤ (4/9) β A(3β) < 2βA(3β)`, with `κ = 3β`, using S2 twice.

**S6 (PROVED; CHECKED `F4`). Levels `t ≥ 2`.**
- `a − b = β R_{θ_x} Σ_y M_y s_y`, where `M_y = I − R_{ω_y}` and `ω_y = θ_y − θ_x`. Also `M_yᵀ M_y = 4 sin²(ω_y/2) Π`, with `Π` the projection onto `span(e₂, e₃)`.
- **Lower.**
  - By S1 and S3, `KL ≥ ½ A'(3β) |a − b|²`.
  - `E_P |Σ_y M_y s_y|² ≥ E[tr Cov(Σ_y M_y s_y | F_{t−2})]`, and the three records at level `t − 1` are conditionally independent given level `t − 2`. So this equals `Σ_y E[tr(M_y Cov(s_y | F_{t−2}) M_yᵀ)] = Σ_y 4 sin²(ω_y/2) E[tr(Π Cov(s_y | F_{t−2}) Π)]`.
  - Each `s_y` is `vMF(β S'_y)` given `F_{t−2}`, with `|β S'_y| ≤ 3β`. By S3 the last expression is at least `Σ_y 4 sin²(ω_y/2)(A(3β)/(3β) + A'(3β))`.
  - Hence `E_P[KL] ≥ c_β Σ_y sin²(ω_y/2)`.
- **Upper.** `KL ≤ ½ · ⅓ |a − b|²` and `|a − b| ≤ β Σ_y 2|sin(ω_y/2)|`. So `KL ≤ (β²/6) · 3 · 4 Σ_y sin² = 2β² Σ_y sin²(ω_y/2)`.
- With S5 this proves (i).

**S7 (PROVED; CHECKED `G1`–`G3`). The capacity bound (ii).**
- The monotone predecessor paths from `p` to level 0 are the draw sequences of a three-colour Pólya urn that starts with one ball of each colour. The path law is uniform on the `C(d + 2, 2)` compositions of each depth `d`, which is exact and checked for `d ≤ 30`.
- The edge flow `f(n → n + e_a) = (n_a + 1)/((d + 3) C(d + 2, 2))` is a unit flow, conserved at every vertex (checked).
- Since `Σ_a (n_a + 1)/(d + 3) = 1`, its energy at depth `d` is at most `1/C(d + 2, 2)`. So `E_T ≤ Σ_{d<T} 2/((d + 1)(d + 2)) = 2T/(T + 1)`. Exact values: `E_1 = 1/3`, `E_2 = 11/24`, `E_3 = 21/40`, `E_10 = 0.66288`, `E_40 = 0.72590`.
- Fix `θ`. Let `x_e ∈ (−π, π]` represent the edge difference mod `2π`; then `sin²(Δθ/2) = sin²(x_e/2)`.
  - Along each path, `Σ x_e ≡ θ₀ (mod 2π)`, so `Σ_{e∈Γ} |x_e| ≥ |θ₀|`.
  - Averaging over the flow gives `Σ_e f_e |x_e| ≥ |θ₀|`.
  - By Cauchy–Schwarz, `θ₀² ≤ E_T Σ_e x_e²`.
  - `sin²(x/2) ≥ x²/π²` for `|x| ≤ π`, since `sin` is concave on `[0, π/2]`.
- So `X ≥ θ₀²/(π² E_T)`.
- The true minimum of `Σ x_e²` is `θ₀²/R_T`, where `R_T ≤ E_T` is the cone's effective resistance. Exact values:
  - `R_1 = 1/3`, `R_2 = 4/9`;
  - `R_3 = 0.50427`, `R_5 = 0.56935`, `R_7 = 0.60432`, `R_9 = 0.62616`, increasing.
- The space-time graph is `Z³`, and a point-to-plane capacity in `Z³` stays positive. The linear model's twist cost sees only the level walk, which is two-dimensional and recurrent.

**S8 (PROVED). General rotation fields (iii).**
- **Levels `≥ 2`:** the computation of S6 goes through with `M_y = I − R_x^{−1} R_y`. This matrix has rank 2, with `M_yᵀ M_y = 4 sin²(ω_y/2) Π_{n_y}`, where `ω_y` and `n_y` are the angle and axis of `R_x^{−1} R_y`.
- **Level 1:** `KL = 3βA(3β)(1 − e₃·R_x e₃) = 6βA(3β) sin²(α_x/2)`, where `α_x = ∠(R_x e₃, e₃)` is the tilt.
- **Path argument:**
  - Along an edge, `|α_x − α_y| ≤ ∠(R_x e₃, R_y e₃) ≤ ω_xy`, by the triangle inequality on `S²`.
  - Since both half-angles lie in `[0, π/2]`, `sin²(ω/2) ≥ sin²(|Δα|/2)`.
  - The path argument of S7 then runs with `|Δα_e|` in place of `|x_e|`, ending at `α_p = θ₀`.

**S9 (PROVED). Consequence.**
- `H ≥ c_β θ₀²/(π² E_T) ≥ c_β θ₀²/(2π²)` for every `T`.
- The entropy inequality `|E f(R_{θ₀} s_p) − E f(s_p)| ≤ √(2H)` therefore cannot be driven to zero by any such twist.
- The quantity GIVEN (2) sends to zero is only the order-`β` innovation part, whose minimum is `1/Σ_{k<T} P_k`. The full cost is bounded below by `c_β` times an XY energy, and that energy's minimum is bounded below uniformly in `T`. This is the same spread term the round-1 report measured growing for the linear-optimal twist (`0.18`, `0.72`, `1.37` at `T = 8, 32, 64`).

**N1 (numerical, labelled; `check.py` N1).** Monte Carlo with 20000 paths on the `T = 3` cone. The exact per-site relative entropies are summed for two twists: the apex only, and linear in the level.
- At `β = 1.5`, `H = 1.04` and `1.71`.
- At `β = 3`, `H = 3.08` and `4.17`.
- All four lie inside `[c_β X, 2β² X]`. This checks the sign conventions of S4 and S6.

## 3. The first failing step

Route A fails at **A2**. "The path-space relative entropy of the twist is at most `C β θ₀²/Σ_{k<T} P_k`" is false for all large `T`, for every `C` and every deterministic site-wise rotation twist (Theorem N). The entropy-inequality route through such twists therefore cannot give `m_t → 0`. The order-`β` part does tend to zero, but the full cost does not.

## 4. What would finish it

- **A deformation that is not a site-wise rotation of the records.**
  - Write the law as `s = R(Ŝ)·W(β|S|, U)` with i.i.d. noise `U`. Rotating the innovations costs only the innovation-type relative entropy per site. However, its effect on `s_p` is not a rotation of the marginal.
  - A proof would have to show that the rotated-innovation process tracks the rotated process up to errors that vanish as `T → ∞`. That means controlling how the nonlinear average `Ŝ` propagates relative rotations.
  - Configuration-dependent rotations (a rotation relative to the local mean) are another option. They need the Jacobian bookkeeping that Theorem N avoids.
- **Route B (comparison with the linear model).**
  - The nonlinear conditional noise `A(β|S|)/(β|S|)` is at least the linear `A(3β)/(3β)` (S2). The tilt of the mean direction satisfies `|Ŝ_⊥| ≥ |S_⊥|/3`.
  - Both push the transverse spread above the linear one. Turning that into an inequality for `S²`-valued records needs a monotone coupling, and none is available here.
- **What Theorem N does not say.** It says the path law's cost of a site-wise twist is three-dimensional, of order `c_β ≈ 2/(27β)` at large `β`. It does not say whether the nonlinear law keeps its initial plane. Block 26's executed decay at `β = 3–24` is untouched by it.
