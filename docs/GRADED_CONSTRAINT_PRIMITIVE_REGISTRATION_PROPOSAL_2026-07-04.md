# Owner One-Pager: Graded-Constraint Primitive Registration (Draft)

**Date:** 2026-07-04
**Type:** primitive registration draft — Class D proposal per
`docs/audit/DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md`. This document carries
no weight until you act on it; cite only as proposed.

## The decision

Whether to register one approved primitive: **record influence on possibility
menus comes in degrees.**

## Draft registration text

> **graded_constraint.** For record-conditioned menus of admissible
> possibilities, a weight function `w >= 0` exists with `w(0) = 0`,
> `w(identity) = 1`, and:
> - **normalization** — weights on each menu sum to one;
> - **additivity** — `w(P + Q) = w(P) + w(Q)` for exclusive alternatives;
> - **non-contextuality** — `w(P)` does not depend on which menu embeds `P`;
> - **domain** — `w` is defined on the full projection lattice of every
>   bonded nearest-neighbor composite, and every finite orthogonal resolution
>   of the composite identity is menu-eligible;
> - **bonding** — every nearest-neighbor pair is bonded; adjacency is the
>   supplied structure that says which composites exist;
> - **conditioning** — menus and weights are conditioned by the surrounding
>   record configuration through the nearest-neighbor channel; eligibility
>   itself does not depend on the record configuration;
> - **coexistence** — grading lives on the available set: an unavailable
>   possibility is in no menu; availability (Admissibility) is untouched;
> - **entangled elements** — composite projections are constraint-bookkeeping
>   alternatives for weighting only; lockable record content remains
>   site-local admissible possibilities.
>
> No rate, propagation rule, orientation, scale, or record-production rule is
> supplied by this registration.

The four clauses bonding / conditioning / coexistence / entangled elements
answer exactly the specification obligations the adversarial seats extracted
from the Born-form bridge note (PR #4916).

## The physical warrant — two observed facts

1. **Identical menus, stably unequal frequencies.** A 70/30 beamsplitter
   presents the same admissible outcome set every run; the frequencies are
   reproducibly 70/30. Binary availability plus symmetry can only pay uniform
   weights on symmetric menus — the harvested r = 1/2 class. Degrees are the
   minimal expression of this fact.
2. **Correlated record statistics across neighboring sites** that no
   site-local weighting reproduces. Pair-level constraint influences record
   statistics, which is the only standard of physical reality the record
   interface offers — that is what the entangled-elements clause registers,
   and no more.

## What it buys immediately

- **Born form becomes forced, not postulated:** the composite-Gleason bridge
  note (PR #4916, stacked on #4915) shows the quadratic form is the unique
  consistent grading, with the dimension-2 loophole voided by the bonded-pair
  domain clause.
- **The r = 1/2 class returns as the zero-information limit** (uniform on
  symmetric menus) — consistency with landed results, no new selection.
- **Weight values become a derivation target from surrounding records** —
  your realized-measure principle — rather than a supplied table.

## What it deliberately does not supply

The composition/propagation rule of the grades (the carrier — a separate
registration, where interference and the Dirac-square shape live), stability,
rate, scale, orientation, and the record-production rule. Those stay at their
own ports.

## Honest flags

- The **domain clause is load-bearing at full strength**: without entangled
  resolutions being menu-eligible, a single `M_2` site admits explicit
  non-quadratic gradings (constructed and exactly refuted only via composites
  in PR #4916). A weakened registration buys almost nothing.
- The **entangled-elements clause is the novel ontology**: pair-level
  constraint bookkeeping with site-local locking. It is exactly what the
  correlated-statistics warrant supports — it does not make composite
  possibilities lockable and does not touch the Record axiom.

## Mechanics if approved

New approved-primitive node in `docs/audit/data/axiom_premise_nodes.json`
plus a policy-log entry, owner-approved. No axiom sentence is edited.
"No possibility is privileged... supplied algebraic structure alone" and
"Only records are readable" remain true as written: registration enlarges the
supplied structure, and the grading is knowable only through record
frequencies.

Recommendation: approve with or after PR #4916 lands, so the certification
chain is in place the day the primitive exists.
