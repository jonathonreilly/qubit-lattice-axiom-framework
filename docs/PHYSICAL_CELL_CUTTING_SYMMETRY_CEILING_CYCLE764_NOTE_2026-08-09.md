# The cell symmetry caps the cover table's rank at 144 and floors its blind space at 48 — Cycle 764

Date: 2026-08-09

Authority: none

Audit: unset.

Status: derived ceiling and floor with a measured, unaccounted residual

Claim type: bounded_theorem

Runner:

- [`physical_cell_cutting_symmetry_ceiling_cycle764_2026_08_09.py`](../scripts/physical_cell_cutting_symmetry_ceiling_cycle764_2026_08_09.py)

Axioms:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## What this responds to

Cycle 763 asked whether the cell's own symmetry picks out the cover table's rank
of 105, and answered no: tables built to be covariant under that symmetry run
over a wide band and 105 sits low in it. But the band itself was only sampled.
The largest dimension seen was 144 and the bound derived by hand fell short of
it, so nothing said whether 144 was the true ceiling or an artefact of sampling.

This cycle replaces the sample with a derivation. The symmetry alone fixes an
exact ceiling on the rank of any covariant table, an exact floor on its blind
space, and the ceiling is shown to be attained.

## The object

The unit four-cube on sixteen corners, cut into least-volume pieces at the
adjacency-cost floor: 2672 candidate pieces of determinant one, 400 of them at
cost floor 6, 15800 cuttings of 24 pieces, 192 pieces actually used and 192
eight-piece covers.

The symmetry permutes the four coordinates and flips any of them: 384 maps,
closed over all 147456 products, acting transitively on the 192 pieces and on
the 192 covers. It has 104 orbits on ordered pairs of pieces, 120 on ordered
pairs of covers and 96 on the cells of the cover-by-piece square. By exact
rational arithmetic the cutting table has rank 88 with kernel 104, and the cover
table has rank 105 with kernel 87.

## Twenty parts

The algebra of maps commuting with the symmetry on the 192 piece directions has
dimension 104, one basis element per orbit on ordered pairs. Its centre is the
kernel of the 10816 conditions saying that a combination commutes with every
basis element. A modular selection of 84 independent rows caps that centre at
dimension 20, and the 20 integer vectors recovered are each verified against all
10816 conditions in both multiplication orders, which floors it at 20. So the
centre has dimension exactly 20.

One central element separates all twenty. Its matrix on the centre has 20
distinct integer eigenvalues, each of nullity one, found by an exact integer scan
over the interval its own row sums allow, bound 6009; three direct products on
the full 192 square confirm that this matrix really is multiplication by that
element. Its eigenspaces on the 192 piece directions are the twenty parts, of
dimensions

    1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 8, 8, 8, 8, 12, 12, 24, 24, 32, 32

Each part carries three integers: a degree d, a piece-side multiplicity m and a
cover-side multiplicity mc. Six sums certify the whole table at once:

    sum of dimensions      192
    sum of m squared       104
    sum of m times mc       96
    sum of mc squared      120
    sum of d times mc      192
    sum of blind            87

Each per-part entry is a modular rank, which can differ from the exact value in
one direction only. Each sum is pinned to a total computed independently and
exactly. Equality of the sums therefore forces every individual entry to be
exact. The third and fifth sums also tie the piece side and the cover side back
to the orbit counts 96 and 192, and the fourth to the 120 orbits on ordered pairs
of covers, so the decomposition is cross-checked against objects that were never
used to build it.

## The theorem

A table from covers to pieces that commutes with the symmetry acts on part i as
one mc by m matrix tensored with the identity on the degree. Its rank is
therefore the sum over parts of d times the rank of that small matrix, and its
blind space the sum of d times m minus that rank. A small matrix has at most
min(m, mc) independent rows, so for every covariant table

    rank  at most   sum of d times min(m, mc)      = 144
    blind at least  sum of d times max(0, m - mc)  =  48

The ceiling is attained. An explicit equivariant integer matrix built from all
96 cell orbits has exact rational rank 144, with no modulus anywhere. So 144 is
the true greatest available to any covariant table, not an upper estimate, and
48 is the true least blind space.

This turns a rank question on a 192 by 192 table into twenty rank questions on
matrices of size at most 6 by 4, and cycle 763's sampled largest of 144 becomes
a derived and attained value.

## What the cover table does with the room

The cover table's own rank is 105 and its blind space 87. Both lie strictly
inside the derived interval: 105 is 39 below the ceiling, and 87 is 39 above the
floor. That 39 is exactly what the symmetry does not account for.

Across the twenty parts, twelve sit exactly at the forced value and eight exceed
it. The eight, as degree / m / mc / blind / forced:

    2/2/2/2/0    4/2/3/4/0    6/2/3/6/0    8/4/6/8/0
    6/4/3/12/6   6/2/3/6/0    6/4/3/12/6   1/1/1/1/0

Their excesses are 2, 4, 6, 8, 6, 6, 6 and 1, summing to the whole 39, so the
other twelve parts contribute none of it.

Six of the eight have mc at least m and two do not. The natural reading — that
the cover side offers room the table declines to use — is therefore wrong as a
general statement: two of the eight have less cover-side room than piece-side
room and still lose rank beyond what that shortage forces.

## Three candidates for the 39, all refuted

The subgroup of even coordinate permutations has order 192 and index 2, and
splits both the 192 pieces and the 192 covers into two classes of 96 and 96. The
plus-minus label of that split is itself one of the twenty parts: the one with
degree, m and mc all equal to 1, whose row is 1/1/1/1/0 — blind, with nothing
forcing it to be.

That label is blind for a reason the runner exhibits rather than assumes. Every
one of the 192 covers splits its eight pieces 4 and 4 between the two classes, so
each cover sum of the label is 0. The same 4-and-4 split holds on the piece side,
each piece lying in four covers of each class, with incidence totals 768 and 768
both equal to 96 times 8. And the single non-identity element fixing a given
cover has permutation sign 1, fixes none of the eight blocks, has cycle type
2, 2, 2, 2 on them and keeps the class — so it cannot separate the label. On that
same element the flip-count parity is -1 and its product with the permutation
sign is -1, which forces both of those alternative labels blind as well: a label
on which a cover-fixing element acts by -1 must sum to zero over that cover.

A second candidate, the aggregate incidence, carries nothing by arithmetic alone.
For any split value a from 0 to 8, the count 96a + 96(8 - a) is 768, and 768 over
192 is 4. The mean number of class-0 pieces per cover is 4 whatever the structure
is, so it cannot be the explanation.

A third candidate is geometric. Two labels read off the pieces themselves — a
corner-parity label and an ordered determinant label — each agree with the class
label on 96 of 192 pieces, that is on exactly half, so neither reproduces it.
The determinant label is a genuine covariant object: with the image corners kept
in the source piece's own ordering, the determinant of the image equals the
determinant of the source times the product of the permutation sign and the
flip-count parity, on all 73728 element-piece pairs with 0 misses. Under the
other reading, where each image piece is re-sorted into its own order, the same
relation fails on 36864 of 73728 pairs, again exactly half, and survives for only
4 of the 384 elements. So the determinant tracks a character that the class label
does not, and the two are not the same object.

## Runner

`physical_cell_cutting_symmetry_ceiling_cycle764_2026_08_09.py`, 28 gates,
`TOTAL: PASS=28 FAIL=0`. Every gate number is an exact integer computation; no
floating point enters any gate.

Controls carried inside the run: 40 equivariance checks on the orbit matrices;
the cover table rebuilt entry by entry as the sum of 4 whole cell orbits; 7
products of orbit matrices recomputed directly and matched against the structure
constants; an integer overflow guard on those products; three products on the
full 192 square pinning the abstract central matrix to the concrete action; and
the exact rational rank of the witness, computed without any modulus.

## Boundary

Two identities in the runner hold by arithmetic whatever the part table says, and
are bookkeeping rather than evidence: that the ceiling plus the floor is 192, and
that the ceiling minus the rank equals the blind space minus the floor. Both
follow from d times min(m, mc) plus d times max(0, m - mc) being d times m. The
content sits beside them: the measured rank 105 is strictly below the ceiling 144
and the measured blind space 87 strictly above the floor 48, and the ceiling is
attained exactly.

Similarly, that every part with cover-side multiplicity 0 has no excess is
arithmetic — such a part is forced entirely into the blind space, so there is
nothing left to exceed. It is reported as a check that the cover table
annihilates those five parts, not as support for the theorem.

Every per-part quantity is a modular rank. The six sums are what make them exact,
and that is the only thing that does; a reader who does not accept the sums
should treat the part table as modular.

The weights inside the central element and inside the witness are arbitrary
deterministic choices carrying no meaning. Their only role is to be generic, and
each is gated by a wrong-value rejector — twenty distinct integer eigenvalues
each of nullity one, and an exact rational rank of exactly 144. A choice that
failed to be generic would fail its gate rather than pass quietly.

The 39 is not explained. Three candidate labels are refuted here and the residual
stands: the cell's own symmetry bounds the cover table's rank on both sides but
does not determine it. The symmetry used here is the full symmetry of the
four-cube, which is larger than the proper cubic rotations the admissibility
axiom names; a ceiling derived from a larger group is still a ceiling, but the
smaller group would give a weaker one, so nothing here should be read as a
statement about the axiom's own covariance. What remains is to name the eight
small matrices whose rank drops make up the 39, which the decomposition above now
makes a finite and small question.
