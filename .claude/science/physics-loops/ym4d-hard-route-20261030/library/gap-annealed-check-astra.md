# Repo search

The target-specific prior file is absent. The supplied `prior/repo-search-2026-11-08.md` concerns earlier obligations; it contains no annealed block-chain theorem. The task row adds no named repo hits. The source's row-821 literature digest is reused as background; row 853 owns the new literature search.

I refreshed main (`bb4ec020d5ad`) and PRs #10114 (`f76f6c649cff`), #10133 (`89faef229ff6`), #10134 (`1e70c7211a2c`), #10141 (`fb99b4dddc72`), and #10144 (`1f20846b8057`). The targeted query was `annealed.{0,30}(block|response)|stationary.{0,25}(coupling|heat.bath)|gap-annealed`, on Markdown/TeX outside this lane and audit records. The four requested PRs had exactly main's ten matching lines. The relevant hits checked were:

| Source read | Closeness |
|---|---|
| Main, `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:1–8,79–94` | Supplied finite-clock Villain law; covariance/masslessness, not this Wilson block criterion. |
| Main, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | Noncompact Dirichlet Maxwell covariance; different law and operator. |
| PR #10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | One-step transfer witness, not a uniform block heat-bath gap. |
| Main, `docs/COMPACT_ROTOR_BRIDGE_CUBIC_BOUNDED_THEOREM_NOTE_2026-09-16.md:105–130,165–188`; `docs/FINITE_CLOCK_GAUSSIAN_SMOOTHING_POSITIVE_LOCAL_ELECTRIC_EXTENSION_AND_FLUX_SCALING_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-15.md:374–432` | Existing stationary Langevin couplings and parameter derivatives under uniform convexity; useful method precedent, not AN1 or its repeated-update issue. |
| This lane, `gap-blockcrit-opus.md:116–154,297–309` | Claude Opus 5.5's direct antecedent: quenched block criterion, Villain obstruction and Gaussian exit response. Reused, not claimed as new. |

No duplicate of this check was located. Registry searches found no competing owner; its annealing matches H-C6c/H-C8a concern RG-history removal/source bounds, not this chain. This is a scoped search, not an absence theorem.

# Statement checks

Provenance: OpenAI Codex, configured gpt-6-astra/xhigh checker; source commit `d7a3a22a9e9a6d6485df28693d11e86d041535c6`. This is a research check, not an audit, and grants no status. Source author: Claude Opus 5.5/max. All source line numbers below refer to `library/gap-annealed-opus.md` at that commit, SHA-256 `3ea756939fd9eb71fbe7bb45752c963d1b53a7018275c337b454bff05200047e`.

Only this report is edited. No numerical computation discharges a step. The GUIDE calibrations, optimal fields, an order-one Wilson application, the seed comparison, and the full imported Villain proof are not being certified. The source's desired conclusions were present in the dispatch; independence here rests on the arguments below, not provider identity alone.

Checkpoint: all requested statements checked, AG first. The conversion implication survives. Literal AN1 equals an essential worst-case exterior condition; nontrivial pure-exterior SP-ext is impossible. The next mathematical decision is whether to replace AN1/P3 by conditions only on surviving paths. The path-sum replacement is sufficient, but no model-specific supplier for it is proved here.

## 1. Theorem AG (a)–(d): HOLDS

Checked lines 58–120, including Lemmas P1 and PE. This verdict is for the implication from the **literal** (AN1)–(AN2). It does not validate the claim that (AN1) avoids worst-case exteriors; see section 3 below.

**Tangent propagation / Lemma PE: HOLDS.** The exact response identity (2.2) gives a positive kernel on configurations and link labels. Its stay term is `Gamma_a(|grad_j h|)` and its jump term is `Gamma_a(R^a_jc |grad_c h|)`. Thus the jump field is evaluated at the **new** block configuration. Composing these kernels gives (3.2) by the Markov property. No differentiation of R and no pathwise differentiable coupling are needed. A measurable field satisfying (2.1) and the stated integrability suffices. AN1 supplies the necessary first and mixed moments. Replacing the terminal derivative by its supremum occurs before applying AN1, so no unjustified independence of that derivative is used.

For each fixed block schedule, every intermediate law is mu: each conditional expectation separately preserves mu. Stay indicators are then deterministic. Every remaining factor is one of AN1's distinct-time jumps. With `T = I - N/|A| + K/|A|`, the resulting entrywise bound is

`mu(|grad_e P^t f|) <= [T^t d(f)]_e`, where `d_i(f)=||grad_i f||_inf`.

AN2 is exactly `w^T T <= q w^T`. Positivity gives (a). The matrix orientation at line 114 is correct: the incoming column is bounded, not the outgoing row.

**L¹ block Poincare / Lemma P1: HOLDS.** The geodesic occupation measure on the unit S³ is rotation invariant. Its mass is the mean geodesic distance, pi/2, by antipodal symmetry of the scalar product. Coordinate replacement under product Haar gives the sum of gradient norms. Jensen first bounds mean deviation by the two-copy integral. If `p=|P_a|`, then `e^(-2 beta p) <= rho <= e^(2 beta p)`. Two upper density factors and one lower density factor give precisely `(pi/2)e^(6 beta p)`. This uses beta >= 0, as in the Wilson coupling convention; use |beta| if extending to negative beta. The same occupation argument works on a unit circle.

**Spectral step: HOLDS.** For smooth f, P1 and (a) give

`||(I-P)P^s f||_1 <= [c_1 n_max/(|A| w_min)] q^s Delta_(inf,w)(f)`.

The telescoping series therefore converges in L¹. Its limit is bounded and P-fixed. Since P averages orthogonal conditional projections, a P-fixed function is fixed by every Gamma_a. AN2 forces the blocks to cover E. Equivalence of mu and product Haar then makes the function constant: under Haar the commuting block integrations together integrate every coordinate. The constant is mu(f). Consequently

`||P^t f-mu(f)||_1 <= [c_1 n_max/(kappa w_min)] q^t Delta_(inf,w)(f)`.

Multiplication by the bounded sup norm yields the source's variance bound `C(f)q^t`. If a centred spectral measure had positive mass above `sqrt(q)+eta` in absolute value, its `2t`-moment would eventually exceed this bound. Density of smooth functions removes that interval for the whole centred subspace. Hence `|A|(1-sqrt(q)) >= kappa/2`, proving (b). The case q=0 gives `P f=mu(f)` directly and causes no division by zero. Here `0 <= q < 1` follows from AN2 and `n_e <= |A|`.

**Langevin comparison: HOLDS.** Conditional block Poincare and `sum_a |grad_(B_a) f|² <= n_max |grad f|²` give (c). For completeness, if a probability density lies between m and M relative to Haar, minimizing over the centring constant gives `Var_gamma f <= M Var_Haar f <= M/(3m) gamma(|grad f|²)`. Thus the stated `3e^(-4 beta p)` is valid. Its slack does not affect the claim.

**Clustering: HOLDS.** For real bounded g, the tilted law has density at most 3; g=0 is immediate. Only blocks meeting Y contribute to the telescoping difference. P1 costs `3c_1` there. The symmetric resolvent is `n^(-1) sum_m (K/n)^m`. There are at most n contributing blocks per starting link, column sums are `alpha_AN^m`, and finite range forces `m >= m_0`. Undoing the tilt costs at most `3||g||_inf`. This gives exactly `9c_1 alpha_AN^m_0/(1-alpha_AN)`. Use the usual value 1 for the zero-step factor when alpha_AN=0. Complex observables follow by complexification or component bounds if needed; the written tilt uses real g.

The constants are uniform only when their named inputs are uniform. No order-one Wilson criterion or transfer-matrix seed is supplied by this theorem.

## 2. Lemma T (i)–(iii), Corollary T1: HOLDS

Checked lines 29–54 and the block geometry in `gap-blockcrit-opus.md:43–58`. On the compact product of spheres, the density bounds give coercivity on centred H¹ functions by the Haar Poincare inequality. The bilinear form `gamma(<grad u,grad v>)` therefore has a unique centred weak solution for the centred smooth source. Elliptic regularity makes it smooth. Uniqueness makes its dependence on v linear. Integration by parts gives (2.1), with the sign printed in the source.

The solution also depends smoothly on the exterior. One can invert `-L_y + Pi_y`, where `Pi_y` projects onto constants, on fixed Sobolev spaces. This operator has trivial kernel, and local inversion of its smoothly varying coefficients gives smooth parameter dependence. Compactness of the exterior and the unit tangent bundle then bounds the Poisson response fields. This supplies PB's qualitative kmax; it supplies no explicit small number.

For a vertex block, internal gauge transformations preserve the block density and its metric and leave the exterior fixed. They preserve h and commute with L_y. Uniqueness makes phi invariant; its gradient annihilates each internal orbit direction. Differentiating the normalized integral gives the direct derivative plus the covariance. Taking the supremum over v gives T1.

At line 35 the sum defining h should run over plaquettes meeting B_a as well as containing j. Adding plaquettes wholly outside B_a changes h only by a sigma-independent constant, which cancels from both the covariance and centred Poisson equation. No conclusion changes.

## 3. Lemma Q: HOLDS; the claimed annealed weakening FAILS

Checked lines 64–78 and 144–150. Q's backward conditioning is valid: after bounding the final factor by a deterministic k, the remaining product is adapted to the earlier history. Iterating proves AN1. The comment that the argument works only at the last jump means one must remove that jump first; it is not an obstruction to the iteration.

There is also a converse, absent from the source. Fix one block a and one pair (j,c), and set

`r(y) = gamma_a(R^a_jc(.,y)|y)`.

Choose the deterministic schedule `a_1=...=a_m=a`, with this same jump at every time. AN1 permits it: it quantifies over arbitrary distinct-time jumps, not just composable label paths. The exterior Y is unchanged. Given Y, the m refreshed blocks are independent samples from gamma_a(.|Y). Therefore

`E[prod_(s=1)^m R^a_jc(U_s) | a_1=...=a_m=a] = mu_ext(r(Y)^m) <= (k^a_jc)^m`.

For any delta>0, a set of positive exterior probability p on which `r >= k+delta` would give `p(k+delta)^m <= k^m` for every m, an impossibility as m tends to infinity. The k=0 case follows already at m=1. Hence

**AN1 is equivalent to `r(y) <= k^a_jc` for mu_ext-almost every y, for every (a,j,c).**

The reverse direction is Q; null sets remain null along a fixed stationary schedule. For the smooth Poisson fields, r is continuous and the Wilson exterior law has full support. The essential supremum is then the actual supremum. Thus AN1 is exactly Q's quenched-exterior criterion for these fields. A rare open set of large conditional responses receives no discount.

This also gives a different check of AG's spectral step, using the existing quenched method of row 836. T1 and `gamma_a(R|y)<=k` give a deterministic sup-gradient inequality `d(Pg)<=T d(g)`. This holds first almost everywhere and then everywhere because Gamma_a g is smooth and the exterior law has full support. Iteration yields `Delta_(inf,w)(P^t f)<=q^t Delta_(inf,w)(f)`. Coordinate geodesics have length at most pi, so for centred smooth f, `||P^t f||_inf <= (pi/w_min)q^t Delta_(inf,w)(f)`. Hence `<f,P^(2t)f> <= ||f||_1 (pi/w_min)q^(2t) Delta_(inf,w)(f)`. The spectral support is at most q in absolute value, giving the stronger block gap kappa. Thus the printed kappa/2 bound is sound; its factor of two is unnecessary under literal AN1. This is a reuse of the quenched contraction argument, with round distance in place of chord distance, not a new annealed theorem.

First failed interpretation: lines 78 and 122, “no uniformity over exteriors,” if meant as a weaker hypothesis than Q. The equivalence does not refute AG. It refutes the advertised annealed improvement and the proposed source of order-one improvement at lines 227 and 249. Block averaging may still improve other older, more restrictive estimates; that is a different comparison.

A possible repair is to assume only the path-sum bounds actually used in AG, as suggested at line 76. Such paths cannot repeat the jump j→c under successive updates of a: after landing in c inside B_a, the next such update kills the path. The repaired condition is different from AN1. No Peierls supplier for it is proved here.

## 4. Proposition PB: HOLDS; nontrivial SP-ext as written FAILS

Checked lines 154–164 and 180–189. P1–P3 imply AN1 by the displayed subset expansion. For nonnegative kg and kmax, deleting the good indicators gives the bound `prod_i(kg_i+eps kmax_i)`. No independence is used. In the symmetric setting summing these numbers gives exactly `alpha_g+eps alpha_max`. The Poisson choice has a finite kmax by section 2 above.

But the proposed **pure exterior** application has a decisive obstruction. Suppose `Bad_a` depends only on the exterior and has stationary probability p>0. Set every update in a schedule of length m equal to a and select all m times. The exterior never moves, so the left side of P3 is p for every m. P3 would require `p <= eps^m` for every m. This is impossible for eps<1.

Thus SP-ext at line 184 cannot hold with eps<1 for any positive-probability exterior bad event under its stated quantifiers. It is not merely a missing estimate. The two-time observation at line 182 alone is insufficient when p<=eps²; arbitrarily many repeated updates give the unconditional obstruction. An exterior-null event is the trivial exception. Taking eps>=1 gives no useful rare-event gain: whenever `alpha_g+eps alpha_max<1`, already `alpha_max<1`, a pointwise sufficient coefficient.

More generally, for mixed block/exterior badness put `p_a(y)=gamma_a(Bad_a|y)`. The same repeated schedule gives `mu_ext(p_a(Y)^m)<=eps^m`. Consequently P3 is equivalent, up to exterior null sets, to `p_a(y)<=eps` for every a; the reverse is FR. This exact P3 is a worst-case conditional badness bound. A criterion charging distinct space-time regions or only surviving label paths would require a new statement and proof.

## 5. Lemma FR: HOLDS

Checked lines 166–168. Conditional on the complete block schedule, the update noise at time s is still sampled from its block conditional law. Earlier bad indicators are measurable before the last selected time. Its conditional probability is at most eps. Remove that time and repeat. This proves P3 for arbitrary selected times. No independence of the exteriors is asserted or needed. Together with the preceding converse, FR already describes the full strength of literal P3, modulo null sets.

## 6. Theorem LW: HOLDS

Checked lines 193–203. Let `D_e=|grad_e g|`. For e outside B_a, `|grad_e Gamma_a g|` is exterior measurable. Thus weighting it by W_e under mu is exactly equivalent to weighting it by Gamma_a W_e. The latter is nonnegative and exterior measurable. Multiplying T1 by it and using the defining conditional-expectation identity gives

`mu(W_e |grad_e Gamma_a g|) <= mu((Gamma_a W_e) D_e) + sum_(c in B_a) mu((Gamma_a W_e) R^a_ec D_c)`.

The second sum occurs only for e in Ev(a). Collecting the coefficients of D_c gives exactly Phi_c in (LW); no misplaced conditional expectation remains. Hence `Delta_W(Pg)<=q Delta_W(g)`.

LW also forces coverage. If c belongs to no block, integration of its inequality gives `|A|mu(W_c) <= (|A|-kappa)mu(W_c)`, impossible. Since bounded W>=1 controls all unweighted L¹ gradients, P1 and the spectral argument in section 1 apply. The factor ||W||_inf changes a finite-torus prefactor, not the spectral rate. The printed block and Langevin constants follow.

The informal cycle claim at line 207 is not a consequence of this proof. LW contains `Gamma_a(W_e)(U)`, not W_e(U), so weights do not telescope around a cycle at one configuration. A cycle obstruction would need a separate bound relating those conditional averages to point values. Keep that discussion as an unproved heuristic; it establishes no impossibility result for LW.

## 7. Lemma N (i)–(iv): HOLDS

Checked lines 172–178. In (iii) and (iv), alpha_AN has the symmetric meaning fixed at line 74, and “one such observable” retains the unit-gradient bound of (ii).

One jump in AN1 gives (i). More precisely than (ii), an observable supported on C inside B_a satisfies

`sum_j mu(|grad_j Gamma_a O|) <= sum_j sum_(c in C) mu(R^a_jc)`

when each indicated gradient is at most one. There is no direct exterior derivative because O is a block observable. Taking C=B_a gives (ii). Taking the disjoint singletons C={c} and summing gives (iii), without multiplying the entire right side by |B_a|. Taking the disjoint four-link plaquettes gives (iv). The real quaternion product has unit norm, so its scalar-part derivative in any one unit tangent direction has absolute value at most one. Finally `L/|B_a|=1/4` gives the displayed factor.

For invariant block observables the exterior-gradient terms of GQ vanish. The same inequalities hold with R'; this does not make the ignored exterior gauge-jump coefficient zero in AG'. GUIDE observations are neither these exact expectations nor upper bounds for them.

**Auxiliary Lemma H: HOLDS AFTER CORRECTION.** At line 170, Holder with m factors (padding by 1 if necessary) is valid because every configuration has law mu even after fixing the schedule. As m increases the norms converge to the **essential** supremum, not necessarily the pointwise supremum for the allowed measurable fields. They coincide for the continuous Poisson fields. H alone gives no single finite-m bound for all lengths.

## 8. Lemma GQ: HOLDS; Theorem AG': HOLDS AFTER CORRECTION

Checked lines 126–140. The sign in GQ is correct. Gauge invariance gives `grad_B g dot zeta_B + grad_ext g dot zeta_ext=0`, hence `grad_B g dot xi = grad_B g dot (xi+zeta_B) + grad_ext g dot zeta_ext`. This is a pointwise identity even for configuration-dependent zeta; no derivative of zeta is being taken.

The gradient, block-gap and Langevin-gap conclusions of AG' hold. Gauge covariance of every block conditional expectation keeps P^t f invariant. In the path expansion, keep block jumps, gauge jumps and stays as labelled alternatives. This includes a gauge self-jump j→j separately from the stay indicator. Expanding those alternatives uses at most one response factor per time. The matrix is exactly `M'=|A|I-N+K+K''`. The weighted column inequality gives contraction. Smooth invariant functions are dense in the invariant subspace by compact-group averaging, so the same spectral argument proves the restricted gaps.

The clustering clause must use the **total** response matrix. Correct line 136's reference to AG(d) as follows:

> In the symmetric case, require the augmented coefficients to have constant column sum `n alpha_tot`, where `alpha_tot = |B|^(-1)[sum_(j,c) k^a_jc + sum_(j,e) k''^a_je] < 1`. Require range at most r for both types of jumps. Then (3.3) holds with alpha_tot and this r, for invariant f.

The old definition at line 74 counts only block jumps. It cannot be left unchanged in the clustering formula when K'' is present. The resolvent is `n^(-1) sum_m ((K+K'')/n)^m`; both its column sum and its propagation distance read K''. This is the first missing change in the proof at line 138. With the displayed correction the calculation in AG(d) is valid, including self-jumps. The gap conclusions and constants need no correction.

## 9. Theorem UA: HOLDS, conditional on the named Theorem V

Checked lines 231–239 against `gap-tu-retry.md:61–101,333–345`. The imported theorem concerns the exact periodic Villain law here, the unit-circle metric, the gauge-invariant Langevin gap, all sufficiently large integer sides including odd sides, and the full limit at each fixed beta>=2^14. This check reuses that result; it does not recheck its covariance/score proof or the earlier checker's verdict. The method behind that input is credited in the source to Jurg Frohlich and Thomas Spencer.

Let `l=min phi_beta>0`, `u=max phi_beta<infinity`, and let p bound the number of plaquettes meeting a fixed block. The unnormalized density lies between l^p and u^p. Its normalized density lies between `(l/u)^p` and `(u/l)^p`. Haar on a product of unit circles has gap 1, so density comparison gives the uniform conditional gap `c_* >= (l/u)^(2p)>0`. The circle occupation proof gives the analogous finite L¹ constant. Thus AG applies with all these constants independent of M.

For a fixed generated shape, n_max is bounded independently of M. If AN held along unbounded M with a fixed margin kappa, it would imply `gamma_V(beta;M)>=kappa c_*/(2n_max)>0`. Theorem V excludes that subsequence. This is precisely the quantifier “for every fixed kappa, eventually no such criterion,” not failure of every arbitrarily small M-dependent margin on every finite torus.

The symmetric second clause follows already from the first: `alpha_AN<=alpha<1` gives the fixed margin `n(1-alpha)>0`. No further score-correlation argument or range assumption is needed for that implication. The named obstruction is AN2 for coefficients satisfying AN1; no tangent or spectral step fails for the circle model. The Gaussian “mechanism” at line 241 remains heuristic for Villain and is not needed for UA.

## 10. Proposition GFF-AN: HOLDS AFTER CORRECTION of its domain

Checked lines 243–247 against `gap-blockcrit-opus.md:306–309`. The earlier source specifies Z^d and finite blocks. The conditional response calculation is correct. The new statement must retain a defined Gibbs probability and the minimum-weight hypothesis; “every weights” cannot silently assert that an arbitrary weight function on Z^d attains a minimum.

A precise version sufficient for this check is:

> Let mu be a Gaussian Gibbs probability on Z^d with the displayed nearest-neighbour specification, and let the blocks be finite. Assume the local transport fields are integrable and satisfy (2.1). At every site x* attaining the global minimum of the positive weights, the stated upper bound for kappa holds, provided the block incidence sums there are finite. For m=0, it excludes a positive margin. This includes constant or positive periodic weights for a proper massless GFF in d>=3. For m>0 the same calculation holds on a finite torus. The massless finite-torus version is a coefficient calculation for proper block conditionals, not a statement under an unnormalized torus density.

The last distinction is necessary: at m=0 the finite periodic energy is unchanged by adding a constant to every field, so its integral over the constant mode is infinite. Conditioning that mode to zero changes the block conditionals. Pinning boundary sites can introduce absorption and also changes the blanket massless conclusion. Neither modification is supplied in the note. No such issue arises for the stated infinite-volume GFF example in four dimensions.

Here is the calculation, retaining the earlier Gaussian result rather than redoing its construction. The conditional mean solves the discrete Dirichlet equation

`(2d+m²) mean_x = sum_(z~x, z in B_a) mean_z + sum_(y~x, y outside B_a) phi_y`.

Following a walk until it exits or is killed gives the nonnegative kernel H_a. Thus `sum_y H_a(x,y)=1-rho_a(x)`. Testing the transport identity with phi_x gives `gamma_a(xi_x|y)=H_a(x,y)` for a unit perturbation at exterior site y. If only compactly supported tests are admitted, truncate phi_x with bounded-gradient cutoffs. Integrability of the field and Gaussian moments justify the limit. Therefore `gamma_a(|xi_x||y)>=H_a(x,y)` and `mu(R^a_yx)>=H_a(x,y)`. AN1 with one jump gives k>=H.

At a minimum-weight site x*, every exterior weight is at least w_x*. Consequently the incoming coefficient is at least

`w_x* sum_(a contains x*) sum_y H_a(x*,y) = w_x* [n_x* - sum_(a contains x*) rho_a(x*)]`.

Comparing this with AN2 proves the displayed margin bound. For m=0 a walk exits a finite block almost surely: in a finite block there is a fixed positive chance of exit within a fixed finite number of steps, and iteration makes indefinite survival probability zero. Thus rho_a=0 and kappa<=0. This verifies the intended massless coefficient test, without importing a finite-torus massless probability that does not exist.

## 11. Remaining claims, sources and scope

The weakened averaged-path premise at line 76 **HOLDS** as a sufficient replacement: the proof of AG(a) uses exactly the sum of those nonnegative path products. This is the candidate repair identified in section 3, not something literal AN1 already says.

The “no ceiling from CEIL” statement at line 191 **HOLDS** in its limited logical sense. `gap-blockcrit-opus.md:264–270` bounds one particular single-site walk construction; it does not bound all possible block transport fields. Our converse to Q does not identify optimal transport fields with that construction. The small-beta existence argument at line 213 also holds for a fixed covering family: smooth parameter dependence of the Poisson inverse and h=0 at beta=0 give a uniform `R<=C beta` on its compact local parameter space. Finite incoming counts then give AN2 for sufficiently small beta. No numerical threshold follows from the value of C left unspecified there.

Theorem UA's summaries at lines 272 and 284 must retain its **fixed positive margin** quantifier. The theorem excludes a volume-uniform margin for a fixed finite shape. It does not assert the absence of every volume-dependent positive margin on each finite torus. Its claim about a one-point spin-wave obstruction at line 241 is a heuristic, not a consequence of Theorem V.

The GUIDE table and beta-window discussion were read, not validated as probability estimates. No run was made. No Wilson gap at beta of order one, no mass gap in a continuum theory, no seed comparison and no novelty claim is established here. The full upstream Villain covariance theorem is an explicit reused premise of section 9, not a new check result.

**Sussman–Alpoge prior work.** The outline README, matching chunk rows and neighbouring rows, and obligations were used before source excerpts. Searches for `heat.bath|Dobrushin|annealed|Villain|Glauber|Helffer` found no such outline-index target. The mass-gap/scalar-gap scope rows in chunks 01 and 29 and obligations led to outline lines 588–599, 770–780 and 31871–31882. The scalar constrained gap is a different operator; the physical mass gap remains separate. CA-I index searches, including `ca-4.12-4.19/`, located no heat-bath target. The full-account index's three “annealed” titles are in CA-II and concern RG histories; those proofs are not imported or judged here. The CA-I source's scope at 2698–2712 and 3215–3225 likewise does not assert a mass gap. These bounded checks locate no prior proof of the present conversion; they are not a claim about every differently named result in the account.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, for those source distinctions and the indexed account. Both requested TeX files were fetched once from revision `31a47c543775`, into the new directory `/tmp/sa-gap-annealed-check-astra.odoPw3/`. Search outputs and source hashes are retained there. No Balaban estimate is imported in this check, and none of Tadeusz Balaban's papers was needed or copied. Claude Opus 5.5 is credited for the checked source and its block-criterion antecedent; the separate literature map remains the work of its named Codex author.

The configuration was not changed. The session approval policy is `never`; no escalation was requested. Only the requested report is a repository change. No registry, FINISH row, science status, source proof or external post was changed.

| Requested statement | Verdict |
|---|---|
| AG (a)–(d), including P1 and PE | HOLDS |
| T (i)–(iii), T1 | HOLDS |
| Q | HOLDS |
| PB | HOLDS |
| FR | HOLDS |
| LW | HOLDS |
| N (i)–(iv) | HOLDS |
| AG' | HOLDS AFTER CORRECTION of clustering coefficient/range |
| UA | HOLDS, given Theorem V |
| GFF-AN | HOLDS AFTER CORRECTION of probability/weight domain |

RESULT: Theorem AG and its conversion steps HOLD, but literal AN1 is equivalent to an essential worst-case exterior bound, and nontrivial pure-exterior SP-ext with eps<1 FAILS under repeated block updates; AG' needs the total gauge-jump coefficient for clustering, GFF-AN needs its probability/weight domain stated, and no order-one Wilson gap is established; the path-sum-only repair still lacks a model-specific supplier.
