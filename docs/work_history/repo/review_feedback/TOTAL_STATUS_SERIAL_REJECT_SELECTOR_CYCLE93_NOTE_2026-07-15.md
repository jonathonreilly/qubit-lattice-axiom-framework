# Total-Status Serial-Reject Selector — Cycle 93

**Date:** 2026-07-15  
**Authority:** none  
**Status:** exact supplied-harness decision primitive; candidate transport remains open  
**Constitutional effect:** none

Companion runner:

```text
scripts/total_status_serial_reject_selector_cycle93_2026_07_15.py
```

## Result

The corrected 48-bit comparator no longer has to go silent at the first
mismatch. Its physical certificate spine can carry a total status:

```text
H1 = every bit seen so far agrees
H0 = at least one bit seen so far disagrees.
```

At each bit the next certificate is `H1` exactly when the previous certificate
is `H1` and the two current bits agree. Otherwise it is `H0`. The eight local
truth assignments collapse to six canonical strict-nearest-neighbor rows and
144 proper-cubic raw rows. Forty-eight raw rows are the existing equality rows
with the same `H1` output.

The final cell is guarded by the already-live `ALL` record and one fixed `H0`
blocker. A terminal `H1` writes the first bit of the associated output program
and starts the existing Cycle-90 writer. A terminal `H0` writes the already-live
`AUX` content instead. The output writer cannot consume `AUX`, so a rejected row
stops physically.

The corrected live, binary, comparator, writer, EMPTY, status, and final-cell
union has 5,680 raw inputs and no output conflict.

## Exhaustion

Every one of the 236 live programs was compared with itself and written through
the complete output pipeline:

```text
states                    15,576
append edges              15,340
exact terminals              236
wrong or parasitic writes      0.
```

All 11,328 one-bit perturbations write `AUX` and then stop. The runner also
checks all 55,460 ordered unequal pairs of the 236 selected programs; every
pair writes exactly one `AUX` reject record and the post-reject state is quiet.
That selected-pair corpus has first differences at 26 of the 48 positions;
the separate one-bit perturbation corpus exercises all 48 mismatch positions.
Ninety-six proper-cubic/translated controls are exact.

This removes the logical need to fan one candidate stream out to 236 complete
comparators. A physical serial selector may compare one reference, consume the
`AUX` rejection token, move the same candidate to the next reference, and stop
at the unique `H1` match.

## Exact boundary

Cycle 93 does not yet build that moving selector. The exact residual is:

```text
AUX_GATED_CANDIDATE_TRANSPORT
```

Starting from `AUX`, copy or route the same validated 48-bit candidate to the
next supplied reference without changing bit order, exposing an unintended
writer port, or crossing the permanent rejected-prefix record. Repeat through
the finite reference bank and bind the unique match to its output word.

The `ALL/AUX` final cage is supplied. The candidate/reference streams, writer
cage, and reference bank are supplied. Seed growth, physical bank layout, and
multi-front contact remain separate work. This is a decision primitive, not a
complete selector, autonomous macrostep, selected physical law, or TOE.

No foundation edit, registry edit, queue edit, audit verdict, or commit is
made. No axiom addition follows from this finite physical selector primitive.

## No-Go Discipline Gate

No universal no-go or minimum is asserted. The narrow positive result and its
unbuilt transport edge are stress-tested below.

### N1 — alternative routes

1. **ATTEMPTED:** 236 parallel equality comparators work only with supplied
   candidate fanout; they do not retire transport.
2. **ATTEMPTED:** the original all-binary Cycle-87 Patricia gate is exact in
   isolation but produces mixed-pipeline parasites.
3. **ATTEMPTED:** a live-guide re-cage repairs that local gate and remains a
   live Patricia-embedding route.
4. **ATTEMPTED:** the total-status chain here replaces quiet mismatch with one
   physical reject token and passes the full selected-pair corpus.
5. **RULED OUT BY SCOPE:** a host-language trie classifies programs but is not
   a lattice construction until its bit bus and nodes are physical records.

### N2 — wall independence

`AUX_GATED_CANDIDATE_TRANSPORT` precedes physical reference-bank iteration;
bank iteration precedes seed-grown placement. They are a dependency chain, not
three inflated independent walls. Nearby-front contact is independent of this
single-selector path and remains in the separate Cycle-84/Cycle-91 ledger.

### N3 — hidden-wall scan

The streams, reference bank, writer program, `ALL/AUX` cage, and placement are
explicitly supplied. “Serial” names the intended next construction and is not
treated as already physical. No background axis is used by a row: the cage is
closed under all proper-cubic rotations.

### N4 — residual matching

Cycle 82's `CANDIDATE_FANOUT_TO_198_PROGRAMS` and the live Cycle-90
`SERIAL_PROGRAM_SELECTION` concern the same row-selection interface. Cycle 87
addresses one-bit branching but not candidate transport. Cycle 93 closes only
the match/reject decision and cites neither recurrence nucleation nor clock,
probability, matter, or gravity as if they were this transport residual.

### N5 — rhetoric audit

The result is finite and exact for the corrected 236-program bank. It does not
say every finite selector has this cost, every unknown 48-bit word rejects, or
that a physical serial layout exists merely because the status automaton does.

### N6 — partial-closure paths

The transport edge can be retired by a caged copy cable, a seed-grown Patricia
bus, a different spatial bank layout, or a monolithic macrocell. All are local
law/compiler routes. None requires a new axiom or primitive merely because it
has not yet been built.

### N7 — hostile steelman

A hostile reviewer should say that the live-guide Patricia repair may be much
smaller than copying a 48-bit candidate past as many as 235 rejects, and that
the permanent H0/AUX trail may obstruct the next comparator. That objection is
correct: Cycle 93 proves the decision automaton and its mixed safety, not the
transport geometry. The next cycle must compare the routes physically.

### N8 — cross-cycle echo

Cycles 55, 78, and 85 repeatedly retired supplied-boundary walls by separating
a finite launcher-last builder from a recurrent core. The same pattern is
available here: first construct one AUX-gated transport cell, then prove a
finite repeating or bank-indexed induction. The prior successes keep the route
open; they do not count as this missing construction.

**Gate outcome:** PASS for the narrow positive decision primitive. No selector
or constitutional no-go ships.

## Verification

```text
python3 scripts/total_status_serial_reject_selector_cycle93_2026_07_15.py
```
