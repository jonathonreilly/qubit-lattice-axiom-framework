<!-- Original PR9813 source SHA256 54a3fd4b9ac0a5d1fcef603338e39dcdd24779dc3b8e75ef06bbff4f97d2e9a2. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent order-eight Q8 invariant reduction

Disposition: PASS for the invariant classification and the reported relative coefficients, conditional on the independently checked touching-square connected coefficient supplied in this task. I have not recomputed that latter high-order coefficient here. This is an order-eight diagonal coefficient statement, not an all-orders state or pole theorem.

## Exhaustion by layerwise edge parity

For L=10 and eight transverse insertions, a diagonal N0 process cannot flip an entire column. In each longitudinal layer, therefore, every transverse vertex has even degree in the insertion multigraph. Reduce edge multiplicities modulo two. The resulting simple edge set is Eulerian. At total insertion count at most eight its nonempty components can only be:

1. A square (four edges), with up to four extra insertions in even multiplicities.
2. A six-edge rectangle, with two extra insertions.
3. A simple eight-edge polygon.
4. Two squares, possibly sharing vertices/edges before the mod-two reduction, in one or different longitudinal layers.

There is no two-edge simple cycle. An eight-edge Eulerian graph with a degree-four vertex decomposes into two squares; it is not a missing new primitive polygon. A connected simple eight-edge polygon bounds exactly a straight triomino, an L triomino, or a 2 by 2 box (up to translations/rotations/reflections).

At a vertex, the final background Z exponent is determined by the parities of its X and Y insertions. Adding a repeated edge twice cannot alter this exponent. Thus repeated-edge decorations of a four-cycle give only its single P operator; decorations of a six-cycle give only nearest-neighbor PP. A word with empty odd-edge set gives only a scalar. Phases and denominators affect coefficients, not these operator identities.

For two squares the operator is their P product. Equal squares give a scalar; edge-adjacent squares give nearest-neighbor PP; vertex-adjacent squares give diagonal PP. Squares with disjoint sets of columns have no connected contribution: the chosen product background and H0 factor over those columns, so the disconnected energy cumulant, including its folded terms, vanishes. Two squares sharing a column at distinct longitudinal layers can be connected through the vertical energy only at equal or neighboring layers (including the periodic neighbor); at greater separation the flip costs and perturbation variables factor. This accounts for the same-layer and adjacent-layer terms in the supplied diagonal-PP coefficient.

Folded terms do not evade this list. At order eight they multiply lower-order scalar, P, or nearest-PP contributions, with the potentially new P times P case arising from two order-four squares. The connected/disconnected distinction just described still applies after the folds are included. In particular one cannot retain disconnected P_p P_q terms at arbitrary separation merely because they appear in an individual normalization term.

These arguments require a nonaliased transverse box and a longitudinal period large enough to keep the local-layer classification valid; L=10 satisfies the order-eight longitudinal requirement. They classify the diagonal N0 coefficient. They do not claim the same classification once enough insertions can reverse complete columns.

## Primitive and connected coefficients

The primitive simple-loop result gives:

* straight three-plaquette product: coefficient -c;
* 2 by 2 box product: coefficient -c;
* each of the four L-triomino products: coefficient +h;

with c=9/262144 and h=5/262144 per longitudinal layer. The opposite sign of the six-turn L loop is essential.

The supplied fully connected touching-square calculation gives

    k = 3/65536 - 2*(127/10616832) = 29/1327104

for each diagonal-PP orientation per layer. This is not obtainable from the primitive-loop law alone, and the reduction correctly keeps it as a separate coefficient.

Every remaining background-dependent term is single P or nearest-neighbor PP, or a scalar. Isotropy and square symmetry make their directional coefficients equal. At fixed bad count Q and syndrome perimeter P_boundary,

    sum plaquette-sign = number_of_plaquettes - 2Q,
    sum unordered nearest-neighbor sign-products
        = number_of_neighbor_pairs - 2 P_boundary.

Thus these omitted terms are common on Q8/perimeter16. Fixing only Q8 without fixing perimeter would not permit this omission.

The complete distinguishing part is consequently

    L J lambda^8 [ -c (sum straight3 + sum box4)
                    + h sum four L-triomino orientations
                    + k sum two diagonal-PP orientations ].

## Relative shape energies

I replayed `/tmp/neutral_q8_invariants.py` and checked the conversion from odd-product counts to energy: an odd product changes a coefficient t contribution by -2t. Its total odd counts (straight plus box, L, diagonal) are:

    single: (12,24,12)
    axis separation 3: (20,48,24)
    diagonal separation (2,2): (22,44,22)
    specified four-column line: (28,48,24)
    specified T: (32,40,20).

Subtracting twice the single-column value therefore gives, in units L J lambda^8,

    axis3:  -9/32768,
    diag22: +545/5308416,
    line4:  +9/32768,
    T:      +683/663552.

The root's numbers and signs agree. Axis separation four gives zero in this distinguishing part, as the support argument predicts. The script's `single` row printed under `relative2single` is simply minus its own one-single reference and should not be read as a pair interaction.

The earlier positive primitive diagonal-separation contribution was not by itself a full native result; the connected diagonal-PP term changes that coefficient and is now correctly included. This does not conflict with the existing endpoint-trap arguments, but any new ordering or state selection must use this complete reduction rather than primitive loops alone.
