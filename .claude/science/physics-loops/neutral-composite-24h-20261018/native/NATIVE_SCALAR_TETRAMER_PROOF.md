# Native scalar-feature selfinteraction and a bound tetramer

Status: conditional-support; focused independent checks pass. The same L10
one-qubit Hamiltonian supports a four-column bound family below the threshold
of two separated Q4 neutral endpoint features. This is an excited native
bound band, not the lowest Q8 molecule, a fitted phi-four coupling, or an
empirically identified particle. No interaction has been added.

## Work backward from the derived neutral modes

The dilute scalar field proof intentionally suppresses contacts. Its next
missing physical ingredient is the interaction of two of those SAME modes.
A shortest neutral feature flips two adjacent columns and has four bad
plaquettes with perimeter twelve. Two distant features therefore have Q8
and perimeter twenty-four. Starting from their physical syndromes, rather
than choosing a contact potential, fixes the relevant degenerate manifold.

The global relative normal form and fixed-Q spatial bounds are inherited
from ISOTROPIC_BOUND_FEATURE_PROOF.md. The complete order-eight diagonal
invariant classification is inherited from INDEPENDENT_SECONDARY_ENERGY_CHECK.md,
not from its previously evaluated perimeter-sixteen minimum. All omitted
order-eight terms are scalar, single plaquette P, or nearest-neighbor PP;
they are constant on ANY fixed Q and perimeter. Thus their omission also
holds on Q8/perimeter24. The distinguishing energy per J L lambda^8 is

    -c (sum straight-three P products + sum four-P boxes)
    +h (sum four L-triomino products)
    +k (sum two diagonal PP products),
    c=9/262144, h=5/262144, k=29/1327104.

The k term includes connected touching-square folds. A primitive rectangle
ansatz alone would be insufficient. For an eight-site bad set S let n_A,
n_B,n_D count odd products of these three pattern families. Its energy
relative to the flat sign background, in units J L lambda^8/21233664, is

    F(S)=2[729 n_A-405 n_B-464 n_D].

For two distant shortest neutral features F=-23216. Since Q and perimeter
are matched, subtracting this reference is the full order-eight interaction
and shape difference, not an incomplete chosen pair potential.

## Exhaustive geometric reduction

Every occupied row and column of S has even degree. Eight cells therefore
occupy between two and four rows and between two and four columns. Enumerate
all binary incidence matrices with eight entries, no empty row/column and
even degrees. Perimeter24 is equivalent to exactly four adjacent occupied
pairs. The inverse finite column mask has even parity precisely when
sum_(x,y in S) x*y is even. This follows by summing the discrete double
antiderivative modulo two; translation terms vanish by even row/column sums.
It enforces the positive physical Z-plane sector.

The invariant shapes span at most two lattice units in either coordinate.
A consecutive occupied-coordinate gap is therefore detected only as 1, 2,
or at least 3. Retain far-gap parity separately: representatives 3 and 4
cover every larger odd/even gap. This gives a FINITE exhaustive reduction
of arbitrarily long finite configurations, not a bounded-box guess.
On a sufficiently large even torus, cut each coordinate at its largest
empty gap, which exceeds the invariant range because there are at most
four occupied coordinates. The same reduction then applies without wrap
interactions. The inverse-mask parity is unchanged by the even period.

The root enumeration checks 4912 allowed incidence/gap types. An independent
row-mask enumeration with alternative far representatives 5/6 and an
inclusion-exclusion energy computation reproduces the complete histogram.
The minimum relative value is -5832; the next value is -2916. Exactly four
oriented minima occur, up to translation:

    A_x: columns (0,0),(1,0),(4,0),(5,0),
    A_y: its ninety-degree rotation,
    B_x: columns (0,0),(1,0),(0,3),(1,3),
    B_y: its ninety-degree rotation.

All minimum gaps are finite; there is no hidden long-rod degeneracy at this
minimum. With v=9L/32768 this gives binding J v lambda^8 and gap to the
remaining perimeter24 shape manifold J(v/2)lambda^8, before higher orders.
There ARE extended configurations at the unbound threshold, so this result
does not license replacing the entire scalar collision problem by one
short-range contact channel.

## Microscopic band and the precise binding statement

At fixed Q8, other perimeter bands separate at order Jlambda^6. Other Q
sectors separate at order Jlambda^4, and walls at order J. On every fixed-Q
sector the retained coefficients have volume-independent norms and bounded
spatial moments. Finite-order reductions therefore isolate the four-minimum
subspace with absolute remainder C J R^2 lambda^M, after all denominator
losses. In a fixed momentum/plane fibre it has four states. Let its four
energies be E_a(q), measured above the actual global ground, and let
 epsilon_N(0) be the native single Q4 neutral lower-mode rest energy.
Uniformly in q,

    E_a(q) = 2 epsilon_N(0) - J v lambda^8 + O(Jlambda^10)
             + O(J R^2 lambda^M),    a=1,...,4.

Thus all four levels lie below the two-separated-neutral threshold by
Jv lambda^8[1+O(lambda^2)] in the joint limit. For R~lambda^-p choose
M>8+2p to resolve the leading gap. This is not a lowest-energy statement:
other Q8 molecular bands already lie lower by order Jlambda^6. They remain
separated rather than being silently discarded as nonexistent.

## Complete order-ten selection of the larger feature

The order-ten diagonal difference can be computed without supplying the
unknown renormalizations of earlier invariants. Their D4 orbit counts are
IDENTICAL on A and B: straight-three sum20, box16, L-triomino sum64,
diagonal PP sum32, and the already matched Q/perimeter. Every decoration
of a smaller cycle therefore cancels in B minus A.

Layerwise even-degree parity exhausts the new connected insertion graphs:
a simple ten-edge polygon; a six-cycle plus a four-cycle touching at a
vertex; or two squares connected by one twice-traversed edge. Other
coincident/shared-edge cases reduce to earlier invariants. A repeated-edge
decoration cannot change the background Pauli word. Disconnected folded
terms cancel in the connected energy coefficient, as in the inherited
order-ten pair calculation. The new doubled-bridge PP offsets are (2,0)
and (2,1); the former has equal A/B count and drops out.

The six simple-polygon families are the straight, L, T and skew tetrominoes,
the five-cell P shape, and the six-cell rectangle. The primitive-loop law
and their complete translated/rotated counts give B-A=199/2097152.
The two remaining distinguishing operators have:

| operator orbit | A odd count | B odd count | coefficient per longitudinal layer |
| --- | ---: | ---: | --- |
| diagonal-offset PP at (2,1) | 52 | 56 | -75101/97844723712 |
| skew triple {(0,0),(1,0),(2,1)} | 136 | 144 | 331/226492416 |

These are the independently checked dumbbell and touching-six-plus-four
coefficients from NATIVE_PAIR_SCATTERING_PROOF.md, including folds and
longitudinal placements. They are reused as operator coefficients, not
refitted to the new feature. Consequently

    (E_B-E_A)/(J L lambda^10)
       =199/2097152-16*(331/226492416)+8*(75101/97844723712)
       =949685/12230590464 > 0,

up to relative O(lambda^2). No single winding edge connects any two
translated/oriented minima: their column masks never differ by just an
adjacent pair. Thus there is no off-diagonal order-ten term hidden in this
comparison. The collinear A family is selected before its later collective
motion. A naive second-order winding comparison at order twelve would have
missed this earlier selection.

At q=0 the two A orientations decompose into A1 and B1 symmetry fibres.
There is exactly one A1 state after eliminating the B family across the
order-ten gap. It therefore gives a native C4-even scalar pole within that
symmetry fibre, regardless of the unknown sign of the later A1/B1 splitting.
This does not prove that A1 is lower than B1. No tetramer mobility coefficient,
relativistic dispersion, decay rate or scalar scattering length is assigned.

## Physical readout of the band

For any of the four masks T define the physical operator
D_T=product_(columns r in T) product_z X_(r,z), and its R^-1 normalized
translated Fourier sum O_(q,T). These are products of original physical
spins, not new local qubits. At lambda=0 they create the corresponding unit
band vector. For q=0 subtract the exact ground expectation.

At first order, D_T anticommutes with exactly L n_Y(T) transverse YY bonds
and commutes with the XX and vertical ZZ bonds. Every such virtual pair has
unperturbed energy cost 8J. The difference of the two first-order dressed
states has coefficient 2(lambda/8)=lambda/4 per crossing YY bond. Their
orthogonal wall states give total lost low-band weight L n_Y lambda^2/16.
Internal shape admixtures start at lambda^2 in amplitude, hence affect the
TOTAL four-state band weight only at order lambda^4. The result is

    ||P_tet(q) O_(q,T) |g>||^2
       =1 - L n_Y(T) lambda^2/16 + O(lambda^4)
          + microscopic projector errors.

For the stated X-column sources n_Y=8 for A_x,B_x and n_Y=4 for their
rotations. This source anisotropy is physical; it is not averaged away by
calling the feature scalar. The bipartite lambda-sign symmetry excludes an
odd correction to this spectral weight for the even four-column masks.
For R~lambda^-p, a conservative amplitude projector error is
O(R^3 lambda^(M-8)); choose M>12+3p to put it below lambda^4.
For example p=2,M=30 suffices for the binding and this readout statement.
The formula is the summed band weight, not an assigned residue of its
uncomputed individual eigenvectors.

## Symmetry-covariant scalar source

The X-only sources above have different ultraviolet losses in different
orientations. A genuinely C4-even microscopic source must rotate the spin
axis together with the lattice. At q=0 take the normalized translated sum
of (D_(A_x)^X+D_(A_y)^Y)/sqrt(2), with the exact ground mean removed.
A quarter-turn sends X to Y and Y to -X; the forty-spin mask makes the
latter sign positive. Inside N0 both terms reduce to the respective
A-orientation unit vector. The source is A1 under the quarter-turn and
reflections, not just under a relabeling of its low-energy matrix.

Both terms have eight crossing bonds of the anticommuting transverse axis.
Their first-order wall outputs are mutually orthogonal. The UNIQUE A1
pole in the selected A family therefore has source weight

    1 - (L/2)lambda^2 + O(lambda^4).

Its physical projector error is controlled by the order-ten A/B gap,
not by an unproved A1/B1 gap: O(R^3 lambda^(M-10)) conservatively in
amplitude. M>14+3p places it below lambda^4; p2,M30 still suffices.
This is a deliberately specified physical multi-spin readout, not a
measurement-device derivation or a universal normalization of all sources.

## Assumption movement

The attraction between the already derived neutral features is supplied by
neither a phi-four coefficient nor a new mediator. The native order-eight
loops bind them into a larger forty-spin feature. The model now supplies a
concrete nonlinear composite structure in addition to a dilute free-field
limit. A general scalar selfinteraction, full collision channels, collective motion, microscopic units, preparation, geometry and connection
to observations remain open. All calculations are exposed model development.
