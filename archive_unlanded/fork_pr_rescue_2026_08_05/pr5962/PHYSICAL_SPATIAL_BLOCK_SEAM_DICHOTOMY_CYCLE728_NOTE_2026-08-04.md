# Two cells side by side: what a seam costs when the long axis is spatial

Status: unaudited source note. Cycle 728 of the emergent-geometry lane.

## What this settles

Take two lattice cells side by side and carry them through one tick. Cut the resulting
box into minimal pieces and charge each piece for the pairs of its corners that sit more
than one step apart in space. Two facts about that cost are settled here, both without a
solver anywhere in the artifact.

First, **a dissection that respects the seam between the two cells costs between 216 and
256**, and both ends are attained. The lower end follows from a certificate that holds on
every one of the 2672 minimal pieces of a single cell at denominator 2, the upper end from
a certificate at denominator 3, and both certificates are checked here piece by piece
rather than taken on trust. Respecting the seam means no piece straddles it; the note
shows that this condition is equivalent to the piece lying inside one closed cell, so a
seam-respecting dissection *is* a pair of one-cell dissections and its cost is the sum of
two one-cell costs.

Second, **the dearest dissection cannot respect the seam.** An explicit 48-piece
dissection is exhibited that costs 318, verified here to be a genuine dissection — every
piece of volume one, every one of its 1128 pairs separated by an integer normal produced
on the spot — and 318 sits above 256. Thirty-one of its 48 pieces cross the seam. So the
cost-maximising dissection must break the seam, while the cost-minimising one need not:
the least cost 216 is attained by a dissection that leaves the seam alone. And the
maximum is pinned from above: a ceiling certificate written over the block's own 1080
piece orbits, carried at denominator 12 and checked against every one of the 17280 minimal
pieces, gives 324. The dearest dissection of this box therefore costs between 318 and 324,
where the bound available from the charge alone is 432.

A third result is structural rather than numerical. **No dissection of this box carries
the box's own symmetry.** The box has a symmetry group of order 16; a symmetric dissection
would be a union of whole piece orbits, all orbits have size 16, and 48 pieces over orbits
of 16 leaves exactly 3 orbits. Only 23 of the 1080 orbits can appear in any exact cover at
all, and a direct sweep over triples of those 23 finds none that covers every sample point
exactly once. Symmetry is therefore something a dissection of this box always breaks.

## Objects

The box is `{0,1,2} x {0,1} x {0,1}` in space and `{0,1}` in tick: 24 corners, spatial
volume 2. Its minimal pieces are the 5-corner subsets of unit normalised volume; there are
17280 of them, and a dissection into minimal pieces uses 48. A single cell, `{0,1}` in each
of the four coordinates, has 16 corners, 2672 minimal pieces, and 24 pieces per dissection.
Every number quoted for the single cell is measured in the same artifact, so nothing about
it enters as a supplied constant.

Three charges are read on the same pieces:

- the **spatial adjacency charge**, counting corner pairs whose separation in the three
  spatial coordinates exceeds one step. Its range on minimal pieces is 3 to 9.
- the **transposed charge**, counting separation in the tick together with the two short
  spatial coordinates instead. Its range is 3 to 7.
- the **long-axis span charge**, counting pairs separated by more than one step along the
  long spatial direction. Its range is 0 to 4.

The lattice, its adjacency, and the proper cubic rotations acting on it are the ones fixed
by [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md); no further structure is
used.

## Method: certificates and witnesses, no solver in the artifact

A **floor certificate** is an integer weight `u` per piece orbit together with an integer
constant `Z` and a denominator `D`, such that on every minimal piece the orbit weights it
meets, summed and offset by `Z`, stay at or below `D` times its charge. Summing that
inequality over the pieces of any dissection gives a lower bound on the cost, and the bound
depends only on `u`, `Z`, `D` — not on the dissection. A **ceiling certificate** reverses
the inequality and bounds the cost above. Both are verified here by direct integer
arithmetic against every piece.

The certificate needs the sample points it is written over to be generic. Rather than hope
for that, the weights are built to force it: the largest barycentric integer any corner
sees on any piece is measured first, and the corner weights are then chosen superincreasing
and large enough that no barycentric coordinate of a sample point can vanish. The artifact
then checks the consequence directly — zero boundary incidences over all 17280 pieces — so
every sample point lies in the interior of exactly one piece of any dissection, and the
bound holds with no symmetry assumption at all. Symmetry is used to shrink the certificate,
never to justify it.

A **witness** is an exhibited dissection. Each is checked three ways: every piece has
volume one, the volumes sum to the box, and every pair of pieces carries an integer normal,
produced on the spot, that separates them. Volume plus pairwise separation is already an
exact cover, so no solver is needed to certify a witness either.

The least-cost witnesses are the monotone stencils: for each of the 24 orderings of the
four coordinates, the piece spanned by the corresponding monotone corner path. The dearest
witnesses come from lifting the corners by a height function and taking the lower hull,
accepting only lifts whose lower faces are all minimal pieces and number 48.

## Results

**The seam is a real barrier in the charge, not just in the geometry.** A piece with span
zero sits inside one closed cell; there are 5344 such pieces, and they are exactly two
translated copies of the 2672 one-cell pieces with the charge unchanged by the translation.
Their charge spectrum is the one-cell spectrum doubled. The remaining 11936 pieces all
reach from one face of the box to the other, and the cheapest of them costs 5 where a
confined piece can cost 3. Crossing the seam costs at least two extra, piece by piece.

**One cell brackets exactly at [108, 128].** The floor certificate holds on all 2672 pieces
with least slack zero and equality on 1984 of them, and its value is exactly 108. The
ceiling certificate holds with least slack zero and equality on 944, value exactly 128. Two
witnesses attain the two ends. Stacking each of them over the two cells gives block
dissections at exactly 216 and exactly 256, both with no seam crossings at all — so the
seam-respecting bracket [216, 256] is attained at both ends.

**The measured span of the cost is [216, 318].** The trivial counting bounds — 48 pieces
times the least and greatest charge a single piece can carry — are 144 and 432; both
measured ends sit strictly inside. The 318 witness exceeds the seam-respecting ceiling 256,
which is what makes the dichotomy sharp.

**The block maximum is bracketed at [318, 324].** A ceiling certificate over the block's
own 1080 piece orbits, carried at denominator 12, holds on every one of the 17280 minimal
pieces with least slack zero and equality on 1200 of them, and its value 3888 over 12 gives
324. The 318 witness sits six below that. The bound available from the charge alone — 48
pieces times the greatest charge a single piece can carry — is 432, so the certificate
removes most of the trivial slack without closing the window.

**The two charges part company on the dear dissection and agree on the cheap one.** The
same 48 pieces of the 318 dissection read 238 under the transposed charge. On the stacked
stencil the two charges agree exactly, at 216. That agreement is structural,
not a coincidence: the stencil is built from all 24 orderings of the four coordinates, so
exchanging the long spatial axis with the tick permutes its 24 pieces among themselves, and
the two charges are then forced equal — 108 both ways on one cell. The dear one-cell
dissection has no such symmetry: the same exchange moves it, and its two charges read 128
against 116. Neither charge dominates the other across the piece set — spatial is the
larger on 12208 pieces and the smaller on 1952 — so the two are genuinely different
functions that happen to coincide on the symmetric minimiser.

**A denominator law falls out of the certificate form.** A block certificate value is
`16 T + 48 Z`, with `T` the sum of the orbit weights and `Z` the constant, so it is always
a multiple of 16; the bound it gives is that value divided by `D`. A bound of `c` therefore
needs 16 to divide `c D`: a bound of 216 forces `D` even, and a bound of 324 forces `D`
divisible by four. The certificate carried here has `D = 12`, which serves both.

## Independent cross-checks performed

Every headline number was re-derived by a route the artifact does not use, and every
load-bearing gate was tested by breaking the object it is about.

The count of orbits eligible for a symmetric dissection was recomputed point by point:
for each of the 1080 orbits, all 16 of its pieces were tested directly against all 17280
sample points, with no representative and no transitivity argument. That route returns 23,
and returns the identical set of orbits. An earlier scratch count was wrong and is
discarded. The orbit-sum identity — that the 16 pieces of an orbit together meet each point
16 times as often as the representative does — was added as its own gate after this check.

The stencil's behaviour under exchanging the long spatial axis with the tick was measured
directly rather than argued. It is invariant; the dear cell triangulation under the same
exchange is not, and reflecting the tick rather than permuting coordinates does not preserve
the stencil either. So the invariance is a property of that particular dissection, and the
gate that reports it would fail if it were not.

Each gate was then perturbed. Corrupting a single membership entry, or mis-assigning a
single orbit representative, breaks the orbit-sum identity. Clamping one ineligible orbit
moves the eligible count from 23 to 24; spoiling one eligible orbit moves it to 22. Raising
a single tight entry of the floor certificate, or its constant, breaks the certificate;
lowering a single tight entry of the ceiling certificate, or its constant, breaks that one.
No gate here passes by construction.

The block ceiling certificate was broken the same way: lowering a single tight entry, or
lowering the constant, makes it fail on some piece. Rescaling the weights, the constant and
the denominator together by 2, 3 and 5 leaves the bound at 324 exactly, so no rescaling of
this certificate sharpens it. Its slack was also recomputed from the orbit representatives
alone and agrees piece for piece with the full check over all 17280 pieces.

## Boundary and honest read

**There is no block-level floor certificate.** A certificate ladder was walked against the
block's own 1080 orbits at several denominators and none of them reached 216. So the
statement carried here is that 216 is the least cost found, and that no seam-respecting
dissection costs below it — not that 216 is optimal over all dissections of the block.
Whether a seam-crossing dissection can undercut 216 is open, and a certificate of this
shape is not ruled out for it; what is reported is that the integral versions tried did
not reach it.

**The block ceiling window is not closed.** The certificate gives 324 and the best witness
found reaches 318; those six units are open. The gap is not a search artifact that a finer
denominator removes: a certificate value is `16 T + 48 Z`, hence always a multiple of 16,
and rescaling the weights, the constant and the denominator together leaves the bound
exactly where it was. Sharpening the ceiling needs a different certificate shape, not a
larger denominator.

**The 318 witness is a regular triangulation.** It was found by lifting, so it is a lower
hull, and the sweep that produced it did not improve on 318 across the rounds run. The
number 318 is therefore a certified attained cost, not a certified maximum.

**Two conventions are choices, and both are named.** The charge counts corner pairs
separated by more than one lattice step; the pieces are minimal in normalised volume. Both
are read directly off the lattice adjacency, but neither is forced by it.

## Artifacts

- runner `scripts/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.py`
- cold output `outputs/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04_cold_2026-08-04.txt`
- receipt `outputs/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04_receipt_2026-08-04.json`

The runner prints `TOTAL: PASS=65 FAIL=0`. The cold output is its stdout verbatim; the
receipt transcribes the numbers from that stdout. Every number quoted above appears in the
runner's own output, with the certificate weights themselves the one carve-out — they are
supplied to the runner as integer data and verified by it, not derived by it.
