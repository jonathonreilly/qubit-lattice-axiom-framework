---
claim_id: mobile_records_geometric_formation_selection_and_clock_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "A supplied classical process pairs permanent antipodal projector contents using their positions. Nearest-neighbor whole-record slides allow geometric turns and almost-sure finite-time filling with positive paired births. On finite connected simple graphs admitting a perfect matching, the two-vacancy geometric slide chain is connected, its rare-birth full exit is uniform, and its scaled final-pair clock is exponential independently of that exit. A trace and path comparison imports a matching-chain conductance theorem to bound relaxation in terms of matching counts; with a named monomer theorem it gives an explicit sufficient polynomial slow-birth schedule on even cubic tori in dimension above two. No fixed-rate thermodynamic law, total-growth upper clock bound, operational quantum mechanism, transverse wave, or physical TOE is established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mobile_records_geometric_formation_selection_and_clock_2026_09_21.py
---

# Local record formation, geometric relaxation, and the final-pair clock

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

This specified model allows an old record to leave a site and a later record
to form there while every old content remains unchanged. The partner direction
comes from the current positions, so it can turn. That distinction permits a
finite-graph filling proof and a controlled formation route to the uniform
geometric matching law.

The construction is not a derivation from
[the minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). Pure projector contents,
exact antipodal-content recognition, the spatial rotation action, paired
births and the transition rates are supplied. Exact recognition of arbitrary
unknown qubit states has no operational implementation here. Uniformity
concerns the geometric projection, not immutable marked-state ergodicity.

The finite-graph rare-birth limit holds on every connected simple graph
admitting a perfect matching, including irregular graphs with odd cycles or
bridges. The final part bounds relaxation quantitatively and supplies a
simultaneous volume/slow-formation limit on even cubic tori in dimension above
two: with K record pairs, (beta/kappa) K^12 tending to zero suffices. This is
a conservative proof bound, not a measured exponent or a practical timescale.
Finite positive rates already give nonuniform filling on the eight-vertex
cube. All clock conclusions concern the final two vacancies; they do not
bound the total empty-start formation time.

All five arguments received separate-context reconstruction and decisive
checks before comparison with their author checkers. The external matching
and monomer theorems are imported with their statements, normalizations and
application hypotheses checked; their complete published proofs were not
independently reconstructed. A post-filling observation-time qualification
and one numerical fixture-name correction are preserved with their original
sources, results and selective review records.

The five arguments below are reproduced completely. The later parts extend
the earlier part's results under their additional hypotheses. Historical
source-status sentences are preserved; the evidence packet separately records
which selective independent checks are complete. Publication assembly is an
author verification, distinct from independent mathematical reconstruction.

## Immutable contents with turning geometric partners

2026-09-21. Root proposed construction and conditional finite-volume theorem.
This changes the earlier direction-tag encoding: a dimer's spatial direction
is derived from its two positions, while each record's content stays fixed.
The construction is a classical stochastic process on specified M2-presented
possibilities. It is not an implementation by quantum instruments, a retained
axiom consequence, a Coulomb-phase theorem, or a wave model.

### Contents, domain, and supplied symmetry bridge

A present record contains the pure rank-one projector

    P_n=(I+n.sigma)/2, n in S^2.

Two partners have antipodal contents P_n,P_(-n). The supplied state domain
consists of disjoint nearest-neighbor pairs, with no antipodal coincidence
between records in different pairs. Thus every present record has exactly
one antipodal record anywhere in the configuration, and it is a nearest
neighbor. The partner relation is reconstructible from these contents and
positions; it is not an extra changing direction tag or a hidden pairing
register. Vacancies carry no readout. Record identities only track permanence.

We explicitly supply the usual action P_n -> P_(R n) of a proper cubic
rotation R. Identifying the Bloch-vector rotation action with spatial
rotations, choosing pure projectors, and exact recognition of antipodal
contents are model choices, not consequences of the bare one-site algebra.
In particular, perfectly comparing arbitrary unknown pure-qubit contents
is not an operation already supplied by ordinary quantum theory.

At a finite volume there are finitely many occupied keys; on Z^3 there can
be countably many. A fresh continuously drawn n almost surely coincides
with none of their antipodal classes. No nonlocal rejection test is used.
The specified domain is preserved almost surely over a countable history.
The finite-volume geometric process below is sufficient for the theorem;
no infinite-volume existence or filling theorem is imported here.

### One local rule for formation, with varying nearest-neighbor odds

Fix beta>0 and 0<|epsilon|<1. On each unoriented vacant nearest-neighbor
edge, temporarily write its endpoints as (x,x+d). A birth of two new records
with contents (P_n,P_(-n)) has rate density

    beta f_d(n) dOmega(n),
    f_d(n)=[1+epsilon n.d]/(4 pi).                         (1)

Here d is a unit coordinate vector. The density is positive and integrates
to one, so the total edge rate is beta. Reversing the temporary order sends
(d,n) to (-d,-n), leaving f_d(n) unchanged. Thus no preferred endpoint is
part of the rule. Existing records are neither deleted nor overwritten.

Let D_x be the directions from a vacant x to its vacant nearest neighbors,
and r_x=|D_x|. If r_x>0, the conditional density of the content formed at x,
given that a birth occurs there, is exactly

    p_x(n)=[1+epsilon n.(sum_(d in D_x) d)/r_x]/(4 pi).    (2)

Every incident edge has the same integrated clock beta, including when x
is the second endpoint in a temporary ordering. Formula (2) depends only
on the six nearest-neighbor occupancy conditions. It varies with them:
one available neighbor in +e_1 gives f_(e_1), whereas all six give the
uniform spherical density. If r_x=0, set the unused conditional rule to
the uniform density; the actual formation rate there is zero. This is a
supplied example of varying nearest-neighbor formation odds, not a derived
Born law or a selection of the clock or epsilon by the axioms.

The two newborn contents are correlated. Their joint preparation is stated
as a classical draw followed by record formation; no claim is made that
an unknown parent's quantum state was read or copied. Exact specified n's
have zero singleton probability. Concrete marked histories illustrate
supported outcomes, while positive-probability statements below concern
the geometric histories after the marks have been integrated out.

### Whole-record motion, including turns

Fix kappa>0. If v0,v1 are partners and v2 is a vacant neighbor of v1, perform

    record at v0 -> v1,   record at v1 -> v2              (3)

at rate kappa for that ordered length-two path. The two records remain
antipodal and adjacent, and each takes exactly one nearest-neighbor step.
The new vacancy is v0. A turn is permitted: v0-v1 and v1-v2 need not be
parallel. The reverse ordered path (v2,v1,v0) restores both identities,
so the conservative channel and its reverse have the same rate. Its
acceptance reads only the three sites and their supplied partner contents.
Distinct keys ensure that the other pairs remain valid.

For example, a pair at 0,e_1 can move to e_1,2e_1. A new pair can then form
on -e_1,0. Site 0 has formed twice, while both old contents survive. An
additional turn can change the original pair's geometric direction without
changing either record's projector.

An optional full-density move uses a unit plaquette whose two opposite
edges are pairs. Rotate its four records by one corner, clockwise or
counterclockwise, each at rate nu>=0. Every record takes one nearest-neighbor
step; both old antipodal partnerships survive on the other two edges.
Inverse rotations have equal rates. The projected geometric dimer flip
has rate 2 nu because the two identity-level channels have the same
unmarked target. This channel count must not be silently divided by two.

All edges, ordered paths, plaquettes and both senses are included uniformly.
Translation and proper cubic rotations permute the event family, and (1)
is covariant under the supplied Bloch/spatial action. The rates do not depend
on a chosen columnar reference or a global coordinate parity.

### Every partial matching can gain another pair

Let G be any finite simple graph with a perfect matching P. Apply births
on vacant edges and the length-two slides (3) on G. Every partial matching
M that is not full has a finite legal sequence of slides followed by a birth.

Proof: in the symmetric difference M triangle P, remove their common edges.
Every remaining vertex has degree at most two. Each vertex unmatched by M
is the endpoint of an alternating path, because P matches every vertex.
Such a path has distinct vertices v0,...,v_(2ell+1), both endpoints vacant
in M, with P edges (v0,v1),(v2,v3),... and M edges (v1,v2),(v3,v4),... .
Slide the pair (v2,v1) into the vacancy v0, leaving v2 vacant. Repeat along
the path. After ell slides the two endpoints v_(2ell),v_(2ell+1) are vacant
and adjacent. One birth adds a pair. No existing partner key or individual
content changed, and every moved record took one graph edge per event.
The number of slides plus the birth is at most |G|/2. This proves the claim.

The perfect matching is only a proof device. On an even periodic N^3 cubic
torus, N>=4, a columnar matching demonstrates that it exists; the actual
law does not select that matching or a columnar direction.

For the geometric projection, all integrated birth rates are beta, all
slide channels have rate kappa, and the optional plaquette flip has rate
2 nu. This is a finite-state continuous-time Markov chain with finite rates.
Pair number never decreases. If a closed communicating class contained a
nonfull matching, the preceding positive-rate path would exit its fixed
pair-number level, a contradiction. All nonfull states are therefore
transient. Full packing occurs almost surely in finite time, with finite
expectation at each fixed graph and positive beta,kappa.

This proof gives no useful size-uniform filling time, density scaling,
infinite-lattice filling result, or mixing estimate. It remains true at
nu=0: plaquette rotations are useful for full-density motion, not required
for the filling argument. At kappa=0 the argument fails and ordinary
irreversible dimer deposition can jam; the positive slide hypothesis is
essential. Different final full matchings need not communicate by the
optional plaquette moves.

Starting empty on a translation-invariant finite torus, the expected total
number of records formed at any fixed site is exactly one by symmetry and
full packing. This is compatible with individual sites forming repeatedly.
Mobility redistributes capacity; it does not increase the final total V.

### Geometric Gauss and the remaining state/dynamics questions

Let n_i(x) indicate the geometric matching edge {x,x+e_i}, independent of
which partner content is at either endpoint. With sigma_x=(-1)^(x1+x2+x3),
the established staggered dimer readout is

    B_i(x)=sigma_x[n_i(x)-1/6],
    sum_i [B_i(x)-B_i(x-e_i)]=-sigma_x 1_(x vacant).       (4)

It is a derived geometric field from a collection of records, not a value
newly written into one record. The old finite-volume identity still holds,
and full packing now removes its vacancy charges almost surely in finite
volume. Translating the parity convention changes the sign convention of B;
it does not change any rate or create a preferred physical site.

The orientation counts M_i are now geometric quantities, not immutable
content counts. A turning slide can change them. Thus the earlier all-odd
direction-count obstruction does not apply to this encoding. This does not
invalidate that earlier theorem: it explicitly depended on locked direction
tags. The original counterexamples remain useful tests of that hypothesis.

Without births, the geometric slide/flip chain is reversible with respect
to uniform matchings in each communicating component at fixed pair number.
At full packing only the optional flips remain. This supplies no oscillatory
Euler wave result, no irreducibility across winding or other sectors, and
no claim that formation selects the unrestricted uniform dimer ensemble.
The standard cubic-dimer Coulomb-phase literature motivates further study;
its correlation or quantum-dynamics conclusions do not transfer merely
because (4) is the same readout.

The constructive gain is narrower and concrete: local paired formation,
unchanged M2-presented contents, site reuse, geometric turns, and guaranteed
finite-volume filling coexist under one specified rule. A justified quantum
instrument/readout bridge, the correlated full-state selection, transverse
propagation, and a reason to select this rule remain open.

## Uniform selection in an ordered slow-formation limit

2026-09-21. Root conditional theorem for the supplied geometric-partner
process. This is a finite-graph, ordered rate limit, not a mixing-rate theorem,
a fixed-rate thermodynamic limit, or a physical quantum/Coulomb/wave claim.
The underlying antipodal-content encoding and its quantum comparison gap
remain exactly those in GEOMETRIC_PARTNER_RECORD_FORMATION.md.

### A consequential distinction at finite rates

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

### The last two vacancies suffice for uniform selection in the slow limit

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

#### Vacancy reachability

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

#### Changing alternating cycles without leaving two vacancies

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

### Rare killing gives the exact limiting full-matching law

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
over its starting state. The process from any initially nonfull matching
reaches the near-perfect level before filling, and the strong Markov property applies
there. Its entrance distribution may depend on beta and all earlier formation;
uniform convergence removes that dependence. Therefore

    Law(first full matching) -> Uniform(F), beta->0       (5)

at each fixed finite graph, starting nonfull, with fixed positive kappa.
An already full initial state is excluded: no further births would sample it.
No equilibration
assumption at every earlier pair count is needed. This is a proved finite
state separation of rates, not a claim that the small value beta=0.1 in a
numerical screen is already an equilibrium limit.

On every even cubic torus N>=4 the graph is connected, simple, bipartite and
6-regular, so (5) applies. Optional symmetric plaquette rotations after
filling preserve Uniform(F), even when individual winding sectors do not
communicate. At any common deterministic elapsed time after first filling,
or after an independent random delay, total-variation contraction makes the
discrepancy from that uniform law no greater than its initial value. This
does not cover a state-dependent observation or stopping rule.
There is still no estimate uniform in N: taking beta->0 first and then
N->infinity is an ordered limit with an explicit clock dependence.

### Scope for the campaign

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

## The final-pair clock and an external monomer theorem

2026-09-21. Root conditional derivation, pending selective independent check.
The process, classical antipodal-key resource, graph hypotheses and finite
volume rate limit are those in GEOMETRIC_PARTNER_RECORD_FORMATION.md and
GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md. This note concerns the elapsed
time between first reaching two vacancies and filling, not the whole growth
time from empty. An existing equilibrium theorem is imported explicitly;
it is not rederived or presented as a new result about dimers.

### A finite-state clock law, including its exit state

Let Omega be the near-perfect geometric matchings on a finite connected
regular bipartite simple graph with 2K vertices. The slide generator S is
irreducible and symmetric; kappa>0 is fixed, and fixed additional symmetric
conservative rates are allowed. Let pi be uniform on Omega. Write h(M)=1
when the two vacant vertices are adjacent and 0 otherwise, H=diag(h), and
p=pi(h)>0. For each full matching F, a_F(M) indicates that the unique birth
at M completes F. Put tau for this next-birth waiting time.

For s>=0, the joint Laplace transform

    u_(beta,s,F)(M)=E_M[exp(-s beta tau) 1_(exit=F)]

solves

    [-S+beta(H+sI)] u_(beta,s,F)=beta a_F.              (1)

The bounded vector u takes values in [0,1]. Along any beta->0 sequence, every
convergent subsequence solves S u_0=0, hence is constant, by irreducibility.
Multiply (1) by pi before taking the limit to obtain

    u_(beta,s,F)(M) -> pi(a_F)/(p+s)
                     = (1/|Fset|) p/(p+s).             (2)

Here pi(a_F)=K/|Omega| and p=K|Fset|/|Omega| by the edge-deletion count.
The convergence is uniform in M because Omega is finite. Thus beta tau
converges in law to an exponential variable of rate p, and the full matching
converges jointly to an independent uniform member of Fset. This holds for
an entrance distribution at the two-vacancy level that itself depends on
beta. It does not posit equilibration at earlier pair counts.

### Mean waiting time: do not infer moments from weak convergence alone

Let L=-S, let P project onto constant functions in L2(pi), and Q=I-P.
For |Omega|>1, L restricted to the centered subspace has strictly positive
smallest eigenvalue. Define the centered inverse

    R_beta = [Q L Q + beta Q H Q]^{-1} on ran Q,
    q=h-p 1,    C_beta=<q,R_beta q>_pi.

R_beta stays bounded as beta decreases to zero. The unique mean hitting
time t_beta solves (L+beta H)t_beta=1. Decompose t_beta=c 1+v, pi(v)=0.
The centered and constant equations give exactly

    v=-beta c R_beta q,
    c=1/[beta(p-beta C_beta)],
    t_beta(M)=[1-beta(R_beta q)(M)]
                   /[beta(p-beta C_beta)].              (3)

The denominator is positive: L+beta H is positive definite, and its Schur
complement on constants is beta(p-beta C_beta)>0. Consequently, at each
fixed graph,

    beta E_M tau -> 1/p=|Omega|/[K |Fset|],             (4)

uniformly over starts. This proves mean convergence separately. A one-state
near-perfect chain has h=1 and the assertion is directly exponential; no
centered spectral gap is needed in that case. Since C_beta>=0, the mean
from pi is at least 1/(beta p); finite-rate persistence of the local birth
hazard increases that stationary-start mean. No such one-sided bound for
every individual start is asserted.

The O(1) correction at fixed graph can also be read from (3): with R_0 the
centered inverse of L and C_0=<q,R_0 q>,

    E_M tau=1/(beta p)+C_0/p^2-(R_0 q)(M)/p+O(beta).   (5)

The constants in this expansion may deteriorate with volume. In particular,
beta_N->0 on a sequence of growing systems is not enough without control
of the relevant conservative relaxation. None of (2)--(5) supplies that
control for cubic tori.

### The counting ratio is exactly a monomer susceptibility

Now specialize to the even periodic d-dimensional cubic torus of side N>=4,
volume V=N^d and K=V/2. Let Z_N be its number of full matchings, and let
Z_N(u,v) count matchings with precisely u and v vacant, where u,v lie on
opposite bipartite sublattices. Define

    Xi_N(v)=Z_N(0,v)/Z_N,
    chi_N=sum_(v odd) Xi_N(v).

Counting a near-perfect matching once by its unique pair of vacant vertices,
then using translation invariance, gives

    |Omega|=K Z_N chi_N,
    p_N=1/chi_N,
    lim_(beta->0) beta E_M tau=chi_N.                  (6)

Every neighbor has Xi_N(e_i)=1/(2d): adding the missing edge bijects its
two-vacancy matchings with full matchings containing that edge, whose
uniform occupation probability is1/(2d). There are 2d such neighbors, so
the adjacent-pair weight in the sum is exactly 1, consistent with p_N=1/chi_N.
This identifies the leading formation clock with a precise equilibrium
counting observable; it does not assume a continuum effective action.

### Explicit external input in dimensions greater than two

Use Lorenzo Taggi, [arXiv:1909.06558v3](https://arxiv.org/html/1909.06558v3),
Theorem 2.1, Eq. (2.3), and the bound Eq. (2.5). His even periodic torus and
unweighted monomer counting ratio coincide with the definitions above.
Writing r_d for the expected number of strictly positive-time returns of
simple random walk on Z^d, these results give, for d>2,

    liminf_(N even->infinity) (1/K) chi_N
                 >= [1-r_d/2]/(2d),
    Xi_N(v)<=1/(2d).                                  (7)

For d=3, the paper records 0.51<r_3<0.52, so the lower constant is positive.
The theorem also bounds insertion ratios away from zero at odd axis
separations up to an N-proportional distance (Eq. (2.4)), with the stated
margin and sufficiently large even N. This is an equilibrium monomer
nonconfinement statement; it is not a dipolar dimer-correlation, Gaussian
field, dynamical mixing or photon theorem.

Combining the exact counting identity (6) with (7) yields the conditional
formation consequence

    [1-r_d/2]/(4d)
       <=liminf_(N even->infinity) chi_N/V
       <=limsup_(N even->infinity) chi_N/V
       <=1/(4d).                                      (8)

In particular, in 3D the mean final-pair time has a coefficient between
[1-r_3/2]/12 and1/12 when beta tends to zero first and time is measured in
units V/beta. This is an ordered-limit bound, not a fitted numerical value
for a fixed positive beta. It makes no claim that chi_N/V has a limit.
The full growth time is at least the last-pair time, but(8) is not an upper
bound for the complete empty-start growth process.

For the normalized two-vacancy equilibrium law, conditional on one vacancy
being at0, the other vacancy has probability Xi_N(v)/chi_N at odd v. Equation
(7) therefore also connects the late formation stage to spatially separated
vacancies. This conditional equilibrium law is the conservative near-perfect
law; it is not claimed to hold at every instant of a finite-rate trajectory.

### Scientific scope

The permanent-record process now has a controlled route to uniform full
geometries and a quantitative late formation law tied to a rigorously studied
constrained ensemble. The exact geometric divergence charges are vacancies,
and births remove them in opposite-sublattice pairs. None of this identifies
them as physical electric charges, supplies the missing exact-content
recognition operation on unknown qubits, or gives transverse propagation.
The fixed-rate large-volume screen tests a different order of limits and
must remain labeled numerical. No inference from its apparent infrared
power to the hypotheses or conclusions of Taggi's theorem is used here.

## Two-vacancy connectivity beyond bipartite regular graphs

2026-09-21. Root candidate proof, awaiting exact controls and selective
independent reconstruction. This strengthens the geometric projection of the
supplied permanent-record process; it does not strengthen the operational
meaning of its classical antipodal keys. No new local event is added.

### Statement and legal elementary move

Let G be a finite connected simple graph on 2K vertices, with at least one
perfect matching. Let Omega consist of its matchings with K-1 edges. A slide
replaces an edge {b,c} by {a,b} when a is vacant and {a,b} is an edge of G.
In the actual record process it moves the old record at c to b and the old
record at b to a, leaving c vacant. Both immutable partner contents move one
graph edge; the reverse slide restores them. Every legal slide has positive
rate kappa and its geometric inverse has the same rate.

**Claim.** The slide graph on Omega is connected. The construction below
gives a path between any two states of length at most K^2+4K. For K=1 the
state space is a singleton and the assertion is immediate. No regularity or
bipartite hypothesis is needed. Connectivity concerns geometric matchings,
not a claim that the whole immutable marked state space is irreducible.

### Move a neighboring pair of vacancies through a fixed full matching

Fix a perfect matching F. Its edge contraction graph has one vertex for each
edge of F, with two vertices joined whenever G has an edge between their
endpoints. This graph is connected because G is connected.

Suppose the present state is F minus e={a,a'}, and a bridge edge {a,b} joins
e to f={b,b'} in F. The following two legal slides move the missing edge from
e to f:

    F-e -> F-{e,f}+{a,b} -> F-f.

The first slide moves b' to b and b to a. The second moves the record now at
b to a and the record now at a to a'. The missing sites after the two moves
are b,b'. The intermediate matching has K-1 edges throughout. This argument
does not use the color of any vertex or a fixed location for one vacancy.

Following a simple path in the contracted graph therefore moves the missing
edge to any chosen edge of F in at most 2(K-1) slides. The perfect matching F
is only a proof reference: the actual process never inserts a temporary
record or reads a global instruction in order to make either local slide.

### Use that pair to change a full matching along an alternating cycle

Let C be an alternating cycle for F, of length 2r. Bring the missing edge to
one F edge on C using the preceding construction. Write the cyclic vertices
as v0,...,v(2r-1), with F edges {v(2j),v(2j+1)} and holes v0,v1.

For j=1,...,r-1, slide the pair {v(2j),v(2j+1)} toward the currently vacant
v(2j-1). The new edge is {v(2j-1),v(2j)} and the moving vacancy becomes
v(2j+1); v0 stays vacant. After r-1 slides the state is

    (F symmetric_difference C) minus {v(2r-1),v0}.

All exterior edges are unchanged. Both sides are near-perfect states. Thus
an alternating-cycle change of the reference full matching is implemented
without any birth or deletion. Any two perfect matchings differ by disjoint
alternating even cycles, including when G itself has odd cycles.

### Reach and leave a state with adjacent vacancies

For an arbitrary M in Omega choose any perfect matching P of G. In M
symmetric_difference P, every vertex has degree zero or two except the two
vacancies of M, which have degree one. There is one alternating path joining
those vacancies, beginning and ending in P edges, plus disjoint cycles.
Slide along that path until only its last P edge has two vacant endpoints.
At most K-1 slides suffice. The resulting near-perfect state has the form
F-e for a perfect matching F: adding e is a virtual completion used only in
the proof, not a birth event.

Apply this construction also to a target T in Omega, obtaining F'-e'. Change
F to F' cycle by cycle using the preceding two lemmas, move the final missing
edge to e', and reverse the target's initial slide path. The full sequence
connects M to T using only legal slides.

For completeness, the two initial paths use at most 2(K-1) slides in total.
There are at most floor(K/2) nontrivial alternating cycles, their r values sum
to at most K, and their internal slides total at most K. Moving the vacancy
pair before each cycle uses at most 2(K-1) per cycle. The final missing-edge
placement uses at most 2(K-1). These estimates sum to at most K^2+4K-4,
and hence give the stated convenient bound. This bound on graph diameter is
not a polynomial mixing-time estimate: Omega can have exponentially many
states and bottlenecks have not been bounded.

### Consequence for formation and the clock

At fixed G, the symmetric slide chain is therefore irreducible with uniform
stationary law pi on Omega. With birth rate beta for the unique vacant edge
when the holes are adjacent, every perfect matching F has exactly K
near-perfect birth predecessors, one for each deleted edge. The killed-chain
arguments already derived in GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md
and GEOMETRIC_LAST_PAIR_CLOCK_AND_MONOMERS.md now apply under the weaker graph
hypotheses here. In particular, as beta tends to zero at fixed positive slide
rate and fixed graph:

* From any initially nonfull matching, its first completed geometry tends
  to the uniform law on all perfect matchings.
* Starting at the two-vacancy level, beta times the remaining waiting time
  tends to an exponential variable independent of that uniform exit state.
* Its rate is p=K times the number of full matchings divided by the number of
  near-perfect matchings, and beta times each entrance mean tends to 1/p.

The earlier finite-graph filling proof supplies almost-sure access to the
two-vacancy level. No birth is needed to prove the new connectivity lemma.
Fixed additional symmetric moves preserve the conclusion. Finite beta need
not select uniformly, and a state-dependent observation time after filling
can bias the law; neither qualification is removed.

For a nonbipartite graph the counting formula is

    |Omega| = sum over unordered {u,v} of Z(G minus {u,v}).

On a bipartite graph only opposite-side holes can contribute. The simpler
fixed-origin monomer sum requires the translation hypothesis stated in the
earlier torus note; it is not transferred to arbitrary bounded regions.

The extension covers connected bounded cubic regions that admit a perfect
matching, as well as the original regular tori. It does not automatically
import a large-deviation or field-fluctuation theorem: those results have
their own boundary, topology, measure and limiting hypotheses. No assertion
about fixed-rate large-volume mixing, a Coulomb phase, quantum dynamics or
propagating waves follows from this finite connectivity argument alone.

## Polynomial relaxation and simultaneous formation/volume limits

2026-09-21. Root candidate derivation, awaiting exact controls and selective
independent reconstruction. This uses the supplied classical-key geometric
process and the general-graph two-vacancy construction. It does not add a
deletion event to the physical process. Established matching-chain and
monomer-correlation results are explicit external inputs, not new results
claimed here. No formal retained or audit status is asserted.

### Definitions and finite-graph statement

Let G be a connected simple graph on 2K vertices with a perfect matching,
K>=2. Write m=|E(G)|, P for its perfect matchings, Omega for its (K-1)-edge
matchings, n=|Omega|, Z=|P|, R=n/Z, and pi for uniform measure on Omega.
Let S be the continuous-time slide generator, with rate kappa>0 for each
legal replacement {b,c}->{a,b} when a is vacant. Additional symmetric
conservative transitions can be present; all estimates below continue to
hold because they add a nonnegative Dirichlet form. The state-space
connectivity proof is GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md.

Put L=-S and denote its smallest positive eigenvalue by g. The comparison
below gives

    C_K = 1+2K(K-1),
    g >= kappa/[256 m R^4 C_K].                         (1)

This bound is useful when R is polynomially bounded. It does not claim
polynomial mixing on arbitrary connected graphs, for which R may be
exponential. The singleton K=1 case needs no relaxation estimate.

### An auxiliary chain and its trace on the actual state space

Use the Broder chain on Omega union P only as a comparison object. In
continuous time it has rate kappa for each slide, each completion of a
vacant edge, and each deletion of an edge from a perfect matching. Its
uniform law is reversible. At a full matching F, its K neighbors are
F-e for e in F, and its next neighbor is uniform among them.

Erase the time spent in P. The resulting trace chain on Omega consists of
the original slides and, for every F, jumps F-e -> F-f at rate kappa/K
for e!=f. Self-return excursions contribute no off-diagonal transition.
If A is the near/full incidence matrix and H=diag(h), where h indicates
adjacent vacancies, the positive trace generator is the Schur complement

    L_trace = L_slide + kappa [H - A A^T/K].             (2)

Each near-perfect matching has at most one full completion, since its two
holes specify the only possible missing edge. Every column of A sums to K.
In particular, (2) has zero row sums, as a conservative generator should.

For g0:Omega->R, extend it harmonically to a full F by the average of its
values at the K parents F-e. If mu is uniform on Omega union P, the
Dirichlet energy of this extension is mu(Omega) times the trace energy,
while its variance is at least mu(Omega) Var_pi(g0), by conditional
variance. The Rayleigh principle therefore gives

    gap(trace) >= gap(Broder continuous time).            (3)

The trace is an analytic comparison, not an assertion that a record is
actually erased and later recreated with the same content.

### Route every extra trace jump through record-preserving slides

Fix F. Contract each of its K edges. Choose once and for all a simple path
in the connected contraction graph between every ordered pair e,f in F,
and choose a bridge edge of G for each step. As proved in the general-graph
note, two legal slides move the pair of vacancies from one missing F edge
to the next. This gives a path from F-e to F-f of length at most
D=2(K-1). No edge of the resulting slide path repeats: a micro-edge touches
one of the distinct parent states along a simple contraction path, and
each intermediate state identifies its two missing F edges and bridge.

For a fixed unoriented micro-edge in the slide graph, there are at most
two possible reference perfect matchings F whose routed paths use it.
Indeed, one endpoint of that micro-edge must be a parent F-e; completing
the two holes at either endpoint determines F uniquely. For a fixed F
there are at most K^2 ordered parent pairs. Consequently at most 2K^2
routed paths use any micro-edge. This deliberately loose bound suffices.

The original slide energy is

    E_slide(g0) = (kappa/n) sum_unoriented_slide_edges (Delta g0)^2.

The added trace energy is

    E_add(g0) = kappa/(2Kn)
                sum_F sum_(e,f in F) [g0(F-e)-g0(F-f)]^2.

Cauchy-Schwarz along each path, followed by the preceding congestion
count, gives

    E_add <= D K E_slide,
    E_trace <= C_K E_slide.

Thus gap(slides) >= gap(trace)/C_K. Extra symmetric moves only improve
this lower bound for the actual conservative generator.

### The imported Broder bound and its clock normalization

Jerrum and Sinclair, *Approximating the permanent* (1989), Theorem 3.6,
gives the conductance bound

    Phi >= 1/(16 m R^2)

for their lazy edge-proposal chain on P union Omega, on any graph with
a perfect matching. Their Section 3, pp.1156-1157, selects one graph edge
uniformly and adds a holding probability 1/2. Hence every nontrivial
transition probability is 1/(2m). With our rate convention its transition
matrix is I+B/(2m kappa), where B is the continuous-time Broder generator.
The reversible conductance inequality gap(discrete)>=Phi^2/2 then yields

    gap(Broder continuous time) >= kappa/(256 m R^4).

This proves (1) using (3) and the route comparison. The exact source is the
[author-hosted paper](https://people.eecs.berkeley.edu/~sinclair/perm.pdf),
DOI [10.1137/0218077](https://doi.org/10.1137/0218077), Theorems 2.2 and 3.6
and the stated transition convention. The theorem's general-graph scope,
factor16, squared counting ratio, and lazy factor1/2 were checked against
the primary text. Its established conductance theorem is imported; a
new independent reconstruction of the entire 1989 proof is not claimed.

### A uniform rare-killing estimate without an inverse-hazard penalty

The following argument applies to any irreducible symmetric conservative
chain on Omega with gap g and uniform pi. Let P_t=exp(tS), Pi project onto
constants, and

    A0 = integral_0^infinity (P_t-Pi) dt,
    T_G = (1+log n)/g.

Then A0 is the centered inverse of L and

    ||A0 f||_infinity <= T_G ||f||_infinity.             (4)

To verify the constant, the spectral estimate gives
2 TV(P_t(x,.),pi)<=min(2,sqrt(n-1) exp(-g t)). Split its integral at
(log n)/(2g): the first part is at most (log n)/g and the tail at most1/g.
This proves (4), including functions that are not centered initially.

Now let every adjacent vacant pair complete at rate beta, and let tau be
the remaining time to that birth. Put p=pi(h)=KZ/n and U for uniform
measure on P. For any subset D of perfect matchings, let
a_D(M)=h(M) 1_{completion(M) in D}. Then pi(a_D)=p U(D).
The exit probability u(M)=Pr_M(exit in D) satisfies

    (L+beta H)u=beta a_D,       0<=u<=1.

Write u=c+v, c=pi(u). The centered inverse identity gives

    v=beta A0(a_D-hu),       ||v||_infinity<=beta T_G.

The stationary equation is pi(hu)=p U(D), so
c-U(D)=-pi(hv)/p and |c-U(D)|<=||v||_infinity. The factor p cancels,
because h is nonnegative. Uniformly over every initial near-perfect state,

    TV(law(exit),U) <= min(1,2 beta T_G).                (5)

This estimate also holds from any initially nonfull matching: the earlier
finite-graph filling result gives almost-sure entry to the two-vacancy
level, and (5) is uniform over its possibly beta-dependent entrance law.
No equilibration or mixing estimate at lower pair counts is required for
this statement about the final geometry.

For lambda>=0 the joint transform
u_lambda(M)=E_M[exp(-lambda beta p tau) 1_{exit in D}] solves

    [L+beta(H+lambda p I)]u_lambda=beta a_D.

Repeating the argument, using 0<=u_lambda<=1, gives the explicit bound

    |u_lambda(M)-U(D)/(1+lambda)|
       <= beta T_G (1+lambda p) [1+1/(1+lambda)]
       <= 2 beta T_G (1+lambda).                       (6)

The remaining clock tau always starts at the two-vacancy entrance, even
when the full process starts empty. Equation(6) does not apply to the
entire empty-start duration by silently including its earlier stages.

Mean convergence is checked separately. Set z=beta p E_M[tau]. Its equation
is (L+beta H)z=beta p, with z>=0 and pi(hz)=p. For v=z-pi(z), (4) gives
||v||_infinity<=beta T_G ||z||_infinity, while
|pi(z)-1|<=||v||_infinity. Consequently, if 2 beta T_G<1,

    sup_M |beta p E_M[tau]-1|
           <= 2 beta T_G/(1-2 beta T_G).                (7)

These statements do not infer convergence of moments from weak convergence.

### Even cubic tori: a polynomial schedule

For the periodic d-dimensional cubic torus of even side N>=4, d>2,
K=N^d/2 and m=2dK. The counting identity in the clock note is

    R=K chi_N,
    chi_N=sum_(v odd) Z_N(0,v)/Z_N.

Taggi, [arXiv:1909.06558v3](https://arxiv.org/html/1909.06558v3), Eq.(2.5),
bounds each monomer ratio by1/(2d) under these torus hypotheses. Therefore
R<=K^2/(2d). Substituting in (1), and using C_K<=2K^2, yields

    g_N >= kappa d^3/(64 K^11).

Also n<=2^m since every matching is an edge subset. Thus a fully explicit
upper bound usable in (5)-(7) is

    T_G <= Tstar_N
        := 64 K^11 [1+2dK log2]/(kappa d^3).             (8)

In particular, any schedule with

    (beta_N/kappa) K^12 -> 0                            (9)

gives total-variation convergence of the completed geometry to the uniform
matching law as volume grows. It also gives an asymptotically exponential
last-pair clock beta_N p_N tau of mean1, factorized from the exit geometry
in the precise uniform-event Laplace sense of(6). For example,
beta_N=kappa K^(-12-delta), any delta>0, suffices. This is a conservative
sufficient schedule, not a necessary scaling law or a practical estimate
of relaxation. The exponent12 is an upper-bound artifact, not a critical
or measured exponent of the physical process.

Combining (7) with Taggi's Theorem2.1 lower bound and the clock note's
counting conversion gives the same positive lower and upper constants for
beta_N E[tau]/V as in the earlier ordered limit, now along schedules(9):

    [1-r_d/2]/(4d) <= liminf beta_N E[tau]/V
       <= limsup beta_N E[tau]/V <= 1/(4d).

Neither existence of a coefficient limit nor a total-growth-time upper
bound is asserted. The lower clock bound is imported only for d>2.

### What this closes and leaves open

This supplies a quantitative bridge from permanent local record motion to
a known equilibrium matching ensemble in a simultaneous large-volume and
slow-formation limit. It replaces an unspecified size-dependent choice of
beta by an explicit sufficient polynomial one, subject to the named
external results. The auxiliary deletion is eliminated from the actual
model by a proved comparison path; no physical erasure channel is assumed.

Total-variation convergence transfers bounded-observable distributions and
probability-one limiting events from the uniform ensemble. By itself it
does not transfer exponentially small probabilities, large-deviation rate
functions, or unbounded-moment estimates. The finite-beta experimental
limit is different. No fixed-beta mixing/selection claim, dipolar dimer
correlation theorem, Coulomb-phase theorem, propagating field dynamics,
unknown-qubit recognition mechanism or TOE identification is proved here.

## Evidence and open obligations

[The evidence packet](../.claude/science/mobile-record-geometric-formation-20260921/README.md) preserves the original arguments,
author checkers and their historical outputs, with the one fixture correction
and its old source explicitly preserved. The source-bound
runner executes all five complete assertion suites in a temporary directory.
Exact symbolic and finite graph checks support specified proof steps; they do
not verify an infinite-volume phase or the proof of the imported literature.

The equilibrium input is [Taggi, arXiv1909.06558v3](https://arxiv.org/html/1909.06558v3),
Theorem2.1 and the stated monomer-ratio bound. The note identifies its graph,
dimension and normalization hypotheses. Its proof is not presented as an
independent result of this campaign. The reference PDF is deliberately
excluded from the portable packet; its version, URL and original local hash
are recorded. The relaxation input is [Jerrum and Sinclair (1989)](https://people.eecs.berkeley.edu/~sinclair/perm.pdf),
Theorems2.2 and3.6 with their lazy edge-proposal convention. Auxiliary deletion
is only a comparison device: the record process realizes the replacement
paths entirely through legal immutable-record slides. Its reference PDF and
extracted pages are likewise excluded from the portable packet.

The numerical fixed-rate formation screen is not a premise of these proofs
and is not bundled as theorem evidence. The joint construction of a correlated
formed state and propagating transverse dynamics remains open, as do the
operational quantum bridge and a principle selecting these supplied rates.
No physical charge, Maxwell identification, Lorentz symmetry, gravity or
experimental prediction follows from the geometric Gauss readout alone.

Combined pipeline, strict audit lint and changed-evidence integration are
mechanical integration checks recorded in the evidence packet. No independent audit verdict or retained status is
conferred by this proposed theorem note or its selective checks.
