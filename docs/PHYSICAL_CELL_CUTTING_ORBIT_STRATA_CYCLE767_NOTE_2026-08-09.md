# Complementary sets of cell orbits carry equal rank, and the corner overlaps cut the 96 orbits into 25 strata — Cycle 767

Date: 2026-08-09

Authority: none

Status: proposed_retained

Claim type: bounded_theorem

Machine status:

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Send the self-contained finite theorem and measured strata to independent audit; no downstream consumer is yet known."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The note proves one exact finite complementary-rank identity and reports exhaustive measurements on the declared unit-four-cube object."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Runner:

- [`physical_cell_cutting_orbit_strata_cycle767_2026_08_09.py`](../scripts/physical_cell_cutting_orbit_strata_cycle767_2026_08_09.py)

Axioms:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## What this responds to

Cycle 764 derived a ceiling of 144 on the rank of any table covariant under the
cell's own symmetry and a floor of 48 on its blind space, and showed the ceiling
attained. Cycle 765 reduced any such table to twenty small matrices and ran the
full four-subset census. Cycle 766 measured every sub-sum of the four incidence
orbits and found that each orbit alone already sits at 144, so the excess 39 is
pure cancellation, and that the cancellation is born on pairs.

Every measurement so far was taken on subsets of size at most four out of 96. That
left the other end of the lattice untouched, where almost every orbit is present.
This cycle reaches it with an identity rather than a census, and then asks what
structure on the orbits themselves the ranks are seeing.

## The setting

The object is the unit four-cube. Its corners carry 2672 candidate pieces of unit
determinant, each of volume 1/24, and 400 of those sit at the adjacency-cost
floor 6. The 400 admit 15800 cuttings into 24 pieces, and exactly 192 of the
pieces are used by some cover, a cover being 8 pieces that are pairwise
cutting-disjoint and together meet every cutting. Each used piece lies in 1975
cuttings, and 8 times 1975 is 15800. There are 192 covers.

The symmetry is the group that permutes the four coordinates and flips any subset
of them, of order 384. It is transitive on the 192 pieces and on the 192 covers
and acts freely on the 192 by 192 array of cells, so the 36864 cells fall into 96
orbits of 384 cells each. The cover table, the 0/1 table recording which pieces
belong to which cover, is the sum of the four cell orbits whose cells are
incidences; it has rank 105 and blind dimension 87.

## Result 1: complementary sets of orbits carry equal rank

The identity was derived before it was measured, and it rests on two facts about
the individual orbit tables that the runner measures rather than assumes.

First, every cell lies in exactly one orbit, so the 96 orbit tables add entry by
entry to the all-ones table, whose exact rational rank is 1. Second, each orbit is
free under a group of order 384 and meets every cover in exactly 2 pieces, so
every orbit table is 0/1 with 2 ones in each row and 2 in each column, 384 ones in
all. Both are gated, with 0 orbits off the pattern.

Now split the row space and the column space of a 192-dimensional table into the
constant line and its complement. A table with 2 ones in every row and every
column sends the constant vector to twice itself and preserves the complement, so
for any set S of orbits the summed table is block diagonal there, acting as the
scalar 2|S| on the constant line and as some block A_S on the complement. The
all-ones table is the same kind of object, with 192 on the constant line and 0 on
the complement. Adding S to the orbits left out of S therefore gives 0 on the
complement, so the two blocks are negatives of each other and carry the same rank.
Since 2|S| is never 0 for a non-empty S, the rank of the sum over S equals 1 plus
the rank of A_S, and so equals the rank of the sum over the orbits left out of S,
for every S that is neither empty nor everything. The ceiling splits as 1 for the
constant line plus 143 for its complement, which is why the complement alone can
never carry the full 144.

The identity is checked at three places on the lattice, each rank computed by
exact rational elimination straight from its own table and never supplied by the
pairing:

- the orbits left out of the four incidence orbits give rank 105, the rank of the
  cover table itself;
- the orbits left out of a single incidence orbit give 144, the ceiling, matching
  that orbit alone;
- the orbits left out of each of the six incidence pairs give 72, 93, 117, 129,
  144, 144, matching the cycle 766 pair spectrum entry for entry.

The end points behave as the derivation says they must and not otherwise: the
empty sum has rank 0 while the full sum has rank 1, so this is a statement about
proper non-empty sets.

The pairing itself is gated before it is used. For each set compared, the runner
checks that the left-out set has the complementary size, shares no orbit with the
set, and that the two tables add back to the all-ones table entry by entry. This
matters, because the two headline values 105 and 144 are also the rank of the
cover table and the rank of a single incidence orbit, so a left-out set that
quietly returned its own input would print exactly the same numbers. A copy of the
runner in which the left-out set was replaced by the set itself was run, and that
gate is the gate that flips.

## Result 2: the corner overlaps cut the orbits into 25 strata

Each used piece has exactly 5 corners and two distinct used pieces share at most
4, so a piece is determined by its corner set, and an overlap of 5 says the piece
is one of the blocks of the cover. That gives a symmetry-invariant label on each
cell: for a cell made of a cover C and a piece P, take the sorted list of the
corner overlaps of P with the 8 blocks of C. Recomputed on all 36864 cells, the
label is constant along every orbit, with 0 orbits varying.

Its fibres cut the 96 orbits into 25 strata, of sizes 12 strata of size 2, 7 of
size 4, 4 of size 6, 1 of size 8 and 1 of size 12. The cells whose label contains
a 5 are exactly the four incidence orbits, and they form one whole stratum. So the
incidence set that the cover table is built from is cut out by the corner data
alone, with no reference to the cuttings.

The finer label built from the body overlaps, the count of cuttings a piece shares
with each block of a cover, takes 83 values, strictly refines the corner label, and
takes the value 1975 exactly on the four incidence orbits.

Summing each stratum and taking the exact rank: the largest stratum rank is 143,
one below the ceiling 144, so no stratum attains it; the smallest blind dimension
across the strata is 49, one above the floor 48; and the incidence stratum gives
105, as it must.

## Result 3: the corner label does not decide the rank repair

Cycle 766 found that replacing the first of the four incidence orbits by a
suitable non-incidence orbit lifts the rank from 105 to the ceiling. Restricted to
that one slot, 19 of the substitutions reach 144, and the lifting orbit named in
cycle 766 is one of them, sitting in stratum 23. One lifting member and one
non-member are re-derived here by exact rational elimination and agree with the
modular reduction, the non-member staying below the ceiling.

Lifting is not a property of the stratum. Across the 25 strata, 0 lift wholly, 10
do not lift at all, and 15 are mixed. So the corner-overlap data, which does cut
out the incidence set exactly, does not by itself say which orbit repairs the rank.

## Result 4: the four incidence orbits live inside a single cover

The group has order 384 and is transitive on the 192 covers, so the subgroup
fixing a cover has order 2. Its non-identity element moves all 8 blocks of that
cover, fixing 0 of them, and therefore splits them into 4 partner pairs. Each pair
lies in one cell orbit, and the four pairs land in the four incidence orbits, one
pair each; every partner pair meets in 2 corners.

That is a structural reading of the number four. The four incidence orbits are not
an arbitrary quadruple singled out by the cover table; they are the four partner
classes of a single cover under the order-2 symmetry that fixes it.

Among the six incidence pairs the value 72 is attained by exactly one pair. It is
recomputed here by exact rational elimination, and the next value up is 93.

## Boundary

- Nothing here touches the axioms and nothing here is a physics claim. The object
  is a finite piece of combinatorics about the cutting of the four-cube, and its
  bearing on the framework is the same as that of the cycles before it: it maps how
  much a covariant table can see.
- Result 1 is a theorem, derived before measurement, and the gates are consistency
  checks on it. What makes them evidence about this object rather than about the
  algebra is that the predicted values were produced by independent exact rank
  computations on tables assembled from the orbits left out, with the pairing gated
  separately.
- Results 2, 3 and 4 are measurements, not theorems. The stratum count, the size
  histogram, the per-stratum ranks, the lifting counts and the partner overlaps are
  reported as measured. Two design predictions were falsified and are reported as
  measured: no stratum attains the ceiling, and lifting is not a stratum property.
- The four-subset census of cycle 765 transfers by Result 1 to the sets of the
  complementary size. That transfer is a corollary of the identity and is not
  separately measured here.
- Some clauses inside the runner's gates are redundant rather than discriminating:
  a rank recomputed with identical arguments, or a quantity re-derived from a
  stored value. They are harmless, but they carry no evidence, and no claim in this
  note rests on them.
- The symmetry used throughout is the group of order 384 described above. No larger
  symmetry of the four-cube is claimed or used.

## Runner

`physical_cell_cutting_orbit_strata_cycle767_2026_08_09.py` runs 60 gates and
reports TOTAL: PASS=60 FAIL=0 in 5973 characters of output.
