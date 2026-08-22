---
claim_id: z_symmetric_three_site_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+1 on the four #7186 z-probes, intersection, and reverse/face of each are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py
---

# Simultaneous Incoming And Outgoing Reverse And Face At t+1 On Four #7186 Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** simultaneous own earliest incoming nearest-neighbor step set `M`
and own outgoing dual `O` at each probe's `τ=t+1`, their intersection, and
reverse/face of each, on the four nszopinz #7186 z-probes in
`B_3(0)={n:n·n<=9}`, no global T. Same process and z-probes as nszopinz
#7186. Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`.
`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. Seeds are a singleton seed letter.
Unformed at `τ` is `UNDEFINED`. `O(q,τ)` is the outgoing dual of `M`: the
set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed in `B_3(0)` and
`e` is in `M(q+e,τ)`. Unformed `q` at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Intersection is `M(q,τ) ∩ O(q,τ)`; unformed is
`UNDEFINED`. Reverse at `τ` holds if and only if `A` and `B` are formed by
that cut and some pair from the scored sets of `A` and `B` sums to
`(0,0,0)`. Face likewise on `C,D`. Empty or `UNDEFINED` on either side is
`UNDEFINED`. This is the first simultaneous display of `M` and `O` at
`t+1` on the nmzpin HOLDING own-incoming member. This is not leftover of
nmt2zp `M` two-tick HOLD/HOLD. This is not leftover of nmot2zp `O`
two-tick. This is not leftover of nmoutzp eventual-`O` hold/hold. This is
not leftover of unique own-incoming or own-outgoing letters. This is not
leftover of mixed #7188 fail/fail. This is not leftover of nmsimopp /
nmsimsy / nmsimzx simultaneous bits on other members. This is not the
two-tick lock-count clock composition. Uniqueness of incoming or outgoing
locks is not required. Mixed remains a set. Occupancy `n` is not used. O
is not M. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at a per-probe cut
`τ=t+1`. Reverse and face of `M` and of `O` are scored on existence of an
opposite pair in each probe's own set at that probe's `t+1`. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock
letter is a different readout and is not used as the object. A `Z^3` sum of
those locks is a different readout and is not used. Occupancy `n` is not
used. A six-neighbor star is not the letter. The construction does not use
occupancy.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of own incoming M and own outgoing O together at t+1 on the four #7186 z-probes, with empty intersection, reverse hold and face hold from M, and reverse hold and face hold from O; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face
target_blocker_text: "display M and O together at t+1 on the four #7186 z-probes, their intersection, and reverse/face of each, no global T"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep simultaneous M, O, intersection, and reverse/face displayed; do not write existential opposite into Admissibility, do not reduce to a unique letter, do not replace O by M, do not replace either set by six-neighbor lock union, do not replace the display by nmt2zp M two-tick or nmot2zp O two-tick, do not use occupancy n, and do not wait for a global later T."
conditional_surface_status: "exact on B_3(0) for simultaneous M and O at t+1 on the four #7186 z-probes, no global T; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose own
incoming sets, outgoing sets, and intersection are scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`,
`C=(0,2,0)`, `D=(1,1,0)`. `A` is a seed. Same process and z-probes as
nszopinz #7186.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,0,1), (0,0,-1)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,0,1)=−e_1`, and `L(0,0,-1)=−e_1`. The
third site is the z-mirror of the two-site opposite-lock partner `(0,0,1)`.
This seed is not the two-site opposite-lock seed `{0,(0,0,1)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
y-symmetric three-site seed `{0,(0,1,0),(0,-1,0)}`. This seed is not the
x-symmetric three-site seed `{0,(1,0,0),(-1,0,0)}`. Same process as nszmenu
#7188 on the x-probes; the scored sites here are the z-probes.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required. Mixed remains a set.

## Named simultaneous sets `M` and `O` at `t+1`

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed in B_3(0) and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate outgoing steps collapse in the set. The
construction does not require `M` or `O` to be a singleton. It does not sum
either set. It does not replace `O` by `M`. It does not replace either set
by locks of six-neighbors of `q`. It does not wait for a global later T.
Occupancy `n` is not used. O is not M.

Intersection at `τ` is `M(q,τ) ∩ O(q,τ)`. If either side is `UNDEFINED`,
the intersection is `UNDEFINED`. Empty intersection is empty, not
`UNDEFINED`.

Reverse from a scored family at `τ` holds if and only if `A` and `B` are
formed by that cut and some `a` in the family at `A` and some `b` in the
family at `B` have `a+b=(0,0,0)`. Face likewise on `C,D`. Empty or
`UNDEFINED` on either side of a comparison is `UNDEFINED`; nonempty with
no opposite pair fails. Reverse/face of `M` and reverse/face of `O` are
separate reports.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not an occupancy-kernel
inner product.

## Theorem 1 — ticks, `M`, `O`, and intersection at `τ=t+1`

On this process the four z-probes form. Compare to nmt2zp: that leftover
reports `M(q,t+1)=M(q,t)` at every scored probe. Compare to nmot2zp: that
leftover reports `O` empty or singleton at `t` and enlarged at `t+1`. Here
`M` and `O` are read together at `τ=t+1`:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_3}
M(D, τ) = {+e_2, −e_2, −e_3}
O(A, τ) = {+e_2, −e_2, +e_3}
O(B, τ) = {+e_2, −e_2, +e_3}
O(C, τ) = {+e_1, −e_1, +e_2, −e_2}
O(D, τ) = {+e_1, −e_1}
M(A, τ) ∩ O(A, τ) = {}
M(B, τ) ∩ O(B, τ) = {}
M(C, τ) ∩ O(C, τ) = {}
M(D, τ) ∩ O(D, τ) = {}
```

`A` is a seed at tick 0. Mixed remains a set: `M(D,τ)` has three incoming
steps and `O(A,τ)` has three outgoing steps. Unique own-incoming letters
would assign `UNDEFINED` at `D`. Unique own-outgoing letters would assign
`UNDEFINED` at `A`, `B`, `C`, and `D`. Here uniqueness is not required.
`M` and `O` are disjoint at each of the four probes at `τ`. Empty
intersection is empty, not `UNDEFINED`. Reverse HOLD of #7186 uses
`−e_1` in `M(A)` against `+e_1` in `M(B)`. Those incoming letters are
absent from `O(A,τ)` and `O(B,τ)`. Reverse HOLD of #7186 does not use an
incoming letter that is also outgoing. O is not M. No six-neighbor star.

This is not leftover of nmt2zp `M` two-tick HOLD/HOLD: that leftover
compares `M` at `t` versus `t+1` and does not display `O` or intersection.
This is not leftover of nmot2zp `O` two-tick: that leftover compares `O` at
`t` versus `t+1` and reports reverse `UNDEFINED` then hold. This is not
leftover of nmoutzp eventual-`O` hold/hold: that leftover reads `M` of
neighbors without a `t+1` simultaneous `M` report. This is not leftover of
unique own-incoming or own-outgoing letters. This is not leftover of mixed
#7188 fail/fail. This is not leftover of nmsimopp / nmsimsy / nmsimzx:
those leftovers use other seeds and other probe families.

## Theorem 2 — reverse/face from `M` at `τ`

Reverse from `M` holds if and only if some `a` in `M(A,τ)` and some `b` in
`M(B,τ)` have `a+b=(0,0,0)`. The sets are `{−e_1}` and `{+e_1}`. The pair
`−e_1+(+e_1)` sums to zero. Reverse holds.

Reverse from M at τ: hold

Face from `M` holds if and only if some `c` in `M(C,τ)` and some `d` in
`M(D,τ)` have `c+d=(0,0,0)`. The sets are `{+e_3}` and `{+e_2, −e_2, −e_3}`.
The pair `+e_3+(−e_3)` sums to zero. Face holds.

Face from M at τ: hold

Unique own-incoming letters on these z-probes report reverse hold and face
`UNDEFINED` from mixed `M(D,τ)`. Same-tick-inclusive six-neighbor lock union
leftover reports reverse fail from `{+e_1}` at neighbors of seed `A`. Those
are different objects. Reverse from `M` holds at `τ` because a pair from
`M(A,τ)` and `M(B,τ)` is opposite.

## Theorem 3 — reverse/face from `O` at `τ`

Reverse from `O` holds if and only if some `a` in `O(A,τ)` and some `b` in
`O(B,τ)` have `a+b=(0,0,0)`. The sets are `{+e_2, −e_2, +e_3}` and
`{+e_2, −e_2, +e_3}`. The pair `+e_2+(−e_2)` sums to zero. Reverse holds.

Reverse from O at τ: hold

Face from `O` holds if and only if some `c` in `O(C,τ)` and some `d` in
`O(D,τ)` have `c+d=(0,0,0)`. The sets are `{+e_1, −e_1, +e_2, −e_2}` and
`{+e_1, −e_1}`. The pair `+e_1+(−e_1)` sums to zero. Face holds.

Face from O at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Unique own-outgoing
letters on these z-probes report reverse `UNDEFINED` and face `UNDEFINED`
from mixed `O` at `τ`. nmot2zp leftover reports reverse `UNDEFINED` at `t`
and hold at `t+1`. nmoutzp eventual-`O` leftover reports reverse hold and
face hold from the same `τ` sets with no simultaneous `M`. Those are
different objects. Reverse from `O` holds at `τ` because a pair from
`O(A,τ)` and `O(B,τ)` is opposite.

At the same cut, reverse/face from `M` hold and reverse/face from `O` hold,
while `M ∩ O` is empty at every scored probe. Simultaneous HOLD of both
families does not mean the families share a letter.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require either set to be a singleton.
- It does not sum either set.
- It does not replace `O` by `M`.
- It does not replace either set by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint unique own-incoming or own-outgoing lock-vector
  letters on these z-probes as the object.
- It does not reprint nmt2zp `M` two-tick HOLD/HOLD.
- It does not reprint nmot2zp `O` two-tick.
- It does not reprint nmoutzp eventual-`O` hold/hold.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not reprint nmsimopp / nmsimsy / nmsimzx simultaneous bits as
  this member.
- It does not use occupancy `n`.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
z-symmetric three-site process, the simultaneous incoming and outgoing sets at
`t+1`, their intersection, and the reverse/face bits of each are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nszopinz #7186 seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen incoming sets |
| `O` at `τ=t+1` | Theorem 1; enlarged outgoing duals |
| intersection `M ∩ O` at `τ` | Theorem 1; empty at each probe |
| reverse and face from `M` at `τ` | Theorem 2; hold / hold |
| reverse and face from `O` at `τ` | Theorem 3; hold / hold |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nmt2zp `M` two-tick HOLD/HOLD | not this display |
| leftover of nmot2zp `O` two-tick | not this display |
| leftover of nmoutzp eventual-`O` hold/hold | not this display |
| leftover of unique own-incoming or own-outgoing letters | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of nmsimopp / nmsimsy / nmsimzx | not this display |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: `M` and `O` together at `t+1` on the four #7186 z-probes, intersection, and reverse/face of each. |
| V2 | Current main has no landed simultaneous incoming-and-outgoing reverse/face at `t+1` on these four #7186 z-probes. |
| V3 | Own incoming sets, own outgoing sets, intersections, and the `hold`/`fail`/`UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads both duals at one cut and scores existence of an opposite pair in each. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace `O` by `M`, does not replace either set by
six-neighbor lock union, does not identify this display with the two-tick
lock-count clock, does not identify the bits with nmt2zp `M` HOLD/HOLD, does
not identify the bits with nmot2zp `O` two-tick, and does not identify the
bits with mixed #7188 fail/fail. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nmt2zp `M` two-tick | reuse earliest incoming `M` at `t` versus `t+1` | that leftover is HOLD/HOLD composition of `M` alone; it does not display `O` or intersection | ATTEMPTED |
| nmot2zp `O` two-tick | reuse outgoing `O` at `t` versus `t+1` | that leftover reports reverse `UNDEFINED` then hold and composition fail; it does not display simultaneous `M` or intersection | ATTEMPTED |
| nmoutzp eventual-`O` | read `O` from eventual neighbor `M` with no `t+1` cut against `M` | that leftover already reports the `τ` outgoing sets and hold/hold; it hides that `M ∩ O` is empty | ATTEMPTED |
| unique own letter | replace mixed `M` or `O` by a singleton or `UNDEFINED` | `M(D,τ)` has three incoming steps and `O(A,τ)` has three outgoing steps; mixed remains a set; unique-letter face from `M` and reverse/face from `O` are `UNDEFINED` | ATTEMPTED |
| empty intersection as `UNDEFINED` | treat empty `M ∩ O` as unformed | both families are formed at `τ`; empty intersection is empty, not `UNDEFINED` | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes `+e_1` at `A` from the origin partner; `M(A,τ)` is `{−e_1}` and `O(A,τ)` does not contain `+e_1` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores own incoming and outgoing step sets at one cut | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail on the x-probes | different probes of this process; this member reports hold/hold from `M` and hold/hold from `O` | ATTEMPTED |
| nmsimopp / nmsimsy / nmsimzx | reuse simultaneous bits on other seeds or probe families | different seeds and probes; not this member | ATTEMPTED |
| sum of `M` or `O` | replace each set by its `Z^3` sum | the construction does not sum; sum of mixed `O(A,τ)` cancels to `+e_3` while the set stays three-element | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis; mixed `A` outgoing at `τ` would drop the axes of `e_2` and `e_3` | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading the sets | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `O` with `M`, and
missing Record identification of existential opposite are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own incoming set and
own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
existential opposite, four z-probes with seed `A`, empty intersection empty
not `UNDEFINED`, mixed remains a set, and simultaneous reverse/face of each
family are declared. No uniqueness of locks, no six-neighbor lock union as
the scored object, no lock-count clock, no global later T, no formation
attachment from already-recorded six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
hold reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest incoming and outgoing nearest-neighbor step | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets, four outgoing sets, four intersections, reverse/face of each | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Because both reverse/face reports HOLD at `t+1`, `M` and `O`
should share a letter, or one family should be dropped as leftover of the
other. nmt2zp already answered `M` hold/hold. nmot2zp already answered `O`
hold at `t+1`. nmoutzp already answered eventual-`O` hold/hold. Empty
intersection should be `UNDEFINED`. Mixed `D` incoming and mixed `A`
outgoing should make face or reverse `UNDEFINED`. Six-neighbor lock union
already answered reverse fail on this same process. Mixed #7188 already
answered fail/fail. nmsimopp / nmsimsy / nmsimzx already answered
simultaneous `M` and `O`. Named signs should suffice. And HOLD of both
families is only tautological because children form at `t+1`.

**Answer:** `M` is earliest incoming from the record prefix. `O` is the
outgoing dual of that prefix. They are disjoint at every scored probe at
`τ`. Empty intersection at a formed probe is empty, not `UNDEFINED`. Mixed
`M(D,τ)` and mixed `O(A,τ)` remain sets; reverse and face hold in each
family. nmt2zp is `M` at two cuts. nmot2zp is `O` at two cuts, with
`UNDEFINED` at `t`. nmoutzp eventual-`O` has no simultaneous `M`.
Six-neighbor lock union is a different object. Mixed #7188 fail/fail is a
different probe family of this process. nmsimopp / nmsimsy / nmsimzx used
other seeds and probes. Named signs lost the axis. Simultaneous HOLD is the
displayed fact that each family has an opposite pair at `t+1`; it is not an
Admissibility rewrite and it does not identify `O` with `M`.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same z-probes assigned
`−e_1`, `+e_1`, `+e_3`, `UNDEFINED` and reported reverse hold with face
`UNDEFINED`. nszopinz #7186 own incoming exist-opposite reported reverse
hold and face hold from `M`. nmt2zp `M` two-tick composition reported
reverse hold and face hold at both cuts with composition HOLD because `M`
is frozen. nmot2zp `O` two-tick composition reported reverse `UNDEFINED`
then hold, face `UNDEFINED` then hold, and composition fail. nmoutzp
eventual-`O` reported reverse hold and face hold from the `τ` outgoing sets
with no simultaneous `M`. Mixed #7188 two-tick composition reported reverse
fail and face fail with composition HOLD. nmsimopp / nmsimsy / nmsimzx
score other seeds or other probe families. A two-tick lock-count clock
composition scored a different clock, not own incoming and outgoing step
sets. This note is not those displays: `M` and `O` are read together at
`t+1` on the four #7186 z-probes, intersection is empty, reverse/face from
`M` hold, and reverse/face from `O` hold.

**Gate disposition:** PASS for the simultaneous incoming-and-outgoing
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals `M` two-tick of nmt2zp,” “the predicate equals nmot2zp
`O` two-tick,” “the predicate equals nmoutzp eventual-`O`,” “the predicate
equals six-neighbor lock union,” “the predicate equals the two-tick
lock-count clock,” “the predicate equals mixed #7188 fail/fail,” “the
predicate equals nmsimopp / nmsimsy / nmsimzx,” “bits are Admissibility,”
“`M` equals `O`,” or “intersection is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nszopinz #7186
perp-step incoming-lock process, reads each probe's own incoming set and
own outgoing dual from the record prefix at that probe's `t+1`, reports
intersection, and checks Theorems 1--3. It also checks that empty
intersection is empty not `UNDEFINED`, that mixed sets remain sets, that
unique-letter reverse/face from `O` at `τ` is `UNDEFINED`, that `O` is
disjoint from `M`, that a formation member from already-recorded
six-neighbor locks is not attached, and that the display is not nmt2zp `M`
two-tick HOLD/HOLD and not nmot2zp `O` two-tick. No runner cache is
written.
