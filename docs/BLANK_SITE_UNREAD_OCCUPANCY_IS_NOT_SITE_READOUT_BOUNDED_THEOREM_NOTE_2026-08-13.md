---
claim_id: blank_site_unread_occupancy_is_not_site_readout_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window, a site readout is defined only where a record is present. Occupancy of a blank site is a total extra field, not Record content, and the old formation count I(W) is a lemma of a supplied set, not a live axiom readout. The note does not adopt J, restore I, or pick a formation rate."
upstream_dependencies:
  - minimal_axioms
runner: scripts/blank_site_unread_occupancy_is_not_site_readout_2026_08_13.py
---

# Blank Unread: Window Occupancy Is Not a Site Readout

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** two-site window consequence of the landed Record wording.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/blank_site_unread_occupancy_is_not_site_readout_2026_08_13.py`](../scripts/blank_site_unread_occupancy_is_not_site_readout_2026_08_13.py)
**Parent:** axiom memo only
([`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)).

## Result Up Front

Live Record says:

> A site with no record cannot be read.

On a two-site window with one blank site, a site readout is therefore a
partial map: defined at the occupied site and undefined at the blank site.
The occupancy field that returns `0` at the blank site is defined there. So
occupancy is extra bookkeeping, not a site readout and not Record content.

The old formation count `I(W)` is the cardinality of the set of occupied
sites in a supplied window. That integer is a lemma of the supplied set. Live
Record does not name `I`. This note does not restore `I`, does not adopt
`J`, and does not pick a formation rate.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact two-configuration algebra on a declared window: site-readout domain, occupancy totality, and supplied-set count. No axiom edit, no J, no restored I, no formation rate."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "whether blank-site occupancy or the old I(W) count can be read as live Record site readout"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the declared two-site window and the two lock configurations; formation law and any later occupancy field remain extra if wanted as a total field on W"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the window be

`W = {x, y}`.

A configuration of locks is a partial assignment of record values to sites of
`W`. The two configurations used here are

`σ_occ = {x ↦ A}`

with `y` blank, and

`σ_full = {x ↦ A, y ↦ B}`.

A **site readout** of a configuration is the partial map that returns the
locked value only at sites that carry a record. Live Record:

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

So a site readout of `σ_occ` is defined at `x` (value `A`) and undefined at
`y`.

Define occupancy by

`o(z) = 1` if `z` carries a record, else `0`.

Then `o` is a total function on `W`. On `σ_occ` one has `o(y) = 0`.

The old formation count of a supplied window is the cardinality

`I(W) := |{z ∈ W : formed}|`.

That symbol is historical. It is not named by live Record.

## Theorem 1

Quote the blank-unread sentence: “A site with no record cannot be read.”

On `σ_occ`, the domain of a site readout is `{x}`, not `W`. The value at `x`
is `A`. The map is undefined at `y`.

## Theorem 2

The occupancy function `o` is defined at `y` on `σ_occ`, with value `0`.
A site readout of `σ_occ` is not defined at `y`. Therefore `o` is not a site
readout in the sense of the landed sentence. Occupancy of a blank site is
extra bookkeeping, not Record content.

## Theorem 3

The old count `I(W) = |{z ∈ W : formed}|` equals `1` on `σ_occ` and `2` on
`σ_full`. Each number is the cardinality of a set of sites. Live Record does
not name `I`. Display the count as a lemma of a supplied set, not as axiom
readout.

## Theorem 4

This note does not adopt `J`, does not restore `I`, and does not pick a
formation rate. Formation occupancy remains extra if one wants a total field
on `W`.

## Mutation Predicates

The following predicates fail:

1. “site readout of `σ_occ` is defined at `y`”
2. “live memo contains `I(empty)=0`” as governing Record content

The live Record section of
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
is the text from `### Record / Fixed Reality` through `## Qualification`.
That section contains the blank-unread sentence and does not contain
`I(empty)=0`. The rest of the memo may mention `I(empty)=0` only as removed
or as “not Record axiom content.”

## What This Does Not Claim

- No axiom is edited.
- Named `I` is not restored as axiom content.
- `J` is not adopted.
- No formation site, probability, or rate is selected.
- Occupancy is not promoted to Record content.
- The result is a consequence check on the landed wording, not a pairing
  construction and not a further axiom wave.
