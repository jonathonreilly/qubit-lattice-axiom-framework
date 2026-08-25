---
claim_id: two_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame at t+1 on the four x-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Cyclic Next/Prev Lex-Smallest Outgoing Determinant Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four X-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-smallest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that sign, on the
four x-probes of the two-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same
process and x-probes as nm2axx. `M`, `O`, and split as nm2ax12x. Orient as
nm2oricyccz. Let `t(q)` be the formation tick of probe `q`. Let
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
with `1−1→3`. `O_next = O ∩ {±e_next}`. `O_prev = O ∩ {±e_prev}`. If either
empty, Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next` is the
lex-smallest vector in `O_next` (hence `+e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. Reverse HOLDs if and only if `Orient(A)=Orient(B)` both
`±1`. Face HOLDs if and only if `Orient(C)=Orient(D)` both `±1`. Cover and
split do not score handedness. This is not leftover of nm2axx axis-cover.
This is not leftover of nm2ax12x 1-in 2-out split. This is not leftover of
nm2oricyccz z-probe cyclic. This is not leftover of nm2oricycx lex-largest.
This is not leftover of lex-one axis-order. This is not leftover of
lex-largest cyclic. This is not leftover of
lexicographic unsigned `o1,o2`. This is not leftover of unique signed
`|O_i|=1`. This is not leftover of leftover-of-`M` alone. This is not
leftover of leftover-of-`O` alone. This is not leftover-empty fail. This
is not leftover of y-probe cyclic. This is not leftover of nmunopp union.
This is not leftover of nmt2opp `M` frozen at `t`. This is not leftover of
nmot2opp two-tick composition. This is not leftover of nmoutopp untimed
eventual-`O`. This is not leftover of mixed #7188 fail/fail. This is not
leftover of the 1-axis opposite two-site seed. This is not leftover of the
same-lock two-site seed. The second pair is a new seed, not a formed
child. A is not a seed. Uniqueness is not required. Mixed remains a set.
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev lex-smallest
oriented frame is the integer sign of `det(m,o_next,o_prev)` with unique
signed incoming letter `m` of axis index `i`, `e_next` and `e_prev` the
cyclic neighbors of that axis, and the lex-smallest signed outgoing letter
on each of those axes under `+e < −e`. Reverse and face are scored on
equal `±1` signs at the paired probes. Named signs `{+,−}` of locks are a
coarser readout and are not used as the object. A singleton unique
outgoing lock letter is a different readout and is not used as the object.
Unsigned axis units of `Axis(O)` are a different readout and are not used.
Lex-one signed letters in axis order `e1<e2<e3` are a different readout
and are not used. Lex-largest cyclic next/prev is a different readout and
is not used. Unique signed letters requiring `|O_i|=1` are a different
readout and are not used. Existential opposite of signed locks is a
different readout and is not used. Axis-cover without the frame sign is a
different readout and is not used. 1-in 2-out split without the frame sign
is a different readout and is not used. Leftover-empty fail of unsigned
leftover axis sets is a different readout and is not used. A `Z^3` sum of
those locks is a different readout and is not used. Occupancy of sites is
not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the two-axis opposite seed, Orient fail,+1,-1,fail, reverse fail and face fail from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face
target_blocker_text: "display cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame reverse/face on the four x-probes of the two-axis opposite seed, first display of nm2oricyccz Orient on x-probes"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to lex-one axis-order, do not reduce to lex-largest cyclic, do not reduce to z-probe cyclic, do not reduce to y-probe cyclic, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the two-axis opposite seed and reverse/face from that sign; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose cyclic
next/prev lex-smallest outgoing determinant orientation of `M` and `O` is
scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. A is not a seed. Same process and x-probes as
nm2axx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`. This seed is not the y-axis opposite `±e_2` seed.

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

## Named cyclic next/prev lex-smallest determinant of `M` and `O` at `τ=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
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
e_next = e_{i+1} with 3+1→1.
e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}.
O_prev = O ∩ {±e_prev}.
If O_next or O_prev is empty, Orient fails, not UNDEFINED.
Else o_next is the lex-smallest vector in O_next under +e < −e
(hence +e if both signs). o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The outgoing pair is signed and cyclic from `Axis(M)`, not axis-order of
`Axis(O)`. Mixed opposite signs on one outgoing cyclic axis make that
`O_next` or `O_prev` of size 2; lex-smallest still picks `+e`, so Orient is
defined when split HOLDs and both cyclic sides are nonempty. Unique
outgoing letters of the whole set `O` are not required: mixed `O` remains
a set, and unique-letter readout of mixed `O` is `UNDEFINED` while this
Orient is a sign. Empty `O_next` or `O_prev` is Orient fail, not
`UNDEFINED`. A vanishing determinant is fail. Sign of a nonzero integer
determinant is `+1` or `−1`. Split HOLD required: cover fail or 2-in 1-out
is Orient fail, not UNDEFINED.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse fails here as well, but cover is
unsigned occupation and does not report `Orient(B)=+1`. Identifying split
reverse with this reverse is refused: split reverse fails from split fail
at `A`, while this Orient at `B` is `+1` and at `C` is `−1` on two split
HOLD sites. Identifying leftover-empty fail with this reverse is refused:
leftover at `A` is `{e_2}` and leftover at `B` is empty. Identifying
lex-one axis-order with this reverse is refused: lex-one at `B` is `+1`,
the same sign as cyclic lex-smallest at `B`, but lex-one is axis-order of
`Axis(O)` and is not cyclic from `Axis(M)`. Identifying nm2oricycx
lex-largest cyclic with this reverse is refused: lex-largest cyclic at
`B` is `−1` and at `C` is `+1`. Identifying unique signed `|O_i|=1` with
this reverse is refused: unique signed fails at `B` and at `C` from mixed
`±e_3`. Identifying unsigned cyclic `+e_next,+e_prev` with this reverse is
refused: unsigned cyclic at `B` is `+1` and at `C` is `+1`, while this
Orient at `C` is `−1`. Identifying y-probe cyclic with this reverse is
refused: y-probe cyclic reverse HOLDs from `+1,+1` while this x-probe
reverse fails. Identifying z-probe cyclic with this reverse is refused:
z-probe cyclic reverse HOLDs and z-probe cyclic face HOLDs. Identifying a
named sign of those locks with reverse or face is refused: named-sign
lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, `i`, `o_next`, `o_prev`, and Orient at `τ=t+1`

On this process the four x-probes form. Compare to nm2axx cover and
nm2ax12x split: both fail reverse and fail face on this member from cover
fail at `A` and at `D`. Compare to leftover axis: leftover `{e_2}` at `A`
and empty leftover at `B`. Compare to lex-one axis-order: lex-one at `B`
is `+1` and at `C` is `−1`, the same signs as this letter on these
x-probes, from axis-order of `Axis(O)` rather than cyclic slots of
`Axis(M)`. Compare to nm2oricycx lex-largest: reverse fails and face fails
with Orient `fail,−1,+1,fail`. Compare to nm2oricyccz z-probe cyclic:
reverse HOLDs and face HOLDs on those z-probes. This display reads the
cyclic next/prev lex-smallest outgoing determinant of those same timed
sets on the x-probes:

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ) = {−e_3}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {−e_3}
O(A, τ) = {+e_1}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {−e_2, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
split(A) = fail
split(B) = hold
split(C) = hold
split(D) = fail
i(A) = fail
o_next(A) = fail
o_prev(A) = fail
Orient(A) = fail
i(B) = 1
o_next(B) = +e_2
o_prev(B) = +e_3
det(B) = 1
Orient(B) = +1
i(C) = 1
o_next(C) = −e_2
o_prev(C) = +e_3
det(C) = -1
Orient(C) = −1
i(D) = fail
o_next(D) = fail
o_prev(D) = fail
Orient(D) = fail
```

A is not a seed. `A` forms at tick 2 by the incoming step `−e_3`. Mixed
remains a set: `O(B,τ)` has three outgoing steps and `O(D,τ)` has two.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Unique
signed `|O_i|=1` fails at `B` and at `C` because each has both `±e_3`.
Lex-smallest picks `+e_3` on that mixed cyclic prev axis. `M` is a
singleton at each probe. Split fails at `A` and at `D` from leftover
`{e_2}`, so `i`, `o_next`, `o_prev`, and Orient fail there, not
`UNDEFINED`. At `B` and at `C`, `m=+e_1` so `i=1`, `e_next=e_2`, and
`e_prev=e_3`. Cover and split HOLD at `B` and at `C` and do not score that
cyclic lex-smallest Orient is `+1` then `−1`. Lex-one axis-order at `B` is
`(+e_2,+e_3)` and Orient `+1`, the same sign as this letter at `B`.
Lex-largest cyclic at `B` is `−1` from `o_prev=−e_3`. Unsigned cyclic
`+e_2,+e_3` at `B` is `+1` and at `C` is `+1`, while this Orient at `C` is
`−1` from `o_next=−e_2`. O is not M.

On the 1-axis opposite two-site seed, `A=(1,0,0)` forms later with mixed
incoming, cover HOLDs at each x-probe, and split fails at `A` from 2-in
1-out, so Orient at `A` is fail, not UNDEFINED. That is leftover of the
first pair. Here four sites are seeds of two opposite pairs. On the
y-probes of this same seed, split HOLDs at `A` and at `B`, cyclic
lex-smallest Orient is `+1` at `A` and `+1` at `B`, so y-reverse HOLDs
and y-split reverse HOLDs while this x-reverse fails. On the z-probes,
cyclic lex-smallest Orient is `+1,+1,−1,−1`, so z-reverse HOLDs and
z-face HOLDs. Those probe-direction readouts are not this x-probe display.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `B`, and
`C`; at `D`, `O` at `t` is already `{−e_1}` from the seed neighbor
`(0,1,0)`. Split fails at `t` and Orient is fail, not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)=fail` and `Orient(B)=+1`. Reverse fails. This is HOLD
iff equal `±1` signs, not leftover of nm2axx axis-cover, not leftover of
nm2ax12x 1-in 2-out split, not leftover of nm2oricyccz z-probe cyclic, not
leftover of nm2oricycx lex-largest, not leftover of lex-one axis-order,
not leftover-empty fail, and not exist-opposite.

Reverse oriented frame at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at `A`. Split reverse fails because split fails at
`A`. Cover and split do not score handedness: at the two split HOLD sites
`B` and `C`, Orient is `+1` then `−1`. Lex-one reverse fails because
lex-one at `A` fails and lex-one at `B` is `+1`, the same sign as this
letter at `B` but still reverse fail from `A`. Lex-largest cyclic at `B`
is `−1`, not this `+1`. Unique signed reverse fails because both unique
signed signs fail. Z-probe cyclic reverse HOLDs because both of those
signs are `+1`. Leftover-empty reverse fails because leftover of
the union is `{e_2}` at `A` and empty at `B`. Leftover of `M` reverse
fails because leftover of `M` at `A` is `{e_1, e_2}` and at `B` is
`{e_2, e_3}`: nonempty and unequal. Leftover of `O` reverse fails because
leftover of `O` at `A` is `{e_2, e_3}` and at `B` is `{e_1}`.
Exist-opposite reverse of signed `M` fails. Exist-opposite reverse of
signed `O` fails. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=−1` and `Orient(D)=fail`. Face fails.

Face oriented frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Cyclic lex-smallest oriented face fails because `D` is
fail, not `±1`. Lex-one face fails from the same split fail at `D`, and
lex-one at `C` is `−1`, the same sign as this Orient at `C`. Unique signed
face fails because neither unique signed sign is `±1`. Unsigned cyclic
at `C` is `+1` while this Orient at `C` is `−1`. Z-probe cyclic face HOLDs
because both of those signs are `−1`. Cover and split do not score
handedness. On the 1-axis opposite two-site seed, cover reverse HOLDs
while Orient at `A` is fail from 2-in 1-out. This two-axis member is not
leftover of that 1-axis split face fail. The four y-probes of this same
seed give cyclic lex-smallest Orient `+1` at `A` and `+1` at `B` and
Orient fail at `D` from split fail, so oriented y-face fails while
y-reverse HOLDs. The four z-probes give oriented reverse hold and
oriented face hold. Those probe-direction readouts are not this x-probe
display. Leftover-empty face fails because leftover of the union is empty
at `C` and `{e_2}` at `D`. Leftover of `M` at `C` is `{e_2, e_3}` and
leftover of `M` at `D` is `{e_1, e_2}`: nonempty and unequal. Leftover of
`O` at `C` is `{e_1}` and leftover of `O` at `D` is `{e_2, e_3}`.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed
`O` fails. Cyclic lex-smallest oriented face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Split fails at `A` and Orient at `A` is fail, not
`UNDEFINED`. At `B`, mixed `O ∩ {±e_3}` has size 2 and lex-smallest still
picks `+e_3`.

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
- It does not replace Orient by lexicographic unsigned `o1,o2` orientation.
- It does not replace Orient by unique signed `|O_i|=1` letters.
- It does not replace Orient by lex-one axis-order `e1<e2<e3`.
- It does not replace Orient by nm2oricycx lex-largest cyclic next/prev.
- It does not replace Orient by unsigned cyclic `+e_next,+e_prev`.
- It does not replace Orient by unsigned axis units of `Axis(O)`.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
- It does not treat empty `O_next` or `O_prev` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace Orient by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nm2axx axis-cover reverse fail face fail as this
  oriented display.
- It does not reprint nm2ax12x 1-in 2-out split reverse fail face fail as
  this oriented display.
- It does not reprint nm2oricyccz z-probe cyclic reverse hold face hold as
  this oriented display.
- It does not reprint nm2oricycx lex-largest reverse fail face fail as
  this oriented display.
- It does not reprint y-probe cyclic reverse hold from `+1,+1` as this
  letter.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the z-probes as this letter.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite seed process, cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1`, and
the reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual |
| split at `τ` | Theorem 1; fail at `A,D`, hold at `B,C` |
| axis index `i` and cyclic `(o_next,o_prev)` | Theorem 1; fail at `A,D`; `i=1` at `B,C` |
| integer `det(m,o_next,o_prev)` | Theorem 1; fail, `1`, `-1`, fail |
| Orient at `τ` | Theorem 1; `fail`, `+1`, `−1`, `fail` |
| reverse from oriented frame at `τ` | Theorem 2; `fail` |
| face from oriented frame at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this oriented display |
| leftover of exist-opposite HOLD | not this oriented display |
| leftover of nm2axx axis-cover FAIL | not this oriented display |
| leftover of nm2ax12x 1-in 2-out split FAIL | not this oriented display |
| leftover of nm2oricyccz z-probe cyclic HOLD | not this oriented display |
| leftover of nm2oricycx lex-largest cyclic FAIL | not this oriented display |
| leftover of lex-one axis-order | not this oriented display |
| leftover of unique signed `|O_i|=1` | not this oriented display |
| leftover of y-probe cyclic | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the same-lock two-site seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| empty `O_next` or `O_prev` scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1` on the four x-probes of the two-axis opposite seed, and reverse/face from that sign. |
| V2 | Current main has no landed cyclic-next-prev-lex-smallest-outgoing-determinant reverse/face of timed `M` and `O` on these four x-probes of the two-axis opposite seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic next/prev lex-smallest signed outgoing letters from `Axis(M)` at the same `t+1` cut, reverse fails, face fails, Orient at `B` is `+1` while nm2oricycx lex-largest at `B` is `−1`, unsigned cyclic at `C` is `+1` while this Orient at `C` is `−1`, and z-probe cyclic reverse HOLDs. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by lex-one axis-order, does not replace Orient by
nm2oricycx lex-largest cyclic, does not replace Orient by unique signed
`|O_i|=1`, does not replace Orient by nm2axx axis-cover, does not replace
Orient by nm2ax12x 1-in 2-out split, does not replace Orient by
nm2oricyccz z-probe cyclic, does not identify this display with the 1-axis
opposite two-site seed, and does not identify it with nmunopp union. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2axx axis-cover | reuse cover reverse fail and cover face fail | cover is unsigned occupation; Orient at `B` is `+1` and at `C` is `−1` | ATTEMPTED |
| nm2ax12x 1-in 2-out split | reuse split reverse fail and split face fail | split HOLDs at `B` and at `C` while Orient there is `+1` then `−1`; Cover and split do not score handedness | ATTEMPTED |
| nm2oricyccz z-probe cyclic | reuse z-probe reverse hold and face hold | z-probe Orient is `+1,+1,−1,−1` so reverse HOLDs and face HOLDs; x-probe reverse fails and face fails | ATTEMPTED |
| nm2oricycx lex-largest | pick `−e` when both signs occupy a cyclic axis | lex-largest at `B` is `−1` and at `C` is `+1`; this letter at `B` is `+1` and at `C` is `−1` | ATTEMPTED |
| lex-one axis-order | pick lex-smallest per `Axis(O)` in `e1<e2<e3` | lex-one at `B` is `+1` and at `C` is `−1`, the same signs as this letter, from axis-order of `Axis(O)` not cyclic slots of `Axis(M)` | ATTEMPTED |
| lexicographic unsigned `o1,o2` | reuse unsigned units of `Axis(O)` | unsigned at `B` and at `C` are both `+1`; this Orient is `+1` then `−1` | ATTEMPTED |
| unique signed `|O_i|=1` | require a singleton on each outgoing axis | unique signed fails at `B` and at `C` from mixed `±e_3`; this Orient is a sign | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover `{e_2}` at `A` and empty at `B`; leftover reverse fail does not report `Orient(B)=+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` fails and of signed `O` fails; those bits are not cyclic columns | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `+1` | ATTEMPTED |
| unsigned cyclic units | replace signed `o_next,o_prev` by `+e_next,+e_prev` | unsigned cyclic at `C` is `+1` while this Orient at `C` is `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `A` and `D` fail from leftover `{e_2}` with `|Axis(M)|=1` | ATTEMPTED |
| empty `O_next` as `UNDEFINED` | treat empty cyclic outgoing as unformed | empty `O_next` or `O_prev` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=3`, mixed `M(A)`, cover hold | different seed; here four tick-0 sites, `t(A)=2`, `M(A)={−e_3}` | ATTEMPTED |
| y-probe cyclic | score the four y-probes on this seed | y-probe Orient `+1,+1` so y-reverse HOLDs while this x-reverse fails; this letter is the four x-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-smallest determinant orientation at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail on the two-axis opposite x-probes | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; `O(D,τ)` is `{+e_1, −e_1}` here and `{+e_1}` on same-lock | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(D)` sums to `0` while `Axis(O)(D)` is `{e_1}` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with lex-one axis-order, missing identification of
Orient with nm2oricycx lex-largest cyclic, missing identification of Orient
with unique signed `|O_i|=1`, missing identification of Orient with nm2axx
axis-cover, missing identification of Orient with nm2ax12x 1-in 2-out
split, missing identification of Orient with nm2oricyccz z-probe cyclic,
missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
`e_next,e_prev` from the axis index of `m`, lex-smallest signed outgoing
letter on each cyclic axis under `+e < −e`, integer determinant sign, empty
`O_next` or `O_prev` as Orient fail not `UNDEFINED`, split fail as Orient
fail not `UNDEFINED`, four x-probes with `A` not a seed, second pair as a
new seed not a formed child, and mixed remains a set are declared. No
uniqueness of outgoing locks, no six-neighbor lock union as the scored
object, no lock-count clock, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | unique signed incoming letter and cyclic next/prev lex-smallest outgoing letters | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse fail and face fail are only leftover of
nm2ax12x split reverse fail; lex-one already answers mixed `O`; cover
reverse already answers the three-axis occupation; leftover of `M` alone
already answers reverse; leftover of `O` alone already answers reverse;
exist-opposite of signed `O` already answers reverse; z-probe cyclic
already answers handedness; mixed #7188 already reported fail/fail; the
second pair is only the formed child `(0,0,1)` of the 1-axis seed; unique
outgoing letters should be required; and nm2oricycx lex-largest cyclic
already gives the same reverse bit because reverse fails either way.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that leftover as reverse fail from
empty leftover at `B`. Orient reverse fails because `Orient(A)=fail` and
`Orient(B)=+1`. Orient face fails because `Orient(D)=fail`. Cover and
split fail reverse and face on this member and do not score that signed
pair: split HOLDs at `B` and at `C` while Orient is `+1` then `−1`.
Lex-one axis-order at `B` is `+1` from lex-smallest `(+e_2,+e_3)`, the
same sign as this letter at `B`; the construction is axis-order of
`Axis(O)`, not cyclic from `Axis(M)`. nm2oricycx lex-largest cyclic at
`B` is `−1` and at `C` is `+1`, the opposite pair of signs. Unique signed
`|O_i|=1` fails at `B` and at `C` from mixed `±e_3`; this Orient is a
sign. Unsigned cyclic at `C` is `+1` while this Orient at `C` is `−1`.
Z-probe cyclic reverse HOLDs and z-probe cyclic face HOLDs; this x-probe
reverse fails and this x-probe face fails. Y-probe cyclic reverse HOLDs
from `+1,+1` while this x-reverse fails. Unique outgoing letters would
assign `UNDEFINED` at mixed `O(B)`; this Orient is `+1`, not
`UNDEFINED`. Mixed #7188 is a different z-symmetric process with mixed
`M`. The second pair is a new seed, not a formed child: `(0,0,1)` is
recorded at tick 0 with lock `+e_2`. Reverse oriented frame is HOLD iff
equal `±1` signs at `A` and at `B`, not leftover of nm2ax12x split and not
leftover of nm2oricycx lex-largest.

### N8 — cross-cycle echo

nm2axx cover on these four x-probes fails reverse and fails face. nm2ax12x
1-in 2-out split on the same seed fails reverse and fails face, with split
HOLD at `B` and at `C`. Lex-one axis-order on these x-probes would report
Orient fail at `A`, `+1` at `B`, `−1` at `C`, and fail at `D`, the same
signs as this letter. nm2oricycx lex-largest reports `fail,−1,+1,fail`.
Unique signed outgoing letters fail at mixed `O`. The four y-probes of
this same seed report cyclic lex-smallest Orient `+1` at `A` and `+1` at
`B`, so y-reverse HOLDs. The four z-probes report cyclic lex-smallest
Orient `+1,+1,−1,−1`, reverse hold, and face hold. Leftover axis reports
leftover `{e_2}` at `A` and empty leftover at `B`. This note is not those
displays: it reports cyclic next/prev lex-smallest outgoing determinant
orientation of the 1-in 2-out frame of `M` and `O` at `τ=t+1` on the
two-axis opposite x-probes, with `t(A)=2`, `t(B)=1`, `t(C)=3`, and
`t(D)=2`, `Orient(A)=fail`, `Orient(B)=+1`, `Orient(C)=−1`,
`Orient(D)=fail`, reverse fail, and face fail. Cover and split do not
score handedness.

**Gate disposition:** PASS for the cyclic-next-prev-lex-smallest-outgoing-determinant `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals lex-one axis-order,” “the
predicate equals nm2oricycx lex-largest cyclic,” “the predicate equals
unique signed HOLD,” “the predicate equals nm2axx axis-cover HOLD,” “the
predicate equals nm2ax12x 1-in 2-out split HOLD,” “the predicate equals
nm2oricyccz z-probe cyclic HOLD,” “the predicate equals the 1-axis opposite
two-site seed,” “the predicate equals nmunopp union,” “bits are Admissibility,”
“split fail is UNDEFINED,” “empty `O_next` is UNDEFINED,” “reverse
oriented frame holds,” or “face oriented frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the unique signed incoming letter, the
cyclic axis index, and the lex-smallest signed outgoing letters on
`e_next` and `e_prev`, reports the integer determinant and its sign, lists
new records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that Orient is
fail, `+1`, `−1`, fail from cyclic lex-smallest columns, that reverse fails
and face fails, that split fail is Orient fail not `UNDEFINED`, that empty
`O_next` or `O_prev` is Orient fail not `UNDEFINED`, that the 1-axis
opposite two-site seed is a different member, that leftover-empty fail is
a different predicate, that leftover of `M` alone and leftover of `O`
alone are different objects, that mixed sets remain sets, that
unique-letter Orient is `UNDEFINED` at mixed `O`, that lex-one at `B` is
`+1` matching this Orient at `B`, that nm2oricycx lex-largest at `B` is
`−1`, that unsigned cyclic at `C` is `+1` while this Orient at `C` is
`−1`, that unique signed fails at mixed `O`, that z-probe cyclic reverse
HOLDs while this reverse fails, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
that `A` is not a seed, that the y-probes and z-probes of this seed are not
this letter, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
