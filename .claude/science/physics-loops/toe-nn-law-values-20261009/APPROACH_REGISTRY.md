# Approach registry

Family A: simultaneous conjugation covariance of one pair's Pauli coefficients
under the proper cubic group and under one bond's stabilizer.

Target contract: exact rational nullspace dimensions and bases; positivity
interval of the isotropic line; location of CHSH square 8.

Terminal status of Family A for cycle 1: the contract is proved under the
density hypothesis. The missing lemma for a physical identification is the
removal of that hypothesis.

Family B: product-class orbit weights on the six signed axes, one edge, local
readouts, no density.

Target contract: exact CHSH squares of that pair law, compared with 4 and 8.

Terminal status of Family B for cycle 2: proved. Coordinate square
`8 lambda^2 ≤ 8/9`. Global-sign square equals 4 only on the named boundary.
No local `[-1,1]` readout has square 8. The directed six-parameter maximum
is a different family and is not implied by Family B.

Family C: singular values of the directed correlation matrix, together with
the four eigenvalues of the declared density pattern.

Target contract: the exact elementary CHSH square on that positive pattern,
and the signed-axis square as a separate finite comparison.

Terminal status of Family C for cycle 3: proved under the density hypothesis.
The elementary square is at most `8`, with equality exactly on the circle
`p = q = 0`, `v = -1`, `u^2 + t^2 = 1`. Signed-axis square `8` holds at the
four diagonal points of that circle and fails at the singlet, where the
magnitude is at most `2`. Removing the density hypothesis is not implied.

Family D: partial traces of the directed density, and the linear coefficient
of `t` in a coordinate weight matrix.

Target contract: exact wing reductions; the condition `W_xy = W_yx` for
blindness to `t`; the value `2t` of one antisymmetric weight; the action of
`diag(1,-1,1)` on `T`. No CHSH square.

Terminal status of Family D for cycle 4: proved under the density hypothesis
and a supplied readout convention. Local projective weights miss `t`.
Symmetric weights miss `t`. The named antisymmetric weight equals `2t`.
`P` flips the sign and is not a proper rotation. Selecting that sign is
not implied.

Quadratic-channel family: degree-2 polynomials on one real `3×3` matrix,
invariant under signed permutations.

Target contract: the exact dimension and a basis; the effect of one
rational rotation on the two middle squares; the directed substitution,
including the sign of `t`. No CHSH square and no readout weight.

Terminal status for cycle 5: proved under the matrix hypothesis. The
invariant space has dimension `4` for both the proper group and the full
signed-permutation group. The directed restriction is even in `t` and
misses the symmetric-off-diagonal coefficient. Selecting the four ratios
is not implied.

Family F: soldered product factors on a record-value orbit that is not the
bond correlation and not the chiral pair of `(1, 2, 3)`.

Target contract: whether the proper orbit of `(0, 1, 2)` splits under
mirrors; whether the transverse-sign factor has support; one explicit
normalised product and its path correlation at a supplied `kappa`.

Terminal status for cycle 6: proved under the product hypothesis. The
orbit is achiral of size `24`. The transverse-sign factor is identically
`0`. The axis-role product is mirror-fixed, and the path correlation is
`1/72` at `kappa = 1/2`. Selecting `kappa` is not implied. Other 24-point
orbits and higher-rank bond spaces are not implied.

Family G: partial-neighbour expansion of one bond factor `1 + kappa F`,
and the quarter-turn sectors of the rank-1 products on the orbit of
`(0, 1, 2)`.

Target contract: whether soldered covariance forces a nonzero `kappa`, or
whether every normalised product of this shape leaves `kappa` free. No
path mass and no CHSH square.

Terminal status for cycle 7: proved under the product hypothesis.
Covariance does not contain `kappa`. Normalisation at one nonzero value
holds for every value, or only at `0`. Both branches occur on this orbit.
Selecting `kappa` is not implied. A second power `kappa^2 G` is not
implied.

Family H: quadratic pencils in the span of the two odd cap lines on the
orbit of `(0, 1, 2)`, coefficients in `{-2,-1,0,1,2}`.

Target contract: whether partial normalisation isolates a unique nonzero
`t` for an independent pencil, or whether `t = 0` always remains. No path
mass and no CHSH square.

Terminal status for cycle 8: proved under the product hypothesis. Every
independent pencil normalises at `0`. The counts are `32` only at `0`,
`256` at two rationals, and `208` at three. The balance pencil is exactly
`{0, 1/2}`, both strictly positive. Selecting `t` is not implied. A factor
that is not `1` at the parameter origin is Family I, not a corollary.

Family I: one shifted bond factor on the same two odd cap lines,
`1 + (1 - 2 t) X + (t^2 - t + 1) Y`, whose value at `t = 0` is not the
constant `1`.

Target contract: whether this one soldered factor has a unique nonzero
partial-normalisation value. No path mass, no CHSH square, and no
coefficient census.

Terminal status for cycle 9: proved under the product hypothesis. The
unique real normalisation value is `t = 1/2`. There the factor is
`1 + (3/4) Y`, and the bond values are strictly positive. The root is the
root of the supplied polynomial `1 - 2 t`. Selecting `t` is not implied.
The odd cap alphabet stops. Another pencil is not implied.

Family J: fully recorded binary colorings of the six axis directions,
with two supplied actions on the locked output.

Target contract: the shell orbits; the stabilizer orbits on the six
directions; whether any shell forces one locked possibility. No bond
factor and no `3×3` correlation.

Terminal status for cycle 10: proved under those two actions. There are
10 shell orbits. The constant shells force the uniform law of mass `1/6`
under the soldered action, and no shell forces one direction. Under the
unsoldered action, `511` varying laws lock each label at each shell.
Selecting either action, or the uniform law, is not implied. A blank
neighbor is not implied.

Family K: shells with exactly one blank axis direction and the other five
entries in `{0,1}`, under the soldered six-direction action.

Target contract: the shell orbits; whether the blank slot is a singleton
output orbit; whether any shell forces one locked direction; whether
every covariant conditional has support larger than one point. No bond
factor and no unsoldered label.

Terminal status for cycle 11: proved under that action. There are 12
shell orbits. The blank and its antipode are singleton output orbits on
every shell. No shell forces one direction. Support size 1 occurs, and
neither point mass is selected. Two or more blanks are not implied.

Family L: every coloring of the six axis directions by `{0, 1, blank}`,
under the soldered six-direction action.

Target contract: which shells have output type `(1,)`, and which have a
unique invariant probability on the six directions. Name them if any
exist. No bond factor, no deleted-blank menu, and no unsoldered label.

Terminal status for cycle 12: proved under that action. There are 729
shells. No shell has output type `(1,)`. The unique invariant laws are
the uniform law of mass `1/6` on `000000`, `111111`, and `bbbbbb`. No
shell forces one direction. Neither the uniform law nor either five-blank
point mass is selected. A menu that deletes blanks is not implied.

Family M: the 81 colorings of one unit square by `{0, 1, blank}`, and the
integer assignments that transform by the boundary sign of a
corner-preserving proper isometry.

Target contract: decide whether that covariance forces a unique nonzero
circulation, or whether every covariant assignment has circulation 0 or a
free sign. Name the free orbits if the module is larger. No edge flux, no
deleted-blank menu, and no six-direction shell.

Terminal status for cycle 13: proved under that character. There are 81
colorings and 21 orbits. The covariant module is free of rank 3, with
free orbits `001b`, `011b`, and `01bb`. Zero is covariant. The three
coefficients are independent, so the circulation is not unique and not
unique up to one sign. The other 57 colorings are forced to 0. No
coefficient is selected. A menu that deletes blanks is not implied.

Family N: one alternating sum of the four corner values, with blank
counted as `0`, tested against the boundary-sign character of Family M.

Target contract: decide whether that one assignment is covariant, and if
so name its three integer coefficients on `001b`, `011b`, and `01bb`. If
not, name one isometry and one coloring. Do not adopt the sum as a flux.

Terminal status for cycle 14: proved under that character and that numeric
map. The assignment is not covariant. The witness is the half-turn
`(x, y, z) ↦ (y, x, -z)` and the coloring `0101`, where the sum is `-2`
rather than `+2`. No coefficient triple is assigned. The sum is not a
flux. Other weight vectors are not implied.

Family O: integer weights `(w0, w1, w2, w3)` on the four corners, with
blank counted as `0`, tested against the boundary-sign character of
Family M.

Target contract: find every such weight for which the weighted corner sum
is covariant. Give a `Z`-basis of the solution module, or prove that the
only solution is `0`. Do not adopt a surviving weight as a flux.

Terminal status for cycle 15: proved under that character and that numeric
map. The relation lattice is the even-sum sublattice of `Z^4`, of index
`2`, generated by four rows of determinant `-2`. Exact division of the
pivot `2` returns only `(0,0,0,0)`. A basis is empty. The zero weight is
not a flux. A separate integer for blank is not implied.
