# Block 4: fixed resources for a native Gaussian compiler

Personal continuation, 2026-09-14. Candidate construction and proof plan;
not yet a demonstrated periodic compiler or a selected native law. No agents.
Deadline unchanged: 2026-09-15 01:30:44 UTC.

## Why this route now

Block 3's Gaussian comparison is in PR8124 at
833a47c0b4f5bef43a4935fd22de2ed5d7b8c9c7; its checkout was removed after
remote/PR/clean/ignored-file verification. The interacting logarithm still
ends at a noncircular locality obligation. The native compiler has a distinct
constructive gap that is not a new formulation of the phase estimate.

Main's corrected 2026-08-23 strict-neighbor Gaussian compiler explicitly
leaves a fixed-density periodic finite-type map, seams, full-map cubic
covariance, and a genuine adjacent selector for its untagged S0 carrier.
Its per-edge private-height crossbar is exact on finite fixtures but grows
with the edge roster. Those boundaries were refreshed from the current
note. Its source, codec and fixture formulas must be read before claiming
an instantiation. A tag orbit check alone is not a routing/covariance proof.

There are two new mechanisms to test: an equivariant full-dimensional tag
codec, and a periodic route map using private heights per EDGE TYPE and
coarse color rather than per edge occurrence.

## A. Full-payload finite tags by disjoint open charts

Use the orthonormal Hilbert-Schmidt basis B0=I/sqrt(2), Bj=sigma_j/sqrt(2).
Let G be the 24 proper signed-permutation rotations. v=(1,2,3) has a free
G-orbit. For finite role labels r and frame R, define the Hermitian center

    C_{r,R}=8r B0 + sum_j (Rv)_j Bj.

The centers have strictly positive minimum separation. Choose epsilon=1/4,
to be checked against their exact separation. For z in C^4 define

    E_{r,R}(z)=C_{r,R}
       + epsilon [z0 B0+sum_j(R z_vector)_j Bj]/sqrt(1+||z||^2).    (4A1)

This is a smooth bijection from R^8 onto the open Hilbert-Schmidt ball of
radius epsilon about that center. The finitely many balls are disjoint,
so r,R are decoded from M itself; the radial inverse recovers all four
complex z coordinates. There is no untagged full-payload exception and
no extra continuous coordinate. This uses the continuous M2 possibility
domain and supplied nonlinear charts; it is not finite-bit compression.

For any SU(2) lift U_S of S in G, conjugation gives

    U_S E_{r,R}(z) U_S* = E_{r,SR}(z).                       (4A2)

Unlike changing a scalar frame code by a separate rule, the ambient action
here is an actual M2 star-algebra automorphism. The chart's scalar payload
labels are unchanged while its local Pauli frame rotates. Any desired
nontrivial spinor transformation of the decoded source variables is a
separate correspondence and must not be assumed from (4A2).

In eight real dimensions the radial Jacobian is

    |det DE|=epsilon^8/(1+||z||^2)^5,
    |det D E^-1|=epsilon^2/(epsilon^2-||M-C||^2)^5.           (4A3)

The source Gaussian measure is pushed forward by this chart. If represented
relative to ambient Lebesgue measure, include this inverse Jacobian. A
constant Jacobian would be wrong. Unused payload slots can carry independent
unit complex Gaussians, so all active carrier charts remain eight-dimensional
while only selected decoded slots participate in edges. No finite-precision,
uniform inverse-Lipschitz or axiom-selected reference-measure claim follows.

Initial checks: exact center separation and group action; radial inverse;
analytic/numerical eight-real-dimensional Jacobian; Gaussian integral after
change of variables; a wrong constant Jacobian and wrong frame as falsifiers.

Support qualification to check before any native interpretation: a Gaussian
pushforward under (4A1) has the CLOSED ball as its measure-theoretic support,
although the finite-payload chart image is the open ball. Its boundary has
zero probability and no finite inverse payload. The chart theorem is exact
on finite z and interior M, and probabilistic correspondences are almost
sure; it is not a pointwise decoder of every supported native possibility.
A total boundary readout could be defined separately, but it would not make
the boundary a finite-payload inverse. Preserve this distinction explicitly.

For four independent unit complex Gaussian payloads, ||z||^2 has Gamma(4,1)
law. If r=||M-C|| and d=epsilon-r, the boundary-layer probability should be
exp(-s^2) sum_{j=0}^3 s^(2j)/j!, where
s^2=(epsilon-d)^2/[epsilon^2-(epsilon-d)^2]. The inverse differential norm
on ||z||<=R is (1+R^2)^(3/2)/epsilon; its squared expectation under this
particular Gaussian is 193/epsilon^2. These quantify a possible precision
boundary; they do not remove it or apply automatically to correlated source
payloads with other covariance.

## B. Exact path relay for an arbitrary Hermitian precision edge

For a scalar complex Gaussian precision edge Q_uv=a, a path of L>=2 physical
edges can replace it with h=L-1 private complex variables z1,...,zh.
Delete Q_uv and its conjugate, add 1 to Q_uu and h|a|^2 to Q_vv, give the
hidden path diagonal (2,...,2,1), and use edge coefficients

    Q_{u,z1}=1,
    Q_{zj,z(j+1)}=1,
    Q_{zh,v}=(-1)^h a.                                    (4B1)

Eliminate hidden variables in reverse order. Every pivot equals one. The
off-diagonal sign alternates back to a; the diagonal increments cancel.
Thus the hidden determinant is one, and the Schur complement is the original
precision. A direct tridiagonal inverse should give
(H_hidden^-1)_{11}=1, (H_hidden^-1)_{hh}=h and
(H_hidden^-1)_{1h}=(-1)^(h-1), supplying an independent calculation.
This is a proposed exact identity to check with complex rational edges,
whole small precision matrices, and normalized Gaussian determinants.

The resulting full precision is positive definite whenever the original
one is, because its hidden block is positive and its Schur complement is
the original. Individual local summands need not all be positive. Local
conditional Gaussian measures use the positive on-site precision blocks.

## C. Proposed periodic routing geometry

Input must be an actual finite-type periodic scalar or grouped-payload
precision graph, with bounded integer coarse displacements |delta|_infinity
<=R, at most four payload variables per home, and a checked finite number
of external routed edges per home. Begin with eight external edge endpoints
per home; larger rosters need an explicit port construction, not a count.
Any already local Record-star gadget can remain as a protected finite cluster,
provided its external port budget and geometry are checked.

Choose a coarse color period P>R+1 (e.g. P=2R+2). A home cluster's in-cell
x,y position depends on its finite coarse color and home type. Different
colors, home types and endpoint ports have different vertical-column
positions modulo a large fixed microcell side M. Keep all home/terminal
scaffolds at low fixed z, and assign a distinct higher z offset to each
(edge type, source color). These are finite rosters independent of cover size.

Eight terminal routes can leave a scalar home through four horizontal
neighbors, two payload channels per neighbor. From each such neighbor the
channels move to heights z0-1 and z0+1, then radially to distances 4 and 6
in that horizontal direction. Those distinct x,y endpoints become their
vertical columns. A longer terminal arm can cross a shorter arm's column;
that uses two distinct payload slots, not an identified variable.

An edge rises/descends in its source and destination columns to its private
horizontal plane, then follows an x-then-y Manhattan path. Distinct types
or colors have different horizontal planes modulo M. Equal type/color
occurrences are separated by P coarse cells, exceeding their path-box
extent; this is the proposed noncollision argument. The same color at
different coarse z is separated by P M, exceeding a vertical segment's
span. Thus at most one vertical and one horizontal path should cross at a
point; terminal layers need their own exact occupancy audit. Four payload
slots from (4A1) provide room, but the complete bound must be proved.

All coordinates are to be explicit integer functions of coarse position,
finite type, color and port. The map must be tested on lifted infinite
coordinates first, then quotient covers with periods divisible by P.
Wrap seams require vertex/edge multiplicity checks, not just endpoint
identification. A claim for all cover sizes would need a further construction;
restriction to divisible covers must be explicit if used.

For frame S, rotate the entire microcoordinate and slot map and use chart
frame S R. Prove the covariance square for every mapped carrier and every
edge coefficient, not merely the abstract tag action. Source components
that transform in another internal representation need a separate map.

## D. Boundaries that remain even if this succeeds

An exact local Gaussian marginal is not an autonomous formation process.
Full-condition Gaussian Markov probabilities need not equal probabilities
conditioned only on the subset of already formed records. The fixed tag
pattern, graph, source action, background and reference measure are supplied
conditions, not axioms or selected physical laws. Permanent-record formation
and a selected history law remain distinct. Likewise a 1+1-dimensional source
fixture does not prove a native 3+1-dimensional physical spacetime realization.

Do not claim the corrected DK compiler's full open W_NN is closed until the
actual source graph, grouping, role selectors, finite coefficients, protected
Record star, covariant source action and wrap family have all been matched.
If this particular embedding fails, retain the codec or relay identities as
private tools and reassess. No axiom wall follows from that failure.

## E. First checks and source reading, 16:09 UTC

The first codec/relay runner passed: 1,728 role/frame/action cases, exact
frame separation squared 6, an independent ambient star-product check,
eight-real-dimensional finite-difference Jacobians, a normalized pushed
Gaussian radial integral, and exact complex-rational Schur/determinant
identities for paths of 2 through 10 edges. These are author checks of finite
instances, not an independent review or a periodic compiler certificate.
The boundary-layer calculation confirms the support qualification above.

The actual fixture supplier and primary compiler were read through their
source construction, factor splitting, Record bridge and route assembly.
The finite supplier has source cover T=12, physical half-cover T/2, widths
4/8, an antiperiodic fold, pinned slices and a supplied nonuniform background.
The source is 1+1-dimensional. Repeating a disconnected finite fixture would
not establish a connected arbitrary-cover physical source family and must
not be passed off as one. The current proof target is therefore first a
conditional periodic graph compiler, followed by source matching where the
hypotheses are actually verified. The existing protected Record-star packing
is not covered by the separated-home eight-port geometry without an extra
cluster escape construction.

For the first generic graph construction use separated homes and eight ports.
A single periodic four-payload home with three axial edge types and a body
diagonal edge type saturates eight endpoints and exercises all three coarse
directions. All edges will be routed, including wrap seams. This is a genuine
connected periodic test family, but it is not yet the DK source family.

## F. Explicit map and all-volume occupancy proof

The prototype now implements the following finite formulas. Number the H home
types and E edge types. At most four complex payloads are at each home and at
most eight routed edge endpoints are incident there. Let P=2R+2, C=P^3 and
q=ceil(sqrt(CH)). For color c=n mod P, let i(c)=(c_x P+c_y)P+c_z and
j=H i(c)+h. With z0=8, set

    M=max(20q+20, z0+16+EC)+16,
    home(n,h)=Mn+(10+20(j mod q),10+20 floor(j/q),z0).

The role/coordinate assignment is periodic under n -> n+P k with physical
translation MP k. Homes and their radius-six horizontal scaffolds fit strictly
inside the x,y microcell, and all distinct (color,home) scaffolds have disjoint
horizontal projections. Ports 2d,2d+1 use the four horizontal directions d:
first step one unit along d, then to z0-1 or z0+1, then along d to distances
four or six. The resulting eight column positions are distinct.

Edge type e from (n,h) to (n+delta,h') uses the two assigned endpoint columns
and the plane

    z=max(n_z,n_z+delta_z) M+z0+8+e C+i(n mod P).

Its horizontal part moves first in x and then in y. All offsets of these
planes are strictly between the terminal layers and M. Every segment is
nearest-neighbor by construction. A crude uniform path-length bound is
L <= (3R+4)M+16. Constants depend on the finite input roster, never the cover.

Here is the occupancy argument on the infinite lifted lattice, before taking
a periodic quotient. Equal horizontal planes require the same edge type,
source color and source z coordinate (the endpoint maximum shift is fixed
by the edge type). Any two distinct such occurrences
have an x or y source displacement of at least PM. The corresponding path
boxes have width at most (R+1)M, strictly less than PM, so the horizontal
paths cannot meet. Thus there is at most one horizontal path at any site.

Column positions modulo M identify the home color, home type and endpoint
port uniquely. Equal lifted x,y coordinates therefore fix source/destination
home x,y and allow only z translations by PM of the same column role. Each
vertical segment has length less than (R+1)M, less than PM, so these translated
segments cannot overlap. Thus at most one vertical segment visits a site.

At terminal levels horizontal routing planes are absent. For each home the
two ports in a given horizontal direction share their first neighbor and
then separate to levels z0+-1. A column at radius four may cross the upper
arm at level z0+1, using two distinct scalar variables. The radius-six column
cannot meet the lower arm, whose radius is at most four. Different directions
and different home scaffolds do not intersect. A column from another z copy
cannot reach the local scaffold because its span is less than PM minus the
scaffold margin. Consequently terminal sites also have load at most two.
No route visits any home. Homes have at most four variables, every other
active site at most two. Unused chart slots can be independent Gaussian
spectators, and shared physical positions never identify scalar variables.

The same argument applies on every cover with each coarse period a positive
multiple of P: lifting a collision from the quotient would produce one of
the forbidden infinite-lattice collisions. A path has coordinate span below
PM in each axis, so it cannot self-alias on such a quotient. Edge occurrences
remain distinct, even when they meet the same visible endpoint; multiplicity
belongs to the scalar graph. Finite local slot order is fixed by the tuple
(edge type, source color, path index), sorted at the physical site's residue
modulo MP. It is unchanged when passing to a larger permitted cover.

For the four-edge, one-home connected test family, P=4 and M=296. The 4^3
cover has 196,288 active sites and 196,864 hidden scalar variables, versus
392,576 and 393,728 on the 8x4x4 cover. The maximum path has 1,522 edges in
both. The check verifies every actual path step and every hidden coordinate,
including 96 and 160 wrap steps respectively; ordinary load is two. This
supports the formulas but the general occupancy proof above is the claim.
The physical microcell volume M^3 is large and mostly inactive. No efficient
simulation, small renormalization factor or finite-precision theorem follows.

## G. A second exact proof of the entire Gaussian marginal

For one path let z0=u and let a=Q_uv, h=L-1. Define the affine triangular
residuals, at fixed visible variables,

    r_j=z_j+z_(j-1)+(-1)^j a v,  j=1,...,h.

Then the routed quadratic form equals

    x* Q x + sum_paths sum_j |r_j|^2.                    (4G1)

Expanding the squares gives hidden diagonal (2,...,2,1), nearest path edges
one, endpoint correction 1 and h|a|^2, and terminal edge (-1)^h a. All
interior z_j--v terms cancel between neighboring residuals. The remaining
u--v term is -a and cancels the source precision edge +a. Thus the final
expanded form is precisely the nearest-neighbor routed form even though
the squares in this proof separately mention the remote endpoint v.

The map (z_1,...,z_h) -> (r_1,...,r_h) is complex affine triangular with
unit determinant. Integration against product d^2z/pi gives one for the
added residual Gaussian. Distinct paths have distinct hidden variables,
even at physical crossings, so this proof composes for the entire graph.
It proves normalization and visible marginal exactly for every permitted
finite cover whenever the supplied visible precision Q is positive definite.
It is also a direct second derivation of positivity, independent of the
tridiagonal inverse used in the first finite checks. Uniform source gaps,
infinite-volume Gaussian existence and native formation are extra hypotheses.

## H. A measurable completion at the supported boundary

The support caveat in A has an explicit remedy if a Borel codec, rather than
a continuous chart everywhere, is acceptable. This is a second codec and
must not silently inherit the first codec's smoothness claim.

Write f(r)=epsilon r/sqrt(1+r^2). Define a radius bijection from [0,infinity)
onto [0,epsilon] by

    rho(r)=f(r)                 if r is not a positive integer,
    rho(1)=epsilon,
    rho(n)=f(n-1)               for integers n>=2.

It is the ordinary radial chart except on the countable collection of
positive-integer spheres. All missing radii f(1),f(2),... are filled by the
next sphere; the first sphere fills the boundary radius epsilon. The center
stays the center. The inverse sends epsilon to 1, f(n) to n+1 for positive
integers n, and all other radii to s/sqrt(epsilon^2-s^2). This is a pointwise
Borel bijection with finite inverse at every point of the CLOSED ball.

Set E_sharp(z)=C+rho(||z||) L_R z/||z|| for z!=0 and E_sharp(0)=C.
The same orthogonal equivariance proof as (4A2) applies. Closed balls remain
disjoint because twice epsilon is less than the center separation. Thus both
role/frame selection and finite payload decoding work at every supported
matrix in these closed balls, including their boundaries.

Every positive-integer sphere has eight-real-dimensional Lebesgue measure
zero. Therefore E_sharp and E agree almost everywhere for any absolutely
continuous payload measure, including every nondegenerate conditional or
joint finite Gaussian used here. Their pushforward probability measures are
identical. The inverse Jacobian density (4A3) still represents that common
measure almost everywhere; it is not a finite density prescription on the
boundary. The total inverse and smooth inverse agree almost surely under
the common measure, and each is to be used with its own pointwise codec.

This is an exact measurable construction, not a robust numerical encoding.
At source radius one its image jumps to epsilon, whereas the limiting image
from nonspecial radii is f(1). Similar jumps occur at every positive integer.
If an extra physical premise requires continuity or stable finite-precision
decoding at every supported possibility, this completion does not meet it.
No such premise is being inferred or added to the native axioms here.

For Gaussian Markov conditionals, the total decoder can define the mean
even for a neighboring boundary value: it assigns that point a finite
payload. This does not determine which conditional is relevant to a partial
formation history or prove the selected Gaussian law is a native dynamics.

## I. Uniform spectral bounds and the local conditional kernel

This is a conditional extension, with the source precision explicitly supplied.
Assume on every permitted cover m I <= Q <= Lambda I for fixed m>0 and finite
Lambda. Let h_* bound the hidden variables per route and a_* the coefficient
modulus. Write all path residuals as A z+B x. The direct sum of path matrices
A has diagonal and first subdiagonal one, so ||A||<=2 and ||A^-1||<=h_*.
For maximum routed endpoint degree d<=8, a crude bound is

    ||B|| <= b = sqrt((1+a_*) d max(1,h_* a_*)).

This follows from the maximum absolute row and column sums: each residual
has at most a unit source-endpoint coefficient and one coefficient of modulus
a_*; a visible variable occurs as a source at most d times or as a destination
in at most d paths of h_* residuals. A mixture of incoming and outgoing paths
still obeys d max(1,h_* a_*). The endpoint assumption is per home, hence also
bounds each variable. Internal home couplings remain in Q.

With T(x,z)=(x,Az+Bx), the routed precision is
T* diag(Q,I) T. Thus

    m_tilde = min(m,1)/(1+h_*(1+b))^2,
    Lambda_tilde = max(Lambda,1)(3+b)^2

are uniform lower and upper bounds. These constants are intentionally crude.
Adding independent unit Gaussian spectator slots preserves bounds after
taking min/max with one. The lower bound depends on fixed geometry and the
supplied source gap; it is not a lower bound uniform as m tends to zero.

On the infinite periodic scalar-slot graph, the resulting bounded strictly
positive nearest-neighbor precision has an inverse by the norm-convergent
series Lambda_tilde^-1 sum_n (I-Q_tilde/Lambda_tilde)^n. At physical graph
distance d the first potentially nonzero term has n>=d, giving

    |(Q_tilde^-1)_(x alpha,y beta)|
       <= m_tilde^-1 (1-m_tilde/Lambda_tilde)^d.

For fixed finite sets, finite-cover covariance entries converge as every
cover period grows: finite polynomial terms agree locally and the remaining
norm tail is uniform. The limiting positive covariance supplies consistent
finite-dimensional complex Gaussian distributions and hence a Gaussian
field. This is a massive supplied comparison; a massless source requires
its own covariance existence/zero-mode argument.

At a site s, collect its four decoded variables y_s (including spectators).
The complete-neighbor conditional of the finite Gaussian has precision
Q_ss, mean -Q_ss^-1 sum_(t~s) Q_st y_t and covariance Q_ss^-1. Encoding this
measure gives a matrix-valued nearest-neighbor conditional kernel. The same
formula is the infinite massive Gaussian specification. This statement is
about full conditional distributions, not probabilities conditioned only
on previously formed records.

A finite coordinate role can include the physical residue modulo MP and
the local scalar-slot roster. If all six neighbors have consistent supplied
roles and frame, one neighbor already predicts the target role by adding its
relative lattice displacement in that frame; the remaining neighbors check
consistency. Thus a single rule can look up the target Gaussian block from
nearest-neighbor role data. Co-rotating the entire graph, frame and matrices
makes the kernel covariant; under translation the relative role arithmetic
is unchanged. The identification of spatial frame with a Pauli frame, the
role pattern, source action and coefficients are supplied conditions. This
does not derive them from the algebra or assert that privileged matrix tags
are selected by the Qubit axiom.

The domain can be stated for six present, consistent neighbor records. It
then supplies one possible conditional write distribution at an isolated
hole. It does not supply a formation schedule, a way to create that boundary
from no records, or a one-pass sampler for the full joint Gaussian law.
Those are distinct process obligations and remain open.

## J. Protected Record cluster match, 16:25 UTC

The actual current width-four, c=1/2 fixture was intercepted just before
its historical crossbar. This is a read/extract probe, not a modified source
certificate. Its 494 routed edges give external home demands S0=8, S1=1,
S2=1. The source SHA and supplier SHA, full scalar roster and coefficients
are recorded in BLOCK4_DK_SOURCE_ROSTER.json. S0 carries p12,p8,p9,z5;
S1 carries y8,y9,z25; S2 carries y12,z28; the center carries h8,h9,h12.

A protected cluster at B retains the Record center B and neighbors
S0=B+(1,0,0), S1=B+(0,1,0), S2=B+(0,0,1), with payload counts 3,4,3,2.
The other three Record neighbors B-e_x,B-e_y,B-e_z are protected blanks:
no auxiliary route may touch them. A width-twenty separated cluster box
replaces a separated home box. The exact terminal template is:

- S0: three ports through +x, three through +y and two through -y. A port
  moves three steps in that direction, branches by -1,0,+1 in the transverse
  horizontal coordinate, and then moves one step up to its column pin.
- S1 and S2: one port each through -x, moving three steps, branching by -y,
  then stepping up. All ten column projections are distinct.

Unlike the earlier candidate plane convention, the final routing plane is
above BOTH endpoints, using max(n_z,n_z+delta_z). Otherwise a descending
column could retrace a terminal's final upward step. This is a real design
correction, not a discarded no-go. With upward columns, direct enumeration
of this fixed template bounds terminal occupancy by three: S0's shared first
segments carry three independent scalar variables; the S1 column crosses
one S2 terminal point with load two; no column crosses the Record center,
other homes or protected blanks. Elsewhere the same one-horizontal/one-
vertical proof applies. All cluster coordinates remain within the separated
box, and all role/slot identities are periodic under MP translations.

A connected grouped periodic stress family with three S0--S0 axial types,
one S0--S1 type and one S0--S2 type has exactly these demands. Its P=4,M=360
fundamental cover has 289,424 active sites and 290,464 hidden scalars; the
8x4x4 cover doubles both. Ordinary load is at most three, S0 load is four,
and every route avoids the three protected blanks. The full-payload tag
codec gives S0 its own decodable role and frame without an adjacent selector.

This matches the finite source's local protected geometry and capacity. It
DOES NOT turn the supplied finite DK action into a compatible arbitrary-cover
periodic source family. The stress edge roster is disclosed and different.
In particular, the antiperiodic fold, pinned slices, source transformations
and single-Record versus periodically repeated contexts still need a source
family theorem before full W_NN closure can be claimed.
