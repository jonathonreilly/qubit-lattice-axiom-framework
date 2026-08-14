---
claim_id: occupancy_pairing_and_content_match_pairing_disagree_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On two disjoint occupied unit locks with unequal lock labels A and B, the supplied occupancy-product pairing equals 1 and the supplied content-match pairing equals 0. Live Record names each site's lock label, not a two-argument pairing of labels. Both tables are extras. Named additive I is not restored."
upstream_dependencies:
  - minimal_axioms
runner: scripts/occupancy_pairing_and_content_match_pairing_disagree_2026_08_14.py
---

# Occupancy Pairing And Content-Match Pairing Disagree

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact comparison of two supplied extra pairing tables on two
disjoint occupied unit locks. Live Record is quoted without rewrite. No
pairing is adopted. Named additive `I` is not axiom content and is not
restored. No two-argument map is read out of the axiom memo.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/occupancy_pairing_and_content_match_pairing_disagree_2026_08_14.py`](../scripts/occupancy_pairing_and_content_match_pairing_disagree_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Take two disjoint occupied unit locks: site `s` locks content `A`, site
`t` locks content `B`, and `A ≠ B`. Live Record names each site's lock
label. It does not name a pairing of those labels.

Two extra tables are displayed, not adopted.

Occupancy-product pairing (extra): `B_π(s,t) = 1` if both sites are
occupied, else `0`. On the displayed pair, `B_π(s,t) = 1`.

Content-match pairing (extra): `B_eq(s,t) = 1` if both sites are occupied
and the lock labels are equal, else `0`. On the displayed pair,
`B_eq(s,t) = 0`.

Therefore `B_π(s,t) = 1 ≠ 0 = B_eq(s,t)`. Same two locks, two supplied
tables. The control cell with both locks equal to `A` has
`B_π = B_eq = 1`. The disagreement is the different-label cell, not
occupancy alone.

The live memo does not name `B_π`, does not name `B_eq`, and does not name
a two-argument pairing. Named additive `I` is not Record axiom content
and is not restored here. The pairing arguments are occupied locks and
their labels, not an occupancy field.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact table comparison on one displayed pair of occupied unit locks. Both pairing tables are extras. Live Record is quoted; I is not restored."
trace_class: frontier_discovery
target_claim_id: occupancy_pairing_and_content_match_pairing_disagree
target_blocker_text: "whether a product-on-occupancy table and a same-label table agree when two occupied locks have different content"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the displayed (A,B) pair and the same-label control cell; no pairing is adopted and no axiom is added"
hypothetical_axiom_status: "not proposed; B_π and B_eq remain extras; I is not restored"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Record sentences quoted below. They
  are quoted without rewrite. The axiom memo is the only parent.
- **Explicit theorem-domain condition:** two disjoint occupied unit locks
  with labels `A` and `B`, together with the two supplied extra tables
  `B_π` and `B_eq`. Those tables are not derived from the axioms.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** adopting either table, pairing on an occupancy
  field, restoring named additive `I`, and any physical two-site
  composition rule remain outside the target proved here.

## Exact Objects

All runner values are exact `Fraction` entries `0` or `1`. No float is
used.

A unit lock at a site is either occupied, in which case it carries exactly
one lock label, or unoccupied, in which case it carries no readable
content. Sites `s` and `t` are distinct.

The supplied occupancy-product pairing (extra, not adopted):

```text
B_π(s,t) = 1  if both sites are occupied,
B_π(s,t) = 0  otherwise.
```

The supplied content-match pairing (extra, not adopted):

```text
B_eq(s,t) = 1  if both sites are occupied and the lock labels are equal,
B_eq(s,t) = 0  otherwise.
```

Displayed occupied pair: `s` locks `A`, `t` locks `B`, with `A ≠ B`.

Same-label control: both sites lock `A`.

The live Record axiom, quoted and not rewritten:

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

> When present, a record locks exactly one admissible local possibility.

The live denial that named additive `I` is axiom content, quoted and not
rewritten:

> Finite additivity, a named scalar collection functional `I`, and an assigned
> value `I(empty)=0` are not Record axiom content.

## Theorem 1 — the two extra tables disagree on `(A,B)`

Site `s` is occupied with label `A`. Site `t` is occupied with label `B`.
Both sites are occupied, so `B_π(s,t) = 1`. The lock labels are unequal,
so `B_eq(s,t) = 0`. Therefore

```text
B_π(s,t) = 1 ≠ 0 = B_eq(s,t).
```

Same two locks, two supplied tables.

## Theorem 2 — live Record names two one-site labels

Quote the live Record sentences above. Site `s` reads `A` and site `t` reads `B`.
That is two one-site labels. The readout value at each site is determined
by that site's record content alone.

The axiom memo does not name a two-argument map, does not name `B_π`, and
does not name `B_eq`. Record names each site's lock label, not a pairing
of labels.

## Theorem 3 — both tables are extras

The occupancy-product table and the content-match table are displayed
extras. This note does not adopt `π`. It does not pair on a `J` field:
the arguments are occupied locks and their labels, not an occupancy
field. It does not restore named additive `I`.

## Control — same-label cell agrees

If both locks are `A`, both sites are occupied and the labels are equal,
so `B_π(s,t) = 1` and `B_eq(s,t) = 1`. The disagreement of Theorem 1 is
the different-label cell, not occupancy alone.

If either site is unoccupied, both tables return `0`. That cell is
unreadability of absence, not a scalar assignment `I(empty)=0`.

## Mutation Checks

Three predicates must fail:

1. `B_π(s,t) == B_eq(s,t)` on the displayed `(A,B)` pair.
2. The live memo contains `I(empty)=0` as Record axiom content.
3. The live memo names a two-argument pairing.

Predicate 1 fails by Theorem 1. Predicate 2 fails because the only live
occurrences of `I(empty)=0` are denials that the assignment is Record
content. Predicate 3 fails because the memo names neither `B_π` nor
`B_eq` nor any two-argument pairing.

## Honest-auditor / Boundary

This note compares two supplied extra tables on one displayed pair of
occupied unit locks. It does not adopt either table. It does not install
a pairing as axiom content. It does not restore `I`. It does not pair on
a `J` field. It does not claim that Record already contains a
two-argument map. It does not assign a scalar to an unoccupied site.

The live Record parent is only the quoted lock-and-readout sentences plus
the quoted denial that `I` is axiom content. No other parent is used.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here, and no audit verdict is
authored here.

## What This Does Not Claim

- Neither extra table is adopted as framework content.
- No pairing-on-occupancy-field construction is used or endorsed.
- Named additive `I` is not restored and `I(empty)=0` is not reinstalled.
- Live Record is not rewritten.
- No physical two-site composition rule is derived.
- Unoccupied sites remain unreadable; unreadability is not a scalar value.

## Live Parent Quotes

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

> When present, a record locks exactly one admissible local possibility.

> Finite additivity, a named scalar collection functional `I`, and an assigned
> value `I(empty)=0` are not Record axiom content.

Their dependency role is limited to one-site lock labels, content-only
readout, unreadability of a site with no record, and the denial that `I`
is axiom content. The two pairing tables are separately supplied extras.

## Runner Contract

The companion runner checks Theorems 1–3, the same-label control, the
unoccupied cell, and the three mutations with exact rational arithmetic.
It quotes the live axiom sentences, records the import boundary, and
refuses adoption of `π`, pairing on a `J` field, and restoration of `I`.
Declared review inputs are this note and the axiom memo only.
