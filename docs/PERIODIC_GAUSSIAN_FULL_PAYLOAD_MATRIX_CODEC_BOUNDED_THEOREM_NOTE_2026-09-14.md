---
claim_id: periodic_gaussian_full_payload_matrix_codec_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "An explicitly supplied finite-type periodic complex Gaussian precision graph with at most four payloads and eight external endpoints per separated home has a fixed-period cubic nearest-neighbor auxiliary realization on covers divisible by the stated color period. The construction preserves the visible Gaussian marginal exactly, uses at most four complex payloads per physical site, and has a covariant full-payload M2 codec with finite role/frame tags. A disclosed protected Record-cluster template is also embedded. A Borel completion decodes every point of each closed matrix support ball, at the cost of discontinuity. Uniform massive source bounds imply uniform compiled bounds. The periodic DK source family, selection of source/action/measure, physical spinor correspondence and autonomous Record formation remain open."
upstream_dependencies: []
runner: scripts/periodic_gaussian_full_payload_matrix_codec_2026_09_14.py
---

# Periodic Gaussian routing with full-payload matrix tags

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

A finite-type periodic Gaussian graph can be routed through the cubic lattice
with a fixed amount of space per coarse cell and at most four complex payloads
at each physical site. The auxiliary Gaussian integral recovers the original
measure exactly. Finite role and frame tags can coexist with all four complex
payload coordinates in M2(C), using disjoint nonlinear charts. An optional
measurable completion includes every supported boundary point in the decoder.
These are conditional mathematical constructions, with large fixed overhead.

## Status, target and supplied premises

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_bounded_theorem_note_2026-08-23
target_blocker_text: "A periodic finite-type bounded-density embedding and its seam/cubic-covariance proof remain open."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Match a coherent arbitrary-cover DK source family to the explicit input hypotheses; treat probabilities conditional on formation separately from Gaussian full conditionals."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit matrix chart, periodic coordinate, Gaussian integral and norm derivations for supplied finite-type graphs; the physical source and process are not selected."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The downstream consumer is the strict-neighbor Gaussian compiler in
`ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-23.md`.
Its current finite certificate uses a distinct height per edge occurrence.
The quoted target is in its paired canonical runner output at main revision
`5deabeb698a27c2c3f68c5df685af2521ef15307`. This note supplies a generic
periodic graph construction and a protected cluster template. It does not
assert that the finite DK fixture already defines the required source family.
All mathematics used here is re-established below; no retained status or
theorem from that contextual source is imported.

The inputs are a finite coarse unit cell, its scalar variables grouped into
homes, a periodic Hermitian precision and its coefficients, a reference complex
Lebesgue measure, and a spatial-frame/Pauli-frame identification. They are
supplied definitions. The role pattern, encoding, coarse scale and Gaussian
action are chosen constructions. The native axioms and the approved scale,
kinetic-isotropy and realized-state primitives select none of these objects.
There are no fitted observations or imported phase estimates. A physical
spinor transformation is not inferred from the scalar payload transport.

## 1. Input graph and exact marginal theorem

Coarse cells are n in Z^3. There are finitely many home types h, each carrying
between one and four complex variables. An external edge type specifies its
source home/slot, destination home/slot, displacement delta in Z^3 and complex
precision coefficient a. Its occurrence at n joins that source to the
destination at n+delta. All coefficients repeat by one coarse cell; a larger
source period must first be incorporated into the finite unit cell. Internal
home precision entries are allowed. The external endpoint count at each home
is at most eight, counting multiplicities and incoming plus outgoing edges.
External self-edges at zero displacement and the same home are internal entries
instead. Assume at least one external type; the edgeless case is on-site.

Let R bound the infinity norm of all displacements, P=2R+2, and let each
finite coarse cover period be a positive multiple of P. Supply a positive
definite precision Q on that cover. With reference product d^2x/pi, its
normalized density is det(Q) exp(-x*Qx). Positivity is a hypothesis, not
something inferred from the geometry or the Qubit domain.

The construction below produces a positive definite precision on visible
variables plus private auxiliaries. Every cross-site term is between cubic
nearest neighbors. Its normalized marginal on the visible variables is
exactly the supplied Gaussian. The number of scalar variables and physical
sites per coarse cell is bounded by constants depending only on the finite
input roster. The map and local slot assignment repeat with period MP for
an explicitly specified finite M. All permitted finite cover seams use that
same map. There is no assertion for arbitrary indivisible cover periods.

## 2. Exact Gaussian subdivision, including normalization

For an external source coefficient Q_uv=a, replace its physical route by a
path of L edges, with h=L-1 private hidden variables z1,...,zh. Delete a
and its conjugate from the visible precision. Add 1 to Q_uu and h|a|^2 to
Q_vv. The hidden diagonal is (2,...,2,1), its consecutive off-diagonal
entries are one, and the endpoint coefficients are

    Q_(u,z1)=1,  Q_(zh,v)=(-1)^h a.                         (1)

All entries use the convention that the quadratic form is x*Qx. Set z0=u.
A direct identity for the FULL expanded routed form is

    routed action = x*Qx + sum_paths sum_(j=1)^h
                            |zj+z_(j-1)+(-1)^j a v|^2.   (2)

To verify it, the squares give each intermediate z diagonal twice and the
last one once. Consecutive z couplings are one. Interior z_j--v terms cancel
between consecutive squares. The remaining u--v term is -a, cancelling the
original source edge, and the remaining last edge is (1). The visible
diagonal increments are exactly those stated above. Individual squares in
this proof mention a remote v; their expanded sum is the nearest-neighbor
quadratic form, so no separate locality is claimed for each square.

At fixed visible variables, the residuals in (2) are an affine triangular
function of the z variables with complex determinant one. Their Gaussian
integral against product d^2z/pi equals one. Distinct paths have distinct
hidden variables even when they cross at one physical site. Therefore (2)
proves positivity, the exact full marginal and normalization for the entire
graph, without an approximation or an extensive determinant omission.

A separate check uses the hidden tridiagonal inverse:

    (H_hidden^-1)_(ij)=(-1)^(i+j) min(i,j),  det H_hidden=1.

Multiplication verifies this formula, including the final diagonal one.
The endpoint Schur complement cancels the visible diagonal increments and
recovers a. Reverse elimination has one unit pivot per hidden variable.
The runner checks both the Schur formula with complex rational coefficients
and the residual identity for every routed path in a complete finite graph.

## 3. Explicit periodic coordinates

Let H be the number of home types, E the number of external edge types,
C=P^3 and q=ceil(sqrt(CH)). For c=n mod P define
i(c)=(c_x P+c_y)P+c_z and j=H i(c)+h. Put z0=8 and

    M=max(20q+20, z0+16+EC)+16,
    home(n,h)=Mn+(10+20(j mod q),10+20 floor(j/q),z0).       (3)

Sort the finitely many incident edge-type endpoints at each home to assign
ports 0,...,7. Ports 2d and 2d+1 use the four directions +x,-x,+y,-y.
From the home they first step one unit in that direction, then to height
z0-1 or z0+1, then radially outward to distance four or six respectively.
These distinct horizontal positions are the vertical column pins. The
whole terminal scaffold fits inside its separated radius-six home box.

An occurrence of type e at n, with destination m=n+delta, uses the plane

    z=max(n_z,m_z) M+z0+8+e C+i(n mod P).                  (4)

Follow the source terminal to its pin, move vertically to (4), move first
in x and then in y to the destination column, descend to its pin, reverse
its terminal and finish at its home. The plane is above both terminals.
All steps are explicit nearest-neighbor integer steps. A crude bound is

    L <= (3R+4)M+16.                                      (5)

Indeed the two vertical spans sum to at most (R+2)M plus terminal margins;
the two horizontal spans sum to at most 2(R+1)M; the terminal arms cost
at most fourteen steps. The slack in (5) covers these margins.

The map is exactly periodic: adding Pk to n adds MPk to every path vertex.
No coordinate or type roster in (3)--(5) depends on the number of cover cells.

## 4. Occupancy and seams for every permitted cover

Consider the lifted infinite lattice first. Equal horizontal planes imply
equal edge type and source color, since the offsets in (4) are distinct
modulo M. Their source z coordinates must then agree. Two distinct such
occurrences differ in x or y by at least P coarse cells. Their horizontal
path boxes have width less than (R+1)M in each direction, strictly less than
PM. The corresponding translated paths cannot overlap. Thus there is at
most one horizontal path at any site.

Column positions modulo M determine the home color, home type and endpoint
port uniquely. Equal lifted x,y coordinates therefore permit only z
translations by PM of the same endpoint role. A column span is less than
(R+1)M, so these translated spans cannot overlap. There is at most one
vertical path at a site. Generic intersections consequently have load two,
with separate scalar coordinates at the intersection.

Horizontal routing planes never occur at terminal heights. The two ports
of a given direction share their first neighbor, with load two, then separate.
A radius-four column may cross the other arm at height z0+1, again with
load two. A radius-six column cannot meet a radius-four arm. Other directions
and other home boxes do not meet. A column of another z copy cannot reach
this terminal because PM exceeds its span plus the scaffold margin. No route
touches any home. Thus ordinary sites have at most two scalar variables;
homes have at most four.

Now quotient by any coarse periods divisible by P. A collision would lift
to a collision of distinct infinite-lattice occurrences, already excluded
or accounted for as a two-slot crossing. Each path's span in every coordinate
is less than PM, so it cannot identify two of its own vertices on a permitted
quotient. Endpoints and edge multiplicities survive the wrap seams. This is
an actual quotient argument, not an inference from resource counts.

At each site's physical residue modulo MP, sort its hidden scalar identifiers
(edge type, source color, path index) to choose their payload slots. This
finite roster is unchanged on a larger permitted cover. Visible home slots
are assigned separately. Unused slots can be independent unit complex
Gaussian spectators. They integrate to one and make every carrier a full
four-complex-dimensional Gaussian chart.

Sites outside the active coordinate map have no routed variables. If a
comparison field on every physical lattice site is desired, fill those
sites with four independent spectator coordinates and their periodic role.
The resulting total site count is the fixed microcell volume times the
number of coarse cells. These are mathematical field variables; assigning
them does not assert that records have formed there. The reserved blanks
below mean sites excluded from the auxiliary routing, without a new claim
about their actual formation state.

## 5. A protected finite Record-star template

One may replace a separated home box by the following explicitly checked
finite cluster. Relative to B, put the center at 0 and three homes at
(1,0,0),(0,1,0),(0,0,1), with payload counts 3,4,3,2 respectively when
listed as center,S0,S1,S2. Protect the other three center neighbors
(-1,0,0),(0,-1,0),(0,0,-1): no route may visit them. Supply external port
demands eight at S0 and one at each of S1,S2, with no routed external edge
at the center. Any supplied internal precision uses only on-site terms
and center-to-S0/S1/S2 edges. Such terms already have the required locality.

S0 has three ports through +x, three through +y and two through -y. Each
moves three steps, branches by -1,0,+1 in the transverse horizontal axis,
and steps up once to its pin. S1 and S2 each move three steps through -x,
branch by -y and step up. Their ten column projections are distinct. All
columns ascend to (4), so no column retraces a final upward terminal step.

The shared initial segments at S0 have load at most three. The S1 column
crosses one S2 terminal point with load two. Listing these ten finite paths
shows that none visits a home, center or protected blank; no other column
intersects a terminal. Outside this fixed cluster the one-horizontal and
one-vertical argument above applies. Separate cluster boxes by twenty units
as in (3), with the grid sized to the cluster-type roster. Thus ordinary
load is at most three and home load at most four, on the same cover family.

This is a supplied template, not a theorem about all Record clusters. Its
port demands match the local shape extracted in the personal campaign from
one current finite DK fixture. The public runner re-establishes the geometry
without importing that fixture. A periodic repetition of the template is a
stress source; it is not silently identified with the finite DK action's
antiperiodic fold, pinned slices or single-Record context.

## 6. Full-dimensional matrix tags and covariance

Use the orthonormal Hilbert-Schmidt basis B0=I/sqrt(2), Bj=sigma_j/sqrt(2).
Let G be the 24 proper signed-permutation rotations and v=(1,2,3). This
vector has a free G orbit. For a finite integer role r and frame R in G set

    C_(r,R)=8r B0+sum_j (Rv)_j Bj,  epsilon=1/4.

Different roles are at least eight apart in their central coordinate.
The minimum squared separation in one frame orbit is six; the finite signed
permutation list verifies it, or compare the possible integer differences.
The closed epsilon-balls are therefore disjoint. For z in C^4 define

    E_(r,R)(z)=C_(r,R)+epsilon L_R(z)/sqrt(1+||z||^2),
    L_R(z)=z0 B0+sum_j (R z_vector)_j Bj.                  (6)

Each E is a smooth bijection onto its OPEN ball. The matrix itself identifies
role and frame from the disjoint centers. If y=L_R^-1(M-C), then
z=y/sqrt(epsilon^2-||y||^2). All four complex payload coordinates survive:
there is no untagged full-payload exception or extra continuous coordinate.
This exploits a continuous possibility domain, not finite-bit compression.

For proper rotation S, the ambient map a0 I+a.sigma -> a0 I+(Sa).sigma
is a star-algebra automorphism. The Pauli product uses the dot and cross
products, both preserved by S, and S is real so it preserves the adjoint.
Equivalently this is conjugation by either SU(2) lift of S. Consequently

    U_S E_(r,R)(z) U_S* = E_(r,SR)(z).                    (7)

Co-rotate the complete spatial coordinate map and its frame, retaining its
scalar slot labels and coefficients. Every mapped vertex, edge, role and
slot then satisfies the same covariance square, and (7) intertwines the
matrix values. This is covariance of a supplied scalar graph in a supplied
frame. It does not prove that decoded fields transform as physical spinors,
or select a source/background that breaks no physical symmetries.

The eight-real-dimensional radial Jacobian is

    |det DE|=epsilon^8/(1+||z||^2)^5,
    |det DE^-1|=epsilon^2/(epsilon^2-||M-C||^2)^5.          (8)

The radial singular value is epsilon/(1+||z||^2)^(3/2); each of the other
seven is epsilon/sqrt(1+||z||^2), proving (8). Push forward the supplied
Gaussian measure. Relative to ambient matrix Lebesgue measure its density
must include the inverse Jacobian. A constant Jacobian gives the wrong
measure. This construction supplies, rather than derives, a base measure.

## 7. Every supported boundary point: a separate Borel codec

For an absolutely continuous full-support Gaussian payload, the pushforward
under (6) has the CLOSED ball as its measure-theoretic support. Its boundary
has zero probability but belongs to the support and has no finite inverse
under the smooth chart. An almost-sure correspondence alone therefore does
not give a decoder for every supported possibility.

A second, explicitly discontinuous codec resolves this pointwise issue. Put
f(r)=epsilon r/sqrt(1+r^2) and define

    rho(r)=f(r)       for r not a positive integer,
    rho(1)=epsilon,
    rho(n)=f(n-1)     for integers n>=2.                  (9)

This is a Borel bijection from [0,infinity) onto [0,epsilon]. Its inverse
sends epsilon to 1, f(n) to n+1 for positive integers n, and other radii s
to s/sqrt(epsilon^2-s^2). Keep the center fixed and replace the radial factor
in (6) by rho(||z||)/||z||. The resulting E_sharp is a pointwise Borel
bijection onto the CLOSED ball, with finite inverse everywhere. It remains
equivariant because the change depends only on the norm. The balls remain
disjoint, so all their supported matrices have a unique role/frame/payload.

The two codecs differ only on countably many positive-integer spheres,
which have eight-dimensional Lebesgue measure zero. Their pushforward
measures are identical for every absolutely continuous payload law. The
inverse Jacobian density in (8) describes that common measure almost
everywhere. It is not a finite boundary density formula. The inverses also
agree almost surely; each pointwise codec must use its corresponding inverse.

At radius one, E_sharp jumps from the limiting radius f(1) to epsilon.
Thus it does not inherit smoothness, continuity or numerical robustness
from (6). If a further physical premise requires such regularity at every
supported possibility, this completion does not establish it. No such
premise is added to the axioms here. Even the smooth chart has no global
inverse-Lipschitz bound. For four independent unit complex Gaussians,
||z||^2 has Gamma(4,1) density, and (8) gives
E||DE^-1||^2=193/epsilon^2; this bound does not automatically apply to other
covariances or to the discontinuous codec at its exceptional spheres.

## 8. Uniform massive bounds and a local Gaussian specification

Assume additionally m I<=Q<=Lambda I uniformly on the cover family, m>0.
Let h_* bound route hidden length, a_* coefficient modulus and d<=8 the
endpoint count per home. In (2) write all residuals as Az+Bx. The path
blocks of A are lower bidiagonal with diagonal/subdiagonal one, giving
||A||<=2 and ||A^-1||<=h_*. Absolute row and column sums give

    ||B||<=b=sqrt((1+a_*) d max(1,h_* a_*)).

Each residual has at most a unit source coefficient and one coefficient
of modulus a_*. Each visible scalar is incident to at most d paths; a
destination appears in at most h_* residuals of each path. These are the
claimed row/column bounds even with mixed incoming/outgoing incidences.

For T(x,z)=(x,Az+Bx), the precision is T*diag(Q,I)T. Bounds
||T||<=3+b and ||T^-1||<=1+h_*(1+b) give

    m_tilde=min(m,1)/(1+h_*(1+b))^2,
    Lambda_tilde=max(Lambda,1)(3+b)^2.                    (10)

Both are independent of cover size. Spectators preserve the bounds after
taking min/max with one. These constants are deliberately crude and need
not remain useful as the source mass tends to zero.

On the infinite periodic scalar-slot graph, the compiled nearest-neighbor
precision has the norm-convergent inverse series
Lambda_tilde^-1 sum_n (I-Q_tilde/Lambda_tilde)^n. Between physical sites at
graph distance D the first contributing term has n>=D. Therefore

    |(Q_tilde^-1)_(x alpha,y beta)|
       <=m_tilde^-1 (1-m_tilde/Lambda_tilde)^D.            (11)

Finite polynomial terms agree locally as all cover periods grow, and the
remaining tail is uniform. Finite-cover covariances converge on every finite
set to the positive inverse above. The associated consistent finite Gaussian
distributions define an infinite Gaussian field. This proves a massive
supplied comparison; massless source covariance existence and zero modes
require separate arguments.

The four decoded variables at s, including spectators, have complete-neighbor
conditional mean -Q_ss^-1 sum_(t~s)Q_st y_t and covariance Q_ss^-1. This
follows by completing the square in the local Gaussian block. Encoding that
distribution gives a nearest-neighbor matrix-valued conditional kernel.
The Borel codec supplies a finite decoded mean even at a supported boundary
neighbor; its extension there is a chosen version on null conditions.

A finite role may include the physical residue modulo MP and the local slot
roster. Consistent neighboring roles/frame determine the target role by
relative lattice displacement. They can therefore select the correct block
using one fixed rule on this supplied domain. Co-rotation and translation
preserve that relative rule. The frame identification, role pattern and
coefficients remain supplied, not axiomatic selections.

This is a FULL Gaussian conditional. It is not necessarily the distribution
conditioned only on previously formed records. With six present consistent
neighbors it can specify a conditional write at an isolated hole. It does
not choose when or where records form, construct those boundary records,
or give a permanent one-pass sampler of the joint Gaussian field.

## 9. Finite challenges, scope and reproduction

The primary runner is self-contained and reads no scientific repository
inputs. Its finite checks exercise the matrix star action, inverse, eight-real
Jacobian and normalized radial Gaussian integral; exact rational path Schur
complements; the optional closed-support inverse; every coordinate and seam
of a connected grouped periodic graph on 4^3 and 8x4x4 covers; multiple home
types and negative/range-two edges; the protected cluster on two covers; a
whole routed action against the independent residual formula; and small
full precision matrices against the congruence and norm bounds.

The main four-edge family has M=296. Its two covers use 196,288 and 392,576
active sites, and 196,864 and 393,728 hidden scalar variables. The maximum
route length is 1,522 on both, ordinary load is two, and home load is four.
Internal home edges connect the scalar species; the three axial types
connect all coarse cells. The protected-template family has M=360, ordinary
load three and maximum home load four. These finite counts challenge the
general formulas; they are not an all-volume proof by enumeration.

Reproduce with:

```bash
python3 scripts/periodic_gaussian_full_payload_matrix_codec_2026_09_14.py
```

The paired output is [the canonical runner cache](../logs/runner-cache/periodic_gaussian_full_payload_matrix_codec_2026_09_14.txt).

The main unresolved consumers are the compatible periodic DK source family
and its physical transformations, action/measure selection, and the process
connecting nearest-neighbor probability kernels to permanent formation
histories. This note does not close full W_NN, select a Hamiltonian or state,
establish a photon phase or TOE, or justify an axiom amendment.

## Review record

Personal author review; independent review and audit remain pending. The
review keeps the smooth open chart separate from the discontinuous closed
codec, keeps scalar graph covariance separate from a physical spinor claim,
and treats the Record template as supplied. Routing planes are above both
endpoints so upward terminal stubs cannot be retraced by descending columns.
The publication claim is the explicit conditional construction, not the
completion of the larger native compiler or formation program.

Eleven source mutations against primary SHA-256
`6f1c835da1722f7892790e056b14113968e1cf15099bdd6836ed10f8df7a2d57`
all produced relevant assertion failures: dropping the fourth complex payload;
transposing its frame; changing the matrix Jacobian; failing to fill the
support boundary; reversing a complex relay sign; reusing edge-type planes;
removing coarse-color column separation; putting a plane below a terminal;
identifying crossing slots; reversing a whole-action endpoint sign; and
overstating the compiled spectral lower bound. These are author challenges,
not an independent reviewer verdict. The canonical cache binds the unchanged
primary and its declared 180-second execution envelope.
