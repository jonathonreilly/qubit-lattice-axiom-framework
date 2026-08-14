---
claim_id: two_cube_l1_clock_source_ticks34_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube L1 patch the identity Delta rho(A)+Delta rho(B)=F+S continues to hold at ticks 3 and 4. Tick 3: new locks (1,1,1) shared and (2,1,0),(2,0,1) B-only, so F=3, S=1, Delta rho(A)=1, Delta rho(B)=3. Tick 4: new lock (2,1,1) B-only, so F=1, S=0, Delta rho(A)=0, Delta rho(B)=1. This is the remaining-tick table of the shared-face identity."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_clock_source_ticks34_2026_08_14.py
---

# Shared-Face Clock-Source Identity At Ticks 3 And 4

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact shared-face clock-source identities at ticks 3 and 4 of the displayed L1 occupancy kernel on one twelve-site two-cube carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_clock_source_ticks34_2026_08_14.py`](../scripts/two_cube_l1_clock_source_ticks34_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The shared face is `F* = {{v : v_x = 1}}`. Write `S` for the number of
new locks on `F*` and `F` for the number of new locks on the patch.

**Theorem.** The identity

```text
Delta rho(A) + Delta rho(B) = F + S
```

holds on the remaining ticks:

```text
tick 3:  F=3, S=1, Delta rho(A)=1, Delta rho(B)=3,  1+3 = 3+1
tick 4:  F=1, S=0, Delta rho(A)=0, Delta rho(B)=1,  0+1 = 1+0
```

Tick 3 new locks: `(1,1,1)` on the shared face and `(2,1,0)`, `(2,0,1)`
in `B` only. Tick 4 new lock: `(2,1,1)` in `B` only.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer shared-face identities at ticks 3 and 4 of a reconstructed L1 kernel on one two-cube carrier."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_clock_source_ticks34
target_blocker_text: "whether Delta rho(A)+Delta rho(B)=F+S holds on ticks 3 and 4 including saturation"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded remaining-tick identity"
conditional_surface_status: "exact on the supplied two-cube L1 patch for ticks 3 and 4; earlier ticks are a separate table"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Record sentences, quoted without rewrite.
- **Explicit theorem-domain condition:** reconstructed L1 kernel and the shared-face decoder `S = |new locks intersect F*|`.
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

Tick 3: `F=3`, `S=1`, `Delta rho(A)=1`, `Delta rho(B)=3`.
Tick 4: `F=1`, `S=0`, `Delta rho(A)=0`, `Delta rho(B)=1`.

## Exact Target And Proof Obligations

Compute new locks, `F`, `S`, and both cube increments at ticks 3 and 4,
then check the identity and the displayed integers.

## Theorems

### Theorem 1 — cube increments count new locks, shared sites twice

`Delta rho(C) = |new locks intersect C|` for `C in {{A,B}}`.

### Theorem 2 — clock plus shared-face count equals the pair-sum

`Delta rho(A)+Delta rho(B) = F+S` at both remaining ticks.

### Theorem 3 — the tick-3/4 table

The displayed integers `(F,S,Delta A,Delta B) = (3,1,1,3)` then
`(1,0,0,1)` are exactly those increments.

## What Is Not Claimed

- No physical source identification.
- No replacement of the two-tick table.

- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No unique member of the axiom class.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch and checks the theorems with exact `Fraction` arithmetic. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs are
this note and the axiom memo only.
