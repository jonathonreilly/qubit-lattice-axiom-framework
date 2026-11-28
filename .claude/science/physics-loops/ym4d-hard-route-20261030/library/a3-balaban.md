# Balaban's background propagators and outline A3
Provenance: OpenAI Codex (GPT-6; exact runtime variant and configured reasoning effort not exposed; requested effort max), checkout `713766c1b62d67c9c8afaa5828efb56d5d49d7ea`; Sussman–Alpoge outline `31a47c543775`; Tadeusz Bałaban, CMP **98** (1985), 17–51; **99** (1985), 75–102 and 389–434; **102** (1985), 277–309; research text, not an audit, grants no status.

## 1. Scope, sources and live checkpoint

Moves: queue row 82, A3 (`sa-ledger` #3). The target is the complete Section 8 table of `gates/a3-gate-b2c312b2e.md`, with the outline's actual averages, gauges, conditioning and boundary equations. A proof would supply the response input; an explicit failure would identify the clause that must change. Failure to transfer a theorem is not a counterexample to A3.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline, A3, its Landau-pair and complex-domain formulation, and its comparison architecture. Credit Tadeusz Bałaban for the averaging, regular-field, propagator and variational constructions examined below. The outline was fetched once to `/tmp/sa_ym4.tex` from the requested commit. Bałaban's owner-supplied OCR files remain outside the repository in `../../balaban/`; OCR formulas are reconstructed explicitly where used. CMP 95 and CMP 96 are not in hand and cannot silently supply a proved input.

Source discipline: this checkout is the pin above; the gate is read in full; only its surviving scopes of Lemmas 1, 2, H and single-layer Theorem E may be reused from `a3-response.md`. The workflow document named in `AGENTS.md` is absent. The task-specific instructions govern this single-file research note. No computation, independent check, audit, commit or publication is claimed.

Status: **STOPPED — session research budget exhausted before the full vector/localization port was completed.** A3 is neither proved nor refuted. The scalar, averaging and boundary subresults below are written research arguments; the remaining imports and transfers are explicit in §§13–14. No partial result is being labelled PROVED for queue row 82.

## 2. What the published theorems actually provide

The previous broad search is `lit-large-field.md` §3 and `lit-balaban.md`; their access limitations are superseded here by the owner-supplied papers. The targeted search in these papers finds the following dependency chain. Numbers in this table refer to CMP 99, 389–434, not the outline. This is a statement/proof map, not acceptance of its cited inputs.

| Result | Object and proof dependency |
|---|---|
| 3.1, pp. 397–398 | Scalar covariant inverse \(G'=(\Delta_U+Q'^*aQ')^{-1}\), with local value, derivative, Hölder, mixed-derivative, local \(L^2\) and weighted global estimates (3.42)–(3.47). |
| 3.2, pp. 398–399 | Coarse scalar inverse \((Q'G'^2Q'^*)^{-1}\), (3.48); hence the regular kernel of \(P=1-R\), (3.49). |
| 3.3, p. 399 | The same package for \(G_0=(\Delta^{\rm W}_U+DRD^*+Q^*aQ)^{-1}\). This notation distinguishes it from the later gauge-extended \(G\). |
| 3.4, pp. 400–407 | Holomorphic perturbation on (3.37), proved by the resolvent series (3.64), (3.67), (3.86), **assuming** 3.1–3.3 at the real base. |
| Corollaries 3.5–3.6, pp. 407–408 | Small fields about identity, then fields with a small gauge on a cube. The initial flat estimates are explicitly taken from CMP 96. |
| 3.7 and Corollary 3.8, pp. 409–410 | Scalar random walk, (3.90), with local dependence and walk-length bounds. The summation explicitly uses CMP 96 Lemma 2.1. |
| 3.9, p. 413 | Random walk for \((Q'G'^2Q'^*)^{-1}\). This is not just inversion of an entrywise estimate. |
| 3.10, pp. 415–416 | Random walk for \(G_0\), including the nonlocal \(DRD^*\) commutator. |
| 3.11, p. 416 | Positivity, using positive local inverses and a small parametrix remainder. |
| 3.12, pp. 417–423 | Gauge-extended \(G,G_1\) and constrained lifts \(H,H_1\); nonlinear-average quadratic corrections require (3.36). **The covariant-Laplacian estimate of (3.42) is explicitly excluded for \(G,G_1\).** |
| 3.13, pp. 424–426 | Gauge-fixed constrained covariance \(\mathcal C\), with the same Laplacian exception. It is positive on its fluctuation space, not strictly positive on the ambient space, where constraints give a kernel. |

Two additional results are relevant to the requested boundary/covariance rows: 3.14, pp. 426–427, compares two compatible sequences by cancelling walks localized in their common region; 3.15, pp. 427–432, concerns the **unit-lattice** covariance after axial-coordinate elimination. The latter uses CMP 96 Lemma 2.4 for the flat gap and a specific local pivot-coordinate map. Neither conclusion follows by renaming the covariance of 3.13.

Domains matter. Equations (3.35)–(3.36), p. 396, require a small gauge on each specified cube and a second-order bound in that gauge. They reconstruct as
\[
 |A|\le C M\alpha_0 s^{-1},\quad |\nabla A|\le C M\alpha_0s^{-2},\quad
 |d^*dA|\le C M\alpha_0s^{-3},\qquad s=L^j\eta.
\]
The first two are used for 3.1–3.11; the last is needed for 3.12–3.13. The powers are fixed by (3.35)–(3.38) and the weighted norm definition (3.41), not by accepting malformed OCR superscripts. Complex perturbations are \(e^{i\eta A'}U\), with \(|A'|\le\alpha_1s^{-1}\), \(|\nabla_UA'|\le\alpha_1s^{-2}\); the stronger version also bounds \(D_U^*D_UA'\) by \(\alpha_1s^{-3}\). These are configuration neighborhoods, not automatically the outline's datum polydiscs or its decoupling discs.

CMP 102, pp. 307–309, differentiates the nonlinear fixed-point equation and proves a small **global norm** for its derivative operator in (185)–(188). The localized second-variation bound (189), which is used for exponential decay (190), is then stated with the calculation expressly omitted. Consequently (189) is a separate proof obligation, even when all CMP 99b propagators are granted. This is a precise earlier stopping point than an unspecified need for a nonlinear theorem.

## 3. Exact scalar projection and the gauge conversion it really gives

Here is a hand derivation of the projection identities used by Bałaban, CMP 99b (3.21)–(3.25), (3.115), (3.118), (3.152). It also fixes the OCR placement of inverse and transpose. Work on one **fixed**, finite real lattice with specified boundary spaces and their cell-weighted inner products. Let \(D\) be the scalar covariant gradient, \(\Delta=D^*D\), and \(Q_s\) the pillar average. Assume \(Q_s\) is onto and
\(A_s=\Delta+Q_s^*aQ_s>0\), where \(a>0\) on rows. Put
\[
 S=A_s^{-1},\quad N=(Q_sS^2Q_s^*)^{-1},\quad
 R=I-SQ_s^*NQ_sS.                                      \tag{3.1}
\]
For any nonzero row vector \(b\),
\(\langle b,Q_sS^2Q_s^*b\rangle=\|SQ_s^*b\|^2>0\), proving existence of \(N\). If \(T=Q_sS\), the rightmost term in (3.1) is \(T^*(TT^*)^{-1}T\). Direct multiplication makes it symmetric and idempotent, with range \(\operatorname{ran}T^*\). Thus \(R\) is the orthogonal projection onto \(\ker T\). Furthermore
\[
 \ker(Q_sS)=\Delta\ker Q_s.                             \tag{3.2}
\]
Indeed, for \(Q_s\lambda=0\), \(S\Delta\lambda=\lambda\), so \(\Delta\lambda\in\ker T\). Conversely, if \(Tf=0\), take \(\lambda=Sf\); then \(Q_s\lambda=0\) and \(\Delta\lambda=f\). This proves (3.2), without replacing \(R\) by the projection onto \(\ker Q_s\).

Define
\[
 E=I-DSRD^*.                                           \tag{3.3}
\]
Since \(Q_sSR=0\), one has \(\Delta SR=R\). Hence \(RD^*E=0\), \(E^2=E\), and \(ED\lambda=0\) for \(\lambda\in\ker Q_s\). If the **actual** constraint rows \(Q\) obey \(QD\lambda=0\) on \(\ker Q_s\), then also \(QE=Q\). Thus \(E\) sends a field to the specified Landau slice by a constraint-preserving gauge tangent. All of this is finite-dimensional algebra. A depth-uniform norm bound for \(E\), its derivatives or its kernel still requires the estimates for \(S,N\) and the averages.

The same formulas extend holomorphically with transposes on a complex neighborhood on which the two inverses remain invertible. Orthogonality is then replaced by the algebraic identities. Replacing a transpose by a Hermitian adjoint at complex data would destroy holomorphy.

### An explicit check that the surviving local gauge cannot be substituted

At identity, take a periodic lattice with \(2N\) blocks of odd side \(s\ge5\) in every direction, with \(N\) as large as the outline's torus floor requires. Use one fixed color and let \(f\) be constant in the transverse coordinates, equal to \(+1,-1,+1,-1,\ldots\) on successive blocks in direction 1. Let \(\Pi\) subtract each pillar mean. Then \(\Pi f=0\). On the cyclic direction choose \(A_1\) recursively by
\(A_1(t)=A_1(t-1)-f(t)\); the zero sum of \(f\) makes this periodic. Set all other components to zero. With \(D^*A(t)=A_1(t-1)-A_1(t)\), we have \(D^*A=f\), so \(\Pi D^*A=0\).

Choose \(t=0\) at the first site of a positive block and \(t=2\) strictly inside it. For the positive scalar Laplacian,
\(\Delta f(0)=2\) and \(\Delta f(2)=0\). Let \(\lambda\) be a point mass at \((0,x_\perp)\) minus a point mass at \((2,x_\perp)\). Both points lie in one pillar, so \(Q_s\lambda=0\), whereas
\[
 \langle f,\Delta\lambda\rangle
 =\langle\Delta f,\lambda\rangle=2
\]
in counting measure (the common positive cell weight changes neither nonvanishing nor the conclusion). By (3.2), \(Rf\ne0\). Therefore the gauge of Lemma E, \(\Pi D^*A=0\), is not Bałaban's \(RD^*A=0\), even at the flat background. Multiplying by any positive small amplitude preserves the distinction. This configuration refutes only their identification, **not A3** or existence of a bounded conversion.

## 4. The retained local estimates and their exact scope

The gate's surviving Lemmas 1 and 2 give, on an embedded rectangular four-dimensional box of side at most \(l\),
\[
 \inf_\omega\|A-d\omega\|_2^2\le\tfrac32l^2\|dA\|_2^2,
 \qquad \|f-\operatorname{Av}f\|_2^2\le2l^2\|df\|_2^2.
\]
For completeness the count is as follows. Average coordinate-ordered paths from \(y\) to \(x\). An edge in direction \(i\), compared with the adjacent path, sweeps at most \(3l\) plaquettes. A given plaquette separating \(a\) from \(n_j-a\) sites is read by \((|D|/n_j)2a(n_j-a)\le |D|l/2\) pairs. Jensen and the path Cauchy–Schwarz inequality give the first bound. A scalar path has at most \(4l\) edges; the identical edge count gives the second. These are box statements, not extension theorems across holes.

Lemma H gives \(\|h\|_{\infty,Q_r}\le Cr^{-2}\|h\|_{2,Q_{2r}}\) for a lattice-harmonic scalar function. Its proof uses the one-dimensional average-plus-total-variation inequality in each of four directions; a mixed difference of order \(m\) receives \(r^{-(4-m)}\). Cauchy–Schwarz contributes \(Cr^2\), and \(m\) Caccioppoli estimates on nested boxes contribute \(Cr^{-m}\). Each term is \(Cr^{-2}\|h\|_2\); reserve one mesh step per difference and absorb bounded \(r\) by the pointwise \(\ell^2\) bound.

The single-layer Theorem E remains available **with its original local energy/potential right-hand side**,
\[
 \sum_{j=1}^n\|sA_L\|_{L^4(\mathcal A_j(y))}
   +|\Phi_n(A_L)(y)|
 \le C(L)\big(\|dA_L\|_{2,N_y}+s^{-1}\|A_L\|_{2,N_y}\big),\quad s=L^n.
\]
Here \(A_L\) is in the \(\Pi\)-slice, the annuli and normalized top measure are those of the source, and \(N_y\) comprises the neighboring top blocks. Retain the gate's corrections: the test bump reads a plaquette collar, and \(\Delta|x|^2=-8\) for the positive Laplacian. No estimate in this section replaces its right side by coarse data, supplies the \(R\)-slice bound, or proves a multiscale seam result.

## 5. Weighted summability on the outline's metric: a hand proof

This supplies the **summation input actually needed here** where CMP 99b invokes CMP 96 Lemma 2.1. It does not purport to transcribe the unavailable lemma. Credit Bałaban for the multiscale convolution method and Sussman–Alpoge (with Claude and Codex) for the continuous weighted metric and order of constants. The counting proof below is explicit and does not use the false depth-independent polynomial count rejected by the gate.

Let \(s_j=L^j\eta\), let \(\Omega_j\) be nested, with
\(\operatorname{dist}_\infty(\Omega_q^c,\Omega_{q+1})>\rho s_q\), and assume \(\rho\ge1\). At level \(j\), the tops form a subset of the \(s_j\)-grid in \(\Omega_j\setminus\Omega_{j+1}\). Use precisely the outline's path metric: cost \(s_j^{-1}\) per unit length in layer \(j\), bare cost outside \(\Omega_1\), and paths allowed on the torus, including outside \(\Omega_0\). Empty layers and members equal to the torus cause no extra crossings. Endpoints are assigned their specified layer; boundary conventions can be handled by limits from that layer.

Fix a top \(y\) of level \(i\). A path of cost at most \(r\) from \(y\), reaching layer \(h>i\), crosses every complete collar of levels \(i+1,\ldots,h-1\). For each such \(q\), take the segment after the last exit from \(\Omega_q^c\) and before the first subsequent entrance into \(\Omega_{q+1}\). Its Euclidean length is at least \(\rho s_q\), its scale is at most \(s_q\), and its cost is at least \(\rho\). Using first entrances in increasing order gives disjoint segments. Therefore
\[
 h\le i+1+r/\rho.                                      \tag{5.1}
\]
Reversing a path ending at a top of level \(j<i\) gives \(j\ge i-1-r/\rho\). Thus any endpoint in the metric ball has
\[
 |j-i|\le1+r/\rho.                                     \tag{5.2}
\]
The maximum scale along the path is at most \(s_iL^{1+r/\rho}\). Its lifted Euclidean displacement is consequently at most \(r s_iL^{1+r/\rho}\), since Euclidean length is at most maximum scale times metric length.

At a fixed endpoint level \(j\), a cube of this radius contains at most
\[
 \big(3+2rL^{2+2r/\rho}\big)^4
 \le (3+2r)^4L^{8+8r/\rho}
\]
grid points, by (5.2). On a torus, lift the path from a fixed lift of \(y\); counting lifted grid points only overcounts distinct endpoints, so the same bound holds. There are at most \(3+2r/\rho\le5(1+r)\) possible levels. Hence for every real \(p\),
\[
 \sum_{d(y,z)\le r}(s_z/s_y)^p
 \le 5L^{8+|p|}(1+r)(3+2r)^4
       \exp\!\left(\frac{(8+|p|)\log L}{\rho}r\right).   \tag{5.3}
\]
Metric balls can indeed have exponential growth; (5.3) pays for it by the separated collars.

Given \(\tau>0\) and \(p_0\ge0\), choose
\[
 \rho\ge\max\{1,\,2(8+p_0)\log L/\tau\}.               \tag{5.4}
\]
Summing the shells \(n\le d<n+1\), using (5.3) at \(n+1\), gives, simultaneously for \(|p|\le p_0\),
\[
 \sup_y\sum_z(s_z/s_y)^p e^{-\tau d(y,z)}
 \le C(L,p_0,\tau)<\infty.                             \tag{5.5}
\]
For example the right side is bounded by a fixed multiple of
\(L^{8+p_0}e^{\tau/2}\sum_{n\ge0}(n+2)^5e^{-\tau n/2}\).
This series converges without numerical evaluation: for sufficiently large \(n\), \(5\log(n+2)\le\tau n/4\); the remaining tail is geometric and the finite initial part defines a constant. The inequality for the logarithm follows, for instance, from \(\log t\le2\sqrt t\) and then taking \(n\) above a fixed quadratic function of \(1/\tau\). Both Schur sums follow because the same proof applies to \(-p\).

In particular, for \(0<\tau'<\tau\), after applying (5.4) with \(\tau-\tau'\), the triangle inequality gives the convolution bound
\[
 \sum_z(s_z/s_y)^p e^{-\tau d(y,z)}e^{-\tau d(z,y')}
 \le C e^{-\tau'd(y,y')}.                             \tag{5.6}
\]
Indeed factor out \(e^{-\tau'd(y,y')}\), leave
\(e^{-(\tau-\tau')d(y,z)}\), and bound the remaining exponential by one. Products with other scale powers are reduced to (5.6) by factoring their endpoint powers and taking the corresponding \(p\). This proves summability for every fixed finite collection of scale powers, with no dependence on depth, volume or region shape. The rate and powers must be chosen **before** the gap. It does not prove that a flat propagator satisfies the kernel estimates being summed.

For the source's layer-discrete path metric, every admissible path is admissible for the outline metric, so \(d_{\rm outline}\le d_{\rm discrete}\). An already established exponential bound in the latter therefore implies the same pointwise bound in the former. Summation in the former is justified separately by (5.5), not by reversing this metric inequality.

## 6. Lifts, covariances and weights: the exact algebraic port

The following reconstructs CMP 99b (3.118)–(3.153) directly; it does **not** assert the inverses' uniform bounds. Retain §3's spaces, assume the constraint is onto, and let \(L\) be a symmetric form on one-forms. Define its gauge extension \(L_\pi=E^*LE\), and suppose
\[
 A_1=L_\pi+DRD^*+Q^*aQ>0,\quad G_1=A_1^{-1},\quad
 N_1=(QG_1Q^*)^{-1},\quad H_1=G_1Q^*N_1.              \tag{6.1}
\]
The row inverse exists since \(G_1>0\) and \(Q\) is onto. Because \(EDSR=0\) and \(QDSR=0\),
\(A_1DSR=DR\); thus
\[
 G_1DR=DSR,\qquad RD^*G_1=RSD^*,\qquad RD^*H_1=0.      \tag{6.2}
\]
For the last equality, transpose \(QDSR=0\). Also \(QH_1=I\). It follows by multiplying (6.1) that \(H_1b\) is stationary for \(\tfrac12\langle A,LA\rangle\) subject to \(QA=b,RD^*A=0\): for a tangent \(v\),
\(\langle v,LH_1b\rangle=\langle v,A_1H_1b\rangle=0\).
Here \(Ev=v,EH_1b=H_1b\), so replacing \(L\) by \(L_\pi\) in this pairing is exact. Strict positivity of \(A_1\) on the tangent space proves uniqueness.

The constrained covariance is
\[
 C=G_1-G_1DRD^*G_1-G_1Q^*N_1QG_1.                    \tag{6.3}
\]
Indeed, (6.2) and \(\Delta SR=R\) give
\(RD^*G_1DR=R\). Hence \(QC=RD^*C=0\). For every tangent \(v\),
\(\langle v,A_1Cf\rangle=\langle v,f\rangle\), because the two subtracted terms pair with \(Qv\) and \(RD^*v\). This characterizes the inverse of the restricted positive form and proves (6.3), including the fine-force convention. The quadratic-form projection is \(P_f=CA_1\); it is the identity on the tangent space and annihilates its \(A_1\)-orthogonal complement. In particular, ambient zero eigenvalues of \(C\) are required by the constraints. This is the interpretation of positivity appropriate to 3.13.

At a physical current, the Wilson Hessian's gauge extension is obtained by the second variation of gauge invariance. At an independent current the outline instead prescribes an explicit bilinear correction (outline lines 10165–10190). Then (6.2) has the current-defect term displayed in outline (1c), statement 3. Dropping it would identify different operators. Equations (6.1)–(6.3) above assert the exact gauge-invariant case only; they do not erase that defect off shell.

### Cell volumes cannot be dropped

Let \(w_b=\eta^4\) on fine bonds and \(w_c=\xi_c^4\) on rows of physical potential. For a counting matrix \(T(c,b)\), its adjoint is
\[
 T^*(b,c)=w_b^{-1}T(c,b)^{\mathsf T}w_c.                \tag{6.4}
\]
This follows by expanding the two inner products as finite sums. An integral kernel \(K(x,z)\) represents the counting matrix \(w_zK(x,z)\). CMP 98 (138) correspondingly defines the functional derivative as \(\eta^{-4}\) times the coordinate derivative. The factors in CMP 99b (3.48), (3.132), (3.133) must be read with these conventions: an inverse of order four on tops has a density proportional to \(\xi_y^{-4}\xi_{y'}^{-4}\), and its counting matrix absorbs the source \(\xi_{y'}^4\); the order-two row inverse behaves the same way with order two. This reconstructs the density/counting distinction; it does not choose an unverified numerical constant from the OCR.

For dimensionless bond data \(b_c=\xi_ca_c\), the natural row energy in four dimensions is counting measure:
\(\sum_c\xi_c^4\xi_c^{-2}|a_c|^2=\sum_c|b_c|^2\).
Thus the dimensionless constraint is \(K=\mathsf mQ\), and its lift is \(H_B=H_1\mathsf m^{-1}\). A bound for \(H_1\) is not the response bound until this input factor is included. This explains the extra inverse length stated just after CMP 99b (3.133). When rewritten as localized force-to-output operator bounds with their cell measures, (5.5) sums them without a factor counting fine sites. A bare entrywise bound alone does not establish PW12.

## 7. What the random-walk and complex-perturbation arguments prove

Here is the precise conditional analytic argument underlying CMP 99b 3.4, 3.7–3.10. Normalize local blocks by the input/output powers of \(\xi\) and the cell volumes. For a block matrix \(T\), define
\[
 \|T\|_\mu=\max\left\{
 \sup_y\sum_z e^{\mu d(y,z)}\|T_{yz}\|,
 \sup_z\sum_y e^{\mu d(y,z)}\|T_{yz}\|\right\}.         \tag{7.1}
\]
Each entry norm is an operator norm between the specified local spaces, not a count of fine coordinates. If scale ratios are needed, conjugate by the corresponding powers of \(\xi\); §5 controls both sums. The triangle inequality and matrix multiplication give
\(\|ST\|_\mu\le\|S\|_\mu\|T\|_\mu\): expand each product, use \(d(y,z)\le d(y,x)+d(x,z)\), then sum the two nonnegative sums in order. The identity has norm one.

Suppose a parametrix \(G^{\rm loc}\) for the **actual** operator satisfies
\[
 A G^{\rm loc}=I-T,\qquad \|T\|_\mu\le q<1.           \tag{7.2}
\]
Then \(G^{\rm loc}\sum_{n\ge0}T^n\) is a right inverse; on finite equal-dimensional spaces this is the inverse. Its norm is at most \(\|G^{\rm loc}\|_\mu/(1-q)\). If local terms are holomorphic on a common domain and these bounds are uniform there, the series and all its Cauchy integrals converge uniformly, proving holomorphy. For \(A'=A-V\), use \(T=VG\) to obtain
\[
 G'=G(I-VG)^{-1},\qquad G'-G=GVG'.                    \tag{7.3}
\]
These are Bałaban's (3.64), (3.86), reconstructed by multiplication, with no sign inferred from OCR. First-difference and Hölder output bounds follow from the corresponding bounds on the **leftmost** local inverse, if the remainder maps its force space to itself with norm \(q\). For a right derivative one must also factor or transpose the source derivative. No argument here restores the excluded \(\Delta_U G_{(1)}\) estimate.

For real symmetric \(A\), positivity can be checked without the ambiguous OCR eigenvector calculation in 3.11. If \(G^{\rm loc}>0\), \(AG^{\rm loc}=I-T\), and \(\|T\|_{2\to2}<1\), take the symmetric matrices
\[
 B_t=(1-t)I+t(G^{\rm loc})^{1/2}A(G^{\rm loc})^{1/2}.
\]
They are similar to \(I-tT\), which are invertible by the Neumann series. No eigenvalue of \(B_t\) can cross zero, and \(B_0=I\), so \(B_1>0\), proving \(A>0\). Finite-dimensional eigenvalue continuity follows directly from the minimum Rayleigh quotient and the operator-norm continuity of \(B_t\). Thus this positivity step is proved when (7.2) and positivity of the local inverses have been proved.

### The boundary model that is actually harmless

On a finite arbitrary set of bare bonds, with \(Q=Q'=I\), \(R=0\), and identity background, put
\(A=\eta^{-2}a_0I+d_{\rm in}^*d_{\rm in}\), \(a_0>0\). Here \(d_{\rm in}\) uses just the included plaquettes. Extension by zero and the Fourier identity on the full periodic lattice give
\(0\le\eta^2d_{\rm in}^*d_{\rm in}\le16I\): the full curl symbol is \(|q|^2I-qq^*\), where \(q_\nu=e^{ip_\nu}-1\) and \(|q|^2\le4\cdot4\). Dropping plaquettes decreases its form. Hence
\[
 A^{-1}=\frac{\eta^2}{a_0+16}
 \sum_{n\ge0}\left(I-\frac{\eta^2A}{a_0+16}\right)^n.  \tag{7.4}
\]
The \(n\)-th term vanishes between bonds whose plaquette-adjacency distance exceeds \(n\), and has norm at most \((16/(a_0+16))^n\). Therefore
\[
 |A^{-1}(b,b')|\le\eta^2a_0^{-1}
 \left(\frac{16}{a_0+16}\right)^{\operatorname{dist}_{\rm adj}(b,b')}.
\]
Finite differences cost only fixed powers of \(\eta^{-1}\); their mesh-scaled value, first-difference, second-difference and Hölder estimates follow by subtracting the finitely many neighboring entries. This proves the flat local boundary model uniformly over shapes. It does **not** set the global \(R\) to zero in layer zero: \(R\) has a tail from the other layers. Controlling that tail in the assembled boundary parametrix is still required.

### A smooth flat row lift, including outward seams

The gate's graph-norm defect can be repaired explicitly. This is a flat lemma for the outline's **straightened** rows, with no inward rows. Work in fine units, take odd \(L\ge33\), gap \(\rho>4L\), and the outline's nonwrapping floor. For a row of scale \(s=L^j\), \(j\ge1\), put \(m=(s-1)/2\), \(d=\lfloor m/8\rfloor\), and
\[
 h_d(t)=(1-|t|/d)_+,\qquad
 g_+(w)=h_d(w-2d)-\tfrac13h_d(w-6d).
\]
These profiles are sampled at integer coordinates. Symmetry and the finite triangular sum give
\[
 \sum_t h_d(t)=d,\quad \sum_t t h_d(t)=0,\quad
 \sum_w wg_+(w)=2d^2-\tfrac13 6d^2=0,\quad
 \sum_wg_+(w)=\tfrac23d\ge s/72.                       \tag{7.5}
\]
For the last bound use \(d\ge m/16\) and \(m\ge s/3\). The support is in \([d,7d]\subset(0,m)\); in particular it vanishes in a neighborhood of the seam face. Its supremum is at most one, and its first difference at most \(64/s\). There is no longitudinal jump.

Let \(w\) measure the longitudinal coordinate from the face bond where the row tent is maximal. Use \(g(w)=g_+(w)+g_+(-w)\) for an interior row. For an outward row use just the reflected or unreflected half supported in its **coarse** block. In the three transverse directions use
\(h_{m+1}(t)\), whose mass is \(m+1\). Set the only nonzero component of \(\phi_c\) equal to
\[
 \frac{s^3}{(\sum_w g(w))(m+1)^3}\,
 g(w)\prod_{\nu\ne\mu}h_{m+1}(t_\nu).                \tag{7.6}
\]
The straightened row has coefficient \(s^{-4}(s-|w|)\). By (7.5), \(q_c\phi_c=1\). Either adjacent parallel row reads the moment \(\sum_{w>0}wg(w)\) or its reflection, which is zero. Other rows of that scale either read a different component or a disjoint transverse block. Thus \(q_{c'}\phi_c=\delta_{c'c}\) at the same level. The one-sided normalization in (7.6) is essential.

The prefactor is at most \(576/s\); each first difference is at most \(36864/s^2\), and the field plus its one-step difference support contains at most \(16s^4\) sites. Consequently
\[
 \|\xi^{-1}\phi_c\|_2^2+\|\nabla\phi_c\|_2^2
 \le10^{12}.                                         \tag{7.7}
\]
Every nonzero field value is in its assigned layer, so the potential weight here is \(\xi=s\). The counting and the displayed constants prove (7.7) by multiplication; no enumeration is used. At level zero use the unit bond field instead; its bound is smaller.

Put \(R_0b=\sum_c b_c\phi_c\) and \(K=qR_0-I\). A fine row cannot read a coarse bump, since its endpoints avoid the coarse region and coarse outward bumps are strictly inside their coarse half. A coarse interior row cannot read a fine bump. Only a coarse **outward** row can read fine bumps in its outer block. That block contains a full array of \(L^4\) finer pillars. Separation excludes a second seam in this array: the other seam is more than \(\rho s_{j-1}>4s_j\) away. Thus the contributing finer rows are interior rows. Also a bump belonging to an outward row cannot be read by an outward row one level higher. These facts prove
\[
 K^2=0,\qquad T=R_0(I-K),\qquad qT=I.                 \tag{7.8}
\]
This proves nilpotence from support, not merely from triangularity.

A cross-level entry is bounded by \(576L^{-3}\): the coarse tent is at most \(s_j^{-3}\), and the finer bump has absolute sum at most \(576s_{j-1}^3\). A row reads at most \(16L^4\) finer bumps, and a finer bump is read by at most 16 coarse rows, by the adjacent-double-block count. Therefore the two Schur sums are at most \(9216L\) and \(9216L^{-3}\), giving \(\|K\|_{2\to2}\le9216/L\). At a fine bond, at most two consecutive levels of bumps can occur; at each level there are at most two adjacent longitudinal/transverse choices for a fixed component difference. Bounding their product choices by \(2^4\) and the two levels by two, the overlap is below 64. Cauchy–Schwarz at each site and (7.7) yield
\[
 \|\xi^{-1}Tb\|_2^2+\|\nabla Tb\|_2^2
 \le64\cdot10^{12}(1+9216/L)^2\|b\|_2^2.              \tag{7.9}
\]
Zero extension outside \(\Omega_0\) only affects bare unit bumps at that boundary; they obey the same estimate. All higher-level bumps lie inside their row blocks. On the torus the chosen floor keeps these supports embedded.

In particular the squares of \(\|dTb\|_2\) and \(\|RD^*Tb\|_2\) are bounded by the right side of (7.9), since an orthogonal projection is contractive and the flat full-lattice identity is \(\|dA\|_2^2+\|d^*A\|_2^2=\|\nabla A\|_2^2\). Restricting the curl or divergence to the domain decreases the respective squared norms of the zero extension. If the positive flat \(G_0\) is already supplied, this lift proves a uniform lower bound on the **dimensionless-row** Gram matrix \(qG_0q^*\): minimizing the quadratic form with \(qA=b\) costs at most the energy of \(Tb\), including the row mass \(a_0\|b\|_2^2\). Its exact minimum is \(\langle b,(qG_0q^*)^{-1}b\rangle\). Thus the upper bound for this inverse Gram matrix is (7.9)'s constant plus \(a_0\). Restoring physical rows gives the \(\xi_c^2\) lower bound. This repairs the row lift, but does not prove positivity or the full regularity estimates for \(G_0\) itself.

### Real scalar positivity and a scalar Gram lower bound

A further part of the unavailable flat input can be proved directly, and it extends to a real regular field with the new pillar means. Assume each pillar \(P\) of side \(s\ge L\eta\) has a gauge on a slightly larger cube with
\(|A|\le\delta/s,\ |\nabla A|\le\delta/s^2\), where \(\delta\) is a sufficiently small fixed number. These are actual hypotheses of the regular-pair class, not a curvature-only gauge theorem. For this paragraph use the contour-mean comparison (8.12), whose proof involves no scalar inverse.

The dependency order of the next arguments is §§4–5, then the finite averaging lemmas of §8 and the free Green lemma of §12, then the scalar results here. Neither of those later-numbered local lemmas uses a background propagator, so their use here is not circular.

In that gauge the scalar Poincaré inequality of §4 and Cauchy–Schwarz for the average give
\[
 \|f\|_{2,P}
 \le C s\|df\|_{2,P}+s^2|\operatorname{Av}_P f|
 \le C s\|D_Uf\|_{2,P}+s^2|Q'_Uf(P)|
                         +C\delta\|f\|_{2,P}.
\]
Indeed \(d-D_U\) has coefficient bounded by \(C\delta/s\), and
\(|(Q'_U-\operatorname{Av})f|\le C\delta s^{-2}\|f\|_{2,P}\).
Absorb the last term. Squaring and summing over the disjoint pillars, with the level-zero identity handled directly, proves
\[
 \sum_P s_P^{-2}\|f\|_{2,P}^2
 \le C\left\{\|D_Uf\|_2^2+
                  \sum_P s_P^2|Q'_Uf(P)|^2\right\}.   \tag{7.10}
\]
All within-pillar bonds are present; any other gradient terms are nonnegative. Thus the actual real scalar \(A_s=D_U^*D_U+Q_U'^*aQ'_U\), \(a=s_P^{-2}\), is positive definite on the stipulated finite boundary space, and \(S=A_s^{-1}\) exists. There is no global gauge choice in this argument.

To obtain the stronger scalar Gram lower bound, construct a second-order graph lift of \(Q'_U\). For a non-bare pillar take
\(\chi_P(x)=\prod_{\nu=1}^4\psi((x_\nu-y_\nu)/s)\),
where a fixed smooth \(\psi\) equals one on \([-1/8,1/8]\), vanishes outside \((-1/4,1/4)\), and \(0\le\psi\le1\). Sampling this profile gives
\[
 |\nabla\chi_P|\le C/s,\quad
 |\nabla^2\chi_P|\le C/s^2,\quad
 c\le \operatorname{Av}_P\chi_P\le1.
\]
The last lower bound follows by counting the central interval in each coordinate; \(s/\eta\ge33\) makes the count a fixed positive fraction of the pillar. The derivative bounds follow by integrating the ordinary derivatives of \(\psi\) over one or two mesh segments. The support has several mesh steps of room before the pillar boundary.

Let \(M_Pb=Q'_U(\chi_P b)\), in the chosen gauge. Equation (8.12) implies
\(\|M_P-(\operatorname{Av}\chi_P)I\|\le C\delta\operatorname{Av}\chi_P\).
Thus \(M_P\) is invertible with a fixed bound. Define \(F_b\) on this pillar by
\(\chi_P M_P^{-1}b_P\), transformed back to the original gauge, and put \(F_b=b_P\) at bare pillars. Then \(Q'_UF_b=b\) exactly. The covariant product rule, the two cutoff derivatives and the two gauge bounds give
\[
 \|\Delta_UF_b\|_2^2\le C\sum_P|b_P|^2,\qquad
 \|Q_U'^*a b\|_2^2\le C\sum_P|b_P|^2.               \tag{7.11}
\]
For the first inequality each non-bare pillar contributes at most
\(C s^4(s^{-2}|b_P|)^2\). Bare point fields contribute at most a fixed number of terms of size \(\eta^4(\eta^{-2}|b_P|)^2\); their one-step supports have bounded overlap. For the second inequality the adjoint of a real transported pillar mean sends \(b_P\) to its unitary transport at each site, followed by \(s^{-2}\); its squared norm is \(s^4s^{-4}|b_P|^2\). These counts prove (7.11) with the fine-cell weights included.

Since \(A_sF_b\) has norm at most \(C\|b\|_{\ell^2(\text{tops, count})}\), for every row \(\beta\)
\[
 |\langle\beta,b\rangle_{\rm top}|
 =|\langle SQ_U'^*\beta,A_sF_b\rangle_{\rm f}|
 \le C\|SQ_U'^*\beta\|_2\|b\|_{\ell^2(\text{count})}.
\]
The norm of the left functional on counting \(\ell^2\) is
\((\sum_P s_P^8|\beta_P|^2)^{1/2}\), because the top pairing has weight \(s_P^4\). Taking its supremum proves
\[
 Q'_US^2Q_U'^*\ge c\,m^4,\qquad
 0<(Q'_US^2Q_U'^*)^{-1}\le C\,m^{-4}                 \tag{7.12}
\]
as quadratic forms in the physical top pairing. This proves existence and a real scalar Gram gap, including the flat case. By itself it proves neither an exponential kernel nor a complex continuation; those are supplied next, followed by the output pointwise estimates.

### Weighted scalar energy and the top Gram kernel

The next argument supplies the exponential assertion for the scalar Gram inverse; the following paragraph then handles output pointwise estimates. It uses the real small-gauge hypotheses of the preceding paragraph. Write
\(\mathcal E(u)=\|D_Uu\|_2^2+\|a^{1/2}Q'_Uu\|_{\rm top}^2\);
(7.10) gives \(\mathcal E(u)\ge c\|m^{-1}u\|_2^2\).
Let \(w=e^{\mu d(\,\cdot\,,P')}\), with \(\mu>0\) small.
Along a fine bond \(|\log w(x)-\log w(x')|\le C_L\mu\eta/m_x\).
Within one pillar its oscillation is at most \(C\mu\).

For a real symmetric matrix \(A\), direct expansion gives
\[
 \operatorname{Re}\langle w^2u,Au\rangle-\langle wu,Awu\rangle
 =\tfrac12\sum_{x,z}\eta^4
       \operatorname{Re}\langle u(x),A(x,z)u(z)\rangle
                              (w(x)-w(z))^2.
\]
This formula uses the counting kernel for \(A\). For the scalar gradient term its off-diagonal coefficients have size \(\eta^{-2}\) on neighbors. For the mass term within a pillar of side \(s\), they have size at most \(\eta^4s^{-6}\); this follows by expanding \(Q'^*s^{-2}Q'\), since its transports are unitary. The inequality \(2ab\le a^2+b^2\), the preceding weight differences, and the sum of \(s^4/\eta^4\) sites in a pillar give
\[
 |\operatorname{Re}\langle w^2u,A_su\rangle-\mathcal E(wu)|
       \le C_L\mu^2\|m^{-1}wu\|_2^2.                \tag{7.13}
\]
At Dirichlet edges \(u=0\) outside the domain, so the boundary cross term is zero. Adjacent pillar scales differ by at most \(L\), which accounts for the constant at seams.

For \(u=Sf\), choose \(C_L\mu^2<c/2\), absorb the right side by (7.10), and apply Cauchy–Schwarz to \(\langle w^2u,f\rangle\). The result is
\[
 \mathcal E(wu)^{1/2}+\|m^{-1}wu\|_2
                   \le C\|mwf\|_2.                \tag{7.14}
\]
For \(u=SD_U^*g\), instead use
\(\langle w^2u,D_U^*g\rangle=\langle D_U(w^2u),g\rangle\).
The product rule writes \(D_U(w^2u)\) as a weight times \(D_U(wu)\), plus a term bounded by \(C_L\mu\,m^{-1}|wu|\,w\). Absorption gives the same left side bounded by \(C\|wg\|_2\). Therefore, for sources over \(y'\),
\[
 \begin{split}
 \|\mathbf1_y S\mathbf1_{y'}\|_{2\to2}
       &\le C m_y m_{y'}e^{-\mu d(y,y')},\\
 \|\mathbf1_y D_US\mathbf1_{y'}\|_{2\to2}
       &\le C m_{y'}e^{-\mu d(y,y')},\\
 \|\mathbf1_y SD_U^*\mathbf1_{y'}\|_{2\to2}
       &\le C m_y e^{-\mu d(y,y')},\\
 \|\mathbf1_y D_USD_U^*\mathbf1_{y'}\|_{2\to2}
       &\le Ce^{-\mu d(y,y')}.
 \end{split}                                       \tag{7.15}
\]
Replacing a pillar by its assigned top costs a bounded metric distance. On a fixed finite torus the weights are bounded, so no limiting existence argument is hidden here. All constants in (7.13)–(7.15) are uniform in that torus.

Put \(K=Q'S^2Q'^*\). Since \(\|Q'^*e_y\|_2=m_y^2\), (7.15) gives
\(\|\mathbf1_z SQ'^*e_y\|_2\le C m_z m_y^3e^{-\mu d(z,y)}\).
The top pairing has weight \(m_y^4\), so
\[
 |K(y,y')|_{\rm count}
 \le C m_y^{-1}m_{y'}^3
       \sum_z m_z^2e^{-\mu(d(z,y)+d(z,y'))}
 \le C m_y m_{y'}^3e^{-\mu' d(y,y')}.                \tag{7.16}
\]
The last step is exactly (5.6) with \(p=2\) and a reduced rate. The matrix
\(J=K m^{-4}\), in counting coordinates, is real symmetric and satisfies \(J\ge cI\) by (7.12). Its entries are bounded by
\(C(m_y/m_{y'})e^{-\mu'd(y,y')}\). Equation (5.2) absorbs this ratio into another fixed reduction of rate. Thus \(|J(y,y')|\le Ce^{-\nu d(y,y')}\), and both Schur sums are bounded.

For \(v_y=e^{\theta d(y,y_0)}\),
\[
 |(vJv^{-1}-J)(y,y')|
 \le C\theta\,d(y,y')e^{-(\nu-\theta)d(y,y')}.
\]
Section 5 bounds its two Schur sums by \(C'\theta\). Choose \(\theta<\nu/2\) and \(C'\theta<c/2\). Since \(\|J^{-1}\|_{2\to2}\le c^{-1}\), the resolvent series proves
\(\|(vJv^{-1})^{-1}\|_{2\to2}\le2/c\).
Apply it to a coordinate unit vector at \(y_0=y'\). This proves
\[
 |K^{-1}(y,y')|_{\rm count}
       =m_y^{-4}|J^{-1}(y,y')|
       \le C m_y^{-4}e^{-\theta d(y,y')}.             \tag{7.17}
\]
This is the required real scalar top-Gram kernel, with the new pillar means and the stated boundary spaces. It uses no flat propagator theorem. It does not yet yield the fine pointwise kernels of \(S\) or the derivative kernels of \(D(1-R)D^*\).

The same two conclusions, (7.15) and (7.17), have a controlled complex extension on the regular-pair class. Here are the relative estimates needed for that assertion. Write \(\mathbf U=e^{i\eta A'}U\), \(\|mA'\|_\infty\le\alpha_1\), and keep the real reference energy \(\mathcal E\). Expanding one transported shift shows
\(\|(D_{\mathbf U}-D_U)f\|_2\le C_L\alpha_1\|m^{-1}f\|_2\).
The local complex comparison of §8.7 and Cauchy in the reference variable show
\(\|a^{1/2}(Q'_{\mathbf U}-Q'_U)f\|_{\rm top}
\le C_L\alpha_1\|m^{-1}f\|_2\).
One may check the latter directly by summing the coefficient majorant
\(C_L\alpha_1\eta^4/s^4\) within each pillar and using Cauchy–Schwarz. Thus, with bilinear transposes,
\[
 |\langle f,(A_{\mathbf U}-A_U)g\rangle|
   \le C_L\alpha_1\mathcal E(f)^{1/2}\mathcal E(g)^{1/2}. \tag{7.18}
\]
Complex conjugation in estimating the absolute value does not change this bound. Conjugating the operator by \(w\) adds first-order form errors bounded by \(C_L\mu\) in the same energy norms: expand \(D(wf)\), and for \(Q'\) use its within-pillar weight oscillation. Choose \(C_L(\mu+\alpha_1)<c'\) small enough for the relative Neumann series in the Hilbert space with norm \(\mathcal E^{1/2}\). This proves invertibility, holomorphy and the weighted energy bounds for \(S_{\mathbf U}\), with (7.15) unchanged up to constants. This is a form argument; it does not assume a bounded pointwise derivative of the current.

For completeness it also controls the Gram inverse without confusing a bilinear square with positivity. Let \(T_z=S_zQ_z'^*\) and \(T_0=SQ'^*\). The resolvent identity and (7.18), applied to a source \(e_y\), give
\[
 \|\mathbf1_x(T_z-T_0)e_y\|_2
   \le C_L\alpha_1 m_xm_y^3e^{-\mu d(x,y)}.
\]
Indeed the difference of the direct sources has weighted energy-dual norm
\(C_L\alpha_1m_y^3\); the other source is
\(-(A_z-A_0)T_z e_y\), whose weighted dual norm is bounded by (7.18) and (7.14). Taking the bilinear products \(T_z^{\mathsf T}T_z\), subtracting the real product, and using exactly the sum in (7.16) gives
\[
 |(J_z-J_0)(y,y')|\le C_L\alpha_1e^{-\nu d(y,y')}.
\]
Its norm, and its small exponential conjugates, are \(O_L(\alpha_1)\) by §5. Choose that norm below \(c/4\) and repeat the inverse-series argument for \(J_0\). It gives (7.17) for the complex Gram inverse and proves its holomorphy. Positivity is used only at the real reference. This closes the scalar existence, weighted \(L^2\) and top-Gram parts. The next argument supplies the scalar pointwise members needed for the projection; the vector construction is separate.

### Scalar value/gradient bounds and the regular projection kernel

The pointwise part needed for the projection can also be obtained from the energy bounds. The following local argument is written out to avoid treating a Sobolev endpoint as automatic. On an embedded cube with side comparable to \(r\), in fine units, suppose
\(\Delta_Uu=g\), \(U\) is real, and a local gauge obeys
\(|A|\le\delta/r,\ |\nabla A|\le\delta/r^2\). Then on a fixed smaller cube,
\[
 |u|+r|\nabla_Uu|
       \le C\{r^{-2}\|u\|_{2,\mathrm{larger\ cube}}
                                      +r^2|g|_\infty\}. \tag{7.19}
\]
The constants are uniform in the number of fine sites when \(\delta\) is sufficiently small.

Here is a proof. Positivity of the scalar Dirichlet Green function follows from the maximum principle. Its infinite-lattice counterpart is nonnegative: integrate
\(e^{-t\Delta}=e^{-8t}\sum_{n\ge0}t^n\mathcal A^n/n!\),
where \(\mathcal A\) is the nearest-neighbor adjacency matrix; every entry is nonnegative. Fourier integration identifies the integral with the convergent formula in §12. For an interior point of a cube and a site one step from a face, its Dirichlet Green function is bounded above by the half-space Green function, by the maximum principle. Reflection expresses the latter as the difference of two infinite-lattice Green functions with arguments two steps apart. Equation (12.1) bounds this by \(Cr^{-3}\). Hence each coefficient of the cube's Poisson kernel, seen from a fixed inner cube, is at most \(Cr^{-3}\). Also the sum of its Dirichlet Green kernel is at most \(Cr^2\): compare the equation \(\Delta v=1\), \(v=0\) at the boundary, with a positive quadratic polynomial whose Laplacian is one.

The covariant Kato inequality is elementary here:
\(\Delta|u|(x)\le|\Delta_Uu(x)|\).
At a nonzero \(u(x)\), take its unit vector in the equation and use
\(\operatorname{Re}\langle u(x)/|u(x)|,\operatorname{Ad}U(x,z)u(z)\rangle
\le|u(z)|\); at zero the inequality follows directly. Choose a cube radius between \(r\) and \(2r\) whose boundary squared norm is at most \(C r^{-1}\|u\|_2^2\). Such a radius exists by summing the disjoint shells. Comparison with its harmonic extension and the Poisson/Green bounds just proved gives
\[
 |u|_{\rm inner}\le
 Cr^{-3}r^{3/2}(r^{-1}\|u\|_2^2)^{1/2}+Cr^2|g|_\infty
 =C(r^{-2}\|u\|_2+r^2|g|_\infty).
\]
Use a fixed larger outer cube so this estimate holds throughout the region where the gradient will be bounded.

In the local gauge write
\(\Delta u=g+B\nabla u+Cu\), with
\(|B|\le C\delta/r,\ |C|\le C\delta/r^2\);
these coefficients follow by the paired-shift expansion used in §12.
For an ordinary Poisson equation on a cube of radius \(d\), its central gradient is bounded by
\[
 C d^{-1}\sup|u|+C d\sup|\Delta u|.
\]
To verify this estimate, write the solution as its harmonic extension plus the Dirichlet Green integral. A harmonic gradient is bounded by \(C d^{-1}\sup|u|\), using Lemma H on its differences and Caccioppoli. For the Green integral, subtract from the full-space convolution its harmonic boundary correction. Equation (12.1) sums its first derivative to \(Cd\); its boundary values are at most \(Cd^2\sup|\Delta u|\), so the same harmonic gradient estimate bounds the correction.

Finally maximize \(d(x)|\nabla u(x)|\) on an inner cube, where \(d(x)\) is the distance to its boundary. At a maximizer with \(d(x)\) larger than a fixed number of mesh steps, apply the preceding estimate on a cube of radius \(d(x)/4\). On that cube \(d\) is comparable to \(d(x)\), so the drift term is at most \(C\delta\) times the same maximum. Absorb it. At a maximizer within a bounded number of mesh steps, the elementary bond difference is bounded by twice the value supremum and already gives the result. Thus
\(|\nabla u|_{\rm inner}\le C(r^{-1}\sup|u|+r|g|_\infty)\).
This completes (7.19). Restoring spacing \(\eta\) preserves its displayed dimensions.

Apply it to \(u=Sf\), where \(f\) is supported over \(y'\), and set \(F=|f|_\infty\). At a point of pillar \(P\),
\[
 |Q'^*aQ'u|\le m_P^{-4}\|u\|_{2,P}.
\]
By (7.15), \(\|u\|_{2,P}\le C m_Pm_{y'}^3e^{-\mu d(P,y')}F\).
Take a local cube of radius a sufficiently small fixed multiple of \(m_y/L\) around an output point over \(y\). Its larger cubes meet only neighboring scales, remain inside \(\Omega_0\) when \(m_y>\eta\), and meet only a bounded number depending on \(L\) of pillars. The norms in (7.19) are therefore bounded by those just displayed. The direct \(f\) term is zero unless its supporting pillar is nearby; in that case the two scales and distances are comparable and the same bound applies. We obtain
\[
 |Sf|_y\le C m_y^{-1}m_{y'}^3e^{-\mu'd(y,y')}F,\qquad
 |\nabla_USf|_y\le C m_y^{-2}m_{y'}^3e^{-\mu'd(y,y')}F.
\]
Absorb the ratio \((m_{y'}/m_y)^3\) by (5.2). The equation itself bounds \(\Delta_USf=f-Q'^*aQ'Sf\); (12.2) bounds the Hölder difference of the gradient. Thus
\[
 |Sf|_y,\ |\nabla_USf|_y,\ |\Delta_USf|_y,
       [\nabla_USf]_{\alpha,y}
 \le C_\alpha[m_y^2,m_y,1,m_y^{1-\alpha}]
                         e^{-\mu''d(y,y')}F.          \tag{7.20}
\]
For a bare output pillar use \(|u(x)|\le\eta^{-2}\|u\|_{2,\{x\}}\) in (7.15), and then the finitely many neighboring values for the existing differences and Laplacian. This gives the same bounds, including near an arbitrary outer boundary. Hence an embedded local PDE cube is not being assumed at a hole.

These bounds extend to the complex scalar operator with the stated first-order control of \(A'\). In the fixed real gauges, paired shifts and the averaging coefficient differences give, for \(V=A_{\mathbf U}-A_U\),
\[
 |Vh|_y\le C_L\alpha_1
  \max_{z\ {\rm near}\ y}
       \{m_z^{-2}|h|_z+m_z^{-1}|\nabla_Uh|_z\}.
\]
“Near” here means the finitely many neighboring pillars of the covariant shifts and the single pillar of each scalar average; their scales are comparable. The paired-shift coefficient uses
\(|A'|\le\alpha_1/m,\ |\nabla_UA'|\le\alpha_1/m^2\).
By (7.20) and §5, \(VS\) has norm \(C_L\alpha_1\) on every exponential-weighted force supremum space being used. Choose it below \(1/2\); then
\(S_{\mathbf U}=S(I+VS)^{-1}\) gives the value/gradient bounds on that common complex domain. The equation and §12 give the other members of (7.20). This series is holomorphic and agrees with the energy inverse by uniqueness. This argument does not assert the mixed-derivative bounds for a merely bounded differentiated source.

Now set \(F_y(x)=(SQ'^*e_y)(x)\). It is a response to a bounded source in one pillar, so (7.20) gives its values, first differences and gradient Hölder differences, uniformly also on the complex class. Since
\[
 (I-R)(x,x')_{\rm count}
  =\eta^4\sum_{a,b}F_a(x)\,N(a,b)_{\rm count}
                                      m_b^{-4}F_b(x')^{\mathsf T},
\]
insert (7.17) and (7.20), and apply (5.6) twice, redistributing endpoint powers before summing. For zero or one derivative at either endpoint this gives
\[
 |\nabla_x^r(I-R)(x,x')(\nabla_{x'}^{\mathsf T})^t|_{\rm density}
   \le C m_y^{-2-r}m_{y'}^{-2-t}e^{-\mu_0d(y,y')},
 \quad r,t\in\{0,1\}.                                \tag{7.21}
\]
For example the undifferentiated product contributes
\(m_y^2m_{y'}^2m_a^{-4}m_b^{-4}\) before the two sums; moving the two inverse powers to the matching endpoints leaves
\(m_y^{-2}m_{y'}^{-2}\). A derivative lowers its endpoint power by one; a gradient Hölder quotient lowers it by a further \(\alpha\). This proves the regular projection kernel, including the particular \(D(1-R)D^{\mathsf T}\) member needed by the vector operator. Every rate loss here is fixed and positive; choose the gap large enough for the finite collection of §5 sums. Localization to a changed sequence and the vector inverse have not been obtained by this kernel calculation.

## 8. Average, gauge and class transfers

### 8.1 Centring at identity has an exact finite-depth transfer

Credit Bałaban for the corner-block construction and the outline's authors for identifying the centring issue. On a torus whose side is a multiple of \(s_k=L^k\eta\), write the old blocks as
\(a+\{0,\eta,\ldots,s_j-\eta\}^4\), \(a\in s_j\mathbb Z^4\).
Translate **all fine sites and all regions once**, by
\[
 t=-\tfrac12(s_k-\eta)(1,1,1,1).
\]
The translated block is the centred block with centre
\[
 c=a-\tfrac12(s_k-s_j)(1,1,1,1)\in s_j\mathbb Z^4,
\]
since \(L^{k-j}\) is odd. This works simultaneously for every \(j\): its lower corner is exactly \(c-(s_j-\eta)/2=a+t\). Relabel each coarse site and row by these centres. A straight path from \(x\) to \(x+s_je_\nu\) translates to the same straight path in the translated block. At identity the straightened bond average and the scalar pillar average are therefore exactly intertwined by the fine translation and the coarse relabelling. The curl, gradient, cell measures and **matching** Dirichlet compressions are intertwined too. Equations (3.1) and (6.1) transfer their inverses algebraically whenever they exist.

This establishes centring for the flat straight-average propagators, with no accumulation over depth. Assigned centres differ from the translated corner nodes within their own pillars, a bounded metric distance, so endpoint exponential bounds change by only a constant. It does not transfer a corner-based axial tree into the outline's soft axial coordinates, does not change inward-bond conventions, and does not change a compressed action into the action of inner plaquettes. Those are different operations.

### 8.2 A curved contour mean is genuinely a different row

The outline's contour mean is the near-family solution of
\(\sum_\gamma\log(U(\gamma)V^{-1})=0\), over coordinate-ordered shortest paths (outline lines 7065–7076). Bałaban's CMP 98 construction uses one comb. Even after aligning base sites and using the centred comb comparator, the distinction is explicit in one block. Take \(L\ge5\), a centred block with centre \(0\), \(x=\eta(e_1+e_2)\), and all links equal to identity except
\[
 U(\eta e_1,\eta(e_1+e_2))=e^{it\sigma_3},\quad 0<t\ll1.
\]
The two orders of the nonzero directions give \(e^{it\sigma_3}\) and \(I\). The symmetric mean is \(e^{it\sigma_3/2}\), since the two logarithms about this value are \(\pm it\sigma_3/2\). The comb order \(4,3,2,1\) gives \(I\). For a scalar color field supported at \(x\) with value \(\sigma_1\), the level-one pillar rows differ by
\[
 L^{-4}\big(\operatorname{Ad}(e^{it\sigma_3/2})\sigma_1-\sigma_1\big)\ne0. \tag{8.1}
\]
The nonvanishing follows by multiplying the two diagonal entries of \(e^{it\sigma_3/2}\) against the off-diagonal entries of \(\sigma_1\). Every affected plaquette is \(e^{\pm it\sigma_3}\); its current is bounded by a fixed multiple of \(t\eta^{-3}\), the local logarithmic potential by \(t\eta^{-1}\), its first differences by \(2t\eta^{-2}\), and its second differences by a fixed multiple of \(t\eta^{-3}\). Thus, on a one-layer torus, choosing \(t\) below \(c\varepsilon L^{-3}\) meets all the smallness requirements, including the stronger second-order one. This is an admitted small **regular field**, without a claim of criticality. It prevents literal identification of the propagators on the regular-pair class, but is not a counterexample to their perturbative comparison.

The elementary real-field comparison is an area estimate: interchanging two neighboring coordinate segments changes a path by a rectangle; at most six such interchanges compare two coordinate orders in four dimensions. If all intervening plaquettes satisfy \(\|U(p)-I\|\le\epsilon\eta^2/s^2\), the product/telescoping identity for unitary matrices bounds the difference of transports on a cube of side \(r\le s\) by \(C\epsilon(r/s)^2\). Each plaquette is conjugated by a unitary transport, which preserves the norm, and a rectangle contains its area divided by \(\eta^2\) plaquettes. This proves the estimate without commuting the plaquettes. A near-diagonal group mean obeys the same value estimate: write its logarithmic equation in a ball about one transport; its derivative in the unknown is \(-I+O(\epsilon(r/s)^2)\), so the contraction map obtained by adding that equation to the unknown has norm below \(1/2\) when the radius is small. Integration of that derivative and the bound on its value at zero give the bound for the fixed point.

The first transfer needed beyond this value comparison is the derivative-density and column-sum bound for the iterated straightened average. CMP 98 (124), (139)–(157) obtains that bound from its explicit single-comb formula. For the contour-mean map and its accumulated site factors the needed relative one-step errors are
\[
 e_m\le C_L\{\epsilon L^{-2(j-m)}+rL^{m-j}\},           \tag{8.2}
\]
in both row and column norms, and the local functional-derivative versions including their \(\eta^4\) factors. Given (8.2), its accumulation is harmless:
\[
 \prod_{m<j}(1+e_m)
 \le\exp\!\left(C_L\left\{\frac{\epsilon}{L^2-1}
                              +\frac r{L-1}\right\}\right).
\]
This last inequality is proved by \(\log(1+x)\le x\) and the two geometric sums. The premise (8.2), with derivatives and seam folding, is asserted in outline (1b), mechanism 1, and Proposition 1a.1.13. The single-step argument below verifies a local part of that premise and isolates what its iteration still needs. A per-level \(O(\epsilon)\) comparison would instead allow \(e^{Ck\epsilon}\) and would not discharge A3.

### 8.3 Gauge and regular-class requirements

Once the scalar propagators for the **new** \(Q'\) have their uniform bounds, (3.3) gives the linear change to its Landau slice. This algebra neither constructs the nonlinear gauge factor nor bounds its values at tops. The needed nonlinear normalization is exactly
\(u_B(y)v_j[\mathcal H(B)](y)=I\). Its derivative requires the uniform composite bounds on the site factors in (8.2); a choice of nodal values cancelling an unrelated contour functional is not an admissible replacement.

CMP 99a Proposition 6, pp. 98–99, supplies local logarithmic gauges from curvature **and current** on a larger cube, with bounds of size \(CM\alpha_0\), and requires \(CM\alpha_0\) small. Its proof constructs a nested sequence around the cube, gauges the averages, and uses that paper's earlier gauge theorem. It is not a curvature-only lemma. The outline's proposed application erodes the first member before extending by identity (outline line 9801); this is meant to keep every protruding plaquette read by Proposition 6 inside the original domain. That geometric inclusion and the gauge theorem it invokes must both hold. An arbitrary extension by identity need not preserve small curvature on protruding plaquettes.

Moreover the outline's arbitrary regular pair has an independent \(\mathbf J\), a gauge bound on a cube of \(\alpha_0\) rather than \(CM\alpha_0\), and only first-order control of the complex perturbation. CMP 99b 3.12–3.13 assumes (3.36) and the physical-current construction. CMP 99b 3.4 alone does not prove the independent-current extension. The explicit current-defect equation in outline (1c), statement 3, is the first identity that must be retained in such a port. Matching field strength alone is insufficient.

### 8.4 The one-step contour-mean derivative can be transferred

Here is a direct local proof, rather than an appeal to Bałaban's unproved generalization to other averages. Fix \(L\) and an embedded double block with the fixed enlargement needed for its contour paths. Normalize its fine spacing to one. For \(W_0\) with plaquette size at most \(q\), the coordinate-tree gauge expresses each remaining link as a product of a bounded number, depending only on \(L\), of conjugated plaquettes. Telescoping the product gives \(\|W_0^g-I\|\le C_Lq\). The gauge is unitary, and may be fixed once at the reference; thus it changes no row or column norm of the derivative.

In this averaging subsection \(S_W\) denotes the one-step straightening map, not the scalar inverse \(S\) of §§3 and 7.

All operations in a single step involve finitely many matrices, at most a number depending on \(L\). Their logarithms and exponentials are holomorphic on a fixed ball about identity. For each contour mean, its logarithmic equation has derivative \(-I\) in the unknown at identity, after division by the number of contours. Write that equation as \(-v+f(v,z)=0\); on a sufficiently small fixed ball, the derivative of \(f\) in \(v\) is at most \(1/2\). The contraction gives the mean and its holomorphy there. Its derivatives of orders at most three are bounded on a smaller closed ball by Cauchy's integral formula. Define \(C_L\) to dominate those finite derivative bounds, the number of local bonds and the number of rows reading any one fine bond. This is a stated existence definition of a finite constant, independent of mesh, volume and depth.

For completeness, the straightening used in this calculation is explicit. Write \(W=e^{ia}W_0\), \(V_y(x)=W(y,x)W_0(y,x)^{-1}\), and let \(v_y\) be its block mean. Set
\[
 g(x)=W_0(y,x)^{-1}v_y^{-1}W(y,x),\qquad x\in B(y).
\]
Then \(g(y)=v_y^{-1}\) and covariance of the contour mean gives \(W^g(y,x)=W_0(y,x)\). The one-step straightened logarithm is that of \(\mathcal M(W^g)\mathcal M(W_0)^{-1}\). At identity, differentiating the contour mean gives the arithmetic contour sum. The ordinary average's two site terms are the difference of the block means of that sum; the two factors \(v_y^{-1}\) cancel them. Its derivative is therefore exactly the straight-path average. This proves the cancellation used in comparing the schemes; the plain derivative would fail this test.

The straight-path matrix has row sum \(L\) and column sum \(L^{-3}\): each row averages \(L^4\) paths of length \(L\); at a fixed parallel bond, the two adjacent longitudinal tents have total weight \(L\), multiplied by \(L^{-4}\). The finite derivative bounds just established imply for the actual one-step straightened Jacobian \(S(W_0,a)\), with \(u=\sup|a|\),
\[
 \|S(W_0,a)\|_{\rm row}\le L[1+C_L(q+u)],\qquad
 \|S(W_0,a)\|_{\rm col}\le L^{-3}[1+C_L(q+u)].         \tag{8.3}
\]
Indeed compare in the fixed tree gauge with its value at \((I,0)\), integrate its bounded derivative along the segment of logarithmic coordinates, and sum the finitely many coefficients. The factors \(L\), \(L^{-3}\) are absorbed into the definition of \(C_L\) for the error. The same argument gives a difference bounded by \(C_Lu\) between the Jacobians at \(a\) and at zero, in both relative norms. Complex \(a\) is included in this analytic ball; no complex gauge chosen afresh is needed.

A useful additional check is the exact leading curvature coefficient. At identity the coarse curl kills the site terms and
\[
 (d_{\rm coarse}Q_{\rm path}a)_{\mu\nu}(y)
 =L^{-4}\sum_{x\in B(y)}\sum_{r,t=0}^{L-1}
           (da)_{\mu\nu}(x+re_\mu+te_\nu).            \tag{8.4}
\]
This is obtained by telescoping first the \(\mu\)-edges and then the \(\nu\)-edges; all interior edges cancel. Its coefficients are positive and total \(L^2\). In the tree gauge \(|a|\le C_Lq\), the fine plaquette logarithm is \(da+O_L(q^2)\), and the coarse one is the left side of (8.4) plus \(O_L(q^2)\), by the bounded second derivatives of the finite analytic functions. For real plaquettes the logarithm has norm at most \(q+C_Lq^2\). Therefore
\[
 q_{m+1}\le L^2q_m+C_Lq_m^2.                          \tag{8.5}
\]
If this recurrence is applicable to every reference read set below a row of height \(j\), starting with \(q_0\le\epsilon L^{-2j}\), it gives \(q_m\le2\epsilon L^{2(m-j)}\). To check the induction, put \(b_m=L^{2(j-m)}q_m\); while \(b_m\le2\epsilon\), its accumulated increase is at most \(4C_L\epsilon^2/[L^2(L^2-1)]\), which is below \(\epsilon/2\) for a fixed sufficiently small \(\epsilon\).

Thus the factor \(L^2\), and the local derivative comparison, have written proofs. Their iteration needs the domain and composition check next; (8.3)–(8.5) alone would not certify it.

### 8.5 Iterating the straightened rows on the no-inward geometry

This subsection proves the averaging input at a **real** reference with the outline's small curvature profile, on its standard geometry without inward rows. It is not yet a comparison of the two curved propagators. Credit Bałaban, CMP 98 (139)–(157), for the geometric accumulation method, and the outline's authors for the straightened composition and the summable-error prescription (outline lines 9808–9821).

Fix a row of height \(j\ge1\). To evaluate its composition, form its read sets backwards: include the bonds of each one-step double block, the coordinate rectangles needed to compare its contours, and the plaquettes used by the local tree gauge. Each backwards step adds at most \(c_L L^m\) fine spacings at height \(m\). Therefore the complete fine read set is within \(a_Ls_j\) of the row's double block, where one may take \(a_L=4+c_L/(L-1)\), increased to accommodate the fixed first step. This is a geometric sum, not a depth-dependent enlargement. Choose the gap so that \(\rho>4(a_L+2)L\), and take the stipulated nonwrapping floor for these enlarged cubes. Every such read set is inside \(\Omega_{j-1}\) and \(\Omega_0\): the distance from \(\Omega_j\) to \(\Omega_{j-1}^c\) exceeds \(\rho s_{j-1}\); the outer block of an outward row adds at most \(2s_j\). For an interior row the inclusion is easier. The smallest local scale read is consequently \(s_{j-1}\); encountering a higher layer only improves the curvature bound. This proves the missing scale comparison, with the gap chosen after the finite local constants.

On these successive read sets put \(W_m=\mathcal M^mU_0\). Their plaquette norms \(q_m\) obey (8.5), with shrinking read sets as just specified, and
\(q_0\le L^2\varepsilon L^{-2j}\). The induction following (8.5) gives
\[
 q_m\le2L^2\varepsilon L^{2(m-j)},\quad 0\le m\le j,    \tag{8.6}
\]
after a fixed reduction of \(\varepsilon\). All references remain real and unitary. Local gauges at different steps need not agree: (8.3) is a norm estimate, invariant under the fixed real gauge at that step.

Let \(a_0=\eta A\), with \(\sup\xi|A|\le r\). On the read set of an actual row, \(|a_0|\le LrL^{-j}\). Define recursively
\(a_{m+1}=S_{W_m}(a_m)\), using the one-step straightening of §8.4. Its value at zero is zero. Integration of (8.3) along the segment from zero to \(a_m\) gives
\[
 u_{m+1}\le L[1+C_L(q_m+u_m)]u_m,\qquad
 u_m:=\sup|a_m|.
\]
Here and below the supremum is on the corresponding backwards read set. Bootstrap \(u_m\le2LrL^{m-j}\). Under that bound, the product of the correction factors is at most
\[
 \exp C_L\left\{\frac{2L^2\varepsilon}{L^2-1}
                         +\frac{2Lr}{L-1}\right\}<\frac32.
\]
Choose \(r,\varepsilon\) so this holds and so \(2Lr\), \(2L^2\varepsilon\) lie in the one-step analytic balls. The bound improves the bootstrap to \(u_m\le(3/2)LrL^{m-j}\); finite induction proves it at every depth. The proof includes complex \(a_0\). It uses the real reference only for the gauges and the curvature recurrence.

The composition is exact, not a product of approximate averages. If
\[
 \mathcal M^m(e^{i\eta A}U_0)
       =v_m e^{ia_m}W_m v_m^{-1}
\]
on bonds, gauge covariance and the one-step identity give this equation at level \(m+1\), with
\(v_{m+1}=v_m|_{\text{new sites}}\,\mathsf v_m(a_m)\).
The initial values are \(v_0=I\), \(a_0=\eta A\). This proves by induction the outline's \(\mathcal Q^{\rm st}_j(A)=a_j\) and its specified accumulated site factors. Each one-step read is in a double block, so nesting also proves that the un-enlarged functional itself reads only the final double block. The enlargement above was used for estimates, not for a different definition.

Multiplication of the row and column bounds (8.3), and the preceding geometric sum, now proves
\[
 \|D_{a_0}a_j\|_{\rm row}\le C_LL^j,\qquad
 \|D_{a_0}a_j\|_{\rm col}\le C_LL^{-3j}.              \tag{8.7}
\]
For the column norm take all rows of a fixed height on their required read sets; deleting rows only decreases the estimate. At each intermediate level the number of rows reading a bond is the finite incidence number used in (8.3). Therefore the matrix-product column estimate applies, rather than multiplying a row estimate by the total number of rows.

The matrices in (8.7) are holomorphic for \(\sup|a_0|<r_*L^{-j}\), with \(r_*>0\) depending on \(L\) alone. Cauchy's formula on a smaller ball gives
\[
 \|D a_j(a_0)-D a_j(0)\|_{\rm row}\le C_LrL^j,
 \qquad
 \|D a_j(a_0)-D a_j(0)\|_{\rm col}\le C_LrL^{-3j}.    \tag{8.8}
\]
Here \(L^j\sup|a_0|\le Lr\), with the factor \(L\) absorbed in \(C_L\). To see that this is a Banach-norm estimate, restrict to the complex line \(a_0+t h\), apply the Cauchy integral to the matrix itself, and use (8.7) under the integral; then integrate its derivative from zero to \(a_0\). Repeating on independent complex lines proves the corresponding multilinear estimates of orders two and three, with the usual factorials. It does not multiply a bound separately for every fine coordinate.

In physical variables a coefficient in (8.7) is at most
\(C_L\eta L^{-3j}=C_L\eta^4s_j^{-3}\). Thus its transpose in the fine-cell pairing has size \(C_Ls_j^{-3}\), exactly the force-density power. A fine bond is read by rows at its own pillar height and, possibly, outward rows of the next height; the gap excludes any other height, and the double-block geometry bounds their number at each height. This proves the transpose estimate after summing rows. The double block has bounded \(d_{\mathbf B}\)-diameter, at most a constant depending on \(L\); its only scales are \(s_j,s_{j-1}\). Hence the same proof works with any weight satisfying \(w(x)/w(z)\le e^{\mu d_{\mathbf B}(x,z)}\), at a cost \(e^{C_L\mu}\).

Consequently, for \(C(A)=\mathcal Q^{\rm st}(A)-K_0A\), the local bounds \(C(0)=C'(0)=0\), \(C'=O(\|A\|_X)\), \(C''=O(1)\), and \(C''(A)-C''(0)=O(\|A\|_X)\) hold both as row maps and as the force-valued transposes required in §9. The estimate uses only the potential member of \(X\), so adjoining its first-difference member is legitimate. Level-zero rows are exactly linear. This discharges §9's averaging input on this real-reference, no-inward domain. It does not discharge the propagator inputs there, or extend them to the outline's independent-current complex pair.

The site factors also satisfy \(\|\mathsf v_m-I\|\le C_Lu_m\), directly from their finite analytic formula. Product telescoping and \(\sum_m u_m\le2Lr/(L-1)\) give
\[
 |v_j-I|+|v_j^{-1}-I|\le C_Lr.                       \tag{8.9}
\]
Their Cauchy derivatives have the same local weighted bounds. This proves the top-factor estimate once a potential \(A\) with the required response has been constructed; it does not construct that potential.

### 8.6 The actual outward reduced row

The nonlinear seam identity can now be checked directly. Let \(c\in\Gamma_j\) have its outer end \(z=c_+\) in layer \(j-1\). All level-\((j-1)\) bonds within \(B(z)\) are interior determining rows. On those rows the straightened data are exactly \(B\). Thus the one-step factor \(\mathsf v_z\) in \(v_j(z)=v_{j-1}(z)\mathsf v_z\) is the finite analytic function of those interior data \(B\) and of \(W_{j-1}\), with no unknown field left in it.

At the inner top impose \(u(c_-)v_j(c_-)=I\), and at the outer top impose \(u(z)v_{j-1}(z)=I\). The exact factorization of §8.5 gives
\[
 M_{\mathbf B}((e^{i\eta A}U_0)^u)(c)
     =e^{i\mathcal Q^{\rm st}_j(A)(c)}\mathbf V_0(c)
                           \mathsf v_z(B)^{-1}.
\]
Therefore this row equals \(e^{iB(c)}\mathbf V_0(c)\) precisely when
\[
 e^{i\mathcal Q^{\rm st}_j(A)(c)}
      =e^{iB(c)}\operatorname{Ad}(\mathbf V_0(c))
                                      \mathsf v_z(B). \tag{8.10}
\]
At an interior row both endpoint factors cancel and \(\mathsf b(B)=B\). Reflecting the orientation gives the other outward formula. Because \(\mathsf v_z\) reads only interior rows, the inverse of \(B\mapsto\mathsf b(B)\) first leaves those rows fixed and then solves (8.10) by multiplication and the unique small logarithm for each outward row. This proves local holomorphy, invertibility and \(\sup|\mathsf b(B)|\le C_L\sup|B|\), with uniformly local derivatives. There is no recursion through outward rows. The relevant row neighborhoods have bounded weighted diameter and at most \(O(L^4)\) interior rows, so the same conclusion holds in the weighted norms used in §9.

This proves the no-inward **constraint** transfer and its top normalization. It does not identify a solution of the inner-plaquette stationarity equations with a solution for a different boundary action. Inward seam nodes have a different normalization and are not covered by (8.10).

### 8.7 What can be compared to the flat rows in a fixed local gauge

The derivative norm in (8.7) can be sharpened to \((1+C_L(\varepsilon+r))L^j\) and \((1+C_L(\varepsilon+r))L^{-3j}\), since its product is \(\exp(O_L(\varepsilon+r))\). This alone does not prove closeness to the flat matrix; coefficients could have different transports. The following argument accounts for those transports.

Suppose on the complete read neighborhood of a height-\(j\) row a fixed real gauge has \(U_0=e^{i\eta A_0}\), \(\sup|A_0|\le\delta/s_j\), with \(\delta\) small. Apply the composition of §8.5 to this field as a perturbation of identity. Its straightened intermediate fields \(b_m\) and site factors \(t_m\) satisfy
\[
 \mathcal M^mU_0=t_m e^{ib_m}t_m^{-1},\quad
 |b_m|\le C_L\delta L^{m-j},\quad
 t_{m+1}=t_m z_m,\quad |z_m-I|\le C_L\delta L^{m-j}.
\]
These estimates also follow directly from the value recursion with reference curvature zero. In particular \(|t_m-I|\le C_L\delta\). By gauge covariance, the one-step derivative at \(\mathcal M^mU_0\) is
\[
 S_m'=\operatorname{Ad}(t_m)|_{m+1}
              (Q_0+E_m)\operatorname{Ad}(t_m)^{-1}|_m,
\]
where \(Q_0\) is the unit-step straight-path matrix and the finite analytic estimate at \(e^{ib_m}\) gives
\(\|E_m\|_{\rm row}/L,\ \|E_m\|_{\rm col}/L^{-3}
\le C_L\delta L^{m-j}\).
When these matrices are multiplied, adjacent transports do not create one unsummable error per level. Their product is exactly
\(\operatorname{Ad}(t_{m+1})^{-1}\operatorname{Ad}(t_m)
=\operatorname{Ad}(z_m^{-1})\), at the common level. These are the same summable errors. Expand the difference of the two products by replacing one factor at a time; bound the preceding and succeeding products by the exponential of the sum of their relative errors. This gives
\[
 \frac{\|K_{0,j}/\eta-Q_0^{j}\|_{\rm row}}{L^j}
  +\frac{\|K_{0,j}/\eta-Q_0^{j}\|_{\rm col}}{L^{-3j}}
       \le C_L\delta.                               \tag{8.11}
\]
Here \(K_{0,j}\) differentiates the dimensionless row with respect to the physical fine potential; \(K_{0,j}/\eta\) differentiates with respect to fine link angles. The remaining output factor \(\operatorname{Ad}(t_{j-1})\) differs from identity by \(O_L(\delta)\), and is included in (8.11). This proof does not require one common tree gauge at every intermediate level.

For the scalar pillar transport, write each factor at level \(m\) using
\(\mathcal M^mU_0=t_m e^{ib_m}t_m^{-1}\).
The contour mean for \(e^{ib_m}\) differs from identity by \(C_L|b_m|\). At consecutive levels the intervening factors again reduce to \(z_m^{\pm1}\). Telescoping the product proves \(|\mathsf T(y,x)-I|\le C_L\delta\) in the fixed fine gauge, including its endpoint factor. Each fine site occurs in exactly one pillar mean of that height. Therefore
\[
 \|Q'_j-Q'_{j,0}\|_{\rm row}\le C_L\delta,
 \qquad
 \|Q'_j-Q'_{j,0}\|_{\rm col}\le C_L\delta L^{-4j}.     \tag{8.12}
\]
Equations (8.11)–(8.12), with the cell-volume conversion of §6, are the local row perturbations needed in a parametrix. They apply to every row contained in a patch carrying the assumed small gauge. With Bałaban's single comb in place of the contour mean, the same finite analytic calculation and the same exact flat derivative give these inequalities as well. After aligning base sites by their reference transports, the difference of the two curved schemes consequently obeys the sum of their two bounds. This is a local quantitative transfer, not a literal identification of the two scalar projections or of their inverses.

There is a local complex-reference extension which does not require a second-order bound. The preceding construction of \(b_m,t_m,z_m\) used the identity as reference; it therefore works for a complex \(A_0\) in the same small potential ball. Now add a perturbation to that complex reference. If its straightened increments are \(a_m\), set \(\widehat a_m=\operatorname{Ad}(t_m^{-1})a_m\). Gauge covariance gives the exact recursion
\[
 \widehat a_{m+1}
   =\operatorname{Ad}(z_m^{-1})S_{e^{ib_m}}(\widehat a_m).
\]
The relative row and column errors are bounded by
\(C_L(\delta L^{m-j}+|\widehat a_m|)\). Their sum is finite, just as in §8.5. The bootstrap there applies with \(q_m\) replaced by \(\delta L^{m-j}\). Only the final factor \(\operatorname{Ad}(t_j)\), bounded by \(1+C_L\delta\), remains; one must not multiply that bound separately at every level. This proves (8.7)–(8.9) and their Cauchy/transpose versions at such complex references.

For a regular pair in (1c), use the real gauge provided on a cube containing the row's double block. In that gauge
\(\mathbf U=e^{i\eta A'}e^{i\eta A_0}=e^{i\eta\widetilde A}\), with
\(s_j|\widetilde A|\le C_L(\alpha_0+\alpha_1)\); the logarithm exists by its convergent local series. An outward double block uses the cube at height \(j-1\), costing the fixed factor \(L\), not a number of layers or \(M_1\). The gap and \(M_1\gg L\) put this cube in the two allowed layers. The complex-reference argument therefore supplies the same averaging input on this no-inward regular-pair class, with radius independent of \(M_1\). The independent current does not enter the averaging maps. This does not yet prove any of the propagator assertions at that pair.

The Ward identity is also exact for the new rows. Differentiate a site gauge transformation of \(U_0\). Gauge covariance of the contour mean makes the derivative of its block factor equal to the gauge parameter at the base minus its transported block mean. In the straightened average the base terms cancel, leaving the coarse difference of that mean. Thus, with consistent orientations,
\(QD\lambda=\bar D Q'\lambda\).
At an outward end the height-\(j\) mean is the transported mean of the height-\((j-1)\) pillar means: expand the nested sums and multiply the defining contour transports. If every actual top mean vanishes, this outer mean vanishes too. It follows that \(QD\lambda=0\) on \(\ker Q'\), supplying the constraint identity assumed in §§3 and 6. This algebra does not use stationarity; the separate Hessian identity does use the physical current.

## 9. The missing nonlinear differentiation, with its exact inputs exposed

This section gives a **conditional** replacement for the omitted CMP 102 (189) calculation. It is useful because it separates a lengthy differentiation from its load-bearing locality inputs. It does not assume (189) itself. Credit Bałaban for the linearizing transformation (47)–(73) and the remainder (80).

Use \(X\) for the weighted potential/first-difference norm, \(Y\) for the force norm \(\sup_y\xi_y^3|f|\), and \(B\) for dimensionless row sup norm. A subscript \(w\) multiplies these local norms by \(w_y>0\), with \(w_y/w_z\le e^{\mu d(y,z)}\). All adjoints below use §6's measures. The following are **inputs**, not consequences of an unweighted sup estimate:

1. The actual linear lift \(H:B\to X\), its adjoint \(H^*:Y\to B\), the operators \(T=L_\pi H:B\to Y\), \(T^*:X\to B\), and \(U=H^*L_\pi H:B\to B\) are bounded by one fixed \(b\ge2\), in the unweighted and all these weighted norms. For \(T\), use its row representation from (6.1), not an unbounded second difference of an arbitrary input.
2. The nonlinear row remainder \(C\) is holomorphic on a fixed local chart, \(C(0)=C'(0)=0\). Its first derivative and its adjoint have norms at most \(b\|a\|_X\). Its second derivative obeys both
\[
 \|C''(a)[h,k]\|_{B,w}\le b\|h\|_{X,w}\|k\|_X,
\quad
 \|C''(a)[h]^*v\|_{Y,w}\le b\|h\|_{X,w}\|v\|_B.       \tag{9.1}
\]
The same two bounds for \(C''(a)-C''(0)\) have the extra factor \(\|a\|_X\), after increasing \(b\) by a chart-radius constant. They include boundary rows and the local source-density factors. For local rows these statements follow from a density bound on \(C'\), its column sum, and Cauchy on a larger local chart; output-only bounds on \(C\) do not suffice for the adjoint statement.
3. The Wilson remainder \(V_0\), after subtracting its constant, linear and quadratic parts, satisfies
\(\|V_0'(a)\|_Y\le b\|a\|_X^2\) and
\(\|V_0''(a)h\|_{Y,w}\le b\|a\|_X\|h\|_{X,w}\).
This is a local first-order estimate. In CMP 102 (39), (91)–(96), the potentially dangerous term is \(D^*[a,a]\); the covariant product rule expresses it as \([Da,a]+[a,Da]\), with shifted transports, so its variation uses \(h,Dh\), not two differences of \(h\). The other terms contain the compensating mesh factor or are zeroth order. Near an action boundary the scale is bare, so the finite missing-neighbor terms have the same scaled bound. All these local products have bounded incidence and obey the same weighted bound, enlarging \(b\).

For the outline, §§8.5 and 8.7 prove input 2 on the no-inward real-reference and local complex regular-pair domains; §8.6 supplies the reduced datum used with it. For Bałaban's average, the corresponding printed sources are CMP 98 Proposition 4, Proposition 5 and their analytic extensions. The direct contour-mean argument above replaces the particular single-comb formula (124); it does not claim that the two curved rows are equal. Input 1, including its actual operator domains, is still unproved here. Input 3 is being used as the stated local expansion estimate, rather than as a substitute for the missing operator bounds.

Choose \(r\le\min\{1,(32b^2)^{-1}\}\), with the ball of radius \(4r\) inside the primitive chart. Solve
\[
 D(a)=C(a-HD(a)),\qquad p(a)=a-HD(a).                  \tag{9.2}
\]
Here \(D\) is Bałaban's nonlinear **row map**, not the covariant derivative. On \(\|a\|_X\le r\) and \(\|D\|_B\le2br^2\), one has \(\|p(a)\|_X\le r+2b^2r^2<2r\); integration of \(C'\) bounds \(\|C(p)\|\le(b/2)(2r)^2=2br^2\). The derivative with respect to \(D\) has norm at most \(2b^2r<1/2\). Thus successive substitution converges geometrically in this closed ball and gives the unique fixed point there. Each iterate is holomorphic and their geometric difference bounds are uniform on smaller complex balls, so the limit is holomorphic.

Put \(F=C'(p)\), \(N=(I+FH)^{-1}\), \(P=I-HD'(a)\). Differentiating (9.2) gives the exact identities
\[
 D'=NF,\quad P=I-HNF,\quad
 D''[h,k]=N C''(p)[Ph,Pk].                             \tag{9.3}
\]
The series for \(N\) has norm at most two in every permitted weight. Consequently \(\|D'\|,\|D'^*\|\le4br\), \(\|P\|,\|P^*\|\le2\), and the two versions of the second-derivative bound in (9.1) hold for \(D''\) with constant \(8b\). These adjoint bounds follow by transposing (9.3) in the second variation: its three factors are \(P^*\), \(C''(p)[Ph]^*\), \(N^*\), bounded respectively by \(2,b\|Ph\|,2\).

Let \(C_2(a)=\tfrac12C''(0)[a,a]\) and \(D_3=D-C_2\). In (9.3) subtract \(C''(0)\), first in \(N\), then in \(C''(p)\), and then in each of the two copies of \(P\). The differences satisfy
\(\|N-I\|\le4b^2r\), \(\|C''(p)-C''(0)\|\le2br\), \(\|P-I\|\le4b^2r\).
Their four products, and the corresponding adjoints, give
\(\|D_3''[h]^*v\|_{Y,w}\le100b^4r\|h\|_{X,w}\|v\|_B\).
This also proves that subtracting the quadratic term removes the zeroth-order Hessian contribution; no assertion of smallness is being made merely from analyticity.

With \(j=H^*J\), \(\|J\|_Y\le1\), rewrite CMP 102 (80) as
\[
 V(a)=-\langle D_3(a),j\rangle-\langle a,TD(a)\rangle
       +\tfrac12\langle D(a),UD(a)\rangle+V_0(p(a)).
\]
Here \(U\) is symmetric. A second differentiation in direction \(h\) gives, with the star denoting the unfilled variation,
\[
\begin{aligned}
 V''(a)h={}&-D_3''[h]^*j\\
 &-TD'h-D''[h]^*T^*a-D'^*T^*h\\
 &+D''[h]^*UD+D'^*UD'h\\
 &+P^*V_0''(p)Ph-D''[h]^*H^*V_0'(p).                 \tag{9.4}
\end{aligned}
\]
This lists every term of the omitted second differentiation. The first line is at most \(100b^5r\|h\|_{X,w}\); the next line at most \(16b^2r\|h\|_{X,w}\); the third at most \(32b^3r^2\|h\|_{X,w}\); the last at most \((8br+32b^3r^2)\|h\|_{X,w}\). Since \(b\ge2,r\le1\),
\[
 \|V''(a)h\|_{Y,w}\le256b^5r\|h\|_{X,w}.             \tag{9.5}
\]
For \(h\) localized at \(z\), take \(w_y=e^{\mu d(y,z)}\). Equation (9.5) is the localized exponential second-variation bound needed in place of (189), **conditional on inputs 1–3**. It costs no number of layers or fine sites.

For example, at a critical base, CMP 102 (175) becomes
\(a_1=-\mathcal C V'(a_1+H_1B)\). In this display \(B\) denotes the **reduced** row datum; for the original datum insert \(\mathsf b(B)\) from §8.6 and differentiate that map as well. If \(\|\mathcal C\|_{Y,w\to X,w},\|H_1\|_{B,w\to X,w}\le b\), take \(256b^6r\le1/4\), and \(b\sup|B|\le r/4\). On \(\|a_1\|_X\le r/4\) the map is a contraction and maps the ball into itself: integrate (9.5) from zero to bound \(V'\), using \(V'(0)=0\). Its differentiated equation is
\[
 (I+\mathcal C V''(a_1+H_1B))\,\partial_Ba_1
       =-\mathcal C V''(a_1+H_1B)H_1.
\]
The same Neumann bound in every weight proves first-response exponential decay in \(X\) throughout that datum polydisc. The physical potential is \(p(a_1+H_1B)\), whose derivative has the additional bounded factor \(P\) from (9.3). This closes the **conditional differentiation step**, not existence of the actual weighted operator inputs.

The current and second-order members still require the actual stationary equation with multiplier. If it is available, differentiation gives
\(F''(A)h=K_A^*\dot\omega+(K'_A[h])^*\omega\); the derivative-density bounds estimate this in \(Y\). To recover \(D^*Dh\), subtract the curvature and first-order nonlinear remainders. To recover the covariant component Laplacian in the Landau slice, use
\(DD^*h=D(1-R)D^*h\), and estimate that **regular** kernel. This explains how response-specific second-order bounds can hold despite the exception in 3.12. It does not allow use of a nonexistent Laplacian bound for the full covariance, and it does not itself supply the multiplier or the nonlinear top factor on the outline's domain.

## 10. Complex decoupling and derivatives that join sets

CMP 99b 3.4 proves analyticity in a field perturbation satisfying (3.37). It does not introduce independent decoupling parameters. The outline correctly observes at (1c), mechanism (j), that identities such as \(QH=I\) cannot be imposed on the decoupled sums: setting all parameters around a row to zero deletes its contributing terms. One must perform the algebraic cancellations in (9.4) **before** inserting the parameters, and then use that expression as the definition off the undecoupled physical slice.

The analytic implication can be proved exactly. Suppose actual local terms \(O_\omega\) have already been constructed, with their correct force/output norms, and for some \(\mu>0\)
\[
 \sum_{|\omega|=n}\|O_\omega\|_\mu\le bq^n,
 \qquad 0<q<1.                                       \tag{10.1}
\]
Suppose a term is multiplied by a monomial \(s^\omega\) of degree at most \(\nu(n+1)\), supported on its assigned hull, and choose \(R>r>1\) with \(qR^\nu<1\). On \(|s_i|<R\),
\[
 \sum_\omega\|s^\omega O_\omega\|_\mu
 \le \frac{bR^\nu}{1-qR^\nu}.                         \tag{10.2}
\]
The bound proves local uniform convergence and holomorphy. A multi-index \(\alpha\) supported on finitely many parameters has, on \(|s_i|\le r\),
\[
 \|\partial_s^\alpha O(s)\|_\mu
 \le\alpha!(R-r)^{-|\alpha|}
              \frac{bR^\nu}{1-qR^\nu}.                \tag{10.3}
\]
Apply the one-variable Cauchy integral in each differentiated coordinate, with circles of radius approaching \(R-r\); the product of the contour lengths cancels the corresponding denominators. No factor depending on the total number of parameters appears.

For joining decay, use a stronger version of (10.1) with a term bound containing \(e^{-2\mu\ell(\omega;y,y')}\), where \(\ell\) is its tree length. A mixed derivative vanishes unless its hull meets every differentiated parameter set. If each such meeting is within fixed metric distance \(a\) of the tree, the minimal connecting-tree length \(\mathcal T\) of the endpoints and these sets satisfies
\(\mathcal T\le\ell+a(|\operatorname{supp}\alpha|+2)\): attach one segment of length at most \(a\) for each set and endpoint. Retain half the exponential for summing (10.1) and use the other half to obtain the factor
\[
 e^{\mu a(|\operatorname{supp}\alpha|+2)}e^{-\mu\mathcal T}
\]
in (10.3). Thus joining derivatives retain decay **when the actual expansion has this locality**. Analyticity of a single real inverse, or an entrywise exponential estimate on its sum, does not supply (10.1) or hull dependence. The outline uses a more efficient length-versus-parameter count rather than the sufficient degree bound here; either requires a proof for its assigned terms.

The remaining actual-domain work is to build those terms with the outline's rows, independent current, boundary conventions and exact common enlarged discs. CMP 99b's complex neighborhood cannot simply be renamed as those discs. In particular the complete derivative/Hölder package must be bounded on the larger domain before Cauchy can be applied on the smaller one. Section 9 gives a conditional nonlinear construction once those uniform operator data and average majorants are present; it does not construct them.

## 11. Seams, inner action and finite-box comparison

The seam lift (7.5)–(7.9) treats the flat straightened rows, including their one-sided normalization. Sections 8.5–8.6 separately prove the no-inward nonlinear reduced-datum identity, its local holomorphy and the top-factor bounds. These are constraint statements. They do not identify the two boundary actions or the stationary equations associated with them.

There is a separate boundary mismatch even at identity. Let \(\iota\) extend an inner bond field by zero outside \(\Omega_0\). Then
\[
 \langle A,d_{\rm full}^*d_{\rm full}|_{\Omega_0}A\rangle
 -\langle A,d_{\rm in}^*d_{\rm in}A\rangle
 =\sum_{p\not\subset\Omega_0}|d(\iota A)(p)|^2.        \tag{11.1}
\]
Choose a rectangular \(\Omega_0\), a tangential bond on a boundary face, set its field value to a nonzero fixed color and all other values to zero. The plaquette just outside that face reads precisely this bond, so the right side is strictly positive. This explicitly distinguishes Bałaban's compressed whole-lattice Hessian from the outline's inner-plaquette Hessian. It refutes their literal equality, not a controlled boundary perturbation.

There is a useful exact cancellation in the bare collar. Since \(Q'\lambda=\lambda\) at every level-zero top, \(\lambda\in\ker Q'\) vanishes outside \(\Omega_1\). The local scalar Laplacian therefore sends it to a function supported in the one-mesh-step neighborhood \(N_\eta(\Omega_1)\). By (3.2),
\[
 R=\mathbf1_{N_\eta(\Omega_1)}R\mathbf1_{N_\eta(\Omega_1)},
 \qquad
 DRD^*=\mathbf1_{N_{3\eta}(\Omega_1)}DRD^*
                              \mathbf1_{N_{3\eta}(\Omega_1)}. \tag{11.2a}
\]
The second indicator in the first equality follows by transposition. Three mesh steps in the second equality safely accommodate both endpoint conventions. This argument also applies with the holomorphic transpose whenever the inverses defining \(R\) exist. Thus the nonlocal gauge term does **not** reach the outer boundary through a tail: it has exact zero rows there. Changing the scalar boundary convention changes neither \(\Delta\ker Q'\) nor \(R\), provided the changed coefficients are outside this collar. This corrects a possible overreading of the warning after (7.4): nonzero bare-layer rows can occur near \(\Omega_1\), not arbitrarily far into its bare exterior.

Likewise \(Q'SR=0\) implies that \(SRf\) vanishes on every bare top. Hence the gauge change \(E-I=-DSRD^*\) has zero output outside the one-step neighborhood of \(\Omega_1\). An artificial finite-box boundary cutting a higher layer is a different situation; (11.2a) does not assert locality of the old gauge rows at that boundary.

At identity let \(A_{\rm c}\) use the compressed curl and \(A_{\rm i}\) use only inner plaquettes, with the same \(Q,R\) and row coefficient \(a_0=1\). Their difference is the positive boundary form \(B_\partial\) in (11.1). All its bonds lie in the bare layer and are determining rows: separation keeps any inward seam a distance greater than three mesh steps away. The full curl norm used in (7.4) gives
\[
 0\le B_\partial\le16\eta^{-2}\mathbf1_\partial
                  \le16 Q^*aQ.
\]
Both the inner curl and \(DRD^*\) are nonnegative. Consequently
\[
 A_{\rm i}\le A_{\rm c}\le17A_{\rm i}.              \tag{11.2b}
\]
In particular, any proved scale-weighted coercivity of \(A_{\rm c}\) transfers to \(A_{\rm i}\) with loss at most 17. If \(A_{\rm c}>0\), both inverses exist, and their exact difference is
\(A_{\rm i}^{-1}-A_{\rm c}^{-1}=A_{\rm i}^{-1}B_\partial A_{\rm c}^{-1}\).
The latter identity does not by itself bound the first inverse's kernel; coercivity and an exponential kernel estimate are different assertions. The proof of (11.2b) uses positivity of the **flat** curl, so it is not an unproved form comparison for an arbitrary curved Wilson Hessian.

For the nonlocal gauge term \(\mathcal P=D(1-R)D^*\), the parametrix comparison needed in CMP 99b (3.105) is exactly
\[
 \mathcal P h-h\mathcal P_\square
 =\zeta[\mathcal P_\square,h]
   +\zeta(\mathcal P-\mathcal P_\square)h
   +(1-\zeta)\mathcal P h,\quad \zeta h=h.             \tag{11.2}
\]
Expansion verifies the identity. The three terms need, respectively, a cutoff commutator, comparison of scalar/Gram inverses on two domains, and a tail estimate. Their bounds cannot be inferred from an estimate on \(\mathcal P\) alone. Near the outer boundary (11.2a) reduces \(\mathcal P\) to the local \(DD^*\), so there the tail issue disappears. In covers that meet the nontrivial layers, comparison of the actual scalar/Gram inverses is still needed. Bałaban obtains it by cancellation of common localized walks; it remains to construct and bound those walks with the new rows and the arbitrary first member. This is the unresolved kernel step after the bare model and the flat form comparison.

The final finite-box implication is elementary **once those actual boundary equations are supplied**. Suppose the boundary forcing \(f\), decomposed into coarse pillars, obeys
\(\|f_z\|_{\rm force}\le A(R+1)^s\), and the actual inverse from \(z\) to \(y\) is at most \(Ce^{-\mu d(y,z)}\) in the required weighted output norms. If its support is at distance at least \(D\) from \(y\), (5.5) gives
\[
 \|Gf\|_y\le C'A(R+1)^s e^{-\mu D/2}.                \tag{11.3}
\]
Factor out \(e^{-\mu D/2}\) and sum the remaining half-rate. If the forcing instead has a tail \(e^{-\nu d(z,\partial\Lambda)}\), use
\(d(y,\partial\Lambda)\le d(y,z)+d(z,\partial\Lambda)\), reserve half of \(\min\{\mu,\nu\}\) for this distance, and sum again. These are cell sums, with force measures as in §6. For an affine field, local rows and first two cutoff differences produce a polynomial in \(R+1\); exponentially local gauge rows require (11.2). This proves the form of PW12 from its explicit operator hypotheses, not those hypotheses themselves.

For outline Theorem 6(c), the corresponding conditional last step is to interpolate the joined collar data in a **common admitted critical branch**. If that branch exists, the local datum variation is bounded by \(C_\mu\varepsilon_1\), and the response bound holds throughout it, integration and (5.5) give
\[
 \xi_y|f|+\xi_y^2|\nabla f|+\xi_y^3|D^*Df|
 \le C_\mu'\varepsilon_1e^{-\mu' d(y,W^c)}.
\]
The mismatch may be \(O(\mu)\) inside the collar, giving the stated \(e^{O(\mu)\mu'}\) prefactor. The no-inward nonlinear seam row identity is now supplied by §8.6. One must still prove restriction of the actual stationary equations and uniform chart/current room along the interpolation. Stationarity on the old constraint manifold alone does not prove stationarity after changing its equations. The remaining hypotheses identified in the gate's §7 cannot be removed by the constraint identity alone.

## 12. Recovering the Hölder member from the actual second-order response

This is a local analytic implication, useful because the Laplacian bound excluded from CMP 99b 3.12 cannot be asserted for its full inverse. It proves that **if the response itself** has the potential, first-difference and component-Laplacian bounds in Theorem 4, its Hölder member follows on the specified local cubes. It does not obtain that Laplacian bound from a first-difference bound.

First work on \(\mathbb Z^4\). The scalar Green function is
\[
 G(x)=(2\pi)^{-4}\int_{[-\pi,\pi]^4}
 \frac{e^{ip\cdot x}}{\lambda(p)}\,dp,
 \qquad \lambda(p)=4\sum_{\nu=1}^4\sin^2(p_\nu/2).
\]
The integral converges at zero since its absolute integrand is \(O(|p|^{-2})\) in dimension four. For \(n=0,1,2\), any product of \(n\) forward or backward differences has
\[
 |\nabla^nG(x)|\le C_n(1+|x|_\infty)^{-2-n}.        \tag{12.1}
\]
Here is the Fourier estimate, including its short-distance convention. For \(|x|_\infty\le4\) bound the integrable symbol directly. Otherwise put \(R=|x|_\infty\), choose a smooth cutoff at frequencies of order \(R^{-1}\), and split the integral. Near zero the differentiated symbol has size \(C|p|^{n-2}\), whose integral on this ball is \(CR^{-n-2}\). Away from it integrate by parts \(N=n+3\) times in a coordinate with \(|x_\nu|=R\). Derivatives of the symbol have size \(C|p|^{n-2-N}\). Their radial integral from \(R^{-1}\) to one is at most \(CR\); multiplication by \(R^{-N}\) again gives \(CR^{-n-2}\). Each derivative of the cutoff has the same bound by scaling. The symbol and cutoff are periodic, so the boundary terms cancel. Away from a fixed neighborhood of zero all their derivatives are bounded. These facts prove (12.1), including every shell, without a numerical evaluation or an assumption about the finite-torus frequency mesh.

Let a scalar or componentwise vector function \(h\) be defined on an embedded cube of side \(8s\), with \(s\ge16\), and suppose there
\[
 |h|\le M/s,\qquad |\nabla h|\le M/s^2,
 \qquad |\Delta h|\le M/s^3.
\]
Choose a cutoff equal to one on the middle cube of side \(4s\), supported in the cube of side \(6s\), with first and second differences bounded by \(C/s\), \(C/s^2\). For example a fixed smooth scalar cutoff of \(x/s\), sampled on the lattice, has these bounds by integrating its ordinary derivatives along one or two unit segments. The discrete product rule gives \(f=\Delta(\chi h)\) supported in that cube and \(|f|\le CM/s^3\). Extension by zero is harmless because the cutoff vanishes on a collar. The exact identity \(G\Delta(\chi h)=\chi h\) follows either from the Fourier formula or from \(\Delta G=\delta_0\) and finite summation.

For two points in the middle cube at distance \(r\), \(1\le r\le s\), split the sum for \(\nabla G*f\) into distances at most \(8r\) from one of the points and the complement. The near part of the difference is at most
\(CMs^{-3}\sum_{t\le Cr}(1+t)^3(1+t)^{-3}\le CMr/s^3\).
On the complement telescope along a coordinate path between the two points and apply the second bound (12.1). The result is at most
\(CMrs^{-3}\sum_{Cr\le t\le Cs}(1+t)^{-1}\).
Consequently
\[
 |\nabla h(x)-\nabla h(x')|
   \le CM s^{-2}\frac rs\bigl(1+\log(s/r)\bigr)
   \le C_\alpha M s^{-2}(r/s)^\alpha,
 \quad 0<\alpha<1.                                  \tag{12.2}
\]
For the last inequality put \(t=r/s\). The function
\(t^{1-\alpha}(1+\log(1/t))\) is bounded on \((0,1]\), as is seen by writing \(t=e^{-u}\) and maximizing \(e^{-(1-\alpha)u}(1+u)\). Small cubes have only a bounded number of mesh steps; their bound follows from twice the gradient supremum. Restoring spacing \(\eta\) gives the same statement for \(\eta\le r\le s\), with physical differences and the stated powers of \(s\).

The covariant version needs precisely the local first-order gauge bounds already required of the regular class. On a cube where \(U=e^{i\eta A}\), \(|A|\le a/s\), \(|\nabla A|\le a/s^2\), expansion of one shift gives
\[
 |(\Delta_U-\Delta)h|
 \le C\{ |A|\,|\nabla h|+(|\nabla A|+|A|^2)|h|\}.
\]
This estimate follows by pairing the two opposite shifts: the coefficient of a first difference is \(O(A)\), and the remaining coefficient is \(O(\nabla A+A^2)\). The exponential remainder is bounded by its absolutely convergent series for \(\eta|A|\) small. Thus a bound \(|\Delta_Uh|\le M/s^3\) supplies the ordinary bound used above. The difference between ordinary and covariant gradients is \(O(Ah)\); its difference between the two points is bounded using \(|\nabla A|\), \(|\nabla h|\) and the same product rule. Transporting along a path of length \(O(r)\) adds at most \(Ca(r/s)M/s^2\), because each link is within \(C\eta a/s\) of identity. For a small complex perturbation the product norms acquire only \(e^{Ca}\). Hence (12.2) holds with the covariant transports and throughout such a fixed complex chart.

Near a multiscale seam take a cube of size a fixed small multiple of \(\xi_y/L\). Separation ensures that it meets only the two neighboring scales and is inside \(\Omega_0\) unless the scale is bare. For larger separations up to \(\xi_y\), the first-difference supremum itself gives (12.2), with a factor depending on \(L,\alpha\). In the bare layer any nonzero separation is at least \(\eta\), so the same conclusion on existing differences is immediate from their supremum. A weight \(e^{\mu d(y,y_c)}\) changes by a bounded factor on these cubes. The conditional response bound therefore has exactly the factor \(\xi_y^{-2-\alpha}\) and retains a fixed fraction of its exponential rate. This settles the Hölder *implication*; the response equation and its second-order bound remain load-bearing premises.

## 13. Published flat inputs: replaced parts and cited-pending remainder

CMP 95 and CMP 96 have not been obtained. The unreconstructed portions below are **cited-pending**, credited to Bałaban. They are not inferred from the number or titles of his theorems. The source anchors in CMP 99b identify exactly where its proof imports them; the displays below state the needed inputs in consistent modern notation rather than purporting to transcribe unread formulas. Replacements proved here are identified explicitly; the name of a package does not mean that all of it remains pending or that all of it is proved.

Write \(m_y=\xi_y\), \(e_{yy'}=e^{-\delta d(y,y')}\). In this list all operators are flat, with matched boundary spaces, and forces have their fine-cell pairing. A local \(L^2\) norm includes \(\eta^4\). The scalar average is the pillar mean; the vector average is the straight-path row per unit length. Constants must be uniform over admitted separated sequences, depths and compatible tori. Hölder differences have exponent strictly below one and range at most the local scale.

**F1 — flat scalar inverse and local regularity.** For
\(S_0=(d^*d+Q_0'^*aQ'_0)^{-1}\), positivity and existence, and, for \(f\) supported over \(y'\),
\[
 \begin{split}
 |S_0f|_y&\le C m_y^2 e_{yy'}|f|,\\
 |\nabla S_0f|_y+|S_0\nabla^*f|_y&\le C m_y e_{yy'}|f|,\\
 |\Delta S_0f|_y&\le C e_{yy'}|f|,\\
 [\nabla S_0f]_{\alpha,y}
       +[S_0\nabla^*f]_{\alpha,y}
    &\le C_\alpha m_y^{1-\alpha}e_{yy'}|f|.
 \end{split}                                        \tag{13.1}
\]
The mixed derivative requires a Hölder source:
\[
 |\nabla S_0\nabla^*f|_y
  +m_y^\beta[\nabla S_0\nabla^*f]_{\beta,y}
 \le C_{\epsilon,\beta}e_{yy'}
             (|f|+m_{y'}^\epsilon[f]_\epsilon),        \tag{13.2}
\]
with the admissible exponents of the source estimate, in particular one may fix \(0<\beta<\epsilon<1\). Also needed are localized \(L^2\) bounds
\(\|\mathbf1_y\nabla^r S_0(\nabla^*)^t\mathbf1_{y'}\|_{2\to2}
\le C m_y^{2-r-t}e_{yy'}\), for \(r,t\in\{0,1\}\), and the corresponding \(\Delta S_0\) bound. Fixed powers may be moved between endpoint scales with a loss of rate by §5. Sources: CMP 99b (3.42)–(3.47), pp. 397–398; the flat import is identified on pp. 399, 407–410 as CMP 96 Proposition 2.2 and CMP 95 Proposition 1.2. The local mean-value estimate retained in §4 and the implication in §12 do not prove (13.1) for this multiscale inverse. In particular an arbitrary bounded source cannot be substituted for the Hölder source in (13.2).

**Replacement obtained:** (7.10) proves scalar positivity, and (7.15) proves the displayed localized \(L^2\) bounds with at most one derivative on each side, including their complex versions. Equation (7.20) adds the value, output-gradient, output-Laplacian and output-gradient Hölder members. These results also apply to the actual new scalar rows on the specified no-inward regular-pair class. The pointwise \(S_0\nabla^*\) and mixed-source members (13.2) have not been proved here; a bounded differentiated source is not covered by (7.20).

**F2 — scalar top Gram inverse and the regular projection kernel.** For
\(N_0=(Q'_0S_0^2Q_0'^*)^{-1}\), the required counting-kernel bound is
\[
 |N_0(y,y')|_{\rm count}\le C m_y^{-4}e_{yy'}.        \tag{13.3}
\]
Equivalently, after a fixed redistribution of scale powers and loss of rate, the density in the top measure is bounded by
\(C m_y^{-4}m_{y'}^{-4}e_{yy'}\). For \(P_0=I-R_0\), the fine-kernel densities needed by the vector construction are
\[
 |\nabla_x^r P_0(x,x')(\nabla_{x'}^*)^t|
   \le C m_y^{-2-r}m_{y'}^{-2-t}e_{yy'},
 \quad r,t\in\{0,1\},                               \tag{13.4}
\]
including the corresponding Hölder differences. Here “regular” is measured in the local scale. At bare sites the bound allows the local delta kernel and its differences; for example \(P_0=I\) if every pillar is bare. It does not permit an unsuppressed fine delta kernel in a large coarse pillar. Sources: CMP 99b (3.48)–(3.49), pp. 398–399, citing CMP 96 Proposition 2.3; its local comparison at pp. 410–413 also invokes that paper's (2.83)–(2.85). Formula (13.4)'s powers are reconstructed from the order-zero projection, one inverse length per derivative and the four-dimensional density. **Replacement obtained:** (7.12) and (7.17) prove the scalar Gram gap and (13.3); (7.21) proves (13.4), including the stated Hölder members. These proofs apply also to the new rows and small complex regular pairs on the no-inward class. The locality/comparison of these kernels under changes of sequence remains pending; no walk assignment is supplied by their global kernel bounds.

**F3 — flat vector inverse, row Gram and lift.** For
\[
 G_{00}=(d^*d+dR_0d^*+Q_0^*aQ_0)^{-1},
\]
with the compressed whole-lattice curl, one needs positivity, all the versions of (13.1)–(13.2) and the localized \(L^2\) bounds, and
\[
 Q_0G_{00}Q_0^*\ge\gamma m^2,\qquad
 |(Q_0G_{00}Q_0^*)^{-1}(c,c')|_{\rm count}
       \le C m_c^{-2}e_{y_cy_{c'}}.                  \tag{13.5}
\]
For \(H_0=G_{00}Q_0^*(Q_0G_{00}Q_0^*)^{-1}\), the physical-row counting bounds are \(|H_0(b,c)|\le Ce_{yy_c}\), \(|\nabla H_0(b,c)|\le C m_y^{-1}e_{yy_c}\), with the specified Hölder and force-transpose versions. The dimensionless datum inserts the further source factor \(m_c^{-1}\). Sources: CMP 99b pp. 399, 407–408, 417–422, and its references to CMP 95 (1.103), (1.107) and CMP 96 (2.35). Section 7 supplies a smooth right inverse of the actual flat rows and hence proves the lower-bound part of (13.5) **if** the positive \(G_{00}\) is supplied. Section 11 transfers flat coercivity to the inner action. Neither proves the full inverse package, even at identity on every sequence.

**F4 — the unit-lattice fluctuation gap and conditional covariance.** This is a different covariance from (6.3). In the top-scale units let
\(A_k=(Q_0G_{00}Q_0^*)^{-1}-a\). On fields supported in the specified union of top blocks, with vanishing one-step straight average and vanishing strict-axial tree variables, one needs
\[
 \langle B,A_kB\rangle\ge cL^{-5}\|B\|_2^2.          \tag{13.6}
\]
Equivalently, after the local pivot-coordinate embedding \(I_{\rm piv}\), one needs \(I_{\rm piv}^*A_k I_{\rm piv}\ge\gamma_0I\), with the stated norm comparison and uniformity for conditioning subsets. This is precisely the flat input cited as CMP 96 Lemma 2.4 at CMP 99b p. 428, before Theorem 3.15. The compressed inverses must then have uniform exponential kernels in these coordinates. A positive inverse on the fine Landau slice does not prove (13.6). The outline's plain-average/soft-contour gauge requires its own coordinate comparison; neither centring nor (8.11) identifies that gauge with the strict tree gauge. The outline's separately proved flat reference chapters might replace this input, but their full arguments and their conditioning transfer have not been imported here.

**F5 — locality of the local flat models.** Where the walk construction changes a sequence or a torus, it needs the following form of the flat bounds: operators on a common inner region have identical locally defined terms until a walk reaches the changed region, and the remaining terms obey the same derivative norms with an extra exponential in that distance. The local inverses and cutoffs must have support/read sets contained in their assigned enlargements. CMP 99b pp. 408–410 explicitly reuses CMP 95 Proposition 1.2, CMP 96 Proposition 2.2, the latter paper's local constructions, and its estimates (2.44), (2.83)–(2.85), (2.135). This input is not an assertion that any two exponentially decaying matrices are close. Section 7 proves how a small actual remainder is summed, and §10 proves what follows from an actual local walk expansion. Neither constructs the local flat models of those unavailable sections.

The summation portion of CMP 96 Lemma 2.1 is **replaced here by §5**, on the outline's larger path class. The identities behind CMP 95/96's scalar projection and constrained inverse are **replaced by §§3 and 6**. The scalar positivity, localized energy bounds, top Gram kernel, output regularity and regular projection kernel are **replaced by (7.10)–(7.21) and their continuation arguments**. These replacements must not be counted as verification of the differentiated-source, vector, fluctuation-coordinate or locality portions still pending in F1–F5.

## 14. Coverage and the first remaining obligations

The following table answers the gate's Section 8 requirement by requirement. “Proved” in a cell refers only to the written substatement and is a research claim by this note, not independent review or retained status.

| Gate requirement | Written result here | First remaining obligation |
|---|---|---|
| Actual inverse kernels and conditional covariances, force/cell weights and boundary rows | Exact projection/lift/covariance algebra; fine/row measure conversion; scalar positivity, weighted \(L^2\), output regularity, top Gram and regular projection kernels, including complex continuation; smooth flat row lift; bare boundary inverse and flat form comparison | The remaining differentiated-source and locality parts of F1–F5, and the actual vector parametrix. Conditional unit-lattice covariances additionally need the correct coordinate/conditioning gap. |
| Weighted potential, gradient, current, second-order and Hölder response | Local averaging majorants and their transposes; complete conditional second variation (9.4); weighted contraction implication; local Hölder implication (12.2) | Actual weighted propagators and multiplier estimates. Recover the response's current and component Laplacian from its actual equations; do not insert the excluded \(\Delta G_{(1)}\) estimate. |
| Specified Landau pair and top factor | Exact linear slice map and Ward identity; explicit distinction from the \(\Pi\)-slice; correct composite factors, their bounds and the outward top normalization | Construct the nonlinear solution in that slice on the full datum domain, identify it with \(\Phi\), and establish pair uniqueness. Linear gauge algebra and a top-factor bound alone do not do this. |
| Full complex datum domains, enlarged decoupling discs, Cauchy and joining decay | Local complex averaging extension; conditional holomorphic fixed point; Cauchy and joining estimates for an explicitly hypothesized local expansion | Uniform estimates for the six actual propagators at independent-current pairs, with the ceiling independent of \(M_1\), and the actual local walk assignment on the prescribed enlarged discs. |
| Restriction, seams and finite boxes | Flat seam lift; exact no-inward reduced datum; original outer-boundary cancellation; finite-box forcing-to-response implication | Restriction of the actual stationary equations, arbitrary conditioning/boundary compatibility, and a common admitted branch for the collar interpolation of Theorem 6(c). Kept inward nodes are not covered by the no-inward construction. |

The first unresolved transfer in the present route is the **localized comparison of the scalar/projection kernels on changing sequences**, needed in (11.2) and in the actual vector parametrix. The global scalar bounds now have written proofs, but they are not a local walk assignment. The source-derivative members used in its commutators also remain to be supplied in their precise norms. Even granting the cited-pending flat vector package, one must assemble and bound the actual remainder with the new rows and boundary action. Writing \(A G^{\rm loc}=I-T\) and assuming \(\|T\|<1\), as in §7, does not prove it.

There is a further genuinely different issue at the independent current. The outline's correction \(\Delta'_\pi[\mathbf J]\) contains \(\lambda_A=G'RD^*A\), shifted \(\lambda_A\), and \(D\lambda_A\). Its effect must be estimated **after composition with the inverse**, retaining the derivatives in the bilinear formula at outline lines 10172–10190. It is not justified to posit a bounded map \(\Delta'_\pi:X\to Y\) from only a supremum bound on \(\mathbf J\): moving derivatives across that pairing produces derivatives of a merely bounded current and mixed scalar inverses. The resolvent estimates must handle those compositions in their actual norms. CMP 99b's physical-current proof with (3.36) is not already a proof on the first-order independent-current class. No counterexample to that desired composed estimate has been obtained.

The explicit configurations in §§3, 8.2 and 11 disprove three shortcuts, respectively \(\Pi=R\), equality of comb and contour-mean pillar rows, and equality of compressed and inner actions. **None is a counterexample to A3.** The written subresults do not exhaust A3 and do not imply existence of Yang–Mills theory.

### Source identities and recovery

The source pin is `713766c1b62d67c9c8afaa5828efb56d5d49d7ea`. The exact external outline is `31a47c543775`, fetched once, SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. Its key excerpts are A3 at 3864–3896; the datum/Landau/response statements at 9693–9746; Theorem 6(c) at 9782–9790; the operator definitions and current correction at 10105–10199; the principal bounds and walk data at 10253–10469; and PW1–PW3/PW12 at 13425–13513/13670–13712. These are line anchors in that fetched text, not citations to a later revision.

The gate's SHA-256 is `886287f9020611fc7ed7a9c67422604e2e08c60f6a615edfabafa4b241b94700`; `a3-response.md` is `db895742da4170a1be32b50ba63c69938e1f2b04197d491888a624b641889a05`. The external OCR identities are:

| External file, left outside the repository | SHA-256 |
|---|---|
| `cmp98.txt` | `0ff2fffafed9aad0af74426471a804de2916c6c5c16bcf2122bc822d69f7b69c` |
| `cmp99a.txt` | `90e285e77fae7839a554fc3e925ee7fd00612094c930b9ec2cbc138fa377e6cc` |
| `cmp99b.txt` | `0aed21d3bdcc4e114bec312577d1082a763f8489b58a158b0f60c3e8f045be4a` |
| `cmp102.txt` | `78b973edee2f485e6c3c1eb49e9077bc244f5e13d720d432f25d949cd054203f` |

The hashes are recovery bookkeeping, not mathematical verification. The formulas reconstructed from the OCR are identified where used: §2's scale powers, §3's scalar projection, §6's constrained covariance and measure convention, §7's resolvent sign, §9's complete second variation, and §13's imported norm package. No ambiguous OCR formula has been treated as an exact checked transcription.

Recovery decision: retain the written scalar/averaging arguments for checking on their stated domains, and resume at the localized comparison (11.2), the differentiated-source norms and the vector parametrix. After those, the independent-current correction, fluctuation-coordinate covariances, nonlinear Landau identification and decoupled walk domains still require their own proofs. The three explicit shortcut counterexamples must be preserved; none licenses REFUTED for A3. Only this research note was edited in the repository. There was no computer-assisted mathematical discharge, subagent, audit, commit, push, PR or post, and no status was granted.
