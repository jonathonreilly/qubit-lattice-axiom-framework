---
claim_id: y_axis_same_lock_e3_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis-cover of M and O at t+1 on the four #7198 z-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_axis_same_lock_e3_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py
---

# Incoming And Outgoing Axis Cover At t+1 Reverse And Face On Four #7198 Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** axis-cover of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that cover, on the
four nsye3sz #7198 z-probes in `B_3(0)={n:n·n<=9}`. Same process as the
y-axis same-lock `+e_3` two-site seed. Let `t(q)` be the formation tick of
probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds are
a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of
`e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is `Axis(S)={e_i | some ±e_i in
S}`. Cover holds at `q` if and only if `Axis(M)` intersect `Axis(O)` is
empty and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`. Unformed at `τ`
is `UNDEFINED`. Else fail. Reverse holds if and only if cover holds at `A`
and at `B`. Face holds if and only if cover holds at `C` and at `D`. Either
side `UNDEFINED` is `UNDEFINED`. This is not leftover-axis reverse. This is
not leftover of leftover-of-`M` alone. This is not leftover of leftover-of-`O`
alone. This is not leftover of the y-axis opposite `±e_3` seed. This is not
leftover of nsye3sz exist-opposite of signed locks. This is not leftover of
unique-letter mixed `UNDEFINED`. Uniqueness of incoming or outgoing locks is
not required. Mixed remains a set. Occupancy of sites is not used.
Named-sign lettering is not used. The construction does not use a
six-neighbor star. A is not a seed. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1. This note does not write axis-cover
into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks. This display does not use occupancy.
Mixed stays a set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_axis_same_lock_e3_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py`](../scripts/y_axis_same_lock_e3_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Reverse and face are scored on cover at the paired probes. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock
letter is a different readout and is not used as the object. Existential
opposite of signed locks is a different readout and is not used as the
cover reverse: exist-opposite of signed M fails reverse and face on these
z-probes, while cover holds. Leftover-axis equality of nonempty leftovers
is a different readout: leftover empty fails leftover reverse, while cover
holds here. A `Z^3` sum of those locks is a different readout and is not
used. Occupancy of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of axis-cover of M and O at t+1 on the four #7198 z-probes, cover hold at each probe, reverse hold and face hold from cover; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_axis_same_lock_e3_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face
target_blocker_text: "display axis-cover of M and O at t+1 on the four #7198 z-probes, and reverse/face from that cover, no unique lock required"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep axis-cover of M and O at t+1 displayed; do not write cover into Admissibility, do not reduce to leftover-axis reverse, do not reduce to leftover of M alone or leftover of O alone, do not replace cover by existential opposite of signed locks, do not identify the display with nsye3sz exist-opposite HOLD of six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for axis-cover of M and O at t+1 on the four #7198 z-probes and reverse/face from that cover; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose axis-cover
of `M` and `O` is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`,
`C=(2,0,0)`, `D=(1,1,0)`. A is not a seed. Same process and z-probes as
nsye3sz #7198.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
same locks `L(0)=+e_3` and `L(0,1,0)=+e_3`. Those locks are the same letter
and are perpendicular to the seed edge. This seed is not the y-axis opposite
`±e_3` seed `{0,(0,1,0)}` with locks `+e_3/−e_3`. This seed is not the y-axis
opposite `±e_2` seed `{0,(0,1,0)}` with locks `±e_2`. This seed is not the
nnseed two-site seed `+e_1/+e_2`. This seed is not the opposite two-site
seed `+e_1/−e_1`. This seed is not the same-lock two-site seed `+e_1/+e_1`.

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

## Named axis-cover of `M` and `O` at `τ=t+1`

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate steps collapse in the set. The construction does
not require `M` or `O` to be a singleton. It does not sum either set. It
does not replace `O` by `M`. It does not wait for a global later T.
Occupancy of sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover of `M` and `O` at the same cut:

```text
cover(q) HOLD iff Axis(M(q,τ)) intersect Axis(O(q,τ)) is empty
and Axis(M(q,τ)) union Axis(O(q,τ)) equals {e_1,e_2,e_3}.
```

If `q` is unformed at `τ`, then cover is `UNDEFINED`. Else fail. Axis is
unsigned: `+e_i` and `−e_i` occupy the same axis. Cover is complementary
occupation of the three lattice axes. Leftover of the union
`{e_1,e_2,e_3}` minus `(Axis(M) union Axis(O))` empty is weaker: two sides
that both occupy all three axes have empty leftover and fail cover because
the intersection is nonempty. Leftover of `M` alone is a different object.
Leftover of `O` alone is a different object.

Reverse axis-cover holds if and only if cover at `A` and cover at `B` both
HOLD. Face axis-cover holds if and only if cover at `C` and cover at `D`
both HOLD. Either side `UNDEFINED` is `UNDEFINED`. Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-axis reverse with
this reverse is refused: leftover reverse fails when leftover is empty, and
this reverse holds from cover. Identifying existential opposite of signed
locks with cover reverse is refused: exist-opposite of signed M fails
reverse and face here, while cover holds.

## Theorem 1 — ticks, `M`, `O`, `Axis`, and cover at `τ=t+1`

On this process the four z-probes form. Compare to nsye3sz #7198: that
leftover reports same-tick union own incoming lock with exist-opposite
reverse hold and face hold. Exist-opposite of signed `M` on these same
z-probes fails reverse and fails face. This display reads unsigned
axis-cover of timed `M` and `O` on the y-axis same-lock `+e_3` seed:

```text
t(A)=3
t(B)=2
t(C)=4
t(D)=2
M(A, τ) = {+e_1, −e_1, +e_2}
M(B, τ) = {+e_3}
M(C, τ) = {+e_3}
M(D, τ) = {+e_3}
O(A, τ) = {+e_3}
O(B, τ) = {+e_1, −e_1, +e_2}
O(C, τ) = {+e_1, −e_1, −e_2}
O(D, τ) = {+e_1, −e_1, −e_2}
Axis(M)(A, τ) = {e_1, e_2}
Axis(O)(A, τ) = {e_3}
Axis(M)(B, τ) = {e_3}
Axis(O)(B, τ) = {e_1, e_2}
Axis(M)(C, τ) = {e_3}
Axis(O)(C, τ) = {e_1, e_2}
Axis(M)(D, τ) = {e_3}
Axis(O)(D, τ) = {e_1, e_2}
cover(A) = hold
cover(B) = hold
cover(C) = hold
cover(D) = hold
```

A is not a seed. `A` forms at tick 3 by three earliest incoming steps
`+e_1`, `−e_1`, and `+e_2`. Mixed remains a set: `M(A,τ)` has three earliest
incoming steps and `O(B,τ)` has three outgoing steps. Unique letters would
assign `UNDEFINED` at mixed probes. Here uniqueness is not required.
At each probe, `Axis(M)` and `Axis(O)` are complementary: their union is
`{e_1,e_2,e_3}` and their intersection is empty. Cover therefore holds at
each probe. Leftover of the union is empty at each probe. Empty leftover
fails leftover reverse; cover reverse holds here. O is not M. `M` at `τ` is
frozen equal to `M` at `t`. `O` at `t` is empty at each of the four z-probes,
so cover at `t` fails; new records at `t+1` fill `O` and cover holds.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (0, 0, 2)
new 6-NN of B at t(B)+1: (2, 1, 1), (0, 1, 1), (1, 2, 1)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (2, 0, 1), (0, 0, 1), (1, -1, 1)
```

## Theorem 2 — reverse from axis-cover at `τ`

Reverse axis-cover holds if and only if cover at `A` and cover at `B` both
HOLD. Both covers HOLD. Reverse holds.

Reverse axis cover at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Leftover-axis reverse
fails because leftover is empty at `A` and at `B`. Leftover-of-`M`
reverse would fail because leftover of `M` at `A` is `{e_3}` and leftover
of `M` at `B` is `{e_1, e_2}`: nonempty and unequal. Leftover-of-`O`
reverse would fail because leftover of `O` at `A` is `{e_1, e_2}` and
leftover of `O` at `B` is `{e_3}`. Exist-opposite of signed M fails
reverse: `{+e_1, −e_1, +e_2}` against `{+e_3}` has no pair summing to zero.
Those leftovers are not this display.

## Theorem 3 — face from axis-cover at `τ`

Face axis-cover holds if and only if cover at `C` and cover at `D` both
HOLD. Both covers HOLD. Face holds.

Face axis cover at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Leftover-axis face fails because leftover is empty at `C` and at `D`.
Leftover-of-`M` face would hold because leftover of `M` at `C` and at `D`
is `{e_1, e_2}`. Leftover of `O` at `C` and at `D` is `{e_3}`: leftover-of-`O`
face would hold. Exist-opposite of signed M fails face: `{+e_3}` against
`{+e_3}` has no opposite pair. Exist-opposite of signed `O` holds face.
This display scores cover of `Axis(M)` and `Axis(O)`, which holds at `C`
and at `D`, so face holds.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require cover sides to be a singleton.
- It does not sum either set.
- It does not replace cover by leftover of `M` alone.
- It does not replace cover by leftover of `O` alone.
- It does not replace cover by leftover-axis equality of nonempty leftovers.
- It does not replace cover by existential opposite of signed locks.
- It does not replace `O` by `M`.
- It does not replace cover by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint leftover-axis reverse.
- It does not reprint leftover of leftover-of-`M` alone.
- It does not reprint leftover of leftover-of-`O` alone.
- It does not reprint leftover of the y-axis opposite `±e_3` process.
- It does not reprint nsye3sz exist-opposite of signed locks.
- It does not reprint mixed unique-letter `UNDEFINED` as this cover.
- It does not use occupancy of sites as the letter.
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
y-axis same-lock `+e_3` process, axis-cover of `M` and `O` at `t+1`, and the
reverse/face bits from cover are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; y-axis same-lock two-site seed `+e_3/+e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary at each probe |
| cover at `τ` | Theorem 1; hold at each probe |
| reverse from cover at `τ` | Theorem 2; `hold` |
| face from cover at `τ` | Theorem 3; `hold` |
| unique lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-axis reverse | not this cover display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of y-axis opposite `±e_3` z-probes | not this display |
| leftover of nsye3sz exist-opposite of signed locks | not this display |
| global later T | not used |
| axis-cover as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: axis-cover of `M` and `O` at `t+1` on the four #7198 z-probes, and reverse/face from that cover. |
| V2 | Current main has no landed axis-cover reverse/face of timed `M` and `O` on these four #7198 z-probes. |
| V3 | Cover bits at one cut and the two cover reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned axis-cover of own incoming and own outgoing at the same `t+1` cut and scores reverse/face from cover. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace cover by leftover of `M` alone or leftover of
`O` alone, does not replace cover by leftover-axis reverse, does not
replace cover by existential opposite of signed locks, and does not
identify this display with nsye3sz exist-opposite HOLD of six-neighbor lock
union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-axis reverse | score nonempty leftover-axis equality | leftover empty at each probe, leftover reverse fail, leftover face fail; cover reverse hold | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_3}` and at `B` is `{e_1,e_2}`, nonempty unequal; reverse of leftover of `M` fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_1,e_2}` and at `B` is `{e_3}`, nonempty unequal; reverse of leftover of `O` fails | ATTEMPTED |
| leftover of y-axis opposite `±e_3` | reuse seed `{0,(0,1,0)}` with locks `+e_3/−e_3` | this seed locks `+e_3/+e_3`; perp-step sees only the lock axis so timed `M` and `O` on these z-probes coincide, while the seed letter at `(0,1,0)` differs | ATTEMPTED |
| leftover of y-axis opposite `±e_2` | reuse seed `{0,(0,1,0)}` with locks `±e_2` | cover at `B` fails and cover at `D` fails; reverse fail | ATTEMPTED |
| leftover of nnseed `+e_1/+e_2` | reuse nnseed two-site seed | cover at `B` fails; reverse fail | ATTEMPTED |
| leftover of nsopp `+e_1/−e_1` | reuse opposite two-site seed | `M(A,τ)` there is `{+e_3}` at tick 1; here `M(A,τ)` is mixed at tick 3 | ATTEMPTED |
| leftover of same-lock `+e_1/+e_1` | reuse same-lock two-site seed on `e_1` | seed letters here are `+e_3/+e_3` | ATTEMPTED |
| leftover of x-probes on this seed | reuse `A=(1,0,0)` | x-probe `A` has `M={+e_1}` at tick 1; z-probe `A` is mixed at tick 3 | ATTEMPTED |
| leftover of y-probes on this seed | reuse `A=(0,1,0)` | y-probe `A` is a seed; z-probe `A` is not a seed | ATTEMPTED |
| nsye3sz exist-opposite | reuse signed reverse hold and face hold of six-neighbor lock union | those bits HOLD from signed opposite pairs in neighbor locks; exist-opposite of signed M fails; cover is unsigned complementary axes | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(A,τ)` remains a set; unique-letter cover at `A` is `UNDEFINED`; cover still holds | ATTEMPTED |
| shared-axis leftover empty | both sides occupy all three axes | leftover empty, cover fails because intersection is nonempty | ATTEMPTED |
| exist-opposite of signed locks | score `a+b=(0,0,0)` inside `M` or `O` | exist-opposite of signed M fails reverse and face; cover holds | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes partner locks; cover is unsigned complementary axes of `M` and `O` | ATTEMPTED |
| sum of a set | replace cover by a `Z^3` sum | the construction does not sum; `M(A,τ)` sums to `+e_2` while `Axis(M)(A)` is `{e_1,e_2}` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by axis-cover | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of cover with leftover-axis
reverse, missing identification of cover with leftover of `M` alone, missing
identification of cover with exist-opposite of signed `M`, and missing Record
identification of cover reverse are distinct open premises. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, y-axis same-lock two-site seed locks `+e_3` and `+e_3`,
perpendicular step rule, incoming-step lock, own incoming set and own
outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`, unsigned
axis, cover as empty intersection and three-axis union, four z-probes with
`A` not a seed, and mixed remains a set are declared. No uniqueness of
lock, no six-neighbor lock union as the scored object, no leftover-axis
equality as the scored reverse, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
cover `hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four cover bits, reverse/face from cover | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for cover reverse/face, a
formation-rate rule, and a physical selector among complementary axis
splits. None is taken here.

### N7 — hostile steelman

**Steelman:** Cover HOLD is only leftover empty; reverse HOLD is only
nsye3sz exist-opposite HOLD of six-neighbor lock union; leftover of `M`
alone already gives a third direction; leftover of `O` alone already
gives the complementary axes; y-axis opposite `±e_3` already gives the
same timed `M` and `O` on these z-probes; x-probes and y-probes on this
seed also hold cover; and complementary occupation is only three-axis
covering already implied by leftover empty.

**Answer:** Leftover empty is unsigned union equal to `{e_1,e_2,e_3}`. Cover
also requires empty intersection. Two sides that occupy all three axes have
empty leftover and fail cover. Leftover reverse fails on empty leftover;
cover reverse holds. Exist-opposite HOLD of six-neighbor lock union is a
signed pair readout; exist-opposite of signed M fails reverse and face on
these z-probes while cover holds. Leftover of `M` alone and leftover of `O`
alone are one-sided leftovers; leftover-of-`M` reverse fails here. The
y-axis opposite `±e_3` seed locks `−e_3` at `(0,1,0)`; this seed locks
`+e_3`. X-probes and y-probes are different frames: y-probe `A` is a seed
and x-probe `A` has singleton `M={+e_1}` at tick 1. Cover reverse is HOLD
of cover at `A` and at `B`, not leftover-axis equality and not exist-opposite
of signed locks.

### N8 — cross-cycle echo

nsye3sz #7198 reported reverse hold and face hold from same-tick union own
incoming lock on these four z-probes. Exist-opposite of signed `M` on the
same process fails reverse and fails face. Leftover-axis reverse fails
because leftover is empty. This note is not those displays: it reports
axis-cover of `M` and `O` at `τ=t+1` on the y-axis same-lock `+e_3` seed,
cover hold at each of the four z-probes, reverse hold, and face hold.

**Gate disposition:** PASS for the axis-cover `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover of `M` alone,”
“the predicate equals leftover of `O` alone,” “the predicate equals
leftover-axis reverse,” “the predicate equals nsye3sz exist-opposite HOLD,”
“the predicate equals exist-opposite of signed M,” “bits are Admissibility,”
“cover fails,” “reverse axis-cover fails,” “face axis-cover fails,” or
“empty leftover is this reverse.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the y-axis same-lock
two-site perp-step incoming-lock process, reads each probe's own earliest
incoming set and own outgoing dual from the record prefix at that probe's
`t+1`, reports unsigned axis of each, reports cover of the union, lists new
records in `B_3(0)` between `t` and `t+1` that meet a probe's six-neighbors,
and checks Theorems 1--3. It also checks that cover holds at each probe,
that leftover empty fails leftover reverse while cover reverse holds, that
leftover of `M` alone and leftover of `O` alone are different objects, that
exist-opposite of signed M fails reverse and face, that mixed sets remain
sets, that unique-letter cover is `UNDEFINED` at mixed `M(A)`, that
shared-axis leftover empty fails cover, that the construction does not
sum, that a formation member from already-recorded six-neighbor locks is
not attached, and that the display is not the y-axis opposite `±e_3`
leftover process. No runner cache is written.
