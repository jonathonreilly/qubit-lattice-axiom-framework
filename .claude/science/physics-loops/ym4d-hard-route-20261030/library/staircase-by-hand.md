State of attack
===============

Completed at pinned source `28e261c1726d3afc037eb4e1255b32968f66806e`.
Only this file was written. No numerical job, machine enumeration,
subagent, audit, commit, or external publication is part of this work.

- **discharged (source trace):** O1 remains consumed by O3 and SRC in
  `sector-values.md:47-74`, and by the current low-order route recorded in
  `parts/hard-core--mapped.md:88-94`. The retirement of Section 3's older
  LIFT-I route does not retire O1.
- **discharged:** every lexicographic prefix and its complement have
  non-pinching local graph patterns, for every size and every seam. Sections
  2--4 give a discrete reflection operator and its absolute norm bound.
- **discharged (theorem with explicit premise):** under the level-k
  plaquette bound (BG), Section 5 gives a covariant extension with zero
  parent-block means, the absolute constant (EXT), and precisely (E-D0).
- **implication:** the mapped class-reference bound and its stated threshold
  choice imply (BG), by Section 6. The staircase extension input to F-D
  is therefore supplied within that class-reference hypothesis.
- **unchecked:** F-D's other estimates, the fine lifting in D-coer, and
  HS-P/HS-T and gas inputs retain their own obligations. O1 is not promoted
  to an unconditional theorem, nor is O2's already slower rate promoted.

## Scope and source convention

**discharged (scope).** The target's `GOAL.md`, including its prohibition on
computer-assisted proof steps, and `FINISH.md:78-106` were read. The sibling
attempt and the excluded gate families were not read. File reads and source
identity checks are bookkeeping, not mathematical evidence. The entry-point
workflow `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from this pinned
checkout; this bounded task follows the user's explicit contract and the
target rules. Source line references below refer to the pinned revision.

**unchecked (scope of existing claims).** Labels in other files are not
certifications by this note. In particular the full F-D, HS-P, HS-T, gas
bounds, and nonlinear Taylor arguments retain their own proof obligations.

## 1. What is still consumed

**discharged (source trace).** The order and O1--O3 are at
`sector-values.md:37-59`; SRC is at lines 66--74. The current mapped
obligation explicitly retains this staircase input at
`parts/hard-core--mapped.md:83`. Its lines 88--94 retain SRC, O1 and O3 in
Prop DS and the low-order closure. More directly,
`one-step-closure.md:148-158` drops the old data recursion but uses the
rooted O1 norm in Step A, then Prop DS in Step B. O1 is also read at the
top face in `sector-values.md:268`. Thus the item is live. The different
O1--O3 attached to the withdrawn Lemma OC at mapped line 81 are not these
lemmas.

**discharged (interface identification).** F-D calls the free region `Y`
and its frozen complement `Omega` (`fibre-propagator.md:118`). The
extension in D-coer is FROM `Omega`, not from `Y`: for
`u = omega_k = r^(k) omega`, it requires an extension with

    E u = u on Omega,       r^[k](E u) = 0 on every free parent block,
    ||E u||_N + ||D_k E u||_{N,density} <= C_ext C ||H_s||_L2.       (E-D)

These are precisely Step (4), line 124. Step (3) supplies a bound on
`D_k u` inside Omega and zero covariant means on its parent blocks.
Here `n=k+1`, so the extension is on the level-k lattice, with L sites
per side of a parent box. It is not an extension on the arbitrarily fine
original lattice. F-D's conclusion is at lines 162--172.

**unchecked (inherited inputs).** D-coer's relation between `D_k u` and
`H_s` in Step (3), the fine lifting
after (E-D), its saddle estimates, and the conversion to the chart
covariance are not proved by this note. Below, the extension estimate
itself is proved in explicit density norms.

## 2. Local geometry, without a pattern enumeration

**discharged (G1: all prefixes, all seams).** Number the boxes in each
ordered coordinate by `0,...,N_j-1`, starting at that order's seam and
using its selected sign. Let

    I_a = { b : b <=_lex a }.

If `b <= c` coordinatewise and `c <=_lex a`, then `b <=_lex c <=_lex a`:
at the first unequal coordinate of b and c the entry of b is smaller.
Thus I_a is a product-order down-set. The strict prefix is the same
argument, with `<_lex a`.

In a sufficiently small neighborhood of any point there are at most
two incident box indices in each coordinate. Orient that local
coordinate so its smaller index is the lower side. At an ordinary wall
this is the ordinary orientation; at the seam, the incident indices
are `N_j-1,0`, so it reverses. These choices are independent in the
four coordinates. The incident free cells are therefore a down-set of
`{0,1}^4`. If `N_j=1`, both sides have the same index, and membership is
independent of that bit. This covers coincident seams, `N_j=2`, and
one-box directions, without assuming that the torus has a global
product order compatible with its periodic topology. Reversing every
local bit makes the frozen complement a down-set too.

**discharged (G2: graph property is stronger than absence of a diagonal
pair).** Let `I` be a nonempty proper down-set of subsets of
`{1,...,d}`, d=4. The closed union of its incident orthants, after
translation and the preceding sign choices, is

    K_I = union_{J in I} { x : x_j <= 0 for every j not in J }.

Indeed, the positive-coordinate set of such an x is a subset of J;
conversely take J to be that positive-coordinate set. Put

    1 = (1,...,1),   y = x - x_d 1,   t = x_d,
    h(y) = max_{J in I} min_{j not in J} (-y_j),       y_d = 0.

All the minima are over nonempty sets. Then

    x in K_I  <=>  t <= h(y).                         (G)

Each function `-y_j` is 1-Lipschitz in the maximum norm. Taking a
minimum or maximum preserves that bound: if every pair of corresponding
entries differs by at most e, their extrema differ by at most e.
Consequently h is 1-Lipschitz. The map

    F(x) = x - h(x-x_d 1) 1

takes K_I to `{z_d <= 0}`. Its inverse is
`F^-1(z)=z+h(z-z_d 1)1`; both have maximum-norm Lipschitz constant at
most 3, since `|Delta(x-x_d 1)|_inf <= 2|Delta x|_inf`.
In Euclidean norm both constants are at most 6, since in four
dimensions `|z|_inf<=|z|_2<=2|z|_inf`.
Thus every nontrivial local pattern is explicitly bi-Lipschitz to a
half-space, with the same bound. There is no pinch on either side.
Empty and full patterns need no boundary chart. This proves the
geometric assertion for every size and every prefix, including seams.

## 3. Integer reflection and its local energy bound

**discharged (E1: an actual lattice operator).** Use integer coordinates
in a local chart. A half-open assignment of sites to boxes merely
changes the thresholds to integers `c_j`. Set

    D = union_{J in I} { m in Z^d : m_j <= c_j for j not in J },
    y=m-m_d 1,  t=m_d,
    h(y)=max_{J in I} min_{j not in J}(c_j-y_j),
    q(m)=t-h(y),
    R(m)=m+(1-2q(m))1,
    pi(m)=m if q(m)<=0, and R(m) otherwise,
    (E_I u)(m)=u(pi(m)).                             (R)

These formulas use only integer arithmetic, not rounding of a
continuum extension. Since R preserves y and sends t to `2h(y)+1-t`,
it is an involution interchanging D and its complement. Each point of
D has exactly two preimages under pi. Thus, for any real Hilbert-space
valued u,

    sum_Zd |E_I u|^2 = 2 sum_D |u|^2.                 (R0)

**discharged (E2: paths of length at most seven).** For `j<d`, changing
`m` to `m+e_j` changes h by either -1 or 0. For `j=d`, it changes h by
0 or 1: the other y-coordinates decrease by 1 and `y_d=0` stays fixed.
This follows directly by applying minimum and maximum to entries
which change by 0 or the indicated unit. In both cases

    q(m+e_j)-q(m) is 0 or 1.

Write `pi(m)=m-a(q(m))1`, with `a(q)=max(0,2q-1)` on integer q.
Across a bond the change in a is 0, 1, or 2. Therefore

    pi(m+e_j)-pi(m) = e_j-s1,  s in {0,1,2},
    |pi(m+e_j)-pi(m)|_1 <= 2d-1 = 7.                 (P)

Both endpoints lie in D. Join each to their coordinatewise minimum
by coordinate paths, decreasing first and then increasing in a fixed
coordinate order. Every vertex on the first part is below the first
endpoint, and every vertex on the second below the second endpoint;
the down-set property keeps the whole path in D. Its length is the
distance in (P).

Let `M=2d-1`. A fixed undirected edge of D can be used only by paths
whose starting image pi(m) lies within maximum-norm distance M of
one fixed endpoint of that edge. There are at most `(2M+1)^d` such
images, two preimages per image, and d positive coordinate bonds per
preimage. Cauchy--Schwarz on each path consequently gives

    sum_{edges of Z^d} |Delta E_I u|^2
      <= A_d sum_{internal edges of D} |Delta u|^2,
    A_d := M * 2d * (2M+1)^d,
    A_4 = 56 * 15^4.                                (R1)

Zero-length paths contribute zero. Edges are counted once in both
sums. This is a written counting bound, not a machine enumeration.
Together (R0)--(R1) bound the reflection operator independently of
the pattern, lattice spacing, box size, prefix and volume.

## 4. Patching at one parent-box scale

**discharged (E3: norms and a global scalar extension).** Parent boxes
have side 1 and L lattice sites per side. For a set A of sites define

    ||u||_0,A^2 = L^-d sum_{m in A}|u(m)|^2,
    ||du||_A^2 = L^(2-d) sum_{b internal to A}|Delta_b u|^2,
    ||u||_1,A^2 = ||u||_0,A^2 + ||du||_A^2.            (N)

Use the usual periodic edges, counting multiplicities if the torus is
very small. These are density-normalized site and gradient norms.
The theorem in this section applies to Omega or Y; take A=Omega for
D-coer.

For `L>=128`, put `r=L/64`. On the torus take centers c on the
Cartesian grid of spacing r (there are exactly `64 N_j` centers in
direction j), and tensor tents

    theta_c(x)=product_j (1-|x_j-c_j|/r)_+.

Distances here use the local periodic lift of a tent. On each interval
between consecutive centers the two one-dimensional tents add to 1;
therefore `sum_c theta_c=1`. Each tent is supported in a cube of radius
r, and its change along a unit coordinate bond is at most `1/r`.

The cube of radius `16r=L/4` about c meets at most one parent-box wall
in each coordinate and is injective on the torus. On its lattice sites
A therefore agrees, after local sign choices, with a set D of E1;
coordinates with no wall in the cube are irrelevant to membership.
Classify a patch using its sites at distance at most 2r from c:

- If all are in A, extend `theta_c u` by zero outside its support.
- If none are in A, use zero.
- Otherwise use (R) on the local D, applied to
  `f_c=theta_c u`, which is defined as zero on the rest of D.

This last definition needs no values of u outside the chart. Its
reflected support stays inside the chart: for a nonzero source point
p, `|p-c|_inf<=r`, choose a point b outside D with `|b-c|_inf<=2r`.
Let `K=ceil(3r)`. Then `p+K1>=b`, so it is outside D. Since
`q(p+s1)=q(p)+s`, the outward reflected point is at displacement
`1-2q(p)<=2K-1<=6r+1`. Its distance from c is at most `7r+1<=8r`.
Thus the extension has support in the radius-8r cube. On any bond
with a nonzero output endpoint, one image lies in the radius-r source
cube and the other is within seven lattice steps of it. The coordinate
path between them stays in the radius-(r+7) cube, inside the chart.
The source edges touching f_c also stay in that chart.
The all-in-A case has the same energy bound because every edge
touching its nonzero support has both endpoints in A.

Periodize these local outputs and add them; call the operator E.
On A each summand equals `theta_c u`, so `Eu=u`. At most
`B=19^d` output supports meet any site or edge: centers contributing
to an edge are within radius `8r+1<=9r` of its first endpoint, and
there are at most 19 centers per coordinate in such an interval.

For the input energies the product difference identity and
`|v+w|^2<=2|v|^2+2|w|^2` give

    sum_c ||f_c||_0^2 <= ||u||_0,A^2,
    sum_c ||df_c||^2
      <= 2||du||_A^2 + 2^(d+2) d 64^2 ||u||_0,A^2.   (T)

For the second bound, at most `2^(d+1)` tents touch either endpoint
of a bond, each has difference at most `1/r`, and there are d
positive bonds per site. The other term uses
`sum_c theta_c(m+e_j)^2<=1`. All nonzero source-edge terms are
internal edges of A. Cauchy--Schwarz over the at most B output
summands, followed by (R0)--(R1), proves

    ||Eu||_1^2 <= C_s^2 ||u||_1,A^2,
    C_s^2 := max(1+2d*128^2,
                 B*(2+2 A_d+2^(d+2) d 64^2 A_d)).    (E-s)

For `1<=L<128`, simply use zero extension: every crossing edge
contributes the squared value of its A endpoint, at most `2d` such
edges per site. Its norm is bounded by the first term defining C_s.
Thus (E-s) holds for every integer L>=1 and every torus size. No
continuum interpolation or unproved trace theorem is needed.

## 5. Covariant derivative and block means

**discharged (E4: a quantitative background hypothesis).** On the
level-k lattice let T_xy be the orthogonal adjoint transport from y
to x, and replace Delta in (N) by `T_xy u(y)-u(x)`; write this norm
as `||u||_1,A,U`. Assume

    ||T_boundary(p)-1||_op <= epsilon_0/L^2
       for every level-k plaquette p,
    epsilon_0 := 1/(4d^2),       d=4.                 (BG)

Means r_B are the uniform site averages transported to a block
center along in-block coordinate paths of length at most dL. A
convex average over coordinate orders is allowed. This is the
one-level mean of `fibre-propagator.md:23`, with the coordinate
contours specified in `composite-adjoint.md:18`.

Here is the needed local gauge construction. In an ordinary lattice
rectangle of side at most L, choose a corner and transport along
coordinates in a fixed order to each site. In that frame, a link is
the holonomy of the two ordered paths differing by one last edge.
Move that edge backwards past the later-coordinate portions of the
path. Each interchange of perpendicular neighboring edges replaces
one two-edge path by the other two-edge path around one plaquette,
and hence multiplies the holonomy by a conjugate of that plaquette
holonomy. There are at most `(d-1)L<=dL` interchanges. The algebraic
identity

    A_1...A_s-1 = sum_{l=1}^s A_1...A_{l-1}(A_l-1)

for orthogonal factors gives a norm bound by the sum of the factor
errors. Therefore every transformed link in the rectangle satisfies

    ||T_xy^g-1|| <= kappa/L,   kappa=d epsilon_0=1/(4d). (LG)

The patch rectangles in Section 4, including their needed lattice
edges, have side at most L. They have local lifts even at seams.
The construction also applies to the open coordinate cube of each
whole block; wrapping edges can be treated as its boundary edges.
It makes no choice of a global gauge or a trivial topological sector.

**discharged (E5: covariant patch extension).** For each patch use its
frame G_c, extend `theta_c G_c u` by its scalar operator, and transform
back on the output patch. Define

    E_U u = sum_c G_c^-1 E_c(theta_c G_c u).           (E-U)

This remains linear in u and is the identity on A. The difference
between the ordinary gradient of G_c u and its covariant gradient
has density norm at most `sqrt(d) kappa ||u||_0`. Consequently,
using three terms in the product difference instead of two,

    sum_c ||d(theta_c G_c u)||^2
      <= 3||D_U u||_A^2
         +(3d kappa^2+3*2^(d+1)d64^2)||u||_0,A^2.

For each output the covariant gradient squared is at most twice
the ordinary gradient squared plus `2d kappa^2` times its mass
squared. Apply (R0)--(R1) and the same overlap count B. Since
`kappa<=1/(4d)`, comparison with the displayed C_s gives, for example,

    ||E_U u||_1,U <= C_g ||u||_1,A,U,    C_g:=4 C_s.   (E-cov)

For L<128, zero extension proves the same bound without a gauge:
unitary transport does not change the crossing-edge contribution.
All constants in (E-cov) are absolute.

**discharged (E6: explicit correction of covariant means).** In a
block B write its sites as `m_j=0,...,L-1`. Extend by zero outside B
the function

    psi_B(m)=product_j min(1,4(m_j+1)/L,4(L-m_j)/L),
    b_B=psi_B / average_B psi_B.

At least half the sites in each coordinate have the corresponding
factor equal to 1 (the integer interval from `L/4-1` to `3L/4`
has at least L/2 sites in `0,...,L-1`). Thus the average is at least
`2^-d=1/16`. It follows that

    average_B b_B=1,   0<=b_B<=16,
    |Delta b_B|<=64/L,                              (b)

including bonds to the zero exterior.

Use the block frame G_B from E4. In this frame every path transport
R_Bx entering r_B differs from 1 by at most `d kappa`, by the same
product identity and the path length dL. Set

    M_B=average_{x in B} b_B(x) R_Bx,
    Q_B c(x)=G_B(x)^-1 b_B(x) M_B^-1 G_B(center)c,

and set Q_B c=0 outside B. Then `||M_B-1||<=d kappa<=1/4`.
The series `sum_{s>=0}(1-M_B)^s` converges in operator norm, has
product 1 with M_B by telescoping, and has norm at most 2. Hence
Q_B is well defined and `r_B Q_B c=c` exactly.

The mass bound is `|Q_B c|<=32|c|`. On each interior bond, (LG) and
(b) give a density-normalized gradient bound
`2(64+16 kappa)|c|<=160|c|`; on a boundary bond the bound is
`128|c|`, since the other endpoint is zero. If a periodic direction
has just one block, its wrapping edge has two boundary values of
the same bump; their sum is bounded by `256|c|`. Use this larger
bound for all edges. There are at most `2d L^d` edges touching a
block. For a collection of disjoint blocks, an edge sees at most two
block corrections. Thus

    ||sum_B Q_B c_B||_1,U^2
      <= C_b^2 sum_B |c_B|^2,
    C_b^2:=32^2+4d*256^2.                            (Bump)

Take A=Omega and define the required operator

    E_U^0 u := E_U u - sum_{B in Y} Q_B r_B(E_U u).   (E0)

It equals u on Omega, and has zero r_B mean on every block of Y.
The average defining r_B is contractive by Cauchy--Schwarz and
orthogonality, so
`sum_{B in Y}|r_B v|^2<=||v||_0^2`. Consequently

    ||E_U^0 u||_1,U <= C_ext ||u||_1,Omega,U,
    C_ext := (1+C_b) C_g.                            (EXT)

This is an explicit absolute constant, independent of L, the
number of boxes, the prefix and the seam. When u already has zero
means in Omega, (E0) has zero means in every block. Empty Omega
uses the zero operator; full Omega with zero block means uses the
identity. Both satisfy (EXT).

**discharged (E7: the mass term in the input costs no L).** For an
ordinary block function v, the variance identity is

    sum_x |v(x)-vbar|^2
      = (2 L^d)^-1 sum_{x,z}|v(x)-v(z)|^2.

Expanding both sides gives `sum_x |v(x)|^2-L^d|vbar|^2`, since
`sum_x v(x)=L^d vbar`; this proves the identity for vector values too.
Use non-wrapping internal edges of the coordinate cube; any
additional periodic edges only increase the energy. Join x to z
by changing coordinates in order. A path has length
at most dL. A fixed edge in coordinate j can occur for at most
`L^(d-1) L^2=L^(d+1)` ordered pairs: coordinates before j fix the
target coordinates and leave their starting coordinates free;
coordinates after j do the reverse; the j pair has at most L^2
choices. Cauchy--Schwarz and the identity give

    ||v-vbar||_0,B^2 <= d ||dv||_B^2.                (Poi)

For a function u with `r_B u=0`, put `v=G_B u`. Since all R_Bx
are within d kappa of 1,
`|vbar|<=d kappa ||u||_0,B`. Combining (Poi) with
`||dv||<=||D_U u||+sqrt(d) kappa ||u||_0,B` gives

    ||u||_0,B^2
       <= 2d||D_U u||_B^2+3d^2 kappa^2||u||_0,B^2,
    ||u||_0,B^2 <= 4d||D_U u||_B^2.                  (Poi-U)

The last absorption uses `3d^2 kappa^2=3/16<1/2`.
Sum over frozen blocks and use (EXT). The exact extension estimate
needed before the fine lifting is therefore

    ||E_U^0 u||_0 + ||D_U E_U^0 u||
       <= sqrt(2(1+4d)) C_ext ||D_U u||_Omega.        (E-D0)

No bound on a derivative across the frozen/free boundary was put
on the right side. Substitution of D-coer's Step (3) into (E-D0)
gives (E-D), conditional only on that step's stated input bound.

## 6. Match to O1 and the order of constants

**discharged (conversion of the flux convention).** For an
anti-Hermitian plaquette logarithm F and the Hilbert--Schmidt norm,

    e^F X e^-F-X = integral_0^1 e^(tF)[F,X]e^(-tF) dt,
    |[F,X]| <= 2 |F| |X|.

The last inequality follows from
`|FX|_HS<=||F||_op|X|_HS<=|F|_HS|X|_HS`, and the same bound for XF.
Conjugation is isometric. Hence `||Ad(e^F)-1||_op<=2|F|`.
A different fixed normalization of su(2) changes only this fixed
factor.

**implication (the consumer's background, precisely).** The extension
in D-coer is performed after `u=r^(k) omega`, at level k=n-1, as
recorded in Section 1. The class-reference assertion at
`sector-values.md:17` is

    flux(V^*(V')) <= C_r L^-1 T_2.

`one-step-closure.md:11` defines the class by `flux<=T_2`;
`analytic-lift.md:9` explicitly assumes this at each level.
The threshold scaling `T_2=C a_*/L^2` is stated at
`parts/hard-core--mapped.md:794,804`. Write its fixed constant as
A_T, and put `A_ref=A_T max(1,C_r)`. These stated class inputs give
`sup_p |F_p(V_k)|<=A_ref a_*/L^2` on the lattice where E0 acts.
Choosing

    a_* <= 1/(8 d^2 A_ref)                           (small)

therefore implies (BG), by the preceding conversion. This is a
conditional use of the class-reference assertion, not a proof of
(R3) or of existence of that reference. In particular it does not
deduce a pointwise bound on the arbitrarily fine U from an L^4 bound;
the warning at `fibre-propagator.md:192` is respected.

The one-level mean used here has coordinate contours. If a different
consumer uses rerouted contours, (EXT) applies only after checking
their in-block length bound. Nothing about rough-cell rerouting is
needed for the class reference here; `composite-adjoint.md:116`
explicitly separates those cases.
The identification of this transported average with the consumer's
`r^[k]` is used as stated at `fibre-propagator.md:23`; the nonlinear
block-map identities underlying that statement are not rederived here.

**implication (O1).** With the class input just specified, insert
(E-D0) into D-coer's Step (4). The geometry-dependent constant in
F-D is absolute. If the remaining assertions of F-D at
`fibre-propagator.md:122-128,162-172` hold, its inverse has the
claimed absolute exponential rate on every frozen staircase.
If, in addition, the pinning/cumulant estimates HS-P and HS-T and
the gas bounds (A1'), (A2) used in `sector-values.md:47` hold, O1
has its stated rooted derivative bound. Those analytic assertions
are not discharged here. There is no numerical premise in the
geometry or the extension being substituted.

**discharged (constant dependence of this repair).** The displayed
C_ext is fixed using d=4 alone. Thus it can occupy the C_ext slot
before L in the current order at `parts/hard-core--mapped.md:24`.
It may reduce the absolute rate subsequently obtained from F-D,
but it introduces no L dependence and no factor per RG level.
Condition (small) is imposed when a_* is chosen after L, so it
does not reverse that order. No larger L is used to offset the
large explicit extension constant.

**unchecked (O2 and O3's separate analytic inputs).** The convex
interpolation in O2 still requires the rate `mu_c(L)` specified
at `sector-values.md:310`; an absolute rate for its two endpoints
does not by itself prove an absolute rate for the interpolation.
O3's tail and weight keep that slower rate and their stated fixed
relative loss. This note supplies no new justification of their
covariance, Taylor or tail bounds. Since the staircase construction
does not fail, the alternative of replacing O1's rate by a slower
Combes--Thomas rate is not needed to repair this item.

## 7. Provenance and closing status

**discharged (provenance and scope of inspection).** Read: GOAL;
FINISH's independence and rules sections; the order, O1--O3, SRC,
current consumers and hostile rate clauses in sector-values; F-D,
D-coer and their relevant settings in fibre-propagator; the current
mapped obligation and constant-order entries; closure Sections 1
and 10 and the indicated earlier rate comparison; the class setting
of analytic-lift; and the indicated contour definitions in
composite-adjoint. Searches also located background/contour
statements in block-poincare-energy-package. These source files
were checked unchanged against the pinned commit. No sibling
attempt, excluded gate, or numerical check file was read. The only
editable file changed is `library/staircase-by-hand.md`.

**discharged.** G1--G2 prove no pinch at all prefixes and all seams.
(R), (R0)--(R1), (E-s) give the local and global scalar extensions.
Under the explicit level-k bound (BG) and the stated one-level
means, (E0), (EXT), and (E-D0) prove the required covariant extension
and mean correction with an absolute constant. Degenerate torus
sizes and small L are included. These are written arguments; no
check script was opened or run and no reported PASS was used.

**implication.** For the mapped class reference, (BG) follows from
its stated class-flux bound and (small). The extension input needed
for the absolute-rate version of O1 is thus available conditional
on that class-reference bound and the stated identification of the
one-level means. O1 itself additionally needs F-D's remaining
coercivity, fine lifting, saddle and chart assertions, HS-P/HS-T
including the pinning limit, and the named gas bounds.

**unchecked / still open.** This is one author's hand proof with no
independent check. The remaining analytic statements just listed,
O2's interpolated-action bounds, and O3/SRC's nonlinear estimates
are not proved here. A claim of the full O1--O3 or Yang--Mills
argument being discharged would exceed this result. There is no
remaining staircase-pattern or reflection-operator obligation
within the precise hypotheses of (EXT).
