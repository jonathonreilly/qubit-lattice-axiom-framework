# A1 through Balaban's layer induction
Provenance: Codex (GPT-6; exact serving variant and runtime effort not exposed), requested effort max; checkout `87d622fadaafd8630ee58e2a009190b756464b1e`; Sussman–Alpoge outline `31a47c543775`; T. Balaban, *The variational problem and background fields in renormalization group method for lattice gauge theories*, Commun. Math. Phys. **102** (1985), 277–309; research text, not an audit, and no status granted.

## 1. Target, attribution, and proof contract

Queue row 81 targets A1, item 1 of `sa-ledger.md`, and the uniform
regularity input (U) used by rows 77 and 80. The question is whether the
fixed-geometry argument of `a1-orbit.md`, Sections 7–9, can be replaced by
an induction with one choice of constants for every separated sequence.
The two growing constants exhibited there concern a particular gauge and
a discontinuous seed; neither is a counterexample to the critical-orbit
statement. No run supplies a step of the argument here.

The endpoint is a **conditional proof** of the default
critical-orbit, holomorphy and restriction theorem in Sections
8–9. The sole cited-pending operator package used by that
proof is F0, specified in Section 3.9. Section 10 distinguishes
this result from the additional, unproved pointed-core
admission clause of the full A1 obligation.

The target and its centred contour-average construction are credited to
Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text. All uses of the variational reduction, constraint straightening,
contraction, local improvement, and induction in CMP 102 are credited to
Tadeusz Balaban. An imported statement marked **cited-pending** is an
unchecked mathematical premise, not a discharged library result.

Use level-\(k\) units, \(\eta=L^{-k}\), \(\xi_j=L^{j-k}\), and
\(\mathsf L\) equal to the largest corner scale of a bond or plaquette.
For a real configuration define
\[
 r(U)=\max\{\sup_p\eta^{-2}\mathsf L(p)^2|U_p-1|,
                    \sup_b\mathsf L(b)^3|J(U)(b)|\}.
\]
The datum norm is the maximum error of the outline's actual test loops,
including substituted finer averages at seams. The default convention
omits inward bonds. The extension retaining inward bonds additionally
tests pinch holonomies. These are different constraint spaces and must
not be identified silently.

A1 asks for a nonempty critical residual orbit, uniqueness in a fixed
larger regularity neighbourhood, a linear estimate for \(r(U)\), and a
Borel real representative with holomorphic continuation on uniform local
scale balls. Its restriction, seam, and torus clauses also belong to the
target. A proof for Balaban's average alone does not automatically prove
this statement for the outline's average.

The outline was fetched once to `/tmp/sa_ym4.tex`. Balaban's OCR and scan
are read at `~/ym4d-papers/cmp102.txt` and
`~/ym4d-papers/balaban_cmp102_277.pdf`; neither is copied into the
repository. Source equations below use their printed numbers. Corrections
of garbled OCR are identified where used.

## 2. What CMP 102 actually proves and what has to be transported

Balaban's notation is retained in this section. Put
\(s_j=L^j\eta\), let \(\Lambda_j\) be his determining sites, and
let \(\mathcal B_k=\bigcup_j\Lambda_j\). A configuration is in
\(\mathfrak U_k(\varepsilon_0)\) when, on every \(\Omega_j\),
\[
 |\partial U-1|<\varepsilon_0\eta^2s_j^{-2},\qquad
 |D_U^*\partial U|<\varepsilon_0\eta^2s_j^{-3}.                 \tag{2.1}
\]
Its averages equal \(V\) on \(\Lambda_j\); residual gauges are
one at the determining sites. Tests at a seam use the finer average
on the missing coarse edge (CMP 102, p. 278, (7)).

**Theorem 1 as used, with credit to Balaban.** There are
\(a_0,a_1,B_3>0\), depending on \(d,L\), with
\(B_3a_1\le a_0\), such that data with test errors less than
\(\varepsilon_1\le a_1\) have a minimal orbit in
\(\mathfrak U_k(B_3\varepsilon_1)\). It is the only critical orbit
in \(\mathfrak U_k(\varepsilon_0)\) whenever
\(B_3\varepsilon_1\le\varepsilon_0\le a_0\). On the two-layer
cubes specified on pp. 278–279, of side \(2Ms_j\), a gauge gives
\(U^{u^{-1}}=e^{i\eta A}\) and
\[
 |A|\le B_3M\varepsilon_1s_j^{-1},\quad
 |\nabla A|\le B_3M\varepsilon_1s_j^{-2},\quad
 |\partial^*\partial A|,|\Delta A|
       \le B_3M\varepsilon_1s_j^{-3}.                         \tag{2.2}
\]
The first-difference Hölder bound has exponent \(\beta<1\),
constant \(B_4(\beta_0)M\varepsilon_1\) for
\(0\le\beta\le\beta_0<1\), and scale \(s_j^{-2-\beta}\).
The allowed size is \(M\le M(\varepsilon_1)
=R_1M_1a_1/\varepsilon_1\). These last parameters were badly
garbled in the OCR; the scan of p. 279 fixes them. This is a claim about
his average and his boundary conventions.

The reconstruction of (2.1) is fixed by the powers in printed (2),
the current identity (28), and the scaling in (9)–(10). Balaban's full
matrix expression \(\eta^{-2}D_U^*\partial U\) is stronger than
its imaginary part \(J(U)\). There is a harmless converse at small
real curvature: for a unitary matrix \(W\),
\[
 \operatorname{Re}W-1=-\tfrac12(W-1)^*(W-1).
\]
Each term in a lattice divergence costs at most \(2/\eta\);
there are at most six adjacent plaquettes in dimension four. Thus the
real part of that matrix expression is bounded by
\(C\varepsilon^2\eta\mathsf L^{-4}
\le C\varepsilon^2\mathsf L^{-3}\), with the fixed adjacent-scale
factor at a seam included in \(C(L)\). Therefore the outline's real
curvature/current hypotheses supply (2.1) with radius
\(C(L)(\varepsilon+\varepsilon^2)\). This conversion does not
identify the two averaging maps.

The proof has three distinct uses of smallness:

1. Proposition 2 puts **every** regular orbit in a common Landau chart.
2. Propositions 3–7 solve the critical equation in that chart and obtain
   a preliminary radius \(C_*C_1B_3\varepsilon_1\).
3. Proposition 8 improves **any** sufficiently regular critical point
   to radius \(B_3\varepsilon_1\). This is the step that prevents a
   new factor \(C_*L^3\) at every level.

The centring translation, by itself, is innocuous: at level \(j\)
use the same translated centres and transported bond orientations.
Replacing the single comb by a mean of contours changes the map even
after this translation. The outline explicitly records a linear
\(O(\alpha_0)\) difference at a curved background (mechanism 2,
lines 9822–9840), as well as nonlinear differences. A claim that this
replacement is merely a change of notation would be false.

## 3. Imported statements, exactly at the strength used here

All constants in the following statements are uniform in depth, volume,
and the admitted separated domains. The quantifier is essential. Write
\[
 \|A\|_X=\max_j\sup_{\Omega_j}
          \max\{s_j|A|,s_j^2|\nabla A|\},\quad
 \|f\|_{-3}=\max_j\sup_{\Omega_j}s_j^3|f|,
 \quad\|B\|_\infty=\sup_{\mathcal B_k}|B|.
\]
Here \(qA(c)=s_{j(c)}Q_{j(c)}A(c)\); it is the dimensionless
linear row, not the plain average with its node factors attached.
Pairings of bare fields carry \(\eta^d\); coarse kernels are
integrated with \(s_{j(c)}^d\). This explains the inverse cell-volume
factors in their printed kernel bounds.

### 3.1 CMP 98 (1985), 17–51: averaging operations

**P98.2 — rebuilt in Section 3.5 for Balaban's average**, Proposition 2, used on CMP 102 pp. 278,
300–303. At small curvature, all iterated averages and seam tests
appearing there exist. Their plaquette errors have the scale-square
bound; in particular regularity (2) gives (7) with
\(\varepsilon_1=O(\varepsilon_0)\). On the top two layers of the
local cube in Section F, datum tests of size \(\varepsilon_1\)
give coarse plaquette errors \(\varepsilon_1\) in one part and
\(2L^2\varepsilon_1\) in the adjacent part (p. 303, before (160)).
No claim about an arbitrary contour rule is part of this citation.

**P98.4–5 — rebuilt in Section 3.5 for Balaban's average**, Proposition 4 and Proposition 5,
including (136), (157), used in CMP 102 (44), (55)–(56), (69)–(73).
For complex \(A\) in the fixed small weighted value ball,
\[
 \mathcal Q_j(\eta A)=s_jQ_jA+C_j(s_jA),\qquad
 |C_j(s_jA)(c)|\le C_2s_j^2\sup_{D(c)}|A|^2,                \tag{3.1}
\]
where \(D(c)\) is the double block under row \(c\). The map is
holomorphic for weighted radius less than \(c_4\), its constant
and linear Taylor coefficients vanish, and its derivative is supported
in \(D(c)\). With a functional derivative defined using the bare
\(\eta^d\) pairing, its pointwise kernel is bounded by
\(C_3\varepsilon s_j^{1-d}\) at weighted radius
\(\varepsilon\); this is precisely the scaling used in (72).
Taylor coefficients and the derivative after subtracting its linear
term obey the corresponding Cauchy estimates. The finite-dimensional
analyticity of a *single* row does not prove these uniform iterated
bounds.

### 3.2 CMP 99 (1985), 75–102: regular configurations and gauges

**G99.2 — reduction rebuilt in Section 3.8, conditional on F0**,
Theorem 2 with (1.29), (1.31),
(1.33)–(1.39), used on CMP 102 pp. 280–281. For a pair \(U,U_0\)
satisfying those regularity assumptions and with average mismatch
\(\alpha_1\), the axial representative of their relative field
has a unique conversion to the slice
\[
 U^{u^{-1}}=e^{i\eta A}U_0,\quad RD_{U_0}^*A=0,\quad
 \mathcal Q_j(U_0;\eta A)=B\quad(c\in\Lambda_j),             \tag{3.2}
\]
with the prescribed transformed gauge averages
\(R_0\overline{u}^{\,j}=1\) on \(\Lambda_j\). In CMP 102's
application,
\[
 \|B\|_\infty<2dLC_1\varepsilon_1,\qquad
 \|A\|_X,\ |D^*DA|_{-3},\ |\Delta_{U_0}A|_{-3}
       <B_1(\varepsilon_0+C_1\varepsilon_1).                \tag{3.3}
\]
The row datum \(B\) includes the endpoint/block-factor correction
of (1.31); it is not generally \(i^{-1}\log(VV_0^{-1})\) at
a seam. This theorem is used to cover all competitors, not just to
construct one small solution.

**G99.D — reduction rebuilt in Section 3.8, conditional on F0**,
Section D and (1.70), (1.74), used in
CMP 102 (123)–(126). For \(f\in\operatorname{ran}R\) in a
fixed small \(|\cdot|_{-2}\) ball, the equation replacing
\(RD^*A=0\) by \(RD^*A=f\), while preserving the straightened
constraint and the gauge normalization in (3.2), has a unique small
gauge solution, analytic in its small variables. Consequently a slice
critical point is critical with respect to all constraint-preserving
variations. The existence of an unconstrained Coulomb gauge is a weaker
statement.

**G99.F — reduction rebuilt in Section 3.8, conditional on F0;
its converse is (3.11)**, Section F, in particular Proposition 6,
the local gauges (1.135)–(1.136), and Proposition 7, used in CMP 102
pp. 280, 299–302. On its specified two-layer cubes a regular field
has a small local potential with first, Hölder, and second-difference
bounds of size \(CM\varepsilon_0\) in the local units. The
hierarchical axial normalizations and averaging constructions used in
(144)–(156) exist on these cubes. Conversely, a small relative
potential satisfying (19)–(21) reconstructs a regular configuration
in the original constrained space, with radius
\(O(1)C_1B_3\varepsilon_1\). The torus/boundary enlargements
in that result must be retained.

**G99.1 — rebuilt in Section 3.6**, Lemma 1, used on CMP 102 p. 303.
For the local, axially normalized double block in (154), coarse
closeness \(\alpha_1\) and plaquette radius \(\alpha_0\)
give the fine-bond estimate used there:
\[
 |V_1(x_1,x'_1)-1|
    <4d^2L^2\varepsilon_1+2L^2|x-y|\varepsilon_1,
\]
when \(\alpha_0=L^2\varepsilon_1\) and
\(\alpha_1=2L^2|x-y|\varepsilon_1\). Taking the small logarithm
therefore yields, on the last two layers,
\[
 |B(x,x')|<(8d^2L^2+4L^2|x-y|)\varepsilon_1.                \tag{3.4}
\]
This is the local datum gain in printed (160).

The elementary plaquette expansions (1.21)–(1.22), (1.50), (1.52),
(1.54) used from this paper are rebuilt below as algebraic estimates;
they need no separate cited-pending premise.

### 3.3 CMP 99 (1985), 389–434: background propagators

**P99.H — algebra and reduction rebuilt in Section 3.9, conditional
on F0 and the stated source geometry**, Theorems 3.12–3.13 and
(3.126)–(3.148), used in CMP 102 (45)–(46), (87)–(89),
(103), (110)–(121). There is a positive gauge-fixed quadratic form
\(\Delta_1\), including the quadratic correction caused by the
nonzero reference current. Its constrained minimizer \(H_1\)
and fibre inverse \(\mathfrak G_1\) satisfy
\[
 qH_1=1,\ RD^*H_1=0,\ q\mathfrak G_1=RD^*\mathfrak G_1=0,
 \quad\|H_1B\|_X\le B_0\|B\|_\infty,
 \quad\|\mathfrak G_1f\|_X\le B_0\|f\|_{-3}.              \tag{3.5}
\]
The corresponding uncorrected minimizer \(H\) obeys the same
first-order bound. These operators have the locally scaled exponential
kernel bounds used in (69), (86), (103), (161). The coarse inverse
\((QGQ^*)^{-1}\) has (3.132)'s bound, as needed to estimate
(88)–(89). The correction \(\Delta^{(2)}\) in (79) has the
smallness bound (3.137); omitting it would give the wrong fibre Hessian
at a nonzero current.

**P99.G — reduction rebuilt in Sections 3.9 and 5, conditional on F0
and the stated source geometry**, Theorem 3.3, (3.42), (3.49),
(3.69), and (3.119)–(3.133), used in CMP 102 (128)–(140).
For
\[
 G=(\Delta+DRD^*+Q^*aQ)^{-1},\quad
 H_0=GQ^*(QGQ^*)^{-1}s^{-1},\quad
 P_0=1-GQ^*(QGQ^*)^{-1}Q,
\]
the estimates include the second-order covariant Laplacian estimate
and \(|\Delta_{U_0}H_0B|_{-3}\le B_0\|B\|_\infty\).
Also \(DPD^*\), with \(P=1-R\), is bounded at the stated
weights, the local term \(\Delta-D^*D\) is curvature-small,
and the gauge correction \(\Delta-\Delta_\times\) has the
current identity (138). These are the inputs needed to obtain
second-order bounds; (3.5) alone does not contain them. The identities
and their use are written out in Section 5.

**P95/96 — flat inverse input F0 remains cited-pending; the
summation input is proved in Section 3.7**, also required, although outside the
three papers singled out in the task: CMP 95 (1984), 17–40 and CMP
96 (1984), 223–250 supply the flat operators used in Section F.
CMP 96 Lemma 2.1 controls convolution/Neumann series, and
(2.47)–(2.51) control the mixed-scale sum in CMP 102 (162).
Its precise required value is displayed in Section 6. The unweighted
number of nearby fine bonds cannot replace that sum.

### 3.4 What the four library files actually supply

`lattice-uhlenbeck.md`, Lemma U, supplies a real box gauge with
\(\ell^4\) potential and \(\ell^2\) derivative control. On a
single-scale box with \(N=\xi/\eta\), the hand count
\(6(N+1)^4\le96N^4\) and
\(|\log U_p|\le2\varepsilon N^{-2}\) give
\(\|\log\partial U\|_2\le20\varepsilon\).
It therefore applies at a radius independent of depth. But
\(\sup|A|\le\|\eta A\|_4/\eta\) loses \(\xi/\eta\)
in the required scaled supremum norm. Its gauges do not have the
prescribed node values. This proves a useful local input and does not
discharge G99.2, G99.D, or G99.F.

`fibre-propagator.md`, Theorems F/F-D, supplies an energy-space
saddle inverse for its class map and restricted gauge projector,
at a supplied regular critical background. `c0-loc.md`, Sections
8–11, supplies common-frame comparisons and coercivity on its
admitted pruned-leaf geometry; its Section 11 explicitly keeps the
top-collar admission and existence of a regular stationary lift as
inputs. Neither result is a proof of (3.5) and P99.G in supremum
and second-order norms on every outline sequence. In particular,
existence of a background cannot be imported from a theorem which
assumes that background's stationarity.

The requested `gates/a3-gate-b2c312b2e.md` is absent from the tree at
`87d622fad` (including the named gates directory). Consequently no result
of `a3-response.md` is used here as a checked premise. Its stated flat
theorem concerns local energy norms; its stated curved theorem assumes
(W), and its nonlinear continuation assumes (U). Neither headline
discharges the supremum estimates needed here, and importing (U) would
be circular. The preceding limitations of the other library results
remain in force.

### 3.5 Rebuilding CMP 98, Propositions 2, 4 and 5

Credit throughout this subsection: Balaban, CMP 98, pp. 24–26 and
34–42, especially (48)–(54), (122)–(157). These are proofs for his
straightened average. Section 7 treats the additional transport question;
it is not contained in these citations.

**Curvature.** On the four-block neighbourhood of a coarse square,
choose coordinate-tree gauge based at a corner. Moving a link to the
tree by elementary squares expresses its transport as a product of at
most \(dL\) conjugated plaquettes. The exact telescoping identity
\(\prod_i W_i-1=\sum_i(\prod_{h<i}W_h)(W_i-1)\), with unitary
factors, bounds its distance from 1 by the sum of those plaquette
distances. Write the resulting links as \(e^{ia_b}\), with
\(|a_b|\le C_dL\varpi\). For \(\sum|a_b|\le r<1\), expanding
the exponentials and \(\log(1+X)=\sum_{n\ge1}(-1)^{n+1}X^n/n\)
bounds all terms after the linear term by
\(C_r(\sum|a_b|)^2\). These absolutely convergent series also
justify their differentiation on a smaller complex ball.

The linear term of the four averaged edges is the average, over the
starting points in a block, of the boundary sum of an \(L\)-square.
Every interior edge cancels with its reverse. Each such square has
exactly \(L^2\) elementary plaquettes. Thus, if \(v_m\) bounds
plaquettes after \(m\) steps,
\[
 v_{m+1}\le L^2v_m+C(L^2v_m)^2.                         \tag{3.6}
\]
This cancellation, not a bound on four separate contours, gives the
coefficient \(L^2\). It is Balaban's (48). The remainders from the
four edges and elementary squares satisfy the displayed quadratic
bound by the preceding convergent series.

To check uniformity, suppose initially \(v_0\le\alpha L^{-2n}\).
Put \(w_m=L^{2(n-m)}v_m\). As long as \(w_m\le2\alpha\), (3.6)
gives
\[
 w_{m+1}-w_m\le4C\alpha^2L^{2(m+1-n)},\qquad
 \sum_{m=0}^{n-1}L^{2(m+1-n)}\le(1-L^{-2})^{-1}.
\]
Choose \(4C\alpha/(1-L^{-2})<1\), and choose \(2\alpha\)
inside the one-step logarithm domain. Induction then gives
\(w_m<2\alpha\) at every step. Retaining the quadratic term gives
\(v_n\le\alpha+C'\alpha^2\), the strength of (54). The argument
uses only the four underlying blocks. At a seam, replacing its missing
edge by the finer average has precisely the one-level scale loss
\(L^2\); applying the same estimate in those finer units gives the
\(2L^2\varepsilon_1\) bound used in CMP 102 (160).

**Analytic remainder.** Work in units in which the final double block
has side 1, so \(t_m=L^{m-n}\). Removing the two endpoint factors
from one averaging step leaves a linear map of norm
\(L(1+C\alpha t_m^2)\) on link angles, and a remainder bounded
by \(CL^2\) times the squared angle norm. Here is the cancellation
behind that assertion. Differentiate a product along a contour: each
insertion is transported to the initial endpoint. The contour pieces
inside the two endpoint blocks cancel against the derivatives of the
two removed block factors. The remaining insertions are those of the
straight segments. Changing their transports around an elementary
square costs its plaquette error; summing the at most \(C_dL^2\)
squares gives \(C\alpha t_m^2\). The differentiated logarithm and
exponential are identity plus an operator of this size: this follows
by differentiating their convergent series. A second derivative costs
at most the product of the two contour lengths, giving \(CL^2\).
This is the content of (110)–(126), with the endpoint cancellation
in (120). It applies to complex perturbations of a real reference.

Let \(a_m\) be the angle after \(m\) steps, divided by \(t_m\),
and let \(r=\sup|A|\). The preceding estimates give
\[
 a_{m+1}\le(1+C\alpha t_m^2)a_m+Ct_{m+1}a_m^2.
\]
Since \(\sum t_m^2\le(1-L^{-2})^{-1}\) and
\(\sum t_m\le(1-L^{-1})^{-1}\), a bootstrap gives
\(a_m\le2r\) for fixed small \(\alpha,r\). For example, bound
the product of the linear factors by
\(\exp(C\alpha/(1-L^{-2}))\), require it to be at most \(5/4\),
and choose \(r\) so that the accumulated quadratic terms are at
most \(r/4\) before multiplication by this product. Applying the
same recurrence to the difference from the composed linear maps gives
\[
 |\mathcal Q_n(\eta A)-Q_nA|
 \le4Cr^2 e^{C\alpha/(1-L^{-2})}/(1-L^{-1}).              \tag{3.7}
\]
All constants are independent of \(n\). Each composition is analytic
on this same ball; the expansion has zero constant and linear terms
after subtraction. Rescaling the final block to side \(s_j\) proves
(3.1). This reconstructs the powers in the OCR of (130)–(135);
the scan of printed p. 38 confirms that the two sums are in \(L^m\)
and \(L^{2m}\), respectively.

**Functional derivative, which is stronger than (3.7).** Let
\(Q'_m f\) denote the normalized positive double-block averaging
majorant in (141), and let \(Q\) be the positive straight-segment
average. Their counting identities are obtained by counting starting
points of a segment containing a given link:
\(Q''Q_mf\le2dQ'_{m+1}f\),
\(QQ'_mf\le(2-L^{-1})Q'_{m+1}f\), and
\(Q''Q'_mf\le2dQ'_{m+1}f\). End links occur fewer times and
only improve these inequalities. With (139) these give
\[
 |Q_m(U_0)f|\le Q_m|f|+2C'_1\alpha t_m^2 Q'_m|f|.
\]
For completeness the nonlinear induction uses the exact composition
identity (152), in the units of its output block,
\[
 C_{m+1}(A)=LQ(U_0^m)C_m(L^{-1}A)
 +C\big(U_0^m,L^{-1}Q_mA+C_m(L^{-1}A)\big).              \tag{3.8}
\]
Differentiate (3.8), apply the preceding three counting inequalities
and the one-step second-derivative bound, and suppose
\(|DC_m(A)f|\le C_3|A|Q'_m|f|\). The coefficient in the resulting
bound for \(DC_{m+1}\), divided by \(C_3|A|Q'_{m+1}|f|\), is at most
\[
 1-L^{-2}+4dC'_1\alpha L^{-3}
 +\frac{C''_1}{C_3}L^{-2}
 (1+4dC'_1\alpha L^{-2}+C_2L^{-1}r+2dC_3L^{-1}r)^2.     \tag{3.9}
\]
This is (154), checked in the scan of p. 41. Choose
\(C_3\ge6C''_1\), enlarge it for the one-step bound, and then
choose \(\alpha,r\) so that
\(4dC'_1\alpha L^{-1}\le1/4\) and the parentheses squared
are at most 3. The expression in (3.9) is then at most
\(1-L^{-2}/4\). This proves the derivative induction, including
its base case, without losing a factor at each level. At unit output
scale the kernel of \(Q'_m\), with the \(\eta^d\) pairing, is at
most 1 by (141). Restoring the scale makes the kernel bound
\(C_3r s_j^{1-d}\). Its support is the double block because (3.8)
never reads outside it. This proves the strength of (157) used in
CMP 102 (72). The scan of p. 42 fixes the missing OCR right-hand
side of (157): it is \(C_3|A|\), not a bound independent of \(A\).

### 3.6 The reconstruction lemma and the elementary current estimate

Credit: Balaban, CMP 99, 75–102, Lemma 1, pp. 79–80, and
(1.43)–(1.54), pp. 83–86. In relative axial gauge on a double
block, an interior link is a product of conjugated relative
plaquettes filling its rectangle with the coordinate tree. There
are at most \((d-1)(L-1)\) such plaquettes. The two original
curvatures bounded by \(\alpha_0L^{-2}\) bound a relative
plaquette by \(2\alpha_0L^{-2}\). Moving a crossing link along
the common face costs at most \(4(d-1)d\alpha_0\); the straight
reference crossing link is then fixed to within the coarse mismatch
\(\alpha_1\), using the defining mean and its small logarithm
branch. Telescoping each unitary product proves
\[
 |V_b-1|\le4d^2\alpha_0+\alpha_1.                        \tag{3.10}
\]
This is (1.25), with its hypotheses on *relative* contours retained.
With \(\alpha_0=L^2\varepsilon_1\),
\(\alpha_1=2L^2|x-y|\varepsilon_1\), and
\(|\log W|\le2|W-1|\), it proves (3.4).

The current estimate does not need an inverse theorem. Transport the
four perturbations on a plaquette to one endpoint. Expanding their
product gives \(i\eta^2DA\) at first order. Its quadratic part
is the sum of the square of the curl and commutators of the four
insertions. In the latter, replacing neighbouring values by their
value at the base leaves \(2[A_\mu,A_\nu]\); all other terms have
at least one factor \(\eta\nabla A\). Apply the divergence and
use the discrete product rule. The difference of
\([A_\mu,A_\nu]\) is bounded by
\(C|A||\nabla A|\); the explicit \(\eta\) in every remaining
quadratic term cancels the possible \(\eta^{-1}\) of divergence.
The cubic remainder before divergence has size \(C\eta^3|A|^3\),
so after division by \(\eta^2\) and divergence it costs
\(C|A|^3\). Commuting a transport past the reference plaquette
costs \(C\eta^{-2}|\partial U_0-1||A|\). Thus, in local units,
\[
 |J(e^{i\eta A}U_0)-J(U_0)-D^*DA|_{-3}
 \le C\big(|A|_{-1}|\nabla A|_{-2}
             +|A|_{-1}^3+\alpha_0|A|_{-1}\big).          \tag{3.11}
\]
The matrix-current version has the same estimate. These are exactly
the types of terms in (1.54), whose coefficients are 36d, 50d and
10d in Balaban's norm convention. Formula (3.11) records the
reconstruction from the garbled OCR; no equality with those numerical
coefficients is needed in this note. It also proves the converse
regularity assertion of Proposition 7: small \(A,\nabla A,D^*DA\)
over a regular reference give small curvature and current of
\(e^{i\eta A}U_0\). The gauge back to the normalized axial
representative changes neither real norm.

### 3.7 The mixed-scale sums do not require an unverified citation

This supplies the summation and Neumann-series part of CMP 96 used
in CMP 102 (69)–(73), (86), (161)–(163). Credit for its use in
this proof: Balaban. The following counting proof is independent
of the missing CMP 96 text. It applies to the outline's metric
and omitted-inward convention as well.

Let \(y,z\) be tops, with scales \(s_y,s_z\), and let \(d\)
be the layer metric. A path crossing a complete intervening layer
has length at least \(\rho\) in that layer's units: it joins
\(\partial\Omega_{i+1}\) to \(\Omega_i^c\), whose ordinary
distance is at least \(\rho s_i\). The portions for distinct
complete layers are disjoint. The first and last layers need
not be crossed completely. Consequently
\[
 |\log_L(s_y/s_z)|\le1+d(y,z)/\rho.                       \tag{3.12}
\]
The same argument bounds the largest scale met by a path of length
at most \(R\), starting at \(y\), by \(s_yL^{1+R/\rho}\).
Its ordinary length is at most \(Rs_yL^{1+R/\rho}\). Thus the
tops at layer distance at most \(R\), of any fixed scale, lie in
an ordinary ball of that radius, and their mesh is at least
\(s_yL^{-1-R/\rho}\). A cube count bounds their number by
\(C(R+1)^4L^{8+8R/\rho}\). There are at most
\(3+2R/\rho\) possible scales. Lifting a torus path to its
covering lattice gives the same upper bound: identifying periodic
copies only reduces the number of endpoints.

For fixed \(a>0\), \(p\in\mathbb R\), and nonnegative integer
\(q\), choose \(\rho\ge2(8+|p|)\log L/a\), with \(\rho\ge1\).
Summing integer distance shells using (3.12) gives
\[
 \sup_y\sum_z e^{-a d(y,z)}(1+d(y,z))^q(s_y/s_z)^p
 \le C L^{8+|p|}\sum_{m\ge0}(m+2)^{q+5}e^{-am/2}<\infty. \tag{3.13}
\]
The last convergence needs no numerical evaluation: for all large
\(m\), \((m+2)^{q+5}\le e^{am/4}\), and the tail is geometric.
Constants may be defined by this convergent series. This proves
the sum required in (162), with \(s_y=1,p=1,q=1\) in the
local rescaling used there.

The convolution measure matters. Suppose
\[
 |K(y,z)|\le b\,s_z^{-d}(s_y/s_z)^p e^{-a d(y,z)}.
\]
Integration over an intermediate top uses \(s_z^d\); scale powers
telescope in a product. Split each exponential into equal rates.
The triangle inequality puts one half on the endpoint distance;
successive summation of the other halves uses (3.13) at \(p=0\).
The kernel of an \(n\)-fold product is bounded by
\[
 b^nS(a/2)^{n-1}s_z^{-d}(s_y/s_z)^p e^{-a d(y,z)/2}.
\]
For \(bS(a/2)<1\) its Neumann series converges absolutely.
Different fixed scale powers are absorbed by reserving a further
fraction of the rate and using (3.12). This proves the convolution
mechanism for the derivative of the straightening map; it does
not construct the flat Green functions.

### 3.8 Checking the gauge theorem's proof and its dependency

Credit: Balaban, CMP 99, 75–102, (1.55)–(1.64),
(1.65)–(1.125), and (1.128)–(1.138). This subsection rebuilds
the gauge argument **conditional on the scalar and vector inverse
bounds in Section 3.9**. It is not an unconditional promotion of
G99.2 or a theorem for a different average.

The three scalar operators actually used are
\[
 G'=(D^*D+Q'^*aQ')^{-1},\quad
 R=1-G'Q'^*(Q'G'^2Q'^*)^{-1}Q'G',\quad
 H'=G'^2Q'^*(Q'G'^2Q'^*)^{-1}.                            \tag{3.14}
\]
They must satisfy \(Q'H'=1,\ Q'G'R=0\), and
\[
 \|G'Rf\|_Z\le C|f|_{-2},\quad
 \|H'X\|_Z+|D^*DH'X|_{-2}\le C\|X\|_\infty,\quad
 |Rf|_{-2}\le C|f|_{-2},                                 \tag{3.15}
\]
where \(\|\lambda\|_Z=\max\{\sup|\lambda|,\sup s|D\lambda|\}\).
These are the bounds used in (1.91)–(1.98), obtained there from
CMP 99, 389–434, Theorems 3.1–3.2.

First the reconstruction estimate (3.10) gives all truncations
of the pair a common mismatch bound. At a fixed link in layer \(j\),
successive curvature errors below that layer have sizes at most
\(C\alpha_0L^{2(n-j)}\), whose sum is bounded independently of
\(j\). The coarse mismatch enters with coefficient 1 at each
descent. The seam correction (1.31) is read at its outer endpoint's
double block; its factor is bounded by \(2dL\). The correction
is not applied once per finer level: those levels lie under that
same double block and use the interior reconstruction formula.
This gives (1.65)–(1.66) in Balaban's conventions.

Suppose the previous truncation supplies \(u_1\), with
\(U_1=e^{i\eta A}\). On adding the last layer its value and
first-difference bounds worsen by at most \(L^2\). The ascent
formula for \(u_1\) is a product of one-step block factors.
A factor at intermediate scale \(t\) differs from 1 by at most
\(Ct\sup|A|\); its covariant difference has the analogous bound
with \(\nabla A\). Summing the geometric scale series proves
(1.70), (1.73), (1.74), uniformly in depth.

Write the corrective gauge \(u'=e^{i\lambda'}\). Its normalization
is \(\mathcal Q'(u_1,\lambda')=0\). CMP 98 (184)–(214) gives
\(\mathcal Q'=Q'\lambda'+C'(u_1,\lambda')\), where
\[
 |C'(u_1,\lambda')|\le
 C(\alpha_3+\|\lambda'\|_Z)\|\lambda'\|_Z.                 \tag{3.16}
\]
Here \(\alpha_3\) bounds the ascent factors of \(u_1\).
The calculation is as follows. Expand
\(\log(e^{-i\lambda(x)}e^{i\operatorname{Ad}(U_0(x,x'))
\lambda(x')})\); its linear term is \(i\eta D\lambda\).
The endpoint contour sums telescope. Every remaining term contains
\(\lambda D\lambda\), the mismatch of an ascent factor, or the
reference curvature. Terms linear in \(\lambda\), including
their curvature dependence, belong to the exact \(Q'\lambda\)
and are subtracted. The remaining bounds at level \(n\) are
\(C(\alpha_3+\alpha_4)\alpha_4t_n\) and
\(C\alpha_0\alpha_4^2t_n^2\). Their geometric sums give (3.16).
Analyticity follows from the same
logarithm series as in Section 3.5.

Straighten the normalization by
\[
 \lambda'=\lambda-H'D'(\lambda),\qquad
 D'(\lambda)=C'(u_1,\lambda-H'D'(\lambda)).                \tag{3.17}
\]
On a small \(Z\)-ball, (3.15)–(3.16) and Cauchy's formula
bound this fixed-point map's Lipschitz constant by
\(C(\alpha_3+\alpha_4)\). Its image is bounded by
\(C(\alpha_3+\alpha_4)\alpha_4\). Choose the radii so that
the constant is below \(1/2\). Iteration gives a unique
analytic \(D'\); the inverse change is the same contraction
with \(\lambda=\lambda'+H'X\). The normalization has become
exactly \(Q'\lambda=0\).

The logarithm of a gauge-transformed link and the discrete product
rule give (1.88): its divergence is a sum of
\(e^{-i\operatorname{ad}\lambda'}D^*A\),
\(g(i\operatorname{ad}\lambda')D^*D\lambda'\), and an error
\(g_3\) bounded by \(C|D\lambda'||A|\).
Here \(g(0)=1\) and \(|g(z)-1|\le C|z|\); the sign of the
second term follows the convention for \(D\).
On \(Q'\lambda=0\), \(RD^*D\lambda=D^*D\lambda\).
Invert \(1+R(g-1)R\) by its Neumann series. In Balaban's
sign convention the resulting equation is (1.100),
\[
 \lambda=G'RD^*A+G'Rg_4(\lambda,D\lambda,A,D^*A),\qquad
 |g_4|_{-2}\le C\alpha_4B_1(\alpha_0+\alpha_1).            \tag{3.18}
\]
The terms in \(g_4\) come from \(g-1,g_3,H'D'\); each has
the indicated small factor. Cauchy's formula on a ball twice
as large bounds the Lipschitz constant of the nonlinear term
by \(CB_1(\alpha_0+\alpha_1)\). Choose a fixed uniqueness
radius first, and then the smaller invariant ball of radius
\(CB_1(\alpha_0+\alpha_1)\). This proves existence,
uniqueness and the preliminary estimate
\(C(L)B_1(\alpha_0+\alpha_1)\).

The a priori reset, CMP 99 (1.55)–(1.64), is necessary.
Let \(\alpha_2\) be that preliminary value bound. The two
current bounds and (3.11) estimate \(D^*DA\). The constraint
is \(qA=B-C(A)\). With \(RD^*A=0\), applying the vector
inverse \(G_0=(D^*D+DRD^*+Q^*aQ)^{-1}\) gives
\[
 \|A\|_X\le C\{\alpha_0+\alpha_1+
                    \alpha_2\|A\|_X+\alpha_2^2\}.        \tag{3.19}
\]
Using the Wilson Hessian in \(G_0\) adds and subtracts a
curvature term of size \(C\alpha_0\alpha_2\), with the
same consequence. Choose \(C\alpha_2<1/2\), absorb the third
term, and take the data small enough that
\(C[C(L)B_1(\alpha_0+\alpha_1)]^2\le\alpha_0+\alpha_1\).
Fix \(B_1\) to dominate the resulting inverse constant once.
The new bound is \(B_1(\alpha_0+\alpha_1)\), independent of
the preliminary loss. Equation (3.11) then bounds \(D^*DA\).
The covariant Weitzenbock identity and the bound for \(DPD^*\),
\(P=1-R\), give the Laplacian bound; the Hölder inverse gives
the Hölder bound. This is the first reset in the layer induction.

For uniqueness, two normalized gauges taking the same axial
representative to the small slice differ by a gauge in the
fixed ball of (3.18), by the ascent bounds. With the first
slice field as input, both the identity and that relative
gauge solve the same correction equation. Contraction makes
them equal. Thus the chart covers all regular competitors.

For the inhomogeneous slice \(RD^*A=f\), the linear forcing
in (3.18) acquires \(-G'f\). The same contraction works for
small \(|f|_{-2}\), and proves the transversality needed in
CMP 102 (123)–(126). It does **not** prove second-order
potential bounds from \(|f|_{-2}\) alone. CMP 99 Theorem 8,
p. 101, asserts these stronger bounds without a bound on
\(Df\); the outline flags this at line 7763. They are not
used here: only the finite-dimensional open thickening of
the slice is required.

Proposition 6's local gauge needs no critical background.
Around its cube choose successively larger cubes with gaps
\(R_1M_1s_n\); total enlargement is at most
\(R_1M_1s_j/(1-L^{-1})\). Fix coordinate-tree gauge for the
top average. Plaquette telescoping gives links bounded by
\(CM\alpha_0\). Descend (3.10) to bound all finer averages
by the same quantity. Extend by 1 outside a further enlarged
cube. Every plaquette read by the new nested domains lies
in the unchanged region; the artificial jump is not assigned
a regularity estimate. Apply the gauge theorem to this field
with reference 1. Its inverse inputs are the flat ones, so
this invocation does not assume the curved result being proved.
It gives the local value, derivative and Laplacian bounds
\(CM\alpha_0\) when \(M\alpha_0\) is small, exactly as in
(1.128)–(1.138). Combined with (3.11), this accounts for
both uses of G99.F.

### 3.9 What the background-propagator paper proves from its flat inputs

Credit: Balaban, CMP 99, 389–434, especially pp. 393–399,
408–416, 419–426. The scan fixes three important OCR ambiguities:
(3.48) has the kernel factor \(s_y^{-4}s_z^{-d}\), (3.132)
has \(s_y^{-2}s_z^{-d}\), and Theorems 3.12–3.13 explicitly
**exclude** the covariant-Laplacian estimate for the corrected
propagators. The excluded estimate cannot be used in Proposition 7
of CMP 102; Section 5 supplies its replacement.

**Remaining flat input, F0 (cited-pending).** On Balaban's separated
domain class, with his row and boundary conventions, at \(U=1\),
the positive inverses
\[
 G'_{\rm f}=(d^*d+Q'^*aQ')^{-1},\quad
 C'_{\rm f}=(Q'G_{\rm f}'^{\,2}Q'^*)^{-1},\quad
 G_{\rm f}=(d^*d+dR_{\rm f}d^*+Q^*aQ)^{-1}
\]
have the following estimates, also on the localized sequences used
in the proof. If \(f\) is supported in the pillar of \(z\), the
norms of \(G_{\rm f}f,\nabla G_{\rm f}f,\Delta G_{\rm f}f,
G_{\rm f}d^*f\) on the pillar of \(y\) are bounded by
\[
 C(s_y^2,s_y,1,s_y)e^{-a d(y,z)}\|f\|_\infty.             \tag{3.21}
\]
The scalar inverse has the corresponding estimates. For a
two-sided first derivative, the input is a local Hölder norm:
\[
 |\nabla G_{\rm f}d^*f|_y
 \le C_\epsilon e^{-a d(y,z)}
       (\|f\|_\infty+s_z^\epsilon[f]_\epsilon),\quad
             0<\epsilon<1.                              \tag{3.22}
\]
The Hölder-\(\beta\) output has the additional factor
\(s_y^{-\beta}\) and needs Hölder-\((\beta+\epsilon)\)
input, with \(\beta+\epsilon<1\). For the one-sided
gradient the bound is
\([\,\nabla G_{\rm f}f\,]_{\beta,y}
\le C_\beta s_y^{1-\beta}e^{-ad(y,z)}\|f\|_\infty\),
with the same scalar assertion.
The precise energy input used in the perturbation argument is
\[
 \langle A,T_{\rm f}A\rangle
   \ge c(\|\nabla A\|_2^2+\|s^{-1}A\|_2^2),\qquad
 \langle\lambda,T'_{\rm f}\lambda\rangle
   \ge c(\|d\lambda\|_2^2+\|s^{-1}\lambda\|_2^2).
\]
Here \(T_{\rm f}=G_{\rm f}^{-1}\), \(T'_{\rm f}=G_{\rm f}'^{-1}\);
all norms use the physical cell volumes and the stipulated
Dirichlet extensions. The coarse Gram forms obey
\[
 c\|s\psi\|_2^2\le\langle\psi,QG_{\rm f}Q^*\psi\rangle
                        \le C\|s\psi\|_2^2,\qquad
 c\|s^2\chi\|_2^2
 \le\langle\chi,Q'G_{\rm f}'^{\,2}Q'^*\chi\rangle
                        \le C\|s^2\chi\|_2^2.
\]
These are included in F0, not inferred merely from
finite-dimensional invertibility. Finally
\[
 |C'_{\rm f}(y,z)|\le Cs_y^{-4}s_z^{-d}e^{-a d(y,z)},\qquad
 |(QG_{\rm f}Q^*)^{-1}(y,z)|
       \le Cs_y^{-2}s_z^{-d}e^{-a d(y,z)}.                \tag{3.23}
\]
These are the flat specializations of (3.42)–(3.48),
(3.132), not claims that an \(L^\infty\) second-gradient
estimate holds on arbitrary bounded forces. CMP 99 derives
them from CMP 95 and 96; those texts are not among the supplied
files. The library energy estimates in Section 3.4 do not give
(3.21)–(3.23). Section 3.7 retires the cited summation lemma,
but not F0.

Here is the remaining reduction, so that F0 is not concealed
behind a citation to all of CMP 99. In a small local gauge
\(U=e^{i\eta A}\), \(|A|\le CM\alpha_0/s\) and
\(|\nabla A|\le CM\alpha_0/s^2\). For every oriented link
\[
 D_U-d=s^{-1}E,\quad |E|\le CM\alpha_0.
\]
Expanding \(D_U^*D_U-d^*d\) gives a first-order term with
coefficient \(CM\alpha_0/s\), and a zero-order term with
coefficient \(CM\alpha_0/s^2\). The latter follows by
differentiating \(A\) once, not by a bare \(\eta^{-1}\)
bound on a transport. Section 3.5 bounds the change in the
row operators and their transposes by \(CM\alpha_0\) in
their scaled row and column norms. Therefore the difference
of the inverse operators, composed with the flat inverse,
has norm at most \(CM\alpha_0\) in the value/gradient norms.
Its series is
\[
 (T_{\rm f}+E)^{-1}
       =T_{\rm f}^{-1}\sum_{n\ge0}(-ET_{\rm f}^{-1})^n.   \tag{3.24}
\]
Terms with a derivative on each side use (3.22). Taking
fixed \(\epsilon,\beta>0\) with \(\beta+\epsilon<1\)
closes those compositions; it is not legitimate to use the
false endpoint \(\epsilon=0\). Formula (3.13) sums the
off-diagonal factors. This proves the small-local-gauge
step, CMP 99 Corollaries 3.5–3.6, conditional on F0.

For a general regular field, cover by the paper's two-layer
cubes and take a partition \(\sum h_\nu^2=1\) with
\(|\nabla h_\nu|\le C/(Ms)\) and
\(|\Delta h_\nu|\le C/(M^2s^2)\).
Let \(G'_\nu\) denote the local inverse supplied by (3.24).
For the scalar operator \(T'\), the product rule gives
\[
 T'\sum_\nu h_\nu G'_\nu h_\nu=1-E',\qquad
 \|E'\|\le C/M.                                         \tag{3.25}
\]
The commutator is a gradient of \(h_\nu\) times a first
derivative of \(G'_\nu\), plus its Laplacian times \(G'_\nu\).
The nonlocal mass term has the same bound because a row is
supported on one double block and
\(|h_\nu(x)-h_\nu(y)|\le C/M\) there. Enlargements give
bounded overlap; (3.13) handles separated pillars.
Choose \(M\) first so that \(CS(a/2)/M<1/4\).
Then (3.25) and its geometric inverse give the scalar bounds.

For \(C'=(Q'G'^2Q'^*)^{-1}\), form
\(C'_0=\sum h_\nu C'_\nu h_\nu\). Multiplication by
\(Q'G'^2Q'^*\) leaves three errors: a term outside the
local cube, the difference \(G'^2-G_\nu'^2\) inside it,
and a commutator with \(h_\nu\). This is (3.95).
The first term has distance at least \(M\), hence
\(Ce^{-aM}\). In the second, expand both inverses by
(3.25). Walks entirely inside their common enlarged cube
cancel term by term; every remaining product reaches the
changed boundary and has the same exponential gain.
The third term contains a cutoff difference and is \(C/M\).
Splitting rates and summing (3.13) bounds all three by
\(C/M+Ce^{-aM}\). A second Neumann series proves (3.48).
Formula (3.14) now proves the bounds for \(P=1-R\),
including \(DPD^*\), because each differentiation falls
on one of the two scalar inverses. These are (3.49).

For the vector inverse, write
\(DRD^*=DD^*-DPD^*\). The first part is local.
The commutator with the second part has kernel
\((h_\nu(x)-h_\nu(x'))DPD^*(x,x')\), hence is \(C/M\)
after (3.13). The mass term has exactly the two errors
\(-S^*aQ+Q^*aS\), where
\[
 (Sf)(c)=\sum_b Q(c,b)(h_\nu(b)-h_\nu(c_-))f(b).
\]
These are CMP 99 (3.102)–(3.104).
The remaining difference between \(P\) and its local
version is estimated by the common-walk cancellation just
used for \(C'\). Its term with no cutoff derivative and
no path reaching the changed boundary equals the local
\(DP_\nu D^*\) term and cancels it; this is the cancellation
on p. 415. Every other term has \(C/M\) or \(Ce^{-aM}\).
Thus (3.25) holds for the vector operator as well.
This accounts for the nonlocal gauge projection, rather than
treating it as a local mass.

The same three-error construction proves the bound for
\((QGQ^*)^{-1}\), starting with its flat lower bound and
local inverses in F0. This is the argument referred to but
not repeated at CMP 99 p. 422, before (3.132).
Positive definiteness is retained by the small form
perturbation in (3.24), and by applying the partition
identity to the quadratic form with the same absorbable
commutator error. All choices precede the depth and volume.

This checks how the paper passes from flat inverses to
curved ones **on its geometric and boundary conventions**.
Its cover on p. 408 is a cover of the whole torus, explicitly
using \(T\setminus\Omega_1\) in its outer layer. Replacing
that construction by a cover of the outline's arbitrary
first member, with only inner-plaquette regularity, requires
a boundary argument; (3.25) alone does not provide it.
This separate transport requirement is retained in Section 7.

Here is the algebra for the last two inverse operators,
which can be checked without Gaussian integration. Put
\(S=1-DG'RD^*\). The identities \(Q'G'R=0\) and
\(D^*DG'R=R\) show \(RD^*S=0\); \(S\) is the identity
on that slice. The gauge-invariant extension of the
Wilson quadratic form is
\[
 \Delta_\pi=S^*\Delta S.
\]
Gauge invariance of the full action implies \(D^*J=0\).
Its second derivative along a gauge curve expresses
\(\Delta_\pi-\Delta\) as a bilinear form containing \(J\)
and at most one derivative on each test field, exactly
(3.117)–(3.120). The current bound therefore makes it
a small form perturbation in the norms of (3.21)–(3.22).

Straightening the nonlinear constraint introduces the
quadratic form
\[
 \langle A,W A\rangle=2\langle HC^{(2)}(A),J\rangle.
                                                               \tag{3.26}
\]
It is essential: omitting it changes the constrained Hessian.
By the derivative estimate in Section 3.5 and the bound for
\(H^*J\), its local operator bound is
\(|WA|_y\le C\alpha_0s_y^{-2}\sup_{D(y)}|A|\), with
the paper's \(M\) factor if its radius is \(M\alpha_0\).
Extending it by \(S^*WS\) gives the corrected form \(K_1\).
Adding the gauge and row masses gives an invertible operator
\(\widehat K_1=K_1+DRD^*+Q^*aQ\), with inverse \(G_1\).
The small-form series (3.24) proves the first-order and
Hölder bounds; no Laplacian bound is asserted here.

Minimizing a positive quadratic form subject to \(QA=B\)
and \(RD^*A=0\) gives the Lagrange equations, hence
\[
 H_1=G_1Q^*(QG_1Q^*)^{-1},\quad
 \Pi=1-H_1Q-G_1DRD^*,\quad
 \mathfrak G_1=\Pi G_1
  =G_1-G_1Q^*(QG_1Q^*)^{-1}QG_1-G_1DRD^*G_1.           \tag{3.27}
\]
For dimensionless data multiply \(H_1\) on the right by
\(s^{-1}\), as in Section 3.3. To verify the gauge terms,
for \(\lambda\in\ker Q'\) the extended form kills \(D\lambda\)
and \(QD\lambda=0\). The equation for
\(G_1D Rf\) therefore has the unique solution \(DG'Rf\).
It follows that \(RD^*G_1Q^*=0\) and
\(RD^*G_1DR=R\). These identities prove
\(Q\Pi=RD^*\Pi=0\), \(\Pi^2=\Pi\), and
\(\Pi^*\widehat K_1=\widehat K_1\Pi\).
They prove every constraint identity in (3.5).
Combining (3.21)–(3.23), the row bounds and (3.13) proves
its two operator estimates. In particular the fibre inverse
has **both** subtractions in (3.27); subtracting the row
part alone does not impose Landau gauge.

## 4. Propositions 2–6: the common chart and its critical equation

This section is Balaban's CMP 102 Sections A–E, reconstructed
with the inputs and qualifications in Section 3. Until Section 7,
the averaging and boundary conventions are his. F0 is a premise.

Take a reference \(U_0\) with regularity
\(C_1B_3\varepsilon_1\) and average mismatch
\(C_1\varepsilon_1\). Section 3.8 puts every competitor at
regularity \(\varepsilon_0\) in the same slice, with reduced
datum \(|B|\le2dLC_1\varepsilon_1\) and
\(\|A\|_X\le B_1(\varepsilon_0+C_1\varepsilon_1)\).
The seam factor in (1.31) is included in \(B\).
This is Proposition 2; it is a coverage statement.

**Straightening (Proposition 3).** Write
\(\mathcal Q(A)=qA+C(A)\), with \(qH=1,RD^*H=0\).
Define \(\mathcal D\) and \(T\) by
\[
 \mathcal D(A')=C(A'-H\mathcal D(A')),\qquad
 T(A')=A'-H\mathcal D(A').                               \tag{4.1}
\]
On \(|A'|_{-1}\le r\), use the ball
\(|X|\le r/B_0\) for the right-hand fixed-point equation.
Its argument has value norm at most \(2r\); its image is
at most \(4C_2r^2\). Choose \(4C_2B_0r\le1\).
Cauchy's formula on the larger value ball bounds its
Lipschitz constant by \(9C_2B_0r\). Choose this at most
\(1/2\), and \(3r\) within Section 3.5's analytic radius.
Successive differences are bounded by a geometric series,
so iteration converges, uniquely and holomorphically.
Substituting back gives \(|\mathcal D(A')|\le4C_2r^2\).

Now \(qT+C(T)=qA'\) and \(RD^*T=RD^*A'\), exactly.
For a small \(A\), the inverse is explicitly
\(A'=A+HC(A)\): then \(C(A)\) solves the equation for
\(\mathcal D(A')\), and uniqueness identifies it.
The same estimates bound the first derivative of \(T(A')\)
in space by \(r+4B_0C_2r^2\). They show its range contains
a smaller \(X\)-ball, rather than just a value ball.

Differentiating (4.1) gives
\[
 D\mathcal D=(1+DC(T)H)^{-1}DC(T).                       \tag{4.2}
\]
The double-block derivative bound of Section 3.5 and the
kernel bound for \(H\) bound \(DC(T)H\) by \(Cr\) in
the exponential-kernel norm. Section 3.7 sums its Neumann
series. Thus \(D\mathcal D\) has the same exponential
localization and a factor \(r\); subtracting its linear
Taylor term gives a factor \(r^2\), by Cauchy's formula.
This is the actual content of CMP 102 (69)–(73).

**The nonlinear force (Proposition 4).** The plaquette expansion
of the Wilson action at \(U_0\) is
\[
 F(A)=F(0)+\langle A,J\rangle
       +\tfrac12\langle A,\Delta_\pi A\rangle+V_0(A)
       \quad(RD^*A=0).
\]
The only cubic part with a derivative, after transporting
all insertions to one corner, is a fixed multiple of
\(\langle DA,\sum_{b_1<b_2}i[A(b_1),A(b_2)]\rangle\).
The other terms are bounded locally by
\[
 C\big(|A|^4+\eta\,|F(U_0)|\,|A|^3\big),
 \qquad F(U_0)=\eta^{-2}(\partial U_0-1).
\]
These assertions follow by multiplying four exponential
series. Terms of degree four and higher are bounded by
the exponential remainder
\(\sum_{n\ge4}z^n/n!\le z^4e^z/4!\).
The cubic commutator is obtained by cyclicity of trace:
the symmetric products cancel and the antisymmetric
products pair with the linear curl. This is CMP 102
(25)–(40). Its differentiated curl term is treated by
the product rule in (3.11), not by a factor \(\eta^{-1}\).

Insert \(A=T(A')\). Since
\(\mathcal D^{(2)}=C^{(2)}\), the quadratic term is
\(\tfrac12\langle A',\Delta_1A'\rangle\), where
\[
 \Delta_1=\Delta_\pi-W,\qquad
 \langle A',WA'\rangle=2\langle HC^{(2)}(A'),J\rangle .
\]
The remaining functional is exactly
\[
 V(A')=-\langle H\mathcal D_{\ge3}(A'),J\rangle
 -\langle A',\Delta_\pi H\mathcal D(A')\rangle
 +\tfrac12\langle H\mathcal D(A'),
                       \Delta_\pi H\mathcal D(A')\rangle
 +V_0(T(A')).                                           \tag{4.3}
\]
Its force satisfies
\[
 |V'(A')|_{-3}\le C_4\|A'\|_X^2.                        \tag{4.4}
\]
To verify all four terms: (4.2) after its linear term
is removed makes the first \(O(|J|_{-3}r^2)\).
For the second, the minimizing identity
\(\Delta_\pi H=Q^*(QGQ^*)^{-1}s^{-1}
-Q^*a s^{-1}\) moves the apparent second derivative
onto row operators; (3.23), the row derivative and
(3.13) make its two differentiated terms \(O(r^2)\).
The third has one \(D\mathcal D=O(r)\) and one
\(\mathcal D=O(r^2)\), hence is \(O(r^3)\) by the
same identity. The fourth has terms \(A\nabla A\),
\(A^3\), and \(\eta F(U_0)A^2\), all \(O(r^2)s^{-3}\);
composition with \(T\) adds (4.2), whose kernel is summable.
This accounts for CMP 102 (85), (88), (89), (90), (93)
separately. It also proves holomorphy of the force on
the fixed \(X\)-ball. No volume factor appears, because
the bounds are for the force at a bond.

**Critical equation (Propositions 5–6).** Put
\(A'=A_1+H_1B\). The tangent space is
\(\ker q\cap\ker RD^*\), and \(H_1B\) is orthogonal
to it for \(\Delta_1\). Therefore stationarity is
equivalent, using (3.27), to
\[
 A_1=-\mathfrak G_1J-\mathfrak G_1V'(A_1+H_1B).          \tag{4.5}
\]
Every solution automatically has \(qA_1=RD^*A_1=0\).
Conversely applying the constrained quadratic operator
to (4.5) gives the tangent Euler equation. Thus no
stationary solutions have been discarded.

Write \(h=B_0|B|\), \(j=B_0|J|_{-3}\).
On \(\|A_1\|_X\le r\), the map in (4.5) has norm
at most \(j+B_0C_4(r+h)^2\). For two inputs, Cauchy's
formula on a ball of radius \(r+h\) about their segment
gives Lipschitz constant \(4B_0C_4(r+h)\).
Choose a fixed \(r_*>0\) such that
\(4(r_*+h)\) is within the force's analytic radius and
\(4B_0C_4(r_*+h)\le1/2\), then take \(j,h\) small.
This gives uniqueness in a fixed ball.
For the linear bound take the smaller ball
\(r=2j+2h\). The inequality
\(B_0C_4(r+h)^2\le j+2h\) holds when \(j+h\)
is below a fixed threshold. The map preserves that
ball and is a contraction there. Its solution satisfies
\(\|A_1\|_X\le C(|J|_{-3}+|B|)\).

Combining it with \(T\) gives a unique slice critical
point with \(\|A\|_X\le CC_1B_3\varepsilon_1\).
The larger uniqueness ball was fixed before the smaller
existence ball; one cannot prove uniqueness of all regular
orbits just by working on the latter.

## 5. Proposition 7: recover second derivatives before regularity

Credit: Balaban, CMP 102, pp. 296–300, (123)–(143).
This section is still conditional on F0 in Balaban's
domain convention.

Section 3.8's inhomogeneous gauge theorem thickens the
slice to \(RD^*A=f\), preserving its nonlinear row datum.
The action is constant along the corresponding gauge
pieces. A critical point on the slice is therefore
critical on this thickened constraint manifold.
The gauge variable is now free in an open set, so its
Euler variations are all \(\delta A'\) with \(q\delta A'=0\).
This is the reason a second equation is available.

Let \(G_0=(\Delta+DRD^*+Q^*aQ)^{-1}\) use the
**unextended** Wilson Hessian \(\Delta\). Define
\[
 H_0=G_0Q^*(QG_0Q^*)^{-1}s^{-1},\qquad
 P_0=1-G_0Q^*(QG_0Q^*)^{-1}Q,\qquad A'=A_0+H_0B.
\]
Then \(qA_0=0\), and differentiation of the thickened
functional gives
\[
 (\Delta+DRD^*)A_0
    =-P_0^*J+P_0^*W A'-P_0^*\widetilde V'(A').           \tag{5.1}
\]
Here \(\widetilde V\) uses the unextended Hessian in (4.3);
the same term-by-term force bound (4.4) holds. The right
side has norm at most \(CC_1B_3\varepsilon_1\) in
\(|\cdot|_{-3}\): \(W\) is curvature/current-small by
(3.26), and the row projection is bounded by (3.23).
The unextended inverse has the Laplacian estimate (3.21),
so \(|\Delta_{U_0}H_0B|_{-3}\le C|B|\).

For \(A_0\), write \(\Delta=D^*D+\Delta'\) and
\(DRD^*=DD^*-DPD^*\). Expanding the two finite
differences gives
\[
 D^*D+DD^*=\Delta_{U_0}+\mathcal F,\qquad
 |\mathcal F A_0|_y\le C\alpha_0s_y^{-2}
                                     \sup_{D(y)}|A_0|.
                                                               \tag{5.2}
\]
The extra terms are commutators of two covariant
translations. Each is an adjoint plaquette minus identity,
divided by \(\eta^2\), which proves the bound in (5.2).
The term \(\Delta'\) has the same curvature bound.
The term \(DPD^*A_0\) has norm \(C\|A_0\|_X\) in
\(|\cdot|_{-3}\), by (3.49) and (3.13).
Thus (5.1)–(5.2) give
\[
 |\Delta_{U_0}A'|_{-3}\le CC_1B_3\varepsilon_1.           \tag{5.3}
\]

It remains to undo straightening: \(A=A'-H\mathcal D(A')\).
The minimizing identity for \(H\), used after (4.3),
gives \(|\Delta_\pi HB|_{-3}\le C|B|\).
Since \(RD^*H=0\), polarizing
\(\Delta_\pi=S^*\Delta S\) leaves, in
\(\langle X,(\Delta_\pi-\Delta)HB\rangle\), only terms
containing \(G'RD^*X\), \(HB\), and \(J\). Their
summation by parts is CMP 102 (138), and gives
\[
 |(\Delta_\pi-\Delta)HB|_{-3}\le C\alpha_0|B|.
\]
Subtract \(\Delta'HB\) to bound \(D^*DHB\).
Use (5.2) and \(RD^*HB=0\) to bound its componentwise
Laplacian. Consequently
\[
 |D^*D H\mathcal D(A')|_{-3}
 +|\Delta_{U_0}H\mathcal D(A')|_{-3}
       \le C|\mathcal D(A')|\le C\|A'\|_X^2.             \tag{5.4}
\]
Equations (5.3)–(5.4) and (3.11) prove that the constructed
configuration is regular at \(CC_1B_3\varepsilon_1\).
Using (4.5) alone for this conclusion would be unjustified.

To make the current step explicit, \(A'\) itself satisfies
\(RD^*A'=0\), because both the original potential and the
straightening correction \(H\mathcal D\) do. Hence (5.2)
gives \(D^*DA'=\Delta_{U_0}A'+\mathcal F A'-DPD^*A'\).
Each term on the right has the required force bound.
Equation (5.4) transfers it from \(A'\) to \(A\), so the
linear current term in (3.11) is controlled as well.

At the constructed critical point, repeat the expansion
with that point as reference. Now \(B=0\) and the linear
term vanishes on the tangent fibre. Its quadratic term
is positive there, and the remainder is cubic. In the
finite-dimensional fibre this proves a strict local
minimum, after residual gauge directions are removed.
No assertion about rough global minima is needed for A1.

## 6. Proposition 8: the reset and the induction it actually closes

Credit: Balaban, CMP 102, Section F, pp. 300–305.
This section proves the reset from the inputs already stated.
It separates that reset from the construction of admissible
inductive data.

Let \(U\) be any constrained critical point with regularity
\(\varepsilon_0\), sufficiently small. Around a chosen bond
or plaquette of layer \(j\), rescale \(s_j=1\). Choose the
two-layer cube and nested enlargements in (144).
Section 3.8 gives a gauge in which
\(U=e^{i\eta A}\) and \(\|A\|_X\le CM\varepsilon_0\).
The local reference is now 1. The auxiliary datum is the
actual average of \(U\) on its artificial boundaries.
Any sufficiently small variation preserving this stronger
datum and supported in the local box preserves the original
datum, and its action variation is the same. This follows
by iterating locality of the original average, with the
new outer layer frozen. Thus the localized field is critical.
This uses neither its existence by a previous induction
nor its being a global minimum.

In this gauge its straightened datum satisfies two different
bounds. Globally, \(|B|\le CM\varepsilon_0\).
On the last two layers through the centre, the datum tests
and (3.10) give
\[
 |B(c)|\le (8d^2L^2+4L^2|c_--y|)\varepsilon_1.           \tag{6.1}
\]
The logarithm bound used to pass to (6.1) is valid because
\(M\varepsilon_0\) is small. The centre \(y\) is the
chosen unit pillar, or the centre of the larger cube in
the local-gauge conclusion. The remaining, artificial
datum lies at layer distance at least \(R_1M_1\).

In the flat reference, (4.5) and (4.1) read
\[
 A=A_1+HB-H\mathcal D(A_1+HB),\qquad
 A_1=-\mathfrak G V'(A_1+HB).                            \tag{6.2}
\]
There is no reference current and no current-induced
quadratic correction. Put
\[
 S_*=\sup_y\sum_z
 e^{-a d(y,z)/2}(1+d(y,z))(s_y/s_z).
\]
Section 3.7 proves \(S_*<\infty\), uniformly once the
separation exceeds its fixed lower bound. The kernel
bounds for \(H,\nabla H,D^*DH,\Delta H\), with (6.1)
on the near part and the coarse global bound on the
far part, give CMP 102 (161):
\[
 \max\{|HB|,|\nabla HB|,|d^*dHB|,|\Delta HB|\}_{\Delta}
 \le18d^3L^3B_0S_*M_\Delta
                \max\{\varepsilon_1,e^{-aR_1M_1/2}\varepsilon_0\}.
                                                               \tag{6.3}
\]
Here \(M_\Delta=1\) for the central unit pillar, and
\(M_\Delta=M\) for the larger cube. In the far sum
one reserves half the exponential to reach the artificial
boundary. Its remaining factor absorbs both the linear
distance growth in (6.1) and the scale ratio. This is
why counting nearby fine bonds without their coarse
kernel weights would give the wrong answer.

Set \(B_3=72d^3L^3B_0S_*\), or any larger fixed number.
Choose \(R_1M_1\) sufficiently large that
\(B_3e^{-aR_1M_1/2}\le1/2\). There is no circular
choice: \(S_*\) was bounded uniformly over every gap
above its previously fixed minimum.
The linear term in (6.2) is now at most
\[
 \tfrac14M_\Delta\max\{B_3\varepsilon_1,\varepsilon_0/2\}
                                                               \tag{6.4}
\]
in all four norms.

The nonlinear terms in (6.2) are bounded in the first
two norms by (4.1), (4.4) and the flat inverse. In the
second-order norms use (5.1)–(5.4) at reference 1.
Their common bound is \(C(M\varepsilon_0)^2\).
Writing \(M'=M/(R_1M_1)\), and making the harmless
enlargement of \(C\) that includes \(R_1M_1\), choose
\(a_5>0\) so that
\[
 M'\varepsilon_0\le a_5
 \quad\Longrightarrow\quad
 C(M\varepsilon_0)^2\le\tfrac18M'\varepsilon_0.            \tag{6.5}
\]
All logarithm, chart and contraction thresholds can be
included in this same finite choice.
The scan of p. 304 confirms that the coefficient in
(166)–(167) is \(1/8\), which is unclear in the OCR.

For the central pillar \(M'=M_\Delta=1\), combine
(6.4)–(6.5), and set
\(m=\max\{B_3\varepsilon_1,\varepsilon_0/2\}\).
Since \(\varepsilon_0\le2m\), all four potential norms
are at most \(m/2\). The plaquette and current expansion
(3.11), now at reference 1, bounds their regularity
by \(m/2+C m^2\). Decrease \(a_5\) so that this is at
most \(m\). Returning to the original real gauge changes
neither curvature nor current. The centre was arbitrary:
\[
 r(U)\le\varepsilon_0
 \quad\Longrightarrow\quad
 r(U)\le\max\{B_3\varepsilon_1,\varepsilon_0/2\}.           \tag{6.6}
\]

Apply (6.6) repeatedly to the same field and same datum.
All smallness assumptions improve at each application.
After \(n\) applications,
\[
 r(U)\le\max\{B_3\varepsilon_1,2^{-n}\varepsilon_0\}.
\]
Letting \(n\to\infty\) proves
\(r(U)\le B_3\varepsilon_1\), including the zero-datum
case. This is an ordinary real inequality argument,
not an infinite computation. For strict radii, first
apply it with slightly enlarged datum and field radii
inside their thresholds.

For the larger cube, first use the just-proved global
bound \(\varepsilon_0=B_3\varepsilon_1\), then (6.4)–(6.5).
It gives the four local bounds \(CM\varepsilon_1\)
for \(M'\varepsilon_1\le a_1\). Hölder estimates follow
from the corresponding first-derivative inverse estimates
on the enlarged cube; their constant depends on
\(\beta_0<1\). This recovers (9)–(10), with the allowed
size \(M(\varepsilon_1)=R_1M_1a_1/\varepsilon_1\).

**Where the depth disappears.** Suppose, in addition,
that the lower-depth datum required by CMP 102 (11)
has been constructed with its stated test bound. Apply
the depth-\((k-1)\) theorem to that datum. In the new
units the reference has radius at most
\(L^3B_3\varepsilon_1\): curvature loses \(L^2\),
current loses \(L^3\). Sections 4–5 produce radius
\(CC_1B_3\varepsilon_1\), with \(C_1=L^3\).
Equation (6.6) resets it to \(B_3\varepsilon_1\).
Thus the induction does not iterate \(CL^3\).

Choose constants in this order: the block size \(L\);
flat inverse constants and rates (F0); the summation
threshold; the local inverse constants; \(B_1,B_3\);
the localization length \(R_1M_1\); the fixed chart and
uniqueness radii; \(a_5\); then \(a_0,a_1\), small
enough for the finite list of inequalities above.
In particular require \(B_3a_1\le a_0\) and
\(CC_1B_3a_1\le a_5\). Depth, torus and datum are
quantified only after these choices.
This proves the **inductive implication** once the
lower-depth datum construction and the stated operator
inputs hold. The seam version of that datum construction
for the outline is examined next; it is not supplied
by the numerical factor \(L^3\).

## 7. Transport to the outline: what can and cannot yet be concluded

The target throughout this section is the actual map at outline
lines 7065–7115, credited to Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text. The contour
family has at most \(4!\) coordinate-ordered paths. Its contour
mean is the Federbush mean, while its bond average is the
exponential of the arithmetic mean of the closed-row logarithms.
These two means must not be interchanged.

### 7.1 The one-step change of averaging map is controlled

On one double block, two coordinate-ordered transports with
the same endpoints differ by swapping adjacent coordinate
runs. Each swap sweeps a rectangle with at most \(L^2\)
plaquettes; at most six swaps order four directions.
Telescoping the plaquette products bounds their difference
by \(6L^2\varpi\), with the harmless additional factor
for the lengths of a double-block path. This is valid in
an arbitrary real gauge.

For a family \(e^{Z_i}W_*\), the contour mean \(e^YW_*\)
satisfies
\[
 0=n^{-1}\sum_i\log(e^{Z_i}e^{-Y})
   =n^{-1}\sum_iZ_i-Y+R(Z,Y).
\]
On a fixed small ball the convergent product and logarithm
series give
\(|D_YR|\le C\max_i|Z_i|+C|Y|\), and bounded second
derivatives. The contraction proof in
the fixed-geometry note, Section 5.1, therefore has constants
independent of the number of paths: the normalized sum has
total weight 1. Its derivative at coincident transports is
their arithmetic mean. Every derivative of the actual
one-step average is thus obtained by differentiating finite
products, logarithms, and this bounded implicit inverse.

Subtract its two node-factor derivatives. At a flat reference,
the endpoint contour sums cancel exactly, leaving
the straight-segment average \(Q^{\rm s}\).
At curvature \(\varpi\), every failure of that cancellation
is a transport around one of the rectangles just counted,
or a derivative of a logarithm/mean away from its coincident
value. Its coefficient is \(C(L)\varpi\).
Since each derivative reads only the double block, there are
constants depending on \(L\), but not on the torus, such that
\[
 K_0=Q^{\rm s}_{U_0}+E,\quad
 |Ef|\le C(L)\varpi Q''|f|,\qquad
 |D\mathcal Q(A)-K_0|\le C(L)|A|\,Q'' .                 \tag{7.1}
\]
Here \(Q''\) is the positive double-block majorant, and
the scale is one fine step. To justify the entrywise
majorant, set all but one input component to zero in
the differentiated finite expression; every insertion
has a coefficient bounded by the displayed small quantity.
Divide by the positive weight of \(Q''\), at worst a
fixed power of \(L\). This changes \(C(L)\), not its
depth dependence. The same argument controls the transpose.

Accordingly the analytic iteration and derivative induction
of Section 3.5 apply to the actual straightened map,
with new one-step constants: the leading positive
straight average is identical, and all new terms carry
the small factor in (7.1). This proves the actual-map
analogues of P98.4–5 on a double block contained in one
layer or its adjacent finer layer. At a seam use the
finer layer's units, costing the fixed factor \(L^2\).
The one-step curvature proof in (3.6) also applies:
the mean's first derivative is arithmetic averaging,
so the four endpoint contour contributions cancel,
and the remainder is quadratic.

What this proves is a bound for each actual map and its
own derivative. It does not yet prove a bound for the
difference between the full iterated actual derivative
and Balaban's derivative at a *different sequence of
reference averages*. That distinction is addressed
explicitly in Section 7.4.

### 7.2 The seam descent can be reduced to a fixed-size inverse

Here is a concrete construction, rather than identifying
CMP 102 (11) with the outline's datum. Delete the last
region \(\Omega_k\), and work on the lattice of level
\(k-1\). The old exterior data there are fixed.
Inside a level-\(k\) block put the fine internal links
equal to 1. Between two such blocks put \(V_k(c)\)
on every crossing link of their common face.
For an outward coarse bond \(c=(y,z)\), \(z\) lies
in the finer region. On a crossing link ending at
\(x\in B(z)\), put
\[
                 W(b)=V_k(c)\,V_{k-1}(\Gamma_{z,x}),
                                                               \tag{7.2}
\]
with the inverse formula if its orientation is reversed.
The interior endpoint's block transport is 1.
All contours on the right of (7.2) lie in the fixed
outer block. Therefore this rule changes no prescribed
finer link: those crossing links were inward bonds of
the finer level, omitted by the target's convention.

Away from the new seam this is the exact lift of
the fixed-geometry note. Across the seam its coarse
average has error \(C(L)\varepsilon\): slide the
outer part of each averaging path to \(\Gamma_{z,x}\).
The discrepancy is a product of at most \(C L^2\)
outer plaquettes. The straight reference path has
coarse transport \(V_k(c)\), and the remaining
closed-row logarithms are \(O(L^2\varepsilon)\).
Taking their normalized mean proves the error bound.

The seed has fine plaquette error \(C(L)\varepsilon\)
in a collar of fixed coarse width. To check corners,
project each fine plaquette crossing block faces
onto its coarse plaquette. Its product is conjugate
to that coarse test, with the outer coarse edges
replaced by the averages of the fixed finer data,
times the local path-sliding errors just bounded.
This is also true with one or three outer blocks:
each missing coarse edge is replaced by its finer
average before cancellation. The number of replacements
is at most four. A plaquette contained within the old
finer region is unchanged. Away from the collar the
exact lift's nontrivial plaquettes are copies of the
old coarse plaquettes, so their bound incurs no new
factor.

For exact constraints use the middle pivot on the
face of each coarse bond. It occurs in no other
coarse row: endpoint contours stay inside blocks,
and straight segments in another direction do not
cross that face in the pivot direction. None of
these seam pivots is a fixed finer bond.
At a flat field exactly \(L\) of the \(L^4\)
straight segments contain this pivot, so its
derivative is \(L^{-3}\operatorname{Ad}(T_c)\).
The transport \(T_c\) is unitary. By (7.1) the
derivative at the seed is this invertible map
plus an error \(C(L)\varepsilon\).

Write the row equation for its pivot change \(x\)
as \(f_c(0)+D_cf_c\,x+N_c(x)=0\).
The second derivative is bounded by \(C(L)\) on
a fixed ball. If \(C(L)\varepsilon L^3<1/2\),
then \(\|(D_cf_c)^{-1}\|\le2L^3\).
The map
\[
 x\longmapsto-(D_cf_c)^{-1}\{f_c(0)+N_c(x)\}
\]
is a contraction on \(|x|\le C(L)\varepsilon\),
after choosing \(\varepsilon\) sufficiently small.
The equations are independent once the nonpivot
links are fixed. This proves an exact one-step
section with a factor \(C_\downarrow(L)\) confined
to the new seam collar. It uses the actual pivot
calculation of the outline, lines 8165–8285, with
the counting and inverse argument supplied here.

The construction alone does not justify repeatedly
replacing \(\varepsilon\) by \(C_\downarrow\varepsilon\).
A suitable induction class has tests at most
\(\varepsilon\) near each *remaining* seam and at
most \(C_\downarrow\varepsilon\) elsewhere.
New modifications are confined to the deleted
seam's collar. The gap, chosen larger than twice
that collar width, separates it from every remaining
seam. Subsequent descents lift this old collar in
the interior, where the lift is exact and does not
amplify its plaquette bound. Thus the same two
radii persist to the bottom. For such an induction
class the seed's loss is \(C_\downarrow\), not
\(C_\downarrow^k\).

This establishes the local section and the reason
for the two-radius bookkeeping. A global A1 proof
still needs the uniform inverse and chart on this
whole class; a one-step pivot inverse, whose size
is \(L^3\), cannot supply that inverse by iteration.

### 7.3 Frozen outer bonds remove one boundary issue for A1

This concerns the variational problem, not every
unconditioned propagator claimed in the outline.
If \(\Omega_1=\varnothing\), all fine bonds are
fixed and there is no existence problem. Otherwise
choose an auxiliary first member surrounding
\(\Omega_1\), with a collar wider than every
one-step double block and action stencil, and
contained with a further stencil margin in
\(\Omega_0\). Such a collar exists once the given
gap exceeds this fixed width. If \(\Omega_1=T\),
use \(T\) itself.

Every unfixed fine bond has an endpoint in
\(\Omega_1\). Every plaquette containing such
a bond, and every determining average that can
change, lies inside the auxiliary member.
Indeed a level-1 outward row reads at most its
two blocks, and a higher row's double block is
contained in the preceding region, hence in
\(\Omega_1\). Consequently variations with the
original constraints are precisely variations
of this smaller problem with the outer fine
bonds frozen. Action differences and constraint
differences agree exactly.

A reference field or competitor can be extended
arbitrarily beyond the original \(\Omega_0\).
Every plaquette touching the auxiliary member
is still an inner plaquette of \(\Omega_0\), so
the source's protruding-plaquette hypothesis holds
there. No estimate is assigned to the distant
extension jump. This reduces A1's outer boundary
to the auxiliary first member used on CMP 99
p. 394. It does not prove an estimate for the
original, unconditioned \(G\) at the original
outer boundary. That stronger statement is not
needed for this reduction.

### 7.4 What a comparison argument would have to prove

The needed comparison, after the two output row frames are
identified, is
\[
 \mathcal Q^{\rm st}(A)=\mathsf qA+\mathsf C(A),\qquad
 |\mathsf C(A)|\le C(\alpha_0+\|A\|_X)\|A\|_X,
                                                               \tag{7.3}
\]
\[
 \|D\mathsf C(A)\|_{X\to\ell^\infty}
 +\|D\mathsf C(A)^*\|_{\ell^\infty\to F}
 \le C(\alpha_0+\|A\|_X),\qquad F=(|\cdot|_{-3}),          \tag{7.4}
\]
where \(\mathsf q\) is the dimensionless Balaban row
at the same fine reference. Corresponding site-average
estimates are needed for the gauge normalization.
Forces and coarse dual variables in (7.4) use the
pairings of Section 3; in four dimensions the
dimensionless row pairing has weight \(s^{d-4}=1\).

One cannot obtain these estimates merely by identifying
the two one-step derivatives: changing the mean also
changes the reference average at every later step.
Independently chosen local gauges would not automatically
agree at shared nodes.

The route below avoids that inference. Section 7.6 compares
each scheme's own recursion with its flat recursion in a
local regular gauge. Sections 7.7–7.10 build the operators
and the gauge chart directly for the actual map. Thus the
main proof never assumes a simultaneous alignment of the
two schemes' intermediate reference averages.

### 7.5 An alternative multiplier reduction, with its premise exposed

It is useful to finish the algebra to see exactly
what (7.3)–(7.4) would buy. This is an implication,
not the route used in Section 8.
Use the comb projection \(\mathsf R\), and write
\[
 K=\Delta^{\rm W}_{U_0}+D\mathsf R D^*+\mathsf q^*\mathsf q,
 \quad G=K^{-1},\quad
 H=G\mathsf q^*(\mathsf qG\mathsf q^*)^{-1},\quad
 \widetilde G=G-H\mathsf qG.
\]
Assume their uniform bounds have been transported
to the determining set under consideration.
Write \(F'(A)=J+\Delta^{\rm W}_{U_0}A+N(A)\),
where \(|N(A)|_{-3}\le C\|A\|_X^2\), by (3.11).
The penalized Euler equations and the actual
constraint are
\[
 F'(A)+D\mathsf R D^*A
       =(\mathsf q+D\mathsf C(A))^*\omega,\qquad
 \mathsf qA+\mathsf C(A)=b.                             \tag{7.7}
\]
Here \(b\) is the actual reduced datum, including
its triangular seam correction, not the plain
logarithm of the coarse mismatch.

Applying \(H^*\) to the first equation eliminates
the multiplier:
\[
 w(A)=[1+H^*D\mathsf C(A)^*]^{-1}
                     H^*(F'(A)+D\mathsf R D^*A).
                                                               \tag{7.8}
\]
The inverse exists under (7.4).
Summation by parts changes
\(H^*D^*DA\) into \((DH)^*DA\); thus only
first differences of \(A\) enter its estimate.
The kernel bounds and (3.13) give
\[
 |w(A)|\le C(|J|_{-3}+\|A\|_X),\qquad
 |w(A)-w(\widetilde A)|\le C\|A-\widetilde A\|_X .
\]
Substitution into (7.7) gives a fixed point in \(X\):
\[
 A=\widetilde G[-J-N(A)+D\mathsf C(A)^*w(A)]
                         +H[b-\mathsf C(A)].             \tag{7.9}
\]
Its Lipschitz constant is at most
\(C(\alpha_0+r+|J|_{-3})\) on \(\|A\|_X\le r\).
Each non-small derivative of \(w\) is multiplied
by the small \(D\mathsf C\).
Choose a fixed uniqueness radius and then the
smaller invariant radius \(C(|J|_{-3}+|b|)\),
as in Section 4. This proves a unique small
solution of the **penalized** equations.

One further input is indispensable. The actual
constraint-preserving gauge directions must map
surjectively, under \(A\mapsto\mathsf R D^*A\),
onto \(\operatorname{ran}\mathsf R\).
Pairing (7.7) with those directions then forces
\(\mathsf R D^*A=0\), because the action and
actual constraint are constant on their gauge
curves. This is the analogue of Section 3.8,
with the actual gauge averages. Its normalization
map has linear part \(Q'_{\rm actual}\), whereas
\(\mathsf R\) was built from \(Q'_{\rm Balaban}\).
Linear row comparison alone would not prove this
nonlinear assertion. Without it, (7.9) proves neither
criticality of the original constrained problem nor
coverage of every regular orbit. Sections 7.7–7.10
instead use the actual \(R\) and construct its chart;
no comb-normalization transport is assumed there.

Once that transversality holds, second derivatives
come directly from (7.7): its right side is bounded
in \(F\) by (7.4), and the slice condition and
(5.2) bound \(D^*DA,\Delta_{U_0}A\).
At a critical reference the derivative of (7.7)
contains
\(F''(0)-[D^2\mathcal Q^{\rm st}(0)]^*\omega_0\);
thus this multiplier method retains precisely
the current-induced Hessian correction (3.26).

At reference 1 the two straightened linear rows
coincide, so (7.3) has no linear error.
The local improvement argument of Section 6
then applies to the actual map if its local
slice and inverse have been supplied. Together
with Section 7.2's two-radius descent, this
would close the depth induction.

### 7.6 Direct row estimates avoid comparing reference averages

Credit: the useful direct recursion, and the distinction between
the fixed-leg column sum and the summed-leg row sum, are in the
Sussman–Alpoge outline, with Claude and Codex as authors of that
text, (PX141)–(PX154), lines 11507–11640. The following argument
checks those estimates. It improves the endpoint of Sections
7.4–7.5; it does not take a propagator bound from that outline.

Fix a row of length \(s=L^j\eta\), put \(n=L^j\), and enlarge
its double block by a fixed multiple of \(s\). First assume a
single real gauge on that enlargement satisfies
\[
 s|A_0|+s^2|\nabla A_0|\le C\alpha,\qquad
 U_0=e^{i\eta A_0},\qquad
 |\partial U_0-1|\le C\alpha(\eta/s)^2.                 \tag{7.10}
\]
This is a local hypothesis, not a choice of compatible gauges
on all row carriers. Section 3.8, Proposition 6, supplies it
from the source regularity conditions, conditional on F0;
at a seam the adjacent scale costs a fixed power of \(L\).
No current background constructed in A1 is used to obtain it.

In raw link coordinates at one step let \(F_W(a)\) be the
logarithm of the actual straightened mean in Section 7.1.
Products, the contour mean and logarithms are analytic on
\(\|\log W/i\|_\infty+\|a\|_\infty<c/L\). Every path has
at most \(CL\) links. Shrinking \(c\) makes their products
and the arguments of all logarithms stay in a fixed ball.
There the convergent logarithm series and the mean contraction
bound \(F\) by a constant.

Its derivative at \(W=1,a=0\) is the straight raw average
\(S_L\), of row norm \(L\) and column norm \(L^{-3}\).
Two Cauchy circles of radius a fixed multiple of \(L^{-1}\),
one in the reference and one in the increment, therefore give
\[
\begin{split}
 \|D_aF_W(a)-S_L\|_{\rm row}&\le C_L\delta L,\\
 \|D_aF_W(a)-S_L\|_{\rm col}&\le C_L\delta L^{-3},\\
 \sup_b\sum_{c,b'}|D_bD_{b'}F_W(a)(c)|&\le C_L,\qquad
 \delta=\|\log W/i\|_\infty+\|a\|_\infty .              \tag{7.11}
\end{split}
\]
For the column bound a fixed link enters at most a fixed
number of neighbouring one-step rows. Within one row the
supremum norm of each scalar output differential equals the
sum of the absolute values of its scalar coefficients.
Summing over the three color coordinates bounds the sum of
matrix norms by a fixed color factor. With one input fixed,
the same argument applies to the Hessian. The remaining
one-step counts and the division by \(L^{-3}\) cost only
powers of the fixed \(L\). These are estimates for the finite
formula, not estimates inferred from the dimension of a
many-level field space.

Put \(W_r=\mathcal M^rU_0\), \(t_r=L^r/n\).
The straight product, the plaquette telescoping of Section
3.5, and the one-step Taylor remainder give
\[
 \alpha_{r+1}\le L\alpha_r+C_L(\alpha_r^2+\omega_r),\quad
 \omega_{r+1}\le
       L^2(1+C_L\alpha_r)\omega_r+C_L\omega_r^2,         \tag{7.12}
\]
where \(\alpha_r=\|\log W_r/i\|_\infty\),
\(\omega_r=\sup|\partial W_r-1|\).
Initially \(\alpha_0\le C\alpha/n\) and
\(\omega_0\le C\alpha/n^2\). Divide (7.12) by
\(t_{r+1}\), respectively \(t_{r+1}^2\). Under the
bootstrap \(\alpha_r/t_r,\omega_r/t_r^2\le K\alpha\),
the relative quadratic errors have sum at most
\(C_LK\alpha\sum_{r<j}(t_r+t_r^2)\). The inhomogeneous
\(\omega_r/t_{r+1}\) contribution to the first bound has
sum at most \(C_LK\alpha\sum t_r\).
First choose \(K\) to dominate this fixed linear transfer
from curvature to potential, then choose \(\alpha\) so that
the remaining exponential factor is below \(3/2\).
A first-exit argument gives
\[
       \alpha_r\le C_L\alpha t_r,\qquad
       \omega_r\le C_L\alpha t_r^2.                    \tag{7.13}
\]
One may separate the curvature bootstrap first to avoid
feeding the linear transfer back as a quadratic error.
Both sums are geometric: \(\sum_{r<j}t_r<1/(L-1)\).

For an increment \(A\) with \(s\|A\|_\infty\le r_*\),
set \(a_0=\eta A\), \(a_{r+1}=F_{W_r}(a_r)\).
The exact straightening identity implies, inductively,
\[
 \mathcal M^r(e^{i\eta A}U_0)=(e^{ia_r}W_r)^{v_r},
 \qquad v_{r+1}=v_r|_{\rm next}\,u_{W_r}(a_r).         \tag{7.14}
\]
The gauge factors do not change the recursion for \(a_r\).
Since \(F_W(0)=0\), (7.11) gives, for
\(p_r=\|a_r\|_\infty/t_r\),
\[
 p_{r+1}\le p_r[1+C_Lt_r(\alpha+p_r)].
\]
If \(C_L(\alpha+2r_*)/(L-1)<\log2\), first exit gives
\(\|a_r\|_\infty\le2r_*t_r\). Also
\(\|u_{W_r}(a_r)-1\|\le C_Lr_*t_r\), so the product of
their complex condition numbers is bounded by
\(\exp(C_Lr_*/(L-1))\). It has no factor depending on \(j\).

Let \(P_{b,a}\) denote the product of derivatives of the
recursion from step \(a\) through step \(b-1\).
Multiplying (7.11), now with the summable radii (7.13),
gives
\[
 \|P_{b,a}\|_{\rm row}\le C L^{b-a},\qquad
 \|P_{b,a}\|_{\rm col}\le C L^{-3(b-a)}.                \tag{7.15}
\]
For the *per-length* row \(q_j(A)=a_j/s\), its derivative
in physical fine coordinates is \(n^{-1}P_{j,0}\).
Consequently its row sum is bounded by \(C\), its column
sum by \(Cn^{-4}\), and each coefficient by \(Cn^{-4}\).
Telescoping against the flat product, term by term, proves
\[
\begin{split}
 \|Dq_j(A)-Q^0_j\|_{\rm row}
                  &\le C_L(\alpha+r_*),\\
 \|Dq_j(A)-Q^0_j\|_{\rm col}
                  &\le C_L(\alpha+r_*)n^{-4}.          \tag{7.16}
\end{split}
\]
Here the flat operator is expressed in this carrier's
local fine and row frames. There is no assertion that these
frames are a single global gauge.

For completeness the second derivative needed in the force
also has a density bound. Twice differentiating (7.14)
produces
\[
 D^2a_j=\sum_{r<j}
 P_{j,r+1}D^2F_{W_r}(a_r)[P_{r,0}\cdot,P_{r,0}\cdot].
\]
Fix its first fine input and sum its second. With
\(n_r=L^r,\ m_r=L^{j-r-1}\), the outer coefficient costs
\(Cm_r^{-3}\), the fixed inner leg costs \(Cn_r^{-3}\),
and the summed inner leg costs \(Cn_r\).
Equation (7.11) bounds the remaining one-step sum.
Thus, after multiplying by \(\eta^2/s\),
\[
 \sup_b\sum_{b'}|D_bD_{b'}q_j(A)(c)|
 \le C_L{\eta^2\over s}
                 \sum_{r<j}m_r^{-3}n_r^{-2}
 \le C_L s(\eta/s)^4 .                                \tag{7.17}
\]
The last inequality is
\(m_r^{-3}n_r^{-2}=L^3n_r/n^3\) and
\(\sum_{r<j}n_r<n/(L-1)\).
Integrating (7.17) along \(tA\), \(0\le t\le1\), gives
the derivative bound for the quadratic remainder, including
the physical \(\eta^{-4}\) in the functional derivative.

A fine bond belongs to row carriers of only its own or
an adjacent layer: a level-\(j\) carrier lies inside
\(\Omega_{j-1}\) and outside \(\Omega_{j+1}\), with at
most a one-cell enlargement. At each such layer the number
of carriers is bounded. Their scales differ by at most a
fixed power of \(L\). In the physical pairings this proves
the full-map column estimate and, for
\(|\omega(c)|\le\gamma s_c^{-3}\),
\[
 \left|\sum_c s_c^4
       \langle\omega(c),D^2q_c(0)[u,v]\rangle\right|
 \le C_L\gamma\,\|u\|_{\rm mass}\|v\|_{\rm mass},\quad
 \|u\|_{\rm mass}^2=\sum_b\eta^4s_b^{-2}|u(b)|^2.       \tag{7.18}
\]
Indeed (7.17) times \(s_c^4|\omega(c)|\) is at most
\(C_L\gamma\eta^4s_c^{-2}\) on either fixed fine leg;
Schur's inequality and the bounded carrier count prove
the displayed estimate.

The same proof applies to the comb scheme on aligned
partitions. Each chain is compared with the common flat
chain, so the two chains need never be aligned at their
intermediate reference averages. Gauge covariance makes
the resulting row/column estimates invariant under the
choice of the local gauge used to prove them. Thus
Section 7.4's shared-node objection does not obstruct
these **operator coefficient bounds**. It remains
necessary to construct the actual global gauge chart,
to use the correct seam endpoint readout in its algebra,
and to justify the critical-point induction in that chart.

### 7.7 The shared-node readout is exact and uses one adjacent layer

Credit: the explicit endpoint extension is (PX31)–(PX38) of
the Sussman–Alpoge outline, with Claude and Codex as authors,
lines 10668–10719. Here is its algebra in the notation needed
for the gauge proof.

Let \(T_j(y,x)\) be the product, in order from \(y\) down
to \(x\), of the actual internal mean transports through
the successive averages of \(U_0\). On the disjoint
assigned pillars put
\[
 (Q'_{\rm p}\lambda)(y)=L^{-4j(y)}
       \sum_{x\in B^{j(y)}(y)}
                   \operatorname{Ad}(T_{j(y)}(y,x))\lambda(x).
                                                               \tag{7.19}
\]
For real \(U_0\) every transport is unitary. The map
\((E_{\rm p}\psi)(x)=\operatorname{Ad}(T_j(y,x))^{-1}\psi(y)\)
therefore satisfies \(Q'_{\rm p}E_{\rm p}=1\).
In the physical fine and top pairings,
\(E_{\rm p}=(Q'_{\rm p})^*\) and
\(Q'_{\rm p}(Q'_{\rm p})^*=1\): the \(L^{4j}\) fine
cells in a pillar have total volume \(s_y^4\).
This proves rank directly.

At an outward level-\(j\) row, the outer centre \(z\)
has assigned level \(j-1\). Its full block is the union
of \(L^4\) assigned finer pillars. The product defining
\(T_j\) gives the identity
\[
 Q'_j\lambda(z)=L^{-4}\sum_{w\in B(z)\cap T^{(j-1)}}
 \operatorname{Ad}(T_{z,w}(\mathcal M^{j-1}U_0))
                         (Q'_{\rm p}\lambda)(w).       \tag{7.20}
\]
The weights multiply to \(L^{-4j}\), and the transports
multiply in their path order. Denote this finite extension
by \(\mathcal E_{j,z}\); at an assigned level-\(j\) centre
use simply \(\mathcal E_{j,z}\psi=\psi(z)\).
For a per-length field row define
\[
 (\bar D_{\rm e}\psi)(c)=s_c^{-1}
 \{\operatorname{Ad}(\mathcal M^jU_0(c))
                    \mathcal E_{j,c_+}\psi
                       -\mathcal E_{j,c_-}\psi\}.      \tag{7.21}
\]
There is no new independent site unknown at the outer
centre. In particular, replacing its readout by its
single assigned top value would be wrong.

Differentiate a relative contour under an infinitesimal
gauge. Its variation is its transported endpoint value
minus its initial value. The mean derivative at the
coincident relative transports is arithmetic averaging.
At one step the derivative of the node factor is
\(Q'_1\lambda-\lambda|_{\rm next}\).
The product rule in (7.14) makes the intermediate values
telescope, yielding \(Q'_j\lambda-\lambda|_{T^{(j)}}\).
Subtract these endpoint factors from the plain row
variation. The result, with per-length normalization, is
\[
                    Q_{\rm actual}D
                         =\bar D_{\rm e}Q'_{\rm p}.     \tag{7.22}
\]
Thus \(Q'_{\rm p}\lambda=0\) implies
\(Q_{\rm actual}D\lambda=0\), also across a seam.

The nonlinear counterpart is equally local. Suppose
two potentials are related by a fine gauge. At level
\(r\) write \(h_r\) for the induced gauge between their
straightened averaged fields. Formula (7.14) determines
it recursively:
\[
 h_{r+1}=u_{W_r}(a'_r)^{-1}
                  (h_r|_{\rm next})u_{W_r}(a_r),        \tag{7.23}
\]
up to reversing all factors if the opposite convention
for the group action is adopted. Require \(h_{j(y)}(y)=1\)
at each assigned top. For an outward row all sites and
internal bonds of its outer level-\((j-1)\) block are
assigned at that finer level. Consequently \(h_{j-1}=1\)
on that block, its two straightened fields agree there,
and their \(u\)-factors in (7.23) agree. Hence \(h_j(z)=1\)
as well. The determining row is unchanged.
This proves that normalization at assigned tops preserves
all the straightened determining constraints. It does
not require separate prescriptions at shared nodes.

Each extension (7.20) reads one finer block. A finer
pillar belongs to one such outer block and at most eight
incident coarse rows. Both normalized row and column
counts are therefore bounded at fixed \(L\). The
amplitude and volume ratios cost one power of the
adjacent scale, not a product through all levels.
The reduced datum has the same one-step geometry:
its outward factors read only interior finer rows.
For its differential \(D+T\), where \(D\) is the
invertible logarithmic diagonal, \(TD^{-1}T=0\);
thus its inverse is \(D^{-1}-D^{-1}TD^{-1}\).
This is the explicit formula (BGD4), not the assertion
that an arbitrary triangular matrix is uniformly
invertible.

### 7.8 How far the actual-row operator transport now goes

The coefficients proved in Sections 7.6–7.7 suffice for
the **local perturbation steps** of Section 3.9. This
statement has a bounded set of hypotheses:

1. The local regular gauge (7.10), including its first
   derivative, is available on each enlarged carrier.
2. The flat operators F0 use the same aligned partitions,
   determining rows and auxiliary first member.
3. Local extensions and partitions of unity are chosen
   with the source's separation margins.

For the scalar precision
\(T'=D^*D+(Q'_{\rm p})^*aQ'_{\rm p}\), the differential
part changes by a first-order coefficient \(C\alpha/s\)
and a zeroth-order coefficient \(C\alpha/s^2\).
The row change is bounded by \(C\alpha\) and its
physical column density by \(C\alpha s^{-4}\), by the
site version of (7.15)–(7.16). For that version each
one-step transported site average is a weighted mean
with row sum 1, column sum \(L^{-4}\), and its
departure from the flat mean is \(C_L\alpha_rt_r^0\).
Equation (7.13) sums these departures.
Thus the normalized local precision perturbation,
composed with F0, is \(C\alpha\). Its Neumann inverse
exists for \(C\alpha<1/2\).

Next construct \(R,H'\) from this actual \(Q'_{\rm p}\)
by (3.14). The exact rank just proved and the
scalar Gram inverse in F0 make the local Gram
perturbation invertible. The identities
\(Q'H'=1,\ Q'G'R=0\) are matrix identities and remain
exact. Equation (7.22) gives \(QD G'R=0\), which is
the typed identity used when forming the transverse
projection \(S=1-DG'RD^*\).

The field precision has the same differential
perturbation and the mass-form perturbation
\[
 (Q_0+\delta Q)^*a(Q_0+\delta Q)-Q_0^*aQ_0
 =(\delta Q)^*aQ_0+Q_0^*a\delta Q
                            +(\delta Q)^*a\delta Q.
\]
The row/column density estimates bound these terms
by \(C\alpha\) in the scaled mass norm. The transverse
term is handled by the already constructed scalar
operators, exactly as in the decomposition
\(DRD^*=DD^*-DPD^*\) of Section 3.9.
The quadratic-current correction is controlled by
(7.18), with the actual multiplier or \(H^*J\);
it is not deleted from the Hessian.

A cutoff commutator with any actual row has kernel
\(Q(c,b)[h(b)-h(c)]\). Its support has diameter
\(Cs_c\); on a localization box of side \(Ms_c\)
the bracket is at most \(C/M\).
The row/column bounds make both commutator norms
at most \(C/M\). The same holds for \(Q'_{\rm p}\)
and the one-adjacent-level extension. Thus the
source's *local* parametrix errors have exactly
the required \(C/M+C M\alpha\) bound, with a new
constant depending only on the fixed finite mean.

Two distinctions are still essential. First, these
estimates do not by themselves construct a global
parametrix on a new boundary convention. Section
7.3 supplies a variational reduction, but every
local inverse in a global cover must still use
that same reduced first member and its frozen
rows. Second, the normalized gauge correction
requires its nonlinear \(Z\)-norm estimate, not
only the linear identity (7.22). Both are needed
before the implication in Section 7.5 is a proof
for all regular competitors. They cannot be
replaced by a finite-dimensional inverse-function
theorem with an unspecified radius.

### 7.9 A direct boundary inverse on the auxiliary first member

There is a way to supply the boundary step just identified
without extending a regular field through the original
outer boundary. Choose the auxiliary member in Section 7.3
so its boundary has a bare-layer collar of width at least
\(4M\eta+4L\eta\). All nonbare field rows have carriers
away from this collar. There \(Q=Q'=1\), in the
per-length conventions at the bare scale.

Moreover \(R\) has no matrix entries there. In fact
\[
 \operatorname{ran}R=D^*D\ker Q',
\]
and \(\ker Q'\) consists of site fields vanishing outside
\(\Omega_1\). Applying \(D^*D\) enlarges this support
by only one fine step. An orthogonal projection onto
vectors supported in that enlargement has both its
rows and its columns zero outside it. Consequently
\(DRD^*\) vanishes beyond a two-step enlargement.
This support fact also follows from the defining
projection; it must not be replaced by an assumption
that \(R=1\) in the bare layer.

For a boundary cube use the local precision on its
intersection with the auxiliary member, with zero
extension of the varying fields. It is the scalar
covariant Laplacian plus \(a\eta^{-2}\), or the
covariant curl form plus \(a\eta^{-2}\) on bonds.
The Wilson correction has operator norm at most
\(C\varepsilon\eta^{-2}\): each plaquette has four
bonds, each bond belongs to at most \(2(d-1)\)
plaquettes, and each coefficient error is
\(C|\partial U-1|\eta^{-2}\).
For \(\varepsilon<a/(2C)\) the real local precision
\(K_{\partial}\) satisfies
\[
 {a\over2}\eta^{-2}\,1
       \le K_{\partial}\le C_a\eta^{-2}\,1.             \tag{7.24}
\]
The upper bound follows by applying
\(|\sum_{i=1}^4v_i|^2\le4\sum_i|v_i|^2\) to each
plaquette and counting the adjacent plaquettes.
It is independent of the shape of the intersection.
This argument uses neither a smooth boundary nor
a Fourier representation.

Set \(\tau=2C_a\eta^{-2}\). The exact series
\[
 K_{\partial}^{-1}
   =\tau^{-1}\sum_{m\ge0}(1-\tau^{-1}K_{\partial})^m   \tag{7.25}
\]
converges in \(L^2\), with ratio at most
\(1-a/(4C_a)<1\). Each factor has range at most two
fine steps. Its \(x,z\) entry is therefore zero until
\(2m\eta\ge\operatorname{dist}(x,z)\); each remaining
entry is bounded by its \(L^2\) norm. Summing the
geometric tail gives
\[
 |(K_{\partial}^{-1}f)(x)|
 \le C\eta^2 e^{-c\,\operatorname{dist}(x,z)/\eta}
                         \|f\|_\infty                 \tag{7.26}
\]
for \(f\) supported in one bare cell, with a fixed
color/orientation factor. There are at most
\(C(m+1)^4\) fine cells at distance between \(m\eta\)
and \((m+1)\eta\); hence the corresponding row sums
are finite and uniform.

A first, respectively second, lattice difference
of the kernel costs at most \(C\eta^{-1}\),
respectively \(C\eta^{-2}\), and shifts its arguments
by at most two fine steps. Equation (7.26) therefore
gives precisely the value, gradient and Laplacian
weights \(\eta^2,\eta,1\). Hölder differences cost
the further factor \(\eta^{-\beta}\), since distinct
fine sites are separated by at least \(\eta\).
The same finite-range proof applies to an adjoint
derivative on the input.

For the local site Gram, \(Q'=1\), so its inverse
is \(G'^{-2}=T'^2\); it has range two and size
\(C\eta^{-4}\). For the field Gram its inverse is
the local precision itself. These are the local
coarse-inverse bounds required in the parametrix.
Small complex perturbations are admitted by the
Neumann series around these real operators, with
the same fixed reduction of radius.

Cover the auxiliary member by the source's two-layer
interior cubes together with these boundary cubes.
Use normalized hat functions, of support diameter
\(CMs\) and slope \(C/(Ms)\), and include a slightly
larger cube for each local inverse. Fixed-dimensional
grid overlap bounds their number at a point by a
constant; taking the square-root normalization
\(h_\nu=f_\nu/(\sum_\mu f_\mu^2)^{1/2}\), with
\(\sum f_\mu^2\ge1\), gives \(\sum h_\nu^2=1\).
The product rule and the row commutator calculation
in Section 7.8 give the scalar defect \(C/M\).
For the site Gram use the three errors in Section
3.9: an off-box term, a difference of local inverses,
and a cutoff commutator. Common walks cancel in
the inverse difference; each remaining walk reaches
the enlarged cube boundary. Its exponential tail
is bounded by Section 3.7. Boundary cubes have the
same estimates by (7.26). The nonlocal \(P=1-R\)
part of the vector defect uses these already
constructed scalar walks. Thus each defect has
two-sided weighted norm at most
\[
                    C/M+C M\alpha+Ce^{-cM}.            \tag{7.27}
\]
Choose \(M\) first so the first and last terms are
below \(1/8\), and \(\alpha\) next so the middle
term is below \(1/8\). The Neumann expansions
converge, with the convolution estimates (3.13).
This supplies the global operator construction on
the auxiliary member, conditional on F0 for the
interior cubes. The cover need not extend through
the original outer boundary.

### 7.10 Nonlinear normalization: the estimate the linear identity needs

Work in the \(Z\) norm of Section 3.8, and use the actual
recursion (7.23). Its logarithms at the assigned tops define
the normalization map \(\mathcal N_A(\lambda)\). Signs are
chosen so its derivative at \(A=\lambda=0\) is \(Q'_{\rm p}\).
The needed estimate is
\[
 \mathcal N_A(\lambda)=Q'_{\rm p}\lambda+N_A(\lambda),
 \qquad
 \|N_A(\lambda)\|_\infty
       \le C(\|A\|_X+\|\lambda\|_Z)\|\lambda\|_Z.       \tag{7.28}
\]
Its radius and \(C\) must be independent of the number
of averages. A fixed-dimensional inverse-function
argument would not prove that.

Here is a direct way of obtaining this estimate.
On a row carrier use (7.10), and let \(h_r\) be the
induced gauge at step \(r\). Transport its values to
the base of one block before comparing them.
Write \(v_r\) for their largest covariant nearest-link
difference in matrix norm. Initially
\(v_0\le C\delta/n\), where \(\delta=\|\lambda\|_Z\).
For a single block the relative transport under \(h\)
is, exactly,
\[
 h(y)\,T(e^{ia}W)(y,x)\,h(x)^{-1}T(W)(y,x)^{-1}.
                                                               \tag{7.29}
\]
If \(h(x)\) is the parallel transport of a single
constant \(h(y)\), (7.23) gives exactly \(h(y)\);
there is no quadratic error in that common value.
In general factor that common value out of (7.29).
All remaining gauge differences have size \(C_Lv_r\).
The finite analytic formula and its derivative at
coincident inputs then give a convex transported
linear average plus an error whose coefficient is
\(C_L(\alpha_r+\|a_r\|+v_r)\).

To estimate differences between neighboring output
blocks, pair corresponding sites of their input
blocks. A path joining each pair has \(L\) links.
The sum of its covariant increments is at most
\(Lv_r\). Commuting the two paths needed to use a
common frame produces at most \(CL^2\) plaquettes,
each bounded by \(\omega_r\); multiplying a gauge
variation contributes the additional factor
\(\sup|\log h_r|\le C\delta\). The nonlinear mean
has the just-bounded coefficient. Thus, while
\(v_r\le K\delta t_r\),
\[
 v_{r+1}\le
 L[1+C_L(\alpha+r_*+\delta)t_r]v_r
                   +C_L\alpha\delta t_r^2.             \tag{7.30}
\]
This uses the flat coefficient \(L\), not a
strictly larger fixed number at every step.
After division by \(t_{r+1}\), its errors are
summable. Choose \(K\) above the initial constant
and the finite curvature transfer, then the radii
so the product of the remaining factors is below
\(3/2\). First exit proves \(v_r\le K\delta t_r\).
Factoring common values also shows
\(|\log h_r|\le C\delta\).

For complex gauges the common changes of frame
must be counted as well. Along one branch the
change of the block value between successive
steps is \(O(\delta t_r)\), by the same finite
formula. Express every intermediate frame relative
to its preceding frame. Their condition numbers
have product at most
\(\exp(C\delta\sum t_r)\), rather than
\(\exp(C\delta j)\). This gives the complex
version on a fixed smaller \(Z\) ball.

Subtract now the exact linearized recursion.
Terms independent of \(\lambda\) vanish.
Terms linear in \(\lambda\), including all
reference-curvature terms, are exactly \(Q'_{\rm p}\lambda\)
by (7.19)–(7.22). Every remaining one-step term
contains either \(a_r\) and a gauge difference,
or two gauge factors of which at least one is
a difference. Equation (7.29) and its exact
constant-value property justify the latter
assertion: the Taylor remainder vanishes on
the constant family, so subtracting that family
in one argument factors out the difference.
Its bound is
\[
             C_L(r_*+\delta)\delta t_r .
\]
The transported site averages have norm one
in the real case; their perturbed products
have uniformly bounded norm by (7.30).
Summing over \(r\) proves (7.28).
Cauchy's formula on a ball with a fixed margin
gives its Lipschitz estimate
\[
 \|N_A(\lambda)-N_A(\tilde\lambda)\|_\infty
 \le C(\|A\|_X+\delta)\|\lambda-\tilde\lambda\|_Z.
                                                               \tag{7.31}
\]
At a seam only (7.20) is added; its count and scale
ratio are fixed. Thus neither estimate gains a
depth factor.

This supplies the replacement for CMP 98 (184)–(214)
used in the gauge proof. Apply (3.17) with the actual
\(H'\), whose bounds now follow from Sections 7.8–7.9.
The contraction makes the normalization exactly
\(Q'_{\rm p}\lambda=0\). Then the link-logarithm
identity, inversion of \(1+R(g-1)R\), and equation
(3.18) use only \(D,R,G',H'\) and this normalization;
their algebra is unchanged. The a priori estimate
(3.19) uses the actual row remainder bounded in
(7.17) and the actual vector inverse. Its absorption
again resets the preliminary loss.

Finally the preliminary comparison of two axial
representatives needs no new inverse. Replace each
comb path in the proof of (3.10) by its contour mean.
Section 7.1 bounds the replacement by its enclosed
plaquettes. At intermediate scale \(t\) the extra
error is \(C\alpha(t/s)^2\), so the reconstruction
sum remains geometric. The mismatch still enters
with coefficient one, since at zero curvature the
mean reproduces the common transport exactly.
At the outward end (7.20) and the reduced datum
introduce one adjacent-scale factor. Thus the
preliminary ascent in Section 3.8, its correction
and its reset apply with the actual rows.
The uniqueness contraction includes every regular
competitor, not merely potentials already placed
in the small slice.

All statements of this paragraph remain conditional
on F0. They use the actual \(R\) built from (7.19).
The unresolved comparison of *gauge-normalization
maps* with the comb \(R\) in Section 7.5 is therefore
unnecessary. The multiplier calculation there is
an alternative, not the route used below.

## 8. Conditional uniform critical-orbit conclusion

Here “conditional” means that F0, stated precisely
in Section 3.9, remains cited-pending. This section
does not promote F0 to a proved library input.
The determining set is the outline's default one,
with inward bonds omitted.

The actual-row constructions of Section 7 supply
the hypotheses of Sections 4–6. The substitutions
are specific: \(q,C\) become the actual straightened
row and its remainder; \(Q'\) is (7.19); \(R\) is
(3.14) with that \(Q'\); the reduced datum contains
the outward factor of (7.20). The identities used
to straighten the constraint, remove its nonlinear
part, form the transverse precision, and obtain
the fibre equation use \(QH=1\) and \(QD G'R=0\);
both have been established. The estimates for
the nonlinear force use the row Hessian density
(7.17), the Wilson product expansion (3.11),
and the actual inverse. Thus the contraction
and the separate recovery of second derivatives
apply with a new finite set of constants.

The radius reset is done at reference 1. At this
reference the actual and source straight rows
agree, the source flat kernels F0 apply, and
the actual nonlinear errors have the bounds
just proved. In the local construction the
artificial coarse boundary is filled with the
actual averages of the critical configuration;
no claim that it is a global minimum is made.
Section 6 therefore gives
\[
 r(U)\le\varepsilon_0
 \quad\Longrightarrow\quad
 r(U)\le\max\{B\varepsilon_{\rm data},\varepsilon_0/2\},
                                                               \tag{8.1}
\]
with constants independent of the number of layers.
Here \(B\) includes the actual finite-mean constants.

For clarity, the descent class is enlarged before
induction. Fix \(C_\downarrow\) from Section 7.2.
Permit datum tests of size \(E=C_\downarrow e\)
everywhere, but require size \(e\) in the protected
collars of all seams still to be deleted. Deleting
one seam changes only its collar, with bound
\(C_\downarrow e\). Every remaining protected
collar is untouched. An old changed collar is
subsequently in the interior of the deleted
region, where the lift has exactly the old
plaquette tests. Hence the same \(E,e\) class
is preserved under each descent. Neither number
is multiplied on descending again.

At depth zero every fine link is prescribed.
There is one configuration and no nonzero
admissible variation. A plaquette of this
datum has the prescribed test bound; the
finite current is a sum of at most \(2(d-1)\)
plaquette contributions and is bounded by
\(C E\eta^{-3}\). Enlarge \(B\) once to include
this base case.

Assume the orbit theorem at depth \(k-1\)
for this enlarged datum class. Its background
is a reference for depth \(k\), with regularity
at most \(C_1BE\); the scale change costs
\(C_1\le C(L)L^3\), and the exact seam section
fixes the required coarse reference data.
The actual chart and Sections 4–5 construct a
critical configuration of radius at most
\(C C_1BE\), and place every regular competitor
in the fixed uniqueness ball. Choose \(E\) so
this preliminary radius is inside the reset
radius. Equation (8.1), applied repeatedly to
the same critical field, brings its regularity
back to \(BE\). The contraction gives one
orbit. This completes the depth induction.

Start this enlarged induction from an ordinary
datum of radius \(\varepsilon_1\) by taking
\(e=\varepsilon_1\). The resulting orbit first
has the bound \(BC_\downarrow\varepsilon_1\).
Applying (8.1) to its *original* datum resets
that bound to \(B\varepsilon_1\). Therefore,
conditional on F0, the default constraint
problem has one regular critical residual
orbit, with
\[
 |\partial U(p)-1|
       \le B\varepsilon_1\eta^2\mathsf L(p)^{-2},
 \qquad
 |J(U)(b)|\le B\varepsilon_1\mathsf L(b)^{-3},            \tag{8.2}
\]
and a larger uniqueness radius fixed before
the depth and volume. This is the uniform
critical-orbit assertion of (1b) Theorem 1,
at the explicitly stated input boundary.

The choices are: \(L\); F0 constants and rates;
the summation gap; localization size and
auxiliary boundary width; actual one-step and
seam constants; operator and gauge constants;
\(B\); fixed uniqueness and reset radii; then
the admissible datum radius small enough for
\(CC_1BC_\downarrow\varepsilon_1\) to fit all
these radii. None is chosen as a function of
the number of layers.

## 9. Holomorphy, a Borel representative, and exact restriction

### 9.1 The datum ball is uniform

Credit: Balaban, CMP 102, Section G, especially (170)–(177).
Only its analyticity construction is used here; the
additional second-derivative estimate asserted later in
that section is not imported without proof.

Let \(U_0\) be the real critical representative at a
datum \(V_0\) strictly inside the admissible radius.
Its first variation vanishes on the tangent fibre,
so \(\mathfrak G_1J=0\). This follows by pairing
with the range of the constrained covariance; it
does not assert \(J=0\). For a raw datum increment
\(V=e^{iB}V_0\), first use the exact reduced-datum
map, including the outward factors. Its norm is
at most \(C_L\|B\|_\infty\) on a fixed complex ball.

In (4.5) the constant term on the fibre now vanishes.
The unknown is determined by the same contraction,
uniformly on \(\|B\|_\infty<r_B\), where \(r_B\) is
chosen after the fixed chart radius. Its iterates
are holomorphic and converge uniformly on every
smaller closed ball: the error after \(m\) steps
is bounded by \(2^{-m}\) times the first error.
Uniform convergence of their finite coordinate
power series, or Cauchy's formula on smaller
circles, proves holomorphy of their limit.
The bound is
\[
 \|A(B)\|_X\le C\|B\|_\infty,\qquad
 |D^*DA(B)|_{-3}+|\Delta_{U_0}A(B)|_{-3}
                          \le C\|B\|_\infty.           \tag{9.1}
\]
The second assertion uses the Euler equation of
Section 5 after subtracting its value at \(B=0\).
All constant force terms cancel. Its remaining
linear forcing is \(O(B)\), and every nonlinear
term contains \(A(B)\). Thus it is not deduced
from holomorphy in a value norm alone.

The gauge to the chosen axial representative
is an explicit recursive map. At a node keep
its gauge value equal to 1. In the block below
a fixed parent, the equation fixing a contour
to its reference value determines the child's
gauge by multiplication and inversion of that
contour transport. Repeat down the pillars.
Every nonnode has a unique parent; no gauge
value is assigned twice. The contour variable
can be either the comb or the actual mean.
Both are covariant and equal 1 on the zero
field. This proves existence and uniqueness
of the representative, not merely existence
of some spanning-tree gauge.

Relative to \(U_0\), a factor at intermediate
scale \(t\le s\) differs from 1 by at most
\(C\|B\|_\infty t/s\), by (7.14)–(7.15).
The product therefore has norm and inverse
norm at most \(\exp(C\|B\|_\infty/(1-L^{-1}))\).
It is holomorphic on a fixed ball, also for
complex \(B\); no product of a fixed loss over
all levels is used. Conjugation by this gauge
and (9.1) give the holomorphic representative
\(\Phi_{V_0}(B)\), with
\[
 M_{\mathbf B}\Phi_{V_0}(B)=e^{iB}V_0,\qquad
 r(\Phi_{V_0}(B))
           \le C(\varepsilon_1+\|B\|_\infty).          \tag{9.2}
\]
For complex fields \(r\) denotes the same two
matrix-norm inequalities, not a claim of
unitary gauge invariance. The preceding bound
on the conjugators justifies their use.

Choose \(\varepsilon_1\) and \(r_B\) so real
increments in that ball keep the datum within
the larger existence radius. On real overlaps
the canonical representatives agree by orbit
uniqueness and the unique axial gauge. Hence
they define a continuous, therefore Borel,
representative on the whole regular real
datum domain. The domain is Borel, since its
finitely many test maps are Borel and are
analytic on the regular branches being used.
If a map on all real data is desired, extend
this representative by a fixed configuration
off that domain; no criticality is asserted
there. On complex overlaps uniqueness follows
from the identity theorem, applied one datum
coordinate at a time from an open real box.
Neither a compactness argument depending on
the dimension nor a minimum of depth-dependent
chart radii is used.

### 9.2 Restriction requires an extension of variations

Let \(\Omega'_q\subset\Omega_q\) be a separated
subsequence, and put \(V'=M_{\mathbf B'}(U|_{\Omega'_0})\).
Here \(U\) is the regular critical field of the larger
problem. Consider a differentiable constraint-preserving
curve in the smaller problem, and extend it by the
fixed values of \(U\) outside \(\Omega'_0\).
Its varying fine bonds touch \(\Omega'_1\);
by the first gap all plaquettes containing those
bonds lie in \(\Omega'_0\). Thus its first action
variation in the larger and smaller problems agrees.

The extension preserves each old determining row.
At level zero the old fixed links do not touch
\(\Omega_1\), whereas every varying link touches
\(\Omega'_1\subset\Omega_1\); hence they are fixed.
For an old level-\(j\) row there are two cases.
If an endpoint lies in \(\Omega'_j\), neither
endpoint can lie in \(\Omega'_{j+1}\), because
neither lay in \(\Omega_{j+1}\). The row is a
new determining row and is fixed directly.
For \(j\ge1\) its other endpoint is still inside
\(\Omega'_0\), since the gap exceeds its length.
If neither endpoint lies in \(\Omega'_j\),
its whole two-block carrier is outside that
region, by alignment of the region with the
block partition. On this carrier the required
level-\((j-1)\) averages are fixed by the
smaller problem. To verify that assertion,
descend to the first level at which the
carrier meets a new region: a row meeting
that region is a determining row; a row
outside it is expressed through one more
level of finer rows. The recursion terminates
at level zero, where the links are fixed.
The exact semigroup law for the actual mean
then fixes the old level-\(j\) row. Outward
rows use their actual finer endpoint block,
which is precisely the readout (7.20).
This argument concerns the plain group
averages, so no unexplained node factor is
lost on extension.

The extended curve is therefore admissible
for the larger critical problem. Its first
variation is zero, proving criticality of
the restricted field. Local scales in the
smaller sequence are no larger than in
the original sequence, so the curvature
and current regularity bounds persist.
The converse averaging bound gives datum
radius at most \(C L^2\varepsilon_1\).
Choose the original radius so this lies
in the smaller problem's existence range.
Its orbit uniqueness now proves
\[
 U_{\mathbf B'}(M_{\mathbf B'}(U|_{\Omega'_0}))
       =U|_{\Omega'_0}\quad
                   \bmod\mathcal G^{\rm res}(\mathbf B'). \tag{9.3}
\]
This proves the exact restriction in (1b)
Theorem 6(b). It also justifies the localization
of critical variations used in Section 6.
Uniqueness alone would not have proved (9.3).

### 9.3 What changing the torus means here

If the varying domain, its action stencils and
all determining carriers fit without wrapping
inside two tori, and the fixed exterior data
agree on their read sets, the two finite
variational problems are literally the same.
The extension argument just given identifies
their critical orbits; the same parent
contours identify their canonical representatives.
Their holomorphic continuations agree on
the common ball by the real identity.

More generally one may restrict a background
from a larger torus and prescribe its actual
restricted averages on a smaller admitted
problem; (9.3) applies. This does not assert
that arbitrary periodic backgrounds on two
different tori agree when their remote data
are unrelated. Their exponential comparison
is the stronger response assertion of
Theorem 6(c), not an exact restriction identity.

## 10. Scope: the whole pointed-core clause is a further requirement

The proof target inherited from *a1-orbit.md*, Section 2,
is (1b) Theorems 1 and 3 and the exact restriction used
by Theorem 6(b), on the default determining set. Sections
8–9 give its depth-uniform version conditional on F0.
They do not justify announcing that every sentence of
Obligation A1 at outline lines 3811–3831 is discharged.
In particular, the added pointed-window sentence concerns
the full pair cores and all actual substitutions.

One part of that sentence has a short independent proof.
Credit: the determinant argument and midpoint tent count
are from the Sussman–Alpoge outline, with Claude and Codex
as authors, (PH20)–(PH21) and the whole-core discussion
following (PW6). Suppose the *entire admitted core*
has \(|U_p-1|\le C a\eta^2\) at every plaquette read
by its own unit tent. For \(U_p=1+E\in\mathrm{SL}(2,\mathbb C)\),
\[
          \operatorname{tr}E=-\det E,\qquad
 \left|1-\tfrac12\operatorname{tr}U_p\right|
                         \le\tfrac12\|E\|^2.
\]
The first identity follows by expanding the two-by-two
determinant of \(1+E\); the second uses the product of
the two singular values of \(E\). Thus the holomorphic
Wilson plaquette action is bounded by \(C a^2\eta^4\).

Write \(\eta=N^{-1}\) and
\(h_z(p)=\prod_{\nu=1}^4(1-|p_\nu-z_\nu|)_+\),
evaluated at the plaquette midpoint. For an unshifted
coordinate the exact normalized sum is
\[
 N^{-1}\left[1+2\sum_{r=1}^{N-1}(1-r/N)\right]=1.
\]
For a half-mesh shifted coordinate it is
\[
 2N^{-1}\sum_{r=0}^{N-1}(1-(r+\tfrac12)/N)=1.
\]
Both equalities follow by
\(\sum_{r=1}^{N-1}r=N(N-1)/2\), whose pairing proof
also includes \(N=1\) with the empty sum.
Taking the product of the four one-dimensional
identities gives \(\eta^4\sum_{p_{\mu\nu}}h_z(p)=1\)
in each of the six orientations. Therefore
\[
                         |A_z(U)|\le C a^2.           \tag{10.1}
\]
This holds on the whole core under its curvature
clause, and includes the coarsest mesh and young
ages. It does not require the field to lie in
the smaller Taylor ball.

What is not proved here is that each actual outer,
inner and removed substitution lies in its assigned
core with a common margin for *every* hereditary
tower clause, including its independent-current
and node/gauge clauses. A bound such as (9.2)
does not imply that assertion. The tower scales
can be smaller than the ambient scales; the
clauses have their own shrinking margins.
Nor does separate holomorphy at two endpoint
pairs put the segment between them in a
possibly nonconvex hereditary core.

Precisely, if the clauses are
\(\|\mathcal R_a(X)\|<r_a\), one needs, on the
actual common substitution curve \(X_\nu\),
\[
 \|\mathcal R_a(X_\nu)-\mathcal R_a(X_0)\|
       <\epsilon_a r_a
 \quad\hbox{for every }a,\qquad
 \|\mathcal R_a(X_0)\|\le(1-\epsilon_a)r_a.              \tag{10.2}
\]
The implication from (10.2) to admission is the
triangle inequality. The uniform estimate for
the whole list is substantive. It is (BGR32)–(BGR33)
and the substitution-room obligation in the
outline, not a theorem of the four Balaban papers
read here. No such estimate is imported from
*a3-response.md*: its specified gate is absent
from this pinned checkout. Consequently (10.2)
is recorded as an unproved additional A1
requirement, not relabelled as a proved consequence
of the variational theorem or as another F0 input.

The version retaining inward rows is also not
identified with the default problem. It has
additional pinch tests and an enlarged field-row
space. The proof above does not supply its
additional inf-sup statement by simply appending
rows to \(Q\). The conclusions of Sections 8–9
have exactly the default convention stated at
their beginning.

## 11. Input ledger and endpoint

The following are mathematical input labels, not audit
verdicts or repository status changes.

| Input consumed by CMP 102 | What is supplied here |
| --- | --- |
| CMP 98 Proposition 2, plaquettes of iterated averages | Section 3.5 rebuilds its curvature recursion; Sections 7.1 and 7.6 give the actual-mean version. |
| CMP 98 Propositions 4–5, analytic remainder and functional derivative | Sections 3.5, 7.6 prove the recursion, strict slack, row density and fixed-leg Hessian sum. |
| CMP 98 gauge averages, (184)–(214) | Section 3.8 rebuilds their use; Sections 7.7 and 7.10 supply the actual endpoint algebra and nonlinear normalization. |
| CMP 99, 75–102, Lemma 1 and current/converse estimates | Section 3.6 supplies the plaquette telescoping and the discrete product-rule expansion. |
| The same paper, Theorem 2 and inhomogeneous gauge correction | Section 3.8 gives the contraction and its a priori reset; Sections 7.7–7.10 transport them, conditional on F0. The unneeded overstrong second-order assertion of Theorem 8 is not used. |
| The same paper, Proposition 6 local gauges | Section 3.8 gives the reference-1 construction, conditional on F0; the boundary margin is retained in Sections 7.3 and 7.9. |
| CMP 99, 389–434, Theorems 3.1–3.3 and the scalar Gram inverse | Section 3.9 rebuilds the local perturbation and walk reduction, conditional on F0. Sections 7.8–7.9 give the actual-row and auxiliary-boundary transport. |
| The same paper, corrected Hessian, minimizer and fibre inverse | Section 3.9 retains both current corrections and the gauge subtraction; Sections 4–5 prove the nonlinear use and recover second derivatives separately. |
| CMP 96 mixed-scale summation used in CMP 102 (162) | Section 3.7 proves the scale-volume count and the convergent sums directly. |
| CMP 95/96 flat scalar, vector, Gram and Hölder inverse estimates | **Cited-pending F0**, stated with norms, weights, geometry and energy forms in Section 3.9. Neither the supplied companion-paper reductions nor the named library energy estimates prove all of it. |

The principal OCR reconstructions are recorded at
their uses: CMP 98 (130)–(131), the strict coefficient
in (154), and the \(|A|\) in (157); CMP 99, 389–434,
the distinct weights in (3.48) and (3.132) and the
Laplacian exclusion in Theorems 3.12–3.13; CMP 102's
local datum (160), scale weights in (162), and the
\(1/8\) in (166)–(167). They were checked against
the indicated scan excerpts or reconstructed from
the neighboring identities as stated in the text.
No OCR string is treated as reliable merely because
it appears in the text layer.

**PROVED, as a conditional research statement:** F0
implies the default determining-set theorem of
Sections 8–9: a unique regular constrained critical
orbit, linear curvature and current bounds, a Borel
real axial representative, uniform local holomorphic
datum balls, exact restriction, and the stated
nonwrapping torus compatibility. The constants do
not grow with the number of separated layers.
The two relevant resets are written explicitly;
the datum descent has its own two-radius invariant.

This is not an unconditional discharge of A1.
F0 remains cited-pending, and the full pointed-core
admission requirement (10.2) remains unproved.
No counterexample to A1 has been obtained. No
audit, numerical discharge, external status claim
or repository status change is part of this note.
