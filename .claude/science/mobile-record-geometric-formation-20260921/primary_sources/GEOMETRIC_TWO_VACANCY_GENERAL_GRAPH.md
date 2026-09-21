# Two vacancies connect the matching space without regularity or bipartiteness

2026-09-21. Root candidate proof, awaiting exact controls and selective
independent reconstruction. This strengthens the geometric projection of the
supplied permanent-record process; it does not strengthen the operational
meaning of its classical antipodal keys. No new local event is added.

## Statement and legal elementary move

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

## Move a neighboring pair of vacancies through a fixed full matching

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

## Use that pair to change a full matching along an alternating cycle

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

## Reach and leave a state with adjacent vacancies

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

## Consequence for formation and the clock

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
