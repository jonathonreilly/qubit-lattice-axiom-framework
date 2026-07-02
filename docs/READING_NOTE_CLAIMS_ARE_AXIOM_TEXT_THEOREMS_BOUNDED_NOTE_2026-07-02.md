# Four Policy Reading-Note Claims Are Axiom-Text Theorems

**Date:** 2026-07-02
**Type:** bounded theorem (definitional derivations; reading-note retirement support)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note writes no audit
verdict, sets no audit status, and forecasts no audit outcome.
**Primary runner:** [`scripts/frontier_reading_note_derivations_2026_07_02.py`](../scripts/frontier_reading_note_derivations_2026_07_02.py)
**Runner output:** [`outputs/frontier_reading_note_derivations_2026_07_02.txt`](../outputs/frontier_reading_note_derivations_2026_07_02.txt)

## Purpose

The owner rule of 2026-07-02 — no rulings, only clarity — requires that
semantic content carry premise weight only as axiom text or as derivation that
passes audit. Four claims currently recorded as citable reading notes in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6 are in fact theorems of the
current axiom text. This note derives them, so the corresponding reading notes
can be retired as load-bearing surfaces. Nothing here adds axiom content.

## Supplied Surface

All derivations use only `docs/MINIMAL_AXIOMS_2026-06-29.md` sentences:

> A site need not carry a record.

> When present, a record locks exactly one local possibility from the subset
> available at that site under Admissibility; the locked possibility is
> invariant under repeated readout.

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`.

> A state is a configuration of records.

> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

## T1 — A lock outside the available subset is not a record; statehood needs no separate admissibility check

Record text defines a record as locking exactly one local possibility *from
the subset available at that site under Admissibility*. An assignment locking
an unavailable possibility fails the definition — it is not a record. A
configuration containing such an assignment therefore contains a non-record,
and by "A state is a configuration of records" it is not a state. Hence
admissibility of states is definitionally inherited: no separate check is
axiom content. `[checks 1-3]`

## T2 — Per-site record uniqueness

Record text types the record as an optional per-site item: "A site need not
carry a record. When present, a record locks exactly one local possibility."
The option-carry syntax (absent, or present locking exactly one) leaves no
reading on which one site simultaneously carries two conflicting locks; a
two-lock assignment at one site is not an instance of the sentence's type.
`[checks 4-5]`

## T3 — The empty configuration is a state with zero readout

The empty configuration contains no non-record (vacuously), so it is a
configuration of records, hence a state. Its scalar readout is `I(empty)=0`
verbatim from Record text. `[checks 6-7]`

## T4 — The "supplied" disambiguation is carried by the axiom text

The law-discipline sentence says a law's "domain is a supplied condition";
the Admissibility axiom speaks of "nearest-neighbor conditions." The
qualifier "supplied" appears in the law sentence and not in the Admissibility
sentence — the disambiguation recorded in the reading note is a fact of the
text, not additional semantic content. `[checks 8-9]`

## Consequence

The four reading-note claims (statehood/admissibility inheritance; per-site
uniqueness; empty-state; "supplied" disambiguation) are theorem or text-fact
content and need no citable reading note. Retirement is recorded in the
policy section 6 entry of the same date; the historical entry text is
preserved unedited.

## Does NOT

- Does not add, amend, or reword any axiom or primitive.
- Does not touch the remaining semantic reading notes ("answer" typing,
  "condition" as predicate, the law-side naturality clause) — those are
  definitions pending the second promotion batch, not derivable.
- Does not relocate procedural audit content (done separately in the
  audit-loop skill).
- Does not set audit status; the independent audit lane is the only status
  authority.

## Dependencies

- [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
  (section 6, for the reading notes being retired; cited as target, not
  authority)

## No-Promotion Statement

This note does not promote, demote, or set the audit status of any
dependency. The independent audit lane is the only status authority.
