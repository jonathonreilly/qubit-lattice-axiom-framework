# Physical cell cutting: the whole symmetry group of one wall fiber's cover instance, the refuted free involution, and the empty geometric support

Date: 2026-08-15
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
- `next_trace_action: take the membership matrix of this fiber instance over the field with two elements and hunt a parity-forcing linear functional on the 14-solution system, or refute that any such functional exists by an exact rank census; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination of the whole group of row permutations preserving one wall fiber's cover instance, of the group that group induces on the fiber's fold-held cuttings, of the free involutions among the induced elements, and of which induced elements a permutation of the sample points can carry; no physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the
unit four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive
at the adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into,
the 192 pieces occurring in at least one cutting, the 384 signed coordinate maps of the cell, and
the slot-preserving subgroup of order 96 for axis zero. The pair of tetrahedral letters on the two
slots of axis zero gives the interface matrix, of trace 2000, with exactly 48 entries equal to 36.
Each of those 48 fibers holds 36 cuttings, is held setwise by exactly 2 of the 384 maps, and its
nontrivial holder — that fiber's fold — holds 14 of the 36.
The stem `PHYSICAL_CELL_CUTTING_FOLD_INVARIANT_GLOBAL_CENSUS_CYCLE790_NOTE_2026-08-15` is not yet
on main and is referenced by name only; it reduced the 48 folds to 6 distinct maps with serving
census `{8: 6}` and derived the evenness of the sample fold's 336 held cuttings from a free
involution that pairs the served fibers across each other rather than inside any one of them,
leaving the evenness of 14 measured. Its named entrance was to hunt that carrier one level down,
on a single fiber, or refute it.

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from that object alone: it rebuilds the object from the corner
list before any gate runs, uses the standard library only, performs no file input or output and no
randomness, and gates each recomputed census against the value stated here. The composition rule
on the 384 maps is derived from the corner action and checked on 20 fixed pairs.

## The fiber instance

The sample fold is `(0,3,2,1)/15` and the fiber taken is the first one it serves, at letter pair
`(0,4)`. That fold acts freely on the 400 kept pieces, so they fall into 200 two-orbits with no
singleton and with no two-orbit whose two pieces have overlapping interiors. Each of the fiber's
14 fold-held cuttings is a union of such two-orbits, exactly 12 of them, and only 40 of the 200
two-orbits occur in any of the 14. That is the whole instance: a cover problem with 40 rows and 14
solutions, each solution a 12-subset of the rows.

The instance is far from a generic design. The occurrence census over the 40 rows — how many of
the 14 solutions each row lies in — is `{1: 6, 2: 10, 3: 2, 4: 7, 6: 9, 8: 3, 10: 3}`, whose
weighted sum 168 is 14 times 12 as it must be. Over the 91 unordered solution pairs the census of
intersection sizes is `{0: 12, 1: 6, 2: 10, 3: 14, 4: 4, 5: 14, 6: 4, 7: 5, 8: 10, 9: 1, 10: 11}`,
and since every solution has exactly 12 rows the symmetric-difference census is the mirror image
`{4: 11, 6: 1, 8: 10, 10: 5, 12: 4, 14: 14, 16: 4, 18: 14, 20: 10, 22: 6, 24: 12}`, with the
identity 24 minus twice the meet gated on every one of the 91 pairs.

## The class structure and the kernel

Two rows lying in exactly the same solutions are interchangeable for the solution system.
Grouping the 40 rows by that membership relation gives exactly 20 classes, with size
census `{1: 6, 2: 10, 3: 2, 4: 2}` summing to 40 and with the 20 membership sets pairwise
distinct. Any permutation of the rows that stays inside classes carries each solution onto itself
as a row set — the runner checks this constructively with one explicit swap inside a class of size
2 — so the group of such permutations is a kernel, and its order is the product of the class-size
factorials, 1024 times 36 times 576, that is 21233664.

## The whole symmetry group

A row permutation preserving the solution system permutes the 14 solutions, and the map to that
induced permutation has exactly the kernel above. Which permutations of the 14 are induced is
decided by a condition on classes alone: a permutation is induced exactly when carrying membership
sets through it sends the multiset of class memberships and sizes to itself. The runner runs a
complete backtracking search over all permutations of the 14, pruning only by that necessary
condition on partial images — never by comparison with any expected answer — and the search
terminates with exactly 2 survivors, the identity and one more. Both survivors are then verified
constructively by building an explicit row bijection and checking that it carries each solution's
row set onto the image solution's row set exactly.

The sole nontrivial induced element is an involution with cycle census `{1: 10, 2: 2}`: it
exchanges the solutions in two pairs and fixes the other 10. Free involutions on the 14, which
would need cycle census `{2: 7}`, number exactly 0 — not by argument but by the same complete
search, since only 2 permutations survive at all. The search is discriminating rather than
permissive: each of the survivor's two-cycles taken alone fails the class condition, so the two
exchanges must move together.

The whole group of row permutations preserving the instance therefore has order 2 times 21233664,
that is 42467328, and the induced action has order exactly 2. Squaring the nontrivial element
gives the identity, and squaring its explicit row bijection gives a map that holds every solution
setwise, so the extension is closed as stated.

This answers the named entrance of the previous cycle in the negative: no free involution exists
on this fiber's cover problem, and there is no room for one, since the induced group has order 2
and its only nontrivial element fixes 10 of the 14.

## The geometric emptiness

A weaker carrier could still survive that refutation, so the question is asked again with the
geometry attached. Each row carries a point support: the combined interior of its two
pieces inside the 625 sample points. For each point, the set of rows covering it is that point's
incidence pattern; there are exactly 68 distinct patterns and no point is left uncovered. A
permutation of the sample points realizes a row bijection only if it carries the pattern multiset
to itself under the relabelling of rows.

The runner enumerates by backtracking all class-respecting row bijections for the identity and for
the nontrivial induced element, pruning by support-size equality and by support-intersection sizes
against every previously assigned row, and applies the exact pattern-multiset test at each leaf.
For the identity there is exactly 1 survivor, and it is the identity row map. For the nontrivial
element there are 0. So of the whole order-42467328 group, exactly one element is carried by a
permutation of the sample points, and it is the one that carries nothing.

## The cell group cannot see it

The cell group gives an independent reading of the same negative. Of the 384 signed coordinate
maps, exactly 2 hold the fiber's 14 cuttings setwise, the identity and the fold itself, and each
of those induces the identity permutation on the 14 — the fold does not merely hold the set, it
holds every one of the 14 individually. So 0 of the 384 induce the nontrivial abstract element.

A native re-derivation checks that the instance is the right one. None of the fiber's other 22
cuttings is a union of two-orbits, so the 14 are exactly the fiber's cuttings visible in the
quotient. An independent exact cover over the 200 two-orbit rows on the 625 sample points yields
336 solutions of size 12, and filtering those by assembled letter pair `(0,4)` leaves 14 equal, as
piece sets, to the fold-held cuttings of the fiber — so the instance is reachable without the
cutting enumeration.

## What stays measured

The evenness of 14 is still measured, not derived. What this cycle derives is sharper than another
failure to find a carrier: on this fiber's cover instance there is nothing left to look through.
The whole symmetry group and its induced action on the 14 are known exactly, the free
involutions among the induced elements number 0, and the only geometrically carried element is the
identity. If the evenness of 14 has a carrier, that carrier is not a symmetry of the fiber's cover
instance, abstract or geometric, and the hunt has to move to a structure that is not a group
action — which is what the trace gate above names.

## Boundary and honest reading

Measured, not derived, at the declared finite scope: the 40 rows and the occurrence census over
them; the pairwise meet and symmetric-difference censuses over the 91 pairs; the 20 membership
classes and their size census; the 68 incidence patterns; the counts 336, 22 and 14 in the native
re-derivation; the holder count 2 inside the cell group; and, above all, the per-fiber count 14,
whose evenness remains measured, not derived.

Derived at the declared finite scope: the kernel order 21233664 as the product of the class-size
factorials, together with the fact that within-class permutations hold every solution; the induced
group order exactly 2 and the cycle census `{1: 10, 2: 2}` of its nontrivial element, by a
complete search over all permutations of the 14 with a necessary-condition prune, checked against
its own near misses; the count 0 of free involutions on the 14; the whole group order 42467328 and
the closure of the extension; the count 1 of geometrically carried elements and the count 0 for
the nontrivial element; the count 0 of cell-group elements inducing it; and, from these together,
that no symmetry of this fiber's cover instance can account for the evenness of 14.

All of the above are computational identities of the declared unit four-cube object, its 15800
cuttings, and the order-384 symmetry group of the cell. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

## Next entrance

Group actions on this instance are settled, so the entrance moves to linear structure. Write the
membership matrix of the 40 rows against the 14 solutions over the field with two elements and ask
whether some linear functional on the row space evaluates to a constant on all 14 solution
vectors, since such a functional would force the parity of the count directly rather than through
a pairing. An exact rank census settles it either way: either a parity-forcing functional is
exhibited, or its non-existence is proved by rank. Nothing about the outcome is claimed here.

## Reproduction

Run
[physical_cell_cutting_single_fiber_cover_rigidity_cycle791_2026_08_15.py](../scripts/physical_cell_cutting_single_fiber_cover_rigidity_cycle791_2026_08_15.py).
The reviewed cached output belongs at
[physical_cell_cutting_single_fiber_cover_rigidity_cycle791_2026_08_15.txt](../logs/runner-cache/physical_cell_cutting_single_fiber_cover_rigidity_cycle791_2026_08_15.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, finishes in
well under a minute on the reference machine, and stays far below one gigabyte. Its final line is
`TOTAL: PASS=12 FAIL=0`, and it exits nonzero if any gate fails.

## Review record and boundary

- Rows are the two-orbits of the 400 kept pieces under the stated representative fold, and
  solutions are that fiber's fold-held cuttings written as row sets. Both conventions are fixed
  before any search runs; other choices of fold or fiber give other instances, and the results are
  reported for the stated one.
- The geometric question is asked about permutations of the 625 sample points and the incidence
  structure only. The cell group does not act on the sample grid and is treated separately; the
  two negatives are independent, not one restated.
- Pattern-multiset invariance is a necessary condition for a row bijection to be carried by a
  point permutation, so a count of 0 survivors refutes carriage outright, while the single
  survivor for the identity is exhibited and checked to be the identity row map.
- The runner prints censuses, search sizes and counts; the membership matrix, the row lists and
  the solution sets are not printed, so the note quotes censuses and identities instead.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.
