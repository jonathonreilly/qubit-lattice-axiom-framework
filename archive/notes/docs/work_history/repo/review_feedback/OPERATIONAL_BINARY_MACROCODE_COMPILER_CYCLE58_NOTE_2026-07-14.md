# Operational Binary Macrocode Compiler — Cycle 58

**Date:** 2026-07-14

**Type:** authority-free positive finite candidate-law construction, exact
binary codebook, complete asynchronous graph, proper-cubic covariance test,
and bounded operational handoff

**Authority: none.** This note is not an axiom proposal, registered primitive,
retained theorem, audit verdict, or permission to change foundation, registry,
policy, queue, or audit state. **No live foundation or audit edit is
authorized.** It issues **no audit verdict**, commit, push, or PR. It makes **no
axiom need** claim.

Companion runner:

```text
scripts/operational_binary_macrocode_compiler_cycle58_2026_07_14.py
```

## Result Up Front

Cycle 58 positively constructs the first operational binary macrocode object:

> `BINARY_DATA_VALID_HANDSHAKE`.

The Cycle-52 rail uses 48 phase/position roles plus `BACKSTOP`. Its current
runner treats those as distinct one-site `M_2(C)` contents, while its note
correctly says that no one-site decoder for the generally nonorthogonal choices
has been constructed. Cycle 58 replaces that extensional role alphabet at the
storage boundary with ordered six-record words over the exact `H0/H1` pair
already present in the Cycle-43/47 seed.

The exact candidate-law dictionary in Cycle 41 represents `H1/H0` by the
opposite Bloch vectors `+/- (0,1,0)`. They are complementary rank-one
projectors. Cycle 58 does not select a new basis: its finite harness and output
records use that seed-carried pair, and every proper-cubic image carries the
whole spatial frame with it.

For each of all 64 six-bit words, a supplied 30-record binary harness builds:

```text
six ordered DATA records
six ordered certificate records
one spatial VALID record
one spatial READY/launch record
```

Every new record is either `H0` or `H1`. DATA grows in order along one
nearest-neighbour spine. A second spine may follow DATA at any speed but can
never overtake it. `VALID` requires the sixth certificate; READY requires
VALID. Each word has exactly **30 reachable states**, **44 directed edges**, one
terminal, zero parasites, zero output conflicts, and zero overwrite attempts.
The graph contains every interleaving of the DATA and certificate fronts.

The union rule table covers all 64 words simultaneously. Its proper-cubic
closure has 132 raw directional signatures and no conflicting output. The
runner exhausts all 64 words under all 24 proper-cubic rotations: **1,536 graph
instances**, **46,080 reachable states**, and **67,584 directed edges**, all
exact transformed copies. It separately checks all 4,096 arbitrary subsets of
the six DATA positions; none directly enables VALID, READY, or decoding.

This closes only operational word storage, completion certification, and
ordered readout for the exact finite object. It does not yet construct the
harness from the seven-record seed or compile a Cycle-52 logical neighbour
rule into binary comparison/build circuits. The exact next operational
residuals are:

> `SEED_TO_BINARY_HARNESS`

and

> `VALIDATED_WORD_TO_EXACT_NN_RULE_MATCH`.

Neither residual is evidence for an axiom addition.

## 1. Exact Codebook

Write each rail role as

```text
phase bits | y bits | z bits.
```

The structural assignment is:

```text
A/B/C/D = 00/01/10/11
y       = 00/01/10/11
z       = 00/01/10
```

Thus the 48 Cycle-52 roles occupy exactly the 48 words whose last two bits are
not `11`. The special port roles `LAUNCH_A`, `LAUNCH_B`, `LAUNCH_C`, and
`LAUNCH_D` are the ordinary codes at the corresponding phase/position ports;
they do not consume extra words.

The `z=11` band supplies sixteen control words. This cycle assigns fourteen:

```text
BACKSTOP, Z0, H0, H1,
AUX, JOINT, RING, JOIN,
COMPLETE, P0, P1, ARM,
START, VALID.
```

Two words remain reserved. The live role/control inventory therefore uses 62
of 64 words. If rejected experimental labels such as `TIP` and `TOKEN` were
revived, they would consume the last two; any further genuinely distinct
macro-role would require retiring/reusing a control or moving to seven bits.

Two Cycle-55 roles illustrate the encoding:

```text
A_2_1 = 001001
A_1_2 = 000110
```

Their Hamming distance is four. Cycle 58 does not claim that this assignment
optimizes the Cycle-55 alias graph; a later comparator compiler may permute the
48 injective words while preserving six-bit capacity.

The elementary lower bound is exact for perfectly distinguishable binary
storage:

```text
2^5 = 32 < 49 <= 64 = 2^6.
```

This is also the finite perfect-decoding specialization of the accessible
information bound in Holevo, [*Bounds for the Quantity of Information
Transmitted by a Quantum Communication Channel*](https://www.mathnet.ru/eng/ppi903)
(1973). The builder copies only the fixed orthogonal `H0/H1` alphabet. It does
not invoke a copier for arbitrary nonorthogonal qubit contents, which would run
into Wootters and Zurek, [*A single quantum cannot be
cloned*](https://doi.org/10.1038/299802a0) (1982).

## 2. Exact Radius-One Geometry

Let the seed-carried frame be `(d,e,u)`. In the natural presentation, the
ordered six-site DATA core is

```text
Gamma6 = {(i,0,0) : i=0,...,5}.
```

The certificate spine is the parallel set

```text
{(i,1,0) : i=0,...,5}.
```

The DATA core alone does not claim an intrinsic orientation: its order is read
in the frame carried from the official seed. The complete 30-record harness,
including its start and terminal markers, has trivial stabilizer under the 24
proper cubic rotations for every one of the 64 program words. No global
coordinate origin, coordinate congruence class, or preferred lattice axis is
installed in the law.

At DATA stage `i`, the open target sees exactly:

```text
the preceding DATA record (or the supplied start record);
a lower H0 marker;
the program bit H0 or H1;
and an H1 reference opposite the program bit.
```

Its successor and certificate neighbour remain open. The local signature
therefore contains four recorded nearest neighbours and copies exactly the
program bit. The geometric pattern makes the output a rotation-invariant
function of the exact signature: `H0/H1` against the opposite H1 reference.

Certificate stage `i` sees exactly three recorded nearest neighbours:

```text
DATA[i], CERT[i-1], and one H0 marker.
```

For `i=0`, the finite harness supplies the preceding certificate start. The
certificate output is always H1. The three-neighbour VALID and READY inputs
overlap some certificate inputs under rotation, but every overlap demands the
same H1 output. The full raw table is therefore single-valued.

Every rule offset is one of the six cubic nearest-neighbour directions. No
site reads a six-bit word, no site emits a 49-valued content, and rule identity
is carried by the permanent local geometry.

## 3. Complete DATA-to-VALID Graph

Represent a partial state by `(d,c)`, where `d` DATA records and `c`
certificate records have formed. Append-only reachability gives exactly

```text
0 <= c <= d <= 6.
```

There are 28 such pairs. From each pair, the next DATA write is available when
`d<6`, and the next certificate write is available when `c<d`. This gives every
interleaving without choosing a schedule. After `(6,6)`, VALID and then READY
add two more states:

```text
reachable states = 28 + 2 = 30
directed edges   = 21 DATA + 21 CERT + VALID + READY = 44.
```

The runner scans every open nearest-neighbour candidate at every state. For
all 64 words together it establishes:

- the DATA contents reproduce the six supplied program bits exactly;
- DATA and certificate occupancy are always prefixes;
- the certificate prefix never exceeds the DATA prefix;
- no partial state exposes more than the next DATA and next certificate;
- VALID implies all six DATA and all six certificates are present;
- READY implies VALID;
- decoding returns no role before VALID;
- decoding after VALID returns exactly the codebook label;
- every maximal schedule joins one exact terminal; and
- no rule writes outside the declared fourteen-record output footprint.

The separate arbitrary-subset control inserts each of the 64 subsets of the
six correct DATA bits into each of the 64 program harnesses, without inserting
certificates. None of those 4,096 states directly enables VALID, READY, or the
decoder. Thus the completion handshake does not reduce to “sixth DATA site
present”; it leaves an explicit permanent certificate chain in the state.

## 4. Proper-Cubic Covariance And Output Aliases

The union table is generated before any graph run from every word/stage input
and all 24 determinant-`+1` signed permutation images. It contains:

```text
raw directional signatures: 132
output-conflicting inputs:      0
new output contents:       {H0,H1}
input radii:                    1
```

The exact frontier of every one of the 1,920 natural word/stage states equals
the intended next DATA/CERT/VALID/READY set. This is stronger than checking
only the final word: it catches every rotated output alias and every premature
launch at every partial state.

The runner then rotates and translates the seven-record official seed, the
entire binary harness, and the declared output footprint together. Every one
of the 1,536 transformed graphs has the same 30-state/44-edge census, exact
transformed state set, and exact transformed terminal. The macrocode table is
also quiet on the official seven-record seed by itself.

## 5. Decoder And Readout Boundary

The operational decoder is deliberately not a one-site label oracle. After
VALID, it reads the ordered tuple of the six individual DATA records in the
seed-carried frame and applies the displayed finite codebook. The physical law
itself has already distinguished `H0` from `H1` in each exact local signature;
the Cycle-41 candidate dictionary makes them orthogonal projectors.

This does not derive that the bare Record axiom's scalar readout `I` separates
the pair. Summing the six scalar values would in any case lose bit order and
can collapse different words to one Hamming weight. A later retained bridge
must either show

```text
I(H0) != I(H1)
```

for the selected pair, or implement a seed-relative spatial comparator/readout
using the exact candidate law. Until then, direct scalar readout is a named
conditional boundary, not content silently added to the axiom.

## 6. Exact Residuals

### `SEED_TO_BINARY_HARNESS`

The runner includes the exact seven-record Cycle-43/47 seed and proves the
macrocode rules are quiet on it, but the 30-record H0/H1 program/cage harness is
supplied at a disjoint seed-relative location. It is not yet grown from those
seven records. A seed-autonomous compiler must construct that finite binary
geometry append-only, reserve its open DATA/CERT tunnel, and write the desired
six program bits without already assuming the role it is meant to encode.

### `VALIDATED_WORD_TO_EXACT_NN_RULE_MATCH`

Cycle 58 validates and decodes one block. It does not yet replace a Cycle-52
cooperative write. That requires binary fanout/comparison circuits which:

1. consume the validated words of the relevant logical neighbours;
2. certify the required open logical directions;
3. select exactly one Cycle-52 rule port;
4. build the six DATA bits of the output block in fresh space;
5. issue its VALID token last; and
6. remain single-valued under all rotated tables and asynchronous collisions.

That is candidate-law/compiler work. It is also the point where the binary
macrocode must be reconnected to Cycle 56's remaining A-slice construction and
to `FIRST_ROLE_DIFFERENTIATION`'s now-positive off-target path.

## 7. Constitutional Disposition

No axiom addition follows from this construction. The codebook, binary cage,
certificate spine, VALID/READY handshake, covariance closure, and eventual
rule comparator are finite exact-law content.

An axiom change would be implicated only by insisting on a one-site 49-way
perfect decoder, a globally preinstalled preferred binary basis or macrocell
tiling, or a universal copier for arbitrary `M_2(C)` contents. Cycle 58 uses
none of those.

The cycle also supplies no formation occurrence, fairness, probability, rate,
clock, mass, or gravity law. The graph classifies which append is available at
each reachable state; it does not assert that an available write occurs or how
often.

## Verification

```text
python3 scripts/operational_binary_macrocode_compiler_cycle58_2026_07_14.py
PASS=63 FAIL=0
```
