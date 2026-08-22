---
claim_id: z_symmetric_three_site_two_tick_record_stack_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse/face from own incoming sets at t versus t+1 on the four #7188 x-probes, and whether t+1 bits equal t bits, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_two_tick_record_stack_composition_reverse_face_2026_08_15.py
---

# Two-Tick Record-Stack Composition Of Own-Incoming Reverse And Face On Four Z-Symmetric Three-Site X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from each probe's own earliest incoming
nearest-neighbor step *set* `M` at that probe's formation tick `t` versus
`t+1`, on the four z-symmetric three-site x-probes in
`B_3(0)={n:n·n<=9}`, no global T. Let `t(q)` be the formation tick of
probe `q`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. Unformed at `τ` is
`UNDEFINED`. Reverse at a cut holds if and only if `A` and `B` are formed
by that cut and some `a` in `M(A,·)` and some `b` in `M(B,·)` have
`a+b=(0,0,0)`. Face likewise on `C,D`. Empty or `UNDEFINED` on either
side is `UNDEFINED`. Composition HOLD if and only if the `t+1`
reverse/face bits equal the `t` bits (neither side `UNDEFINED`, or both
`UNDEFINED`). This is not leftover of same-tick-inclusive six-neighbor
lock union. This is not leftover of unique own-incoming letters. This is
not the two-tick lock-count clock composition. Uniqueness of incoming
locks is not required. Mixed remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_two_tick_record_stack_composition_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_two_tick_record_stack_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in each
probe's own incoming set at that probe's `t` and at `t+1`. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock
letter is a different readout and is not used. A `Z^3` sum of those locks is
a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of own earliest incoming sets M at each of the four z-symmetric three-site x-probes at t and at t+1, with reverse fail, face fail, and composition HOLD because t+1 bits equal t bits; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_two_tick_record_stack_composition_reverse_face
target_blocker_text: "display reverse and face from own incoming sets at t versus t+1 on the four z-symmetric three-site x-probes, no global T, and whether those bits compose"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse, face, and composition displayed; do not write existential opposite into Admissibility, do not reduce to a unique incoming letter, do not replace M by six-neighbor lock union, do not replace M by a lock-count clock, and do not wait for a global later T."
conditional_surface_status: "exact on B_3(0) for two-tick composition of own-incoming reverse/face on the four z-symmetric three-site x-probes, no global T; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Displayed process

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, and `e_3=(0,0,1)`. The six nearest-neighbor
steps are

```text
NN = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
```

The finite host is the closed Euclidean ball of radius 3 centered at the
origin,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

No larger host is used. The four x-probes are the only sites whose own
incoming sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

`A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,0,1), (0,0,-1)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,0,1)=−e_1`, and `L(0,0,-1)=−e_1`. This
is the same process as the z-symmetric three-site same-tick union-own
display on these x-probes.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required.

## Named incoming set `M` at `t` and at `t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Duplicate incoming steps collapse in the set.
The construction does not require `M(q,τ)` to be a singleton. It does not
sum `M(q,τ)`. It does not replace `M` by locks of six-neighbors of `q`.
It does not wait for a global later T.

Reverse at a cut holds if and only if `A` and `B` are formed by that cut
and some `a` in `M(A,·)` and some `b` in `M(B,·)` have `a+b=(0,0,0)`. Face
at a cut holds if and only if `C` and `D` are formed by that cut and some
`c` in `M(C,·)` and some `d` in `M(D,·)` have `c+d=(0,0,0)`. Empty or
`UNDEFINED` on either side of a comparison is `UNDEFINED`; nonempty with
no opposite pair fails.

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`, with neither side `UNDEFINED` or both
sides `UNDEFINED`. Else composition fails. The `t+1` bits are a function of
the `t` stack on this process precisely when composition HOLD. Displayed,
not adopted.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero inside `M`.

## Theorem 1 — ticks, `M` at `τ0` and at `τ1`, and new six-neighbor records

On this process the four x-probes form, and the own incoming sets at each
probe's `t` equal the own incoming sets at `t+1`:

```text
t(A)=3
t(B)=2
t(C)=4
t(D)=2
M(A, τ0) = {+e_2, −e_2}
M(B, τ0) = {+e_1}
M(C, τ0) = {+e_1}
M(D, τ0) = {+e_1}
M(A, τ1) = {+e_2, −e_2}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_1}
M(D, τ1) = {+e_1}
```

`A` is mixed: two earliest incoming steps `+e_2` and `−e_2`. Mixed remains a
set. `B`, `C`, and `D` are singletons `{+e_1}`. New records in `B_3(0)`
between `τ0` and `τ1` that meet a probe's six-neighbors are later arrivals
and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 0, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0)
new 6-NN of D at t(D)+1: (1, 2, 0), (1, 0, 0)
```

The new neighbor `(2, 0, 0)` of `A` is probe `C`, formed at tick 4 with
incoming `+e_1`. The step from that neighbor into `A` is parallel to the
parent lock, so it is not an allowed incoming step. The new neighbors of
`B`, `C`, and `D` arrive after those probes' earliest incoming tick, so they
are not earliest. Therefore `M(q,τ1)=M(q,τ0)` at every scored probe.

This is not leftover of unique own-incoming letters: that readout would
replace mixed `M(A)` by `UNDEFINED`. This is not leftover of
same-tick-inclusive six-neighbor lock union: that leftover includes `+e_1`
at `A` from the origin neighbor and reports reverse hold. This is not the
two-tick lock-count clock composition.

## Theorem 2 — reverse at `τ0` and at `τ1`

Reverse holds if and only if some `a` in `M(A,·)` and some `b` in `M(B,·)`
have `a+b=(0,0,0)`. At `τ0` the sets are `{+e_2, −e_2}` and `{+e_1}`. No
pair sums to zero. Reverse fails. At `τ1` the sets are the same, so reverse
fails again. Both sides are nonempty and defined, so this is not
`UNDEFINED`.

Reverse at τ0: fail
Reverse at τ1: fail

Unique own-incoming letters on these x-probes report reverse `UNDEFINED`
from mixed `A`. Same-tick-inclusive six-neighbor lock union reports reverse
hold from `−e_2` at same-tick neighbors of `A` against `+e_2` at `B`. Those
are different objects. Reverse fails here because the own incoming set at
`A` never contains `−e_1`.

## Theorem 3 — face at `τ0` and at `τ1`, and composition

Face holds if and only if some `c` in `M(C,·)` and some `d` in `M(D,·)` have
`c+d=(0,0,0)`. At `τ0` the sets are `{+e_1}` and `{+e_1}`. No pair sums to
zero. Face fails. At `τ1` the sets are the same, so face fails again.

Face at τ0: fail
Face at τ1: fail

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`. Both reverse reports are `fail` and both
face reports are `fail`, so the bits match and neither side is `UNDEFINED`.

Composition: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. The `t+1` reverse/face
bits are a function of the `t` stack on this process: new six-neighbor
records between the cuts do not change earliest incoming `M`.

This is not leftover of unique own-incoming letters (reverse `UNDEFINED`,
face fail). This is not leftover of same-tick-inclusive six-neighbor lock
union (reverse hold, face hold). This is not the two-tick lock-count clock
composition.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the incoming set to be a singleton.
- It does not sum the incoming set.
- It does not replace `M` by locks of six-neighbors.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint unique own-incoming lock-vector letters on these
  x-probes.
- It does not reprint same-tick-inclusive six-neighbor lock union.
- It does not reprint the two-tick lock-count clock composition.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency. The full one-site possibility domain has algebraic presentation `M_2(C)`.
Records form. When present, a record locks exactly one admissible local possibility.
Admissibility determines, for each site, the probability distribution over
the possibilities by a nearest-neighbor rule; it does not supply the formation site, probability, or rate.
The displayed process, the sets `M`, and the reverse/face/composition bits
are additional finite data, not axiom content.

## No-Go Discipline Gate

The negative content here is only the bounded refusal to adopt the bits as
Admissibility, to identify `M` with six-neighbor lock union, to require a
unique incoming letter, or to identify this display with the two-tick
lock-count clock. It is not a claim that reverse cannot hold on another
process.

### N1

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| unique own-incoming letter | replace mixed `M(A)` by a singleton or `UNDEFINED` | `A` has two earliest incoming steps; mixed remains a set; unique-letter reverse is `UNDEFINED` while set reverse fails | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes `+e_1` at `A` and reports reverse hold; `M(A)` is `{+e_2, −e_2}` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores own incoming step sets, not a lock-count clock | ATTEMPTED |
| sum of `M` | replace each set by its `Z^3` sum | the construction does not sum; reverse already fails from the sets | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis; mixed `A` would drop the axis of `e_2` | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading `M` | `τ0(q)=t(q)` and `τ1(q)=t(q)+1` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `M` with six-neighbor
lock union, and missing Record identification of existential opposite are
distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own earliest incoming
set from records with tick `<= τ`, per-probe `τ0=t` and `τ1=t+1`,
existential opposite, four x-probes with non-seed `A`, and composition as
equality of the two-cut bits are declared. No uniqueness of incoming
locks, no six-neighbor lock union as the scored object, no lock-count
clock, no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail`/`HOLD` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest incoming nearest-neighbor step in `M` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets at two cuts and reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** New six-neighbor records between `t` and `t+1` should enlarge
`M`, so reverse or face should flip; mixed `A` should make reverse
`UNDEFINED`; six-neighbor lock union already answered hold/hold on this
same process; unique own-incoming letters already answered reverse
`UNDEFINED` with face fail; the two-tick lock-count clock already answered
two-tick composition; named signs should suffice; and composition HOLD is
only tautological because incoming is frozen at formation.

**Answer:** `M` is earliest incoming from the record prefix. New
six-neighbor records at `t+1` are later arrivals, so they do not enter
`M`. Mixed `A` remains the set `{+e_2, −e_2}`; reverse is `fail`, not
`UNDEFINED`. Six-neighbor lock union is a different object and reports
reverse hold. Unique own-incoming letters drop the mixed set at `A`. The
two-tick lock-count clock composition is a different member. Named signs
lost the axis. Composition HOLD is the displayed fact that the `t+1` bits
equal the `t` bits on this process; it is not an Admissibility rewrite.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same x-probes assigned
`UNDEFINED`, `+e_1`, `+e_1`, `+e_1` and reported reverse `UNDEFINED` with
face fail. A same-tick-inclusive six-neighbor lock union display reported
reverse hold and face hold from five-lock and two-lock neighbor sets. A
two-tick lock-count clock composition scored a different clock, not own
incoming step sets. This note is not those displays: `M` is the own
earliest incoming set, reverse fails, face fails, and composition HOLD
because those bits are unchanged from `t` to `t+1`.

**Gate disposition:** PASS for the two-tick own-incoming-set reverse/face
composition reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals six-neighbor lock union,” “the predicate equals the
two-tick lock-count clock,” “bits are Admissibility,” “reverse holds,”
“face holds,” “composition fails,” or “`M` changes at `t+1`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the z-symmetric three-site
perp-step incoming-lock process, reads each probe's own earliest incoming
set from the record prefix at that probe's `t` and at `t+1`, lists new
records in `B_3(0)` between those cuts that meet a probe's six-neighbors,
and checks Theorems 1--3. It also checks that mixed `A` remains a set, that
unique-letter reverse is `UNDEFINED`, that six-neighbor lock union leftover
holds reverse, that the construction does not sum, that a formation member
from already-recorded six-neighbor locks is not attached, and that the
display is not the two-tick lock-count clock composition. No runner cache
is written.
