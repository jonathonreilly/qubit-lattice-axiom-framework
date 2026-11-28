# inn-check: queue row 180
Provenance: Codex (GPT-6; requested effort xhigh; runtime variant and effort not exposed), commit `1274a69d91421c823a67029d6051e1025690211d`; Sussman–Alpoge commit `31a47c543775`; research check, not an audit; no status granted.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline. Claude wrote `inn-213.md` Sections 6–7. SA numbers below refer to the fetched TeX. All checks are by hand.

## 1. History, pairs and transport: Sections 6a–6c

**ADVANCE, conditional on the stated background maps and premise U°.** Checked line by line by Codex, first failing step none.

- **History:** the pure gauge creation in `support-envelope.md` Sections 16 and 22 survives. Its non-top gauge site disappears under averaging. Thus the stored level-\(k_\flat\) core is vacuum, although the earlier failed test remains inside its core operation. The quiet window meets SA 17575–17585. The operation permits \(B=0\). The later reference draw does not enter this prepared read. The cell placement gives (H1)–(H3), with no inner islands.
- **Pairs:** the commuting constant-curvature field is critical. Its averages retain the affine potential. Uniqueness identifies its tower restrictions and local backgrounds, under the named chart premises. The potential bound \(|z|D_X\) gives the stated complex admission; real admission uses \(|t|\le\varepsilon_k\).
- **Lemma J:** the signed fundamental-cycle areas sum to one around \(P_E\). Some edge therefore has \(|A(e)|\ge1\). The comb errors are at most \(|z|/(2L)\) in direction 2 and \(|z|[1/2-1/(2L)+1/(2(L^2-1))]<|z|/2\) in direction 3. The node gauge adds the same endpoint difference to the coarse edge and its crossing shell row. Direction-4 rows have zero angle.
- **Last-shell test:** SA 17598–17602 explicitly joins the core to vacuum. It does not join it to the moving \(V_0(\mathbf p)\). Thus it passes at the stored flat core and does not remove the mixed holonomy. Resetting the shell after transforming only the core is not a gauge transformation.

## 2. Theorem F and the size comparison: Sections 6d–6e

**ADVANCE for F(a), F(b), and F(c)'s stated inner Wilson comparison in U°.** Checked line by line by Codex, first failing step none in the small-coupling regime used for the counterexample.

There are \(\#S\ge8(M\check R_{k_\flat})^2\) mixed plaquettes with \(|\phi|\ge|z|/2\). Their ancestor neighborhoods lie inside the inner cutoff. Equation (6.5) of `sa-2.13-2.md` gives
\[
f(t)\ge\frac{x\#S}{16\pi^2}t^2=\kappa_1t^2.
\]
Holomorphy, reality and \(f(0)=0\) give \(c_1=0\), \(c_2\ge\kappa_1\). Cauchy's remainder bound gives \(-\Re f(i\tau)\ge\kappa_1\tau^2/2\) for the stated sufficiently small \(\tau\). Fixed counting constants can be included in the curvature majorant. Subtracting any pair-independent inner read loses at most a factor two.

At the coupling ceiling, \(t=\varepsilon_k<t_0,\rho\) and \(\tau\asymp\alpha_*/D_X<\tau_1,\rho\). The other cutoffs decay only polynomially in \(\ell\). Hence the bounds are \(c(M\check R)^2p_0^2\) and \(cx\alpha_*^2\). Against \(N_0=O(\ell^{4r+1})\), the real ratio is at least \(c\ell^{2\mathfrak p_0-2r-1}\). It diverges when \(\mathfrak p_0>r+1/2\); SA 18639 chooses \(\mathfrak p_0\ge6r+1\). For \(\alpha_*\asymp g_k\ell^q\), the complex ratio is at least \(c\ell^{2q-4r-1}\to\infty\). With a smaller ADM radius, the stated \(\alpha_A\ge g_k(1+\ell)^{2r+1}\) still gives a ratio at least \(c\ell\). Strict support margins give a neighborhood at each fixed coupling; no uniform mass lower bound follows.

**CORRECT-NO-ADVANCE for the claimed outline diagnosis beyond this scope; first failing step none as a conditional claim.** SA 17591–17596 does not select U°. The result refutes that representative with the supplied inner cutoff. The complete majorant failure still assumes the stated (Pre), (Ref) and (Act) controls. No inner islands does not remove the ordinary stored forms and elimination factors of SA 17528–17558; their response must remain covered by (Act). The unwritten contour-mean variant in Section 6e(c) is not established by this check.

## 3. Definition R and Proposition D: Sections 7a–7b

**Definition R: CORRECT-NO-ADVANCE.** Checked line by line by Codex, first failing step none as a proposed definition. Fixed comb products are holomorphic and real-unitary. Averaging covariance gives (R3) exactly, even across the cutoff of \(h\). This does not establish equivalence of the full operations.

**Proposition D: ADVANCE under its curvature, transport and row-chart premises.** Checked line by line by Codex, first failing step none. A comb loop bounds at most \(|b_--z_c|_1/\eta+1\) plaquettes. Bounded complex transports, the product estimate and the row Schwarz estimate give (7.1). GEO3 then supplies \(\xi_{s'}^2\le L^{-\mathsf N/2}\). The real truncated datum remains conditional on (Adm-bar) and its collar-tower admission.

## 4. Theorem I: Section 7c

**WRONG as proved. First failing step: Step 1's integration path.** The note has \(\mathbf D=e^{iv}\tilde{\mathbf D}\), but integrates along \(\tilde{\mathbf D}e^{i\sigma v}\). Its endpoint is generally different. The local correction is \(e^{i\sigma v}\tilde{\mathbf D}\).

**A second failure remains in Step 4.** Its direction \(\hat\beta\) is complex. For \(\beta=isT\), its purported real slice is \(e^{-zT}p_{\rm r}\), non-unitary for real \(z\ne0\). Steps 1–3 therefore give no small bound on that diameter. Lemma 3.2 cannot be applied there. The correct slice is already in `pre-213.md` Lemma T: \(\beta(z)=\beta_R+z\beta_I/\|\beta_I\|\), evaluated at \(z=i\|\beta_I\|\).

The Wilson comparison can use that repair with the enlarged real regularity \(\varepsilon^\sharp\). The complete theorem still needs bounds for every read in the seminorms of (M), including currents and towers. (M) states domain room, not those displacement bounds. The claimed \(1+N_0\) form also needs \(\sum_y b_yN_y\le C N_0\). Neither Definition R nor this check supplies these premises.

## 5. Corollary P\(^R\): Section 7d

**WRONG as proved. First failing step: covariance of every term of (2.2) at the same \(B'\).** The quadratic form is frozen at the real splitting. Write \(L_pB=\operatorname{Ad}(h(p)^{-1})B\), row by row. Even with the quadratic form recomputed for R, covariance gives
\[
Q^R_{p_{\rm r}}(B)=Q^\circ_{p_{\rm r}}(L_{p_{\rm r}}B),
\]
whereas the proposed composed U° expression contains \(Q^\circ_{p_{\rm r}}(L_pB)\). Their difference was omitted. Unitarity on a real slice does not identify these forms at complex \(p\). Doubling \(\delta'\) does not bound that difference. A repair must retain it and redo the joint-chart estimate.

The conditional Wilson obstruction survives. Theorem I and Corollary P\(^R\) do not yet close the repaired (Inn) argument. Only this report was edited; no numerical proof step, audit, commit or external action was performed.

