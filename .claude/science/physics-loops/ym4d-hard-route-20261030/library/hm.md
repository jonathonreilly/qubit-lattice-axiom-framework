# H-M: the Gaussian matrix envelope

Provenance: Codex, Pass 2 (distil), 2026-11-04; checkout a4e8c4a7f252a783dc375f56a239236463c54159. Research text, not an audit; grants no status. Based on Claude's `hm-draft.md`. Material from the pinned Sussman–Alpoge account is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. This manuscript is not yet refereed.

The result is a conditional local matrix construction with early constants, on the **specified axial representatives** below. It does not establish H-M on every declared SA core: the draft's passage to such representatives is unproved. Physical identification also retains G-ID. Theorem 7 states the exact envelope; Theorem 8 proves its structural clauses; Corollary 13.1 gives the UM budget. All proofs are by hand.

SA, CA-I/II/III and Y3 denote the five raw sources at commit 31a47c543775. The collared functional, Gaussian comparison, local-resolvent method and inverse-volume cost strategy belong to Sussman and Alpoge's text, authored with Claude and Codex. The layered inverse and walk method comes through the library from Tadeusz Bałaban; h-walk also uses Jonathan Dimock's parametrix exposition. The grouped series below adapts Codex's inv-root. Source checks and input identities are recorded in [the check record](../checks/hm-pass2/source-checks.md) and [the manifest](../checks/hm-pass2/source-identities.json).

## 1. Definitions and imports

**Geometry.** Fix odd \(L\ge27\), depth \(k\), bare mesh \(\epsilon_{\rm lat}=L^{-k}\), scales \(\xi_j=L^{j-k}\), and the fixed longer sequence \(\mathbf S=(\Omega_0,\ldots,\Omega_{k+1})\) of [pr-lay](pr-lay.md) §1. Its separation is \(\rho_{\rm lay}=R_1M_1\); the operator uses its depth-\(k\) truncation. The longer point scales \(l\le L\), largest-incident-scale seam convention, inner plaquettes, outer Dirichlet convention and omitted inward rows are those of that note. All required boxes and margins embed in the torus. The torus grids accommodate the powers of \(L\) chosen below. No assertion compares different determining sequences.

Let \(I\) be its positively stored, non-pivot, level-\(k\) bond coordinates, with three real colours per bond. A coordinate \(x\) has base point \(\hat x\); at most \(n_c=12\) coordinates share one site. Put \(d(x,y)=|\hat x-\hat y|_\infty\), periodically. Thus
\[
 \#\{y:d(x,y)\le t\}\le n_c(2t+1)^4.                                      \tag{1}
\]
Fine localization cubes have side \(M\), coarse parameter cubes side \(\ell=LM\), in level-\(k\) units; \(\Lambda\) is the finite coarse partition of the torus. Use compatible half-open ownership of sites and include every site of each read stencil. For a union \(Z_0\) of fine cubes, \(H=Z_0^\sharp\) is the union of coarse cubes containing a fine cube equal to, or sharing a corner with, a cube of \(Z_0\). This union-preserving collar satisfies \(\operatorname{dist}_\infty(Z_0,H^c)\ge M\). It is the permitted fixed enlargement of SA 14338–14347, used consistently in every formula here. \(I_0=\{x:\hat x\in Z_0\}\) includes all coordinates read by the selected potentials and tests; enlarge \(Z_0\) first if necessary. Write \(\chi=1_{I_0}\).

**Fields and local domains.** Real links are in \(SU(2)\); real potentials are traceless Hermitian matrices. Complex potentials and currents are independent complexifications. With matrix operator norm, put
\[
 P=(U,A',\mathbf J),\quad \mathbf U=e^{i\epsilon_{\rm lat}A'}U,\quad P_0=(U,0,0),\qquad
 (\nabla^U_\nu A')_\mu(x)=\epsilon_{\rm lat}^{-1}
 [\operatorname{Ad}(U_\nu(x))A'_\mu(x+\epsilon_{\rm lat}e_\nu)-A'_\mu(x)].       \tag{2}
\]
Transposition is bilinear; accretivity uses the Euclidean Hermitian inner product on coordinates. Fixed colour/coordinate norm conversions are included in the imported constants.

On a set \(Y\), \(\mathcal R_{\rm loc}(Y;\alpha_0,\alpha_1,\alpha_J)\) means: on every complete contained stencil, both real and complex normalized curvatures are \(<\alpha_0\), the bounds \(l|A'|,l^2|\nabla^UA'|<\alpha_1\) and \(l^3|\mathbf J|<\alpha_J\) hold, and every contained natural gauge cube of side at most \(c_gM_1\xi_j\) in the two-layer zone admits a real gauge with \(\xi_j|A|,\xi_j^2|\nabla A|<\alpha_0\). Here normalized curvature is \(\epsilon_{\rm lat}^{-2}l_p^2|\partial U-I|\), and the gauge derivative is plain. Define
\[
 r_Y(P)=\max_{\text{contained reads}}\{l|A'|,l^2|\nabla^UA'|,l^3|\mathbf J|\}.     \tag{3}
\]
Empty maxima are zero. Actual witnessing gauges are required.

The class \(\mathcal K(Y;a_0,a_1,j_0)\) imposes SA R4 on \(Y\): both plaquette defects \(<a_0\epsilon_{\rm lat}^2\), \( |A'|,|\nabla^UA'|<a_1\), \( |\mathbf J|<j_0\), and on every contained box of side at most \(C_{\rm box}LM\) a real gauge with \( |A|,|\nabla A|<C_{\rm pot}Ma_0\). It imposes also **Rep**: \(V=\mathcal M^kU\) is block axial on every active next-level block whose complete averaging read neighbourhood lies in \(Y\). Choose an early radius \(r_{\rm av}\) containing those reads; the iterated averaging range is bounded by a geometric sum of the scales, hence by an \(L\)-dependent constant. These classes restrict hereditarily.

Block axial means that the **averaged contour** \(c_b(V;x)=V(y_b,x)\) equals \(I\) for all sites assigned to block \(b\), not that links on a tree equal \(I\). SA 7178 distinguishes these gauges. Means and logarithms use the actual regular analytic branches.

**Outstanding — all-core representatives.** R4, and the additional R5–R6 conditions defining SA's hereditary core, do not imply Rep. From \(\mathcal U_k^\circ(Y)\subset\mathrm{R4}(Y)\) one cannot infer \(\mathcal U_k^\circ(Y)\subset\mathcal K(Y)\). Gauge invariance required of activities at SA 5729–5736 does not prove that this non-covariant soft-gauge precision, its local Gaussian functional and its assigned carriers descend to every core triple. A representative/descent theorem must establish existence, preservation of all domains, and restriction/overlap compatibility. None is supplied here. Taking a supremum over \(\mathcal K\) does not yet bound the intended supremum over every core.

The following are imports, with their library qualifications retained.

* **R (global real gap).** Pr-lay §2: on every admitted separated sequence, every global real \(U\) in this block-axial representative with real bound \(<a_R\) has real symmetric precision \(\mathsf A(P_0)\ge c_LI\). This is the conditional a2-layers theorem, retaining its flat inputs, a2-curved coefficient inputs and [a2-layers-gate](../gates/a2-layers-gate.md) cap/separation repairs. It does not require criticality.
* **W (primitive complex inverse/walk package).** Use [h-walk](h-walk.md) (I1)–(I3), Lemma U and the algebraic precision decomposition, **with** [h-walk-gate](../gates/h-walk-gate.md) §§5–8: complex inverse/conjugation bounds on every separated cut-down, arbitrary coefficient bound \(\sup_c\xi_c^3|j_c|\le\gamma_j\), the all-scale absolute row/column bound for \(\Delta^{(2)}[j]\), and bounded analytic finite-stencil one-step maps. The four inverse bounds alone do not supply the second-jet commutator bound. Use smooth pillar cutoffs with two controlled differences in the graph norm. Retain \(C_*^{n+\sum m_i}\) in the branched estimate and the count \(C_h^{m+1}\) at length \(m\ge0\). Reject h-walk's region-trace canonicity and single-term reflection claims. At global pairs the resulting fixed-region expansion sums to the actual symmetric precision (7) of pr-lay, below a ceiling \(a_h>0\).
* **AV (actual averaging).** The contour mean and nonlinear average are SA QC1–QC4, 7943–8001, on their regular branches, with the finite-stencil analyticity just named. Their nonlinear covariance is proved in Lemma 3; it is not identified with h-walk (I2), which literally states covariance of derivative rows.
* **FG/UM.** The finite-dimensional implication FG1–FG12, SA 13894–14249, and the UM potential, cutoff and geometric counting inputs, SA 14276–14811. For early \(K\ge1\) there are dimension-independent \(A_K,\varepsilon_0(K),\zeta_0(K)>0\) such that the normalized marginal with \(D=C+C\Gamma\Gamma^{\mathsf T}C\) costs \(e^{A_K(\varepsilon+\zeta)m}\). Failed tests use disjoint coordinate blocks, fixed real cutoff sets and the extra tilt in Corollary 13.1. Actual potentials must satisfy UM1 and its joint holomorphy/locality clauses on the entire external domain used and their declared fluctuation boxes. For an application over all of \(\mathcal K\), this is an explicit additional domain hypothesis; it is not inferred from the matrix construction.
* **G-ID (physical clause only).** At an admitted complete physical pair the Gaussian part of the actual step has covariance \(\mathsf A(P_W)^{-1}\). SA 14108–14118 sketches this identification; pr-lay (9) retains physical-current and background-branch identities. This is not TP1's different, still imported, Gaussian-energy identification.

The precision in this manuscript is exactly pr-lay (7), including its active injection, pivot derivative, Wilson/current corrections and ambient soft-gauge Hessian. If the physical step instead uses its completed form (9), **F** is additionally required: the local analytic symmetric correction \(-E_{\rm free}[J_{\rm GF}]\) vanishes at \(P_0\), has fixed full read range and entries \(\le C_Fr(P)\). Add those entries as labels before making any choices below; enlarge all dependent constants. No identification of the two physical Hessians is presumed.

All imported constants/floors are uniform in depth, volume, region shape and larger admitted layer gaps. Preserve frozen IN1's internal order: first its geometric, flat and local analytic data and rates; then \(M_1,R_1,\rho_{\rm lay}\) and their floors; then the resulting R/W constants. The constants in (4), (7), (12)–(13), (22), and Lemma 4's localization scales are fixed **before \(\kappa\)**, independently of \(M,\bar\kappa\). FG constants and \(W_0\) follow them and still precede \(\kappa\); then choose rates, \(\bar\kappa\), \(M\) above floors, and finally radii and the coefficient-ratio tube. Conditions (23)–(24) are these later floors and ceilings. A smaller final coupling ceiling may supply the radii; it does not redefine an early constant.

## 2. Local walk coefficients

**Lemma 1 (local, fixed-region walk bounds).** Under W, after its early \(M_1,R_1\) floors, the precision has a transpose-symmetric labelled family \(a_\omega(P)_{xy}\), with fixed connected full read hulls \(H_\omega\) containing both endpoints. Whenever \(H_\omega\subset Y\), it is defined directly at \(P\in\mathcal R_{\rm loc}(Y;\alpha)\), \(\alpha<a_h\), holomorphic in \(A',\mathbf J\) at fixed \(U\), real at real data and equal to the global coefficient if an admitted extension exists. There are early \(R_h,W,\mu_W>0\), \(W\ge\max(1,c_L)\), and field-independent majorants \(m_\omega(x,y)\) such that
\[
 |a_\omega(P)_{xy}|\le m_\omega(x,y),\qquad
 \max\left\{\sup_x\sum_{y,\omega},\sup_y\sum_{x,\omega}\right\}
       e^{\mu_W t_\omega}m_\omega(x,y)\le W.                         \tag{4}
\]
Here \(t_\omega\ge d(x,y)\) is the infimum of physical tree lengths through the endpoints meeting the non-root cells; \(H_\omega\subset N_{R_h}(T)\) for every such tree \(T\). The root cell is within \(R_h\) of the supported left endpoint. Fixed joining/read margins are included in \(R_h=O_L(M_1)\).

*Proof.* A local model at cell \(\kappa\) uses h-walk Lemma C's separated cut-down \(\Omega^\kappa\subset\kappa^{(4)}\). Its layer index is no larger than the original one, so curvature, potential, derivative and current bounds weaken. A natural cube in a cut-down layer \(i\) lies in the original two-layer zone \(i_0,i_0+1\); if \(i\le i_0\), its side is at most \(c_gM'\xi_i\le c_gM_1\xi_{i_0}\), and the original gauge bound at \(\xi_{i_0}\) implies that at \(\xi_i\). The only other case is the unchanged top layer. Thus C1–C4 admit each cut-down using only data on its full box. C5's false assertion about region traces is unnecessary for fixed regions.

The unfolded inverse is a finite sum of words with at most 25 primitive inverse factors. Conjugation in W yields exponential decay between pillar-supported source and target. For the site graph norm, use smooth \(\chi\) and
\[
 A_s(\chi\lambda)=\chi A_s\lambda+[A_s,\chi]\lambda,\qquad
 \|[A_s,\chi]\lambda\|\le C(\|m^{-1}D\lambda\|+\|m^{-2}\lambda\|).
\]
The identity \(A_sG'f=f\) controls its last graph component; duality gives the transpose. Two controlled differences of \(\chi\), rather than nonsmooth exponential conjugation of the graph norm, justify localization. Summing intermediate pillars spends part of the rate; the convergent pillar-volume sum is part of W's separation floors. This proves the h-walk Lemma L bound on each admitted cut-down without a global inverse at \(P\).

Parametrix coefficients are finite products of these inverses, cutoffs and their commutators. Each commutator costs \(C/M_1\); the absolute second-jet row/column premise controls averaging vertices. In a transposed multiplier term the physical pairing contributes \(\xi_c^3\xi_c^{-4}\xi_c=1\). Its normalized current bound is therefore \(C\gamma_0\), without a depth factor. The zero-length multiplier \(j^{(0)}\) supplying a trunk inverse reads additional local-model boxes. Include every such box: it meets the coefficient row, hence lies within \(O_L(M_1)\) of the trunk cell. Omitting them would make locality false.

For a decorated tree with \(n\) trunk transitions, \(v\) vertices and branch lengths \(m_i\ge1\), retain \(C_*^{n+\sum m_i}\). The inverse-scale power is \(p=n-v+\sum m_i\), while its counted size is \(q=n+\sum(m_i+1)\). Thus
\[
 3p-q=2(n-v)+2\sum_i(m_i-1)\ge0.
\]
Join branches to the trunk at their overlapping stencils. Their tree length consumes part of the decay, leaving a rate for all intermediate-pillar sums. This gives
\[
 |A_\omega(x,y)|\le C_h(C_hM_1^{-1/3})^{|\omega|}
              e^{-\delta_hD(\omega;x,y)}.                         \tag{5}
\]
These are bounds on each product, not consequences of summing to a global inverse. On the depth-\(k\) sequence all scales are at most one, so \(D\ge t_\omega\). At a fixed endpoint there are boundedly many roots; reverse the multiplier branch when that term is re-rooted. The repaired count is \(C_h^{m+1}\). With \(C_h^2M_1^{-1/3}\le1/2\), spend half of (5)'s exponent on length and half on endpoint summation, using (1). This proves (4) with fixed \(\mu_W\le\delta_h/2\), enlarged constants absorbing the root margin.

Take uncut read boxes, actual stencils, endpoints and fixed joining paths as \(H_\omega\); they are connected and satisfy the radius bound. Do not intersect this geometric hull with \(\Omega_0\). For entrywise transpose partners use the same enlarged hull and half the coefficient plus half its transpose. The total symmetric precision is unchanged, and the two-sided majorant is preserved. Holomorphy follows factorwise from W and by normal convergence. No extension of the local triple was used. \(\square\)

**Lemma 2 (conversion and complex displacement).** If \(c_gM_1\le C_{\rm box}M\), a triple in \(\mathcal K(Y)\) belongs to \(\mathcal R_{\rm loc}(Y;\alpha)\) for
\[
 \alpha_0>L^2(1+C_{\rm pot}M)a_0,\quad \alpha_1>L^2a_1,\quad
 \alpha_J>L^3j_0,\qquad r_Y(P)\le L^3(a_1+j_0).                      \tag{6}
\]
Set, early,
\[
 h=\min(a_R,a_h,1/2),\quad H_1=16L^2W/h,\qquad
 r_{\rm loc}=\min\{h/(16L^2),c_L/(8H_1)\}.                          \tag{7}
\]
If \(U\) has local real bound \(<h/2\), the line \(P_z=(U,zA',z\mathbf J)\) is in the local regular class below \(h\) for \( |z|<h/(8L^2r)\), \(r=r_Y(P)>0\). For \(r<r_{\rm loc}\) and every subfamily of readable labels, its weighted absolute displacement sum is at most \(H_1r\), and so is its operator displacement.

*Proof.* Since \(l\le L\), scaling R4's inequalities and gauge bounds proves (6); the cube-size floor makes the gauge cubes eligible. At a plaquette of scale \(\xi\), let \(\alpha\) be the maximum of \(\xi|zA'|\) on its links and \(\xi^2|\nabla^U(zA')|\) on its forward-curl differences. Adjacent scales differ by at most \(L\), so \(\alpha\le L^2|z|r\). Transport its four potentials by real links. Their signed sum is the covariant curl plus a term bounded by \(4\epsilon_{\rm lat}|\partial U-I|\alpha/\xi\). The product-exponential remainder is at most \(16\epsilon_{\rm lat}^2\alpha^2/\xi^2\), since \(e^t-1-t\le t^2\) for \(t\le1\). Thus, for \(\alpha\le1/16\) and real bound \(r_0\le1/4\),
\[
 \epsilon_{\rm lat}^{-2}\xi^2|\partial\mathbf U_z-\partial U|
 \le2\alpha+4r_0(\epsilon_{\rm lat}/\xi)\alpha+16\alpha^2\le4\alpha.
\]
The claimed disc has \(\alpha<h/8\); real gauges are unchanged. Schwarz applied to \([a_\omega(P_z)-a_\omega(P_0)]/(2m_\omega)\) gives \(16L^2m_\omega r/h\) at \(z=1\). Sum (4). If \(r=0\), the displacement is zero. \(\square\)

## 3. The local gap

**Lemma 3 (box extension in the correct axial convention).** Let \(B^+\) be an embedded rectangular box that is a union of next-level blocks, with room for its unit neighbourhood. Suppose \(U\) has a real gauge \(U^g=e^{i\epsilon_{\rm lat}A}\) there with \( |A|,|\nabla A|\le\alpha\le1/16\), and Rep holds on its blocks whose averaging reads lie in \(B^+\). Let \(F\) be their union. There is a global real block-axial field \(\widetilde U\), agreeing with \(U\) on bonds with endpoints in \(F\), with real bound at most \(8L^2\alpha\).

*Proof.* For positive direction \(\mu\), clamp base points to the rectangular set \(B^+_\mu\) on which the whole \(\mu\)-bond lies in \(B^+\). Let \(\pi_\mu\) be that clamp and \(\chi(x)=(1-\operatorname{dist}_\infty(x,B^+))_+\). Set \(A_\mu^{\rm ext}(x)=\chi(x)A_\mu(\pi_\mu x)\), zero outside the embedded neighbourhood. Neighbouring clamped points are equal or neighbouring. Hence \( |A^{\rm ext}|\le\alpha\), \( |\nabla A^{\rm ext}|\le2\alpha\). At a plaquette the linear exponential term is a curl bounded by \(4\epsilon_{\rm lat}^2\alpha\), and the remainder by \(16\epsilon_{\rm lat}^2\alpha^2\). Thus \(U'=e^{i\epsilon_{\rm lat}A^{\rm ext}}\) has defect at most \(5\epsilon_{\rm lat}^2\alpha\). Extend \(g\) arbitrarily as a real site gauge and gauge \(U'\) back, obtaining \(U''=U\) on \(B^+\).

Nonlinear covariance follows from the actual averaging formula. Every path transport transforms by its endpoint gauges. The mean equation \(\sum_i\log(T_iT^{-1})=0\) is conjugated at its initial endpoint; uniqueness of its regular branch gives the same covariance for its solution. In QC3 the closed products and logarithms conjugate at the block centre; the final straight transport supplies the second endpoint. Therefore
\[
 \mathcal M^k(U^u)=(\mathcal M^kU)^{u|_{\text{level-}k\text{ sites}}},\qquad
 c_b(V^v;x)=v(y_b)c_b(V;x)v(x)^{-1}.                              \tag{8}
\]
This algebraic identity holds for arbitrary real site gauges; smoothness is unnecessary.

On a block outside \(F\), take \(v(x)=c_b(\mathcal M^kU'';x)\), with \(v(y_b)=I\); on blocks in \(F\), take \(v=I\). Blocks partition the level-\(k\) sites. Lift \(v\) to bare sites by setting it equal to \(I\) elsewhere, and put \(\widetilde U=(U'')^v\). Formula (8) makes the outside blocks axial. Protected blocks have unchanged averaging reads and endpoint gauges \(I\), so remain axial. Bonds inside \(F\) are unchanged. Finally \(\widetilde U\) is gauge equivalent to \(A^{\rm ext}\). Curvature and the witnessing gauges give the real bound \(\max(5L^2\alpha,2L^2\alpha)\le8L^2\alpha\). The embedding condition avoids a periodic clamping seam. \(\square\)

Define the hull-restricted symmetric matrix, extended by zero on unused coordinates,
\[
 \mathsf A^Y(P)=\sum_{H_\omega\subset Y}a_\omega(P).                 \tag{9}
\]
Only surviving terms are evaluated. An undefined coefficient outside \(Y\) is not multiplied by zero.

**Lemma 4 (real local gap and complex short-range gaps).** Choose an early power \(\ell_{\rm IMS}\) of \(L\) and buffer \(b_{\rm tail}>R_h\) such that
\[
 \frac{c_{\rm IMS}W}{\mu_W^2\ell_{\rm IMS}^2}\le c_L/8,\quad
 2We^{-\mu_W(b_{\rm tail}-R_h)}\le c_L/8,\quad
 c_{\rm IMS}=16\cdot400^2\cdot4/e^2.
\]
Put \(b_{\rm gap}=2\ell_{\rm IMS}+b_{\rm tail}+r_{\rm av}+4L\). Impose the later size and real-radius conditions
\[
 2\ell_{\rm IMS}+2b_{\rm gap}\le C_{\rm box}LM,\qquad
 L^2(1+C_{\rm pot}M)a_0<h/16.                                      \tag{10}
\]
If \(P\in\mathcal K(Y)\), \(N_{b_{\rm gap}}(S)\subset Y\), and \(\chi_S\) projects onto coordinates based in \(S\), then
\[
 \chi_S\mathsf A^Y(P_0)\chi_S\ge3c_L/4,\qquad
 \operatorname{Re}\chi_S\mathsf A^Y(P)\chi_S\ge5c_L/8
       \quad(r_Y(P)<r_{\rm loc}).                                \tag{11}
\]
If \(\mathsf A_<^Y\) retains only labels with \(t_\omega\le r_c\), where \(We^{-\mu_Wr_c}\le c_L/8\), its same compression has real part at least \(c_L/2\), and norm at most \(W\).

*Proof.* Use tensor-product tents centred on the \(\ell_{\rm IMS}\)-grid, normalized to \(\sum_c h_c^2=1\). Their supports are cubes \(Q_c\) of side \(2\ell_{\rm IMS}\). The sum of squares of the unnormalized tents is between \(1/16\) and \(1\). Product and quotient differences give \( |h_c(x)-h_c(y)|\le400d(x,y)/\ell_{\rm IMS}\); at most 32 indices contribute at either of two sites. The exact identity
\[
 \mathsf A^Y=\sum_c h_c\mathsf A^Yh_c+\tfrac12\sum_c[h_c,[h_c,\mathsf A^Y]]
\]
has double-commutator norm at most \(c_{\rm IMS}W/(\mu_W^2\ell_{\rm IMS}^2)\), by (4) and \(\sup_{t\ge0}t^2e^{-\mu_Wt}=4/(e^2\mu_W^2)\).

For \(Q_c\) meeting \(S\), round its \(b_{\rm tail}+r_{\rm av}+2L\) neighbourhood outward to next-level blocks. The resulting box lies in \(Y\) and has the size allowed in (10). Its R4 gauge has \(\alpha<C_{\rm pot}Ma_0<h/(16L^2)\). Lemma 3 extends its protected interior to a global axial field of real bound \(<a_R\), agreeing with \(U\) on \(N_{b_{\rm tail}}(Q_c)\). Apply R there. A label contributing to the difference of the compressions on \(Q_c\) must leave that matching neighbourhood, so its tree length is at least \(b_{\rm tail}-R_h\). The two tails cost at most \(c_L/8\). Each localized vector \(h_cv\) therefore has gap \(7c_L/8\); summing and paying the IMS loss gives \(3c_L/4\). This compares fields in the **same representative** on matching reads, without covariance of the soft-gauge Hessian.

Lemma 2 loses at most \(H_1r\le c_L/8\), giving \(5c_L/8\). Deleting the long-label tail loses at most \(We^{-\mu_Wr_c}\le c_L/8\). Bound (4) gives the norm. For a whole-torus support use R directly, with the same weaker constants. \(\square\)

## 4. The locally defined inverse-root series

For this section the working domain \(\mathcal W(Y)\) consists of real \(U\) obeying Rep and the local gauge/curvature bounds used in Lemma 4, and complex data with \(r_Y(P)<r_{\rm loc}\). It does not impose R5–R6, nor require a global extension. Its fixed-\(U\) fibres are open and contain every \(P_z\) with \(|z|r_Y(P)<r_{\rm loc}\). This open working domain, not a closed radius inequality, is the holomorphy domain.

For a labelled family \(B_\alpha(x,y)\) of lengths \(t_\alpha\ge d(x,y)\), define its absolute weighted Schur norm by the maximum of the row and column sums of \(e^{\theta t_\alpha}|B_\alpha(x,y)|\). In a product keep the intermediate coordinate and both labels, add their lengths and unite their hulls. The weighted norms multiply, by the two Schur sums. Shared endpoints join the hulls.

Choose, in order, the following early constants:
\[
 a_s=c_L/2,\quad b_s=W,\quad
 \Lambda_{\rm res}=2b_s^2/a_s,\quad
 q_*=\left(1-\frac{3a_s^2}{4b_s^2}\right)^{1/2}<1,
\]
\[
 p_{r_c}=16n_cr_c^4\sum_{j\ge0}(j+1)^4q_*^{j/2}.                    \tag{12}
\]
Choose integer \(r_c\ge1\) so
\[
 We^{-\mu_Wr_c}\le c_L/8,\qquad
 We^{-\mu_Wr_c/2}p_{r_c}/\Lambda_{\rm res}\le1/4;
\]
then set \(\theta=\min(\mu_W/2,-\log q_* /(2r_c))\), and choose integer \(n\ge1\) so
\[
 n_c(2nr_c+1)^4q_*^{n/2}\le1/4.
\]
These choices exist because an exponential dominates a fixed polynomial. Finally set
\[
 R_*=nr_c+r_c+R_h+b_{\rm gap},\qquad U_{\rm root}=2p_{r_c}/\sqrt{\Lambda_{\rm res}}. \tag{13}
\]

**Theorem 5 (local grouped root).** On \(\mathcal W(Y)\) there is a labelled series \(\sum_{\alpha:H_\alpha\subset Y}r_\alpha(P)\) with connected full read hulls, each within \(R_*\) of its length-\(t_\alpha\) tree, such that its field-independent absolute \(\theta\)-moment is at most \(U_{\rm root}\). Terms are local, holomorphic at fixed \(U\), and real at real data. For \(r_Y(P)\le r_{\rm loc}/2\),
\[
 \left\|\sum_{\alpha:H_\alpha\subset Y}
           (r_\alpha(P)-r_\alpha(P_0))\right\|
 \le 2U_{\rm root}\,r_Y(P)/r_{\rm loc}.                             \tag{14}
\]
On the whole torus its sum is the principal symmetric root \(\mathsf A(P)^{-1/2}\).

*Proof.* Split precision labels into \(t_\omega\le r_c\) and the long family \(E\). For \(t\ge0\), form the **grouped entries**
\[
 N_t=\frac{\Lambda_{\rm res}I-\mathsf A_<}{\Lambda_{\rm res}+t},\quad
 P_t=\frac1{\Lambda_{\rm res}+t}\sum_{j=0}^{n-1}N_t^j,\quad Q_t=N_t^n. \tag{15}
\]
An entry of these polynomials is evaluated from its coordinate paths, using the normally convergent short-label entry sums. It is not a polynomial in finitely many walk labels. Group before assigning a tag. Assign to a \(P_t\) or \(Q_t\) entry the union of the radius-\(R_*\) endpoint balls and length \(d(x,y)\), the \(\ell^\infty\) distance; trees in Lemma 6 and the crossing bound are measured in the same \(\ell^\infty\) metric. The balls are connected because \(d(x,y)\le nr_c\). Every path and every short coefficient it reads lies inside these balls.

To bound such an entry using only its hull, compress \(\mathsf A_<^Y\) to the radius-\(nr_c\) coordinate ball about its first endpoint. The hull supplies the \(b_{\rm gap}\) margin. Lemma 4 gives accretivity \(a_s\) and norm \(b_s\) on that compression. For every vector \(v\),
\[
 \|(I-\mathsf A_</\Lambda_{\rm res})v\|^2
 \le(1-2a_s/\Lambda_{\rm res}+b_s^2/\Lambda_{\rm res}^2)\|v\|^2
 =q_*^2\|v\|^2.
\]
Coordinate paths of at most \(n\) short steps cannot leave this ball. Hence their grouped entry satisfies
\[
 |N_t^j(x,y)|\le
 \left(\frac{q_*\Lambda_{\rm res}}{\Lambda_{\rm res}+t}\right)^j
 1_{\{d(x,y)\le jr_c\}}\quad(0\le j\le n).                         \tag{16}
\]
Use (1), \(e^{\theta jr_c}q_*^j\le q_*^{j/2}\), and
\((2jr_c+1)^4\le16r_c^4(j+1)^4\). The resulting pair-independent entry majorants give
\[
 |P_t|_\theta\le\frac{p_{r_c}}{\Lambda_{\rm res}+t},\quad
 |Q_t|_\theta\le1/4,\quad |E|_\theta\le We^{-\mu_Wr_c/2}.             \tag{17}
\]
These inequalities remain true when only readable hulls are kept: they bound each grouped entry before summation. No positivity of a cut matrix away from these interior balls was used.

Let \(K_t\) be the labelled union of \(Q_t\) entries and products \(-EP_t\), and let \(\mathcal R_\alpha(t)\) be the products in \(P_t\sum_{m\ge0}K_t^m\), retaining the intermediate coordinates. Equations (12), (17) give \(|K_t|_\theta\le1/2\), so the absolute moment is at most \(2p_{r_c}/(\Lambda_{\rm res}+t)\). Hulls are unions of connected factor hulls with shared endpoints; their trees concatenate and have additive length. Define
\[
 r_\alpha(P)=\frac1\pi\int_0^\infty t^{-1/2}\mathcal R_\alpha(t;P)\,dt. \tag{18}
\]
The scalar substitution \(t=\Lambda_{\rm res}u^2\) gives
\(\int_0^\infty t^{-1/2}/(\Lambda_{\rm res}+t)\,dt=\pi/\sqrt{\Lambda_{\rm res}}\).
Tonelli proves the claimed absolute majorant; uniform integrable bounds on compact parameter sets prove holomorphy. Schwarz on \(|z|<r_{\rm loc}/r_Y(P)\) applied termwise proves (14).

On the whole torus, \((\mathsf A+t)P_t=I-Q_t+EP_t=I-K_t\). Thus the resolvent series equals \((\mathsf A+t)^{-1}\). Lemma 4 gives its right-half-plane spectrum. The scalar identity \(z^{-1/2}=\pi^{-1}\int_0^\infty t^{-1/2}(z+t)^{-1}dt\) for \(\operatorname{Re}z>0\) follows first for real \(z>0\) by the same substitution, then by holomorphy. Differentiating this identity for the finite Jordan blocks proves the matrix identity. Since \(\mathsf A^{\mathsf T}=\mathsf A\), its root is symmetric. \(\square\)

## 5. Tags and the matrix envelope

For each full read hull \(H_\alpha\), tag it once by each coarse cube it meets:
\[
 s^{H_\alpha}=\prod_{\Delta:\Delta\cap H_\alpha\ne\varnothing}s_\Delta.
                                                                    \tag{19}
\]
Fix a coarse union \(Z\supset H=Z_0^\sharp\). Set \(s=1\) on \(H\), \(|s_\Delta|<e^{\bar\kappa}\) on \(Z\setminus H\), and \(s=0\) off \(Z\). Define \(s^0=1_H\). Keep only hulls contained in \(Z\), then evaluate their coefficients. With the two independently tagged series define
\[
 \mathsf A(s;P)=\sum_\omega s^{H_\omega}a_\omega(P),\quad
 \mathsf r(s;P)=\sum_\alpha s^{H_\alpha}r_\alpha(P),\quad
 C=(\chi\mathsf A(s)\chi)^{-1},\quad
 \Gamma=-\chi\mathsf A(s)(1-\chi)\mathsf r(s).                       \tag{20}
\]
The inverse acts only on \(I_0\). References are
\[
 C_*=(\chi\mathsf A^H(P_0)\chi)^{-1},\qquad
 \Gamma_*=-\chi\mathsf A^H(P_0)(1-\chi)\mathsf r(s^0;P_0).            \tag{21}
\]
In dimension zero the functional is evaluation at the empty vector and equals one on \(1\).

**Lemma 6 (tag counting and collar crossing).** If a hull lies within radius \(R\) of a connected tree of length \(t\), and \(LM\ge8R\), it meets at most \(16+128t/(LM)\) coarse cubes. If a labelled product starting in \(Z_0\) has a hull leaving \(H\), its total length is at least \(M-R_*\). A nearest-neighbour connected surviving hull lies in one wall-component of \(Z\); a corner-connected selected fine domain lies in one wall-component of \(H\).

*Proof.* Traverse the tree twice and divide the tour into at most \(1+8t/(LM)\) pieces of length at most \(LM/4\). A piece thickened by \(R\) has coordinate diameter at most \(LM/2\), so meets at most two grid intervals per coordinate, or 16 cubes. Approximate the infimum defining length. A leaving point is at distance at least \(M\) from the starting support and within \(R_*\) of the connected product tree, proving the crossing bound. Nearest-neighbour steps change the coarse cube index in at most one coordinate, so stay in one wall-component. The corner collar contains the coordinate-wise wall path between any two touching fine cubes. \(\square\)

Choose the following early constants, after (13):
\[
 \begin{split}
 K_0&=1+\frac4{3c_L}+W+WU_{\rm root},\qquad b=32,\qquad d=\theta/4,\\
 H_0&=\frac8{3c_L^2}(W+H_1)+WU_{\rm root}
          +U_{\rm root}H_1+\frac{2WU_{\rm root}}{r_{\rm loc}},\\
 C_\tau&=4/c_L+K_0+1,\qquad H_p(M)\equiv L^3 .
 \end{split}                                                       \tag{22}
\]
After \(\bar\kappa>\log2\), choose the power \(M\) of \(L\) above all earlier floors and
\[
 \begin{gathered}
 M\ge\max(2R_*,b_{\rm gap},\ell_{\rm IMS}),\quad LM\ge8R_*,
 \quad c_gM_1\le C_{\rm box}M,\quad
 \frac{128\bar\kappa}{LM}\le\theta/2,\\
 2\ell_{\rm IMS}+2b_{\rm gap}\le C_{\rm box}LM,\qquad
 E_M:=e^{32\bar\kappa-dM},\quad WE_M\le c_L/8,\quad H_0E_M\le1/2 .
 \end{gathered}                                                     \tag{23}
\]
Choose the later radii and tube so
\[
 L^2(1+C_{\rm pot}M)a_0<h/16,\qquad
 L^3(a_1+j_0)<\min(r_{\rm loc}/2,1/(2H_0)),\qquad |\tau-1|\le1/2.     \tag{24}
\]

**Theorem 7 (main matrix statement).** Assume R, W, AV, the fixed geometry and (23)–(24), and \(P\in\mathcal K(Z;a_0,a_1,j_0)\). The matrices defined by (19)–(21) exist on every independent coarse disc \(|s_\Delta|<e^{\bar\kappa}\), are jointly holomorphic at fixed \(U\), and \(C=C^{\mathsf T}\). Their references are real, \(C_*>0\), and
\[
 \|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0,\qquad
 \operatorname{Re}C^{-1}\ge c_L/2,\qquad \|C\|\le2/c_L.              \tag{25}
\]
For \(C_\tau^{\rm mat}=\tau^{-1}C\), \(\Gamma_\tau=\tau^{1/2}\Gamma\), with the root near one,
\[
 \|C_\tau^{\rm mat}-C_*\|+\|\Gamma_\tau-\Gamma_*\|
 \le H_0\{e^{b\bar\kappa-dM}+L^3(a_0+a_1+j_0)\}
                  +C_\tau|\tau-1|.                               \tag{26}
\]
Thus the numerical clause of frozen IN1 H-M holds for this family on \(\mathcal K\), with all five envelope constants fixed before \(\kappa,M,\bar\kappa\).

*Proof.* Lemma 4 on the collar gives \(\|C_*\|\le4/(3c_L)\); (4) gives \(\|C_*^{-1}\|\le W\), and Theorem 5 gives \(\|\Gamma_*\|\le WU_{\rm root}\). For a single tag, Lemma 6 bounds its modulus by \(\exp(16\bar\kappa+\theta t/2)\); a product of the two independently tagged families costs \(\exp(32\bar\kappa+\theta(t_1+t_2)/2)\). A varied term has reference tag zero and total length at least \(M-R_*\ge M/2\). Spending the remaining half-moment gives
\[
 \|\chi(\mathsf A(s;P)-\mathsf A(s^0;P))\chi\|\le WE_M,\qquad
 \|\Gamma(s;P)-\Gamma(s^0;P)\|\le WU_{\rm root}E_M.                 \tag{27}
\]
The same positive majorants justify convergence on closed subdiscs and even at the displayed radius. This count needs the exponent 32 because \(\Gamma\) has two tag sets; it is not shown to be necessary.

Put \(r=r_Z(P)\). Lemma 2 and (27) give
\(\|C^{-1}-C_*^{-1}\|\le WE_M+H_1r\le c_L/4\).
This proves (25) and, by the inverse identity,
\[
 \|C-C_*\|\le\frac8{3c_L^2}(WE_M+H_1r).
\]
At \(s^0\) add and subtract the real \(X_0=\chi\mathsf A^H(P_0)(1-\chi)\). The two field changes cost
\[
 \|\Gamma(s^0;P)-\Gamma_*\|
 \le U_{\rm root}H_1r+2WU_{\rm root}r/r_{\rm loc}.
\]
Together these prove a bound \(H_0(E_M+r)\le1\). In particular \(\|\Gamma\|\le K_0+1\). For \(|\tau-1|\le1/2\),
\[
 |\tau^{-1}-1|\le2|\tau-1|,\qquad
 |\tau^{1/2}-1|\le|\tau-1|,
\]
so scaling costs at most \((4/c_L+K_0+1)|\tau-1|\). Use (6); adding the harmless \(a_0\) term yields (26). Holomorphy follows from the coefficient series and inversion of the accretive compression. Symmetry follows from the transpose-paired precision labels. \(\square\)

## 6. Structural clauses and exact scope

For \(\iota=(\mathbf D,P_{\rm fail})\), let \(\mathbf D\) be a selected finite set of tagged potential domains. Let \(Y_{\rm box}\) be the union of their bond sets requiring a fluctuation box, and \(P_{\rm fail}\) a set of distinct failed bonds outside \(Y_{\rm box}\). Precisely as in SA UM2, use
\[
 F_\iota=(-1)^{|P_{\rm fail}|}\chi_{Y_{\rm box}}
       \prod_{b\in P_{\rm fail}}(1-\chi_b)
       \prod_{Y\in\mathbf D}(e^{V(Y)}-1),\qquad
 \chi_b=1_{\{|B(b)|<\mathfrak b\}} .
\]
Here \(\chi_{Y_{\rm box}}=\prod_{b\in Y_{\rm box}}\chi_b\). Set the integrand to zero outside this product, before evaluating box-only potentials. Its complete fine support is the \(Z_0\) of (20). This is the imported integrand, with its failed-bond index distinguished from the reference field \(P_0\). The empty selection contributes only the leading one.

**Theorem 8 (the localized functional).** Assume Theorem 7 and FG/UM. Require, in addition, that the right side of (26), denoted \(\varepsilon\), satisfies \(\varepsilon\le\varepsilon_0(K_0)\). Define
\[
 D=C_\tau^{\rm mat}+C_\tau^{\rm mat}\Gamma_\tau\Gamma_\tau^{\mathsf T}C_\tau^{\rm mat},
 \qquad
 \mathcal J[F]=\int_{\mathbb R^{I_0}}F(b)\,
   \frac{e^{-b^{\mathsf T}D^{-1}b/2}\,db}
        {(2\pi)^{|I_0|/2}(\det D)^{1/2}},                           \tag{28}
\]
with determinant branch continued from the positive reference.

1. This is SA's FG4 functional, normalized by \(\mathcal J[1]=1\). Matrices, and integrals of the prescribed holomorphic potentials with allowed quadratic growth, are jointly holomorphic in the fixed-\(U\) fibre and parameter discs; cutoffs remain fixed and real. Coefficients are real at real data.
2. With \(s\) extended by zero, restriction from \(Z'\) to \(Z\subset Z'\) changes none of \(C,\Gamma,D,\mathcal J\), provided both use the same fixed region sequence and supports. Rectangular matrices are compared after padding unused auxiliary columns by zero.
3. If \(Z=\bigsqcup_i Z_i\) is its wall-component decomposition, a component missing \(H\) contributes no parameter dependence. The remaining \(D\) splits into the corresponding diagonal blocks, each constructed from \(Z_0\cap Z_i\) and \(Z_i\). A product integrand splits into the product of its normalized integrals.
4. The local dimension is \(m=|I_0|\le12(LM)^4\#Z\), independently of the auxiliary dimension.
5. The exact finite interpolation identity holds:
\[
 \mathcal J(Z_0;\mathbf1;P)[F_\iota]
   =\sum_{Z\supset H} T(Z,\iota),\qquad
 T(Z,\iota)=
 \prod_{\Delta\subset Z\setminus H}\int_0^1ds_\Delta\,\partial_{s_\Delta}
          \mathcal J(Z_0;s_Z;P)[F_\iota].                          \tag{29}
\]
It is asserted when the complete \(P\) is in this working domain. Components missing \(H\) give zero terms; the other terms factor over wall-components.
6. At a complete pair in this domain, with \(\tau=1\),
\[
 D(\mathbf1;P)=\chi\mathsf A(P)^{-1}\chi.                           \tag{30}
\]
On an admitted complete physical pair, G-ID makes (28) the marginal of the step's actual Gaussian fluctuation law. If the coefficient-ratio convention scales the complete precision by \(\tau\), the covariance in (30) is divided by \(\tau\).

*Proof.* Theorem 7 supplies FG1, so FG6 gives (28), normalization and the dimension-only domination. FG's accretivity estimate supplies a common integrable Gaussian majorant on compact parameter sets for the allowed quadratic tilt. Integrating Cauchy's formula proves joint holomorphy. The explicit smallness condition above is essential; Theorem 7's weaker error bound by one alone does not justify this Gaussian assertion.

Only full hulls contained in \(Z\) survive. Lemmas 1 and Theorem 5 evaluate them entirely from the restricted data, proving heredity. Every surviving hull is connected. A precision entry touching \(I_0\) and every product in \(\Gamma(x,z)\) therefore lie in the component of \(\hat x\). Two such products sharing \(z\) must be in the same component, so \(\Gamma\Gamma^{\mathsf T}\) and \(D\) are block diagonal. The collar operation preserves unions, and each individual fine cube's collar is wall-connected; hence \((Z_0\cap Z_i)^\sharp=H\cap Z_i\). Selected corner-connected domains cannot cross components by Lemma 6. The positive-reference determinant branches factor, as do the densities and mixed derivative integrals. Unused components have identically zero mixed derivatives. Counting at most 12 coordinates per site proves the dimension bound. Iterating the one-variable fundamental theorem of calculus on the finite cube \([0,1]^{\Lambda\setminus H}\) proves (29); the UM Mayer identity and fixed cutoff expansion use their specified finite local integrands.

For (30), at all ones the precision series sums to \(\mathsf A\), and Theorem 5 gives the symmetric root \(R=\mathsf A^{-1/2}\). In blocks relative to \(I_0\sqcup I_0^c\), write \(\mathsf A=\left(\begin{smallmatrix}a&\beta\\\beta^{\mathsf T}&\delta\end{smallmatrix}\right)\). Then
\[
 C=a^{-1},\quad \Gamma=-\beta R_{2\cdot},\quad
 \Gamma\Gamma^{\mathsf T}=\beta(\mathsf A^{-1})_{22}\beta^{\mathsf T}.
\]
The Schur complement \(\sigma=\delta-\beta^{\mathsf T}a^{-1}\beta\) is invertible, with \((\mathsf A^{-1})_{22}=\sigma^{-1}\). Block inversion gives
\[
 (\mathsf A^{-1})_{11}=a^{-1}+a^{-1}\beta\sigma^{-1}\beta^{\mathsf T}a^{-1}=D.
\]
This proves the matrix identity. Only G-ID identifies this precision with the physical step. Direct substitution in (28) gives \(D_\tau=\tau^{-1}D\). \(\square\)

**Outstanding — actual-family and stage interfaces.** Theorems 7–8 specify a replacement decoupling with the required identities on \(\mathcal K\); they do not identify its coefficients at \(s\ne\mathbf1\) with another assigned expansion. To consume it as frozen IN1 H-M, the actual construction must use these full-read carriers, and its whole declared local domain must be admitted to the representative class or supplied with a compatible descent theorem. For the physical clause, pr-lay Theorem 8's global regularity and a small \(r(P_W)\) alone do not imply the stronger real-gauge ceiling (10); full membership in the present working domain and G-ID are required.

The assembly's PR1 and [ci-form](ci-form.md) H-D/H-G/H-S retain those application obligations. Neither frozen [p82](p82.md), frozen [tp1](tp1.md), nor the retained records and proposed domain repairs of [st1-r2](st1-r2.md) and [st1-draft3](st1-draft3.md) establish this admission or the representative interface. No assertion here changes those notes or their status.

## 7. The two counterexamples

**Proposition 9 (what IN1's three-site example establishes).** The example in frozen IN1 Lemma 2 remains a counterexample to heredity of its auxiliary path-weighted family. It is not a counterexample to full-read tagging; the two families need not agree off \(s=\mathbf1\).

*Proof.* In the example \(A=I-T\), \(T_{12}=t\), \(T_{23}=u\), the local coordinate is 1, the collar is \(\{1,2\}\), and site 3 is cut. The global root has
\[
 ((I-T)^{-1/2})_{22}=1+\tfrac38(t^2+u^2)+O((|t|+|u|)^4).
\]
Also \(R_{21}=t/2+O((|t|+|u|)^3)\). The path-weighted construction gives
\[
 D_{\rm path}=1+t^2(R_{21}^2+R_{22}^2)
       =1+t^2+t^4+\tfrac34t^2u^2+O((|t|+|u|)^6).
\]
These convergent binomial expansions for small \(t,u\) prove exterior dependence, although the retained root entries have endpoints in the collar. In the full-read construction every coefficient reading edge \(23\) has a hull meeting site 3; its tag is zero. Surviving grouped entries read no \(u\), so neither does their \(D\). This is a coefficient-locality statement, not an application of Theorem 7's quantitative large-collar floors to a three-site lattice. It does not refute IN1's example or equate the two parameter families. \(\square\)

**Proposition 10 (a local R4 triple without an extension at a fixed regularity ceiling).** The draft's constant-on-two-cubes interpolation is incorrect. The following replacement satisfies R4, and for sufficiently small bare mesh has no global extension with the prescribed real-curvature and normalized derivative ceilings. No R5–R6 membership is asserted.

*Proof.* Let \(\ell=LM\) and let \(Z\) consist of the five half-open cubes with lower corners
\[
 0,\quad \ell e_3,\quad \ell(e_1+e_3),\quad
 \ell(e_1+e_2+e_3),\quad \ell(e_1+e_2).
\]
Take a sufficiently large torus, and the constant determining sequence, so the longer scale everywhere is \(L\ge1\). Let
\[
 p=(\ell-\epsilon_{\rm lat},\ell-\epsilon_{\rm lat},0,0),\qquad
 q=(\ell,\ell,0,0).
\]
Let \(d_Z(p,x)\) be nearest-neighbour graph distance, measured in physical length, using only vertices in \(Z\). This graph is connected. Every path from \(p\) to \(q\) goes up to the third-coordinate height \(\ell\) and back, so \(d_Z(p,q)\ge2\ell\). Set
\[
 \varphi(x)=c\max\{-1,1-2d_Z(p,x)/\ell\},\quad
 U=I,\quad \mathbf J=0,\quad A'_3(x)=\varphi(x)X,\quad A'_\mu=0\ (\mu\ne3),
                                                                    \tag{31}
\]
on contained positive bonds, where \(X\) is a Hermitian colour matrix of norm one. Then \(\varphi(p)=c\), \(\varphi(q)=-c\), \(|\varphi|\le c\), and every contained difference is at most \(2c/\ell\). All link exponentials commute. A contained \(3\nu\)-plaquette has holonomy
\(\exp(\pm i\epsilon_{\rm lat}[\varphi(x+\epsilon_{\rm lat}e_\nu)-\varphi(x)]X)\).
Its defect is at most \(2c\epsilon_{\rm lat}^2/\ell\); other plaquettes are trivial. The real gauges are zero. Choose \(c>0\) with
\[
 c<a_1,\qquad 2c/\ell<\min(a_0,a_1).
\]
This verifies **both** real and complex curvature clauses of R4 and all its derivative/gauge clauses. The amplitude can be decreased to fit any positive local ceilings used here.

Suppose an extension has \(|\partial\widetilde U-I|\le r_0\epsilon_{\rm lat}^2\) and \(l^2|\nabla^{\widetilde U}\widetilde A'|\le r_*\), for fixed positive \(r_0,r_*\). Join \(p\) to \(q\) by the two missing bottom links, and close the loop by ascending to height \(\ell\), taking two horizontal links in the bridge cubes, and descending. All links of the latter path lie in \(Z\), with \(U=I\). Two elementary vertical ribbons fill this loop using \(2\ell/\epsilon_{\rm lat}\) plaquettes. Telescoping their unitary, conjugated plaquette products yields, for the bottom transport \(g\),
\[
 |g-I|\le2r_0\ell\epsilon_{\rm lat}.
\]
Two covariant difference steps give
\[
 |cX+\operatorname{Ad}(g)cX|\le2\epsilon_{\rm lat}r_*,
 \qquad
 |cX+\operatorname{Ad}(g)cX|\ge2c(1-|g-I|).
\]
If \(2r_0\ell\epsilon_{\rm lat}\le1/2\) and \(2\epsilon_{\rm lat}r_*<c\), these inequalities contradict one another. Normalized curvature bounds on the constant scale \(L\) are stronger than the real bound used here.

The draft instead prescribed \(+c\) and \(-c\) on the *entire* two bottom cubes. Near their tops they are joined through the bridge by only a few mesh steps, so that prescription cannot have the claimed derivative bound. It also omitted complex curvature when calling \(a_0\) arbitrary. Formula (31) repairs both failures. The conclusion concerns R4 at fixed ceilings, not a full hereditary-core counterexample. \(\square\)

## 8. The UM consequence

**Corollary 13.1 (conditional UM4–UM6, UM14 and early cost one).** Assume the representative-domain hypotheses of Theorems 7–8, UM1's potential and finite-type bounds, the fixed-cutoff and failed-test hypotheses of FG12, and IN1's other rate/count constraints. Then UM4–UM6 hold for the constructed family on every \(P\in\mathcal K(Z)\) within (24); UM5 has \(c_m=12\). There is a positive \(W_0\) fixed before \(\kappa,\bar\kappa,M\), for which the later floors/ceilings give UM14 and \(C_0^{\rm UM}\le1\).

*Proof.* Enlarge the imported \(A=A_{K_0}\), the UM potential-density count \(P_d\), and \(c_m\) to at least one. Put
\[
 D_0=Ac_mL^4,\qquad
 W_0=\min\{[3P_dL^4(1+Ac_m)]^{-1},\,\zeta_0/(2P_d)\}.              \tag{32}
\]
All these choices precede \(\kappa\). After the required rates and \(\bar\kappa\), choose \(M\) satisfying (23) and, with
\[
 \varepsilon_*=\min\{\varepsilon_0,(3D_0M^4)^{-1}\},\qquad
 \gamma_{\rm tilt}=\min\{2/(3D_0M^4),\zeta_0\},
\]
require
\[
 H_0e^{32\bar\kappa-dM}\le\varepsilon_*/2,\qquad
 H_0L^3(a_0+a_1+j_0)+C_\tau|\tau-1|\le\varepsilon_*/2.              \tag{33}
\]
The first is a floor: \(e^{dM}\ge(dM)^5/5!\) proves \(M^4e^{-dM}\to0\). The second is a later radius/tube ceiling compatible with (24). Thus \(\varepsilon\le\varepsilon_*\). In the notation of SA 14373–14401, \(K=K_0\), \(R_s=e^{\bar\kappa}>2\), and \(m\le c_m(LM)^4\#Z\), which are exactly UM4–UM5. FG6/FG12 give UM6,
\[
 |\mathcal J[F]|\le F_*
 \exp\{A(\varepsilon+\zeta+\gamma_{\rm tilt}/2)m
                  -\gamma_{\rm tilt}\mathfrak b^2|P_{\rm fail}|/2\},
\]
for distinct disjoint failed-test blocks, with \(\zeta+\gamma_{\rm tilt}/2\le\zeta_0\). There is no exterior auxiliary-dimension factor.

UM13 gives \(\zeta=P_dW_0M^{-4}\). Hence
\[
 P_dW_0M^{-4}+\gamma_{\rm tilt}/2\le\zeta_0,                        \tag{34}
\]
which is exactly UM14 at SA 14513–14517. Its UM15 cost is
\[
 C_0^{\rm UM}
 =P_dL^4W_0(1+Ac_m)+D_0M^4(\varepsilon+\gamma_{\rm tilt}/2)
 \le\tfrac13+\tfrac13+\tfrac13=1.                                 \tag{35}
\]
The **bound one and \(W_0\)** are fixed early; \(\varepsilon_*,\gamma_{\rm tilt}\) are not. Retain IN1's later failed-bond floor
\(\mathfrak b^2\ge(2/\gamma_{\rm tilt})\{\Theta+\log(4c_b(LM)^4)\}\),
its insertion-smallness premise and its nonempty rate window. Theorem 8 supplies the structural identities separately from this numerical estimate. \(\square\)

This matches [um-novelty](um-novelty.md)'s distinction: SA assumes the actual enlarged-disc matrix and structural inputs, proves UM6 conditionally from FG, and imposes UM14 as a tilt compatibility condition. Neither those passages nor the arithmetic (35) proves admission of every declared complex pair. The draft's assertion that the exact all-core problem of FINISH row 274 has now been supplied is therefore withdrawn.

## Change log (pass 3 fixes, lead, 2026-11-05)

Applied the findings of `gates/hm-gate.md` (Claude fresh session, first failing step none):
1. The source-check record linked at line 7 is not in this clone; the referee read every cited SA line directly.
2. Lemma 2's proof: the missing factor epsilon_lat is restored in 4 epsilon_lat |dU - I| alpha/xi (line 100 already had it).
3. Grouped root entries carry the l-infinity length d(x,y); Lemma 6 and the crossing bound use the same l-infinity metric.
4. The UM range is SA 14276-14811.
5. The exponent 32 is what this count needs, not shown necessary.

**Status: frozen**, as a conditional theorem on R4 intersect Rep. Outstanding, named: the all-core conclusion (descent; `library/descent-draft.md`), G-ID for the physical clause, F for the completed gauge form. Reopens only on a `wrong` signal or when an import it reads changes.

## Result

The manuscript proves a conditional local walk estimate (Lemma 1), a local real and complex gap (Lemma 4), a normally convergent local root series (Theorem 5), and the early matrix envelope (26), normalization, fixed-region heredity, wall factorization, local dimension and exact interpolation/Schur identities (Theorems 7–8). Corollary 13.1 gives UM4–UM6 and UM14 with an early cost envelope one on the specified representative class. Imports are R, repaired W, actual averaging/branches AV and FG/UM; G-ID is needed for physical identification, and F if the completed gauge form is used. Their flat, curved-coefficient, inverse and geometric premises remain premises.

**Definitions supplied or sharpened:** the full-stencil local regular class and size (3); R4 intersected with Rep, with its strict domain distinction; averaged-contour block axiality and its full averaging read radius; half-open cube ownership and the corner collar; connected uncut read hulls including zero-length multiplier reads and transpose partners; physical tree lengths with the root margin; field-independent labelled moments and product labels; the open working domain; grouped short-entry polynomials and their ball hulls; the local integrated root; the full-hull tag and discard-before-evaluation rule; reference matrices, empty-coordinate functional and determinant branch; the fixed-ceiling meaning of nonextension. UM2's integrand is restated, not newly defined. The distinct symbols are \(\epsilon_{\rm lat}\) (mesh), \(\mu_W\) (moment rate), \(\rho_{\rm lay}\) (layer separation), \(b_{\rm tail},b_{\rm gap}\) (buffers), \(q_*\) (contraction), \(\zeta\) (Gaussian tilt), \(\Lambda_{\rm res}\) (resolvent scale), and \(P_{\rm fail}\) (failed bonds, distinct from the real reference \(P_0\)).

**Corrections and checks against the draft and other notes:**

1. Lemma 1 is now a local cut-down argument with the graph-norm, all-scale second-jet, branch-power, root-count and zero-length-read repairs. The draft's unqualified import of h-walk H3 was wrong; fixed-region field locality survives. No region-change or reflection theorem is claimed.
2. The draft's Ax reading as a tree gauge was wrong. Lemma 3 uses averaged contours and proves nonlinear covariance from the actual formula; derivative-row covariance alone was insufficient. Torus room is explicit.
3. Lemma 4's localization route is valid under these repairs and Rep. The all-core conclusion was not: adding Rep restricts the domain, and activity gauge invariance does not supply descent. This is the first remaining **Outstanding** within the claimed H-M supply.
4. The inv-root and carrier-check estimates are valid conditional implications on their supplied regular domain. Extending them to genuinely local data needs Lemmas 1–4 and the local compression in (16). Pair-independent majorants, grouped entry sums and open fibres now justify root holomorphy and Schwarz. The root at a cut parameter is not asserted to be the root of the mutilated precision.
5. The draft correctly accepted carrier-check's correction that SA already gives a covariance construction scheme (10311–10338, 10533–10550). Our series is an explicit replacement. Equality with another series off the physical endpoint is neither proved nor required for its displayed readers.
6. IN1 Lemma 2's chain counterexample remains correct for its own family. The full-read replacement excludes its mechanism; it does not disprove the example. IN1's Outstanding paragraph cannot yet be replaced by the draft's proposed all-core assertion.
7. The no-extension example required a new Lipschitz potential, a complex-curvature check and a fixed-ceiling statement. Proposition 10 supplies them and makes no R5–R6 claim.
8. The matrix-error proof is shortened by comparing the entire tagged product before its two field changes. It retains the double-tag exponent 32 and explicit floors. The completed gauge correction changes all dependent early constants, not merely one Lipschitz constant.
9. Gaussian normalization, integral holomorphy and the finite gas identity now explicitly require FG smallness and allowed potential growth. Physical identification requires full working-domain admission and G-ID, not just the weaker pr-lay stage statement.
10. The draft's conditional arithmetic agreeing with um-envelope and IN1 Lemma 3 is right; it does not close c4-order's actual-supply condition or um-novelty's all-core question. The latter remains outstanding, as do the actual stage/domain and physical-identification interfaces. No frozen context note or gate was edited.

These are research implications and counterexamples, not independently refereed results. **This text is not yet refereed and grants no scientific or audit status.**
