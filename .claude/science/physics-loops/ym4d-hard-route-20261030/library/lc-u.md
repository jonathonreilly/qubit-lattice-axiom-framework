# Covariant localization at a class-fill wall
Provenance: OpenAI Codex; configured model `gpt-6-astra`, effort `max` (local configuration, not an attestation of the serving backend); commit `67b7f74b403c1051ad2cf4353d7d153483a2e79a`; mapped-side research text, not an audit; grants no status.

## 1. Scope, units, and the test attempted first

**Discharged (scope).** The prescribed GOAL and FINISH sections were read first.
This investigation writes only this note. The pinned repository methodology
was read with `git show`, because it is absent from the sparse working tree.
The single-file research instruction overrides campaign and delivery
procedures. No numerical result, enumeration, audit, or external theorem is
used to discharge a mathematical statement.

**Unchecked (inherited inputs).** The source's assertions about existence of
class fills, their regularity (R3), the one-wall inverse, and the composite
constraint operators are research inputs to be distinguished below. Their
printed labels are not new verification here. The flat and pure-gauge
calculations in `fd-local.md` are the starting comparison, not a proof for a
curved background.

**Discharged (normalization).** Rescale the coarser leaf size \(S\) to one.
Write \(\epsilon=\eta/S\), \(\ell=1/L\), and

\[
 f(x)=S^2F_U(Sx),\qquad
 \|f\|_{4,B_1}=S\|F_U\|_{4,B_S}.
\]

An \(L^4\) norm on a fine lattice is

\[
 \|f\|_{4,E}=(\epsilon^4\sum_{p\in E}|f(p)|^4)^{1/4}.
\]

The same density convention applies to site and bond fields. A row at leaf
size \(\sigma\) has row density \(\sigma^4\), with the additional factor
\(\sigma^{-2}\) in `Lam`. Thus a bound for individual row entries, a bound
in the density-weighted row norm, and a bound on every contour are different
assertions.

Potentials rescale by \(\widetilde H(x)=S H(Sx)\), so the two sides
of (LC_U) are unchanged by this rescaling. Throughout this note
\(D_Uu(x,\nu)=\eta^{-1}[u(x)-\operatorname{Ad}_{U_\nu(x)}
u(x+\eta e_\nu)]\), with its density adjoint: these are the divided
differences in potential normalization used in the local mean test.
An angular difference is divided by its mesh before being used here.

**Unchecked (first attempted falsifier).** The first test is curvature
concentrated in one leaf, particularly on a thin set crossed by prescribed
contours. It must be checked against stationarity, compatibility, and the
actual (R3) supplier before it could refute \(LC_U\). A field with small
\(\|f\|_4\) alone is not an admissible counterexample. No such admission is
made by defining arbitrary frozen data after choosing the field.

**Unchecked (memory).** The perturbation-of-a-Gram-matrix and weighted
conjugation ideas are familiar methods recalled from memory. Every use
claimed below is accompanied by its elementary argument. No gauge-fixing,
trace, elliptic regularity, or discrete Sobolev theorem recalled from memory
is treated as discharged.

## 2. The concentrated-leaf attack and what (R3) actually says

**Discharged (the dangerous density, in the requested units).** Put all the
fourth-power mass in a fine leaf of side \(\ell=1/L\). Constant magnitude

\[
 |f|=a/\ell\quad\hbox{on volume }\ell^4
 \quad\Longrightarrow\quad
 \|f\|_4=a,\qquad \|f\|_2=a\ell.                 \tag{2.1}
\]

In particular the curvature density is \(La\), not \(a\). A bound on an
angle of a block of size \(\ell\) should be of order \(a\ell\), not of
order \(a\ell^2\). At a single finest plaquette the analogous calculation
is \(\epsilon^2|f_p|\leq\epsilon\|f\|_4\). These are density calculations;
they do not construct curvature of a connection.

**Discharged (why a tempting sheet is not a counterexample).** A formal
sheet with area \(\ell^2\), transverse thickness \(\epsilon^2\), and
magnitude \(a/(\ell\epsilon)^{1/2}\) has fourth norm \(a\), whereas its
surface sum is \(a\ell^{3/2}\epsilon^{-1/2}\). Thus restriction of an
arbitrary four-dimensional density to a prescribed two-dimensional sheet
has no such bound. But an abelian plaquette cochain supported on this
sheet, with a nonzero jump in a transverse direction and no other
components, has \(df\ne0\) on the transverse cubes. Since \(d^2A=0\), it
cannot be \(dA\). The nonabelian problem likewise has exact cube holonomy
identities. `composite-adjoint.md` explicitly withdraws its earlier sheet
example for this reason. This calculation refutes a density-to-trace
inference; it refutes neither (R3) nor \(LC_U\).

**Discharged (a stationary version of the first attack fails).** There is
a useful exact test in the commuting small-angle sector. Take \(U=e^{AZ}\)
with one fixed Cartan generator \(Z\), choose every logarithm in its small
branch, and keep all the original identity parents and frozen data. In this
sector the actual block map is linear on \(A\): products add angles and
the log-average averages them. Denote its complete constrained linear map
by \(Q\), including the frozen data. An attempted localized perturbation
with these data has \(QA=0\). If it were stationary, testing by the
admissible variation \(A\) would give

\[
 0=\langle Q^*\lambda,A\rangle
   =\sum_p(dA)_p\sin((dA)_p).                         \tag{2.2}
\]

For \(|(dA)_p|<\pi/2\), every summand is nonnegative and vanishes only
when \((dA)_p=0\). Consequently this candidate has zero curvature. Fixed
links contribute no term since \(A\) vanishes there. Positive action
normalization factors do not change the conclusion. Choosing the coarse
data to be \(QA\) instead removes \(QA=0\), but does not make an arbitrary
\(A\) stationary: the equation \(d^*\sin(dA)=Q^*\lambda\) still has to be
solved. Thus this test produces no admissible degenerating background.

**Unchecked (limits of that test).** Equation (2.2) excludes only the
commuting, small-angle, zero-data perturbation. Nonzero class data can
produce nonconstant stationary curvature. No assertion of uniqueness for
all admissible data, or exclusion of all counterexamples, follows from
(2.2). Large fine fields made stationary by freezing every link are not
the class-fill backgrounds in the question.

**Discharged (source content).** Mapped Text 5.3, (R3), concerns the
stationary lift near the smooth one-shot trial of (R1), constructed by
(R2). It supplies a local \(H^2\) estimate for the relative field in the
stated local Landau representation and a curvature \(L^4\) estimate.
It does not supply a pointwise fine-curvature estimate. The intermediate
angle estimate invoked in `fibre-propagator.md:192` is actually developed
in `composite-adjoint.md:85–96` (AD0). Its norm is

\[
 E_j=(\sum_{p\text{ at level }j}|\theta_p|^4)^{1/4},
 \qquad E_0=\epsilon\|f\|_4,\qquad
 E_j\leq2s_j\|f\|_{4,B^+}.                          \tag{2.3}
\]

Here the fixed box and its read enlargement must be retained. There is
no density factor \(s_j^4\) in \(E_j\). In particular (2.3) implies a
bound on *each blocked plaquette*. It is not a bound on each fine
surface spanning an arbitrary long fine path.

**Implication (the summation, including a concentration in one leaf).**
Write \(e_j=E_j/s_j\). The recurrence asserted in AD0 is

\[
 e_{j+1}\leq e_j(1+bL^{5/2}s_je_j),                 \tag{2.4}
\]

where \(b\) is a dimension-dependent constant from the one-step expansion.
Given (2.4), \(e_j\leq2e_0\) follows without a depth factor if

\[
 2bL^{5/2}e_0\sum_{j<m}s_j\leq\log2.
\]

Indeed the first index violating the bound would instead obey
\(e_m/e_0\leq\prod_{j<m}(1+2bL^{5/2}s_je_0)\leq2\).
For a nest ending at leaf size \(\sigma\),
\(\sum_{j<m}s_j\leq\sigma/(L-1)\). If a one-step contour ladder has at
most \(b_1L^2\) plaquettes, (2.3) therefore yields

\[
 \sum_{j<m}\alpha_j
 \leq 2b_1L^2\frac{\sigma}{L-1}\|f\|_4,
 \qquad \alpha_j:=b_1L^2\max_p|\theta_p^{(j)}|.
                                                               \tag{2.5}
\]

At the fine leaf this is at most \(4b_1a\) for \(L\geq2\); at the coarse
leaf it is at most \(4b_1La\). Both are small after \(L\) is fixed and
\(a_*\) is decreased. Neither requires the false bound \(|f|\leq a\).
This settles the powers and the absence of a depth factor in *this*
summation. It does not establish the transport comparison needed below.

**Discharged (what is not implied just by summing AD0).** A moment in a common fine
frame compares a path built from the blocked fields \(M^j(U)\) with a
path in \(U\). A blocked link is a log-average, not the holonomy of its
centre line. Differentiating a prescribed contour also produces loops
at its changes of level. Summing (2.5) for a single nested point is not
a proof of either comparison. In particular an unproved pointwise
fine axial-gauge bound cannot replace this step. The additional path
coarsening argument is given in Section 5.

## 3. A supported mean test; the Gram operator cannot be omitted

**Discharged (a useful way to avoid differentiating the prescribed comb).**
On a cubical fine block \(B\) of side \(\sigma\), choose a base site \(z\),
and let \(J_z(x)\) be adjoint transport from \(z\) to \(x\) along the
axis-ordered fine path. There is a choice of \(z\) for which

\[
 \|D_UJ_z\|_{2,B}^2\leq 2^{10}\sigma^2\|F_U\|_{2,B}^2.       \tag{3.1}
\]

Here the derivative is an operator from the three-dimensional colour
space, with its operator norm bounded by the estimates below; changing
to the sum over three basis vectors only enlarges the displayed constant.
To prove (3.1), compare the paths to \(x\) and \(x+\eta e_\nu\).
Their loop is the union of at most three strips, one cell wide, in the
planes \(\nu i\), \(i>\nu\). Successively removing their plaquettes and
using orthogonality of adjoint transport bounds the transport difference
by \(2\sum_p|\theta_p|\). Division by \(\eta\), followed by
Cauchy–Schwarz along a strip of length at most \(\sigma\), gives
\(4\sigma\sum_{p\text{ in strip}}\eta|F_p|^2\).
The squared sum over the at most three strips costs at most three.
Average this inequality over all base sites \(z\), and sum it over \(x\)
with density \(\eta^4\). For the strip in plane \(\nu i\), coordinates
before \(i\) are supplied by \(x\), coordinates after \(i\) by \(z\).
The unused coordinates cancel their averaging denominators. For its
remaining coordinate, each \(t_i\) lies between \(z_i,x_i\) for at most
all pairs, so

\[
 \operatorname{avg}_{z_i}\sum_{x_i}\eta
       \sum_{t_i\text{ between }z_i,x_i}\eta |F(t_i)|^2
 \leq\sigma\sum_{t_i}\eta|F(t_i)|^2.
\]

There are six choices \(\nu<i\). The resulting coefficient is at most
\(4\cdot3\cdot6\), before the harmless three-colour enlargement, and
is below \(2^{10}\). At least one \(z\) is no worse than the average.
This proves (3.1) by a finite sum, with no search or selection by a run.
For an interior tent, boundary derivatives only differentiate the tent;
extend \(J_z\) one edge where necessary. Its value outside the tent is
irrelevant. The finest site uses the site indicator directly.

**Discharged (what (3.1) does not say).** It selects an energy-controlled
fine frame. It says nothing about its orientation relative to the
source's *prescribed* composite contours. A gauge choice cannot set
those relative holonomies to the identity. This is exactly where the
transport comparison, rather than a bound on \(D_UJ_z\), remains needed.

**Implication (a precise sufficient comparison).** Use \(v_B=|B|=\sigma^4\)
and the density \(v_B\) on the site row. Write the actual site average as

\[
 r_Bu=\operatorname{avg}_{x\in B} A_B(x)u(x),
\]

where \(A_B(x)\) is the average of the adjoint transports over the actual
hierarchical contours. Suppose a root rotation \(O_B\) and the selected
frame \(J_B\) satisfy

\[
 \sup_{x\in B}\|A_B(x)J_B(x)-O_B\|\leq\delta,
 \qquad \delta\leq\tfrac14.                         \tag{3.2}
\]

Then, in the stated row density,

\[
 G_B:=r_Br_B^*=\operatorname{avg}_x A_B(x)A_B(x)^*,
 \qquad \tfrac9{16}I\leq G_B\leq I.                 \tag{3.3}
\]

For the lower bound, \(A_B(x)J_B(x)\) has smallest singular value at least
\(1-\delta\), and average the resulting quadratic inequality. The upper
bound follows because an average of orthogonal maps has norm at most one.
Thus the inverse is bounded by \(16/9\), independently of the number of
fine sites. Averaging transports does **not** make \(G_B=I\).

**Implication (the exact covariant mean identity).** Let \(p_B\geq0\) be
the tensor tent of mean one used in `fd-local.md`, supported in the
interior of \(B\). Put

\[
 M_B=\operatorname{avg}_x p_B(x)A_B(x)J_B(x),\qquad
 g_B(x)=\sigma^2p_B(x)J_B(x)M_B^{-1}c_B.             \tag{3.4}
\]

By (3.2), \(\|M_B-O_B\|\leq\delta\), so
\(\|M_B^{-1}\|\leq4/3\) and \(r_Bg_B=\sigma^2c_B\).
The scalar tent has supremum at most \(2^{16}\) and each derivative at
most \(2^{18}/\sigma\). From (3.1) and
\(\|F\|_{2,B}\leq\sigma\|F\|_{4,B}\), the product rule gives, for
\(\sigma\|F\|_{4,B}\leq1\),

\[
 \|g_B\|_2\leq K_m\sigma^2v_B^{1/2}|c_B|,
 \|D_Ug_B\|_2\leq K_m\sigma v_B^{1/2}|c_B|,
 \qquad K_m=2^{30}.                                 \tag{3.5}
\]

These constants also cover the finest indicator and its adjacent edges.
Set \(\phi=D_U^*H\), \(P=1-r^*G^{-1}r\), and
\(c_B=G_B^{-1}r_B\phi\). Orthogonal projection and summation by parts,
with the density \(v_B\) retained, give exactly

\[
 \sigma^2v_B|c_B|^2
 =\langle D_Ug_B,H\rangle-\langle Pg_B,P\phi\rangle.
                                                               \tag{3.6}
\]

Consequently

\[
 \sigma v_B^{1/2}|c_B|
 \leq K_m\bigl(\|H\|_{2,B^+}+\sigma\|P\phi\|_{2,B}\bigr).
                                                               \tag{3.7}
\]

This proves the needed mean estimate given (3.2), without differentiating
\(A_B(x)\). In particular the derivative of the prescribed hierarchical
kernel is not being asserted to have a bounded fine \(H^1\) norm.

**Implication (the projector commutator with its full support).** Write
\(\phi=P\phi+r^*c\). On a leaf, subtract a scalar constant \(\chi_B\).
The two parts of \([P,\chi]\phi\) are
\(P(\chi-\chi_B)r^*c\) and
\(-(1-P)(\chi-\chi_B)P\phi\). Projections are contractions and
\(\|r_B^*c_B\|_2\leq v_B^{1/2}|c_B|\). Thus

\[
 \|[P,\chi]\phi\|_{2,B}
 \leq\operatorname{osc}_B\chi
       (v_B^{1/2}|c_B|+\|P\phi\|_{2,B}).             \tag{3.8}
\]

Use \(\operatorname{osc}_B\chi\leq4c_\chi\sigma/(RS)\), (3.7),
\(\sigma\leq2S\), and the bounded edge overlap of disjoint leaves.
Summing squares gives the gauge term in \(LC_U\) with, for example,
\(2^{12}(K_m+1)^2c_\chi^2/R^2\) in front of its right-hand graph
expression. The block mean is controlled before the commutator is
estimated; replacing \(P D_U^*H\) by \(D_U^*H\) would bypass this issue.

## 4. The two-scale bond matrix and support bookkeeping

**Implication (the finite matrix test, not an infinite Neumann inverse).**
Let \(K=2^{120}\) be the deliberately loose flat bump constant of
`fd-local.md`. In each leaf use all its at most eight incident bond rows
and all three colour components. Test them on the twenty-four transported
flat bumps in the energy-controlled frame of Section 3, including zero
targets for incident rows assigned to a different leaf. Rotate the row
frames at their roots. A sufficient estimate is

\[
 \|\mathcal M_{B,U}-I\|_{\mathbb R^{24}\to\mathbb R^{24}}
 \leq 2^{12}K D(L)\,\sigma\|F\|_{4,B^{++}}
 \leq\tfrac14.                                      \tag{4.1}
\]

Here \(D(L)\) must bound both the transport comparison and the residual
of \(Q^o\) after its positive path part has been removed, in potential
normalization. The factor \(2^{12}K\) allows the twenty-four entries per
row, the signed tents' absolute moments, and the finite incidences. Given
(4.1), the series
\[
\mathcal M^{-1}=\sum_{q\geq0}(I-\mathcal M)^q
\]
converges in this *finite leaf matrix*, with norm at most \(4/3\).
It mixes only bumps in that leaf. Hence no inverse tail leaves the leaf.
Finest identity rows instead use their bond indicators directly, assigned
to their tails; no twenty-four-dimensional interior construction is
required in a one-site leaf. Their one-edge support and overlap are
included in the same bounds.
For periodic identifications, count endpoint occurrences rather than
distinct row names in this local matrix. If both endpoint blocks of
a row are the same physical leaf, split its unfolded kernel into its
two endpoint contributions, impose the desired moment in the assigned
occurrence and zero in the other, and then add them back. There are
still at most eight occurrences and twenty-four colour moments. The
two occurrences can have different root rotations, including a
nontrivial flat torus holonomy; each rotation is independent of the
point inside its copy of the leaf. Thus no global pure-gauge assumption
is hidden in the local comparison. These auxiliary moments create
no additional multipliers in the saddle.
Together with (3.1), and after making \(a_*\) smaller, the corrected
single-scale lift has mass and gradient bounds with \(2K\) in place of
\(K\). A global right inverse would not establish this support assertion.

**Implication (the curved kernel input, stated rather than hidden).** The
estimates needed along with (4.1) are that each row is supported in its
two endpoint blocks and that its absolute kernel obeys

\[
 |C_cH|\leq 2\sigma_c^{-2}\|H\|_{2,R_c},\qquad
 \sigma_c^{-2}|C_c((\chi-\chi_c)H)|^2
 \leq 2^{10}\frac{c_\chi^2}{(RS)^2}
                 \sigma_c^{-4}\|H\|_{2,R_c}^2.       \tag{4.2}
\]

The second follows from the first *for the absolute kernel*, since its
support has diameter at most \(8\sigma_c\). Cancellation in a signed
kernel is not sufficient. AD1 gives an explicit absolute majorant for
the one-step residual; AD0 supplies the proposed summation across its
levels. Section 5 rebuilds sufficient weaker bounds, allowing finite
constants depending on \(L\). No bound for arbitrary \(H\) is inferred
just from testing twenty-four bumps.

**Implication (density and the jump).** Given (4.2), multiply by the row
density \(\sigma_c^4\). The factor \(\sigma_c/(RS)\) from the cutoff
cancels the factor \(\sigma_c^{-1}\) from `Lam`. With at most eight
overlaps at each of the two scales, enlarging constants gives

\[
 \|C_U(\chi H)\|_{\Lambda}^2
 \leq 2^{15}c_\chi^2(RS)^{-2}\|H\|_{2,P^{++}}^2.   \tag{4.3}
\]

There is no factor \(L^4\) for the leaf concentration in (2.1).
Denote the exact supported single-scale inverses by \(R_f,R_c\), at
\(S/L,S\). The construction is

\[
 B_f=R_fq_f,\qquad B_c=R_c(q_c-C_cB_f),\qquad B=B_f+B_c.
                                                               \tag{4.4}
\]

Coarse leaf interiors meet no retained finer row. The coarse rows touched
by \(B_f\), including rows with initially zero error, are all included in
the second correction. If the density-normalized coarse row bound is at
most two, its off-diagonal norm in `Lam` is at most \(4K/L\): the mass of
\(R_fq_f\) is at most \(2K(S/L)\|q_f\|_\Lambda\), followed by the coarse
weight \(S^{-1}\). For \(L\geq16K\), (4.4) therefore has

\[
 S^{-2}\|B\|_2^2+\|\nabla_UB\|_2^2
 \leq K_b^2\|q\|_\Lambda^2,\qquad K_b=64K^2.       \tag{4.5}
\]

Only the assigned leaf and then the coarse neighbours touched by the
first correction are used; their row supports and leaves lie in the
specified \(32S\) enlargement. This is a two-step operation, not an
iteration over the total depth.

**Implication (constant budget for the proposed repair).** Equations
(3.8), (4.3), and (4.5) would establish \(LC_U\), for example with

\[
 A_{\rm loc}=2^{30}(K_b+K_m+1)^2c_\chi^2,            \tag{4.6}
\]

an absolute number. Choose the localization radius \(R\) using this
number and the one-wall constant, then \(L\geq16K\), and then \(a_*\)
small enough for AD0, (3.2), (4.1), and the form perturbation below.
Allowing \(D(L)\) in that last smallness condition is legitimate.
Allowing an uncontrolled depth factor there is not. Equations
(3.2), (4.1), and (4.2) are conditions of this implication; Section 5
establishes them before drawing the localization conclusion.

## 5. Coarsening the path before estimating its transport

**Discharged (finite one-step constants).** The constants in this paragraph
depend on \(L\), not on spacing or depth. Consider the one-step patches
consisting of the two endpoint blocks of a bond or the four blocks of a
plaquette, enlarged by two child blocks. In an axial gauge at a corner,
each edge log is bounded by \(cL^2\max|\theta_p|\): remove the plaquettes
of its coordinate strips one at a time. The estimate used is

\[
 \|I-A_1\cdots A_q\|\leq\sum_i\|I-A_i\|,              \tag{5.1}
\]

obtained by telescoping, with unitary or orthogonal factors. Choose \(r_L>0\)
so that all the finitely many links, loops and log-averages lie in the
logarithm ball of matrix radius \(1/4\) when the patch's fourth angle norm
is at most \(r_L\). The logarithm and exponential series, including their
first two derivatives, converge uniformly on the closed ball of radius
\(1/3\). The finite maps and those derivatives therefore have finite
maxima. Define \(b_L,q_L\geq1\) to be these maxima enlarged by the finite
entry counts, axial-gauge factors and patch incidences used below. This
defines constants by a stated existence argument; no computed value is
used. Their size is paid only by a threshold chosen after \(L\).

**Discharged (a version of AD0 sufficient here).** On the actual class
branch write, for the four sides of a parent plaquette,

\[
 \Omega_x^{(i)}=e^{v_x^{(i)}}\Omega_0^{(i)},\quad
 A_i=\operatorname{avg}_xv_x^{(i)},\quad
 V'^{(i)}=e^{A_i}\Omega_0^{(i)}.
\]

Couple contour choices at shared vertices when forming the product
\(W_x\); each side still has its prescribed averaging marginal.
The endpoint contours then cancel. Thus \(W_x\) is a conjugate of the
boundary holonomy of an
\(L\)-by-\(L\) child square \(S_x\), and successive plaquette removal gives

\[
 |\log W_x|\leq\sum_{p\in S_x}|\theta_p|.             \tag{5.2}
\]

The difference between \(\log\operatorname{hol}(P')\) and
\(\operatorname{avg}_x\log W_x\) vanishes to first order at the flat
field: the four averaged displaced-side terms are the same \(A_i\)'s
and the centre-square term is common. Taylor's formula with integral
remainder on the finite logarithm ball bounds that difference by
\(b_LE_j(Q)^2\). The bound for axial-gauge link logs by \(E_j(Q)\) is
included in \(b_L\). This retains the centre-square term; it does not
bound that term by the displaced-side angles alone.

The linear fourth-norm constant is exactly \(L\). Indeed
\(w(P',p)=L^{-4}\#\{x:p\in S_x\}\) has row sum \(L^2\) and column sum
\(L^{-2}\). For the latter count, the two transverse coordinates fix
the block and start, while in each longitudinal coordinate there are
exactly \(L\) starts over all coarse blocks. Weighted Jensen gives

\[
 \sum_{P'}\left(\sum_pw(P',p)|\theta_p|\right)^4
 \leq L^6\sum_{P',p}w(P',p)|\theta_p|^4
 =L^4\sum_p|\theta_p|^4.                             \tag{5.3}
\]

Restricting the output plaquettes only decreases the column sum.
The nonlinear remainders have fourth norm at most \(b_LE_j^2\), after
enlarging \(b_L\) for the fixed overlap of \(Q\). This follows from
\(\sum_Q E_j(Q)^8\leq(\max_QE_j(Q)^4)\sum_Q E_j(Q)^4\).
Consequently

\[
 E_{j+1}\leq LE_j+b_LE_j^2,\qquad
 e_{j+1}\leq e_j(1+(b_L/L)s_je_j).                   \tag{5.4}
\]

For leaves of size at most two in \(S=1\) units, the bootstrap in
Section 2 proves

\[
 a\leq a_0(L):=\min\{r_L/8,\ 1/[100(1+b_L)]\}
 \quad\Longrightarrow\quad E_j\leq2s_ja.             \tag{5.5}
\]

At each stage use the backward read set of all paths and rows being
estimated. One step expands it by a fixed multiple of \(s_{j+1}\);
the sum of those lengths is bounded by a fixed multiple of the leaf
size. Restrict the initial fourth norm to that full fine read set.
The column-count inequality above applies unchanged to such restricted
outputs. Thus this argument uses the norm on an enlarged box, never
only the norm on the leaf holding the concentration.

**Discharged (the one-step open-path identity).** At level \(j\), replace
the vertices of a coordinate path by their parent-block centres and
insert the prescribed centre-to-vertex contours. The adjacent inserted
contours cancel exactly in the product. A path portion inside one
block becomes a closed loop. A portion crossing to an adjacent block
becomes a path between the centres. Compare it first to the centre line
and then to the actual blocked link \(e^A\Omega_0\).

Each local comparison uses at most \(c_1L^2\) plaquettes. To see the area
bound, commute its coordinate segments past each other; a swap of two
perpendicular unit steps removes one plaquette. There are at most eight
segments, each of length at most \(2L\). Also
\(|A|\leq\operatorname{avg}|v_x|\leq c_1L^2\max|\theta_p|\).
The loose value \(c_1=2^{12}\) covers these counts and conversion to
adjoint norm. By (5.1) the local replacement error is therefore at most
\(c_1L^2E_j(Q)\). No fine surface is estimated by a four-dimensional
norm in this step: the surface is in a fixed finite one-step lattice.

**Discharged (the gain for a long path).** A fine coordinate path of at
most eight segments and length at most \(16\sigma\) projects to at most
eight coordinate segments. Along a segment its block index changes
monotonically in one coordinate. At scale \(s_j\leq\sigma\) it meets at
most \(2^{10}\sigma/s_j\) blocks. The two-block patches along each segment
have bounded overlap; corner repeats cost at most eight. Hölder yields

\[
 \sum_{Q\ {\rm along\ path}}E_j(Q)
 \leq c_2(L)(\sigma/s_j)^{3/4}E_j
 \leq2c_2(L)\sigma^{3/4}s_j^{1/4}a.                 \tag{5.6}
\]

For example \(c_2(L)=2^{20}L^4\) overcounts all child incidences and
rounding. It is deliberately not optimized. Finally

\[
 \sum_{j<m}s_j^{1/4}
 \leq \frac{\sigma^{1/4}}{L^{1/4}-1}.                \tag{5.7}
\]

Replacing the fourth-norm sum in (5.6) by a maximum would lose this
gain and could cost a constant per level. The concentrated-leaf
configuration (2.1) satisfies exactly the same Hölder bound.

**Discharged (the endpoint identities).** Let \(x_j\) be the successive
ancestors of a fine site. In coarsening an open path from the leaf root
to that site, all inserted interior contours cancel. The only endpoint
factors left after all the steps are
\(\Gamma_{x_m,x_{m-1}}\cdots\Gamma_{x_1,x_0}\), evaluated in their
respective blocked fields. These are precisely the paths in the
composite site average. The projected path at the last level is
constant. Coarsen a fine path from the root to \(z\) and then to \(x\);
it has at most eight segments, so (5.6)–(5.7) compare the prescribed
hierarchical transport to the frame \(J_z(x)\).

For the positive bond-path kernel the same cancellation has one extra
prefix. At one step its path is a centre-to-start contour followed by
a prefix of the straight line in the bond direction. The chosen child
bond lies on that line. On replacing the prefix by the contour to that
bond's block centre, the difference is a local loop, and a single
coarse bond remains if the prefix has crossed the block face. At the
next step that bond extends the next prefix by one edge. Thus the
replacement is repeated with a prefix ending at either endpoint of
the selected child bond. There is at most one such carry at each
level, since the line crosses only the two endpoint blocks. The
positive path part preserves the bond direction. It introduces no
branching or growing number of prefixes. Each replacement has the
two-block area bound of the preceding paragraph. At the top the
remaining path is the identity or the fixed bond from the row root
to the assigned endpoint leaf. It can be put into a row rotation
\(O_{cB}\), independent of \(x\) inside that leaf.

This is also valid for each allowed ordering of contour axes:
the inserted contour is that very ordering, and the local loop still
has the same length/area bound. Average afterwards. With \(J_z(x)\)
viewed as a map from the frame at \(z\) to the fine frame at \(x\),
both the site and bond path kernels therefore obey

\[
 \|T_{c,x}J_z(x)-O_{cB}\|
 \leq d_L\sigma a,\qquad
 d_L=1+\frac{2^{20}L^2c_2(L)}{L^{1/4}-1}.            \tag{5.8}
\]

The extra bounded endpoint loops sum by
\(\sum_{j<m}E_j\leq2\sigma a/(L-1)\) and fit in this constant.
The estimate holds for every \(z\), hence for the energy-controlled
choice in (3.1). It makes no pointwise bound on that gauge's connection.

**Discharged (the residual row norm, including absolute kernels).** Write
\(Q_j^o=P_j+\mathcal E_j\). In potential and density normalization, the
scalar absolute kernel of \(P_j\) has norm at most one: it has the flat
positive path weights, and Jensen with their row and column densities
proves the contraction. The residual is zero at a flat field.
Integrating the finite first-derivative bound defining \(q_L\), entry
by entry in the axial gauge above, gives

\[
 \big\|\,|\mathcal E_j|\,\big\|_{N_j\longrightarrow N_{j+1}}
 \leq q_LE_j.                                      \tag{5.9}
\]

Absolute bars denote the matrix of colour-coefficient norms, before
cancellation. The finite entry count, the change to potential
normalization, and the number of incident one-step patches are included
in \(q_L\). Rescaling a one-step patch changes neither that matrix norm
nor \(q_L\). Gauge changes multiply its colour entries by orthogonal
maps, so the estimate is frame independent.

Expand the composite product of \(P_j+\mathcal E_j\) and bound every term
by its absolute kernel. If \(2q_L\sigma a/(L-1)\leq1/4\), its residual
has norm at most

\[
 \prod_{j<m}(1+q_LE_j)-1
 \leq 2q_L\sum_{j<m}E_j
 \leq \frac{4q_L\sigma a}{L-1}.                      \tag{5.10}
\]

The elementary inequality \(e^t-1\leq2t\), \(0\leq t\leq1/2\),
follows by the exponential series. Forgetting transports in the
composite of the \(P_j\)'s leaves exactly the flat box/triangle kernel.
Its row \(L^2\) norm is at most \(\sigma^{-2}\). Extracting one row of
density \(\sigma^4\) from (5.10) costs \(\sigma^{-2}\). This proves
(4.2) and the density-normalized bound of two used in (4.4), after
requiring (5.10) to be at most \(1/4\). The supports remain the two
endpoint blocks throughout composition.
For the density-normalized operator on a whole retained scale, use that
the path part is a contraction and that the residual row supports
overlap at most eight times. A row residual at most
\(\sigma^{-2}/4\) therefore gives an operator residual at most
\(\sqrt8/4<1\). This verifies the bound of two used at the jump;
a pointwise row bound alone would not have verified it.

**Discharged ((LC_U), on its stated background domain).** Equation (5.8)
gives (3.2). On a signed bond bump its path-moment error is at most its
absolute scalar moment times \(d_L\sigma a\). Its residual moment is
bounded by (5.10) times the bump's \(L^2\) norm. Thus (4.1) holds with

\[
 D(L)=1+d_L+4q_L/(L-1).
\]

Let \(C_b\) be the absolute conversion from the stated local hypothesis
\(S\|F\|_{4,B_S}\leq Ca_*\) to the norm on the fixed fine read
enlargement in (5.5). It includes the stated \(C\) and the fourth root
of the fixed number of unit boxes; it is independent of depth, volume,
\(L\), and \(R\). All comparisons above fit inside a fixed enlargement
of the one leaf or two endpoint leaves, not the whole radius-\(R\)
patch. The following sufficient threshold covers \(\sigma/S\leq2\):

\[
 C_ba_*\leq\min\left\{
 a_0(L),\ \frac{L-1}{32(1+q_L)},
 \frac1{2^{16}KD(L)},\ \frac1{4d_L},\ \frac12
 \right\}.                                         \tag{5.11}
\]

Now (3.3)–(3.8) and (4.3)–(4.5) prove (LC_U), with
\(A_{\rm loc}\) in (4.6), independent of \(L\).
Support can also be checked without a norm estimate. A row meeting
\(P\) has its assigned leaf within \(2\sigma\) in maximum distance.
After the fine correction, a touched coarse row and its assigned
leaf add at most another \(4S\); the one-edge derivative margin adds
at most \(S\). Everything lies within \(P+[-8S,8S]^4\), hence within
\(P^+\). Every input row read is inside \(P^{++}\).

Choose \(R\) from (4.6) and the one-wall constant before choosing
\(L\geq16K\). Then impose (5.11), decreasing it further if needed for
the later form estimates. This gives the permitted \(a_{\rm loc}(L,R)\).
The argument uses the actual class branch and its local \(L^4\)
curvature bound. Stationarity supplies that bound at the intended
backgrounds; it is not an extra estimate used inside this linear
localization proof.

## 6. Admission of the background, including the heavy wall

**Discharged (which hypotheses the proof reads).**

| Hypothesis actually read | Use here | Stated supplier; limit |
|---|---|---|
| Actual class branch, prescribed short contours, no rough rerouting or Haar branch | Finite maps, endpoint cancellation, positive path kernel in Section 5 | Mapped Text 3.1 and the class branch in Text 5; AD1 gives the one-step formula |
| \(S\lVert F_U\rVert_{4,B_S}\leq Ca_*\) on every read box and enlargement | (3.1), (5.5), and (5.6) | Mapped Text 5.3 (R3), at the stationary lift supplied by (R1),(R2); (NC) states its local-scale use |
| Compatible pruned leaves and the actual endpoint-block rows | Exact zero finer moments, correction, support | The whole-block frozen/free construction in F-D and fd-jumps Sections 3–4 |
| Stationarity for the actual constraints | Not needed inside (LC_U) once the preceding hypotheses hold; needed for the multiplier/Hessian calculation below | The defining stationary class fill, not an arbitrary fine field |

**Discharged (what is not read).** The proof of (LC_U) reads no raw
fine-energy cap, heavy-shell gain, pointwise fine-curvature bound, or
\(H^2\)-to-\(L^\infty\) assertion. An Eps ball alone is insufficient:
it does not supply (5.5). The input from (R3) is the curvature fourth
norm, not an assumed trace theorem.

**Gap (the stage's supply is not repaired).** For a globally class top
without frozen data, (R1)–(R3) are the stated background supplier.
For arbitrary quiet frozen histories, quiet-boundary-rarity uses ST,
the junction response estimate and (QD) to identify a small stationary
fill. Heavy-wall Section 5 and hw-thick Section 5 leave the stage
construction/non-concentration beside a heavy wall conditional.
Section 5 here proves an estimate **if** its local curvature bound
and class branch are supplied; it does not produce such a fill for
every quiet datum. Application to those histories therefore still
reads an output which the failed stage was intended to supply,
through admission to the class-fill/R3 domain. There is no additional
heavy-wall term inside (LC_U). The heavy-wall counterfields are not
silently admitted as stationary class fills.

## 7. Top collars and the interface's layer width

**Discharged (complete families, including width \(6t_0\)).** Keep the
front conditions (N),(B) of quiet-boundary-rarity. Enlarge the outside
layer to all bricks within \(6t_0\) of its front. Brick rounding puts
its points within \(7t_0s_l\) of \(E_l\). Their parents are within

\[
 (2/3)t_0+7t_0/L+2                                  \tag{7.1}
\]

of \(E_{l+1}\), in level-\((l+1)\) cells. The inner margin from
\(E_{l+1}\) is at least \(3t_0s_l\), up to a fixed cell-rounding
allowance. For \(L\geq64,t_0\geq32\), (7.1) is below \(7t_0/8\).
It fits even in a \(t_0\)-wide upper layer with positive margin,
and hence in its \(6t_0\)-wide enlargement. Allowing rounding and
the factor four between lattice and maximum metrics leaves

\[
 F_l+[-t_0s_l/4,t_0s_l/4]^4\subset F_{l+1}.          \tag{7.2}
\]

Here each complete family's top has its specified upper region,
and \(F_l\) is the union of the layers. Unions preserve (7.2)
pointwise. For the separate interface margin choose conservatively
\(t_0\geq4r_SL\), retaining \(w=6t_0>d_f\) and \(r_SL>d_f\).
Also choose \(t_0\geq10^4RL^2\), as in fd-local. The order of constants
permits these fixed choices after \(L,a_*\), before depth and data.

**Gap (a recursively truncated top).** If a new family ends at \(t\),
the required test is

\[
 \Sigma_t^{\rm new}+[-t_0s_t/4,t_0s_t/4]^4
       \subset F_{t+1}^{\rm old/current}.            \tag{7.3}
\]

There is no \(E_{t+1}^{\rm new}\) to which (N),(B) apply. When the
current problem's whole domain is fixed at level \(t+1\), that domain
supplies (7.3), provided the new layer has the stated distance from
its boundary. Otherwise the older frozen region must supply it.
Quietness is a field condition and supplies no distance. The junction
paragraphs and start/restore rules read here do not verify (7.3) for
every recursively admitted datum in \((I_l^{\mathfrak d})\).
Changing \(t_0\) to \(6t_0\) does not fill a missing upper region.

**Discharged (domain conclusion).** A family satisfying the interface's
full definition already includes its top clearance. It passes when
(7.3) is part of that admission. A truncated object cannot be admitted
solely from its lower (N),(B) pairs. This is a producer/domain
verification still owed, not a counterexample to (LC_U). The cover
and several-jump implication below apply to (7.2), including (7.3)
at every truncation, with the enlarged width. No source has been
changed to declare that its recursive data meet these conditions.

## 8. The Hessian error, including its multiplier

**Discharged (the local Hölder estimate).** No Sobolev theorem from
memory is needed for this exponent. For a compactly supported lattice
scalar \(v\), telescoping in coordinate \(i\) bounds \(|v(x)|\) by
\(A_i(\widehat x_i)=\sum_{t_i}\eta|D_iv|\). Repeated Hölder gives

\[
 \sum_x\eta^4\prod_{i=1}^4A_i(\widehat x_i)^{1/3}
 \leq\prod_{i=1}^4
       \left(\sum_{\widehat x_i}\eta^3A_i\right)^{1/3}.
\]

To check that particular use, integrate coordinate four with exponents
\(3,3,3\), separate \(A_4^{1/3}\) by exponents \(3,3/2\), and apply the
three-function version to the remaining factor. That version follows
by Cauchy–Schwarz first in coordinate three, then in coordinates one
and two. Hence \(\|v\|_{4/3}\leq\frac14\sum_i\|D_iv\|_1\).
Set \(v=|H|^2\). Link transport is orthogonal, so
\(|D_i|H|^2|\leq(|H|+|H(\cdot+\eta e_i)|)|\nabla_{U,i}H|\).
Cauchy–Schwarz proves, with room,

\[
 \|H\|_{8/3}^2\leq8\|H\|_2\|\nabla_UH\|_2.           \tag{8.1}
\]

A tensor cutoff equal to one on a box of side \(S\), zero outside
its fixed enlargement, and with derivatives at most \(4/S\), gives

\[
 \|H\|_{8/3,B_S}^2\leq C_SS
       \left(S^{-2}\|H\|_{2,B_S^+}^2+
                         \|\nabla_UH\|_{2,B_S^+}^2\right).       \tag{8.2}
\]

One may take \(C_S=2^{20}\) in the summed estimate, allowing the tensor
cutoff and at most \(5^4\) overlaps. The proof is valid for finite
lattice sums. Periodic local boxes use the same cutoffs.

**Discharged (graph comparison on a one-wall patch).** Sum (3.7), with
the bounded adjacent-edge overlap, and use the two leaf scales. It gives

\[
 \|(1-P)D_U^*H\|^2\leq2^{10}K_m^2
       \left(L^2S^{-2}\|H\|^2+\|PD_U^*H\|^2\right).             \tag{8.3}
\]

Summation by parts in curl squared plus divergence squared produces
gradient squared and commutators of covariant differences. Each
commutator is a shift times
\(\eta^{-2}(\operatorname{Ad}U_p-I)\), bounded by \(2|F_p|\).
There are at most four directions and six plaquette types. Bound
their products by Hölder and (8.2), including the fixed shifts.
For \(2^{30}C_ba_*\leq1/4\), absorb the gradient term. For supported
localized fields this yields

\[
 S^{-2}\|H\|^2+\|\nabla_UH\|^2\leq C_G(L)G_P(H)^2,
 \quad C_G(L)=2^{40}(K_m+1)^2L^2,                    \tag{8.4}
\]

where \(G_P(H)^2=S^{-2}\|H\|^2+\|d_UH\|^2+\|PD_U^*H\|^2\);
all enlarged supports are included. This does not replace \(S\) by
the finer wall scale with an absolute constant.

**Discharged (Wilson curvature error).** Differentiating the four
plaquette exponentials twice gives their transported-leg square
plus an error bounded by
\(2^8|\theta_p|\sum_{b\in\partial p}\eta^2|H_b|^2\).
Indeed at \(U_p=1\) the sixteen ordered leg pairs combine to the
square. Replacing \(U_p\) by the identity in each pair costs at most
its matrix distance, bounded by \(|\theta_p|\); \(2^8\) also covers
the colour and trace normalizations. Use \(\theta_p=\eta^2F_p\),
sum the finite incidences, and apply (8.2),(8.4). The error is at
most \(C_AC_ba_*C_G(L)G_P(H)^2\), with \(C_A=2^{30}\) sufficient.
It has the desired form, with no pointwise-curvature substitution.

**Implication (stationarity gives the local multiplier bound).** Assume
the actual stationary equation \(DA=C_U^*\lambda\) for the pruned
constraints. Test with the supported right inverse of a single row
of side \(\sigma\), with unit row value. Its gradient norm is at
most \(K_b\sigma\) in \(S=1\) units. The first variation and
Cauchy–Schwarz bound its pairing by
\(C\|F\|_{2,\operatorname{supp}B^+}K_b\sigma\).
The support has bounded coarser-scale volume. Including the row
density \(\sigma^4\) therefore gives

\[
 \sigma^3|\lambda_c|\leq C_\lambda a_*,
 \qquad C_\lambda=2^{20}C_bK_b.                      \tag{8.5}
\]

This reads stationarity for these constraints. Curvature alone, or
stationarity for a different functional, does not supply (8.5).

**Implication (the constrained second jet).** Use the source's smooth
contour-free chain \(N\), with derivative \(Q^o\), and its stationary
Hessian
\(\mathfrak bH=D^2A-\langle\lambda,D^2N\rangle\).
The one-step second jet is a finite analytic map on the logarithm ball:
\[
 |b_j[\theta,\theta](c)|
 \leq b_{2,L}\sum_{b\in R_c}|\theta_b|^2 .
\]
Define \(b_{2,L}\) by the finite second-derivative maximum as in
Section 5. The adjoint positive path part decreases a pointwise
angular multiplier by \(L^{-3}\): a child bond lies on \(L\) of
the \(L^4\) lines in total, including endpoint translates.
The residual costs at most \(q'_LE_j\) in this finite norm.
Its relative product is bounded by
\(\prod_j(1+L^3q'_LE_j)\leq2\), on decreasing \(a_*\) after \(L\).

In a leaf rescaled to size one put \(t_j=s_j/\sigma\).
The forward field has density norm at most twice the input norm,
by (5.9)–(5.10). The backward multiplier is at most
\(2t_{j+1}^3\Lambda\), where
\(\Lambda=\sigma^3|\lambda_c|\). In the chain rule the level-\(j\)
second-jet contribution is consequently at most

\[
 c_L\Lambda\,t_{j+1}^3t_j^{-2}\|H\|_2^2
 \leq c_LL^3\Lambda\,t_j\|H\|_2^2.                   \tag{8.6}
\]

The factor \(t_j^{-2}\) converts the squared angular field to its
potential density norm. Summation costs \(1/(L-1)\), not depth.
In physical coordinates the result is
\(C_J(L)a_*\sigma^{-2}\|H\|_{2,R_c}^2\).
One may define \(C_J(L)\) as \(C_\lambda\) times the finite
second-jet/incidence constant in (8.6) times \(4L^3/(L-1)\).
Only two row scales meet a localized patch. Their endpoint-block
overlap is bounded, and \(\sigma^{-2}\leq L^2S^{-2}\). Therefore

\[
 |\mathfrak bH[H,H]-\|d_UH\|^2|
 \leq C_{\rm form}(L)a_*G_P(H)^2,
 \quad C_{\rm form}(L)=C_AC_bC_G(L)+2^8L^2C_J(L).     \tag{8.7}
\]

This establishes the requested error form when the stationary
equation and the identification of the actual constrained Hessian
with this chain Hessian are supplied. It includes its multiplier.
The latter identification is the source's class/Ward input; this
calculation does not substitute curl squared for the actual Hessian.
For the adjoint product, a sufficient additional threshold is
\(C_ba_*\leq (L-1)\log2/[8L^3(1+q'_L)]\).
Take the minimum of this threshold, (5.11), the absorption threshold
in (8.4), and the form threshold below when defining
\(a_{\rm loc}(L,R)\). All are chosen after \(L,R\).

## 9. Several-jump F-D: the precise implication and its absolute rate

**Implication (domain and inherited inputs).** Take any finite pruned
leaf hierarchy with (7.2), including every truncated top, whole parent
blocks, the enlarged interface width, and
\(t_0\geq10^4RL^2\). Supply actual compatible class-fill backgrounds
with the local curvature hypothesis everywhere read. Supply the
one-wall coercivity constant \(C_0\), absolute as in fd-local, and
the actual constrained-Hessian/class identification and Ward identity.
The following deduction establishes the several-jump inverse on that
domain. It does not certify that every history in the boundary
induction belongs to this domain.

**Implication (coercivity with all constants chosen in order).** Let
\(W=\|H/h\|^2\), \(E=\|d_UH\|^2+\|P_ND_U^*H\|^2\), using fd-local's
size function and cover of total overlap \(N=16^4\).
The local correction is now (LC_U), and scalar covariant product
rules cost only the Lipschitz constant of the cutoff. The flat IMS
calculation in fd-local Section 4 therefore applies with
\(e=A_{\rm loc}N/R^2\), enlarged by an absolute factor for the finite
curl/divergence incidences. Choose, explicitly,

\[
 R^2\geq2^{20}(1+C_0)A_{\rm loc}N,\qquad
 C_{\rm form}(L)a_*\leq[100(1+16C_0)]^{-1}.          \tag{9.1}
\]

The terms to absorb are at most \((4C_0+1)eW\); the coefficient of
\(E\) is at most \(8C_0+4C_0e\). Thus \(W\leq16C_0E\) on
\(\ker C_N\), and the actual gauge-fixed Hessian is coercive there
with a constant at least
\(c=[2(1+16C_0)]^{-1}\) in the norm \(W+E\).
The absolute domination used in Section 8, summed over this cover,
also bounds the form on this whole space after enlarging
\(C_{\rm form}(L)\) by fixed overlap factors.

**Implication (global inf-sup without a depth factor).** Under the
strengthened collar, the two-block support of a retained row of side
\(\sigma\) contains leaves of size only \(\sigma\) or \(\sigma/L\).
Indeed a further refinement wall would have to be within \(2\sigma\)
of its coarse leaf, whereas (7.2) separates it by at least
\(t_0\sigma/(4L^2)>2\sigma\). At each point at most two adjacent
active row scales occur. Same-scale endpoint supports have bounded
overlap.

Use the leaf inverses of Section 4 simultaneously, calling the map
\(R_0\). Its squared gradient and weighted mass bounds sum over disjoint
leaf interiors, with bounded adjacent-edge overlap. Thus
\(\|R_0q\|_{W+E}\leq C_R\|q\|_\Lambda\), where \(C_R=2^{12}K_b\)
is sufficient. Its row matrix is \(C_NR_0=I+T\). The off-diagonal
part raises scale by just one level and has norm at most \(4K/L\),
by the density calculation following (4.4). Outputs at different
levels are orthogonal in the direct-sum row norm, so the same bound
holds for \(T\), without summing over levels. For \(L\geq16K\),
\[
 R=R_0(I+T)^{-1},\qquad \|R\|\leq2C_R.               \tag{9.2}
\]
The inverse series terminates on a finite hierarchy, and its norm
is bounded by its geometric majorant independently of the depth.
Its possible global tails do not replace the compact construction
used for (LC_U).

**Implication (which graph norm is used in this proof).** Write
\(\mathcal G^2=W+E\) for an auxiliary stronger norm and
\(G^2=\|H\|^2+E\) for the source's unweighted top-unit graph norm.
Since \(h\leq1\), \(G\leq\mathcal G\). This distinction is necessary:
curvature near a fine sheet need not give a uniformly bounded form
on all of the unweighted \(G\) space. The proof first inverts in
\(\mathcal G\), then uses
\(\|J\|_{\mathcal G^*}\leq\|J\|_{G^*}\) and \(G\leq\mathcal G\)
to obtain the claimed inverse bound. It does not assert an
unproved uniform equivalence of these norms.

Let \(K_N=\mathfrak bH+D_UP_ND_U^*\), with form norm at most two
on \(\mathcal G\), after (9.1). For data \(C_NH=y\), first lift
\(Ry\), then solve for \(h=H-Ry\in\ker C_N\). Minimizing its strictly
positive finite quadratic form gives
\[
 \|h\|_{\mathcal G}\leq
 c^{-1}(\|J\|_{\mathcal G^*}+4C_R\|y\|_\Lambda).
\]
The remaining functional \(J-K_NH\) vanishes on \(\ker C_N\);
its multiplier norm is bounded by applying it to \(R\), hence by
\(2C_R(\|J\|_{\mathcal G^*}+2\|H\|_{\mathcal G})\).
These facts prove invertibility of the saddle, with for example
\[
 M=10(1+4C_R)^2(1+c^{-1})                           \tag{9.3}
\]
as an absolute inverse bound. No bound independent of \(L\) for the
raw constraint operator was required.

**Implication (conjugation and the fast rate).** Conjugate on fine
fields by \(e^f\), and on a row by \(e^{f(z_c)}\), with
\({\rm Lip}(f)\leq\delta\leq1/10\) in top units. Each row kernel
acquires a factor bounded by \(C\delta\sigma_c\), since its support
diameter is \(2\sigma_c\). This cancels its \(\Lambda\) weight.
The two-active-scale overlap just proved and (4.2) bound this
commutator by an absolute constant times \(\delta\|H\|_2\).
The curl and divergence commutators have the same bound by their
product rules. For \(P_N\), (3.7)–(3.8), now applied to the relative
exponential on each leaf, give
\(C(K_m+1)\delta(\|H\|+\|P_ND_U^*H\|)\).

Finally the curvature and second-jet errors in Section 8 were
bounded by absolute values of their local bilinear coefficients.
Their endpoints are separated by at most the row diameter, at most
two top units. Inserting the exponential difference costs at most
\(C\delta\) in the same bound. By (9.1) its coefficient is absolute.
Thus the full conjugation error on
\(\mathcal G\times\Lambda^*\) is at most \(C_{\rm com}\delta\),
where \(C_{\rm com}\) is an absolute finite sum of these displayed
product, overlap and mean-test constants. Set
\[
 \delta_\#=\min\{1/10,\ (4MC_{\rm com})^{-1}\}.        \tag{9.4}
\]
A geometric-series inversion then bounds the conjugated inverse
by \(2M\), independently of \(L\), depth and volume.

**Implication (actual form of the conclusion).** With
\[
 \mathcal S_N=
 \begin{pmatrix}K_N&C_N^*\\ C_N&0\end{pmatrix},
 \qquad
 \|y\|_\Lambda^2=\sum_c\sigma_c^4\sigma_c^{-2}|y_c|^2,
\]
the result is
\[
 \|e^f\mathcal S_N^{-1}e^{-f}\|_
 {\,G^*\times\Lambda\ \longrightarrow\ G\times\Lambda^*}
 \leq2M,\qquad {\rm Lip}(f)\leq\delta_\#.             \tag{9.5}
\]
For a source annihilating fine gauge directions and zero constraint
right-hand side, the supplied Ward identity makes the solution obey
\(P_ND_U^*H=0\): test by \(D_U\omega\), \(\omega\in\ker r_N\), then
use the positive operator \(P_ND_U^*D_UP_N\) on that space. Its
kernel consists of covariantly constant fields with zero covariant
leaf means, hence is zero. The class/chart identification then gives
\[
 |M_Y^{-1}(i,j)|\leq C(L)e^{-\delta_\# d(i,j)},        \tag{9.6}
\]
including opposite walls and along a wall. The chart may put \(L\)
in the prefactor. The exponent (9.4) stays absolute.

**Implication (exact consumer content; other inputs remain owed).**

| Consumer | What (9.5)–(9.6) supply, on admitted backgrounds and collars |
|---|---|
| \((MD^*_1)\) | The class-integral covariance kernel across its middle third, with an absolute fast exponent. HS-P, perturbation control, the gas, FILL and the two-tier induction are still separate inputs. The factor \(C(L)x_1\lvert A\rvert^P\) is allowed; an arbitrary \(L\)-dependent fast exponent is not. |
| \((I_2^{\mathfrak D})\) | Coercivity after the chart, with amplitude/coercivity constants depending on \(L\), and its (H2) response at an absolute rate. It does not supply the class fill, (7.3), the Laplace/gas estimates or the remainder induction. |
| \((SCR_1)\) | Through MD*, rarity and the stated history-law argument, an envelope with an absolute \(a_f>0\). F-D alone is not a screening or probability statement. |
| K-transport | After that SCR bound, \(2B_j\Phi_j(k_m)+3\sqrt{\tau_j(m)}\), with the square root halving the fast exponent and changing \((z_j^{\rm cut})^{1/2}\) to \((z_j^{\rm cut})^{1/4}\). It does not turn a slow unsuppressed term into the rare tier. |

**Discharged (why a weaker rate would not answer the question).** If
one only obtained \(\|\mathcal S_N^{-1}\|\leq M(L)\), the above
perturbation proof would allow only
\(\delta\leq[2M(L)C_{\rm com}]^{-1}\).
For \(\delta(L)<\kappa\), no finite prefactor changes
\(e^{-\delta(L)d}\) to a bound by \(e^{-\kappa d}\) at unbounded
distances: their ratio grows as \(e^{(\kappa-\delta(L))d}\).
Increasing \(x_*\) cannot fix that. The auxiliary norm and the
absolute constants in (9.1)–(9.4) are what avoid that loss here.

## 10. Decision and reading boundary

**Discharged (the local result).** Equations (3.1)–(5.11) give a written
proof of (LC_U) for its actual class-branch, local-\(L^4\) background
hypotheses, with the original support requirement and order of choices.
The two Gram conclusions are \(9I/16\leq r_Br_B^*\leq I\) and inverse
norm at most \(4/3\) for each normalized finite bond-moment block.
The transport bound is obtained by coarsening and fourth-norm counting,
not by restricting an arbitrary curvature density to each fine path.
No admissible stationary counterexample was found; the rejected
sheet and zero-data attempts have their precise failures in Section 2.

**Implication (limit of the several-jump result).** Section 9 gives the
absolute-rate several-jump F-D implication on the explicitly admitted
domain, with the inherited one-wall and Hessian/Ward inputs stated.
It does not establish all the producer's recursively quantified
instances: the class-fill supply beside a heavy wall and the top
inclusion (7.3) remain conditional. Thus this note does not claim
\((MD^*_1)\), \((I_2^{\mathfrak D})\), \((SCR_1)\), or K-transport as
newly established. The terminal decision refers to the requested
local inequality; the downstream qualifications are part of it.

**Discharged (source and verification record).** Read GOAL and the
three prescribed FINISH sections first. Scientific reads were bounded
excerpts of fd-local (Sections 1–6 and 8), fibre-propagator (setting,
form, F-D, (NC), and hostile point (6')), the block energy package
(setting, Lemmas 1–4 and Theorems 6–7), composite-adjoint (AD1, AD0
and composite estimates), mapped Text 3.1, Leaf-Q, (H1) in the ball,
(R1)–(R3), and its constant order; heavy-wall Section 5 and its
consumer discussion; hw-thick Section 5 and the stated smaller target;
quiet-boundary-rarity (setting, layers, region data, exploration,
induction statement, MD*, boundary bulk step); fd-jumps (the operator,
pruned leaves, and row commutator); joint-induction-two-step's dependency
table; and the upper-chain interface, layer statement and two-tier
profile. Some initial searches returned long or truncated lines;
load-bearing statements were then read in bounded ranges.
An upper-chain range also displayed its historical comparison in
20.1; none of that comparison is a proof input here.

**Discharged (limits).** No forbidden file or gate was opened. No
external proof account, literature theorem or numerical result supplies
a discharged step. The installed physics-loop procedure was read for
applicability; its campaign and delivery actions were not invoked.
The repository methodology was read at the pinned commit. No audit,
subagent, commit, push, PR, post or computational mathematical check was
performed. Source inspection, editing and final scope/format inspection
are not mathematical certificates. This is author research and grants
no scientific status.

PROVED
