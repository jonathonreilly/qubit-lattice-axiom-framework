# TD2: the ordinary-distance Lemma TD — pass 1 (long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session. Pass 1 of the ordinary-distance Lemma TD after the Codex distil `td.md` withdrew the counterexample of `td-draft.md` (Proposition 7.1). Research text. It is not an audit and grants no status. No other model has read it. Method: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen.

No step rests on a computation. Every argument is a finite sum, a finite Möbius inversion, a Cauchy estimate on a polydisc, the one-variable Schwarz lemma, a tree or walk count, or a comparison of explicit numbers. Each is meant to be Lean-formalisable.

Credit. The regular polymer gas (UM1)–(UM30), the class bound (R23) with its relative tree length, the boxing map, the ten-cell margin, the class rule for islands and the walk-switch localisation are the work of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the outline `ym4.tex` ("SA") and the three-dimensional manuscript `YM3_I.tex` ("Y3"), revision `31a47c543775`. Y3's per-string hull products (Y3 52582–52585) are the device behind td.md Lemma 3. The renormalisation-group step, the large-field regions, the tests and the operation **R** are Tadeusz Balaban's (CMP 99, 109, 116, 119, 122). Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions. The allocation rule in td.md Lemma 1 is J. C. Bird's.

Line references. SA L = `scratchpad/sa/ym4.tex`; Y3 L = `scratchpad/sa/YM3_I.tex`. TD = `library/td.md` (the distil; its imports and corrections are binding here). TDd = `library/td-draft.md`. CI = `library/ci-form.md`. NL1-L, IN1, ST1 = the frozen `nl1-L.md`, `in1.md`, `st1-r3.md`. PAN = `library/pan-draft.md`. I quote the line before I say what a source states. "States" means that the text at those lines says so; it does not mean that the source proves it.

Status words: **[P]** proved here, not checked; **[I]** import, with owner; **[R]** reading of a source, flagged; **[O]** Outstanding; **[CE]** counterexample to an implication; **[design]** a choice.

---

## 0. Result

**Decision.** Ordinary-distance TD is **proved** [P], conditional on the imports of TD (R, A, X, G, RUN and the named admission inputs) with two changes to their statement. Both changes are necessary for any proof from these inputs. Neither is a new physical input.

1. **(X°) — the carrier premise before contraction.** TD's premise (8) is a bound on a *contracted* Steiner length. TD itself says that (8) is proved by projecting a supplied covering tree and *then* contracting islands (TD 90). (X°) is the same premise one step earlier: an *ordinary* fine tree \(T_f\) of length \(\le C_{\rm pr}(1+d_f^{\rm old})\) that passes near every unexcused cube of \(X_f\) and meets every hub that \(X_f\) uses. This is what SA's literal relative length gives (SA 6191–6195, read as in TD Proposition 11). Proposition 6 shows that (8) alone does **not** imply ordinary TD: a chain of hubs at the minimal spacing \(s_0\) of G refutes every local decomposition. This is the withdrawn draft Proposition 7.1, with its radius bookkeeping corrected (it needs no ratio of adjacent radii), and with its scope corrected: it refutes the contracted premise, not SA.
2. **(G-ord) — the island constant is early.** The island constant \(C_{\rm isl}\) of G (TD's \(C_0\) in \(D_H=C_0L\check R_i+6\)) must be fixed with the geometric constants, before \(\kappa\) and \(\bar\kappa\). SA's class rule measures smallness by "a cube of \(O(1)\) level-\(i\) cells" (SA 17575), a cell count. TD Theorem 10 step 4 lists a "\(C_0\)" among late constants; that placement must move (it may be a name collision with CI row 5's post-\(M\) constant \(C_0\), CI 174). Proposition 7 shows that the requirement is sharp: if \(C_{\rm isl}\) may be chosen after \(\bar\kappa\), the inputs admit a single-island counterexample.

**Theorem A (ordinary TD)** [P from TD Lemmas 1–4, (X°), (G-ord)]. With \(\lambda_T:=\lambda_V+1\) and the floor \(\log(e^{\bar\kappa}-1)\ge2\lambda_T(2+C_{\rm isl}/10)+36+\log6400\), the exempt Boolean pieces \(V^{\rm ex}(W)=\sum_f f_W\) of TD (14) obey
\[
 |V^{\rm ex}(W;P,\zeta)|\le a_T\,e^{-\lambda_T d_f(W)},\qquad a_T\to0\ (\gamma\downarrow0),
\]
on the whole complex polydisc \(|\zeta|_c\le\mathfrak b\), uniformly in \(P\in\mathcal O_\sigma(U)\). Here \(d_f(W)=\operatorname{St}(W)\) is the ordinary fine tree length of CI (1)–(8). Corollary A′ regroups them on connected supports with rate \(\lambda_V\).

**How the island-hull lengths are paid** (task item 2). By the response, over the ten-cell gap. Each time a Boolean piece enters a hub it has already paid at least \(G_0\approx10\) level-\(i\) cells of response decay; crossing the hub costs at most \(D_H\approx C_{\rm isl}\) cells. The ratio \(D_H/G_0\le1+C_{\rm isl}/10\) is a cell-count ratio, fixed before \(\bar\kappa\). So \(\bar\kappa\gg\lambda_V C_{\rm isl}\) pays every crossing. Crossings *between* hubs inside one boundary carrier are paid by that term's own relative length, because SA's tree is a lattice tree. The islands' own mass (C3, IN1 217–219) cannot pay: it is fixed at creation and does not grow with \(\check R_i\) (§5.1). No refiling of exempt terms is needed for TD.

**What closes CI** (task item 3; Theorem B, §8). Ordinary TD puts the exempt potentials into the *ordinary* gas. CI's regular-gas theorem (CI Theorem 5) then applies with TD supplied, under its own imports. The natural window, the hub-contracted counts and the linked polymers of TD are not needed. TD's second filing failure (raw unions that omit the islands of their contracted length) disappears: all output lengths are ordinary, and no exemption is claimed. TD's first filing failure remains: **external-pair carriers**. The first remaining Outstanding statement is

> **(DR-locP)** [O, owner ST1]. For every switch \(s\) with \(|s_c|<e^{\bar\kappa}\), every source \(S\) in the source ball and every face-component \(K'\) of \(\operatorname{supp}s\), the response \(h(s;P,S)\) on the bonds and stencils of \(K'\) depends on the external pair \(P\) only through \(P|_{N_{c_P}(K')}\), for a geometric \(c_P\) fixed before \(\kappa\), compatibly with the declared restriction maps.

NL1-L's H-DR states the component reads "at fixed \(P\)" (NL1-L 170–171). Three attacks on the filing statement (File-P) are recorded in §8.3. The first (Boolean localisation in \(B\)) fails. The second (switch Möbius with geometric-mean bounds) gives the exact decomposition by P-carrier but its per-cube sums do not close. The third (joint switch–fluctuation composition with a logarithmic excused collar) closes the sums given (DR-locP) and one further lemma (JC), stated exactly.

**Line count**: reported in the session reply.

---

## 1. Sources, quoted

### 1.1 SA: relative length, margins, boxing, the class rule

- *Relative length and (R23)* (SA 6191–6205). For an exempt family, the length minimises \(M^{-1}\) times tree length over subfamilies contained in \(X\); "the tree meets each cube outside \(\bigcup\mathsf F\) and each member of \(\mathsf F\), but need not fill those members" (SA 6193–6195). For a label the family is the level-\(j\) hulls of its standing islands (SA 6196). SA 6197–6198 adds that the result is at most \(d_j(X)\) and "asserts no decay across an exempt island". (R23) is \(|B_{\mathcal S}(j,X,o)|\le\mathsf Be^{-\kappa d_j^\natural(\mathcal S;X)}\) (SA 6200–6205). **[R]** I read "tree" as a tree in the cube graph, as TD Proposition 11 does (binding). Under this reading a tree that meets two unexcused cubes contains a lattice path between them. "No decay across an exempt island" then means that the island's own extent is not charged, not that two cubes on opposite sides of it are joined free. Proposition 6 shows what changes under the other reading.
- *Ten-cell margin* (SA 17317–17325). For step \(t\): \(\Omega_t^c=Q_t'^{\sim2}\cup P_t'^{\sim4}\cup\widehat Y^{\sim8}\), \(Z^{[0]}=\mathsf{bx}((\Omega_t^c)^{\sim2}\cup R_t'^{\sim})\), with hulls and layers "in level-\(t\) cells" (SA 17317). The free evolution is \(\Phi_t(Y)=\mathsf{bx}(\widehat Y^{\sim10})\) (SA 17328). The boxing map "replaces each component contained in a cube of \(O(1)\) cells by its bounding box" (SA 17317, end).
- *Radii* (SA 17334). \(\check R_k\) is the smallest power of \(L\) not less than \((\log\min_{i\le k}x_i)^r\), \(r\ge2\); it is non-increasing; \(\check R_k\le L\check R_{k+1}\); two consecutive drops never occur.
- *Class rule* (SA 17575). A component belongs to the class when, among other conditions, "\(X\cap Z_i\) is a single component of \(Z_i\) and is small, that is, contained in a cube of \(O(1)\) level-\(i\) cells". Inside the window \(Z_i\cap X=H_i^{[10]}\) (SA 17579). The side of \(X\) in cells "is comparable to the fixed point of the free evolution" (SA 17583, same paragraph). Later in the paragraph: no cell, box or box neighbourhood wraps around the torus.
- *Standing islands* (SA 19523). The bounds of a standing island refer to its creation level and do not involve the later level \(k\).
- *Response splitting* (SA 5794–5797). When \(s\) vanishes on separating cubes, the equations split over the remaining components.
- *Walk switches* (SA 17903–17920). Each walk in the response carries a parameter \(s(\Delta)\) for every cube it visits; brackets and Schwarz give \(f(U^{\rm old})-f(U^{\rm new})=\sum_{Y\supset X}f_Y\) with \(|f_Y|\le2\mathsf ab_fe^{-(\bar\kappa-1)\mathfrak m(X,Y)}\). TD's source table (TD 468) records that these lines do not prove the multipoint or external-carrier assertions. I agree.
- *(UM1), (UM7)* (SA 14293–14313; 14416–14433). (UM1) is a hypothesis on the actual local potentials, with tree length \(d_f\). (UM7) is \(\#Y^\sharp\le C_h(1+d_f(Y)/L)\), proved by a closed walk along a covering tree; the proof does not use connectivity of \(Y\).

### 1.2 Y3

Y3 52582–52585: the parameter family is completed by one on the core collar, by \(s\) on other big cubes and by zero outside; one multiplies "a coefficient or string by the product of \(\bar s\) over its big-cube hull". The products are attached term by term. TD Lemma 3 uses the same device on the response pieces.

### 1.3 Our notes (binding inputs)

- *TD* (whole). Hypotheses R (TD 25–35), A (TD 51–61) with the Outstanding complex island amplitude (TD 63), X (TD 65–71), G (TD 73–90). Lemmas 1–4 (TD 94–172) are used verbatim. Theorem 5 (TD 174–204) is the contracted version of Theorem A. Proposition 11 (TD 442–447) fixes the literal reading of SA's relative length and withdraws draft Proposition 7.1. Theorem 9 and its Outstanding filing input (TD 365–379).
- *TD (8)* (TD 85–90): \(\operatorname{St}_{\Gamma^\natural}(\pi X_f)\le C_{\rm pr}(1+d_f^{\rm old})\) and \(X_f\) meets a hub or the live set. TD 90: "Projecting a supplied covering tree and then contracting its covered islands proves (8) if all read enlargements fit its fixed collar."
- *CI TD* (CI 87–94): the decomposition (8) with \(|V^{\rm ex}(W)|\le a_Ee^{-\lambda_Td_f(W)}\), \(\lambda_T\ge\lambda\), \(\sup_{\theta\ge\gamma^{-2}}a_E\to0\). CI 18 defines \(d_f(Y)\) as the least edge count of a tree meeting all cubes of \(Y\), allowing additional vertices.
- *NL1-L H-DR* (NL1-L 159–171). Joint holomorphy and (7); component reads depend "only on \(s|_{K'}\) and the source rows assigned to \(K'\), at fixed \(P\)".
- *PAN* (draft). PAN 57: "\(C_0\) is the class constant: a standing island's hull lies in a cube of \(C_0\) level-\(i\) cells (SA L17575)". PAN 163–165: (G-gap), (G-isl), (G-sep). PAN table 425: \(C_0\), "the O(1) of single boxes", chosen independently and early. PAN 409 and 496 (F4): decay across islands is not available from (R23); PAN pays island diameters by \(\bar\kappa\gg\kappa\) and the ten-cell gap. PAN 495 (F3): Möbius localisation over all supersets of a large object fails by boundary entropy.
- *IN1* (frozen). Island mass bound \(\mathfrak M_c(i,X)\le e^{-(2-\varepsilon_{\rm rar})P_i-\kappa_1|X|_i}\) at creation level (IN1 217–219). Rows 2 and 4 with Amendment 1 (IN1 228, 230, 666–676).

---

## 2. Setting and the two changed inputs

Notation is TD's throughout: the fine cube graph with corner adjacency and degree 80, its distance \(d\), \(\operatorname{St}\), \(\operatorname{MST}\), the collapsed weight \(m_X(W)\) of TD (1), the Boolean difference \(D_W\) of TD (2), the response data of R and TD (4), the admission data of A, and the hubs \(\widetilde H=N_2(H)\) of G with \(s_0=\check R_i-4\), \(D_H\), \(G_0=10L\check R_i-2\). Gas cubes are the cubes owning free bonds. For an exempt term \(f\): \(\mathcal B_f\) its complete reads, \(X(f)=\{\Delta_b:b\in\mathcal B_f\}\), \(X_f\supset X(f)\) its presentation set, \(d_f:=d_f^{\rm old}\), \(\widetilde\omega_f\le\widehat\omega_fe^{-\kappa d_f}\) and the per-cube sum \(N_{\rm ex}\) of TD (6). Write \(f_W\) for the left side of TD (14) at \(P\) and \(\zeta\):
\[
 f_W(P;\zeta)=D_W\big[\Phi_f(P,h_0+G(\mathbf1,\cdot))\big](\zeta),\qquad
 V^{\rm ex}(W)=\sum_{f\ \rm exempt}f_W .
\]
TD Theorem 5 proves that \(\sum_WV^{\rm ex}(W)\) is the exempt exponent difference, exactly, that each \(V^{\rm ex}(W)\) is holomorphic in \(P\) and \(\zeta\), real at real data, and that it reads \(\zeta\) only on the bonds of \(W\). These parts carry over unchanged. Only the bound changes.

**Constants introduced here.**

- \(C_{\rm isl}\ge1\): the island constant. G's hub box side is \(D_H=C_{\rm isl}L\check R_i+6\). This is TD's \(C_0\), renamed to avoid the clash with CI row 5.
- \(c_{\rm col}\ge0\): a fixed read-collar width in fine cubes.
- \(\widetilde H^+:=\{x:d(x,\widetilde H)\le c_{\rm col}\}\), the collared hub. It lies in a box of side \(D_H+2c_{\rm col}\). A gas cube has distance at least \(G_0-c_{\rm col}\) from it.
- \(\eta_H:=1+C_{\rm isl}/10\).

**(G-ord)** [I: LF1(2); R: SA 17575, PAN 57, PAN 425]. \(C_{\rm isl}\) and \(c_{\rm col}\) are fixed in IN1 row 2 with the other geometric constants. They are uniform in \(L\) and independent of \(\kappa,\bar\kappa,M\).

*Reason for the reading.* SA's class rule (SA 17575) and boxing map (SA 17317) measure size by a number of cells, \(O(1)\). The free-evolution fixed point (SA 17328, 17583) is a cell count: \(n\mapsto\lceil n/L\rceil+20\) has a fixed point below 22 for \(L\ge2\). A standing island made at level \(k\) is not moved later (SA 19523), and level-\(i\) cells only grow with \(i\) because \(\check R_{i-1}\le L\check R_i\) (SA 17334). So its later hull fits in \(C_{\rm isl}\) cells with \(C_{\rm isl}\) a fixed number. That standing islands keep this bound at every later main step is G's (G-isl), an LF1 import; I do not prove it. TD Theorem 10 step 4 places "island geometry ... prefactors \(C_0\)" after \(M\). For TD Theorem 5 this was harmless, since \(D_H\) entered only through the logarithmic ceilings (7). For ordinary TD the placement matters (Proposition 7).

**(X°) — ordinary carrier premise** [I: NL1(1)/LF1, the projection and containment of TD 90; R: SA 6191–6196]. For every exempt term \(f\) there is a tree \(T_f\) in the fine cube graph with
\[
 |E(T_f)|\le C_{\rm pr}(1+d_f),
\]
such that

- (a) every cube \(x\in X_f\) satisfies \(d(x,V(T_f))\le c_{\rm col}\), or lies in \(\widetilde H^+\) for a hub \(\widetilde H\) that \(T_f\) meets;
- (b) \(X_f\) meets a hub or the live set.

\(C_{\rm pr}\ge1\) is geometric, fixed in row 2, uniform in \(L,M,\kappa,\bar\kappa\).

*Where (X°) comes from.* For a boundary term or kept form, take SA's minimising tree at level \(j\) (SA 6191–6195). It meets every unexcused level-\(j\) cube of \(X\) and each excused member. Project it to level-\((i-1)\) cubes; a tree of length \(n\) in level-\(j\) cube units projects to a connected subgraph with at most \(C(1+n)\) edges, since level-\((i-1)\) cubes are at least as coarse. The excused members are level-\(j\) hulls of standing islands; the import is that each lies in a hub (TD 90, "the asserted containment"). The reads of \(X_f\setminus X\) lie within the fixed collar. Then (a) holds. For islands, \(T_f\) is one cube of the island's hub, \(d_f=0\), and \(X_f=X^{\uparrow}\subset\widetilde H^+\). For exempt remainders and drop-outs, \(d_f\) is the full length and \(T_f\) is a covering tree. Part (b) is TD (8)'s side condition.

*Relation to TD (8).* Contracting the hubs maps \(T_f\) to a connected subgraph of \(\Gamma^\natural\) with no more edges. So (X°) gives the contracted length of \(\pi V(T_f)\). Adding the collar connectors gives (8) when they are absorbed in TD's "fixed collar". The converse fails: Proposition 6 satisfies (8) with \(C_{\rm pr}=1\), yet has no ordinary tree of the required length.

---

## 3. Two geometric lemmas

Fix an exempt \(f\) and a nonempty set \(W\) of gas cubes. Write \(m:=m_{X(f)}(W)\). Take a minimum spanning tree \(\mathcal T\) of the complete graph on \(W\cup\{*\}\) with the weights of TD (1), rooted at \(*\). Let \(l_c\) be the weight of the parent edge of \(c\in W\), so \(\sum_cl_c=m\) (TD (10)). Let \(R\subset W\) be the children of \(*\). For \(c\in R\), choose \(x_c\in X(f)\) with \(d(c,x_c)=d(c,X(f))=l_c\). Realise each edge \(\{c,c'\}\) of \(\mathcal T\) between cubes by a geodesic of \(d(c,c')\) edges, and each root edge \(\{c,*\}\) by a geodesic from \(c\) to \(x_c\). Let \(Q\) be the union. Then \(|E(Q)|\le m\), and every \(c\in W\) is joined in \(Q\) to some \(x_{c'}\), \(c'\in R\), by a path of at most \(m\) edges: follow the tree path from \(c\) towards \(*\). This is TD Lemma 1(3) with its proof.

**Lemma 3.1 (ordinary spanning through an exempt carrier)** [P from (X°), G]. Assume
\[
 10L\check R_i\ \ge\ 6+2c_{\rm col}+(1+C_{\rm isl}/10)(2+c_{\rm col}).        \tag{T4}
\]
Then
\[
 d_f(W)=\operatorname{St}(W)\ \le\ (1+\eta_H)\,m\;+\;C_{\rm pr}(1+d_f)\;+\;c_{\rm col}|W|.        \tag{3.1}
\]

*Proof.* For each \(c\in R\) choose a connector path \(\pi_c\) from \(x_c\) to \(V(T_f)\), as follows. By (X°)(a), applied to \(x_c\in X(f)\subset X_f\), one of two cases holds.

- *Case 1:* \(d(x_c,V(T_f))\le c_{\rm col}\). Take a geodesic of at most \(c_{\rm col}\) edges.
- *Case 2:* \(x_c\in\widetilde H^+\) for a hub \(\widetilde H\) that \(T_f\) meets. Pick \(y\in V(T_f)\cap\widetilde H\). Both \(x_c\) and \(y\) lie in one box of side \(D_H+2c_{\rm col}\). The box does not wrap around the torus (SA 17575, end of the paragraph, imported with G). In the corner-adjacency graph the distance between two cubes of a box is their Chebyshev distance, realised inside the box. So a path of at most \(D_H+2c_{\rm col}\) edges joins them.

The union \(U:=Q\cup T_f\cup\bigcup_{c\in R}\pi_c\) is connected: every component of \(Q\) contains some \(x_c\), each \(x_c\) is joined to \(T_f\), and \(T_f\) is connected. \(U\) contains \(W\). A spanning tree of \(U\) is a tree meeting \(W\), so
\[
 \operatorname{St}(W)\le|E(U)|\le m+C_{\rm pr}(1+d_f)+\sum_{c\in R}|\pi_c| .
\]
Case-1 connectors cost at most \(c_{\rm col}\) each, and there are at most \(|R|\le|W|\) of them. In Case 2, \(c\) is a gas cube and \(x_c\in\widetilde H^+\), so \(l_c=d(c,x_c)\ge G_0-c_{\rm col}\). Summing over Case-2 cubes, their number is at most \(m/(G_0-c_{\rm col})\). Hence
\[
 \sum_{c\in R}|\pi_c|\le c_{\rm col}|W|+\frac{D_H+2c_{\rm col}}{G_0-c_{\rm col}}\,m .
\]
Finally, (T4) is equivalent to \(D_H+2c_{\rm col}\le\eta_H(G_0-c_{\rm col})\). Indeed \(\eta_H(G_0-c_{\rm col})=10L\check R_i+C_{\rm isl}L\check R_i-(1+C_{\rm isl}/10)(2+c_{\rm col})\), and \(D_H+2c_{\rm col}=C_{\rm isl}L\check R_i+6+2c_{\rm col}\). This proves (3.1). ∎

**Lemma 3.2 (the gap is paid)** [P from (X°), G]. 
\[
 m+C_{\rm pr}(1+d_f)+2c_{\rm col}\ \ge\ G_0 .                                \tag{3.2}
\]

*Proof.* Take \(c\in W\). Follow \(Q\) from \(c\) to some \(x:=x_{c'}\) (at most \(m\) edges). If \(x\in\widetilde H^+\) for some hub, a further \(c_{\rm col}\) edges reach a hub cube. Otherwise \(d(x,V(T_f))\le c_{\rm col}\) by (X°)(a): go to \(z\in V(T_f)\). By (X°)(b) choose \(y\in X_f\) in a hub or in the live set. If \(d(y,V(T_f))\le c_{\rm col}\), go along \(T_f\) from \(z\) to a vertex within \(c_{\rm col}\) of \(y\), then to \(y\). Otherwise \(y\in\widetilde H^+\) for a hub that \(T_f\) meets; go along \(T_f\) to a cube of that hub. In every case a walk of at most \(m+2c_{\rm col}+C_{\rm pr}(1+d_f)\) edges joins \(c\) to a cube of a hub or of the live set. By G, a gas cube has distance at least \(G_0\) from every hub and from the live set. ∎

*Remark (what the two lemmas use).* Lemma 3.1 pays each entry into a hub by the response edges spent to reach it: \(D_H\) against \(G_0-c_{\rm col}\). This is the ten-cell gap of SA 17317–17328 against the \(O(1)\)-cell island of SA 17575. Crossings between different hubs of one carrier are inside \(T_f\), so they are paid by \(d_f\). Neither lemma contracts anything.

---

## 4. Ordinary TD

Recall from TD (4): \(a=\tfrac12\log(D/6400)\), \(D=e^{\bar\kappa}-1\), \(\delta=(8e)^{-1}\), \(\beta_c(\zeta)=2K_1|\zeta|_c/\varrho\), \(\vartheta=4K_1\mathfrak b/(\delta\varrho)\). On \(|\zeta|_c\le\mathfrak b\) we have \(2\beta_c/\delta\le\vartheta\).

**Theorem A (ordinary TD)** [P from TD Lemma 4, Lemmas 3.1–3.2, X, (X°), G, (G-ord)]. Assume R, A, X, (X°), G, (G-ord). Put \(\lambda_T:=\lambda_V+1\) and \(\vartheta_T:=\vartheta e^{\lambda_Tc_{\rm col}}\). Assume
\[
 \lambda_TC_{\rm pr}\le\kappa/4,\qquad                                         \tag{T1}
\]
\[
 a_1:=a-6-\lambda_T(1+\eta_H)\ \ge\ 12,                                       \tag{T2}
\]
\[
 \vartheta_T<1,                                                                 \tag{T3}
\]
and (T4). Then for every \(P\in\mathcal O_\sigma(U)\), every nonempty set \(W\) of gas cubes and every complex \(\zeta\) with \(|\zeta|_c\le\mathfrak b\) for \(c\in W\) (in particular every real \(B\) in the box),
\[
 |V^{\rm ex}(W;P,\zeta)|\le a_T\,e^{-\lambda_Td_f(W)},\qquad
 a_T:=2e^{\kappa/4}N_{\rm ex}\,\vartheta_T\,e^{-\nu(G_0-C_{\rm pr}-2c_{\rm col})},          \tag{4.1}
\]
with \(\nu:=\min\{\kappa/(4C_{\rm pr}),a_1/2\}\). The decomposition \(\sum_WV^{\rm ex}(W)=\sum_f[\Phi_f(P,h_0+G(\mathbf1,B))-\Phi_f(P,h_0)]\) is exact; each term is holomorphic in \(P\) and \(\zeta\), real at real data, and reads \(\zeta\) only on \(W\). Under RUN, \(a_T\to0\) as \(\gamma\downarrow0\), uniformly in histories, with all earlier constants fixed.

*Proof.* Fix \(f\) and \(W\); write \(m_f=m_{X(f)}(W)\). Condition (T2) gives \(a\ge12\). Condition (T3) gives \(\vartheta<1\), so \(\beta_c<\delta/2\). TD Lemma 4 applies:
\[
 |f_W|\le\widetilde\omega_f\prod_{c\in W}\frac{2\beta_c}{\delta}\,e^{-(a-6)m_f}
      \le\widehat\omega_fe^{-\kappa d_f}\,\vartheta^{|W|}\,e^{-(a-6)m_f}.
\]
Multiply by \(e^{\lambda_Td_f(W)}\) and use (3.1):
\[
 e^{\lambda_Td_f(W)}|f_W|
 \le\widehat\omega_f\,e^{\lambda_TC_{\rm pr}}\,\vartheta_T^{|W|}\,
     e^{-(\kappa-\lambda_TC_{\rm pr})d_f}\,e^{-a_1m_f}.
\]
By (T1), \(e^{\lambda_TC_{\rm pr}}\le e^{\kappa/4}\) and \(\kappa-\lambda_TC_{\rm pr}\ge\kappa/2+\kappa/4\). By (T3) and \(|W|\ge1\), \(\vartheta_T^{|W|}\le\vartheta_T\). Split \(a_1m_f=(a_1/2)m_f+(a_1/2)m_f\). Since \(\kappa/4\ge\nu C_{\rm pr}\) and \(a_1/2\ge\nu\), Lemma 3.2 gives
\[
 \tfrac\kappa4d_f+\tfrac{a_1}2m_f\ \ge\ \nu(C_{\rm pr}d_f+m_f)\ \ge\ \nu(G_0-C_{\rm pr}-2c_{\rm col}).
\]
Therefore
\[
 e^{\lambda_Td_f(W)}|f_W|\le e^{\kappa/4}\vartheta_T e^{-\nu(G_0-C_{\rm pr}-2c_{\rm col})}\cdot
 \widehat\omega_fe^{-(\kappa/2)d_f}\,e^{-(a_1/2)m_f}.
\]
*Sum over \(f\).* Fix \(c_0\in W\). By TD Lemma 1(3), \(m_f\ge d(c_0,X(f))=d(c_0,\Delta_f)\) for a cube \(\Delta_f\in X(f)\) nearest \(c_0\). Assign \(f\) to \(\Delta_f\). Since \(a_1/2\ge6\), TD (9) and (6) give
\[
 \sum_f\widehat\omega_fe^{-(\kappa/2)d_f}e^{-(a_1/2)m_f}
 \le\sum_{\Delta}e^{-6d(c_0,\Delta)}\sum_{f:X(f)\ni\Delta}\widehat\omega_fe^{-(\kappa/2)d_f}
 \le2N_{\rm ex}.
\]
This proves (4.1). Exactness, holomorphy, reality and \(\zeta\)-locality are TD Theorem 5's, since \(V^{\rm ex}(W)\) is the same function.

*Size.* TD's proof of Theorem 5 (TD 202–203) gives \(\vartheta\le C(\bar\kappa)(g\ell^{p_0}+\ell^{p_0-q})\to0\). The factor \(e^{\lambda_Tc_{\rm col}}\) is fixed after \(\kappa\), so \(\vartheta_T\to0\). \(N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}\) by X. RUN gives \(\check R_i\ge(\ell-1)^r\), \(r\ge2\), so \(G_0\ge10L(\ell-1)^r-2\). With an integer \(n>t_{\rm ex}\), \(e^{\nu x}\ge(\nu x)^n/n!\) shows that \(N_{\rm ex}e^{-\nu(G_0-C_{\rm pr}-2c_{\rm col})}\to0\). Hence \(a_T\to0\). (T3) and (T4) are ceilings on \(\gamma\) for the same reasons. ∎

**Corollary A′ (connected supports)** [P from Theorem A]. Fix a total order on finite trees of the fine graph. For a nonempty \(W\), let \(\widehat W\) be the vertex set of the least minimum tree meeting \(W\). Then \(\widehat W\) is connected, \(W\subset\widehat W\) and \(|\widehat W|=d_f(W)+1\). Put
\[
 V^\circ(Y;P,\zeta):=\sum_{W:\ \widehat W=Y}V^{\rm ex}(W;P,\zeta)
\]
for connected \(Y\). Then \(\sum_YV^\circ(Y)=\sum_WV^{\rm ex}(W)\), each \(V^\circ(Y)\) reads \(\zeta\) only on the gas cubes of \(Y\), and
\[
 |V^\circ(Y)|\le2a_T\,e^{-\lambda_Vd_f(Y)},\qquad d_f(Y)=|Y|-1 .                 \tag{4.2}
\]

*Proof.* Each \(W\) has one \(\widehat W\), so the sum is a regrouping of a finite sum. At most \(2^{|Y|}\) sets \(W\) satisfy \(W\subset Y\). Each such term with \(\widehat W=Y\) has \(d_f(W)=|Y|-1\). So \(|V^\circ(Y)|\le2^{|Y|}a_Te^{-\lambda_T(|Y|-1)}=2a_Te^{-(\lambda_T-\log2)(|Y|-1)}\), and \(\lambda_T-\log2\ge\lambda_V\). ∎

*Remark.* \(\widehat W\) may contain cubes that own no free bond, for example cubes of the gap region. This is the same situation as for class carriers (CI 18 allows any fine cubes). If the actual gas interface J requires supports inside the gas region, use Steiner trees in the gas subgraph instead; Theorem A does not supply that bound. (UM7)'s proof (SA 14424–14433) uses only a covering tree, so the collar count holds for both conventions.

*Remark (the bound is on a complex polydisc).* CI's TD asks for the bound on real boxes and holomorphy on the declared complex boxes. Theorem A gives the bound on \(|\zeta|_c\le\mathfrak b\), complex. Cauchy estimates in \(\zeta\) on smaller polydiscs follow.

---

## 5. Where the island-hull lengths are paid

The task names three possible payers. I take them in turn.

### 5.1 The islands' own mass (C3, LF1) — does not pay

IN1 217–219 requires, for each island at its creation level \(i\), \(\mathfrak M_c(i,X)\le e^{-(2-\varepsilon_{\rm rar})P_i-\kappa_1|X|_i}\). SA 19523 says the bounds of a standing island refer to the level at which it was made.

*Exact reason it fails.* The cost to be paid in a Boolean piece is \(\lambda_T\) times a hub crossing, about \(\lambda_TC_{\rm isl}L\check R_i\) fine cubes at the current main step. It grows without bound as \(\gamma\downarrow0\). The island's mass gain is \(\kappa_1|X|_{i_0}\) at its creation level \(i_0\), with \(|X|_{i_0}\le C_{\rm isl}^4\) cells. That number is bounded and does not grow with the later \(\check R_i\). Also the mass is a factor of the stored measure. It is not a factor of the exponent difference \(f_W\), and the gas does not integrate the island's region. Moving it there would need a new formation map, not a bound.

### 5.2 Hub contraction plus a bound on hub sizes — this is what pays

Theorem A is this route without the contraction. The hub-size bound is the cell-count ratio
\[
 \frac{D_H+2c_{\rm col}}{G_0-c_{\rm col}}\le\eta_H=1+\frac{C_{\rm isl}}{10}\qquad\text{(under (T4))},
\]
which is SA's ten cells of margin (SA 17317–17328) against an island of \(O(1)\) cells (SA 17575). The response pays it at rate \(a-6\), because \(\bar\kappa\) is chosen after \(\lambda_V\) and \(C_{\rm isl}\). The contraction of TD Theorem 5 discards exactly this payment. It writes \(\ell^\natural(W)\) where \(\operatorname{St}(W)\le(1+\eta_H)\ell^\natural(W)+\dots\) was available. That is why TD needed the hub-contracted counts and linked polymers.

### 5.3 Refiling exempt terms — not needed for TD

Theorem A files nothing new: \(V^{\rm ex}(W)\) is TD's function. Refiling enters only for external-pair carriers (§8).

### 5.4 The ten-cell gap of SA 17317–17325

It matters in one place: the ratio \(\eta_H\). It is the reason the floor (T2) is \(\bar\kappa\gtrsim\lambda_VC_{\rm isl}\), not \(\bar\kappa\gtrsim\lambda_VC_{\rm isl}L\). The factor \(L\) cancels because the gap and the island are both measured in level-\(i\) cells. If the gap were one cell, the ratio would be about \(C_{\rm isl}\) and (T2) would still close. If the gap were zero, Lemma 3.2 would give nothing, and the island amplitudes \(\widehat\omega_f\approx2B_f\), which do not decay, would not tend to zero.

*A separation I could not source.* Inside its formation window an island's trace is the box \(H_i^{[10]}\) (SA 17579). If distinct standing islands kept disjoint ten-cell boxes at every later main step, distinct hubs would be about \(20\) cells apart. Then even the contracted reading of §6 would give a ratio \(\le1+C_{\rm isl}/20\), and no chain counterexample would exist. I found no line that states this separation after the window. G states only \(s_0=\check R_i-4\) (TD 73), and PAN's (G-sep) argues only one level-\((i-1)\) cell (PAN 165). I do not use the stronger separation.

---

## 6. Sharpness: the two changes are necessary

Both propositions refute an *implication*. They exhibit data satisfying the listed inputs for which no exact local decomposition has the TD bound. They do not exhibit an actual Yang–Mills history.

**Reduction lemma 6.0 (mixed differences decide every decomposition)** [P]. Let the gas cubes be exactly \(c_1\ne c_2\), and let \(F(\zeta)\) be the exempt exponent difference. Suppose \(F=\sum_{\varnothing\ne W\subset\{c_1,c_2\}}V(W)\), with \(V(W)\) depending on \(\zeta\) only through the bonds of \(W\), and \(\sup_{\rm box}|V(W)|\le a\,e^{-\lambda d_f(W)}\). For real \(t_1,t_2\) in the box, put \(\zeta^{(t_1,t_2)}\) with \(\zeta_{b_k,1}=t_k\) and all other coordinates zero. Then
\[
 \big|F(\zeta^{(t_1,t_2)})-F(\zeta^{(t_1,0)})-F(\zeta^{(0,t_2)})+F(\zeta^{(0,0)})\big|\le4a\,e^{-\lambda d(c_1,c_2)}.
\]
*Proof.* \(V(\{c_k\})\) does not depend on the other cube's variable, so its mixed difference vanishes. Only \(V(\{c_1,c_2\})\) remains, with four values each bounded by \(ae^{-\lambda d(c_1,c_2)}\). ∎

This answers the distil's remark that failure of one displayed decomposition does not refute the existential claim (TD 447). With two gas cubes there is no entropy sum.

**Lower endpoint used below.** In every rate window in use, \(\lambda_V\ge5\kappa/L\). *Proof.* IN1 (24) requires \(\lambda\ge\Theta/L\) with \(\Theta=C_h^{\rm UM}\{3+c_\ell[(1+4\beta_s)\kappa+g_*]\}\). Here \(C_h^{\rm UM}\ge1\), because a single fine cube has a nonempty collar and (UM7) at \(d_f=0\) gives \(C_h\ge1\); and \(c_\ell\ge5\), because \(\ell_c(Z)=d_c(Z)+5\ge5\) at \(N=1\) (TDd (7.1), checked). TD's natural window (32) has \(A_*\ge A_{\rm old}\) and the same conclusion. ∎

### 6.1 Contracted carriers do not suffice

**Proposition 6 (TD (8) does not imply ordinary TD)** [CE]. Fix \(\gamma\) below the ceilings of G and (7), and any \(\lambda_T\ge\lambda_V\). For every \(m\ge1\) there are data satisfying R, A (two-sided), X with an exempt length \(d_f\) obeying (6) and TD (8) with \(C_{\rm pr}=1\), and G with hubs of side \(D_H\) at spacing \(s_0+2\), such that every exact local decomposition with the TD bound has
\[
 a\ \ge\ c(\gamma)\,\exp\big\{(m-1)\big[\lambda_T(D_H+s_0+1)-\kappa(s_0+2)\big]\big\},
\]
with \(c(\gamma)>0\) independent of \(m\). Since \(\lambda_T(D_H+s_0+1)-\kappa(s_0+2)\ge\check R_i\big(5C_{\rm isl}-1\big)\kappa>0\), no amplitude uniform in volume exists.

*Construction.* Coordinates \((x_1,x')\in\mathbb Z\times\mathbb Z^3\) on a torus of side larger than the configuration plus \(2D_H\). Put \(p_1=G_0+1\), \(p_{k+1}=p_k+D_H+s_0+1\), and hubs \(\widetilde H_k=[p_k,p_k+D_H-1]\times[0,D_H-1]^3\), \(k=1,\dots,m\). Consecutive hubs are at distance \(s_0+2\ge s_0\). Hulls are \(H_k=\widetilde H_k\) shrunk by two layers. Put \(\bar x'=(\lfloor D_H/2\rfloor,\lfloor D_H/2\rfloor,\lfloor D_H/2\rfloor)\), \(c_1=(0,\bar x')\), \(c_2=(p_m+D_H+G_0,\bar x')\). The gas is \(\{c_1,c_2\}\); the live set is empty. Then \(d(c_k,\text{hubs})=G_0+1\ge G_0\), and
\[
 d(c_1,c_2)=2G_0+1+mD_H+(m-1)(s_0+1).
\]
The conditions (7) are conditions on \(\check R_i\) only and hold below the ceiling.

Exempt term: one boundary term \(f\) with reads \(b_k\in c_k\) (a free bond), \(X(f)=\{c_1,c_2\}\), and \(X_f=\{c_1,c_2\}\cup\bigcup_k\widetilde H_k\cup(\text{axis cubes } \{(x_1,\bar x')\}\text{ between them})\). In \(\Gamma^\natural\), the axis path \(c_1\to[\widetilde H_1]\to\dots\to[\widetilde H_m]\to c_2\) has \(\ell:=2(G_0+1)+(m-1)(s_0+2)\) edges and covers \(\pi X_f\). Put \(d_f:=\ell\). Then (8) holds with \(C_{\rm pr}=1\), and \(X_f\) meets a hub. Put \(\widehat\omega_f:=\min\{1,N_{\rm ex}\}\), \(\widetilde\omega_f=\widehat\omega_fe^{-\kappa d_f}\), \(b_f:=\widetilde\omega_f/2\). The per-cube sum (6) has one term.

Response and source: take the source map \(S(v)=v\) on rows, \(v_0=0\), \(u(\zeta)=c_Tg\,\zeta\) cube-locally, and the response \(h(s;P,S):=\varepsilon_\Psi\Psi S\), independent of \(s\) and \(P\). Here \(\Psi\) places each row's value as the \(H\)-component on its own bond and zero elsewhere, and \(\varepsilon_\Psi:=\min\{1,C_D/C_\nabla\}\), where \(C_\nabla\) bounds \(n_b\) of a single-bond \(H\) by its size. Then \(h\) is holomorphic, zero at zero source, reads on each switch component only its own rows, and \(n_b(h)\le C_D\|S\|_{\rm src}\le C_DE_{\bar\kappa}\|S\|_{\rm src}e^{-\mu_Rd_+(b,\operatorname{supp}S)}\), because \(h\) vanishes near \(b\) unless the row of \(b\) lies in \(\operatorname{supp}S\), where \(d_+=0\). Its Lipschitz and chart conditions hold with \(C_A=1\). Take scalar functionals \(\lambda_k\) on shifts with \(|\lambda_k(h)|\le n_{b_k}(h)\) and \(\lambda_k(\varepsilon_\Psi\Psi S)=\varepsilon_\Psi c_\Psi S_{b_k,1}\), \(c_\Psi>0\) fixed (the \(l|H|\) entry of \(n_b\)). Define
\[
 \Phi_f(P,h):=b_f\,\frac{\lambda_1(h)}{A_{b_1}}\,\frac{\lambda_2(h)}{A_{b_2}} .
\]
On \(\mathcal A_f\), \(|\lambda_k(h)|<A_{b_k}\), so \(|\Phi_f|\le b_f\). It is holomorphic and real at real data. Since \(b_k\)'s row lies in \(\mathcal S\), \(A_{b_k}=A_V\).

*Failure.* \(h_0=0\) and \(G(\mathbf1,\zeta)=\varepsilon_\Psi c_Tg\Psi\zeta\). So \(F(\zeta)=b_f(\varepsilon_\Psi c_\Psi c_Tg/A_V)^2\zeta_{b_1,1}\zeta_{b_2,1}\), and its mixed difference at \((t_1,t_2)\) is \(F\) itself. Lemma 6.0 with \(t_k\uparrow\mathfrak b\) gives
\[
 \tfrac12\widehat\omega_f\Big(\frac{\varepsilon_\Psi c_\Psi c_Tg\mathfrak b}{A_V}\Big)^2e^{-\kappa\ell}\le4a\,e^{-\lambda_Td(c_1,c_2)}.
\]
Insert \(\ell\) and \(d(c_1,c_2)\); the \(m\)-dependent part of the exponent is \((m-1)[\lambda_T(D_H+s_0+1)-\kappa(s_0+2)]\). With \(D_H=C_{\rm isl}L\check R_i+6\), \(s_0=\check R_i-4\) and \(\lambda_T\ge5\kappa/L\),
\[
 \lambda_T(D_H+s_0+1)-\kappa(s_0+2)\ge5C_{\rm isl}\kappa\check R_i-\kappa(\check R_i-2)\ge\check R_i(5C_{\rm isl}-1)\kappa .
\]
∎

*What Proposition 6 shows, and the corrections to TDd Proposition 7.1.* (i) The bookkeeping needs only G's own bounds: spacing \(s_0\) and hub side \(D_H\). No ratio \(\check R_i/\check R_{i-1}\) occurs, so the defect named at TD 447 is gone. (ii) The data satisfy TD's stated premise (8), but **not** (X°): any ordinary tree meeting \(c_1\) and \(c_2\) has at least \(d(c_1,c_2)\) edges, which exceeds \(C_{\rm pr}(1+\ell)\) for large \(m\). (iii) Hence the proposition refutes the contracted premise, not SA. Under the literal reading of SA 6193–6195 (TD Proposition 11), this boundary term would have \(d_f\ge d(c_1,c_2)/C\), and Theorem A covers it. (iv) The proposition does show that "no decay across an exempt island" (SA 6198) must not be read as a free crossing between unexcused cubes. If SA intends that reading, ordinary TD fails at the level of (R23), and CI must instead assume TD-natural and solve TD's filing problem (TD 375–379).

### 6.2 The island constant must be early

**Proposition 7 (necessity of (G-ord))** [CE, under the model hypothesis (Mon) below]. Suppose \(C_{\rm isl}\) may be chosen after \(\bar\kappa\). Assume (Mon): for the two read bonds \(b_L,b_R\) below, \(d_+(b_L,\text{rows of }c_1)\le d_+(b_L,\text{rows of }c_2)\), and the mirror statement for \(b_R\). Then there are data satisfying R, A (an island), X, (X°) and G for which ordinary TD fails for every \(\lambda_T\ge\lambda_V\) once
\[
 C_{\rm isl}>\frac{20(\bar\kappa+2)}{\lambda_V}-20 .
\]
Hence any proof of ordinary TD from these inputs needs \(\bar\kappa\) chosen after \(C_{\rm isl}\), with a floor of the form (T2).

*Construction.* One hub \(\widetilde H=[p,p+D_H-1]\times[0,D_H-1]^3\), \(c_1=(p-G_0-1,\bar x')\), \(c_2=(p+D_H+G_0,\bar x')\); gas \(\{c_1,c_2\}\), live set empty, \(\mathcal S=\) rows of \(c_1,c_2\). Then \(d(c_1,c_2)=2G_0+D_H+1\). Island term \(f\): reads \(b_L\) in the hub cube \((p,\bar x')\) and \(b_R\) in \((p+D_H-1,\bar x')\); \(X_f=X^\uparrow\subset\widetilde H^+\); \(d_f=0\); \(T_f=\{(p,\bar x')\}\). Then (X°) holds.

Response (walk model): for a bond \(b\) on the axis line and a row \(r\) of \(c_1\) (if \(b=b_L\)) or of \(c_2\) (if \(b=b_R\)), put
\[
 h_b(s;S):=\varepsilon_\Psi\sum_re^{-\mu_Rd_+(b,r)}\,\tau_0^{\,d(\Delta_r,\Delta_b)}\Big(\prod_{c\in[\Delta_r,\Delta_b]}s_c\Big)S_r,\qquad\tau_0:=e^{-\bar\kappa-2},
\]
where \([\Delta_r,\Delta_b]\) is the straight face-connected axis segment, and \(h=0\) elsewhere. If a term is nonzero, the whole segment lies in \(\operatorname{supp}s\); so the response on each face-component reads only that component's rows and switches. On \(|s_c|<e^{\bar\kappa}\) the product is at most \(e^{\bar\kappa(n+1)}\), \(n=d(\Delta_r,\Delta_b)\), so \(|h_b|\le\varepsilon_\Psi e^{\bar\kappa}\|S\|\,e^{-\mu_Rd_+(b,\operatorname{supp}S)}\sum_rN_{\rm row}e^{-2n}\). With \(\varepsilon_\Psi:=C_De^{-\bar\kappa}/(4C_\nabla N_{\rm row})\) this is (3). It is linear in \(S\), so it vanishes at zero source and is holomorphic.

Island function: \(\Phi_f:=(\omega/4)(\lambda_L(h)/A_{b_L})(\lambda_R(h)/A_{b_R})\), with \(A_f:=\omega/4\), \(B_f:=\omega/2\), \(\omega:=\min\{1,N_{\rm ex}\}\). Then \(\operatorname{Re}\Phi_f\le A_f\) on \(\mathcal A_f\) and (5) holds since \(h_0=0\).

*Failure.* By (Mon), the row \(r_1\in c_1\) nearest \(b_L\) in \(d_+\) attains \(d_+(b_L,\mathcal S)\); so \(e^{-\mu_Rd_+(b_L,r_1)}/A_{b_L}=1/A_V\). Likewise for \(b_R\), \(r_2\). Take \(\zeta\) supported on \(r_1,r_2\). The mixed difference of \(F\) is
\[
 \frac\omega4\Big(\frac{\varepsilon_\Psi c_\Psi c_Tg}{A_V}\Big)^2\tau_0^{2(G_0+1)}\,t_1t_2\ \ge0 ,
\]
since the response at \(b_L\) reads only \(c_1\) and at \(b_R\) only \(c_2\). Lemma 6.0 gives \(a\ge c(\gamma)\exp\{\lambda_T(2G_0+D_H+1)-2(G_0+1)(\bar\kappa+2)\}\), with \(c(\gamma)\) polynomial in \(\ell\) at fixed early constants. The exponent is \(L\check R_i[\lambda_T(20+C_{\rm isl})-20(\bar\kappa+2)]+O(\bar\kappa)\). Under the stated inequality it tends to \(+\infty\) faster than any power of \(\ell\), since \(\check R_i\ge(\ell-1)^r\). So no \(a\) with \(a\to0\) exists. ∎

*On (Mon).* (Mon) is a property of ST1's input metric \(d_+\) on the two read bonds; it holds when \(d_+\) restricted to the configuration is nondecreasing in axis separation. I have not derived it from ST1 and mark it **[R]**. Proposition 7 is a sharpness statement; nothing on the critical path uses it.

*On another possible payer.* The admission room in A is \(A_b=A_Ve^{-\mu_Rd_+(b,\mathcal S)}\). The actual room of an island read (PAN Lemma 7.4) does not shrink with the distance to \(\mathcal S\). A composition lemma normalised by the actual room would gain a factor \(e^{-\mu_Rd_+(b,\mathcal S)}\), of order \(e^{-\mu_RM\,G_0}\) in fine-cube units if \(d_+\) is a lattice metric, and could pay hub crossings with \(M\) large instead of \(\bar\kappa\). That route needs a new room import and is not used.

---

## 7. Constant order

Theorem A adds the following to TD Theorem 10's order. "Early" means fixed before \(\kappa\), independent of \(M\) and \(\bar\kappa\).

| Constant or condition | Where fixed | Before \(\kappa\)? | Independent of \(M,\bar\kappa\)? |
|---|---|---|---|
| \(C_{\rm isl}\) (island cells), \(c_{\rm col}\), \(C_{\rm pr}\) | IN1 row 2, geometric, uniform in \(L\) | yes | yes |
| \(\eta_H=1+C_{\rm isl}/10\) | row 2 | yes | yes |
| \(L\) floor \(L>8C_{\rm pr}A_{\rm old}\) (with the existing \(L>4C_h^{\rm WF}A_{\rm old}\)) | row 2 | yes | yes |
| \(\kappa\) floor \(\kappa\ge8C_{\rm pr}(B_{\rm old}(L)+1)\) | row 4 | (is the \(\kappa\) choice) | yes |
| \(\lambda_V\) in IN1 (24); \(\lambda_T=\lambda_V+1\) | row 4, after \(\kappa\) | no (after) | yes |
| (T2): \(\log(e^{\bar\kappa}-1)\ge2\lambda_T(2+C_{\rm isl}/10)+36+\log6400\) | the \(\bar\kappa\) step, after \(\lambda_V\) | no | is the \(\bar\kappa\) floor; independent of \(M\) |
| \(\nu=\min\{\kappa/(4C_{\rm pr}),a_1/2\}\) | after \(\bar\kappa\) | no | independent of \(M\) |
| \(N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}\) | after \(M\), before \(\gamma\) | no | depends on \(M\) (amplitude only) |
| (T3) \(\vartheta e^{\lambda_Tc_{\rm col}}<1\), (T4), G's (7) | ceilings on \(\gamma\) | — | — |

*The window.* (T1) needs \(\lambda_V+1\le\kappa/(4C_{\rm pr})\). Take \(\lambda_V=A_{\rm old}\kappa/L+B_{\rm old}(L)\) at IN1 (24)'s lower endpoint, with TD's \(A_{\rm old}=bC_h^{\rm UM}c_\ell\), \(B_{\rm old}(L)=\lambda_0+\sigma_0+C_h^{\rm UM}(3+c_\ell g_*)/L\), \(b=1+4\beta_s\). If \(L>8C_{\rm pr}A_{\rm old}\), then \(1/(4C_{\rm pr})-A_{\rm old}/L>1/(8C_{\rm pr})\), and \(\kappa\ge8C_{\rm pr}(B_{\rm old}(L)+1)\) gives (T1). Both are floors, \(L\) before \(\kappa\). TD's (32) with \(A_*\ge A_{\rm old}\), \(B_*\ge B_{\rm old}\) and its \(\kappa\)-floor also implies (T1) up to the extra \(+1\); either choice works.

*Amendment 1.* On the ordinary route the natural window, the constants \(c_1,c_2,\sigma_2,\Theta^\natural\) and the floor \(L>L_0^\natural\) are not needed. Keeping them is harmless: raising floors weakens no step (IN1 676). The new requirements are the \(L\) floor \(8C_{\rm pr}A_{\rm old}\) and the \(\kappa\) floor above. Their slope gap is \((1/(4C_{\rm pr})-A_{\rm old}/L)\kappa\), as TD 421 asks for Amendment 1. No cycle: \(C_{\rm isl}\) is read only by the \(\bar\kappa\) floor and by ceilings on \(\gamma\).

*\(M\) only as a lower bound.* \(M\) enters only through \(N_{\rm ex}\) and the imported floors (\(M\ge R_\sigma+3\), ST1 row 8's \(M\ge C_{\rm dec}\bar\kappa\)). No condition of Theorem A is a ceiling on \(M\).

---

## 8. What closes CI

### 8.1 The regular gas with ordinary exempt potentials

**Theorem B (CI reduction on the ordinary route)** [P, as an implication]. Assume `(CI-old)`, the admission hypotheses of ST1 Theorem 14 and ST3 Theorem 14′ used in A, R, A, X, (X°), G, (G-ord), RUN, CI's H-D, H-G, H-S, H-C, H-W (and H-O, H-F if used), the constant order of CI with §7 added, and (T1)–(T4). Then:

1. CI's TD (CI 87–94) holds with \(\lambda_T=\lambda_V+1\ge\lambda\) and \(a_E=a_T\to0\) (Theorem A). The connected regrouping \(V^\circ\) satisfies the ordinary-type bound (17) of TD's J, with \(\ell_t=d_f\) and amplitude \(2a_T\), without the quadratic allowance (Corollary A′).
2. CI Theorem 5 applies: the regular gas formed by CI (9)–(11) with the exempt type \(V^\circ\) satisfies CI (28)–(29), with the **ordinary** coarse length \(\ell_c(X)=d_c(X)+5\) on raw unions, holomorphic, Borel and real on the common fibre.
3. In TD Theorem 9's filing requirement (TD 365–369), the third bullet reduces to CI's existing filing step for island-free histories (CI 352: "the specified scale and hull comparison"). The raw-union bound is in the ordinary length, and no island exemption is claimed, so the full-island containment condition is vacuous. TD's second filing failure (TD 379) does not occur. CI 352's comparison itself stays an input, as in CI.

Consequently CI at an exempt main step follows from NL1-L's CI induction, as in TD Theorem 9, **once the first two bullets of TD Theorem 9 hold**: actual external-pair and stored-variable carriers with declared chain domains, and exact regrouping with summable multiplicities, heredity and covariance.

*Proof.* Item 1 is Theorem A, Corollary A′ and \(\lambda_T\ge\lambda_V\). For item 2: CI Theorem 5's hypothesis list names TD "whenever exempt terms occur" (CI 330) and otherwise uses H-D, H-G, H-S, H-C, H-W and the constant order; item 1 supplies TD, and §7 keeps the order. The exempt type is one more connected ordinary type; CI's type count stays fixed. For item 3: CI (28) bounds raw unions in the ordinary coarse length, as for island-free histories, so the filing step is CI 352's, unchanged. A boundary filing would use SA's relative length, which is at most the ordinary length (SA 6197), so the ordinary bound implies the relative one. No exemption is claimed, so no containment is needed. TD's obstruction at TD 379 was the inequality \(d_i^\natural(\mathcal S';X)\le d^{\natural c}(X)\) between a relative and a *contracted* length; on this route no contracted length occurs. The induction step is TD Theorem 9's, with these inputs. ∎

*What Theorem B does not change.* The imports remain as listed in TD's Result (TD 482): actual DR, complete admission, the complex island amplitude (5), per-cube amplitude sums, hub geometry, actual Gaussian and hereditary structure (TD's J and its Outstanding Gaussian identification, TD 235), and the ordinary potential bounds. The island-formation bounds `(Size-isl)`, `(Loc-isl)` remain LF1 inputs (TD 379).

### 8.2 The remaining filing statement

TD's first filing failure is not about lengths. Its example (TD 377) is \(F(p,B)=\epsilon p_zB_c\): Boolean localisation in \(B\) leaves the read of \(p_z\) at a remote \(z\). Here the remote reads are of two kinds. \(\Phi_f\) reads \(P\) on \(X_f\), which may be a whole island hull far from \(W\). The response \(h(s;P,S)\) reads \(P\) wherever its walks go; in particular \(h_0(P)=h(\mathbf1;P,S(v_0))\) reads \(P\) along walks from the whole stored source \(\mathcal S\). Note that the same question arises for class terms: CI's H-C presentations have exact component locality in \((s,\zeta)\) (CI 58, NL1-L Theorem 4(2)), not in \(P\).

**(File-P) — external-pair carriers of exempt pieces** [O, owners ST1 (response), NL1-L/LF1 (filing)]. For every exempt \(f\) and nonempty \(W\) there is an exact finite decomposition
\[
 f_W(P;\zeta)=\sum_{Y}f_{W}^{(Y)}(P|_{Y};\zeta),
\]
over connected fine sets \(Y\supset W\cup X_f\), each piece defined on the declared chain domain \(\mathcal O_\sigma(Y;U)\) with H-S's restriction and covariance, such that for every cube \(c\)
\[
 \sum_{f}\ \sum_{Y\ni c}\ \sup|f_W^{(Y)}|\,e^{\lambda_P\,\ell^{\rm rel}(Y)}\le C\,a_T e^{-\lambda_V d_f(W)}
\]
(summed also over \(W\) as needed by the gas), where \(\ell^{\rm rel}(Y)\) is the relative length with the collared hubs inside \(Y\) excused, and \(\lambda_P\) is a fixed fraction of \(\kappa\).

Matching \(\ell^{\rm rel}\) (which excuses collared hubs) with IN1's boundary class (which excuses level-\(j\) hulls) is part of the filing import.

### 8.3 Three attacks on (File-P)

**Attack 1 — Boolean localisation in \(B\) alone.** *Fails.* The pieces \(f_W\) are local in \(\zeta\) on \(W\) but not in \(P\). TD 377's example \(\epsilon p_zB_c\) satisfies every bound of Theorem A at small \(\epsilon\), and its read at \(z\) does not disappear under any Möbius inversion in \(\zeta\). *Exact reason:* the Boolean variables are fluctuation variables; \(P\) is not one of them.

**Attack 2 — switch Möbius under (DR-locP), with geometric-mean bounds.** Assume (DR-locP) and the following extension of A's island hypothesis (5):

> **(5-sw)** [O, extends TD's Outstanding complex island amplitude]. On the switched polydisc \(|s_c|<e^{\bar\kappa}\), \(s|_{X_f}=1\), \(|\zeta|_c<R\), the presentation \(F_f(P;s,\zeta):=\Phi_f\big(P,h(s;P,S(v_0+u(s\odot\zeta)))\big)\) satisfies \(|F_f-f_0|\le\widetilde\omega_f^{\rm sw}\le C_{\rm sw}\widehat\omega_fe^{-\kappa d_f}\), and (5) holds at every corner \(s_A=\mathbf1_{X_f\cup A}\).

For a finite set \(V\) of cubes outside \(X_f\), put
\[
 f_{W,V}(P;\zeta):=\sum_{A\subset V}(-1)^{|V\setminus A|}\,D_W\big[F_f(P;\mathbf1_{X_f\cup A},\cdot)\big](\zeta).
\]

**Proposition 8.1** [P from (DR-locP), (5-sw), R, A, TD Lemmas 2–4]. (i) \(f_W(P;\zeta)=\sum_{V}f_{W,V}(P;\zeta)\), the sum over all subsets of the complement of \(X_f\). (ii) \(f_{W,V}=0\) unless \(W\subset X_f\cup V\) and \(X_f\cup V\) is connected. (iii) \(f_{W,V}\) depends on \(P\) only through its restriction to \(N_{c_P+1}(X_f\cup V)\). (iv)
\[
 |f_{W,V}|\le\big(\widetilde\omega_f\widetilde\omega_f^{\rm sw}\big)^{1/2}\,(2\vartheta)^{|W|/2}\,(2/D)^{|V|/2}\,e^{-\frac{a-6}2m_{X(f)}(W)}
\]
on \(|\zeta|_c\le\mathfrak b\).

*Proof.* (i) Möbius inversion on the finite set of cubes outside \(X_f\), at the corner \(\mathbf1\). (ii) At \(s_A\), the factor \(s_A\odot\zeta\) kills \(\zeta\) off \(X_f\cup A\), so \(D_W\) vanishes unless \(W\subset X_f\cup A\subset X_f\cup V\). If a cube \(v\in V\) is not joined to \(X_f\) inside \(X_f\cup V\), then toggling \(v\) does not change the component of \(X_f\) in \(\operatorname{supp}s_A\); by NL1-L Theorem 4(2) the value does not change, and the alternating sum in \(v\) vanishes. (iii) At \(s_A\), \(\Phi_f\) reads \(P\) on \(X_f\) (admission A), and every read \(b\in\mathcal B_f\) has its stencil in \(X_f\) (carrier definition, CI 18). The response there is the response on the component of \(X_f\cup A\) containing \(X_f\); by (DR-locP) it reads \(P\) only within \(c_P\) of that component. Its sources are the rows of that component, and each source row reads its cube and one neighbour layer (R). (iv) *Switch bound.* Fix \(\zeta\). The function \(g(s_V)=D_W[F_f(P;s,\cdot)](\zeta)\), with \(s=1\) on \(X_f\) and \(0\) off \(X_f\cup V\), is holomorphic on \(|s_c|<e^{\bar\kappa}\) (\(c\in V\)) and bounded by \(2^{|W|}\widetilde\omega_f^{\rm sw}\), because \(f_0\) cancels in the alternating sum. Write the alternating corner sum as \(\int_{[0,1]^V}\partial_{s_V}g\). At each point of \([0,1]^V\) the polydisc of radii \(D=e^{\bar\kappa}-1\) lies in the domain, so Cauchy gives \(|f_{W,V}|\le2^{|W|}\widetilde\omega_f^{\rm sw}D^{-|V|}\). *Fluctuation bound.* \(|f_{W,V}|\le2^{|V|}\max_A|D_W[F_f(P;s_A,\cdot)]|\). At a corner \(s_A\) the response is \(h(s_A;\cdot)\). TD Lemma 2's expansion runs over switch sets \(Y\supset B_b\) inside \(\operatorname{supp}s_A\); the coefficients are those of the expansion at \(\mathbf1\), and fewer of them occur, so (12) holds at \(s_A\) with the same constant. R's bound gives \(n_b(h(s_A;P,S(v_0)))\le A_b/3\). With (5-sw) at \(s_A\), TD Lemma 4 applies at \(s_A\): \(|D_W[F_f(P;s_A,\cdot)]|\le\widetilde\omega_f\vartheta^{|W|}e^{-(a-6)m_{X(f)}(W)}\). Take the geometric mean of the two bounds. ∎

*Where Attack 2 fails.* The per-cube sum in (File-P) at a cube \(c\in X_f\) runs over all \(V\), because every carrier \(X_f\cup V\) contains \(c\). The bound (iv) has no decay in the distance from \(V\) to the reads. For an island, \(X_f\supset\) a hull face of about \(D_H^3\) cubes, and single-cube sets \(V\) adjacent to it already contribute about \(D_H^3(2/D)^{1/2}\); sets of \(k\) separated cubes contribute about \((D_H^3(2/D)^{1/2})^k/k!\). The bound sums to \(\exp\{cD_H^3D^{-1/2}\}\), and \(D_H\to\infty\) as \(\gamma\downarrow0\) while \(D\) is fixed. *Exact reason:* PAN F3 (PAN 495): attachments anywhere along a large read set, with only a per-cube switch cost. This is a failure of the bound, not a proof that the true sum diverges.

**Attack 3 — joint switch–fluctuation composition with a logarithmic excused collar.** Keep the switches equal to one on the collar \(N_\rho(X_f)\), with
\[
 \rho=\rho_i:=\Big\lceil\frac{8}{a-6}\log(D_H+2c_{\rm col}+3)\Big\rceil ,
\]
and expand only outside it. \(\rho_i\) grows like \(\log\check R_i\), so \(\rho_i\le G_0/4\) below a ceiling on \(\gamma\). The collar is excused in \(\ell^{\rm rel}\); it lies in a box of side \(D_H+2c_{\rm col}+2\rho_i\), still of ratio \(\le\eta_H+o(1)\) to the gap. The needed estimate is:

> **(JC) joint composition** [O]. Under R, A and (5-sw), for \(V\) outside \(N_\rho(X_f)\),
> \[
>  |f_{W,V}|\le C\,\widetilde\omega_f^{\rm sw}\prod_{c\in W}\frac{2\beta_c}{\delta}\;\Big(\frac{C}{D}\Big)^{|V|/2}\;e^{-(a-12)\,m_{N_\rho(X_f)}(W\cup V)} .
> \]

*Route to (JC).* Treat each switch cube as a second Boolean variable of its cube. TD Lemma 2's proof already bounds the switch coefficients of the response at a read \(b\) by \(D^{-|Y\setminus B_b|}\) over connected \(Y\supset B_b\); a switch cube at distance \(n\) from the reads forces \(|Y|\ge n\). This should give response pieces indexed by pairs (fluctuation set, switch set) with a joint hull product, and then TD Lemma 3 with two labels per cube, at the cost of a larger animal constant in TD (9). I have not written this proof; the doubled entropy and the corner-switch admission need to be checked line by line.

*Given (JC), the sums close* [P from (JC)]. At a cube \(c\in X_f\) the sum over \(V\) is a sum over forests rooted at the collapsed vertex \(N_\rho(X_f)\). Its weight is at most \(\exp\{\sum_{y:d(y,X_f)\ge\rho}C'e^{-(a-12)d(y,X_f)}\}\). The shell at distance \(n\) has at most \(8(D_H+2c_{\rm col}+2n+1)^3\) cubes, so the exponent is at most \(C''(D_H+2c_{\rm col}+2\rho)^3e^{-(a-12)\rho}\) (a geometric tail in \(n\ge\rho\)). When \(a-12\ge(a-6)/2\), the choice of \(\rho\) gives \(e^{-(a-12)\rho}\le(D_H+2c_{\rm col}+3)^{-4}\), and \(2\rho\le D_H\) below a ceiling on \(\gamma\); so the exponent is bounded by a constant fixed before \(\gamma\). At a cube \(c\notin N_\rho(X_f)\) the sum is rooted at \(c\) and is bounded by TD (9). The relative length satisfies \(\ell^{\rm rel}(X_f\cup V)\le C_{\rm pr}(1+d_f)+(1+\eta_H)m_{N_\rho(X_f)}(V\cup W)+c_{\rm col}|V\cup W|\) by Lemma 3.1's argument with \(N_\rho(X_f)\) excused. So a fixed fraction of the decay pays \(e^{\lambda_P\ell^{\rm rel}}\).

*Exact reason Attack 3 stops.* It consumes (DR-locP), which R and H-DR do not supply (NL1-L 170–171: "at fixed \(P\)"), and (JC), whose proof is outlined but not written. A3 does not touch the gas assembly with P-labels (each cluster term's P-carrier is the union of its Gaussian region and its pieces' carriers); that step is a further bookkeeping item for the filing.

**The first remaining Outstanding statement is (DR-locP).** Attack 1 shows that no device in \(B\) creates \(P\)-locality, and Attacks 2 and 3 both use (DR-locP). It is a statement about ST1's actual response. SA describes the mechanism (walk switches at SA 17905–17907; splitting of the equations at SA 5794–5797) but does not prove it for our DR. If the actual operator reads a background that depends on the pair globally, (DR-locP) needs its own walk expansion of that background. Then come (JC), (5-sw) and the P-labelled assembly, in that order.

---

## 9. Status

### 9.1 Statements of this draft

| Statement | Status |
|---|---|
| Lemma 3.1 (ordinary spanning through an exempt carrier) | [P] from (X°), G, (T4) |
| Lemma 3.2 (the gap is paid) | [P] from (X°), G |
| Theorem A (ordinary TD, \(\lambda_T=\lambda_V+1\), \(a_T\to0\)) | [P] from TD Lemma 4, R, A, X, (X°), G, (G-ord), RUN, (T1)–(T4) |
| Corollary A′ (connected supports, rate \(\lambda_V\)) | [P] from Theorem A |
| §5.1 (C3 cannot pay) | [P] as stated: bounded versus unbounded |
| Lemma 6.0 (mixed differences) | [P] |
| Proposition 6 (TD (8) insufficient; chain at spacing \(s_0\)) | [CE] |
| Proposition 7 ((G-ord) necessary) | [CE] under the model hypothesis (Mon) [R] |
| §7 order (floors \(L>8C_{\rm pr}A_{\rm old}\), \(\kappa\ge8C_{\rm pr}(B_{\rm old}+1)\), (T2)) | [P] no cycle |
| Theorem B (CI reduction on the ordinary route) | [P] as an implication |
| Proposition 8.1 (switch Möbius pieces) | [P] from (DR-locP), (5-sw) |
| Closing of sums given (JC) | [P] from (JC) |

### 9.2 Imports and Outstanding items

| Item | Owner | Status |
|---|---|---|
| R, A, X, G, J, RUN of TD; admission (ST1 Thm 14, ST3 Thm 14′) | ST1, NL1-L, LF1, IN1 | [I], as in TD |
| Complex island amplitude (5) | NL1-L/PAN | [O] (TD 63) |
| (X°) ordinary carrier premise | NL1(1)/LF1 | [I]; same projection and containment as TD 90, before contraction |
| (G-ord) island constant early | LF1(2) | [I]; [R] SA 17575, PAN 57, 425; TD Thm 10 step 4 must move \(C_0\) |
| (DR-locP) | ST1 | **[O] — first remaining** |
| (JC) joint composition | this lane | [O], route in §8.3 |
| (5-sw) island bound at corner switches | NL1-L/PAN | [O] |
| P-labelled gas assembly and class matching of excused collars | NL1-L/LF1/IN1 | [O] |
| (Mon) in Proposition 7 | ST1 | [R], sharpness only |

### 9.3 Corrections proposed to other notes (not made; no frozen file edited)

- **TD (8):** state it before contraction, as (X°). The contracted form does not imply ordinary TD (Proposition 6).
- **TD Theorem 10 step 4:** move the island constant (\(C_0\), here \(C_{\rm isl}\)) to step 1 with the geometric constants. Check whether step 4's "\(C_0\)" was CI row 5's unrelated post-\(M\) constant.
- **TD Result and CI:** ordinary TD is proved under (X°) and (G-ord); TD-natural and the linked gas are not needed for CI. TD's second filing failure does not arise on the ordinary route.
- **TDd Proposition 7.1:** its construction is a valid counterexample to the contracted premise, with spacing \(s_0\) and no radius ratio (Proposition 6). It is not a gap in SA under the literal reading.
- **IN1 Amendment 1:** on the ordinary route its natural-window floors may stay but are not needed; the floors \(L>8C_{\rm pr}A_{\rm old}\) and \(\kappa\ge8C_{\rm pr}(B_{\rm old}(L)+1)\), and the \(\bar\kappa\) floor (T2), are what Theorem A needs. This is for the lead; IN1 is frozen.

### 9.4 Checks this draft needs (for the referee)

1. Lemma 3.1, Case 2: the Chebyshev-distance step inside a non-wrapping box, and the count \(\#\{\text{Case 2}\}\le m/(G_0-c_{\rm col})\).
2. Theorem A's split of exponents and the charge to the nearest read cube.
3. That SA's projected relative tree gives (X°)(a) with a collar fixed before \(\kappa\), including the read enlargements \(X^\uparrow\).
4. Proposition 6's model response: that it satisfies every clause of R with the actual seminorm \(n_b\) (the constants \(C_\nabla,c_\Psi\)).
5. Proposition 8.1(iv): TD Lemma 2 at corner switches.

Only `library/td2-draft.md` is written. Retrieval, searches and file bookkeeping discharge no mathematical step. The text is not refereed, is not an audit and grants no status.
