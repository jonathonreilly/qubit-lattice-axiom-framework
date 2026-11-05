# PR-lay: precision gap and decay at complex layered stage pairs

Provenance: Codex, pass 2 (distillation), 2026-11-04, checkout 2afa141308f85e0fb262acd684c25a49e354feb6; Claude's 497-line [pass-1 draft](pr-lay-draft.md) read in full. Research text, not an audit; no status is granted.

Credit: **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, for the regular-pair class, operators, layered geometry and complex directional argument. SA, CA-I and YM3 below mean their outline, complete account I and YM3/YM3_I.tex at **31a47c543775**. Tadeusz Balaban supplies the background-field and walk methods; Jonathan Dimock supplies expositions. Library imports by Claude and Codex retain their dependencies.

The main result is Theorem 3, an operator implication on a specified class. Theorem 8 transfers it to stage pairs **if** their actual domains satisfy the named admission inputs. That identification remains **Outstanding**. All deductions below are hand proofs.

## 1. Definitions

**Geometry and units.** Fix odd \(L\ge27\), depth \(k\ge0\), \(\eta=L^{-k}\), and \(\xi_j=L^{j-k}\). On a finite compatible four-dimensional torus let
\[
 \mathbf S=(\Omega_0,\ldots,\Omega_{k+1}),\qquad
 \operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho\xi_j,\quad
 \rho=R_1M_1.                                                     \tag{1}
\]
Each member is a union of aligned level-\(j\) \(M_1\)-cubes; \(M_1,R_1\) are powers of \(L\). Empty terminal regions are allowed. The **longer class** has layers \(\mathcal L_j=\overline{\Omega_j\setminus\Omega_{j+1}}\), with \(\mathcal L_{k+1}=\Omega_{k+1}\). Boundary readings use the largest incident scale. A bond or plaquette has the largest corner scale \(l_b,l_p\). Inward constraint rows are omitted. Fine fields have the inner-plaquette, outer Dirichlet convention of a2-layers §1.

The operators below use the sequence **cut at depth \(k\)**: its last layer is \(\Omega_k\), including \(\Omega_{k+1}\). Write \(\widehat l=\min(l,1)\) for its point scale, extended by \(\eta\) outside \(\Omega_0\), and
\[
 D(x,y)=\inf_{\gamma:x\to y}\int_\gamma \widehat l(z)^{-1}\,ds_\infty.
                                                                    \tag{2}
\]
This is the depth-\(k\) metric of h-walk (H2), not the longer metric which uses scale \(L\) in \(\Omega_{k+1}\). Let \(d(x,y)\) be periodic \(\ell^1\) distance in level-\(k\) units. Free coordinates are positively stored, non-pivot level-\(k\) bonds touching \(\Omega_{k+1}\), with three real colour coordinates per bond. Thus there are at most twelve coordinates per site. A compression acts on its coordinate subspace.

All required cubes and their read margins embed in the torus. In particular this includes the walk-model boxes and the side-\((s+6)\) cubes used below. This torus-room requirement is part of the geometry, not a volume-dependent constant.

**Fields and regularity.** Real fields take values in \(SU(2)\); complex fields take values in \(SL(2,\mathbb C)\). Potentials are traceless complex \(2\)-by-\(2\) matrices. Their norm is the matrix operator norm. Real potentials are Hermitian. The colour pairing is \(\frac12\operatorname{Tr}(XY)\); final coordinate norms are Euclidean in an orthonormal real colour basis, with \(\langle v,w\rangle_H=\sum_x\overline{v_x}w_x\). Transposes use the bilinear pairing, not this Hermitian pairing. Fixed finite-dimensional norm conversions are included in imported constants. Set
\[
 P=(U,A',\mathbf J),\quad \mathbf U=e^{i\eta A'}U,\quad
 P_0=(U,0,0),\qquad
 (\nabla^U_\nu A')_\mu(x)
 =\eta^{-1}\{\operatorname{Ad}(U_\nu(x))A'_\mu(x+\eta e_\nu)-A'_\mu(x)\}.
                                                                    \tag{3}
\]
Here \(U\) is real and \(\mathbf J\) is independent of \(\mathbf U\). Reversal uses \(A'(\bar b)=-\operatorname{Ad}(U(b)^{-1})A'(b)\). Every derivative reading includes its full stencil.

Fix an integer cube constant \(c_g\ge1\), large enough for the imported local models. Say that \(U\) has **real bound \(r_0\)** if
\[
 \eta^{-2}l_p^2|\partial U(p)-I|\le r_0
\]
on every inner plaquette, and every cube of side at most \(c_gM_1\xi_j\) in \(\Omega_0\cap(\mathcal L_j\cup\mathcal L_{j+1})\) has a real gauge \(U^g=e^{i\eta A}\) with
\(\xi_j|A|,\xi_j^2|\nabla A|\le r_0\).
For the final layer use \(\mathcal L_{k+2}=\varnothing\). The gauge bound holds throughout the cube on contained stencils. We require actual witnessing gauges, rather than assuming attainment of an infimum.

Define the own-scale complex size
\[
 r(P)=\max_{b,\mu,\nu}
 \{l_b|A'(b)|,\ l_b^2|(\nabla^U_\nu A')_\mu(b)|,\ l_b^3|\mathbf J(b)|\}.
                                                                    \tag{4}
\]
The derivative is based at the positively stored component bond. At a shared face all required layer readings are imposed. Define \(s(P)\) as the maximum of (4) and, for every plaquette at each required scale \(\xi\), the four quantities \(\xi|A'|\) on its links and the two quantities \(\xi^2|\nabla^UA'|\) used in its forward curl. Separation with \(\rho>4\) gives
\[
                        r(P)\le s(P)\le L^2r(P).                    \tag{5}
\]
Indeed a plaquette stencil cannot cross two layer boundaries: it would cross a complete layer of width \(>\rho\eta\), whereas its diameter is at most \(2\eta\). Its scales therefore differ by at most \(L\). This costs at most \(L^2\) for a first derivative.

The **regular class** \(\mathcal R_h(\mathbf S)\) consists of pairs for which some \(r_0,r_1,r_J<h\) satisfy: \(U\) has real bound \(r_0\); \(\eta^{-2}l_p^2|\partial\mathbf U(p)-I|\le r_0\); \(l_b|A'|,l_b^2|\nabla^UA'|\le r_1\); and \(l_b^3|\mathbf J|\le r_J\), on all the specified reads. This is a precise sufficient reading of SA 10129–10137 on the longer sequence, with its real cube gauges and largest-scale seam convention.

**The operator and its gauge convention.** Fix the step's real representative, with \(\mathcal M^kU\) block axial on the active blocks. This is a hypothesis on that representative. Full gauge covariance of the soft gauge Hessian is not asserted. In the matched physical bilinear pairings set
\[
\begin{split}
 G'&=(D_{\mathbf U}^{\mathsf T}D_{\mathbf U}+Q'^{\mathsf T}\mathsf aQ')^{-1},&
 R&=I-G'Q'^{\mathsf T}(Q'G'^2Q'^{\mathsf T})^{-1}Q'G',\\
 S&=I-D_{\mathbf U}G'RD_{\mathbf U}^{\mathsf T},&
 G_0&=(\Delta^{W}_{\mathbf U}+D_{\mathbf U}RD_{\mathbf U}^{\mathsf T}
                                  +Q^{\mathsf T}\mathsf aQ)^{-1},\\
 G&=(G_0^{-1}-\Delta'_\pi[\mathbf J])^{-1},&
 \mathsf H&=GQ^{\mathsf T}(QGQ^{\mathsf T})^{-1},\\
 G_1&=(G^{-1}-S^{\mathsf T}\Delta^{(2)}[\mathsf H^{\mathsf T}\mathbf J]S)^{-1},&
 \mathsf H_1&=G_1Q^{\mathsf T}(QG_1Q^{\mathsf T})^{-1}.
\end{split}                                                        \tag{6}
\]
Here \(Q,Q'\) are the actual straightened field and site averages. The row-weight operator \(\mathsf a\), distinct from the scalar gap \(a\) below, is \(\xi_c^{-2}\) on rows and the specified comparable \(\xi_y^{-2}\) weight on tops. \(\Delta^W\) is the inner Wilson Hessian; \(\Delta'_\pi\) is the explicitly symmetric independent-current form of SA 10163–10185. Also \((B,\Delta^{(2)}[j]B)=2(C^{(2)}(B),j)\), with \(C^{(2)}\) the quadratic straightened average per unit length. These maps, their branches and boundary conventions are imported; inversion is not inferred from the notation.

Put \(V=\mathcal M^k\mathbf U\). Let \(\iota\) inject the active level-\(k\) bonds into all determining rows, and \(C_V\) be the derivative of the actual pivot graph. With \(K_{\rm GF}\) the ambient Hessian of the actual soft gauge functional,
\[
 A(P)=C_V^{\mathsf T}\left[
 \iota^{\mathsf T}\{(QG_1Q^{\mathsf T})^{-1}-\mathsf a\}\iota+K_{\rm GF}
       -E_{\rm amb}[\iota^{\mathsf T}\mathsf H_1^{\mathsf T}\mathbf J]\right]C_V.
                                                                    \tag{7}
\]
This is SA 10200–10208 and 14091–14107 with active injections explicit. Define
\[
 q_V(B)=i^{-1}\Log(\mathcal M(e^{iB}V)\mathcal M(V)^{-1}),\quad
 E_{\rm amb}[j](b,c)=\langle h_V^{\mathsf T}j,q_V''(0)[b,c]\rangle ,
                                                                    \tag{8}
\]
where \(h_V\) is the pivot-supported right inverse of \(q_V'(0)\).
Thus \(E_{\rm free}[j]=C_V^{\mathsf T}E_{\rm amb}[j]C_V\); it must not be sandwiched again. The completed form is
\[
 A_{\rm full}=A-E_{\rm free}[J_{\rm GF}],\qquad
 J_{\rm GF}=\nabla_B\mathrm{GF}(e^{iB}V)|_{B=0}.                      \tag{9}
\]
Identification of (9) with a physical action Hessian additionally requires the physical-current and background-branch identities. Estimates at independent currents do not prove that identification.

## 2. Imports and order of choice

**R — real gap.** There are positive \(c_L,a_R\) and geometric floors such that \(A(P_0)\) exists, is real symmetric, and \(A(P_0)\ge c_LI\) whenever the longer sequence satisfies those floors and \(U\) has real bound \(<a_R\) in the stated axial representative.

This is the conditional content of a2-layers Theorem A, with the cap and separation repairs in [its check](../gates/a2-layers-gate.md), §§4–7. It retains the flat c0-loc inputs and a2-curved coefficient/second-jet inputs, examined in [a2-curved-gate](../gates/a2-curved-gate.md). They are not re-proved here.

**W — complex walk package, fixed regions.** For every \(\mathcal R_{a_W}(\mathbf S)\) above fixed floors, all inverses in (6)–(7) exist, and
\[
 A(P)=\sum_\omega A_\omega(P),\qquad
 |A_\omega(P)_{xy}|
 \le C_h(C_hM_1^{-1/3})^{|\omega|}
                         e^{-\delta_hD(\omega;x,y)}.                \tag{10}
\]
Here \(C_h\ge1,\delta_h,a_W>0\). At most \(C_h^{m+1}\) terms of length \(m\) have a given root. At most \(N_r\) roots contribute at a fixed \(x\). The tree distance is at least \(D(x,y)\). Each term is holomorphic in \((A',\mathbf J)\) at fixed \(U\) and fixed regions, and real at \(P_0\).

This imports only the surviving kernel/support/holomorphy clauses of h-walk Theorem H, with [h-walk-gate](../gates/h-walk-gate.md), §§5–8. Its premise includes the repaired a2-layers complex inverse/conjugation package **on every cut-down**, the all-scale absolute row/column second-jet coefficient bound of a2-curved (8.3)/(8.10), and the bounded analytic one-step maps. The four inverse bounds alone are insufficient. The rejected region-trace canonicity and single-term reflection claims are not imported. W already uses a complex operator package; the gap deduction below is not an independent construction of that package.

**F — optional gauge correction.** On the same class, for \(r(P)<a_F\), the symmetric matrix \(E_{\rm free}[J_{\rm GF}]\) vanishes at \(P_0\), has range at most \(r_F\) in \(d\), and entries at most \(C_Fr(P)\). This follows conditionally from a2-full Lemma 4.1 and its bounded finite stencils, using the ambient/free correction in [a2-full-gate](../gates/a2-full-gate.md), §§3–4. The fixed norm conversions are included in \(C_F\).

All constants just named, including the floors, depend only on the early analytic/geometric inputs. Those inputs must be uniform in depth, volume, region shape and larger admissible gaps. Their known library derivations remain conditional.

Choose constants in this order, respecting frozen [IN1](in1.md), “Constant order,” and c4-order rows 1–7:

1. Fix margins, exponents, \(L,c_g\), the label-gap constant \(c\), flat/averaging inputs, R and W, and F if used. Fix their rates and ceilings, the local-gauge constants, the profile/response rates, and the RUN constants needed by B. Rates precede the actual gap. Set \(h=\min(a_R,a_W,1/2)\).
2. Choose \(M_1\ge\max(M_R,M_W,8C_h^6)\), where \(M_R,M_W\) are the imported cube floors. Then choose \(R_1\ge64L\), with \(\rho=R_1M_1\) above all imported floors, including B's rate-times-gap floors, and \(\rho\ge3L^2+2\). Set
\[
\begin{gathered}
 V_0(\mu)=12\left(\frac{1+e^{-\mu}}{1-e^{-\mu}}\right)^4,\quad
 \mu_0=\delta_h/4,\quad H=2N_rC_h^2,\quad b=HV_0(\mu_0),\\
 a=c_L/2,\quad H_1=16L^2H/h,\quad
 r_*=\min\{h/(16L^2),\,c_L/(2H_1V_0(\mu_0))\}.                    \tag{11}
\end{gathered}
\]
For F also fix \(E_F=C_Fe^{\mu_0r_F}\) and replace \(r_*\) by
\(\min(r_*,a_F,a/[2E_FV_0(\mu_0)])\), omitting the last constraint if \(C_F=0\).
3. Fix the returned bounds \(C_{\rm RA},C_\lambda,C_\lambda'\) of §4 and \(C_G\) of (20), from the earlier inputs and \(M_1\). These choices all precede the entropy parameter \(\kappa\). Then choose \(\kappa,\bar\kappa\), and the construction size \(M\), with \(M_1\mid M\), \(LM\ge2\rho\) and \(cM\ge2\rho\).
4. Choose the test/radius amplitudes \(A_0,C_0,C_1\), any post-\(M\) box constants, and finally \(\gamma\). Quantities chosen at this last step may depend on \(M,\bar\kappa\).

Thus \(a,b,H,\mu_0,H_1,r_*\) are fixed **before \(\kappa\), independently of \(M,\bar\kappa\)**. There is no identification of the field size \(r(P)\) with \(\kappa\). The draft's row numbers 1–3 for this package were incorrect; c4-order places it through row 7.

## 3. Operator estimates

**Lemma 1 (summation and holomorphy).** Under W and the choices above,
\[
 |A(P)_{xy}|\le He^{-\mu_0d(x,y)},\qquad \|A(P)\|\le b.             \tag{12}
\]
Each entry is holomorphic along every holomorphic one-variable family staying in \(\mathcal R_h\), with fixed real factor and regions.

*Proof.* Since \(\widehat l\le1\), every path in (2) has length at least its physical \(\ell^\infty\) arclength. Periodic endpoint distances satisfy \(d_\infty\ge d/4\); hence \(D\ge d/4\). Sum (10), first over its at most \(N_r\) roots, then lengths:
\[
 \sum_\omega|A_\omega(P)_{xy}|
 \le N_rC_h^2e^{-\delta_hD(x,y)}
        \sum_{m\ge0}(C_h^2M_1^{-1/3})^m
 \le He^{-\mu_0d(x,y)} .
\]
Each torus site has a distinct chosen lift in \(\mathbb Z^4\) at its periodic distance from \(x\). Therefore
\(\sum_y e^{-\mu d(x,y)}\le12\sum_{z\in\mathbb Z^4}e^{-\mu|z|_1}=V_0(\mu)\).
Both Schur sums are at most \(HV_0(\mu_0)\). The same geometric majorant is uniform along the family. Uniform convergence of the holomorphic entry series proves holomorphy. ∎

**Lemma 2 (an admitted complex line).** Suppose \(U\) has real bound \(r_0<h/2\), and \(r=r(P)>0\). For
\[
 P_z=(U,zA',z\mathbf J),\qquad |z|<R:=h/(8L^2r),                 \tag{13}
\]
one has \(P_z\in\mathcal R_h(\mathbf S)\).

*Proof.* We first bound a plaquette at any one of its required scales \(\xi\). Let \(B=zA'\), \(\alpha=s(P_z)\), and let \(P_U=\partial U(p)\). Write the varied plaquette as
\(\prod_{\ell=1}^4e^{i\eta Y_\ell}P_U\), transporting each oriented \(B\) by the preceding real link product. Unitarity preserves its norm. Direct multiplication gives
\[
 \sum_\ell Y_\ell
 =\eta(\nabla_\mu^UB_\nu-\nabla_\nu^UB_\mu)(x)
 +(I-\operatorname{Ad}P_U)
   [\operatorname{Ad}(U_\nu(x))B_\mu(x+\eta e_\nu)+B_\nu(x)].
\]
Since \(|(I-\operatorname{Ad}P_U)X|\le2|P_U-I||X|\), the sum is at most
\(2\eta\alpha\xi^{-2}+4|P_U-I|\alpha\xi^{-1}\).
For \(t=\sum_\ell|\eta Y_\ell|\le4(\eta/\xi)\alpha\le4\alpha\le1\), the exponential series gives
\[
 \left|\prod_\ell e^{i\eta Y_\ell}-I-i\eta\sum_\ell Y_\ell\right|
 \le e^t-1-t\le t^2.
\]
The last inequality follows by bounding \(\sum_{n\ge2}1/n!\le1\). Consequently, for \(\alpha\le1/16\) and \(r_0\le1/4\),
\[
 \eta^{-2}\xi^2|\partial(e^{i\eta B}U)-\partial U|
 \le2\alpha+4r_0(\eta/\xi)\alpha+16\alpha^2\le4\alpha.             \tag{14}
\]
By (5) and (13), \(\alpha\le L^2|z|r<h/8\le1/16\). Thus the complex curvature is \(<r_0+h/2<h\). The potential, derivative and current bounds are \(<h/8\); the real cube gauges are unchanged. All class radii can be chosen strictly below \(h\). ∎

**Theorem 3 (PR1(5a), regular-class form).** Assume R and W, the definitions and choices above. For every such longer sequence, every axial real \(U\) with real bound \(r_0<h/2\), and every pair \(P\) with \(r(P)<r_*\), the inverses in (6)–(7) exist and
\[
\begin{split}
 A(P)^{\mathsf T}&=A(P),\qquad A(P_0)\text{ is real symmetric},\\
 \operatorname{Re}\langle v,A(P)v\rangle_H&\ge a|v|^2,\qquad \|A(P)\|\le b,\\
 |A(P)_{xy}|&\le He^{-\mu_0d(x,y)},\\
 |(A(P)-A(P_0))_{xy}|&\le H_1r(P)e^{-\mu_0d(x,y)}.               \tag{15}
\end{split}
\]
Every coordinate compression has the same gap on its range and the restricted entry bounds. At \(P_0\) the last difference is zero. Constants are uniform in the sense stated in §2.

*Proof.* If \(r=0\), use R and Lemma 1. Otherwise (13) has \(R>2\). Lemmas 1–2 give a holomorphic function \(f(z)=A(P_z)_{xy}\), bounded by \(He^{-\mu_0d(x,y)}\) on that disc. Apply Schwarz's lemma to \(f(z)-f(0)\), bounded by twice that number and vanishing at zero. At \(z=1\),
\[
 |f(1)-f(0)|\le2He^{-\mu_0d}/R=H_1r e^{-\mu_0d}.
\]
Schur summation gives \(\|A(P)-A(P_0)\|\le H_1rV_0(\mu_0)<c_L/2\). The real symmetric gap from R extends to complex vectors by splitting their real and imaginary parts. Subtracting the perturbation proves the Hermitian-part gap.

All quadratic Hessians in (6)–(8), including the specified current form, are bilinearly symmetric. \(G'\) is symmetric, and the formula for \(R\) is symmetric. Inversion and congruence preserve this symmetry; successively \(G_0,G,G_1,QG_1Q^{\mathsf T}\), and (7) are symmetric. W supplies existence; it also supplies reality at \(P_0\). Lemma 1 supplies the upper bounds. Finally
\(\langle v,\chi A\chi v\rangle_H=\langle\chi v,A\chi v\rangle_H\).
The gap is \(a|\chi v|^2\), not \(a|v|^2\) on the whole zero-extended space. ∎

**Lemma 4 (completed gauge form).** With F and its extra ceiling in §2, (15) holds for \(A_{\rm full}\), replacing
\[
 (a,b,H,H_1)\quad\hbox{by}\quad
 (a/2,\ b+a/2,\ H+E_Fr_*,\ H_1+E_F).                              \tag{16}
\]

*Proof.* The correction vanishes for \(d>r_F\), so its entries are at most \(E_Fr(P)e^{-\mu_0d}\). Its Schur norm is at most \(E_Fr(P)V_0(\mu_0)<a/2\). It is symmetric and zero at \(P_0\). Add these estimates to (15). The geometric identity behind (9) is also direct: differentiating \(q_V(\Phi_V(u))=0\) twice gives \(\Phi_V''=-h_Vq_V''[C_V\cdot,C_V\cdot]\). The chain rule for the gauge functional supplies precisely \(-E_{\rm free}[J_{\rm GF}]\). ∎

## 4. Admission at actual structures

The following inputs concern the **same current longer sequence and real representative** used in (7). They are additional hypotheses, not consequences of Theorem 3.

**G — actual geometry.** At each structure, including the next region used by its fibre, members are unions of aligned level-\(j\) \(M\)-cubes or cells made of those cubes. Stage, prepared and retained drop-out sequences have gaps at least \(LM\xi_j\). Label gaps are at least \(cM\xi_j\), for fixed \(c>0\). All required torus room holds. This is the geometry asserted in SA Proposition 2.3, 17398–17407, and the conditional supply in os-draft Lemma 2.3/Corollary 2.4. It is not independently established here for all histories.

**B — real background supply.** At every such structure \(U\) is the supplied regular critical background, in the step's real axial representative. On complete elements,
\[
 \eta^{-2}l_p^2|\partial U(p)-I|,\quad l_b^3|J^\circ_\eta(U)(b)|
 \le C_{\rm RA}\lambda(e)\varepsilon_{m(e)},\qquad
 \lambda(e)\le C_\lambda(\log\theta_{m(e)})^{2r_R},                 \tag{17}
\]
where \(\varepsilon_m=A_0\theta_m^{-1/2}(\log\theta_m)^{p_0}\) and
\(\theta_m\ge\gamma^{-2}>1\). Every inner plaquette is complete for its curvature reading; a complete current bond has all six incident plaquettes supplied. \(J^\circ\) has the normalization used by ST1 in the divergence estimate below.

The source is st1-r2 Lemma 10, (56)–(60), with
\(C_{\rm RA}=12C_PC_{\rm sm}L^4\). It retains PROF, AV/CURV, A1/F0/REG, RUN, the actual tests (58), the inherited raw-lift bound (56), and the specified complete carriers. At outputs it additionally retains st1-draft3 Lemma B1: BOX-bg, GEO-box, RUN-low, the output lift rule, and \(\gamma\le\gamma_B(M)\). These are draft conditional results, not new conclusions of this manuscript. In particular, existence of the real background and satisfaction of its tests are not derived by (17).

**Q — local real gauge.** In any level-\(i\) units, on a cube of side \(s\), assume its side-\((s+6)\) enlargement is supplied. If there
\[
 |\partial U-I|<wL^2\eta_i^2,\quad
 |D_U^{\mathsf T}\partial U|<2L^3w\eta_i^2,\quad
 (s+2)L^3w<c_{\rm rg},
\]
there is a real gauge on the cube with
\[
             |A|,|\nabla A|<4L^3B_*(s+2)w.                         \tag{18}
\]
Take \(0<c_{\rm rg}\le1\), \(B_*\ge1\), fixed before \(\kappa\). This is precisely ST1's RCG4 import, from a1-balaban §3.8, conditional on F0. Its existing check follows the ported estimates as sketches; it does not make (18) unconditional. The auxiliary gauge construction is fixed at its own floors, as in frozen P82 I7; it is not required to use the actual large \(M_1,R_1\) as auxiliary sizes.

**D — global current-layer domain supply.** Every complex input pair on which the consumer uses (7), with its fixed real \(U\), satisfies on **every required bond and derivative stencil of \(\Omega_0\)**
\[
\begin{split}
 l|A'|,\ l^2|\nabla^UA'|&\le(1+\beta_s)\lambda_\sigma C_1
                 \theta_\nu^{-1/2}(\log\theta_\nu)^q,\\
 l^3|\mathbf J|&\le(1+\beta_s)\lambda_\sigma C_0
                 \theta_\nu^{-1/2}(\log\theta_\nu)^q,\qquad
 \lambda_\sigma\le C_\lambda'(\log\theta_\nu)^{2r_R}.              \tag{19}
\end{split}
\]
Here \(l\) is the **current** longer-sequence scale, and \(\nu\) is the radius index actually assigned to that read. For ordinary interior reads \(\nu=m\). The initial structure must satisfy the same envelope, or a separately specified envelope tending to zero.

**Outstanding — D for the actual domains.** SA 6141–6155 defines layer radii on represented domains; it does not verify (19) globally for every input of NL1 Theorem V′. ST1 records are frozen at birth (st1-r2 84–99). One must show that the actual roster supplies a current-scale bound at every read, including boundaries, outputs, drop-outs and the next fibre's longer sequence. A real reference passing formation tests does not prove this assertion for every complex input. Replacing the domain by its intersection with (19) changes the consumer hypothesis; it requires checking coverage of its actual substitutions and integrals.

SA also assigns level-one radii to layer zero, level-\(t-1\) radii to an unfinished top, and separate initial radii (6145–6148). The draft omitted these exceptions. If \(|\nu-m|\le1\), bounded adjacent frame increments give \(\theta_m\le2\theta_\nu\) for sufficiently small \(\gamma\), hence \(\log\theta_m\le2\log\theta_\nu\); one may use \(C_\lambda'=2^{2r_R}C_\lambda\). This repairs the envelope **once the actual index and read coverage are supplied**. No general preservation under shifts is inferred solely from \(q>p_0\); it also needs the response and gap budgets.

**Lemma 5 (geometry transfer).** G and the floors on \(M\) imply (1). Intersecting two sequences satisfying (1), on aligned common refinements, preserves the smaller strict separation floor.

*Proof.* An \(M\)-cube is a union of \((M/M_1)^4\) \(M_1\)-cubes. Both gap bounds in G are at least \(2\rho\xi_j>\rho\xi_j\). For a meet \(C_j=A_j\cap B_j\), a point of \(C_{j+1}\) belongs to both inner members and
\(C_j^c=A_j^c\cup B_j^c\). Its distance from this union is the smaller of the two distances. Cube membership follows from the common refinement. This proves the implication; it does not prove G. ∎

**Lemma 6 (real cube admission).** Assume G, B and Q. Put
\[
 v=C_{\rm RA}C_\lambda A_0
          \sup_m\theta_m^{-1/2}(\log\theta_m)^{p_0+2r_R},\qquad
 C_G=8L^4B_*(c_gM_1+2L).                                        \tag{20}
\]
If
\[
 2L^6(c_gM_1/L+2)v<c_{\rm rg},\qquad L^3v\le1/8,                 \tag{21}
\]
then \(U\) has real bound \(C_Gv\).

*Proof.* Curvature follows directly from (17), since every inner plaquette is a complete curvature read. Consider a gauge cube \(Z\subset\mathcal L_j\cup\mathcal L_{j+1}\).

For \(j\ge1\), work in level-\((j+1)\) units and write the bare mesh there as \(\eta'\). The cube side satisfies \(s\le c_gM_1/L\). Its three-unit enlargement, with two extra bare meshes, lies inside \(\Omega_{j-1}\), because
\(\rho/L^2\ge3+2/L^2\) and \(\eta'\le L^{-2}\).
All current stencils there are complete and their scales are at least \(L^{-2}\). Hence
\[
 |\partial U-I|\le L^4v\,\eta'^2,\qquad |J^\circ_{\eta'}|\le L^6v.
\]
For unitary \(P\), the difference between \(P-I\) and its skew-Hermitian part is
\(-\frac12(P-I)^*(P-I)\). Apply this at the six incident plaquettes, with unitary transports, in the Wilson-current normalization. It gives the ST1 conversion
\[
 |D_U^{\mathsf T}\partial U|
 \le\eta'^2|J^\circ_{\eta'}|+6\eta'^{-1}\sup|\partial U-I|^2.
\]
With \(w=L^2v\), this is
\(\le\eta'^2 L^4w(1+6w\eta')<2L^4w\eta'^2\);
indeed \(w\eta'\le L^2v\le1/(8L)<1/6\).
Use (18) with \(w'=Lw=L^3v\). Its smallness condition follows from (21), with room also for strict curvature bounds. The resulting gauge has
\[
 |A|,|\nabla A|<4L^6B_*(c_gM_1/L+2)v
\]
in these units. Conversion to scale \(\xi_j\) costs respectively \(L^{-1}\) and \(L^{-2}\). Both normalized bounds are at most \(C_Gv/2\).

For \(j=0\), \(Z\) has at most \(n\le c_gM_1\) bare intervals along a side. Use coordinate-ordered tree gauge from a corner. Moving a non-tree link through each of the other three coordinate segments expresses it as a product of at most \(3n\) transported plaquettes. All lie in \(Z\). Unitarity and telescoping give \(|U^g(b)-I|\le3nv\). This is less than \(2\) by (21). For the principal \(SU(2)\) logarithm, \(2|\sin(\vartheta/2)|\ge2|\vartheta|/\pi\) for \(|\vartheta|\le\pi\). Therefore
\[
 \eta|A|\le(3\pi/2)nv,\qquad
 \eta^2|\nabla A|\le2\sup\eta|A|\le3\pi nv\le C_Gv.
\]
The last inequality uses \(B_*\ge1,L\ge27\). The cube gauges are existential and curvature is gauge invariant, so this proves the real-bound assertion in the already fixed step representative. ∎

**Lemma 7 (uniform smallness).** For any fixed \(Q\ge0\), if
\(0<\gamma<\min(1,e^{-Q})\), then
\[
 \sup_{t\ge\gamma^{-2}}t^{-1/2}(\log t)^Q
       \le\gamma(2\log\gamma^{-1})^Q=:F_Q(\gamma)\longrightarrow0.
                                                                    \tag{22}
\]
Under D, \(r(P)\le D_cF_{q+2r_R}(\gamma)\), where
\(D_c=(1+\beta_s)C_\lambda'\max(C_0,C_1)\).

*Proof.* The derivative of \(t^{-1/2}(\log t)^Q\) has the sign of \(Q-\frac12\log t\) for \(t>1\). It is nonpositive on the indicated interval. For the limit put \(u=\log\gamma^{-1}\) and choose an integer \(n>Q\). The exponential series gives \(e^u\ge u^n/n!\), so \(e^{-u}(2u)^Q\le2^Q n!u^{Q-n}\to0\). Substitute (19) and take the supremum for the last assertion. The same argument applies to (20). ∎

**Theorem 8 (conditional transfer to stage pairs).** Assume R, W, G, B, Q and D uniformly for every structure and every history under consideration, with constants chosen in §2. Then there is a common \(\gamma_{\rm PR}>0\) such that for \(0<\gamma\le\gamma_{\rm PR}\), every specified consumer pair and its real reference satisfy (15). If F is also supplied, (16) holds.

More precisely, choose \(\gamma_{\rm PR}\) below all imported coupling ceilings, including \(\gamma_B(M)\) at outputs, so that (21) holds and
\[
 C_G C_{\rm RA}C_\lambda A_0F_{p_0+2r_R}(\gamma)<h/2,\qquad
 D_cF_{q+2r_R}(\gamma)<r_* .                                      \tag{23}
\]
Include the initial envelope if it is specified separately. The ceiling may depend on \(M,\bar\kappa\) and the late amplitudes. None of the constants in (15)–(16) does.

*Proof.* Lemma 7 permits every strict inequality in (23) and (21) simultaneously below one positive ceiling. Imported ceilings are assumed common over the quantified histories. Lemma 5 gives the geometric class; Lemma 6 gives the real bound; (19) and Lemma 7 give \(r(P)<r_*\). Apply Theorem 3, and Lemma 4 when required. At \(P_0\) the complex size is zero. The same argument applies to a stage cut at its own depth, provided G, B and D hold for that cut; a compression then retains the estimates. ∎

**Outstanding — the actual Gaussian comparison.** Theorem 8 supplies the precision hypotheses of frozen IN1 Lemma 2. It does not supply IN1's H-M: that includes the actual collared matrices, their enlarged parameter discs, heredity, wall factorization and physical identification. IN1 108 and its discussion after Lemma 2 explicitly retain that distinction. Consequently the precision part of NL1's (CI-form)(ii) follows conditionally here; its separate Gaussian-comparison part and CI itself do not. Frozen TP1's REG/G-ID and extraction imports are unchanged.

The theorem reads one nest at a time, so it requires no comparison with an inherited tower's scale. This explains why layered-a3 (3) is not an extra loss in (15). It does not prove that actual domain admission or the tower bounds of PR1(5b) can be bypassed.

## 5. Source checks and the draft's proposed corrections

Each external line range quoted or used by the pass-1 argument was checked in the pinned raw text, after the relevant sa-index rows and neighbours. The three raw files were fetched once. Only bounded excerpts were read. CA-II and CA-III are not cited by that draft and supply no input here. Source hashes and excerpt records are in /tmp/pr-lay-pass2; this manuscript states the conclusions needed to read it without those scratch records.

| Checked source lines | Finding |
|---|---|
| [SA](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) 5696–5718; 6026–6038; 6141–6155 | Confirms tower clauses, running radii and lifted structure spaces. The latter specify radius-index exceptions and a separate base structure. They do not verify D for the local chain domains in this checkout. |
| SA 9793–9802; 10113–10210; 10242–10263; 10307 | Confirms the noncritical regular-pair class, bilinear conventions, separate averages and operator formulas. The ceiling is stated independent of \(M_1\). Torus floors and the distinction between a local class on \(X\cap\Omega_1\) and a global class must be retained. The global propagator claim is a sketched input here. |
| SA 10604–10635; 10828–10937 | PX1/PX4 give the metric and layer barrier. PX54–PX68 contain a conditional derivation of complex transport/site bounds. PX58 already uses the admitted directional Cauchy method. The new use here is its application to precision entries under W, not invention of that method. |
| SA 11204–11255; 11313–11347 | Confirms the pivot chain rule, active/current distinctions and gauge-gradient term. PX115 defines the plaquette curl; PX117 is exactly the prefix identity used in Lemma 2. |
| SA 14091–14205 | Confirms the short precision and sketches its comparison. The independent inverse-root decoupling and collar geometry are additional requirements. These lines do not identify arbitrary path-weighted matrices with the actual localized Gaussian. |
| SA 17398–17407; 17578–17592; 17618–17630; 19485–19495 | Confirms the stated one-later-\(M\)-cube gaps, prepared shell construction, tests, overlap lifts and final coupling-ceiling order. The waiting depth is explicitly defined at 6035; citing only 17585 for that definition is imprecise. These are not proofs of the global input-domain coverage claimed in the draft. |
| [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex) 45439–45521; 46035–46085 | Confirms the three real gauge clauses, weighted radii, conditional operator statement and complex gap. Its class is not silently identified with (1)–(4), and its theorem is not used as an additional proof here. |
| CA-I 49495–49546 | Confirms application-side inclusion and drop-out-space obligations. The draft's 49495–49502 pinpoint does not reach the later-drop-out discussion; that starts at 49531. This scope restriction does not assert that CA-I lacks the proof of its conditional operator theorem. |
| [YM3-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex) 53308–53327 | Confirms the meet construction and its smaller-gap argument. It supplies no four-dimensional stage-admission theorem. The unused claim that YM3 has no analogue of R is removed; absence of a search term would not establish that claim. |

The draft's recommendations about other notes have the following dispositions. **None of those files is edited.**

| Recommendation or scope correction | Disposition |
|---|---|
| Split assembly PR1(5) into precision (5a) and tower comparison (5b). | **Right as a distinction of statements.** Assembly 187 is layered-a3 (1), consumed by stage-resp. Theorem 3 is (5a)'s conditional operator result; Theorem 8 still needs actual admission. Calling all of (5a) closed would be premature. |
| Replace IN1's layered “open” entry by a proved consumer theorem, and repair its identification with assembly PR1(5). | **The identification correction is right; the closure recommendation is not justified.** The old in1-draft 800 conflates different statements, although 807 already distinguishes them. Frozen in1.md is the operative text and retains H-M and formation obligations. |
| Remove PR-lay as NL1's first missing input and merely add I-G to its domain definition. | **Not justified.** D requires an actual coverage/admission proof or an explicit consumer change with its consequences checked. The additional Gaussian part of (CI-form)(ii) also remains. |
| Declare OS (F-4) satisfied. | **Only its requested theorem form is supplied.** Larger strict gaps define subclasses, so Theorem 3 has the floor property. os-draft Theorem 3.1 still requires its regularity/domain hypotheses; sequence separation alone does not admit a field. |
| P82 is already layered and is not itself a theorem for \(A\). | **Right.** Frozen P82 Theorem P treats the real constrained inverse \(S_q^\circ\). Its complex independent-current extension is not supplied by this distillation. The proposed fallback route is unproved and is omitted. |
| a3-close 99 concerns only towers and is irrelevant to every admission issue here. | **Too broad.** Its open item is layered hereditary-core admission, including simple conditions along actual substitutions. Theorem 3 does not consume that theorem, but this does not remove D for those actual substitutions. |

## 6. Definitions supplied in this distillation

The supplied or sharpened definitions are: (i) the longer class versus the depth-\(k\) metric, including the next region; (ii) free scalar coordinates, norms and compression space; (iii) complete stencils, largest-scale seam readings and the auxiliary stencil size \(s(P)\); (iv) witnessed real bound \(r_0\), with no assumed minimizer; (v) the fixed real axial representative; (vi) active-row injection and the ambient/free constraint forms (8); (vii) the full global domain input D with its actual radius index and base-structure clause; and (viii) the distinction between field size \(r(P)\) and entropy parameter \(\kappa\). D is an exposed hypothesis, not a definition silently imposed on the existing consumers.

## 7. Result

**Proved here:** Theorem 3 gives symmetry, a uniform precision gap, exponential entry decay and an exponentially decaying perturbation linear in the complex pair size. It assumes R and W on the stated regular class. Lemma 4 adds the completed gauge form under F. Lemmas 5–7 and Theorem 8 give a conditional admission route under G, B, Q and D. Every precision-estimate constant precedes \(\kappa\) and is independent of \(M,\bar\kappa\); late quantities enter only the coupling ceiling. The useful additional deduction from the walk package is the entrywise Lipschitz estimate.

**Imports retained:** the real layered gap and its flat/coefficient inputs; the repaired complex walk package, including its all-scale second-jet and cut-down uniformity premises; optionally the finite gauge correction; actual sequence geometry; the tested critical-background/profile and output packages; the local gauge theorem conditional on F0; running/lift envelopes; and the still **Outstanding** global current-layer admission D. The actual Gaussian H-M interface and tower comparison PR1(5b) remain separate.

**Corrections made to pass 1:**

1. Replaced the asserted complete consumer closure by the explicit conditional admission theorem. Formation at a real reference, record retention and well-definedness do not establish D for all complex inputs. Restored boundary/top radius conventions and the initial envelope.
2. Used frozen IN1, P82 and TP1. Removed the inference from precision estimates to the full actual Gaussian comparison and the proposed downstream status promotions.
3. Distinguished the longer regularity sequence from the cut metric. Made stencil conversions explicit, inserting the harmless \(L^2\) factor in \(H_1\) and its smallness ceiling.
4. Fixed operator typing: active injections, ambient versus already-free constraint forms, the prescribed axial reference and the extra full-form ceiling missing from draft Theorem B.
5. Removed the defective alternate symmetry proof. With the draft's \(P_{z,w}\), the desired point is \((1,i)\), not \((1,1)\); moreover that proof's \(R>2\) hypothesis was absent from its stated proposition. The algebraic proof suffices.
6. Specified torus room, complete gauge buffers, witnessing gauges and the compression subspace. Kept the bare-layer tree-gauge argument and the enlarged-cube/current estimates explicitly.
7. Retained every material qualification of the imported checks, especially W's coefficient premise and prior complex inverse package. No independent proof of that package or of the proposed P82 fallback is claimed.
8. Corrected the constant-table placement and source pinpoints. Qualified the draft's a3-close claim, removed its unsupported YM3 absence claim, and removed duplicate summaries, tests and unused two-pair comparisons.

This is a distillation and conditional proof of the precision comparison step sketched in the sources, not a proof of actual four-dimensional stage-domain admission or Yang–Mills existence. No computer-assisted step discharges any claim. **This text is not yet refereed.**
