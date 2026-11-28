## Repo search

The dedicated prior note `prior/gap-hcphys-check-astra.md` is absent. I read the lead's general record `prior/repo-search-2026-11-08.md` in full. It covers November 8 obligations, not the later bridge/HC-phys claims. Its closest hits are:

- `origin/main:docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145`, read at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`: a supplied noncompact Dirichlet law and its Hessian/covariance comparison. Different law and metric; no bridge or HC-phys conclusion.
- PR 10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:100–153`: the opening argument for a positive one-step loop correlation, and a finite-energy comparison explicitly lacking a cutoff-uniform mixing consequence. Related transfer operator, different claim. The digest records the same source on PR 10133; it is not independent evidence.
- The digest's PR 10141 hits concern background operators and history bookkeeping; its PR 10134 search reports no closer result. Those unrelated sources were not reopened. This digest contains no prior check of the later CAP, TEL, EE or COUNT statements.

These are source comparisons, not an absence theorem over all branches. No entry for this check or HC-phys was found in `open-registry.md`. This is the explicitly requested cross-provider check, not a new attack on UNIT or another row's open problem. The local inputs are Theorem BR (`gap-fc-max.md:128–183`) and Lemma IHC (`gap-ladder-max.md`, checked below as an input/application). Credit their authors; neither is newly claimed here.

Provenance: OpenAI/Codex, configured model and effort; source commit `5d5d2f7b350f71450df4786adf43ff258a3d9688`. Research text, not an audit; grants no status. No numerical or computer-assisted proof. The requested filename is a lane identifier, not evidence of model identity.

Scope: `gap-hcphys-max.md` Lemmas CAP, TEL, EE, COUNT, Route 2(a), the crossed-channel identity, and (P1)–(P4) against `guide/lane982/SOURCES.md`. Author: Claude Fable 5.2 max. The earlier row-984 conclusions appeared in the queue search; they are not used as proof. Only this report is edited.

Completed work:

1. Finish the source/ownership search and pin cited ranges.
2. Check CAP against the bridge identities, including endpoints.
3. Check TEL and distinguish it from its proposed application.
4. Check EE and COUNT with their quantifiers and consumer implications.
5. Check Route 2(a) and the crossed channel.
6. Verify (P1)–(P4) in the account; write final verdicts and one RESULT line.

Downloads are confined to the fresh directory `/tmp/sa-gap-hcphys-check-astra.QLAoYp`. The outline, CA-I and CA-II were each fetched once at `31a47c543775`. Credit throughout: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Balaban for the operator work cited there.

## 1. CAP: the bridge identity and its interpretation

Source: `gap-hcphys-max.md:62–79`; objects and proof read at `gap-fc-max.md:46–53,128–200`. Put \(b=1/\beta\), and use the probability law
\[
 dJ_s(x,y,w)=Z^{-1}m(dx)g_s(x-y)g_{b-s}(y-w)m(dw)\,dy.
\]
Its endpoint marginals are \(\nu\), its middle marginal is \(\nu_s\), and \(u_s(y)=\mathbb E[f(W)\mid Y=y]\). Integrating out \(Y\) gives the one-step endpoint law. Thus
\[
 \mathbb E[u_s(Y)\mid X]=Pf(X),\qquad
 \mathbb E_{\nu_s}u_s=\nu(f),\qquad
 \|Pf\|_2^2\le F(s):=\mathbb E u_s(Y)^2\le\|f\|_2^2.
\]
Both endpoint Jensen inequalities and the mean-zero claim in L75 **HOLDS**. They do not reverse either conditional kernel. In particular \(\operatorname{Var}_{\nu_s}u_s=F(s)\) when \(\nu(f)=0\).

**CAP (a), L66,74: HOLDS**, given BR(ii). At \(q=2\), \(F'(s)=\mathbb E_{\nu_s}|\nabla u_s|^2\). Integrate on \([\varepsilon,b-\varepsilon]\) and use the displayed inequalities. Signed continuous functions cause no problem: translation by a constant preserves this derivative and the difference of the endpoint squared norms. The first excited eigenfunction is bounded and continuous: its eigenvalue is nonzero and it equals that eigenvalue's inverse times the continuous-kernel integral applied to itself.

**CAP (a'), L68: HOLDS AFTER CORRECTION** in the sense of supplying its omitted endpoint argument. This does not assume a posterior concentration estimate. Couple the middle variable as
\[
 Y_s=(1-s/b)X+(s/b)W+\sqrt{s(b-s)/b}\,\xi,
\]
with \(\xi\) independent standard Gaussian. At \(s\downarrow0\), \(Y_s\to X\) in probability; the quotient defining \(u_s\) converges uniformly on compact neighbourhoods of \(M\) to the smooth quotient at \(s=0\). Boundedness then gives \(F(s)\to\|Pf\|_2^2\).

At \(s\uparrow b\), \(Y_s\to W\) in mean square, since the endpoint variables are bounded. For a bounded Lipschitz function \(v\) on the ambient space,
\[
 \|f\|_2^2-F(s)
 =\mathbb E\operatorname{Var}(f(W)\mid Y_s)
 \le\mathbb E|f(W)-v(Y_s)|^2.
\]
Bounded Lipschitz extensions approximate any continuous \(f\) uniformly on compact \(M\): for example clip \(\inf_{x\in M}(f(x)+j|y-x|)\) to the range of \(f\), then let \(j\to\infty\). Fix such an approximation, take \(s\uparrow b\), then let the approximation error vanish. Hence \(F(s)\to\|f\|_2^2\). Monotone integration of \(F'\ge0\) now gives the asserted full energy identity.

**CAP (b)'s inequality, L70,75: HOLDS.** For normalized \(f_1\), \(F(s)\ge e^{-2E_1}\); therefore
\[
 e^{-2E_1}\int_0^b\gamma_s\,ds
 \le 1-e^{-2E_1}.
\]
The displayed cap follows. Zero rates are interpreted as the valid form \(\gamma_s\operatorname{Var}(\phi)\le\mathcal E_s(\phi)\), avoiding division by zero.

**The equality/comparability sentence in L70: FAILS.** The stronger BR-gap estimate follows directly from \(F'\ge\gamma_sF\):
\[
 \frac12\int_0^b\gamma_s\,ds\le E_1.
\]
Both bounds face the same way. They give no lower bound on the integral in terms of \(E_1\). The admissible choice \(\gamma\equiv0\) already refutes the claimed comparability for \(E_1>0\). Replace the sentence by this stronger one-sided bound. Accordingly L77's “of the order” is valid only for a bridge certificate **assumed to deliver** a fixed positive physical rate while \(E_1=Ma\); it is not a conclusion for every admissible \(\gamma\).

**CAP (c), L72: HOLDS.** For bounded centered \(g\), insert \(1+tg\) into LSI. Its entropy is \(2t^2\operatorname{Var}g+o(t^2)\), while its Dirichlet energy is \(t^2\mathcal E(g)\). This proves Poincaré with rate \(\alpha_s\). Thus both the claimed cap and \(A/2\le E_1\) hold, and \(A/2\le(2\beta_0)^{-1}\sup_s\alpha_s\) follows from the bridge length. In the stated Gaussian check, each half of the integral is \(\log(1+c/\beta)=\omega\), so the integral is \(2\omega\); its inequality is correct.

## 2. TEL

**Lemma TEL, L107–111: HOLDS**, for independent levels with the stated positive LSI rates. Tensorisation gives
\[
 \operatorname{Ent}(g^2)\le\sum_k\mathbb E\operatorname{Ent}_{\mu_k}(g^2)
 \le2\sum_k\rho_k^{-1}\mathbb E|\nabla_{A_k}g|^2.
\]
For completeness, the first inequality follows by iterating the exact two-variable entropy decomposition. Its second term is bounded by averaging conditional entropies in the other coordinate, since \(h\mapsto\operatorname{Ent}(h)\) is convex for nonnegative \(h\). That convexity follows from Cauchy–Schwarz: the second variation is \(\int v^2/h-(\int v)^2/\int h\ge0\). Thus no independence of the summands after applying \(f\) is assumed. Insert \(g=f(\sum_kD_kA_k)\); the chain rule gives \(\nabla_{A_k}g=D_k^T\nabla f\), exactly the matrix in L109. Approximation gives the usual extended-value statement when needed; a zero matrix means \(Y\) is deterministic.

**The proposed use at L113: HOLDS AFTER CORRECTION as a conditional benchmark only.** For independent Gaussian levels with covariances \(C_k\), the pushed-forward covariance is exactly \(C_Y=\sum_kD_kC_kD_k^T\). Linear test functions give an upper bound \(1/\|C_Y\|\) on any LSI rate. The displayed lower bound from TEL and this Gaussian upper bound agree in order **if** the asserted map norms and scale/coupling comparisons hold. No such maps, independence, or bridge-law identification follow from (P1)–(P3). Also use the full-action convexity rate \(\lambda_k\beta_k\), not the unperturbed precision \(a_-\beta_k\), unless the constant has been explicitly reduced (section 6 below). T3 and the roughness exponent are not established by TEL; this check does not reopen their separate lanes.

## 3. EE and the claimed hierarchy

The following uses the stated thermal trace with a simple vacuum, \(E_1>0\), and finite traces and first energy moments at the times used. These are the setting of L133, not conclusions about the continuum limit. Read input: `gap-ladder-max.md:119–150,195–201`.

| Statement | Verdict | Check |
|---|---|---|
| EE(a), L141: U1 implies U2 | **HOLDS** | Apply U1 directly to \(p_s(u,\cdot)\), then \(L^1\)-\(L^2\) interpolation with exponent \(\theta_m=2e^{-2\alpha_*m}/(1+e^{-2\alpha_*m})\), then Jensen in \(u\). The Hilbert–Schmidt norm squared is \(1+S(2s+2mT)\). This is IHC's argument with lag \(mT\); it does not require \(s/T\) to be an integer. |
| EE(b), L141,143 | **HOLDS** | \(X'=-U\le-\kappa aX\) gives \(X(\ell/a)\le X(\tau_0/a)e^{-\kappa(\ell-\tau_0)}\). Insert TH and compare with \(x_*:=\log(1+s_*)\). |
| EE(c), L141,143 | **HOLDS** | Integrate \((\log X)'=-U/X\). For the actual start value, the seed is equivalent to \(\int_{t_0}^{t_1}U/X\,dt\ge\log(X(t_0)/x_*)\). Replacing \(X(t_0)\) by its upper bound \(\Theta\) gives a sufficient condition, not an equivalence. |
| EE(d), L141,143 | **HOLDS** | \(U\ge E_1S/(1+S)\), \(X\le S\); for \(S\le1\), \(U/X\ge E_1/2\). Integrating from any time \(t_c\) with \(S(t_c)\le1\) gives the claimed bound. No assumption that the first such time is attained is necessary. |

**The hierarchy at L131 and the RESULT sentence at L274: FAILS as a claimed deduction from EE.** EE(a) proves U1 \(\Rightarrow\) U2. It does not prove that this contraction from one start yields the pointwise differential inequality U3. The exact identity in EE(c) concerns an **integral** of \(U/X\); a lower bound on that integral cannot be differentiated to obtain a lower bound on its integrand. No counterexample to the actual Wilson U3 is claimed here.

Correct replacement: U1 implies U2; U3 separately implies the seed under EE(b)'s size condition. On U3's stated interval it also gives
\[
 X(t_0+2mT)\le e^{-2\kappa aTm}X(t_0)
 \le[1-\tanh(\kappa aTm)]X(t_0),
\]
for integers \(m\ge0\) with \(t_0+2mT\le\ell/a\). It does not give U2 at times beyond that interval. Neither this proof nor the original EE identifies U1, U2 and UNIT as equivalent. Whether additional hypotheses give a reverse implication is outside this check.

## 4. COUNT

**COUNT(a)–(c), L145–151: HOLDS**, under the displayed hypotheses. For \(t>0\), each of the \(N(E)\) terms with energy at most \(E\) is at least \(e^{-tE}\). Thus \(\log N(E)\le tE+X(t)\). With \(C=2\Theta\), the function \(tE+Ce^{-M(t-\tau)}\) is minimized on \([\tau,\infty)\), for \(0<E\le CM\), at
\[
 t_*=\tau+M^{-1}\log(CM/E).
\]
Its value is exactly L147, including the endpoint \(E=CM\). At \(E=0\), the omitted separate statement is \(N(0)=1\). Part (c) follows termwise and in fact needs only \(t\ge t_c\) and finite \(S(t_c)\), not \(S(t_c)\le1\).

**COUNT's reading, L153 and L274: HOLDS AFTER CORRECTION.** It is an upper bound on state counts implied by a thermal envelope, not an equivalence with a gas model or with hypercontractivity. It makes no literal identification of states, dispersion, particle statistics, or phase space. A spectral count alone does not determine the eigenfunctions or their \(L^p\) norms, which HC reads.

There is also a time-domain qualification. COUNT(b) assumes the envelope for **all real** \(t\ge\tau\). U1 in this note supplies it only at \(t=\tau+2mT\), with \(M=\alpha_*/T\). To consume that grid estimate directly, choose the first grid time at or above \(t_*\). The valid bound is
\[
 \log N(E)\le E\tau+\frac EM\left(1+\log\frac{2\Theta M}{E}\right)+2TE,
 \qquad 0<E\le2\Theta M.
\]
Equivalently use the all-real envelope with prefactor \(2\Theta e^{2MT}\). The original exact COUNT(b) formula needs its stated all-real hypothesis; it does not follow with unchanged constants merely by saying “lengths in lattice units.” This qualification does not alter the lemma itself.

## 5. Route 2(a) and the crossed channel

**Route 2(a), L187–189: HOLDS.** Let \(Q=P^{2T}\). Reversibility and the even integer power make \(Q\) a positive semidefinite contraction. On a nonatomic probability space there are measurable sets with arbitrarily small positive measure. For \(f_A=\mathbf1_A/\sqrt{\nu(A)}\),
\[
 \operatorname{Ent}_\nu(f_A^2)=\log(1/\nu(A)),\qquad
 0\le\langle f_A,(I-Q)f_A\rangle\le1.
\]
This disproves every finite constant in the stated inequality on all of \(L^2(\nu)\). The vacuum law here has a positive continuous density relative to product Haar, so is nonatomic. This all-functions assertion should not be silently replaced by an assertion on an arbitrary restricted trajectory class.

The semigroup sentence also holds directly, without importing a log-Sobolev equivalence theorem:
\[
 e^{-\tau(I-Q)}=e^{-\tau}\sum_{j\ge0}\frac{\tau^j}{j!}Q^j
 \ge e^{-\tau}I
\]
on nonnegative functions. For \(1\le p<q\le\infty\), apply it to \(\nu(A)^{-1/p}\mathbf1_A\). The output \(L^q\) norm is at least \(e^{-\tau}\nu(A)^{1/q-1/p}\), which is unbounded as \(\nu(A)\downarrow0\).

**Crossed-channel identity, L211: HOLDS** for admissible **integer** lattice extents and one common partition-function normalization. Write \(X_{B'}\), rather than \(X'\), to distinguish the crossed logarithm from the derivative used in EE. With \(B=(2n)^3\) and \(B'=(2n)^2\times t\), the two trace identities for the same isotropic torus are
\[
 \log Z(B\times t)=t\log\lambda_0(B)+X_B(t)
 =2n\log\mu_0(B')+X_{B'}(2n).
\]
Subtracting gives exactly L211. Here \(X_{B'}=\log(1+S_{B'})\), not the unlogged excited thermal sum \(S_{B'}\). The identity does not extend by this argument to noninteger real \(t\), even though \(X_B(t)\) itself has a spectral definition there. It supplies no bound on either ground-state difference or the crossed thermal term.

## 6. Source check of (P1)–(P4)

All line numbers below refer to the downloaded texts at `31a47c543775`, not a later version. I used `sa-index/README.md`, the matching chunk-04 rows and neighbouring obligations, and the `ca-full` rows and their neighbours. For the operator theorem I also used `ca-4.12-4.19/README.md` and chunk-03:78–101 before reading CA-I. Index status labels are locators, not evidence.

The primary files are the [outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex) and [CA-II](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex). These are Ethan Sussman and Levent Alpoge's text, authored with Claude and Codex. The following is a faithfulness check of our port, not a validation of their full proofs or Balaban's papers.

### P1, L46: HOLDS AFTER CORRECTION

The quotation and local antecedent are accurate. CA-II 80152–80200 fixes the Euclidean bond metric, takes \(a_-I\le Q\le a_+I\) and exponential entry decay from the operator theorem, and states level/background/volume uniformity. CA-II 75164–75212 assumes \(Q(U,0)\ge\gamma_0/2\) and proves only the consequent inverse and Gaussian variance bounds.

The account-wide status needs correction. The source is also its **own** Theorem `4.14:thm-operator-theorem`, CA-I 46035–46156. Clause (B), 46076–46081, states the base-point and perturbed lower bounds; clause (I), 46122–46126, states uniformity. The source has an in-book proof, not merely a Balaban citation: 46170–46171 points to four lemmas; `4.14:prf-positivity-inversion` at 47686–47735 states and begins the positivity argument; 48132–48139 collects the conditional conclusion. I did not check that proof's full dependency closure.

Correct wording: **CA-II imports a conditional operator theorem developed in CA-I, drawing on Balaban; actual background admission remains an application hypothesis.** CA-I 49495–49546 expressly places the gauge-space supply outside that implication. Outline 3835–3862 likewise separates general fluctuation-fibre coercivity from the flat reference theorem and from a physical mass gap. Neither the outline's open package nor the index's `PROVED` label determines the status of every application.

### P2, L48: HOLDS for the metric conversion; HOLDS AFTER CORRECTION for the full-action constant

CA-II 80014–80050 defines free level-\(k\) bonds and a product of open convex norm balls of radius \(A_1(\log x_k)^{p_0}\). At 80039–80041 the unscaled fluctuation coordinate is \(z=g_kA\). Consequently
\[
 \operatorname{Hess}_z H(z/g_k)=g_k^{-2}\operatorname{Hess}_A H(A).
\]
Thus quadratic precision \(a_-\) becomes \(a_-\beta_k\). This is the Euclidean metric of these fluctuation coordinates on a four-dimensional region, not an identified fine-slice metric or an intrinsic group metric at arbitrary fields.

For the **full** exponent \(H=\tfrac12A^TQA+h^TA-P(A)\), the stated general bound is \(\lambda=\lambda_A-\varepsilon_0\), hence \(\lambda\beta_k\) in \(z\). Keeping the original \(a_-\) as the full-action rate omits \(P''\). It is legitimate to rename a smaller uniform positive constant, but that reduction must be explicit. The same correction applies to L54,113,225 and the RESULT's use of \(a_-\).

### P3, L50: HOLDS AFTER CORRECTION

The quoted definition at CA-II 81161–81186 is accurate: at zero weight, coercivity yields \(\operatorname{Hess}H\ge(\lambda_A-\varepsilon_0)I\). However, this proposition is an abstract comparison theorem. It assumes coercivity for \(H_0\) and explicitly assumes **no convexity** for \(H_1\) (81188–81190). Thus it alone does not establish “each small-field fluctuation law.”

For a member of the actual stated small-field class, cite the additional class conditions at CA-II 83840–83868: \(Q\ge\mathsf q_-I\), \(\|P''\|\le\varpi\le\mathsf q_-/4\), product convex windows, and the conditioning clause. They give
\[
 \operatorname{Hess}\Phi=Q-P''\ge(\mathsf q_--\varpi)I
 \ge\tfrac34\mathsf q_-I.
\]
This is a conditional strong log-concavity statement with the class's uniform constants. Keep membership and smallness as hypotheses; it does not apply to all comparison laws \(H_1\), to a mixture of histories, or to the fine bridge laws. No Bakry–Émery theorem is rebuilt or applied to an actual lattice law in this check.

### P4, L52: HOLDS AFTER CORRECTION to its scope

The listed results and their local qualifications match the source:

| CA-II range read | What the source actually supplies |
|---|---|
| 81161–81215 | Lipschitz comparison under the stated weighted coercivity hypothesis. |
| 81493–81536 | A two-sided **ratio of read-set marginal densities**, with its weighted derivative hypotheses. |
| 81804–81853 | Centered sub-Gaussian bounds for linear functionals, under zero-weight coercivity. |
| 83869–83905 | Correlation decay assuming the Helffer–Sjöstrand representation and the extra smooth-extension hypothesis, in addition to class membership. |
| 84178–84210 | The proof does not use a spectral gap of its Langevin generator or an inverse-Hessian variance inequality, and keeps the convex windows. |

The quoted “does not use” statement is accurate. It is not a theorem that no Poincaré inequality exists or can follow. In particular, **L225's broader “no ... Poincare” sentence: FAILS literally.** CA-I 47632 mentions a two-block Poincaré inequality and CA-II 135674–135690 explicitly states a one-dimensional one. Those are not physical transfer-gap estimates.

I repeated the case-insensitive `Sobolev|Bakry|hypercontract` search: no hits in CA-I and one in CA-II, at 133310 (a discrete Sobolev norm). The broader listed CA-II search has the four reported hits at 84184,84205,133310,135674. These results support **“no small-field LSI or hypercontractive theorem located in these CA-I/II passages and searches.”** They do not prove absence from the entire account; CA-III was not read. CA-I 2704–2712 explicitly excludes a mass-gap assertion. The assertion of a Bakry–Émery criterion remains a recalled external input and is not used here as a discharged step.

Scope limits: no audit, numerical run, new mass-gap attack, or source repair. This check does not validate BR's entire upstream construction, CA-I Theorem 4.14's proof closure, the actual-model hypotheses of IHC/TH, or Theorem ZD and its proposed equivalence with the HC route. UNIT, HC-phys, PQ-EX, TR-LF, T3 and the roughness exponent remain outside its proof claims. The source stays at the pinned commit; only this report is written. It is left locally on `codex/gap-hcphys-check-astra-20261115`, uncommitted and unpushed.

RESULT: HOLDS for CAP(a),(b),(c), both endpoint inequalities and the mean-zero identity, TEL on independent levels, EE(a)–(d), COUNT(a)–(c) under its stated time hypothesis, Route 2(a), and the crossed-channel identity on lattice tori; HOLDS AFTER CORRECTION for CAP(a')'s endpoint proof, TEL's proposed use, COUNT's reading/time-grid application, and the source scope/constants in (P1)–(P4); FAILS for L70's two-sided comparison, L131/L274's claimed deduction of pointwise U3 from the integrated decay, and L225's blanket Poincaré absence claim. Research check only; no status or mass gap granted.
