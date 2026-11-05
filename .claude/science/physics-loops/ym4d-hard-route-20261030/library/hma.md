# HM-A: the Gaussian family for the relative Y3 gauge form

Provenance: Codex, pass 2 (distil), checkout ba43ce7ef; research text, not an audit; grants no status. Based on Claude's hma-draft.md. Not yet refereed.

Credit: the regular-pair operators, relative gauge quadratic form, collared Gaussian and UM method come from **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, revision `31a47c543775`. SA denotes their `YM4_sketch_500.tex`, CA-I/II/III their complete account, and Y3 `YM3/YM3_I.tex`. The background and walk methods come through the library from **Tadeusz Bałaban** and **Jonathan Dimock**. Library imports retain their stated premises. All arguments below are by hand.

This note addresses assembly-status critical-path item 6. It proves conditional matrix, formation, determinant and physical-Hessian statements. It does **not** identify a changed stored gauge factor with the old one. That obstruction is stated where the formation theorem uses it.

## 1. Definitions and imports

**D1 (geometry and domain).** Use frozen [hm](hm.md) §1 and [descent](descent.md) (1)–(2): odd \(L\ge27\), \(L>L_0^\natural\), depth \(k\), mesh \(\eta=L^{-k}\), scales \(\xi_j=L^{j-k}\), and one fixed admitted separated longer sequence \(\mathbf S=(\Omega_0,\ldots,\Omega_{k+1})\). Its operator sequence stops at \(k\); its separation is \(R_1M_1\). Keep its boundary spaces, inner plaquettes, omitted inward rows, active mask, pivots, embedded read boxes and analytic branches fixed. Fine cubes have side \(M\), coarse cubes side \(\ell=LM\), in level-\(k\) units. Cubes have half-open site ownership; geometric contact and filing use their closed versions.

Let \(I\) be the positively stored nonpivot level-\(k\) bonds, with three colours per bond; there are at most \(n_c=12\) scalar coordinates per site. Bond vectors use the Euclidean colour norm. Transposes use the bilinear colour pairing \(\frac12\operatorname{tr}(XY)\); estimates use the Hermitian norm. Matrix entries below are \(3\times3\) bond blocks, with operator norm. Include all scalar/block conversions in the early walk constant, **before** choosing any contraction or radius.

A triple is \(P=(U,A',\mathbf J)\), with \(U\) real, \(\mathbf U=e^{i\eta A'}U\), pair \(\mathbf p(P)=(\mathbf U,\mathbf J)\), and \(P_0=(U,0,0)\). On every complete contained read, \(\mathrm{R4}(Y;a_0,a_1,j_0)\) requires
\[
 |\partial U-I|,|\partial\mathbf U-I|<a_0\eta^2,\quad
 |A'|,|\nabla^UA'|<a_1,\quad |\mathbf J|<j_0.                 \tag{1}
\]
Every contained eligible box of side at most \(C_{\rm box}LM\) must also have a real gauge with \(|A|,|\nabla A|<C_{\rm pot}Ma_0\). Derivative stencils and their margins are included. Put \(r_Y(P)=\max\{l|A'|,l^2|\nabla^UA'|,l^3|\mathbf J|\}\), with hm's largest-incident scale \(l\le L\). R5–R6 and admission of actual chain domains are additional conditions, not consequences of (1).

For active blocks with complete reads in \(Y\), **Rep** means \(c_b(\mathcal M^kU;x)=I\), where \(c_b(V;x)=V(y_b,x)\) is the averaged contour. It is a condition on **\(U\)**, not on \(\mathbf U\). A real gauge induces orthogonal bond blocks \(O_b=\operatorname{Ad}(g(b_-))\). R4 and \(r_Y\) are invariant under that action.

**D2 (nonlinear Y convention).** Put \(V=\mathcal M^k\mathbf U\) and
\[
 W^V_{b,x}(D)=c_b(e^{iD}V;x),\quad
 \widehat W^V_{b,x}(D)=W^V_{b,x}(D)W^V_{b,x}(0)^{-1},\quad
 \Phi^Y_V(D)=\sum_{b,x\ne y_b}[1-\tfrac12\operatorname{tr}\widehat W^V_{b,x}(D)]. \tag{2}
\]
The proposed new fluctuation factor is \(e^{-x\Phi^Y_V(D)}\), with relative indicator \(|\widehat W^V_{b,x}(D)-I|<\epsilon_j\). At a real axial **\(V\)** it is SA 7181–7182, including the same scalar normalizer; SA writes \(\Re\operatorname{tr}\) where this text writes \(\operatorname{tr}\), and at a complex axial \(V\) this factor is the holomorphic continuation of SA's. This definition is an adopted nonlinear extension of Y3's quadratic form; Y3 31522–31536 alone defines only that form. It does not instruct an owner to change already stored tests.

**D3 (pivot and candidate precision).** The actual plain constraint is
\[
 q_V(D)=i^{-1}\operatorname{Log}[\mathcal M(e^{iD}V)\mathcal M(V)^{-1}].
\]
Its pivot graph \(C_V(u)\) has nonpivot part \(u\), satisfies \(C_V(0)=0\), \(q_V(C_V(u))=0\), and has derivative \(\mathsf C_V\). Let \(h_V\) be the pivot-supported right inverse of \(q'_V(0)\). Define
\[
 E_{\rm amb}[j](D,E)=\langle h_V^{\mathsf T}j,q''_V(0)[D,E]\rangle,
\]
\[
 \mathsf A^Y(P)=\mathsf C_V^{\mathsf T}
 \left[\iota^{\mathsf T}\{(QG_1Q^{\mathsf T})^{-1}-\mathsf a\}\iota
       +\mathsf G^Y_V-E_{\rm amb}[\iota^{\mathsf T}H_1^{\mathsf T}\mathbf J]\right]\mathsf C_V,
 \qquad \mathsf G^Y_V=\operatorname{Hess}_0\Phi^Y_V.             \tag{3}
\]
Here \(\iota\) injects the active level-\(k\) rows. This is frozen PR-lay (6)–(8) with the Y gauge term; its identification as the physical Hessian is a theorem below, not part of this definition.

**Named imports.**

* **M:** frozen hm Lemmas 1–4, Theorem 5, Theorems 7–8 and Corollary 13.1, and frozen descent Lemmas 1, 2, 4 and Theorem B, with **R, W, AV, W-cov, PF** as stated in descent 60–66. Import their analytic, matrix and structural claims, **excluding the physical G-ID clause in both texts**. Thus retain the real gap, flat/curved/separation premises, local complex inverse and all-scale second-jet bounds, smooth two-difference cutoffs, repaired tree counts and zero-length multiplier reads, actual analytic means, common branches and fixed-region pair dependence. Include [h-walk-gate](../gates/h-walk-gate.md) §§5–8 and [a2-layers-gate](../gates/a2-layers-gate.md)'s stated repairs. Descent rebuilds the representative estimates for Y first; it does not substitute equality of the two forms at complex Rep triples. All constants are uniform in depth, volume, shape and larger admitted gaps.
* **PIV:** uniformly on the domains in use, \(C_V\) is holomorphic for \(|u|_\infty<\rho_p\), obeys \(|C_V(u)|_\infty\le C_p|u|_\infty\), has a fixed radius \(r_p\) for its free-variable and \(V\)-reads, and commutes with real gauge transport. The means obey a uniform bound \(|W^V(D)|,|W^V(0)^{-1}|\le G\) for \(|D|_\infty<\rho_a\), with early \(\rho_p,\rho_a>0\) and \(C_p,G\ge1\). These are nonlinear analytic-domain inputs. No frozen text supplies PIV; it is listed as **Outstanding** in the Result. (Its mean-bound part G is in descent Lemma 2's proof, from AV and Cauchy; the graph part should follow from the holomorphic implicit-function theorem, not yet written.) Covariance of the **linear** pivot derivative alone does not supply them.
* **FG/UM:** SA 13904–14089 and 14219–14249's finite-dimensional Gaussian comparison; UM's finite potential types, fixed real cutoffs, disjoint failed-bond blocks, carrier counts, rate conditions and finite interpolation/Mayer identities. The potentials must be supplied on their whole declared complex domains. The comparison and count implications are imported, not reproved here.
* **BG:** cp12 D1–D3, its P81/P82 hypotheses, and the repaired [a3-derivative](a3-derivative.md) §6 system, with [its gate](../gates/a3-derivative-gate.md) §§6.1, 7. Physical application also requires the actual background-branch match and next-constraint criticality specified in §5. Those are not matrix-envelope conclusions.
* **Q-real:** frozen PR-lay Q, including RCG4/F0, and cp12 Theorem 7 on every required enlarged box, only for Lemma 9 below.

## 2. The relative gauge and the assigned family

**Lemma 1 (meaning, uniqueness and zero gradient).** Under AV, at a real \(V\) let \(v(x)=c_b(V;x)\) in each active block, with \(v(y_b)=I\). Then \(V^v\) is axial and
\[
 \Phi^Y_V(D)=\mathrm{GF}(e^{iO(v)D}V^v).                       \tag{4}
\]
Among nonlinear families defined on these real gauge orbits, (2) is the unique family which equals the absolute soft-gauge function at every axial reference and is covariant under every real gauge. This uniqueness requires equality of the **whole functions**, not only their Hessians. Formula (4) continues holomorphically wherever both analytic branches exist in a common connected continuation domain.

At every real or complex reference,
\[
 \nabla\Phi^Y_V(0)=0,\qquad
 \mathsf G^Y_V(D,E)=\sum_{b,x}\langle\mathsf b_V(D)_{b,x},\mathsf b_V(E)_{b,x}\rangle,
 \quad \mathsf b_V(D)=i^{-1}\partial_t|_0\operatorname{Log}\widehat W^V(tD). \tag{5}
\]
Consequently the completed-form correction \(-E_{\rm free}[J_{\rm GF}]\) is zero, including after pivot substitution. The relative insertion uses the same scalar gauge normalizer at every real reference held fixed during its orbit integral.

*Proof.* Equivariance of the actual contour mean gives

\(c_b((e^{iD}V)^v;x)=v(y_b)c_b(e^{iD}V;x)v(x)^{-1}=\widehat W^V_{b,x}(D)\).

At zero it equals \(I\); the exponential chart transforms bondwise by \(O(v)\). This proves (4). Transport any other covariant family to \(V^v\) to prove uniqueness. The same algebra holds for complex \(v\) on common branches; alternatively apply the identity theorem from a real open set. It does not assert availability of an arbitrary new complex domain.

Write each relative contour as \(e^{iH(D)}\), \(H(0)=0\), \(\operatorname{tr}H=0\). Its trace has expansion \(2-\frac12\operatorname{tr}H(D)^2+O(D^3)\). Thus \(1-\frac12\operatorname{tr}e^{iH(D)}=\frac12\langle H(D),H(D)\rangle+O(D^3)\), proving (5). The chain rule for \(\Phi^Y_V\circ C_V\) has no \(C_V''\) contraction because its gradient is zero.

The relative insertion also uses SA's scalar normalizer at a non-axial real reference:
\[
 z_{\mathfrak G}(x,\epsilon)=\int_{SU(2)}
  1_{\{|h-I|<\epsilon\}}e^{-x(1-\frac12\operatorname{tr}h)}\,dh.
\]
Indeed, hold the reference contour \(W_0\) fixed and fix the gauge at block centres. An internal site gauge sends an actual contour \(W\) to \(Wv(x)^{-1}\). Haar invariance and inversion invariance transform the integral of its relative factor, whose argument is \(Wv(x)^{-1}W_0^{-1}\), into the displayed integral. The site gauges are independent, so the product of the normalized insertions has orbit average one. This real insertion identity does not replace a carried factor when a later reference changes; an analytic continuation retains its chosen scalar branch and formation hypotheses. ∎

**D4 (full-read assignment).** Adopt hm's fixed-region precision labels with the gauge labels replaced by (5). Their hulls contain all uncut read boxes, stencils, endpoints, joins, and zero-length multiplier reads. Pair transpose partners on a common hull and sum intermediate colours before assigning labels. Form hm Theorem 5's local grouped resolvent and root labels from these coefficients, with its endpoint balls and full product hulls. No local field is extended to a global field in this definition.

For selected fine support \(Z_0\), use hm's corner collar \(H=Z_0^\sharp\) and \(\chi=1_{I_0}\). A hull \(H_\alpha\) receives the tag \(\prod_{\Delta\cap H_\alpha\ne\varnothing}s_\Delta\). Set \(s=1\) on \(H\), zero off the coarse union \(Z\supset H\), and discard unreadable hulls **before** evaluation. The two separately tagged series give
\[
 C=(\chi\mathsf A^Y(s)\chi)^{-1},\quad
 \Gamma=-\chi\mathsf A^Y(s)(1-\chi)\mathsf r^Y(s),\quad
 D_\tau=\tau^{-1}(C+C\Gamma\Gamma^{\mathsf T}C).               \tag{6}
\]
The root series \(\mathsf r^Y(s)\) is not defined as \(\mathsf A^Y(s)^{-1/2}\). Define \(\mathcal J[F]\), for FG's permitted integrands, by the normalized Gaussian with covariance \(D_\tau\) on the fixed real \(I_0\)-space, using the determinant branch from its positive reference. Empty dimension means evaluation at the empty vector. This is the carrier assignment used in the statements below; the Y choice alone does not select a decoupling expansion.

**Theorem 2 (a: carrier identification and early envelope).** Assume M and FG, and adopt D4 for the actual local Gaussian construction. Take exactly descent (5)–(8)'s constants and radii, with all hm (23) floors. Then at every \(P\in\mathrm{R4}(Z;a_0,a_1,j_0)\), on independent discs \(|s_\Delta|<e^{\bar\kappa}\), \(C=C^{\mathsf T}\), \(\Gamma\) is rectangular, and the real references from \(P_0,s=1_H\) satisfy \(C_*>0\) and
\[
 \|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0,\qquad
 \|\tau^{-1}C-C_*\|+\|\tau^{1/2}\Gamma-\Gamma_*\|
 \le\varepsilon:=H_0\{e^{32\bar\kappa-dM}+L^3(a_0+a_1+j_0)\}+C_\tau|\tau-1|,
 \quad d=\theta/4.                                           \tag{7}
\]
The positive constants \(K_0,H_0,d,C_\tau\) precede \(\kappa\), independently of \(M,\bar\kappa\). The functional is normalized, hereditary for these full reads, wall-factorizing, holomorphic at fixed real \(U\), real at real parameters, pair-dependent and real-gauge covariant. At fixed geometry its kernel, and its integrals of jointly Borel permitted integrands, are jointly Borel in the admitted real data. Its scalar local dimension is at most \(12(LM)^4\#Z\); hm (29)'s finite interpolation identity holds.

*Proof.* Each fixed-region coefficient and its full hull depends only on the pair and the fixed geometric record, by descent Lemma 4. Grouping, transposition and tagging preserve that property. That lemma reruns hm's local bounds for the Y coefficients. Descent Lemma 1 transports every R4 triple to a representative with the same radii; its real orthogonal conjugation transports the rerun bounds back. Descent Theorem B therefore gives (7), normal convergence, the structural assertions and the dimension count. No equality with the absolute complex precision is used. Restriction sets missing-hull tags to zero; wall separation kills every connecting hull. On each common branch chart the means, finite matrices and their inverses depend continuously on the real data; their normally convergent labelled sums are Borel. Fixed Borel cutoffs and FG domination preserve that property under integration. Normalization and interpolation are hm Theorem 8 applied to (6). ∎

For **this assignment**, (7) supplies IN1 H-M's matrix clauses with \(b=32,H_p=L^3\). Here IN1 H-M's datum \((C,\Gamma)\) is read as the rescaled pair \((\tau^{-1}C,\tau^{1/2}\Gamma)\), with covariance \(D_\tau\) (SA 14243–14247); with that reading (7) is exactly IN1 (9). Frozen descent (15) carries the same reading. Together with Theorem 4 it supplies the comparison read by TD J and NL1-L Theorem 7's CI-Gauss, once their entire domains are admitted. The Gaussian structural clauses of ci-form H-S hold at the fixed geometric record. To supply ci-form H-G's additional limit (4), its whole domain must have bounds \(a_i(\gamma),j_0(\gamma)\to0\) and \(\sup|\tau-1|\to0\); then \(\Delta_\gamma=H_0L^3(a_0+a_1+j_0)+C_\tau\sup|\tau-1|\to0\). Fixed absolute ceilings alone do not imply this limit. **Outstanding (DOM/formation match):** no theorem here places every CI or ST1 domain in R4, supplies that whole-domain shrinking, or identifies an independently chosen family of old activities with D4. Physical identification is Theorem 8, not a premise hidden in Theorem 2.

## 3. Local formation and the UM budget

Use IN1's real frame \(\theta_j\), \(g_j=\theta_j^{-1/2}\), \(\delta_j=A_1g_j(\log\theta_j)^{p_0}\), \(\epsilon_j=(A_0/A_1)\delta_j\), and \(\tau=x_j/\theta_j\), \(|\tau-1|\le1/4\). **Fix \(b=\sqrt{\theta_j}u\)** as the real integration coordinate even when \(x_j\) is complex. The box is the product of bond balls \(|b(\beta)|<\mathfrak b_j:=\sqrt{\theta_j}\delta_j\); its cutoffs remain fixed while analytic parameters vary. Using \(\sqrt{x_j}u\) instead would move this real box.

For each gauge summand set \(h_{b,x}(u)=1-\frac12\operatorname{tr}\widehat W^V_{b,x}(C_V(u))\), and subtract its exact quadratic Taylor polynomial:
\[
 f_{b,x}(u)=h_{b,x}(u)-\tfrac12 h''_{b,x}(0)[u,u].             \tag{8}
\]
Let \(Y_{b,x}\) contain the complete free-variable **and external-pair** reads, including iterated averaging, pivot and joining reads. Choose a fixed rectangular hull for these reads and take all fine cubes meeting it. By PIV and AV its diameter has an early bound \(R_g\). Define
\[
 V_{\rm GF}(Y;P,b)=-x_j\sum_{Y_{b,x}=Y}f_{b,x}(b/\sqrt{\theta_j}). \tag{9}
\]
This supplies a gauge potential type. It differs from assigning only the fluctuation read to a carrier.

**Lemma 3 (b1: gauge formation).** Put \(\rho=\min(\rho_p,\rho_a/C_p)\), \(B=1+G^2\), and let \(N_o\) bound the number of gauge summands reading any one free bond. Assume \(M>R_g+2\), \(\delta_j\le\rho/2\), and \(A_0>2BA_1/\rho\). Then the relative indicator is one throughout each selected box, and (9) is hereditary on its complete reads, holomorphic there, real at real data and real-gauge invariant. It satisfies UM1 with
\[
 |V_{\rm GF}(Y;P,b)|\le a_{\rm GF}e^{-\lambda_Vd_f(Y)}
       \left(1+M^{-4}\sum_{\beta\subset Y}|b(\beta)|^2\right),\qquad
 a_{\rm GF}=4BN_o\rho^{-3}e^{32\lambda_V}M^4\delta_j.          \tag{10}
\]
At fixed later constants, \(\sup_{\theta_j\ge X_0}a_{\rm GF}\to0\) as \(X_0\to\infty\). In particular \(a_{\rm GF}\le W_0/4\) is a final coupling ceiling.

*Proof.* The matrix function \(\widehat W(C_V(u))-I\) is zero at zero and bounded by \(B\) on the radius-\(\rho\) ball. Apply scalar Schwarz to each norming linear functional along the complex line through \(u\). Its norm is at most \(B|u|_\infty/\rho<\epsilon_j/2\), proving the indicator assertion. This deletion is justified only on the selected small box; keep its cutoff.

Lemma 1 gives \(h(0)=h'(0)=0\). On a line \(u=t v\), \(|v|_\infty=1\), the Cauchy coefficient bound for \(|h|\le B\) gives
\[
 |f(u)|\le\sum_{n\ge3}B(|u|_\infty/\rho)^n
 \le2B\rho^{-3}\delta_j|u|_\infty^2.
\]
Since \(|x_j|/\theta_j\le5/4<2\), each term in (9) is bounded by \(4B\rho^{-3}\delta_j\sum_{\beta\text{ read}}|b(\beta)|^2\). Summing uses \(N_o\). The hull has width less than \(M\), so its cube rectangle has at most \(2^4=16\) cubes. A tree through their centres has fine-cube length at most 15, so \(e^{15\lambda_V}\) suffices (the text keeps the valid larger factor 32). This proves (10). Analyticity, reality and covariance follow termwise from AV, PIV and Lemma 1; the geometric reads do not vary with fields. Finally \(\delta_j=A_1e^{-t/2}t^{p_0}\) with \(t=\log\theta_j\). For \(t>2p_0\) it decreases to zero; the exponential series with any integer power greater than \(p_0\) proves that limit. ∎

On a declared **larger complex bond box** \(|b|_\infty<R_b\), the same proof gives (10) with \(\delta_j\) replaced by \(\delta_B=g_jR_b\le\rho/2\): substitute this upper bound for \(|u|_\infty\) in the displayed Cauchy sum. In particular ci-form's scalar polydisc \(R=(\log\theta_j)^q\) requires \(R_b=\sqrt3R\) and the ceiling on \(a_{\rm GF}\) with this \(\delta_B\). It still tends to zero since \(g_j(\log\theta_j)^q\to0\). This extension does not move the real cutoff or delete indicators outside it. If the actual real window has factor \(C_{\rm win}\), replace its cutoff by \(C_{\rm win}\delta_j\) and impose \(A_0>2BC_{\rm win}A_1/\rho\). These are later ceilings, not changes to early matrix constants.

**Theorem 4 (UM4–UM6, UM14 and cost at most one).** Assume Theorem 2, FG/UM and the actual fixed-cutoff/finite-type structure. Take \(P_d\ge1\) from UM9–UM13 at a fixed early fine-entropy gap, uniformly for all later larger rates. With \(A=A_{K_0}\), \(c_m=12\) and \(D_0=Ac_mL^4\), choose
\[
 W_0=\min\{[3P_dL^4(1+Ac_m)]^{-1},\zeta_0/(2P_d)\}          \tag{11}
\]
before \(\kappa\). After \(M\), set
\[
 \varepsilon_* =\min(\varepsilon_0,(3D_0M^4)^{-1}),\quad
 \gamma_t=\min(2/(3D_0M^4),\zeta_0),\quad \varepsilon\le\varepsilon_*.
                                                                    \tag{12}
\]
Then UM4–UM6 hold for D4, UM14 holds, and \(C_0^{\rm UM}\le1\). Explicitly, if a permitted integrand has
\[
 |F(b)|\le F_*e^{\zeta|b|^2}
          \prod_{\beta\in P_{\rm fail}}1_{\{|b(\beta)|\ge\mathfrak b_j\}},
 \qquad \zeta\ge0,\quad \zeta+\gamma_t/2\le\zeta_0,
\]
with distinct bond blocks \(P_{\rm fail}\subset I_0\), then
\[
 |\mathcal J[F]|\le F_*\exp\{A(\varepsilon+\zeta+\gamma_t/2)m
                       -\gamma_t\mathfrak b_j^2|P_{\rm fail}|/2\},
 \qquad m\le c_m(LM)^4\#Z. \qquad\text{(UM6)}
\]
There is no exterior-dimension factor. If the remaining actual potential types satisfy UM1 with total norm \(a_{\rm rest}\le W_0/4\), Lemma 3 and \(a_{\rm GF}\le W_0/4\) also supply the amplitude hypothesis of UM12–UM16.

Explicitly, UM6 bounds an integrand of modulus at most \(F_*e^{\rho_t|b|^2}\), with distinct failed bond blocks \(P_0\), by
\[
 F_*\exp\{A_{K_0}(\varepsilon+\rho_t+\gamma_t/2)m
                  -\gamma_t\mathfrak b^2\#P_0/2\},\qquad
 m\le c_m(LM)^4\#Z,
\]
where \(\rho_t+\gamma_t/2\le\zeta_0\) and \(\mathfrak b\) is the fixed real threshold. The same proof gives the bound for every tilt \(\gamma>0\) with \(\rho_t+\gamma/2\le\zeta_0\), as SA's UM6 states, and the integrals are jointly holomorphic in the stated parameters. (Here \(P_0\) denotes the failed bond blocks only, not the reference triple.) On the potential-coupling discs \(\rho_t=P_dW_0M^{-4}\). No auxiliary dimension enters this cost.

*Proof.* Theorem 2 supplies UM4–UM5. On the failed-test support, \(\sum_{\beta\in P_{\rm fail}}|b(\beta)|^2\ge\mathfrak b_j^2|P_{\rm fail}|\); an extra tilt \(\gamma_t/2\) in FG therefore gives UM6. The potential tilt satisfies \(P_dW_0M^{-4}+\gamma_t/2\le\zeta_0\), which is UM14. Directly,
\[
 C_0^{\rm UM}=P_dL^4W_0(1+Ac_m)+D_0M^4(\varepsilon+\gamma_t/2)
 \le\tfrac13+\tfrac13+\tfrac13=1.                            \tag{13}
\]
The first half of (7)'s error can meet \(\varepsilon_*/2\) by a later \(M\)-floor: \(e^{dM}\ge(dM)^5/5!\). The remaining half is a later radius/tube ceiling. Thus the bound one and \(W_0\) are early; the defect and tilt are late. The potential norms add to at most \(W_0/2\). The imported finite Mayer/cutoff identities and UM12–UM16 then apply, with their retained rate and failed-test conditions. This does not assert the stronger activity/logarithm smallness without its further amplitude ceiling. ∎

**Outstanding (actual formation and stored tests).** Draft Lemma 4.4 is too strong. The non-gauge primitive operator chain is unchanged, but a stored quadratic form is constructed from the precision and changes with it. Earlier activities cannot be declared unchanged on that basis. SA 17531 also explicitly retains a gauge factor in a stored operation; SA 17558 treats it as a function of stored variables, independent of the changing background. Lemma 3 proves no identity for such a factor outside its small box.

Indeed take a flat field \(V=I^g\), with \(g(y_b)=I\), \(g(x)=e^{it\sigma}\) at one internal noncentre site, and \(\sigma^2=I\), \(\operatorname{tr}\sigma=0\). All paths to that site have mean \(e^{-it\sigma}\). Thus at \(D=0\) the relative factor has exponent zero, whereas the corresponding absolute summand is \(1-\cos t>0\). The indicators differ when \(\epsilon_j<2\sin(t/2)\). Choose \(t>0\) inside the analytic branch and then this threshold. Flatness permits R4 with arbitrary positive radii. This proves a difference of functions, not an admitted-history counterexample. It also rules out the draft's blanket unchanged-test claim.

New approximate fluctuation tests have axial references (SA 17317; frozen ST1 r4 FC5). Carried gauge factors read stored \(V_j\) (SA 17709–17712), which need not be axial. SA 17346 separately sets a gauge factor to one where its contour mean is undefined; 17369 makes old indicators one only on specified new-test supports. A construction must retain the old factor in its stored coordinates or prove a change-of-variables identity transporting its measure and every test. **Gauge-factor coverage, FC-test and that actual formation match remain Outstanding.** Theorem 4's \(a_{\rm rest}\) and structural hypotheses retain this issue; it is not removed by proving the new gauge remainder cubic. Frozen DR (4)–(5) uses the primitive operators, without (3)'s soft-gauge Hessian, so its algebraic response definition is unaffected.

## 4. The vacuum determinant

**D5 (compressed vacuum assignment).** Fix a union \(S\) of free bond blocks which are actually integrated, and put \(A_S=\chi_S\mathsf A^Y\chi_S|_S\). For the full Gaussian take \(S=I\). For a conditional step take its integration region, keeping the exterior variables fixed. Membership in \(S\) is part of the fixed geometric record.

Use hm (12)–(17), with the Y labels and the bond-block convention of D1. Write \(\Lambda=\Lambda_{\rm res}\), \(p=p_{r_c}\), and decrease the rate to \(0<\theta\le1/2\). In the grouped polynomials compress to \(S\), and keep all intermediate bonds in \(S\):
\[
 N_t=\frac{\Lambda I-A_{S,<}}{\Lambda+t},\quad
 P_t=\frac1{\Lambda+t}\sum_{j=0}^{n-1}N_t^j,\quad
 Q_t=N_t^n,\quad K_t=Q_t-E_SP_t,\quad
 \mathcal R(t)=P_t\sum_{m\ge0}K_t^m.                         \tag{14}
\]
Here \(E_S\) is the long-label family; the two summands of \(K_t\) retain their separate labels. Separate the field-independent term \( (\Lambda+t)^{-1}I\) of \(P_t\). For every remaining closed labelled product \(\alpha:x\to x\), use its full hull \(H_\alpha\), additive tree length \(t_\alpha\), and define
\[
 n_\alpha=\int_0^\infty\mathcal R_\alpha(t)_{xx}\,dt,\qquad
 X_\alpha=\bigcup_{\Delta\cap H_\alpha\ne\varnothing}\Delta,\qquad
 \mathbf N_S(X;P)=\tfrac12\sum_{x,\alpha:X_\alpha=X}\operatorname{tr}n_\alpha(P). \tag{15}
\]
Evaluate a local term only when its complete hull is supplied. This definition includes the local \(S\)-mask; it makes no assertion comparing unrelated masks or determining sequences.

**Theorem 5 (b2: local determinant bound).** Under M and the working-domain ceilings of Theorem 2, the assignment (15) has the following properties.

1. At every complete admitted pair, with the continued logarithm from \(P_0\),
   \[
   -\tfrac12\log\det A_S=-\tfrac12|S|_{\rm scalar}\log\Lambda
                            +\sum_X\mathbf N_S(X;P).         \tag{16}
   \]
2. Each term is defined also at local pairs with its full reads, is hereditary for the fixed geometry, holomorphic at fixed real \(U\), real at real data, and real-gauge invariant.
3. The early rooted bounds are
   \[
   \sup_x\sum_{\alpha:x\to x}e^{\theta t_\alpha}|n_\alpha(P)|\le2p,\qquad
   \sup_x\sum_{\alpha:x\to x}e^{\theta t_\alpha}|n_\alpha(P)-n_\alpha(P_0)|
       \le4p\,r_Y(P)/r_{\rm loc},                            \tag{17}
   \]
   the second for \(r_Y(P)\le r_{\rm loc}/2\).
4. Put \(C_{\rm hull}=2(2\lceil R_*\rceil+5)^4\). If
   \[
   LM\ge\max(4\kappa C_{\rm hull}/\theta,32/\theta),          \tag{18}
   \]
   then, for every coarse cube \(\Delta\),
   \[
   \sum_{X\ni\Delta}e^{\kappa d_{k+1}(X)}|\mathbf N_S(X;P)|
       \le C_{\rm vac}(LM)^4,\qquad
   C_{\rm vac}=48n_cp\,e^{1/4+\theta R_*/2}.                  \tag{19}
   \]
   The difference from \(P_0\) has the same bound multiplied by \(2r_Y(P)/r_{\rm loc}\). All constants in (17)–(19), apart from the displayed \(M,\kappa\), precede \(\kappa\).

*Proof.* Off Rep: descent Lemma 4 reruns hm on \(\mathcal K\) for the Y labels, and descent Lemma 1 with Theorem B's conjugation carries each grouped entry by orthogonal bond blocks, preserving block norms, accretivity and traces of closed products; so hm's entry majorants hold at every complete admitted R4 pair. First check the construction for a compression. In hm's proof of (16), replace each coordinate ball by its intersection with \(S\). Its real-part lower bound \(a_s=c_L/2\) and upper bound \(W\) persist under compression. Every path of at most \(n\) short steps remains in that ball, and its full read margin remains in the hull. Thus the same entry majorants hold without a global extension of the local data. In block norm the coordinate count \(n_c=12\) is an upper bound; norm conversions were included before these constants were chosen.

Let \(s_t=\Lambda/(\Lambda+t)\). Keeping the first extra power of \(s_t\) in hm (16)–(17) gives
\[
 |P_t-(\Lambda+t)^{-1}I|_\theta\le p\Lambda/(\Lambda+t)^2,\quad
 |Q_t|_\theta\le s_t^n/4\le s_t/4,\quad
 |E_SP_t|_\theta\le s_t/4.
\]
These are absolute labelled Schur bounds, not estimates obtained after cancellation. Since \(|K_t|_\theta\le s_t/2\), the nonleading part of (14) has absolute moment at most \(2p\Lambda/(\Lambda+t)^2\). Its integral is \(2p\), proving (17)'s first bound and normal convergence. On the line \(P_z=(U,zA',z\mathbf J)\), the common working tube contains \(|z|<r_{\rm loc}/r_Y(P)\). Subtract each coefficient's value at zero and apply Schwarz to its twice-majorant. Summing proves the second bound.

On a complete pair \(A_S\) is accretive with gap at least \(5c_L/8\). Direct multiplication gives \((A_S+t)P_t=I-K_t\), so (14) sums to \((A_S+t)^{-1}\). For \(\Re z>0\), integration to \(T\) followed by \(T\to\infty\) proves
\[
 \operatorname{Log} z=\int_0^\infty[(1+t)^{-1}-(z+t)^{-1}]\,dt.            \tag{20}
\]
The integrand has bound \(|z-1|/[(1+t)(\Re z+t)]\), giving holomorphic continuation from positive real \(z\). Triangularizing the finite matrix shows \(\operatorname{tr}(A_S+t)^{-1}=\sum_i(\lambda_i+t)^{-1}\), including algebraic multiplicities. Hence its integrated trace is \(\sum_i\operatorname{Log}\lambda_i\), a holomorphic logarithm of \(\det A_S\), real at the positive reference. Separating \( (\Lambda+t)^{-1}I\) and using the integrable majorant proves (16). This is the continued determinant logarithm, not necessarily the principal logarithm of the scalar determinant.

Each coefficient reads its pair and fixed mask only on its hull. Products, integration and normal summation preserve this property. After intermediate colours are grouped, a closed product is conjugated by the root's orthogonal block; its trace is invariant. This proves assertion 2.

For the length estimate use **unit cells in level-\(k\) units**, not bare sites of spacing \(\eta\). The latter would introduce a false factor \(\eta^{-4}\). A tour of a length-\(t_\alpha\) tree has length \(2t_\alpha\). At most \(2t_\alpha+2\) unit-spaced samples cover it within distance one. The unit cells meeting \(H_\alpha\subset N_{R_*}(T)\) therefore number at most \(C_{\rm hull}(1+t_\alpha)\). Include every incident unit cell at boundaries. They form a face-connected set, since the full hull contains its joining paths. Each lies in its owning coarse cube, as the grids align, and every filed closed coarse cube owns a cell meeting the hull. A tree through their centres lies in \(X_\alpha\), meets every coarse cube of that set, and has length at most their number. Thus
\[
 \kappa d_{k+1}(X_\alpha)\le\frac{\kappa C_{\rm hull}}{LM}(1+t_\alpha)
                                      \le\theta(1+t_\alpha)/4.
\]
This argument works on the periodic grid as well. A term whose hull meets \(\Delta\) has \(\operatorname{dist}(x,\Delta)\le t_\alpha+R_*\). Spend half the remaining moment on this distance. Since \(|\operatorname{tr}n|\le3|n|\), (17) bounds the sum in (19) by
\[
 3p e^{\theta/4+\theta R_*/2}
       \sum_xe^{-\theta\operatorname{dist}(x,\Delta)/2}.
\]
Use the \(\ell^\infty\) distance inherited from hm. If \(d_\nu\) is the coordinate distance to the cube, then \(\operatorname{dist}_\infty=\max_\nu d_\nu\ge\frac14\sum_\nu d_\nu\). Consequently the last sum is at most
\[
 n_c\prod_{\nu=1}^4\left(LM+1+2\sum_{m\ge1}e^{-\theta m/8}\right)
 \le n_c(LM+1+16/\theta)^4\le16n_c(LM)^4
\]
under (18). This repairs the draft's use of an \(\ell^1\) product bound at an \(\ell^\infty\) distance, at the price of the larger harmless \(32/\theta\) floor. It proves (19), including the difference bound. ∎

For a real Gaussian with exterior block \(T=I\setminus S\), completing the square gives
\[
 \int e^{-\frac12(b_S^{\mathsf T}A_Sb_S+2b_S^{\mathsf T}A_{ST}b_T+b_T^{\mathsf T}A_{TT}b_T)}db_S
 =(2\pi)^{|S|_{\rm scalar}/2}(\det A_S)^{-1/2}
 e^{-\frac12b_T^{\mathsf T}(A_{TT}-A_{TS}A_S^{-1}A_{ST})b_T}. \tag{21}
\]
The translation \(b_S\mapsto b_S+A_S^{-1}A_{ST}b_T\) proves it; the admitted holomorphic Gaussian continuation gives the complex version. Thus (16) supplies the determinant part of the **conditional** normalizer as well as the full one. A ratio \(\tau\) adds \(-|S|_{\rm scalar}\operatorname{Log}\tau/2\), assigned per integrated coordinate; \(u\mapsto b\) adds the corresponding fixed \(\theta_j\) scalar factor.

SA 17528–17545 uses the compressed determinant in (21), together with elimination factors \(z^{(j)}\). The draft's assertion that the full-space determinant is the only step normalizer is therefore incorrect. The extensive bound (19) can enter IN1 row 7 after \(M\); floor (18) is compatible with row 5, which follows \(\kappa\). **Outstanding (full vacuum interface):** this determinant theorem does not prove the \(z^{(j)}\) bounds, identify all class/boundary assignments across changing geometric records, or supply H-OL's companion and coefficient readout. Nor does its fixed-\(U\) difference estimate compare a curved real reference with the flat reference. Those extra identifications cannot be obtained by calling the remaining reference term a number.

## 5. The physical Gaussian clause

**D6 (physical hypotheses and Gaussian part).** A complete physical pair has \(\Omega_0\) equal to the torus, the real regular background \(U_+\), physical inner-action current \(J=F'(0)\), and every read required for the full free space \(I\). Here \(F(a)=\mathcal A(e^{i\eta a}U_+)\), with the invariant inner-plaquette action and the boundary spaces of BG. Initially use \(P_W=(U_+,0,J)\). The following hypotheses specify the physical application.

* **PH1:** BG holds at \(U_+\), with a common P81 chart \(\Phi_{\rm ch}(B)\), raw straightened \(q\), \(K=q'(0)\), multiplier \(\lambda_0\), and the repaired Landau identities of a3-derivative (37). All inverses used below, including \(G_1\) and \(QG_1Q^{\mathsf T}\), exist at this same pair.
* **PH2:** \(U_+\) is critical for the actual next constraint, including the stored unchanged rows. Varying \(V=\mathcal M^kU_+\) on the fibre \(q_V(C_V(u))=0\), with those rows fixed, preserves that next constraint. PIV holds on the common neighbourhood.
* **PH3 (actual branch match):** on that neighbourhood, the step's \(U_k(e^{iC_V(u)}V)\) has the same regular critical orbit as \(\Phi_{\rm ch}(\iota C_V(u))\), and at zero that orbit is \(U_+\)'s. The match persists under real gauge transport. Frozen ST1 r4 Lemma 5 can supply it with its **A1/F0/REG uniqueness, restriction, admission and CV premises**; the existence of a chart named in cp12 D3 alone is insufficient.
* **PH4 (normalization and active datum):** BG and PR-lay use the same actual straightened row map \(q(a)=\mathsf m(Qa+C^{(2)}(a)+O(a^3))\), including its outward factors and second jet. Fine pairing is \(\eta^4\), rows use counting pairing, \(\mathsf m(c)=\xi_c\), and \(\mathsf m\iota=\iota\). The active injection varies only the highest level \(k\), keeping finer rows fixed. The actual pivot graph is retained.

The **Gaussian part** is the quadratic Taylor term at \(u=0\) of
\[
 -x_j\psi(u),\qquad
 \psi(u)=\mathcal A(U_k(e^{iC_V(u)}V))+\Phi^Y_V(C_V(u)).       \tag{22}
\]
Jacobians, older activities, profile differences and remaining exponents are potentials; they are not included in this definition. At \(\tau=1\) the normalized coordinate is \(b=\sqrt{\theta_j}u\). This definition does not claim that the full nonlinear fluctuation law is Gaussian.

**Lemma 6 (six-term gauge identity).** At a physical reference, for gauge directions in BG's admitted site space, use \(\chi^+(b)=\operatorname{Ad}(U_+(b))\chi(b_+)\) and define
\[
 \lambda_A=G'RD^{\mathsf T}A,\quad \lambda_A^+(b)=\operatorname{Ad}(U_+(b))\lambda_A(b_+),\quad
 \mathsf S=I-DG'RD^{\mathsf T},\quad
 \Pi_J(\chi,C)=\tfrac12\langle i[\chi,C]-i[C,\chi^+],J\rangle_{\rm f}.
\]
SA 10172–10185's explicit six-term form obeys
\[
 \Delta'_\pi[J](A,C)=\Pi_J(\lambda_A,C)+\Pi_J(\lambda_C,A)
 -\tfrac12\{\Pi_J(\lambda_A,D\lambda_C)+\Pi_J(\lambda_C,D\lambda_A)\}. \tag{23}
\]
For \(J=F'(0)\),
\[
 \Pi_J(\chi,C)=\Delta^W(C,D\chi),\qquad
 \Delta^W-\Delta'_\pi[J]=\mathsf S^{\mathsf T}\Delta^W\mathsf S. \tag{24}
\]

*Proof.* The first two terms of (23) are the first four terms in SA's display. Since \(\lambda^+=\lambda+\eta D\lambda\), the sum of its last two \(\Pi\)'s is
\(\langle i[\lambda_A,D\lambda_C]+i[\lambda_C,D\lambda_A],J\rangle_{\rm f}\).
The two additional \(\eta[D\lambda_A,D\lambda_C]\) terms cancel by antisymmetry. This gives exactly the two remaining terms with their coefficient \(-1/2\).

For the physical identity, a bond transforms as
\(e^{it\chi}e^{i\eta A}e^{-it\chi^+}U_+\).
Expanding the exponential/logarithm to first order in \(A\) and \(t\) gives its chart generator
\[
 X_\chi(A)=-D\chi-\tfrac i2[A,\chi+\chi^+]+O(A^2),\qquad
 DX_\chi(0)[C]=\tfrac12(i[\chi,C]-i[C,\chi^+]).
\]
For completeness, the coefficient of \(t\), to first order in \(Y\), in \(\log(e^{tX}e^Ye^{tZ})\) is \(X+Z-\frac12[Y,X]+\frac12[Y,Z]\). Substituting \(X=i\chi,Y=i\eta A,Z=-i\chi^+\) and dividing by \(i\eta\) gives the displayed sign and coefficient. Differentiate \(\langle F'(A),X_\chi(A)\rangle=0\), the infinitesimal invariance of the inner action, in direction \(C\). Since \(X_\chi(0)=-D\chi\), it gives the first equality in (24). Expanding \(\Delta^W(A-D\lambda_A,C-D\lambda_C)\), its last term equals each of \(\Pi_J(\lambda_A,D\lambda_C)\) and \(\Pi_J(\lambda_C,D\lambda_A)\). Comparing their half-sum with (23) proves the second equality. ∎

**Lemma 7 (slice, active datum and multiplier Hessian).** Under PH1 and PH4,
\[
 KD\chi=0\quad(Q'\chi=0),\qquad K\mathsf S=K,\qquad
 RD^{\mathsf T}\mathsf S=0.                                 \tag{25}
\]
Put \(L_0=F''(0)-(DK[\,\cdot\,])^{\mathsf T}\lambda_0\). For the **active** value function
\[
 \Phi_{\rm act}(B)=\mathcal A(\Phi_{\rm ch}(\iota B)),
\]
one has
\[
 \Phi'_{\rm act}(0)=\iota^{\mathsf T}\lambda_0,\qquad
 \Phi''_{\rm act}(0)=\iota^{\mathsf T}[(QG_1Q^{\mathsf T})^{-1}-\mathsf a]\iota. \tag{26}
\]

*Proof.* The repaired node identity is
\(m(a)(c)=v[a](c_-)e^{i\widetilde q(a)(c)}V_0(c)v[a](c_+)^{-1}\), with \(D\widetilde q_0=\mathcal T_0K\) and invertible triangular \(\mathcal T_0\). Along the pure gauge \(U_+^{e^{it\chi}}\), a3-derivative Lemma 6.1 gives \(\dot v(y)=i(\chi(y)-Q'\chi(y))\). Comparing derivatives of the node identity with direct covariance of \(m\), when \(Q'\chi=0\), gives \(D\widetilde q_0D\chi=0\). Invert \(\mathcal T_0\) to prove the first statement. This kernel statement is sufficient; it is not an identification of every raw outward row with SA's differently normalized \(QD=\bar DQ'\).

The explicit projection formula gives \(Q'G'R=0\), so \(KDG'R=0\) and \(K\mathsf S=K\). With \(\Delta=D^{\mathsf T}D\),
\(\Delta G'=I-Q'^{\mathsf T}a_{\rm top}Q'G'\), where \(a_{\rm top}\) is the imported site mass, implies \(R\Delta G'R=R^2=R\). Therefore \(RD^{\mathsf T}\mathsf S=0\); also \(\mathsf S h=h\) whenever \(RD^{\mathsf T}h=0\).

The reduced datum is exactly \(\mathsf b(\iota B)=\iota B\). Interior rows are relative logarithms; each outward endpoint correction reads only immediately finer interior data, which PH4 holds at zero. Its factor is therefore \(v_z(0)=1\). This is the literal active-flatness check in SA 11183–11202, rather than an inference from a support mask alone.

The repaired chart equations give \(RD^{\mathsf T}a=0\), \(F'(a)=K_a^{\mathsf T}\omega\), and \(q(a)=\mathsf b(B)\). Along active rows, \(dF(a)=\langle\omega,\iota\,dB\rangle\), proving the first formula in (26). For an active tangent \(e=\iota b\), let \(h_e,\omega_e\) be the derivatives of the chart and multiplier. Differentiating the constraint, slice and critical equations gives
\[
 Kh_e=e,\quad RD^{\mathsf T}h_e=0,\quad
 L_0h_e=K^{\mathsf T}\omega_e,\qquad
 \Phi''_{\rm act}(0)b=\iota^{\mathsf T}\omega_e.             \tag{27}
\]
The unrestricted value function retains its reduced-datum derivatives; no full-row value-Hessian assertion is needed.

To compare with SA, \(K=\mathsf mQ\), \(J=K^{\mathsf T}\lambda_0\), \(QH=I\), and \(q''=2\mathsf m C^{(2)}\). Hence \(H^{\mathsf T}J=\mathsf m\lambda_0\), and SA's \(\Delta^{(2)}[H^{\mathsf T}J]\) is exactly the multiplier contraction in \(L_0\). Lemma 6 turns
\[
 G_1^{-1}-Q^{\mathsf T}\mathsf aQ
   =\mathsf S^{\mathsf T}L_0\mathsf S+DRD^{\mathsf T}=:X.
\]
By (25) and (27), \(Xh_e=K^{\mathsf T}\omega_e\). Put \(a_r=\mathsf m^{-1}\mathsf a\mathsf m^{-1}\). Adding \(K^{\mathsf T}a_rKh_e\) gives \(h_e=G_1K^{\mathsf T}(\omega_e+a_re)\). Multiply by \(K\) and invert \(KG_1K^{\mathsf T}=\mathsf m(QG_1Q^{\mathsf T})\mathsf m\) to obtain
\[
 \omega_e=\mathsf m^{-1}[(QG_1Q^{\mathsf T})^{-1}-\mathsf a]\mathsf m^{-1}e.
\]
Now \(e=\iota b\) and \(\mathsf m\iota=\iota\); (27) proves (26). ∎

**Theorem 8 (c: G-ID(cov) on the admitted R4 class).** Assume M, PH1–PH4 and D2. At every admitted complete physical pair in R4, the exponent (22) has no linear term, and its quadratic term in fixed normalized coordinates is
\[
 -\tfrac\tau2 b^{\mathsf T}\mathsf A^Y(P_W)b.                \tag{28}
\]
At \(\tau=1\) its Gaussian covariance is \(\mathsf A^Y(P_W)^{-1}\). At \(s=\mathbf1\), (6) is its \(I_0\)-marginal covariance, divided by \(\tau\). This holds without imposing Rep, and for every admitted splitting of the same physical pair.

*Proof.* First work at an axial physical representative. PH3 identifies the action in (22) with \(\Phi_{\rm act}(C_V(u))\). PH2 makes its first derivative zero: the actual reconstructed curve lies in the next constraint. Lemma 1 makes the gauge derivative zero as well.

Differentiate \(q_V(C_V(u))=0\) twice. The nonpivot part of \(C_V''\) is zero, so
\[
 C_V''(0)[u,v]=-h_Vq_V''(0)[\mathsf C_Vu,\mathsf C_Vv].
\]
The chain rule and (26) now give
\[
 \psi''(0)=\mathsf C_V^{\mathsf T}
 [\Phi''_{\rm act}(0)+\mathsf G^Y_V-E_{\rm amb}[\iota^{\mathsf T}\lambda_0]]\mathsf C_V.
\]
Since \(QH_1=I\), \(H_1^{\mathsf T}J=\mathsf m\lambda_0\), and \(\mathsf m\iota=\iota\), this is exactly (3). The scaling \(x_j u^2=\tau b^2\) proves (28). At axial \(V\), the entire gauge functions, hence their Hessians, agree with the absolute form.

For a non-axial real physical background, descent Lemma 1 supplies a real canonical axial representative with the same radii. PH3 transports the actual branch, PIV transports its graph, and (2) transports its gauge factor. Thus \(\psi_{P^g}(O(g)u)=\psi_P(u)\). Its Hessian and (3) undergo the same orthogonal conjugation. This proves (28) on all admitted R4 orbits. Pair dependence extends the conclusion to another admitted splitting; it does not admit a new splitting by itself.

Finally at complete data the untagged root is the symmetric \(\mathsf A^{-1/2}\). If \(B=\mathsf A^{-1}\), block inversion gives \(B_{00}=C+C A_{01}B_{11}A_{10}C\). The right side equals \(C+C\Gamma\Gamma^{\mathsf T}C\). This is the marginal identity in (6); normalized finite-dimensional Gaussian integration identifies the functional. Conditional integration on a proper \(S\) instead uses (21), with precision \(A_S\) and mean \(-A_S^{-1}A_{ST}b_T\). ∎

This proves the algebra sketched at **SA 10208** and 14109–14120 under the named background inputs. SA 10210 starts the walk geometry. **Outstanding (physical application):** PH1–PH4, their common admitted domains and the actual branch match must hold for each step. Gauge invariance of the action alone would not identify two different background branches. TP1's energy identification G-ID(TP) is a different statement and is not proved here.

**Lemma 9 (physical admission; corrected draft Lemma 6.10).** Let \(P_W=(U_+,0,J(U_+))\). Assume the torus room of M and, for every required box of side \(S\le C_{\rm box}LM\), Q-real on its enlargement of side \(S+22\), including complete currents, F0 and the common finer-unit seam gauge. Suppose
\[
 |\partial U_+-I|<a_0\eta^2,\quad |J(U_+)|\le L^2w<j_0,\quad w<a_0,
\]
\[
 (S+18)L^3w<c_{\rm rg},\qquad
 4L^3B_*(S+18)w\le a_{\rm FH}.                              \tag{29}
\]
Then \(P_W\in\mathrm{R4}(\mathbb T;a_0,a_1,j_0)\) for \(a_1>0\), with cp12's \(C_{\rm pot}\). To use Theorems 2 and 5 also impose **all** descent (7)–(8) ceilings, not just the real-gauge ceiling.

*Proof.* The two curvature requirements coincide and the \(A'\) requirements vanish. The current inequality gives its required strict ceiling. Cp12's PR1 application supplies on each smaller box
\[
 |A|,|\nabla A|\le C_{\rm pot}Mw<C_{\rm pot}Ma_0,\qquad
 C_{\rm pot}=4L^3B_*(C_{\rm box}L+18)\max(C_F,C_{F,\alpha_H}).
\]
Its proof requires exactly the enlarged-box and seam premises retained above. These verify every clause of (1). The working-domain conversion then uses \(L^2(1+C_{\rm pot}M)a_0<h/16\) **and** \(r(P_W)\le L^3j_0<r_{\rm loc}/2\), with the remaining envelope ceilings. ∎

Supplying (29) for actual histories remains DOM/BG1. The implication is correct; the draft's final sentence omitted the independent complex/current working-domain ceiling and could not be read literally with arbitrary \(j_0\).

## 6. The two operator transfers

**Lemma 10 (PR-lay Theorem 3 off Rep).** Rebuild PR-lay's R/W estimates for the Y coefficients as in descent Lemma 4. Include the scalar-to-bond-block factor at most three in \(H_{\rm PR}\) before defining
\[
 V_0(\mu)=12\left(\frac{1+e^{-\mu}}{1-e^{-\mu}}\right)^4,\quad
 H_{{\rm PR},1}=16L^2H_{\rm PR}/h_{\rm PR},\quad
 r_{\rm PR}=\min\{h_{\rm PR}/(16L^2),
                  c_L/[2H_{{\rm PR},1}V_0(\mu_{\rm PR})]\}.
\]
Here \(h_{\rm PR},\mu_{\rm PR}\) and the walk summation floors are PR-lay (11)'s early quantities, recomputed for Y. Let \(d_{\rm PR}\) be PR-lay's periodic \(\ell^1\) distance between bond base points. Every complete R4 pair whose real data convert to PR-lay's real class with bound \(<h_{\rm PR}/2\), and whose \(r(P)<r_{\rm PR}\), satisfies
\[
 \begin{split}
 \mathsf A^Y&=(\mathsf A^Y)^{\mathsf T},\quad
 \Re\mathsf A^Y\ge(c_L/2)I,\quad
 \|\mathsf A^Y\|\le H_{\rm PR}V_0(\mu_{\rm PR}),\\
 |\mathsf A^Y(P)_{\beta\beta'}|
   &\le H_{\rm PR}e^{-\mu_{\rm PR}d_{\rm PR}(\beta,\beta')},\\
 |(\mathsf A^Y(P)-\mathsf A^Y(P_0))_{\beta\beta'}|
   &\le H_{{\rm PR},1}r(P)e^{-\mu_{\rm PR}d_{\rm PR}(\beta,\beta')}.
 \end{split}                                                     \tag{30}
\]
These are bond-block bounds, with all constants before \(\kappa\), independent of \(M,\bar\kappa\). Coordinate compressions have the same gap on their range.

*Proof.* At a real representative the Y and absolute gauge Hessians agree, giving R. On complex representatives they need not agree: use the Y finite-stencil bound to rerun W, its geometric summation and the admitted-line Schwarz argument of PR-lay Lemmas 1–2. That argument yields the two entry bounds in (30); Schur summation bounds the perturbation by \(H_{{\rm PR},1}V_0r<c_L/2\), proving the gap. For a general real splitting, take the canonical real gauge \(u(U)\). The **same** gauge takes \(P_0\) to its representative. For each bond pair,
\[
 \mathsf A^Y(P)_{\beta\beta'}
 =O_\beta^{-1}\mathsf A^Y(P^{u(U)})_{\beta\beta'}O_{\beta'},
\]
and the identical formula holds for the difference from \(P_0\). Both orthogonal blocks preserve the block operator norm, while \(r(P)\) and the real class are invariant. This proves the transport without an additional radius loss. Symmetry, holomorphy, reality and compression follow from the same conjugation and R/W. Converting scalar entries after choosing \(r_{\rm PR}\) would instead require rechecking the Schur loss; the stated order avoids that mistake. ∎

**Lemma 11 (carrier-adopt Theorem A with Y; rests on unfrozen carrier-adopt Definition D, Lemmas C and P, Theorem A, on inv-root and on h-walk-fix, checked by Codex in carrier-check.md but not frozen).** At complete admitted pairs the Y bounds of M give \(\Re\mathsf A^Y\ge aI\), \(\|\mathsf A^Y\|\le b\), with
\[
 a=5c_L/8,\qquad b=W.
\]
Use carrier-adopt Definition D as an **explicit replacement** of the stored series, with its closed-cell retention rule and enlarged full hulls. Recompute inv-root's constants \(\Lambda_c,p_c,\vartheta,R_c\) using this \(a,b\) and the repaired Y walk moment. They are early. Put
\[
 W_A=e^{2\vartheta R_h}W,\quad
 W_C=2p_ce^{2\vartheta R_c}/\Lambda_c,\quad W_*=W_A+W_A^2W_C.
\]
For cell size \(s=LM\check R\), \(\check R\ge1\), the kept matrix \(\mathsf K\) obeys
\[
 \Re\mathsf K\ge[a-W_*e^{-\vartheta s/2}]I\ge(5c_L/16)I       \tag{31}
\]
provided \(LM\ge8R_c\) and
\[
 M\ge M_{\rm cut}:=\max\{0,\tfrac2{\vartheta L}\log(2W_*/a)\}.
\]
The rejected part has carrier-adopt Lemma P's bound
\[
 \sup_Q\sum_{X\ni Q}e^{\kappa d_{k+1}(X)}
           |\mathsf B^\times(X)|
 \le C_B H_b^2e^{-\vartheta LM\check R/32}                    \tag{32}
\]
for stored fields \(\sup_\beta|b(\beta)|\le H_b\), if also
\(M\ge1024\kappa/(\vartheta L)\). The constant \(C_B\) is early.

*Proof.* Compression preserves \(a,b\) and the walk moment. Inv-root's short/long split, finite grouped polynomial and geometric resolvent construction therefore apply with these numbers; taking \(t=0\) gives the covariance moment \(W_C\). The full hull satisfies diameter at most its tree length plus twice the fixed margin. This yields the displayed diameter moments for the precision and inverse. Absolute product summation gives \(W_*\) for the true Schur series
\(\Sigma=A_{I_cI_c}-A_{I_cJ_c}A_{J_cJ_c}^{-1}A_{J_cI_c}\).

For \(w=-A_{J_cJ_c}^{-1}A_{J_cI_c}v\), one has
\((v,w)^*A(v,w)=v^*\Sigma v\), hence \(\Re\Sigma\ge aI\), including at complex pairs. A carrier of diameter \(<s\) meets at most two adjacent grid intervals in each direction; all those closed cells have a common point. Its nonempty stored-cell intersection is connected and the other cells lie within one layer, so the retention rule keeps it. Thus a rejected chain meeting a stored endpoint has diameter at least \(s\). Its row and column sums are at most \(W_*e^{-\vartheta s/2}\), proving (31) by subtraction from the true Schur form.

For (32), the same rejected chain has tree length \(t\ge s/2\). Carrier-adopt Lemma P's covering tour gives
\(d_{k+1}(X)\le32+256t/(LM)\) and
\(\operatorname{dist}(x,Q)\le32LM+256t\) when \(Q\in X\).
Split the absolute \(\vartheta t\) moment into four quarters, using them for rejection, polymer length, root distance and summation. With \(\beta=\vartheta/1024\), the bound is
\[
 \tfrac12H_b^2\,[W+W^2(2p_c/\Lambda_c)]
 e^{-\vartheta s/8+\vartheta LM/16}
 \sum_xe^{-\beta\operatorname{dist}(x,Q)}.
\]
The last sum is at most \(C_\beta(LM+1)^4\). Since \(s\ge LM\), half the remaining exponential absorbs that polynomial by the exponential series, giving (32). The floor on \(M\) makes its native rate \(\vartheta LM/1024\) at least \(\kappa\). ∎

This verifies Theorem A(i)–(iv) for the replacement. Its (v), carriage across labels or tori, **also retains** h-walk-fix Lemma N, Theorems W′/H′ and their gate's region-restriction and common-lift hypotheses. Under those hypotheses each grouped entry reads the same coefficients and mask on a common hull, so products and normally convergent sums agree there. Descent's fixed-region pair dependence alone does not prove those extra hypotheses. The exponent \(-b^{\mathsf T}\mathsf Kb/2\) has coercive coefficient \(a/4=5c_L/32\), or \(a/8\) if half is reserved, rather than the matrix coefficient \(a/2\). Neither this transfer nor inv-root's global argument admits a nonextendible local pair; Theorem 2 uses hm's local construction for that reason.

## 7. Order and consumer boundary

The following is the order of **this implication**, within IN1's ten-row order and its Amendment 1. No early constant is defined using a later coupling ceiling.

| IN1 rows | Choices and retained conditions |
|---|---|
| 1–3 | Fix margins, exponents, hull geometry, \(L\ge27\) odd with \(L>L_0^\natural\), flat and averaging data, analytic/gauge/inverse rates and ceilings. Then choose \(M_1,R_1\), separation floors, tower and seam data in their imported order. Obtain R/W/AV and PIV uniformly in larger admitted gaps. |
| 4, before \(\kappa\) | Fix the Y walk bounds \(W,\mu_W,R_h\); \(h,H_1,r_{\rm loc}\); local buffers and grouped-root \(r_c,n,\theta,R_*,p,U_{\rm root}\). Fix \(C_{\rm hull},C_{\rm vac},\rho,B,N_o,R_g\); Lemmas 10–11's constants if used. Then fix descent (5)'s \(K_0,H_0,b=32,d=\theta/4,C_\tau,H_p=L^3\); FG's \(A,\varepsilon_0,\zeta_0\); \(P_d,c_m,D_0,W_0\) from (11). **All precede \(\kappa\), independently of \(M,\bar\kappa\).** |
| 4–5, after those constants | Choose \(\kappa\ge\kappa_0^\natural(L)\), then IN1's \(\Theta\), rate-window choice and potential rates; then \(\bar\kappa>\log2,\kappa_1\), response lengths/radii and preparation constants. Retain the rate window, entropy, insertion and failed-test conditions read by FG/UM and TD. Choose \(M\), a power of \(L\), above all imported collar/tower floors and the explicit floors below. |
| 6 | Set \(\varepsilon_*,\gamma_t\) by (12). Choose post-\(M\) chart and cutoff constants, \(A_1\), then \(A_0>2BA_1/\rho\). Choose absolute radii, current ceilings and coefficient-ratio room as below, and all separate consumer radius ratios. |
| 7–8 | Choose determinant/reference volume allowances, including \(C_{\rm vac}(LM)^4\), and the other \(E_N,C_E\), boundary, flow and tube constants **only after their separate interfaces are supplied**. Fix \(a_{\rm rest}\)'s allowed ceiling. |
| 9–10 | Increase \(X_0\) so running radii satisfy the fixed ceilings, \(\delta_j\le\rho/2\), \(a_{\rm GF}\le W_0/4\), \(a_{\rm rest}\le W_0/4\), and the actual tube and domain conditions. Then take the coupling \(g\le X_0^{-1/2}\), frame and admitted grid. The bound \(C_0^{\rm UM}\le1\) and \(W_0\) do not change. |

Explicitly the \(M\)-floors include hm (23),
\[
 \begin{gathered}
 M\ge\max(2R_*,b_{\rm gap},\ell_{\rm IMS}),\quad LM\ge8R_*,
 \quad c_gM_1\le C_{\rm box}M,\quad
 128\bar\kappa/(LM)\le\theta/2,\\
 2\ell_{\rm IMS}+2b_{\rm gap}\le C_{\rm box}LM,\quad
 We^{32\bar\kappa-dM}\le c_L/8,\quad
 H_0e^{32\bar\kappa-dM}\le\min(1/2,\varepsilon_*/2),
 \end{gathered}
\]
and \(M>R_g+2\), (18), and Lemma 11's floors if that transfer is used. Because \(\kappa\) is already fixed, (18) creates no cycle. All are eventually satisfied by increasing a power of \(L\): the only polynomial-versus-exponential comparison needed is \(M^4e^{-dM}\le5!/(d^5M)\).

The later ceilings are
\[
 \begin{gathered}
 L^2(1+C_{\rm pot}M)a_0<h/16,\quad
 L^3(a_1+j_0)<\min(r_{\rm loc}/2,1/(2H_0)),\quad |\tau-1|\le1/4,\\
 H_0L^3(a_0+a_1+j_0)+C_\tau|\tau-1|\le\varepsilon_*/2.
 \end{gathered}
\]
Take also Lemma 10's early \(r_{\rm PR}\) ceiling when (30) is consumed, and PH/Q-real's independent admission conditions when physical statements are consumed. The factor \(e^{32\lambda_V}\) in (10) is fixed after the rate choice; it is **not** an early matrix constant. Its size is paid by the final \(X_0\). For a larger declared fluctuation domain, impose Lemma 3’s ceiling with its actual \(\delta_B\), and include the stated \(C_{\rm win}\) factor in the real-cutoff and \(A_0\) choices.

## 8. Source checks and supplied definitions

The source pin is [31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775). The outline index, its neighbouring rows and obligations were used before reading bounded source excerpts; the five raw files were each fetched once. The following records the source checks relevant to the conclusions, not a claim to have proved their imported packages.

| Source lines checked | Reading used here |
|---|---|
| SA 5665–5694; 7178–7193; 7943–8001; 8436–8455 | R4 includes witnessing gauges; contour means differ from comb transport; the absolute factor and Hessian use the actual means and branches. |
| Y3 3633–3647; 31510–31545, especially 31522–31536 | The trace pairing and relative quadratic form. The latter passage does not specify a unique nonlinear gauge factor; D2 adds that convention and Lemma 1 states the valid uniqueness claim. Its three-dimensional volume pairing is not substituted for PH4. |
| SA 10139–10214; 10296–10306; 11176–11247 | Straightened/plain normalization, explicit six-term current continuation, active datum, pivot curvature and gauge choice. The substantive physical identification is at 10208; 10210 starts walks. Lemmas 6–7 supply the identities used here by hand. |
| SA 10311–10336; 10550–10554 | The outline already has propagator/covariance walk schemes and response parameters. D4 and carrier-adopt D are specified replacements; their tagged terms are not asserted equal to a different scheme. DR's response parameters are not the coarse UM switches. |
| SA 13904–14089; 14091–14270; 14293–14412; 14485–14560 | FG is the abstract Gaussian implication. The step discussion excludes a Gaussian law for the full nonlinear disintegration. UM separately requires actual matrices, domains, supports, cutoffs and identities; its budget and term bounds are conditional. |
| SA 17252–17260; 17382–17389; 17317; 17344–17347; 17367–17370; 17520–17564; 17709–17712 | Threshold ratios, axial approximate-test references, totality conventions, the limited support on which old indicators are one, the compressed determinant plus elimination factors, and stored gauge weights. These passages contradict the blanket unchanged-factor claim, not the small-box estimate of Lemma 3. |
| CA-I 8110–8148; 49495–49548, located also through the CA 4.12–4.19 index | The local-real-base statement carries outstanding proof; the operator application's background-gauge supply is an explicit condition outside its implication. Neither admits the consumer domains here. |
| CA-II 3460–3504; 59595–59618 | The first excerpt is surrounding constant/reference-kernel discussion, not the complex-Gaussian lemma itself. The second expressly leaves the local-data companion decay step open and explains why its constants must precede \(M\). |
| CA-III 98896–98937 | The sourced-expansion lemma assumes its format/cluster statements and a vertex input whose proof is incomplete at one step. It does not discharge actual formation here. |

No absence or novelty conclusion is inferred from these bounded readings. The nonlinear Y choice also does not justify replacing an old stored factor without its measure identity.

**Definitions supplied or made explicit.**

1. D1's bond-block norm, fixed geometric record and half-open ownership, while retaining the imported R4 and Rep definitions; in particular Rep concerns the real factor.
2. D2's whole nonlinear relative exponent and indicator, distinct from Y3's quadratic definition; the domain of the uniqueness assertion and the fixed-reference orbit reading of its scalar normalizer.
3. D3–D4's actual pivot convention and assigned full-read Y labels, separate root tags, discard-before-evaluation rule, normalized marginal, reference branch and empty-coordinate convention.
4. PIV's nonlinear holomorphic radius, uniform bound and complete read requirement; the fixed real normalization \(b=\sqrt{\theta_j}u\), its fixed real box versus the declared complex box, the Taylor-subtracted gauge potential and its external-pair hull.
5. D5's integration mask, compressed grouped resolvent, nonleading integrated closed labels, coarse filing, continued determinant logarithm and aligned unit-cell count.
6. D6's Gaussian part, PH1–PH4 including the actual branch match, highest-level active injection and fine/row pairing conventions; the active value function and Lagrangian Hessian.
7. Lemma 6's \(\Pi_J\) notation and the distinction between a slice-kernel identity and a raw-row identity; Lemma 9's complete physical-admission premises.
8. Lemmas 10–11's recalibrated Y block constants and kept/rejected replacement, and §7's early-versus-late budget allocation. The old source and library objects not changed by these definitions remain imports.

## Result

Under the named premises, Theorem 2 supplies the assigned Y Gaussian carriers and local matrix/structural envelope; Lemma 3 and Theorem 4 give the gauge formation estimate, UM4–UM6, UM14 and the early cost bound one; Theorem 5 gives a local determinant decomposition for the actual integration mask; and Theorem 8 proves G-ID(cov) on every **admitted complete physical R4 pair**, including non-axial real representatives. Lemmas 10–11 give the two requested operator transfers with their stated domains and extra carriage premises.

The imports are M's **R, repaired W, AV, W-cov and PF**, nonlinear **PIV**, **FG/UM** and the remaining actual potentials' full-domain UM1/interface; physical **BG and PH1–PH4**; and **Q-real/F0** for the admission lemma. Cross-record carriage additionally reads the named h-walk-fix hypotheses. All their flat, curved, inverse, tower, seam, branch and uniformity premises remain premises. Theorems here do not grant scientific or audit status.

**Outstanding:** PIV (the nonlinear pivot graph and contour-mean bounds; no named supplier); the actual stored-test/gauge-factor and old-activity formation match; whole-domain admission and the shrinking required by ci-form; physical chart/step branch matching at each actual history; and the full vacuum interface, including elimination factors, class/boundary and companion/coefficient identifications. The draft's assertion that nothing in item 6 remains outstanding is withdrawn. G-ID(TP), complete CI and H-OL are not proved.

**Corrections made in distillation.**

1. Restricted uniqueness to whole covariant nonlinear functions on the stated gauge orbits and common analytic domains. Equality of quadratic forms is insufficient. Replaced agreement “on Rep” by agreement at axial \(V\); complex Rep alone does not make \(V\) axial.
2. Made D4 an explicit construction choice and retained actual-formation and whole-domain requirements. A matrix envelope alone does not identify old activities, and fixed absolute radii do not imply ci-form's limiting perturbation bound.
3. Kept the correct zero-gradient argument, so the Y gauge completion has no F term. Stated PIV as the nonlinear input actually needed; linear pivot covariance does not supply it.
4. Used fixed real \(\sqrt{\theta_j}\) scaling and fixed cutoffs at complex couplings. Added external-pair reads to the gauge hull and the radius factor for larger declared complex boxes, including ci-form's scalar polydisc. Checked the relative insertion's scalar normalizer by Haar invariance. The remainder has order **at least three**, with the explicit norm tending to zero; no nonzero cubic coefficient is asserted.
5. Rejected draft Lemma 4.4: stored forms and earlier activities may change, and SA 17531 contains a gauge factor. The flat non-axial example distinguishes the two factors without claiming an admitted-history counterexample. Small-box deletion does not settle FC-test.
6. Replaced the claimed sole full determinant by the compressed determinant and conditional mean actually used. Retained the elimination factors and cross-record vacuum obligations. The determinant logarithm is the continued trace logarithm, not necessarily the principal scalar logarithm.
7. Repaired the vacuum count using a doubled tree tour and aligned unit cells, avoiding a bare-mesh density factor; enlarged \(C_{\rm hull}\). Repaired the \(\ell^\infty\) root sum with the additional \(32/\theta\) floor. The floor \(LM\ge4\kappa C_{\rm hull}/\theta\) is compatible with IN1 because \(M\) follows \(\kappa\).
8. Proved the six-term identity with its signs and factors, used only the needed slice kernel identity, kept the raw-datum normalization, and restricted the value-Hessian assertion to active data. Added PH3's precise branch match; covariance of the action alone does not supply it.
9. Added the missing current/complex working-domain ceilings and enlarged-box/F0/seam conditions to draft Lemma 6.10.
10. Recomputed carrier-adopt's constants at gap \(5c_L/8\), distinguished true Schur and truncated forms, kept the extra carriage hypotheses, and corrected the exponent's coercive coefficient. Wrote out PR-lay's bond-block transport with the norm conversion before its radius choice. The global inv-root series still needs hm's local reconstruction for local data.

**Checks of the draft's proposed corrections to other texts** (those files are unchanged):

| Passage | Conclusion |
|---|---|
| IN1 L106, “actual fluctuation law” | The draft's scope correction is right: this Gaussian identifies the quadratic part and its Gaussian marginal, not the full nonlinear law (SA 14215–14217). Calling the wording harmless would additionally require the actual formation identities retained above. |
| hm L47 and L482, F | The draft is right **for Y**: Lemma 1 makes F moot. This does not refute hm's historical statement for the absolute/completed reading or remove its other imports. |
| hm L45 source pinpoint | The correction to SA 14109–14120 is right. SA 10208 is the additional multiplier-Hessian sketch; 10210 concerns walks. |
| IN1 L108, inv-root/carrier-adopt | The global-versus-local distinction is right. D4 uses hm's local construction; no equality of independently tagged series follows, and no arbitrary existing assignment becomes hereditary. |
| FINISH row 274 and assembly-status §4 item 2 | The draft correctly identifies stale planning descriptions: descent is recorded frozen and FINISH row 278 chooses Y. That decision does not establish the draft's stronger complex-Rep equality or close the compatibility issues. |
| IN1's \(\rho,\rho_0\) versus hm/descent's \(\zeta,\zeta_0\) | The draft is right that these denote the same Gaussian tilt allowance; this is a notation change. |
| SA 10335 covariance | The Y labels are covariant after intermediate colours are grouped, as descent proves. This is not a proof for the unchanged absolute off-axial form and not a source-novelty claim. |

This research text is **not yet refereed**.

## Change log (freeze, 2026-11-05)

Distilled by Codex on the Mini. Refereed line by line by a fresh Claude session ([hma-gate](../gates/hma-gate.md)): first failing step none, 7 findings, all repairable. Applied by the lead (Claude):

1. D2: SA's \(\Re\operatorname{tr}\) vs this text's \(\operatorname{tr}\); agreement at real axial \(V\), holomorphic continuation at complex axial \(V\).
2. Theorem 2 to IN1 H-M (9): H-M's datum is the rescaled pair \((\tau^{-1}C,\tau^{1/2}\Gamma)\). Frozen descent (15) has the same reading.
3. Lemma 3's tree count: \(e^{15\lambda_V}\) suffices. Editorial.
4. UM6 holds for every tilt \(\gamma>0\), with joint holomorphy; the symbol clash on \(P_0\) is noted.
5. Theorem 5 off Rep: cites descent Lemmas 1, 4 and Theorem B.
6. PIV is added to the Outstanding list (no named supplier).
7. Lemma 11 names its unfrozen sources.

Referee verdict on SA's UM conditions: proved only for the adopted Y family D4, on R4 within descent (7)–(8)'s ceilings, without Rep; not for SA's absolute gauge factor (descent Theorem A). UM4 with \(R_s=e^{\bar\kappa}>2\), \(K=K_0\), \(\varepsilon\le\varepsilon_*\); UM5 with \(c_m=12\); UM6 in SA's form; UM14 with \(C_p=P_d\); UM15 cost \(C_0\le1\) with \(W_0\) fixed before \(\kappa\); gauge-type UM1 from Lemma 3. Imported: SA's FG1–FG12 and the counting constant of UM9–UM13; library M (frozen hm, descent Theorem B); PIV. Not supplied: UM1 for the other potential types; SA's structural identities linking UM3 to the actual step's expansion.

Status: **frozen.** Item 6 shrinks: gauge form fixed; formation and vacuum bounds done for the gauge potential and the compressed determinant; G-ID(cov) under PH1–PH4. Open: carrier identification (D4 adopts hm's carriers rather than identifying them), stored-test/gauge-factor formation match, whole-domain admission, PH1–PH4 per step, the full vacuum interface, PIV.

