# A slow-formation limit selects uniform full geometric matchings

2026-09-21. Root conditional theorem for the supplied geometric-partner
process. This is a finite-graph, ordered rate limit, not a mixing-rate theorem,
a fixed-rate thermodynamic limit, or a physical quantum/Coulomb/wave claim.
The underlying antipodal-content encoding and its quantum comparison gap
remain exactly those in GEOMETRIC_PARTNER_RECORD_FORMATION.md.

## A consequential distinction at finite rates

At positive finite birth rate, filling does not in general select the uniform
law on full matchings. For the reflecting eight-vertex cube with kappa=1,
nu=0 and birth rate b=beta/kappa, exact absorption gives

    P(first full matching is columnar)
      =(6 b^3+77 b^2+308 b+308)
          /[7(b+6)(3 b^2+19 b+22)].                       (1)

There are three columnar and six other full matchings. Their uniform law
would give probability 1/3. Formula (1) instead gives 699/2156 at b=1,
has limit 1/3 as b decreases to zero, and limit 2/7 as b tends to infinity.
The calculation is a full finite-state harmonic boundary problem, not an
inference from the large-volume formation screen. The fast-rate limit still
allows motion between successive birth bursts; it is not beta>0,kappa=0,
which can jam. The parameter endpoints must not be conflated.

## The last two vacancies suffice for uniform selection in the slow limit

Let G be a finite connected k-regular bipartite simple graph, with equally
sized vertex classes L,R, |L|=|R|=K, k>0. Use the geometric partner births
at rate beta per vacant edge and the reversible length-two slides at rate
kappa>0. Any additional symmetric matching-preserving conservative channels
may be included; the plaquette rotations are one example. Their rates and
kappa stay fixed as beta decreases to zero.

The geometric chain restricted to matchings with K-1 edges, with births
temporarily suppressed, is irreducible under the slides alone. Its stationary
law is therefore uniform over all such near-perfect matchings. The following
proof makes the graph condition and both vacancy roles explicit.

### Vacancy reachability

First, connected regularity gives a strict Hall inequality

    |N(S)|>|S| for every nonempty proper S subset L.        (2)

Indeed k|S| edges enter N(S), so |N(S)|>=|S|. Equality would use every edge
incident to N(S), separating S union N(S) as a component, contrary to
connectedness. The same argument holds with L and R exchanged. Existence
of a perfect matching follows from the non-strict Hall inequality (or from
the usual elementary augmenting-path construction); the cubic torus also
has an explicit columnar one.

For a near-perfect M let l0 in L and r0 in R be its two vacancies. Keep r0
fixed. Make a directed graph on L: l -> l' when l is adjacent to a matched
r != r0 whose M partner is l'. A directed path from l0 can be executed by
slides, moving the L vacancy along that path while r0 stays fixed.

If S is the set reachable from l0 in this directed graph, every neighbor
of S other than r0 is matched into S minus {l0}. Thus |N(S)|<=|S|. Inequality
(2) excludes any proper S, so every L vertex is reachable. A shortest
directed path has no repeated L vertex; its matched R vertices are also
distinct, so it really is a sequence of legal vacancy moves. Interchanging
L and R proves that the R vacancy can be positioned arbitrarily while the
L vacancy stays fixed.

### Changing alternating cycles without leaving two vacancies

Take two near-perfect matchings M,M'. Position both vacancies of M at those
of M' using the preceding moves. The symmetric difference then consists of
disjoint even alternating cycles. To flip one such cycle C, take a shortest
M-alternating vacancy path from the L vacancy to any L vertex of C. The
path meets C for the first time in its last matched R-L edge; all of its
earlier vertices are outside C.

Slide along the path. The vacancy now sits on C, and the entering R vertex
is matched to the preceding external L vertex. Continue the vacancy around
C along its other alternating edges. The final step through that entering
R vertex returns the vacancy to the external path and completes the flip
of C. Retrace the earlier path in reverse, restoring every matching edge
outside C and the original vacancy positions. Every operation is a legal
length-two slide. Repeat for the remaining cycles.

This proves geometric irreducibility, including cycles that wind around a
periodic graph. It does not assert that every identity-labeled or continuously
marked configuration communicates: permanence can retain information invisible
to the geometric projection. Uniformity here and below concerns matchings.

## Rare killing gives the exact limiting full-matching law

Write Omega for the finite set of near-perfect matchings and F for the set
of perfect matchings. Let S be the conservative generator on Omega, and
pi its uniform invariant law. Define h(M)=1 if the two vacancies are adjacent
and zero otherwise. On a simple graph there is at most one birth edge at
this level. For a specified full matching F0 define a_F0(M)=1 when that
birth completes precisely F0, and zero otherwise.

Let u_beta(M) be the probability that the next birth completes F0, starting
from M. It is the unique bounded solution of the killed-chain equation

    [-S+beta diag(h)] u_beta = beta a_F0.                 (3)

The filling theorem ensures that this next birth occurs almost surely.
The vector u_beta lies in [0,1]^Omega. Along any beta->0 subsequence, take
a convergent sub-subsequence. Equation (3) gives S u_0=0, so irreducibility
makes u_0 a constant c. Multiplying (3) by pi gives, at every positive beta,

    pi(h u_beta)=pi(a_F0).

Consequently c=pi(a_F0)/pi(h). Deleting any of the K edges of F0 gives a
distinct predecessor in Omega, each with one enabled completion. Thus

    pi(a_F0)=K/|Omega|,
    pi(h)=K |F|/|Omega|,
    c=1/|F|.                                             (4)

All subsequential limits agree, and Omega is finite. Convergence is uniform
over its starting state. The process from any partial matching reaches the
near-perfect level before filling, and the strong Markov property applies
there. Its entrance distribution may depend on beta and all earlier formation;
uniform convergence removes that dependence. Therefore

    Law(first full matching) -> Uniform(F), beta->0       (5)

at each fixed finite graph, with fixed positive kappa. No equilibration
assumption at every earlier pair count is needed. This is a proved finite
state separation of rates, not a claim that the small value beta=0.1 in a
numerical screen is already an equilibrium limit.

On every even cubic torus N>=4 the graph is connected, simple, bipartite and
6-regular, so (5) applies. Optional symmetric plaquette rotations after
filling preserve Uniform(F), even when individual winding sectors do not
communicate. Total-variation contraction makes any later observation time
at fixed N no worse than the initial discrepancy from that uniform law.
There is still no estimate uniform in N: taking beta->0 first and then
N->infinity is an ordered limit with an explicit clock dependence.

## Scope for the campaign

This gives a local irreversible-formation route to a specified correlated
full-matching ensemble in a controlled finite-volume slow-birth limit.
Its microscopic geometric Gauss identity is exact after filling. It no
longer requires imposing that geometric ensemble through a global Fourier
preparation. Formation at a fixed positive rate remains a different law;
equation (1) is an explicit warning against suppressing that distinction.

Neither the infrared behavior of Uniform(F) nor a propagating field theory
has been proved here. With nu=0 full configurations freeze; with the supplied
symmetric flips their geometric dynamics is reversible. The usual quantum
dimer theory needs additional coherent Hilbert-space and Hamiltonian input
and cannot be identified with these classical records. The exact-content
comparison, rotation bridge, choice of events and separation of rates also
remain named supplied structure. This is progress on state formation under
those choices, not a derivation of a physical TOE.
