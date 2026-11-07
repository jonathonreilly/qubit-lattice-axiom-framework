# d4-budget: carried domains and two fixed radii
Provenance: Codex (GPT-6 family; assigned effort max; runtime variant and effort not exposed); checkout `6c5f42191c4ca23fce4672117033d43b709b0df7`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit; grants no status.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the cited constructions.
Balaban supplies the underlying background and response method.
This note addresses queue row 236, using rows 226 and 234.
All proof steps below are written mathematics.

## 1. Source check

The [YM4 outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) makes admission an input at L5813–5824.
It says: “Every occurrence of (R10) requires a domain-inclusion hypothesis”.
L6149–6157 also assumes stage inclusion for the spaces defined using preceding structures.
L17904–17918 sketches carriage using “the response and hereditary-domain estimates”.
The bracket argument at L5826–5855 is proved conditional on those inputs.

[QED3](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/QED3/QED3.tex) gives explicit conditional radius proofs.
L8723–8788 compares each additive contribution with its target threshold.
L9504–9546 obtains a contraction at most \(L^{-3/4}\) after scaling, including local gauge representatives.
These proofs supply a method, not the YM4 history invariant.
The root QED3 URL returned 404; the pinned GitHub tree supplied the path above.

The target is `loc-4.md` (4), including all earlier interpolation parameters.
One-move room does not imply this target.
`wf7-bf.md` Section 3 retains outer admission as an input for long members.
`gamma-bx-check.md` also retains (FG) and rejects Proposition I*'s promotion from half radii to full radii.

The additional passages do not remove those qualifications.
YM4 L17610–17630 compares real stage tests, including overlapping collars and the factor \(L_\flat^2/L^2\).
L17820–17838 and L18185–18204 concern later real evaluations compatible with stored fields.
They do not estimate independent complex corners of every defining composition.
[YM3_I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex), L48576–48658, proves strip transfer after assuming a ball in the member's domain.
Its proof sums the enlarged shifts before applying the logarithm.

## 2. The decay sum, with its hypothesis exposed

Fix a target level \(j\), one chart, and one clause \(a\).
Write \(d_{a,k}=\sup\|\mathcal R_a(Q_{k+1})-\mathcal R_a(Q_k)\|\).
The supremum includes the earlier parameters.
Suppose the **transported prefix increments** satisfy
\[
 d_{a,k}\le C_a r_{a,j}u_k\sqrt{1+k-j}\,L^{-(k-j)},\qquad k\ge j.
 \tag{5}
\]
If \(u_k\le u_*\), then
\[
 \sum_{k\ge j}d_{a,k}
 \le \frac{C_a u_*}{(1-L^{-1})^2}\,r_{a,j}.
 \tag{6}
\]
Indeed, \(\sqrt{1+n}\le n+1\) and \(\sum_{n\ge0}(n+1)x^n=(1-x)^{-2}\).
Thus \(C_a u_*<\epsilon_a(1-L^{-1})^2\) proves `loc-4.md` (4) under (5).
The bound is uniform in the number of prefixes.

Here is the source of the factors for one admitted response.
`ld-decoupled.md` (2), (5), and (6) give the weighted first-order bound on a fixed sequence.
`bx-fix.md` Lemma 0 adds the Hölder bound.
`wf-room-2.md` (6.4), with its check's corrections, bounds the assigned current.
Walk summation has already been done in these norms.
It must not be replaced by a volume count at each age.
The running radii satisfy \(a_{\iota,k}/a_{\iota,j}\le C\sqrt{1+k-j}\), as in (R18).
Changing units supplies these factors:

| Quantity | Factor for age \(n=k-j\) |
|---|---|
| Potential | \(L^{-n}\) |
| First difference and normalized curvature | \(L^{-2n}\) |
| Gradient Hölder seminorm | \(L^{-(2+\alpha_H)n}\) |
| Independent current | \(L^{-3n}\) |
| Inherited (R6) allowance under restriction | \(L^{-n}\) |

The last line follows directly from \(a_{0,k}L^{-(k-p)}=L^{-n}a_{0,k}L^{-(j-p)}\).
These factors justify a one-response majorant of the form (5).
They do not identify that response with an increment of a nested composition.

On a WF disc, \(|\nu_k|<c_\nu/s_k\) and \(\delta_k=s_k\alpha_k\).
Hence \((1+|\nu_k|)\delta_k\le(s_k+c_\nu)\alpha_k\).
This leaves the geometric factor in (5).
In contrast, enlarging **every** earlier multiplier to its full age-dependent (R11) radius cancels that factor.
The resulting upper majorant is constant per level and is not summable.
This is a failure of that majorant, not a divergent YM4 history.
R12 defines earlier carried terms at \(\nu=1\); their auxiliary Cauchy discs are not automatically independent stored parameters.
One must specify which discs a composition actually retains.

## 3. A fixed-chart budget, including outer long members

The following implication controls every clause on a single layer.
Retain Lemma T, the averaging bounds, and the Hölder estimates used in `loc-4.md` Section 4.
Fix one real factor and its witnessing local gauges.
Start with every clause below one quarter of its radius.
Let \(Q_{m+1}=Q_m\dotplus(h_m,q_m)\), with
\[
 b_m=\sup\bigl(\|h_m\|_{1,\alpha_H}+\|q_m\|_\infty\bigr),
 \qquad E=\sum_m b_m<c_*a_0.
 \tag{7}
\]
The bounds must hold on the auxiliary larger input domain, before admission is concluded.
The shifts must be jointly holomorphic in their retained parameters and input variables.
Assume \(a_0\le a_1\), \(a_1^2\le C_0a_0\), and the fixed smallness ceilings of Lemma T.
Then every prefix lies below half radii, for sufficiently small fixed \(c_*\).

**Proof.** The exponential and logarithm series give
\(\|A'\boxplus h-A'\|_{1,\alpha_H}\le C\|h\|_{1,\alpha_H}\).
The plaquette product gives \(\eta_j^{-2}\|\partial\mathbf U_{m+1}-\partial\mathbf U_m\|\le Cb_m\).
The current changes by \(q_m\).
Real-factor clauses do not change.
These estimates hold uniformly on the auxiliary domain with radii \((2a_0,2a_1)\).
Use ratio constant \(2C_0\) and the corresponding smaller ceiling on this auxiliary domain.

Fix any normalized tower quantity \(f\) from (R6).
For \(b_m>0\), Lemma T gives \(\|f(z)\|\le Aa_0\) for \(|z|<da_0/b_m\).
If \(b_m=0\), every quantity is unchanged.
Here \(A,d\) are fixed, independently of the tower.
Before a first exit, \(\|f(0)\|<a_0\).
Schwarz's lemma applied to \(f(z)-f(0)\) gives
\[
 \|f(1)-f(0)\|\le (A+1)b_m/d.
\]
Choose \(c_*\) so each accumulated change is less than one quarter of its radius.
Induction excludes a first exit.
This proves (4) for these compositions, uniformly over all towers.

The chart clauses have separate ceilings.
Let \(r_Q\) denote the uniform potential-chart radius supplied by the tower construction.
Choose the radii so the auxiliary potentials have norm below \(r_Q/2\).
Choose \(2C_{\rm AV}a_1<r_B/2\) for every tower datum.
The averaging derivative bounds each datum increment by \(C_{\rm AV}b_m\).
Decrease \(c_*\) so their sum is below the retained datum room.
Choose the absolute ceilings so every matrix entering a small logarithm satisfies \(\|Z-I\|<1/2\).
On this ball, its series has derivative norm at most \(2\).
Thus the logarithm increments also have a summable bound \(Cb_m\).
Lemma T supplies the background continuation throughout these auxiliary charts.
No continuation is inferred from endpoint agreement. \(\square\)

This also admits one outer long-member evaluation from a full regular input.
Use the running-radius floor of `wf-room.md` (4.1) and choose odd \(L\ge7\).
Restriction from level \(k+1\) to \(j\le k\) gives, with \(n=k+1-j\ge1\),
\[
 L^{-n}\frac{a_{\iota,k+1}}{a_{\iota,j}}
 \le L^{-n}\sqrt{1+n}\le(\sqrt2/L)^n<1/4.
 \tag{8}
\]
This includes inherited towers and the restricted real gauges.
The Hölder factor is smaller still.
On the full input domain, assume the named response and current bounds hold.
Retain the radius convention \(\alpha_k\le C_\alpha a_{0,k}\).
Then the outer WF shift satisfies
\[
 b\le C(s_k+c_\nu)\alpha_k L^{-(k-j)}\le C'(s_k+c_\nu)a_{0,j}.
\]
Choose \(s_k<c_\nu/2\) and \(c_\nu\) small enough for (7).
Every clause, continuation and logarithm chart is then admitted.
There is no dependence on the diameter of the long member.
Its activity tail, `wf7-bf.md` (5), can now be used.
That tail cannot replace (7).
At seams or stages, (8) must be replaced by the actual layer margin.

## 4. Where the all-history proof stops

The ordinary layer comparison is summable.
Put \(c^0_{t,p}=1-\beta_s(1-2^{-(t-p)})\), the phase-zero coefficient with no remade contribution.
Then \(c^0_{t,p}-c^0_{t+1,p}=\beta_s2^{-n}\), with \(n=t+1-p\ge1\).
A normalized response bound \(Cu\sqrt{1+n}e^{-D(n-1)}\) fits that gap if
\[
 \frac{Cu}{\beta_s}2^n\sqrt{1+n}e^{-D(n-1)}
 \le \frac{2\sqrt2Cu}{\beta_s}<1,
 \qquad D\ge\log4.
 \tag{9}
\]
Indeed, \(n+1\le2^n\) gives the displayed bound.
The coefficient gaps telescope, so their total expenditure is at most \(\beta_s\).
This is the conditional comparison in `wf-room-2.md` Corollary R and its check, Section 5.

A stage does not have that same gap.
At fixed \(t\), the phase contribution decreases by \(\mathsf g_t(p)/(2\mathsf N_t)\) per stage.
A newly recorded remade level \(l\) additionally costs \(\beta_R2^{-|p-l|}\).
The lift and the ambient layer can also change.
These statements follow by subtracting (R22); they do not estimate a substituted field.
They must be compared in one target chart, using both determining sequences.

The stage count alone gives no divergence.
On a waiting window, (R19) makes \(\theta_j\) comparable to \(\theta_t\) after increasing the fixed floor.
Indeed \(|\theta_j-\theta_t|\le \bar B\mathsf N_t+c_5\), and \(\mathsf N_t\le L(\log\theta_t)^r\).
The ratio \((\log y)^r/y\) tends to zero, since \(e^x\ge x^n/n!\) for any integer \(n>r\).
Thus even the crude count satisfies
\[
 \mathsf N_t^2\max_{t-\mathsf N_t\le j\le t}
       \frac{\delta_j}{\alpha_{0,j}}
 \le C(\log\theta_t)^{2r+\mathfrak p_0-q}\longrightarrow0
 \quad(q>\mathfrak p_0+2r).
 \tag{10}
\]
Equation (10) does not pay an unspecified chart loss or an unspecified phase gap.

The missing input is the stage version of (5) on the larger input domain.
Already for (R5), it must compare the two actual continuation data after transporting the earlier composition.
It must retain \(r_B\)-room for every preceding structure and both tower rules.
`ld-decoupled.md` proves a fixed-sequence response estimate; its hypotheses include admitted inputs.
`wf-room-2.md` Section 3 explicitly leaves compatibility with changed labels open.
Neither result supplies that transported stage increment.
The real estimates at YM4 L18185–18204 do not bound its independent complex parameters.
Assuming its existence while applying (9) would assume the required admission.

Scalar Gaussian logarithms require their own domain input.
`regional-gauss.md` (7) uses \(\|I-c^{-1}A_Y\|\le q<1\), uniformly in each region.
`gamma-bx-check.md` Section 4 leaves this input open for the lifted/stage cores and the consumed patch precision.
The group-logarithm estimate in Section 3 does not establish this operator inequality.
No actual history with divergent prefix increments has been obtained here.

## 5. The two-radius correction of Proposition I*

Fix the radii once, before induction.
Put
\[
 D_j^+=\mathcal U_j^H(a_{0,j},a_{1,j},a_{0,j}),\qquad
 D_j^-=\mathcal U_j^H(a_{0,j}/2,a_{1,j}/2,a_{0,j}/2).
\]
The induction must bound each old member on \(D_j^+\).
The smaller domain supplies room for evaluations and Cauchy estimates.
The output bound must hold on \(D_{k+1}^+\), with these same definitions.

**Corrected implication.** Retain (FG), the corrected BX package, UR, YA, and B4's other analytic inputs.
Require their response, chart and Gaussian estimates on the larger input domains.
For every \(P\in D_{k+1}^+\), require admission of every defining composition and Cauchy disc.
Base evaluations in \(D_j^-\), with a fixed collar in \(D_j^+\), suffice.
Incoming healed members must already have the required bounds on their larger domains.
Then B4's induction preserves the larger-domain bounds without shrinking the radii.

**Proof.** Fix an arbitrary \(P\in D_{k+1}^+\).
Every old member is evaluated inside its bounded holomorphic domain.
Put \(\underline a_j=\min_\iota a_{\iota,j}\).
The retained collar gives Cauchy bounds with fixed costs \(C_n\underline a_j^{-n}\).
Use Lemma B's augmented norm for the pair Taylor balls.
For other curves, use all clause margins; convexity of (H) alone is insufficient.
The corrected BX estimate and UR/YA therefore give (19) at this \(P\).
B4's remaining estimates give the new member bound there.
Their constants are uniform over \(D_{k+1}^+\) by hypothesis.
Composition and the stipulated normal convergence give holomorphy on that entire domain.
Thus the induction repeats with the same pair \(D^-,D^+\). \(\square\)

The regular single-layer admission hypotheses can be checked on the larger input domain.
For inner boxes retain (C), BG, T4, AX, AV and MS from `wf7-bf.md`.
Equation (8) puts the restricted input below one quarter of the old radii.
Choose the response ceiling so its clause expenditure is below one eighth.
The shifted outer pair is then below three eighths.
For an inner box pair, the two endpoint/gauge factors from `loc-4.md` give
\[
 (9/8)^2(3/8)=243/512<1/2
\]
for its curvature and hereditary clauses.
The datum estimate is \(\|B\|\le C_BM a_{0,\ell}\xi_j/\xi_\ell\).
The same radius comparison bounds \(a_{0,\ell}\xi_j/\xi_\ell\) by \(a_{0,j}\).
The fixed relation \(CMa_0\ll a_1\) admits its potential and Hölder clauses below half radii.
The absolute ceiling puts this datum below \(r_I\) and retains the logarithm charts.
This includes outer long members through Section 3.

In `bx-fix.md` Lemma 2, replacing the half input by the full input only doubles its input bounds.
Its five proof steps still give \(a_{\rm out}\le C_M(\alpha_k+\alpha_{0,k+1})\), with an enlarged fixed constant.
Retain (FG) for the Hessian identities and node-gauge equality.
Enlarge the fixed young-age range when the half-datum condition fails.
The old-age condition and the node-gauge smallness ceiling remain explicit.
These changes do not shrink either domain with the step number.

This does not verify the implication's hypotheses at every layered or stage input.
At a same-layer young window, the factor in (8) is absent.
Repeating the printed inner proof from a full-radius starting bound gives \((9/8)^2>1\), even before adding a shift.
That failed estimate is not a counterexample to admission.
It identifies the layer margin that a full repair must supply.
Simply doubling both named radii reproduces the same failure at the next step.

## Result

**Correction of our text, with two conditional proofs.**
Equations (5)–(7) prove a summable fixed-chart budget from uniform transported response bounds.
Section 3 admits single-layer outer long-member evaluations under the stated larger-domain response inputs.
Section 5 gives the non-shrinking two-radius induction with its larger-domain hypotheses explicit.
It does not establish those hypotheses for the complete carried family.

**The requested all-history budget (4) remains open.** No divergent actual history is proved.
**First input still open:** a uniform stage estimate for the transported (R5) continuation datum on the larger core.
It must cover every earlier parameter, changed determining sequence, and preceding-structure chart, with its actual (R22) margin.
The assigned current, stored-data transport, and scalar logarithm domains must then satisfy the same budget.
(FG) remains a separate input to Proposition I*.
This is neither a proof of the outline's sketched all-history admission nor a counterexample to it.
The new arguments have not been independently checked.
