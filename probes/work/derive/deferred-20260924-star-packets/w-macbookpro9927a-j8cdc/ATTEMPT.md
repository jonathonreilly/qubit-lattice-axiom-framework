# deferred-20260924-star-packets, first pass a1: the energy coherence the actual star occurrence needs

**Provenance and scope.**
- Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-macbookpro9927a-j8cdc`, task `J:derive:deferred-20260924-star-packets:a1`.
- This is the first bounded pass on batch 14. It is not an exhaustion of the bundle.
- `origin/main` is `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8` and is the science authority.
- The frozen heads are:
  - PR8923 `191ad04ad48d64c55d31c34521caec68444bfa64`;
  - PR8929 `413c01cc40fd085380125c8e1ec66a61f503eee3`;
  - PR8936 `69462972e8ef9585bdd8d85969e31c7b0b3638c3`.

  They were fetched, and all 13 source blobs read were verified against the manifest SHA256 (RECOVERY_STATUS.json).
- **Related problems, inspected before calculating:**
  - `composite-bodies-rest-energy-without-a-larger-site-algebra`: a3 from the other machine, and a4 from this machine (`w-macbookpro90c72-j16c3`), both confirmed by grok-4.6. They cover contact-bound walkers and a rest energy inside M₂(C).
  - `the-rest-energy-of-a-record` a1, from this machine (`w-macbookpro9927a-j7968`). It covers a record's bare energy under the formation clause.

  None concerns the star's energy supply, coherence or clock. Nothing is reused from them, and none is the same question.
- **Plan, formed before calculating.**
  1. Find the first statement of the PR8923/8929/8936 auxiliary supply and clock work that goes beyond the landed baseline.
  2. Take its fixed-input (preparation) result as given within its hypotheses.
  3. Work out what the physical occurrence itself requires.

## 1. The landed baseline, and the deferred statement chosen

**Landed on main (read there):**
- EXACT_MICROSCOPIC_ENERGY_AT_A_STAR_BIRTH:
  - the four-site star (A vertex 0, B leaves 1–3), with `h = (W − εF)ᵀ(W − εF)` and `H = δε⁻⁴h`;
  - the dressed zero-energy input `d = (A + εFA)/√(1+3ε²)`;
  - the actual marked outputs, with spectral weight `p = cε²/(1+3ε²)` at `Ω = δε⁻⁴(1+3ε²)`, where `c ∈ {2, 1, 3/2}`.
- FINITE_TIME_STAR_ENERGY_AND_SUPPLY_BOUND: `E_total(t) = E_no + (3δ/2ε²)P_b`, and the mean supply bound `E_R(0) ≥ E_total(t)`.
- STAR_ENERGY_COST_ACROSS_THE_ELECTRIC_FAMILY: `H_λ = H₀ + KλE2` with the common preparation, and the attributed uniform-in-λ Duhamel estimate. It gives `sup|z| = O(ε³)`, `E_no = O(ε²)` and `P_b = 1 − e^{−12κt} + O_T(ε²)`, uniformly for `λ ∈ [0,1]`.
- FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS: the buffered battery. It acts as the exact translated unitary on complete blocks, has error `η_L` on all inputs, and is exact on the energy probabilities of energy-stationary inputs ("energy moments agree even when coherences between different energies do not").
- AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS: the history-Hamiltonian clock.

None of these says how much **energy coherence** a supply must provide.

**Deferred, and beyond that baseline.** The statement is PR8929's `coherent_energy_supply_author/COHERENT_FUEL_FOR_ONE_ACTUAL_STAR_OUTPUT.md` (SHA256 `93a93b02…`). Its independent reconstruction is `PRE_COHERENT_ENERGY_SUPPLY.md` (`33420632…`). Its claims:
- **(2)** Every energy-stationary state `σ` has `‖φφ* − σ‖₁ ≥ 2√(p(1−p))`, attained by the dephased output.
- **(4)** A two-level coherent fuel `√(1−p)|0⟩ + √p|1⟩` with gap `Ω` makes `φ` exactly.
- **(5)** The fuel's coherence must satisfy `C_R(η) ≥ 2√(p(1−p))`.

Both packets restrict this to fixed-input **preparation** of one conditional output: "not the original instrument or GKLS process", with no waiting law and no event time.

**The open question.** How much coherence does the physical **occurrence** need from an energy-stationary supply? The occurrence is the GKLS state at a fixed observation time, with births at unrecorded times.

## 2. The residual worked

**Domain.**
- The landed physical star (16 states), for either original instrument.
- `H_λ = δε⁻⁴h + KλE2`, with `λ ∈ [0,1]` and `δ, K, κ, ε > 0`.
- The common dressed input `ψ`.
- The GKLS state `ρ_λ(t)` at a fixed `t > 0`.

**Energy-stationary supply.** A finite environment `(H_R, η)` with `[η, H_R] = 0`, and a joint unitary `U` with `[U, H_λ + H_R] = 0`. Its output is `σ = tr_R U(ψψ*⊗η)U*`.

**Notation.**
- `Δ` pinches onto the distinct eigenvalues of `H_λ`.
- `C_H(ρ) = ‖ρ − Δρ‖₁`.
- `D(ρ)` is the trace distance from `ρ` to the `H_λ`-stationary states.

**Claims.**

(i) **Born-branch factorization** (all λ). The state splits into the unborn and born branches:
```
ρ_λ(t) = |v⟩⟨v| + ∫_0^t w(u) e^{−iH_λ(t−u)} ρ_prep e^{iH_λ(t−u)} du,
w(u) = (4κ/ε²)|⟨s, v(u)⟩|²,     ρ_prep = 𝒥(ss*)/4,
```
- `v` is the unborn branch; `ρ_prep` is the ε-free prepared first-event ensemble.
- So every coherence block of the born branch is `P_b(t) φ_τ(E−E′) P_E ρ_prep P_E′`.
- `φ_τ(ω) = E[e^{−iω(t−τ)} | τ ≤ t]` is the characteristic function of the birth time.

(ii) **λ = 0.**
- The best trace error of any energy-stationary supply is exactly `C_H(ρ₀(t))`.
- It decomposes as
  ```
  C_H(ρ₀(t)) = 2|⟨d,v⟩⟨r,v⟩| + P_b(t) C_prep |φ_τ(Ω)|
             = 4√3 (κ/δ) ε³ e^{−12κt} (1 + O_T(ε²)),
  ```
- The born term is `O(ε⁵)`:
  - `C_prep = (1 + √6/3)ε + O(ε²)` for the resolved instrument and `(√3/3 + 2√6/3)ε` for the coherent one;
  - `|φ_τ(Ω)| = O_T(ε⁴)`.
- **Comparison.** Preparing one actual output needs `2√(p(1−p)) = 2√c ε + O(ε³)`, which is larger by a factor of order `ε⁻²`.

(iii) **λ ∈ (0,1] is not uniform.** The electric term splits the nine-fold zero cluster of N=3:
- the six F-null occupied states sit exactly at `2Kλ`;
- three states sit at `μ₋ = 2Kλ + 3Kλε²(1 − 3ε²) + O(ε⁶)`.

Every energy-stationary supply has trace error at least `2‖P_null ρ P_μ₋‖₁ − C_H(ψψ*)`. As `ε → 0` this tends to the λ-free limit `(1 − e^{−12κt})·2√2/9` (resolved) or `(1 − e^{−12κt})·4√2/9` (coherent). The limit is discontinuous at `λ = 0`.

## 3. Steps

1. **ASSUMED.**
   - The supplied model, the instruments and the GKLS law are as landed.
   - The class of energy-stationary supplies is the deferred note's §2 hypotheses (stationary environment, conserving unitary). No readout is used; conditional versions need effects commuting with `H_R`, as there.
   - No reservoir is adopted and no physical selection is made.

2. **PROVED / CHECKED (E1) — the model, rebuilt from the definitions.**
   - 16 physical states (4 with one record, 12 with three). Every hop and mark stays in the Gauss sector.
   - `h = W − ε(F+Fᵀ) + ε²FᵀF`.
   - On N=3, `h² = (1+3ε²)h` (energies 0 ×9 and `Ω` ×3). On N=1 the spectrum is `{0, 1, 1, 1+3ε²}`.
   - `Σjᵀj = 4W` on N=1 and 0 on N=3, for both instruments.
   - Every mark annihilates `A` and vanishes on N=3.
   - `(W − εF)d = 0`.

3. **PROVED / CHECKED (E2) — the factorization (i).**
   - Let `L₀` be the no-jump generator and `𝒥_κ = (κ/ε²)Σ_m j_m(·)j_mᵀ`.
   - Dyson's identity gives `ρ(t) = e^{tL₀}ρ₀ + ∫₀ᵗ e^{(t−u)L}𝒥_κ e^{uL₀}ρ₀ du`.
   - `𝒥_κ` maps N=1 into N=3 and vanishes on N=3. On N=3 the generator is `−i[H_λ,·]`, because the loss is zero there. So the series stops after one jump.
   - The no-event evolution keeps `span{A, s}` invariant (checked exactly for `H_λ` and for the loss). Hence `v(u) = α(u)A + β(u)s`.
   - Every mark kills `A`, so `𝒥_κ(vv*) = (κ/ε²)|β|²𝒥(ss*)`, with `tr 𝒥(ss*) = 4` exactly for both instruments.
   - Projecting onto eigenspaces gives the blocks. Also `P_b(t) = ∫₀ᵗ w`.
   - The prepared outputs are ε-free, as the landed note states. The occurrence differs from the preparation only through the birth-time law.

4. **PROVED — Lemma A (stationary supplies give nearly stationary outputs).**
   - `X ↦ tr_R U(X⊗η)U*` is covariant: `[U, H + H_R] = 0` and `η` is stationary.
   - So `σ′ = tr_R U(Δ(ψψ*)⊗η)U*` is stationary, and `‖σ − σ′‖₁ ≤ C_H(ψψ*)` by contractivity.
   - Hence `D(σ) ≤ C_H(ψψ*)`, and `‖σ − ρ‖₁ ≥ D(ρ) − C_H(ψψ*)`.
   - At `λ = 0`, `ψ = d` is an eigenvector, so `σ` is exactly stationary.

5. **PROVED — Lemma B (distance to the stationary set).**
   - Take `E ≠ E′` and the polar decomposition `P_E ρ P_E′ = V|P_E ρ P_E′|`, and set `Y = V + V*`.
   - Then `‖Y‖ ≤ 1`, `tr(Yσ) = 0` for every stationary `σ`, and `tr(Yρ) = 2‖P_E ρ P_E′‖₁`.
   - So `D(ρ) ≥ 2‖P_E ρ P_E′‖₁`.
   - If `ρ` is supported in two eigenspaces, `σ = Δρ` attains it: `D(ρ) = C_H(ρ)`. This is the deferred note's (2), for any rank.
   - `ρ₀(t)` is supported in the eigenspaces `{0, Ω}`: the no-event branch stays in `span{d, r}` and N=3 has only these two energies.

6. **PROVED — Lemma C (attaining it at λ = 0, and the energy law).**
   - **The supply.** A stationary carrier with levels `{0, Ω}`, populations `(1 − p_hi, p_hi)`, and a zero-energy classical register.
   - **The unitary.** A conserving swap sends `d⊗|0⟩⊗|k⟩ → a_k⊗|0⟩⊗|k⟩` and `d⊗|Ω⟩⊗|k⟩ → b_k⊗|0⟩⊗|k⟩`. Here `a_k` and `b_k` are ensemble decompositions of the two diagonal blocks of `Δρ₀(t)`.
   - This makes `Δρ₀(t)` exactly. So the best error over energy-stationary supplies is exactly `C_H(ρ₀(t))`.
   - **The energy law, for any conserving account from `d`,** stationary or not, with `H_R ≥ 0`:
     - it must satisfy `P_η(H_R ≥ Ω) ≥ P_final(H ≥ Ω) = p_hi(t)`, since `H + H_R` is conserved and `H_R ≥ 0`;
     - `p_hi(t) = E_total(t)/Ω`, because `ρ₀(t)` has only the energies 0 and `Ω`.
   - This dominance is the sharp form of the landed mean bound. An energy-eigenstate supply must hold at least `Ω`, which is `1/p_hi` times `E_total`.

7. **PROVED / CHECKED (E3, N1, N2) — (ii).**
   - **The decomposition.** By steps 3 and 5 on the two orthogonal record sectors, `C_H = 2|⟨d,v⟩⟨r,v⟩| + P_b C_prep |φ_τ(Ω)|`. Checked against the direct 256-dimensional superoperator to `1e−9` relative at six points (resolved and coherent, `ε = 0.3, 0.2, 0.15`).
   - **The no-event coefficient (E3).** The slow root is `z_s = −6κ + (18κ − 12iκ²/δ)ε² + O(ε⁴)`, the landed value. The slow eigenvector's high component is `−2√3 i(κ/δ)ε³ + O(ε⁵)`.
   - **The fast coefficient** is `O(ε³)`, with `Re z_f = −2κ/ε² + O(1)`, as in the landed eigenvector argument. So `C_no = 4√3(κ/δ)ε³e^{−12κt}(1 + O_T(ε²))` plus a fast part that is exponentially small at fixed `t`.
   - **`|φ_τ(Ω)| = O_T(ε⁴)`.** `w` is a sum of four exponentials:
     - the slow-slow term (amplitude `O(κ)`) integrates against `e^{iΩu}` to `O(κ/Ω) = O(ε⁴)`;
     - the resonant cross term (amplitude `O(κε²)`, decay `2κ/ε²`) gives `O(ε⁴)`;
     - `P_b` is bounded below at fixed `t > 0`.
   - **`C_prep`.** From `P_Ω φ = −ε(Fφ − εFᵀFφ)/(1+3ε²)`, `C_prep = 2‖ρ_prep Fᵀ‖₁ ε + O(ε²)`. The constant is `1 + √6/3` (resolved) and `√3/3 + 2√6/3` (coherent), exact by sympy.
   - **N2 (float).** `C_H/[4√3ε³e^{−12κt}] = 1.0041, 1.0020, 1.0005` at `ε = 0.1, 0.05, 0.025`. `C_born/ε⁵` stays near 6, and `C_prep/ε → 1.813 → 1 + √6/3`.

8. **PROVED / CHECKED (E4, N3) — (iii).**
   - **The spectrum (E4, exact in λ, K, δ, ε).**
     - The six F-null occupied states `x` satisfy `(W − εF)x = 0`, `Wx = 0` and `E2x = 2x`, so `H_λx = 2Kλx` exactly.
     - The other six N=3 states form three identical invariant blocks `span{σ_f, f}`, with matrix `δε⁻⁴[[3ε², −√3ε], [−√3ε, 1]] + Kλ diag(2, 3)`.
     - The shifted block has determinant `3Kλδ/ε²` and positive trace. So `μ₋ > 2Kλ` for every `λ > 0`, with `μ₋ − 2Kλ = 3Kλε²(1 − 3ε²) + …`.
   - **The born coherence between the two parts.** `ρ_prep` lives on the occupied states and annihilates the full-B states `f`. Write the `μ₋` eigenvectors as `c₁σ_f + c₂f`. Then `‖P_null ρ P_μ₋‖₁ = P_b(t) |φ_τ(ω_λ)| |c₁| Ĉ/2` exactly, with:
     - `ω_λ = μ₋ − 2Kλ`;
     - `|c₁| = 1 − O(ε²)`;
     - `Ĉ = 2‖P_null ρ_prep P_sym‖₁ = 2√2/9` (resolved, singular values `√2/18`, `√2/36`, `√2/36`) and `4√2/9` (coherent), exact.
   - **The limit.**
     - `|φ_τ(ω)| ≥ E cos(ω(t − τ)) ≥ cos(ωt)` for `ωt ≤ π/2`, and `ω_λ t = O(ε²)`.
     - The landed uniform Duhamel estimate gives `P_b → 1 − e^{−12κt}` uniformly in λ.
     - The input's own coherence `C_H(ψψ*)` comes from `ψ` against the λ-perturbed `N=1` eigenvectors. It is `O(ε⁵)`: the float values give `C_H(ψψ*)/ε⁵ → 3.45` at `λ = 1` and `0.863` at `λ = 1/4`, i.e. about `2√3 Kλ/δ`.
     - By Lemmas A and B, the error of every energy-stationary supply is at least `(1 − e^{−12κt})Ĉ − o(1)`.
   - **N3 (float, `t = 0.1`).**
     - Resolved: `C_H(ρ) = 0.20965, 0.21506, 0.21820` at `ε = 0.2, 0.1, 0.05`, against the limit `0.21961`. The obstruction lower bound is `0.194`, `0.213` and `0.218`.
     - Coherent: `0.40429 … 0.43615`, against `0.43923`.
     - `λ = 1/4` and `λ = 1` agree to three digits.

9. **Reading (c).**
   - The coherent fuel's `2√(p(1−p))` is a cost of **preparing** a conditional output at a known moment.
   - **At λ = 0 the occurrence at a fixed observation time** needs only `O(ε³)` coherence, carried almost entirely by the unborn branch. An unrecorded birth time multiplies every born coherence by the birth-time characteristic function at the Bohr frequency, and at `Ω ~ ε⁻⁴` that function is `O(ε⁴)`.
   - **For λ > 0** the electric term creates a Bohr frequency `3Kλε²` that the birth time cannot average. A strictly stationary supply then misses by `O(1)`.
   - So the λ-uniform energy bill of the landed notes does **not** give a λ-uniform stationary supply.

## 4. Where the route stops, and the next obligation

- **The first step this pass does not reach** is a time-resolved version of (iii).
  - The λ > 0 obstruction sits at the slow Bohr frequency `ω_λ ≈ 3Kλε²`. Exact stationarity demands a phase reference over times far beyond `1/ω_λ`, and the pinching `Δ` is discontinuous at `λ = 0`.
  - A physically uniform statement needs covariance restricted to a finite horizon, or coherence counted only across gaps `≥ ω_min`. That notion, and the obstruction under it, are open.
- **Also open:**
  - the heralded or time-stamped version: conditioning on the birth time restores `2√(p(1−p))` per output, and a time record needs a clock, whose coherence consumption in the landed clock construction is not computed;
  - general graphs and repeated births, where the Dyson series no longer stops after one jump.
- **Not claimed:**
  - any physical reservoir or selection of λ;
  - any no-go for coherent supplies (the landed battery is coherent and works);
  - any audit status.

The next ranked source groups are in RECOVERY_STATUS.json.

## 5. Running it

```
python3 probes/work/derive/deferred-20260924-star-packets/w-macbookpro9927a-j8cdc/check.py
```

- **Dependencies:** sympy, numpy and scipy.
- **Checks.** Four exact families (E1–E4, sympy) and three labelled float families (N1–N3, the full 256-dimensional GKLS superoperator).
- **Runtime:** a few seconds.
- **Mutation census: 7 of 7 caught.**
  - a mark that needs only an empty A (E1, Gauss);
  - a hop onto an occupied leaf (E1);
  - half the loss in the no-event generator (E3);
  - E2 counting the vertex (E4, N3);
  - a doubled born weight (N1);
  - a wrong limit constant (N3);
  - a wrong-sign dressed input (N1, N3).
