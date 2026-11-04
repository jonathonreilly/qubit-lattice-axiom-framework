lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T04:51Z

# Check of `library/regional-gauss.md` Sections 3–5 (queue row 233)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; branch `claude/ym4d-hard-route` at `4603ba50f`. One line-by-line reading by the other model. Not an audit; grants no status. Status: in progress; sections are saved as the check proceeds.

Moves: (D3) of `library/loc-3.md` and (LOC), through the regional input of `library/d3-local.md` (1).

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the regular-pair and core definitions (SA L10128–10138, (R4)–(R6) at L5664–5731), the slice extension (SA L7754), the inclusion hypotheses (SA L6138–6158), the patch operation (SA L17643–17645), and YM3_I Propositions II-44-37 and II-69-13 with (II-44-14) and (II-68-16), whose finite algebra the note ports. Tadeusz Balaban for the background-field, averaging and independent-current architecture behind these operators. The note under check is Codex's.

Sources read. SA `YM4_sketch_500.tex` and `YM3/YM3_I.tex` at `31a47c543775`, fetched once by URL into a scratch folder: SA L5660–5735, L6136–6160, L7748–7760, L10124–10140, L17636–17650; YM3_I L40185–40203, L40734–40750, L51590–51700. Repository: `a2-layers.md` §1, §4.1, §7.5–7.6, (4.0); `gates/a2-layers-gate.md` §6–7; `a2-full.md` §3–5, §10; `gates/a2-full-gate.md` §3–5; `inv-root.md` §2 (10)–(11), §5 (18)–(19); `meet-6c.md` Lemma J*; `d3-local.md` §2 (1); `gates/d3-local-check.md` 2.6–2.9; `gates/ur-gauge-check.md` D2; `c4-order.md` rows 6, 12, 16; `gates/gamma-bx-check.md` (queue row 234).

No computation was run. Every step below is a hand argument.

## 1. Section 3: intrinsic regional matrices and their gap

**3.1 The domain \(\mathcal R_4(X)\) and (3) (L69–80). ADVANCE.** The clauses are those of SA L10128–10138 as written in `a2-layers.md` §1: plaquette curvature below \(\alpha_0\eta^2\xi_j^{-2}\), \(\xi_j|A'|,\xi_j^2|\nabla_UA'|<\alpha_1\), \(|\mathbf J|<\gamma_0\xi_j^{-3}\), and a real gauge with \(\xi_j|A|,\xi_j^2|\nabla A|\le\alpha_0\) on every cube of side at most \(c_gM_1\xi_j\) inside \(\mathcal L_j\cup\mathcal L_{j+1}\). The axial clause is the hypothesis that `a2-full.md` §10, defect 5, and Theorem II add to `a2-layers.md` Theorems A and B. So (1) holds on this class with \(\gamma=c_L\) (Theorem A at \((U,0)\)), \(B=C_A\) (`a2-full.md` Lemma 5.1) and \(C_*=C_B\) (Theorem B) for the matrix of `inv-root.md` (10). For \(A^{\rm full}\) take \(C_*=C_B+C_{II}\) (Theorem II). The reference \((U,0)\) is a real regular pair, because the clauses on \(U\) hold and the zero current meets the current clause. The class is open in \((A',\mathbf J)\) at fixed real \(U\), since every inequality on \(A',\mathbf J\) is strict (SA L10132–10134).

**3.2 The meet is a separated sequence (L82–96). ADVANCE.** Take \(q\ge1\). \(\Omega_q\) is a union of aligned \(M_1\xi_q\)-cubes (`a2-layers.md` §1). \(T_q(Y)\) is such a union by (4). So \(\Omega^Y_q\) is one too. For \(q=0\), \(Y\) is a union of construction cubes; these are unions of aligned \(M_1\xi_0\)-cubes, because \(M\ge M_1\) are powers of \(L\) (`c4-order.md` rows 6 and 12). A cube \(Q\) of \(T_{q+1}(Y)\) has \(\operatorname{dist}(Q,T_q(Y)^c)>\rho\xi_q>0\), so \(Q\subset T_q(Y)\); the meet is nested. For the gap,
\[
 \operatorname{dist}\big((\Omega^Y_q)^c,\Omega^Y_{q+1}\big)
 =\min\big\{\operatorname{dist}(\Omega_q^c,\Omega^Y_{q+1}),\operatorname{dist}(T_q(Y)^c,\Omega^Y_{q+1})\big\}
 \ge\min\big\{\operatorname{dist}(\Omega_q^c,\Omega_{q+1}),\operatorname{dist}(T_q(Y)^c,T_{q+1}(Y))\big\}>\rho\xi_q .
\]
The second distance is a minimum over finitely many cubes, each \(>\rho\xi_q\). This is `meet-6c.md` Lemma J*(b) without its key-inclusion step, which (4) does not need: here the erosion runs through every level. Dimension enters nowhere.

**3.3 Regularity on the meet (L98–112). ADVANCE, with one floor made explicit (G1 below).**
- Layers. \(\Omega^Y_i\subset\Omega_i\), so the new layer index of a point or stencil is at most its old index. Each bound of 3.1 has the form \(c\,\xi^{-p}\) with \(p\ge0\), or \(\xi^{p}|\cdot|<c\) with \(p>0\). Each is weaker at the smaller scale \(\xi_i\le\xi_j\). This covers curvature (\(\xi^{-2}\)), \(A'\) and \(\nabla_UA'\) (\(\xi^{1},\xi^{2}\)), and the current (\(\xi^{-3}\)).
- Gauge cubes. Let \(Q\subset X\) be a tested cube in new layers \(i,i+1\), of side at most \(c_gM_1\xi_i\). Then \(Q\subset\Omega^Y_i\subset\Omega_i\). Let \(j\ge i\) be largest with \(Q\subset\Omega_j\) (fine sequence, \(j\le k\)). If \(j\le k-2\), pick \(x\in Q\setminus\Omega_{j+1}\). Every \(z\in\Omega_{j+2}\) has \(|x-z|_\infty>\rho\xi_{j+1}\). Every \(y\in Q\) has \(|x-y|_\infty\le c_gM_1\xi_i\). So \(Q\cap\Omega_{j+2}=\emptyset\) if \(c_gM_1\xi_i\le\rho\xi_{j+1}\), by the strict gap. Since \(\xi_{j+1}\ge L\xi_i\) and \(\rho=R_1M_1\), the condition \(c_g\le R_1L\) suffices. If \(j\in\{k-1,k\}\), \(Q\) lies in \(\mathcal L_{k-1}\cup\mathcal L_k\) of the cut sequence. In all cases \(Q\) lies in old layers \(j,j+1\), has side at most \(c_gM_1\xi_j\), and so carries the old gauge. Its bounds \(\xi_j|A|,\xi_j^2|\nabla A|\le\alpha_0\) imply the same with \(\xi_i\).
- Top. Every next block of \(\Omega^Y_{k+1}\) is a next block of \(\Omega_{k+1}\), so it is axial. The level-\(k\) averages on bonds touching it read the two level-\(k\) blocks at the ends of each bond. These lie within \(2\xi_k=2<\rho\) of \(\Omega^Y_{k+1}\), hence in \(\Omega^Y_k\subset\Omega^Y_q\) for every \(q\le k\), by the gap at \(q=k\). So \(V^Y=V\) there.
- No criticality is used. `a2-layers.md` Theorems A and B hold on or off shell. So the meet is admitted for (1) with the same \(M_1,\rho,\alpha_0,\alpha_1,\gamma_0\).
- The Dirichlet boundary \(\partial\Omega^Y_0\) lies in \(\mathcal L^Y_0\) by the gap at \(q=0\). This is the boundary placement that `a2-layers.md` §4.1 handles (bare rows; boundary plaquettes never used). So Theorem A applies to \(\Omega^Y_0\ne\mathbb T\). It is a new sequence, not a conditioning set; the gate's restriction (`a2-layers-gate.md` §6, "conditioning means compression") is respected.

**3.4 Erosion depth (L114–119). ADVANCE.** \(\sum_{q=0}^k\xi_q<L/(L-1)\) and \(\sum_{q=0}^k\xi_{q+1}<L^2/(L-1)\), so \(e_{k+1}<L(\rho+LM_1)/(L-1)\). For the induction, let \(\operatorname{dist}(x,Y^c)>e_{q+1}\) and let \(Q\ni x\) be the aligned \(M_1\xi_{q+1}\)-cube. Each \(z\in Q\) has \(\operatorname{dist}(z,Y^c)>e_q+\rho\xi_q\). Each \(w\notin T_q(Y)\) has \(\operatorname{dist}(w,Y^c)\le e_q\) by the hypothesis. The distance function is 1-Lipschitz, so \(|z-w|_\infty>\rho\xi_q\), and \(Q\subset T_{q+1}(Y)\). This is `meet-6c.md` Lemma J*(a).

**3.5 Deep mask (L120–123). ADVANCE.** Let \(b\in I_Y\) and \(|z-b|_\infty\le C_{\rm st}\). Points of \(Y^c\) are at distance \(>r_N\) from \(b\), so \(\operatorname{dist}(z,Y^c)>r_N-C_{\rm st}>e_{k+1}\ge e_q\). By 3.4, \(z\in T_q(Y)\) for every \(q\le k+1\). So the meet equals the move's sequence on the \(C_{\rm st}\)-box of \(b\). Hence \(b\) touches \(\Omega^Y_{k+1}\), and its pivot status and stencils are unchanged. The order of choice is admissible: \(r_N\) depends on \(L,\rho,M_1\) only, uniformly in \(k\), and \(M\) comes after \(\rho\) (`c4-order.md` row 12). The condition \(4(r_N+1)<LM\) is not used in Sections 3–4.

**3.6 Gap, inverse and the full torus, (5)–(6) (L125–142). ADVANCE.** (1) on the meet gives \(\gamma\le\mathsf A[\Omega^Y,(U,0)]\le B\) and the perturbation bound on all free coordinates of the meet. Compression to \(I_Y\) is zero extension of vectors: \(\langle v,A_Yv\rangle=\langle\iota v,\mathsf A\,\iota v\rangle\) and \(\|\chi\Delta\chi^{\mathsf T}\|\le\|\Delta\|\). With (3), the Hermitian part of \(A_Y(P)\) is at least \(\gamma-\gamma/4\). Cauchy–Schwarz gives injectivity, so \(\|C_Y\|\le4/(3\gamma)\) in finite dimension. Theorems A and B include existence of every defining inverse. For \(Y=\mathbb T\), \(T_q(Y)^c=\emptyset\) and \(I_Y=I\), so (5) is the move's block. It is the move's actual Gaussian precision at the physical step pair (`a2-full.md` Theorem I, with the ambient/free reading of `a2-full-gate.md` §3, D1). Elsewhere it is the specified matrix of `inv-root.md` (10); Section 5 of the note records this as part of (10).

**3.7 Relation to YM3_I II-69-13 (L144–147). ADVANCE.** II-69-13 (L51590–51603) asserts complex symmetry, the real two-sided bound, the \(\gamma/4\) perturbation bound and \(\|1-c^{-1}A\|\le q\). Its proof localises by mesh cutoffs (L51617–51660). The note replaces that step by the layered theorems, applied to the meet itself. That is a correct substitution on \(\mathcal R_4\).

## 2. Section 4: existence and coherence of the logarithms

**4.1 The series (7) (L151–172). ADVANCE.** \(A_Y(U,0)\) is real symmetric with spectrum in \([\gamma,B]\). So \(I-c^{-1}A_Y(U,0)\) has spectrum in \([-(B-\gamma)/(B+\gamma),(B-\gamma)/(B+\gamma)]\). Adding \((\gamma/4)/c=\gamma/(2(B+\gamma))\) gives \(\|T_Y\|\le(B-\gamma/2)/(B+\gamma)=q<1\). Then \(\|\sum_nT_Y^n/n\|\le-\log(1-q)\), which gives the bound in (7). Convergence is uniform on the slice, and \(A_Y\) is holomorphic there (finite compositions and inverses of holomorphic matrices). So \(L_Y\) is holomorphic. For \(e^{L_Y}=A_Y\): the series \(\sum_n|t|^n/n\) converges for \(|t|\le q\) and \(\exp\) is entire, so the composed series in the commuting powers of \(T_Y\) may be rearranged; the scalar identity \(\exp(-\sum_nt^n/n)=1-t\) then gives \(e^{L_Y}=c(I-T_Y)=A_Y\). On a positive real matrix the series is \(\log\lambda\) on each eigenvalue. Per bond, \(\operatorname{tr}L_Y(b,b)\) is YM3_I (II-44-14) and (II-68-16), with the same factor 3 for \(\dim\mathfrak{su}(2)\).

**4.2 Coherence (L174–180). ADVANCE.** \(L_Y\) is a fixed function of \(A_Y\), with \(c\) uniform. \(A_Y\) depends only on the pair, the meet and the mask: Theorem B's operators are continuations in \(\mathbf U\) and \(\mathbf J\). So two splittings of one pair, both in \(\mathcal R_4\), give one matrix and one series. Under \(A'=S^{-1}AS\) the partial sums conjugate, so the limits conjugate; no norm bound on \(S\) is needed for this. The note claims no more.

**4.3 Components (L182–187). ADVANCE.** Row 230 checked this argument (`d3-local-check.md` 2.8). Restated briefly: a box in \(Y\) is nearest-neighbour connected. A nearest-neighbour step out of a wall-component of \(Y\) lands in \(Y^c\), because a lattice neighbour in another cube of \(Y\) means a shared wall. So erosion tests, the meet, the deep mask and every contained stencil split, and existing inverses keep the block form.

**4.4 Determinant and Gaussian integral, (8) (L189–204). ADVANCE, with one unstated line (G2 below).** Schur triangularisation gives \(\det e^{L}=e^{\operatorname{Tr}L}\). For real \(v\), \(\operatorname{Re}(v^{\mathsf T}Av)=v^{\mathsf T}\tfrac12(A+A^*)v\ge\tfrac34\gamma|v|^2\), which gives a Gaussian majorant. Take the ball \(\|A-A_0\|<\gamma/2\) of complex symmetric matrices around \(A_0=A_Y(U,0)\). On it the Hermitian part is \(\ge\gamma/2\), and \(\|I-c^{-1}A\|\le B/(B+\gamma)<1\). So both sides of (8) are holomorphic in the independent entries. They agree on the real points, which are positive definite. A polydisc about \(A_0\), with the identity theorem applied in one variable at a time, gives equality near \(A_0\). The ball is convex, so equality holds on it. \(A_Y(P)\) is in the ball by (6).

**4.5 Normaliser (L206–210). ADVANCE.** With \(P\in\mathcal R_4(\mathcal P)\), every \(F(Y;P)\), \(Y\subset X\subset\mathcal P\), exists. The sum rule and the zero coefficients on disconnected \(X\) are `d3-local-check.md` 2.6 and 2.9. The note claims no decay bound.

**4.6 Collared parameters, (9) (L212–225). ADVANCE as an implication from (2) for the regional operator's own tagged series.** A varied carrier joins integration bonds and meets a varied cube at distance at least \(w\). Its hull lies within \(R_h\) of its tree, so \(\ell_\omega\ge w-R_h\). A traversal of length \(2\ell\), cut into pieces of length at most \(M/4\), with \(M\ge8R_h\), gives pieces of diameter \(<M\). Each meets at most \(2^4\) cubes, which is `inv-root.md` (18). With \(|s_\Delta|\le e^{\bar\kappa}\), \(|s^\omega-1|\le2e^{16\bar\kappa+C_g\bar\kappa\ell/M}\). With \(C_g\bar\kappa/M\le\eta/2\), each row or column sum is at most \(2e^{16\bar\kappa}e^{-\eta(w-R_h)/2}W\). The Schur test gives (9). It is the one-factor case of `inv-root.md` (19). The split \(\gamma/8+\gamma/8\) restores (6), so (7)–(8) follow. Symmetry of \(A(s)\) needs the transpose-closed series, as the note says. Holomorphy in \(s\) holds on the declared discs (`inv-root.md` §5). The constants are in admissible order: \(M\) and \(w\) come after \(\bar\kappa\) and \(\eta\) (`c4-order.md` rows 9 and 12). (2) for the meet's operator is a premise; \(\mathcal R_4\) retains it explicitly (L79, L65).

## 3. Section 5: first input that does not port

**5.1 Full core against \(\mathcal R_4\) (L229–237). CORRECT-NO-ADVANCE.** SA (R4)–(R6) (L5671–5729) ask for small curvature, small \(A',\nabla_UA',\mathbf J\), a real gauge with \(|A|,|\nabla A|<C_{\rm pot}Ma_0\) on every box of side at most \(C_{\rm box}LM\), and the tower bounds (R6). No clause asks that the given representative be axial. The non-implication is not only asserted: the pair \((\mathbf 1^g,0)\) of 5.2 is in the core, and its top datum at \(k=0\) has \(W(y,x)=e^{-i\varepsilon T}\ne\mathbf 1\), so it is not in \(\mathcal R_4\). The core's gauge radius also carries the factor \(M\); the note records this at L268. (10) is a correct statement of the missing assertion.

**5.2 The witness (L239–261). CORRECT-NO-ADVANCE; it is `ur-gauge-check.md` D2, re-derived.** YM3_I L40199–40201 indeed transfers its flat comparison by "unitary gauge covariance". With the action \(U(b)\mapsto u(b_-)U(b)u(b_+)^{-1}\) (`a2-full.md` §3), a path from \(y\) to \(x\) in \(\mathbf 1^g\) has product \(g(y)g(x)^{-1}=e^{-i\varepsilon T}\), so every contour mean equals it. The change \(g(x)\to e^{i(\varepsilon-t)T}\) keeps \(g=\mathbf 1\) at every block centre. Each coarse contour product is then \(\mathbf 1\), so the datum stays fixed and the change is a fibre direction. Then \(1-\tfrac12\operatorname{tr}W(y,x)=1-\cos(t-\varepsilon)\), and the relative summand is \(1-\cos t\). Their second derivatives at \(t=0\) are \(\cos\varepsilon\) and \(1\). All other summands and the Wilson action are constant along this gauge orbit. So no covariance identity carries the axial operator to the absolute one at \(\mathbf 1^g\). The note says correctly that the gap \(1-\cos\varepsilon\le\varepsilon^2/2\) does not refute positivity.

**5.3 Slice extension, radii and inclusions (L263–270). CORRECT-NO-ADVANCE.** SA L7754 reads as quoted: \(F^\natural(\mathfrak z)=F(\mathsf c[\mathfrak z]\cdot\mathfrak z)\), with locality, bounds and holomorphy asserted and not proved. `a2-full.md` §10, defect 5, records that \(G^{(2)}_V\) and \(\hat J_{\rm GF}\) are not covariant. `c4-order.md` row 16 keeps \(CM\alpha_0<\alpha_1\) after \(M\) (row 12). SA L6153–6158 calls restriction and stage substitution "analytic inclusion hypotheses".

**5.4 Patch precision (L272–275). CORRECT-NO-ADVANCE.** SA L17645 carries the profile in the gauge form \(\|\phi^{1/2}D\mathsf HB\|^2\) and in the action \(A(x''_k\phi_{\rm c},\cdot)\). `a2-full.md` §10, open item 5, excludes this Gaussian, "degenerate where \(\phi=0\)".

**Changed input since the note.** Row 234 (`gates/gamma-bx-check.md` §4, Codex) reads the meet prescription of Section 3 with \(A^{\rm rel}\). Its Lemma 2 removes the axial-reference clause for regular moves, so (10) advances there. Still open from (10): admission of lifted and stage cores, identification with each move's consumed Gaussian, and the patch precision. This check of Sections 3–4 is the check that row 234 assumes for the meet prescription and the logarithm.

## 4. Missing lines (neither breaks a consumer)

**G1. The separation floor at L105.** Make it explicit: \(c_g\le R_1L\), where \(c_gM_1\xi_j\) is the gauge-cube side of SA L10137 (`a2-layers.md` §1). This is admissible: \(c_g\) is fixed before \(M_1\) by (4.0), and \(R_1\) comes after \(M_1\) (`c4-order.md` row 6). The actual move gaps are at least \(\min(LM,2cM\check R_j)\xi_j\) (`meet-6c.md` Lemma G (G-c)), and \(M\) is chosen after \(\rho\), so the raised floor costs nothing. Row 6's \(R_1\ge8L^3\) already gives it when \(c_g\le8L^4\).

**G2. Complex symmetry at L199.** The holomorphic continuation is on complex **symmetric** matrices, so it needs \(A_Y(P)^{\mathsf T}=A_Y(P)\) for the bilinear transpose. Without it, \(\int e^{-v^{\mathsf T}Av/2}\) sees only the symmetric part, and (8) can fail. It holds: every summand of `inv-root.md` (10) is bilinear-symmetric. \(G^{(2)}_V\) is a Hessian; \(R^{\mathsf T}=R\) (`a2-full.md` Lemma 3.1); the six-term form of SA L10176–10185 is symmetric in its two arguments (`a2-full-gate.md` §3); \(\Delta^{(2)}[\cdot]\) and \(E^{(2)}[\cdot]\) are second jets; compression keeps symmetry. YM3_I II-69-13 states this clause (L51592). Add one sentence to Section 3.

No numeric job was run or needed; memory pressure was not tested for that reason.

## Verdict

| Step | Verdict | First failing line |
|---|---|---|
| 3.1 \(\mathcal R_4(X)\), (3), constants of (1) | ADVANCE | none |
| 3.2 meet is separated, cubes, nesting, gap \(\rho\xi_q\) | ADVANCE | none |
| 3.3 regular pair, gauges, top axiality on the meet | ADVANCE | none; floor G1 made explicit |
| 3.4 \(e_{k+1}\) bound and erosion induction | ADVANCE | none |
| 3.5 deep mask \(I_Y\), order \(r_N\to M\) | ADVANCE | none |
| 3.6 (5)–(6), \(C_Y\), full-torus block | ADVANCE | none |
| 3.7 port of YM3_I II-69-13 | ADVANCE | none |
| 4.1 series (7), holomorphy, \(e^{L_Y}=A_Y\) | ADVANCE | none |
| 4.2 coherence, similarity, splittings | ADVANCE | none |
| 4.3 split over wall-components | ADVANCE (also row 230, 2.8) | none |
| 4.4 (8), determinant root, continuation | ADVANCE | none; G2 to be stated |
| 4.5 normaliser existence and exact locality on \(\mathcal R_4\) | ADVANCE | none |
| 4.6 collared parameters (9) | ADVANCE, implication from (2) on the meet | none |
| 5.1 full core is not in \(\mathcal R_4\); statement (10) | CORRECT-NO-ADVANCE | none |
| 5.2 witness \(\cos\varepsilon\) against \(1\) | CORRECT-NO-ADVANCE | none |
| 5.3 SA L7754, the \(CM\) radius, SA L6138–6158 | CORRECT-NO-ADVANCE | none |
| 5.4 patch precision SA L17643–17645 | CORRECT-NO-ADVANCE | none |

## What this moves

- **(D3), regional existence on \(\mathcal R_4\).** `regional-gauss.md` Sections 3–4 are now checked line by line by Claude, first failing step none. That holds as an implication from the named inputs: `a2-layers.md` Theorems A and B, `a2-full.md` Lemma 5.1 and Theorem II, `inv-root.md` (11) on each meet, and h-walk's inverse and coefficient premises. Together with row 230, the normaliser of `d3-local.md` (1) exists and is exactly local on \(\mathcal R_4\).
- **(10).** Section 5 is a correct diagnosis. With row 234, (10) holds for regular moves with \(A^{\rm rel}\). The next (D3) lanes are the three open parts of (10), the polymer decay bound of the normaliser, and the walk expansion of \(C^{(j)}(\Lambda_{j+1})\) (row 230, G2).
- **If this check had failed,** `d3-local.md` (1) would have had no regional matrices, and Theorem W would have lost (D3). It did not fail.

## Result

**Check of our own new text** (Codex's `regional-gauss.md`, Sections 3–5). Checked line by line by Claude, first failing step none. Sections 3–4 ADVANCE: intrinsic regional matrices on the tower meet, the uniform gap (6), coherent logarithms (7), and the determinant and Gaussian identities (8) on \(\mathcal R_4\), with the collared form (9) as an implication. Two lines should be added: the floor \(c_g\le R_1L\) (G1) and the complex symmetry of \(A_Y\) (G2). Neither changes a conclusion. Section 5 is CORRECT-NO-ADVANCE: (10) is the right missing assertion; the \(\mathbf 1^g\) witness repeats `ur-gauge-check.md` D2 and is right; the SA quotations match the pinned text. No correction of the outline is made. Open: the parts of (10) beyond row 234 (lifted and stage cores, identification with each move's Gaussian, the patch precision), summable polymer bounds, and (D1).
