# Local curved coercivity: common frames and the one-wall reduction
Provenance: OpenAI Codex (GPT-6 family; serving variant and configured effort not exposed to this session), commit `dd46a31ef41db19db1d02596f2cfa1e119931ba0`; mapped-side research text, not an audit, grants no status.

## 1. Contract and source boundary

**discharged (scope).** The requested `GOAL.md` and three sections of
`FINISH.md` were read first. This note is the only output. The pinned
`SCIENCE_WORKFLOW.md` was read with `git show`, since it is absent from
the sparse working tree. The specific single-item, single-file instructions
govern this investigation; no campaign, audit, numerical proof, external
posting, or delegation is being undertaken.

**discharged (normalization).** Put the coarser patch scale (S=1), the
other retained scale (h=1/L), and the fine mesh η. Norms use density
η^4 on fine sites/bonds and σ^4 on rows at scale σ. The curvature
in these units is (f(x)=S^2F(Sx)), so

    ||f||_(4,B_1) = S ||F||_(4,B_S).

Here F_p=η^-2 log U_p in the small plaquette branch, H is a
potential-normalized bond field, and
D_Uu(x,ν)=η^-1[u(x)-Ad(U_ν(x))u(x+ηe_ν)]. Adjoint operators
use the displayed density norms. The row norm Λ has the additional
factor σ^-2. The operators C_U, r_U and d_U are the actual composite
gradient-removed rows, hierarchical site means and transported curl
of the specified class map, with a consistent bond-origin convention.

Only boxes covering the actual patch, its row supports, and the backward
read sets of its contours may supply this bound. The hypothesis does not
extend it to a parent-scale box across an unrelated much finer wall.

**discharged (the two targets differ).** The middle inequality of
`fan-ext.md` (9.9) is a site-mean operator comparison on a common bounded
cube. A uniform comparison of every transported path in that frame implies
it by the scalar averaging kernel and Cauchy–Schwarz. The converse is not
asserted: an operator norm controls averaged coefficients, not their
pointwise values. Moreover (C0-loc) also involves bond rows, curl, divergence,
the projected divergence, and one-wall geometry. These are separate
conclusions, even if one transport lemma can supply both reductions.

**unchecked (inherited results at entry).** Printed labels in `lc-u.md`, `fan-ext.md`
and `fibre-propagator.md` are source claims, not independent verification.
In particular, construction of the stationary class branch, its (R3)
bound, flat coercivity, and the final chart identification must each keep
their own scope. No numerical evidence printed in those sources is used.
The flat input is subsequently checked in Section 6; branch construction
and chart admission are not promoted by that check.

**unchecked (memory).** Gauge perturbation, Sobolev, and saddle inverse
methods are familiar from memory. Only arguments actually written and
checked in this note may be labelled discharged; a remembered theorem
alone supplies no step.

## 2. First obstruction tests

**discharged (a concentrated curvature density is not yet a connection).**
Putting magnitude (a/h) on a four-cube of side (h) gives fourth norm
(a), second norm (ah), and face flux scale (ah). A formal sheet can
have a much larger trace, but an arbitrary sheet of one curvature component
violates the cube identity (dF=0) in the commuting sector. It cannot be
used as a counterexample without constructing its link field and checking
all resulting curvature components. Nor does selecting coarse data after
selecting links prove their stationarity.

**discharged (an actual tube, including its return curvature).** Work in
one Cartan direction (Z), normalized by ‖Z‖=1. Choose mesh multiples
η≤w/8≤t/8, taking w and t to be multiples of 8η, and, inside one
fine leaf, put

    U_1(x)=exp(η A_1(x)Z),  U_j(x)=1 (j>1),
    A_1(x)=(α/t) χ(x_1) ∏_(j=2)^4 (1-|x_j|/w)_+.

Here 0≤χ≤1 is supported in an interval of length t and equals one on
its middle half. All plaquette angles are exactly the corresponding
differences of ηA_1; there is no commutator term. For small α the
principal curvature is therefore (F_{1j}=-D_jA_1 Z), with every other
component zero. Counting the support and the middle intervals gives

    2^-20 α^4/(t^3 w) ≤ ||F||_4^4 ≤ 2^12 α^4/(t^3 w).       (2.1)

For the upper bound, each of three components is at most
|α|/(tw), on volume at most 2t(4w)^3. For the lower bound take the
middle half in x_1 and intervals of length w/4 in the other three
coordinates, with one of them in a linear part of its tent. Each
interval contains at least its length/(2η) sites. The derivative
factor is 1/w and the other two tent factors are at least 1/2; these
counts give at least 2^-19, hence the displayed coefficient 2^-20.

A rectangle with one long side on the tube axis, of length t/2, and
its opposite side outside the tube has holonomy exp((α/2)Z), up to
orientation. Thus ||F||_4≤a forces

    |α| ≤ 32 a t^(3/4) w^(1/4) ≤ 32 a t.                      (2.2)

Concentrating transversely makes this holonomy smaller at fixed fourth
norm. Setting t=w gives the four-dimensional lump bound |α|≤32aw.
These are genuine link configurations satisfying the cube identities;
they do not kill the proposed comparison. They are not declared stationary
class fills. At identity prescribed data a commuting small-angle stationary
perturbation in ker Q is even more restricted: testing stationarity with
its potential gives Σ_p (dA)_p sin((dA)_p)=0. For |(dA)_p|<π/2 every
summand is nonnegative, forcing dA=0. Neither test excludes all possible
counterexamples.

## 3. Common frames: the precise reduction to an open-path estimate

**discharged (finite top closure).** Let Q be a cube of side ρ in S=1
units, containing the supported field, every touched row/leaf and their
margins. Take ρ=64(R+1), and reserve an additional fixed multiple of S
for backward contour read sets. Write a_Q=||F||_(4,Q_read). Covering
Q_read by unit boxes gives a_Q≤N_R^(1/4) C a_*, where N_R is their
finite number; it depends on R, not depth or L. This statement is
conditional on having the stated bound on EACH of these boxes.

Suppose the blocked-angle estimate E_j≤2s_j a_Q has been established
through scale S=1. On the S-lattice every plaquette then has angle at
most 2a_Q. A closed coordinate path of length at most m in a rectangular
cube can be reduced to the constant path with at most m^2 elementary
plaquette swaps: reorder its directed steps by coordinate, then cancel
opposite steps. A swap crosses one unit plaquette, and the number of
ordered pairs of steps is at most m^2. Intermediate paths remain in the
coordinate bounding box if each original coordinate segment is first
shortened by cancelling its backtracks. For the paths below an even
safer construction is to fill each segment against the cube's ordered
root path; the total number of squares is at most 4mρ. Either count
is bounded by 2^12(ρ+1)^2.

For orthogonal matrices,

    ||I-A_1⋯A_n|| ≤ Σ_i ||I-A_i||,
    ||Ad(exp X)-I|| ≤ 2|X|,

by telescoping the product and integrating the commutator along exp(tX).
Consequently the remaining top loop costs at most

    2^14(ρ+1)^2 a_Q.                                           (3.1)

This is a surface estimate on a fixed, parent-sized lattice. Applying
the same surface count directly on the fine lattice and substituting
||F||_4 would be invalid.

**implication (the common-frame estimate).** Fix a fine root z in Q and
let J_z(x) be its ordered fine-path frame. Assume the following open-path
coarsening assertion for the actual block map, with a constant K_L
independent of fine depth:

    error at level j ≤ K_L Σ_(B met by the path) E_j(B),
    Σ_(B met by the path) E_j(B)
       ≤ K_L (ρ/s_j)^(3/4) E_j(Q_read).                     (3.2)

The endpoints must be the actual hierarchical contour products; for
bond rows this includes the prefix ending at the selected fine bond.
The second inequality is finite Hölder once the projected path meets at
most K_Lρ/s_j patches with overlap at most K_L. Given these precise
identities and E_j≤2s_j a_Q, summing the first inequality costs

    2K_L^2 ρ^(3/4) a_Q Σ_(s_j<1) s_j^(1/4)
       ≤ 2K_L^2 ρ^(3/4) a_Q/(L^(1/4)-1).                    (3.3)

Use the fixed fine path from each row root c to z to define its rotation
O_c. To compare T_(c,x)J_z(x) with O_c, close this path with the path
represented by T_(c,x) and the ordered z-to-x path. All fine endpoint
factors then cancel. After (3.2), close the remaining S-lattice loop by
(3.1). The resulting bound, uniform in the root z, the row, its assigned
endpoint leaf, and x, is

    ||T_(c,x)J_z(x)-O_c|| ≤ K_(L,R) a_Q,
    K_(L,R)=8K_L^2(ρ+1)/(L^(1/4)-1)
                         +2^16(ρ+1)^2.                       (3.4)

The constants allow both paths and their endpoint corrections. Choosing
one O_c for the whole row requires this closed-path argument; unrelated
O_(c,B)'s for its two leaves would not suffice.

**discharged (dependency separation).** The first assertion of (3.2), including
its endpoint identity for bond-prefix paths, is load bearing.
`lc-u.md` (5.6)–(5.8) is its proposed supplier. Equations (3.1) and
(3.3) alone do not prove it. The next section checks that supplier rather
than treating the geometric summation as an endpoint identity.

## 4. The path identity and its limitations

**discharged (what a one-step replacement actually does).** At one scale,
insert the prescribed contour from the centre of each visited child block
to each path endpoint. The contour at an interior endpoint occurs next to
its inverse, so cancels exactly. For a coordinate segment, the sequence
of block indices is monotone in that same coordinate. Removing repetitions
therefore leaves one coordinate segment, not a growing collection of
segments. For a concatenation of at most eight segments it leaves at most
eight. The number of visited blocks at mesh s is at most
16+length/s; allowing the prescribed one-step enlargements costs a finite
overlap depending only on L and dimension.

An inside-block portion becomes a loop; an adjacent-block portion becomes
a path between their centres. Commute its coordinate steps to the centre
path. Every swap is one plaquette. The inside-block contours have at most
four coordinate segments, each at most L child edges; the adjacent-block
case uses two such contours and a line of at most 2L child edges. Including
a corner and a bond's possible final extra edge leaves fewer than 32L
steps. There are fewer than (32L)^2 swaps. The difference between the
centre path Ω_0 and the blocked link exp(A)Ω_0 costs no more: A is the
mean of the logarithms of precisely these displaced-path loops, each
bounded by the same sum of plaquette angles. Telescoping orthogonal
products thus bounds one replacement by 2^14 L^2 E_j(B).

**discharged (site endpoint).** If x_j is the ancestor of x at level j,
the uncancelled factors after j replacements are exactly

    Γ_(x_j,x_(j-1)) ⋯ Γ_(x_1,x_0),  x_0=x.                  (4.1)

This follows inductively: the next inserted endpoint contour is on the
left of the previous product; all interior inserted contours cancel.
At the leaf level its root is fixed as x varies in that leaf. Equation
(4.1) is the defining kernel path of the composite site average.

**discharged (bond endpoint, including the carry).** Here is that
identification for the positive kernel defined in AD1 of
`composite-adjoint.md`. At level j a row is c=(y,μ); a term chooses
x∈B_j(y) and the t-th bond b of the line from x to
x+Ls_j e_μ, 0≤t<L. Its colour transport p_j is the contour
Γ_(y,x) followed by the prefix ending at tail(b). For δ∈{0,1},
append δ copies of b and call its endpoint q. In each transverse
coordinate q has x's coordinate, and in the longitudinal coordinate

    q_μ=x_μ+(t+δ)s_j,       0≤t+δ≤L.

Since B_j(y+Ls_j e_μ)=B_j(y)+Ls_j e_μ, q belongs to exactly one
of those two half-open blocks. Its parent is therefore y or
y+Ls_j e_μ; write δ' for that alternative. Insert a fixed canonical
endpoint contour Γ_(parent(q),q). The one-step replacement just proved
gives, with transports read as maps from endpoint colour to start colour,

    p_j Ad(U_j(b))^δ
       = Ad(U_(j+1)(c))^δ' Γ_(parent(q),q) + E,
    ||E|| ≤ 2^14 L^2 E_j(B^+).                               (4.1b)

When δ'=0 the coarse factor is the identity. When δ'=1 it is the
actual log-averaged coarse link, not the centre-line holonomy. Their
difference was included in the one-step estimate. At j=0 start with
δ=0. In the next factor of the composite kernel the remaining coarse
link in (4.1b) is precisely the selected bond of that next factor.
Consequently its power δ' is appended to the next prefix, and (4.1b)
applies again. Induction leaves one flag, never two prefixes or a
branching path. The endpoint contours multiply in exactly the order
(4.1), and the final factor is the row link to power zero or one.
Every error is multiplied on both sides by orthogonal maps, so errors
add without growth.

Canonical inserted contours can be fixed once at all endpoints. If a
kernel term uses another allowed axis ordering, compare it to this one
inside that same one-step patch by plaquette swaps. This is already
covered by the 32L step count. Thus averaging over orders or over kernel
terms does not change the bound or the chosen row rotation. At a row
root c, the fixed upward endpoint chain from its fine representative
may be nontrivial; include that chain in O_c. This avoids assuming that
every intermediate block centre equals c. The same convention works at
both endpoints of the row.

**discharged (angle bootstrap on the prescribed class branch).** The
following is the quantitative content needed from the finite block map.
For a parent plaquette, use the same displacement x on its four sides,
translated at each vertex. Use the same chosen contour at a shared
vertex; choosing one common axis ordering preserves each side's averaging
marginal. Endpoint contours then cancel in adjacent factors. Their
product is a conjugate of the boundary of the L-by-L child square.
Its linear plaquette kernel w has row sum L^2
and column sum L^-2. Thus weighted Jensen gives

    Σ_P (Σ_p w(P,p)|θ_p|)^4
       ≤ L^6 Σ_(P,p) w(P,p)|θ_p|^4 = L^4 E_j^4.

In an axial frame on the finite one-step patch, link logs are bounded
by a fixed multiple of L^2 E_j. Choose a radius r_L so all logs involved
stay in the matrix logarithm ball of radius 1/4. On its closed enlargement
of radius 1/3 the exponential and logarithm series and their first two
derivatives converge uniformly. Their maxima, multiplied by the finite
entry and incidence counts, define a finite b_L. Taylor's integral
remainder, after the common first-order term cancels, yields

    E_(j+1) ≤ L E_j+b_L E_j^2,
    e_(j+1) ≤ e_j[1+(b_L/L)s_j e_j],  e_j=E_j/s_j.             (4.2)

The overlapping one-step patches cost only a fixed factor in b_L:
Σ_B E_j(B)^8≤(max_B E_j(B)^4)Σ_B E_j(B)^4. Restricting to backward
read sets can only decrease the column count. If

    a_Q ≤ min{r_L/8, 1/[100(1+b_L)]},                         (4.3)

then E_0=ηa_Q and the first possible violation of e_j≤2a_Q is
excluded by

    e_j/a_Q ≤ exp((2b_L a_Q/L)Σ_(i<j)s_i) < 2,
    Σ_(s_i<1)s_i = 1/(L-1).

The column sum is L^-2 because a fixed child plaquette fixes the two
transverse block/start coordinates and has L possible starts in each
longitudinal coordinate, each of weight L^-4. The nonlinear difference
has zero first derivative: differentiation of exp(mean log) at the
identity is the mean derivative, and products differentiate by summing
the four side derivatives. This proves (4.2) with the specified finite
Taylor constant. It uses the actual class map; a rough rerouting or a
different averaging marginal is outside the assertion.

**discharged (completion of the common-frame comparison).** The counting
in this section allows K_L=2^30 L^8 in (3.2), including the local area,
patch overlap and Hölder factors. For a path with at most eight segments,
the number of one-step patches is at most 2^10ρ/s_j; each plaquette is
in at most 2^16L^4 of their enlarged patches. Hölder therefore costs
at most (2^10ρ/s_j)^(3/4)(2^16L^4)^(1/4), below K_L(ρ/s_j)^(3/4).
The single endpoint error at each level from (4.1b) is bounded by the
same larger expression. This proves (3.2), so (3.4) is discharged.
There is no factor proportional to the number of levels.

**discharged (what is enough for `fan-ext` (9.9)).** With (4.2) and the
site endpoint calculation, (3.4) for site means gives, on a whole common
cube and its interpolation margin,

    ||r^(k)(J_z f)-O average_h f||_N ≤ θ ||f||_2,
    θ=K_(L,R)a_Q.                                              (4.4)

Indeed each block error is at most θ average|f|; square, multiply by
the block volume, and sum disjoint blocks. The same closed-path test
applied to a blocked edge gives
||O_x^-1 Ad(V_k(xx'))O_x'-I||≤θ, with a larger K_(L,R) if needed.
For a parent-sized interpolation chart the radius R in this calculation
is fixed absolutely. Thus θ=C_tr(L)a_Q has the required form. Section 5
below supplies its frame-energy line. The bond-prefix calculation also
gives the transport part of the stronger bond-row comparison needed for
(C0-loc).

**discharged (the residual is an operator estimate, not a path).** Write
Q_j^o=P_j+E_j^op as in AD1. All coefficients of E_j^op vanish at a flat
connection. In a one-step axial frame they are analytic functions of
finitely many link logs. Define q_L≥1 by enlarging the maximum of their
first derivatives on the logarithm ball to include its finite matrix
dimensions, the density conversions, axial-strip factors and overlap.
The fundamental theorem of calculus, entry by entry, then gives

    || |E_j^op| ||_(N_j→N_(j+1)) ≤ q_L E_j.                  (4.5)

Absolute bars mean colour-entry norms before cancellation. The scalar
positive path operator has norm at most one: its row weights and
density-weighted column weights sum to one. On multiplying the factors,

    || |Q^(o,m)-P^(m)| || ≤ ∏_(j<m)(1+q_LE_j)-1
       ≤ 4q_L a_Q/(L-1) =: θ_res,                           (4.6)

provided 2q_La_Q/(L-1)≤1/4. This follows by bounding the product by
an exponential and using exp(t)-1≤2t for 0≤t≤1/2. Extracting a
row at scale σ costs σ^-2 in density norm. Summing row estimates
uses at most eight endpoint supports per scale and two scales.
Consequently, in a common frame and with root rotations removed,

    ||C_flat H_0 - O^-1 C_U H||_Λ ≤ 8L ε ||H||_2,
    ε=K_(L,R)a_Q+θ_res,       H_0=J_z^-1H.                  (4.7)

The factor L is the largest row weight σ^-1, since σ∈{1/L,1}.
The same absolute-kernel estimates apply to localized rows. They will
be paid by smallness of a_Q after L is chosen.

## 5. Frame energy, Sobolev, and the projected graph norm

**discharged (fourth-norm frame estimate).** Comparing the ordered paths
to x and x+ηe_ν gives at most three strips, of width one edge and
length at most ρ. Removing their plaquettes one at a time gives

    |D_(U,ν)J_z(x)| ≤ 2 Σ_strips Σ_(p in strip) η|F_p|.

Fourth-power Hölder on each strip costs ρ^3, and combining three
strips costs 3^3. Average over z and sum over x with density η^4.
For a strip in the ν i plane, unused base-point coordinates cancel
their averaging denominators. In coordinate i,

    avg_(z_i) Σ_(x_i) η Σ_(t_i between z_i,x_i) η |F(t_i)|^4
       ≤ ρ Σ_(t_i) η |F(t_i)|^4.

There are six pairs ν<i. Thus the coefficient for the sum of fourth
powers of directional operator norms is at most 2^4·3^3·6. Passing
to the Euclidean norm of all directional matrix entries costs at most
36 (four directions and three colours), still below 2^18. The identical
argument with squares costs less than 2^12. Choose a root by minimizing
the sum of the two expressions divided by their respective average
bounds. Its sum is at most two. Enlarging constants gives simultaneously

    ||D_UJ||_4 ≤ 64ρ ||F||_4 =: κ,
    ||D_UJ||_2 ≤ 128ρ ||F||_2.                                (5.1)

If F=0 both expressions vanish and any root works. This is an existence
argument on a finite set, not a search used as proof. Since (3.4) holds
for every root, the chosen root also has the common-frame comparison.
On a fixed parent-sized cube, Hölder gives ||D_UJ||_2≤64ρ^2a_Q;
this proves the energy line of `fan-ext` (9.9).

**discharged (lattice Sobolev in the form actually used).** For a finitely
supported scalar v, telescoping along each coordinate gives
|v(x)|≤A_i(x without x_i), where A_i is the line sum of |D_iv|.
Applying Hölder in coordinate four with exponents 3,3,3, separating
A_4 by exponents 3,3/2, and then applying Cauchy–Schwarz in the three
remaining coordinates yields

    ||v||_(4/3) ≤ ∏_i ||D_iv||_1^(1/4)
                 ≤ (1/4)Σ_i ||D_iv||_1.                    (5.2)

For clarity, the three-coordinate step is
∫(A_1(x_2,x_3)A_2(x_1,x_3)A_3(x_1,x_2))^(1/2)
≤(∫A_1 ∫A_2 ∫A_3)^(1/2): first integrate x_3 by
Cauchy–Schwarz, then integrate x_1,x_2 by Cauchy–Schwarz.
These are finite sums with the same density factors as the integrals.

Take v=|H|^3. Orthogonal transport gives Kato's elementary difference
bound, and

    |a^3-b^3| ≤ (3/2)(a^2+b^2)|a-b|,  a,b≥0.

Applying Cauchy–Schwarz and translation invariance to (5.2), then
dividing by ||H||_4^2 when nonzero, proves

    ||H||_4 ≤ (3/2)||∇_UH||_2 ≤ 4||∇_UH||_2.             (5.3)

The same argument at v=|H|^2 gives
||H||_(8/3)^2≤8||H||_2||∇_UH||_2. These statements concern
compactly supported fields extended by zero. For a local box insert a
tensor cutoff on its double enlargement; its derivative is at most
4/side, giving the corresponding mass term. No Sobolev result from
memory is used.

**discharged (means before the projector).** On each leaf B of side
σ choose its own frame with the square estimate in (5.1). The local
version of (3.4) makes its actual averaging kernel within θ_B≤1/4
of one rotation. Hence its Gram matrix G_B satisfies
9I/16≤G_B≤I. Use the tensor interior tent p_B with mean one,
supremum at most 2^16 and coordinate derivatives at most 2^18/σ.
The moment M_B=average(p_B A_BJ_B) has inverse norm at most 4/3.
For φ=D_U*H, c_B=G_B^-1r_Bφ and
g_B=σ^2p_BJ_BM_B^-1c_B, product differentiation and (5.1) give

    r_Bg_B=σ^2c_B,
    ||g_B|| ≤ K_m σ^2 |B|^(1/2)|c_B|,
    ||D_Ug_B|| ≤ K_m σ |B|^(1/2)|c_B|,
    K_m=2^30,                                                   (5.4)

provided σ||F||_(4,B)≤1. The finest leaf uses its site indicator.
For the derivative term involving the frame, use
||F||_(2,B)≤σ||F||_(4,B); all remaining terms differentiate the
scalar tent, including boundary edges. Summation by parts gives exactly

    σ^2 |B| |c_B|^2
       = <D_Ug_B,H> - <P_Ug_B,P_Uφ>.

This follows because <g_B,r_B*c_B>=|B|<r_Bg_B,c_B>; the Gram matrix
has not been replaced by I. Dividing and summing disjoint leaves,
with at most sixteen adjacent-edge occurrences, gives

    ||(1-P_U)φ||^2
       ≤ 2^10 K_m^2 (L^2||H||^2+||P_Uφ||^2).               (5.5)

For a scalar multiplier χ subtract one constant χ_B in each leaf.
The two projector commutator terms are
P_U(χ-χ_B)r_B*c_B and -(1-P_U)(χ-χ_B)P_Uφ. Their norms
sum to at most osc_B(χ)(|B|^(1/2)|c_B|+||P_Uφ||_B).
This records the estimate needed later for cutoffs and exponentials.

**discharged (the graph comparison (8.4)).** Expand curl squared plus
divergence squared and sum differences by parts. Equal-direction terms
give ||∇_UH||^2; each remaining term is a commutator of two covariant
shifts, hence a shift times η^-2(Ad(U_p)-I). Its coefficient is at
most 2|F_p|. The four directions, six plaquette types and shifted
endpoints cost less than 2^12 after Cauchy–Schwarz over their occurrences.
Hölder and the 8/3 estimate above therefore bound their sum by

    2^20 a_Q (||H||^2+||∇_UH||^2).

For the transported-leg convention, its difference from the forward
covariant exterior difference is a sum of at most four terms
η^-1(Ad(U_p)-I)H at shifted corners. Its norm is at most
2^6η||F||_4||H||_4≤2^8a_Q||∇_UH||, since η≤1; this includes
the at most three plaquette orientations using a fixed bond component.
Replacing that exterior difference by d_U in the squared identity
therefore adds at most a fixed multiple of
(a_Q+a_Q^2)||∇_UH||^2, covered by the displayed 2^20 bound after
enlarging it to 2^24. Taking a_Q≤2^-30 absorbs the derivative term.
Insert (5.5) for the missing mean divergence. With
E=||d_UH||^2+||P_UD_U*H||^2, this proves

    ||H||^2+||∇_UH||^2 ≤ C_G(L)(||H||^2+E),
    C_G(L)=2^40(K_m+1)^2L^2.                                    (5.6)

For a uniform-scale model in its own units the same argument has L^2
replaced by 1. Equation (5.6) is an estimate, not a coercivity assertion:
its mass term is still on both sides.

**discharged (differential and projector comparison in the common frame).**
For H_0=J^-1H, subtracting ordinary from covariant differences leaves
products of D_UJ with shifted H. There are at most four legs and three
intermediate transports in a plaquette expression. Telescoping those
products, Hölder, (5.1), and (5.3) give

    (||dH_0-J^-1d_UH||^2
       +||D*H_0-J^-1D_U*H||^2)^(1/2)
       ≤ 2^12 κ ||∇_UH||.                                  (5.7)

In the first term J at the plaquette base is understood; changing its
base costs another one of the included edge products. Let A=O^-1r_UJ
and r_0 be the flat leaf average. Then ||A-r_0||≤ε, ||A||≤1,
||AA*-I||≤3ε and ||(AA*)^-1||≤16/9 for ε≤1/4.
Expand A*(AA*)^-1A-r_0*r_0 into three differences. The bounds just
given yield

    ||J^-1P_UJ-P_0|| ≤ 16ε.                                  (5.8)

Also ||D_U*H||≤2||∇_UH|| by its four directional terms and
translation of the sums. Combining (5.7) and (5.8), with room for both
components, proves

    (||dH_0||^2+||P_0D*H_0||^2)^(1/2)
       ≤ sqrt(E)+2^14(κ+ε)||∇_UH||.                       (5.9)

All L and R dependence in these comparisons is explicit in C_G,
κ=64ρa_Q, and ε; none is assigned to a coercivity constant.

## 6. The flat inputs and their constants

**discharged (flat input checked here; provenance retained).** The flat
argument is from `fan-ext.md` Sections 2–8. The following records its
load-bearing calculations and constants, rather than borrowing the word
"proved" from its heading. All norms here are density norms, d=4.

On a unit lattice block, joining ordered pairs of sites by coordinate
paths in the variance identity gives
||v-average v||^2≤d||Dv||^2: paths have at most dN edges, and a fixed
edge is used by at most N^(d+1) ordered pairs. The zero-extended tensor
bump

    b(m)=∏_i min(1,4(m_i+1)/N,4(N-m_i)/N) / its average

has mean one, supremum 16 and differences at most 64/N, since at least
half the sites in each direction have the unnormalized factor one.
For disjoint unit blocks its mass and derivative squared bounds are

    B_0=16^2,    B_1=4d·64^2.                                 (6.1)

**discharged (all brick fans, not just a planar wall).** A cube of radius
b/64 in the brick tiling of side b meets at most one possible wall
position in each coordinate: these positions are separated by at least
b/8. At a split in coordinate j the lower-coordinate walls in its two
layers have different residues modulo twice their displacement. Thus a
coordinate cannot occur in both descendant branches. The local pattern
is a binary tree with at most four internal nodes, using distinct
coordinates. This covers every assignment of its leaves to Ω or Y.

For such a tree give each leaf score zero initially. At a node with
coordinate z subtract z_+ from every lower-subtree score and (-z)_+
from every upper-subtree score. Scores q are read modulo a common
constant. The inverse formula at that node is

    z=max_(upper subtree)q-max_(lower subtree)q.

Ancestor contributions cancel and each subtree's normalized maximum is
zero, proving this inverse recursively. In maximum norm the score map
and its inverse have Lipschitz constants 8 and 2. If I is the set of
Ω leaves, F(q)=max_I q-max_(I complement)q satisfies
F(q+t1_I)=F(q)+t. Hence q↦q-2F(q)1_I is an involution of Lipschitz
constant 5, fixing the interface and reversing its sides. Its conjugate
in lattice coordinates has Lipschitz constant K_f=80.

Round the reflected exterior point to a nearest lattice site in a
maximizing Ω leaf; walls lie between sites, and the error is at most
1/2 in every coordinate. Keep interior sites fixed. Images of neighbors
are joined inside Ω by at most M_f=4(K_f+2)=328 edges. To verify the
last statement, use their first separating node: before crossing it,
adjust coordinates constrained only in the destination subtree; after
crossing, adjust those constrained only in the source subtree. Distinct
coordinate sets make all these moves stay in the two chosen leaves.
No coordinate backtracks. Each image has at most ν_f=1+(K_f+2)^4
preimages. Cauchy–Schwarz on these paths gives the extension derivative
constant C_f=M_fν_f d(2M_f+1)^d; a source edge can be reached from at
most (2M_f+1)^d starting images and dν_f input edges per image.

For gluing use tensor tents on a grid of spacing

    T_f=328, J_f=1328, r_f=1/(64J_f), B_f=(2T_f+3)^d.

Their sum is one. A reflected nonzero output is within T_f r_f of its
tent centre: a source is within r_f and an exterior point within 2r_f,
so reflection across their intervening boundary costs at most
3(K_f+1)r_f, plus rounding. All source paths lie inside radius J_f r_f,
where the preceding tree describes the actual tiling. At most B_f
outputs overlap. The product rule for the tents gives summed derivative
cost 2||Du||^2+2^(d+2)d r_f^-2||u||^2. If the mesh exceeds r_f, zero
extension instead costs at most 2d r_f^-2||u||^2. Consequently an exact
extension E has

    C_E^2=max{1+2d r_f^-2,
       B_f[ν_f+2C_f+2^(d+2)d r_f^-2 C_f]}.

After gluing, subtract b_B average_B(Eu) on each Y parent. It leaves
every Ω site unchanged and makes every Y parent mean zero. By (6.1)
and contraction of the mean, its squared extension bound is

    A_ext=(1+sqrt(B_0+B_1))^2 C_E^2.                            (6.2)

Everything is absolute; boundary collars must contain the read charts
and the one additional parent length for these mean corrections.

**discharged (fine lift, not the discontinuous least-mass lift).** For
h-grid data v, interpolate multilinearly from the lowest fine vertex of
each h-block. Convexity and corner incidence give
||Iv||^2≤N_0||v||_N^2, ||D Iv||^2≤N_1||D_hv||_N^2, with
N_0=2^d, N_1=2^(d-1). Let e_B=v_B-average_B Iv. Corner paths give
Σh^d|e_B|^2≤E_1h^2||D_hv||^2, E_1=d2^(d-1); separately it is
at most 2(1+N_0)||v||^2. Correct by the h-scaled bumps in (6.1).
The resulting Jv has exactly the prescribed means and

    ||Jv||≤J_0||v||,       ||D Jv||≤J_1||D_hv||,
    J_0^2=2N_0+4B_0(1+N_0),
    J_1^2=2N_1+2B_1E_1.                                        (6.3)

The h^2 in the error estimate cancels the h^-2 cost of the correction's
derivative. No interpolation constant is iterated over fine depth.

**discharged (flat torus estimate).** The flat site operator r is the
box mean and the bond operator Q has one additional box factor in its
longitudinal direction. This follows by multiplying the finite sums
D_L(q)D_M(Lq)=D_(LM)(q); it also gives QD=D'r and rr*=I.
For aliases q=p+2πn in the fine zone, set

    δ_i(q)=(exp(iηq_i)-1)/η, δ'_i(p)=exp(ip_i)-1,
    b_i(q)=ηΣ_(j=0)^(η^-1-1)exp(iηq_i j),
    rhat=∏_i b_i,       ρhat_μ=rhat b_μ.

Phases are kept consistently in QD=D'r. Finite Fourier orthogonality
is the geometric sum of roots of unity. Concavity of sine on [0,π/2]
gives |δ(q)|≥(2/π)|q|, |b_i(p)|≥2/π, and
|δ'(p)|≥(2/π)|p|. Also Σ_alias|rhat|^2=1 and |q|≥|p|.
Thus, for p≠0,

    B(p)=Σ_alias |rhat|^2/|δ|^2,
    B(p)|δ'(p)|^2≥c_1=(2/π)^(2d+2),
    |δ'(p)|^2Σ_alias|ρhat_μ|^2/|δ|^2≤c_2=(π/2)^2.

For QH=0 put φ=D*H, c=rφ, S_B=B^-1,
g=(-Δ)^-1r*S_Bc and β=δ'S_Bc/|δ'|^2. Set these to zero
at p=0, where c=0 since a periodic divergence has mean zero.
Then rg=c, D'*β=S_Bc, and E_0=Dg-Q*β is divergence free.
The component identity

    |δ|^2 I=δδ*+(δ wedge)*(δ wedge)

has cancelling off-diagonal terms. It gives
E_0=d*(-Δ)^-1dE_0 and dE_0=-dQ*β. The preceding bounds give

    ||g||≤g_0||c||,  g_0=(π/2)^2/c_1,
    ||(-Δ)^-1dQ*β||≤b_0||c||,  b_0=sqrt(c_2)/c_1.

Indeed the latter squared bound is at most
c_2 S_B^2|c|^2/|δ'|^4 per parent frequency; for the former use
S_B≤|p|^2/c_1 and Σ|rhat|^2=1. Pairing g with φ and using QH=0
now gives ||c||≤b_0||dH||+g_0||P_0φ||. Hence
||∇H||^2≤C_div(||dH||^2+||P_0φ||^2), where
C_div=1+2max(b_0^2,g_0^2).

Each Q row has nonnegative density of integral one, supremum at most
one and support in a side-3 cube. The variance bound at its start,
followed by |average H|≤||H-average H|| when its Q moment is zero,
and the overlap of at most 4^d such cubes, gives

    C_P=4^d(1+3^d)9d,
    ||H||^2+||∇H||^2 ≤ C_T (||dH||^2+||P_0D*H||^2),
    C_T=(1+C_P)C_div.                                           (6.4)

**discharged (flat one-jump coercivity).** Finer frozen rows imply the
parent QH=0 by composition. Minimize ||H-Dω||^2 over rω=0;
the block variance bound makes this finite quadratic positive definite.
Write H_s=H-Dω, y=||H_s||, x=||Dω|| and p=||P_ND*H||.
Then H_s is orthogonal to Dω, P_0D*H_s=0, dH_s=dH and
y^2≤C_T||dH||^2. Also ||ω||≤sqrt(d)x.
On internal frozen h-bonds, u=r^(k)ω obeys
D_hu=-Q^(o,k)H_s, whose norm is at most y by Jensen. Its unit-parent
means vanish. Apply (6.2), the parent variance bound, and (6.3).
They give a fine w with r_N(ω-w)=0 and

    ||w||≤a_0 y, ||Dw||≤a_1 y,
    a_0=J_0 sqrt((1+d)A_ext), a_1=J_1 sqrt((1+d)A_ext).

Exactly, x^2=<ω-w,P_ND*H>+<Dw,H>. Bound this by
sqrt(d)xp+a_0yp+a_1y^2+a_1xy. The three Young inequalities
sqrt(d)xp≤x^2/4+dp^2, a_1xy≤x^2/4+a_1^2y^2, and
a_0yp≤p^2/2+a_0^2y^2/2 prove

    ||H||^2 ≤ C_F (||dH||^2+||P_ND*H||^2),
    C_F=max{4d+2,(2+4a_1+4a_1^2+2a_0^2)C_T}.                    (6.5)

This is free of L and is known before R is selected. The condition
on w is exactly the retained means, not equality of all fine values
on Ω together with zero fine means on Y.

**discharged (flat row correction).** Put K=2^120 and L≥16K.
On each nontrivial leaf there are at least L sample points per direction.
For p(t) proportional to (1-4|t-1/2|)_+, let a=average(tp) and
v=average((t-a)^2p). The two intervals [5/16,3/8] and [5/8,11/16]
each have p-mass at least 1/128, so the pair variance formula gives
v≥2^-18. The two functions

    p[1-a(t-a)/v],       p[1+(1-a)(t-a)/v]

have moments (1,0) and (0,1) against (1-t,t), by expansion. Tensor
with p in the transverse directions. These bumps separate the two
incident longitudinal rows; other directions are separate components.
Their supremum and coordinate slopes are at most 2^34 and 2^37.
There are at most eight rows per leaf and eight touching derivative
supports, so K bounds their mass and scale times gradient norm.
Finest identity rows use indicators. Lift fine rows first and then
all coarse residual rows. Coarse bumps meet no retained fine row;
the cross term is at most sqrt(2)K/L in the weighted row norm.
Thus the two-step lift B has

    C_flat Bq=q,
    (||Bq||^2+||∇Bq||^2)^(1/2)≤K_*||q||_Λ,
    K_*=16K^2.                                                  (6.6)

Its support adds only the touched endpoint leaves and their neighbors.
Every row touched by the first correction, including a row with initial
value zero, is included in the second. This is an exact supported
correction, not a global inverse with uncontrolled tails.

## 7. (C0-loc) on a coordinate patch

**discharged (absorption, with each error coefficient).** Let C_UH=0
and H have the specified supported read set. Use the common frame of
Section 5 and set q=C_flat H_0. By (4.7) and (6.6),

    b=8K_*Lε,    ||Bq||_(H1)≤b||H||,
    H_hat=H_0-Bq,    C_flat H_hat=0.

The curl/divergence norm of Bq is at most 4||∇Bq||. Equations
(5.6), (5.9) and (6.5) therefore imply, with m=||H||,

    m ≤ sqrt(C_F)[sqrt(E)+e(m+sqrt(E))+4bm]+bm,
    e=2^14(κ+ε)sqrt(C_G(L)).                                 (7.1)

The term e is precisely the derivative and projector error, including
the L in the graph comparison; b is precisely the constraint correction.
Impose

    e≤1/[8(1+sqrt(C_F))],
    b≤1/[8(1+4sqrt(C_F))],
    ε≤1/4,  a_Q≤2^-30,                                     (7.2)

as well as (4.3), (4.6), and the local mean thresholds in Section 5.
Then the coefficient of m on the right of (7.1) is at most 1/4,
and its coefficient of sqrt(E) is at most (9/8)sqrt(C_F).
Thus m≤(3/2)sqrt(C_F E). In particular the convenient absolute
constant

    C_loc=4C_F

satisfies the requested inequality on a coordinate patch. Rescaling
back to S multiplies the mass by S^-2 and leaves both energy terms in
the same units. The entire list (7.2) is a finite positive threshold
on a_* after L and R, through a_Q≤N_R^(1/4)C a_*.

**discharged (periodic bookkeeping requires localization).** A
common frame on a lifted coordinate cube is not necessarily a single
frame on a torus with nontrivial flat holonomy. If a patch wraps around
a period, its distinct lifted occurrences must not be identified in
(4.7). The coordinate-patch proof above does not silently assume that
small curvature kills such holonomy. The following localization supplies
the required correction and the periodic version.

## 8. Localization, TP-sharp, and curved D-coer

**discharged (supported curved correction).** Test the at most eight
incident bond rows and three colour components of one leaf on its
twenty-four flat bumps from (6.6), transported by that leaf's frame.
Sections 3–5 bound its moment-matrix difference from the identity by
2^12K times the local transport-plus-residual error. Require this
quantity to be at most 1/4. The geometric inverse series has norm at
most 4/3 and mixes only these twenty-four bumps. Their covariant
derivatives are bounded by the scalar derivatives plus the bounded
supremum of the bumps times ||D_UJ_B||_2 from (5.1). After shrinking
a_* this gives single-scale lifting constants 2K. Finest identity
rows are exact without a frame. Fine correction followed by coarse
correction, as in (6.6), gives

    C_U Bq=q,
    ||Bq||^2+||∇_UBq||^2≤K_b^2||q||_Λ^2,
    K_b=64K^2.                                                  (8.1)

All the zero moments on unassigned incident rows are imposed too.
Every new coarse row touched by the fine correction is included.
If periodicity identifies two endpoint leaves, split the unfolded
row into its two endpoint occurrences for this finite moment test.
Set the assigned occurrence's moment to the target and the other to
zero, then recombine. The two scalar weights remain (1-t,t); the
rotations may differ between occurrences. These are auxiliary moments,
not extra saddle multipliers. Finest self-identified identity rows
again use their indicators.
Supports add at most 32 parent lengths, a fixed allowance already
required in the local read domain.

For a cutoff with |Dχ|≤c_χ/R and C_UH=0, the absolute row
kernel gives, by its diameter at most 8σ and at most sixteen
two-scale endpoint occurrences,

    ||C_U(χH)||_Λ^2 ≤ 2^15 c_χ^2 R^-2 ||H||_(read)^2.

Put H_χ=χH-BC_U(χH). Covariant curl and divergence product
rules have the same cutoff factor. The projector term is the two-term
commutator after (5.5); its σ oscillation cancels the σ^-1 in that
mean estimate. Therefore, on a squared partition Σχ_i^2=1 with
overlap N=16^4, write e=A N/R^2, where the absolute choice

    c_χ=10N,
    A=2^40(K_b+K_m+1)^2 c_χ^2                               (8.2)

covers the row correction, its derivatives, and both projector terms.
In units S=1 the summed inequalities are

    ||H||^2 ≤ 4Σ_i||H_i||^2+e||H||^2,
    Σ_i E(H_i) ≤ 2E(H)+e(||H||^2+E(H)).                   (8.3)

For example the row correction derivative squared costs at most
2^19K_b^2 c_χ^2/R^2 times the local mass; the projected-mean term
costs at most 2^18(K_m+1)^2 c_χ^2/R^2 times local mass plus p^2.
The remaining at most four-leg product terms fit below 2^16c_χ^2.
Their squared-triangle and overlap factors are covered by (8.2).
Thus (8.3) does not require a bound for the unprojected divergence
independent of L.

**discharged (periodic closure and the final C_0).** Choose an integer
R_1 with

    R_1^2≥2^20(1+C_loc)A N.                                    (8.4)

On an integer periodic cover large enough that each radius-10R_1 cube
is a coordinate cube, use a regular grid of tensor tents, normalize
their squared sum to one, and apply (8.3). For example multiply every
period by 64R_1 and use grid spacing R_1. Each tent is one on its
inner cube, zero outside its triple cube; the quotient derivative is
bounded by 10N/R_1. Overlap is below N. Use the coordinate-patch
constant C_loc on each corrected H_i. Absorbing
(4C_loc+1)e gives

    ||H||^2 ≤ 16 C_loc E(H).

All fields and operators before cutoff are periodic lifts. Their
squared norms are multiplied by the number of copies; division gives
the same estimate on the original torus. Only lifted occurrences are
identified after the sum. No global trivialization of a flat holonomy
has been used. For a supported field in a nest, make the one-jump
continuation only on the read neighborhood of its support; outside
that neighborhood the field and its read rows are zero. Cutoff
corrections read only the reserved margin. This uses no curvature
bound at a remote wall.

The constant valid for both coordinate and periodic cases is therefore

    C_0=16C_loc=64C_F.                                         (8.5)

R_1 is absolute and chosen from flat constants. The caller may enlarge
its R to at least R_1; its later smallness threshold uses the resulting
finite read cubes. In physical units (8.5) is exactly

    S^-2||H||^2 ≤ C_0 (||d_UH||^2+||P_UD_U*H||^2),
    supp H in the admitted one-wall patch,  C_UH=0.             (C0-loc)

**implication (the exact local hypothesis and its boundary).** For every
cube used above the required curvature norm is on its backward contour
read set, including full touched leaves and derivative margins. One
may take Q_read=Q+[-64S,64S]^4 in the coordinate construction; in S=1
units at most (ceil(ρ)+130)^4 unit boxes cover it. Only when those
boxes are part of the admitted patch/read enlargement does the given
local hypothesis bound a_Q. Enlarging a read cube across an unrelated
smaller-scale wall is forbidden: a box at scale s there can contribute
order (S/s)a_* in S units. Equations (7.1)–(8.5) do not convert bounds
on those s-boxes into an S-box bound. If "patch" means only the support
with none of its contour read sets, that is an insufficient specification
of the local hypothesis; this theorem uses the read-set convention in
`lc-u.md` Section 6 and in D1's proposed repair.

**discharged (repair of TP-sharp at a background).** In the uniform-scale
torus model all leaves have scale S=1. Apply (8.5) there. Summing the
unit-box version of (5.6) uses bounded overlap, with no factor L^2;
let G_1=2^44(K_m+1)^2 include the cutoff overlaps. Then

    ||H||^2+||∇_UH||^2
       ≤ C_sharp E(H),  C_sharp=G_1(1+C_0),  Q_U^oH=0.       (8.6)

Every derivative error was estimated by ||D_UJ||_4||H||_4.
The pointwise assertion |Ã|≤CaR in `fibre-propagator.md:75` is
therefore unnecessary. This is a local-curvature theorem on the torus
with the bound on every unit read box, not a torus theorem usable at
an unrelated coarser scale in a nest.

**implication (curved D-coer, including the actual form).** Let
β_U be the stationary chain Hessian, and suppose its absolute local
form estimate is

    |β_U[H,V]-<d_UH,d_UV>|
       ≤ ε_form ||H||_G||V||_G,
    ε_form≤1/[4(1+C_0)],  G^2=||H||^2+E(H).                  (8.7)

On ker C_U, (8.5) implies G^2≤(1+C_0)E. Thus
β_U[H,H]+||P_UD_U*H||^2≤3E/4, proving

    ||H||^2≤2C_0(β_U[H,H]+||P_UD_U*H||^2).                 (8.8)

This proves the curved D-coer reduction without importing the unproved
background transverse decomposition (10.1) of `fan-ext.md`. The form
hypothesis and its stationarity/identification content are addressed
next; a curl-square estimate alone does not identify the fibre Hessian.

## 9. The pruned Ward identity and the form error

**implication (exact hypotheses for the Ward calculation).** Let N_l be
the smooth contour-free chains on the actual class branch, restricted
to the independent retained bond rows. Their differentials at U are
C_l. Assume the actual stationary equation

    DA(U)=Σ_l C_l*λ_l.                                      (9.1)

For a fine gauge parameter ω, covariance of these chains has the
explicit nearby-field form

    DN_l(U') W_ω(U')=D_(N_l(U')) ϖ_l(U'),
    ϖ_l(U)=r^(l)ω.                                          (9.2)

Here ϖ_l is obtained by differentiating the actual coarse gauge
element of the chain, not by choosing a representative through a
stabilizer. At one step that element is
g_l(e^(t v)·V)(e^(t v)|centres)g_l(V)^-1. Differentiating at t=0
defines a linear map R_l(V) on v, smooth in V; at the base point it
is ev-Φ_lD_l=r^[l]. Composition gives the exact recursion
ϖ_(l+1)=R_lϖ_l. These statements use the specified smooth chains;
their existence as charts for a supplied class minimum is a separate
admission input.

Gauge invariance of A and (9.1) give only

    Σ_l <D_l*λ_l,r^(l)ω'>=0 for every fine ω'.              (9.3)

There is no conclusion D_l*λ_l=0 at individual retained levels.

**discharged (compatibility of the differentiated parameter).** Suppose
r_Nω=0 on every present site leaf and put ξ_l=d_(H')ϖ_l at U.
At a retained leaf ϖ_l(U)=0. At a refined node all its descendants
are present leaves; applying the linear recursion upward therefore
also gives ϖ_l(U)=0 there. Differentiating the recursion at a
refined node gives

    ξ_(l+1)=(dR_l)ϖ_l+R_lξ_l=r^[l]ξ_l.                   (9.4)

The first term vanishes on every child involved. On a coarse leaf
there is no demand that its unretained children's ϖ vanish; that
leaf's ξ is prescribed directly. This distinction is essential.

The leaf Gram matrices are invertible by Section 5. Hence one fine
ω' with leaf values r_Nω'=ξ_N exists explicitly:
ω'=r_N*(r_Nr_N*)^-1ξ_N. Inducting up each refined subtree using
(9.4) shows r^(l)ω'=ξ_l at every endpoint of every retained row.
Those endpoints are leaves or refined nodes; a row through an
unrefined larger leaf is not an independent finer retained row.
Thus (9.3) implies Σ_l<D_l*λ_l,ξ_l>=0. No norm bound for
ω' and no level-by-level Ward identity is needed.

**implication (the repaired null identity).** Put

    β_U=D^2A(U)-Σ_l<λ_l,D^2N_l(U)>.

Differentiate D(A-Σ_l<λ_l,N_l>)(U')W_ω(U') using (9.2).
The derivative of W_ω drops out because the first derivative of
this Lagrangian is zero at U. The remaining two terms are

    β_U[H',D_Uω]
      =-Σ_l<D_l*λ_l,ξ_l>
       -Σ_l<λ_l,(d_(H')D_l)ϖ_l(U)>=0.                    (9.5)

The first sum vanishes by (9.3)–(9.4); the second by zero leaf and
refined-node parameters. Also C_ND_Uω=0 by covariance. This repairs
D2 for an arbitrary finite pruned hierarchy under its actual summed
stationarity. It makes no assumption about a trivial stabilizer.

**discharged (size of the Wilson error).** Differentiating the four
plaquette factors twice gives the transported-leg square plus finitely
many terms bounded by 2^8|θ_p|Σ_(b in ∂p)η^2|H_b|^2.
At holonomy I the sixteen ordered leg pairs combine to the square;
replacing the holonomy in any pair by I costs at most |θ_p|.
Use θ_p=η^2F_p and sum incidences. Hölder with exponents
4,8/3,8/3, the local version of (5.3), and (5.6) bound the bilinear
error on a one-wall patch by

    2^30 C_b a_* C_G(L) ||H||_G||V||_G.                         (9.6)

Here C_b is the stated local-curvature constant times the fourth root
of the fixed number of unit boxes read by one row. The same estimate
holds with absolute coefficients. A pointwise potential or curvature
bound has not been substituted.

**implication (the multiplier and second jet).** Test (9.1) with the
exact supported lift of a unit row at scale σ. Its gradient norm is
at most K_bσ; its support uses a fixed number of coarser read boxes.
The first variation is bounded by curvature's second norm times that
gradient. Including the row density σ^4 gives

    σ^3|λ_c|≤C_λ a_*,   C_λ=2^20 C_bK_b.                 (9.7)

In a leaf rescaled to one, let t_j=s_j/σ. Define J_(2,L) as the
maximum of the one-step chain's second derivative on the closed
logarithm ball, enlarged by its finite entry and overlap counts.
Then its angular second jet is bounded by
J_(2,L)Σ_b|θ_b|^2. This is a finite analytic maximum, specified
independently of depth. Define q'_L likewise for the residual in the
angular adjoint supremum norm. The positive path adjoint decreases
that norm by L^-3: a child bond lies on L of the L^4 starting lines.
The product of relative errors is at most two if

    C_ba_*≤(L-1)log(2)/[8L^3(1+q'_L)].                       (9.8)

Thus the backward multiplier is at most 2t_(j+1)^3Λ, with
Λ=σ^3|λ_c|, and the forward potential density norm is at most
twice the input norm by (4.5)–(4.6). Converting the squared angular
field to its density norm costs t_j^-2. A level's contribution is
therefore at most

    8 J_(2,L) Λ t_(j+1)^3 t_j^-2 ||H||^2
       =8 J_(2,L) L^3 Λ t_j ||H||^2.

Summing t_j costs 1/(L-1). With polarization and incidence allowances,
one may take

    C_J(L)=32 C_λ J_(2,L)L^3/(L-1),
    C_form(L)=2^30 C_b C_G(L)+2^8L^2 C_J(L).                    (9.9)

On a two-scale patch, σ^-2≤L^2 S^-2 and endpoint supports overlap
at most sixteen times. This proves (8.7) with
ε_form=C_form(L)a_* once its smallness threshold is imposed.
The estimate is also valid for the matrix of absolute bilinear
coefficients before cancellation: each bound above was applied in
that form. Its two endpoints are in one row support, of diameter at
most eight parent lengths. These facts, not merely a signed quadratic
inequality, will control conjugation.

**unchecked (identification boundary).** Equations (9.1), (9.2) and
the specified N_l make this the stationary *chain* Hessian. Identifying
its Schur form, after compatible coarse gauge changes, with the actual
class-coordinate Hessian M_Y remains an input about the chosen class
minimum and chart. The repaired summed Ward identity removes the
particular D2 obstruction; it does not prove existence of that minimum
or of its chart for all recursively generated data.

## 10. Several jumps: (NC) and F-D with an absolute rate

**implication (admitted geometry).** Take a finite pruned hierarchy of
whole parent blocks, with the prescribed brick tilings, adjacent-scale
interfaces, and

    F_l+[-t_0s_l/4,t_0s_l/4]^4 ⊂ F_(l+1).

This includes every truncated top. In the notation of `lc-u.md` (7.3),
the additional test at each new top t is precisely

    Σ_t^new+[-t_0s_t/4,t_0s_t/4]^4 ⊂ F_(t+1)^(old/current).    (10.1)

Quietness does not supply this inclusion. Choose the geometric integer
t_0, compatible with the brick and parent lattices, at least
max{10^4 R L^2,4r_S L}, and retain the enlarged width 6t_0.
The local curvature hypothesis and class branch must hold on every
actual read enlargement in this domain, not at arbitrary top scale.

**discharged (cover without a depth factor).** Write σ(x) for the
retained leaf scale and set

    w(x)=sup_y{σ(y)-dist_∞(x,y)/(1000R)},  r(x)=Rw(x).

The triangle inequality gives Lip(r)≤1/1000. The collar in (10.1)
separates a point of scale s_k from any scale s_m≥L^2s_k by at
least t_0s_m/(4L^2)≥2500R s_m. Such y contributes negatively to
the supremum. Thus σ≤w≤Lσ. On a boundary F_l, continuity from
its two sides gives w=s_(l+1).

Choose disjoint cubes of radius r(x) in decreasing order of radius.
A rejected centre lies in twice an intersecting chosen cube. In a
tenfold cube radii differ by at most one percent; comparing the
volumes of the disjoint original cubes bounds total multiplicity by
N=16^4. Two distinct scale walls cannot meet such a cube, since
their boundary values of w differ by at least L. The same reasoning
on a hundredfold cube still works: the variation is at most ten
percent. It covers the common-frame read enlargement as well.
Tensor cutoffs, equal to one on the inner cover and zero on triple
cubes, normalized by the square root of their squared sum, have
sum χ_i^2=1 and derivative at most 10N/(RS_i), S_i=w(x_i).
Fine-cell margins fit for the chosen large R. Local periodic lifts
and the covering argument of Section 8 handle capped periods.

**discharged (repair of (NC)).** The coarser retained scale of a
wall patch is at most 2S_i. Enlarge its local constant to
C_wall=4C_0 for this comparison. Put

    W=||H/w||^2,    E=||d_UH||^2+||P_ND_U*H||^2,
    R^2≥2^20(1+C_wall)A N.                                   (10.2)

Apply the supported curved correction (8.1) to each χ_iH. Its
summed estimates (8.3) now read
W≤4Σ_i S_i^-2||H_i||^2+eW and
Σ_i E(H_i)≤2E+e(W+E), e=A N/R^2. Apply (C0-loc), not a flat
lemma at an unproved pointwise approximation to U. The terms to
absorb are (4C_wall+1)eW, and the coefficient of E is
8C_wall+4C_wall e. Hence

    W≤16C_wall E.                                             (10.3)

The source's s^# can be taken to include the 1000R coarse-scale
collar, so w≤s^# and (10.3) implies its stated (NC). Neither the
original step weight with a narrower unexplained collar nor the
finer weight σ is silently substituted. The false sentence
"U=1 up to Ca_*R_0^2" in the old proof is replaced by Sections 3–7.

**implication (form, inf-sup, and inversion).** Enlarge C_form(L) by
2^20N for the fixed patch incidences and choose a_* so

    ε_*:=2^20N C_form(L)a_*≤1/[100(1+16C_wall)].             (10.4)

The absolute form estimate in Section 9 is then valid on
ᵊ^2=W+E. It gives form norm at most two and kernel coercivity
c=[2(1+16C_wall)]^-1 for K_N=β_U+D_UP_ND_U*.

A row of size σ touches only active scales σ and σ/L: a further
wall would lie within two row lengths, contradicting the collar
t_0σ/(4L^2)>2σ. Lift all rows inside their assigned leaves by
(8.1)'s single-scale construction, calling this R_0. Disjoint leaf
interiors and bounded derivative overlap give

    ||R_0q||_ᵊ≤C_R||q||_Λ,  C_R=2^12K_b.

Its row matrix is I+T. The off-diagonal part raises level exactly
once. Its norm is at most 4K/L, because the mass of a fine lift
carries its fine scale and the coarse row weight divides by the
coarse scale. Different output levels are orthogonal in the row
direct sum. Therefore ||T||≤4K/L≤1/4, without summing over depth.
The finite triangular series gives a right inverse
R_N=R_0(I+T)^-1 with ||R_N||≤2C_R.

For data C_NH=y, write H=R_Ny+h, h∈ker C_N. Completing the square
in the finite positive kernel form gives

    ||h||_ᵊ≤c^-1(||J||_(ᵊ*)+4C_R||y||_Λ).

The functional J-K_NH vanishes on ker C_N; evaluating it on R_Nq
defines its multiplier and bounds its norm by
2C_R(||J||_(ᵊ*)+2||H||_ᵊ). Thus the saddle

    ᵎ_N=[[K_N,C_N*],[C_N,0]]

has inverse norm at most

    M=10(1+4C_R)^2(1+c^-1),                                    (10.5)

independent of L, fine depth and volume. An upper bound independent
of L for the raw constraint operator is unnecessary.

**implication (absolute decay rate).** Conjugate fine fields by e^f
and rows by e^(f(z_c)), with Lip(f)≤δ≤1/16 in top units.
On a row, |f(x)-f(z_c)|≤8δσ_c, and
|exp(t)-1|≤2|t| for |t|≤1. The row weight σ_c^-1 cancels
this scale, so its commutator costs at most 2^10δ||H||.
Curl and divergence product commutators cost at most 2^6δ||H||.
For P_N use the two mean terms after (5.5) with the relative
exponential on each leaf; their cost is at most
2^12(K_m+1)δ(||H||+||P_ND_U*H||).

The plus and minus differentiated expressions pair in the conjugated
quadratic form. If their errors are at most aδ, the product error
is at most (2a+a^2)δ. The curvature and second-jet error kernels
have diameter at most eight top lengths. Their absolute bounds and
(10.4) give at most 16ε_*δ in the same form norm. Including the
row terms, a sufficient common absolute constant is

    C_com=2^40 N(K_m+K_b+1)^2,
    δ_#=min{1/16,(4M C_com)^-1}.                              (10.6)

The geometric inverse series for the conjugation perturbation has
ratio at most 1/4. Consequently

    ||e^f ᵎ_N^-1 e^-f||_(ᵊ*×Λ → ᵊ×Λ*) ≤ 2M.          (10.7)

Since w≤1 in top units, the source norm G^2=||H||^2+E satisfies
G≤ᵊ and ||J||_(ᵊ*)≤||J||_(G*). Thus (10.7) also has the
requested G*×Λ→G×Λ* meaning. No uniform equivalence of these
two graph norms is asserted.

**implication (exactness and the class kernel).** For a source annihilating
fine gauge directions and zero constraint data, test the saddle equation
with D_Uω, r_Nω=0. Equations (9.5) and covariance leave
<P_ND_U*H,P_ND_U*D_Uω>=0. The latter operator on ker r_N is
positive definite: a zero-energy vector is parallel on each bond;
in an ordered-path frame its values are one constant vector, whose
leaf mean cannot vanish because the leaf moment matrix is invertible.
Finite-dimensional positivity therefore implies P_ND_U*H=0.

Now supply the actual class/Schur identification and coordinate
functionals J_i of norm at most C_chart(L), supported in a fixed
number of parent cells. Choose
f(x)=δ_# min{dist(x,supp J_j),dist(supp J_i,supp J_j)}.
Applying (10.7) gives

    |M_Y^-1(i,j)|≤2M C_chart(L)^2 exp(2δ_# d_chart)
                         exp(-δ_# dist(i,j)).                 (10.8)

Here d_chart is the fixed coordinate support enlargement; include it
in the allowed prefactor C(L). The rate (10.6) is absolute, including
opposite walls and along a wall. A prefactor depending on L has not
been used to repair a rate depending on L.

## 11. Inputs, order of choice, and recovery checkpoint

**discharged (order of constants).** First fix the dimension and the
specified block/contour rule, then the absolute constants in (6.1)–(6.6),
C_0=64C_F, C_wall=4C_0, K_m, K_b, N and A. Next choose an integer
R satisfying (8.4) and (10.2). Choose L≥16K. Only then choose a_*>0
small enough for the following finite list, using
a_Q≤C(ceil(64(R+1))+130)a_*:

1. The one-step logarithm radius and angle bootstrap (4.3).
2. The residual product threshold after (4.6), all local mean errors
   at most 1/4, a_Q≤2^-30, and C_ba_*≤2^-60 for the summed
   unit-box derivative comparison in (8.6).
3. The two error coefficients e,b in (7.2).
4. The finite leaf moment error in (8.1) at most 1/4 and its frame
   derivative product at most the reserved K bound.
5. The adjoint product threshold (9.8), and the form thresholds
   (8.7),(10.4).

Every entry is a strictly positive finite threshold for fixed L,R.
Define a_* to be the minimum of these thresholds, decreased by a
factor two. Finally choose t_0 with the stated lower bounds and
lattice divisibility. Depth, volume, data and an admitted U are
quantified after these choices. No threshold may depend on fine depth
or on the number of leaves. The constants C_0, C_sharp, M and δ_#
depend only on the fixed absolute construction; L enters thresholds
and the class-coordinate prefactor.

**implication (what remains supplied, not proved here).** The claims
above have the following precise boundary.

| Input | Role and status in this note |
|---|---|
| Prescribed nested cubical class maps and short axis-ordered contours, or their stated averages | Define C_U,r_U and the positive path terms. Their local algebra and comparisons are checked here. Rough rerouted contours or another logarithm branch are outside this theorem. |
| Actual local curvature bound on every patch read box/enlargement | The analytic hypothesis. Existence of the (R1)–(R3) stationary lift with these bounds is **unchecked** here. Bounds at a remote smaller wall do not supply it. |
| Whole parent leaves, compatible pruning, brick geometry and all top collars | Domain of one-wall and several-wall conclusions. In particular (10.1), which is `lc-u.md` (7.3), remains a producer **gap** for arbitrary recursively admitted data. It is an explicit admission condition here. |
| Smooth contour-free chains and stationarity (9.1) for the actual constraints | Needed for (9.5), the multiplier bound, and the actual Hessian conclusions. Curvature alone supplies none of this. The Ward calculation is an **implication** from these inputs, with the summed identity now proved. |
| Class/Schur identification and bounded local coordinate functionals | Needed only to turn the saddle inverse into M_Y^-1 in (10.8); **unchecked** as a construction for every claimed class fill. The operator inverse (10.7) does not assert such existence. |
| Independent verification | **unchecked**. This is one author's written argument. No independent reader, formalization, audit, numerical enclosure or runner is offered as proof. |

**discharged (decisions).** (C0-loc) and the middle line of `fan-ext`
(9.9) are different statements. The common-frame transport comparison
(3.4), proved by the endpoint/carry calculation and top closure,
supplies both the site-mean comparison and the row perturbation.
The derivative comparison uses an L4 frame bound against lattice
Sobolev, not a pointwise axial potential. Equations (8.6), (9.5),
(8.8), and (10.3)–(10.8) give the requested TP-sharp repair, pruned
Ward repair, curved D-coer, and several-jump conclusion on the stated
admitted domain. None supplies branch existence or the missing top
inclusions for a larger producer domain.

**discharged (source and recovery record).** All source content is pinned
at `dd46a31ef41db19db1d02596f2cfa1e119931ba0`. Necessary passages were
read in bounded ranges: GOAL and the three requested FINISH sections;
the allowed lc-u gate; `lc-u.md` Sections 1–9; `fan-ext.md` Sections
1–10; `fibre-propagator.md` setting, TP-sharp, D-coer/F-D, (NC),
and hostile point (6'); `composite-adjoint.md` AD1/AD0 and their
definitions; `fd-local.md` Sections 1–4 and the local-domain definition;
the energy package's setting and initial lemmas; mapped Text 3.1 and
the (R1)–(R3) paragraphs. The pinned workflow was read by `git show`.
Search hits in allowed sources were retrieval aids, not proof imports.
No forbidden file, gate on the independent attempt, outside AI account,
or external literature was opened. No mathematical run was performed.

The failed tube/lump falsifiers are in Section 2. The recovery crux is
(4.1b): its one carry and fixed endpoint contours are what permit
(3.4) on every row in one common frame. The second crux is the norm
absorption (7.1), whose two coefficients are explicitly small by (7.2).
Any change to the contour rule, pruning, read-set admission, or flat fan
geometry requires refreshing those dependencies. The only editable file
changed is this note; no prompt file or platform instruction was changed.

PROVED
