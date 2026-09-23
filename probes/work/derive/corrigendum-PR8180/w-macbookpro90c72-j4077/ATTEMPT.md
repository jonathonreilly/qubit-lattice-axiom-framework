# Corrigendum packet for PR #8180 (block 35): derivation attempt 1 of 2

Worker `w-macbookpro90c72-j4077` (claude-opus-5-5), unit `J-derive-corrigendum-PR8180-a1`.

**Sources, pinned by commit.** Line numbers below are the lines at these commits.

- Block 35, PR #8180 head `7c844adf`: the note, runner, control and refuting spec, and the pack files.
- Block 34, PR #8178 head `e6ffae5b`: note and runner.
- Block 13, PR #8147 head `9c364d1d`.
- Block 26, PR #8170 head `f9e11770`.
- The other notes of PRs #8146–#8180 and the #8179 decision record, at their branch heads.

`check.py` in this directory verifies each finite claim exactly (family `Q` re-reads the 20 quoted lines verbatim). Nothing in it uses floating point. It runs in about 2 s.

**Provenance and independence.**
- No earlier unit of mine touched PR #8180. The other PR #8180 units from this machine's worker prefix were grok-4.6 workers.
- I formed the plan below before reading the prior attempt `a2` (`w-jonathonsmac4f50-jb8bf`, claude-opus-5). There is no referee log for `a2`, so none of it is GIVEN.
- After finishing the route I compared with `a2`. We agree on the T1 diagnosis and on the counts `8/24` (L = 3) and `19/45` (L = 4). I recomputed those in a different exact field: my own Q(ζ₁₂) class here, against sympy's Q(√3, i) in `a2`.
- Where the routes differ:
  - New here for T1: L = 6 (`47/105`, `24/36`); the exact form of the set where the multiplier sentence holds; the transposed-matrix computation of L106's first line.
  - New here for T3/D2: a frame-free route. It has three parts: a zero-set lemma that rules out a product in **every** frame; the Hessian-rank separation with its invariance proof; and the structural reason the drift is shared (both inverse kernels depend on level time only through `Re(φe^{iw})`).
  - New here for (b): block 13's T3(ii) already states the correct separation.
  - `a2` works through explicit (k, τ) propagators and rates. I use those only as a corollary (S13), checked at two exact modes.
- `a2` and I are both Claude models. Independence in the model-family sense has to come from the referee.

## 1. The statement attempted

**Conventions.** Each is quoted verbatim by `check.py` Q.

- **P.** `(Pθ)_x = (θ_x + θ_{x−e₁} + θ_{x−e₂})/3`. Source: note L85, "the predecessors of `(i, j)` are `(i, j)`, `(i − 1, j)`, `(i, j − 1)`"; control L17 uses `np.roll(s, 1, ·)`.
- **Characters.** `e_k(x) = e^{ik·x}` with `k ∈ (2π/L)Z_L²`. Also `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`, `u = |φ|²` and `y = √(1 − u)`.
- **Minus transform.** `θ̂_k = L^{−1}Σ_x e^{−ik·x}θ_x`, block 34's transform (b34 L85). Block 35 L86 takes its modes from block 34.
- **+ik transform.** `θ̂⁺_k = L^{−1}Σ_x e^{+ik·x}θ_x`.
- **Pairing.** `Cov(X, Y) = E[(X − EX)·conj(Y − EY)]`. This is the executed pairing: note L88 `E[ŝ_⊥(k,t) ŝ_⊥(k,t+s)*]`, and control L37 `past·conj(cur)` with numpy's forward DFT at L27.
- **The cross-covariance operator.** `Σ_{t,t+s} := [Cov(θ_{x,t}, θ_{x',t+s})]_{x,x'}`.

**T1′ (the corrected T1).** From `θ_0 = 0`, for every `L`, every `k`, `t ≥ 1` and `s ≥ 0`:

- **(a)** `P e_k = conj(φ(k)) e_k` and `Pᵀ e_k = φ(k) e_k`.
  - With the minus transform, `(Pθ)^_k = conj(φ(k)) θ̂_k`. Block 34's "`P` acts as multiplication by `φ(k)`" (b34 L85, L104, L108) and block 35's "multiplier `φ(k)`" (L86) therefore hold exactly on the modes with `φ(k) ∈ ℝ`.
  - Those modes are `k₁ + k₂ ∈ 2πZ` or `k₁ − k₂ ∈ π + 2πZ`.
  - With the +ik transform the multiplier is `φ(k)`.
- **(b)** Minus transform, executed pairing:
  - `Cov(θ̂_k(t), θ̂_k(t+s)) = φ(k)^s Var θ̂_k(t)`;
  - `Var θ̂_k(t) = σ²(1 − u^t)/(1 − u)` for `u < 1`, and `σ²t` at `k = 0`.

  **This is block 35's display (L104), verbatim.** With the +ik transform and the same pairing the covariance is `conj(φ)^s Var`.
- **(c)** `Σ_{t,t+s} = Σ_t (Pᵀ)^s`.
  - On the minus mode `k` it multiplies by `φ^s σ²(1 − u^t)/(1 − u)`, which is its eigenvalue on `e^{ik·x}`. On the +ik mode `k` it multiplies by the conjugate.
  - On the nonzero modes its stationary limit is `C_s = σ²(I − PP*)^{−1}P*^s`, which multiplies the minus mode `k` by `σ²φ^s/(1 − u)`.

  **This is block 35's operator gloss (L104), verbatim, and it equals the display.**
- **(d)** L106's first line, "`θ̂_k(t+s) = φ^s θ̂_k(t) + (noise of levels t+1..t+s)`", is false with the minus transform wherever `φ^s ∉ ℝ`. The true regression coefficient is `conj(φ)^s`. L106's next step, "so the covariance is `φ^s` times the variance", is false with the executed pairing if that first line were true.
  - The two slips cancel: `E[θ̂(t)·conj(conj(φ)^s θ̂(t) + η)] = φ^s Var`. The conclusion stands.
- **(e)** The defect as confirmed ("differ by complex conjugation on every nonzero mode") is true in L86's labelling, where mode `k` is the one on which `P` acts by `φ`, i.e. the +ik mode.
  - There the gloss is `σ²conj(φ)^s/(1 − u)`, against the display's `σ²φ^s/(1 − u)`.
  - They differ exactly on the pairs with `φ(k)^s ∉ ℝ`, **not on every nonzero mode**.
  - The display and the gloss agree on 8 of 24 pairs `(k ≠ 0, s = 1..3)` for L = 3, 19 of 45 for L = 4 and 47 of 105 for L = 6.
- **(f)** Runner B1 declares `φ` positive (runner L138) and B2 uses cosine characters only. Both are invariant under `φ ↦ conj φ`, so neither can see (a)–(e).
  - The sine–cosine cross covariance can: `Cov(c·θ_t, s·θ_{t+s}) − Cov(s·θ_t, c·θ_{t+s}) = Im(φ^s)·W` with `W = cᵀΣ_t c + sᵀΣ_t s`. The conjugate reading flips its sign.

**Minimal correction of T1.**
- Keep the display and the gloss.
- Pin the minus transform and the executed pairing.
- Replace the multiplier `φ` by `conj(φ)` in b35 L86 and L106's first line.
- Fix the source the same way in b34 L4, L85, L104 and L108.

Block 34's conclusions use `u = |φ|²` only and are unaffected. The alternative correction keeps L86 with the +ik transform. It must then conjugate the display (`φ^s → conj(φ)^s`), because the gloss is fixed by the matrix identity `Σ_{t,t+s} = Σ_t(Pᵀ)^s`.

**T3′ (the corrected T3/D2).** Take `E(K) = Σ_a 2(1 − cos K_a)` (the comparator; block 19) and `z = (1/3)Σ_a e^{iK_a}`, `K ∈ ℝ³`.

- `D(K) := |1 − z|²` is `σ²` divided by the spectral density of the linearized formation field on `Z³`. It is block 13's symbol at `w = 1/3`.
- **(a)** `3D = E − 3(1 − u(K₁ − K₃, K₂ − K₃))`, and `u(K₁ − K₃, K₂ − K₃) = |z|²`.
- **(b)** `E` and `D` vanish only at `K ∈ 2πZ³`. Hence, for every frame of momentum space near 0 (any homeomorphism `Ψ` with `Ψ(0) = 0` of plane × line; in particular the lattice and level frames), neither `F∘Ψ` nor `1/(F∘Ψ)` is of the form `f(p)g(q)`, for `F ∈ {E, D}`.
  - D2's product test therefore returns "not a product" for **both** kernels in every frame and separates nothing.
  - The note's "The formation kernel is exactly of that form" is false in the representation where the test is applied.
- **(c)** In level coordinates `K = (k₁ + w, k₂ + w, w)`:
  - `E = 6 − 6Re(φ(k)e^{iw})`;
  - `D = 1 − 2Re(φ(k)e^{iw}) + u(k)`.

  Both depend on level frequency only through `Re(φe^{iw})`, so any phase (drift) along levels is common to both. In `(k, τ)`:
  - the comparator is `G(k, τ) = conj(φ)^τ(1 + y)^{−τ}/(6y)` for `τ ≥ 0`;
  - the formation kernel is `σ²conj(φ)^τ/(1 − u)`.

  Both are a plane factor times a propagator with the phase `conj(φ)^τ`. "It has no causal direction" (L116) fails as a contrast drawn from the drift.
- **(d)** Hessians at `K = 0`:
  - `Hess E = 2I` (rank 3);
  - `Hess 3D = (2/3)𝟙𝟙ᵀ` (rank 1, range spanned by `𝟙 = (1,1,1)`, the axis of the causal cone, `τ = X₁ + X₂ + X₃`).

  The rank is invariant under every C² change of frame fixing 0 and under multiplication by a positive C² normalization (`β`, `c(β)`, `σ²`). **This separation holds in every frame and representation:** elliptic (no distinguished direction) against parabolic (one non-null direction, the causal axis).
- **(e)** With `K = εa + ε²b𝟙` and `a·𝟙 = 0`:
  - `3D = ε⁴(3b² + |a|⁴/12) + O(ε⁵)`;
  - `E = ε²|a|² + O(ε³)`.

  So `D` has leading part `(K·𝟙)²/9 + |K_⊥|⁴/36`. This is block 13's T3(ii) ("`K²/9`" along the level direction, "`|k|⁴/36`" across), and it is the correct statement of the separation.

**Minimal correction of T3/D2.** Replace the product-structure sentences by (a), (b) and (d), with (e) as block 13's form. Keep T3's decay bound and the drift's series, which are unaffected.

## 2. Steps

**S1 (PROVED; CHECKED T1a).** The characters are eigenvectors of `P` and `Pᵀ`.
- `(Pe_k)(x) = (e^{ik·x} + e^{ik·(x−e₁)} + e^{ik·(x−e₂)})/3 = e_k(x)(1 + e^{−ik₁} + e^{−ik₂})/3 = conj(φ)e_k(x)`.
- `Pᵀ` averages over `x, x + e₁, x + e₂`, so `Pᵀe_k = φe_k`.
- Checked exactly in Q(ζ₁₂) (`ζ₁₂⁴ = ζ₁₂² − 1`) for every mode of L = 3, 4, 6.

**S2 (PROVED; CHECKED T1a).** The multiplier under each transform.
- Write `⟨a, b⟩ = Σ conj(a)b`, so `θ̂_k = L^{−1}⟨e_k, θ⟩`. Then `(Pθ)^_k = L^{−1}⟨Pᵀe_k, θ⟩ = conj(φ)θ̂_k`.
- For the +ik transform, `θ̂⁺_k = L^{−1}⟨e_{−k}, θ⟩`. It gives the multiplier `conj(φ(−k)) = φ(k)`.
- Real modes: `Im φ = (sin k₁ + sin k₂)/3 = (2/3)sin((k₁+k₂)/2)cos((k₁−k₂)/2)`. So `φ ∈ ℝ` iff `k₁ + k₂ ∈ 2πZ` or `k₁ − k₂ ∈ π + 2πZ`.
- Checked on a generic rational field (nonzero on every mode):
  - `(Pθ)^_k = conj(φ)θ̂_k` on all modes;
  - the stated `φθ̂_k` fails on 6/9, 10/16 and 24/36 modes, exactly the modes with non-real `φ`;
  - the characterization of the real modes matches mode by mode.
- b34 T1.1's proof computes "`e^{−ik·e}`" per shift, which gives `conj(φ)`, and then appeals to "the conjugate convention" without naming one. That step is where the multiplier label goes wrong.

**S3 (PROVED; CHECKED T1b).** The mode covariance under each transform.
- Minus transform: for a real matrix `M = [E θ_{x,t}θ_{y,t+s}]`, `E[θ̂_k(t)·conj θ̂_k(t+s)] = L^{−2}Σ_{x,y} e^{−ik·x}e^{ik·y}M_{xy} = L^{−2}e_kᴴMe_k`.
- +ik transform: the same pairing gives `L^{−2}e_{−k}ᴴMe_{−k}`.
- With `M = Σ_{t,t+s} = Σ_t(Pᵀ)^s` (S4) and S1:
  - `e_kᴴΣ_{t,t+s}e_k = φ^s W`, where `W = e_kᴴΣ_t e_k`;
  - `e_{−k}ᴴΣ_{t,t+s}e_{−k} = conj(φ)^s W`, because `W(−k) = W(k)` is real (`Σ_t` is symmetric).
- `Σ_t = σ²Σ_{j<t}P^j(Pᵀ)^j`. By S1, `P^j(Pᵀ)^je_k = u^je_k`, so `W = L²σ²(1 − u^t)/(1 − u)`, and `L²σ²t` at `k = 0`.
- Checked on the runner's own recursion `Σ_{t+1} = PΣ_tPᵀ + I` (runner L103–114), in exact Fractions, for `t ≤ 5, 4, 3` on L = 3, 4, 6 and `s ≤ 3`: all three identities, and the zero mode's `t/L²`.

**S4 (PROVED; CHECKED T1b, T1c).** The operator gloss.
- `Σ_{t,t+s} = E[θ_t(P^sθ_t + noise)ᵀ] = Σ_t(Pᵀ)^s`, because the later noise is independent of `θ_t`. This is L106's matrix form, and it is correct.
- For a circulant `A` with `Ae_k = λ(k)e_k`, the minus multiplier is `λ(k)`: `(Aθ)^_k = L^{−1}⟨Aᵀe_k, θ⟩`, and `Aᵀe_k = conj(λ(k))e_k` for a real circulant. The +ik multiplier is `λ(−k) = conj(λ(k))`.
- For `u < 1`, `I − PPᵀ` acts on `e_k` by `1 − u > 0`. So `Σ_{j≥0}(PPᵀ)^j` converges on the nonzero modes, and `C_s = σ²(I − PP*)^{−1}P*^s` multiplies the minus mode `k` by `σ²φ^s/(1 − u)`.
- `u < 1` for `k ≠ 0`: `|1 + e^{ik₁} + e^{ik₂}| = 3` iff all three unit vectors coincide.
- Checked on a generic rational field for every mode and `s ≤ 3`:
  - `(Σ_{t,t+s}θ)^_k (1 − u) = φ^s(1 − u^t)θ̂_k` for the minus transform;
  - the conjugate identity for the +ik transform;
  - `t·θ̂_0` at `k = 0`.

**S5 (PROVED; CHECKED T1d).** L106's first line.
- The regression coefficient of `θ̂_k(t+s)` on `θ̂_k(t)` (minus transform) is `E[θ̂_k(t+s)·conj θ̂_k(t)]/Var = e_kᴴΣ_{t,t+s}ᵀe_k/W`.
- `Σ_{t,t+s}ᵀ = P^sΣ_t` acts on `e_k` by `conj(φ)^s`, so the coefficient is `conj(φ)^s`.
- Indeed `θ̂_k(t+s) = conj(φ)^sθ̂_k(t) + Σ_{j<s}conj(φ)^jξ̂_k(t+s−1−j)`, and the sum is independent of `θ̂_k(t)`.
- Checked from the explicitly transposed matrices: the coefficient is `conj(φ)^s` on every pair, and equals the stated `φ^s` exactly where `φ^s ∈ ℝ`.

**S6 (PROVED; CHECKED T1f).** The disagreement set. In L86's labelling (the +ik mode), S3 gives display `φ^s` against gloss `conj(φ)^s`, with `W ≠ 0`. They agree iff `φ^s = conj(φ^s)`, i.e. iff `φ(k)^s ∈ ℝ`.
- This includes non-real `φ` with `φ^s` real. At L = 3, `k = 2π(1,1)/3`, `φ = i/√3` and `φ² = −1/3`.
- Checked counts: 8/24 (L = 3), 19/45 (L = 4), 47/105 (L = 6).

**S7 (PROVED; CHECKED T1e).** The runner's checks are blind to the conjugation; the cross covariance is not.
- For real `S` and `e_k = c + is`: `e_kᴴSe_k = (cᵀSc + sᵀSs) + i(cᵀSs − sᵀSc)`.
- With `S = Σ_{t,t+s}` and S3, `e_kᴴSe_k = φ^sW`.
- If `2k ∉ 2πZ²`, then `e_kᵀSe_k = 0` for a circulant `S`, which gives `cᵀSc = sᵀSs` and `cᵀΣc = W/2`. Hence B2's statistic `cᵀSc/cᵀΣ_tc = Re φ^s = Re conj(φ)^s`: blind.
- The cross term `cᵀSs − sᵀSc = Im(φ^s)W` changes sign under `φ ↦ conj φ`.
- B1 with a positive symbol `φ` is blind for the same reason.
- Checked on L = 4, where the characters are rational: exactly on every pair, and nonzero on all 26 pairs with `φ^s ∉ ℝ`.
- Orientation: `Σ_r c(r)e^{ik·r} ∝ φ^s ≈ e^{is(k₁+k₂)/3}`, with `c(r) = Cov(θ_{x,t}, θ_{x+r,t+s})`. So the correlation with records `s` levels later is centred at `+(s/3, s/3)`, away from the predecessors at `−e₁, −e₂`.

**S8 (PROVED; CHECKED T3a, T3b).** The identity and its level form.
- `u(K₁ − K₃, K₂ − K₃) = |e^{−iK₃}z|² = |z|²`, and `E = 6 − 6Re z`. Then `3D = 3 − 6Re z + 3|z|² = E − 3(1 − |z|²)`.
- In level coordinates, `z = φ(k)e^{iw}`.
- Lagrange: `9|z|² = 3 + 2Σ_{a<b}cos(K_a − K_b)`.
- Checked as identities between Laurent polynomials in `X_a = e^{iK_a}` (sympy, exact), and in `Y₁, Y₂, W` for the level form.

**S9 (PROVED).** No product in any frame.
- `E = 0` iff every `cos K_a = 1`.
- `D = |1 − z|² = 0` iff `z = 1`. By S8, `|z| ≤ 1`, with equality iff all `K_a − K_b ∈ 2πZ`, and then `z = e^{iK₁}`. So `D = 0` iff `K ∈ 2πZ³`.
- **Lemma.** Let `F ≥ 0` be continuous near 0, with `F(0) = 0` and `F > 0` elsewhere near 0. Let `Ψ: (p, q) ↦ K` be a homeomorphism of neighbourhoods of 0 in `ℝ² × ℝ`. Then `F∘Ψ ≠ f(p)g(q)`, and `1/(F∘Ψ) ≠ f(p)g(q)` on the punctured neighbourhood.
  - Proof for `F∘Ψ`: `f(0)g(0) = 0`. If `g(0) = 0`, then `F∘Ψ(p, 0) = 0` for all small `p`. If `f(0) = 0`, then `F∘Ψ(0, q) = 0` for all small `q`. Either contradicts positivity off 0.
  - Proof for `1/(F∘Ψ)`: suppose `1/(F∘Ψ) = f(p)g(q)`. Then `f, g ≠ 0` off 0, and `F∘Ψ = f'(p)g'(q)` with `f' = 1/f` and `g' = 1/g` for `p, q ≠ 0`.
    - Fix `q ≠ 0` and let `p → 0`. Continuity gives `f'(p) → F∘Ψ(0, q)/g'(q) =: c`, which is independent of `q`, and `0 < c < ∞`.
    - Symmetrically, `g'(q) → d ∈ (0, ∞)`.
    - Then `F∘Ψ(p, q) → cd > 0` as `(p, q) → 0` with `p, q ≠ 0`, contradicting `F(0) = 0`. ∎

**S10 (PROVED; CHECKED T3c).** An instance of S9 in the runner's own statistic. The statistic `f·f_ab − f_af_b` (that is, `f²∂²log f`) is nonzero for `E` and for `D`:
- in the lattice frame `(K₁, K₃)` at `(π/2, π/3, π/6)`;
- in the level frame `(k₁, w)` at `(π/3, π/6, π/2)`.

It is computed exactly with `∂_a = iX_a∂_{X_a}` and evaluated in Q(ζ₁₂). This is runner D2's test (L245–247) applied to both kernels. It calls both non-products.

**S11 (PROVED; CHECKED T3d).** The Hessian separation.
- The ε² coefficients of `E(εv)` and `3D(εv)` are `|v|²` and `(v·𝟙)²/3`. So the Hessians are `2I` (rank 3) and `(2/3)𝟙𝟙ᵀ` (rank 1).
- Invariance: `F(0) = 0` and `∇F(0) = 0`, since both functions are minimal there. Hence `Hess(F∘Ψ)(0) = DΨ(0)ᵀ Hess F(0) DΨ(0)` for any C² `Ψ` with `Ψ(0) = 0` and `DΨ(0)` invertible, and `Hess(hF)(0) = h(0)Hess F(0)` for C² `h` with `h(0) > 0`. Both preserve rank.

**S12 (PROVED; CHECKED T3e).** The parabolic leading part.
- Series in `ε` with `K = εa + ε²b𝟙` and `a₃ = −a₁ − a₂`: the coefficients of `3D` at `ε⁰..ε³` vanish, and the `ε⁴` coefficient is `3b² + |a|⁴/12`.
- `E`'s `ε²` coefficient is `|a|²`.
- For `D = 3D/3`: along `𝟙` this is block 13's `K²/9` (with `K = Σ_a K_a = 3ε²b`), and across it is block 13's `|k|⁴/36` (b13 L225–226).

**S13 (PROVED; CHECKED T3f).** The (k, τ) forms.
- Let `G(k, τ) := (2π)^{−1}∫e^{iwτ}/E(k, w) dw`, with `E(k, w) = 6 − 3φe^{iw} − 3conj(φ)e^{−iw} ≥ 6(1 − |φ|) > 0`. It solves `6G(τ) − 3φG(τ+1) − 3conj(φ)G(τ−1) = δ_{τ0}` (multiply by `E` and integrate).
- The candidate `G = z_*^τ/(6y)` for `τ ≥ 0` and `conj(z_*)^{|τ|}/(6y)` for `τ ≤ 0`, with `z_* = conj(φ)/(1 + y)`, solves the same recurrence:
  - for `τ ≠ 0`, `φz_*² − 2z_* + conj(φ) = 0` by `y² = 1 − u`;
  - at `τ = 0`, `6A(1 − u/(1 + y)) = 6Ay = 1`.
- Uniqueness: the difference of two bounded solutions solves the homogeneous recurrence, whose solutions are `αz_*^τ + β((1 + y)/φ)^τ`, with `|z_*|² = (1 − y)/(1 + y) < 1`. Boundedness at `τ → +∞` gives `β = 0`, and at `τ → −∞` gives `α = 0`. If `φ = 0`, then `G = δ/6`.
- The formation side is `Σ_re^{−ik·r}Cov(θ_{x,t}, θ_{x+r,t+s}) = conj(φ)^sσ²(1 − u^t)/(1 − u)` (S3, the +ik pairing).
- Same phase. Rates `−log|φ| = −½log(1 − y²) = y²/2 + O(y⁴)` against `−log|z_*| = artanh y = y + O(y³)`, with `y² = kᵀMk + O(|k|⁴)`: of order `|k|²` against `|k|`.
- Checked exactly at L = 4, `k = 2π(1,0)/4` and `2π(1,1)/4`, where `u = 5/9` and `y = 2/3` are rational: the recurrence for `τ = −4..4`, and `|z_*|² = 1/5`.

**ASSUMED.** Only the conventions of §1, quoted from the sources. The uniqueness in S13 and the lemma in S9 are proved above.

**Negative control (run separately, not in the log).** Replacing `φ` by `conj(φ)` in `check.py`, which is the L86/L106 reading, makes T1a–T1f all fail.

## 3. (b) Every use, with a verdict

Verdicts are *unaffected*, *holds on the corrected domain/reading* (T1′/T3′), or *needs its own repair*.

### Block 35 note (`7c844adf`)

| Lines | Statement | Verdict |
|---|---|---|
| L4 (claim_scope), L24–27, L98, L104, L177 (first clause) | covariance `σ²φ(k)^s/(1 − |φ|²)`; `C_s = σ²(I − PP*)^{−1}P*^s` | holds on the corrected reading (T1′(b)(c)); the conventions must be stated |
| L86 | "modes `θ̂_k`, multiplier `φ(k)`" (from block 34) | needs its own repair: `P` acts by `conj(φ)`, and `P*` by `φ` (S2) |
| L87 | `C_s(k) := Cov(θ̂_k(t), θ̂_k(t+s))`; "as an operator `C_s = Σ_x Cov(θ_{x,t}, θ_{x',t+s})`" | the first holds with the executed pairing. The second is misprinted (a sum over `x` leaves a function of `x'`) and needs its own repair: `[Cov(θ_{x,t}, θ_{x',t+s})]_{x,x'}` |
| L88, L122–128, L37–43 | executed phases "reproduce `φ(k)^s` in phase" | unaffected: numpy's forward DFT with `past·conj(cur)` is T1′(b)'s reading, and the control's phases (e.g. `+2.62/+2.62` at `k = 2π(4,1)/L`, `s = 64`) match |
| L106, first line and "so the covariance is `φ^s` times the variance" | the proof | needs its own repair (S5); the conclusion holds |
| L106, execution "`Re φ(k)^s` for every cosine character" and L4's "against Re phi(k)^s for every cosine character" | B2 | true but blind (S7): add the sine–cosine term |
| L108 | "heat kernel of the level walk with multiplier `φ`" | holds: `P*` acts by `φ` on `e^{ik·x}` |
| L112 (T2) | small-k form, symmetry groups | unaffected (uses `u` and `E` only) |
| L116, bound | `|C_s|/C_0 = |φ|^s ≤ e^{−2|k|²s/(9π²)}` | unaffected |
| L116 (D1), L4, L29 | `φ = 1 + i(k₁+k₂)/3 + O(k²)`, drift "along the axis of the causal cone" | the series holds. The orientation holds for the backward kernel `P^s`; the forward correlation is centred at `+(s/3, s/3)` (S7). As a contrast with the comparator it needs its own repair: the comparator has the same phase (T3′(c)) |
| L116 (D2); L4 "not of the product form … in any direction (proved)" | "`1/E(k)` is not of the form `f(k₁,k₂)g(k₃)` … so it cannot be read as a plane Green function times a propagator; it has no causal direction. The formation kernel is exactly of that form." | first clause true (S9). The inference, the causal-direction contrast and the last sentence need their own repair (S9, S10, S13); the correct separation is S11–S12 |
| L32–35 | comparator "with no distinguished direction and no product structure; it is a different object" | "no distinguished direction" holds (`Hess E = 2I`, S11). "No product structure" needs its own repair: true in full momentum, but not a separation, and false in `(k, τ)`. "A different object" holds on T3′ |
| L45–54 | plain words: diffusion across levels, no 3D potential | holds on T3′ (parabolic against elliptic, S11–S13) |
| L57, L92 (iii), L100, L196 | "the non-product form of the comparator (T3)" / "the proof that … has no product structure in any direction" / T3 row / family D | needs its own repair (replace with S11–S12) |
| L135 (N1.1) | "the tiny tori check the chain exactly (T1)" | needs its own repair: the cosine check does not test the phase (S7) |
| L137 (N1.3) | a product of `1/E` in a rotated frame "excluded … no frame gives it"; "the formation kernel's product structure holds in the level-time frame by construction" | the conclusion for `1/E` holds with S9's proof (the note's argument covers the lattice frame only). The formation sentence needs its own repair (S9, S10) |
| L160 (N5) | "the non-product form of `1/E`" | needs its own repair |
| L166 (N7), L128 (iii) | "the forms differ at the linear level"; "differ in their form, not in their normalization" | holds on T3′ (Hessian rank survives positive normalizations, S11) |
| L169 (N8) | block 13's heat kernel returns | unaffected; block 13's T3(ii) also supplies the separation (S12) |
| L172 | falsifier "cross-level recursion and `Re φ^s` differ" | unaffected but blind; add `Im φ^s` |
| L174 | falsifier "`log(1/E)` with vanishing mixed derivative" | needs its own repair (it cannot fire for a reason that separates) |
| L177 | "not a product of a plane factor and a propagator" | needs its own repair (S13) |

### Block 35 runner, control, refuting spec and pack files (`7c844adf`)

- **Runner.** See §4.
- **Control L27/L37.** Unaffected (the T1′(b) reading).
- **Refuting spec L28–33.** Unaffected. It uses complex characters `e^{+ik·x}/L` with `eᴴΣ(P^s)ᵀe` against `φ^s`, and reports `2.19e−15`. That is T1′(c)'s eigenvalue reading, and it did test the phase.
- **`RESULTS_block35.md`.**
  - L6: holds on the corrected reading; the cosine check is blind.
  - L8: the bound and the series are unaffected. "`1/E` is not a product of a plane factor …" needs its own repair.
- **`CLAIM_STATUS_CERTIFICATE_block35.md` L6** ("the comparator's non-product form") needs its own repair.
- **`NO_GO_LEDGER.md` L11, `HANDOFF.md` L30, `STATE.yaml` L114 (comment), `GOAL_block35.md` L8.** "No product structure in any direction" needs its own repair. "Different objects" holds on T3′.
- **`CHECKER_block35_findings.md`.**
  - L7: float recursion against `φ(k)^s`. Unaffected.
  - L10: "the comparator's non-product form" by finite differences. True, but not a separation; needs its own repair as a claim.

### Other notes of the campaign

I fetched every block 12–35 branch and the #8179 decision record. Blocks 12–24 are PRs #8146–#8158, and blocks 25–35 are #8168 and #8170–#8180; PRs #8159–#8167 and #8169 are other lanes. I grepped the 28 docs notes at their heads for:
- phase-bearing powers `φ^s` / `conj(φ)`;
- `P*`, `Pᵀ` and "adjoint";
- "multiplier";
- Fourier kernels `e^{±ik…}`;
- "characteristic function";
- "heat kernel";
- "product form/structure";
- "mixed derivative";
- "drift";
- `θ̂` / `ŝ`;
- `Cov(`.

| Note | Where | Verdict |
|---|---|---|
| Block 34 (#8178, `e6ffae5b`) | L4 claim_scope "multiplier phi(k)", L85, L104 (T1.1 and its proof), L108 (T1.3 recursion `θ̂_k(t+1) = φ(k)θ̂_k(t) + ξ̂_k(t)`); runner docstring L5 | needs its own repair: `conj(φ)` with its transform, or the +ik transform (S2). Everything else uses `u` only and is unaffected: T1.2, the variances, the memory time `3βL²/A(3β)`, `V_L` and T3. Its runner's B1/B2 test `|φ|²` only (runner L199–219) |
| Block 13 (#8147, `9c364d1d`) | L191–196 (`|φ|²` as the difference walk's characteristic function); L218–255 (T3: symbol `|1 − wΣe^{−ik_j}|²`, parabolic expansion) | unaffected. T3(ii) is the separation that block 35's D2 needed (S12) |
| Block 26 (#8170, `f9e11770`) | L86, L127: `φ(θ) = (1 + e^{−iθ₁} + e^{−iθ₂})/3`, the backward level walk's characteristic function, used through `u` and `p_k(y) = (2π)^{−2}∫φ^k e^{−iθ·y}` | unaffected (consistent convention) |
| Block 19 (#8153), block 29 (#8173) | the comparator's channel `⟨|ŝ(k)|²⟩ ≤ 1/(βE(k))` (b19 L185), `G_L(r)` (b29 L76), real even symbols | unaffected |
| Block 22 (#8156), block 24 (#8158) | a real `φ = (1/3)Σcos k_i`; the overlap weight `φ(s, s')` | unaffected (different objects) |
| Block 28 (#8172) | L56, L126: "the directed heat kernel of block 13", forward cone | unaffected |
| Decision record (#8179) | `DECISION_RECORD.md` L13 (where the Green-function kernel was located) | unaffected |
| Blocks 12 (5 notes on #8146), 14–18, 20, 21, 23, 25, 27, 30–33 | no hit for any of the patterns above in the sense used here. Every "product form" hit in blocks 12, 24, 26, 27, 28 and 29 is the rule's or the law's product form (block 24's is a factorization over components), not a kernel | no use |

Not searched: consumers outside PRs #8146–#8180, for example gravity-lane notes named at b35 L73.

## 4. (c) The lines that must change

### Note (`7c844adf`)

- **L86.** "modes `θ̂_k`, multiplier `φ(k) = …`" → "modes `θ̂_k = L^{−1}Σ_x e^{−ik·x}θ_x` (block 34), on which `P` acts by `conj(φ(k))` and `P*` by `φ(k)`, `φ(k) = …`".
- **L87.**
  - Add "with `Cov(X, Y) = E[(X − EX)·conj(Y − EY)]`".
  - "`C_s = Σ_x Cov(θ_{x,t}, θ_{x',t+s})`" → "`C_s = [Cov(θ_{x,t}, θ_{x',t+s})]_{x,x'}`, whose eigenvalue on `e^{ik·x}` is `C_s(k)`".
- **L104, L24–27 and L4.** State the transform and pairing of L86–87 once. Display and gloss unchanged.
- **L106.**
  - "`θ̂_k(t+s) = φ^s θ̂_k(t) + (noise…)` … so the covariance is `φ^s` times the variance" → "`θ̂_k(t+s) = conj(φ)^s θ̂_k(t) + (noise…)` … so `E[θ̂_k(t)·conj θ̂_k(t+s)] = φ^s Var θ̂_k(t)`".
  - After "`Cov/Var = Re φ(k)^s`" add "and `Cov(c·θ_t, s·θ_{t+s}) − Cov(s·θ_t, c·θ_{t+s}) = Im φ(k)^s·W` with the sine character".
- **L116, D1.** "drifts by one third of a step along each predecessor direction per level" → "the correlation with records `s` levels later is centred at `+(s/3, s/3)`, away from the predecessors, on the `(1,1,1)` axis; in level coordinates the comparator carries the same phase".
- **L116, D2.** Replace the three sentences "The comparator's `1/E(k)` is not of the form … The formation kernel is exactly of that form." by "With `z = (1/3)Σ_a e^{iK_a}`, the formation law's inverse kernel is `|1 − z|² = [E − 3(1 − u)]/3`. Neither kernel is a product in any frame (each inverse vanishes only at `K = 0`), and in `(k, τ)` both are a plane factor times a propagator with phase `conj(φ)^τ`. They are separated by the Hessian of the inverse kernel at `K = 0`: `2I` for `E` (elliptic, no distinguished direction) against `(2/9)𝟙𝟙ᵀ` for `|1 − z|²` (parabolic, its one non-null direction the causal-cone axis), with leading part `(K·𝟙)²/9 + |K_⊥|⁴/36` (block 13, T3(ii)) (D2)."
- **L32–35, L57, L92 (iii), L100, L137, L160, L177, L196.** Replace "no product structure" / "the non-product form" / "not a product of a plane factor and a propagator" / "the formation kernel's product structure … by construction" by the Hessian separation (elliptic, rank 3, against parabolic, rank 1 along `(1,1,1)`).
- **L135.** "the tiny tori check the chain exactly" → "… check the chain exactly, the phase through the sine–cosine term".
- **L172.** "and `Re φ^s` differ" → "and `Re φ^s` or `Im φ^s` differ".
- **L174.** "or `log(1/E)` with vanishing mixed derivative (D1–D2)" → "a Hessian of `E` other than `2I` or of `3|1 − z|²` other than `(2/3)𝟙𝟙ᵀ`, or the identity `3|1 − z|² = E − 3(1 − u)` failing (D1–D2)".

### Runner (`7c844adf`)

- **L5–8.** Docstring: add the transform and the pairing.
- **L13.** "`phi(k) = 1 - i(k1 + k2)/3 + O(k^2)`" → "`1 + i(k1 + k2)/3`". The minus sign is `conj(φ)`'s series; D1 at L236 checks `+`. Also drop "no distinguished direction" as a contrast unless it is stated through the Hessian.
- **L138–148 (B1).** `ph` is declared `positive=True`. Use a complex `φ` with `conj(φ)` as its own symbol, or check S2–S5 on the tori (`check.py` T1a–T1d).
- **L161–177 (B2).** Add the sine–cosine cross term `Im φ^s` or complex characters (`check.py` T1e; refuting spec L28–33 already does this), and update the message at L177.
- **L232.** Comment "`1 - i`" → "`1 + i`".
- **L237.** D1 message: state the orientation (`+(s/3, s/3)`, forward).
- **L238–248 (D2).** Replace the mixed-derivative test and its message with the identity, the two Hessians and the parabolic leading part (`check.py` T3a, T3d, T3e).
- **L253 (`FENCES[0]`).** Must equal the new note L177.
- **L299–300 (`N5_LINES`).** Add the sine term; replace "the non-product form of 1/E by a mixed derivative" by the Hessian separation.
- **L43–51 (`MUTATION_GATE`).** Add a B mutation that conjugates `φ`: today's B1/B2 pass it, which is the defect's signature. Add a D mutation on the Hessian.
- **Runner cache.** `logs/runner-cache/admissibility_rule_gravity_node_kernel_…_2026_09_18.txt` regenerates with the runner.

### Block 34 (source of the multiplier label; `e6ffae5b`)

- **L4, L85, L104, L108.** "multiplier `φ(k)`" / "`(Pθ)^_k = φ(k)θ̂_k`" / "`θ̂_k(t+1) = φ(k)θ̂_k(t) + ξ̂_k(t)`" → `conj(φ(k))` with its transform `L^{−1}Σe^{−ik·x}`.
- **L104's proof.** "the conjugate convention gives the stated `φ`" → "each shift multiplies `θ̂_k` by `e^{−ik·e}`, so `P` multiplies it by `conj(φ(k))`".
- **Runner docstring L5.** Change the same way.

## 5. What would finish it

(a)–(c) are complete as stated. The edits in §4 are the note owners' to make; this packet touches no PR.

Two things are left open:
- Consumers outside PRs #8146–#8180 that use D2's product contrast, such as the gravity lane's notes. I did not search them.
- Whether block 35 should restate its kernel in the level-frame `(k, ω)` form `σ²/|1 − φe^{iω}|²`. That is an editorial choice, not a repair.
