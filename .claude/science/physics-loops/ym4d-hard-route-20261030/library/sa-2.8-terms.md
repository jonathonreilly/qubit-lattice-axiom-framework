lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T10:55Z

# sa-2.8-terms: the ten terms of the outline's Proposition 2.8, displayed and bounded

Queue row 102. Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, checkout `aa9fa8d1b`; Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775` (SHA-256 `d7f77d4d...b4d6f`, fetched once into a scratch folder). Research text, same-model, not gated, not an audit; grants no status. No numeric job was run; every step below is a written argument.

**Credits.** The prepared/healed construction, the cancellation identity of 2.8 and the reference law are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text (SA 17576-17662, 17840-17880). Balaban supplies the programme behind them: CMP 122 (the R operation and Proposition 1, = the outline's Proposition 2.4), CMP 102 (backgrounds), CMP 95, 96, 99 (propagators). The exact ten-term identity (1.3) below is Codex's (`library/sa-2.8.md` (3)); its scope notes are kept. The two-background comparison used throughout is Theorem 6(c) as proved, conditionally, in `library/a3-derivative.md` Section 10 (Claude, on Codex Sections 1-6) and repaired in `gates/a3-derivative-gate.md` (Codex). The signed-minimum identity is `library/sp-decide.md` (4.1), (4.8) and the two-sided Gram bound `library/qr-decide.md` (2.4)-(2.6) (both Codex).

**Status:** finished 2026-11-02T23:48Z (worker); same-model implication, ungated. A cross-provider gate is needed before anything here counts.

## 0. Result

**Moves:** Package C rank 2 (`library/route-decisions.md` 3.2 item 2 and 4.2 item 3) and reversal test 4.3, second bullet.

| Statement | Verdict |
|---|---|
| Reversal test 4.3, bullet 2, as worded ("signed remainder not small although every term's absolute bound holds") | **cannot fire.** Identity (1.3) is exact, so the triangle inequality bounds the remainder by the sum of the term bounds. A signed failure has to show up as a term that the source sets to zero but that is not zero, or as a term that has no small bound. Both cases are examined in Section 2. |
| Counterexample search (Section 2: core cutoff, linear term, signed minimum, depth growth, deep exterior weights, denominator) | **no counterexample.** Two defects in the source, both repaired: the linear term in \(B\) does not vanish (D1), and the core cutoff \(\phi_{\rm c}\) has to carry a margin of shells (D2). |
| The ten terms, displayed (Section 1) and bounded (Section 5) | **implication; every step is written here or in a cited gated text.** \(|\mathsf R_X|\le\) (6.1) \(\to0\) uniformly in level, depth, torus and history. It reads the named inputs of Section 3: Lemma 10.1 (Theorem 6(c)) on auxiliary meet localisations for four comparisons, with (SEP), (SEP-L); P81 at full strength; Theorem 4 at the real critical reference; Proposition 2.4; (D-F) with the profile bound; and the geometric premises GEO1-GEO6 and EXT. |
| Linear term "vanishes because \(U_0\) is critical" (SA 17866) | **WRONG as stated, harmless.** It equals \(-g_k^{-1}DA(1-\phi,S)[\eta\mathsf HB]\), bounded in 5.8, (9a)-(9b). |
| (G1) of `gates/a3-derivative-gate.md` (identification of the outline's joined sequence), as read by 2.8 | **not needed.** Every comparison goes through an auxiliary meet localisation (Lemma MJ), for which (G1)-(G3) hold by construction; this is the gate's own visible repair. What 2.8 reads of row 103 (3) is only (SEP) and (SEP-L): the outline's localisations are separated and agree with the global sequences inside \(X\) away from their collar. |
| \(\phi_{\rm c}\) "cuts off the old core" (SA 17855) | **Underspecified.** It must be the core plus about \(\mathsf N_k/2\) inner shells. The literal core indicator puts plaquettes at weighted distance \(O(1)\) from the core mismatch, against the source's own sentence at SA 17874; the scaling in 2.2(a) suggests a remainder of order \(p_0^2\check R_k^3\). With the margin, all ten terms are small. |

What stays open is listed in Section 8. Nothing new is added to the hard core: every analytic input is one already on the A3 list (rows 81, 85, 98, 103), now applied to four named comparisons, plus the geometry the outline asserts in Proposition 2.3.

## 1. Setting and the ten terms

**Units and constants.** Level-\(k\) units: level-\(k\) block side 1, bare spacing \(\eta=L^{-k}\), level-\(j\) spacing \(\xi_j=L^{j-k}\). \(x=x_k\), \(g=g_k=x^{-1/2}\) (so \(xg^2=1\)), \(\varepsilon_k=g\,p_0(g)\), \(\delta'=\delta'_k=gA_1p_1(g)\), \(p_0(g)=A_0(\log g^{-2})^{\mathfrak p_0}\), \(p_1(g)=(\log g^{-2})^{\mathfrak p_1}\), \(\mathfrak p_1<\mathfrak p_0-Cr\). \(\check R=\check R_k\ge(\log\min_{i\le k}x_i)^r\), \(r\ge2\); \(\mathsf N=\mathsf N_k=\check R_k\); \(k_\flat=k-\mathsf N\) (SA 17334, 17575, 17660). \(\theta=\delta_0/8\) is the rate of Theorem 6(c) as proved (Lemma 10.1). Write \(\ell:=\log x\).

**Fields** (SA 17585-17612, table of `sa-2.8.md` Section 2):

- \(P=U''\): the global prepared background. Its sequence is \(\mathcal O^p\) (the determining sequence after all stages). Its data are \(e^{igB}V_0\) on the shells, with \(V_0=\mathcal M^jS\) on the shell of level \(j\), \(k_\flat\le j\le k\); the stored core datum \(\zeta\) on the core \(C=C_{k_\flat}\); and the unchanged exterior data. \(B\) is the old multiscale shell variable in the tree gauge \(T_0\), with \(\|gB\|_\infty<\delta'\) (SA 17598).
- \(P_X\): the localisation of \(P\) in \(X\) (Theorem 6(c), \(W=X\)).
- \(H=\bar U\): the global healed background. Its sequence is \(\mathcal O^h\), level \(k\) throughout \(X\). Its data are \(e^{igb}V_\Lambda\) on \(\Lambda=\Lambda^{\rm pr}\), the exterior \(V_k\), and the history outside \(X\). \(b\) is the new reference variable in \(\delta_{\rm ax}\), with \(\|gb\|_\infty<M_0\varepsilon_k\) (SA 17604).
- \(R(b)=U_{k,X}(e^{igb}V_\Lambda)\): the localisation of \(H\) in \(X\). \(S=U_0=R(0)\) is the reference critical background.
- \(T(B)\): the background of the localised prepared sequence \(\mathbf D_{pX}=\mathbf D(\mathcal L_X\mathcal O^p)\), with \(e^{igB}V_0\) on the shells and the averages of \(S\) on every other row, the core included. \(F(B)=A(\phi,T(B))\) and \(\widetilde F(u)=A(\phi,\widetilde T(u))\), with \(T(B)=\widetilde T(gB)\).

**Weights.** \(v\) is the healed weight \(x_k(\cdot)\) (\(\Lambda_i\mapsto\Lambda_i\cup X\), SA 17402); \(w=x''_k=x^{(\mathsf N)}\) (SA 17630-17640); \(x\) is the scalar \(x_k=\beta-\sum_{i\le k}b_i\).

**Cutoffs (specified here; the source leaves them open).** \(\chi=\phi_X\) is the indicator of the bare plaquettes \(p\) with \(d(p,X^c)\ge\tfrac34M\check R\). Let \(Z^\natural\) be the union of the core \(C\) and the shells of levels \(k_\flat,\dots,k_\flat+n_{\rm c}-1\), with

\[
 n_{\rm c}:=\lfloor\mathsf N/2\rfloor .
\tag{1.1}
\]

\(\psi=\phi_{\rm c}\) is the indicator of the plaquettes with all corners in \(Z^\natural\), and \(\phi=\chi-\psi=\chi(1-\psi)\) (because \(Z^\natural\subset\Lambda\subset\{\chi=1\}\)). The *margin* is \(Z^\natural\setminus C\). Section 2.2(a) shows why it is needed.

**Gaussian.** Write \(\widetilde T(u)=(e^{i\eta\tau(u)}S)^{w(u)}\) in Landau form (Theorem 3), and let \(\mathsf H:=D\tau(0)\) be the linear response of the localised prepared background at \(S\) to shell data. The bare-bond angle of the response is then \(\eta\mathsf HB\). For a plaquette \(p\), \((d_S A)_p\in\mathfrak{su}(2)\) is the first-order term of the holonomy of \(e^{iA}S\) at \(p\), transported to its base point. Then

\[
 Q(B):=\tfrac12\sum_p\phi(p)\,|(d_S\eta\mathsf HB)_p|^2\ \ge0 .
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

**Repair (D2).** Take \(\psi=\mathbf 1_{Z^\natural}\) with the margin (1.1). Crossing a shell costs \(\ge M\) in \(d_{\mathbf B}\) (GEO3), so \(d(\operatorname{supp}\phi,C)\ge Mn_{\rm c}\ge\tfrac12M\check R-M\). This is the source's distance clause with \(c=\tfrac12\). Its cost is checked in 5.9 (\(R_{10}\) keeps a factor \(L^{-4(\mathsf N-n_{\rm c})}\)) and in Section 7 (the inner-shell Gaussian moves into the retained core term). A margin of \(C\log\ell/(\theta M)\) shells would already make \(R_7\to0\). The choice \(\mathsf N/2\) reproduces the source's rate.

**(b) The linear term. Not zero (D1); bounded.** The source says (SA 17866): "The linear term in \(B\) vanishes because \(U_0\) is critical on the fibre." Exactly, by Lemma LM below,

\[
 xDF(0)[B]=g^{-1}D\widetilde F(0)[B]=g^{-1}DA(\phi,S)[\eta\mathsf HB]
 =-g^{-1}\big\{DA(\psi,S)[\eta\mathsf HB]+DA(1-\chi,S)[\eta\mathsf HB]\big\}.
\tag{2.1}
\]

The criticality of \(S\) kills \(DA(1,S)[\eta\mathsf HB]\), not \(DA(\phi,S)[\eta\mathsf HB]\). The right side vanishes only if the current of \(S\) is orthogonal to \(\eta\mathsf HB\) on \(\operatorname{supp}\psi\cup\operatorname{supp}(1-\chi)\), and nothing in the construction provides that. Inside the margin, \(\mathsf HB=O(\|B\|)\) with no decay, and \(S\) has curvature \(C(M)\varepsilon_k\). The bounds (9a), (9b) of 5.8 show that the term is small: \(g^{-1}\) is beaten by the factor \(\xi^2\le L^{-2(\mathsf N-n_{\rm c})}\) inside \(Z^\natural\), and by \(e^{-\theta M\check R/2}\) outside \(\chi\). So the source's sentence is wrong as stated and harmless after the repair. A large linear term would need \(S\) to carry a current of order 1 inside \(Z^\natural\). That contradicts Proposition 2.4's bound \(|\partial S-\mathbf1|\le C(M)\varepsilon_k\eta^2\).

**(c) The signed change of minimum (`sp-decide.md` (4.1)), at \(B=b=0\).** Here \(\mathsf R_X(0,0)=A(v,H_0)-A(w(1-\psi),P_0)\). Write \(m_0=A(1,S)\) and \(m_p=A(1,P_X(0))\), the minimum of the localised prepared problem with core datum \(\zeta\) and shell data \(V_0\). By (4.1), \(A(U)-m_0=[A(U)-m_p]+[m_p-m_0]\), and \(m_p-m_0\ge0\): \(P_X(0)\) lies in the class of Proposition 2.4, which has \(S\) as its minimum, because \(A(P_X(0))\ge A(U_{k,X}(\mathcal M^kP_X(0)))\ge A(S)\).

The signed excess \(x(m_p-m_0)\) is large. It is the action price of the core datum, of order \(x\varepsilon_{k_\flat}^2\) per core-boundary block. It splits as
\[x(m_p-m_0)=x[A(\psi,\cdot)]_S^{P_X(0)}-R_7|_{B=0}+x[A(1-\chi,\cdot)]_S^{P_X(0)}.\]
The first piece sits on the retained side. The third compares two localised backgrounds that agree, rows and data, outside \(\Lambda\) (EXT), and it is bounded exactly as \(R_1\) is (I1 on the box complement, Lemma BC). So the only route by which the large signed quantity can reach \(\mathsf R_X\) is leakage out of \(Z^\natural\), which is \(R_7\), bounded by (W3) in 5.4.

The lesson of (4.8) applies: a signed change of minimum has either sign and is not controlled by any positivity or fluctuation cost. No convexity argument can replace the decay estimate here. A counterexample along this line is exactly a failure of 6(c) for the core-complement region (W3).

**(d) Growth with depth. Absorbed in every case.** There are three sources of growth.

- (d1) \(|w-x|\le B_*\mathsf N\) on \(\operatorname{supp}\phi\) (Lemma W). Summed over the outer shells, \(R_5=O(\mathsf N\cdot K_X\varepsilon_1^2)=O(g^2\,\mathrm{polylog})\).
- (d2) In \(R_1\) the exterior weights \(v(p)\le x_k+B_*d_0(1+\check R)(1+k-j)\) grow linearly in \(k-j\) on deep levels \(j\ll k\) outside \(X\). The weighted distance grows at least like \(c_g(k-j-1)\) (GEO4), so Lemma BC absorbs every polynomial in \(k-j\). The thresholds do not grow: \(x\mapsto x^{-1/2}(\log x)^a\) decreases for \(\log x>2a\), so \(\check R_j^2\varepsilon_j\le4L^2\check R_k^2\varepsilon_k\) whenever \(x_j\ge x_k-c_5\) and \(x_k\) is large.
- (d3) The localised problems carry collar towers down to bare level, with \(L^{4(k-q)}\) tops at level \(q\). The response decays in the joined metric, which grows by \(\ge\rho\) per tower level (Theorem 6(a)). Lemma BC, applied to the joined sequence, gives a sum free of the depth \(k\). In the original metric the tower tops would get no extra suppression, so the joined metric is needed for this sum.

**(e) Large fields elsewhere.** Other components' large fields sit off the determining set (`floor-screen.md` Lemma O; gate item 1: off the full fixed joined datum). On the determining set the data are regular, by (D-F) (rows 96, 97). So \(P\) and \(H\) exist globally, and \(R_1\) is a comparison of two regular backgrounds.

**(f) The denominator.** \(\log\mathsf D_X=-xA(\chi,S)+\log Z_b(S)\), where \(Z_b(S)\) is the \(b\)-fluctuation integral. It is not one of the ten terms. Section 7 shows that it depends on the field only through a factor \(e^{O(n_b\varepsilon_h)}\), \(n_b\le12(C_\Lambda M)^4\). That is small, but it is not a "number" (D3).

### 2.3 Verdict

No counterexample. The reversal test of `route-decisions.md` 4.3, second bullet, does not fire. Every route to a signed failure ends at one of the inputs of Section 3, mainly Lemma 10.1 (P81, P82°) on the meet sequences of the four comparisons W1-W4, with (SEP) and (SEP-L). Two statements of the source are corrected (D1, D2), and one consumer item is added (D3).

## 3. Inputs, with their standing

Nothing below is proved here. Each input is either a gated implication on the A3 list or an assertion of the outline, and each is labelled.

**I1, Theorem 6(c), two-background form** (SA 9783-9789, last sentence: "Two backgrounds whose sequences and whose data coincide on \(W\) differ there to this extent"). Let \(U,U'\) be real backgrounds of separated sequences whose members and real \(\varepsilon_1\)-regular data coincide on a \(\mu\)-collared region \(W\), each collar lying in one layer, with \(\varepsilon_1\le\mathsf a(L,\rho,\mu)\). Let \(U^\circ_W\) be the background of the **meet** joined sequence of Lemma MJ, which is the same for both sequences by MJ(iii). Then on \(W\),
\[U=(e^{i\eta f}U^\circ_W)^w,\qquad U'=(e^{i\eta f'}U^\circ_W)^{w'},\]
and at every top \(y\) of the joined sequence away from the collars,
\[\xi_y|f|,\ \xi_y^2|\nabla f|\le E\,e^{-\theta d_{\mathbf B}(y,W^c)},\qquad E:=C_\mu\varepsilon_1,\]
and likewise for \(f'\), with \(d_{\mathbf B}\) the original metric. It is used for four instances:

| | sequences | \(W\) | pair | term |
|---|---|---|---|---|
| W1 | \(\mathcal O^p\) and \(\mathcal L_X\mathcal O^p\) | \(X^-:=\{d(\cdot,X^c)\ge\tfrac14M\check R\}\) | \(P,\ P_X\) | \(R_6\) |
| W2 | \(\mathcal O^h\) and \(\mathcal L_X\mathcal O^h\) | \(X^-\) | \(H,\ R(b)\) | \(R_3\) |
| W3 | \(\mathbf D_{pX}\) | localised domain minus \(C\); collar in the level-\(k_\flat\) shell | \(T(B),\ P_X\) | \(R_7\) |
| W4 | \(\mathcal O^p\), \(\mathcal O^h\) (global) | \(\mathbb T\setminus\Lambda\); collar in \(X\setminus\Lambda\), layer \(k\) | \(P,\ H\) | \(R_1\) |

Coincidence on \(W\): for W1 and W2 by (SEP-L) below, since the outline's collar of \(X\) has width \(\le C_c\mu\le\tfrac14M\check R\). For W3, \(T(B)\) and \(P_X\) share \(\mathbf D_{pX}\) and all data off \(C\). For W4, in \(X\setminus\Lambda\) both \(\mathcal O^p\) and \(\mathcal O^h\) contain every level up to \(k\) (\(Z''_i\subset\Lambda\), \(X\setminus C\subset\Omega_{k_\flat}\)), with the same datum \(V_k\); outside \(X\) both are the history's.

*Standing:* `library/a3-derivative.md` Lemma 10.1, gated ADVANCE as a repaired conditional implication (`gates/a3-derivative-gate.md` Section 10), from P81, P82° (gated implication, `gates/p82-curved-gate.md`, given \(U_0\in\mathrm{Reg}\), open in row 103 (1)), (G1)-(G3), separatedness, and admission. **With the meet construction, (G1)-(G3) hold by Lemma MJ.** This is the gate's own visible repair, and here it needs no identification with the outline's joined sequence, because \(U^\circ_W\) is only an intermediate of the proof. What remains of row 103 (3) for this consumer is:
- **(SEP)** every sequence used (\(\mathcal O^p,\mathcal O^h,\mathcal L_X\mathcal O^p=\mathbf D_{pX},\mathcal L_X\mathcal O^h\) and the towers) is separated and block-aligned (Theorem 6(a), asserted by the outline);
- **(SEP-L)** the outline's localisations \(\mathcal L_X\mathcal O^p\), \(\mathcal L_X\mathcal O^h\) coincide with \(\mathcal O^p\), \(\mathcal O^h\), members and data, on \(X\) minus a collar of width \(\le C_c\mu\). This is the outline's own definition (SA 9786: the collar is the \(O(1)\) outermost layers of cubes of side \(\mu\xi_{j_a}\); the joined sequence "coincides with the given sequence well inside \(W\)"; the joined datum "equals \(\mathbf V\) on the old bonds").

Neither of these is the identification the gate left open. If the outline's \(\mathcal L_X\) is taken to be the meet (the gate's visible repair), then (SEP) for it also follows from Lemma MJ, given the towers' separation.

**I2, P81 at full strength,** for \(\mathbf D_{pX}\) and for \(\mathbf D(\mathcal L_X\mathcal O^h)\). It supplies:
- a unique regular critical orbit near the datum of \(S\);
- a holomorphic chart \(\Phi\) on the sup-norm polydisc of radius \(r_{\rm B}\) (local units) around that datum, with \(q\circ\Phi=\mathrm{id}\), Landau representative \(\Phi=(e^{i\eta\tau})^{u}\) (Theorem 3), and complex regularity: at every top, local complex curvature and \(\xi|\tau|\), \(\xi^2|\nabla\tau|\) are \(\le C_{\rm R}r_{\rm B}\);
- the Lagrange representation \(\nabla A(S)=Dq(S)^{\mathsf T}\lambda\).

*Standing:* `library/a1-balaban.md`, gated (row 91), given F0 (discharged by row 95, gated in row 99). Open: pointed-core admission (10.2), and complex regularity at full strength (`gates/a3-derivative-gate.md` Section 12 item 4). The multiplier is used only through \(\lambda_\Lambda=0\) and the pairing \(\lambda\cdot Dq\); both are free of normalisation, so M1 is not read.

**I3, Theorem 4 at the real critical reference \(S\),** for \(\mathbf D_{pX}\) and for the reference problem, in the all-weights form (BGR11 row sums, Lemma 8.2). For a shell datum \(v\), the response \(h=\mathsf Hv\) obeys, at every top of the joined sequence,
\[\xi_y|h(y)|+\xi_y^2|\nabla h(y)|\le C_4\|v\|_\infty\,e^{-\theta d_{\mathbf B'}(y,\operatorname{supp}v)}\]
(\(\mathbf B'\) the joined metric). *Standing:* `library/a3-derivative.md` Theorem 4, first paragraph (real critical references), gated ADVANCE as repaired, from P81 and P82°. Only real critical references are used, so the independent-current and complex-reference paragraphs (M2, item 3 of the gate) are not read.

**I4, Proposition 2.4** (Balaban CMP 122 Proposition 1; SA 17656-17662; cited-pending, not in hand). \(V_\Lambda\) is the unique critical orbit of \(f(V)=A(U_{k,X}(V))\) and its minimum in the mild class. \(|\partial S_p-\mathbf1|\le C(M)\varepsilon_k\eta^2\) on the plaquettes of \(\Lambda\) and of an \(O(1)\) neighbourhood. In axial gauge the Hessian is \(\ge c(M)>0\).

**I5, (D-F) and the profile bound.** On the support of the tests, the data of \(\mathcal O^p\), \(\mathcal O^h\), their localisations and \(\mathbf D_{pX}\) are \(\varepsilon_1\)-regular, with
\[\varepsilon_1:=4L^2C_F\check R^2\varepsilon_k\]
(the old-core datum at \(C_F\check R_l^2\varepsilon_l\), the shells at \(\delta'+C(M)\varepsilon_k\), the new box at \((C(M)+4M_0)\varepsilon_k\), all \(\le\varepsilon_1\) by 2.2(d2)). Every background involved has local curvature \(a(y)\le C_{\rm P}\varepsilon_1\) at every top. *Standing:* (D-F) gated for every case (rows 88, 94, 96, 97), given Proposition 2.4 and premises H1-H4. The curvature bound is (1b) Theorem 2, first half (`library/a3-profile.md`, gated row 86), given P81 and P82.

**GEO, geometry asserted by the outline** (Proposition 2.3, catalogue C2; not checked here):
- GEO1: \(\operatorname{dist}(\Lambda,X^c)\ge2M\check R-M\). By SA 17576-17580, \(\Omega_k^c\cap X=H_k^{[8]}\) and \(X=X\cap Z_k=H_k^{[10]}\) (pushed out by 8 and 10 level-\(k\) cells of side \(M\check R\)). The nest boxes lie in \(\Omega_l^c\cap X\) (SA 17421), and \(\Lambda\) is \(Z''_k\) plus one layer of \(M\)-cubes (SA 17598). With \(\chi\) as in Section 1 and \(\check R\ge4+4C_c\mu/M\) this gives \(d(\operatorname{supp}\chi,X^c)\ge\tfrac34M\check R\) and \(d(\Lambda,\operatorname{supp}(1-\chi))\ge M\check R\), measured in level-\(k\) units. In \(X\setminus\Lambda\) every sequence is at level \(k\), and everywhere \(d_{\mathbf B}\ge\) the Euclidean distance. Write \(c_0:=\tfrac12\) for the common lower bound \(c_0M\check R\) used below.
- GEO2: \(X\) has at most \(n_X^4\) cells of level \(k\) (SA 17583).
- GEO3: the core has side \(\le C_nM\check R\,\xi_{k_\flat}\) (SA 17598). The nest box bounding the shells of levels \(<l\) has side \(\le C_nM(\check RL^{k_\flat-l}+L)\,\xi_l\). The shell of level \(j\) has width \(\ge M\xi_j\), so it costs \(\ge M\) to cross in \(d_{\mathbf B}\), and it has at most \((C_nM(\check RL^{k_\flat-j}+L))^4\) tops. The level-\(k_\flat\) shell contains the collar of W3 (\(M\ge C_c\mu\)). \(\Lambda\) has side \(\le C_\Lambda M\).
- GEO4 (gaps): every sequence used, joined sequences included, has \(\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})\ge c_g\xi_j\) for all \(j\). Here \(c_g\ge M\) on label and prepared layers and \(c_g\ge\rho\) on tower layers, with \(64\log L\le\theta\min(M,\rho)\).
- GEO5 (profiles, SA 6331-6336: supplied data, so this is a premise on that data). For a region \(\Lambda_i\) of level \(i\):
  - (a) \(\varphi[\Lambda_i](p)\) depends only on \(\Lambda_i\cap B(p,w_i)\), with \(w_i:=C_pM\check R_i\xi_i\) and \(C_p\le\tfrac34\);
  - (b) it is \(0\) off \(\Lambda_i\) and \(1\) at points farther than \(w_i\) from \(\Lambda_i^c\);
  - (c) at every plaquette \(p\) carried by the top \(y\) of the determining sequence, \(\#\{i\le k:\varphi[\Lambda_i](p)<1\}\le d_0(1+\check R)(1+k-j(y))\). Action levels can be finer than determining ones inside marks (SA 17432-17446); the factor \(1+\check R\) allows for one window.

  Since \(\check R_i\le L^{k-i}\check R_k\) (SA 17584), \(w_i\le\tfrac34M\check R\) for every \(i\le k\).
- GEO6: for \(i\le k_\flat\), \(X\cap\Lambda_i^c\) lies in \(C\) together with the layer \(\Omega_i\setminus\Lambda_i\) next to it, inside the level-\(k_\flat\) shell, so within \(\Lambda\). This follows from \(Z_i\subset Z_{k_\flat}\) (\(\Omega\)'s decrease), \(C=X\cap Z_{k_\flat}\), and \(\Omega_{j+1}\subset\Lambda_j^{\sim-1}\) (SA 17406).
- EXT: the localisations \(\mathbf D_{pX}\) and \(\mathbf D(\mathcal L_X\mathcal O^h)\) have the same domain, the same rows outside \(\Lambda\) (the level-\(k\) rows of \(X\setminus\Lambda\) and the same collar tower), and the same data there: the lift of the same exterior field (SA 9776-9786; `sa-2.8.md` Section 2 table).

**FLOW** (Theorem 2.1 hypotheses, `sa-2.8.md` Section 4): \(|b_i|\le B_*\); \(\min_{i\le k}x_i\ge x_k-c_5\) (R19). Hence \(\check R\ge\tfrac12\ell^r\) for \(x\ge2c_5\), and \(\mathsf N=\check R\).

## 4. Lemmas proved here

Throughout, \(\|\cdot\|\) on \(2\times2\) matrices is the operator norm. For \(G\in\mathrm{SU}(2)\) with eigenvalues \(e^{\pm i\vartheta}\), \(a(G)=1-\tfrac12\operatorname{tr}G=1-\cos\vartheta=\tfrac12\|1-G\|^2\). Each bare plaquette is assigned to the top of the finest pillar among its corners. A top \(y\) then carries at most \(6(\xi_y/\eta)^4\) plaquettes (its pillar has \((\xi_y/\eta)^4\) sites, each the lower corner of six plaquettes).

**Lemma W (weights).** Assume GEO1, GEO3, GEO5, GEO6, FLOW, and \(L^{n_{\rm c}-1}>4C_p\check R\). Then:
1. \(v=x\) on \(\operatorname{supp}\chi\), so \(R_4=0\);
2. \(v=w\) at every plaquette farther than \(\tfrac34M\check R\) from \(\Lambda\), so \((v-w)(1-\chi)\equiv0\) and \(R_2=0\);
3. \(|w-x|\le B_*\mathsf N\) on \(\operatorname{supp}\phi\);
4. \(v(p)\le x+B_*d_0(1+\check R)(1+k-j(y))\) at every plaquette carried by the top \(y\).

*Proof.*
1. Let \(p\in\operatorname{supp}\chi\). The healed action regions are \(\Lambda_i\cup X\supset X\) for every \(i\le k\) (SA 17402), and \(d(p,X^c)\ge\tfrac34M\check R\ge w_i\). By GEO5(b), \(\varphi[\Lambda_i\cup X](p)=1\) for all \(i\le k\), so \(v(p)=\beta-\sum_{i\le k}b_i=x\).
2. The healed and prepared action regions differ only inside \(\Lambda\). For \(k_\flat<i\le k\), \((\Lambda_i\cup X)\setminus\Lambda_i^{(\mathsf N)}=Z''_i\cap X\subset\Lambda\) (SA 17630-17636). For \(i\le k_\flat\), \(\Lambda_i^{(\mathsf N)}=\Lambda_i\) and \((\Lambda_i\cup X)\setminus\Lambda_i=X\cap\Lambda_i^c\subset\Lambda\) (GEO6). By GEO5(a), at a plaquette farther than \(w_i\) from \(\Lambda\) the two profiles of level \(i\) read the same region, so they are equal. Since \(\max_iw_i\le\tfrac34M\check R\), \(v=w\) there. By GEO1, \(\operatorname{supp}(1-\chi)\) is at distance \(\ge M\check R\) from \(\Lambda\).
3. Let \(p\in\operatorname{supp}\phi\subset X\setminus Z^\natural\). Then \(w(p)-x=\sum_{i\le k}b_i(1-\varphi[\Lambda_i^{(\mathsf N)}](p))\). Levels \(k_\flat<i\le k\) contribute at most \(B_*\) each, \(\mathsf N\) of them. For \(i\le k_\flat\), the complement of \(\Lambda_i\) inside \(X\) lies in \(C\) and the layer next to it, which sits inside the level-\(k_\flat\) shell (GEO6). Now \(p\) lies beyond the margin shells of levels \(k_\flat+1,\dots,k_\flat+n_{\rm c}-1\), so its distance to that set is \(\ge M\xi_{k_\flat+n_{\rm c}-1}=ML^{n_{\rm c}-1-\mathsf N}\) (GEO3). Its distance to \(X^c\) is \(\ge\tfrac34M\check R\ge w_i\). On the other hand \(w_i\le C_pM\check R_{k_\flat}\xi_{k_\flat}\le2C_pM\check RL^{-\mathsf N}\), using \(\check R_i\xi_i\le\check R_{k_\flat}\xi_{k_\flat}\) (SA 17584) and \(\check R_{k_\flat}\le2\check R\) (FLOW, \(x_{k_\flat}\le x+B_*\mathsf N\), \(x\) large). With \(L^{n_{\rm c}-1}>4C_p\check R\) these levels contribute nothing.
4. \(v(p)=x+\sum_ib_i(1-\varphi_i(p))\) with \(0\le1-\varphi_i\le1\) and \(|b_i|\le B_*\). Count by GEO5(c). \(\square\)

**Lemma MJ (meet localisation).** Let \(\Omega=(\Omega_q)\) be a separated sequence: gaps \(\operatorname{dist}_\infty(\Omega_q^c,\Omega_{q+1})\ge c_g\xi_q\), members unions of level-\(q\) blocks. Let \(\mathcal T=(\mathcal T_q)\) be the tower of a \(\mu\)-collared region \(W\) whose collars lie in single layers of \(\Omega\), with \(\mathcal T_0=W\supset\mathcal T_1\supset\cdots\), members unions of blocks of the same lattices, and gaps \(\ge\rho\xi_q\) (Theorem 6(a) for towers). Put \(\Omega'_q:=\Omega_q\cap\mathcal T_q\). Then:
1. \(\Omega'_0=\Omega_0\cap W\), \(\Omega'_q\subset\Omega_q\), and each \(\Omega'_q\) is a union of level-\(q\) blocks. These are (G1) and (G2).
2. \(\operatorname{dist}_\infty((\Omega'_q)^c,\Omega'_{q+1})\ge\min(c_g,\rho)\,\xi_q\): the meet is separated, and (G3) follows.
3. If a second separated sequence \(\widetilde\Omega\) has \(\widetilde\Omega_q\cap W=\Omega_q\cap W\) for all \(q\), with the same data on the rows inside \(W\), then its meet with \(\mathcal T\) is the same sequence with the same joined datum.

*Proof.*
1. \(\mathcal T_0=W\), and an intersection of block unions on one lattice is a block union.
2. \((\Omega'_q)^c=\Omega_q^c\cup\mathcal T_q^c\) and \(\Omega'_{q+1}\subset\Omega_{q+1}\cap\mathcal T_{q+1}\). The distance from a union is the minimum of the distances, and each one is bounded below by the gap of its own sequence.
3. \(\mathcal T_q\subset W\), so \(\widetilde\Omega_q\cap\mathcal T_q=\Omega_q\cap\mathcal T_q\). The rows are determined by the members. Old rows lie in \(W\), where the data agree. New collar rows carry the lift of the data of old rows of the collar layer, which also lie in \(W\). \(\square\)

So Lemma 10.1, applied with the meet, needs no premise about how the outline itself builds its joined sequences. Only (SEP) and (SEP-L) are read.

**Lemma SC (action comparison from I1).** Let \((U,U',W)\) satisfy I1 with amplitude \(E\le1\). Let \(a(y)\le1\) bound the local curvature of \(U^\circ_W\): \(\|1-\partial U^\circ_{W,p}\|\le a(y)(\eta/\xi_y)^2\) for \(p\) over \(y\). Then for every weight \(\varpi\ge0\), at every top \(y\) of the joined sequence away from the collars,

\[
 \sum_{p\text{ over }y}\varpi(p)\,|a_p(U)-a_p(U')|
 \le C_{\rm SC}\,\bar\varpi(y)\,\big(a(y)+Ee^{-\theta d_y}\big)Ee^{-\theta d_y},
 \qquad d_y:=d_{\mathbf B}(y,W^c),
\tag{4.1}
\]

where \(\bar\varpi(y)=\max_{p\text{ over }y}\varpi(p)\) and \(C_{\rm SC}\) is absolute.

*Proof.*
- **Gauge.** \(a_p\) is invariant under the gauge transformations \(w,w'\), so it suffices to compare \(e^{i\eta f}U^\circ\) with \(U^\circ\) at \(p\). Let \(G,H\) be their holonomies at \(p\), in the common base-point gauge.
- **Holonomy difference.** By the conversion of `gates/a3-derivative-gate.md` (consumer check), the four inserted exponentials give a linear term \(\eta^2df\), a remainder \(\le C\eta^2|f|^2\), and a curl conversion \(\le C\eta|f|\,\|1-H\|\). That computation is local to \(p\), and each of the three terms is bounded by (I1) at \(y\):
\[\eta^2|\nabla f|\le(\eta/\xi_y)^2Ee^{-\theta d_y},\qquad \eta^2|f|^2\le(\eta/\xi_y)^2E^2e^{-2\theta d_y},\qquad \eta|f|\,\|1-H\|\le(\eta/\xi_y)^3a(y)Ee^{-\theta d_y}.\]
So \(\|G-H\|\le3C(\eta/\xi_y)^2Ee^{-\theta d_y}\), and \(\|1-G\|\le\|1-H\|+\|G-H\|\).
- **Scalar step.** By \(a=\tfrac12\|1-\cdot\|^2\) and the reverse triangle inequality,
\[|a(G)-a(H)|\le\tfrac12(\|1-G\|+\|1-H\|)\|G-H\|\le\tfrac32C(2a(y)+3CEe^{-\theta d_y})(\eta/\xi_y)^4Ee^{-\theta d_y}.\]
- **Sum.** Multiply by \(6(\xi_y/\eta)^4\) plaquettes, apply the bound to \((U,U^\circ)\) and \((U',U^\circ)\), and add. \(\square\)

*Relation to (L).* For the pair \((P,P_X)\) and one plaquette of the common level-\(k\) layer, (4.1) with \(\varpi=1\) is the gate's (L1). The gate then absorbs the amplitude \(E\) into half the distance decay to get (L) with \(m=\theta/2\) (`gates/a3-derivative-gate.md`, consumer check). Here \(E\) is kept explicit and the bound is summed over tops instead, which also covers the finer layers and the other three pairs.

**Lemma BC (counting).** Let a sequence satisfy GEO4, let \(E\subset\Omega_k\) have Euclidean diameter \(\le D\) (level-\(k\) units), and let \(s\ge0\), \(\theta'\ge\theta/2\). Then

\[
 \sum_{\text{tops }y}(1+k-j(y))^s\,e^{-\theta'd_{\mathbf B}(y,E)}\le C_{\rm BC}(s)\,(D+4)^4,
\tag{4.2}
\]

with \(C_{\rm BC}\) depending on \(s,\theta,L\) only. Hence the same sum over \(\{d_{\mathbf B}(y,E)\ge R_0\}\), taken with \(e^{-\theta d}\), is \(\le e^{-\theta R_0/2}C_{\rm BC}(s)(D+4)^4\).

*Proof.*
1. **Layer crossings.** \(d_{\mathbf B}(y,E)\ge c_g(k-j(y)-1)_+\). A path from \(y\notin\Omega_{j(y)+1}\) to \(E\subset\Omega_k\) must, for each \(i=j(y)+1,\dots,k-1\), pass from its last point in \(\Omega_i^c\) to its first point in \(\Omega_{i+1}\). That stretch lies in \(\Omega_i\setminus\Omega_{i+1}\), has Euclidean length \(\ge\operatorname{dist}(\Omega_i^c,\Omega_{i+1})\ge c_g\xi_i\), and carries weight \(\xi_i^{-1}\) in \(d_{\mathbf B}\) (SA 9602). The stretches for different \(i\) are disjoint.
2. **Euclidean bound.** \(d_{\mathbf B}(y,E)\ge|y-E|\), since every weight in \(d_{\mathbf B}\) is \(\ge\xi_k^{-1}=1\).
3. **Count.** Tops of level \(j\) are sites of a lattice of spacing \(\xi_j=L^{j-k}\), so at most \(16(D+2n+4)^4L^{4(k-j)}\) of them have \(n\le|y-E|<n+1\).
4. **Sum.** Split \(e^{-\theta'd}\le e^{-\theta'c_g(k-j-1)_+/2}e^{-\theta'|y-E|/2}\). The sum is at most
\[16\sum_{m\ge0}(1+m)^sL^{4m}e^{-\theta'c_g(m-1)_+/2}\ \sum_{n\ge0}(D+4)^4(1+2n)^4e^{-\theta'n/2}.\]
By GEO4, \(\theta'c_g/2\ge\theta c_g/4\ge16\log L\), so the \(m\)-series is \(\le C(s,L)\). The \(n\)-series is \(\le c(\theta)(D+4)^4\). \(\square\)

**Lemma BC2 (core sum).** The tops of \(C\) have levels \(\le k_\flat\), and every path from them to the level-\(k_\flat\) shell \(E_\flat\) stays in \(C\cup E_\flat\). Then

\[
 \sum_{\text{tops }y\subset C}\xi_y^2e^{-\theta d_{\mathbf B}(y,E_\flat)}\le3L^2\operatorname{vol}(C)\,\xi_{k_\flat}^{-2}.
\]

*Proof.* As in step 1 of BC, \(d\ge c_g(k_\flat-j-1)_+\). There are at most \(\operatorname{vol}(C)\xi_j^{-4}\) tops of level \(j\), because pillars partition. Hence the sum is
\[\le\operatorname{vol}(C)\xi_{k_\flat}^{-2}\sum_{m\ge0}L^{2m}e^{-\theta c_g(m-1)_+}\le\operatorname{vol}(C)\xi_{k_\flat}^{-2}(1+L^2+1),\]
since \(L^2e^{-\theta c_g}\le L^{-62}\). \(\square\)

**Lemma LM (multiplier form; \(T(0)=S\)).** Assume I2, I4, EXT.
1. \(\nabla A(S)=Dq_{\rm ext}(S)^{\mathsf T}\lambda_{\rm ext}\) on the common localised domain. Here \(q_{\rm ext}\) collects the rows outside \(\Lambda\), collar rows included.
2. \(S\) is critical for \(\mathbf D_{pX}\) with its own datum, and \(T(0)=S\) modulo \(\mathcal G^{\rm res}(\mathbf D_{pX})\).
3. \(q_{\rm ext}(\widetilde T(u))=q_{\rm ext}(S)\) on the chart. Hence \(DA(1,S)[\eta\mathsf Hv]=0\) for every shell datum \(v\).

*Proof.*
1. By I2, \(\nabla A(S)=Dq(S)^{\mathsf T}\lambda\) with \(q=(q_{\rm ext},q_\Lambda)\), where \(q_\Lambda\) collects the level-\(k\) rows with an end point in \(\Lambda\), the variables of \(f\) (SA 17660). From \(q\circ\Phi=\mathrm{id}\) we get \(Dq\,D\Phi=\mathrm{id}\). For a datum tangent \(\delta\) on the \(\Lambda\)-rows, criticality of \(V_\Lambda\) (I4) gives
\[0=Df(V_\Lambda)[\delta]=DA(S)[D\Phi(0,\delta)]=\lambda\cdot Dq\,D\Phi(0,\delta)=\lambda_\Lambda\cdot\delta.\]
So \(\lambda_\Lambda=0\).
2. By EXT, the rows of \(\mathbf D_{pX}\) outside \(\Lambda\) are the \(q_{\rm ext}\) rows with the same data, and the other rows lie in \(\Lambda\). A tangent \(h\) to the constraint set of \(\mathbf D_{pX}\) at \(S\) therefore has \(Dq_{\rm ext}(S)h=0\), and \(DA(S)h=\lambda_{\rm ext}\cdot Dq_{\rm ext}(S)h=0\). \(S\) is regular for \(\mathbf D_{pX}\): at a top \(y\), \(\|1-\partial S_p\|\le C(M)\varepsilon_k\eta^2\le C(M)\varepsilon_k(\eta/\xi_y)^2\) (I4), and its datum is regular by the converse of Theorem 1. By the uniqueness in I2 for \(\mathbf D_{pX}\), \(T(0)=S\) modulo \(\mathcal G^{\rm res}\).
3. \(\widetilde T(u)=\Phi_{pX}(e^{iu}\cdot M_{\mathbf D_{pX}}S)\) changes only shell rows, which lie in \(\Lambda\), so \(q_{\rm ext}\) is constant. Differentiate at \(u=0\) and pair with \(\lambda_{\rm ext}\), using item 1. \(\square\)

**Lemma TQ (Cauchy bounds on the prepared chart).** Assume I2 with \(C_{\rm R}r_{\rm B}\le\tfrac12\). Let \(u_0,v\) be real with \(\|u_0\|_\infty\le r_{\rm B}/4\) and \(\|v\|_\infty\le1\), and let \(K_\phi\) be the number of tops of \(\mathbf D_{pX}\) carrying plaquettes of \(\operatorname{supp}\phi\). Then:
1. \(|D^3\widetilde F(u_0)[v,v,v]|\le1152\,C_{\rm R}^2K_\phi/r_{\rm B}\);
2. at every top, with \(\tau''=D^2\tau(0)[v,v]\), \(\xi_y|\tau''(y)|+\xi_y^2|\nabla\tau''(y)|\le16C_{\rm R}/r_{\rm B}\).

*Proof.*
1. For \(|z|<r_{\rm B}/2\), the datum \(u_0+zv\) lies within \(3r_{\rm B}/4\) of the real datum of \(S\). By I2, every plaquette over \(y\) has \(\|1-\partial\Phi(u_0+zv)_p\|\le C_{\rm R}r_{\rm B}(\eta/\xi_y)^2\le\tfrac12\). For \(G\in\mathrm{SL}(2,\mathbb C)\) put \(Y=1-G\). Then \(1=\det G=1-\operatorname{tr}Y+\det Y\), so \(\operatorname{tr}Y=\det Y\), and \(|a(G)|=\tfrac12|\det Y|\le\tfrac12\|Y\|^2\). Hence \(A_y(z):=\sum_{p\text{ over }y}\phi(p)a_p(\Phi(u_0+zv))\) is holomorphic, with \(|A_y|\le6(\xi_y/\eta)^4\cdot\tfrac12C_{\rm R}^2r_{\rm B}^2(\eta/\xi_y)^4=3C_{\rm R}^2r_{\rm B}^2\). Cauchy's inequality on \(|z|=r_{\rm B}/4\) gives \(|A_y'''(0)|\le6\cdot3C_{\rm R}^2r_{\rm B}^2(4/r_{\rm B})^3\). Sum over \(y\).
2. \(z\mapsto\tau(zv)(y)\) is holomorphic for \(|z|<r_{\rm B}\), with \(\xi_y|\tau|\) and \(\xi_y^2|\nabla\tau|\le C_{\rm R}r_{\rm B}\) (I2). Use Cauchy's inequality at radius \(r_{\rm B}/2\). \(\square\)

## 5. The ten terms, bounded

**Shorthand.** \(\varepsilon_1=4L^2C_F\check R^2\varepsilon_k\) (I5), \(E=C_\mu\varepsilon_1\), \(a(y)\le C_{\rm P}\varepsilon_1\), with the coupling small enough that \(C_{\rm P}\varepsilon_1,E\le1\). Since \(x\varepsilon_k^2=p_0(g)^2\),

\[
 \Pi:=x(C_{\rm P}\varepsilon_1+E)E\le C_\Pi\,\check R^4p_0(g)^2,\qquad C_\Pi:=32L^4C_F^2C_\mu\max(C_{\rm P},C_\mu).
\]

\(K_X:=(n_XM\check R)^4+16C_n^4M^4(\check R^4+\mathsf NL^4)\) bounds the number of tops of any sequence used that carry plaquettes of \(\operatorname{supp}\chi\setminus Z^\natural\) (GEO2, GEO3). \(\|B\|_\infty\le\delta'/g=A_1p_1(g)\). \(C'_{\rm c}\) is the curl-conversion constant: \(|(d_S\eta h)_p|\le C'_{\rm c}(\eta/\xi_y)^2(\xi_y^2|\nabla h|+\xi_y|h|a(y))\).

**5.1** \(R_2=R_4=0\) (Lemma W, items 1-2).

**5.2** \(R_3\): I1-W2, \(\varpi=x\chi\). The tops of \(\mathcal O^h\) under \(\operatorname{supp}\chi\) are level-\(k\) tops of \(X\), at most \((n_XM\check R)^4\) of them, each with \(d_y=d_{\mathbf B}(y,(X^-)^c)\ge\tfrac34M\check R-\tfrac14M\check R=\tfrac12M\check R\) (GEO1). By (4.1),
\[|R_3|\le C_{\rm SC}\,\Pi\,(n_XM\check R)^4e^{-\frac12\theta M\check R}.\]

**5.3** \(R_6\): I1-W1, \(\varpi=x\phi\), at most \(K_X\) tops, \(d_y\ge\tfrac12M\check R\):
\[|R_6|\le C_{\rm SC}\,\Pi\,K_Xe^{-\frac12\theta M\check R}.\]

**5.4** \(R_7\): I1-W3, \(\varpi=x\phi\). For \(y\) under \(\operatorname{supp}\phi\), \(d_{\mathbf B}(y,W_3^c)\ge\min\{Mn_{\rm c},\tfrac34M\check R\}=Mn_{\rm c}\): reaching \(C\) means crossing the \(n_{\rm c}\) margin shells, each costing \(\ge M\) (GEO3). So
\[|R_7|\le C_{\rm SC}\,\Pi\,K_Xe^{-\theta Mn_{\rm c}}.\]

**5.5** \(R_1\): I1-W4, \(\varpi=v(1-\chi)\le x(1+B_*d_0)(1+\check R)(1+k-j(y))\) (Lemma W, item 4, with \(x\ge1\)). Every top under \(\operatorname{supp}(1-\chi)\) has \(d_y=d_{\mathbf B}(y,\Lambda)\ge M\check R\) (GEO1). Its nearest points in \(\Lambda\) lie in the level-\(k\) outer shell \(E_k\subset\Omega_k\), of diameter \(\le2C_\Lambda M\). The data are \(\varepsilon_1\)-regular at every level (I5 with 2.2(d2)), so (4.1) holds at every top. Summing with Lemma BC (\(s=1\), \(R_0=M\check R\)):
\[|R_1|\le C_{\rm SC}\,\Pi\,(1+B_*d_0)(1+\check R)\,C_{\rm BC}(1)(2C_\Lambda M+4)^4e^{-\theta M\check R/2}.\]
This is the only global sum. It is uniform in the torus, in the depth, and in the other components' state.

**5.6** \(R_5\): \(|w-x|\le B_*\mathsf N\) on \(\operatorname{supp}\phi\) (Lemma W, item 3). Over a top, \(\sum_pa_p(P)\le6(\xi/\eta)^4\cdot\tfrac12(C_{\rm P}\varepsilon_1)^2(\eta/\xi)^4\). So
\[|R_5|\le3B_*\mathsf N\,C_{\rm P}^2\varepsilon_1^2K_X.\]

**5.7** \(R_8\): \(t\mapsto\widetilde F(tgB)\) is real and \(C^3\) on \([0,1]\), since \(\|tgB\|_\infty\le\delta'\le r_{\rm B}/4\). Taylor's formula with Lagrange remainder gives \(R_8=-\tfrac x6D^3\widetilde F(t_*gB)[gB,gB,gB]\) for some \(t_*\in(0,1)\). Trilinearity, \(xg^3=g\) and Lemma TQ item 1 give
\[|R_8|\le192\,C_{\rm R}^2\,g\,(A_1p_1)^3K_X/r_{\rm B}.\]

**5.8** \(R_9\). By Lemma LM item 2, \(A(\phi,S)=F(0)\).
- **Second derivative.** In Landau form \(\widetilde T(u)=(e^{i\eta\tau(u)}S)^{w(u)}\), with \(\tau(0)=0\) and \(D\tau(0)=\mathsf H\); the gauge \(w(u)\) drops out of \(a_p\). Differentiating twice along \(t\mapsto\eta\tau(tB)\),
\[D^2\widetilde F(0)[B,B]=\sum_p\phi(p)\big\{D^2a_p(S)[\eta\mathsf HB,\eta\mathsf HB]+Da_p(S)[\eta\tau'']\big\},\qquad \tau''=D^2\tau(0)[B,B].\]
- **Expansion of \(a_p\).** Write \(\partial(e^{itA}S)_p=\partial S_p\exp(itX_1+t^2X_2+O(t^3))\), where \(X_1=(d_SA)_p\) is the transported sum (\(|X_1|\le4|A|_p\)) and \(X_2\) is the BCH commutator term (traceless, \(|X_2|\le8|A|_p^2\)). Then
\[\tfrac{d^2}{dt^2}a_p\big|_0=\tfrac12\operatorname{tr}X_1^2-\tfrac12\operatorname{tr}\big((\partial S_p-1)(2X_2-X_1^2)\big).\]
So \(D^2a_p(S)[A,A]=|(d_SA)_p|^2+\kappa_p\), with \(|\kappa_p|\le32\|1-\partial S_p\|\,|A|_p^2\) (using \(|\operatorname{tr}MN|\le2\|M\|\|N\|\)). Similarly \(|Da_p(S)[A]|\le\|1-\partial S_p\|\,|(d_SA)_p|\). Hence \(\tfrac12D^2\widetilde F(0)[B,B]=Q(B)+\tfrac12K_1+\tfrac12K_2\), with \(K_1=\sum\phi\kappa_p(\eta\mathsf HB)\) and \(K_2=\sum\phi Da_p(S)[\eta\tau'']\). Since \(xg^2=1\),
\[R_9=-xDF(0)[B]-\tfrac12K_1-\tfrac12K_2.\]
- **The linear term (2.1).** By Lemma LM item 3, \(xDF(0)[B]=-g^{-1}\{DA(\psi,S)[\eta\mathsf HB]+DA(1-\chi,S)[\eta\mathsf HB]\}\). Over a top \(y\), by I3 and the curl conversion, \(\sum_p|Da_p(S)[\eta\mathsf HB]|\le12C'_{\rm c}C_4\,a_S(y)\|B\|_\infty e^{-\theta d(y,\text{shells})}\).
  - *(9a), the \(\psi\) part.* On \(Z^\natural\), \(a_S(y)=C(M)\varepsilon_k\xi_y^2\) (I4). The margin tops give, by GEO3,
\[\sum_{j=k_\flat}^{k_\flat+n_{\rm c}-1}(C_nM(\check RL^{k_\flat-j}+L))^4\xi_j^2\le16C_n^4M^4(\check R^4L^{-2\mathsf N}+L^2L^{-2(\mathsf N-n_{\rm c})}).\]
The core tops give \(\le3L^2(C_nM\check R)^4L^{-2\mathsf N}\) by BC2. Together they give \(\Sigma_\psi:=20C_n^4M^4\check R^4L^2L^{-2(\mathsf N-n_{\rm c})}\). Since \(g^{-1}\varepsilon_k\|B\|\le p_0A_1p_1\),
\[\text{(9a)}\le12C'_{\rm c}C_4C(M)\,p_0A_1p_1\,\Sigma_\psi.\]
  - *(9b), the \((1-\chi)\) part.* The tops of the common localised domain outside \(\operatorname{supp}\chi\), the collar tower of \(X\) included, have \(a_S\le C_{\rm P}\varepsilon_1\) and \(d\ge d_{\mathbf B'}(y,E_k)\ge M\check R\). Lemma BC, applied to the joined sequence, gives
\[\text{(9b)}\le48C'_{\rm c}C_4C_{\rm P}L^2C_F\check R^2p_0A_1p_1\,C_{\rm BC}(0)(2C_\Lambda M+4)^4e^{-\theta M\check R/2}.\]
- **The Hessian discrepancy.** \(|K_1|\le\sum_y6(\xi/\eta)^4\cdot32a_S(\eta/\xi)^2\cdot(\eta/\xi)^2(\xi|h|)^2\le192C_{\rm P}\varepsilon_1C_4^2(A_1p_1)^2K_X\). By Lemma TQ item 2, \(|K_2|\le96C'_{\rm c}C_{\rm P}\varepsilon_1C_{\rm R}(A_1p_1)^2K_X/r_{\rm B}\). Neither needs decay: the current of \(S\) is \(O(\varepsilon_1)\) and \(\operatorname{supp}\phi\) carries polylogarithmically many tops.

So \(|R_9|\le\text{(9a)}+\text{(9b)}+\tfrac12|K_1|+\tfrac12|K_2|\).

**5.9** \(R_{10}\): \(Z^\natural\) has side \(\le C_nM(\check R+L)L^{n_{\rm c}-\mathsf N}\) (GEO3), so \(\operatorname{vol}(Z^\natural)\le(C_nM(\check R+L))^4L^{-4(\mathsf N-n_{\rm c})}\). Then
\[0\le R_{10}=x\sum_{p\in Z^\natural}\tfrac12\|1-\partial S_p\|^2\le3C(M)^2p_0^2\operatorname{vol}(Z^\natural)\le3C(M)^2C_n^4M^4(\check R+L)^4p_0^2L^{-4(\mathsf N-n_{\rm c})}.\]

## 6. Theorem and order of constants

**Theorem 2.8-T (implication).** Assume I1 (W1-W4), I2, I3, I4, I5, GEO1-GEO6, EXT and FLOW, with the cutoffs of Section 1. Let \(X\) be a component of the class, at a real point of the tests of (1)-(3) of the operation and of the reference cutoff, in any frame. Then \(|\mathsf R_X|\le\sum_{a}(\text{5.1-5.9})\). Write \(\ell=\log x_k\), \(\check R\ge\tfrac12\ell^r\), \(n_{\rm c}\ge\tfrac12\check R-1\), \(p_0=A_0\ell^{\mathfrak p_0}\), \(p_1=\ell^{\mathfrak p_1}\). Then

\[
 |\mathsf R_X|\le C_*(1+\ell)^{K_*}\big(e^{-\theta M\ell^r/4}+L^{-\ell^r/2}+e^{-\ell/2}\big),\qquad K_*=9r+2\mathfrak p_0+3\mathfrak p_1+4,
\tag{6.1}
\]

with \(C_*\) depending only on the constants fixed in steps 1-4 below. Since \(r\ge2\), the right side is \(\le C'_*g_k^{1/2}\) for \(g_k\) small, and it tends to 0 uniformly in the level, the depth, the torus, the history and the frame. The slowest pieces are \(R_8\) and \(K_1,K_2\), of order \(g\ell^{O(1)}\): "a positive power of \(g_k\)", as SA 17876 says. The localisation pieces \(R_1,R_3,R_6,R_7\) carry \(e^{-c\theta M\ell^r}\), the source's rate. The core pieces (9a) and \(R_{10}\) carry \(L^{-c\mathsf N}\).

*Proof.* Sum 5.1-5.9. Bound each polynomial factor by a power of \(1+\ell\), using \(\check R\le L\ell^r\), \(\mathsf N=\check R\), \(K_X\le C(1+\ell)^{4r+1}\), \(\varepsilon_1^2\le16L^4C_F^2\check R^4g^2p_0^2\). Each exponential factor is one of the three in (6.1): \(e^{-\theta Mn_{\rm c}}\le e^{\theta M}e^{-\theta M\ell^r/4}\), and \(L^{-2(\mathsf N-n_{\rm c})}\le L^{-\check R}\). \(\square\)

**Order of constants** (nothing is chosen after the coupling ceiling, and nothing depends on \(k\), \(\mathsf N\), the torus or the history):

1. \(L\); \(\delta_0\), with \(\theta=\delta_0/8\); \(\rho\); \(\mu=M'_1\); and the A3 package constants \(C_\mu,C_4,C_{\rm R},r_{\rm B},C_{\rm P},C'_{\rm c}\).
2. \(M\), subject to \(M\ge C_c\mu\) and \(64\log L\le\theta M\) (GEO3, GEO4). Then \(C(M),c(M),C_n,n_X,C_\Lambda,C_F,B_*,d_0\).
3. \(M_0\).
4. \(A_0,A_1,\mathfrak p_0,\mathfrak p_1,r\), as in the outline's (2e); only their being fixed is used.
5. The ceiling \(\gamma\). For \(g_k\le\gamma\), all of the following hold: \(C_{\rm P}\varepsilon_1,E\le1\); \(\varepsilon_1\le\mathsf a(L,\rho,\mu)\); \(\delta'\le r_{\rm B}/4\); \((C(M)+4M_0)\varepsilon_k\le\varepsilon_1\); \(L^{n_{\rm c}-1}>4C_p\check R\); \(\check R\ge4+4C_c\mu/M\); \(x_k\ge2c_5\); and (6.1) \(\le\epsilon\) for the prescribed \(\epsilon\).

## 7. Outside the ten terms: what the consumer's "numbers" contain

These items are not part of \(\mathsf R_X\). They concern \(\mathbf T'_k(X)\) (SA 17642), where the source writes "+numbers".

**(a) The denominator (D3).** \(\log\mathsf D_X=-xA(\chi,S)+\log Z_b(S)\), with
\[Z_b(S)=\int db\,\delta_{\rm ax}\chi(\Lambda)\,e^{-x[A(\chi,R(b))-A(\chi,S)]}.\]
\(Z_b(S)\) depends on the exterior field through \(S\), so it is not a number. Implication sketch, with these inputs:
1. *Linear term.* \(b\) moves only \(\Lambda\)-rows, so Lemma LM item 1 applies to the reference problem: \(xDA(\chi,S)[DR(0)b]=-g^{-1}DA(1-\chi,S)[DR(0)b]\), bounded like (9b) times \(\|b\|\le M_0p_0\).
2. *Cubic term.* \(\le Cg(M_0p_0)^3n_b/r_{\rm B}\) on the cutoff box \(\|gb\|<M_0\varepsilon_k\) (Lemma TQ for the level-\(k\) chart), with \(n_b\le12(C_\Lambda M)^4\).
3. *Hessian.* Let \(\mathfrak h_S\) be the \(b\)-Hessian and \(\mathfrak h_0\) its flat value, which is coercive with constant \(c(M)\) in \(\delta_{\rm ax}\) gauge (I4). If \(\|\mathfrak h_0^{-1/2}(\mathfrak h_S-\mathfrak h_0)\mathfrak h_0^{-1/2}\|\le\varepsilon_h\le\tfrac12\), then \((1-\varepsilon_h)\le\mathfrak h_0^{-1/2}\mathfrak h_S\mathfrak h_0^{-1/2}\le(1+\varepsilon_h)\). This is the two-sided argument of `qr-decide.md` (2.4): triangle inequality, then diagonalisation. It gives \(|\log\det(\mathfrak h_S\mathfrak h_0^{-1})|\le2n_b\varepsilon_h\).
4. *Tails.* The Gaussian tail outside the box is \(\le n_be^{-c(M)M_0^2p_0^2/2}\).

Together, \(\log Z_b(S)=\log Z_b^0+O(n_b\varepsilon_h)+o(1)\), where \(Z_b^0\) is the flat Gaussian normalisation (a number). **Not written out here:** the bound \(\varepsilon_h\le C(M)\varepsilon_1/(c(M)r_{\rm B})\). It would follow from Cauchy's inequality for the holomorphic dependence of \(\mathfrak h\) on the exterior datum, but that dependence and its sup bound are not stated in I2. Status: small, open, a consumer item.

**(b) The \(B\)-normalisation after the margin (D2).** \(Q\) is coercive only on the outer-shell variables. The inner-shell \(B\)'s (levels \(<k_\flat+n_{\rm c}\)) are integrated only against \(e^{-A(w\psi,P(B))}\) and the test \(\chi'\), so their Gaussian normalisation is no longer among the "numbers". The retained core operation of \(\mathbf T'_k(X)\) keeps its form: SA 17642 already writes \(-A(x''_k\phi_{\rm c},U''(e^{ig_kB},V''))\) with the \(B\)-dependence inside. Only the bookkeeping of which normalisations are numbers changes. Also, the source's factor \(L^{-\mathsf N_k}\) for the core term's complex continuation (SA 17886) becomes \(L^{-(\mathsf N_k-n_{\rm c})}\); this is not checked further.

## 8. Defects, consumer changes, open items

**Defects in the source's 2.8, ranked by what they break** (none breaks the conclusion after its repair):

- **D2, the core cutoff** (SA 17855, 17874). The cutoff is unspecified, and the literal core indicator contradicts the source's own distance clause. Scaling (unchecked) suggests \(R_7\sim-p_0^2\check R^3\) and an \(O(p_0)\) linear force on the innermost shell \(B\)'s (2.2(a)). *Repair:* \(\psi=\) the core plus \(n_{\rm c}=\lfloor\mathsf N/2\rfloor\) shells. It is checked against \(R_{10}\) (5.9), \(R_7\) (5.4), Lemma W, and the consumer (7(b)).
- **D1, the linear term** (SA 17866). "Vanishes" is false: it equals (2.1). *Repair:* the bounds (9a), (9b).
- **D3, the denominator** (SA 17642, "+numbers"). Its fluctuation factor depends on the field, by \(e^{O(n_b\varepsilon_h)}\) (Section 7(a)).
- **D4, \(H\) in \(Q\)** (SA 17642). Unspecified. Here \(\mathsf H:=D\widetilde T(0)\) at \(S\). With the flat \(H_0\) one more discrepancy appears: \(\le C\varepsilon_1\|B\|^2K_X\), by the same two-sided argument (`qr-decide.md` (2.4)) applied to \(d_S\mathsf H\) against \(dH_0\). It is small, but it needs the flat-to-curved response bound (row 98's perturbation) at \(S\).
- **D5, \(R_1\) is global.** It reads 6(c) for the complement of a box on the whole torus (W4) and a count of tops (Lemma BC). The source's interpolation paragraph (SA 17890-17910, amplitude \(Cg_k^{-1}e^{-cM\check R_k}\)) reads the same input.

**What changes for consumers.** \(\mathbf T'_k(X)\) keeps its form. \(\phi_{\rm c}\) must be read as \(\psi\) of Section 1, and the Gaussian \(Q\) as (1.2). The bound \(|\mathsf R_X|\le\) (6.1) replaces "tends to zero uniformly". The denominator and normalisation items of Section 7 go with "numbers".

**Open, hardest first:**
1. **I1's analytic core: P81 and P82° on the meet sequences of W1-W4,** together with (SEP). (SEP-L) is the outline's definition. Lemma MJ removes the (G1) identification for this consumer. The gate's item 1 concerns proving 6(c) for the outline's own localised background as \(U^\circ\); 2.8 never needs that. If P82° fails on one of these curved meet sequences (one global, two with a hole), the corresponding localisation term (\(R_1,R_3,R_6,R_7\)) has no bound. This is where 2.8 would fail if it fails.
2. **P81 at full strength for \(\mathbf D_{pX}\).** Complex regularity and a uniform chart radius on the shell data (Lemma TQ). Pointed-core admission (10.2) remains open.
3. **\(U_0\in\mathrm{Reg}\)** (row 103 (1)), for P82° at \(S\), which I3 reads.
4. **Proposition 2.4** (CMP 122 Proposition 1, not in hand), and (D-F)'s premises H1-H4.
5. **GEO1-GEO6, EXT** (catalogue C2). GEO5 is a condition on the supplied profile data (SA 6331-6336). GEO1 and GEO3 are read from SA 17576-17598.
6. **Section 7(a)** written out (\(\varepsilon_h\)).

**What moved.** Package C rank 2 (`route-decisions.md` 3.2 item 2) goes from "ten terms described, not displayed; stops at (L)" to "displayed; bounded as an implication; reduces to 6(c) on four named comparisons plus the outline's geometry". Reversal test 4.3, second bullet: as worded it cannot fire, and in its honest form it reduces to item 1 above. M1 and M2 are not read. Nothing here is waste for the next lane. For this consumer, row 103's item 3 narrows to (SEP) and (SEP-L): the (G1) identification is not read by 2.8.

**Method.** No numeric job was run (none was needed; memory was not tested). Source reads: SA 17398-17446, 17566-17662, 17840-17910, 9598-9604, 9734-9789, 6325-6365, 17330-17336. Library reads: `sa-2.8.md`, `route-decisions.md` 3-4, `sp-decide.md` 4-5, `qr-decide.md` 2-5 (Sections 3-5 there concern the retired (QR) tangent problem and are not used; only the two-sided argument of (2.4) is), `a3-derivative.md` 10, 12, `gates/a3-derivative-gate.md` 10-12, `floor-screen.md` 0-2, `gates/floor-screen-gate.md` 1-2. Same-model text; a gate by another provider is needed before any of it counts.
