# Physical cell cutting: the label sum is an affine function of one family trace

Date: 2026-08-14
Authority: none.
Audit: unset.
Scope: exact finite counts and identities for the declared unit four-cube cell object; no
physical, dynamical or lattice-wide identification is claimed.

This note adds no citation edges. The sibling artifacts
`PHYSICAL_CELL_CUTTING_LABEL_SUM_SIZE_BOUND_CYCLE781_NOTE_2026-08-14`,
`PHYSICAL_CELL_CUTTING_DIAGONAL_PARITY_CYCLE782_NOTE_2026-08-14` and
`PHYSICAL_CELL_CUTTING_GROUP_TILING_CENSUS_CYCLE783_NOTE_2026-08-14` are written in backticks
for context only. Nothing below depends on them: the runner shipped with this note rebuilds the
object from the corners and produces every number quoted here, and each number is printed on a
line of its output.

## The object

The cell is the unit four-cube. Its 16 corners carry 2672 five-corner subsets of unit
determinant. The adjacency cost of such a subset has floor 6, and 400 candidates attain the
floor; those 400 are the kept pieces. An exact cover search over 625 generic sample points
returns 15800 cuttings, each by 24 pieces, and exactly 192 of the kept pieces occur in any
cutting. All of this is integer and rational arithmetic — determinants by two-by-two
complements, inverses by exact elimination, covers by integer masks.

Two auxiliary structures ride along.

The first is the walk. A piece is described by a start corner together with an order of the
four axes: step from the start corner along the axes in that order, and the five corners
visited are the piece. There are 384 such walk namings from the 16 corners, exactly 2 per
piece, and the minimal naming of a piece is the one whose start corner lies below its opposite.
The second naming of the same piece begins at the opposite corner and reverses the axis order.

The second is the chamber decomposition. The twelve cut walls of the cell divide it into 192
chambers, each indexed by an axis order together with a sign triple. Each piece holds 8
chambers, each chamber lies in 8 pieces, and inside a single cutting each chamber is held
exactly once. That partition property holds with no failures across all 15800 cuttings, and it
is what makes chamber bookkeeping a faithful description of a cutting.

The label of a piece is read off its minimal naming: the sign of the axis order, times the
corner weight sign, which is minus one raised to the number of ones in the start corner. The
label sum of a cutting is the sum of the labels of its 24 pieces. Over the 15800 cuttings the
label sum census is

- label sum minus 8 on 120 cuttings,
- label sum minus 4 on 2832 cuttings,
- label sum 0 on 9896 cuttings,
- label sum 4 on 2832 cuttings,
- label sum 8 on 120 cuttings.

Those five values are the whole range: the label sum of a cutting of this cell never leaves
them.

## Positions from the incidence

Take a piece, list the 8 chambers it holds, and keep only the axis order of each chamber. The
resulting set of axis orders is the position of the piece. Nothing is chosen in this
definition; the position map is read straight from the incidence between pieces and chambers.

Three counts follow, all of them exact:

- there are 12 distinct positions;
- each position is a set of 8 axis orders, and is the position of exactly 16 pieces;
- each of the 24 axis orders lies in exactly 4 of the 12 positions.

So the 192 pieces fall into 12 blocks of 16, and the blocks are as evenly spread over the axis
orders as those numbers permit. The position is the coarse coordinate used in the rest of this
note.

## The family and its halves

Call H the family of pieces whose minimal naming uses the last axis within the first two steps
of its walk. This is a condition on the naming alone. Its size is 96, half of the 192 pieces.
Splitting H by label gives the positive half, of size 48, and the negative half, of size 48.

The family sits evenly across the positions: every one of the 12 positions meets H in exactly 8
pieces and meets the positive half in exactly 4. Both halves are therefore spread uniformly,
and no position is favoured. Which 4 of the 8 family pieces at a position carry the positive
label is not explained by any of the counts here; see the boundary section.

## The constant trace and the affine law

The trace of a cutting is the set of its pieces that belong to H. Two facts about the trace are
the substance of this cycle.

First, the trace has constant size. Every one of the 15800 cuttings meets H in exactly 12
pieces, with no exceptions. A cutting of 24 pieces splits exactly in half between the family
and its complement, always.

Second, one number about the trace fixes the label sum. Write p for the number of trace pieces
that lie in the positive half. Then the label sum of the cutting is 4 times the quantity p minus
6, with no exceptions over the 15800 cuttings. Twelve pieces of information collapse to one,
and that one enters linearly.

Three consequences drop out of the affine law and were checked separately.

- The number of label-positive pieces in a cutting is exactly 2 p. This is forced: the label sum
  equals the count of label-positive pieces minus the count of label-negative pieces, and the
  two counts add to 24, so the label sum is twice the positive count less 24; comparing with the
  affine law gives the positive count as 2 p.
- The parameter p runs from 4 to 8 and no further, since the label sum census takes exactly the
  five values listed above.
- A cutting attains label sum size 8 exactly when p is 4 or when p is 8.

The three corollaries hold together with no failures over the 15800 cuttings.

Because the law is affine and injective on the range, the census of p over the cuttings is the
label sum census relabelled: p equal 4 on 120 cuttings, p equal 5 on 2832, p equal 6 on 9896, p
equal 7 on 2832, p equal 8 on 120, total 15800. Either census determines the other, so the
label sum distribution of this cell is now a statement about a single family count.

## The mirror

Let the mirror be the cell symmetry that keeps the axis order fixed and reflects the first
coordinate. It is one of the 192 sign-minus elements of the order-384 symmetry group of the
cell, where the sign character of an element is the sign of its axis order times minus one
raised to the number of reflected axes. The mirror acts on pieces by naming transport: it moves
the start corner of the minimal naming and permutes the axis order, and the image naming names
another piece.

What the runner measures about the mirror:

- it is a bijection of the 192 pieces;
- it carries H onto H;
- it carries the positive half of size 48 onto the negative half of size 48;
- it negates the label of every piece, with no failures across the 192.

The mirror is not alone: of the 192 sign-minus elements of the group, 24 both keep H and swap
its two halves. The mirror is one of those, and is the one used below.

One consequence is immediate, and it was then checked directly rather than assumed. Since the
mirror keeps H and exchanges the halves, and since it carries cuttings to cuttings, sending a
trace to its mirror image is a bijection of the set of traces which carries the class with
parameter p onto the class with parameter 12 minus p, and preserves the number of cuttings
that complete a given trace. That premise is not re-checked here; the conclusion is, on every
trace, with no failures on the completion count and none on the parameter over all 6152
traces. In particular the layers at p equal 5 and p equal 7 must agree entry by entry, and the
census entries 2832 and 2832 must be equal — which they are.

## The trace layer

The trace of a cutting is a set of 12 family pieces. Different cuttings can share a trace, so
the natural second object is the layer of distinct traces together with the completion count of
each: the number of cuttings whose trace it is.

Over the 15800 cuttings there are 6152 distinct traces. The completion counts distribute as
1 on 2688 traces, 2 on 1536, 3 on 816, 4 on 384, 5 on 96, 7 on 168, 8 on 96, 9 on 48 and 10 on
320. The weighted total is 15800, as it must be. Note the gap: no trace has completion count 6,
although both 5 and 7 occur, so the set of attained completion counts is not an interval.

Cut the layer by the parameter p: 120 traces at p equal 4, 1488 at 5, 2936 at 6, 1488 at 7 and
120 at 8.

- The two outer layers are pure: every trace there has completion count 1, so on those layers
  the trace determines the cutting outright.
- The layers at p equal 5 and p equal 7 agree entry by entry — completion count 1 on 816
  traces, 2 on 480, 3 on 72, 5 on 48, 8 on 48, 9 on 24 — which is 1488 traces carrying 2832
  cuttings on each side. This is the mirror statement made concrete.
- The middle layer has completion count 1 on 816 traces, 2 on 576, 3 on 672, 4 on 384, 7 on 168
  and 10 on 320: 2936 traces carrying 9896 cuttings.

## Extremes are fixed by the trace alone

Of the 15800 cuttings, 240 attain label sum size 8, split 120 and 120 by sign. Every one of
them is the unique completion of its trace, and the traces that arise are exactly the two outer
layers, 120 and 120. Being extremal is therefore a property of the trace: given the 12 family
pieces of a cutting whose parameter is 4 or 8, both the label sum and the remaining 12 pieces
are determined, and no further information about the cutting is needed.

## The refutation

The obvious next guess is that the completion count depends only on the parameter, so that the
cutting census would be a product factorization over the trace layer: the number of traces in a
class, times a completion count common to that class. On the two outer layers this is exactly
what happens, with common completion count 1.

It fails everywhere else. On each of the three interior classes the completion count takes 6
distinct values, so no class-constant factor exists there. Two explicit witnesses in the middle
layer, printed by the runner, make the failure concrete:

- a trace with completion count 1, whose family members are 0 1 11 26 27 30 33 35 42 43 45 48;
- a trace with completion count 10, whose family members are 2 3 6 7 10 11 12 13 14 15 16 17.

The two traces share the parameter and differ in completion count by an order of magnitude.
Whatever governs the completion count is finer than the parameter, and this cycle does not
identify it. The factorization question is settled negatively and does not need re-attacking in
this form.

## The rejector

The two laws are properties of this family, not of any half-sized set of pieces. Replace the
least-indexed member of H by the least-indexed piece outside it, keeping the size at 96, and
re-run the two tests: the constant trace fails on 3390 of the 15800 cuttings, and the affine law
fails on 1975. A single-piece perturbation therefore breaks both statements on thousands of
cuttings, so neither law is an artefact of counting or of the size of H.

## Reproduction

Run `scripts/physical_cell_cutting_trace_law_completion_cycle784_2026_08_14.py`. It is
self-contained: standard library only, no file input or output, no randomness, no external
data. It rebuilds the object from the corners, prints one line per gate, and ends with the
totals line reading PASS=14 and FAIL=0 followed by a resource line. It runs in under 60 s of
the declared 900 s budget and under 250 MB of the declared 2500 MB budget.

## Boundary

The following are measured, not derived, at this scope: the constant trace size 12; the affine
law itself; the family size 96 and the halves at 48 and 48; the position spread 8 and 4; the
completion count histogram and its per-parameter refinements; the preservation of H by the
mirror and the exchange of the halves; and the count 24 of sign-minus group elements that do
both.

The following are derived from those measurements: the label-positive count 2 p; the range of
the parameter; the equivalence between label sum size 8 and the outer parameters; the transport
of the trace layer by the mirror, hence the entry-by-entry equality of the layers at p equal 5
and p equal 7; and the fact that the p census and the label sum census carry each other.

The gates are computational identities on a declared finite object. They are exact, they are
reproducible, and they say nothing about arbitrary cutting systems of other cells, about
physical dynamics, or about a lattice-wide construction.

Open, and named here without being attacked: which 4 of the 8 family pieces at a given position
carry the positive label. The spread counts say the selection exists and is uniform across
positions, but no rule producing it from the incidence or the naming is known, and this cycle
offers none.

Out of scope by intent: the per-profile cutting counts of the earlier cycles, the tile and
translate machinery those cycles used, and any attempt to promote the family H to a canonical
construction. The refutation above is a negative result about the trace layer and should be
read as bounding the next question, not as a verdict on the object.
