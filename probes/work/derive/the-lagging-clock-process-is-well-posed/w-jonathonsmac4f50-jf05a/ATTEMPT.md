# Block 169's lagging-clock process is well posed

- **Task:** `J:derive:the-lagging-clock-process-is-well-posed:a1`
- **Worker:** `w-jonathonsmac4f50-jf05a`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)

**Provenance.**
- Block 169 is a supervisor harvest from this machine (same model family). It harvests probe #9158, by `w-macbookpro9927a` (Claude, another machine), refereed by #9325 (Grok).
- This attempt proves the assumption A0 that block 169 leaves open. It is not a review of block 169.
- No attempt on this problem existed on `ai/probes` at claim time.

**Sources.**
- Block 169: pushed branch `physics-loop/admissibility-induced-law-block169-…-20260926`. Its A0, T1 and the process definition are quoted below.
- Block 95, as landed on `origin/main` (`e37967e326`), for the record rates.

## Setting (block 169, as on its branch)

- **The lattice.** A finite torus `(ℤ/L)^d` with `L ≥ 3`: `V` sites, `q = 2d` neighbours, diameter `D = d⌊L/2⌋`.
- **Records.** `N` records, `1 ≤ N ≤ V − 1`, one per site. A record moves `x → y` onto an empty neighbour at rate `exp[a u_x + (1 − a)u_y] h/q`, with `h = W(C′)/(W(C) + W(C′)) ∈ (0, 1)`, `a ∈ [0, 1]` and `W > 0`.
- **Field.** Between jumps the field follows the flow of the current configuration:

      du_z/dt = Γ w_z((Mu)_z + f_z),   f = λ(n_C − n̄),   w = e^u,   M = Adj/q − I,   Γ > 0,   λ ∈ ℝ.

- **Invariant** (block 169 T1). `S(u) = Σ_z e^{−u_z}` is invariant.
- **A0** (block 169, verbatim in substance).
  - The joint process does not explode.
  - Dynkin's formula holds for the test functions used.
  - Where needed, a stationary law exists on each level set of `S`, with finite moments of `w` and `u`, and long-run averages equal its expectations.

## (1) Statement

**Theorem W.** Take every such torus and all `Γ > 0`, `λ`, `a`, `W`, `N`, and a level `s > 0`. Put

    σ = |λ| N(V − N)/V,
    T₁(K) = K + 1/e,
    T_ℓ(K) = K + 1 + T_{ℓ−1}(K e^{K+1}),
    F* = V (log(V/s) + T_D(qσ)).

Then:

- **(a) Uniform bound.** Along every path of the joint process, and indeed along every switching signal between the flows, `F(t) = Σ_z u_z(t) ≤ max(F(0), F*)`. Hence

      −log s ≤ u_z(t) ≤ max(F(0), F*) + (V − 1) log s   for all z, t.

- **(b) No explosion.** Jump rates are bounded by `N e^{U}`, where `U` is the bound in (a). There is no explosion, and Dynkin's formula holds for bounded `C¹` test functions of `(C, u)`.
- **(c) A stationary law.** On each level set `S = s`, a stationary law exists. It is supported in the compact forward-invariant set `K*_s = {S = s, F ≤ F*}`, so all moments of `u` and `w` are finite.
- **Not proved.** The uniqueness or ergodicity of the stationary law, that is, A0's clause "long-run averages equal its expectations".

## (2) Steps

### Step 1 — the derivative of F (PROVED; CHECKED X1)

For any vectors `a` and `b`, `Σ_z a_z(Mb)_z = −(1/q) Σ_edges (a_x − a_y)(b_x − b_y)`. Each unordered edge appears twice in `Σ_z a_z Σ_{y∼z}(b_y − b_z)`. So along the flow of any configuration:

    dF/dt = Γ [ Σ_z w_z f_z − (1/q) Σ_edges (w_x − w_y)(u_x − u_y) ],

and every edge term is `≥ 0`, since `w = e^u` is increasing. X1 checks this exactly for random rational vectors on ring 5, the `3×3` torus and the `3³` torus. Jumps do not change `u`, so `F` is continuous along paths.

### Step 2 — the level set (PROVED from block 169 T1; CHECKED X2)

- `S = s` is invariant (X2: `M` has zero column sums and `Σf = 0`).
- Each `e^{−u_z} ≤ s`, so `u_z ≥ −log s`.
- `max_z e^{−u_z} ≥ s/V`, so `u_min ≤ log(V/s)`.

### Step 3 — the source (PROVED; CHECKED X3)

- `Σf = 0`, so `Σ w f = Σ (w − w_min) f ≤ (W − w_min) Σ f⁺`, with `W = max w`.
- `Σ f⁺` equals `|λ|N(1 − n̄) = σ` for either sign of `λ`: records carry `λ(1 − n̄)` and empty sites `−λn̄`.
- X3 tests the bound exactly for random rational `w`, every `N` and `λ = ±7/3`.

### Step 4 — the path lemma (PROVED; CHECKED X4, float screen P1)

Let `Φ(a, b) = (e^a − e^b)(a − b) ≥ 0`.

**Lemma.** Let `a_0 ≥ a_i ≥ a_ℓ` for all `i`, with `A = a_0 − a_ℓ` and `K ≥ 0`. If `A ≥ T_ℓ(K)`, then `Σ_{i<ℓ} Φ(a_i, a_{i+1}) ≥ K e^{a_0}`.

*Proof,* by induction over all lengths up to `ℓ`. `T` is nondecreasing in `ℓ` and in `K`.
- **`ℓ = 1`.** `Φ(a_0, a_1) = e^{a_0}(1 − e^{−A})A ≥ e^{a_0}(A − 1/e) ≥ K e^{a_0}`, using `δe^{−δ} ≤ 1/e` (X4).
- **`ℓ ≥ 2`.** Let `δ = a_0 − a_1 ≥ 0`.
  - If `δ ≥ K + 1`, then `Φ(a_0, a_1) ≥ e^{a_0}(δ − 1/e) ≥ K e^{a_0}`.
  - Otherwise `a_1 − a_ℓ > A − K − 1 ≥ T_{ℓ−1}(Ke^{K+1}) > 0`.
    - Let `M = a_j` be the maximum of `a_1, …, a_ℓ`. Then `j < ℓ`, since `a_1 > a_ℓ`.
    - The sub-path `a_j, …, a_ℓ` has at most `ℓ − 1` steps, starts at its maximum, ends at `a_ℓ`, and drops by `M − a_ℓ ≥ a_1 − a_ℓ`.
    - By induction its dissipation is `≥ K e^{K+1} e^{M} ≥ K e^{K+1} e^{a_0 − δ} > K e^{a_0}`. ∎

**Applying it.** Take a shortest path from the site of `u_max` to the site of `u_min`. Its length is `ℓ ≤ D`, and its values lie in `[u_min, u_max]`. All other edge terms are `≥ 0`, so

    (1/q) Σ_edges (w_x − w_y)(u_x − u_y) ≥ (K/q) W   whenever u_max − u_min ≥ T_D(K).

The float screen P1 checks 4000 random paths per case (`ℓ = 1..3`); the smallest dissipation/`K e^{a_0}` ratio is 1.007.

### Step 5 — the uniform bound (PROVED)

- With `K = qσ`, Steps 1, 3 and 4 give `dF/dt ≤ ΓW(σ − σ) = 0` whenever `u_max − u_min ≥ T_D(qσ)`.
- If `F > F*`, then `u_max ≥ F/V > log(V/s) + T_D(qσ)`. With Step 2's `u_min ≤ log(V/s)`, this gives `u_max − u_min > T_D(qσ)`.
- So `dF/dt ≤ 0` whenever `F > F*`.
- `F` is continuous along paths and only the configuration jumps. Take the last time `F = max(F(0), F*)`: after it `F` cannot increase. Hence `F(t) ≤ max(F(0), F*)`.
- Then `u_max ≤ F − (V − 1)·min u ≤ max(F(0), F*) + (V − 1) log s`.
- Nothing here depends on the switching times, so the bound holds for every switching signal. The float screen S1 (a greedy adversary) stays bounded, at the scale of the fixed-configuration equilibria.
- The same bound gives global existence of each fixed-configuration flow: the vector field is locally Lipschitz and the solution stays a priori bounded.

### Step 6 — no explosion and Dynkin (PROVED; one standard import)

- On `[0, ∞)`, every allowed hop has rate `≤ e^{U}/q`. So the total rate is `≤ N e^{U}`.
- **Construction.** Build the process by thinning. A Poisson clock of rate `Λ̄ = N e^{U}` carries i.i.d. uniform marks. At each tick the current state jumps to `C′` if the mark lies in the interval of length `r(C → C′; u)/Λ̄` assigned to `C′`, and otherwise it stays.
- The number of jumps on `[0, t]` is at most a Poisson(`Λ̄t`) variable, which is finite. So there is no explosion.
- **Dynkin's formula.** For bounded `g(C, u)` that is `C¹` in `u`, the change `g(X_t) − g(X_0)` splits into:
  - the flow part `∫ ∇_u g · Γw(Mu + f_C) ds`;
  - the jump sum.

  The jump sum minus its compensator `∫ Σ_{C′} r(C → C′; u)(g(C′, u) − g(C, u)) ds` is a martingale.
- **ASSUMED (named standard fact).** A compensated marked point process with bounded intensity and bounded marks is a martingale.

### Step 7 — a stationary law on each level set (PROVED)

- **The state space.** `𝒦 = {configurations} × K*_s` is compact and forward invariant (Step 5, with `F(0) ≤ F*`).
- **Feller property.** Fix the clock and marks, and an initial point `x₀`.
  - With probability one no mark lies exactly on an interval endpoint at the state it is used in.
  - Flows depend continuously on initial data (they are Lipschitz on `K*_s`), and the endpoints depend continuously on `u`. So nearby initial points make the same jump decisions, and `X_t(x) → X_t(x₀)`.
  - By bounded convergence, `P_t g` is continuous for continuous `g`.
- **Krylov–Bogoliubov.**
  - The averages `μ_T = T⁻¹∫_0^T δ_{x₀}P_t dt` are tight, since `𝒦` is compact.
  - Any weak limit `μ` satisfies `μ(P_s g) = lim μ_T(P_s g) = lim T⁻¹∫_0^T P_{t+s} g(x₀) dt = μ(g)`.
  - So `μ` is stationary, supported in `𝒦`, and all its moments are finite.

## (3) Where it stops

- **The first unresolved step is uniqueness, or ergodicity, of the stationary law.** It is needed for "long-run averages equal its expectations", which block 169 T2's time-stationary pair law uses.
- **What does not transfer.** For a common record path, the field copies contract in the `H⁻¹` norm of `v = e^{−u}`. A pointwise proof gives `d/dt ½‖v − ṽ‖²_{H⁻¹} = −Γ⟨v − ṽ, log v − log ṽ⟩ ≤ 0`. But the record paths of two copies depend on their fields, so this does not yet give a coupling.
- **A1** (differentiability at `λ = 0`) is not addressed.
- **The threshold.** `F*` is explicit but astronomically large: `T_D` is an iterated exponential of height about `D`. It is a proof bound, not an estimate.

## (4) What would finish it

- A coupling of two copies that meets in configuration, with positive probability, and then uses the `H⁻¹` contraction. Alternatively, a minorisation (Harris) on `𝒦` giving a unique stationary law on each level set.
- For A1: differentiability of that stationary law in `λ`, for example through a spectral gap of the linearised generator.

## ASSUMED

- The supplied clauses of block 169 and block 95.
- That compensated marked point processes with bounded intensity are martingales (standard).

Everything else is proved above. The finite identities are exact (X1–X4). P1 and S1 are float screens only.

## Reproduce

```bash
python3 probes/work/derive/the-lagging-clock-process-is-well-posed/w-jonathonsmac4f50-jf05a/check.py
```

The run takes about 1 s.
