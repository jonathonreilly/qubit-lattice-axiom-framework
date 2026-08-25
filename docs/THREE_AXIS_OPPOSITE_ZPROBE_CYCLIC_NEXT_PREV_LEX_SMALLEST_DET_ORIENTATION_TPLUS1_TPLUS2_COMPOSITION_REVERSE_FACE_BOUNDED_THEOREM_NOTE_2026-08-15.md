---
claim_id: three_axis_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic lex-smallest orientation at t+1 versus t+2 on the four z-probes of the three-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Cyclic Lex-Smallest Orientation Freeze t+1 Versus t+2 Reverse And Face On Four Z-Probes Of The Three-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-smallest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ1=t+1` and `τ2=t+2`, reverse/face from that
sign at each cut, and composition of Orient, on the four z-probes of the
three-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same process and z-probes
as nm2axz. Orient as nm2oricyccz at each cut. `M` and `O` as nm2ax12z.
Let `t(q)` be the formation tick of probe `q`. Cuts are local: `τ1=t+1`,
`τ2=t+2`. There is no global T. Do not score τ=t. `M(q,τ)` is the set of
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
likewise. `Orient(q,τ)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. Reverse HOLDs if and only if `Orient(A)=Orient(B)` both
`±1` at that cut. Face HOLDs if and only if `Orient(C)=Orient(D)` both
`±1` at that cut. Composition HOLDs if and only if `Orient` at `τ1` equals
`Orient` at `τ2` at `A,B,C,D`. Cover and split do not score handedness.
This is not leftover of nm2oricyccz cyclic lex-smallest orientation at
`t+1` on the two-axis opposite seed. This is not leftover of nm2oricycl3z
cyclic lex-largest reverse fail and face fail on this three-axis seed.
This is not leftover of cyclic lex-smallest orientation at `t+1` alone. This is not leftover of nm2simt2z simultaneous `M` and `O`
freeze. This is not leftover of nm2orichz leftover-axis reverse HOLD whose
face fails because C and D swap `(m,pair)` columns. This is not leftover
of nm2orionez lex-one reverse fail whose face HOLDs from `e1<e2<e3` order
independent of `m`. This is not leftover of nm2chiralz lexicographic
unsigned `o1,o2` orientation. This is not leftover of nm2oridetz unique
signed outgoing letters. This is not leftover of nm2axz axis-cover. This
is not leftover of nm2ax12z 1-in 2-out split. This is not leftover of
leftover-of-`M` alone. This is not leftover of leftover-of-`O` alone. This
is not leftover-empty fail of leftover axis. This is not leftover of
nmunopp union. This is not leftover of nmt2opp `M` frozen at `t`. This is
not leftover of nmot2opp two-tick composition. This is not leftover of
nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188
fail/fail. This is not leftover of the 1-axis opposite two-site seed. This
is not leftover of the same-lock two-site seed. The second pair is a new
seed, not a formed child. Uniqueness is not required. Mixed remains a
set. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/three_axis_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+1` and `τ2=t+2`. Axis is the unsigned lattice direction of a signed
lock. Cover is the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)`
and `Axis(O)`. Split is cover together with `|Axis(M)|=1`. The cyclic
next/prev lex-smallest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-smallest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. Reverse and face are scored on equal `±1`
signs at the paired probes at each cut. Composition is equality of those
four Orient reports across the two cuts. Named signs `{+,−}` of locks are
a coarser readout and are not used as the object. A singleton unique outgoing lock
letter is a different readout and is not used as the object. Unsigned
axis units of `Axis(O)` are a different readout and are not used. Unique
signed letters requiring `|O_i|=1` are a different readout and are not
used. Opposite-pair leftover-axis orientation is a different readout and
is not used. Lex-one signed outgoing letters in axis order `e1<e2<e3`
independent of `m` are a different readout and are not used. Cyclic
lex-largest (`−e` if both signs) is a different readout and is not used.
Existential opposite of signed locks is a different readout and is not
used. Axis-cover without the frame sign is a different readout and is not
used. 1-in 2-out split without the frame sign is a different readout and
is not used. Simultaneous `M` and `O` freeze is a different readout and
is not used. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic lex-smallest orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 on the four z-probes of the three-axis opposite seed, Orient at A,B,C,D at each cut, reverse hold and face hold at each cut, composition hold; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_opposite_zprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display cyclic lex-smallest orientation freeze t+1 versus t+2 reverse/face composition on the four z-probes of the three-axis opposite seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic lex-smallest orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 displayed; do not write Orient into Admissibility, do not reduce to nm2oricyccz two-axis t+1, do not reduce to nm2oricycl3z lex-largest fail/fail, do not reduce to t+1 alone, do not reduce to nm2simt2z M-and-O freeze, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to leftover-axis, do not reduce to lex-one signed e1<e2<e3, do not reduce to cyclic lex-largest, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic lex-smallest orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 on the four z-probes of the three-axis opposite seed, reverse/face at each cut, and composition; displayed, not adopted"
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
x-probes is the third-pair seed `(2,0,0)`. Same process and
z-probes as nm2axz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(2,0,0)` locks `+e_3`. Site `(2,1,0)`
locks `−e_3`. The second pair is a new seed, not a formed
child of the first pair. The third pair is a new seed, not a formed child:
on the two-axis opposite seed those sites form at tick 3 locking `+e_1`.
This seed is not the two-axis opposite seed of nm2oricyccz. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0.

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

## Named cyclic next/prev lex-smallest determinant of `M` and `O` at `τ1` and `τ2`

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T.
Do not score `τ=t`.

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

Cover at a probe at a cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

Split at a probe at a cut:

```text
split(q) HOLDs iff cover HOLDs and |Axis(M)|=1
(hence |Axis(O)|=2).
```

2-in 1-out is fail of split, not UNDEFINED. If `q` is unformed at `τ`, then
split is `UNDEFINED`.

Oriented frame at a cut, as nm2oricyccz:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1→1. e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}. O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is lex-smallest in O_next (hence +e if both signs).
o_prev likewise.
Orient(q,τ) = sign of the integer determinant of columns (m, o_next, o_prev).
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

Reverse oriented frame at a cut holds if and only if `Orient(A)=Orient(B)`
and both signs are `±1`. Face oriented frame at a cut holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Composition holds if and only if `Orient(q,τ1)=Orient(q,τ2)` at each of
`A,B,C,D`. Either side `UNDEFINED` is `UNDEFINED`. Else if the four signs
agree across the two cuts, composition HOLDs. Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse and face without reading
cyclic signed columns; leftover-axis face fails while this face HOLDs.
Identifying split reverse with this reverse is refused: split HOLDs reverse
and face without the cyclic order of `Axis(M)`. Identifying leftover-empty
fail with this reverse is refused: leftover-empty fail scores empty leftover
as reverse fail and face fail, while this reverse HOLDs and this face HOLDs;
on unique signed `O={+e_1,+e_3}` leftover is empty while Orient is `+1`.
Identifying lexicographic unsigned `o1,o2` with this reverse is refused:
unsigned reverse fails and unsigned face HOLDs with `+1,+1`, while this
reverse HOLDs and this face HOLDs with `+1,+1` then `−1,−1`. Identifying
nm2orionez lex-one signed `e1<e2<e3` with this reverse is refused: lex-one
reverse fails from axis order independent of `m`, while this reverse HOLDs.
Identifying unique signed `|O_i|=1` with this reverse is refused: unique
signed reverse fails because `A` and `C` have an opposite pair in `O`,
while this reverse HOLDs. Identifying leftover-axis orientation with this
reverse is refused: leftover-axis reverse fails because `B` has no
opposite pair in `O`, while this reverse HOLDs. Identifying cyclic
lex-largest with this reverse is refused: lex-largest picks `−e` if both
signs and reports reverse fail and face fail. Identifying nm2oricyccz
two-axis lex-smallest with this freeze is refused: that seed has mixed
`O(B)` and `O(D)` with an extra `−e_3`. Identifying nm2oricycl3z with this
reverse is refused: that letter is lex-largest fail/fail on this seed.
Identifying nm2simt2z `M` and `O` freeze with this composition is refused:
that letter is equality of lock sets, not equality of
`det(m,o_next,o_prev)` signs. Identifying a named sign of those locks with
reverse or face is refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, and Orient at `τ1` and `τ2`

On this process the four z-probes form. Compare to leftover axis: that
leftover reports empty leftover at each probe and leftover reverse fail
and leftover face fail. Compare to nm2axz cover and nm2ax12z split: both
HOLD reverse and face on this member. Compare to nm2chiralz lexicographic
unsigned `o1,o2` orientation: reverse fails and face HOLDs on this member
with signs `−1,+1,+1,+1`. Compare to nm2oridetz unique signed outgoing
letters: reverse fails and face fails because `|O_i|≠1`. Compare to
nm2orichz leftover-axis reverse fail whose face fails because `B` and `D`
have no opposite pair in `O`. Compare to nm2orionez lex-one reverse fail
whose face HOLDs from `e1<e2<e3` order independent of `m`. Compare to
nm2oricycl3z cyclic lex-largest: reverse fails and face fails with
`−1,+1,+1,−1`. Compare to nm2oricyccz: that letter is two-axis lex-smallest
at `t+1` alone. This display reads the cyclic next/prev lex-smallest
outgoing determinant of those same timed sets at both cuts:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=1
M(A, τ1) = {+e_2}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_3}
M(D, τ1) = {+e_1}
O(A, τ1) = {+e_1, −e_1, +e_3}
O(B, τ1) = {+e_2, +e_3}
O(C, τ1) = {+e_1, −e_1, −e_2}
O(D, τ1) = {−e_2, +e_3}
split(A, τ1) = hold
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = hold
m(A, τ1) = +e_2
i(A, τ1) = 2
o_next(A, τ1) = +e_3
o_prev(A, τ1) = +e_1
det(A, τ1) = 1
Orient(A, τ1) = +1
m(B, τ1) = +e_1
i(B, τ1) = 1
o_next(B, τ1) = +e_2
o_prev(B, τ1) = +e_3
det(B, τ1) = 1
Orient(B, τ1) = +1
m(C, τ1) = +e_3
i(C, τ1) = 3
o_next(C, τ1) = +e_1
o_prev(C, τ1) = −e_2
det(C, τ1) = -1
Orient(C, τ1) = −1
m(D, τ1) = +e_1
i(D, τ1) = 1
o_next(D, τ1) = −e_2
o_prev(D, τ1) = +e_3
det(D, τ1) = -1
Orient(D, τ1) = −1
M(A, τ2) = {+e_2}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_3}
M(D, τ2) = {+e_1}
O(A, τ2) = {+e_1, −e_1, +e_3}
O(B, τ2) = {+e_2, +e_3}
O(C, τ2) = {+e_1, −e_1, −e_2}
O(D, τ2) = {−e_2, +e_3}
Orient(A, τ2) = +1
Orient(B, τ2) = +1
Orient(C, τ2) = −1
Orient(D, τ2) = −1
```

`A` is a seed at tick 0 with seed letter `+e_2`. Mixed remains a set:
`O(A,τ1)` has three outgoing steps and `O(C,τ1)` has three outgoing steps.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Unique
signed `|O_i|=1` fails at `A` and at `C` because those probes have an
opposite pair in `O`; it HOLDs at `B` and at `D` because `O(B)={+e_2,+e_3}`
and `O(D)={−e_2,+e_3}` have one letter per axis. Cyclic lex-smallest picks
`+e` on each mixed cyclic slot, so `(o_next,o_prev)` is defined at `A` and
at `C`. `M` is a singleton at each probe, so the unique signed `m` exists.
At each probe at each cut split HOLDs. Cover and split HOLD at each probe
and do not score that cyclic lex-smallest Orient is `+1,+1,−1,−1`. At `A`,
`i=2` so `e_next=e_3` and `e_prev=e_1`; mixed `O_prev={±e_1}` yields
`o_prev=+e_1`. At `C`, `i=3` so `e_next=e_1` and `e_prev=e_2`; mixed
`O_next={±e_1}` yields `o_next=+e_1`. Leftover-axis at `A` is pair `+e_1`
leftover `+e_3` and that Orient is `−1`; leftover-axis at `B` and at `D`
fails from no opposite pair. Lex-one at `A` uses axis order
`(+e_1,+e_3)` independent of cyclic next/prev of `m` and reports `−1`,
while cyclic `(o_next,o_prev)=(+e_3,+e_1)` reports `+1`. Cyclic lex-largest
at `A` picks `o_prev=−e_1` and reports `−1`. The third pair removes `−e_3`
from `O(B)` and from `O(D)` relative to the two-axis opposite seed. O is
not M.

On the 1-axis opposite two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and `C` is 2-in 1-out, so split fails at `C` and
Orient at `C` is fail, not UNDEFINED. That is leftover of the first pair.
Here both `(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a
second axis, and `(2,0,0)` and `(2,1,0)` are seeds of a third opposite pair.
On the y-probes of this same seed, split HOLDs at `A` with `m=−e_1` so
`i=1`, `o_next=+e_2`, `o_prev=−e_3`, and cyclic lex-smallest Orient at that
y-probe is `+1`. Y-probe `B` is `+1`, so y-probe reverse HOLDs as this
z-probe reverse HOLDs. Y-probe `D` has split fail, so y-face fails while
this z-face HOLDs.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`. The `t+2` neighbor of `A` forms with
earliest incoming `+e_3`, so `−e_2` does not enter `O(A,τ2)`. The `t+2`
neighbor of `B` forms with earliest incoming `−e_2`, so `+e_1` does not
enter `O(B,τ2)`. The `t+2` neighbor of `D` forms with earliest incoming
`+e_2`, so `+e_1` does not enter `O(D,τ2)`:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2)
new 6-NN of A at t(A)+2: (0, -1, 1)
new 6-NN of B at t(B)+2: (2, 1, 1)
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: (2, 0, 1)
```

`M` is frozen from `t` to `t+1` and from `t+1` to `t+2`. At `t`, `O` is
empty at each probe, split fails, and Orient is fail, not UNDEFINED.
Do not score `τ=t`.

## Theorem 2 — reverse and face from oriented frame at `τ1` and `τ2`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. At `τ1`, `Orient(A)=+1` and `Orient(B)=+1`. Reverse HOLDs. At `τ2`,
`Orient(A)=+1` and `Orient(B)=+1`. Reverse HOLDs. This is HOLD iff equal
`±1` signs, not leftover of nm2chiralz lexicographic unsigned `o1,o2`,
not leftover of nm2oridetz unique signed outgoing letters, not leftover
of nm2orichz leftover-axis, not leftover of nm2orionez lex-one, not
leftover of nm2axz axis-cover, not leftover of nm2ax12z 1-in 2-out split,
not leftover of nm2oricycl3z lex-largest, not leftover-empty fail, and
not exist-opposite.

Reverse oriented frame at τ1: hold
Reverse oriented frame at τ2: hold

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Leftover-axis reverse fails because leftover-axis at `B` has no opposite
pair in `O`, while this reverse HOLDs. Lexicographic unsigned reverse
fails because unsigned `Orient(A)=−1` and `Orient(B)=+1`. Unique signed
reverse fails because unique signed at `A` fails. Lex-one signed reverse
fails because lex-one `Orient(A)=−1` from `e1<e2<e3` order independent of
`m`. Cyclic lex-largest reverse fails with `−1,+1`. Leftover-empty reverse
fails because leftover of the union is empty at `A` and at `B`. Leftover
of `M` reverse fails because leftover of `M` at `A` is `{e_1, e_3}` and at
`B` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` reverse fails
because leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`: nonempty
and unequal. Exist-opposite reverse of signed `M` fails. Exist-opposite
reverse of signed `O` fails. Presence of an opposite pair in `O` HOLDs at
`A` and fails at `B`. Those leftovers are not this display.

Reverse HOLDs at both cuts.

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
At `τ1`, `Orient(C)=−1` and `Orient(D)=−1`. Face HOLDs. At `τ2`,
`Orient(C)=−1` and `Orient(D)=−1`. Face HOLDs.

Face oriented frame at τ1: hold
Face oriented frame at τ2: hold

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. Cyclic lex-smallest oriented face
HOLDs because both signs are `−1`. Leftover-axis face fails because
leftover-axis at `D` has no opposite pair. Lex-one signed oriented face
HOLDs because both lex-one signs are `−1`; those signs are these signs at
`C` and at `D` but lex-one reverse fails. Lexicographic unsigned face
HOLDs because both unsigned signs are `+1`; those unsigned columns are
not cyclic `o_next,o_prev`. Unique signed face fails because unique signed
at `C` fails. Cover and split do not score handedness. Presence of an
opposite pair in `O` HOLDs at `C` and fails at `D`, so pair-presence face
fails while this face HOLDs from cyclic lex-smallest columns. On the
1-axis opposite two-site seed, cover face HOLDs while split face fails at
`C` from 2-in 1-out, and Orient at `C` is fail, not UNDEFINED. This
three-axis member is not leftover of that 1-axis split face fail. The
four y-probes of this same seed give cyclic lex-smallest Orient `+1` at
`A` and Orient fail at `D` from split fail, so oriented y-face fails
while this z-face HOLDs. The four x-probes give oriented reverse fail and
oriented face fail. Those probe-direction readouts are not this z-probe
display. Leftover-empty face fails because leftover of the union is empty
at `C` and at `D`. Leftover of `M` at `C` is `{e_1, e_2}` and leftover of
`M` at `D` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` at `C`
is `{e_3}` and leftover of `O` at `D` is `{e_1}`: nonempty and unequal.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed
`O` fails. Cyclic lex-smallest oriented face HOLDs.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover HOLDs at `D` and split HOLDs at `D`. Orient at `D`
is `−1` from cyclic `(−e_2,+e_3)` with unique letters per axis of `O`.

Reverse holds at both cuts. Face holds at both cuts.

## Theorem 3 — composition of Orient at `τ1` versus `τ2`

Composition HOLDs if and only if `Orient` at `τ1` equals `Orient` at `τ2`
at `A,B,C,D`. `Orient(A,τ1)=Orient(A,τ2)=+1`,
`Orient(B,τ1)=Orient(B,τ2)=+1`, `Orient(C,τ1)=Orient(C,τ2)=−1`,
`Orient(D,τ1)=Orient(D,τ2)=−1`. Composition HOLDs.

Composition of Orient: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

The reverse-and-face orientation of nm2oricyccz on the three-axis seed
(reverse HOLD, face HOLD at `t+1`) freezes at `t+2`: the four signs are
unchanged. That freeze is the present letter. It is not leftover of
nm2oricyccz on the two-axis seed, which has mixed `O(B)` and `O(D)`. It
is not leftover of nm2oricycl3z, which scores lex-largest reverse fail
and face fail on this seed at one cut. It is not leftover of a `t+1` cut
alone. It is not leftover of nm2simt2z, which scores equality of `M` and
of `O` rather than equality of Orient. On this member `M` and `O` also
freeze, so simultaneous freeze HOLDs as a leftover; the scored object
remains the four Orient signs. Bit-stability of reverse HOLD and face
HOLD is a leftover predicate: those bits can agree while a probe sign
flips, which composition of Orient would fail. Composition of Orient at
`τ=t` versus `τ=t+1` fails because Orient is fail at formation and `±1`
at `t+1`. Do not score `τ=t`.

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
- It does not replace Orient by unsigned axis units of `Axis(O)`.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not replace Orient composition by nm2simt2z `M` and `O` freeze.
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
- It does not reprint nm2orichz leftover-axis reverse fail face fail as
  this oriented display.
- It does not reprint nm2orionez lex-one reverse fail face hold as this
  oriented display.
- It does not reprint nm2oricycl3z cyclic lex-largest reverse fail face
  fail at `t+1` alone.
- It does not reprint nm2oricyccz cyclic lex-smallest orientation on the
  two-axis opposite seed.
- It does not reprint nm2simt2z simultaneous `M` and `O` freeze as this
  Orient composition.
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
three-axis opposite seed process, cyclic lex-smallest orientation of the 1-in
2-out frame of `M` and `O` at `t+1` versus `t+2`, reverse/face at each cut,
and composition of Orient are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ1` and at `τ2` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ1` and at `τ2` | Theorem 1; HOLDING outgoing dual, freeze |
| unique signed `m`, axis index `i`, cyclic `(o_next,o_prev)` | Theorem 1; singleton `M`, lex-smallest pair defined |
| integer `det(m,o_next,o_prev)` at both cuts | Theorem 1; `1`, `1`, `-1`, `-1` at each cut |
| Orient at `τ1` | Theorem 1; `+1`, `+1`, `−1`, `−1` |
| Orient at `τ2` | Theorem 1; `+1`, `+1`, `−1`, `−1` |
| reverse from oriented frame at `τ1` and at `τ2` | Theorem 2; `hold` at each cut |
| face from oriented frame at `τ1` and at `τ2` | Theorem 2; `hold` at each cut |
| composition of Orient | Theorem 3; `hold` |
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
| leftover of nm2oricycl3z lex-largest fail/fail | not this freeze letter |
| leftover of nm2oricyccz two-axis `t+1` | not this freeze letter |
| leftover of nm2simt2z `M` and `O` freeze | not this Orient composition |
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
| score at `τ=t` | refused |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: do the reverse-and-face cyclic lex-smallest Orient signs of the three-axis opposite seed freeze from `t+1` to `t+2` on the four z-probes. |
| V2 | Current main has no landed cyclic-lex-smallest reverse/face composition of timed `M` and `O` at `t+1` versus `t+2` on these four z-probes of the three-axis opposite seed. |
| V3 | Orient reports at two cuts, the reverse/face bits at each cut, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at two local cuts and reports that reverse HOLDs, face HOLDs, and the four signs freeze, while lex-largest reverse fails and face fails, leftover-axis reverse fails, unique signed reverse fails, and nm2simt2z scores lock-set equality rather than Orient equality. |
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
nmcover axis-cover, does not replace Orient by nm2axz axis-cover, does not
replace Orient by nm2ax12z 1-in 2-out split, does not replace this freeze
by nm2oricyccz two-axis `t+1`, does not replace this freeze by
nm2oricycl3z lex-largest fail/fail, does not replace Orient composition by
nm2simt2z `M` and `O` freeze, does not identify this display with the
1-axis opposite two-site seed, and does not identify it with nmunopp
union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2oricyccz two-axis `t+1` | reuse reverse hold and face hold on the two-axis seed | that seed has mixed `O(B)` and `O(D)` with extra `−e_3`; this letter is the three-axis freeze | ATTEMPTED |
| nm2oricycl3z lex-largest | reuse cyclic lex-largest reverse fail and face fail | lex-largest reverse fails and face fails with `−1,+1,+1,−1`; this reverse HOLDs and this face HOLDs with `+1,+1,−1,−1` | ATTEMPTED |
| `t+1` cut alone | reuse reverse hold and face hold at one cut | that letter has no `t+2` cut and no Orient composition | ATTEMPTED |
| nm2simt2z `M` and `O` freeze | score equality of lock sets | simultaneous freeze HOLDs here as leftover; composition of this letter is equality of Orient signs | ATTEMPTED |
| reverse/face bit-stability | score reverse and face bits equal across cuts | those bits can agree while a probe sign flips; composition of Orient would then fail | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face hold | unsigned reverse fails while this reverse HOLDs; unsigned `o1,o2` at `C` is `(e_1,e_2)` while cyclic is `(+e_1,−e_2)` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed reverse fails because `A` is mixed; this reverse HOLDs; unique signed at `B` and at `D` HOLDs while `A` and `C` fail | ATTEMPTED |
| nm2orichz leftover-axis | reuse leftover-axis reverse hold and face fail | leftover-axis reverse fails because `B` has no opposite pair; this reverse HOLDs | ATTEMPTED |
| nm2orionez lex-one | reuse lex-one reverse fail and face hold | lex-one reverse fails from `e1<e2<e3` order independent of `m`; this reverse HOLDs from cyclic next/prev of `Axis(M)` | ATTEMPTED |
| cyclic lex-largest | reuse same cyclic axes with `−e` if both signs | lex-largest reverse fails and face fails with `−1,+1,+1,−1`; this Orient is `+1,+1,−1,−1` | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold on these z-probes | cover HOLDs reverse and face without cyclic signed columns | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse hold and split face hold | split HOLDs reverse and face without cyclic order of `Axis(M)`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails while this reverse HOLDs; leftover face fails while this face HOLDs; unique signed `O={+e_1,+e_3}` has empty leftover and Orient `+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal; leftover of `M` reverse fails while this reverse HOLDs | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` fails while this reverse HOLDs; exist-opposite face of signed `O` fails while this face HOLDs | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence reverse fails because `B` has no opposite pair; this reverse HOLDs | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `+1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both agree; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| score at `τ=t` | compose Orient at formation versus `t+1` | leftover of nmot2opp; Orient is fail at `t` and `±1` at `t+1`; Do not score `τ=t` | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and split HOLDs at `C` | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse HOLDs (`+1,+1`) and y-face fails; this letter is the four z-probes with face HOLD | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four z-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-smallest outgoing determinant orientation of own incoming and outgoing at `t+1` versus `t+2` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse hold and face hold at both cuts on the three-axis opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_3` while cyclic is `(+e_3,+e_1)` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
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
nmcover axis-cover, missing identification of Orient with nm2axz axis-cover,
missing identification of Orient with nm2ax12z 1-in 2-out split, missing
identification of this freeze with nm2oricyccz two-axis `t+1`, missing
identification of this freeze with nm2oricycl3z lex-largest fail/fail, missing
identification of Orient composition with nm2simt2z `M` and `O` freeze,
missing identification of this seed with the 1-axis opposite two-site seed,
and missing Record identification of Orient reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3`, perpendicular step rule, incoming-step lock,
own incoming set and own outgoing dual from records with tick `<= τ`,
per-probe `τ1=t+1` and `τ2=t+2`, unsigned axis, cover as complementary
occupation of `{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, unique
signed `m` when split HOLDs, cyclic next/prev axes of `Axis(M)`,
lex-smallest signed outgoing letter under `+e < −e` (hence `+e` if both
signs), integer determinant sign, empty `O_next` or empty `O_prev` as
Orient fail not `UNDEFINED`, split fail as Orient fail not `UNDEFINED`,
four z-probes with seed `A`, second pair as a new seed not a formed child,
third pair as a new seed not a formed child, mixed remains a set, and
composition as equality of Orient at the two cuts are declared.
No uniqueness of outgoing locks, no six-neighbor lock union as the scored
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
| per element | unique signed incoming letter and cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at a probe's `t+1` and `t+2` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports at `t+1` and `t+2`, reverse/face at each cut, composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, a later cut `t+3`, and a physical selector among 1-in
2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse hold and face hold are only leftover of cover
and split; leftover-axis already answers reverse; lex-one already answers
face HOLD; unique signed `|O_i|=1` already answers mixed `O`; leftover of
`M` alone already answers reverse; leftover of `O` alone already answers
reverse; exist-opposite of signed `O` already answers reverse; mixed #7188
already reported fail/fail; the second pair is only the formed child
`(0,0,1)` of the 1-axis seed; the third pair is only a formed child of the
two-axis seed; unique outgoing letters should be required; cyclic
lex-largest already gives the same split HOLD; unsigned incoming axis
already gives the same signs because each `M` letter is the positive unit;
because `M` and `O` freeze, composition is nm2simt2z; because reverse HOLD
and face HOLD at both cuts, composition is only bit-stability; nm2oricyccz
already answered reverse-and-face lex-smallest orientation; and
nm2oricycl3z already displayed this seed.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Orient reverse HOLDs because `Orient(A)=+1` and
`Orient(B)=+1`. Orient face HOLDs because both signs are `−1`. Cover and
split HOLD reverse and face on this member and do not score cyclic signed
columns. Leftover-axis reverse fails because `B` has no opposite pair;
this reverse HOLDs. Lex-one reverse fails from `e1<e2<e3` order
independent of `m`; this reverse HOLDs. Lexicographic unsigned `o1,o2`
reverse fails with `−1,+1` and face HOLDs with `+1,+1`. Unique signed
`|O_i|=1` reverse fails because `A` is mixed; this reverse HOLDs. Cyclic
lex-largest reverse fails and face fails with `−1,+1,+1,−1`; those signs
are not these signs. Presence of an opposite pair in `O` HOLDs at `A` and
at `C` and fails at `B` and at `D`. Leftover of `M` alone at `A` is
`{e_1,e_3}` and at `B` is `{e_2,e_3}`: nonempty unequal. Leftover of `O`
alone at `A` is `{e_2}` and at `B` is `{e_1}`. Unique outgoing letters
would assign `UNDEFINED` at mixed `O(A)`; this Orient is `+1`, not
`UNDEFINED`. On unique signed `O={+e_1,+e_3}` leftover is empty while
Orient is `+1`, so leftover-empty fail is not this predicate. Mixed #7188
is a different z-symmetric process with mixed `M`. The second pair is a
new seed, not a formed child: `(0,0,1)` is recorded at tick 0 with lock
`+e_2`, whereas the 1-axis child forms at tick 1 with lock `+e_3`. The
third pair is a new seed, not a formed child: on the two-axis seed those
sites form at tick 3 locking `+e_1`. nm2oricyccz scores the two-axis seed.
nm2oricycl3z scores lex-largest fail/fail at one cut. nm2simt2z scores
equality of `M` and of `O`. Reverse/face bit-stability can HOLD while a
probe sign flips. Reverse oriented frame is HOLD iff equal `±1` signs at
`A` and at `B` at that cut, not leftover of leftover-axis and not leftover
of nm2orionez lex-one. Composition of Orient: hold.

### N8 — cross-cycle echo

nm2axz cover on this three-axis seed reported cover HOLD at each of the
four z-probes, reverse hold, and face hold. nm2ax12z 1-in 2-out split on
the same seed reported split HOLD at each of the four z-probes, reverse
hold, and face hold. nm2chiralz lexicographic unsigned `o1,o2` on the same
seed reported Orient `−1,+1,+1,+1`, reverse fail, and face hold.
nm2oridetz unique signed outgoing letters on the same seed reported Orient
fail at `A` and at `C`, reverse fail, and face fail. nm2orichz leftover-axis
on the same seed reported leftover-axis fail at `B` and at `D` from no
opposite pair, leftover reverse fail, and leftover face fail. nm2orionez
lex-one on the same seed reported reverse fail and face hold from
`e1<e2<e3` order independent of `m`. Leftover axis reported empty leftover
at each of four z-probes, leftover reverse fail, and leftover face fail.
nm2oricycl3z reported cyclic lex-largest Orient `−1,+1,+1,−1`, reverse
fail, and face fail at `t+1` alone. nm2oricyccz reported cyclic
lex-smallest reverse hold and face hold on the two-axis seed. The four
y-probes of this same seed reported cyclic lex-smallest Orient `+1` at `A`
from `m=−e_1` and Orient fail at `D` from split fail, so y-reverse HOLDs
and y-face fails. This note is not those displays: it reports cyclic
next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out
frame of `M` and `O` at `τ1=t+1` versus `τ2=t+2` on the three-axis opposite
seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=1`,
`Orient=+1,+1,−1,−1` at both cuts, reverse hold at both cuts, face hold
at both cuts, and composition hold. Cover and split do not score
handedness.

**Gate disposition:** PASS for the cyclic-lex-smallest `t+1` versus `t+2`
reverse/face reports and displayed composition above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals leftover-empty fail,” “the predicate equals leftover
of `M` alone,” “the predicate equals leftover of `O` alone,” “the
predicate equals exist-opposite HOLD,” “the predicate equals opposite-pair
presence in `O`,” “the predicate equals nm2chiralz lexicographic unsigned
`o1,o2` HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orichz leftover-axis HOLD,” “the predicate equals
nm2orionez lex-one HOLD,” “the predicate equals cyclic lex-largest HOLD,”
“the predicate equals nmcover axis-cover HOLD,” “the predicate equals
nm2axz axis-cover HOLD,” “the predicate equals nm2ax12z 1-in 2-out split
HOLD,” “the predicate equals nm2oricyccz two-axis `t+1`,” “the predicate
equals nm2oricycl3z lex-largest fail/fail,” “the predicate
equals nm2simt2z `M` and `O` freeze,” “the predicate equals the 1-axis
opposite two-site seed,” “the predicate equals nmunopp union,” “bits are
Admissibility,” “split fail is UNDEFINED,” “empty `O_i` is UNDEFINED,”
or “composition of Orient fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
`t+2`, reports the unique signed incoming letter, the axis index `i` of
`m`, and the cyclic next/prev lex-smallest outgoing letters, reports the
integer determinant and its sign at both cuts, lists new records in
`B_3(0)` between `t` and `t+1` and between `t+1` and `t+2` that meet a
probe's six-neighbors, and checks Theorems 1--3. It also checks that
Orient is `+1,+1,−1,−1` at `A,B,C,D` at both cuts, that reverse HOLDs at
both cuts while leftover reverse fails and lexicographic reverse fails,
that face HOLDs at both cuts while leftover-axis face fails because `D`
has no opposite pair, that composition HOLDs, that split fail is Orient
fail not `UNDEFINED`, that empty `O_next` or empty `O_prev` is Orient fail
not `UNDEFINED`, that the 1-axis opposite two-site seed is a different
member with Orient fail at `C`, that leftover-empty fail is a different
predicate, that leftover of `M` alone and leftover of `O` alone are
different objects, that mixed sets remain sets, that unique-letter Orient
is `UNDEFINED` at mixed `O`, that cyclic lex-largest reports reverse fail
and face fail, that unique signed reverse fails while this reverse HOLDs,
that leftover-axis reverse fails while this reverse HOLDs, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that the second pair and the third
pair are new seeds not formed children, that the y-probes and x-probes of
this seed are not this letter, that `τ=t` is not scored, and that the
display is not the two-tick lock-count clock composition. No runner cache
is written.
