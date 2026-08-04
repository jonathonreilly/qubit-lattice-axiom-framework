# Extremal adjacency cost of the single cell is a condition on one piece at a time, and at the floor its support is settled completely

Status: unaudited source note. Cycle 730 of the emergent-geometry lane.

## What this settles

Cycle 725 measured the adjacency cost of dissecting one cell of the doubled lattice into
minimal pieces, and found the interval 108 to 128 with both ends attained. That is a
statement about whole dissections. This cycle asks what the two zero-gap certificates say
about a *single* piece, and finds that they turn both ends of the interval into a
membership test applied to one piece at a time.

Write the floor certificate as integers on point orbits with a denominator. For any
dissection of cost C, the per-piece slacks sum to exactly the denominator times C minus
108. At a zero-gap certificate that identity has no room left in it: a dissection attains
108 exactly when every one of its pieces carries slack zero, that is, exactly when every
piece belongs to one explicitly listed set. Cheapness needs no coordination between the
pieces of a dissection; it is a property each piece has or does not have on its own. The
same argument runs at the ceiling with the ceiling certificate.

Equivalently, a zero-gap floor certificate assigns each piece a number that sums to
exactly 108 over *every* dissection whatever its cost, and never exceeds that piece's own
adjacency charge. The excess cost of a dissection is then a sum of nonnegative local
defects, one per piece, vanishing precisely on the rule.

Three further things follow, and all three are measured here.

1. The rule is necessary and not sufficient. Of the 51 orbits in the floor rule, 38 occur
   in dissections drawn from that rule and 13 cannot; at the ceiling, 21 of 23 occur and 2
   cannot. The local condition over-approximates the extremal support, strictly.

2. At the floor the exclusions are themselves local. Force one rule piece in, delete every
   rule piece meeting it, and look for a sample point with no surviving piece over it.
   That single deduction step rules out 624 of the 2416 floor-rule pieces, in 13 orbits,
   every one of them at the first round, with no branching and no dependence on the order
   in which points are visited. The inference is short: a dissection of cost 108 has every
   piece on the rule by the slack identity, and it induces an exact cover of the sample
   points because none of them sits on a boundary, so a piece the step strands lies in no
   cost-108 dissection at all. The 13 orbits it rules out and the 38 the enumeration
   exhibits are disjoint, and together they are the whole rule, so the refutation route
   and the realization route control each other.

3. At the ceiling the same step returns no verdict on any of the 1040 pieces, and the two
   ceiling exclusions rest on the whole search instead. Minimality is local both in the
   bound and in the exclusion of pieces that never participate; maximality here is local
   in the bound alone.

The reason this is worth recording beyond the dissection problem is the shape of the
statement. The framework's admissibility content in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is a single fixed local
rule that selects, site by site, which local possibilities remain available. An extremal
adjacency cost that reduces to per-piece membership in a fixed list has the same logical
form: a global optimum recovered as a local availability test, with the certificate
playing the part of the fixed rule.

## Objects

The cell is the unit 4-cube spanned by three lattice directions and one tick, with 16
corners. A piece is a five-corner subset of unit content; there are 4368 five-subsets and
2672 of them have volume 1/24, so a dissection of the cell uses exactly 24 pieces. The
nonzero scaled volumes take the values 1, 2 and 3, so 1/24 is the floor and no coarser
piece can be substituted.

The cost of a piece is its adjacency charge: the number of corner pairs whose separation
in the three spatial directions exceeds one step. Over the 2672 minimal pieces the charge
spectrum is 3 with multiplicity 64, 4 with 384, 5 with 1152, 6 with 768 and 7 with 304.
Charging every piece its cheapest or dearest value gives only the interval 72 to 168 by
counting, against the measured 108 to 128, so the interval is not a counting fact.

The cell keeps all 24 proper rotations, and with the tick flip the symmetry group has 48
elements. The 2672 pieces fall into 57 orbits of sizes 16 and 48, and adjacency charge is
constant on each orbit, so the certificate program can be written one row per orbit.

## Method: certificates and witnesses, no solver in the artifact

The bound is carried by sample points, not by faces. Weights are chosen past the
barycentric bound of the cell -- corner coordinates are bounded by 3 and the weight total
is 12810 -- which makes the 2736 sample points generic: no two collide under the group,
and 0 of them lie on the boundary of any piece. Because no sample point is on a boundary,
every point lies strictly inside exactly one piece of any dissection, so a per-piece
inequality summed over a dissection gives a valid bound with no symmetry assumption at
all. Symmetry only shortens the program.

A floor certificate is a vector of integers on point orbits together with a denominator,
such that on every one of the 2672 pieces the weighted point count does not exceed the
denominator times that piece's charge. Summing over a dissection gives the bound. The
ceiling certificate reverses the inequality. Both are checked here in integer arithmetic
over every piece, and the tightest row is recomputed in unbounded integers to confirm no
overflow.

Dissections are produced by exact cover over sample points, with no cost objective
anywhere in the search: the cost of what comes back is read off afterwards. Refutations
use two routes, both deterministic and neither a solver -- a node-capped backtracking
cover search, and the single deduction step described above. Realized counts from search
are lower bounds on what occurs; refutations are conclusive.

## Results

**Two zero-gap certificates.** The floor certificate has denominator 24 and value 2592,
which is exactly 108 times 24, so the cost is at least 108. The ceiling certificate has
denominator 6 and value 768, exactly 128 times 6, so the cost is at most 128. Both are
valid on all 2672 pieces and both round to the measured interval. The floor certificate
survives rescaling by 2, 3 and 5 -- denominators 48, 72 and 120 give the same bound --
confirming that the denominator is a carrier, not a claim.

**Both certificates are discriminating.** Raising a single live weight on a tight row
makes the floor inequality fail somewhere, and adding a single point to a live column of a
tight row makes that row violate its own bound. Neither gate holds by construction.

**The rule.** 2416 pieces sit on a tight floor row and 1040 on a tight ceiling row; 784
are on both and none is on neither. Rule membership never splits an orbit, as the
certificate is orbit-indexed. The floor rule spans 51 orbits and the ceiling rule 23. The
6 orbits the floor rule excludes, 256 pieces, are two recognisable shapes: 4 of them carry
a pure-tick edge and 2 carry a body diagonal.

**The locality statement, on real dissections.** With no cost objective used anywhere,
exact cover restricted to the floor-rule pool returns a dissection of 24 pieces at cost
108; restricted to the ceiling-rule pool, cost 128; unrestricted, cost 114. The slack
identity holds exactly on all three: floor slack 0 and ceiling slack 120 at cost 108,
480 and 0 at cost 128, 144 and 84 at cost 114. The 24 monotone corner paths dissect the
cell at cost 108 with every piece on the rule. The sharpest witness is a dissection at
cost 110 with exactly one off-rule piece, whose own slack is 48, which is 24 times the
2 units of excess -- the whole cost excess is carried by that one piece.

**Necessary, not sufficient.** Drawing 200000 dissections from the floor rule uses 38 of
its 51 orbits; from the ceiling rule, 21 of its 23. Forcing a piece of 9 floor orbits, 432
pieces, leaves the whole cover search empty, and likewise for 2 ceiling orbits, 96 pieces.
The same search is not vacuously empty: forcing each of the 24 pieces of an exhibited
floor dissection in turn returns a dissection at cost 108 in 22 of the 24 cases and never
returns the empty answer, and at the ceiling all 24 return a dissection at cost 128.

**The single deduction step.** Over the whole floor rule it rules out 624 of 2416 pieces
in 13 orbits, all at the first round. Those 13 orbits plus the 38 the enumeration exhibits
are the whole 51-orbit rule, with no overlap and no gap, and the split never cuts an
orbit. Over the whole ceiling rule it rules out 0 of 1040.

**The witness is nameable.** For the first floor piece the step refutes, the stranded
sample point is exhibited: 76 rule pieces contain it, all 76 overlap the forced piece, and
the forced piece does not contain it -- so once that piece is in, the point cannot be
covered. Exactly one piece of the already-exhibited stencil dissection contains the same
point, so the point is perfectly coverable in general; it is the forcing that strands it.

**Both supports are settled.** At the floor, 38 of 51 orbits occur and the other 13
cannot, with none left open. At the ceiling, 21 of 23 occur and the other 2 cannot.

## Independent cross-checks performed

- Every headline number was recomputed by a second route that differs from the runner's at
  each step -- pieces by determinant sign rather than by stored inverse, orbits by
  generator closure rather than by the stored labelling, containment by integer facet
  half-spaces rather than by barycentric coordinates, and cost by spatial Hamming distance
  rather than by restricted L1 separation. All agreed, with no disagreement recorded.
- The witness above was re-derived entirely from facet half-spaces, with the stencil
  rebuilt from the 24 monotone corner paths rather than imported: the same 76 containing
  pieces, the same complete overlap, the same excluded forced piece, and exactly one
  stencil piece over the point. The two containment routes agree piece for piece.
- Overlaps in that witness are certified by a sample point strictly interior to both
  pieces, which proves overlap outright; a failed separating-hyperplane search would only
  have been corroboration, and was run separately as such.
- The cover search was re-run under three unrelated point orders. No order ever produced a
  contradicting verdict; disagreements between orders are only settled against unsettled.
- Carve-out, named for the record: the recorded output settles 9 of the 13 refuted floor
  orbits by whole search inside the artifact. The remaining 4 were settled the same way
  under two unrelated point orders outside the artifact; those runs are not part of the
  recorded output, and inside the artifact those 4 orbits rest on the deduction step.
- The certificates were re-derived at three rescalings and the tightest row recomputed in
  unbounded integers.

## Boundary and honest read

- The deduction step is a floor phenomenon here. It returns no verdict at the ceiling, so
  the two ceiling exclusions rest on the whole search route alone. That asymmetry is a
  measured result of this cycle, not a limitation of effort.
- Realized-orbit counts from enumeration are budget-dependent lower bounds. Raising the
  budget can only raise them. The refutations are not budget-dependent in the same way:
  the deduction step is order-free and terminates in one round.
- The rule is a strict over-approximation of the extremal support at both ends, so
  membership in it certifies nothing about a single piece beyond eligibility.
- The certificate denominator is a carrier, not a claim. Nothing here says 24 or 6 is the
  smallest denominator that works.
- Sample points certify the bound and the covers; they are not a proof device for
  regularity, face-to-face structure, or any statement about the block. This cycle
  measures the single cell.
- The locality statement is about this cost function on this object. It is offered as a
  structural echo of the admissibility form, not as a derivation of it.

## Artifacts

- Runner: `scripts/physical_local_extremality_rule_cell_cycle730_2026_08_04.py`
- Recorded output: `outputs/physical_local_extremality_rule_cell_cycle730_2026_08_04_cold_2026-08-04.txt`
- Receipt: `outputs/physical_local_extremality_rule_cell_cycle730_2026_08_04_receipt_2026-08-04.json`

The runner reports `TOTAL: PASS=45 FAIL=0`. The receipt is transcribed from the recorded
output; the runner does not write it. Every number quoted above appears in that output,
apart from the cross-check carve-out named in prose in the section above.
