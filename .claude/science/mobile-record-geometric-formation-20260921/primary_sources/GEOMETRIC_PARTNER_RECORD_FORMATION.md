# Permanent antipodal records with a movable geometric pairing

2026-09-21. Root proposed construction and conditional finite-volume theorem.
This changes the earlier direction-tag encoding: a dimer's spatial direction
is derived from its two positions, while each record's content stays fixed.
The construction is a classical stochastic process on specified M2-presented
possibilities. It is not an implementation by quantum instruments, a retained
axiom consequence, a Coulomb-phase theorem, or a wave model.

## Contents, domain, and supplied symmetry bridge

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

## One local rule for formation, with varying nearest-neighbor odds

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

## Whole-record motion, including turns

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

## Every partial matching can gain another pair

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

## Geometric Gauss and the remaining state/dynamics questions

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
