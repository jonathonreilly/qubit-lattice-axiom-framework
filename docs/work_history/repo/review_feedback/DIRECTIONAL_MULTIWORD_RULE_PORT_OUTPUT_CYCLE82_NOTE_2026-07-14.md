# Directional Multiword Rule Port And Output — Cycle 82

**Date:** 2026-07-14
**Authority:** none
**Status:** positive supplied-harness construction for full six-neighbour rows and universal output writer
**Constitutional effect:** none

Companion runner:

```text
scripts/directional_multiword_rule_port_output_cycle82_2026_07_14.py
```

## Result up front

Two operational pieces now exist in physical `H0/H1` records:

1. A complete six-neighbour exact signature can be serialized as six ordered
   eight-bit slots and compared by one 48-bit equality chain. Its final
   certificate is a physical rule port.
2. Conditional on an incoming physical H1 rule port, a finite writer copies
   any supplied eight-bit output program into fresh DATA records, follows each
   DATA record with a certificate, and writes VALID last.

The construction is end-to-end for the three arity-six rows in the selected
198-row Cycle-60/67/72/80 table. They are the hardest occupied-neighbour case:
every direction contains a role word, so no open-direction surrogate is
needed. Each matched pipeline has exactly:

```text
supplied source records        262
physical appends                65
reachable states                66
append edges                    65
terminals                        1
false or parasitic appends       0
output conflicts                 0
```

The 65 appends are 48 comparator certificates, eight DATA records, eight
output certificates, and one VALID record. The terminal DATA spine is exactly
the eight-bit code assigned to that selected row's output.

The output writer was also exhausted independently over all 256 possible
eight-bit programs:

```text
writer source       69 supplied records + one incoming H1 port
writer appends      17
aggregate states  4608
aggregate edges   4352
terminals          256
wrong output         0
parasites            0
conflicts             0
```

All Cycle-82 harnesses and program rails are supplied. This is not a
seed-grown compiler, not a 198-way physical program bank, and not a claim that
an actually occupied six-neighbour lattice boundary has already been routed
into the candidate spine.

## 1. Directional encoding

The seed-carried frame orders the six nearest-neighbour directions. Each slot
contains exactly one eight-record physical word. Thus an exact neighbourhood
program has fixed length:

```text
6 directions x 8 records = 48 bits
```

For a recorded neighbour, the slot is the Cycle-81 word assigned to its
content. For an open direction, the finite program uses one otherwise
reserved eight-bit `EMPTY` word. That produces 198 distinct 48-bit programs,
one per selected canonical exact signature. Their minimum pairwise Hamming
distance is one; equality, not error correction, is the present requirement.

The EMPTY word is only a program-level placeholder in this cycle. No rule has
yet derived or written it from physical openness. Therefore the complete
198-row encoding inventory is real, while physical execution is currently
restricted to the three rows with all six directions occupied.

The order is relational. The asymmetric cage carries a finite frame and the
whole construction is closed under all 24 proper cubic rotations. A global
axis or coordinate congruence is not a law input.

## 2. One comparator instead of six plus a fan-in tree

Six separate eight-bit comparators would require routing six MATCH records to
an additional conjunction network. The serial form is smaller conceptually
and uses no new equality law:

```text
direction -x word
direction -y word
direction -z word
direction +z word
direction +y word
direction +x word
```

concatenated in the seed frame. Cycle 81's two five-neighbour equality rows
advance through those 48 physical bit pairs. Any mismatch leaves the current
certificate site open and the chain quiet. If all bits agree, certificate 48
forms. That record is already `H1` and is used directly as the rule port; no
separate symbolic MATCH or Boolean fan-in exists.

As an off-target control, the runner replaces each of the six expected roles
by every other one of the 134 assigned roles for each full row. All 2,394
one-role substitutions stop quietly before the rule port. None exposes the
output writer.

This closes the logical conjunction for a supplied, ordered candidate stream
and a supplied row program. It does not yet transport six real neighbour
macroblocks into that stream or choose which of 198 stored programs receives
the candidate.

## 3. Physical eight-bit output writer

The writer alternates DATA and certificate sites along one seed-frame line.
For each bit:

1. DATA sees the preceding `H1` port/certificate, its supplied program bit,
   and three fixed cage records, then writes that physical `H0` or `H1` bit.
2. CERT sees the new DATA record plus four fixed cage records and writes `H1`.
3. The next DATA site can then proceed.

After certificate 8, a completely surrounded VALID site writes `H1`. The
physical table has five canonical rows and 48 proper-cubic raw rows. Twenty-
four raw rows safely coincide with earlier `H1` rows; the demanded output is
identical. The complete provisional Cycle-58 + selected extensional + Cycle-81
comparator + Cycle-82 writer union contains 4,588 raw rows and is
single-valued.

The fixed 62-record writer cage has trivial proper-cubic stabilizer. The full
writer source is 69 supplied program/cage records plus the incoming physical
port. An external diagnostic reads the eight DATA records only after VALID;
the law never receives or emits an extensional role label.

`RULE_PORT_TO_EIGHT_BIT_OUTPUT_WORD` is therefore closed conditionally on an
incoming physical H1 rule port and a supplied output program/cage. Seed-grown
placement and programming remain separate obligations.

## 4. Exact end-to-end rows

The three six-neighbour selected rows output `DONE`, `I2`, and `P2`. For each:

- the reference stream is the row's exact six-slot physical program;
- the candidate stream is the same supplied six-slot word sequence;
- the 48-bit certificate chain reaches its final physical port;
- that port starts the associated eight-bit output writer;
- every intermediate state has exactly one intended append; and
- the terminal DATA spine decodes to the selected output word.

Every proper-cubic image uses the same raw laws. Ninety-six transformed
pipeline controls have exact transformed frontiers.

This is the first direct physical path in the present compiler work from a
multi-neighbour role pattern to its output macro-word. It remains a finite
supplied-harness path, not yet the autonomous lattice law.

## 5. Exact residuals

### `NEIGHBOUR_MACROBLOCKS_TO_ORDERED_STREAM`

Route the six actual seed-relative neighbour macroblocks into one ordered
48-bit candidate spine without copying a symbolic label, crossing another
reserved footprint, or assuming a global orientation. The source word must be
the validated physical DATA spine of the neighbour block.

### `OPEN_DIRECTION_TO_EMPTY_WORD`

For the 195 selected rows with arity below six, turn a locally certified open
direction into the reserved EMPTY slot word. It must stay sensitive to any
extra recorded neighbour and cannot treat absence as a prewritten record.

### `CANDIDATE_FANOUT_TO_198_PROGRAMS`

Supply the same six-slot candidate to the 198 distinct row programs, or build
an equivalent serial selector, so exactly one physical final certificate can
form. The permanent partial prefixes left by rejected rows must remain inert,
and associated output programs must not start without their own port.

### `SEED_TO_RULE_PORT_OUTPUT_HARNESS`

Grow the comparator cage, candidate/reference streams, output program rail,
DATA/CERT cage, and reserved open sites from the official seed or selected
recurrent terminal. The present 262-record end-to-end source is supplied.

These residuals distinguish two claims cleanly:

- `DIRECTIONAL_MULTIWORD_MATCH_TO_RULE_PORT` is closed for supplied ordered
  streams with all six directions occupied; it remains open for physical
  routing, openness, and 198-way selection.
- `RULE_PORT_TO_EIGHT_BIT_OUTPUT_WORD` is closed for an incoming physical port
  and supplied program/cage; it remains open for autonomous harness growth.

## 6. Scope and constitutional disposition

Cycle 82 does not select the exact physical law, attach the recurrent tube to
the real q/a/b/c front, establish multi-front confluence, or derive occurrence,
probability, rate, clock, mass, gravity, or resource price.

No foundation edit, registry edit, audit verdict, queue edit, or commit is
authorized or made. No axiom addition follows from the directional serializer,
comparator port, output writer, or their remaining finite compiler work.

## Verification

```text
python3 scripts/directional_multiword_rule_port_output_cycle82_2026_07_14.py
```
