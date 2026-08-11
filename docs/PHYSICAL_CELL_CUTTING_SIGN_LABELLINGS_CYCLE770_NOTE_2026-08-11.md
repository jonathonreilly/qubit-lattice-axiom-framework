# Physical cell cutting: three sign labellings split every cover four and four (cycle 770)

Date: 2026-08-11
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

Status: a bounded theorem about the cell object of this lane, verified end to end by
[the runner](../scripts/physical_cell_cutting_sign_labellings_cycle770_2026_08_11.py),
which rebuilds the object from nothing and reports 31 gates, all passing. The group of 384
signed coordinate maps has exactly four sign characters. Each transports to a labelling of
the 192 pieces by plus and minus one, and each of the three nonconstant labellings sums to
zero on every one of the 192 covers: every cover carries four pieces of each sign. Two of
the three zeros are structural and contribute nothing to rank; the third is a lone number
that could a priori have been any of the 9 even values from -8 to 8 and is 0, which is one
genuine unit of the excess 39. The theorem is bounded — these four rows supply 2 of a
carried-in ceiling 144 and 1 of the excess 39, and say nothing about the remainder of the
blind space of dimension 87. The work is finite combinatorics on the object itself and adds no axiom
to [the minimal axiom set](MINIMAL_AXIOMS_2026-06-29.md).

## 1. The object and the group

The runner rebuilds everything from the 16 corners of the unit four-cube. Among the
five-corner subsets there are 2672 of unit determinant, and 400 of those sit at the
adjacency cost floor 6. Those 400 admit 15800 exact cuttings of the cell, each cutting
using 24 pieces; exactly 192 distinct pieces occur, and each lies in 1975 cuttings. A
cover is a set of 8 pieces meeting every cutting exactly once, and there are 192 of them
(`C0`, `C1`).

The group is the 384 signed coordinate maps: permute the four coordinates, then flip any
subset of them. It is shut under composition, carries pieces to pieces and covers to
covers, and acts by 384 distinct bijections on each of the two sets. Both actions form a
single orbit, and both point stabilisers have order 2 with the non-identity element
squaring to the identity (`C2` to `C5`).

## 2. The four sign characters and the labellings they transport

Two elements generate all 384 maps, so a sign character is fixed by its two values on
those generators and there are at most 4 of them. Four distinct ones are exhibited — the
trivial character, the sign of the coordinate permutation, the parity of the flip mask,
and the product of the last two — and each is checked to be a homomorphism on all 147456
products, so there are exactly 4 (`C6`).

All 4 take the value 1 on the non-identity element of the piece stabiliser (`C7`). That is
the whole reason the labellings exist. A character trivial on a point stabiliser transports
along the orbit: fix piece 0 with label 1, and give the image of piece 0 under a map the
value of the character at that map. The stabiliser lying in the kernel makes this well
defined, transitivity makes it defined at every piece, and the character being plus and
minus one valued makes the labelling plus and minus one valued. The label at piece 0 is the
one free bit, so each labelling is unique up to a global sign. The runner checks well
definedness and full equivariance on all 73728 map-piece pairs; the plus counts are 192,
96, 96 and 96 (`C9`).

## 3. The measurement

The trivial labelling sums to 8 on every cover, as it must. Each of the other 3 sums to 0
on every one of the 192 covers, and since a cover holds 8 pieces this says that every
cover carries 4 pieces labelled plus and 4 labelled minus (`C10`).

## 4. The separation: two structural zeros and one real one

The three zeros are not the same kind of fact, and that is the honest heart of the note.

The 2 characters taking the value -1 on the non-identity element of the cover stabiliser
have no copy in the cover module at all: their transport to the covers is inconsistent,
and the runner gates that inconsistency directly, on all 192 covers (`C19`). For those two
the cover sum has nowhere to live. The zero is forced by the absence of the part, not by
any cancellation among pieces, and it carries no rank.

The permutation sign character is 1 on both stabilisers, so both sides carry exactly one
copy of it and its cover sum is a single number. A priori that number could have been any
of the 9 even values from -8 to 8. It is 0, and that is measured, not derived (`C20`).
This is the one genuine rank drop among the three, and it is the one that names a unit of
the excess.

## 5. The closed form, and its uniqueness

The flip parity labelling has a closed form: it is the parity of the total number of ones
across the 5 corner index vectors of the piece. The runner checks that identification on
all 192 pieces, with global sign 1 (`C11`), and checks that this parity is the product of
the 4 single-axis parities (`C12`).

No single axis does the job alone. Each single-axis parity is 96 and 96 on the pieces, but
its cover sums are 0 on 144 covers, 8 on 24 and -8 on 24 — the same three counts for all 4
axes — so 48 of the 192 covers are entirely one-sided for it (`C13`). The four one-sided
sets have 48 covers each, they meet pairwise in 0 covers, and together they cover all 192.
Four sets of that size cannot do that unless they are disjoint, so the four sets partition
the covers: every cover is one-sided for exactly 1 axis, and that axis is a function of the
cover (`C14`).

The closed form is unique. Walking all 65536 subsets of the 16 corners and testing each
resulting parity labelling against every cover, exactly 2 subsets give a labelling that
sums to zero on every cover, and both have size 8: the mask 27030 of the odd-weight
corners, and its complement 38505 (`C26`). Because a piece has 5 corners, an odd number,
complementing a subset negates its labelling at every piece — the runner checks that for
all 65536 subsets — so those 2 subsets are one labelling up to the global sign, and the
subset 27030 reproduces the flip parity labelling exactly (`C27`). Up to sign, the flip
parity labelling is therefore the unique corner-subset parity blind to the covers.

## 6. What is not the answer

The orientation sign of a piece — the determinant of the 4 edge vectors from its first
corner, with the corners taken in increasing index order — is also 96 and 96, which makes
it the natural candidate for the splitting function. It is not the answer. Its cover sums
spread out: -8 on 6 covers, -4 on 32, -2 on 16, 0 on 84, 2 on 16, 4 on 32 and 8 on 6. Only
84 of the 192 covers balance, and the orientation sign differs from the corner-ones parity
on 96 of the 192 pieces (`C15`). The split is not the simplex orientation; that candidate
is refuted, not merely unproven.

The complete walk of section 5 sharpens the refutation. Because the orientation sign is not
blind, it is neither of the 2 blind subsets, and in fact it is not any of the 65536
corner-subset parity labellings at all, in either global sign (`C28`). It is not a
different subset — it is not of that form.

## 7. Consequences and boundary

The 3 nonconstant labellings are linearly independent over the rationals: their 3 by 3
Gram determinant is 7077888, which is not zero (`C16`). Each satisfies `M u = 0` exactly
over the integers, where `M` is the 192 by 192 cover-by-piece incidence (`C17`). They
therefore span an explicitly described subspace of dimension 3 inside the blind space.

That blind space has dimension exactly 87, certified from both sides over the integers
rather than scanned. A choice of 105 rows and 105 columns gives a minor of determinant -1,
and a minor whose determinant is a unit forces the rank up to at least 105 in every
characteristic. The inverse of such a minor is itself integral, so each of the 192 rows of
`M` is an integer combination of those 105 rows, which forces the rank back down to at most
105 in every characteristic. The two sides agree, so the rank is exactly 105 and the blind
dimension is exactly 87, over the rationals and over every field alike (`C18`). Rank 105 at
2 fixed primes is kept as corroboration; on its own it would have bounded the blind
dimension from above and no more.

In the part bookkeeping, the four one-dimensional rows have piece multiplicities 1, 1, 1, 1
and cover multiplicities 1, 1, 0, 0. They supply 1 + 1 + 0 + 0 = 2 to the covariant rank
ceiling and 0 + 1 + 0 + 0 = 1 to the excess (`C21`). Against a ceiling of 144 carried in
from an earlier cycle of this lane — from which the measured rank 105 leaves an excess of
39 — these four rows account for 2 of the ceiling and 1 of the excess (`C22`). The 144 is
carried in rather than measured here, and the cycle it comes from is in flight rather than
on the main line, so the comparison is context and nothing in this cycle rests on it. The
remaining drops of that count sit in rows of dimension above one and are untouched here.

One number invites a connection that is not made. The count 48 appears twice: as the number
of covers one-sided for a single axis (`C13`), and as the blind floor of the earlier cycle
of this lane. No connection between the two is derived here, and none should be read into
the coincidence of the value.

## 8. Runner summary

The runner is standalone: it rebuilds every object it uses and reads no cache. It prints
31 gate lines, and no floating point enters any of them — all numbers are exact
computational identities over the integers, the rationals and 2 fixed primes.

Three wrong-value rejectors show that the gates discriminate. Flipping the label of any
single one of the 192 pieces breaks a cover for each of the 3 labellings, with the fewest
and the most both 8 (`C23`). Each of 72 swaps of oppositely labelled pieces, 24 per
labelling, breaks between 8 and 16 covers (`C24`). Perturbing the action by a transposition
breaks the transport exactly when the 2 swapped pieces carry different labels, which
happens in 16 of the 36 combinations tried and for 8 of the 12 transpositions (`C25`).

The run stays under 900 s, under 2500 MB and under 5200 printed characters (`C29`), and
the source is pure ASCII with no tab and no long dash, with all 41 barred strings absent
(`C30`). The final line is:

```
TOTAL: PASS=31 FAIL=0
```
