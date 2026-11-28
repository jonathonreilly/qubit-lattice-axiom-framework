First failing step: none.

# Gate of `library/pr-lay.md` (pass 3)

Text: `library/pr-lay.md`, 381 lines, Codex pass-2 distillation of Claude's draft. I read it once, line by line, and checked every numbered statement. I did not edit it.

## What was checked and holds

- **Lemma 1 (12).** With at most \(N_r\) roots and at most \(C_h^{m+1}\) terms of length \(m\), the sum is \(N_rC_h^2e^{-\delta_hD}\sum_m(C_h^2M_1^{-1/3})^m\). \(M_1\ge8C_h^6\) gives ratio \(\le1/2\), so the bound is \(H=2N_rC_h^2\). \(\widehat l\le1\) and \(d_\infty\ge d/4\) give \(D\ge d/4\), so the rate is \(\mu_0=\delta_h/4\). There are \(4\times3=12\) coordinates per site, and \(\sum_{\mathbb Z^4}e^{-\mu|z|_1}=((1+e^{-\mu})/(1-e^{-\mu}))^4\). So \(V_0\) is right, and the Schur bound gives \(b\). Holomorphy follows from uniform convergence. \(R_h\subset R_{a_W}\) because \(h\le a_W\).
- **Lemma 2.** I recomputed the prefix product. \(Y_1=B_\mu(x)\), \(Y_2=\mathrm{Ad}(U_\mu(x))B_\nu(x+\mu)\), \(Y_3=-\mathrm{Ad}(P_UU_\nu(x))B_\mu(x+\nu)\) and \(Y_4=-\mathrm{Ad}(P_U)B_\nu(x)\) sum exactly to the displayed curl plus \((I-\mathrm{Ad}P_U)[\cdots]\). This is SA PX117 (11346), quoted correctly. \(|(I-\mathrm{Ad}P)X|=|[X,P-I]|\le2|P-I||X|\). The bound \(e^t-1-t\le(e-2)t^2\le t^2\) holds for \(t\le1\). In (14), \(\xi\le l_p\) gives \(|P_U-I|\le r_0\eta^2/\xi^2\), so \(2\alpha+4r_0(\eta/\xi)\alpha+16\alpha^2\le4\alpha\) for \(r_0\le1/4\) and \(\alpha\le1/16\). (5) and (13) give \(\alpha<h/8\). The complex curvature is then below \(r_0+h/2<h\). The same \(r_0\) bounds real and complex curvature in the class; the closing sentence correctly enlarges it to a common radius below \(h\).
- **(5).** A plaquette stencil touches at most two adjacent layers because \(\rho>4\). So the corner scales differ by at most \(L\), which costs \(L\) for potentials and \(L^2\) for first derivatives.
- **Theorem 3, the Schwarz step.** \(r<r_*\le h/(16L^2)\) gives \(R>2\). \(f(z)=A(P_z)_{xy}\) is holomorphic on \(|z|<R\) by Lemmas 1–2. \(P_{z=0}=P_0\). \(|f-f(0)|\le2He^{-\mu_0d}\). Schwarz on radius \(R\) gives \(|f(1)-f(0)|\le2He^{-\mu_0d}\cdot8L^2r/h=H_1re^{-\mu_0d}\), with \(H_1=16L^2H/h\) as in (11). Then Schur gives \(\|A-A_0\|\le H_1rV_0<c_L/2\) from the second term of \(r_*\). The real-symmetric gap extends to complex vectors because the cross terms cancel. This gives the gap \(a=c_L/2\).
- **Theorem 3, symmetry.** \(R\) is symmetric when \(G'\) is. \(S\) is not symmetric, but it enters only through the congruence \(S^{\mathsf T}\Delta^{(2)}S\), and the text does not claim more. SA's \(\Delta'_\pi\) (10176–10185) is visibly symmetric under \(A\leftrightarrow C\). \(E_{\rm amb}\) is symmetric because it is a second derivative. The compression clause is right: the gap is \(a|\chi v|^2\).
- **Lemma 4.** For \(d\le r_F\), \(C_Fr\le E_Fre^{-\mu_0d}\) with \(E_F=C_Fe^{\mu_0r_F}\), and the norm is \(<a/2\) by the extra ceiling. Each entry of (16) checks. The identity \(\Phi''=-h_Vq''[C_V\cdot,C_V\cdot]\) and its chain rule agree with a2-full-gate §3, Lemma 3.6, and its ambient/free repair.
- **Lemma 5.** Both G gaps are \(\ge2\rho\xi_j\) by step 3. Meets keep the smaller floor.
- **Lemma 6, \(j\ge1\).**
  - Unit conversions: \(|\partial U-I|\le L^4v\eta'^2\) and \(|J^\circ_{\eta'}|\le L^6v\).
  - Unitary skew-part identity and conversion: the conversion with 6 is weaker than the exact 3, so it is safe.
  - The \(1+6w\eta'<2\) step holds since \(w\eta'\le v\).
  - With \(w'=L^3v\), the three RCG4 premises are strict: \(L^4<L^5\); \(2L^4w=2L^6v=2L^3w'\), strict from the previous step; and (21) with factor 2 to spare.
  - Rescaling costs \(L^{-1}\) and \(L^{-2}\). The result is \(4L^4B_*(c_gM_1+2L)v=C_Gv/2\).
  - Room: \(\rho/L^2\ge3+2/L^2\) keeps the enlargement and its stars inside \(\Omega_{j-1}\), strictly inside \(\Omega_0\).
- **Lemma 6, \(j=0\).** The axial tree gauge needs at most \(3n\) plaquettes per link. The telescoping bound is \(\le3nv<2\). Jordan's inequality gives \(\eta|A|\le(3\pi/2)nv\), and \(3\pi c_gM_1\le C_G\).
- **Lemma 7.** The sign of the derivative and the monotone supremum are right. The limit via \(e^u\ge u^n/n!\) is right. \(r(P)\le D_cF_{q+2r_R}\) needs \(\theta_\nu\ge\gamma^{-2}\) at every assigned index; that is part of RUN/D.
- **Line 257.** RUN gives \(\theta_m\le\theta_\nu+C_\theta\le2\theta_\nu\). With \(\theta_\nu\ge2\), \(\log\theta_m\le2\log\theta_\nu\), so \(C'_\lambda=2^{2r_R}C_\lambda\).
- **Theorem 8.** Lemma 5 gives the geometry. Lemma 6 with (23a) gives a real bound \(<h/2\le a_R\). D, Lemma 7 and (23b) give \(r<r_*\). The ceilings in \(\gamma\) are monotone, because the supremum is over \(t\ge\gamma^{-2}\).
- **Constants rule.** \(a,b,H,\mu_0,H_1,r_*\) and \(E_F\) depend only on \(c_L,C_h,N_r,\delta_h,L,h,C_F,r_F\). h-walk's order of constants makes all of these functions of \(L\), fixed before \(M_1\). None depends on \(M_1,\kappa,\bar\kappa\) or \(M\). \(C_G\) depends on \(M_1\) but enters only (21) and (23). The late quantities \(A_0,C_0,C_1,\beta_s\) and \(\gamma_B(M)\) enter only the coupling ceiling. This agrees with c4-order rows 5–7 (walk constants, then \(M_1\to R_1\to\rho\), then \(c_L\)), row 8 (\(\kappa\)), row 12 (\(M\)) and row 16 (amplitudes), and with frozen IN1 "Constant order" rows 3–6 and 9.
- **D is not used silently.** Theorem 3 uses only R and W. Lemma 4 uses only F. Lemmas 5–6 use only G, B and Q. D enters only in Lemma 7's second assertion, which says "Under D", and in Theorem 8. Every downstream sentence (329, 366, 368) is conditional on D.
- **Imports against their notes and gates.**
  - **R:** a2-layers Theorem A (76–88, 652–663) and a2-layers-gate §7 (cap repair). R uses only the real gap at \(P_0=(U,0,0)\). It does not use Theorem B's full-A2 scope, which the gate rejects.
  - **W:** h-walk Theorem H (H1)–(H3) and h-walk-gate §8. The count \(C_h^{m+1}\), the bounded roots, the \(M_1^{-1/3}\) decay and fixed-region holomorphy are exactly the surviving clauses. The longer-sequence metric only weakens (H2).
  - **F:** a2-full Lemma 4.1 and a2-full-gate §§3–4.
  - **Q:** RCG4 as stated in st1-r3 136 and st1-draft2 219. It comes from a1-balaban §3.8, conditional on F0, and a1-balaban-gate 158 calls those estimates sketches. The text says the same.
  - **G:** os-draft Lemma 2.3 and Corollary 2.4. There is no os-draft gate in `gates/`.
  - **Frozen texts:** P82 I7 (154) and IN1 108/H-M are quoted correctly.
- **SA quotations.** I read every cited range in `sa/ym4.tex`. The readings are correct:
  - 10129–10137: regular pairs and cube gauges.
  - 10141–10208: operator formulas; \(\Delta'_\pi\) at 10176–10185; \(\mathsf A\) at 10204.
  - 14091–14107: actual regular precision.
  - 6141–6155: lift; layer-zero, top and base-structure exceptions; inclusion called hypotheses.
  - 6035: waiting depth.
  - 17398–17407: Prop. 2.3 gaps \(cM\check R_j\) and \(LM\).
  - 10307: ceiling independent of \(M_1\).
  - 10242–10263, 9793–9802, 5696–5718 and 6026–6038.
  - PX1, PX4, PX54–PX68: PX58 is a directional Cauchy step.
  - 11204–11255: PX101–PX104 pivot chain rule.
  - 17578–17592, 17618–17630 and 19485–19495.

## Findings

1. **Lines 228–229 and 255. B's source pinpoints use superseded ST1 rounds. Repairable, not fatal.**
   - **What is wrong:** the text cites st1-r2 Lemma 10 (56)–(60) with \(C_{\rm RA}=12C_PC_{\rm sm}L^4\), st1-draft3 Lemma B1, and st1-r2 84–99. The operative ST1 is st1-r3. Its Lemma 10 (648–700) drops the smoothed lift \(\lambda\) and states (59) as \(l^2\eta^{-2}|\partial U-I|,\ l^3|J^\circ|\le C_U\ell_m^{2r_R}\varepsilon_m\), with \(\ell_m=\log\theta_m\). Its Lemma B1 is at 717–723, and the frozen-at-birth clause is at 112.
   - **What still holds:** the st1-r2 arithmetic is right (\(2C_P\cdot6C_{\rm sm}L^4\)). \(\varepsilon_m\) with \(A_0\) matches st1-r3 (Tq0).
   - **Repair:** cite st1-r3 Lemma 10 (56), (58), (59), Lemma B1 and line 112. Replace \(C_{\rm RA}\lambda(e)\le C_{\rm RA}C_\lambda(\log\theta)^{2r_R}\) by \(C_U(\log\theta)^{2r_R}\). Only the product \(C_{\rm RA}C_\lambda\) enters \(v\), (20) and (23), so the proofs are unchanged with \(C_{\rm RA}C_\lambda\to C_U\). \(C_U\) precedes \(\kappa\) and \(M\) (st1-r3 682), so step 3 stays valid.

2. **Lines 255 and 329. The NL1 cross-references use draft names. Repairable, not fatal.**
   - **What is wrong:** "NL1 Theorem V′" and "NL1's (CI-form)(ii)" appear only in nl1-L-draft.md and ci-form-draft.md. The operative nl1-L.md has Theorem 4 (input L) and Theorem 7, with items CI-base, CI-maps, CI-Gauss and CI-form. There the precision/comparison package is item 3, **CI-Gauss**, and the domain obligation is CI-maps.
   - **Repair:** retarget 255 to the inputs of nl1-L Theorem 4/Theorem 7 (CI-maps). Retarget 329 to "the precision part of CI-Gauss". The conclusion is unchanged: H-M and CI stay open.

3. **Line 331. The seam-loss claim is right in scope, but it is under-stated. Repairable (clarity), not fatal.**
   - **What holds:** Theorem 3's hypotheses and proof read only the current longer sequence's scales. The only seam factor is the fixed \(L^2\) of (5), which sits in \(H_1\) and \(r_*\). So layered-a3 (3), the factor \(L^{2v}/L_\flat^{2v}>4^v\) from bounding a coarser tower by finer control, does not enter (15).
   - **What is missing:** for Theorem 8, any conversion from an inherited or birth scale to the current scale is the content of D, because (19) is posed at the current \(l\). The same applies to B's current-scale reading. So the loss is moved into D, not removed.
   - **Repair:** add one sentence saying that any such conversion, including a (3)-type loss, must be paid in verifying D (and B), and that Theorem 8 does not avoid it.

4. **Lines 318 and 329. Holomorphy is not stated where IN1 Lemma 2 needs it. Repairable, not fatal.**
   - **What is wrong:** the text says Theorem 8 "supplies the precision hypotheses of frozen IN1 Lemma 2". IN1 Lemma 2 (276) also asks that \(A(P)\) be holomorphic, and (15) does not list this.
   - **Repair:** add Lemma 1's clause to Theorem 8's conclusion. The entries are holomorphic along holomorphic families in \(\mathcal R_h\) with fixed real \(U\) and fixed regions. Also note that IN1's holomorphy must be along families of that kind.

5. **Lines 278–297. Lemma 6, \(j\ge1\), uses a cube that may not be aligned. Repairable, constants unchanged.**
   - **What is wrong:** \(Z\) is any cube of side \(\le c_gM_1\xi_j\) (SA 10137 says "every cube"). ST1's conventions (st1-r3 §1) make cubes aligned, and the text applies RCG4 to \(Z\) itself in level-\((j+1)\) units.
   - **Repair:** apply RCG4 to the aligned level-\((j+1)\) cube of side \(s+1\) that contains \(Z\), and restrict the gauge to \(Z\).
     - Room: this needs \(\rho\ge4L^2+2\). It holds, because \(\rho=R_1M_1\ge64L\cdot L\).
     - (21): the factor 2 already covers \((s+3)\le2(s+2)\).
     - Bound: the gauge bound becomes \(4L^4B_*(c_gM_1+3L)v\le C_Gv\), so the conclusion "real bound \(C_Gv\)" stands.

## Verdict

Theorem 3 is proved as an implication from R and W on the stated regular class:
- symmetry;
- the uniform gap \(c_L/2\);
- the entry decay \(He^{-\mu_0d}\);
- the Schwarz-lemma perturbation \(H_1r(P)e^{-\mu_0d}\), linear in the complex pair size.

Lemma 4 is proved under F. Lemmas 5–7 and Theorem 8 are a correct conditional admission route under G, B, Q and D. D is used only where it is named. The constants of (15)–(16) are fixed before \(\kappa\) and do not depend on \(M\) or \(\bar\kappa\); late quantities enter only the coupling ceiling. The seam loss of layered-a3 (3) does not enter (15); for the actual domains it is moved into D (finding 3).

All five findings are pinpoint, scope or bookkeeping repairs, and none is fatal. D for the actual domains, IN1's H-M, and PR1(5b) remain open, as the text itself says.

Checked line by line by Claude (fresh session).
