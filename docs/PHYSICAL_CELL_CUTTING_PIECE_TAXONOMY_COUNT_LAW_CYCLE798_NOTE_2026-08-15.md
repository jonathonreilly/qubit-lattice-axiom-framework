# Physical cell cutting: the tree taxonomy of the pieces, the derived point-count law, and the wall separator

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
- `next_trace_action: derive a closed-form point count for the three-arm family, the one of the three piece families whose 192 members carry the units 1, 3, 7 and 14 under no known rule; derive why every one of the 15800 cuttings carries the same ascent census 1, 11, 11 and 1 rather than merely inheriting it from the landed unit profile; and read what the class-set multiplicities 2, 4, 8, 16 and 64 are counting; none of that is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, on the declared finite cell, that each of the 400 kept pieces carries exactly 4 corner-adjacency edges on its 5 corners and is connected, hence is a tree, and that the degree multisets realize exactly three types with census 192, 192 and 16, each family independently rebuilt as a set of corner sets by bit-flip walks, by one-bit stars and by arm sets, and matched exactly; that the 192 pieces occurring in a cutting are exactly the chain family; that the 384 signed coordinate maps of the cell decompose the 400 kept pieces into exactly 3 orbits of sizes 16, 192 and 192 which are those same families, each carrying all four units 1, 3, 7 and 14 so that the unit is constant on no orbit; that a membership description read off the tree alone agrees with the exact barycentric membership at all 625 grid points for 400 of 400 pieces; that every chain has point count comb(8 - s, 4) for the ascent count s of its effective-offset word and every hub has point count comb(8 - w, 4) for the three-axis weight w of its hub corner, so that the counts 70, 35, 15 and 5 are 5 times the units 14, 7, 3 and 1; that the 192 chain words are pairwise distinct and pair into 96 classes of 2 under the fourth-axis flip, which fixes no chain and permutes the 15800 cuttings with none fixed; that every cutting carries 24 distinct classes and the one ascent census 1, 11, 11 and 1; and that the 24 unordered wall edges on the 12 wall letters split into exactly 2 components of 6 which separate the two landed letter-pair families at the smallest off-diagonal value 18, the 6 within-component pairs each with 4 common neighbours and the 6 cross-component pairs forming a perfect matching of all 12 wall letters; the letter lists, the three-arm unit census and the class-set multiplicities are anchored as measured, and no physical or lattice-wide identification is made`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the unit
four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive at the
adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into, the 192
pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell. Points are
counted on the generic sample grid with per-axis offsets 1, 2, 4 and 8, that is 5 values on each of
the four axes and 625 points in all, written here on the integer scale in which the cell has width
80. The pair of facet letters on the two slots of the first axis, drawn from a 16-letter alphabet,
gives the interface matrix of trace 2000, whose entries of value 36 are the wall.

The previous cycle, whose note is `PHYSICAL_CELL_CUTTING_LETTER_ACTION_ORBIT_CENSUS_CYCLE797_NOTE_2026-08-15.md`,
counted three things it could not explain. Every kept piece has a point count of exactly 5 times a
unit drawn from the spectrum 1, 3, 7 and 14; every one of the 15800 cuttings realizes the single unit
profile 1, 11, 11 and 1; and the smallest off-diagonal interface value 18 is carried by two families
of 6 unordered letter pairs each that the matrix value itself cannot tell apart. This cycle asks why,
and answers the first and the third. Nothing from the previous cycle is assumed: the object, the
alphabet, the matrix and the wall are all rebuilt by the linked runner before any gate runs, and the
previous cycle's two letter-pair lists enter only as comparison targets, pinned in the source and
never read by the code that forms the split.

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from the corner list alone: it uses the standard library only,
performs no file input or output and no randomness, and gates each recomputed value against the value
stated here.

## The taxonomy of the pieces

- **Every kept piece is a tree on its five corners.** Join two corners of a piece when they differ in
  a single coordinate. Each of the 400 kept pieces then carries exactly 4 such edges and is
  connected, which for 5 vertices is exactly the statement that the piece is a tree. This is not an
  extra hypothesis about the pieces; it is a consequence of the unit-determinant condition together
  with the adjacency cost floor 6, and the runner checks it for all 400.
- **There are exactly three trees, and their census is 192, 192 and 16.** Sorting the five degrees of
  a piece gives only three multisets: 1, 1, 2, 2 and 2, the chain, a path through all five corners;
  1, 1, 1, 2 and 3, the three-arm, a corner of degree 3 with two single-step arms and one two-step
  arm; and 1, 1, 1, 1 and 4, the hub, a corner joined to all four of its one-bit neighbours. No
  fourth type occurs, and no piece falls outside the three.
- **Each family is rebuilt from scratch and matches exactly.** The chains are built as bit-flip
  walks: from each of the 16 start corners, in each of the 24 orders of the four axes, flip one bit
  per step; the 384 walks give exactly 192 distinct corner sets. The hubs are built as the 16 one-bit
  stars. The three-arms are built by choosing a corner, an excluded axis and an extending axis among
  the remaining three, giving 192 sets. All 400 constructed sets are kept pieces, and family by
  family the constructed sets equal the sets found by degree. The classification therefore does not
  depend on reading the degrees at all.
- **The used pieces are exactly the chains.** A kept piece occurs in at least one cutting if and only
  if its tree is a path: the 192 used pieces and the 192 chains are the same set of corner sets, 192
  of 192. The three-arms and the hubs are kept by the cost floor and then never used.

## The families are the cell-group orbits

The 384 signed coordinate maps of the cell carry kept pieces to kept pieces, and they decompose the
400 into exactly 3 orbits, of sizes 16, 192 and 192. Those orbits are the three families: orbit and
family agree as sets, one family at a time. So the taxonomy is not a bookkeeping convenience but the
orbit decomposition of the symmetry of the cell, and the fact that only chains are used says that
being used is a property of the whole orbit.

The unit is not a function of the orbit. Each orbit carries all four units: the chain orbit with
census 1 unit at 8 pieces, 3 at 88, 7 at 88 and 14 at 8; the three-arm orbit with 1 at 14, 3 at 82, 7
at 82 and 14 at 14; the hub orbit with 1 at 2, 3 at 6, 7 at 6 and 14 at 2. The unit is therefore
constant on no orbit, so no argument from the cell symmetry alone can fix it, and whatever explains
the spectrum has to be a property of the individual piece.

## The description and the count law

- **A description read off the tree alone reproduces membership at every grid point.** For a point
  and an axis, write the oriented coordinate as the point value on that axis when the corner bit is
  zero, and as 80 minus that value when the bit is one. A chain is then the set of points on which
  the oriented coordinates taken along the walk are strictly decreasing, with the first below 80 and
  the last above 0. A hub at a corner is the set of points on which the four oriented coordinates at
  that corner sum to less than 80. A three-arm with hub corner c, mid corner m and axes d and e is
  the set on which the three oriented coordinates at c on the axes other than d sum to less than 80,
  while the oriented coordinate on axis e at c exceeds the oriented coordinate on axis d at m, which
  is itself above 0. The runner builds each piece's membership set from this description alone and
  compares it with the exact barycentric membership at all 625 grid points: they agree for 400 of
  400 pieces. The two routes share no code, and the description route never reads the barycentric
  inverse matrices.
- **The chain count is a binomial coefficient of the ascent count.** Walking a chain from its
  smaller-indexed end, each step lies on some axis and either raises or lowers that coordinate bit;
  give the step the axis offset when the bit rises and 16 minus that offset when it falls. The four
  steps give the effective-offset word of the chain, and the description above becomes a strictly
  decreasing selection of one grid value per step, one from each of four arithmetic progressions
  whose residues are the letters of that word. The count depends on the word only through its ascent
  count s, the number of adjacent places where the word increases, and it equals comb(8 - s, 4). The
  runner verifies this for every one of the 192 chains, and the ascent census is 8 chains at 0, 88 at
  1, 88 at 2 and 8 at 3.
- **This derives both the quantum and the spectrum.** The four values the law can take are
  comb(8, 4) = 70, comb(7, 4) = 35, comb(6, 4) = 15 and comb(5, 4) = 5, which are 5 times 14, 7, 3
  and 1. The factor 5 and the four-value spectrum are therefore consequences of the count law, not
  observations about the pieces, and the same law gives each chain's own unit rather than only the
  set of possible units.
- **The hubs obey the same law with a different exponent.** For a hub the description is a single sum
  below 80, and the count is comb(8 - w, 4) where w is the number of set bits of the hub corner on
  the first three axes. The axis whose offset is 8 is invisible to w, because 16 minus 8 is again 8,
  so its two directions carry the same effective offset. All 16 hubs obey this, with weight census 2
  hubs at 0, 6 at 1, 6 at 2 and 2 at 3.

## The three-arm family stays measured

All 192 three-arm pieces have point count 5 times a unit of the same spectrum, with census 14 pieces
at unit 1, 82 at 3, 82 at 7 and 14 at 14. No closed form is given here, and the obvious candidate is
ruled out: the weight of the hub corner does not determine the unit. The runner prints a witness
pair at hub weight 0, the piece on corners 0, 1, 2, 4 and 9 with unit 7 against the piece on corners
0, 1, 2, 8 and 12 with unit 14. So no function of the hub corner alone can carry the law for this
family, and the gate fails if no such witness exists, which keeps the openness of the question a
tested statement rather than a silence.

## The word pairing and the cuttings

- **The words pair.** The 192 chain words are pairwise distinct, and the map sending a word to its
  reversed word with each letter replaced by 16 minus it pairs them into exactly 96 classes of 2.
  The two chains of a class are each other's images under the pure fourth-axis flip, the cell map
  with the identity permutation of axes and the single flip on the axis of offset 8. That map fixes
  no chain, 0 of 192.
- **Every cutting carries all its classes distinctly.** The fourth-axis flip permutes the 15800
  cuttings and fixes none of them, and every cutting carries 24 distinct classes, so no cutting ever
  contains a chain together with its fourth-axis flip image.
- **The count law re-derives the constant profile.** Because the count law turns the ascent count
  into the unit, the landed unit profile is the same statement as the ascent census inside a cutting,
  and that census is 1 chain at ascent 0, 11 at 1, 11 at 2 and 1 at 3 for all 15800 cuttings. The
  totals also close: 70 plus 11 times 35 plus 11 times 15 plus 5 is 625, the whole grid.
- **The class set forgets the cutting, the word set does not.** The 15800 cuttings carry only 4116
  distinct sets of 24 classes, with multiplicity census 2636 sets carried by 2 cuttings each, 936 by
  4, 336 by 8, 192 by 16 and 16 by 64. The 15800 sets of 24 words, on the other hand, are pairwise
  distinct, so it is exactly the pairing that loses the cutting, and the multiplicities 2, 4, 8, 16
  and 64 are a further structure this note does not explain.

## The wall separator

The wall is the set of entries of the interface matrix at value 36; unordered it is a graph of 24
edges on the 12 wall letters. That graph has exactly 2 connected components, the letters 0, 4, 7,
10, 11 and 14, and the letters 2, 3, 5, 9, 12 and 13. Inside a component every letter has exactly one
non-neighbour, so each component contributes 3 non-adjacent pairs, and each component is a complete
graph on 6 letters with a perfect matching removed.

This separates what the matrix value could not. The 12 unordered letter pairs at the smallest
off-diagonal value 18 split into exactly 6 within a component and 6 across, and the split reproduces
the two landed families exactly. The within-component six are the pairs 0 and 7, 2 and 13, 3 and 5, 4
and 11, 9 and 12, 10 and 14, each an antipodal pair of its component, each with 4 common neighbours.
The cross-component six are the pairs 0 and 12, 2 and 11, 3 and 10, 4 and 13, 5 and 14, 7 and 9, and
they form a perfect matching covering all 12 wall letters. Over all 36 cross-component letter pairs
the value census is 6 pairs at 18, 24 at 52 and 6 at 90, so the matching is exactly the rare part of
the cross traffic. The degeneracy of the previous cycle is therefore a degeneracy of the value only:
connectivity in the wall graph is a strictly finer invariant, and it tells the two families apart.

## Derived versus measured

Derived at the declared finite scope. That every kept piece is a tree is derived by checking the edge
count and the connectivity at all 400, not sampled. That there are exactly three families is derived
by the degree multiset over all 400, and the family membership is derived a second time by
independent construction, with set equality required both ways, so an anchor cannot seed a family.
That the used pieces are the chains is derived by set equality, 192 of 192. The orbit decomposition
is derived by closure under all 384 maps and compared with the families only after being formed. The
inequality description is derived in the strong sense that it is verified against the exact
barycentric membership at every one of the 625 points for every one of the 400 pieces, with no
sampling and no tolerance. The chain law comb(8 - s, 4) and the hub law comb(8 - w, 4) are derived in
the same sense, piece by piece over the 192 chains and the 16 hubs, and with them the factor 5 and
the four units 1, 3, 7 and 14 stop being observations and become consequences. The pairing of words
into 96 classes of 2, the vanishing of the fixed chains, the distinctness of the 24 classes in every
cutting, and the two components of the wall graph with the resulting split of the pairs at 18 are all
derived by complete enumeration over the declared object.

What is measured, not derived, at the declared finite scope: the three-arm unit census 14, 82, 82 and
14, for which no closed form is offered and only the negative result stands; the per-cutting ascent
census 1, 11, 11 and 1, which the count law converts into the landed unit profile and which the
distinctness of the 24 classes constrains, but which is not derived here; the class-set multiplicity
census 2636, 936, 336, 192 and 16; the identity of the wall letters and the two component lists,
which are labels of the declared alphabet and the declared point frame; and the interface values 18,
36, 52 and 90 themselves. The witness pair at hub weight 0 is a measured exhibit, and it is used only
to refute a candidate rule, never to support one.

## Boundary and the honest auditor read

All of the above are computational identities of the declared unit four-cube object, its 400 kept
pieces, its 15800 cuttings, its 16-letter alphabet and the order-384 symmetry group of the cell. The
count law is stated for the sample grid of 625 points on the integer scale of width 80 with the
per-axis offsets 1, 2, 4 and 8; the ascent count is a function of those offsets, and nothing here
claims the law survives a different offset choice. The letter labels, the two component lists and the
two letter-pair families are stated in the labels of the declared alphabet and the declared point
frame, and are not claimed to be frame-independent. The negative result for the three-arm family is a
refutation of one named candidate, the hub-corner weight, and says nothing about other candidate
rules. No physical, dynamical, or lattice-wide identification is claimed, no continuum limit is
taken, and nothing here is asserted about cell-cutting systems outside the declared object.

## Next entrance

Three questions are now sharp. The first is the three-arm law: two of the three families have a
binomial count law read off the tree, the third does not, and the witness shows the missing rule must
see more of the piece than its branch corner. The second is the per-cutting ascent census: the count
law has turned a statement about sizes into a statement about words, so the constancy of 1, 11, 11
and 1 across all 15800 cuttings is now a purely combinatorial fact about which words can share a
cutting, and the distinctness of the 24 classes is the first constraint on it. The third is the
multiplicity ladder 2, 4, 8, 16 and 64 on the class sets: the powers of 2 and the single value 64
suggest the pairing acts on the cuttings with fixed sets of independent toggles, and identifying
those toggles would say what a class set forgets.

## Review record

- The taxonomy runs in the honest direction: the degrees classify first, the independent
  constructions run second and never read the degree classification, and the gate requires set
  equality in both directions rather than a count match.
- The membership description and the barycentric membership are computed by disjoint code paths. The
  description path uses only the corner adjacency of the piece and the grid values; it never touches
  the inverse matrices used by the barycentric path, so agreement at all 625 points on all 400 pieces
  is a genuine two-route check.
- The count law is compared against the measured point count of each piece, never fitted: the
  binomial is evaluated from the ascent count or the corner weight alone, and a single mismatch would
  fail the gate.
- The negative result for the three-arm family is gated positively: the gate requires an explicit
  witness pair with equal hub weight and unequal unit, so it fails if the candidate rule were in fact
  correct.
- The wall split is computed from the graph alone by connected components. The previous cycle's two
  letter-pair lists are pinned in the source as comparison targets and are never read by the code
  that forms the components or the split.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a commit
  cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Reproduction

Run the [runner](../scripts/physical_cell_cutting_piece_taxonomy_count_law_cycle798_2026_08_15.py).
The reviewed
[cache](../logs/runner-cache/physical_cell_cutting_piece_taxonomy_count_law_cycle798_2026_08_15.txt)
belongs beside it and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC`
budget, finishes in well under a minute on the reference machine, and stays far below one gigabyte.
Its final line is `TOTAL: PASS=10 FAIL=0`.
