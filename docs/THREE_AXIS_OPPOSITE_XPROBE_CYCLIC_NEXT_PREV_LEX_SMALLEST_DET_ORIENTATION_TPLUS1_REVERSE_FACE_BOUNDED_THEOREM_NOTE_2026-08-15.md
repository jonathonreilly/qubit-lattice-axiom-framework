---
claim_id: three_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic lex-smallest orientation of the 1-in 2-out frame at t+1 on the four x-probes of the three-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Cyclic Lex-Smallest Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four X-Probes Of The Three-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-smallest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that sign, on the
four x-probes of the three-axis opposite seed in `B_3(0)={n:n·n<=9}`.
x-probes as nm2axx. Orient as nm2oricyccz. Let `t(q)` be the formation
tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick `<= τ`.
Seeds are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`:
the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is
in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required. When split
HOLDs, `m` is the unique vector in `M`. Let `i` in `{1,2,3}` be the axis
index of `m`. `e_next = e_{i+1}` with `3+1→1`. `e_prev = e_{i-1}` with
`1−1→3`. `O_next = O ∩ {±e_next}`. `O_prev = O ∩ {±e_prev}`. If either
empty, Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next` is the
lex-smallest vector in `O_next` (hence `+e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. Reverse HOLDs if and only if `Orient(A)=Orient(B)` both
`±1`. Face HOLDs if and only if `Orient(C)=Orient(D)` both `±1`. Cover and
split do not score handedness. This is not leftover of nm2axx axis-cover.
This is not leftover of nm2ax12x 1-in 2-out split. This is not leftover of
nm2oricyccz z-probe cyclic. This is not leftover of nm2oricyccx two-axis x.
This is not leftover of nm2oricycl3x lex-largest. This is not leftover of
nm2oricycl3y y-probe cyclic. This is not leftover of nm2oricycl3z z-probe
cyclic. This is not leftover of nm2orionez lex-one. This is not leftover of
nm2chiralz lexicographic unsigned `o1,o2`. This is not leftover of
nm2oridetz unique signed outgoing letters. This is not leftover of
nm2orichz leftover-axis. This is not leftover of leftover-of-`M` alone.
This is not leftover of leftover-of-`O` alone. This is not leftover-empty
fail. This is not leftover of nmunopp union. This is not leftover of
nmt2opp `M` frozen at `t`. This is not leftover of nmot2opp two-tick
composition. This is not leftover of nmoutopp untimed eventual-`O`. This
is not leftover of mixed #7188 fail/fail. This is not leftover of the
1-axis opposite two-site seed. This is not leftover of the same-lock
two-site seed. This is not leftover of the two-axis opposite seed. The
second pair is a new seed, not a formed child. The third pair is a new
seed, not a formed child. `C=(2,0,0)` is a third-pair seed. `A` is a
formed child of that third pair. Uniqueness is not required. Mixed remains
a set. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py)

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
signed incoming letter `m` of axis index `i`, cyclic axes of `Axis(M)`, and
the lex-smallest signed outgoing letter on each of those cyclic slots under
`+e < −e`. Reverse and face are scored on equal `±1` signs at the paired
probes. Named signs `{+,−}` of locks are a coarser readout and are not used
as the object. A singleton unique outgoing lock letter is a different
readout and is not used as the object. Unsigned axis units of `Axis(O)` are
a different readout and are not used. Lex-one signed letters in axis order
`e1<e2<e3` are a different readout and are not used. Lex-largest cyclic
next/prev is a different readout and is not used. Unique signed letters
requiring `|O_i|=1` are a different readout and are not used. Opposite-pair
leftover-axis orientation is a different readout and is not used.
Existential opposite of signed locks is a different readout and is not
used. Axis-cover without the frame sign is a different readout and is not
used. 1-in 2-out split without the frame sign is a different readout and
is not used. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic lex-smallest orientation of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the three-axis opposite seed, Orient -1,+1,-1,fail, reverse fail and face fail; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_opposite_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face
target_blocker_text: "display cyclic lex-smallest orientation reverse/face on the four x-probes of the three-axis opposite seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to nm2oricycl3x lex-largest, do not reduce to two-axis x, do not reduce to y-probe or z-probe cyclic, do not reduce to lex-one, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic lex-smallest orientation of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the three-axis opposite seed and reverse/face from that sign; displayed, not adopted"
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
`C=(0,0,2)`, `D=(1,0,1)`. x-probes as nm2axx. `C` is a third-pair seed.
`A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(2,0,0)` locks `+e_3`. Site `(2,1,0)`
locks `−e_3`. The second pair is a new seed, not a formed child. The third
pair is a new seed, not a formed child. This seed is not the 1-axis
opposite two-site seed `{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is
not the two-axis opposite seed of nm2axx. This seed is not the perp
two-site seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`.

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

Oriented frame at the same cut, as nm2oricyccz:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1→1.
e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}.
O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e.
o_next is the lex-smallest vector in O_next (hence +e if both signs).
o_prev is the lex-smallest vector in O_prev.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The outgoing pair is signed. Mixed opposite signs on a cyclic slot make
`|O_next|=2` or `|O_prev|=2`; lex-smallest still picks `+e`, so Orient is
defined when split HOLDs. Unique outgoing letters of the whole set `O`
are not required: mixed `O` remains a set, and unique-letter readout of
mixed `O` is `UNDEFINED` while this Orient is a sign. Empty `O_next` or
empty `O_prev` is Orient fail, not `UNDEFINED`. A vanishing determinant
is fail. Sign of a nonzero integer determinant is `+1` or `−1`. Split
HOLD required: axis-overlap cover fail is Orient fail, not UNDEFINED.
Lex-largest on the same cyclic slots is a different readout and is not
used. Axis-order lex-one `(o_j,o_k)` is a different readout and is not
used.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse HOLDs without reporting
`Orient(A)=−1` versus `Orient(B)=+1`. Identifying split reverse with this
reverse is refused: split reverse HOLDs without cyclic next/prev columns.
Identifying leftover-empty fail with this reverse is refused:
leftover-empty fail scores empty leftover as reverse fail and face fail
without those signs. Identifying leftover of `M` alone with this reverse
is refused: leftover of `M` reverse HOLDs because leftover of `M` at `A`
and at `B` is `{e_2,e_3}`, while this reverse fails. Identifying leftover
of `O` alone with this reverse is refused: leftover of `O` reverse HOLDs
because leftover of `O` at `A` and at `B` is `{e_1}`. Identifying
lexicographic unsigned `o1,o2` with this reverse is refused: unsigned
Orient at `C` is `+1` while cyclic Orient at `C` is `−1`. Identifying
nm2oricycl3x lex-largest with this reverse is refused: lex-largest Orient
at `C` is `+1` while this Orient at `C` is `−1`. Identifying unique signed
`|O_i|=1` with this reverse is refused: unique signed fails at `C` while
this Orient at `C` is `−1`. Identifying opposite-pair leftover-axis with
this reverse is refused: leftover-axis at `C` is `+1` while this Orient at
`C` is `−1`. Identifying unsigned incoming axis with this reverse is
refused: unsigned incoming reverse HOLDs with `+1,+1` while this reverse
fails with `−1,+1`. Identifying a named sign of those locks with reverse
or face is refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, `i`, `o_next`, `o_prev`, and Orient at `τ=t+1`

On this process the four x-probes form. Compare to leftover axis: leftover
of the union is empty at `A`, `B`, `C`, and `D`, leftover reverse fail and
leftover face fail. Compare to nm2axx axis-cover and nm2ax12x 1-in 2-out
split: both HOLD reverse and fail face on this member, matching the reverse
and face bits but not the signs. Compare to nm2oricycl3x lex-largest on
these same x-probes: that readout scores Orient `−1,+1,+1`, fail, reverse
fail, and face fail, with Orient at `C` equal to `+1`. Compare to
lexicographic unsigned `o1,o2`: that readout scores Orient `−1,+1,+1`, fail.
Compare to leftover of `M` alone: leftover of `M` reverse HOLDs. Compare to
the two-axis opposite x-probes of nm2oricyccx: that member scores `t(A)=2`,
`t(C)=3`, `M(A)={−e_3}`, Orient fail, `+1`, `−1`, fail. Compare to the four
y-probes of this same seed: cyclic lex-smallest reverse HOLDs and face
fails. Compare to the four z-probes of this same seed: cyclic lex-smallest
reverse HOLDs and face HOLDs. This display reads cyclic next/prev of
`Axis(M)` with lex-smallest signed `O` on each slot:

```text
t(A)=1
t(B)=1
t(C)=0
t(D)=1
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_3}
M(D, τ) = {−e_1}
O(A, τ) = {−e_2, −e_3}
O(B, τ) = {+e_2, +e_3}
O(C, τ) = {+e_1, −e_1, −e_2}
O(D, τ) = {−e_1, +e_2, −e_3}
split(A) = hold
split(B) = hold
split(C) = hold
split(D) = fail
m(A) = −e_1
i(A) = 1
o_next(A) = −e_2
o_prev(A) = −e_3
det(A) = -1
Orient(A) = −1
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
m(D) = −e_1
i(D) = 1
o_next(D) = +e_2
o_prev(D) = −e_3
det(D) = 1
Orient(D) = fail
```

`C` is a seed at tick 0 with seed letter `+e_3`. `A` is a formed child of
that third pair: `A` forms at tick 1 from `(2,0,0)` locking incoming
`−e_1`. Mixed remains a set: `O(C,τ)` has three outgoing steps. Unique
outgoing letters would assign `UNDEFINED` at mixed `O(C)`. Unique signed
`|O_i|=1` fails at `C` because `O(C)` has both `±e_1`. Cyclic lex-smallest
picks `+e_1` on that mixed cyclic slot, so `(o_next,o_prev)=(+e_1,−e_2)`
and `det(+e_3,+e_1,−e_2)=-1`. Lex-largest on the same slot picks `−e_1`
and scores Orient `+1` at `C`. At `A`, split HOLDs, `i=1`, cyclic slots
are `e_2` and `e_3`, each occupied by one sign, and
`det(−e_1,−e_2,−e_3)=-1`. Unsigned incoming axis at `A` replaces `m` by
`+e_1` and scores `+1`, so unsigned incoming reverse HOLDs while this
reverse fails. At `B`, split HOLDs and `det(+e_1,+e_2,+e_3)=1`. At `D`,
`m` is singleton `{−e_1}` so `i=1`, `o_next=+e_2`, `o_prev=−e_3`, and
`det(−e_1,+e_2,−e_3)=1`, but split fails from cover fail: `Axis(M)`
intersect `Axis(O)` is `{e_1}` because `−e_1` occupies both `M` and `O`.
Leftover of the union at `D` is empty. Split HOLD is required, so Orient at
`D` is fail, not `UNDEFINED`. Cover and split HOLD reverse on this member
and do not score that Orient at `A` is `−1` and Orient at `B` is `+1`. O
is not M.

On the 1-axis opposite two-site seed, `t(A)=3`, `t(C)=4`, mixed `M(A)`,
cover HOLDs at `A` while split fails at `A`, and Orient at `A` is fail,
not UNDEFINED. On the two-axis opposite seed, `t(A)=2`, `t(C)=3`,
`M(A)={−e_3}`, and `C` is a formed child locking `+e_1`, not a seed. Here
`(2,0,0)` and `(2,1,0)` are seeds of a third opposite pair on a third
axis, `t(C)=0`, and `t(A)=1`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(2,0,0)` is a
seed, so it is not a new 6-NN of `A`. Site `(2,1,0)` is a seed, so it is
not a new 6-NN of `D`:

```text
new 6-NN of A at t(A)+1: (1, -1, 0), (1, 0, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (3, 0, 0), (1, 0, 0), (2, -1, 0)
new 6-NN of D at t(D)+1: (1, 2, 0), (1, 1, -1)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `B`, and
`C`. At `D`, `O` at `t` is `{−e_1}` because the first-pair seed `(0,1,0)`
is already recorded, and `O` grows to `{−e_1, +e_2, −e_3}` at `t+1`.
Orient at `t` is fail, not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)=−1` and `Orient(B)=+1`. Reverse fails. This is HOLD iff
equal `±1` signs, not leftover of nm2oricycl3x lex-largest, not leftover
of nm2oricyccx two-axis x, not leftover of nm2chiralz lexicographic
unsigned `o1,o2`, not leftover of nm2oridetz unique signed outgoing
letters, not leftover of nm2orichz leftover-axis, not leftover of
nm2orionez lex-one, not leftover of nm2axx axis-cover, not leftover of
nm2ax12x 1-in 2-out split, not leftover-empty fail, and not exist-opposite.

Reverse oriented frame at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Lexicographic unsigned reverse fails because unsigned `Orient(A)=−1` and
`Orient(B)=+1`. Unique signed reverse fails because unique signed signs
are `−1` and `+1`. Leftover-axis reverse fails because leftover-axis at
`A` is fail from no opposite pair in `O`. Cyclic lex-largest reverse
fails with the same reverse bit, but lex-largest Orient at `C` is `+1`
while this Orient at `C` is `−1`. Unsigned incoming reverse HOLDs because
both of those signs are `+1`. Leftover-empty reverse fails because leftover
of the union is empty at `A` and at `B`. Leftover of `M` reverse HOLDs
because leftover of `M` at `A` and at `B` is `{e_2, e_3}`: nonempty and
equal. Leftover of `O` reverse HOLDs because leftover of `O` at `A` and at
`B` is `{e_1}`: nonempty and equal. Exist-opposite reverse of signed `M`
holds. Exist-opposite reverse of signed `O` holds. Presence of an opposite
pair in `O` fails at `A` and fails at `B`, so pair-presence reverse fails
without reporting the cyclic signs. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=−1` and `Orient(D)` is fail. Face fails.

Face oriented frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Cyclic lex-smallest oriented face fails because Orient
HOLDs at `C` from `det(+e_3,+e_1,−e_2)=-1` and fails at `D` from split
fail by axis overlap, even though `o_next` and `o_prev` are both occupied
and `det(−e_1,+e_2,−e_3)=1`. Cyclic lex-largest face also fails, with
Orient `+1` at `C`. Lexicographic unsigned face fails, with Orient `+1` at
`C`. Unique signed face fails because unique signed at `C` fails. Pair
face fails with this face: pair HOLDs at `C` and fails at `D`. Leftover-axis
face fails with leftover-axis `+1` at `C`. On the 1-axis opposite two-site
seed, cover face HOLDs while split face fails, and Orient at `A` is fail,
not UNDEFINED. This three-axis member is not leftover of that 1-axis split
face fail: here `t(C)=0` and `C` is a third-pair seed. On the two-axis
opposite x-probes, reverse fails and face fails with `t(C)=3`. The four
y-probes of this same seed give cyclic lex-smallest reverse HOLD and face
fail. The four z-probes give cyclic lex-smallest reverse HOLD and face
HOLD. Those probe-direction readouts are not this x-probe display.
Leftover-empty face fails because leftover of the union is empty at `C`
and at `D`. Leftover of `M` at `C` is `{e_1, e_2}` and leftover of `M` at
`D` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` at `C` is
`{e_3}` and leftover of `O` at `D` is empty. Exist-opposite face of signed
`M` fails. Exist-opposite face of signed `O` holds. Cyclic lex-smallest
oriented face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `D` and split fails at `D`. Pair fails at
`D`. Orient at `D` is fail. Cyclic slots at `D` are occupied; Orient fails
from split fail, not from an empty cyclic slot.

Face fails.

## What this note does not claim

- It does not select a unique outgoing lock.
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
- It does not replace Orient by nm2orionez lex-one axis-order letters.
- It does not replace Orient by nm2oricycl3x lex-largest cyclic next/prev.
- It does not replace Orient by opposite-pair leftover-axis orientation.
- It does not replace Orient by unsigned axis units of `Axis(O)`.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
- It does not treat empty `O_i` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace Orient by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmcover axis-cover reverse hold face fail as this
  oriented display.
- It does not reprint nm2axx axis-cover reverse hold face fail as this
  oriented display.
- It does not reprint nm2ax12x 1-in 2-out split reverse hold face fail as
  this oriented display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2` reverse fail
  face fail as this oriented display.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichz leftover-axis reverse fail face fail as
  this oriented display.
- It does not reprint nm2orionez lex-one reverse fail face fail as this
  oriented display.
- It does not reprint nm2oricycl3x lex-largest reverse fail face fail with
  Orient `+1` at `C` as this oriented display.
- It does not reprint nm2oricyccx two-axis x reverse fail face fail as this
  member.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the z-probes as this letter.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
three-axis opposite seed process, cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1`,
and the reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `1`, `1`, `0`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at `A,B,C`, fail at `D` |
| unique signed `m`, cyclic index `i`, lex-smallest `o_next`, `o_prev` | Theorem 1; singleton `M`; `i=1,1,3,1`; slots occupied at `D` |
| integer `det(m,o_next,o_prev)` | Theorem 1; `-1`, `1`, `-1`, `1` |
| Orient at `τ` | Theorem 1; `−1`, `+1`, `−1`, fail |
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
| leftover of nmcover axis-cover HOLD | not this oriented display |
| leftover of nm2axx axis-cover HOLD | not this oriented display |
| leftover of nm2ax12x 1-in 2-out split HOLD | not this oriented display |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of nm2oricycl3x lex-largest | not this oriented display |
| leftover of nm2oricyccx two-axis x | not this oriented display |
| leftover of opposite-pair presence in `O` | not this oriented display |
| y-probe or z-probe Orient on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the two-axis opposite seed | not this display |
| leftover of the same-lock two-site seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| empty `O_i` scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: cyclic lex-smallest orientation of the 1-in 2-out frame of `M` and `O` at `t+1` on the four x-probes of the three-axis opposite seed, and reverse/face from that sign. |
| V2 | Current main has no landed cyclic-lex-smallest reverse/face of timed `M` and `O` on these four x-probes of the three-axis opposite seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at the same `t+1` cut, reverse fails from `−1` versus `+1` while leftover of `M` reverse HOLDs and unsigned incoming reverse HOLDs, Orient at `C` is `−1` while lex-largest at `C` is `+1` and while lexicographic at `C` is `+1`, and y-probe reverse HOLDs while this reverse fails. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by nm2chiralz lexicographic unsigned `o1,o2`, does not replace
Orient by nm2oridetz unique signed `|O_i|=1`, does not replace Orient by
nm2orionez lex-one, does not replace Orient by nm2oricycl3x lex-largest,
does not replace Orient by nm2orichz leftover-axis, does not replace
Orient by nmcover axis-cover, does not replace Orient by nm2axx
axis-cover, does not replace Orient by nm2ax12x 1-in 2-out split, does
not identify this display with the 1-axis opposite two-site seed, does
not identify it with the two-axis opposite seed of nm2oricyccx, and does
not identify it with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2oricycl3x lex-largest | reuse lex-largest reverse fail and face fail | lex-largest Orient at `C` is `+1` from `o_next=−e_1`; this Orient at `C` is `−1` from `o_next=+e_1` | ATTEMPTED |
| nm2oricyccx two-axis x | reuse two-axis x reverse fail and face fail | two-axis has `t(A)=2`, `t(C)=3`, `M(A)={−e_3}`, and `C` is a formed child; here `t(A)=1`, `t(C)=0`, and `C` is a third-pair seed | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face fail | unsigned Orient at `C` is `+1` from `(e_1,e_2)`; this Orient at `C` is `−1` from `(+e_1,−e_2)` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed fails at `C` from mixed `±e_1`; this Orient at `C` is `−1` | ATTEMPTED |
| nm2orionez lex-one axis-order | reuse axis-order lex-one columns | on this member lex-one agrees at `A,B,C,D`; on unique signed `O={+e_1,+e_3}` with `m=+e_2` lex-one is `−1` while cyclic lex-smallest is `+1` | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse fail and face fail | leftover-axis at `C` is `+1` from `det(+e_3,+e_1,+e_2)`; this Orient at `C` is `−1` | ATTEMPTED |
| nm2axx axis-cover | reuse cover reverse hold and cover face fail | cover reverse HOLDs without cyclic columns; Cover and split do not score handedness | ATTEMPTED |
| nm2ax12x 1-in 2-out split | reuse split reverse hold and split face fail | split reverse HOLDs without `o_next,o_prev`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with these bits without reporting `Orient(A)=−1`; leftover of the union is empty at each probe | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` reverse HOLDs from equal `{e_2,e_3}` while this reverse fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` reverse HOLDs from equal `{e_1}` while this reverse fails | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold of `M` and of `O` | exist-opposite reverse of signed `M` holds and exist-opposite reverse of signed `O` holds while this reverse fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence reverse fails without cyclic columns; pair HOLDs at `C` and fails at `A` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | unsigned incoming reverse HOLDs with `+1,+1`; this reverse fails with `−1,+1`; flipping `m` from `−e_1` to `+e_1` on `O={−e_2,−e_3}` flips Orient from `−1` to `+1` | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(C,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` fails from overlapping cover, not from 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED; this `D` fails from split fail with occupied cyclic slots | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=3`, `t(C)=4`, mixed `M(A)`, cover face HOLD | different seed; second pair is a new seed, not a formed child; here `t(A)=1` and `t(C)=0` | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse HOLDs (`+1,+1`) and y-face fails; this letter is the four x-probes | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe reverse HOLDs and z-face HOLDs; this letter is the four x-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic lex-smallest orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports Orient `−1`, `+1`, `−1`, fail on the three-axis opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(C)` sums to `−e_2` while cyclic lex-smallest is `(+e_1,−e_2)` | ATTEMPTED |
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
missing identification of Orient with nm2oridetz unique signed `|O_i|=1`,
missing identification of Orient with nm2orionez lex-one, missing
identification of Orient with nm2oricycl3x lex-largest cyclic next/prev,
missing identification of Orient with nm2orichz leftover-axis, missing
identification of Orient with nmcover axis-cover, missing identification of
Orient with nm2axx axis-cover, missing identification of Orient with
nm2ax12x 1-in 2-out split, missing identification of this seed with the
1-axis opposite two-site seed, missing identification of this seed with the
two-axis opposite seed, and missing Record identification of Orient reverse
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3`, perpendicular step rule, incoming-step lock,
own incoming set and own outgoing dual from records with tick `<= τ`,
per-probe `τ=t+1`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, unique signed `m` when
split HOLDs, cyclic `e_next` and `e_prev` of the axis of `m`, lex-smallest
signed outgoing letter on each cyclic slot under `+e < −e`, integer
determinant sign, empty `O_next` or empty `O_prev` as Orient fail not
`UNDEFINED`, split fail as Orient fail not `UNDEFINED`, four x-probes with
seed `C`, third pair as a new seed not a formed child, mixed remains a
set, and `A` as a formed child of the third pair are declared. No
uniqueness of outgoing locks, no six-neighbor lock union as the scored
object, no lock-count clock, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | unique signed incoming letter and cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at a probe's `t+1` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse fail and face fail are only leftover of cover
and of split; leftover-axis already answers handedness; lex-one already
answers mixed `O`; lex-largest cyclic already answers cyclic slots; unique
signed `|O_i|=1` already answers mixed `O`; leftover of `M` alone already
answers reverse; leftover of `O` alone already answers reverse;
exist-opposite of signed `O` already answers reverse; mixed #7188 already
reported fail/fail; the third pair is only the formed child `(2,0,0)` of
the two-axis seed; unique outgoing letters should be required; unsigned
incoming axis already gives the same reverse bit because reverse fails
either way; two-axis x already answered reverse-fail face-fail; and y-probe
or z-probe cyclic already answered this seed.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Orient reverse fails because `Orient(A)=−1` and
`Orient(B)=+1`. Orient face fails because Orient at `D` is fail. Cover and
split HOLD reverse and fail face on this member and do not score those
cyclic columns. Leftover of `M` reverse HOLDs from equal `{e_2,e_3}` while
this reverse fails. Leftover of `O` reverse HOLDs from equal `{e_1}` while
this reverse fails. Exist-opposite reverse of signed `M` holds and
exist-opposite reverse of signed `O` holds while this reverse fails.
Unsigned incoming reverse HOLDs with `+1,+1` while this reverse fails.
Lexicographic unsigned Orient at `C` is `+1` while this Orient at `C` is
`−1`. Unique signed fails at `C` while this Orient at `C` is `−1`.
Leftover-axis at `C` is `+1` while this Orient at `C` is `−1`. Lex-largest
cyclic Orient at `C` is `+1` while this Orient at `C` is `−1`. Unique
outgoing letters would assign `UNDEFINED` at mixed `O(C)`; this Orient is
`−1`, not `UNDEFINED`. On unique signed `O={+e_1,+e_3}` leftover is empty
while Orient is `+1`, so leftover-empty fail is not this predicate. Mixed
#7188 is a different z-symmetric process with mixed `M`. The third pair is
a new seed, not a formed child: `(2,0,0)` is recorded at tick 0 with lock
`+e_3`, whereas the two-axis child at that site forms at tick 3 with lock
`+e_1`. Two-axis x has `t(A)=2` and `M(A)={−e_3}`. Y-probe reverse HOLDs
and z-probe reverse HOLDs; this x-probe reverse fails. Reverse oriented
frame is HOLD iff equal `±1` signs at `A` and at `B`, not leftover of
nm2oricycl3x lex-largest and not leftover of leftover of `M` alone.

### N8 — cross-cycle echo

nm2axx cover on the two-axis seed reported cover fail at `A`, cover HOLD
at `B` and at `C`, cover fail at `D`, reverse fail, and face fail.
nm2oricyccx cyclic lex-smallest on that two-axis seed reported Orient
fail, `+1`, `−1`, fail, reverse fail, and face fail with `t(A)=2` and
`t(C)=3`. nm2oricycl3x lex-largest on this three-axis seed reports Orient
`−1,+1,+1`, fail, reverse fail, and face fail, with Orient at `C` equal to
`+1`. Leftover axis reports empty leftover at each of four x-probes,
leftover reverse fail, and leftover face fail. The four y-probes of this
same seed report cyclic lex-smallest reverse HOLD and face fail. The four
z-probes of this same seed report cyclic lex-smallest reverse HOLD and
face HOLD. This note is not those displays: it reports cyclic next/prev
lex-smallest outgoing determinant orientation of the 1-in 2-out frame of
`M` and `O` at `τ=t+1` on the three-axis opposite seed, with `t(A)=1`,
`t(B)=1`, `t(C)=0`, and `t(D)=1`, `Orient(A)=−1`, `Orient(B)=+1`,
`Orient(C)=−1`, `Orient(D)=fail`, reverse fail, and face fail. Cover and
split do not score handedness.

**Gate disposition:** PASS for the cyclic-lex-smallest `t+1` reverse/face
reports above. FAIL / DO NOT SHIP for “the predicate equals the named
sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals nm2chiralz lexicographic unsigned `o1,o2`
HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orionez lex-one HOLD,” “the predicate equals
nm2oricycl3x lex-largest HOLD,” “the predicate equals nm2orichz
leftover-axis HOLD,” “the predicate equals nmcover axis-cover HOLD,” “the
predicate equals nm2axx axis-cover HOLD,” “the predicate equals nm2ax12x
1-in 2-out split HOLD,” “the predicate equals nm2oricyccx two-axis x,”
“the predicate equals the 1-axis opposite two-site seed,” “the predicate
equals nmunopp union,” “bits are Admissibility,” “split fail is
UNDEFINED,” “empty `O_next` or empty `O_prev` is UNDEFINED,” “reverse
oriented frame holds,” or “face oriented frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the unique signed incoming letter, the
cyclic axis index, and the lex-smallest `o_next` and `o_prev`, reports the
integer determinant and its sign, lists new records in `B_3(0)` between `t`
and `t+1` that meet a probe's six-neighbors, and checks Theorems 1--3. It
also checks that Orient is `−1`,`+1`,`−1`,fail from cyclic lex-smallest
columns, that reverse fails and face fails while leftover of `M` reverse
HOLDs and unsigned incoming reverse HOLDs, that lex-largest Orient at `C`
is `+1` while this Orient at `C` is `−1`, that split fail is Orient fail
not `UNDEFINED`, that empty `O_next` or empty `O_prev` is Orient fail not
`UNDEFINED`, that the 1-axis opposite two-site seed is a different member
with `t(A)=3`, that the two-axis opposite seed is a different member with
`t(A)=2` and `M(A)={−e_3}`, that leftover-empty fail is a different
predicate, that leftover of `M` alone and leftover of `O` alone are
different objects, that mixed sets remain sets, that unique-letter Orient
is `UNDEFINED` at mixed `O`, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
that the third pair is a new seed not a formed child, that the y-probes
HOLD reverse and the z-probes HOLD reverse and HOLD face and are not this
letter, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
