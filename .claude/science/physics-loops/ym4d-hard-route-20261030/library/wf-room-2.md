lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T16:13Z

# wf-room-2: the rest of the WF substitution room (queue row 116)

Pinned at 9faf010d6 (branch claude/ym4d-hard-route). Research-stage working state; no status, not an audit. Written section by section.

Moves: `sa-ledger.md` rank 4 (WF substitution room, SA L15879), from where row 113 stopped (`wf-room.md` Section 9).

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Same-provider work, ungated. It reads Codex text (`wf-room.md`, `a2-curved.md`, `a3-balaban.md`) and Claude text (`a3-close.md`, `a3-derivative.md` Sections 6.1-10, `assign-adopt.md`, `a3-clauses.md`). Outline: Sussman-Alpoge `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (sha256 `d7f77d4d...4d6f`, the same file as rows 103-110) and not copied here. SA line numbers refer to that file. No Balaban text was read in this session beyond what the cited library notes record. No numeric job was run. Every step is written by hand.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the window maps (WF1)-(WF7) and (OA1)-(OA12), the hereditary core (R4)-(R11), the substitution-room mechanism (SA 15879-15995), the first and second response systems (SA 10356-10465), (1b) Theorems 3-6 and the BGR24-27 joint Cauchy argument. T. Balaban (CMP 102, 109, 119) for the background, the domains of the effective actions and the radial-interpolation proof that `wf-room.md` Section 7 reconstructs. OpenAI Codex for `wf-room.md` (row 113), whose Sections 3-7 this note continues.

## 0. Result

(Filled in at the end.)

## 1. Inputs and their standing

| Label | Statement used | Where | Standing |
|---|---|---|---|
| (T4) | Theorem 4, first paragraph, on the whole datum polydisc: at a real critical reference \(U_0\) of a separated sequence \(\mathbf B\) (gap \(\ge\rho_0\), no inward bonds, above the floors) and every complex \(B\) with \(\sup|B|<r_{\rm B}\), the Landau pair \((a(B),u_B)\) of \(\Phi_{\mathbf V_0}(B)=(e^{i\eta a}U_0)^{u_B}\) has responses \(h=\partial_{e_c}a\), \(\delta J\), \(\dot u\) (at tops) with \(\xi_y|h|+\xi_y^2|\nabla h|+\xi_y^3|\delta J|+|\dot u(y)|\le Ce^{-\theta d_{\mathbf B}(y,y_c)}|e|\), \(\theta=\delta_0/8\); and \(\|a(B)\|_X\le C\sup|B|\), \(|u_B-\mathbf 1|\le C\sup|B|\) at tops | `a3-derivative.md` (31), (34), 7.3, 7.5, 7.6 | gated (row 89), conditional on P81, P82° (rows 91, 100, 101), F0 (row 99), \(U_0\in\) Reg (row 103, gate row 106) |
| (AX) | The canonical representative \(\Phi\) is fixed by the explicit recursive axial gauge: node values, then down each pillar, a contour of \(\Phi\) from parent to child equals its reference value; conjugators have norm and inverse norm \(\le\exp(C\sup|B|/(1-L^{-1}))\); \(r(\Phi(B))\le C(\varepsilon_1+\sup|B|)\) | `a1-balaban.md` 9.1, (9.2) | gated (row 91, positive finding (c)) |
| (AV) | Iterated-average bootstrap \(a_{m+1}\le(1+C\alpha t_m^2)a_m+Ct_{m+1}a_m^2\) and the curvature recursion (3.6) | `a1-balaban.md` 3.5; gate row 91 Section 1 | gated |
| (MS) | Mixed-scale counting: crossing a complete layer costs \(\rho\) in the weighted metric; local scales at weighted distance \(d\) differ by at most \(Le^{(\log L)d/\rho}\); at most \(C(R+1)^4L^{8+8R/\rho}\) cells within weighted distance \(R\) | `a1-balaban.md` 3.7; gate row 91 Section 1 | gated |
| (6.2) | Real layered tower estimate, with its profile form before the last supremum | `wf-room.md` Section 6 | Codex, ungated; inputs gated (A1 (8.2), averaging, `a3-profile.md` (30) with D1); its proof is re-checked in Section 4.4 below |
| (P2) | Plaquette expansion: from both curvature bounds and \(|A'|\), \(|D_UA'|\le C(a_0+a_1^2)\) in local units, and the same for \(A'_{\rm R},A'_{\rm I}\) | `a3-close.md` Lemma T Step 2 (SA 15890-15898) | same-model, ungated; pointwise, re-derived in 4.4 |
| (DA) | Definition A towers: nested cube unions, gaps \(>\rho\xi'_q\) (first rule) and \(\ge LM_1'\xi'_q\) (second rule) in the finer unit, erosion depth \(e_q\le3M_1'\xi'_q\); meets are separated | `assign-adopt.md` Lemma A (A1)-(A3); `meet-6c.md` Lemma J*, Prop. 7.1 | same-model (Codex gate row 114 pending for assign-adopt); meets gated row 106 |
| (W) | `wf-room.md` (3.2), (4.2)-(4.7), (5.5)-(5.6), (7.1)-(7.3) | `wf-room.md` | Codex, ungated |

Notation. \(\mathbf B'\) is the inner sequence (a tower or a meet) with local scale \(\xi'\) and weighted metric \(d'\); \(\mathbf B\) is the ambient separated sequence with local scale \(l\ge\xi'\) and weighted metric \(d\le d'\); \(\lambda=\xi'/l\le1\). All weighted metrics measure length in units of the local scale. \(\kappa:=2\log L/\rho\).

## 2. Counterexamples first

**C1. The unrestricted layered quantifier fails on an admissible field (item 4).** Let a layered domain \(X\) meet a label layer \(\mathcal L_r\), and let \(Z\subset X\) be a union of \(\pi_p\)-cubes, \(p>r\), containing a cube \(Q_{**}\subset\mathcal L_r\) of side \(16\xi_p\) whose concentric cube \(Q_*\) of side \(4\xi_p\) lies at distance \(>4M\xi_{p-1}\) from \(Z^c\). Take \(A'=0\), \(\mathbf J=0\) and a real abelian field \(U=e^{i\eta A}\), \(A=\phi_0\,\chi(x)\,x_1\,T\,dx_2\), \(T=\operatorname{diag}(1,-1)\), where \(x\) is centred at the centre of \(Q_*\), \(\chi=1\) on \(Q_*\), \(\chi\) is supported in \(Q_{**}\) and \(|\nabla\chi|\le C/\xi_p\). Then \(F=dA=\phi_0(\chi\,dx_1\wedge dx_2+x_1d\chi\wedge dx_2)\) has \(|F|\le C\phi_0\), \(|\nabla F|\le C\phi_0/\xi_p\), and \(F=\phi_0\,dx_1\wedge dx_2\) on \(Q_*\). Put \(\phi_0=c\,\alpha_{0,r}\xi_r^{-2}\) with \(c\le 1/(CM)\). In \(\mathcal L_r\) every layered simple condition of SA 10262 holds: the plaquettes are \(e^{i\eta^2F_{12}T}\) (bare plaquettes in the \(12\)-plane; others trivial), so the curvature is \(<\alpha_{0,r}\eta^2\xi_r^{-2}\); on each cube of side \(CM\xi_r\) the axial primitive of \(F\) from the cube's centre is gauge equivalent to \(A\) (abelian, contractible cube) and has \(\xi_r|A|,\xi_r^2|\nabla A|\le CMc\,\alpha_{0,r}\). Off \(Q_{**}\), \(U=\mathbf 1\).

Every Definition A tower of \(Z\) cut at depth \(n=p\) has \(Q_*\subset T'_p\), by (A3): the erosion depth is \(e_p\le3M_1'\xi_p<4M\xi_{p-1}\), since \(M\ge L^3M_1'\). The datum \(M_{\mathbf B'}(U)\) is computed with Federbush's mean, which for commuting near-identity elements is the exponential of the mean logarithm. So in the axial gauge from the centre of \(Q_*\) (contour angles \(\le 8\phi_0\xi_p^2\)), each level-\(p\) averaged link over \(Q_*\) is \(e^{i\bar\theta T}\), where \(\bar\theta\) is a linear average of line integrals of \(A\). The averaged \(12\)-plaquette is therefore \(e^{i\Theta T}\), with \(\Theta=\phi_0\xi_p^2=c\,\alpha_{0,r}L^{2(p-r)}\), the flux of the constant \(F\) through the coarse square. Let \(a_{\rm cl}\) be the clause radius at \(Q_*\) in level-\(p\) normalisation: \(a_{\rm cl}=a_0L^{-(j-p)}\le a_0\) under (R6), and \(a_{\rm cl}\le C\alpha_{0,r}L^{p-r}\) under every reading of Section 3. Since \(\Theta/(\alpha_{0,r}L^{p-r})=cL^{p-r}\) grows without bound, some \(p-r\) gives \(C_1a_{\rm cl}<\Theta\le\pi/100\) once \(\alpha_{0,r}\) is below a fixed multiple of \(c/C_1^2\). Here \(C_1\) is the constant of the next sentence. Suppose \(U_p(Z;P)\) satisfied its clause on \(Z^\circ\supset Q_*\). The curvature recursion (AV) would bound every level-\(p\) averaged plaquette of \(U_p(Z;P)\) over \(Q_*\) by \(C_1a_{\rm cl}\) in angle. By the constraint \(M_{\mathbf B'}(U_p(Z;P))=M_{\mathbf B'}(U)\), that plaquette is \(e^{i\Theta T}\), a contradiction. The failure reads no property of the assignment beyond \(T'_q\) containing a level-\(q\) block in \(\mathcal L_r\) for some \(q>r\). So under the unrestricted reading, the layered analogue of Theorem 5(a) (simple conditions imply the core) is false, and the room mechanism loses its base. Repair: Section 3.

**C2. The crude linear response loses \(\lambda^{-1}\) (item 1). Not a counterexample.** Differentiating \(w\mapsto\Phi(B(w))\) through the averages gives \(|\partial_w\Psi_x[h]|\le C\lambda(x)^{-2}\sum_ce^{-\theta d'(x,y_c)}\xi'(c)|h|\le C\lambda(x)^{-1}\sup e^{-(\theta-\kappa)d'}l|h|\) for the ambient-normalised quantities \(\Psi_x\) of Section 4. At an unsettled element (\(\lambda(x)\ll1\)) this is the loss `wf-room.md` 6 stops on. Test: \(h=-D_U\chi\) a pure gauge supported far from \(x\). It changes the tower background at \(x\) by a conjugation, of relative size \(e^{-\theta d'}|\chi|\), so the true response has no loss. The bound ignores that curvature responds to the curl of \(h\), not to \(h\). Section 4.5 proves the response bound without the loss.

**C3. The first system has no multiplier (item 2).** SA (R9) and SA 10360-10379 define \((\mathbf H,X,\mathbf A)\); the sentence at SA 10423-10428 ("Its increment is formed from the multiplier") names no formula. Two natural readouts, \(\lambda_1=H(s)^{\mathsf T}F'_{\mathbf U}(\mathbf H)\) and \(\lambda_2\) solving \((K_{\mathbf H}H(s))^{\mathsf T}\lambda_2=H(s)^{\mathsf T}F'_{\mathbf U}(\mathbf H)\), differ already at \(s=1\) on the physical locus: there \(\lambda_2\) is the constrained multiplier \(\lambda\) and \(\lambda_1=\lambda+((K_{\mathbf H}-K_0)H)^{\mathsf T}\lambda\ne\lambda\) whenever \(\lambda\ne0\), \(\mathbf H\ne0\). Hence the current is a specification the construction has to supply, as with the erosion assignment and the profile rule. Section 6 supplies one.

**C4. The raw inner datum fails (7.2) (item 3).** Let the real factor be a pure gauge \(U=\mathbf 1^g\) with \(g\) arbitrary (unitary), \(A'=0\). The plain average (WF3) is \(\mathcal M^j(U)=\mathbf 1^{\tilde g}\), with \(\tilde g\) the induced node gauge. Its logarithm \(B_{\rm raw}(c)=\frac1i\log[\tilde g(c_-)\tilde g(c_+)^{-1}]\) is of order one, so \(\|B_{\rm raw}\|\le C_BMa\tau\) fails for every small \(a\). (7.2) can hold only after the node factor \(v\) of Theorem 5(d) is removed. Section 7.

## 3. The layered quantifier (item 4)

The outline defines the layered spaces only in words: SA 6150-6153 ("the simple, tower and small-field-core clauses with those layer radii ... on every subdomain and every preceding structure"), SA 9654 ("radii assigned layer by layer"), and SA 10262 (the layered simple bounds). Here is an explicit statement. It is a definition, offered as the reading under which (1b) Theorems 5(a), 5(b), 6(d) and the room estimate SA 15933 are consistent.

**(LQ) Layered tower clauses.** Let \(X\) be a domain of a layered space at level \(j\), and let \(\boldsymbol\Omega=(\Omega_q)\) be the label sequence of the structure being checked. One structure at a time, the clause is imposed for every level \(p\le j\), every \(Z\subset X\cap\Omega_p\) that is a union of \(\pi_p\)-cubes, every \(1\le n\le p\), and both rules of Definition A. It requires two things. First, the tower configuration \(U_n(Z;P)\) of (R5) exists in its continuation domain. Second, at every element \(x\) of \(Z^\circ\) (\(Z\) minus two layers of the \(M\)-cubes of \(\pi_{p-1}\)), with \(r(x)\ge p\) the label layer of \(x\), \(l(x)=\xi_{r(x)}\) its local scale and \(\xi'(x)\) the tower's local scale,
\[
 \eta^{-2}l(x)^2\,|\partial U_n(Z;P)-\mathbf 1|<a^{\rm cl}(x),\qquad
 l(x)^2\xi'(x)\,|J(U_n(Z;P))|<a^{\rm cl}(x),
\tag{3.1}
\]
and the same with \(U\) in place of \(\mathbf U\). The clause radius is \(a^{\rm cl}(x)=c_\sigma(x\mid r(x))\,L_\flat^{2e_\sigma(x)}\alpha_{0,r(x)}\): the layer radius of SA (R22) at the layer of \(x\), with its structure coefficient and lift.

*Normalisation.* (3.1) is the normalisation of SA Theorem 5(b) ("use the factors \(\eta^{-2}l^2\) and \(l^2\xi'\)"). In a single layer (\(r(x)\equiv j\)) the (R6) clause reads \(\eta^{-2}\xi_j^2|\partial U_n-\mathbf 1|<a_0L^{j-p}\) and \(\xi_j^2\xi_n|J|<a_0L^{j-p}\). (Convert \(|\partial U_n-\mathbf 1|<a_0L^{-(j-p)}\eta_p^2\) and \(\xi_n^3|J|<a_0L^{-(j-p)}L^{2(n-p)}\) to the scale \(\xi_j=L^{j-p}\xi_p\).) So (3.1) with radius \(a_0\) implies (R6), with slack \(L^{j-p}\). The weaker layered reading, (R6) with \(j\) replaced by \(r(x)\) and \(a_0\) by the layer radius, is implied in the same way. Section 4 proves the stronger form, so every result below holds under either reading.

*Why \(Z\subset\Omega_p\).*
1. It is necessary: C1 exhibits a field satisfying every layered simple condition whose tower clause fails as soon as a level-\(p\) region may reach a layer \(r<p\), for every assignment.
2. It is exactly the hypothesis of SA Theorem 5(b). For \(q\le n\le p\), \(T'_q\subset Z\subset\Omega_p\subset\Omega_q\), so the tower lies member by member in the label sequence, and \(\xi'\le l\) on \(Z\).
3. It is the reading under which the restriction of SA Theorem 6(d), second case, lands in the layered space (`assign-adopt.md` 4.7(c)).
4. A level-\(p\) region may still reach the coarser layers \(r>p\); (3.1) is imposed there too, with the layer-\(r\) radius. This is where \(\lambda=\xi'/l<1\), and Section 4 is needed.

*Every preceding structure.* For \(\widetilde U^c_\sigma\) the same clause is imposed with each preceding structure's own regions \(\Omega^{\sigma'}_q\) and radii. Nothing in Section 4 depends on which label sequence is used, as long as it is separated with gap \(\ge\rho\) and contains the tower member by member.

*Not checked here.* Whether the label operations (healing, drop-outs, SA 6100-6160) ever shrink \(\Omega_p\) under the domain of an existing level-\(p\) term is a property of the label formation. If they did, that term's towers would leave the quantifier. This belongs to the label geometry (rows 118-119), not to the room estimate.

**Verdict on item 4.** The quantifier is stated as (LQ); \(Z\subset X\cap\Omega_p\) is necessary (C1) and sufficient for Section 4. It is a definition-level repair of the outline, like Definition A and the profile rule (5.1) of `geo-prop23.md`.

## 4. The localised complex layered tower estimate (item 1)

### 4.1 Statement

**Theorem L.** Fix \(L\ge L_0\). There are \(\rho_*\) (depending on \(L\) and on the rates \(\delta_0\) of (T4) and \(\delta\) of (6.2)), radii \(a_*,r_Q>0\) and constants \(K_L,C_b\) (depending on \(L\) and \(\rho\) only) with the following property.

Let \(\mathbf B\) be an ambient separated sequence and \(\mathbf B'\) a separated sequence without inward bonds, above the floors, lying member by member inside it (\(\Omega'_q\subset\Omega_q\)), both with gap \(\ge\rho\ge\rho_*\). Instances: every Definition A tower of a \(Z\subset\Omega_p\) cut at any depth \(n\le p\), either rule (gaps by (A2), \(LM_1'\ge\rho\)); every meet \(\Omega_q\cap T_q\) (Lemma J*, Prop. 7.1, gated row 106). Let \(U\) be real and \(w\) a complex potential with, at every plaquette and bond of \(\Omega'_0\), in ambient local units,
\[
 \eta^{-2}l^2|\partial U-\mathbf 1|\le a_0,\quad
 \eta^{-2}l^2|\partial(e^{i\eta w}U)-\mathbf 1|\le a_0,\quad
 l|w|\le a_1,\quad l^2|\nabla_Uw|\le a_1,
 \tag{H}
\]
with \(a_0\le a_1\le a_*\) and \(a_1^2\le C_0a_0\). Put \(\|w\|_*=\sup_b\xi'(b)|w(b)|\) and
\[
 B(w)=\tfrac1i\log\big[M_{\mathbf B'}(e^{i\eta w}U)\,M_{\mathbf B'}(U)^{-1}\big],\qquad
 U_{\mathbf B'}(w)=\Phi_{M_{\mathbf B'}(U)}(B(w)),
\]
which is the tower configuration of (R5) when \(\mathbf B'\) is a tower. For an element \(x\) at \(d'\)-distance \(\ge C_L\) from \((\Omega'_0)^c\) (for a tower, every element of \(Z^\circ\)) put
\[
 \Psi_x(w)=\Big(\eta^{-2}l(x)^2\big(\partial U_{\mathbf B'}(w)(p_x)-\mathbf 1\big),\ \ l(x)^2\xi'(x)\,J(U_{\mathbf B'}(w))(b_x)\Big).
\]
Then:

- **(a) Existence and a priori bound.** \(U_{\mathbf B'}\) is defined and holomorphic on \(\{\|w\|_*<r_Q\}\), which contains every \(w\) satisfying (H), and \(|\Psi_x(w)|\le K_L(a_0+a_1^2)\) under (H).
- **(b) Response with decay, no loss in \(\lambda\).** If \(w_1,w_2\) both satisfy (H) and \(h=w_2-w_1\), then
\[
 |\Psi_x(w_2)-\Psi_x(w_1)|\le C_b\Big[\sup_{d(x,y)\le2}\|h\|_{1,y}+\sup_y e^{-\theta_b d(x,y)}\|h\|_{0,y}\Big],
 \tag{4.1}
\]
with \(\|h\|_{0,y}=l(y)|h(y)|\), \(\|h\|_{1,y}=\|h\|_{0,y}+l(y)^2|\nabla_Uh(y)|\) and \(\theta_b=\theta/8\).
- **(c) Decay from a source.** If moreover \(\|h\|_{1,y}\le h_0e^{-\gamma d(y,S_0)}\) for a set \(S_0\) and some \(0<\gamma\le\theta_b\), then \(|\Psi_x(w_2)-\Psi_x(w_1)|\le e^{2\gamma}2C_bh_0e^{-\gamma d(x,S_0)}\).

(a) is the complex analogue of (6.2), with the factor \((l/\xi')^2\) cancelled. (b) is SA Theorem 5(b)'s Lipschitz clause, at every element of \(Z^\circ\) and not only at settled ones, with weight \(e^{-\theta_bd^\flat}\) in the ambient metric \(d^\flat=d\). (c) is "keeping the decay from the integrated field". The far part of (4.1) reads only the zeroth-order norm.

### 4.2 Lemma A' (localised averages)

*Statement.* There is \(r_*=r_*(L)>0\) such that, if \(\|w\|_*<r_*\) and (H) holds for \(U\) with \(a_0\le r_*\), then \(B(w)\) is defined and holomorphic, real for real \(w\), \(B(0)=0\), and for every determining row \(c\), with \(P(c)\) its pillar (the bare bonds its iterated average reads),
\[
 |B(w)(c)|\le 2L\sup_{P(c)}\xi'|w|,\qquad
 |DB(w)[h](c)|\le 4L\sup_{P(c)}\xi'|h|\quad(\|w\|_*\le r_*/2).
 \tag{4.2}
\]

*Proof.* Write \(\mathcal M^m(e^{i\eta w}U)(b)=e^{i\beta_m(b)}\mathcal M^m(U)(b)\) on level-\(m\) bonds, and \(a_m(b)=|\beta_m(b)|/t_m\), with \(t_m\) the level-\(m\) scale. The one-step bound of (AV) is local. A level-\((m+1)\) bond reads only the level-\(m\) bonds of its carrier (double block and contours), so
\(a_{m+1}(b)\le(1+C\alpha_bt_m^2)\max_{\rm carrier}a_m+Ct_{m+1}\max_{\rm carrier}a_m^2\), where \(\alpha_b\) is the curvature of \(U\) on the carrier in physical units. By (H), \(\alpha_bt_m^2\le a_0(t_m/l)^2\le a_0L^2\), and \(\sum_m(t_m/l)^2\le L^2/(1-L^{-2})\) along a pillar. The bootstrap of the row-91 gate (product \(\le5/4\), quadratic sum \(\le r/4\)) therefore closes on each pillar with \(a_0(c):=\sup_{P(c)}|w|\), provided \(Ct_q\sup_{P(c)}|w|\) is small for the level \(q\) of \(c\). It gives \(|\beta_q(c)|\le2t_q\sup_{P(c)}|w|\). Every bare bond of \(P(c)\) lies in \(\Omega'_q\), or, for an outward row, in the adjacent finer block. So \(t_q\le L\xi'(b)\) there, and \(t_q\sup_{P(c)}|w|\le L\sup_{P(c)}\xi'|w|\le L\|w\|_*\). This proves the first bound and fixes \(r_*\). Each step is a composition of Federbush means of near-identity elements and principal logarithms, holomorphic and real on real arguments. For the derivative, fix \(w\) with \(\|w\|_*\le r_*/2\) and \(h\) with \(\sup_{P(c)}\xi'|h|=1\). Then \(\zeta\mapsto B(w+\zeta h)(c)\) is holomorphic on \(|\zeta|<r_*/2\) and bounded by \(2Lr_*\), and Cauchy's estimate gives \(4L\). \(\square\)

### 4.3 Lemma D (first response of the representative, with decay)

*Statement.* Let \(\mathbf B'\) be as in Theorem L, \(\mathbf V'\) a real \(\varepsilon'\)-regular datum with \(\varepsilon'\le\varepsilon_D\), \(U'_0=\Phi_{\mathbf V'}(0)\) and \(\Phi=\Phi_{\mathbf V'}\). For an element \(x\) with top \(y_x\), let \(\psi_x(B)=(\eta^{-2}\xi'(x)^2(\partial\Phi(B)(p_x)-\mathbf 1),\ \xi'(x)^3J(\Phi(B))(b_x))\). There are \(r_D,C_D\), depending on \(L,\rho\) only, such that on \(\{\sup|B|<r_D\}\), for every row \(c\) and \(e\in\mathfrak g^c\),
\[
 |\partial_s\psi_x(B+se_c)|_{s=0}|\le C_De^{-\theta d'(y_x,y_c)}|e|,\qquad |\psi_x(B)|\le C_D(\varepsilon'+\sup|B|).
 \tag{4.3}
\]

*Proof.* By Proposition 6.4 of `a3-derivative.md`, \(\Phi(B)=W^{u_B}\) with \(W=e^{i\eta a(B)}U'_0\), the Landau pair of (T4). Write \(h=\partial_{e_c}a\) and \(\dot u=\partial_{e_c}u_B\).

*(i) The gauge factor at every site.* By (AX), the canonical representative is fixed by the axial condition: for each parent-child pair \((y,z)\) of the pillar recursion, the contour variable of \(\Phi(B)\) from \(y\) to \(z\) equals that of \(\Phi(0)=U'_0\). This is a holomorphic identity, true for real \(B\) and hence on the polydisc. Contour variables (a single contour, or Federbush's mean over the contour family) are covariant: \(T_{W^u}(y,z)=u(y)T_W(y,z)u(z)^{-1}\). Hence
\[
 u_B(z)=T_{U'_0}(y,z)^{-1}\,u_B(y)\,T_W(y,z)
\]
down every pillar, starting from the node values \(u_B=v[a]^{-1}\) of (37). A contour of a level-\(m\) block has \(t_m/\eta\) links, \(T_W=T_{U'_0}(\mathbf 1+O(t_m|a|))\), and \(|\partial_{e_c}T_W|\le Ct_m\sup_{\rm contour}|h|\); the mean is Lipschitz (`a3-derivative.md` 4.1). With \(T_{U'_0}\) unitary,
\(|u_B(z)-\mathbf 1|\le|u_B(y)-\mathbf 1|+Ct_m|a||u_B(y)|\) and
\(|\dot u(z)|\le|\dot u(y)|(1+Ct_m|a|)+C|u_B(y)|t_m\sup|h|\).
Summing the geometric series \(\sum_mt_m\le L\xi'(y)/(L-1)\) down the pillar, with \(\xi'|a|\le\|a\|_X\le C\sup|B|\) by (31), gives at every bare site \(z\)
\[
 |u_B(z)-\mathbf 1|\le C\sup|B|,\qquad |\dot u(z)|\le C\big(|\dot u(y_z)|+\sup_{P(z)}\xi'|h|\big)\le Ce^{-\theta d'(z,y_c)}|e|,
\]
by (T4) at the node \(y_z\) and on the pillar. The pillar has \(d'\)-diameter \(O(1)\), and scales on it agree within a factor \(L\).

*(ii) Curvature.* \(\partial\Phi(p)=\operatorname{Ad}(u_B(x_p))\,\partial W(p)\) for a plaquette based at \(x_p\). The link variation is \(\partial_{e_c}W(b)=i\eta E_{a(b)}h(b)W(b)\), with \(E_a=\int_0^1\operatorname{Ad}(e^{it\eta a})dt\). Moving the links to the right,
\(\partial_{e_c}\partial W(p)=i\eta\big[\sum_i\operatorname{Ad}(W_1\cdots W_{i-1})E_{a_i}h_i\big]\partial W(p)\),
and the bracket is \(\eta(D_Wh)_p+O(|h||\partial W(p)-\mathbf 1|)+O(\eta|a||h|)\) (the partial-path argument of `wf-room.md` (3.5)). Also \(|D_Wh-D_{U'_0}h|\le C|a||h|\), and \(|\partial W-\mathbf 1|\le C(\varepsilon'+\sup|B|)\eta^2\xi'^{-2}\) (regularity of \(U'_0\) and \(\|a\|_X\le C\sup|B|\)). Since \(\eta\le\xi'\),
\(\eta^{-2}\xi'^2|\partial_{e_c}\partial W(p)|\le C(\xi'^2|\nabla h|+\xi'|h|)\le Ce^{-\theta d'}|e|\).
Then \(\partial_{e_c}[\operatorname{Ad}(u)(\partial W-\mathbf 1)]=[\dot uu^{-1},\operatorname{Ad}(u)(\partial W-\mathbf 1)]+\operatorname{Ad}(u)\partial_{e_c}\partial W\). Its normalised size is at most \(C(|\dot u|+e^{-\theta d'}|e|)\), because \(|u|,|u^{-1}|\le2\).

*(iii) Current.* \(J(\Phi)(b)=\operatorname{Ad}(u_B(b_-))J(W)(b)\) (the current is based at the initial site), \(\xi'^3|\partial_{e_c}J(W)|\le Ce^{-\theta d'}|e|\) is (T4) 7.3, and \(\xi'^3|J(W)|\le C\). The same commutator computation applies.

The value bound is (9.2) together with \(|u|,|u^{-1}|\le2\). \(\square\)

*Remark.* (i) is the only step beyond (T4): (T4) bounds \(\dot u\) at tops, and the tower clause reads the representative at every site. The pillar recursion supplies the rest.

### 4.4 The real values: (P2) pointwise and (6.2) re-checked

*(P2), pointwise.* Fix a plaquette with links \(e^{i\eta w_i}U_i\). Moving the background links to the right and using the four-factor Baker-Campbell-Hausdorff series,
\(\partial(e^{i\eta w}U)(p)\,\partial U(p)^{-1}=\exp\big(i\eta^2(D_Uw)_p+O(\eta|w||\partial U-\mathbf 1|)+O(\eta^2|w|^2)\big)\).
With (H), and \(\eta\le l\), taking logarithms gives \(l^2|D_Uw|\le C(a_0+a_1^2)\) at \(p\). Here \(l\) is constant on \(p\) up to a factor \(L\). Since \(\operatorname{Ad}(U)\) commutes with \(X\mapsto X^*\) for unitary \(U\), \(D_Uw_{\rm R}=\frac12(D_Uw+(D_Uw)^*)\), and likewise for \(w_{\rm I}\). The same expansion for \(U_v=e^{i\eta v}U\), \(v\in\{w_{\rm R},w_{\rm I}\}\), gives
\[
 \eta^{-2}l^2|\partial U_v-\mathbf 1|\le C_2(a_0+a_1^2)\quad\text{on }\Omega'_0 .
 \tag{4.4}
\]
Also \(|w_{\rm R}|,|w_{\rm I}|\le|w|\) and \(\nabla_Uw_{\rm R}=(\nabla_Uw)_{\rm R}\). This is Lemma T Step 2 with the global radius replaced by the local one.

*(6.2), re-checked.* Every step of `wf-room.md` Section 6 was redone; it is a Codex proof read here by Claude. The steps are:
- scale comparison (6.3), with \(C_L=L^4\) from \(\lambda(y)/\lambda(x)\le L^2e^{\kappa d'(x,y)}\), using (MS) for each sequence and \(d\le d'\);
- the local averaging step (6.4): (AV)'s curvature recursion on one test carrier, with the carrier inside one or two adjacent ambient layers because the gap exceeds the carrier constant;
- A1 for the \(C_L\varepsilon\)-regular datum;
- the profile theorem (`a3-profile.md` (30), gated row 86, with D1 from row 99);
- absorption of \(\lambda(y_\tau)^2/\lambda(x)^2\) by half the profile rate when \(4\log L/\rho\le\delta/2\).

No step fails. The profile form, before the last supremum, is
\[
 \eta^{-2}l(x)^2|\partial U'-\mathbf 1|+l(x)^2\xi'(x)|J(U')|\le C_L\sup_\tau e^{-\delta d'(x,\tau)/2}\,\varepsilon(\tau),
 \tag{4.5}
\]
where \(\varepsilon(\tau)\) is the ambient-normalised curvature of the real field on the carrier of the test \(\tau\). Note: the conclusion holds for the real background in any real representative, since \(|\partial U'-\mathbf 1|\) and \(|J(U')|\) are invariant under unitary gauge transformations.

At real \(v\), \(U_{\mathbf B'}(v)=\Phi_{M_{\mathbf B'}(U)}(B(v))\) is the canonical real background of the datum \(M_{\mathbf B'}(U_v)\). This holds because \(\Phi\) agrees with \(U^\circ(e^{iB}\mathbf V)\) for real \(B\) (Theorem 3). Hence, by (4.4) and (6.2),
\[
 |\Psi_x(v)|\le C_LC_2(a_0+a_1^2),\qquad v\in\{0,w_{\rm R},w_{\rm I}\}.
 \tag{4.6}
\]

### 4.5 Lemma Q (localised quadratic remainder)

*Cells.* The cells of \(\mathbf B'\) are the level-\(q\) blocks contained in \(\Omega'_q\setminus\Omega'_{q+1}\) and the top-level blocks of the last member. They partition \(\Omega'_0\), because each member is a union of aligned cubes of side at least its own block side. The tower scale is constant on a cell, and a cell has \(d'\)-diameter \(\le2\). Each cell is read by at most \(N_L\) determining rows, all with tops at \(d'\)-distance \(\le C_L\): a bare bond lies in carriers of adjacent levels only (SA 11606). By (MS), at most \(C(R+1)^4L^{8+8R/\rho}(3+2R/\rho)\) cells lie within \(d'\)-distance \(R\) of \(x\). Hence
\[
 S(\gamma):=\sup_x\sum_Qe^{-\gamma d'(x,Q)}<\infty\qquad\text{for }\gamma>9\log L/\rho .
 \tag{4.7}
\]

*Statement.* Put \(r_Q=\min\{r_*,r_D/(2L)\}\) and \(\|w\|_{*,Q}=\sup_{b\in Q}\xi'(b)|w(b)|\). Then \(\psi_x\circ B\) is holomorphic on \(\{\|w\|_*<r_Q\}\), and for \(\|w\|_*\le r_Q/2\),
\[
 \big|\psi_x(B(w))-\psi_x(0)-D(\psi_x\circ B)(0)w\big|
 \le\frac{C_Q}{r_Q}\Big(\sum_Qe^{-\theta d'(x,Q)/2}\|w\|_{*,Q}\Big)^2 .
 \tag{4.8}
\]

*Proof.* *First derivative, one cell.* Let \(\|v\|_*<r_Q\) and let \(k\) be supported in a cell \(Q\). Then \(\sup|B(v)|<r_D\) by (4.2). Lemma D and (4.2) give
\[
 |D(\psi_x\circ B)(v)k|\le\sum_{c\text{ reads }Q}C_De^{-\theta d'(y_x,y_c)}\,4L\|k\|_{*,Q}\le C'e^{-\theta d'(x,Q)}\|k\|_{*,Q}.
\]
*Second derivative, two cells* (the argument of SA (BGR25), credited to the outline's authors). Let \(\|v\|_*\le r_Q/2\), and let \(k\), \(k'\) be supported in cells \(Q\), \(Q'\) with \(\|k'\|_{*,Q'}=1\). The function \(\zeta\mapsto D(\psi_x\circ B)(v+\zeta k')k\) is holomorphic on \(|\zeta|<r_Q/2\), where it is bounded by \(C'e^{-\theta d'(x,Q)}\|k\|_{*,Q}\). Cauchy's estimate gives \(|D^2(\psi_x\circ B)(v)[k,k']|\le(2C'/r_Q)e^{-\theta d'(x,Q)}\|k\|_{*,Q}\). The second derivative is symmetric, so the same holds with \(Q'\) in place of \(Q\), and the bound carries \(e^{-\theta\max\{d'(x,Q),d'(x,Q')\}}\le e^{-\theta(d'(x,Q)+d'(x,Q'))/2}\).
*Remainder.* The remainder is \(\int_0^1(1-t)D^2(\psi_x\circ B)(tw)[w,w]\,dt\), with \(\|tw\|_*\le r_Q/2\). Expanding \(w=\sum_Qw\mathbf 1_Q\) gives (4.8) with \(C_Q=C'\). \(\square\)

### 4.6 Proof of (a)

Under (H), \(\|w\|_*=\sup\lambda\,l|w|\le a_1\le a_*\le r_Q/4\). So existence and holomorphy follow from Lemma A', A1 and Theorem 3 for the \(C_1L^2a_0\)-regular datum \(M_{\mathbf B'}(U)\) (the averaging step of (6.4)), and Lemma D. Put \(\Psi_x=\lambda(x)^{-2}\psi_x\circ B\), and let \(R_2(v)\) be its Taylor remainder at \(0\). The linear term at the real point \(0\) is complex linear, and \(w=w_{\rm R}+iw_{\rm I}\). Hence the exact identity
\[
 \Psi_x(w)=\Psi_x(w_{\rm R})+i\Psi_x(w_{\rm I})-i\Psi_x(0)+R_2(w)-R_2(w_{\rm R})-iR_2(w_{\rm I}).
 \tag{4.9}
\]
The three real values are bounded by (4.6). For the remainders, \(v\in\{w,w_{\rm R},w_{\rm I}\}\) has \(\|v\|_{*,Q}\le a_1\sup_Q\lambda\le a_1\lambda(x)L^2e^{\kappa(d'(x,Q)+2)}\), by the profile comparison of 4.4. So (4.8) gives
\[
 |R_2(v)|\le\frac{C_Q}{r_Q}\lambda(x)^{-2}\Big(a_1\lambda(x)L^2e^{2\kappa}\sum_Qe^{-(\theta/2-\kappa)d'(x,Q)}\Big)^2
 \le\frac{C_QL^4e^{4\kappa}}{r_Q}S(\theta/2-\kappa)^2\,a_1^2 .
\]
The factor \(\lambda(x)^{-2}\) cancels against the two factors \(\lambda\) of the quadratic term, cell by cell. This is the local form of the cancellation \(S(\alpha_1'/R)^2\) in Lemma T. It needs \(\theta/2-\kappa>9\log L/\rho\), i.e. \(\rho>22\log L/\theta\). Summing,
\(|\Psi_x(w)|\le3C_LC_2(a_0+a_1^2)+3C_QL^4e^{4\kappa}S^2r_Q^{-1}a_1^2=:K_L(a_0+a_1^2)\). \(\square\)

*Why the global argument failed and this one does not.* `wf-room.md` 6 applied Cauchy's estimate on one ball of the global norm \(\sup l|w|\). That ball allows \(\lambda=1\) somewhere, which bounds the radius by a constant, while the crude size at \(x\) is \(\lambda(x)^{-2}\). Here the second derivative is localised cell by cell, with decay in the larger of the two distances, before any norm is taken. The profile comparison then pairs each \(\lambda(x)^{-1}\) with a \(\lambda(Q)\) from a cell that is close in \(d'\).

### 4.7 Proof of (b) and (c)

Put \(\chi=\phi(d(x,\cdot))\) with \(\phi=1\) on \([0,1]\), \(\phi=0\) on \([2,\infty)\) and \(|\phi'|\le2\). Then \(|\nabla\chi|\le2/l\), since \(d\) is \(1\)-Lipschitz with weight \(1/l\). The ambient scale varies by at most \(L^2\) on \(\{d(x,\cdot)\le2\}\), because \(\rho>2\). Split
\(\Psi_x(w_2)-\Psi_x(w_1)=[\Psi_x(w_1+\chi h)-\Psi_x(w_1)]+[\Psi_x(w_2)-\Psi_x(w_1+\chi h)]\).

*Near part.* Let \(b=\sup_{d(x,y)\le2}\|h\|_{1,y}\), so that \(\|\chi h\|_{1,y}\le3b\). If \(b\ge d_*a_0\), then (a) gives \(|\Psi_x(w_2)-\Psi_x(w_1)|\le2K_L(1+C_0)a_0\le(2K_L(1+C_0)/d_*)\,b\), and we are done. Otherwise consider \(w_\zeta=w_1+\zeta\chi h\) for \(|\zeta|<\zeta_*:=d_*a_0/(3b)\). Its potential and gradient bounds hold with \(2a_1\). Its curvature follows from the pointwise form of `wf-room.md` (3.5): from 4.4, \(\eta^{-2}l^2|\partial(e^{i\eta(w+k)}U)-\partial(e^{i\eta w}U)|\le C\|k\|_1(1+a_0+a_1+\|k\|_1)\). So the curvature is at most \(2a_0\) once \(d_*\) is small. Thus \(w_\zeta\) satisfies (H) at \((2a_0,2a_1)\). By (a), \(F(\zeta)=\Psi_x(w_\zeta)-\Psi_x(w_1)\) is holomorphic with \(|F|\le2K_L(2+4C_0)a_0\), and \(F(0)=0\). Schwarz's lemma at \(\zeta=1<\zeta_*\) gives \(|F(1)|\le6K_L(2+4C_0)b/d_*\).

*Far part.* The segment \(w_1+\chi h+t(1-\chi)h\), \(0\le t\le1\), stays in \(\{\|\cdot\|_*\le3a_1\}\subset\{\|\cdot\|_*<r_Q\}\). There the first-derivative bound of 4.5 holds; it needs only holomorphy, not (H). The increment \((1-\chi)h\) is supported in \(\{d(x,\cdot)>1\}\). Summing over the cells \(Q\) meeting that set,
\[
 |\Psi_x(w_2)-\Psi_x(w_1+\chi h)|\le\lambda(x)^{-2}\sum_QC'e^{-\theta d'(x,Q)}\sup_Q\lambda\,\|h\|_{0}
 \le C''\lambda(x)^{-1}\sum_Qe^{-(\theta-\kappa)d'(x,Q)}\|h\|_{0,Q}.
\]
*Each far cell is far in \(d'\) relative to \(\lambda(x)\).* Let \(y\in Q\) with \(d(x,y)>1\), and \(R=d'(x,y)\), so \(d'(x,Q)\ge R-2\). Along a \(d'\)-geodesic, \(\lambda\le\lambda(x)L^2e^{\kappa R}\), so \(1<d(x,y)\le\int\lambda\,ds/\xi'\le\lambda(x)L^2Re^{\kappa R}\). Since \(R\le e^{\kappa R}/\kappa\), this gives \(e^{2\kappa R}\ge\kappa/(L^2\lambda(x))\). If \(\kappa/(L^2\lambda(x))\le1\), then \(\lambda(x)^{-1}\le L^2/\kappa\). Otherwise \(e^{-(\theta-\kappa)R/2}\le(L^2\lambda(x)/\kappa)^{(\theta-\kappa)/(4\kappa)}\le L^2\lambda(x)/\kappa\), once \((\theta-\kappa)/(4\kappa)\ge1\), i.e. \(\rho\ge10\log L/\theta\). In both cases \(\lambda(x)^{-1}e^{-(\theta-\kappa)d'(x,Q)/2}\le e^{\theta}L^2/\kappa=e^{\theta}L^2\rho/(2\log L)\). Write \(e^{-(\theta-\kappa)d'}=e^{-(\theta-\kappa)d'/2}e^{-(\theta-\kappa)d'/4}e^{-(\theta-\kappa)d'/4}\). The first factor absorbs \(\lambda(x)^{-1}\); the second is summable by (4.7) with \(\gamma=(\theta-\kappa)/4\), which needs \(\rho>38\log L/\theta\); the third is at most \(e^{\theta}e^{-\theta_bd(x,y)}\) at the point \(y\) of \(Q\) where \(\|h\|_0\) is largest, using \(d\le d'\) and \(\operatorname{diam}_dQ\le2\). This proves (4.1), with \(\theta_b=(\theta-\kappa)/4\ge\theta/8\) for \(\kappa\le\theta/2\).

*(c).* For the near part, \(\sup_{d(x,y)\le2}h_0e^{-\gamma d(y,S_0)}\le e^{2\gamma}h_0e^{-\gamma d(x,S_0)}\). For the far part, \(e^{-\theta_bd(x,y)}e^{-\gamma d(y,S_0)}\le e^{-\gamma d(x,S_0)}\), by \(\gamma\le\theta_b\) and the triangle inequality. \(\square\)

### 4.8 Order of constants; what is read; scope

*Order.* \(L\); the flat and A1 constants; \(\delta_0\) (so \(\theta=\delta_0/8\)) and \(\delta\); then \(\rho\ge\rho_*:=\max\{\rho_0',8\log L/\delta,40\log L/\theta\}\) (\(\rho_0'\) of `a3-close.md` 1); then \(r_*,r_D,r_Q,C_D,C_Q,K_L,C_b\); then \(a_*\le r_Q/4\) and \(d_*\). This is the order the row-91 gate requires (the separation chosen after F0's rate, `gates/a1-balaban-gate.md` 1, 3.7). No constant depends on the depth, the number of layers, \(\lambda\), the shape of \(Z\) or the volume.

*What is read of Definition A.* Only (A1)-(A3): the members are nested unions of aligned cubes (cells), the gaps are \(\ge\rho\) in the finer unit, and \(Z^\circ\subset T'_n\). For meets, the same, from Lemma J* and Prop. 7.1.

*Comparison with the outline.* SA Theorem 5(b) asserts existence, holomorphy and a Lipschitz bound with weight \(e^{-c\delta d^\flat}\) at settled elements. Theorem L gives all three at every element of \(Z^\circ\), plus the a priori bound (a). In a single layer, (a) is Lemma T(b) at the ambient level, and (b) gives the increments that `wf-room.md` 3 obtained by Schwarz's lemma. So Theorem L also re-derives Lemma T(b) in its single-layer case, without the global radius \(c_TL^{p-n}\).

*Label.* Theorem L is an **implication** from (T4), (AX), (AV), (MS), (6.2) and (DA), all gated except (6.2), which is re-checked here, and (DA), whose gate is pending in row 114. Same-model, ungated.

## 5. Consequence: the layered room for the tower clauses (SA 15933)

**Corollary R.** Take the setting of (LQ) and Theorem L, the shrinking coefficients (R22), and an outer substitution \(A'(z)=A'\boxplus z\mathbf H\), \(|z|<R\). Assume two premises:
- (i) the assigned response decays from its source set \(S_0\) (the support of the integrated field): \(\|\mathbf H\|_{1,y}\le C_R(1+|\nu|)\delta_ke^{-\gamma_Hd(y,S_0)}\) in ambient units. This is the weighted form of (4.5), "choosing an exponential weight gives the first-response decay" (SA 10414-10415).
- (ii) the nested geometry: an element of layer \(m\) separated from \(S_0\) by \(n\) layers has \(d(x,S_0)\ge cML(n-1)\) (`wf-room.md` 4.7, the gap of one later-level \(M\)-cube per layer).

Put \(\gamma=\min\{\gamma_H,\theta_b\}\). Then every layered tower clause (3.1) at such an \(x\) changes by at most \(C|z|(1+|\nu|)s_k\rho_m\,e^{-\gamma cML(n-1)}\) in units of its radius. Its ratio to the coefficient gap \(\beta_s2^{-n}\) of (4.6) is at most \((C'/\beta_s)|z|(1+|\nu|)s_k\) once \(\gamma cML\ge\log4\). The bound is uniform in the number of layers.

*Proof.* By `wf-room.md` (3.4), applied bond by bond, \(h_z=A'(z)-A'\) has \(\|h_z\|_{1,y}\le C|z|\|\mathbf H\|_{1,y}\). Theorem L(c) bounds the change of \(\Psi_x\) by \(C|z|C_R(1+|\nu|)\delta_ke^{-\gamma d(x,S_0)}\). Dividing by the layer-\(m\) radius gives the factor \(\delta_k/\alpha_{0,m}\le s_k\rho_m\le Cs_k(1+n)^{1/2}\), by (WF1)-(WF2). Then (4.7) of `wf-room.md` applies with \(D=\gamma cML\). \(\square\)

*Scope.* The simple clauses of a layered space are pointwise and change by \(C|z|\|\mathbf H\|_{1,x}\), with the same decay. The current clause needs the decay of the current increment, which Section 6 gives through (5.5) in weighted norms. With Section 3 of `wf-room.md` (single layer) and Corollary R (tower clauses across layers), the outline's claim at SA 15933, "the quotient of its response bound by its margin contains \(2^\nu(1+\nu)^{1/2}e^{-c\delta_0ML(\nu-1)}\)", holds as an **implication** from premises (i)-(ii). The geometric premise (ii) belongs to rows 118-119 (GEO, the W3 gap). Premise (i) is the weighted first-response estimate of the first system, which `a3-derivative.md` (34) proves at \(s\equiv1\) and real-critical references, and the outline asserts for the decoupled system.

## 6. First-system and removed-map current readouts (item 2)

### 6.1 What the outline fixes, and what it does not

The decoupled response (R9), written out at SA 10360-10379, has unknowns \((X,A_\bullet,\mathbf A,\mathbf H)\) and no multiplier. Its requirements are:
- it vanishes at \(B'=0\);
- it is real and gauge covariant;
- it splits over wall-components when \(s\) vanishes on separating cubes, and is zero on a component with no datum;
- at \(s=1\) over a critical real background it is the background response with \(F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\lambda\) (SA 10450-10458);
- its reduced current is "a second component ... obtained from the constraint multiplier", of value \(L^{-3}\mathbf J+\mathsf j\) after one change of units, with the multiplier construction "required independently" (SA 5781-5785);
- per SA 10423-10428, "its increment is formed from the multiplier, so that the second-order part of the gradient enters only through \((D^{\mathsf T}DA,He_c)=(DA,DHe_c)\)".

No formula is given (C3). The second system has a multiplier, \(\lambda=H(s)^{\mathsf T}\mathbf J+\dots\), but "it is not substituted for the first system on arbitrary local cores" (SA 10447-10449).

### 6.2 Specification (adopted here)

Let \(\mathbf H=\mathbf H(s;P,B')\) be the first-system field on its domain \(Y\), at the pair \(\mathbf p(P)=(\mathbf U,\mathbf J)\). Let \(K_A\) be the derivative of the straightened rows at \(A\) in the chart at \(\mathbf U\), \(F'_{\mathbf U}(A)\) the chart gradient of the action at \(e^{i\eta A}\mathbf U\), and \(H(s)=\mathsf H(s)\mathsf m^{-1}\) the decoupled constrained minimiser of (R9). Put \(T(s)=(K_{\mathbf H}-K_0)H(s)\), an operator on rows. Define the first-system multiplier \(\lambda^{\rm I}\), its anchor \(\lambda^{\rm I}_0\) and the current increment \(\mathsf j\) by
\[
 \big(1+T(s)^{\mathsf T}\big)\lambda^{\rm I}=H(s)^{\mathsf T}F'_{\mathbf U}(\mathbf H),\qquad
 \lambda^{\rm I}_0=H(s)^{\mathsf T}F'_{\mathbf U}(0),\qquad
 \mathsf j=R_{\mathbf H}K_{\mathbf H}^{\mathsf T}\lambda^{\rm I}-K_0^{\mathsf T}\lambda^{\rm I}_0 .
 \tag{6.1}
\]
Here \(R_A=(E_A^{\mathsf T})^{-1}\) is the chart conversion (5.2) of `wf-room.md`, and \(\mathsf j\) is its anchored readout (5.4) with \((A,\lambda,\lambda_0)=(\mathbf H,\lambda^{\rm I},\lambda^{\rm I}_0)\). The substituted pair carries the independent current \(\mathbf J+\mathsf j\), additively, as (R8) requires. The removed-map currents are the differences of (6.1) for the original and the box systems, each with its own \(H(s)\), field and anchor.

### 6.3 Properties

**(S1) Holomorphy.** By (5.1), \(\|T(s)\|\le C\|\mathbf H\|_X\|H(s)\|\le C\widehat b\,\|\mathbf H\|_X\), with \(\widehat b=Ce^{16\bar\kappa}\) the decoupled operator bound (SA 10400-10404). On the response ball \(\|\mathbf H\|_X\le C\widehat b\sup|B'|\) this is \(\le1/2\) once \(\sup|B'|\le c\widehat b^{-2}\), the ceiling SA already imposes. The inverse is then a convergent Neumann series, and \(\lambda^{\rm I},\mathsf j\) are holomorphic in \((s,A',\mathbf J,B')\) on the declared domain, real at real arguments. They do not depend on \(\mathbf J\); independence is a special case of holomorphy.

**(S2) Vanishing at \(B'=0\).** There \(\mathbf H=0\), \(T=0\), \(K_{\mathbf H}=K_0\) and \(R_0=1\), so \(\lambda^{\rm I}=\lambda^{\rm I}_0\) and \(\mathsf j=0\). This holds for every independent current, as R9 requires, and unlike the force-only system (A) of `a3-clauses.md` (`wf-room.md` 5, last paragraph).

**(S3) Splitting.** Suppose \(s\) vanishes on separating cubes thicker than the ranges of \(K\), \(F'\) and \(R\). Then \(H(s)\) is block diagonal over wall-components (SA: "the equations split"), and \(K_{\mathbf H}-K_0\), \(F'_{\mathbf U}\), \(R_{\mathbf H}\) are local. So (6.1) splits. On a component with no datum, \(\mathbf H=0\) there, so \(\lambda^{\rm I}=\lambda^{\rm I}_0\) and \(\mathsf j=0\) there. Gauge covariance and transport by common lifts follow because every operator in (6.1) is covariant: the current at a bond is based at its initial site and transported by \(\operatorname{Ad}\) there, the node transport of SA 5769.

**(S4) Exactness on the physical locus.** Let \(s=1\), let \(\mathbf U=U\) be a real critical background with \(\mathbf J=J(U)=K_0^{\mathsf T}\lambda_0\), and let \(B'\) be real. Then \(K_0H(1)=1\) (`a3-derivative.md` (27)) and \(F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\lambda\) (SA 10450-10453). So
\(H^{\mathsf T}F'(\mathbf H)=(K_{\mathbf H}H)^{\mathsf T}\lambda=(1+T^{\mathsf T})\lambda\), and uniqueness in (6.1) gives \(\lambda^{\rm I}=\lambda\). Also \(\lambda^{\rm I}_0=H^{\mathsf T}J(U)=(K_0H)^{\mathsf T}\lambda_0=\lambda_0\), since \(F'_U(0)=J(U)\). Hence
\(\mathbf J+\mathsf j=R_{\mathbf H}K_{\mathbf H}^{\mathsf T}\lambda=R_{\mathbf H}F'(\mathbf H)=J(e^{i\eta\mathbf H}U)\),
by `wf-room.md` (5.2). The assignment therefore agrees on the physical locus with the current of the critical configuration, as SA 15957-15959 requires.

**(S5) Bounds.** Write \(F'_{\mathbf U}(\mathbf H)-F'_{\mathbf U}(0)=D^{\mathsf T}_{\mathbf U}D_{\mathbf U}\mathbf H+\Delta'_{\mathbf U}\mathbf H+N_{\mathbf U}(\mathbf H)\). The zeroth-order term \(\Delta'_{\mathbf U}\) includes the chart term bounded through \(\eta|J(\mathbf U)|\le C\alpha_0\xi^{-2}\) (`a3-clauses.md` (B1)), and the remainder is quadratic (`a3-derivative.md` (11)-(12), read at complex pairs as in (B2)-(B4)). Then
\[
 \lambda^{\rm I}-\lambda^{\rm I}_0=(1+T^{\mathsf T})^{-1}\Big[(D_{\mathbf U}H(s))^{\mathsf T}D_{\mathbf U}\mathbf H+H(s)^{\mathsf T}(\Delta'_{\mathbf U}\mathbf H+N_{\mathbf U}(\mathbf H))-T^{\mathsf T}\lambda^{\rm I}_0\Big],
 \tag{6.2}
\]
and \(\lambda^{\rm I}_0=(D_{\mathbf U}H(s))^{\mathsf T}\mathcal F(\mathbf U)\), where \(\mathcal F(\mathbf U)\) is the plaquette field with \(F'_{\mathbf U}(0)=D^{\mathsf T}_{\mathbf U}\mathcal F\) and \(|\mathcal F|\le C\eta^{-2}|\partial\mathbf U-\mathbf 1|\le C\alpha_0\xi^{-2}\). Both identities are integrations by parts: the second derivative sits on \(H\), never on \(\mathbf H\), as the outline intends. Hence, in the weighted norms of `wf-room.md` 5,
\[
 \|\lambda^{\rm I}-\lambda^{\rm I}_0\|_{Y,w}\le C\,C_H\big(1+\|\lambda^{\rm I}_0\|_Y\big)\|\mathbf H\|_{X,w},\qquad
 \|\lambda^{\rm I}_0\|_Y\le C\,C_H\alpha_0,
 \tag{6.3}
\]
and then, by (5.5),
\[
 \|\mathsf j\|_{F,w}\le C\,C_H(1+C_H\alpha_0)\|\mathbf H\|_{X,w}.
 \tag{6.4}
\]
This reads one operator input:

(O1) *Weighted row sums for \(H(s)\) and \(D_{\mathbf U}H(s)\).* For a weight \(w\) of rate \(\le\theta\),
\(\sup_cw(c)\,\eta^4\sum_b|H(s)(b,c)|\,\mathsf L_b^{-3}w(b)^{-1}\le C_H\) and the same for \(D_{\mathbf U}H(s)\) with \(\mathsf L_b^{-2}\). These are the column halves of BGR11, in the counting pairing.

At \(s\equiv1\), (O1) is the BGR11 member of P82° (Theorem P (e), gated row 100) and of Theorem P\(^{\mathsf c}\) (e) (`a3-clauses.md`) at complex pairs. For decoupled \(s\) it is part of the outline's statement 4 and walk expansions (1c.7, "each decoupled operator has norm at most \(\widehat b\)"), which the library has not rebuilt: `h-walk.md` covers \(\chi_Y\mathsf A\chi_Y\), not \(H(s)\). So (O1) is **cited-pending** for \(s\ne1\), with \(C_H=C\widehat b\).

*Proof of (6.3)-(6.4) from (O1).* Use the duality of the pairing row by row. For a row \(c\),
\(|(D H e_c)^{\mathsf T}D\mathbf H|\le\eta^4\sum_b|DH(b,c)||D\mathbf H(b)|\le\|\mathbf H\|_{X,w}\,\eta^4\sum_b|DH(b,c)|\mathsf L_b^{-2}w(b)^{-1}\),
and (O1) gives \(C_Hw(c)^{-1}\). The \(H^{\mathsf T}\) terms are the same with \(\mathsf L_b^{-3}\), since \(|\Delta'\mathbf H|+|N(\mathbf H)|\le C(\alpha_0+\|\mathbf H\|_X)\mathsf L^{-3}\|\mathbf H\|_{X,w}w^{-1}\). For \(\lambda^{\rm I}_0\), use \(|\mathcal F|\le C\alpha_0\mathsf L^{-2}\) and the \(DH\) row sum with \(w\equiv1\). Finally \(\|T^{\mathsf T}\mu\|_{Y,w}\le C\|\mathbf H\|_{X,w}\|\mu\|_Y\) by (5.1), and \(\|(1+T^{\mathsf T})^{-1}\|\le2\) in every weight. \(\square\)

**(S6) Removed maps.** Let \((\mathbf H,\lambda^{\rm I})\) and \((\mathbf H^\square,\lambda^{{\rm I},\square})\) be the original and box systems, with operators \(H(s)\), \(H^\square(s)\). Then \(\mathsf j-\mathsf j^\square\) is the difference of (5.4) at two arguments, plus the change of the operator. By (5.6) along the segment, and by (6.2) for the multiplier difference,
\[
 \|\mathsf j-\mathsf j^\square\|_{F,w}\le C\big(\|\mathbf H-\mathbf H^\square\|_{X,w}+\|(H(s)-H^\square(s))\|_{\rm (O1)}\,(\|\mathbf H\|_{X,w}+\alpha_0)\big).
\]
So the removed current inherits the removed factor \(e^{-cM/\sigma_j}\) exactly when the field difference and the operator difference carry it. That is the outline's "compatible boundary comparison" (SA OA7 paragraph), **cited-pending**, the same input the removed field needs.

**Verdict on item 2.** The first system does not determine a current (C3). Specification (6.1) is admissible: it is holomorphic, anchored, splitting and covariant, and exact on the physical locus. With it, the outer and removed current readouts are instances of `wf-room.md` (5.4), and their bounds (6.4) and (S6) are implications from (O1), proved at \(s\equiv1\) and pending for decoupled \(s\), together with the removed boundary comparison. The match asked for in row 116 is done for the formula; it is not closed for decoupled \(s\).
