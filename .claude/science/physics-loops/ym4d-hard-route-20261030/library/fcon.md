# FCON: mean matching and stage-contour tests

Provenance: Codex, pass 2 of Claude's `fcon-draft.md`, at checkout `c8dab7974ace28516f8ac295f7baaedaba923ef7`. Research text, not an audit; grants no status. Source material by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, is credited where used. Not yet refereed.

The arguments below are by hand. **FC-mean-match is proved for the declared split, conditional on its actual-family identification. FC-test is conditional on the older-test margin and the complete factor accounting stated below.** Neither condition is obtained by renaming a remainder. This supplies precisely conditional assertions for ST1 Theorem 14 hypothesis 5, Corollary 14′ and GEOH Lemma 10; it does not close critical-path item 7.

SA denotes the outline at `31a47c543775`; CA-I, II, III denote its complete accounts; Y3 denotes `YM3/YM3_I.tex` at that revision. The stage, averaging, gauge and contour constructions are credited to **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. Their underlying background and renormalization methods come from Tadeusz Bałaban; the library's flat-propagator exposition also uses Jonathan Dimock. Source checks are recorded in [checks/fcon-pass2/source-checks.md](../checks/fcon-pass2/source-checks.md). All line references to library files use this checkout.

## Definitions and imports

**D1 (stage and variables).** Fix a finite admitted history, its geometric record and frame. A passing stage of level \(j\) enlarges member \(j+1\). Use the relative removed and added row sets \(E,C_+\) of [geoh](geoh.md), Definition 5, and \(F=E\setminus p(C_+)\), \(N=|F|\). The rim coordinates are \(\mathfrak a\), disjoint from \(F\), as required by **SLOT-ST**. Retained rows and other stored coordinates are parameters. This does not assert SLOT-ST's actual storage match; geoh L257 retains that input. SLOT-CA and FM-match are additionally required only for a separately fixed CA-I presentation.

For new datum \(W\), let \(U_+\) be its canonical regular critical background, \(V=M_-(U_+)\), and \(V^\sharp=M_-(U_+^\sharp)\) the localized test reference. Both use Amendment CV's contour means. Put
\[
 g=g_j=\theta_j^{-1/2},\quad \ell_j=\log\theta_j,\quad
 \delta'=A_1g\ell_j^{p_1},\quad \varepsilon_j=A_0g\ell_j^{p_0},\quad b=\delta'/g,
\]
\[
 \eta_e=i^{-1}\operatorname{Log}(V_e(V_e^\sharp)^{-1}),\quad m_e=\eta_e/g,
 \quad u_e(Z)=i^{-1}\operatorname{Log}(e^{igZ_e}e^{-i\eta_e}),\quad \beta(Z)=u(Z)/g. \tag{1}
\]
The common small branches are part of admission. On removed rows set
\(D(Z)=e^{ia_V(u(Z))}V\), with \(a_V(u)=\Psi_V(\mathsf C_Vu)\); copy retained rows. On free rows, exactly,
\[
 D_e(Z)=e^{igZ_e}V_e^\sharp,\qquad u(m)=0,\qquad D(m)=V. \tag{2}
\]
Write \(D_b=\{Z\in(\mathbb R^3)^F:|Z_e|<b\}\) and
\(T^\sharp_\rho=\{Z:|\Re Z_e|+|\Im Z_e|<\rho\}\). The Pauli basis gives three real colours per row. Quadratic forms use bilinear transposes; their block operator bounds use the complex Euclidean colour norm. The matrix operator norm controls that norm and agrees with it on real potentials. Thus ST1's bounds apply to the estimates below.

**D2 (imports H).** Retain the following premises of [st1-r4](st1-r4.md), Theorem 14 and Corollary 14′, with Amendments CV and GS: GEO, GEO-mark, GEO-box and full read margins; CH/F2; AV/CURV; A1/F0/REG; P82°–M1 and (15); PROF/RCG4; OPS/SLICE/UNQ; RUN/RUN-low and formation (56), (58); ST-test, ST-test\(^{\rm hol}\), and one stated LOC clause. **FC-mean-match and FC-test are not included in H.** Include SLOT-ST, initial/unfinished base admission, persistent-record compatibility, and the main-step and BOX supplies wherever the history uses them. Complex domain membership is an input on the whole parameter set, not a consequence of real membership. The raw chart, boundary buffer, uniqueness, source and pinning budgets of F4, Lemmas 12–13 and Theorem 14 remain in force.

For analytic compositions import **DR Theorem 4** on the full source and switch domains, with its W, ONE, PW, NL, column, Rows/Pair and admission hypotheses; retain its restriction/transport/component premises when used. In particular \(s_D=\epsilon_De^{-64\bar\kappa}\), \(E_{\bar\kappa}=e^{48\bar\kappa}\). Import **CI for previously formed activities**, including their target domains, real ties, pair descent when needed, and stored-slot rules. Assume the **actual rim-form and normalizer supply required by HM/CI** on those domains; descent alone does not provide it. CP12 Theorem 3 supplies (15) only under its stated P81/P82, coefficient and admission premises. DOM-draft Theorem 8 is a conditional proposal, not an additional frozen admission theorem; its LOC♮ remains open. These imports are used only with their own qualifications.

**D3 (stored integrand and analytic parameters).** Keep the complete specified integrand
\(\Theta(\mathfrak a,D)=\Xi(\mathfrak a,D)e^{\mathcal A(\mathfrak a,D)}\)
of ST1 Theorem FM. It includes every earlier density, test, gauge factor, normalizer, strip factor and Gaussian weight. Fix the factor allocation as part of the presentation. A factor is *moved* when it varies with \(Z\) at fixed \(W,\mathfrak a\) and other Borel parameters. An indicator is *redundant* when it equals one on all of \(D_b\), for every real datum in use and every remaining stored parameter on its support. Real data in use have a common open real slice in the connected continuation chart. For joint holomorphy, a merely Borel factor without a supplied analytic extension must either be held fixed in **both** \(Z,W\), or be constant in \(Z\) and locally constant on the real \(W\)-chart and replaced by that constant. Independence of \(Z\) alone only permits contour deformation at fixed \(W\).

**D4 (order of constants).** Use IN1 L221–236 and Amendment 1, with ST1 L160–171. First choose exponents, fractions, geometric data and odd \(L\) above every imported floor (in particular \(L\ge27\) when descent is used), and \(2\le L_\flat<L/2\). Next choose flat/averaging data, local gauges/inverses, profile/response rates, \(M_1,R_1\), separation and chart bounds. Fix \(C_{\rm ch},C_\ell,C_{\rm av},r_u,r_{\rm sol},r_{\rm hol},M_*\), and LOC's \(C_F,a>0\) here. Any uniform precision constants \(s_1,c_S,K_0,H_0,\ldots\) used below must also be supplied before \(\kappa\), independently of \(M,\bar\kappa\). Then choose \(\kappa\), the other rates, \(\bar\kappa\), \(M\) above its floors, post-\(M\) constants and \(A_1,A_0,C_0,C_1\). Finally decrease \(\gamma\). No late amplitude defines an early constant.

The final ceiling imposes all imported ceilings, FC1/FC7/FC8, \(C'_A\delta'_j<s_D\), and the gauge ceiling (8) below, uniformly over the stage window. The source and pinning budgets remain those of (70)–(73); a source-domain bound alone does not imply them. FC7 gives
\[
 \mu_\sharp:=\max_e|m_e|\le g^{-1}\sqrt{M_*C_F}\,e^{-aR_\sharp/2},
 \qquad \mu_\sharp/b\longrightarrow0,\qquad |m_e|\le b/16. \tag{3}
\]
Here \(R_\sharp\ge MR_t/4\), and the limit is uniform in the stage window for each fixed choice of the earlier and late parameters. No uniform limit in unbounded \(M,\bar\kappa\) is asserted.

## Mean matching

**Lemma 1 (CV, the gauge forms, and zero first variation).** Every moved level-\(j\) block-contour factor reads only free internal rows of a new-member block. Its reference mean is exactly \(I\), at real and complex admitted data. Consequently its absolute gauge function equals the relative-trace function defined below; their common pullback Hessian is descent's Y3 form. If \(\mathcal P\) is any carried subset of level-\(j\) pairs, then
\[
 d_{\beta=0}\left[\kappa_j\mathcal S(e^{ia_V(g\beta)}V)
       +\Gamma_{\mathcal P}(e^{ia_V(g\beta)}V)\right]=0,
 \quad \Gamma_{\mathcal P}(D)=x_j\sum_{(y,x)\in\mathcal P}
                 [1-\tfrac12\operatorname{tr}D(y,x)]. \tag{4}
\]
Here \(\mathcal S(D)=S_{\Omega_0}(\Phi_-(D))\); \(\kappa_j\) is the action coefficient, distinct from IN1's rate \(\kappa\). No gauge-coverage assumption is needed for (4). Positivity can require coverage.

*Proof.* A coordinate-ordered shortest path between a block centre and a block site stays inside that aligned cube. Each internal row of a new-member block is removed and free; pivots cross faces (ST1 L1131–1137). In an old deeper block no internal row is removed. In a block outside the new deeper member the internal rows retain their status. Thus these are all moved pairs. Every noncentre site of a new-member block becomes a nonnode with that centre as parent. CV sets the corresponding mean of \(\mathcal M^jU_+\), hence of \(V\), equal to \(I\). Holomorphy and successive one-variable identity theorems extend this equality from the open real slice to the connected chart.

For one pair put \(w(A)=(e^{iA}V)(y,x)\) and define the relative-trace function as \(1-\tfrac12\operatorname{tr}[w(A)w(0)^{-1}]\). Since \(w(0)=I\), it equals the absolute function throughout their common branch, not only to second order. Write \(w(tA)=e^{iH(t)}\). The analytic mean lies in \(SL(2,\mathbb C)\), so \(\operatorname{tr}H(t)=0\). With \(H(0)=0\),
\(1-\tfrac12\operatorname{tr}e^{iH(t)}=\tfrac14t^2\operatorname{tr}\dot H(0)^2+O(t^3)\).
Thus the Hessian is \(\tfrac12\operatorname{tr}[\dot H_A(0)\dot H_B(0)]\), precisely Y3's bilinear form, including complex directions. Its zero gradient means the nonlinear chart adds no gradient–second-derivative term to the pullback Hessian. Nonmoved pairs have zero pullback derivatives. The action curve stays in the new fixed determining fibre by ST1 (67). At zero its reconstructed background is \(U_+\) up to residual gauge. Criticality and gauge invariance give zero action derivative. Continue that identity on the same chart. This proves (4). ∎

**D5 (declared Gaussian split).** Define, without dropping either coefficient,
\[
 \mathcal W(D)=-\kappa_j\mathcal S(D)-\Gamma_{\mathcal P}(D),\quad
 \mathcal K=\mathcal A-\mathcal W,\quad
 S=-\operatorname{Hess}_{\beta=0}\mathcal W(e^{ia_V(g\beta)}V).
\]
Thus the factors \(g^2\kappa_j\) and \(g^2x_j\) belong to \(S\); identifying a coefficient-ratio parameter elsewhere requires these normalizations. For the actual carried rim form write \(\Delta^{\rm loc}(D)\), including its specified pair evaluation. Set
\[
\begin{aligned}
 R_{\rm rec}&=\tfrac12(Z-m)^{\mathsf T}S(Z-m)-\tfrac12\beta(Z)^{\mathsf T}S\beta(Z),\\
 T_3&=\mathcal W(D(Z))-\mathcal W(V)+\tfrac12\beta(Z)^{\mathsf T}S\beta(Z),\\
 P_{\rm slot}&=-\tfrac12\langle\mathfrak a,[\Delta^{\rm loc}(D(Z))-\Delta^{\rm loc}(V)]\mathfrak a\rangle,\\
 K_1&=\mathcal K(\mathfrak a,D(Z))-\mathcal K(\mathfrak a,V)-P_{\rm slot},\\
 J&=\sum_{e\in F}\log s(g^2Q(Z_e))+\log[\Pi_V(u(Z))/z_V],\qquad
 \mathcal R=R_{\rm rec}+T_3+P_{\rm slot}+K_1+J. \tag{5}
\end{aligned}
\]
Here \(Q(z)=\sum_{a=1}^3z_a^2\), \(s(q)=(\sin\sqrt q/\sqrt q)^2\), and \(\Pi_V,z_V,\sigma_H\) are FM3–FM5's exact coarea factors. The logarithm of \(\Pi_V/z_V\) is the sum of the local matrix-trace and pivot-Haar logarithms of FMd. Their increments, not their product over all rows, lie in fixed logarithm balls. The free-Haar logs use their small-argument branches. In general \(J(m)\ne0\); it is retained.

**Lemma 2 (exact split and its scope).** For nonnegative Borel or absolutely integrable real stored integrands,
\[
 I(W)=(\sigma_Hg^3)^Nz_Ve^{\mathcal W(V)}
  \int d\mathfrak a\,e^{\mathcal K(\mathfrak a,V)}
  \int_{D_b}dZ\,\Xi(\mathfrak a,D(Z))
       e^{-\frac12(Z-m)^{\mathsf T}S(Z-m)+\mathcal R(\mathfrak a,Z)}. \tag{6}
\]
The declared precision is symmetric, real on real data and holomorphic in the admitted datum. Its Gaussian has centre \(m\) and no rim coupling. The reference and centre are independent of \(\mathfrak a\). All other linear and quadratic terms, including seam, rim and Jacobian terms, remain in (5). The term \(T_3\) has a zero of order at least three at \(Z=m\).

*Proof.* FC1 identifies the real passing domain with \(D_b\). Substitute FM5 into FC2. Its density is \((\sigma_Hg^3)^Nz_Ve^J\). Insert \(\mathcal A=\mathcal W+\mathcal K\) and the four add-and-subtract identities in (5); the exponent is exactly \(\mathcal A+J\). Tonelli or absolute Fubini gives (6). No normalization or test has been discarded. Lemma 1 removes the first Taylor coefficient of \(\mathcal W\); the definition of \(S\) removes its second coefficient in \(T_3\). Since \(\beta(m)=0\), its analytic composition still has order at least three. Symmetry, reality and holomorphy follow by differentiating the joint holomorphic chart function. The stated absence of rim coupling concerns the chosen quadratic factor, not the full exponent. ∎

**Lemma 3 (recentering and conditional force).** Let \(s_1=\max_e\sum_{e'}\|S_{ee'}\|\) on the admitted parameter domain. Then
\[
 -\tfrac12(Z-m)^{\mathsf T}S(Z-m)
 =-\tfrac12Z^{\mathsf T}SZ+R_0(Z),\quad
 R_0=m^{\mathsf T}SZ-\tfrac12m^{\mathsf T}Sm,
 \quad |R_0|\le Ns_1\mu_\sharp(2b+\mu_\sharp/2) \tag{7}
\]
on \(T^\sharp_{2b}\). This centres the Gaussian at the test origin. Its precision is still \(S(V)\), which need not be local. Also \(D(0)\) equals \(V^\sharp\) only on free rows; the pivots still solve the true constraint.

If, at fixed rim variables, \(|\mathcal R|\le\mathcal M\) holomorphically on that tube and \(\Re(v^*Sv)\ge c_S\|v\|_2^2\) for all complex \(v\), set \(f=\nabla\mathcal R(m)\). Then \(|f_{e,a}|\le2\mathcal M/b\), and the model keeping **only the constant and linear part of the remainder** has centre \(m+S^{-1}f\), with
\(\|S^{-1}f\|_\infty\le2\sqrt{3N}\mathcal M/(c_Sb)\).
If the quadratic remainder is also retained, its precision is \(S-\mathcal R''(m)\), and that matrix's inverse must instead be bounded. No exact nonlinear saddle is asserted.

*Proof.* Expand the symmetric quadratic form. Sum block operator norms, using \(|Z_e|_2<2b\), to obtain (7). Equation (3) proves the uniform smallness of \(\mu_\sharp/b\) at fixed late parameters. A complex disc of radius \(b/2\) in any one colour coordinate about \(m\) stays inside the tube: its row's real-plus-imaginary norm is at most \(2|m_e|_2+2(b/2)\le9b/8\). Cauchy's integral formula bounds the derivative by \(2\mathcal M/b\). Accretivity gives \(\|S^{-1}\|_2\le c_S^{-1}\); solving the model's linear stationary equation gives the displayed estimate. Retaining the second derivative changes that equation to \((S-\mathcal R''(m))(Z-m)=f\). ∎

These force estimates are conditional. A rim-uniform majorant and a volume-uniform force budget are not supplied by saying that NL1/LF1 owns the remainder. The \(\sqrt N\) bound alone gives neither. To keep FC9's stated fractions, one may impose \(\mu_\sharp\le b/32\) and \(\|S^{-1}f\|_\infty\le b/32\); the first follows from its localization proof, the second is additional.

**Theorem 4 (FC-mean-match, with the required identification).** Under H, the declared split (5) has exactly FCr's Gaussian and centre. If the actual stage's Gaussian presentation is this split, including the coarea/vacuum factors, the actual rim assignment and its holomorphic switch/external-pair extension, it supplies FC-mean-match to the frozen consumers. Then \(m_r=0\), \(\vartheta_m=0\), and \(\epsilon_m=1/16\) are valid for both FC7's \(b\) and F5's \(b_j=9b/8\). Positivity, the complex perturbation estimate and the full remainder bound remain separate NL1/LF1 inputs.

*Proof.* Lemmas 1–2 identify the declared quadratic and account for every extra term. Equation (3) gives \(|m-0|\le b/16<b_j/16\). No real shift of the test centre is used; this is the meaning of \(\vartheta_m=0\). On any admitted family of data holomorphic in switches, the identified factors are holomorphic by composition. Dependence on data outside \(X^\sharp\) enters the geometric construction through \(V\); the independently prescribed exterior-pair and current dependence of an actual Gaussian is included only by the identification premise. Lemma 3 gives the exact alternative centred at zero. ∎

**Outstanding — actual-family identification (HM/CI).** The preceding premise is not proved by D5. ST1 L1450 names a quantitative package, not a definition of a unique stage precision. NL1-L Theorem 7 (L578–589) requires actual matrices, normalization, heredity, wall factorization and full-domain formation formulas. CI-form H-G/H-S (L42–59) uses the normalized local covariance \(D=C+C\Gamma\Gamma^{\mathsf T}C\); its precision is \(D^{-1}\). Hm L361–373 identifies a physical marginal by a Schur complement only with G-ID, and leaves stage identification explicit. Descent L279–285 retains actual formation and vacuum bounds after a change of split. These facts settle draft Remark 3.4′: no frozen NL1/LF1 statement identifies its declared \(S\) at every stage. One must identify the appropriate full, compressed or marginal matrix in the specified coordinates, with coupling ratios, rim terms, determinants and switched carriers. If another Gaussian is assigned, its exact difference belongs in (5), and its bounds must be proved there. This is an existing actual-family obligation, not a counterexample to either split.

## Tests and continuation

**Lemma 5 (the soft gauge indicators).** On a fixed smaller AV branch let \(C_{\rm av}\) bound the contour mean's real Lipschitz constant in the maximum path-product group distance. Set \(C_{\rm gi}=\tfrac94(L-1)C_{\rm av}\). Require room for both path families in that branch and
\[
 2C_{\rm gi}\delta'_j<\varepsilon_j,
 \quad\text{equivalently}\quad
 2C_{\rm gi}(A_1/A_0)\ell_j^{-(p_0-p_1)}<1. \tag{8}
\]
Every moved level-\(j\) gauge indicator with threshold at least \(\varepsilon_j/2\) is one throughout \(D_b\), for real admitted data. Its exponential has the holomorphic extension obtained by replacing \(\Re\operatorname{tr}\) with \(\operatorname{tr}\).

*Proof.* FC1 gives \(|u_e|<9\delta'_j/8\). Lemma 1 makes every row on a moved gauge contour free. Each path has at most \(2(L-1)\) bonds. Insert successive unitary partial products to telescope its change; bi-invariance of the real group distance gives a bound \(\tfrac94(L-1)\delta'_j\). The mean changes by at most \(C_{\rm gi}\delta'_j\). Its reference value is \(I\), so \(|D(y,x)-I|\le C_{\rm gi}\delta'_j<\varepsilon_j/2\). The bound \(|e^{iH}-I|\le|H|\) follows by integrating \(ie^{itH}H\) for Hermitian \(H\). Reference path products need not individually equal \(I\); AV's smaller common branch supplies their room. Their changes remain in that room after a fixed-factor coupling ceiling. Equation (8) is another final ceiling because \(p_0>p_1\). Finally an \(SU(2)\) matrix has conjugate eigenvalues, hence real trace. Its trace extension is holomorphic; real part is not. ∎

**Lemma 6 (fixed factors, and the stopped-stage reading).** At fixed datum and stored parameters, the following do not vary with \(Z\): functions of retained rows; functions of the constrained new averages and their further defined averages; tests of fixed rim/strip variables; and frozen failure factors whose complete reads precede the current operation window. The level-\(j\) gauge factors outside new-member blocks are also fixed. An earlier passing-stage output is holomorphic in the present moved coordinates if its own FC-test, domains and majorants have already been established.

*Proof.* The fibre equation fixes every added average to \(W\); retained rows are copied. Iterating a defined fixed average does not change it. Other stored rows remain independent coordinates. SA 17518–17528 puts the strip cutoff in its own real strip variable; background discrepancies occur in its reconstructed bond and Jacobian, not in that cutoff. The carried tests do not acquire a new background dependence on reevaluation (SA 17558). Thus the stated fixed-coordinate tests remain Borel parameters. Lemma 1 treats the gauge factors.

For the flagged reading in draft Lemma 4.3, SA 17575 and 17585 specify the levels of operation \(t\) exactly as \(t-N_t,\ldots,t-1\). This is not RUN-low's \(t-N_t^0\). An operation that stops has no subsequent stage of its own. A frozen failure born at operation \(s\) has its full test function and data at levels at most \(s\), including the datum of its localized reference, not merely its failed free rows. If a later class component contains that mark, GEO-mark gives \(s<t-N_t\); none of these rows is moved by its stages. For another component, F7's complete-carrier separation gives independence. This uses frozen carriage; recomputing the old test with a new external background would require another argument. Finally, an already integrated passing branch is a holomorphic function of its datum by its earlier FC2 application. Compose it with the present holomorphic datum map. This is a finite induction using earlier stages only. ∎

The independence just proved is at fixed \(W\). Joint continuation still requires D3's qualification on all declared analytic components of \(W\). Likewise the smooth strip cutoff is never complexified. For fixed strip variable its Jacobian is affine in the analytic discrepancy, and its reconstructed bond is a holomorphic logarithm on the prescribed branch (ST1 F1). Haar and coarea coefficients are holomorphic by FM5. Carried activities compose the maps
\(Z\mapsto u\mapsto a_V(u)\mapsto b_V(a_V(u))\mapsto h_Y\mapsto P\dotplus zh_Y\mapsto f\).
H supplies the branch, DR source ball, target-domain inclusion and old CI at every arrow. Kept forms and normalizers require their actual pair-function supply. These are conditional analytic statements, not consequences of a bounded real integrand.

**Lemma 7 (OT: older-test margin — Outstanding).** Let \(\tau\) be any older type-(58) datum-loop test in the specified stored integrand whose level-\(j\) stencil contains a moved row. Use its own recorded threshold
\[
 t_\tau=C_{\rm te}L_\flat^{2\mathcal E_{\rm old}(\tau)}
                 \varepsilon_{m_{\rm old}(\tau)},\qquad C_{\rm te}=6C_{\rm sm}L^4.
\]
Let \(n_\tau\) count moved bond occurrences in its oriented loop. The precise remaining margin assertion is, uniformly over every admitted finite history, passing stage and real datum in use,
\[
 |\partial V(\tau)-I|\le t_\tau-K_\tau\delta'_j,
 \qquad K_\tau=\tfrac98n_\tau C_{\rm ch}L^4. \tag{OT}
\]
For a plaquette one may use \(K_\tau=\tfrac92C_{\rm ch}L^4\). The constants have D4's order. No proof or admitted-history counterexample is established here.

**Lemma 8 (what OT would prove).** OT makes the corresponding older indicator redundant on \(D_b\).

*Proof.* F2 and FC1 give \(\|a_V(u)\|<\tfrac98 C_{\rm ch}L^4\delta'_j\). In a real loop product, replace each moved bond in turn, including inverses with their unitary transports. Each replacement changes the product in operator norm by at most that bond's group angle. Hence
\[
 |\partial D(Z)(\tau)-\partial V(\tau)|<K_\tau\delta'_j.
\]
The triangle inequality and OT give \(|\partial D(Z)(\tau)-I|<t_\tau\), as required. ∎

OT is sufficient, not necessary, for redundancy. Its margin uses an upper bound on the largest change; that bound need not be attained in the outward direction. Even a refutation of OT would not by itself refute FC-test.

Three attempts to establish OT have the following precise limits.

1. **Profile and fine-from-coarse control.** On a complete averaging carrier lying in new layer \(j+1\), iteration of AV/CURV followed by PROF suggests the bound \((1+o(1))C_P(L)L^{-2}\) times the new datum profile. To turn it into \((1+o(1))4C_P(L)L_\flat^4L^{-2}t_\tau\), one additionally needs
   \(\mathcal E_{\rm new}(\tau')\le\mathcal E_{\rm new}(x)+1+d(x,\tau')/\rho_0\),
   \(\mathcal E_{\rm new}(x)\le\mathcal E_{\rm old}(\tau)+1\), and the corresponding radius-index comparison. The layer-distance estimate and \(\delta\rho_0\ge64\log L\) then sum the profile as in ST1 L675–678. At a selected \(L\), \(8C_P(L)L_\flat^4<L^2\) would leave fixed fractional room on those carriers. The profile proof, a3-profile L290–295 and L616–666, permits dependence on \(L\) through its inverse, chart and localization constants; it supplies no such inequality. The condition \(C_P(L)=o(L^2)\) would suffice to choose \(L\), but is not necessary. Nor does (56)'s polynomial upper envelope compare inherited exponents to the old local threshold. At a seam the averaging carrier can meet the lower layer, so the uniform \(L^{-2}\) step itself needs a separate estimate; ST1 imports the larger seam constant. CP12's derivative theorem supplies neither missing comparison. Thus even a better interior profile constant alone would not prove OT for every consumed loop.
2. **Graded stage thresholds.** SA 17612–17624 sketches the implication using additional curvature thresholds with a fixed graded margin. A test of this reference with \(|\partial V(\tau)-I|<(1-\beta_s/2)t_\tau\) would imply OT once \(K_\tau\delta'_j\le\beta_st_\tau/2\). For an own-level loop the ratio tends to zero by (Tq0). Frozen ST-test, however, tests free rows against \(V^\sharp\); (58) is an upper bound without this inward margin. Adding the reference test changes the passing branch and creates a new failing branch. Its gain, ownership, history rules and all other older-test implications need proof, including at the seams. SA's graded argument is not a proof for the changed test. No such change is adopted here.
3. **Indicator splitting and continuation.** Write an older indicator as \(1-(1-\chi)\). This gives an exact correction integral; it does not show that integral vanishes. Continuing the first part from a real open region of redundancy need not reproduce the actual stage integral elsewhere. ST1's example \(\int_{-b}^b\mathbf1_{|z+x|<b}\,dz=2b-|x|\) exhibits the possible failure. Exact redundancy would suffice, and OT would prove it, but neither is necessary for every possible cancellation of an integral. The draft's asserted equivalence to OT was too strong.

Passing of one old datum in the same \(D_b\) chart gives only \(|\partial V(\tau)-I|<t_\tau+K_\tau\delta'_j\). It gives no lower margin. A thin-shell counterexample would require a specified nonzero-weight admitted history and its CV critical reference with \(|\partial V(\tau)-I|>t_\tau-K_\tau\delta'_j\), together with all older tests, stage selection and stored-variable constraints. A freely chosen smooth field or a tunable upper bound does not provide this history. No such witness has been constructed.

**Outstanding — complete factor accounting.** Theorem FM preserves whatever full integrand is supplied; its list of factor types does not specify that integrand. The draft treats its classes as exhaustive without proving this for the actual stage. In particular SA 17396 and 17624 also discuss older approximate-fluctuation tests. Their replacement by one for SA's design is not inherited automatically by ST-test. For each such factor one must identify its fixed rim/stored read, or prove its redundancy, or provide its permitted analytic treatment. The same applies to any nonconstant Borel factor in the analytic datum. This is part of FC-test's existing actual-integrand obligation, not an additional permission to drop factors. Lemma 6 settles the stopped-stage level range but does not supply a missing factor register.

**Theorem 9 (FC-test in the frozen consumer's sense).** Assume H, (8), OT, and the following complete accounting for the specified stage. Each retained factor, including earlier failures and approximate-fluctuation tests, is either holomorphic jointly in \(Z,W\) near the relevant closed contours, a fixed Borel factor in D3's sense, or an indicator covered by Lemma 5, Lemma 8, or another supplied redundancy proof. Earlier-stage outputs have their domain and majorant hypotheses already established. Then the full remaining integrand has FC2's analytic premise at every fixed Borel parameter, after harmless replacement of redundant indicators. Thus it supplies FC-test to Theorem 14 hypothesis 5, Corollary 14′ and geoh Lemma 10. For holomorphy after outer integration, also assume FC2's locally uniform integrable majorant.

*Proof.* Lemmas 5 and 8 replace their indicators by one without changing any real passing integral. D3 handles fixed Borel factors. The analytic maps following Lemma 6 handle the supplied activity, strip, form and coarea factors. Apply Lemma 6 inductively to earlier passing outputs. Completeness of the accounting now covers every factor, so their product is jointly holomorphic at fixed Borel parameters. Under the majorant, pass the Cauchy integral formula through the rim integral and the bounded \(Z\)-domain. This proves holomorphy in \(W\); agreement on the open real slice and connectedness give uniqueness. ∎

The majorant is a separate requirement. One sufficient form, after including all analytic prefactors, is a bound on each compact parameter set by
\(C_K e^{-c_a|\mathfrak a|^2/4}\), with \(c_a>0\). It follows, for example, from \(\Re S_a\ge c_a I\) and a bound of the remaining log modulus by \(c_a|\mathfrak a|^2/4+C_K'\), where \(S_a=\Delta^{\rm loc}(V)\). Gaussian integrability follows by a product of one-dimensional Gaussian integrals. Neither a pointwise bound on the final integral nor a fixed-rim bound \(\mathcal M\) proves this domination. NL1-L (18), CI-form H-G/H-S and IN1 H-E keep that distinction.

**Theorem 10 (the conditional stage contour).** Assume Theorem 4's actual-family identification and Theorem 9's hypotheses and majorant, uniformly wherever a stage contour is consumed in an admitted finite history. Then (6) is the exact real stage integral and its unique holomorphic continuation. Its matched centre satisfies (3). For every fixed real vector \(\nu\) with \(|\nu_e|\le b/16\), in particular \(\nu=\Im m\), the fixed-boundary map of FC9 gives the exact deformation inside \(T_b^\sharp\). FC8 maps this tube by \(Z\mapsto\beta(Z)\) into F4's tube \(\mathcal T_j\). This supplies the contour clauses, with all other consumer premises retained.

*Proof.* Theorems 4 and 9 supply matching and analyticity; Lemma 2 supplies real equality. Apply FC9 at fixed parameters and then use the common majorant for the outer integral. Its bump equals zero outside radius \(13b/16\) and one inside \(7b/16\), so the deformation fixes the boundary and stays in the tube because \(13b/16+b/16<b\). Its rank-one Jacobian is exactly FC9's factor. For one bond, align the first real coordinate with \(\nu_e\); the one-dimensional contour homotopy has fixed endpoints. The integral of its parameter derivative is a boundary term and vanishes. Fubini iterates over the finite row set, under the majorant. Finally FC8 gives \(\|u(Z)\|<9\delta'_j/4\), hence \(\beta(Z)\in\mathcal T_j\). Notice that \(T_b^\sharp\) and \(\mathcal T_j\) use different coordinates; their relationship is this map, not literal inclusion. ∎

## Result

The hand arguments prove CV equality of the absolute and relative-trace gauge functions and identification of their Hessian with the Y3 form, zero first variation, the exact Gaussian/remainder identity, the recentring bound, the conditional linear-force estimate, and redundancy of the moved soft-gauge indicators. They resolve the stage-range reading in draft Lemma 4.3. Theorems 4, 9 and 10 state exactly the additional hypotheses needed by the frozen contour consumers. **OT remains unproved and unrefuted.** Actual-family identification, complete factor accounting, domains/LOC, and uniform analytic domination remain explicit; item 7 is not closed.

The imports are H and D4's early uniformity, the specified complete Haar/delta presentation and SLOT-ST, the actual HM/CI family and rim forms, and the separately stated factor and majorant premises. No CA-I presentation is identified. This is a distillation and correction of our draft, with conditional extensions of its hand arguments. It makes no correction or novelty claim about the Sussman–Alpoge manuscripts.

Corrections to the draft, including its proposed corrections to frozen texts:

1. **Lemmas 3.1–3.2 survive.** At a moved CV pair the absolute and relative-trace functions agree on the common branch; their Hessian equals Y3's quadratic form. FC5 L1221's conditional premise is established for these level-\(j\) pairs. FC5 is not wrong; its separate coverage/precision warning remains necessary. Zero first variation does not identify a full conditional Gaussian.
2. **Remark 3.4′ and Theorem 3.4 were overstated.** The arbitrary-split identity does not settle NL1/LF1's actual precision. Keep normalization, coefficient ratios, current extension, marginal/compressed distinctions and switched carriers in the matching obligation. No arbitrary external-pair dependence is determined by holomorphy in the physical datum alone.
3. **Proposition 3.5 is an exact recentring, not localization of the precision.** Its correction has the sign and bound in (7). The origin matches \(V^\sharp\) on free rows only. Use factorwise logarithms in (5); FMd does not put their whole product near one, and \(J(m)\) need not vanish.
4. **Proposition 3.7 bounds only its stated linear truncation.** A full quadratic model uses \(S-\mathcal R''(m)\); an exact saddle needs further nonlinear control. Fixed-rim and dimension-dependent bounds do not supply a uniform contour centre or an outer majorant. A larger centre bound also requires rechecking FC9's fractions.
5. **Lemma 4.2 survives with explicit AV branch room.** SA L7181's \(\Re\operatorname{tr}\) agrees with ST1 L1218's \(\operatorname{tr}\) on real \(SU(2)\) data. The latter is the correct holomorphic extension; neither real formula is erroneous.
6. **Lemma 4.3 needs the full frozen read.** Use \(t-N_t\), not \(t-N_t^0\), and the stopped test's whole birth-level datum. Independence of moved rows alone does not imply joint holomorphy in \(W\). The draft's exhaustive factor assertion and its treatment of all older tests were not established.
7. **OT is sufficient, not equivalent to FC-test.** The profile route additionally needs inherited-threshold and seam control. Subquadratic growth of \(C_P(L)\) is sufficient, not necessary. Adding a graded reference test changes the operation and needs its failure gain; indicator splitting leaves an unestimated correction. A thin-shell reference must be realized in an admitted history before it refutes OT.
8. **ST1 L1431–1432 has only a wording defect.** The action-plus-gauge function has zero linear term; a Hessian itself has no linear term. The proof in Lemma 1 gives the intended statement.
9. **The draft's correction of assembly-status is not justified.** ST1 and geoh are direct consumers, but the edge FCON → CI is a valid indirect dependency. NL1-L L565 explicitly requires contour and normalization identities before its formation representation; its stage CI-form also needs them. Keep the edge, clarifying the intermediate consumers if desired. The draft's zero-count search missed this occurrence.
10. **Final scope and coordinates are corrected.** SLOT-ST still has actual storage premises, DOM-draft is not frozen supply, and FC8 is a coordinate-map containment. Neither the exact split nor the contour identity proves positive precision, the full remainder estimate, CI, or an admissible history realization.

**Definitions supplied, including local notation:** D1's variable partition \((E,C_+,F,N,\mathfrak a)\), references, \((g,\ell_j,\delta',\varepsilon_j,b)\), \((\eta,m,u,\beta,D)\), domains and block norms; D2's import package H; D3's stored presentation, moved factor, redundancy and analytic/Borel distinction; D4's \(\mu_\sharp\); Lemma 1's carried pair set, \(\Gamma_{\mathcal P}\) and relative-trace function; D5's \((\mathcal W,\mathcal K,S,R_{\rm rec},T_3,P_{\rm slot},K_1,J,\mathcal R,Q,s)\) and logarithm branches; Lemma 3's \((s_1,R_0,\mathcal M,c_S,f)\) and linear-force model; Theorem 4's actual-family identification; Lemma 5's \((C_{\rm av},C_{\rm gi})\); Lemma 7's own-record threshold \(t_\tau\), moved-occurrence count \(n_\tau\), \(K_\tau\) and OT margin; Theorem 9's complete factor accounting and the sufficient-majorant notation \(S_a,c_a\); and Theorem 10's deformation vector \(\nu\). Reintroduced inherited objects retain their stated imports.

Only `library/fcon.md` and its source-check record were written in the checkout. No frozen text, gate, ledger, status file or editable prompt file was changed. **This text is not yet refereed, is not an audit, and grants no status.**
