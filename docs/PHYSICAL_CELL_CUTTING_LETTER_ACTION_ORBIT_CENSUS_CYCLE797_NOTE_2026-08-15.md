# Physical cell cutting: the letter action, the orbit census of the interface matrix, and the piece-size quantum

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
- `next_trace_action: derive, from the piece geometry and the adjacency cost floor alone, why the unit spectrum of the kept pieces is 1, 3, 7, 14 and why every one of the 15800 cuttings realizes the single profile of one lightest piece, eleven of each middle size and one heaviest; and find what separates the two orbits that share the smallest off-diagonal value 18, the one degeneracy the matrix value cannot see while the action can; none of that is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: an exact determination, on the declared finite cell, that each of the 96 signed coordinate maps fixing the first axis induces exactly one pair consisting of a permutation of the 16 facet letters and a slot-swap flag while all 288 other maps induce none for either flag value, that the flag is bit zero of the map's flip mask, that the assignment is a faithful homomorphism at all 9216 ordered pairs whose permutation part has kernel of size 2 and image of order 48, that the interface matrix is symmetric and equivariant so that its 256 ordered letter pairs fall into exactly 10 orbits on which the matrix is constant, carrying the 9 distinct values 18, 36, 50, 52, 90, 92, 100, 104 and 200 with a single degeneracy at 18 where two orbits of size 12 share one value, that the 48 wall entries of value 36 are exactly one of those orbits and unordered form a 4-regular graph of 24 edges on the 12 wall letters, that every one of the 400 kept pieces has a point count of exactly 5 times a unit drawn from the spectrum 1, 3, 7, 14 whose sum is 25 and that all 15800 cuttings carry one and the same unit profile totalling 125 units, and that the light, middle and heavy classes of the previous cycle are exactly the piece-size composition of the distinguished exchange, with the product-structure hypothesis for the union sizes 50, 100 and 175 refuted at every exchange of every fiber over all 6 axis pairs; the letter lists, the edge lists and the censuses are anchored as measured, and no physical or lattice-wide identification is made`

## Inputs and scope

The declared finite object is the one this lane has carried throughout: the 16 corners of the unit
four-cube, the 2672 five-corner unit-determinant pieces built on them, the 400 that survive at the
adjacency-cost floor 6, the 15800 cuttings of 24 pieces each that those 400 assemble into, the 192
pieces occurring in at least one cutting, and the 384 signed coordinate maps of the cell. Points are
counted on the generic sample grid with per-axis offsets 1, 2, 4, 8, that is 5 values on each of the
four axes and 625 points in all. The pair of facet letters on the two slots of the first axis, drawn
from a 16-letter alphabet, gives the interface matrix of trace 2000, whose 48 entries of value 36 are
the wall.

The previous cycle showed that exactly the 96 maps fixing the first axis act on the wall, that they
act transitively, that each entry stabilizer has order 2 and is that entry's own fold, and that the
light, middle and heavy split of 8, 32 and 8 is stable across a second generic point frame yet is
moved by the action itself. It left three questions at the letter level: which letter pairs carry the
wall and why; what the light and heavy classes are as letter-level objects; and where the union
values 50, 100 and 175, all multiples of 25, come from. Those are the questions this note answers.
Nothing from the previous cycle is assumed: the object, the alphabet, the matrix, the folds, the rows
and the exchanges are all rebuilt by the linked runner before any gate runs, and the previous cycle's
class lists enter only as anchors to compare a freshly recomputed classification against.

These are finite-scope object choices, not imported physical primitives. Every integer below is
recomputed by the linked runner from the corner list alone: it uses the standard library only,
performs no file input or output and no randomness, and gates each recomputed value against the value
stated here.

## The letter representation

- **Every acting map induces exactly one letter permutation together with a slot-swap flag, and no
  other map induces any.** A cell map permutes the 15800 cuttings, hence carries each cutting's pair
  of first-axis letters to the letter pair of the image cutting. Whether that induced pair map comes
  from a single permutation of the 16 letters, with the two slots either kept or swapped, is a
  well-posed question, and both flag values are tested for every one of the 384 maps. Exactly the 96
  maps that fix the first axis answer yes, each with exactly one valid pair of permutation and flag;
  the other 288 answer no for both flags. The complement is counted, not assumed. The flag is not
  free either: it is bit zero of the map's flip mask at all 96 acting maps, so the slot swap is
  precisely the reversal of the first axis.

- **The assignment is a faithful homomorphism.** At all 9216 ordered pairs of acting maps the letter
  permutation composes in the order in which the maps are applied and the flags add modulo two. The
  96 pairs of permutation and flag are pairwise distinct, so the action of the acting maps on the
  letters together with the flag is faithful. The permutation alone is not: exactly 2 maps give the
  identity permutation, namely the identity map with flag 0 and the pure first-axis flip with flag 1,
  so the permutations form an image of order 48. The wall action of the previous cycle is therefore
  not merely a symmetry of a list of 48 entries; it is a representation of the acting maps by letters.

- **The letters themselves fall into two orbits, and one of them is the wall alphabet.** Under the 96
  permutations the 16 letters split into exactly 2 orbits, of sizes 12 and 4. The size-12 orbit is
  exactly the set of letters that occur in wall entries, namely 0, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13
  and 14; the size-4 orbit is its complement, 1, 6, 8 and 15. Row sums are constant on each orbit,
  862 on the wall letters and 1364 on the others, and diagonal entries are constant too, 100 on the
  wall letters and 200 on the others, with the trace 2000 recovered.

- **The interface matrix collapses to ten orbit constants.** The matrix is symmetric at all 256
  entries and equivariant under all 96 acting maps, with the slots swapped when the flag is set. The
  induced action on the 256 ordered letter pairs has exactly 10 orbits, of sizes 4, 12, 12, 12, 12,
  12, 48, 48, 48 and 48, and the matrix is constant on each of them. The orbit values are the 9
  distinct entries 18, 36, 50, 52, 90, 92, 100, 104 and 200, so the value determines the orbit
  everywhere except at the smallest off-diagonal value 18, which is carried by two different orbits of
  size 12 each. That is the single degeneracy of the whole matrix: the numeric entry cannot separate
  those two orbits, but the action can. Each of the two is held by the transpose and so consists of 6
  unordered pairs; the first is 0 and 7, 2 and 13, 3 and 5, 4 and 11, 9 and 12, 10 and 14, and the
  second is 0 and 12, 2 and 11, 3 and 10, 4 and 13, 5 and 14, 7 and 9. The two edge sets are disjoint
  and together give all 12 unordered pairs at that value. The value census over the 256 entries is 24
  entries at 18, 48 at 36, 48 at 50, 48 at 52, 12 at 90, 48 at 92, 12 at 100, 12 at 104 and 4 at 200;
  the weighted sum recovers the cutting count 15800 and the diagonal recovers the trace 2000.

## The wall as an orbit and a graph

The wall is not a pairing, and it is not a coincidence of value: the 48 entries of value 36 are
exactly one of the 10 pair orbits. The previous cycle established transitivity by moving cuttings; it
is now visible one level up, as the statement that the wall is a single orbit of ordered letter
pairs. The action on a wall entry is given by the letter formula, that is the image entry is obtained
by applying the permutation to both letters and swapping the slots when the flag is set, and this is
verified at all 4608 pairs of an acting map with a wall entry.

At the unordered level the wall is a graph: 24 edges on the 12 wall letters, and every one of those
letters has degree exactly 4. So the answer to the first entrance question of the previous cycle is
that the wall letters carry a 4-regular graph, which is why no letter of the wall alphabet is special
and why 24 doubles to 48 under the two orders of a pair.

## The size quantum and the constant profile

Every one of the 400 kept pieces has a point count that is exactly 5 times an integer unit, and the
unit takes only the four values 1, 3, 7 and 14. The census over the kept pieces is 24 pieces of unit
1, 176 of unit 3, 176 of unit 7 and 24 of unit 14; over the 192 used pieces it is 8, 88, 88 and 8.
The four distinct units sum to 25.

The profile is not merely available, it is forced: every one of the 15800 cuttings has the same unit
profile, one piece of unit 1, 11 pieces of unit 3, 11 pieces of unit 7 and one piece of unit 14. That
is 125 units, that is 625 points, the whole sample grid, and the 24 pieces of a cutting are accounted
for as 1 plus 11 plus 11 plus 1. No cutting deviates. The size quantum is therefore a property of the
object and not of any particular cutting, and the multiples of 25 that the previous cycle asked about
are already present in the piece sizes before any exchange is looked at.

## Class as composition

In each of the 48 wall fibers the fold-held cuttings decompose over 40 rows, and among those rows the
equal-union exchanges are the pairs of disjoint row pairs sharing a point union. Over every exchange
of every fiber, that is all 192 of them, the sorted pair of half unit-profiles is a function of the
union point-size and of nothing else: union 50 gives halves of units 1, 3, 3, 3; union 100 gives 3,
3, 7, 7; union 175 gives 7, 7, 7, 14. There are 0 exceptions.

Each fiber carries exactly one exchange of broken count 2, the one the previous cycle identified as
carrying the whole distinction, and its union size is 50 at 8 fibers, 100 at 32 and 175 at 8. That
census agrees with the light, middle and heavy letter-pair lists of the previous cycle at 48 of 48
fibers. So the trichotomy is read off directly: light means the distinguished exchange carries a
piece of the smallest unit 1 in each half, heavy means it carries a piece of the largest unit 14, and
middle means neither end appears. The light and heavy classes are the two ends of the piece-size
spectrum, which answers the second entrance question, and it explains without difficulty why the
classification is not invariant under the action: the composition is stated relative to the point
frame that gives pieces their point counts, exactly the relativity the previous cycle measured.

## A refuted product hypothesis

The obvious reading of the union values 50, 100 and 175 as 2, 4 and 7 times 25 is that an exchange
union is a base set on two axes times the full square of 25 points on the complementary two axes.
That hypothesis is refuted here. Grouping each union's points by their coordinates on a chosen axis
pair and asking whether every nonempty group has exactly 25 points returns 0 factorizations out of
the 1152 tests, that is every exchange union of every fiber against each of the 6 unordered axis
pairs, and the same test on single row supports returns 0 out of 11520. The test is not vacuous: run
on the whole sample grid it reports a factorization on all 6 of the 6 axis pairs, so a positive
answer is reachable and the object simply does not give one.

The factor 25 therefore belongs to the object through its piece sizes, not through a product
structure of the unions. That answers the third entrance question, in the negative for the shape the
previous cycle proposed and in the affirmative for the quantity it was chasing.

## Derived versus measured

Derived at the declared finite scope. The uniqueness of the flag is derived, in the sense that both
flag values are tested at every one of the 384 maps and exactly one survives at each of the 96 acting
maps while neither survives at the other 288. The homomorphism and the faithfulness are derived by
verification at all 9216 ordered pairs, not sampled. The orbit decompositions of the 16 letters and
of the 256 ordered pairs are derived by closure under the full set of 96 actions, and the constancy
of the matrix on each orbit follows from the equivariance, which is itself checked entry by entry.
That the wall is one orbit, and hence that its unordered graph is regular, is derived rather than
observed. The half-profile law is derived in the same sense: it is verified as a function of union
size with 0 exceptions over every exchange of every fiber, and its failure at a single exchange would
have been reported.

What is measured, not derived, at the declared finite scope: the value census of the matrix and the 9
distinct values themselves; which letters are wall letters, anchored as the measured list 0, 2, 3, 4,
5, 7, 9, 10, 11, 12, 13, 14 with complement 1, 6, 8, 15; the two edge lists at value 18 and the 24
edges of the wall graph, all of which are frame-anchored labels; the row sums 862 and 1364; the unit
spectrum 1, 3, 7, 14 and its censuses; the constant profile of one, eleven, eleven and one; and the
broken-count-2 census 8, 32 and 8. Above all, why the unit spectrum is 1, 3, 7, 14 and why every one
of the 15800 cuttings carries the same profile are measured facts here, not consequences of anything
proved in this note.

## Boundary and the honest auditor read

All of the above are computational identities of the declared unit four-cube object, its 400 kept
pieces, its 15800 cuttings, its 16-letter alphabet and the order-384 symmetry group of the cell. The
letter graph and the two edge lists at value 18 are stated in the labels of the declared alphabet and
the declared point frame, and are not claimed to be frame-independent. The refutation is a refutation
of one named product hypothesis on this object, tested over all 6 axis pairs, and says nothing about
other factorization shapes. No physical, dynamical, or lattice-wide identification is claimed, no
continuum limit is taken, and nothing here is asserted about cell-cutting systems outside the
declared object.

## Next entrance

Two questions are now sharp. The first is the size quantum: the units 1, 3, 7 and 14 sum to 25, they
appear in the fixed multiplicities 1, 11, 11 and 1 in every cutting, and both the spectrum and the
multiplicities are so far only counted. Deriving them from the corner geometry and the adjacency cost
floor would explain the multiples of 25 at their source and would make the class composition a
theorem rather than a table. The second is the degeneracy at value 18: it is the only place where the
interface matrix fails to separate its own orbits, so whatever function does separate them is a
strictly finer invariant of the object than the matrix, and finding it is the natural next reading of
the letter level.

## Review record

- Rows are the two-orbits of the 400 kept pieces under each fiber's own fold, and blocks are that
  fiber's fold-held cuttings written as row sets. Both conventions are fixed before any computation
  runs, and every statement is made for all 48 fibers, not for a chosen one.
- The letter maps are found by search, not by construction from the coordinate action: for each of
  the 384 maps and each of the two flag values the runner attempts to build a bijection from the
  cutting images and rejects it on the first inconsistency, so the 288 failures are genuine failures
  and the 96 successes are genuine solutions.
- The composition convention is the base convention, apply the second map first, and the
  homomorphism is tested in that order at every one of the 9216 ordered pairs.
- The orbit decompositions are computed by closure under the recomputed actions and are compared
  against the anchors of size and value only after being formed, so an anchor cannot seed an orbit.
- The class comparison runs in the honest direction: the runner recomputes each fiber's distinguished
  exchange and its union size, then compares the resulting classification against the previous
  cycle's letter-pair lists. The lists are never used to decide a class.
- The refutation gate carries a positive control on the same code path, the whole sample grid, which
  must and does report a factorization on all 6 axis pairs, so the two zeros cannot be an artifact of
  a broken test.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a commit
  cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries the results above stand as exact finite computational identities on the
declared object, and as nothing wider.

## Reproduction

Run the [runner](../scripts/physical_cell_cutting_letter_action_orbit_census_cycle797_2026_08_15.py).
The reviewed
[cache](../logs/runner-cache/physical_cell_cutting_letter_action_orbit_census_cycle797_2026_08_15.txt)
belongs beside it and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC`
budget, finishes in well under a minute on the reference machine, and stays far below one gigabyte.
Its final line is `TOTAL: PASS=10 FAIL=0`.
