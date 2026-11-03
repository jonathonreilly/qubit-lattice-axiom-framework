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

**Definition D.** Let \(\mathcal P\) be the partition of the torus into closed parameter cubes \(\Delta\), with complex parameters \(s=(s_\Delta)\). For a walk \(\omega=(\kappa_0,\dots,\kappa_n)\) of Theorem W for \(\mathbb K[S,P,0]\), let \([\![\omega]\!]=\bigcup_i\kappa_i^{(4)}\) be its hull. Let \(\kappa^\sharp\) be the concentric cube of side \(8L^2M_1\xi_\kappa\), and \([\![\omega]\!]^+:=\bigcup_i\kappa_i^\sharp\). This set is physical, so it does not depend on which sequence's metric is used (§3 needs this). It contains the reach of the cutoff normalisations (`gates/h-walk-gate.md` §3: \(O_L(M_1)\); see Lemma C1). Assume \(R_1\ge8L^3\). Then \(\kappa^\sharp\) meets at most three consecutive layers, because \(\Omega_{i+2}\) is at distance \(>\rho\xi_{i+1}\ge8L^4M_1\xi_\kappa\) and \(\Omega_{i-1}^c\) at distance \(>\rho\xi_{i-1}\ge8L^2M_1\xi_\kappa\) from a cube \(\kappa\subset\mathcal L_i\). So the local scale on \(\kappa^\sharp\) is \(\ge\xi_\kappa/L\), and its \(d_{\mathbf B}\)-diameter is \(\le16L^3M_1\). Put
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

**Lemma P (cubes against length; the outline's mechanism (i) with an explicit constant).** Let \(r_1:=16L^3M_1+4L\) and \(\ell_{\mathsf P}>8r_1\). Let \(\omega\) be a walk, \(y\) a pillar meeting \(\operatorname{supp}\tilde h_{\kappa_0}\), and \(z\) any point. Then \(\#\mathsf P(\omega)\le2^4(1+4d_{\mathbf B}(\omega;y,z)/\ell_{\mathsf P})\). Hence, for \(|s_\Delta|\le e^{\bar\kappa}\),
\[
 |s^\omega|\le e^{16\bar\kappa}\,e^{(64\bar\kappa/\ell_{\mathsf P})\,d_{\mathbf B}(\omega;y,z)} .
 \tag{2.2}
\]
*Proof.* \(\kappa^{(4)}\) has side \(9M_1\xi_\kappa\), hence Euclidean diameter \(18M_1\xi_\kappa\). It meets at most two consecutive layers, where the local scale is at least \(\xi_\kappa/L\) (`h-walk.md` §3, "Two layers"). So the \(d_{\mathbf B}\)-diameter of \(\kappa^{(4)}\) is at most \(18LM_1\), and that of \(\kappa^\sharp\supset\kappa^{(4)}\) at most \(16L^3M_1\) (Definition D). Let \(\Gamma\) be a path from \(y\) to \(z\), of \(d_{\mathbf B}\)-length \(t\), meeting \(X_{\kappa_1},\dots,X_{\kappa_n}\). For \(i\ge1\), \(X_{\kappa_i}\subset\kappa_i^{(4)}\) meets \(\Gamma\). For \(i=0\), \(\kappa_0^{(4)}\supset\operatorname{supp}\tilde h_{\kappa_0}\) meets the pillar \(y\), of diameter \(\le4L\), and \(\Gamma\) starts in \(y\). So \([\![\omega]\!]^+\) lies in the \(r_1\)-neighbourhood of \(\Gamma\). Cut \(\Gamma\) into \(m=\max\{1,\lceil4t/\ell_{\mathsf P}\rceil\}\) arcs of length \(\le\ell_{\mathsf P}/4\). By the triangle inequality, the \(r_1\)-neighbourhood of an arc has diameter \(\le\ell_{\mathsf P}/4+2r_1<\ell_{\mathsf P}/2\). So it meets at most \(2^4\) cubes, by (P). Thus \(\#\mathsf P(\omega)\le2^4m\le2^4(1+4t/\ell_{\mathsf P})\). The left side is an integer independent of \(\Gamma\), so the bound holds with \(t=d_{\mathbf B}(\omega;y,z)\). Finally \(|s^\omega|\le e^{\bar\kappa\#\mathsf P(\omega)}\). \(\square\)

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

(d) If \([T_\omega]_{A\nu}(b,c)\ne0\), then \(b\) is based in \(\operatorname{supp}\tilde h_{\kappa_0}\) (the output support) and \(c\) in \(\operatorname{supp}\theta_{\kappa_n}\) (the input is read through \(\theta_{\kappa_n}\)). Both lie in \([\![\omega]\!]\). The hull is connected: consecutive \(\kappa_i^{(4)}\) share \(X_{\kappa_{i-1}}\cap X_{\kappa_i}\ne\emptyset\). So is \([\![\omega]\!]^+=\bigcup_i\kappa_i^\sharp\), since \(\kappa_i^\sharp\supset\kappa_i^{(4)}\). If a base point lies in a cube of \(\mathcal N\), that cube is in \(\mathsf P(\omega)\). If the two lie in different wall-components, Lemma WC applied to \([\![\omega]\!]^+\) puts a cube of \(\mathcal N\) in \(\mathsf P(\omega)\). In both cases \(s^\omega=0\). If \(\mathsf P(\omega)\subset\mathcal W\), then \([\![\omega]\!]\subset\bigcup\mathcal W\), and \(T_\omega\) reads the fields only on its hull (the field part of W(c), kept by the gate). \(\square\)

**What (d) does and does not give.** It gives block diagonality and field-locality, which are what (S3) of `wf-room-2.md` and SA's splitting clause use. It does not give the region-trace locality of W(c)–(d), which `gates/h-walk-gate.md` §3 found WRONG at (C5). That clause matters only when two **different sequences** are compared. Section 3 meets it in the removed comparison and avoids it there by a compatible choice of expansions, not by repairing (C5).

**Consequence for `wf-room-2.md` §6.3.** With Definition D, (O1) holds on the whole decoupling polydisc with \(C_H=C_LB_Le^{16\bar\kappa}\). So (6.3)–(6.4) and the gate's corrected (S5) hold for decoupled \(s\). They are conditional only on the first system's own field bounds, which are not part of (O1) (§5). Label: **implication**. (2.1) is a specification, admissible by SA 5775–5783 and mechanism (j).

**Counterexample attempts (done first).**
- (a) *Many parameters on one walk.* With \(|s_\Delta|=e^{\bar\kappa}\) everywhere, a long walk carries \(e^{\bar\kappa\#\mathsf P(\omega)}\). Lemma P makes each cube beyond the first \(2^4\) cost length \(\ell_{\mathsf P}/64\), so the exponential decay pays once \(\ell_{\mathsf P}\ge256\bar\kappa/\tau_L\). No failure.
- (b) *Vanishing parameters near a row.* Then \(QH(s)=0\) there, not \(1\) (SA 10562). (O1) is a bound and reads no identity. No failure.
- (c) *Corner cells.* These give the factor \(e^{16\bar\kappa}\), which is the outline's \(\widehat b\). No failure.

## 3. Item (2): the removed-map comparison, with every changed ingredient

### 3.1 What changes, and the hypotheses

The removed fields are "the differences produced by replacing the original response and the original background by their box versions" (SA 15949–15952), with the factor \(e^{-cM/\sigma_j}\) (WF7). The removed currents are the differences of (6.1) for the two systems (`wf-room-2.md` §6.2). The gate's Defect 2 lists what may change between them: reference, node transport, rows, inner-plaquette action. Here both systems are put in common coordinates, and each change is either proved identical on an explicit carrier or bounded with its boundary exponential.

The two systems are \(\mathfrak D=(S,P)\), the step's separated sequence with its pair, and \(\mathfrak D^\square=(S^\square,P^\square)\), a separated sequence on the box with its pair. Both have cube size \(M_1\) and gap \(\ge\rho\), so `h-walk.md` Theorem W applies to each, and Theorems A and B hold for each. Let \(G\subset R_z\) be the agreement region. Write \(D_x:=d_{\mathbf B}(x,G^c)\) (the metric of \(S\); \(D_x=0\) off \(G\)) and \(w_G:=e^{\theta'D}\). This weight is in \(\mathcal W_{\theta'}\). For \(\kappa\in K\) let \(\kappa^\sharp\) be the concentric cube of side \(8L^2M_1\xi_\kappa\).

- **(H-seq)** The regions of \(S\) and \(S^\square\) coincide on \(G^\sharp:=\bigcup\{\kappa^\sharp:\kappa^{(4)}\subset G\}\). Assume also \(R_1\ge8L^3\), so that each \(\kappa^\sharp\) meets at most three consecutive layers.
- **(H-pair)** On \(G\), \(\mathbf U^\square=(e^{i\eta X}\mathbf U)^g\) and \(\mathbf J^\square=\operatorname{Ad}(g)(\mathbf J+\delta\mathbf J)\), with a gauge transformation \(g\) (the node lift and the change of representative) and
\[
 \|\delta P\|(x):=\xi_x|X(x)|+\xi_x^2|\nabla_{\mathbf U}X(x)|+\xi_x^3|\delta\mathbf J(x)|\le\varepsilon_Pe^{-\theta_PD_x},\qquad|g(x)-\mathbf 1|\le\varepsilon_Pe^{-\theta_PD_x}.
\]
  Here \(\varepsilon_P\le c_Pa_{\min}\), \(a_{\min}=\min\{\alpha_0,\alpha_1,\gamma_0\}\), and \(P\) satisfies the class inequalities with half the ceiling.
- **(H-field)** \(\varepsilon_H:=\sup_{b\in G}w_G(b)\max\{\xi_b|\mathbf H-\mathbf H^\square|,\xi_b^2|\nabla(\mathbf H-\mathbf H^\square)|\}\), with \(\mathbf H^\square\) in the gauge of (H-pair).
- **(Spec)** Both systems use Definition D, with the same partition \(\mathcal P\) and the same parameters \(s\). The comparison is between two **specified** maps, as SA 5775–5783 allows. A compatible choice is part of the box map's specification, in the way the outline calls for a "compatible boundary comparison" (SA OA7 paragraph).

When the box response is taken at the same pair restricted, as in "replacing the original response by its box version", (H-pair) holds with \(X=0\), \(\delta\mathbf J=0\), \(g=\mathbf 1\). When the background is replaced too, (H-pair) is the localisation estimate (1b) Theorem 6(c) (SA 9779–9787: "two backgrounds whose sequences and whose data coincide on \(W\) differ there to this extent"), with \(\theta_P=\delta_W\) and \(\varepsilon_P=C_\mu\varepsilon_1\). Its current member \(\xi^3|D^*Df|\) bounds the removed **background** current directly, so no readout formula enters there.

### 3.2 Term identity and the operator comparison

**Lemma C1 (term identity).** Assume (H-seq). Let \(\omega\) be a walk of \(S\) with \(\kappa_i^{(4)}\subset G\) for every \(i\). Then \(\omega\) is a walk of \(S^\square\). Its factors \(\tilde h_{\kappa_i},\theta_{\kappa_i}\), its cut-down sequences \(S^{\kappa_i}\), and its commutator stencils are the same for both systems. Hence \(T^\square_\omega\) and \(T_\omega\) are the same holomorphic function on the local class on \([\![\omega]\!]\), evaluated at \(P^\square|_{[\![\omega]\!]}\) and \(P|_{[\![\omega]\!]}\) respectively.

*Proof.* A cube \(\kappa'\) is in \(K_i\) iff it is a level-\(i\) \(M_1\)-cube contained in \(\overline{\mathcal L_i}\). Here \(\kappa'\subset\overline{\mathcal L_i}\) is decided by \(\Omega_i,\Omega_{i+1}\) on \(\kappa'\). The cutoffs \(\tilde h_\kappa,\phi_\kappa\) depend only on \(\kappa\). The normalisation of \(\theta_\kappa\) sums \(\phi_{\kappa'}\) over the cubes with \(\operatorname{supp}\phi_{\kappa'}\cap\kappa^{(1/4)}\ne\emptyset\). By the two-layer property, which holds in both sequences since both are separated with gap \(\rho\ge64LM_1\), these have \(\xi_{\kappa'}\in\{\xi_\kappa/L,\xi_\kappa,L\xi_\kappa\}\). Each lies within \(\ell^\infty\)-distance \(2LM_1\xi_\kappa\) of \(c_\kappa\), hence inside \(\kappa^\sharp\). Cubes of level \(\ge\) level\((\kappa)+2\) cannot be present in either sequence: \(\Omega_{i+2}\) lies at distance \(>\rho\xi_{i+1}\ge64L^2M_1\xi_\kappa\) from \(\mathcal L_i\). So the same candidate cubes, decided by the same regions, enter both denominators. This is the gate's repair of (C5) (`gates/h-walk-gate.md` §3), which is provable here because the two sequences agree on a fixed enlargement. The "absent candidate" problem cannot arise inside \(G^\sharp\). The cut-down \(S^\kappa\) is determined by \(\kappa\) and \(\Omega_i\cap\kappa^{(4)}\) (C1–C4, gated). The commutator \([\mathbb K,\tilde h_\kappa]=[\mathbb K_\kappa,\tilde h_\kappa]\) reads data within \(\kappa^{(5/2)}\). The rest is (C2), and Theorem W(c)'s field part, kept by the gate. \(\square\)

**Theorem C (operator comparison).** Assume the hypotheses of Theorem B for both systems, together with (H-seq), (H-pair) and (Spec). Put \(r'':=C_\sharp M_1\), the \(d_{\mathbf B}\)-diameter bound of \(\kappa^{(4)}\) plus \(4L\), with \(C_\sharp=C_\sharp(L)\). Put \(\theta':=\min\{\theta_P/2,\tau_L/16\}\). Then, for every row \(c\) of \(G\) and pillar \(y\), with \(|s_\Delta|\le e^{\bar\kappa}\) and \(D_y=0\) for \(y\notin G\),
\[
 \|(H(s)-H^\square(s))(\cdot,c)\|_{E,y}\le C_*\,e^{-\theta'(D_y+D_c)}\,e^{-(\tau_L/16)d_{\mathbf B}(y,c)},
 \qquad C_*=C_LB_Le^{16\bar\kappa}e^{\tau_Lr''}\big(1+\varepsilon_P/a_{\min}\big).
 \tag{3.1}
\]
Consequently, for force-type \(f\) and plaquette-type \(q\) supported anywhere,
\[
 \|(H-H^\square)(s)^{\mathsf T}f\|_{Y,w_G}\le C_*K_{\tau_L/32}\sup_b\xi_b^3|f(b)|,\qquad
 \|(D(H-H^\square)(s))^{\mathsf T}q\|_{Y,w_G}\le C_*K_{\tau_L/32}\sup_p\xi_p^2|q(p)|.
 \tag{3.2}
\]
Here \(D\) is the curl at \(\mathbf U\) on the first term and at \(\mathbf U^\square\) on the second. Their difference is a local term bounded by \(C|X|\), carried in Lemma K below.

*Proof.* Split the walks contributing to \(H(s)(\cdot,c)\) at \(y\) into \(\mathcal W_{\rm in}\), those with every \(\kappa_i^{(4)}\subset G\), and \(\mathcal W_{\rm out}\), the rest, and do the same for the box system. By Lemma C1 the \(\mathcal W_{\rm in}\) families coincide. They carry the same monomials \(s^\omega\), since \(\mathsf P(\omega)\) is defined from \([\![\omega]\!]^+\), the same set for both.

*Inner walks.* By (H-pair), the pair on \([\![\omega]\!]\) is joined to \(P^\square\) (in the gauge \(g^{-1}\)) by \(P(t)=(e^{i\eta tX}\mathbf U,\mathbf J+t\,\delta\mathbf J)\). Its real factor \(U\) is fixed, and its complex factor \(A'(t)\) is defined by \(e^{i\eta A'(t)}=e^{i\eta tX}e^{i\eta A'}\). Let \(\varepsilon_\omega:=\sup_{[\![\omega]\!]}\|\delta P\|\). For \(|t|\le R_\omega:=c\,a_{\min}/\varepsilon_\omega\), every class inequality holds on \([\![\omega]\!]\). The potential bounds use BCH with \(\eta|X|\le\varepsilon_\omega\). The curvature bound uses the local expansion \(\partial(e^{i\eta Y}\mathbf U)=(1+i\eta^2D_{\mathbf U}Y+O(\eta^2|Y|^2+\eta|Y||\partial\mathbf U-1|))\partial\mathbf U\) (SA 15884), with half the curvature ceiling free. The current bound is immediate, and the real gauge clause concerns \(U\) only. So \(t\mapsto T_\omega(P(t))F_{c,e}\) is holomorphic on \(|t|<R_\omega\), and bounded there by (6.2). Cauchy's estimate on the disc \(|t|\le R_\omega/2\) gives \(\|(T_\omega(P^\square)-T_\omega(P))F_{c,e}\|_{\mathcal X,y}\le(C\varepsilon_\omega/a_{\min})\,B_L(C_W/M_1)^ne^{-(\tau_L/2)d(\omega;y,c)}\xi_c\). Let \(\delta_\omega:=d_{\mathbf B}([\![\omega]\!],G^c)\). Then \(\varepsilon_\omega\le\varepsilon_Pe^{-\theta_P\delta_\omega}\). Any path from \(y\) to \(c\) meeting the cells comes within \(\delta_\omega+r''\) of \(G^c\), so \(d(\omega;y,c)\ge D_y+D_c-2\delta_\omega-2r''\). Split \((\tau_L/4)d(\omega;y,c)\ge(\tau_L/8)d(y,c)+(\tau_L/8)(D_y+D_c-2\delta_\omega-2r'')\), and use \(\delta_\omega\le\min\{D_y,D_c\}\). This gives
\(\theta_P\delta_\omega+(\tau_L/8)(D_y+D_c-2\delta_\omega)\ge\min\{\theta_P/2,\tau_L/8\}(D_y+D_c)\). If \(\theta_P\ge\tau_L/4\), the \(\delta_\omega\) terms have a nonnegative coefficient. Otherwise use \(\delta_\omega\le(D_y+D_c)/2\).

*Outer walks.* Some \(\kappa_i^{(4)}\not\subset G\). For \(i\ge1\), the path meets \(X_{\kappa_i}\) within \(r''\) of \(G^c\), so \(d(\omega;y,c)\ge D_y+D_c-2r''\). For \(i=0\), \(D_y\le r''\), and \(d(\omega;y,c)\ge d(y,c)\ge D_c-D_y\ge D_y+D_c-2r''\). Each family, original and box, is bounded by (6.2) and Lemma P separately.

*Summation.* As in Theorem B(b), with \(|s^\omega|\le e^{16\bar\kappa}e^{(\tau_L/4)d(\omega;y,c)}\), at most \(N_L\nu_1^n\) walks of length \(n\) at \(y\), and \(\sum_n(\nu_1C_W/M_1)^n\le2\). The factor \(e^{\tau_Lr''}\) collects \(e^{2r''\tau_L/8}\), and \(\theta'\le\tau_L/16\) leaves \(e^{-(\tau_L/16)d(y,c)}\). This is (3.1).

(3.2) follows as in Steps 2–3 of Theorem A. For a pillar \(y\), \(|((H-H^\square)^{\mathsf T}f)(c)|\) receives at most \(2L^2\|(H-H^\square)(\cdot,c)\|_{E,y}\sup_{b\in y}\xi_b^3|f(b)|\). Multiply by \(w_G(c)=e^{\theta'D_c}\) and sum over \(y\), using \(\sum_ye^{-(\tau_L/16)d(y,c)}\le K_{\tau_L/32}\). The curl is Step 2's covariant-difference bound. \(\square\)

So walks that stay inside the agreement region are identical up to the pair change. That change is paid by the decay of \(\delta P\) into the region. Walks that leave it pay twice the distance to its complement. No region-trace locality beyond Lemma C1 is used. The price of the cutoff margin is the fixed factor \(e^{\tau_Lr''}=e^{C_LM_1}\). It is beaten by the box depth, since in (WF7) \(D\ge cM/\sigma_j\) and \(M\) is chosen after \(M_1\) (SA 10582: "\(\ell_{\mathsf P}\) and \(M\) … are each at least a multiple of \(M_1\)").

### 3.3 Local differences

**Lemma K.** Let \(\mathbf U^\square=e^{i\eta X}\mathbf U\) on a neighbourhood of a bond \(b\) with \(D_b>C_L\), and let \(A,A^\square\) lie in the field ball. At bonds with \(D_b>C_L\) the two systems have the same rows, plaquettes and stencils near \(b\), by (H-seq). Put \(e_b:=\sup_{N(b)}(\xi|A-A^\square|+\xi^2|\nabla(A-A^\square)|)\) and \(x_b:=\sup_{N(b)}\|\delta P\|\), over the fixed neighbourhood \(N(b)\) of the row carriers and plaquettes through \(b\). Then
- (K1) \(\xi_b^3|(K_A(\mathbf U)-K_{A^\square}(\mathbf U^\square))^{\mathsf T}\lambda(b)|\le C(e_b+x_b)\sup_{N(b)}|\lambda|\), and \(\xi_b^3|((K_A-K_0)(\mathbf U)-(K_{A^\square}-K_0)(\mathbf U^\square))^{\mathsf T}\lambda(b)|\le C(e_b+x_b\sup_{N(b)}\xi|A^\square|)\sup|\lambda|\);
- (R1) \(|R_A(b)-R_{A^\square}(b)|\le C\eta|A-A^\square|(b)\);
- (F1) with \(\mathcal N_{\mathbf U}(A):=\Delta'_{\mathbf U}A+N_{\mathbf U}(A)\), \(\xi_b^3|\mathcal N_{\mathbf U}(A)(b)-\mathcal N_{\mathbf U^\square}(A^\square)(b)|\le C(\alpha_0+\|A\|_X+\|A^\square\|_X)(e_b+x_b)\);
- (F2) \(\xi_p^2|\mathcal F(\mathbf U)(p)-\mathcal F(\mathbf U^\square)(p)|\le Cx_p\), and \(\xi_p^2|((D_{\mathbf U}-D_{\mathbf U^\square})A)(p)|\le Cx_p\sup_{N(p)}\xi|A|\).

At bonds with \(D_b\le C_L\) each quantity of either system is bounded separately by its own (5.1), (5.3) and \(|\mathcal F|\le C\alpha_0\xi^{-2}\) (with the system's own rows and plaquettes).

*Proof.* Each quantity at \(b\) is a finite holomorphic expression in the bond variables of \(N(b)\). Row values are holomorphic in \((A',A)\) on a polydisc of radius \(r_L\) in row units (statement 3, SA 10289–10296; `a3-derivative.md` §4.1 (5)–(7)). The chart conversion \(R_A=(E_A^{\mathsf T})^{-1}\) is given by the exponential series (5.2). \(\mathcal F\) is the traceless part of \(\eta^{-2}\partial\mathbf U\). \(\mathcal N\) is the Taylor remainder of the chart gradient (`a3-derivative.md` (11)–(12), at complex pairs (B2)–(B4) of `a3-clauses.md`). A change of base \(\mathbf U\to e^{i\eta X}\mathbf U\) is a change \(A'\to A'\boxplus X\) of the complex factor. So each difference is the increment of a holomorphic function along a segment of length \(\le e_b+x_b\), in units of the polydisc radius. Cauchy's estimate on that polydisc, with the size bounds (5.1), (5.3) and \(|\mathcal F|\le C\alpha_0\xi^{-2}\) as the suprema, gives each line. In (K1), the density factor \(\eta^4\xi_c^{-3}\) of the row entries and bounded carrier overlap give the \(\xi_b^{-3}\), as in `wf-room.md` (5.1). The second line of (K1) uses that \((K_A-K_0)(\mathbf U)\) vanishes at \(A=0\) for every base. So its base derivative carries a factor \(\xi|A^\square|\), by Schwarz's lemma in \(A\). For (F2), the plaquette expansion above gives \(\eta^{-2}|\partial(e^{i\eta X}\mathbf U)-\partial\mathbf U|\le C(|\nabla X|+|X|^2+\eta^{-1}|X|\alpha_0\eta^2\xi^{-2})\le C\xi^{-2}x_p\). Also \(D_{\mathbf U^\square}-D_{\mathbf U}\) multiplies transported values by \(\eta^{-1}(\operatorname{Ad}e^{i\eta X}-1)\), of size \(\le3|X|\). \(\square\)

### 3.4 Theorem D: the removed current

**Theorem D.** Assume the hypotheses of Theorem C, the field ball \(\|\mathbf H\|_X,\|\mathbf H^\square\|_X\le r\) with \(CC_Hr\le1/4\), and (H-field). Let \(\mathsf j\) and \(\mathsf j^\square\) be the readouts (6.1) of the two systems, each with its own lift, field, rows, action and anchor, and with \(\mathsf j^\square\) computed in the gauge of (H-pair). Then, on bonds of \(G\),
\[
 \|\mathsf j-\operatorname{Ad}(g)\mathsf j^\square\|_{F,w_G}
 \le C_D\big(\varepsilon_H+(\|\mathbf H\|_X+\|\mathbf H^\square\|_X)\big),
 \qquad C_D=C_L\,C_*\,K_{\tau_L/32}\,(1+C_H)^2 .
 \tag{3.3}
\]
So at a bond \(b\) of \(G\), \(\xi_b^3|\mathsf j(b)-\operatorname{Ad}(g)\mathsf j^\square(b)|\le C_De^{-\theta'D_b}(\varepsilon_H+\|\mathbf H\|_X+\|\mathbf H^\square\|_X)\). The removed current carries the boundary exponential and is proportional to the response amplitude. Both anchors, both actions, both row sets, both lifts and the node transport are included.

*Proof.* Work in the gauge of (H-pair), and write \(\delta\) for (original) minus (box). Rows and bonds of \(G\) with \(D>C_L\) are common to both systems. Quantities of one system at rows or bonds that the other lacks are bounded by that system's own estimates, and lie where \(w_G\le e^{\theta'C_L}\). Use the anchored form of `wf-room.md` (5.5):
\(\mathsf j=\mathsf j_1+\mathsf j_2+\mathsf j_3\), with
\(\mathsf j_1=R_{\mathbf H}K_{\mathbf H}^{\mathsf T}(\lambda-\lambda_0)\),
\(\mathsf j_2=R_{\mathbf H}(K_{\mathbf H}-K_0)^{\mathsf T}\lambda_0\) and
\(\mathsf j_3=(R_{\mathbf H}-1)K_0^{\mathsf T}\lambda_0\).

*Step 1 (anchors).* \(F'_{\mathbf U}(0)=D_{\mathbf U}^{\mathsf T}\mathcal F(\mathbf U)\) for the inner-plaquette action of each system (gate row 125, S5). So \(\lambda_0=(D_{\mathbf U}H)^{\mathsf T}\mathcal F\) and \(\lambda_0^\square=(D_{\mathbf U^\square}H^\square)^{\mathsf T}\mathcal F^\square\), where \(\mathcal F^\square\) vanishes off the box's inner plaquettes. On a common row \(c\),
\[
 \lambda_0-\lambda_0^\square=(D(H-H^\square))^{\mathsf T}\mathcal F+(D_{\mathbf U^\square}H^\square)^{\mathsf T}(\mathcal F-\mathcal F^\square)+((D_{\mathbf U}-D_{\mathbf U^\square})H^\square)^{\mathsf T}\mathcal F .
\]
The first term is bounded by (3.2), since \(\xi^2|\mathcal F|\le C\alpha_0\). For the second, \(\xi_p^2|\mathcal F-\mathcal F^\square|(p)\) is \(\le Cx_p\le C\varepsilon_Pe^{-\theta_PD_p}\) on common plaquettes (F2). It is \(\le C\alpha_0\) on plaquettes of one action only, which lie where \(D_p\le C_L\). Apply (O1) for \(H^\square\) with weight \(w_G\in\mathcal W_{\theta'}\) (Theorem B(c), \(\theta'\le\tau_L/8\)). The third term is (F2) and (O1). Hence \(\|\lambda_0-\lambda_0^\square\|_{Y,w_G}\le C(C_*+C_H)(\alpha_0+\varepsilon_P)\). The derivative was moved onto the lift before estimating, as the gate requires. A staggered real part has \(|J(\mathbf U)|\) up to \(C\alpha_0\eta^{-1}\xi^{-2}\) (SA 10531), and the two actions' currents differ by that much at the box boundary. A bound through \(J\) would therefore lose \(\xi/\eta\), and the integrated form does not.

*Step 2 (multipliers).* By (6.2) of `wf-room-2.md`, \((1+T^{\mathsf T})(\lambda-\lambda_0)=\Phi\) with
\(\Phi=(DH)^{\mathsf T}D\mathbf H+H^{\mathsf T}\mathcal N(\mathbf H)-T^{\mathsf T}\lambda_0\), and likewise for the box. On common rows, subtracting the two equations gives
\[
 \mu:=\delta(\lambda-\lambda_0)=\delta\Phi-\big[T^{\mathsf T}(\lambda-\lambda_0)-T^{\square\mathsf T}(\lambda^\square-\lambda_0^\square)\big],
\]
where \(T^{\mathsf T}\nu-T^{\square\mathsf T}\nu^\square=(H-H^\square)^{\mathsf T}(K_{\mathbf H}-K_0)^{\mathsf T}\nu+H^{\square\mathsf T}[(K_{\mathbf H}-K_0)-(K^\square_{\mathbf H^\square}-K^\square_0)]^{\mathsf T}\nu+H^{\square\mathsf T}(K^\square_{\mathbf H^\square}-K^\square_0)^{\mathsf T}(\nu-\nu^\square)\). The last term is \(T^{\square\mathsf T}_G\mu\), the box operator applied to \(\mu\) extended by zero off common rows. Its norm in \(Y_{w_G}\) is \(\le CC_H\|\mathbf H^\square\|_X\le1/4\), by the gate's localized product estimate (row 125, S5: weight on the multiplier) and (O1) with weight \(w_G\). Rows where only one system lives contribute source terms bounded by (6.3) of that system, at \(w_G\le e^{\theta'C_L}\). So \(\|\mu\|_{Y,w_G}\le\frac43\|\text{source}\|_{Y,w_G}\). The source terms:
- \((D(H-H^\square))^{\mathsf T}D\mathbf H\) and \((H-H^\square)^{\mathsf T}\mathcal N(\mathbf H)\): by (3.2), at most \(C_*K(1+\alpha_0)\|\mathbf H\|_X\);
- \((D_{\mathbf U^\square}H^\square)^{\mathsf T}D(\mathbf H-\mathbf H^\square)\): (O1) with weight \(w_G\) gives \(\le C_H\varepsilon_H\);
- \(((D_{\mathbf U}-D_{\mathbf U^\square})H^\square)^{\mathsf T}D\mathbf H\), \(H^{\square\mathsf T}(\mathcal N(\mathbf H)-\mathcal N^\square(\mathbf H^\square))\), and the curl difference on \(\mathbf H\): by (F1), (F2) and (O1), at most \(C_H(\alpha_0+r)(\varepsilon_H+\varepsilon_P\|\mathbf H\|_X)\), plus terms supported at \(D\le C_L\) bounded by \(C_H(\alpha_0+r)(\|\mathbf H\|_X+\|\mathbf H^\square\|_X)\);
- \(-\delta(T^{\mathsf T}\lambda_0)\): the same splitting as above with \(\nu=\lambda_0\), giving \(C_*K\|\mathbf H\|_X\|\lambda_0\|_Y+C_H(\varepsilon_H+\varepsilon_P\|\mathbf H\|_X+\|\mathbf H^\square\|_X\mathbf 1_{\partial})\|\lambda_0\|_Y+CC_H\|\mathbf H^\square\|_X\|\lambda_0-\lambda_0^\square\|_{Y,w_G}\);
- the first two terms of the \(T\)-difference with \(\nu=\lambda-\lambda_0\): (3.2) and (K1), with \(\|\lambda-\lambda_0\|_Y\le CC_H(1+C_H\alpha_0)\|\mathbf H\|_X\) by (6.3).

With \(\|\lambda_0\|_Y\le CC_H\alpha_0\) and Step 1, this gives \(\|\mu\|_{Y,w_G}\le C_D'(\varepsilon_H+\|\mathbf H\|_X+\|\mathbf H^\square\|_X)\).

*Step 3 (readout).* \(\delta\mathsf j_1=R_{\mathbf H}K_{\mathbf H}^{\mathsf T}\mu+[R_{\mathbf H}K_{\mathbf H}^{\mathsf T}-R_{\mathbf H^\square}K^{\square\mathsf T}_{\mathbf H^\square}](\lambda^\square-\lambda_0^\square)\). The first part is \(\le C\|\mu\|_{Y,w_G}\), by (5.1) with the weight on the multiplier. The second is (K1) and (R1) times \(\|\lambda^\square-\lambda^\square_0\|_Y\le CC_H\|\mathbf H^\square\|_X\). Next, \(\delta\mathsf j_2\) and \(\delta\mathsf j_3\) are, term by term, (R1), (K1) times \(\|\lambda_0\|_Y\), plus \(C\|\mathbf H^\square\|_X\|\lambda_0-\lambda_0^\square\|_{Y,w_G}\) (product estimate with the weight on the multiplier). Every term is at most \(C_D(\varepsilon_H+\|\mathbf H\|_X+\|\mathbf H^\square\|_X)\) in \(F_{w_G}\). For the node transport, \(\mathsf j^\square\) is covariant (S3 of `wf-room-2.md`, and gauge covariance of \(H^\square(s)\), Theorem B(a)). So the readout in the original gauge is \(\operatorname{Ad}(g)\) of the one computed here. Moreover \(\xi^3|(\operatorname{Ad}(g)-1)\mathsf j^\square|\le C\varepsilon_Pe^{-\theta_PD}\cdot C\|\mathbf H^\square\|_X\) by (6.4), which is in the bound since \(\theta_P\ge\theta'\). \(\square\)

**What this settles, and what it reads.** Defect 2 of the gate is answered at the level it asks. The removed current's comparison now includes the second anchor term \((H^\square)^{\mathsf T}(F'_U(0)-F'_{U^\square}(0))\), in integrated form. It also includes the change of action, the change of rows, the chart conversions and the node lifts. No common segment is assumed, and none of `wf-room.md` (5.6)'s fixed-background hypotheses is used. Label: **implication** from Theorems A–C, Lemma K, and the two inputs:
- (H-pair) for the box background: (1b) Theorem 6(c) for the box localisation. The library has 6(c) for the meets of 2.8 (`meet-6c.md` Theorem M, gated row 106) and for localisations (`a3-derivative.md` §10, gated row 89). The box localisation of the window is a further instance; it is not re-checked here.
- (H-field) for the response, \(\|\mathbf H-\mathbf H^\square\|_{X,w_G}\). It follows from the R9 contraction in weighted norms once the other decoupled operators (\(H_1(s)\), \(\mathfrak G(s)\)) satisfy the analogue of (3.1). The same walk-term argument gives that analogue from their expansions (`h-walk.md` Theorem T, Corollary T as repaired by its gate). The contraction itself needs the first system's own decoupled field bounds in the norms \(\|\cdot\|_\varpi\) (§5). That is not done here.

**Counterexample attempts (done first).**
- (a) *The two actions' currents at the box boundary* (a staggered real part, SA 10531). They differ by up to \(C\alpha_0\eta^{-1}\xi^{-2}\), which would break any bound through \(J\). It does not break Step 1, because the anchor is integrated against \(D H\). This is the reason for the gate's instruction "transfer derivatives … to the corresponding lift".
- (b) *A walk hugging the box boundary from a deep row to a deep bond.* Its pair difference is not small near the boundary, but its length is at least \(D_y+D_c-2\delta_\omega\). It is paid in the split of Theorem C. No failure.
- (c) *Different row sets near the boundary.* Then \(T\) and \(T^\square\) act on different spaces, so the global telescoping \(M^{-1}-(M^\square)^{-1}\) is not available as written. It is replaced by the equation for \(\mu\) on common rows (Step 2). No failure.
