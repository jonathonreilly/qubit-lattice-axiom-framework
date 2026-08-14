---
claim_id: l1_formation_independent_of_m2_action_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube L1 member, forming_sites(o) is a function of occupancy only. Two first-wave content assignments — all plus labels, and the same labels conjugated by the permutation (+,-,-) — produce the same tick-2 formation set. Therefore this member does not invoke Aut(M_2). A faithful action is not used."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l1_formation_independent_of_m2_action_2026_08_14.py
---

# L1 Formation Does Not Use An M2 Action

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact independence of the displayed L1 formation set from two first-wave content tables on one twelve-site two-cube carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/l1_formation_independent_of_m2_action_2026_08_14.py`](../scripts/l1_formation_independent_of_m2_action_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The occupancy kernel uses only the occupancy function `o`. Content labels
on already-locked sites do not enter `n`.

Take the first-wave locks and two content tables:

```text
labels_+ : every first-wave site labelled +
labels_P : the same table conjugated by the permutation (+,-,-)
```

The second table is a displayed Pauli flip of content, not an occupancy
change.

**Theorem.** The tick-2 formation set computed from occupancy is

```text
{(1,1,0), (1,0,1), (0,1,1), (2,0,0)}
```

and is identical for both content tables. Recomputing from the lock set
with no labels attached returns the same set. Therefore `L1` formation
does not invoke `Aut(M_2)`. A faithful action is not used by this
member.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact equality of the tick-2 formation set under two displayed content tables that differ by a Pauli flip; formation reads occupancy only."
trace_class: frontier_discovery
target_claim_id: l1_formation_independent_of_m2_action
target_blocker_text: "whether displayed L1 formation invokes Aut(M_2) or a faithful action"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded action-independence claim"
conditional_surface_status: "exact on the supplied two-cube L1 member for the two displayed first-wave content tables; other actions remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Qubit sentence that the one-site possibility
  domain is `M_2(C)`, quoted without rewrite. Qubit privileges no possibility
  and does not pick an automorphism.
- **Explicit theorem-domain condition:** reconstructed L1 kernel and two
  displayed content tables on first-wave locks.
- **External empirical or literature inputs:** none.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> Records form.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone.

Their dependency role is limited to the cubic site set, lock permanence, and
the unreadability of absence. The occupancy kernel, the two-cube patch, and
the tick index are separately supplied.

## Exact Objects

All runner values are exact integers or rationals in `Q`. No float is used.

First-wave locks: `(1,0,0)`, `(0,1,0)`, `(0,0,1)`. Content tables
`all +` versus `(+,-,-)` on those three labels. Tick-2 formation set as
above.

## Exact Target And Proof Obligations

Exhibit two distinct content tables, check that occupancy is unchanged,
and check that the tick-2 formation set is the same occupancy-only set.

## Theorems

### Theorem 1 — the two content tables differ

The permutation `(+,-,-)` flips two of the three first-wave labels, so
the tables are not equal.

### Theorem 2 — formation ignores the tables

`forming_sites` reads `n(o)` only. Both tables, and a recomputation with
no labels, return the same tick-2 set. Formation therefore does not
invoke `Aut(M_2)`.

## What Is Not Claimed

- No Aut-selection of a SWAP corner.
- No comparison of two algebra actions on `sigma_x`.

- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No unique member of the axiom class.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch and checks the theorems with exact `Fraction` arithmetic. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs are
this note and the axiom memo only.
