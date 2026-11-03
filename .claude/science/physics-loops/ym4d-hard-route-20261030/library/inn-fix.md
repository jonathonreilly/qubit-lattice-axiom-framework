lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T08:02Z

# inn-fix: (Inn) under Definition R, repaired (queue row 182)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, pinned at `f7d7160ff`. Sussman–Alpoge outline at `31a47c543775`, fetched by URL into a private scratch folder (SHA-256 prefix `d7f77d4da3eb2303`, as before). Research text, not an audit; no status granted. **Proved by Claude, not yet checked by the other model.**

**Moves:** `library/sa-ledger.md` rank 6 (2.13), its (Inn) comparison under Definition R; `library/t0-skeleton.md` item 3. This repairs `library/inn-213.md` Section 7 along `gates/inn-check.md` Sections 4–5.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text: the operation, the pair domain and its core (SA 9646–9654), Theorems 5 and 6 of their Package A as cited below, the decomposition SA 18041–18100, the inner reads (SA 18152), the count \(N_0=N_0^\circ+\sum_yN_0(\omega'_y)\) (SA 18088) and the later-read estimate (SA 18188–18200). Codex: the truncation \(\bar P\), premise (M) and the margin lemma (1) (`inn-213.md` Section 2), `sa-2.13-2.md` Lemma 3.2, Theorem 6(c) as Lemma 10.1 of `a3-derivative.md` (with Claude), and the check `gates/inn-check.md`. Claude: Definition R, Proposition D, Theorem P, Lemmas A, E, T (`inn-213.md` 7, `pre-213.md`). T. Balaban: the background programme, the axial gauge and the estimate (190) of CMP 102 that `a3-derivative.md` proves as Theorem 4.

All library inputs read here have one line-by-line check by the other model, except where marked. No numeric job was run, and none was needed. Every step is a written argument.

## 0. Result

| Statement | Where | Verdict |
|---|---|---|
| Theorem I\(^R\)(a), the inner Wilson factor | Section 3 | proved as an implication. It uses the path \(e^{i\sigma v}\tilde{\mathbf D}\) and `pre-213.md` Lemma T's real slice, top by top. |
| Theorem I\(^R\)(b), the inner reads | Section 4 | proved as an implication. Every seminorm of (M) is bounded, the current included. The tower clauses follow from the outline's Theorem 5(c). \(\sum_yb_yN_y\le2C_VN_0(\omega)\). |
| Corollary P\(^R\), (Pre) under Definition R | Section 5 | proved as an implication. \(Q^R_{p_{\rm r}}\) is kept, and the joint chart is redone in the R representative. The U° form keeps \(Q^R_{p_{\rm r}}(B)-Q^\circ_{p_{\rm r}}(L_{\mathbf p}B)\) and bounds it. |
| Premise "\(m_{y,a}\ge g_k^{1/2}\)" of the old Theorem I | Section 4.1 | **WRONG as a premise.** No inner read satisfies it. It is replaced by the outline's own room. |
| Old Theorem I, Step 3 count of tops | Section 3, Step 5 | **gap, repaired.** The core's finer tops were counted as \(O(\ell^{4r+1})\) with no decay. T4's decay into the core pays for them. |

The repaired bound replaces (7.2) of `inn-213.md`. At the coupling ceiling, at every admitted pair \(\mathbf p\) and every \(\xi\) in the support,
\[
 |V^{\rm Inn}_X(\xi;\mathbf p)|\ \le\ \epsilon_W+\tfrac83\,C_V\,\bar a\sum_yN_0(\omega'_y)\ \le\ C'_{IW}\,g_k^{1/4}+\tfrac83\,C'_a\,g_k^{1/4}\,C_V\,N_0(\omega).
 \tag{7.2\(^R\)}
\]
Here \(C_V\) is the constant of the outline's bound \(|V|\le C_VN_0\) at the inner levels (the induction hypothesis), and \(C'_{IW},C'_a\) do not depend on \(C_V\). So (Inn) adds at most \(C'_{IW}g_k^{1/4}+\frac18C_VN_0(\omega)\) once \(\frac{64}3C'_ag_k^{1/4}\le1\), and the induction constant is not consumed.

**What this does not show.** It does not prove the named premises (Section 1): the domain room (M\(^R\)), which rests on the outline's Theorems 5(a), 5(c), 6(d) and its later-read estimate, cited and not rebuilt; the island placement (ISL); the induction hypothesis (IND); the orbit convention (GO). It does not treat (Act). It does not show that Definition R gives the same integral as the outline's operation (`gates/inn-check.md` Section 3).

## 1. Setting, notation and premises

Notation is that of `inn-213.md` Section 7 and `pre-213.md` Sections 2–3. Level-\(k\) units. \(x=x_k\), \(g=g_k=x^{-1/2}\), \(\ell=\log x\), \(\mathsf N=\mathsf N_k=\check R\ge\frac12\ell^r\), \(\check R\le L\ell^r\), \(r\ge2\). \(n_{\rm c}=\lfloor\mathsf N/2\rfloor\), \(n_{\rm m}=\lfloor\mathsf N/4\rfloor\), \(s'=k_\flat+n_{\rm c}+n_{\rm m}\), so \(\xi_{s'}\le L^{-\mathsf N/4}\). \(Z^\natural\) is the core \(C\) with the margin shells of levels \(k_\flat,\dots,k_\flat+n_{\rm c}-1\). \(W\), \(N_{\rm c}\), \(z_c\) and \(h\) are those of Definition R. \(E_\flat\) is the level-\(k_\flat\) shell. For a top \(t\) of \(\mathcal O^p\) in \(Z^\natural\) put
\[
 \lambda(t):=d_{\mathbf B}(t,E_\flat)\ \text{ if }t\subset C,\qquad \lambda(t):=0\ \text{ otherwise}.
\]
By step 1 of Lemma BC, \(\lambda(t)\ge c_g(k_\flat-j(t)-1)_+\) for a core top of level \(j(t)\) (`sa-2.8-terms.md` Lemma BC2).

Fix an admitted pair \(\mathbf p\), an admitted splitting with real part \(p_{\rm r}\), and \(\beta(\mathbf p)\), \(\|\beta(\mathbf p)\|_\infty\le\beta_A\) (Corollary P item 1). Put \(\mathbb D:=\{\|\beta\|_\infty<6\beta_A\}\) (complex) and \(\mathbb D^{\mathbb R}_5:=\{\beta\text{ real},\ \|\beta\|_\infty\le5\beta_A\}\).

**The \(\beta\)-family under Definition R.** For \(\beta\in\mathbb D\) form the six backgrounds of `pre-213.md` 2a at the exterior datum \(e^{i\beta}p_{\rm r}\). Let \(U^\circ(\beta):=S_\beta\) in the representative \(U^\circ\) (`ref-chart.md` 9b). Put \(h_\beta(x):=T_{U^\circ(\beta)}(z_c\to x)\) on \(N_{\rm c}\) and \(\mathbf 1\) elsewhere, \(S^R_\beta:=U^\circ(\beta)^{h_\beta}\), \(V^R_0(\beta):=(\mathcal M^jS^R_\beta)_j\). The R-prepared datum \(\mathbf D(\beta)\) carries \(\zeta\) on core rows, \(e^{igB}V^R_0(\beta)\) on shell rows, and the pair's data elsewhere. \(P(\xi;\beta)\) is its background. \(\tilde{\mathbf D}(\beta)\) equals \(\mathbf D(\beta)\) except that \(V^R_0(\beta)\) is replaced by \(\mathbf 1\) on the shell rows of levels \(\le s'\) in \(W\). \(\bar{\mathbf D}\) and \(\bar P(\xi)\) are those of `inn-213.md` 7c; they do not depend on the pair. At \(\beta=\beta(\mathbf p)\) these are the objects at the pair (`pre-213.md` 2a).

**The inner reads.** \(y\) runs over the inner islands \((m_y,Y_y)\) of \(\omega\). The read is \(q_y(U):=(U,J(U))|_{Y_y^\sim}\) (SA 18152). \(F_y(\cdot):=\Phi_{\omega'_y}(\xi'_y;\cdot)-\Phi^\circ_{\omega'_y}(\xi'_y)\) is the pair-dependent part of the island's exponent. Then, as in `inn-213.md` 7c,
\[
 V^{\rm Inn}_X(\xi;\mathbf p)=-A(w\psi,P(\xi;\beta(\mathbf p)))+A(w\psi,\bar P(\xi))+\sum_y\big[F_y(q_y(P(\xi;\beta(\mathbf p))))-F_y(q_y(\bar P(\xi)))\big].
\]
The stored forms and elimination factors are not inner reads. Their response belongs to (Act) (`gates/inn-check.md` Section 2).

**Premises.**
- **(I)** Those of the old Theorem I without its margin premise: Definition R, (ADM'), Corollary P with \(6\beta_A\), Lemma E's enlargement, I1 through Lemma MJ, I2 (P81 at full strength, radius \(r_{\rm B}\)), I3, I5 at the enlarged regularity, GEO3, GEO4, (SEP), (SEP-L) for \(\mathcal L_W\), (Adm-bar), the premises of Proposition D, \(0\le w\le2x\) on \(\operatorname{supp}\psi\), the frame bound \(\theta_m\le\theta_k+\bar B(k-m)\) for \(m\le k\) (SA (R19), 6020) and the tube \(|\theta_k-x_k|\le\frac12x_k\) (SA (R20), 6041). I3 is read as T4's first paragraph at a real critical reference on its **whole** polydisc, with the potential, gradient and current members (`a3-derivative.md` 6–7, (34), 7.3; gate ADVANCE). This is not T4 re-centred at a complex reference.
- **(ISL)** Every inner island has \(Y_y^\sim\subset Z^\natural\) and \(m_y\le k_\flat\). (SA 18523: the island's failed test is paid by the outer component's retained core action.)
- **(IND)** The outline's bound SA 18086 at the inner levels, which is the induction hypothesis. On every triple \((U,A',\mathbf J)\) of the core \(D_y:=\mathcal U^\circ_{m_y}(Y_y^\sim;\alpha_{0,m_y},\alpha_{1,m_y})\), \(\Phi_{\omega'_y}(\xi'_y;\cdot)=\Phi^\circ_{\omega'_y}-\frac12q_y(\xi'_y;U)+V_y\) with \(|V_y|\le C_VN_0(\omega'_y)\). The Gaussian \(q_y\) is formed at the real \(G\)-valued factor \(U\) (SA 17822, 18050). \(\Phi\) is holomorphic in the pair (SA 18059).
- **(GO)** \(F_y\) takes one value on the complex gauge orbit of a pair of \(D_y\), and a read is evaluated there (SA 9654, end of the paragraph *Complex fields*).
- **(M\(^R\))** Domain room. Put \(\bar U_y:=\bar P(\xi)|_{Y_y^\sim}\). The real triple \((\bar U_y,0,J(\bar U_y))\) lies in the core of level \(m_y\) at half radii \((\frac12\alpha_{0,m_y},\frac12\alpha_{1,m_y})\), and the outline's Theorem 5(c) holds at level \(m_y\): an outer substitution \(\mathbf U\mapsto e^{i\eta\mathbf A}\mathbf U\) with \(|\mathbf A|,|\nabla_{\mathbf U}\mathbf A|<c_{\rm T}\alpha_0\) in level-\(m_y\) units takes half radii to full radii (SA 9757; \(c_{\rm T}\sim1/K^\sharp\)). The outline supplies the first clause through its later-read estimate (SA 18188–18200), Theorem 6(d) (SA 9790) and Theorem 5(a) (SA 9746). These are cited, unchecked and not rebuilt.

Constants are fixed in the order of `pre-213.md` Section 5, then \(C_h,C_\Delta\) of Lemma H, then the constants of Sections 3–5. The coupling ceiling comes last.

## 2. The R datum on the polydisc

**Lemma H (proved by Claude, not yet checked).** Put \(C'_v:=\max(1,\sqrt2C_v)\), \(C_h:=3(C_w+C_a)C'_v\), \(C_\Delta:=\max(C_\natural,\,2C_h+4C_S)\), \(D_{N_{\rm c}}:=4C_nM(\check R+L^3)\xi_{s'}\), and
\[
 \delta^\sharp:=C^\sharp_D(\varepsilon_k+6\beta_A)\,L\xi_{s'}\big(4C_nM(\check R+L^3)+8L\big)\xi_{s'},
\]
with \(C^\sharp_D\) the constant \(C_D\) of (7.1) formed with \(6\beta_A\) in place of \(\beta_A\). Assume at the ceiling \(6C_\Delta\beta_A\le r_{\rm B}/4\), \(D_{N_{\rm c}}\le1\), \(6C_wC'_v\beta_A\le\frac18\), and Proposition D's radius condition at \(6\beta_A\). Then for every \(\beta\in\mathbb D\):

- (a) \(|h_\beta(x)h_0(x)^{-1}-\mathbf 1|\le C_h\|\beta\|_\infty\) for every \(x\in N_{\rm c}\).
- (b) Every row \(c\) with both ends in \(N_{\rm c}\) has \(|\log V^R_0(\beta)(c)|\le\delta^\sharp\).
- (c) The row-by-row left increment \(\Delta'(\beta):=\frac1i\log(\mathbf D(\beta)\tilde{\mathbf D}(0)^{-1})\) is \(0\) on core rows, at most \(8\delta^\sharp\) on shell rows with both ends in \(N_{\rm c}\), and at most \(C_\Delta\|\beta\|_\infty\) on every other row. The same holds for \(\frac1i\log(\mathbf D(\beta)\mathbf D(0)^{-1})\).
- (d) For real \(\beta\in\mathbb D^{\mathbb R}_5\), \(\mathbf D(\beta)\) and \(\tilde{\mathbf D}(\beta)\) are real and \(\varepsilon^R\)-regular, with \(\varepsilon^R:=\varepsilon_1+4C_M\delta^\sharp+6C_\Delta\beta_A\); and \(\mathbf D(\beta)=e^{iv(\beta)}\tilde{\mathbf D}(\beta)\), with \(v(\beta)\) supported on the shell rows of levels \(\le s'\) in \(W\) and \(\|v(\beta)\|_\infty\le\delta^\sharp\). (\(C_M\ge1\) is the Lipschitz constant of one average on its fixed chart.)

*Proof.* (a) GEO3 bounds the side of the nest box of the shells of levels \(\le s'+1\) by \(C_nM(\check RL^{k_\flat-s'-2}+L)\xi_{s'+2}\le C_nM(\check R+L^3)\xi_{s'}\). So \(|x-z_c|_1\le D_{N_{\rm c}}\) on \(N_{\rm c}\). In the box, \(U^\circ(\beta)(b)=u_B(b_-)e^{i\eta a(b)}U^\circ(0)(b)u_B(b_+)^{-1}\) with \(|a|\le C_aC'_v\|\beta\|_\infty\) and \(|u_B^{\pm1}-\mathbf 1|\le C_wC'_v\|\beta\|_\infty\) (`ref-chart.md` 9b, 9f, with \(B=(\beta,v(\beta))\)). Along the comb the gauge factors telescope:
\[
 h_\beta(x)=u_B(z_c)\,\Pi\,h_0(x)\,u_B(x)^{-1},\qquad \Pi:=\prod_ie^{i\eta\operatorname{Ad}(T_{i-1})a(b_i)},
\]
where \(T_{i-1}\) are the partial transports of the real \(U^\circ(0)\). Since \(|e^{i\eta Y}|\le e^{\eta|Y|}\), \(\|\Pi-\mathbf 1\|\le e^{D_{N_{\rm c}}C_aC'_v\|\beta\|}-1\le2C_aC'_v\|\beta\|\). Then \(h_\beta h_0^{-1}=u_B(z_c)\,\Pi\,\operatorname{Ad}(h_0(x))u_B(x)^{-1}\), and \(\operatorname{Ad}\) of the unitary \(h_0(x)\) keeps operator norms. The product of three factors near \(\mathbf 1\) gives (a).

(b) Proposition D holds at every \(\beta\in\mathbb D\) with \(6\beta_A\) for \(\beta_A\). Its curvature premise is `ref-chart.md` 9f, which at \(\|\beta\|_\infty<6\beta_A\) reads \(\|\partial S_\beta-\mathbf 1\|\le2(C(M)\varepsilon_k+120C_aC'_v\beta_A)\eta^2\le C'(M)(\varepsilon_k+6\beta_A)\eta^2\) with \(C'(M):=2\max(C(M),20C_aC'_v)\). Its transport premise \(|T_i^{\pm1}|\le3\) holds at the ceiling. A row of level \(j\le s'+1\) with both ends in \(N_{\rm c}\) has \(\xi_j\le L\xi_{s'}\) and \(|c_--z_c|_1\le D_{N_{\rm c}}\). Insert these into (7.1).

(c) Core rows carry \(\zeta\) in both data. On the shell rows of levels \(\le s'\) in \(W\), \(\tilde{\mathbf D}(0)=e^{igB}\), so \(\Delta'_c=\operatorname{Ad}(e^{igB})\log V^R_0(\beta)(c)\). \(\operatorname{Ad}\) of the real \(e^{igB}\) is an isometry, and (b) applies. On the other shell rows with both ends in \(N_{\rm c}\), \(\tilde{\mathbf D}(0)=\mathbf D(0)\), so \(\Delta'_c=\operatorname{Ad}(e^{igB})\log(V^R_0(\beta)V^R_0(0)^{-1})\). By (b) both factors lie within \(2\delta^\sharp\) of \(\mathbf 1\), and \(|\log X|\le2|X-\mathbf 1|\) gives \(8\delta^\sharp\). On a shell row with only \(c_-\) in \(N_{\rm c}\), covariance (R3) gives \(V^R_0(\beta)(c)=h_\beta(c_-)e^{i\delta_c(\beta)}\mathcal M^j(U^\circ(0))(c)\) with \(|\delta_c|\le C_S\|\beta\|_\infty\) (Proposition S\('\)). So \(V^R_0(\beta)V^R_0(0)^{-1}=[h_\beta h_0^{-1}](c_-)\cdot\operatorname{Ad}(h_0(c_-))e^{i\delta_c}\), and (a) bounds its logarithm by \(2(C_h+2C_S)\|\beta\|_\infty\). The mirror case is the same. On shell rows with no end in \(N_{\rm c}\), \(V^R_0=V_0\) and Proposition S\('\) applies. Box rows move by \(v(\beta)\) with \(|v|_\infty\le\sqrt2C_v\|\beta\|_\infty\) (Theorem C), and the pair's rows by \(\beta\). With \(\mathbf D(0)\) in place of \(\tilde{\mathbf D}(0)\) only the rows in \(W\) change, and the bound \(8\delta^\sharp\) covers them.

(d) For real \(\beta\), \(h_\beta\) is unitary (R1), so both data are real. *Shell tests.* \(e^{igB}V^R_0=(e^{igB'}V_0)^{h}\) with \(B'(c):=\operatorname{Ad}(h(c_-)^{-1})B(c)\), and \(|gB'|=|gB|<\delta'\). A test value is a closed holonomy, so a gauge conjugates it. These tests are therefore those of the U° prepared datum at \((B',e^{i\beta}p_{\rm r})\), which is \(\varepsilon^\sharp\)-regular by I5 with Lemma E. *Core tests* are unchanged. *Interface tests* read core rows and innermost shell rows. The last-shell test (SA 17598) bounds them by \(\frac12\varepsilon_{k_\flat}\) with the vacuum on the shell side. The factors \(e^{igB}\) and \(V^R_0=e^{iO(\delta^\sharp)}\) add at most \(4C_M(\delta'+\delta^\sharp)\); \(\varepsilon_1\) already contains \(4\delta'\). *Tests near \(\partial\Lambda^{\rm pr}\)* see \(h=\mathbf 1\) (R2). So \(\mathbf D(\beta)\) is \(\varepsilon^R\)-regular, because \(\varepsilon^\sharp\le\varepsilon_1+6C_\Delta\beta_A\). \(\tilde{\mathbf D}(\beta)\) equals \(\bar{\mathbf D}\) on \(W\), which is \(\varepsilon_1\)-regular by (Adm-bar), and equals \(\mathbf D(\beta)\) off \(W\). A test meeting both sides differs from the same test of \(\mathbf D(\beta)\) by left factors \(e^{-iv}\), so by at most \(4C_M\delta^\sharp\). Finally \(v(\beta):=\operatorname{Ad}(e^{igB})\log V^R_0(\beta)\) on the shell rows of levels \(\le s'\) in \(W\) gives \(\mathbf D=e^{iv}\tilde{\mathbf D}\), and (b) bounds it. \(\square\)

*Size.* \(\xi_{s'}^2\le L^{-\mathsf N/2}\), so \(\delta^\sharp\le C_\delta(\varepsilon_k+6\beta_A)(1+\check R)L^{-\mathsf N/2}\) with \(C_\delta:=C^\sharp_DL(4C_nM(1+L^3)+8L)\). Also \(\varepsilon^R\le Cg(1+\ell)^{\mathfrak p}\), \(\mathfrak p=\max(\mathfrak p_0+2r,q)\), as for \(\varepsilon^\sharp\) in `pre-213.md` (3.1).

**Lemma C (weighted count of the tops of \(Z^\natural\)).** For \(\theta'\ge\theta/4\),
\[
 \sum_{t\subset Z^\natural}e^{-\theta'\lambda(t)}\ \le\ T^\theta_\natural:=26L^4(C_nM\check R)^4\le C_T\,\ell^{4r},\qquad C_T:=26C_n^4M^4L^8 .
\]
*Proof.* Margin tops have \(\lambda=0\). GEO3 gives at most \((C_nM(\check RL^{k_\flat-j}+L))^4\) tops of level \(j\), so the \(n_{\rm c}\) margin levels hold at most \(8(C_nM)^4(2\check R^4+n_{\rm c}L^4)\le16L^4(C_nM\check R)^4\). The core has side \(\le C_nM\check R\xi_{k_\flat}\) (GEO3), so at most \((C_nM\check R)^4L^{4i}\) tops of level \(k_\flat-i\), each with \(\lambda\ge c_g(i-1)_+\). Since \(\theta c_g\ge64\log L\), \(\sum_{i\ge0}L^{4i}e^{-\theta c_g(i-1)_+/4}\le1+L^4\sum_{i\ge1}L^{-12(i-1)}\le2L^4\). Add, and use \(\check R\le L\ell^r\). \(\square\)

The old Step 3 summed a bound with no decay over all tops of \(Z^\natural\). The core can hold tops of every finer level (Lemma BC2), so that count is not \(O(\ell^{4r+1})\). Lemma C pays for them with the decay \(e^{-\theta'\lambda}\) that T4 supplies.

## 3. The inner Wilson factor

**Theorem I\(^R\)(a) (implication; proved by Claude, not yet checked).** Assume (I) and the ceiling of Lemma H. Put \(e^R:=8C_4C_{\rm BC'}(\theta/2)\,\delta^\sharp\). Then at every admitted pair \(\mathbf p\) and every \(\xi\) in the support,
\[
 \big|A(w\psi,P(\xi;\beta(\mathbf p)))-A(w\psi,\bar P(\xi))\big|\le\epsilon_W:=\sqrt{96C_{\rm SC}}\,C_9\,T^\theta_\natural\;x\varepsilon^R\Big[(2C_{\rm P}\varepsilon^Re^R)^{1/2}+\big((C_{\rm P}+C_\mu)C_\mu\big)^{1/2}\varepsilon^Re^{-\theta Mn_{\rm m}/2}\Big],
\]
and \(\epsilon_W\le C_{IW}(1+\ell)^{2\mathfrak p+5r}\big(L^{-\ell^r/8}+e^{-\theta M\ell^r/16}\big)\le C'_{IW}\,g_k^{1/4}\).

*Proof.* **Step 1 (real \(\beta\); the path \(e^{i\sigma v}\tilde{\mathbf D}\)).** Fix \(\beta\in\mathbb D^{\mathbb R}_5\). By Lemma H(d), \(\mathbf D(\beta)=e^{iv}\tilde{\mathbf D}(\beta)\) with \(\|v\|_\infty\le\delta^\sharp<r_{\rm B}\), and \(\tilde{\mathbf D}(\beta)\) is real and \(\varepsilon^R\)-regular. Let \(\tilde P(\beta)\) be its real critical background (P81). In P81's chart \(\Phi\) about \(\tilde{\mathbf D}(\beta)\), the coordinate of a datum is its left increment. So the datum path \(\sigma\mapsto e^{i\sigma v}\tilde{\mathbf D}(\beta)\), \(\sigma\in[0,1]\), is the chart segment \(\sigma\mapsto\sigma v\). Its end \(\Phi(v)\) is \(P(\xi;\beta)\), by uniqueness of the regular critical orbit. This is the path that `gates/inn-check.md` Section 4 gives; the old proof integrated along \(\tilde{\mathbf D}e^{i\sigma v}\), whose end is not \(\mathbf D\). T4 holds at every point of the polydisc (I3). Superpose its per-row responses along \(\sigma v\):
\[
 P(\xi;\beta)=(e^{i\eta a_1}\tilde P(\beta))^{u_1},\qquad
 \xi_t|a_1(t)|+\xi_t^2|\nabla a_1(t)|\le C_4\sum_{c\in\operatorname{supp}v}|v_c|e^{-\theta d_{\mathbf B}(t,y_c)}\le e^R\,e^{-\theta\lambda(t)/2}
\]
at every top \(t\). For the last step split \(e^{-\theta d}\le e^{-\theta d(t,\operatorname{supp}v)/2}e^{-\theta d(t,y_c)/2}\), use at most \(8\) rows per top and Lemma BC\('\) at rate \(\theta/2\), and use \(d_{\mathbf B}(t,\operatorname{supp}v)\ge\lambda(t)\). The last holds because every row of \(\operatorname{supp}v\) lies in a shell, and a path from a core top to a shell meets \(E_\flat\) first (Lemma BC2).

**Step 2 (real \(\beta\); localisation).** \(\tilde{\mathbf D}(\beta)\) and \(\bar{\mathbf D}\) coincide on \(W\), and \(\mathcal O^p\), \(\mathcal L_W(\mathcal O^p)\) coincide on \(W\) minus its collar ((SEP-L)). I1 through Lemma MJ, with Lemma E's enlargement, gives \(\tilde P(\beta)=(e^{i\eta f_1}P^\circ_W)^{w_1}\) and \(\bar P=(e^{i\eta f_2}P^\circ_W)^{w_2}\), with \(\xi_t|f_i|+\xi_t^2|\nabla f_i|\le C_\mu\varepsilon^Re^{-\theta d_{\mathbf B}(t,W^c)}\). For a top \(t\) of \(Z^\natural\), \(d_{\mathbf B}(t,W^c)\ge Mn_{\rm m}+\lambda(t)\): a path reaches \(E_\flat\), then crosses the \(n_{\rm m}\) shells of levels \(k_\flat+n_{\rm c},\dots,s'-1\), each at cost \(\ge M\) (GEO3).

**Step 3 (real \(\beta\); per top).** Group the plaquettes of \(\operatorname{supp}\psi\) by the tops \(t\) of the meet sequence. Inside \(W\), away from its collar, this is \(\mathcal O^p\). Put
\[
 f_t(\beta):=\sum_{p\text{ over }t}w(p)\psi(p)\big[a_p(P(\xi;\beta))-a_p(\bar P(\xi))\big].
\]
Lemma SC with Lemma E bounds the pair \((\tilde P(\beta),\bar P)\). Its one-pair local form bounds \((P(\xi;\beta),\tilde P(\beta))\), with amplitude \(e^Re^{-\theta\lambda(t)/2}\) from Step 1 and curvature \(a(t)\le C_{\rm P}\varepsilon^R\) of \(\tilde P(\beta)\) (I5). Its proof reads only the Landau form at \(t\). With \(\varpi=w\psi\le2x\) and \(e^R\le C_{\rm P}\varepsilon^R\) at the ceiling,
\[
 |f_t(\beta)|\le\epsilon_t:=2xC_{\rm SC}\Big[2C_{\rm P}\varepsilon^Re^R\,e^{-\theta\lambda(t)/2}+(C_{\rm P}+C_\mu)C_\mu(\varepsilon^R)^2e^{-\theta(Mn_{\rm m}+\lambda(t))}\Big].
\]

**Step 4 (complex pairs; Lemma T's real slice).** \(f_t\) is holomorphic on \(\mathbb D\). Indeed \(h_\beta\) is holomorphic (R1), the increments of \(\mathbf D(\beta)\) over \(\mathbf D(0)\) are below \(6C_\Delta\beta_A\le r_{\rm B}/4\) (Lemma H(c)), and P81's chart is holomorphic. By P81 (9.2) the complex local curvature of \(P(\xi;\beta)\) is at most \(C_9\varepsilon^R\) in the axial representative. For \(G\in{\rm SL}(2,\mathbb C)\), \(|a(G)|\le\frac12\|\mathbf 1-G\|^2\), and \(a_p\) is invariant under complex gauge. A top carries at most \(24(\xi_t/\eta)^4\) plaquettes, and \(\bar P\) is real with curvature \(\le C_{\rm P}\varepsilon_1\le C_9\varepsilon^R\). So \(|f_t|\le\mathsf B_t:=48x(C_9\varepsilon^R)^2\) on \(\mathbb D\). `pre-213.md` Lemma T now applies to \(f_t\). Its slice is \(\beta(z)=\beta_R+z\beta_I/\|\beta_I\|_\infty\), with \(\beta(\mathbf p)=\beta_R+i\beta_I\) row by row and \(\beta_R,\beta_I\) Hermitian. It is real for real \(z\) and reaches \(\beta(\mathbf p)\) at \(z=i\|\beta_I\|_\infty\). This replaces the old direction \(\hat\beta=\beta(\mathbf p)/s\), whose "real" segment \(e^{z\hat\beta}\) is not unitary. Lemma T gives \(|f_t(\beta(\mathbf p))|\le\sqrt{\mathsf B_t\epsilon_t}\).

**Step 5 (sum).** Sum \(\sqrt{\mathsf B_t\epsilon_t}\) over the tops of \(Z^\natural\), use \(\sqrt{u+u'}\le\sqrt u+\sqrt{u'}\), and apply Lemma C at rates \(\theta/4\) and \(\theta/2\). This gives \(\epsilon_W\). *Size.* \(x(\varepsilon^R)^2\le C(1+\ell)^{2\mathfrak p}\). Also \(\varepsilon_k+6\beta_A\le\varepsilon^R\), so the Size line of Lemma H gives \(e^R/\varepsilon^R\le8C_4C_{\rm BC'}C_\delta(1+\check R)L^{-\mathsf N/2}\). Hence \(x\varepsilon^R(\varepsilon^Re^R)^{1/2}=x(\varepsilon^R)^2(e^R/\varepsilon^R)^{1/2}\le C(1+\ell)^{2\mathfrak p+r/2}L^{-\mathsf N/4}\). With \(\mathsf N\ge\frac12\ell^r\), \(n_{\rm m}\ge\ell^r/8-1\) and \(T^\theta_\natural\le C_T\ell^{4r}\), the first bound follows. For the second, let \(\ell\ge2\). Since \(r\ge2\), \(L\ge5\) and \(\theta M\ge64\log L\), we have \(L^{-\ell^r/8}\le e^{-\ell/4}\) and \(e^{-\theta M\ell^r/16}\le e^{-\ell/4}\). As in the proof of Theorem P, \((1+\ell)^Ke^{-\ell/8}\le(8K)^K\). So \(\epsilon_W\le C'_{IW}e^{-\ell/8}=C'_{IW}g_k^{1/4}\). \(\square\)

T4 holds on the whole polydisc, so Lemma D\(^\sharp\) below also bounds the potential of \(P(\xi;\beta(\mathbf p))\) over \(\bar P\) at the complex pair. With the \({\rm SL}(2,\mathbb C)\) scalar step of Lemma SC (factor 3, `ref-chart.md` 9f), that gives the Wilson bound directly, without the square root. The route above uses only real per-top bounds and the crude complex bound, as the check asked.

## 4. The inner reads

### 4.1 The old margin premise holds for no inner read

The old Theorem I assumed (M) at \(q_y(\bar P(\xi))\) with margins \(m_{y,a}\ge g_k^{1/2}\). A margin is room inside the domain. So the margin of a curvature or current clause is at most the radius of that clause. In the units of the domain, level \(m=m_y\), that radius is \(\alpha_{0,m}=C_0\theta_m^{-1/2}(\log\theta_m)^q\) (SA 6033; the core, SA 9646–9654). The map \(\theta\mapsto\theta^{-1/2}(\log\theta)^q\) decreases for \(\theta\ge e^{2q}\). (R19) gives \(\theta_m\ge\theta_k-c_5\), and (R20) gives \(\theta_k\ge\frac12x\). So \(\alpha_{0,m}\le2C_0g_k\ell^q\) at the ceiling, and this is below \(g_k^{1/2}\) once \(2C_0\ell^qe^{-\ell/4}<1\). The premise therefore fails for every island, and Step 5 of the old proof had no admissible input. Section 4.2 uses the outline's own room, of size \(c_{\rm T}\alpha_{0,m}\). Section 4.4 shows that the displacement is smaller than that room by a factor that beats every power of \(g_k\).

### 4.2 The chart for (M), with the real part fixed

Fix \(y\), \(m:=m_y\), \(\bar U:=\bar U_y\), \(\bar J:=J(\bar U)\). The chart sends \(h=(\mathbf A,\mathbf j)\) to the triple \((\bar U,\mathbf A,\bar J+\mathbf j)\), that is, to the pair \((e^{i\eta\mathbf A}\bar U,\bar J+\mathbf j)\). Here \(\mathbf A\) is a complex Lie-algebra-valued 1-form on the bonds of \(Y_y^\sim\), and \(\mathbf j\) is a complex independent current. The seminorms are taken in level-\(m\) units:
\[
 \|h\|_1:=\sup\xi_m|\mathbf A|,\quad \|h\|_2:=\sup\xi_m^2|\nabla_{\bar U}\mathbf A|,\quad \|h\|_3:=\sup\xi_m^3|\mathbf j|,\qquad m_1=m_2:=c_{\rm T}\alpha_{0,m},\quad m_3:=\tfrac12\alpha_{0,m},
\]
and \(\|h\|_{*,y}:=\max_a\|h\|_a/m_a\).

**(M) holds at \(\bar p_y=(\bar U,0,\bar J)\).** By (M\(^R\)) the real triple lies in the core at half radii. A point of the ball \(\{\|h\|_{*,y}<1\}\) has \(|\mathbf A|,|\nabla_{\bar U}\mathbf A|<c_{\rm T}\alpha_{0,m}\). Theorem 5(c), the outer substitution, then puts \((\bar U,\mathbf A,\cdot)\) in the core at full radii, **every tower clause included**. The current clause holds because \(|\bar J+\mathbf j|<\frac12\alpha_{0,m}+\frac12\alpha_{0,m}\); no tower clause reads the independent current. The real part is \(\bar U\) at every point of the ball. So the clauses on \(U\) alone (its curvature, its local real gauges, its tower configurations) are those of the real read. **This is how the towers enter:** they are functions of \(\mathbf A\), and Theorem 5(c) controls all of them nonlinearly on the whole ball. The only displacement bounds the towers need are the bounds on \(\|h\|_1\) and \(\|h\|_2\).

**The margin lemma with the real part fixed.** On the ball, (IND) gives \(F_y(\bar U,\mathbf A,\bar J+\mathbf j)=-\frac12q_y(\xi'_y;\bar U)+V_y(\bar U,\mathbf A,\bar J+\mathbf j)\). The Gaussian is formed at the \(G\)-valued factor, and that factor is \(\bar U\) at every point. So \(q_y\) cancels exactly:
\[
 f_y(h):=F_y(\bar p_y+h)-F_y(\bar p_y)=V_y(\bar U,\mathbf A,\bar J+\mathbf j)-V_y(\bar U,0,\bar J).
\]
\(f_y\) is holomorphic on the ball, because \(\Phi\) is holomorphic in the pair and the pair is holomorphic in \(h\). Also \(|f_y|\le2C_VN_0(\omega'_y)\). Lemma (1) of `inn-213.md` Section 2 then gives, for \(\|h\|_{*,y}\le a<1\),
\[
 |F_y(\bar p_y+h)-F_y(\bar p_y)|\le2C_V\,N_0(\omega'_y)\,\frac a{1-a}.
 \tag{4.1}
\]
In the old notation, \(b_y=2C_V\) and \(N_y=N_0(\omega'_y)\).

*Why the real part is fixed.* At a read with another real part \(U\), the Gaussian \(q_y(\xi'_y;U)\) moves with \(U\). It is not bounded by \(CN_0(\omega'_y)\) uniformly in depth: it carries \((A_1p_1(g_{m}))^2\), which grows with \(\log x_m\). With the real part fixed, it drops out of every difference.

### 4.3 Lemma K (composition of Landau forms)

**Lemma K (proved by Claude, not yet checked).** Let \(U_0\) be real, \(f_1,f_2\) real 1-forms, \(w_1,w_2\) real gauges, \(\tilde P:=(e^{i\eta f_1}U_0)^{w_1}\), \(\bar P:=(e^{i\eta f_2}U_0)^{w_2}\), and \(a\) a complex 1-form. Define \(\mathbf A\) bond by bond by
\[
 e^{i\eta\mathbf A(b)}:=e^{i\eta\operatorname{Ad}(w_2w_1^{-1}(b_-))a(b)}\,e^{i\eta\operatorname{Ad}(w_2(b_-))\varphi(b)},\qquad e^{i\eta\varphi}:=e^{i\eta f_1}e^{-i\eta f_2}.
\]
Then:
- (i) \((e^{i\eta a}\tilde P)^{w_2w_1^{-1}}=e^{i\eta\mathbf A}\bar P\).
- (ii) \(J(e^{i\eta\mathbf A}\bar P)-J(\bar P)=\operatorname{Ad}(w_2w_1^{-1})\big[J(e^{i\eta a}\tilde P)-J(\tilde P)\big]+\operatorname{Ad}(w_2)\big[J(e^{i\eta f_1}U_0)-J(U_0)\big]-\operatorname{Ad}(w_2)\big[J(e^{i\eta f_2}U_0)-J(U_0)\big]\).
- (iii) There is an absolute \(c_K\) with this property. If at a top \(t\), on the bonds over \(t\) and their neighbours, \(\epsilon_a:=\xi_t|a|+\xi_t^2|\nabla_{\tilde P}a|\) and \(\epsilon_f:=\max_i(\xi_t|f_i|+\xi_t^2|\nabla_{U_0}f_i|)\) satisfy \(\epsilon_a+2\epsilon_f\le1/c_K\), then \(\xi_t|\mathbf A|+\xi_t^2|\nabla_{\bar P}\mathbf A|\le2(\epsilon_a+2\epsilon_f)\) there.

*Proof.* (i) On a bond \(b\), the left side is \(w_2(b_-)\,e^{i\eta\operatorname{Ad}(w_1(b_-)^{-1})a(b)}e^{i\eta f_1(b)}U_0(b)\,w_2(b_+)^{-1}\), and \(\bar P(b)=w_2(b_-)e^{i\eta f_2(b)}U_0(b)w_2(b_+)^{-1}\). Their quotient is \(e^{i\eta\mathbf A(b)}\). (ii) The current is the left-variation gradient of the gauge-invariant action, so \(J(V^G)(b)=\operatorname{Ad}(G(b_-))J(V)(b)\) for real \(G\), and by continuation for complex \(G\). Apply this to (i) and to the definitions of \(\tilde P\) and \(\bar P\). Then add and subtract \(\operatorname{Ad}(w_2w_1^{-1})J(\tilde P)=\operatorname{Ad}(w_2)J(e^{i\eta f_1}U_0)\). (iii) For \(|X|+|Y|\le\frac14\), \(R(X,Y):=\operatorname{BCH}(X,Y)-X-Y\) obeys \(|R|\le3(|X|+|Y|)^2\), and its Lipschitz constant on that ball is at most \(c(|X|+|Y|)\) with \(c\) absolute. Here \(X,Y\) are \(\eta\) times local quantities, so in local units each remainder costs at most \(c(\eta/\xi_t)(\epsilon_a+2\epsilon_f)^2\). For the derivative use covariance, \(\nabla_{V^g}(\operatorname{Ad}(g)Z)=\operatorname{Ad}(g)\nabla_VZ\). It turns \(\nabla_{\bar P}\) into \(\nabla_{e^{i\eta f_2}U_0}\) and \(\nabla_{\tilde P}\) into \(\nabla_{e^{i\eta f_1}U_0}\). A base change \(V\mapsto e^{i\eta\psi}V\) with real \(\psi\) moves \(\nabla_VZ\) by at most \(2|\psi||Z|\), since \(|\operatorname{Ad}(e^{i\eta\psi})-1|\le2\eta|\psi|\); in local units that is \(2(\xi|\psi|)(\xi|Z|)\). The base changes used have \(\xi|\psi|\le2\epsilon_f(1+o(1))\). Collecting, \(\xi_t|\mathbf A|+\xi_t^2|\nabla_{\bar P}\mathbf A|\le\epsilon_a+2\epsilon_f+c'_K(\epsilon_a+2\epsilon_f)^2\), and \(c_K:=\max(10,c'_K)\) gives (iii). \(\square\)

### 4.4 Lemma D\(^\sharp\): the displacement of every read, in every seminorm

**Lemma D\(^\sharp\) (proved by Claude, not yet checked).** Assume (I), (ISL) and the ceiling of Lemma H. Put \(C_\flat:=\max(C_4,C_{\delta J})\) and
\[
 \vartheta^0:=3\Big[8C_\flat C_{\rm BC'}(\theta/2)\big(8\delta^\sharp+6C_\Delta\beta_Ae^{-\theta M(n_{\rm m}+1)/2}\big)+2C_\mu\varepsilon^Re^{-\theta Mn_{\rm m}}\Big],
\]
and assume \(\vartheta^0\le3/c_K\). Then for every \(\beta\in\mathbb D\) and every inner island \(y\) there are a complex 1-form \(\mathbf A\) on \(Y_y^\sim\) and a complex gauge \(G\) with \(P(\xi;\beta)=(e^{i\eta\mathbf A}\bar P)^G\) there. At every top \(t\) of \(\mathcal O^p\) carrying a bond of \(Y_y^\sim\),
\[
 \xi_t|\mathbf A|+\xi_t^2|\nabla_{\bar P}\mathbf A|+\xi_t^3\big|J(e^{i\eta\mathbf A}\bar P)-J(\bar P)\big|\ \le\ \vartheta^0e^{-\theta\lambda(t)/2}.
\]

*Proof.* **(1) The chart about \(\tilde P_0\).** Let \(\tilde P_0\) be the real critical background of \(\tilde{\mathbf D}(0)\) (Lemma H(d) at \(\beta=0\)). By Lemma H(c), \(\mathbf D(\beta)=e^{i\Delta'(\beta)}\tilde{\mathbf D}(0)\) with \(\|\Delta'(\beta)\|_\infty\le\max(8\delta^\sharp,6C_\Delta\beta_A)<r_{\rm B}\). So \(P(\xi;\beta)=\Phi(\Delta'(\beta))=(e^{i\eta a}\tilde P_0)^u\) in P81's chart about \(\tilde{\mathbf D}(0)\). T4's first paragraph holds at every point \(s\Delta'\), \(s\in[0,1]\), of the polydisc. Integrating its responses over \(s\) gives
\[
 \xi_t|a|+\xi_t^2|\nabla_{\tilde P_0}a|\le C_4\sum_c|\Delta'_c|e^{-\theta d_{\mathbf B}(t,y_c)},\qquad \xi_t^3|J(e^{i\eta a}\tilde P_0)-J(\tilde P_0)|\le C_{\delta J}\sum_c|\Delta'_c|e^{-\theta d_{\mathbf B}(t,y_c)}
\]
(`a3-derivative.md` (34) and 7.3). Split the rows. Rows with both ends in \(N_{\rm c}\) have \(|\Delta'_c|\le8\delta^\sharp\); they are shell rows (\(\Delta'=0\) on core rows), so \(d_{\mathbf B}(t,y_c)\ge\lambda(t)\). The other rows have \(|\Delta'_c|\le6C_\Delta\beta_A\) and \(d_{\mathbf B}(t,y_c)\ge M(n_{\rm m}+1)+\lambda(t)\). The last holds because \(Y^\sim_y\subset Z^\natural\) (ISL): such a row lies in a shell of level \(\ge s'+1\), or beyond, and a path to it crosses the \(n_{\rm m}+1\) shells of levels \(k_\flat+n_{\rm c},\dots,s'\) at cost \(\ge M\) each (GEO3). Lemma BC\('\) at rate \(\theta/2\), with at most 8 rows per top, gives \(\epsilon_{a,t}\le8C_\flat C_{\rm BC'}(\theta/2)(8\delta^\sharp+6C_\Delta\beta_Ae^{-\theta M(n_{\rm m}+1)/2})e^{-\theta\lambda(t)/2}\), and the same bound for the current.

**(2) Localisation at \(\beta=0\).** As in Step 2 of Section 3, \(\tilde P_0=(e^{i\eta f_1}P^\circ_W)^{w_1}\) and \(\bar P=(e^{i\eta f_2}P^\circ_W)^{w_2}\), with potential and gradient members \(\le C_\mu\varepsilon^Re^{-\theta d_{\mathbf B}(t,W^c)}\) (Lemma 10.1 of `a3-derivative.md`). *Current member (one line, proved here).* Lemma 10.1 writes \(f=\int_0^1D\mathcal H(sB_0)[B_0]\,ds\) and bounds each linear response in the weighted norm with \(w(y)=e^{\theta d_{\mathbf B}(y,W^c)}\). The derivation of 7.3 bounds the current of a linear response at a bond by the weighted norms of \((h,\dot\omega)\) at nearby rows; weights move by at most \(e^{\theta D_L}\) between neighbours, as in 7.5. So \(\xi_t^3|J(e^{i\eta f_i}P^\circ_W)-J(P^\circ_W)|\le C_\mu\varepsilon^Re^{-\theta d_{\mathbf B}(t,W^c)}\), after \(C_\mu\) is enlarged by a fixed factor. Also \(d_{\mathbf B}(t,W^c)\ge Mn_{\rm m}+\lambda(t)\).

**(3) Compose.** Apply Lemma K with \(U_0=P^\circ_W\), \(\tilde P=\tilde P_0\), and \(a,f_1,f_2\) as above. It gives \(e^{i\eta\mathbf A}\bar P=(e^{i\eta a}\tilde P_0)^{w_2w_1^{-1}}\), hence \(P(\xi;\beta)=(e^{i\eta\mathbf A}\bar P)^G\) with \(G:=u\,w_1w_2^{-1}\). Lemma K(iii) bounds the potential and gradient by \(2(\epsilon_{a,t}+2\epsilon_{f,t})\). Lemma K(ii), with the isometries \(\operatorname{Ad}\) of real gauges, bounds the current by \(\epsilon^J_{a,t}+2\epsilon^J_{f,t}\). The sum is at most \(\vartheta^0e^{-\theta\lambda(t)/2}\). \(\square\)

This lemma reads T4 at complex points of the polydisc about the real \(\tilde P_0\), with its current member. That is T4's first paragraph (gate ADVANCE, `gates/a3-derivative-gate.md` Sections 6–7). The complex gauge \(u\) of the chart is never bounded: the read is taken in the representative \(e^{i\eta\mathbf A}\bar P\), which is a real gauge transform of the Landau form \(e^{i\eta a}\tilde P_0\). This respects the gate's limit on 7.6.

### 4.5 Theorem I\(^R\)(b)

**Theorem I\(^R\)(b) (implication; proved by Claude, not yet checked).** Assume (I), (ISL), (IND), (GO), (M\(^R\)), the ceiling of Lemma H and of Lemma D\(^\sharp\), and \(\bar a\le\frac14\), where
\[
 \bar a:=\frac{2L^3C_B}{c'C_0}\cdot\frac{\vartheta^0}{g_k},\qquad c':=\min(c_{\rm T},\tfrac12),\qquad C_B:=\sup_{d\ge0}(1+\bar Bd)^{1/2}L^{-(d-1)_+}.
\]
Then at every admitted pair \(\mathbf p\) and every \(\xi\) in the support,
\[
 \Big|\sum_y\big[F_y(q_y(P(\xi;\beta(\mathbf p))))-F_y(q_y(\bar P(\xi)))\big]\Big|\le\tfrac83\,C_V\,\bar a\sum_yN_0(\omega'_y)\le\tfrac83\,C_V\,\bar a\,N_0(\omega).
\]
Moreover \(\bar a\le C_a(1+\ell)^{\mathfrak p+r}\big(L^{-\ell^r/4}+e^{-\theta M\ell^r/16}\big)\le C'_a\,g_k^{1/4}\).

*Proof.* Fix \(y\), \(m:=m_y\le k_\flat\) and \(d:=k_\flat-m\ge0\).

(a) *The read in the chart.* By Lemma D\(^\sharp\) at \(\beta=\beta(\mathbf p)\), and the covariance of \(J\), the pair \(q_y(P(\xi;\beta(\mathbf p)))\) is the \(G\)-transform of \((e^{i\eta\mathbf A}\bar U,J(e^{i\eta\mathbf A}\bar U))\) on \(Y_y^\sim\). By (GO), \(F_y\) takes one value at both. So the actual read is the chart point \(h_y:=(\mathbf A,J(e^{i\eta\mathbf A}\bar U)-\bar J)\) of 4.2, and the real read is \(h=0\).

(b) *Units.* A bond of \(Y_y^\sim\) over the top \(t\) of level \(j=j(t)\) has \(\xi_m^s|\cdot|=(\xi_m/\xi_t)^s\,\xi_t^s|\cdot|\), with \(s=1,2,3\) for the potential, derivative and current. Lemma D\(^\sharp\) bounds the local quantities by \(\vartheta^0e^{-\theta\lambda(t)/2}\). We claim \((\xi_m/\xi_t)^se^{-\theta\lambda(t)/2}\le L^3L^{-(d-1)_+}\). Use \(e^{-\theta c_g/2}\le L^{-32}\).
- \(t\subset C\), \(j\ge m\): the factor is at most \(L^{-(j-m)}L^{-(k_\flat-j-1)_+}\), and \((j-m)+(k_\flat-j-1)_+\ge d-1\).
- \(t\) a margin top: \(j\ge k_\flat\), so the factor is at most \(L^{-d}\).
- \(t\subset C\), \(j<m\): the factor is at most \(L^{3(m-j)}L^{-32(k_\flat-j-1)}\). Since \(k_\flat-j-1\ge(m-j-1)+d\), this is at most \(L^{32-29(m-j)-32d}\le L^3L^{-32d}\).

So \(\|h_y\|_a\le L^3L^{-(d-1)_+}\vartheta^0\) for \(a=1,2,3\).

(c) *Margins.* (R19) gives \(\theta_m\le\theta_k+\bar B(k-m)\) with \(k-m=\mathsf N+d\). (R20) gives \(\frac12x\le\theta_k\le\frac32x\). At the ceiling \(2\bar B\mathsf N\le x\) and \(\log\theta_m\ge1\). So \(\alpha_{0,m}\ge C_0\theta_m^{-1/2}\ge\frac12C_0g_k(1+\bar Bd)^{-1/2}\). Hence
\[
 a_y:=\|h_y\|_{*,y}\le\frac{L^3L^{-(d-1)_+}\vartheta^0}{c'\alpha_{0,m}}\le\frac{2L^3}{c'C_0}(1+\bar Bd)^{1/2}L^{-(d-1)_+}\,\frac{\vartheta^0}{g_k}\le\bar a\le\tfrac14 .
\]
The deep islands (\(d\) large) are paid by the decay through the layers between their level and the shells; their smaller radius costs only \((1+\bar Bd)^{1/2}\).

(d) *Sum.* (4.1) with \(a=a_y\le\bar a\le\frac14\) gives \(|F_y(\bar p_y+h_y)-F_y(\bar p_y)|\le\frac83C_V\bar aN_0(\omega'_y)\). Sum over \(y\), and use \(N_0(\omega)=N_0^\circ(\omega)+\sum_yN_0(\omega'_y)\) (SA 18091). In the old notation this is \(\sum_yb_yN_y=2C_V\sum_yN_0(\omega'_y)\le2C_VN_0(\omega)\).

(e) *Size.* By the Size line of Lemma H, \(\delta^\sharp/g\le C_\delta(p_0(g)+6\beta_A/g)(1+\check R)L^{-\mathsf N/2}\le C(1+\ell)^{\mathfrak p+r}L^{-\mathsf N/2}\). Also \(\beta_A/g\le C(1+\ell)^q\) and \(\varepsilon^R/g\le C(1+\ell)^{\mathfrak p}\). With \(\mathsf N\ge\frac12\ell^r\) and \(n_{\rm m}\ge\ell^r/8-1\) this gives the bound on \(\bar a\). The last inequality is that of Section 3. \(\square\)

**(7.2\(^R\)).** Theorem I\(^R\)(a) and (b) together give (7.2\(^R\)) of Section 0.

## 5. Corollary P\(^R\), repaired

The failure (`gates/inn-check.md` Section 5): the old proof composed every term with U° at \(B'=L_{\mathbf p}B\). The quadratic form is frozen at the real splitting, so covariance gives \(Q^R_{p_{\rm r}}(B)=Q^\circ_{p_{\rm r}}(L_{p_{\rm r}}B)\), not \(Q^\circ_{p_{\rm r}}(L_{\mathbf p}B)\). The repair below stays in the R representative. It keeps \(Q^R_{p_{\rm r}}\) and redoes the joint chart there. The U° form follows at the end, with the difference kept and bounded.

**Corollary P\(^R\) (implication; proved by Claude, not yet checked).** Assume the hypotheses of Theorem P, Definition R, and the ceiling of Lemma H, with \(C_\Delta\) for \(C_\natural\) and \(\varepsilon^R\) for \(\varepsilon^\sharp\) in every ceiling condition of `pre-213.md` Sections 3 and 4c. Let \(V^{{\rm Pre},R}_X(\mathbf p)\) be (2.1) formed with the R backgrounds (\(P,P_X\) and \(T(B)\), the ones that read \(V_0\) or the reference rows of \(T(B)\)) and with
\[
 Q^R_{p_{\rm r}}(B):=\tfrac12\sum_p\phi(p)\,\big|(d_{S^R_0}\eta\mathsf H^RB)_p\big|^2,
\]
the real full mixed form of the splitting in the R representative. Then at every admitted pair, on every admitted splitting, \(V^{{\rm Pre},R}_X(\mathbf p)\) obeys (5.1) of `pre-213.md` with \(\varepsilon^R\) for \(\varepsilon^\sharp\). In particular \(|V^{{\rm Pre},R}_X(\mathbf p)|\le C'^R_{\rm Pre}\,g_k^{1/4}\).

*Proof.* Theorem P's proof reads three things for each term of (2.2). Each holds in the R representative.

(i) *Holomorphy and the crude bound (Lemma A\(^R\)).* The datum increments of the R backgrounds over their real data at \(\beta=0\) are at most \(C_\Delta\|\beta\|_\infty\) on \(\mathbb D\). For the shell rows this is Lemma H(c). The reference rows of \(\tilde T^R\) carry \(\mathcal M(S^R_\beta)\). On rows with both ends in \(N_{\rm c}\), the core rows included, they move by at most \(8\delta^\sharp\): Lemma H(b) holds for every averaged row with both ends in \(N_{\rm c}\), because the proof of Proposition D does not use that the row is a shell row. Elsewhere \(h=\mathbf 1\), and they move as in U°. So the R backgrounds are holomorphic on \(\mathbb D\), and (3.2) holds with \(\varepsilon^R\).

(ii) *Real per-top bounds at real \(\beta\in\mathbb D^{\mathbb R}_5\).* The R data are real and \(\varepsilon^R\)-regular (Lemma H(d)). For the reference data of \(\tilde T^R\) every row is \(h\)-transformed, so their tests are conjugates of the U° tests. The meet coincidences W1–W4 of `sa-2.8-terms.md` Section 3 hold. R changes only rows in \(N_{\rm c}\subset\Lambda\), and it changes them the same way in both members of W1 (\(P^R\) and \(P^R_X\) both carry \(e^{igB}V^R_0\)) and of W3 (\(T^R(B)\) and \(P^R_X\) share \(\mathbf D_{pX}\) and all data off \(C\)). W2 reads only the reference, and W4 compares outside \(\Lambda\), where \(h=\mathbf 1\). EXT holds for the same reason. Lemma LM holds for \(S^R=S^h\): \(\nabla A(S^h)\) is the gauge transform of \(\nabla A(S)\), the exterior rows see \(h=\mathbf 1\), and \(\tilde T^R_\beta(0)=S^R_\beta\) modulo residual gauge. So Lemma E's per-top estimates hold, and 4a–4b bound \(R_1,R_3,R_5,R_6,R_7,R_{10}\) with \(\varepsilon^R\).

(iii) *The block \(Y^R:=Q^R_{p_{\rm r}}(B)-x\{A(\phi,T^R_\beta(B))-A(\phi,S_\beta)\}\).* The R joint chart \((\beta,u)\mapsto\tilde T^R_\beta(u)\), with shells \(e^{iu}V^R_0(\beta)\) and reference rows \(\mathcal M(S^R_\beta)\), has the room of 4c. For \(\|\beta\|_\infty<\rho^R_Q:=\min\{\rho_\beta/2,\ r_{\rm B}/(16C_\Delta),\ \rho_{S'}\}\) and \(\|u\|_\infty<r_{\rm B}/16\), every increment is below \(r_{\rm B}/2\) by (i). So (4.2), (4.3) and the exact Taylor split hold verbatim. \(Y^R_5=0\) by Lemma LM item 2 in R and the identity theorem. For \(Y^R_2\), covariance at the real \(h_0\) gives \(\tilde F^R_0(u)=\tilde F^\circ_0(L_0u)\), with \(L_0u(c):=\operatorname{Ad}(h_0(c_-)^{-1})u(c)\) a real linear isometry of the shell data in sup norm. The real identity (5.8) of row 107 at the argument \(L_0B\) reads
\[
 \tfrac12D^2_u\tilde F^R_0(0)[B,B]=Q^R_{p_{\rm r}}(B)+\tfrac12K^R_1(B)+\tfrac12K^R_2(B),\qquad Q^R_{p_{\rm r}}(B)=Q^\circ_{p_{\rm r}}(L_0B),\quad K^R_i(B):=K^\circ_i(L_0B).
\]
The \(K^R_i\) obey the row-107 bounds, since \(\|L_0B\|_\infty=\|B\|_\infty\). So \(Y^R_2=-\frac12(K^R_1+K^R_2)+\frac12(G^R(0)-G^R(\beta))\) with \(G^R(\beta):=D^2_u\tilde F^R_\beta(0)[B,B]\). Schwarz's lemma on the fixed ball \(\rho^R_Q\) bounds the last bracket as in 4c. \(Y^R_4\) and \(\mathsf L^R\) are as in 4c. \(B\) is the real stored variable with \(\|gB\|_\infty<\delta'\), so the ceiling \(\delta'\le r_{\rm B}/32\) is unchanged. The real bound \(\epsilon_{\rm L}\) at real \(\beta\) uses Lemma LM item 3 for \(S^R\) and (9a)–(9b). There the curvature \(a_{S^R}=a_S\) is gauge invariant, and the \((1-\chi)\) region lies where \(h=\mathbf 1\). Lemma T then applies to \(\mathsf L^R\) as in 4c. \(\square\)

**The U° form keeps a difference.** Covariance at the complex \(h_\beta\) gives \(A(\phi,T^R_\beta(B))=A(\phi,T^\circ_\beta(L_\beta B))\), with \(L_\beta B(c):=\operatorname{Ad}(h_\beta(c_-)^{-1})B(c)\). So
\[
 Y^R(\beta)=Y^\circ_\beta(L_\beta B)+D_Q(\beta),\qquad D_Q(\beta):=Q^R_{p_{\rm r}}(B)-Q^\circ_{p_{\rm r}}(L_\beta B)=Q^\circ_{p_{\rm r}}(L_0B)-Q^\circ_{p_{\rm r}}(L_\beta B),
\]
with \(Y^\circ_\beta(B'):=Q^\circ_{p_{\rm r}}(B')-x\{A(\phi,T^\circ_\beta(B'))-A(\phi,S_\beta)\}\). At \(\beta=\beta(\mathbf p)\), \(D_Q\) is the difference \(Q^R_{p_{\rm r}}(B)-Q^\circ_{p_{\rm r}}(L_{\mathbf p}B)\) of the check. It does not vanish at complex pairs. It is small:
\[
 |D_Q(\beta(\mathbf p))|\le72\,q_Q\,C_h\,\beta_A\,(A_1p_1)^2,\qquad q_Q:=\sup_{v\ \mathrm{real},\ \|v\|_\infty\le1}|Q^\circ_{p_{\rm r}}(v)|\le3072C_{\rm R}^2K_\phi+\tfrac12(k_1+k_2),
\]
where \(k_i\) bound \(K_i\) on the real unit ball (row 107), and the bound on \(q_Q\) is (4.3) with (5.8). *Proof.* \(Q^\circ_{p_{\rm r}}\) is a real symmetric form. Polarization, with \(|X|,|Y|\le|X+iY|\) for Hermitian \(X,Y\), gives \(|Q^\circ(z_1,z_2)|\le8q_Q\|z_1\|\|z_2\|\) for complex arguments. Then \(D_Q=Q^\circ(L_0B-L_\beta B,\,L_0B+L_\beta B)\). Lemma H(a) gives \(\|L_0B-L_\beta B\|\le3C_h\|\beta\|\|B\|\), and \(\|L_0B+L_\beta B\|\le3\|B\|\), \(\|B\|\le A_1p_1\). \(\square\) So \(|D_Q|\le C(1+\ell)^{4r+1+2\mathfrak p_1+q}g_k\), which sits inside the \(e^{-\ell/2}\) term of (5.1). With \(D_Q\) kept, the composed route closes too. \(Y^\circ_\beta(L_\beta B)\) obeys 4c with the complex argument \(L_\beta B\), \(\|gL_\beta B\|\le2\delta'\) (so \(\delta'\le r_{\rm B}/64\)). \(K_i\) at complex arguments cost a factor 12, \(Y_2\) uses Schwarz in \(\beta\) at the fixed argument \(L_{\beta(\mathbf p)}B\), and Lemma T applies to \(\beta\mapsto\mathsf L(\beta;L_\beta B)\), which is real at real \(\beta\). Both routes give the same bound up to constants.
