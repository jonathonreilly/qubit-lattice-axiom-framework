---
claim_id: j_zero_is_absence_not_a_menu_element_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window, the displayed C1 map J:W→{0}∪M has a definitional occupancy retract o_J if and only if 0 is not a menu element. Honest M={A,B} makes J(z)=0 mean unformed. Counterfactual M0={0,A} makes the same symbol both absence and a lock label, so o_J is not occupancy-of-locks. Current Record already treats unformed as not a locked possibility. The note is a wording constraint on a hypothetical C1 retype, not an adoption of C1, of a vacuum possibility, of L_phys, of r=1/2, or of a pairing on J."
upstream_dependencies:
  - minimal_axioms
runner: scripts/j_zero_is_absence_not_a_menu_element_hypothetical_2026_08_13.py
---

# J Zero Is Absence, Not A Menu Element

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact two-site retract arithmetic for a displayed, not adopted,
C1 site-indexed map. Wording constraint only: `{0}∪M` requires `0 notin M`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/j_zero_is_absence_not_a_menu_element_hypothetical_2026_08_13.py`](../scripts/j_zero_is_absence_not_a_menu_element_hypothetical_2026_08_13.py)

## Result Up Front

A C1 Record retype that writes a site-indexed map

`J:W → {0}∪M`

uses a disjoint union. That notation is honest only if `0 notin M`. Then
`J(z)=0` means unformed, and the retract `o_J(z)=0` iff `J(z)=0` is occupancy.

If the menu itself contains the token `0`, the same symbol is both absence
and a declared lock label. The retract then counts a lock-0 site as unformed,
so `o_J` is not occupancy-of-locks. Current Record already forbids that
reading: unformed is not a locked possibility.

This is a wording constraint on a hypothetical C1 retype. It does not adopt
C1. It does not pick the menu `{A,B}`. It does not install a vacuum
possibility. It does not force `r=1/2`. It does not adopt `L_phys`. It does
not put a pairing on `J`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two-site retract identities and the M0 ambiguity are exact finite algebra. C1 remains a displayed counterfactual; no Record rewrite is adopted."
trace_class: negative_route_pruning
target_claim_id: c1_j_zero_is_absence_not_a_lock_label
target_blocker_text: "C1 wording must keep absence outside the lock menu"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the displayed two-site window; C1 not adopted"
hypothetical_axiom_status: "C1 follow-on: J zero is absence not a lock label; 0 notin M required; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `W={x,y}` be a two-site window, written in the order `(x,y)`.

Honest lock menu:

`M={A,B}` with `0 notin M`.

Displayed C1 map (not adopted):

`J:W → {0}∪M`.

Definitional retract, exact integers:

`o_J(z)=0` if `J(z)=0`, else `o_J(z)=1`.

In code this retract is the identity-gate map `o_from_J`.

Occupancy of a history is the `{0,1}`-valued map that is `1` exactly at
sites that carry a formed lock. On honest `M`, a formed lock is a value in
`M`, never the token `0`.

Counterfactual menu that contains the token `0`:

`M0={0,A}`.

A map `J0:W → {0}∪M0` then has the same point-set codomain as a map into
`M0`. The union is not disjoint.

Two honest histories on `M`:

| History | Reading | `J` | occupancy | `o_from_J` |
|---|---|---|---|---|
| `u` | unformed at `x`, lock `A` at `y` | `(0,A)` | `(0,1)` | `(0,1)` |
| `v` | lock `A` at `x`, unformed at `y` | `(A,0)` | `(1,0)` | `(1,0)` |

Displayed ambiguous cell on `M0`:

`ambiguous_J0=(0,A)` with `0` an element of `M0`.

Current Record sentences used as the only parent (axiom memo
`docs/MINIMAL_AXIOMS_2026-06-29.md`):

```text
Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. For any finite collection of pairwise-disjoint records, scalar readout
`I` is additive, with `I(empty)=0`.
```

No other parent is used. C1 retract arithmetic is reconstructed here.

## Theorem 1 — On honest M, o_J is occupancy

On `M={A,B}` the displayed codomain `{0}∪M={0,A,B}` is a disjoint union:
the absence token is not a lock label.

For history `u`, `J(u)=(0,A)`. The identity gate `o_from_J(u)` returns
`(0,1)`, which is the occupancy of `u`. For history `v`, `J(v)=(A,0)` and
`o_from_J(v)=(1,0)`, the occupancy of `v`.

Thus `J(z)=0` means unformed, not “lock 0.” The retract is occupancy
because every nonzero value is a genuine menu element and every unformed
site is written `0`. Occupancy is not an extra map under this displayed
typing; it is the definitional retract of `J`.

Identity gates: `o_from_J(u)` and `o_from_J(v)`.

## Theorem 2 — On M0 the same 0 is absence and a lock label

Now take `M0={0,A}`, so `0` is a declared lock label. The same symbol is
then used for two Record-distinct readings at a site:

- unformed: no record is present;
- lock `0`: a record is present and locks the menu element `0`.

A map `J0:W → {0}∪M0` cannot tell those readings apart. The displayed
cell `ambiguous_J0=(0,A)` is one pair of symbols with two preimages:

- unformed at `x`, lock `A` at `y`, occupancy `(0,1)`;
- lock `0` at `x`, lock `A` at `y`, occupancy-of-locks `(1,1)`.

The syntactic retract still returns `o_from_J(ambiguous_J0)=(0,1)`. If the
`0` at `x` was a lock, that site is counted unformed. So `o_J` is not
occupancy-of-locks on `M0`.

The predicate “`o_from_J` recovers occupancy on `M0`” therefore fails as a
well-defined occupancy-of-locks: the `0` at `x` is not classified.

Identity gate: displayed `ambiguous_J0`, with `o_from_J(ambiguous_J0)`
evaluated and the classification predicate failing.

## Theorem 3 — Current Record already keeps absence outside the menu

Record says a present record locks exactly one admissible local possibility.
Unformed is the absence of a record, not a locked possibility. The locked
content, when present, is an element of the local menu. The empty collection
has `I(empty)=0`; that scalar `0` is a count, not a lock label.

C1 wording, if written, must therefore keep absence outside the menu: a
disjoint union `{0}∪M` with `0 notin M`, or a tagged sum `none+M`. A menu
that contains a zero token collapses those types.

This is a constraint on a hypothetical retype. It is not a Record rewrite
and not a fifth extra.

## Theorem 4 — No menu pick, no C1 adoption, no vacuum possibility

The honest pair `{A,B}` is a displayed two-element lock menu. Nothing here
selects that pair as the physical one-site menu. The displayed map `J` is
not adopted as Record readout. The token `0` is not installed as a vacuum
possibility or as a locked “empty” outcome.

## Theorem 5 — No r=1/2, no L_phys, no pairing on J

Do not force `r=1/2`. Do not adopt `L_phys`. Do not put a pairing on `J`.
Those are separate extras. A wording constraint that `0` is absence is not
a Newton pairing, not a rate, and not a physical-lattice adoption.

## Mutation Predicates And Identity Gates

- Predicate “`0` is an element of honest `M`” must fail.
- Predicate “`o_from_J` on honest `u` equals `(0,1)`” must pass via the
  identity gate `o_from_J(u)`.
- Predicate “`J0` on `M0` classifies lock-0 versus unformed” must fail.
- Identity gates must call `o_from_J` on `u` and `v`, and on the displayed
  `ambiguous_J0`.

## What This Does Not Do

- It does not adopt a Record rewrite or a C1 axiom sentence.
- It does not cite unmerged PRs or any parent other than the axiom memo.
- It does not name a fifth extra, a vacuum lock, or a pairing on `J`.
- It does not force `r=1/2` or adopt `L_phys`.
- It does not claim that the four axioms already supply site-indexed `J`.

## No-Go Discipline Gate

The negative claims are restricted to honest `M` versus counterfactual
`M0` on two sites. The gate does not certify a Record rewrite.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Honest retract | `o_from_J` on `u`,`v` | Theorem 1: occupancy recovered | **ATTEMPTED** |
| `0∈M` as a lock label | put `0` in `M0={0,A}` | Theorem 2: `J0=(0,A)` is ambiguous | **ATTEMPTED** |
| Current Record on unformed | quote unformed is not a locked possibility | Theorem 3: absence stays outside the menu | **ATTEMPTED** |
| Pick menu `{A,B}` or install vacuum | enlarge the display | Theorem 4: refused | **ATTEMPTED** |
| Pairing, `r=1/2`, `L_phys`, adopt C1 | enlarge the display | Theorem 5: refused | **ATTEMPTED** |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| honest retract / `M0` ambiguity | no: retract needs `0∉M` | no: ambiguity is the `0∈M0` case | independent |
| wording constraint / vacuum lock | no: `0∉M` is not a vacuum possibility | no: a vacuum lock would still need a menu | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}` | stipulated finite object |
| honest `M={A,B}` | stipulated; `0∉M` |
| `M0={0,A}` | stipulated counterfactual |
| pairing, `r=1/2`, `L_phys` | not used |
| observations | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | unformed is not a locked possibility | exact current wording; no `J` borrowed |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two honest cells and one ambiguous `M0` cell | no classification of every menu |
| per site | window `{x,y}` | no lattice-wide vacuum |
| per mode | retract is a `{0,1}` indicator | no pairing |
| per block | `0`-as-absence versus `0`-as-lock-label | no C1 adoption |
| lattice-wide | not executed | two-site window only |

The runner emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure paths

1. Keep current Record: unformed is not a lock; no `J`.
2. Owner wording could adopt `J` later with a tagged sum `none+M`.
3. A later derivation could produce occupancy without naming `J`.

None of those paths is taken here.

### N7 — hostile steelman

> Token `0` is just a spelling of absence. Putting it in the menu is a
> notation abuse, not a physics constraint. Occupancy is still well-defined.

The steelman is right that `0∈M` is notation abuse. Theorem 2 shows the
abuse is load-bearing: the same cell cannot tell lock-0 from unformed.
C1 wording must keep the disjoint union honest.

### N8 — cross-cycle echo

This is a C1 follow-on wording constraint, not pairing-on-`J`, not a
fifth extra, and not a vacuum axiom.

**Gate disposition:** PASS for the honest retract identities, the `M0`
ambiguity, and the Record reading that unformed is not a lock label.
FAIL / DO NOT SHIP for “C1 is adopted,” “`0` is a vacuum possibility,”
“an axiom update is necessary,” or “`o_J` recovers occupancy on every menu.”

## Review Record

Independent audit remains required before any effective status may
change. No `review-loop` was invoked in producing this artifact.
