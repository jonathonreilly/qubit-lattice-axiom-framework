# CI: whole-domain base, form, and Mayer domination

Provenance: Codex (GPT-6), Pass 2 distillation of Claude's `ci-draft.md`, at repository commit `77146588eae28c7e571ea59b6eb4caebf2769561`; research text, not an audit, grants no status, not yet refereed. Sussman–Alpoge material is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, at `31a47c543775`.

All arguments below are by hand. The background and integration methods also retain their credit to Tadeusz Bałaban and Jonathan Dimock. “Proved” below means the displayed implication, with its hypotheses; it never means that the actual construction satisfies them. Only this file is changed.

## 1. Definitions and consumer contract

**D1 (domains and coordinates).** Fix a finite admitted history and a main step \(n=i-1\to i\). Use ST1-r4 with Tq0, CV, GS, permanent records, R1 cores and their original radius indices. A fibre fixes real \(U\), geometry, branches and Borel stored data; its analytic coordinates are \(P=(U,A',\mathbf J)\), together with every declared holomorphic stored coordinate and surviving coupling/source variable. The current is independent. The pair is \((e^{i\eta A'}U,\mathbf J)\). Every assertion on a whole domain quantifies over **all its local fibres**, not only restrictions of global fields.

Write \(g=\theta_n^{-1/2}\), \(\ell=\log\theta_n\), \(R=\ell^q\), \(\mathfrak b=C_{\rm win}A_1\ell^{p_0}<R\). In nl1-L's Pauli coordinates, \(|\zeta|_\infty=\max_{b,a}|\zeta_{b,a}|\) and \(u(b)=g\sum_a\zeta_{b,a}T_a\), with \(c_T=3\) for its matrix norm. Real cutoffs are fixed bond balls of Euclidean radius \(\mathfrak b\). Do not replace \(g\) by \(x^{-1/2}\) when \(x\) is complex. Fine cubes have side \(M\); their corner graph has degree at most 80. A bond has one owning cube. \(\mathcal G\) is the set owning integrated bonds, \(d\) its periodic cube distance, and \({\rm St}(Y)\) the least tree edge count covering \(Y\), with extra vertices allowed. For connected \(Y\), \({\rm St}(Y)=|Y|-1\). IN1's \(d_j(X)\) instead measures an in-domain geometric tree in units \(M\); these lengths are not silently identified.

**D2 (switched presentations).** Use exactly nl1-L (5):
\[
 H_f=h_0(P)+h(s;P,S(v_0\oplus u(s\odot\zeta)))-h(s;P,S(v_0)),\quad
 h_0=h(1;P,S(v_0)),\quad
 F_f=f\!\left(\rho_f^{\rm res}(P\dotplus\mathcal P_PH_f);\mathfrak q_f\right).
 \tag{1}
\]
A connected seed carrier \(X_f\) contains the old activity's complete reads, endpoint pillars, pin stencils and stored-slot reads. It is not automatically the external-pair carrier of \(F_f\). Put
\(\mathbb S_X(a)=\{s:s|_X=1,\ |s_c|<e^a\ (c\notin X)\}\), \(a>0\), and \(\mathbb D_R=\{|\zeta|_\infty<R\}\).
Component locality means nl1-L Theorem 4(2): at fixed \(P\), equal switches and fluctuations on the same component \(K_X(s)\) give equal values. The centre \(f_0(P)=F_f(P;s,0)\) is switch-independent. It need not be real at complex \(P\).

**D3 (CI).** The exact target is nl1-L D4/Theorem 7. Each initial or newly formed activity must have its declared bound, holomorphy, Borel dependence, realness, real ties, real-gauge covariance, restriction and overlap agreement, and near/far stored-slot rules on its entire chain domain. Late activity bounds cannot select earlier domain or precision constants. Formation requires fixed positive \(\sigma\)-finite measures and jointly Borel, parameter-holomorphic integrands such that, for every compact polydisc \(K\) in the fibre,
\[
 f(P)=\sum_\nu\int G_\nu(P,\xi)\,d\mu_\nu(\xi),\qquad
 \sum_\nu\int\sup_{P\in K}|G_\nu(P,\xi)|\,d\mu_\nu(\xi)<\infty .
 \tag{2}
\]
The supremum must have a Borel integrable majorant. This is **nl1-L (18)**. Contour and normalization identities precede (2). A bound on the final integral is insufficient.

**D4 (regular-gas requirements).** Retain ci-form H-D, H-G, H-S and its finite gas formulas (9)–(11). H-S includes exact formation, fixed cutoffs, normalized hereditary Gaussian assignments, wall factorization, physical identification and all identities in D3. H-G uses the actual normalized covariance
\(D=C+C\Gamma\Gamma^{\mathsf T}C\), symmetric holomorphic \(C\), rectangular holomorphic \(\Gamma\), real at real data, and references \(C_*>0,\Gamma_*\) fixed throughout each analytic fibre. Their early bound is \(\|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K\); the local dimension is \(m\le c_m(LM)^4|Z|\), and
\[
 \|C-C_*\|+\|\Gamma-\Gamma_*\|\le
 H_0e^{b_G\bar\kappa-d_GM}+\Delta_\gamma,\qquad
 \sup_{\theta\ge\gamma^{-2}}\Delta_\gamma\longrightarrow0.
 \tag{3}
\]
Matrix norms here are Euclidean operator norms. For HMA take its rescaled datum \((\tau^{-1}C,\tau^{1/2}\Gamma)\), \(\tau=x/\theta_n\).

The remaining exact requirements are:

* **H-C:** the presentations in D2 obey \(|F_f-f_0|\le\omega_f\) on \(\mathbb S_{X_f}(\bar\kappa)\times\mathbb D_R\), and \(\sup_\Delta\sum_{X_f\ni\Delta}\omega_fe^{\alpha|X_f|}\le N_C\), uniformly before the coupling ceiling. The printed ci-form (5) takes \(\alpha=\kappa/2\). Lemma 3 below justifies only the explicitly modified version **H-C\('\)**, \(\alpha=\kappa/(2c_X)\), under its carrier assumptions.
* **H-W:** literally ci-form (6)–(7)/nl1-L Lemma 3 requires an affine finite-range read \(w_f\), \(\|w_f\|\le\delta_0+c_Tg|\zeta|_\infty\), where \(\delta_0=C_{\rm st}A_1g\ell^{p_0}\); a holomorphic \(\phi_f\) on radius \(c_W\), real on real inputs, with \(|\phi_f|\le B_f\) and vanishing derivatives below integer order \(k_f\ge1\); complete range \(2R_W+2<M\), \(\delta_0+c_TgR<c_W/2\), multiplicity \(C_WM^4\), and \(a_W=2C_WM^4e^{15\lambda}\max_f B_f[(\delta_0+c_Tg\mathfrak b)/c_W]^{k_f}\to0\). The replacement below proves the *potential conclusion* where its different premises hold; it does not prove those affine premises.
* **H-I:** with the **original** scalar part, ci-form (32) requires a holomorphic complete exponent, real on real inputs, and the pointwise decomposition
\(\Phi_\omega=\Phi_\omega^\circ-q_\omega/2+V_\omega\), \(\Phi_\omega^\circ\) real, \(q_\omega\ge0\), \(|V_\omega|\le C_I N_0(\omega)\). Here \(N_0\) is the additive own-level stored-site count, including collars and coordinate multiplicities. A supplied finite ceiling \(\Phi_{\omega,*}^\circ\ge\sup_P\Phi_\omega^\circ(P)\) gives
\(\Re(\Phi_\omega-\Phi_\omega^\circ)\le C_IN_0\) and
\(\sup_P|e^{\Phi_\omega}|\le e^{\Phi_{\omega,*}^\circ+C_IN_0}\).
Separate holomorphy of \(q_\omega,V_\omega\) is not asserted. This remains distinct from oscillation.
* **UM1-rest:** every non-gauge type is holomorphic on its declared boxes/cores, has H-S's interface, and
\[
 |V^a(Y;P,b)|\le a_a e^{-\lambda{\rm St}(Y)}
       \left(1+M^{-4}\sum_{\beta\subset Y}|b_\beta|^2\right),\qquad
 a_{\rm rest}:=\sum_{a\ne{\rm GF}}a_a\le W_0/4 .
 \tag{4}
\]
The bound is needed on each required real box; globally free types need it on the full real space. Holomorphic extension alone does not delete a cutoff.

**D5 (imports, with their scope).**

| Import | Precisely retained supply |
|---|---|
| MAP/OLD | nl1-L H-ST, H-FL, H-DR, H-ACT, (8)–(9), Theorem 4, and earlier CI, with ST1-r4 CV/GS in place of stale r3 pointers. Actual term identification is separate below. |
| DOM | dom's S/M, persistent roster and complete local coverage, actual input membership, half-gap substitution, R4 or its explicitly matched corrected envelope, every island's fixed creation-domain inclusion, and whole-domain shrinking for (3). Dom Theorems 3, 6–8 are conditional implications, not this actual supply. |
| DR | dr W/ONE, PW, NL, column, Rows/Pair, ABS, S-loc, LIFT, regional admission and matching. Frozen pw now supplies PW on its regular envelope under P82, the repaired walk specification and parameter condition (P). Rows/Pair, NL and ABS have the stated supplier in rows.md, **not yet refereed**. Admission and transport remain separate. |
| HM | frozen hma M, PIV, FG/UM, adopted D4 full-read assignment, early envelope, shrinking domains, fixed-cutoff structure; PH1–PH4 and actual branch/constraint match for physical G-ID. Its Theorems 2, 4, 8 and Lemma 3 are used only under these premises. |
| GEO/RUN | actual TD hub/gas separation, complete lifted reads and projection conventions; geoh's actual record, ownership, class and reserve interfaces; dom Theorem 1/geoh Lemma 1 for \(\check R_i\ge(\ell-1)^r\). IN1 H-G alone does not assert TD's hub geometry. |
| LF | IN1 H-O (18) on fixed complex creation domains; H-E (16) when stored variables are integrated; H-LF/H-SUM when exact operation/history sums are used. These remain actual-formation imports. |
| STAGE | fcon's actual-family match, complete factor accounting, OT/test margins, admitted tubes and common outer majorant; stage-specific boxes and BOX at outputs. Fcon does not close these premises. |
| FILE | drlocp's joint pair-locality/labelled bounds and G-P, cls's complete-read/multiplicity/Lift/Mon premises, and the four matching conditions in §6. These texts are not yet refereed. |

**Outstanding — FORM.** No symbol in this table defines missing maps into existence. In particular, declaring the draft's (2.1) to be the complex exponent does not prove agreement with the actual operation, stored factors, or branches. Agreement on physical pairs cannot determine independent-current dependence. Keep **FORM** as the explicit hypothesis that the proposed decomposition is the complete actual exponent, with its fixed zero-value normalizations, on every declared local fibre.

**D6 (constant order).** Follow IN1 rows 1–10 and Amendment 1. Fix power-count constants first, taking \(C\ge3\), and \(q>\max(3p_0,p_0+2r,p_0+2r_R,Cp_0)\), with IN1's other exponent inequalities and nl1-L's already chosen lift budget \(r_R\). Fix geometric conversion, read and multiplicity conventions, \(c_X=4802,C_{\rm pr},c,C_{\rm isl}\) before \(L\); all constants used to choose \(L\) must be uniform in \(L\). Enlarge \(C_h^{\rm WF}\ge c_X\), then choose odd \(L\) above IN1/TD/CLS's retained floors. Fix analytic, response, Gaussian and any HOL-K constants **before \(\kappa\), independently of \(M,\bar\kappa\)**. Lemma 9's stronger Gaussian constant is fixed here, and \(W_0\) is chosen using it.

Choose \(\kappa\), then the gas rate \(\lambda\) in ci-form (15), additionally \(\lambda+1\le\kappa/(2c_X)\) and \((\lambda+1)C_{\rm pr}\le\kappa/4\). Enlarge the early \(L\) floor if these slopes require it, as td2 (13) does. Next choose \(\bar\kappa\) above all TD/CLS and Cauchy floors; for §7 require
\(\log[(e^{\bar\kappa}-1)/2]\ge\max(\Theta,\lambda+1)\).
Then choose \(M\), a power of \(L\), above read, decay, Gaussian and collar floors. Only then choose box/radius amplitudes \(A_1,A_0,C_0,C_1\), activity/list/age bounds and all other IN1 row-7–8 constants. Finally choose \(X_0=\gamma^{-2}\) for every smallness/admission ceiling, then actual run/torus data. A purported supplier which cannot meet this order remains Outstanding.

## 2. Elementary analytic statements

**Theorem 1 (CI-base).** For the bare presentation specified in IN1 L219, the Wilson plaquette functions satisfy CI on each initial domain with its declared finite radius. If that domain imposes \(\|W_p-I\|_{\rm op}<a\eta^2\), then
\[
 a_p=1-\tfrac12{\rm tr}W_p=\tfrac12\det(I-W_p),\qquad
 |a_p|\le\tfrac12a^2\eta^4 .
 \tag{5}
\]
A coefficient-weighted activity has the additional factor \(|x_0|\). There are no initial regular families, islands or stored-slot clauses.

*Proof.* Positive links are \(e^{i\eta A'(b)}U(b)\); negative links are their inverses, which are also entire functions of \(A'\). Their determinants equal one. The \(2\times2\) determinant identity gives (5); Hadamard's inequality gives \(|\det X|\le\|X\|_{\rm op}^2\). At real Hermitian traceless \(A'\), all links are in \(SU(2)\) and their traces are real. Gauge transformations conjugate \(W_p\). The function depends only on its four link variables, not on the splitting or independent current; hence it is Borel, respects restrictions and common lifts, and has all ties. If only \(\sup_b\|A'(b)\|_{\rm op}\le a_1<\infty\) is given, use \(\|W_p\|\le e^{4\eta a_1}\) and \(|a_p|\le(1+e^{4\eta a_1})^2/2\). These are whole-domain bounds. Entirety alone would give no uniform bound on an unbounded initial domain. ∎

**Lemma 1 (order-\(k\) switched localization).** Let \(\Phi\) be jointly holomorphic and component-local on \(\mathbb S_X(a)\times\mathbb D_R\), with \(|\Phi|\le B\) and connected \(X\ne\varnothing\). Let \(\mathsf R_k=\mathrm{Id}-T_{k-1}\), \(k\ge1\), where \(T_{k-1}\) is the Taylor polynomial in \(\zeta\) at zero. For \(Y\supset X\), put switches to one on \(X\), to \(\tau\in[0,1]^{Y\setminus X}\), and zero elsewhere, and define
\[
 f_Y^{(k)}=\int_{[0,1]^{Y\setminus X}}
       \partial_\tau^{Y\setminus X}\mathsf R_k\Phi(s_Y(\tau),\zeta)\,d\tau .
\]
The empty derivative is evaluation. Then
\[
 \sum_{Y\supset X}f_Y^{(k)}=\mathsf R_k\Phi(1,\zeta),\qquad
 |f_Y^{(k)}|\le(k+1)B(r/R)^k(e^a-1)^{-|Y\setminus X|}
 \quad(|\zeta|_\infty\le r<R).
 \tag{6}
\]
Disconnected \(Y\) gives zero. Each piece reads fluctuations only in \(Y\), is jointly holomorphic, and inherits reality.

*Proof.* Iterate the fundamental theorem of calculus in the unfixed switches. A component of \(Y\) missing \(X\) has no connection to \(X\) through nonzero switches; component locality kills its derivative. It also proves the fluctuation-read assertion. On a complex line \(\zeta=te\), Cauchy bounds each Taylor coefficient by \(BR^{-j}\); thus \(|\mathsf R_k\Phi|\le(k+1)B\) on \(\mathbb D_R\). Divide its order-\(k\) zero by \(t^k\), and let the maximum-principle circle increase to \(R\). Apply Cauchy in the distinct switch variables on circles about real \(\tau\) of radius \(r'<e^a-1\), then let \(r'\) increase. There is no derivative factorial. Compact integration preserves Cauchy's formula and reality. If \(\Phi=F-f_0\), already bounded by \(\omega\) and zero at \(\zeta=0\), the \(k=1\) constant improves to \(\omega\). ∎

**Lemma 2 (shell decay).** If \(|F-f_0|\le\omega\), \(F(s,0)=f_0\), and the hypotheses of Lemma 1 hold at rate \(a_*>a_1>0\), then, with \(G_X=d(X,\mathcal G)\),
\[
 |F(s,\zeta)-f_0|\le
 \omega e^{-(a_*-a_1)G_X}|\zeta|_\infty/R
 \quad(s\in\mathbb S_X(a_1)).
 \tag{7}
\]
An empty gas gives zero. The more general difference \(\Phi(s,\zeta)-\Phi(s,0)\), \(|\Phi|\le B\), has \(2B\) in place of \(\omega\).

*Proof.* For each shell \(1\le j\le G_X\), multiply all its switches by \(t_j\). The resulting function is bounded on \(|t_j|<e^{a_*-a_1}\). If any \(t_j=0\), the component of \(X\) contains no gas cube, so the difference vanishes. Successively divide these zeros and apply the one-variable maximum principle. Evaluating at all \(t_j=1\) gives the exponential factor. Divide the remaining zero in \(\zeta\) along a complex line to obtain (7). The case \(G_X=0\) is ordinary Schwarz. ∎

This proves the analytic content of draft Lemmas 4.1–4.2, with a sharper centered constant. It uses no layer-distance estimate. The stored source still affects \(F-f_0\) through the derivative of the response at that source; it is **not** confined to \(f_0\). Component locality, uniformity in stored data and complete pin reads are what make (7) valid.

**Lemma 3 (carrier payment and its limits).** Suppose \(X\) is a connected old \(M\)-cube polymer with tree length \(d_j(X)\), and its complete seed lies in the cube cover of the physical \(c_{\rm rd}<M\) neighbourhood of \(X\), in the same units. Then
\[
 |X_f|\le c_X(1+d_j(X)),\qquad c_X=2\cdot7^4=4802 .
\]
Suppose there are at most \(J_{\rm pt}(M)|X|\) indexed terms per \(X\), each with \(\omega_f\le2E_*e^{-\kappa d_j(X)}\). If \(\kappa\ge4c_X\log6400+4\), then
\[
 \sup_\Delta\sum_{X_f\ni\Delta}\omega_fe^{\kappa|X_f|/(2c_X)}
 \le972J_{\rm pt}(M)c_Xe^{\kappa/2}6400^{2c_X}E_* .
 \tag{8}
\]
Here \(|X|\) counts cubes. If pointing is at unit sites, its \(M^4\) multiplicity belongs in \(J_{\rm pt}(M)\).

*Proof.* Double a covering tree of length \(d_jM\). At most \(2d_j+2\) points spaced by arclength \(M\) cover it within \(M\). Each met cube and its \(c_{\rm rd}\)-neighbourhood fit in an open sup-ball of radius \(3M\); this meets at most \(7^4\) fine cubes. For \(n\le d_j<n+1\), there are at most \(81\sum_{k\le c_X(n+2)}6400^{k-1}\le162\,6400^{c_X(n+2)}\) old polymers within the required neighbourhood of a given seed cube. The rooted animal bound follows by a canonical doubled spanning-tree walk of \(2(k-1)\) steps, with at most 80 choices per step. The exponential weight leaves \(2E_*e^{\kappa/2}e^{-\kappa d_j/2}\). Sum with the multiplicity \(J_{\rm pt}c_X(n+2)\); \(\sum_{n\ge0}(n+2)e^{-2n}<3\), giving (8). ∎

This is a sufficient rate conversion, not a refutation of ci-form's conditional H-C. Its original half-rate would require a stronger geometric/decay supply. The replacement needs the actual seed-collar hypothesis; long pillars or additional reads are not covered by naming \(c_{\rm rd}\). At age \(\nu\), even projected singleton old cubes can occur \(L^{4\nu}\) times per current cube. Constant functions show that the crude choice \(\omega_f=2b_f\) need not sum uniformly, although their true oscillation is zero. Thus this example refutes that *majorant argument*, not H-C itself.

## 3. Wilson terms and the off-physical Gaussian defect

**D7 (an exact candidate split).** At fixed \(g\), write the scalar Wilson-plus-Y exponent as
\(\Psi_0=-x\sum_pa_p(\Pi^{\rm W})-x\Phi_V^Y(C_V(g\zeta))\).
Write its Taylor polynomial as \(c+L\zeta+\zeta^{\mathsf T}H\zeta/2\), and put
\[
 K_{\rm def}=H+\tau\mathsf A^Y(P),\qquad
 \Psi-\Psi(P,0)=-\tfrac{\tau}{2}\zeta^{\mathsf T}\mathsf A^Y\zeta
 +L\zeta+\tfrac12\zeta^{\mathsf T}K_{\rm def}\zeta
 +V_{\rm W3}+V_{\rm GF}+V_{\rm pr}+V_{\rm J}
 +\sum_f(F_f-f_0).
 \tag{9}
\]
Here \(V_{\rm W3}\) is the scalar Wilson remainder of order at least three,
\(V_{\rm GF}\) is HMA's gauge remainder, and \(V_{\rm pr}\) is the **entire zero-subtracted** profile difference
\(\left[-\sum_p(x_p-x)a_p(\Pi^{\rm W}(P,\zeta))\right]_{\zeta=0}^{\zeta}\).
The Jacobian difference is \(V_{\rm J}\).
Equation (9) is algebraically exact for this candidate expression. FORM must identify it with the actual integrand, including stored terms and normalizers. This avoids counting profile remainders twice, and retains the \(\tau\) factor required by frozen hma (28).

**W-local (explicit additional premises).** For each plaquette, its composed scalar function has Lemma 1's holomorphy/locality and complete seed of at most 16 cubes. On all its switched evaluations,
\(\|W_p-I\|\le\sqrt2C_0g\ell^q\eta_{m(p)}^2\), and
\(\sup_\Delta\sum_{X_p\ni\Delta}\eta_{m(p)}^4\le C_{\rm pl}M^4\).
These require actual read geometry and weighted layer counting; H-ST does not state the draft's uniform layer-count constant \(C_{\rm lay}\).
For the profile estimate additionally require **PROF-tube**:
\(\sup_p|x_p-x|\le2t(\theta_n)\) on these same evaluations.
IN1 (3) bounds \(x_j\) relative to its **own** \(\theta_j\); it does not prove PROF-tube for every old-layer profile.

**JAC (exact import).** Factor \(j(P;u)=\prod_\nu j_\nu(P;u|_{{\rm st}_\nu})\) on fixed complete stencils of diameter at most \(c_{\rm rd}\), with at most \(C_{\rm jac}M^4\) factors per seed carrier. Each continued factor logarithm is jointly holomorphic for \(\|u\|<\rho_J\) on the whole external fibre, real on its real slice, and
\(|\log j_\nu(P;u)-\log j_\nu(P;0)|\le C_J\).
The constants are early. Positivity at real points alone does not supply this complex nonvanishing/branch assertion.

**Outstanding — actual W supply.** W-local, PROF-tube and JAC have not been derived on the whole prescribed local fibres. The next lemma proves their quantitative consequence; FORM must also identify the complete actual terms.

**Lemma 4 (three W estimates).** Under MAP/DOM, W-local, \(|x|\le5\theta_n/4\), \(\log(e^{\bar\kappa}-1)\ge\lambda+1\), and JAC where used, the three potentials have (4) with
\[
\begin{split}
 a_{\rm W3}&\le5C_{\rm pl}C_0^2e^{16(\lambda+1)}
                  M^4(C_{\rm win}A_1)^3\ell^{3p_0-q},\\
 a_{\rm pr}&\le4C_{\rm pl}C_0^2e^{16(\lambda+1)}
                  M^4C_{\rm win}A_1(t/\theta_n)\ell^{q+p_0},\\
 a_{\rm J}&\le e^{15\lambda}C_{\rm jac}C_JM^4
                         c_Tg\mathfrak b/\rho_J .
\end{split} \tag{10}
\]
The middle line requires PROF-tube. All tend uniformly to zero above \(X_0\to\infty\), under \(q>3p_0\), IN1 (3) and \(c_Tg\mathfrak b<\rho_J\).

*Proof.* Equation (5) gives scalar Wilson bound
\(B_p\le(5/4)C_0^2\ell^{2q}\eta_m^4\).
Apply (6) with \(k=3\). For connected \(Y\), multiply by \(e^{\lambda{\rm St}(Y)}\), use \(|X_p|\le16\), and sum:
\[
 e^{\lambda{\rm St}(Y)}|V_{\rm W3}(Y)|
 \le4(\mathfrak b/R)^3e^{16(\lambda+1)}|Y|e^{-|Y|}
                         \sup_\Delta\sum_{X_p\ni\Delta}B_p.
\]
This proves the first line. The profile bound is \(B_p\le2(t/\theta_n)C_0^2\ell^{2q}\eta_m^4\); apply (6) with \(k=1\). Schwarz applied to each zero-subtracted Jacobian logarithm gives the last line. Its seed has tree length at most 15. IN1's last tube limit is exactly \(C_0A_1(t/\theta_n)\ell^{q+p_0}\to0\). The remaining limits follow from negative logarithmic powers and \(e^{-t/2}t^N\to0\), proved by the exponential series with any integer exponent \(>N\). ∎

To derive W-local's curvature comparison from running radii, use the **full** frame bound \(\theta_m\ge\theta_n-c_5\) for old layers and \(\theta_i\ge\theta_n-\bar B\). The sufficient floor is
\(X_0\ge2\max(c_5,\bar B,e^{2q},1)\).
The function \(x^{-1/2}(\log x)^q\) decreases above \(e^{2q}\), giving the stated \(\sqrt2\) comparison. The draft omitted the \(c_5\) loss. The complete switched-domain inclusion, local reads and layer count still require W-local/DOM.

**HOL-K (new, not supplied).** Fix an admitted real critical reference
\(P_W=(U_+,0,J(U_+))\). With \(l=l_+(b)\), use the unnormalized regular-envelope norms
\(\|A'\|_{\rm reg}=\sup_b\max(l|A'|,l^2|\nabla^{U_+}A'|)\) and
\(\|J\|_{\rm reg}=\sup_b l^3|J|\); these do **not** divide by running radii.
There must be early \(\rho_K>0,K_H\ge1,c_H>0\), uniform in level, volume and geometry and independent of \(M,\bar\kappa,\gamma\), such that the **actual normalized** coefficients in (9) extend holomorphically to
\[
 \mathcal N_K(P_W)=
 \{\|A'\|_{\rm reg}<\rho_K,\
       \|\mathbf J-J(U_+)\|_{\rm reg}<\rho_K\},
 \quad
 |L_\beta|\le K_H,\quad
 |(K_{\rm def})_{\beta\beta'}|\le K_He^{-c_Hd_{\rm lat}(\beta,\beta')}.
 \tag{11}
\]
Here \(d_{\rm lat}\) measures level-\(n\) lattice units and includes colour-count conventions. This is the draft's fixed-radius import, with the missing \(\tau\) normalization repaired. Also require **CENTRE**: FORM identifies the action expanded at \(\zeta=0\), including its stored centre, with the physical action covered by HMA PH1–PH4, so \(L(P_W)=K_{\rm def}(P_W)=0\). A whole-domain application needs compatible patches of this kind covering **every** required local fibre, with
\[
 \delta_\gamma=\sup_P(\|A'\|_{\rm reg}
                  +\|\mathbf J-J(U_+)\|_{\rm reg})\longrightarrow0 .
\]
A bound on \(\mathbf J\) alone is not a bound on this difference.

**Lemma 5 (conditional defect bound).** Under HOL-K/CENTRE and \(\delta_\gamma\le\rho_K/2\),
\[
 |L_\beta|\le\epsilon_K,\quad
 |(K_{\rm def})_{\beta\beta'}|\le\epsilon_Ke^{-c_Hd_{\rm lat}},
 \qquad \epsilon_K=K_H\delta_\gamma/\rho_K.
\]
Group linear coordinates by their owning cube. Assign quadratic pairs to fixed shortest cube paths. With \(M\ge2\lambda/c_H\), they obey (4), with
\(a_{\rm lin}\le6\epsilon_KM^4\) and
\(a_{\rm quad}\le e^\lambda C_{\rm dec}\epsilon_KM^4\),
where \(C_{\rm dec}=\sup_\beta\sum_{\beta'}e^{-c_Hd_{\rm lat}/2}<\infty\).

*Proof.* Along \(P_W+t(P-P_W)\), the entry is holomorphic for \(|t|<\rho_K/\delta_\gamma\), uniformly bounded as in (11), and zero at zero. Schwarz gives the entry bounds. There are at most \(12M^4\) scalar coordinates per cube; use \(|z|\le(1+|z|^2)/2\). If a pair's assigned path has \(n\) edges, its endpoints have lattice separation at least \((n-1)M\). Split its exponential into two equal factors. One pays \(e^{-\lambda(n-1)}\); sum the other over the partner, using \(|zz'|\le(|z|^2+|z'|^2)/2\). Four-dimensional shell counts make \(C_{\rm dec}\) finite. These steps prove the stated norms. They prove fluctuation locality; external-pair filing of the coefficients remains FILE. ∎

**Outstanding — HOL-K and CENTRE.** Frozen hma proves the matrix envelope and the physical identity under PH1–PH4. It does not bound the action's normalized first derivative on (11), identify the stored centre there, or cover arbitrary local fibres by critical-centred patches. Frozen dr/pw and unrefereed rows bound the response to a reduced source on their admitted envelopes; they neither identify this Wilson Hessian with the independent-current precision nor give the normalized bounds (11). Cauchy on a shrinking running ball cannot yield a fixed \(\rho_K\).

The normalization obstruction is concrete: for the scalar action \(S(a)=a^2/2\),
\(-g^{-2}S(A'+g\zeta)\) has \(L=-A'/g\). Its physical value at \(A'=0\) is zero and its response is entire, but no \(g\)-uniform bound holds on a fixed \(A'\)-ball. On \(A'=g\ell^q\), it is \(-\ell^q\). This is a counterexample to the proposed inference from analyticity and physical matching, **not** to the actual YM coefficient. A cancellation or a different quantitative off-physical formation estimate is required. The draft's “unbounded defect if HOL-K fails” is also too strong: failure of a sufficient import proves no such conclusion.

## 4. The OSF-loc reduction

**D8 (the pointed object).** At old scale \(j\), sum a member over its domains at one base \(z\), with its hypothetical unit-translation/hypercubic companion. Subtract that **same** member's coefficient \(b[G]\), defined by CP12 D6/IN1 (5), times its midpoint tent action, and its vacuum value. CP12 D6 requires: normal convergence through two derivatives at the flat reference \((1,0)\); gauge covariance of the actual response; gauge-invariant members without fixed colour spectators; full pointed symmetry; uniformly exponentially summable absolute Hessian moments; the actual normalized response \(h=(H,d^*dH)\); affine constant-curl reproduction modulo gradients with zero current; and the stated action normalization. Cancellation is for this pointed total, not for each domain separately after absolute values.

**Lemma 6 (what CP12 already gives).** Assume CP12 D6–D7 for the actual window: its product datum ball, first-response bound (15) throughout the complex ball, doubled member-core room and all evaluations admitted; its affine decomposition (22), compatible boundary equations and exponential comparison; member and own-action bounds and coefficient estimate; rooted entropy, diameter/long-domain control; and \(\rho_\nu^2\le C(1+\nu)\), including young-age membership. With \(\sigma=L^{-\nu}\), one base contributes, after its own subtraction,
\[
 C\mathsf g(\rho_\nu^2\sigma^{4+\alpha_{\rm H}}
                         +\rho_\nu^3\sigma^6).
 \tag{12}
\]
After at most \(C(M)\sigma^{-4}\) bases, the bound is
\(C(M)\mathsf g f_\nu\), \(f_\nu=(1+\nu)^{3/2}L^{-\alpha_{\rm H}\nu}\), whose sum is finite. A vacuum-only member without colour spectators has instead \(C(M)\mathsf g(1+\nu)\).

Here \(\nu=n-j\); CP12 D7 uses age \(\nu+1\). IN1's list weight is correspondingly \(f_{\nu+1}^{\rm IN1}\). Its row-7 choice must majorize this displayed sequence after that index shift; a pre-existing numerical forgetting weight is not itself an oscillation estimate.

*Proof.* CP12 Lemma 8 annihilates the affine quadratic tensor of the complete pointed total. Here is the quantitative step of its Lemma 9. Cauchy on CP12 D7's response ball bounds the second response by \(C/r_B\) times the product of two half-rate decays. Integrating along the datum segment gives
\(\|\mathcal P^W(D)\|_X\le CD_X^sa_{\rm out}\sigma^2\) and
\(\|\mathcal P^W(D)-L_F\|_X\le CD_X^s(a_{\rm out}\sigma^{2+\alpha_{\rm H}}+r_B^{-1}a_{\rm out}^2\sigma^4)\).
Cauchy on the doubled member ball bounds its Hessian by \(Cg_X/a_j^2\) and its third-order remainder by \(Cg_X(\|\mathcal P\|/a_j)^3\). Expansion at \(L_F\) gives (12) times a polynomial in \(D_X=2+\operatorname{diam}X\). If the scaled radius is not small, the whole-core bound and \(1+t^2\le C_ct^3\), \(t\ge c>0\), give the same estimate. The counterterm has size \(C\mathsf g\) on its fixed support and obeys the same argument.

Sum the polynomial domain factors against the entropy gap. Complete the affine cancellation before taking its absolute value; the omitted tensor tail and the remote non-chart norm tail cost \(C\mathsf g(1+\rho_\nu^2\sigma^4)e^{-c/\sigma}\), which is absorbed in (12). Young ages use their supplied core membership and a fixed lower bound for \(\sigma\). Counting bases proves the result; the ratio of successive \(f_\nu\) tends to \(L^{-\alpha_{\rm H}}<1\). Without quadratic subtraction, \(DG(0)=0\) and second-order Cauchy give \(Cg_XD_X^{s'}\rho_\nu^2\sigma^4\), with the same tail/young-age treatment. ∎

**Outstanding — OSF-loc, one precise remaining transfer lemma.** For every old regular family \(G_j\), construct an **exact linear localization of its pointed, own-subtracted total** into presentations \(\mathcal F_f(P;s,\zeta)\), with connected complete seeds, the zero-centre/component/structural properties of D2, and actual declared local domains. Uniformly in all those external pairs and all fine switches \(|s_c|<e^{\bar\kappa}\), prove
\[
 \sup_\Delta\sum_{f:X_f\ni\Delta}
 e^{\alpha|X_f|}
 \sup_{\mathbb S_{X_f}(\bar\kappa)\times\mathbb D_R}
       |\mathcal F_f-\mathcal F_f(s,0)|
 \le C_{\rm OSF} f_{n-j}\|G_j\|_{j,\kappa},
 \quad \alpha=\kappa/(2c_X).
 \tag{13}
\]
For defects/remainders require the analogous vacuum-only bound with \(1+n-j\), under their actual OSF5/IN1 norm bounds. Non-exempt boundary/strip/kept terms need their own summable carrier budget; CP12 D6 does not cover a fixed colour spectator. The constant and any radius-ratio/point-count factors are fixed before \(\gamma\). The localization must preserve the cancellation inside each pointed total, pay its carrier weight and all multiplicities, and reproduce the specified actual exponent at \(s=1\).

Lemma 6 proves the *window-value estimate* needed in (13) under CP12 D6–D7. Three attempted implications still fail: (i) ordinary class bounds with (8) lose \(L^{4\nu}\); (ii) layer separation concerns the layer of a read, not the age of the reading member; (iii) pointed cancellation plus real (15) does not supply CP12 D7's smooth combined field, independent-current/core membership and affine-boundary comparison on every switched ball, nor the absolute carrier sum after regrouping. A bound on a signed total cannot be substituted into that sum. No new unspecified “lattice Poincaré lemma” is needed for Lemma 6; CP12 already supplies the conditional Taylor argument.

**Theorem 2 (conditional H-C\('\)).** If (13), the stated vacuum-only versions, and the remaining carried-kind budgets hold on the whole domains, then H-C\('\) holds, and
\[
 a_C=(\mathfrak b/R)N_C\longrightarrow0 .
 \tag{14}
\]
At fixed \(\theta_n\), the carrier budget is at most
\(C_{\rm OSF}[E_0\sum_{\nu\ge0}f_\nu+
 \sum_{\nu\ge0}(1+\nu)(L^{-(\nu+1)}
             +C_H(\theta_n+\underline\lambda\nu-c_5)^{-p})]
 +N_{\rm other}\), \(p>2\), with the actual norm constants retained.
Its supremum over \(\theta_n\ge2(c_5+1)\) is a finite choice of \(N_C\) before \(\gamma\). IN1's remainder bound permits \(p=\kappa_0/2\).

*Proof.* Sum the nonnegative bounds in (13). The defect sum is geometric. With \(y=\theta_n-c_5\ge\theta_n/2\ge1\),
\(1+\nu\le C(y+\underline\lambda\nu)\); comparison with the integral of
\((y+\underline\lambda t)^{1-p}\) bounds the remainder sum by \(Cy^{2-p}\).
For class potentials apply Lemma 1 in its centered form and use
\(\lambda+1\le\alpha\); charging each seed to a cube of \(Y\) gives
\(e^{\lambda{\rm St}(Y)}|V^C(Y)|\le(\mathfrak b/R)|Y|e^{-|Y|}N_C\).
Finally \(q>p_0\). ∎

**Dependency correction.** The route uses item 1's localized regularity, with CP12 (15) only on its stated admitted class. It uses the *actual-member normalization/covariance and companion match* included in item 9, plus items 4–5 for switched domains. It does not use the numerical one-loop value or the whole SF theorem to cancel a member's own coefficient. CP12 has already proved the conditional cancellation and window gain. Thus the actual graph needs the specific (13)/member-match edge before CI; this does not prove an unavoidable dependency on all of item 9. With the H-O route below, CI also conditionally reads a part of item 10. The planning sentence “Each depends only on earlier items” is not a valid ordering for these chosen interfaces.

## 5. Islands and the frozen H-ACT/H-FL clauses

**Lemma 7 (what H-O proves).** Assume IN1 H-O (18) and DOM's inclusion of every evaluated pair and arbitrary admitted shift into the fixed creation domain. At fixed stored \(\xi\), let \(o_f=\operatorname{osc}\Phi_{\omega,f}\). Then
\[
 |\Phi_{\omega,f}(\xi;p)-\Phi_{\omega,f}(\xi;p')|\le o_f,\qquad
 A_f(\xi)-\Re\Phi_{\omega,f}(\xi;p')\le o_f,\quad
 A_f(\xi)=\sup_p\Re\Phi_{\omega,f}(\xi;p).
 \tag{15}
\]
Thus td A (5)'s complex deficit is supplied with \(B_f=o_f\), and its oscillation route uses \(\widetilde\omega_f=o_f\). For the full exponent retain its supplied external-pair-independent scalar part \(\Phi^\circ_\omega(\xi)\). For a fixed reference \(p_*\) in that domain,
\[
 |\Phi_\omega(\xi;p)-\Phi_\omega(\xi;p_*)|\le O_\omega:=\sum_f o_f,
 \qquad |e^{\Phi_\omega(\xi;p)}|
       \le e^{\Re\Phi_\omega(\xi;p_*)+O_\omega}.
 \tag{16}
\]
No real reference is needed for these inequalities. At one carrier \(R\), H-O supplies the summed amplitude
\(B_\Phi(\log\theta_m)^{2p_0}e^{-\kappa d_m^\natural(\mathcal S;R)}\).

*Proof.* These are exactly the differences bounded by IN1 (8), since \(\xi\) is held fixed and both complex pairs lie in its defining supremum. Taking real parts and then the supremum proves (15); a finite value at one pair makes that supremum finite. Sum over the supplied carrier pieces and exponentiate to prove (16). ∎

**Outstanding — H-I and nl1-L L188.** Neither (15) nor (16) proves
\(\Re(\Phi_\omega-\Phi_\omega^\circ)\le C_\Psi V^\circ\), nor ci-form's \(C_IN_0\) bound relative to its original scalar part. Add an arbitrary positive constant \(N\) to one carrier: its oscillation stays zero while either proposed bound fails for fixed \(V^\circ,N_0\). Recentring into a new scalar \(\Phi^\circ+\sum_f\Phi_f(p_*)\) is allowed algebra, but changes the normalization being estimated; its exponential still needs H-E's integrable envelope. It does not satisfy the frozen consumer by renaming \(B_f\). Even an \(O_\omega\) bound has creation-scale logarithms and carrier counts, not the specified uniform volume bound. H-I or an explicitly approved replacement with its mass/normalization proof remains an import.

The draft's td X correction is useful **for carrier-resolved island pieces**: retain \(d_f^{\rm old}=d_m^\natural(\mathcal S;R_f)\) and its weight when the complete-read geometry is supplied. TD's zero length for a whole island is a permitted coarser convention, not a false theorem. It still requires its independently stated per-read sum. H-O excludes the one-sided counterexample in td only when its quantitative oscillation norm is imposed.

**Outstanding — H-FL's raw-datum supply.** Retain \(S(0)=0\), holomorphy on \(\|v\|<a_{\rm ch}\), \(\|S(v)\|_{\rm src}\le C_A\|v\|\), radius \(R_\sigma\) for source-row reads, and actual physical identification and source support in nl1-L L140–157. To obtain its raw bound (6), require **TEST-v0**: each stored free row is the same unscaled logarithmic datum, in the same norm and chart, which passed
\(\|v_0(b)\|\le C_{\rm test}A_1g_m\ell_m^{p_1}\) at some \(m\le n\), with early \(C_{\rm test}\). DOM's group-distance test does not itself state this logarithmic comparison.

The **literal full-source import** in nl1-L L130–157 is
\[
 \operatorname{supp}S(v_0\oplus u(s\odot\zeta))\subset\mathcal S_{\rm src},
 \qquad d_+(b,\mathcal S_{\rm src})
 \ge\rho_{\rm sep}(n-m_+(b)-3)_+-C_{\rm car},\qquad m_+(b)\le i .
\]
It includes the stored source. Here \(\rho_{\rm sep}\) is nl1-L's \(\rho_0\), distinct from §7's Gaussian tilt \(\rho_0\); choose \(\mu_R\rho_{\rm sep}/2\ge\log16\) in its early order. Keep its shift seminorm
\(n_b(H,K)=\max(l_+|H|,l_+^2|\nabla^UH|,l_+^3|K|)\),
and all of nl1-L (8)–(9)'s pinning/admission budgets. Neither TEST-v0 nor a gap to the integrated gas proves this source-support separation.

**Lemma 8 (stored threshold and geometric distance).**
(a) Under TEST-v0, \(p_1\le p_0\) and
\(X_0\ge2\max(c_5,e^{2p_1},1)\), H-FL (6) holds with \(C_{\rm st}=\sqrt2C_{\rm test}\).
(b) For an exempt term, suppose a current-level relative tree of length \(d_oM\) meets every unexcused cube and each chosen hull, the whole presentation set \(X_f\) lies in the cube cover of its domain's physical \(c_{\rm rd}<M\) neighbourhood, and \(X_f\) meets a hub or the live set. Then X° holds with \(C_{\rm pr}=2,c=2\), provided each excused hull lies in the corresponding current island hull \(H\), whose hub is \(\widetilde H=N_2(H)\). Explicitly, its tree \(T_f\) has at most \(C_{\rm pr}(1+d_o)\) edges and every cube of \(X_f\) lies in \(N_c(T_f)\) or in \(N_c(\widetilde H)\) for a hub \(\widetilde H\) met by \(T_f\). With X° and the TD gas gap,
\[
 d(X_f,\mathcal G)+C_{\rm pr}(1+d_o)+2c\ge G_0 .
 \tag{17}
\]

*Proof.* For (a), \(\theta_m\ge\theta_n-c_5\ge\theta_n/2\).
The function \(t^{-1/2}(\log t)^{p_1}\) decreases above \(e^{2p_1}\).
Its value is at most \(\sqrt2g\ell^{p_1}\le\sqrt2g\ell^{p_0}\), giving the bound.
For (b), sample a doubled relative-tree walk at arclength \(M\).
Consecutive owning cubes are equal or adjacent; their spanning tree has at most \(2(1+d_o)\) edges. Every unexcused cube met by the original tree is within one cube of this tree. Complete reads cost one more. Reads near an excused hull are in its \(N_2\) hub, met by the sampled tree. To prove (17), follow a shortest gas-to-read path, join the tree within \(c\) if necessary, and traverse it to a hub or live-set contact. If the read is already in a collared hub, only \(c\) more edges are needed. This constructs a gas-to-hub/live walk of the claimed length; G supplies its lower bound. ∎

**Outstanding — the draft's full-source claim.** Exemptness means *meeting* a hub/live set, not lying within two cubes of it. A carrier can follow a path of length \(G_0\) from a hub to the gas. It satisfies X° with a correspondingly long \(d_o\), but \(d(X_f,\mathcal G)=0\). Draft Theorem 11.1 therefore does not follow. Nor does (7) prove a lower bound for nl1-L's
\(D_f=\min_{b\in\mathcal R_f}d_+(b,\mathcal S_{\rm src})\): the stored source may meet those reads. The valid replacement combines (7) or TD's increment estimate with (17) and the old length weight. The literal full-source lower bound is not supplied. This preserves the useful difference estimate without discarding the long-carrier case.

**Outstanding — H-ACT identifications.** OLD supplies the interface only for earlier activities on their actual domains. Strip identification and its bound, elimination branches (for example a supplied \(|z-1|\le1/2\) gives \(|\log z|\le2|z-1|\) by its power series), exact W decomposition, kept-form relative carriage/native-action oscillation, and island-domain inclusion remain explicit MAP/FORM hypotheses. Formula (9) alone establishes none of these identifications. The stale nl1-L L127 reference must be read through ST1-r4's actual CV branch and its uniqueness/admission premises. Lemmas 1–2 are indifferent to the representative once their hypotheses hold; they do not verify those hypotheses after a representative change.

## 6. Ordinary TD, age and filing

Keep td2's **R, A, X, G, RUN, X° and G-ord**, including TD's unused but retained natural-route floors and contracted carrier premise. R includes the full row-product source ball, invariance under row masks and independent row scalings, source completion/chart/locality, at most 16 cubes per response stencil, \(M\ge R_\sigma+3\), and the response bound
\(n_b(h)\le C_DE_{\bar\kappa}\|S\|_{\rm src}e^{-\mu_Rd_+(b,\operatorname{supp}S)}\).
A is admission of every shift \(n_b(h)<A_b=A_Ve^{-\mu_Rd_+(b,\mathcal S_{\rm src})}\) on all complete reads; \(n_b(h_0)\le A_b/3\), and a doubled radius-\(A_b/4\) ball about \(h_0\) is admitted. Its amplitudes are two-sided bounds, kept-form oscillations, or (15). G requires hubs \(N_2(H)\), separation \(\check R_i-4\), side bound \(C_{\rm isl}L\check R_i+6\), their nonwrapping collars, and gas-to-hub/live distance \(G_0=10L\check R_i-2\). X° is the tree/read condition in Lemma 8(b); it must be supplied at every old level. G-ord fixes \(C_{\rm pr},c,C_{\rm isl}\) before \(\kappa\), uniformly in later \(L,M,\bar\kappa\).

**X/AGE (Outstanding for the actual multilevel family).** With the same admitted functions and their actual multiplicities, require
\[
 \widetilde\omega_f\le\widehat\omega_fe^{-\kappa d_o},\qquad
 \sup_c\sum_{f:X(f)\ni c}\widehat\omega_fe^{-\kappa d_o/2}
       \le N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}.
 \tag{18}
\]
One-level carrier entropy in cls Lemma 6 gives \(12(1+2V_*)\), with \(V_*=(D^*)^4\), only after its geometry, one-slot-per-carrier and rate \(\kappa\ge2\log76800\) assumptions. Per-read use must also count read collars, pointings, origins and stored factors. It does not count all older levels. In particular H-O carries \(\ell_m^{2p_0}\). At fixed \(\theta_n\), IN1 allows \(\theta_m=\theta_n+b(n-m)\) for arbitrarily large age; \(\ell_m\) is unbounded. A current-gap exponential alone does not supply (18). The draft's numerical one-level constant omits these read/multiplicity qualifications.

For precision, use td2 (4)'s
\[
\begin{gathered}
 D=e^{\bar\kappa}-1,\quad a=\tfrac12\log(D/6400),\quad \delta=(8e)^{-1},\\
 \varrho=\frac{\min(s_D/2,C_Ac_{\rm ch}L^{-9}/2)}
                   {c_TC_Ae^{\bar\kappa}g},\quad
 A_R=4C_DE_{\bar\kappa}s_DD^{15},\\
 A_V=C_DE_{\bar\kappa}C_A(3\delta_{\rm src}+c_Tge^{\bar\kappa}R),
 \quad K_1=\max(1,4A_R/A_V),\quad
 \vartheta=4K_1\mathfrak b/(\delta\varrho).
\end{gathered}
\]
Here \(\delta_{\rm src}\) must bound the actual stored datum, including \(C_{\rm st}\); impose \(C_A\delta_{\rm src}<s_D/2\) and \(\|v_0\|<c_{\rm ch}L^{-9}/2\). For nonempty gas \(W\), let \(m_f(W)\) be the MST on \(W\cup\{*\}\) with edges \(d(c,c')\) and root edges \(d(c,X(f))\). Boolean differences use one variable per gas cube.

**Theorem 3 (ordinary TD, conditional).** Under the preceding exact inputs, put
\(\lambda_T=\lambda+1\), \(\eta_H=1+C_{\rm isl}/10\),
\(\vartheta_T=\vartheta e^{\lambda_Tc}\),
\(a_1=a-6-\lambda_T(1+\eta_H)\), and
\(\nu_T=\min(\kappa/(4C_{\rm pr}),a_1/2)\).
Assume
\[
 10L\check R_i\ge6+2c+\eta_H(2+c),\quad
 \lambda_TC_{\rm pr}\le\kappa/4,\quad a_1\ge12,\quad\vartheta_T<1 .
\]
Then the exempt difference has the exact Boolean decomposition
\[
 \sum_f[F_f(P;1,b)-f_0(P)]=\sum_{\varnothing\ne W}V^{\rm ex}(W;P,b),
 \quad |V^{\rm ex}(W)|\le a_Te^{-\lambda_T{\rm St}(W)},\quad
 a_T=2e^{\kappa/4}N_{\rm ex}\vartheta_T
                 e^{-\nu_T(G_0-C_{\rm pr}-2c)}\longrightarrow0 .
 \tag{19}
\]
It is jointly holomorphic on the declared domains and fluctuation-local on \(W\). External-pair locality is a separate conclusion to prove.

*Proof.* TD Lemmas 1–4 give
\(|f_W|\le\widehat\omega_fe^{-\kappa d_o}\vartheta^{|W|}
e^{-(a-6)m_f(W)}\).
Their mechanism is as follows: switch localization of a response row, followed by the \(6400^{n-1}\) animal count, gives
\(\sum_{n\ge n_0}6400^{n-1}D^{16-n}\le2D^{15}(6400/D)^{n_0-1}\).
Independent source scalings supply one Schwarz factor per gas cube. Allocate a rooted MST's parent-edge costs \(l_c\). At threshold \(t\), vertices with \(l_c>t\) root distinct components of the graph of edges of weight at most \(t\); otherwise an exchange would shorten the MST. A tree joining any subset \(A\) to the root therefore needs at least \(\#\{c\in A:l_c>t\}\) edges above \(t\). Integrating in \(t\) proves
\(\sum_{c\in A}l_c\le{\rm MST}(A\cup\{*\})\).
On radii \((\delta/\beta_c)e^{(a-6)l_c}\), the composed shift sum is at most
\((A_b/4)2\sum_{r\ge1}(2e\delta)^r=(A_b/4)(2/3)\).
Thus A admits the composition and repeated Schwarz proves the displayed term bound. One-sided islands use (15) or TD's Borel–Carathéodory argument; no real-centre assertion is used.

Realize root edges as paths to complete reads. Join these to \(T_f\); a hub crossing costs at most its diameter plus \(2c\), paid by \(\eta_H\) times the gas-to-hub root-edge cost. The first ceiling gives
\({\rm St}(W)\le(1+\eta_H)m_f+C_{\rm pr}(1+d_o)+c|W|\).
The same path construction gives \(m_f+C_{\rm pr}(1+d_o)+2c\ge G_0\).
After weighting by \(e^{\lambda_T{\rm St}(W)}\), reserve
\(\kappa d_o/2+a_1m_f/2\) for summation. The remainder is at least
\(\nu_T(G_0-C_{\rm pr}-2c)\).
For fixed \(c_0\in W\), \(m_f\ge d(c_0,X(f))\); charge each term to a nearest read and use (18) and \(\sum_ce^{-6d(c_0,c)}\le2\). This proves (19). Finite Boolean inversion proves exactness. RUN and (18) leave a polynomial in \(\ell\) times \(e^{-c(\ell-1)^r}\); the exponential series proves its uniform tail limit. ∎

Assign \(W\) to a fixed minimal connecting tree \(Y\). Since \(|Y|={\rm St}(W)+1\), summing \(e^{-|Y|+1}\) over subsets \(W\subset Y\) costs at most \(e(2/e)^{|Y|}\le2\). Thus connected exempt potentials have norm \(a_{\rm ex}\le2a_T\) at rate \(\lambda\), with the same field dependence. This is td2 Corollary 4's fluctuation filing.

**Outstanding — old reads and actual filing.** For standing successors, cls Lemma 5 supplies projected *member* containment. It explicitly leaves full reads and units open. The draft's Lemma 8.2 assumes these away and substitutes members for hubs without preserving the stated gap. Under cls's actual D1–D4, its Lemma 7 is the available replacement: keep \(\eta_o=1+C/10\), impose its (10), and reduce the tail gap to \(G_i-C_{\rm pr}-2c-E_i\). Retired islands require healed-region containment. Neither this nor Lemma 8 proves X° for all actual older terms.

The required **(Cls+)** is exactly cls Proposition 12, conditional on:

* **Match-SF/O:** new-class inputs satisfy H-SF/H-O and return the required rate \(\kappa\), including every boundary origin.
* **Match-read/file:** all endpoint/stencil/pin reads, units, multiplicities, complete local domains, covariant regrouping and emitted scale/rate comparisons are supplied.
* **Match-heal/LD:** retired members lie in the actual enlarged healed region; its multilevel sum has the paid volume bound, and outside it the stated positive long-domain bound holds.
* **Match-history:** recursive records, including swallowed ancestry, exist and transport in every permitted local chart.

Additionally, drlocp Proposition 6.2 requires G-P and **weighted activities after Gaussian/Mayer formation**, including connecting paths and Gaussian read collars. Its Theorem 3 supplies weighted potentials only. These are explicit Outstanding steps. Pair locality on restrictions of global fields does not construct arbitrary local-domain functions. No altered excused-family amendment is applied to IN1 in this note.

## 7. Normal Gaussian and Mayer domination

**Lemma 9 (a uniform density majorant).** Under D4's H-G, let
\(B_K=K+K^4\), \(c_\Delta=5(K+1)^3\), and fix, before \(\kappa\),
\[
 \varepsilon_0\le\min\{1,(2Kc_\Delta)^{-1},
                      (8B_KK^2c_\Delta)^{-1}\},\qquad
 \rho_0\le(8B_K)^{-1}.
\]
These may also be decreased for any imported Gaussian comparison. Put
\[
 A^\#\ge\max\{1,A_K,\ Kc_\Delta+2B_KK^2c_\Delta,\ 2B_K\}.
\]
If \(\varepsilon\le\varepsilon_0\), \(0\le\rho\le\rho_0\), and a jointly Borel \(F\), holomorphic in the surviving analytic parameters, satisfies
\(|F(P,t;b)|\le F_0e^{\rho|b|^2}\) uniformly on the prescribed analytic domain, then
\[
 \int_{\mathbb R^m}\sup_{P,t}|\rho_{D(P,t)}(b)F(P,t;b)|\,db
 \le F_0 e^{A^\#(\varepsilon+\rho)m}.                    \tag{20}
\]
Use an upper integral if the supremum is not known to be Borel; (21) is an explicit Borel majorant with the same integral bound. Here \(\rho_D\) is the normalized Gaussian density with the determinant root continued from \(D_*\); in dimension zero the integral is evaluation.

*Proof.* Telescoping \(C+C\Gamma\Gamma^{\mathsf T}C\) gives
\(\|D-D_*\|\le c_\Delta\varepsilon\), while
\(K^{-1}I\le D_*\le B_KI\).
For \(u=Kc_\Delta\varepsilon\le1/2\), every singular value of
\(I+D_*^{-1/2}(D-D_*)D_*^{-1/2}\) is at least \(1-u\). Hence the determinant-root ratio is at most
\((1-u)^{-m/2}\le e^{um}\).
The inverse identity gives
\(\|D^{-1}-D_*^{-1}\|\le2K^2c_\Delta\varepsilon\).
Thus the single positive function
\[
 F_0e^{Kc_\Delta\varepsilon m}\rho_{D_*}(b)
       e^{(K^2c_\Delta\varepsilon+\rho)|b|^2}             \tag{21}
\]
dominates every integrand. It is Borel under H-S. With
\(q=K^2c_\Delta\varepsilon+\rho\le1/(4B_K)\), diagonalizing the real positive \(D_*\) gives
\(\int\rho_{D_*}e^{q|b|^2}\le e^{2B_Kqm}\), by
\(-\log(1-x)\le2x\) for \(0\le x\le1/2\).
This proves (20). Integrating Cauchy's formula against (21) proves holomorphy with fixed real cutoffs. ∎

This strengthens an estimate of the final Gaussian integral: it places the supremum **inside** the integral. The draft's Theorem 9.1 did not justify that move with its claimed quantitative cost.

Use ci-form's geometric constants \(P_d,c_m,c_f,C_h,c_\ell,C_v,C_D,\kappa_D,c_{\rm adj}\) and fixed type entropy \(S_\xi\), with its complete collar convention. Precisely, for a selected family \(\mathcal D\), failed bonds \(P_0\), and its coarse polymer \(Z\), put \(r=|\mathcal D|\), \(v=|P_0|\), \(h=|Z\setminus Z_0^\sharp|\), \(N=|Z|\). The geometric estimates required are ci-form (23)–(24):
\[
\begin{gathered}
 N\le C_h\{r+L^{-1}\textstyle\sum_{Y\in\mathcal D}{\rm St}(Y)+v+h\},\quad
 \sum_{Y:Y^\sharp\subset Z}e^{-\xi{\rm St}(Y)}
       \le c_fL^4S_\xi N,\\
 \ell_c(Z)=d_c(Z)+5\le c_\ell N,\quad
 |Z|\le C_v(d_c(Z)+1),\quad
 \ell_c(\cup_jZ_j)\le\sum_j\ell_c(Z_j)
 \quad\hbox{for an incompatible connected list}.
\end{gathered}                                                    \tag{22}
\]
Here \(d_c\) is the minimum coarse-graph tree edge count, with the same adjacency/collar convention. There are at most \(C_De^{\kappa_Dm}\) coarse polymers through a cube with \(m\le d_c<m+1\); incompatibility uses at most \(c_{\rm adj}N\) neighbouring cubes. These estimates follow by doubling covering trees, cutting their walks into pieces of length \(L\), and charging each piece's fixed collar to a bounded number of cubes. The degree-80 walk count with binary membership flags bounds the fine entropy. They apply to the actual carriers only when the stated collar convention has been supplied.

Choose \(g_*>\kappa_D+C_v\) so that
\[
 B_*=\frac{C_De^{2C_v-5g_*}}{1-e^{-(g_*-\kappa_D-C_v)}}\le c_{\rm adj}^{-1}.
\]
In ci-form (14), replace \(A\) by \(A^\#\):
\[
 W_0=\min\{[3P_dL^4(1+A^\#c_m)]^{-1},\rho_0/(2P_d)\},
 \qquad D_0=A^\#c_mL^4.                                  \tag{23}
\]
Set \(\mu=(1+4\beta_s)\kappa\), \(\Lambda=\mu+g_*\),
\(K_*=2+c_\ell\Lambda\), \(\Theta=C_h(1+K_*)\), and use the rate window
\(\lambda\ge\lambda_0+\sigma_0+\Theta/L\), \(\lambda_0,\sigma_0>\kappa_f\),
as well as D6. After \(M\), impose
\[
 \varepsilon\le\min(\varepsilon_0,(3D_0M^4)^{-1}),\quad
 \gamma_t=\min\{2/(3D_0M^4),\rho_0\},\quad
 p_*=c_b(LM)^4e^{-\gamma_t\mathfrak b^2/2}.
\]
The actual smallness follows from (3), first by \(M\), then by \(X_0\).
For total potential norm \(a\), put
\[
 A_a^\#=2c_fL^4S_{\sigma_0}/W_0,\quad
 a_*^\#=\min\{W_0/2,(4e^\Theta A_a^\#)^{-1}\},\quad
 t_*=e^\Theta(A_a^\#a+p_*)\le\tfrac12.                    \tag{24}
\]
Require \(a\le a_*^\#\), \(p_*\le(4e^\Theta)^{-1}\). These are late coupling ceilings.

**Lemma 10 (normal Mayer formation).** Assume H-G/H-S on every prescribed local fibre and coarse polydisc, (4) for every actual potential type uniformly there, (22) and the choices (23)–(24). Then ci-form (9)–(11) have representations of the form (2), including the Mayer logarithm. More precisely, each \(H(Z)\) has a representation whose summed integral majorant \(m_Z\) satisfies
\[
 m_Z\le t_*e^{-\Lambda\ell_c(Z)},\qquad
 e^{\mu\ell_c(X)}
 \sum_{n\ge1}\frac1{n!}\sum_{\cup Z_j=X}
       |\phi(Z_1,\ldots,Z_n)|\prod_jm_{Z_j}\le t_*B_* .   \tag{25}
\]
The majorants are uniform on the whole declared local domains, hence on every compact polydisc.

*Proof.* Keep real Gaussian coordinates, cutoffs and switch cubes fixed. For each selected potential introduce an auxiliary scalar coupling of radius
\(\mathcal R_Y=(W_0/a)e^{(\lambda-\lambda_0){\rm St}(Y)}\ge2\).
At each **fixed real \(b\)** the product \(\prod_Y(e^{z_YV_Y}-1)\) is entire in these couplings, vanishes on every coordinate zero, and is bounded on their polycircle by \(2^r\exp(\sum_Y|z_YV_Y|)\). Divide by \(\prod_Yz_Y\) and apply the maximum principle successively. At \(z_Y=1\) this yields the pointwise factor \(\prod_Y\mathcal R_Y^{-1}\), before any Gaussian integral or supremum. When \(a=0\), nonempty potential selections vanish.

For coarse first derivatives use Cauchy circles of the **fixed** radius
\(r_s=(e^{\bar\kappa}-1)/2\) about real switches; each costs \(r_s^{-1}\).
These circles lie strictly inside the given polydisc. All measures now are fixed positive measures: Lebesgue measure, unit switch-cube measure and normalized angular measures. Signs and complex kernels belong to the integrand.

The rooted density sums following from (22) give
\(\sum|z_YV_Y|\le P_dW_0L^4N+P_dW_0M^{-4}|b|^2\).
For distinct failed bonds,
\(\prod(1-\chi_b)\le e^{-\gamma_t\mathfrak b^2v/2}
e^{\gamma_t|b|^2/2}\).
Apply (21), with \(\rho=P_dW_0M^{-4}+\gamma_t/2\le\rho_0\).
Its total exponent per coarse cube is
\[
 P_dL^4W_0(1+A^\#c_m)+D_0M^4(\varepsilon+\gamma_t/2)\le1 .
\]
Consequently the **integral of an absolute majorant** for a selection is at most
\[
 e^N(2a/W_0)^r
 e^{-(\lambda-\lambda_0)\sum_Y{\rm St}(Y)}
 e^{-\gamma_t\mathfrak b^2v/2}r_s^{-h}.                  \tag{26}
\]
No supremum is moved through an integral.

Pay \(e^{(1+K_*)N}\) by (22), using \(\Theta\) for the \(r,v,h\) costs and the rate window for the length cost. The remaining positive selection sum is bounded by
\[
 e^{-K_*N}\!
 \left[\prod_{Y:Y^\sharp\subset Z}
   (1+(2a/W_0)e^\Theta e^{-\sigma_0{\rm St}(Y)})
 \prod_{b:b^\sharp\subset Z}(1+e^\Theta e^{-\gamma_t\mathfrak b^2/2})-1\right]
 \le e^{-K_*N}(e^{t_*N}-1)
 \le t_*e^{-\Lambda\ell_c(Z)} .
\]
This proves the first inequality in (25). Pointwise Schwarz retains ci-form's factor 2; the changes are the stronger density budget and fixed interior coarse Cauchy radius.

For the logarithm retain the finite alternating connected coefficient \(\phi\) as one scalar. Its absolute value is bounded by the number of spanning trees: order the incompatibility edges and toggle the least edge whose endpoints have a path of smaller edges. This pairs connected graphs with opposite signs; any unpaired connected graph is a tree. Set \(w_Z=e^{\mu\ell_c(Z)}m_Z\). Coarse entropy gives
\(\sup_q\sum_{Z\ni q}w_Ze^{|Z|}\le t_*B_*\), and hence
\(\sum_{Y\not\sim Z}w_Ye^{|Y|}\le|Z|/2\).
The rooted labelled-tree sums of height at most \(h\) obey
\(T_Z^{(0)}=1\),
\(T_Z^{(h+1)}=\exp(\sum_{Y\not\sim Z}w_YT_Y^{(h)})\).
Induction gives \(T_Z^{(h)}\le e^{|Z|}\); monotone convergence gives the full bound. Mark a polymer containing a fixed cube of \(X\); the \(1/n!\) becomes \(1/(n-1)!\). Use (22)'s union inequality and the rooted bound to obtain the second inequality in (25).

Expand each product of \(H\)'s using its fixed-measure representations. Products of their Borel majorants are integrable by Tonelli; (25) sums them. This is (2), without expanding \(\phi\) into absolute graph summands. Cauchy's formula passes under these majorants. Restrictions to smaller domains use the same estimates. ∎

**Theorem 4 (UM1-rest and conditional CI-form).** Assume D1–D6, H-G and (22)–(24)'s parameter choices, the complete FORM/FILE/H-S interfaces, HM for the gauge potential, and the hypotheses of Lemmas 4–5 and Theorems 2–3 for all the terms they cover. The smallness ceilings on \(a,p_*\) are imposed below. Supply any other actual non-gauge type with (4) and its own uniformly vanishing amplitude \(a_{\rm extra}\). Then
\[
 a_{\rm rest}=a_{\rm W3}+a_{\rm pr}+a_{\rm J}
              +a_{\rm lin+quad}+(\mathfrak b/R)N_C+2a_T
              +a_{\rm extra}\le W_0/4                  \tag{27}
\]
after the final coupling ceiling; \(a_{\rm lin+quad}=a_{\rm lin}+a_{\rm quad}\).
The choice \(a_{\rm extra}=0\) requires complete factor accounting, not a declaration that no extra type is wanted. With HMA's \(a_{\rm GF}\le W_0/4\), increase \(X_0\) further so that
\(a=a_{\rm GF}+a_{\rm rest}\le a_*^\#\) and (24) holds. Any insertion/free types are included in this sum.

On each whole local fibre the resulting regular gas has
\[
 |H(Z)|\le t_*e^{-\Lambda\ell_c(Z)},\qquad
 |E(X)|\le t_*B_*e^{-\mu\ell_c(X)},\qquad
 |\partial^\nu E(X)|\le\nu!\prod_jr_j^{-\nu_j}
                         t_*B_*e^{-\mu\ell_c(X)},       \tag{28}
\]
where the derivative bound is at the centre of any contained polydisc of radii \(r_j\).
It has all supplied real, gauge, tie, Borel, stored-slot and overlap identities, and the normal domination (2). Under H-I, the separate island amplitude obeys its bound in D4; H-O alone does not supply it.

*Proof.* Each term of (27) tends uniformly to zero by the cited lemmas and imports, after all its constants have been fixed. Their finite sum therefore meets both \(W_0/4\) and the stronger activity ceiling. HMA Lemma 3 supplies the same limit for the gauge term under HM; a fixed \(W_0/4\) bound alone would not suffice for the stronger ceiling. Lemma 10 proves (28), normal convergence and holomorphy; Cauchy's formula gives its derivative bound. Complete integrand identities from H-S pass through the convergent operations. Formal expansion of the finite compatible-polymer gas, grouped by connected components, gives its logarithm near zero activity. Replace every \(H\) by \(uH\); (25) continues this identity for \(|u|<1\), and domination at \(u=1\) gives
\(\mathcal Z_Q=\exp(\sum_{X\subset Q}E(X))\ne0\).
The island assertion is simply its separately supplied decomposition in D4. ∎

**Theorem 5 (conditional whole-domain CI induction).** Order the structures of a finite history. Assume Theorem 1 for its bare initial presentation; nl1-L Theorem 7's CI-maps and CI-Gauss, with MAP/OLD and all full-source, radius and domain margins; Theorem 4 for each main-step regular gas; H-I and the complete interface for each newly formed island; LF/H-E wherever stored variables are integrated; and STAGE/FILE and every remaining scalar, normalizer, companion and stage/output formation bound with (2). All inputs must be supplied on every prescribed local fibre, without using the bound then being proved. Then CI holds on the entire chain domain at every structure.

*Proof.* Induct in formation order. Earlier CI and the admitted maps give the old-factor interface. Theorem 4 gives the regular outputs; the other stipulated formation rules give the remaining outputs. Their Borel majorants permit integration and summation of Cauchy's formula on any compact polydisc. The supplied integrand identities pass through the same operations, and overlap agreement joins the fibres. Theorem 1 starts the induction. ∎

This is a sufficient theorem, not an “if and only if” description of CI. In particular, the FCON \(\to\) CI edge remains: its actual stage identity and common outer majorant are read before (2). No main-step radius \(R=\ell^q\) is assigned to a preparatory stage; nl1-L L619–627 retains its separate stage box and output BOX budgets.


## 8. Definitions supplied and source checks

The definitions supplied or made explicit here are:

1. D1–D2: whole local fibres, fixed Gaussian/Pauli coordinates and cutoff norms, bond ownership and distinct tree metrics; complete seed versus external-pair carrier; the centred substitution and switch domains.
2. D3–D5: the normal-integrand criterion, exact H-C/H-W/H-I and UM1-rest contracts, fixed-reference Gaussian datum, scoped import names, FORM and FILE.
3. D6 and Lemma 3: early versus late choices, the conversion \(c_X\), pointing/read multiplicity \(J_{\rm pt}\), and H-C\('\).
4. D7 and §3: scalar/profile/gauge/Jacobian splitting, normalized defects \(L,K_{\rm def}\), W-local, PROF-tube, JAC, HOL-K's regular norms and lattice distance, CENTRE and its covering/shrinking requirement.
5. D8 and §4: the pointed own-subtracted object, age convention and \(f_\nu\), and the linear localization/oscillation norm required by OSF-loc.
6. §§5–6: \(o_f,A_f,O_\omega\), TEST-v0, \(\rho_{\rm sep}\), complete presentation versus read sets, X°/G-ord, X/AGE, Boolean coefficients, rooted \(m_f\), and the TD rates and amplitudes.
7. §7: Gaussian density/branch and the Borel majorant (21); \(c_\Delta,A^\#,W_0,D_0,\rho_0,\varepsilon_0,\gamma_t\); tagged selections, coarse length/entropy conventions, \(B_*,\mu,\Lambda,K_*,\Theta,p_*,a_*^\#,t_*,m_Z\), the fixed Cauchy radius and the total non-gauge norm. Gas formulas and \(\phi\) remain exactly ci-form (9)–(11).

External source revision is \(31a47c543775\): [SA outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), complete account [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), [CA-II](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex), [CA-III](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_III.tex), and [YM3-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex). Credit for these texts is Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Each raw file was fetched once to /tmp; only bounded excerpts were read. The outline index, neighbouring rows and obligations, and the CA-I 4.12–4.19 index guided the checks. The table records the draft's direct source anchors and the added passages used here; it does not treat their conditional applications as proved.

| Checked source lines | Finding |
|---|---|
| SA 250–258, 2713–2723, 19651–19664 | The real Wilson convention and determinant identity agree with (5). Line 2719 writes the trace formula for real \(SU(2)\); it does not itself establish the draft's complex continuation. Theorem 1 does. |
| SA 5665–5694; 6191–6198; 6291–6314 | R4 includes more than curvature; relative trees meet excused hulls without filling them; R25's oscillation/admission requirements do not establish later chain-domain inclusion. |
| SA 17255–17290; 17457–17459 | The thresholds, labelled exponent and unlabelled E/R families are present; the core theorem is credited to Bałaban. Old regular terms are taken by later integrations, with analytic-space transport conditions. |
| SA 19540–19672, especially 19562–19568 and 19666–19670 | Own-coefficient pointed cancellation has the stated symmetry/response/moment hypotheses. OSF3–OSF4 **assume** the localized window estimates and membership; OSF6–OSF7 sum them. The renormalisation assertion is explicitly still required. |
| SA 13437–13534; 13728–13892; 17060–17074 | The response-ball/Taylor route and conditional own-subtracted age gain support CP12's formulation. OA16 sums an already supplied old amplitude; it does not establish (13). |
| SA 1223–1347; 14236–14249; 14293–14318; 14400–14412 | The tree cancellation/root recursion is present, with the Kotecký–Preiss attribution. The \(\tau\)-rescaling, UM1, fixed cutoffs and separate structural hypotheses agree with §7. The supremum-density bound (20) is proved here. |
| CA-I 49495–49548 | Operator conclusions leave application admission, actual background classes and drop-out choices as conditions. No whole-CI-domain supply is obtained. |
| CA-II 79920–80013; CA-III 98896–98937 | II displays Bałaban's exponent, stored/free split and conditional Gaussian, expressly without reproducing its derivation. III's sourced expansion assumes its format/cluster and vertex inputs. Neither proves FORM, H-W or HOL-K. |
| YM3-I 52582–52589; 31522–31536 | The first is an individual Gaussian-string hull construction, not nonlinear DR-row locality. The second is a relative quadratic gauge form, not a unique nonlinear extension. |

## Result

Theorem 1 proves CI-base for the specified bounded bare domains. The elementary localization, carrier conversion and density/Mayer arguments are hand proofs. Theorems 2–5 prove **conditional** H-C\('\), ordinary TD, UM1-rest with total norm at most \(W_0/4\), regular CI-form with nl1-L (18), and the precise whole-domain CI induction. They do not establish CI for the actual construction.

The imports are D5's MAP/OLD, DOM, DR, HM, GEO/RUN, LF, STAGE and FILE, with the additional W-local/PROF-tube/JAC, HOL-K/CENTRE, CP12 D6–D7/OSF-loc, TEST-v0, X/AGE and H-I premises at their stated places. Remaining actual obligations are the transfer lemma (13), normalized off-physical defects and critical-centred coverage, complete formation and every local-domain admission, the literal full-source separation, multilevel exempt/read sums, original island normalization and LF envelopes, filing/healing/history matches, and stage/output/normalizer/companion supply. Frozen PW now supplies its conditional operator estimate; it is not the missing OSF transfer.

Every substantive correction to the draft, including its proposed corrections to other texts, is recorded below. The named other files are unchanged.

| Draft claim or proposed correction | Disposition in this manuscript |
|---|---|
| CI-base is import-free; Lemmas 4.1–4.2 | Base bounds require the specified initial domain and coefficient. Both analytic lemmas are valid with their locality/domain hypotheses; centered constants improve, and stored sources still affect derivatives. |
| W decomposition and running bounds | Separate the entire profile difference once; restore HMA's \(\tau\) factor. Supply composed reads, weighted layer counts, PROF-tube and complex JAC branches. Retain \(c_5\) and the sufficient \(2e^{2q}\) running floor. |
| nl1-L Lemma 3; new HOL-K | The affine-read lemma is correct conditionally; the draft does not verify its premises for composed W terms. Lemma 4 replaces its potential estimate under different explicit premises. HOL-K needs actual normalized coefficients, CENTRE and covering; hma/dr do not prove it. Its failure does not prove an unbounded actual defect. |
| nl1-L L188; H-I from H-O | Reject the replacement \(B_f=O_\omega\) relative to the original scalar. H-O supplies complex differences and TD's deficit; the original amplitude/scalar normalization remains separate. |
| nl1-L L127 | The pointer is stale. Use ST1-r4 CV/GS and actual admission/uniqueness. Representative-independent analytic lemmas do not verify a changed branch's hypotheses. |
| IN1 row 1 | Correct to require the early power-count choice \(C\ge3\), hence \(q>3p_0\). This strengthens the chosen exponents; it is not an error in the conditional row. |
| ci-form H-C (5) | The smaller \(\kappa/(2\cdot4802)\) weight is sufficient under the complete-seed collar hypothesis, with early \(C_h^{\rm WF}\ge4802\) and actual pointing multiplicities. The printed stronger H-C is a hypothesis, not refuted. A nonsummable crude \(2b_f\) majorant does not refute an oscillation bound. |
| hma's Outstanding list | The draft read hma-draft. Frozen hma already retains PIV, stored-test/gauge-factor matching, whole-domain admission, physical branch and vacuum interfaces. Preserve them; add no fictitious closure from physical G-ID. Use the later frozen pw and explicitly unrefereed rows only in their scopes. |
| td X; X° and old projections | Whole-island length zero is a valid coarse convention; carrier lengths are a conditional refinement. H-O solves the complex-deficit issue under fixed-domain admission. Current X° requires the **whole** presentation collar; old member projection does not prove complete-read coverage. Use CLS's actual weakened gap, and retain multilevel AGE and all multiplicities. |
| nl1-L L494–502; draft Theorem 11.1 and H-FL | Retain the frozen full-source warning. Gas distance can vanish for a long exempt carrier; use the distance/length tradeoff (17). The stored-threshold bound requires TEST-v0's identical logarithmic datum and chart. |
| OSF-loc; dependence on items 1 and 9 | CP12 already proves conditional pointed cancellation and window gain. The missing step is the exact weighted switched-localization transfer (13), with actual CP12 D6–D7 supply. The needed item-9 input is member/response/companion matching, not the numerical one-loop value or all of SF. The H-O route also reads item 10. |
| Mayer domination and UM1-rest | Replace the unjustified integral-of-supremum inference by (21), pointwise Schwarz and fixed interior Cauchy circles. Enlarge the Gaussian comparison constant before \(\kappa\). Account for every actual type; zero free/extra norm requires FORM. The UM/CI conclusions are sufficient implications, not equivalences. |
| Formation, filing and claimed dependency closure | A definition and physical-pair agreement do not prove actual independent-current formation. Fluctuation locality is not whole external-pair filing. Retain the four CLS matches, weighted **formed-activity** filing, FCON's outer majorant and every stage/BOX budget. |

This text is **not yet refereed**, is research rather than an audit, and grants no scientific or audit status.
