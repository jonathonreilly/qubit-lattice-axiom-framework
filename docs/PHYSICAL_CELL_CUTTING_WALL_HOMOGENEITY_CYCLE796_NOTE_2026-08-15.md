# Physical cell cutting: wall homogeneity, the fold as entry stabilizer, and the frame-stable class split

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
- `next_trace_action: read the letter level of the interface matrix directly — why the 48 entries of value 36 are the letter pairs they are, why the acting maps move an entry between the light, middle and heavy classes of union size while the class sizes stay put, and where the union values 50, 100 and 175 come from as multiples of 25; none of that is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, on the declared finite cell, of which of its 384 signed coordinate maps carry the wall of the interface matrix to itself — exactly the 96 that fix the first axis, with all 288 others failing — of the transitivity of that action on the 48 wall entries, of the counting identity that forces every entry stabilizer to have order 2, of the identification of that stabilizer with the entry's own fold as computed by an independent per-fiber search, of the conjugation law carrying folds along the action at all 4608 map-entry pairs, of the single conjugacy class of 6 folds each serving 8 fibers, and of the split of the 48 entries into 8 light, 32 middle and 8 heavy by the union sizes of their equal-union exchanges, together with the measured fact that this split is stable across a second generic point frame yet is not preserved by the action itself; which letter pairs carry which class is anchored as a measured list, and no physical or lattice-wide identification is made`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the unit
four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive at the
adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into, the 192
pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell. The pair
of tetrahedral letters on the two slots of the first axis, drawn from a 16-letter alphabet, gives
the interface matrix of trace 2000 with exactly 48 entries equal to 36. Each of those 48 fibers
holds 36 cuttings and is held setwise by exactly 2 of the 384 maps; its nontrivial holder is that
fiber's fold, and each fold holds 14 of its own fiber's 36 cuttings, each an exact union of 12 of
the 40 rows that the fold's 200 two-orbits contribute, with incidence kernel dimension 8 and
exactly 4 equal-union exchanges.

Earlier cycles of this lane established that per-fiber anatomy and put the 48 systems into a single
instance up to relabelling of the 40 rows; the immediately preceding stem
`physical_cell_cutting_pinned_pair_anatomy_cycle795_2026_08_15` is not yet on main and is referred
to by name only. Nothing from it is assumed here: the object, the fold table, the rows, the held
cuttings, the kernels and the exchanges are all rebuilt by the linked runner before any gate runs.

The question this note asks is a level up from the fiber. The wall — the 48 entries of value 36 —
has until now been a list of 48 separate instances that happen to look alike. Does the cell's own
symmetry group act on that list, and if so, what does the action say about the fold, which so far
has only been found by search, one fiber at a time?

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from the corner list alone: it uses the standard library only,
performs no file input or output and no randomness, and gates each recomputed value against the
value stated here.

## The law

- **Exactly 96 of the 384 maps act on the wall, and they are exactly the maps fixing the first
  axis.** For a map to act on the wall it must send each entry's 36 cuttings into the cuttings of a
  single entry of the same value. Testing all 384 maps, exactly 96 do: every one of the 96 that fix
  the first axis succeeds, and all 288 that move it fail. The identity induces the identity, and on
  all 9216 ordered pairs of acting maps the induced maps compose in the order in which the maps are
  applied. This is what makes the wall an object with a symmetry rather than a list: the acting set
  is a subgroup, and it is named intrinsically, by the axis that carries the letters, not by hand.

- **The action is transitive: the wall is homogeneous.** The 48 entries form one orbit of size 48.
  Every wall entry can be carried to every other by a symmetry of the cell, so the 48 per-fiber
  systems are not merely isomorphic as abstract incidence data — they are literally the same object
  seen from 48 positions of the cell. Everything proved at one fiber now transports to all of them
  by construction rather than by regating fiber by fiber.

- **The counting identity forces stabilizer order 2, and the stabilizer is the fold.** With 96
  acting maps and one orbit of size 48, the stabilizer of each entry has order 96 divided by 48,
  that is exactly 2, and the measured census confirms order 2 at all 48 entries. The nontrivial
  element of that stabilizer is exactly the entry's fold, at 48 of 48 entries, where the fold table
  is built by a completely separate computation: for each fiber, search all 384 maps for those
  holding the fiber setwise, which returns exactly 2 of them and their nontrivial member. What an
  earlier cycle could only measure — that each fiber is held by exactly 2 maps — this cycle derives
  from the orbit count, and the two computations agree entry by entry.

- **Folds transport by conjugation.** For every acting map and every entry, the fold of the image
  entry is the conjugate of the fold of the source entry by that map: 4608 checks, that is 96 maps
  by 48 entries, all passing, in either ordering of the map and its inverse, with each inverse found
  by search over the 384 maps rather than assumed. The fold is therefore not 48 unrelated accidents
  but a single equivariant assignment.

- **The 6 folds are one conjugacy class, each serving 8 fibers.** Only 6 distinct maps occur as
  folds, all involutions. Inside the acting 96 they form exactly one conjugacy class, and the number
  of fibers each one serves is 8 for every one of them: 48 = 6 x 8. The fold is thus a class
  function of the wall, and the wall is a homogeneous space carrying it.

- **The class split by union size is frame-stable but is moved by the action.** Each entry's 4
  equal-union exchanges have point union sizes forming a sorted four-tuple. Exactly three tuples
  occur: 8 entries are light, with sizes 50, 100, 100, 100; 32 are middle, with 100, 100, 100, 100;
  and 8 are heavy, with 100, 100, 100, 175. Within each class the full table of broken count against
  union size is single-valued, and the difference lives entirely in the exchange of broken count 2,
  whose union is 50, 100 or 175 while the other three are 100 throughout. Every union size is a
  multiple of 25. Recomputing the entire per-fiber anatomy on a second generic point frame, with
  per-axis offsets 3, 5, 6, 7 in place of 1, 2, 4, 8, reproduces the same kernel dimension 8, the
  same 4 exchanges with the same supports and the same half-splits at 48 of 48 fibers, the same
  broken-count and union-size table, and the same 8 / 32 / 8 split with the same members. Yet the
  split is not invariant under the action: a searched map carries the light entry with letter pair
  2, 12 to a middle entry, and another searched map carries the same light entry to a heavy one, in
  both cases mapping the 14 held cuttings exactly onto the 14 held cuttings of the target and
  matching exchange to exchange, with the broken-2 union going 50 to 100 in the first case and 50 to
  175 in the second while the other three stay at 100.

## Derived versus measured

Derived at the declared finite scope. The stabilizer order 2 is derived, from the acting count 96
and the single orbit of size 48, and no longer needs the per-fiber holder search; the agreement of
the derived stabilizer with the independently searched fold is a check between two computations,
neither of which reads the other's result. The conjugation law is derived in the sense that it is verified on every one of
the 4608 map-entry pairs, not sampled. The single conjugacy class and the equal service count 8
follow from transitivity together with the conjugation law, and are also measured directly. That the
class split cannot be an invariant of the abstract instance follows immediately from transitivity
plus the observed movement between classes: since all 48 entries lie in one orbit, any quantity
genuinely intrinsic to the instance must be constant across the wall, so a quantity that takes three
values is a property of how the instance sits relative to the point frame and the letter labels, not
of the instance.

What is measured, not derived, at the declared finite scope: that exactly the 96 first-axis maps act, with
288 failures — the failure of the other 288 is checked map by map, not argued; the class sizes 8, 32
and 8; which letter pairs carry which class, anchored as measured lists, the light pairs being
2 and 12, 4 and 14, 5 and 13, 7 and 11, and the heavy pairs 2 and 3, 4 and 7, 10 and 11, 12 and 13,
each pair occurring on 2 entries, once for each order of its two letters; the union values 50, 100
and 175 themselves and their common divisor 25; and the frame stability, which is established at one
additional generic frame and not proven for all frames.

All of the above are computational identities of the declared unit four-cube object, its 15800
cuttings, and the order-384 symmetry group of the cell. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

## What the wall now asks

What opened is a letter-level question that could not even be posed before. The wall is homogeneous,
so no fiber is special; the fold is equivariant, so no fold is special; and yet the letters split the
48 entries into 8, 32 and 8 in a way that survives a change of point frame while being scrambled by
the cell's own symmetry. That is exactly the signature of a quantity attached to the interface
matrix rather than to the fiber: the 48 entries of value 36 sit inside a 16-letter alphabet whose
matrix has trace 2000, and the split must be readable from that matrix. The wall now asks what the
light, middle and heavy classes are as sets of letter pairs, and why the exchange of broken count 2
is the one that carries the whole distinction.

## Next entrance

Read the interface matrix at letter level. The concrete entrance is the union values themselves:
50, 100 and 175 are 2, 4 and 7 times 25, the light and heavy classes have 8 members each against 32
in the middle, and the entire distinction is carried by a single exchange, the one with broken count
2. Worth reading next is whether the 16 letters carry a natural pairing under which the 48 entries
of value 36 are described directly, whether the light and heavy pairs are the two ends of one
letter-level statistic, and whether the factor 25 is the point frame speaking or the object. Because
the action moves entries between classes, any answer must be stated relative to the frame; because
the wall is homogeneous, any answer will hold at all 48 entries at once.

## Review record

- Rows are the two-orbits of the 400 kept pieces under each fiber's own fold, and blocks are that
  fiber's fold-held cuttings written as row sets. Both conventions are fixed before any computation
  runs, and every statement is made for all 48 fibers, not for a chosen one.
- The fold table and the wall action are computed independently. The fold table comes from a search
  over all 384 maps for those holding each fiber setwise; the stabilizers come from the induced maps
  on the 48 entries. Neither is derived from the other, so their agreement at 48 of 48 entries is a
  genuine cross-check and not a restatement.
- Inverses of acting maps are found by search over the 384 maps, and both orderings of the
  conjugation are tested, so the composition convention cannot silently carry the result.
- The transport statement is searched, not planted: the runner walks the acting maps in construction
  order and reports the first one reaching each of the other two classes out of the named light
  entry, then verifies that map by explicit image of the 14 held cuttings and of all 4 exchanges as
  frozen sets.
- The point cardinalities of the equal-union exchanges are properties of a labelling relative to the
  point frame; the runner anchors them as the full measured table over the 48 entries and repeats
  the entire per-fiber computation on a second generic frame, gating the two against each other.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a commit
  cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Reproduction

Run the [runner](../scripts/physical_cell_cutting_wall_homogeneity_cycle796_2026_08_15.py). The
reviewed [cache](../logs/runner-cache/physical_cell_cutting_wall_homogeneity_cycle796_2026_08_15.txt)
belongs beside it and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC`
budget, finishes in well under a minute on the reference machine, and stays far below one gigabyte.
Its final line is `TOTAL: PASS=10 FAIL=0`.
