# Physical cell cutting: letter action, interface-matrix orbit census, and piece-size unit spectrum

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
- `next_trace_action: derive, from the piece geometry and the adjacency cost floor alone, why the unit spectrum of the kept pieces is 1, 3, 7, 14 and why every one of the 15800 cuttings realizes the single profile of one unit-1 piece, eleven unit-3 pieces, eleven unit-7 pieces and one unit-14 piece; and find what separates the two orbits that share the smallest off-diagonal value 18, the one degeneracy the matrix value cannot see while the action can; none of that is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: exact finite computation on the declared cell: the 96 first-axis-fixing signed coordinate maps act faithfully on the 16 interface letters with a derived slot-swap flag; the symmetric interface matrix is constant on 10 ordered-pair orbits; its 48 value-36 pairs form one orbit and a 4-regular unordered graph; the 400 kept pieces have units in the spectrum 1, 3, 7, 14; every cutting has profile 1, 11, 11, 1; and every equal-union exchange has the profile fixed by its union size; enumerated values and labelled lists remain measured outputs, the continuous-cutting interpretation is explicit upstream support, and no physical or lattice-wide identification is made`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Inputs and scope

The declared finite object has 16 corners of the unit four-cube, 2672 five-corner
unit-determinant pieces, 400 pieces at adjacency-cost floor 6, 15800 selected
24-piece covers, 192 pieces occurring in at least one cover, and 384 signed
coordinate maps of the cell. Points are counted on the generic sample grid with
per-axis offsets 1, 2, 4, 8: 5 values on each of the four axes and 625 points in
all. The pair of facet letters on the two slots of the first axis, drawn from a
16-letter alphabet, gives the interface matrix of trace 2000; its 48 entries of
value 36 are called the **value-36 interface set** below.

The exact continuous-cutting certification for this same enumerated family is
landed upstream in the
[Cycle-782 diagonal-parity note](PHYSICAL_CELL_CUTTING_DIAGONAL_PARITY_CYCLE782_NOTE_2026-08-14.md).
That source separately checks normalized volumes, pairwise continuous interior
disjointness and total volume. This note imports only that geometric
interpretation. Its runner independently rebuilds the finite object, alphabet,
matrix, folds, rows and exchanges before testing the new identities; it does
not import any unlanded sibling result.

Every numeric output below is recomputed by the linked runner from the corner
list. The runner uses the standard library only, performs no file input or
output and no randomness, and gates each recomputed value against the value
stated here. Its cache envelope additionally binds this note and the landed
Cycle-782 note and runner as declared audit inputs, so later source drift cannot
leave the cached computation looking current.

### Import and support inventory

| Item | Classification | Role in the claim |
|---|---|---|
| Unit four-cube corners, determinant-one five-corner pieces, adjacency-cost floor and exact-cover search | zero-input structural | Declare and exhaustively rebuild the finite combinatorial object. |
| Offset tuple `(1, 2, 4, 8)` and five sample points per axis | explicit normalization/boundary condition | Fix the finite enumeration frame; no frame-independent or continuum claim is made. |
| [Cycle-782 continuous-cutting certificate](PHYSICAL_CELL_CUTTING_DIAGONAL_PARITY_CYCLE782_NOTE_2026-08-14.md) and its paired runner | upstream support | Supply the exact continuous-geometric interpretation of the independently re-enumerated 15800 covers; this dependency has no inherited audit grade. |
| Matrix entries, orbit representatives, letter labels, unit spectrum and profile censuses | support-only computational outputs | These are exhaustive measured outputs, not imported premises or analytic derivations. |
| Framework axioms or approved primitives; physical, observational, fitted, literature, PDG or cosmological inputs | none | No such input enters the finite claim. |

## Exact target

> On the declared finite unit-four-cube family, the 96 first-axis-fixing signed
> coordinate maps act faithfully on the 16 interface letters together with the
> derived slot-swap flag; the 16 letters have orbits of sizes 12 and 4, the 256
> ordered letter pairs have exactly 10 matrix-constant orbits, the 48 value-36
> pairs form one orbit and a 4-regular unordered graph, every kept piece has
> point count five times a unit in `{1, 3, 7, 14}`, every one of the 15800
> continuously certified cuttings has unit profile `(1, 11, 11, 1)`, and every
> equal-union exchange has the half-profile specified by its union size.

This target is exhaustive only for the declared finite family and frame. It
does not assert an analytic derivation of the measured spectrum or profile, a
physical carrier, a lattice-wide construction, or a result for another cell or
sampling frame.

## Proof-obligation graph

1. **Object reconstruction.** Rebuild the pieces, sample-grid covers, used
   pieces, facet alphabet and signed coordinate maps; import only the landed
   Cycle-782 continuous-geometry certificate for the same cover family.
2. **Letter-map existence and uniqueness.** Try both slot flags for each of the
   384 cell maps, enforce bijectivity, and count the 96 unique successes and 288
   failures.
3. **Faithful action.** Derive the flag from the first-axis flip, check all 9216
   ordered compositions, injectivity of permutation-plus-flag pairs, and the
   two-element kernel of the permutation projection.
4. **Matrix equivariance.** Recompute the interface matrix and check symmetry
   and equivariance entry by entry under all 96 actions.
5. **Orbit decompositions.** Close the letter and ordered-pair orbits under the
   full action, then compare their sizes and matrix values with the stated
   outputs only after the orbits have been formed.
6. **Value-36 graph.** Check that the 48 value-36 pairs are exactly one pair
   orbit and that their 24 unordered edges give degree four at each of the 12
   incident letters.
7. **Piece and cutting profiles.** Count every piece mask, then every cutting,
   to establish the unit spectrum and the single `(1, 11, 11, 1)` profile.
8. **Exchange profiles.** Rebuild every fold-held fiber and all 192 equal-union
   exchanges, then verify the half-profile law with zero exceptions and the
   distinguished-exchange union-size census.
9. **Target conjunction.** Combine obligations 1-8; no obligation assumes the
   target or a target-equivalent lemma.

The strongest open lemma is an analytic derivation of the unit spectrum and
constant cutting profile from the corner geometry and adjacency-cost floor.
That lemma would explain the measured outputs but is not needed for, and is not
claimed by, this exact finite target.

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
  so the permutations form an image of order 48. The value-36 interface action is therefore not
  merely a symmetry of a list of 48 entries; it is a representation of the acting maps by letters.

- **The letters themselves fall into two orbits, and one is incident to the value-36 set.** Under the 96
  permutations the 16 letters split into exactly 2 orbits, of sizes 12 and 4. The size-12 orbit is
  exactly the set of letters that occur in value-36 entries, namely 0, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13
  and 14; the size-4 orbit is its complement, 1, 6, 8 and 15. Row sums are constant on each orbit,
  862 on the incident letters and 1364 on the others, and diagonal entries are constant too, 100 on
  the incident letters and 200 on the others, with the trace 2000 recovered.

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

## The value-36 interface set as an orbit and a graph

The 48 entries of value 36 are exactly one of the 10 pair orbits. This makes
transitivity visible at the letter level: the value-36 interface set is a single orbit of ordered
letter pairs. The action on a value-36 entry is given by the letter formula, so its image is obtained
by applying the permutation to both letters and swapping the slots when the flag is set, and this is
verified at all 4608 pairs of an acting map with a value-36 entry.

At the unordered level the value-36 interface set is a graph: 24 edges on its 12 incident letters,
and every one of those letters has degree exactly 4. Thus no incident letter is distinguished by
degree, and 24 unordered edges give 48 ordered entries.

## The piece-size unit spectrum and the constant profile

Every one of the 400 kept pieces has a point count that is exactly 5 times an integer unit, and the
unit takes only the four values 1, 3, 7 and 14. The census over the kept pieces is 24 pieces of unit
1, 176 of unit 3, 176 of unit 7 and 24 of unit 14; over the 192 used pieces it is 8, 88, 88 and 8.
The four distinct units sum to 25.

The profile is not merely available, it is forced: every one of the 15800 cuttings has the same unit
profile, one piece of unit 1, 11 pieces of unit 3, 11 pieces of unit 7 and one piece of unit 14. That
is 125 units, that is 625 points, the whole sample grid, and the 24 pieces of a cutting are accounted
for as 1 plus 11 plus 11 plus 1. No cutting deviates. The unit spectrum is therefore a property of the
declared object and not of any particular cutting.

## Exchange profiles by union size

In each of the 48 value-36 fibers the fold-held cuttings decompose over 40 rows, and among those rows the
equal-union exchanges are the pairs of disjoint row pairs sharing a point union. Over every exchange
of every fiber, that is all 192 of them, the sorted pair of half unit-profiles is a function of the
union point-size and of nothing else: union 50 gives halves of units 1, 3, 3, 3; union 100 gives 3,
3, 7, 7; union 175 gives 7, 7, 7, 14. There are 0 exceptions.

Each fiber carries exactly one exchange of broken count 2. Its union size is 50 at 8 fibers, 100 at
32 and 175 at 8. This is an exhaustive census internal to the declared object; it is not compared
with, or used to import, labels or classifications from an unlanded sibling result.

## Derived versus measured

Derived at the declared finite scope. The uniqueness of the flag is derived, in the sense that both
flag values are tested at every one of the 384 maps and exactly one survives at each of the 96 acting
maps while neither survives at the other 288. The homomorphism and the faithfulness are derived by
verification at all 9216 ordered pairs, not sampled. The orbit decompositions of the 16 letters and
of the 256 ordered pairs are derived by closure under the full set of 96 actions, and the constancy
of the matrix on each orbit follows from the equivariance, which is itself checked entry by entry.
That the value-36 interface set is one orbit, and hence that its unordered graph is regular, is derived rather than
observed. The half-profile law is derived in the same sense: it is verified as a function of union
size with 0 exceptions over every exchange of every fiber, and its failure at a single exchange would
have been reported.

What is measured, not derived, at the declared finite scope: the value census of the matrix and the 9
distinct values themselves; which letters are incident to value-36 entries, anchored as the measured list 0, 2, 3, 4,
5, 7, 9, 10, 11, 12, 13, 14 with complement 1, 6, 8, 15; the two edge lists at value 18 and the 24
edges of the value-36 graph, all of which are frame-anchored labels; the row sums 862 and 1364; the unit
spectrum 1, 3, 7, 14 and its censuses; the constant profile of one, eleven, eleven and one; and the
broken-count-2 census 8, 32 and 8. Above all, why the unit spectrum is 1, 3, 7, 14 and why every one
of the 15800 cuttings carries the same profile are measured facts here, not consequences of anything
proved in this note.

## Boundary and the honest auditor read

All of the above are computational identities of the declared unit four-cube object, its 400 kept
pieces, its 15800 cuttings, its 16-letter alphabet and the order-384 symmetry group of the cell. The
letter graph and the two edge lists at value 18 are stated in the labels of the declared alphabet and
the declared point frame, and are not claimed to be frame-independent. All asserted results are
positive finite identities at that scope. No physical, dynamical, or lattice-wide identification is
claimed, no continuum limit is taken, and nothing here is asserted about cell-cutting systems
outside the declared object.

## Next entrance

Two questions are now sharp. The first is the piece-size unit spectrum: the units 1, 3, 7 and 14 sum to 25, they
appear in the fixed multiplicities 1, 11, 11 and 1 in every cutting, and both the spectrum and the
multiplicities are so far only counted. Deriving them from the corner geometry and the adjacency cost
floor would explain the multiples of 25 at their source. The second is the degeneracy at value 18: it is the only place where the
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
- Each fiber's distinguished exchange and its union size are recomputed directly. The resulting
  census is checked against a stated finite output only; no sibling label list enters the runner.
- The runner's nine gates assert only the positive finite identities within the exact target and
  proof-obligation graph above.
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
Its final line is `TOTAL: PASS=9 FAIL=0`.
