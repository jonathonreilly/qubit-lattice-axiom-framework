# Lawful H0 reference fork — Cycle 114

Date: 2026-07-15

Authority: none

Disposition: positive bounded construction;
partial-narrowing-with-live-constructive-routes

Write scope: runner + review note only

Companion runner:

```text
scripts/lawful_h0_reference_fork_cycle114_2026_07_15.py
```

No predecessor edit; no foundation edit; no axiom edit; no primitive edit; no
registry edit; no queue edit; no policy edit; no audit verdict; and no commit
is made here.

## Result

Cycle 111's next object,

```text
SECOND_VALID_LITERAL_HISTORY_TO_LAWFUL_H0_REFERENCE
```

is closed at bounded availability grade.

The exact Cycle-100 word is the valid, lawfully generated record corpus

```text
R_B11 = 10010100.
```

Five of its eight data records are physical `H0` records.  Cycle 114 copies
one of them through three new local rows into the exact Cycle-109 reference
site.  The existing Cycle-109 mismatch status and reject rows then complete a
lawful `H0` branch:

```text
stored bit2=(1,5,1)=H0
  -> COPY=(2,5,1)=H0
  -> GUARD=(2,5,2)=H0
  -> REFERENCE=(2,6,2)=H0
  -> STATUS=(3,6,2)=H0
  -> PAYLOAD-SITE=(4,6,2)=AUX
  -> LAUNCH=(4,5,2)=A_0_0.
```

There is no post-front mutation and no external fault injection.  Every record
in that chain is an append licensed by the combined candidate-law table from
the unchanged 264-record Cycle-100 terminal.

The original Cycle-109 `H1` path remains in the same fixed table.  The fork is
a schedule race at one precise local seam:

- if Cycle 109's original `T_H0` guard forms before `COPY`, its permanent
  presence changes the copy site's complete local signature and the original
  `H1 -> R_B11` history completes unchanged;
- if `COPY` forms first, it changes the guard's complete local signature; the
  `H0 -> AUX -> A_0_0` history completes instead.

Append-only occupancy makes those branches mutually exclusive after the first
of the competing records forms.  Both are law-admissible histories.  The
runner does not select which occurs and computes no branch probability.

## The minimum probes

### One-row physical-H0 existence probe

The smallest standalone probe uses stored bit1 at `(1,5,0)=H0`:

```text
south R_A22 + north stored H0 -> STANDALONE_COPY=(1,5,-1)=H0.
```

That complete local signature occurs at exactly one open site.  The addition
is one canonical / 24 raw proper-cubic rows, has zero overlap with Cycle 109,
and gives a 7,520-row single-valued union.

Its exact asynchronous graph is:

```text
states        22,640
edges        119,452
terminals          1
terminal size     47
bad fronts         0
max frontier      10
```

All 96 rail appends remain exact.  The standalone locality product is
`2,196,080` states / `13,760,284` edges, all `7,520 x 24 = 180,480` raw
proper-cubic images preserve output, and every rotated completed history
exposes only the rotated next rail record.

This closes lawful physical `H0` reference existence from the valid word with
zero new supplied records.  It does not close the comparator target: the
standalone copy remains five L1 steps from Cycle 109's reference site.

### Three-row comparator probe

The selected comparator route uses stored bit2 because its nearest unique open
copy site is already embedded in the grown reader/certificate geometry.  The
three new rows are:

```text
1. H0 + R_A01 + H1 + R_B32 + R_B40 -> COPY=H0
2. H1 + stored H0 + COPY=H0 + BACKSTOP -> GUARD=H0
3. R_B21 + GUARD=H0 + R_B32 -> REFERENCE=H0.
```

The new surface is three canonical / 72 raw rows.  It is disjoint from the
7,496 Cycle-109 rows, so the full 7,568-row union is single-valued and remains
inside the 153-role onsite alphabet.

This is the smallest landed route among the tested constructions that retains
both the original `H1` history and a physical `H0` history at the actual
comparator.  It is not claimed as a global lower bound over every encoding or
larger local circuit.

Two shorter-looking routes fail the stated two-history target:

- changing Cycle 109's existing guard output from `T_H0` to `H0` creates 24
  literal raw-input/output conflicts; replacing the row would erase rather
  than preserve the `H1` history;
- the nearest inherited `H0` is two lattice steps from the reference.  A
  direct midpoint write occupies the guard before the landed `BACKSTOP` cage
  can form, so another repair row is still required for the exact mismatch
  status.

An exhaustive rotated-motif search finds only the actual Cycle-109 `STATUS`
site with its actual `REFERENCE` site missing.  There is no already-present
translated `H1/H0/BACKSTOP` comparator elsewhere in this corpus.

## Exact graph

The two-history graph starts from the exact Cycle-100 terminal and supplies no
Cycle-114 record.  Every asynchronous ordering is exhausted:

```text
local states              17,880
local edges               88,642
terminal histories             2
H1 terminal writes            46
H0 terminal writes            48
bad fronts                     0
maximum frontier              10
```

The two terminal summaries are exactly:

| history | copy | guard | reference | status | decision site | launch |
|---|---|---|---|---|---|---|
| existing correct branch | absent | `T_H0` | `H1` | `H1` | `R_B11` | absent |
| new mismatch branch | `H0` | `H0` | `H0` | `H0` | `AUX` | `A_0_0` |

All eight one-bit changes of the stored word, wrong `VALID`, and wrong `READY`
still reach one stopped graph and never reach either comparator outcome.  Their
state/edge/terminal-size census is unchanged from Cycle 109:

```text
bit 0   760 / 2,274 / 29
bit 1   680 / 2,022 / 28
bit 2   600 / 1,770 / 27
bit 3   440 / 1,186 / 26
bit 4   120 /   238 / 20
bit 5   200 /   490 / 20
bit 6    80 /   152 / 18
bit 7    60 /   109 / 17
VALID    40 /    66 / 16
READY    20 /    23 / 15
```

Thus the new branch depends on the exact valid word history.  A source mutation
is a negative control, never reclassified as a second valid input.

## Rail and covariance controls

Both lawful terminals retain every one of the 96 required rail appends as an
exact singleton frontier.  The new support is at minimum L1 distance seven
from those rail records, and none of the 72 new raw rows matches any of the 97
rail prefixes.  The exact asynchronous locality product is:

```text
states = 17,880 x 97                         = 1,734,360
edges  = 88,642 x 97 + 17,880 x 96          = 10,314,754
```

Every one of the `7,568 x 24 = 181,632` proper-cubic raw images preserves its
output.  “Canonical” in the runner and this note means only one representative
of a proper-cubic signature orbit.  It supplies no direction, physics, or
authority.

## What closed and what did not

Closed here:

```text
LAWFUL_ALTERNATE_H0_REFERENCE_GENERATION
SECOND_VALID_LITERAL_HISTORY_TO_LAWFUL_H0_REFERENCE
```

The closure is deliberately narrow.  It proves that the already-valid word
can cause a later local record history to contain `H0` at the actual comparator
reference, and that the landed mismatch/reject path can consume it.  It does
not prove an alternate valid **bit0 word**, a second generated complete role
encoding, a host-addressable selector, or a reusable serial stream.

The next useful construction is:

```text
ADDRESSABLE_TWO_VALUED_REFERENCE_STREAM
```

At present, both reference values are law-admissible but the local schedule
race chooses which history completes.  A strict compiler must instead bind the
chosen value to an explicit candidate/address record and extend that control
through the all-bit reusable status harness.  Successor allocation remains
ordered after that apparatus; it is not another simultaneous first blocker.

No occurrence, fairness, rate, weighting, probability, or time law follows
from the two reachable histories.  State count, edge count, and the existence
of two terminals are not branch weights.

## Bare-metal and constitutional meaning

This is a particularly literal model of a “read.”  The stored `H0` never
changes.  A new open site has a local availability row whose input includes
that earlier `H0` record.  If the new site records `H0` first, that permanent
fact changes which later guard and reference records are locally available.
Nothing observes an unsettled object and nothing later locks an earlier fact.

The result therefore adds no support for read-caused formation, later-read
locking, independent-witness locking, or clock locking.  It also does not
select an occurrence rule: the fixed candidate law permits both terminal
histories, while the current axioms do not state which enabled append happens
first.  That missing operational selection belongs to the exact-law/occurrence
program, not silently to Record prose.  No axiom addition follows.

The approved primitive scopes remain exactly:

- scale reference: units only;
- kinetic reference: `c_t=c_s` form only; and
- realized-state reference: pointwise realized-state reference only.

None supplies an `H0`, a schedule, a branch selector, or a comparator.

## Cycle 112 coordination boundary

Cycle 112 remained unlanded at the Cycle-114 freeze and was not consumed.
A contemporaneous message reported a zipper prototype with several lawfully
grown `H0` data records and an exact Cycle-93 status path.  Without a runner
and note in the shared tree, that report is a live future route rather than
evidence, a table import, or a disposition change here.

## N1–N8 no-go-discipline gate

Status: **PASS for the bounded positive closure; FAIL for any universal
negative.**  The next residual is shipped only as
partial-narrowing-with-live-constructive-routes, not a universal no-go.

### N1 — Alternative-route enumeration

| route | marker | exact result |
|---|---|---|
| Copy stored bit1 to `(1,5,-1)` | `ATTEMPTED` | One-row zero-source positive; proves physical H0 existence but remains five L1 steps from the comparator reference. |
| Copy stored bit2 through guard into exact reference | `ATTEMPTED` | Selected three-row positive; produces the 17,880-state two-history fork and exact H0 reject branch. |
| Change the original C109 guard output directly | `ATTEMPTED` | Adding it creates 24 raw output conflicts; substituting it removes the H1 history, so it does not meet the two-history target. |
| Reuse an existing landed H0-output row at REFERENCE | `ATTEMPTED` | C109 has eight H0-output canonical classes, but none matches the lawful reference prefix. |
| Generate a second complete encoded role at the C100 endpoint | `ATTEMPTED` | The landed ten-write surface makes only R_B11/VALID/READY; every one-bit substitution stops before the next certificate. |
| Find a translated existing comparator around another H0 | `ATTEMPTED` | Full proper-cubic motif search finds only the current STATUS/REFERENCE pair missing H0. |
| Treat C109's injected H0 control as physical input | `ATTEMPTED` | Rejected by the target antecedent: that control deletes the lawful H1 reference and inserts H0 externally. |

The unlanded zipper route remains credible and untested.  A broad claim that
an addressable source cannot be built is therefore premature.

### N2 — Wall-independence audit

After the present closure, let `W0` be addressable H0/H1 selection, `W1` be
the all-bit status stream plus reusable harness, and `W2` be successor-cell
allocation.

| pair | closing first closes second? | closing second closes first? | independent? | disposition |
|---|---:|---:|---:|---|
| `W0/W1` | no | yes | no | `W0` is the first sub-edge; a complete addressable all-bit harness necessarily contains it. |
| `W0/W2` | no | yes on the selected route | no | reusable successor allocation consumes an addressable predecessor harness. |
| `W1/W2` | no | yes on the selected route | no | `W2` is ordered after the combined stream/harness stage. |

The collapsed current wall set therefore contains one first object,
`ADDRESSABLE_TWO_VALUED_REFERENCE_STREAM`.  The table does not inflate the
downstream harness and successor allocator into co-equal present blockers.
This ordering is for the selected strict-compiler route, not all imaginable
architectures.

### N3 — Hidden-wall scan

The load-bearing boundary is explicit: 264 inherited generated records; five
stored H0 word bits; the 7,496-row C109 law; three new orbit-representative
rows; zero supplied Cycle-114 records; finite asynchronous append semantics;
and a 96-append rail horizon.  “Canonical” is signature compression only.
“History” means one reachable append-only record configuration, not a supplied
state measure.  The schedule race is exposed rather than presented as a
selector.  No occurrence, fairness, weight, rate, probability, or unbounded
continuation is hidden.

### N4 — Residual matching

| cited witness | exact prior residual | Cycle-114 use | match? |
|---|---|---|---:|
| Cycle 100 | valid generated R_B11 word; first harness still open | exact H0 source records | yes |
| Cycle 101 | all eight literal bits physically consumed; read does not lock them | exact reader/certificate geometry for COPY | yes |
| Cycle 109 | lawful alternate H0 reference absent; injected H0 only a fault control | exact residual closed without injection | yes |
| Cycle 111 | `SECOND_VALID_LITERAL_HISTORY_TO_LAWFUL_H0_REFERENCE` is the next object | exact target and closure name | yes |
| Cycle 93 | total H0/H1 status recurrence exists with supplied apparatus | future all-bit route only | partial; not cited as current zero-source closure |

No probability, clock, storage, or axiom residual is used as evidence for the
local H0 construction.

### N5 — Resolution and rhetoric audit

| resolution | tested result |
|---|---|
| per stored record | five exact H0 word records exist; two are used in positive probes |
| per copied record | one standalone and one comparator-local H0 copy are schedule-exhausted |
| per exact reference site | H0 reaches C109 REFERENCE and its reject chain |
| per reachable local history | exactly two terminal histories, both lawful |
| addressed candidate/value selection | not closed; the branch is schedule-selected |
| all-bit reusable stream | not closed |
| successor/unbounded lattice | not tested |

Accordingly, the result is never phrased as a complete two-valued selector or
an all-bit compiler theorem.

### N6 — Primitive and partial-closure path scan

No approved primitive supplies the missing address or selector.  Several
nonconstitutional paths remain live:

- add an explicit grown address record that gates COPY versus the original
  guard before either becomes enabled;
- extend the bit-local fork across the stored eight-bit word;
- attach the compatible Cycle-93 status recurrence after growing its cages;
- use the reported zipper data records after literal artifact verification;
- redesign the surface encoder so each bit carries its next address; or
- translate the comparator into a disjoint second cell and select the cell by
  a generated role.

These are candidate-law constructions.  The zero-edit route remains live.

### N7 — Strongest hostile steelman

The strongest hostile steelman is that the residual may be only one small
integration circuit away from closure.  Cycle 114 already gives both values,
the exact C109 mismatch decision, append-only mutual exclusion, and a
corruption-safe valid-word antecedent.  Cycle 93 already contains the full
serial status truth table, and the reported unlanded zipper allegedly grows
several H0 data records.  A single physical address rail could delay the
original guard until the selected data bit arrives and convert the schedule
race into a value-selected fork.  That route is concrete and credible, so no
broad selector no-go can ship.

### N8 — Cross-cycle echo

Cycle 100 removed a supplied word by growing R_B11 directly.  Cycle 101 removed
the supplied first-reader apparatus with a local surface walk.  Cycle 108
retired a reader/rail collision by role remapping.  Cycle 109 retired the
unconditional-cap/reject collision by a local table substitution.  Cycle 114
now retires fault-only H0 by copying a permanent H0 already in the generated
word.  All are examples of source removal, physical context, or local
recompilation closing a seam without constitutional change.  The same repair
mechanisms remain available for addressability.

## Final disposition

Cycle 114 supplies the missing lawful `H0` reference history from the actual
generated corpus and reuses the exact Cycle-109 reject path.  The one-row probe
closes physical H0 existence; the three-row fork closes the actual comparator
reference target while preserving the H1 history.  The next object is
`ADDRESSABLE_TWO_VALUED_REFERENCE_STREAM`.  Constitutional delta: zero.
