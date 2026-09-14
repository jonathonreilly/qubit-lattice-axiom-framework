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
