# An explicit uniform error bound for the record-color Euler limit

2026-09-21. Root conditional proof candidate; separate checking pending.
This refines the routed and moving-geometry proofs without changing their
generator, color law, fields or time scale. The preparation result is reused
only for the optional transfer from completed formation.

The earlier proof took N to infinity at fixed block radius and then enlarged
the block. Its existence-only block gap and unspecified fixed-block remainder
can be replaced by explicit estimates. The resulting exponent is a sufficient
upper bound, not an optimal rate, a fitted exponent or a finite-size diffusion
law.

## 1. Statement

Fix full-support color probabilities p, k0>|gamma|, a bounded plaquette rate
nu>=0, a finite observation horizon T, and finitely many fixed Fourier modes
Q=2pi m. Keep all assumptions of DIMER_ROUTED_RECORD_TRANSPORT.md and, for
nu>0, DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md. Initially take product colors
independent of an arbitrary full matching law; the latter may be deterministic.

There is a finite C=C(p,k0,gamma,nu,Q,T), independent of the even N and the
initial matching law, such that, for sufficiently large N,

    sup_(0<=t<=T) E ||Y_N(Q,t)-exp(-i A(Q)t)Y_N(Q,0)||^2
                   <= C N^(-1/6).                         (1)

This is a supremum of expectations, not the expectation of a path supremum.
The L2 norm is at most C^(1/2)N^(-1/12). With the previously stated
post-completion preparation at epsilon_N=N^-4, the same squared bound holds
with an additional O(N^-1) term. A physical endpoint-normalized field retains
its known sqrt(2) factor and an additional squared O(N^-2) discrepancy.

The proof below establishes the block estimate for every integer radius
6<=l with 2l+5<N/2. In this range its squared error bound is

    C [l^5/N + 1/l + l^2/N^2 + 1/N].                      (2)

Choosing l=floor(N^(1/6)), for sufficiently large N, proves (1). No numerical
constant C or useful finite-N accuracy threshold is claimed. The original
finite-volume simulation evidence remains separate.

## 2. An explicit gap on every contracted local cube

Let B be the all-site cube of side L=2l+1 centered at a black site, and C its
set of matched pairs having at least one endpoint in B. The cube embeds
without a periodic identification in the stated radius range. Write m=|C|.
Every pair covers at most two cube sites, so m>=L^3/2. Choose one endpoint
inside B as a representative for each pair, deterministically. Representatives
of different pairs are distinct. The image of the connected lattice graph
inside B is a connected graph on C, contained in the actual contracted graph.

For every ordered pair of sites of B, route in coordinate order 1,2,3 using
the unique monotone coordinate segments. A physical edge in direction i
cutting that coordinate after a sites is used by exactly

    2 a(L-a) L^2 <= L^4/2                                (3)

ordered paths. The factor two counts the two orientations; the other two
coordinates each leave one freely chosen endpoint coordinate. There is no
periodic tie convention here. Each path is simple and has length at most
3(L-1).

For every unordered pair of elements of C, choose one lexicographic order
of their representatives and use that physical path. These are a subset of
the ordered all-site paths, so (3) bounds their edge loads. Contract matching
edges and erase loops. This cannot lengthen the path or introduce an edge.
Each simple contracted edge has at most two physical representatives by
bipartiteness. Its reference-path load is therefore at most L^4.

The forward/reverse endpoint-transposition word has length at most
2[3(L-1)]-1<=6L, and each edge appears at most twice. Its total edge use over
all chosen endpoint pairs is at most 2L^4. With the same unit-rate form
convention as the preparation proof,

    D_all <= 12L^5 D_C,
    Var(f) <= (2/m)D_all <= 48L^2 D_C.                    (4)

Here D_C includes only simple contracted edges represented inside B. Every
one is a legal whole-pair exchange of the full process. Given exterior
colors and the counts on C, the uniform sector is invariant under each
internal transposition, so the previously proved complete-permutation
inequality applies. Same-color swaps have zero increment. The actual global
symmetric Dirichlet form dominates each included edge form with rate k0/2.
Thus the local inverse-gap factor A_l used in the replacement proof can be
taken at most 48(2l+1)^2 for the unit-rate form, or 96(2l+1)^2/k0 when its
rate domination is included. Only the O(l^2) bound is needed below.

The argument does not assume that a context-truncated nonreversible block
generator has the product law. It uses conditional variance and actual
symmetric swap forms, exactly as the original replacement proof.

## 3. Quantitative centered-current and canonical bounds

The current uses four distinct pairs within a fixed radius. For l>=6 they
lie in C. Let h_u be the current minus its conditional expectation given
the C counts. It is bounded uniformly in l and orthogonal to those counts.
Conditional Poincare, the variational H-minus-one formula, and the O(l^3)
overlap of the block supports give

    ||K^(-1/2) sum_u a_u h_u||_(-1,S_M)^2 <= C l^5       (5)

for uniformly bounded deterministic a_u. Constants include the fixed rates,
color probabilities and finite number of directions. In fixed geometry the
stationary forward/backward estimate gives an integrated squared bound
C T l^5/N. In moving geometry the already proved intervalwise estimate gives
the same bound conditioned on any autonomous marked geometry history. Its
constant has no factor counting geometry jumps.

Let q_C be the empirical color law on C. Sampling the four current colors
without replacement instead of independently changes its expectation by
at most C/m. The current expectation is a polynomial in p with uniformly
bounded first and second derivatives on the probability simplex. Taylor's
formula and the fourth-moment bound for a bounded iid empirical mean yield

    hat j = J(p)+A(q_C-p)+W,
    E W=0,       E||W||^2 <= C/m^2 <= C l^(-6).           (6)

The mean is exactly zero separately for each matching footprint. At most
C l^3 supports overlap a fixed one, so the normalized spatial sum of W
has squared norm at most C l^-3. Its integrated squared bound is C T^2 l^-3.

Replace q_C by q_l, the empirical law on the black sites of the ordinary
cube about u. Their sets differ in at most C l^2 positions, and both
cardinalities are of order l^3. In the resulting centered linear combination,
the C l^2 boundary coefficients are O(l^-3); the C l^3 common coefficients
change by O(l^-4). Its squared norm is therefore at most C l^-4.
The O(l^3) overlap bound makes the normalized spatial sum's squared norm
at most C/l. Shifting this ordinary black cube by a black-to-black lattice
displacement of length at most two gives the same estimate. All counts and
constants are uniform for l in the range of Section 1.

## 4. Uniform phase errors rather than a fixed-block constant

The phase-gradient expansion is

    N[phi(q_delta u)-phi(u)]
      = -i phi(u) Q.(delta-d_(q_delta u)) + r_(delta,u),
    |r_(delta,u)| <= C_Q/N.                              (7)

Its constant is independent of l because each routing displacement has
length at most two. To control its product with a smoothed centered field,
write q_l(u)-p=m_l^-1 sum_(v in B_l(u)) z_v, z_v=xi_v-p.
For any coefficients b_u bounded by B,

    K^(-1/2) sum_u b_u [q_l(u)-p]
       = K^(-1/2) sum_v c_v z_v,
    |c_v| <= B,                                         (8)

because each black site belongs to exactly m_l translated ordinary black
cubes. Independence of the z_v gives a squared bound C B^2. The same
conclusion, with a fixed geometric constant, holds for C blocks: their
cardinalities are bounded below by c l^3 and each site belongs to at most
C l^3 of them. Consequently the phase remainder in (7) and the extra
O(N^-1) phase change in the incoming-direction cancellation have squared
norm at most C/N^2, with no hidden l-dependent factor.

For the main ordinary-cube average, translation invariance makes its Fourier
sum exactly b_l(Q/N)Y_N, where b_l is the normalized average of phase factors
over the black offsets in that cube. Every offset has norm at most sqrt(3)l,
so |b_l(Q/N)-1|<=sqrt(3)|Q|l/N. The exact stationary second moment of Y_N is
bounded independently of geometry and N, giving squared error C l^2/N^2.
No symmetry improvement of that estimate is needed.

The incoming matching-direction term is canceled using the pointwise
identity sum_delta A_delta=0 and reindexing the routing permutation. The
remaining shifted ordinary-cube terms have squared bound C/l from Section 3;
their phase differences use (8). Thus its quantitative treatment does not
assume a regular or equilibrated matching.

## 5. The joint martingale and the propagated error

Combining (5)-(8), the integrated routed drift error has squared expectation
at most C_T[l^5/N+1/l+l^2/N^2]. The canonical l^-3 term is smaller than 1/l.
The original local-jump estimate bounds the martingale bracket by C T/N.
For moving geometry the additional plaquette drift has integrated squared
bound C T nu^2|Q|^2/(k0 N), and its bracket is also O(N^-1). These bounds
hold uniformly in the entire geometry history where conditioning is used;
the actual martingale is still that of the unconditioned joint process.

Let E_N(t) be the difference between Y_N(t) and its Euler propagator. The
martingale decomposition gives

    E_N(t) = M_N(t)+R_N(t)-i A(Q) integral_0^t E_N(s) ds,

where the integrated drift error R_N has the preceding uniform second-
moment bound. A fixed-dimensional variation-of-constants estimate, or
Cauchy--Schwarz followed by Gronwall on E||E_N(t)||^2, gives (2), with a
constant depending on A(Q) and T. It requires only fixed-time second moments
uniformly over the interval. Taking l=floor(N^(1/6)) proves (1).

The optional formed-state transfer uses the already checked path-law total-
variation estimate epsilon_N=N^-4. Since the squared field residual is
bounded by C_T K, its expectation changes by at most C_T K epsilon_N=O(N^-1).
This is smaller than (1); the random time to complete formation remains
additional. No optimal rate or numerical fit has entered this proof.

## 6. Decisive controls and remaining scope

Finite controls should check the open-cube physical edge loads in (3), the
contracted endpoint words for matching footprints meeting a boundary, and
the coefficient bounds in (8) including irregular footprints. The all-N
conclusion rests on the uniform combinatorial and moment estimates above,
not on a finite-size regression. The original wave theorem, its moving-
geometry extension and the complete-permutation inequality remain explicit
dependencies until the selective check of this refinement is complete.

The positive longitudinal color variances, separate geometric Gauss field,
supplied microscopic clock, absence of quantum preparation and missing
physical field identification are unchanged.
