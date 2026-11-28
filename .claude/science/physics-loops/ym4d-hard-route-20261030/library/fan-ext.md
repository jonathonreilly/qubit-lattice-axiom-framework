# Exact extensions at a one-jump brick interface
Provenance: OpenAI Codex (GPT-6 family; exact serving variant and configured effort not exposed), commit `048ba59a20c837f054c1125dc2d9c386fbc887f6`; different provider from the Anthropic author of `fibre-propagator.md` identified by the assignment; research mathematics, not an audit, grants no status.

## 1. Contract, scales, and the first attempted obstruction

**discharged (source identification).** In `fibre-propagator.md:118,124`,
Omega is the frozen region and Y is its free complement. Put n=k+1,
measure lengths in level-n parent boxes, and write h=1/L for the level-k
spacing and eta for the original fine spacing. The actual condition is

    r^(k) w = r^(k) omega on Omega,
    r^(n) w = 0 on Y.                                      (1.1)

There is NO condition r^(k)w=0 on Y. Nor is fine-site equality w=omega
on Omega required. The extension before lifting is of u=r^(k)omega on
the h-lattice, with exact site equality there and zero parent means on
Y. This distinction changes the answer to the proposed wording.

**discharged (the extra two-level requirement is false).** Take U=1,
eta=h=1/L, brick side b=8, and the 8b-periodic quotient in each
coordinate of the tiling (3.1). Let Omega be its one-brick-thick slab
0<=x_4<b and omega(x)=sin(2 pi x_1). This slab is a union of whole
bricks. The coordinate periods are compatible: translating by 8b e_j
changes the indices in (3.1) by 8e_j-4e_(j-1) (omit the second term
for j=1). Write V=b(8b)^3 for the slab volume. Each parent mean is
zero. For L>=3, the geometric sums of exp(2 pi i j/L) and
exp(4 pi i j/L) give

    ||omega||_Omega^2=V/2,
    ||D omega||_Omega^2 <= 2V L^2 sin^2(pi/L) <= 2V pi^2.

The last inequality follows by integrating |cos t|<=1 from 0 to pi/L.
Requiring the finer retained mean to vanish on Y now says w=0 at
every Y site: each finer block is a single site. One interface alone
then contributes

    eta^(4-2) sum_{interface sites}|omega|^2 = LV/(2b)

to ||Dw||^2. Thus the OPTIMAL constant for the literal extra condition
is at least L/[8(1+4 pi^2)]. This is an admissible flat one-jump brick
slab. It refutes the extra condition, not D-coer. Below the question
is corrected to (1.1),
as the assignment permits. No counterexample is being silently
discarded.

**discharged (what the tangential attack does not show).** With only
parent means on Y, continue the same sine across a full unit slab.
It still has zero parent mean, and its mass and tangential energy
per unit volume are those just displayed. There is no L loss.
Killing it in thickness h costs order 1/h; that thickness is not a
requirement of (1.1).

**discharged (least mass is the wrong lift).** For prescribed averages
on adjacent h-blocks the least-L2 fine lift is constant on each block:
expanding sum|v-c|^2 proves this minimization directly. A jump Delta
across their common face has energy Delta^2/eta per unit face area.
The coarse energy is Delta^2/h. Their ratio h/eta diverges with fine
depth. Section 6 will use a different, explicitly bounded lift; the
energy minimizer is bounded by that competitor.

**unchecked (inherited labels).** A source's word "proved" is not a
verification by this note. The background supplier and identification
inputs will be separated from the flat argument. No numerical result
in a source is used as evidence. No mathematical assertion below is
imported from memory; supporting elementary arguments are displayed.

## 2. The difficult mean correction, at its correct scale

**discharged (norm convention).** For a lattice spacing a dividing 1,
set

    ||v||_0,A^2 = a^4 sum_{x in A}|v(x)|^2,
    ||Dv||_A^2 = a^2 sum_{edges internal to A}|v(x+ae_j)-v(x)|^2.

Every unoriented edge is counted once, with periodic multiplicities.
Write ||v||_1,A^2 for their sum. Values may lie in any finite-dimensional
real Hilbert space. Parent blocks are disjoint half-open unit cubes;
brick faces lie on parent faces. Means below are normalized site means.

**discharged (bounded, exact correction).** In a parent block containing
N=1/a sites per direction, define, and extend by zero outside the block,

    psi(m)=product_{j=1}^4 min(1,4(m_j+1)/N,4(N-m_j)/N),
    b=psi/average(psi),                 0<=m_j<N.

At least N/2 sites in each coordinate have factor one, so average(psi)
is at least 1/16. Thus average(b)=1, |b|<=16, and |Delta b|<=64a,
including a bond to its zero exterior. These bounds also hold for
N=1. For disjoint blocks, an edge sees at most two such zero-extended
bumps. Counting at most 2d N^d edges touching a block, d=4, gives

    ||sum_B b_B c_B||_0^2 <= B_0 sum_B |c_B|^2,
    ||D sum_B b_B c_B||^2 <= B_1 sum_B |c_B|^2,
    B_0=16^2,                    B_1=4d 64^2.        (2.1)

The factor two for two endpoints is included in B_1. On a periodic
block self-edge the same estimate follows by treating the two endpoint
values separately; no independence of their coefficients is required.

Given ANY exact extension E with ||Eu||_1<=C_E||u||_1,Omega, put

    E^0 u=Eu-sum_{B subset Y} b_B average_B(Eu).

Corrections are zero at every Omega site, each corrected mean is
exactly zero, and Cauchy--Schwarz gives sum|average_B(Eu)|^2<=||Eu||_0^2.
Consequently

    ||E^0 u||_1 <= (1+sqrt(B_0+B_1)) C_E ||u||_1,Omega. (2.2)

This is a parent-scale correction, with no L or depth factor. At scale
h the gradient constant in (2.1) is B_1/h^2; it is wrong to apply those
smaller bumps to an arbitrary order-one residual. Section 6 supplies
the compensating h^2 for the different problem of lifting prescribed
h-block means.

**discharged (input Poincare).** On a unit N^d-site block the variance
identity is

    sum_x |u(x)-ubar|^2=(2N^d)^(-1)sum_{x,z}|u(x)-u(z)|^2.

Join x to z by changing coordinates in order. Each path has at most
dN edges; any edge belongs to at most N^(d+1) ordered-pair paths.
Cauchy--Schwarz and multiplication by a^d therefore give
||u-ubar||_0^2<=d||Du||^2 (a deliberately loose bound). For zero parent
means, summing disjoint blocks yields

    ||u||_1,Omega^2 <= (1+d)||Du||_Omega^2.           (2.3)

Only internal edges enter. In particular (2.2) does not conceal a
boundary trace term. What remains to supply it is an exact extension E
for the brick patterns; a staircase extension alone does not cover
every such pattern.

## 3. A quantitative cover and the complete finite pattern list

**discharged (a smaller, verified radius).** Let b be brick side length
in parent units. BG's t_0 is in level-k cells, so b=t_0/L and b>=8.
The lower corners of the four-dimensional bricks are

    b(m_1+m_2/2+m_3/4+m_4/8,
      m_2+m_3/2+m_4/4, m_3+m_4/2, m_4),  m in Z^4. (3.1)

This follows by substituting the stated shift once at each recursive
layer. Projected walls perpendicular to coordinate i lie in
b 2^{-(4-i)} Z. Distinct possible wall positions in any coordinate
are therefore separated by at least b/8. A cube of maximum-norm
radius b/64 meets at most one wall position in each coordinate.

Recursively split such a cube at its highest-coordinate wall, if one
exists. Below that wall and above it, continue with the lower
coordinates. A coordinate cannot be used in both branches: at a split
in coordinate j the projected i-walls, i<j, in its two adjacent layers
have residues differing by b/2^(j-i) modulo b/2^(j-i-1). They are
distinct, and the projection separation just proved excludes both
from the cube. The same argument applies at every descendant split.
Thus the entire cube, not just the germ of its center, has a binary
decision tree with at most four internal nodes, each using a DIFFERENT
coordinate. Its leaves are the incident bricks, at most five.
Translations of the wall positions and the unused coordinates cause
no additional patterns.

**discharged (exhaustive finite list, without machine enumeration).**
Let o denote a leaf and (A,B) a split with lower child A and upper
child B. Every possible shape is in the following complete list.
The proof works for the full list whether or not every entry is
realized in a particular periodic tiling; some entries are equivalent
under reflections, which we need not identify:

| Internal nodes | Shapes |
|---|---|
| 0 | o |
| 1 | a=(o,o) |
| 2 | b=(a,o), c=(o,a) |
| 3 | d=(b,o), e=(c,o), f=(a,a), g=(o,b), h=(o,c) |
| 4 | (d,o), (e,o), (f,o), (g,o), (h,o), (b,a), (c,a), (a,b), (a,c), (o,d), (o,e), (o,f), (o,g), (o,h) |

Assign distinct coordinates from {1,2,3,4} to internal nodes, decreasing
along every root-to-leaf path. Assign each leaf independently to Omega
or Y: all 2^(m+1) assignments for a tree with m nodes. Empty and full
assignments have no interface. This is the requested complete list of
patterns including their labels; it is a finite parametrization, not
a claim to have run a finite test. Exhaustiveness follows because the
root's two subtree sizes sum to m-1. For m=4 their possibilities are
(3,0),(2,1),(1,2),(0,3), giving exactly the fourteen displayed entries.

Cover space by cubes of radius b/128 centered on the grid of spacing
b/128. Their enlarged cubes of radius b/64 have the property proved
above; at most 5^4 enlarged cubes contain a point. The same construction
in compatible local periodic lifts covers a brick torus. Thus a
verified fixed fraction of brick size replaces BG(b)'s unproved use
of t_0/8. No claim that a germ stays unchanged on the original ball
is needed.

For the consumer's enlarged patch of radius 10R in parent units,
10R<=b/128 suffices to place it inside an enlarged cover chart whose
core contains its center. In the t_0 convention above this is
t_0>=1280RL. This is the quantitative one-interface chart condition;
it does not settle clearance between distinct retained levels.

**discharged (why the staircase proof is not literally applicable).**
The balanced tree f=(a,a) in three active coordinates has leaves

    {z<0,x<0}, {z<0,x>0}, {z>0,y<0}, {z>0,y>0}.

Select the first and fourth. A displacement in z changes membership
in opposite directions for two choices of (x,y). No reversal of the
z coordinate makes this a product-order down-set. Its boundary has
open z=0 facets with both outward normals +e_z and -e_z. A graph
direction transverse to both would have to have positive scalar
product with both normals; a direction tangent to either facet
cannot give a Lipschitz graph either. Thus the single down-set
reflection in `staircase-by-hand.md:131-187` cannot
simply be applied to this pattern. The next construction handles it
and every pattern in the table, without composing facet reflections.

**discharged (a depth loss for the naive fan construction only).**
The branch-dependent fold sends (x,y,z) to (-|x|,y,z) for z<0 and
to (x,|y|,z) for z>0. It does not commute with interchanging the two
layers: at (r,-r,-1/2) in lattice units, folding and then reversing z
gives (-r,-r,1/2), whereas reversing z and then folding gives
(r,r,1/2). Neighboring sites across z=0 consequently acquire source
images at distance 4r+1, not a uniformly bounded lattice distance.

This is an actual energy failure, not just a large Lipschitz estimate.
Use the prescribed field omega=sin(2 pi(x+y)) on the two selected
bricks. It has zero mean on every unit parent and bounded input H1
norm independently of eta. In the three tangential intervals

    x in [1/32,3/32], y in [-3/32,-1/32],
    the fourth coordinate in [-1/32,1/32],

the two naive reflected values at z=-eta/2,+eta/2 differ by at least
1/2: their arguments are opposite and their positive sine is at least
sin(pi/8)>=1/4. For eta<=1/32 each interval contains at least
1/(32eta) sites, so those crossing edges alone have energy at least
1/(2^17 eta). Subsequent parent-bump corrections have mean coefficients
at most one and boundary values at most 64eta. For eta<=1/512 the
corrected jump remains at least 1/4, with energy at least
1/(2^19 eta). Thus this fold plus its parent corrections fails in
fine depth. Section 4 replaces the fold; (5.3) shows that the OPTIMAL
constant for the corrected extension does not suffer this loss.

## 4. An exact discrete reflection for every listed fan

**discharged (explicit flattening of the tree).** Translate each active
coordinate so its wall is zero. Write z_v for the coordinate at an
internal node v; lower means z_v<0. To a leaf assign scores recursively:
a leaf has score 0; at a node z, subtract z_+=max(z,0) from every score
of its lower subtree and subtract (-z)_+ from every score of its upper
subtree. The resulting leaf scores q_i have max_i q_i=0. Their largest
score is attained precisely in the leaf selected by the signs of z;
on walls, all leaves containing the point may tie.

Scores are considered modulo addition of a common constant. In the
coordinates q_i-q_last, call the map T. Its inverse is explicit:

    z_v = max_{i in upper subtree(v)} q_i
          - max_{i in lower subtree(v)} q_i.        (4.1)

To verify (4.1), the contributions from ancestors are equal on both
subtrees; each subtree's internally normalized maximum is zero; the
two shifts at v differ by z_v. Conversely the maxima and differences
recursively recover all normalized scores, proving bijectivity.
Each score is a sum of at most four signed positive parts. Hence in
maximum norms T has Lipschitz constant at most 8, and T^-1 at most 2.
Unused coordinates are carried along unchanged. This proves the
piecewise linear change of variables, rather than invoking the
combinatorics of a fan as a substitute for a map.

Let S be the nonempty proper set of Omega leaves and set

    F(q)=max_{i in S}q_i-max_{i not in S}q_i.

Omega is F>=0 in these coordinates. Adding t 1_S changes F by exactly
t. The map

    R_S(q)=q-2 F(q)1_S                               (4.2)

is an involution, reverses the sign of F, and fixes F=0. In quotient
coordinates it has Lipschitz constant at most 5: F is 2-Lipschitz and
the vector 1_S-1_{last in S}1 has maximum norm one. Therefore

    R=T^-1 R_S T,        Lip(R)<=K:=80,    R^2=Id.   (4.3)

Here is an explicit chart, including constants. Fix references a in S
and b outside S. Use the within-group differences xi_i=q_i-q_a in S
and xi_j=q_j-q_b outside S, omitting the reference components, and
t=F(q). This map on the score quotient is 2-Lipschitz. Its inverse
sets xi_a=xi_b=0 and

    q_i=xi_i-max_S xi+t  (i in S),
    q_j=xi_j-max_(S complement) xi  (j outside S),

then subtracts q_last. The inverse is at most 6-Lipschitz. Composing
with T and (4.1), and leaving inactive coordinates alone, gives a
chart of maximum-norm Lipschitz constants 16 and 12 taking Omega to
{t>=0}. At a boundary center, the image of a radius-r cube contains
the radius-r/12 cube about its image and is contained in the radius-16r
cube. This supplies quantitative chart domains as well as a finite
pattern description; the domain need not be an unchanged germ or
the image of the original ball. The extension below only needs the
directly verified involution (4.3).

**discharged (lattice values, not cell means of an interpolant).** Work
in lattice units. The walls are between sites: each active coordinate
z_v takes values m-c_v-1/2, m,c_v integers. Consequently each site
selects a unique leaf. For an exterior site x, take R(x), choose any
maximizing leaf in S, and round each coordinate to a nearest lattice
coordinate, taking the sign prescribed by that leaf if a coordinate
is exactly zero. For coordinates not constrained by that leaf either
nearest choice is allowed. The error is at most 1/2 per coordinate,
and the rounded site lies in the chosen leaf. Denote it by pi(x);
put pi(x)=x on Omega. Fix tie choices once, independently of u.
Then Eu(x)=u(pi(x)) reproduces every prescribed site exactly.

Rounding does not destroy the energy estimate. For two exterior
neighbors the images differ in maximum norm by at most K+1. For
an edge crossing the interface, its straight segment meets F=0 at
a point fixed by R; (4.3) bounds the two images by K+2. Thus all
neighboring images have l1 distance at most

    M=d(K+2)=328.                                   (4.4)

At most

    nu=1+(K+2)^d                                    (4.5)

sites have any particular image: besides the possible interior site,
all exterior preimages have R(x) within 1/2 of that image, so their
x's lie in a cube of radius K/2 by the inverse Lipschitz bound. An
interval of length K contains at most K+2 lattice sites.

**discharged (paths stay on the prescribed side).** Two sites p,q
in the same leaf can be joined in that leaf by a coordinate-monotone
path. For different leaves, let v be their first separating node.
Before crossing its wall, adjust the coordinates constrained only by
q's descendant path to their values at q; p's leaf does not constrain
those coordinates. Shared ancestor constraints remain satisfied.
Move the coordinate of v across its wall, and then adjust the
coordinates constrained only by p's path to their q values. Adjust
the remaining unconstrained and common-ancestor coordinates in either
stage. Every coordinate moves monotonically between its endpoint
values; all sites before the crossing lie in p's leaf, and all sites
after it in q's. The distinct-coordinate property of the tree is
essential here. The length is exactly |p-q|_1, at most M for images
of an edge. This proof covers the balanced, noncommuting example in
Section 3.

For a fixed source edge, a path using it starts within maximum-norm
distance M of that edge. There are at most (2M+1)^d possible starting
images, nu preimages of each, and d positive input edges per preimage.
Path Cauchy--Schwarz proves, with no search or enumeration,

    sum |Eu|^2 <= nu sum_Omega |u|^2,
    sum |Delta Eu|^2 <= C_R sum_internal |Delta u|^2,
    C_R=M nu d(2M+1)^d.                             (4.6)

All constants are explicit and absolute. This replaces the unavailable
commuting-facet reflection. It also avoids any claim that sampling or
averaging a continuum extension preserves prescribed lattice values.

## 5. Glue first, then restore the means

**discharged (bounded overlap and locality).** Set

    T_*=4K+8=328,   J=2T_*+2M+16=1328,
    rho=1/(64J),    B=(2T_*+3)^d,       d=4.

First suppose a<=rho. On the Cartesian grid of spacing rho put the
tensor tents theta_c(x)=product_j(1-|x_j-c_j|/rho)_+. On each grid
interval its two one-dimensional tents sum to one, so sum_c theta_c=1.
Their physical coordinate Lipschitz constants are at most 1/rho.
These tents are compatible with every integer parent-period torus,
since 1/rho is an integer. All computations use local periodic lifts.

Write r=rho/a>=1 in lattice units. The cube of radius Jr about c is
contained in a physical cube of radius 1/64<=b/64, so Section 3 supplies
one of the exact tree models D throughout it. If all sites within 2r
are prescribed, extend theta_c u by zero; if none are, use zero;
otherwise apply Section 4 to f_c=theta_c u on D, defined to be zero
away from its source support.

This asks for no unknown u values. Indeed a nonzero source p is within
r of c and there is an exterior site b' within 2r of c. The segment
pb' meets the model boundary at z, with |p-z|_inf<=3r. Since R(z)=z,

    |R(p)-p|_inf <= 3(K+1)r.

If an exterior output site x has pi(x)=p, then |R(x)-p|_inf<=1/2,
so |x-R(p)|_inf<=K/2. Therefore |x-c|_inf<=(3K+4)r+K/2<=T_*r.
An edge with a nonzero output endpoint has one source image in the
radius-r cube; its other image and their path are in the radius-(r+M)
cube, inside Jr. Hence every input edge used in (4.6) is an actual
internal Omega edge in the chart. The all-prescribed case is valid
because r+1<=2r. This verifies support before periodizing and adding
the outputs.

There are at most B output supports at a site or an edge: a contributing
center is within (T_*+1)rho of either fixed endpoint. For the sources,
the discrete product difference formula gives

    sum_c ||f_c||_0^2 <= ||u||_0,Omega^2,
    sum_c ||Df_c||^2 <= 2||Du||_Omega^2
                 +2^(d+2)d rho^(-2)||u||_0,Omega^2. (5.1)

For the second term at most 2^(d+1) tents touch either endpoint of an
edge, each difference is at most a/rho, and each site has d positive
edges. For the first term use sum_c theta_c(x)^2<=1. These counts also
cover sites on a tent boundary.

Adding the local extensions gives Eu=u on Omega and, by (4.6),

    ||Eu||_1^2 <= C_E^2||u||_1,Omega^2,
    C_E^2=max{1+2d rho^(-2),
      B[nu+2C_R+2^(d+2)d rho^(-2) C_R]}.             (5.2)

For a>rho use zero extension instead: its additional crossing-edge
energy is at most 2d a^(-2)||u||_0^2, covered by the first term in
(5.2). Thus every fine depth and every L are included.

**discharged (flat exact extension theorem).** Apply the correction
of Section 2 only after summing the partition. The resulting w=E^0u
satisfies exact site equality on Omega and zero unit-parent means on
Y, with

    ||w||_0^2+||Dw||^2 <= A_ext (||u||_0^2+||Du||^2)_Omega,
    A_ext=(1+sqrt(B_0+B_1))^2 C_E^2.                 (5.3)

If the prescribed parent means vanish, all parent means of w vanish.
A_ext depends only on dimension. It is independent of L, eta, number
of bricks, their chosen subset, and volume. The proof applies to every
listed local fan with a chart collar, and globally by the explicit
bounded-overlap construction. At an artificially truncated patch the
input must be supplied on the source collar just specified; no estimate
from an arbitrary cut-off interior without its collar is asserted.
For the mean correction the output patch must also include every
whole Y-parent block meeting the reflected support, at most one
additional parent length in maximum distance. The corrections read
no new Omega data. Their blocks are disjoint and their edge overlap
is two by (2.1), so this enlargement introduces no mesh or depth
factor. Gluing precedes correction so a later partition does not
spoil any restored mean.

**discharged (comparison with the staircase supplier).** Its integer
reflection and parent bumps have the right scale. Its down-set
hypothesis covers staircases, not all the present fans. Sections 3--5
replace that hypothesis and its reflection; the exact parent-mean
correction (2.1) is the flat form of its Section 5 correction. Thus
the mechanism applies after this enlargement of the geometric proof,
not by citing its staircase constant for an unlisted geometry.

## 6. A bounded fine lift with prescribed h-block averages

**discharged (a local competitor, all depths).** For coarse values v_z
on the h-grid, index each averaging block by its lowest fine site z
and attach its prescribed value v_z to that vertex for interpolation.
This is a relabeling of block-center values by one fixed translation;
their neighbor differences and density norm do not change. Interpolate
multilinearly on the cubes from z to z+(h,h,h,h), and evaluate at the
fine eta-sites. Call the result Iv. Since its tensor coefficients are
nonnegative and sum to one, and a vertex belongs to at most 2^d cubes,

    ||Iv||_0^2 <= N_0 ||v||_N^2,           N_0=2^d.

Its eta-difference in coordinate j is the convex combination of the
coarse j-differences divided by h. A coarse j-edge belongs to at most
2^(d-1) cubes. This holds also for the last eta-edge ending on the
next coarse face, since multilinear interpolation agrees there. Hence

    ||D_eta Iv||^2 <= N_1 ||D_h v||_N^2,   N_1=2^(d-1). (6.1)

Put e_z=v_z-average_{B_z}(Iv). Jensen followed by paths along the at
most d edges from z to each corner gives

    sum_z h^d|e_z|^2 <= E_1 h^2||D_h v||_N^2,
    E_1=d 2^(d-1).                                  (6.2)

To see the count, |v_z-v_{z+epsilon}|^2 is at most d times the sum
of its path's squared edge differences; averaging corner weights
assigns an edge weight at most one; each edge is in at most 2^(d-1)
cubes. Also, directly from Jensen and (6.1)'s mass bound,

    sum_z h^d|e_z|^2 <= 2(1+N_0)||v||_N^2.          (6.3)

Use the normalized bump from Section 2 in each h-block (N=h/eta),
and define Jv=Iv+sum_z b_{B_z} e_z. Then r^(k)Jv=v EXACTLY. Scaling
(2.1), and using (6.2) for derivatives and (6.3) for mass, gives

    ||Jv||_0^2 <= J_0^2||v||_N^2,
    ||D_eta Jv||^2 <= J_1^2||D_hv||_N^2,
    J_0^2=2N_0+4B_0(1+N_0),
    J_1^2=2N_1+2B_1 E_1.                            (6.4)

These constants are absolute, not iterated once per fine level. When
eta=h, the interpolation is the identity at sites and e_z=0.

**discharged (energy minimization survives).** On a finite torus the
affine space of prescribed block means is nonempty by J. The energy
quadratic is positive definite on its difference space: zero energy
means constant on the connected lattice, and zero block means kill
that constant. Completing the square therefore gives a unique energy
minimizer g. Its energy is at most that of Jv. The block variance
argument of Section 2, now at scale h, gives

    ||g||_0^2 <= ||v||_N^2+d h^2||D_eta g||^2
              <= (1+4d^2 J_1^2)||v||_N^2.          (6.5)

Here ||D_hv||_N^2<=4d h^(-2)||v||_N^2 follows by bounding each squared
difference by twice the two squared endpoint values. This proves both
norm bounds for the energy lift, rather than borrowing a mass estimate
as a derivative estimate. The simpler J suffices for D-coer.

**discharged (the exact compatibility needed in D-coer).** Set u=r^(k)
omega on Omega, form v=E^0u on the h-grid, and take w=Jv. Then
r^(k)(omega-w)=0 on Omega. Plain averages compose exactly on disjoint
blocks, so r^(n)w=0 on Y and r_N(omega-w)=0. Exact agreement of fine
omega on Omega is unnecessary here; preserving only these averages
is what permits the bound in terms of u rather than the much larger
fine energy of omega. Section 5 separately proves exact fine-site
extension if that stronger datum, with only parent means, is wanted.

## 7. Flat torus input and D-coer, with constants

**discharged (the flat operators being used).** D is the density-normalized
forward site difference; D*, d, and d* use its adjoint difference and
the corresponding exterior difference. A change of the source's sign
or bond-origin convention changes only unitary phases below. At U=1,
r is the plain parent average and Q_mu is the product box average with
one additional longitudinal box average. This is the box/triangle
operator of `block-poincare-energy-package.md:23-27`. Here is also its
direct algebra: one step averages paths in direction mu over all block
starts; removing the endpoint contour leaves the path average, hence
one extra box in that direction. Composing box averages concatenates
the disjoint digits of a site index, and composing longitudinal path
averages does the same for its path index. Thus the formula is valid
at arbitrary depth. Explicitly, for D_N(q)=sum_{j=0}^{N-1}exp(iqj),
D_L(q)D_M(Lq)=D_(LM)(q), since j+Ls runs exactly from 0 to LM-1.
On a pure gradient the endpoint contour telescopes, so subtracting
its correction from the center value gives the plain site average.
This verifies the r formula as well. In particular

    QD=D'r,  rr*=I,  ||QH||_N<=||H||_0.             (7.1)

The first identity telescopes each longitudinal path; the second is
averaging a blockwise constant field; the last is Jensen, since row
weights sum to one and their density-weighted column sums are one.
These facts also hold with parent length h and its density h^d.

**discharged (a complete flat torus estimate).** The following finite
Fourier argument supplies the torus input, so it is not an additional
extension premise. Fourier orthogonality follows from the geometric
sum of roots of unity, and summing its squared coefficients is Parseval.
Group fine frequencies into aliases q=p+2 pi ell of a parent frequency
p in [-pi,pi]^d, retaining only q in the fine frequency zone. Put

    delta_mu(q)=(exp(i eta q_mu)-1)/eta,
    delta'_mu(p)=exp(i p_mu)-1,
    b_mu(q)=eta sum_{j=0}^{eta^-1-1} exp(i eta q_mu j),
    rhat(q)=product_mu b_mu(q),  rhohat_mu(q)=rhat(q)b_mu(q).

The formulas just proved give these symbols, up to immaterial phases
that are kept consistently in QD=D'r. The sine formula for the finite
geometric sum gives |b_mu|<=1; at q=p, |b_mu(p)|>=2/pi. The elementary
concavity bound sin t>=2t/pi on [0,pi/2] gives

    |delta(q)|>=(2/pi)|q|,   |delta(p)|<=|p|,
    |delta'(p)|>=(2/pi)|p|.

Every retained alias has |q|>=|p|. Also sum_alias |rhat(q)|^2=1 by
rr*=I. These observations avoid any infinite alias-series estimate.
For p!=0 set

    B(p)=sum_alias |rhat(q)|^2/|delta(q)|^2, S(p)=1/B(p),
    c_1=(2/pi)^(2d+2), c_2=(pi/2)^2.

Keeping the q=p term proves B(p)|delta'(p)|^2>=c_1. Conversely,

    G_mu(p):=sum_alias |rhohat_mu(q)|^2/|delta(q)|^2
            <= c_2/|p|^2,
    |delta'(p)|^2 G_mu(p)<=c_2.                     (7.2)

The last step uses |delta'(p)|<=|p|. Now take QH=0, phi=D*H,
c=r phi, and P=I-r*r. The global mean of c vanishes because the sum
of a periodic divergence vanishes. Set all constructions below to
zero at p=0 and define

    g=(-Delta)^(-1)r*Sc,
    beta_mu=delta'_mu Sc/|delta'|^2.

The adjoint phase in D'^* is understood, so D'^*beta=Sc. We have rg=c
and, using sum|rhat|^2=1 and the lower bound for |delta(q)|,

    ||g||<=g_0||c||,       g_0=(pi/2)^2/c_1.

Indeed S<=c_1^-1|p|^2, so each frequency's squared bound is at most
c_1^-2|p|^4 sum|rhat|^2/|delta|^4<=g_0^2. Put E=Dg-Q*beta.
Then D*E=0 by (7.1), and E has zero mean. For each nonzero frequency,
the algebra of wedge multiplication by delta and its adjoint gives

    |delta|^2 I = delta delta* + (delta wedge)^*(delta wedge).

Expanding the two sides component by component verifies this identity:
the off-diagonal products cancel and the diagonal is sum|delta_mu|^2.
It proves E=d*(-Delta)^(-1)dE and dE=-dQ*beta. By (7.2),

    ||(-Delta)^(-1)dQ*beta||<=b_0||c||,
    b_0=sqrt(c_2)/c_1.                              (7.3)

To check (7.3), the squared alias sum is at most
sum_mu G_mu|beta_mu|^2<=c_2 S^2|c|^2/|delta'|^4.
Finally,

    ||c||^2=<g,phi>-<Pg,Pphi>
            =<E,H>-<Pg,Pphi>,
    ||c||<=b_0||dH||+g_0||Pphi||.                  (7.4)

The term <Q*beta,H> is zero. The same wedge identity gives
||grad H||^2=||dH||^2+||phi||^2, and phi=Pphi+r*c is an orthogonal
sum. Therefore, with C_div=1+2 max(b_0^2,g_0^2),

    ||grad H||^2<=C_div (||dH||^2+||Pphi||^2).       (7.5)

For completeness, the remaining mass Poincare estimate is also a
finite path estimate. Enclose each Q-row support in a cube of side
at most 3. Its nonnegative density rho has integral one and sup rho<=1.
The variance argument of Section 2 on that cube gives
||f-fbar||^2<=9d||grad f||^2. If <rho,f>=0 then
|fbar|^2=|<rho,f-fbar>|^2<=||f-fbar||^2. Since the cube volume is at
most 3^d,

    ||f||^2<=(1+3^d)9d||grad f||^2.

For each bond component these cubes cover the lattice and have overlap
at most 4^d. On a small torus use the lifted cubes, counting their
periodic copies; the same bound holds. Put

    C_P=4^d(1+3^d)9d,
    C_T=(1+C_P)C_div.

Then

    ||H||_0^2+||grad H||^2
       <= C_T (||dH||^2+||P D*H||^2),  QH=0.       (7.6)

All Fourier sums here are symbolic finite identities, not performed
computations. Their bounds hold for every spacing, depth, and torus.

**discharged (the transverse decomposition).** For H in ker bC, the
finer retained constraints imply the parent constraint QH=0: compose
the one-level maps on frozen parent rows, and use the explicitly
retained parent rows elsewhere. Minimize ||H-Domega||^2 over r omega=0.
The unit-parent Poincare inequality makes the quadratic positive
definite on that subspace, so completing the square gives a unique
omega. With H_s=H-Domega,

    P D*H_s=0,    QH_s=0,    dH_s=dH,
    ||H_s||_0^2<=C_T||dH||^2,
    ||omega||_0<=sqrt(d)||Domega||.                 (7.7)

This verifies all uses of the torus result in the flat reduction.
At U=1 the form bH is exactly ||dH||^2; its stationary multiplier is
zero and no curvature or class-minimum premise enters this equality.

**discharged (D-coer).** Write y=||H_s||, x=||Domega||,
p=||P_N D*H||. On internal level-k bonds in Omega,

    D_h(r^(k)omega)=-Q^(o,k)H_s.

By (7.1), its density norm is at most y. Its parent means vanish.
Sections 2, 5, and 6 give a fine w with r_N(omega-w)=0 and

    ||w||<=a_0 y,       ||Dw||<=a_1 y,
    a_0=J_0 sqrt((1+d)A_ext),
    a_1=J_1 sqrt((1+d)A_ext).                        (7.8)

Since <Domega,H_s>=0 and phi=D*H, summation by parts gives

    x^2=<omega-w,P_N phi>+<Dw,H>
        <=sqrt(d)xp+a_0 yp+a_1 y^2+a_1 xy.

Use sqrt(d)xp<=x^2/4+dp^2,
a_1xy<=x^2/4+a_1^2y^2, and
a_0yp<=p^2/2+a_0^2y^2/2. Thus

    x^2<=(2d+1)p^2+(2a_1+2a_1^2+a_0^2)y^2,
    ||H||^2 <= C_0 (||dH||^2+||P_N D*H||^2),
    C_0=max{4d+2, (2+4a_1+4a_1^2+2a_0^2) C_T}.     (7.9)

This is the flat D-coer on every admissible one-jump union of the
specified bricks. Every constant in the extension and reduction is
given above. It is independent of L, fine depth and volume. No small
curvature parameter is used to hide a flat L loss.

## 8. The flat one-jump F-D and its absolute rate

**discharged (row lift, including its cross-scale term).** Here take
L>=4K_b, K_b=2^120; a lower cutoff on L is permitted by the supplier's
order of constants. The preceding extension and D-coer require no
such large cutoff. In the row norm use weight sigma^(-2) times the
site density sigma^d, with sigma=h or 1.

For clarity, rebuild the finite moment test used in `fd-local.md:103-135`.
On the actual lattice in [0,1) put b(t)=(1-4|t-1/2|)_+,
p=b/avg(b), a=avg(tp), and v=avg((t-a)^2p). There are at least 32
sites whenever the averaging scale is not the original fine scale.
Counting sites in [5/16,3/8] and [5/8,11/16] gives p-mass at least
1/128 in each interval and avg(b)>=1/16. The variance identity
v=(1/2)avg_{t,s} p(t)p(s)(t-s)^2 gives v>=2^-18. Consequently

    psi_-=p[1-a(t-a)/v],
    psi_+=p[1+(1-a)(t-a)/v]

have respective moments (1,0),(0,1) against (1-t,t). Expansion using
avg p=1, avg p(t-a)=0, avg pt(t-a)=v proves these equalities exactly.
The functions and their slopes are bounded by 2^22 and 2^25; tensoring
with p in the other three directions bounds the bond bump by 2^34
and each slope by 2^37. Longitudinal bond midpoints, if used in the
triangle convention, merely shift the actual sample values t; the
same interval count and moment identities hold. Finite differences
obey the same slope bound, including the zero exterior of the support.

Assign each row to one of its leaf endpoints, at most eight rows per
leaf. Put its component bump inside that leaf. The two longitudinal
moments separate its two incident rows; transverse tile means separate
the other rows. Distinct leaf interiors are disjoint. Cauchy--Schwarz
over four derivative directions, eight rows and eight touching supports
costs less than 2^10 in norm. Thus K_b bounds both the mass lifting
constant and sigma times its gradient lifting constant. At the original
fine scale the retained identity rows use their bond indicators, whose
mass and gradient bounds obey these same constants.

Lift fine rows first, B_f=R_h y_f. Then set

    B_c=R_1(y_c-C_c B_f),        R y=B_f+B_c.        (8.1)

The coarse bumps lie inside free parent leaves, so no retained finer
row reads them. Fine bumps may feed coarse rows, and (8.1) subtracts
ALL those moments. The coarse moment norm of B_f is at most sqrt(2)
times its mass by Jensen. Since ||y_f||_N<=h||y||_Lam, this term is
at most sqrt(2)K_b/L in weighted norm. Counting the supports as above
gives the deliberately loose bound

    ||Ry||_0^2+||grad Ry||^2<=K_*^2||y||_Lam^2,
    K_*=16K_b^2.

The product formulas for curl and divergence give
||dB||<=sqrt(6)||grad B||, ||D*B||<=2||grad B|| in d=4. Thus
||R||_{Lam to G}<=R_*=4K_*. This accounts explicitly for the
cross-scale feedthrough; same-scale biorthogonality alone would not.

**discharged (saddle inversion).** Write

    K_N[H,V]=<dH,dV>+<P_N D*H,P_N D*V>,
    S_N=[[K_N,bC*],[bC,0]].

Its form norm on G is at most one, and (7.9) gives coercivity
alpha=(1+C_0)^(-1) on ker bC. For data (f,y), write H=Ry+z with
z in ker bC. The restricted positive quadratic equation has the
unique solution with

    ||z||_G<=alpha^-1(||f||_{G*}+R_*||y||_Lam).

The residual f-K_NH annihilates ker bC. Define its multiplier by
lambda(q)=(f-K_NH)(Rq); then ||lambda||<=R_*(||f||+||H||).
This proves existence, uniqueness and, in the product Hilbert norms,

    ||S_N^-1||<=M_0,
    M_0=4(1+R_*)^2(1+alpha^-1).                    (8.2)

No upper bound for ||bC|| enters (8.2).

**discharged (the means in the graph commutator).** On a leaf B of
side sigma let c_B=average_B(D*H), phi=D*H, p=P_N phi. Apply the
scaled bump of Section 2 with mean sigma^2 c_B and zero exterior,
calling it g_B. Orthogonal projection and summation by parts give

    sigma^2|B||c_B|^2=<Dg_B,H>-<P_Ng_B,p>.

The single-block versions of (2.1) bound its mass by
sqrt(B_0)sigma^2|B|^(1/2)|c_B| and gradient by
sqrt(B_1)sigma|B|^(1/2)|c_B|. Dividing and summing, an edge belongs
to at most two enlarged leaves. With K_m=4sqrt(B_0+B_1)+1 this yields

    (sum_B sigma^2|B||c_B|^2)^(1/2)
       <=K_m(||H||+||p||).                         (8.3)

For a multiplier chi, expansion of [P_N,chi]phi on a leaf gives both
(chi-average chi)c_B and the constant -average((chi-average chi)p).
Their norms are at most osc_B(chi)(|B|^(1/2)|c_B|+||p||_B).
Thus the oscillation sigma Lip(chi) cancels the inverse sigma in (8.3).
This is why the graph norm, not the full divergence norm, suffices.

**discharged (quantitative conjugation).** Let f be delta-Lipschitz,
delta<=1/16, in parent units. Give row variables the value f at their
row root. The following constants bound the differences after
conjugating by exp(f):

| Term | Bound in its indicated density norms |
|---|---|
| Constraint and its adjoint | 64 delta times the L2 norm of H; row diameter <=8sigma, weight sigma^-1, at most two scales and bounded tile overlap |
| Curl, after removing exp(f) | 16 delta times the L2 norm of H |
| P_N D*, after removing exp(f) | 64(1+K_m) delta times the G norm of H |

Here |exp(t)-1|<=2|t| for |t|<=1 follows by its convergent power
series. On an edge |t|<=delta eta; on a row |t|<=8delta sigma.
The curl bound is the product difference formula with at most four
legs per plaquette. For the last bound, apply the same formula to
the divergence and apply (8.3) to the two parts of the projector
commutator just displayed; the normalized exponent oscillation on
a leaf is at most 8delta sigma. No bound for phi without projection
was inserted. These estimates hold with f replaced by -f.

The conjugated quadratic forms pair the plus and minus differential
expressions. If each differs from its unconjugated expression by
c delta, their product error is at most (2c+c^2)delta for delta<=1.
The row terms are linear. Thus a common deliberately loose bound is

    ||exp(f)S_N exp(-f)-S_N||<=C_com delta,
    C_com=2^20(1+K_m)^2.                            (8.4)

These are estimates on G x Lam* into its dual; the exponential
factors are canceled before estimating, so max f does not enter.

Choose

    delta_flat=min{1/16, (2M_0 C_com)^(-1)}.         (8.5)

The geometric inverse series has ratio at most 1/2, proving a
conjugated inverse norm at most 2M_0. Taking
f(x)=delta_flat min(dist(x,X'),dist(X,X')) and using its constant
values on X and X' proves the off-diagonal bound with rate
delta_flat, independent of L, depth, geometry subset and volume.

**discharged (flat class solution and its Schur form).** For J that
annihilates D(ker r_N), test the saddle equation with Dv, v in
ker r_N. The curl term vanishes and bC Dv=0, giving
<P_ND*H,P_N(-Delta)v>=0. The unit-block Poincare argument makes
P_N(-Delta)P_N invertible on ker r_N; on h-leaves its gap is larger.
Testing with its inverse applied to P_ND*H proves P_ND*H=0.
Thus H is the minimizing class representative for the flat quadratic
form. Minimizing that finite positive quadratic form over its inner
variables gives its Schur quadratic form M_Y; solving with a functional
of the remaining coordinates gives M_Y^-1 by the same completion of
the square. This proves the linear class/Schur assertion.

A level-k tree coordinate is a finite combination of Q^(o,k)H values
and paths on at most neighboring parent boxes. (7.1) bounds the first
map; the remaining matrix has finitely many entries depending on L,
not eta. Therefore a coordinate functional J_i has a local G* norm
at most C_chart(L). Applying (8.5) to J_i,J_j yields

    |M_Y^-1(i,j)|<=2M_0 C_chart(L)^2
                    exp(-delta_flat d(i,j)),        (8.6)

with the fixed support enlargement absorbed into the prefactor.
The nonlinear identification of this quadratic form with an actual
background class fill is a different assertion, addressed next.

## 9. Backgrounds: the supplier, exact conditional estimates, and limits

**discharged (what the supplier actually asserts); unchecked (its proofs
as a package).** The hypotheses must be read on the same stationary
class branch, with the source's actual short contours and all the read
enlargements. Mapped Text 5.3, lines 734--750, has the following content.

| Supplier | Actual input/output and scope |
|---|---|
| (R1) | From small coarse flux a, construct one smooth trial U^tr, once over the cell complex. Its fine plaquette bound is R(Ca); with the smoothing used in (R3), its box-scale derivative of curvature is O(a). Its blocking residual is O(a); it need not already have the prescribed blocked field. |
| (R2) | Conditional on the inverse at the trial, solve the nonlinear multiplier equations near U^tr in local Eps norms. The relative field has norm O(a), the multiplier is bounded, and the constructed stationary branch is unique in that ball. The extra gauge equation is subsequently killed. This is an existence/branch assertion, not a statement about all fields in the ball. |
| (R3) | For that stationary lift, with the smooth trial and (R2), the proposed local Landau argument gives an H2 bound for the relative field and an L4 curvature bound C_R3 a, uniformly in depth and L, on every specified box with its enlargement. It gives no pointwise bound on the actual fine curvature. |

No proof of existence of those backgrounds is supplied by this note.
In particular the use of the response in (R2)/(R3) must not be turned
into a circular proof of the inverse at that response. One may first
assume an admitted stationary background with these bounds and prove
an implication there; construction and bootstrap closure remain
separate obligations.

**implication (the coarse covariant extension is available).** Suppose
the level-k plaquette transports satisfy

    ||Ad hol(p)-I|| <= epsilon_0 h^2,
    epsilon_0=1/(4d^2),                    d=4.      (9.1)

This is a condition on the BLOCKED connection, not a pointwise bound
on the fine U. In a rectangle of side at most one, an ordered-path
gauge changes a link into a product of at most d/h plaquettes. The
telescoping product identity for orthogonal matrices bounds its
deviation from I by kappa h, kappa=d epsilon_0=1/(4d). Hence ordinary
and covariant derivatives in that frame differ by at most
sqrt(d)kappa times the site mass norm. Apply that comparison to the
input and output of each reflection in Sections 4--5. The three-term
product bound in place of the two-term bound in (5.1), followed by
the reverse comparison on the output, is bounded by 4C_E in H1 norm.
All rectangles in that construction have side less than one.

For each unit parent use its own ordered-path frame G_B. Every
one-level prescribed contour has at most d/h edges; in this frame
its transport differs from the root rotation by at most d kappa=1/4.
If r_B is the actual one-level mean, its moment on b_BG_B^{-1}c is a
matrix M_B within 1/4 of that rotation. The geometric inverse series
therefore gives ||M_B^-1||<=2. The corrected bump

    Q_Bc=b_BG_B^{-1}M_B^-1 c

has r_BQ_Bc=c exactly. Its mass is at most 32|c| and its covariant
gradient at most 2(64+16kappa)|c| per unit volume; the boundary value
estimate is no larger than 256|c|, allowing periodic endpoints. Thus

    ||sum_B Q_B c_B||_{1,U}^2
      <= C_bU^2 sum_B|c_B|^2,
    C_bU^2=32^2+4d 256^2.                           (9.2)

The source mean is an average of orthogonal maps and so is contractive.
Subtract these moments on Y as in Section 2. This gives the exact
coarse covariant extension with constant

    C_ext,U=4(1+C_bU)C_E.                           (9.3)

For zero covariant parent means, in the same gauge
|average(G_Bu)|<=d kappa||u||. Apply the variance estimate and
||d(G_Bu)||<=||D_Uu||+sqrt(d)kappa||u||. It yields

    ||u||^2<=2d||D_Uu||^2+3d^2kappa^2||u||^2
             <=4d||D_Uu||^2,                      (9.4)

because 3d^2kappa^2=3/16<1/2. Thus the input mass again costs no L.
These are proved implications from (9.1), for ALL the fan patterns,
not just for staircases.

**unchecked (the proposed supply of (9.1)).** `lc-u.md` Section 5,
especially (5.4)--(5.5), proposes the blocked-angle estimate
E_j<=2s_j a_R on a full read enlargement, where
E_j=(sum_p|theta_p^(j)|^4)^(1/4), a_R=C_R3 a.
At j=k it gives max|theta_p^(k)|<=2h a_R.
The elementary adjoint bound ||Ad exp(X)-I||<=2|X| follows by
integrating exp(tX)[X, .]exp(-tX). Hence (9.1) follows if

    a_R<=epsilon_0 h/4,                             (9.5)

as well as lc-u's threshold for its recursion. This sacrifices an
L-dependent background threshold, not the flat extension constant.
I have read that candidate proof but have not independently discharged
its endpoint/coarsening identities for the actual nonlinear block map.
It is explicitly an unchecked supplier here. The stronger class-
reference input in `staircase-by-hand.md:451-470` is another sufficient
supply of (9.1), conditional on that particular reference assertion.
Neither route is a fine pointwise curvature assertion.

**implication (exact fine covariant means, with the Gram matrix).**
The useful inputs of `lc-u.md` Sections 3 and 5 can be separated.
On a leaf B of side sigma suppose an orthogonal frame J_B obeys

    ||D_UJ_B||_{2,B}<=2^5 sigma||F_U||_{2,B},
    sup_x ||A_B(x)J_B(x)-O_B||<=epsilon<=1/4,         (9.6)

where r_Bv=average_x A_B(x)v(x) is the ACTUAL hierarchical mean,
and O_B is a fixed rotation. The first is the candidate averaged
ordered-path energy estimate; the second is its proposed transport
comparison, not a consequence of the first. If those two inputs hold,

    9I/16 <= G_B:=r_Br_B*<=I

in row density |B|. This follows from the singular-value lower bound
1-epsilon for A_BJ_B and its contraction upper bound. With the
nonnegative bump b_B of Section 2 define

    M_B=average b_B A_BJ_B,
    q_B(c)=b_BJ_BM_B^-1 c.

Then ||M_B^-1||<=4/3 and r_Bq_B(c)=c exactly. Scaling (2.1),
using Holder ||F||_2<=sigma||F||_4, and differentiating the product,
gives, for sigma||F||_4<=1,

    ||q_B(c)||<=2^6 |B|^(1/2)|c|,
    ||D_Uq_B(c)||<=2^16 sigma^-1 |B|^(1/2)|c|.       (9.7)

For example the interior product term is bounded by
(4/3)16*2^5 sigma||F||_2 |c|
<=2^10 sigma^2||F||_4 |c|<=2^10 sigma |c|,
and the differentiated scalar bump is at most a fixed multiple of
64 sigma |c|. These terms fit below 2^16; boundary edges differentiate
only the bump. No derivative of the prescribed hierarchical kernel
A_B is being claimed.

For c_B=G_B^-1 r_B phi and g_B=sigma^2q_B(c_B), the exact identity is

    sigma^2|B||c_B|^2=<D_Ug_B,H>-<P_Ng_B,P_Nphi>,
    P_N=I-r_N*(r_Nr_N*)^-1r_N.                      (9.8)

The equality uses <g_B,r_B*c_B>=|B|<r_Bg_B,c_B>, so it does not
replace the Gram matrix by I. It gives the covariant version of
(8.3), with an absolute mean-test constant. Subtracting a scalar
constant on each leaf gives both parts of [P_N,chi]phi exactly as
in Section 8. Equations (9.7)--(9.8) therefore discharge the mean
and projector algebra CONDITIONAL ON (9.6).

**unchecked (what is still needed for the fine background lift).**
The single-block right inverse (9.7) alone is not an energy lift of
arbitrary neighboring means: using it separately costs h^-2||v||^2.
One sufficient, more local comparison is the following. On a bounded
parent-sized cube C, require a fine orthogonal frame J_C and coarse
rotations O_z on its h-blocks such that, in density norms,

    ||D_UJ_C||_{2,C}<=C_f a_R,
    ||r^(k)(J_C f)-O average_h(f)||_N<=epsilon||f||_0,
    ||O_z^-1 Ad(V_k(zz')) O_z'-I||<=epsilon,
    epsilon<=C_tr(L)a_R.                            (9.9)

The comparison must hold on each entire interpolation support and
its one-edge margin, with bounded overlap. The intended sources are
the frame estimate of lc-u Section 3, its coarsening comparison in
Section 5, and the blocked plaquette bound. A version with a common
parent-sized frame in precisely (9.9)'s domains has NOT been verified
here. It is narrower than an extension theorem: it concerns the
transport/mean kernels and one frame on a full cube, with no interface,
no prescribed u, no mean corrections, and no saddle operator.

**implication (why (9.9) suffices, rather than hiding another lift).**
Use scalar tensor tents on the parent grid, supported in parent-sized
cubes, summing to one on coarse sites. In each chart apply the scalar
J of Section 6 to theta_c O_c^-1 v and transform the result by J_C.
Let P_0v be the sum. At epsilon=0, its r^(k) means sum to v exactly.
For nonzero epsilon the middle line of (9.9), (6.4), and bounded
overlap give

    r^(k)P_0=I+E,    ||E||_{N to N}<=C_a epsilon,
    ||P_0v||<=C_a||v||,
    ||D_UP_0v||<=C_a(||D_kv||+||v||)
                   +C_b(h^-1 epsilon+h^-2 a_R)||v||. (9.10)

One explicit overestimate is

    C_a=2^30(1+J_0+J_1), C_b=(1+C_f)C_a.

Use cubes of radius four for the frames: the parent tents have radius
one, the scalar lift enlarges support by at most h, and the one-edge
margin is at most h. At most 9^4 such cubes meet a point; the scalar
lift has supremum at most 33 times the largest neighboring coarse
value (interpolation costs one, and its mean correction at most
16*2). Together with the four coordinate products these counts are
smaller than the factor 2^30 above. To check the last two terms:
comparing a coarse edge in the O frame costs epsilon/h times its
endpoint value. The product
with D_UJ_C costs ||D_UJ_C||_2 times the supremum of the scalar
interpolant/lift. Each such lift is a bounded combination of coarse
values, so its supremum is at most a fixed constant times
h^-2||v||_{N,C+}; this is simply the largest summand bound in the
four-dimensional density norm. Summing the charts costs a fixed
overlap. These facts prove (9.10) directly, without a fine connection
supremum bound.

Choose a_R after L so that
C_a epsilon<=1/2 and C_b(h^-1epsilon+h^-2a_R)<=1.
Then v'=(I+E)^-1v exists, ||v'||<=2||v||, and

    ||D_k(v'-v)||<=2sqrt(d)h^-1||v'-v||
                  <=4sqrt(d)C_a h^-1epsilon||v||.

The first inequality is valid for unitary covariant edge differences
by the endpoint square bound. Thus J_Uv=P_0v' has EXACT r^(k) mean v
and satisfies

    ||J_Uv||+||D_UJ_Uv||<=C_JU(||v||+||D_kv||).      (9.11)

One may take C_JU=16(C_a+1): C_b>=C_a makes the displayed bound on
D_k(v'-v) at most 8||v||, and substitution in (9.10) bounds the mass
plus gradient by (12C_a+2)||v||+C_a||D_kv||. Composing (9.11) with
(9.3)--(9.4) supplies the needed background lift. This implication is
proved; the precise transport supply (9.9) is unchecked. In particular
this note does not promote the background extension to an unconditional
consequence of the phrase "local L4 curvature".

## 10. Background D-coer and F-D: the precise implications

**implication (coercivity, with its additional inputs visible).** In
addition to (9.1), (9.9), and their smallness thresholds, suppose the
background torus input supplies

    H=H_s+D_Uomega,  r^(n)omega=0,  P_rD_U*H_s=0,
    ||H_s||^2<=C_TU bH[H,H],
    ||omega||<=C_omega||D_Uomega||,                 (10.1)

with absolute C_TU,C_omega, the exact covariance identity, and
||Q^(o,k)||<=2 in density norm. The torus background comparison and
its fine covariant Poincare estimate in (10.1) are separate inputs;
they are not inferred here from (R3) alone. The proposed row bound
is in lc-u (5.9)--(5.10), read here as unchecked.

By (9.3)--(9.4), (9.11), and the internal-gradient identity used in
Section 7, the fine lift has both norms at most A_U||H_s||, where

    A_U=2sqrt(2) C_JU sqrt(1+4d) C_ext,U.

Repeating the three displayed Young inequalities of Section 7, with
C_omega in place of sqrt(d), proves

    ||H||^2<=C_0U(bH[H,H]+||P_ND_U*H||^2),
    C_0U=max{4C_omega^2+2,
             (2+4A_U+6A_U^2)C_TU}.                (10.2)

Thus the reduction introduces no L or depth loss at a background
once its specified inputs have absolute constants. This is a proved
implication; (10.1) and the indicated suppliers are not newly proved
background theorems in this note.

**implication (stationarity is a different hypothesis).** To make bH
the constrained Hessian, assume the actual stationary equation
DA(U)=DN(U)*lambda, a smooth contour-free chain N at that point, and
the Ward identity D'_V*lambda=0. Then

    bH=D^2A(U)-<lambda,D^2N(U)>.

For a fine gauge direction W_omega at nearby U', covariance has the
exact form DN(U')W_omega(U')=D'_{N(U')}varpi_omega(U'), with
varpi_omega(U)=r omega. Differentiate
D(A-<lambda,N>)(U')W_omega(U')
=-<lambda,D'_{N(U')}varpi_omega(U')> at U. Its left side is
bH[H',D_Uomega], because the stationary first derivative is zero.
The right side is the sum of

    -<D'_V*lambda, d_{H'}varpi_omega>
    -<lambda,(d_{H'}D'_N)(r omega)>.

Both terms vanish when r omega=0. Also ker r_N is contained in
ker r^(n), because the fine retained means compose to the parent
mean on Omega and the parent mean itself is retained on Y.
This proves the needed null-direction
identity under stationarity, without any claim that small curvature
implies stationarity or that the coarse stabilizer is trivial.

**implication (curvature and multiplier errors, term by term).** Given
a uniform local discrete Sobolev constant C_S, the Wilson curvature
bilinear term obeys

    sum |F||H||V|
       <=||F||_4||H||_(8/3)||V||_(8/3)
       <=C_S^2 a_R ||H||_Eps||V||_Eps.             (10.3)

The first inequality is Holder with exponents 4,8/3,8/3; the second
uses the stated Sobolev input and interpolation between L2 and L4.
It is not a pointwise estimate. The multiplier term separately
requires an absolute-kernel local bound for D^2N, of size
C_jet(L)||lambda||; its first exponential commutator must satisfy
the corresponding local bound as well. Neither follows from (10.3).

Assume those bounds, the covariant mean test (9.8), and absorption of
the Weitzenbock error. They give the graph comparison
||H||_Eps<=C_g L||H||_G (the leaf mean part costs at most h^-1=L).
Thus (10.3) costs C_S^2 C_g^2 L^2 a_R in graph norm, and the multiplier
term costs C_jet(L) C_g^2 L^2 ||lambda||. Choose a_R and ||lambda||
after L so that their sum and the other local comparison errors are
at most 1/2. In particular the needed signed AND absolute local
bilinear estimate is

    |bH[H,V]-<d_UH,d_UV>|<=epsilon_form||H||_G||V||_G,
    epsilon_form<=1/2,                             (10.4)

with the same local absolute-kernel control for conjugation. These
are named background requirements; an unweighted signed quadratic
bound is insufficient for the commutator.

**implication (one-jump background F-D with an absolute rate).** Given
(10.2)--(10.4), an absolute graph-norm row right inverse R_U, and the
covariant versions of the three rows of the commutator table in
Section 8 with absolute common constant C_com,U, the saddle is
coercive on its kernel with

    alpha_U=1/[2(1+C_0U)].

Indeed G^2<=C_0U K_N[H,H]+K_N[H,H]+epsilon_form G^2.
The form norm is at most two. The lifting-and-kernel solution of
Section 8, with this form bound, gives for example

    M_U=8(1+R_U)^2(1+2/alpha_U),
    delta_U=min{1/16, (2M_U C_com,U)^(-1)},
    ||exp(f)S_U^-1 exp(-f)||<=2M_U
                  when Lip(f)<=delta_U.            (10.5)

Every constant in (10.5) is absolute once the comparison errors are
absorbed; the allowed a_#(L) is not required to be absolute. The row
and mean candidates in lc-u Sections 3 and 5 may supply parts of
this hypothesis, but are used here only as the explicitly unchecked
comparisons specified above. Their labels in that file are not
independent verification.

Given the null-direction identity and positivity of
P_N D_U*D_U P_N on ker r_N, the same test as Section 8 removes the
gauge term for gauge-invariant J. Separately assume that the actual
compatible class minimum exists in this branch and that its local
coordinate Hessian is the Schur form of this stationary problem.
Only under that identification does (10.5) give

    |M_Y^-1(i,j)|<=C(L) exp(-delta_U d(i,j)).         (10.6)

Curvature, stationarity, and identification are three distinct inputs.
For an arbitrary field with small L4 curvature, (10.6) is not claimed.
For all backgrounds asserted by (R1)--(R3), this note likewise makes
no unconditional claim until the listed comparison and bootstrap
obligations are independently discharged.

## 11. Decision, source boundary, and recovery checkpoint

**discharged (decision for the corrected item).** The literal extra
finer-mean condition on Y has an optimal-constant counterexample in
Section 1. For the actual D-coer condition (1.1), the flat exact
extension and flat D-coer are proved in Sections 2--7. All brick fans
and their quantitative local cover are included. Section 8 proves
the resulting flat one-jump saddle estimate and absolute rate for
the stated large-L range. The staircase result has the correct
mean-correction scale; its geometric domain required the explicit
tree replacement above. No failure of the optimal corrected flat
extension constant remains from the attempted attacks.

**implication (precise background result).** Under the explicit blocked
connection hypothesis (9.1), the coarse covariant fan extension is
proved. Exact covariant mean tests and the fine lift are proved as
implications from (9.6) and (9.9), respectively. Background D-coer
and F-D are the implications (10.2), (10.5), and (10.6), with their
extra hypotheses intact. This is the limit of the background result,
not an assertion of a pointwise estimate or a construction of a
stationary class fill.

**gap (next mathematical checks, not the flat extension).** The most
specific unresolved background comparison is (9.9)'s middle
inequality on a common parent-sized fine frame. It is a statement
about a mean kernel on a full cube and contains neither a boundary
extension nor a saddle problem; (9.10)--(9.11) show exactly how it
would be consumed. I expect it to hold on the supplier's admitted
short-contour class branch because coarsening produces the summable
s_j^(1/4) transport error proposed in lc-u (5.6)--(5.8); this is an
expectation, not a proof. The background torus comparison, local
absolute multiplier estimate, and nonlinear bootstrap/identification
also retain their independent obligations.

**discharged (read boundary and source identities).** All scientific
sources below were read at the pinned commit. Bounded reads covered:
GOAL.md; FINISH.md's three requested sections; the complete short
`gates/dcoer-codex-e0c0b9a6f.md`; `fibre-propagator.md`'s definitions,
flat and background torus arguments, D-coer, BG, one-jump F-D and
hostile notes; `staircase-by-hand.md` Sections 1--5 and
Section 6 through line 477; `block-poincare-energy-package.md:1-110`;
`fd-local.md:84-160`; `lc-u.md:120-324,439-735`;
`composite-adjoint.md:1-36` for the actual contour convention;
mapped Text 3.1 at lines 376--401 and Text 5.3's (R1)--(R3)
paragraphs, located by targeted searches. Searches elsewhere
in the mapped file were navigation, not verification of its other
arguments. The source's numerical paragraphs were not used.

The absent sparse-worktree SCIENCE_WORKFLOW.md was read with git show
at the pinned revision; the locally available planning AGENTS.md
was read without checking it out. Its planning supplies no premise.
The exercise skill was inspected for applicability, not executed:
this is a bounded assigned derivation, not a new broad exercise or
campaign. No web/literature theorem, memory-only lemma, simulation,
machine enumeration, or computed proof certificate is part of the
argument. The prohibited files and the independent attempt were
not read. No subagent, audit, commit, push, PR or post was made.

**discharged (current recovery state).** Source identity remains
`048ba59a20c837f054c1125dc2d9c386fbc887f6`. Only
`library/fan-ext.md` was written; no editable prompt, instruction,
or other source file changed. The reusable constants are (2.1),
(4.3)--(4.6), (5.2)--(5.3), (6.4), (7.9), and (8.5). Failed routes
are the extra fine means on Y, the least-mass lift, and unqualified
use of the staircase geometry. The remaining decisions concern the
explicit background inputs above. This checkpoint grants no status.

PROVED
