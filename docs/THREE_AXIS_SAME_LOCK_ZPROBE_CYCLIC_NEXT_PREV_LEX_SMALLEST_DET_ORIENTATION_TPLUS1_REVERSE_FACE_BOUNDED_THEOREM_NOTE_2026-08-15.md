---
claim_id: three_axis_same_lock_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic lex-smallest orientation of the 1-in 2-out frame at t+1 on the four z-probes of the three-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_same_lock_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Cyclic Next/Prev Lex-Smallest Outgoing Determinant Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four Z-Probes Of The Three-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-smallest outgoing determinant orientation of the
1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing dual
`O` at each probe's `τ=t+1`, and reverse/face from that sign, on the four
z-probes of the three-axis same-lock seed in `B_3(0)={n:n·n<=9}`. z-probes as
nm2axz. `M`, `O`, split as nm2ax12z. Orient as nm2oricyccz (lex-smallest
cyclic).
Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)`
is the set of earliest incoming nearest-neighbor steps at `q` using only
records with tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the
outgoing dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e`
is formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty
`O` is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required. When split HOLDs,
`m` is the unique vector in `M`. Let `i` in `{1,2,3}` be the axis index of
`m`. `e_next = e_{i+1}` with wrap `3+1→1`. `e_prev = e_{i-1}` with wrap
`1−1→3`. `O_next = O ∩ {±e_next}` and `O_prev = O ∩ {±e_prev}`. If either
is empty, Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next` is the
lex-smallest vector in `O_next` (hence `+e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. Reverse HOLDs if and only if `Orient(A)=Orient(B)` both
`±1`. Face HOLDs if and only if `Orient(C)=Orient(D)` both `±1`. Cover
and split do not score handedness. This is not leftover of nm2oricyccslz
cyclic next/prev lex-smallest on the two-axis same-lock seed. This is not
leftover of nm2oricycc3z cyclic next/prev lex-smallest on the three-axis
opposite seed. This is not leftover of nm2oricyccz cyclic next/prev
lex-smallest on the two-axis opposite seed. This is not leftover of
nm2oricyclslz lex-largest cyclic next/prev on the two-axis same-lock seed.
This is not leftover of nm2oricyclz cyclic next/prev on the opposite seed.
This is not leftover of nm2orionez lex-one signed outgoing orientation on
this same-lock seed. This is not leftover of nm2slz axis-cover. This is not
leftover of nm2chiralz lexicographic unsigned `o1,o2` orientation. This is
not leftover of nm2oridetz unique signed outgoing letters. This is not
leftover of nm2orichz leftover-axis. This is not leftover of nm2orichz
opposite-pair leftover-axis orientation. This is not leftover of nm2axz
axis-cover. This is not leftover of nm2ax12z 1-in 2-out
split. This is not leftover of leftover-of-`M` alone. This is not leftover
of leftover-of-`O` alone. This is not leftover-empty fail of leftover axis.
This is not leftover of nmunopp union. This is not leftover of nmt2opp `M`
frozen at `t`. This is not leftover of nmot2opp two-tick composition. This
is not leftover of nmoutopp untimed eventual-`O`. This is not leftover of
mixed #7188 fail/fail. This is not leftover of the 1-axis same-lock two-site
seed. This is not leftover of the two-axis same-lock seed. Neither pair is
opposite. The second pair is a new seed, not a formed child. The third pair
is a new seed, not a formed child. Uniqueness is not required. Mixed remains
a set. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_same_lock_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_same_lock_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev lex-smallest
oriented frame is the integer sign of `det(m,o_next,o_prev)` with unique
signed incoming letter `m` and the lex-smallest signed outgoing letter on the
two axes cyclic from `Axis(M)` under `+e < −e`. Reverse and face are scored
on equal `±1` signs at the paired probes. Named signs `{+,−}` of locks are
a coarser readout and are not used as the object. A singleton unique
outgoing lock letter is a different readout and is not used as the object.
Unsigned axis units of `Axis(O)` are a different readout and are not used.
Lex-largest cyclic next/prev is a different readout and is not used.
Lex-smallest signed letters in axis order `e1<e2<e3` are a different readout
and are not used. Unique signed letters requiring `|O_i|=1` are a different
readout and are not used. Opposite-pair leftover-axis orientation is a
different readout and is not used. Existential opposite of signed locks is a
different readout and is not used. Axis-cover without the frame sign is a
different readout and is not used. 1-in 2-out split without the frame sign is
a different readout and is not used. Leftover-empty fail of unsigned leftover
axis sets is a different readout and is not used. A `Z^3` sum of those
locks is a different readout and is not used. A six-neighbor star is not the
letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four z-probes of the three-axis same-lock seed, Orient fail at A from split fail, Orient +1,−1,−1 at B,C,D, reverse fail and face hold; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_same_lock_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face
target_blocker_text: "display cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame reverse/face on the four z-probes of the three-axis same-lock seed, not lex-largest cyclic, not unique |O_i|=1, not unsigned axis units, not leftover axis, not cover, not split, not lex-one"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to lex-largest cyclic next/prev, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to lex-one signed axis order, do not reduce to opposite-pair leftover-axis, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, do not identify with nm2oricyccz opposite-seed reverse hold, do not identify with nm2oricyccslz two-axis same-lock unique signed fail at B, do not identify with nm2oricycc3z three-axis opposite reverse hold, do not identify with nm2oricyclslz lex-largest reverse fail, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four z-probes of the three-axis same-lock seed and reverse/face from that sign; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose cyclic
next/prev lex-smallest outgoing determinant orientation of `M` and `O` is
scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second same-lock pair. `C` of the
x-probes is the third-pair seed `(2,0,0)`. z-probes as nm2axz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. `(0,0,1)` locks `+e_2` and
`(0,1,1)` locks `+e_2`. `(2,0,0)` locks `+e_3` and `(2,1,0)` locks
`+e_3`. The second pair is a new seed, not a formed child of the first
pair. The third pair is a new seed, not a formed child: on the two-axis
same-lock seed those sites form at tick 3 locking `+e_1`. Neither pair is
opposite. This seed is not the 1-axis same-lock two-site seed
`{0,(0,1,0)}` with `+e_1/+e_1` alone. This seed is not the two-axis
same-lock seed of nm2oricyccslz. This seed is not the three-axis opposite
seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3`. This seed is not the
two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`. This seed is not the
perp two-site seed `+e_1/+e_2`. This seed is not the x-axis same-lock seed
`{0,(1,0,0)}` with `+e_2/+e_2`. This seed is not the z-symmetric three-site
seed `{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site
seed that also records `(0,-1,0)` at tick 0.

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
e_next = e_{i+1} with 3+1 → 1.
e_prev = e_{i-1} with 1−1 → 3.
O_next = O ∩ {±e_next}, O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is the lex-smallest vector in O_next
(hence +e if both signs). o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The outgoing pair is signed and cyclic from `Axis(M)`, not from axis-order
`e1<e2<e3`. Mixed opposite signs on one cyclic axis make `|O_next|=2` or
`|O_prev|=2`; lex-smallest still picks `+e`, so Orient is defined when split
HOLDs. Unique outgoing letters of the whole set `O` are not required: mixed
`O` remains a set, and unique-letter readout of mixed `O` is `UNDEFINED`
while this Orient is a sign. Empty cyclic side is Orient fail, not
`UNDEFINED`. A vanishing determinant is fail. Sign of a nonzero integer
determinant is `+1` or `−1`. Split HOLD required: 2-in 1-out is Orient
fail, not UNDEFINED. If unique `m` exists, `i`, `o_next`, and `o_prev` may
still be reported when split fails; Orient is then fail, not those vectors.
Lex-largest on the same cyclic slots is a different readout and is not used.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse fails from overlapping `e_2` at
`A` and cover face HOLDs, while Orient at `C` and at `D` is `−1`. Identifying
split reverse with this reverse is refused: split reverse fails from
split fail at `A` and split face HOLDs, while the signed frame at `C`
and at `D` is `−1`. Identifying leftover-empty fail with this reverse is
refused: leftover-empty fail scores empty leftover as reverse fail and
face fail, while this face HOLDs; on unique signed `O={+e_1,+e_3}` leftover
is empty while Orient is `+1`. Identifying lexicographic unsigned `o1,o2`
with this reverse is refused: unsigned reverse fails and unsigned face
HOLDs with `+1,+1`, while this reverse fails and this face HOLDs with
`−1,−1`. Identifying lex-one signed axis-order letters with this reverse is
refused: lex-one reverse fails and lex-one face HOLDs with `−1,−1`, matching
these bits on this member, but on unique signed `O={+e_1,+e_3}` with
`m=+e_2` lex-one is `(+e_1,+e_3)` with Orient `−1` while cyclic is
`(+e_3,+e_1)` with Orient `+1`. Identifying unique signed `|O_i|=1` with this
reverse is refused: unique signed reverse fails because unique signed at
`A` fails, while unique signed at `B` and at `D` HOLD from the third pair;
unique signed face fails because unique signed at `C` fails. Identifying
opposite-pair leftover-axis orientation with this reverse is refused:
leftover-axis reverse fails and leftover-axis at `D` fails, while this
Orient at `D` is `−1` and this face HOLDs. Identifying nm2oricyccslz
two-axis same-lock lex-smallest with this reverse is refused: that member
has `O(B)={+e_2,+e_3,−e_3}` and unique signed fail at `B` and at `D`;
this unique signed HOLDs at `B` and at `D`. Identifying nm2oricycc3z
three-axis opposite lex-smallest with this reverse is refused: that member
has split HOLD at `A`, `Orient(A)=+1`, and reverse HOLD; here split fails
at `A` and reverse fails. Identifying nm2oricyclslz lex-largest cyclic on
the two-axis same-lock seed with this reverse is refused: lex-largest
there has `Orient(B)=−1` from mixed `±e_3`. Identifying nm2oricyccz
opposite-seed Orient reverse hold and face hold with this reverse is
refused: nm2oricyccz has split HOLD at `A` and `Orient(A)=+1` equal to
`Orient(B)=+1`; here split fails at `A` and `Orient(A)` is fail.
Identifying nm2oricyclz opposite-seed lex-largest reverse hold with this
reverse is refused: nm2oricyclz has `Orient(A)=−1` with split HOLD.
Identifying nm2slz axis-cover with this reverse is refused: cover does not
report the signed determinant. Identifying a named sign of those locks
with reverse or face is refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, `i`, cyclic pair, and Orient at `τ=t+1`

On this process the four z-probes form. Compare to leftover axis: that
leftover reports empty leftover at each probe and leftover reverse fail
and leftover face fail. Compare to nm2slz axis-cover: cover fails at `A`
from overlapping `e_2` and HOLDs at `B`, `C`, and `D`, so cover reverse
fails and cover face HOLDs. Compare to nm2oricyccz cyclic next/prev
lex-smallest on the two-axis opposite seed: that member has split HOLD at
`A`, `O(A,τ)={+e_1, −e_1, +e_3}` missing the partner letter,
`Orient(A)=+1`, reverse HOLDs from equal `+1` signs, and face HOLDs.
Compare to nm2oricyccslz lex-smallest cyclic on the two-axis same-lock
seed: reverse fails and face HOLDs with the same signs `fail,+1,−1,−1`,
but two-axis `O(B)` has `−e_3` and unique signed fails at `B` and at `D`.
Compare to nm2oricycc3z lex-smallest cyclic on the three-axis opposite
seed: reverse HOLDs and face HOLDs with `+1,+1,−1,−1` and split HOLD at
`A`. Compare to nm2oricyclslz lex-largest cyclic on the two-axis
same-lock seed: reverse fails and face HOLDs with signs `fail,−1,+1,+1`.
Compare to nm2oricyclz cyclic next/prev lex-largest on the opposite seed:
reverse HOLDs from equal `−1` signs. Compare to nm2orionez lex-one on this
same-lock member: reverse fails and face HOLDs with signs `fail,+1,−1,−1`.
Compare to nm2axz cover and nm2ax12z split on the opposite seed: both HOLD
reverse and face there. Compare to nm2chiralz lexicographic unsigned
`o1,o2` orientation on this same-lock member: reverse fails and face HOLDs
with unsigned signs `fail,+1,+1,+1`. Compare to nm2oridetz unique signed
outgoing letters: unique signed fails at `A` and at `C` and HOLDs at `B`
and at `D`. Compare to nm2orichz opposite-pair leftover-axis orientation:
reverse fails and leftover-axis at `D` fails. This display reads the
cyclic next/prev lex-smallest outgoing determinant of those same timed
sets:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=1
M(A, τ) = {+e_2}
M(B, τ) = {+e_1}
M(C, τ) = {+e_3}
M(D, τ) = {+e_1}
O(A, τ) = {+e_1, −e_1, +e_2, +e_3}
O(B, τ) = {+e_2, +e_3}
O(C, τ) = {+e_1, −e_1, −e_2}
O(D, τ) = {−e_2, +e_3}
split(A) = fail
split(B) = hold
split(C) = hold
split(D) = hold
m(A) = +e_2
i(A) = 2
o_next(A) = +e_3
o_prev(A) = +e_1
det(A) = fail
Orient(A) = fail
m(B) = +e_1
i(B) = 1
o_next(B) = +e_2
o_prev(B) = +e_3
det(B) = 1
Orient(B) = +1
m(C) = +e_3
i(C) = 3
o_next(C) = +e_1
o_prev(C) = −e_2
det(C) = -1
Orient(C) = −1
m(D) = +e_1
i(D) = 1
o_next(D) = −e_2
o_prev(D) = +e_3
det(D) = -1
Orient(D) = −1
```

`A` is a seed at tick 0 with seed letter `+e_2`. The partner of that pair,
`(0,1,1)`, is also a seed at tick 0 with seed letter `+e_2`. Mixed remains
a set: `O(A,τ)` has four outgoing steps. Unique outgoing letters would
assign `UNDEFINED` at mixed `O`. Unique signed `|O_i|=1` fails at `A` and
at `C` because `O(A)` has both `±e_1` and `O(C)` has both `±e_1`. At `B`
and at `D` unique signed HOLDs because the third pair forms `(1,1,0)` and
`(1,0,0)` at tick 1 locking `−e_1`, so those sites are not outgoing of
`B` and of `D` at `τ=t+1`. On the two-axis same-lock seed, `O(B)` also has
`−e_3` and unique signed fails at `B` and at `D`. At `A`, unique `m` still
gives `i=2`, `o_next=+e_3`, and `o_prev=+e_1`, but split fails from
overlapping `e_2` in `Axis(O)`, so Orient fails, not `UNDEFINED`. Split
HOLD is required. `M` is a singleton at each probe, so the unique signed
`m` exists. Cover and split fail at `A` from overlapping `e_2` and HOLD at
`B`, `C`, and `D`; they do not score that cyclic Orient at `C` and at `D`
is `−1`. Unsigned axis-order 2-plane at `C` is `(e_1,e_2)` and
lexicographic Orient at `C` is `+1`, while cyclic Orient at `C` is `−1`.
Unsigned Orient at `B` is `+1` and cyclic Orient at `B` is `+1`; unsigned
face HOLDs with `+1,+1` while this face HOLDs with `−1,−1`. Lex-one signed
axis-order pair at `B` is `(+e_2,+e_3)` with Orient `+1`, matching cyclic
`(o_next,o_prev)` at `B` on this member; on unique signed `O={+e_1,+e_3}`
with `m=+e_2` lex-one is `(+e_1,+e_3)` with Orient `−1` while cyclic is
`(+e_3,+e_1)` with Orient `+1`. Lex-largest cyclic pair at `B` is
`(+e_2,+e_3)` with Orient `+1`, agreeing with lex-smallest because `O(B)`
has no mixed slot; lex-largest at `C` picks `o_next=−e_1` from mixed
`±e_1` and reports Orient `+1`, while this Orient at `C` is `−1`. Opposite-pair leftover-axis at `B` and at `D`
fails because those `O` have no opposite pair, while this Orient is `+1`
at `B` and `−1` at `D`. The same-lock partner letter `+e_2` is already in
`O(A)` at formation tick `t` itself: `O(A,t)={+e_2}`. O is not M.

On the 1-axis same-lock two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and `C` is 2-in 1-out, so split fails at `C` and
Orient at `C` is fail, not UNDEFINED. That is leftover of the first pair.
Here both `(0,0,1)` and `(0,1,1)` are seeds of a second same-lock pair on a
second axis, and `(2,0,0)` and `(2,1,0)` are seeds of a third same-lock
pair on a third axis. On the y-probes of this same seed, split HOLDs at
`A` and cyclic Orient at that y-probe is `−1`, lexicographic unsigned
`o1,o2` there is `+1`, and opposite-pair leftover-axis Orient there fails
from no opposite pair in `O`. Y-probe reverse fails (`−1,+1`) and y-face
HOLDs (`+1,+1`); this z-probe reverse fails and this z-face HOLDs with
`−1,−1`. Those y-probe signs are not these z-probe signs.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. The partner seed of
`A` is already recorded at tick 0, so it is not among those new records.
Sites `(1,1,0)` and `(1,0,0)` form at tick 1 from the third pair, so they
are not new 6-NN of `B` or of `D`:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2)
```

`M` is frozen from `t` to `t+1`. At `t`, `O(A)={+e_2}` and `O` is empty at
`B`, at `C`, and at `D`; split fails at each probe, and Orient is fail,
not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)` is fail and `Orient(B)=+1`. Reverse fails. This is HOLD
iff equal `±1` signs, not leftover of nm2oricyccz cyclic next/prev, not
leftover of nm2oricyclslz lex-largest, not leftover of nm2oricyclz cyclic
next/prev, not leftover of nm2orionez lex-one, not leftover of nm2slz
axis-cover, not leftover of nm2chiralz lexicographic unsigned `o1,o2`, not
leftover of nm2oridetz unique signed outgoing letters, not leftover of
nm2orichz opposite-pair leftover-axis, not leftover of nm2axz axis-cover,
not leftover of nm2ax12z 1-in 2-out split, not leftover-empty fail, and
not exist-opposite.

Reverse oriented frame at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at `A` from overlapping `e_2`. Split reverse fails
because split fails at `A`. Cover and split do not score handedness.
Lexicographic unsigned reverse fails because unsigned Orient at `A` is
fail and at `B` is `+1`. Lex-one signed reverse fails because lex-one
Orient at `A` is fail and at `B` is `+1`. Unique signed reverse fails
because unique signed at `A` fails, even though unique signed at `B` is
`+1`. Opposite-pair leftover-axis reverse fails because that Orient at
`A` is fail. Cyclic reverse fails because `Orient(A)` is fail, not a
`±1` sign. Leftover-empty reverse fails because leftover of the union is
empty at `A` and at `B`. Leftover of `M` reverse fails because leftover
of `M` at `A` is `{e_1, e_3}` and at `B` is `{e_2, e_3}`: nonempty and
unequal. Leftover of `O` reverse fails because leftover of `O` at `A` is
empty. Exist-opposite reverse of signed `M` fails. Exist-opposite reverse
of signed `O` fails. Presence of an opposite pair in `O` HOLDs at `A` and
fails at `B`. nm2oricyccz reverse HOLDs from equal `+1` signs with split
HOLD at `A`. nm2oricycc3z reverse HOLDs from equal `+1` signs with split
HOLD at `A` on the three-axis opposite seed. nm2oricyccslz reverse also
fails, and unique signed fails at that two-axis `B`. nm2oricyclslz reverse
fails from `Orient(B)=−1` on the two-axis same-lock seed, not from
`Orient(B)=+1`. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=−1` and `Orient(D)=−1`. Face HOLDs.

Face oriented frame at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. Cyclic signed oriented face HOLDs
because both signs are `−1`. Lexicographic unsigned face HOLDs because
both unsigned signs are `+1`; those signs are not these signs.
Lex-one signed face HOLDs because both lex-one signs are `−1`; those
columns are axis-order `(o_j,o_k)`, not cyclic `(o_next,o_prev)`. Unique
signed face fails because unique signed at `C` fails, even though unique
signed at `D` is `−1`. Opposite-pair leftover-axis face fails because
leftover-axis at `D` fails. Lex-largest cyclic face fails with `+1,−1`,
not these `−1,−1`. Cover and split do not score handedness. Presence of
an opposite pair in `O` HOLDs at `C` and fails at `D`, so pair-presence
face fails while this face HOLDs. On the 1-axis same-lock two-site seed,
cover face HOLDs while split face fails at `C` from 2-in 1-out, and Orient
at `C` is fail, not UNDEFINED. This three-axis member is not leftover of
that 1-axis split face fail. The four y-probes of this same seed give
cyclic Orient `−1` at `A` and `+1` at `B`, so oriented y-reverse fails,
and y-face HOLDs with `+1,+1` while this z-face HOLDs with `−1,−1`. The
four x-probes give oriented reverse fail and oriented face fail. Those
probe-direction readouts are not this z-probe display. Leftover-empty face
fails because leftover of the union is empty at `C` and at `D`. Leftover
of `M` at `C` is `{e_1, e_2}` and leftover of `M` at `D` is `{e_2, e_3}`:
nonempty and unequal. Leftover of `O` at `C` is `{e_3}` and leftover of
`O` at `D` is `{e_1}`: nonempty and unequal. Exist-opposite face of signed
`M` fails. Exist-opposite face of signed `O` fails. Cyclic signed oriented
face HOLDs. nm2oricyccz face also HOLDs with `−1,−1` on the opposite seed;
that is leftover of a different seed. nm2oricyccslz face HOLDs with
`−1,−1` on the two-axis same-lock seed, but unique signed fails at that
`D`. nm2oricyclslz face HOLDs with `+1,+1` on the two-axis same-lock seed;
those columns are lex-largest, not these columns.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover reverse fails from overlapping axes at `A`. Cover
HOLDs at `D` and split HOLDs at `D`. Orient at `D` is `−1` from cyclic
`(−e_2,+e_3)`. Orient at `A` is fail because split fails, not because `O`
is unformed.

Face HOLDs.

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
- It does not replace Orient by lex-one signed axis-order letters.
- It does not replace Orient by nm2oricyclslz lex-largest cyclic next/prev.
- It does not replace Orient by nm2oricyccslz two-axis same-lock lex-smallest.
- It does not replace Orient by nm2oricycc3z three-axis opposite lex-smallest.
- It does not replace Orient by unique signed `|O_i|=1` letters.
- It does not replace Orient by opposite-pair leftover-axis orientation.
- It does not replace Orient by unsigned axis units of `Axis(O)`.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
- It does not treat empty cyclic `O_next` or `O_prev` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace Orient by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmcover axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2oricyccz cyclic reverse hold face hold with
  `Orient(A)=+1` as this oriented display.
- It does not reprint nm2oricyclslz lex-largest reverse fail face hold with
  `Orient(B)=−1` as this oriented display.
- It does not reprint nm2oricyclz cyclic reverse hold face hold with
  `Orient(A)=−1` as this oriented display.
- It does not reprint nm2orionez lex-one reverse fail face hold with
  `Orient(A)` fail and `Orient(B)=+1` as this oriented display.
- It does not reprint nm2slz axis-cover reverse fail face hold as this
  oriented display.
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2ax12z 1-in 2-out split reverse hold face hold as
  this oriented display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2` reverse fail
  face hold with `+1,+1` as this oriented display.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichz opposite-pair leftover-axis reverse fail
  face fail as this oriented display.
- It does not reprint the 1-axis same-lock two-site seed as this member.
- It does not score the y-probes or the x-probes as this letter.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this oriented display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition.
- This is not the two-tick lock-count clock composition.
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

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
three-axis same-lock six-site process, cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1`, and
the reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three disjoint same-lock pairs `+e_1/+e_1`, `+e_2/+e_2`, and `+e_3/+e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual includes partner `+e_2` at `A` |
| split at `τ` | Theorem 1; fail at `A`; HOLD at `B`,`C`,`D` |
| unique signed `m`, index `i`, and cyclic `(o_next,o_prev)` | Theorem 1; singleton `M`; cyclic pair defined at each probe, Orient fail at `A` |
| integer `det(m,o_next,o_prev)` | Theorem 1; fail, `1`, `-1`, `-1` |
| Orient at `τ` | Theorem 1; fail, `+1`, `−1`, `−1` |
| reverse from oriented frame at `τ` | Theorem 2; `fail` |
| face from oriented frame at `τ` | Theorem 3; `hold` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this oriented display |
| leftover of exist-opposite HOLD | not this oriented display |
| leftover of nmcover axis-cover HOLD | not this oriented display |
| leftover of nm2axz axis-cover HOLD | not this oriented display |
| leftover of nm2ax12z 1-in 2-out split HOLD | not this oriented display |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2orionez lex-one signed axis order | not this oriented display |
| leftover of nm2oricyclslz lex-largest cyclic next/prev | not this oriented display |
| leftover of nm2oricyccslz two-axis same-lock lex-smallest | not this oriented display |
| leftover of nm2oricycc3z three-axis opposite lex-smallest | not this oriented display |
| leftover of nm2oricyccz lex-smallest opposite z | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz opposite-pair leftover-axis | not this oriented display |
| leftover of opposite-pair presence in `O` | not this oriented display |
| y-probe or x-probe Orient on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| leftover of nm2oricyclz cyclic opposite z | not this display |
| leftover of nm2oricyccz cyclic opposite z | not this display |
| leftover of nm2oricyclslz lex-largest same-lock z | not this display |
| leftover of nm2slz axis-cover | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis same-lock two-site seed | not this display |
| leftover of the two-axis same-lock seed | not this display |
| leftover of the two-axis opposite seed | not this display |
| leftover of the three-axis opposite seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| empty cyclic side scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1` on the four z-probes of the three-axis same-lock seed, and reverse/face from that sign. |
| V2 | Current main has no landed cyclic-next/prev-lex-smallest-outgoing-determinant reverse/face of timed `M` and `O` on these four z-probes of the three-axis same-lock seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at the same `t+1` cut, reverse fails from Orient fail at `A` while face HOLDs with `−1,−1`, cover reverse fails from overlapping `e_2`, unsigned face HOLDs with `+1,+1` while this face HOLDs with `−1,−1`, lex-largest cyclic face fails with `+1,−1`, unique signed HOLDs at `B` and at `D` while two-axis same-lock unique signed fails there, unique signed face fails, nm2oricyccslz unique signed fails at `B`, and nm2oricycc3z opposite-seed reverse HOLDs. |
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
nm2oricyclslz lex-largest cyclic next/prev, does not replace Orient by
nm2oricyccslz two-axis same-lock lex-smallest, does not replace Orient by
nm2oricycc3z three-axis opposite lex-smallest, does not replace Orient by
nm2oricyccz lex-smallest on opposite z, does not replace Orient by
nm2oridetz unique signed `|O_i|=1`, does not replace Orient by nm2orichz
opposite-pair leftover-axis, does not replace Orient by nmcover
axis-cover, does not replace Orient by nm2axz axis-cover, does not replace
Orient by nm2ax12z 1-in 2-out split, does not identify this display with
the 1-axis same-lock two-site seed, does not identify it with nm2oricyclz
cyclic next/prev on the opposite seed, does not identify it with nm2slz
axis-cover, and does not identify it with nmunopp union. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2oricyccz cyclic opposite z | reuse opposite-seed reverse hold and face hold | nm2oricyccz has split HOLD at `A` and `Orient(A)=+1` equal to `Orient(B)`; here split fails at `A` from overlapping `e_2` and `Orient(A)` is fail, so reverse fails | ATTEMPTED |
| nm2oricyccslz two-axis same-lock lex-smallest | reuse two-axis same-lock reverse fail and face hold | two-axis `O(B)` has `−e_3` and unique signed fails at `B` and at `D`; this unique signed HOLDs at `B` and at `D` | ATTEMPTED |
| nm2oricycc3z three-axis opposite lex-smallest | reuse three-axis opposite reverse hold and face hold | opposite has split HOLD at `A` and reverse HOLD with `+1,+1`; here split fails at `A` and reverse fails | ATTEMPTED |
| nm2oricyclslz lex-largest two-axis same-lock z | reuse lex-largest reverse fail and face hold | two-axis lex-largest signs are `fail,−1,+1,+1`; this lex-smallest is `fail,+1,−1,−1`; this lex-largest face fails with `+1,−1` | ATTEMPTED |
| nm2oricyclz cyclic opposite z | reuse opposite-seed lex-largest reverse hold and face hold | nm2oricyclz has split HOLD at `A` and `Orient(A)=−1` equal to `Orient(B)`; here split fails at `A` from overlapping `e_2` and `Orient(A)` is fail, so reverse fails | ATTEMPTED |
| nm2orionez lex-one same-lock z | reuse lex-one reverse fail and face hold | lex-one signs match `fail,+1,−1,−1` on this member; on unique signed `O={+e_1,+e_3}` with `m=+e_2` lex-one is `(+e_1,+e_3)` with Orient `−1` while cyclic is `(+e_3,+e_1)` with Orient `+1` | ATTEMPTED |
| nm2slz axis-cover | reuse cover reverse fail and cover face hold | cover does not report signed det; cover HOLDs at `C` and at `D` while Orient is `−1` | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned face HOLDs with `+1,+1` while this face HOLDs with `−1,−1` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed fails at `A` and at `C` and HOLDs at `B` and at `D`; unique signed face fails while this face HOLDs | ATTEMPTED |
| nm2orichz opposite-pair leftover-axis | reuse leftover-axis reverse and face | leftover-axis reverse fails and leftover-axis at `D` fails; this Orient at `D` is `−1` and this face HOLDs | ATTEMPTED |
| nm2axz axis-cover | reuse opposite-seed cover reverse hold and cover face hold | nm2axz HOLDs at `A`; here cover fails at `A` because `O(A)` includes partner `+e_2` | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse opposite-seed split reverse hold and split face hold | opposite split HOLDs at `A`; here split fails at `A`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with these bits, leftover face fails while this face HOLDs; unique signed `O={+e_1,+e_3}` has empty leftover and Orient `+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal; leftover of `M` face fails while this face HOLDs | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is empty, leftover reverse fails for a one-sided empty leftover, not Orient fail from split fail | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` fails and exist-opposite face of signed `O` fails; exist-opposite does not read cyclic columns | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at `A` and at `C` and fails at `B` and at `D` without cyclic columns | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is fail, not `UNDEFINED` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both fail at `A` and agree at `B,C,D`; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `A` fails from overlapping cover, not from 2-in 1-out | ATTEMPTED |
| empty cyclic side as `UNDEFINED` | treat empty `O_next` or `O_prev` as unformed | empty cyclic side is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis same-lock two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and split HOLDs at `C` | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse fails (`−1,+1`) and y-face HOLDs with `+1,+1` while this z-face HOLDs with `−1,−1`; this letter is the four z-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four z-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-smallest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face hold on the three-axis same-lock seed | ATTEMPTED |
| 1-axis same-lock two-site reuse | reuse `+e_1/+e_1` alone | different seed; this member is three disjoint same-lock pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_2+e_3` while Orient at `A` fails | ATTEMPTED |
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
missing identification of Orient with nm2orionez lex-one, missing identification of
Orient with nm2oricyclslz lex-largest cyclic next/prev, missing
identification of Orient with nm2oricyccz lex-smallest opposite z, missing
identification of Orient with nm2oridetz unique signed `|O_i|=1`, missing
identification of Orient with nm2orichz opposite-pair leftover-axis, missing
identification of Orient with nmcover axis-cover, missing identification of
Orient with nm2axz axis-cover, missing identification of Orient with
nm2ax12z 1-in 2-out split, missing identification of Orient with nm2oricyclz
cyclic next/prev, missing identification of Orient with nm2slz axis-cover,
missing identification of this seed with the 1-axis same-lock two-site seed,
and missing Record identification of Orient reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint same-lock seed pairs `+e_1/+e_1`,
`+e_2/+e_2`, and `+e_3/+e_3` at `(2,0,0)/(2,1,0)`, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis, cover as
complementary occupation of `{e_1,e_2,e_3}`, split as cover and
`|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic next/prev axes
of `Axis(M)`, lex-smallest signed outgoing letter per cyclic axis under
`+e < −e`, integer determinant sign, empty cyclic side as Orient fail not
`UNDEFINED`, split fail as Orient fail not `UNDEFINED`, four z-probes with
seed `A`, second pair as a new seed not a formed child, third pair as a
new seed not a formed child, and mixed remains a set are declared. No uniqueness of outgoing locks, no
six-neighbor lock union as the scored object, no lock-count clock, no global
later T, no formation attachment from already-recorded six-neighbor locks,
and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | unique signed incoming letter and cyclic next/prev lex-smallest outgoing letters of `Axis(M)` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse fail and face hold are only leftover of
nm2oricyccz cyclic next/prev on opposite z; they are only leftover of
nm2oricyccslz two-axis same-lock lex-smallest; they are only leftover of
nm2oricycc3z three-axis opposite lex-smallest; they are only leftover of
nm2oricyclslz lex-largest; they are only leftover of nm2orionez lex-one;
they are only leftover of nm2slz cover; unique signed `|O_i|=1` already
answers mixed `O`; cover reverse and split reverse already answer the
occupation; leftover of `M` alone already answers reverse; leftover of
`O` alone already answers reverse; exist-opposite of signed `O` already
answers reverse; opposite-pair leftover-axis already answers handedness;
mixed #7188 already reported fail/fail; the third pair is only a formed
child of the two-axis seed; unique outgoing letters should be required;
and unsigned incoming axis already gives the same signs because each `M`
letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Orient reverse fails because `Orient(A)` is fail and
`Orient(B)=+1`. Orient face HOLDs because both signs are `−1`. Cover and
split fail reverse and HOLD face on this member and do not score that
signed pair at `C` and at `D`. nm2oricyccz on the opposite seed has
`Orient(A)=+1` with split HOLD and reverse HOLDs; here `O(A)` includes
partner `+e_2`, split fails, `Orient(A)` is fail, and reverse fails.
nm2oricycc3z on the three-axis opposite seed has reverse HOLD with
`+1,+1`. nm2oricyccslz on the two-axis same-lock seed has the same reverse
fail and face hold signs, but two-axis `O(B)` has `−e_3` and unique signed
fails at `B` and at `D`; this unique signed HOLDs at `B` and at `D`.
nm2oricyclslz lex-largest on the two-axis same-lock seed has Orient
`fail,−1,+1,+1`; this display has `fail,+1,−1,−1`. nm2orionez lex-one on
this same-lock seed has the same signs `fail,+1,−1,−1` as this display on
these four z-probes; those columns are axis-order, not cyclic next/prev,
and on unique signed `O={+e_1,+e_3}` with `m=+e_2` lex-one is `−1` while
cyclic is `+1`. nm2slz cover reverse fails from overlapping `e_2` but does
not report `−1` at `C` and at `D`. Lexicographic unsigned `o1,o2` reverse
fails with `fail,+1` and face HOLDs with `+1,+1`; unsigned Orient at `C`
is `+1` while cyclic Orient at `C` is `−1`. Unique signed `|O_i|=1`
fails at `A` and at `C` and HOLDs at `B` and at `D`; unique signed face
fails while this face HOLDs. Opposite-pair leftover-axis reverse fails
and leftover-axis at `D` fails; this Orient at `D` is `−1`. Presence of
an opposite pair in `O` HOLDs at `A` and at `C` and fails at `B` and at
`D`. Leftover of `M` alone at `A` is `{e_1,e_3}` and at `B` is
`{e_2,e_3}`: nonempty unequal. Leftover of `O` alone at `A` is empty.
Exist-opposite reverse of signed `O` fails. Unique outgoing letters would
assign `UNDEFINED` at mixed `O(A)`; this Orient is fail, not `UNDEFINED`.
On unique signed `O={+e_1,+e_3}` leftover is empty while Orient is `+1`,
so leftover-empty fail is not this predicate. Mixed #7188 is a different
z-symmetric process with mixed `M`. The second pair is a new seed, not a
formed child: `(0,0,1)` is recorded at tick 0 with lock `+e_2`, whereas
the 1-axis child forms at tick 1 with lock `+e_3`. The third pair is a new
seed, not a formed child: `(2,0,0)` is recorded at tick 0 with lock
`+e_3`, whereas the two-axis same-lock child forms at tick 3 with lock
`+e_1`. Reverse oriented frame is HOLD iff equal `±1` signs at `A` and at
`B`, not leftover of nm2oricyccslz unique signed fail at `B` and not
leftover of nm2oricycc3z reverse hold.

### N8 — cross-cycle echo

nm2slz axis-cover on this three-axis same-lock seed reported cover fail at
`A` from overlapping `e_2`, cover HOLD at `B`,`C`,`D`, reverse fail, and
face hold. nm2oricyccz cyclic next/prev lex-smallest on the two-axis
opposite seed reported `Orient(A)=+1` with split HOLD, reverse hold, and
face hold. nm2oricyccslz cyclic next/prev lex-smallest on the two-axis
same-lock seed reported Orient `fail,+1,−1,−1`, reverse fail, and face
hold, with unique signed fail at `B` and at `D`. nm2oricycc3z cyclic
next/prev lex-smallest on the three-axis opposite seed reported Orient
`+1,+1,−1,−1`, reverse hold, and face hold. nm2oricyclslz lex-largest
cyclic on the two-axis same-lock seed reported Orient `fail,−1,+1,+1`,
reverse fail, and face hold.
nm2oricyclz cyclic next/prev on the two-axis opposite seed reported
`Orient(A)=−1` with split HOLD, reverse hold, and face hold. nm2orionez
lex-one on this same-lock seed reported Orient `fail,+1,−1,−1`, reverse
fail, and face hold. nm2axz cover on the opposite seed reported cover HOLD
at each of the four z-probes, reverse hold, and face hold. nm2ax12z 1-in
2-out split on the opposite seed reported split HOLD at each of the four
z-probes, reverse hold, and face hold. Leftover axis reported empty
leftover at each of four z-probes, leftover reverse fail, and leftover
face fail. The four y-probes of this same seed reported cyclic Orient `−1`
at `A` and Orient `+1` at `B`, so y-reverse fails and y-face HOLDs with
`+1,+1`. This note is not those displays: it
reports cyclic next/prev lex-smallest outgoing determinant orientation of
the 1-in 2-out frame of `M` and `O` at `τ=t+1` on the three-axis same-lock
seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=1`, `Orient(A)` fail,
`Orient(B)=+1`, `Orient(C)=−1`, `Orient(D)=−1`, reverse fail, and face
hold. Cover and split do not score handedness.

**Gate disposition:** PASS for the cyclic-next/prev-lex-smallest-outgoing-determinant `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals nm2oricyccz cyclic HOLD,” “the predicate
equals nm2oricyccslz two-axis same-lock unique signed fail,” “the
predicate equals nm2oricycc3z three-axis opposite HOLD,” “the predicate
equals nm2oricyclslz lex-largest HOLD,” “the predicate equals nm2oricyclz
cyclic HOLD,” “the predicate equals nm2orionez lex-one HOLD,” “the
predicate equals nm2slz axis-cover HOLD,” “the predicate equals
nm2chiralz lexicographic unsigned `o1,o2` HOLD,” “the predicate equals
nm2oridetz unique signed HOLD,” “the predicate equals nm2orichz
opposite-pair leftover-axis HOLD,” “the predicate equals nmcover
axis-cover HOLD,” “the predicate equals nm2axz axis-cover HOLD,” “the
predicate equals nm2ax12z 1-in 2-out split HOLD,” “the predicate equals
the 1-axis same-lock two-site seed,” “the predicate equals nmunopp union,”
“bits are Admissibility,” “split fail is UNDEFINED,” “empty cyclic side is
UNDEFINED,” or “reverse oriented frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the unique signed incoming letter, the
axis index `i`, and the cyclic next/prev lex-smallest outgoing letters,
reports the integer determinant and its sign, lists new records in
`B_3(0)` between `t` and `t+1` that meet a probe's six-neighbors, and
checks Theorems 1--3. It also checks that Orient is fail,`+1`,`−1`,`−1`
from cyclic lex-smallest columns, that reverse fails and face HOLDs while
cover reverse and split reverse fail, that split fail is Orient fail not
`UNDEFINED`, that empty cyclic side is Orient fail not `UNDEFINED`, that
nm2oricyccz opposite-seed Orient at `A` is `+1` while this Orient at `A`
is fail and that opposite reverse HOLDs while this reverse fails, that
nm2oricyclslz lex-largest Orient at `B` is `−1` while this Orient at `B`
is `+1`, that the 1-axis same-lock two-site seed is a different member
with Orient fail at `C`, that leftover-empty fail is a different
predicate, that leftover of `M` alone and leftover of `O` alone are
different objects, that mixed sets remain sets, that unique-letter Orient
is `UNDEFINED` at mixed `O`, that lexicographic unsigned Orient at `C` is
`+1` while this Orient at `C` is `−1`, that lex-one face HOLDs with
`−1,−1` matching this face from axis-order columns, that unique signed
face fails while this face HOLDs, that opposite-pair leftover-axis reverse
fails while this reverse also fails from a different object, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that the second pair is a new seed
not a formed child, that the third pair is a new seed not a formed child,
that neither pair is opposite, that unique signed HOLDs at `B` and at `D`
while two-axis same-lock unique signed fails there, that three-axis
opposite reverse HOLDs while this reverse fails, that the y-probes and
x-probes of this seed are not this letter, and that the display is not
the two-tick lock-count clock composition. No runner cache is written.
