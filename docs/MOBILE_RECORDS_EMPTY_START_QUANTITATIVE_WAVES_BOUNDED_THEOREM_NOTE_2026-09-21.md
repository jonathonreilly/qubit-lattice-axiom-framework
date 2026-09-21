---
claim_id: mobile_records_empty_start_quantitative_waves_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied permanent-paired-record process on even cubic tori, an auxiliary bipartite-graph comparison bounds every nonfull slide gap polynomially. A killed-chain estimate gives a polynomial expected filling-time bound at every fixed positive birth and slide rate. A separate quantitative refinement bounds the stationary finite-mode Euler color-wave squared error by O(N^-1/6). These results compose into an unconditioned wave window at a polynomial deterministic time from an empty lattice. The displayed powers are conservative upper bounds, not measured exponents or practical time scales. No fixed-rate uniform matching selection, geometric photon, quantum preparation or TOE is derived."
upstream_dependencies:
  - minimal_axioms
  - mobile_records_moving_geometry_color_waves_bounded_theorem_note_2026-09-21
runner: scripts/mobile_records_empty_start_quantitative_waves_2026_09_21.py
---

# Quantitative color waves from an initially empty record lattice

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

The supplied process can start with every site vacant, form permanent pairs
while existing records move, and reach a color-wave observation window at
a predetermined time. This improves the earlier
[formed-state result](MOBILE_RECORDS_MOVING_GEOMETRY_COLOR_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md) by bounding its random
formation phase and making its wave-error estimate quantitative.

This construction is not a derivation from the
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). It inherits paired births,
marked partnerships, exact classical content recognition, the specified
fourteen-color probabilities, local exchange and slide rates, and a physical
clock. It uses the same microscopic law throughout. Dummy vertices and
nonlocal auxiliary exchanges appear only inside a mathematical comparison.

Let N>=8 be even and K=N^3/2. With fixed beta,kappa>0, k0>|gamma| and
bounded fixed plaquette rate nu>=0, the complete arguments below give:

1. Every nonempty, nonfull geometric layer has slide gap at least
   kappa/(2^23 K^22). The comparison imports the previously identified
   Jerrum--Sinclair matching-chain theorem and Taggi's cubic monomer bound,
   with the same source identities and normalization as the formation
   dependency. The new steps are exact padded fibers and their variance
   and Dirichlet-energy comparison.
2. From the empty lattice, the expected full-matching time F satisfies

       E F <= A_N = 2K^3/beta + 2^27 K^26/kappa.

   This holds at every fixed positive beta and kappa. It does not imply
   uniform matching selection at those rates. A different, explicitly
   volume-dependent rare-birth schedule gives a separate uniform-selection
   result; its limits are stated in Part I.
3. With iid reference colors and any full matching law, the finite-mode
   squared Euler propagation error is at most C N^-1/6 for sufficiently
   large N and fixed modes and macroscopic horizon. Its constant depends
   on the fixed probabilities and rates and is not given as an accuracy
   estimate. The norm rate is N^-1/12. Bounded autonomous geometry motion
   is included.
4. For any 0<eta<1, a deterministic observation time is

       t_N = 2A_N/eta
             + [8N(3N-1)/k0][(K/2)log14 + log(1/eta)].

   The actual empty-start future law, projected onto matching geometry and
   pair colors, is within eta in total variation of a full-state reference
   process with iid colors and an allowed, possibly biased matching law.
   This comparison does not claim mixing of the extra immutable record keys. With eta=N^-4, its squared wave error is bounded
   by C N^-1/6+C' N^-1. Histories that have not completed are included in
   the error bound; no success conditioning or reset is performed.

The resulting sufficient deterministic time is O(N^82) at fixed positive
rates. This very large power reflects loose worst-case estimates. It is
neither an observed filling exponent nor a claim of useful practical
preparation time. The purpose of the bound is to make the conditional
empty-start construction finite and explicit in one limit.

For the stated orbit-isotropic color probabilities, four vector modes
propagate with c=|gamma|sqrt(rho_A rho_B/3) at nonzero gamma and wavevector.
The general matrix theorem does not impose that mode count. The color
field's static longitudinal fluctuations remain distinct from the geometric
Gauss constraint. No physical electromagnetic identification follows.

The three complete source arguments are reproduced below with titles
removed and headings shifted. Their historical pending-review sentences
are preserved. The source-bound selective reports in the evidence packet
define the completed check coverage; formal retention remains unaudited.

## I. Every-stage relaxation and fixed-rate filling

2026-09-21. Root conditional proof candidate; independent check pending.
This completes a quantitative comparison left open in the all-stage clock
note, for bipartite graphs with a perfect matching and a controlled final-pair
matching-count ratio. The microscopic process is unchanged. Auxiliary dummy
vertices, deletions and nonlocal exchanges are proof devices only.

### 1. Definitions, dependencies and results

Let G be a connected simple bipartite graph with K vertices in each part,
K>=2, m edges and at least one perfect matching. Let a_r be its number of
r-edge matchings, with a_r=0 outside 0<=r<=K, and put R=a_(K-1)/a_K.
The physical geometric slide generator S_j has rate kappa>0 for every
legal replacement {b,c}->{a,b} when a is vacant. It preserves rank j.
Birth adds a vacant edge at rate beta>0. Both are the rules of the earlier
geometric formation notes. Additional symmetric conservative moves may be
included; they improve the Dirichlet lower bounds used here.

For 1<=j<K, write k=j+1, h=K-k and

    m_hat = m+2hK,
    R_hat = (h+1)^2 a_j/a_k + 2h + a_(k+1)/a_k,
    U_j = (h+1)R + 2h + m/(k+1),
    C_j = 1+(2K-2)(m+m^2)(k-1)(k+1+2m).

Then R_hat<=U_j, and the following sufficient slide-gap bound holds:

    gap(S_j) >= kappa/[256 m_hat^2 (h+2) R_hat^4 C_j]
              >= kappa/[256 m_hat^2 (h+2) U_j^4 C_j].     (1)

For the even cubic nearest-neighbor torus N>=8, K=N^3/2 and m=6K. Importing
the same explicitly identified Taggi v3 monomer bound R<=K^2/6 gives the
deliberately coarse uniform consequence

    gap(S_j) >= kappa/(2^23 K^22),  1<=j<K.              (2)

The established Jerrum--Sinclair Broder-chain bound, including its exact
continuous-time normalization, is reused from
GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md. Its primary Theorems 2.2
and 3.6 had already been checked at the pinned source identity. The
all-cardinality connectivity, counting injection and slide/adjacent-rank
comparison are reused from GEOMETRIC_ALL_STAGE_FORMATION_CLOCK.md. Those
dependencies remain explicit; no new proof of the 1989 theorem is claimed.

Section 5 gives a uniform killed-chain estimate at every beta>0. In
particular, the cubic process satisfies

    E_empty T_fill <= 2 K^3/beta + 2^27 K^26/kappa.        (3)

This is a conservative mathematical upper bound on the supplied process.
It is not a measured growth exponent, sharp time scale, assertion of fast
practical preparation or fixed-rate uniform-matching selection. The large
power results from several loose comparisons.

### 2. A padded bipartite graph and its exact fibers

For a fixed stage j, adjoin h labeled dummy vertices to each part of G.
Connect every left dummy to every original right vertex and every right
dummy to every original left vertex. Add no dummy--dummy edges. Call this
graph G_hat. It is connected and simple, has 2(K+h) vertices and m_hat
edges, and has perfect matchings because a_k>0.

Use the ordinary continuous-time Broder chain on its perfect and near-
perfect matchings, with rate kappa per legal slide, completion or deletion
from a perfect matching. Its invariant law is uniform on that combined
space. Project a matching to the edges joining two original vertices.
Write f0=(h!)^2. The exact fiber counts are:

| Augmented state | Original rank | Fiber count per original matching |
| --- | ---: | ---: |
| Perfect | k | f0 |
| Near-perfect, both holes original | j=k-1 | (h+1)^2 f0 |
| Near-perfect, one original and one dummy hole | k | 2h f0 |
| Near-perfect, both holes dummy | k+1 | f0, when h>=1 |

For a perfect augmented matching, the h unmatched original vertices in
each part are assigned bijectively to the opposite dummy set. This gives
(h!)^2 possibilities. For two original holes, choose one unassigned
original vertex out of h+1 on each side, then assign the other h. For one
original and one dummy hole, one side has h choices of original hole, h
choices of dummy hole and (h-1)! assignments, while the other side has h!
assignments. Its count is h f0; there are two orientations. For two dummy
holes, the count is h^2((h-1)!)^2=f0. When h=0 this last class is absent
and a_(k+1)=0.

Thus the augmented near-perfect/perfect ratio is exactly R_hat. The
earlier injection gives a_j/a_k<=R/(K-j)=R/(h+1). Counting possible next
edge additions gives (k+1)a_(k+1)<=m a_k. These establish R_hat<=U_j.
They do not require an oracle or sampling of a uniform matching.

The imported Broder result applies to G_hat and yields

    gap(Broder_hat) >= kappa/(256 m_hat R_hat^4).          (4)

This chain contains no physical interpretation of a dummy vertex or record
deletion. The following comparison removes those auxiliary states.

### 3. Compare with the already defined adjacent-rank chain

Let B_j be the auxiliary chain of the all-stage note on
Omega_j union Omega_k: rate kappa for each single-edge addition/deletion
between levels and each valid single-edge exchange within either level.
The exchange may replace disjoint edges. It has the uniform invariant law.
Let Z_B=a_j+a_k, and write D_B(g)=kappa/Z_B times the sum of squared
differences over its unoriented transition edges.

Call augmented states with original rank j or k good; the remaining states
have original rank k+1 and two dummy holes. For a function g on B_j, define
F on the full augmented Broder space by

    F(eta)=g(M),                     if eta is good with projection M;
    F(eta)=(1/(k+1)) sum_(e in U) g(U-e),
                                     if its projection U has rank k+1. (5)

All augmented transitions between two states with two dummy holes leave U
unchanged. Indeed a slide adds an edge incident to a dummy hole; it can
only remove a dummy edge (unchanged U) or an original edge (exit to rank k).
There is no edge between the two dummy holes for completion. Every exit
from such a state has original projection U-e for an edge e of U.

A transition between good states either leaves the projection fixed or
projects to one B_j edge. An original/original deletion or addition changes
rank by one; replacing two original edges sharing the slide center is a
single-edge exchange. A slide involving only dummy edges leaves the
original matching unchanged. These cases exhaust the Broder moves.

Every augmented state has at most m_hat outgoing nontrivial transitions:
each graph edge supplies at most one legal proposal. Put

    f_min=(2h+1)f0,    f_max=(h+1)^2 f0.

These are the minimum and maximum good fiber sizes, including h=0. Let
Z_hat be the total augmented state count. For every constant c,

    (1/Z_hat) sum_eta |F(eta)-c|^2
       >= (f_min/Z_hat) sum_(M in B_j) |g(M)-c|^2.

Taking minima over c gives

    Var_hat(F) >= w Var_B(g),    w=f_min Z_B/Z_hat.       (6)

For a fixed projected B_j edge, at most f_max m_hat good-to-good
augmented transitions lie over it. Their normalized Dirichlet energy is
therefore bounded by kappa f_max m_hat/Z_hat times the B_j squared-edge
sum. For a fixed rank-(k+1) matching U and one parent U-e, at most
f0 m_hat augmented transitions connect that parent fiber to the two-dummy-
hole fiber over U. All internal edges of the latter have zero F increment.

Using the complete-graph variance identity,

    sum_(e in U) |g(U-e)-average|^2
        = (1/(k+1)) sum_(unordered e,f in U)
                                      |g(U-e)-g(U-f)|^2,

its boundary energy is at most kappa f0 m_hat/[Z_hat(k+1)] times the
last sum. Each pair U-e,U-f is one upper-level B_j exchange, and its union
uniquely specifies U. Hence these pairs are not duplicated across U.
Combining both energy bounds gives

    D_hat(F) <= w m_hat [f_max/f_min + f0/((k+1)f_min)] D_B(g)
              <= w m_hat(h+2) D_B(g).                   (7)

For h=0 there is no two-dummy boundary; the extra positive term is simply
an unused upper bound. The last inequality follows from
(h+1)^2/(2h+1)<=h+1 and 1/[(k+1)(2h+1)]<=1.

The Rayleigh inequality for (4), together with (6)-(7), yields

    gap(B_j) >= gap(Broder_hat)/[m_hat(h+2)].              (8)

No Markov property for the projected augmented trajectory is assumed.
In particular, the perfect and mixed-hole fibers at rank k need not have
identical projected transition rates. The function-extension comparison
is sufficient, and its fiber mass cancels explicitly in (6)-(7).

### 4. Return to physical slides and bound the cubic constants

The already proved empty-corridor comparison gives

    gap(S_j) >= gap(B_j)/C_j.

Its paths contain only actual immutable-record slides. Applying (4) and
(8) proves (1). The graph padding is bipartite; no analogous assertion is
made for a nonbipartite graph by this argument.

On the cubic torus, K>=256 and m=6K. Since j>=1,
h<=K-2 and h+2<=K. The following deliberately loose bounds suffice:

    m_hat <= 4K^2,
    U_j <= K^3/6 + 4K <= K^3,
    C_j <= 2^11 K^5.

For the last inequality use 2K-2<=2K, m+m^2<=42K^2,
k-1<=K and k+1+2m<=14K; adding the leading one stays below 2^11 K^5.
Substituting into (1) gives (2), since
256*(4K^2)^2*K*(K^3)^4*(2^11K^5)=2^23K^22.

### 5. A killed-chain estimate at arbitrary positive birth rate

This elementary estimate does not require rare births. In one nonempty
rank-j layer let L=-S be its positive symmetric generator, pi uniform,
g>0 a lower bound on its gap, n=a_j, and h(M) its vacant-edge count.
Assume 0<=h<=m and pi(h)=p>0. For a real or complex f=c+v with
c=pi(f) and pi(v)=0, the weighted triangle and square inequalities give

    p|c|^2 <= 2 pi(h|f|^2)+2m ||v||_2^2.

Thus, with E(f)=<f,Lf>+beta pi(h|f|^2),

    ||f||_2^2 <= [2/(beta p)+(1+2m/p)/g] E(f).           (9)

The smallest eigenvalue of L+beta H is consequently at least the reciprocal
of the bracket. The survival probability from a point is
(exp[-t(L+beta H)]1)(M). Its L2 norm decays at that rate and evaluation at
a point costs sqrt(n), so survival is at most min(1,sqrt(n)e^(-lambda t)).
Integrating gives the uniform mean bound

    E_M tau_j <= (1+(1/2)log a_j)
                  [2/(beta p_j)+(1+2m/p_j)/g_j].         (10)

For a singleton layer no gap is needed; its constant hazard gives the
exact exponential waiting time. The empty layer has mean 1/(beta m).
The formula is only used where the uniform sector has positive variance;
one may give a singleton an infinite gap and use (10) as an upper bound.

The strong Markov property and uniformity in the entrance matching permit
summing (10) across stages. On the cubic torus, the earlier counting
injection implies

    p_j=(j+1)a_(j+1)/a_j >= (j+1)(K-j)/R >= 6/K.

Also log a_j<=log(2^m)<=6K, so 1+(1/2)log a_j<=4K,
m/p_j<=K^2 and 1+2m/p_j<=3K^2. Each term (10) is at most

    (4/(3beta))K^2 + (12*2^23/kappa)K^25.

There are fewer than K such terms. Adding 1/(6beta K) and using
12*2^23<2^27 proves (3). Extra symmetric geometry motion can be retained:
it preserves the uniform layer law and increases the conservative gap.
The full birth/slide process remains irreversible because births add records.

### 6. One explicit simultaneous uniform-selection schedule

The fixed-rate filling bound does not make the first completed geometry
uniform. For that stronger selection goal the earlier rare-killing estimates
can now use a polynomial bound at every stage. From (2) and log a_j<=6K,

    B_j=(1+log a_j)/g_j <= 2^26 K^23/kappa.

Choose, as an explicitly volume-dependent auxiliary family,

    beta_K = kappa 2^(-32) K^(-27).                       (11)

Then delta_j=beta_K m B_j<=3/(32K^3). The total-variation distance between
the entire sequence of postbirth geometries and independent uniform
matchings of their respective ranks is at most

    sum_j 2delta_j <= 3/(16K^2).                          (12)

This follows by composing the uniform conditional exit-kernel bounds;
the empty stage has its exact uniform first edge. For normalized stage
clocks W_j=beta_K p_j tau_j, the joint Laplace transform at any fixed
vector 0<=lambda_j<=Lambda differs from the product of independent
unit-exponential transforms by at most 3(1+Lambda)/(16K^2). This uses the
earlier bounded killed-transform kernels and their telescoping composition.
It does not assert total-variation convergence for the continuous waiting
times in a dimension changing with K.

The stage conditional means satisfy

    sup_M |E_M W_j-1| <= 3/(13K^3).

Hence beta_K E_empty T_fill/C(G) has the same relative error bound, where
C(G)=sum_j 1/p_j. Together with C(G)<=K H_K/3 this supplies an expected
time O(K^28 log K/kappa) for the special selection family (11).
It is an ordered family of supplied rates, not a volume-independent law
or a claim that the fixed-beta process selects uniform matchings.

### 7. Connection to formed-state waves and remaining limits

At fixed positive beta and kappa, the color-coded paired formation rule has
the same autonomous geometric process and now the explicit expected filling
bound (3). Its final color counts remain multinomial, independently of the
geometric trajectory. The separately checked O(N^5) color-preparation time
and arbitrary-matching wave theorem can therefore follow a polynomially
bounded expected empty-start formation phase. A simulation need not approach
the enormous worst-case bound for the proof to apply.

If near-uniform full geometry is also required, (11)-(12) provide it; later
symmetric plaquette motion preserves the uniform reference law. The colors
and geometric Gauss field remain distinct. None of these improvements
derives the microscopic rates, exact content recognition, quantum coherence,
a propagating geometric photon or a physical theory of everything.

Finite controls must verify every padded fiber class, actual augmented
transition projection and the variance/energy normalization. The killed-
operator estimate requires separate matrix controls. These are tests of
the proof, not evidence of an empirical filling exponent. Independent
checking and publication integration remain pending.

## II. Quantitative propagation through moving geometry

2026-09-21. Root conditional proof candidate; separate checking pending.
This refines the routed and moving-geometry proofs without changing their
generator, color law, fields or time scale. The preparation result is reused
only for the optional transfer from completed formation.

The earlier proof took N to infinity at fixed block radius and then enlarged
the block. Its existence-only block gap and unspecified fixed-block remainder
can be replaced by explicit estimates. The resulting exponent is a sufficient
upper bound, not an optimal rate, a fitted exponent or a finite-size diffusion
law.

### 1. Statement

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

### 2. An explicit gap on every contracted local cube

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

### 3. Quantitative centered-current and canonical bounds

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

### 4. Uniform phase errors rather than a fixed-block constant

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

### 5. The joint martingale and the propagated error

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

### 6. Decisive controls and remaining scope

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

## III. Deterministic observation from empty initialization

2026-09-21. Root conditional composition argument; independent check pending.

This note composes the proposed all-stage polynomial filling estimate with
the separately checked formed-state preparation and moving-geometry wave
results. It introduces no new microscopic transition. The geometric process
is autonomous, its records are permanent, and the fourteen pair colors have
the specified birth law. Rates, classical content recognition, paired births
and a physical clock remain supplied premises.

### 1. The explicit deterministic schedule

On an even cubic torus N>=8, set K=N^3/2 and take fixed beta,kappa>0,
k0>|gamma| and bounded fixed plaquette rate nu>=0. Start with every site
vacant. Let F be its first full-matching time. The proposed all-stage
estimate, if accepted, gives

    E F <= A_N := 2 K^3/beta + 2^27 K^26/kappa.

Fix any 0<eta<1. Define

    H_N = 2 A_N/eta,
    s_N = [8N(3N-1)/k0] [(K/2)log14 + log(1/eta)],
    t_N = H_N+s_N.                                      (1)

Both times are deterministic. Markov's inequality gives

    P(F>H_N) <= eta/2.                                   (2)

The formed-state preparation theorem with epsilon=eta/2 gives a conditional
total-variation error at most eta/2 after s_N units of post-formation color
evolution, uniformly in the completed arrangement and geometry history.
If completion occurs before H_N, evolution has at least s_N units to mix
before t_N. Longer evolution preserves the same contraction bound.

The event E={F<=H_N} is determined by the autonomous geometry. Conditional
on its entire history, the final color counts still have the multinomial
law with K trials and the specified full-support probability vector p.
Transport and rotations permute these immutable colors; they do not change
their counts. The uniform distribution within each count sector, mixed
with those multinomial probabilities, is exactly p^K.

Consequently, conditional on any geometry history in E, the color law at
t_N is within eta/2 of p^K. This statement uses the previously proved
contraction for an arbitrary prescribed sequence of geometry intervals and
record permutations. It does not assume that the actual entrance geometry
or its later history is stationary or uniform among matchings.

### 2. Construct the reference law and couple its future

For histories in E, use the actual full geometry at t_N as the reference
geometry. For histories outside E, substitute any one fixed full matching.
Sample reference colors from p^K independently of this reference geometry.
This defines a probability law on full colored matchings. The actual law
at t_N and that reference law differ in total variation by at most

    P(E^c)+eta/2 <= eta.                                 (3)

Here total variation is sup_A |mu(A)-rho(A)|, so the maximal-coupling
mismatch probability is that same distance. On E the bound follows by
mixing the conditional estimates. The entire E^c mass costs at most its
probability, whether the lattice has completed during (H_N,t_N] or remains
partially filled. No conditioning on successful formation is applied to
the law being claimed for the actual process.

Couple the initial states at t_N maximally, then use the same transition
randomness whenever they agree. Since the reference is already full, its
future has only the same color exchanges and autonomous plaquette motion;
there are no possible further births or vacant-site slides. Its generator
therefore agrees exactly with the actual full-state generator. Agreement
persists for the whole future path. The total-variation bound eta thus
holds for every finite future time interval, including an interval of
microscopic duration NT with fixed macroscopic T.

This reference construction is for the proof. No extra reset, conditional
rejection, color resampling or matching replacement is performed by the
physical process. The law of the reference geometry may be highly biased.
That is allowed by the uniform-in-matching wave theorem.

### 3. Transfer the quantitative wave bound

For definiteness define the fourteen-component pair field even before
completion. At each black site b let xi_b be the basis vector for the
color of its pair when it is covered, and zero when it is vacant. Put

    Y_N(Q,u) = K^(-1/2) sum_b exp(-i Q.b/N) (xi_b(u)-p).

On full states this is precisely the field in the routed wave theorem.
On every partial or full state its Euclidean norm is at most 2sqrt(K),
since ||xi_b-p||<=2. For fixed Q and 0<=t<=T the matrix propagator
U_Q(t)=exp[-i A(Q)t] has a finite norm bounded independently of N. Therefore

    ||Y_N(Q,t_N+Nt)-U_Q(t)Y_N(Q,t_N)||^2 <= C_(Q,T,p) K

holds deterministically for both processes. On their coupled agreement
event the two errors coincide. Using (3), the actual mean squared error
is at most the reference mean squared error plus C_(Q,T,p) K eta.

The proposed quantitative Euler result, if accepted at its stated premises,
bounds the reference error by C N^(-1/6), uniformly in the reference
geometry law and for fixed bounded nu. Take eta=N^(-4) in (1). Then

    sup_(0<=t<=T) E ||Y_N(Q,t_N+Nt)-U_Q(t)Y_N(Q,t_N)||^2
        <= C N^(-1/6) + C' N^(-1).                      (4)

This is a supremum of expectations. No expectation of a path supremum is
claimed. A fixed finite collection of modes and times transfers in the
same way. Its propagated Gaussian limit follows from the reference result
and the vanishing path-law total-variation difference. The two-physical-
endpoint field has the same conclusion with the previously established
sqrt(2) normalization and its O(N^(-2)) squared endpoint-displacement error.

For orbit-isotropic p the same conditional vector equations apply:

    partial_t X = (gamma rho_A/3) curl Y,
    partial_t Y = -gamma rho_B curl X,
    c = |gamma| sqrt(rho_A rho_B/3).

The scalar speed and four propagating modes require that isotropy condition,
as well as nonzero gamma and Q. The general matrix result uses the stated
full-support p and does not impose that mode count. The static longitudinal
color modes retain positive equilibrium variance. They are not identified
with the matching's geometric Gauss constraint.

### 4. Scope of the improvement

At fixed positive beta,kappa,k0, (1) with eta=N^(-4) is a polynomial
deterministic schedule; the leading displayed worst-case bound scales as
O(N^82/kappa). This exponent is only the consequence of the loose supplied
upper bounds. It is not an observed scaling law or useful numerical estimate.
The microscopic law is unchanged with N; only the time at which it is
observed grows with N. Uniform final-matching selection is unnecessary for
this result and is not asserted for fixed birth rate.

The logical gain is a single conditional statement from empty initialization
to an unconditioned wave-observation window. It removes an assumed formed
initial state, not the supplied microscopic law, colors, clock, recognition
or preparation time. The all-stage filling and quantitative Euler inputs
remain explicit provisional dependencies until their separate checks finish.
There is no quantum preparation, derived Born rule, geometric photon,
Lorentz symmetry, gravity or physical TOE claim here.

## Verification and remaining physics

[The evidence packet](../.claude/science/mobile-record-empty-start-quantitative-waves-20260921/README.md) preserves all three arguments,
the unchanged author sources and outputs, and selective independent checks.
The runner executes six mathematical control groups plus source bookkeeping.
Three mutations test the padded fiber multiplicity, the small-birth-rate
killed estimate and the open-cube path orientation factor. Complete proof
arguments, rather than finite inventories, support the all-volume claims.

The quantitative author N32,l6 fixture tests a local current-containing
footprint; it does not meet the stronger global theorem inequality
2l+5<N/2. The independent N36,l6 controls also exercise that range. Larger
footprint paths are sampled where explicitly stated. Matrix gap comparisons
are numerical; the discrete fiber and path counts and specified rational
killed-operator controls are exact. The scalar clock and deterministic
coupling conclusions require their full conditional proofs.

This result narrows two preparation gaps in a supplied classical model.
It does not derive its rates, clock, exact recognition or continuum structure
from the axioms. It supplies no nonlinear hydrodynamic limit, optimal mixing
or damping exponent, quantum preparation, Born rule, propagating geometric
photon, Lorentz symmetry, gravity, empirical prediction or TOE.
