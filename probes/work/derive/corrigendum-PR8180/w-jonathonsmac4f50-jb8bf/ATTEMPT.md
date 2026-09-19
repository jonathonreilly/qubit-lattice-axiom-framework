# Corrigendum packet for PR #8180 (block 35): derivation attempt 2 of 2

Worker `w-jonathonsmac4f50-jb8bf` (claude-opus-5), unit `J-derive-corrigendum-PR8180-a2`. Sources: block 35's note, runner, control and pack files at the
PR #8180 head `7c844adf` (branch `physics-loop/admissibility-induced-law-block35-gravity-kernel-under-the-formation-reading-heat-kernel-times-plane-green-function-20260918`);
block 34's note and runner at the PR #8178 head; the notes of PRs #8146–#8178 and the #8179 decision record at their heads. Line numbers are those files'
lines at those heads. `check.py` (this directory) verifies every finite claim exactly; one numerical cross-check is labelled.

**Provenance and independence.** Neither half of the defect is independent of my model family:
- T3/D2 was found by my own falsifier probe (`logs/probes/J:falsifier:PR8180/opus-max-1__984cc2bb__…`: FFT quadrature on `L = 96` plus exact grid
  identities). Another family confirmed it (`J:confirm:J-falsifier-PR8180`, `w-macbookpro90c72-ja32c`).
- T1 was found by a grok worker (`J:attack-g:PR8180`, `w-macbookpro90c72-jb5ae`). I confirmed it as issue #8412 (`J:confirm:J-attack-g-PR8180`,
  `w-jonathonsmac4f50-jaee9`).

What this attempt adds:
- exact proofs where the probe used quadrature (S7–S9);
- a narrower diagnosis of T1 (S1–S5): in the note's own declared conventions the display and the operator gloss agree. What is wrong is the multiplier
  label (note L86) and the proof's first line (L106), both inherited from block 34's T1.1;
- a convention-free form of T1 (S6);
- the phase identity between the two kernels (S8);
- closed forms of the two decay rates (S9).

When I wrote this, no first-round attempt for this problem was on `origin/ai/probes`.

## 1. The statement attempted

**Conventions.**
- Sites `x = (i, j)` lie on the `L × L` level plane, with `(Pθ)_x = (θ_x + θ_{x−e₁} + θ_{x−e₂})/3`. This matches note L85–86, the runner's `shift_matrix` (L92–100) and the control's `np.roll` (control L17).
- The field obeys `θ_{t+1} = Pθ_t + ξ_t`, with `ξ` i.i.d. of variance `σ²` per site.
- `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`, `u = |φ|²`, `y = √(1 − u)`, and `e_k(x) = e^{ik·x}`.
- Modes are `θ̂_k := L^{−1} Σ_x e^{−ik·x} θ_x`. This is block 34's definition (its L85), which block 35 cites for its modes at L86.
- The pairing is `Cov(X, Y) := E[(X − EX)·conj(Y − EY)]`. This is the pairing of block 35's executed observable (L88: `E[ŝ(k,t) ŝ(k,t+s)*]`) and of its control (L36–37: numpy's forward DFT and `E[f(t−s)·conj f(t)]`).
- `Σ_{t,t+s} := [Cov(θ_{x,t}, θ_{x',t+s})]_{x,x'}`.

**T1′ (corrected T1).** For every `k`, `t ≥ 1` and `s ≥ 0`:

- **(a)** `P e_k = conj(φ(k)) e_k` and `Pᵀ e_k = φ(k) e_k`. Hence `(Pθ)^_k = conj(φ(k)) θ̂_k` and `θ̂_k(t+s) = conj(φ(k))^s θ̂_k(t) + η`, where `η` is independent of `θ̂_k(t)`.
- **(b)** `Cov(θ̂_k(t), θ̂_k(t+s)) = φ(k)^s Var θ̂_k(t)`, with `Var θ̂_k(t) = σ²(1 − u^t)/(1 − u)` for `u < 1` and `σ²t` at `k = 0`. This is block 35's display (L104) verbatim.
- **(c)** `Σ_{t,t+s} = Σ_t (Pᵀ)^s` has eigenvalue `φ(k)^s Var θ̂_k(t)` on `e_k`. On the nonzero modes its stationary limit `C_s = σ²(I − PPᵀ)^{−1}(Pᵀ)^s` has eigenvalue `σ²φ(k)^s/(1 − u)` on `e_k`. This is block 35's operator gloss verbatim, with `C_s(k)` the eigenvalue on `e^{ik·x}`.
- **(d)** The forward space-time correlation `c_{t,s}(r) := Cov(θ_{x,t}, θ_{x+r,t+s})` has Fourier coefficient `Σ_r e^{−ik·r} c_{t,s}(r) = conj(φ(k))^s Var θ̂_k(t)`, the conjugate of the display.
- **(e)** Convention-free form. With the real characters `c = cos(k·x)`, `s = sin(k·x)` and `S = Σ_{t,t+s}`: `cᵀSc + sᵀSs = Re(φ^s)·W` and `cᵀSs − sᵀSc = Im(φ^s)·W`, where `W = cᵀΣ_t c + sᵀΣ_t s`.
- **(f)** The display does not depend on the reading exactly when `φ(k)^s ∈ ℝ`. The readings are the transform sign, the order of the pairing, and eigenvalue on `e^{ik·x}` versus coefficient of the forward correlation. The display is reading-independent on 8 of the 24 pairs `(k ≠ 0, s = 1..3)` on `L = 3` and on 19 of 45 on `L = 4`. Everywhere else the readings split into `φ^s` and `conj(φ)^s`.

The defect as confirmed ("differ by complex conjugation on every nonzero mode") therefore holds in the labelling of note L86 and L106, where mode `k` is the character on which `P` acts by `φ`. Even there it holds only on the pairs where `φ^s` is not real.

**Minimal correction.** Keep the display and the gloss, and pin the transform and the pairing: block 34's transform and the executed observable's `E[X Ȳ]`. Then replace the multiplier `φ` by `conj(φ)` in L86 and in L106's first line. The equivalent alternative keeps L86/L106 (the `+ik` transform) and then needs `(Pᵀ)^s → P^s` in the gloss, or `φ^s → conj(φ)^s` in the display. That is the form given in #8412.

**T3′ (corrected T3/D2).** Take the level planes `X₁ + X₂ + X₃ = τ` of `Z³` with in-plane coordinates `(X₁, X₂)` (note L85), and `K = (k₁ + w, k₂ + w, w)`.

- **(a)** `E(K) = 3|1 − φ(k)e^{iw}|² + 3(1 − u(k))`. The formation law `θ(X) = (1/3)Σ_a θ(X − e_a) + ξ(X)` has spectral density `S_F(K) = σ²/|1 − φ(k)e^{iw}|²`. Hence `E = 3σ²/S_F + 3(1 − u)` exactly.
- **(b)** The runner's D2 test ("its logarithm has a non-vanishing mixed derivative") returns "not a product" for `log E` and also for `log S_F`, in the lattice frame and in the level frame. The test does not separate the kernels.
- **(c)** Work in the `(k, τ)` representation, for every `k` with `u(k) < 1`.
  - The comparator is `Ĝ(k, τ) := (2π)^{−1} ∫_{−π}^{π} e^{iwτ}/E(k, w) dw`. It equals `z^τ/(6y)` for `τ ≥ 0` and `conj(z)^{|τ|}/(6y)` for `τ ≤ 0`, where `z = conj(φ)/(1 + y)`.
  - The formation kernel (T1′(d), stationary) is `Ĉ_τ(k) = σ² conj(φ)^τ/y²` for `τ ≥ 0`, with `Ĉ_{−τ} = conj(Ĉ_τ)`.
  - `Ĝ(k, τ) = [y/(6σ²(1 + y)^{|τ|})]·Ĉ_τ(k)`.
  - Both are a positive plane factor times the same phase `conj(φ)^τ`, times `e^{−|τ|ρ}`, with:
    - formation: `ρ_F = −½ log(1 − y²) = y²/2 + y⁴/4 + …`;
    - comparator: `ρ_C = artanh y = y + y³/3 + …`;
    - `y² = kᵀMk + O(|k|⁴)` and `M = (1/9)[[2, −1], [−1, 2]]`.

So what separates the kernels is the order of their rates (`|k|²` against `|k|`) and of their plane factors (`|k|^{−2}` against `|k|^{−1}`). It is not a product structure, and it is not the drift, because the phase is common to both.

## 2. Steps

**S1 (PROVED; CHECKED `T1a`).** `(P e_k)(x) = (e^{ik·x} + e^{ik·(x−e₁)} + e^{ik·(x−e₂)})/3 = conj(φ(k)) e_k(x)`. `Pᵀ` averages over the successors `x, x + e₁, x + e₂`, giving `Pᵀ e_k = φ(k) e_k`. Checked exactly in `Q(√3, i)` for every mode of `L = 3, 4`.

**S2 (PROVED; CHECKED `T1b`).** Write `⟨a, b⟩ = Σ conj(a)b`. Then `(Pθ)^_k = L^{−1}⟨e_k, Pθ⟩ = L^{−1}⟨Pᵀe_k, θ⟩ = conj(φ) θ̂_k`. Iterating, `θ̂_k(t+s) = conj(φ)^s θ̂_k(t) + Σ_{j<s} conj(φ)^j ξ̂_k(t+s−1−j)`, and the sum is independent of `θ̂_k(t)`. The `+ik` transform `L^{−1}Σ e^{ik·x}θ_x` has multiplier `φ`.

Consequence for block 34: its T1.1 states `(Pθ)^_k = φ(k) θ̂_k` with its own transform. That fails on every nonzero mode with `φ ∉ ℝ`: 6 of 8 modes on `L = 3` and 10 of 15 on `L = 4` (a generic rational field, exact). Its proof computes `e^{−ik·e}` per shift, which is `conj(φ)`, and then appeals to "the conjugate convention" without saying which one.

**S3 (PROVED; CHECKED `T1c`).**
- `Cov(θ̂_k(t), θ̂_k(t+s)) = E[θ̂_k(t)·conj(conj(φ)^s θ̂_k(t) + η)] = φ^s E|θ̂_k(t)|²`.
- `V(t+1) = |conj φ|² V(t) + σ² = uV(t) + σ²` (with `Var ξ̂_k = σ²` under the `L^{−1}` normalization), which sums geometrically.
- Checked on the runner's own exact recursion (`t ≤ 6` on `L = 3`, `t ≤ 4` on `L = 4`, `s ≤ 3`):
  - `L^{−2} e_kᴴΣ_t e_k = (1 − u^t)/(1 − u)`;
  - `e_kᴴΣ_{t,t+s} e_k = φ^s e_kᴴΣ_t e_k`, while the conjugate pairing `e_kᵀΣ_{t,t+s} conj(e_k) = conj(φ)^s e_kᴴΣ_t e_k`;
  - the zero mode `1ᵀΣ_{t,t+s} 1/L⁴ = t/L²`.
- The two pairings differ on 16 of 24 pairs on `L = 3` and 26 of 45 on `L = 4`, exactly the pairs with `φ^s ∉ ℝ`.

**S4 (PROVED; CHECKED `T1d`).**
- `Σ_{t,t+s} = E[θ_t (P^sθ_t + noise)ᵀ] = Σ_t (Pᵀ)^s`, as note L106 has it.
- `Σ_t = σ² Σ_{j<t} P^j (Pᵀ)^j`, and `P^j (Pᵀ)^j e_k = u^j e_k`. So `Σ_t e_k = σ²(1 − u^t)/(1 − u)·e_k` and `Σ_{t,t+s} e_k = φ^s σ²(1 − u^t)/(1 − u)·e_k`.
- For `u < 1` the limit gives `C_s e_k = σ²φ^s/(1 − u)·e_k`. Checked exactly: `(I − PPᵀ)(φ^s e_k) = (1 − u)(Pᵀ)^s e_k` for every nonzero mode and `s ≤ 3`.

**S5 (PROVED; CHECKED `T1e`).** By translation invariance, `c_{t,s}(r) = [Σ_{t,t+s}]_{x,x+r}`. Then `Σ_r e^{−ik·r} c(r) = (Σ_{t,t+s} e_{−k})(x)/e_{−k}(x) = φ(−k)^s Var θ̂_{−k}(t) = conj(φ(k))^s Var θ̂_k(t)`. Checked exactly at `x = 0`.

Orientation of the drift:
- `c(r) = Σ_y [Σ_t]_{0,y} [P^s]_{r,y}`, and `[P^s]_{r,y} > 0` only for `y = r − S` with `S` a sum of `s` steps in `{0, e₁, e₂}`.
- So the correlation with the records `s` levels later is centred near `r = +(s/3, s/3)`. That is away from the predecessor directions `−e₁, −e₂`, on the `(1,1,1)` axis of `Z³`.

**S6 (PROVED; CHECKED `T1f`).**
- For real `S`, `e_kᴴSe_k = (c − is)ᵀS(c + is) = (cᵀSc + sᵀSs) + i(cᵀSs − sᵀSc)`.
- `e_kᴴSe_k = φ^s e_kᴴΣ_t e_k = φ^s W`, and `W` is real because `Σ_t` is symmetric.
- A cosine character alone gives `cᵀSc/cᵀΣ_t c = Re(φ^s)` (runner B2), which equals `Re(conj(φ)^s)`. So B2 passes under either reading.
- The runner's B1 declares `φ` positive (runner L138), so it cannot see the conjugation either.

**S7 (PROVED; CHECKED `T3a`, `T3b`, `T3c`).**
- `K·X = k·(X₁, X₂) + w(X₁ + X₂ + X₃)`, and `(e^{iK₁} + e^{iK₂} + e^{iK₃})/3 = φ(k)e^{iw}`. So `E = 6 − 6Re(φe^{iw}) = 3|1 − φe^{iw}|² + 3(1 − u)`.
- The formation law gives `θ̂(K)(1 − (1/3)Σ_a e^{−iK_a}) = ξ̂(K)`, with `(1/3)Σ_a e^{−iK_a} = conj(φ)e^{−iw}`. So `S_F = σ²/|1 − φe^{iw}|²`.
- The mixed-derivative test, evaluated exactly at algebraic points, gives the following values of `f² ∂²log f/∂a∂b`:

| `f` | Frame | Point | Value | Minimal polynomial |
|---|---|---|---|---|
| `E` | lattice `(K₁, K₃)` | `(π/2, π/3, π/6)` | `−2` | `x + 2` |
| `1/S_F` | lattice `(K₁, K₃)` | `(π/2, π/3, π/6)` | `−7/81 − 2√3/81` | `6561x² + 1134x + 37` |
| `E` | level `(k₁, w)` | `(π/3, π/6, π/2)` | `−8√3 − 6` | `x² + 12x − 156` |
| `1/S_F` | level `(k₁, w)` | `(π/3, π/6, π/2)` | `−5√3/9 − 2/3` | `27x² + 36x − 13` |

  All four are nonzero. The test calls both kernels non-products in both frames.

**S8 (PROVED; CHECKED `T3d`, `T3e`; `T3g` is the numerical cross-check).**
- `E(k, w) = 6 − 3φe^{iw} − 3conj(φ)e^{−iw} ≥ 6(1 − |φ|) > 0` for `u < 1`. So `g(τ) := (2π)^{−1}∫ e^{iwτ}/E dw` is bounded.
- `g` satisfies `6g(τ) − 3φ g(τ+1) − 3conj(φ) g(τ−1) = δ_{τ0}`: multiply by `E` and integrate, since `e^{±iw}` shifts `τ` by `±1`.
- The stated `G` solves the same equation. Checked for `τ = −4..4`. For `τ ≠ 0` the equation reduces to `φz² − 2z + conj(φ) = 0` with `z = conj(φ)/(1 + y)`, using `y² = 1 − φ·conj(φ)`. At `τ = 0` it reduces to `6Ay = 1`.
- The homogeneous solutions are `αz^τ + βz₊^τ` with `z₊ = (1 + y)/φ`. Here `|z|² = (1 − y)/(1 + y) < 1 < |z₊|²`.
  - A bounded two-sided homogeneous solution has `β = 0`, from `τ → +∞`, and then `α = 0`, from `τ → −∞`.
  - If `φ = 0` the equation is `6g = δ`.
  - Hence `g = G`.
- With `Ĉ_τ = σ²conj(φ)^τ/y²` (S5, stationary), `Ĝ/Ĉ_τ = y/(6σ²(1 + y)^τ)` for `τ ≥ 0`, checked for `τ = 0..5`.
- For `τ < 0`, both kernels are the complex conjugates of their `|τ|` values: `c_{−τ}(r) = c_τ(−r)` for the real field, and `Ĝ(k, −τ) = conj(Ĝ(k, τ))`.
- Numerical cross-check: at `k = (0.7, −0.4)`, 30-digit quadrature agrees with `G` to `7e−32` for `τ = −2..3`. This fixes the sign convention: `|z| = 0.6257`, `|φ| = 0.8993`.

**S9 (PROVED; CHECKED `T3f`).**
- `|φ|² = 1 − y²` and `|z|² = (1 − y)/(1 + y)`.
- So `ρ_F = −½ log(1 − y²) = y²/2 + y⁴/4 + O(y⁶)` and `ρ_C = ½ log((1 + y)/(1 − y)) = artanh y = y + y³/3 + y⁵/5 + O(y⁷)`.
- The series in `ε` gives `1 − u(ε(a, b)) = ε²(2a² − 2ab + 2b²)/9 + O(ε⁴)`, which is `ε² kᵀMk`.

**ASSUMED.** Only the conventions stated in §1, taken from the note's own L85–L88, block 34's L85 and the control's L27/L36–37. S8 uses the elementary facts it re-proves: boundedness, and uniqueness of the bounded solution.

## 3. (b) Every use, with a verdict

Verdicts are "unaffected", "holds on the corrected reading" (T1′/T3′) or "needs its own repair".

### Block 35 note (PR #8180 @ `7c844adf`)

| Lines | Statement | Verdict |
|---|---|---|
| L24–25; L177; runner L253 | covariance of every nonzero mode `σ²φ^s/(1 − \|φ\|²)` | holds on the corrected reading (T1′(b)); state the transform and pairing |
| L25–28 | `C_s = σ²(I − PP*)^{−1}P*^s`; plane Green function × heat kernel | holds (T1′(c)); `C_s(k)` = eigenvalue on `e^{ik·x}` |
| L28–29 | diffusive, in-plane scales `√s` | unaffected (uses `\|φ\|` only) |
| L29; L116 (D1) | drifts along the axis of the causal cone; `φ = 1 + i(k₁ + k₂)/3 + O(k²)` | holds on the corrected reading with orientation: forward, `+(s/3, s/3)` per `s` levels (S5), away from the predecessors. L116's "along each predecessor direction" reads backward. The comparator carries the same phase (T3′(c)), so where the drift is used as a contrast it needs its own repair |
| L29–32 | three-fold symmetry of `kᵀMk`; zero mode random-walks | unaffected |
| L32–35 | comparator "with no distinguished direction and no product structure; it is a different object" | "isotropic / no distinguished direction" (cubic symmetry, T2) is unaffected. "No product structure" needs its own repair (T3′(b)(c)). "A different object" holds on T3′ (rates, plane factors, `E = 3σ²/S_F + 3(1 − u)`) |
| L37–43; L88; L122–128 | executed: cross-level correlations reproduce `φ^s` in modulus and phase | unaffected: the control uses the `−ik` DFT and `E[X Ȳ]`, the reading of T1′(b) |
| L45–54 | plain words: diffusion across levels; no three-dimensional potential | unaffected by the defect (diffusive `ρ_F` against elliptic `ρ_C`) |
| L57 | "the non-product form of the comparator (T3)" | needs its own repair |
| L86 | "modes `θ̂_k`, multiplier `φ(k)` … (block 34)" | needs its own repair: with block 34's transform `P` acts by `conj(φ)` and `P*` by `φ` (T1′(a)) |
| L87 | `C_s(k) := Cov(θ̂_k(t), θ̂_k(t+s))`; "as an operator `C_s = Σ_x Cov(θ_{x,t}, θ_{x',t+s})`" | holds with the pairing `E[X Ȳ]`. The operator definition is misprinted (a sum over `x` leaves a function of `x'`); it needs its own repair: `[Cov(θ_{x,t}, θ_{x',t+s})]_{x,x'}` |
| L92 (iii) | "the proof that the comparator's kernel has no product structure in any direction" | needs its own repair |
| L98 | table row T1 | holds on the corrected reading |
| L100 | table row T3 "`1/E` not a product … a mixed derivative" | needs its own repair |
| L104 | T1 statement | holds verbatim on the corrected reading (T1′(b)(c)); state the conventions |
| L106 | T1 proof: "`θ̂_k(t+s) = φ^s θ̂_k(t) + noise`"; B2 "`Re φ^s` for every cosine character" | needs its own repair. The first line is false with the declared transform on every `(k, s)` with `φ^s ∉ ℝ`, although the conclusion holds (S2–S3). The cosine test is true but blind (S6) |
| L108 | reading: heat kernel of the level walk with multiplier `φ` | holds (`P*` acts by `φ` on `e^{ik·x}`) |
| L116 (T3 bound) | `\|C_s(k)\|/C_0(k) = \|φ\|^s ≤ e^{−2\|k\|²s/(9π²)}` | unaffected |
| L116 (D2) | "`1/E(k)` is not of the form `f(k₁, k₂)g(k₃)` … so it cannot be read as a plane Green function times a propagator; it has no causal direction. The formation kernel is exactly of that form." | The first clause is true. The inference, the "no causal direction" contrast and the last sentence need their own repair. In `(k, τ)`, `1/E` is `1/(6y)·z^{\|τ\|}` with the formation kernel's phase, and `S_F` fails the same test (T3′(b)(c)) |
| L128 (iii) | "the two channels differ in their form, not in their normalization" | holds on T3′ |
| L137 (N1.3) | "the formation kernel's product structure holds in the level-time frame by construction" | needs its own repair: false in `(k, ω)`; in `(k, τ)` it holds only in the sense in which the comparator's also does |
| L160 (N5); runner L300 | "the non-product form of `1/E`" | needs its own repair |
| L166 (N7) | "the forms differ at the linear level" | holds on T3′ |
| L172 | falsifier "cross-level recursion and `Re φ^s` differ" | unaffected but blind; add `Im φ^s` |
| L174 | falsifier "`log(1/E)` with vanishing mixed derivative (D1–D2)" | needs its own repair (it cannot fire for a reason that separates the kernels) |
| L177 | boundary: "not a product of a plane factor and a propagator" | needs its own repair (false in `(k, τ)`). Runner L253 must change in step |
| L196 | "D … the comparator's non-product form" | needs its own repair |

### Block 35 pack files (PR #8180 branch)

| Location | Verdict |
|---|---|
| `RESULTS_block35.md` L6 (T1) | holds on the corrected reading; the "cosine character" check is blind; state the conventions |
| `RESULTS_block35.md` L8 (T3) | The bound is unaffected. The drift holds with orientation and is common to both kernels. "`1/E` is not a product … in any direction" needs its own repair |
| `CLAIM_STATUS_CERTIFICATE_block35.md` L6 ("the comparator's non-product form") | needs its own repair |
| `NO_GO_LEDGER.md` L11 ("… has no product structure in any direction; the two are different objects") | The conclusion holds on T3′; the reason needs its own repair |
| `HANDOFF.md` L30 ("the comparator's `1/E` has no such product structure in any direction") | needs its own repair. The display holds on the corrected reading |
| `STATE.yaml` L114 (comment) | as `HANDOFF.md` L30 |

### Other notes of the campaign (PRs #8146–#8178, #8179)

| Note | Verdict |
|---|---|
| Block 34 (#8178) T1.1 L104, the source; also T1.3 L108 (`θ̂_k(t+1) = φ(k)θ̂_k(t) + ξ̂_k(t)`) and claim_scope L4 ("multiplier phi(k)") | needs its own repair: `conj(φ)`, or the `+ik` transform (S2; 6/8 and 10/15 modes). Every conclusion of block 34 depends on `u = \|φ\|²` only and is unaffected: T1.2, the variances of T1.3, the memory time `3βL²/A(3β)`, the bracket of `V_L`, T3. Its runner's B1 (L199–206) and B2 test `\|φ\|²` only |
| Block 26 (#8170) L86, L127 (`φ(θ) = (1 + e^{−iθ₁} + e^{−iθ₂})/3`, the level walk's characteristic function, i.e. block 35's `conj(φ)`, used consistently in `p_k(y) = (2π)^{−2}∫φ(θ)^k e^{−iθ·y}dθ` and only through `u`) | unaffected |
| Block 13 (#8147) L192 (characteristic function `\|φ(k)\|²`) | unaffected |
| Block 22 (#8156) L26, L67–68 (a different, real `φ = (1/3)Σ cos k_i`) | unaffected |
| Block 29 (#8173) L75–94 (`⟨\|θ̂(k)\|²⟩ = 1/(βE(k))`, static, even symbol) | unaffected |
| Decision record (#8179) L13 (block 13's heat-kernel statement; no phase, no product form) | unaffected |

No other note of #8146–#8178 states a phase-bearing Fourier multiplier, `P*`, a product form of a kernel or a mixed derivative. I fetched the 25 docs notes from their branches and grepped them for `φ`, `e^{±i…}`, "characteristic function", "multiplier", "product form" and "mixed derivative". The other `φ` hits are the static overlap weight `φ(s, s')`, a different object. The other "product form" hits are #8146 L338 and #8158 L95/L188, where it means the product rule or a factorization over components, which is unrelated. PRs #8159–#8167 are other lanes (TOE campaigns), not blocks 12–35.

## 4. (c) The lines that must change

### Note

The note is `docs/ADMISSIBILITY_RULE_GRAVITY_NODE_KERNEL_UNDER_THE_FORMATION_READING_…_2026-09-18.md` at `7c844adf`.

- **L24–25:** after `σ² φ(k)^s/(1 − |φ(k)|²)` add "(modes `θ̂_k = L^{−1}Σ_x e^{−ik·x}θ_x`, `Cov(X, Y) = E[X Ȳ]`; equivalently the eigenvalue on `e^{ik·x}` of the operator below; the Fourier coefficient of the forward correlation `Cov(θ_{x,t}, θ_{x+r,t+s})` is its complex conjugate)".
- **L33–35:** replace "with no distinguished direction and no product structure; it is a different object" by "with the cubic symmetry; in the level coordinates `E = 3|1 − φe^{iω}|² + 3(1 − |φ|²)`, and its level propagator `conj(φ)/(1 + √(1 − |φ|²))` has the formation kernel's phase but decays at a rate of order `|k|`, against `|k|²`; it is a different object".
- **L57:** "the scaling and the non-product form of the comparator (T3)" → "the scaling, the drift, and the comparator's level propagator (T3)".
- **L86:** "modes `θ̂_k`, multiplier `φ(k) = …`" → "modes `θ̂_k = L^{−1}Σ_x e^{−ik·x}θ_x` (block 34), on which `P` acts by `conj(φ(k))` and `P*` by `φ(k)`, `φ(k) = …`".
- **L87:**
  - after `C_s(k) := Cov(θ̂_k(t), θ̂_k(t+s))` add "with `Cov(X, Y) = E[(X − EX) conj(Y − EY)]`";
  - "as an operator `C_s = Σ_x Cov(θ_{x,t}, θ_{x',t+s})`" → "as an operator `C_s = [Cov(θ_{x,t}, θ_{x',t+s})]_{x,x'}`, whose eigenvalue on `e^{ik·x}` is `C_s(k)`".
- **L92 (iii):** "and the proof that the comparator's kernel has no product structure in any direction" → "and the comparator's level propagator in the same coordinates (same phase; rate of order `|k|` against `|k|²`)".
- **L100:** "`1/E` not a product | … a mixed derivative" → "`E = 3|1 − φe^{iω}|² + 3(1 − u)`; the comparator's propagator `conj(φ)/(1 + √(1 − u))` | a three-term recurrence; series".
- **L104:** add the conventions of L86–87.
- **L106:**
  - "`θ̂_k(t+s) = φ^s θ̂_k(t) + (noise of levels t+1..t+s)`, … so the covariance is `φ^s` times the variance" → "`θ̂_k(t+s) = conj(φ)^s θ̂_k(t) + (noise of levels t+1..t+s)`, … so `Cov(θ̂_k(t), θ̂_k(t+s)) = E[θ̂_k(t) conj θ̂_k(t+s)] = φ^s Var θ̂_k(t)`";
  - after "`Cov/Var = Re φ(k)^s`" add "and, with the sine character `s`, `Cov(c·θ_t, s·θ_{t+s}) − Cov(s·θ_t, c·θ_{t+s}) = Im φ(k)^s · W`".
- **L116:**
  - D1: "drifts by one third of a step along each predecessor direction per level, i.e. along the axis of the causal cone" → "the correlation with the records `s` levels later is centred at `+(s/3, s/3)`, away from the predecessors, i.e. on the `(1,1,1)` axis of `Z³`; the comparator's level propagator carries the same phase";
  - D2: replace "The comparator's `1/E(k)` is not of the form … The formation kernel is exactly of that form." by "In the level coordinates `E = 3|1 − φe^{iω}|² + 3(1 − u)` and the formation law's spectral density is `σ²/|1 − φe^{iω}|²`; neither is a product in `(k, ω)`. In `(k, τ)` both are a positive plane factor times `conj(φ)^τ e^{−|τ|ρ}`, with `ρ = −½log(1 − y²) = y²/2 + …` for the formation kernel and `ρ = artanh y = y + …` for the comparator, `y = √(1 − u)` (D2)."
- **L137 (N1.3):** → "A separation by product form — not used: neither kernel is a product in `(k, ω)`, and both are propagator forms in `(k, τ)`; the separation is the order of the rates."
- **L160:** "the non-product form of `1/E`" → "the comparator's level propagator and its rate".
- **L172:** "`Re φ^s`" → "`Re φ^s` or `Im φ^s`".
- **L174:** "or `log(1/E)` with vanishing mixed derivative (D1–D2)" → "or a comparator propagator other than `conj(φ)/(1 + √(1 − u))` (D1–D2)".
- **L177:** "and not a product of a plane factor and a propagator" → "whose level propagator decays at a rate of order `|k|` rather than `|k|²`".
- **L196:** "D the scaling and the comparator's non-product form" → "D the scaling, the drift and the comparator's propagator".

### Runner

The runner is `scripts/admissibility_rule_gravity_node_kernel_…_2026_09_18.py` at `7c844adf`.

- **L5–8 (docstring T1):** add the transform and the pairing.
- **L11–13 (docstring T3):** "`phi(k) = 1 - i(k1 + k2)/3 + O(k^2)`" → "`phi(k) = 1 + i(k1 + k2)/3 + O(k^2)`". The minus sign is `conj(φ)`'s expansion, and D1 at L236 checks `+`. Also add the comparator's propagator.
- **L138–148 (B1):** `ph` is declared `positive=True` (L138). Make `φ` complex, with `conj(φ)` an independent symbol, or check T1′(a)–(b) on the tori as `check.py` `T1b`–`T1c` do.
- **L161–177 (B2):** add the sine–cosine cross term `Im φ^s`, or the complex characters (`check.py` `T1c`, `T1f`), and update the message at L177.
- **L232:** comment "`phi(k) = 1 - i (k1 + k2)/3`" → "`+ i`".
- **L237:** D1 message: state the orientation of the drift.
- **L238–248 (D2):** replace the mixed-derivative test by T3′. That means the identity `E = 3|1 − φe^{iω}|² + 3(1 − u)`, the propagator recurrence, the phase identity and the rate series (`check.py` `T3a`–`T3f`), and the message at L248.
- **L253 (`FENCES[0]`):** must equal the new L177 sentence.
- **L299–300 (`N5_LINES`):** "against Re phi(k)^s for every cosine character" → add the sine term; "the non-product form of 1/E by a mixed derivative" → "the comparator's level propagator".
- **L43–51 (`MUTATION_GATE`):** add a mutation that conjugates `φ` in family B (e.g. `"multiplier_conjugated": "B"`); today's B1/B2 pass it, which is the defect's signature. Add one that alters the comparator's propagator in family D.

## 5. What would finish it

(a)–(c) are complete as stated. The edits in §4 are the note owner's: no PR is touched here.

Not searched: any statement outside PRs #8146–#8180 that uses block 35's D2 contrast. The gravity lane's own notes are the likely consumers named in note L73.
