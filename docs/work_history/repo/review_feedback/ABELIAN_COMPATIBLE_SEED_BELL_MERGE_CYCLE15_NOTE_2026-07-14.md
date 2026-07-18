# Abelian Compatible-Seed Bell Merge — Cycle 15

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is a conditional exact construction, assumptions
exercise, and bounded no-go stress test. It is not an axiom proposal, retained
theorem, audit verdict, or claim that nature is literally a computer. It
changes no axiom, primitive, premise registry, review queue, or audit surface.

Companion runner:

```text
scripts/abelian_compatible_seed_bell_merge_cycle15_2026_07_14.py
```

## Result Up Front

Cycle 14's multi-front collision wall has an exact split.

The compatible half closes. A homogeneous nearest-neighbor rule

```text
P at x + open, unprotected nearest neighbor y  ->  P at x + P at y
```

is a same-content grow-only map. `P` is one rank-one possibility in the same
`M2(C)` already supplied at each site, not an extra local register. Every
nomination of an open target proposes exactly the same content. Permanent
record maps therefore form a join-semilattice under compatible union. The join
is commutative, associative, idempotent, and inflationary. It follows that
every finite compatible seed set has one least closure, independent of rewrite
order. This is exact branchwise schedule confluence with no hidden priority and
no hidden cursor.

The runner couples that program field to two protected relational Bell cages.
Each cage retains the Cycle 13/14 nearest-neighbor `CZ-CZ` interaction, permanent
preparation certificate, center `X` record, and endpoint `Z` records. Program
writes cannot enter a cage's three data sites or certificate site. Bell writes
cannot leave them. For any fixed supplied physical outcome in each cage, the
program actions, preparations, center events, and left/right reads commute
whenever they are simultaneously ready. Twenty-two deliberately different
schedules on a 504-site finite box reach the identical complete record map.
The exact quantum calculation still gives the four parity-consistent complete
histories, each with conditional weight `1/4` under the supplied
projective/Born instrument.

The incompatible half cannot be repaired by an order-free append after the
fact. If two enabled transitions add

```text
(site s, content a)          and          (site s, content b),   a != b,
```

then the two successors have no common extension in a state space with one
locked possibility per site and permanent records. A later merge label `j`
would have to replace `a` or `b`; waiting to write `j` is a different
pre-write arbitration rule; routing both values to different sites consumes
additional capacity; and choosing one is a priority. This is the smallest
nonjoinable critical pair. It does not depend on the larger Cycle 14 builder
geometry.

The complete atomic critical-pair census makes the boundary exhaustive for
singleton additions on two representative sites with three contents. Of the
21 unordered pairs including self-pairs, 15 are joinable diamonds and six are
the distinct-content/same-site obstruction. The runner also checks the larger
representative pairs: two nominations of the same `P`, disjoint `P` writes,
program versus certificate, two cages, left versus right read, duplicate Bell
event, an overlapping compatible multi-site union, and one incompatible
output pair.

A topological braid does not remove this boundary. Three-qubit `SWAP`
generators satisfy the Yang-Baxter braid relation exactly, so unrecorded
carriers can be rerouted without an ordering choice. But moving a carrier that
is already a record clears its old site and changes its content, which is not
an extension. Literal defect annihilation likewise removes a record. Keeping a
permanent trail makes the motion append-only, but then the trail is another
grow-only record map and its intersections face the same compatible-union
criterion. Commuting `CZ` interactions retain Bell capability but do not join
incompatible record contents.

This closes only compatible-seed scheduler confluence. It is not a full
autonomous replacement for Cycle 14's repeated self-writing Bell front. The
Bell cages and their protected supports are finite supplied boundary content;
the physical outcome in each cage is supplied branch content; preparation,
occurrence, and read instruments remain candidate law fields; and weights,
actuality, and rate remain open. The construction says exactly what a
collision-free append-only sector can do and exactly where it stops.

Formation-as-extension remains a theorem of this candidate law, not a theorem
of the current four axioms. No new Record axiom is forced. The collision
boundary follows from one record per site plus permanence once distinct writes
are admitted; it is not an independent constitutional atom. A future law must
make prospective conflicts compatible before the first permanent write, keep
them on different sites, or state an outcome/priority rule. Adding a more
poetic synonym for “formation” to the Record axiom would not choose among those
physical laws.

## Framework and Predecessor Refresher

The exercise was run against the live foundation and governance surfaces:

- `docs/MINIMAL_AXIOMS_2026-06-29.md`;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`;
- `docs/audit/data/axiom_premise_nodes.json`;
- the registered scale-reference, kinetic-isotropy, and realized-state notes;
- the fresh `origin/main` exercise, review-loop, and no-go-discipline
  instructions; and
- `docs/repo/CONTROLLED_VOCABULARY.md`.

The foundation remains four axioms and three registered primitives. Lattice
supplies the actual cubic site set and nearest-neighbor relation. Qubit supplies
one `M2(C)` possibility algebra per actual site. Admissibility supplies a
fixed, uniform local rule for available possibilities. Record says that
records form, lock exactly one admissible local possibility, are permanent,
and are the only readable facts. It explicitly withholds formation dynamics.
It also does not supply collision arbitration, occurrence, preparation,
probability, actuality, or rate.

Cycle 14 supplied a finite seven-record seed and an append-only Bell front that
wrote its next relational header. It proved indefinite growth on an isolated
blank corridor. Its exact collision counterexample put `B0` and `B1` at the
same target under two legal front orientations. If one wrote before the other
became locally visible, permanence froze the first arrival. Cycle 14 therefore
left arbitrary multi-front confluence open.

This cycle asks the narrower mathematical question that counterexample forces:

> What is the largest order-free append-only sector, and can a braid or merge
> operation include genuinely different outputs without adding priority,
> hidden state, or overwrite?

## Exact State Order

A classical record state is a partial map

```text
R : Z3 -> record content.
```

The map is only the already-recorded part of the framework state; it does not
replace the local `M2` possibility algebra. The extension order is

```text
R <= S  iff  every (site,content) in R is also in S.
```

Thus an allowed transition may add records but may neither remove one nor
change its content.

Two maps are compatible exactly when they agree on every shared site. Their
join is compatible union:

```text
R join S = R union S.
```

On compatible maps this operation is:

```text
commutative:  R join S = S join R
associative:  (R join S) join T = R join (S join T)
idempotent:   R join R = R
inflationary: R <= R join S.
```

These are CRDT/abelian-network properties, but no software metaphor is needed
for the proof. They are ordinary properties of consistent sets of permanent
facts.

The runner realizes every named local content as a rank-one projector in one
`M2`. The header, Bell-read, certificate, and `P` labels are different
possibilities, not different dimensions of the site's carrier. The candidate
still imports the relational frame/connection needed to compare named
projectors across sites.

## The Positive Law

### Homogeneous program spread

At every actual site and in each of the six nearest-neighbor directions, apply
the same rule:

```text
if x carries P,
and y is a nearest neighbor of x,
and y is open,
and y is not a protected role in a recognized Bell cage,
then append P at y.
```

The physical write is across one nearest-neighbor edge. The rule contains no
coordinate, origin, preferred axis, agent identifier, timestamp, or mutable
front state. Translation and all 24 proper cubic rotations preserve it.
Multiple `P` sources nominating the same target make the identical addition;
source identity is irrelevant. This is the minimum same-content merge code.

The protected-role test is a bounded relational guard, not a global mask. A
Bell cage is recognized by the same six-record orientation header used in
Cycles 13 and 14. For program `(t,d,e)`, with `u=d cross e`, the data sites are

```text
t+d, t+2d, t+3d,
```

the certificate site is `t-e`, and the six header sites are

```text
t+e, t+2e, t+3e, t+u, t+2u, t+d+e+u.
```

The law ranges over every perpendicular ordered pair `(d,e)`, so the cage has
no law-level orientation. The exact runner checks all 24 proper cubic rotations
and all six unit translations.

### Bell cage actions

Within a recognized cage:

1. a reset/preparation event prepares the fresh triple as `|+++>` and appends
   certificate `C` at `t-e`;
2. nearest-neighbor `CZ` acts on the first/second and second/third edges;
3. an `X` outcome is appended at the center site; and
4. the two endpoint `Z` outcomes may be appended in either order.

The certificate and every read are permanent. The complete phase is readable
from records. The construction inherits the explicit prices already found in
Cycles 13 and 14: reset/preparation is irreversible on the same carrier,
occurrence is law content, and the projective/Born instrument is imported.

For schedule testing, each cage is assigned one of the physically allowed
complete outcomes. One fixture uses `X+,Z0,Z0`; the other uses `X-,Z0,Z1`.
This is not a branch selector. It conditions the rewrite-order question on a
fixed physical history. Different allowed physical outcomes are not expected
to converge to the same record state; doing so would erase actuality.

## Compatible Seed Domain

The theorem applies to every finite compatible seed set under these explicit
conditions:

1. initial partial record maps agree wherever they overlap;
2. complete cage supports are identical or disjoint;
3. identical cages use the same transported frame and instrument;
4. a `P` seed is not placed on a cage header, trigger, data, or certificate
   role; and
5. the physical outcome branch assigned to an identical cage is the same.

These are compatibility conditions, not an arbitration rule. They say that
the input does not already demand two different permanent facts at one site.
Calling an incompatible seed “compatible” would hide the very wall being
tested.

Protected cage placement is boundary content. Bell outcomes remain supplied
branch content. Same-content spread is candidate law content.

## Confluence Theorem

For every finite compatible seed set, and for every fixed assignment of
allowed Bell outcome branches, every fair sequence of enabled actions has the
same least fixed-point record map.

### Proof

Each action is inflationary: it adds one record and changes none. Two
simultaneously enabled program actions either add `P` at different sites or
add the same `P` at the same site. Their unions commute. Program actions never
target protected cage sites. Actions in disjoint cages have disjoint targets.
Within one cage, preparation precedes the center event; after the center event,
the left and right endpoint actions have disjoint targets and commute.
Duplicate recognition of the identical cage proposes identical additions.

Consequently, every simultaneously enabled compatible pair forms a local
diamond. In a finite domain, every nontrivial action strictly increases record
count, so rewriting terminates. Termination plus local confluence gives a
unique normal form. Equivalently, repeated application computes the least
fixed point of a monotone Horn closure operator. On an infinite lattice, every
finite derivation is a prefix of the same directed union; fairness is needed
only to ensure that an action which stays enabled is eventually taken.

No priority or cursor appears in the state or proof. Ordering can change the
time at which a site is written, but not which record map is reached.

The finite fixture contains two disjoint cages, two `P` seeds, and 504 sites.
It runs first-action, last-action, and twenty pseudorandom schedules. All 22
schedules fill the domain and end in the identical record map while using
different action histories.

## Complete Atomic Critical-Pair Census

Take two representative sites and three representative contents `P,H0,H1`.
There are six singleton append actions. The unordered pairs including the six
self-pairs total 21.

```text
same action/self pair                         6 joinable
different sites, any contents                 9 joinable
same site, distinct contents                  6 nonjoinable
                                               ----------
                                               21 total
```

Every joinable case is an exact two-step diamond. Each nonjoinable case is the
same mathematical obstruction: the first path permanently writes one content
where the second path permanently writes another.

The representative higher-structure census is:

| Pair | Result | Reason |
|---|---|---|
| two `P` parents, same target | diamond | identical idempotent addition |
| two `P` writes, disjoint targets | diamond | disjoint union |
| `P` write and cage preparation | diamond | protected/disjoint targets |
| preparations in distinct cages | diamond | disjoint supports |
| left and right endpoint reads | diamond | disjoint targets |
| duplicate identical Bell event | diamond | identical addition |
| overlapping compatible multi-site writes | diamond | shared entries agree |
| different contents at one site | no join | permanence forbids common extension |

This census addresses rewrite-order nondeterminism. Quantum outcome alternatives
at a measurement are different physical histories, not scheduler critical
pairs. We do not collapse them under a confluence slogan.

## Minimal Impossibility Boundary

Let `R` be a record state with open site `s`. Suppose two legal transitions are

```text
R -> R_a = R union {(s,a)}
R -> R_b = R union {(s,b)},     a != b.
```

Assume there were a common extension `T`. Permanence requires `T(s)=a` because
`R_a <= T`, and also `T(s)=b` because `R_b <= T`. A partial function cannot
have both values at one argument. Contradiction.

This proves a bounded no-go:

> Once distinct contents have actually been written at the same one-record
> site on alternate paths, no later append-only operation can make those paths
> confluent.

In short, distinct permanent outputs at one site are nonjoinable after either
write. This does not prove a general no-go for conflict avoidance before
formation, spatial routing, or globally consistent histories.

It does not prove that nature cannot avoid the pair. It enumerates the escape
routes:

1. **Compatibility before write.** Compute one common content while the target
   is still open, then write only that content. This needs a law saying when
   the proposal set is complete; a late proposal reopens the problem.
2. **Spatial routing.** Preserve both values at distinct sites. This consumes
   capacity and needs a collision-free allocation code.
3. **Larger local carrier.** Store a set of proposals locally. The stipulated
   one-`M2`/site target does not supply that extra tensor factor, and permanent
   updating of the set is still forbidden after the first record.
4. **Overwrite or erasure.** Replace `a` by a join label. This directly violates
   record permanence.
5. **Priority or selection.** Let one proposal win. This can be a physical law,
   stochastic event, or boundary choice, but it is not confluence and must be
   stated openly.
6. **Global solution.** Admit only histories whose full record assignment is
   consistent. This can avoid local conflicts, but global admissibility and
   actuality become the missing law fields.

The Cycle 14 `B0/B1` collision is an instance of this theorem. Same-content
copying removes the conflict by changing the code, not by merging `B0` and
`B1` after either is permanent.

## Topological Braid and Defect Probe

The braid route has one genuine success. On three unrecorded qubit carriers,
nearest-neighbor SWAP operators obey

```text
S12 S23 S12 = S23 S12 S23.
```

Thus two descriptions of the same braid give exactly the same unitary. A
carrier can be moved around another carrier without a hidden priority.

That does not yet solve the record problem:

- `SWAP |100> = |010>` moves an excitation by clearing one site and filling
  another. If the old occupation was a record, the map is not an extension.
- A defect/anti-defect annihilation removes both defects. If either was a
  record, annihilation violates permanence.
- Leaving an immutable world-line trail preserves permanence. The trail is
  then an append-only set, and two trails can share a site only when their
  proposed permanent content agrees.
- Adjacent `CZ` gates commute and supply the entangling resource used by the
  Bell cage. Commutativity of unitaries does not create a common extension for
  two different record maps.

A topological encoding may still be useful upstream of record formation. It
could braid unrecorded possibilities and postpone locking until a compatible
joint value is available. That is a formation/occurrence law proposal, not a
post-record merge. The present probe therefore keeps the route open in its
proper domain and closes the claim that braiding alone repairs already
different permanent outputs.

## Bare-Metal Interpretation

The exact result supports a modest storage-accounting picture without turning
the metaphor into an axiom.

An append-only universe can avoid collision bookkeeping cheaply when every
causal route to a site agrees on the fact to be stored. Duplicate causes are
then idempotent: the universe need not remember which arrived first. This is
the physical content behind the same-content CRDT analogy.

When routes disagree, append-only storage has no cost-free merge. The system
must spend something before the write:

- more space to keep both proposals;
- more causal depth to form a joint proposal;
- a selector/actuality event to keep one;
- or a global consistency restriction that forbids the conflict.

The “compute/storage limited” intuition therefore identifies a real design
pressure, but it does not select one of these laws. Resource economy can
motivate a same-content or delayed-locking formation mechanism. It cannot by
itself derive which physical outcome becomes actual, its probability, or its
rate.

## Science-Lane Ledger

| TOE lane | What this cycle establishes | What remains |
|---|---|---|
| record formation | every candidate transition is an explicit permanent extension | occurrence/locking condition is still law content |
| collision handling | complete confluence for compatible same-content seeds | incompatible proposals require pre-write law or selection |
| locality/covariance | `P` writes across NN edges; cage is relational; translations and 24 proper rotations checked | transported frame remains imported |
| quantum/Bell | exact one-`M2` content and NN `CZ-CZ` parity histories survive | preparation/instrument, weights, actuality imported |
| record-only readiness | cage phase is reconstructible from header, trigger, certificate, and reads | `P` field does not self-generate repeated cages |
| time/clock | partial order of extensions is explicit | no metric rate or lapse follows |
| capacity | conflicts can be routed only by spending extra sites | no law selects capacity allocation |
| gravity/saturation | append-only routing exposes a qualitative storage pressure | no curvature, Einstein dynamics, or coupling derived |
| mass/counting | no new result | counting/conjugacy fork untouched |
| chirality/matter | braid route remains possible before locking | no fermion spectrum or chiral law derived |

The positive construction closes only compatible-seed scheduler confluence.
It does not close the framework's formation, actuality, probability, rate,
mass, gravity, or chirality lanes.

## Law, Boundary, and Constitutional Classification

### Candidate law content

- same-content `P` spread;
- recognition/protection of a finite relational cage;
- reset/preparation instrument;
- Bell interaction and read instrument; and
- occurrence conditions for each append.

### Boundary content

- finite `P` seeds;
- protected cage placement is boundary content;
- the transported relational frame;
- blank/open support; and
- supplied branch assignment used to test schedule order.

### Still open

- Bell outcomes remain supplied branch content;
- weights and actuality remain open;
- rate remains open;
- arbitrary incompatible-seed resolution;
- autonomous repeated Bell-cage generation;
- global capacity and saturation dynamics; and
- the downstream mass, gravity, and matter lanes.

### Axiom consequence

Formation-as-extension remains a theorem of the candidate law. It is not a
theorem of the current four axioms because the axioms do not choose this law or
say when it fires. No new Record axiom is forced.

The collision boundary follows from one record per site plus permanence. It is
already a consequence of taking “locks exactly one local possibility” and
“records are permanent” literally. It does not warrant a separate Merge axiom.
The missing content is dynamical: what prospective incompatible proposals do
before any record forms. That belongs first in competing conditional laws and
their discriminating probes, not in constitutional wording.

## No-Go Discipline N1–N8

### N1 — Alternative route enumeration

Tested routes were same-content compatible union, a precomputed local join,
spatial routing, larger local storage, overwrite, priority/selection, global
consistency, unitary braid transport, defect annihilation, immutable braid
trails, and commuting entangling gates. The positive sector and each escape
price are stated separately.

### N2 — Wall-independence audit

The nonjoinable-pair proof uses only: one record content per site, permanence
as extension, and two actually available distinct writes at one open target.
It does not use Born weights, clock rate, frame choice, mass counting, reset,
or the specific Cycle 14 header. Removing any one of the three used premises
removes the proof.

### N3 — Hidden-wall scan

The positive theorem is restricted to compatible inputs, fair schedules, and
fixed physical outcome branches. Cage placement, initial `P` seeds, relational
frame, blank support, reset, instrument, and outcome branch are exposed. The
finite fixture does not establish autonomous repeated cage production.

### N4 — Residual matching

The residual is not vaguely “collisions.” It is the exact critical pair
`(s,a)` versus `(s,b)` with `a != b` after either permanent append. Upstream
braiding and delayed formation remain live because they avoid reaching that
residual rather than trying to join it afterward.

### N5 — Rhetoric audit

“CRDT,” “abelian,” “braid,” “compute,” and “storage” are analogies or standard
mathematical labels, not explanations by themselves. Every positive claim is
backed by a map, matrix identity, finite census, or order proof. No claim that
nature is literally simulated is made.

### N6 — Partial-closure path scan

The same-content sector is a real partial closure: duplicate causal paths need
no priority, arbitrary finite compatible seeds have one closure, and Bell cages
can coexist branchwise. Upstream topological routing is also left open. The
negative result is not allowed to erase those gains.

### N7 — Steelman

The strongest contrary proposal is: braid all still-open quantum information,
compute one symmetric joint value, and form a record only after the braid has
made the proposals compatible. This evades the post-write no-go and may supply
a useful formation model. Its remaining burden is an exact local stopping rule
that knows the joint proposal is complete, retains Bell outcomes, grows from
finite data, and supplies occurrence without a hidden cursor or global clock.

### N8 — Cross-cycle echo

Cycle 14's explicit `B0/B1` collision is reproduced at the abstract singleton
level rather than merely cited. Cycle 13's Bell calculation is rerun. The
result agrees with earlier walls: append-only visibility is achievable;
actuality, rate, and incompatible-content selection are not supplied by
permanence alone.

## Bottom Line

The smallest successful merge law is not a clever collision algorithm. It is
agreement before writing: all paths that reach one target append the same
content. In that sector, permanent facts form an abelian grow-only structure
and order disappears exactly.

The smallest failure is equally bare: two different permanent contents at one
site. Once either is locked, no later read, clock tick, braid, or merge record
can make the histories equal without overwrite, extra storage, or selection.

That distinction is useful for the formation-language question. A viable
bare-metal law may delay locking until causal evidence has become compatible,
or may let a record-forming event select one branch. But the present axioms do
not decide which. The honest next probe is upstream of formation: construct a
local, covariant readiness condition that turns many open proposals into one
compatible write while retaining Bell statistics and without smuggling in a
global completion signal.
