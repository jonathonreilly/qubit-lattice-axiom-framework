# Promotion Value Gate — Cycle 704

Answered before the PR. Not an audit certificate; predicts no audit verdict.

## V1 — obstruction

Not an `audited_conditional` verdict this time but a **named open item in two
landed notes**, quoted verbatim:

> "Migrating-record semantics — OPEN. Bare permanence does not separately state
> site immobility."
> — `RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_..._2026-07-11`

> "A migrating-record semantics remains an untested alternative."
> — `ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_..._2026-07-13`

The cycle does not close the open item. It establishes that one whole class of
argument — readout — can never close it, and finds a consequence that holds
whichever way it closes.

## V2 — new derivation, with the sweep

**Searched commit `6959f21815`**, refreshed immediately before the sweep.

| # | command | hits | classification |
|---|---|---|---|
| M1 | `git grep -n -iE "migrat(ing\|ion).{0,40}record\|record.{0,40}migrat(ing\|ion)\|site immobil\|record mobility" origin/main -- 'docs/*.md'` | the two notes quoted above, plus a review-feedback census row listing "record identity and migration" as missing content | **the open item itself.** No note tests it. |
| M2 | `git grep -n -iE "readout.{0,50}(invariant\|blind).{0,30}(move\|position\|site)\|(move\|reposition).{0,40}readout unchanged" origin/main -- 'docs/*.md'` | one hit, my own landed cycle 698 note | **absence** of any application to migration |
| M3 | `git grep -n -iE "admissibility.{0,50}position\|position.{0,40}admissibility.{0,30}(sensitive\|depends)" origin/main -- 'docs/*.md'` | unrelated composition-law and instrument-law rows | **nonmatching** |
| F1–F4 | formable/reachability, "records form" bootstrap, formation-time vs revalidation, landed formation notes | the two 2026-07-04 bootstrap theorems and ~12 formation notes | **read before building.** The bootstrap notes already establish `A0` nonempty from "Records form" and the flip-closure of the reachable class; this cycle deliberately does not restate either. |

New content: readout-invisibility of migration; the vacated-origin count
asymmetry between the formation and migration gates; the strict-permissiveness
consequence; and the exhibition of the permanence-reading split on a single
move.

## V3 — could the audit lane already do this from retained primitives plus standard math?

The arithmetic is elementary — neighbour counts on a cubic lattice. What is not
available to the audit lane is the pairing: that the readout clause is blind to
position (hence cannot decide the open question) while the Admissibility clause
is not, and that the asymmetry between the two gates is created by the mover
vacating its origin. The corpus records the open item twice without testing it.

## V4 — non-trivial?

Yes, and one part of it corrected a genuine error. The first draft claimed the
two gates were the same predicate and "verified" it with two identical function
bodies over 2187 rules — a tautology, caught in self-review before submission,
withdrawn, and replaced by the geometric result that they differ by exactly one
neighbour for adjacent moves. The surviving claims each carry a control: M1 has
a content-change control, M2 has the non-adjacent contrast, M4 verifies the
starting configuration is admissible under both readings before the move.

## V5 — one-step variant?

**Checked against `origin/main` at `6959f21815`.** No. Against the landed
bootstrap theorems: those establish `A0` nonempty and flip-closure of the
reachable class; neither concerns migration, readout invariance, or the gate
asymmetry. Against landed cycles 698/699: those concern readout kernels and
couplings, with no formation or migration. Against this campaign's backlogged
cycles: 700 concerns closure of the admissible set under union and subset, not
motion of a record; 702's Part II was rejected partly for presuming a
revalidation semantics, and this cycle's M4 exists specifically to exhibit that
split rather than presume it.

**Verdict: PR allowed.**

## Owner direction

Built under the instruction to go after the formation rule and push the
frontier. It does not supply a formation rule and says so; it removes one class
of argument from contention and adds one constraint that survives either
resolution.
