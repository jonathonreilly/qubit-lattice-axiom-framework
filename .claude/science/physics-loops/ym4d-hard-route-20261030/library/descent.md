# Descent for H-M: Theorems A and B and Proposition C

Provenance: Codex, Pass 2 (distil), 2026-11-05, from Claude's 425-line `descent-draft.md`; checkout `7126dc00add0c03f564e03161d9ef6627c023b52`. Hand arguments only. Research text, not an audit; grants no status. Not yet refereed.

**Credit and sources.** SA denotes `YM4_sketch_500.tex`, CA-I the complete account I, and Y3 `YM3/YM3_I.tex`, at [revision 31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775). Their domains, averages, Gaussian construction and relative gauge form are credited to **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. The background and walk methods come through the library from Tadeusz Bałaban and Jonathan Dimock. Library inputs by Claude and Codex retain their stated premises. Source-line checks and identities are in [the check record](../checks/descent-pass2/source-checks.md).

**Main statement.** The absolute CF2 reading does not satisfy an all-R4 real gap (Theorem A). For each fixed admitted region sequence, replacing its ambient gauge Hessian by Y3's relative form gives the all-R4 H-M envelope, with the same radii and early constants as the replacement's representative-domain construction (Theorem B). Agreement with the absolute precision on all of R4 intersect Rep is incompatible with both the real tie and real-gauge covariance (Proposition C). These are conditional statements under the imports below. They do not identify the actual nonlinear formation with the replacement construction.

## Definitions and hypotheses

Use the geometry and full-stencil conventions of [hm](hm.md) §1 and [pr-lay](pr-lay.md) §1: odd \(L\ge27\), depth \(k\), bare mesh \(\eta=L^{-k}\), scales \(\xi_j=L^{j-k}\), separated longer sequence \(\mathbf S=(\Omega_0,\ldots,\Omega_{k+1})\), omitted inward rows, inner plaquettes and outer Dirichlet boundaries. All required boxes embed in the torus. The regions, cutoffs, active mask, pivots and branches are fixed. No comparison between different determining sequences is asserted.

The free space \(I\) consists of positively stored, non-pivot level-\(k\) bonds, with three real colours per bond. Its norm is Euclidean for \(\langle X,Y\rangle=\frac12\operatorname{tr}(XY)\). Transposes are bilinear; operator bounds use the Hermitian norm. A real site gauge acts by
\[
 U^g(b)=g(b_-)U(b)g(b_+)^{-1},\qquad
 A'^g(b)=\operatorname{Ad}(g(b_-))A'(b),\qquad
 \mathbf J^g(b)=\operatorname{Ad}(g(b_-))\mathbf J(b).
 \tag{1}
\]
Write \(\mathcal G\) for its real orthogonal action on \(I\). A central gauge has \(\mathcal G=I\).

A triple \(P=(U,A',\mathbf J)\) has pair \(\mathbf p(P)=(\mathbf U,\mathbf J)\), where \(\mathbf U=e^{i\eta A'}U\), and reference \(P_0=(U,0,0)\). On a supplied region \(Y\), **R4** means, on every complete contained read,
\[
 |\partial U-I|,|\partial\mathbf U-I|<a_0\eta^2,\quad
 |A'|,|\nabla^UA'|<a_1,\quad |\mathbf J|<j_0,
 \tag{2}
\]
and every contained box of side at most \(C_{\rm box}LM\) admits a real gauge \(U^h=e^{i\eta A}\) with \( |A|,|\nabla A|<C_{\rm pot}Ma_0\). Here
\[
 (\nabla^U_\nu A')_\mu(z)=\eta^{-1}
 [\operatorname{Ad}(U_\nu(z))A'_\mu(z+\eta e_\nu)-A'_\mu(z)].
\]
This is SA 5665–5694. Its hereditary core further imposes R5–R6; those tower conditions are not used below. Put \(r_Y(P)=\max\{l|A'|,l^2|\nabla^UA'|,l^3|\mathbf J|\}\) over contained reads, with the largest-incident-scale convention and \(l\le L\).

Blocks partition level-\(k\) sites with fixed ownership. Let \(\mathfrak B(Y)\) contain the active next-level blocks whose complete iterated averaging reads lie in \(Y\). Write \(y_b\) for a block centre and \(c_b(V;x)=V(y_b,x)\) for its **averaged contour**, not a tree transporter. **Rep** means \(c_b(\mathcal M^kU;x)=I\) for \(b\in\mathfrak B(Y)\), \(x\in b\). Set \(\mathcal K(Y)=\mathrm{R4}(Y)\cap\mathrm{Rep}(Y)\). A residual gauge is constant on each such block's level-\(k\) sites; it need not be constant at other bare sites.

For a level-\(k\) field \(V\), let
\[
 W_{b,x}^V(D)=(e^{iD}V)(y_b,x),\quad
 \widehat W_{b,x}^V(D)=W_{b,x}^V(D)W_{b,x}^V(0)^{-1},\quad
 \mathsf b_V(D)_{b,x}=\frac1i\frac d{dt}\Big|_0\log\widehat W_{b,x}^V(tD).
\]
Define two holomorphic quadratic forms, summing \(x\ne y_b\):
\[
 \begin{split}
 \mathsf G^{\rm abs}_V&=\operatorname{Hess}_{D=0}
       \sum_{b,x}[1-\tfrac12\operatorname{tr}W_{b,x}^V(D)],\\
 \mathsf G^{\rm Y}_V(D,E)&=\sum_{b,x}
       \langle\mathsf b_V(D)_{b,x},\mathsf b_V(E)_{b,x}\rangle.
 \end{split} \tag{3}
\]
The first is the absolute CF2 Hessian on real fields (SA 8436–8455); the second is Y3 31522–31536, used in four-dimensional block geometry. Y3 3633–3647 fixes the same trace pairing. Let \(\mathsf C_V\) be the actual pivot-graph derivative. With \(V=\mathcal M^k\mathbf U\), define
\[
 \mathsf A^\bullet(P)=X(\mathbf p(P))+\mathsf C_V^{\mathsf T}
                    \mathsf G^\bullet_V\mathsf C_V,
 \qquad \bullet\in\{\mathrm{abs},\mathrm Y\}.                    \tag{4}
\]
Here \(X\) is exactly pr-lay (7) without \(K_{\rm GF}\): it retains the active injection, straightened inverse, row mass and plain-constraint current contraction. Changing (3) changes the off-axial precision; it is not a reinterpretation of a fixed matrix.

The imports are:

* **R:** hm §1's global real gap \(\mathsf A^{\rm abs}(P_0)\ge c_LI\), at real block-axial references of real bound \(<a_R\), uniformly over the admitted separated sequences. Its flat, curved-coefficient and separation premises remain imports.
* **W:** hm §1's primitive inverse/walk package, including h-walk (I1)–(I3), Lemma U and h-walk-gate §§5–8's repairs. This includes uniform complex inverses on every cut-down; arbitrary scale-bounded multiplier coefficients; the all-scale absolute second-jet bound; bounded analytic one-step maps; two-difference cutoffs; branch powers, root counts and all zero-length multiplier reads. It excludes the rejected region-trace and reflection claims. Use h-walk's explicit fixed-region formulas, not an arbitrary expansion having the same sum.
* **AV:** the actual means and averages on their common regular analytic branches, with local branch existence and uniform finite-stencil bounds on the admitted domains. The formulas are SA QC1–QC4, 7943–8001; the quantitative mean and one-step bounds are at 8002–8053 and 8108–8141. Iterated-domain admission and the bounds read by W remain imported.
* **W-cov:** h-walk (I2)'s covariance of the straightened field/site rows and their derivatives, hence of the non-gauge terms under every real gauge; the covariance of \(\mathsf C_V\) follows directly from Lemma 1's equation (10). This is the surviving covariance clause of h-walk-gate §§6–8, not full covariance of the absolute gauge Hessian.
* **PF:** use the operators at the complex pair itself, with the same intrinsic branches on overlaps, as in SA 10139 and 10163–10186 and pr-lay (6)–(8). The real splitting certifies the domain; it is not an extra matrix coefficient. Lemma 4 verifies this property through the explicit labelled construction.
* **FG/UM:** hm's finite-dimensional Gaussian comparison and its declared potential, fixed-cutoff, finite-type and carrier-count hypotheses. For Theorem B's UM conclusion, these hold on the **whole R4 domain in use**, for the replacement family and its actual integrands. Retain IN1's other rate/count, insertion-smallness and failed-test conditions. They are not consequences of a matrix bound.
* **G-ID(flat):** only for Theorem A, the flat precision is the \(C^2\) fibre Hessian of the gauge-invariant critical action plus CF2, in canonical Gaussian normalization. **G-ID:** only for physical identification in Theorem B, the admitted complete axial physical precision is the Gaussian precision of the step. These are the identifications sketched at SA 10208 and 14108–14120. They are distinct from TP1's Gaussian-energy identification.

**Order of choice.** Follow frozen IN1, “Constant order,” and hm (4), (7), (12)–(13), (22)–(24), (32)–(35). First fix geometric margins, \(L\), flat/analytic data, rates and ceilings; then \(M_1,R_1\), separation floors and R/W constants. Include the bound for (3)'s Y form here, enlarging moments to cover both readings when they are compared. Next fix \(W,\mu_W,R_h\), \(h,H_1,r_{\rm loc}\), localization buffers, root grouping constants \(r_c,n,\theta,R_*,U_{\rm root}\), and
\[
 \begin{split}
 K_0&=1+4/(3c_L)+W+WU_{\rm root},\quad b=32,\quad d=\theta/4,\\
 H_0&=\tfrac8{3c_L^2}(W+H_1)+WU_{\rm root}
             +U_{\rm root}H_1+2WU_{\rm root}/r_{\rm loc},\\
 C_\tau&=4/c_L+K_0+1,\qquad H_p(M)=L^3.
 \end{split}                                                     \tag{5}
\]
Fix FG constants \(A=A_{K_0},\varepsilon_0,\zeta_0\), \(c_m=12\), the UM density constant \(P_d\ge1\), \(D_0=Ac_mL^4\), and
\[
 W_0=\min\{[3P_dL^4(1+Ac_m)]^{-1},\zeta_0/(2P_d)\}.                \tag{6}
\]
**Every constant through (6) precedes \(\kappa\), independently of \(M,\bar\kappa\).** Then choose \(\kappa\) and the other IN1 rates, \(\bar\kappa>\log2\), and \(M\) above hm (23)'s geometric, rate and collar floors. Finally choose radii and \(\tau\) satisfying
\[
 L^2(1+C_{\rm pot}M)a_0<h/16,\quad
 L^3(a_1+j_0)<\min(r_{\rm loc}/2,1/(2H_0)),\quad |\tau-1|\le1/2.     \tag{7}
\]
For the UM conclusion also impose
\[
 \begin{gathered}
 \varepsilon_* =\min\{\varepsilon_0,(3D_0M^4)^{-1}\},\quad
 \gamma_{\rm tilt}=\min\{2/(3D_0M^4),\zeta_0\},\\
 H_0e^{32\bar\kappa-dM}\le\varepsilon_*/2,\qquad
 H_0L^3(a_0+a_1+j_0)+C_\tau|\tau-1|\le\varepsilon_*/2.
 \end{gathered}                                                     \tag{8}
\]
These are later floors/ceilings, not definitions of early constants. The \(M\)-floor exists since \(e^{dM}\ge(dM)^5/5!\). Replacing the form may change the early constants and these final ceilings. Descent from the replacement's representative class introduces no further change of constants or radii. All uniformity premises of hm and IN1 remain in force.

## Proofs

**Lemma 1 (real orbits and the canonical representative).** R4 and \(r_Y\) are invariant under every real site gauge, with exactly the same radii. Under AV the gauge
\[
 u_Y(U)(x)=c_b(\mathcal M^kU;x)\quad
 (b\in\mathfrak B(Y),\ x\in b\text{ at level }k),\qquad
 u_Y(U)=I\text{ at other bare sites}                              \tag{9}
\]
is well-defined and real, and \(P^{u_Y(U)}\in\mathcal K(Y)\). It equals \(I\) when \(U\) is already Rep. The representative is canonical for the fixed blocks and branches, not a choice independent of those data.

*Proof.* A plaquette defect transforms by conjugation at its base point. Unitary conjugation preserves its norm, also for complex plaquettes. The same holds for \(A'\) and \(\mathbf J\). Substituting (1) gives
\[
 (\nabla^{U^g}A'^g)_\mu(z)
       =\operatorname{Ad}(g(z))(\nabla^UA')_\mu(z).
\]
If \(h\) witnesses a box gauge for \(U\), then \(hg^{-1}\) witnesses the identical potential for \(U^g\), since \((U^g)^{hg^{-1}}=U^h\). Thus every bounded quantity in (2), the local regular class and \(r_Y\) is preserved.

Every path transport transforms by its endpoint gauges. The mean equation \(\sum_i\log(T_iT^{-1})=0\) conjugates at the initial endpoint. Uniqueness on AV's branch gives endpoint covariance of its solution. QC3's closed logarithms conjugate at the block centre; its final straight transport supplies the other endpoint. Iterating proves
\[
 \mathcal M^k(U^g)=(\mathcal M^kU)^{g|_{\Lambda_k}},\qquad
 c_b(V^v;x)=v(y_b)c_b(V;x)v(x)^{-1}.                              \tag{10}
\]
The real mean lies in \(SU(2)\); the empty contour is \(I\). Disjoint site ownership makes (9) unambiguous and gives \(u(y_b)=I\). Equation (10) now makes every required contour equal \(I\). The first part preserves the radii.

For later use, two such representatives related by \(g\) differ by

\(r=u_Y(U^g)g u_Y(U)^{-1}\), with \(r(x)=g(y_b)\) on each required block. Conversely a gauge preserves Rep exactly when it is residual there, by (10). No R5–R6 invariance is needed. ∎

**Lemma 2 (relative and absolute gauge forms).** On AV's branch, \(\mathsf G^{\rm Y}_V\) is the Hessian of
\[
 \Phi_V^{\rm Y}(D)=\sum_{b,x}[1-\tfrac12\operatorname{tr}\widehat W_{b,x}^V(D)].
\]
Its gradient at zero vanishes. It equals \(\mathsf G^{\rm abs}_V\) at **every block-axial \(V\)**, real or complex. Under every real gauge \(v\),
\[
 \mathsf G^{\rm Y}_{V^v}=\mathcal V\mathsf G^{\rm Y}_V\mathcal V^{-1}. \tag{11}
\]
It is a bounded analytic finite-stencil form on the fixed smaller domains of AV, with an early bound.

*Proof.* For one contour write \(\widehat W(tD)=\exp(iH(t))\), \(H(t)=t\mathsf b+O(t^2)\), \(\operatorname{tr}H(t)=0\). Expanding the trace gives
\[
 1-\tfrac12\operatorname{tr}e^{iH(t)}
       =\tfrac14t^2\operatorname{tr}\mathsf b^2+O(t^3).
\]
The first derivative is zero; polarization of the second derivative gives (3). If \(W(0)=I\), the absolute and relative functions themselves coincide, proving equality of Hessians without a flatness assumption.

Equation (10), also valid at complex fields in the branch, gives
\[
 \widehat W^{V^v}(\mathcal V D)
       =v(y_b)\widehat W^V(D)v(y_b)^{-1}.
\]
The bilinear trace pairing is invariant under this conjugation. This proves (11); real gauges also preserve the operator norms and analytic neighborhoods. Each contour has finitely many paths of length at most \(2L\). In AV's local small gauge their products and mean have uniform holomorphic bounds on a fixed ball. Cauchy's formula on a smaller fixed ball bounds their first derivatives and \(W(0)^{-1}\), hence \(\mathsf b_V\) and (3). The stencil has at most \(L^4-1\) noncentre sites. Its bound depends on \(L\) and the early branch data, not on \(M,\bar\kappa\), depth or volume. At real data \(\mathsf b_V\) is Hermitian, so the form is real. ∎

**Theorem 3 (A: central-flip obstruction).** Assume R, AV, W-cov and G-ID(flat). On a complete flat torus choose an active block \(b\) and an interior noncentre site \(x\) whose eight incident level-\(k\) bonds are internal and active. Let \(w(x)=-I\), \(w=I\) at all other bare sites. Then \(P^w=(I^w,0,0)\) satisfies R4 for every positive choice of radii. Yet \(\mathsf A^{\rm abs}(P^w)\) has a negative direction. It cannot be the orthogonal transport of the positive flat precision.

*Proof.* The plaquette holonomies of \(I^w\) are all \(I\); \(A'=\mathbf J=0\). On every box the witness \(w^{-1}\) restores the zero potential. Thus all quantities in R4 are zero, even though \(c_b(\mathcal M^kI^w;x)=-I\).

Centrality gives \(e^{iD}V^w=(e^{iD}V)^w\). Precisely the contour ending at \(x\) changes to \(-W_{b,x}^V(D)\); all other contour endpoints have unchanged gauges. Hence
\[
 1-\tfrac12\operatorname{tr}W_{b,x}^{V^w}(D)
 =1+\tfrac12\operatorname{tr}W_{b,x}^V(D)
 =2-[1-\tfrac12\operatorname{tr}W_{b,x}^V(D)].
\]
If \(K_x\) is this one absolute Hessian, then
\[
 \mathsf G^{\rm abs}_{V^w}=\mathsf G^{\rm abs}_V-2K_x,\qquad
 \mathsf A^{\rm abs}(P^w)=\mathsf A^{\rm abs}(P_0)
                         -2\mathsf C_I^{\mathsf T}K_x\mathsf C_I. \tag{12}
\]
For the second equality use W-cov and \(\mathcal W=I\): \(X\) and the pivot derivative are unchanged.

Take a traceless Hermitian \(\sigma\) with \(\sigma^2=I\), and \(\lambda=\sigma\delta_x\) on level-\(k\) sites. Define \(d\lambda(z,z')=\lambda(z')-\lambda(z)\). The path \(e^{itd\lambda}=I^{e^{-it\lambda}}\) is pure gauge, pinned at every next-level centre. Its one-step average is unchanged by (10). Its eight nonzero bonds contain no pivot. Thus its free restriction \(b_\lambda\) satisfies \(\mathsf C_Ib_\lambda=d\lambda\), and \( |b_\lambda|^2=8\).

Every internal path from \(y_b\) to \(z\) has transport \(e^{it\lambda(z)}\), so its mean is the same matrix. The gauge functional along this straight coordinate line is exactly \(1-\cos t\). Consequently
\[
 \mathsf G_I^{\rm abs}(d\lambda,d\lambda)=K_x(d\lambda,d\lambda)=1.
\]
The critical action is the Wilson action of the selected critical background: it is nonnegative and vanishes at the flat background. Its chart gradient there is zero. Gauge invariance makes it constant along this fibre orbit. G-ID(flat) therefore gives \(X(P_0)(b_\lambda,b_\lambda)=0\); no acceleration term remains in the Hessian chain rule. Canonical normalization is SA 8457–8463. Equation (12) yields the exact values
\[
 \mathsf A^{\rm abs}(P_0)(b_\lambda,b_\lambda)=1,\qquad
 \mathsf A^{\rm abs}(P^w)(b_\lambda,b_\lambda)=-1.                 \tag{13}
\]
The unit-vector Rayleigh quotient is \(-1/8\le-c_L\), by R at \(P_0\). This proves the assertion. ∎

With W, the local version uses **all base points of the eight bonds**, denoted \(S_\lambda\). If \(S\supset S_\lambda\) and \(N_{b_{\rm gap}}(S)\subset Y\), hm's tail bound removes at most \(c_L/8\), so the compression of \(\mathsf A^{{\rm abs},Y}(P^w)\) has a unit-vector value at most \(-7c_L/8\). An admitted complex displacement with \(r_Y<r_{\rm loc}\) changes this by at most \(c_L/8\), leaving real part at most \(-3c_L/4\). Restrict the omitted-label sum to the normalized \(b_\lambda\) to obtain these bounds. The draft's condition \(x\in S\) alone was insufficient: incoming bonds have different base points. A complete-torus support already proves failure of hm's positive-reference prescription and FG1 for the literal family. No claim that SA selected this reading is involved.

**Lemma 4 (fixed-region labels: port, covariance and ties).** Replace only the gauge term in h-walk's local precision labels by (3)'s Y form. Then hm's representative-domain construction and estimates hold under R, W and AV, with early constants for this replacement. Under W-cov and PF, its precision and root carrier coefficients, grouped over intermediate colours, are real-gauge covariant and functions of the pair on their full read hulls.

*Proof.* At every real Rep reference the gauge forms agree by Lemma 2; hence R is unchanged. The new gauge labels have the same finite stencil and an early analytic bound by Lemma 2. This supplies exactly the gauge part of W's (I3). The primitive inverses and non-gauge tree labels are unchanged. Hm Lemma 1 therefore has the same proof with enlarged early moments. Its Lemma 2 uses only R4 and Cauchy bounds. Its Lemmas 3–4 compare matching fields with global real axial extensions, where R still applies. The grouped root proof, Theorems 7–8 and Corollary 13.1 then use those bounds and geometry. No gauge-gradient correction is needed for the new form: Lemma 2 makes that gradient zero.

Here is the missing PF-label check, using h-walk §§3–8. Cut-down regions, cutoffs and boundary spaces depend only on fixed geometry. In §4 the entries of \(K[\mathbf S,\mathbf p,j]\) are built from \(D_{\mathbf U},Q,Q',\Delta^W_{\mathbf U}\), their derivatives, the explicit current contractions, scalar weights and \(j\). By PF each is a pair function. Their local inverses are unique finite matrix inverses, so have the same property. Thus every §6 product

\(\widetilde h_{\kappa_0}S_{\kappa_0}\theta_{\kappa_0}R_{\kappa_1}\cdots R_{\kappa_n}\)

is a pair function. In §7, \(j_\beta(c)=\xi_c^{-4}\langle H_\beta e_c,\mathbf J\rangle\), its finite zero-length sum \(j^{(0)}\), the local inverses using \(j^{(0)}\), and the vertices \(V_\beta\) successively retain that property. So do the tree products and their final transposed multipliers. The §8 factors \(\mathsf C_V,E^{(2)}_V,\mathsf G^{\rm Y}_V\) read the pair alone. Include the extra \(j^{(0)}\) read boxes, as hm requires. Real witnessing gauges and real norms enter only estimates and admission; no such gauge enters these formulas. Therefore equal pairs on a full hull give equal precision coefficients. Hm's short-entry sums, polynomial grouping, products and convergent root integral preserve this equality. This proves PF-label for this specified construction, on common branches and fixed geometry.

For covariance, the same induction uses W-cov, Lemma 2 and the fact that scalar cutoffs commute with the gauge action at their base points. Inverses, transposes and products intertwine the appropriate input/output actions. A product with a **fixed intermediate scalar colour** need not be covariant. Sum those colours at each fixed spatial path first; hulls, lengths and tags are independent of colour. This regrouping changes none of the matrix sums. Triangle inequalities preserve the absolute majorants; any endpoint block-norm conversion is paid once in the early constants. Hm's root integral preserves the resulting covariance. ∎

**Theorem 5 (B: all-R4 H-M envelope).** Assume R, W, AV, W-cov and PF, the stated geometry, the order (5)–(7), and all hm (23) floors. On every \(P\in\mathrm{R4}(Z;a_0,a_1,j_0)\), with no Rep condition, use Lemma 4's coefficients directly at \(P\). For a fine support \(Z_0\), use hm's corner collar \(H=Z_0^\sharp\subset Z\) and projection \(\chi\) onto free coordinates based in \(Z_0\). Tag each full hull \(F\) once by each coarse cube it meets: \(s^F=\prod_{\Delta:\Delta\cap F\ne\varnothing}s_\Delta\). Set \(s=1\) on \(H\), \(s=0\) off \(Z\), and \( |s_\Delta|<e^{\bar\kappa}\) on \(Z\setminus H\). Discard unread hulls before evaluating coefficients. Define
\[
 \begin{split}
 \mathsf A(s;P)&=\sum_\omega s^{H_\omega}a_\omega^{\rm Y}(P),\quad
 \mathsf r(s;P)=\sum_\alpha s^{H_\alpha}r_\alpha^{\rm Y}(P),\\
 C&=(\chi\mathsf A(s;P)\chi)^{-1},\qquad
 \Gamma=-\chi\mathsf A(s;P)(1-\chi)\mathsf r(s;P),\\
 C_*&=(\chi\mathsf A^H(P_0)\chi)^{-1},\quad
 \Gamma_*=-\chi\mathsf A^H(P_0)(1-\chi)\mathsf r(1_H;P_0).
 \end{split}                                                     \tag{14}
\]
Here \(\mathsf A^H=\mathsf A(1_H)\); the compressed inverses act on \(\chi I\).
Then the series converge normally, \(C=C^{\mathsf T}\), and the references are real with \(C_*>0\). They obey
\[
 \begin{gathered}
 \|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0,\quad
 \operatorname{Re}C^{-1}\ge c_L/2,\quad \|C\|\le2/c_L,\\
 \|\tau^{-1}C-C_*\|+\|\tau^{1/2}\Gamma-\Gamma_*\|
 \le H_0\{e^{32\bar\kappa-dM}+L^3(a_0+a_1+j_0)\}
                       +C_\tau|\tau-1|=:\varepsilon.            \tag{15}
\end{gathered}
\]
The constants are exactly those of the Y-form construction on \(\mathcal K\); they need not equal the absolute family's previously chosen constants.

The matrices are holomorphic at fixed \(U\), hereditary for fixed geometry and common supports, and real-gauge covariant. They have the pair tie on every common admitted domain at **every \(s\)**. References are gauge covariant but need not be independent of the splitting.

If FG/UM holds and \(\varepsilon\le\varepsilon_0\), the normalized Gaussian with
\[
 D_\tau=\tau^{-1}(C+C\Gamma\Gamma^{\mathsf T}C)                  \tag{16}
\]
has hm Theorem 8's normalization, holomorphy, heredity, wall factorization, local dimension \(m\le12(LM)^4\#Z\), and finite interpolation identity. On a complete pair, at \(s=\mathbf1,\tau=1\), \(D=\chi(\mathsf A^{\rm Y}(P))^{-1}\chi\). G-ID identifies this with the actual Gaussian step on admitted axial physical pairs. With (8) and the remaining UM hypotheses, UM4–UM6 and UM14 hold with \(C_0^{\rm UM}\le1\) and early \(W_0\).

*Proof.* Lemma 1 gives \(u=u_Z(U)\) with \(P^u\in\mathcal K(Z)\), identical radii and identical \(r_Z\). This gauge is fixed on a fixed-\(U\) fibre. Lemma 4 gives termwise covariance after colour grouping, and the projections commute with its orthogonal action. Thus (14) is conjugate to the representative construction. For the rectangular coupling the formula is
\[
 C(P)=\mathcal U_0^{-1}C(P^u)\mathcal U_0,\qquad
 \Gamma(P)=\mathcal U_0^{-1}\Gamma(P^u)\mathcal U_I,
\]
Here \(\mathcal U_I\) acts on all free coordinates and \(\mathcal U_0\) is its restriction to \(\chi I\). The references obey the same formulas, since \(P_0^u=(P^u)_0\). Hm's operator norms, real parts and accretivity are preserved **exactly** under these conjugations. This proves (15) and normal convergence using its already fixed absolute majorants. Individual scalar entry moduli are not asserted invariant.

The definition evaluates the labels at \(P\); it does not use \(u_Z\). Thus changing \(Z\) with parameters zero outside a smaller domain preserves each surviving coefficient and its tag. Pair ties follow from Lemma 4 even after hull truncation. Fixed-\(U\) holomorphy follows from the same formulas and normal convergence. Connected hulls give wall block decomposition. Gauge covariance of the functional means the usual change of variables on its test function; it does not assert invariance of an arbitrary integrand. Gauge-invariant bond-ball cutoffs and covariant potentials preserve this change of variables.

FG gives the normalized density with covariance (16). Its positive-reference branch is unique in the accretive Gaussian neighborhood, so two splittings giving the same \(D_\tau\) give the same functional. Potential ties are an additional part of the integrand hypothesis. Restriction, factorization and dimension counting are those of hm Theorem 8; interpolation is the finite fundamental theorem of calculus in the exterior parameters. On a complete pair the root sum is \(\mathsf A^{-1/2}\). The block inverse identity yields

\((\mathsf A^{-1})_{00}=A_{00}^{-1}+A_{00}^{-1}A_{01}(\mathsf A^{-1})_{11}A_{10}A_{00}^{-1}=D\).

Only G-ID identifies this algebraic Gaussian with the physical step. At the axial physical locus SA 11239–11247 gives zero absolute gauge gradient, and Lemma 2 gives equality of the two Hessians there.

Finally FG6/FG12 and \(\zeta=P_dW_0M^{-4}\) give UM6. Equations (6), (8) imply \(\zeta+\gamma_{\rm tilt}/2\le\zeta_0\) and
\[
 C_0^{\rm UM}=P_dL^4W_0(1+Ac_m)
               +D_0M^4(\varepsilon+\gamma_{\rm tilt}/2)
             \le\tfrac13+\tfrac13+\tfrac13=1.
\]
This proves the claimed UM budget without choosing an early constant after \(M\). ∎

**Proposition 6 (C: agreement, tie and covariance cannot coexist).** Under AV, PF and W-cov, no precision assignment on all R4 torus triples can satisfy simultaneously:

1. agreement with \(\mathsf A^{\rm abs}\) on every triple of \(\mathcal K\);
2. equality at two real splittings of the same real pair;
3. covariance under every real gauge.

*Proof.* Fix any admitted depth and an interior level-\(k\) site \(x\) as in Theorem A. On bare sites put \(g_\varphi(x)=e^{-i\varphi\sigma}\), \(g_\varphi=I\) elsewhere. With \(d_{\rm bare}f(z,z')=f(z')-f(z)\), set
\[
 P_0=(I,0,0),\quad P_1=(I,\eta^{-1}\varphi d_{\rm bare}(\sigma\delta_x),0),\quad
 P_2=(I^{g_\varphi},0,0).
\]
Here \(e^{i\eta A'_\varphi}=I^{g_\varphi}\), \( |A'_\varphi|\le|\varphi|/\eta\), \( |\nabla A'_\varphi|\le2|\varphi|/\eta^2\), and both group fields are flat. Choose \(0<\varphi<\pi/4\) small enough for every final radius and displacement ceiling. No depth-independent lower bound on this witness is required. Then \(P_0,P_1\in\mathcal K\), \(P_2\in\mathrm{R4}\); \(P_1,P_2\) split the same pair and \(P_2=P_0^{g_\varphi}\). This avoids the draft's unspecified smooth bump.

The three asserted properties would force
\[
 \mathsf A^{\rm abs}(I^{g_\varphi},0)
       =\mathcal G_\varphi\mathsf A^{\rm abs}(I,0)\mathcal G_\varphi^{-1}. \tag{17}
\]
W-cov cancels the \(X\) terms. Evaluate on the orbit tangent \(b_\lambda\) from Theorem A, which commutes with \(g_\varphi\). Its full coordinate line is a commuting pure gauge, pinned at the coarse centres. AV therefore keeps its next average fixed. It has no pivot component, so \(\mathsf C_{I^{g_\varphi}}b_\lambda=d\lambda\), also at this non-axial \(V\). Its only nonconstant contour is

\(W_{b,x}^{I^{g_\varphi}}(t\,d\lambda)=e^{i(t+\varphi)\sigma}\).

Thus the left gauge Hessian in (17) is \(\cos\varphi\), whereas the right one is \(1\). Since \(1-\cos\varphi=2\sin^2(\varphi/2)>0\), (17) fails. This proof needs no unknown second Taylor coefficient and no G-ID. Under R/W, for sufficiently small \(\varphi\) both whole-torus Gaussians exist. Their covariances determine their precisions, so the same incompatibility holds for equality of their full normalized functionals. ∎

**Lemma 7 (changing the Gaussian split).** For the preceding R/W/AV family, in the library's convention \(e^Vd\mu_A\), where \(A\) is a precision, replacing \(A_{\rm abs}\) by \(A_{\rm Y}\) preserves the integrand measure with the choice
\[
 V_{\rm Y}(b)=V_{\rm abs}(b)
  +\tfrac12 b^{\mathsf T}(A_{\rm Y}-A_{\rm abs})b
  +\tfrac12\log\frac{\det A_{\rm abs}}{\det A_{\rm Y}}.           \tag{18}
\]
Use common analytic determinant branches near the positive references.

*Proof.* Divide the densities \( (2\pi)^{-m/2}(\det A)^{1/2}e^{-b^{\mathsf T}Ab/2}\). Their ratio gives (18). For unnormalized Gaussian weights the determinant term is instead accounted for in the vacuum normalization. On \(\mathcal K\), the full-precision difference has finite stencil and entries \(O(r_Y)\): it is bounded holomorphic on hm Lemma 2's line disc and vanishes at its real axial centre, so Schwarz gives this estimate. A cube contribution to the quadratic term is bounded by \(C r_Y\sum|b|^2=C r_YM^4(M^{-4}\sum|b|^2)\). For a localized **marginal**, however, the precisions in (18) are \(D_{\rm abs}^{-1},D_{\rm Y}^{-1}\); finite stencil of the full-precision difference does not prove locality of this correction or of its determinant. ∎

**Outstanding — actual formation and admission.** Theorem B constructs the Y-form family on R4 with the specified ceilings. An application must use these carriers and supply its potentials, normalization and bounds there. Lemma 7 does not establish that every existing NL1/LF1 formation can be switched while retaining UM1 or the required local vacuum assignment. Nor does this note put every ST1 chain domain inside this R4 domain. These are the actual-family and CI obligations in hm 371–373, nl1-L Theorem 7, st1-r2 §1 and st1-draft3 §4.3, retained also in st1-r4's CI. G-ID and AV/W's branch and operator inputs remain imports. Real R5–R6 covariance would require the continued background's compatible gauge action; it is neither needed nor proved here.

## Change log (pass 3 fixes, lead, 2026-11-05)

Applied the findings of `gates/descent-gate.md` (Claude fresh session, first failing step none):
1. The source-check record linked at line 5 is not in this clone; the referee read every cited line directly.
2. hm's tilt constants are written zeta_0, zeta again (they had been renamed rho_0, rho, which clashes with pr-lay's layer separation rho = R_1 M_1).
3. Correction 8's support, stated exactly: SA 11229-11231 defines the gauge Hessian as that of "the actual function D -> GF(e^{iD}V)", and SA 7182's GF is absolute, so the absolute form is SA's literal off-axial reading there, and the flip triple P^w meets SA's regular-pair conditions (10129-10137). A defect is still not established: SA 11245-11247 leaves the choice to "the model being considered", SA 11239-11240 chooses the step's V block axial, R5-R6 for P^w are unchecked, and SA 7181's indicator 1{|V(y,x) - 1| < eps_k} puts the central flip outside the support of SA's gauge-fixing factor.
4. Covariance of C_V is cited to Lemma 1's (10), not to h-walk (I2).
5. W(0)^{-1} is bounded because det W(0) = 1, so the inverse is the adjugate (not by Cauchy's formula).
Referee's addition: the absolute gauge gradient vanishes at P^w, so Theorem A also holds for the completed form (pr-lay (9), SA PX104). The canonical representative is Lemma 1 (not Lemma 2).

**Status: frozen**, as a conditional theorem. Outstanding, named: local formation and vacuum bounds. Reopens only on a `wrong` signal or when an import it reads changes.

## Result

Theorems A and B and Proposition C are proved as hand-derived implications in their stated scope. Theorem B removes the Rep restriction for the **specified replacement matrix family**, with unchanged admissible radii and no new late dependence of an early constant. Lemma 4 also supplies its fixed-region pair tie at all parameters. The imports are R, repaired W, AV, W-cov, PF and FG/UM, with G-ID(flat) for A and G-ID only for B's physical clause. The outstanding application obligations are stated above.

**Definitions supplied or sharpened:** the two separate ambient gauge forms, relative function and trace normalization; R4 without Rep; active complete-read blocks and disjoint site ownership; the canonical bare-site gauge and its residual action; \(X\) as the unchanged non-gauge precision; full eight-bond support and the bare difference in C's witness; pair-only fixed-region labels with common intrinsic branches; colour-grouped carrier coefficients; the replacement's references and independent early constants; and normalized reweighting (18).

**Corrections to the draft and checks of its proposed corrections:**

1. **A survives, with scope and support repairs.** Equation (13) is exact and R4 radii are unchanged. The localized statement needs the entire bond support. At a general axial \(V\), the derivative is \(\mathsf b_V\), not CF3's flat \(\gamma\). No R5–R6 or physical identification follows merely from R4.
2. **B survives for the stated replacement.** Pair dependence of a total matrix alone does not prove a local tie, even at \(s=\mathbf1\). Lemma 4 supplies the missing factorwise proof and closes PF-label for the fixed formulas. Covariance requires colour grouping, not invariance of individual scalar entries. The new constants are early; literal equality of the old and new truncated-root references is not claimed when grouping constants change.
3. **C survives, with a shorter exact witness.** A commuting gauge at one bare site, with mesh-dependent small amplitude, replaces the unconstructed bump and the \(\pm\varphi\) cancellation of an unknown Taylor coefficient. Its conclusion concerns assignments agreeing with the whole absolute precision on \(\mathcal K\); it does not forbid arbitrary gauges or other replacement forms.
4. **The IF-pot assertion was wrong.** Its quadratic sign is reversed for \(e^V\), and it omitted normalized determinant accounting. Equation (18) repairs the identity; local formation and vacuum bounds remain Outstanding. Thus “none inside the target beyond the imports” does not establish the actual IN1/NL1/ST1 interface.
5. **Frozen pr-lay and hm are not refuted.** Pr-lay (7) uses the absolute ambient reading while its real factor is required to be Rep (line 60; Theorem 3). Hm has the same restriction (lines 33–47; Theorems 7–8). Both evaluate the form at non-axial \(\mathbf U=e^{i\eta A'}U\) even inside \(\mathcal K\), so the replacement genuinely changes those matrices. The central-flip real reference lies outside their stated domain. Their frozen implications stand; the unsupported extension of their absolute statements to all R4 fails. Hm 37 and 494 correctly retain that limitation. Pr-lay's warning that full gauge covariance is not asserted is correct for the absolute reading.
6. **H-walk's wider reading must be distinguished from a gap claim.** Its §2.1 explicitly uses the absolute CF2 Hessian on non-axial regular fields. Its surviving fixed-region walk estimate does not assert a positive gap there. The gate's corrected non-covariance calculation and block-constant covariance remain right. Its phrase “exactly under” does not classify accidental stabilizers; Lemma 4 proves full real-gauge covariance only for the replacement. No additional frozen walk estimate is refuted by A.
7. **Hm-draft 134's inference was unjustified.** Gauge invariance of activities does not make the absolute Gaussian matrices covariant. B supplies an orbit reduction for the replacement's invariant bounds, not an automatic equality of arbitrary supremum expressions. The optional transported-absolute construction is unnecessary here; C shows why any such extension retaining agreement and covariance cannot also have the real tie.
8. **No defect in SA's text as written is established.** SA 10200 does not fix the off-axial form. SA 11243–11247 explicitly distinguishes absolute and relative derivatives. The assertion at 14144 cannot be transferred through arbitrary real gauges under the absolute reading; A proves that conditional obstruction. It does not show that SA made that choice. The draft's “must be the Y3 form” was too strong: Y3 supplies a sufficient covariant choice, not a uniqueness theorem. No novelty claim follows from `um-novelty.md`'s bounded survey. The relative form and the Gaussian and inverse-volume cost strategies are already in the credited sources.

The context notes remain conditional: P82 concerns real constrained inverses; TP1 retains its distinct Gaussian-energy input; IN1 requires actual carriers; ST1 retains whole-domain CI. No frozen note, gate, prompt, ledger or status file was changed. **This text is not yet refereed and grants no scientific or audit status.**


*Referee status (lead, 2026-11-05): refereed line by line by a fresh Claude session; see the change log above and `gates/descent-gate.md` (st1-r4: `gates/st1-r4-gate.md`). The "not yet refereed" sentence in the Result above predates that check.*
