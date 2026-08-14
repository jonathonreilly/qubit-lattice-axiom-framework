# Physical cell cutting: the identification survives the proper-rotation half

Date: 2026-08-11
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

## What is shown

The lattice input supplies proper rotations. This note shows that the cover identification carried by
the finite cell-cutting object does not lean on the orientation-reversing half of the signed coordinate
maps. Restricting the acting group of 384 signed coordinate maps to the determinant plus one half of
order 192 kills the cover stabiliser, splits the pieces into two orbits of 96, and enlarges the ambient
family of candidate labellings from 3321960 to 11035418241600 — and the two-sided conditions still cut
that enlarged family down to exactly 2 members, with the cover incidence among them. A second route that
never looks at the family, counting equivariant maps on each side and intertwining them, lands on the
same 2. Everything below is a list of computational identities about one explicitly rebuilt finite
object; the runner `scripts/physical_cell_cutting_proper_rotation_half_cycle778_2026_08_11.py` rebuilds
that object from the corners of the four-cube upward and prints 17 gates, J0 through J16.

## The object

The object is the one built in `c773`-`c777`: the unit four-cube; its 2672 five-corner pieces of unit
determinant; the 400 of those that sit at the adjacency-cost floor 6; the 15800 cuttings of the cube into
24 such pieces; the 192 pieces that occur in some cutting, each of them in 1975 cuttings; and the 192
covers, a cover being 8 pieces that meet every cutting exactly once. The acting group is the 384 signed
coordinate maps, 24 axis moves times 16 sign flips, acting on pieces and on covers at the same time. The
cover incidence is the 192-by-192 zero-one matrix recording which pieces lie in which cover. Throughout,
the holder of a point means the set of maps that leave that point alone, its stabiliser.

## The stabiliser determinant law

A signed coordinate map is an axis move together with a flip mask. Its linear part carries, in the row of
each output axis, a single entry equal to one minus twice that axis's flip bit, in the column of the axis
the move reads. The determinant of that matrix, by cofactor expansion, is the sign of the axis move times
minus one to the number of flipped axes. The runner builds all 384 matrices, checks each one against the
map it is supposed to be on all 16 corners, and takes all 384 determinants by cofactor expansion: 384 of
384 agree with the sign-times-parity formula, and the same comparison run with the flip parity dropped
disagrees on 192 of them, so the check discriminates rather than holding by construction.

A holder of order 2 survives the restriction exactly when its second map has determinant plus one. The
cover holder generator is a single-axis flip, determinant -1, and dies. The piece holder generator is not
a flip, determinant 1, and lives.

## What the restriction does to each side

The determinant plus one half is closed, has order 192 and index 2, and is normal under all 384
conjugations; the cover holder generator has determinant -1 and the piece holder generator has
determinant 1. Under the half, the 192 covers form one regular orbit of 192 with holder of order 1, and
the 192 pieces form two orbits of 96 with holder of order 2.

The two outcomes are not interchangeable, and the runner shows that by cross-applying the rules. The
piece generator's determinant rule applied to the cover side predicts 2 orbits against the measured 1,
and the cover generator's rule applied to the piece side predicts 1 against the measured 2. Both cross
predictions are wrong and each side's own rule is right.

## The enlarged family

The action on pairs of a piece with a cover is free: 192 orbit tables, every orbit of size 192, together
partitioning the all-ones 192-by-192 matrix of 36864 entries. Each table has row degree 1 and nonzero
column degree 2. Those degrees are measured, not derived, and the census convention is then read off from
them rather than assumed: a row of the incidence sums to 8, and 8 over the row degree 1 wants 8 labels
appearing once each; a column sums to 8, and 8 over the column degree 2 wants 4 labels appearing twice
each.

The tables split 96 and 96 by which piece orbit they target, and a table meets every piece of its own
orbit exactly 2 times. Any union of 4 tables from one group with 4 from the other is therefore 8-regular
on both sides, and the legal ambient family has size C(96,4)^2 = 11035418241600, the square of the
full-group family C(96,4) = 3321960. Restricting the symmetry input makes the space of candidate
labellings larger, not smaller, which is why the identification below is a stronger statement than the
full-group one and not a weaker one.

The cover incidence itself meets exactly 8 of the 192 tables, 4 from each group; each met table lies
wholly inside the incidence, and the 8 sum back to it exactly.

## The two censuses and the crossing

Row side: a candidate passes when, at every one of the 192 covers, the 8 pieces its tables select are
themselves a cover. At a fixed cover the table-to-piece map is a bijection, so the candidates are exactly
the 192 covers, and every one of them passes. The row census has 192 members, one for each cover, and
each member draws 4 tables from each of the two groups.

Column side, taken one piece orbit at a time: at an orbit representative, the 96 tables of that group cut
the 192 covers into pairs, so a member of the column census is pinned by a piece column that the piece
holder leaves alone. There are 16 such columns, they yield 16 members on each orbit, and 256 in product.
The two representatives can be chosen to share the same holder, which is what makes the per-orbit count
the same 16 on both sides.

The row census and the column census cross in exactly 2 members, and the cover incidence is in the row
census and in the crossing.

## The independent equivariant-map route

This route consults neither the family, nor the censuses, nor the tables. Because the covers are one free
orbit, an equivariant map on the cover side is pinned by the image of a single cover, giving 192 of them.
On the piece side an equivariant map is pinned by one image per orbit, and each image must be left alone
by that orbit representative's holder: 256 well-defined maps, of which 128 are bijections, 64
orbit-preserving and 64 orbit-swapping. Equivariance is gated explicitly on all 192 maps of the legal
half rather than inherited from the way the maps are built. Of the 24576 pairs of a cover map with a
piece map, exactly 2 satisfy the intertwining condition, and each of those 2 is the pair of actions of
one of the 2 central maps of the full group. Two routes with no shared input land on the same 2.

## Normalizer arithmetic

The two orbit representatives share the same holder generator. Its class in the full group has size 12
and does not split under the restriction. Its full-group centraliser has order 32 and is not contained in
the legal half, so the legal normalizer has order 16, giving per-orbit index 8. The generator fixes 16
pieces, 8 in each orbit, and 0 covers. The cover holder generator's centraliser has order 96, and it
fixes 0 pieces and 48 covers. This is the arithmetic behind the asymmetry: the piece side keeps a holder
and gains an orbit label, the cover side loses its holder and becomes free.

## Boundary

- This is a statement about a finite object and the symmetry input that object is given. It does not
  claim that the determinant plus one half IS the group the axiom supplies. What it shows is the weaker
  and cleaner thing: the identification is insensitive to whether the orientation-reversing maps are
  available. Take them away and the answer does not move.
- The identification lands at 2, not 1. The residual factor of 2 is the pair of central maps of the full
  group, that is, the pair of ways of naming covers that no map in the group can tell apart. Pushing 2
  down to 1 would need an observable sensitive to how covers are named, and none of the instruments built
  so far is sensitive to that.
- The 96 and 96 piece split is real, but the two orbits are isomorphic as legal-half sets: there are 64
  bijections between them, and any orientation-reversing map undoes the split. No geometric invariant
  computing the orbit label is known. Four local candidates were tested — sorted determinant sign, count
  of even-parity corners, corner index sum parity, and total coordinate sum parity — and all four fail:
  none of them is even constant on an orbit, because none of them is invariant under the action to begin
  with. What geometric invariant computes the orbit label is open.

## Honest auditor read

- The claim is bounded to this finite object. Nothing here asserts that the physical symmetry input is
  exactly the determinant plus one half. The load-bearing point is the insensitivity to the difference,
  and that is what the gates measure.
- Three of the gates are built as rejectors rather than confirmations. The determinant gate fails if the
  determinant is taken by any proxy that ignores the flip mask, since the parity-dropped comparison must
  disagree on a nonzero count and it disagrees on 192. The cross-swap gate fails if the two holder
  generators are handed the same determinant, which is exactly what such a proxy would do. The
  perturbation gate attacks the answer directly: each of the 8 tables of the cover incidence is swapped
  for a different table of the same group, 760 single swaps in all, and every one of the 760 is rejected
  by the row-census test.
- The candidate-invariant gate passes by correctly reporting a negative, and it is written so that a
  genuine separating invariant would make it fail rather than pass.
- The runner rebuilds the object from the four-cube corners upward, reads no stored data, and prints what
  it measures. Its object counts agree with the counts of the earlier cycles on every quantity it checks,
  and the run is reproducible byte for byte.
