# Independent moving-geometry extension reconstruction

This reconstruction precedes access to any author moving-nonlinear checker
or results. The complete new source was read at SHA-256
`939c87d2d4688e3f4e66550d3a54e024966866b8744db80d4befd3f1d68317d1`.
The precise state/rate definition, fixed-winding proof and nonlinear
entropy algebra were reused at the identities in the source manifest.

**Assessment:** no actionable gap found in the stated qualitative
extension. The new steps reconstruct correctly, including the use of the
actual nonstationary geometry marginal and rough microscopic matchings.
The quantitative addendum has not yet been read in this pre-comparison
packet and is not used below.

## 1. Conditional color entropy with the actual geometry marginal

The process is the closed matching/color projection. At every fixed M,
routed swaps preserve uniform product colors pi and have the same positive
floor r_*. An autonomous geometric mark maps (M,c) to (M',P c), with a
color-independent rate and a permutation P. Therefore the joint law
rho(t) times pi solves the full forward equation whenever rho(t) solves
the actual autonomous geometry equation. The color part annihilates pi
at fixed M, and geometric permutations preserve it. No stationary law of
M is being substituted for its actual marginal.

Write mu(M,c)=rho(M) pi(c) f_M(c). Conditional normalization is
E_pi f_M=1 for each M with positive mass. Then

    H0 = sum_M rho(M) E_pi f_M log f_M,
    0 <= H0 <= K log14.

For a geometric channel M->M' with rate a and permutation P, its
contribution to the derivative is

    a rho(M) E_pi f_M(c) [log f_(M')(P c)-log f_M(c)]
      = -a rho(M) KL(pi f_M || pi (f_(M') composed with P)) <=0.

This explicit formula assumes positive geometry masses; the finite-state
log-sum contraction yields the integrated extension to zero masses. In
particular, a point-mass initial geometry causes no problem. The formula
also shows how the derivative of the geometry marginal is included; using
an arbitrary frozen geometry reference at later times would be a different
quantity.

The color contribution at each M is bounded as in the preceding proof:

    H0' <= -2 N r_* sum_M rho(M) D_M(sqrt f_M).

Integrating gives K log14/(2 N r_*), uniformly over the initial geometry
law and correlations allowed by the conditional color preparation. This
argument conditions at the current time, not on a future geometry history,
and needs no later product structure of the actual color law.

Autonomy is substantive. As an outside-hypothesis countercontrol, start
with fixed geometry0 and a uniform binary color. Let geometry0->1 have
rate2 for color0 and rate1 for color1, with identity color action. At
t=log2 the joint law is

    [[1/8,1/4],[3/8,1/4]],

so conditional color entropy relative to the actual geometry marginal and
uniform color is strictly positive, though it started at zero. Thus
color permutations alone would not justify the contraction claim. The
source includes the autonomy assumption needed to exclude this example.

## 2. Exact owner coverage and connected internal graphs

For a physical cube of even side L, owner B_z contains all black sites
inside C_z and any black partners just outside whose white endpoints lie
inside. Hence L^3/2<=m_z<=L^3, and B_z lies in the one-step enlargement.

For each black anchor u, let A(u) be the set of cube origins containing u.
It has L^3 elements. Its nearest-neighbor partner v has another such set,
and their intersection has (L-1)L^2 elements. Thus an owner is present in
exactly

    |A(u) union A(v)| = L^3+L^2 = w_L

blocks, independently of its direction. Double counting yields
`sum_z m_z=K w_L`; therefore `omega_z=m_z/w_L` has total weight K. This
uses all N^3=2K physical cube origins, of both parities. Replacing this by
an unweighted average of variable-size owner blocks would lose this exact
identity.

Map the vertices and edges of the connected physical cube graph to their
pair owners. Its image is a connected multigraph on B_z, even when an
owner lies outside the physical cube. A nonloop edge comes from a physical
black-white edge (u,u+delta), and its owners are exactly u and q_delta(u).
It is therefore an actual bare routed swap. Parallel images retain their
multiplicity. Such swaps connect every color arrangement in a fixed block
count sector. Finitely many local matching patterns and count sectors at
fixed L give a positive minimum nontrivial gap g_L, uniform in M and N
once the local cube embeds. No large-L estimate is needed for this
qualitative proof.

A fixed nonmatching physical edge belongs to exactly (L-1)L^2 cubes.
Summing the internal bare Dirichlet forms, with these multiplicities,
therefore gives `(L^3-L^2) D_M`. Matching edges contribute zero on both
sides. This verifies the normalization of the internal/full comparison.

Conditioning on M, exterior colors and block counts gives uniform
reference block arrangements. For a conditional-mean-zero observable V,
the same square-root-density argument as before yields

    |E_mu V| <= 2||V||_infinity g_L^(-1/2)
                 sqrt(sum_M rho(M) E_pi D_(C_z,M)(sqrt f_M)).

This remains true for geometry-dependent V, blocks and weights: at fixed
M they are deterministic, and Cauchy-Schwarz over rho uses its unit total
mass. In particular omega_z can be absorbed into V because omega_z<=1.
Summing over 2K origins and integrating the conditional dissipation gives
`K C_(L,T)/sqrt(N)`. No conditional uniformity of mu is assumed.

## 3. Geometry-dependent routed coefficients cancel only at block scale

The permutation q_delta has displacement at most two lattice steps.
For a nonfixed route its consecutive four contexts are distinct: the
delta-coordinate displacement is positive, at most two, until a periodic
cycle closes, so its length is at least N/2. This is also part of the
unchanged routed premise. The predecessor is explicitly
`q_delta^(-1)(u)=u+d_M(u)-delta`. All four contexts stay within a fixed
physical distance of u.

Consequently all but O(L^2) anchors of B_z have their full stencils inside
the block. The exact count-conditional current differs from its product
expectation F_delta(pbar_z)/2 by O(1/m_z), by four-index sampling coupling.
The factor a_delta(u) is retained inside this local average; it is bounded
but can be microscopically rough. Fixed routes have a_delta=0 and cause
no repeated-site problem.

The local tensor is

    T_z=(1/2) sum_delta sum_(u in B_z) a_delta(u) tensor delta.

Substituting a_delta=delta-d_M(q_delta u), the first part equals m_z I.
The second part is a boundary error. Indeed q_delta(B_z) differs from B_z
only in a fixed-width boundary strip, and

    sum_(u in B_z) d_M(q_delta u)
      = sum_(v in B_z) d_M(v)+O(L^2).

The leading vector sum is independent of delta and cancels against
sum_delta delta=0. This is a deterministic identity up to the boundary
error for every matching; no matching isotropy or expectation over M is
used.

One explicit uniform bound is available for checking the order: both
B_z and its image contain the black sites of the cube shrunk by two,
and lie in the cube enlarged by three. Their symmetric difference is at
most `[(L+6)^3-(L-4)^3]/2 <=18 L^2` for L>=16. Thus the tensor error's
Euclidean matrix norm is at most 54 L^2. Optimization of this constant is
irrelevant here. The pointwise tensor need not be I; the independent
rough-matching fixture includes a nonzero pointwise countercontrol.

After dividing the block sums by w_L, boundary errors cost O(K/L),
canonical errors O(K/L^3), and translating smooth coefficients O(K L/N).
The conditional mixing estimate adds K C_(L,T)/sqrt(N). The remaining
routed entropy term is exactly the weighted continuum-flux expression
in the source, up to these errors.

## 4. Actual plaquette marks and zero canonical mean

Direct record tracking on a flippable square confirms the supplied
projection: clockwise and counterclockwise rotations preserve all four
keys and their pair memberships, move every record by one edge, and give
the opposite geometric matching. At the two black positions, one mark
swaps the pair colors and the other is the identity; which sense swaps
depends on the initial matching orientation. Equal rates nu give exactly
one color-swap drift at rate nu, alongside geometry flip rate 2nu.

Hence for the log profile Theta the actual geometric drift is

    nu sum_(flippable P) [theta(v_P/N)-theta(u_P/N)]
                                      .(I_(u_P)-I_(v_P)).

The coefficient and flippability depend on M only. Conditional on block
counts, any two distinct positions have identical one-point marginals;
the indicator difference has exact zero mean even in boundary count
sectors. Averaging the marked channels by the chosen black anchor uses
the same coverage w_L. Removing boundary squares, expanding only the
smooth theta, and applying conditional block mixing proves the stated
vanishing time-integrated geometric drift on the Euler scale.

This is not a pathwise assertion that each plaquette current is zero.
An inhomogeneous product profile is not invariant under these spatial
permutations; its actual drift is kept in the entropy calculation and
then controlled by this argument.

## 5. Weighted entropy closure uniform in the geometry law

The exact comparison identity is

    h=H0-E_mu Theta-K log14.

Its derivative uses the full conditional entropy estimate above. The
derivative of an assumed stationary matching density is never dropped.
Owner-block averaging is an algebraic identity at each time; neither the
random blocks nor their weights are differentiated in time.

For any smooth deterministic scalar f, the exact owner coverage gives

    sum_z omega_z f(z/N)=sum_black_u f(u/N)+O(K L/N),

uniformly in M. Apply this to the entropy-flux divergence to control the
constant term. The linear Taylor coefficient cancels pointwise on the
simplex tangent by the same PDE/symmetrizer identity as in the fixed
proof, with any weight omega_z. The remainder is bounded by
`C sum_z omega_z |pbar_z-p(z/N)|^2`.

Condition the reference law on M. Its colors are independent with the
prescribed spatial probabilities; blocks of disjoint owners are
independent. If B_z and B_z' overlap, endpoints of the same nearest-neighbor
pair lie in their respective cubes, bounding origin displacement by a
cube of side at most 2L+3. Thus an overlap coloring with chi=32L^3 slots
is available for L>=16, including empty classes. No periodic tiling or
statistical regularity of M is assumed.

The previously derived fourteen-coordinate estimate is

    E exp[(m_z/14)|pbar_z-E pbar_z|^2] <=29.

With alpha=1/1792,
`2 alpha chi=L^3/28<=m_z/14`; omega_z<=1 only reduces that exponent.
Holder over the overlap coloring therefore gives at most
`(2K/chi)log29` for the centered contribution. The smooth mean shift is
O(L/N), and its total weighted cost is C alpha K L^2/N^2 by
sum omega_z=K. All these bounds hold for every M with identical constants,
so averaging any actual rho(t) preserves the exponential bound.

The entropy inequality consequently gives

    E_mu sum_z omega_z |pbar_z-p_z|^2
      <= h/alpha+C K/L^3+C K L^2/N^2.

The coefficient of h is independent of L. The stated Gronwall estimate
then follows. Hold even L fixed, take N through even values tending to
infinity, and then take L to infinity. This proves the qualitative
conditional entropy-density limit without a gap rate or geometry-mixing
estimate.

The comparison color marginal is the deterministic product profile,
irrespective of rho. Fixed-time concentration therefore transfers by the
entropy event inequality. Routed and plaquette moves both have bounded
displacement, total rate O(K) and smooth-test jumps O(1/(N K)); Euler
acceleration gives bracket O(1/(N K)) and bounded drift. The existing
Doob/finite-mesh argument proves the uniform-time empirical conclusion.

## 6. Controls, scope and failures

The independently written checker constructs a sparse irregular perfect
matching on a torus with N=180, L=16, by a fixed finite sequence of legal
plaquette changes. Three owner cubes test actual contracted connectivity,
physical-edge multiplicities, all local routed stencils, the tensor
boundary error and a pointwise-tensor counterexample. Exact pair-origin
coverage is checked in several actual matching directions. A separate
N=12,L=4 enumeration counts every origin/anchor incidence; it tests the
combinatorial identity, not the theorem's large-block hypothesis.

The complete 392-state two-color-position/fourteen-label plaquette
projection tests the geometric conditional-entropy derivative with a
nonstationary marginal, its negative-KL expression, the evolving uniform
conditional reference, and finite-time contraction including point-mass
initial geometry. The color-dependent-rate countercontrol is explicitly
outside the hypotheses. Exact canonical indicator cancellations and
the constants alpha, chi and m_min complete the new controls.

The first independent execution succeeded. Full source, outputs, versions,
empty stderr and command receipt are retained; no failed attempt was
discarded. These are selected finite controls of the argument, not a
simulation of its hydrodynamic limit.

The result concerns the matching/color projection, supplied entropy-close
inhomogeneous color preparation, a fixed positive routed floor, autonomous
color-independent plaquette marks, and a stipulated fixed smooth interior
PDE solution. It does not give a nonlinear evolution law for the separate
geometric Gauss field, birth-produced preparation, shocks, boundary
continuation, microscopic key statistics or quantum dynamics. The
qualitative limit alone gives no rate or simultaneous block choice.
