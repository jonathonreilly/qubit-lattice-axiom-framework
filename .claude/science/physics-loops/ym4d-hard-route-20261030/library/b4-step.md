# B4: the complex small-field step (rows 172, 177)
Provenance: Codex (GPT-6 family; exact serving variant and runtime effort not exposed; requested effort max); row 177 at `a09e72326c8a86898546f75dcd038d13c02ccd4f`, continuing row 172 at `b1388bfbddc5c20f5ccb2e7fbb14a0560ebfcafe`; Sussman–Alpoge source `31a47c543775`. Research text, not an audit; no status granted.

## 0. Check of Claude's `wf-c.md`, Sections 2–4

**Lemma C and Corollary CC: ADVANCE, as implications from their stated inputs.**
Checked line by line by Codex, first failing step none in these statements.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the underlying constructions.
The collar has one ambient scale, \(l=\xi_j\). Hence the two sums used are
\[
 \sum_{m=q}^{j-1}L^{m-j}\le\frac1{L-1},\qquad
 \sum_{m=q}^{j-1}L^{2(m-j)}\le\frac1{L^2-1}.
\]
The first controls the complex perturbations; the second controls the real reconstruction error.
Telescoping products of left-perturbed unitaries gives \(e^{\sum|\gamma_m|}-1\), including inverse factors.
The node covariance follows by induction down each pillar, with the prescribed multiplication order.
The logarithms in CC stay on one branch after its explicit radius reduction.
Old rows agree. Thus their difference has only collar support.
The real reference is regular by the converse averaging bound, since the joined scales are no larger.
These facts prove (2) below, subject to CC's displayed smallness inequality.

**Lemma RC: ADVANCE, with P81, [AX] and the stated geometry.**
Checked line by line by Codex, first failing step none.
Extend each smaller constraint-preserving variation by the fixed outside field, as in `a3-derivative.md` Lemma 10.2.
The fixed boundary rows remove crossing-plaquette variations; descent through the averages preserves every old row.
This proves real criticality. Orbit uniqueness and the node-normalized axial recursion give the real identity.
Both sides are holomorphic on the same datum ball supplied by CC.
Apply the one-variable identity theorem successively to each complex coordinate.
The identity then holds throughout that ball. On unchanged interior pillars the recursion is identically one.

**Theorem 6c^C: ADVANCE as the stated comparison implication.**
The segment between the two datum logs stays inside the common ball.
Its forcing has weighted norm at most
\(C e^{\theta(c_1\mu+D_L)}\|b_U-b_J\|_\infty\).
T4 and its multiplier equation give the field, gradient and current differences on this whole segment.
The operator norm includes the row sum; no collar count is added.
The gauge order is \(w=G^{-1}g_{\rm ax}^{-1}u'_U(u'_J)^{-1}\), as the note states.
For the second-difference member, one can avoid an implicit second-order BCH chain rule:
\[
 \begin{split}
 D_V^*D_Vf={}&\Xi_f^{\mathsf T}[J(e^{i\eta f}V)-J(V)]
 +(\Xi_f^{\mathsf T}-I)J(V)-\Delta'_Vf-N_V(f),\\
 &V=U_W^\circ,\qquad \Xi_f=\int_0^1\operatorname{Ad}(e^{it\eta f})\,dt.
 \end{split}
\]
This follows from \(F'(f)=\Xi_f^{\mathsf T}J(e^{i\eta f}V)\), retaining the chart conversion.
The local Wilson expansion in `a3-derivative.md` Sections 4 and 7.3 bounds the last three terms by
\(C(\xi^{-3}\xi|f|+\xi^{-3}\xi^2|\nabla f|)\) on the admitted small ball.
The already bounded current difference therefore bounds \(\xi^3|D_V^*D_Vf|\).
All products preserve the distance weight by placing it on the difference factor.
For the all-site condition number, telescope relative to the unitary factors at \(\beta=0\).
Their perturbations sum to \(C\|\beta\|\); this gives \(e^{C\|\beta\|}\), without a spurious \(e^{C\varepsilon_1}\) loss.
These details supply the two abbreviated size steps in Section 2.5.

**(H-node): ADVANCE on common interior axial pillars and over one Landau reference.**
On the former, \(G=g_{\rm ax}=1\); integrate the all-site T4 gauge response along the collar segment.
On the latter, the exact identity
\(e^{i\eta\mathcal H'_U}U'_*=e^{i\eta\widetilde f}e^{i\eta\mathcal H'_J}U'_*\)
has \(g=1\), so \(\varepsilon_N=0\).
There is one unused failure: Section 3(a), line 175, extends small \(|g-1|\) to all collar pillars using a condition number.
That inference is **WRONG**: the unitary matrix \(-I\) has condition number one and distance two from \(I\).
This does not refute the canonical-gauge claim; it leaves that extension unproved.
The box-first route uses the common-reference identity, not this extension or the two-reference case.

**Theorem A: ADVANCE as an implication with \(\alpha_k\le C_\alpha\alpha_{0,k}\).**
Checked line by line by Codex, first failing step none on its stated box-first domain.
Write \(u=s_k+c_\nu\). The shift has size \(Cu\alpha_k\).
The curvature and current clauses therefore move by \(CC_\alpha u\) of their radii.
The potential clauses use \(\alpha_0\le\alpha_1\).
(LD) pays the slow radius ratios at lower layers; Corollary R pays the shrinking tower gaps.
Choose \(2C_Ac_\nu\le1/8\) after these constants. Half-radius input then gives the claimed \(5/8\) bound.
Lemmas N and E (with the existing repair of N) and Theorem I give, at age zero,
\[
 \left(\frac98\right)^2\frac58=\frac{405}{512}<\frac45,
 \qquad 2025<2048.
\]
Thus the margin is at least \(1/5\); no age gain is used there.
For age \(m\ge1\), the additional factor is \(2\sqrt{1+m}L^{-2m}\).
It decreases, since its consecutive ratio is at most \(\sqrt{3/2}/9<1\) for \(L\ge3\).
At \(m=1\), its product with \(405/512\) is less than \(1/4\): use \(\sqrt2<10/7\).
The potential clause is below half its radius by \(CM\alpha_0<\alpha_1\).
The hereditary unit factors in Theorem I are at least one, so the same fractions apply to every clause.
The node-reduced datum stays inside \(r_B/2\) after the displayed ceiling on \(M\alpha_0\).
All estimates hold on the full stated \((s,t,\nu,\mathbf J)\) domain.
The radius convention is essential; this check does not replace it by \(\alpha_k\asymp\sqrt{\alpha_{0,k}}\).

The consumed collar and core inputs are now available as implications. Sections 2–4 below retain the row-172 stop for provenance.

## 1. Target and sources

The target is B4, SA 4006–4037, including the small-field map used at SA 22879.
SA denotes `YM4_sketch_500.tex` at the commit above, fetched once to `/tmp/sa_ym4.tex`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for that formulation.
Credit Tadeusz Bałaban for the background and small-field constructions.

The step must admit complex data throughout its product box, with constants independent of depth, volume and label count.
Its finer derivatives require their own stated domains.
The real result in `one-step-closure.md` does not supply either assertion.
This note follows the first unresolved input before attempting the cluster expansion.

## 2. The first input at row 172 (historical)

Row 172 stopped at the complex WF4 package in SA 15745–15833, before WF8.
It was needed for every allowed outer pair, including independent currents, throughout
\[
 |s_\Delta|<e^{\bar\kappa},\qquad 0\le t\le1,
 \qquad |\nu|<c_\nu/s_k.                                      \tag{1}
\]
The package needs common datum/core room and compatible boundary comparison with the prescribed node factors.
Section 0 supplies the missing comparison and admission implications for the adopted box-first route.

## 3. Where row 172 stopped (historical)

The precise missing step was the following common chart.
Let \(V^U\) be the restricted datum and \(V^J\) the joined datum, after the prescribed node gauges.
On every instance of (1), one must place them in a common admitted background chart:
\[
 V^U=e^{ib_U}V_*,\quad V^J=e^{ib_J}V_*,\quad
 \|b_U\|_\infty,\|b_J\|_\infty<r_B/2,
 \quad \operatorname{supp}(b_U-b_J)\subset\mathcal C,
 \quad \|b_U-b_J\|_\infty\le C a.                       \tag{2}
\]
Here \(V_*\) is a real regular reference datum, \(\mathcal C\) the actual collar, and \(a\) its regularity radius.
The constants and margins must be independent of depth and volume.
The Landau pair must also satisfy `o1-decoupled.md` Theorem I.

**What (2) would give, by hand.** Put \(b_u=b_J+u(b_U-b_J)\), \(0\le u\le1\).
Convexity keeps this segment in the datum ball.
For the normalized field, gradient and current coordinates \(Z_y\) in that same Landau chart, T4 gives
\[
 Z_y(b_U)-Z_y(b_J)=\int_0^1 DZ_y(b_u)[b_U-b_J]\,du.
\]
Choose the weight \(w(y)=e^{\theta d(y,W^c)}\), below the allowed response rate.
Memberwise containment gives \(d\le d'\), so this is also an allowed weight for the joined sequence.
If every collar row has \(d(c,W^c)\le c_1\mu\), the weighted response bound yields
\[
 |Z_y(b_U)-Z_y(b_J)|
 \le C a e^{\theta c_1\mu}e^{-\theta d(y,W^c)}.          \tag{3}
\]
The operator bound already includes the row sum. There is no factor counting rows or levels.
This was only a comparison implication until `wf-c.md` supplied (2).

The old proof used unitary transports in `a3-derivative.md` Lemma 10.3.
For complex transports, write the surface product as \(\prod_{r=1}^N T_rP_r^{\pm1}T_r^{-1}\).
If \(\|P_r-I\|\le a<1/2\) and \(\|T_r\|\|T_r^{-1}\|\le K\), telescoping gives
\[
 \left\|\prod_{r=1}^N T_rP_r^{\pm1}T_r^{-1}-I\right\|
 \le(1+2Ka)^N-1\le e^{2NKa}-1.                         \tag{4}
\]
Indeed \(\|P_r^{-1}-I\|\le a/(1-a)\le2a\), and each conjugated factor differs from identity by at most \(2Ka\).
Thus complex transport and node bounds were needed. Lemma C now supplies them as checked in Section 0.

## 4. Literature and scope at the row-172 stop

Bałaban CMP **109**, pp. 273–279, separates local analyticity of (3.25) from the core inclusion (3.36).
Row 172 read those excerpts and checked pp. 275–278 against the scan.
His construction retains the box background's current and transports both current and fluctuation with the gauge.

In particular, SA 7569 requires, for each radius component,
\[
 (1+\beta_s)^{-1}\le
 \frac{\alpha_{i,k+1}}{\alpha_{i,j}}
 \le(1+\beta_s)\sqrt{k+2-j},\qquad
 CM\alpha_0<\alpha_1,\quad \alpha_1^2\le C\alpha_0.       \tag{5}
\]
These comparisons alone do not prove the datum and core inclusions; Section 0 now supplies the route's implications.
CMP **116** is absent from the permitted paper folder and was not read.
The QED3 and YM3 manuscripts are also absent from the permitted local sources.
No missing source is counted as evidence.

## 5. Resume: the local Gaussian is available conditionally

The continuation uses the radius ratios (5), the half-radius input core and the convention in Section 0.
The relevant Gaussian is the UM Gaussian, not the reference-box Hessian.
Read `inv-root.md` (11), (17)–(20) and its check in `carrier-adopt.md` Section 1.
With the adopted series, `um-envelope.md` (7) gives
\[
 \|C-C_0\|+\|\Gamma-\Gamma_0\|\le\epsilon_G,
 \qquad \|C_0\|+\|C_0^{-1}\|+\|\Gamma_0\|\le K_G.       \tag{6}
\]
These retain their named A2 and repaired walk premises.
The matrices \(C,C_0\) are symmetric; \(C_0\) is real positive definite and \(\Gamma_0\) is real. Put \(m=\dim C\).
Here \(C=(\chi A(s)\chi)^{-1}\) and \(\Gamma=-\chi A(s)(1-\chi)r(s)\).
The two factors keep their separate tags; \(r(s)\) is not \(A(s)^{-1/2}\).
Thus the previously missing inverse-root estimate is not a new stopping point.

**Gaussian comparison, rebuilt from (6).** Put \(D=C+C\Gamma\Gamma^{\mathsf T}C\), and define \(D_0\) likewise.
Transposes here are bilinear. The eigenvalues of \(D_0\) lie between \(K_G^{-1}\) and \(K_G+K_G^4\).
Expanding the finite products gives \(\|D-D_0\|\le C(K_G)\epsilon_G\).
The Neumann series therefore gives \(\operatorname{Re}D^{-1}\ge c(K_G)I\) for sufficiently small \(\epsilon_G\).
The auxiliary Gaussian has joint precision
\[
 Q=\begin{pmatrix}C^{-1}&-\Gamma\\-\Gamma^{\mathsf T}&I+\Gamma^{\mathsf T}C\Gamma\end{pmatrix}.
\]
At the real reference, its quadratic form is
\((b-C_0\Gamma_0\xi)^{\mathsf T}C_0^{-1}(b-C_0\Gamma_0\xi)+|\xi|^2\).
The triangular change and its inverse have norms bounded by \(1+K_G^2\).
Small perturbation preserves a positive real part, independently of both dimensions.
Integrating \(\xi\) gives precision
\(C^{-1}-\Gamma(I+\Gamma^{\mathsf T}C\Gamma)^{-1}\Gamma^{\mathsf T}=D^{-1}\).
Block elimination gives \(\det D=\det C\det(I+\Gamma^{\mathsf T}C\Gamma)\).
These identities first follow by real Gaussian completion, then by holomorphic continuation on the admitted ball.
They identify the normalized functional with the Gaussian of covariance \(D\), including for fixed measurable cutoffs.

For \(|F(b)|\le F_*e^{\rho|b|^2}\), compare this density with the real \(D_0\) density.
Use \(\log\det(I+E)=\sum_{n\ge1}(-1)^{n+1}\operatorname{tr}(E^n)/n\) and
\(|\operatorname{tr}(E^n)|\le m\|E\|^n\).
Gaussian integration of the remaining quadratic tilt gives
\[
 |\mathcal J[F]|\le F_*e^{A_K(\epsilon_G+\rho)m}.          \tag{7}
\]
Choose \(\rho\) so that the tilted precision keeps half its reference gap.
If \(v\) distinct cutoff bonds fail, \(|b|^2\ge v\mathfrak b^2\).
Apply (7) with \(\rho+\gamma/2\), extracting \(e^{-\gamma v\mathfrak b^2/2}\).
Only the local dimension \(m\) enters the bound; the auxiliary dimension cancels before the estimate.
This rebuilds SA FG6 and UM6, conditional on (6), with no zero-free assumption.

I read Balaban CMP **109**, pp. 269–270 and 275–280, for this continuation.
His (3.25)–(3.53) require the inner-core inclusion before composition and Cauchy estimates.
Section 0 rebuilds that inclusion for this route; (6)–(7) address the later Gaussian integration separately.
His assertion about the scalar remainder at (3.1) is not used as a proved local activity bound.

## 6. First new stop: formation of the intrinsic scalar potential

**The first unproved input is UM1 for the actual intrinsic action/gauge potential.**
This precedes the application of B1, even with zero older potentials and \(x=\mathsf t\).
Put \(g=\mathsf t^{-1/2}\) and \(\mathfrak b=\delta(\mathsf t)/g\).
Let \(\mathcal P_k^{G,A}\) be the remainder after the actual one-step fibre substitution and quadratic subtraction.
Its physical scalar is the action/gauge remainder in SA 7601–7614; its local continuation must use the assigned operators.
The required part of SA UM1 is an exact family, on the declared local cores, with
\[
 \mathcal P_k^{G,A}=\sum_Y V_k^{G,A}(Y),\qquad
 |V_k^{G,A}(Y;P,B)|\le C_M\delta(\mathsf t)e^{-\lambda_Vd_f(Y)}
 \left(1+M^{-4}\sum_{b\subset Y}|B(b)|^2\right).          \tag{8}
\]
The equality is at complete physical data; each term must have its assigned full read support and hereditary restrictions.
The bound must hold throughout the complex fluctuation boxes, external cores and enlarged decoupling discs.
Its constants must not depend on depth or volume.
The rate must meet UM19, not merely be positive.
The pivot and Haar logarithms in SA 7479–7487 are further pieces of \(\mathbb P^{(k)}\), not covered by this cubic claim.

**First reduction: the actual B1 argument reads (8).**
SA 1191–1310 applies the hard-core tree bound after the activity criterion is verified.
In the actual expansion, the selected factors are \(e^{V(Y)}-1\), with the fixed real cutoffs of UM2.
UM13 needs the rooted sum of their absolute bounds before Gaussian integration.
If the full UM1 budget is \(0<a_{\rm pot}<W_0\), enlarge each selected coupling to
\(\mathcal R_Y=(W_0/a_{\rm pot})e^{(\lambda_V-\lambda_0)d_f(Y)}\).
UM1 and the rooted domain count then bound their sum by
\(C_pW_0L^4\#Z+C_pW_0M^{-4}|B|^2\).
For that count, a covering-tree traversal of length \(C(m+1)\) gives at most \(C_De^{\kappa_fm}\) rooted domains.
Choose \(\lambda_V>\lambda_0>\kappa_f\) and sum the resulting geometric series.
There are at most \(CL^4\#Z\) fine root cubes; for the quadratic term, sum at each bond first.
Choose \(W_0\) with \(C_pW_0M^{-4}\le\rho_0(K_G)\); equation (7) then integrates this quadratic majorant.
Without the actual UM1 family, neither that coupling disc nor its Gaussian domination has been justified.
Thus an abstract gas with small activities cannot discharge this application of B1.

**Second reduction: try the scalar primitive of [NL].**
Use the adopted reduced expression in `nl-r9.md` (4.6), with its own \(H(s)\) and \(M_s\).
Call this scalar \(R_s(a)\); its gradient is the five-term \(W_s^{\rm red}(a)\).
It vanishes through degree two. On the star-shaped field ball, [NL] gives
\(\|W_s^{\rm red}(ua)\|_{F,1}\le A_Nu^2r^2\), where \(r=\|a\|_{X,1}\).
The constant \(A_N\) retains the stated [PW], [Rows] and [RED] premises.
The physical pairing therefore proves, by hand,
\[
 R_s(a)=\int_0^1\langle a,W_s^{\rm red}(ua)\rangle_f\,du,
 \qquad |R_s(a)|\le\frac{A_Nr^3}{3}
                 \eta^4\sum_b\xi_b^{-4}.                \tag{9}
\]
Here \(\xi_b|a(b)|\le r\) and \(\xi_b^3|W_s^{\rm red}(ua)(b)|\le A_Nu^2r^2\); integrate \(u^2\).
This proves a scalar bound for that primitive. It does not identify it with the full one-step remainder after the pivot map.
Nor does it bound the absolute local family in (8).
The [NL] norm bounds an already summed force; (8) needs bounds before the carrier sums, with the actual support assignment.
Expanding the implicit field and the fibre substitution into those carriers would be a sufficient next route.
I have not bounded their scalar Taylor remainders in that absolute family norm on the full complex domains.
The inference from (9), or from \(g|B|^3\le\delta|B|^2\), to (8) is the first failed application here.
Balaban's scalar analyticity assertion and SA 7864 do not supply that calculation.
After these two reductions the attempt stops at (8). This is a gap, not a counterexample to (8) or B4.

## 7. Row 186: check of Claude's `um1.md`

Provenance: Codex (GPT-6 family; runtime effort not exposed), at `f33ea406fd0ccd9bf02512e36dc7c8b76bd16f75`. One line-by-line check; research text, not an audit; no status.

**First failed input: [D]'s extension of wall-zero splitting to the actual \(M_s\).**
It fails at `um1.md:74`, and Lemma S uses it at line 98.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for R9, UM and B1/B4.
SA below retains the source pin of Section 1, fetched once for this continuation.

### 7.1 The response lemmas

**Lemma P: ADVANCE, conditional on [R9] and the stated core conditioning.**
Checked line by line by Codex, first failing step none.
Write \(e=2BC_{B'}\|u\|_\infty\).
The four transported insertions have signed sum bounded by
\(2\eta e+C\alpha\eta^2e\).
Their exponential product therefore differs from identity by
\(C\eta^2(e+e^2)\le C'\eta^2e\).
Multiplication by the bounded background plaquette gives (4.1).
This uses the covariant difference bound, not a bound on the response's full Laplacian.

**Lemma S: WRONG at Step 0 for the specified operators.**
The source definition in `nl-r9.md:179–188` is
\[
 M_s=\mathsf m^3[W_0^{-1}]_s\mathsf m^{-1}-a_0I,
 \qquad\text{the diagonal }-a_0I\text{ has no parameter}.       \tag{10}
\]
Each walk in \([W_0^{-1}]_s\) has a nonempty tag set: its hull contains its row endpoint.
Set every parameter to zero, an allowed point of the decoupling polydisc.
Every walk then vanishes, including every zero-length walk, whereas
\[
 M_{\boldsymbol0}=-a_0I,\qquad
 M_{\boldsymbol0}e_c=-a_0e_c\ne0                           \tag{11}
\]
for a nonzero raw-row vector \(e_c\); `a2-layers.md:61` chooses the stabilizing coefficient \(a_0=1\).
All parameter cubes now belong to \(N\).
Lemma S's Step 0 instead asserts zero on those rows for all four operators, including \(M_s\).
Equations (10)–(11) contradict that assertion directly.

This is an operator-definition mismatch, independent of depth, volume and the background current.
It does not refute the claimed splitting of the nonlinear response \(H\).
The exterior factors \(H_1(s),G(s),H(s)\) still have their tagged support properties.
A possible repair must treat \(-a_0I\) as a local map throughout the Picard chains.
It must include the joined local read stencils in the neighboring tags; that repair is unproved here.
Retagging the diagonal would change the assigned R9 system when \(s\ne1\).

**Corollary R: CORRECT-NO-ADVANCE as an implication from a valid Lemma S and [RT].**
The plaquette's root star contains each corner star.
A second wall-component contributes a differentiated parameter on which the rooted anchor does not depend.
That derivative is zero. Matching the full read hulls then gives heredity by identical Picard iterates.
This conditional argument passes; (11) prevents using the supplied proof of its Lemma S input.

### 7.2 The scalar calculation and the rate

**Lemma T and the anchor estimates: ADVANCE as the stated implications.**
Checked line by line by Codex, first failing step none in this calculation.
For \(r=r_1/2\ge2\), the linear determinant term has coefficients bounded by \(2ABr^{1-n}\).
The quadratic determinant term has coefficients bounded by \(B^2r^{2-n}\).
The factor \(1/2\) and the two geometric sums give
\[
 \sum_{n\ge3}|f_n|\le2ABr^{-2}+B^2r^{-1}
 =8ABr_1^{-2}+2B^2r_1^{-1}.
\]
Multiplication by \(\mu^n\le\mu^2\) proves the second bound.
For the action anchor, insert \(A=C_0\alpha\eta^2\), \(B=C_1\delta\eta^2\) and \(r_1=r_R/\delta\).
Then \(\alpha\le r_R\) and \(g^{-2}\mu^2\le\delta^{-2}\sum_Y|y|^2\) give (5.2).
Taking \(A=0\) gives (5.3). Local truncation of \(y\) still requires Corollary R.

**Theorem U: CORRECT-NO-ADVANCE as a conditional construction; its actual-data application is blocked by (11).**
Repeated fundamental theorems of calculus give its exact finite bracket identity.
Holomorphic composition and Cauchy integration give (H) on the named domains.
Conditional on Corollary R, each bracket costs \(e^{-(\bar\kappa-1)|Y\setminus X_0|}\).
There are at most \(6(M/\eta)^4|Y|\) action anchors, canceling the \(\eta^4\) in (5.2).
The inequalities \(|X_0|\le16\), \(|Y|e^{-|Y|}\le e^{-1}\) and \(d_f(Y)\le|Y|-1\) give (6.1).
The finite gauge-anchor count gives (6.2); their sum is the stated \(K_{GA}\delta\).
Thus no depth or volume factor arises in this conditional scalar calculation.

**Rate: CORRECT-NO-ADVANCE, conditional on the local family.**
Choose the common \(\lambda>\lambda_0+\Theta/L+\sigma_0\) in `um-envelope.md` (8).
Then \(\bar\kappa\ge\max\{\lambda+2,\Theta+1\}\) gives both UM19 inequalities, with \(R_s=e^{\bar\kappa}\).
The later choice of \(M\), then the radii, then \(t\), absorbs \(K_{GA}\delta(t)\).
This checks the rate allocation. It cannot repair the support identity (11).

## 8. Stop before applying B1

The first reduction in Section 6 needs UM1 for the assigned operators, including its local support and heredity.
The failed input above prevents that application. No new B1 conclusion is drawn.
The Gaussian comparison (7) remains checked by Claude, first failing step none, conditional on (6).
It bounds the integral but does not establish the missing response support identity.

Balaban CMP **109**, pp. 269–270, (3.1), likewise separates scalar analyticity from localization.
His pp. 275–276, (3.25)–(3.29), retain the assigned current and field transformations on their proper domains.
Those passages do not replace the failed operator identity. Their method is credited to Tadeusz Balaban.
B4, the map 1.6, and the finer potential, zone and mixed derivatives are not reached.

## Result

**Stopped at UM1 [D] and Lemma S, Step 0: the actual \(M_{\boldsymbol0}=-a_0I\), not zero.**
The nonlinear splitting conclusion is not refuted; its supplied proof has a false operator input.
The scalar remainder and rate calculations pass conditionally. Equation (7) remains checked by Claude.
B1, B4 and 1.6 remain unproved here, including their finer derivatives on their own domains.
Only this file was changed. Every mathematical step above is by hand; no status is granted.
