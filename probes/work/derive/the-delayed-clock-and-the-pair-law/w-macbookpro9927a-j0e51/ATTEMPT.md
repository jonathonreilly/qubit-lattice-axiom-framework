# The delayed clock and the pair law — attempt 1 of 2

Worker `w-macbookpro9927a-j0e51` (claude-opus-5-5), unit `J-derive-the-delayed-clock-and-the-pair-law-a1`. Exact checks are in `check.py` in this directory. Family letters (Q, A, …, S) refer to it.

**Disclosure.**
- This machine refereed attempt a2 as `w-macbookpro90c72-jd141`. Attempt a2 is `w-macbookpro90c72-ja546`, written by another agent (model grok-4.6); the referee found it fails at its step S3.
- My plan here is my own unlanded plan of 2026-09-23: the invariant, the first order in 1/Γ, and the product and reversibility routes.
- The referee report's side computation R4 (one record, first order in 1/Γ) reappears below as a corollary of S4 and S8, with its own exact checks.
- New here:
  - the first-order-in-log κ solution for every Γ (S4);
  - the product theorem for an arbitrary field law (S6);
  - the reversibility theorem (S7);
  - the exact rate-weighted identity (S5);
  - the quasi-static limit (S9).

**Sources, as landed on main.** They are pinned by commit and SHA-256 in family Q.
- Block 95 (`docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_…_2026-09-23.md`): its rates, T1, T2 and T3.
- Block 53 (`docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_…_2026-09-21.md`): the operator `L = I − A`, and T5, the departure-timed walker's weights `∝ 1/w`.
- The relaxation is the task's supplied clause. Block 57 enters only through the task's remark that this clause is separate from kinetic terms.
- Nothing is adopted.

**Two corrections of the task's paraphrase.** The landed versions control.
1. *Sign.* Block 95 T2 gives `π ∝ W exp[6λ(1−2a) Σ_pairs G]`. At departure timing `a = 1` this is `W exp(−6λ Σ_pairs G)`. The task's "`W(C) exp(6 log(κ) Σ_pairs G)`" has the opposite sign. I use the landed sign, and nothing below depends on the task's.
2. *Level.* Block 95 fixes the level of `u` by "mean u = 0". The relaxation clause does not conserve the mean of `u`; it conserves `Σ_z 1/w_z` exactly (S1). The invariant, not the mean, therefore fixes the level of the slaved field (S2).

Block 95's pair law is a neutralized finite-torus law, and everything below is on finite tori.

## 1. Statement attempted

**Setting.**
- *Lattice.* The torus is `T = (Z/L)^d`, with `L ≥ 3`, `V = L^d`, `q = 2d` and neighbour set `E`.
  - Block 95 is stated for `d = 3` (`q = 6`). On a ring (`d = 1`) the task's `1/6` and `6λ` become `1/q` and `qλ`.
- *Operators.*
  - `Δ = qI − Adj` and `M = Adj/q − I = −Δ/q`. Block 53's `L` is `−M`.
  - `G` solves `ΔG = δ_0 − 1/V` with `Σ G = 0`; `G2 = G∗G`; `λ = log κ`.
- *Records.* There are `N` records, `1 ≤ N ≤ V − 1`, one per site, with occupation vector `n_C` and `n̄ = N/V`.
- *Field.* `u ∈ R^V` and `w = e^u`.
- *Hop rates* (block 95). A move `x → y` onto an empty neighbour has rate `exp[a u_x + (1−a) u_y] · h/q`, with `h = W(C′)/(W(C)+W(C′))`.
  - Main case: `a = 1` (departure timing) and `W = 1` (so `h = 1/2`). A record at `x` then hops to each empty neighbour at rate `r0 w_x`, with `r0 = 1/(2q)`. On the cubic torus this is `w_x/12`, as in block 95 T3.
- *Field clause* (supplied): `du_z/dt = Γ w_z ((M u)_z + λ (n_{C,z} − n̄))`.
- *Joint process.* It is piecewise deterministic: `u` is continuous and follows the flow of the current configuration `C`; `C` jumps at the rates above, evaluated at the current `u`.

**Assumptions (not proved here).**
- **A0 (well-posedness).**
  - The joint process is non-explosive.
  - Dynkin's formula `d/dt E f(X_t) = E Lf(X_t)` holds for bounded `f(C,u)` that are C¹ in `u` and have bounded `Lf`.
  - For (a), (b) and S5: a stationary law exists on each level set of `Σ 1/w`, long-run averages equal its expectations, and `w` and `u` have finite moments under it.
  - Proved here: for a fixed configuration the flow is global and bounded (S2), and jumps do not move `u`. Not proved: a bound on `u` that is uniform over switching configurations.
- **A1 (first order).** On the level set `Σ 1/w = V`, the stationary law is weakly differentiable in `λ` at `0`, and `(C, u/λ)` converges to the `λ = 0` joint law. This makes the `O(λ)` solution of S4 the Taylor coefficient of the true stationary law.

**Claims.**
- (a) One record: the long-run hop rate `R`, the diffusion constant, and whether the record traps itself.
- (b) Two records: the first-order correction to the pair law in `1/Γ`, and reversibility.
- (P) There is no stationary joint law `μ(C)·Q(du)` of product form.

## 2. Steps

**S1 (PROVED; CHECKED B). The invariant.**
- Along the flow, `d/dt Σ_z e^{−u_z} = −Σ_z e^{−u_z} Γ e^{u_z}((Mu)_z + λ(n_z − n̄)) = −Γ[Σ_z (Mu)_z + λ Σ_z (n_z − n̄)] = 0`.
  - The first sum vanishes because `M` has zero column sums on a regular graph.
  - The second vanishes because `Σ n = N = V n̄`.
- Jumps do not move `u`.
- So `S(u) := Σ_z 1/w_z` is constant along every path, for every `Γ, λ, a, W, N`.

**S2 (PROVED; CHECKED B, C). Fixed configuration and the slaved limit.**

(i) *The equilibrium.*
- For fixed `C` the flow is `Γ w ⊙ M(u − u*(C))`.
- Here `u*(C) = qλ Σ_{r∈C} G(· − r) + log(Z(C)/S)` and `Z(C) = Σ_z exp(−qλ Σ_{r∈C} G(z − r))`.
- This holds because `M(qλ Σ G) = −λ(n_C − n̄)` and constants lie in `ker M`.
- The added constant is the unique one with `Σ e^{−u*} = S`.

(ii) *Convergence.*
- Let `E_C(u) = ½⟨u − u*, −M(u − u*)⟩`. Then `dE_C/dt = −Γ Σ_z w_z ((M(u−u*))_z)² ≤ 0`, with equality iff `u − u*` is constant.
- On a level set, a bounded `E_C` bounds the oscillation of `u − u*`, and the invariant bounds its level. So orbits are bounded, the flow is global, and by LaSalle it converges to `u*(C)`.
- Since `w_z ≥ 1/S`, the decay is at least `dE_C/dt ≤ −(2Γμ_1/S) E_C`, where `μ_1` is the smallest nonzero eigenvalue of `−M`.

(iii) *The slaved chain (Γ = ∞: `u = u*(C)` at all times).*
- Its rates are `Z(C)/S` times block 95's rates.
- Block 95 T2 gives detailed balance for `π95 ∝ W exp[qλ(1−2a) Σ_pairs G]`, and a configuration-dependent time change `f(C)` turns a reversible law `π` into `π/f`. So the slaved chain's law is `π_∞ = π95 / Z(C)`.
- CHECKED C: the balance identity in log form holds for every move with `a ∈ {1, ½, 0, 3/7}`.
- For one record `Z` does not depend on the position. For two records it does, from order `λ²`: on ring 6, `Z = V + λ² c2(D) + O(λ³)` with `c2 = 56/27, 89/108, 8/27` at `D = 1, 2, 3`.
- I do not prove that the `Γ → ∞` limit of the relaxing process's stationary law is `π_∞`; that is a singular-perturbation statement. S4 and S8 agree with it at their orders.

**S3 (PROVED; CHECKED D). Jump chains (`a = 1`, `W = 1`).**

(i) *One record.*
- Every neighbour is empty and every hop has rate `r0 w_X`, so each step is uniform on `E` whatever the field.
- The mean one-step increment of `|X|²` is exactly 1, so `|X|² − (number of hops)` is a martingale and `E|X(t)|² = E N(t)`.
- Under A0 the diffusion constant is exactly `R/(2d)` in lattice units, at every `Γ` and `λ`.
- The field acts on the record only through waiting times.

(ii) *Two records, separation `D = x2 − x1 ≠ 0`.*
- Record 1 moving by `e ≠ D` sends `D` to `D − e`; record 2 moving by `e ≠ −D` sends `D` to `D + e`.
- Each of these maps reaches every `D′ ∈ N(D)\{0}` exactly once (CHECKED D on rings 3–6, 3×3, 4×4, 3³ and 4³).
- So, given a hop, `D′` is uniform on `N(D)\{0}` whatever the two clocks and whichever record moves.
- The separation's jump chain is therefore exactly simple random walk on `T\{0}` at every `Γ` and `λ`, with stationary law `ν(D) ∝ deg(D) = q − [D ∈ E]`.
- Under A0 the time-stationary pair law is `π(D) = ν(D) τ̄(D) / Σ ν τ̄`, where `τ̄(D)` is the mean sojourn per visit. The pair law is fixed entirely by the mean sojourn times.

**S4 (PROVED given A1; CHECKED E). First order in λ, for every Γ > 0, every N and every a (W = 1).**

(i) *The λ = 0 process.*
- Put `S = V`, so that `w ≡ 1` at `λ = 0`, and write `u = λφ`.
- At `λ = 0` the records do symmetric exclusion: each empty–occupied bond exchanges at rate `r0`. This is stirring.
- The rescaled field obeys `dφ/dt = Γ(Mφ + n_C − n̄)`, the clause divided by `λ` in the limit. Its sum is `Σφ = 0` (S1 at first order).

(ii) *The moment equations.*
- Under the `λ = 0` stationary law `P0` (`π0` uniform; `φ` a bounded linear filter of the record history), set `m(C) := E_0[φ 1{C}] ∈ R^V`.
- Dynkin's formula for `f = 1{C = C0} φ_z` gives the closed linear system

  `Γ[M m(C0) + π0 (n_{C0} − n̄)] + r0 Σ_{C∼C0} (m(C) − m(C0)) = 0` for all `C0`,

  where `C ∼ C0` runs over the configurations one allowed move away. The relation is symmetric.

(iii) *The solution: `m(C) = π0 γ φ*(C)`, with `φ*(C) = q Σ_{r∈C} G(· − r)` and `γ = Γ/(Γ + r0 q)`.*
- `M φ*(C) = −(n_C − n̄)`, from `ΔG = δ − 1/V`.
- The stirring identity is `Σ_{C∼C0} (n_C − n_{C0}) = −Δ n_{C0}`. An exchange across an empty–occupied bond changes `n` by `δ_y − δ_x`; an exchange across a bond with equal contents changes nothing.
- Hence `Σ_{C∼C0} (φ*(C) − φ*(C0)) = q G∗(−Δ n_{C0}) = −q(n_{C0} − n̄)`.
- Substituting, the left side of the system equals `π0 (n_{C0} − n̄)[Γ(1 − γ) − r0 q γ] = 0`. ∎
- CHECKED E, with exact residual 0 in 64 cases:
  - rings 5–7, 3×3, 4×4, 3³ and 4³;
  - `N = 1–3`, `Γ ∈ {⅓, 1, 5/2}` and `a ∈ {1, ½, 0}`.
- Both controls fail in all 42 control cases: `γ = 1` (the slaved field) and `γ = Γ/(Γ + 1)`.

(iv) *Uniqueness.*
- The operator `m ↦ (Γ M m(C) + r0 Σ_{C′∼C}(m(C′) − m(C)))_C` is `ΓM ⊗ I + I ⊗ Q0`.
- `M` and `Q0` are symmetric, negative semidefinite, and act on different factors. So the kernel consists of vectors constant in both `z` and `C`: it is spanned by `m ≡ 1`.
- The solution is then fixed by `Σ_{C,z} m = E_0[Σφ] = 0`.
- CHECKED E: exact rank 49/50 on ring 5 with `N = 2`, and 89/90 on ring 6 with `N = 2`.
- Consequence: **`E_0[φ | C] = γ φ*(C)`.** At first order in `λ`, the conditional mean clock field given the records is `γ` times the slaved field: the same shape, with its depth reduced by `γ`, for every configuration and every number of records.

(v) *The record law at `O(λ)`.*
- Dynkin's formula for `f = 1{C = C0}`, expanded to `O(λ)` under A1, gives the stationarity equation of the chain with rates `r0 (1 + λγ[a φ*_x(C) + (1−a) φ*_y(C)])`. This is block 95's slaved chain with `λ → γλ`.
- By block 95 T2 at coupling `γλ`, its `O(λ)` law is `π0 (1 + qγλ(1−2a)(P(C) − P̄))`, with `P = Σ_pairs G`. It is unique because stirring is irreducible.
- CHECKED E: the `O(λ)` master equation, with the exact `m`, is solved with residual 0.

(vi) *Readings.*
- **(b) The pair law.**
  - At first order in `log κ`, block 95's pair law survives with `log κ → γ log κ`, where `γ = 2Γ/(2Γ+1) = 1 − 1/(2Γ) + 1/(4Γ²) − …`.
  - At `a = 1` the separation weight is `∝ 1 − qγλ(G(D) − P̄)`. On ring 6 this gives `π1/π0 = −⅓, ⅙, ⅓` (times `γλ`) at `D = 1, 2, 3`.
  - The first-order correction in `1/Γ` multiplies the exponent by `(1 − 1/(2Γ))`. At this order in `λ` the result is exact in `Γ`.
- **(a) One record.**
  - `R = r0 q E[e^{u_X}] = (r0 q V/S)[1 + γqλG(0)] + O(λ²)`.
  - With `R_∞ = (r0 q/S) Z e^{qλG(0)}` and `R_0 := r0 q V/S`: **`R = R_0 + γ(R_∞ − R_0) + O(λ²)`**, that is, **`R/R_∞ = 1 − qλG(0)/(2Γ+1) + O(λ²)`**.
  - The `1/Γ` coefficient `−qλG(0)/2` is the referee side computation R4.
  - For `κ < 1` (`λ < 0`) the lagging record is faster than the slaved one. The record's own well, `E[u_X]/λ = γ qG(0)`, is shallower by the factor `γ`: ring 6 gives `γ·35/36`, and 3³ gives `γ·88/81`.

**S5 (PROVED given A0; float S). An exact identity at every λ and Γ** (one record, `a = 1`, `W = 1`).
- For `f = u_X`: `Lf = Γ w_X((Mu)_X + λ(1 − 1/V)) + r0 w_X Σ_e (u_{X+e} − u_X) = w_X[(Γ + r0 q)(Mu)_X + Γλ(1 − 1/V)]`.
- Stationarity then gives **`E[w_X (Mu)_X] = −γ λ (1 − 1/V) E[w_X]`**, while the slaved field has `(Mu*)_X = −λ(1 − 1/V)`.
- So at the record's departures (the rate-weighted average), the log-clock contrast between its neighbourhood and its site is exactly `γ` times the slaved contrast, at every coupling.
- [float] The relative residual is `4·10⁻⁵` at `λ = −1.5`, `Γ = 1` on ring 6.

**S6 (PROVED given A0; CHECKED F). No product law.** Let `λ ≠ 0`, `0 < Γ < ∞`, `1 ≤ N ≤ V − 1`, any real `a` and any positive `W`. Then no stationary law `μ(C) Q(du)` exists, for any probability measure `Q` on `R^V`.

(i) *`Q` is carried by a line.*
- Set `ρ := Σ_C μ(C) n_C` (so `Σρ = N`), and let `u_ρ` be the mean-zero solution of `M u_ρ = −λ(ρ − n̄)`.
- Let `E_ρ(u) = ½⟨u − u_ρ, −M(u − u_ρ)⟩` and `S(u) = Σ e^{−u_z}`.
- Take `f(C,u) = h(E_ρ(u)) ψ(S(u))`, where:
  - `h ∈ C¹` is bounded, and `h′ ≥ 0` is supported in `[ε, K]` and positive inside;
  - `ψ ∈ C¹_c((0,∞))` and `ψ ≥ 0`.
- Jumps do not change `f`, and `S` is invariant under every flow (S1). Averaging over `μ`, which enters linearly through `n`,

  `∫ Lf d(μ⊗Q) = −Γ ∫ ψ(S) h′(E_ρ) Σ_z w_z ((M(u − u_ρ))_z)² Q(du)`.

- On the support of `h′(E_ρ)ψ(S)` the vector `u` lies in a compact set, because `E_ρ` bounds its oscillation and `S` its level. So A0 applies and the integral is 0.
- The integrand is ≥ 0, and > 0 wherever `h′ψ > 0`, because there `E_ρ > 0` and so `M(u − u_ρ) ≠ 0`.
- Letting `ε → 0` and `K → ∞`, and exhausting `(0,∞)` by supports of `ψ`, gives `Q(E_ρ > 0) = 0`. So `Q` is carried by the line `u_ρ + R1`.

(ii) *A test function coupling configuration and field.*
- Take `f = χ(C) ℓ(u − u_ρ) ψ(S) φ(E_ρ)`, where:
  - `χ` is arbitrary;
  - `ℓ` is linear with `ℓ(1) = 0`;
  - `φ ∈ C¹_c([0,∞))` equals 1 near 0.
- On the line:
  - `ℓ(u − u_ρ) = 0`, so the jump part vanishes;
  - the derivatives of `ψ(S)` along the flows, and of `φ(E_ρ)`, vanish;
  - with `w = e^c w_ρ`, the drift of configuration `C` equals `Γλ e^c w_ρ ⊙ (n_C − ρ)` (CHECKED F).
- Hence `0 = Γλ [∫ e^c ψ dQ] Σ_C μ(C) χ(C) ℓ(w_ρ ⊙ (n_C − ρ))`.
- Choose `ψ` with `∫ e^c ψ dQ > 0`. Then for every `C` with `μ(C) > 0` and every `ℓ ⊥ 1`, we get `w_ρ ⊙ (n_C − ρ) = β1`.
- Summing `n_C − ρ = β/w_ρ` gives `0 = β Σ 1/w_ρ`. So `β = 0` and `n_C = ρ` (CHECKED F).
- Every supported configuration therefore has the same occupation vector: `μ = δ_{C0}` and `ρ = n_{C0}`.

(iii) *Escape from `C0`.*
- Take `f = 1{C = C0} ψ(S) φ(E_ρ)`.
- On the line the drift of `C0` vanishes, since the line consists of `C0`'s equilibria. So `Lf = −k_out(C0, u) ψ(S) < 0` wherever `ψ > 0`.
- Here `k_out > 0`: some record has an empty neighbour, and block 95's rates are positive.
- So `∫ Lf dπ < 0`, a contradiction. ∎

Attempt a2 treated `Q` as a point mass, and the referee's repair covered point masses. This proof covers every `Q`.

**S7 (PROVED given A0). No stationary law of the joint process is reversible**, for `λ ≠ 0` and every finite `Γ > 0` (any `a` and `W`, `1 ≤ N ≤ V − 1`).
- Write `F(C,u) = Γ w ⊙ (Mu + λ(n_C − n̄))`. Under A0, `u(t) − u(0) = ∫_0^t F(C_s, u_s) ds`.
- For the reversed path `x̃(t) = x((T − t)−)`, we get `ũ(t) − ũ(0) = −∫_0^t F(C̃, ũ) dr`.
- Let `Φ(x) = ∫_0^T |u(t) − u(0) − ∫_0^t F ds| dt`.
  - On forward paths `Φ = 0` almost surely.
  - On reversed paths `Φ = 2 ∫_0^T |∫_0^t F(C̃, ũ) dr| dt`.
- Equality in law therefore forces `F(C_s, u_s) = 0` for almost every `s`, almost surely.
- Then `u` is constant and `Mu + λ(n_{C_s} − n̄) = 0` for almost every `s`.
- With positive probability two different configurations are each occupied for positive time in `[0,T]`. That gives `λ(n_C − n_{C′}) = 0`, so `λ = 0`. ∎

At `Γ = ∞` the configuration chain is reversible (block 95 T2). Reversibility is lost exactly when the clock lags.

**S8 (PROVED at first order in 1/Γ, remainder under A0; CHECKED H). The sojourn route.** This is an independent check of S4 at order `λ/Γ`, and it is exact in `λ` for one record.

(i) *One record.*
- After a hop from `x` to `y`, the field starts at `u*(x) + O(e^{−cΓτ_prev})`. The previous sojourn is shorter than the relaxation time only with probability `O(1/Γ)`.
- In rescaled time `s = Γt`, the lag `v = u − u*(y)` obeys `dv/ds = e^{u*(y)+v} ⊙ Mv`, which does not contain `Γ`.
- Write `ε = e^{v_y} − 1`; then `∫|ε| = O(1/Γ)`. Expanding `E τ = ∫ e^{−R_∞ t − R_∞ ∫_0^t ε} dt` gives

  `E τ = 1/R_∞ − J(λ)/Γ + O(Γ⁻²)`, with `J(λ) = ∫_0^∞ (e^{v_y(s)} − 1) ds`.

  The error from replacing `e^{−R_∞ s}` by 1 is at most `R_∞ ∫ s|ε| = O(Γ⁻²)`.
- So **`R/R_∞ = 1 + R_∞ J(λ)/Γ + O(Γ⁻²)`**, exactly in `λ`.
- At first order in `λ`:
  - `∫_0^∞ v ds = (1/w0)(−M)⁺ v(0) = (q/w0) G∗v(0)`, with `v(0) = qλ(G(· − x) − G(· − y))`.
  - At the record's site this equals `(q²λ/w0)(G2(e) − G2(0)) = −qλG(0)/w0`. The last step uses `ΔG2 = G`, which gives `G2(0) − G2(e) = G(0)/q` (CHECKED A, H).
  - With `R_∞ = r0 q w0`, this gives `R_∞ J = −qλG(0)/2`, as in S4.
- [float] On ring 6 at `λ = −1.5`, `R_∞ J(λ) = 0.352`: 0.48 of the linear value, with the same sign.

(ii) *Two records at order `λ/Γ`.*
- After an arrival at `D` from `D′ ∈ N(D)\{0}`, by either record, the same computation gives

  `E[τ | D′, D] = (1/R_∞(D)) [1 + (r0 deg(D) λ/Γ)(qG(0) − q²(G2(D′) − G2(D)))] + O(λ²/Γ, Γ⁻²)`.

- In the reversible jump chain of S3, the arrival neighbour is uniform on `N(D)\{0}`.
- The identity `Σ_{D′∈N(D)\{0}} (G2(D′) − G2(D)) = −G(D) − [D∈E] G(0)/q` (from `ΔG2 = G`; CHECKED H for all `D`) makes the mean shift `−(r0 q² λ/Γ)(G(0) + G(D))`.
  - This holds for adjacent and distant `D` alike, because `deg(D)` cancels.
- With `ν ∝ deg` and `R_∞(D) ∝ deg(D) w*(D)`, this gives `π(D) ∝ exp(−qλ(1 − 1/(2Γ)) G(D)) / Z(D)` at this order: S4's `γ`, to first order in `1/Γ`.

(iii) *The observed separation process is not time-reversible at order `λ/Γ`.*
- The forward sojourn at `D` depends on the arrival neighbour `D′`, through `G2(D′)`.
- The next separation is uniform and independent of the sojourn (S3). Time reversal would make the sojourn depend on the departure neighbour instead of the arrival one.
- `G2` takes different values on `N(D)\{0}` (CHECKED H):
  - ring 6, `D = 2`: `{−265/864, 119/864}`;
  - 3³, `D = (0,0,1)`: `{−19/8748, 23/2187}`.

**S9 (PROVED given the averaging principle, ASSUMED; CHECKED K). The quasi-static limit Γ → 0, one record.**
- *The limit rate.* For a frozen field the departure-timed record has stationary law `∝ 1/w` (block 53 T5). Its long-run rate is `Σ_x (w_x⁻¹/S) q r0 w_x = q r0 V/S`, the same for every field on the level set. So `R → R_0 = r0 q V/S` as `Γ → 0`, at every `λ`.
- *Comparison with the slaved rate.*
  - `R_0/R_∞ = V e^{−qλG(0)}/Z`.
  - `G(0) > G(z)` for every `z ≠ 0`. By Fourier, `G(0) − G(z) = V⁻¹ Σ_k (1 − cos k·z)/E(k) > 0`; CHECKED A.
  - So `R_0 > R_∞` iff `λ < 0`.
- *Stability of the uniform quasi-static field.*
  - At the uniform field the dwelling density responds as `δρ = −δu/V`. So the growth rate of each mode is `Γ w0 (μ − λ/V)`, for each eigenvalue `μ < 0` of `M`.
  - The uniform field is unstable iff `λ < V μ_1`, where `μ_1 = −(2 − 2cos(2π/L))/q`.
  - The thresholds are −3 on ring 6, −27/2 on 3³ and −64/3 on 4³.
  - I do not treat what replaces the uniform field beyond that coupling.

## 3. Where the route stops

1. *Not exact in λ at finite Γ.* The closure in S4 uses stirring's one-point function at `λ = 0` and a rate perturbation that is linear in the field. At `O(λ²)` the `λ = 0` dynamics still closes the second-moment equations (a linear field driven by stirring), so the `O(λ²)` law is finite linear algebra. I did not do it.
2. *Assumptions.* S4 needs A1, and S5–S8 need A0. Neither is proved. The float family S (ring 6) is consistent with both:
   - At `λ = ±0.2` and `Γ ∈ {¼, 1, 4}`, the one-record coefficient and the pair-law `γ` agree with S4 to about 4σ. They exclude the slaved value.
   - At `λ = −1.5` the rate falls from about `R_0` (`Γ = 0.01`) toward `R_∞` (`Γ = 10`).
   - That `R(Γ)` is monotone is an observation, not a claim.
3. *No closed form.* The first-order-in-`1/Γ` coefficient at finite `λ` is the functional `J(λ)` of a finite nonlinear ODE, and I have no closed form for it.
4. *General W.* It is not treated: at `λ = 0` the records do not stir, and the one-point function does not close.

## 4. What would finish it

- **A0.** Non-explosion from a Lyapunov function in `u` that is uniform over configurations.
  - The quadratic forms tried here fail, because the `w`-weighting lets exponential weights beat them.
  - Ergodicity would then follow from S2's uniform contraction and irreducibility.
- **A1.** Differentiability of the stationary law at `λ = 0`, for instance from uniform geometric ergodicity on a compact invariant set.
- **The `O(λ²)` pair law**, from the second-moment system (finite and exact).
- **The localized quasi-static branch** for `λ < Vμ_1`: averaging, followed by a fixed point of Poisson–Boltzmann type.

## Answers

- **(a) No self-trapping.**
  - The jump chain is simple random walk at every `Γ`, and the diffusion constant is exactly `R/(2d)`. The trail acts only through waiting times.
  - At first order in `log κ`, the record's own well is shallower by the factor `γ`, and `R = R_∞[1 − q log κ · G(0)/(2Γ+1)] + O(log²κ)`.
  - For `κ < 1` the lagging record is faster than the slaved one, and the two limits satisfy `R_0 > R_∞` at every `κ < 1`.
- **(b) The pair law and reversibility.**
  - At first order in `log κ` the pair law survives with `log κ → γ log κ`, where `γ = 2Γ/(2Γ+1)`. Its first-order correction in `1/Γ` multiplies the exponent by `(1 − 1/(2Γ))`.
  - The joint process is reversible for no finite `Γ`, and the observed separation is not reversible at order `log κ/Γ`.
- **(P)** No stationary joint law of the form (record law) × (field law) exists at finite `Γ` when `log κ ≠ 0`.
