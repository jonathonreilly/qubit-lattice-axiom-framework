lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T04:14Z

# d3-local-check: `library/d3-local.md` Sections 2–3, line by line (queue row 230)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session, no subagents; branch `claude/ym4d-hard-route` at `642076279`. Checked text: `library/d3-local.md` (Codex) at that commit. Sussman–Alpoge `YM4_sketch_500.tex` (SA) and `YM3/YM3_I.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (sha256 `d7f77d4d…4d6f` and `248959db…c443`), not copied here. One reading by one other model. Not an audit; grants no status. No numeric job was run. I redid every step by hand.

Kind of result: check of our own new text (FINISH item 10, so no outline line is needed).

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the constructions this check reads: SA (UM3), (UM29), (BGD5)–(BGD6), the normaliser and kept-form paragraphs (SA L17541–17558) and the local Gaussian comparison (SA L13954–14262); YM3_I Definition II-19-15 with (St2) and (II-19-21), Proposition II-44-37, and (II-64-11)–(II-64-15). Tadeusz Balaban for the constrained-response and random-walk machinery behind these notes. OpenAI Codex wrote `d3-local.md`.

## Verdict

| Statement in `d3-local.md` | Verdict |
|---|---|
| §2 Local Gaussian structure: \(C,\Gamma\) read only the live region and split over wall-components (L35–40) | **ADVANCE** |
| §2 Normaliser: (1) is exact, local, and zero on disconnected \(X\) (L42–53) | **ADVANCE** |
| §2 Kept forms: (2) splits exactly into local polymer pieces (L55–62) | **ADVANCE** |
| §2 Other normalisers and \(z\)-factors (L64) | **ADVANCE** |
| §3 Current (3): existence, walk form (4), component locality, zero where there is no datum, exact on the physical locus (L66–92) | **ADVANCE** |

Checked line by line by Claude, first failing step none. Each verdict is an implication from the inputs the note names, plus one input it uses without naming (G2 in Section 4). No defect breaks a consumer. Section 4 gives two missing lines and their repairs.

## 1. Sources read first

SA L3918–3935, L5755–5800, L6228–6265, L8230–8246, L8300–8362, L9995–10080, L10395–10456, L10546–10560, L13954–14420, L14676–14775, L17525–17560, L18730–18756. YM3_I L37769–37800, L37885–38010, L38490–38580, L40600–40950, L51150–51260, L51708–51726. Repository: `loc-3.md` §4 ((D1)–(D3), Lemma C), `wf-room-2.md` §6.2–6.3, `wf-room.md` (5.2), `nl-r9.md` (3.2)–(3.3) and (4.2), `o1-decoupled.md` Definition D, Lemma WC and Theorem B, `um1-fix.md` (F) and Corollary R′, `h-walk-fix.md` §5, `a3-derivative.md` (27). I read `regional-gauss.md` §§3–4 for context only; row 233 checks it.

The quoted passages support the classification that Sections 2–3 rely on:

- SA L14406–14410 names "heredity, normalized-functional and wall-factorization identities" as the remaining hypotheses of the UM gas. Section 2 supplies the first and the third. SA (FG6) (L13966) gives the second.
- SA L17541–17548 sketches the normaliser: alternating sums over \(Y\subset X\) of "the diagonal entries of the logarithm of the operator built on \(Y\)". YM3 Proposition II-44-37 proves the 3D form per bond.
- SA L17550–17556 states the kept-chain test. YM3 (II-64-11)–(II-64-15) and Proposition II-64-65 prove the 3D form.
- SA L5785–5790: the current is "a second component of this input"; "the multiplier construction and its uniform bounds are required independently". SA L10404–10406 says only that the increment is "formed from the multiplier". SA L5793–5797 requires the response to split over wall-components and to be zero on a component with no datum. So the current's construction is assumed, as `d3-local.md` §1 says.
- SA L10449–10451: at \(s=1\) over a critical real background, \(F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\lambda\). Section 3's physical identification reads this.

## 2. Section 2, step by step

**2.1 Set-up (L33). ADVANCE.** The conventions for data and index sets are the ones Theorem W (a) reads. [RT] (`um1-fix.md` Corollary R′(b)) makes the index sets local: whether \(\omega\) is a term depends on the geometry only on \([\![\omega]\!]^+\).

**2.2 Live hulls (L35). ADVANCE, as a requirement on the tags.** It holds for the full monomial of Definition D, \(s^\omega=\prod_{\Delta\in\mathsf P(\omega)}s_\Delta\) with \(\mathsf P(\omega)\) the cubes that meet \([\![\omega]\!]^+\) (`o1-decoupled.md` (2.1)). SA mechanism (i) (L10552–10556) also tags every cube of \(\mathsf P(\omega)\); only its bound leaves the factor \(e^{2^4\bar\kappa}\). Lemma WC then puts each live hull in one wall-component: the closed grid cubes through one point form a wall-connected star, and connectedness of the hull carries this along.

**2.3 Splitting and the inverse (L35). ADVANCE.** An entry \((x,y)\) of a product of block-diagonal factors sums over intermediate points in the component of \(x\). If \(M=\bigoplus_iM_i\) is invertible, each \(M_i\) is injective, hence invertible. Then \(\bigoplus_iM_i^{-1}\) is a two-sided inverse, so it is \(M^{-1}\).

**2.4 \(C\) and \(\Gamma\) read only the live region (L36–40). ADVANCE.** The entries of \(\chi A(s)\chi^{\mathsf T}\) read only live hulls, and \(C\) is a function of these entries. An entry of \(\Gamma\) is \(-\sum_{v\notin Z_0}A(s)_{bv}r(s)_{vu}\). Each live term has \(b,v,u\) in one component. So \(\Gamma\) uses no auxiliary coordinate outside the live part of that component. This is (II-19-21) in "reads only" form. It holds at every complex \(s\) that vanishes outside \(Z\), not only at the Boolean points of YM3 L38529–38533. The reading of \(r(s)\) is SA L14167–14170.

**2.5 Factorisation (L40). ADVANCE, with one missing line (G1).** The joint precision (FG7) is block diagonal over the components, plus the identity on the unused auxiliary coordinates. The branch argument for the root is YM3 L37984–37990. This gives wall-factorization for a product integrand. With (FG6), \(\mathcal J[1]=1\). Then the term \(E(X)\) of (UM29) reads only \(X\), because it uses only \(H(Z)\) with \(Z\subset X\) (SA L14680–14682, L14735).

**2.6 Normaliser sum rule (L42–51). ADVANCE.**
\(\sum_{X\subset\mathcal P}n_X=\sum_{Y\subset\mathcal P}F(Y)\sum_{W\subset\mathcal P\setminus Y}(-1)^{|W|}=F(\mathcal P)\), with \(0^0=1\). Each summand of \(n_X\) reads only some \(Y\subset X\). For \(\mathcal P\) the whole torus, the erosion tower is the move's own sequence and the deep mask is the whole mask (`regional-gauss.md` (4)–(5)). So the requirement "full-region matrix = actual precision" is consistent. It is SA's \(-\tfrac12\log\det(\mathsf C^{\mathsf T}\Delta^{(j)}\mathsf C|_{\Lambda_{j+1}})\) (SA L17541). Writing \(\operatorname{Tr}\log A_Y\) bond by bond gives YM3's per-bond terms (II-44-16) and (II-68-22), so the remark at L53 is correct.

**2.7 Centring constants (L51). ADVANCE.** \(n_X(P_0)\) reads the trace on \(X\), so each slot's constant is itself a local piece. SA's "number" (L17541) is fixed per label, and the note's warning agrees with that.

**2.8 Tower split (L53). ADVANCE.** Let \(Y=Y_1\sqcup Y_2\) with no wall adjacency, \(x\in Y_1\), \(y\in Y_2\). The segment \([x,y]\) leaves \(Y_1\) at a point \(p\) in the closure of \(Y^c\). If the segment passes from \(Y_1\) straight into \(Y_2\), then \(p\) lies on a contact of codimension at least two. The closed cubes through \(p\) then include a cube of \(Y^c\); otherwise the star at \(p\) would join \(Y_1\) to \(Y_2\) through walls. Hence \(\operatorname{dist}_\infty(x,Y^c)\le\operatorname{dist}_\infty(x,Y_2)\). So each erosion test of `regional-gauss.md` (4) gives the same answer in \(Y\) and in its component. Induction on \(q\) splits \(T_q(Y)\), and the meet with \(\Omega_q\) splits too. An \(r_N\)-box inside \(Y\) lies in one component, so the deep mask splits. The note leaves this last point implicit, as YM3 does at L40920. Every stencil, average, contour and pivot map of the rebuilt construction then lies in one component. Sums, products, transposes and existing inverses keep the block form (2.3). Then \(A_Y=\bigoplus_iA_{Y_i}\), and the logarithm series of \(T_Y=\bigoplus_iT_{Y_i}\) splits. So \(F(Y)=\sum_iF(Y_i)\). This is the argument of YM3 L40892–40923.

**2.9 Disconnected \(X\) (L53). ADVANCE.** Let \(X_i\) be a wall-component of \(X\), with \(X\ne X_i\). Write \(Y=Y_i\sqcup Z\) with \(Y_i\subset X_i\) and \(Z\subset X\setminus X_i\). By 2.8 the coefficient of \(F(Y_i)\) in \(n_X\) is
\((-1)^{|X_i\setminus Y_i|}\sum_{Z\subset X\setminus X_i}(-1)^{|(X\setminus X_i)\setminus Z|}=0\).

**2.10 Kept forms (L55–62). ADVANCE; reads one unnamed input (G2).** (2) is the Schur complement \(p_E\Delta p_E-p_E\Delta p_IC_Ip_I\Delta p_E\), expanded. It equals YM3 (II-64-11) and the chains of SA L17550. In a live entry \((e,e')\) of a triple, the intermediate bonds lie in \(\mathrm{hull}(\alpha)\cap\mathrm{hull}(\beta)\) and \(\mathrm{hull}(\beta)\cap\mathrm{hull}(\gamma)\). So the union of the three hulls is connected and contains \(e\) and \(e'\). SA's test reads \(\Omega_{j+1}\cap Z_{j+1}\) only on the level-\((j+1)\) cells that the carrier meets, and connectedness of a cell set is intrinsic. So a collar of one cell suffices. \(\sum_{\mathfrak k}\Delta^{\rm loc}_{\mathfrak k}\) is a sum of kept chains with local coefficients, whatever the component names. YM3 also compresses a kept term to \(p_{\mathfrak k}\) (L51182). On the carrier, a stored bond lies in \(\mathfrak k\) exactly when it lies in a met cell of \(\Omega\cap Z\). So that compression is decided locally too, and its omission does not affect the split. Regrouping by polymer uses absolute convergence, and a finite torus has finitely many polymers.

**2.11 \(z\)-factors (L64). ADVANCE.** \(z(\theta,\epsilon)\) is a number (SA L18734–18742). A pivot row uses only its own double block (SA L8239–8240). The log-determinant of the straightening is a sum of local trace logarithms (SA L8343–8347). Expanding \(\prod_c[1+(z_c-1)]\) gives finite products, each reading the union of its blocks.

## 3. Section 3, step by step

Notation as in the note: \(h=\mathbf H_s\), \(C'_h=K_h-K_0\), and \(T_\omega\) a Definition D term that outputs on \(\operatorname{supp}\tilde h_{\kappa_0}\) and reads rows within \(r_0\) of \(\operatorname{supp}\theta_{\kappa_n}\).

**3.1 Definition (3) (L68–79). ADVANCE.** Put \(T(s)=(K_{\mathbf H}-K_0)H(s)\). Then \(1+T(s)^{\mathsf T}=I+H_s^{\mathsf T}C'_h{}^{\mathsf T}\), so (3) is `wf-room-2.md` (6.1) term by term. It is BGD6 (SA L10034) with the undecoupled lift \(E_0\) replaced by \(H_s\). \(E_h\) and \(R_h\) are those of `wf-room.md` (5.2) (its L194–204). There \(\|E_h-1\|\le Cr\), so the geometric series gives \(R_h\).

**3.2 Existence and (4) (L81–86). ADVANCE.** If the absolute majorants satisfy \(\||H_s^{\mathsf T}|\,|C'_h{}^{\mathsf T}|\|\le Bcr\le\tfrac12\), the Neumann series converges with majorant \(\sum_n(Bcr)^nB\|F'_U(h)\|\). So its walk expansion converges absolutely. Both bounds are available in absolute form. The bound on \(C'_h{}^{\mathsf T}\) is the second line of `nl-r9.md` (3.3); it is derived from the entrywise bounds (3.2) and Cauchy's formula. The bound \(B\) on \(H_s^{\mathsf T}\) is `nl-r9.md` (4.2). It rests on the column member of (O1), `o1-decoupled.md` Theorem B(b)–(c), whose proof bounds \(|s^\omega|\,\|T_\omega F\|\) walk by walk before summing. The remark on monomials is correct: \(s^{\omega_1}s^{\omega_2}\) differs from \(s^{\omega_1\cup\omega_2}\) at complex \(s\), and the two vanish together at Boolean \(s\).

**3.3 Component locality (L88). ADVANCE.** A live term of \((H^{\mathsf T}C'^{\mathsf T})^nH^{\mathsf T}F'\) has entries
\((T_{\omega_1}^{\mathsf T})_{c_0b_1}(C'^{\mathsf T})_{b_1c_1}(T_{\omega_2}^{\mathsf T})_{c_1b_2}\cdots F'(b_{n+1})\).
Here \(b_1\in\operatorname{supp}\tilde h_{\kappa_0(\omega_1)}\subset[\![\omega_1]\!]\). Also \(b_1\in D_{c_1}\subset\kappa_n(\omega_2)^{(4)}\subset[\![\omega_2]\!]^+\), by the margin of Lemma C. So consecutive enlarged hulls meet, and Lemma WC puts the whole chain in one component \(K\). The force stencil at \(b_{n+1}\), and the readout \(R_hK_h^{\mathsf T}\) at the rows \(c_0\), lie within a fixed distance of an output support \(\operatorname{supp}\tilde h_{\kappa_0}\subset\kappa_0^{(4)}\). Definition D's \(\kappa_0^\sharp\) contains them: its side is \(8L^2M_1\xi_{\kappa}\), against \(9M_1\xi_\kappa\) for \(\kappa^{(4)}\). So this output-end margin comes from Definition D, not from the margin stated in Lemma C. Both hold. \(R_h\) has radius zero, so the only joined run of local maps is \(R_hK_h^{\mathsf T}\), of one radius. The floor (F) of `um1-fix.md` covers it.

**3.4 Comparison with \(\mathbf 1_K\) (L90). ADVANCE.** A chain that is live at \(\mathbf 1_{\mathcal K}\) lies in \(K\), so it is live at \(\mathbf 1_K\). The converse holds because \(K\subset\mathcal K\). Its coefficients agree by (D2). Every stencil it reads lies in \([\![\omega]\!]^+\subset\operatorname{int}\bigcup K\) (Lemma C Step 1), where Lemma C gives the same \(h\). The anchor \(\lambda^0\) agrees in the same way. A bond \(b\) outside every \(\operatorname{int}\bigcup K\) gets \(j_s(b)=0\). Indeed \(j_s(b)\) reads \(\lambda_s,\lambda_s^0\) only at rows \(c\) with \(b\in D_c\). A live chain that outputs at \(c\) has \(D_c\subset[\![\omega_1]\!]^+\subset\operatorname{int}\bigcup K\).

**3.5 No datum (L92). ADVANCE.** Lemma C Step 5 gives \(h=0\) at \(\mathbf 1_K\). Then \(C'_0=0\), \(R_0=I\), \(\lambda_s=\lambda_s^0\), and \(j_s=K_0^{\mathsf T}\lambda_s^0-K_0^{\mathsf T}\lambda_s^0=0\). This meets SA L5796–5797 for the current component, and the anchor need not vanish.

**3.6 Physical locus (L92). ADVANCE.** `a3-derivative.md` (27) gives \(K_0H(1)=I\). So \(\lambda_1^0=H(1)^{\mathsf T}K_0^{\mathsf T}\lambda_*^0=(K_0H(1))^{\mathsf T}\lambda_*^0=\lambda_*^0\). SA L10449–10451 gives \(F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\lambda\). Applying \(H(1)^{\mathsf T}\) gives \((I+H^{\mathsf T}C'^{\mathsf T})\lambda=H^{\mathsf T}F'\). The bracket is invertible by 3.2, so \(\lambda_1=\lambda\). Then \(\mathbf J+j_1=R_hK_h^{\mathsf T}\lambda=R_hF'_U(h)=J(e^{i\eta h}\mathbf U)\) by (5.2). The phrase "At physical \(s=1\)" means \(s=1\) at a real critical background with \(\mathbf J=J(U)\), as `wf-room-2.md` (S4) states. The note's next sentence uses exactly that. Off this locus, (3) asserts no Euler equation, as the note says.

## 4. Two missing lines (neither breaks a consumer)

**G1. Wall-factorization needs a collar identity that Section 2 does not state.** YM3 (St2) says the block of the \(Z_0\)-structure on a component \(\gamma_i\) equals the structure built for \(Z_i:=Z_0\cap\gamma_i\) at \(s_i\). For this the always-on collars must agree: \((Z_0\cap\gamma_i)^\sharp=Z_0^\sharp\cap\gamma_i\). Otherwise a cube of \(Z_0^\sharp\cap\gamma_i\) outside \(Z_i^\sharp\) is fixed at 1 in one structure and carries a parameter in the other. *Repair.* YM3 L37955–37968 proves the identity. The proof ports to the YM4 collar of SA L14338–14347, which has the same form. The neighbour layer of one fine cube is a box of fine cubes. Its coarse parents form a box of coarse cubes, which is wall-connected. If that box lies in \(Z\), it lies in the component of its fine cube. Taking unions gives the identity.

**G2. The kept forms read an open input that the note does not name.** Step 2.10 uses \(C_I=C^{(j)}(\Lambda_{j+1})=\sum_\beta g_\beta\), with each \(g_\beta\) reading only its hull. `h-walk-fix.md` §5 item 5 records: "Statement 5 for C^(k)(Y) is not in h-walk.md, and it stays open." Section 4 of the note names the regional matrices and then "the stated absolute convergence", but not this expansion. *Repair.* List it among the open inputs of (D3). The same item gives a route: build it from the terms of \(A\) by the parametrix of SA mechanism (h) (L10550), so that its terms inherit the read sets \([\![\omega]\!]^\sharp\) by Theorem T′. YM3 proves the 3D form as its string expansion (L51150–51165, (II-64-44)).

## 5. What this moves

Moves: (LOC), through (D3) and the current clause of `loc-3.md` Lemma C.

- **(D3), exact-locality half.** It is now an implication, checked once, from: the intrinsic regional matrices and coherent logarithms on every move's cores (`regional-gauss.md` on \(\mathcal R_4\), check row 233); the tagged precision and inverse-root expansions with full hull tags (`h-walk.md` Theorem H, `inv-root.md`); the walk expansion of \(C^{(j)}(\Lambda_{j+1})\) with hull read sets (G2, open); absolute convergence of these series; and the outline's pivot chart (QC19)–(QC25), cited. Positivity of the kept forms, decay bounds and completeness at \(s=1\) are separate obligations; the note does not claim them.
- **Lemma C, current clause.** It holds for the completion (3), given Lemma C's field hypotheses, `nl-r9.md` (3.3) and (4.2) (hence `o1-decoupled.md` Theorem B), and \(Bcr\le\tfrac12\) on the response ball. So Lemma C now covers both components \((\mathbf H,\mathsf j)\) of the response, in the form Lemma M (ii)–(iii) reads.
- **If this had failed**, Theorem W would lose (D3) or the current half of (D1c). It did not fail, so the next (D3) lanes are the regional existence (row 233, then its input (10)) and the expansion in G2.
- **Not checked here:** Section 4 of the note. The open inputs of Theorem W outside this item are as rows 226 and 229 record.

## Result

**Check of our own new text** (Codex's `d3-local.md` Sections 2–3). Every step ADVANCE, checked line by line by Claude, first failing step none. As implications from the named inputs, these hold: exact locality of the Gaussian restriction (heredity and wall-factorization of \((C,\Gamma)\)), of the normaliser (exact sum rule, zero coefficients on disconnected polymers), of the kept forms and of the \(z\)-factors; and, for the explicit completion (3), the walk form (4), component locality, vanishing on a component with no datum, and exactness on the physical locus. Two missing lines break nothing: the (St2) collar identity (YM3's proof ports, G1), and the unnamed open input, the walk expansion of \(C^{(j)}(\Lambda_{j+1})\) (G2). No correction of the outline. Still open: the regional matrices on every move's cores, the expansion in G2, and absolute convergence on every move; outside this item, (D1) through [RED] and (D4).
