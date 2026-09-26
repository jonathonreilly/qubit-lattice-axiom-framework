# Independent reconstruction before author-control access

2026-09-21. Selective mathematical review of the supplied quantitative
refinement. This is not frontier authorship or an audit disposition. The new
note has been read completely; the quantitative author checker, its outputs,
and its preserved development failure remain unopened at this boundary.
Complete source identities are in PRE_COMPARISON_SOURCES.json. No production
observables, N256 data, quantum work, or other new candidates were accessed.

## Conclusion at this boundary

The claimed sufficient squared-error bound follows from the checked routed
and moving-geometry hypotheses with the estimates below. I find no
mathematical defect in the new argument at this boundary. The key improvement
is a uniform local inverse gap of order l^2, rather than a fixed-block
existence statement. The loss from overlapping blocks is order l^3. The
phase-coefficient argument removes the earlier unspecified dependence on l.
Constants may depend on the fixed full-support color law, rates, modes and
horizon. Nothing here gives a useful numerical constant or an optimal
exponent.

## 1. Local comparison with constants

Let L=2l+1 and let C contain the matched pairs meeting the embedded all-site
cube. Every pair covers at most two sites, so m=|C|>=L^3/2. Map every cube
site to its pair. The image of its connected edge graph is connected on C.
Choose one distinct representative inside the cube for each pair.

For coordinate-order monotone routes between all ordered cube sites, an
undirected edge in coordinate i, after a sites of that coordinate, is used
2a(L-a)L^2 times. In coordinates before i the path has already reached the
destination coordinate, leaving the source coordinate free; after i the
source coordinate is fixed by the edge and the destination is free. These
are the two L factors. The two directions give the factor 2. Thus the load
is at most L^4/2 and every route has length at most 3(L-1).

The selected representative routes for unordered pair endpoints are a
subset of these ordered routes. Contract matching edges, erase any loops,
and retain a simple path. Erasure introduces no new edge. A contracted edge
has at most two physical representatives: black endpoint of the first pair
to white endpoint of the second, or the reverse pairing. Bipartiteness is
essential to that multiplicity statement. Consequently a contracted edge
has reference-path load at most L^4.

A simple path of length d implements its endpoint transposition by the
forward word followed by the reverse word with the last edge omitted. This
has length 2d-1<=6L and uses any edge at most twice. Intermediate colors are
restored; equal colors simply give zero increments. With the unit-rate form
D=(1/2)sum_edges E[(f^e-f)^2], path Cauchy--Schwarz and invariance of the
uniform count sector under each intermediate transposition give

    D_all <= (6L)(2L^4) D_C = 12L^5 D_C.

The previously proved permutation inequality Var<=2D_all/m therefore yields

    Var <= 48L^2 D_C <= (96L^2/k0) D_actual.

The last step uses one actual symmetric channel of rate at least k0/2 per
included simple edge. Exterior colors and C counts can be conditioned on;
all internal transpositions preserve that conditional uniform law. No
invariance of a context-truncated nonreversible block process is assumed.

## 2. Replacement powers and exact centering

For the four-site current, define h_u by subtracting its conditional mean
on the footprint counts. It is count-orthogonal and uniformly bounded. If
G=K^(-1/2)sum_u a_u h_u with bounded deterministic coefficients, conditional
Poincare bounds each pairing with a test function by C sqrt(A_l D_C(f)).
Cauchy--Schwarz over the K centers then gives

    |<G,f>| <= C sqrt(A_l sum_u D_Cu(f))
             <= C sqrt(A_l l^3 D_actual(f)).

Each actual edge occurs in at most C l^3 blocks. The variational definition
of the negative norm gives ||G||_-1^2<=C A_l l^3<=C l^5. Real and imaginary
parts give the complex-observable statement with another fixed constant.
The inherited stationary forward/backward bound on a physical interval Nt,
including the outside factor 1/N for Euler-time integration, gives
C T l^5/N. The checked conditional-history estimate gives this same bound
for autonomous moving geometry, without a factor for the number of switches.
This relies on the conditional product color law and its permutation
isometries, not on a stationary geometric law.

Given m counts, the four distinct current sites sample without replacement.
Coupling four draws gives an O(1/m) difference from independent draws.
The independent current mean is a fixed-degree polynomial J. Its Taylor
remainder at p has squared expectation O(1/m^2), since the empirical fourth
moment is O(1/m^2). Thus

    hat j=J(p)+A(q_C-p)+W,  E||W||^2<=C/m^2.

Here E W=0 is exact: E hat j=J(p) and E q_C=p for each fixed matching
footprint under iid colors. It does not assert that the separate
without-replacement correction and Taylor remainder each have zero mean.
Disjoint footprints are independent, so the overlap count makes the
normalized W sum have variance at most C l^3 l^-6=C l^-3.

The ordinary black cube has m_B=(L^3+(-1)^l)/2 sites, all represented in C.
The additional pairs have their black endpoint outside and white endpoint
inside; their number is O(L^2). Write m_C=m_B+e. The exact squared coefficient
norm of the difference of the two centered averages is

    e/m_C^2 + m_B(1/m_C-1/m_B)^2 = 1/m_B-1/m_C = O(l^-4).

For colors its variance is this coefficient norm times the fixed covariance
matrix. A bounded black-to-black displacement, including one chosen by the
matching, changes only O(l^2) sites and obeys the same estimate. Summing with
bounded deterministic geometric weights and using overlap gives C/l. The
four-current footprint is included for the note's l>=6 and embedding range.

## 3. Phase and incoming-direction cancellation

An important inherited step is done before any approximation: constant
current terms cancel exactly in sum_u N[phi(q_delta u)-phi(u)]J_delta(p),
because q_delta is a permutation. The original routed proof states this
explicitly. Bounding those uncentered constants by the phase remainder would
not be legitimate and could introduce a volume factor. The new argument
correctly continues the centered-field calculation of that proof.

For the displacement a=delta-d_(q_delta u), |a|<=2, the elementary bound
|exp(-is)-1+is|<=s^2/2 gives

    |N[phi(q_delta u)-phi(u)]+i phi(u) Q.a| <= 2|Q|^2/N.

For ordinary translated black blocks each v belongs to exactly m_B centers.
Consequently the coefficient of z_v after exchanging sums has magnitude
at most sup|b_u|. For C blocks there are at most L^3 centers containing a
given pair and m_C>=L^3/2, so the bound can, conservatively, be 2sup|b_u|.
Independent centered colors then give a normalized variance O(sup|b|^2),
uniformly in l. The same argument applies componentwise to bounded matrices.
All coefficients used here are deterministic conditional on the geometry;
the independence inference is not a claim for arbitrary color-dependent
random coefficients.

The ordinary-block Fourier multiplier is exact by translation invariance:
the coefficient at v is phi(v) times the average of exp(i Q.r/N) over black
offsets r. Its distance from one is at most sqrt(3)|Q|l/N. This gives squared
error C l^2/N^2, without needing symmetry or a stronger Taylor estimate.

For incoming d_v terms, reindex u=q_delta^-1(v) and subtract the common
phi(v)[q_l(v)-p]. The common term vanishes by sum_delta A_delta=0. The
remaining shift in the block has variance C/l after summation; the phase
change has coefficient norm O(1/N), hence squared error C/N^2. This permits
arbitrary matchings, not only periodic examples or an equilibrium matching.

## 4. Integrated errors and propagation

All preceding variances are uniform at a fixed time conditional on any
autonomous geometry history, because colors retain their homogeneous
product law under that conditioning. Time Cauchy--Schwarz gives uniform
second moments of the time integrals without assuming independence across
times. The negative-norm term uses the stronger energy estimate already
checked. Together the integrated routed residual has squared expectation

    C_T [l^5/N + l^-3 + l^-1 + l^2/N^2 + N^-2].

The routed martingale bracket is O(T/N). For the moving extension its extra
drift estimate is O(T nu^2 |Q|^2/(k0 N)), and the joint-process martingale
adds only O(T/N). The conditional argument is not a claim that the actual
joint martingale remains a martingale after revealing future geometry.

Let delta denote the right-hand bound C_T[l^5/N+1/l+l^2/N^2+1/N]. The exact
integral equation for E(t) has forcing M(t)+R(t) whose fixed-time second
moment is at most delta. With a fixed finite matrix A,

    E||E(t)||^2 <= C delta + C ||A||^2 T int_0^t E||E(s)||^2 ds.

Gronwall gives sup_t E||E(t)||^2<=C_(A,T) delta. This does not use a
derivative of R, normality of A, or an expectation of a time supremum.
Taking l=floor(N^(1/6)) balances l^5/N and 1/l. Its lower-radius and
embedding requirements hold for sufficiently large even N. The other
terms are smaller. This proves the claimed squared rate N^-1/6 and the
norm rate N^-1/12 under the inherited hypotheses.

The checked preparation theorem supplies a path-law total variation error
epsilon_N=N^-4. The residual squared is bounded by C_T K on every path, so
expectations differ by O(K epsilon_N)=O(N^-1). This includes the stipulated
post-completion waiting period; no uniform bound for the preceding random
completion time has been added. For endpoint-normalized fields, the
within-pair phase discrepancy has conditional squared expectation O(N^-2)
under product colors. Applying the same transfer can add O(N^-1).

## 5. Independent controls and their limits

The independently written independent_check.py imports no author code.
Its first execution passed with empty stderr; the full stdout and receipt
are preserved. Complete numeric output was read, not inferred from a PASS
total. It checks:

* All ordered open-cube routes for L=3,5,7: 729, 15625 and 117649 ordered
  pairs, all 54, 300 and 882 physical-edge loads exactly equal (3).
* Boundary-crossing local footprints in N16, l2 columnar/irregular
  matchings: all 2775 and 3003 representative endpoint words. These test
  the geometric sublemma only, not the l>=6 current application.
* Valid l6, N36 columnar/irregular footprints: connected 1183/1181 pair
  graphs, physical multiplicity at most two, 6000 deterministically
  preselected endpoint words in each. These are sampled word inventories,
  not exhaustive congestion verification for that size. They also check
  exact boundary-average coefficient norms.
* Every ordinary and irregular block membership in an N16 fixture with
  l2; all six route directions and a non-axis Fourier mode. Membership,
  bounded coefficients, the exact convolution multiplier and the Taylor
  remainder hold numerically. This is a coefficient sublemma control;
  the all-N inequalities above are analytic.
* Exact Fraction binomial calculations for m=4,7,13,31,64, p=1/3. For the
  scalar pair U statistic, its centered nonlinear remainder has variance
  2p^2(1-p)^2/[m(m-1)], and the empirical fourth moment is
  3p^2(1-p)^2/m^2+p(1-p)(1-6p(1-p))/m^3. These control the sampling and
  moment step rather than substitute a different record model.
* A nonnormal two-dimensional propagation matrix with bounded integrated
  forcing at frequencies 1,17,203. The exact augmented matrix exponential
  satisfies the integral equation to below 8e-17 and the conservative
  fixed-time Gronwall bound. This checks the absence of an unjustified
  forcing-derivative or matrix-normality requirement.

There were no failed executions in this independent phase. No finite test
proves the all-N result or supplies its unspecified constant. Full-support
p, bounded fixed rates and modes, fixed T, conditional product colors and
the specified autonomous moving geometry remain necessary premises. The
bound has no claim uniform at a density boundary, for modes growing with N,
for a growing horizon or geometry rate, or for a nonproduct color entrance.
It does not identify a physical field or the static geometric Gauss field
with the color fields.
