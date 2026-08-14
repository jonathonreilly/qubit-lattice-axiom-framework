# Physical cell cutting: the covers are the chambers of a hyperplane arrangement, and the label sum of a cutting is divisible by four

Date: 2026-08-14
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

## What this cycle asks

The unit four-cube cell object is rebuilt from scratch here as in the sibling cycles
`cycle 773`, `cycle 776`, `cycle 777`, `cycle 778` and `cycle 779`: of the 2672
five-corner sets of unit determinant, the ones at the adjacency cost floor 6 number 400;
exact cover of the cell by floor pieces has 15800 solutions, each of 24 pieces; the pieces
that actually occur number 192, each in 1975 cuttings, for 379200 slots; and the naming of
a piece by a start corner together with an order of the four axes gives 384 namings, 2 per
piece.

`cycle 779` answered the question *what are the 192 pieces*: they are the staircase paths,
and each carries a handedness label L equal to the sign of the axis order times minus one
to the weight of the start corner, single valued on the path. It left two things standing
as search outputs or measurements:

* the 192 **covers of 8** — eight pieces no two of which share a cutting — came out of a
  clique enumeration, with no description of what a cover *is*;
* the label sum S(T), summed over the 24 pieces of a cutting T, was measured to be a
  multiple of 4 on all 15800 cuttings, with no argument forcing it.

This cycle answers both. The covers are the chambers of a hyperplane arrangement, read at
a point; and the divisibility by 4 follows from a local statement about a piece and its
chambers, summed over a cutting.

## The chamber identification

**T1.** Put u = x - 1/2 in each of the four coordinates, so that u = 0 is the centre of the
cell. Cut the open cell by the 12 hyperplanes

> x_i = x_j and x_i + x_j = 1, one of each for every one of the 6 coordinate pairs,

that is, by u_i - u_j = 0 and u_i + u_j = 0. Name a chamber of that cut by the pair
(b, s), where b is the order of the four magnitudes |u_1|, ..., |u_4| taken decreasingly —
a permutation of the four axes — and s = (s1, s2, s3) collects the signs of u at the first
three slots of b. The sign at the fourth slot is **not** chamber data: u at that slot
vanishing is not one of the 12 walls, so both of its signs lie in one and the same chamber.
There are 24 orders times 8 sign triples = 192 chambers. The naming is faithful: the 192
exact rational sample points below realise 192 distinct sign patterns on the 12 walls, and
none of them sits on a wall (gate K3).

The following facts are all verified on the rebuilt object.

**(a) Each used piece holds exactly 8 chambers**, dealt by a sign recursion. For the piece
named (v0, sigma) and each rho in {+1, -1} of length 3, run down the axis list sigma
popping from the front when rho_k = +1 and from the back otherwise; the popped axes in
order are b, and s_k = rho_k times eta at b_k, where eta_j = 1 - 2 v0_j at the start
corner. The 8 values of rho give 8 distinct chambers, and the piece's other naming deals
exactly the same 8 (gate K3).

**(b) Each chamber lies in exactly 8 used pieces** (gate K3). The two counts agree on the
total: 192 times 8 = 1536 incidence slots, seen from either side.

**(c) The identification is geometric, not combinatorial bookkeeping.** For each chamber
take the exact rational point whose offsets from the centre are 8/20, 6/20, 4/20 and 2/20
down the b-order, with signs (s1, s2, s3, +1). Testing that point against the five integer
affine forms of each of the 192 pieces, with exact rational arithmetic, it lies strictly
inside exactly the 8 pieces that (a) assigns to it, with 0 mismatches over all 192 chambers
(gate K5). So the incidence dealt by the recursion is the true containment incidence.

**(d) The 192 chamber piece-sets are exactly the 192 covers.** They are pairwise distinct,
and the sorted list of them equals the sorted list of the covers returned by the clique
enumeration of `cycle 779` (gate K7).

**(e) Each chamber meets each cutting in exactly one piece.** Checked directly on all 192
times 15800 = 3033600 chamber and cutting pairs, with 0 exceptions (gate K6).

Fact (e) is the conceptual content, and it has a short reason once the chambers are in
view: a
cutting partitions the cell, so any point of the cell lies in exactly one of its 24 pieces,
and a whole chamber travels together because no piece boundary crosses a chamber. The
counting is tight — the 24 pieces of a cutting carry 24 times 8 = 192 chamber slots, which
is exactly the number of chambers, so the assignment is a bijection. This is what a cover
is: **a cover is the point-evaluation class of a chamber**, the set of pieces that can hold
that chamber. The covers stop being the output of a search over the 192 pieces; they are
read off the arrangement, which does not know about the cuttings at all.

## The local label formula

**T2.** For every incident piece and chamber pair,

> L(P) = sign(b) times s1 times s3 times eta at b2 times eta at b4,

where sign(b) is the sign of the order b as a permutation, s1 and s3 are the first and
third chamber signs, and eta is taken at the start corner of P. Verified on all 192 times
8 = 1536 incident pairs with 0 failures (gate K4).

Two readings. First, the handedness of a piece is a *local* quantity: one chamber it holds,
plus the corner parity of the piece at two slots of that chamber's order, already determine
it. Second, the formula is what makes the next section work, because it expresses L in
chamber data on which one can build functions of the chamber alone.

## The mod-four law, derived

Write, for a piece P with naming (v0, sigma),

> q1(P) = 1 when sign(sigma) = -1 and 0 otherwise, q2(P) = the weight of v0 modulo 2.

Both are well defined on the path, not merely on the naming: the two namings of a piece
agree on L and on the pair (q1, q2) for all 192 pieces, and q1 = 1 on 96 of them, q2 = 1 on
96 (gate K2).

**(i) Product form.** L(P) = (1 - 2 q1(P)) times (1 - 2 q2(P)) on all 192 pieces (gate K2).

**(ii) The per-cutting identity.** With A1 = sum of q1, A2 = sum of q2 and A12 = sum of the
product q1 q2, all over the 24 pieces of a cutting T,

> S(T) = 24 - 2 A1 - 2 A2 + 4 A12,

an identity holding on all 15800 cuttings with 0 failures (gate K11). It is (i) expanded:
each piece contributes 1 - 2 q1 - 2 q2 + 4 q1 q2.

**(iii) Certificates on chambers.** Define two functions of a chamber c = (b, s) alone:

> g1(c) = 1 when sign(b) times s1 s2 s3 = +1, and 0 otherwise;
> g4(c) = 1 when sign(b) = -1 and the last slot b4 is a fixed axis j, and 0 otherwise.

Then, for every one of the 192 pieces P:

* **Claim one.** The sum of g1 over the 8 chambers of P is congruent to q2(P) modulo 2 —
  0 failures (gate K8).
* **Claim two.** The sum of g4 over the 8 chambers of P is congruent to q1(P) modulo 2, and
  this holds for each of the 4 choices of the fixed axis j: 768 checks, 0 failures (gate
  K9).

So each of the two piece statistics that build the label is recovered, modulo 2, from a
function of the chambers the piece holds.

**(iv) The totals are even.** Summed over all 192 chambers, g1 has weight 96, and g4 has
weight 24 for each of the four axes (gate K10). Both are even, and that is the whole input
the next step needs.

**(v) Telescoping.** Fix a cutting T and sum claim one over its 24 pieces. The left side is
a double sum over pairs (P, c) with P in T and c a chamber of P. By T1(e) each chamber
belongs to exactly one piece of T, and every chamber belongs to some piece of T, so the
pairs are in bijection with the 192 chambers and the double sum collapses to the total
weight of g1 over all chambers, which is 96 by (iv). The right side is A2(T) modulo 2.
Hence

> A2(T) is congruent to 96, that is to 0, modulo 2, for every cutting.

The same argument with g4 at a fixed axis gives A1(T) congruent to 24, that is to 0, modulo
2. Both are confirmed directly: 0 cuttings of the 15800 have odd A1, and 0 have odd A2
(gate K11). Now feed the two parities into (ii). Modulo 4 the term 4 A12 drops, and 2 A1
and 2 A2 both drop because A1 and A2 are even, leaving

> S(T) congruent to 24, that is to 0, modulo 4, for every cutting.

Directly: S is divisible by 4 on all 15800 cuttings, 0 exceptions, with census -8 on 120
cuttings, -4 on 2832, 0 on 9896, 4 on 2832 and 8 on 120 (gate K12). The divisibility by 4,
a census fact in `cycle 779`, is therefore derived here from T1(e) plus the two piecewise
claims and the two even totals.

The chain has a control. Gate K13 perturbs it in two ways: flipping g1 at a single chamber
breaks claim one at exactly 8 pieces, precisely the pieces that hold that chamber; and
negating the label of a single piece breaks the identity (ii) at exactly 1975 cuttings,
precisely the cuttings through that piece. Both perturbations are detected, and each count
is the one the structure predicts, so the gates can fail and do fail when the object is
disturbed.

## What this does not establish

**The bound on the size of S is measured, not derived.** The census says S lies in the five
values -8, -4, 0, 4, 8, so |S| is at most 8 over the 15800 cuttings; nothing above forces
that bound. Divisibility by 4 restricts S to a lattice, not to an interval, and the
derivation in the mod-four law section is silent about size.

A live path towards the bound, opened by the same chamber picture and reported here as a
measurement only: group the 24 pieces of a cutting by their main diagonal, taking the
smaller of the start corner and its opposite, which gives 8 diagonals, and let D_w be the
label sum of the pieces on diagonal w. Measured over the 15800 cuttings, |D_w| never
exceeds 4, and the maximum is attained; the sum over the 8 diagonals of |D_w| takes the
value 0 on 9320 cuttings, 4 on 6096 and 8 on 384, so its largest value is 8 (gate K14).
Since |S| is at most the sum of |D_w| by the triangle inequality, and that sum has largest
value 8, a per-diagonal bound proved rather than measured would deliver the bound on |S|
pointwise. That derivation is not attempted here.

**A2 modulo 4 is observed, not derived.** A2 is divisible by 4 on all 15800 cuttings (gate
K14), which is stronger than the parity the telescoping argument gives. A certificate in
the style of (iii) taking values modulo 4 rather than modulo 2 would sharpen the whole law;
none is offered here, and finding one is the natural next path.

Two further limits, stated plainly. The derivation of the mod-four law uses T1(e), which is
verified on the rebuilt object over all 3033600 chamber and cutting pairs rather than
proved from the definition of a cutting; the geometric reading in the chamber identification section says why it
must hold, but the note claims only what the gates check. And the claim type is
bounded_theorem, not a stronger one, because the object is the finite cell as rebuilt: the
statements are theorems about it, and nothing here extends them to any other cell.

## Relation to sibling cycles

The object, the label and the clique enumeration of the covers are taken from `cycle 779`,
which this note extends rather than corrects: nothing in `cycle 779` is withdrawn, and its
192 covers are reproduced exactly by the chamber construction. The cover incidence used in
`cycle 778` and the sharing and blindness results of `cycle 777` and earlier are consistent
with the reading here, in which a cover is a point of the cell rather than a set of pieces;
this note does not re-derive them. All references above are to sibling cycles by name only,
with no citation edges: the predecessor note is not on the main line yet, so this note
carries none.

## Gate list with the measured numbers

All 14 gates are computational identities about the explicitly rebuilt finite object, exact
over the integers and the rationals; no floating point enters any gate. The runner is
`scripts/physical_cell_cutting_chamber_cover_mod_four_cycle780_2026_08_14.py` and it uses
the standard library only.

* **K1** object rebuild: 2672 unit pieces, cost floor 6, 400 at the floor, 15800 cuttings
  of 24, 192 used pieces each in 1975, 379200 slots, 384 namings, 2 per piece.
* **K2** the label: product form on 192 of 192 pieces; both namings agree on L and on
  (q1, q2) for 192; q1 = 1 on 96, q2 = 1 on 96.
* **K3** the chambers: 12 walls, 24 orders times 8 signs = 192 chambers, 8 per piece from
  either naming, 8 pieces per chamber, 192 distinct wall sign patterns, 0 on a wall.
* **K4** the local formula on all 192 times 8 = 1536 incident piece and chamber pairs,
  0 failures.
* **K5** geometry: 192 exact sample points, offsets 8/20, 6/20, 4/20, 2/20 from the centre,
  each strictly inside exactly 8 of the 192 pieces, 0 mismatches.
* **K6** the partition read at a point: on all 192 times 15800 = 3033600 chamber and
  cutting pairs the meeting is exactly 1 piece, 0 exceptions.
* **K7** the clique enumeration returns 192 covers of 8, and the sorted cover sets equal
  the 192 distinct chamber piece-sets.
* **K8** claim one on all 192 pieces, 0 failures.
* **K9** claim two on all 192 pieces for each of the 4 axes, 768 checks, 0 failures.
* **K10** totals over the 192 chambers: g1 weight 96, g4 weight 24 on each axis, all even.
* **K11** per cutting on all 15800: the identity holds with 0 failures; cuttings of odd A1
  0, of odd A2 0.
* **K12** S divisible by 4 on 15800 of 15800 cuttings, 0 exceptions; census -8:120,
  -4:2832, 0:9896, 4:2832, 8:120, sum 15800.
* **K13** the control: flipping g1 at one chamber breaks claim one at exactly 8 pieces;
  negating one piece label breaks the identity at 1975 cuttings.
* **K14** the boundary: 8 diagonals, largest |D_w| 4, census of the sum of |D_w| 0 on 9320,
  4 on 6096, 8 on 384, largest 8, A2 divisible by 4 on 15800.
