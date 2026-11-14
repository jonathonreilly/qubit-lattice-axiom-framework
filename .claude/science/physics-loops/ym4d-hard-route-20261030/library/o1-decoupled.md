lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T17:43Z

# o1-decoupled: R9's current-corrected lift and (O1), the removed-map comparison, hereditary admission of the inner Landau map (queue row 126)

Pinned at 533faafc0 (branch claude/ym4d-hard-route). Research-stage working state; no status, not an audit. Written section by section.

Moves: `sa-ledger.md` rank 4 (WF substitution room, SA L15879), where it stops after `gates/wf-room-2-gate.md` (§§0, 6.3, 7.3, 8).

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Same-provider work, ungated. It reads Claude text (`h-walk.md`, `a2-layers.md` §7, `wf-room-2.md`, `a3-clauses.md`) and Codex text (`wf-room.md`, and the gates of rows 92, 120, 125, which are Codex's). Outline: Sussman–Alpoge `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (sha256 `d7f77d4d…4d6f`, the same file as rows 103–125), not copied here; SA numbers are its lines. No numeric job was run. Every step is written by hand.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the operators \(\mathsf G_0,\mathsf G,\mathsf H\) and the current continuation \(\Delta'_\pi\) (SA 10142–10192), the decoupled response (R9) (SA 5762–5790, 10356–10415), mechanisms (f), (i), (j) (SA 10540, 10552, 10562), the window maps (WF1)–(WF7) and (OA7). T. Balaban for the method: random-walk expansions from local inverses on cut-down sequences (CMP 99b pp. 408–410), decoupling parameters paid by length with the leftover \(e^{16\bar\kappa}\) (CMP 116 p. 5, as the outline cites it), and the hereditary-domain argument of CMP 109. Claude for `h-walk.md`, `a2-layers.md`, `wf-room-2.md`; OpenAI Codex for `wf-room.md` and for the gate repairs used here.

## 0. Result

Status: finished 2026-11-03 (worker). Same-model and ungated; a cross-provider gate is needed. All three parts of row 126 are proved as implications from gated or named inputs. No counterexample was found.

- **(1) R9's lift and (O1).** R9's current-corrected lift is the \(A\nu\) block of `h-walk.md`'s unfolded inverse at coefficient \(j=0\) (Lemma U, gated). It is not the P82° lift. They differ by \((1+T^\circ E_{\mathbf J})^{-1}\).
  - *Theorem A, \(s\equiv1\).* (O1) holds on the general complex, independent-current pair domain. Lemma L's local energy decay of a column gives the weighted column sums by Cauchy–Schwarz on each pillar.
  - *Theorem B, \(|s_\Delta|<e^{\bar\kappa}\).* (O1) holds with \(C_H=C_LB_Le^{16\bar\kappa}\), for the decoupled lift specified from Theorem W's walk expansion (Definition D), uniformly in depth. Lemma P proves the outline's mechanism (i) with explicit constants, under a stated hypothesis on the parameter cubes. Lemma WC gives the splitting.
- **(2) Removed-map comparison.**
  - *Theorem C.* The decoupled lifts of the original and box systems differ by \(e^{-\theta'(D_y+D_c)}\) in the distance to the complement of their agreement region. The proof is a term identity for walks that stay inside the region (Lemma C1, which proves the needed instance of the (C5) repair), plus a Cauchy estimate in the pair.
  - *Theorem D.* The removed current carries that factor and is proportional to the response amplitude. Changed anchors (integrated against \(DH\), never through \(J\)), actions, rows, chart conversions, lifts and node transports are all included.
  - Inputs left: 6(c) for the box localisation at complex data (it is gated at real data), the node-lift clause for Landau representatives, and the response comparison (H-field).
- **(3) Hereditary admission of the inner Landau map.**
  - *Lemma RI.* This is (1b) Theorem 6(b) on the complex datum disc, with its node lift \(g_Z\): explicit, holomorphic, of condition number \(\le e^{C_g\sup|B|}\). It follows from the gated real restriction identity (9.3) and the identity theorem, as in Balaban CMP 109 (3.38).
  - *Theorem I.* Every tower clause (R6), at every \(Z,p,n\) and for both rules, follows from the inner configuration's own level-\(j\) curvature and current bounds, with no \(K^\sharp\) loss. §4.5 writes the actual inequalities and the order of choice; the gate's "\(C\sqrt{1+m}L^{-2m}\le1/4\)" becomes \(L^2\ge6\sqrt2\lambda_a\).
- **Where rank 4 now stops:** the first system's own decoupled field bounds. These are the first-line (sup-norm) bounds \(\widehat b\) for \(H(s),H_1(s),\mathfrak G(s)\), which need a pointwise upgrade of the walk terms (§5, item 1). After them come 6(c) for the box localisation and the Landau node-lift comparison.

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

**Consequence.** The gate's first failing step (row 125, Defect 1: "(O1) at \(s=1\) is not given by the cited P82° for the specified lift") is replaced by Theorem A. (O1) now holds for **R9's own** current-corrected lift on the general complex, independent-current pair domain, uniformly in depth. The gate's partial repair, for the P82° lift at a reduced rate, is no longer needed. This is the repair the gate asked for, in its own terms. First, the \"uniform bound on the current-corrected Hessian perturbation, including the transpose in \(\Delta'_\pi\)\" is `a2-layers.md` (7.2): \(|\langle A,\Delta'_\pi[\mathbf J]C\rangle|\le C_7\gamma_0\|A\|_X\|C\|_X\), complex form in its §7.6(c). Being a bound on a bilinear form, it controls the operator and its transpose at once. Second, the \"resolvent argument identifying the resulting constrained lift\" is Lemma U(c) with Lemma L. The specification (6.1) and the gate's corrected (S5) estimates of `wf-room-2.md` §6.3 read (O1) as stated, with \(C_H=C_H^{(1)}\). Label: **implication**, from gated inputs (Lemma U, Lemma L with its repair) and the conditional premise (I1).

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
- **(H-pair)** On \(G\), \(\mathbf U^\square=(e^{i\eta X}\mathbf U)^g\) and \(\mathbf J^\square=\operatorname{Ad}(g)(\mathbf J+\delta\mathbf J)\), for a gauge transformation \(g\) (complex, holomorphic in the data, with bounded condition number) and
\[
 \|\delta P\|(x):=\xi_x|X(x)|+\xi_x^2|\nabla_{\mathbf U}X(x)|+\xi_x^3|\delta\mathbf J(x)|\le\varepsilon_Pe^{-\theta_PD_x}.
\]
  Here \(\varepsilon_P\le c_Pa_{\min}\), \(a_{\min}=\min\{\alpha_0,\alpha_1,\gamma_0\}\), and \(P\) satisfies the class inequalities with half the ceiling.
- **(H-node)** In the **assigned** representatives of the two maps (their node and gauge conventions, SA 15955), \(|g(x)-\mathbf 1|\le\varepsilon_Ne^{-\theta_PD_x}\) on \(G\). (H-pair) alone allows any \(g\). (H-node) is needed only to compare the readouts in their own representatives rather than in a common gauge.
- **(H-field)** \(\varepsilon_H:=\sup_{b\in G}w_G(b)\max\{\xi_b|\mathbf H-\mathbf H^\square|,\xi_b^2|\nabla(\mathbf H-\mathbf H^\square)|\}\), with \(\mathbf H^\square\) in the gauge of (H-pair).
- **(Box)** \(S^\square\) is a separated sequence with cube size \(M_1\) and gap \(\ge\rho\). For instance, take the cut-down of `h-walk.md` Lemma C with \((M_1,\rho)\) in place of \((M',\rho')\), on a box large enough for its nested enlargements. \(P^\square\) is a regular pair for \(S^\square\) below the ceiling.
- **(Spec)** Both systems use Definition D, with the same partition \(\mathcal P\) and the same parameters \(s\). The comparison is between two **specified** maps, as SA 5775–5783 allows. A compatible choice is part of the box map's specification, in the way the outline calls for a "compatible boundary comparison" (SA OA7 paragraph).

When the box response is taken at the same pair restricted, as in "replacing the original response by its box version", (H-pair) and (H-node) hold with \(X=0\), \(\delta\mathbf J=0\), \(g=\mathbf 1\). When the background is replaced too, (H-pair) is the localisation estimate (1b) Theorem 6(c) (SA 9779–9787: "two backgrounds whose sequences and whose data coincide on \(W\) differ there to this extent"), with \(\theta_P=\delta_W\) and \(\varepsilon_P=C_\mu\varepsilon_1\). Its current member \(\xi^3|D^*Df|\) bounds the removed **background** current directly, so no readout formula enters there. 6(c) fixes its gauge \(w\) only at the tops away from the collars (\(w=v_q[f]^{-1}\), within \(C|f|\) of \(\mathbf 1\)) and leaves it free elsewhere. So (H-node) is a property of the assigned representatives, not of 6(c). For representatives in axial gauge outside common nodes, it follows from the node values by the recursive formula of [AX], with the condition-number estimate of Lemma RI below. For Landau representatives it needs a comparison of the two Landau factors, which is not done here.

### 3.2 Term identity and the operator comparison

**Lemma C1 (term identity).** Assume (H-seq). Let \(\omega\) be a walk of \(S\) with \(\kappa_i^{(4)}\subset G\) for every \(i\). Then \(\omega\) is a walk of \(S^\square\). Its factors \(\tilde h_{\kappa_i},\theta_{\kappa_i}\), its cut-down sequences \(S^{\kappa_i}\), and its commutator stencils are the same for both systems. Hence \(T^\square_\omega\) and \(T_\omega\) are the same holomorphic function on the local class on \([\![\omega]\!]\), evaluated at \(P^\square|_{[\![\omega]\!]}\) and \(P|_{[\![\omega]\!]}\) respectively.

*Proof.* A cube \(\kappa'\) is in \(K_i\) iff it is a level-\(i\) \(M_1\)-cube contained in \(\overline{\mathcal L_i}\). Here \(\kappa'\subset\overline{\mathcal L_i}\) is decided by \(\Omega_i,\Omega_{i+1}\) on \(\kappa'\). The cutoffs \(\tilde h_\kappa,\phi_\kappa\) depend only on \(\kappa\). The normalisation of \(\theta_\kappa\) sums \(\phi_{\kappa'}\) over the cubes with \(\operatorname{supp}\phi_{\kappa'}\cap\kappa^{(1/4)}\ne\emptyset\). By the two-layer property, which holds in both sequences since both are separated with gap \(\rho\ge64LM_1\), these have \(\xi_{\kappa'}\in\{\xi_\kappa/L,\xi_\kappa,L\xi_\kappa\}\). Each lies within \(\ell^\infty\)-distance \(2LM_1\xi_\kappa\) of \(c_\kappa\), hence inside \(\kappa^\sharp\). Cubes of level \(\ge\) level\((\kappa)+2\) cannot be present near \(\kappa\) in either sequence: \(\Omega_{i+2}\) lies at distance \(>\rho\xi_{i+1}\ge64L^2M_1\xi_\kappa\) from \(\mathcal L_i\). Cubes of level \(\le\) level\((\kappa)-2\) cannot either: \(\Omega_{i-1}^c\) lies at distance \(>\rho\xi_{i-1}\ge64M_1\xi_\kappa\) from \(\Omega_i\). So the same candidate cubes, decided by the same regions, enter both denominators. This is the gate's repair of (C5) (`gates/h-walk-gate.md` §3), which is provable here because the two sequences agree on a fixed enlargement. The "absent candidate" problem cannot arise inside \(G^\sharp\). The cut-down \(S^\kappa\) is determined by \(\kappa\) and \(\Omega_i\cap\kappa^{(4)}\) (C1–C4, gated). The commutator \([\mathbb K,\tilde h_\kappa]=[\mathbb K_\kappa,\tilde h_\kappa]\) reads data within \(\kappa^{(5/2)}\). The rest is (C2), and Theorem W(c)'s field part, kept by the gate. \(\square\)

**Theorem C (operator comparison).** Assume the hypotheses of Theorem B for both systems (for the box system this uses (Box)), together with (H-seq), (H-pair) and (Spec). Put \(r'':=C_\sharp M_1\), the \(d_{\mathbf B}\)-diameter bound of \(\kappa^{(4)}\) plus \(4L\), with \(C_\sharp=C_\sharp(L)\). Put \(\theta':=\min\{\theta_P/2,\tau_L/16\}\). Take \(H^\square(s)\) at \((P^\square)^{g^{-1}}\), the common gauge of (H-pair). Let \(d_*(y,c):=\min\{d_{\mathbf B}(y,c),d^\square_{\mathbf B}(y,c)\}\), the smaller of the two sequences' metrics. Then, for every row \(c\) of \(G\) and pillar \(y\), with \(|s_\Delta|\le e^{\bar\kappa}\) and \(D_y=0\) for \(y\notin G\),
\[
 \|(H(s)-H^\square(s))(\cdot,c)\|_{E,y}\le C_*\,e^{-\theta'(D_y+D_c)}\,e^{-(\tau_L/16)d_*(y,c)},
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

*Inner walks.* By (H-pair), the pair on \([\![\omega]\!]\) is joined to \(P^\square\) (in the gauge \(g^{-1}\)) by \(P(t)=(e^{i\eta tX}\mathbf U,\mathbf J+t\,\delta\mathbf J)\). Its real factor \(U\) is fixed, and its complex factor \(A'(t)\) is defined by \(e^{i\eta A'(t)}=e^{i\eta tX}e^{i\eta A'}\). Let \(\varepsilon_\omega:=\sup_{[\![\omega]\!]}\|\delta P\|\). For \(|t|\le R_\omega:=c\,a_{\min}/\varepsilon_\omega\), every class inequality holds on \([\![\omega]\!]\). The potential bounds use BCH with \(\eta|X|\le\varepsilon_\omega\). The curvature bound uses the local expansion \(\partial(e^{i\eta Y}\mathbf U)=(1+i\eta^2D_{\mathbf U}Y+O(\eta^2|Y|^2+\eta|Y||\partial\mathbf U-1|))\partial\mathbf U\) (SA 15884), with half the curvature ceiling free. The current bound is immediate, and the real gauge clause concerns \(U\) only. So \(t\mapsto T_\omega(P(t))F_{c,e}\) is holomorphic on \(|t|<R_\omega\), and bounded there by (6.2). (6.2) needs the pair only in the local class on each \(\kappa_i^{(4)}\): each factor is a local inverse on a cut-down inside \(\kappa_i^{(4)}\) (Lemma L, with (C4)'s local-class clause) or a commutator reading \(\kappa_i^{(5/2)}\). So no extension of \(P(t)\) beyond the hull is needed. Cauchy's estimate on the disc \(|t|\le R_\omega/2\) gives \(\|(T_\omega(P^\square)-T_\omega(P))F_{c,e}\|_{\mathcal X,y}\le(C\varepsilon_\omega/a_{\min})\,B_L(C_W/M_1)^ne^{-(\tau_L/2)d(\omega;y,c)}\xi_c\). Let \(\delta_\omega:=d_{\mathbf B}([\![\omega]\!],G^c)\). Then \(\varepsilon_\omega\le\varepsilon_Pe^{-\theta_P\delta_\omega}\). Any path from \(y\) to \(c\) meeting the cells comes within \(\delta_\omega+r''\) of \(G^c\), so \(d(\omega;y,c)\ge D_y+D_c-2\delta_\omega-2r''\). Split \((\tau_L/4)d(\omega;y,c)\ge(\tau_L/8)d(y,c)+(\tau_L/8)(D_y+D_c-2\delta_\omega-2r'')\), and use \(\delta_\omega\le\min\{D_y,D_c\}\). This gives
\(\theta_P\delta_\omega+(\tau_L/8)(D_y+D_c-2\delta_\omega)\ge\min\{\theta_P/2,\tau_L/8\}(D_y+D_c)\). If \(\theta_P\ge\tau_L/4\), the \(\delta_\omega\) terms have a nonnegative coefficient. Otherwise use \(\delta_\omega\le(D_y+D_c)/2\).

*Outer walks.* Some \(\kappa_i^{(4)}\not\subset G\). For \(i\ge1\), the path meets \(X_{\kappa_i}\) within \(r''\) of \(G^c\), so \(d(\omega;y,c)\ge D_y+D_c-2r''\). For \(i=0\), \(D_y\le r''\), and \(d(\omega;y,c)\ge d(y,c)\ge D_c-D_y\ge D_y+D_c-2r''\). Each family, original and box, is bounded by (6.2) and Lemma P separately, each in its own metric. The regions, hence the densities of the two metrics, agree on \(G\). So a box path from \(y\) to \(c\) that comes within \(r''\) of \(G^c\) also has box length \(\ge D_y+D_c-2r''\): its pieces inside \(G\) are measured alike. A box path that stays in \(G\) has box length \(\ge d_{\mathbf B}(y,c)\). Hence the box terms decay in \(d^\square(\omega;y,c)\ge d_*(y,c)\).

*Summation.* As in Theorem B(b), with \(|s^\omega|\le e^{16\bar\kappa}e^{(\tau_L/4)d(\omega;y,c)}\), at most \(N_L\nu_1^n\) walks of length \(n\) at \(y\), and \(\sum_n(\nu_1C_W/M_1)^n\le2\). The factor \(e^{\tau_Lr''}\) collects \(e^{2r''\tau_L/8}\), and \(\theta'\le\tau_L/16\) leaves \(e^{-(\tau_L/16)d(y,c)}\). This is (3.1).

(3.2) follows as in Steps 2–3 of Theorem A. For a pillar \(y\), \(|((H-H^\square)^{\mathsf T}f)(c)|\) receives at most \(2L^2\|(H-H^\square)(\cdot,c)\|_{E,y}\sup_{b\in y}\xi_b^3|f(b)|\). Multiply by \(w_G(c)=e^{\theta'D_c}\) and sum over \(y\), using \(\sum_ye^{-(\tau_L/16)d_*(y,c)}\le K_{\tau_L/32}+K^\square_{\tau_L/32}\). Both ball counts hold, since both sequences are separated with the same parameters; the constant \(K\) below means this sum. The curl is Step 2's covariant-difference bound. \(\square\)

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

**Theorem D.** Assume the hypotheses of Theorem C, the field ball \(\|\mathbf H\|_X,\|\mathbf H^\square\|_X\le r\) with \(CC_Hr\le1/4\), and (H-field). Let \(\mathsf j\) be the readout (6.1) of the original system. Let \(\mathsf j^\square_g\) be that of the box system computed at \((P^\square)^{g^{-1}}\), the common gauge of (H-pair), each with its own lift, field, rows, action and anchor. Then, on bonds of \(G\),
\[
 \|\mathsf j-\mathsf j^\square_g\|_{F,w_G}
 \le C_D\big(\varepsilon_H+\|\mathbf H\|_X+\|\mathbf H^\square\|_X\big),
 \qquad C_D=C_L\,C_*\,K_{\tau_L/32}\,(1+C_H)^2 .
 \tag{3.3}
\]
In the assigned representatives the box readout is \(\mathsf j^\square=\operatorname{Ad}(g)\mathsf j^\square_g\), by covariance. Under (H-node), \(\xi^3|(\operatorname{Ad}(g)-1)\mathsf j^\square_g|\le C\varepsilon_Ne^{-\theta_PD}\,C_H\|\mathbf H^\square\|_X\) by (6.4). So at a bond \(b\) of \(G\),
\[
 \xi_b^3|\mathsf j(b)-\mathsf j^\square(b)|\le\big(C_D+CC_H\varepsilon_N\big)e^{-\theta'D_b}\big(\varepsilon_H+\|\mathbf H\|_X+\|\mathbf H^\square\|_X\big).
\]
The removed current carries the boundary exponential and is proportional to the response amplitude. Both anchors, both actions, both row sets, both lifts and the node transport are included.

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

*Step 3 (readout).* \(\delta\mathsf j_1=R_{\mathbf H}K_{\mathbf H}^{\mathsf T}\mu+[R_{\mathbf H}K_{\mathbf H}^{\mathsf T}-R_{\mathbf H^\square}K^{\square\mathsf T}_{\mathbf H^\square}](\lambda^\square-\lambda_0^\square)\). The first part is \(\le C\|\mu\|_{Y,w_G}\), by (5.1) with the weight on the multiplier. The second is (K1) and (R1) times \(\|\lambda^\square-\lambda^\square_0\|_Y\le CC_H\|\mathbf H^\square\|_X\). Next, \(\delta\mathsf j_2\) and \(\delta\mathsf j_3\) are, term by term, (R1), (K1) times \(\|\lambda_0\|_Y\), plus \(C\|\mathbf H^\square\|_X\|\lambda_0-\lambda_0^\square\|_{Y,w_G}\) (product estimate with the weight on the multiplier). Every term is at most \(C_D(\varepsilon_H+\|\mathbf H\|_X+\|\mathbf H^\square\|_X)\) in \(F_{w_G}\). For the node transport, \(\mathsf j^\square\) is covariant (S3 of `wf-room-2.md`, and gauge covariance of \(H^\square(s)\), Theorem B(a), continued to complex \(g\) near the unitary group by the identity theorem as in `a3-clauses.md` §3 Step 2(iii)). So \(\mathsf j^\square=\operatorname{Ad}(g)\mathsf j^\square_g\), and the last display follows from (H-node) and (6.4), since \(\theta_P\ge\theta'\). \(\square\)

**What this settles, and what it reads.** Defect 2 of the gate is answered at the level it asks. The removed current's comparison now includes the second anchor term \((H^\square)^{\mathsf T}(F'_U(0)-F'_{U^\square}(0))\), in integrated form. It also includes the change of action, the change of rows, the chart conversions and the node lifts. No common segment is assumed, and none of `wf-room.md` (5.6)'s fixed-background hypotheses is used. Label: **implication** from Theorems A–C, Lemma K, and the two inputs:
- (H-pair) for the box background. The box-background map is 6(c)'s single-part localised background (SA 9784: \"the problem posed on the tower of the part, with values taken from the lift of \(V\)\"). At **real** data, (H-pair) is `a3-derivative.md` Lemma 10.1 (gated row 89), with \(\theta_P=\delta_0/8\) and \(\varepsilon_P=Ce^{\theta(c_1\mu+D_L)}\varepsilon_1\). Its premise (G1) is discharged for Definition A collars by `a3-close.md` Lemma J and `assign-adopt.md` (gates rows 106, 114). At **complex** data on the window's analytic domain, which the removed substitutions use, Lemma 10.1 is not stated. Its proof is a weighted contraction around a real critical reference, and it would need Theorem P\(^{\mathsf c}\) in place of P82°. This is not done here.
- (H-field) for the response, \(\|\mathbf H-\mathbf H^\square\|_{X,w_G}\). It follows from the R9 contraction in weighted norms once the other decoupled operators (\(H_1(s)\), \(\mathfrak G(s)\)) satisfy the analogue of (3.1). The same walk-term argument gives that analogue from their expansions (`h-walk.md` Theorem T, Corollary T as repaired by its gate). The contraction itself needs the first system's own decoupled field bounds in the norms \(\|\cdot\|_\varpi\) (§5). That is not done here.

**Counterexample attempts (done first).**
- (a) *The two actions' currents at the box boundary* (a staggered real part, SA 10531). They differ by up to \(C\alpha_0\eta^{-1}\xi^{-2}\), which would break any bound through \(J\). It does not break Step 1, because the anchor is integrated against \(D H\). This is the reason for the gate's instruction "transfer derivatives … to the corresponding lift".
- (b) *A walk hugging the box boundary from a deep row to a deep bond.* Its pair difference is not small near the boundary, but its length is at least \(D_y+D_c-2\delta_\omega\). It is paid in the split of Theorem C. No failure.
- (c) *Different row sets near the boundary.* Then \(T\) and \(T^\square\) act on different spaces, so the global telescoping \(M^{-1}-(M^\square)^{-1}\) is not available as written. It is replaced by the equation for \(\mu\) on common rows (Step 2). No failure.

## 4. Item (3): hereditary restriction and datum transport for the inner Landau map

### 4.1 What is owed, and Balaban's mechanism

The gate's Defect 4: the endpoint estimate (7.2) bounds curvature and current at the chosen elements, but it "does not check every subdomain and truncation, the restriction identity with its prescribed gauge, or all simple potential/gradient bounds on the independent \(B'\) disc". The gate's repair is to prove, for each lower tower, the restriction/background identity with its node lift, to bound that lift on the whole disc, and to transfer the generated background's bounds to that tower.

Balaban does exactly this in CMP 109, pp. 277–280 (the scan was read for this note). His space \(U^c_j(X,\alpha_0,\alpha_1)\) (p. 262, (1.10)–(1.16)) has the hereditary condition (iv). The backgrounds \(U_n(M^\cdot(\mathbf U))\) of the averages of \(\mathbf U\), for the subsequences \(\{\Omega_0,\dots,\Omega_n\}\) of maximal domains on \(X\), obey \(|\partial U_n-1|<\alpha_0\xi^2\) and \(|J_n|<\alpha_0(L^n\xi)^2\) on \(\tilde X^{-2}\). For the inner configuration \(\exp i\xi\mathbf H_j(\square_0,\cdot)\), his identity (3.38) reads
\[
 U_n(X,M^\cdot(\exp i\xi\mathbf H_j(\dots)))=(\exp i\xi\mathbf H_j(\dots))^{u_j(\bar u_j)^{-1}},
\]
with \(\bar u_j\) block-constant. "This identity and the bound on \(u_j\) in (3.37) imply that the condition (iv) is a consequence of the condition (iii), with a bit better constant" (p. 278). He then bounds the endpoint ((3.39)–(3.42)), interpolates in \(\tau\) ((3.43)–(3.47)), and adds \(B'\) under \(2B_3\alpha_3\le\beta L^{-2}\alpha_0\) ((3.48)–(3.52)). "The condition (iv) follows from the corresponding identity (3.38)" (p. 280). Lemma 4 (3.53) states the result.

In the outline's terms, (iv) is the tower clause (R6) (SA 5697–5716), and (3.38) is (1b) Theorem 6(b) (SA 9776–9778). The library has Theorem 6(b) at real critical fields: `a1-balaban.md` §9.2, (9.3), proved by extending constraint-preserving variations and gated ADVANCE (`gates/a1-balaban-gate.md` §6). `a3-close.md` Lemma T used it at a real reference. What is new here is its use at the **complex** inner datum, its node lift, and the order of constants.

### 4.2 Setting and inputs

Let \(\square_0\) be the box of SA Theorem 5(c), and \(\mathbf B'_0\) its tower (first rule) cut at depth \(j\), with members \(T'_q(\square_0)\). Let \((\mathcal H,u)\) be Theorem 3's Landau pair over \(\mathbf V_0=\mathbf 1\) for \(\mathbf B'_0\), so \(\Phi(B)=(e^{i\eta_j\mathcal H(B)})^{u(B)}\). The **inner Landau map** is
\[
 B\longmapsto P_{\rm in}(B):=\big(\mathbf 1,\ \mathcal H(B),\ J(\mathbf U_{\rm in}(B))\big),\qquad \mathbf U_{\rm in}(B):=e^{i\eta_j\mathcal H(B)} ,
\]
read as `wf-room-2.md` §7.4 and SA 5(c) state it. Let \(X\) be a domain with \(X\subset T'_j(\square_0)\) ("the domains well inside \(\square_0\)", SA 5(c)). All lengths are in level-\(j\) units.

Inputs, with their labels:
- [Φ] `a3-derivative.md` Theorem 4 first paragraph and (31), 7.6, at \(U_0=\mathbf 1\). \(\mathcal H,u\) are holomorphic on \(\sup|B|<r_{\rm B}\), real at real \(B\), with \(\|\mathcal H(B)\|_X\le C_{\mathcal H}\sup|B|\) and \(|u-\mathbf 1|\le C\sup|B|\). Gated (row 89). At \(U_0=\mathbf 1\) its premises P81, P82° reduce to the flat package (rows 95, 99).
- [9.3] The restriction identity at real regular critical fields, for a separated subsequence \(\Omega'_q\subset\Omega_q\). Gated.
- [AX] The canonical representative is fixed by the explicit recursive axial gauge outside the nodes, with conjugator bound \(\exp(C\|B\|/(1-L^{-1}))\) (`a1-balaban.md` 9.1). Gated.
- [A′] `wf-room-2.md` Lemma A′ at the identity: \(|\log M_{\mathbf B'}(e^{i\eta A})(c)|\le2L\xi'_c\sup|A|\) on a tower. Gated ADVANCE, conditional (row 125, §4.2).
- [E] The endpoint: \(\|B_{\rm end}\|\le C_BM\alpha_0\tau\) and \(\|f(B_{\rm end})\|\le(1+\beta)a\tau^2\), \(\tau=L^{-(k+1-j)}\), in the Landau representative over \(\mathbf 1\) (`wf-room-2.md` Lemmas N, E, with the gate's §7.2 repair of N; endpoint ADVANCE, row 125 §7.3). Here \(a\) is the level-\((k+1)\) tower-clause radius of the input.
- [7.1] `wf-room.md` (7.1) (Codex). Its proof was re-checked here: a one-variable Schwarz expansion of \(z\mapsto f(zB)\) bounds the terms of degree \(\ge2\) by \(2Ct^2\|B\|^2/r_{\rm B}\), and a Cauchy derivative bound of \(3C\) on the \(3r_{\rm B}/4\)-ball handles \(B'\). No failure.
- [DA] Definition A towers are nested sequences of subsets of their base set, separated, with erosion depth \(e_q\le3M_1'\xi'_q\) (`assign-adopt.md` Lemma A; gate row 114 with its repairs).

### 4.3 Lemma RI: the restriction identity on the complex disc

**Lemma RI.** There are \(r_{\rm I}=r_{\rm I}(L)>0\) and \(C_g=C_g(L)\) such that the following holds for every \(Z\subset X\) of level \(p\le j\), every erosion rule, and every \(1\le n\le p\). Let \(\mathbf B'_Z\) be the tower of \(Z\) cut at depth \(n\). Then, for every complex \(B\) with \(\sup|B|<r_{\rm I}\):
- (a) The tower configuration \(U_n(Z;P_{\rm in}(B))\) of (R5) exists in its continuation domain.
- (b) \(U_n(Z;P_{\rm in}(B))=\big(\mathbf U_{\rm in}(B)|_{T'_0(Z)}\big)^{g_Z(B)}\), where \(g_Z(B)\) is the residual gauge transformation, equal to \(\mathbf 1\) at the nodes of \(\mathbf B'_Z\), defined by the recursive axial formula of [AX] applied to \(\mathbf U_{\rm in}(B)|_{T'_0(Z)}\). It is holomorphic in \(B\), unitary at real \(B\), and \(|g_Z|\,|g_Z^{-1}|\le e^{C_g\sup|B|}\).

*Proof.* (a) For \(P_{\rm in}\) the real factor is \(\mathbf 1\), so (R5) reads \(U_n(Z;P_{\rm in}(B))=\Phi^Z_{\mathbf 1}(B_Z)\) with \(B_Z=\frac1i\log M_{\mathbf B'_Z}(\mathbf U_{\rm in}(B))\). On \(X\subset T'_j(\square_0)\), the local scale of \(\mathbf B'_0\) is \(\xi_j=1\), and \(\sup|\mathcal H(B)|\le C_{\mathcal H}\sup|B|\). The tower of \(Z\) has scales \(\xi'\le\xi_j\). So [A′] (with \(U=\mathbf 1\), for which its hypothesis (H) is trivial) gives \(\sup|B_Z|\le2LC_{\mathcal H}\sup|B|\) on the determining rows. Theorem 3's continuation radius \(r_{\rm B}\) is uniform over separated sequences above the floors, so (a) holds once \(2LC_{\mathcal H}r_{\rm I}<r_{\rm B}/2\).

(b) *Real \(B\).* For real \(B\) with \(\sup|B|<r_{\rm I}\), \(\Phi(B)\) is the real regular critical field of the \(\mathbf B'_0\)-problem at the datum \(e^{iB}\), and \(\mathbf U_{\rm in}(B)=\Phi(B)^{u(B)^{-1}}\) with \(u(B)\) real.

*Nesting.* For \(q\le n\), [DA] gives \(T'_q(Z)\subset Z\subset X\subset T'_j(\square_0)\subset T'_q(\square_0)\). For \(q>n\), \(\mathbf B'_Z\) has no member. So \(\mathbf B'_Z\) is a separated subsequence of \(\mathbf B'_0\) in the sense of [9.3].

*Datum radius.* The datum of the restriction is \(CL^2\sup|B|\)-regular (the converse bound of Theorem 1), which is within the existence range for \(r_{\rm I}\) small. So [9.3] gives \(U_{\mathbf B'_Z}(M_{\mathbf B'_Z}(\Phi(B)|_{T'_0(Z)}))=\Phi(B)|_{T'_0(Z)}\) modulo \(\mathcal G^{\rm res}(\mathbf B'_Z)\).

*Covariance.* The averages are covariant with node values: \(M_{\mathbf B'_Z}(U^h)=M_{\mathbf B'_Z}(U)^{h|_{\rm nodes}}\) (SA (R3)). The variational problem is invariant under real gauge transformations. So for the real node gauge \(h=u^{-1}|_{\rm nodes}\), the orbit at the datum \(M_{\mathbf B'_Z}(\Phi|_Z)^h\) is the image of the orbit at \(M_{\mathbf B'_Z}(\Phi|_Z)\) under any extension of \(h\). Taking \(u^{-1}\) itself as the extension, \(\mathbf U_{\rm in}(B)|_{T'_0(Z)}\) lies in the regular critical orbit of the \(\mathbf B'_Z\)-problem at its own datum \(e^{iB_Z}\). The canonical representative of that orbit is \(\Phi^Z_{\mathbf 1}(B_Z)\), the unique element in axial gauge outside the nodes (SA Theorem 1; [AX]). The residual transformation reaching it from \(\mathbf U_{\rm in}|_{T'_0(Z)}\) is unique. It is given recursively: \(g=\mathbf 1\) at the nodes; at a non-node site \(x\) of level \(q\) with block centre \(z\), \(g(x)=g(z)\,(\mathcal M^q\mathbf U_{\rm in})(\Gamma_{z,x})\), so that the comb transports of the averages become \(\mathbf 1\). This proves (b) at real \(B\).

*Complex \(B\).* The left side \(\Phi^Z_{\mathbf 1}(B_Z(B))\) is a composition of holomorphic maps on \(\sup|B|<r_{\rm I}\): \(\mathcal H\), the averages and logarithms near \(\mathbf 1\), and \(\Phi^Z_{\mathbf 1}\) on its ball. The right side is holomorphic, since \(g_Z(B)\) is a finite product of comb transports of averages of \(\mathbf U_{\rm in}(B)\), each holomorphic near \(\mathbf 1\). The two sides agree on the real points, a totally real subspace of full dimension of the connected polydisc. The identity theorem gives (b) on the whole polydisc.

*Condition number.* The comb factors use level-\(q\) plain averages at bonds inside blocks, which need not be determining rows. So cite the bootstrap in the proof of [A′], not its statement. That bootstrap bounds every level-\(m\) bond of a carrier by its finer carrier, and gives \(|\beta_q(b)|\le2t_q\sup|w|\) for every level-\(q\) bond \(b\) whose carrier lies in the tower region, where \(\mathcal M^q(e^{i\eta w}\mathbf 1)(b)=e^{i\beta_q(b)}\) and \(t_q=L^{q-j}\) in level-\(j\) units. With \(w=\mathcal H(B)\), \(|\log\mathcal M^q(\mathbf U_{\rm in})(b)|\le2C_{\mathcal H}L^{q-j}\sup|B|\). A comb \(\Gamma_{z,x}\) has at most \(4L\) bonds. So each recursive factor has norm and inverse norm at most \(\exp(8LC_{\mathcal H}L^{q-j}\sup|B|)\), for complex \(B\) as well. The product down a pillar, over the levels \(q\le j\), has norm and inverse norm at most \(\exp(8LC_{\mathcal H}\sup|B|/(1-L^{-1}))\le\exp(16LC_{\mathcal H}\sup|B|)\). This gives \(C_g:=32LC_{\mathcal H}\). It is the estimate of [AX] in a1-balaban 9.1, with no product of fixed losses over the levels. \(\square\)

### 4.4 Theorem I: the inner triple lies in the hereditary core

Write \(\phi(B)\) for the pair of normalised quantities \((\eta_j^{-2}(\partial\mathbf U_{\rm in}(B)-\mathbf 1),\ J(\mathbf U_{\rm in}(B)))\) in level-\(j\) units, at the elements of \(X\), and \(|\phi|_X\) for its supremum.

**Theorem I.** Let \(\sup|B|<r_{\rm I}\), and suppose
\[
 \text{(i) } e^{C_g\sup|B|}\,|\phi(B)|_X<\alpha_{0,j},\qquad
 \text{(ii) } C_{\mathcal H}\sup|B|<\alpha_{1,j}.
\]
Then \(P_{\rm in}(B)\in\mathcal U^\circ_j(X;\alpha_{0,j},\alpha_{1,j},\alpha_{0,j})\). That is, the simple conditions (R4) hold. Every tower configuration of (R5), for every \(Z\subset X\) of every level \(p\le j\), both rules and every \(1\le n\le p\), exists in its continuation domain and satisfies (R6) for \(\mathbf U\) and for \(U\).

*Proof.* (R4). \(U=\mathbf 1\) has trivial plaquettes and real gauge \(A=0\). \(|\partial\mathbf U_{\rm in}-\mathbf 1|<\alpha_{0,j}\eta_j^2\) and \(|\mathbf J|=|J(\mathbf U_{\rm in})|<\alpha_{0,j}=a_2\) follow from (i). \(|A'|,|\nabla_UA'|\) are \(|\mathcal H|,|\nabla\mathcal H|\le\|\mathcal H(B)\|_X<\alpha_{1,j}\) by [Φ] and (ii).

(R6) for \(\mathbf U\). Fix \(Z,p,\) a rule and \(n\). By Lemma RI, \(U_n(Z;P_{\rm in})=(\mathbf U_{\rm in}|_{T'_0(Z)})^{g_Z}\). On \(Z\) with two layers of level-\((p-1)\) \(M\)-cubes removed, every bond has its six plaquettes inside \(T'_0(Z)\), whose erosion depth \(3M_1'\eta\) is much smaller than \(M\eta\) [DA]. So at a plaquette \(\mathfrak p\) based at \(x\), \(\partial U_n(\mathfrak p)-\mathbf 1=g_Z(x)(\partial\mathbf U_{\rm in}(\mathfrak p)-\mathbf 1)g_Z(x)^{-1}\). At such a bond, the current of the inner-plaquette action of \(T'_0(Z)\) is \(\operatorname{Ad}(g_Z(b_-))J(\mathbf U_{\rm in})(b)\). Both are bounded by \(e^{C_g\sup|B|}\) times the corresponding quantity of \(\mathbf U_{\rm in}\).

*Units.* The bare mesh in level-\(p\) units is \(\eta_p=L^{j-p}\eta_j\), so the curvature clause \(a_0L^{-(j-p)}\eta_p^2\) equals \(a_0L^{j-p}\eta_j^2\). A current in level-\(n\) units is \(L^{-3(j-n)}\) times its level-\(j\) value, so the current clause \(a_0L^{-(j-p)}L^{2(n-p)}\) in level-\(n\) units is \(a_0L^{2j-p-n}\) in level-\(j\) units. Both exponents are \(\ge0\), since \(n\le p\le j\). So every clause of (R6) is implied by \(e^{C_g\sup|B|}|\phi(B)|_X<\alpha_{0,j}\), which is (i). The same holds for the infinite list, with no \(K^\sharp\) loss: this is Balaban's "(iv) is a consequence of (iii)".

(R6) for \(U=\mathbf 1\). The tower configurations of \(\mathbf 1\) are \(\Phi^Z_{\mathbf 1}(0)=\mathbf 1\). \(\square\)

**Why no flux amplification (test C1 of `wf-room-2.md`).** C1 shows that a field obeying only the simple conditions can have tower configurations with \(L^{2(p-r)}\) times its curvature. \(\mathbf U_{\rm in}\) is not such a field. It is itself a background of a tower containing every \(\mathbf B'_Z\), and Lemma RI makes its tower configurations gauge copies of itself. This is why the inner map needs the restriction identity, and why a small-simple-radii admission (SA 5(a), with its \(K^\sharp\) loss) would not do the same job.

### 4.5 The actual inner datum, and the order of constants

Apply Theorem I to \(B=\varsigma B_{\rm end}+B'\), \(\varsigma\in[0,1]\), \(B'\) complex. By [E] and [7.1], with \(C_f\) the constant of \(\|f(B)\|\le C_f\|B\|\),
\[
 |\phi(B)|_X\le\big(1+\beta+4C_fC_B^2M^2a/r_{\rm B}\big)a\tau^2+3C_f\sup|B'| .
\]
**Constants.** Let \(m=k+1-j\ge1\), so \(\tau=L^{-m}\). By SA 5(c), the input radius is \(a\le\lambda_a\alpha_{0,k}\) for a fixed factor \(\lambda_a\). Under SA 5(c)'s flow hypothesis \(-C_x\le x_q-x_{q'}\le C_x(q'-q)\), take the running radii in the form (OA1), \(\alpha_{0,i}=c_\alpha x_i^{-1/2}(\log x_i)^q\) with one constant \(c_\alpha\), and couplings with \(x_k\ge\max\{C_x,e^2\}\). Then \(x_j/x_k\le1+C_x(k-j)/x_k\le m\), and the logarithmic factor contributes at most \(2\). So
\[
 \alpha_{0,k}\le2m^{1/2}\alpha_{0,j},\qquad a\tau^2\le2\lambda_am^{1/2}L^{-2m}\alpha_{0,j}\le2\sqrt2\,\lambda_aL^{-2}\alpha_{0,j},
\]
since \(m\mapsto(1+m)^{1/2}L^{-2m}\) is decreasing for \(L\ge2\) and \(m^{1/2}\le(1+m)^{1/2}\). This is the explicit form of the inequality "\(C\sqrt{1+m}L^{-2m}\le1/4\)" that the gate asks for.

Fix \(\beta=1/8\). Choose:
- the field ceiling \(4C_fC_B^2M^2\lambda_a\alpha_{0,k}\le\beta r_{\rm B}\) (radii after \(M\));
- \(\sup|B'|<c_{B'}\min\{\alpha_{0,j-1},\alpha_{0,j}\}\) with \(3C_fc_{B'}\le1/8\) and \(C_{\mathcal H}c_{B'}\le1/4\);
- the radii so small that \(C_g(C_BM\lambda_a\alpha_{0,k}+c_{B'}\alpha_{0,j})\le\log(1+\beta)\) and \(\sup|B|<r_{\rm I}\);
- \(L^2\ge3\cdot2\sqrt2\,\lambda_a\).

Then (i) of Theorem I holds:
\[
 e^{C_g\sup|B|}|\phi|_X\le\tfrac98\big(\tfrac54\cdot2\sqrt2\lambda_aL^{-2}+\tfrac18\big)\alpha_{0,j}\le\tfrac98\big(\tfrac{5}{12}+\tfrac18\big)\alpha_{0,j}<\alpha_{0,j}.
\]
For (ii), \(C_{\mathcal H}\sup|B|\le C_{\mathcal H}C_BM\lambda_a\alpha_{0,k}\tau+\alpha_{0,j}/4\). The first term is \(\le2C_{\mathcal H}C_BM\lambda_aL^{-1}\alpha_{0,j}\). Under the outline's radius relation \(M\alpha_0\ll\alpha_1\) (SA 9911: "\(\alpha_1'\ge c\alpha_1\) together with \(M\alpha_0\ll\alpha_1\), the relation that holds between the two radii in the application"), with \(\alpha_{0,j}\le\alpha_{1,j}\), it is below \(\alpha_{1,j}/2\).

The order is: \(L\) (with \(L^2\ge6\sqrt2\lambda_a\)), then the flat and background constants \(C_{\mathcal H},C_B,C_f,C_g,r_{\rm B},r_{\rm I}\), then \(M\), then the radii and couplings. Nothing depends on \(j,k\) or the depth. The \(m\)-dependence is absorbed by \(\sup_m\).

### 4.6 Datum transport and the node lift

The actual (WF4) pair at the raw datum is \(\Phi(\varsigma B_{\rm end}+B')^{\tilde v}\), whose current transforms with it. It is the complex gauge transform of the Landau triple's pair by \(u\cdot\tilde v\). By Lemma N as repaired by the gate (§7.2), the node factor \(v\) and \(B_{\rm end}\) are explicit holomorphic functions of \(\mathbf U|_{\square_0}\), with \(|v||v^{-1}|\le e^{CM\alpha_1}\), on the whole disc where the simple conditions hold. \(|u-\mathbf 1|\le C\sup|B|\) on the whole datum disc [Φ]. The identity of representatives on the complex first-order ball is the gate's §7.3, via the real slice and the identity theorem. Lemma RI supplies the remaining node lift, the one for each lower tower: \(g_Z\), equal to \(\mathbf 1\) at the tower's nodes, explicit, holomorphic, of condition number \(\le e^{C_g\sup|B|}\). So every gauge in the chain from the actual pair to each tower configuration is explicit, holomorphic on the whole independent datum disc, and bounded there.

**Verdict on item (3).** Defect 4 of the gate is repaired. Lemma RI is (1b) Theorem 6(b) on the complex disc, with its node lift. Theorem I proves hereditary admission of the inner Landau triple at every \(Z,p,n\) and both rules, uniformly. §4.5 writes the actual inequalities and the order of choice. Label: **implication**, from [9.3], [AX] and [Φ] (gated), [A′] and [E] (gated conditional, row 125), [DA] (gated with repairs, row 114), [7.1] (re-checked here), and SA 5(c)'s hypotheses: the flow bound, the input tower clause at level \(k+1\), \(X\subset T'_j(\square_0)\), and the radius relation \(M\alpha_0\ll\alpha_1\). Not covered: a layered \(X\) meeting several layers of \(\square_0\)'s tower. SA 5(c) does not use one, since it states the inner substitution at one level \(j\) well inside the box.

**Counterexample attempts (done first).**
- (a) *Flux amplification (C1).* Excluded for backgrounds by Lemma RI, as explained in §4.4. C1 used a field that is not a background of the tower.
- (b) *A second critical orbit at complex data.* The tower configuration is a specified branch, the continuation of the canonical representative, and the identity theorem propagates equality from the real slice. Other orbits are irrelevant. No failure.
- (c) *Non-unitary node factors (gate §7.4's flat example).* These concern the raw representative. Theorem I is about the Landau triple, whose real factor is \(\mathbf 1\). All non-unitarity sits in \(g_Z\), \(u\), \(\tilde v\), whose condition numbers are bounded. No failure.
- (d) *\(Z\) reaching the edge of \(X\).* (R6) is imposed only on \(Z\) minus two layers of \(M\)-cubes, where all six plaquettes of every bond lie in \(T'_0(Z)\). Nesting needs only \(Z\subset X\subset T'_j(\square_0)\). No failure.

## 5. Verdicts, what changes, what stays open

| Part of row 126 | Result | Where | Reads |
|---|---|---|---|
| (1) identify R9's lift | \(H=\mathsf H\mathsf m^{-1}\), \(\mathsf H=[\mathbb K^{-1}]_{A\nu}\) for the unfolded system at \(j=0\). It is the saddle lift of \(M_{\mathbf J}=\Delta^{\rm W}+DRD^{\mathsf T}-\Delta'_\pi[\mathbf J]\), and \(H=(1+T^\circ E_{\mathbf J})^{-1}H^\circ\) relative to P82° | §1.1 | Lemma U (gated) |
| (1) (O1) at \(s\equiv1\), general complex independent-current pairs | **implication** (Theorem A), \(C_H=C_LB_LK_{\tau_L/2}\), rates \(\le\tau_L/2\) | §1.2 | Lemma L (gated with repair), (I1) |
| (1) (O1) for \(\lvert s_\Delta\rvert<e^{\bar\kappa}\) | **implication** (Theorem B), with the specified expansion (2.1). \(C_H=C_LB_Le^{16\bar\kappa}K_{\tau_L/8}\), rates \(\le\tau_L/8\). Splitting and field-locality proved (Lemma WC). The cube count (mechanism (i)) proved (Lemma P) | §2 | Theorem W (a)–(b) (gated), (I1) on cut-downs, hypothesis (P) on \(\mathcal P\) |
| (2) removed-map comparison | **implication** (Theorems C, D): the operator difference and the removed current carry \(e^{-\theta'd_{\mathbf B}(\cdot,G^c)}\), with changed anchors (integrated against \(DH\)), actions, rows, chart conversions, lifts and node transport all included | §3 | Theorems A–B for both systems, Lemma K, (H-seq), (Box), (H-pair), (H-node), (H-field) |
| (3) hereditary restriction and datum transport | **implication** (Lemma RI, Theorem I): (1b) Theorem 6(b) on the complex disc with its node lift \(g_Z\), and hereditary admission at every \(Z,p,n\) and both rules, with no \(K^\sharp\) loss. Explicit order of constants (§4.5) | §4 | (9.3), [AX], [Φ] (gated); [A′], [E] (gated conditional); [DA]; SA 5(c)'s hypotheses |

**Defects found in the inputs (for the lead to forward).** At most these; none breaks a consumer.
1. `wf-room-2.md` line 331 (already WRONG per the gate). The right source of (O1) at \(s\equiv1\) is `h-walk.md` Lemma L, not P82°. The gate's partial repair through P82° is superseded by Theorem A.
2. `h-walk.md` Theorem W(c)–(d) (region-trace locality, WRONG per its gate). For two sequences that agree on a fixed physical enlargement \(G^\sharp\), the needed instance is proved here (Lemma C1). The general repair of (C5), with candidates absent in one sequence, is still open (row 123). Our chain reads only the instance.
3. SA mechanism (i) states "a tree of length \(t\) comes close to at most \(2^4\max\{1,Ct/\ell_{\mathsf P}\}\) cubes". This needs the parameter cubes to be large in **every** local unit (hypothesis (P)), for instance top-level cubes. If they were finer in finer layers, the count would fail. Lemma P proves the count under (P), with \(C=2^6\) and \(\ell_{\mathsf P}>8(16L^3M_1+4L)\).
4. SA 9911 / 5(c) state the potential clause of the inner substitution through "\(M\alpha_0\ll\alpha_1\)". §4.5 shows that this relation is genuinely used, through the factor \(M\) of \(\|B_{\rm end}\|\le C_BM\alpha_0\tau\). It is not implied by \(\alpha_0\le\alpha_1\), so it must be part of the radius rule.

**What changes elsewhere (for the lead to forward; no other file edited).**
- `wf-room-2.md` §6.3, (O1): proved at \(s\equiv1\) on the general pair domain (Theorem A), and for decoupled \(s\) with Definition D (Theorem B). Then (6.3)–(6.4), with the gate's corrected S5, hold on the whole decoupling polydisc, given the first system's field \(\mathbf H\) with its bounds. (S6) is replaced by Theorem D.
- `wf-room-2.md` §7.3 and the gate's Defect 4: the core conclusion is now proved (Theorem I), with the actual inequalities.
- `sa-ledger.md` rank 4: (O1) and the inner hereditary admission move from open to implication. The removed comparison moves to implication from the named inputs below.

**Where rank 4 now stops (hardest first).**
1. **The first system's own decoupled field bounds.** These are the existence and weighted first-response bounds of the R9 fixed point in the norms \(\|\cdot\|_\varpi\) (SA 10380–10404), which need the **first-line** (sup-norm) bounds \(\widehat b\) for \(H(s)\), \(H_1(s)\), \(\mathfrak G(s)\). (O1) gives the column half only. The walk terms are bounded here in local \(L^2\) (Theorem W). Their pointwise upgrade needs local elliptic regularity for the eight-unknown unfolded local models, including the current terms \(c_J\). The visible route is to rerun `p82-curved.md` §6 (Proposition 6.2) and `a3-clauses.md` Step 5 (Lemma 6.1′) on \(\mathbb K_\kappa\), with \(c_J\) as a Lemma 6.1′-type perturbation of size \(\gamma_0\). Not attempted. The same bounds give (H-field) through the weighted contraction and the analogue of (3.1) for \(H_1(s),\mathfrak G(s)\).
2. **(H-pair) at complex data:** (1b) Theorem 6(c) for the window's single-part box localisation is gated at real data (`a3-derivative.md` Lemma 10.1). Its complex form is needed and not done. The direct route reruns Lemma 10.1 at the complex reference \(U^\circ_W(\mathbf V)\), using the complex-pair response of `a3-clauses.md` §4 and Theorem P\(^{\mathsf c}\). It has to identify that response with the continued Landau pair on the physical locus, by the identity theorem in the reference datum. A two-constants (harmonic-measure) argument from the real slice would give the value member on thin complex discs. It does not control the derivative member \(\xi^2|\nabla X|\) that Theorem C's Cauchy step needs, so it is not a substitute.
3. **(H-node) for Landau representatives:** a comparison of the two Landau factors. For axial representatives with common nodes it follows from [AX] and the node values.
4. The nested-geometry premise (\(X\subset T'_j(\square_0)\), box sizes) and label-formation checks, unchanged from row 116.
