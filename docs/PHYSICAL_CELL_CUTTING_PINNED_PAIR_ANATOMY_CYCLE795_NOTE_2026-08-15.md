# The pinned pair: anatomy of the two exceptional cuttings, the symmetry that fixes each of them, and the two directions outside the light span

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
- `next_trace_action: the instance's own symmetry provably cannot pair the two exceptional cuttings, so a carrier for the parity of the held count must come from structure that does not preserve the minimal exchange graph; the point-cardinality classes of the wall measured here are the nearest such structure, and their fold-by-class table is the first thing to read; no such carrier is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, at every wall fiber of the declared finite cell, of the full weight census of that fiber's own kernel, of the overlap and difference structure of its weight-four and weight-six vectors together with the span they generate, of the profile of its nine weight-eight vectors by multiplicity as a difference of held cuttings and by membership in that span, of the identification of the two exceptional cuttings by graph degree and of the two span-outside directions that emanate from the isolated one, of a derived degree lemma forbidding any shared-row-preserving bijection from exchanging the two, of a complete backtracking search whose nontrivial member fixes each exceptional cutting individually and fixes the named kernel directions as vectors on the rows, and of the equivariant split of the dominant pairing into four fixed pairs and two exchanged ones; the point cardinalities of the equal-union exchanges and their fold-by-class table are labelling-level and are anchored as measured censuses over the fibers, never as one value; no physical or lattice-wide identification`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the unit
four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive at the
adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into, the 192
pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell. The pair
of tetrahedral letters on the two slots of axis zero, drawn from a 16-letter alphabet, gives the
interface matrix of trace 2000 with exactly 48 entries equal to 36. Each of those 48 fibers holds
36 cuttings and is held setwise by exactly 2 of the 384 maps; its nontrivial holder is that fiber's
fold, and each fold holds 14 of its own fiber's 36 cuttings.

The stem `PHYSICAL_CELL_CUTTING_CLEAN_EXCHANGE_SYMMETRY_CYCLE794_NOTE_2026-08-15` is not yet on main
and is referenced by name only. It named a dominant exchange that pairs 12 of the 14 fold-held
cuttings and strands the other 2. Everything that rests on it is rebuilt here rather than assumed,
and regated at all 48 fibers: each fold cuts the 400 kept pieces into 200 two-orbits, each held
cutting is an exact union of 12 of them, exactly 40 of the 200 occur across the 14, the 625 by 40
point-row incidence over the field with two elements has rank 32 and kernel dimension 8 with all
256 kernel vectors of even weight, and each of the 672 held cuttings covers each of the 625 sample
points exactly once.

The question this note asks is what those 2 stranded cuttings are: whether the kernel around them
has any named shape, whether they are distinguishable from each other by an invariant of the
instance rather than of a labelling, and whether any symmetry of the instance pairs them — since
such a pairing would carry the evenness of 14 outright. The answer is that they are canonically
distinguishable, that no symmetry can pair them, and that the instance's entire symmetry fixes each
of them where it stands.

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from that object alone: it rebuilds the object from the corner list
before any gate runs, uses the standard library only, performs no file input or output and no
randomness, and gates each recomputed value against the value stated here.

## What is proved

- **The kernel has one weight census over the whole wall.** The kernel of a fiber's point-row
  incidence has dimension 8, and the weights of its 256 vectors read
  `{0: 1, 4: 4, 6: 1, 8: 9, 10: 5, 12: 13, 14: 16, 16: 17, 18: 30, 20: 31, 22: 44, 24: 40, 26: 24, 28: 12, 30: 7, 32: 1, 34: 1}`,
  a single distinct value over the 48 fibers, 17 weights totalling 256. The census is not unimodal
  and it is not the census of a random even-weight code of that dimension: it has exactly 4 vectors
  of weight 4, exactly 1 of weight 6, exactly 9 of weight 8, and a single vector of weight 34 far
  above the rest. Everything below reads structure off the light end of that census.

- **The light vectors span a fixed subspace of dimension four.** Among the 6 unordered pairs of the
  4 weight-4 kernel vectors exactly 1 pair overlaps, and it overlaps in exactly 1 row; the other 5
  pairs are disjoint. The overlap census is `{0: 5, 1: 1}` and the census of pairwise difference
  weights is `{6: 1, 8: 5}`, each single-valued over the 48 fibers. The one overlapping pair differs
  by the unique kernel vector of weight 6, so the weight-6 vector is not an extra object: it is the
  difference of the only two light vectors that meet. The span over the field with two elements of
  those 5 light vectors has exactly 16 members, that is dimension 4, at every fiber, and it is
  exactly half the dimension of the kernel.

- **The nine weight-eight vectors split five inside the light span and four outside.** Classify each
  weight-8 kernel vector by the ordered pair consisting of its multiplicity as a difference over the
  91 pairs of held cuttings and its membership in the light span. The census is
  `{(0,1): 3, (1,0): 2, (2,0): 2, (2,1): 2}` with 1 meaning inside, single-valued over the 48
  fibers. So 5 lie inside the light span and 4 outside; every weight-8 vector of multiplicity 0,
  that is every one that is not a difference of held cuttings at all, lies inside the span; and the
  2 vectors of multiplicity 1, the directions realized by exactly one pair of held cuttings each,
  both lie outside it. Multiplicity and span membership are independent-looking labels, and the
  census shows they are not independent.

- **The two exceptional cuttings are canonically distinguishable.** Call two held cuttings a minimal
  exchange when they share 10 of their 12 rows; as a graph on the 14 held cuttings the degree census
  is `{0: 1, 1: 4, 2: 9}` at every fiber. The dominant difference, the unique kernel vector of
  multiplicity 6, breaks exactly 2 held cuttings, and those 2 are the exceptional pair. Their graph
  degrees are 0 and 1. Degree is an invariant of the instance and not of a labelling, so the pair is
  ordered by the instance itself: one exceptional cutting is the isolated vertex, the other is an
  endpoint of a path, and there is exactly 1 vertex of degree 0 in the whole graph.

- **Both multiplicity-one weight-eight directions emanate from the isolated cutting.** The
  difference of the two exceptional cuttings has weight 8 and multiplicity 1, and the only pair of
  held cuttings realizing it is the exceptional pair itself. The other multiplicity-1 weight-8
  vector is likewise realized by exactly 1 pair, and that pair joins the degree-0 cutting to a
  cutting of degree 2. So both of the kernel's singly realized weight-8 directions have the isolated
  cutting as one endpoint: one carries it to its fellow exceptional cutting, the other to a
  degree-2 cutting. Both lie outside the light span, at 48 of 48 fibers.

- **The whole symmetry fixes each exceptional cutting individually.** The complete backtracking
  search for block-level self-equivalences of a fiber's instance against itself returns exactly 2
  elements at every fiber. Its nontrivial member is an involution whose cycle structure on the 14
  held cuttings is 10 fixed points and 2 two-cycles, and it fixes each of the 2 exceptional cuttings
  where it stands. Acting on the 40 row coordinates it fixes as vectors, not merely as a set, all 7
  named kernel directions: the 4 weight-4 vectors, the weight-6 vector, the dominant difference and
  the exceptional pair's own difference. The pinning is therefore at the level of the rows and not
  only at the level of the blocks.

- **The dominant pairing splits equivariantly as four plus two.** The dominant difference pairs the
  12 non-exceptional held cuttings into 6 pairs, each pair differing by that one vector. The
  nontrivial self-equivalence fixes 4 of those 6 pairs as sets and exchanges the remaining 2 pairs
  with each other, and its 4 moved cuttings are exactly the union of those 2 exchanged pairs. So the
  symmetry and the dominant pairing commute in the strongest available sense: the pairing is a map
  of the symmetry's orbits, and the 2 stranded cuttings sit outside both.

## The degree lemma

Let s be any bijection of the 14 held cuttings onto themselves that preserves, for every pair, the
number of rows the two cuttings share. Then s carries pairs sharing 10 of their 12 rows to pairs
sharing 10 of their 12 rows, so s is an automorphism of the minimal exchange graph and preserves the
degree of every vertex. The two exceptional cuttings have degrees 0 and 1, and the degree census
`{0: 1, 1: 4, 2: 9}` records exactly 1 vertex of degree 0, so no such s exchanges them. Every
self-equivalence of the instance is such a bijection, because it is induced by a permutation of the
40 rows and a shared-row count is a count of rows. Hence no symmetry of the instance pairs the two
exceptional cuttings — the pairing that would have carried the evenness of 14 outright cannot exist
inside the instance. This is a derivation, and the complete search confirms it constructively at all
48 fibers: the entire nontrivial symmetry fixes each of the 2 individually, and does not exchange
them.

## Derived versus measured

Derived at the declared finite scope: the degree lemma above and its consequence that no
self-equivalence of the instance exchanges the two exceptional cuttings; that the weight-6 kernel
vector is the difference of the unique overlapping pair of weight-4 vectors, once the overlap census
`{0: 5, 1: 1}` is in hand, since two weight-4 vectors meeting in exactly 1 row differ by a vector of
weight 6; and that the exceptional pair's difference is fixed as a vector by any self-equivalence
fixing both members, since a permutation of the rows commutes with the symmetric difference of two
row sets. The equivariance of the four-plus-two split follows from the row-level fixing of the
dominant difference together with the block action.

Measured, not derived, at the declared finite scope: the whole kernel weight census and every number
in it; the value 16 for the light span and the fact that its dimension is exactly half the kernel's;
the weight-8 profile `{(0,1): 3, (1,0): 2, (2,0): 2, (2,1): 2}` and, with it, the fact that both
multiplicity-1 directions lie outside the span and share the isolated cutting as an endpoint; the
self-equivalence count 2 and the cycle structure 10 fixed points with 2 two-cycles; and the count 14
itself, whose evenness remains measured, not derived, exactly as before.

The labelling level is measured, not derived, and is reported as such. The four union sizes of a
fiber's equal-union exchanges read 50 100 100 100 at 8 fibers, 100 100 100 100 at 32 and
100 100 100 175 at 8. Grouping the 48 fibers by their fold, the multiset of per-fold class censuses
is: 3 folds see only the middle class, 1 fold splits 4 light and 4 heavy, and 2 folds split 4 middle
with 2 light and 2 heavy. The 48 wall entries are closed under the swap of the two letters, with 0
diagonal entries, and each of the two extreme classes is closed under that swap on its own: the
light class is the 8 ordered entries of the unordered letter pairs (2,12), (4,14), (5,13), (7,11)
and the heavy class the 8 of (2,3), (4,7), (10,11), (12,13). Nothing here explains why the wall
splits 8, 32 and 8, why one fold carries both extremes and three carry neither, or why the extreme
classes are closed under the letter swap. Those are the measured facts and no conclusion is drawn
from them in this note; a row's point support depends on which pieces its fiber uses, so these
cardinalities are properties of a labelling, and the note treats them as an entrance rather than as
a result.

All of the above are computational identities of the declared unit four-cube object, its 15800
cuttings, and the order-384 symmetry group of the cell. No physical, dynamical, or lattice-wide
identification is claimed, no continuum limit is taken, and nothing here is asserted about
cell-cutting systems outside the declared object.

## What the wall now asks

The parity target was moved from 14 cuttings onto 2, and this cycle establishes that those 2 cannot
be moved further by anything living inside the instance. The degree lemma is a genuine obstruction,
not a failed search: any bijection preserving shared-row counts preserves graph degree, the two
exceptional cuttings carry different degrees, and so the pairing that would discharge the evenness
of 14 is not available at that level at all. The wall therefore changes shape rather than standing
where it was. It is no longer "find the involution pairing the two"; it is "find the structure that
does not preserve the minimal exchange graph and still acts on the wall".

That reframing is what makes the labelling level interesting rather than incidental. The classes
measured above are exactly of that kind: the point-cardinality class of a fiber is invisible to the
minimal exchange graph, which never looks at point counts, yet it partitions the 48 fibers 8, 32 and
8 and interacts with the folds in a way that is not constant. A map of the wall that mixes fibers of
different classes is not required to preserve degrees, and is therefore not blocked by the lemma.

## Next entrance

Read the fold-by-class table as an object in its own right. Three questions are ready to be asked
of it with the machinery already built here: whether the class of a fiber is determined by its
letter pair alone, given that both extreme classes are closed under the letter swap and consist of
4 unordered pairs each; whether the 1 fold carrying 4 light and 4 heavy fibers is distinguished
among the 6 folds by anything other than that census; and whether a map of the wall that carries a
light fiber to a heavy one exists at all inside the 384 maps of the cell, since such a map would
move point cardinalities and hence could not be an instance self-equivalence in the sense pinned
down above. None of those three is claimed here. What is claimed is that the route through the
instance's own symmetry is now fully characterised and the route through the labelling level is
open, with its first table already measured.

## Review record

- Rows are the two-orbits of the 400 kept pieces under each fiber's own fold, and blocks are that
  fiber's fold-held cuttings written as row sets. Both conventions are fixed before any computation
  runs, and every statement is made for all 48 fibers, not for a chosen one; every census is a
  multiset, never a list of row labels, and the runner gates that each takes exactly 1 distinct
  value over the 48 fibers.
- The light-vector gate is stated on invariants and not on positions: it asserts how many pairs
  overlap and in how many rows, not which sorted index positions do, so a relabelling of the rows
  cannot change what is being tested.
- The exceptional pair is identified by the exchange the dominant difference breaks, and its graph
  degrees are then read off the independently built minimal exchange graph; neither object is
  computed from the other's answer.
- The self-equivalence used in the row-level gates is built from the clean exchange's half-pairing
  and then verified by explicit image on the 14 held cuttings, on all 256 kernel vectors and on all
  256 coset members, and is required to induce the same block permutation as the complete search
  returns; both half-pairings are checked, not one.
- When testing whether the dominant pairing fixes a pair of cuttings as a set, the image pair and
  the original pair are both sorted before comparison, so an exchange within a pair is correctly
  counted as fixed rather than as moved.
- The point cardinalities of the equal-union exchanges are fiber-dependent; the runner's
  labelling-level gate is anchored to the full measured census over the 48 fibers and to the
  multiset of per-fold class censuses, never to a single sample-fiber value and never to a fold
  index, since fold indices are labelling artifacts.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a commit
  cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Reproduction

Run
[physical_cell_cutting_pinned_pair_anatomy_cycle795_2026_08_15.py](../scripts/physical_cell_cutting_pinned_pair_anatomy_cycle795_2026_08_15.py).
The reviewed cached output belongs at
[physical_cell_cutting_pinned_pair_anatomy_cycle795_2026_08_15.txt](../logs/runner-cache/physical_cell_cutting_pinned_pair_anatomy_cycle795_2026_08_15.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, finishes in
well under a minute on the reference machine, and stays far below one gigabyte. Its final line is
`TOTAL: PASS=10 FAIL=0`.
