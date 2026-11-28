# H-O: carrier oscillations at creation

Codex, 2026-11-08. Original note at `8f3484ab9`; revision based on checkout `e0b244c62`.
Research text. Not an audit. Grants no status. This revision is not independently checked.
No computation supplies a proof step.

**Result: stop (c), at supplier lemma HC-WEIGHT after three routes.**
Y 73373–73652 already supplies an absolute kept-change sum on its common admitted complex range.
Section 4 gives the two-complex-pair implication and the constant order.
The Claude check found a separate gap in its collar input, \(b_V\).
Y 73843–73868 sketches that input; Y 73660–73758 proves an unweighted total instead.
Section 4A states the remaining positive weighted sum and gives the three failed routes.
The anchored-disc algebra is sufficient if that sum is supplied. It does not supply the sum.
Thus \(b_V\) remains open within H-O. No actual-history counterexample was found.
Full-domain substitution room remains `D4-CARRIED`, owned by DOM.
Admission of later island reads remains H-E, whose registry owner is none.
This is not an unconditional proof of IN1 H-O or a counterexample to an actual history.

## 1. Target and prior work

The target is IN1 (18), with oscillation defined by IN1 (8):

\[
 \sum_{f:R_f=R}\sup_{\xi,P,P'\in\mathcal K_{t,X}}
 |\Phi_{\omega,f}(\xi;P)-\Phi_{\omega,f}(\xi;P')|
 \le B_\Phi\ell_t^{2p_0}
       e^{-\kappa d_t^\natural(\mathcal S;R)},\qquad
 \ell_t=\log\theta_t.
 \tag{1}
\]

Here the supremum over \(\xi\) means \(\xi\in S_\omega\).
Both pairs vary independently on the fixed complex creation domain.
The stored variables agree in the two evaluations.
The constant \(B_\Phi\) precedes the coupling ceiling.

The requested `prior/ho-collar.md` is absent at this checkout.
The H-O row of `prior/lfi.md` and `gates/lfi-ho-check.md` were read before this attack.
The digest identified the absolute kept-change sum as the first hard step.
Section 3 already ports that sum. The quadratic budget is also existing work.
The check corrects the digest's treatment of the collar budget: its per-carrier form is still open.
The action-of-averages proof in `sa-2.13-2.md` §6 is also existing work.
None is re-derived here.

The registry assigns H-O no other owner. FINISH row 515 assigns this collar continuation.
The original note was row 499; its Claude check was row 508.
Composition room belongs to DOM. Later island admission belongs to H-E.
General formation and common integral envelopes remain their existing inputs.

Credit throughout: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Bałaban supplies the large-field method and kept-factor construction used by that text.
The source abbreviations are:

- **Y:** [YM4_1400.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex), commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
- **SA:** [YM4_sketch_500.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), commit `31a47c543775`.
- **I:** [theorem_0_complete_account_raw_I.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), at the same commit as SA.

The local `sa-index` supplied the SA and I locators.
External files were already present at the requested paths. Reads used bounded excerpts.

## 2. Port ledger

“Proved there” below retains the source's hypotheses. It does not supply an actual-history antecedent.

| Premise or step | Source and standing | Use here |
|---|---|---|
| Two complex pairs, fixed stored variables, fixed creation domain | SA 6265–6314; definition and required bound. Y 1420–1446 repeats it. | Exact target (1). |
| Hereditary core, independent current, gauges and all tower clauses | SA 5663–5736; definitions and domain requirements. | Small curvature alone does not define the domain. |
| Tied exponent and real quadratic reference | Y 73208–73262; construction and required tie. | Apply complex estimates to the tied reader. |
| Analytic main-step quadratic and its absolute walk bound | Y 73264–73354; proved on the admitted glued datum, using the stated walk and response inputs. | Existing quadratic budget. |
| Pinned substitution and kept-member difference estimate | Y 73373–73559; the Schwarz estimate is proved on the admitted disc. | Port the actual difference, conditional on that disc's supply. |
| Disc inclusion from the profile comparison | Y 73508–73556; **SKETCHED**. | Its full carried-composition application remains (11a). |
| Rooted absolute sum of kept changes | Y 73561–73652; proved from the member majorants and prepared geometry. | Reuse this sum with its exact domain. |
| Pair reader and quadratic correction | Y 73778–73839; proved on the common formed core, with prepared Wilson estimates and tie. | Preserve the prescribed exponent and its carrier. |
| Total collar majorant | Y 73660–73758; proved on the common admitted range. | Gives \(C_{\rm col}(1+\bar c)N_0\), without per-carrier decay. |
| Birth allocation | Y 73843–73909; the per-carrier collar step is **SKETCHED** and the conclusion is stated as real oscillation. | The numerical allocation is reusable; \(b_V\) needs its own proof. |
| Two kept members on an orbit chart | I 84503–84678; conditional on the listed KH inputs. | This does not by itself bound the sum over prescribed carrier factors. |
| Later stage-total and fixed-number conclusions | I 87328–87381 and 88187–88221; explicitly incomplete. | These do not remove the domain or carrier-sum inputs. |

## 3. The absolute sum already supplied by Y

Fix one actual finite history and its stored variables.
Keep its original masks, pivot factors, stored coordinates and carrier multiplicities.
Write \(\mathfrak C_\omega\) for the common admitted range used in Y 73373–73652.
This includes the output complex triples, cube parameters and enlarged spectator discs used there.
It is not defined here to equal IN1's creation domain.

The source's anchor \(q(\xi)\) uses the stored inner rows and identity exterior rows.
It is independent of the output pair.
For a kept member with original carrier \(R\), the actual difference is

\[
 \delta_R(\xi;\mathfrak z)
 =T_R^1(\xi;\mathfrak z)-\varphi_R(q(\xi)|_R).
 \tag{2}
\]

Y 73387–73465 constructs the anchor and formed datum.
Y 73466–73555 constructs the pinned substitution \(\mathfrak S_R(\lambda)\).
Both the potential and current increments are multiplied before levelling.
The target retains the original stored pins.
For

\[
 u_R=(h_t-1-n_R)_+,\qquad Q=4L^8,
 \qquad
 a_R=C_*\ell_t^{-(q-p_1-r/2)}Q^{-u_R},
 \tag{3}
\]

the supplied disc has radius \(2/a_R\).
Its centre reads \(q(\xi)|_R\). Its endpoint reads the actual kept factor.
Here \(q\) in the exponent denotes the radius exponent, not the anchor map.

The source proves, by Schwarz on that disc,

\[
 \sup_{\mathfrak C_\omega}|\delta_R|\le a_R b_R^\sharp.
 \tag{4}
\]

This is Y 73557–73559. Its supremum is complex.
It is not obtained by extending a real bound through qualitative holomorphy.
The source sketches target-domain admission at Y 73508–73556.
Using (4) on the full creation domain requires the quantitative supply in (11a), despite that sketch.
The island part of the spectator bound additionally requires H-E, as in (11b).

Y 73561–73584 supplies the member majorant after removing stored-only constants.
Island members use their inherited oscillation bounds.
Strip members use their quadratic walk sums and the full pivot logarithms.
Splitting a member into copies also splits its bound.
Thus the sum of copy bounds does not increase.
The source's exponents are

\[
 p^\sharp=2p_0+12r+2,\qquad \sigma=9r+p^\sharp.
\]

Y 73586–73640 counts roots at their own levels, including the drop-out delay.
It proves

\[
 \sum_R b_R^\sharp Q^{-u_R}
 \le K_A' B_\Phi^\sharp
       \ell_t^{p^\sharp+13r}(1+\log\ell_t)^\sigma.
 \tag{5}
\]

The old-level count contributes \(L^{4p}\).
The anchored response contributes \(Q^{-p}\), apart from the recorded delay.
The source sums those factors before returning (5).
There is no new genealogy count here.

Combining the source's (4) and (5), as Y 73642–73652 does, gives

\[
 \begin{split}
 \sum_R\sup_{\mathfrak C_\omega}|\delta_R|
 &\le C_A B_\Phi^\sharp
       \ell_t^{2p_0-\epsilon}(1+\log\ell_t)^\sigma,\\
 \epsilon&=q-p_1-\tfrac{51}{2}r-2,\qquad C_A=C_*K_A'.
 \end{split}
 \tag{6}
\]

The supremum is inside the sum. This distinction is essential.
The power in (6) is exactly the source's \(5r+E+12r+2\),
where \(E=2p_0+p_1+17r/2-q\).
The source's stronger mass choice \(E+12r+2<0\), together with \(p_0>6r\), implies \(\epsilon>0\).

This locates the estimate omitted from the digest's H-O source ranges.
It ports an existing complex estimate on its stated range.
It does not identify that range with every point of IN1's fixed domain.

## 4. Exact implication for two complex pairs

Assume the supplied formation maps place every allowed \((\xi,P)\) in the range of Section 3.
Retain every source premise: the prepared geometry, response bounds, original target spaces,
absolute strip majorants, pivot charts and incoming island bounds.
Retain the tie: all admitted triples representing one pair give the same prescribed factor value.
This is the input used at Y 73248–73252 and 73404, not a consequence of a size estimate.
Also retain the collar and quadratic bounds specified below on that same full domain.
These are hypotheses of this implication.

For two independent complex pairs \(P,P'\), the anchor in (2) is the same.
Consequently

\[
 \begin{split}
 \sum_R\sup_{\xi,P,P'}
 |\delta_R(\xi;P)-\delta_R(\xi;P')|
 &\le 2\sum_R\sup_{\xi,P}|\delta_R(\xi;P)|\\
 &\le 2C_A B_\Phi^\sharp
       \ell_t^{2p_0-\epsilon}(1+\log\ell_t)^\sigma.
 \end{split}
 \tag{7}
\]

The first inequality holds term by term, before summing.
Every amplitude supremum includes all admitted triples representing the indicated pair.
The tie identifies their values; it does not admit any missing triple.
It allows the maximizing stored variables and pairs to differ between factors.
It requires neither a path from \(P\) to \(P'\) nor a common real splitting.
Both evaluations use the same pair-independent anchor for their fixed \(\xi\).

The output assignment is the one in Y 73887–73892.
Every \(\delta_R\) is formed through the full island reader in Y 73466–73559.
Each therefore has output carrier \(R_*=X^\sim\).
The new quadratic has that carrier too.
Its hull length in the output label is zero.
Thus (7) bounds the required sum of their individual oscillations on \(R_*\).
It does not replace that sum by the oscillation of their total.
The smaller collar carriers retain their original decay.

Use the tied pair reader of Y 73778–73839:

\[
 -\tfrac12\theta_t q_{0,X}^\natural(f;P)
 +V_X^{\rm col}(P)+\sum_R\delta_R(P)
 +\tfrac12\theta_t(q_{0,X}^\natural-q_{0,X})(f),
 \qquad f=g_tB.
 \tag{8}
\]

The stored-only trunks have been placed in \(\Phi_\omega^\circ\).
Equation (8), with those trunks, preserves the original exponent.
Use the source's tied grouping as the actual pair factors.
An auxiliary summand containing the real reference form need not descend separately to the pair.
Its amplitude estimate is used uniformly over all admitted splittings, inside that grouping.
The nonnegative real reference quadratic is not substituted for a holomorphic pair factor.

The source budgets used here are as follows.

- The required anchored collar bound is
  \(b_V\ell_t^{2p_0}e^{-\kappa d_t^\natural(\mathcal S;R)}\) per output carrier.
  Its constant is independent of the inherited island constant.
  This is the allocation in Y 73843–73868, using its single-term collar bound.
- The quadratic and displayed correction have total complex amplitude at most
  \(C_QA_1^2\ell_t^{2p_1+5r}+C_Q\).
  This uses Y 73264–73354 and 73778–73839, with the size allocation at 73878–73886.
  Twice this amplitude bounds their oscillation.

The second statement uses the admitted glued datum and the prepared Wilson estimate.
The first retains the single-term collar estimate as an input.
Neither statement follows from an integrated mass bound.

The following constant choice completes the implication.
Write \(B_\Phi^\sharp\le C_{\rm strip}+C_{\rm isl}B_\Phi\).
Such fixed constants follow from the strip/island split defining \(b_R^\sharp\) in Y 73561–73584.
Fix \(B_\Phi\ge\max\{1,2b_V\}\) before the coupling ceiling.
Use the source exponent gaps

\[
 \epsilon>0,\qquad \eta=2p_0-2p_1-5r>0.
 \tag{9}
\]

For this implication, impose explicitly at **IN1 row 1**
\[
 q>2p_0+p_1+\tfrac{41}{2}r+2,\qquad
 p_1<p_0-\tfrac52r.
 \tag{9a}
\]
The first inequality is the source's \(E+12r+2<0\).
It gives \(\epsilon>2p_0-5r>0\), since row 1 also requires \(p_0>6r\).
The second gives \(\eta>0\).
IN1's broad row-1 choices permit these inequalities but do not state them explicitly.
They are extra explicit requirements of this implication, before choosing the coupling ceiling.
Only this note is edited; IN1 itself is unchanged.
Now choose \(X_0\) so that, for every \(\ell\ge\log X_0\),

\[
 \begin{split}
 2C_A(C_{\rm strip}+C_{\rm isl}B_\Phi)
       \ell^{-\epsilon}(1+\log\ell)^\sigma&\le B_\Phi/4,\\
 2C_Q(A_1^2\ell^{-\eta}+\ell^{-2p_0})&\le B_\Phi/4.
 \end{split}
 \tag{10}
\]

This is a written existence choice.
For the first limit, put \(y=\log\ell\) and choose an integer \(n>\sigma\).
The inequality \(e^{\epsilon y/2}\ge(\epsilon y/2)^n/n!\) proves the required decay.
The other two powers decay because their exponents are positive.
Hence (10) holds on a whole tail, uniformly in the history and level.
Set \(\gamma=X_0^{-1/2}\) only afterwards.

The collar spends at most half of (1).
The kept changes spend at most one quarter by (7) and (10).
The quadratic pieces spend at most one quarter.
Their sum proves (1) for a newly formed island under the stated inputs.
For a standing island, restriction preserves its old creation-domain bound.
Finite ancestry then propagates the same \(B_\Phi\), starting from the bare presentation without islands.
There is no additional summation over ancestors in this last step.

## 4A. Collar continuation: the weighted primitive sum

The three parts of \(V_X^{\rm col}\) are fixed by Y 73655–73659.
They are the localized action difference, the small Wilson sum, and the Wilson weight correction.
The kept changes \(\delta_R\) are separate. They cannot pay for a second copy of a collar term.
Cancel matched trunks first, as Y 73660–73673 requires.
Keep the prescribed carriers, masks, coefficients and multiplicities.
Moving a smaller carrier to \(X^\sim\) would change this task.

**The carrierwise analytic reduction.** Put \(R_s=e^{\bar\kappa}\).
Index the primitive collar reads by \(e\), including their prescribed copies.
Let \(K\) be their differenced switch cubes; their fixed switch cubes are understood.
Write \(R(e,K)\) for the actual output carrier, including every read mask.
This is the carrier supplied by the construction, not merely the support of a kernel.

For an anchored old read, write its holomorphic evaluation as \(F_e(s,\lambda;\xi,P)\).
Assume (11a) and all its required bounds on
\[
 |s_\Delta|<R_s,\qquad |\lambda|<2/a_e,\qquad 0<a_e\le1.
\]
Assume \(F_e(s,0;\xi,P)=A_e(s,\xi)\), independent of \(P\).
Let \(M_e\) bound \(|F_e|\) there, after removing stored-only constants.
The bound is uniform over stored variables and all admitted triples representing \(P\).
Every numerical copy weight is included in \(M_e\).

Schwarz gives \(|F_e(s,1;\xi,P)-A_e(s,\xi)|\le a_eM_e\).
Use the same anchor for both independent complex pairs.
Apply the exact cube-bracket estimate of Sussman and Alpoge, SA 5827–5859.
For the localized bracket \(H_{e,K}\), this gives
\[
 \operatorname{osc}H_{e,K}
 \le 2a_eM_e(R_s-1)^{-|K|}.
 \tag{C1}
\]
Indeed, the anchored difference has supremum at most \(a_eM_e\) on the switch polydisc.
The Cauchy difference kernel contributes \((R_s-1)^{-1}\) for each differenced cube.
The triangle inequality for two pairs contributes the factor two.
The anchor may depend on \(s\); its bracket is still independent of \(P\).
Its subtraction here is only an estimate, not a change of the prescribed factors.

A fresh primitive with bound \(M_e\) needs no anchoring gain.
The same estimate holds with \(a_e\) replaced by one.
Denote these respective weights by \(w_e=a_e\) and \(w_e=1\).
Stored-only primitives contribute zero and are omitted.
Assume the actual localization groups these brackets into the actual collar factors, without extra copies.
Triangle inequalities, before either supremum or carrier sum, then give
\[
 \sum_{f:R_f=R}\operatorname{osc}v_f^{\rm col}
 \le 2\sum_{e,K:R(e,K)=R}
        w_eM_e(R_s-1)^{-|K|}.
 \tag{C2}
\]
This is a two-complex-pair statement. A real bound has not been continued by assertion.
The tie and the actual bracket identification remain required.

**Supplier lemma HC-WEIGHT — open.** On the supplied common complex domains, identify the prescribed collar factors with the brackets in (C2).
Prove that those actual primitives admit bounds satisfying
\[
 \sup_{\omega,t,R}\;
 \ell_t^{-2p_0}
 \sum_{e,K:R(e,K)=R}
 w_eM_e(R_s-1)^{-|K|}
 e^{\kappa d_t^\natural(\mathcal S;R)}
 \le C_{\rm HC}<\infty.
 \tag{C3}
\]
Here \(\mathcal S\) is the output label used in (1).
The constant precedes the coupling ceiling and is independent of the inherited island constant \(B_\Phi\).
It may depend on the earlier ordinary-entry, response and geometric constants.
The primitive bounds must cover all three collar parts just listed, with their actual subtractions and net weights.
Assume the corresponding composition domains have been supplied as in (11a); island spectator bounds require (11b).
No missing domain is included in the claim of this supplier lemma.
The bound must be uniform in the cutoff, torus, depth and admitted histories.

This is a positive majorant estimate, stronger than an oscillation estimate of a summed function.
It retains the output length while summing the native roots and switch extensions.
Equations (C2)–(C3) would prove the requested collar bound with \(b_V=2C_{\rm HC}\).
The choice \(B_\Phi\ge2b_V\) in Section 4 would then be valid.
No value of \(C_{\rm HC}\) is supplied here.

**Route 1: the prescribed anchored discs.** Apply (C1) before summing old roots.
For the kept reads, Y supplies \(a_e=C_*\ell_t^{-(q-p_1-r/2)}Q^{-u_e}\).
Its count pays \(L^{4u}\) with \(Q^{-u}\); without delays the ratio is \((4L^4)^{-1}<1\).
Y 73586–73640 also treats the delays and proves (5).
Those estimates already give (6), so they are not re-derived.
For the collar, however, (C3) retains the additional factor \(e^{\kappa d_t^\natural(\mathcal S;R)}\).
The kept argument files its whole-reader changes on \(X^\sim\), where this factor is one.
Y 73887–73892 does not make it one for the smaller collar carriers.
The depth discount alone supplies no relation between \(u_e\) and that output length.

For a precise test of that inference, fix \(0<a\le1\) and set
\[
 F_n(\lambda,z)=\tfrac a2\lambda z,
 \qquad |\lambda|<2/a,\quad |z|<1.
 \tag{C4}
\]
Its anchor is zero, its disc supremum is one, and its endpoint oscillation is \(a\).
Assign the endpoint to a carrier of length \(n\).
Its weighted oscillation is \(ae^{\kappa n}\), which is unbounded.
One may take \(a=C_*\ell_t^{-(q-p_1-r/2)}Q^{-u}\) at fixed \(t,u\).
Thus even the exact amplified radius cannot replace an output-length estimate.
This is a counterexample to that analytic inference, not to an actual collar construction.
Route 1 stops at the weighted root sum (C3).

**Route 2: restrict the proved total collar majorant to one carrier.**
Y 73660–73758 gives
\[
 \sum_\lambda\sup|v_\lambda^{\rm col}|
 \le C_{\rm col}(1+\bar c)N_0(\omega).
 \tag{C5}
\]
Restricting its positive sum gives a bound for any selected carrier, but leaves \(N_0(\omega)\).
It gives neither a uniform birth-scale power nor an output-length weight.
The source counts ordinary roots using \(z_j(X)\) and then sums over \(j\).
Fixing a carrier after that summation does not recover the spent length decay.

For example, take two independent unit-disc variables at the ends of a path of length \(n\).
The single function \(v_n(z_0,z_n)=(z_0+z_n)/2\) has supremum one and oscillation two.
Its connected carrier must span the path. Take that path to contain no exempt hull.
It satisfies (C5) with \(N_0=n+1\) and constant one.
For fixed \(\ell_t,b_V\), it violates \(2\le b_V\ell_t^{2p_0}e^{-\kappa n}\) at large \(n\).
This tests only the implication from (C5); it is not an actual-history counterexample.
The Wilson estimates at Y 73707–73754 and their net weights retain this same limitation when used only as totals.
Route 2 therefore does not prove (C3).

**Route 3: localize with the complete read set before doing the root count.**
Sussman and Alpoge give this argument for a fixed bond read at Y 63044–63158.
Its actual hypotheses include the full datum masks, a bounded read star, and component locality.
With a base of \(n_e\) cubes and \(n=|K|\), its geometric inputs have the form
\[
 d_t(R(e,K))\le c_h(n+n_e),\qquad
 \#\{K:|K|=n\}\le C_e e^{c_{\rm ent}n}.
\]
Consequently the same positive sum is bounded by
\[
 \sum_K e^{\kappa d_t^\natural(\mathcal S;R(e,K))}
       w_eM_e(R_s-1)^{-|K|}
 \le
 \frac{w_eM_e C_e e^{\kappa c_hn_e}}{1-\rho},
 \qquad
 \rho=\frac{e^{c_{\rm ent}+\kappa c_h}}{R_s-1}<1.
 \tag{C6}
\]
This ports their geometric series; \(d_t^\natural\le d_t\) justifies its use here.
For bounded read stars it preserves the required length weight.
Now fix the output carrier \(R\) before summing primitives.
Let \(\mathcal E_R=\{e:R(e,K)=R\text{ for some }K\}\).
Use the same estimate at rate \(\kappa+\tau\), with fixed \(\tau>0\), and put
\[
 \begin{split}
 \rho_+&=\frac{e^{c_{\rm ent}+(\kappa+\tau)c_h}}{R_s-1}<1,\\
 S_R&=\sum_{e\in\mathcal E_R}
          w_eM_e C_e e^{(\kappa+\tau)c_hn_e}.
 \end{split}
\]
Then the positive sum required by (C3), before division by \(\ell_t^{2p_0}\), is at most
\[
               \frac{e^{-\tau d_t^\natural(\mathcal S;R)}}{1-\rho_+}S_R.
 \tag{C7}
\]
This keeps the carrier fixed. It does not ask for a uniform total over all output carriers.
For example, a bound \(S_R\le C\ell_t^{5r}(1+d_t^\natural(\mathcal S;R))^m\), with fixed \(m\), would suffice.
Exponential decay absorbs that polynomial, and \(5r<2p_0\).
But Y 73675–73703 supplies the unweighted root count, not this bound for \(S_R\).
The bond-read theorem also does not bound \(S_R\) for history-dependent bases and masks.
In particular its \(C_e\) depends on the bounded read star.
Replacing it by a history-independent constant for a growing base is not justified.

The native ordinary-domain comparison in SA 19445 can help pay this base cost.
It compares \(d_j(X)\) with \(d_t(\widehat X)\), with no added layer.
It does not state the same comparison for arbitrary changed exempt families and complete added read masks.
This distinction cannot be erased: if a long region \(H\) is exempt, \(d_{j,\{H\}}^\natural(H)=0\).
After that exemption is removed, its coarse image can have arbitrarily large tree length.
This follows directly from the definition at SA 6191–6198.
It is a test of a general metric inference, not a claim that such an unmatched hull occurs in an actual history.
Actual preparation may exclude it; that exclusion must enter the count with the prescribed carriers.
The rate list SA 17999–18009 supplies available margins, not this matched-carrier assertion.
Thus (C6) handles a bounded read, and (C7) is the remaining carrierwise root-count test.
Neither establishes (C3) for the full collar roster.

These are three routes to the same supplier lemma, not three independently verified failures of the Yang–Mills construction.
The CA alternative does not supply it: I 84503–84586 concerns two whole kept members and assumes its potential bound in KH1.
I 88187–88221 still assumes that bound and labels its later proof incomplete.
The source-difference estimate at Y 80704–80748 also uses the whole island carrier; its length is zero.
None gives the positive weighted sum for the prescribed smaller collar carriers.

**Recovery checkpoint.** First prove HC-WEIGHT for that actual roster, retaining the output weight before native-root summation.
Use the original masks and track the exempt hulls through the output carrier assignment.
Do not repeat (5), the unweighted collar count, the fixed-bond bracket theorem, or the quadratic budget.
The conclusion here is stop (c): HC-WEIGHT is unproved after the three routes above.
It is not a no-go theorem, a proof of \(b_V\), or a refutation of an actual history.

## 5. Separate admission inputs

Full-domain composition admission is separate from the collar estimate.
For every history, every \(\xi\in S_\omega\), and every \(P\in\mathcal K_{t,X}\),
the actual maps must produce the source's admitted datum and spectator values.
For each kept member they must also supply

\[
 \mathfrak S_R(\lambda;P,s,\xi)\in D_R^{\rm original}
 \quad\left(|s_\Delta|<e^{\bar\kappa},\quad |\lambda|<2/a_R\right),
 \tag{11a}
\]

with the same stored pins, original masks and pivot charts.
The value at \(\lambda=1\) must be the actual kept read.
All defining compositions must be admitted, not only their final pair.
The required amplified radius is exactly
\[
 \varrho_R=\frac{2}{a_R}
 =\frac{2}{C_*}\ell_t^{q-p_1-r/2}Q^{u_R}.
 \tag{11r}
\]
It grows like \(Q^{u_R}\). A fixed radius greater than one does not suffice.

This is an application of the existing D4 contract, not a new proposed supplier lemma.
`loc-4.md` §5, lines 150–161, requires precisely full input-domain admission,
stored arguments, gauges, logarithm charts, all compositions, a finite supremum and quantitative amplified radius.
`src-array.md` lines 222–226 retains that condition for the carried maps and healing gauges.
The registry row `D4-CARRIED` assigns it to **DOM**.
Equation (11r) specifies what that supplier must return for this consumer.
`DOM-FULL` also retains actual roster coverage and input membership in `dom.md` line 359.

The last clause of the former (11) was a second input.
For every island member, on the same spectator and substitution range, require
\[
 \text{its actual inner read}\ \in\mathcal K_{i,Y}^{\rm birth}.
 \tag{11b}
\]
Its inherited bound then applies on its own fixed creation domain.
This is **H-E later admission**, not H-O and not a reassignment to DOM.
SA 6305–6310 separates this inclusion from the creation bound; IN1 line 186 requires it expressly.
The registry owner of H-E is **none**.

Y's inclusion argument at 73508–73556 is a sketch, not an absent argument.
It does not supply every defining carried composition on a separately fixed creation domain.
`src-array.md` line 225 separates profile estimates from their domains.
The scalar composition example in `loc-4.md` §5 shows why one-move room cannot supply all mixed corners.
Its exterior-strip application, Y 63569–63677, explicitly uses a served target and its supplied profile gap.
Its local walk theorem, Y 32043–32176, also retains history admission for the prescribed separation.
Neither permits changing the creation domain after inspecting the kept terms.

The CA operator theorem does not remove this issue.
I 49495–49546 expressly leaves the expansion's background inclusion and later drop-out spaces outside its implication.
The two-member lemma in I assumes its sourced-set bounds and admitted families.
Its incomplete stage-total continuation cannot establish (11a) or (11b).

`sa-2.13-2.md` §7 likewise leaves the full complex remainder bound open on the actual prepared/inner substitutions.
Its existing action and normalization estimates do not supply these domain statements.
Neither owned composition admission nor H-E is attacked in this collar continuation.

## 6. Status table

| Claim | Status |
|---|---|
| Exact two-complex-pair consumer and fixed birth domain | **Ported from SA 6265–6314**, and IN1 (8), (18). |
| Actual anchored kept difference on an admitted amplified disc | **Ported from Y 73373–73559**. The algebra is conditional on disc supply. |
| Inclusion on the amplified disc | **SKETCHED in Y 73508–73556**; open as (11a), `D4-CARRIED`, owner DOM, with radius (11r). |
| Absolute sum with supremum inside the sum, equation (6) | **Ported from Y 73561–73652**. |
| Two-complex-pair inequality (7) | **Proved here**, conditional on full-domain supply of (6). |
| Full-reader carrier \(X^\sim\), with zero exempt hull length | **Ported from Y 73887–73892**; retain its actual assignment. |
| Tied quadratic reader and correction | **Ported from Y 73264–73354 and 73778–73839**, on the admitted glued datum. |
| Total collar majorant (C5) | **Ported from Y 73660–73758**, on the common admitted range. It has no per-carrier decay. |
| Carrierwise Schwarz–Cauchy reduction (C1)–(C2) | **Conditional implication**, using SA 5827–5859 and the actual localization. No full-roster weighted estimate follows. |
| **First open input: HC-WEIGHT, (C3)** | **Open within H-O, FINISH row 515**. Three routes in Section 4A did not prove it. No separate registry row is created. |
| Per-carrier collar constant \(b_V\) | **Open**. It would equal \(2C_{\rm HC}\) if HC-WEIGHT held. Y 73843–73868 sketches the allocation only. |
| Prepared geometry, response, strip majorants, original pivots, tie and incoming class bounds | **Inputs** to the ported estimates. No general actual-history supply is claimed here. |
| Budget allocation with \(B_\Phi\) fixed before \(\gamma\) | **Proved here**, as the implication in Section 4. |
| Full creation-domain composition admission (11a) | **Open — `D4-CARRIED`, owner DOM**. This consumer requires \(2/a_R\), growing like \(Q^{u_R}\), not merely a radius greater than one. |
| Later island reads in their own creation domains, (11b) | **Open — H-E later admission, owner none**, SA 6305–6310; IN1 line 186. |
| H-O for the actual IN1 construction on every fixed creation domain | **Open**. HC-WEIGHT, (11a), and (11b) remain distinct required inputs. |

The Claude findings are applied here; this continuation has no new Claude check.
Only `library/lfi-ho.md` is edited. No editable prompt file, registry, gate or source manuscript is changed.
