# A quantitative cubical SU(2) fill, without a compactness import

Author: openai/gpt-6-astra/max, mac-mini-codex, item 8.
Source under examination: `c72caef9ea6ca9431d7a529104500fd69aae806d`.
Status: **discharged** for the mathematical statements below, by the proofs
given here; author work, not independently checked or audited. Application
to the unchanged threshold in Lemma OW is **gap**, as explained in
`../parts/hard-core--fill.md`. No numerics are used.

The construction uses vertex gauges and a cubical differential-form
interpolant. Credit for the finite-element viewpoint: Whitney, and the
cubical differential-form framework of Douglas N. Arnold and Gerard Awanou,
[arXiv:1204.2595v3](https://arxiv.org/abs/1204.2595v3). Only that paper's
abstract/bibliographic page was consulted. No theorem from it, Uhlenbeck
compactness, or a lattice interpolation theorem is an input: all the
properties used here are proved below. No novelty claim is made.

## 1. Conventions and elementary holonomy bounds

Identify SU(2) with unit quaternions, the unit sphere in R^4. Its distance
d is the spherical distance, so d(1,-1)=pi. Write theta_p(U) for the
distance of a plaquette holonomy from 1. For a Lie algebra element a,
|a| is its Euclidean quaternion norm; exp(a) has distance |a| from 1
when |a|<=pi. Thus

    |q-r| <= d(q,r) <= (pi/2)|q-r|,       |[a,b]| <= 2|a||b|.       (1)

The first follows from |q-r|=2 sin(d(q,r)/2); the second from quaternion
multiplication. Left and right multiplication and conjugation preserve d.
We orient links from x to y and use U^g_xy=g(x)U_xy g(y)^(-1).

**Lemma H (discharged).** On a rectangular lattice disk D,

    d(1,Hol(boundary D)) <= sum_{p in D} theta_p(U).                (2)

Proof. Attach plaquettes one at a time, first along a row and then row by
row, transporting each added plaquette's loop to the same base vertex.
Cancellation of the edge shared with the current boundary expresses its
new holonomy as the old holonomy times a conjugate of the added plaquette
holonomy. Induction gives a product containing each plaquette once. The
triangle inequality and conjugation invariance give (2). The same argument
applies to a disk triangulated into finitely many polygons: first cut along
a spanning tree of the dual graph; the cut edges occur twice with inverse
transports and cancel. Only (2) for rectangles is used for lattice gauges.

The analogous continuum inequality will also be used, with a proof rather
than an interpolation citation. For a smooth connection A, define edge
transport as the inverse of forward transport P'=-A_t P; a constant
component a on a unit edge therefore gives exp(a). Transport on the
piecewise smooth paths below is defined by the Volterra series: its
order-j iterated integral has norm at most (integral |A_t| dt)^j/j!,
so the series converges uniformly, satisfies the ODE on each piece, and
is continuous in bounded continuously varying coefficients. Uniqueness
follows by iterating the integral equation for a difference, with the same
factorial bound. Since A_t is traceless and anti-Hermitian, differentiating
P^*P and det(P) keeps P in SU(2). On a parametrized disk,
gauge first along its bottom edge and then along the vertical curves. In
this gauge A_t=0 and A_s(s,0)=0. Differentiating the transport ODE gives

    partial_t A_s(s,t)=F_ts(s,t),

where the curvature on the right has been conjugated by the transport.
This identity can also be checked by substituting
A^g=gAg^(-1)-dg g^(-1) into F=dA+A wedge A. Hence the distance of the top
edge's transport from 1 is at most

    integral |A_s(s,1)| ds <= integral integral |F_ts| dt ds.       (3)

The other three boundary transports are trivial. A triangle is the same
argument with the bottom edge collapsed to a vertex, by parametrizing
segments from that vertex to the opposite edge; its Jacobian supplies the
ordinary area. For a connection smooth on pieces with matching tangential
traces, triangulate a planar disk by those pieces and apply (3) on every
triangle. Shared edge transports agree and cancel by the product argument
above. Thus, if the curvature comass on every piece is at most B,

    theta(boundary D) <= B area(D).                               (4)

This includes a disk on a piece interface: use its common tangential
trace. The forms constructed below have a finite polyhedral subdivision,
are smooth up to each piece boundary, and satisfy these trace conditions.

## 2. A quantitative extension of an equatorial gauge

**Lemma E (discharged).** Let d=2 or 3, Q=product_i[0,n_i], with
integer n<=n_i<=2n. On the lattice vertices of boundary Q let h take
values in SU(2), with d(h(x),h(y))<=B/n on its edges, B>=1.
If n>=64B, it extends to all vertices of Q with edge differences at most
H(B)/n, where the following deliberately loose constants suffice:

    M(B)=2^12(1+B),
    delta(B)=2^(-40)(1+M(B))^(-2),
    H(B)=2^16(1+M(B)) delta(B)^(-2).                             (5)

Proof. Rescale each coordinate to [0,1]. Triangulate every fine square of
the boundary by a fixed diagonal. For d=2 the boundary pieces are already
intervals. On a triangle interpolate the vertex quaternions affinely in
R^4 and normalize their sum to unit length. The vertices of a triangle
are within 2B/n<=1/32 of any one vertex in chord distance. Thus the norm
before normalization is at least 31/32. A normalized affine interpolation
has derivative at most twice the affine derivative here; each rescaled
coordinate derivative is bounded by 4B before normalization. This gives
a facewise Lipschitz bound 16B.

The interpolations agree on shared edges. On boundary[0,1]^d, two points
on non-opposite faces can be joined through a common edge with length at
most twice their Euclidean separation, by unfolding the two faces. On
opposite faces their separation is at least 1 and a boundary path through
vertices has length at most 2d. These paths give an intrinsic-to-Euclidean
distance bound 12 for d<=3. Together with (1), the interpolated map f is
M(B)-Lipschitz, in the spherical target metric and Euclidean source metric.

Here is the quantitative replacement for a compactness assertion. Put
M=M(B), delta=delta(B). Cover each of the at most six boundary faces by
small squares or intervals of side at most delta/(100M). Their number is
at most 2^16 (M/delta)^2, since the face dimension is at most 2.
Each image piece has diameter less than delta/50. Its 2delta neighborhood
is contained in a spherical ball of radius 3delta. On the unit S^3 such
a ball has volume as follows: the parametrization
q=(cos u, sin u omega), omega in S^2, has metric
du^2+sin^2(u) d omega^2, hence volume element sin^2(u) du d omega.
Integrating gives

    4 pi integral_0^(3delta) sin^2 t dt <= 36 pi delta^3
                                           < 2^7 delta^3.

Consequently the 2delta neighborhood of f(boundary Q) has volume less
than 2^23 M^2 delta < 2^(-17), whereas S^3 has volume 2pi^2 (integrate
4pi sin^2 t for 0<=t<=pi). There is a point p at distance at least
2delta from the image. A sufficiently close point in a fixed countable
dense subset has distance greater than delta; use such a point as p.

Stereographic projection from p, written without a choice of frame, is

    S_p(q) = (q-(q.p)p)/(1-q.p) in p-perp,
    S_p^(-1)(w) = [2w+(|w|^2-1)p]/(1+|w|^2).

On points at distance at least delta from p,
|S_p(q)|<=2/delta and ||D S_p||<=8/delta^2; these follow from
1-cos(delta)>=2delta^2/pi^2 and the displayed formula. For the global
Lipschitz bound, the same formula gives
|S_p(q)-S_p(r)|=2|q-r|/(|q-p||r-p|), so it is at most
8delta^(-2) d(q,r). The inverse has derivative at most 2 everywhere.
Thus w=S_p f has sup norm at most 2/delta and Lipschitz constant at
most 8M/delta^2.

Let c be the center of the unit cube, rho(x)=2|x-c|_infinity, and
pi(x)=c+(x-c)/rho(x). Extend w by v(x)=rho(x)w(pi(x)), v(c)=0.
For x,x' in the cube,

    |rho(x)-rho(x')| <= 2|x-x'|,
    min(rho(x),rho(x')) |pi(x)-pi(x')| <= 3|x-x'|.

The second inequality follows by subtracting (x-c)/rho(x) and
(x'-c)/rho(x') and using |x-c|<=sqrt(d)rho(x)/2. Hence
Lip(v)<=4/delta+24M/delta^2. Compose with S_p^(-1), use (1), and
restrict to vertices. Its bound is less than H(B), and an elementary
rescaled edge has length 1/n_i<=1/n. The trace is h exactly. QED.

There is no assertion here about extending a map S^3 to S^3. The only
equators used have dimension 1 or 2. At finite n<64B an arbitrary vertex
extension is allowed, with the trivial edge bound pi; the next lemma
accounts for that case separately.

## 3. A bounded gauge on the boundary of a cell

**Lemma G (discharged).** Let Q be a lattice rectangle of dimension
m=2,3,4, all side lengths between n and 2n. Suppose its boundary
plaquettes have theta<=K/n^2; for m=2 this hypothesis is empty.
There is a boundary vertex gauge with

    d(1,U^g_b) <= G(K)/n,
    B(K)=16(1+K),
    G(K)=100pi(1+B(K))+4K+H(B(K)).                               (6)

Proof for m=2. Its perimeter has P>=4n links. If its based holonomy is
exp(a), |a|<=pi, put H_0=exp(a/P). Starting with g(v_0)=1, set
g(v_{j+1})=H_0^(-1) g(v_j) U_j. At the end
g(v_P)=H_0^(-P)Hol=1, so every oriented boundary link becomes H_0.
This is at most pi/(4n), as required.

For m=3,4, let D be the bottom face and the side walls, including their
upper rim, and P the top face. From the bottom corner to any vertex of D,
take the axis-ordered path on the bottom, then the last coordinate straight
up the wall. The tree gauge g_D makes these path transports trivial.
For a bottom link, the loop comparing the two root paths is filled by
strips of total area at most (m-2)2n: move the link past the later
coordinate segments in the axis order. A tangential wall link adds one
vertical strip of area at most 2n. All these strips lie on D. Vertical
links have trivial transport. Thus (2) gives

    d(1,U^g_D_b) <= 6K/n.

An axis gauge g_P on the top face similarly gives 4K/n. On their common
equator, h=g_P g_D^(-1) therefore satisfies
d(h(x),h(y))<=10K/n<=B(K)/n: insert the two gauged link values into
U^g_P_xy=h(x) U^g_D_xy h(y)^(-1) and use the triangle inequality.
When n>=64B(K), extend h over P by Lemma E and replace g_P by
h_tilde^(-1)g_P. It now equals g_D on the rim and its links have angle
at most [4K+H(B(K))]/n. These gauges define one gauge on the entire
boundary. If n<64B(K), take any gauge on the boundary instead:
pi<=64pi B(K)/n<=G(K)/n. QED.

No smooth extension of this boundary gauge to the interior is asserted
or needed. Lattice vertex gauges extend arbitrarily, including gauges
whose continuum representatives would have nonzero degree.

## 4. Exact interpolation, continuum fill, and restriction to lattice links

**Lemma C (discharged).** For Q as in Lemma G, every boundary field has
an extension with those exact boundary links and

    max_{p in Q} theta_p <= E(K)/n^2,
    E(K)=2^20 [1+K+G(K)^2].                                     (7)

If n<32G(K), choose any interior links. Then theta_p<=pi and
pi n^2<1024pi G(K)^2<E(K), so (7) holds. Assume henceforth
n>=32G(K). Apply Lemma G and write its boundary links as exp(a_b),
|a_b|<=G(K)/n<=1/32, using the unique small logarithm.

The needed bound on the ordinary cochain curl is elementary. If a_1,...,a_4
are the signed edge logarithms of a plaquette, alpha=max|a_i|<=1/32,
expand the four exponentials in their absolutely convergent power series.
All terms of degree at least two have total norm at most
exp(4alpha)-1-4alpha<=16alpha^2. Since
|Hol-1|<=theta_p, this gives

    |(da)_p| <= [K+16G(K)^2]/n^2.                               (8)

Rescale Q coordinatewise to the unit m-cube. On any fine boundary face
cell, with local coordinates t_i in [0,1], define a tangential 1-form by

    A_i = n_i sum_{epsilon in {0,1}^{d-1}} a_{i,epsilon}
                     product_{j != i} lambda_{epsilon_j}(t_j),
    lambda_0(t)=1-t, lambda_1(t)=t,       A=sum_i A_i dx_i.        (9)

Here d is the dimension of that boundary face, at most 3, and
a_{i,epsilon} are its parallel i-edge logarithms. This is the tensor
product edge interpolant, written explicitly. Its tangential trace on
each shared subface is the same formula on that subface. On a fine edge
A is constant with integral a_b, so its transport is exp(a_b) exactly.

Each coefficient satisfies |A_i|<=2G(K), hence |A|<=4G(K). On a
fine cell, differentiating (9) shows that the coefficient of dx_i wedge
dx_j in dA is n_i n_j times a convex combination of the oriented
plaquette cochain curls (da) on its parallel ij-faces. The terms are
the two differences of the i- and j-edge coefficients, with their
oriented signs; all other lambda factors are unchanged. Equation (8)
therefore gives the comass bound

    |dA| <= 12[K+16G(K)^2].                                     (10)

The factor 12 bounds three coordinate 2-form coefficients, each at most
4[K+16G(K)^2]; for d<3 it is still an upper bound. Equality of tangential
traces means no interface curvature measure is omitted.

On the unit m-cube put rho=2|x-c|_infinity and pi=c+(x-c)/rho.
For rho>=1/2, ||D pi||<=6 (m<=4). Set psi=0 for rho<=1/2 and
psi=2rho-1 otherwise, so |dpsi|<=4, and define

    A_ext=psi pi^*A on rho>=1/2,       A_ext=0 inside.

The trace is A at rho=1. On each piece its curvature is

    dpsi wedge pi^*A + psi pi^*(dA)
                               + psi^2 (pi^*A wedge pi^*A).

Using (1), (10), and |pi^*A|<=24G(K), its comass is at most

    96G(K)+432K+8064G(K)^2
                              <= 2^14[K+G(K)+G(K)^2].           (11)

The angular sectors and the inverse images of the fine boundary faces
give a finite polyhedral subdivision. Across their interfaces tangential
traces match; at rho=1/2 the form is zero. Thus the hypotheses of (4)
hold, including on fine squares crossing interfaces. Define each interior
lattice link by its A_ext transport. Every rescaled fine plaquette has
area 1/(n_i n_j)<=1/n^2, so (4), (11) imply (7). On every boundary
edge the transport is exactly the gauged original link by (9).

Finally extend g from Lemma G to the interior vertices by g=1 and undo
it: W_xy=g(x)^(-1) U_ext_xy g(y). It equals the original U on boundary
links exactly, and conjugates every plaquette holonomy, preserving (7).
This last operation is purely discrete. It neither assumes a bounded
derivative of the extended gauge nor a smooth trivialization extending
its boundary degree. QED.

This proves the lattice-to-continuum-to-lattice step actually used here.
It does not claim that arbitrary original links admit an L-infinity
bounded global continuum potential in their original gauge. The bounds
are obtained after the proved boundary gauge lemma, and the gauge is
undone only on lattice vertices.

## 5. Fill of a whole complex with prescribed cells

**Theorem S (discharged).** Let a finite rectangular cell complex in
dimension at most 4 refine the unit lattice, with each positive-dimensional
cell's side lengths between n and 2n. Let P be a subcomplex on which fine
links are prescribed consistently and every prescribed fine plaquette has
angle <=t. If t n^2<=K_*, then an extension to the whole complex exists
with exact prescribed links and

    max theta <= C_*(K_*)/n^2,
    K_2=max(K_*,E(0)),
    K_3=max(K_2,E(K_2)),
    C_*(K_*)=max(K_3,E(K_3)).                                   (12)

Proof. On unprescribed 1-cells set all fine links to 1. Fill every
unprescribed 2-cell using Lemma C with K=0, since its boundary has no
plaquettes. Prescribed 2-cells already have bound K_*/n^2. Next apply
Lemma C on every unprescribed 3-cell with K=K_2; then on every
unprescribed 4-cell with K=K_3. At each stage its boundary links are
already fixed and stay fixed, so the cell fills agree on every overlap.
A fine plaquette lies in a single coarse cell or its boundary: the coarse
walls are at integer lattice coordinates. This proves (12) for all
plaquettes, including seam plaquettes. The stages have depth three,
regardless of the number of cells, components, holes, or handles. QED.

The construction can be a Borel function of the supplied links, with
the geometry fixed. Fix the axis orders and triangulations. In Lemma E
choose the first point of a fixed countable dense subset whose distance
from the interpolated image is greater than delta. Such a point exists
by the proof, and each choice test is open in the finite boundary data:
the interpolated image is compact and depends continuously on those
data. For the cycle logarithm at -1 choose one fixed axis. All other
operations are continuous on their chosen branches, including transport
ODEs on finitely many pieces. An arbitrary-interior-link case uses 1.
Thus no measurable-selection theorem is imported. Neither gauge
covariance nor translation covariance of this particular choice is
asserted; (F2)'s existence statement does not ask for them.

## 6. The multiplicative version of (F2), and frozen bricks

**Theorem F2-mult (discharged).** Put K_0=16pi, take 0<t<=1, and
n=ceil(sqrt(K_0/t)). Then K_0<=t n^2<=4K_0. On a hypercubic lattice
torus, or on a full rectangular complex whose outer boundary is
prescribed and regular, suppose theta_p(V)<=t outside a set X of fine
cells containing all plaquettes with theta_p(V)>t. With

    C_a=C_*(4K_0)/K_0,                                         (13)

there is a fill of flux at most C_a t, equal to V off a set within
lattice l^1 distance 8n of X. On a torus this set lies in tube(X) as
defined in `quiet-boundary-rarity.md:45` whenever d_x>=32n. Constants
are independent of x, L, level, depth, volume and the field. They are
large, explicit functions of the displayed numerical K_0 alone.

Proof on a torus of side N>=2n. Partition each periodic coordinate into
integer intervals of lengths between n and 2n: take floor(N/n) intervals
and distribute the remainder among them. Select precisely the coarse
4-cells containing a fine plaquette with angle >t. Let P consist of all
unselected coarse 4-cells and their faces, and prescribe V on P. A
prescribed fine plaquette cannot be rough: any coarse 4-cell containing
a rough plaquette was selected. Theorem S applies to the entire torus
complex. Its bound C_*(4K_0)/n^2 is at most C_a t.

All modified links belong to selected cells; each such cell has l^1
diameter at most 8n and contains a rough plaquette in X. The number of
selected cells is at most 96|X| if X is a union of elementary 4-cells:
each closed 4-cell has 24 two-dimensional faces, and a plaquette is
contained in at most four coarse 4-cells. Thus their volume is at most
1536n^4|X|.
A larger harmless bound 2^16 n^4|X| covers conventions which assign a
plaquette to any incident fine cell. No boundary component count enters.

For the tube inclusion, write F={z:dist(z,X)>2d_x}. If
dist(y,X)<=d_x/2, then dist(y,F)>=3d_x/2>d_x by the triangle inequality,
so y belongs to the tube before outward rounding. The selected cells
lie in that neighborhood.
If N<2n and X is nonempty, the torus's l^1 diameter is at most 2N<4n,
so F is empty and the tube is the entire torus; take the identity field.
If X is empty, keep V. For a rectangular domain use the same proof on
any partition with side lengths in [n,2n] and regular prescribed outer
faces; the existence of that partition is part of the stated geometry.
QED.

**Frozen-brick clause (implication; proof of the stated implication).** Suppose
the frozen sets are unions of the whole bricks specified in Lemma BG
of `fibre-propagator.md:134`, t_0 is a multiple of 8 in fine lattice
units, t_0>=8n, and the ambient periodicity or outer boundary is
compatible with that tiling. Require also that the walls are lattice
vertex hyperplanes (up to one common integer translation), and that every
frozen bond is contained in one of the closed frozen bricks. Call these
precise discrete requirements (FG). Every wall of those bricks has its
coordinate in (t_0/8)Z: every shift in their recursive definition is an
integer multiple of t_0/8. Divide each interval of length t_0/8 into
integer intervals in [n,2n], as above. The resulting global rectangular
mesh refines every brick wall, independently of which bricks are frozen.
Every frozen brick with plaquette angles <=t is a union of unselected
coarse cells. Therefore F2-mult preserves all its links automatically.
This construction depends on V and the fixed mesh only, not on the
chosen frozen mask or on the chain below V. Many frozen boundary
components cause no change in the constants. No local half-space or
manifold theorem from Lemma BG is used.

The clause does not verify (FG) for other conventions assigning crossing
bonds to site-centered blocks. It does not cover arbitrary frozen bonds inside a cell, a
noncompatible periodic brick pattern, or a prescribed outer face with
rough plaquettes. Those are additional problems, not implicit hypotheses
of this proof. It also does not prove compatibility with multilevel
blocking constraints; F2 specifies same-level links only.

## 7. Exact scope

- **Discharged:** (2), Lemmas E, G, C, Theorem S, and F2-mult with (13),
  including exact boundary links and the lattice/continuum bridge.
- **Implication, given (FG) and t_0>=8n:** preservation of all regular
  frozen bricks, with a reference chosen from the level field alone.
- **Gap:** preservation of the *same* threshold t rather than C_a t
  when X is defined by theta>t. Equations (7), (12), (13) do not give it.
- **Gap:** the full use of this fill in Lemma OW and Theorem Z; in
  particular, no (CI-N), (CI-N)^d, (W1), (W2), or energy optimality is
  proved by a sup-curvature fill. No consumer file has been changed.

The former compactness route is unnecessary for the multiplicative fill.
This is not a proof of compactness of connections, and does not turn that
unproved assertion into a premise. No numerical computation was run.
