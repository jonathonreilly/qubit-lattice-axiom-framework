## Repo search

Writer: OpenAI Codex, dispatched as **gpt-6-astra xhigh**, FINISH row 1070. Checked source: `ddf2831107bcd569809b485c24c5d15207f23a2f`, `library/gap-aniso-trajectory.md`, row 1066 by Claude Fable 5.2 medium. This is a research check, not an audit; it grants no status and claims no mass gap. I did not read row 1069, attack the seed, construct a bridge, check the full published O(n) proofs, or run Lean or numerical proofs. All source line numbers below refer to this pin.

The requested `prior/gap-aniso-check-astra.md` is absent. The lead reports searching main and PRs 10114, 10133, 10134 and 10141, without itemized target hits. I read the November 8 search digest in full. It concerns earlier UV/history obligations, not this target. Exact target searches in it and `open-registry.md` found no competing owner. I read `prior/gap-aniso-read-luna.md` (row 1067) in full and used its source map, rather than repeating its survey.

I fetched main and checked the relevant passages at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`:

| Prior hit | Passage checked | Closeness and use |
|---|---|---|
| `research/mass-gap/library/prior/gap-tests-lit.md` | 23–25, 63–75 | Five-dimensional anisotropic SU(2) numerical phase evidence; U(1) action/theorem cautions. Adjacent controls, not a 2+2 bridge. |
| `research/mass-gap/library/prior/gap-vir-lit.md` | 31–33 | Karsch abstract-level weak-coupling matching. Reused; no nonperturbative supplier. |
| `research/mass-gap/library/gap-vir-sc.md` | 198–202 | The anisotropy response at order-one coupling is open. Different consumer, same caution. |
| `docs/GAUGE_WILSON_CUBE_SLAB_ANISOTROPIC_CENTRAL_OSCILLATOR_BOUNDED_THEOREM_NOTE_2026-09-07.md` | 1–42; 72, 98, 123–125 | Supplied finite-cube Gaussian/oscillator interface. Explicitly excludes a microscopic multilayer transfer and selected continuum dynamics. Not this trajectory. |

Row 1067 reports the same oscillator note on the four PR refs and no closer target hit. I did not repeat that global PR search. In this checkout I used row 1053's face/anchor definitions and the existing consumer correction in `gap-flux-w-check-astra.md:146–178`; I did not redo the checked FACE-LIM or ANCH proofs. The published 2+2 coefficients found below cover one literature question, not this check of row 1066.

The SA-index README, matching chunk rows and their neighbours, and obligations were consulted first. Names for the present sheet/bridge objects have no matching entry. The closest anisotropy rows are `chunk-06.md:117–128`, obligations 327–334: SA 7006–7014 concerns a small traceless plane-weight insertion and a sketched one-loop law, not the strong layered corner. SA 580–599 separates scalar reconstruction from a mass-gap estimate. Those source ranges were read. The CA 4.12–4.19 index concerns background/operator/stage questions and has no target matching entry. CA-I 2697–2712 explicitly does not assert clustering, a mass gap or regularisation independence. Thus none supplies `(S-q)` or `(UNIV-aniso)`. Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, and Balaban for the construction on which they build.

Downloads were made only in the new directory `/tmp/sa-gap-aniso-check-astra.pOBsR6`. The outline and CA-I were each fetched once at `31a47c543775`. The output was saved incrementally. Only this report changes in the checkout.

## Verdict map

`HOLDS` below covers the stated implication or finite identity, not the truth of an open premise. The numbered findings give the corrections and first failing lines.

| Requested item | Verdict |
|---|---|
| Step 4: `(MIX)` attribution and choice of `X` | **FAILS**, line 76 as a reading of the cited theorem; corrected input in finding 1. |
| `R_eps`, directional lengths, `xi_R` | **HOLDS AFTER CORRECTION** of domains, quantifiers and physical identification, finding 1. |
| Chain `(S),(T),(B)` and consumer | **HOLDS AFTER CORRECTION** as an open dependency plan; the claimed decisions do not follow, findings 2 and 6. |
| BARE and BARE-1 | **HOLDS AFTER CORRECTION** to positive finite parameters, with separately defined face limits, finding 1. |
| PERP-BD (a)–(c) | **HOLDS** given `(S-q)`, on the domain of `xi_R`. The blanket continuum reading **FAILS**, line 108, finding 2. |
| 5.3(a), engineering counting | **HOLDS AFTER CORRECTION**: tree-level counting, not exact blocking, finding 3. |
| 5.3(b), exponent `3/4` and cube | **HOLDS AFTER CORRECTION** as a perturbative sheet calculation. Its ratio formula **FAILS**, line 126, finding 3. |
| 5.3(c), logarithmic 2+2 coefficients | **HOLDS AFTER CORRECTION** as a published perturbative result; universal domain claim not established, finding 4. |
| 5.3(d), exhaustive crossover cases | **FAILS**, first missing control in line 131; independent false inference in line 132, finding 5. |
| 5.3(e), displayed power | **HOLDS** as algebra conditional on its matching equations and assumed length asymptotic, finding 5. |
| 5.3(f), eventual exit in that ansatz | **HOLDS AFTER CORRECTION** to an asymptotic conditional statement; full decision **FAILS**, finding 5. |
| REN(1) | **HOLDS AFTER CORRECTION** for the one-cutoff conclusion `C_beta`; the torus-seed identification **FAILS**, line 153, finding 6. |
| REN(2) | **HOLDS AFTER CORRECTION** with an actual continuum limit, spectral passage and universality; `xi_R=1` alone is insufficient, finding 6. |
| REN(3) | **HOLDS AFTER CORRECTION** as a one-way sufficient path; the “removes none” inference fails, finding 6. |
| Four items of 5.4 | Conditional U(1) obstruction and monotonicity direction survive; the claimed blocking flow does not; the 2D theorem alone supplies no coupled estimate, finding 6. |
| Lemma PERP | **HOLDS**, finite free box, finding 7. |
| Claim S2 | **HOLDS**, SU(2), finite free box; its uniform estimate needs the specified mixing constants, finding 7. |
| U1-BR | **HOLDS AFTER CORRECTION** as a conditional statement for one specified action; the cited Wilson application is not verified, finding 8. |
| Layer phase control and K1 | **HOLDS AFTER CORRECTION** to their actual scope, finding 8. |
| “V2 FAILS as a route by S0” | **FAILS** as a proved retirement of V2. Only the unspecified bridge is tautological given the seed; V2 remains uncompleted, finding 9. |

## 1. Definitions, source scope and bare algebra

**First failing source claim: line 76.** I opened OpenAI's *Sharp mass bounds for the two-dimensional O(4) model*, at `4eaee87548250b2682affda7d05d947c05554bae`: Theorem 3.1, p. 12; (3.67) and §3.12.1, p. 32. It supplies a Lipschitz-observable estimate on unpinned free subgraphs and sufficiently large unpinned tori, with polynomial overhead and

\[
\Xi(\beta)=\exp\{\pi\beta+C\sqrt{(1+\beta)\log(2+\beta)}\}.
\]

It does not there supply arbitrary pinned boundary conditions or a sup-norm-only estimate for all bounded functions. The uniqueness assertion is for periodic local limits. Row 1009 reports these restrictions correctly. Charged estimates with pins elsewhere in the paper do not enlarge the all-observable theorem's domain. The paper is a cited, unchecked input here. [Pinned source](https://raw.githubusercontent.com/openai/math/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf).

**Replacement text:** “Assume `(MIX)` on the specified sheet laws, with its observable norms, dependence on beta and boundary class stated. The cited theorem proves a weaker unpinned Lipschitz version. The stronger version printed here is OPEN.” For step 6's smooth matrix insertions, the weaker version may suffice with extra factors; no pinned assertion is needed for the finite-box identity.

Choose `X(beta)>=1` finite on the seed's domain. Declare whether constants are uniform in beta. An admissible mixing length is not unique: replacing it by any larger function preserves the bound. Nothing in `(MIX)` forces a sharp two-loop asymptotic or makes `X` invertible. Hence line 123 cannot identify this `X` with a physical two-point length. Use separate notation `xi_phys` for that additional asymptotic hypothesis. The assertion `X>=xi_2` follows if `xi_2` means the optimal exponential length in the same state: apply `(MIX)` to spin coordinates and sum the four covariances in the zero-field symmetric state. It does not compare arbitrary definitions or boundary conditions.

Define each directional common rate as the supremum of `m>=0` for which every allowed local pair has a finite translated-covariance prefactor, uniform over the stated states and translations. The supremum need not be attained. Use reciprocal conventions at zero and infinity. Define `xi_R` only where both lengths are positive and finite. Equality with a ratio of physical spacings needs matched observables and convergence of directional physical lengths to the same nonzero finite value. It is not a consequence of naming their ratio. In a 2+2 action one measured ratio does not tune all three kinetic coefficients; see finding 5.

For `eps>0`, `beta_M,beta_T>0`, `X(beta_M)<infinity`, the BARE proof is reversible division by positive numbers followed by the increasing square-root map. On the classical family the two inequalities are exactly

\[
\xi_0^2\ge\beta X(\beta)^2/\varepsilon,
\qquad
\xi_0^2\ge X(\beta)^2/(\varepsilon\beta).
\]

Taking their maximum proves BARE-1. Choosing `xi_0` above that maximum for each positive beta proves the existence of bare families in `R_eps`. It makes no claim about physical anisotropy. At `beta_T=0`, `beta_M=0`, or `beta_L=infinity`, use the original inequalities and separately defined extended ratios; do not divide by zero. The face is an extension of the parameter space, not a finite Wilson coupling point.

## 2. What `(S-q)` and PERP-BD actually establish

Let `q=log(1/(C eps))>0`. The transverse clause of `(S-q)` makes `q` an admissible common rate. Thus `l_perp<=1/q`. For defined `xi_R`, `l_par=xi_R l_perp` gives (b), and `xi_R>=q l_par` gives (c). This proves all three mathematical conclusions of PERP-BD. It uses neither longitudinal matching nor perturbation theory.

This is a valid **conditional obstruction**, not a determination of the proposed seed. The distinction is explicit:

- `(S)` asks for qualitative clustering at each point of a region.
- `(S-q)` asks for a common transverse rate bounded away from zero throughout that region.
- Qualitative rates can be positive at every point of a sequence and tend to zero. Hence `(S)` does not imply `(S-q)`.
- Lemma PERP controls finitely many Taylor coefficients at the face. It supplies no uniform radius or summable coefficient bound, and no estimate off the face.

**Line 112 fails at “If (S-q) is false, V2 has no seed”. Replacement:** “If `(S-q)` holds, the diverging-length trajectory `(T)` is impossible. Failure to prove, or even failure of, `(S-q)` does not refute `(S)`. A weaker seed needs separate analysis.” A uniform convergent expansion with the claimed activity bounds could prove `(S-q)`; that expansion remains open. Its desired output cannot decide the trajectory before it is proved.

**Line 108 needs a target restriction.** O(4) covariance alone does not force divergent lattice correlation lengths. For a simple logical counterexample, let `Z_n` be independent standard Gaussians on a four-dimensional lattice and set `Phi_a(f)=a^2 sum_n Z_n f(an)` for smooth compactly supported test functions. Then

\[
\operatorname{Cov}(\Phi_a(f),\Phi_a(g))
=a^4\sum_n f(an)g(an)\longrightarrow\int f(x)g(x)\,dx.
\]

Their Gaussian characteristic functions therefore converge to rotationally invariant white noise, although lattice correlations vanish off the diagonal. This is not a Wilson counterexample and has no nontrivial separated propagation. It refutes the unqualified assertion that no rotation can act on such a limit.

**Replacement:** “A continuum scaling with `a_perp l_perp` tending to a nonzero physical correlation length and `a_perp->0` requires `l_perp->infinity`. PERP-BD excludes that scaling under `(S-q)`.” Alternatively, a uniform bound `A_j exp(-q r/a_perp,j)` with `log A_j=o(1/a_perp,j)` makes separated correlations vanish. Establish that uniformity for the renormalized, possibly smeared observables before using it. The assertion that a particular nontrivial longitudinal continuum limit exists (line 114) is also not proved by an upper correlation-length bound.

## 3. Counting and the sheet exponent

**5.3(a): replacement.** “For a slowly varying classical field, longitudinal rescaling by `b` gives engineering factors `b^2 beta_T`, `beta_L/b^2`, and `beta_M`.” The powers follow by the two longitudinal volume factors and the number of longitudinal derivatives in each quadratic curvature term. They are not the coefficients of an exactly blocked Wilson measure. Integration produces further interactions, and no blocking kernel or projection onto three coefficients is specified in line 118.

**The exponent check.** The original 1976 Brézin–Zinn-Justin full text was not obtained openly: the APS full-text endpoint returned 401; institutional retrospective links returned 404; an open-scan host did not connect. I did not pay, sign in or bypass access. I instead checked the equations in Zinn-Justin's own openly available *Vector models in the large N limit: a few applications*, §3.2, equations (3.14), (3.17a,b), p. 26, and the integrated field factor (3.20), p. 27. These are finite-N sigma-model RG equations despite the title. The page images were read because extracted formulas were garbled. Credit Brézin and Zinn-Justin for the method; the expanded 1976 paper also credits Le Guillou. [Open author lecture copy](https://saalburg.aei.mpg.de/wp-content/uploads/sites/25/2017/03/zinn.pdf), [arXiv record](https://arxiv.org/abs/hep-th/9810198).

Writing `s=log b`, inverse temperature `B=1/t`, and `q=B(b)`, the cited one-loop equations give

\[
\frac{dB}{ds}=-\frac{n-2}{2\pi},
\qquad
\frac{d\log z}{ds}=-\frac{n-1}{4\pi B}.
\]

Dividing and integrating gives

\[
z=(q/B)^{(n-1)/(2(n-2))}=(q/B)^{3/4}\quad(n=4).
\]

The normalized spin two-point factor is `z^2=(q/B)^(3/2)`. Four distinct independent sheet fields give `z^4=(q/B)^3` at first order in the transverse perturbation. Thus the exponent and cube survive. This is formal perturbation theory while both stiffnesses are large, not an identity of unit spins or a bound on the interacting blocked model. Higher-order interactions and errors are not controlled by this calculation.

The two-loop physical scale `B^(-1/2) exp(pi B)` is consistent with the normalization in OpenAI's O(4) paper, pp. 2–3; that paper's stated theorem gives two-sided order bounds, not the claimed exact prefactor for `(MIX)`. If the separate ansatz `xi_phys(B)=K_2 B^(-1/2) exp(pi B)(1+o(1))` and `xi_phys(q)=xi_phys(B)/b` are assumed, taking logarithms does give

\[
q=B-\pi^{-1}\log b-(2\pi)^{-1}\log(B/q)+o(1).
\]

**First algebraic failure: line 126.** Even granting line 134's equations,

\[
\beta_T=\frac{B^3}{K_T b^2 q^2},\qquad
\xi_{MT}=\sqrt{K_T}\,b\,\frac qB.
\]

With the additional assumption `xi_R=K_R b`, this gives

\[
\frac{\xi_{MT}}{\xi_R}=\frac{\sqrt{K_T}}{K_R}\frac qB.
\]

After unit tree normalization, its leading logarithmic sheet term is `-log b/(pi B)`, not the printed `+3 log(xi_R)/(2 pi beta)`. If the matching factors themselves have additional logarithmic dependence, the ratio is undetermined without computing them. Neither reading gives line 126. This is a consistency check of the proposed ansatz, not a replacement derivation of Wilson matching.

## 4. Published anisotropy coefficients and their domain

Karsch's original scan, pp. 285–287 and 295–297, confirms the 3+1 weak-coupling setting, finite Hamiltonian-limit coefficients, and the restriction on changing anisotropy while preserving all physics at strong coupling. The SU(2) derivative values quoted in row 1066 agree with its abstract. Smallness is asymptotic in the gauge coupling; the paper supplies no theorem about the present seed region. [Open Karsch scan](https://noah.nrw/ubbihs/download/pdf/5114815).

There **are** published 2+2 coefficients: Giuseppe Burgio, Alessandra Feo, Mike Peardon and Sinéad M. Ryan, *Gauge Theories on a 2+2 Anisotropic Lattice*, §II.A, p. 5, and §IV.B, p. 14, equations (38)–(40). The two coefficient differences in (38)–(39) grow logarithmically with anisotropy. Their introduction discloses computer symbolic algebra; this report uses their result only as published perturbative evidence, not as a discharged proof. [Primary preprint](https://arxiv.org/abs/hep-lat/0303005).

**Replacement for 5.3(c):** “Published 2+2 matching has logarithmically growing one-loop corrections. Its unresummed small-correction regime requires, in particular, `g^2 log xi` small. This is not a nonperturbative calibration in `R_eps`.” The hand sheet exponent is consistent with the presence of logarithms, but it does not compute the two full gauge-theory coefficients.

The purported equivalence `log xi << pi beta` iff `xi << X(beta)` up to powers is false. Even `xi=exp(pi beta/2)` is exponentially smaller than the asserted `X`, while `log xi/(pi beta)=1/2` does not tend to zero. Nor can `xi_MT` be substituted for calibrated `xi` outside a small-correction regime.

A valid *asymptotic* incompatibility follows if one additionally has `X(B)>=c B^(-1/2) exp(pi B)` and a calibration `xi_MT/xi=1+o(1)`: BARE gives `log xi/(pi B)>=1+o(1)`, inconsistent with `log xi=o(B)`. This does not establish the literal finite-point assertion “no point of R_eps lies in the domain”. A formal perturbative expansion has no proved validity region of that form in either cited paper. No use of its extrapolation can close the seed or the bridge.

## 5. The crossover cases and formula (e)

**Case (i), first unsupported inference, line 131:** a gap for decoupled sheets does not prove uniform clustering after the sheets are coupled. That is precisely the stability/expansion input `(S)`. Its below-one transverse length is taken from PERP-BD, so this case is not an independent proof without `(S-q)`. Evaluating the weak-coupling formula at terminal stiffness of order one is also uncontrolled. The proposed enlargement by `B^3` remains a conjecture.

**Case (ii), first failing inference, line 132:** `beta_T(b_*)=beta_M(b_*)` does not put *all three* blocked couplings near `beta_*`. The longitudinal coupling is independent; on the face it remains infinite. Even with classical counting one may choose `beta_L/b_*^2` arbitrarily larger than `beta_*`. The missing second tuning is exactly the issue discussed by Burgio et al., §II.A. Thus neither an isotropic blocked action nor `xi_R=K_R b_*` follows. The longitudinal hierarchy may fail earlier as well. These are not two proved exhaustive cases. The attribution of the weak-coupling four-dimensional finite length to an additional mass-gap input is correct.

**Formula (e) holds conditionally.** With `B=beta_M`, `q=beta_*`, the two equalities printed in line 134 imply exactly

\[
\beta_T X(B)^2=K_T^{-1}B^3q^{-2}X(q)^2.
\]

If the assumed asymptotic for this `X(q)` is inserted, this becomes

\[
(K_2^2/K_T)B^3q^{-3}e^{2\pi q}(1+o(1)).
\]

There is no algebraic error in that power. The factor `B^3/q^3` comes from the four field factors; cancellation of the extra `q` uses the two-loop length prefactor. Both inputs must be retained. They are not established for the strong-mixing `X` of step 4.

**Replacement for (f):** “For a family satisfying all these matching assumptions, with `q->infinity`, `B/q>=1`, and matching constants bounded away from zero and infinity, `beta_T X(B)^2->infinity`. Hence such a family eventually leaves `R_eps`.” An asymptotic calculation gives no exit threshold at “order one or below, whatever the unknown constants are”. It does not classify all points inside `R_eps` or prove a trajectory impossible there independently of `(S-q)`.

## 6. REN, the consumer, and the four bridge suggestions

Let `C_beta` mean exactly line 148's conclusion: every specified isotropic limit state clusters exponentially on the allowed local observables. Then, **assuming S is true**, `(S => C_beta)` is logically equivalent to `C_beta`. This tautology is the valid part of REN(1). It does not prove either proposition. Existence of a seed point must also be supplied; a conditional with false antecedent says nothing about the endpoint.

**The one-cutoff qualification in line 153 matters.** If “T_JW-lat at one coupling” means its fixed-cutoff restriction `C_beta`, the claimed containment holds by the preceding tautology. It does not contain the full named `T_JW-lat` in `gap-wall-assumptions-opus.md:485`, which requires a common physical rate for all sufficiently fine cutoffs and a total observable class. Even the fixed-cutoff restriction should specify a common rate across that class and the state quantifiers. A carry must accept that exact input. The already existing correction `gap-flux-w-check-astra.md:146–178` requires matched cutoff observables, cutoff-independent prefactors, the continuum reflection datum, `(H2)` and `(TOT)`.

**First failing inference in REN(1): line 153's torus sentence.** Infinite-volume local clustering does not control every finite-torus electric-flux sector or its partition-function deficit. Moreover, `parts/gap.md:24–26` says the fixed-coupling seed is needed **at each beta of the window**, with a carry, not merely at one unspecified beta. If a separate all-flux finite-torus seed and the exact carry are assumed, their conditional implication may be cited; `(BR-iso)` as defined does not provide them.

**Replacement for REN(1):** “Given `(S)`, `(BR-iso)_beta` is equivalent to `C_beta`, an unresolved one-coupling clustering target. To reach `T_JW-lat`, supply its common-rate, state, observable and cutoff-uniform transport clauses. A torus route separately requires the all-flux seed and its carry.”

**REN(2):** fixing `xi_R=1` fixes one measured ratio, not O(4) invariance or isotropic Wilson couplings. The parametrization by all `s>=s_0` is itself an existence assertion. Given an actual continuum family, convergence sufficient to pass uniform spectral bounds, and `(UNIV-aniso)` identifying its dynamics with the intended theory, the bridge includes the continuum gap. Those are additional hypotheses; the conditional containment is correct. Bare equality of two correlation lengths proves none of them.

**REN(3):** after adjoining the face and assuming the requisite face state and bounds, `(FACE-SG)` plus a nonvacuous lower clustering bound in `(BR-L)` is a sufficient route to `C_beta`. If `eps X(beta)^(-2)>beta`, start at `min(beta,eps X(beta)^(-2))`; there is no reversed interval to traverse. This proves only `V1-inputs => bridge`, not the converse. Therefore it does not prove that every V2 bridge retains all V1 obligations. Also `(BR-L)` as quoted on `[beta,infinity]` already assumes endpoint control.

The four items of 5.4 have these scopes:

1. **Soft bridge:** the endpoint-only universal assertion is false given a same-action U(1) counterexample (finding 8). This does not refute every group-blind method. An additional hypothesis, such as a verified uniform bound along the path, could fail for U(1). It must distinguish the counterexample; it need not mention the group by name.
2. **Monotonicity:** accepting U(1) Wilson-loop monotonicity, increasing loops decreases `-log` of the loop. If the area-rate limit exists, this gives an upper bound on tension at the stronger coupling. That direction cannot provide a positive lower bound. This is not itself a theorem about connected local correlations. No new SU(2) monotonicity result is supplied.
3. **Transverse blocking:** the assertion that a flow runs toward the anchor throughout `R_eps` is unproved. No RG transformation or estimate for its generated action is given. A bound on one correlation length does not define such a flow. The observation that no quantitative bridge step is supplied is correct.
4. **2D theorem:** the cited theorem concerns individual sheets. It alone gives no estimate for an order-one inter-sheet interaction. This is a scope statement, not a theorem excluding combinations with further input.

## 7. The finite-box results and the second-order bound

**Lemma PERP, lines 174–184: HOLDS.** On a finite free box all observables and `X_T` are bounded. The logarithmic moment generating function is analytic near the origin. Differentiating covariance `k` times in `t` inserts `k` copies of `X_T` into the joint cumulant. Expand by multilinearity.

For a term involving distinct plaquettes `P`, form `C=cl_P(A)`. If `k<d(A,B)`, `C` misses `B`. Every plaquette boundary lies entirely in `C` or entirely outside it. Thus one nonempty group of entries depends on the sheets in `C` and the other on sheets outside it. The product sheet law makes these groups independent. Their log generating function is a sum, so its mixed derivative vanishes. Repetitions do not increase `|P|`. Taylor's theorem proves the finite-box `O(t^d)`. Use `d=infinity` if no connecting set exists. This proof is finite cumulant algebra and is Lean-formalizable; it gives no uniform remainder.

**Claim S2, lines 188–196: HOLDS for SU(2) as stated.** The four boundary sheets are distinct. A centre flip on sheet 3 or 4 kills first order. At second order, distinct transverse plaquettes have an unobserved sheet appearing once, which kills that term; repeating a plaquette other than `p` omits one of the two observable sheets. Only `p,p` remains. This uses a free two-dimensional transverse box, not a small periodic cell with identified edges.

Set `M=Phi_1 Phi_2`, `N=Phi_4 Phi_3`. Independent left-right invariance gives

\[
E[N(u)\otimes N(v)]=\frac{G(u,v)^2}{4}I_4.
\]

Its trace is `E<N(u),N(v)>=G(u,v)^2`: each relative sheet matrix has expectation `G I_2`. Hence conditional integration over sheets 3 and 4 gives

\[
E[x_p(u)x_p(v)\mid1,2]
=\frac{G(u,v)^2}{8}
\operatorname{tr}\bigl(\Phi_1(v)^{-1}\Phi_1(u)
\Phi_2(u)\Phi_2(v)^{-1}\bigr).
\]

Centring `F,H` factorizes the two remaining sheet expectations. The Taylor factor `1/2` gives the printed **`1/16`**. The fourth-cumulant reduction is valid because the remaining partitions contain an odd insertion or the independent covariance of `F,H`.

**Uniform second order: HOLDS AFTER CORRECTION of constants.** Assume the actual unpinned two-point and matrix-insertion bounds with length `X>=1`, and write their amplitudes explicitly. For a fixed displacement `r=v-u` and finite support `A`,

\[
\sum_u e^{-\operatorname{dist}(A,\{u,u+r\})/X}
\le 2|A|\sum_{z\in\mathbb Z^2}e^{-|z|_\infty/X}
\le C|A|X^2.
\]

The last inequality follows by counting `8n` sites at max-norm radius `n>=1` and summing the geometric derivative. Discarding the other exponential only enlarges the sum. If `|G(u,u+r)|<=A_G e^{-|r|/X}` uniformly in `u`, then `sum_r sup_u |G(u,u+r)|^2<=C A_G^2 X^2`. Therefore the coefficient is at most `C A_G^2 A_F A_H |A| X^4`, uniformly in box size. No translation invariance of a finite free box is assumed. This completes the elementary sums in the source.

Uniformity in **beta** requires uniform amplitude control too. The cited unpinned theorem has beta-dependent polynomial overhead; it is not the stronger `(MIX)` asserted in line 76. Without that control, the calculation does not establish the universal small parameter `beta_T X^2` with fixed epsilon. It proves no all-order polymer estimate. The first bullet's extensive bound from two-point decay alone is a valid crude bound, not a proof that no sharper argument exists. The claimed susceptibility factor `X^2 B^(-3)` remains perturbative.

## 8. U(1), layers and test K1

**F1 and U1-BR.** For the face model at sufficiently small `beta_M,beta_T`, the stated Dobrushin route is appropriate: each sheet spin has four mixed-bond neighbours and belongs to two transverse plaquettes, each involving three other spins. A change in a neighbour changes a bounded conditional potential by a quantity tending uniformly to zero with these couplings. The finite sum of influences is therefore below one for sufficiently small couplings. The cited uniqueness theorem then gives exponential mixing. At the exact zero-coupling face point independence proves this directly, without invoking that theorem.

Thus the **logical implication** in U1-BR holds: one endpoint with exponential clustering and another without it refute the unrestricted endpoint-only bridge. The application must keep one action fixed. Guth's accessible abstract specifies a **Villain** action and nonconfinement; nonconfinement alone is not the stated local-correlation conclusion. The Fröhlich–Spencer full theorem was not obtained: the IHES link yielded metadata and the Springer download was a rendered subscription-preview page, not the article. Its abstract asserts a massless phase but does not settle the Wilson weight and exact observable bound. Row 1066's Wilson extension is recalled, and the threshold `2^14` must not be transferred between weights. [Guth record](https://doi.org/10.1103/PhysRevD.21.2291), [Fröhlich–Spencer record](https://doi.org/10.1007/BF01213610).

**Replacement:** “U1-BR holds conditional on `(F3)` for the same specified action as the seed. The cited Wilson application remains unverified here. A Villain counterexample applies to a bridge whose domain includes that action, with its own small-coupling seed.” No full U(1) theorem is discharged in this check.

**The corner and layer control:** the Gaussian dimension of the four-vertex perturbation is `1/(pi K)` with renormalized XY stiffness `K`; using bare `beta_M` is a low-temperature approximation. Relevance at that fixed point does not prove its eventual four-dimensional endpoint, absence of every layer phase, or exponential/nonexponential clustering at positive `beta_T`. Those inferences in line 217 must remain conjectural. The 4+1 layer evidence in row 1067 is mean-field/numerical and has Coulomb layers. It warns against assuming a phase-free path; it is not a rigorous phase theorem for 2+2 SU(2).

The sentence that Claim S2 “holds for U(1)” needs correction: PERP is group-blind, but S2's `I_4/4` and coefficient use the four-dimensional quaternion representation. Circle variables give `I_2/2` instead. The same kind of second-order argument exists, not the identical formula.

**K1:** a whole-state mixing hypothesis correctly rejects a massless product factor. At `beta_T=0`, for U(1) sheets with free symmetry, the local transverse plaquette observable satisfies

\[
\operatorname{Cov}(\cos\theta_p(u),\cos\theta_p(v))
=\tfrac12 G_{XY}(u,v)^4.
\]

This follows by expanding the cosines and integrating the four independent sheet phases. Thus a nonexponentially decaying positive XY two-point function gives a gauge-invariant local obstruction already on the face. For a product gauge group with factorized action, observing this factor ignores the finite SU(2) length. This is the correct diagnostic against a method that reads only the SU(2) factor.

It does **not** refute a theorem whose hypotheses already restrict the group to SU(2), nor prove that no relation between its spin length and full mixing length can be established. **Replacement for “R must use X”:** “The expansion needs whole-sheet mixing control. Use a length `X` for that control, or prove a quantitative comparison with `xi_2` before retaining the old region.” If `X=infinity`, exclude that parameter from the finite-mixing domain; do not evaluate `0·infinity` or say simultaneously that the region is empty and contains its zero-transverse endpoint. The U(1), frozen-group and Pin(2) exclusions in step 7 share this domain convention; their separate phase assertions are cited controls, not newly checked theorems.

## 9. Scope of the route verdict and final handoff

The first unsupported decision is step 4, line 83, “none inside R_eps”, before the quantitative seed is proved. The unconditional account of this in step 8.1 drops a premise that step 5.2 retains. Line 170's assertion that the old consumer is a failing line likewise exceeds the conditional result.

The endpoint-only `(BR-iso)` is indeed tautological **given a true seed**: it asks for exactly its endpoint conclusion. That explains why the printed bridge supplies no reduction. It does not prove that every quantitative transport theorem must assume the endpoint gap, or that all anisotropic constructions fail. REN also does not establish the asserted torus-seed equivalence. A one-way sufficient V1 path does not make that path necessary for V2.

**Replacement verdict:** “The strengthened route `(S-q)+(T)` is inconsistent because PERP-BD excludes the required diverging transverse length. Neither `(S-q)` nor an exhaustive matching argument has been proved for the Wilson region. The printed endpoint bridge supplies no mechanism beyond an open one-coupling clustering target. V2 remains an uncompleted proposal; its retirement by S0 is not proved.”

The K2/K3/K4/K6/K7/K8 and auxiliary rows of step 7 are scope/conditional-control bookkeeping. This check covers their use of `X`, the claim of no uniform pinned extension, and the absence of a bridge. It does not recheck their separately owned underlying lemmas or turn the five-dimensional numerical control into a theorem. No new attack is proposed. In particular, “no consumer for S” is not established; only the proposed direct diverging-length consumer is excluded **if `(S-q)` holds**.

Final checkpoint: source pin unchanged; all requested parts of row 1066 read. BARE's algebra, conditional PERP-BD, PERP and SU(2) S2 survive at the stated scopes. Open obligations remain `(MIX)` as printed, all-order uniform expansion including finite `beta_L`, calibrated two-parameter matching, a quantitative endpoint/continuum bridge, and universality. No registry, FINISH, source proof or audit file was edited. Access limits: original 1976 Brézin–Zinn-Justin and full Fröhlich–Spencer text not read; the exponent was checked against Zinn-Justin's open primary lecture equations. `pdftotext` was unavailable; PyMuPDF supplied text and page images. These extraction tools supplied no mathematical proof step.

RESULT: Row 1070 — HOLDS for conditional PERP-BD and finite-box PERP/SU(2) S2; BARE and the sheet-power calculation HOLD AFTER CORRECTION of scope; the mixing attribution, ratio formula, exhaustive matching, REN consumer identification and proved S0 retirement FAIL at the lines above. V2 remains OPEN as an uncompleted proposal; no mass gap or status is claimed.
