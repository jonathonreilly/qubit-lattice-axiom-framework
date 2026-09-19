# plane-memory-loss, attempt 3 (worker w-macbookpro90c72-j17cb, model grok-4.6)

No prior attempt was printed at claim time. Route: make the three suggested arguments exact enough to see which step fails, and record the identities a later proof would use. Definitions from PR #8170 (block 26 T1–T5, N1.4) and PR #8171 (block 27 T1–T4).

The object is the unsoldered sphere formation law in level order: `K_β(s | S) ∝ e^{β s·S}`, `S` the sum of the three recorded predecessors, read as a synchronous automaton on `Z^2`. Magnetization from the aligned plane: `m_t = E[s_x(t) · e]`. Block 26 executes `m_t → 0` at `β = 3,6,12,24` on large finite planes; block 27 proves it for `β < 1/√3`. The infinite-plane statement at every `β` is open.

## (1) The statement attempted

Route (i) (path-space twist) fails at the bounded-cost step. Route (ii) (linear comparison) cannot be closed because the unconstrained linear variance diverges while `|s|=1`. Route (iii) (invariance plus uniqueness) is block 26 T4 on every finite torus and block 27 T2 for `β < 1/√3`; it does not pass to `Z^2` without a mixing-time bound uniform in `L`. The sharp small-field Wasserstein Lipschitz constant of the kernel is `1/3`, not `1/√3`; a global `W_1(K_V, K_{V'}) ≤ |V−V'|/3` would extend uniqueness to `β < 1`, and is the first unproved step of that extension. Mean-field forgets iff `β ≤ 1`. Identities: `KL(vMF(κ u) || vMF(κ u')) = κ A(κ)(1−u·u')`; one-dimensional `W_1` of the `z`-marginals, uniform against `vMF(κ e)`, equals `A(κ)`; `P_1=1/3`, `P_2=5/27`, `P_3=31/243`, `P_4=71/729`.

## (2) Steps

**Step 1 — Langevin bounds (PROVED; CHECKED L).** `A(κ)=coth κ − 1/κ`. `A(κ) < κ/3` for `κ>0` because `u(κ)=(κ²+3)sinh κ − 3κ cosh κ` has `u(0)=0` and `u'(κ)=κ(κ cosh κ − sinh κ)` with `(κ cosh − sinh)'=κ sinh ≥ 0`. `A(κ)/κ` is decreasing (`A'(0)=1/3`; the polynomial `κ² sinh²κ − 3 sinh²κ + 3κ²` has vanishing Taylor coefficients through order `κ^5` and nonnegative coefficients thereafter). Consequently `F(V)=A(|V|) V/|V|` is `(1/3)`-Lipschitz at the origin, and `A(3β m) ≤ β m` with equality only at `m=0`.

**Step 2 — route (i) fails (PROVED; CHECKED K).** For two equal-concentration von Mises–Fisher laws the relative entropy is the exponential-family identity

    KL(K_{κ u} || K_{κ u'}) = κ A(κ) (1 − u·u').

A spatial twist that rotates a predecessor by an angle `θ` therefore costs `(κ A(κ)/2) θ² + O(θ⁴)` nats per site (CHECKED K.2). On an `L×L` torus a unit global in-plane rotation is a gradient of size `θ ∼ 1/L`. Summing `N=L²` sites and `T` levels, the path-space cost is `Θ(T)`, independent of `L` (CHECKED K.4). A twist of bounded cost as `L→∞` at fixed `T` does not exist, and sending `T→∞` makes the cost unbounded. This is block 26 N1.4, with the KL written exactly. The equilibrium box argument that uses a bounded-cost twist therefore gives nothing in level time. **First failing step of route (i): the cost is `Θ(T)`, not `o(T)`.**

**Step 3 — one-dimensional Wasserstein identity (PROVED; CHECKED W).** The `z`-coordinate of the uniform measure on `S²` is uniform on `[−1,1]`; under `vMF(κ e)` it has quantile `Q(p)= −1 + log(1+p(e^{2κ}−1))/κ`. The one-dimensional `W_1` is

    ∫_0^1 (Q_vMF − Q_unif) dp = (κ e^{2κ} + κ − e^{2κ} + 1) / (κ (e^{2κ}−1)) = A(κ)

identically (CHECKED W.1). Projection onto `e` therefore gives `W_1^{R^3}(uniform, vMF(κ e)) ≥ A(κ)`. Combined with Step 1, the small-field Lipschitz constant of the kernel in `W_1` is exactly `1/3` (since `A(κ)/κ → 1/3`), which is strictly smaller than block 27's `1/√3`. With three predecessors a factor `1/3` would yield contraction `β` (threshold `β<1`); the factor `1/√3` yields `√3 β` (threshold `β<1/√3`).

**Step 4 — the first unproved step of a `β<1` extension (PROVED as a reduction; the inequality ASSUMED and not checked globally).** A causal `W_1` coupling satisfies `D_{t+1} ≤ Lip · E|V−V'|` with `V=β S`. If `W_1(K_V, K_{V'}) ≤ |V−V'|/3` for all `V,V'`, then `D_{t+1} ≤ (β/3) E|S−S'| ≤ β D_t`, uniqueness and exponential forgetting for `β<1`. The inequality holds in the small-field limit (Step 3) and would match the mean-field threshold (Step 6). It is **not** established away from `V=0`: `W_1 ≥ |F(V)−F(V')|` (block 27 T4) and `|F|` has Lip `≤ 1/3`, but `W_1` can exceed the distance of means. **This is the first failing step of route (ii)'s coupling half.** Block 27 T4 already notes that no coupling of this kind passes `β=1`; the new content is the sharp constant `1/3` at zero and the exact `z`-marginal identity.

**Step 5 — linear comparison does not close (PROVED as a no-go).** The linearized transverse variance is `v_t = (A(3β)/(3β)) ∑_{k<t} P_k` per component (block 26 T5), with `P_k = ∑_y p_k(y)^2` the return sum of the three-predecessor walk (each step `(0,0)`, `e_1`, or `e_2` with probability `1/3`). Exact: `P_1=1/3`, `P_2=5/27`, `P_3=31/243`, `P_4=71/729` (CHECKED P). The local-limit `k P_k → 3√3/(4π)` gives `γ(β)=(3√3/(4π)) A(3β)/(3β)` and `v_t ∼ γ(β) log t → ∞`. On the sphere `|s|=1` forces the actual transverse second moment to be `≤ 1`, so the linear recursion is not a lower bound once `v_t` is order one. The comparison with the linear model therefore fails at the step “the linear variance is a lower bound for the nonlinear one”: it is an upper-regime description of small fluctuations, not a Lyapunov function on the sphere. Recurrence of `P` is why the linear field diverges, and why the linearization cannot be used globally.

**Step 6 — mean-field (PROVED; CHECKED M).** Ignoring fluctuations, `m_{t+1}=A(3β m_t)`. Step 1 gives `A(3β m) ≤ β m`, so the only fixed point in `[0,1]` is `0` when `β ≤ 1`, and it is globally attracting on `[0,1]`. For `β>1` the map has a positive fixed point (mean-field order). On the one-site plane, `S=3 s_t` with `|S|=3` always, so `m_t=A(3β)^t` from the aligned state (block 27 T3). Mean-field without fluctuations is not the infinite-plane law: fluctuations are what block 26 sees at `β=3>1`.

**Step 7 — route (iii) (PROVED as a reduction).** The kernel is `O(3)`-covariant, so any unique invariant law is rotation-invariant and has `m=0`. Uniqueness holds on every finite torus at every `β` (block 26 T4) and on `Z^2` for `β<1/√3` (block 27 T2). Passing uniqueness to `Z^2` at large `β` needs a mixing time `o` of the observation time, uniformly in `L`. No such bound is proved; the finite-`L` forgetting of T4 can be as slow as one likes in `L`. **First failing step of route (iii) at large `β`: uniformity in `L`.**

## (3) Where the route stops

The infinite-plane statement `m_t → 0` for every `β` is not proved. Route (i) is closed as a no-go. Route (ii) is reduced to a global `W_1` Lipschitz bound of `1/3` (open) and cannot use the linear variance as a Lyapunov function. Route (iii) is reduced to mixing uniform in `L`. The gap `(1/√3, ∞)` on `Z^2` remains; `(1/√3, 1)` would fall if Step 4's inequality holds.

## (4) What would finish it

A proof or counterexample of `W_1(K_V, K_{V'}) ≤ |V−V'|/3` for all `V,V'` (a spherical-grid linear program at rational `κ` would be a finite check for a counterexample); a second-moment Lyapunov using `E[A(β|S|)(S·e)/|S|]` and a uniform lower bound on `E|S_⊥|²` that does not linearize; a mixing-time bound on the `L×L` torus of the form `T_mix = o(L^∞)` or `poly(L)` at large `β`.
