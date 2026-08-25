---
claim_id: two_axis_same_lock_yprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame at t+1 on the four y-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Cyclic Next/Prev Lex-Largest Outgoing Determinant Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four Y-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-largest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that sign, on the
four y-probes of the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same
process and y-probes as nm2sly. `M`, `O`, and split as nm2sl12. Orient as
nm2oricyclz. Let `t(q)` be the formation tick of probe `q`. Let
`τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton
seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Axis
of a defined lock set `S` is `Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs
at `q` if and only if `Axis(M)` intersect `Axis(O)` is empty and `Axis(M)`
union `Axis(O)` equals `{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if
cover HOLDs and `|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required.
When split HOLDs, `m` is the unique vector in `M`. Let `i` in `{1,2,3}` be
the axis index of `m`. `e_next = e_{i+1}` with `3+1→1`. `e_prev = e_{i-1}`
with `1−1→3`. `O_next = O ∩ {±e_next}` and `O_prev = O ∩ {±e_prev}`. If
either is empty, Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next`
is the lex-largest vector in `O_next` (hence `−e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of columns
`m`, `o_next`, `o_prev`. If split fails, Orient fails, not `UNDEFINED`.
Reverse HOLDs if and only if `Orient(A)=Orient(B)` both `±1`. Face HOLDs
if and only if `Orient(C)=Orient(D)` both `±1`. Cover and split do not
score handedness. This is not leftover of nm2oricyclz cyclic next/prev on
opposite z. This is not leftover of nm2orionez lex-one signed outgoing
letters. This is not leftover of nm2chiralz lexicographic unsigned `o1,o2`
orientation. This is not leftover of nm2oridetz unique signed outgoing
letters. This is not leftover of nm2orichz opposite-pair leftover-axis
orientation. This is not leftover of nm2sl axis-cover. This is not leftover
of nm2sl12 1-in 2-out split. This is not leftover of leftover-of-`M` alone.
This is not leftover of leftover-of-`O` alone. This is not leftover-empty
fail of leftover axis. This is not leftover of nmunopp union. This is not
leftover of nmt2opp `M` frozen at `t`. This is not leftover of nmot2opp
two-tick composition. This is not leftover of nmoutopp untimed eventual-`O`.
This is not leftover of mixed #7188 fail/fail. This is not the two-tick
lock-count clock composition. This is not leftover of the
one-axis same-lock two-site seed. This is not leftover of nsopp
`+e_1/−e_1`. This is not leftover of nnseed `+e_1/+e_2`. This is not leftover
of the two-axis opposite seed. The second pair is a new seed, not a formed
child. Uniqueness is not required. Mixed remains a set. A is a seed.
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev oriented
frame is the integer sign of `det(m,o_next,o_prev)` with unique signed
incoming letter `m` and the lex-largest signed outgoing letter on each of
the two cyclic leftover axes of `Axis(M)` under `+e < −e`. Reverse and face
are scored on equal `±1` signs at the paired probes. Named signs `{+,−}` of
locks are a coarser readout and are not used as the object. A singleton
unique outgoing lock letter is a different readout and is not used as the
object. Unsigned axis units of `Axis(O)` are a different readout and are
not used. Unique signed letters requiring `|O_i|=1` are a different readout
and are not used. Lex-one signed letters in axis order `e1<e2<e3` are a
different readout and are not used. Opposite-pair leftover-axis orientation
is a different readout and is not used. Existential opposite of signed locks
is a different readout and is not used. Axis-cover without the frame sign is
a different readout and is not used. 1-in 2-out split without the frame sign
is a different readout and is not used. Leftover-empty fail of unsigned
leftover axis sets is a different readout and is not used. A `Z^3` sum of
those locks is a different readout and is not used. Occupancy of sites is
not used. A six-neighbor star is not the letter. The construction does not
use a six-neighbor star. The construction does not use occupancy.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four y-probes of the two-axis same-lock seed, Orient at A,B,C,D, reverse hold and face fail from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face
target_blocker_text: "display cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame reverse/face on the four y-probes of the two-axis same-lock seed, first display of nm2oricyclz Orient on same-lock y"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to lex-one signed axis order, do not reduce to opposite-pair leftover-axis, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, do not identify this display with nm2oricyclz opposite z, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four y-probes of the two-axis same-lock seed and reverse/face from that sign; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose cyclic
next/prev lex-largest outgoing determinant orientation of `M` and `O` is
scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. A is a seed. Same process and y-probes as nm2sly.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `+e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the two-axis opposite seed
`{0,(0,1,0),(0,0,1),(0,1,1)}` with locks `+e_1/−e_1` and `+e_2/−e_2`. This
seed is not the one-axis same-lock two-site seed `{0,(0,1,0)}` with locks
`+e_1/+e_1`. This seed is not the nnseed two-site seed `+e_1/+e_2`. This
seed is not the opposite two-site seed `+e_1/−e_1`.

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

## Named cyclic next/prev determinant of `M` and `O` at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
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
not require `O` to be a singleton. It does not sum either set. It does not
replace `O` by `M`. It does not wait for a global later T. Occupancy of
sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover at a probe at the same cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

Split at a probe at the same cut:

```text
split(q) HOLDs iff cover HOLDs and |Axis(M)|=1
(hence |Axis(O)|=2).
```

2-in 1-out is fail of split, not UNDEFINED. If `q` is unformed at `τ`, then
split is `UNDEFINED`.

Oriented frame at the same cut:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1→1. e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}. O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is the lex-largest vector in O_next
(hence −e if both signs). o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The outgoing pair is signed and cyclic from `Axis(M)`, not from axis order
`e1<e2<e3`. Mixed opposite signs on one leftover axis make `|O_next|=2` or
`|O_prev|=2`; lex-largest still picks `−e`, so Orient is defined when split
HOLDs and both leftover axes meet `O`. Unique outgoing letters of the whole
set `O` are not required: mixed `O` remains a set, and unique-letter readout
of mixed `O` is `UNDEFINED` while this Orient is a sign. Empty `O_next` or
empty `O_prev` is Orient fail, not `UNDEFINED`. A vanishing determinant is
fail. Sign of a nonzero integer determinant is `+1` or `−1`. Split HOLD
required: 2-in 1-out is Orient fail, not UNDEFINED.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse while leftover reverse fails,
and cover does not score that both signs are `−1`. Identifying split reverse
with this reverse is refused: split HOLDs reverse without a sign, while
lex-one reverse fails on these same probes. Identifying leftover-empty fail
with this reverse is refused: leftover-empty fail scores empty leftover as
reverse fail, while this reverse HOLDs. Identifying lexicographic unsigned
`o1,o2` with this reverse is refused: unsigned reverse HOLDs with `+1,+1`,
while this reverse HOLDs with `−1,−1`. Identifying nm2orionez lex-one signed
outgoing with this reverse is refused: lex-one reverse fails because
`Orient_lex(A)=−1` and `Orient_lex(B)=+1`, while this reverse HOLDs.
Identifying unique signed `|O_i|=1` with this reverse is refused: unique
signed reverse fails because `O(B)` has both `±e_3`. Identifying opposite-pair
leftover-axis orientation with this reverse is refused: leftover-axis reverse
fails because `O(A)` has no opposite pair. Identifying nm2oricyclz opposite-z
cyclic with this reverse is refused: opposite-z cyclic face HOLDs while this
face fails. Identifying a named sign of those locks with reverse or face is
refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, `i`, `o_next`, `o_prev`, and Orient at `τ=t+1`

On this process the four y-probes form. Compare to leftover axis: leftover
is empty at `A`, `B`, and `C`, leftover reverse fails, and leftover face
fails. Compare to nm2sl cover and nm2sl12 split: both HOLD reverse and fail
face on this member. Compare to nm2chiralz lexicographic unsigned `o1,o2`
orientation: reverse HOLDs with `+1,+1` while this reverse HOLDs with
`−1,−1`. Compare to nm2orionez lex-one signed outgoing: reverse fails
because lex-one at `B` picks `+e_3`. Compare to nm2orichz opposite-pair
leftover-axis: reverse fails because `O(A)` has no opposite pair. Compare
to nm2oricyclz cyclic next/prev on opposite z: reverse HOLDs and face HOLDs
there, while this face fails. This display reads cyclic next/prev
lex-largest outgoing determinant of timed `M` and `O` on the two-axis
same-lock y-probes:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {+e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
O(A, τ) = {+e_2, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1}
split(A) = hold
split(B) = hold
split(C) = hold
split(D) = fail
i(A) = 1
o_next(A) = +e_2
o_prev(A) = −e_3
det(A) = -1
Orient(A) = −1
i(B) = 1
o_next(B) = +e_2
o_prev(B) = −e_3
det(B) = -1
Orient(B) = −1
i(C) = 2
o_next(C) = −e_3
o_prev(C) = −e_1
det(C) = 1
Orient(C) = +1
i(D) = fail
o_next(D) = fail
o_prev(D) = fail
det(D) = fail
Orient(D) = fail
```

A is a seed at tick 0 with seed letter `+e_1`. Mixed remains a set:
`O(A,τ)` has two outgoing steps, `O(B,τ)` has three, and `O(C,τ)` has four.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Unique signed
`|O_i|=1` holds at `A` and fails at `B` and at `C`: `O(B)` has both `±e_3`
and `O(C)` has both `±e_1` and both `±e_3`. Cyclic lex-largest at `B` picks
`o_prev=−e_3` from `{+e_3,−e_3}`, so `(o_next,o_prev)=(+e_2,−e_3)` and
Orient is `−1`. Lex-one at `B` picks `+e_3` and Orient is `+1`. `M` is a
singleton at each of `A,B,C,D`, so the unique signed `m` exists. Split HOLDs
at `A`, `B`, and `C`. Split fails at `D` because cover fails from missing
`e_2`; that fail is not 2-in 1-out: `|Axis(M)|=1` at `D`. Orient at `D` is
fail, not `UNDEFINED`. Cover and split HOLD at `A` and at `B` and do not
score that cyclic Orient is `−1,−1`. Unsigned axis-order 2-plane at `A` and
at `B` is `(e_2,e_3)` and lexicographic Orient there is `+1`, while cyclic
`(o_next,o_prev)` is `(+e_2,−e_3)` and Orient is `−1`. Opposite-pair
leftover-axis at `A` fails from no opposite pair in `O`. O is not M.

On the one-axis same-lock two-site seed, `t(B)=2` and `t(D)=3`, cover HOLDs
at `D` as 2-in 1-out, and split fails at `D`, so Orient at `D` is fail, not
UNDEFINED. That is leftover of the first pair. Here both `(0,0,1)` and
`(0,1,1)` are seeds of a second same-lock pair on a second axis. On the
x-probes of this same seed, Orient at `A` fails from split fail, so
oriented x-reverse fails. On the z-probes of this same seed, Orient at `A`
fails from split fail and oriented z-face HOLDs. Those probe-direction
readouts are not this y-probe display.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. The seed site
`(0,1,1)` is a six-neighbor of `A` already recorded at tick 0, so it is not
a new record at `t(A)+1`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at each probe, split
fails, and Orient is fail, not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)=−1` and `Orient(B)=−1`. Reverse holds. This is HOLD iff
equal `±1` signs, not leftover of nm2chiralz lexicographic unsigned
`o1,o2`, not leftover of nm2orionez lex-one signed outgoing letters, not
leftover of nm2oridetz unique signed outgoing letters, not leftover of
nm2orichz opposite-pair leftover-axis, not leftover of nm2sl axis-cover,
not leftover of nm2sl12 1-in 2-out split, not leftover of nm2oricyclz
cyclic next/prev on opposite z, not leftover-empty fail, and not
exist-opposite.

Reverse oriented frame at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Lexicographic unsigned reverse HOLDs because unsigned `Orient(A)=+1` and
`Orient(B)=+1`; those signs are not these signs. Unique signed reverse fails
because unique signed at `B` fails. Opposite-pair leftover-axis reverse
fails because leftover-axis at `A` fails from no opposite pair in `O`.
Lex-one signed reverse fails because lex-one at `A` is `−1` and at `B` is
`+1`. Leftover-empty reverse fails because leftover of the union is empty
at `A` and at `B`. Leftover of `M` reverse HOLDs because leftover of `M` at
`A` and at `B` is `{e_2, e_3}`. Leftover of `O` reverse HOLDs because
leftover of `O` at `A` and at `B` is `{e_1}`. Exist-opposite reverse of
signed `M` fails: `{+e_1}` against `{+e_1}` has no pair summing to zero.
Exist-opposite reverse of signed `O` holds. Presence of an opposite pair in
`O` at `A` fails and at `B` HOLDs, so pair-presence reverse fails. Those
leftovers are not this display.

Reverse holds.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=+1` and `Orient(D)=fail`. Face fails.

Face oriented frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D` from missing `e_2`. Split face
fails because split fails at `D`. Lex-one signed oriented face fails
because Orient at `D` is fail. Lexicographic unsigned face fails because
Orient at `D` is fail. Unique signed face fails. Opposite-pair leftover-axis
face fails. Cover and split do not score handedness. Presence of an opposite
pair in `O` HOLDs at `C` and fails at `D`. On the one-axis same-lock
two-site seed, cover face HOLDs while split face fails at `D` from 2-in
1-out, and Orient at `D` is fail, not UNDEFINED. This two-axis member is
not leftover of that one-axis split face fail: here `D` fails cover from
missing `e_2`, not from 2-in 1-out. The four x-probes of this same seed
give oriented reverse fail and oriented face fail. The four z-probes of
this same seed give oriented reverse fail and oriented face hold. Those
probe-direction readouts are not this y-probe display. On nm2oricyclz
opposite z, cyclic reverse HOLDs and cyclic face HOLDs; this face fails.
Leftover-empty face fails because leftover of the union is empty at `C`
while leftover at `D` is `{e_2}`. Leftover of `M` at `C` is `{e_1, e_3}`
and leftover of `M` at `D` is `{e_1, e_2}`: nonempty and unequal. Leftover
of `O` at `C` is `{e_2}` and leftover of `O` at `D` is `{e_2, e_3}`:
nonempty and unequal. Exist-opposite face of signed `M` fails. Exist-opposite
face of signed `O` holds. Cyclic signed oriented face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `D` and split fails at `D`. Orient at `D`
is fail from split fail, not `UNDEFINED`. Mixed `O(B)` has both signs on
`e_3`; cyclic lex-largest picks `−e_3` while lex-one picks `+e_3`.

Face fails.

## What this note does not claim

- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require outgoing sides to be singletons.
- It does not sum either set.
- It does not replace Orient by leftover-empty fail.
- It does not replace Orient by leftover of `M` alone.
- It does not replace Orient by leftover of `O` alone.
- It does not replace Orient by existential opposite of signed locks.
- It does not replace Orient by presence of an opposite pair in `O`.
- It does not replace Orient by lexicographic unsigned `o1,o2` orientation.
- It does not replace Orient by unique signed `|O_i|=1` letters.
- It does not replace Orient by opposite-pair leftover-axis orientation.
- It does not replace Orient by nm2orionez lex-one signed axis order.
- It does not replace Orient by unsigned axis units of `Axis(O)`.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
- It does not treat empty `O_next` or empty `O_prev` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace Orient by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nm2sl axis-cover reverse hold face fail as this
  oriented display.
- It does not reprint nm2sl12 1-in 2-out split reverse hold face fail as
  this oriented display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2` reverse hold
  with `+1,+1` as this oriented display.
- It does not reprint nm2orionez lex-one reverse fail as this oriented
  display.
- It does not reprint nm2oridetz unique signed reverse fail as this
  oriented display.
- It does not reprint nm2orichz opposite-pair leftover-axis reverse fail as
  this oriented display.
- It does not reprint nm2oricyclz cyclic next/prev reverse hold face hold on
  opposite z as this oriented display.
- It does not reprint the one-axis same-lock two-site seed as this member.
- It does not score the x-probes or the z-probes as this letter.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this oriented display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
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

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis same-lock process, cyclic next/prev lex-largest outgoing determinant
orientation of the 1-in 2-out frame of `M` and `O` at `t+1`, and the
reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock four-site seed `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual at `A,B,C`; singleton at `D` |
| split at `τ` | Theorem 1; hold at `A,B,C`; fail at `D` from missing `e_2` |
| unique signed `m`, cyclic `i`, `(o_next,o_prev)` | Theorem 1; singleton `M`; cyclic pair defined at `A,B,C`; fail at `D` |
| integer `det(m,o_next,o_prev)` | Theorem 1; `-1`, `-1`, `1`, fail |
| Orient at `τ` | Theorem 1; `−1`, `−1`, `+1`, fail |
| reverse from oriented frame at `τ` | Theorem 2; `hold` |
| face from oriented frame at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this oriented display |
| leftover of exist-opposite HOLD | not this oriented display |
| leftover of nm2sl axis-cover HOLD | not this oriented display |
| leftover of nm2sl12 1-in 2-out split HOLD | not this oriented display |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2orionez lex-one signed axis order | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz opposite-pair leftover-axis | not this oriented display |
| leftover of nm2oricyclz cyclic next/prev on opposite z | not this oriented display |
| leftover of opposite-pair presence in `O` | not this oriented display |
| x-probe or z-probe Orient on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the one-axis same-lock two-site seed | not this display |
| leftover of the two-axis opposite seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| empty `O_next` or `O_prev` scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1` on the four y-probes of the two-axis same-lock seed, and reverse/face from that sign. |
| V2 | Current main has no landed cyclic-next/prev-lex-largest-outgoing-determinant reverse/face of timed `M` and `O` on these four y-probes of the two-axis same-lock seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic lex-largest signed outgoing letters from `Axis(M)` at the same `t+1` cut, reverse HOLDs with `−1,−1` while lex-one reverse fails with `−1,+1` and unsigned reverse HOLDs with `+1,+1`, leftover-axis reverse fails, and nm2oricyclz opposite-z face HOLDs while this face fails. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by nm2chiralz lexicographic unsigned `o1,o2`, does not replace
Orient by nm2orionez lex-one signed axis order, does not replace Orient by
nm2oridetz unique signed `|O_i|=1`, does not replace Orient by nm2orichz
opposite-pair leftover-axis, does not replace Orient by nm2sl axis-cover,
does not replace Orient by nm2sl12 1-in 2-out split, does not identify this
display with nm2oricyclz opposite z, and does not identify it with the
one-axis same-lock two-site seed. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse hold and face fail | unsigned reverse HOLDs with `+1,+1` while this reverse HOLDs with `−1,−1`; unsigned `o1,o2` at `A` is `(e_2,e_3)` while cyclic is `(+e_2,−e_3)` | ATTEMPTED |
| nm2orionez lex-one signed axis order | reuse lex-one reverse fail | lex-one at `B` picks `+e_3` so reverse fails; cyclic at `B` picks `−e_3` so reverse HOLDs | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail | unique signed at `B` fails because `|O ∩ {±e_3}|=2`; cyclic still picks `−e_3` | ATTEMPTED |
| nm2orichz opposite-pair leftover-axis | reuse leftover-axis reverse fail | leftover-axis at `A` fails from no opposite pair in `O`; this reverse HOLDs | ATTEMPTED |
| nm2oricyclz cyclic on opposite z | reuse opposite-z reverse hold and face hold | opposite-z face HOLDs with `+1,+1` at `C,D`; this face fails; `t(D)=1` there and `t(D)=2` here | ATTEMPTED |
| nm2sl axis-cover | reuse cover reverse hold and cover face fail on these y-probes | cover reverse HOLDs without a sign; Cover and split do not score handedness | ATTEMPTED |
| nm2sl12 1-in 2-out split | reuse split reverse hold and split face fail | split reverse HOLDs without a sign; lex-one reverse fails on the same split-HOLD probes | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with these bits while this reverse HOLDs; unique signed `O={+e_2,−e_3}` has empty leftover and Orient `−1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` is `{e_2,e_3}`, nonempty equal; leftover of `M` reverse HOLDs without a sign | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` is `{e_1}`, nonempty equal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` fails while Orient reverse HOLDs; exist-opposite face of signed `O` HOLDs while this face fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence fails at `A` so that reverse fails while this reverse HOLDs | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-largest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `−1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both agree; flipping `m` on `O={+e_2,−e_3}` from `+e_1` to `−e_1` flips Orient from `−1` to `+1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` is 1-in 1-out missing `e_2`, not 2-in 1-out | ATTEMPTED |
| empty `O_next` as `UNDEFINED` | treat empty signed outgoing on a cyclic leftover axis as unformed | empty `O_next` or `O_prev` is Orient fail, not UNDEFINED | ATTEMPTED |
| one-axis same-lock two-site seed | reuse `t(B)=2`, `t(D)=3`, cover hold at `D` as 2-in 1-out | different seed; here `t(B)=1`, `t(D)=2`, and cover fails at `D` from missing `e_2` | ATTEMPTED |
| two-axis opposite y-probes | reuse seed letters `−e_1` at `A` and `−e_2` at `(0,1,1)` | `M(A,τ)` is `{+e_1}` here and `{−e_1}` there; opposite-y reverse fails while this reverse HOLDs | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four y-probes | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe reverse fails and z-face HOLDs; this letter is the four y-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-largest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse hold and face fail on the two-axis same-lock seed | ATTEMPTED |
| nsopp `+e_1/−e_1` | reuse opposite two-site seed | nsopp reverse fails; this seed has four sites and reverse HOLDs | ATTEMPTED |
| nnseed `+e_1/+e_2` | reuse nnseed two-site seed | nnseed reverse fails from Orient fail at `B` | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_2−e_3` while cyclic is `(+e_2,−e_3)` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with nm2chiralz lexicographic unsigned `o1,o2`,
missing identification of Orient with nm2orionez lex-one signed axis order,
missing identification of Orient with nm2oridetz unique signed `|O_i|=1`,
missing identification of Orient with nm2orichz opposite-pair leftover-axis,
missing identification of Orient with nm2sl axis-cover, missing
identification of Orient with nm2sl12 1-in 2-out split, missing
identification of this seed with nm2oricyclz opposite z, missing
identification of this seed with the one-axis same-lock two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
`e_next,e_prev` from the axis index of `m`, lex-largest signed outgoing
letter per leftover axis under `+e < −e`, integer determinant sign, empty
`O_next` or `O_prev` as Orient fail not `UNDEFINED`, split fail as Orient
fail not `UNDEFINED`, four y-probes with seed `A`, second pair as a new seed
not a formed child, and mixed remains a set are declared. No uniqueness of
outgoing locks, no six-neighbor lock union as the scored object, no
lock-count clock, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient reverse `hold` and face `fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | unique signed incoming letter and cyclic lex-largest `o_next`, `o_prev` from `Axis(M)` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse hold and face fail are only leftover of nm2sl12
split reverse hold and split face fail; unsigned `o1,o2` already gives reverse
hold and face fail; leftover of `M` alone already answers reverse; leftover
of `O` alone already answers reverse; exist-opposite of signed `O` already
answers reverse; leftover-axis already answers handedness; cyclic on opposite
z already displayed this Orient; lex-one already picks a signed letter on
each leftover axis; mixed #7188 already reported fail/fail; the second pair
is only the formed child of the one-axis seed; unique outgoing letters should
be required; and unsigned incoming axis already gives the same signs because
each `M` letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail.
Orient reverse HOLDs because `Orient(A)=−1` and `Orient(B)=−1`. Orient face
fails because `Orient(D)` is fail. Cover and split HOLD reverse and fail face
on this member and do not score that signed pair. Lexicographic unsigned
`o1,o2` reverse HOLDs with `+1,+1`; this reverse HOLDs with `−1,−1`. Lex-one
signed reverse fails because lex-one at `B` picks `+e_3` while cyclic
lex-largest picks `−e_3`. Unique signed `|O_i|=1` reverse fails because
`O(B)` has both `±e_3`; this reverse HOLDs. Opposite-pair leftover-axis
reverse fails because `O(A)` has no opposite pair; this reverse HOLDs.
nm2oricyclz cyclic next/prev on opposite z reverse HOLDs and face HOLDs;
this face fails, and `t(D)=2` here versus `t(D)=1` there. Presence of an
opposite pair in `O` fails at `A`, so pair-presence reverse fails, while this
reverse HOLDs. Leftover of `M` alone at `A` and at `B` is `{e_2,e_3}`:
nonempty equal without a sign. Leftover of `O` alone at `A` and at `B` is
`{e_1}`. Exist-opposite reverse of signed `M` fails while Orient reverse
HOLDs. Unique outgoing letters would assign `UNDEFINED` at mixed `O(A)`;
this Orient is `−1`, not `UNDEFINED`. On unique signed `O={+e_2,−e_3}`
leftover is empty while Orient is `−1`, so leftover-empty fail is not this
predicate. Mixed #7188 is a different z-symmetric process with mixed `M`.
The second pair is a new seed, not a formed child: `(0,0,1)` is recorded at
tick 0 with lock `+e_2`. Reverse oriented frame is HOLD iff equal `±1` signs
at `A` and at `B`, not leftover of nm2orionez lex-one and not leftover of
nm2sl12 split.

### N8 — cross-cycle echo

nm2sl cover on this two-axis same-lock seed reported cover HOLD at `A,B,C`,
cover fail at `D` from missing `e_2`, reverse hold, and face fail. nm2sl12
1-in 2-out split on the same seed reported split HOLD at `A,B,C`, split fail
at `D`, reverse hold, and face fail. nm2chiralz lexicographic unsigned
`o1,o2` on these y-probes reports Orient `+1,+1,−1,fail`, reverse hold, and
face fail. nm2orionez lex-one signed outgoing letters on these y-probes
reports Orient `−1,+1,−1,fail`, reverse fail, and face fail. nm2orichz
opposite-pair leftover-axis on these y-probes reports Orient fail at `A`
from no opposite pair, reverse fail, and face fail. nm2oricyclz cyclic
next/prev on opposite z reports Orient `−1,−1,+1,+1`, reverse hold, and
face hold. Leftover axis reports empty leftover at `A,B,C`, leftover `{e_2}`
at `D`, leftover reverse fail, and leftover face fail. The four x-probes of
this same seed report cyclic reverse fail and cyclic face fail. The four
z-probes of this same seed report cyclic reverse fail and cyclic face hold.
This note is not those displays: it reports cyclic next/prev lex-largest
outgoing determinant orientation of the 1-in 2-out frame of `M` and `O` at
`τ=t+1` on the two-axis same-lock seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`,
and `t(D)=2`, `Orient(A)=−1`, `Orient(B)=−1`, `Orient(C)=+1`, `Orient(D)=fail`,
reverse hold, and face fail. Cover and split do not score handedness.

**Gate disposition:** PASS for the cyclic-next/prev-lex-largest-outgoing-determinant
`t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals six-neighbor lock union,” “the predicate
equals leftover-empty fail,” “the predicate equals leftover of `M` alone,”
“the predicate equals leftover of `O` alone,” “the predicate equals
leftover-axis reverse,” “the predicate equals cover reverse,” “the
predicate equals nm2sl12 split reverse,” “the predicate equals nm2orionez
lex-one,” “the predicate equals nm2oricyclz opposite z,” “the predicate
equals exist-opposite of signed M,” “bits are Admissibility,” “2-in 1-out
is `UNDEFINED`,” “Orient fails at `A`,” “reverse oriented frame fails,”
“face oriented frame holds,” “cover holds at `D`,” or “empty leftover is
this reverse.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
four-site perp-step incoming-lock process, reads each probe's own earliest
incoming set and own outgoing dual from the record prefix at that probe's
`t+1`, reports 1-in 2-out split, reports axis index `i` of unique signed
`m`, reports cyclic lex-largest `o_next` and `o_prev`, reports the integer
determinant sign, lists new records in `B_3(0)` between `t` and `t+1` that
meet a probe's six-neighbors, and checks Theorems 1--3. It also checks that
Orient is `−1` at `A` and at `B`, `+1` at `C`, and fail at `D`, that reverse
HOLDs and face fails, that leftover empty fails leftover reverse while
Orient reverse HOLDs, that leftover of `M` alone and leftover of `O` alone
are different objects, that exist-opposite of signed M fails reverse, that
lex-one reverse fails while cyclic reverse HOLDs, that unique signed reverse
fails at mixed `O(B)`, that leftover-axis reverse fails from no opposite pair
at `A`, that mixed sets remain sets, that unique-letter Orient is
`UNDEFINED` at mixed `O(A)` while this Orient is `−1`, that split fail is
Orient fail not `UNDEFINED`, that empty `O_next` or `O_prev` is Orient fail
not `UNDEFINED`, that the construction does not sum, that a formation member
from already-recorded six-neighbor locks is not attached, that the display
is not the two-axis opposite leftover process, and that the display is not
nm2oricyclz cyclic next/prev on opposite z.
No runner cache is written.
