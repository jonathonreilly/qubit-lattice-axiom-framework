---
claim_id: unlocked_labels_are_invisible_occupancy_is_not_lock_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the two-site star {x,y} with menu {A,B}, content-only readout sees only lock patterns: I(L_1)=1, I(L_2)=2, I(empty)=0, and I(ghost)=I(L_1)=1 because an unlocked label is not a record; the ghost is not a state; occupancy-without-lock is extra and is not axiom content."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unlocked_labels_are_invisible_occupancy_is_not_lock_2026_08_13.py
---

# Unlocked Labels Are Invisible And Occupancy Is Not Lock

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact type split, on one two-site star and one two-point menu,
between a Record lock pattern and a putative unlocked site-label.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/unlocked_labels_are_invisible_occupancy_is_not_lock_2026_08_13.py`](../scripts/unlocked_labels_are_invisible_occupancy_is_not_lock_2026_08_13.py)

## Result Up Front

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies a
content-only additive scalar on finite pairwise-disjoint record collections,
and it identifies a state with a configuration of records. Those sentences
are quoted only as premises and are not edited:

> Only records are readable. A readout value is determined by record content alone.
> For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.
>
> A state is a configuration of records.

On the two-site star `{x,y}` with menu `{A,B}`, a **lock pattern** is a
partial map `L: {x,y} ⇀ {A,B}`. Readout with unit strengths is the domain
count `I(L)=|dom(L)|`. That count sees only locks:

`I(L_1)=1`, `I(L_2)=2`, `I(empty)=0`.

A **putative occupancy** is a total map `O: {x,y} → {A,B,∅}`. Decorating a
site that carries no record with an unlocked menu label does not add a
record. The ghost occupancy that locks `A` at `x` and writes unlocked `B` at
`y` therefore has the same content-only readout as `L_1`:

`I(ghost)=I(L_1)=1`.

The unlocked `B` is invisible. The ghost is not a state. The two states in
the comparison are the lock patterns `L_1` and `L_2`. Occupancy-without-lock
is an extra label that the quoted sentences do not read. This note does not
adopt that extra object, does not claim that no later occupancy compiler
exists, and does not edit an axiom.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: occupancy_versus_lock
target_blocker_text: "identify site occupancy with Record lock, or read unlocked labels"
source_of_blocker_text: handoff
reachability_to_target: prunes
next_trace_action: "Unlocked labels are invisible and are not states. Occupancy-without-lock is extra. Do not adopt axiom text."
hypothetical_axiom_status: "no edit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work on the two-site star `{x,y} ⊂ Z^3` with the single edge `xy`. The local
possibility menu is the two-point set

`X = {A, B}`.

A **lock pattern** is a partial map

`L: {x,y} ⇀ {A,B}`.

Absence of a value means no record at that site. Record uniqueness makes the
partial map at most single-valued. Each locked site is a unit-strength
record. Scalar readout is the domain count

`I(L) := |dom(L)|`,

so `I(empty)=0` is the empty partial map. The three lock patterns used below
are

| pattern | lock at `x` | lock at `y` | `dom(L)` | `I(L)` |
|---|---|---|---|---|
| `empty` | empty | empty | `∅` | `0` |
| `L_1` | `A` | empty | `{x}` | `1` |
| `L_2` | `A` | `B` | `{x,y}` | `2` |

A **putative occupancy** is a total map

`O: {x,y} → {A,B,∅}`

together with a distinguished subset of sites that actually lock. A nonempty
occupancy value that is not a lock is an **unlocked label**. The ghost used
below is

| object | value at `x` | value at `y` | locked sites | `I` |
|---|---|---|---|---|
| `O_ghost` | `A` (locked) | `B` (unlocked) | `{x}` | `1` |

The ghost and `L_1` have the same lock pattern. They differ only by the
unlocked `B` at `y`.

A declared content law on the menu is the probability

`μ(A)=1/3`, `μ(B)=2/3`.

Its support is `{A,B}`. A lock pattern is **lawful** for `μ` when every
locked value lies in that support. Both `L_1` and `L_2` are lawful. The
Admissibility reading note used only as a formation pin is that the
distribution concerns which possibility a forming record locks, conditional
on formation at that site; it does not supply the formation site,
probability, or rate.

## Exact Target And Obligation Graph

**Exact target.** Prove that content-only readout sees only lock patterns,
that a putative unlocked label is invisible and is not a Record state, and
that occupancy-without-lock is extra.

| Obligation | Role | Disposition |
|---|---|---|
| pin “Only records are readable” and content-only readout | premise | quoted from the axiom memo |
| pin `I(empty)=0` | premise | quoted from the axiom memo |
| pin “A state is a configuration of records.” | premise | quoted from the axiom memo |
| compute `I(L_1)=1`, `I(L_2)=2`, `I(empty)=0` | Theorem 1 | unit-strength domain count |
| compute `I(ghost)=I(L_1)=1` | Theorem 1 | unlocked label is not a record |
| show the ghost is not a state | Theorem 2 | states are lock patterns |
| show no readout of the ghost `B` exists | Theorem 3 | content-only |
| show the same `μ` is compatible with `L_1` and `L_2` | Theorem 4 | formation still free |
| record that occupancy-without-lock is extra | Theorem 5 | scoped residual |
| identify occupancy with lock, or read unlocked labels | pruned route | Theorems 1--3 |
| claim that no occupancy compiler exists | non-claim | not made |
| edit an axiom to name occupancy-without-lock | non-claim | not required |

## Theorem 1 — I Sees Only Locks

**Claim.** `I(L_1)=1`, `I(L_2)=2`, and `I(empty)=0`. Adding an unlocked
label does not change `I`: `I(ghost)=I(L_1)=1`.

**Proof.** Each locked site is one unit-strength record. The empty lock
pattern has empty domain, so `I(empty)=0` is the quoted identity. The domain
of `L_1` is `{x}`, so `I(L_1)=1`. The domain of `L_2` is `{x,y}`, so
`I(L_2)=2`. Additivity on the disjoint one-site records at `x` and at `y`
recovers the same `2`:

`I(L_2)=I(L_1)+I(y↦B)=1+1=2`.

The ghost has the same lock pattern as `L_1`. Site `y` carries an unlocked
`B`, which is not a record. Content-only readout is determined by record
content alone, so the unlocked label does not enter `I`. Therefore
`I(ghost)=I(L_1)=1`. In particular `I(ghost)≠I(L_2)`.

## Theorem 2 — States Are Record Configurations

**Claim.** Quote: “A state is a configuration of records.” The ghost
occupancy is not a state. The two states in the comparison are `L_1` and
`L_2`.

**Proof.** A lock pattern is exactly a configuration of records on the star:
each element of `dom(L)` is one record locking one menu value. Thus `L_1`
and `L_2` are states, and the empty lock pattern is the empty configuration.
The ghost is not a lock pattern. It carries an extra unlocked label at `y`
that is not a record. That extra mark is not part of any configuration of
records, so the ghost is not a state.

The predicate `is_state` is true of a lock pattern and false of the ghost.
Identifying the ghost with `L_2` would replace a non-state by a two-record
state and would change `I` from `1` to `2`.

## Theorem 3 — Content-Only Readout Sees No Ghost Label

**Claim.** Quote: “Only records are readable. A readout value is determined
by record content alone.” No readout of the ghost `B` exists.

**Proof.** Readable content is the locked content. The readable set of
`L_1` is the singleton record `(x,A)`. The readable set of the ghost is the
same singleton: `y` carries no record, so the unlocked `B` is not readable.
The readable set of `L_2` is `{(x,A),(y,B)}`. No content-only functional of
the ghost returns the unlocked `B`, because that label is not record
content. A readout that counted every nonempty occupancy value would return
`2` on the ghost and would contradict `I(ghost)=1`.

## Theorem 4 — Formation Still Free

**Claim.** The same content law `μ` with support `{A,B}` is compatible with
`L_1` and with `L_2`. Unlocking is not a third physical option supplied by
the axioms; it is an extra label that the axioms do not read.

**Proof.** Both locked values of `L_1` and of `L_2` lie in `supp(μ)={A,B}`,
so both patterns are lawful. The same per-site law is therefore compatible
with one lock and with two locks. The Admissibility reading note already
says that the distribution does not supply the formation site, probability,
or rate. Unlocking `y` while writing `B` there is not a third lawful lock
pattern: it is not a lock pattern at all. The axioms read `L_1` or `L_2`.
They do not read the ghost.

## Theorem 5 — Scoped Residual

**Claim.** Occupancy-without-lock is not derived and is not axiom content.
A later occupancy rule would be extra. No axiom is edited. The note does
not claim that no occupancy compiler exists.

**Proof.** Theorems 1--3 show that the quoted Record sentences see lock
patterns and do not see unlocked labels. Theorem 4 shows that those
sentences still leave formation free between `L_1` and `L_2`. None of those
facts produces a total occupancy map, and none of them reads an unlocked
label. Declaring such a label makes a second object. That declaration is
the extra structure.

The residual is scoped. It does not say that a later compiler of occupancy
from some further supplied structure is closed. It does not say that a
later selector forcing a lock at every nonempty site is impossible. It says
only that those objects are not the present Record readout and are not the
present notion of state.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- identify site occupancy with Record lock;
- treat an unlocked label as readable content;
- force formation at every occupied site;
- claim that no occupancy compiler exists;
- derive a formation-rate law or a lattice-wide occupancy process;
- replace the full one-site domain `M_2(C)` by the two-point menu.

The scope is the exact type split on one two-site star: `I` sees only locks,
the ghost is invisible and is not a state, and occupancy-without-lock is
extra.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current content-only readout sentence and `I(empty)=0` | premise | quoted; no edit |
| current “Only records are readable” sentence | premise | quoted; no edit |
| current “A state is a configuration of records.” sentence | premise | quoted; no edit |
| Admissibility reading note that the distribution does not supply site or rate | formation pin | quoted; not enlarged |
| two-site star, menu `{A,B}`, `L_1`, `L_2`, ghost | declared algebra | computed here |
| occupancy-without-lock as readable content | residual | live, not derived |

The exact advance is a finite type-split theorem. Independent audit remains
required before any effective status may change. An unmerged two-site
support exhibit that used occupancy as a synonym for lock patterns is a
sibling, not a premise; the lock patterns used here are reconstructed.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The quoted Record sentences say “Only records are readable” and “A state is a configuration of records.” The obstruction is the identification of site occupancy with Record lock, or a readout of unlocked labels. This note splits those types on one star. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for unlocked labels, occupancy-versus-lock, putative occupancy, and “I sees only locks.” Hits: ACPHILAMBDA occupancy notes are orbit-grain statements (K/CPT 2-sector occupancy, `r=1/2` grain) and do not split lock from unlocked site-labels; Koide occupancy notes are statistical-slot or orbit-occupancy objects; the axiom memo never names occupancy. No landed type-split theorem that an unlocked label is invisible to `I` appears on that commit. An unmerged two-site support exhibit treats occupancy as a synonym for lock patterns and is a sibling, not a premise. |
| V3 | Independently checkable? | Textbook partial maps (functions defined on a subset) do not mention Record, readout, or state. The runner recomputes `I` as a unit-strength domain count and checks `is_state` by absence of unlocked labels, in exact integer/`Fraction` arithmetic. |
| V4 | More than a restatement? | Yes. The witnesses `I(L_1)=1`, `I(L_2)=2`, `I(empty)=0`, and `I(ghost)=I(L_1)=1` are not restatements of the quoted sentences. |
| V5 | One-step relabel? | No. `I(empty)=0` alone says that the empty collection reads zero. It does not compare the ghost to `L_1` or separate `I=1` from `I=2`. The type split needs that pair. |

## No-Go Discipline Gate (Theorems 4–5)

The negative claim is restricted to this: occupancy-without-lock is extra,
unlocking is not a third option supplied by the axioms, and the quoted
sentences do not select a lock at every occupied site. The gate does not
ship a global non-existence theorem against a later occupancy compiler.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| count unlocked labels | set `I` to the number of nonempty occupancy values | Theorem 1: `I(ghost)` would become `2`, but content-only `I` stays `1` | **ATTEMPTED** |
| treat ghost as a state | declare `O_ghost` a Record state | Theorem 2: a state is a configuration of records; the ghost is not | **ATTEMPTED** |
| force formation at every occupied site | lock every nonempty occupancy value | Theorem 4: that selector turns the ghost into `L_2` and changes `I` from `1` to `2`; it is extra | **ATTEMPTED** |
| occupancy-lock synonym | identify every total occupancy map with its nonempty labels as locks | Theorems 1--3: the ghost would collapse to `L_2`, contradicting `I(ghost)=1` | **ATTEMPTED** |
| axiom edit naming unlocked labels | add a sentence that unlocked labels are readable | not required by content-only readout; see N6 | **ATTEMPTED** |
| `I(empty)=0` alone | derive the type split from the empty-collection identity | V5: the empty identity does not compare ghost to `L_1` | **ATTEMPTED** |

### N2 — wall independence

Theorems 4 and 5 close only the claim that the quoted sentences already
supply occupancy-without-lock or force a lock at every occupied site. They
do not close Theorem 1 (the count), Theorem 2 (the state predicate),
Theorem 3 (content-only invisibility), a later occupancy compiler, or a
later formation-rate law. Those walls remain independent. Invisibility of
an unlocked label does not by itself forbid a later extra compiler.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| two-site star `{x,y}` and menu `{A,B}` | declared finite objects |
| lock pattern as a partial map | declared Record configuration |
| putative occupancy and unlocked labels | explicit extra marks |
| unit-strength readout `I(L)=|dom(L)|` | explicit content-only count |
| `μ(A)=1/3`, `μ(B)=2/3` | declared content law; support `{A,B}` |
| axiom edit naming occupancy-without-lock | live governance path; not required |
| later occupancy compiler | open; not assumed absent |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | “Only records are readable”; content-only readout; `I(empty)=0`; “A state is a configuration of records.” | quoted as premises only; no edit |

No unmerged occupancy synonym exhibit is used as a parent. The lock
patterns and the ghost are recomputed here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | lock patterns `L_1`, `L_2`, `empty`, and the ghost occupancy | no classification of every site-label decoration |
| per site | each star site is empty, locked, or carrying an unlocked label; `I` counts only locks | no composite carrier |
| per mode | menu labels `{A,B}` are content; unlocked `B` is not a value of `I` | no spectral-mode exhaustion |
| per block | type split on one star, plus the scoped residual that occupancy-without-lock is extra | no occupancy compiler and no axiom edit |
| lattice-wide | checked and not executed | no lattice-wide occupancy process |

The residual is a type-split gap. It is not lattice-wide.

### N6 — live partial-closure paths

1. A later occupancy compiler that uses more than Record content — for
   example a declared total site-label — to name occupancy-without-lock
   without editing an axiom.
2. A later selector that forces a lock at every nonempty site, converting
   a ghost into `L_2` by extra rule.
3. A later readout that is not content-only and that treats unlocked
   labels as readable.
4. An owner-approved typed axiom addition that named occupancy-without-lock.
   Content-only readout does not require that addition.

The quoted Record sentences already name readable records, content-only
`I`, `I(empty)=0`, and states as record configurations. They do not name
unlocked labels. No axiom sentence is required by Theorem 5.

### N7 — hostile steelman

> Occupancy is just the lock pattern written as a total map with a blank
> at empty sites. The ghost is then `L_2`, so `I` already counts occupancy.

**Answer.** A total map that writes a menu value at a site with no record
is not a lock pattern. Theorem 1 computes `I(ghost)=1` and `I(L_2)=2`.
Theorem 2 refuses the ghost as a state. The synonym that collapses the
ghost to `L_2` is exactly the identification this note prunes.

### N8 — cross-cycle echo

Orbit-grain occupancy notes on `origin/main` concern K/CPT sector weights
and statistical slots. They do not read an unlocked site-label as a Record
state. The present type split does not reverse those notes. It answers a
different question: among Record readouts, only locks are visible; among
putative site-labels, an unlocked mark is extra.

**Gate disposition.** PASS for invisibility of unlocked labels, for the
state/non-state split, and for the scoped residual that occupancy-without-lock
is extra. FAIL / DO NOT SHIP for “no occupancy compiler exists,” “formation
is forced at every occupied site,” or “an axiom edit is required.”

## Primary Runner

[`scripts/unlocked_labels_are_invisible_occupancy_is_not_lock_2026_08_13.py`](../scripts/unlocked_labels_are_invisible_occupancy_is_not_lock_2026_08_13.py)
recomputes `I` from lock domains, the ghost comparison `I(ghost)=I(L_1)=1`,
the state predicate, content-only readable sets, and the shared content law
in exact rational arithmetic. Identity gates call `I_of_locks(L)` and
`is_state(L)`. A predicate that `I` counts unlocked labels must fail (ghost
still `I=1`). Replacing `L_1` by `L_2` must change `I` from `1` to `2`. A
predicate that the ghost is a state must fail Theorem 2.
