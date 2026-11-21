# Gate of `library/hm.md` (H-M, pass 3)

First failing step: none.

Provenance: Claude (Opus 5.5), fresh session, 2026-11-05. Clone HEAD `3f1418b1f0bc`; `hm.md` last changed in `565c00f13`. SA = pinned `ym4.tex`; YM3 = pinned `YM3_I.tex`. Research text, not an audit. It grants no status. No computation was used as a proof step. Only this file was written.

Scope: every numbered statement of `hm.md` (Lemmas 1–4, 6; Theorems 5, 7, 8; Propositions 9, 10; Corollary 13.1), the imports R, W, AV, FG/UM, G-ID and F, and the match with frozen `in1.md` H-M.

## Findings

All findings are repairable. None is fatal. None changes a statement.

1. **Line 7, provenance.** The links to `../checks/hm-pass2/source-checks.md` and `source-identities.json` point to files that do not exist in this checkout. I could not check the distiller's source record. I read every cited SA line directly instead (see "Source readings"). Repair: add the two files, or remove the links.

2. **Line 97, Lemma 2 proof, typo.** "a term bounded by \(4|\partial U-I|\alpha/\xi\)" is missing a factor \(\epsilon_{\rm lat}\). Each link potential has size \(\epsilon_{\rm lat}\alpha/\xi\). Two of the four are transported along paths that differ by the holonomy, so the term is at most \(4\epsilon_{\rm lat}|\partial U-I|\alpha/\xi\). After normalizing by \(\epsilon_{\rm lat}^{-2}\xi^2\) this gives \(4r_0(\epsilon_{\rm lat}/\xi)\alpha\), which is the term the display on line 100 uses. The display and the conclusion \(\le4\alpha\) are correct. Repair: insert \(\epsilon_{\rm lat}\).

3. **Lines 196 and 249, metric of tree lengths.** A grouped \(P_t\) or \(Q_t\) entry has length \(d(x,y)\), the \(\ell^\infty\) distance. A nearest-neighbour lattice tree from \(x\) to \(y\) can be up to \(4d(x,y)\) long. So the "tree" for such an entry has to be read in the \(\ell^\infty\) (king-move) metric. Lemma 6 works in that reading: its proof uses only "diameter ≤ length", and the crossing bound uses only "length ≥ \(\ell^\infty\) distance reached". Precision labels have physical lengths, which are no shorter. Repair: say once that tree lengths are \(\ell^\infty\) path lengths. No constant changes.

4. **Line 44, citation range.** "SA 14276–14816" runs five lines into the next SA module. The UM module ends at line 14811, which is the range frozen IN1 cites. Repair: cite 14276–14811.

5. **Line 296, wording.** "The exponent 32 is necessary because Γ has two tag sets." The 32 is what this count needs: two independent tags, each costing at most \(16\bar\kappa+\theta t/2\). The proof does not show that it is necessary. Repair: "required by this count".

## Statement-by-statement check

**Lemma 1 (lines 53–83).** The proof checks against h-walk Lemma C (C1)–(C4), Lemma L, Theorems W, T and H, and `h-walk-gate` §§3, 5–8.
- The cut-down admission matches (C4): layer index not larger; gauge cubes of side \(c_gM'\xi_i\le c_gM_1\xi_{i_0}\); top layer unchanged. The (C5) failure only concerns region traces, so with fixed regions it is not used (gate §6).
- "At most 25 primitive inverse factors" matches the gate count, whose successive maxima are 5, 10, 13, 18 and 23.
- The graph-norm commutator identity and its bound are copied correctly from gate §5. The last graph component comes from \(A_sG'f=f\), and duality gives the transpose.
- The transposed-multiplier weight \(\xi_c^3\xi_c^{-4}\xi_c=1\) and the bound \(C\gamma_0\) match gate §7. The zero-length multiplier reads match gate §8.
- I recomputed the tree exponent identity: \(q=n+\sum m_i+v\) and \(p=n-v+\sum m_i\) give \(3p-q=2(n-v)+2\sum(m_i-1)\).
- Summation: count \(C_h^{m+1}\) times \(C_h(C_hM_1^{-1/3})^m\) gives \(C_h^2(C_h^2M_1^{-1/3})^m\le C_h^22^{-m}\). Take \(\mu_W\le\delta_h/2\) and \(D\ge t_\omega\ge d(x,y)\). Then \(e^{-\delta_hD/2}\) pays the sum over \(y\) by (1), and the bounded root count \(N_r\) is absorbed. This proves (4).
- The condition \(C_h^2M_1^{-1/3}\le1/2\) is exactly pr-lay's floor \(M_1\ge8C_h^6\).
- Symmetrizing with the same hull keeps the total and the two-sided majorant.
- Conclusion: the statement holds, conditional on W as repaired.

**Lemma 2 (lines 85–102).**
- (6): \(l\le L\) gives \(r_Y\le\max(L^2a_1,L^3j_0)\). Gauge cubes of side \(c_gM_1\xi\) with \(\xi\le L\) fit inside R4 boxes because \(c_gM_1\le C_{\rm box}M\).
- Curvature: \(2\alpha+4r_0(\epsilon/\xi)\alpha+16\alpha^2\le4\alpha\) holds for \(\alpha\le1/16\) and \(r_0\le1/4\). On the disc, \(\alpha<h/8\), so the complex normalized curvature is \(<h/2+h/2\).
- Schwarz at radius \(h/(8L^2r)>1\) gives \(16L^2m_\omega r/h\), so the displacement is at most \(H_1r\).
- Correct. Finding 2 is a typo only.

**Lemma 3 (lines 106–117).**
- The clamped and cut-off extension gives \(|A^{\rm ext}|\le\alpha\) and \(|\nabla A^{\rm ext}|\le2\alpha\). The cutoff falls over one level-\(k\) unit, which is \(L^k\) bare steps, so its normalized slope is at most 1.
- The defect is at most \(4\epsilon^2\alpha+16\epsilon^2\alpha^2\le5\epsilon^2\alpha\). With scales up to \(L\), the real bound is \(\le8L^2\alpha\).
- I checked covariance (8) against QC1–QC3:
  - Path transports are conjugated by their endpoint gauges.
  - QC1 is conjugated at its initial endpoint, and uniqueness of the regular branch is preserved under unitary conjugation.
  - The QC3 loop is based at \(y\).
  - The straight transport \(U[c]\) gives the second endpoint.
- The gauge \(v=c_b\) on unprotected blocks makes them axial. Protected blocks keep \(v=I\) and read only \(B^+\), where \(U''=U\). Bonds in \(F\) are unchanged.
- Correct.

**Lemma 4 (lines 125–152).**
- IMS identity: \(\sum_c[h_c,[h_c,A]]=2A-2\sum_ch_cAh_c\). Its entries are \((h_c(x)-h_c(y))^2A(x,y)\).
- Constants: at most 16 tents per site, so at most 32 per pair. The factor 400 holds; a direct estimate gives 272, because each one-dimensional sum of squares is \((2/\ell)\)-Lipschitz with values in \([1/2,1]\). With \(\sup t^2e^{-\mu t}=4/(e^2\mu^2)\) this gives \(c_{\rm IMS}=16\cdot400^2\cdot4/e^2\).
- Box geometry:
  - The rounded box has side at most \(2\ell_{\rm IMS}+2b_{\rm tail}+2r_{\rm av}+8L\le2\ell_{\rm IMS}+2b_{\rm gap}\le C_{\rm box}LM\).
  - The box lies in \(N_{b_{\rm gap}}(S)\subset Y\).
  - Every block that meets \(N_{b_{\rm tail}}(Q_c)\) is protected, so \(F\supset N_{b_{\rm tail}}(Q_c)\).
  - With \(\alpha<h/(16L^2)\), Lemma 3 gives real bound \(<h/2\le a_R/2\).
- Comparison step:
  - Labels inside \(N_{b_{\rm tail}}(Q_c)\) are the same for \(U\) and for \(\widetilde U\). This holds for bare reads and for \(V=\mathcal M^k\) reads, since \(V\) agrees between protected sites.
  - Other labels have \(t_\omega\ge b_{\rm tail}-R_h\), so the two Schur tails cost at most \(c_L/8\).
- Gaps: \(c_L-c_L/8\) gives \(7c_L/8\). The IMS loss gives \(3c_L/4\). Lemma 2 gives \(5c_L/8\). Removing long labels gives \(c_L/2\). The norm is at most \(W\).
- Correct. The proof uses Rep openly and needs no covariance of the soft-gauge Hessian.

**Theorem 5 (lines 183–226).**
- Contraction: \(\Lambda=2b^2/a\) gives \(1-2a/\Lambda+b^2/\Lambda^2=1-3a^2/(4b^2)\), and \(q_*<1\) because \(W\ge c_L\).
- Paths of at most \(n\) short steps stay in \(B(x,nr_c)\). That ball has a \(b_{\rm gap}\) margin inside the \(R_*\) hull, so Lemma 4 applies to the compression.
- (17):
  - The bound uses \(e^{\theta r_c}\le q_*^{-1/2}\) and \((2jr_c+1)^4\le16r_c^4(j+1)^4\).
  - The bound \(|E|_\theta\le We^{-\mu_Wr_c/2}\) uses \(\theta\le\mu_W/2\).
  - These give \(|K_t|_\theta\le1/4+1/4\).
- The identity \((A+t)P_t=I-Q_t+EP_t\) checks. The integral \(\int_0^\infty t^{-1/2}(\Lambda+t)^{-1}dt=\pi/\sqrt\Lambda\) gives \(U_{\rm root}\).
- (14): Schwarz on the radius \(r_{\rm loc}/r\ge2\) gives the stated bound. The disc stays in \(\mathcal W(Y)\), not necessarily in \(\mathcal K\); that is why \(\mathcal W\) is defined.
- The whole-torus root uses the right half-plane spectrum and holomorphic calculus.
- Correct. Finding 3 is about the metric only.

**Lemma 6 (lines 249–251).**
- Counting: at most \(1+8t/(LM)\) pieces, each of diameter \(\le LM/4+2R\le LM/2\). Each piece meets at most 16 cubes.
- Crossing bound: \(\operatorname{dist}_\infty(Z_0,H^c)\ge M\).
- Wall connectivity: the collar of one fine cube is a box of coarse cubes, so it is wall-connected.
- Correct.

**Theorem 7 (lines 278–314).**
- Double tag: \(2\times(16\bar\kappa+\theta t/2)\) needs \(128\bar\kappa/(LM)\le\theta/2\). A varied term has \(t_1+t_2\ge M-R_*\ge M/2\), so it costs \(e^{32\bar\kappa-\theta M/4}=E_M\) times \(|A|_\theta|r|_\theta\le WU_{\rm root}\).
- Floors:
  - \(WE_M\le c_L/8\) and \(H_1r\le c_L/8\) give \(\operatorname{Re}C^{-1}\ge c_L/2\) and \(\|C\|\le2/c_L\).
  - The inverse identity costs \(8/(3c_L^2)\).
  - Splitting the field change in Γ costs \(U_{\rm root}H_1r+2WU_{\rm root}r/r_{\rm loc}\).
  - The sum is \(\le H_0(E_M+r)\), with \(H_0\) exactly as in (22).
- Scaling: \(|\tau^{-1}-1|\le2|\tau-1|\) and \(|\tau^{1/2}-1|\le|\tau-1|\) give \(C_\tau=4/c_L+K_0+1\).
- \(K_0\) bounds the sum \(4/(3c_L)+W+WU_{\rm root}\).
- The real reference does not need a flat gauge. This is why \(a_0\) enters only through ceiling (10).
- Correct.

**Constants rule.**
- \(K_0\), \(H_0\), \(C_\tau\), \(d=\theta/4\), \(b=32\) and \(H_p\equiv L^3\) depend on \(c_L,a_R\) (pr-lay/c4-order row 7), on \(W,\mu_W,R_h,a_h,C_h\) (rows 5–6), and on \(L\), \(n_c\), \(r_c\), \(n\), \(\ell_{\rm IMS}\), \(b_{\rm tail}\) and \(r_{\rm av}\). All of these are fixed before \(\kappa\). None depends on \(M\), \(\bar\kappa\) or the radii.
- The later conditions are floors on \(M\): \(c_gM_1\le C_{\rm box}M\), \(M\ge2R_*\), \(LM\ge8R_*\), \(128\bar\kappa/(LM)\le\theta/2\), \(E_M\). Ceiling (24) bounds the radii and \(\tau\).
- This matches IN1 row 4 and pr-lay §2.

**Theorem 8 (lines 327–369).**
- Items 1–4:
  - FG1 with \(K_0\ge1\) and the explicit \(\varepsilon\le\varepsilon_0(K_0)\) gives FG6.
  - Heredity holds because grouped entries read only labels inside their \(R_*\) balls.
  - Wall factorization: connected hulls stay in one component, \(\Gamma\Gamma^{\mathsf T}\) is block diagonal, and \((Z_0\cap Z_i)^\sharp=H\cap Z_i\).
  - Dimension: \(12(LM)^4\#Z\).
- Item 5 is the iterated fundamental theorem of calculus, in the form of UM3.
- Item 6:
  - At \(s=1\), \(\Gamma\Gamma^{\mathsf T}=\beta(R^2)_{22}\beta^{\mathsf T}=\beta\sigma^{-1}\beta^{\mathsf T}\), and \(D=(\mathsf A^{-1})_{11}\).
  - \(D_\tau=\tau^{-1}D\) checks.
- Correct.

**Proposition 9 (lines 377–388).**
- \(R_{22}=1+\tfrac38(t^2+u^2)+O(4)\) and \(R_{21}=t/2+O(3)\).
- \(t^2(R_{21}^2+R_{22}^2)\) gives \(t^2+t^4+\tfrac34t^2u^2+O(6)\).
- This matches IN1 lines 329–330. Correct.

**Proposition 10 (lines 390–428).**
- The five-cube chain makes \(d_Z(p,q)\ge2\ell\). The two bottom links leave \(Z\).
- The potential satisfies R4. Rep also holds trivially, since \(U=I\).
- The loop is filled by \(2\ell/\epsilon\) plaquettes, so \(|g-I|\le2r_0\ell\epsilon\).
- Two covariant steps give \(|cX+\operatorname{Ad}(g)cX|\le2\epsilon r_*\), against the lower bound \(\ge2c(1-|g-I|)\). This is a contradiction for small \(\epsilon\).
- Correct as a fixed-ceiling statement.

**Corollary 13.1 (lines 432–469).**
- I checked (32)–(35) against UM13–UM15, SA 14490–14529.
- With \(\zeta=C_pW_0M^{-4}\), UM15's \(C_0=C_pW_0L^4(1+A_Kc_m)+A_Kc_mL^4M^4(\varepsilon+\gamma/2)\le\tfrac13+\tfrac13+\tfrac13\).
- UM14 holds: \(P_dW_0M^{-4}\le\zeta_0/2\) and \(\gamma_{\rm tilt}/2\le\zeta_0/2\).
- The floor \(M^4e^{-dM}\to0\) is valid.
- \(W_0\) and the bound one are fixed early. \(\varepsilon_*\) and \(\gamma_{\rm tilt}\) are not. This matches IN1 Lemma 3 (22)–(23) term by term.
- Correct.

## No silent use of descent

Every conclusion carries its domain:
- Lemma 4 assumes \(\mathcal K(Y)\), which includes Rep.
- Theorem 5 is stated on \(\mathcal W(Y)\), which includes Rep.
- Theorem 7 assumes \(P\in\mathcal K(Z)\).
- Theorem 8 (29) is "asserted when the complete \(P\) is in this working domain".
- Item 6 and line 371 require working-domain membership and G-ID.
- Corollary 13.1 is stated "on every \(P\in\mathcal K(Z)\)".
- Lines 289 and 475 say "on \(\mathcal K\)" or "on the specified representative class".

Heredity and wall factorization use only the stated fact that \(\mathcal K\) restricts hereditarily. This is true: a block whose read neighbourhood lies in \(Z\) also has it in \(Z'\supset Z\). No step takes a supremum over the SA core or infers \(\mathcal U^\circ_k\subset\mathcal K\).

## Imports

- **R.** hm line 41 matches pr-lay §2 R: \(c_L,a_R\), the fixed axial representative and the real bound. The `a2-layers-gate` §§5 and 7 cap and separation repairs are cited. The gate checked the off-shell argument without stationarity, which agrees with "does not require criticality".
- **W.** hm line 42 matches pr-lay §2 W (10), with counts \(C_h^{m+1}\) and \(N_r\), and `h-walk-gate` §§5–8: the graph-norm repair, the second-jet premise, \(C_*^{n+\sum m_i}\), \(C_h^{m+1}\), and rejection of (C5)/(H3) canonicity and reflection.
- **AV.** QC1–QC4 are at SA 7943–8001. The reading that h-walk (I2) states covariance of the derivative rows \(Q,Q'\) is correct (h-walk line 358). Lemma 3 proves the nonlinear covariance it needs.
- **FG/UM.** FG1–FG12 are at SA 13894–14249, and UM1–UM15 at SA 14276–14529. The UM2 integrand at line 318 is SA UM2 with \(Y_0\to Y_{\rm box}\) and \(P_0\to P_{\rm fail}\).
- **G-ID.** SA 14108–14118 states \(C^{(k)}=\mathsf A(P_W)^{-1}\) at the background pair and gives a reason in a few lines. "Sketches" is accurate.
- **F.** hm line 47 matches pr-lay F.
- **Other notes.** `inv-root`, `carrier-adopt`, `um-envelope` and `c4-order` have no separate gate files in `F/gates`. `carrier-check` covers inv-root, carrier-adopt and um-envelope (6). Its count \(32+256l/(LM)\) equals twice Lemma 6's count. hm agrees with these notes in every place it uses them. c4-order row 8 (cost envelope fixed before \(\bar\kappa,M\)) and row 14 (actual matrix package still required, SA 14779–14791) agree with hm lines 371 and 471.

**Match with frozen IN1 H-M (in1.md lines 99–106).** Theorem 7 gives every numerical clause of (9) with the required order:
- complex symmetric \(C\) and rectangular \(\Gamma\);
- real \(C_*>0\) and \(\Gamma_*\), with \(K_0\ge1\);
- \(H_0,b,d,C_\tau>0\) before \(\bar\kappa,M\), and \(H_p(M)=L^3\);
- the discs \(|s_\Delta|<e^{\bar\kappa}\).

Theorem 8 gives normalization, heredity, wall factorization, holomorphy and the dimension bound. One part does not match: IN1 imports these for the **actual** functional and carriers. hm supplies a replacement family on \(\mathcal K\). It says so openly at lines 5, 289 and 371. This is the declared Outstanding item, not a hidden mismatch.

## Source readings

Each reading below matches the cited text:
- SA 5729–5736: the gauge-invariance tie; extension to complex orbits is "an additional statement".
- SA 7178: box-axial (comb tree) versus block-axial (averaged contour).
- SA 10311–10338 and 10533–10550: the walk scheme for \(C^{(k)}(Y)\) and \(\chi_Y\mathsf A\chi_Y\), and parametrix mechanisms (f)–(h). "A covariance construction scheme" is a fair reading.
- SA 14091–14205:
  - IMS localization, collared \(C\) and \(\Gamma\), and the reference;
  - 14164–14169: \(\mathsf r(s)\) "does not denote \(\mathsf A(s)^{-1/2}\)";
  - \(\tau\)-rescaling and \(|\tau-1|\le c(LM)^{-4}\).
- SA 14338–14347: the collar and the permitted fixed enlargement.
- SA 14373–14401: UM4–UM6.
- SA 14513–14517: UM14.

hm.md quotes no YM3 line. The YM3 ranges named in the brief come from `hm-draft.md`. I read them anyway:
- YM3 39867–39874 has the "multiplied once by each parameter in its domain" and omit-vanishing-monomial rule. hm (19) and line 235 follow it.
- YM3 40217–40250 has the IMS kernel identity and the \(7\gamma/8\to3\gamma/4\) pattern. Lemma 4 parallels it.
- YM3 43564–43604 has M-independent early constants.

hm.md uses none of these as a proof step.

## Verdict

hm.md proves what it states, line by line, conditional on the imports R, repaired W, AV and FG/UM. G-ID is needed only for the physical clause, and F only for the completed form. The five findings are a missing check-record link, one typo, one metric clarification, one citation range and one wording point. None affects a statement or a constant. The constants rule holds. The double-tag exponent 32 and every floor check. The all-core (descent) conclusion is not used anywhere. It is correctly kept Outstanding.

Checked line by line by Claude (fresh session).
