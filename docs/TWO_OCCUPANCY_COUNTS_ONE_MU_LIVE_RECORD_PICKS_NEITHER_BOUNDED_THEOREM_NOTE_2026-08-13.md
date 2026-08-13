---
claim_id: two_occupancy_counts_one_mu_live_record_picks_neither_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a four-site window the same site content law μ is compatible with two record configurations that differ in occupancy. The empirical counts r=N_formed/|W| are then 1/4 and 1/2. Live Record (blank unread; no named I) supplies a site readout only where a record is present, so neither displayed rate is Record content and neither is adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_occupancy_counts_one_mu_live_record_picks_neither_2026_08_13.py
---

# Two Occupancy Counts At One μ; Live Record Picks Neither Rate

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact four-site occupancy versus content-law split under the
live Record wording (blank unread; named `I` not axiom content).
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_occupancy_counts_one_mu_live_record_picks_neither_2026_08_13.py`](../scripts/two_occupancy_counts_one_mu_live_record_picks_neither_2026_08_13.py)

## Result Up Front

A nearest-neighbor content law can be the same at every site of a finite
window while the number of formed records on that window is not. The two
displayed occupancy rates therefore disagree. Live Record does not turn
either rate into a readout, and this note adopts neither.

Three exact statements locate the split.

1. **Content law is not occupancy.** The same `μ` is compatible with one
   lock and with two locks on a four-site window. The empirical ratios
   `r(σ1)=1/4` and `r(σ2)=1/2` are then unequal.
2. **Blank occupancy is not a site readout.** Live Record makes a site
   with no record unreadable. Reconstructing that fact: the site readout
   of `σ1` is defined only at `w`. A ratio `N_formed/|W|` puts unread
   blank sites in the denominator and is not Record content.
3. **Live Record does not name `r`.** Both rates are displayed. Neither
   is adopted. Named `I` and `I(empty)=0` are not restored.

No canonical axiom is edited. No formation-site rule, minimum occupancy,
or rate-law class is selected.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four-site occupancy split, blank-unread readout domain, and non-adoption of either displayed rate are proved on declared finite objects. A physical formation-rate law remains extra."
trace_class: negative_route_pruning
target_claim_id: record_formation_rate
target_blocker_text: "live Record (blank unread, no named I) still does not pick a formation rate"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed two-configuration witness; a derived rate law remains open"
hypothetical_axiom_status: "none; no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the window be

`W={w,x,y,z}`, `|W|=4`.

At every site of `W` the same content law on two admissible local
possibilities is

`μ(A)=3/5`, `μ(B)=2/5`.

This is a sitewise possibility distribution of the kind the live
Admissibility wording supplies: it concerns which possibility a forming
record locks. It is the same function at every site of the window. It is
not an occupancy count.

A state is a configuration of records. Write `blank` for a site with no
record. The two configurations are

- `σ1`: lock `A` at `w`; `x,y,z` blank
- `σ2`: lock `A` at `w` and at `x`; `y,z` blank

Let `N_formed(σ)` be the number of sites in `W` that carry a record.
The empirical occupancy ratio on the window is the extra assignment

`r(σ)=N_formed(σ)/|W|`.

Direct count gives `N_formed(σ1)=1` and `N_formed(σ2)=2`, hence

`r(σ1)=1/4`, `r(σ2)=1/2`.

Live Record, quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

```text
Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.
```

The same memo states that a named scalar functional `I`, finite
additivity, and `I(empty)=0` are not Record axiom content. The 2026-08-13
revision removed those clauses; they are not restored here.

## Theorem 1 — Same μ, Two Occupancy Counts

Every formed lock in `σ1` and in `σ2` is the possibility `A`. That
possibility is in the support of `μ` because `μ(A)=3/5≠0`. Blank sites
do not contradict `μ`: the content law is not an occupancy law, and
Admissibility does not supply the formation site or rate.

Both configurations are therefore compatible with the same `μ`. They are
not the same occupancy:

`N_formed(σ1)=1 ≠ 2=N_formed(σ2)`,

so the empirical ratios disagree:

`r(σ1)=1/4 ≠ 1/2=r(σ2)`.

The predicate `r(σ1)==r(σ2)` fails. Content law and occupancy are
different objects.

## Theorem 2 — Occupancy Of A Blank Site Is Not A Site Readout

Live Record: only records are readable; a readout value is determined by
record content alone; a site with no record cannot be read.

In `σ1` the only site that carries a record is `w`, and that record locks
`A`. The site readout of `σ1` is therefore defined only at `w`. The
sites `x,y,z` are blank. Assigning them occupancy `0` and reading that
`0` would be a readout of absence. The live wording does not assign a
scalar to absence.

The ratio `r(σ)=N_formed(σ)/|W|` uses `|W|` as denominator. On `σ1`
that denominator is one formed site plus three unread blanks. The blanks
are not Record content, so `r` is not a Record readout.

The same holds for `σ2`: the site readout is defined only at `{w,x}`;
`y` and `z` remain unread; `r(σ2)=1/2` still divides by `|W|`.

## Theorem 3 — Live Record Does Not Name r

Record names occurrence, one lock per site, permanence, content-only
readout, and unreadability of a blank site. It does not name a window
ratio, a formation-rate law, or a choice between `1/4` and `1/2`.

Both rates are displayed:

| configuration | formed sites | `N_formed` | `r=N_formed/|W|` |
|---|---|---|---|
| `σ1` | `{w}` | `1` | `1/4` |
| `σ2` | `{w,x}` | `2` | `1/2` |

Neither rate is adopted. The note does not install a rate law, does not
prefer the smaller occupancy, does not prefer the larger occupancy, and
does not restore `I` or `I(empty)=0`.

## Boundary

- The witness is one four-site window and one pair of configurations.
  It does not classify all occupancy patterns or all content laws.
- Compatibility with `μ` is support compatibility of formed locks. It is
  not a derivation of `μ` from occupancy, or of occupancy from `μ`.
- A later retained construction could still supply a formation-site rule
  or a rate law. This note does not close that route and does not take
  it.
- Independent questions about a distinguished formation site or a
  selected rate-law class are out of scope.
- No axiom, primitive, ledger, or audit surface is edited.
