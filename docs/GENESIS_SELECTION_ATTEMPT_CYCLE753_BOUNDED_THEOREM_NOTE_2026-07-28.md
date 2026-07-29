# Genesis-word selection — minimality derived, the residual counted — Cycle 753

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle753_genesis_selection_attempt_2026_07_28.py`](../scripts/frontier_cycle753_genesis_selection_attempt_2026_07_28.py)
- [`frontier_cycle753_selection_independent_check_2026_07_28.py`](../scripts/frontier_cycle753_selection_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

W1's last declared item was the genesis word's *selection*: Cycle 732
derived its correctness, but the word itself was a convention. This
cycle asks whether selection reduces to minimality — and gets a
quantified answer:

- **27 is proven minimal**: an exhaustive pruned search (four pruning
  rules, each with a safety proof — one-bit-per-gate weight bound;
  minimum-length monotonicity; free C₁₁ translation action;
  commutation/Prüfer quotient completeness) finds **zero lawful words
  at every length 0–26**. The independent checker re-proved all four
  pruning rules with its own arguments and validated the pruned
  census against an unpruned brute-force window;
- **the minimal stratum is counted exactly**: at length 27 the raw
  translated-word orbit has
  1,304,242,256,990,794,732,881,944,806,061,811,799,701,848,064,000,000,000
  members, collapsing under the declared commutation/translation
  equivalences to
  **42,277,452,950,578,284,263,485,622,772,148,731,904 minimal
  classes** — both integers recomputed independently by the checker
  from the symmetry-group arithmetic;
- **the landed word is anchored**: the Cycle-732 word has length 27
  and sits in the minimal family at a determined Prüfer rank;
- **the outcome is B**: selection is not eliminated but *reduced and
  measured* — what remains supplied is exactly **one base-28 Prüfer
  rank among the enumerated minimal classes**. The convention shrinks
  from "a 27-gate word" (a free choice in a space of ~10⁵⁷) to "one
  rank in a counted class family" — with minimality itself now a
  theorem, not a preference.

## Supplied / derived / open

### Supplied

- the one Prüfer rank (the residual selection convention, exactly
  quantified); the declared gate alphabet and register layout;
  everything the Cycle-732 lineage declares.

### Derived

- minimality of 27 (exhaustive, pruning-validated); the complete
  minimal-class census with exact counts; the landed word's anchor and
  rank; the four pruning-safety proofs (independently re-proven).

### Open

- whether any further landed structure distinguishes one minimal class
  (which would retire the rank too — no candidate identified at this
  scope); everything inherited at original scopes.

## Negative-claim discipline

No negative claim ships. The residual rank is a measured convention,
not a wall; nothing here claims the rank underivable.

## Verdict

W1's final supply line is now a number: one rank among
4.2 × 10³⁷ counted minimal classes, in a space where minimality itself
is proven. For the axiom conversation this is the intermediate case
between derivation and missing content — the axioms force the length
and the class structure, and leave exactly one enumerated choice.
Independent audit still required.
