# The wall instance is one: every fiber system is a relabelling of a single coset problem

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
- `next_trace_action: name the action of the canonical instance's single nontrivial symmetry on its 14 held cuttings and read off its cycle structure on the fourteen, since a fixed-point count for an involution on the fourteen has the same parity as the fourteen itself; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, at every wall fiber of the declared finite cell, that the weight census of the fiber's kernel, the column profiles of its kernel and of its coset, and the cover and pairwise-intersection invariants of its fold-held cuttings are single-valued over the fibers; together with a complete backtracking search that exhibits an explicit relabelling of the rows carrying the sample fiber's instance onto every other fiber's instance, verified by explicit image on kernel, blocks and coset; a count of exactly two such relabellings per fiber matching the two symmetries of the sample instance; and an honest rejection of a perturbed control by the same search; no physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the
unit four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive
at the adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into,
the 192 pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell.
The pair of tetrahedral letters on the two slots of axis zero, drawn from a 16-letter alphabet,
gives the interface matrix of trace 2000 with exactly 48 entries equal to 36. Each of those 48
fibers holds 36 cuttings and is held setwise by exactly 2 of the 384 maps. Its nontrivial holder
is that fiber's fold; the 48 folds are involutions and collapse to 6 distinct maps with serving
census `{8: 6}`, and each fold holds 14 of its own fiber's 36 cuttings.

The stem `PHYSICAL_CELL_CUTTING_FIBER_LINEARIZATION_LAW_CYCLE792_NOTE_2026-08-15` is not yet on
main and is referenced by name only. It put every fiber into linear form: each fold cuts the 400
kept pieces into 200 two-orbits, each of a fiber's 14 fold-held cuttings is an exact union of 12
of them, exactly 40 of the 200 occur across the 14, the 625 by 40 point-row incidence over the
field with two elements has rank 32 and kernel dimension 8 with all 256 kernel vectors of even
weight, and the 13 differences of the held vectors from the first lie in that kernel and span it,
so the affine hull of the 14 is the whole 256-element coset of the all-ones system. Everything in
that list is recomputed here rather than assumed, and regated as G3, with the span statement
regated in a sharper set-level form as G7. The previous cycle also found the weight census of the
coset to be the same at all 48 fibers, with its 14 minimum-weight members exactly the 14 held
cuttings; that census is carried by name here and is not recomputed by this runner.

The question this note asks is whether the 48 per-fiber systems, already known to carry one
coset weight census while being 48 pairwise-distinct labelled objects, are one instance carried
in 48 different labellings of its 40 rows. If they are, the parity question the lane is chasing
stops being a question about 48 systems and becomes a question about one.

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from that object alone: it rebuilds the object from the corner
list before any gate runs, uses the standard library only, performs no file input or output and no
randomness, and gates each recomputed value against the value stated here.

## The law

- **The further invariants are single-valued.** Beyond the coset weight census, four more
  invariants take exactly 1 distinct value over the 48 fibers. The weight census of the kernel
  itself is `{0: 1, 4: 4, 6: 1, 8: 9, 10: 5, 12: 13, 14: 16, 16: 17, 18: 30, 20: 31, 22: 44,
  24: 40, 26: 24, 28: 12, 30: 7, 32: 1, 34: 1}`, of total 256. Each of the 40 coordinates is 1 on
  exactly 128 of the 256 kernel vectors and on exactly 128 of the 256 coset members, so both
  column profiles are `{128: 40}` at every fiber. The 14 held cuttings have per-coordinate cover
  profile `{1: 6, 2: 10, 3: 2, 4: 7, 6: 9, 8: 3, 10: 3}` of total incidence 168, which is 14
  times 12, and pairwise support-intersection census `{0: 12, 1: 6, 2: 10, 3: 14, 4: 4, 5: 14,
  6: 4, 7: 5, 8: 10, 9: 1, 10: 11}` over the 91 pairs.

- **The equivalence is real, not inferred from the invariants.** A complete backtracking search,
  which can and does return NOT FOUND, finds for the sample fiber against every one of the other
  47 an explicit bijection of the 40 coordinates. Each is verified not by invariant matching but
  by explicit image: all 256 kernel vectors of the sample map onto the target's 256 kernel
  vectors as a set, the 14 held cuttings map onto the target's 14, and all 256 coset members map
  onto the target's 256. All three set equalities hold at 47 of 47.

- **The count is 2.** Enumerating every equivalence rather than the first gives exactly 2 for
  each of the 47 targets, and the sample instance has exactly 2 symmetries of its own, the
  identity and one nontrivial involution. The two match for the expected reason and the reason is
  checked rather than asserted: composing the nontrivial symmetry with either of a target's two
  equivalences yields the other, at all 47 targets, so composition acts freely and transitively
  on the equivalence set.

- **The control is honestly rejected.** A target built from the sample by moving one coordinate
  out of one block and another coordinate into it — the block staying at weight 12, so the object
  is still 14 blocks of weight 12 on 40 coordinates — is rejected NOT FOUND by the same search
  entry point, with the feasibility screening living inside that function so the control
  exercises the real path.

The search runs at the level of bijections of the 14 blocks, and that is licensed by a lemma
rather than by convenience. Any bijection of the coordinates carrying kernel onto kernel and
coset onto coset preserves weight, hence carries minimum-weight coset members to minimum-weight
coset members, that is, the 14 onto the 14. Conversely any bijection carrying the 14 onto the 14
carries their affine hull onto the affine hull and their difference span onto the difference
span; since the 13 differences span the kernel, the affine hull is the coset and the difference
span is the kernel, so it carries kernel onto kernel and coset onto coset. Instance equivalence
is therefore exactly equivalence of the 14-block systems, and a search over bijections of the 14
blocks — with the 40 coordinates classed by their exact membership pattern across the 14 blocks,
same-pattern coordinates interchangeable, and same-pattern classes required to meet classes of
equal size — is a complete search, whose images of kernel and of coset depend only on the block
bijection. The span fact is the previous cycle's; it is gated again here as G7 at all 48 fibers
in the sharper set-level form, 256 vectors equal to 256 vectors, not an equality of dimension 8
alone.

## What the wall now asks

The parity question descends to one canonical instance: a single set of 14 vectors of weight 12
on 40 coordinates, whose difference span is the kernel of dimension 8 in which every vector has
even weight, and whose affine hull is the distinguished coset. Every one of the 48 fibers carries
that same instance, differing only in the labelling that gives its own 40 occurring two-orbits,
drawn from the 200 its fold produces, to the 40 coordinates.
"Why is 14 even" is now a question about one instance carrying one nontrivial symmetry, not a
question about 48 systems that happen to agree; and the object in which an answer must be found
has shrunk from 48 cover problems on 400 pieces to one coset problem on 40 coordinates.

## Boundary and honest reading

Measured, not derived, at the declared finite scope: the weight census of the kernel; both of
the column profiles at 128 of 256; the cover profile and the
pairwise support-intersection census of the 14; the count 2 of equivalences and of symmetries;
and, above all, the count 14 itself, whose evenness remains measured, not derived.

Derived at the declared finite scope: that instance equivalence is exactly equivalence of the
14-block systems, by the lemma above, whose span input is regated here at all 48 fibers as a set
equality; that the sample instance is carried onto every one of the other 47 by an explicit
relabelling of the 40 coordinates, checked by explicit image on all 256 kernel vectors, the 14
blocks and all 256 coset members; that the number of such relabellings is exactly 2 at each
target and equals the number of symmetries of the sample, composition acting freely and
transitively; and that a one-block perturbation is not equivalent to the sample.

The equivalence classes say nothing yet about why the census has an even minimum-weight count.
Nothing here derives the count 14, its parity, or either census; what is established is that
there is a single object to ask the question of. All of the above are computational identities of
the declared unit four-cube object, its 15800 cuttings, and the order-384 symmetry group of the
cell. No physical, dynamical, or lattice-wide identification is claimed, no continuum limit is
taken, and nothing here is asserted about cell-cutting systems outside the declared object.

## Next entrance

Name the action of the canonical instance's single nontrivial symmetry on its 14 held cuttings.
That symmetry is now a distinguished finite object rather than one of 48 accidents, and its cycle
structure on the fourteen is the next thing to read off: a fixed-point count for an involution on
the fourteen has the same parity as the fourteen itself, so a cycle structure with a named reason
for its fixed points would carry the parity of 14 directly. Whether the reason exists is not
claimed here; what is claimed is that the target is now one involution on one set of 14.

## Review record and boundary

- Rows are the two-orbits of the 400 kept pieces under each fiber's own fold, and blocks are that
  fiber's fold-held cuttings written as row sets. Both conventions are fixed before any
  computation runs, and every invariant statement is made for all 48 fibers, not for a chosen one.
- The search is a real backtracking search over block bijections that returns NOT FOUND when no
  equivalence exists, and the control at G10 calls the same entry point and does return NOT FOUND.
  No witness is derived from its target: each witness is constructed from a found block bijection
  and then verified by explicit image on kernel, blocks and coset.
- The completeness of the block-level search rests on the lemma stated above, whose span input is
  regated at G7 as a set equality of 256 with 256 at all 48 fibers rather than carried over.
- The runner prints censuses, counts and profiles; the incidence matrices, the row lists, the
  kernel vectors and the coordinate bijections are not printed, so the note quotes censuses and
  identities instead.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Reproduction

Run
[physical_cell_cutting_wall_instance_uniqueness_cycle793_2026_08_15.py](../scripts/physical_cell_cutting_wall_instance_uniqueness_cycle793_2026_08_15.py).
The reviewed cached output belongs at
[physical_cell_cutting_wall_instance_uniqueness_cycle793_2026_08_15.txt](../logs/runner-cache/physical_cell_cutting_wall_instance_uniqueness_cycle793_2026_08_15.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, finishes in
well under a minute on the reference machine, and stays far below one gigabyte. Its final line is
`TOTAL: PASS=10 FAIL=0`, and it exits nonzero if any gate fails.
