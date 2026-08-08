# Scale-free adjacency ceiling and the dissection cost bracket — Cycle 724

Date: 2026-08-03

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Runner: `scripts/physical_scale_free_adjacency_dissection_bracket_cycle724_2026_08_03.py`
(23 PASS / 0 FAIL, exit 0). Every number below is exact integer arithmetic over a
complete enumeration — determinants by integer cofactor expansion, affine ranks by
fraction-free integer elimination — except the three ratios, which are exact
rationals printed at one decimal place. The interior-disjointness predicate is
decided by an integer separating-hyperplane scan and independently cross-checked by
a linear programme, the runner's one floating-point surface; that cross-check is
fail-closed: only a proven-infeasible programme certifies disjointness, and any
other unsuccessful solver termination aborts the run.

## Supplied model, and what stays open

Everything in this note is a theorem of a **supplied** structural model, not of the
framework axioms alone. The model: assembly cells are 4-simplices — five vertices
with all ten vertex pairs graded — on the tick-extended domain `Z^3 x {tick}`, and a
dissection is a family of such cells with pairwise disjoint interiors whose volumes
sum to the region's. What each premise actually supplies:

- the **Lattice** axiom supplies the spatial `Z^3` nearest-neighbour adjacency that
  grades the vertex pairs — nothing else;
- the registered **kinetic-isotropy primitive** supplies the equal tick/edge graining
  under which the tick coordinate enters the model — no cell selection and no
  rule-to-tick correspondence;
- the simplex/corner/dissection structure itself, and the fixed-two-tick spatial
  refinement, are supplied here as the declared domain of the theorem.

Two identifications stay **open**, exactly as the active review queue records: the
physical tick–Admissibility realization bridge (which rule variation corresponds to
which tick), and the identification of physical assembly cells with
pairwise-adjacency simplices. A nonsimplicial cell complex whose actual 1-skeleton
edges are nearest-neighbour does not require every vertex pair to be adjacent — the
cubic cell is the elementary example — and nothing in the framework selects
simplicial cells. This note therefore does **not** remove any physical construction
escape; it closes the simplex route only, inside the supplied model.

## Why this exists

An in-flight, unlanded predecessor (cycle 723, provenance only — see Dependencies)
measured that no **corner** simplex cell of the tick-extended unit cell is
adjacency-only: every such cell uses at least one vertex pair whose spatial
footprint reaches two sites or more. That measurement was corner-restricted, so it
left open the question of whether a simplex cell on a refined lattice, or with
vertices at other rational positions, might be adjacency-only after all.

This cycle closes that question for the entire simplex model. The proof is analytic
— a clique lemma plus an affine-span count — with one finite cross-check of the
lemma on a 125-site box. The adjacency-only condition is shown to bound the
**affine rank** of the vertex set, which is a scale-free statement: it holds for any
lattice resolution, any box, any vertex positions whatever. Within the supplied
model the cell count then becomes a cost question rather than a feasibility
question, and the rest of the note brackets that cost. The physical reading of that
closure is bounded by the open identifications named above.

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
any lattice scale, any vertex choice, any box. The corner restriction used by the
unlanded predecessor is not needed and is not doing any work. The rejector confirms the gate
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
| ratio minimised by | cost 7, volume 3 units of 24 |
| same ratio restricted to the floor-cost cells | 72 |

The cost of **any** corner dissection is therefore at least **56**. The unlanded
predecessor reported 48 by chaining a facet census with a cone relation and volume
bookkeeping; that number carries no dependency edge here and is not load-bearing —
the present argument is a single line of volume-weighted arithmetic over a complete
census, and it lands higher.

Two things are worth stating because they cut against the natural reading. First,
the ratio-minimising cells are not the cost-minimising ones: the 64 floor-cost cells
sit at ratio 72, well above 56. Second, 56 is a **lower bound only**. The runner
identifies the ratio-minimising `(cost, volume) = (7, 3)` cell class; it neither
constructs nor searches for a volume-complete, pairwise interior-disjoint family
built from it. No claim is made that any dissection attains 56, and the
pairwise-disjointness constraints could raise the true optimum — the unimodular
restriction below shows exactly that kind of tightening, from 56 to 96.

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

Benchmark each of the 24 cells at cost five: a cost-3 cell saves 2, a cost-4 cell
saves 1, and cells of cost 6 or 7 only add, so the total cost is **at least** 120
minus the total saving `2·n3 + n4` (the exact identity is
`C = 120 − 2·n3 − n4 + n6 + 2·n7`, whose omitted excess is nonnegative). The saving
is capped by two clique numbers:

- the largest pairwise interior-disjoint family of **floor-cost** cells has size **8**;
- the largest such family of **below-average-cost** cells (cost 3 or 4) has size **16**,
  and its witness contains no floor-cost cell at all.

Hence the saving `2·n3 + n4 = n3 + (n3 + n4)` is at most 8 + 16 = 24, and every
unimodular corner dissection costs at least **96**. A dissection of all floor-cost
cells, which would cost 72, does not exist.

For the upper end, the monotone path stencil — the 24 paths that step from the cell's
zero corner to its all-ones corner one axis at a time — is a genuine dissection: all
24 cells are of minimal volume, no two overlap, and their volumes sum to the whole
cell. Its cost profile is 12 cells at cost 4 and 12 at cost 5, total **108**, and its
cheapest cell costs 4, so it never attains the per-cell floor of 3.

**Bracket.** Unimodular corner dissections cost between **96 and 108**; arbitrary
corner dissections cost at least 56. The unlanded predecessor's bracket was 48 to
108 (provenance only).

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

- Every claim here is a theorem of the supplied tick-extended simplex/dissection
  model. The physical tick–Admissibility realization bridge and the identification
  of physical assembly cells with pairwise-adjacency simplices are open;
  nonsimplicial cell complexes whose 1-skeleton edges are nearest-neighbour are
  untested and are not excluded by anything in this note.
- The affine-flatness result is scale-free and vertex-free, and it is the one claim
  here with no enumeration inside it beyond the 125-site clique check. Its exact
  statement: a pairwise spatial-nearest-neighbour vertex set in `Z^3 x` one tick
  coordinate has affine rank at most two. Everything after it is a **cost**
  statement, and every cost statement is over corner vertex sets of a specified cell.
- The floor of 56 is a lower bound only. No dissection attaining it is exhibited,
  and no claim is made that it is attainable.
- The floor of 96 is a floor over **unimodular** corner dissections. Dissections
  mixing volumes are covered only by the weaker floor of 56.
- The bracket 96 to 108 is not closed. No claim is made that 108 is optimal; the
  runner reports the bracket, not a minimiser.
- The clique numbers 8 and 16 are maxima over the corner census only. They are not
  bounds on any refined or non-corner family.
- The refined measurement is at one refinement step. No sequence, limit, or asymptotic
  statement is made.
- The three ratios are exact rationals of measured integers, printed at one decimal
  place; the linear-programme cross-check tolerance and the refinement rescaling
  factor are supplied constants of the runner.
- Nothing here is a statement about the second-variation form, its spectrum, or any
  continuum quantity. This cycle is combinatorics of the supplied tick-extended
  simplex model.

## Honest auditor read

The strongest claim is the affine-flatness ceiling: it is two lines of argument, its
one enumeration is a 125-site box, and it strictly generalises the unlanded
predecessor's corner-restricted result while being cheaper to check. The bound of 56
is next, being a single volume-weighted minimum over a complete census — a lower
bound with no attainability claim. The largest framing risk of the whole note is a
physical over-read: none of these numbers selects the simplex model as the physical
assembly domain, which is why the supplied-model section stands first.

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
from itself. The cross-check is fail-closed: only a proven-infeasible programme counts
as a disjointness certificate, and any other unsuccessful solver termination aborts
the run rather than silently agreeing with the hyperplane scan.

The weakest framing risk is the refined measurement, and it is stated against
interest above: 80 is a floor over a region, not a count, and it does not exceed 108.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the Lattice axiom's spatial `Z^3`
  nearest-neighbour adjacency, which grades the vertex pairs. That is the only thing
  the axiom supplies here; it does not select the cell model.
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the
  registered primitive supplying the equal tick/edge graining under which the tick
  coordinate enters the supplied model. It supplies no cell selection and no
  rule-to-tick correspondence.

Context, cited without a dependency edge — none of the following is load-bearing.
Landed, unaudited, not used in any formula or gate here:
`PHYSICAL_DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_CYCLE695_NOTE_2026-07-25.md`
(the monotone path stencil appears there in an edge-direction census; this runner
constructs and verifies the stencil directly from the vertex coordinates) and
`PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md` (the
covariance ceiling of unit-cell triangulations). Provenance only, absent from main
at the time of writing: the in-flight cycle 723 corner-restricted adjacency result
and its floor of 48, `physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03`;
and the in-flight cycle 721 and cycle 722 frame-label measurements
`physical_stencil_derived_centrality_cycle721_2026_08_02` and
`physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02`. The results of this
note are independent of all of them; every enumeration and witness is rebuilt
locally by the runner.

## Review record

Iteration 1 of the combined adversarial science review (Sol, 2026-08-08) returned
FIX_THEN_PROCEED. The broad physical claim that this cycle "removes the physical
construction escape", and the attribution of the tick-extended assembly domain to
the Lattice axiom, were demoted to what the runner proves: a bounded combinatorial
theorem of the supplied tick-extended simplex/dissection model, with the physical
tick–Admissibility realization bridge and the simplex identification left open. The
unsupported claim that the arbitrary-dissection bound 56 is attained (and hence
immune to disjointness tightening) was removed; 56 stands as a lower bound only.
The earlier broad wording must not be cited as a passed gate. The same review made
the linear-programme cross-check fail-closed, replaced rounded floating determinants
and ranks with exact integer arithmetic, and moved the two non-load-bearing
dependency edges to context while adding the kinetic-isotropy premise edge.

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
   grows, and that is the quantity a frame-label reading would need.
4. **The facet floor.** The unlanded predecessor's facet count of 18 was read off a
   census. Whether it is forced by the facet's own adjacency graph alone is a
   self-contained question at one dimension lower, and would tighten the chain the
   floor of 96 rests on.
