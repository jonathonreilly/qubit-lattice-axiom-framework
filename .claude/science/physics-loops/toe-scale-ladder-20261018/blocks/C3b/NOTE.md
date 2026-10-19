# C3b: Ergodic covariant formation clocks: internal-symmetry order needs infinite ancestries; noisy, power-law and nucleation-growth clocks have none

**Block:** C3b of `toe-scale-ladder-20261018`. It follows up the OPEN items of `blocks/C3/NOTE.md` §7: ergodic covariant long-range clocks, `λmin = 0`, and non-Markov rates.
**Date:** 2026-10-19. **Status:** author draft. Not independently reviewed. Unaudited.
**Claim types:**
- `PROVED`: proof given here, from the stated premises.
- `IMPORTED`: a standard theorem, cited and not re-proved.
- `CONDITIONAL`: an implication from an imported premise.
- `EXACT-CHECK`: a finite exact certificate.
- `NUMERICAL`: Monte Carlo with finite-size scaling. Error bars are 1 SE over independent samples.
- `OPEN`.

**Runner:** `scripts/run_all.sh` writes `logs/run_all.log` (the TOTAL line is quoted in §9). Per-script output is in `logs/*.out`.

## 0. Result up front

The target question splits into two answers. They depend on **which symmetry** the order breaks.

1. **Literal question: yes, trivially, and only by inheritance (EXACT-CHECK, witness X, §2).**
   - *Clock:* `T_x = (x_1+x_2+x_3 + φ) mod 2 + 0.4·U'_x`, with `φ` a uniform random phase and `U'` iid uniform.
   - *Properties:* the clock is translation-ergodic and `O_h`-covariant in law.
   - *Rule:* nearest-neighbour, "content 1 iff some neighbour formed earlier".
   - *Result:* the record is exactly the late-sublattice indicator, with `Cov(ξ_0, ξ_x) = ±1/4` at every distance. That is genuine LRO of an ergodic law.
   - *Interpretation:* the record copies a crystal pattern that the clock already has. The clock is not mixing. No internal symmetry is broken.
   - **So ergodicity of the clock is the wrong hypothesis.** The two meaningful hypotheses are mixing (for positional order) and internal symmetry (for phase or colour order).
2. **Internal-symmetry order (the I-16 kind) needs infinite ancestries, for every clock law (PROVED, Theorem K, §3).**
   - *Setting:* let a group `Γ` act on the menu and preserve the rule. Majority/Potts rules and the I-16 six-axis rule are examples. The clock law is **arbitrary**: it need not be ergodic, mixing or covariant. The marks are iid.
   - *Bound:* for every `Γ`-mean-zero local `f`, `|E f(ξ_A) g(ξ_B)| ≤ ‖f‖‖g‖ · P(Anc(A) ∩ Anc(B) ≠ ∅)`.
   - *Consequence:* if ancestries are a.s. finite, no ergodic component breaks `Γ`, and order-parameter correlations decay at the rate of the ancestry tail.
   - *Corollary for d = 1:* there, every stationary clock has finite ancestries, by Poincaré recurrence (Prop. K3). So internal SSB never occurs in d = 1.
3. **Positional/local LRO needs a non-mixing clock or infinite ancestries (PROVED, Theorem M, §2).** If ancestries are a.s. finite, the record is a translation-equivariant factor of (clock, marks). A factor of a mixing system is mixing. So no local observable has covariance-LRO.
4. **Finite ancestries hold for the three candidate mechanisms:**
   - **Theorem H (PROVED, §4).** Suppose the clock has a non-interpolable local random component: conditional on `T_0`, every finite set of other clocks has density `≤ K^{|S|}`. Then `P(L(0) ≥ n) ≤ c_n (KM)^n/n! + P(T_0 − min_{B(0,n)} T > M)`. Sublinear oscillation therefore gives finite ancestries.
     - This covers candidate **(b)**: every stationary Gaussian clock with `∫ f^{-1} < ∞`, including all power-law covariances, and every fractional (gradient-stationary) Gaussian clock with Hurst `H < 1`.
     - It covers candidate **(c)** for any additive noise strength `s > 0`.
     - For Gaussian clocks it also bounds record correlations by the clock's maximal correlation. Power-law record correlations are allowed; LRO is not.
   - **Theorem J (PROVED, §5).** Take any formation dynamics with bounded rates `λ ≤ λmax`, finite range and **arbitrary history dependence**, with `λmin = 0` allowed. If every site forms a.s., then the coding radius satisfies `P(R ≥ n+1) ≤ P(τ_0 > t) + c_n(λmax t)^{n+1}/(n+1)!` for every `t`. So the record is a finitary factor of iid (FFIID): mixing, no LRO and no SSB.
     - This closes candidate **(a)**, nucleation-growth.
     - For nucleation rate ε and growth rate ≥ a, the correlation length satisfies `ξ(ε) ≤ C ε^{−1/(d+1)}`. That is the Kolmogorov–Johnson–Mehl–Avrami (KJMA) scale. The simulated exponent is `−0.326 ± 0.005` in d = 2, against the KJMA value −1/3 (NUMERICAL).
     - The trivial case `λ(∅) = 0` with no seeds forms nothing at all (Prop. J3).
5. **What LRO there is, and where.**
   - Nucleation-growth (a): only the domain size diverges as ε → 0. The ε → 0 limit is the non-ergodic q-colour mixture of C3 §1.
   - Fractional clocks (b) as `H → 1`: the ancestry scale of Theorem H grows like `exp(O(1/(1−H)))`. At `H = 0.95` the simulated boxes (up to 512²) still show growing `⟨L⟩` and `χ_L` (NUMERICAL, §7). This is a **divergent crossover length, not LRO**: Theorems H and K prove that colour correlations vanish at every `H < 1`.
   - The ordered endpoint `H = 1` is the random-tilt level clock, which is non-ergodic.
   - Noise-free two-stage Voronoi–level clocks (c), whose cell interiors run Toom's eroder: colour correlation length about 0.3 ℓ, and no LRO in finite-size scaling (NUMERICAL).
6. **Still OPEN.**
   - Mixing, `O_h`-covariant clocks in d ≥ 2 that **violate both** Theorem H's premise and Theorem J's premise. These are clocks with no non-interpolable local randomness and no bounded-rate Poisson representation, such as deterministic factor clocks and deterministic growth delays (`λmax = ∞`). For these, finiteness of ancestries is not proved. No example with infinite ancestries is known to me.
   - Holes and jamming, i.e. sites that never form.

**Net answer to the target.** Within the classes of Theorems H and J, an ergodic covariant clock **cannot** produce internal-symmetry long-range order, or any LRO of local observables if the clock is mixing. That is a proved no-go on an explicitly quantified family. The only ergodic LRO it can produce is crystal order copied from a non-mixing clock. The candidate mechanisms (a), (b) and (c) give large but finite domains.

## 1. Setting and reduction

The setting is as in C3 §1: `Z^d` with nearest neighbours (`D = 2d`), a finite menu `M`, a finite-range normalised rule `r_x(·|η)`, iid uniform marks `U` independent of the clock field `T` (of any law), and the strict-earlier convention. `L(x)`, `Anc(x)` (which contains x itself) and `c_n ≤ D(D−1)^{n−1}` are as in C3.

**Lemma 0 (PROVED).**
- The formation equations, and hence `Anc`, `L` and the set of solutions, depend on `T` only through the edge orientation field `o(x,y) = sign(T_x − T_y)`, `y ∈ N(x)`.
- They are therefore unchanged under strictly monotone maps of `T` and under adding a global constant.
- So "ergodic/mixing clock" may be read as ergodic/mixing **increments**. Gradient-stationary clocks such as fractional Gaussian fields are admissible.

**Lemma 1 (PROVED; C3 A1 argument).** Suppose `Anc(x)` is a.s. finite for every `x`. Then:
- there is exactly one solution `ξ = F(T,U)`, computed on the finite DAG `Anc(x)`;
- `F` is measurable and commutes with every lattice automorphism that preserves the rule;
- given `T`, the law of `ξ|_{Anc(A)}` is the sequential kernel `∏_{y∈Anc(A)} r_y(ξ_y | ξ|_{earlier nbrs})`, and it is independent of the selector.

## 2. Mixing transfer and the inherited-order witness

**Theorem M (PROVED from IMPORTED ergodic theory).** Let `T` be stationary, with ancestries a.s. finite.
- (i) If `T` (or its increments) is ergodic, the record law is ergodic. The product of an ergodic action with an iid (Bernoulli, hence weakly mixing) action is ergodic (IMPORTED), and a factor of an ergodic system is ergodic.
- (ii) If `T` (or its increments) is mixing, the record is mixing: a product of mixing systems is mixing, and so is any factor. Hence `Cov(f(ξ_A), g(ξ_{B+x})) → 0` for all local `f, g`, and there is no covariance-LRO.
- *Contrapositive:* covariance-LRO of the record requires either infinite ancestries or a non-mixing orientation field.

**Witness X (EXACT-CHECK s1(a)).** This is the clock and rule of §0 item 1.
- Parity of `x_1+x_2+x_3` is invariant under all 48 elements of `O_h` (checked exhaustively). Under the random phase the clock is stationary and ergodic: a transitive two-point rotation times iid.
- The noise (amplitude < 1/2) never reverses the sublattice order.
- The record equals the late-sublattice indicator in every sample. `Cov = +1/4` at even and `−1/4` at odd separation.
- So the target's literal hypothesis ("the clock field itself ergodic") permits LRO. That LRO is the clock's own crystal structure, read off by a nearest-neighbour rule. Ancestries have depth 1.

## 3. Theorem K: internal symmetry cannot break with finite ancestries, for any clock law

**Theorem K (PROVED).**
- *Premises:* `Γ` is a finite group acting on `M` with `r_x(γs | γ∘η) = r_x(s|η)` for all `x, s, η`. `T` has an arbitrary law and is independent of the iid marks. `A, B` are finite. `f: M^A → R` is `Γ`-mean-zero, i.e. `Σ_γ f(γs) = 0` for all `s`, and `g` is any bounded function. `Anc(A), Anc(B)` are a.s. finite.
- **(K1)** `|E[f(ξ_A) g(ξ_B)]| ≤ ‖f‖_∞ ‖g‖_∞ · P(Anc(A) ∩ Anc(B) ≠ ∅)`.
- **(K2)** In addition, suppose `T` is stationary, the rule is translation-covariant, and `P(L(0) ≥ n) → 0`. Then every translation-ergodic component `μ_ω` of the record law has `E_{μ_ω} f = 0` for every `Γ`-mean-zero local `f`, i.e. no spontaneous breaking of `Γ`. Moreover, `Cov(f(ξ_A), f(ξ_{A+x})) ≤ ‖f‖² · 2|A| P(L(0) ≥ (|x| − diam A)/2)`.
- **(K3, d = 1)** Every stationary real clock on `Z` (any law, ergodic or not) has a.s. finite ancestries. Hence (K2) holds for all stationary clocks in d = 1.

**Proof.**
- **(K1).** `E_T := {Anc(A) ∩ Anc(B) = ∅}` is `T`-measurable. By Lemma 1, given `T`, `ξ_A` is a function of `U|_{Anc(A)}` and `ξ_B` of `U|_{Anc(B)}`. On `E_T` these are disjoint, so the two are conditionally independent. The conditional law of `ξ_{Anc(A)}` is a product of rule kernels, which is `Γ`-invariant by the hypothesis on `r`. Hence `E[f(ξ_A)|T] = 0`, and `E[fg|T] = 0` on `E_T`. Off `E_T`, `|E[fg|T]| ≤ ‖f‖‖g‖`.
- **(K2).** `Anc(y) ⊂ B(y, L(y))`, so an overlap forces some `L(y) ≥ (|x| − diam A)/2` for `y ∈ A ∪ (A+x)`. Take a union bound with stationarity. Let `S_n` be the box average of `f∘θ_x`. Then `E S_n² → 0` by K1, while `S_n → E_{μ_ω} f` in `L²` (mean ergodic theorem, IMPORTED). So `E[(E_{μ_ω}f)²] = 0`.
- **(K3).** In d = 1 a decreasing path is a straight monotone run. On the event of an infinite run `T_0 > T_1 > T_2 > …` to the right, take a rational interval `I ∋ T_0` of length `< T_0 − T_1`. Poincaré recurrence for the shift (IMPORTED) gives `T_n ∈ I` for infinitely many `n`, a.s. on `{T_0 ∈ I}`. But `T_n < T_1 < inf I` for `n ≥ 2`, a contradiction. A countable union over `I` and over both directions shows the event is null. ∎

**Checks.**
- EXACT-CHECK s1(e): ring `Z_7`, noisy majority with δ = 1/10. The clock is ½ deterministic order plus ½ iid, which is non-exchangeable and non-mixing. `E σ_0 = 0` exactly, and `|E σ_0σ_r| ≤ P(overlap)` holds for r = 1, 2, 3, with exact rationals (e.g. r = 3: 0.4425 ≤ 0.6984).
- NUMERICAL: s3 checks K1 for the Gaussian clocks. Those bounds are not tight.

**Consequences.**
- I-16's six-axis rule is invariant under `O_h` acting on the **menu alone** (it uses only the relations `v' = v`, `−v` or `⊥ v`; C3 §6). So I-16's six ordered phases are internal SSB, and K says they **require** infinite ancestries, as the level clock has.
- More generally, any "Toom-type" ordering of a symmetric menu needs decreasing paths of unbounded length with positive probability.

## 4. Theorem H: non-interpolable local randomness forces finite ancestries (candidates b, c)

**Premises.**
- (H1) For every finite `S ⊂ Z^d∖{0}`, conditional on `T_0`, `T_S` has a density `≤ K^{|S|}`.
- (H2) `ψ_n(M) := P(T_0 − min_{|y|≤n} T_y > M)`.

**Theorem H (PROVED).**
- **(H-a)** `P(L(0) ≥ n) ≤ c_n (KM)^n / n! + ψ_n(M)` for all `n ≥ 1`, `M > 0`.
- **(H-b)** Suppose (H1) and (H2) hold at every site with the same `K` and `ψ`, and `ψ_n(ηn) → 0` for some `η < 1/(e(D−1)K)`. Then `P(L ≥ n) → 0`, ancestries are a.s. finite, and Theorems M and K apply.

**Proof.** `L(0) ≥ n` gives a strictly decreasing self-avoiding walk (SAW) `0, y_1, …, y_n` inside `B(0,n)`. Off the `ψ` event, all its values lie in `(T_0 − M, T_0)`. Conditional on `T_0 = t`, the probability that a fixed SAW satisfies `t > T_{y_1} > … > T_{y_n} > t−M` is at most `K^n · vol{t > u_1 > … > u_n > t−M} = (KM)^n/n!`. Take a union over the `c_n` SAWs. For (H-b), use `n! ≥ (n/e)^n`: then `c_n (Kηn)^n/n! ≤ (D/(D−1)) (e(D−1)Kη)^n → 0`. ∎

**Sufficient conditions for (H1) (PROVED).**
- (i) `T = T_1 + Y`, with `Y` iid of density `≤ K` and independent of `T_1`. `T_1` is arbitrary, possibly non-stationary. Proof: condition on `(T_1, Y_0)`, then average.
- (ii) `T` stationary Gaussian with spectral density `f` and `v := [∫ f^{-1} dk/(2π)^d]^{-1} > 0`. Then `K = (2πv)^{-1/2}`. Proof: `det Cov(T_S | T_0) = ∏_k Var(T_{y_k} | T_0, T_{y_1..y_{k−1}}) ≥ v^{|S|}`, because conditioning on more variables lowers the Gaussian conditional variance, and `v = Var(T_0 | T_{≠0})` (Kolmogorov interpolation, IMPORTED).
  - EXACT-CHECK s1(b): on tori, `1/Q_00 = 1/mean(1/f)` to `10^{-9}`, and the determinant bound holds for 600 random `S`.
  - MC s1(d): the volume bound holds for correlated Gaussian paths.

**Corollary H-G (candidate b; PROVED with IMPORTED Maruyama).**
- *Stationary Gaussian clocks* with `∫ f^{-1} < ∞`. Every continuous `f > 0` on the torus qualifies, including power-law `C(r) ~ r^{−α}`, `α > 0`, and smooth fields with finite correlation scale. Then `ψ_n(M) ≤ (|B_n|+1) e^{−M²/(8σ²)}`, so ancestries are finite. If `C(r) → 0`, the field is mixing (Maruyama, IMPORTED), and Theorems M and K give no covariance-LRO and no internal SSB.
- *Gradient-stationary (fractional) Gaussian clocks*: `f(k) = lap(k)^{−(1+H)}`, `0 < H < 1`, where `lap(k) = Σ_i (2 − 2cos k_i)` is the lattice Laplacian symbol (as in `s3`). Here `f ≥ (4d)^{−(1+H)} > 0`, so (i) applies with `K = (2π (4d)^{−(1+H)})^{−1/2}`. Also `Var(T_0 − T_y) ≤ A|y|^{2H}`, so `ψ_n(ηn) ≤ |B_n| e^{−η²n^{2−2H}/(2A)} → 0`. Ancestries are finite for every `H < 1`. The increment covariance decays like `r^{2H−2} → 0`, so the increments are mixing (IMPORTED, vector Maruyama). There is no LRO.
- *Quantitative bound (H4, CONDITIONAL on the imported Csáki–Fischer and Kolmogorov–Rozanov facts).* Let `ρ_m(A,B)` be the maximal correlation of the clock on the disjoint windows `A+B(m)` and `B+B(m)`. Then
  `|Cov(f(ξ_A), g(ξ_B))| ≤ ‖f‖‖g‖ [ρ_m(A,B) + 2(|A|+|B|) P(L ≥ m)]`.
  For a Gaussian clock, `ρ_m` is the largest canonical correlation. So record correlations can be at most as long-ranged as the clock's canonical correlations. Power laws are allowed; LRO is not.

**Scale (s3b, indicative).** The `n*` with `P(L ≥ n*) ≤ 1/2` guaranteed by (H-a), in d = 2:

| Clock | `n*` |
|---|---|
| power law, α = 0.25 | 47 |
| power law, α = 1 | 30 |
| fractional, H = 0.5 | 954 |
| fractional, H = 0.8 | ≈ 1.2·10⁹ |
| fractional, H = 0.95 | > 10¹⁵ |

The bound is crude. It shows that the theorem's guarantee is effective only beyond a scale that grows like `exp(O(1/(1−H)))`.

**Candidate (c) with noise.** The two-stage clock of s4 is a cellwise level clock `⟨w_c, x − n_c⟩ + V_c` plus `sZ`. With any `s > 0` it satisfies (i), with `K ∝ 1/s`, and its oscillation is bounded by the cell diameters, which grow like `(log n)^{1/d}`. So ancestries are finite: no LRO and no internal SSB (PROVED). The scale of the bound is about `e(D−1)ℓ/s`.

## 5. Theorem J: bounded rates with `λmin = 0` and history dependence (candidate a; C3 options iii and iv)

**Model (graphical).**
- Each site has a Poisson process `Π_x` of rate `λmax`, with iid marks `(V, U)`. Optionally there are iid site marks `χ_x` (seeds).
- A point at `(x,t)` with `x` blank is accepted iff `V ≤ λ_x(H_x(t−), χ_x)/λmax`.
- `H_x(t−)` is the **full history** on `[0,t)` of the states in `x + N_0` (who formed, when, with what content).
- `λ_x` is any measurable functional with values in `[0, λmax]`; zero is allowed. The content is `Φ_x(H_x(t−), U)`.
- This includes Markov rates, time-inhomogeneous rates, age-dependent rates, and all of C3 Theorem C.

**Theorem J (PROVED).**
- **(J1)** For each `t`, a.s. only finitely many points lie on backward chains from any site with `t_0 ≤ t`. So the dynamics on `[0,t]` is well-defined and locally determined (Harris argument).
- **(J2)** Suppose `τ_0 < ∞` a.s., i.e. every site forms. Then for every `t > 0`,
  `P(R(0) ≥ n+1) ≤ P(τ_0 > t) + c_n (λmax t)^{n+1}/(n+1)!`.
  Hence the final record is a finitary factor of iid: mixing of all orders, with no LRO and no SSB (Theorems M and K). Taking `t = n/(2e(D−1)λmax)` makes the second term `≤ (D/(D−1)) 2^{−n}`.
- **(J3)** Suppose `λ_x = 0` whenever the neighbourhood history is empty, and the start is empty with no seeds. Then a.s. no site ever forms.

**Proof.**
- **(J1)–(J2).** Use backward chains `(y_k, t_k)` as in C3 §4, with `t_0 > … > t_n`, `y_k ∈ N(y_{k−1})`, and each `t_k` **any** point of `Π_{y_k}`. No relevance cutoff is needed.
  - Along a fixed SAW, the expected number of chains with `t_0 ≤ t` is `λmax^{n+1} vol{t ≥ t_0 > … > t_n > 0} = (λmax t)^{n+1}/(n+1)!` (MC check s1(c)).
  - The loop erasure of C3 (C2) applies verbatim.
  - The decision at a point `(x,s)` needs only the neighbourhood history on `[0,s)`. That history is decided by earlier points of neighbours, recursively. A neighbour with no point before `s` is blank on `[0,s)`.
  - `ξ_0` is fixed by the points of `Π_0` in `(0, τ_0]` and by what is reachable from them. On `{τ_0 ≤ t}` everything lies in chains with `t_0 ≤ t`. Markov's inequality then gives the bound, and the read-set is `reach ∪ ∂reach`.
- **(J3).** On `[0,t]` the reach is finite. Its earliest accepted point would have an empty neighbourhood history, hence rate 0, a contradiction. ∎

**Corollary J-KJMA (candidate a; PROVED).**
- *Premises:* rates are `≥ ε` for every blank site and `≥ a` once a neighbour has formed, and `λmax < ∞`.
- *Formation-time tail.* Let `r = ⌊at/4⌋`. Then
  `P(τ_0 > t) ≤ exp(−ε|B_r| t/2) + P(Gamma(r,a) > t/2) ≤ exp(−c_d ε a^d t^{d+1}) + e^{−0.3 r}`.
  The first term: if nothing in `B(0,r)` has formed by `t/2`, every site there is still blank and isolated, and so nucleates at rate `≥ ε`. The second: growth from the first formed site along a geodesic is dominated by a sum of `Exp(a)` variables (strong Markov property in the graphical construction).
- *Conclusion:* `P(R ≥ n+1) ≤ C(2^{−n} + e^{−c'n}) + exp(−c'' ε n^{d+1})`. So the local correlation length is `O(ε^{−1/(d+1)})` as ε → 0, i.e. `O(ε^{−1/3})` in d = 2.
- *Comparison with C3 Theorem C.* Theorem C gives the scale `O(1/ε)`, with superexponential tails. The two bounds are complementary.
- *Seeded variant* (iid seeds of density `p`, rate 0 for isolated non-seeds, so `λmin = 0`): `τ_0 < ∞` a.s., and J applies.

**Relation to KJMA, Toom and erosion.**
- The domains are Johnson–Mehl cells, of linear size `(a/ε)^{1/(d+1)}`.
- Toom-type stability, i.e. non-ergodicity of a positive-rate PCA, needs a **time direction along which the same sites are re-updated**. In a formation process each site is written once. Re-updating is mimicked only along infinitely long decreasing paths, which (J2) excludes.
- This is exactly the level-clock case. With `T_x = x_1+x_2+x_3` and the noisy majority-of-earlier-neighbours rule (q = 2), the 3D record is the space-time history of Toom's NEC majority PCA, since each site's three earlier neighbours are `x − e_i`. By Toom (1980, IMPORTED), it has ≥ 2 phases at small noise. This is a second G-II witness besides I-16, CONDITIONAL on Toom's theorem.

## 6. Candidate (c) without noise, and the renormalisation picture

**Clock.** Poisson–Voronoi cells of mean volume ℓ³. Each cell gets a uniform random body diagonal `w_c`, and `T_x = ⟨w_c, x − n_c⟩`, with tie-break `10^{−7}`. This clock is mixing (a factor of iid) and `O_h`-covariant in law.

**What is proved and what is not.** Theorem H's `K` is effectively infinite here, so finiteness of ancestries is **not proved**.

**Picture.**
- Inside a cell each site has exactly three earlier neighbours `x − w_i e_i`. So the noisy-majority rule runs Toom's eroder for about ℓ levels, with inflow from earlier cells.
- At the cell scale this is again a formation process, now with essentially independent cell clocks. That puts the coarse problem back into the finite-ancestry class.
- This is a heuristic (not proved).

**Numerics (s4, NUMERICAL).**
- Colour correlation length `ξ ≈ 2.0, 2.9, 3.7` for `ℓ = 4, 8, 12`, i.e. `ξ/ℓ ≈ 0.3`.
- `⟨L(x)⟩` is independent of the box size `L` (e.g. 11.1 at ℓ = 8 for L = 24, 48, 72).
- `χ_L = N⟨m²⟩` does not grow like `L³`; see the log for the fitted slopes.
- Control: an isolated level-ordered open box gives a strongly ordered late corner, `|m| = 0.94, 0.83, 0.71` for side 16, 32, 48. The within-cell mechanism exists; it is the cells that destroy LRO.

## 7. Numerical results (finite-size scaling)

All criteria were declared in the script headers before running.

**(a) Nucleation-growth, d = 2 (s2).**

| ε | `ξ(1/e)` |
|---|---|
| 1e-2 | 4.15 ± 0.02 |
| 3e-3 | 6.04 ± 0.04 |
| 1e-3 | 8.55 ± 0.05 |
| 3e-4 | 13.0 ± 0.1 |
| 1e-4 | 18.9 ± 0.2 |

- Fit: `ξ ∝ ε^{−0.326 ± 0.005}`, with χ²/dof 7.5, i.e. small curvature from pre-asymptotic corrections. KJMA predicts −1/3.
- At fixed ε, `χ_L` is flat in L: slope −0.04 ± 0.15 (ε = 1e-2) and −0.04 ± 0.26 (ε = 1e-3). LRO would give 2.
- Seeded `λmin = 0` variant: `C(L/2)` is consistent with 0.
- Cross-implementation check: the ε → ∞ limit reproduces the iid-clock model, `C(1) = 0.5768(17)` against `0.5749(19)`.

**(b) Gaussian clocks, d = 2, majority rule (s3, s3b).**
- *Power law, α = 0.25 and 1:* `⟨L⟩ ≈ 2.9` and `2.6`, independent of L. `χ_L` slope 0.01 ± 0.07 and 0.05 ± 0.07.
- *Fractional, H = 0.5:* `⟨L⟩` is 4.97, 5.08, 5.13 for L = 64, 128, 256 (saturating), and the `χ_L` slope is 0.05 ± 0.07.
- *Fractional, H = 0.8:* `⟨L⟩` is 8.7, 10.3, 11.8, 13.3 for L = 64 to 512, and `χ_L` is 37, 40, 45, 54.
- *Fractional, H = 0.95:* `⟨L⟩` is 12.7, 17.7, 23.5, 31.2, and `χ_L` is 62, 70, 110, 131. The `χ_L` slope over 64–256 is 0.34 ± 0.16. LRO would give 2.
- *Declared-criterion failures.* The criterion "`⟨L⟩` stable to 10% between the two largest boxes" **failed** for H = 0.8 and 0.95. These are the 2 FAILs in the total.
  - This is a finite-size observation. It is not in tension with Theorem H, whose effective scale `n*` for these H exceeds 10⁹ (s3b).
  - The numerics alone cannot tell H = 0.95 apart from a slowly ordering system. The no-LRO statement for these H rests on the proof (H-G plus K), not on the simulations.
- *Bond observable* `σ_xσ_{x+e1}`: it shows resolved power-law correlations for H = 0.8 (`~ r^{−2.97±0.09}`) and H = 0.95 (`~ r^{−2.1}`, with χ²/dof 18, unreliable). It is unresolved for the other families.
- *Colour correlations:* at r = 64 they are at most `2·10^{−3}`.

**(c) Two-stage clock (s4).** See §6 and `logs/s4_two_stage.out`.

## 8. No-Go Discipline Gate (N1–N8)

The negative claim is: no internal SSB, and no local LRO for mixing clocks, within the clock classes of Theorems H and J, and in d = 1 for all stationary clocks.

**N1, routes that might evade it.**
1. A non-mixing ergodic clock. ATTEMPTED: it **succeeds** for positional order (witness X). The claim is narrowed accordingly.
2. Power-law Gaussian clocks. ATTEMPTED; closed by H-G.
3. Fractional clocks with `H → 1`. ATTEMPTED; closed for every `H < 1`. The crossover scale diverges, and the numerics do not resolve it at `H = 0.95`.
4. Nucleation-growth with `λmin → 0`, and seeded `λmin = 0`. ATTEMPTED; closed by J.
5. History-dependent (non-Markov) bounded rates. ATTEMPTED; closed by J.
6. Two-stage clocks with noise. Closed by H. Without noise, NUMERICAL only, and OPEN.
7. Deterministic delays or `λmax = ∞`. NOT closed; OPEN.
8. Clocks with ties or exchangeable mixtures. C3's W-tie example breaks no internal symmetry, and its ancestries are finite, so it is consistent with K.

**N2, wall independence.**
- The two escape conditions (non-mixing; infinite ancestries) are independent: X has finite ancestries and is non-mixing, and the level clock has infinite ancestries.
- For internal SSB only infinite ancestries matter (K).

**N3, hidden walls.**
- The marks are iid and independent of the clock.
- The rule has finite range and is normalised; holes are excluded.
- In H: premises (H1) and (H2).
- In J: `λmax < ∞` and every site forms.
- Covariance is used only for stationarity: none of the bounds needs `O_h`.

**N4, residual matching.**
- I-16 and Toom are cited as G-II witnesses with infinite ancestries, which matches the necessity in K.
- KJMA is used only as a numerical comparison.

**N5, rhetoric.**
- "No LRO" means local observables only.
- Divergent correlation lengths, power-law correlations of non-symmetric observables, and non-local cluster observables are **not** excluded.

**N6, partial closure.** Adopting a non-mixing crystal clock gives positional order (X), but only by putting the order into the clock.

**N7, steelman.** "A mixing `O_h`-covariant deterministic clock with no local randomness might have infinite descending paths and order." This is correct as an open possibility. Theorem K says that is exactly what it would need.

**N8, cross-cycle echo.** C3's OPEN items (iii) `λmin = 0` and (iv) non-Markov rates are closed for bounded rates by J, under the premise that every site forms. C3 §7's "power-law Gaussian" OPEN item is closed by H-G.

## 9. Load-bearing steps for independent check

1. **Theorem K1:** the conditional law of `ξ|_{Anc(A)}` given `T` is the `Γ`-invariant product kernel, and the records are conditionally independent on disjoint ancestries.
2. **Theorem H-a:** the conditional density premise (H1), and the volume `M^n/n!` of the band. For Gaussians, the claim `det Cov(T_S|T_0) ≥ v^{|S|}`.
3. **Theorem J2:** chains over **all** Poisson points with `t_0 ≤ τ_0` cover the dependency of `ξ_0` under history-dependent acceptance, and `P(τ_0 > t)` enters only through the event `{τ_0 > t}`.
4. **Witness X** (trivial, but it decides the literal question).

**Files.**
- `scripts/c3b_common.py`
- `scripts/s1_exact_checks.py`
- `scripts/s2_nucleation_growth.py`
- `scripts/s3_gaussian_clocks.py`
- `scripts/s3b_scale_of_theorem_H.py`
- `scripts/s4_two_stage.py`
- `scripts/run_all.sh` → `logs/run_all.log`, which ends with the TOTAL line (`PASS=… FAIL=2`). The 2 FAILs are the declared finite-size criteria in s3 for H = 0.8 and 0.95; see §7.

**Literature, not re-derived.**
- Toom, *Stable and attractive trajectories in multicomponent systems* (1980).
- Maruyama (1949): mixing of Gaussian processes.
- Kolmogorov (1941): interpolation.
- Kolmogorov–Rozanov (1960); Csáki–Fischer (1963).
- KJMA: Kolmogorov 1937, Johnson–Mehl 1939, Avrami 1939.
- Penrose (2002): stabilization for monotone particle systems. This may contain J-type statements; no novelty is claimed for the method.
