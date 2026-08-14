# Physical cell cutting: the odd-diagonal count of every cutting is divisible by four

Date: 2026-08-14
Authority: none.
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

## What this cycle asks

The unit four-cube cell object is rebuilt from scratch here as in the sibling cycles
`cycle 779`, `cycle 780` and `cycle 781`: of the 2672 five-corner sets of unit determinant,
the ones at the adjacency cost floor 6 number 400; exact cover of the cell by floor pieces
has 15800 solutions, each of 24 pieces; the pieces that actually occur number 192; and the
naming of a piece by a start corner together with an order of the four axes gives 384
namings, 2 per piece. The two namings of a piece carry opposite start corners and reversed
axis orders, and the minimal naming is the one whose start corner is the smaller of the
two. Write (v0, sg) for that minimal naming.

Every piece then carries a **diagonal label** diag(P) = v0, a value below 8, the lower of
the two opposite corners the staircase path runs between. The quantity this cycle is about
is the count

> A2(T) = the number of pieces of the cutting T whose diagonal label has odd corner
> weight, that is, whose label is one of 1, 2, 4, 7.

`cycle 780` derived a divisibility by 4 for the handedness label sum, and `cycle 781`
sharpened it to a pointwise identity and a size bound. Neither says anything about the
diagonal label, which is a different per-piece attribute: it is a corner, not a sign, and
it is blind to the axis order that the handedness label reads. The census of A2 over the
15800 cuttings nonetheless lands on multiples of 4 only. This note derives that.

> **T.** A2(T) is divisible by 4 for every one of the 15800 cuttings.

The derivation is local everywhere except at one place. A chamber is named (b, s) as in
`cycle 780`, with b the order of the four magnitudes of u = x - centre taken decreasingly
and s the signs of u at the first three slots of b; the sign at the fourth slot is not
chamber data. There are 192 chambers, each piece holds 8 of them, each chamber lies in 8
pieces, and every chamber meets every cutting in exactly one piece. That last statement,
the partition property of `cycle 780`, is re-verified on the rebuilt object with 0 failures
over the 15800 cuttings (gate K1), and it is the only global input used below: every other
step is a statement about one piece and its 8 chambers, or about one chamber.

Two derived sets of pieces are used throughout. The **half set** H is the set of pieces
whose minimal naming steps axis 3 within its first 2 steps; H has 96 members. The
**odd-diagonal half-set indicator** hodd(P) is 1 when P lies in H and its diagonal label
has odd corner weight, and 0 otherwise; exactly 48 of the 192 pieces have hodd = 1
(gate K8). The choice of axis 3 is a choice of one coordinate, made once and kept.

## The sign classes and the local law

Each label w below 8 gives a sign pattern on the four axes, plus one where the bit of the
label is clear and minus one where it is set. Because the labels run below 8 the fourth
axis always carries plus one, so the pattern is genuinely a pattern on three axes with a
fixed fourth. Let Y_w be the class of chambers whose signs agree with that pattern at the
three axes their own order puts first. Each of the 8 classes holds exactly 24 of the 192
chambers (gate K2).

Fix a piece i with minimal naming (v0, sg) and a label w. Compare the sign pattern of the
label diag(i) with the sign pattern of w, not axis by axis but **step by step**: the
mismatch pattern of the pair is the set of step positions k at which the two patterns
disagree at the axis sg[k] that the piece takes at step k. The count of chambers of the
piece lying in Y_w depends on nothing else.

> **T1 (the local law).** For every one of the 1536 pairs of a piece and a label, the
> number of chambers of the piece lying in Y_w is 1 when w is the label of the piece;
> 4 when the mismatch pattern is the last step alone, or the last three steps together;
> 6 when it is the last two steps; and 0 in every other case.

Verified with 0 failures over the 1536 pairs, and the pair classes themselves are counted
rather than assumed: 192 self pairs, 144 pairs whose mismatch is the last step alone, 48
whose mismatch is the last three, 96 whose mismatch is the last two, and 1056 pairs that
contribute nothing. The weighted total is 192 plus 4 times 144 plus 4 times 48 plus 6
times 96, which is 1536, and 1536 is also 8 times 192, one entry for each chamber of each
piece (gate K3). The law is therefore not merely consistent, it is complete: it accounts
for every chamber of every piece exactly once.

## The telescoping identity

Sum the local law over the 24 pieces of a cutting T. By the partition property the left
side counts each of the 24 chambers of Y_w exactly once. On the right, write n_w for the
number of pieces of T whose label is w, a_w for the number whose mismatch pattern at w is
the last step alone, c_w for the number whose mismatch is the last three steps, and q_w
for the number whose mismatch is the last two. Then

> n_w = 24 - 4 a_w - 4 c_w - 6 q_w,

on every cutting at every label, with 0 failures over the 126400 instances (gate K4).
Reduce modulo 4. The two four-weighted terms drop, and 6 q_w becomes 2 q_w, so

> n_w is congruent to 2 q_w modulo 4.

The whole of the mod-four behaviour of the label counts is carried by the class with the
six-valued entry. That the 6 is doing the work and not the 4 is checked directly: replacing
the six-valued entry of the local law by 4 breaks the rule at exactly 96 pairs, which are
exactly the pairs of that class (gate K12).

## The transported label

The class carrying the 6 has a closed form, and the closed form is what turns a statement
about labels into a statement about pieces. For a piece i, let x(i) be the diagonal label
with the bits of the last two axes of its order flipped, and let phi(i) be the smaller of
x(i) and the corner opposite to x(i), so that phi(i) is again a label below 8.

> **T2 (the q class).** For every one of the 1536 pairs, the mismatch pattern of the pair
> is the last two steps if and only if the piece lies in the half set H and phi of the
> piece equals the label w.

Verified with 0 failures, and the 8 fibres of phi on H are counted and all have size 12,
so phi spreads the 96 pieces of H evenly over the 8 labels (gate K5). In particular q_w is
the number of pieces of T lying in H with phi equal to w.

> **T3 (parity transport).** On each of the 96 pieces of H, the corner weight of phi has
> the same parity as the corner weight of the diagonal label.

Verified with 0 failures (gate K6). The reason is short enough to state: x differs from
the diagonal label by flipping the bits of two distinct axes, which changes the corner
weight by an even amount, and passing to the opposite corner flips all 4 bits, which is
even again. So the parity survives both operations.

Now sum over the four labels of odd corner weight. On the left the telescoping identity
gives A2(T), the count of pieces of T with odd label, as the sum of n_w over those four
labels. On the right the sum of q_w over those four labels counts the pieces of T lying in
H whose phi is odd, which by T3 is the count of pieces of T lying in H whose diagonal label
is odd, that is, the hodd-count of T. That coupling is checked on its own, with 0 failures
over the 15800 cuttings (gate K14). Hence

> A2(T) is congruent to 2 times the hodd-count of T, modulo 4.

Divisibility by 4 is now exactly the statement that the hodd-count is even.

## The parity certificate

The evenness comes from a function of the chamber alone, gathered into a set G3 of chambers
by five conditions. Two of them sit over the chambers whose order carries axis 3 in its
second slot with second sign plus one: one takes the orders whose last two slots ascend,
together with disagreeing first and third signs, and the other the orders whose last two
slots descend, together with third sign plus one. Each of those two cells holds 6 chambers.
The remaining three sit over the chambers whose order opens with axis 3 and whose first
sign is plus one: the orders whose last three slots ascend contribute 2 chambers when the
second and third signs agree, the orders whose third slot carries the largest of the last
three axes contribute 4 chambers when the second sign is minus one, and the orders whose
last three slots descend contribute 2 chambers when the third sign is plus one.

> **T4 (the certificate).** The five cells are pairwise disjoint, of sizes 6, 6, 2, 4 and 2,
> so G3 holds 20 chambers, an even number; and for every one of the 192 pieces, the number
> of chambers of the piece lying in G3 has the same parity as hodd of the piece.

The disjointness and the five sizes are measured on the rebuilt object, not read off the
conditions, and the per-piece parity law holds with 0 mismatches over the 192 pieces, its
support being the 48 pieces with hodd = 1 (gates K7 and K8).

Sum the parity law over the 24 pieces of a cutting. By the partition property the left side
counts each chamber of G3 exactly once, giving 20, which is even. The right side is the
hodd-count of T. Therefore

> **every cutting holds an even number of odd-diagonal half-set pieces**,

with 0 failures over the 15800 cuttings (gate K9). Combined with the previous section,
A2(T) is congruent to 2 times an even number modulo 4, hence to 0, which is theorem T, and
it too is confirmed cutting by cutting with 0 failures over the 15800 (gate K10).

That the certificate is load-bearing rather than decorative is checked by dropping a single
chamber from it: the per-piece parity law then fails at exactly 8 pieces, and those 8 are
exactly the pieces holding the dropped chamber (gate K11). The number 8 is measured on the
perturbed object and compared with the count the incidence structure predicts, not imposed.

A last check guards the one arbitrary-looking ingredient, the minimal naming. All of diag,
membership in H, and hodd are recomputed from the second naming of each piece, using the
complement-and-reversal algebra directly on its raw start corner and axis order rather than
by looking the minimal naming up first, and the resulting 192 values agree everywhere
(gate K13). The theorem does not depend on which of the 2 namings of a piece is held.

## The two censuses

Both distributions are **measured, not derived**. Over the 15800 cuttings the hodd-count
takes the value 0 on 472 cuttings, 2 on 1848, 4 on 3384, 6 on 4392, 8 on 3384, 10 on 1848
and 12 on 472; the values are exactly the even numbers up to 12, and the shape is symmetric
about 6 (gate K9). The count A2 takes the value 0 on 112 cuttings, 4 on 1176, 8 on 3936,
12 on 5352, 16 on 3936, 20 on 1176 and 24 on 112; the values are exactly the multiples of 4
up to 24, and the shape is again symmetric, about 12 (gate K10).

The derivation above forces the support of both censuses and nothing more. It says the
hodd-count is even and that A2 is a multiple of 4; it does not say why the middle values
are so much heavier, why the two are so nearly proportional, or why the ends carry 472 and
112 respectively. The censuses are measured, not derived; the divisibility is derived.

## What this does not establish

**The census shapes are not derived.** Only the support is. The symmetry of both
distributions, the peak at the middle value, and every individual multiplicity above are
measurements on the rebuilt object, and nothing in the chain predicts them. In particular
the derivation constrains A2 to the multiples of 4 between 0 and 24 and does not exclude
any of them.

**The certificate is exhibited, not derived.** The set G3 is given by five conditions on
the chamber and its correctness is a finite check over the 192 pieces; nothing here derives
those conditions from the geometry, and no claim is made that they are the only such set.
The same applies to the closed form phi and to the local law: each is stated and checked,
and each could have other presentations.

**The half set carries a choice.** H is defined by axis 3 appearing within the first 2
steps of the minimal naming. The derivation never uses which coordinate was taken, but
neither does it show that the choice is immaterial, and nothing is claimed about the
half sets the other three coordinates would give.

**The partition property is verified, not proved from the definition.** It is checked over
all 15800 cuttings on the rebuilt object; the geometric reading given in `cycle 780` says
why it must hold, but this note claims only what the gates check.

**Nothing here leaves the finite object.** The claim type is bounded_theorem because the
statements are theorems about the unit four-cube cell as rebuilt, with its 192 pieces, its
192 chambers and its 15800 cuttings. No extension to another cell, to a larger family of
cuttings, or to any continuum statement is claimed or implied.

## Relation to sibling cycles

The object, the chamber picture and the partition property are taken from `cycle 779` and
`cycle 780`, and the minimal naming and the half set are taken from `cycle 781`; this note
extends them rather than corrects them, and nothing in any of the three is withdrawn. The
attribute studied here is new: `cycle 780` and `cycle 781` both concern the handedness
label, a sign, whereas A2 counts a property of the diagonal label, a corner. The local law,
the transported label phi, the parity transport and the parity certificate are new here.
The half set reappears in a different role, as the support of the class carrying the
six-valued entry of the local law rather than as the carrier of a label sum, and the fact
that the same 96 pieces serve both is a measurement, not something derived. All references
above are to sibling cycles by name only, with no citation edges: the predecessor notes are
not on the main line yet, so this note carries none.

## Gate list with the measured numbers

All 14 gates are computational identities about the explicitly rebuilt finite object, exact
over the integers and the rationals; no floating point enters any gate. The runner is
`scripts/physical_cell_cutting_diagonal_parity_cycle782_2026_08_14.py` and it uses the
standard library only.

* **K1** object rebuild: 2672 unit pieces, cost floor 6, 400 at the floor, 15800 cuttings
  of 24, 192 used pieces, 192 chambers, 8 chambers per piece, 8 holders per chamber, and
  the partition property with 0 failures over the 15800 cuttings.
* **K2** the sign classes: each of the 8 label classes holds 24 of the 192 chambers, 0 size
  failures over the 8.
* **K3** the local law 1, 4, 4, 6, 0 by mismatch pattern, 0 failures over the 1536 pairs,
  with pair classes 192 self, 144 and 48 at the value 4, 96 at the value 6, 1056 at 0, and
  weighted sum 1536.
* **K4** the telescoping identity for n_w on every cutting at every label, 0 failures over
  the 126400 instances.
* **K5** the q class: the six-valued mismatch pattern holds exactly at the half-set pieces
  with phi equal to the label, 0 failures over the 1536 pairs, and 8 fibres of phi of
  size 12.
* **K6** parity transport on the half set, 0 failures over its 96 pieces.
* **K7** the certificate shape: five pairwise disjoint clause cells of sizes 6, 6, 2, 4, 2,
  total 20 chambers, even.
* **K8** the certificate law: per-piece parity of the certificate count equals hodd, 0
  failures over the 192 pieces, support 48.
* **K9** evenness: every cutting holds an even number of odd-diagonal half-set pieces, 0
  failures over the 15800, with the census 472, 1848, 3384, 4392, 3384, 1848, 472.
* **K10** the theorem: A2 is the sum of n_w over the odd labels 1, 2, 4, 7, congruent to 2
  times the hodd-count and to 0 modulo 4, 0 failures over the 15800, with the census 112,
  1176, 3936, 5352, 3936, 1176, 112.
* **K11** the first control: dropping 1 chamber from the certificate breaks the per-piece
  parity at exactly 8 pieces, its holders.
* **K12** the second control: replacing the 6 of the local law by 4 breaks the rule at
  exactly 96 pairs of the 1536, exactly the q class.
* **K13** naming invariance: the second of the 384 namings, 2 per piece, taken by
  complement and reversal, gives the same 192 hodd values, 0 failures.
* **K14** the coupling: the sum of q_w over the four odd labels equals the hodd-count of
  the cutting, 0 failures over the 15800.
