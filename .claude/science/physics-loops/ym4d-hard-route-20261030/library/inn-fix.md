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
- **(I)** Those of the old Theorem I without its margin premise: Definition R, (ADM'), Corollary P with \(6\beta_A\), Lemma E's enlargement, I1 through Lemma MJ, I2 (P81 at full strength, radius \(r_{\rm B}\)), I3, I5 at the enlarged regularity, GEO3, GEO4, (SEP), (SEP-L) for \(\mathcal L_W\), (Adm-bar), the premises of Proposition D, \(0\le w\le2x\) on \(\operatorname{supp}\psi\), and FLOW (\(|b_i|\le B_*\)) with the tube \(\theta_m\le2x_m\) (SA (R20)). I3 is read as T4's first paragraph at a real critical reference on its **whole** polydisc, with the potential, gradient and current members (`a3-derivative.md` 6–7, (34), 7.3; gate ADVANCE). This is not T4 re-centred at a complex reference.
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
