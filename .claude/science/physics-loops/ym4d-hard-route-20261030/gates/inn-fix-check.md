# inn-fix-check: queue row 192
Provenance: Codex (GPT-6; requested effort xhigh; runtime variant and effort not exposed), commit `62a78dba89355b6aae6d190d1289459112e5aff9`; Sussman–Alpoge commit `31a47c543775`; research check, not an audit; no status granted.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline. Claude wrote `library/inn-fix.md`. SA line numbers refer to the outline fetched once into `/tmp/sa_ym4.tex`. This checks rank 6's (Inn) by hand.

## 1. Section 2: the R datum and weighted count

**Lemma H: ADVANCE under (I) and the stated ceilings.** Checked line by line by Codex, first failing step none for the operation's rows. The comb products telescope. Real \(h_0\) preserves norms, including at rows crossing \(\partial N_{\rm c}\). Proposition D supplies \(\delta^\sharp\) on the near-core rows. The real tests give the stated enlarged regularity.

For later uses, the increment over \(\mathbf D(0)\) also has the bound \(C_\Delta\|\beta\|\) on near-core rows. Apply covariance at both endpoints: the two gauge increments cost \(2C_h\|\beta\|\), and S' supplies the reference increment. Small-product logarithms fit inside \(C_\Delta=\max(C_\natural,3C_h+6C_S)\). This supplements H(c)'s displayed \(8\delta^\sharp\) bound.

**Lemma C: ADVANCE.** Checked line by line by Codex, first failing step none. The core sum is bounded by \(1+L^4\sum_{i\ge1}L^{-12(i-1)}\le2L^4\). The margin count fits the stated constant. Thus finer core tops are paid for by decay.

## 2. Section 3: Theorem I^R(a)

**ADVANCE as an implication from (I).** Checked line by line by Codex, first failing step none. The path \(e^{i\sigma v}\tilde{\mathbf D}\) ends at \(\mathbf D\). T4 and localisation give the displayed real per-top bound. Lemma T uses \(\beta_R+z\beta_I/\|\beta_I\|\), which is Hermitian for real \(z\). Its disc stays inside \(\mathbb D\). The square root leaves decay rates \(\theta/4\) and \(\theta/2\); Lemma C sums both. The stated \(C'_{IW}g_k^{1/4}\) follows.

## 3. Section 4: Theorem I^R(b)

**Sections 4.1–4.2: ADVANCE under (M^R), (OD), and (IND).** Checked line by line by Codex, first failing step none. The old margin exceeds the running radius at small coupling. The new ball satisfies \(\max(\|h\|_1,\|h\|_2)+\|h\|_3<c_*\alpha_{0,m}\). Thus (OD) covers every tower clause. Keeping \(\bar U\) fixed cancels the Gaussian exactly and gives \(|f_y|\le2C_VN_0(\omega'_y)\).

**Lemmas K and D^sharp: ADVANCE under their stated inputs.** Checked line by line by Codex, first failing step none. K's gauge products and current subtraction are exact. The current estimate follows by integrating Section 7.3's weighted response along the same chart path. The localisation path has the same estimate. Only real gauges enter K's norm comparison; the unbounded complex gauge is removed through (GO).

**Theorem I^R(b) and the count: ADVANCE, conditional.** Checked line by line by Codex, first failing step none. In all three seminorms, the unit change costs at most \(L^3L^{-(d-1)_+}\). The radius costs at most \(2(1+\bar Bd)^{1/2}/(C_0g_k)\). Their product gives \(a_y\le\bar a\). Equation (4.1) then gives \((8/3)C_V\bar aN_0(\omega'_y)\). SA 18091 gives exactly
\[
\sum_y b_yN_y=2C_V\sum_yN_0(\omega'_y)\le2C_VN_0(\omega).
\]

## 4. Section 5: Corollary P^R

**ADVANCE under its named premises.** Checked line by line by Codex, first failing step none. The endpoint-product estimate in Section 1 also applies to reference rows crossing the cutoff. It holds on the fixed ball \(\rho_Q^R\): there \(C_h\|\beta\|\le r_{\rm B}/48\). Thus the joint chart has the required room, independently of \(\beta_A\).

At the real centre, covariance gives \(Q^R(B)=Q^\circ(L_0B)\). The Hessian identity, cubic estimate, and real-slice linear estimate therefore carry over. The alternative expression keeps
\[
D_Q=Q^\circ(L_0B)-Q^\circ(L_\beta B).
\]
Polarization gives \(|D_Q|\le72q_QC_h\beta_A(A_1p_1)^2\). This is \(g_k\) times a fixed polynomial in \(\ell\), as claimed.

## 5. Bound (7.2^R) and the induction constant

**(7.2^R): ADVANCE, conditional; first failing step none.** Checked line by line by Codex. Adding (a) and (b) gives the displayed bound. The ceiling \((64/3)C'_ag_k^{1/4}\le1\) makes its recursive coefficient at most \(1/8\), independently of \(C_V\).

**“The induction constant is not consumed”: CORRECT-NO-ADVANCE beyond this conditional budget.** First failing step none with Section 6's explicit proviso. The other terms must still fit the remaining budget, including the additive Wilson term. This does not close the induction or (Act).

## 6. Does Definition R give the same integral?

**CORRECT-NO-ADVANCE: equality remains unproved, as the note states.** First failing step none in that disclaimer. SA 17591–17596 leaves the representative unspecified; this permits a proposed choice, but supplies no identity between complete operations.

The first unsupported step in a covariance proof would be preservation of the last-shell support. Pulling R back by \(h^{-1}\) sends
\[
(\mathbf1,\zeta)\longmapsto((\mathbf1)^{h^{-1}},\zeta^{h^{-1}}),
\]
whereas the original test joins the transformed core to \(\mathbf1\) (SA 17598–17602). Those data need not be gauge equivalent. Shell fluctuations, all stored factors, and the complex contour must also be matched. Sections 2–5 establish estimates for the R construction; they establish neither equality nor inequality of the full integrals.
