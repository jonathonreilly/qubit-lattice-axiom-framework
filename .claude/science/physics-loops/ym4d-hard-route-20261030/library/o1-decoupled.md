lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T17:43Z

# o1-decoupled: R9's current-corrected lift and (O1), the removed-map comparison, hereditary admission of the inner Landau map (queue row 126)

Pinned at 533faafc0 (branch claude/ym4d-hard-route). Research-stage working state; no status, not an audit. Written section by section.

Moves: `sa-ledger.md` rank 4 (WF substitution room, SA L15879), where it stops after `gates/wf-room-2-gate.md` (§§0, 6.3, 7.3, 8).

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Same-provider work, ungated. It reads Claude text (`h-walk.md`, `a2-layers.md` §7, `wf-room-2.md`, `a3-clauses.md`) and Codex text (`wf-room.md`, and the gates of rows 92, 120, 125, which are Codex's). Outline: Sussman–Alpoge `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (sha256 `d7f77d4d…4d6f`, the same file as rows 103–125), not copied here; SA numbers are its lines. No numeric job was run. Every step is written by hand.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the operators \(\mathsf G_0,\mathsf G,\mathsf H\) and the current continuation \(\Delta'_\pi\) (SA 10142–10192), the decoupled response (R9) (SA 5762–5790, 10356–10415), mechanisms (f), (i), (j) (SA 10540, 10552, 10562), the window maps (WF1)–(WF7) and (OA7). T. Balaban for the method: random-walk expansions from local inverses on cut-down sequences (CMP 99b pp. 408–410), decoupling parameters paid by length with the leftover \(e^{16\bar\kappa}\) (CMP 116 p. 5, as the outline cites it), and the hereditary-domain argument of CMP 109. Claude for `h-walk.md`, `a2-layers.md`, `wf-room-2.md`; OpenAI Codex for `wf-room.md` and for the gate repairs used here.

## 0. Result

(Filled in at the end.)

## 1. Item (1) at \(s\equiv1\): the lift, and (O1) on the general pair domain

### 1.1 Identification of R9's lift

R9 (SA 10360–10366) uses \(H=\mathsf H\mathsf m^{-1}\) with (SA 10149–10156)
\[
 \mathsf G_0=(\Delta^{\rm W}_{\mathbf U}+DRD^{\mathsf T}+Q^{\mathsf T}aQ)^{-1},\qquad
 \mathsf G=(\mathsf G_0^{-1}-\Delta'_\pi[\mathbf J])^{-1},\qquad
 \mathsf H=\mathsf GQ^{\mathsf T}(Q\mathsf GQ^{\mathsf T})^{-1},
\]
all at the pair \(P=(\mathbf U,\mathbf J)\) of the step. The current in \(\Delta'_\pi\) is the **independent** \(\mathbf J\), not \(J(\mathbf U)\). \(\Delta'_\pi\) is the explicit continuation (SA 10175–10190). \(Q\) is the linear part per unit length of the straightened rows, \(\mathsf m\) multiplies row \(c\) by \(\xi_c\), and \(K_0:=\mathsf mQ\) is the derivative at \(A=0\) of the raw straightened rows. Kernels are taken in counting measure, \((HB')(b)=\sum_cH(b,c)B'(c)\).

**(I-a) Saddle characterisation.** Let \(q_{\mathsf G}\) be the bilinear form of \(\mathsf G^{-1}\) in the fine pairing, and put \(M_{\mathbf J}:=\Delta^{\rm W}_{\mathbf U}+DRD^{\mathsf T}-\Delta'_\pi[\mathbf J]\). Wherever \(\mathsf G\) and \((Q\mathsf GQ^{\mathsf T})^{-1}\) exist, \(\mathsf Hf\) is the unique \(A\) with \(QA=f\) and \(q_{\mathsf G}(A,A')=0\) for all \(A'\in\ker Q\). Equivalently, \((A,\mu)\) solves \(M_{\mathbf J}A-Q^{\mathsf T}\mu=0\), \(QA=f\) for some \(\mu\). So the row mass \(Q^{\mathsf T}aQ\) drops out, and \(K_0H=\mathsf mQ\mathsf H\mathsf m^{-1}=1\).

*Proof.* \(Q\mathsf Hf=f\) is immediate. \(\mathsf G^{-1}\mathsf Hf=Q^{\mathsf T}(Q\mathsf GQ^{\mathsf T})^{-1}f\in\operatorname{ran}Q^{\mathsf T}=(\ker Q)^\perp\), so \(q_{\mathsf G}(\mathsf Hf,\cdot)\) vanishes on \(\ker Q\). Then \(M_{\mathbf J}\mathsf Hf=Q^{\mathsf T}[(Q\mathsf GQ^{\mathsf T})^{-1}-a]f\), with \(\mu=[(Q\mathsf GQ^{\mathsf T})^{-1}-a]f\). For uniqueness, take a difference \(A_0\in\ker Q\) with \(q_{\mathsf G}(A_0,\cdot)=0\) on \(\ker Q\). Then \(\mathsf G^{-1}A_0=Q^{\mathsf T}\nu\) for some \(\nu\), so \(A_0=\mathsf GQ^{\mathsf T}\nu\) and \(0=QA_0=(Q\mathsf GQ^{\mathsf T})\nu\). Hence \(\nu=0\) and \(A_0=0\). The condition "\(q(A,\cdot)=0\) on \(\ker Q\)" does not change if a multiple of \(Q^{\mathsf T}aQ\) is added to the form, and it does not depend on the pairing used to turn forms into operators. \(\square\)

**(I-b) Block of the unfolded inverse.** At coefficient \(j=0\), `h-walk.md` Lemma U(c) gives \(\mathsf H=[\mathbb K^{-1}]_{A\nu}\) for \(\mathbb K=\mathbb K[S,P,0]\), whenever \(G',N,\mathsf G\) and \(W=Q\mathsf GQ^{\mathsf T}\) exist. Its eight-unknown elimination, with its transpose conventions and both Schur signs, is gated ADVANCE (`gates/h-walk-gate.md` §4). It reads exactly the outline's \(\mathsf G\) with \(\Delta'_\pi[\mathbf J]\) (the three terms of \(c_J(A,LA)\) are SA's continuation with equal arguments).

**(I-c) It is not the P82° lift (agreeing with the gate's Defect 1).** The P82° lift \(H^\circ\) solves the saddle system of (I-a) with \(M^\circ=d^{\mathsf T}d+DRD^{\mathsf T}\) (or \(\mathfrak d^{\mathsf T}\mathfrak d+DRD^{\mathsf T}\)) in place of \(M_{\mathbf J}\). Put \(E_{\mathbf J}=M_{\mathbf J}-M^\circ\). This is the curvature part of the Wilson Hessian minus \(\Delta'_\pi[\mathbf J]\). Let \(T^\circ\) be the field block of \(S^{\circ-1}\). Rewrite the \(\mathbf J\)-system as \(S^\circ(A,\mu)=(-E_{\mathbf J}A,f)\). Then \(A=-T^\circ E_{\mathbf J}A+H^\circ f\), so
\[
 H=(1+T^\circ E_{\mathbf J})^{-1}H^\circ
\]
wherever both sides exist. The two lifts differ at first order in \(E_{\mathbf J}\), already at \(s\equiv1\). The route below does not pass through P82°. It also needs no bound on \(E_{\mathbf J}\) in \(X_w\to F_w\), which would require the transpose of \(\lambda_A=G'RD^{\mathsf T}A\) (`a3-clauses.md` §4.3).

### 1.2 Theorem A: (O1) at \(s\equiv1\)

**Inputs.**
- [L] `h-walk.md` Lemma L, gated ADVANCE after the graph-norm repair (`gates/h-walk-gate.md` §5). It is conditional on (I1), the conjugation package of `a2-layers.md` §7 with the repairs of `gates/a2-layers-gate.md`. At complex pairs with complex independent current, (I1) is `a2-layers.md` §7.6(b)–(c), which that gate accepts conditionally on its complex local coefficient inputs (`a2-curved.md` (8.4)–(8.7) on a fixed complex disc, gated row 93). The gate's premise qualification concerns the coefficient \(\Delta^{(2)}[j]\). It is empty here, because \(j=0\).
- The dual-norm computation \(\|e\,\delta_c\|_{\mathcal X^*}=\xi_c\) for a unit colour vector \(e\) placed in the \(\nu\)-slot at row \(c\) (`gates/h-walk-gate.md` §7, Lemma J check: the dual of \(\sum\xi_c^6|\nu_c|^2\) under the physical row pairing).
- A pillar carries at most \(4(\xi_y/\eta)^4\) bonds. Bonds and plaquettes based in a pillar have scale in \([\xi_y,L\xi_y]\). Pillars have \(d_{\mathbf B}\)-diameter \(\le4L\) (`a2-layers.md` 5.1, 7.3). \(K_\tau:=\sup_c\sum_ye^{-\tau d_{\mathbf B}(y,c)}<\infty\) when \(\tau\rho'\ge16\log L\) (`h-walk.md` §5, from the gated ball count).

**Theorem A.** Assume the hypotheses of Lemma L: (I1), \(M_1\ge M_C(L)\), and the ceiling \((\alpha_0,\alpha_1,\gamma_0)\le a_*(L)\), with \(\tau_L\rho'\ge256\log L\). Let \(P=(\mathbf U,\mathbf J)\) be any regular pair for the depth-\(k\) sequence, real or complex, with independent complex current. Then, for every row \(c\) and pillar \(y\),
\[
 \|H(\cdot,c)\|_{E,y}\le C_LB_L\,e^{-\tau_Ld_{\mathbf B}(y,c)} ,
 \tag{1.1}
\]
where \(\|A\|_{E,y}^2=\|\nabla_UA\|_{2,y}^2+\|\mathsf m^{-1}A\|_{2,y}^2\) is the local energy norm at \(y\) (physical \(L^2\), terms based in \(y\)). For every weight \(w\) with \(w(b)\le e^{\theta d_{\mathbf B}(b,b')}w(b')\) and \(0\le\theta\le\tau_L/2\),
\[
 \sup_cw(c)\,\eta^4\sum_b|H(b,c)|\,\xi_b^{-3}w(b)^{-1}
 +\sup_cw(c)\,\eta^4\sum_p|D_{\mathbf U}H(p,c)|\,\xi_p^{-2}w(p)^{-1}
 \le C_H^{(1)}:=C_LB_LK_{\tau_L/2}.
 \tag{1.2}
\]
Display (1.2) is (O1) of `wf-room-2.md` §6.3 at \(s\equiv1\). Every constant depends on \(L\) only: not on the depth, mesh, volume, region shape, \(M_1\), or the pair.

*Proof.* **Step 1 (a column is a supported source).** For a unit colour vector \(e\), let \(F_{c,e}\in\mathcal X^*\) be the source \(e\,\delta_c\) in the \(\nu\)-slot, zero in the others. By Lemma U(d) with \(f=g=g'=0\), the solution of \(\mathbb K\Psi=F_{c,e}\) has \(\nu=-W^{-1}e\delta_c\) and \(A=\mathsf GQ^{\mathsf T}W^{-1}e\delta_c=\mathsf H(\cdot,c)e\). \(F_{c,e}\) is supported near the pillar of \(c\), and \(\|F_{c,e}\|_*=\xi_c\). Lemma L gives \(\|\mathsf H(\cdot,c)e\|_{E,y}\le\|\mathbb K^{-1}F_{c,e}\|_{\mathcal X,y}\le B_Le^{-\tau_Ld_{\mathbf B}(y,c)}\xi_c\). Now \(H(\cdot,c)=\mathsf H(\cdot,c)\xi_c^{-1}\). Taking \(e\) over an orthonormal basis of \(\mathfrak g^c\) and the operator norm in colour costs a factor \(\sqrt3\). This is (1.1).

**Step 2 (Cauchy–Schwarz on one pillar).** For \(A=H(\cdot,c)e\), using \(\xi_b\ge\xi_y\) and the bond count,
\[
 \eta^4\sum_{b\in y}\xi_b^{-3}|A(b)|
 \le\Big(\eta^4\sum_{b\in y}\xi_b^{-4}\Big)^{1/2}\Big(\eta^4\sum_{b\in y}\xi_b^{-2}|A(b)|^2\Big)^{1/2}
 \le2\,\|\mathsf m^{-1}A\|_{2,y}.
\]
For the curl at the complex pair, \((D_{\mathbf U}A)(p)\) is \((D_UA)(p)\) plus terms \(\eta^{-1}(\operatorname{Ad}e^{i\eta A'(b')}-1)\) applied to transported values \(A(b'')\) on \(\partial p\). These are bounded by \(3|A'(b')||A(b'')|\le3\alpha_1\xi^{-1}|A(b'')|\). Also \(|(D_UA)(p)|\le|\nabla_\mu A_\nu(x)|+|\nabla_\nu A_\mu(x)|\) for \(p=(x;\mu,\nu)\). So
\(\eta^4\sum_{p\in y}\xi_p^{-2}|D_{\mathbf U}A(p)|\le C_L\sum_{y'\in y^+}\|A\|_{E,y'}\), where \(y^+\) is the set of at most \(N_L\) pillars within \(d_{\mathbf B}\)-distance \(1\) of \(y\).

**Step 3 (summation).** For \(b\) based in \(y\), \(w(c)/w(b)\le e^{\theta(d_{\mathbf B}(y,c)+4L)}\). By Steps 1–2,
\[
 w(c)\,\eta^4\sum_b\frac{|H(b,c)|}{\xi_b^3w(b)}\le\sum_y e^{\theta(d(y,c)+4L)}\,2\sqrt3\,C_LB_Le^{-\tau_Ld(y,c)}\le C_LB_L\,K_{\tau_L/2},
\]
since \(\theta\le\tau_L/2\) and \((\tau_L/2)\rho'\ge16\log L\). The curl term is the same, with \(y^+\) and \(d(y',c)\ge d(y,c)-1\). \(\square\)

**Consequence.** The gate's first failing step (row 125, Defect 1: "(O1) at \(s=1\) is not given by the cited P82° for the specified lift") is replaced by Theorem A. (O1) now holds for **R9's own** current-corrected lift on the general complex, independent-current pair domain, uniformly in depth. The gate's partial repair, for the P82° lift at a reduced rate, is no longer needed. The specification (6.1) and the gate's corrected (S5) estimates of `wf-room-2.md` §6.3 read (O1) as stated, with \(C_H=C_H^{(1)}\). Label: **implication**, from gated inputs (Lemma U, Lemma L with its repair) and the conditional premise (I1).

**Counterexample attempts (done first).**
- (a) *Large actual current.* A staggered real part has \(|J(\mathbf U)|\) up to \(C\alpha_0\eta^{-1}\xi^{-2}\) (SA 10531). \(J(\mathbf U)\) does not enter \(\mathsf G\). The Wilson Hessian contributes curl-squared plus a curvature remainder of mass-form size (PX114–PX118, used through (I1)), and \(\Delta'_\pi\) is evaluated at the independent \(\mathbf J\), with \(|\mathbf J|<\gamma_0\xi^{-3}\) (`a2-layers.md` (7.2)). No failure. A reading with \(\Delta'_\pi[J(\mathbf U)]\) would fail (`a3-clauses.md` §4.2(a)), but R9 does not use one.
- (b) *Column sums against row sums.* A lift whose columns are \(L^2\)-small but not summable would need mass at distance with no decay. Lemma L excludes this pillar by pillar, and Step 2 is a proof, not an estimate of a typical case. No failure.
- (c) *Complex links.* \(|\operatorname{Ad}\mathbf U(b)|\le e^{2\eta|A'|}\le1+4\alpha_1\) per bond. Only the curl term sees it (Step 2). No failure.

## 2. Item (1) for decoupled \(s\): the specified expansion, and (O1) on \(|s_\Delta|<e^{\bar\kappa}\)

### 2.1 The specification

The outline treats the decoupled operators of (R9) as **specified data**: "specified linear maps … They include their walk coefficients and convergence domains" (SA 5775–5783). It requires no identity between decoupled sums (mechanism (j), SA 10562), and builds the propagators' expansions by mechanism (f) (SA 10476, 10540). As with the erosion assignment, the profile rule and specification (6.1), the expansion must be supplied. We supply the one of `h-walk.md` Theorem W at \(j=0\).

**Definition D.** Let \(\mathcal P\) be the partition of the torus into closed parameter cubes \(\Delta\), with complex parameters \(s=(s_\Delta)\). For a walk \(\omega=(\kappa_0,\dots,\kappa_n)\) of Theorem W for \(\mathbb K[S,P,0]\), let \([\![\omega]\!]=\bigcup_i\kappa_i^{(4)}\) be its hull and \([\![\omega]\!]^+\) the set of points at \(d_{\mathbf B}\)-distance \(\le r_+:=C_LM_1\) from it. Here \(r_+\) is at least the reach of the cutoff normalisations (`gates/h-walk-gate.md` §3: \(O_L(M_1)\)). Put
\[
 \mathsf P(\omega)=\{\Delta\in\mathcal P:\Delta\cap[\![\omega]\!]^+\ne\emptyset\},\qquad
 s^\omega=\prod_{\Delta\in\mathsf P(\omega)}s_\Delta,
\]
\[
 \mathsf H(s):=\sum_\omega s^\omega\,[T_\omega]_{A\nu},\qquad H(s):=\mathsf H(s)\mathsf m^{-1}.
 \tag{2.1}
\]
\(H_1(s)\), \(\mathfrak G(s)\) and the walk data in \(\mathsf W_s\) are defined the same way from their own expansions. They are not used in this section.

**Hypothesis (P).** Every set of \(d_{\mathbf B}\)-diameter less than \(\ell_{\mathsf P}/2\) meets at most \(2^4\) cubes of \(\mathcal P\). It holds when \(\mathcal P\) is a grid of physical side at least \(\ell_{\mathsf P}\xi_{\max}/2\), with \(\xi_{\max}\) the top scale. Indeed \(d_{\mathbf B}(x,x')\ge|x-x'|/\xi_{\max}\), since the density of \(d_{\mathbf B}\) is everywhere at least \(\xi_{\max}^{-1}\). Each coordinate projection of such a set then has length less than the grid side and meets at most two grid intervals.

### 2.2 Two lemmas

**Lemma P (cubes against length; the outline's mechanism (i) with an explicit constant).** Let \(r_1:=18LM_1+2r_++4L\) and \(\ell_{\mathsf P}>8r_1\). Let \(\omega\) be a walk, \(y\) a pillar meeting \(\operatorname{supp}\tilde h_{\kappa_0}\), and \(z\) any point. Then \(\#\mathsf P(\omega)\le2^4(1+4d_{\mathbf B}(\omega;y,z)/\ell_{\mathsf P})\). Hence, for \(|s_\Delta|\le e^{\bar\kappa}\),
\[
 |s^\omega|\le e^{16\bar\kappa}\,e^{(64\bar\kappa/\ell_{\mathsf P})\,d_{\mathbf B}(\omega;y,z)} .
 \tag{2.2}
\]
*Proof.* \(\kappa^{(4)}\) has side \(9M_1\xi_\kappa\), hence Euclidean diameter \(18M_1\xi_\kappa\). It meets at most two consecutive layers, where the local scale is at least \(\xi_\kappa/L\) (`h-walk.md` §3, "Two layers"). So the \(d_{\mathbf B}\)-diameter of \(\kappa^{(4)}\) is at most \(18LM_1\), and that of its \(r_+\)-enlargement at most \(18LM_1+2r_+\). Let \(\Gamma\) be a path from \(y\) to \(z\), of \(d_{\mathbf B}\)-length \(t\), meeting \(X_{\kappa_1},\dots,X_{\kappa_n}\). For \(i\ge1\), \(X_{\kappa_i}\subset\kappa_i^{(4)}\) meets \(\Gamma\). For \(i=0\), \(\kappa_0^{(4)}\supset\operatorname{supp}\tilde h_{\kappa_0}\) meets the pillar \(y\), of diameter \(\le4L\), and \(\Gamma\) starts in \(y\). So \([\![\omega]\!]^+\) lies in the \(r_1\)-neighbourhood of \(\Gamma\). Cut \(\Gamma\) into \(m=\max\{1,\lceil4t/\ell_{\mathsf P}\rceil\}\) arcs of length \(\le\ell_{\mathsf P}/4\). By the triangle inequality, the \(r_1\)-neighbourhood of an arc has diameter \(\le\ell_{\mathsf P}/4+2r_1<\ell_{\mathsf P}/2\). So it meets at most \(2^4\) cubes, by (P). Thus \(\#\mathsf P(\omega)\le2^4m\le2^4(1+4t/\ell_{\mathsf P})\). The left side is an integer independent of \(\Gamma\), so the bound holds with \(t=d_{\mathbf B}(\omega;y,z)\). Finally \(|s^\omega|\le e^{\bar\kappa\#\mathsf P(\omega)}\). \(\square\)

As in the outline, the leftover \(e^{16\bar\kappa}\) cannot be avoided: a cell at a corner of the grid meets \(2^4\) cubes.

**Lemma WC (walls separate connected sets).** Let \(\mathcal P\) be a cubical grid on the torus with at least three cubes per direction, and \(\mathcal N\subset\mathcal P\). Let \(C\) be a connected set such that every cube of \(\mathcal P\) meeting \(C\) lies in \(\mathcal P\setminus\mathcal N\). Then all cubes meeting \(C\) lie in one wall-component of \(\mathcal P\setminus\mathcal N\) (components for the relation "share a three-dimensional face", SA 5795).

*Proof.* For a point \(x\), the cubes containing \(x\) have grid indices \(\prod_\mu I_\mu\). Here \(I_\mu\) is one index, or two consecutive ones when \(x_\mu\) lies on a grid hyperplane. Two such cubes whose indices differ in one coordinate share a 3-face, and any two indices of the product are joined by changing one coordinate at a time. So the star \(\mathrm{St}(x)\) is face-connected, and lies in a single wall-component when it avoids \(\mathcal N\). Let \(\mathcal C\) be the cubes meeting \(C\), and suppose \(\mathcal C\) meets two components \(\mathcal W_1\) and \(\mathcal W_2\cup\dots\). Put \(C_1=C\cap\bigcup_{\Delta\in\mathcal C\cap\mathcal W_1}\Delta\), and let \(C_2\) be the same with the other components. Both are closed in \(C\), being finite unions of closed cubes intersected with \(C\). They are nonempty and cover \(C\). They are disjoint, because a point in both would have its star meeting two components. This contradicts connectedness. \(\square\)

### 2.3 Theorem B: (O1) for decoupled \(s\)

**Theorem B.** Assume the hypotheses of Theorem W (those of Lemma L, with (I1) uniform on every cut-down, and \(M_1\ge M_W(L)\), \(M_1\ge2\nu_1C_W\)), (P), and \(\ell_{\mathsf P}\ge\max\{8r_1+1,\,256\bar\kappa/\tau_L\}\). For every regular pair \(P\) of the depth-\(k\) sequence (real or complex, independent current) and every \(s\) with \(|s_\Delta|\le e^{\bar\kappa}\):

- (a) The series (2.1) converges absolutely, uniformly in \((s,P)\). \(\mathsf H(s)\) is jointly holomorphic in \((s,P)\) on the open polydisc times the open class, real at real \((s,P)\), and gauge covariant. Also \(\mathsf H(1)=\mathsf H\).
- (b) For every row \(c\) and pillar \(y\), \(\|H(s)(\cdot,c)\|_{E,y}\le2\sqrt3N_LB_L\,e^{16\bar\kappa}\,e^{-(\tau_L/4)d_{\mathbf B}(y,c)}\).
- (c) **(O1):** for every weight of rate \(\theta\le\tau_L/8\), the two sums in (1.2), with \(H(s)\) in place of \(H\), are at most \(C_H:=C_LB_L\,e^{16\bar\kappa}K_{\tau_L/8}\).
- (d) **Splitting.** Suppose \(s_\Delta=0\) for \(\Delta\in\mathcal N\). Then \(H(s)(b,c)=0\) whenever the base point of \(b\) or of \(c\) lies in a cube of \(\mathcal N\), or the two lie in cubes of different wall-components of \(\mathcal P\setminus\mathcal N\). Each block of \(H(s)\) on a wall-component \(\mathcal W\) depends on the pair only through its values on \(\bigcup\mathcal W\).

The constant \(C_H\) has the form \(\widehat b=Ce^{16\bar\kappa}\) of SA 10383. Order of choice: \(L\); then \(a_*,\tau_L,B_L,C_W,\nu_1,N_L\); then \(M_1\); then \(\bar\kappa\) (free of \(M_1\)); then \(\ell_{\mathsf P}\). This is the outline's order (SA 10582). Nothing depends on depth, mesh, volume or region shape.

*Proof.* (b) Apply (6.2) of Theorem W, as gated (`gates/h-walk-gate.md` §6: chaining redone, no failing step), to \(F_{c,e}\), which is supported near \(c\). Use (2.2) with \(z=c\) and \(64\bar\kappa/\ell_{\mathsf P}\le\tau_L/4\):
\[
 |s^\omega|\,\|T_\omega F_{c,e}\|_{\mathcal X,y}\le B_L\,e^{16\bar\kappa}(C_W/M_1)^n e^{-(\tau_L/4)d_{\mathbf B}(\omega;y,c)}\,\xi_c .
\]
A term is nonzero at \(y\) only if \(y\) meets \(\operatorname{supp}\tilde h_{\kappa_0}\), which leaves at most \(N_L\) choices of \(\kappa_0\), by bounded overlap (c4). At most \(\nu_1^n\) walks of length \(n\) start at \(\kappa_0\). Also \(d_{\mathbf B}(\omega;y,c)\ge d_{\mathbf B}(y,c)\). Summing \(\sum_n(\nu_1C_W/M_1)^n\le2\) and dividing by \(\xi_c\) gives (b).

(a) By (b), for fixed \((y,c)\) the series converges absolutely, uniformly on the closed polydisc times the class. At fixed volume there are finitely many \((y,c)\). Each term is a monomial in \(s\) times \([T_\omega]_{A\nu}\). The latter is holomorphic and real in the fields; the gate keeps this part of W(c): "for fixed regions, the cutoffs are fixed scalar numbers: this failure does not introduce additional field reads or spoil holomorphy in the fields". It is gauge covariant (gate §6: covariance of the algebraic construction survives). A uniform limit of holomorphic functions of finitely many variables is holomorphic. At \(s\equiv1\), \(\sum_\omega[T_\omega]_{A\nu}=[\mathbb K^{-1}]_{A\nu}=\mathsf H\), by Theorem W(a) and (I-b).

(c) Steps 2–3 of Theorem A, with (b) in place of (1.1) and \(\theta\le\tau_L/8\), so that the sum is \(\sum_ye^{-(\tau_L/8)d(y,c)}\le K_{\tau_L/8}\).

(d) If \([T_\omega]_{A\nu}(b,c)\ne0\), then \(b\) is based in \(\operatorname{supp}\tilde h_{\kappa_0}\) (the output support) and \(c\) in \(\operatorname{supp}\theta_{\kappa_n}\) (the input is read through \(\theta_{\kappa_n}\)). Both lie in \([\![\omega]\!]\). The hull is connected: consecutive \(\kappa_i^{(4)}\) share \(X_{\kappa_{i-1}}\cap X_{\kappa_i}\ne\emptyset\). Its \(r_+\)-enlargement is connected too, since \(d_{\mathbf B}\) is a path metric. If a base point lies in a cube of \(\mathcal N\), that cube is in \(\mathsf P(\omega)\). If the two lie in different wall-components, Lemma WC applied to \([\![\omega]\!]^+\) puts a cube of \(\mathcal N\) in \(\mathsf P(\omega)\). In both cases \(s^\omega=0\). If \(\mathsf P(\omega)\subset\mathcal W\), then \([\![\omega]\!]\subset\bigcup\mathcal W\), and \(T_\omega\) reads the fields only on its hull (the field part of W(c), kept by the gate). \(\square\)

**What (d) does and does not give.** It gives block diagonality and field-locality, which are what (S3) of `wf-room-2.md` and SA's splitting clause use. It does not give the region-trace locality of W(c)–(d), which `gates/h-walk-gate.md` §3 found WRONG at (C5). That clause matters only when two **different sequences** are compared. Section 3 meets it in the removed comparison and avoids it there by a compatible choice of expansions, not by repairing (C5).

**Consequence for `wf-room-2.md` §6.3.** With Definition D, (O1) holds on the whole decoupling polydisc with \(C_H=C_LB_Le^{16\bar\kappa}\). So (6.3)–(6.4) and the gate's corrected (S5) hold for decoupled \(s\). They are conditional only on the first system's own field bounds, which are not part of (O1) (§5). Label: **implication**. (2.1) is a specification, admissible by SA 5775–5783 and mechanism (j).

**Counterexample attempts (done first).**
- (a) *Many parameters on one walk.* With \(|s_\Delta|=e^{\bar\kappa}\) everywhere, a long walk carries \(e^{\bar\kappa\#\mathsf P(\omega)}\). Lemma P makes each cube beyond the first \(2^4\) cost length \(\ell_{\mathsf P}/64\), so the exponential decay pays once \(\ell_{\mathsf P}\ge256\bar\kappa/\tau_L\). No failure.
- (b) *Vanishing parameters near a row.* Then \(QH(s)=0\) there, not \(1\) (SA 10562). (O1) is a bound and reads no identity. No failure.
- (c) *Corner cells.* These give the factor \(e^{16\bar\kappa}\), which is the outline's \(\widehat b\). No failure.
