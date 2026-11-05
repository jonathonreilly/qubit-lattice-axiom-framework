# PIV: uniform holomorphic pivot graph and contour means

Provenance: Codex, 2026-11-05, checkout bab62f4057038b20ac8accd6d073fd90e6d49da5. Research text, not an audit; grants no status. Written arguments only. Source constructions are credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at source commit 31a47c543775.

This supplies the nonlinear import PIV of frozen [hma.md](hma.md), on its admitted working domains. The primitive averaging and domain imports remain imports. This does not prove that every history supplies those domains. The proof uses no run, enumeration, or numerical enclosure.

## 1. Source reading and scope

The outline already proves the one-step construction. This note checks its primitive estimates and specializes its contraction to HMA. It is not a claim that the outline omitted this proof.

The search used sa-index/README.md, the neighbouring rows of chunk-07.md, and obligations.md lines 390–403. The complete-account search used ca-4.12-4.19/README.md and chunk-04.md lines 45–71. The pinned [outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) and [complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex) were each fetched once. The existing literature record lit-balaban.md, lines 1–90, was also read; no inaccessible paper is used below.

| Source checked | What is used; source status |
|---|---|
| SA 7943–8001 | The embedded double block, implicit contour mean, explicit block average, and physical logarithm \(q_V\); definitions. |
| SA 8002–8053 | The mean contraction, holomorphy and covariance; proved on the small branch. |
| SA 8055–8163 | Local unitary gauges, a bounded joint holomorphic map, and dimension-independent Cauchy estimates; proved under the displayed local smallness. |
| SA 8165–8241 | Isolated pivots, the coefficient \(L^{-3}I_3\), and its inverse perturbation estimate; proved under QC18. |
| SA 8255–8306 | The nonlinear contraction and its converse; proved under those primitive hypotheses. The source says “exactly finite range, not merely exponentially local” (8286–8288). Older-domain inclusion “remains a different estimate” (8305–8306). |
| SA 8362–8390 | The local estimates precede \(M\); input ceilings and any complex gauge condition numbers must be charged. This is not an all-window admission theorem. |
| CA-I 46952–47063, 47118–47231 | The analogous unit-lattice operators, pivot inverse and averaged-background admission hypotheses; conditional results. Its convention gives \(J_c=L^{-3}\pi_c\), not \(J_c=\pi_c\). We use the outline's actual mean and normalization. |

Local dependencies read: HMA in full; [hma-gate](../gates/hma-gate.md) finding 6; [st1-r4](st1-r4.md) AV/CURV, CH, Lemma 3 and F2; [fcon](fcon.md) D1–D4 and Lemma 1; [dom](dom.md) its imports, Theorem 13 and Lemma 14; and [descent](descent.md) AV, its order, and Lemmas 1–2. ST1 F2 already proves a conditional nonlinear chart. Only its primitive support, analytic-domain and inverse requirements are used here; its nonlinear conclusion is not assumed. DOM's real pivot-test estimate is not substituted for complex chart admission.

Keep HMA's geometry, active rows, pivot set, common analytic branches and complete reads fixed. A complete read includes the intermediate averaging carriers and their margins. Retained coordinates are parameters; a restricted chart sets their variations to zero. Distances below are in level-\(k\) units. Assume \(L\ge27\) is odd, with IN1 Amendment 1's further floor.

For a traceless matrix \(A=\sum_{j=1}^3z_j\sigma_j\), write \(\|A\|\) for its operator norm and \(|A|_c=|z|_2\). Then
\[
 |A|_c\le\|A\|\le\sqrt2|A|_c\le2|A|_c.                 \tag{1}
\]
Indeed \(\operatorname{tr}(A^*A)=2|z|_2^2\), and the Hilbert–Schmidt norm lies between the operator norm and \(\sqrt2\) times it. Array norms are supremum norms. We first use operator norm, then convert to HMA's complex colour norm. Unitary conjugation is isometric in both.

## 2. Explicit one-step analytic constants

Set
\[
 a=\frac1{2^{16}L},\qquad K_1=\frac2a,\qquad K_2=\frac{16}{a^2},
 \qquad v_*=\min\left\{\frac a8,\frac1{4L^3K_2}\right\}.       \tag{2}
\]
An admissible local reference has a **real** gauge \(s_c\) on each double block \(D_c\), and on each single block read by a contour mean, with
\[
 V^{s_c}=e^{iv_c},\qquad \|v_c\|_\infty<v_* .                 \tag{3}
\]
Different blocks may use different gauges. Section 6 checks this condition on HMA's working class, with early ceilings. No complex gauge with an uncontrolled condition number is used.

**Lemma 1 (the actual mean, with constants).** On
\(\|v\|_\infty<a,\ \|D\|_\infty<a\), the actual contour means and \(q_{e^{iv}}(D)\) are jointly holomorphic. They satisfy
\[
 \|q_{e^{iv}}(D)\|_\infty\le1,\qquad
 \|W^{e^{iv}}(D)\|,\ \|W^{e^{iv}}(D)^{-1}\|\le2.             \tag{4}
\]
They are the branches of QC1–QC4 and AV.

*Proof.* Put \(E(X,Z)=\log(e^Xe^{-Z})-X+Z\). If \(s=\|X\|+\|Z\|\le1/4\), convergent series give
\[
 \|e^Xe^{-Z}-I\|\le\frac{s}{1-s},\quad
 \|e^Xe^{-Z}-I-X+Z\|\le\frac{s^2}{2(1-s)},
\]
\[
 \|\log(I+H)-H\|\le\frac{\|H\|^2}{2(1-\|H\|)},\qquad
 \|E(X,Z)\|\le2s^2.                                       \tag{5}
\]
The two remainder bounds are at most \(2s^2/3\) and \(4s^2/3\). For \(0<s<1/8\), apply Cauchy's formula to \(E(X,Z+zT)\), \(\|T\|=1\), on \(|z|=s\). Equation (5) gives
\[
 \|D_ZE(X,Z)\|\le8s.                                      \tag{6}
\]
At \(s=0\) this follows from the series. Norming linear functionals reduce the matrix estimates to scalar Cauchy formulas.

For \(\max_j\|X_j\|\le t\le1/128\), solve
\[
 Z=\overline X+\frac1n\sum_jE(X_j,Z),\qquad \|Z\|\le2t.      \tag{7}
\]
The case \(t=0\) gives \(Z=0\). For \(t>0\), the image has norm at most \(t+18t^2<2t\). The Lipschitz constant is at most \(24t\le3/16\). Iteration from zero is Cauchy, since successive differences decrease by this factor. The limit is the unique fixed point in the ball. Convergence is locally uniform in the \(X_j\). Passing Cauchy's formula to the limit proves holomorphy. Trace zero is preserved: triangularizing a matrix near \(I\) gives \(\operatorname{tr}\log P=\log\det P\), which is zero for these determinant-one products. For unitary products the small logarithm is anti-Hermitian, since conjugate transpose changes it to its negative. Thus real iterations remain anti-Hermitian. The matrix \(e^Z\) is the actual small contour mean, with
\[
 \|Z\|\le2\max_j\|X_j\|,\qquad
 \|e^{\pm Z}\|\le e^{2t}\le(1-2t)^{-1}<2.                  \tag{8}
\]
Normalized nonnegative path weights sum to one, so no path-count factor enters.

A product of exponentials with total exponent norm \(b\le1/4\) satisfies
\[
 \|P-I\|\le e^b-1\le\frac b{1-b},\qquad
 \|\log P\|\le\frac b{1-2b}\le2b.                          \tag{9}
\]
An oriented link of \(e^{iD}e^{iv}\), or its inverse, has total exponent norm at most \(2a\). Each internal path has at most \(2L\) links. Its logarithm has norm at most \(8La<1/128\). Equation (8) bounds the mean logarithm by \(16La\). Each straight segment costs at most \(2La\). The closed product \(Z_x\) in QC3 therefore has total exponent norm at most \(36La<1/4\). Its logarithm has norm at most \(72La\). The normalized outer sum has the same bound.

In the relative product defining \(q\), the two outer exponentials cost at most \(144La\). The two straight products cost at most \(4La\). Thus
\[
 \|q_{e^{iv}}(D)\|\le296La<1.                             \tag{10}
\]
These are rational bounds; \(296<2^{16}\) suffices. Every logarithm remains in its convergent series ball. Products, inverses and (7)'s uniform limit prove joint holomorphy. The mean and its inverse obey (8). Local uniqueness identifies the construction with AV's regular branch. ∎

**Lemma 2 (Cauchy bounds and the pivot inverse).** Under (3), for \(\|D\|_\infty<a/4\), let \(K_V=q'_V(0)\) and \(R_V(D)=q_V(D)-K_VD\). Then
\[
 \|K_V\|\le K_1,\quad \|q''_V(D)\|\le K_2,\quad
 \|R_V(D)\|\le\frac{K_2}{2}\|D\|^2,\quad
 \|DR_V(D)\|\le K_2\|D\|.                                 \tag{11}
\]
Each selected pivot block is invertible and holomorphic, with
\[
 \|J_c^{-1}\|\le H:=2L^3.                                 \tag{12}
\]

*Proof.* A scalar circle of radius \(a/2\) about \(D=0\) in Lemma 1 gives \(K_1\). For second derivatives at \(\|D\|<a/4\), use two scalar directions of radius \(a/4\). Their sum stays below \(3a/4\), giving \(16/a^2\). This constant also bounds \(D_vD_Dq\) for \(\|v\|,\|D\|<a/4\). Supremum-norm directions avoid any factor counting bonds. Taylor's integral formula along \(tD\), \(0\le t\le1\), gives (11).

Put \(h=(L-1)/2\) and \(p(c)=(y+he_\mu,y+(h+1)e_\mu)\). Internal paths stay in a block and contain no pivot. A straight segment in QC3 is parallel to \(c\) and crosses only the face between its endpoint blocks. Its only possible selected pivot is \(p(c)\). This proves isolation, including at nonlinear order.

At \(V=I\), differentiating the mean equation gives the arithmetic mean of path sums. The straight reference derivative in each closed logarithm cancels its final derivative in QC3. Hence
\[
 (K_ID)(c)=\sigma_D(y)+L^{-4}\sum_{x\in B(y)}D([x,x+Le_\mu])
                    -\sigma_D(y'),                        \tag{13}
\]
where \(\sigma_D\) averages the internal contour sums. These contain no pivot. Precisely the \(L\) starting points with zero transverse displacement give a segment containing \(p(c)\). Every occurrence is positive. Thus \(J_c(I)=L^{-3}I_3\).

In (3)'s unitary gauge, the mixed Cauchy estimate gives
\[
 \|J_c(e^{iv_c})-L^{-3}I_3\|\le K_2\|v_c\|<\frac1{4L^3}.
\]
The Neumann series bounds its inverse by \(4L^3/3<2L^3\). Transforming back multiplies on both sides by unitary adjoint maps and preserves the norm. The inverse is holomorphic where its determinant is nonzero. No nonlinear chart was assumed. ∎

## 3. A quantitative holomorphic implicit-function theorem

This proof specifies every radius and applies simultaneously to all active rows.

Let \(\iota u\) extend free coordinates by zero on pivots. Let \(h_Vw\) equal \(J_c^{-1}w(c)\) at \(p(c)\), and vanish elsewhere. Isolation gives
\[
 K_Vh_V=I,\quad \|h_V\|\le H,\qquad
 \mathsf C_V=\iota-h_VK_V\iota,\quad K_V\mathsf C_V=0,\quad
 \|\mathsf C_V\|\le B:=1+HK_1.                             \tag{14}
\]
The map preserves free coordinates. All maps in (14) are holomorphic in the reference.

Set
\[
 r=\min\left\{\frac a8,\frac1{8HK_2}\right\},\qquad
 \rho_{\rm op}=\frac r{2B}.                                \tag{15}
\]
For \(\|u\|<\rho_{\rm op}\), put \(t=\mathsf C_Vu\). In the pivot subspace solve
\[
 z=-h_VR_V(t+z),\qquad C_V(u)=t+z.                         \tag{16}
\]
On \(\|z\|\le\|t\|\), one has \(\|t+z\|\le2\|t\|<r\). Equation (11) gives
\[
 \|h_VR_V(t+z)\|\le2HK_2\|t\|^2\le\frac18\|t\|,\qquad
 \|h_VDR_V(t+z)\|\le HK_2r\le\frac18.                      \tag{17}
\]
The map preserves the closed ball and is a contraction. At \(t=0\), its fixed point is zero. Otherwise iteration from zero converges geometrically, with
\[
 \|z_{n+1}-z_n\|\le(1/8)^n\frac{HK_2}{2}\|t\|^2.
\]
This is uniform on the common reference domain and the free ball. Each iterate is holomorphic in \((V,u)\). Passing Cauchy's formula through the locally uniform limit proves joint holomorphy.

Equations (14)–(16) give \(q_V(C_V(u))=0\) and \(C_V(u)|_{\rm free}=u\). Moreover,
\[
 C_V(0)=0,\quad C'_V(0)=\mathsf C_V,\qquad
 \|C_V(u)\|\le2B\|u\|<r,\quad
 \|C_V(u)-\mathsf C_Vu\|\le2HK_2B^2\|u\|^2.                \tag{18}
\]
Differentiation and the Neumann series give
\[
 \|D_uC_V(u)\|\le\frac B{1-HK_2r}\le\frac87B.               \tag{19}
\]

For full-coordinate uniqueness, let \(a_1,a_2\) be solutions with the same free coordinates and \(\|a_i\|<r\). Their difference is pivot-supported. Therefore
\[
 a_1-a_2=-h_V(R_V(a_1)-R_V(a_2)),\qquad
 \|a_1-a_2\|\le\tfrac18\|a_1-a_2\|.
\]
They agree. This is the actual small graph of HMA and ST1 F2, with the same free variables. Real inputs give real iterates and a real graph. Empty constraint or free-coordinate sets obey the same statement.

## 4. Exact reads and gauge transport

For row \(c\), (16) uses only \(u\), \(V\), and its own pivot on \(D_c\). The coefficient \(J_c^{-1}\) and the pivot component of \(t\) read that same block. Induction through the iterates proves exact dependence on these data alone. Taking the limit introduces no new reads. Equations can share free coordinates; no product decomposition of their free variables is asserted.

A double block and its one-bond margin lie within \(\ell^\infty\) distance \(2L+2\) of the relevant pivot base (in \(\ell^1\) the reach is about \(5L/2\); the read radius \(r_p=4L+8\) holds in both). For a bare-field read after \(k\) averages, each lower step adds at most \((2L+2)L^{-j}\), \(1\le j\le k\), in level-\(k\) units. This is QC3's double-block read, rescaled at that step. The additional reach is at most
\[
 (2L+2)\sum_{j=1}^kL^{-j}<\frac{2L+2}{L-1}\le3.            \tag{20}
\]
One safe common radius, including endpoint and bond margins, is
\[
 r_p=4L+8.                                                \tag{21}
\]
It bounds the free-variable and \(V\)-reads, and also their composed bare-field reads. Embedded lifts and complete margins are retained. No field outside a supplied read is extended. A restricted chart has the identical formula after retained variations are set to zero.

For a real site gauge \(g\), set \(O_gD(b)=\operatorname{Ad}(g(b_-))D(b)\). Path products transform by their endpoints. Conjugating the mean equation and using local uniqueness gives
\[
 W^{V^g}_{b,x}(O_gD)=g(y_b)W^V_{b,x}(D)g(x)^{-1},\qquad
 q_{V^g,c}(O_gD)=\operatorname{Ad}(g(c_-))q_{V,c}(D).        \tag{22}
\]
These identities hold on the specified common branches. A gauge sends (3) to the same condition, using \(s_cg^{-1}\), with unchanged norms. Hence \(O_gC_V(u)\) is a solution for \(V^g\), has free coordinates \(O_gu\), and lies in the uniqueness ball. Section 3 gives
\[
 C_{V^g}(O_gu)=O_gC_V(u).                                 \tag{23}
\]
This proves covariance of the whole nonlinear function. It also identifies constructions on overlapping local gauge charts. Gauges certify estimates only; they are not coefficients or additional reads of \(C_V\).

## 5. PIV constants in HMA's norms

By (1), (4), (15), and (18), choose
\[
 \boxed{\rho_p=\frac r{4B},\quad C_p=4B,\quad
 \rho_a=\frac a2,\quad G=2,\quad r_p=4L+8.}                 \tag{24}
\]
For \(|u|_{c,\infty}<\rho_p\), its operator norm is below \(\rho_{\rm op}\), and
\[
 |C_V(u)|_{c,\infty}\le\|C_V(u)\|_\infty
                 \le4B|u|_{c,\infty}=C_p|u|_{c,\infty}.    \tag{25}
\]
For \(|D|_{c,\infty}<\rho_a\), one has \(\|D\|_\infty<a\). Lemma 1 in a local unitary gauge, followed by (22), gives
\[
 \|W^V(D)\|\le G,\qquad \|W^V(0)^{-1}\|\le G.               \tag{26}
\]
Endpoint multiplication by unitaries preserves these bounds, even when the real reference contour is far from \(I\). Rep is not required.

All constants in (24) depend only on the fixed one-step scale and norm convention. In particular \(B=1+4L^3/a\), \(r>0\), and \(\rho_p>0\). The formulas have the source's powers \(C_p=O(L^4)\) and \(\rho_p\asymp L^{-9}\), with fixed prefactors specified in (2), (14), (15), and (24). Only the explicit formulas are used.

## 6. Working-domain check and IN1 order

We check (3) using the primitive AV/CURV bounds recorded in ST1 line 127 and Lemma 3, on complete admitted averaging carriers. These are retained averaging inputs, not a conclusion about unadmitted histories. This explicitly states the averaging content used for admission; finite-stencil holomorphy alone would not prove (32).

Name the early averaging constants as follows. Let \(r_{\rm av}>0\) be a fixed weighted value radius for the raw-average bound, \(C_Q\ge1\) its constant, and \(v_{\rm rec}>0,C_{\rm rec}\ge1\) constants for the real curvature recursion
\[
 v_{n+1}\le L^2v_n+C_{\rm rec}(L^2v_n)^2
                         \quad(L^2v_n<v_{\rm rec}).        \tag{27}
\]
Here \(v_n\) is the largest plaquette defect on the complete intermediate reads. The raw relative row logarithm of \(\mathcal M^k(e^{i\eta A'}U)\) versus \(\mathcal M^kU\) has bound \(C_Q\xi_k\sup\|A'\|\), on the fixed value ball. This is AV's raw row bound; a straightened row without its node factors would not suffice. Set
\[
 C_E=2LC_Q,
\]
\[
 a_0^*=\min\left\{\frac{v_{\rm rec}}4,\frac1{16C_{\rm rec}},
                         \frac{v_*}{128L}\right\},\qquad
 a_1^*=\min\left\{\frac{r_{\rm av}}{4L},\frac{v_*}{16C_E}\right\}.
                                                               \tag{28}
\]
Both are positive and precede \(M,\bar\kappa,\kappa\).

Plaquette defects \(|\partial U-I|\) and CURV's \(v_n\) are taken in operator norm; any equivalent norm costs at most a factor 2, absorbed by the room in (33). Suppose HMA's absolute radii satisfy \(a_0<a_0^*,a_1<a_1^*\). Put \(V_0=\mathcal M^kU\) and \(V=\mathcal M^k\mathbf U\). For the real averages, \(v_0\le a_0L^{-2k}\). Set \(w_n=L^{2(k-n)}v_n\). Equation (27) becomes
\[
 w_{n+1}\le w_n+C_{\rm rec}L^{2(n+1-k)}w_n^2.              \tag{29}
\]
The sum of its geometric coefficients is at most \(L^2/(L^2-1)<2\). If preceding \(w_n\)'s are at most \(2a_0\), iteration of \(1+x\le e^x\) bounds the next one by
\[
 a_0\exp(4C_{\rm rec}a_0)\le\frac{a_0}{1-1/4}
                               =\frac43a_0<2a_0.          \tag{30}
\]
Also \(L^2v_n\le2a_0<v_{\rm rec}\) at every step using (27). First-crossing induction proves \(v_k\le2a_0\). For \(k=0\), this is immediate.

On the rectangular double block, use a coordinate-order comb gauge of real \(V_0\). Sliding an extra edge past later coordinate segments inserts at most \(8L\) plaquettes. There are at most three later coordinate intervals, each shorter than \(2L\); \(8L\) also covers endpoints. Unitary telescoping gives
\[
 \|V_0^{s_c}(b)-I\|\le8L\sup_p\|\partial V_0(p)-I\|
                                    \le16La_0.            \tag{31}
\]
This gauge needs no extension or global holonomy condition.

The AV value ball is available since \(2La_1<r_{\rm av}\), with (1) accounting for complex colour norms. Its raw row bound gives
\[
 V=e^{iE}V_0,\qquad \|E\|_\infty\le C_Ea_1.                \tag{32}
\]
The extra factor \(L\) safely includes the largest-incident-scale convention. It is fixed early, not multiplied once per depth. A level-\(k\) row itself has \(\xi_k=1\), so the direct bound is the smaller \(2C_Qa_1\). Common branches and complete carriers remain AV hypotheses.

Since \(C_Ea_1<1/2\), (31) and the exponential series imply
\[
 \|V^{s_c}-I\|\le2C_Ea_1+16La_0<\frac{v_*}{4}<\frac12,
\]
\[
 \|i^{-1}\log V^{s_c}\|\le2\|V^{s_c}-I\|
                  \le4C_Ea_1+32La_0<\frac{v_*}{2}.         \tag{33}
\]
Thus (3) holds with room, uniformly on the complex domain, also for single-block reads. All hypotheses of Lemmas 1–2 and Section 3 have been checked for these references. The same local equations and uniqueness identify their regional restrictions with ST1's CH charts on common small domains.

These ceilings fit the existing HMA/descent formulas. In the early primitive ceiling \(a_h\) of hm, include
\[
 a_h\le\min\{16L^2a_0^*,\ 32L^5a_1^*\}.                   \tag{34}
\]
Decreasing an admissible analytic ceiling preserves its estimates. Do this before forming hm's
\[
 h=\min(a_R,a_h,1/2),\qquad
 r_{\rm loc}=\min\{h/(16L^2),c_L/(8H_1)\}.
\]
Then descent (7), already required by HMA, implies
\[
 a_0<\frac h{16L^2(1+C_{\rm pot}M)}\le a_0^*,\qquad
 a_1<\frac{r_{\rm loc}}{2L^3}\le\frac h{32L^5}\le a_1^*.    \tag{35}
\]
No late constant defines an early radius. If working constants were already fixed without (34), impose (28) as row-6 absolute ceilings instead; (24) does not change. The assertion concerns these chosen working domains, not every R4 class with arbitrary radii.

IN1 rows 1–3 choose geometry, \(L\), primitive AV constants, (2), (28), and early ceilings. Before \(\kappa\) in row 4, fix (12), (14), (15), and (24), then HMA's constants which consume them. Amendment 1 raises the earlier floor on \(L\) and the later floor on \(\kappa\). Row 5 chooses \(\bar\kappa,M\) and their read/collar floors. Row 6 chooses absolute radii and amplitude ratios. Rows 7–8 make the later choices. Rows 9–10 make the running radii small enough and choose coupling and grid. None of (24) depends on \(M,\bar\kappa\), depth, volume, shape, or a larger admitted separation.

HMA Lemma 3 can therefore use
\[
 \rho=\min\{\rho_p,\rho_a/C_p\}>0,\qquad 1+G^2=5.           \tag{36}
\]
Section 4's full reads supply its early finite gauge-read radius. Stored tests, actual formation, whole-history admission and physical branch matching remain separate. DOM's outstanding local-rule and roster coverage claims do not follow from (33).

## Result

**Proof** PIV holds for HMA's fixed admitted working domains, retaining the primitive averaging inputs stated in Section 6 and choosing the early ceiling (34), which implies the working ceilings (28). The constants are (24). The actual graph is jointly holomorphic, satisfies (25), has the exact finite reads (21), and obeys (23). The contour bounds are (26). Their radii and bounds precede \(\kappa\) and are independent of \(M,\bar\kappa\), depth and volume.

This is a reconstruction and quantitative specialization of Sussman–Alpoge's proved one-step argument, with explicit norm and working-domain estimates. It retains the frozen primitive averaging/admission inputs and does not prove actual-history DOM. Proved here by Codex, not yet checked by the other model. Research text, not an audit; grants no status.

## Change log (freeze, 2026-11-05)

Written by Codex in one proof-lane round on the Mini. Refereed line by line by a fresh Claude session ([piv-gate](../gates/piv-gate.md)): first failing step none, no fabricated step, 4 findings, none fatal, none changing (24). Applied by the lead (Claude):

1. (20): \(\ell^\infty\) distance stated.
2. PIV is proved conditional on ST1 r4's AV/CURV (constants \(C_Q,r_{\rm av},v_{\rm rec},C_{\rm rec}\)); hma now names this text as PIV's supplier (hma Amendment 1).
3. Working domain: the lead records the second option, (28) imposed as an IN1 row-6 ceiling on HMA's radii (hma Amendment 1). This leaves frozen hm (7) unchanged.
4. Plaquette-defect norm: operator norm.

Referee checks kept: the implicit-function step (radius \(\min\{a/8,1/(8HK_2)\}\), contraction 1/8, uniqueness on the full ball) is SA QC22–QC24 with explicit constants; Lemmas 1–2; exact reads (21) (SA 8284–8288); covariance (23); contour bounds (26) with \(G=2\); ceilings (28)–(33); constants match SA's powers and depend only on \(L\) and early AV constants.

Status: **frozen.** PIV holds as HMA uses it, from ST1 AV/CURV, on HMA's working domains with (28) as a row-6 ceiling.

