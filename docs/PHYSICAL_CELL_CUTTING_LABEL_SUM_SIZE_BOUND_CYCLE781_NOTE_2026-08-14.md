# Physical cell cutting: the label sum of a cutting is fixed by its positive half-set count, and the size of the label sum is at most eight

Date: 2026-08-14
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

## What this cycle asks

The unit four-cube cell object is rebuilt from scratch here as in the sibling cycles
`cycle 779` and `cycle 780`: of the 2672 five-corner sets of unit determinant, the ones at
the adjacency cost floor 6 number 400; exact cover of the cell by floor pieces has 15800
solutions, each of 24 pieces; the pieces that actually occur number 192, each in 1975
cuttings; and the naming of a piece by a start corner together with an order of the four
axes gives 384 namings, 2 per piece. A piece carries a handedness label L equal to the sign
of the axis order times the corner weight parity sign of the start corner, and S(T) denotes
the label sum over the 24 pieces of a cutting T.

`cycle 780` identified the covers as the chambers of the twelve-wall cut of the open cell
and derived the mod-four law: S(T) is divisible by 4 on every cutting. It left the size of
S standing as a measurement. Its own boundary section says so plainly: the census puts S in
the five values -8, -4, 0, 4, 8, so |S| is at most 8 over the 15800 cuttings, and nothing in
that derivation forces the bound, since divisibility restricts S to a lattice and not to an
interval.

This cycle derives the bound, pointwise and by a finite obstruction, and the mod-four law
comes back out of it as a corollary. The statement proved is sharper than a bound:

> **T.** Let H be the half set defined below and let p and m be the numbers of pieces of a
> cutting T lying in H with label plus one and minus one. Then p + m = 12, both p and m are
> at most 8, and S(T) = 2 (p - m) = 4 (p - 6). Hence p lies between 4 and 8, S(T) lies in
> -8, -4, 0, 4, 8, and |S(T)| is at most 8.

Three ingredients, each local to one piece and its 8 chambers, and each summed over a
cutting by the partition property of `cycle 780`: a halving identity, a constant count, and
a sealing obstruction. The partition property itself is re-verified here on the rebuilt
object, every chamber meeting every cutting in exactly one piece, with 0 failures over the
15800 cuttings (gate K2). It is the only global input used below.

## The halving identity

Fix the naming of a piece. Of its 2 namings, take the one whose start corner v0 is the
smaller of the two opposite corners; write sigma for its axis order. On that minimal naming

> L(P) = sign(sigma) times chi(v0),

where sign(sigma) is the sign of the order as a permutation and chi(v0) is plus one on a
start corner of even weight and minus one on one of odd weight. The 8 start corners of
minimal namings realise both values, and the formula matches the label of the piece on all
192 pieces with 0 mismatches (gate K3).

Now define the **half set**

> H = the pieces whose minimal naming steps axis 3 within its first 2 steps.

H has 96 members, splitting 48 with L = plus one and 48 with L = minus one (gate K4). The
choice of axis 3 is a choice of one coordinate, made once and kept; the derivation below
never uses which coordinate was taken, and nothing is claimed here about the other three.

A chamber is named (b, s) as in `cycle 780`, with b the order of the four magnitudes of
u = x - centre taken decreasingly and s = (s1, s2, s3) the signs of u at the first three
slots of b; the sign at the fourth slot is not chamber data. Define a function of the
chamber alone,

> g1(b, s) = sign(b) times s1 times s2 times s3 when b ends in axis 3, and 0 otherwise.

**T1.** g1 takes the value minus one on 24 chambers, 0 on 144 and plus one on 24, so its
total over the 192 chambers is 0; and for every piece P,

> the sum of g1 over the 8 chambers of P equals L(P) when P is outside H, and minus L(P)
> when P is inside H.

Both halves are verified on the rebuilt object with 0 failures over the 192 pieces
(gate K5).

The identity telescopes. A cutting holds each of the 192 chambers in exactly one of its 24
pieces, so summing the per-piece sums over T sums g1 over every chamber exactly once:

> 0 = sum over the chambers of g1 = sum over P in T of (sum of g1 over the chambers of P)
> = S(T) - 2 S_H(T),

where S_H(T) is the label sum over the pieces of T that lie in H. Hence

> **S(T) = 2 S_H(T) on every cutting**, with 0 failures over the 15800 (gate K6).

The whole label sum is carried by the half set. That is the first reduction: a sum over 24
pieces becomes twice a sum over the pieces of T inside H, and the next section shows there
are always exactly 12 of those.

## The constant twelve

Define a second function of the chamber alone, this time a set:

> W = the chambers whose order carries axis 3 in its second slot, whose last two slots
> ascend, and whose second sign s2 is plus one.

W has 12 members.

**T2.** For every piece P, the number of members of W among the 8 chambers of P is 1 when P
lies in H and 0 when it does not. Verified on all 192 pieces: 1 on each of the 96 pieces of
H and 0 on each of the other 96, with 0 failures (gate K7).

Summing over a cutting with the partition property again, the left side counts each of the
12 members of W exactly once and the right side counts the pieces of T inside H:

> **every cutting holds exactly 12 pieces of H**, with 0 failures over the 15800 (gate K8).

So p + m = 12 with p and m the counts of half-set pieces of label plus one and minus one,
and S_H = p - m = 2 p - 12. Combined with the halving identity,

> S(T) = 2 S_H(T) = 2 (p - m) = 4 (p - 6).

At this stage S is a function of the single integer p, which lies between 0 and 12; the
mod-four law is already implied, but the size bound still needs p kept away from the ends.

## The sealed families

Two pieces of one cutting share no chamber: if they did, that chamber would meet the
cutting in more than one piece. So the pieces of T inside H with label plus one form a
pairwise chamber-disjoint family inside the 48 positive half-set pieces, and likewise for
the negative ones. If p were 9 or more, T would contain such a family of 9.

Those families can be listed completely. Inside the 48 positive half-set pieces there are
exactly 24 pairwise chamber-disjoint families of 9, and inside the 48 negative ones exactly
24. The count is produced twice by two different searches, an extension walk in index order
over the disjointness graph and a take-it-or-leave-it walk carrying the union of chambers
already used, and the two agree as sets and not merely in count (gate K9).

**T3.** Each of those 48 families is sealed: it leaves a chamber that no member holds, all 8
of whose holding pieces meet the family. Verified for every one of the 48, with 0 failures
(gate K10).

The obstruction follows at once. Suppose a cutting T contained a sealed family F. The
witness chamber c is held by exactly one piece Q of T, and Q is one of the 8 pieces holding
c, so Q shares a chamber with some member of F. That member is also in T, and two pieces of
one cutting share no chamber, so Q is that member; but no member of F holds c, and Q holds
c. The contradiction means no cutting contains any of the 48 families, hence

> **p is at most 8 and m is at most 8.**

The bound is not a bound on the enumeration: it is the statement that a family of 9 which
exists as a disjoint family cannot be part of a partition of the cell, because the chamber
it strands has nowhere left to go.

## The theorem and its corollary

Put the three together. From the constant twelve, p + m = 12; from sealing, p is at most 8
and m is at most 8, so p is at least 4 and lies between 4 and 8; from the halving identity,
S = 4 (p - 6). Therefore

> S lies in -8, -4, 0, 4, 8 and |S| is at most 8, on every cutting,

with 0 failures over the 15800 cuttings (gate K11). Divisibility by 4 is now a corollary
rather than a separate law, and the size bound that `cycle 780` could only measure is
derived pointwise, from the value of p on the single cutting in hand.

The bound is attained at both ends: p takes the value 4 on 120 cuttings and 8 on 120, and
the label sum census matches term for term, -8 on 120, -4 on 2832, 0 on 9896, 4 on 2832 and
8 on 120 (gate K12). The correspondence between the two censuses is the theorem read
backwards, and it is exact, not approximate.

Two controls check that the gates discriminate. Negating g1 at a single chamber breaks the
per-piece identity at exactly 8 pieces, which are precisely the pieces holding that chamber
(gate K13); and dropping a single piece from H breaks the constant twelve at exactly 1975
cuttings, which are precisely the cuttings through that piece (gate K14). Neither number is
imposed: each is measured on the perturbed object and compared with the count the structure
predicts.

## What this does not establish

**The p-census is measured, not derived.** The distribution of p over the 15800 cuttings,
120 at 4, 2832 at 5, 9896 at 6, 2832 at 7 and 120 at 8, is symmetric about 6 and sharply
peaked, and none of that is forced by anything above. The derivation constrains p to the
five values and no further; why the middle value is so much heavier, and why the two ends
carry exactly 120 apiece, is open.

**Family transitivity is measured, not derived.** The 24 families in each half are checked
one at a time, both for the enumeration and for the sealing, and the witness chamber is
found separately for each. Whether the 24 are all alike under the symmetries of the cell,
which would let one sealed family do the work of all of them, is not settled here; no such
action is exhibited, so the regularity visible in the numbers stays a measurement.

**The sharpening deferred by `cycle 780` is not attempted.** That note observed a
divisibility by 4 of one of its two telescoping counts, stronger than the parity its
argument gives, and asked for a certificate taking values modulo 4. Nothing here supplies
one. The present derivation reaches the same divisibility by a different argument, through
p, and so does not answer that question either.

Two further limits, stated plainly. The partition property is verified on the rebuilt
object over all 15800 cuttings rather than proved from the definition of a cutting; the
geometric reading given in `cycle 780` says why it must hold, but this note claims only what
the gates check. And the claim type is bounded_theorem, not a stronger one, because the
object is the finite cell as rebuilt: the statements are theorems about it, and nothing here
extends them to any other cell or to any larger family of cuttings.

## Relation to sibling cycles

The object, the handedness label and the chamber picture are taken from `cycle 779` and
`cycle 780`, and this note extends them rather than corrects them: nothing in either is
withdrawn. The mod-four law of `cycle 780` is re-derived here as a corollary of a sharper
statement, and the size bound its boundary section listed as a measurement is discharged.
The halving identity and the constant twelve are new here, as is the sealing obstruction;
the partition property is the one thing carried over and it is re-checked rather than
assumed. All references above are to sibling cycles by name only, with no citation edges:
the predecessor notes are not on the main line yet, so this note carries none.

## Gate list with the measured numbers

All 14 gates are computational identities about the explicitly rebuilt finite object, exact
over the integers and the rationals; no floating point enters any gate. The runner is
`scripts/physical_cell_cutting_label_sum_size_bound_cycle781_2026_08_14.py` and it uses the
standard library only.

* **K1** object rebuild: 2672 unit pieces, cost floor 6, 400 at the floor, 15800 cuttings
  of 24, 192 used pieces each in 1975, 384 namings, 2 per piece.
* **K2** the partition property: each of the 24 pieces of a cutting holds 8 of the 192
  chambers, each chamber sits in 8 pieces, 0 failures over the 15800 cuttings.
* **K3** the minimal naming: L = sign of the axis order times the corner weight parity
  sign, over 8 start corners, 0 mismatches on the 192 pieces.
* **K4** the half set: the pieces whose minimal naming steps axis 3 within its first 2
  steps number 96, splitting 48 and 48 by label.
* **K5** the halving certificate on chambers: value census -1 on 24, 0 on 144, 1 on 24,
  chamber total 0, and 0 per-piece failures on the 192 pieces.
* **K6** the halving identity S = 2 S_H, 0 failures over the 15800 cuttings.
* **K7** the W certificate: 12 chambers, exactly 1 inside each of the 96 half-set pieces
  and 0 inside each of the other 96, 0 failures on the 192.
* **K8** the constant twelve: every cutting holds exactly 12 half-set pieces, 0 failures
  over the 15800.
* **K9** families of 9 pairwise-disjoint pieces: 24 inside the positive half and 24 inside
  the negative half, with two search orders agreeing.
* **K10** the sealing: each of the 48 families leaves a chamber it does not hold whose 8
  holders all meet it, 0 failures over the 48.
* **K11** the theorem S = 4 (p - 6) with p + m = 12 and p between 4 and 8, 0 failures over
  the 15800 cuttings.
* **K12** the p census 120, 2832, 9896, 2832, 120 at p = 4, 5, 6, 7, 8, sum 15800, and the
  label sum census -8 on 120, -4 on 2832, 0 on 9896, 4 on 2832, 8 on 120.
* **K13** the first control: negating the halving certificate at one chamber breaks the
  per-piece identity at exactly 8 pieces, its holders.
* **K14** the second control: dropping one piece from the half set breaks the constant 12
  at exactly 1975 cuttings, the cuttings through it.
