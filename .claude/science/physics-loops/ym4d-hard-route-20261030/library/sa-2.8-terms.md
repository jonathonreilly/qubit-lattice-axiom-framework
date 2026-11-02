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
