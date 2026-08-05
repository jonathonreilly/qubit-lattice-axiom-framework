# What a two-cell block costs, pinned at both ends, and why lifting cannot reach the top

Status: unaudited source note. Cycle 729 of the emergent-geometry lane.

## What this settles

Take two lattice cells side by side, carry them through one tick, cut the resulting box
into minimal pieces, and charge each piece for the pairs of its corners that sit more than
one step apart in space. The previous cycle bracketed that cost between 216 and 324 and
exhibited a dissection costing 318. This note pins the interval exactly, and explains why
the earlier search stopped where it did.

**The cost of a dissection of this box lies between 216 and 320, and both ends are
attained.** The floor is carried by an integer certificate at denominator 512, valid with
least slack zero on all 1080 piece orbits and again piece by piece on all 17280 minimal
pieces, and attained by the stacked monotone stencil. The ceiling is carried by an integer
certificate at denominator 49, checked the same two ways, and attained by an exhibited
48-piece dissection costing 320. Charging every piece the least or the most its charge
allows gives only 144 to 432, so both ends sit well inside what counting alone delivers.
Neither certificate is searched for inside the artifact: both arrive as integer data and
are verified there by direct integer arithmetic.

**The dearest dissection is not the lower hull of any lift.** Sixteen of its facets are
carried by a single piece and lie away from the boundary of the box, so the dissection is
not face-to-face; a lower hull always is. The stacked stencil and the earlier 318 witness
are lower hulls, each with an exhibited integer height clearing all 912 lower-face
inequalities. So the three objects separate cleanly: lifting reaches 216 and 318, and the
dissection costing 320 is not reachable that way at all. That is the answer to a question
the previous cycle left open — its hill climb generated dissections by lifting, and the
maximiser lies outside the reach of that construction by a structural obstruction, not by
bad luck in the search.

**Two statements from the previous cycle are corrected here, both upward.** Its best
witness of cost 318 is superseded by the verified dissection of cost 320. And its boundary
read — that sharpening the block ceiling would need a different certificate shape rather
than a larger denominator — does not hold: the shape here is the same one, and what
changes is the denominator. The earlier argument was that a certificate value is always a
multiple of 16, so the bounds a certificate can reach are coarse; that granularity bites
only while the denominator stays at or below 16. At denominator 49 the value 15728 sits 48
above 320 times the denominator, which is less than the denominator itself, so the bound
lands exactly on 320 rather than on the 324 the previous cycle reported.

## Objects

The box is `{0,1,2} x {0,1} x {0,1}` in space and `{0,1}` in tick: 24 corners, spatial
volume 2. Of its 42504 five-corner subsets, 17280 have unit normalised volume; these are
the minimal pieces, and a dissection into them uses 48. The spatial adjacency charge counts
corner pairs whose separation in the three spatial coordinates exceeds one step; on minimal
pieces it ranges from 3 to 9, with spectrum 128, 768, 2816, 4928, 5760, 2608 and 272 pieces
at each value. The transposed charge reads the same count with the tick substituted for the
long spatial axis.

The box has a symmetry group of order 16 — the 8 proper rotations that preserve it,
doubled by the tick flip. The 17280 minimal pieces fall into 1080 orbits, every one of size
16.

The lattice, its adjacency, and the proper cubic rotations acting on it are the ones fixed
by [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md); no further structure is
used.

## Method: certificates and witnesses, no solver in the artifact

A **floor certificate** is an integer weight per piece orbit together with an integer
constant and a denominator, such that on every minimal piece the orbit weights that piece
meets, summed and offset by the constant, stay at or below the denominator times its
charge. Summing that inequality over the 48 pieces of any dissection turns it into a lower
bound on the cost that depends only on the certificate, never on the dissection. A
**ceiling certificate** reverses the inequality and bounds the cost above. Both are
verified here by integer arithmetic against every orbit row and then against every one of
the 17280 pieces.

The step that makes the sum work is that each sample point lies inside exactly one piece of
any dissection, so the weights add up the same way no matter how the box is cut. Rather
than hope the sample points are generic, the artifact forces it: the largest barycentric
integer any corner sees on any piece is measured first — it is 6 — and the corner weights
are then chosen superincreasing and large enough that no barycentric coordinate of a sample
point can vanish, with the resulting weights spread by under 1.15. The consequence is then
checked directly, as zero boundary incidences over all 17280 pieces. The bound therefore
holds with no symmetry assumption at all; symmetry only shrinks the program from 17280 rows
to 1080, and the artifact confirms that shrinking is lossless by reproducing all 17280 piece
rows from the 1080 orbit rows, and by re-running both certificates at full size.

A **witness** is an exhibited dissection, checked three ways: every piece has volume one,
the volumes sum to the box, and every one of its 1128 pairs of pieces carries an integer
normal, produced on the spot, that separates them. Volume together with pairwise
separation is already an exact cover, so certifying a witness needs no solver either.

**Regularity** is settled in both directions without a solver. A lift assigns a height to
each of the 24 corners; the lower faces of the lifted polytope form a face-to-face complex,
so any dissection arising as a lower hull is face-to-face. Contrapositively, one interior
facet carried by a single piece already rules out every lift: a three-dimensional face of a
four-simplex is a facet, so if some second piece covered the other side of it the two
pieces would meet in that whole facet and the count would be two, not one. In the other
direction an exhibited integer height, checked against all 912 lower-face inequalities in
integer arithmetic, proves a dissection is a lower hull outright. Both directions are pure
verification of supplied data.

## Results

**The floor is 216.** The certificate has value 110144 at denominator 512; 216 is what that
rounds up to, and the certificate is valid with least slack zero over all 1080 orbit rows,
tight on 30 of them, with the identical least slack recovered from all 17280 pieces
directly. The stacked monotone stencil — for each of the 24 orderings of the four
coordinates the piece spanned by the corresponding monotone corner path, stacked over both
cells — is verified to be a dissection and to cost exactly 216. So the floor is certified
and attained.

**The ceiling is 320.** The certificate has value 15728 at denominator 49; 320 is what that
rounds down to, again with least slack zero over all 1080 orbit rows, tight on 53, and
matched piece by piece over all 17280. An exhibited 48-piece dissection is verified to be a
dissection and to cost exactly 320. So the ceiling is certified and attained, and the cost
of a dissection of this box is pinned to the interval from 216 to 320 with both ends
reached.

**The maximiser is not regular, and that is why lifting stopped at 318.** Sixteen facets of
the 320 dissection are carried by one piece and lie away from the box boundary, so it is
not face-to-face and no lift produces it. Meanwhile the stacked stencil carries an integer
height clearing all 912 inequalities with worst value -16, and the earlier 318 witness
carries one with worst value -32. A lift-based search therefore has 216 and 318 inside its
reach and 320 outside it. The separation is not an artifact of which height was tried: the
stencil's own height, applied to the dearest dissection's rows, fails them by 336.

**The picture is stable under the checks that could have broken it.** Rescaling a
certificate's weights, constant and denominator together by 2, 3 and 5 leaves its bound
exactly where it was — 1024, 1536 and 2560 on the floor side, 98, 147 and 245 on the
ceiling side — so neither end is an artifact of the denominator chosen. Swapping the long
spatial axis for the tick axis leaves the stencil at 216. Recomputing the tightest
certificate row in unbounded integers returns the same zero, so nothing here rides on
machine word size.

## Independent cross-checks performed

Every headline number was re-derived by a route the artifact does not use, and every
load-bearing gate was tested by damaging the object it is about.

The three costs — 216 for the stencil, 320 for the dearest dissection, 318 for the earlier
witness, and 216 again for the stencil under the transposed charge — were recomputed by a
plain double loop over corner pairs with no array machinery at all, and agree. The
certificate slacks were recomputed in unbounded integers and the two bounds in exact
rational arithmetic, and agree. A fractional relaxation of the same counting program,
solved independently of every certificate, returns exactly the same two endpoints, so
neither certificate is leaving anything on the table that a certificate of this shape
could have collected.

The membership matrix is the one place a floating-point inverse could have rounded
silently, so it was rebuilt from exact integer cofactor adjugates for a large random sample
of pieces together with the tightest certificate row, and agrees entrywise. The exact
cover claimed for each witness was re-tested on fresh random rational points in exact
rational arithmetic: every point lying off the shared faces is inside exactly one piece,
and no point escapes every piece. A first version of that test demanded that no sampled
point land on a face at all, which random rational sampling cannot deliver, and it reported
failures for the plain stencil — a dissection beyond doubt. Restating the predicate
correctly cleared all three witnesses.

Non-regularity was then proved a second time, by machinery disjoint from the facet count: an
exact integer vector of nonnegative multipliers on the 912 lower-face inequalities, summing
them to zero, exists for the dearest dissection and is verified with no solver. No such
vector exists for the stencil or for the earlier witness, as must be the case since both are
lower hulls. Regularity was also confirmed a third way, by taking the convex hull of the 24
lifted corners directly and reading its lower facets: for the stencil and for the earlier
witness they are exactly the 48 pieces, and the stencil's lift does not reproduce the
dearest dissection.

Each gate was then perturbed. Raising the floor certificate's constant by one breaks it;
lowering the ceiling certificate's constant by one breaks that one. Deleting any single
positive weight from the floor certificate drops its bound below 216, so no weight is
decoration. Raising a membership entry on a row with no slack, in a column whose weight is
live, breaks the floor certificate every time it is tried. Lowering the charge of the
tightest row breaks it. Swapping one piece of the dearest dissection leaves pairs
unseparated, so the separation test is not automatic. Two perturbations deliberately did
*not* break their gate, and both were chased down rather than waved through: moving a single
corner of the stencil height by one changes nothing, because being a lower hull is an open
condition and the heights that induce a given hull form a cone with interior — the least
single-corner move that does break it is 16 in either direction at every one of the 24
corners, exactly the margin the artifact reports, so the cone is bounded and the witness is
not vacuous. And corrupting a membership entry in a column whose weight is zero changes no
product, which is why the retargeted version above is the honest form of that control.

## Boundary and honest read

**The interval is pinned for this box and this charge, not in general.** What is settled is
that dissections of the two-cell one-tick box have adjacency cost between 216 and 320 with
both ends attained. Nothing here says how that interval scales, and the previous cycle's
seam result — that a dissection which respects the seam between the two cells costs between
216 and 256 — remains the separate statement it was. The two fit together: the floor 216 is
reached without breaking the seam, while 320 is above 256, so the maximiser must break it.

**Both certificates are supplied data.** The weights, constants and denominators are
integer inputs that the artifact verifies; it does not search for them. The denominators
512 and 49 are the ones the certificates are carried at, and no claim is made that either
is the smallest denominator at which a certificate of this shape exists.

**Non-regularity is proved for this maximiser, not for maximisers as a class.** The 320
dissection is not a lower hull and no lift produces it. Whether every cost-maximising
dissection of every such box shares that property is open, and the argument given here does
not settle it.

**Two conventions are choices, and both are named.** The charge counts corner pairs
separated by more than one lattice step; the pieces are minimal in normalised volume. Both
are read off the lattice adjacency, but neither is forced by it.

## Artifacts

- runner `scripts/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04.py`
- cold output
  `outputs/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04_cold_2026-08-04.txt`
- receipt
  `outputs/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04_receipt_2026-08-04.json`

The runner prints `TOTAL: PASS=43 FAIL=0`. The cold output is its stdout verbatim; the
receipt transcribes the numbers from that stdout. Every number quoted above appears in the
runner's own output, with three carve-outs named in place: the certificate weights,
constants and denominators are supplied to the runner as integer data and verified by it
rather than derived by it; the cross-check counts come from separate probes that are not
part of the landed artifact; and the values 324 and 256 are quoted from the previous
cycle's own record, not measured here.
