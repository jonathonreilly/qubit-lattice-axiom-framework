# Physical context-program dispatcher — Cycle 193

Date: 2026-07-16

Status: retained-grade constructive bridge; audit unset

Authority: none

Companion runner:
`scripts/physical_context_program_dispatcher_cycle193_2026_07_16.py`

## Result up front

Cycle 193 removes the host-side context lookup left by Cycle 191.

Three physical `H0/H1` context records now feed a strict-nearest-neighbour,
append-only dispatcher. Seven binary routers carry one active `H1` token
through a complete three-level tree. The token reaches exactly one of eight
spatial leaves:

```text
000  R1
001  R2
010  R3
011  C1
100  C2
101  C3
110  OMIT
111  INVALID / reserved.
```

The first seven leaves are physically adjacent to seven supplied binary tape
banks. The reserved `INVALID` leaf has no tape. At a selected legal leaf,
twelve ordered `H1` scan records append beside the bank's twelve physical
program bits. Unselected banks remain unscanned.

Thus the context record selects an ordered gate-token tape by physical local
history. There is no host dictionary lookup, no context-specific
eight-valued role, and no 32-valued payload.

This is not microscopic quantum execution. The selected tape still needs a
physical interpreter that gives the binary tokens their `H`, `CNOT`, pointer
copy, inverse-program, and coherent-carrier meanings. That gate-semantics atom
remains imported.

## Frozen predecessors

The runner pins:

```text
Cycle-179 runner
e5a143d7e35a084d8d3689008c7babe72b35934a5c447a8b41467837c1dd7d85

Cycle-179 note
ea8ed6744398b8dc435fa4a72d49ed017da43e5b3c566c645d4be40ff3bb9393

Cycle-191 runner
b7e3b21aef6005cb9715cf5c1b2612f6748c216066f771abfe4a3c01d9c10bc9

Cycle-191 note
62dc9974746976aeb202d91386b98c935ae335dda63e0ce0da86a5a2a8aa37ec
```

Cycle 179 supplies the relevant physical carrier type: separated `H0/H1`
records, ordinary bit cables, and finite append-only causal execution. Its
five-lane result does not reconstruct the five bits as one 32-valued site.

The context program is three bits, so Cycle 193 consumes three designated
lanes of that record representation. It does not collapse, reinterpret, or
require the other two Cycle-179 lanes. Full predecessor coexistence is tested
below.

Cycle 191 supplies the exact six decoder programs and code allocation. It
already proved that one H/CNOT circuit interpreter reproduces all six
Peres–Mermin pointer dilations. Its remaining host-side operation was choosing
the instruction string from a context code.

## Physical program encoding

Each legal tape bank contains exactly twelve `H0/H1` records:

```text
bit 0       RUN
bits 1..3   decoder length, binary 0..4
bits 4..11  four ordered two-bit gate-token slots.
```

The token code is:

```text
00  H0
01  H1
10  CX01
11  CX10.
```

Unused slots contain `00`. They remain physical program records and are
included in the deletion and flip controls.

The exact bank words are:

| code | label | RUN | length | four token slots |
|---|---|---:|---:|---|
| `000` | R1 | 1 | 0 | `H0 H0 H0 H0` |
| `001` | R2 | 1 | 4 | `H0 CX10 CX01 H0` |
| `010` | R3 | 1 | 3 | `H0 CX01 H0 H0` |
| `011` | C1 | 1 | 1 | `H1 H0 H0 H0` |
| `100` | C2 | 1 | 3 | `CX01 CX10 H1 H0` |
| `101` | C3 | 1 | 2 | `CX10 H1 H0 H0` |
| `110` | OMIT | 0 | 0 | `H0 H0 H0 H0` |
| `111` | INVALID | — | — | no bank |

All seven twelve-bit words are distinct. Decoding them reproduces the
Cycle-191 programs exactly.

`R1` and `OMIT` therefore no longer alias merely because both decoder strings
are empty. `RUN=1` tells the later common interpreter to execute the pointer
copy for R1; `RUN=0` makes OMIT skip the instrument.

## Smallest honest architecture used here

Seven legal actions require three context bits. Reserving the eighth code for
`INVALID` makes the complete binary tree exact.

Within the declared one-binary-router-per-decision architecture, eight leaves
require seven internal routers. Cycle 193 uses exactly seven.

Within the declared fixed-field tape format:

```text
one RUN bit
+ three bits for five possible lengths
+ eight bits for four two-bit tokens
= twelve bits.
```

That is exact for this format. It is not a global coding or Kolmogorov
minimality theorem, and the 61,989-record isolated cage is not claimed to be a
minimum embedding.

Selecting banks in place is smaller and more honest than copying all twelve
bits into a common address. The physical active-token/scan ancestry identifies
which bank is live. A later local token reader must follow that selected
spine; it may not replace the physical selection with a host address.

## Two local-law families

### Cable-fed absence-safe router

The first compact router attempt was correct only after both inputs arrived.
Its fixed cage accidentally matched an older Cycle-179 row while both sockets
were empty. Cycle 193 did not retain that cell.

The final router is required to be quiet in four preconditions:

```text
neither token nor bit present
token only
bit H0 only
bit H1 only.
```

When both inputs exist it executes:

```text
active H1 token + H0 bit -> H0 gate -> branch 0 H1
active H1 token + H1 bit -> H1 gate -> branch 1 H1.
```

The token and bit sockets are ordinary Cycle-179 cable endpoints. The final
family has:

```text
canonical schemas             4
proper-cubic raw rows         48
overlap with Cycle 179         0
new onsite roles               0.
```

### Ordered tape scan

A selected branch starts a serial scan. Each scan site sees:

```text
previous H1 scan record
one adjacent H0/H1 program bit
three fixed H0 markers
one open successor.
```

It appends one `H1` scan record for either bit value. The next site then has
its predecessor. Deleting a program bit blocks its scan site and every later
site; the bit is load-bearing rather than decorative.

The family has:

```text
canonical schemas              2
proper-cubic raw rows          30
safe retained overlaps         24
net-new raw rows                6
new onsite roles                0.
```

The complete candidate law is:

```text
Cycle-179 law              101,714
router net delta                48
scan net delta                   6
Cycle-193 union             101,768
conflicts                         0.
```

Every raw neighbourhood has exactly one output.

## Integrated physical execution

The fixed scaffold contains:

```text
binary router sites                    7
legal tape banks                       7
physical tape bits                    84
potential router dynamic sites        21
potential scan dynamic sites          84
potential cable dynamic sites      5,105
fixed isolated records             61,989.
```

Only the path selected by the context forms. All six contexts, OMIT, and
reserved INVALID pass under the same geometry and law.

Both lexicographically minimum and maximum schedulers reproduce the same
history for every code. Every pair of nearest-neighbour dynamic sites is a
declared direct parent/child pair. Therefore independent enabled writes cannot
change one another's local premise. This is the finite confluence certificate;
it supplies causal order, not a duration or occurrence rate.

For the longest Cycle-191 decoder, R2, the integrated dependency certificate
is:

```text
dynamic records              4,388
load-bearing edges           4,383
causal roots                     7
maximum causal depth           878
selected-leaf depth            866
completed-scan depth           878.
```

The complete R2 physical history closes in all 24 proper-cubic orientations.
R2 exercises both context-bit values, both branch types, both tape-bit values,
and all four gate-token encodings. The router and scan row families are also
closed explicitly under the same 24 rotations.

## Deletion and flip controls

The runner executes:

```text
context-record deletions                    24
context-record flips                        24
selected program-bit deletions              84
selected program-bit flips                  84
unselected program-bit mutations           168
two-bit gate-token deletions                 28
two-bit gate-token flips                     28.
```

Deleting any context input suppresses every selected tape. Flipping one
context input selects exactly the code at Hamming distance one, including
transitions to or from `INVALID`.

For every selected tape bit, deletion blocks the associated scan site.
A counterfactual boundary flip still permits the scan but changes exactly
that physical bit. Six length-field flips deliberately produce an invalid
length code; this exposes the need for validation in the later interpreter
rather than hiding malformed programs.

Deleting either two-bit token pair blocks that token position. Flipping both
bits selects the exactly altered two-bit token code. Unselected-bank
deletions and flips neither start that bank nor change the selected word.

These flips are alternative supplied program-bank fixtures. They are not
overwrites of already permanent records.

## Predecessor coexistence

Raw conflict freedom is not the only coexistence test.

The complete Cycle-179 hard history is replayed under the augmented
101,768-row law:

```text
fixed initial records          3,971,023
dynamic records                  341,029
maximum frontier                      27
terminal residual                      0
final output                          H1.
```

The dispatcher adds no onsite role. In particular, it adds neither a
context-specific eight-valued role nor a 32-valued payload role. Its program
contents remain separate physical `H0/H1` records.

## Exact import reduction

Cycle 191 required:

```text
classical context code
-> host lookup of one decoder string
-> host execution of the common circuit interpreter.
```

After Cycle 193:

```text
three physical context records
-> local cables
-> seven physical binary routers
-> one selected physical twelve-bit tape
-> ordered physical scan spine.
```

Host-side context lookup is removed. The supplied program bank is now visible
physical boundary content with deletion and corruption controls.

## Remaining gate-semantics atom

The new result stops at the correct seam.

Still unbuilt are:

1. a local reader that consumes the selected scan/bit pairs in order;
2. the physical meaning of token codes `H0`, `H1`, `CX01`, and `CX10` on a
   coherent carrier;
3. the common two-pointer-copy operation;
4. reversal of the decoder program after the copy;
5. fresh coherent system/pointer boundary states; and
6. proof that one homogeneous cubic law realizes those operations.

Cycle 191 proves the algebraic circuit equalities conditional on those gate
meanings. Cycle 193 proves physical lookup and ordered tape selection
conditional on the supplied bank. Neither result turns a classical bit cable
into a qubit gate.

The surviving atom is therefore substantially smaller than six imported
PVM/instrument tables or a host context dispatcher, but it is still physical
content.

Separately:

- the Born trace pairing remains imported;
- prepared-state identity remains a read-side condition;
- actual branch selection remains open;
- trial/reset and frequency remain open;
- no local occurrence rate or metric clock follows;
- matter and gravity are not derived.

No axiom, foundation, primitive, registry, policy, audit, or queue edit
follows. No axiom conclusion follows. No commit or push is made.

## Verification

```text
PYTHONPATH=scripts \
python3 scripts/physical_context_program_dispatcher_cycle193_2026_07_16.py
```

The retained runner must finish:

```text
PASS 19
FAIL 0
RESULT CYCLE193_PHYSICAL_CONTEXT_DISPATCHER_GREEN
```
