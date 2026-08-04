# The adjacency cost of a cell dissection is always even, and its spectrum is exactly the eleven even integers from 108 to 128

Status: unaudited source note. Cycle 732 of the emergent-geometry lane.

## What this settles

Earlier cycles of this lane bracketed the adjacency cost of a dissection of the single
cell: it lies between 108 and 128, and both ends are attained. That left the inside of
the bracket open. Twenty-one integers sit in it; nothing said which of them a dissection
can actually realise.

This note answers that, and the answer is sharp. Exactly eleven of the twenty-one occur:
the even ones. The evenness is not a feature of the dissections that happened to be
constructed. It is forced, by an exhibited object that can be checked by hand once it is
written down — a set of 228 sample points that meets every piece of least volume in a
number of points congruent, modulo 2, to that piece's adjacency charge. Summing that
congruence over the pieces of any dissection turns it into a statement about cost, and
228 is even.

Three further things follow, and each of them is the kind of statement that this lane has
been unable to make before.

The parity argument carries no constant term. It therefore never appeals to how many
pieces a dissection has, nor to their volumes. The conclusion follows from the covering
property alone: that each sample point lies inside exactly one piece.

The certificate cannot keep the full symmetry of the cell. A complete sweep of all 98
subgroups of the cell's 48 symmetries shows that among the 12 subgroups of order at least
12, exactly one admits an invariant certificate, and it has order 12. The symmetry the
argument must give up is therefore index 4, exactly, and no more.

Modulo 2 is the sharp modulus, by two independent routes. The eleven exhibited costs
differ by a greatest common divisor of 2, so no larger modulus divides all the
differences. And modulo 3 there is no certificate at all — not as the outcome of a
failed search, but because of an exhibited local obstruction that turns out to be a
common feature of the cell rather than one freak configuration.

All of this concerns the single cell, and is stated about it. Its inputs are the lattice
adjacency of [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and nothing
else.

## Objects

The cell is the 4-cube on 16 corners: three spatial coordinates and one tick, each corner
a point of `{0,1}^4`. A piece is a set of five corners; there are 4368 of them, and 2672
have least nonzero volume. Those 2672 are the pieces a dissection may use.

The adjacency charge of a piece counts the pairs of its five corners whose distance in
the three spatial coordinates exceeds one — the pairs that are not nearest neighbours of
the lattice. The charge spectrum over the 2672 pieces is
`[(3, 64), (4, 384), (5, 1152), (6, 768), (7, 304)]`. The adjacency cost of a dissection
is the sum of the charges of its 24 pieces.

The cell keeps 24 proper rotations, and with the tick flip the symmetry group has 48
elements. It acts on the pieces with 57 orbits, of sizes 16 and 48, summing to 2672, and
the charge is constant on every orbit.

Sample points are chosen so that no point lies on any piece boundary. Superincreasing
weights with total 12810 and barycentric bound 3 produce 2736 of them, none on a
boundary, falling into 57 orbits of size 48 — one for each piece orbit, so the action on
the points is free. Each piece contains between 6 and 409 of them and each point lies in
between 90 and 224 pieces, so the incidence has no empty row and no empty column.

That there are no points on a boundary is the load-bearing property, and it is worth
naming separately. It means every sample point is interior to exactly one piece of any
dissection whatsoever. A congruence that holds piece by piece therefore sums over a
dissection without any hypothesis about how the dissection was built.

## Method: certificates and witnesses, no solver in the artifact

The runner exhibits objects and checks them. It does not search for them, and it calls no
optimiser.

A parity certificate is a set of sample points together with a constant, such that for
every piece of least volume the number of certificate points inside it, plus the
constant, is congruent to the piece's charge modulo 2. The certificate in this note is
derived inside the runner by exact Gaussian elimination over the field of two elements, so
no list of 228 point indices is transcribed by hand. Its properties are then checked
directly against all 2672 pieces.

The bounding certificates are the integer weight systems of earlier cycles, pasted in as
literals and re-verified here: the exhibited floor rows hold on all 2672 pieces and sum
over a dissection to 23328, which is 108 times 216; the exhibited ceiling rows hold on all
2672 pieces and sum to 384, which is 128 times 3.

The dissections are pinned as eleven explicit 24-tuples. Each is verified from scratch:
24 distinct pieces of least volume, pairwise disjoint by an exhibited integer separating
direction, and every one of the 2736 sample points covered. Volume and disjointness
together make the cover exact without a solver being asked anything.

The subgroup sweep takes every one-element extension of every set already found to a
fixpoint. This reaches every subgroup, because any subgroup generated by elements
`h_1, ..., h_k` is the last link of the chain of subgroups generated by the initial
segments, and every link of that chain is a one-element extension of the previous one.

Exact integer elimination over a finite field, verification of an exhibited integer
combination, and a complete enumeration over an explicit finite set are all arithmetic,
not search. Nothing in the artifact hands a question to a solver.

## Results

**The parity certificate.** The exhibited set of 228 sample points meets every one of the
2672 pieces of least volume in a number of points congruent to that piece's charge modulo
2, with no constant term. Because 228 is even, and because each sample point is interior
to exactly one piece of any dissection, the adjacency cost of every dissection of the cell
is even. The eleven exhibited dissections confirm this concretely: summing the point set
over the pieces of each of them returns 228 every time.

**The certificate is rigid.** Moving any single one of the 2736 sample points into or out
of the set breaks at least 90 of the 2672 congruences. Changing the constant term by one
breaks every one of them. Neither the complementary point set nor the set of all sample
points certifies the same congruence.

**The symmetry ladder is sharp at index 4.** The 48 symmetries of the cell have 98
subgroups. Of the 12 whose order is at least 12 — with orders
`[(48, 1), (24, 3), (16, 3), (12, 5)]` — exactly one admits an invariant certificate. All
7 subgroups of order above 12 fail. The survivor has order 12, carries the tick flip on 0
of its elements, and has rotation traces `[-1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 3]`. It
splits the 2736 sample points into 228 orbits of size 12, and the certificate is a union
of 19 of them. Exactly 12 of the 48 symmetries fix the certificate, and they are that
subgroup. So the parity argument keeps a pure rotation subgroup of order 12 and drops the
tick flip entirely; the symmetry falls by index 4 and no further.

**There is no rule modulo 3, and the obstruction is geometric.** Four pieces of least
volume sit inside the single six-corner set `[0, 1, 3, 7, 8, 10]`. Counted with
multiplicities `[1, 2, 2, 1]` they cover 266 sample points exactly three times each and
the remaining 2470 not at all — a triple cover of part of the cell and nothing else. Any
rule assigning a residue modulo 3 to each piece would have to hand that triple cover a
total divisible by 3. The four charges are `[4, 5, 6, 5]`, and
`1 x 4 + 2 x 5 + 2 x 6 + 1 x 5 = 31`, which is 1 modulo 3. The multiplicities themselves
add to 6, so the obstruction survives any constant shift as well.

**And that obstruction is common, not exceptional.** The cell has 8008 six-corner
subsets. 1104 of them carry an obstruction of exactly this kind using only the pieces of
least volume they contain themselves: 864 hold four such pieces and 240 hold six. The
wall at modulus 3 is a pervasive local feature of the cell.

Eliminating the whole point-level system agrees with the local witness: modulo 3 the
system has rank 465 and an inconsistent row, while modulo 2 it has the same rank 465 and
is consistent.

**The spectrum.** The exhibited floor rows bound every cost below by 108. The exhibited
ceiling rows bound every cost above by 128. The certificate makes every cost even. Eleven
exhibited dissections realise costs
`[108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128]`, and the greatest common divisor
of their differences is 2. The adjacency cost spectrum of the cell is therefore exactly
those eleven even integers.

## Independent cross-checks performed

Every headline of this note was re-derived by a method the runner does not use, and every
gate was tested against a perturbed object to confirm it discriminates. These checks were
run in separate probes, not inside the artifact; the counts they report in this section
are therefore theirs, and are not among the numbers the runner prints.

The incidence of points in pieces was rebuilt with exact rational barycentric
coordinates, with no common denominator and no integer scaling anywhere. On a sample of
20 pieces taken at a fixed stride through the 2672, checked against all 2736 points, it
disagreed with the runner's integer incidence nowhere.

The subgroup family was rebuilt by a different closure: every subgroup is the join of its
cyclic subgroups, so closing the distinct cyclic subgroups under pairwise join reaches all
of them. It returns the identical family of 98. There are 34 distinct cyclic subgroups,
not one per element, since different elements generate coinciding cyclic subgroups.

The eleven dissections were re-validated against a second, independent family of sample
points built from different weights. It yields 2736 points, none on a boundary, orbits of
size 48, and column sums between 90 and 224 — and all eleven covers hit every point of it
exactly once. The construction does not depend on the particular weights chosen.

The elimination over the field of two elements was redone with rows held as big integers
and lowest-set-bit pivoting, with no array library involved, and returned the same rank
465.

The perturbation tests behaved as required. One point of the certificate set moved breaks
rows. A witness with one piece swapped is no longer a dissection. Equal weights instead of
superincreasing ones put points on boundaries, where the runner's family puts none. No
subgroup of order above 12 leaves the exhibited point set invariant.

Certifiability is not generic, and this is worth stating on its own. The point-level
system modulo 2 has rank 465 among its 2672 rows, so the targets it can certify are a
very thin subspace. Ten uniformly random targets were tested and none was certifiable.
Ten random shuffles of the charge vector itself were tested and none was certifiable
either — a shuffle keeps how many pieces carry an odd charge and still fails. That the
actual charge vector is certifiable is therefore a fact about how charge sits on the
pieces of this cell, not something any assignment of the same charges would give.

One check changed the language of this note. Nudging the floor weights by a single unit
breaks a row in only 12 of the 24 possible directions, so those weights are not the only
integer system that certifies the floor. The note therefore says "the exhibited floor
rows" throughout and never speaks of a unique floor certificate.

## Boundary and honest read

The parity theorem is about this cell. It is proved by exhibiting a certificate for this
cell's 2672 pieces, and it says nothing about any other object. An earlier cycle's attempt
at a parity law across objects was refuted, and nothing here revives it.

The certificate was found by elimination, so this note does not claim it is the only one,
or the smallest. What is claimed is that the exhibited one works, is rigid under
single-point changes, and forces evenness.

The floor of 108 and the ceiling of 128 are inherited from earlier cycles of this lane and
re-verified here rather than re-derived. The new content is the parity, the sharpness of
the modulus, the index-4 symmetry ladder, and the attainment of every even value between
the bounds.

The eleven dissections are exhibited, not classified. The note does not say how many
dissections realise each cost, only that each even cost is realised.

The step from the row congruence to the cost statement uses that no sample point lies on a
piece boundary. That is measured, not assumed, and it is what makes the argument
independent of any structural hypothesis about the dissection.

## Artifacts

- Runner: `scripts/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04.py`
- Recorded output:
  `outputs/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04_cold_2026-08-04.txt`
- Receipt:
  `outputs/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04_receipt_2026-08-04.json`

The runner reports `TOTAL: PASS=39 FAIL=0`. Every number quoted above appears in that
output.
