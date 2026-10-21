# C3: Clocks with finite ancestry tails force finitary, superexponentially mixing record laws; within bounded-rate Markov clocks, an ordered record phase needs infinite-range clock dependence

**Block:** C3 of `toe-scale-ladder-20261018` (target: `SCALE_LADDER_MAP.md`, section C3; OBL-R2.2).
**Date:** 2026-10-18. **Status:** Independently reviewed (REVIEW.md, verdict ready); unaudited. The independent review (`REVIEW.md`, separate code in `review_scripts/`, `TOTAL: PASS=75 FAIL=0`) found the proofs of A, A′, B, C and D correct and raised non-blocking findings F1–F8. These are applied here; see §12.
**Claim types used:** `PROVED` (proof given here, from the stated premises), `ON-MAIN` (already proved in a cited main note), `COROLLARY` (immediate from ON-MAIN items plus routine steps), `CONDITIONAL` (proved implication from an imported premise), `EXACT-CHECK` (exhaustive finite certificate), `NUMERICAL` (Monte Carlo, declared 4-SE tolerance), `OPEN`.
**Runner:** `scripts/run_all.sh` → `logs/run_all.log`, which ends with `TOTAL: PASS=59 FAIL=0`.

## 0. Result up front

1. **Base case (iid clocks): mostly a corollary of what is on main.** Take any finite menu, any finite-range rule (zeros allowed; site-dependent rules allowed), iid clocks of any law and iid marks. Then the record field is a finitary factor of iid (FFIID). This uses the decreasing-path ancestor argument already on main (2026-09-07, 2026-10-08). The new items are small but real:
   - the explicit coding-radius statement;
   - a **correction of the map's constant**. The bound `D(D-1)^{n-1}/(n+1)!` (with `D = 2d`) is the tail of the longest decreasing path `L`. The coding radius `R` satisfies only `P(R ≥ n+1) ≤ D(D-1)^{n-1}/(n+1)!`. The map's statement `P(R ≥ n) ≤ ...` is **false**: the XOR rule on Z has `P(R≥2) = 2/3 > 1/3` and `P(R≥3) = 17/60 > 1/12` (EXACT-CHECK);
   - two covariance bounds. One decays like `(2e(D-1)/r)^{r/2}`, as the map says. The other is stronger, `exp(-r ln r + O(r))`, and comes from a stopping-set coupling.
2. **New: state-dependent covariant rates.** Let the formation rate be `λ(η) ∈ [λmin, λmax]` with `λmin > 0`, depending on the formed neighbourhood (contents included). Then the record field is still FFIID, with
   `P(coding radius ≥ n+1) ≤ D(D-1)^{n-1} κ^{n+1}/(n+1)!`, where `κ = λmax/λmin`.
   The decay is superexponential **for every finite κ**; there is no threshold. The proof uses a Poisson graphical construction with thinning, a cutoff at each site's first "sure" point, and loop-erased space-time decreasing chains (PROVED). This covers the 2026-09-22 clocks `1+k`, `(1+k)^2` and `1/(1+k)` (κ = 7, 49, 7 on Z^3).
3. **New, elementary: correlated clocks.** Exchangeable tie-free clocks give exactly the iid record law. Clocks that are finite-range factors of iid (`T_x = g(ζ|_{x+K})`) give FFIID with tail `D(D-1)^{n-1}/⌈(n+1)/|K-K|⌉!` (PROVED).
4. **Counterexample family, and what a clock must do to give order.** Items 1–3 rule out a covariant counterexample with bounded rate ratio, finite-range dependence, or tie-free exchangeability. Within bounded-rate Markov clocks, order therefore needs **infinite-range clock dependence**. Two kinds of example exist:
   - **Directed level clock.** The level clock of the 2026-09-16 note is not cubic-covariant. Under it, uniqueness given the data fails (several phases coexist). This is ON-MAIN.
   - **Covariant-in-law mixtures.** The mixture of the level clock over the cubic group is covariant in law, up to a global time shift. Its record field has covariance long-range order `Cov ≥ 0.1388` at every separation (CONDITIONAL on the imported 2026-09-16 theorem T7). This LRO is of the automatic non-ergodic-mixture kind. Its real content is the phase coexistence inherited from I-16, and the phase is extra randomness beyond the clock and marks.

   The reviewer's tie witness is a simpler example of the same kind, and it is unconditional. With probability ½ all clocks are tied; with probability ½ they are iid. The clock is exchangeable and pairwise uncorrelated, yet `Cov = 1/9` for every r ≥ 3 (EXACT-CHECK s3(f)). Other escapes stay OPEN: `λmin = 0`, `λmax = ∞`, and non-Markov rates.
5. **Three-regime classification (Theorem G; not exhaustive).** It gives a necessary condition, with scope:
   - "No order" covers only local observables. It excludes long-range order, spontaneous symmetry breaking (SSB), power-law correlations, Coulomb/pinch-point correlations, and Bragg peaks.
   - It does **not** exclude percolation-type transitions of non-local cluster observables. Example: the formed-site set at a fixed time is exactly Bernoulli percolation (2026-10-08 note), which has a critical point.

## 1. Setting (definitions adopted from the 2026-09-07 note)

- **Graph.** `G = Z^d`. Each site has a finite symmetric neighbourhood `N(x) = x + N_0`, with `0 ∉ N_0` and `D := |N_0|`. Nearest-neighbour: `N_0 = {±e_i}`, `D = 2d`. All graph distances `|x-y|` are in this graph. `c_n` is the number of self-avoiding walks (SAW) of `n` edges from 0, and `c_n ≤ D(D-1)^{n-1}`.
- **Menu and rule.** `M` is a finite menu. A partial neighbour condition `η` is a partial map `N(x) → M`. A rule assigns to each site `x` and each `η` a probability `r_x(·|η)` on `M`; it is normalised for every `η`, including the empty one, and zeros are allowed. The rule is *translation-covariant* if `r_{x+a}(·|η∘τ_a) = r_x(·|η)`. Covariance is used **only** for stationarity statements. The mixing bounds hold for site-dependent rules too.
- **Selector.** `Φ_x(η, u)` is any measurable map with `Φ_x(η, U) ~ r_x(·|η)` when `U ~ Unif[0,1]`. The 09-07 exponential-race selector is one instance.
- **iid-clock model (main-note model).** The data are `ω_x = (T_x, U_x)`, iid over `x`, with `T_x` of arbitrary law and `U_x` uniform and independent of `T_x`. At its formation, `x` sees exactly the neighbours `y` with `T_y < T_x` (strict). Simultaneous formations do not see each other; this matters only if the law of `T` has atoms. The record is `ξ_x = Φ_x(ξ|_{\{y∈N(x): T_y<T_x\}}, U_x)`.
- **Ancestors.** `Anc(x)` is the set of `y` reachable from `x` by a path `x = y_0, y_1, …, y_n = y` with `y_k ∈ N(y_{k-1})` and `T_{y_0} > T_{y_1} > … > T_{y_n}`. Such paths are self-avoiding. `L(x) ∈ [0, ∞]` is the supremum of their lengths, and `S_x := Anc(x) ∪ ∂Anc(x)` is the *explored set*.
- **Coding radius.** `R(x)` is the least `m` such that `ω|_{B(x,m)}` determines `ξ_x`, meaning `ξ_x` is a.s. constant over all modifications of `ω` outside `B(x,m)`. A factor is *finitary* if `R(x) < ∞` a.s.
- **Order notions (local).** A record law has *covariance-LRO* if `limsup_{|x|→∞} |Cov(f(ξ_0), f(ξ_x))| > 0` for some single-site `f`; this is defined for any law. It is *critical/power-law* if some local truncated two-point function decays no faster than a power.
  - For an **ergodic** (extremal) law, covariance-LRO is genuine long-range order, and "long-range order" without qualification means this.
  - For a **non-ergodic** law, covariance-LRO is automatic once the ergodic components have different one-site marginals, and it only signals a mixture. Genuine order is then a property of the ergodic components, e.g. non-unique coexisting phases.
  - G-I (§7) excludes covariance-LRO outright, because its laws are mixing.
  - The §6 witnesses both have covariance-LRO. In `W` it comes from coexisting ergodic phases (I-16). In W-tie it comes only from mixing two clock laws.

## 2. Theorem A: iid clocks (base case)

**Theorem A.** In the iid-clock model:

- **(A1)** A.s. every `Anc(x)` is finite, and there is exactly one field `ξ` satisfying the formation equations.
- **(A2)** `P(L(x) ≥ n) ≤ c_n/(n+1)! ≤ D(D-1)^{n-1}/(n+1)!` for `n ≥ 1`. When the law of `T` is continuous, `E[# decreasing SAWs of length n from x] = c_n/(n+1)!` exactly.
- **(A3)** `R(x) ≤ L(x)+1`. Hence `P(R(x) ≥ n+1) ≤ D(D-1)^{n-1}/(n+1)!`, and `ξ` is a finitary factor of the iid field `ω`. The index shift is necessary: for `d = 1`, `M = {0,1}` and the XOR rule (own mark bit if no earlier neighbour; otherwise XOR of the earlier neighbours' records), `P(R ≥ 2) = 2/3` and `P(R ≥ 3) = 17/60`. These equal `P(L ≥ 1)` and `P(L ≥ 2)` and exceed the map's proposed `2/3! = 1/3` and `2/4! = 1/12`.
- **(A4)** If the rule is translation-covariant, the factor map commutes with translations, so the record law is a stationary FFIID. If a lattice automorphism `g` together with a menu permutation preserves the rule, the record law is `g`-invariant. If the law of `T` is continuous, the record law does not depend on it.

**Claim types.**
- (A1) is ON-MAIN only for iid **Exp(λ)** clocks on Z^3 (`D = 6`), in 09-07 "Infinite recursive construction" (lines 45–49) and 10-08 §2 (line 60). The version for any clock law, clocks with atoms, general `D` and arbitrary rules is COROLLARY: the same proof.
- The first inequality of (A2) is likewise ON-MAIN only for exponential clocks with `D = 6`. For any law and general `D` it is COROLLARY: the same proof with `c_n` in place of `6·5^{n-1}`.
- (A3)–(A4) are PROVED here; they were not stated on main. The XOR values are EXACT-CHECK.

**Proof.**
- **(A2).** For a fixed SAW of `n` edges, the `n+1` iid times are strictly decreasing with probability `P(all distinct)/(n+1)! ≤ 1/(n+1)!`: conditional on all being distinct, exchangeability makes the rank permutation uniform. Take a union bound over the `c_n` SAWs. For continuous laws, linearity of expectation gives the equality.
- **(A1).** Since `P(L ≥ n) → 0` and `{L = ∞} ⊂ {L ≥ n}` for every `n`, `L < ∞` a.s. Local finiteness then gives `|Anc(x)| < ∞`. Evaluate `ξ` on the finite DAG `Anc(x)` in increasing time order; induction forces every value (09-07).
- **(A3).** `S_x` is found by an exploration that reads `T` at `x`, then at the neighbours of every site found to be an ancestor. It reads exactly `S_x`, and `ξ_x` is a function of `(T,U)|_{S_x}`. If `L(x) ≤ m-1`, then `S_x ⊂ B(x,m)` and the event `{L(x) ≤ m-1}` is itself determined by `ω|_{B(x,m)}`, so `R(x) ≤ m`.

  For the XOR example, the script enumerates the ordering and mark classes on the ball together with window extensions. It finds that every class with `L ≥ 1` (respectively `L ≥ 2`) has two extensions with different `ξ_0`. That gives `P(R≥2) ≥ 2/3` and `P(R≥3) ≥ 17/60`. The upper bounds come from `R ≤ L+1`, and the exact `P(L≥n) = 2/(n+1)! − 1/((2n+1) n!^2)` on Z, which is enumerated for `n ≤ 4`.
- **(A4).** The factor map is defined by a translation-equivariant local recursion. If `g` preserves the rule, then `ξ(gω)` and `gξ(ω)` solve the same equations, so uniqueness gives equality, and `gω` has the law of `ω`. When `T` is continuous, only the order of the times enters, and the order is uniform on every finite set. ∎

**Proposition A′ (exchangeable clocks).** Suppose the clock field is exchangeable under all permutations of `Z^d`, a.s. tie-free, and independent of the iid marks. Then the record law equals the iid-clock record law of A4. (PROVED.)

*Proof.* By de Finetti/Hewitt–Savage on the countable index set, the clock field is a mixture of iid fields with a random directing law `Q`. Since `P(T_x = T_y) = E Σ_a Q({a})^2 = 0`, `Q` is a.s. atomless. Conditional on `Q`, A4 says the record law does not depend on `Q`. ∎

## 3. Theorem B: decay of correlations

Let `a(k) := D(D-1)^{k-1}/(k+1)!` for `k ≥ 1`, and `a(k) := 1` for `k ≤ 0`. Let `f, g` be bounded functions of `ξ|_A` and `ξ|_B`, with `A, B` finite and `r := dist(A,B)`.

**Theorem B.** In the iid-clock model:

- **(B1)** `|Cov(f,g)| ≤ 2‖f‖_∞‖g‖_∞ (|A|+|B|) · a(⌈r/2⌉ − 1)`. This is at most the following (useful for `r > 2e(D-1)`; the reviewer notes that it holds for every `r`):
  `2‖f‖‖g‖(|A|+|B|) · (D/(D-1)) · (2e(D-1)/r)^{⌈r/2⌉}`.
  This is the map's `(2e(2d-1)/r)^{r/2}` form, with the prefactor made explicit.
- **(B2)** `|Cov(f,g)| ≤ 2‖f‖‖g‖ · P(S_A(ω) ∩ S_B(ω′) ≠ ∅) ≤ 2‖f‖‖g‖ Σ_z p_A(z) p_B(z)`, where `ω′` is an independent copy of `ω`, `S_A = ∪_{x∈A} S_x`, and `p_A(z) := min(1, Σ_{x∈A} a(|z−x|−1))`. For single sites at distance `r`, the right side is `exp(−r ln r + O(r))`.
- **(B3)** Consequences:
  - the record law is mixing, and in fact mixing of all orders. Mixing of all orders is not derived from the two-set bound B2: it holds because a stationary factor of an iid field is mixing of all orders (IMPORTED, standard), or alternatively by the same coupling applied to k sets;
  - the law has no long-range order and is ergodic, so a rule symmetry cannot be broken spontaneously (the law is unique and invariant by A4);
  - every local truncated correlation decays superexponentially, so every local structure factor `S(q) = Σ_x e^{iqx} Cov(f(ξ_0), f(ξ_x))` extends to an entire function of `q`;
  - hence there are no power laws, no dipolar/Coulomb `|x|^{-d}` correlations, no pinch points and no Bragg peaks.

  By Ornstein–Weiss theory, a stationary FFIID process on `Z^d` is isomorphic to a Bernoulli shift. This is IMPORTED and not used elsewhere.

**Claim types.** (B1), (B2) and (B3) are PROVED here. The asymptotic in (B2) is PROVED with an unoptimised constant. Exact sums for `d = 1` are in s3(c).

**Proof.**
- **(B1).** Let `m = ⌈r/2⌉ − 1`, so `2m < r`. Put `f_m := f·1{R(x) ≤ m ∀x∈A}`. This is `ω|_{A+B(m)}`-measurable, because `{R(x) ≤ m}` and the value of `ξ_x` on it are determined there. Define `g_m` likewise. The two windows are disjoint, so `f_m ⊥ g_m`.

  Write `f = f_m + Δf` with `|Δf| ≤ ‖f‖ 1_{E_A}`, where `E_A = {∃x∈A: R(x) > m}`. Then `|Cov(Δf, g)| ≤ 2E|Δf|‖g‖`, so
  `|Cov(f,g)| ≤ 2‖f‖‖g‖(P(E_A)+P(E_B))`,
  and `P(R > m) ≤ P(L ≥ m) ≤ a(m)`.

  The Stirling form follows from `(k+1)! ≥ ((k+1)/e)^{k+1}` with `k+1 = ⌈r/2⌉ ≥ r/2`.
- **(B2).** `S_A` is a stopping set: the event `{S_A = S}` is determined by `ω|_S`. Let `ω*` equal `ω` on `S_A(ω)` and `ω′` elsewhere. Summing over the countably many finite `S`, `ω*` has the law of `ω`, because `P(S_A(ω)=S, ω|_S∈·)·P(ω′|_{S^c}∈·)` recombines to the law of `ω`.

  Moreover `S_A(ω*) = S_A(ω)` and `ξ_A(ω*) = ξ_A(ω)`. If `S_B(ω′) ∩ S_A(ω) = ∅`, then `ω* = ω′` on `S_B(ω′)`, so `ξ_B(ω*) = ξ_B(ω′)`. Therefore:
  - `E f g = E f(ξ_A(ω)) g(ξ_B(ω*))`;
  - `E f · E g = E f(ξ_A(ω)) g(ξ_B(ω′))`;
  - the two integrands differ only on `{S_A(ω) ∩ S_B(ω′) ≠ ∅}`.

  By independence, that probability is at most `Σ_z P(z∈S_A)P(z∈S_B)`. Also `z ∈ S_x` implies an ancestor within distance 1 of `z`, hence `L(x) ≥ |z−x|−1`.

  For the asymptotic, write `k_1 = |z−x|` and `k_2 = |z−y|`, so `k_1 + k_2 = s ≥ r`. Then `a(k_1−1)a(k_2−1) ≤ D^2 (2(D−1))^{s} s/s!`, using `k_1! k_2! ≥ s!/2^s`, plus the boundary cases `k_i ≤ 1`, which are smaller. The number of `z` with `k_1 + k_2 = s` is at most `(2s+1)^d` for nearest-neighbour `N_0`, and at most `(2hs+1)^d` for a general finite `N_0` of ℓ∞-range `h`. The asymptotic is unchanged. Summing over `s ≥ r` gives `≤ C_d r^{d+1}(2e(D−1)/r)^r` for `r ≥ 4e(D−1)`.
- **(B3).** Two-set mixing follows from (B2) applied to cylinder functions, approximating general `L^2` functions. Mixing of all orders uses the import cited above, or the k-set version of the coupling. A unique and therefore invariant law that is mixing cannot be a non-trivial mixture of symmetry-related phases. ∎

## 4. Theorem C: state-dependent covariant rates (new content (a))

**Model.** The rate is a measurable `λ_x(η)` of the formed neighbourhood `η` of `x` (contents included), with `0 < λmin ≤ λ_x(η) ≤ λmax < ∞`, and `κ := λmax/λmin`. The content at formation is `Φ_x(η, U)`. The intended process is the Markov birth process with generator

`(𝓛f)(ρ) = Σ_{x blank} λ_x(η_x(ρ)) Σ_s r_x(s|η_x(ρ)) [f(ρ^{x→s}) − f(ρ)]`.

This includes the generator of 09-07 (constant `λ`) and the 09-22 rate laws.

**Graphical construction.** Independently for each `x`, take a Poisson process `Π_x` of rate `λmax` on `(0,∞)`, with iid marks `(V,U)` uniform on `[0,1]^2`. At a point `(x,t,V,U)` with `x` blank at `t−`, `x` forms iff `V ≤ λ_x(η_x(t−))/λmax`, with content `Φ_x(η_x(t−), U)`.

- A point is *sure* if `V ≤ λmin/λmax`. Let `σ_x` be the first sure point; `σ_x ~ Exp(λmin)`, independently over `x`.
- A sure point is always accepted, so the formation time satisfies `τ_x ≤ σ_x`. The points of `x` after `τ_x` are inert.
- The *relevant points* of `x` are the points of `Π_x ∩ (0, σ_x]`.
- A *backward chain* of length `n` from `x` is a sequence `(y_k, t_k)_{k=0..n}` with `y_0 = x`, `y_k ∈ N(y_{k−1})`, `t_0 > t_1 > … > t_n`, and each `t_k` a relevant point of `y_k`. The *reach* `C(x)` is the set of sites `y_n` over all backward chains, and `ρ(x) := max_{y∈C(x)} |y−x|`.

**Theorem C.**

- **(C1)** For a fixed SAW `(y_0, …, y_n)` with distinct sites, the expected number of backward chains along it is exactly `κ^{n+1}/(n+1)!`. Hence
  `E[# distinct-site backward chains of length n from x] = c_n κ^{n+1}/(n+1)! ≤ D(D−1)^{n−1}κ^{n+1}/(n+1)!`.
- **(C2)** (Loop erasure.) If a backward chain from `x` ends at `(y,s)`, then a backward chain with pairwise distinct sites ends at `(y,s)`.
- **(C3)** `P(ρ(x) ≥ n) ≤ D(D−1)^{n−1}κ^{n+1}/(n+1)!`. A.s. `C(x)` is finite for every `x`, and the graphical rules determine a unique trajectory. Every site forms at the finite time `τ_x ≤ σ_x`. The final record field `ξ = ξ_∞` is a finitary factor of the iid marked-Poisson field, with coding radius at most `ρ(x)+1`. So
  `P(R(x) ≥ n+1) ≤ D(D−1)^{n−1}κ^{n+1}/(n+1)!`.
  The same holds for the configuration at any fixed time `t`.
- **(C4)** Theorem B and the stationarity and symmetry parts of A4 hold with `a(k)` replaced by `a_κ(k) := min(1, D(D−1)^{k−1}κ^{k+1}/(k+1)!)`. The last sentence of A4 (the law does not depend on the clock law) does **not** carry over: under rate modulation the record law depends on `λ`. Correlations still decay superexponentially for every finite `κ`. The bounds become effective beyond the scale `r ≈ 2e(D−1)κ`; for example, the half-distance bound needs `r ≳ 2e(D−1)κ`.
- **(C5)** The trajectory is a version of the Markov process with generator `𝓛`. Each blank site with condition `η` forms at rate `λmax·(λ(η)/λmax) = λ(η)`, with content law `r(·|η)`.

**Claim types.** (C1)–(C4) are PROVED. The construction is checked independently against an exact finite law in s2(c), and against forward simulation in s2(d). (C5) is PROVED at the level of the graphical representation. That it coincides with the Liggett/Harris Feller semigroup is standard for bounded, finite-range rates (IMPORTED: Liggett 1985, Ch. I).

**Proof.**
- **(C1).** The sites are distinct, so the `Π_{y_k}` are independent. By the Mecke/Slivnyak formula, the intensity of relevant points of one site at time `t` is `λmax · P(no sure point of Π in (0,t)) = λmax e^{−λmin t}`. Hence the expected count is

  `∫_{t_0>…>t_n>0} Π_k λmax e^{−λmin t_k} dt = κ^{n+1} P(Z_0 > … > Z_n) = κ^{n+1}/(n+1)!`, with `Z_k` iid `Exp(λmin)`.

  This is checked symbolically for `n ≤ 4` in s2(a), and by Monte Carlo in s2(b).
- **(C2).** Take a chain ending at `(y,s)` with the fewest steps. Suppose `y_j = y_k` with `j < k`. The sequence `(y_0,t_0), …, (y_{j−1},t_{j−1}), (y_k,t_k), …, (y_n,t_n)` is again a backward chain:
  - `y_k = y_j ∈ N(y_{j−1})`;
  - `t_k < t_j < t_{j−1}`;
  - relevance is a property of the point;
  - if `j = 0`, then `(y_k,t_k)` is itself a relevant point of `x`.

  This chain is shorter, which is a contradiction.
- **(C3).** If `ρ(x) ≥ n`, then by (C2) there is a distinct-site chain to a site at distance `≥ n`. Its length is `≥ n`, and truncating it gives a distinct-site chain of length exactly `n`. Apply Markov's inequality with (C1), and let `n → ∞`.

  *Determinacy.* The state of `y` at `t−` is decided by the relevant points of `y` before `t` and their acceptance and content decisions. Each decision at a point `s` needs the states of the neighbours at `s−`. A neighbour `z` with no relevant point before `s` is blank at `s−`, because its formation point would be relevant. So computing the whole history of `x` visits only points of the reach. These are finitely many, since each site has a geometric number of relevant points. They are evaluated in increasing time order, and induction gives uniqueness.

  The data read are the marked processes on `C(x) ∪ ∂C(x)`; boundary sites are read to confirm they have no earlier relevant point. So `R(x) ≤ ρ(x)+1`. The exploration is a stopping set, and (C4) repeats the proof of B2. ∎

**Where the hypotheses bite.**
- The factorial comes from requiring each relevant point at time `t` to have survived the sure-point cutoff, which costs `e^{−λmin t}`. With `λmin = 0` there is no cutoff, and this argument says nothing.
- With `λmax = ∞` the thinning fails, and the "process" may be ill-defined: it can avalanche with no first event.
- No *threshold* in `κ` appears. The earlier site-level reduction, which drops the time ordering, gives only exponential bounds needing `(D−1)κ`-type smallness. The time ordering of the chain restores the factorial.

## 5. Theorem D: finite-range-correlated clocks

**Theorem D.** Let `T_x = g(ζ|_{x+K})`, with `ζ` iid, `K` finite and `b := |K−K|`. Let the marks be iid and independent of `ζ`, and use the strict-earlier convention.

- A fixed SAW of `n` edges is strictly decreasing with probability at most `1/⌈(n+1)/b⌉!`.
- Hence `P(L(x) ≥ n) ≤ D(D−1)^{n−1}/⌈(n+1)/b⌉!`, and `ξ` is a finitary factor of `(ζ, U)`, with coding radius at most `L(x) + 1 + max_{k∈K}|k|`.
- Theorem B holds with this tail.

(PROVED. EXACT-CHECK for `T_x = max(ζ_x, ζ_{x+1})` with `n ≤ 7`; the exact values are `2/(n+2)!`. NUMERICAL for a sum clock on four Z^2 path shapes.)

*Proof.* Walk along the path and greedily keep a site, then discard the at most `b−1` later path sites `y` with `y − x ∈ K − K`. This keeps `k ≥ ⌈(n+1)/b⌉` sites whose windows `x+K` are pairwise disjoint. Their clocks are therefore iid. A strictly decreasing path makes the kept subsequence strictly decreasing, which has probability at most `1/k!`. The rest is as in Theorems A and B. ∎

## 6. Theorem F: ordered witnesses with infinite-range clocks (counterexample family, part (a))

**Imported premise (I-16).** This is the 2026-09-16 note, Theorem T7: the six-axis product rule on Z^3 with weights `(p,1,2)`, `p ≥ 285718`, in level order `τ(x) = x_1+x_2+x_3`. The level automaton has six distinct translation-invariant invariant laws `ν_a`, `a ∈ {±e_i}`, each with `P(v_x ≠ a) ≤ 3/10^5`.

A stationary invariant law of the probabilistic cellular automaton extends, by Kolmogorov, to a `Z^3`-translation-invariant record field `N_a`. A shift by `e_1` advances the level, and an in-plane shift composes with it. The bound is preserved because Cesàro limits keep closed conditions.

**Theorem F (CONDITIONAL on I-16).** Let `g` be uniform on the cubic group `O_h`, so `w = g(1,1,1)` is uniform on the 8 body diagonals. Use the clock `T_x = ⟨w, x⟩` (with the ancestry run from the infinite past), and let `W := (1/48) Σ_{g∈O_h} g_* N_{e_1}`. Then:

- `W` is a record field for the covariant six-axis rule;
- it is invariant under translations and under `O_h`;
- its clock is covariant in law **only up to a global time shift**, i.e. as an order relation. As a real-valued field it is not translation-invariant (`T_0 ≡ 0`);
- the record is **not** a function of the clock and the marks: the phase `g e_1` is extra randomness, coupled to the clock direction (`⟨g e_1, w⟩ = +1` always);
- for `b = e_1` and every `x`,
  `Cov_W(1{v_0=b}, 1{v_x=b}) ≥ (1/6)(1 − 6·10^{−5}) − 1/36 = 124991/900000 > 0.1388`.

*Proof.* The rule depends only on whether `v' = v`, `v' = −v` or `v' ⊥ v`, so it is `O_h`-invariant. Hence `g_*N_a` is the level-order field for the diagonal `g(1,1,1)`.
- By symmetry, `E_W 1{v=b} = 1/6`.
- The components with `g e_1 = e_1` are 8 of 48. In each of them both sites equal `b` with probability `≥ 1 − 2·3·10^{−5}`.
- Drop the other components, which contribute `≥ 0`. ∎

**Remarks.**
- `W` is non-ergodic: it is a mixture.
- Its clock has perfect infinite-range correlation, and `P(L ≥ n) = 1` for every `n`; see s3(e).
- No ergodic covariant witness is claimed (OPEN). See §1: for non-ergodic laws, covariance-LRO only signals a non-trivial mixture.
- No covariant counterexample exists inside the classes of Theorems A, A′, C and D. That is a theorem, not a failed search.

**What F does and does not show.** Covariance-LRO of a non-ergodic mixture is automatic once the components have different one-site marginals; witness W-tie below has it with FFIID components. So the inequality above is not itself the content. The content is that `W` is a covariant-in-law (modulo time shift) record field whose ergodic components are the **non-unique** coexisting level-order phases of I-16. Uniqueness given the data fails there, which never happens in the classes of G-I.

**Recorded witness W-tie (reviewer F1; EXACT-CHECK s3(f), and the reviewer's r4).**
- *Clock:* with probability ½ every `T_x = ½`; with probability ½ the `T_x` are iid U[0,1].
- *Rule on Z:* content 0 if no neighbour is strictly earlier, content 1 otherwise. The zero `r(·|∅) = δ_0` is allowed.

The clock field is exchangeable and pairwise uncorrelated, and it is translation- and reflection-covariant in law on Z. (The same construction on Z^d with the nearest-neighbour rule is exchangeable and hence covariant under every lattice automorphism, O_h included. Only the Z version is checked.) Yet `E ξ = 1/3`, `E ξ_0 ξ_r = 2/9` and `Cov(ξ_0, ξ_r) = 1/9` for every `r ≥ 3`. This is covariance-LRO, again of the non-ergodic-mixture kind. It shows that the hypothesis "tie-free" in A′ cannot be dropped.

## 7. Theorem G: a three-regime classification (not exhaustive) and a necessary clock property (part (b))

Fix `d`, a finite menu, a finite-range rule (covariant or not), and selector marks iid and independent of the clocks.

**(G-I) Clock classes with finite ancestry tails force a trivial record phase. PROVED.** This class contains:
- iid clocks of any law (A);
- exchangeable tie-free clocks (A′);
- finite-range factors of iid (D);
- Markov covariant rates with `0 < λmin ≤ λ ≤ λmax < ∞` (C).

In each case the record law is unique given the data. It is FFIID, with coding-radius tail at most `D(D−1)^{n−1}κ^{n+1}/(n+1)!` (κ=1 for A and A′) or `D(D−1)^{n−1}/⌈(n+1)/b⌉!`. Local correlations decay superexponentially. There is no long-range order, no SSB of any rule symmetry, and no power-law or Coulomb correlation of local observables.

**(G-II) Directed infinite-range clock: ordered phase. ON-MAIN (I-16).** The level order on Z^3 is translation-covariant up to a time shift but breaks `O_h`, and it has six ordered phases.

**(G-III) Covariant-in-law infinite-range clock: ordered, non-ergodic phase. CONDITIONAL on I-16 (Theorem F).**

**Necessity corollary (PROVED from G-I).** Suppose a record law under the stated rule class has covariance-LRO (§1), SSB, or local correlations that are not `O(exp(−c r ln r))`. Then its clock data lie outside every class in G-I. Concretely, it needs **one** of:
- (i) clock **dependence** of infinite range, not reducible to a finite-range factor of iid or to a **tie-free** exchangeable family. Examples: the level clock, and the exchangeable clocks with ties of W-tie;
- (ii) a non-trivial mixture of clock laws that induce different record laws. This is a special case of (i), listed for clarity; W-tie and `W` are examples;
- (iii) a degenerate rate ratio, `λmin = 0` or `λmax = ∞`;
- (iv) a non-Markov, history-dependent rate law outside Theorem C.

Items (iii) and (iv) are not tested here and are listed only as gaps in scope. This list is a restatement of "outside G-I". It is **not** a claim that every clock in (i)–(iv) orders, and the three regimes G-I, G-II and G-III are not exhaustive.

**Explicitly outside the claim (OPEN).**
- Ergodic covariant clocks with long-range but decaying correlations, for example stationary power-law-correlated Gaussian time fields.
- FFIID clocks with heavy-tailed coding radius.
- Rate laws with `λmin = 0` from a translation-invariant start, such as jamming or nucleation-free growth. Example: cooperative sequential adsorption (CSA) with zero isolated rate. Note that random sequential adsorption (RSA)-type exclusion with `λ = 0` reduces to one clock per site and is FFIID by Penrose–Sudbury.
- Percolation transitions of non-local cluster observables. These occur already in class G-I (10-08 note).

## 8. Corollary vs new; novelty

| Item | Status |
|---|---|
| Finite ancestors, existence and uniqueness, `6·5^{n−1}/(n+1)!` (d=3) | ON-MAIN (09-07, 10-08); generalised to `c_n`, general `D`, clocks with atoms |
| FFIID and coding radius; correction of the map constant `R` vs `L` | new statement; elementary corollary |
| Covariance bounds B1 and B2; no long-range order, SSB or Coulomb for **all** finite-range rules with iid clocks | new in repo. The 10-16 note proved the stronger 1-dependence only for order-blind positive rules. |
| Theorem C (bounded-ratio state-dependent rates, all κ) | new in repo; real content of (a) |
| A′ and D (exchangeable, finite-range-correlated clocks) | new in repo; elementary |
| F, W-tie and G (covariant-in-law witnesses; three-regime classification, not exhaustive) | assembled; F conditional on I-16; W-tie exact |

**Literature.**
- Decreasing-path ancestry is Penrose–Sudbury (Ann. Appl. Probab. 15 (2005), arXiv math/0503519).
- Stabilization for RSA and cooperative sequential adsorption: Penrose–Yukich (AAP 12 (2002)); Penrose, "Random parking, sequential adsorption and the jamming limit" (CMP 2001); Penrose, "Limit theorems for monotonic particle systems and sequential deposition" (SPA 98 (2002) 175–197); Penrose, Probability Surveys 5 (2008).
- The stopping-set / disagreement coupling of B2 is the van den Berg–Maes / van den Berg–Steif style.
- FFIID theory: Holroyd, Schramm and Wilson; Spinka.

I did not read the full text of Penrose (2002). Its "monotonic particle systems" framework very plausibly already contains a Theorem-C-type stabilization for bounded-ratio cooperative adsorption. **No novelty is claimed for the probabilistic method or for Theorem C in substance.** The repo-specific content is the following:
- the explicit factorial constants with `κ`;
- the rule-independence over arbitrary finite menus and selectors;
- the corrected coding-radius constant;
- the application to record-phase existence (OBL-R2.2);
- the three-regime classification (not exhaustive) with the covariant-in-law witnesses.

## 9. No-Go Discipline Gate (N1–N8)

The negative claim is G-I: no long-range order, SSB or power-law local correlations for the quantified clock classes. It is a proved theorem on an explicitly quantified family, not an impossibility for "covariant formation" in general.

**N1, routes that might evade the no-go, five distinct ones.**
1. Neighbour-dependent rates, attempting order by rate modulation. ATTEMPTED, closed by Theorem C for every κ.
2. Correlated covariant clocks of finite range. ATTEMPTED, closed by Theorem D.
3. Tie-free exchangeable or "random global speed" clocks. ATTEMPTED, closed by A′. With ties allowed, the route is not closed (W-tie).
4. Clocks with atoms, i.e. synchronous partial updates. ATTEMPTED, closed by the strict-decrease bound in A2.
5. Infinite-range clocks, and exchangeable clocks with ties. ATTEMPTED and **not closed**: they do give order (F, W-tie). This is outside the claimed domain, and the claim is narrowed to exclude it.
6. Rules with zeros or site dependence. Closed: A–D never use positivity or covariance for the bounds.
7. `λmin = 0`. Not closed; listed as OPEN.

**N2, wall independence.** There are two escape conditions: infinite-range clock dependence, and degenerate rate ratio. They are not shown independent. An RSA-type `λ=0` rule reduces to an iid clock, so degeneracy does not imply escape. Their relation is recorded as unresolved.

**N3, hidden walls.** These are explicit premises:
- the selector marks are iid and independent of the clocks;
- the rule has finite range;
- the rule is normalised on every condition, so formation always succeeds and holes are excluded;
- in C the rate is Markov.

"Standard" is used only for the Liggett/Harris semigroup identification (C5), which is IMPORTED and not load-bearing for the record-law conclusions.

**N4, residual matching.**
- I-16 attacks "does any formation reading order?", which matches G-II/G-III.
- The 10-16 note covers only order-blind positive rules. It is used only for comparison, not as a witness.
- The 10-08 percolation result is used only to delimit the scope, for non-local criticality.

**N5, resolution.** The negative statement is for *local observables*: finite-support functions and their two-point and higher truncated correlations. It is explicitly **not** asserted for non-local cluster or percolation observables, which do have critical points (10-08). It is also not asserted for finite but large correlation lengths, which can be about `e(D−1)κ`.

**N6, partial closure.** Adopting a covariant-in-law level clock (F) closes "order exists", but at the price of an infinite-range clock premise. No convention-level closure exists.

**N7, steelman.** "Theorem F shows covariance does not forbid order. An *ergodic* covariant clock could order, for instance a long-range-correlated Gaussian time field whose decreasing paths have heavy tails. So the classification's class boundary is not sharp."
- *Answer:* this is correct, and it is recorded as OPEN. The theorem claims necessity of leaving the G-I classes, not sufficiency of any particular infinite-range clock.

**N8, cross-cycle echo.**
- The map's own caveat ("part (1) is close to a corollary") is confirmed.
- The 10-16 "no Coulomb" conclusion is extended from order-blind positive rules to all finite-range rules under iid or local clocks. It is weakened from 1-dependence to superexponential decay.

## 10. Load-bearing step for independent check

1. **Theorem C.**
   - The relevance cutoff (formation point ≤ σ_x; points after formation are inert).
   - The "blank-boundary" inference in the determinacy argument.
   - The Mecke intensity `λmax e^{−λmin t}` in (C1).
   - The loop-erasure lemma (C2), which is where the factorial survives revisits.
2. **The stopping-set resampling in B2** (`ω*` has the law of `ω`).
3. **The XOR exact certificate** that falsifies the map's `R`-constant. The script uses blank-exterior window extensions (s1(d)), and its correctness depends on those being admissible extensions, i.e. exterior clocks later than the window.

## 11. Files

- `scripts/c3_common.py`
- `scripts/s1_iid_paths_and_coding_radius.py` (exact Z^1 path tails; SAW counts; Monte Carlo for Z^2 and Z^3; XOR coding radius)
- `scripts/s2_rate_modulated.py` (symbolic C1; Monte Carlo chain counts; exact 4-cycle jump-chain law vs graphical construction; backward coding map vs forward ring simulation; reach tail; covariance observation)
- `scripts/s3_correlated_clocks_and_witness.py` (Theorem D exact and Monte Carlo; B2 bound vs Monte Carlo; F arithmetic; level-clock tail; W-tie exact)
- `scripts/run_all.sh` → `logs/run_all.log` (`TOTAL: PASS=59 FAIL=0`); per-script outputs in `logs/*.out`.

## 12. Review dispositions (REVIEW.md, F1–F8)

| Finding | Disposition |
|---|---|
| F1: the necessity list is false as worded (tie counterexample) | (i) is restricted to *tie-free* exchangeable clocks, and "correlation" is replaced by "dependence" in §0 item 4, the title and G. Mixtures are added as (ii). The counterexample is recorded as witness W-tie (§6) and checked exactly in s3(f). The run total is now 59 PASS. N1 route 5 is updated. |
| F2: F's LRO is the automatic non-ergodic-mixture kind | F is restated as non-uniqueness and phase coexistence inherited from I-16. Automatic mixture-LRO is noted, and the §1 LRO notion is restricted to ergodic laws (remark in §6). |
| F3: covariance only up to time shift; the phase is extra randomness | Added to the statement of Theorem F and to §0 item 4. |
| F4: the "trichotomy" overstates | Retitled as a "three-regime classification (not exhaustive)". The title and §0 item 4 are qualified "within bounded-rate Markov clocks". G-I is renamed "clock classes with finite ancestry tails". The open options (iii) and (iv) are kept. |
| F5: the status line | Updated in the header. |
| F6: A1/A2 claim types | ON-MAIN only for Exp clocks with D=6; the general version is COROLLARY (§2). |
| F7: B2 count for general N_0; mixing of all orders | The `(2hs+1)^d` count is added. Mixing of all orders now cites the factor-of-iid property, or the k-set coupling. |
| F8: C4 "A4 verbatim" | Changed to "the stationarity and symmetry parts of A4"; the clock-law-independence of A4 is explicitly excluded. |
| B1 remark (the Stirling form holds for all r) | Noted in B1. |
| Confirmation nits (end of REVIEW.md) | §1 now defines covariance-LRO for any law, with genuine LRO reserved for ergodic laws. This is consistent with the §6 remark and the non-ergodic examples in G. W-tie is moved after Theorem F's proof and remarks. N1 route 3 now says "tie-free", and N2 says "dependence". W-tie is called translation/reflection-covariant on Z, with the Z^d version noted. The status line is updated. |
