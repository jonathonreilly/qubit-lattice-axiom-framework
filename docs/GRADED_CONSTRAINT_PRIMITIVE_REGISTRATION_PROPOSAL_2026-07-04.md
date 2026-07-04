# Owner One-Pager: Graded-Constraint Primitive Registration (Draft)

**Date:** 2026-07-04
**Type:** meta (primitive registration draft; no theorem claim)
**Authority class:** Class D proposal per
`docs/audit/DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md`. This document carries
no weight until you act on it; cite only as proposed.
**NOT AT APPROVAL GRADE (2026-07-04 owner correction).** An earlier cut of
this pager presented the full clause block as approval-ready text. That
bundled two different kinds of content: new supplied structure (approvable,
eventually) and interface claims about the landed axioms (reads — never
approvable; they must arrive as bounded notes that pass audit, conditional on
the core). This cut separates them. The owner approval, when it comes, is the
thin last act: the core only, after the interface notes and warrant filings
have passed audit.

## The eventual decision

Whether to register one approved primitive: **record influence on possibility
menus comes in degrees.** What would be approved is the CORE below and
nothing else.

## The core (the only eventually-approvable text)

> **graded_constraint.** For record-conditioned menus of admissible
> possibilities, a weight function `w >= 0` exists with `w(0) = 0`,
> `w(identity) = 1`: normalized on each menu, additive over exclusive
> alternatives, non-contextual across embedding menus, and defined on the
> full projection lattice of every nearest-neighbor composite, with every
> finite orthogonal resolution of the composite identity menu-eligible. No
> rate, propagation rule, orientation, scale, or record-production rule is
> supplied.

The composite-domain sentence is supplied structure (it uses adjacency; it
does not reinterpret it). Everything else the old draft carried moves below,
into the audit pipeline.

## Superseded draft framing (kept for the record)

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

The clause block above is the superseded bundle. Its interface clauses
(conditioning, coexistence, entangled elements) are NOT registration text:
they are claims about how the core sits with Admissibility and Record, and
each must be derived and audited as a bounded note conditional on the core:

- **Note target N1 (coexistence):** conditional on the core, grading is
  supported on available possibilities only, and Admissibility's availability
  is unaltered — consistency theorem against the landed Admissibility
  sentences.
- **Note target N2 (conditioning interface):** the record-conditioning of
  menus and weights uses the nearest-neighbor channel and leaves eligibility
  configuration-independent — consistency theorem against the landed
  neighbor-variation sentence; the record-conditioning itself is core supply,
  not a read.
- **Note target N3 (entangled elements):** `w` defined on composite
  projections while lockable record content stays site-local — consistency
  theorem against "a record locks exactly one admissible local possibility"
  and "Only records are readable."
- **Filing target N4 (warrants):** the two observed facts below enter as
  empirical-constraint rows through the audit lane (the recorded-branch
  filing pattern), replacing prose warrants.

These four targets are the specification obligations extracted from the
closed, unmerged Born-form bridge review in PR #4916. That PR is historical
input only; any live use must arrive as a fresh, self-contained conditional
note through the review/audit channel.

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

## What it would target after review/audit

- **Born form as a conditional theorem target, not a postulate:** a fresh
  composite-Gleason bridge note would need to show that the quadratic form is
  the unique consistent grading, with the dimension-2 loophole voided by the
  bonded-pair domain clause.
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
  non-quadratic gradings; the closed PR #4916 review indicated that composites
  are the route to refutation, but that route still needs a live, audited note.
  A weakened registration buys almost nothing.
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

## Pipeline to approval grade (in order)

1. A fresh, self-contained Born-form conditional note lands, carrying the core
   as a named conditional premise and incorporating the useful PR #4916 review
   lessons without depending on that closed branch.
2. N1-N3 consistency notes drafted, seat-refuted, landed; N4 empirical
   constraints filed through the audit lane.
3. Audit passes over that surface.
4. Downstream work references the audited notes, carrying the core as a
   named conditional premise. Registration stays available as an owner supply
   act for the moment some lane needs the premise unconditional to close a
   physical number; no work blocks on it.

Recommendation: run the derivations, submit them for review and audit, and
reference them. No approval is requested or scheduled.
