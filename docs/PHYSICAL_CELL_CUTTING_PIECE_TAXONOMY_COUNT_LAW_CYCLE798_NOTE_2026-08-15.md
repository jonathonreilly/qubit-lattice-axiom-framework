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
- `next_trace_action: derive a closed-form point count from the full tree data of the three-arm family; derive why every one of the 15800 cuttings carries the same ascent census 1, 11, 11 and 1; and interpret what the class-set multiplicities 2, 4, 8, 16 and 64 count; these questions are outside the exact finite target here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, on the declared finite cell, that each of the 400 kept pieces carries exactly 4 corner-adjacency edges on its 5 corners and is connected, hence is a tree, and that the degree multisets realize exactly three types with census 192, 192 and 16, each family independently rebuilt as a set of corner sets by bit-flip walks, by one-bit stars and by arm sets, and matched exactly; that the 192 pieces occurring in a cutting are exactly the chain family; that the 384 signed coordinate maps of the cell decompose the 400 kept pieces into exactly 3 orbits of sizes 16, 192 and 192 which are those same families, with each realizing all four units 1, 3, 7 and 14; that a membership description read off the tree alone agrees with the exact barycentric membership at all 625 grid points for 400 of 400 pieces; that every chain has point count comb(8 - s, 4) for the ascent count s of its effective-offset word and every hub has point count comb(8 - w, 4) for the three-axis weight w of its hub corner, so that the counts 70, 35, 15 and 5 are 5 times the units 14, 7, 3 and 1; that the 192 chain words are pairwise distinct and pair into 96 classes of 2 under the fourth-axis flip, whose fixed-chain and fixed-cutting counts are both 0; that every cutting carries 24 distinct classes and the one ascent census 1, 11, 11 and 1; and that the 24 unordered wall edges on the 12 wall letters split into exactly 2 components of 6, with the 6 within-component pairs at the smallest off-diagonal value 18 each with 4 common neighbours and the 6 cross-component pairs forming a perfect matching of all 12 wall letters; the letter lists, the three-arm unit census and the class-set multiplicities are anchored as measured, and no physical or lattice-wide identification is made`

- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object consists of the 16 corners of the unit four-cube, the 2672 five-corner
unit-determinant pieces built on them, the 400 that survive at the
adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into, the 192
pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell. Points are
counted on the generic sample grid with per-axis offsets 1, 2, 4 and 8, that is 5 values on each of
the four axes and 625 points in all, written here on the integer scale in which the cell has width
80. The pair of facet letters on the two slots of the first axis, drawn from a 16-letter alphabet,
gives the interface matrix of trace 2000, whose entries of value 36 are the wall.

The linked runner rebuilds the object, alphabet, matrix and wall before any gate runs. The two
explicit letter-pair lists at interface value 18 are output-label anchors checked only after the
wall components and their intrinsic within/cross partition have been computed. They come from the
same finite enumeration and carry no dependency on an earlier cycle artifact.

The unit four-cube, five-corner unit-determinant candidate rule, sample-grid offsets, integer width,
and choice of the first axis for the interface matrix are declared finite-domain and frame choices.
The adjacency-cost floor is then computed rather than supplied. The offsets and width are explicit
normalization/boundary conditions for the point-count identities, and the axis choice fixes only the
reported letter labels. No literature value, fitted value, observational comparator, or external
scientific input enters. Every integer below is recomputed from the corner list and these declared
choices by a standard-library-only runner with no file input, file output, or randomness.

## Exact target and proof-obligation graph

**Exact target.** For the declared 16-corner unit four-cube, the fixed 625-point grid and the
resulting finite cutting/interface construction, establish by exact exhaustive computation the
three tree families and symmetry orbits, the chain and hub point-count formulas, the chain-word and
cutting censuses, the three-arm unit census and positive equal-hub-weight witness, and the intrinsic
wall-component partition stated below.

| obligation | status in this note | discharge |
|---|---|---|
| Rebuild the complete finite domain and all cuttings | proved here | G1 enumerates every candidate, kept piece and exact cover. |
| Classify every kept piece and identify the used family | proved here | G2 and G3 use degree data and separate set constructions. |
| Identify the symmetry-group orbits | proved here | G4 closes the 400-piece set under all 384 maps. |
| Match tree inequalities to simplex interiors | proved here | G5 compares distinct formulas at every one of 400 × 625 cases. |
| Establish the chain and hub count formulas | proved here | G6 and G7 check each member against its exact simplex count. |
| Record the three-arm census and equal-weight witness | proved here at finite scope | G8 checks all 192 units and the two named pieces. |
| Establish the word pairing and cutting censuses | proved here | G9 checks all chains and all 15800 cuttings. |
| Establish the wall partition and its intrinsic properties | proved here | G10 computes the graph components before checking their measured labels. |

All obligation discharges are internal to the finite computation. The exact target's obligation
graph is closed. The strongest adjacent unproved statement is a closed-form point-count law for the
complete three-arm family; a structural derivation of the per-cutting ascent census and an
explanation of the class-set multiplicities are also outside the target.

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

Each orbit realizes all four units: the chain orbit has 8 pieces at unit 1, 88 at 3, 88 at 7 and 8
at 14; the three-arm orbit has 14 at 1, 82 at 3, 82 at 7 and 14 at 14; and the hub orbit has 2 at 1,
6 at 3, 6 at 7 and 2 at 14. Thus the orbit partition is strictly coarser than the unit partition.

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
  400 pieces. After the shared finite-object and grid setup, the routes use distinct formulas: the
  description path never reads or calls the barycentric inverse-matrix computation.
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

## The three-arm finite census and equal-weight witness

All 192 three-arm pieces have point count 5 times a unit of the same spectrum, with census 14 pieces
at unit 1, 82 at 3, 82 at 7 and 14 at 14. The runner records a positive finite witness at hub weight
0: the piece on corners 0, 1, 2, 4 and 9 has unit 7, while the piece on corners 0, 1, 2, 8 and 12 has
unit 14. The claim about this pair is solely its existence in the declared 192-piece family. A
closed-form count based on the full three-arm tree data remains an adjacent open question.

## The word pairing and the cuttings

- **The words pair.** The 192 chain words are pairwise distinct, and the map sending a word to its
  reversed word with each letter replaced by 16 minus it pairs them into exactly 96 classes of 2.
  The two chains of a class are each other's images under the pure fourth-axis flip, the cell map
  with the identity permutation of axes and the single flip on the axis of offset 8. Its fixed-chain
  census is 0 of 192.
- **Every cutting carries all its classes distinctly.** The fourth-axis flip permutes the 15800
  cuttings with fixed-cutting census 0, and every cutting carries 24 distinct classes. Equivalently,
  each cutting selects one member from each of its 24 classes.
- **The count law re-derives the constant profile.** Because the count law turns the ascent count
  into the unit, the enumerated unit profile is the same statement as the ascent census inside a cutting,
  and that census is 1 chain at ascent 0, 11 at 1, 11 at 2 and 1 at 3 for all 15800 cuttings. The
  totals also close: 70 plus 11 times 35 plus 11 times 15 plus 5 is 625, the whole grid.
- **The class set is many-to-one while the word set is injective.** The 15800 cuttings carry 4116
  distinct sets of 24 classes, with multiplicity census 2636 sets carried by 2 cuttings each, 936 by
  4, 336 by 8, 192 by 16 and 16 by 64. The 15800 sets of 24 words, on the other hand, are pairwise
  distinct. The class-set projection creates exactly these fibers, whose multiplicities 2, 4, 8,
  16 and 64 remain an adjacent open structure.

## The wall separator

The wall is the set of entries of the interface matrix at value 36; unordered it is a graph of 24
edges on the 12 wall letters. That graph has exactly 2 connected components, the letters 0, 4, 7,
10, 11 and 14, and the letters 2, 3, 5, 9, 12 and 13. Inside a component every letter has exactly one
non-neighbour, so each component contributes 3 non-adjacent pairs, and each component is a complete
graph on 6 letters with a perfect matching removed.

The 12 unordered letter pairs at the smallest off-diagonal value 18 acquire an intrinsic partition:
exactly 6 lie within a component and 6 cross between components. The within-component six are the
pairs 0 and 7, 2 and 13, 3 and 5, 4 and 11, 9 and 12, 10 and 14, each an antipodal pair of its
component and each with 4 common neighbours.
The cross-component six are the pairs 0 and 12, 2 and 11, 3 and 10, 4 and 13, 5 and 14, 7 and 9, and
they form a perfect matching covering all 12 wall letters. Over all 36 cross-component letter pairs
the value census is 6 pairs at 18, 24 at 52 and 6 at 90, so the matching is exactly the rare part of
the cross traffic. Connectivity in the wall graph therefore refines the interface-matrix value.

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
into 96 classes of 2, the fixed-chain census 0, the distinctness of the 24 classes in every
cutting, and the two components of the wall graph with the resulting split of the pairs at 18 are all
derived by complete enumeration over the declared object.

What is measured, not derived, at the declared finite scope: the three-arm unit census 14, 82, 82 and
14 and the positive equal-weight witness pair; the per-cutting ascent census 1, 11, 11 and 1, which
the count law converts into the enumerated unit profile and which the
distinctness of the 24 classes constrains, but which is not derived here; the class-set multiplicity
census 2636, 936, 336, 192 and 16; the identity of the wall letters and the two component lists,
which are labels of the declared alphabet and the declared point frame; and the interface values 18,
36, 52 and 90 themselves.

## Boundary and the honest auditor read

All of the above are computational identities of the declared unit four-cube object, its 400 kept
pieces, its 15800 cuttings, its 16-letter alphabet and the order-384 symmetry group of the cell. The
count law is stated for the sample grid of 625 points on the integer scale of width 80 with the
per-axis offsets 1, 2, 4 and 8; the ascent count is a function of those offsets, and nothing here
claims the law survives a different offset choice. The letter labels, the two component lists and the
two letter-pair families are stated in the labels of the declared alphabet and the declared point
frame, and are not claimed to be frame-independent. The three-arm witness asserts only that the two
named pieces have equal hub weight and distinct units in this enumeration. The candidate definition
already excludes singular five-corner sets; within it, every kept piece, every cutting and every cell
map is included, so there is no sampling degeneracy. Alternative grids, offsets, frames, cell-cutting
systems, physical or dynamical identifications, lattice-wide claims and continuum limits are outside
the target.

## Next entrance

Three questions are now sharp. The first is a closed-form count from the complete three-arm tree
data, with the named equal-weight pair serving as a finite test case. The second is the per-cutting
ascent census: the count law has turned a statement about sizes into a statement about words, so the constancy of 1, 11, 11
and 1 across all 15800 cuttings is now a purely combinatorial fact about which words can share a
cutting, and the distinctness of the 24 classes is the first constraint on it. The third is the
multiplicity ladder 2, 4, 8, 16 and 64 on the class sets: the powers of 2 and the single value 64
suggest the pairing acts on the cuttings with fixed sets of independent toggles, and identifying
those toggles would say what a class set forgets.

## Review record

- The taxonomy runs in the honest direction: the degrees classify first, the independent
  constructions run second and never read the degree classification, and the gate requires set
  equality in both directions rather than a count match.
- The membership description and the barycentric membership share the declared piece and grid setup
  and then use distinct formulas. The description path uses corner adjacency and oriented grid
  values; it never reads or calls the inverse matrices used by the barycentric path, so agreement at
  all 625 points on all 400 pieces is a genuine two-route check.
- The count law is compared against the measured point count of each piece, never fitted: the
  binomial is evaluated from the ascent count or the corner weight alone, and a single mismatch would
  fail the gate.
- The three-arm result is the positive finite witness itself: the gate requires the named pair to
  have equal hub weight and unequal unit.
- The wall split is computed from the graph alone by connected components. The explicit measured
  letter-pair lists are checked only after the within/cross partition is formed.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a commit
  cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Runner

Run the [runner](../scripts/physical_cell_cutting_piece_taxonomy_count_law_cycle798_2026_08_15.py).
The reviewed
[cache](../logs/runner-cache/physical_cell_cutting_piece_taxonomy_count_law_cycle798_2026_08_15.txt)
belongs beside it and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC`
budget, finishes in well under a minute on the reference machine, and stays far below one gigabyte.
Its final line is `TOTAL: PASS=10 FAIL=0`.
