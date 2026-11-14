# A3: the depth-uniform local regularity profile
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort are not exposed; requested effort: max); repository commit `1ddede8fb5da70ea56d528637c22ee0092d22b70`; Sussman–Alpoge commit `31a47c543775`; T. Balaban, CMP **102** (1985), 277–309, and CMP **99** (1985), 389–434; research text, not an audit, granting no status.

## 1. Scope, sources and the statement being tested

Queue row 84 concerns the shared nonlinear A3 obstruction in
`route-decisions.md` §§1, 4.2: the first half of (1b) Theorem 2 of the
[pinned Sussman–Alpoge outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
The outline's definitions, target and proposed local improvement are due to
**Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of
their text**. Balaban supplies the underlying regular-critical-orbit and
propagator programme. Attribution does not prove an input.

The source was fetched once to `/tmp/sa_ym4.tex`; SA line numbers below
refer to that pinned text. Balaban's papers are read in the owner's
`~/ym4d-papers/` folder and are not copied into the repository. Rows 81
and 82 remain cited-pending inputs wherever their conclusions are used.
No computation discharges a mathematical assertion.

For a separated determining sequence, put
\(\eta=L^{-k}\), \(\xi_j=L^{j-k}\), and write \(d=d_{\mathbf B}\)
for its path metric. The test sizes and proposed profile are
\[
 v(\tau)=\lVert\partial\mathbf V(\tau)-1\rVert,
 \qquad P_\delta(x)=\max_\tau e^{-\delta d(x,\tau)}v(\tau).
 \tag{1}
\]
The target bounds **both**
\[
 \eta^{-2}\mathsf L(p)^2\lVert U_p-1\rVert,
 \qquad \mathsf L(b)^3\lVert J(U)(b)\rVert
 \tag{2}
\]
by \(C P_\delta(x)\) at a corner \(x\), for every critical field
regular at a fixed sufficiently small radius. Constants must be independent
of depth, torus size, datum and shapes of the separated regions, subject
to the stated torus floor. The default convention omits inward bonds;
retaining them adds pinch tests. Criticality is for the actual Wilson
action and the actual nonlinear averaging constraints (SA 9593–9685).

Floor screening (SA 18334–18415) additionally needs an admitted localized
background and control of the contribution of its excluded floor.
Obligation 2.8, `sa-2.8.md` §9, needs a **difference** of two admitted
backgrounds with identical interior data. A one-field profile estimate
alone does not prove that difference estimate.

## 2. Initial exclusions and proof obligations

The counterexample search starts with a floor wall and with data supported
in a large region. Neither a discontinuous lift which is not regular nor
a field which is not critical is a counterexample to (1)–(2).
`a1-orbit.md` §7 already distinguishes the growing comb-gauge potential
of flat data, whose curvature and current vanish, from the discontinuous
lift of curved data, whose normalized curvature grows with depth.

The gate `a3-gate-b2c312b2e.md` §§6–9 rules out using Theorem CL or its
two-background continuation as an established input. Weighted local
\(L^2\) control does not supply the complete pointwise regularity norm,
and a large Euclidean patch need not see just two scales. These issues
must be addressed before a local maximum argument can be applied.

## 3. A localized, slowly varying critical family: the first kill attempt

Here is an exact test at arbitrary depth, rather than a discontinuous
lift or a solution restricted to symmetric variations. Work on a single
coarse lattice, put \(s=L^k\), \(h=(s-1)/2\), and use bare integer
coordinates. Take \(N\ge4\) and a torus with \(8N\) coarse sites in
direction 1, enlarged in the other directions to meet the torus floor.
Define a periodic scalar sequence of period \(8N\) by
\[
 q_j=\begin{cases}
 j/N&0\le j\le N,\\
 1&N\le j\le2N,\\
 (3N-j)/N&2N\le j\le3N,\\
 0&3N\le j\le4N,
 \end{cases}
 \qquad q_{j+4N}=-q_j.
 \tag{3}
\]
Let \(B_j=\{js-h,\ldots,js+h\}\). For \(i=js-h+u\),
\(0\le u<s\), set
\[
 p_i={t\over s^2}\left(q_j+{u+1\over s}(q_{j+1}-q_j)\right),
 \quad f_i=\arcsin p_i,\quad a_{i+1}-a_i=f_i.
 \tag{4}
\]
The antiperiodicity makes \(\sum_i f_i=0\), so \(a\) can be
chosen periodic. Set \(Z=\operatorname{diag}(i,-i)\),
\(U_2(x)=\exp(a_{x_1}Z)\), and \(U_\mu=1\) otherwise.
Currents and multipliers below are written in scalar Cartan coordinates;
their Hermitian generator in the outline's convention is \(-iZ\).
Then \(U_{12}(x)=\exp(f_{x_1}Z)\). For \(0<t<1/8\),
\(|f_i|\le2t/s^2\), while
\[
 p_i-p_{i-1}={t\over s^3}(q_{j+1}-q_j)\quad(i\in B_j).
 \tag{5}
\]

For this Cartan field the actual centered contour mean has zero site
factor: the contour angle is odd in the displacement in direction 2.
Within the small relative-angle branches, its straight part is arithmetic
averaging of the angles. Consequently
\[
 V_2(j)=\exp(b_jZ),\qquad b_j=\sum_{i\in B_j}a_i,
 \qquad V_\mu=1\quad(\mu\ne2).
 \tag{6}
\]
These are group equalities; no globally small choice of \(a\) or \(b\)
is required. Intermediate plaquette angles are sums of at most
\(L^{2n}\) bare angles and have magnitude at most
\(2t(L^n/s)^2\). Lowering \(t\) once by a constant depending on
the finite one-step mean keeps every averaging step on its prescribed
branch, independently of \(N,k\). This is the same averaging mechanism
checked in `a1-orbit.md` §7.4, now with localized data.

The action derivative at a direction-2 link is
\(\sin f_{i-1}-\sin f_i=-t(q_{j+1}-q_j)/s^3\).
Put multiplier \(-t(q_{j+1}-q_j)(-iZ)\) on every coarse direction-2
bond in block \(j\). Its divergence is zero because it is independent
of coordinate 2. The adjoint straight mean contributes \(L^{-3}\)
at each step: a given link is in exactly \(L\) forward segments,
each with weight \(L^{-4}\). The site-factor terms pair to zero
against this divergence-free multiplier. Thus its pullback is exactly
the displayed action derivative. Both sides vanish on perpendicular
colour variations: conjugation by every constant \(e^{uZ}\) fixes
the background, so the derivative of the covariant mean cannot map the
rotating perpendicular plane into the fixed Cartan line. This proves
criticality against **all** constrained variations. The normalized
current is \(-t(q_{j+1}-q_j)(-iZ)\), and the normalized curvature is
at most \(2t\). Choose \(t\) below the fixed regularity radius.

This family does not violate the profile estimate. Indeed its coarse
plaquette angle is
\[
 T_j=b_{j+1}-b_j
       =\sum_{i\in B_j}\sum_{r=i}^{i+s-1}f_r.
 \tag{7}
\]
Near each nonzero block all terms have one sign; the zero intervals
separate the positive and negative supports. The combined multiplicity
of an \(r\in B_j\) in \(T_{j-1}+T_j\) is exactly \(s\).
For \(s\ge3\), the sum of the nonnegative affine values in (4) is
at least \(t\max(|q_j|,|q_{j+1}|)/(3s)\). Since
\(|\arcsin p|\ge|p|\),
\[
 \max(|T_{j-1}|,|T_j|)
       \ge {t\over6}\max(|q_j|,|q_{j+1}|).
 \tag{8}
\]
Also \(|T_j|\le2t\), so its holonomy norm is at least
\(|T_j|/2\). Equations (4)–(5) therefore bound both members of
(2), on block \(j\), by 24 times a test within a fixed number of
coarse spacings. If both endpoints in (8) vanish, both members vanish
there. For \(s=1\), every bond is prescribed: curvature is a datum
test and current is a sum of neighbouring plaquette forces, giving the
same conclusion directly. Thus this explicit family obeys (1)–(2)
with a constant independent of its plateau size and depth. In particular
neither a long plateau nor accumulation of its volume produces a
counterexample in this test. This is a closed test, not a proof for
general nonabelian data.

The heavy-wall test has a different logical boundary. A wall **in** the
determining problem contributes its tests to (1). Deleting them changes
the proposed inequality. A wall violating the fixed regularity radius
does not satisfy Theorem 2's hypothesis. A wall outside the local
variational domain does not enter its inner-plaquette action; influence
through retained boundary rows is datum influence and must be included.
These observations do not prove admission or screening of the arbitrary
floor in row 83.

## 4. Exact cited-pending inputs

The proof below is conditional on the following **ports**, in the
no-inward-bond convention used by floor screening and 2.8. Neither port
is claimed completed at the pinned repository commit. They must use the
outline's mean and its inner-plaquette action, including artificial box
boundary rows. Merely substituting Balaban's notation is insufficient.

**P81: unweighted coordinates and finite-step averaging calculus.**
This is the portion of row 81 needed from Balaban's CMP 102 proof.
Its constants, chart radii and minimum auxiliary geometry depend on
\(L\) alone (dimension is fixed at four):

1. On a fixed one-step block, the mean is local, covariant and analytic
   on the small relative-holonomy branch. If the fine plaquettes have
   norm at most \(u\), its coarse plaquettes have norm at most
   \(L^2u+C_Lu^2\). In block axial gauge, reconstruction of a fine
   bond from the corresponding coarse bond has error at most \(C_Lu\),
   with coefficient **one** on the coarse bond's distance from 1.
   Inside a block there is no coarse-bond term. The outward-row reduction
   is local to its one finer block and has a uniform small-chart
   Lipschitz bound. These are the averaging/gauge inputs to his proof,
   and their identification with the outline's mean is part of row 81.
2. On any admitted separated auxiliary sequence, let a real critical
   field have regularity radius \(r\), and suppose its datum, after a
   node gauge, is at distance at most \(b\) from 1 on **all** rows.
   For \(r+b\) sufficiently small it has a gauge representative
   \(e^{i\eta A}\) and a straightened coordinate \(Z\) satisfying
   \[
   \|A\|_1+\|Z\|_1\le C_{81}(r+b),\qquad
   A=Z-H D(Z),\qquad Z=H\beta-\mathcal G N(Z).
   \tag{9}
   \]
   Here \(\|Z\|_1=\sup\max(\xi|Z|,\xi^2|\nabla Z|)\),
   \(\beta\) is the reduced **angular** row datum, \(H\) is the
   flat constrained extension and \(\mathcal G\) the flat inverse
   on the homogeneous constrained Landau slice. The reduction of the
   datum reads only the row and, for an outward row, its finer outer
   block. In the same fixed ball,
   \[
   \|D(Z)\|_\infty\le C_{81}\|Z\|_1^2,
   \qquad |N(Z)|_{(-3)}\le C_{81}\|Z\|_1^2.
   \tag{10}
   \]
   Write the straightened nonlinear average as \(KA+C(A)\),
   with \(C(0)=C'(0)=0\). Its column bound is
   \(|C'(A)^*\omega|_{(-3)}\le C_{81}\|A\|_1\|\omega\|_\infty\).
   At the representative of a critical field there is a multiplier
   satisfying \(F'(A)=(K+C'(A))^*\omega\), where
   \(F(A)=A_{O_0}(e^{i\eta A})\). This is the actual constrained
   Euler equation, before differentiating a branch. It includes the
   node-gauge identification in the port; stationarity on an unrelated
   slice is not enough.

For precision about the citation: (9) uses CMP 102 Proposition 2,
(19)–(21), Proposition 3's constraint straightening, and the flat-reference
identities (157)–(159) in the proof of Proposition 8; (10) is (55) and
Proposition 4, (97)–(98). The column bound is the quantitative
straightened-average calculus used in that reduction (the summable
one-step row/column bounds in SA 9808–9821). The a priori coordinate bound in that local
construction is (152). Those steps use CMP 99 (75–102), Theorem 2, as
Balaban explicitly says. That gauge input is **inside the pending row-81
port**, not a newly discharged citation here. P81 contains no distance,
profile estimate, or conclusion about nonregular floors.

**P82: flat weighted supremum estimates in the actual row convention.**
There are fixed \(a>0,C_{82}<\infty\), depending on \(L\) alone,
such that, on every admitted
separated auxiliary sequence, for \(0\le\theta\le a\),
\[
 \|H\beta\|_{1,w}
       \le C_{82}\|\beta\|_{\infty,w},\qquad
 \|\mathcal G f\|_{1,w}
       \le C_{82}|f|_{(-3),w},
 \quad w(z)=e^{-\theta d_*(z,z_0)}.
 \tag{11}
\]
The output norm contains \(\xi|A|\) and \(\xi^2|\nabla A|\),
with the same weight;
\(d_*\) is the auxiliary sequence's metric. Row weights are evaluated
at their assigned tops. The linear constraint defining \(H\) includes
the row length: \(K H\beta=\beta\), where \(K\) differentiates
the **angular** average. This prevents loss of a scale factor by using
a per-length kernel on an angular datum.
Also use the corresponding weighted bounds for \(H^*\), from
\(|f|_{(-3),w}\) to row supremum, and for the coarse precision
\(E=H^*\partial^*\partial H\), from row supremum to itself.
The fine-bond inner product is \(\eta^4\sum_b\langle\cdot,\cdot\rangle\);
the angular-row inner product is counting measure. The latter is the
scale-invariant four-dimensional convention: a cell's quadratic energy
is \(\xi^4(\beta/\xi^2)^2\). These choices determine the adjoints.
Using per-length row variables instead requires the compensating row
weights. The estimates are weighted Schur estimates for these kernels,
including their scale factors.
Equivalently, with
\(G_0=(\partial^*\partial+dRd^*+K^*K)^{-1}\),
\(E=(KG_0K^*)^{-1}-I\): multiply the defining equation for
\(H=G_0K^*(KG_0K^*)^{-1}\), use \(KH=I\) and
\(Rd^*H=0\), then pair with \(H\).

P82 is a precise part of the requested row-82 kernel/derivative port.
It includes weighted summation over rows, not just a pointwise column
bound. Its sources are Balaban's flat propagators and their CMP 99
(389–434) formulations (3.42)–(3.49), (3.126)–(3.133), Theorems
3.12–3.13, specialized to 1, with boundary and mean identifications
still pending. No curved inverse, complex continuation, or bound on
\(\Delta\mathcal G\) is used. Nor is an arbitrary-force supremum
bound on \(\partial^*\partial\mathcal G\) assumed: the current
will be estimated through its multiplier. In particular the exception concerning
the covariant Laplacian in Theorems 3.12–3.13 is not discarded.

This is stronger than the surviving estimates of `a3-response.md`:
its gated \(L^2\) estimates do **not** supply (11). Balaban's
Proposition 9 and the printed derivative assertions (189)–(190) are
**not** inputs to this proof. The paper explicitly leaves the relevant
second differentiation unperformed on p. 308.

## 5. Localizing the unweighted reduction

All constants denoted \(C_L\) below may depend on P81, P82 and \(L\),
but not on depth or the localizing length \(\sigma\).
Choose \(\sigma\) to be a sufficiently large power of \(L\).
Choose the original cube size and gap afterwards, so that
\(\mathfrak M,\rho\ge C_L\sigma\). This is the order in
SA 9916; it is essential for the following construction.

For a field element at \(x\), write \(r(x)\) for the larger of
the quantities (2) on its bounded stencil, with the appropriate scale
on each member. Enlarging such stencils changes all constants only by
\(C_L\). Define
\[
 r_R(x)=\max_{d(x,z)\le R}r(z),\qquad
 v_R(x)=\max_{d(x,\tau)\le R}v(\tau),
 \qquad R=C_L\sigma.
 \tag{12}
\]
Supports of averaging rows, not just their endpoint labels, are included
when choosing this fixed \(C_L\).

### 5.1 Geometry and stationarity

A cube of diameter \(C\sigma\xi_j\) about a point of layer \(j\)
cannot meet both \(\Omega_j^c\) and \(\Omega_{j+1}\): those
sets are separated by \(\rho\xi_j\). If it meets the finer layer,
the next finer boundary is at least \((\rho/L)\xi_j\) away.
If it meets the coarser layer, the next coarser boundary is still farther
away. Choose \(\rho>C_L\sigma\), including the fixed padding for
blocks and stencils. The enlarged read cube therefore meets at most
two consecutive original scales, \(s/L,s\). Its diameter is
\(O(\sigma s)\). Paths inside it have original metric length
\(O(L\sigma)\), so the entire construction lies in the ball of (12).
This argument uses the gap **after** the patch size has been fixed;
it does not make the incorrect arbitrary-patch assertion in Theorem CL.

If the stencil lies near \(\Omega_0^c\), separation puts it entirely
in layer zero. Its bonds are prescribed, its plaquette is a datum test,
and its current is a sum of at most six neighbouring plaquette forces.
The desired local inequality follows directly there. Otherwise the
read cube and its padding lie inside \(\Omega_0\). The torus floor
makes them nonwrapping.

Write \(s=\xi_J\). Choose a centered block cube \(C_J\) of
half-side comparable to \(\sigma s\), and enlarge it successively
to cubes \(C_i\), \(i<J\), with gaps at least \(g\xi_i\),
where \(g\) is a fixed admissible auxiliary gap. Round outward to the
fixed auxiliary block grid. The added half-side is at most
\(C g\sum_{i<J}\xi_i\le C g s/(L-1)\). Thus all \(C_i\)
and their required supports fit in the read cube. Put
\[
 O_i=C_i\cap\Omega_i\quad(0\le i\le J),\qquad O_{J+1}=\varnothing.
 \tag{13}
\]
Use an auxiliary block size dividing the original one. Intersections
are unions of those blocks, and remain separated: the complement of
an intersection is the union of the complements, each at the required
distance from the next intersection. In a central cube the auxiliary
and original sequences agree. All changed rows are a physical distance
at least \(c\sigma s\) from \(x\). Since no auxiliary scale
exceeds \(s\), their tops are at auxiliary metric distance at least
\(c\sigma\), after allowing the fixed row support widths.

Prescribe on (13) the **actual averages of \(U\)**. The restriction
is critical. Here is the constraint argument, without invoking uniqueness.
Extend a constrained curve on \(O_0\) by \(U\) outside it. Its
bare outer collar is fixed by the new level-zero rows, so every
plaquette crossing \(\partial O_0\) is unchanged. Inductively the
level-\(i\) averages agree with those of \(U\) on every bond
having no endpoint in \(O_{i+1}\). For the induction step, the
blocks of level-\(i+1\) nodes outside \(O_{i+1}\) are outside
that block union, so their finer rows are already fixed. Averaging
them fixes bonds whose endpoints are both outside \(O_{i+1}\).
The remaining bonds with no endpoint in \(O_{i+2}\) are exactly
the level-\(i+1\) determining rows, fixed by prescription. At an
outward row its outer block consists of fixed finer interior rows;
this includes its contour factors. An old level-\(i\) determining
row has no endpoint in \(\Omega_{i+1}\), hence none in
\(O_{i+1}\); it is consequently
fixed at this stage. Thus the extended curve preserves every old
constraint. The action difference equals the inner-\(O_0\) action
difference, proving stationarity of the restricted field.

Auxiliary scales are no larger than the original ones. The restricted
curvature and current therefore obey the auxiliary regularity bounds
with radius \(C_Lr_R(x)\). At the artificial outer boundary only
layer-zero bonds occur. Even if a truncated current has fewer terms,
its normalized magnitude is at most six times the largest incident
plaquette norm. Thus boundary cancellation is not being assumed.

### 5.2 A datum gauge with the needed local bound

Complete the coarse level-\(J\) grid on the read cube. Use \(V_J\)
where it is prescribed and the one-step average of \(V_{J-1}\)
in the finer region. Outward blocks are fully prescribed at the finer
level, so this is exactly \(\mathcal M^J U\) on the needed rows.
Every coarse plaquette is either an original test or the average of
finer test plaquettes. P81(1) therefore bounds its holonomy norm by
\(C_Lv_R(x)\).

Put this completed datum in comb gauge based at the coarse site nearest
\(x\). A coarse bond at distance \(m\) from that site closes a
loop between two comb paths. Moving the paths one coordinate at a time
fills the loop with at most \(C_L(1+m)\) plaquettes: for a bond in
direction \(\mu\), each later coordinate contributes its strip of
width one and length equal to that coordinate displacement. Products
of transported plaquettes obey
\(\|\prod P_i-1\|\le\sum_i\|P_i-1\|\), since transports
are unitary. Consequently the gauged coarse bond has norm at most
\(C_L(1+m)v_R(x)\) from 1.

Inside a coarse block put the finer datum in block comb gauge, leaving
its top fixed. Its internal bonds have error at most \(C_Lv_R(x)\).
P81's reconstruction inequality compares a crossing fine bond with
the corresponding completed coarse bond, with that same error and
coefficient one on the coarse bond. Thus all original rows in the
central two-level region have error at most
\(C_L(1+d_*(x,y_c))v_R(x)\). Here physical distance divided by
\(s\) is at most \(d_*\), and the two scales differ by only \(L\).

Continue this gauge down to the bare field using block comb gauges.
At level \(n\), the plaquette bound coming from the read cube is
\(C_Lr_R(x)(\xi_n/s)^2\). To check that its constant is uniform,
iterate the one-step bound \(u\mapsto L^2u+C_Lu^2\): after
removing \(L^{2n}\), its relative errors are bounded by a geometric
series \(C_Lr_R\sum_{n<J}L^{2(n-J)}\). For sufficiently small
\(r_R\), the product of \(1+\)these errors is at most 2,
using \(1+t\le e^t\). Formally, at the first step exceeding twice
the linear bound, all preceding steps satisfy that bound, so their
relative-error product is at most
\(\exp(C_Lr_R/(1-L^{-2}))<2\), a contradiction.
Reconstruction now gives
\[
 \|W_n(b)-1\|
 \le \|W_{n+1}(c)-1\|+C_Lr_R(x)(\xi_n/s)^2.
 \tag{14}
\]
The coarse term is absent for an internal bond. Following the unique
coarse bond when present sums a geometric series; it never multiplies
the preceding error by \(C_L\). The top comb has length
\(O(\sigma)\). Hence **every** auxiliary datum row is within
\(C_L\sigma r_R(x)\) of 1, independently of the number of
artificial layers.

The reduced datum in P81 reads only one finer block at an outward row.
Its local Lipschitz bound and \(\|\log W\|\le2\|W-1\|\)
on the smaller chart give
\[
 \begin{split}
 |\beta(c)|&\le C_L(1+d_*(x,y_c))v_R(x)
                  &&\text{on central original rows},\\
 \|\beta\|_\infty&\le C_L\sigma r_R(x)
                  &&\text{on all auxiliary rows}.
 \end{split}
 \tag{15}
\]
All other rows have \(d_*(x,y_c)\ge c\sigma\). Decrease the
fixed regularity radius so that \(C_L\sigma r_R\) remains in
the P81 chart. Applying its unweighted bound gives
\[
                   \|A\|_1+\|Z\|_1\le C_L\sigma r_R(x).
 \tag{16}
\]

## 6. The local improvement, including the current

### 6.1 The local nonlinear force estimate

Let \(F(A)\) be the Wilson action in the exponential chart at 1.
On a stencil with comparable scales \(\xi\), put
\(a_*=\sup|A|\), \(g_*=\sup|\nabla A|\). For
\(\eta a_*\) sufficiently small,
\[
 F'(A)=\partial^*\partial A+M(A),\qquad
 |M(A)|\le C(a_*g_*+a_*^3+\eta g_*^2).
 \tag{17}
\]
Here and below an extra fixed stencil enlargement is understood.
Consequently \(|M(A)|_{(-3)}\le C_L\|A\|_1^2\) when
\(\|A\|_1\le1\).

For completeness, the cancellation supplying the missing power of
\(\eta\) in (17) is as follows. Write
\(E_\mu(z)=e^{i\eta A_\mu(z)}\),
\(P_{\mu\nu}(z)=E_\mu(z)E_\nu(z+\eta e_\mu)
E_\mu(z+\eta e_\nu)^{-1}E_\nu(z)^{-1}\), and
\(h_{\mu\nu}=\eta^{-2}(P_{\mu\nu}-P_{\mu\nu}^*)/(2i)\).
Expanding only the two displaced factors about their values at \(z\)
gives
\[
 h_{\mu\nu}=(\partial A)_{\mu\nu}
                  +R_0(A_\mu(z),A_\nu(z))+R_1(z),
 \quad |R_1|\le C(\eta a_*g_*+\eta^2g_*^2).
 \tag{18}
\]
The constant-field term is the Hermitian Lie-algebra part of the group
commutator divided by \(\eta^2\). It vanishes with its first
derivative at zero, so \(|R_0|\le Ca_*^2\) and its Lipschitz
constant on that ball is at most \(Ca_*\). These bounds follow
directly by applying the fundamental theorem of calculus twice to
the four exponentials; each differentiated exponential has the integral
formula \(D e^X[Y]=\int_0^1e^{(1-t)X}Ye^{tX}\,dt\).
The linear displaced terms in (18) are exactly
\(\nabla_\mu A_\nu-\nabla_\nu A_\mu\). Every remaining
term has either one displacement and an additional factor \(\eta A\),
or two displacements, which proves the displayed bound on \(R_1\).

The exact current pairs opposite staples. Apart from the fixed sign
convention of \(\partial^*\), each pair is
\[
 \eta^{-1}\{h_{\mu\nu}(z)
       -\operatorname{Ad}(E_\nu(z-\eta e_\nu)^{-1})
                         h_{\mu\nu}(z-\eta e_\nu)\}.
 \tag{19}
\]
The difference of the \(R_0\) terms divided by \(\eta\) is
at most \(Ca_*g_*\). For \(R_1\) use its bound at the two
sites, giving \(C(a_*g_*+\eta g_*^2)\). Removing the transport
in (19) costs at most \(Ca_*(g_*+a_*^2)\), since
\(\|\operatorname{Ad}(E)-I\|\le C\eta a_*\).
This proves the same remainder bound for the left current. Finally
the derivative of exponential coordinates is a pointwise matrix
\(T_A=I+O(\eta a_*)\), with \(F'(A)=T_A^*J(U)\).
The linear term has magnitude at most \(C g_*/\eta\), so
multiplication by \(T_A-I\) costs only \(Ca_*g_*\).
This proves (17). At an outer boundary the opposite-staple pairing
can be absent, but only at layer zero, where \(\xi=\eta\).
The Taylor remainder of each remaining staple is at most
\(C a_*^2/\eta+C a_*g_*+C a_*^3\) in force units.
Multiplication by \(\eta^3\) bounds it by \(C\|A\|_1^2\).
Thus the global weighted force bound used below also holds there.

The same four-factor expansion, without taking a divergence, gives
\[
 \eta^{-2}\xi^2\|P-1\|
       \le C\xi^2|\partial A|+C\|A\|_1^2.
 \tag{20}
\]
Neither (17) nor (20) assumes a supremum bound on arbitrary second
differences of \(A\).

### 6.2 Near/far splitting and the multiplier

Let \(w(z)=e^{-a d_*(x,z)}\). From (15),
\[
 \|\beta\|_{\infty,w}
    \le C_L v_R(x)+C_L\sigma e^{-c a\sigma}r_R(x).
 \tag{21}
\]
Indeed \(\sup_{t\ge0}(1+t)e^{-at}\le1+a^{-1}\) on the
central rows, and all other rows have distance at least \(c\sigma\).
This is where the coefficient of \(v_R\) loses its apparent
factor \(\sigma\). The estimate does not count the size of the
datum's support.

Use (9)–(11), (16), and the unweighted bounds for the two quadratic
remainders. They give
\[
 \|A\|_{1,w}
 \le C_L\{v_R(x)+\sigma e^{-ca\sigma}r_R(x)}
                         +C_L\sigma^2r_R(x)^2.
 \tag{22}
\]
Equation (20) proves this same estimate for curvature at the center.
It does not yet prove the estimate for current.

For that estimate let \(\omega\) be the P81 multiplier. Since
\(H\) is the flat energy-minimizing extension and
\(K\mathcal G=0\),
\(H^*\partial^*\partial\mathcal G=0\): equivalently
\(\partial^*\partial H=K^*E\), followed by transposition.
Apply \(H^*\) to the Euler equation in P81 and use (9), (17):
\[
 \bigl(I+H^*C'(A)^*\bigr)\omega
      =E\{\beta-D(Z)\}+H^*M(A).
 \tag{23}
\]
The operator added to \(I\) has unweighted row-supremum norm at
most \(C_L\|A\|_1\). Once \(C_L\sigma r_R\le1/2\),
its inverse is the convergent geometric series with norm at most 2.
Equations (10), (16), (17), and the unweighted P82 bounds first give
\(\|\omega\|_\infty\le C_L\sigma r_R\).
Rewrite (23) as
\[
 \omega=E\beta+\mathcal E,\qquad
 \mathcal E=-E D(Z)+H^*M(A)-H^*C'(A)^*\omega,
 \qquad \|\mathcal E\|_\infty\le C_L\sigma^2r_R^2.
 \tag{24}
\]
Applying the weighted precision estimate to \(E\beta\) and (21)
proves
\[
 \|\omega\|_{\infty,w}
 \le C_L\{v_R+\sigma e^{-ca\sigma}r_R+\sigma^2r_R^2\}.
 \tag{25}
\]

To return to the physical current, use
\(J(U)=(T_A^*)^{-1}(K+C'(A))^*\omega\).
Here \(\|(T_A^*)^{-1}\|\le2\) on the chosen chart.
The column sum of \(K\), with its physical cell factors, is
\(C_L\xi^{-3}\); this is precisely the scale of the current.
A row containing the central bond has its top at bounded auxiliary
distance, and at one of at most two adjacent scales. The weighted
bound for \(K^*\omega\) follows by this column sum and the
bounded change of \(w\) across the double block. The remaining
term has unweighted norm
\(|C'(A)^*\omega|_{(-3)}\le C_L\sigma^2r_R^2\).
Thus (25) bounds the current at the center as well. This avoids an
incorrect supremum estimate on a transverse second-order inverse.
All gauges used here are real and unitary. Plaquette holonomies and
left currents transform by conjugation at their base sites, preserving
their norms, so these are bounds on the original field \(U\).

Enlarge the constants and use \(\sigma\ge1\). For both members
of the required regularity norm we have proved, relative only to
P81 and P82,
\[
 \boxed{\quad r(x)\le C_0v_R(x)
       +\bigl(C_1\sigma^2e^{-c a\sigma}
                    +C_2\sigma^4 r_R(x)\bigr)r_R(x).\quad}
 \tag{26}
\]
All constants here precede \(\sigma\). This is the local
inequality proposed in SA 9863, now with the boundary, gauge, current,
and weighted-summation inputs separated explicitly.

## 7. The slowly varying maximum argument

Choose \(\sigma\) large enough that
\(C_1\sigma^2e^{-ca\sigma}\le1/8\). Such a choice exists:
the exponential series gives \(e^{ca\sigma/2}\ge
(ca\sigma/2)^3/6\), which makes the polynomial times the remaining
decaying exponential tend to zero. Choose the fixed regularity radius
\(\varepsilon_*\) to satisfy all P81 chart restrictions above and
\(C_2\sigma^4\varepsilon_*\le1/8\).
Then every admitted regular critical field satisfies
\[
             r(x)\le C_0v_R(x)+\tfrac14 r_R(x).
 \tag{27}
\]
Choose the geometry as in §5 and set
\(\delta=(\log2)/R\), reducing it if necessary when the bounded
stencil enlargement in (12) is included. The entire choice depends on
\(L\) and the cited-pending uniform constants, not on depth.

Let \(P=P_\delta\) be (1). Triangle inequality for distance to
a set gives
\[
 P(z)\le e^{\delta d(x,z)}P(x),\qquad
                         v_R(x)\le e^{\delta R}P(x)\le2P(x).
 \tag{28}
\]
If any test is nonzero, \(P\) is strictly positive everywhere on
the finite torus. The finite maximum
\(Q=\max_x r(x)/P(x)\) then exists. Equations (27)–(28) imply
\[
 {r(x)\over P(x)}\le2C_0+	frac12 Q,
 \qquad Q\le2C_0+	frac12 Q,
 \qquad Q\le4C_0.
 \tag{29}
\]
If every test is zero, (27) applied at a maximum of \(r\) gives
\(\max r\le\frac14\max r\), hence \(r=0\). Empty determining
sets cause no additional case: an admitted nonempty domain has tops;
an empty domain has no field elements to estimate. This proves
\[
 \boxed{\eta^{-2}\mathsf L(p)^2\|U_p-1\|,
        \quad \mathsf L(b)^3\|J(U)(b)\|
      \le C\max_\tau e^{-\delta d_{\mathbf B}(x,\tau)}
                          \|\partial\mathbf V(\tau)-1\|.}
 \tag{30}
\]
For thresholds \(\varepsilon^{(q)}\) on the tests in layer \(q\),
take the maximum separately on each layer in (30). This gives the
layer-profile version in Theorem 2, with a fixed support-width factor
if distance is measured to layer sites rather than the tests themselves.
No number of layers or tests enters (27)–(30).

## 8. What the consumers may read

**Floor screening.** For an already admitted localized sequence, split
its actual tests into exterior tests \(E\) and a mismatch set \(F\).
If \(v\le\varsigma\) on \(E\) and \(v\le A_F\) on \(F\),
(30) gives exactly
\[
 \eta^{-2}\mathsf L(p)^2\|U_p-1\|
      \le C\{\varsigma+A_F e^{-\delta d(p,F)}\}.
 \tag{31}
\]
Consequently the displayed screening form follows **when** the actual
localized problem has \(A_F\le C R_m^2\varepsilon_m\) and
\(d(p,F)\ge cMR_m\). Its rate is a fixed fraction of the profile
rate \(\delta\). One cannot replace it by a larger, previously
fixed propagator rate \(\delta_0\). Any later common-rate convention
must choose the common rate below this one.

An arbitrary raw floor is not silently assigned the bound on \(A_F\).
If the construction removes that floor and uses an extension obtained
from the exterior shell, row 83 must show which tests the extension
creates, their sizes, and that the resulting localized problem is
admitted. If the raw floor remains among the determining data, its
actual test sizes remain in (31). The theorem proved here neither
removes them nor asserts existence for nonregular data.

**Obligation 2.8.** Formula (30) supplies the individual background
regularity bound wherever its datum profile is small. It does not prove
\(|a_p(P_X)-a_p(P)|\le C a_k^2\eta_k^4e^{-mD_p}\) from
`sa-2.8.md` §9. Applying (30) twice bounds that difference only by
\(C a_k^2\eta_k^4\); it does not make common interior data cancel.
The two-background response and admitted interpolation are still the
separate row-85/6(c) obligations identified by the gate.

## 9. Endpoint and dependency boundary

**PROVED with the cited-pending inputs P81 and P82:** the real,
no-inward-bond first half of (1b) Theorem 2, uniformly in depth, on
the separated localized families used by the named consumers, for
every already admitted critical field regular at the fixed radius.
The local inequality, current estimate, parameter choices, zero-datum
case and weighted maximum argument are written above. The localized
slow-plateau kill attempt is settled explicitly in §3.

The pending list is exactly §4: the ported unweighted coordinate and
averaging calculus from Balaban's CMP 102 proof (row 81, including its
gauge input), and the flat weighted supremum/precision/adjoint bounds
with actual box rows (row 82). Theorem 1's global conclusion alone
would not replace P81; pointwise kernel decay alone would not replace
P82's weighted summation. Neither input is asserted discharged in this
checkout. If either port fails its stated identification, (30) loses
that premise. The optional kept-inward-bond variant, complex response,
arbitrary-floor admission and the comparison (L) are not proved here.

The proof's geometry and maximum argument follow the proposal of
Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors
of their text; the flat coordinate reduction and improvement mechanism
are credited to T. Balaban. This is a research implication with explicit
pending inputs, not an audit or a grant of scientific status. No numerical
proof, subagent, other-file edit, commit, push, PR or post is used.

PROVED (conditional on P81 and P82).
