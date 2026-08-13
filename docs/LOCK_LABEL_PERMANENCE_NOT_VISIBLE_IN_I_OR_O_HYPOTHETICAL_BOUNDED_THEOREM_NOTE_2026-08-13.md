---
claim_id: lock_label_permanence_not_visible_in_i_or_o_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window with a two-entry menu and two snapshots, a legal stay and an illegal same-site lock-label flip share the unit-count I-sequence and the site-occupancy o-sequence. The site-blind bag and the site-indexed field J split them. Record permanence together with one lock per record forbids the relock. The split is displayed and is not adopted as a Record rewrite."
upstream_dependencies:
  - minimal_axioms
runner: scripts/lock_label_permanence_not_visible_in_i_or_o_hypothetical_2026_08_13.py
---

# Lock-Label Permanence Is Not Visible in I or o

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** two-snapshot visibility of a same-site lock-label flip on a
two-site window, under current Record wording and a displayed site-indexed
field `J`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/lock_label_permanence_not_visible_in_i_or_o_hypothetical_2026_08_13.py`](../scripts/lock_label_permanence_not_visible_in_i_or_o_hypothetical_2026_08_13.py)

Parent on `origin/main`: the axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Occupancy stays one unit lock at a fixed site. A legal stay keeps the same
lock label. An illegal relock flips the label at that same site. The named
scalar readout sequence and the weak occupancy sequence are identical on
both histories. The site-blind bag of lock labels and the site-indexed field
`J` split them. The current Record sentences “records are permanent” and
“locks exactly one” together forbid the relock. This note displays that
visibility split. It does not adopt a Record rewrite, a formation rate, a
pairing on `J`, `L_phys`, or a forced value `r=1/2`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer identities on a declared two-site, two-snapshot window; no axiom edit and no adopted readout retype."
trace_class: negative_route_pruning
target_claim_id: lock_label_permanence_visibility_in_named_readout
target_blocker_text: "named scalar I and weak occupancy o do not witness same-site lock-label permanence"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the declared window and the displayed J arithmetic; not adopted"
hypothetical_axiom_status: "C1 follow-on: lock-label permanence not visible in I or o; J and bag split relock; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Window `W={x,y}` with the listed order `(x,y)`. Finite menu `M={A,B}`.
Two snapshots `t=0,1`. Occupancy is already one unit lock at `x` and stays
there.

Reconstructed site-indexed field, displayed and not adopted:

```text
J : W → {0} ∪ M
J(z) = 0                 if the site is empty
J(z) = locked menu entry if the site carries the unit lock
```

A snapshot is written as the ordered pair `(J(x), J(y))`. A history is a pair
of snapshots.

Derived maps, computed from `J` rather than supplied independently:

```text
o(z) = 0 if J(z)=0 else 1
I(J) = |{z in W : J(z) ≠ 0}|
bag(J) = {J(z) : J(z) ≠ 0}
```

The integer `I=1` on a single occupied site is a **unit-count convention**.
Record additivity with `I(empty)=0` is compatible with any fixed positive
unit per disjoint lock; the axioms do not force that unit to be `1`.

Sequences are the two-snapshot tuples

```text
I_seq(H)   = (I(H_0), I(H_1))
o_seq(H)   = (o(H_0), o(H_1))
bag_seq(H) = (bag(H_0), bag(H_1))
J_seq(H)   = (H_0, H_1)
```

Two histories on this window:

```text
legal stay S:     J_0 = (A, 0),  J_1 = (A, 0)
illegal relock R: J_0 = (A, 0),  J_1 = (B, 0)
```

A reconstructed site-move history is used only as a contrast, not as the
illegal object of this note:

```text
site-move Move:   J_0 = (A, 0),  J_1 = (0, A)
```

Identity gates call `I_seq`, `o_seq`, `bag_seq`, and `J_seq` on `S` and `R`.

## Theorem 1 — I-seq and o-seq do not split stay from relock

**Statement.** `I_seq(S)=I_seq(R)=(1,1)` and
`o_seq(S)=o_seq(R)=((1,0),(1,0))`. Weak occupancy is not enough for
lock-label permanence.

**Proof.** Each snapshot of `S` and of `R` has `J(x)∈M` and `J(y)=0`. The
occupancy pair is therefore `(1,0)` at both times, and the unit-count
convention gives `I=1` at both times. The two sequences agree, so neither
`I_seq` nor `o_seq` can tell stay from relock. ∎

The predicates “`I_seq(S)` differs from `I_seq(R)`” and
“`o_seq(S)` differs from `o_seq(R)`” therefore fail.

## Theorem 2 — Bag and J split stay from relock

**Statement.** `bag_seq(S)=({A},{A})` and `bag_seq(R)=({A},{B})`.
`J_seq(S)=((A,0),(A,0))` and `J_seq(R)=((A,0),(B,0))`. Those two pairs
differ.

**Proof.** The site-blind bag of a snapshot is the set of nonzero lock
labels. Stay keeps `{A}` at both times. Relock replaces `{A}` by `{B}` at
`t=1`. The site-indexed field keeps the site and changes the label, so the
`J` sequences differ in the second snapshot. ∎

The predicate “`J_seq(S)=J_seq(R)`” therefore fails.

## Theorem 3 — Record forbids relock; visibility is split across maps

Quote the current Record wording:

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

Together those sentences forbid relock. At `t=0` the record at `x` locks
`A`. Permanence keeps that record. Replacing `A` by `B` at the same site
removes the earlier lock and violates permanence. Adding `B` beside `A` at
the same site would make the site carry more than one record and would
violate “locks exactly one.”

A reconstructed site-move `Move` with the same lock `A` has

```text
I_seq(Move)   = (1,1)                 = I_seq(S)
bag_seq(Move) = ({A},{A})             = bag_seq(S)
o_seq(Move)   = ((1,0),(0,1))        ≠ o_seq(S)
J_seq(Move)   = ((A,0),(0,A))        ≠ J_seq(S)
```

so a site-move is invisible in `I` and in the bag. The label-flip `R` is
invisible in `I` and in `o`, and is visible in the bag. Strong `J` sees
both illegalities. Weak `o` sees only the move. The bag sees only the
relock.

## Theorem 4 — Not a site-move test and not a formation rate

The illegal history of this note does not change site. Occupancy stays one
unit lock at `x` on both `S` and `R`. There is no growth from empty, no
second formation event, and no formation-rate target. Formation is not
reopened. The objects are displayed. They are not adopted.

## Theorem 5 — Display only

Do not adopt a Record rewrite. Do not force `r=1/2`. Do not adopt
`L_phys`. Do not put a pairing on `J`. The `2×2` product table on
occupancies remains extra; this note never introduces a two-argument
pairing through `I` or through `J`.

## Non-claims

- The axioms are not edited.
- Unit-count `I=1` is not derived from Record additivity.
- The note does not select a physical clock, a formation law, or a
  Newton pairing.
- Visibility on this finite window is not an exhaustion of every possible
  record-identity semantics outside the displayed `J` representation.

## No-Go Discipline Gate

The negative claims are restricted to “`I`-seq or `o`-seq witnesses
lock-label permanence” and “this is a restatement of the site-move test.”
The gate does not certify a Record rewrite.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Scalar `I`-seq as the split | evaluate `I_seq` on `S` and `R` | Theorem 1: both `(1,1)` | **ATTEMPTED** |
| Weak occupancy `o`-seq | evaluate `o_seq` on `S` and `R` | Theorem 1: both `((1,0),(1,0))` | **ATTEMPTED** |
| Site-blind bag | evaluate `bag_seq` | Theorem 2: `({A},{A})` vs `({A},{B})` | **ATTEMPTED** |
| Site-indexed `J` | evaluate `J_seq` | Theorem 2: stay ≠ relock | **ATTEMPTED** |
| Treat as site-move / formation | occupy a new site or grow from empty | Theorem 4: occupancy stays at `x` | **ATTEMPTED** |
| Adopt C1, pairing on `J`, `r=1/2`, `L_phys` | enlarge the display | Theorem 5: refused | **ATTEMPTED** |

### N2 — wall independence

Equal `I`-seq does not give equal bags. Equal `o`-seq does not give equal
`J`. A site-move is a different invisibility pattern.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}`, menu `{A,B}`, two snapshots | stipulated finite objects |
| unit-count `I=1` | convention; not forced by additivity |
| reconstructed site-move `Move` | contrast only |
| C1 adoption, pairing on `J` | not used |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | “records are permanent” and “locks exactly one” | quoted; jointly forbid relock |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | stay `S` and relock `R` | no classification of every history |
| per site | occupancy stays at `x` | no lattice-wide permanence theorem |
| per mode | `I`/`o` versus bag/`J` | no pairing on `J` |
| per block | label-flip versus site-move | no formation rate |
| lattice-wide | not executed | only `W={x,y}` |

### N6 — live partial-closure paths

1. Keep permanence as English on the current axiom file.
2. If C1 is later adopted, lock-label permanence is a `J`-seq (and bag)
   fact, not an `I` or `o` fact.
3. A pairing on `J` remains extra either way.

### N7 — hostile steelman

> Permanence is already occupancy permanence, so a same-site relock is
> another record and `o` should not have to see it.

The steelman rewrites “records are permanent.” On the current sentence
plus “locks exactly one,” the same-site label flip is illegal and still
invisible in `I` and `o`.

### N8 — cross-cycle echo

This is a C1 follow-on, not C6 or C7. It is not c1perm: the site does
not change. Formation is not reopened.

**Gate disposition:** PASS for (i) `I_seq` and `o_seq` agree on `S` and
`R`, and (ii) bag and `J` split them. FAIL / DO NOT SHIP for “adopt C1,”
“put a pairing on `J`,” “force `r=1/2`,” or “adopt `L_phys`.”

## Review Record

Independent audit remains required before any effective status may
change. No `review-loop` was invoked in producing this artifact.
