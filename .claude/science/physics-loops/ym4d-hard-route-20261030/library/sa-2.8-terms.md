lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T10:55Z

# sa-2.8-terms: the ten terms of the outline's Proposition 2.8, displayed and bounded

Queue row 102. Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, checkout `aa9fa8d1b`; Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775` (SHA-256 `d7f77d4d...b4d6f`, fetched once into a scratch folder). Research text, same-model, not gated, not an audit; grants no status. No numeric job was run; every step below is a written argument.

**Credits.** The prepared/healed construction, the cancellation identity of 2.8 and the reference law are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text (SA 17576-17662, 17840-17880). Balaban supplies the programme behind them: CMP 122 (the R operation and Proposition 1, = the outline's Proposition 2.4), CMP 102 (backgrounds), CMP 95, 96, 99 (propagators). The exact ten-term identity (3) below is Codex's, from `library/sa-2.8.md` Section 3; its scope notes are kept. The two-background comparison used throughout is Theorem 6(c) as proved, conditionally, in `library/a3-derivative.md` Section 10 (Claude, on Codex Sections 1-6) and repaired in `gates/a3-derivative-gate.md` (Codex). The signed-minimum identity is `library/sp-decide.md` (4.1), (4.8) and the two-sided Gram bound `library/qr-decide.md` (2.4)-(2.6) (both Codex).

## 0. Result

**Moves:** Package C rank 2 (`library/route-decisions.md` 3.2 item 2 and 4.2 item 3) and reversal test 4.3, second bullet.

| Statement | Verdict |
|---|---|
| Reversal test 4.3, bullet 2, as worded ("signed remainder not small although every term's absolute bound holds") | **cannot fire.** Identity (3) is exact, so the triangle inequality bounds the remainder by the sum of the term bounds. A signed failure has to show up as a term that the source sets to zero but that is not zero, or as a term that has no small bound. Both cases are examined in Section 2. |
| Counterexample search (Section 2: core cutoff, linear term, signed minimum, depth growth, deep exterior weights, denominator) | **no counterexample.** Two defects in the source, both repaired: the linear term in \(B\) does not vanish (D1), and the core cutoff \(\phi_{\rm c}\) has to carry a margin of shells (D2). |
| The ten terms, displayed (Section 1) and bounded (Section 5) | **implication, every step written.** \(|\mathsf R_X|\le\) (6.1) \(\to0\) uniformly in level, depth, torus and history. It reads the named inputs of Section 3: Theorem 6(c) for four specified (sequence, region) pairs, P81 at full strength, Proposition 2.4, (D-F), and the geometric premises GEO1-GEO6. |
| Linear term "vanishes because \(U_0\) is critical" (SA 17866) | **WRONG as stated, harmless.** It equals \(-g_k^{-1}DA(1-\phi,S)[\mathsf HB]\), bounded in (5.9). |
| \(\phi_{\rm c}\) "cuts off the old core" (SA 17855) | **Underspecified.** It must be the core plus about \(\mathsf N_k/2\) inner shells. The literal core indicator puts plaquettes at weighted distance \(O(1)\) from the core mismatch, against the source's own sentence at SA 17874; the scaling in 2.2(a) suggests a remainder of order \(p_0^2\check R_k^3\). With the margin, all ten terms are small. |

What stays open is listed in Section 8. Nothing new is added to the hard core: every analytic input is one already on the A3 list (rows 81, 85, 98, 103), now applied to four named comparisons, plus the geometry the outline asserts in Proposition 2.3.

## 1. Setting and the ten terms

**Units and constants.** Level-\(k\) units: level-\(k\) block side 1, bare spacing \(\eta=L^{-k}\), level-\(j\) spacing \(\xi_j=L^{j-k}\). \(x=x_k\), \(g=g_k=x^{-1/2}\) (so \(xg^2=1\)), \(\varepsilon_k=g\,p_0(g)\), \(\delta'=\delta'_k=gA_1p_1(g)\), \(p_i(g)=(\log g^{-2})^{\mathfrak p_i}\) up to the constants \(A_i\), \(\mathfrak p_1<\mathfrak p_0-Cr\). \(\check R=\check R_k\ge(\log\min_{i\le k}x_i)^r\), \(r\ge2\); \(\mathsf N=\mathsf N_k=\check R_k\); \(k_\flat=k-\mathsf N\) (SA 17334, 17575, 17660). \(\theta=\delta_0/8\) is the rate of Theorem 6(c) as proved (Lemma 10.1). Write \(\ell:=\log x\).

**Fields** (SA 17585-17612, table of `sa-2.8.md` Section 2):

- \(P=U''\): the global prepared background. Its sequence is \(\mathcal O^p\) (the determining sequence after all stages). Its data are \(e^{igB}V_0\) on the shells, with \(V_0=\mathcal M^jS\) on the shell of level \(j\), \(k_\flat\le j\le k\); the stored core datum \(\zeta\) on the core \(C=C_{k_\flat}\); and the unchanged exterior data. \(B\) is the old multiscale shell variable in the tree gauge \(T_0\), with \(\|gB\|_\infty<\delta'\) (SA 17598).
- \(P_X\): the localisation of \(P\) in \(X\) (Theorem 6(c), \(W=X\)).
- \(H=\bar U\): the global healed background. Its sequence is \(\mathcal O^h\), level \(k\) throughout \(X\). Its data are \(e^{igb}V_\Lambda\) on \(\Lambda=\Lambda^{\rm pr}\), the exterior \(V_k\), and the history outside \(X\). \(b\) is the new reference variable in \(\delta_{\rm ax}\), with \(\|gb\|_\infty<M_0\varepsilon_k\) (SA 17604).
- \(R(b)=U_{k,X}(e^{igb}V_\Lambda)\): the localisation of \(H\) in \(X\). \(S=U_0=R(0)\) is the reference critical background.
- \(T(B)\): the background of the localised prepared sequence \(\mathbf D_{pX}=\mathbf D(\mathcal L_X\mathcal O^p)\), with \(e^{igB}V_0\) on the shells and the averages of \(S\) on every other row, the core included. \(F(B)=A(\phi,T(B))\) and \(\widetilde F(u)=A(\phi,\widetilde T(u))\), with \(T(B)=\widetilde T(gB)\).

**Weights.** \(v\) is the healed weight \(x_k(\cdot)\) (\(\Lambda_i\mapsto\Lambda_i\cup X\), SA 17402); \(w=x''_k=x^{(\mathsf N)}\) (SA 17630-17640); \(x\) is the scalar \(x_k=\beta-\sum_{i\le k}b_i\).

**Cutoffs (specified here; the source leaves them open).** \(\chi=\phi_X\) is the indicator of the bare plaquettes \(p\) with \(d(p,X^c)\ge c_0M\check R\). Let \(Z^\natural\) be the union of the core \(C\) and the shells of levels \(k_\flat,\dots,k_\flat+n_{\rm c}-1\), with

\[
 n_{\rm c}:=\lfloor\mathsf N/2\rfloor .
\tag{1.1}
\]

\(\psi=\phi_{\rm c}\) is the indicator of the plaquettes with all corners in \(Z^\natural\), and \(\phi=\chi-\psi=\chi(1-\psi)\) (because \(Z^\natural\subset\Lambda\subset\{\chi=1\}\)). The *margin* is \(Z^\natural\setminus C\). Section 2.2(a) shows why it is needed.

**Gaussian.** \(\mathsf H:=D\widetilde T(0)\), the linear response of the localised prepared background at \(S\) to shell data, in Landau form (Theorem 3). For a plaquette \(p\), \((d_S A)_p\in\mathfrak{su}(2)\) is the first-order term of the holonomy of \(Se^{iA}\) at \(p\), transported to its base point. Then

\[
 Q(B):=\tfrac12\sum_p\phi(p)\,|(d_S\mathsf HB)_p|^2\ \ge0 .
\tag{1.2}
\]

**The remainder** (SA 17856-17865, signs as in `sa-2.8.md` (2)):

\[
 \mathsf R_X=A(v,H)-A(w(1-\psi),P)-xA(\chi,R(b))+xA(\chi,S)+Q(B).
\]

**The ten terms** (`sa-2.8.md` (3); the sum was rechecked line by line here):

\[
\begin{aligned}
 R_1&=A(v(1-\chi),H)-A(v(1-\chi),P) &&\text{neighbouring actions, exterior}\\
 R_2&=A((v-w)(1-\chi),P) &&\text{small weight}\\
 R_3&=x\{A(\chi,H)-A(\chi,R(b))\} &&\text{neighbouring actions, healed localisation}\\
 R_4&=A((v-x)\chi,H) &&\text{small weight}\\
 R_5&=-A((w-x)\phi,P) &&\text{small weight, }O(k-j)\\
 R_6&=x\{A(\phi,P_X)-A(\phi,P)\} &&\text{neighbouring actions, prepared localisation}\\
 R_7&=x\{A(\phi,T(B))-A(\phi,P_X)\} &&\text{neighbouring actions, core replacement}\\
 R_8&=-x\{F(B)-F(0)-DF(0)[B]-\tfrac12D^2F(0)[B,B]\} &&\text{beyond quadratic Taylor}\\
 R_9&=x\{A(\phi,S)-F(0)-DF(0)[B]-\tfrac12D^2F(0)[B,B]\}+Q(B) &&\text{linear term, Hessian identification}\\
 R_{10}&=xA(\psi,S) &&\text{reference action in the shrinking core}
\end{aligned}
\tag{1.3}
\]

\(\sum_aR_a=\mathsf R_X\) identically: \(R_1+\dots+R_4=A(v,H)-A(w(1-\chi),P)-xA(\chi,R(b))\), \(R_5+\dots+R_9=-A(w\phi,P)+xA(\phi,S)+Q\), and \((1-\chi)+\phi=1-\psi\), \(\phi+\psi=\chi\). No estimate is used. The source's three kinds of term (SA 17871-17873) are, in order, \(R_1,R_3,R_6,R_7\); \(R_2,R_4,R_5,R_{10}\); and \(R_8,R_9\).

## 2. Counterexample first

### 2.1 The reversal test as worded

Reversal test 4.3, second bullet, asks for a prepared component on which the signed remainder is not small although every term's absolute bound holds. (1.3) is an exact identity, so \(|\mathsf R_X|\le\sum_a|R_a|\). If every \(R_a\) obeys a bound \(b_a\) and \(\sum_ab_a\to0\), then \(\mathsf R_X\to0\), with no room for cancellation to fail. The test can therefore fire in only two ways:

- **(i)** a term that the source treats as zero is not zero and is not small. The candidates are the linear term in \(B\), the identity \(T(0)=S\) and the Hessian identification (all in \(R_9\)), and the weight equalities (\(R_2,R_4\)).
- **(ii)** a term has no small bound at all. The candidates are \(R_7\) near the core, \(R_5\) and \(R_1\) with weights that grow with depth, and \(R_8\) with \(O(\mathsf N(LM)^4)\) shell bonds.

Each candidate is attacked below, hardest first. "Small" means \(\to0\) as \(g_k\to0\), uniformly in level, depth, torus and history.

### 2.2 Attempts

**(a) The core cutoff without a margin. The source's inference fails; the repair is the margin.** Take \(\psi=\mathbf 1_C\), the literal reading of "\(\phi_{\rm c}\) cuts off its old core" (SA 17855). Then \(\operatorname{supp}\phi\) contains the plaquettes of the innermost shell (level \(k_\flat\)) that touch \(C\). \(T(B)\) and \(P_X\) have the same rows and data everywhere except on the core, so \(R_7\) compares them on a region whose boundary is \(\partial C\), and the compared plaquettes lie at weighted distance \(\le2\) from it. The source's sentence "the plaquettes being compared lie at weighted distance at least \(cM\check R_k\) from its boundary" (SA 17874-17875) is false for this comparison, and with it the claimed factor \(e^{-c\delta_0M(\log\theta_k)^r}\).

How large the term could be, as a scaling estimate (an expectation; unchecked):

- The core datum next to the shells is only constrained by the last-shell test, \(|\partial U_{k_\flat,\square}((\mathbf1,V_{k_\flat}))-\mathbf1|<\tfrac12\varepsilon_{k_\flat}\eta_{k_\flat}^2\) (SA 17598), and inside by (D-F), \(C_F\check R^2\varepsilon\). A datum with level-\(k_\flat\) curvature \(\varepsilon_{k_\flat}/4\) along \(\partial C\) passes every test.
- The background spreads the flux of the mixed level-\(k_\flat\) plaquettes across \(\partial C\) onto both sides. Its curvature on the first shell layer is then expected to be of order \(\varepsilon_{k_\flat}\), whereas \(T(B)\) (built from \(S\)) has curvature \(\le\delta'+C(M)\varepsilon_kL^{-2\mathsf N}\) there.
- Per adjacent block of level \(k_\flat\), \(x\varepsilon_{k_\flat}^2\asymp p_0(g)^2\). There are about \((M\check R)^3\) such blocks, so \(|R_7|\sim p_0^2\check R^3\), which grows with \(x\).

The same comparison at first order in \(B\) gives the innermost shell bonds a linear force. It is the shell-row multiplier of \(P_X(0)\), of size up to \(g^{-1}\varepsilon_{k_\flat}\asymp p_0\) per bond, against a Gaussian of curvature 1 and a window \(|B|<A_1p_1\ll p_0\). With \(\psi=\mathbf 1_C\), then, the inner \(B\)'s are not a centred Gaussian, and \(e^{-Q}\) misrepresents them. A proof of these lower bounds would need a converse to 6(c), which is not attempted: no consumer reads the literal cutoff.

**Repair (D2).** Take \(\psi=\mathbf 1_{Z^\natural}\) with the margin (1.1). Crossing a shell costs \(\ge M\) in \(d_{\mathbf B}\) (GEO3), so \(d(\operatorname{supp}\phi,C)\ge Mn_{\rm c}\ge\tfrac12M\check R-M\). This is the source's distance clause with \(c=\tfrac12\). Its cost is checked in 5.10 (\(R_{10}\) keeps a factor \(L^{-4(\mathsf N-n_{\rm c}-1)}\)) and in Section 7 (the inner-shell Gaussian moves into the retained core term). A margin of \(C\log\ell/(\theta M)\) shells would already make \(R_7\to0\). The choice \(\mathsf N/2\) reproduces the source's rate.

**(b) The linear term. Not zero (D1); bounded.** The source says (SA 17866): "The linear term in \(B\) vanishes because \(U_0\) is critical on the fibre." Exactly, by Lemma LM below,

\[
 xDF(0)[B]=g^{-1}D\widetilde F(0)[B]=g^{-1}DA(\phi,S)[\mathsf HB]
 =-g^{-1}\big\{DA(\psi,S)[\mathsf HB]+DA(1-\chi,S)[\mathsf HB]\big\}.
\tag{2.1}
\]

The criticality of \(S\) kills \(DA(1,S)[\mathsf HB]\), not \(DA(\phi,S)[\mathsf HB]\). The right side vanishes only if the current of \(S\) is orthogonal to \(\mathsf HB\) on \(\operatorname{supp}\psi\cup\operatorname{supp}(1-\chi)\), and nothing in the construction provides that. Inside the margin, \(\mathsf HB=O(\|B\|)\) with no decay, and \(S\) has curvature \(C(M)\varepsilon_k\). The bound (5.9) shows that the term is small: \(g^{-1}\) is beaten by the factor \(\xi^2\le L^{-2(\mathsf N-n_{\rm c})}\) inside \(Z^\natural\), and by \(e^{-\theta c_0M\check R/2}\) outside \(\chi\). So the source's sentence is wrong as stated and harmless after the repair. A large linear term would need \(S\) to carry a current of order 1 inside \(Z^\natural\). That contradicts Proposition 2.4's bound \(|\partial S-\mathbf1|\le C(M)\varepsilon_k\eta^2\).

**(c) The signed change of minimum (`sp-decide.md` (4.1)), at \(B=b=0\).** Here \(\mathsf R_X(0,0)=A(v,H_0)-A(w(1-\psi),P_0)\). Write \(m_0=A(1,S)\) and \(m_p=A(1,P_X(0))\), the minimum of the localised prepared problem with core datum \(\zeta\) and shell data \(V_0\). By (4.1), \(A(U)-m_0=[A(U)-m_p]+[m_p-m_0]\), and \(m_p-m_0\ge0\): \(P_X(0)\) lies in the class of Proposition 2.4, which has \(S\) as its minimum, because \(A(P_X(0))\ge A(U_{k,X}(\mathcal M^kP_X(0)))\ge A(S)\).

The signed excess \(x(m_p-m_0)\) is large. It is the action price of the core datum, of order \(x\varepsilon_{k_\flat}^2\) per core-boundary block. It splits as
\[x(m_p-m_0)=x[A(\psi,\cdot)]_S^{P_X(0)}-R_7|_{B=0}+x[A(1-\chi,\cdot)]_S^{P_X(0)}.\]
The first piece sits on the retained side. So the only route by which the large signed quantity can reach \(\mathsf R_X\) is leakage out of \(Z^\natural\), which is \(R_7\), bounded by (W3) in 5.7.

The lesson of (4.8) applies: a signed change of minimum has either sign and is not controlled by any positivity or fluctuation cost. No convexity argument can replace the decay estimate here. A counterexample along this line is exactly a failure of 6(c) for the core-complement region (W3).

**(d) Growth with depth. Absorbed in every case.** There are three sources of growth.

- (d1) \(|w-x|\le B_*(k-j+d_0+1)\) on shell \(j\) (Lemma W). Summed over the outer shells, \(R_5=O(\mathsf N\cdot K_X\varepsilon_1^2)=O(g^2\,\mathrm{polylog})\).
- (d2) In \(R_1\) the exterior weights \(v(p)\le x_k+B_*(k-j(p)+d_0+1)\) grow linearly in \(k-j\) on deep levels \(j\ll k\) outside \(X\). The weighted distance grows at least like \(c_g(k-j-1)\) (GEO4), so Lemma BC absorbs every polynomial in \(k-j\). The thresholds do not grow: \(x\mapsto x^{-1/2}(\log x)^a\) decreases for \(\log x>2a\), so \(\check R_j^2\varepsilon_j\le4L^2\check R_k^2\varepsilon_k\) whenever \(x_j\ge x_k-c_5\) and \(x_k\) is large.
- (d3) The localised problems carry collar towers down to bare level, with \(L^{4(k-q)}\) tops at level \(q\). The response decays in the joined metric, which grows by \(\ge\rho\) per tower level (Theorem 6(a)). Lemma BC, applied to the joined sequence, gives a sum free of the depth \(k\). Measured in the original metric, the collar would cost a factor of order \(k\).

**(e) Large fields elsewhere.** Other components' large fields sit off the determining set (`floor-screen.md` Lemma O; gate item 1: off the full fixed joined datum). On the determining set the data are regular, by (D-F) (rows 96, 97). So \(P\) and \(H\) exist globally, and \(R_1\) is a comparison of two regular backgrounds.

**(f) The denominator.** \(\log\mathsf D_X=-xA(\chi,S)+\log Z_b(S)\), where \(Z_b(S)\) is the \(b\)-fluctuation integral. It is not one of the ten terms. Section 7 shows that it depends on the field only through a factor \(e^{O(n_b\varepsilon_h)}\), \(n_b\le12(C_nM)^4\). That is small, but it is not a "number" (D3).

### 2.3 Verdict

No counterexample. The reversal test of `route-decisions.md` 4.3, second bullet, does not fire. Every route to a signed failure ends at one of the inputs of Section 3, mainly 6(c) for the core-complement region (W3) and the box-complement region (W4). Two statements of the source are corrected (D1, D2), and one consumer item is added (D3).

## 3. Inputs, with their standing

Nothing below is proved here. Each input is either a gated implication on the A3 list or an assertion of the outline, and each is labelled.

**I1, Theorem 6(c), two-background form** (SA 9783-9789, last sentence: "Two backgrounds whose sequences and whose data coincide on \(W\) differ there to this extent"). Let \(U,U'\) be real backgrounds whose sequences and real \(\varepsilon_1\)-regular data coincide on a \(\mu\)-collared region \(W\), each collar lying in one layer, with \(\varepsilon_1\le\mathsf a(L,\rho,\mu)\). Then on \(W\),
\[U=(e^{i\eta f}U^\circ_W)^w,\qquad U'=(e^{i\eta f'}U^\circ_W)^{w'},\]
and at every top \(y\) of the joined sequence away from the collars,
\[\xi_y|f|,\ \xi_y^2|\nabla f|\le E\,e^{-\theta d_{\mathbf B}(y,W^c)},\qquad E:=C_\mu\varepsilon_1,\]
and likewise for \(f'\), with \(d_{\mathbf B}\) the original metric. It is used for four instances:

| | sequences | \(W\) | pair | term |
|---|---|---|---|---|
| W1 | \(\mathcal O^p\) (global) | \(X\) | \(P,\ P_X\) | \(R_6\) |
| W2 | \(\mathcal O^h\) (global) | \(X\) | \(H,\ R(b)\) | \(R_3\) |
| W3 | \(\mathbf D_{pX}\) | localised domain minus \(C\); collar in the level-\(k_\flat\) shell | \(T(B),\ P_X\) | \(R_7\) |
| W4 | \(\mathcal O^p\), \(\mathcal O^h\) (global) | \(\mathbb T\setminus\Lambda\); collar in \(X\setminus\Lambda\), layer \(k\) | \(P,\ H\) | \(R_1\) |

Coincidence on \(W\): for W1 and W2 by definition of the localisation. For W3, \(T(B)\) and \(P_X\) share \(\mathbf D_{pX}\) and all data off \(C\). For W4, in \(X\setminus\Lambda\) both \(\mathcal O^p\) and \(\mathcal O^h\) contain every level up to \(k\) (\(Z''_i\subset\Lambda\), \(X\setminus C\subset\Omega_{k_\flat}\)), with the same datum \(V_k\); outside \(X\) both are the history's.

*Standing:* `library/a3-derivative.md` Lemma 10.1, gated ADVANCE as a repaired conditional implication (`gates/a3-derivative-gate.md` Section 10), from P81, P82° (gated implication, `gates/p82-curved-gate.md`, given \(U_0\in\mathrm{Reg}\), open in row 103 (1)), (G1) and separatedness for the actual joined sequence (open, row 103 (3)), and admission. W1 and W2 are the instances that row 103 names. **W3 and W4 are new instances of the same premise**: regions with a hole, one of them global.

**I2, P81 at full strength,** for \(\mathbf D_{pX}\) and for \(\mathbf D(\mathcal L_X\mathcal O^h)\). It supplies:
- a unique regular critical orbit near the datum of \(S\);
- a holomorphic chart \(\Phi\) on the sup-norm polydisc of radius \(r_{\rm B}\) (local units) around that datum, with \(q\circ\Phi=\mathrm{id}\), Landau representative \(\Phi=(e^{i\eta\tau})^{u}\) (Theorem 3), and complex regularity: at every top, local complex curvature and \(\xi|\tau|\), \(\xi^2|\nabla\tau|\) are \(\le C_{\rm R}r_{\rm B}\);
- the Lagrange representation \(\nabla A(S)=Dq(S)^{\mathsf T}\lambda\).

*Standing:* `library/a1-balaban.md`, gated (row 91), given F0 (discharged by row 95, gated in row 99). Open: pointed-core admission (10.2), and complex regularity at full strength (`gates/a3-derivative-gate.md` Section 12 item 4). The multiplier is used only through \(\lambda_\Lambda=0\) and the pairing \(\lambda\cdot Dq\); both are free of normalisation, so M1 is not read.

**I3, Theorem 4 at the real critical reference \(S\),** for \(\mathbf D_{pX}\) and for the reference problem, in the all-weights form (BGR11 row sums, Lemma 8.2). For a shell datum \(v\), the response \(h=\mathsf Hv\) obeys, at every top of the joined sequence,
\[\xi_y|h(y)|\le C_4\|v\|_\infty,\qquad \xi_y^2|\nabla h(y)|\le C_4\|v\|_\infty e^{-\theta d_{\mathbf B'}(y,\operatorname{supp}v)}\]
(\(\mathbf B'\) the joined metric). *Standing:* `library/a3-derivative.md` Theorem 4, first paragraph (real critical references), gated ADVANCE as repaired, from P81 and P82°. Only real critical references are used, so the independent-current and complex-reference paragraphs (M2, item 3 of the gate) are not read.

**I4, Proposition 2.4** (Balaban CMP 122 Proposition 1; SA 17656-17662; cited-pending, not in hand). \(V_\Lambda\) is the unique critical orbit of \(f(V)=A(U_{k,X}(V))\) and its minimum in the mild class. \(|\partial S_p-\mathbf1|\le C(M)\varepsilon_k\eta^2\) on the plaquettes of \(\Lambda\) and of an \(O(1)\) neighbourhood. In axial gauge the Hessian is \(\ge c(M)>0\).

**I5, (D-F) and the profile bound.** On the support of the tests, the data of \(\mathcal O^p\), \(\mathcal O^h\), their localisations and \(\mathbf D_{pX}\) are \(\varepsilon_1\)-regular, with
\[\varepsilon_1:=4L^2C_F\check R^2\varepsilon_k\]
(the old-core datum at \(C_F\check R_l^2\varepsilon_l\), the shells at \(\delta'+C(M)\varepsilon_k\), the new box at \((C(M)+4M_0)\varepsilon_k\), all \(\le\varepsilon_1\) by 2.2(d2)). Every background involved has local curvature \(a(y)\le C_{\rm P}\varepsilon_1\) at every top. *Standing:* (D-F) gated for every case (rows 88, 94, 96, 97), given Proposition 2.4 and premises H1-H4. The curvature bound is (1b) Theorem 2, first half (`library/a3-profile.md`, gated row 86), given P81 and P82.

**GEO, geometry asserted by the outline** (Proposition 2.3, catalogue C2; not checked here):
- GEO1: \(\operatorname{dist}(\Lambda,X^c)\ge2M\check R-M\). By SA 17576-17580, \(\Omega_k^c\cap X=H_k^{[8]}\) and \(X=X\cap Z_k=H_k^{[10]}\) (pushed out by 8 and 10 level-\(k\) cells of side \(M\check R\)). The nest boxes lie in \(\Omega_l^c\cap X\) (SA 17421), and \(\Lambda\) is \(Z''_k\) plus one layer of \(M\)-cubes (SA 17598). Fix \(c_0:=\tfrac12\). For \(\check R\ge4+4C_c\mu/M\) this gives \(d(\operatorname{supp}\chi,X^c)\ge\tfrac12M\check R\) and \(d(\Lambda,\operatorname{supp}(1-\chi))\ge M\check R\), both measured in level-\(k\) units, where \(d_{\mathbf B}\) is Euclidean.
- GEO2: \(X\) has at most \(n_X^4\) cells of level \(k\) (SA 17583).
- GEO3: the core has side \(\le C_nM\check R\,\xi_{k_\flat}\). The shell of level \(j\) has width \(\ge M\xi_j\) and at most \((C_nM(\check RL^{k_\flat-j}+L))^4\) tops. The level-\(k_\flat\) shell contains the collar of W3 (\(M\ge C_c\mu\)).
- GEO4 (gaps): every sequence used, joined sequences included, has \(\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})\ge c_g\xi_j\) for all \(j\). Here \(c_g\ge M\) on label and prepared layers and \(c_g\ge\rho\) on tower layers, with \(64\log L\le\theta\min(M,\rho)\).
- GEO5 (profiles, SA 6331-6336: supplied data): \(\varphi[\Lambda](p)\) depends only on \(\Lambda\) within \(w_*\le\tfrac12c_0M\check R\) of \(p\). It is \(0\) off \(\Lambda\) and \(1\) at points of \(\Lambda\) farther than \(w_*\) from \(\Lambda^c\). For \(p\) in the shell of level \(j\), \(\varphi[\Lambda^{(\mathsf N)}_i](p)=1\) for \(i<j-d_0\) and \(=0\) for \(i>j\).
- GEO6: \(X\cap\Lambda_i^c\subset C\cup\{\text{layer }\Omega_i\setminus\Lambda_i\}\) for \(i\le k_\flat\). This follows from \(Z_i\subset Z_{k_\flat}\) and \(C=X\cap Z_{k_\flat}\).

**FLOW** (Theorem 2.1 hypotheses, `sa-2.8.md` Section 4): \(|b_i|\le B_*\); \(\min_{i\le k}x_i\ge x_k-c_5\) (R19). Hence \(\check R\ge\tfrac12\ell^r\) for \(x\ge2c_5\), and \(\mathsf N=\check R\).
