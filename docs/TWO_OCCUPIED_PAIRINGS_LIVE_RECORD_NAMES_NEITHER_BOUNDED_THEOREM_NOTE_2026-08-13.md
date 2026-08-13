---
claim_id: two_occupied_pairings_live_record_names_neither_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On two disjoint occupied unit locks, a supplied product pairing B_π fills the four occupied-pair cells by (0,0,0,1) and a supplied count-add pairing B_+ fills the same cells by (0,1,1,2). They disagree at the occupied-occupied cell 1≠2. Live Record names only records readable, content-alone readout, and blank unreadability. It does not name a two-argument map and does not name B_+ as axiom content. Both tables are extras. Neither π nor a J-field pairing is adopted. Named additive I is not restored."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_occupied_pairings_live_record_names_neither_2026_08_13.py
---

# Two Occupied Pairings; Live Record Names Neither

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact four-cell comparison of two supplied pairings on occupied
unit-lock collections against the live Record wording.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_occupied_pairings_live_record_names_neither_2026_08_13.py`](../scripts/two_occupied_pairings_live_record_names_neither_2026_08_13.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Take two disjoint occupied unit locks `s` and `t`. The four pairs of occupied
collections are

```text
(∅,∅), (∅,{t}), ({s},∅), ({s},{t}).
```

A *supplied* product pairing `B_π` fills those cells by `(0, 0, 0, 1)`. A
*supplied* count-add pairing `B_+` fills the same cells by `(0, 1, 1, 2)`.
At the occupied-occupied cell,

```text
B_π({s},{t}) = 1 ≠ 2 = B_+({s},{t}).
```

Live Record names neither table. The live axiom text says that only records
are readable, that a readout value is determined by record content alone, and
that a site with no record cannot be read. It does not name a two-argument
map. It does not name `B_+` as axiom content. Named additive `I` is not
axiom content.

Both tables are extras. They are displayed. This note does not adopt `π`.
It does not pair on a `J` field. It does not restore `I` as an axiom. It
does not install `G_N` or `1/r`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two supplied four-cell tables are exact Fractions; their occupied-occupied disagreement is 1≠2; live Record is quoted and names neither a two-argument map nor B_+; both tables remain extras."
trace_class: negative_route_pruning
target_claim_id: two_occupied_pairings_live_record_names_neither
target_blocker_text: "even a supplied count-pairing and a product-pairing are both extra; live Record names neither"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the four occupied-pair cells; no pairing axiom, J-field pairing, or named I is adopted"
hypothetical_axiom_status: "no pairing axiom is adopted, recommended, or edited; named I is not restored"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Quoted Live Record

The live Record axiom, from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), is used only
for its readable-content wording:

```text
Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.
```

That wording names no two-argument map of occupied collections. It names no
count-add pairing `B_+`. It names no product pairing `B_π`. A blank site is
unread; it is not assigned a scalar pairing value.

The same memo states that finite additivity, a named scalar collection
functional `I`, and an assigned value `I(empty)=0` are not Record axiom
content. The live Record body therefore does not contain `I(empty)=0`. The
predicate “live memo contains `I(empty)=0`” fails.

## Exact Objects

Let `s` and `t` be two occupied unit locks, treated as disjoint. The four
*occupied collections* they generate are `∅`, `{t}`, `{s}`, and `{s} ∪ {t}`.
The four *pairs of occupied collections* are the ordered pairs

```text
(∅, ∅), (∅, {t}), ({s}, ∅), ({s}, {t}).
```

The **product pairing** `B_π` is a supplied extra two-argument table on
those four pairs, *not* axiom content:

```text
B_π(∅, ∅) = 0,
B_π(∅, {t}) = 0,
B_π({s}, ∅) = 0,
B_π({s}, {t}) = 1.
```

Equivalently, on these unit locks, `B_π(S, T) = |S| |T|`. Displayed as a
2×2 with rows `{∅, {s}}` and columns `{∅, {t}}`:

```text
        ∅     {t}
∅       0      0
{s}     0      1
```

The **count-add pairing** `B_+` is a supplied extra two-argument table on
the same four pairs, *not* axiom content. It is count-add on occupied sets:

```text
B_+(∅, ∅) = 0,
B_+(∅, {t}) = 1,
B_+({s}, ∅) = 1,
B_+({s}, {t}) = 2.
```

Equivalently, `B_+(S, T) = |S| + |T|`. Displayed on the same 2×2:

```text
        ∅     {t}
∅       0      1
{s}     1      2
```

All displayed scalars are exact rationals (`Fraction` in the runner). Identity
gates call `B_pi(S, T)` and `B_plus(S, T)`.

Neither table is a pairing on a `J` field. The arguments are occupied
collections of unit locks, not a site-indexed field.

## Theorem 1 — The occupied-occupied cells disagree

**Statement.** `B_π({s},{t}) = 1 ≠ 2 = B_+({s},{t})`.

**Proof.** The supplied product table assigns the occupied-occupied cell
`B_π({s},{t}) = 1`. The supplied count-add table assigns the same cell
`B_+({s},{t}) = 2`. Those are different rationals. Cellwise:

| cell | `B_π` | `B_+` | equal? |
|---|---:|---:|---|
| `(∅, ∅)` | `0` | `0` | yes |
| `(∅, {t})` | `0` | `1` | no |
| `({s}, ∅)` | `0` | `1` | no |
| `({s}, {t})` | `1` | `2` | no |

Three of four cells disagree. In particular the occupied-occupied cell is
`1 ≠ 2`. The predicate `B_π == B_+` is therefore false.

## Theorem 2 — Live Record names neither map

**Statement.** Quote live Record. It does not name a two-argument map and
does not name `B_+` as axiom content.

**Proof.** The quoted live Record sentences are:

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

Those sentences mention records, readability, content-alone determination,
and unreadability of a blank site. They do not introduce a symbol for a map

```text
(occupied collection, occupied collection) ↦ scalar
```

and they do not assign values to the four ordered pairs. In particular they
do not name `B_+` and they do not name `B_π`. The memo's Record body does
not contain `I(empty)=0`, and it states that a named scalar collection
functional `I` is not Record axiom content. So `B_+` is not a live-axiom
rewrite of `I`, and it is not axiom content.

## Theorem 3 — Both tables are extras

**Statement.** Both tables are extras. Display them. Do not adopt `π`. Do
not pair on a `J` field.

**Proof.** Theorem 1 displays both four-cell tables and their disagreement.
Theorem 2 shows that live Record names neither table. A table that is not
named by the live axiom, and is not a retained derivation, is extra. The
product table `B_π` is therefore extra. The count-add table `B_+` is
therefore extra. Displaying them does not adopt them.

This note does not adopt `π`. It does not promote `B_π` or `B_+` to axiom
content. It does not pair on a `J` field: the displayed arguments are
occupied collections of unit locks, not values of a site-indexed field `J`.
Named additive `I` is not restored.

## Mutation

Two predicates must fail.

1. The predicate `B_π == B_+` must fail. By Theorem 1 it fails at
   `({s},{t})`, where the values are `1` and `2`. The runner evaluates that
   predicate by calling `B_pi` and `B_plus`.
2. The predicate “live memo contains `I(empty)=0`” must fail. By the quoted
   live Record body, that string is absent from the live Record section.

Identity gates call `B_pi(S, T)` and `B_plus(S, T)` rather than substituting
a hardcoded four-tuple in place of the pairing constructors.

## Non-Claims

This note does not:

- adopt, recommend, or edit a pairing axiom;
- adopt `π` or the product table `B_π`;
- adopt the count-add table `B_+`;
- pair on a `J` field;
- restore named additive `I` as axiom content;
- claim Newton, a force law, or a gravitational coupling;
- install `G_N` or `1/r`;
- identify occupied-lock counts with physical masses;
- depend on an empty/unit I-table versus `T_π` comparison;
- depend on a multiplicative retype of `I`.

Both supplied pairings remain extras.

## Verification

Run:

```bash
python3 scripts/two_occupied_pairings_live_record_names_neither_2026_08_13.py
```

Expected closeout includes `TOTAL: PASS>=12 FAIL=0`, identity gates that call
`B_pi` and `B_plus`, a failing equality predicate `B_π == B_+`, and a failing
predicate that the live memo contains `I(empty)=0`.
