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

## Next exact action

Decide whether a nonzero coefficient on the matched cross, the swapped
transverse dot, or the scaled cross-dot kernel can pair with a nonzero
vector at the other height and still have every cross moment equal to
0. The parity span is settled. Do not claim the ten-kernel coefficient
span is settled. Do not claim the 300-dimensional affine space is
classified. Do not repeat the bond-space dimension count. Do not
return to the modulus-3 triple. Do not invent a formation rate. Do not
return to shells, plaquette corner weights, or the `(0,1,2)` and
`(1,1,2)` alphabets.

## Cleanup

Keep this one worktree. Delete `docs/audit/data/citation_graph.json` after
each manifest refresh. Remove the worktree only when the session can no
longer continue or free disk falls below 10Gi.
