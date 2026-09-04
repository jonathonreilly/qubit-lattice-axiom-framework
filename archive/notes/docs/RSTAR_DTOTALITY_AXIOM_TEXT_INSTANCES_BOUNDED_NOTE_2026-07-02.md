---
claim_id: rstar_dtotality_axiom_text_instances_bounded_note_2026-07-02
claim_type: bounded_theorem
claim_scope: "Bounded support: the quoted R* finite-additivity/content-determination clauses and the quoted D-totality rule-domain clause are direct instances of current minimal-axiom Record and law sentences, checked on finite witnesses. This does not adjudicate sibling PRs, close any wall or gate, de-list any reading item, import a motion-closure theorem, or change axiom, primitive, policy, registry, audit, or publication surfaces."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
runner: scripts/frontier_rstar_dtotality_axiom_text_instances_2026_07_02.py
---

# R* And D-Totality Clauses As Axiom-Text Instances (Bounded Note)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Audit boundary:** independent audit lane only. This note sets no audit
verdict, predicts no audit outcome, and edits no audit-lane-owned data.
**Primary runner:**
[`scripts/frontier_rstar_dtotality_axiom_text_instances_2026_07_02.py`](../scripts/frontier_rstar_dtotality_axiom_text_instances_2026_07_02.py)
**Cached runner output:**
[`logs/runner-cache/frontier_rstar_dtotality_axiom_text_instances_2026_07_02.txt`](../logs/runner-cache/frontier_rstar_dtotality_axiom_text_instances_2026_07_02.txt)

## Firewall

This note is a bounded clause-mapping note. It does not adjudicate or de-list
any sibling PR, reading item, wall, or gate. It does not import a motion-closure
theorem or decide whether a pointwise, singleton, or narrowed domain is lawful.
Sibling PRs are context only, not dependencies.

The only landed authorities used as dependencies are:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)

## Clause Forms Considered

The bounded observation concerns two clause forms used by in-flight review
surfaces.

**R\*.** A registrable scalar readout is:

1. additive over finite pairwise-disjoint records, with `I(empty)=0`;
2. determined at fixed record content, so an unsupplied auxiliary choice such as
   an imported basis cannot change the value.

**D-totality.** A physical readout rule proposed as a law over a stated supplied
domain must give exactly one answer at every state in that stated domain.

These are the only clauses mapped here. Downstream finite witnesses, sibling
status, context selection, and wall status remain outside this note.

## Axiom Text Used

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

From
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md):

> Derivations may evaluate at the realized state, pointwise.

and:

> This is pointwise evaluation, not a state-selection rule.

## R* Mapping

R\* clause 1 is exactly the Record axiom's finite additivity sentence, with the
same empty baseline.

R\* clause 2 is the exclusion direction of the Record axiom's
content-determination sentence. If two unsupplied auxiliary presentations give
different scalar values while record content is fixed, then the value is not
determined by record content alone. The runner exhibits both sides on a finite
two-record choice orbit: the imported-basis readout varies and fails; the
record-content-only readout is orbit-constant and passes.

This does not prove a converse expressibility theorem. A scalar readout still
needs its own lawful definition; the axiom only bars value changes carried by
non-record auxiliary choices.

## D-Totality Mapping

D-totality is the law sentence applied to a rule's stated supplied domain. A
partial rule that is undefined at an in-domain state fails the requirement to
give exactly one answer. A rule that gives more than one answer at an in-domain
state fails the same requirement. A rule that gives one answer at every
in-domain state passes this clause.

This is a domain-relative statement. It does not prove that a proposed domain is
the full admissible surface, that a narrowed domain is lawful, or that any
particular readout context is supplied across a boundary.

## Realized-State Boundary

The realized-state primitive permits pointwise evaluation of an already-defined
state functional at the realized state. It does not supply a state-selection
rule or a domain certificate. Therefore "evaluate this lawful rule at the
realized state" and "make the realized state the rule's whole domain" are
different moves. This note checks only that boundary; it does not close the
pointwise-domain question.

## Does NOT

- Does not close, reopen, or rule on any wall, gate, or sibling PR.
- Does not de-list R\*, D-totality, or any reading item.
- Does not import or prove a motion-closure theorem.
- Does not assert a fully reading-free ladder.
- Does not touch `w`, CTX-match, context selection, or readout-supplier
  governance.
- Does not set, imply, or predict audit status for any row or PR.
- Does not add, rename, move, or register any axiom, primitive, policy, or
  registry content.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)

## No-Promotion Statement

This note promotes nothing. It records a bounded instance map from two clause
forms to landed premise text, leaving all adjudication and downstream status
changes to their proper lanes.
