# J:derive:plane-memory-loss-2:a2 — the sphere kernel moves by at most a third of its field, so the plane forgets for every β < 1

**Provenance.** Worker `w-macbookpro90c72-j3a3b`, model `claude-opus-5-5`, one session.

I did not re-run Route A. Its deterministic-twist form is closed three times on this branch:
- `a1` (`w-jonathonsmac4f50-jd237`): the path relative entropy of any site-wise rotation twist is at least `c_β` times an edge energy.
- `a4` (`w-jonathonsmac4f50-j5926`): the cone conductances.
- `a3` (`w-jonathonsmac4f50-jdb1c`): `C_T > 4/3`.

I took a different route: the causal coupling of block 27 (PR #8171).
- Block 27 proves loss of memory for `β < 1/√3`.
- Its T4 shows that no coupling of this kind can pass `β = 1`.
- It calls `1/√3` a constant of the route, not a threshold.

This attempt closes the band `[1/√3, 1)`. It computes the kernel's sensitivity exactly, which is `1/3`, and shows the coupling then contracts for every `β < 1`.

## 1. Statement

**Attempted:** block 26's open statement. For every `β > 0`, the sphere formation law started from the aligned plane has `m_t → 0` on the infinite plane.

**Obtained (PARTIAL):** the statement for every `β < 1`, with an exponential rate. It is not obtained for `β ≥ 1`.

Definitions are those of blocks 26 and 27 (PRs #8170, #8171):
- **Kernel.** `K_V(ds) = (κ/(4π sinh κ)) e^{V·s} dσ(s)` on `S²`, with `κ = |V|` and `û = V/κ`. The record at `x` has law `K_{βS_x}`, where `S_x` is the sum of its three predecessors.
- **Constants.** `A(κ) = coth κ − 1/κ`, `A' = dA/dκ`, `y = A/κ`, `a = 1 − 3y`, `C = κ/(4π sinh κ)`.
- **Mean.** `F(V) = E_{K_V}[s] = A û`.
- **Distances.** Chordal distance `|s − s'|`. `W_1` is the Wasserstein distance for it.
- **KR norm.** For a zero-mass signed measure `μ` on `S²`, `‖μ‖_KR = sup{∫ f dμ : f 1-Lipschitz for the chordal distance}`.
- **Causal coupling, `D_t`, `m_t`.** As in block 27: `D_t = sup_x E|s_x − s'_x|`.

Write `∂_d K_V` for the signed measure `(d·∇_V k_V)(s) dσ(s)`, where `k_V` is the density of `K_V`.

**Claim K (the kernel).**
- (i) For every `V ∈ R³` with `|V| ≤ 3` and every unit `d`, `‖∂_d K_V‖_KR ≤ 1/3`.
- Hence `W_1(K_V, K_{V'}) ≤ |V − V'|/3` whenever `|V|, |V'| ≤ 3`.
- (ii) For a unit `w ⊥ V`, `‖∂_w K_V‖_KR = A(κ)/κ` exactly.
- (iii) For every rotation `R`, `W_1(K_V, K_{RV}) = (A(κ)/κ)|V − RV|`.

**Claim M (memory).** For every `β < 1`:
- the causal coupling satisfies `D_{t+1} ≤ β D_t`;
- the level automaton has exactly one invariant law, and it is invariant under every rotation of `S²`;
- the law of level `t` from any initial plane is within per-site `W_1` distance `2β^t` of it;
- from the aligned plane, `m_t ≤ β^t`.

The constant `1/3` in K(i) is sharp. Block 27's T4 gives `W_1(K_V, K_{V'}) ≥ |F(V) − F(V')|`, and `A(δ)/δ → 1/3` as `δ → 0`. So `β < 1` is the full reach of any uniform causal-coupling argument.

## 2. Steps

**Step 1 (PROVED; CHECKED S1, S2): kernel facts.**
- *Moments.* Let `w = s·û`. Under `K_V` it has density `∝ e^{κw}` on `[−1, 1]` (Archimedes). Then `E[w] = A`, `E[w²] = 1 − 2y`, `Var w = A' = 1/κ² − 1/sinh²κ > 0`. The transverse second moment per direction is `E[(s·w)²] = (1 − E w²)/2 = y` for `w ⊥ û`.
- *`A` is concave.* `A'' = −2/κ³ + 2cosh κ/sinh³κ`, so `A'' < 0` is equivalent to `κ³ cosh κ < sinh³κ`. The series `sinh³x − x³cosh x = Σ_{n odd} [(3ⁿ − 3) − 4n(n−1)(n−2)] xⁿ/(4·n!)` has vanishing coefficients at `n = 3, 5` and positive ones for `n ≥ 7`.
- *Why the coefficients are positive for `n ≥ 7`.* By induction `3ⁿ ≥ 4n³`: it holds at `n = 7`, and `(1 + 1/n)³ ≤ 3` for `n ≥ 3`. Also `4n³ > 4n(n−1)(n−2) + 3`.
- *Consequences.*
  - `A'` decreases.
  - `A(0⁺) = 0` and concavity give `A ≥ κA'`, so `y = A/κ` decreases.
  - `A' ≤ y < 1/3`, and hence `a ≥ 0`.
  - `C` decreases, since `(κ/sinh κ)' < 0` follows from `tanh κ < κ`.
  - `a` increases.

**Step 2 (PROVED): the flow bound.** Let `J` be a `C¹` vector field on the closed unit ball `B` with `div J = 0` in `B`. Let `μ` be the measure `(J·n) dσ` on `S² = ∂B`.
- For a chordal-1-Lipschitz `f`, take McShane's extension `F̃(x) = min_s (f(s) + |x − s|)`. It is 1-Lipschitz on `R³`.
- Then `∫ f dμ = ∫_{∂B} F̃ J·n = ∫_B ∇F̃·J ≤ ∫_B |J|`.
- So `‖μ‖_KR ≤ ∫_B |J|`.

**Step 3 (PROVED; CHECKED S3): the weight.** Put `k̃(x) = C e^{V·x}` on `B`. This extends the density `k_V` of `K_V` into the ball.
- `∫_B k̃ = C ∫_0^1 4πr² (sinh κr)/(κr) dr = A/κ` exactly.
- By Cauchy–Schwarz, `∫_B |J| ≤ (∫_B k̃)^{1/2} (∫_B |J|²/k̃)^{1/2}`.
- So `‖μ‖_KR² ≤ (A/κ) · E(J)`, where `E(J) := ∫_B |J|²/k̃`.
- Also `∫_B x_z k̃ = (1/κ)(1 − 3y)`, taking `û = ẑ`.

**Step 4 (PROVED; CHECKED S1.transverse): transverse directions and rotations.** From `∂_V k_V = k_V (s − F(V))`, for `w ⊥ V` we get `∂_w k_V = k_V (s·w)`.
- *The chord flow.* `J_w = k̃ w` has `div J_w = k̃ (V·w) = 0` and flux `k (s·w)`.
- *Upper bound.* `∫|J_w| = ∫ k̃ = A/κ`.
- *Lower bound.* The test function `f = s·w` gives `∫ f ∂_w k_V = E[(s·w)²] = y`. This proves K(ii).
- *Rotations (K(iii)).* Let `n = (V − RV)/|V − RV|` and let `σ` be the reflection in `n^⊥`. Then `σV = RV` and `K_{RV} = σ_* K_V`. On `{s·n > 0}` the density ratio is `e^{|V − RV| s·n} ≥ 1`.
- *Mirror coupling.* Keep the common part fixed and reflect the excess. The cost is `∫_{s·n>0} (k(s) − k(σs)) · 2(s·n) = 2E_V[s·n] = 2A(û·n) = (A/κ)|V − RV|`.
- *Matching lower bound.* The test function `s·(û − Rû)/|û − Rû|` gives `|F(V) − F(RV)| = A|û − Rû| = (A/κ)|V − RV|`.

**Step 5 (PROVED; CHECKED S4): a source flow.** Take `û = ẑ`. Set
- `f(t) = e^{κt}(1 − t²)(a − At)`,
- `N(z) = ∫_{−1}^z f`,
- `q = N e^{−κz}/(1 − z²)²`,
- `p = y − zq`,
- `J_1 = k̃(x) (p(z) x + q(z) ẑ)`.

The steps:
- *(a) `N(1) = 0`.* `N(1) = aI_0 − AI_1`, where `I_0 = ∫ e^{κt}(1 − t²) = 4A sinh κ/κ²` and `I_1 = ∫ t e^{κt}(1 − t²) = 4a sinh κ/κ²`. So `N(1) = 0`.
- *Regularity.* `N'(±1) = f(±1) = 0`, so `N` has double zeros at `±1`. Hence `q`, `p` and `J_1` are entire.
- *(b) The source equation.* `div J_1 = k̃ (div W + κW_z)` with `W = px + qẑ`. The combination `3p + zp' + q' + κ(pz + q)` equals `1` identically (checked symbolically with `N' = f`). So `div J_1 = k̃` in `B`.
- *The boundary flux.* `J_1·n = k (p + zq) = y·k` on `S²`.
- *(c) `a < A`.* If `a ≥ A`, then `f > 0` on `(−1, 1)`, so `N(1) > 0`, contradicting (a). With `a ≥ 0` this gives `0 ≤ a/A < 1`.
- *`N ≥ 0`.* `f ≥ 0` on `[−1, a/A]` and `f ≤ 0` on `[a/A, 1]`. So `N(z) = ∫_{−1}^z f ≥ 0` for `z ≤ a/A`, and `N(z) = −∫_z^1 f ≥ 0` for `z ≥ a/A`.
- *(d) Two representations.* Substituting `t = −1 + (1 + z)u` and `t = 1 − (1 − z)u`:
  ```
  N(z) = (1+z)² ∫₀¹ e^{κ(−1+(1+z)u)} u(2−(1+z)u)(a+A−A(1+z)u) du
       = (1−z)² ∫₀¹ e^{κ(1−(1−z)u)} u(2−(1−z)u)(A−a−A(1−z)u) du.
  ```
- *Bounding `M`.* Let `M = N/(1 − z²)² ≥ 0`. Bound each integrand by its positive part, using `u(2 − ·) ≤ 2u` and the last factor `≤ a + A` (resp. `≤ A − a`). With `ω(Y) = ∫₀¹ 2u e^{−Y(1−u)} du = 2(Y − 1 + e^{−Y})/Y²` and `φ̃(Y) = ∫₀¹ u e^{−Yu} du = (1 − (1+Y)e^{−Y})/Y²`, this gives `M ≤ min(L, R)`, where:
  - `L = (a + A) e^{κz} ω(κ(1+z))/(1 − z)²`,
  - `R = 2(A − a) e^{κ} φ̃(κ(1−z))/(1 + z)²`.
- Both `ω` and `φ̃` decrease in `Y`, with `ω(0) = 1` and `φ̃(0) = 1/2`.

**Step 6 (PROVED; CHECKED S5): every direction.** Let `d = cû + sw` be a unit vector with `w ⊥ û`. Set `J_d = k̃ d − (V·d) J_1`.
- *It is a valid flow.* `div J_d = k̃ V·d − (V·d) k̃ = 0`, and its flux is `k(s·d) − κc·y·k = k(s·d − F·d) = ∂_d k_V`.
- *The cross term.* Integrate `J_1·∇(d·x)` by parts: `∫_B d·J_1 = y(F·d) − c ∫_B x_z k̃ = (c/κ)(y − A')`, using `A' = 1 − 2y − A²`.
- *The energy.* Hence `E(J_d) = y − 2κc·(c/κ)(y − A') + κ²c² e_1 = y − c²[2(y − A') − κ² e_1]`, where `e_1 := E(J_1)`.
- *Reduction.* By Step 3, `‖∂_d K_V‖² ≤ y · max(y, 2A' − y + κ² e_1)`. The expression is linear in `c²`. Since `y ≤ 1/3`, the bound `≤ 1/9` for every `d` is equivalent to `y(2A' − y + κ² e_1) ≤ 1/9`, that is, to `κ² e_1 ≤ B(κ)`.
- *The budget.* `B = 1/(9y) − 2A' + y = (1 − 3y)²/(9y) + 2(1/3 − A')`. Both terms increase in `κ` (Step 1), so `B` increases.

**Step 7 (PROVED; CHECKED S4.disk, S4.bracket, S4.t2parts): the energy of `J_1`.** Integrate over horizontal disks. With `E_K` the law of `z` under `K_V` (density `(κ/(2 sinh κ)) e^{κz}`), `e_1 = t_1 + t_2 + t_3`:
- `t_1 = y² E_K[1 − z⁴]/4 ≤ y³(1 − y)`. This uses `E z⁴ ≥ (E z²)² = (1 − 2y)²`.
- `t_2 = (y/4) E_K[z²(1 − z²)(Az − a)] ≤ y(A − a)/16`. The identity comes from `∫ zN = −½ ∫ z²f`, using `N(±1) = 0`. The bound uses `(Az − a)⁺ ≤ A − a` and `z²(1 − z²) ≤ 1/4`.
- `t_3 = πC ∫_{−1}^1 (1 − z²/2)(1 − z²)² e^{−κz} M² dz`, where `πC = κ/(4 sinh κ)`. Here
  `e^{−κz} M² ≤ min( (a+A)² e^{κz} ω²/(1−z)⁴ , 4(A−a)² e^{κ(2−z)} φ̃²/(1+z)⁴ )`.

**Step 8 (CHECKED R1): `0 < κ ≤ 1/10`.**
- *The budget from below.* `B ≥ 2(1/3 − A')`. Next, `1/3 − A' ≥ κ²/20` is equivalent to `E(κ) := κ² − sinh²κ (1 − κ²/3 + κ⁴/20) ≥ 0`.
- *Why `E ≥ 0`.* Write `E = Σ e_n κ^{2n}`. Exactly, `e_1 = e_2 = 0` and `e_3 = 1/60`. Bounding the tail through `Σ_{m≥2} 2^{2m−1}/(2m)! < 2/5` gives `E/κ⁶ ≥ 1/60 − κ²·(83/60)(2/5) > 0` for `κ ≤ 1/10`.
- So `B/κ² ≥ 1/10`.
- *The energy from above.* The crude bounds `y ≤ 1/3`, `A < κ/3 ≤ 1/30`, `0 ≤ a < A`, `πC ≤ 1/4`, `ω ≤ 1`, `φ̃ ≤ 1/2` and `e^{2κ} ≤ 5/4` give `e_1 ≤ 2/81 + 1/1440 + (1/900)(21/16) < 0.0269 < 1/10`.

**Step 9 (CHECKED R2): `1/10 ≤ κ ≤ 3`.** Use 290 cells `[κ_0, κ_1]` of width `1/100`, and 200 cells of width `1/100` in `z` on `[−1, 1]`. On each κ-cell:
- the κ-dependence goes to endpoint values by the monotonicities of Steps 1 and 6. `κ² ≤ κ_1²`, `y ≤ y(κ_0)`, `a + A ≤ (a + A)(κ_1)`, `0 < A − a ≤ A(κ_1) − a(κ_0)`, `πC ≤ πC(κ_0)` and `B ≥ B(κ_0)`;
- on each z-cell, each factor of the Step 7 integrand is replaced by its supremum. The factors are `e^{κz}`, `e^{κ(2−z)}`, `ω`, `φ̃`, `(1 ∓ z)^{−4}` and `(1 − z²/2)(1 − z²)²`, all monotone in `κ` and `z`;
- the check verifies `κ_1² (t_1^up + t_2^up + T_3^up) ≤ B(κ_0)`, plus the signs `y ≤ 1/3`, `a ≥ 0`, `A − a > 0`.

All values sit at rational points:
- They are computed in integer interval arithmetic scaled by `2^256`, with outward rounding.
- `exp` is reduced by `2^m` and uses a 30-term Taylor sum whose remainder is below one unit.
- Every cell passes. The worst margin `B/lhs` is 1.7356, on `[2.99, 3]`.

**Step 10 (PROVED from 3–9): Claim K.**
- For `0 < κ ≤ 3`, Steps 6–9 give `‖∂_d K_V‖ ≤ 1/3` for every `d`.
- At `V = 0` the flow `d/(4π)` gives exactly `1/3`.
- *The `W_1` bound.* Take `f` 1-Lipschitz and `V_t = V + t(V' − V)`. Then `∫ f d(K_{V'} − K_V) = ∫_0^1 ∫ f ∂_{V'−V} K_{V_t} dt ≤ |V' − V|/3`, because the segment stays in `{|V| ≤ 3}`. Kantorovich–Rubinstein duality turns this into the `W_1` bound.

**Step 11 (PROVED; block 27's T2/T3 argument re-run at scope with the new constant): Claim M.** Let `β < 1`.
- *The contraction.* At a site `x` of level `t+1`:
  `E[|s_x − s'_x| | level t] ≤ W_1(K_{βS_x}, K_{βS'_x}) + η ≤ (β/3)|S_x − S'_x| + η ≤ (β/3) Σ_j |s_{x−e_j} − s'_{x−e_j}| + η`.
  Here `|βS|, |βS'| ≤ 3β < 3`. So `D_{t+1} ≤ βD_t + η`, with `η` arbitrary.
- *Uniqueness.* An invariant law exists: the space is compact and the kernel is Feller (Krylov–Bogolyubov). Couple two invariant laws. Every finite marginal is then within `2|Λ|β^t → 0`, so the two laws coincide.
- *Rotation invariance.* `K_β(R·|RS) = R_* K_β(·|S)`, so the unique law is invariant under every rotation.
- *The magnetization.* Couple the aligned plane `e` with `−e`. The second run has magnetization `−m_t` along `e`. So `2m_t ≤ D_t ≤ 2β^t`.

**Step 12 (NUMERICAL, not load-bearing; printed as `N.lp`).** At `κ = 1`, with `d` at 53° from `V`:
- the discrete transport norm on 400 Fibonacci points is 0.3027;
- the flow bound `(y E(J_d))^{1/2}` is 0.3032;
- `y` is 0.3130.

So the flow of Step 6 is nearly optimal off the transverse plane.

**ASSUMED (standard, named at definition level):**
- Kantorovich–Rubinstein duality on a compact metric space;
- the McShane extension;
- the divergence theorem for (Lipschitz) × `C¹` fields on the ball;
- existence of optimal couplings on the compact sphere;
- the Krylov–Bogolyubov existence of an invariant law.

## 3. The first failing step for the full statement

Step 11 needs `3β·(1/3) < 1`, and for `β ≥ 1` it fails.
- This is not slack in Claim K. The supremum over `|V| ≤ 3β` of the local sensitivity is exactly `1/3`: K(i) bounds it above, and block 27's T4 bounds it below, near `V = 0`.
- A uniform causal coupling must allow two predecessor sums whose segment passes through `0`.
- So **no uniform causal-coupling argument reaches `β ≥ 1`**. This is a precise no-go for the route, now attained at its boundary.

## 4. What would finish it

1. **A contraction that uses configuration information.**
   - The exact transverse factor at a configuration is `g(|S|) = 3A(β|S|)/|S|`, by K(ii).
   - `g` decreases in `|S|` (Step 1). At the aligned configuration it is `A(3β) < 1` for every `β`, and it tends to `β` as `S → 0`.
   - So for `β > 1` it exceeds `1` only below a threshold `r*(β) < 3`.
   - A Lyapunov-weighted metric could contract if the dynamics keeps `P(|S_x| < r*(β))` small. That needs local-order information, which the coupling alone cannot give; this is Route B's ground.
   - In exploratory numerics (not claimed), the full per-`V` sensitivity equals `A/κ` in every direction. That would follow from a weighted Steklov inequality `Var_{K_V}(u|_{S²}) ≤ ∫_B k̃ |∇u|²`.
   - Its non-zonal sectors hold exactly by the ground-state identity `∫k̃|∇(ζ^m w)|² = m∫_{S²} k|ζ^m w|² + ∫k̃|ζ|^{2m}|∇w|²`, with `ζ = x + iy` and `w` zonal.
   - Its zonal sector was only computed.
2. **Route B**, the variance-growth comparison, is untouched here.
3. **Route A with deterministic twists** stays closed (`a1`, `a3`, `a4`). Adapted twists are not covered by those no-gos.
4. Block 26's executed decay at `β ≥ 3` looks algebraic. The present bound is exponential for `β < 1`. Whether the decay mechanism changes in `[1, 3]` is open.

## 5. Running it

```
python3 probes/work/derive/plane-memory-loss-2/w-macbookpro90c72-j3a3b/check.py
```

Requires `sympy`; `scipy` is used only for the numerical block. The run takes about 5 s: 35 exact checks, 290 interval cells, and one labelled numerical line.
