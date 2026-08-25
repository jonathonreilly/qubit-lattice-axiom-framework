---
claim_id: three_axis_farface_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic lex-smallest orientation of the 1-in 2-out frame at t+1 on the four z-probes of the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Cyclic Next/Prev Lex-Smallest Outgoing Determinant Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four Z-Probes Of The Three-Axis Far-Face Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-smallest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that sign, on the
four z-probes of the three-axis far-face opposite seed in `B_3(0)={n:n·n<=9}`. Same
process and z-probes as nm2axz. `M` and `O` as nm2ax12z. Orient as
nm2oricyccz. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is
formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O`
is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required. When split
HOLDs, `m` is unique in `M`. Let `i` in `{1,2,3}` be the axis index of `m`.
`e_next = e_{i+1}` with `3+1→1`. `e_prev = e_{i-1}` with `1−1→3`.
`O_next = O ∩ {±e_next}`. `O_prev = O ∩ {±e_prev}`. If either empty,
Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next` is the
lex-smallest vector in `O_next` (hence `+e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. Reverse HOLDs if and only if `Orient(A)=Orient(B)` both
`±1`. Face HOLDs if and only if `Orient(C)=Orient(D)` both `±1`. Cover
and split do not score handedness. This is not leftover of nm2orichz
leftover-axis reverse HOLD whose face fails because C and D swap
`(m,pair)` columns. This is not leftover of nm2orionez lex-one reverse
fail whose face HOLDs from `e1<e2<e3` order independent of `m`. This is
not leftover of nm2chiralz lexicographic unsigned `o1,o2` orientation.
This is not leftover of nm2oridetz unique signed outgoing letters. This
is not leftover of nm2axz axis-cover. This is not leftover of nm2ax12z
1-in 2-out split. This is not leftover of nm2oricyclz two-axis HOLD. This
is not leftover of cyclic lex-largest on this same far-face seed. This is
not leftover of nm2oricyccz two-axis lex-smallest. This is not leftover of
nm2oricycc3z near-face lex-smallest. This is not leftover of leftover-of-`M` alone. This is
not leftover of leftover-of-`O` alone. This is not leftover-empty fail of
leftover axis. This is not leftover of nmunopp union. This is not leftover
of nmt2opp `M` frozen at `t`. This is not leftover of nmot2opp two-tick
composition. This is not leftover of nmoutopp untimed eventual-`O`. This
is not leftover of mixed #7188 fail/fail. This is not leftover of the
1-axis opposite two-site seed. This is not leftover of the same-lock
two-site seed. This is not leftover of the two-axis opposite seed of
nm2oricyclz. The second pair is a new seed, not a formed child. The
third pair is a new seed, not a formed child.
Uniqueness is not required. Mixed remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev
lex-smallest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-smallest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. Reverse and face are scored on equal `±1`
signs at the paired probes. Named signs `{+,−}` of locks are a coarser
readout and are not used as the object. A singleton unique outgoing lock
letter is a different readout and is not used as the object. Unsigned
axis units of `Axis(O)` are a different readout and are not used. Unique
signed letters requiring `|O_i|=1` are a different readout and are not
used. Opposite-pair leftover-axis orientation is a different readout and
is not used. Lex-one signed outgoing letters in axis order `e1<e2<e3`
independent of `m` are a different readout and are not used. Cyclic
lex-largest (`−e` if both signs) is a different readout and is not used.
nm2oricyccz two-axis lex-smallest is a different readout and is not used.
nm2oricycc3z near-face lex-smallest is a different readout and is not used.
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
claim_type_reason: "Exact report of cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four z-probes of the three-axis far-face opposite seed, Orient at A,B,C,D, reverse hold and face hold from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_reverse_face
target_blocker_text: "display cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame reverse/face on the four z-probes of the three-axis far-face opposite seed, not leftover-axis, not lex-one e1<e2<e3, not unique |O_i|=1, not unsigned axis units, not cover, not split, not two-axis HOLD"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-largest, do not reduce to nm2oricyccz, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four z-probes of the three-axis far-face opposite seed and reverse/face from that sign; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose
cyclic next/prev lex-smallest outgoing determinant orientation of `M` and
`O` is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second opposite pair. `C` of the
x-probes is `(2,0,0)`, not the far-face third-pair seed. Same process and
z-probes as nm2axz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(0,0,−1)` locks `+e_3`. Site `(0,1,−1)`
locks `−e_3`. The second pair is a new seed, not a formed child of the
first pair. The third pair is a new seed, not a formed child, and sits on
the `−z` face opposite the z-probes: on the two-axis opposite seed those
sites form at tick 1 locking `−e_3`. This seed is not the two-axis
opposite seed of nm2oricyclz. This seed is not
the 1-axis opposite two-site seed `{0,(0,1,0)}` with only `+e_1/−e_1`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
same-lock two-site seed `+e_1/+e_1`. This seed is not the z-symmetric
three-site seed `{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric
three-site seed that also records `(0,-1,0)` at tick 0.

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
e_next = e_{i+1} with 3+1→1. e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}. O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is lex-smallest in O_next (hence +e if both signs).
o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The outgoing pair is signed. Mixed opposite signs on one cyclic slot make
`|O_next|=2` or `|O_prev|=2`; lex-smallest still picks `+e`, so Orient is
defined when split HOLDs. Unique outgoing letters of the whole set `O` are
not required: mixed `O` remains a set, and unique-letter readout of mixed
`O` is `UNDEFINED` while this Orient is a sign. Empty `O_next` or empty
`O_prev` is Orient fail, not `UNDEFINED`. A vanishing determinant is fail.
Sign of a nonzero integer determinant is `+1` or `−1`. Split HOLD
required: 2-in 1-out is Orient fail, not UNDEFINED.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse and face without reading
cyclic signed columns. Identifying split reverse with this reverse is
refused: split HOLDs reverse and face without the cyclic order of
`Axis(M)`. Identifying leftover-empty fail with this reverse is refused:
leftover-empty fail scores empty leftover as reverse fail and face fail,
while this reverse HOLDs and this face HOLDs; leftover of the union is
empty while Orient is a sign (`+1,+1,−1,−1`); on unique signed
`O={+e_1,+e_3}` leftover is empty while Orient is `+1`. Identifying
lexicographic unsigned `o1,o2` with this reverse is refused: unsigned
reverse fails with `−1,+1` while this reverse HOLDs with `+1,+1`; unsigned
face HOLDs with `+1,+1` while this face HOLDs with `−1,−1`. Identifying
nm2orionez lex-one signed `e1<e2<e3` with this reverse is refused:
lex-one reverse fails from axis order independent of `m` while this
reverse HOLDs, and lex-one face HOLDs with `−1,−1` as this face HOLDs,
but those columns are axis-order, not cyclic `(o_next,o_prev)`.
Identifying unique signed `|O_i|=1` with this reverse is refused: unique
signed Orient fails at each of `A,B,C,D` from mixed opposite pairs, while
this Orient is `+1,+1,−1,−1`. Identifying leftover-axis orientation with
this reverse is refused: leftover-axis reverse HOLDs with `−1,−1` while
this reverse HOLDs with `+1,+1`, and leftover-axis face fails with
`+1,−1` while this face HOLDs with `−1,−1`. Identifying cyclic
lex-largest with this reverse is refused: lex-largest reverse HOLDs with
`−1,−1` and face HOLDs with `+1,+1`, while this Orient is `+1,+1,−1,−1`.
Identifying nm2oricyccz two-axis lex-smallest with this reverse is
refused: two-axis reverse HOLDs and face HOLDs with the same
`+1,+1,−1,−1` signs on these z-probes, but that seed has four tick-0
sites and forms `(0,0,−1)` at tick 1 locking `−e_3`, while this third
pair is a new seed at tick 0 locking `+e_3/−e_3`. Identifying
nm2oricycc3z near-face lex-smallest with this reverse is refused: that
near-face unique signed HOLDs at `B` and at `D` because those `O` lack
`−e_3`, while this far-face unique signed fails at each probe.
Identifying nm2oricyclz two-axis lex-largest HOLD with this reverse is
refused: two-axis lex-largest is `−1,−1,+1,+1`. Identifying a named sign
of those locks with reverse or face is refused: named-sign lettering lost
the axis.

## Theorem 1 — ticks, `M`, `O`, split, `i`, `o_next`, `o_prev`, and Orient at `τ=t+1`

On this process the four z-probes form. Compare to leftover axis: that
leftover reports empty leftover at each probe and leftover reverse fail
and leftover face fail, while this reverse HOLDs and this face HOLDs.
Compare to nm2axz cover and nm2ax12z split: both HOLD reverse and face on
this member without cyclic signed columns. Compare to nm2oricyccz on the
two-axis opposite seed: reverse HOLDs and face HOLDs with the same
`+1,+1,−1,−1` on these z-probes, from a four-site seed. Compare to
cyclic lex-largest on this same far-face seed: reverse HOLDs and face
HOLDs with opposite signs `−1,−1,+1,+1`. Compare to
nm2chiralz lexicographic unsigned `o1,o2` orientation: reverse fails and
face HOLDs on this member with signs `−1,+1,+1,+1`. Compare to nm2oridetz
unique signed outgoing letters: unique signed fails at each of `A,B,C,D`
because `|O_i|≠1` there. Compare to nm2orichz leftover-axis, which reverse
HOLDs and face fails. Compare to nm2orionez lex-one reverse fail whose
face HOLDs from `e1<e2<e3` order independent of `m`. Compare to
nm2oricycc3z near-face lex-smallest: unique signed HOLDs at `B` and at
`D`. This display reads
the cyclic next/prev lex-smallest outgoing determinant of those same timed
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
O(A, τ) = {+e_1, −e_1, +e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, −e_2}
O(D, τ) = {−e_2, +e_3, −e_3}
split(A) = hold
split(B) = hold
split(C) = hold
split(D) = hold
m(A) = +e_2
i(A) = 2
o_next(A) = +e_3
o_prev(A) = +e_1
det(A) = 1
Orient(A) = +1
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

`A` is a seed at tick 0 with seed letter `+e_2`. Mixed remains a set:
`O(A,τ)` has three outgoing steps. Unique outgoing letters of the whole
set `O` would assign `UNDEFINED` at `A`, at `B`, at `C`, and at `D`.
Unique signed `|O_i|=1` fails at each probe: `O(A)` and `O(C)` have both
`±e_1`, and `O(B)` and `O(D)` have both `±e_3`. Sites `(1,1,0)` and
`(1,0,0)` form at tick 2, so they are new 6-NN of `B` and of `D` at
`τ=t+1` and enter those mixed `O`. Lex-smallest picks `+e` on each mixed
cyclic slot, so `(o_next,o_prev)` is defined at each probe. `M` is a
singleton at each probe, so the unique signed `m` exists. At each probe
split HOLDs. Cover and split HOLD at each probe and do not score that
cyclic lex-smallest Orient is `+1,+1,−1,−1`. At `A`, `i=2` so `e_next=e_3`
and `e_prev=e_1`; mixed `O_prev={±e_1}` yields `o_prev=+e_1`. At `B`,
`i=1` so `e_next=e_2` and `e_prev=e_3`; mixed `O_prev={±e_3}` yields
`o_prev=+e_3`. On the two-axis opposite seed, `O(B)` also has `−e_3` and
cyclic lex-smallest Orient at `B` is `+1`; that seed is four tick-0 sites,
not this six-site far-face seed. Leftover-axis at `A` is pair `+e_1`
leftover `+e_3` and that Orient is `−1`; leftover-axis at `B` is pair
`+e_3` leftover `+e_2` and that Orient is `−1`; leftover-axis at `D` is
pair `+e_3` leftover `+e_2` and that Orient is `−1`, while cyclic at `D`
is `(−e_2,+e_3)` and reports `−1`. Lex-one at `D` uses axis order
`(−e_2,+e_3)` independent of cyclic next/prev and reports `−1`, while
unsigned `o1,o2` at `D` is `(e_2,e_3)` and reports `+1`. Cyclic
lex-largest at `A` picks `o_prev=−e_1` and reports `−1`. O is not M.

On the 1-axis opposite two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and `C` is 2-in 1-out, so split fails at `C` and
Orient at `C` is fail, not UNDEFINED. That is leftover of the first pair.
Here both `(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a
second axis, and `(0,0,−1)` and `(0,1,−1)` are seeds of a third opposite
pair on a third axis, on the `−z` face opposite the z-probes. On the
y-probes of this same seed, split HOLDs at `A` with `m=−e_1` so `i=1`,
`o_next=+e_2`, `o_prev=−e_3`, and cyclic Orient at that y-probe is `+1`.
Y-probe `B` is `+1`, so y-probe reverse HOLDs as this z-probe reverse
HOLDs. Y-probe `D` has split fail, so y-face fails while this z-face
HOLDs.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`. Sites `(1,1,0)` and `(1,0,0)` form
at tick 2, so they are new 6-NN of `B` and of `D`:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at each probe, split
fails, and Orient is fail, not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)=+1` and `Orient(B)=+1`. Reverse HOLDs. This is HOLD
iff equal `±1` signs, not leftover of nm2chiralz lexicographic unsigned
`o1,o2`, not leftover of nm2oridetz unique signed outgoing letters, not
leftover of nm2orichz leftover-axis, not leftover of nm2orionez lex-one,
not leftover of cyclic lex-largest, not leftover of nm2oricyccz two-axis
lex-smallest, not leftover of nm2axz axis-cover, not leftover of nm2ax12z
1-in 2-out split, not leftover of nm2oricyclz two-axis HOLD, not
leftover-empty fail, and not exist-opposite.

Reverse oriented frame at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Leftover-axis reverse HOLDs because leftover-axis at `A` and at `B` are
both `−1`, while this reverse HOLDs with `+1,+1`; leftover-axis face fails
while this face HOLDs.
Lexicographic unsigned reverse fails because unsigned `Orient(A)=−1` and
`Orient(B)=+1`. Unique signed reverse fails because unique signed at `A`
fails. Lex-one signed reverse fails because lex-one `Orient(A)=−1` and
`Orient(B)=+1` from `e1<e2<e3` order independent of `m`. Cyclic
lex-largest reverse HOLDs with opposite signs `−1,−1`. Two-axis
nm2oricyccz reverse HOLDs with `+1,+1` on these z-probes, from a
different four-site seed. Leftover-empty reverse fails because leftover
of the union is empty at `A` and at `B`. Leftover of `M` reverse fails
because leftover of `M` at `A` is `{e_1, e_3}` and at `B` is
`{e_2, e_3}`: nonempty and unequal. Leftover of `O` reverse fails because
leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`: nonempty and
unequal. Exist-opposite reverse of signed `M` fails. Exist-opposite
reverse of signed `O` HOLDs because `+e_3` in `O(A)` meets `−e_3` in
`O(B)`, but exist-opposite face of signed `O` fails. Presence of an
opposite pair in `O` HOLDs at `A` and at `B` without cyclic columns.
Those leftovers are not this display.

Reverse HOLDs.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=−1` and `Orient(D)=−1`. Face HOLDs.

Face oriented frame at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. Cyclic lex-smallest oriented face
HOLDs because the signs are `−1` and `−1`. Leftover-axis face fails
because leftover-axis at `C` is `+1` and leftover-axis at `D` is `−1`,
while this Orient at `D` is `−1`. Lex-one signed oriented face HOLDs
because both lex-one signs are `−1`; those columns are axis-order, not
cyclic `(o_next,o_prev)`. Lexicographic unsigned face HOLDs because both
unsigned signs are `+1`; those unsigned columns are not cyclic
`o_next,o_prev`. Unique signed face fails because unique signed at `C`
fails from mixed `±e_1`. Cover and split do not score handedness.
Presence of an opposite pair in `O` HOLDs at `C` and at `D` without
cyclic columns. On the 1-axis opposite two-site seed, cover face HOLDs
while split face fails at `C` from 2-in 1-out, and Orient at `C` is fail,
not UNDEFINED. This three-axis far-face member is not leftover of that
1-axis split face fail: here split HOLDs at `C` and Orient at `C` is
`−1`. The four y-probes of this same seed give cyclic Orient `+1` at `A`
and `+1` at `B`, so oriented y-reverse HOLDs as this z-reverse HOLDs;
y-face fails from split fail at y-probe `D` while this z-face HOLDs. The
four x-probes give oriented reverse fail and oriented face fail, and
x-probe `C` is `(2,0,0)`, not the far-face third-pair seed. Those
probe-direction readouts are not this z-probe display. Leftover-empty
face fails because leftover of the union is empty at `C` and at `D`.
Leftover of `M` at `C` is `{e_1, e_2}` and leftover of `M` at `D` is
`{e_2, e_3}`: nonempty and unequal. Leftover of `O` at `C` is `{e_3}` and
leftover of `O` at `D` is `{e_1}`: nonempty and unequal. Exist-opposite
face of signed `M` fails. Exist-opposite face of signed `O` fails.
Two-axis nm2oricyccz face HOLDs with `−1,−1` on these z-probes from a
four-site seed. Cyclic lex-largest oriented face HOLDs with `+1,+1`.
Cyclic lex-smallest oriented face HOLDs.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover HOLDs at `D` and split HOLDs at `D`. Orient at `D`
is `−1` from cyclic `(−e_2,+e_3)`.

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
- It does not replace Orient by unique signed `|O_i|=1` letters.
- It does not replace Orient by leftover-axis orientation.
- It does not replace Orient by nm2orionez lex-one signed `e1<e2<e3`.
- It does not replace Orient by cyclic lex-largest (`−e` if both signs).
- It does not replace Orient by nm2oricyccz two-axis lex-smallest.
- It does not replace Orient by nm2oricycc3z near-face lex-smallest.
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
- It does not reprint nmcover axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2ax12z 1-in 2-out split reverse hold face hold as
  this oriented display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2` reverse fail
  face hold with `+1,+1` as this oriented display.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichz leftover-axis reverse hold face fail as
  this oriented display.
- It does not reprint nm2orionez lex-one reverse fail face hold as this
  oriented display.
- It does not reprint nm2oricyclz two-axis reverse hold face hold as this
  oriented display.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the x-probes as this letter.
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

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
three-axis far-face opposite seed process, cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1`,
and the reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis far-face opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at each probe |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M`, lex-smallest pair defined |
| integer `det(m,o_next,o_prev)` | Theorem 1; `1`, `1`, `-1`, `-1` |
| Orient at `τ` | Theorem 1; `+1`, `+1`, `−1`, `−1` |
| reverse from oriented frame at `τ` | Theorem 2; `hold` |
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
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one signed `e1<e2<e3` | not this oriented display |
| leftover of cyclic lex-largest | not this oriented display |
| leftover of nm2oricyccz two-axis lex-smallest | not this oriented display |
| leftover of nm2oricycc3z near-face lex-smallest | not this oriented display |
| leftover of nm2oricyclz two-axis reverse hold face hold | not this oriented display |
| leftover of opposite-pair presence in `O` | not this oriented display |
| y-probe or x-probe Orient on this seed | not this letter |
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
| empty `O_i` scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1` on the four z-probes of the three-axis far-face opposite seed, and reverse/face from that sign. |
| V2 | Current main has no landed cyclic-next-prev-lex-smallest-outgoing-determinant reverse/face of timed `M` and `O` on these four z-probes of the three-axis far-face opposite seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at the same `t+1` cut, reverse HOLDs with `+1,+1` while leftover-empty reverse fails, face HOLDs with `−1,−1` while leftover-axis face fails with `+1,−1` and cyclic lex-largest face HOLDs with `+1,+1`, unique signed fails at each probe while this Orient is `+1,+1,−1,−1`, and the third pair is a far-face seed at tick 0, not the two-axis child at tick 1. |
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
nm2orichz leftover-axis, does not replace Orient by nm2orionez lex-one,
does not replace Orient by cyclic lex-largest, does not replace Orient by
nm2oricyccz two-axis lex-smallest, does not replace Orient by
nm2oricyclz two-axis HOLD, does not replace Orient by
nmcover axis-cover, does not replace Orient by nm2axz axis-cover, does not
replace Orient by nm2ax12z 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned reverse fails with `−1,+1` while this reverse HOLDs with `+1,+1`; unsigned face HOLDs with `+1,+1` while this face HOLDs with `−1,−1`; unsigned `o1,o2` at `B` is `(e_2,e_3)` while cyclic is `(+e_2,+e_3)` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed fails at each of `A,B,C,D` while this Orient is `+1,+1,−1,−1`; an opposite pair in each `O` makes `|O_i|≠1` but lex-smallest still picks `+e` | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse and face | leftover-axis reverse HOLDs with `−1,−1` while this reverse HOLDs with `+1,+1`, and leftover-axis face fails with `+1,−1` while this face HOLDs with `−1,−1` | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse fail and face hold | lex-one reverse fails from `e1<e2<e3` order independent of `m` while this reverse HOLDs, and lex-one face HOLDs with `−1,−1` as this face HOLDs, but those columns are axis-order | ATTEMPTED |
| cyclic lex-largest | reuse same cyclic axes with `−e` if both signs | lex-largest reverse HOLDs with `−1,−1` and face HOLDs with `+1,+1`; this Orient is `+1,+1,−1,−1` | ATTEMPTED |
| nm2oricyccz two-axis lex-smallest | reuse two-axis reverse hold and face hold | two-axis Orient is `+1,+1,−1,−1` with reverse HOLD and face HOLD on these z-probes; this far-face seed records `(0,0,−1)` at tick 0 locking `+e_3`, while the two-axis child forms at tick 1 locking `−e_3` | ATTEMPTED |
| nm2oricycc3z near-face lex-smallest | reuse near-face unique signed HOLD at `B` and at `D` | near-face `O(B)` is `{+e_2,+e_3}` without `−e_3`; this far-face unique signed fails at each probe | ATTEMPTED |
| nm2oricyclz two-axis HOLD | reuse two-axis lex-largest reverse hold and face hold | two-axis lex-largest Orient is `−1,−1,+1,+1`; this far-face lex-smallest member is `+1,+1,−1,−1` | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold on these z-probes | cover HOLDs reverse and face without cyclic signed columns | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse hold and split face hold | split HOLDs reverse and face without cyclic order of `Axis(M)`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails and leftover face fails while this reverse HOLDs and this face HOLDs; leftover of the union is empty while Orient is a sign; unique signed `O={+e_1,+e_3}` has empty leftover and Orient `+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse and face of `M` and of `O` | exist-opposite reverse of signed `O` HOLDs as this reverse HOLDs, but exist-opposite face of signed `O` fails while this face HOLDs; exist-opposite does not read cyclic columns | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at each of `A,B,C,D` without cyclic columns; leftover-axis face still fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `+1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both agree; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and split HOLDs at `C` | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse HOLDs as this reverse HOLDs; y-face fails while this z-face HOLDs; this letter is the four z-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe `C` is `(2,0,0)`, not the far-face third-pair seed; this letter is the four z-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-smallest outgoing determinant orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse hold and face hold on the three-axis far-face opposite seed with singleton `M` at each z-probe | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_3` while cyclic is `(+e_3,+e_1)` | ATTEMPTED |
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
missing identification of Orient with nm2orichz leftover-axis, missing
identification of Orient with nm2orionez lex-one, missing identification of
Orient with cyclic lex-largest, missing identification of Orient with
nm2oricyccz, missing identification of Orient with
nmcover axis-cover, missing identification of Orient with nm2axz axis-cover,
missing identification of Orient with nm2ax12z 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3` at far-face `(0,0,−1)/(0,1,−1)` opposite the
z-probes, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis, cover as
complementary occupation of `{e_1,e_2,e_3}`, split as cover and
`|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic next/prev axes
of `Axis(M)`, lex-smallest signed outgoing letter under `+e < −e` (hence
`+e` if both signs), integer determinant sign, empty `O_next` or empty
`O_prev` as Orient fail not `UNDEFINED`, split fail as Orient fail not
`UNDEFINED`, four z-probes with seed `A`, second pair as a new seed not a
formed child, third pair as a new seed not a formed child, and mixed
remains a set are declared. No uniqueness of outgoing locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

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

**Steelman:** Orient reverse hold and face hold are only leftover of
two-axis nm2oricyccz; cover and split already answer the member; unique
signed `|O_i|=1` already answers mixed `O`; leftover of `M` alone
already answers reverse; leftover of `O` alone already answers reverse;
exist-opposite of signed `O` already answers reverse; leftover-axis already
gives a reverse HOLD; mixed #7188 already reported the three-axis
member; the third pair is only a formed child of the two-axis seed; unique
outgoing letters should be required; cyclic lex-largest already gives HOLD
bits on this far-face seed; and unsigned incoming axis already gives the
same signs because each `M` letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail, while this reverse HOLDs and this face HOLDs. Orient reverse
HOLDs because `Orient(A)=+1` and `Orient(B)=+1`. Orient face HOLDs because
the signs are `−1` and `−1`. Cover and split HOLD reverse and face on this
member and do not score cyclic signed columns. Leftover-axis reverse HOLDs
with `−1,−1`, but leftover-axis face fails with `+1,−1` while this face
HOLDs with `−1,−1`. Lex-one reverse fails from `e1<e2<e3` order independent
of `m` while this reverse HOLDs, and lex-one face HOLDs with `−1,−1` as
this face HOLDs, but those columns are axis-order. Lexicographic unsigned
`o1,o2` reverse fails with `−1,+1` and face HOLDs with `+1,+1`. Unique
signed `|O_i|=1` fails at each of `A,B,C,D` while this Orient is
`+1,+1,−1,−1`. Cyclic lex-largest reverse HOLDs with `−1,−1` and face
HOLDs with `+1,+1`; those signs are not these signs. Two-axis nm2oricyccz
reverse HOLDs and face HOLDs with the same `+1,+1,−1,−1` on these
z-probes, from a four-site seed that forms `(0,0,−1)` at tick 1 locking
`−e_3`. Presence of an opposite pair in `O` HOLDs at each of `A,B,C,D`
without cyclic columns. Leftover of `M` alone at `A` is `{e_1,e_3}` and
at `B` is `{e_2,e_3}`: nonempty unequal. Leftover of `O` alone at `A` is
`{e_2}` and at `B` is `{e_1}`. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(A)`; this Orient is `+1`, not `UNDEFINED`. On
unique signed `O={+e_1,+e_3}` leftover is empty while Orient is `+1`, so
leftover-empty fail is not this predicate. Mixed #7188 is a different
z-symmetric process with mixed `M` and reverse fail face fail. The second
pair is a new seed, not a formed child: `(0,0,1)` is recorded at tick 0
with lock `+e_2`, whereas the 1-axis child forms at tick 1 with lock
`+e_3`. The third pair is a new seed, not a formed child, on the `−z`
face opposite the z-probes: `(0,0,−1)` is recorded at tick 0 with lock
`+e_3`, whereas the two-axis child forms at tick 1 with lock `−e_3`.
Reverse oriented frame is HOLD iff equal `±1` signs at `A` and at `B`,
not leftover of leftover-axis and not leftover of cyclic lex-largest.

### N8 — cross-cycle echo

nm2axz cover on the two-axis opposite seed reported cover HOLD at each of
the four z-probes, reverse hold, and face hold. nm2ax12z 1-in 2-out split
on that seed reported split HOLD at each of the four z-probes, reverse
hold, and face hold. nm2oricyccz cyclic lex-smallest on that two-axis seed
reported Orient `+1,+1,−1,−1`, reverse hold, and face hold. On this
three-axis far-face seed, cover and split still HOLD reverse and face, and
cyclic lex-smallest reverse HOLDs and face HOLDs with the same signs as
that two-axis member; the seed is different: six tick-0 sites, third pair
on the `−z` face. Cyclic lex-largest on this same far-face seed reported
Orient `−1,−1,+1,+1`, reverse hold, and face hold. nm2oricycl3z on the
near third pair `(2,0,0)/(2,1,0)` reported reverse fail and face fail.
nm2oricycc3z near-face lex-smallest reported reverse hold and face hold
with unique signed HOLD at `B` and at `D`. nm2chiralz lexicographic
unsigned `o1,o2` on this seed reported Orient `−1,+1,+1,+1`, reverse fail,
and face hold. nm2oridetz unique signed outgoing letters on this seed
reported Orient fail at each of `A,B,C,D`. nm2orichz leftover-axis on this
seed reported reverse hold and face fail. nm2orionez lex-one on this seed
reported Orient `−1,+1,−1,−1`, reverse fail, and face hold from
`e1<e2<e3` order independent of `m`. Leftover axis reported empty leftover
at each of four z-probes, leftover reverse fail, and leftover face fail.
The four y-probes of this same seed reported cyclic Orient `+1` at `A`
from `m=−e_1` and `+1` at `B`, so y-reverse HOLDs as this reverse HOLDs;
y-face fails from split fail at `D`. This note is not those
displays: it reports cyclic next/prev lex-smallest outgoing determinant
orientation of the 1-in 2-out frame of `M` and `O` at `τ=t+1` on the
three-axis far-face opposite seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and
`t(D)=1`, `Orient(A)=+1`, `Orient(B)=+1`, `Orient(C)=−1`,
`Orient(D)=−1`, reverse hold, and face hold. Cover and split do not score
handedness.

**Gate disposition:** PASS for the cyclic-next-prev-lex-smallest-outgoing-determinant `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals nm2chiralz lexicographic unsigned `o1,o2`
HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orichz leftover-axis HOLD,” “the predicate equals
nm2orionez lex-one HOLD,” “the predicate equals cyclic lex-largest HOLD,”
“the predicate equals nm2oricyccz two-axis HOLD,” “the predicate equals
nm2oricyclz two-axis HOLD,” “the predicate equals
nmcover axis-cover HOLD,” “the predicate equals nm2axz axis-cover HOLD,”
“the predicate equals nm2ax12z 1-in 2-out split HOLD,” “the predicate
equals the 1-axis opposite two-site seed,” “the predicate equals nmunopp
union,” “bits are Admissibility,” “split fail is UNDEFINED,” or “empty
`O_i` is UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis far-face
opposite perp-step incoming-lock process, reads each probe's own earliest
incoming set and own outgoing dual from the record prefix at that probe's
`t+1`, reports split of the pair, reports the unique signed incoming
letter, the axis index `i` of `m`, and the cyclic next/prev lex-smallest
outgoing letters, reports the integer determinant and its sign, lists new
records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that Orient is
`+1,+1,−1,−1` from cyclic lex-smallest columns, that reverse HOLDs and face
HOLDs while leftover-empty reverse and leftover-empty face fail, that
two-axis nm2oricyccz reverse HOLDs and face HOLDs with the same
`+1,+1,−1,−1` from a four-site seed that is not this far-face seed, that
cyclic lex-largest reverse HOLDs and face HOLDs with opposite signs
`−1,−1,+1,+1` on this same seed, that leftover-axis face fails while this
face HOLDs, that lex-one reverse fails while this reverse HOLDs, that
split fail is Orient fail not `UNDEFINED`, that empty `O_next` or empty
`O_prev` is Orient fail not `UNDEFINED`, that the 1-axis opposite two-site
seed is a different member with Orient fail at `C`, that leftover-empty
fail is a different predicate, that leftover of `M` alone and leftover of
`O` alone are different objects, that mixed sets remain sets, that
unique-letter Orient is `UNDEFINED` at mixed `O`, that unique signed fails
at each probe while this Orient is defined, that the construction
does not sum, that a formation member from already-recorded six-neighbor
locks is not attached, that the second pair is a new seed not a formed
child, that the third pair is a new seed not a formed child on the `−z`
face opposite the z-probes, that the y-probes and x-probes of this seed
are not this letter, and that the display is not the
two-tick lock-count clock composition. No runner cache is written.
