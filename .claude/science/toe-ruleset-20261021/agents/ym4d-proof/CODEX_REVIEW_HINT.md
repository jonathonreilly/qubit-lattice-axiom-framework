# PRE-STATED

UTC: 2026-10-29 00:09:20 UTC. Independent hostile review of `HINT55.md`, with the user prompt (including its summaries of the claims) as prior exposure. These criteria are recorded before reading the target or its check implementations. Only this review file will be written; no git commands will be used. Arithmetic will be exact rational or symbolic. Unverified literature recollections, if needed, will be marked `[m]`.

A refutation will be an explicit counterexample satisfying the quantified hypotheses, an exact sign/normalization/threshold contradiction, or a logically invalid claimed implication with a demonstrated missing premise. A check failing outside its stated domain is not a refutation. Missing evidence, an unproved analytic estimate, or inability to identify a continuum observable is `NOT-VERIFIED`, not by itself `REFUTED`.

Specific attacks: (1) a free comparator with the claimed witness, especially an allowed contact term or observable-map ambiguity; (2) misuse of a positive two-point spectral representation to control the one-point expectation of a nonlinear flowed composite; (3) a failure of uniformity, order of limits, or uniform integrability in passing from cutoff observables to a limiting state; (4) an exact failure of the free coefficient or H-RED threshold for admitted constants; (5) a failure of a soft-noise implication for the actual blocking kernel; (6) check gates that merely restate an input, omit a necessary control, or rely on inexact arithmetic.

Verdicts will be `CONFIRMED`, `NOT-VERIFIED`, or `REFUTED`, each with source file and locating string. Conditional algebra will be distinguished from verification of its physical premises. The final section will state exactly what may be banked.

## Scope and disposition

Review date: 2026-10-29 UTC. `L` below means `.claude/science/toe-ruleset-20261021/agents/ym4d-proof`; `E` means its sibling `ym4d-existence`. Locations are file plus searchable string; line numbers are supplementary. I read all 603 lines of `L/HINT55.md` in ranges, all `hi55_a/b/c` criteria, implementations and result logs, and the cited dependency ranges identified below. I did not re-prove the upstream construction, F-tune's analytic hypotheses, or OS0–OS3. No git was used. No source/check files were edited. Local review-loop instructions were used only within this review-file scope; current-main provenance was not checked because git was forbidden.

**Overall: NOT-VERIFIED as a proof of a non-free reconstructed Yang–Mills theory. CONFIRMED as a useful conditional separation theorem for the explicitly prescribed quadratic abelian realization.** The crucial KL calculation is sound in that realization. The main failures of transfer are the substitution of a bounded nonlinear block observable for that quadratic realization, the unproved identification with reconstructed observables, and the missing nonlinear noise-subtraction estimate. Actual Yang–Mills lower/upper bounds remain inputs.

| Claim and location | Verdict | Exact scope |
|---|---|---|
| `HINT55.md`, `Lemma TR`, `(2.1)`, `Lemma SI` | **CONFIRMED** | Tensor, heat-smearing and scale-invariance identities; finite expectations where a difference is taken |
| `HINT55.md`, `Theorem KLM`, `Lemma UV-D`, `Theorem SEP` | **CONFIRMED** | Defined quadratic realizations of `𝔊₀ ∪ 𝔊₁`, the defined `𝔖`, and measurable probability mixtures |
| `HINT55.md`, `Proposition CT` | **CONFIRMED** | A finite family of these scale differences does not exclude free Maxwell contact representatives |
| `HINT55.md`, `Theorem H-RED`, `Theorem H-RED′`, `Theorem H-RED-sharp` | **CONFIRMED** | Conditional inequalities, with their stated domain and convergence assumptions; not verification of those assumptions |
| `HINT55.md`, `Branch D`, `(S4c-lin)`, `survives the OS quotient` | **NOT-VERIFIED** | The actual bounded block/OS observable identification is missing; linearization alone is insufficient |
| `HINT55.md`, `(NOISE-ADD)`, `(ANTI-♭)`, `(W-AF2_r)` | **NOT-VERIFIED** | Nonlinear inputs and the proposed subtraction route |
| `HINT55.md`, `Lemma NA-lin`, `Kernel check for (KER-fwd)` | **CONFIRMED** | Linear variance identity; exact independent multiplicative noise fails for the stated kernel |
| `HINT55.md`, `(N1) Constant normalisations cannot` | **REFUTED** | Unequal colour rescalings need not preserve the class as it is defined by a *summed* covariance |

## 1. What the comparator calculation actually proves

**CONFIRMED — `HINT55.md`, `(2.1)` and `Theorem KLM`.** This is not an application of the KL representation of the composite `E`. For the comparator, the definition is expressly

\[
\mathcal E(t,0)=\frac{t^2}{4}\sum_{a,\mu,\nu}(K_t*F^a_{\mu\nu})(0)^2.
\]

Its expectation therefore uses only the *linear field-strength* two-point function, even if the law of `F` is non-Gaussian. Tracing the tensor gives `2(d−1)p²`, hence in four dimensions

\[
f(t)=\frac{3}{32\pi^2}\int_0^\infty v e^{-2v}h(v/t)\,dv,
\qquad h(u)=u\widehat s(u).
\]

For `ŝ(u)=∫ρ(ds)/(u+s)+p₀`, `ρ≥0`, `p₀≥0`,

\[
h'(u)=\int\frac{s\,\rho(ds)}{(u+s)^2}+p_0\ge0
\]

where differentiating can instead be replaced by the pointwise difference inequality. Thus `f` is non-increasing in `t`, and `f(t₂)−f(t₁)≤0` for `t₁<t₂`. A positive-mass spectral component makes the inequality strict when it couples to the observable. The change of variables for a general self-similar quadratic smearing is also correct. No Wick factorization is required.

**NOT-VERIFIED as an inference from composite positivity — same locations; `HINT55.md`, §1.2 `realising the symbols`.** The positivity of the spectral measure of a gauge-invariant composite `E` concerns `⟨E(x)E(y)⟩`; it does not determine `⟨E(t)⟩` for a nonlinear flow. Nonabelian `G(t)` includes commutators and nonlinear flow terms. There is no corresponding derivation of (2.1) from the two-point function of `E`. The note correctly avoids that mistake inside its explicit comparator definition; it must not promote that definition to an identification theorem about every free realization of the reconstructed observable algebra.

An explicit illustration of the distinction: for a free massive scalar with covariance `1/(p²+M²)`, the positive quadratic observable `E_M(t)=M²(K_t*φ)^2` has

\[
t^2\langle E_M(t)\rangle
=\frac{M^2t}{16\pi^2}\int_0^\infty\frac{v e^{-2v}}{v+M^2t}\,dv>0,
\qquad \lim_{t\downarrow0}t^2\langle E_M(t)\rangle=0.
\]

This is a free theory with an AF-W-type one-point inequality for a different composite. It is **not** a counterexample to SEP's specified Maxwell-field realization. It shows why excluding that realization is not automatically exclusion of every free theory under every possible composite-operator identification.

**CONFIRMED — `HINT55.md`, `Lemma SI`.** Scale invariance of the specified dimensionless energy field implies constant `f`, including canonical Maxwell fields at arbitrary fixed colour couplings and probability mixtures with finite first energy moment. For a mixture whose relevant expectations are infinite, `∞−∞` is not a witness; SEP's finite-UV hypothesis handles the necessary integrability instead.

**CONFIRMED — `HINT55.md`, `Proposition CT`.** Direct integration gives, with `C=3e²/(32π²)`,

\[
f_\varepsilon(t)=C\left(\frac14-\frac{\varepsilon}{4t}+\frac{3\varepsilon^2}{8t^2}\right),
\qquad
f'_\varepsilon(t)=\frac{C\varepsilon}{4t^2}\left(1-\frac{3\varepsilon}{t}\right).
\]

Positivity is certified by `ŝ(u)−e²ε=e²(1−εu)²/u`. The polynomial covariance terms vanish in reflected pairings of linear test fields supported in opposite open half-spaces. Gaussian reconstruction then has the same one-particle space and Fock theory as the canonical Maxwell field, with the appropriate Wick-ordering identification. The flowed quadratic expectations need not coincide. For `ε=1`, the normalized differences are exactly `7/512` at `(4,8)` and `−7/8` at `(1/2,1)`. Choosing `3ε` below all the finitely many finer times makes every prescribed difference positive; increasing `e²` also meets any finitely prescribed positive margins. The divergence at `t↓0` defeats the infinite family. This is a real, correctly repaired counterexample to the single-scale proposal.

**CONFIRMED — `HINT55.md`, `Lemma UV-D` and `Theorem SEP`.** I checked both subtraction cases. In `𝔊₀` the Stieltjes part tends to zero at large `u`; positivity forces a nonnegative constant polynomial or a positive leading coefficient. A degree-`d≥1` contact polynomial produces heat-energy growth of order `t^{−d−1}`. In `𝔊₁`, `S₁(u)→−∞` and `S₁(u)/u→0`; positivity therefore requires a polynomial of degree at least one with positive leading coefficient. These facts prove the asserted divergence alternative. Finite UV liminf forces `p₀=0` and finite total spectral mass in the remaining case.

Fatou is used in the correct direction: along a sequence realizing the mixture's finite UV liminf, `∫liminf f_α≤liminf∫f_α<∞`. Divergent components consequently have zero mixing measure. Almost every remaining component is non-increasing or constant, so its finite-scale value is bounded by the selected UV values. Integration proves SEP. Arbitrary mixtures are covered; no uniform bound on the individual spectral masses and no clustering assumption are needed.

## 2. Comparator coverage, normalization and the block/OS bridge

**NOT-VERIFIED — `HINT55.md`, §1.3 `RP + O(4) + Bianchi`, §2.9 `What "free comparator" must mean for SU(N)`, §8.2 `no free abelian theory`.** The representation theorem is explicitly imported, without a source or a proved tensor/contact classification here. SEP itself does not need that import. Its bankable domain is the displayed covariance class, not all OS theories or all possible choices of gauge-invariant generators.

The cutoff at one subtraction is a genuine restriction, not a completeness theorem. For example, the exact positive twice-subtracted scalar factor

\[
\begin{aligned}
S_2(u)&=\int_1^\infty s\left[\frac1{u+s}-\frac1{1+s}+\frac{u-1}{(1+s)^2}\right]ds\\
&=(u-1)^2\int_1^\infty\frac{s\,ds}{(u+s)(1+s)^2}
=u\log\frac{u+1}{2}-\frac{u-1}{2}\ge0
\end{aligned}
\]

defines a tempered positive Gaussian covariance `T^I S₂`. Its reflected form is the positive massive-field spectral integral; the subtraction polynomials vanish across the reflection plane. It is thus a generalized-free abelian comparator with `ρ(ds)=1_[1,∞)(s)s ds`. It is outside `𝔊`: `S₂(u)~u log u`, whereas the `𝔊₀` remainder decays and the `𝔊₁` remainder is `o(u)` after removing a polynomial. This example's quadratic heat energy diverges, so it does **not** refute AF-W separation. It does refute unqualified completeness of `𝔊`. Higher-subtraction comparators require an additional theorem or an explicit restriction of the advertised conclusion. General tensor contact terms or different free-field/composite identifications likewise cannot simply be declared covered by (1.1).

**REFUTED — `HINT55.md`, `(N1) Constant normalisations cannot`.** The class constrains only `Σ_a⟨F^aF^a⟩`. Take independent Gaussian colours with

\[
\widehat s_1(u)=\frac1{u(1+u)},\qquad
\widehat s_2(u)=\frac1{1+u},\qquad
\widehat s_a=0\quad(a\ge3).
\]

Both are positive Euclidean covariances of the stated tensor form and their sum is `1/u`; hence the law is in the *defined* `𝔊₀`. Rescale colour 1 by `1` and colour 2 by `1/2`. The new summed factor satisfies

\[
h_{\rm new}(u)=\frac14+\frac{3}{4(1+u)}.
\]

Its heat energy is strictly increasing in `t`, with finite UV value `3/(512π²)` and larger value at every `t>0`. By the confirmed UV-D/SEP theorem, the rescaled law is not in `𝔊`. All rescalings used are nonzero. The example uses the deliberately enlarged class: it need not be reflection positive colour by colour. Requiring the relevant spectral property for each colour (or every positive colour contraction) repairs N1. A common positive scalar normalization preserves AF-W, and arbitrary colour couplings of genuine canonical independent Maxwell fields remain covered.

**NOT-VERIFIED — `HINT55.md`, §4.4 `(S4c-lin)`, §6 row `Theorem X-NTAF`, §8.3 `a linear-algebra statement`.** The proposed bridge is substantially stronger than convergence of a derivative at the trivial field. The actual `Ψ_m=‖log V_p‖²_HS` satisfies `0≤Ψ_m≤Nπ²`. A nondegenerate Gaussian quadratic flux `Σ_aF^a(φ_m)^2` is unbounded. They cannot have the same law at fixed resolution and nonzero coupling just because the block map has the asserted linearization. In `E/EXISTENCE.md`, locating `X-S4c`, the actual map contains a nonlinear log cutoff `λ`, exponentiation, and iteration. Those operations are not removed by the stated linearization hypothesis.

There is an exact obstruction to inferring the comparator theorem for bounded blocks from linearization alone. Let `ξ_ν` be a translation- and O(4)-invariant vector-valued compound Poisson white noise of intensity `λ>0`, with independent centred Gaussian vector marks of covariance `δ_νρ`. Put `F=dξ`, in one colour. Then

\[
\langle\widehat F_{\mu\nu}\widehat F^*_{\rho\sigma}\rangle
=\lambda T^I_{\mu\nu,\rho\sigma},
\]

so this is a non-Gaussian member of `𝔊₀` with `ρ=0`, `P=λ`. It obeys Bianchi. Disjoint open half-spaces depend on independent Poisson increments; reflection invariance makes the OS form `\overline{\mathbb E A}\mathbb E B`. Its reconstructed Hilbert space is the vacuum space.

Choose a real compactly supported smooth antisymmetric test tensor `φ` with `∂_μφ_μν` nonzero, and `X_s=F(φ_s)`, `φ_s(x)=s^{-2}φ(x/s)`. Its variance is a positive constant times `λs^{-2}`. In contrast, the compact plaquette and principal-log energies

\[
B_s=2(1-\cos X_s),\qquad
\Psi_s=2\,\operatorname{dist}(X_s,2\pi\mathbb Z)^2
\]

are zero if there is no Poisson point in the support of `φ_s`. Consequently, for a fixed compact support set `C`,

\[
0<\mathbb E B_{s_0},\quad 0<\mathbb E\Psi_{s_0},\qquad
\mathbb E B_s\le4\lambda |C|s^4,\quad
\mathbb E\Psi_s\le2\pi^2\lambda |C|s^4\longrightarrow0.
\]

Strict positivity at `s₀>0` follows on the event of one point in an open set where the derivative test is nonzero, using the continuous nondegenerate marks. These are bounded, local, noise-free *functionals of the input field*, with the same quadratic small-field expansion as flux squared, yet they satisfy AF-W in a vacuum-equivalent contact theory. The contact noise belongs to the input law, not an auxiliary soft RG kernel. This is not asserted to be the continuum law of the actual S4c lattice construction. It is an explicit refutation of **linearization alone ⇒ the quadratic comparator dichotomy for a bounded compact observable**. Lemma EV's two-sided comparability does not supply equality of observables or preserve signs of differences at two scales.

A smaller gap in the same paragraph: a nonzero compactly supported tensor test need not give a nonzero `w`. For example, a nonzero co-closed test `φ=*dη` can satisfy `p_μφ̂_μν=0`, hence `w≡0`. Analyticity of `φ̂` alone does not exclude this. Verify coupling to the field-strength sector. Once `w` is positive on a set in any fixed annulus away from zero, that already suffices for the polynomial-divergence argument; support at arbitrarily large `|v|` is unnecessary.

**NOT-VERIFIED — `HINT55.md`, §9.4 `survives the OS quotient`.** `⟨Ω,[O]⟩` requires an identified observable in the positive-time reconstruction algebra, or a proved extension to it. A four-dimensional heat kernel has tails in both time half-spaces, so `𝓔(t,x)` is not automatically such a local positive-time observable. Moreover CT explicitly exhibits OS-equivalent linear fields with different flowed one-point functions. SEP does prove that AF-W is impossible throughout the stated polynomial-contact families under the *specified quadratic realization*. That is narrower than a general invariance of these one-point functions, or a classification of all observable identifications in a free reconstructed theory. Supply that bridge before claiming the requested OS non-freeness. I do not infer any failure of OS0–OS3 from this missing bridge.

## 3. Free coefficient and normalization

**CONFIRMED — `HINT55.md`, §3.1 `A_∞`, §9.2 `Precision`.** An independent derivation, using the transverse trace rather than the script's hard-coded coefficient, is

\[
\begin{aligned}
\sum_{\mu\nu}\langle G^a_{\mu\nu}(t)G^a_{\mu\nu}(t)\rangle
&=6e_a^2\int\frac{d^4p}{(2\pi)^4}e^{-2tp^2},\\
\int\frac{d^4p}{(2\pi)^4}e^{-2tp^2}&=\frac1{64\pi^2t^2},\\
f(t)&=\frac3{128\pi^2}\sum_a e_a^2.
\end{aligned}
\]

Thus `A_∞=3(N²−1)/(128π²)` for the standard heat time and `e_a²=g_std²`. In FLOW's convention `u=2N/g_std²`, the same value is `2N A_∞/u`. This is an exact free computation; identifying it as the leading term of the interacting measure is a perturbative statement, as §9.2 acknowledges.

**NOT-VERIFIED normalization match — `HINT55.md`, §1.1 `without the factor β`; `PROOF.md`, `S3 Wilson action`.** Literally taking `S_geo=S_W/β=Σ_p(1−Re tr U_p/N)` with the standard gradient gives diffusion coefficient `1/(2N)`. Standard heat time requires `S_geo=g_std² S_W=2N S_W/β`, or an equivalent convention. Diffusion coefficient `α` changes the free coefficient to `A_∞/α²`. Specify the action/gradient convention before identifying the lattice and continuum coefficients. Compare [Lüscher, equations (1.3)–(1.4)](https://arxiv.org/html/1006.4518v3).

**REFUTED numerical convention import — `HINT55.md`, §9.6 `Lüscher's k₁`.** The cited coefficient belongs to the expansion in `α=g²/(4π)`, whereas HINT55 uses it in an expansion in `g²`. The required coefficient is `k_g=k_α/(4π)`. For pure SU(N) at `q=(8t)^{-1/2}` it is exactly

\[
k_g=\frac{N}{16\pi^2}\left(\frac{11}{3}\gamma_E+\frac{52}{9}-3\log3\right).
\]

Consequently the illustrative one-loop value of `4k_g/b₀` is `4γ_E+208/33−(36/11)log3`, not the expression obtained by substituting `k_α` for `k_g`. See [Lüscher, equations (2.32)–(2.36)](https://arxiv.org/html/1006.4518v3). This corrects the `[m]` illustration, not H-RED-sharp or the general remainder inequality. The symbolic leading coefficient `A_∞b₀=33N(N²−1)/(6144π⁴)` in §3.2 is correct.

## 4. Reduction arithmetic, limits and actual Yang–Mills content

**CONFIRMED — `HINT55.md`, `(4.1)`, `(4.2)`, `Theorem H-RED`.** Write `p=1−ϑ∈(0,1]`, `b=β₋log L>0`, `x=U₊(m₀)`, `y=u_{K−m₀}≤x`, `a_m=b(m−m₀)−R_F`. An explicit version of the threshold is

\[
m_1=m_0+\max\left\{0,\left\lceil\frac{(2C_+x/c_-)^{1/p}-x+R_F}{b}\right\rceil\right\}.
\]

With `x≥1` and `C₊≥c₋`, this ensures `a_m>0`. The decisive estimate, uniform over the actual cutoff-dependent `y`, is

\[
\frac{d}{dy}\frac{(y+a)^p}{y}
=-\frac{(y+a)^{-\vartheta}(\vartheta y+a)}{y^2}<0.
\]

Hence `C₊(y+a_m)^{-p}≤c₋/(2y)`, and `W_m≥c₋/(2x)`. No smallness of `C₊/c₋`, of a perturbative remainder, or of `R_F` enters this implication. The cost can be a very large but finite separation. The small-coupling regime of F-tune is an explicit upstream hypothesis, not a new hidden restriction introduced by H-RED. The endpoints `ϑ=1` or `β₋=0` would fail: constant `f` can then meet the corresponding nondecaying bounds. They are properly excluded.

I checked the quoted upstream *statement*: `FLOW.md`, `Theorem F-flow` and `Theorem F-tune`, give the needed direction of running, `β₊≥β₋>0`, and cutoff/torus-independent constants conditionally on their named inputs. This review does not certify the analytic inputs or their delivery by the RG construction.

**CONFIRMED — `HINT55.md`, `Theorem H-RED′`.** Replacing unknown actual couplings by the bounds gives directly

\[
C_+U_-(m)^{-p}\le \frac{c_-}{2U_+(m_0)}.
\]

The quoted comparison of thresholds is correct because
`x+a_m−U₋(m)=(β₊−β₋)m₀log L+R_F≥0`. `E/EXISTENCE.md`, locating `The same two bounds hold for E_K`, does explicitly state cutoff- and volume-uniform bounds for X-NTAF; Lemma EV converts their constants as claimed, `c₋=Nδ_*` and `C₊=(π²N/2)C_ϑ`. This verifies the interface to TS′, conditionally on X-NTAF and its inputs. It does not resolve the block comparator bridge in §2 above.

**CONFIRMED — `HINT55.md`, `Theorem H-RED-sharp`.** Put `v_k=A_sch/f_k`. The exact worst corner is `v_j=u_j−C_sch`, `v_n=u_n+C_sch`; the actual minimum is

\[
\frac{A_{\rm sch}}{u_n+C_{\rm sch}}-\frac{A_{\rm sch}}{u_j-C_{\rm sch}}.
\]

The stated, weaker denominator bound is valid once `β₋Δlog L−R_F−2C_sch>0` and `u_k>C_sch`. The least integer strict threshold is `⌊(R_F+2C_sch)/(β₋log L)⌋+1`. The `O(g⁴)`-to-inverse-coupling conversion in §9.6 does require its explicitly stated `Cg²≤A_∞/2`; it does not license that conversion at arbitrary coupling. No smallness of the coefficient `C` itself is required. A single sharp witness still does not eliminate CT representatives.

**CONFIRMED — `HINT55.md`, §4.1 `Limits`.** At the coarse scale, the second-moment bound supplies uniform integrability and convergence of expectations. At each fixed finer scale, nonnegativity and weak convergence supply the needed upper bound by Portmanteau, without assuming a fourth moment there. In particular

\[
W_m(\omega)\ge\limsup_jW_m(\omega_j)\ge c_W.
\]

Taking the cutoff/volume limit first at each fixed `m`, then `m→∞`, establishes `f(t^(m))→0` and `liminf_{t↓0}f(t)=0`. A countable common subsequence is essential and is included in CONV-E's reading. No interchange of a moving UV scale with the cutoff limit is justified or needed.

**REFUTED as a general continuity assertion — `HINT55.md`, §9.4 `continuous under (MOM-E)/(CONV-E)`.** Only the coarse observable has a uniform moment above order one. For a finer nonnegative variable, `X_j=j b` with probability `1/j` and `0` otherwise converges in law to zero while `E X_j=b`. Keeping the coarse observable constant gives MOM-E and weak convergence but a jump in `W`. Thus the proof gives upper semicontinuity of `W`, not continuity. That is enough for the closed inequalities `W_m≥c_W`; the closed-condition conclusion survives with this correction.

**NOT-VERIFIED from the displayed grid bounds alone — `HINT55.md`, §8.2 `f(t) → 0 as t → 0`.** The proof establishes the discrete limit and the full liminf, which suffice for AF-W. Nonnegative continuous functions can satisfy all grid bounds and have spikes between them: for `t_m=c_tL^{-2m}`, one example on `0<t≤c_t` is

\[
f(t)=\frac1{x+(\beta/2)\log(c_t/t)}+
\sin^2\!\left(\frac{\pi\log(t/c_t)}{2\log L}\right),\qquad x\ge1,\ \beta>0.
\]

Its grid values are `1/(x+βm log L)`, its liminf is zero, and its limsup is one. This is a counterexample to the inference from grid estimates alone, **not a claimed Wilson-flow counterexample**. For the action-density plaquette energy, translation invariance plus Wilson-action dissipation can supply the missing interscale argument: if `e(t)=⟨E(t)⟩` is non-increasing, then for `t_{m+1}≤t≤t_m`, `f(t)≤L⁴f(t_{m+1})`. State and pass that inequality to the limit where applicable; do not assume it for every alternative observable. Also, AF-W itself means a strict finite UV deficit, not necessarily a zero bare charge.

**NOT-VERIFIED — `HINT55.md`, `(TS-low)`, `(TS-up)`, `(MOM-E)`, `(CONV-E)`, `(FLOW-BLK)/(SRC)`.** These remain constructive inputs for the bare Wilson-flow observable. First-moment comparisons alone do not prove a second-moment bound or identify the limiting observable. The conditional reduction is not circular algebra, but the all-scale observable upper bound plus positive fixed-scale lower bound contains the substantive asymptotic-freedom/nontriviality work. Neither the formal β-function nor `hi55_b` supplies it. No unconditional cutoff- and volume-uniform H_int is established here.

## 5. Soft noise and the actual kernel

**CONFIRMED — `HINT55.md`, `Lemma NA-lin`.** Expanding the forward recursion gives `A_m=𝒜^mA₀+Σ_{k<m}𝒜^{m−1−k}ζ_k`. The stated centring and independence kill every cross term. The identity is valid for any square-integrable initial law. It is not an identity for group logarithms or for the nonlinear S4c map.

**CONFIRMED — `HINT55.md`, `Lemma BARE`; `PROOF.md`, `K(V, U) := Π_c k_c`.** Successively integrating normalized transition kernels leaves exactly the bare Wilson marginal. An observable depending only on `U₀` cannot be altered by changing those auxiliary kernels. Also confirmed as a relevant upstream countermodel: `E/EXISTENCE.md`, `Corollary SEP (one-point AF-type bounds`, explicitly supplies logarithmic one-point bounds in a Gaussian soft chain whose reconstructed Hilbert space is the vacuum space. These soft bounds alone cannot certify the bare-field witness.

**CONFIRMED — `HINT55.md`, `Kernel check for (KER-fwd)`; `PROOF.md`, `Decision 4: the RG kernel` and `Lemma H0 (crossing-link structure)`.** Mere non-unitarity of a fixed centre would not suffice: a constant contraction times a unitary location could still give independent noise. The decisive fact here is that the contraction varies with the past field. There is an exact test using the actual contours. In SU(2), set all fine links to the identity except one off-centre crossing link, set to `−I`. Exactly the fraction `q=L^{-3}` of the contours for that coarse link cross it, so

\[
\overline M_c=(1-2q)I=:rI,\quad 0<r<1,
\]

whereas the flat configuration has `M̄_c=I`. Both statements follow directly from the crossing-link structure. The conditional density is proportional to `exp[(κr/(2g²)) Re tr V^{-1}]`. Its maximum/minimum density ratio is `exp(2κr/g²)`, compared with `exp(2κ/g²)` for the flat configuration. This ratio is invariant under translating a fixed noise law on the group. Therefore no choice of deterministic unitary centre turns these two laws into the same independent multiplicative noise.

The discrepancy is not confined to large fields: replace `−I` by `diag(e^{iθ},e^{-iθ})`. The polar modulus of `(1−q)I+q diag(e^{iθ},e^{-iθ})` is the scalar
`r(θ)²=1−2q(1−q)(1−cos θ)`, varying even at arbitrarily small nonzero `θ`. This also explains the quadratic small-field correction.

For `N≥3`, put `diag(−1,−1,1,…,1)` on the crossing link instead. Then `M̄=diag(r,r,1,…,1)` is not unitary. A translate of the flat conditional density would have exponent `a Re tr(V†W)` for some `W∈SU(N)`, `a=κ/(Ng²)`. Equality with the density at `M̄` would force `Re tr[V†(M̄−W)]` to be constant for every `V`. Haar averaging makes that constant zero; orthogonality of the fundamental matrix coefficients, and inequivalence of the fundamental and conjugate representations for `N≥3`, then give `M̄=W`, a contradiction. Thus the exact failure holds for all the stated `N≥2`. A general polar unitary need not itself have determinant one, so the note's polar-coordinate display also needs that qualification; these explicit examples avoid the issue.

**NOT-VERIFIED — `HINT55.md`, §4.4 `(ANTI-♭)` route `(β)`, `(W-AF2_r)`, §9.5 `then (NOISE-ADD)`.** The stated nonlinear NOISE-ADD has the direction

\[
\mathbb E\Psi_{\rm det}\le C_{NA}\mathbb E\Psi_{\rm soft}+C'_{NA}g^{2-2\vartheta}.
\]

It can transfer an upper bound. It cannot transfer a soft lower bound after subtracting noise. Even the exact scalar data `EΨ_soft=2g²`, Gaussian comparison value `2g²=g²(w_fine+w_noise)` with `w_fine=w_noise=1`, and `EΨ_det=0` satisfy that one-sided inequality and zero comparison error, but fail every positive ANTI-♭ bound. This tests the implication supplied by those estimates, not an asserted realization of the actual Wilson chain.

In the additive linear model an additional *equality* supplies the subtraction. For the actual nonlinear kernel one needs, for example, a lower comparison `EΨ_det≥EΨ_soft−N_ref−εg²` with controlled `N_ref` and `ε` below the signal margin. This is not the displayed NOISE-ADD. Further, `E/EXISTENCE.md`, `Lemma NT-G`, uses a Gaussian chain with **constant** fine coupling and noise at the observation coupling `g_j`; the actual multiscale kernel has level-dependent couplings. Equality or a sufficiently accurate inequality between their noise budgets must be proved. Probability `o(1)` for an exceptional event must also be translated into an error at the required signal scale; its limiting parameter and the accompanying moment estimate must be specified. ANTI-♭ is honestly marked open, but its proposed route is not yet a proved reduction to the inputs as written.

## 6. Gates, controls and provenance

**CONFIRMED within the registered finite checks — `checks/hi55_a_comparator.py`, `VERDICT`; `checks/hi55_b_reduction.py`, `VERDICT`.** I executed both unchanged with Python bytecode writes disabled. Their outputs match the saved logs exactly:

- A1/A2/A3a–e/A4 passed; the tensor-sign control failed at all 25 tested momenta; the gauge trace control returned `{3,10/3,4,13/2,13}`; the zero-contact differences were exactly zero; A4 was `3/128` with `π²` factored out.
- B1: 300 parameter sets, no violations, 100/100 registered below-threshold controls behaved. B2: 900 checks, no violations, and 270/270 below-threshold controls behaved.

The finite tests support arithmetic, not the universal analytic statements. B1 tests `ϑ∈{0,1/2}` and computes a threshold at its chosen `u₀`; the cutoff-uniform `y≤x` step is supplied by the handwritten derivative proof. I independently checked that step in 2,160 exact inequalities using `ϑ∈{0,1/3,1/2,2/3,9/10}`, three values of `x`, three ratios `C₊/c₋`, and `y∈{x/99,x/3,x}`, including large ratios. Rational powers were compared by integer powers, not floating-point evaluation. An independent sharp example gave the exact minimum `49/510` and the stated weaker lower bound `7/90`.

**CONFIRMED as informational only — `checks/hi55_c_latfree.py`, `C1`, `C2`, `C3`.** I executed the same rational enclosure/gate code after removing only its float-display loop in memory. No float arithmetic was executed. The three gates passed. For `τ=1,32,64`, respectively, exact outer enclosures for `F_lat` are

\[
\frac{[1836104965000,1836104965001]}{10^{15}},\quad
\frac{[1589364194246,1589364194247]}{10^{15}},\quad
\frac{[1586244668927,1586244668928]}{10^{15}}.
\]

I independently certified the supplied rational `π²` interval using `π=16 arctan(1/5)−4 arctan(1/239)` and alternating-series bounds (24 and 8 terms). The exponential/Bessel tails are valid: the first omitted ratio is at most `1/2`, and the full omitted tail is bounded by the retained last term. The independent lattice derivation is `∫BZ e^{-2τp̂²}=[e^{-4τ}I₀(4τ)]⁴` with the traced field-strength factor `3/2`.

Limit of C1: it proves decrease at the seven listed times, **not** monotonicity at every real `τ≥1`, for every lattice energy definition, or uniformly over finite tori. C2 is a genuine opposite-regime control. C3 checks its two registered windows, not an all-orders asymptotic expansion. The `1/(8τ)` correction agrees symbolically with `e^{-x}I₀(x)∼(2πx)^{-1/2}(1+1/(8x)+…)`, but the finite gates are not a proof of that expansion.

I also ran seven in-memory mutations, with no file changes: wrong tensor sign, wrong Gamma-integral scale, wrong A4 target, missing factor two in the crude threshold, wrong sign of the sharp scheme-error deduction, reversed C1 comparison, and a false π² lower bound. Every mutation was detected by a failed gate or assertion. The runners print FAIL rather than necessarily returning a nonzero exit code; I inspected the verdicts, not merely process success. None of these checks tests KL classification, Fatou, the OS map, nonlinear S4c, nonlinear noise comparison, or an interacting Wilson expectation. The claimed historical order of author criteria and scripts was not independently authenticated by git; it is not part of the mathematical verdict.

Final source/runner hash recheck: 2026-10-29 00:30:57 UTC; all matched the checked inputs. Reviewed target SHA-256: `b4c611b16cd5faa1c1bb59636b85ff39d451d657fb24edc9695f8f2d48105722`.

Runner SHA-256 values, in order a/b/c:

```text
27b56166fabac07854427bce1787796537a8b3cd319195cc3918c18728b05606
60b09b27583a39387aa6d5a2ab07a491056b86637e2a7917cdd91dc4d9f0d515
e4196cad86cecc2aeeb0d2a9c644e5d496959fbe262454c52625504534f2d89d
```

## Exactly what may be banked

1. **CONFIRMED:** the free coefficient `3(N²−1)/(128π²)` for standard continuum heat time; the tensor and gauge-parameter identities; constancy on the specified scale-invariant/canonical Maxwell classes at finite moment.
2. **CONFIRMED:** KLM, the contact-term counterexample, UV-D and mixture separation **for the explicitly defined quadratic abelian observables and `𝔊₀∪𝔊₁`**. They do not apply merely because the observable is gauge invariant or has a positive two-point spectral measure.
3. **CONFIRMED:** H-RED, H-RED′ and H-RED-sharp as conditional algebraic/limit implications. They require no extra small comparison constant. H-RED supplies the uniform witness family and zero UV liminf when its actual observable, moment, convergence and flow inputs hold.
4. **CONFIRMED:** Lemma EV, linear noise addition, invariance of the bare marginal under normalized soft kernels, and failure of exact independent multiplicative noise for the specified contour-mean kernel. The reproduced and mutated gates support their stated arithmetic scopes only.
5. **NOT-VERIFIED; do not bank:** actual bare Yang–Mills TS bounds, nonlinear NOISE-ADD/ANTI-♭ or the proposed subtraction route, the bounded S4c comparator transfer, the reconstructed-observable identification, all-free-theory coverage, or a completed OS0–OS3 non-free construction. The unequal-colour normalization claim is **REFUTED as defined**, the continuity claim needs semicontinuity in its place, and the cited perturbative `k₁` illustration has a `4π` convention error. The bankable advance is the restricted comparator theorem plus conditional reductions, **not an unconditional H_int or a proof that the reconstructed Yang–Mills theory is non-free**.
