# Four fixed-point counts force the cell-orbit count and a positive blind floor — Cycle 769

Date: 2026-08-11

Authority: none

Audit: unset.

Status: Four fixed-point counts, one per stabiliser and target set, reproduce all three orbit counts of the
cell object; the zero among them forces the group to act freely on the 36864 cells, which cycle 768 took as
measured input, and the gap between 104 and 96 forces the blind floor positive and makes ceiling plus floor
equal 192.

Claim type: bounded_theorem

Runner:

- [`physical_cell_cutting_flip_counts_cycle769_2026_08_11.py`](../scripts/physical_cell_cutting_flip_counts_cycle769_2026_08_11.py)

Axioms:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The exact integer fixed-point and orbit counts are self-contained for one finite four-cube cutting system; the part-table multiplicities are computed over a declared prime and no physical interpretation is claimed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "seek a characteristic-zero derivation of the full part table and a structural explanation of the values 8 and 48"
conditional_surface_status: "exact finite combinatorics for the fixed-point and orbit-count half; the part-table multiplicities remain a declared-prime computation"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. What this responds to

The object is the unit four-cube with its 16 corners. Among the corner simplices of
unit absolute determinant there are 2672 candidates; the adjacency cost floor is 6 and
400 candidates attain it; those 400 admit 15800 cuttings of 24 pieces each; 192 of the
pieces actually occur, and there are 192 covers, a cover being 8 pieces that are
pairwise never in a common cutting and that together meet every cutting exactly once.
Each piece lies in 1975 cuttings and 8 times 1975 is 15800. The symmetry group is the
group of coordinate permutations together with independent flips of the axes; it has
order 384 and is transitive both on the 192 pieces and on the 192 covers.

Three cycles left three loose ends here.

Cycle 764 landed a ceiling of 144 and a blind floor of 48 and never said why the two
add to the number of pieces. Cycle 768 built the 20-row part table from which those two
numbers are read, and used the fact that the group acts freely on the cover-by-piece
cells; it took that freeness as an input rather than producing it. Cycle 768 also found,
separately, that one cell orbit on its own has rank 144 and blind dimension 48.

This cycle supplies the missing arguments from four counts that had never been measured:
how many pieces and how many covers are left in place by the non-trivial element of one
piece stabiliser, and the same two counts for one cover stabiliser.

## 2. The counting statement and its proof, in words

Let a finite group act transitively on a set X in such a way that the subgroup fixing a
chosen point has exactly 2 elements, the identity and one further element s, which is
therefore its own inverse. Let Y be any other set the same group acts on. Then the
number of orbits the group has on the set of ordered pairs, first entry from X and
second from Y, is

    (size of Y plus the number of points of Y left in place by s) divided by 2.

The proof is two short steps. First, because the action on X is transitive, every orbit
of pairs contains a pair whose first entry is the chosen point, and two such pairs lie
in the same orbit exactly when their second entries are carried onto each other by
something that fixes the chosen point. So orbits of pairs correspond one for one with
orbits of the 2-element stabiliser acting on Y. Second, a group with 2 elements has
orbits of size 1 or 2 only: size 1 at each point of Y left in place by s, size 2 at every
other point, in pairs. If f of the points are left in place, the number of orbits is
f plus (size of Y minus f) divided by 2, which is the displayed formula.

Both hypotheses hold here. The stabiliser of a piece has order 2, the stabiliser of a
cover has order 2, and each non-identity element squares to the identity. The group is
transitive on pieces and on covers, so nothing depends on which piece or which cover is
chosen.

## 3. The four counts and what they say

Write s_p for the non-identity element of the stabiliser of a piece and s_c for the
non-identity element of the stabiliser of a cover. The two are different elements of the
group. Measured directly on the permutations, and measured, not derived:

    s_p leaves 16 pieces in place and 0 covers in place
    s_c leaves 0 pieces in place and 48 covers in place

Feeding these into the statement of section 2, with 192 for the size of both sets:

    orbits on ordered piece pairs   = (192 + 16) / 2 = 104
    orbits on ordered cover pairs   = (192 + 48) / 2 = 120
    orbits on cover-by-piece cells  = (192 + 0)  / 2 = 96

Those three values, 104 and 120 and 96, are exactly the orbit counts that earlier cycles
obtained from the part table. Here they arrive from four small integers instead. The
third line can be run in either order, taking the first entry from the covers or from
the pieces, and the two readings agree because both fixed-point counts are 0.

The runner obtains each of the three orbit counts three independent ways before it
compares them with the four counts: by sweeping the whole group over every ordered pair,
by walking the pair set from 2 generating elements alone, and by averaging fixed-point
products over all 384 group elements. It also counts the orbits of each 2-element
stabiliser on the far set directly, which is the middle step of the proof made explicit.

## 4. Freeness and the count 96

The zero in the third line is the load-bearing one. If s_c left even one piece in place,
then s_c would sit in that piece's stabiliser as well as in a cover's, and the two
stabilisers would share a non-identity element. Measuring 0 says s_c belongs to no piece
stabiliser at all. Because the group is transitive on both sides, the same holds for
every cover and every piece: the stabiliser of a cover and the stabiliser of a piece meet
in the identity alone.

An element that fixes a cell, meaning a cover and a piece at once, would have to lie in
both stabilisers, so no element other than the identity fixes any cell. The action on
the 36864 cells is free, and the orbit count is then forced rather than measured:

    36864 / 384 = 96, which is 384 divided by 2 times 2,

the product being the two stabiliser orders. Cycle 768 had this as a measured fact and
built on it; one count now delivers it. The runner checks the implication the long way
as well, cover by cover over
all 192 covers, and confirms that no non-identity element of the group fixes any of the
36864 cells.

## 5. The positive floor

Each row of the part table carries a dimension per copy, two multiplicities, m on the
piece side and mc on the cover side, and a row dimension which is the dimension per copy
times m. Summing m against m over the rows gives the piece-pair
orbit count, summing mc against mc gives the cover-pair count, and summing m against mc
gives the cell count. The runner gates all three against the direct orbit counts of
section 3; that bridge is what lets a statement about counts become a statement about
the table.

Suppose m equalled mc on every row. Then the first sum and the third would be equal,
that is 104 would equal 96, which is false. So some row has m different from mc. More
than that: the difference of the two sums is the sum of m times (m minus mc), and it
comes out 8, a positive number, so at least one row must have m strictly larger than mc.
The runner finds 10 such rows.

The blind floor is the sum, over rows, of the dimension per copy times the positive part
of m minus mc. Every row with m larger than mc contributes a positive amount and no
other row contributes anything, so the floor is strictly positive as soon as one such row
exists. Its measured value is 48, carried by those same 10 rows; that last sentence is
bookkeeping, since the dimension per copy is at least 1 on every row, and it is recorded
so the arithmetic can be followed. So 48 is not merely a number that happened to come
out positive; the
excess of the piece-pair count over the cell count leaves it no choice.

The finer weighting, the sum of m times (m minus mc), is 8. It is the same sign pattern
weighted differently from the floor and is recorded here without interpretation.

## 6. Ceiling plus floor is the piece count

For any two numbers x and y, the smaller of the two plus the positive part of x minus y
is x again. Weighting that row by row with the dimension per copy, against m and mc,
gives

    ceiling + floor = sum over rows of dimension per copy times m = 192.

The right side is the sum of the row dimensions, which is 192, the number of pieces, and
also the number of covers. The runner checks the rearrangement on each of the 20 rows
individually, not only on the totals, and reports the two totals as 144 and 48.

So 144 plus 48 equalling 192 is an identity, not a coincidence, and cycle 764 could have
had it for free. Cycle 768's separate finding, that a single cell orbit on its own has
rank 144 and blind dimension 48 so that rank plus nullity is 192 for that one table, is
reproduced here at two primes. That is a consistency check on the identity above and not
an independent derivation of it: it shows one table attaining the ceiling and the floor
at the same time, which the identity permits but does not require.

## 7. What the runner checks

The runner is standalone. It rebuilds the corners, the candidate pieces, the cost floor,
the cuttings, the pieces used and the covers from nothing, then builds the group by
permuting and flipping coordinates, then the part table. Its first line records that all
numbers below it are exact computational identities with no floating point entering any
gate. 35 gates run, in one sequence from C0.

- C0 and C1 rebuild the object and check 2672, 400 at cost floor 6, 15800 cuttings of
  24, 192 pieces used, 192 covers, 1975 cuttings per piece, 8 pieces per cover.
- C2, C3 and C4 build the group of order 384, check closure and distinctness, and check
  that it permutes the 192 pieces and the 192 covers bijectively and transitively.
- C5 checks that 2 named elements generate all 384, and that neither is the identity or
  either stabiliser element, so the perturbation used by C14 and C15 is honest.
- C6 and C7 check both stabiliser orders are 2, that both non-identity elements square
  to the identity, that they differ, and that 384 splits as 2 times 192 both ways.
- C8 counts the three orbit sets by sweeping the group over every ordered pair and gates
  104, 120, 96; it also checks that the labelling produced is invariant under all 384.
- C9 recounts the same three by walking from the 2 generators alone.
- C10 recounts them a third time by averaging fixed-point products over the group.
- C11 prints the four counts 16, 0, 0, 48 on one line.
- C12 checks all four instances of the counting statement in the form twice the orbit
  count minus 192 equals the measured fixed count.
- C13 counts the orbits of each 2-element stabiliser on the far set directly and gets
  104, 120, 96, 96, which is the middle step of the proof.
- C14 and C15 are the discriminator. A generator's piece permutation, and separately a
  generator's cover permutation, is altered by swapping 2 points, the orbit counts and
  the fixed counts are recomputed on the altered action, and the four relations are
  retested. All 6 alterations tried on each side break at least one relation; each
  breaks 3 of the 4, and the first alteration tried already breaks them, so no search
  for a convenient perturbation took place.
- C16 records that the true action breaks 0 of the four.
- C17, C18 and C19 do freeness: no non-identity element fixes any of the 36864 cells,
  the check is repeated cover by cover over all 192 covers, and 36864 equals 384 times
  96 with 96 equal to 384 divided by 2 times 2.
- C20 and C21 build the part table: 20 rows with dimensions 1, 1, 1, 1, 3, 3, 3, 3, 4,
  4, 8, 8, 8, 8, 12, 12, 24, 24, 32, 32, from the 104 orbit matrices, their structure
  constants checked on 7 sampled pairs, and a centre of dimension 20.
- C22 and C23 give the table sums: 192 and 192 for dimension against each multiplicity,
  and 104, 120, 96 for the three multiplicity products.
- C24 is the bridge gate: those three sums equal the direct orbit counts of C8.
- C25 and C26 do the positive floor: the difference of the sums is 8, 10 rows have m
  above mc, and the floor is 48, carried by those 10 rows.
- C27 checks that each row's measured blind dimension is at least its forced part.
- C28 checks the rearrangement of section 6 on each of the 20 rows separately.
- C29 gives ceiling 144 plus floor 48 equal to 192, the piece count and the cover count.
- C30 recomputes the single cell orbit table at 2 primes: rank 144, blind dimension 48.
- C31 and C32 are wrong-value rejectors. 8 of 8 altered fixed-point tuples break at
  least one relation, and 40 of 40 altered table rows fail the row test.
- C33 and C34 are source hygiene and the wall time, memory and output length budget.

## 8. Boundary

This note adds no axiom, no primitive and no import. It is a statement about one finite
object and one finite group, and it says nothing about physics.

The part table's multiplicities m and mc are read as ranks over a single fixed prime,
so the table itself is a measurement rather than a proof. The counting half, sections 2
through 4, is prime-free exact integer combinatorics and does not depend on it.

The rearrangement of section 6 is an identity for any integers whatever. Its content is
therefore not the addition but the fact that both sides are computed from the same 20
rows and that those row dimensions sum to the piece count.

The gap between the ceiling and the rank landed for the full cover table is untouched
this cycle; nothing here bears on it either way.

Nothing in this note fixes which of the 20 rows carry the excess of m over mc beyond
counting them, and nothing here explains the value 8 as against 48.

## 9. Honest auditor read

The weakest step is the part table. Its dimensions and multiplicities come from ranks
computed over one prime; a bad prime would silently lower a rank and could in principle
move m or mc. Three things limit the exposure. The three multiplicity sums are gated
against orbit counts obtained without any prime at all, so a corrupted table would have
to conspire to reproduce 104, 120 and 96 exactly. The single cell orbit rank is checked
at 2 different primes. And the whole of sections 2 through 4, including the freeness
result, uses no linear algebra whatever.

The second weakest step is the discriminator. It alters a generator rather than an
arbitrary group element, so what it rules out is a relation that would hold for any
permutation data of this shape, not every possible way the argument could be vacuous.
It does rule out the failure mode that matters, namely that twice an orbit count minus
192 might equal a fixed-point count for arithmetic reasons alone: alter the action a
little and 3 of the 4 relations fail at once.

The third point is a matter of reading rather than of computation. Section 6 proves that
the ceiling and the floor add to the piece count, and that is genuinely all it proves.
The fact that one cell orbit attains both at once is a separate measurement reproduced
here, and it is offered as a check, not as an explanation of why 144 and 48 are the
values they are.
