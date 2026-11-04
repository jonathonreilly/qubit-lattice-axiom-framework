lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T14:35Z

# loc-3: (LOC) after the s210 repair (queue row 214)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker. Checkout `414c8343f`. Sussman–Alpoge outline `YM4_sketch_500.tex` and `YM3/YM3_I.tex` at `31a47c543775`, fetched by URL into a private scratch folder; "SA L" numbers refer to that file. Research text, not an audit; it grants no status. No machine computation enters any step.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and every method used here (the strip substitution, Theorem 6, the decoupled response (R9), the one interpolation of SA L17905–17918). Balaban for the strip method (CMP 119) and the large-field operation (CMP 122). Codex for `loc.md`, checked in Section 1.

## 0. What the outline does with this step

I read every outline passage that treats the locality of formed terms. Classification: **sketched**. The outline asserts (LOC) and names its method. It does not give the proof, and it lists the method's main input as open.

- SA L17453 (traces and charts) asserts that two histories with equal traces on \(W\) "produce corresponding terms with domains in \(W\)". It adds: "a term is regarded as a partial map on the fields on \(W\)". So the outline's locality is locality in the current fields (the pair), the label and the stored variables.
- SA L17541: for the strip Jacobians and the shifted quantities, "A cluster expansion as in (1d) is applied to each part."
- SA L17558–17564 (carriage): the change of background between moves gives differences that "Localisation turns ... into boundary terms". The stage difference "is localised as well".
- SA L17905–17918 gives the method: "Each walk in the response carries a parameter \(s(\Delta)\) ... Setting a parameter to zero prevents a walk from crossing that cube." Brackets in \(s\) and Schwarz's lemma in \(\lambda\) give \(f(U^{\rm old})-f(U^{\rm new})=\sum_{Y\supset X}f_Y\), \(|f_Y|\le2\mathsf ab_fe^{-(\bar\kappa-1)\mathfrak m(X,Y)}\).
- SA L5762–5800 specifies the decoupled response input (R9). "When \(s\) vanishes on separating cubes, the equations split over the remaining components, and the response on a component with no datum is zero."
- SA L17959–17966 asserts the healed-gas locality: "\(V_{\mathfrak X}(Y)\) depends on the healed family \(\mathfrak X\) only through its components inside \(Y\)".
- SA L3876–3881 states the main input as open: "The corresponding non-Abelian background and multiscale response estimates remain to be proved. This includes the decoupled response assertion numbered 1c.10".

Their three-dimensional manuscript **proves** the formation step by this method. YM3_I, Section "Local terms for the strip substitution" (L48491–48720) and Proposition II-155-54 (L49952–50036; read-out (II-155-39) at L49917, finite difference (II-71-34) at L49943), builds the localized shift \(\mathbf H(b;\mathsf S;\mathbf p)\). It is the Möbius finite difference (II-71-34) of the read-out \(\Phi_{b,\mathsf S}(s;\mathbf p)\) of the decoupled response in the localisation component, at \(s=\mathbf1_{\mathcal K\cup\mathsf P\langle b\rangle}\). It vanishes unless \(\mathsf S\) is connected, contains the reading cubes and meets the boundary cubes, and \(|\mathbf H|\le C\,\mathsf{bs}_{\mathsf S}e^{-\bar\kappa(d_t(\mathsf S)+1)/4}\) (II-155-55). Proposition II-73-32 then localises every local function of the shifted variables (transfer terms (II-73-23)), and (II-73-25), (II-73-41) localise the strip Jacobian. All locality there is locality in the background pair \(\mathbf p\).

Neither manuscript localises with a nest of localised backgrounds. Lemma N (`s210-3.md`) and Lemma N′ (`s210-fix.md`) are the repo's own device. This note checks that device (Sections 1–3), shows that it fails at seams, and then states the outline's route for YM4 as an implication from named inputs (Section 4). So the Result is of two kinds: a check of our own text, and a proof of a step the YM4 outline sketches, ported from YM3_I.

## 1. Check of `loc.md` Sections 5–7 (Codex)

Checked line by line by Claude. Verdicts per statement. First failing step: none. Two statements are made stronger below; neither changes a verdict.

| Statement | Verdict |
|---|---|
| §5: the terminal \(W_N=T\) of (N1′) is outside the domain of Lemma 10.1 when \(\Omega_0\ne T\) | **CORRECT-NO-ADVANCE** |
| §5: hand witness with \(\Omega_0\ne T\) on an allowed branch | **CORRECT-NO-ADVANCE** (conclusion) |
| §5: stopping exhaustions exist as sets after clipping | **ADVANCE** (one wording repair) |
| §5: a box expanding across a seam is not collared | **CORRECT-NO-ADVANCE**; made general by Lemma S |
| §6: identities (8), (9) and the anchor counterexample | **ADVANCE** |
| §6: (N2′) needs a distance lower bound and an anchor condition | **CORRECT-NO-ADVANCE**; the anchor part holds automatically (below) |
| §7: conditional preservation of exact locality | **ADVANCE** as stated; it carries no bounds |

**§5, terminal.** Lemma 10.1 (`a3-derivative.md`) needs (G1): \(\Omega'_0=W\) and \(\Omega'_q\subset\Omega_q\). So \(W\subset\Omega_0\). Correct. The repair needs no new argument. `a3-close.md` Lemma J(b) defines the meet as \(\Omega'_0=\Omega_0\cap\bigcap_bA_b\). A region with no parts is then \(\Omega_0\), its joined problem is the given one, and \(U^\circ_{\Omega_0}=U\). So "\(W_N\) is the torus" in (N1′) should read "\(W_N\) has no parts". This is the clipped terminal convention.

**§5, witness.** The conclusion is correct. A shorter witness: if step 1 has a failure, then \(\Omega_1^c\supset Q_1'^{\sim2}\) or \(P_1'^{\sim4}\) (SA L17317). So \(\Omega_0^c=(\Omega_1^\sim)^c\supset Q_1'^{\sim1}\) or \(P_1'^{\sim3}\), which is not empty. A failed plaquette test is an open condition on the field, so such histories have positive mass. I did not redo the crude-rule details of the \(-1\) configuration; the shorter witness makes them unnecessary.

**§5, exhaustions.** The induction is correct: \(E_0\) is fixed by the label on \(E_0^+\), and \(E_{n+1}\) adds cells of \(E_n^+\setminus E_n\) that the label on \(E_n^+\) decides. One wording repair: \(\Omega_0\) is a union of level-1 cells, not of level-\(t\) cells. Read "adjacent cells which belong to \(\Omega_0\)" as "adjacent level-\(t\) cells contained in \(\Omega_0\)", or run the induction in level-1 cells. Nothing else changes.

**§5, seams.** A connected boundary lies in one part's boundary, because distinct part boundaries are disjoint closed sets. Each part's collar lies in one layer. So a box whose boundary meets two layers is not collared. Correct. Lemma S (Section 2) shows more: every collared region contains each seam component whole, or misses its interior.

**§6.** I redid (8): with \(B^w(x,y)=w(x)B(x,y)w(y)^{-1}\), \(a_{B^w}(x)=w(y(x))a_B(x)w(x)^{-1}\), and the middle factors cancel. (9) is the triangle inequality with bi-invariance: \(d(gXh^{-1},X)\le d(g,1)+d(h,1)\). The bound \(d(D_B,D_C)\le C_Lq\) needs no inverse bound: \(D_B(b)\) is a product of at most \(4L+1\) bonds, so unitary telescoping gives \((4L+1)q\). The counterexample is correct: \(C=\mathbf1\), \(w=\mathbf1\) on one block and \(e^{ia\sigma_3}\) on the next, \(B=C^w\) is flat and block axial, and \(D_B=e^{-ia\sigma_3}\) on a crossing bond.

The anchor condition is not an extra hypothesis for strip bonds. Let \(b\in\Omega_t\setminus\Omega_t^{\sim-1}\) or \(b\in R_t\). Then \(b\) lies at least one level-\(t\) cell inside \(\Lambda_t^c\): \(\Lambda_t^c\supset(\Omega_t^c)^{\sim2}\) and \(Z^{[0]}\supset R_t'^{\sim}\) (SA L17317). Near the live region, \(\partial\Lambda_{k'}\) is at least eight cells away (\(\Omega_t^c\supset\widehat Y^{\sim8}\)). I assume the same one-cell margin where \(\partial\Lambda_{k'}\) bounds a component healed at step \(k'\); I did not check SA's labels there. Every nest member contains \(W_0\). A collar has depth \(n_c\mu\) blocks of its level, at most \(n_c\mu\xi_t\), and a level-\(t\) cell has side \(M\check R_t\xi_t\). So once \(M\check R_t>n_c\mu+4L\), the reads and anchors of \(D(b)\) are tops away from every collar of every \(W_n\). There SA L9776–9786 gives \(w=v_q[f]^{-1}\), so the anchor terms of (9) are bounded by the \(f\) bound of Theorem 6(c), if \(v_q\) is Lipschitz near \(0\) with \(v_q[0]=\mathbf1\) (gauge functional of SA 1b.2; read, not rebuilt). Only the distance lower bound is missing. Section 3 shows that it cannot hold on general histories.

**§7.** Correct. Products, derivatives, integrals over common measures, and convergent sums with equal indices and summands preserve exact equality. The argument fixes no bound and admits no support. Its premise, an admitted common formation family, is what Sections 2–3 show the nest cannot supply. Section 4 supplies such a family by walks; §7's argument then applies to it unchanged.

## 2. Lemma S: a collared region cannot cut a seam

Proved by Claude, not yet checked by the other model.

**Setting.** A separated sequence \(\Omega_0\supset\Omega_1\supset\dots\supset\Omega_k\) of closed unions of cubes in the torus. Put \(\Omega_{k+1}=\varnothing\). The layer of a point \(u\in\Omega_0\) is \(j(u)=\max\{j:u\in\Omega_j\}\), and \(\mathcal L_j=\{j(u)=j\}=\Omega_j\setminus\Omega_{j+1}\). A seam is \(\partial\Omega_q\) with \(1\le q\le k\). Separation gives \(\operatorname{dist}(\Omega_0^c,\Omega_1)>0\), so every seam lies in \(\operatorname{int}\Omega_0\).

A \(\mu\)-collared region (SA L9776–9786, with the meet of `a3-close.md` Lemma J(b)) is \(W=\Omega_0\cap\bigcap_bA_b\), with finitely many parts. Each part \(A_b\) is a union of closed grid cubes of side \(\mu\xi_{j_b}\). Its collar contains at least its outermost layer, the cubes of \(A_b\) that meet \(\overline{A_b^c}\), and the collar lies in \(\mathcal L_{j_b}\). Layers of cubes are read in the sup-norm sense (cubes that meet), as for the outline's enlargements \(\sim\).

**(F)** If \(y\in A_b\) and \(\operatorname{dist}_\infty(y,A_b^c)<\mu\xi_{j_b}\), then \(y\in\mathcal L_{j_b}\).

*Proof.* Let \(Q\) be a cube of \(A_b\) that contains \(y\). Suppose \(Q\) misses \(\overline{A_b^c}\). A grid cube \(Q'\) that meets \(Q\) and is not a cube of \(A_b\) lies in \(\overline{A_b^c}\), so it would make \(Q\) meet \(\overline{A_b^c}\). Hence every cube meeting \(Q\) is in \(A_b\). Their union is the concentric cube of side \(3\mu\xi_{j_b}\), so \(\operatorname{dist}_\infty(y,A_b^c)\ge\mu\xi_{j_b}\), a contradiction. So \(Q\) is in the outermost layer, and \(y\in Q\subset\mathcal L_{j_b}\). \(\square\)

**Lemma S.** Let \(W\) be \(\mu\)-collared, \(1\le q\le k\), and \(S\subset\partial\Omega_q\) connected. Then \(S\subset\operatorname{int}W\) or \(S\cap\operatorname{int}W=\varnothing\).

*Proof.* Suppose neither holds. \(S\cap\operatorname{int}W\) is relatively open in \(S\), not empty and not all of \(S\). Since \(S\) is connected, it is not relatively closed. So there are \(x\in S\setminus\operatorname{int}W\) and \(s_m\in S\cap\operatorname{int}W\) with \(s_m\to x\). Then \(x\in\partial W\). For a finite intersection, \(\partial W\subset\partial\Omega_0\cup\bigcup_b\partial A_b\). As \(x\in\operatorname{int}\Omega_0\), \(x\in\partial A_b\) for some \(b\). Each \(s_m\) is interior to \(W\) and lies on \(\partial\Omega_q\). So there are \(u_m\in W\cap\Omega_q\) and \(u'_m\in W\setminus\Omega_q\) with \(|u_m-s_m|,|u'_m-s_m|<1/m\). Both sequences tend to \(x\). Both lie in \(W\subset A_b\), and \(\operatorname{dist}_\infty(\cdot,A_b^c)\le|\cdot-x|_\infty\to0\) because \(x\in\overline{A_b^c}\). For large \(m\), (F) puts \(u_m\) and \(u'_m\) in the single layer \(\mathcal L_{j_b}\). But \(j(u_m)\ge q\), since \(u_m\in\Omega_q\), and \(j(u'_m)\le q-1\), since \(u'_m\in\Omega_0\setminus\Omega_q\). Contradiction. \(\square\)

**Corollary S1.** A collared region that has one point of a seam component in its interior has the whole component in its interior.

**Corollary S2 (no small localisation at a strip bond).** Let \(b\) be a strip bond of step \(t\) with \(b\in\Omega_t\setminus\Omega_t^{\sim-1}\). Its level-\(t\) cell meets a level-\(t\) cell outside \(\Omega_t\), so a point \(x_b\in\partial\Omega_t\) lies within \(2\ell_t\) of \(b\), where \(\ell_t\) is the cell side. Let \(S_b\) be the component of \(\partial\Omega_t\) that contains \(x_b\). Then every \(\mu\)-collared \(W\) with \(\operatorname{dist}_\infty(b,W^c)>2\ell_t\) has \(S_b\subset\operatorname{int}W\). So its localised background reads the label and the data along all of \(S_b\).

*Proof.* \(x_b\in\operatorname{int}W\); apply Corollary S1. \(\square\)

\(S_b\) bounds a component of \(\Omega_t^c\supset Q_t'^{\sim2}\cup P_t'^{\sim4}\cup\widehat Y^{\sim8}\) (SA L17317). Its size has no bound over histories: if \(\Omega_t^c\) has a component that is a cube of \(R\) cells, \(S_b\) is its boundary. This explains the outline's choice. SA L17518 localises the strip background to the whole component \(\Lambda_t^c\cap\Lambda_{k'}\), and YM3_I (II-13-5) to \(Z_t\cap\Lambda_k\cap\Omega_0^\diamond\). By Corollary S2, no essentially smaller collared region exists around \(b\).
