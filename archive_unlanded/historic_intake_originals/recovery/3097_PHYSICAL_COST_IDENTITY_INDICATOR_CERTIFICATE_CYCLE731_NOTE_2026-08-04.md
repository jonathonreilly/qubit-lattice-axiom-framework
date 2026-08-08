# The adjacency cost of a cell dissection is 108 plus the number of its pieces outside one fixed list

Status: unaudited source note. Cycle 731 of the emergent-geometry lane.

## What this settles

Cycle 725 measured the adjacency cost of dissecting one cell of the doubled lattice into
minimal pieces and found the interval 108 to 128, with both ends attained. Cycle 730 showed
that at a zero-gap certificate, attaining an end of that interval is a membership test
applied to one piece at a time. This cycle asks what the slack of such a certificate does
*away* from its tight set, and finds that at the floor it does the least possible thing.

An exhibited floor certificate with denominator 216 has, over all 2672 minimal pieces,
slack spectrum exactly 0 and 216 -- zero and the denominator, with nothing in between. The
per-piece slacks over any dissection sum to the denominator times the cost minus the
certificate value, and that value is exactly 108 times the denominator, so a slack that can
only be 0 or the denominator turns the inequality into an equality with no rounding left in
it: the cost of a dissection is 108 plus the number of its pieces outside the certificate's
support. That holds for every 24-piece dissection of the cell whatever its cost, and it is
not a bound but a formula. The cost of a dissection is a count.

Three things follow, and all three are measured here.

1. The bound at the other end becomes a statement about membership. Cost is at most 128, so
   at most 20 of the 24 pieces lie outside the support, so every dissection of the cell
   contains at least 4 pieces inside it. A dissection attaining 128 contains exactly 4.

2. The support is settled at the floor. It is 38 orbits, every one of which occurs in a
   dissection of cost 108 all of whose pieces lie inside it, and six such dissections
   already realize all 38 while no five of the 38 forced completions do.

3. The ceiling admits no such reading, and the reason is an exact integer identity rather
   than a failed search. Five of the 57 orbit rows carry an integer dependency with
   coefficients summing to zero; the same combination of their adjacency charges is not
   zero. An indicator at either end would need that combination to be reproduced by a 0/1
   pattern, and at the floor it is, while at the ceiling four of the five orbits are forced
   tight in every zero-gap certificate and the one remaining coefficient cannot reach it.

The last point is the general one. Because a weighting that gives every piece orbit the
same total lies in the span of the certificate columns, *every* dependency among the orbit
rows has coefficient sum zero, and therefore every dependency is an exact identity on the
slacks that does not depend on which certificate was chosen. The five-orbit relation used
here is one instance of that mechanism, not a special object: a complete sweep of the
minimal-support five-element dependencies finds 185 of them, all of coefficient sum zero,
of which 49 have a nonzero charge combination.

The reason this is worth recording beyond the dissection problem is the shape of the
statement. The admissibility content in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is a single fixed local rule
that selects, site by site, which local possibilities remain available. A global cost that
equals a fixed baseline plus a count of sites failing one fixed local test has that form
exactly: the optimum is not merely certified locally, it is *computed* locally, and the
excess is a defect density.

## Objects

The cell is the unit 4-cube spanned by three lattice directions and one tick, with 16
corners. A piece is a five-corner subset of unit content; there are 4368 five-subsets and
2672 of them have volume 1/24, so a dissection of the cell uses exactly 24 pieces. The
scaled volumes of the five-subsets take the values 0, 1, 2 and 3, so the least nonzero one
is 1 and no coarser piece can be substituted.

The cost of a piece is its adjacency charge: the number of corner pairs whose separation in
the three spatial directions exceeds one step. Over the 2672 minimal pieces the charge
spectrum is 3 with multiplicity 64, 4 with 384, 5 with 1152, 6 with 768 and 7 with 304.

The cell keeps all 24 proper rotations, and with the tick flip the symmetry group has 48
elements. The 2672 pieces fall into 57 orbits of sizes 16 and 48, and adjacency charge is
constant on each orbit, so a certificate can be written one row per orbit.

## Method: certificates and witnesses, no solver in the artifact

The bound is carried by sample points, not by faces. Weights are chosen past the
barycentric bound of the cell -- corner coordinates are bounded by 3 and the weight total is
12810 -- which makes the 2736 sample points generic: no two collide under the group, and 0
of them lie on the boundary of any piece. Because no sample point is on a boundary, every
point lies strictly inside exactly one piece of any dissection, so a per-piece inequality
summed over a dissection is a valid bound with no symmetry assumption at all. Symmetry only
shortens the program. The number of sample points per orbit is not the orbit size, so the
row carries real content and not the piece count.

A floor certificate is a vector of integers on point orbits together with a denominator and
a constant, such that on every one of the 2672 pieces the weighted point count does not
exceed the denominator times that piece's charge; the ceiling certificate reverses the
inequality. Both are checked here in integer arithmetic over every piece. The runner
carries no dissection literals: the monotone stencil is rebuilt from the permutations of
the four coordinates, and every other dissection is produced by exact cover over sample
points with no cost objective anywhere in the search, the cost being read off afterwards.

Ranks and dependencies among the orbit rows are computed by fraction-free integer
elimination with a per-row content reduction, so nothing in the artifact leaves the
integers, and every dependency the sweep reports is re-multiplied against the full rows and
checked to residual 0.

## Results

**The floor certificate is an indicator.** Denominator 216 and constant 756, valid on all
2672 pieces, with value 23328, which is exactly 108 times 216, so the gap is zero. Its
slack spectrum over all 2672 pieces is exactly 0 and 216, and the pieces of slack zero are
1792 in number, spanning 38 orbits. Validity by itself is a weak property, so the sweep
reported here tests validity and the zero gap together: 0 of 116 single-step moves in the
certificate entries or the constant survive both.

**The cost identity, on real dissections.** Four dissections are built and their costs read
off afterwards: 108, 114, 108 and 128. Against the count of their pieces outside the
support the identity is exact in all four cases -- 108 with 0 outside, 114 with 6, 108 with
0, 128 with 20. The mechanism is checked separately: the rows of a dissection sum to the
point census, which is what makes the per-piece slacks add to the denominator times the cost
less the value, and summing the certificate over any dissection returns 23328 by a second
route.

**The identity is not vacuous.** Of the 31 orbits that occur in those four dissections, 0
can be moved across the support boundary and leave the identity intact.

**The membership corollary.** The ceiling caps cost at 128, so at most 20 pieces of a
dissection lie outside the support and every dissection holds at least 4 inside; the fewest
seen here is 4.

**The support is exactly the tight set.** In a cost-108 dissection the slacks are
nonnegative and sum to zero, so every piece is tight -- that gives one inclusion. For the
other, each of the 38 support orbits sits in a cost-108 dissection all of whose pieces lie
in the support. Six of those, seeded at orbits 12, 13, 45, 50, 53 and 56, already realize
all 38, and a complete sweep of all 501942 five-subsets of the 38 shows that no five of the
forced completions cover all 38.

**The ceiling admits no indicator.** The exhibited ceiling certificate has denominator 3 and
value 384, exactly 128 times 3, and its slack spectrum is 0, 2, 3 and 4 -- not zero and the
denominator -- with 944 pieces tight in 21 orbits. That is a measurement of one certificate.
The statement that no ceiling certificate can be an indicator is separate and rests on an
integer identity: five orbit rows are dependent with coefficients 3, 1, -1, -1 and -2, at
residual 0; those coefficients sum to 0 and combine the charges 4, 6, 3, 5 and 6 to -2. The
combination therefore equals twice the denominator on every certificate, which is confirmed
on 59 weight vectors. Four of the five orbits sit in an exhibited cost-128 dissection, so a
zero-gap ceiling certificate is tight on all four, leaving three times the fifth slack equal
to twice the denominator. Hence 3 divides the denominator, 3 is the least one and it is
attained. An indicator at the ceiling would need the combination to be 2, and 3 times an
integer is never 2; at the floor the corresponding pattern 0, 1, 0, 1, 1 gives -2 and does.
Changing any single coefficient destroys the dependency, in 10 of 10 attempts.

**The mechanism behind that identity, and its population.** The 57 orbit rows span 13
dimensions, so their dependencies form a 44-dimensional space and the five-orbit relation is
one of many. Adjoining a constant column does not raise the span, so a weighting giving
every piece orbit the same total exists, and consequently every dependency has coefficient
sum zero -- which is exactly what makes each one an identity on the slacks independent of
the certificate. Up to sign and positive scale the rows fall into 49 classes of the same
span 13, and a complete sweep of all 1906884 five-element supports among those classes finds
185 minimal-support dependencies, each verified to residual 0, and every one of coefficient
sum 0 as the span argument requires. Their charge combinations are -2 with multiplicity 22,
0 with 136, 2 with 26 and 4 with 1; so 49 of the 185 carry an exact slack identity, and
those do not all take the same value. What distinguishes the relation
used above is not that it is rare but that its support is minimal in a strong sense: on
those five orbits the dependency is unique up to scale, and no four of them carry one.

**What the support looks like locally.** By charge, the counts of pieces and of support
pieces are 64 of 64 at charge 3, 384 of 384 at charge 4, 960 of 1152 at charge 5, 384 of 768
at charge 6 and 0 of 304 at charge 7. So charge at most 4 forces membership and charge 7
forces exclusion, deciding 752 of the 2672 pieces, while the remaining 1920 at charge 5 or 6
split both ways. None of the 6 local invariants swept separates the 38 support orbits from
the other 19.

## Independent cross-checks performed

- Every headline number was recomputed by a route differing from the runner's at each step:
  volumes by rational elimination rather than by stored integer inverses, adjacency charge
  by bit population count on corner codes rather than by restricted separation, the group by
  breadth-first closure rather than from the stored table, containment
  by permutation-expanded determinants rather than by barycentric coordinates, and the row
  dependencies by an exact rational nullspace of the whole 57-row matrix rather than by
  integer elimination. All agreed.
- Every headline gate was tested for discrimination by perturbing the object it protects.
  The zero-gap, two-value and support-size conditions each reject all single-step moves in
  the certificate entries and all wrong denominators tried, including the homogeneous double
  of the stated one; the ceiling validity condition rejects every single-step move in the
  ceiling entries; every one of the 31 orbits occurring in the four dissections breaks the
  cost identity when moved across the support; stripping the superincreasing weights
  collapses the sample points onto each other and onto piece boundaries;
  no single substitution among the six seeds still realizes all 38; and no single-entry
  corruption of the five rows survives either rank condition.
- The claim that a minimal-support dependency is distinctive was tested and found too
  strong, then replaced by the complete sweep reported above. The population census is the
  corrected statement; the earlier reading of a truncated listing, which suggested every
  nonzero charge combination is plus or minus 2, is refuted by the count of 4 appearing once.
- The certificate literals are read from stored arrays rather than retyped, and the runner
  rebuilds every dissection at run time rather than carrying one.

## Boundary and honest read

- Validity of the floor rows, taken alone, is weak: lowering a live entry preserves it while
  destroying the value, and the homogeneous double of the denominator preserves it too. What
  is claimed here is the conjunction of validity, zero gap, the two-value slack spectrum and
  the exact support size, and that is what the perturbation sweep tests.
- That the exhibited ceiling slack spectrum is not zero-and-the-denominator is a negative
  property of one certificate, and negative properties survive being perturbed away from the
  object they describe. It is recorded as a measurement of that certificate and nothing more;
  the claim that no ceiling indicator exists rests on the integer identity, which is a
  positive statement and does discriminate.
- The identity-perturbation sweep reaches the 31 orbits that occur in the four exhibited
  dissections. The remaining orbits, the 57 less those 31, do not occur in them, so moving
  those across the support cannot disturb an identity checked on those four; the sweep's
  reach is the 31 and no more is claimed.
- The five-orbit relation is not unique and is not claimed to be. The measured statements
  are that its support is minimal, that 185 such relations exist among the 49 classes, and
  that 49 of them carry a nonzero charge combination.
- The floor denominator 216 is a carrier, not a claim; nothing here says it is the smallest
  that works. The ceiling statement is different in kind: there 3 is shown least by the
  divisibility argument above, not by a search.
- The support statement is settled for the 38 orbits by forced completion inside the pool.
  The claim that six suffice and five do not is scoped to those forced completions, which
  are one dissection per orbit, not to all cost-108 dissections.
- Sample points certify the bound and the covers; they are not a proof device for
  regularity, face-to-face structure, or any statement about the block. This cycle measures
  the single cell.
- The locality reading is about this cost function on this object. It is offered as a
  structural echo of the admissibility form, not as a derivation of it.

## Artifacts

- Runner: `scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04.py`
- Recorded output: `outputs/physical_cost_identity_indicator_certificate_cycle731_2026_08_04_cold_2026-08-04.txt`
- Receipt: `outputs/physical_cost_identity_indicator_certificate_cycle731_2026_08_04_receipt_2026-08-04.json`

The runner reports `TOTAL: PASS=45 FAIL=0`. The receipt is transcribed from the recorded
output; the runner does not write it. Every number quoted above appears in that output.
