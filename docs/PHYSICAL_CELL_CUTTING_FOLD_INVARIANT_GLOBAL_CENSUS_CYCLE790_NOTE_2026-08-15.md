# Physical cell cutting: the six folds, the fold-invariant global census, and the first derived evenness on the interface wall

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
- `next_trace_action: hunt a free involution on the cover problem of a single wall fiber, so that the parity carrier found here at the global level reaches one fiber, or refute its existence by the same style of centralizer census; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact fold census over the whole cell group, the global fold-invariant count with its letter-pair decomposition, a free involution that pairs that count, the persistence of per-fiber rigidity, and a native quotient enumeration reproducing the same set; no physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the
unit four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 pieces that
survive at the adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400
assemble into, the 192 pieces that occur in at least one cutting, the 384 signed coordinate maps
of the cell, and the slot-preserving subgroup of order 96 that holds the two boundary three-cubes
of axis zero as a pair. Each cutting dissects each boundary three-cube into a tetrahedral pattern;
exactly 16 such patterns occur, the same 16 on each of the 8 slots, split as 12 light letters of
slot multiplicity 862 and 4 heavy letters of multiplicity 1364. Reading the pair of letters on the
two slots of axis zero gives the interface matrix, whose trace is 2000 and which has exactly 48
entries equal to 36. Each of those 48 fibers holds 36 cuttings, every interface entry is even, and
that evenness has never been derived.

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from that object alone: it rebuilds the whole object from the
corner list before any gate runs, uses the standard library only, performs no file input or
output, uses no randomness, and gates each recomputed census against the value stated here, so
that a wrong object would fail rather than pass quietly. The composition rule on the 384 maps is
not assumed either: the runner derives it from the action on corners and checks it on 20 fixed
pairs against composition of the corner maps themselves before any group argument is used.

## The six folds

The previous cycle worked one fiber at a time. It showed that each of the 48 wall fibers is held
setwise by exactly 2 of the 384 maps, the identity and one nontrivial map called that fiber's
fold, and that the fold holds 14 of the fiber's 36 cuttings. Counting the folds as elements of the
cell group rather than as attributes of fibers collapses the picture. The 48 folds are only 6
distinct maps, and the serving census is exactly `{8: 6}`: each of the 6 serves 8 fibers.

The 6 are `(0,1,3,2)/3`, `(0,1,3,2)/15`, `(0,2,1,3)/9`, `(0,2,1,3)/15`, `(0,3,2,1)/5` and
`(0,3,2,1)/15`, written as a permutation of the four axes followed by the sign mask. Their shape
is uniform and gated: every one holds axis 0 and swaps two of the axes 1 2 3, each of the three
swaps carries exactly 2 masks, every mask is side-swapping on axis 0, and every mask agrees on the
two swapped axes. Nothing about the wall was used to select them; they fall out of the setwise
stabilizer computation run over the whole group of 384.

## The global census

Take the sample fold `(0,3,2,1)/15` and ask what it holds in the whole cell, not in one fiber. It
holds 336 of the 15800 cuttings. Sorted by the interface entry of the cutting, the held count
splits as `{36: 112, 100: 92, 104: 36, 200: 96}`, and the 336 sit on exactly 16 ordered letter
pairs with per-pair count census `{10: 2, 14: 8, 18: 2, 36: 2, 48: 2}`. The 8 wall fibers this
fold serves contribute 14 each, so the wall supplies 112 of the 336 and no more. The remaining 5
of the 6 folds give the identical total 336 and the identical entry census.

The 224 held cuttings outside the wall are not scattered. They sit on 8 letter pairs: the pairs
`(1,1)` and `(15,15)` at interface entry 200 with 48 each, the pairs `(3,3)` and `(14,14)` at
entry 100 with 36 each, the pairs `(5,5)` and `(10,10)` at entry 100 with 10 each, and the pairs
`(6,8)` and `(8,6)` at entry 104 with 18 each, so the remainder splits as 96 plus 72 plus 20 plus
36. Every per-pair count in the whole census is even, the wall's 14 included.

## The derived evenness

The centralizer of the sample fold inside the cell group has order 32, is closed under
composition, contains 16 members that hold axis 0, and every one of its 32 members carries the
336 held cuttings onto themselves. Its orbits on the 336 number 31, with size census
`{4: 4, 8: 14, 16: 13}`.

Inside that centralizer sits the axis-0 side flip: the identity permutation with mask 1, the map
that exchanges the two boundary three-cubes and leaves every other axis alone. It commutes with
all 6 folds, so it acts on the held set of each of them. On the 336 it has no fixed cutting at
all, and its cycle census there is `{2: 168}`. A fixed-point-free involution on a finite set pairs
that set, so the global fold-invariant count is even because it is 2 times 168, and not because it
was measured to be. This is the first evenness on this wall that is derived rather than read off.
It is derived at the global level only.

The side flip is not alone but it is not generic either: of the 32 centralizer members, 12 hold no
cutting of the 336, and of those 12 exactly 4 act as pure two-cycles with census `{2: 168}`. The
carrier is a small, named, structurally identified subset of the centralizer.

## What stays measured

The per-fiber count 14 is untouched by this. The evenness of 14 is itself measured, not derived,
and nothing here removes that gap. The global pairing is a pairing of the 336, and the wall's
contribution to the 336 is 112 spread across 8 fibers, so an even global total is consistent with
any split of 112 into 8 parts. The reduction the previous cycle proved, that a fiber's 36 is even
if and only if its 14 is even, still ends at a measured integer.

## Rigidity persists at the fiber

The fiber-level rigidity does not weaken when the group is enlarged to the centralizer. Of the 32
centralizer members, exactly 2 hold the sample fiber's 14 held cuttings setwise: the identity and
the fold itself. The 16 axis-0 members do carry that 14-set onto the 14-sets of the 8 served
fibers, and each of the 8 is hit exactly 2 times, so the eight 14-sets form one orbit and are
interchangeable, but no member of the centralizer acts inside a single one of them.

The side flip is the sharp case. It pairs the 8 served fibers as `(0,4)-(4,0)`, `(2,9)-(9,2)`,
`(7,11)-(11,7)` and `(12,13)-(13,12)`, four two-cycles with no fiber held. That is exactly why the
derived global evenness does not descend: the free involution moves each fiber to a different
fiber, so it certifies that the eight 14-values are equal in pairs, which was already known, and
says nothing about the parity of any one of them. On letter pairs the same map holds only 6 of the
16, namely `(1,1)`, `(3,3)`, `(5,5)`, `(10,10)`, `(14,14)` and `(15,15)`; each of those 6 has an
even held count and the flip is free on it, and every one of the 6 lies outside the wall.

## The quotient enumeration

The fold acts freely on the 400 kept pieces, so they fall into 200 two-orbits with no singleton,
and no two-orbit has two pieces whose interior sample points overlap. A fold-invariant cutting is
therefore exactly a selection of two-orbits whose interiors partition the cell. Running a native
exact cover over those 200 two-orbit rows on the 625 interior sample points, with no reference to
the enumeration of cuttings at all, yields 336 solutions, each of size 12. As sets of pieces those
336 solutions are equal to the 336 cuttings the fold holds, and their letter-pair distribution is
the same 16 pairs with the same count census `{10: 2, 14: 8, 18: 2, 36: 2, 48: 2}`.

This matters because it is a different counting problem, not a filter of the old one. The named
next entrance of the previous cycle asked whether the fold-invariant cuttings could be counted
natively in the quotient; they can, at half the row count and half the selection size, and the
two readings agree on every census the runner checks.

## Boundary and honest reading

Measured, not derived, at the declared finite scope: the reduction of the 48 folds to 6 distinct
maps and the serving census `{8: 6}`; the axis and mask shape of the 6; the global held count 336
and its entry census; the 16 letter pairs and the per-pair census; the decomposition of the 224
non-wall held cuttings; the centralizer order 32 and its orbit census `{4: 4, 8: 14, 16: 13}` on
the 336; the free-member count 12 and the pure two-cycle count 4; the rigidity value 2 at a single
fiber and the hit count 2 per served fiber; the four fiber two-cycles of the side flip and its 6
held letter pairs; the quotient solution count 336 with its size 12; and, above all, the per-fiber
count 14, whose evenness remains measured, not derived.

Derived at the declared finite scope: the evenness of the global fold-invariant count, since the
side flip commutes with every fold, carries the held set onto itself, and fixes none of the 336, so
that set is paired and its size is 2 times 168; the equivalence of a fold-invariant cutting with a
selection of 12 two-orbits partitioning the cell, which makes the quotient count native rather
than derivative; and the failure of the global pairing to reach one fiber, since the side flip
moves each of the 8 served fibers to a different one.

All of the above are computational identities of the declared unit four-cube object, its 15800
cuttings, and the order-384 symmetry group of the cell. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

## Next entrance

The parity carrier has been found, and it is one axis too coarse. The entrance is to look for the
same kind of carrier one level down: a free involution on the cover problem of a single wall
fiber, acting on the 14 fold-invariant cuttings of that fiber alone rather than on the 336. The
quotient enumeration above supplies the arena, since a fiber's 14 are now a sub-problem of a
cover over two-orbits, and the centralizer census supplies the method, since the same style of
count settles whether such a carrier can exist at all. Either it is exhibited, or it is refuted by
census exactly as the 12 free members were counted here. Nothing about the outcome is claimed in
this note.

## Reproduction

Run
[physical_cell_cutting_fold_invariant_global_census_cycle790_2026_08_15.py](../scripts/physical_cell_cutting_fold_invariant_global_census_cycle790_2026_08_15.py).
The reviewed cached output belongs at
[physical_cell_cutting_fold_invariant_global_census_cycle790_2026_08_15.txt](../logs/runner-cache/physical_cell_cutting_fold_invariant_global_census_cycle790_2026_08_15.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, finishes in
well under a minute on the reference machine, and stays far below one gigabyte. Its final line is
`TOTAL: PASS=12 FAIL=0`, and it exits nonzero if any gate fails.

## Review record and boundary

- Held-cutting counts are attached to ordered letter pairs throughout: the pair of a cutting is
  its letter on the first slot of axis zero followed by its letter on the second. The side flip
  acts on such a pair by exchanging the two slots and mapping each letter, so a pair held by the
  flip is one that is symmetric under that combined action. Other pair conventions give other
  stable counts; the results are reported for the stated one.
- Results are reported for the stated sample fold, and the gate that repeats the global count for
  all six carries the other five. The fiber-level statements are made at one served fiber and
  extended by the orbit statement, which is itself gated rather than assumed.
- The runner prints censuses and the six folds; the fiber membership lists, the interface matrix
  and the solution sets are deliberately not printed, so the note quotes their censuses and the
  identities between them instead.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- The sibling stem `PHYSICAL_CELL_CUTTING_INTERFACE_FREE_FOLD_REDUCTION_CYCLE789_NOTE_2026-08-14`
  is not yet on main and is referenced by name only.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.
