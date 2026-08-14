---
claim_id: l0_record_formation_composition_source_increment_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On a plus-shaped patch the displayed L0 comparator is run for two ticks. A displayed seed occupancy at +x makes n=(1/3,0,0), f=1, spectral menu {P_{x+},P_{x-}} with probabilities 2/3 and 1/3. Tick 1 locks the realized draw. Tick 2 is the identity by permanence. Source increments by 1 at first formation and is unchanged at tick 2. Rotating the seed rotates the lock axis. This is autonomous Record formation and composition for the comparator, not a TOE, not Born, not Newton, not a pairing on a site-indexed readout, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l0_record_formation_composition_source_increment_2026_08_14.py
---

# `L0` Record Formation, Composition, And Source Increment

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** two-tick exact `Q` tables for the displayed `L0` comparator
on a plus-shaped patch. Not a unique member. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/l0_record_formation_composition_source_increment_2026_08_14.py`](../scripts/l0_record_formation_composition_source_increment_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
`L0` tables are reconstructed locally.

## Result Up Front

Reconstruct the displayed `L0` kernel on the plus-shaped patch:
`n_μ = (c_{+μ} − c_{−μ})/3`, `f = 1` iff `n ≠ 0`, and for axis-aligned
`n` the spectral menu is the two eigenprojectors of `ρ` with
`Tr(ρ P)` probabilities.

A displayed seed occupies only the `+x` neighbor. Then `n = (1/3,0,0)`,
`f = 1`, `p(P_{x+}) = 2/3`, `p(P_{x−}) = 1/3`. Tick 0 is unread.
Tick 1 locks the realized draw (displayed `+`). Tick 2 sees an
existing record and is the identity. The source count at the center
is `0`, then `1`, then `1`.

Rotating the seed by the displayed `R_z` sends the lock to `P_{y+}`.
That is cube covariance of the Record update, not an action named
by Lattice.

This is formation plus composition for one comparator. It is not a
TOE, not an integrated gravity law, and not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two-tick exact Q tables run L0 formation, permanence, and a +1 source increment. No law is adopted."
trace_class: frontier_discovery
target_claim_id: l0_record_formation_composition_source_increment
target_blocker_text: "autonomous Record formation and composition after L0 totalize"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit; integrated recoil/gravity remains separate"
conditional_surface_status: "exact for the displayed comparator on a plus-shaped patch; not a unique member"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name `L0`, a source increment, or a tick table.

## Exact objects

Seed occupancy `c = (1,0,0,0,0,0)` in slot order `(+x,−x,+y,−y,+z,−z)`.
`ρ = (I + σ_x/3)/2`. `P_{x±} = (I ± σ_x)/2`.
`R_z = ((0,−1,0),(1,0,0),(0,0,1))`.

## Theorem 1 — tick 0 is unread, source 0

No record at the center. Source increment is `0`.

## Theorem 2 — tick 1 forms and locks the draw

`f = 1`. The displayed draw is `+`. The center locks `P_{x+}`.
Source becomes `1`.

## Theorem 3 — tick 2 is permanence

The center already carries a record. The update is the identity.
Source stays `1`. This is composition of the Record instrument
with itself.

## Theorem 4 — covariance of the lock

`R_z` sends the `+x` seed to a `+y` seed. The tick-1 lock is then
`P_{y+}`. The displayed Bloch action is used only as this check.

## Theorem 5 — not a TOE and not axiom text

Quoted Record names lock and permanence. Quoted Admissibility names
a varying NN distribution. Neither names this two-tick table or a
source. `L0` remains an unselected comparator. Qubit remains `M_2(C)`.

## Mutations

1. Predicate “tick 2 overwrites the lock” must fail.
2. Predicate “source increments again at tick 2” must fail.
3. Predicate “empty seed forms a record” must fail.
4. Predicate “note adopts L0 or a gravity law” must fail.

Identity gates: `seed_plus_x()`, `tick(history)`, `source_of(history)`,
`rotate_seed_rz()`.

## Honest-auditor / Boundary

Finite: one plus-patch, two ticks, exact `Q`. The runner does not
integrate Einstein recoil, Newton `1/r^2`, or a pairing on a site-indexed readout.

This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No Born derivation.
- No Newton force. No pairing on a site-indexed readout.
- Qubit remains `M_2(C)`.
- QCD is unused.
