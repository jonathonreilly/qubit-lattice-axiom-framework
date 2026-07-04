---
claim_id: record_comparability_conditional_chain_arrow_certification_bounded_note_2026-07-04
claim_type: bounded_theorem
claim_scope: "Conditional on the named extra premise 'There is one configuration of records.', realized record stages form one nested chain; with occurrence and permanence this gives order/direction/irreversibility along stages, but no clock, rate, formation rule, state selector, or weight."
upstream_dependencies:
  - minimal_axioms
  - record_comparability_not_derived_by_minimal_axioms_narrow_no_go_note_2026-07-04
runner: scripts/record_comparability_boundary_and_conditional_arrow_2026_07_04.py
---

# Conditional Comparability Certification: One Record Configuration Gives A Chain

**Date:** 2026-07-04
**Type:** bounded_theorem (conditional certification)
**Claim type:** bounded_theorem
**Scope:** conditional on the named extra premise "There is one configuration
of records." The sentence is not in the current axiom memo and is not consumed
as landed axiom content here.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/record_comparability_boundary_and_conditional_arrow_2026_07_04.py`](../scripts/record_comparability_boundary_and_conditional_arrow_2026_07_04.py)

## Conditional Premise

The current axiom surface is
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). The companion
no-go
[`RECORD_COMPARABILITY_NOT_DERIVED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-07-04.md`](RECORD_COMPARABILITY_NOT_DERIVED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-07-04.md)
pins why the conditional sentence is not already derived from that surface.

This note assumes, for the theorem only:

```text
There is one configuration of records.
```

Read precisely: realized record stages belong to one record configuration, so
any two realized configurations are comparable by inclusion. This is the named
comparability premise from the owner decision surface. It is not derived here,
not appended to the axiom memo, and not registered as a primitive.

## Certification

Let `R_i` and `R_j` be two realized record stages. By the conditional premise,
they are comparable:

```text
R_i subset R_j  or  R_j subset R_i
```

Therefore the realized stages form a chain under inclusion. Combined with the
landed Record sentences:

- "Records form.";
- "A site never carries more than one record";
- "records are permanent";
- "A state is a configuration of records";

any actual formation-successor strictly extends its predecessor. Thus along the
realized stages:

- order is inclusion order;
- direction is growth;
- irreversibility is non-removal/non-overwrite of records;
- simultaneous multi-record formation is still a chain jump, not a branch.

## What This Still Does Not Supply

The conditional sentence does not say:

- which admissible possibility a new record locks;
- which site receives a record;
- with what weight or probability a record forms;
- at what rate records form;
- what clock, time metric, or simultaneity convention applies;
- which state or history is selected among all model extensions;
- what Hamiltonian, transfer operator, measurement instrument, or
  record-production process implements formation.

The runner explicitly exhibits two different one-chain extensions,
`empty -> {x}` and `empty -> {y}`, both satisfying the conditional theorem.
That independence is the point: comparability supplies one-chain structure, not
a formation rule or selector.

## Relation To Tier-A Elimination

This packet retires no Tier-A admission. It prevents a false route: current
Record text does not already contain the comparability sentence. If an owner
act later supplies it, arrow-dependent rows can cite a bounded certification of
the chain consequence without smuggling clock/rate/formation-rule content.

The remaining genuine Tier-A derivation targets remain the two entries in
`docs/audit/data/tier_a_admissions.json`: `AC_phi_lambda` and `theta`.

## Verification

The companion runner checks the exact text needles, verifies the underivability
countermodel, checks chain/nesting consequences under the conditional premise,
and tests that multiple site-choice extensions remain valid.

Measured runner output:

```text
TOTAL: PASS=41 FAIL=0
```
