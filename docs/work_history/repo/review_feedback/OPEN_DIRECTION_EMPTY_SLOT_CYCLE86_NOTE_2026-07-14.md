# Open Direction To Physical EMPTY Slot — Cycle 86

**Date:** 2026-07-14
**Authority:** none
**Status:** positive supplied-harness openness encoder and slot comparator
**Constitutional effect:** none

Companion runner:

```text
scripts/open_direction_empty_slot_cycle86_2026_07_14.py
```

## Result up front

An actually open seed-frame direction can be converted into a physical
eight-bit EMPTY candidate and compared against an EMPTY reference without a
symbolic absence flag.

The reserved EMPTY word is chosen as:

```text
11111111
```

It is not assigned to any of the 134 bounded roles. A caged open sensor writes
one physical `H1` only while both axial neighbours are open: the monitored
direction behind it and the first EMPTY candidate site ahead. That sensor
record grows eight contiguous `H1` candidate records. Cycle 81's existing
five-neighbour equality row follows those records against a supplied all-H1
reference spine. Its eighth certificate is the physical slot MATCH.

The exact construction has:

```text
supplied source records             59
new canonical rows                   2
new proper-cubic raw rows            36
full provisional physical rows    4,624
reachable states                     46
append edges                         73
complete terminals                    1
parasites                             0
output conflicts                      0
rotated reachable-state controls  1,104
pre-existing extra controls        3,375
```

The 17 appends are the openness sensor, eight EMPTY candidate bits, and eight
comparator certificates. Candidate growth and comparison may interleave in
every schedule satisfying

```text
0 <= comparator certificates <= candidate bits <= 8.
```

All 45 such post-sensor states occur exactly once, plus the initial pre-sensor
state. Every schedule joins the same complete terminal.

The 59-record source is supplied. It contains the asymmetric frame, reference
word, two comparator cage rails, candidate growth markers, monitored-port
isolation cage, comparator start, and two alias blockers. It is not grown from
the official seed or a recurrent terminal.

## 1. Bare physical openness test

The sensor site has four recorded transverse neighbours. Its rear axial
neighbour is the direction being tested and is genuinely absent from the
source. Its forward axial neighbour is EMPTY bit 1 and is also open. The
openness row is the exact four-neighbour signature; any record at either axial
site changes the exact signature and removes that row.

This does not turn “absence” into a permanent site label. The first permanent
record is the sensor's `H1`, formed only in the exact open context. It is a
causal certificate that starts a physical output spine.

The second new row is an H1 wire. Each candidate target sees its preceding
`H1` plus three fixed `H0` markers and writes `H1`. The first target uses the
sensor as its predecessor; later targets use the preceding candidate bit.
The existing comparator start is supplied, but the equality chain cannot move
until the corresponding candidate bit exists.

Both new rows have four recorded neighbours. Their proper-cubic closures have
36 raw signatures and are disjoint from the Cycle-82 physical table. The
4,624-row provisional union is single-valued.

## 2. The alias found and repaired

The first bare geometry was logically correct but not composition-safe. Two
open sites beside the supplied comparator start saw existing Cycle-58 binary
signatures and wrote parasitic `H1` records. Those sites are:

```text
(-1,1,-1)
(-1,1,+1)
```

Cycle 86 supplies one fixed `H1` blocker at each site. Neither is adjacent to
the sensor, first candidate, or first comparator target, so the intended
signatures are unchanged. Exhaustive search over sensor colours, candidate
wire colours, monitored-port cage colours, and the two blocker colours found
the displayed collision-free assignment. The repaired source has exactly one
initially enabled write: the openness sensor.

This repair is finite law geometry, not an extra role or axiom sentence.

## 3. Extra-neighbour sensitivity

For each of all 134 bounded record contents, the runner inserts one record at
the monitored port before the sensor can form. It also tests one otherwise
unknown control content. Every such source is quiet: no sensor, candidate,
comparator, or off-footprint write is enabled.

Each of those 135 controls is repeated under all 24 proper cubic rotations,
in addition to its natural presentation:

```text
135 x 25 = 3,375 controls.
```

All are quiet. This is content-independent at the level of the exact local
law: the openness signature omits the monitored direction, while every
occupied control adds a fifth neighbour and therefore cannot equal it.

The monitored site is also never naturally writable in any of the 46
reachable no-extra states. Its supplied five-record isolation cage is inert
before the sensor and its completed six-neighbour cage is inert afterward.
Thus a late extra record is not part of this probe's natural graph.

This is a bounded reservation result. Multi-front reservation remains
untested: another nearby apparatus might change the monitored cage and expose
a write not present in this isolated source. The certificate cannot revoke
itself if an externally forced record is inserted after formation, so no
claim beyond the exhausted provisional union is made.

## 4. Composition with the 198 programs

Replacing Cycle 82's provisional EMPTY code by `11111111` preserves all 198
distinct directional programs. Their minimum Hamming distance remains one.
The exact inventory is:

```text
selected programs                 198
programs containing EMPTY         195
programs with all six occupied      3
total open-direction slots        613
```

Cycle 86 physically closes one such slot: open port to grown candidate word
to comparator certificate 8. Translation and proper-cubic covariance let the
same finite module represent any seed-frame direction.

It does not yet place 613 copies into Cycle 82's one contiguous six-slot
candidate geometry. In that geometry adjacent slot boundaries already occupy
the natural predecessor site used by the present H1 wire. Solving that packing
and routing problem is the named next residual, not something hidden by the
198-program census.

## 5. Exact disposition

`OPEN_DIRECTION_TO_EMPTY_WORD` is closed for one isolated, supplied,
seed-relative slot under the complete provisional raw union:

- the port is actually open, not prelabelled EMPTY;
- one extra record of any tested content blocks the encoder;
- the encoder writes eight physical `H1` records;
- the existing comparator validates the word physically;
- all schedules and proper-cubic images agree; and
- the monitored port remains reserved throughout natural reachability.

The remaining physical obligations are:

### `EMPTY_SLOT_TO_SIX_SLOT_CANDIDATE_GEOMETRY`

Pack translated openness modules into any subset of the six directional
slots, preserve the fixed directional order, and connect their final
certificates into the complete row matcher without sharing a predecessor site
or colliding with occupied-word routes.

### `NEIGHBOUR_MACROBLOCKS_TO_ORDERED_STREAM`

Route validated occupied-neighbour words into the other slots in the same
physical geometry.

### `CANDIDATE_FANOUT_TO_198_PROGRAMS`

Distribute or serially classify the completed six-slot candidate without
assuming a symbolic role register and without allowing rejected permanent
prefixes to start an output writer.

### `SEED_TO_OPENNESS_ENCODER_HARNESS`

Grow the present 59-record source and reserve its open sensor/candidate/
certificate footprint from the official seed or selected recurrent front.

No foundation edit, queue edit, audit verdict, commit, push, or PR is made.
No axiom addition follows from this finite openness encoder or its remaining
compiler geometry.

## Verification

```text
python3 scripts/open_direction_empty_slot_cycle86_2026_07_14.py
```
