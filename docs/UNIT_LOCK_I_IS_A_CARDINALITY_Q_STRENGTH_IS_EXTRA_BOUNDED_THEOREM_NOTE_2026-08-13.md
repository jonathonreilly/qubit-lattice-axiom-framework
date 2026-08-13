---
claim_id: unit_lock_i_is_a_cardinality_q_strength_is_extra_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a finite window, a unit-lock pattern is a partial map from sites to a menu of admissible local possibilities. The Record scalar I of that pattern, read as the count of locked sites, is the nonnegative integer cardinality of the domain. A Q-valued per-lock strength sum is a separately displayed extra dictionary: it recovers the cardinal readout when every strength is 1, and it differs from that readout on one lock when every strength is 3/2. The axiom memo names content-only additive I and does not name a rational strength. The extra dictionary is displayed, not adopted, not installed as Newton mass, and not used to force r=1/2 or adopt L_phys."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unit_lock_i_is_a_cardinality_q_strength_is_extra_2026_08_13.py
---

# Unit-Lock I Is A Cardinality; A Q-Valued Strength Is Extra

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite-window readout typing for unit locks under the
current Record wording.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unit_lock_i_is_a_cardinality_q_strength_is_extra_2026_08_13.py`](../scripts/unit_lock_i_is_a_cardinality_q_strength_is_extra_2026_08_13.py)

## Result Up Front

The current Record axiom supplies a scalar readout `I` of record *content*,
additive on finite pairwise-disjoint collections, with `I(empty)=0`. A record
locks exactly one admissible local possibility.

On a finite window that fact is a cardinality. A unit-lock pattern is a
partial map from sites to a menu. The cardinal readout

`I_#(L) := |dom(L)|`

is a nonnegative integer. One lock has `I_#=1`. Two disjoint locks have
`I_#=2`. The empty pattern has `I_#=0`.

A per-lock rational strength

`I_q(L) := sum_{x in dom(L)} q_x`, `q_x in Q_{>0}`,

is an extra dictionary. The trial `q_x=1` recovers `I_#`. The trial `q_x=3/2`
gives `3/2` on one lock and `3` on two locks, so `I_q != I_#` already at one
lock. The axiom memo does not name that dictionary.

This note displays `I_q`. It does not adopt `I_q`, does not install it as
Newton mass, and does not claim that `I_#` is insufficient for a later
dictionary. It does not force `r=1/2` and does not adopt `L_phys`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The cardinal identities and the 3/2 strength mismatch are exact finite-set arithmetic on declared lock patterns. The Q-valued strength remains a displayed extra dictionary, not an adopted primitive or a Newton-mass identification."
trace_class: negative_route_pruning
target_claim_id: record_unit_lock_cardinal_readout
target_blocker_text: "a Q-valued per-lock strength is extra to axiom I"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for I_# on finite unit-lock patterns and for the displayed I_q trials; adoption remains open"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `W` be a finite window of lattice sites and let `M` be a finite menu of
admissible local possibilities. A **unit-lock pattern** is a partial map

`L : W ⇀ M`.

The domain `dom(L)` is the finite set of sites that carry a record. Each value
`L(x)` is the unique locked menu entry at that site. This is the Record
sentence that a record locks exactly one admissible local possibility, read on
a finite window: one site, one lock, one menu entry.

The **cardinal readout** is

`I_#(L) := |dom(L)| ∈ Z_{>=0}`.

A **strength assignment** is a family `q_x ∈ Q_{>0}` indexed by `dom(L)`. The
**strength readout** is

`I_q(L) := sum_{x in dom(L)} q_x ∈ Q_{>0} ∪ {0}`,

with the empty sum equal to `0`. Two trials are used below:

1. `q_x = 1` for every `x` in `dom(L)`, which recovers `I_#(L)`;
2. `q_x = 3/2` for every `x` in `dom(L)`, which multiplies the cardinality by
   `3/2`.

Two patterns are **disjoint** when their domains are disjoint. Their
disjoint union is the partial map whose domain is the set-union of the
domains and whose values agree with each summand on that summand's domain.

The current Record wording, quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), is:

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.
>
> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

That is the entire load-bearing parent. No pairing table, Born weight, Newton
kernel, or unmerged branch is used.

## Theorem 1 — Cardinal `I` On Unit Locks

Let `L_1` be a pattern with `|dom(L_1)|=1` and let `L_2` be a pattern with
`|dom(L_2)|=1` whose domain is disjoint from `dom(L_1)`. Let `L_emptyset` be
the empty partial map.

Then

`I_#(L_1) = 1`,

`I_#(L_1 ⊔ L_2) = |dom(L_1) ∪ dom(L_2)| = 1 + 1 = 2`,

and

`I_#(L_emptyset) = 0`.

If `L` and `L'` are any two disjoint unit-lock patterns on the same window,

`I_#(L ⊔ L') = |dom(L)| + |dom(L')| = I_#(L) + I_#(L')`.

So finite additivity and `I(empty)=0` hold for `I_#`. For unit locks the
Record scalar is the cardinality of the locked-site set.

## Theorem 2 — The `q=3/2` Strength Trial Differs From `I_#`

Keep the same one-lock and two-lock patterns. Assign the constant strength
`q_x = 3/2`. Then

`I_q(L_1) = 3/2`,

`I_q(L_1 ⊔ L_2) = 3/2 + 3/2 = 3`.

In particular

`I_q(L_1) = 3/2 ≠ 1 = I_#(L_1)`.

The same strength dictionary with every `q_x=1` recovers the cardinal
readout:

`I_{q=1}(L) = sum_{x in dom(L)} 1 = |dom(L)| = I_#(L)`.

The two trials therefore separate a displayed extra dictionary from the
integer count. The hostile predicate

`I_q(one lock) = I_#(one lock)` for `q=3/2`

is false.

## Theorem 3 — Record Names Content-Additive `I`, Not A Per-Lock Strength

The quoted Record sentences name:

- formation and unit locking of one admissible local possibility;
- one-record-per-site uniqueness and permanence;
- readability of records only;
- content-only determination of a readout value;
- finite additivity of a scalar `I` on pairwise-disjoint records, with
  `I(empty)=0`.

They do not name a family `q_x ∈ Q_{>0}`, a sum of those values, or any other
Q-valued per-lock strength. The axioms state only their named primitive
content. Therefore `I_q` is extra to the axiom memo. It is a separately
written dictionary on the same finite patterns, not a clause of Record.

## Theorem 4 — Display `I_q`; Do Not Adopt It

The `q=3/2` trial is exhibited so that the extra dictionary is visible as a
distinct rational-valued map. Displaying it is not adopting it.

This note does not:

- register `I_q` as an approved primitive;
- replace axiom `I` by `I_q`;
- install `I_q` as Newton mass, a source coefficient, or a force-law weight;
- claim that `I_#` is insufficient for a later dictionary.

A later retained dictionary may or may not use a rational strength. That
decision is not made here. Cardinal `I_#` remains a well-defined Record
readout of unit-lock content.

## Theorem 5 — Do Not Force `r=1/2`; Do Not Adopt `L_phys`

Nothing in Theorems 1--4 selects a radial exponent, a continuum length, or a
physical-path parameter. In particular this note does not force `r=1/2` and
does not adopt `L_phys`. Those symbols, if they appear in other rows, remain
outside this claim.

## What This Does Not Claim

- It does not edit the axiom memo.
- It does not identify Born weights with `I`.
- It does not construct a pairing table or a two-argument product on `I`.
- It does not claim that every later dictionary must stay integer-valued.
- It does not claim that `I_#` is insufficient for a later dictionary.
- It does not install a Newton mass, a force law, `r=1/2`, or `L_phys`.

## Exact Target And Obligation Graph

**Exact target.** On finite unit-lock patterns, identify axiom `I` with the
domain cardinality and exhibit a Q-valued strength as an extra dictionary
that is recovered at `q=1` and that differs from the cardinality at `q=3/2`.

| Obligation | Role | Disposition |
|---|---|---|
| one lock has `I_#=1` | Theorem 1 | proved by `|dom|=1` |
| two disjoint locks have `I_#=2` | Theorem 1 | proved by disjoint-union cardinality |
| `I_#(empty)=0` and additivity | Theorem 1 | empty set and disjoint union |
| `I_q` at `q=3/2` is `3/2` and `3` | Theorem 2 | exact rational sum |
| `3/2 ≠ 1` at one lock | Theorem 2 | exact inequality |
| `q=1` recovers `I_#` | Theorem 2 | counting sum |
| axiom does not name `q_x` | Theorem 3 | quoted Record wording |
| display without adoption | Theorems 4--5 | explicit non-claims |

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record sentences | parent | quoted from the axiom memo |
| finite partial maps and disjoint union | Theorem 1 | definition-level mathematics |
| `Q_{>0}` sums with `Fraction` | Theorem 2 | exact arithmetic here |
| per-lock strength dictionary `I_q` | displayed extra | not axiom content; not adopted |
| Newton mass, `r=1/2`, `L_phys` | non-claims | not used, not forced, not adopted |
| observations or fitted couplings | none | not used |

## Review Record

Independent audit remains required before any effective status may change.
No axiom file is edited. No runner cache, citation manifest, or ledger
surface is written by this row.
