---
claim_id: z_symmetric_three_site_sametick_union_own_two_tick_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse/face from S⁺ at t versus t+1 on the four #7188 x-probes, and whether those bits compose, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py
---

# Two-Tick Composition Of Same-Tick Union Own Reverse And Face On Four Z-Symmetric Three-Site X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from `S^+` at each probe's formation tick `t`
versus `t+1`, on the four z-symmetric three-site x-probes in
`B_3(0)={n:n·n<=9}`, no global T. Let `t(q)` be the formation tick of
probe `q`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. Let `L(q)` be `q`'s own
unique incoming lock; seeds use seed letters. If several earliest incoming
steps exist, `L(q)` is `UNDEFINED`. At cut `τ`, `S^+(q,τ)` is the set of
locks of six-neighbors of `q` that formed at tick `<= τ` and are not `q`,
union `{L(q)}` when `L(q)` is defined and `t(q)<=τ`. Reverse at a cut holds
if and only if `A` and `B` are formed by that cut and some `a` in
`S^+(A,·)` and some `b` in `S^+(B,·)` have `a+b=(0,0,0)`. Face likewise on
`C,D`. Empty or `UNDEFINED` on either side is `UNDEFINED`. Composition
HOLD if and only if the `t+1` reverse/face bits equal the `t` bits (neither
side `UNDEFINED`, or both `UNDEFINED`). This is not leftover of own
incoming sets `M` (those fail/fail bits are frozen). Uniqueness of incoming
locks is not required. Mixed remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in
`S^+` at that probe's `t` and at `t+1`. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock letter is a different
readout and is not used. An own earliest incoming set `M` is a different
readout and is not used. A `Z^3` sum of those locks is a different readout
and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ at each of the four z-symmetric three-site x-probes at t and at t+1, with reverse hold, face hold, and composition HOLD because t+1 bits equal t bits; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_sametick_union_own_two_tick_composition_reverse_face
target_blocker_text: "display reverse and face from S^+ at t versus t+1 on the four z-symmetric three-site x-probes, no global T, and whether those bits compose"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse, face, and composition displayed; do not write existential opposite into Admissibility, do not reduce to a unique incoming letter, do not replace S^+ by own incoming M, do not replace S^+ by a lock-count clock, and do not wait for a global later T."
conditional_surface_status: "exact on B_3(0) for two-tick composition of S^+ reverse/face on the four z-symmetric three-site x-probes, no global T; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose `S^+`
sets are scored:

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

## Named `S^+` at `t` and at `t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There is no global T.

Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}`. Seeds use seed
letters. If several earliest incoming steps exist, `L(q)` is `UNDEFINED`.

At cut `τ`, `S^+(q,τ)` is the set of locks of six-neighbors of `q` that
formed at tick `<= τ` and are not `q`, union `{L(q)}` when `L(q)` is
defined and `t(q)<=τ`. Same-tick partners are kept when they are neighbors.
The probe itself is excluded from the neighbor set and re-enters only
through `{L(q)}` when that letter is defined and the probe is already
formed. Duplicate locks collapse in the set. The construction does not
require `S^+(q,τ)` to be a singleton. It does not sum `S^+(q,τ)`. It does
not replace `S^+` by the own earliest incoming set `M`. It does not wait
for a global later T.

Reverse at a cut holds if and only if `A` and `B` are formed by that cut
and some `a` in `S^+(A,·)` and some `b` in `S^+(B,·)` have `a+b=(0,0,0)`.
Face at a cut holds if and only if `C` and `D` are formed by that cut and
some `c` in `S^+(C,·)` and some `d` in `S^+(D,·)` have `c+d=(0,0,0)`. Empty
or `UNDEFINED` on either side of a comparison is `UNDEFINED`; nonempty with
no opposite pair fails.

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`, with neither side `UNDEFINED` or both
sides `UNDEFINED`. Else composition fails. Displayed, not adopted.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero inside `S^+`.

## Theorem 1 — ticks, `S^+` at `τ0` and at `τ1`, and new six-neighbor records

On this process the four x-probes form. Own unique incoming letters are
`L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`, and `L(D)=+e_1`. Mixed `A`
remains a set: two earliest incoming steps `+e_2` and `−e_2`, so `L(A)`
does not re-enter. The same-tick-inclusive union sets at each probe's `t`
and at `t+1` are:

```text
t(A)=3
t(B)=2
t(C)=4
t(D)=2
S^+(A, τ0) = {+e_1, +e_2, −e_2, +e_3, −e_3}
S^+(B, τ0) = {+e_1, +e_2}
S^+(C, τ0) = {+e_1, +e_2, −e_2}
S^+(D, τ0) = {+e_1, +e_2}
S^+(A, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}
S^+(B, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}
S^+(C, τ1) = {+e_1, +e_2, −e_2}
S^+(D, τ1) = {+e_1, +e_2, −e_2}
```

New records in `B_3(0)` between `τ0` and `τ1` that meet a probe's
six-neighbors are:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 0, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0)
new 6-NN of D at t(D)+1: (1, 2, 0), (1, 0, 0)
```

The new neighbor `(2, 0, 0)` of `A` is probe `C`, formed at tick 4 with
incoming `+e_1`, already in `S^+(A,τ0)`, so `S^+(A,τ1)=S^+(A,τ0)`. The new
neighbors of `B` add `−e_2`, `+e_3`, and `−e_3`, so `S^+(B,τ1)` is strictly
larger than `S^+(B,τ0)`. The new neighbors of `C` carry `{+e_2, −e_2}`,
already in `S^+(C,τ0)`, so `S^+(C,τ1)=S^+(C,τ0)`. The new neighbors of `D`
add `−e_2`, so `S^+(D,τ1)` is strictly larger than `S^+(D,τ0)`.

This is not leftover of own incoming sets `M`: that readout is
`M(A)={+e_2, −e_2}` and `M(B)=M(C)=M(D)={+e_1}`, with reverse fail and face
fail, and those `M` sets are frozen from `t` to `t+1`. Here `S^+` at `B`
and at `D` changes at `t+1`. This is not leftover of unique own-incoming
letters: that readout would replace mixed `A` by `UNDEFINED`. This is not
the two-tick lock-count clock composition.

## Theorem 2 — reverse and face at `τ0` and at `τ1`

Reverse holds if and only if some `a` in `S^+(A,·)` and some `b` in
`S^+(B,·)` have `a+b=(0,0,0)`. At `τ0` the sets are
`{+e_1, +e_2, −e_2, +e_3, −e_3}` and `{+e_1, +e_2}`. The pair `−e_2` at `A`
and `+e_2` at `B` sums to zero. Reverse holds. `L(A)` is `UNDEFINED`, so
reverse HOLD does not use `L(A)`. At `τ1` the `B` set enlarges, and the
same opposite pair remains, so reverse holds again. Both sides are nonempty
and defined, so this is not `UNDEFINED`.

Reverse at τ0: hold
Reverse at τ1: hold

Face holds if and only if some `c` in `S^+(C,·)` and some `d` in
`S^+(D,·)` have `c+d=(0,0,0)`. At `τ0` the sets are `{+e_1, +e_2, −e_2}`
and `{+e_1, +e_2}`. The pair `−e_2` at `C` and `+e_2` at `D` sums to zero.
Face holds. At `τ1` the `D` set enlarges by `−e_2`, and the same opposite
pair remains, so face holds again.

Face at τ0: hold
Face at τ1: hold

Own incoming sets `M` on these x-probes report reverse fail and face fail.
Unique own-incoming letters report reverse `UNDEFINED` from mixed `A`.
Those are different objects.

## Theorem 3 — composition

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`. Both reverse reports are `hold` and both
face reports are `hold`, so the bits match and neither side is `UNDEFINED`.

Composition: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Composition HOLD is
equality of the reverse/face bits, not equality of the `S^+` sets: `S^+`
at `B` and at `D` grows from `t` to `t+1`, while the bits stay `hold`.

This is not leftover of own incoming sets `M` (reverse fail, face fail,
composition HOLD on frozen `M`). This is not leftover of unique
own-incoming letters (reverse `UNDEFINED`, face fail). This is not the
two-tick lock-count clock composition.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require `S^+` to be a singleton.
- It does not sum `S^+`.
- It does not replace `S^+` by own incoming sets `M`.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint unique own-incoming lock-vector letters on these
  x-probes.
- It does not reprint own-incoming-set reverse/face composition.
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
The displayed process, the sets `S^+`, and the reverse/face/composition bits
are additional finite data, not axiom content.

## No-Go Discipline Gate

The negative content here is only the bounded refusal to adopt the bits as
Admissibility, to identify `S^+` with own incoming `M`, to require a unique
incoming letter, or to identify this display with the two-tick lock-count
clock. It is not a claim that reverse cannot fail on another process.

### N1

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| unique own-incoming letter | replace mixed `A` by a singleton or `UNDEFINED` | `A` has two earliest incoming steps; mixed remains a set; unique-letter reverse is `UNDEFINED` while `S^+` reverse holds | ATTEMPTED |
| own incoming set `M` | score earliest incoming nearest-neighbor steps at the probe | `M` reports reverse fail and face fail with frozen sets; `S^+` reports hold/hold and `S^+(B)` grows | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores `S^+`, not a lock-count clock | ATTEMPTED |
| sum of `S^+` | replace each set by its `Z^3` sum | the construction does not sum; reverse already holds from a pair | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading `S^+` | `τ0(q)=t(q)` and `τ1(q)=t(q)+1` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `S^+` with own
incoming `M`, and missing Record identification of existential opposite are
distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, same-tick-inclusive
six-neighbor locks union own unique incoming lock when defined, per-probe
`τ0=t` and `τ1=t+1`, existential opposite, four x-probes with non-seed `A`,
and composition as equality of the two-cut bits are declared. No uniqueness
of incoming locks, no replacement of `S^+` by `M`, no lock-count clock, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold`/`HOLD` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in `S^+` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `S^+` sets at two cuts and reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** New six-neighbor records between `t` and `t+1` enlarge `S^+`
at `B` and at `D`, so reverse or face should flip; mixed `A` should make
reverse `UNDEFINED`; own incoming `M` already answered fail/fail with
composition HOLD on this same process; unique own-incoming letters already
answered reverse `UNDEFINED`; the two-tick lock-count clock already answered
two-tick composition; named signs should suffice; and composition HOLD is
only tautological because `S^+` is frozen at formation.

**Answer:** Reverse and face are existential opposite of `S^+`, not equality
of the sets. `S^+(B)` and `S^+(D)` grow, yet the opposite pairs that already
hold at `t` remain at `t+1`, so the bits stay `hold`. Mixed `A` leaves
`L(A)` undefined; `S^+(A)` is the neighbor-lock set and reverse holds from
`−e_2` already in that set. Own incoming `M` is a different object and
reports fail/fail. Unique own-incoming letters drop the mixed set at `A`.
The two-tick lock-count clock composition is a different member. Named signs
lost the axis. Composition HOLD is the displayed fact that the `t+1` bits
equal the `t` bits on this process; it is not an Admissibility rewrite and
it is not leftover of frozen `M`.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same x-probes assigned
`UNDEFINED`, `+e_1`, `+e_1`, `+e_1` and reported reverse `UNDEFINED` with
face fail. An own-incoming-set two-tick composition on these same x-probes
reported reverse fail, face fail, and composition HOLD on frozen `M`. A
same-tick-inclusive six-neighbor lock union display at each probe's `t`
already reported reverse hold and face hold from five-lock and two-lock
sets. A two-tick lock-count clock composition scored a different clock.
This note is not those displays: `S^+` is read at `t` and at `t+1`, reverse
holds, face holds, `S^+` at `B` and at `D` grows, and composition HOLD
because those bits are unchanged from `t` to `t+1`.

**Gate disposition:** PASS for the two-tick `S^+` reverse/face composition
reports above. FAIL / DO NOT SHIP for “the predicate equals the named
sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals own incoming `M`,” “the predicate equals the two-tick
lock-count clock,” “bits are Admissibility,” “reverse fails,” “face fails,”
“composition fails,” or “the `S^+` bits change at `t+1`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the z-symmetric three-site
perp-step incoming-lock process, reads `S^+` at each probe's `t` and at
`t+1`, lists new records in `B_3(0)` between those cuts that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that mixed `A`
remains a set, that unique-letter reverse is `UNDEFINED`, that own incoming
`M` leftover fails reverse, that `S^+(B)` grows while reverse stays hold,
that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, and that the display
is not the two-tick lock-count clock composition. No runner cache
is written.
