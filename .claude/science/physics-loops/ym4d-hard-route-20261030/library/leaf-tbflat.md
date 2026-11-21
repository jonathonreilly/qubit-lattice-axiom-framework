# Repo search

Codex, 2026-11-08. FINISH row 551, leaf TB-FLAT.
Checkout: `582805ede283a1c8268a9c1c384c35e7376c42ce`.
Research text. Not an audit. Grants no status. No computer-assisted proof.
New arguments below have not been checked by another provider.

`prior/leaf-tbflat.md` was absent. I used the lead's
`prior/repo-search-2026-11-08.md`, §§2, 8, and `rimtb-tree.md`.
The lead searched main and PRs #10114, #10133, #10134, and #10141.
Its search found no supplier of the changed-boundary response.
This is a bounded search record, not a claim of absence from all literature.

I fetched main and read its science-workflow rule 9.
I fetched #10141 at `c73ad7b177d94f89ff37b77386936e3d52b48b05`
and #10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
The following source ranges were checked with `git show`.

| Hit | What is available | Distance from TF |
|---|---|---|
| #10141, `research/ym4d/library/out-mu.md`, 8–32, 69–82, 189 | Unique regular axial minimizer and holomorphic nesting on its admitted windows. | Reuse on unchanged, memberwise dominated collar windows. No derivative decay or new free-boundary admission. |
| #10141, `research/ym4d/library/fp1.md`, 142–168, 246–258 | Equality of plain and straight flat fibre energies; exponential kernels in current lattice units. | Reuse the fibre algebra. The correcting gauge is not norm controlled. Fine-mesh pointwise density estimates are expressly excluded. |
| #10114, `SQ.md`, 1401–1415, 1458–1467 | The link-reflection identity; real curvature regularity with a controlled current. | The reflection identity is usable. Neither passage gives the hard-row Schur inverse with TF's gauge readouts. |
| #10114, `OFFGLOB2_55.md`, 847–866 | Free-boundary localization and local uniqueness with decay remain open. | A nearby open problem, not a supplier. |

The last two paths are under
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
Credit their repository authors and Codex checks.
The local registry lists H-C-MARK as open and unowned.
A targeted search of the registry, `open-core.md`, and `l17c.md`
found no separate TB-FLAT owner or completed supplier.
Row 551 is the assignment pursued here.

## 1. Ports and the exact readout

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the constrained variational and propagator methods.
SA and I denote their outline and complete account I at `31a47c543775`.
Y denotes `YM4_1400.tex` at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
The supplied `/tmp` copies were already present and were used without refetching.
Source reads were bounded. No numerical calculation was run.

The SA index and neighbouring rows were consulted for the averages,
R4–R6, the saddle equations, and boundary forcing.
The CA §4.12–4.19 index identifies I 43122–43155 as a cited input.
That passage says its block-scale theorem is “used here by statement”.
It does not prove TF for the changed exterior.

Use `out-mu.md` on its admitted windows; do not reprove its uniqueness theorem.
Use `fp1.md`, Lemma 4, for its exact fibre identity, with its stated limits.
Retain the payment already checked in `gates/hcm-repair-check.md`, findings 3–4.
It needs the TB-BC supplier and ownership before it yields the price in
`hcm-repair.md`, §3. TF alone cannot make that payment.

SA 12226–12292, BGR28–BGR30, requires the complete difference force.
Its decay deduction is conditional on the correctly weighted inverse.
SA 5663–5727 specifies the original hereditary domain and independent current.
No trace Hölder hypothesis is added here.

Y 13360–13427 specifies the potential, first difference, and covariant
\(D^{\mathsf T}D\) readouts. Their weights are \(\ell,\ell^2,\ell^3\).
It also specifies curvature, full-stencil current, and the node frame.
It does **not** require the full uncontracted Hessian of the potential.
Only existing consumer stencils are used below.
A logarithm in some other second derivative would not kill TF.

Bałaban's CMP **102** (1985), 277–309, Theorem 1, (1)–(10),
uses separated towers and enlarged interior cubes.
Its Proposition 9, (182)–(190), gives the corresponding response method.
CMP **109** (1987), 249–301, (4.35), compares an interior read with a free response.
That passage supplies no bound on a read touching the new rim.
CMP **96** (1984), 223–250, p.229, explicitly distinguishes its graded
boundary convention from local Neumann conditions at sharp edges.
These are scope checks, not counterexamples.

## 2. Kill test first

**Outcome: no counterexample obtained.**
The null-space test below applies to the actual box.
The nonzero face and corner calculations test homogeneous tangential sectors.
They keep the block constraints exactly. They do not test the whole mixed-depth saddle.
In particular, their success is not a proof of TF.

### 2.1 No physical zero mode on a contractible box

Work with one color. The other colors give identical copies.
Let \(d_X\) be physical curl on the plaquettes wholly inside \(X\).
Let \(Q_X\) be the derivative of the retained literal group averages.
Gauge covariance gives

\[
 Q_X D_X\phi=D_{\mathfrak B}r\phi.                 \tag{1}
\]

Here \(r\phi\) is the value at each determining node.
For raw row logarithms, the right side is the endpoint difference without division by the row length.
This is the endpoint telescoping identity, not a substitution of straight averages.
It holds for mixed rows as well.

Suppose \(Q_Xv=0\) and the free Wilson quadratic energy of \(v\) vanishes.
Then \(d_Xv=0\) on every plaquette.
Choose a base vertex. Define \(\phi(x)\) by integrating \(v\) along a lattice path to \(x\).
Adjacent coordinate steps can be interchanged inside the rectangular box.
Each interchange changes the sum by a plaquette curl, which is zero.
Backtracking also changes nothing. Thus \(v=D_X\phi\).
Equation (1) says that \(\phi\) is constant on each connected determining-node component.
Exactly those transformations preserve the retained data at the identity.
For the complete partition of a connected box, the determining graph is connected.
A fine-site path induces a path through adjacent blocks.
Thus one common constant can be subtracted to make \(\phi\) zero at all determining nodes.
After quotienting them, \(v=0\).

This proves absence of a non-gauge null direction.
It does not bound the smallest positive eigenvalue uniformly.
Any purported inverse must also discard dependent multiplier rows.
Their null vectors are not physical zero modes.

### Literal rows in the homogeneous probes

The literal CA convention must not be silently replaced by centered symmetric rows.
I 43010–43017 refers to Bałaban's averaging map.
CMP 98, (2), (14)–(15), uses corner-rooted blocks and its prescribed paths.
For those paths the one-step flat identity is still
\(Q=S-d_{\rm coarse}\sigma\), where \(\sigma\) is the block mean of the internal path integral.
Iterating gives the fibre identity of `fp1.md`, (9), with the literal path primitive.
The argument works on a complete-block box as well as a torus:
its two scalar maps, block mean and node evaluation, remain onto.
It therefore identifies the curvature minima for the plain and straight fibres.
It does not identify their representatives or bound a general restoring gauge.

Here is the explicit correction used only for the homogeneous probes below.
If \(S(u-a)=0\), put \(c_y=\sigma(u-a)(y)\).
Choose a scalar \(\phi\) with \(\phi(y)=c_y\) at the top nodes.
Then endpoint covariance gives

\[
 Q(u+D\phi)=Qu+d_{\rm coarse}c=Qa.                 \tag{1a}
\]

This keeps **all** literal rows, including the nontangential rows.
It changes no curvature or physical current.
The primitive is bounded by \(C\|u-a\|_\infty\) on the blocks it reads.
Here is the needed bound for the composed literal primitive.
Write \(Q^{[r]}=S^{[r]}-d_r\sigma^{[r]}\).
Endpoint telescoping gives \(\sigma_Ld_r=q_L-r_L\).
Substitution into the next step cancels the two block-mean terms and gives

\[
 \sigma^{[r+1]}=\sigma_LS^{[r]}+r_L\sigma^{[r]}.
\]

The first term averages internal paths of at most \(d(L-1)\) coarse bonds.
Each straight coarse bond integrates the fine field over physical length \(s_r=L^rh\).
Thus this term costs at most \(dLs_r\|u-a\|_\infty\).
The paths stay within the complete top block.
Sum over \(r\) and use \(\sum_{r<m}L^{r+1}h\le L/(L-1)\) when \(L^mh=1\).
This proves the stated uniform bound and its local version.

For these top-spacing-one probes, \(\phi\) can have uniformly bounded derivatives through order three.
Take translates of one fixed smooth function, equal to one at its node,
with support in a cube of radius less than \(1/2\), and multiply by \(c_y\).
The supports are disjoint. Restrict them at a free exterior face.
Their values at every other node are zero.
The mean-value formula bounds physical finite differences by the corresponding smooth derivatives.
Thus the correction costs \(C\sup_y|c_y|\), independently of the mesh.
If \(c_y\) decays with distance from the boundary, the correction has the same decay at a smaller rate.
This explicit correction is not a bound for the task's prescribed gauge on a mixed tower.

### 2.2 Exact face calculation

Take top spacing one and fine spacing \(h=1/n\), with \(n=L^m\) and odd \(L\).
Use \(K\ge2\) complete blocks in the normal direction.
The tangential polarization is \(A_3=u(x_1)T\), with one fixed color \(T\).
First take the tangential directions infinite or periodic.
This is the zero tangential-frequency face model.

The straight 3-row is exactly the block mean of \(u\), in top units.
The other straight rows vanish.
Compute that constrained minimizer first, then apply (1a) to the literal datum of the ambient field.
The fibre identity makes the corrected field a minimizer for those exact literal rows.
In the centered symmetric convention the primitive vanishes by the centered direction-3 sum.
For the literal corner-rooted convention, (1a) must instead be retained.
No approximate row matching is used.

Put fine sites at \(x_j=h(j+1/2)\), for \(0\le j<Kn\).
Prescribe the means of the affine ambient field \(a(x)=fx\):

\[
 n^{-1}\sum_{r=0}^{n-1}u_{in+r}=f(i+1/2),
 \qquad 0\le i<K.                                  \tag{2}
\]

Minimize \(\frac h2\sum_j |(u_{j+1}-u_j)/h|^2\).
Let \(p_j=(u_{j+1}-u_j)/h\).
At the free endpoints set the missing fluxes \(p_{-1}=p_{Kn-1}=0\).
The Euler equation is

\[
 (p_{j-1}-p_j)/h=\lambda_i\quad(j\text{ in block }i).
\]

Write \(t_i=p_{in-1}\), so \(t_0=t_K=0\).
Summing that equation through one block gives

\[
 \lambda_i=t_i-t_{i+1},\qquad
 p_{in+r}=\left(1-\frac{r+1}{n}\right)t_i
                    +\frac{r+1}{n}t_{i+1}.          \tag{3}
\]

The last value in (3) is the interface flux; at the final endpoint it is the missing zero flux.
Sum (3) again to recover the site values and then their means.
With \(\alpha=(n-1)/(2n)\) and \(b=(n^2-1)/(6n^2)\), this gives

\[
 \bar u_i=u_{in}+\alpha t_i+b(t_{i+1}-t_i),
\]
\[
 \bar u_{i+1}-\bar u_i
   =bt_i+(1-2b)t_{i+1}+bt_{i+2}=f.                  \tag{4}
\]

For \(n>1\), put

\[
 q=\frac{1-2b-\sqrt{1-4b}}{2b},\qquad \rho=-q.
\]

Since \(0<b<1/6\), \(0<q<q_*:=2-\sqrt3<1\).
One can check the bound without approximation:
\(b=q/(1+q)^2\), increasing for \(0\le q<1\), and
\(q_* /(1+q_*)^2=1/6\).
The unique solution of (4) is

\[
 t_i-f=-f\frac{\rho^i+\rho^{K-i}}{1+\rho^K}.        \tag{5}
\]

Substitution verifies the recurrence and both endpoint values.
Uniqueness follows from strict diagonal dominance:
\(1-2b>2b\).
Thus

\[
 |t_i-f|\le\frac{|f|}{1-q_*^2}
                  (q_*^i+q_*^{K-i}).               \tag{6}
\]

Equations (3) and (6) bound the first differences of \(w=u-a\).
Its mean in every block is zero, by (2).
Any two sites in a block are less than one unit apart.
Telescoping between them therefore bounds \(|w|\) by the same first-difference bound.
At a full stencil, \(-\Delta_h w=\lambda_i\), because \(\Delta_h a=0\).
Equation (3) bounds \(|\lambda_i|\) by the two adjacent errors in (6).
All three scalar readouts have uniform exponential decay in block distance from the two endpoints.
The correction (1a) preserves that conclusion in its explicitly chosen smooth frame.
For \(n=1\), (2) fixes every site and \(w=0\).

The raw omitted-plaquette force is of order \(f/h\).
The coupled solution has no such loss.
This solves the constant-flux face probe, not the arbitrary-face-force problem.

### 2.3 Two-face corner calculation

Use two normal coordinates and the tangential polarization
\(A_3=(fx_1+gx_2)T\).
The straight row means are
\(f(i+1/2)+g(j+1/2)\).
Let \(u_f,u_g\) be the two one-dimensional solutions just constructed.
Then

\[
 u(x_1,x_2)=u_f(x_1)+u_g(x_2)                       \tag{7}
\]

has those means and the free flux condition on all four normal faces.
Its discrete Laplacian is the blockwise constant
\(\lambda_i^f+\lambda_j^g\).
Pairing it with any zero-block-mean variation gives zero.
The quadratic energy is positive on such variations, so (7) is the unique scalar minimizer.
The potential, first differences, and contracted second readout are sums of the face bounds.
Apply (1a) to retain the ambient field's literal rows; its correction obeys the same uniform bounds.
No corner logarithm appears in these readouts.

These sectors do not impose the remaining tangential faces of an actual finite stage.
Nor do they verify every original hereditary window or its node gauge.
They therefore supply neither an admissible counterexample nor a universal pass of the kill test.
The actual-box result of this section is the null-space conclusion in §2.1.
The unresolved kill test is mesh growth for the coupled response outside these sectors.

## 3. The actual coupled force

Here is an exact finite-dimensional formula for \(B_X\).
It specifies the omitted terms before any estimate.
Take the fine pairing \(\eta^4\sum_b\), and raw row logarithms with counting pairing.
Changing a row pairing changes its adjoint and multiplier together.
Fixed trace normalization factors can be absorbed in the action throughout.
The matrices at the identity are real. Extend their action complex linearly.
Their complex transposes are bilinear, as in SA BGR7–BGR9.

For a retained single-step row \(c=(y,y')\), its derivative is

\[
 (Q^{(1)}a)_c=L^{-4}\sum_{x\in B(y)}
 \left\{I_{\gamma_{y,x}}a+I_{[x,x+L\eta e_\mu]}a
                         -I_{\gamma_{y',x+L\eta e_\mu}}a\right\}, \tag{8}
\]

where \(I_\gamma a=\eta\sum_{b\in\gamma}\operatorname{sgn}(b,\gamma)a_b\).
Average the internal paths with their prescribed multiplicities.
Iterate (8) on the actual levels, retaining the specified mixed rows.
For \(\mathfrak B^{\rm TB}\), remove the artificial lower face-lift rows.
Retain only complete top rows at the exterior.
This defines \(Q_X\); it is not an arithmetic site mean in general.
For the literal corner-rooted convention, (8) is Bałaban CMP 98, (14)–(15).
CMP 109, (0.8), (0.11)–(0.12), gives its contour-averaged version.
Use the actual block roots and path weights; these versions are not identified without a frame map.

Put \(H_X=d_X^*d_X\).
At the identity with zero base multipliers, this is the Wilson Hessian.
The constraint-curvature term of SA BGR4 vanishes at that base point only.
Let \(G_Xa=s_X\) denote the prescribed linear gauge and node equations.
Discard redundant equations, or equivalently quotient their multiplier null space.
The extended saddle is

\[
 \mathcal S_X^N=
 \begin{pmatrix}
 H_X&Q_X^*&G_X^*\\
 Q_X&0&0\\
 G_X&0&0
 \end{pmatrix}.                                      \tag{9}
\]

The plus signs fix the multiplier convention used here.
Write the original equations, before restriction, as

\[
 H_oa_o+Q_o^*\lambda_o+G_o^*\gamma_o=j_o,
 \quad Q_oa_o=d_o,\quad G_oa_o=s_o.                  \tag{10}
\]

All quantities in (10) are the original linear responses to the input \(z\).
Let \(R\) restrict fields and forces to common fine bonds.
Let \(P\) retain common multiplier rows, with zero entries on new rows.
Let \(P_g\) do the corresponding gauge-row identification.
The changed right side is \((j_X,d_X^{\rm row},s_X)\).
The superscript distinguishes row data from the curl operator.

Subtract the original solution restricted to the common variables.
Then

\[
 B_Xz=\begin{pmatrix}f_X\!\\ b_X\!\\ g_X\!\end{pmatrix}, \qquad
 \begin{aligned}
 f_X={}&j_X-Rj_o+(RH_o-H_XR)a_o\\
       &+(RQ_o^*-Q_X^*P)\lambda_o
        +(RG_o^*-G_X^*P_g)\gamma_o,\\
 b_X={}&d_X^{\rm row}-Q_XRa_o,\\
 g_X={}&s_X-G_XRa_o.
 \end{aligned}                                      \tag{11}
\]

Indeed, (10) substituted in (11) gives
\((j_X,d_X^{\rm row},s_X)-\mathcal S_X^N(Ra_o,P\lambda_o,P_g\gamma_o)\).
This proves the difference identity including every row.
On a common physical row, \(b_X=0\) when its datum and full carrier agree.
Newly retained top rows and changed gauge rows must still use (11).
Node restoration is the last row, not an omitted informal adjustment.

The omitted-plaquette term has the explicit form

\[
 ((RH_o-H_XR)a_o)_b
  =\eta^{-1}\sum_{\substack{p\not\subset X\\b\in\partial p}}
          \operatorname{sgn}(p,b)(d_oa_o)_p.          \tag{12}
\]

Only original plaquettes enter this sum.
For retained plaquettes, restriction commutes with curl, so those contributions cancel.
Equation (12) is the surface current diagnosed in `hcm-tb.md`, (TB5).
The remaining two terms in the first row of (11) are equally necessary.

For a physical constrained minimizer, \(j_o=j_X=0\).
If a specified independent-current extension contributes explicit forcing, retain it in (11).
Do not identify that extension with the physical Hessian without its defining equations.
SA 11798–11805 makes this distinction explicitly.

For each fixed finite mesh, compatible row data have an energy minimizer modulo gauge.
To see this, take a point of the affine fibre.
Its curl image is an affine subspace of a finite-dimensional space, hence closed.
The nearest point of that image to zero exists and is unique.
A preimage minimizes the energy.
Two minimizing preimages differ by a zero-curl, zero-row field.
Section 2.1 identifies that difference as a retained-data gauge transformation.
A genuine prescribed slice selects at most one representative.
The same argument with a linear force works when the force annihilates residual gauges.
This proves finite solvability for compatible data and gauge-invariant forcing.
It does not supply a uniform row lift, gauge-restoration bound, or data-admission theorem.

## 4. The remaining lemma in a reduced form

Keep the original input space and norm of TF, including every hereditary read and current radius.
They are not replaced by bounds on surface flux alone.
At finite mesh restrict (9) to its actual fixed slice \(\mathcal V_X\).
Write \(q_X=Q_X|_{\mathcal V_X}\).
Work on the compatible datum image if some rows are dependent.
Choose a right inverse \(E_X\) of \(q_X\).
Let \(P_X\) parametrize \(\ker q_X\), and set

\[
 K_X=P_X^*H_XP_X,\quad
 L_X=P_XK_X^{-1}P_X^*,\quad
 T_X=E_X-L_XH_XE_X.                                 \tag{13}
\]

Section 2.1 gives finite invertibility of \(K_X\) after gauge removal.
These formulas are SA 11807–11888, BGR7–BGR9, ported with the present sign convention.
They are exact identities, not uniform bounds.

For a nonzero gauge residual in (11), choose its actual restoring field \(e_g\).
Its slice equation is \(G_Xe_g=g_X\).
It must preserve the specified node normalization.
Replace

\[
 \widetilde f=f_X-H_Xe_g,\qquad
 \widetilde b=b_X-Q_Xe_g.
\]

The field response is

\[
 w_X(z)=e_g+L_X\widetilde f+T_X\widetilde b.          \tag{14}
\]

The corresponding multiplier follows from BGR8; it is not dropped.
Formula (14) is independent of the auxiliary right inverse used in (13).
Uniqueness proves that independence.
The original comparison's node readout must be restored with the same gauge construction.

**CBR: coupled boundary readout lemma.** For every actual stage and every input \(z\)
in TF's original linearized common domain, construct (14) in the prescribed slice.
Prove, for fixed \(C,c>0\) independent of mesh, depth, and the old core,

\[
 \sup_{x\ {m read}}e^{c d(x,\partial_{\rm changed}X)}
   \mathsf N_x\bigl(w_X(z),\text{its prescribed node readout}\bigr)
       \le C\|z\|_{\rm original}.                  \tag{15}
\]

The readout includes the contracted second operator and full-stencil currents of §1.
The forces are exactly (11), with the same input in every term.
There is no separate arbitrary surface-force quantifier.
Compatible row lifting and gauge restoration on these inputs are included in CBR.
Thus (15), with the finite identities above, would supply TF.
CBR is the one remaining lemma attacked below.

## 5. Three attempts at CBR

### Route 1: constrained energy projection

First suppose the gauges have been aligned and \(b_X=0\).
In the physical comparison with no explicit current source,
the new field minimizes the same quadratic energy over its retained affine fibre.
Writing the correction as \(w\in\ker q_X\), its weak equation is

\[
 \langle d_Xw,d_Xv\rangle
       =-\langle d_XRa_o,d_Xv\rangle,
       \qquad v\in\ker q_X.                        \tag{16}
\]

Set \(v=w\). Cauchy–Schwarz gives

\[
 \|d_Xw\|_2\le\|d_XRa_o\|_2.                     \tag{17}
\]

This estimate keeps the surface cancellation and has no mesh loss.
For nonzero row residual, subtract a row lift first, as in (14).
The same projection argument applies to the remainder.
Thus energy minimization is a valid start; estimating the raw force separately is unnecessary here.

I then tried to obtain (15) from a gap and exponential energy localization.
Even granting both estimates, that step does not give the required point evaluations.
In four dimensions an energy-sized bump can have arbitrarily large point values.
For example, a scalar bump of height \(h^{-1}\), supported on a fixed number of fine sites,
has gradient of size \(h^{-2}\) on a fixed number of bonds.
Its physical gradient energy is bounded, since \(h^4(h^{-2})^2=1\).
Its supremum tends to infinity.
Two opposite bumps in one block also have zero scalar block mean.
This example diagnoses the proposed energy-to-pointwise step only.
It is not asserted to solve the vector response equation.

An evaluation estimate on the **solutions** of (16) is therefore still necessary.
It must include the contracted second readout and the restoring gauge.
FP1's gap does not supply this fine-mesh estimate; its D4 expressly distinguishes the two scales.
**Route 1 stops at that pointwise step of CBR.**
Neither (17) nor a spectral gap is reported as TF.

### Route 2: action reflection and the row Schur complement

For a homogeneous top-block rectangle, use the reflection of `SQ.md`, 1401–1415.
At the linear level, copy tangent components, reverse reflected normal components,
and set crossing normal links to zero.
Call this extension \(\mathcal E\).
Its curl energy is \(2^4\) times the intrinsic box curl energy.
This identity is ported, not re-derived.

For centered symmetric rows, reflection permutes the internal contour families in (8).
A coarse normal row crossing a mirror then maps to its own negative and is zero.
The literal corner-rooted rows require an additional check.
For example, reflection across the left face of a block with sites \(0,h,\ldots,1-h\)
sends its root \(0\) to \(-h\).
The adjacent block's prescribed corner root is \(-1\).
These are different points when \(n>1\).
Thus the action identity alone does not intertwine the prescribed row and node operators.
A change of root inserts internal path integrals, or their linear gauge correction.
Equation (1a) handles this in the homogeneous probes.
It is not a uniform intertwining theorem for the actual mixed rows and their prescribed node frame.

For clarity, the exact algebra on a genuine finite slice is as follows.
Put

\[
 A_X=H_X+q_X^*q_X,\quad G_X^{\rm f}=A_X^{-1},\quad
 W_X=q_XG_X^{\rm f}q_X^*.
\]

Use the compatible independent rows. Then \(A_X\) and \(W_X\) are positive definite.
The constrained inverse and datum lift are

\[
 L_X=G_X^{\rm f}-G_X^{\rm f}q_X^*W_X^{-1}q_XG_X^{\rm f},
 \qquad T_X=G_X^{\rm f}q_X^*W_X^{-1}.              \tag{18}
\]

Direct substitution gives \(q_XL_X=0\), \(q_XT_X=I\), and the constrained equations.
Hence uniqueness identifies (18) with (13).
Reflection can transport these identities when the slice and its row weights also intertwine.
It does not permit replacing \(W_X^{-1}\) by a scalar block Gram inverse.

This attempt acts on the operator and constraints, rather than assuming a reflected input stays in its radius.
Even if the remaining row and slice intertwining is supplied,
reflecting the force (11) still leaves (12) as a layer source of size \(\eta^{-1}\).
Crossing plaquettes in the reflected **solution** vanish.
That fact does not make the cut flux of the original field vanish.
The ordinary volume-force row estimate applied to this extended source still costs \(\eta^{-1}\).

I tried the two available substitutions in (18).
FP1 supplies current-scale covariance kernels, not the required fine readouts of \(L_X\).
Bałaban CMP 109, (4.35), supplies an interior comparison with a distance factor.
It does not estimate the surface trace of (18) at zero distance.
The mixed-core case additionally requires the same literal row and node-frame identification on reflected seam rows.
Keeping those terms in (11) leaves the same unestimated coupled readout (15).
**Route 2 stops at the weighted boundary read of (18) on the range of (11).**
This is not a failure of the reflection identity.

### Route 3: a surface kernel bound

The next attempt was to bound the Neumann surface kernel directly,
then apply it to (12) before adding the row and gauge contributions.
The following exact discrete example rules out that sufficient estimate.
It also shows why the word “coupled” cannot be dropped from CBR.

Take \(h=1/n\), with \(n=L^m\) tending to infinity through the permitted meshes.
Use the half-space \(r\ge0\), with tangential coordinate
\(l\in\mathbb Z/n\mathbb Z\).
Physical coordinates are \((hr,hl)\).
Use two spectator coordinates, and the vector polarization \(A_3=u\).
Take direction 3 periodic and keep the field independent of it.
Thus the vector divergence is zero and its curl Hessian on this polarization is the scalar Laplacian.

Let \(N=\lfloor n/16\rfloor\ge1\), and define

\[
 \theta_j=2\pi j/n,\quad
 \alpha_j=2\operatorname{arsinh}\!\left(\sin(\theta_j/2)\right),
 \quad g_N(l)=\sum_{j=1}^{N}\frac{\sin(\theta_jl)}j.
\]

The surface amplitude \(g_N\) is uniformly bounded.
Here is a hand proof, valid before sampling on the lattice.
For \(0<t\le\pi\), put \(m=\max(1,\lfloor1/t\rfloor)\)
and sum first through \(\min(m,N)\).
Those terms have total absolute value at most \(2\).
Partial sums of \(e^{ijt}\) have magnitude at most \(1/\sin(t/2)\).
Summation by parts bounds the remaining sine sum by
\(C/(m\sin(t/2))\le C'\).
For \(t>1\), take \(m=1\); the same bound is uniform.
Periodicity and oddness cover the remaining values of \(t\).
Hence \(\|g_N\|_\infty\le C\), independently of \(N,n\).

Set

\[
 u_{r,l}=\sum_{j=1}^{N}
    \frac{h e^{-\alpha_jr}}{j(e^{\alpha_j}-1)}
                              \sin(\theta_jl).      \tag{19}
\]

For \(r\ge1\), \(-\Delta_hu=0\), since

\[
 2\cosh\alpha_j-2=4\sin^2(\theta_j/2).
\]

At the free boundary the normal Laplacian is \((u_{0,l}-u_{1,l})/h^2\).
Adding the tangential Laplacian gives

\[
 (-\Delta_{h,N}u)_{0,l}=g_N(l)/h,                 \tag{20}
\]

because \(1-e^{-\alpha}+4\sin^2(\theta/2)=e^\alpha-1\).
Thus (19) is the response to a uniformly bounded physical surface density.

Every complete straight top-block average of (19) is zero in direction 2.
Apply (1a) with \(a=0\) to obtain \(\widehat u=u+D\phi\) with every literal top row zero.
This correction is uniformly bounded in its first three scalar derivatives.
Indeed, \(\sin(\theta_j/2)\ge\theta_j/4\) and
\(\operatorname{arsinh}s=\int_0^s(1+t^2)^{-1/2}dt\ge s/2\) for \(0\le s\le1\).
Thus \(\alpha_j\ge\theta_j/4\), and
\(\|u\|_\infty\le C\sum_{j\ge1}j^{-2}\le2C\).
The path bound preceding (1a) then bounds its node values.
Curl annihilates \(D\phi\), including at the free boundary.
Thus (20) is unchanged and the row multiplier can still be zero.
This example does not obtain its loss by dropping the hard averages.

At the boundary,

\[
 (D_2u)_{0,0}
   =\sum_{j=1}^{N}\frac{\sin\theta_j}{j(e^{\alpha_j}-1)}
   \ge\frac14\sum_{j=1}^{N}\frac1j.               \tag{21}
\]

Indeed \(0<\theta_j\le\pi/8<1/2\), \(\alpha_j\le\theta_j\),
\(e^{\alpha_j}-1\le2\alpha_j\), and \(\sin\theta_j\ge\theta_j/2\).
The harmonic sum diverges; grouping indices between consecutive powers of two proves this by hand.
The readout in (21) is a curvature component of \(u\) and \(\widehat u\), so gauge restoration cannot remove it.
Make the fourth direction a free half-line and keep \(u\) constant in it.
The same calculation holds at the resulting two-face corner.
Its fourth-direction boundary flux is zero.

This disproves an arbitrary-surface-density bound for the first readout,
even with exact top rows in these homogeneous face and corner models.
It is **not a counterexample to TF**.
No uniformly bounded original input \(z\) has been constructed with (11) equal to this surface force alone.
Taking \(Ra_o=u\) would already make its first-difference input norm diverge by (21).
Changing that original field also changes the other terms of (11).
They cannot be discarded while retaining its original norm.

A trace Hölder assumption would suppress this example.
TF does not supply that assumption, and adding it would change the task.
The remaining possible step is a cancellation estimate on the **joint** range of (11).
**Route 3 therefore fails to prove CBR by separately bounding its surface term.**
Equations (19)–(21) identify the precise failed sufficient estimate.

## 6. Result

**Stopping condition (c): CBR, (15), remains open after the three routes above.**
The energy route controls a quadratic norm but not the required pointwise reads.
Reflection gives an action identity, but literal row transport and the coupled boundary trace remain unestimated.
The separate surface-kernel route has the explicit logarithmic obstruction (19)–(21).
These failures do not prove CBR false.

The work supplies the full difference force (11), finite compatible solvability modulo gauge,
the null-space test, and exact constant-flux face and corner responses.
It also rejects the stronger arbitrary-surface-force substitute with the hard top rows retained.
It does not supply TF on the original common domain.
No original hereditary input has been shown to violate TF.

TB-BC and the H-C-MARK payment therefore remain conditional.
The next tree step after a proof of TF would construct the regular constrained branch.
That step has not been reached.
No registry, gate, queue, or other source file was changed.

| Item | Status in this research note | Limit |
|---|---|---|
| Prior admitted-window uniqueness and nesting | Reused | Exactly `out-mu.md`'s domains and published inputs |
| Literal flat average and complete force | Written, (8)–(12) | Actual row, gauge, and current conventions must be retained |
| Physical null mode on the contractible box | Excluded, §2.1 | No uniform eigenvalue estimate follows |
| Finite constrained solution | Established for compatible data modulo gauge | No uniform lifting or admission claim |
| Constant-flux face and two-face scalar sector | Solved, (2)–(7) | Homogeneous tangential sector; not the whole stage problem |
| Arbitrary surface-density inverse bound | False, (19)–(21) | A stronger substitute, not TF |
| Full TF kill test | No admissible counterexample obtained | General coupled mesh growth remains unresolved |
| TB-FLAT / TF | Open | CBR remains after three routes |
| TB-BC and renewed-mark payment | Not supplied | Existing downstream hypotheses remain |

**First open input: CBR (15), for the exact coupled force (11) on TF's original common domain.**
