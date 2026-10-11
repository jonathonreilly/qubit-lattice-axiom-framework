# Handoff — toe-chiral-record-20261010

Base `0b208e91cfc`. Branch `physics-loop/toe-chiral-record-20261010`.
Worktree: `/Users/jonreilly/.grok/campaigns/toe-chiral-20261010/wt`.
One worktree. Do not touch PR 9475 or the Codex photon and D3Q27 trees.

## Done

PR https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9477
is open. Do not merge it and do not open a second PR.

Cycle 1. Soldered bond-symmetric factors on one proper orbit of
`(1, 2, 3)`: linear dimension 84, six direction-record orbits, far-end
rank 6, affine dimension 78. Runner `PASS=14 FAIL=0`. No factor is
selected.

Cycle 2. Order-blindness on the 7-site cross does not cut that family
to the exhibited modulus-3 line. The same cap sign on `a·d = 1` and
`a·d = 2` gives two further strictly positive soldered lines, and the
parent converse makes each order-blind. A mixture of modulus 3 and
modulus 2 has a two-neighbour moment `25/24`. Runner `PASS=22 FAIL=0`.
The rest of the order-blind set is not classified.

Cycle 3. Inside the span of those three cap signs, a nonzero scale has
every product mean equal to 1 only on the three axes. A two-modulus
witness has moment `13/12`. The mixture `(-2, -2, 1)` cancels the
pairwise moments and still has three-neighbour moment `-3`. Runner
`PASS=9 FAIL=0`. Factors outside the span are not classified.

Cycle 4. Each opposite cap `a·d = -m` for `m` in `{1, 2, 3}` is a
strictly positive soldered line, with product mean 1 on all 729 weight
patterns. The bond from `(1, -2, -3)` to `(1, 2, 3)` along `e_z` has
level `-3` product `-1` and positive-cap product 0, so that line sits
outside the positive span. Levels `-1` and `-2` have the same
separation. Runner `PASS=23 FAIL=0`. Slices outside the six oriented
caps are not classified.

Cycle 5. The transverse cross product on the caps `a·e_z = -3` and
`b·e_z = 3`, kept when the transverse absolute values match, extends
by proper rotations to a soldered kernel with values in `{-1, 0, 1}`.
Each record activates one direction and every slice sums to 0, so
every neighbour product has mean 1. The slice at `(-2, 1, 3)` is
nonzero and orthogonal to all six cap signs. Runner `PASS=14 FAIL=0`.
The rest of the order-blind set on this orbit is not classified.

Cycle 6. The 48 signed permutations of `(1, 2, 3)` carry a soldered
bond-symmetric space of dimension 312. Twelve far-end rows are
independent and each totals 48, so far-end sum 1 is an affine space of
dimension 300. 264 orbits have 24 images and 48 have 12. Ordered
covariant bonds form 576 orbits. Runner `PASS=15 FAIL=0`. No factor is
selected. Order-blindness on this alphabet is not classified.

Cycle 7. The transverse-cross formula at absolute heights 1 and 2 each
gives a soldered kernel with values in `{-1, 0, 1}`, one live direction
per record, and slice sums 0. For absolute parameter below 1 the factors
are positive, and the parent converse makes each family order-blind. The
six cap lines and the three transverse crosses are linearly independent,
so each lower-height kernel lies outside the six caps and the modulus-3
cross. Witnesses: height 1 sends `(-3, -2, -1)` to `(-3, 2, 1)` with
value `-1`; height 2 sends `(-3, 1, -2)` to `(3, 1, 2)` with value `-1`.
The sum of the two kernels has two-neighbour moment `23/24`. Runner
`PASS=19 FAIL=0`. Kernels outside these nine are not classified.

Cycle 8. The transverse cross on pairs whose absolute transverse
coordinates are swapped, at each absolute height 1, 2, and 3, gives a
soldered kernel with values in `{-1, 0, 1}`, one live direction, and
slice sums 0. For absolute parameter below 1 the factors are positive,
and the parent converse makes each family order-blind. The six cap
lines, the three matched crosses, and these three swapped crosses are
linearly independent. Witnesses, each of value `-1`: height 1 from
`(-3, -2, -1)` to `(-2, -3, 1)`; height 2 from `(-3, 1, -2)` to
`(1, -3, 2)`; height 3 from `(-2, -1, -3)` to `(-1, -2, 3)`. The sum of
the matched and swapped kernels at height 3 stays one-hot with slice
sum 0. The sum of the swapped kernels at heights 1 and 2 has moment
`23/24`. Runner `PASS=20 FAIL=0`. Kernels outside these twelve are not
classified.

Cycle 9. For each sign and each modulus in `{1, 2, 3}`, the soldered
bond-symmetric kernels supported on `a·d = (sign) m` and
`b·d = -(sign) m`, with slice sum 0, have dimension 3. Six patterns
give dimension 18. Each pattern is spanned by the cap line and the
matched and swapped transverse crosses. The six positive-cap crosses
lie outside the previous twelve kernels. For absolute parameter below 1
each of those six is positive and has product mean 1. The sum of the
positive matched crosses at heights 1 and 2 has moment `23/24`. Runner
`PASS=22 FAIL=0`. Kernels with two live directions are not classified.

Cycle 10. The sum of the cap line at level `+3` and the matched
transverse cross on `a·d = -3` is bond-symmetric, takes values in
`{-1, 0, 1}`, and activates two opposite directions on every record.
Every slice sums to 0 and every opposite-direction product has mean 1.
For absolute parameter below 1 the factors are positive. The seed
`(1, 2, 3)` is live in `e_z` and `-e_z`. The two cap lines at levels
`+3` and `-3` have moment `7/6` on `e_x` at `(-3, -2, -1)`. Runner
`PASS=14 FAIL=0`. This sum lies in the cap-pair span. Kernels outside
that span are not classified.

Cycle 11. A soldered bond-symmetric kernel supported on one reversal
class of endpoint heights, with every slice sum 0, has dimension 3.
There are 21 classes. The kernel is order-blind for a nonzero vector
only when the heights are opposite. Those six classes are spanned by
the eighteen cap-pair kernels. On each of the other fifteen classes
the pair moments leave only zero. Witness sums `-1` and `1` have
uniform averages `-1/24` and `1/24`. Runner `PASS=27 FAIL=0`. A sum of
two classes is not classified.

Cycle 12. A slice-zero soldered kernel supported on one unequal height
signature and at most one other signature has its unequal coordinates
forced to zero. All 240 partner pairs put the six unequal monomials in
pivot position with no remaining term. The kernel drops to the partner.
By the single-signature classification it lies in the eighteen cap-pair
kernels when it is order-blind and nonzero. The square test does not
force signature `(-3, -3)` to zero beside `(3, -3)`. Runner
`PASS=9 FAIL=0`. Equal-height pairs are not classified.

Cycle 13. Every pair of height signatures has joint slice kernel 6, so
the kernel is the direct sum of the two signature kernels. Beside an
opposite partner, the pair moments force an equal-height block to
zero, and the kernel is that opposite signature. Beside a second
equal-height signature both blocks are zero. The three quadrics have
only the origin as a common zero; the eliminant resultant is
`113027603142816`. The triple `(-3, -3)`, `(-3, 3)`, `(3, -3)` has
joint slice kernel 10, the maximum among 1330 triples. Runner
`PASS=16 FAIL=0`. That extra direction is not classified.

Cycle 14. On the signatures `(-3, -3)`, `(-3, 3)`, and `(3, -3)`, the
joint slice kernel has dimension 10. The complement of the three
signature kernels is one line, with values `-1`, `+1`, and `+1` on
one bond orbit of each. Every record has two live directions. The
moment on `±e_x` at `(-3, -2, -1)` is `2`, and the uniform average is
`1/12`. The line is outside the eighteen and is not order-blind.
Runner `PASS=13 FAIL=0`. A mixture with the signature kernels is not
classified.

Cycle 15. Every rational linear mixture of that line with the three
signature kernels whose two-neighbour moments all vanish has complement
coefficient zero and equal-height block zero. The mixture is supported
on `(-3, 3)` and `(3, -3)`, so it lies in the eighteen. The cross
moments between those two blocks are not solved. A fourth signature
is outside the ansatz. Runner `PASS=12 FAIL=0`.

Cycle 16. On the 48 signed permutations of `(1, 2, 3)`, the family
`phi_d(a, b) = 1 + c (a·d)(b·(-d))` is bond-symmetric and soldered, and
every far-end sum equals 48. At `c = 1/10` the factor is strictly
positive, and the uniform moment on `±e_z` at `(1, 2, 3)` is `71/50`.
Order-blindness cuts the normalised space. The order-blind subset is
not classified. Runner `PASS=12 FAIL=0`.

Cycle 17. On the same alphabet the transverse-sign cap at coefficient
`1/2` is bond-symmetric and soldered, takes values `1/2`, `1`, and
`3/2`, and all 729 partner patterns have product mean 1. Every far-end
sum equals 48. The bonds on `e_z` from `(1, 2, 3)` and `(-2, 1, 3)` to
`(1, 2, -3)` have transverse products `+1` and `-1` against chiral
product `-1`, so no scale of the chiral cap matches. Runner
`PASS=10 FAIL=0`.

Cycle 18. On the same alphabet the sign product of orbit chirality and
the transverse sign, at coefficient `1/2`, is bond-symmetric and
soldered. The values are `1/2`, `1`, and `3/2`, and all 729 partner
patterns have product mean 1. Every far-end sum equals 48. The bonds on
`e_z` from `(1, 2, 3)`, `(2, -1, 3)`, and `(-2, -1, 3)` to
`(-2, -1, -3)` have kernel rows `(1, 1, 1)`, `(1, -1, -1)`, and
`(-1, 1, -1)`, with determinant `4`. The sign-product kernel is not a
linear combination of the chiral cap and the transverse-sign cap.
Runner `PASS=11 FAIL=0`.

Cycle 19. On the same alphabet the matched and swapped transverse
crosses on the caps `a·d = 3` and `b·d = -3` are bond-symmetric and
soldered. At coefficient `1/2` each factor takes values `1/2`, `1`,
and `3/2`. Each record meets at most one live direction and every left
slice sums to 0, so every neighbour product has mean 1. Every far-end
sum equals 48. Five bonds on `e_z` from `(-2, -1, 3)` have determinant
`8` against the three caps. Neither cross is a linear combination of
those caps. Runner `PASS=10 FAIL=0`.

Cycle 20. On the same alphabet the matched and swapped transverse
crosses at absolute heights 1 and 2 are bond-symmetric and soldered.
At coefficient `1/2` each factor takes values `1/2`, `1`, and `3/2`.
Each record meets at most one live direction of that cross and every
left slice sums to 0, so every neighbour product has mean 1. Every
far-end sum equals 48. Nine bonds on `e_z` have determinant `8` in
the five height-3 columns followed by these four crosses. Each
lower-height cross is nonzero where the other eight kernels vanish, so
none is a linear combination of the five. Runner `PASS=10 FAIL=0`.

Cycle 21. On the same alphabet the chirality cap, the transverse-sign
cap, and their sign product, at each absolute height 1 and 2, are
bond-symmetric and soldered. At coefficient `1/2` each factor takes
values `1/2`, `1`, and `3/2`. Each cap sign has mean 0 and at most one
live direction, so every neighbour product has mean 1. Every far-end
sum equals 48. Five bonds at each height have determinant `-16`. The
bond from `(-2, -3, 1)` to `(-2, -3, -1)`, and the bond from
`(-1, -3, 2)` to `(-1, -3, -2)`, each have all nine comparison kernels
equal to 0 while the three caps at that height are nonzero. None of
the six caps is a linear combination of the nine. Runner
`PASS=10 FAIL=0`.

Cycle 22. On the same alphabet the parallel transverse-dot sign at each
absolute height 1, 2, and 3 is bond-symmetric and soldered. It is the
sign of the negative transverse dot product when the transverse cross
product vanishes on opposite caps of that height, and 0 otherwise. At
coefficient `1/2` each factor takes values `1/2`, `1`, and `3/2`. Each
record meets at most one live direction and every left slice sums to 0,
so every neighbour product has mean 1. Every far-end sum equals 48.
The bonds from `(-2, -3, 1)` to `(-2, -3, -1)` and to `(2, 3, -1)`,
from `(-1, -3, 2)` to `(-1, -3, -2)` and to `(1, 3, -2)`, and from
`(-2, -1, 3)` to `(-2, -1, -3)` and to `(2, 1, -3)`, agree on all
fifteen comparison kernels and differ by 2 on this kernel. On each
opposite-height pair the slice-zero bond-symmetric soldered kernels
are 10-dimensional. The five same-height kernels span 5 of them, and
this kernel raises the rank to 6. Runner `PASS=10 FAIL=0`.

Cycle 23. On the same alphabet the matched oblique transverse-dot sign
at each absolute height 1, 2, and 3 is bond-symmetric and soldered. It
is the sign of the negative transverse dot product when the absolute
transverse coordinates match and the transverse cross product is
nonzero, and 0 otherwise. Its support is disjoint from the parallel
transverse-dot kernel. At coefficient `1/2` each factor takes values
`1/2`, `1`, and `3/2`. Each record meets at most one live direction and
every left slice sums to 0, so every neighbour product has mean 1.
Every far-end sum equals 48. The bonds from `(-3, -2, 1)` to
`(-3, 2, -1)` and from `(-3, 2, 1)` to `(3, 2, -1)`, from
`(-3, -1, 2)` to `(-3, 1, -2)` and from `(-3, 1, 2)` to `(3, 1, -2)`,
and from `(-2, -1, 3)` to `(-2, 1, -3)` and from `(-2, 1, 3)` to
`(2, 1, -3)`, agree on all fifteen comparison kernels, carry parallel
dot 0, and differ by 2 on this kernel. Inside the 10-dimensional
opposite-height ansatz the rank rises from 6 to 7. Runner
`PASS=10 FAIL=0`.

Cycle 24. On the same alphabet the swapped transverse-dot sign at each
absolute height 1, 2, and 3 is bond-symmetric and soldered. It is the
sign of the negative transverse dot product when the absolute transverse
coordinates are swapped and that dot product is nonzero, and 0 otherwise.
Its support is disjoint from the parallel-dot kernel and from the matched
oblique dot. At coefficient `1/2` each factor takes values `1/2`, `1`,
and `3/2`. Each record meets at most one live direction and every left
slice sums to 0, so every neighbour product has mean 1. Every far-end
sum equals 48. The bonds from `(-3, -2, 1)` to `(-2, -3, -1)` and from
`(-3, 2, 1)` to `(2, -3, -1)`, from `(-3, -1, 2)` to `(-1, -3, -2)` and
from `(-3, 1, 2)` to `(1, -3, -2)`, and from `(-2, -1, 3)` to
`(-1, -2, -3)` and from `(-2, 1, 3)` to `(1, -2, -3)`, agree on all
fifteen comparison kernels, carry parallel dot 0 and matched oblique dot
0, and differ by 2 on this kernel. Inside the 10-dimensional
opposite-height ansatz the rank rises from 7 to 8. Runner
`PASS=10 FAIL=0`.

Cycle 25. On the same alphabet the orthogonal swapped cross at each
absolute height 1, 2, and 3 is bond-symmetric and soldered. It is the
sign of the transverse cross product when the absolute transverse
coordinates are swapped and the transverse dot product vanishes, and 0
otherwise. Its support is disjoint from the three dot kernels and is a
proper subset of the swapped-cross support. At coefficient `1/2` each
factor takes values `1/2`, `1`, and `3/2`. Each record meets at most one
live direction and every left slice sums to 0, so every neighbour
product has mean 1. Every far-end sum equals 48. Four bonds at each
height, with weights `-1`, `-1`, `+1`, and `+1`, have alternating sum 0
on all twenty-four comparison kernels and alternating sum 2 on this
kernel. Inside the 10-dimensional opposite-height ansatz the rank rises
from 8 to 9. Runner `PASS=10 FAIL=0`.

Cycle 26. On the same alphabet the scaled cross-dot kernel at each
absolute height 1, 2, and 3 is bond-symmetric and soldered. On opposite
caps it is twice the sign of the negative cross-dot product when the
absolute transverse coordinates match and the dot product is positive,
and it is that sign when the coordinates are swapped and the dot product
is nonzero. It is 0 when either product vanishes or when the coordinates
match and the dot product is negative. Its product with the parallel-dot
kernel is 0, and so is its product with the orthogonal swapped cross.
At coefficient `1/4` each factor takes values `1/2`, `3/4`, `1`, `5/4`,
and `3/2`. Each record meets at most one live direction and every left
slice sums to 0, so every neighbour product has mean 1. Every far-end
sum equals 48. Four bonds at each height, with weights `+1`, `+1`, `-1`,
and `-1`, have alternating sum 0 on all twenty-seven comparison kernels
and alternating sum 4 on this kernel. Inside the 10-dimensional
opposite-height ansatz the rank rises from 9 to 10. Those ten kernels
are a basis of that ansatz. Runner `PASS=10 FAIL=0`.

Cycle 27. On the same alphabet every rational mixture of the ten basis
kernels on one opposite-height pair is bond-symmetric and soldered.
Every left slice sums to 0, and each record meets at most one live
direction, so every neighbour product has mean 1. The identity covers
the whole rational span. The mixture with all ten coefficients equal to
`1/32` takes the values `29/32`, `15/16`, `31/32`, `1`, `33/32`,
`17/16`, and `19/16`. The mean on `e_z` at `(1, 2, -3)` is 1, and the
mean on `-e_x` and `e_z` at `(2, 1, 3)` and `(1, 2, -3)` is 1. At height
1 the bond on `-e_x` from `(-1, -3, -2)` to `(1, -3, 2)` has chirality
`1` and scaled value `-2`, and the bond to `(1, -3, -2)` has chirality
`-1` and scaled value `0`. Coefficient `2` on the chirality cap takes
values `-1`, `1`, and `3` and still has those means equal to 1. The
integer coefficients `1` through `10` are a moment check, not the span.
Runner `PASS=8 FAIL=0`.

Cycle 28. On the same alphabet the sum of the height-1 and height-2
chirality caps at coefficient `1/2` is strictly positive, with values
`1/2`, `1`, and `3/2`. Every one-neighbour mean is 1. The mean on
`-e_x` and `-e_y` at `(1, -3, -2)` and `(-3, 2, -1)` is `97/96`, and
`1536` unordered two-direction pairs have mean different from 1. The
sum of the height-1 chirality cap and the height-2 sign-product cap, at
the same coefficient, has every two-direction mean equal to 1. Each
record meets at most two live directions, so every neighbour product of
that second mixture has mean 1. These two mixtures do not classify the
coefficient span of two bases. Runner `PASS=9 FAIL=0`.

Cycle 29. On the same alphabet the parity span is the rational span of
the chirality cap, the transverse-sign cap, their sign product, the
swapped transverse cross, the parallel transverse dot, the matched
oblique dot, and the orthogonal swapped cross. The matched transverse
cross, the swapped transverse dot, and the scaled cross-dot kernel lie
outside it. For each height and partner, the span splits into an odd
space of dimension 4 and an even space of dimension 3. Cross moments
of two parity-span vectors vanish exactly when the odd parts are not
both nonzero and the even parts are not both nonzero. The height-1 and
height-2 chirality caps, and the two sign-product caps, have moment
`97/96`. The swapped crosses at heights 1 and 2, and at heights 2 and
3, have moment `95/96`. The swapped crosses at heights 1 and 3 have
every cross moment equal to 0. The parallel-oblique sum plus the
height-2 sign product, at coefficient `1/2`, takes values `1/2`, `1`,
and `3/2` and has every cross moment equal to 0. The ten-kernel
coefficient span is not classified. Runner `PASS=9 FAIL=0`.

Cycle 30. On the same alphabet the excluded span is the rational span
of the matched transverse cross, the swapped transverse dot, and the
scaled cross-dot kernel. For every ordered pair of heights among 1, 2,
and 3, a vector in that span and a ten-kernel vector at the other
height have every kernel cross sum equal to 0 exactly when one of the
two vectors is 0. The matched kernel at height 1 with the zero vector
at height 2 is such a pair. The matched kernels at heights 1 and 2 fail
on `-e_x` and `-e_y` at `(-1, -2, -3)` and `(-1, -2, 3)`, with both
rights `(1, 2, 3)`, centre values `(0, 1)` and `(0, -1)`, kernel cross
sum `-1`, and direct alphabet mean `47/48`. Matched and swapped-dot
self-cross sums lie in `{-1, 0, 1}`. Scaled self-cross sums lie in
`{-4, -1, 0, 2}` on heights `(1, 2)` and `(2, 3)`, and in
`{-2, 0, 1, 4}` on heights `(1, 3)`. A vector with both a parity-span
component and a nonzero excluded coefficient is outside this ansatz.
The ten-kernel coefficient span is not classified. Runner
`PASS=9 FAIL=0`.

Cycle 31. On the same alphabet each plane spanned by one parity kernel
and one excluded kernel is settled against any ten-kernel partner. In
the twenty planes other than the matched oblique dot plus the matched
cross, both coefficients nonzero forces every kernel cross sum to
vanish only for the zero partner. In that remaining plane the ratio of
matched over oblique has a three-dimensional partner kernel exactly at
`1` and `-1`. On height pairs `{1, 2}` and `{2, 3}` the ratio `1` is
spanned by matched plus oblique, by minus swapped plus swapped-dot
plus orthogonal, and by minus the transverse sign minus the sign
product plus twice matched plus twice scaled. The ratio `-1` reverses
the signs of matched, swapped-dot, the transverse sign, and the sign
product. On `{1, 3}` those bases are exchanged. Oblique plus matched
at heights 1 and 2 has every cross sum equal to 0 against itself. The
same vector at heights 1 and 3 has witness cross sum `-4`. Chirality
plus matched against the chirality cap has witness cross sum `2`.
Oblique plus twice matched against oblique has witness cross sum `-1`.
A sum of two parity kernels is outside this ansatz. The ten-kernel
coefficient span is not classified. Runner `PASS=10 FAIL=0`.

Cycle 32. On the same alphabet the two ratio spans of the
oblique-matched plane each have dimension 3. A nonzero vector in
either span has two or more nonzero parity-kernel coefficients and a
nonzero excluded coefficient exactly when it is off that span's
oblique-matched line. Every nonzero vector in either span has a
three-dimensional partner kernel. On height pairs `(1, 2)`, `(2, 1)`,
`(2, 3)`, and `(3, 2)` the partner kernel is the same span. On
`(1, 3)` and `(3, 1)` the two spans exchange. Minus the swapped cross
plus the swapped transverse dot plus the orthogonal cross, at height
1, has every kernel cross sum equal to 0 against matched plus oblique
at height 2. The centre pairs on `-e_x` and `-e_y` are `(-2, 0)` and
`(0, 2)`. The same vectors at heights 1 and 3 have centre pairs
`(0, 0)` and `(-2, 2)` and kernel cross sum `-4`. A vector outside
both spans is not in this count. The ten-kernel coefficient span is
not classified. Runner `PASS=10 FAIL=0`.

Cycle 33. On the same alphabet the equal-coefficient line through the
chirality cap, the transverse-sign cap, and the matched cross lies
outside both ratio spans, because the sum has chirality coefficient 1
and both spans have chirality coefficient 0. A nonzero scale has
partner rank 10 on every ordered height pair, so the only ten-kernel
partner is 0. At coefficient 1 the bond on `-e_x` and `-e_y` against
the height-2 chirality cap has centre pairs `(2, 1)` and `(-2, -1)`
and kernel cross sum `4`. Twice the line has centre pairs `(4, 1)` and
`(-4, -1)` and kernel cross sum `8`. A different ratio of these three
kernels is not in this count. The ten-kernel coefficient span is not
classified. Runner `PASS=7 FAIL=0`.

Cycle 34. On the same alphabet the line through the chirality cap,
twice the transverse-sign cap, and the matched cross lies outside the
equal-coefficient line, because the transverse-sign coefficient is 2
and the chirality coefficient is 1. It also lies outside both ratio
spans, because those spans have chirality coefficient 0. A nonzero
scale has partner rank 10 on every ordered height pair, so the only
ten-kernel partner is 0. At coefficient 1 the bond on `-e_x` and
`-e_y` against the height-2 chirality cap has centre pairs `(3, 1)`
and `(-3, -1)` and kernel cross sum `6`. Twice the line has centre
pairs `(6, 1)` and `(-6, -1)` and kernel cross sum `12`. A different
ratio of these three kernels is not in this count. The ten-kernel
coefficient span is not classified. Runner `PASS=7 FAIL=0`.

Cycle 35. On the same alphabet the line through the chirality cap, the
transverse-sign cap, and twice the matched cross lies outside the
equal-coefficient line and outside the doubled transverse-sign line.
It also lies outside both ratio spans, because those spans have
chirality coefficient 0. A nonzero scale has partner rank 10 on every
ordered height pair, so the only ten-kernel partner is 0. At
coefficient 1 the bond on `-e_x` and `-e_y` against the height-2
chirality cap has rights `(1, -2, -3)` and `(-3, 2, -1)`, centre pairs
`(0, 1)` and `(-2, -1)`, and kernel cross sum `2`. Twice the line has
centre pairs `(0, 1)` and `(-4, -1)` and kernel cross sum `4`. The
equal-coefficient vector on the same bond has kernel cross sum `1`. A
different ratio of these three kernels is not in this count. The
ten-kernel coefficient span is not classified. Runner `PASS=8 FAIL=0`.

Cycle 36. On the same alphabet the line through the chirality cap,
twice the transverse-sign cap, and twice the matched cross lies outside
the equal-coefficient line, the doubled transverse-sign line, and the
doubled matched line. It also lies outside both ratio spans, because
those spans have chirality coefficient 0. A nonzero scale has partner
rank 10 on every ordered height pair, so the only ten-kernel partner is
0. At coefficient 1 the bond on `-e_x` and `-e_y` against the height-2
chirality cap has rights `(1, -2, -3)` and `(-3, 2, -1)`, centre pairs
`(1, 1)` and `(-3, -1)`, and kernel cross sum `4`. Twice the line has
centre pairs `(2, 1)` and `(-6, -1)` and kernel cross sum `8`. The
doubled transverse-sign vector on the same bond has kernel cross sum
`3`. A different ratio of these three kernels is not in this count. The
ten-kernel coefficient span is not classified. Runner `PASS=8 FAIL=0`.

Cycle 37. On the same alphabet the line through twice the chirality
cap, the transverse-sign cap, and the matched cross lies outside the
equal-coefficient line, the doubled transverse-sign line, the doubled
matched line, and the line with transverse-sign coefficient 2 and
matched coefficient 2. It also lies outside both ratio spans, because
those spans have chirality coefficient 0. A nonzero scale has partner
rank 10 on every ordered height pair, so the only ten-kernel partner is
0. At coefficient 1 the bond on `-e_x` and `-e_y` against the height-2
chirality cap has rights `(1, -2, -3)` and `(-3, 2, -1)`, centre pairs
`(-1, 1)` and `(0, -1)`, and kernel cross sum `-1`. Twice the line has
centre pairs `(-2, 1)` and `(0, -1)` and kernel cross sum `-2`. The
doubled sign and matched vector on the same bond has kernel cross sum
`4`. A different ratio of these three kernels is not in this count. The
ten-kernel coefficient span is not classified. Runner `PASS=8 FAIL=0`.

Cycle 38. On the same alphabet the chirality, transverse-sign, and
matched span is the rational span of those three kernels. It is
3-dimensional and meets each ratio span of the oblique-matched plane
only at 0. For every ordered height pair, a nonzero vector in the span
has partner rank 10 exactly when its matched coefficient is nonzero, and
then the only ten-kernel partner is 0. When the matched coefficient is
0, the partner rank is 7 and the partner kernel is the even space of
the partner height relative to the source height. On pairs `(1, 2)`,
`(2, 1)`, and `(1, 3)` that space is spanned by the sign product, the
oblique dot minus the parallel dot, and the orthogonal cross minus half
the swapped cross. On pairs `(3, 1)`, `(2, 3)`, and `(3, 2)` it is
spanned by the sign product, the swapped cross, and the parallel dot
plus the oblique dot. The generators have excluded coefficients 0. The
chirality cap pairs with the sign product. At heights 1 and 2 the bond
on `-e_x` and `-e_y` has centre pairs `(-1, 1)` and `(1, 1)` and kernel
cross sum 0. The chirality cap plus the matched cross has centre pairs
`(-1, 1)` and `(0, 1)` and kernel cross sum `-1`. The triples
`(2, -3, 5)` and `(2, -3, 0)` have partner ranks 10 and 7. A vector
outside the three kernels is not in this count. The ten-kernel
coefficient span is not classified. Runner `PASS=8 FAIL=0`.

Cycle 39. On the same alphabet the even span of an ordered height pair
is the rational span of the even basis of the source height. It is
3-dimensional, its excluded coefficients are 0, and it meets the three
excluded axes only at 0. Every nonzero vector has partner rank 6. The
partner kernel is the odd space of the partner height. On pairs
`(1, 2)`, `(2, 1)`, and `(1, 3)` that space is spanned by the chirality
cap, the transverse-sign cap, the swapped cross, and the parallel dot
plus the oblique dot. On pairs `(3, 1)`, `(2, 3)`, and `(3, 2)` it is
spanned by the chirality cap, the transverse-sign cap, the oblique dot
minus the parallel dot, and the orthogonal cross minus half the swapped
cross. The sign product lies in every even span. At heights 1 and 2 the
bond on `-e_x` and `-e_y` against the chirality cap has centre pairs
`(1, -1)` and `(1, 1)` and kernel cross sum 0. Against the matched
cross the centre pairs are `(1, 0)` and `(1, 1)` and the kernel cross
sum is `1`. The coefficient triples `(1, 0, 0)` and `(1, 1, 1)` have
partner rank 6. A vector outside the even span is not in this count.
The ten-kernel coefficient span is not classified. Runner
`PASS=8 FAIL=0`.

Cycle 40. On the same alphabet the swapped cross is odd on ordered pairs
`(1, 2)`, `(2, 1)`, and `(3, 1)`, and even on `(1, 3)`, `(2, 3)`, and
`(3, 2)`. On each odd pair a nonzero scale has partner rank 7, and the
partner kernel is the even space of the partner height, so no ten-kernel
partner lies outside that space. On `(1, 2)` and `(2, 1)` that space is
spanned by the sign product, the oblique dot minus the parallel dot, and
the orthogonal cross minus half the swapped cross. On `(3, 1)` it is
spanned by the sign product, the swapped cross, and the parallel dot
plus the oblique dot. The generators have excluded coefficients 0. On
each even pair the even-span result gives partner rank 6 and partner
kernel equal to the odd space, which meets the even space only at 0. At
heights 1 and 2 the bond on `-e_x` and `-e_y` against the sign product
has centre pairs `(1, -1)` and `(-1, -1)` and kernel cross sum 0.
Against the chirality cap the centre pairs are `(1, -1)` and `(-1, 1)`
and the kernel cross sum is `-2`. Against the matched cross the centre
pairs are `(1, 0)` and `(-1, 1)` and the kernel cross sum is `-1`. At
heights 1 and 3 the same directions against the chirality cap have
centre pairs `(-1, 1)` and `(-1, -1)` and kernel cross sum 0. Against
the sign product the centre pairs are `(-1, 1)` and `(-1, 1)` and the
kernel cross sum is `-2`. A vector other than the swapped cross is not
in this count. The odd space is not settled. The ten-kernel coefficient
span is not classified. Runner `PASS=9 FAIL=0`.

Cycle 41. On the same alphabet the odd space of an ordered height pair
is the rational span of the odd basis of the source height. It is
4-dimensional, its excluded coefficients are 0, and it meets the even
basis only at 0. Every nonzero vector has partner rank 7. The partner
kernel is the even space of the partner height, so no ten-kernel partner
lies outside that space. On partner pairs `(1, 2)`, `(2, 1)`, and
`(1, 3)` that space is spanned by the sign product, the oblique dot
minus the parallel dot, and the orthogonal cross minus half the swapped
cross. On pairs `(3, 1)`, `(2, 3)`, and `(3, 2)` it is spanned by the
sign product, the swapped cross, and the parallel dot plus the oblique
dot. The parallel-oblique sum lies in the odd space at heights 1 and 2
and outside the chirality and transverse-sign plane. At those heights
the bond on `-e_x` and `-e_y` against the sign product has centre pairs
`(-1, -1)` and `(1, -1)` and kernel cross sum 0. Against the chirality
cap the centre pairs are `(-1, -1)` and `(1, 1)` and the kernel cross
sum is `2`. Against the matched cross the centre pairs are `(-1, 0)`
and `(1, 1)` and the kernel cross sum is `1`. The coefficient tuples
`(1, 0, 0, 0)`, `(0, 0, 0, 1)`, and `(1, 1, 1, 1)` have partner rank 7.
A vector with both an odd part and an even part is not in this count.
The ten-kernel coefficient span is not classified. Runner
`PASS=9 FAIL=0`.

Cycle 42. On the same alphabet a parity vector with both an odd part and
an even part has partner rank 10, so the only ten-kernel partner is 0.
The orthogonal cross lies in the parity span and in neither summand. At
heights 1 and 2 it is half the swapped cross plus the even generator
with swapped coefficient `-1/2` and orthogonal coefficient `1`. The sum
of the chirality cap and the sign product is another mixed vector and
also has partner rank 10. At heights 1 and 2 the bond on `-e_x` and
`-e_y` against the sign product has centre pairs `(0, -1)` and
`(-1, -1)` and kernel cross sum `1`. Against the chirality cap the
centre pairs are `(0, -1)` and `(-1, 1)` and the kernel cross sum is
`-1`. Against the matched cross the centre pairs are `(0, 0)` and
`(-1, 1)` and the kernel cross sum is `-1`. A vector with a nonzero
excluded coefficient is not in this count. The ten-kernel coefficient
span is not classified. Runner `PASS=8 FAIL=0`.

Cycle 43. On the same alphabet the two ratio spans meet only at 0, so
their sum is 6-dimensional. The swapped transverse dot sits only on the
swapped-orthogonal generator, with opposite signs, and the scaled
cross-dot kernel sits only on the cap generator, with coefficient 2 on
both spans. A nonzero vector in the sum has a nonzero ten-kernel partner
if and only if it lies in exactly one span. The partner is that span on height pairs
`(1, 2)`, `(2, 1)`, `(2, 3)`, and `(3, 2)`, and the other span on
`(1, 3)` and `(3, 1)`. A vector with a nonzero part in each span has
partner rank 10. The chirality cap lies outside the sum, and adding it to a nonzero
sum vector still has partner rank 10. At heights 1 and 2 the bond on
`-e_x` and `-e_y` has lefts `(-1, -2, -3)` and `(-1, -2, 3)`. The
swapped-orthogonal generator plus the opposite oblique-matched
generator, against the first oblique-matched generator, has rights
`(1, -2, -3)` and `(-1, 2, -3)`, centre pairs `(0, 0)` and `(2, 2)`,
and kernel cross sum `4`. The chirality cap plus the swapped-orthogonal
generator, against the sign product, has rights `(1, -3, -2)` and
`(-1, 2, -3)`, centre pairs `(-1, -1)` and `(-1, -1)`, and kernel cross
sum `2`. A vector outside the span of the chirality cap and the two
ratio spans is not in this count. The ten-kernel coefficient span is
not classified. Runner `PASS=8 FAIL=0`.

Cycle 44. On the same alphabet the even space, the chirality cap, and
one ratio span form a 7-dimensional sum. The seven-generator map has
rank 46 and nullity 24. The kernel is the product of the odd space on
the even blocks, the even space on the chirality block, and the partner
ratio span on the span blocks. Those three spaces meet pairwise only at
0, so a nonzero vector has a nonzero ten-kernel partner exactly on one
summand. A nonzero swapped-dot or scaled coefficient has such a partner
exactly when the vector lies in the ratio span. At heights 1 and 2 the
bond on `-e_x` and `-e_y` has lefts `(-1, -2, -3)` and `(-1, -2, 3)`.
The sign product plus the swapped-orthogonal generator, against that
generator, has rights `(1, -2, -3)` and `(3, 2, -1)`, centre pairs
`(-1, 0)` and `(-1, 2)`, and kernel cross sum `-2`. The sign product
plus the cap generator, against that generator, has rights `(1, -3, -2)`
and `(-3, 2, 1)`, centre pairs `(-3, 0)` and `(1, -4)`, and kernel cross
sum `-4`. A vector that meets the other ratio span is not in this count.
The ten-kernel coefficient span is not classified. Runner
`PASS=7 FAIL=0`.

Cycle 45. On the same alphabet the even space and both ratio spans form
a 9-dimensional sum, and the chirality cap lies outside it. The
nine-generator map has rank 42 and nullity 48. The projection of that
kernel onto the three even blocks has rank 30. The sign product plus
both cap generators has scaled coefficient 4 and partner rank 10. The
sign product plus one cap generator minus one third of the other has
scaled coefficient `4/3`, swapped-dot coefficient 0, and partner rank
7. That partner kernel is 3-dimensional and depends on the ordered
height pair. The sign product plus one swapped-orthogonal generator and
the opposite oblique-matched generator has swapped-dot coefficient 1
and partner rank 10. At heights 1 and 2 the bond on `-e_x` and `-e_y`
has lefts `(-1, -2, -3)` and `(-1, -2, 3)`. The swapped-dot vector,
against the first oblique-matched generator, has rights `(1, -3, -2)`
and `(-1, 2, -3)`, centre pairs `(-1, 0)` and `(1, 2)`, and kernel
cross sum `2`. The scaled coefficient 4 vector, against that cap
generator, has rights `(1, -3, -2)` and `(-3, 2, 1)`, centre pairs
`(-3, 0)` and `(1, -4)`, and kernel cross sum `-4`. Each listed partner
of the coefficient `4/3` vector has cross sum 0 on those directions. A
nonzero chirality coefficient is not in this count. The ten-kernel
coefficient span is not classified. Runner `PASS=9 FAIL=0`.

Cycle 46. On the same alphabet the even space, both ratio spans, and
the chirality cap form a 10-dimensional sum. The ten-generator map has
rank 49 and nullity 51. The chirality cap alone has partner rank 7.
The sign product plus one cap generator minus one third of the other
has scaled coefficient `4/3` and partner rank 7, and the chirality
block meets that partner only at 0, so every nonzero chirality
coefficient removes those partners. With chirality coefficient 1, that
vector, the sign product plus both cap generators, and the swapped-dot
coefficient 1 vector each have partner rank 10. At heights 1 and 2 the
bond on `-e_x` and `-e_y` has lefts `(-1, -2, -3)` and `(-1, -2, 3)`.
Against the three listed partners, the coefficient `4/3` vector plus
the chirality cap has cross sums `-6/5`, `-1/4`, and `1/2`. A chirality
coefficient other than 1 is not given a full partner rank. The
ten-kernel coefficient span is not classified. Runner `PASS=11 FAIL=0`.

Cycle 47. On the same alphabet the sign product plus one cap generator
minus one third of the other has scaled coefficient `4/3`. Chirality
coefficient 0 has partner rank 7. The coefficient pairs of that vector
and the chirality cap compress to 14 rows, and a running gcd of the
10-by-10 minors is a nonzero multiple of the cube of the chirality
coefficient. Every nonzero chirality coefficient therefore has partner
rank 10. At heights 1 and 2, chirality coefficient 1 has cross sums
`-6/5`, `-1/4`, and `1/2` against the three partners of coefficient 0.
The scaled coefficient 4 vector is not in this all-scale count. The
ten-kernel coefficient span is not classified. Runner `PASS=12 FAIL=0`.

Cycle 48. On the same alphabet the sign product plus both cap generators
has scaled coefficient 4. The coefficient pairs of that vector and the
chirality cap compress to 17 rows, and a running gcd of the 10-by-10
minors is a nonzero constant. Every chirality coefficient therefore has
partner rank 10. The swapped-dot vector is not in this all-scale count.
The ten-kernel coefficient span is not classified. Runner
`PASS=13 FAIL=0`.

Cycle 49. On the same alphabet the sign product plus the swapped-dot
cap generator and the matched cap generator has swapped-dot coefficient
1. The coefficient pairs of that vector and the chirality cap compress to 17
rows. Gaussian elimination at chirality coefficients `0`, `1`, `1/3`,
and `-1` selects ten pivot rows, and the running gcd of those maximal
minors is a nonzero constant. Every chirality coefficient therefore has
partner rank 10. A vector with both a nonzero swapped-dot coordinate
and a nonzero scaled coordinate is not in this all-scale count. The
ten-kernel coefficient span is not classified. Runner
`PASS=14 FAIL=0`.

Cycle 50. On the ordered height pairs `(1, 3)`, `(2, 3)`, and `(3, 2)`,
the second even generator plus both swapped-dot generators has swapped
coordinate `-1` and orthogonal coordinate `2`. The base image has rank
7 and contains every chirality row. The projected 7-by-7 pivot minors
at chirality coefficients `0` and `-1` have a nonzero constant running
gcd, so every chirality coefficient has partner rank 7. A nonzero
chirality coefficient on a vector that meets both spans and has a
nonzero even part need not have partner rank 10. The same coefficients
on the source-same height pairs are not in this rank-7 count. The
ten-kernel coefficient span is not classified. Runner
`PASS=15 FAIL=0`.

Cycle 51. On the source-same ordered height pairs `(1, 2)`, `(2, 1)`,
and `(3, 1)`, the second even generator plus both swapped-dot generators
has swapped coordinate `-2`, parallel coordinate `-1`, oblique
coordinate `1`, and orthogonal coordinate `2`. The base image has rank
10, so chirality coefficient 0 already has partner rank 10. The
coefficient pairs compress to 17 rows. The monic pivot minor at
chirality coefficient 1 is `(c - 2)^2`, and the monic pivot minor at
coefficient 2 is `c^3(c - 1)`. Their gcd is a nonzero constant, so
every chirality coefficient has partner rank 10. The sign product plus
both swapped-dot generators is not in this count. The ten-kernel
coefficient span is not classified. Runner `PASS=16 FAIL=0`.

Cycle 52. On every ordered height pair, the sign product plus both
swapped-dot generators has sign-product coordinate `1`, swapped
coordinate `-2`, and orthogonal coordinate `2`. The base image has rank
10, so chirality coefficient 0 already has partner rank 10. The
coefficient pairs compress to 17 rows. The pivot minors at chirality
coefficients `0`, `1`, `-1`, and `-1/3` have a nonzero constant running
gcd, so every chirality coefficient has partner rank 10. On the
source-same pairs the monic pivot minor at coefficient 0 is
`(c - 1)^7`. The third even generator plus both swapped-dot generators
is not in this count. The ten-kernel coefficient span is not classified.
Runner `PASS=17 FAIL=0`.

Cycle 53. On every ordered height pair, the third even-dot family is the
third even generator plus both swapped-dot generators. On the
source-same pairs the summed vector has swapped coordinate `-5/2` and
orthogonal coordinate `3`. On `(1, 3)`, `(2, 3)`, and `(3, 2)` it has
swapped coordinate `-2`, parallel coordinate `1`, oblique coordinate
`1`, and orthogonal coordinate `2`. The base image has rank 10. The
coefficient pairs compress to 17 rows. The pivot minors at chirality
coefficients `0`, `1`, `-1`, `-1/2`, and `5/2` have a nonzero constant
running gcd, so every chirality coefficient has partner rank 10. A sum
of two even generators is not in this count. The ten-kernel coefficient
span is not classified. Runner `PASS=18 FAIL=0`.

Cycle 54. On every ordered height pair, the second-plus-third even-dot
sum is the second even generator plus the third even generator plus
both swapped-dot generators. On the source-same pairs the summed vector
has swapped coordinate `-5/2`, parallel coordinate `-1`, oblique
coordinate `1`, and orthogonal coordinate `3`. On `(1, 3)`, `(2, 3)`,
and `(3, 2)` it has swapped coordinate `-1`, parallel coordinate `1`,
oblique coordinate `1`, and orthogonal coordinate `2`. The base image
has rank 10. The coefficient pairs compress to 17 rows. The pivot
minors at chirality coefficients `0`, `1`, `-1`, `-1/2`, and `5/2` have
a nonzero constant running gcd, so every chirality coefficient has
partner rank 10. The sum of the first and second even generators is not
in this count. The ten-kernel coefficient span is not classified.
Runner `PASS=19 FAIL=0`.

Cycle 55. On every ordered height pair, the first-plus-second even-dot
sum is the sign product plus the second even generator plus both
swapped-dot generators. On the source-same pairs the summed vector has
sign-product coordinate `1`, swapped coordinate `-2`, parallel
coordinate `-1`, oblique coordinate `1`, and orthogonal coordinate `2`.
On `(1, 3)`, `(2, 3)`, and `(3, 2)` it has sign-product coordinate `1`,
swapped coordinate `-1`, and orthogonal coordinate `2`. The base image
has rank 10. The coefficient pairs compress to 17 rows. The pivot
minors at chirality coefficients `0`, `1`, `-1`, `-1/2`, and `5/2` have
a nonzero constant running gcd, so every chirality coefficient has
partner rank 10. The sum of the first and third even generators is not
in this count. The ten-kernel coefficient span is not classified.
Runner `PASS=20 FAIL=0`.

Cycle 56. On every ordered height pair, the first-and-third even-dot
family is the first and third even generators plus both swapped-dot
generators, with the second even generator omitted or included. On the
source-same pairs the omitted sum has sign-product coordinate `1`,
swapped coordinate `-5/2`, and orthogonal coordinate `3`, and the
included sum also has parallel coordinate `-1` and oblique coordinate
`1`. On `(1, 3)`, `(2, 3)`, and `(3, 2)` the omitted sum has
sign-product coordinate `1`, swapped coordinate `-2`, parallel
coordinate `1`, oblique coordinate `1`, and orthogonal coordinate `2`,
and the included sum has swapped coordinate `-1`. Each base image has
rank 10. The coefficient pairs compress to 17 rows. The pivot minors
at chirality coefficients `0`, `1`, `-1`, `-1/2`, `1/2`, `3/2`, `5/2`,
`2`, `-2`, and `-2/3` have a nonzero constant running gcd, so every
chirality coefficient has partner rank 10. The five coefficients `0`,
`1`, `-1`, `-1/2`, and `5/2` are not this certificate. A vector with
both a nonzero swapped-dot coordinate and a nonzero scaled coordinate
is not in this count. The ten-kernel coefficient span is not
classified. Runner `PASS=21 FAIL=0`.

Cycle 57. On every ordered height pair, both swapped-dot generators
plus the cap generator of either ratio span have partner rank 10 at
every chirality coefficient. The swapped-dot coordinates cancel, so
each sum has swapped-dot coordinate `0` and scaled coordinate `2`. The
plus cap also has transverse-sign coordinate `-1`, sign-product
coordinate `-1`, matched coordinate `2`, swapped coordinate `-2`, and
orthogonal coordinate `2`. The minus cap has transverse-sign coordinate
`1` and sign-product coordinate `1`. Neither vector lies in the even
space or in either ratio span. The base image has rank 10. The
coefficient pairs compress to 17 rows, and the gcd of the 10-by-10
minors is a nonzero constant. The pivot minors at `0`, `1`, `-1`,
`-1/2`, `1/2`, `3/2`, `5/2`, `2`, `-2`, and `-2/3` do not have a
constant gcd. At heights 1 and 2 the bond on `-e_x` and `-e_y` against
the chirality cap has kernel cross sums `-6` and `-2`. A vector with
both a nonzero swapped-dot coordinate and a nonzero scaled coordinate
is not in this count. The ten-kernel coefficient span is not
classified. Runner `PASS=9 FAIL=0`.

Cycle 58. On every ordered height pair, one swapped-dot generator plus
the cap generator of one ratio span splits by span. The same-span sum
lies in that span. It has swapped-dot coordinate `1` or `-1` and scaled
coordinate `2`. Chirality coefficient 0 has partner rank 7. The partner
kernel is that span on pairs `(1, 2)`, `(2, 1)`, `(2, 3)`, and
`(3, 2)`, and the other span on `(1, 3)` and `(3, 1)`. The 14-row
pencil has maximal-minor gcd equal to a nonzero multiple of the cube
of the chirality coefficient, so every nonzero coefficient has partner
rank 10. The opposite-span sum lies in neither span. Its 17-row pencil
has a nonzero constant maximal-minor gcd, so every chirality
coefficient has partner rank 10. At heights 1 and 2 the same-span
witness cross sums are `-2` and `2`, and the opposite-span witness
cross sums are `-2` and `-4`. The sum of one swapped-dot generator and
both cap generators is not in this count. The ten-kernel coefficient
span is not classified. Runner `PASS=9 FAIL=0`.

Cycle 59. On every ordered height pair, one swapped-dot generator plus
both cap generators has partner rank 10 at every chirality coefficient.
The plus-dot sum has swapped-dot coordinate `1` and scaled coordinate
`4`. The minus-dot sum has swapped-dot coordinate `-1` and the same
scaled coordinate. Transverse-sign and sign-product coordinates are
`0`. Neither sum lies in the even space or in either ratio span. The
two sums are linearly independent. Each base image has rank 10. The
coefficient pairs compress to 17 rows, and the gcd of the 10-by-10
minors is a nonzero constant. The pivot minors at `0`, `1`, `-1`,
`-1/2`, `1/2`, `3/2`, `5/2`, `2`, `-2`, and `-2/3` do not have a
constant gcd. At heights 1 and 2 the bond on `-e_x` and `-e_y` against
the chirality cap has kernel cross sums `-6` and `-4`. The sum of both
swapped-dot generators and both cap generators is not in this count.
The ten-kernel coefficient span is not classified. Runner
`PASS=9 FAIL=0`.

Cycle 60. On every ordered height pair, both swapped-dot generators
plus both cap generators have partner rank 10 at every chirality
coefficient. The swapped-dot coordinates cancel, so the sum has
swapped-dot coordinate `0`, matched coordinate `4`, swapped coordinate
`-2`, orthogonal coordinate `2`, and scaled coordinate `4`. It lies
outside the even space and outside both ratio spans. The base image has
rank 10. The coefficient pairs compress to 17 rows, and the gcd of the
10-by-10 minors is a nonzero constant. The pivot minors at `0`, `1`,
`-1`, `-1/2`, `1/2`, `3/2`, `5/2`, `2`, `-2`, and `-2/3` do not have a
constant gcd. At heights 1 and 2 the bond on `-e_x` and `-e_y` against
the chirality cap has kernel cross sum `-6`. One swapped-dot generator
plus twice the cap of the same span is not in this count. The
ten-kernel coefficient span is not classified. Runner `PASS=6 FAIL=0`.

## Next exact action

Decide whether every chirality coefficient on the sum of one
swapped-dot generator and twice the cap of the same ratio span has
partner rank 10. That sum lies in the span and has swapped-dot
coordinate 1 or -1 and scaled coordinate 4. Both swapped-dot generators
plus both cap generators have swapped-dot coordinate 0, scaled
coordinate 4, and partner rank 10 at every chirality coefficient. Do
not claim the ten-kernel coefficient span is settled. Do not claim the
300-dimensional affine space is classified.
Do not repeat the bond-space dimension count. Do not return to the
modulus-3 triple. Do not invent a formation rate. Do not return to
shells, plaquette corner weights, or the `(0,1,2)` and `(1,1,2)`
alphabets.

## Cleanup

Keep this one worktree. Delete `docs/audit/data/citation_graph.json` after
each manifest refresh. Remove the worktree only when the session can no
longer continue or free disk falls below 10Gi.
