# Physical cell cutting: the free fold reduction, full-group rigidity at the interface wall, and the quotient that sees the heavy letters

Date: 2026-08-14
Authority: none
Audit: unset
Status: proposed_retained
Claim type: bounded_theorem
Constitutional effect: none.

## Trace gate

- `trace_class: frontier_discovery`
- `target_claim_id: null`
- `target_blocker_text: null`
- `source_of_blocker_text: frontier_question`
- `reachability_to_target: unknown_frontier`
- `artifact_role: theorem`
- `next_trace_action: enumerate the folded cuttings directly in the quotient of the cell by the free involution and test whether the evenness of the folded count is forced there; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: exact stabilizer rigidity in the whole cell group, a free involution on the declared unit four-cube object, the parity reduction of the stubborn interface fibers, two refutation certificates, and the letter-functional quotient; no physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the
unit four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 pieces that
survive at the adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400
assemble into, the 192 pieces that occur in at least one cutting, the 384 signed coordinate maps
of the cell, and the slot-preserving subgroup of order ninety-six that holds the two boundary
three-cubes of axis zero as a pair. Each cutting dissects each boundary three-cube into a
tetrahedral pattern drawn from a support of 24; exactly 16 such patterns occur, the same 16 on
each of the 8 slots, split as 12 light letters of slot multiplicity 862 and 4 heavy letters of
multiplicity 1364. Reading the pair of letters on the two slots of axis zero gives the interface
matrix, whose trace is 2000 and which has exactly 48 entries equal to 36. Those 48 entries are
the wall this lane has been working against: each of the 48 fibers holds 36 cuttings, every
interface entry is even, and that evenness has never been derived.

These are finite-scope object choices, not imported physical primitives. Every integer below is
derived by the linked runner from that object alone: it rebuilds the whole object from the
corner list before any gate runs, uses the standard library only, performs no file input or
output, uses no randomness, and gates each recomputed census against the value stated here so
that a wrong object would fail rather than pass quietly.

One framing duty applies to every census below and is stated once here rather than repeated.
The 48 wall entries form a single orbit under the induced action of the side-preserving slot
maps on letter pairs, so any quantity attached to a fiber is automatically constant across the
48. Per-fiber uniformity is therefore a corollary of that transitivity, not independent
evidence; the runner nevertheless recomputes each census over all 48 fibers separately, because
the transitivity is itself one of the measured facts and should not be assumed while it is
being used.

## Stabilizer rigidity in the whole cell group

The previous cycle worked inside the slot-preserving subgroup of order ninety-six, where each
wall fiber was already known to have a setwise stabilizer of order two. The natural worry is
that this order-two answer is an artefact of having restricted the group: a larger stabilizer
in the full cell group would change what a fold can mean. It does not.

Every one of the 384 signed coordinate maps of the cell permutes the 15800 cuttings — the
runner checks bijectivity on the nose for each map and finds no defect. Computing the setwise
stabilizer of each wall fiber inside that full group gives the census {2: 48}: order exactly
two for all 48 fibers, the same order as inside the subgroup of order ninety-six. Moreover the
single nontrivial element of each stabilizer lies inside that subgroup in all 48 cases, and in
all 48 cases it is side-swapping: it exchanges the two boundary slots of axis zero. Widening
the group from ninety-six to 384 adds no element to any wall stabilizer.

This is the sense in which the fold is canonical. Each wall fiber carries exactly one
nontrivial symmetry of the cell, that symmetry reverses the two sides of the interface, and
there is no larger symmetry to be found by enlarging the group.

## The fold acts freely on the geometry

Call the nontrivial stabilizer element of a fiber its fold. The fold is free wherever it can be
tested. On corners its cycle type census is {(2, 8): 48}: eight two-orbits, no fixed corner, in
all 48 fibers. On the 400 kept pieces it fixes none — the fixed-piece census over the 48 folds
is {0: 48} — and therefore splits them into 200 two-orbits. It carries the 192 used pieces to
themselves in all 48 fibers and splits them into 96 two-orbits.

Freeness on pieces is what makes the fold useful rather than merely present. A symmetry that
fixed some pieces could act on a cutting by rearranging a fixed part and leaving a remainder,
and a fixed cutting would then carry no parity information. Here nothing at all is fixed below
the level of a whole cutting.

## The parity reduction and the sharpened wall

On its own fiber of 36 cuttings, each fold has 14 fixed cuttings and 11 two-cycles, so
36 = 14 + 2 x 11. The fixed-count census is {14: 48} and there are no longer cycles anywhere.
The congruence this yields is derived, not measured: the size of a fiber and the number of
cuttings the fold holds fixed differ by twice the number of two-cycles, so the fiber size is
even exactly when the folded count is even. The wall moves inward by that congruence — the
question "why is 36 even" becomes the strictly smaller question "why is 14 even".

The 48 folded sets are pairwise disjoint, giving 672 distinct fold-invariant cuttings across
the wall. Because the fold is free on pieces, a cutting it holds fixed cannot contain a piece
the fold fixes; the fold must instead pair the 24 pieces of that cutting among themselves. The
runner confirms exactly this over all 672 invariant cuttings: the fixed-piece census is
{0: 672} and the swapped-pair census is {12: 672}. Every fold-invariant cutting is 12 swapped
piece-pairs and nothing else.

That is the reduction the cycle buys. It replaces a statement about 36 cuttings with a
statement about 14 cuttings that each decompose into 12 disjoint pairs, and it does so by a
derived congruence rather than by a re-measurement. The evenness of 14 is itself measured, not
derived; nothing below removes that gap.

## No free element and the rigidity of the folded set

Two natural continuations of the reduction fail, and both failures are exact.

The first would be to find an element of the cell group acting on a fiber with no fixed cutting
at all — a genuinely free action, which would make the fiber size even for the plainest
possible reason. No such element exists: over all 48 fibers, the number of fibers admitting a
group element that acts without a fixed cutting is 0. The stabilizers have order two, and their
nontrivial elements always fix 14 cuttings.

The second would be to iterate: having reduced 36 to 14, look for a symmetry of the folded set
that pairs its members. On the sample fiber, exactly 2 of the 384 maps hold the 14 folded
cuttings as a set, and both of them act as the identity on those 14. Nothing in the symmetry of
the cell pairs the folded cuttings, so the reduction does not repeat. The 14 folded cuttings
between them use 80 of the used pieces, and their common part is empty, so they are not
variations on a shared core.

## Two refutations recorded as honest misses

Neither of the two most plausible mechanisms for the evenness of 14 survives.

The first candidate is a pairing by boundary frames. Reading, for each cutting, the pair of
piece sets that carry the two boundary three-cubes gives a partition of each fiber into joint
frame classes. In all 48 fibers there are 14 such classes with size multiset
[1,1,1,2,2,2,2,2,2,3,3,5,5,5], of which 8 are odd, and the fold permutes the classes with the
crosstab (4, 4, 2, 4) of held-odd, swapped-odd, held-even and swapped-even classes. The
coincidence of the two counts — 14 classes and 14 folded cuttings — invites a bijection, and
there is none: the distribution of folded cuttings per class is {0: 8, 1: 1, 2: 2, 3: 3} in all
48 fibers, so eight classes contain no folded cutting at all while one class contains three.
All 14 folded cuttings lie inside the 6 classes the fold holds, which is a genuine constraint,
but it is far weaker than a pairing.

The second candidate is an odd-degree counting argument. Build a graph on the 14 folded
cuttings of a fiber by joining two of them when their shared-piece count is exactly t, and a
second family by joining them when the shared count is at least t. Over the whole admissible
range this gives 49 distinct rules, and if any of them made every degree odd, the evenness of
14 would follow immediately from the parity of the degree sum. Every one of the 49 rules fails:
the all-degrees-odd pass count is 0 of 48 fibers for each. The best any non-tautological rule
achieves is 10 odd degrees out of 14.

One rule does pass in all 48 fibers and is excluded on principle rather than on evidence: the
at-least-zero rule, which joins every pair and therefore gives every member degree 13. That
rule has all degrees odd precisely when the number of members is even, which is the statement
it would be used to establish. Counting it as a mechanism would be circular, so it is recorded
here as tautological, excluded, and reported as such by the runner rather than silently
dropped.

## The quotient sees the heavy letters and not the wall

The final probe asks whether the alphabet itself carries the missing parity. Each of the 16
letters is a set of tetrahedral pieces drawn from a support of 24, giving a letter-tetra
incidence matrix with row sums 6 and column sums 4. Over the two-element field it has rank 10
and its left kernel has dimension 6, so there are 64 functionals vanishing on every letter's
incidence row. Evaluating all 64 on the 16 letters sorts the letters into exactly 10 types: 6
two-letter classes and 4 singletons.

The singletons are exactly the 4 heavy letters of multiplicity 1364, and the 12 light letters
of multiplicity 862 fall into the 6 pairs. Nothing in the construction of the kernel knows
about slot multiplicities, so this is a real coincidence of two independent readings of the
alphabet: a rank computation over the two-element field reproduces the heavy-light split that
the cutting count produces. The kernel is also stable under the folds — all 48 induced letter
maps carry it to itself, and they induce only 6 distinct letter maps between them — with orbit
census {1: 2, 3: 2, 4: 2, 6: 2, 12: 3} on the 64 functionals, 11 orbits, and exactly 2
functionals held pointwise by all of them.

The quotient nevertheless does not see the wall. Grouping letter pairs into orbits under the
48 side-preserving letter maps gives 12 orbits, each carrying a single interface value, and the
48 wall entries form one of them. Reading off each orbit's signature in the letter types gives
only 7 distinct signatures among the 12 orbits, and the wall signature is shared: the entry-36
orbit and the entry-52 orbit have the same signature, and so do the entry-90 and entry-100
orbits. Whatever distinguishes the wall from its neighbours in the interface reading, the
letter-functional quotient cannot express it.

## Distances inside the folded set

For orientation, the 14 folded cuttings of the sample fiber are spread out rather than
clustered. With the exchange distance of two cuttings read off from the number of pieces they
share, the census over the 91 pairs is 8:11, 12:1, 16:10, 20:5, 24:4, 28:14, 32:4, 36:14,
40:10, 44:6 and 48:12. Twelve of the 91 pairs are fully apart, sharing no piece at all.

The single nearest pair, at distance 12, shares 18 pieces, and 9 of its 12 swapped pairs
coincide, so even the two most similar folded cuttings differ in a quarter of their pairing.
Across the 14 folded cuttings only 40 distinct swapped pairs occur out of the 96 two-orbits
available on used pieces, so the folded set draws on a restricted part of the pairing structure
without concentrating on any small part of it.

## Boundary and honest reading

Measured, not derived, at the declared finite scope: the stabilizer census {2: 48} in the full
cell group; the corner cycle type {(2, 8): 48} and the free action on kept and used pieces; the
fixed-count census {14: 48}; the frame-class size multiset and crosstab; the 49 refuted counting
rules; the rank 10 and kernel dimension 6 of the incidence matrix together with the coincidence
of its 4 singleton types with the 4 heavy letters; the orbit and signature censuses of the
quotient; the distance census over the 91 pairs; and, above all, the evenness of the folded
count 14 itself, which remains measured, not derived.

Derived at the declared finite scope: the congruence 36 = 14 + 2 x 11 and with it the reduction
of the evenness of a fiber to the evenness of its folded count; the decomposition of every one
of the 672 fold-invariant cuttings into 12 swapped piece-pairs with no fixed piece, which
follows from freeness on pieces; the disjointness of the 48 folded sets; the exclusion of the
at-least-zero rule as tautological; and the constancy of every per-fiber census, which follows
from the single-orbit transitivity of the 48 wall entries.

All of the above are computational identities of the declared unit four-cube object, its 15800
cuttings, and the order-384 symmetry group of the cell. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

What the cycle buys is a strictly smaller wall and a cleaner statement of it. The evenness of
36 is no longer a bare measurement: it reduces, by a derived congruence, to the evenness of 14,
and those 14 cuttings are now known concretely as the fold-invariant ones, each a set of 12
swapped piece-pairs. What the cycle does not buy is the evenness of 14. The cell symmetry does
not pair the folded cuttings, boundary frames do not pair them, no shared-count rule makes
their degrees odd, and the letter-functional quotient cannot even separate the wall from its
neighbours.

## Next entrance

The named next entrance is direct enumeration in the quotient. Because the fold acts freely on
the 192 used pieces with 96 two-orbits, a fold-invariant cutting is exactly a selection of 12
of those two-orbits that tiles the cell, and the folded count is the number of such selections.
That is a smaller and more rigid counting problem than the one this lane has been attacking,
and it is stated entirely inside the declared object. Whether its evenness is forced there is
open; nothing about it is claimed in this note.

## Reproduction

Run
[physical_cell_cutting_interface_free_fold_reduction_cycle789_2026_08_14.py](../scripts/physical_cell_cutting_interface_free_fold_reduction_cycle789_2026_08_14.py).
The reviewed cached output belongs at
[physical_cell_cutting_interface_free_fold_reduction_cycle789_2026_08_14.txt](../logs/runner-cache/physical_cell_cutting_interface_free_fold_reduction_cycle789_2026_08_14.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, finishes
in well under a minute on the reference machine, and stays far below one gigabyte. Its final
line is `TOTAL: PASS=14 FAIL=0`, and it exits nonzero if any gate fails.

## Review record and boundary

- The runner prints censuses, cycle types, ranks and the distance value list; the interface
  matrix, the incidence matrix and the fiber membership lists are deliberately not printed, so
  the note quotes their censuses and the identities between them instead.
- The pair orbits of the letter-functional probe are taken under the side-preserving slot maps
  acting on both coordinates, and the signature of an orbit is the set of letter-type pairs it
  meets. Both choices are stated because other group and signature choices give other orbit
  counts; the blindness result is reported for the stated choice only.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- The sibling stems `PHYSICAL_CELL_CUTTING_INTERFACE_EVENNESS_ROUTES_CYCLE788_NOTE_2026-08-14`
  and `PHYSICAL_CELL_CUTTING_INTERFACE_TRANSFER_SPECTRUM_CYCLE787_NOTE_2026-08-14` are not yet
  on main and are referenced by name only.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.
