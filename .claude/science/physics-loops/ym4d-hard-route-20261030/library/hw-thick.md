# Thick collars and the wall excess inequality
Provenance: OpenAI Codex; configured model `gpt-6-astra`, effort `max` (local configuration, not a runtime attestation); commit `b5d9827c73ed1dc0336961be6bd76149a091896c`; 2026-11-01; research text, not an audit, granting no status.

## 1. Scope and accounting

**Unchecked — source boundary.** This is the mapped-side investigation of
`heavy-wall.md` Section 5 requested by the owner. Source claims are not proved
by their labels. No result recalled from memory is a premise: the elementary
calculations used below are written out. No numerical, search, enumeration,
or formal-checker run supplies a mathematical step. The checkout is the
specified pin. Only this file is written.

**Discharged — definitions and the relevant quantifier.** Fix the stage
constants in their prescribed order, a finite volume, depth, quiet frozen
data, a class top, and an admissible chain \(U\). Write \(\mathcal O(U)\) for
the *allowed operations*: a triggered core, a permitted sparse or dense
collar within clearance, its specified small target, and an actual
replacement preserving the top and every frozen datum and removing the
selected defect. Include enlargements and unions wherever the stage allows
them; do not fix the core before the existential quantifier. For an operation

\[
 G=A_U(D)-A_{T_D}(D),\qquad
 R=A_X(D)-A_{T_D}(D)+A_X(D^c)-A_U(D^c),
 \qquad A(U)-A(X)=G-R.                         \tag{1}
\]

The last identity is subtraction of the same plaquette partition. An
unchanged exterior, however energetic, contributes zero. The recursion needs
uniform positive \(\eta,c_R\) such that

\[
 \forall U\ [\text{a stage trigger remains}\ \Longrightarrow
 \exists o\in\mathcal O(U):\ G_o>0,\quad
 A(U)-A(X_o)\geq\eta G_o+c_RT^2n_o].           \tag{HW-ex}
\]

For the full non-concentration conclusion, "trigger" includes the original
fine-energy and density triggers. A replacement of only coarse rough cells
has a weaker conclusion. The number \(n_o\) counts original rough cells
removed for the first time, including lower levels. Positive gain at one
arbitrarily prescribed core is a stronger demand than (HW-ex).

**Discharged — what a refutation must exclude.** To refute (HW-ex), for each
putative uniform choice of constants one must exhibit an admissible triggered
chain for which *every* allowed operation fails (1)'s payment. A bad prescribed
target mixture does not suffice if another core, enlargement, or removable
component pays. The identity operation pays nothing when \(G>0\); it can be
chosen when there is no trigger, or one can leave a proposed non-triggered
core untouched and operate elsewhere. It cannot be used to terminate a
triggered stage. These distinctions also apply to an epsilon-competitor
formulation, after epsilon tends to zero.

## 2. Hand check of the antipodal calculation

**Discharged — the core calculation of `hw-fine.md` Sections 5–6.** In the
unit-quaternion coordinates of SU(2), direct matrix multiplication gives
\(\tfrac12\operatorname{Re}\operatorname{tr}(r q^{-1})=r\cdot q\).
Take \(m\geq9\) divisible by 3. Put \(\alpha=\pi/m\),
\(q_y=\cos(y\alpha)e_0+\sin(y\alpha)e_3\),
\(\phi_y=\sin(y\alpha)\), and \(\delta_y=r_y-q_y\), with
\(r_0=q_0=e_0,r_m=q_m=-e_0\). Expanding
\(E(r)=\sum_{y=0}^{m-1}(1-r_y\cdot r_{y+1})\), using
\(2q_y\cdot\delta_y=-|\delta_y|^2\) and the sine/cosine recurrences, gives

\[
 E(r)-m(1-\cos\alpha)
 =\cos\alpha\sum_{y=1}^{m-1}|\delta_y|^2
       -\sum_{y=1}^{m-2}\delta_y\cdot\delta_{y+1}
 =\frac12\sum_{y=1}^{m-2}\phi_y\phi_{y+1}
       \left|\frac{\delta_{y+1}}{\phi_{y+1}}
                    -\frac{\delta_y}{\phi_y}\right|^2.       \tag{2}
\]

Both semicircles minimize. Requiring the opposite one at \(i=m/3\) and
the original one at \(k=2m/3\) fixes the displayed quotients to
\(-2e_3,0\). Their difference has squared norm 4. On this interval
\(\phi_y\phi_{y+1}\geq3/4\), and there are \(m/3\) edges. Weighted
Cauchy–Schwarz therefore gives
\(4\leq(2\Delta E)(4m/9)\), or

\[
                         \Delta E\geq 9/(2m).             \tag{3}
\]

This is a lower bound against nonabelian chains too, and sums over independently
retained chains. The algebra does not require a small-angle approximation.

**Discharged — limitation of this calculation.** The two endpoint actions
are equal plaquette by plaquette, so their \(G_D\) is zero for every
plaquette set \(D\). Formula (2) applies to free longitudinal links with
the transverse links retained as in that note. It does not prove constrained
minimality when those transverse links may also move. The actual HW collar
at \(j\geq1\) is clear of lower frozen layers: coarse frozen bonds are
constraints on parents, not a declaration that all these fine transverse
links are fixed. Thus (3), by itself, has neither the domain nor the positive
credit required in (HW-ex).

## 3. Trying to transplant the frustration

**Discharged — width and multiplicity must be compared with credit.** The
explicit interpolant in hw-fine has cost per chain
\[
 (m/3)(\cos\alpha-\cos3\alpha)
 =(2m/3)\sin2\alpha\sin\alpha\leq4\pi^2/(3m).       \tag{4}
\]
Together with (3), this sandwiches that obstruction between constants times
the inverse transition width. For \(C\) retained chains and added core
credit \(g\) per chain, the comparison is between \(C/m\) and \(Cg\):
increasing \(C\) alone changes no ratio. Thickening the transition while
holding \(g\) fixed helps payment. If \(g\) also changes, it must be recalculated;
there is no conclusion from thickness alone. In particular, comparing an
interface cost with zero excess says nothing about a dense trigger with a
different, flat target.

**Discharged — an exact escape when the transverse bonds become free.** Use
the same profile and notation as the antipodal example, with odd \(L\geq9\)
divisible by 3 and \(m\) large enough that \(15L\alpha<\pi\):
\(f(x)=1,-1,0\) at residues \(1,-1,\text{other}\) modulo \(L\),
\(d_x=f(x+1)-f(x)\),
\(U_1=\exp(d_xs(y)Z)\), and all other links identity. Let
\(\Delta s(y)=s(y+1)-s(y)\), so \(|\Delta s|=\alpha\).
Choose any \(0\leq\chi(y)\leq1\), equal to zero on the proposed core's
whole enlarged strip and to one outside a clear strip. Define
\[
 X_1=U_1,\qquad
 X_2(x,y,z,w)=\exp\{f(x)(1-\chi(y))\Delta s(y)Z\},
 \qquad X_3=X_4=1.                              \tag{5}
\]
Multiplication of the four links of a \((1,2)\) plaquette gives
\[
 X_p=\exp\{-d_x\chi(y)\Delta s(y)Z\}.             \tag{6}
\]
Every other plaquette is identity. There is **no** term involving
\(\chi(y+1)-\chi(y)\): the added connection and this variation of the
cutoff are both in direction 2. Since cosine decreases on \([0,\pi]\),
\(a_p(X)\leq a_p(U)\) for every plaquette. All core plaquettes are flat.
An arbitrarily narrow or thick transition works; a wide one is allowed.

**Discharged — exact parents in this escape, for the specified all-lines map.**
The common gauge \(g(x,y)=\exp(f(x)s(y)Z)\) has value 1 at every first-block
centre. It turns (5) into
\[
 X_1^g=1,\qquad X_2^g=\exp\{-f(x)\chi(y)\Delta s(y)Z\},
 \qquad X_3^g=X_4^g=1.                           \tag{7}
\]
For the reflection-symmetric all-lines contours specified in the mapped
source, the straight direction-2 average vanishes because \(\sum_x f(x)=0\).
The rooted contour average vanishes by reflection of \(x\), which changes
the sign of \(f\) and preserves the other factors and contour ordering.
The other straight averages vanish. Each rooted contour or straight piece
has phase magnitude at most \(5L\alpha\), and the whole parent path at most
\(15L\alpha<\pi\), so these are actual logarithms, not a linearization.
Thus each first parent is identity, as are all later parents. Choose
\(\alpha<T\) within the all-lines label region. The same statements hold
for \(U\) and \(X\); no rough branch is invoked. Equation (5) leaves the
fine field unchanged wherever \(\chi=1\), and leaves every parent unchanged
everywhere. Consequently it keeps all coarse frozen data exact; it also
keeps fine frozen data exact if its strip misses them.

**Implication — a legal flat-wall transplantation has a paying operation.**
Place this strip in the lower-layer-free part of a planar frozen level-
\(j\) wall, with identity frozen data and identity top. Use full periodic
tangential sections; no internal retained fine faces are inserted. This is
compatible with the planar nested-layer geometry and clearance stated in
energy-by-stages (CL); that geometry is a supplied stage input here.
For identity fine frozen data as well, put the whole triangular \(s\)-profile
of length \(2m\) inside the clear strip and extend \(s=0\) outside it on a
larger compatible torus. Choose the clearance large enough for this profile
and the operation's margins. Its consecutive differences still have magnitude
at most \(\alpha\), and the parent cancellation above is unchanged.
If the dense-cluster convention requires the larger connected band as
core, take \(\chi=0\) through that whole band and its read margin; (6)
still gives no interface increase. The complete profile was placed within
clearance precisely so this larger operation is available too.
Taking the zero set of \(\chi\) to include the trigger's support enlargement
removes its fine-energy trigger. The flat core field in (5) is a gauge of
identity by a gauge equal to identity at block centres, so it has the same
zero target action and correct parents as the flat small target. HW requires
removal of the defect and the cost (1), not equality to one chosen fine gauge
representative of that target. For this operation
\[
             G=A_U(D)>0,\qquad R\leq0,\qquad n=0.        \tag{8}
\]
Hence it pays, for example, with \(\eta=1/2\). A dense trigger can be
obtained without rough plaquettes: for an aligned fine cube of side
\(B=L^j\) in a linear part of the chain, its action is
\((4B^4/L)(1-\cos(\pi/m))\). Fix \(m/B=L^q\) large enough for the
strip and allowed collars, then increase \(j\). The lower bound
\(1-\cos t\geq2t^2/\pi^2\), obtained by concavity of sine on
\([0,\pi/2]\), makes this at least \(8B^2/L^{2q+1}\), while
\(\alpha\) tends to zero. Identity data are quiet because identity is an
admissible zero-action reference. This is an escape from this proposed
refutation, not a proof for other exterior fields.

**Discharged — why two other additions do not repair this counterexample.**
If an independently removable compact component with an identity boundary
collar is added, deleting that component is an allowed competing operation
whenever its support fits an allowed core. Its removal cannot be forbidden
merely because a different core has been nominated. Similarly, if a proposed
obstruction is entirely contained in a larger allowed core with an identity
collar and identity constraints, replacing that whole component by identity
removes its full action. Rough-cell payment must still be checked; these
observations assert the available action decrease, not a universal bound on
the count of rough cells.

**Gap — arbitrary frustrated exterior remains an actual issue.** A candidate
Dirichlet minimizer driven by an exterior oscillation could obstruct a
prescribed local operation. To refute (HW-ex), one would have to prove its
minimality against all nonabelian fine variations with the actual parent
constraints, keep a genuine trigger after quietness and clearance are
imposed, and exclude enlarged cores which remove the driving oscillation.
Fixing an artificial fine boundary around each proposed core would assume
exactly what the stage does not impose. No such configuration is obtained
here. Equations (5)–(8) explicitly rule out that strategy for the unmodified
antipodal profile once its transverse links are free. Neither this failed
refutation nor a failed search proves (HW-ex).

## 4. A restricted HW theorem, with a relative coercivity estimate

**Implication — exact scope of the theorem.** The following is a commuting
SU(2) theorem in one coherent chart, with explicit additional hypotheses.
It is not asserted for every stage field. Write
\(T_b=\exp(Zt_b)\), \(U_b=\exp(Z(t_b+v_b))\), with real bond cochains
\(t,v\). Write \(f_p=(dt)_p\), \(z_p=(dv)_p\), using the oriented
plaquette coboundary. Thus the Wilson action is exactly \(1-\cos(f_p+z_p)\).
The hypotheses are:

1. **Geometry.** The core's enlarged read support is inside an axis-aligned
   cube \(I\); its collar has width \(wB\) in fine units, where \(B=L^j\).
   No lower frozen layer meets this collar or its one-plaquette margin.
   Set \(\chi(x)=\min(1,\operatorname{dist}_\infty(x,I)/(wB))\) at vertices
   and \(\chi_b=\chi(x)\) on a positive bond starting at \(x\).
   Enlarge \(I\) to include the selected defect's read neighbourhood.
   Let \(D\) be its internal plaquettes and \(H\) all other changed
   plaquettes. In particular \(\chi_b=0\) on every edge of a plaquette
   of \(D\), \(\chi_b=1\) outside the collar, and
   \(|\chi(x+e_\mu)-\chi(x)|\leq1/(wB)\).
2. **Actual constraints and target.** On the fields used here the relevant
   fixed-label block maps have the same real, unwrapped logarithm branches,
   so the prescribed top and frozen data are affine constraints \(Ca=c\)
   on the real connection. Both \(t\) and \(t+v\) have these data, and
   \(C(\chi v)=Cv=0\). The resulting field
   \(X_b=\exp(Z(t_b+\chi_bv_b))\) has an admissible chain, with all fixed
   data exact, and its target core removes the selected trigger.
   These are explicit restrictions: the theorem does not construct a
   nonlinear constraint-restoring correction or infer admissible labels
   from a linearized constraint.
3. **Stationarity and small chart.** The target satisfies
   \(\sum_p\sin f_p\,(da)_p=0\) for compactly supported allowed variations
   \(Ca=0\) in this patch. For \(p\in D\cup H\),
   \(|f_p|,|f_p+z_p|\leq\rho\), with
   \(\rho^2\leq1/(8M)\), where \(M\geq1\) is fixed.
4. **Relative normalization in the collar.** Let \(H_b\) contain the shifted
   bonds entering the cutoff error in (11) below. They are covered by
   rectangular column boxes of length at most \(B\) in direction 1.
   In the *same* real connection \(v\), \(v_1=0\) throughout these boxes,
   and \(v_\nu=0\), \(\nu>1\), on each box's initial direction-1 face.
   Let \(H^+\) contain their \((1,\nu)\) plaquettes and \(H\). Each
   plaquette is used by at most \(P\geq1\) boxes. This is a condition on
   relative traces, not permission to impose new frozen fine faces.
5. **Relative shell and target budgets.** With the actual
   \(G=A_U(D)-A_T(D)>0\),
   \[
      \sum_{p\in H^+}|z_p|^2\leq MG,\qquad
      \sum_{p\in D}|f_p|^2\leq G/144.                  \tag{9}
   \]
   There is no bound on action outside this patch.
6. **Width and rough-cell reserve.** Take
   \(w\geq32\sqrt P\,M\), with this width inside the allowed collar and
   clearance, and \(T^2n\leq M_RG\) with a fixed \(M_R\geq1\).

Under these hypotheses, \(X\) satisfies HW with
\[
                   \eta=\tfrac12,\qquad c_R=\frac1{8M_R}.
                                                               \tag{10}
\]
If \(P,M,M_R\) are absolute, these constants and the required width have
no dependence on depth. Every extra hypothesis is part of this restricted
statement; none is attributed to quietness alone.

**Discharged — relative displacement estimate under hypothesis 4.**
For a tangential bond at column coordinate \(q\leq B\), axial normalization
gives \(v_\nu(q)=\sum_{r=0}^{q-1}z_{1\nu}(r)\).
Consequently
\(|v_\nu(q)|^2\leq B\sum_{r=0}^{B-1}|z_{1\nu}(r)|^2\).
Summing over the at most \(B\) column positions and then boxes, with
the stated multiplicity, gives
\(\|v\|_{H_b}^2\leq PB^2\|dv\|_{H^+}^2\).
This explains exactly the relative trace restriction doing the work.
Neither small plaquettes alone nor parent equality is substituted for it.

**Discharged — relative coercivity and uniqueness near the small target.**
Define
\[
 b_p(z)=1-\cos(f_p+z)-(1-\cos f_p)-(\sin f_p)z.
\]
Twice integrating the second derivative gives
\(b_p(z)=z^2\int_0^1(1-s)\cos(f_p+sz)\,ds\).
If both endpoints lie in \([-\rho,\rho]\), the interval between them
does too, and
\[
       \tfrac12\cos\rho\,z^2\leq b_p(z)\leq\tfrac12z^2.
\]
Here \(\cos\rho\geq1-\rho^2/2\geq1/2\); the first inequality follows
by integrating \(|\sin u|\leq|u|\). The upper bound holds for every
real \(z\), even outside the chart. For a compactly supported relative
variation \(v\) with \(Cv=0\), stationarity cancels its full linear term:
\[
 \tfrac14\|dv\|^2
 \leq A(T\exp(Zv))-A(T)
 \leq\tfrac12\|dv\|^2.                            \tag{RC-small}
\]
If the column normalization covers the whole support, the left side
also bounds \(\|v\|^2/(4PB^2)\). Thus a normalized stationary target is
the unique minimizer in this convex commuting chart. More explicitly,
two stationary normalized connections in the chart have action derivative
difference paired with their difference at least
\(\tfrac12\|d(v_1-v_2)\|^2\); stationarity makes it zero, and the
column inequality makes \(v_1=v_2\). This is not uniqueness among
nonabelian competitors or among connections outside that chart.

**Discharged — the mixed plaquette cost, with constants.** On
\(p=(x;\mu,\nu)\), \(\mu<\nu\), direct expansion gives
\[
 d(\chi v)_p=\chi(x)z_p+\beta_p,\qquad
 \beta_p=[\chi(x+e_\mu)-\chi(x)]v_\nu(x+e_\mu)
       -[\chi(x+e_\nu)-\chi(x)]v_\mu(x+e_\nu).
                                                               \tag{11}
\]
Each positive bond occurs in these shifted terms for at most three
orientations. Squaring a sum of two terms costs at most 2. Hence
\[
 \|\beta\|_H^2
 \leq\frac6{(wB)^2}\|v\|_{H_b}^2
 \leq\frac{6P}{w^2}\|z\|_{H^+}^2.
                                                               \tag{12}
\]
This is the width-based interface cost. The factor \(B^2\) in the
relative displacement estimate cancels the fine width's \(B^2\).

**Discharged — the nonlinear Wilson remainder is included.** Set
\(\delta=1/(16M)\). The inequality
\((a+b)^2\leq(1+\delta)a^2+(1+\delta^{-1})b^2\)
follows from \((\sqrt\delta a-b/\sqrt\delta)^2\geq0\).
Apply it to (11), then apply the upper and lower bounds on \(b_p\):
\[
 \begin{split}
 \sum_H[b_p(d(\chi v)_p)-b_p(z_p)]
 &\leq \frac{\delta+\rho^2/2}{2}\|z\|_H^2
       +\frac{1+\delta^{-1}}2\|\beta\|_H^2\\
 &\leq \frac{G}{16}
       +\frac{51PM^2}{w^2}G
 <\frac G8 .
 \end{split}                                                   \tag{13}
\]
The second term uses \(3(1+16M)M\leq51M^2\).
The strict last inequality follows from \(w^2\geq1024PM^2\) and
\(51<64\). Thus no small-angle equality or discarded fourth-order
Wilson term is hidden in (13).

**Discharged — the target's linear term and the final reserve.** Put
\(L_D=\sum_D(\sin f_p)z_p\), \(q^2=\sum_Dz_p^2\), and
\(a^2=\sum_Df_p^2\). Then
\[
 G=L_D+\sum_D b_p(z_p)\geq q^2/4-aq\geq q^2/8-2a^2.
\]
The last inequality is \((q/\sqrt8-\sqrt2a)^2\geq0\).
By (9), \(q^2\leq(8+1/9)G<9G\), so \(|L_D|\leq aq\leq G/4\).
The supported variation \(a_b=(\chi_b-1)v_b\) is in \(\ker C\).
Target stationarity therefore says that its linear contribution on
\(H\) is \(L_D\), since on \(D\) it is \(-L_D\).
The replacement equals the target on \(D\); unchanged plaquettes outside
\(D\cup H\) cancel exactly. Consequently
\[
 R=L_D+\sum_H[b_p(d(\chi v)_p)-b_p(z_p)]
 \leq3G/8
 \leq(1-\tfrac12)G-\frac{T^2n}{8M_R}.             \tag{14}
\]
This proves (10). Every mixed plaquette, the signed target term, the
Wilson remainder and the rough-cell reserve have been included. Exact
restoration has zero cost only because hypothesis 2 explicitly guarantees
it for this particular cutoff.

## 5. What the stage does and does not supply

**Discharged — the geometric match is only partial.** The stage's clearance
allows fine links under a coarse frozen wall to move while lower data stay
fixed. A cubical collar of a permitted width can therefore meet hypothesis 1.
It does not impose the relative zero traces of hypothesis 4, a common
commuting chart, or \(C(\chi v)=0\). A frozen coarse bond constrains a
parent average, not each fine connection along its support. The cancellation
in (7) supplies the latter equality for that special field, not for a
general cutoff of two fields with equal parents.

**Implication — one coefficient budget is compatible with dense
target sizing.** If the supplied target estimate is
\(A_T(D)\leq C_{\rm tar}T^2|D|\), the dense trigger is
\(A_U(D)\geq KT^2|D|\), and the target has the small real angles assumed
in Section 4, then \(\sum_D f_p^2\leq4A_T(D)\).
Indeed the same double-integration bound at \(f=0\) gives
\(1-\cos f_p\geq f_p^2/4\). Thus \(K\geq577C_{\rm tar}\) implies
\(\sum_D f_p^2\leq G/144\). This is an order-of-constants choice before
\(L\), provided \(C_{\rm tar}\) is absolute. It supplies neither the
target-existence theorem nor the relative shell bound in (9).

**Gap — admission to the restricted theorem.** Quietness (QD) controls the
frozen level-\(j\) data. It supplies no bound on
\(\|dv\|_{H^+}^2/G\) for a non-minimizing fine \(U\), no normalized relative
connection on the actual collar, and no uniform inverse for correcting
\(C(\chi v)\). Enlarging a collar until a raw tail is small is not a
depth-uniform substitute: an estimate of the form
\(E_{\rm inner}\leq C T^2+q^w E_{\rm outer}\), \(0<q<1\), has no uniform
consequence from a fixed allowed \(w\) when \(E_{\rm outer}\) is unbounded.
This is arithmetic about that estimate, not a counterexample to the true
minimizing field. The reserve \(T^2n\leq M_RG\), counting first removals
over all lower levels, likewise needs its own argument. These restrictions
are not claimed to be logically independent.

**Implication — the exact no-loss recursion if the hypotheses could be
supplied at every required operation.** Suppose the stage can repeatedly
apply (14), always with one absolute \(M_R\) independent of \(L\), depth
and freeze history, until its level-\(j\) output
\(W^+\) is class, and can do so for every remaining original trigger.
Let \(U^-\) be that output fine field, \(B_j=\sum_oG_o\) and
\(N_j=\sum_on_o\). Actual action differences telescope:
\[
 A(U)-A(U^-)\geq\tfrac12B_j+\frac{T^2}{8M_R}N_j.
\]
With the *same* lower frozen data in the two reference functionals, exact
parents and regularity of \(W^+\) give the variational inclusion
\(\Phi_{j+1}(W)\leq\Phi_j(W^+)\). Subtracting the references yields
\[
 \Xi_{j+1}(U)\geq\tfrac12B_j+
                  \frac{T^2}{8M_R}N_j+\Xi_j(U^-).       \tag{15}
\]
The coefficient of \(\Xi_j\) is exactly 1. First-removal assignment gives
\(\sum_jN_j=\sum_{k<i}|R_k|\) if every original rough cell is eventually
removed. For termination, also retain the trigger/target lower bound
\(G\geq g_0T^2\) with \(g_0>0\): for example the dense bounds above give
\(g_0=K-C_{\rm tar}>0\) on a nonempty box core. After \(N\) operations
the decrease is at least \(Ng_0T^2/2\), so nonnegativity of action bounds
\(N\leq2A(U)/(g_0T^2)\). Merely asserting \(G>0\), without such a lower
bound or a separate limiting argument, would not prove termination.
Equation (15) has no error per depth and no multiplication of \(1/2\)
through successive depths. The present note does not supply its stated
coverage premise.

**Gap — consequence for the named consumers.** This work neither proves
nor refutes (AE-R). If (15)'s coverage premise held, its class-top form would
follow with \(a_R=1/(8M_R)\); the rough-top term would still require the
separate paid-top construction. A Corollary excluding *all* concentration
requires payment for fine-energy and density triggers, not just coarse rough
cells. The restricted result does not provide that Corollary. LOC-V still
has its explicit a priori lower-stage cell-energy cap and exact gluing
hypotheses in lift-nonlinear Section 4; (RC-small) cannot replace them for
an arbitrary heavy field. For (UP), the class-minimizer identification,
fine-flux control and nonlinear weighted seam estimate remain separate
inputs. The algebraic implications through shell comparison and WAM are
unaffected. Even a successful unweighted HW repair would not establish
the required weighted absorption
\(2A_s(L)M_*(L)\sinh(\nu_{\rm req}r(L))<1\).
A larger dense radius must be checked at the required spatial rate;
an additive loss at every depth cannot be hidden in (15).

## 6. A strictly smaller inequality at which this investigation stops

**Gap — the flat free-side curl lift (FCL).** Here is one concrete remaining
probe, without the nonlinear heavy exterior or the rough-cell accounting.
Use a flat wall made of whole level-\(j\) blocks. Coarse centres with
first coordinate nonnegative are on its frozen side; the physical interface
is the common face between their blocks and the free blocks. A fine bond is
allowed if it is not wholly inside the frozen union. Work at the identity,
with no lower frozen layer in the patch. Fix a coarse cube \(Q\) of side
four adjacent to the wall, measured in level-\(j\) units.

Let \(Q_j\) be the *full* linearization at identity of the specified
all-lines composite map, in bond-logarithm normalization. One step is
\[
 (Q^{[\ell]}H)(y,y')
  =\operatorname{avg}_{x\in B(y)}
       \left[\operatorname{avg}_{\Gamma_{y,x}}\sum_\Gamma H
             +\sum_{[x,x']}H
             -\operatorname{avg}_{\Gamma_{y',x'}}\sum_\Gamma H\right],
 \qquad Q_j=Q^{[j-1]}\cdots Q^{[0]}.
\]
The contours and averaging are those of mapped Text 3.1; no contour-free
operator is silently substituted. Let \(h\) be a real coarse bond cochain,
zero off \(Q\) and on every bond wholly on the frozen side. Extend \(h\)
by zero when computing its coarse curl. The proposed estimate is: there
exist absolute finite \(r_0,C\), independent of \(j,B=L^j,L\) and volume,
such that
\[
 \inf_{\substack{Q_jH=h\ {\rm on\ all\ coarse\ bonds}\\
       \operatorname{supp}H\subset
          \operatorname{shadow}(Q^{+r_0})\cap
                      \{\text{allowed fine bonds}\}}}
             \ \sum_{\text{fine }p}|dH(p)|^2
       \ \leq\ C\sum_{\text{coarse }p}|dh(p)|^2.          \tag{FCL}
\]
The infimum of an empty fibre is infinity. Both sums include plaquettes
crossing the support boundary. Three Lie-algebra components just give
three copies of this real inequality. This asks for a supported lift;
an exponentially decaying unrestricted lift is a different statement.

**Discharged — its zero-curl test for exact gradients.** If
\(h=d\varphi\), with \(\varphi=0\) at frozen centres and off \(Q\), put a
fine site function \(\omega=\varphi\) at level-\(j\) centres and zero at
all other fine sites, and take \(H=d\omega\).
Every rooted path sum telescopes to its endpoint values, so
\(Q_jd\omega=d\varphi=h\). Its fine curl vanishes on every plaquette,
including boundary plaquettes. Its support is within one fine lattice
step of the free centres, hence inside the allowed block union for
\(B\geq9\), with the prescribed margin. Thus (FCL) has no obstruction
from these exact-gradient inputs. This construction does not bound
the transverse part of a general \(h\).

**Gap — the precise unsuccessful step.** Truncating a full-space lift
creates both a curl term \(d\chi\wedge H\) and a nonzero parent error
\(Q_j(\chi H)-h\). Correcting each row by a bump can pay a norm of
\(h\), whereas (FCL) asks for its curl and must give zero for exact
gradients. It also has to use only free fine bonds while keeping
*all* outside parent rows zero. A positive fraction of free lines is
not a proof of this simultaneous supported curl bound.
The compact full-patch construction in lift-nonlinear Section 3
does not establish this free-side version; its straddling bumps and
support restriction would have to be rebuilt for this domain.
No depth-uniform construction for the general transverse input is
proved here.

**Unchecked — expectation, with a reason.** I expect (FCL) to be true for
this flat whole-block geometry. The exact-gradient test above works
without action cost, and the remaining averaging weights on the free
portion of an interface block have macroscopic support rather than the
thin retained faces of the antipodal example. This suggests a local
curl-compatible interpolation with matched block moments. It is a reason
to try that construction, not a coercivity proof or evidence about the
arbitrary-background nonlinear inverse.

**Discharged — why this is strictly smaller, and what solving it would do.**
(FCL) is one linear quadratic inequality at the identity, on one flat
wall and one fixed-size patch. It has no nonlinear plaquette remainder,
arbitrary background connection, choice of a triggered core, small-target
existence, rough-label changes, first-removal reserve, or stage iteration.
It is a smaller subproblem for the *free-side construction*, not a
restatement of a bound on \(R_D\). Nor is it claimed to be logically
necessary for existential HW: an operation crossing the wall or a final
minimal-lift argument could bypass it. Proving (FCL) would remove a
specific linear support obstruction to that construction; it would not
by itself supply Section 4's missing stage hypotheses or prove HW.
Refuting (FCL) would kill this particular free-side lifting plan, not
(HW-ex), (AE-R), or the global route.

## 7. Decision and reading boundary

**Gap — decision.** No admissible configuration refuting the existential
operation quantifier has been established. The actual antipodal profile
admits the paying transverse relaxation (5) once transplanted with free
fine transverse bonds; multiplication of that profile does not defeat it.
The restricted commuting theorem (10) is proved, including its relative
coercivity and every term of its collar cost, but the stage does not
supply its hypotheses. It therefore cannot be reported as a proof of
the recursion's HW. The smaller unresolved inequality singled out for
continuation is (FCL), with the expectation and limitations just stated.
This is a stopping point for this investigation, not an impossibility
theorem or an assertion that the listed approaches exhaust the routes.

**Unchecked — coverage.** GOAL and the three requested FINISH sections
were read first. Scientific reading was restricted to bounded ranges and
locating excerpts of heavy-wall (in particular Sections 4–6), hw-fine
(Sections 5–6 and its scope), energy-by-stages (setting, QD, stage,
restoration and recursion), lift-nonlinear (LIFT-NL, LOC-V and support
claims), paid-inputs-frozen-energy (layer geometry), quiet-boundary-rarity
(quiet data and nested layers), mapped Text 1, 3.1 and 5.1–5.2,
block-poincare-energy-package (setting and operator statements),
lattice-uhlenbeck (setting and Lemma U), active-energy-excess-contract
(Section 1), excess-shell-end (the UP statement), and support-related
locating excerpts of analytic-lift and fibre-propagator. Those source
proofs are not generally certified by this note. Procedure files absent
from the sparse checkout were read at the pin; the planning AGENTS file
was read as instructions only. No prohibited independent-side file or
gate, forbidden library file, external account, or literature proof was
read. No remembered theorem, numerical run, enumeration or computer
certificate discharges a mathematical assertion here. No other worktree
file was edited; no audit, commit, push, PR, post or subagent was used.

STOPPED
