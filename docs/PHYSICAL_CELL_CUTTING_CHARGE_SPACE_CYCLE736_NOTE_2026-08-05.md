# The space of charges on the single cell's least-cost cuttings — Cycle 736

Date: 2026-08-05

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No axiom or primitive is
proposed or adopted. Audit status is set only by the independent audit lane, and effective
status is pipeline-derived.

Primary runner:
[`scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py`](../scripts/physical_cell_cutting_charge_space_cycle736_2026_08_05.py)
(deterministic finite arithmetic; fails closed).

Independent checker:
[`scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py`](../scripts/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.py)
(reconstructs the finite object without importing or executing the primary).

## Supplied model and dependencies

This is a theorem only about a supplied finite model: the four-cube on the sixteen corners
of `{0,1}^4`, with three labelled spatial columns, one labelled tick column, normalized-
volume-one corner 4-simplices, the declared four-coordinate L1 pair charge, and a declared
48-element action made from 24 proper spatial signed permutations and the optional labelled
tick flip. A cutting is a set of 24 such simplices with disjoint relative interiors and
total normalized volume 24.

The [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md) supply only the spatial `Z^3`
nearest-neighbour lattice and proper cubic rotations. The registered
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) supplies only
equal spatial/tick kinetic-form graining. Neither source selects this one-box domain, the
corner-simplex class, the declared pair charge, a physical assembly cell, or a
tick--Admissibility realization.

[Cycle 733](PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md)
is the direct theorem dependency: its hash-bound receipt certifies the same supplied model
and the 15,800-member population through an independent exact geometric route. Cycle 736
also rebuilds that population before computing any new charge-space result. Later
move/charge cycles are comparative context only: none of their receipts or numerical
literals is imported into either runner here.

Within that bounded population, reversing every move of one size is a linear demand on a
piece weight. The induced charges have rank three: eight functions including two constants,
or three nonconstant charges up to complement. One keeps four-piece moves, one keeps
six-piece moves, and one keeps seven-piece moves. The four-keeping charge is exactly the
indicator of one orbit of connected components under the supplied 48-element action. These
are finite incidence and GF(2) statements, not physical conservation laws or framework-wide
selection statements.

## The cell, the floor, and the moves between cuttings

Of the 4368 five-element subsets of the 16 corners, 2672 have normalized volume one. They
carry 2736 generic rational sample points with no collision and no boundary incidence; this
finite incidence structure accelerates the exact-cover search but is not treated as a
geometric proof. For each of the 391 supplied-symmetry orbits of returned covers, the primary
and independent checker separately verify all 276 simplex pairs with exact integer
separating directions. The resulting 107,916 pair certificates, together with 24 unit-
volume pieces, prove disjoint interiors and total volume 24. A hostile control exhibits
sample-disjoint simplices that overlap, confirming that this separate geometry gate is
load-bearing. The declared action has 48 elements and the pieces form 57 orbits under it.

The declared cost of a piece is 6 at the floor and 400 pieces reach it. A complete search
over those 400 visits 502838 nodes and returns 15800 exact geometric cuttings of 24 pieces
each, which between them use 192 of the 400. Every cutting therefore sits at declared cost
24 times 6, or 144.

A move carries one cutting to another and is measured by how many pieces it replaces. Over
all pairs of the 15800 the counts are

    four 46128     five 0         six 31968      seven 60096
    eight 151704   nine 119808    ten 281376

so no move at all replaces five pieces, while the smallest move replaces four. That the
five piece count is zero is a measurement and not a parity effect: a move replacing k
pieces changes 2k of them in all, so it is the change and not k that is forced even, and
sizes of either parity are otherwise present. Different moves can exchange the same set of
pieces; reducing each move to the pieces it takes out and puts in leaves 120, 528, 1152,
4212, 6144 and 25248 distinct exchanges at four, six, seven, eight, nine and ten pieces.
The 120 count is reconstructed here rather than imported from a prior receipt.

## Which sizes of move a weight on the pieces can reverse

Read a weight as a choice of one of two signs on each of the 192 pieces in use, and read
the charge of a cutting as the count of its pieces the weight marks, taken modulo two. A
move changes that reading exactly when the weight marks an odd number of the pieces the
move exchanges. So demanding a charge that every move of one size reverses is a demand made
of the exchanges alone, and it is linear: the weight must mark an odd number of pieces in
each of them.

The runner settles the demand by adding one extra coordinate to the pool and setting it on
every exchange of the size in question. A weight reversing all of them exists exactly when
that extra coordinate does not lie in the span of the enlarged exchanges. When it does lie
in the span, elimination hands back the reason directly: a family of the original exchanges,
of odd size, summing to zero. A weight marking an odd number of pieces in each member of
such a family would have to mark an odd number in their sum, which is empty, so no such
weight exists.

Across the six nonempty move sizes `{4,6,7,8,9,10}` the demand is met at four and at no
other size. The empty size-five class is not assigned a nonvacuous response pattern. A weight is
exhibited whose reading changes across every one of the 46128 smallest moves. At six,
seven, eight, nine and ten pieces the obstruction is exhibited in its place, as families of
7, 5, 5, 7 and 5 exchanges summing to zero, each of odd size. The obstruction is therefore
a small and checkable object at every size where it appears: five or seven exchanges,
against move counts in the tens and the hundreds of thousands.

## How the exchange spans sit inside one another

The 15800 cuttings, each read as its list of pieces, span 88 dimensions, and their
differences span 87. The differences of the exchanges of a single size span 85 at four,
rising to 87 at eight, nine and ten, so the moves on eight pieces already reach everything
the differences of the population reach. At seven they do not: a difference of two cuttings
lying outside the seven piece span is exhibited.

The spans of the small sizes sit in a definite pattern. The four piece span lies inside both
the six piece and the seven piece span, and neither of those two holds the other. Their sum
is the eight piece span, which is also the nine piece and the ten piece span, and their meet
has dimension 85. Since that is the dimension of the four piece span, and the four piece
span lies inside both, the four piece span is exactly the overlap of the six piece and the
seven piece spans. The smallest move is thus not an outlier among the sizes but the common
part of the next two.

That pattern controls what mixed demands can do. Of the 63 non-empty subsets of the six
nonempty sizes `{4,6,7,8,9,10}`,
exactly 3 admit more than one answer pattern — four alone, four with six, and four with
seven — and each of those admits 2. Every other set, the whole of them included, admits
exactly one. So the freedom in the whole question lives entirely at the smallest move and
in the two sizes that share it.

## The three charges

Weights that answer the smallest move uniformly, keeping the reading on every one of the
46128 or reversing it on every one, form a space of dimension 107. Pushed forward onto the
cuttings, those weights induce 8 charges, spanning dimension 3, of which 2 are constant.
Up to swapping the two sides that is 3 charges, and each of them keeps exactly one of the
four, six and seven piece moves:

    keeps           split  rigid side     at 4     at 6     at 7     at 8     at 9    at 10
    four      5664/10136        10136        0     9504    26880    32640    48960   124224
    six       7704/8096          7704    46128        0    26880    28608    87552   190848
    seven     7424/8376          8376    46128     9504        0    21312   102336   183744

read as the two sides of the charge, the side carrying the 48 cuttings that admit no move
on at most eight pieces, and how many moves of each size the charge reverses. The three rows
are reconstructed simultaneously here. The middle row has the 7704/8096 split and flips
26880 of the 60096 seven-piece moves; the bottom row keeps seven-piece moves and reverses
every smallest move; the top row keeps the smallest move outright. Agreement with prior
finite censuses is contextual corroboration, not an input to these values.

The three are not independent as functions. A space of dimension 3 that holds the two
constants leaves exactly 3 charges once the two sides of each are counted as one, and any
one of those is then the sum of the other two; here the top row is the sum of the middle and
the bottom. So the sister charges and the charge keeping the smallest move arrive as a
single triple rather than as three separate finds.

Demanding uniformity at six and at seven together, rather than at four, leaves a weight
space of dimension 105, and every charge those weights put on the cuttings is constant. So
combining the six- and seven-piece demands collapses the induced cutting charge to a
constant: the sister charges are nonconstant alternatives, not an independent pair.

The exhibited weight sits tightly on its demand rather than loosely satisfying it: moving
it on a single piece already destroys uniformity at the smallest move.

## The groups the smallest move leaves, and which charge names them

Join two cuttings whenever a smallest move carries one to the other. The population falls
into 349 groups, of sizes 1, 2, 4, 7, 236 and 9320, with 144, 96, 36, 48, 24 and 1 groups
at each size. They are reconstructed here because the charges are read against them.

No element of the supplied 48-element action splits a group, so it permutes the 349 groups,
and under that action the groups fall into 14 orbits.
Two features of that action carry the result. The 24 groups of size 236 form a single orbit,
whose stabiliser has order 2. The one group of size 9320 is held fixed by all 48.

Against that, every one of the 8 charges is left where it is by all 48 elements of the
supplied action, point by point: not merely permuted among themselves, but each one fixed.
The comparison that gives this force is the indicator of a single group of 236 cuttings,
which the same 48 elements
carry to 24 different functions. So being fixed by the symmetries is not automatic for
functions built out of the groups, and the charges pass a test that a group indicator fails.

The charge that keeps the smallest move is exactly the indicator of that one orbit of 24
groups, holding 5664 of the 15800 cuttings, which is 24 groups of 236. It is therefore not a
solution the elimination happened to return but a named subset of the population, picked out
by the declared finite action on the groups the smallest move leaves. The 48 cuttings
that admit no move on at most eight pieces all sit off it, so the hard core of the population
is on the larger side of this charge.

## Independent cross-checks performed

The independent checker imports or executes neither the primary nor an author summary. It
rebuilds all 2672 unit-volume simplices using an exact recursive determinant, validates every
rounded inverse by integer multiplication, reconstructs the declared corner action, builds
the 2736-point incidence system, and repeats the complete 502838-node cover search. It then
checks one exact-separation representative of every supplied-symmetry orbit, so all 15800
accepted objects are independently certified as geometric cuttings rather than sample-mask
covers.

It next performs the full unordered-pair census, rebuilds all exchange masks, and uses a
separate GF(2) elimination to recover the population ranks, the six exchange-span ranks, and
the fact that the all-ones reversal demand is consistent only at size four. From the
orthogonal space it reconstructs all eight induced charge functions and the three table rows
above. Finally it rebuilds the 349 connected components, their 14 orbits under the supplied
action, and the exact equality between the four-keeping support and the union of 24
components of size 236.

The checker includes five hostile controls. It finds sample-disjoint simplices with
overlapping interiors, so deleting the exact geometry gate is detected. A one-bit mutation
of a smallest exchange changes the certified response rank. A local semantic mutation of
the primary changes its content hash. Mutating the terminal Cycle 733 receipt hash breaks
the declared input contract. A generated receipt with `status: fail` and a nonzero failure
count cannot satisfy the checker acceptance predicate. These controls make the geometry,
semantics, dependency chain, and conditional verdict independently load-bearing.

Canonical evidence:

- [primary cache](../logs/runner-cache/physical_cell_cutting_charge_space_cycle736_2026_08_05.txt)
- [independent cache](../logs/runner-cache/physical_cell_cutting_charge_space_cycle736_independent_check_2026_08_05.txt)
- [generated receipt](../outputs/physical_cell_cutting_charge_space_cycle736_2026_08_05_receipt_2026-08-05.json)

The required fresh sequence is primary first and checker second; the primary regenerates
the receipt, and the checker refuses stale input hashes or a failed verdict.

## No-Go Discipline Gate

Negative assertion class: `derived_no_go_boundary`. The negatives are only exhaustive
statements about the supplied 15,800-member population, the nonempty replacement sizes
`{4,6,7,8,9,10}` (with size five separately certified empty), the fixed 192-piece additive
GF(2) ansatz, and the declared 48-element action.

- **N1 — alternative routes.** Six routes are explicit: the full unordered-pair census;
  collapse to distinct exchange masks; augmented-rank consistency for reversal; direct
  odd-zero exchange certificates; containment plus dimension for the span intersection;
  and connected-component/orbit reconstruction for the support identity. The independent
  checker repeats the pair census, augmented ranks, subspace containments, charge pushforward,
  and component action. No inference is made from the absence of a solver witness.
- **N2 — wall independence.** Three walls are kept separate: the finite-model wall (one
  supplied box and charge), the geometry wall (sample incidence is necessary but not
  sufficient), and the move-window wall (replacement sizes 4 through 10 only). The exact
  separator gate closes the geometry wall for the accepted population; it does not close
  either scope wall.
- **N3 — hidden walls.** The corner-simplex class, minimum-cost restriction, labelled tick,
  four-coordinate L1 charge, characteristic-two additive weights, and 48-element action are
  all declared inputs. No claim is made for nonminimum pieces, nonlinear or nonbinary
  charges, a larger symmetry group, another cell complex, or a physical realization.
- **N4 — residual matching.** The odd-zero witnesses attack only the equations
  `weight · exchange = 1` at sizes 6, 7, 8, 9, and 10. The zero five-piece count attacks
  only the enumerated minimum-population pair census and carries no nonvacuous reversal
  claim. The constant six-plus-seven result
  attacks only additive GF(2) piece weights. No external witness is cited as closing a
  broader residual, so there is no residual mismatch to discard.
- **N5 — rhetoric audit.** The primary cache lands five explicit resolution lines. The
  per-element and per-block levels are checked. Per-site, per-mode, and lattice-wide levels
  are marked not executed with substantive reasons. Every negative below is written at the
  narrowest checked resolution.
- **N6 — partial-closure paths.** Replacement sizes 11 through 24 can be enumerated without
  a new axiom. Other additive groups or nonlinear charge classes can be posed as separate
  finite systems. Multi-cell behavior needs a supplied gluing/transport model and its own
  theorem. These are open extensions, not impossibility walls or proposed primitives.
- **N7 — steelman.** A charge may reverse all moves at an unenumerated larger size; another
  piece class or cost can change every rank; and a multi-cell transport may yield a different
  conserved quantity. None would contradict this packet because none belongs to its finite
  domain.
- **N8 — cross-cycle echo.** Cycle 733 is used only for its independently geometric finite
  population and is rechecked locally. Later move/charge cycles are context only. Their
  stronger or differently scoped negative language is not inherited, and agreement of a
  count is not treated as a proof dependency.

**Status: PASS.** Every N1 route and N2/N3 wall is named, the N4 residuals match the finite
claims, the N5 certificate lands in the canonical primary cache, and N6/N7/N8 keep all
larger routes open.

## Boundary and honest read

The pool of 192 pieces, the 120 exchanges at the smallest move and the group structure they
leave are measured by the search, not derived from a symmetry statement. They are complete
for this cell and this cost, and the note claims nothing beyond that.

The counts of moves and distinct exchanges, the ranks, and the group sizes are measurements
over an explicit finite population; none is forced by a general framework argument. This
cycle independently reconstructs the group profile and action because its new conclusion
reads the charge support against them. The durable result is that reversal is available at
four and at no other enumerated nonempty size; the four-piece span is the intersection of the six-
and seven-piece spans; the induced charge space has rank three; and the charge keeping the
smallest move is exactly one supplied-symmetry orbit of connected components.

The pair census covers replacement sizes four through ten and finds the size-five class
empty. The response theorem covers only the six nonempty sizes `{4,6,7,8,9,10}`: reversal
is available at four and at no other member of that set. Nothing is measured about moves on
eleven or more, and a larger range would need its own census. Likewise the count of 63 sets
is a count of nonempty subsets of those six nonempty sizes.

Every count here is scoped to the single cell of one lattice step and one tick, with the
adjacency cost and the least volume as defined above. No statement is made about cells of
other extent, other adjacency, other costs, or about the lattice as a whole; a claim of that
kind would need its own measurement. In particular the dimension three of the charge space,
the two sides of each charge, and the 24 groups of 236 are properties of this population of
15800 cuttings.

The charges are two valued functions on cuttings, arrived at as weights on pieces. Nothing
here identifies any of them with a physical quantity, and nothing here says any of them is
conserved by a process; each is reversed by moves of some sizes and kept by moves of others,
and the population the sizes are drawn from is fixed by the cost alone. What a space of
charges of this kind would mean for a lattice of many cells is not measured and is not
claimed.

Time enters only as the fourth column of the cell. Nothing in this cycle selects a direction
along it, and the tick flip is kept in the symmetry group throughout, so no result here
depends on an arrow.
