# AUX-gated candidate transport — Cycle 95

**Date:** 2026-07-15  
**Authority:** none  
**Status:** exact two-handoff, three-cell, supplied-apparatus construction  
**Constitutional effect:** none

Companion runner:

```text
scripts/aux_gated_candidate_transport_cycle95_2026_07_15.py
```

## Result up front

Cycle 95 constructs the bounded physical handoff that Cycle 93 named
`AUX_GATED_CANDIDATE_TRANSPORT`. It does not merely add a graph edge or copy a
Python tuple.

The live path is:

```text
candidate vs reference 0 (unequal)
    -> one AUX selector record
    -> four strict-NN 48-bit physical sweeps
    -> decoded H0/H1 candidate copy
    -> reverse 48-bit physical validation
    -> ALL
    -> physical acceptance cable
    -> candidate vs reference 1 (unequal)
    -> one AUX selector record
    -> three strict-NN 48-bit physical sweeps
    -> second decoded H0/H1 candidate copy
    -> reverse 48-bit physical validation
    -> ALL
    -> candidate vs reference 2 (equal)
    -> ALL
    -> exact 17-record selected output.
```

Every causal parent is a Manhattan-distance-one record. Every transported bit
is determined by a physically adjacent earlier H or tagged bit, and every tag
is one of the existing 153 live roles. No law row reads a coordinate, program
index, host tuple, or graph-only parent. All source and grown sites are
disjoint, and no record is overwritten.

For every one of the 236 selected 48-bit programs, the first two supplied
references are unequal and the third is the candidate itself. The exact live
runner exhausts all 681 states of each complete path:

```text
programs                                  236
states per complete protocol              681
all-program success states             160,716
transported copied bits checked         22,656
proper-cubic rotated states             16,344
wrong, missing, conflicting,
or parasitic live frontiers                  0.
```

The asynchronous result does not rely on a host update order. The physical
construction has exactly one enabled record at every nonterminal state, so
the complete legal single-record schedule set is a singleton and is exhausted
at every frontier. All 24 proper cubic images of the entire 681-state protocol
are exact.

## Corruption control

A transported-copy mismatch has different semantics from a reference
mismatch:

- a reference mismatch writes `AUX` and authorizes the next physical handoff;
- a copied-candidate mismatch writes one new validation `AUX` and has no live
  successor.

The runner attacks every one of the 48 copy positions in both handoffs, then
attacks an all-bits-flipped copy and a separated four-bit corruption. It also
attacks the terminal copied bit in both handoffs for all 236 programs. These
572 corruption cases traverse 261,404 exact states. Each wrong bit is injected
only after its site is uniquely enabled with the correct opposite law output;
the compiler never learns a row that makes the wrong bit. Each detector writes
exactly one new `AUX`, and the post-`AUX` live frontier is empty.

## Three failures found before the construction passed

The passing geometry is not the first diagram tried.

1. **Cycle-93 status-cage reuse failed.** On an unequal candidate/reference
   stream, several not-yet-reached status sites matched an old arity-four `H1`
   row. The failure was invisible to terminal-status bookkeeping but visible in
   the actual live frontier. Cycle 95 therefore does not inherit the status
   semantics by assertion. Both transverse sides of each status target now
   carry the existing `BACKSTOP` role, which is absent from every Cycle-93 input
   signature. The caged recurrence earns `H1` iff the prior status is `H1` and
   the current physical bits agree; otherwise it grows absorbing `H0`.
2. **A naked travelling token failed.** Reusing `T_G0` at an open endpoint
   activated old one- and two-neighbour propagation rows in transverse
   directions. The repaired cable alternates phase-typed existing `A_*` roles
   and occupies every unused cable neighbour with existing `LAUNCH_A` records.
3. **A graph-only validation parent failed.** The first draft named final-copy
   completion as a parent of a distant validation start. Its local signature
   could fire early because the named dependency was not a physical neighbour.
   The repair grows an actual `JOINT` turn beside the final decoded bit, grows
   validation START beside that turn, and carries the first `ALL` across a
   51-record nearest-neighbour acceptance cable before comparator 1 can start.

The new table has 123 canonical rows and 2,874 proper-cubic raw images. It is
raw-input-disjoint from Cycle 93's 5,680 rows. Their 8,554-row union is
single-valued.

## Supplied and grown state

The bounded apparatus is explicit:

```text
supplied records                           943
  H0/H1 candidate, references, harness    400
  copy guides T_G1                        240
  status guards BACKSTOP                  192
  cable shells LAUNCH_A                    97
  endpoint/decision guards                 14

grown records                              680
  three 48-status comparators              144
  seven 48-bit transport sweeps            336
  two 49-record validators                  98
  acceptance-carry records                  55
  launch/turn/cable records                 25
  selector/validation decisions              5
  final selected writer                     17.
```

The candidate, three references, writer harnesses, guide rails, status cages,
and cable shells are supplied. The statuses, `AUX/ALL` decisions, launch
records, every tagged and decoded transported bit, validation trails,
acceptance records, next-comparator starts, and final writer are grown by the
one mixed strict-nearest-neighbour table.

## Exact credit and boundary

Closed here:

```text
TWO_CONSECUTIVE_AUX_GATED_CANDIDATE_HANDOFFS
THREE_CONSECUTIVE_COMPARE_SELECT_CELLS
PHYSICAL_48_BIT_ORDER_PRESERVATION
COPY_MISMATCH_TO_ONE_AUX_AND_NO_ADVANCE
ALL_TO_NEXT_PHYSICAL_COMPARATOR_FRONT
```

Still open:

```text
GROWTH_OF_THE_943_RECORD_APPARATUS
PHYSICAL_INDUCTION_THROUGH_THE_COMPLETE_REFERENCE_BANK
NEXT_CELL_SELF_ALLOCATION_AND_RENEWAL
UNBOUNDED_OCCURRENCE_AND_GLOBAL_EXTENSION
MULTI_APPARATUS_CONTACT_OR_SEPARATION
```

The first four construction items form a dependency chain rather than four
independent axiom walls. Cycle 95 is a finite supplied-bank witness. It does not
claim a seed-grown selector, a 236-reference spatial bank, an arbitrary-length
induction, a complete compiler macrostep, a selected exact law, or a TOE.

## Bare-metal and axiom implication

This construction supports a specific bare-metal picture:

- a record is the permanent local append made when the exact local rule enables
  it;
- later records can copy, compare, validate, and decide whether another front
  may propagate;
- validation never overwrites or retroactively locks the earlier record; and
- causal order is the permanent nearest-neighbour trail, not a supplied clock.

Agreement is operationally important, but this probe does not make “two
witnesses” a universal formation criterion. The validator actually consumes
the original bit, the copied bit, a tagged trail, a prior status, and a supplied
cage. Nor does the probe derive a probability measure, a clock rate, matter,
gravity, or a storage-capacity law. Its finite record count makes resource cost
visible, but no conservation or saturation principle follows from that count.

Accordingly, no formation, read-lock, clock-lock, witness, storage-budget, or
probability sentence is forced into the axioms by Cycle 95. The construction is
evidence for placing the needed mechanism in the exact local law and proving
record persistence and downstream validation from that law. A constitutional
identity for the eventual complete law remains a downstream selection question,
not a consequence of this bounded compiler cell.

## No-Go Discipline Gate

No universal no-go is asserted. The following N1–N8 gate stress-tests the
bounded positive and prevents its supplied-state residuals from being promoted
into false impossibility or axiom claims.

### N1 — alternative route enumeration

1. **ATTEMPTED — reuse the Cycle-93 alternating H cage.** It fails the actual
   unequal-stream frontier by enabling early `H1` parasites; the retained
   terminal-only claim being extended is documented in
   `TOTAL_STATUS_SERIAL_REJECT_SELECTOR_CYCLE93_NOTE_2026-07-15.md:24-37,51-55`.
2. **ATTEMPTED — carry one old `T_G0` token through open space.** It branches
   transversely through inherited live rows; the Cycle-92 guide result already
   shows why a non-H cage is load-bearing
   (`LIVE_EMPTY_CAGED_ROUTER_PATRICIA_CYCLE92_NOTE_2026-07-15.md:24-40`).
3. **ATTEMPTED — name distant final-copy completion as a validation parent.** It
   fails because the dependency is not present in the target's six-neighbour
   signature; the `JOINT` turn and physical acceptance cable replace it.
4. **ATTEMPTED — caged, phase-tagged bit transport.** This is the successful
   route: two complete handoffs pass all236, every exact frontier, all24 cubic
   images, and the corruption corpus.
5. **RULED OUT BY PRIOR — host Patricia lookup as physical closure.** Cycle 92
   retains the trie only as a combinatorial inventory and explicitly leaves its
   bit bus and proper-cubic physical embedding open
   (`LIVE_EMPTY_CAGED_ROUTER_PATRICIA_CYCLE92_NOTE_2026-07-15.md:42-56`).
6. **RULED OUT BY PRIOR — completion pulse without value validation.** Cycle 94
   shows that completion alone is not value-faithful and requires literal
   post-write bit verification
   (`LIVE_SEED_ROW_READABLE_MACROSTEP_CYCLE94_NOTE_2026-07-15.md:99-127`).

### N2 — wall-independence audit

The raw residual list collapses as follows:

| pair | closing first closes second? | closing second closes first? | disposition |
|---|---|---|---|
| supplied apparatus / full-bank induction | no | no | distinct stages of one construction chain |
| full-bank induction / self-allocation-renewal | no | no | distinct stages of one construction chain |
| supplied apparatus / self-allocation-renewal | no | yes, if “self-allocation” includes the first cell | collapse into the self-grown-selector chain |
| self-grown-selector chain / unbounded occurrence-extension | no | no | downstream law/semantics stage, not a second Cycle-95 wall |
| self-grown-selector chain / multi-apparatus contact | no | no | independent top-level construction lane |

The collapsed Cycle-95 boundary is therefore one ordered
`SELF_GROWN_UNBOUNDED_SELECTOR_CHAIN` plus the separate
`MULTI_APPARATUS_CONTACT_OR_SEPARATION` lane. It is not five independent
missing axioms.

### N3 — hidden-wall scan

The runner and this note were searched for “we assume,” “by construction,” “as
is standard,” “the framework provides,” “bridge context,” “background,”
“naturally,” “obviously,” “standard QFT,” “registered,” and “canonical.” The
only load-bearing contextual nouns are the explicitly counted supplied rails,
cages, harnesses, and shell records. `Canonical` refers only to proper-cubic
signature equivalence. No hidden physical premise is credited as a theorem.

### N4 — residual matching

| cited witness | witness residual | Cycle-95 residual | match? |
|---|---|---|---|
| `TOTAL_STATUS_SERIAL_REJECT_SELECTOR_CYCLE93_NOTE_2026-07-15.md:63-79` | `AUX_GATED_CANDIDATE_TRANSPORT` | two bounded AUX-gated 48-bit handoffs | yes, bounded instance |
| `POST_CYCLE94_OPERATIONAL_COMPLETENESS_AUDIT_CYCLE96_NOTE_2026-07-15.md:180-191` | `STEP_SELECTOR_TRANSPORT` | mismatch, handoff, next comparator, bit order, no early writer | yes, first two handoffs only |
| `LIVE_DIRECTIONAL_PROGRAM_WRITER_CYCLE90_NOTE_2026-07-15.md:27-38` | `SERIAL_PROGRAM_SELECTION` | physical candidate transport | partial interface match only |
| `LIVE_EMPTY_CAGED_ROUTER_PATRICIA_CYCLE92_NOTE_2026-07-15.md:48-56` | physical Patricia embedding and seed growth | caged linear handoff | no; retained only as an alternative route |
| `LIVE_SEED_ROW_READABLE_MACROSTEP_CYCLE94_NOTE_2026-07-15.md:93-97` | validated output word to next logical front | candidate to next reference | no; cited only for architectural comparison |

The two “no” rows are not used as evidence that Cycle 95 closes transport.

### N5 — rhetoric audit

Tested resolutions are: each bit (all 48 positions), each selected program
(all236), each handoff (two), each consecutive compare cell (three), every
reachable finite state, and every proper-cubic image (all24). A complete
236-reference spatial bank, arbitrary cell count, unbounded recurrence, and
lattice-wide multi-apparatus behavior were not tested. Therefore the result is
phrased only as a two-handoff, three-cell supplied-apparatus construction.

### N6 — partial-closure paths

No new axiom is required to attack the residual. The current caged cable closes
the first bounded instance. Cycle 92 retains a physical Patricia embedding as a
potential smaller bank route. Cycle 94 supplies a value-faithful
output-to-next-front adapter. Cycle 96 classifies selector transport,
self-allocation, recurrence, and contact as theorem targets or exact-law fields,
not automatic constitutional atoms
(`POST_CYCLE94_OPERATIONAL_COMPLETENESS_AUDIT_CYCLE96_NOTE_2026-07-15.md:162-203`).

### N7 — hostile steelman

A hostile reviewer should say that 943 supplied records and a table compiled
against all236 programs can still be an elaborate finite interpreter, not a
self-hosting law of nature. The proof shows that the physical records enact the
handoffs without a host lookup once the apparatus exists; it does not show that
the official seed grows the apparatus, that the same finite interface allocates
an arbitrary next bank cell, or that a caged Patricia layout would not be much
smaller. That objection is correct. It blocks any claim of full-bank or
unbounded closure, but not the exact bounded live-frontier result.

### N8 — cross-cycle echo

Cycle 93 already records that Cycles 55, 78, and 85 retired supplied-boundary
walls by separating a finite launcher-last builder from a recurrent core
(`TOTAL_STATUS_SERIAL_REJECT_SELECTOR_CYCLE93_NOTE_2026-07-15.md:145-151`).
Cycle 94 similarly turns one actual seed-row endpoint into a 132-append readable
next-front path while retaining 472 supplied cell records
(`LIVE_SEED_ROW_READABLE_MACROSTEP_CYCLE94_NOTE_2026-07-15.md:73-97`). Those
examples keep the seed-growth and self-allocation routes open; they forbid a
no-go claim here.

**Gate outcome:** PASS for the narrow positive two-handoff construction and its
collapsed residual boundary. No universal no-go, minimum, law selection, or
axiom requirement ships.

## Verification

```text
python3 scripts/aux_gated_candidate_transport_cycle95_2026_07_15.py
```

Expected summary:

```text
45 PASS / 0 FAIL
```

No foundation, registry, queue, policy, audit state, Cycle-94 artifact, commit,
push, or PR is changed by this cycle.
