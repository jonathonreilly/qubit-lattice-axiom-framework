# Exact adjacency-cost bracket for dissections of one tick-box

Status: unaudited source note. Cycle 725 of the emergent-geometry lane.

## What this settles

The LATTICE axiom of [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
supplies adjacency between nearest neighbours of `Z^3` and nothing else. When one
lattice cell is carried through one tick and the resulting box is cut into corner
pieces, every vertex pair inside a piece whose spatial separation is more than one step
is a slot-use the axiom does not supply. Counting those uses over a dissection gives its
**adjacency cost**.

Cycle 723 measured that cost for the monotone-path stencil and found 108 slot-uses per
cell. The obvious worry is that 108 is a property of the chosen stencil rather than of
the box. It is not.

**Over all dissections of the tick-box into minimal-volume corner pieces, the adjacency
cost is bracketed exactly by 108 and 128, and both ends are attained.** The lower end is
not a stencil property: three structurally unlike dissections reach 108. Cost parity is
forced, so the attainable set is exactly the eleven even values from 108 to 128.

**The bracket has an honest scope.** Admitting coarser corner pieces — pieces of volume
2 and 3 alongside the minimal ones — drops the floor to 68, attained by a genuine
sixteen-piece dissection. Minimality of the pieces is precisely what pins 108.

## Objects

The box is one lattice cell carried through one tick: three spatial coordinates and a
tick coordinate, sixteen corners. A **piece** is the convex hull of five corners with
nonzero volume; a **dissection** is a family of pieces with disjoint interiors whose
volumes fill the box. Of the five-corner subsets, 1360 are degenerate and the remaining
3008 have volume 1, 2 or 3 with multiplicities 2672, 320 and 16. The 2672 volume-1
pieces are the **minimal** ones; a minimal-volume dissection therefore uses exactly 24
pieces. Adjacency cost runs from 3 to 7 over minimal pieces and from 3 to 9 over all
pieces.

The symmetry acting here is the axiom's 24 proper cubic rotations of the spatial
coordinates, with the tick fixed. They permute the minimal pieces in 114 orbits of sizes
8 and 24.

## Method: certificates and witnesses, no solver in the artifact

Bounds are carried as integer multiplier vectors and checked directly; attaining
families are carried as piece lists and checked to be genuine dissections. Nothing in
the runner calls an optimiser.

The bounds are proved through **sample points**. A dissection covers every interior
point of the box exactly once, so a bound proved for every family that covers a fixed
set of sample points exactly once holds for every dissection. Two sample families are
built from pinned recipes: a fixed-weight family with one point per minimal piece, and
an invariant family of 2736 points carried by the 24 rotations into 114 point-orbits all
of size 24. Both have zero boundary incidences against all 3008 pieces, which is what
makes the device sound; every piece contains between 6 and 1041 of the invariant points,
and every invariant point lies in some piece.

Disjointness of the attaining families is **decided**, not sampled. Two convex bodies
have disjoint interiors exactly when a direction separates them; all vertices here are
zero-one corners, so differences lie in the ternary cube and a supporting direction may
be taken orthogonal to three ternary vectors — a three-by-three ternary determinant,
hence entries bounded by 4. Sweeping every direction in that range decides the question.

## Results

**The floor is 108 and it is exact.** A fixed-weight integer certificate with support
211 is tight at 2093 points and totals 108. An invariant certificate over the rotation
orbits reaches the same value using eight orbits at denominator 2, tight at 2224 points.
Three unlike dissections attain it, with cost profiles `{4: 12, 5: 12}`,
`{3: 1, 4: 11, 5: 11, 6: 1}` and `{3: 1, 4: 13, 5: 7, 6: 3}`. The first is the monotone
stencil of cycle 723; the other two share no profile with it. 108 is a property of the
box, not of a stencil.

**The ceiling is 128.** An invariant certificate at denominator 3 is tight at 1136
points and totals 128, and dissections attain it.

**Parity is forced, with a clean scope split.** Over the minimal pieces the cost vector
lies in the span of the point-incidence columns together with the all-ones column over
the two-element field — rank 465 on both sample families — so every minimal-volume
dissection has even cost, and each of seven single-piece perturbations of the cost
vector leaves that span. Combined with the bracket, the attainable costs are exactly
108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, every one realised by a checked
dissection. Over all pieces the rank is again 465 but the cost vector is **not** in the
span: the parity relation does not extend past the minimal pieces.

**The scope boundary: 68.** Admitting every corner piece, an invariant certificate at
denominator 6 is tight at 296 points and totals exactly 68, and a sixteen-piece
dissection with volume profile `{1: 8, 2: 8}` attains it. The bracket over all corner
pieces is 68 to 128.

**A denominator law governs how sharp an invariant certificate can be.** Every sample
point-orbit has size 24, so a covariant certificate at denominator D produces a bound
that is a multiple of 24/D — computable in advance with no optimiser. Sixteen rungs
were predicted this way and every one is attained exactly:

| bracket | D = 1 | D = 2 | D = 3 | D = 6 |
|---|---|---|---|---|
| minimal pieces, floor | 96 | 108 | 104 | 108 |
| minimal pieces, ceiling | 144 | 132 | 128 | 128 |
| all pieces, floor | 48 | 60 | 64 | 68 |
| all pieces, ceiling | 144 | 132 | 128 | 128 |

The endpoint fixes the denominator: 108 needs halves, 128 needs thirds, 68 needs sixths.
A single covariant scheme reaching all three needs sixths. Note the dip at D = 3 in the
first row — sharper denominators are not monotonically better.

**This explains cycle 724's floor of 96.** 96 is the largest multiple of 24 at or below
108, so it is exactly the ceiling of integral covariant certificates; integral covariance
is confined to the window 96 to 144. Integrality alone is not the obstruction — the
fixed-weight family carries an integral certificate reaching 108 — it is covariance
together with integrality that caps at 96. Cycle 724's bound was loose, for a reason now
named.

**A single orbit cannot carry the floor.** The best bound obtainable from any one
point-orbit is 84, below 108; eight orbits suffice.

**Every carried bound is locally maximal.** For five representative certificates, all
114 single-orbit unit strengthenings and the uniform strengthening break feasibility, so
none of them is a slack bound dressed up as a sharp one.

**A discriminating negative control.** A cost-72 family of pieces whose volumes sum to
24 is rejected: it has 86 overlapping interior pairs and fails to cover the sample points
exactly once on both families. Volume bookkeeping alone does not make a dissection, and
the certificates correctly do not apply to it.

## Independent cross-checks performed

Beyond the runner's own 26 gates, each headline number was re-derived by different
machinery before this note was written. These cross-checks used a separate scratch
script that is not carried in this change, so the numbers they confirm are exactly the
ones the runner itself prints.

A third sample family on unrelated weights, with zero boundary incidences, reproduces
the cover-once verdict on every carried family including the control. Pairwise interior
intersection was re-decided by linear-programming feasibility rather than by the
ternary-direction sweep, giving identical verdicts — zero overlapping pairs on the
sixteen dissections and 86 on the control. All four bracket endpoints were recomputed by
simplex on the primal relaxation and returned 108, 128, 68 and 128, matching the carried
integer certificates by a route sharing no code with them.

Each load-bearing gate was also shown to discriminate: corrupting one certificate
multiplier drives the least slack negative, swapping one piece out of a 108-dissection
breaks the cover-once property, a deliberately degenerate sample family fails the
boundary-incidence check outright, and the parity test rejects perturbations that change
the cost parity while accepting those that preserve it.

## Boundary and honest read

- 108 is exact **for minimal-volume corner pieces**. It is not a bound on dissections in
  general: coarser corner pieces reach 68. Any downstream use must carry the piece class
  with it.
- The bracket is a statement about one lattice cell carried through one tick. Extending
  it to longer tick runs or larger spatial blocks is open work, not a corollary.
- The sample-point device bounds a **larger** family than the dissections (everything
  covering the points exactly once). Both ends are attained by exhibited dissections, so
  no gap remains here, but the device on its own gives one-sided information.
- The rotation group acting is the axiom's proper spatial rotations with the tick fixed.
  Whether the improper half or tick-reversing maps change these numbers is not addressed.
- Nothing here derives a metric, a curvature, or a field equation. It fixes an exact
  combinatorial cost that the geometry lane's constructions must pay.

## Artifacts

- Runner: `scripts/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03.py`
- Cold output: `outputs/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03_cold_2026-08-03.txt`
- Receipt: `outputs/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03_receipt_2026-08-03.json`

The runner reports `TOTAL: PASS=26 FAIL=0` in about 2 seconds. Related in-flight cycle
notes of this lane, cited for context and not as dependencies:
`PHYSICAL_ORIENTED_DIAGONAL_STENCIL_ORBIT_CYCLE722_NOTE_2026-08-02`,
`PHYSICAL_ADJACENCY_ADMISSIBLE_ASSEMBLY_TRADE_CYCLE723_NOTE_2026-08-03`,
`PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03`.
