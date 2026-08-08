# Scale-free adjacency ceiling and the dissection cost bracket — Cycle 724

Date: 2026-08-03

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Runner: `scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py`
(23 PASS / 0 FAIL, exit 0). Every number below is exact integer arithmetic over a
complete enumeration, except the three ratios, which are exact rationals printed at
one decimal place. The interior-disjointness predicate is decided by an integer
separating-hyperplane scan and independently cross-checked by a linear programme.

## Why this exists

The preceding cycle measured that no **corner** assembly cell of the tick-extended
unit cell can be built from the six nearest-neighbour directions the LATTICE axiom
names: every such cell uses at least one edge whose spatial footprint reaches two
sites or more. It left open the obvious escape — a construction on a refined cell,
or with vertices at other rational positions, might be adjacency-only after all,
and then the frame-label structure of cycles 721 and 722 would rest on a choice of
cell rather than on the axiom.

This cycle removes that escape, and it removes it without enumerating anything. The
adjacency-only condition is shown to bound the **affine rank** of the vertex set,
which is a scale-free statement: it holds for any lattice resolution, any box, any
vertex positions whatever. The cell count then becomes a cost question rather than a
feasibility question, and the rest of the note brackets that cost.

## An adjacency-only vertex set is affinely flat

Call the spatial footprint weight of a pair of vertices the L1 distance between their
spatial parts, and call a pair **exceeding** when that weight is two or more. A cell
is adjacency-only when none of its vertex pairs exceeds.

**Clique lemma.** Any set of lattice sites that is pairwise at L1 distance at most
one occupies at most **two distinct positions**. Three sites cannot be mutually
adjacent-or-equal unless two of them coincide. Verified by complete enumeration over
the 125 sites of the box from -2 to 2 in each axis: **zero** offending triples.

**Consequence.** An adjacency-only vertex set in the tick-extended lattice therefore
lies in a slab of at most two spatial sites, crossed with the tick axis. Over every
such two-site slab and every five-subset of it, the affine rank takes the values
{1, 2} — never more — and every five-subset has cell volume exactly **zero**.

So no nondegenerate 3-simplex and no nondegenerate 4-simplex is adjacency-only, at
any lattice scale, any vertex choice, any box. The corner restriction of the previous
cycle is not needed and is not doing any work. The rejector confirms the gate
discriminates: the tight corner cell built from the origin and the four unit steps
has affine rank 4 and adjacency cost exactly 3, so it is correctly refused.

## The per-cell floor is three, and the cells that attain it

Define the adjacency cost of a cell as the number of its ten vertex pairs that exceed.
Over the complete corner census — the 3008 nondegenerate five-subsets of the 16
corners — the minimum cost is **3**, attained by exactly **64** cells.

Every one of those 64 has the same shape: a centre corner carrying both ticks, plus
three leaves on three distinct spatial axes. The runner gates that structure
directly, as the multiset of per-vertex exceeding degrees together with the
both-ticks and three-distinct-axes conditions, and gates that all 64 are of minimal
volume. The floor of 3 persists unchanged on the refined cell.

## The volume-weighted floor for arbitrary corner dissections

A dissection of the cell is a family of nondegenerate cells with disjoint interiors
whose volumes sum to the cell's. Weighting each cell by its volume gives a floor that
needs no disjointness bookkeeping at all: the total cost is at least the cell's volume
times the smallest cost-per-unit-volume in the census.

| quantity | value |
| --- | --- |
| smallest cost per unit volume, corner census | 56 |
| attained at | cost 7, volume 3 units of 24 |
| same ratio restricted to the floor-cost cells | 72 |

The floor for **any** corner dissection is therefore **56**. This supersedes the
value of 48 reported by the previous cycle, which chained a facet census with a cone
relation and volume bookkeeping; the present argument is a single line of
volume-weighted arithmetic over a complete census, and it lands higher.

Two things are worth stating because they cut against the natural reading. First,
the ratio-minimising cells are not the cost-minimising ones: the 64 floor-cost cells
sit at ratio 72, well above 56, so restricting to them cannot tighten this bound.
Second, the pairwise-disjointness structure does not tighten it either, for the same
reason — the bound is attained by a cell family the disjointness cap never touches.

## The bracket for unimodular dissections

Restricting to cells of the smallest possible volume makes the bound sharp enough to
be interesting. Of the 3008 nondegenerate corner cells, **2672** have volume exactly
one unit of 24, so any dissection built from them uses exactly 24 cells.

| adjacency cost | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- |
| minimal-volume corner cells | 64 | 384 | 1152 | 768 | 304 |

The compatibility graph on these 2672 cells — an edge when two cells have disjoint
interiors — has **1984616** edges, with degrees running from 987 to 1863. A
dissection is a 24-clique in it.

Writing the cost as 120 minus the total saving, where a cost-3 cell saves 2 and a
cost-4 cell saves 1, the saving is capped by two clique numbers:

- the largest pairwise interior-disjoint family of **floor-cost** cells has size **8**;
- the largest such family of **below-average-cost** cells (cost 3 or 4) has size **16**,
  and its witness contains no floor-cost cell at all.

Hence the saving is at most 8 + 16 = 24, and every unimodular corner dissection costs
at least **96**. A dissection of all floor-cost cells, which would cost 72, does not
exist.

For the upper end, the monotone path stencil — the 24 paths that step from the cell's
zero corner to its all-ones corner one axis at a time — is a genuine dissection: all
24 cells are of minimal volume, no two overlap, and their volumes sum to the whole
cell. Its cost profile is 12 cells at cost 4 and 12 at cost 5, total **108**, and its
cheapest cell costs 4, so it never attains the per-cell floor of 3.

**Bracket.** Unimodular corner dissections cost between **96 and 108**; arbitrary
corner dissections cost at least 56. The previous cycle's bracket was 48 to 108.

## Refining the resolution

Halving the lattice spacing gives 27 spatial sites and two ticks, 54 points, and
**2449800** nondegenerate five-subsets. The per-cell floor is still 3. Weighting by
volume exactly as above, and then rescaling to the original units, gives a floor over
the refined region of **80**.

This is the honest reading, and the runner prints it as such: 80 exceeds the coarse
floor of 56, so refining raises the guaranteed minimum — but 80 sits **below** the
achieved coarse count of 108, so nothing here shows that a finer construction must
cost more in absolute count. The refinement tightens the bound; it does not close the
gap, and it does not rule out a cheaper fine construction.

## Boundary

- The affine-flatness result is scale-free and vertex-free, and it is the one claim
  here with no enumeration inside it beyond the 125-site clique check. Everything
  after it is a **cost** statement, and every cost statement is over corner vertex
  sets of a specified cell.
- The floor of 96 is a floor over **unimodular** corner dissections. Dissections
  mixing volumes are covered only by the weaker floor of 56.
- The bracket 96 to 108 is not closed. No claim is made that 108 is optimal; the
  runner reports the bracket, not a minimiser.
- The clique numbers 8 and 16 are maxima over the corner census only. They are not
  bounds on any refined or non-corner family.
- The refined measurement is at one refinement step. No sequence, limit, or asymptotic
  statement is made.
- The three ratios are exact rationals of measured integers, printed at one decimal
  place; the comparison tolerance and the refinement rescaling factor are supplied
  constants of the runner.
- Nothing here is a statement about the second-variation form, its spectrum, or any
  continuum quantity. This cycle is combinatorics of the assembly domain.

## Honest auditor read

The strongest claim is the affine-flatness ceiling: it is two lines of argument, its
one enumeration is a 125-site box, and it strictly generalises the previous cycle's
corner-restricted result while being cheaper to check. The bound of 56 is next, being
a single volume-weighted minimum over a complete census.

The floor of 96 is the place to attack. It chains three separately computed maxima —
the clique numbers 8 and 16 and the census — and each is a search whose correctness
depends on a pruning rule. That pruning rule is exactly where an earlier reading of
this graph went wrong: taking candidates in increasing rather than decreasing colour
order silently under-reports, which produced a below-average clique of 14 and an
inflated floor of 98 before it was caught. The runner therefore recomputes the
floor-cost maximum with the colour bound **removed entirely**, recomputes the
below-average maximum under a **reversed vertex order**, and re-derives both witnesses'
pairwise disjointness straight from the vertex coordinates rather than from the cached
graph. All four cross-checks agree. An auditor who wants to break this should attack
the below-average maximum of 16, which is the one number with no colour-free
confirmation.

The interior-disjointness predicate carries the whole graph, so it is cross-checked by
a structurally different method: a linear programme that maximises the minimum barycentric
weight of a common point. Over all 2016 pairs of floor-cost cells the two methods
disagree **zero** times, and the self-pair rejector confirms a cell is not disjoint
from itself.

The weakest framing risk is the refined measurement, and it is stated against
interest above: 80 is a floor over a region, not a count, and it does not exceed 108.

## Dependencies

- [Direction set versus triangulation covariance](PHYSICAL_DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_CYCLE695_NOTE_2026-07-25.md) — landed, unaudited: the monotone path stencil and its edge-direction census.
- [Proper-cubic covariance ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md) — landed, unaudited: the covariance ceiling of unit-cell triangulations.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the LATTICE axiom's 6-NN adjacency and proper cubic rotations, which define the admissible set here.

Context, cited without a dependency edge: the in-flight cycle 723 corner-restricted
adjacency result and its floor of 48, which this cycle supersedes,
`physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03`; and the in-flight
cycle 721 and cycle 722 frame-label measurements
`physical_stencil_derived_centrality_cycle721_2026_08_02` and
`physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02`. None of the three is
resident on main at the time of writing, so none carries a dependency edge here; the
results of this note are independent of all three.

## What this opens

1. **Closing the bracket.** The gap between 96 and 108 is a finite search over
   24-cliques of an explicit 2672-vertex graph. Branching on an uncovered interior
   point is a complete branching, since a dissection contains exactly one cell whose
   interior holds it, so the minimum is reachable by search rather than by argument.
2. **Sharpening the floor.** The saving bound uses two clique numbers separately. The
   weighted maximum over the below-average tier, counting a floor-cost cell twice,
   would replace 8 + 16 by a single number and can only raise the floor.
3. **Refined dissections.** The refined region floor of 80 bounds cost per region, not
   per cell count. Measuring an actual refined dissection would say whether the count
   grows, and that is the quantity the frame-label reading needs.
4. **The facet floor.** The previous cycle's facet count of 18 was read off a census.
   Whether it is forced by the facet's own adjacency graph alone is a self-contained
   question at one dimension lower, and would tighten the chain the floor of 96 rests
   on.
