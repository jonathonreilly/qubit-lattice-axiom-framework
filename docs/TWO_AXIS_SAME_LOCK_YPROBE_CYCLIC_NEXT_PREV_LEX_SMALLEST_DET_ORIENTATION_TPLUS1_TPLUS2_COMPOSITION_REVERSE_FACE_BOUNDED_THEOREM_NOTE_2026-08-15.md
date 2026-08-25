---
claim_id: two_axis_same_lock_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic lex-smallest orientation at t+1 versus t+2 on the four y-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Cyclic Lex-Smallest Orientation Freeze t+1 Versus t+2 Reverse And Face On Four Y-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-smallest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ1=t+1` and `τ2=t+2`, reverse/face from that sign
at each cut, and composition of Orient, on the four y-probes of the
two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same process and y-probes
as nm2sly. Orient as nm2oricyccz at each cut. `M`, `O`, split as nm2sl12.
Cyclic `i`, `e_next`, `e_prev` as nm2oricyclz. Let `t(q)` be the formation
tick of probe `q`. Cuts are local: `τ1=t+1`, `τ2=t+2`. There is no global
T. Do not score τ=t. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set
of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
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
likewise. `Orient(q,τ)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. Reverse HOLDs if and only if `Orient(A)=Orient(B)` both
`±1` at that cut. Face HOLDs if and only if `Orient(C)=Orient(D)` both
`±1` at that cut. Composition HOLDs if and only if `Orient` at `τ1` equals
`Orient` at `τ2` at `A,B,C,D`. Cover and split do not score handedness.
This is not leftover of nm2oricyccz cyclic lex-smallest at `t+1` alone.
This is not leftover of nm2simt2z simultaneous `M` and `O` freeze. This is
not leftover of nm2oricyclz lex-largest cyclic next/prev. This is not
leftover of nm2oricyclslz cyclic lex-largest on this same-lock seed. This
is not leftover of nm2orionez lex-one signed outgoing letters. This is not
leftover of nm2chiralz lexicographic unsigned `o1,o2` orientation. This is
not leftover of nm2oridetz unique signed outgoing letters. This is not
leftover of nm2orichz opposite-pair leftover-axis orientation. This is not
leftover of nm2slz axis-cover. This is not leftover of nm2axz axis-cover.
This is not leftover of nm2ax12z 1-in 2-out split. This is not leftover of
leftover-of-`M` alone. This is not leftover of leftover-of-`O` alone. This
is not leftover-empty fail of leftover axis. This is not leftover of
nmunopp union. This is not leftover of nmt2opp `M` frozen at `t`. This is
not leftover of nmot2opp two-tick composition. This is not leftover of
nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188
fail/fail. This is not leftover of the 1-axis same-lock two-site seed.
This is not leftover of the two-axis opposite seed. Neither pair is
opposite. The second pair is a new seed, not a formed child. Uniqueness is
not required. Mixed remains a set. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+1` and `τ2=t+2`. Axis is the unsigned lattice direction of a signed
lock. Cover is the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)`
and `Axis(O)`. Split is cover together with `|Axis(M)|=1`. The cyclic
next/prev lex-smallest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m`, cyclic axes
of `Axis(M)`, and the lex-smallest signed outgoing letter on each of those
cyclic slots under `+e < −e`. Reverse and face are scored on equal `±1`
signs at the paired probes at each cut. Composition is equality of those
four Orient reports across the two cuts. Named signs `{+,−}` of locks are
a coarser readout and are not used as the object. A singleton unique
outgoing lock letter is a different readout and is not used as the object.
Unsigned axis units of `Axis(O)` are a different readout and are not used.
Unique signed letters requiring `|O_i|=1` are a different readout and are
not used. Axis-order lex-one `(o_j,o_k)` is a different readout and is not
used. Lex-largest cyclic next/prev is a different readout and is not used.
Opposite-pair leftover-axis orientation is a different readout and is not
used. Existential opposite of signed locks is a different readout and is
not used. Axis-cover without the frame sign is a different readout and is
not used. 1-in 2-out split without the frame sign is a different readout
and is not used. Simultaneous `M` and `O` freeze is a different readout
and is not used. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 on the four y-probes of the two-axis same-lock seed, Orient −1,+1,+1,fail at A,B,C,D at each cut, reverse fail and face fail at each cut, composition hold; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display cyclic lex-smallest orientation freeze t+1 versus t+2 reverse/face composition on the four y-probes of the two-axis same-lock seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 displayed; do not write Orient into Admissibility, do not reduce to nm2ocyccsly t+1 alone, do not reduce to nm2oricyccz t+1 alone, do not reduce to nm2simt2z M-and-O freeze, do not reduce to lex-largest cyclic next/prev, do not reduce to nm2oricyclslz same-lock lex-largest, do not reduce to lex-one signed axis-order, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to opposite-pair leftover-axis, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 on the four y-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose
cyclic next/prev lex-smallest outgoing determinant orientation of `M`
and `O` at `τ1` and at `τ2` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the first same-lock pair. Same process and
y-probes as nm2sly.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. `(0,0,1)` locks `+e_2` and
`(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed
child of the first pair, and neither pair is opposite. This seed is not
the 1-axis same-lock two-site seed `{0,(0,1,0)}` with `+e_1/+e_1` alone.
This seed is not the two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
x-axis same-lock seed `{0,(1,0,0)}` with `+e_2/+e_2`. This seed is not the
z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`. This seed is not the
y-symmetric three-site seed that also records `(0,-1,0)` at tick 0.

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

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T.
Do not score τ=t.

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
e_next = e_{i+1} with 3+1→1.
e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}.
O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e.
o_next is the lex-smallest vector in O_next (hence +e if both signs).
o_prev is the lex-smallest vector in O_prev.
Orient(q,τ) = sign of the integer determinant of columns (m, o_next, o_prev).
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
HOLD required: 2-in 1-out is Orient fail, not UNDEFINED. Lex-largest on
the same cyclic slots is a different readout and is not used. Axis-order
lex-one `(o_j,o_k)` is a different readout and is not used.

Reverse oriented frame at a cut holds if and only if `Orient(A)=Orient(B)`
and both signs are `±1`. Face oriented frame at a cut holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Composition holds if and only if `Orient(q,τ1)=Orient(q,τ2)` at each of
`A,B,C,D`. Either side `UNDEFINED` is `UNDEFINED`. Else if the four signs
agree across the two cuts, composition HOLDs. Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse HOLDs at `A` and at `B` without
reporting `Orient=−1,+1,+1,fail`. Identifying split reverse with this
reverse is refused: split reverse HOLDs and split face fails without
cyclic next/prev columns. Identifying leftover-empty fail with this
reverse is refused: leftover-empty fail scores empty leftover as reverse
fail and face fail, matching these bits from empty leftover at `A,B,C`
and `{e_2}` at `D`; on unique signed `O={+e_1,+e_3}` leftover is empty
while Orient is `+1`. Identifying lexicographic unsigned `o1,o2` with
this reverse is refused: unsigned reverse HOLDs with `+1,+1` while this
reverse fails with `−1,+1`. Identifying unique signed `|O_i|=1` with this
reverse is refused: unique signed reverse fails because unique signed at
`B` fails while cyclic Orient at `B` is `+1`. Identifying opposite-pair
leftover-axis orientation with this reverse is refused: leftover-axis
reverse fails from no opposite pair in `O(A)`. Identifying nm2orionez
lex-one axis-order with this reverse is refused: lex-one reverse fails
matching these bits, but at `C` lex-one is `−1` while cyclic is `+1`.
Identifying nm2oricyclz lex-largest cyclic next/prev with this reverse is
refused: opposite-seed lex-largest reverse HOLDs. Identifying
nm2oricyclslz lex-largest on this same-lock seed with this reverse is
refused: lex-largest reverse HOLDs from equal `−1` at these y-probes.
Identifying nm2oricyccz opposite-seed reverse hold and face hold with
this reverse is refused: nm2oricyccz has split HOLD at z-probe `A` and
`Orient(A)=+1`. Identifying nm2ocyccsly `t+1` alone with this freeze is
refused: that letter has no `t+2` cut. Identifying a named sign of those
locks with reverse or face is refused: named-sign lettering lost the
axis.

## Theorem 1 — ticks, `M`, `O`, and Orient at `τ1` and `τ2`

On this process the four y-probes form. Compare to leftover axis: leftover
of the union is empty at `A`,`B`,`C` and `{e_2}` at `D`, leftover reverse
fail and leftover face fail. Compare to nm2sly cover: cover HOLDs at
`A`,`B`,`C` and fails at `D`, so cover reverse HOLDs and cover face fails.
Compare to nm2oricyccz cyclic lex-smallest on the two-axis opposite
z-probes: that member has split HOLD at `A`, `Orient(A)=+1`, reverse HOLDs
from equal `+1` signs, and face HOLDs. Compare to nm2oricyccy cyclic
lex-smallest on the two-axis opposite y-probes: reverse HOLDs from equal
`+1` signs and face fails. Compare to nm2oricyccslz cyclic lex-smallest on
the same-lock z-probes: reverse fails and face HOLDs with signs
`fail,+1,−1,−1`. Compare to nm2oricyclslz lex-largest on this same-lock
member: reverse HOLDs from equal `−1` signs at these y-probes. Compare to
nm2orionez lex-one on this same-lock member: reverse fails from `−1,+1`
and face fails. Compare to nm2chiralz lexicographic unsigned `o1,o2`
orientation: unsigned reverse HOLDs with `+1,+1`. Compare to nm2oridetz
unique signed outgoing letters: unique signed reverse fails because
`|O_i|≠1` at `B`. Compare to nm2orichz opposite-pair leftover-axis
orientation: reverse fails from no opposite pair in `O(A)`. Compare to
nm2ocyccsly: that letter is the `t+1` cut alone on these y-probes. This
display reads the cyclic next/prev lex-smallest outgoing determinant of
those same timed sets at both cuts:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ1) = {+e_1}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_2}
M(D, τ1) = {−e_3}
O(A, τ1) = {+e_2, −e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ1) = {+e_1}
split(A, τ1) = hold
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = fail
m(A, τ1) = +e_1
i(A, τ1) = 1
o_next(A, τ1) = +e_2
o_prev(A, τ1) = −e_3
det(A, τ1) = -1
Orient(A, τ1) = −1
m(B, τ1) = +e_1
i(B, τ1) = 1
o_next(B, τ1) = +e_2
o_prev(B, τ1) = +e_3
det(B, τ1) = 1
Orient(B, τ1) = +1
m(C, τ1) = +e_2
i(C, τ1) = 2
o_next(C, τ1) = +e_3
o_prev(C, τ1) = +e_1
det(C, τ1) = 1
Orient(C, τ1) = +1
m(D, τ1) = −e_3
i(D, τ1) = 3
o_next(D, τ1) = fail
o_prev(D, τ1) = fail
det(D, τ1) = fail
Orient(D, τ1) = fail
M(A, τ2) = {+e_1}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_2}
M(D, τ2) = {−e_3}
O(A, τ2) = {+e_2, −e_3}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ2) = {+e_1}
Orient(A, τ2) = −1
Orient(B, τ2) = +1
Orient(C, τ2) = +1
Orient(D, τ2) = fail
```

`A` is a seed at tick 0 with seed letter `+e_1`. The partner of that pair,
the origin, is also a seed at tick 0 with seed letter `+e_1`. Mixed remains
a set: `O(B,τ1)` has three outgoing steps and `O(C,τ1)` has four outgoing
steps. Unique outgoing letters would assign `UNDEFINED` at mixed `O(B)`
and at mixed `O(A)` (two letters). Unique signed `|O_i|=1` HOLDs at `A`
because each cyclic axis carries one sign, and fails at `B` and at `C`
from opposite pairs. At `D`, unique `m=−e_3` still gives `i=3`, but
`O_prev` on `e_2` is empty, so the cyclic pair fails and Orient fails, not
`UNDEFINED`. Split HOLD is required: split fails at `D` from incomplete
cover. Cover and split HOLD at `A`,`B`,`C` and fail at `D`; they do not
score that cyclic Orient at `A` is `−1` and at `B` is `+1`. Unsigned
axis-order 2-plane at `A` is `(e_2,e_3)` and lexicographic Orient at `A`
is `+1`, while cyclic Orient at `A` is `−1`. Lex-one signed axis-order
pair at `A` is `(+e_2,−e_3)` with Orient `−1`, matching cyclic
`(o_next,o_prev)` at `A`; at `C` lex-one is `(+e_1,+e_3)` with Orient `−1`
while cyclic is `(+e_3,+e_1)` with Orient `+1`. Lex-largest cyclic pair at
`B` is `(+e_2,−e_3)` with Orient `−1`, while this pair is `(+e_2,+e_3)`
with Orient `+1`. Opposite-pair leftover-axis at `A` fails from no opposite
pair in `O`. At `t`, `O` is empty at each of the four y-probes. O is not M.

On the 1-axis same-lock two-site seed, `A=(0,1,0)` is still a seed at tick
0 locking `+e_1`, but `O(A)` includes both `±e_3`, so cyclic Orient at `A`
is `+1`, `t(B)=2`, and `D` is 2-in 1-out, so split fails at `D` and Orient
at `D` is fail, not UNDEFINED. That 1-axis reverse HOLDs from equal `+1`
signs. Here the second pair `(0,0,1)` and `(0,1,1)` are seeds of a second
same-lock pair on a second axis, `O(A)={+e_2,−e_3}` has no `+e_3`, and
cyclic Orient at `A` is `−1`. On the z-probes of this same seed, split
fails at `A` from overlapping `e_2`, cyclic Orient at that z-probe is
fail, z-reverse fails, and z-face HOLDs; this y-probe reverse fails and
this y-face fails. Lex-largest y-reverse HOLDs (`−1,−1`).

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. The partner seed of
`A` is already recorded at tick 0, so it is not among those new records.
The `t+2` neighbors of `A` include `D=(1,1,0)` with earliest incoming
`−e_3`, so `+e_1` does not enter `O(A,τ2)`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
new 6-NN of A at t(A)+2: (1, 1, 0), (-1, 1, 0)
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
```

`M` is frozen from `t` to `t+1` and from `t+1` to `t+2`. At `t`, `O` is
empty at `A`, at `B`, at `C`, and at `D`; split fails at each probe, and
Orient is fail, not UNDEFINED. Do not score `τ=t`.

## Theorem 2 — reverse and face from oriented frame at `τ1` and `τ2`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. At `τ1`, `Orient(A)=−1` and `Orient(B)=+1`. Reverse fails. At
`τ2`, `Orient(A)=−1` and `Orient(B)=+1`. Reverse fails. This is HOLD
iff equal `±1` signs, not leftover of nm2chiralz lexicographic unsigned
`o1,o2`, not leftover of nm2oridetz unique signed outgoing letters, not
leftover of nm2orichz opposite-pair leftover-axis, not leftover of
nm2orionez lex-one, not leftover of nm2oricyclz lex-largest, not leftover
of nm2oricyclslz lex-largest on this seed, not leftover of nm2oricyccz
opposite-seed reverse hold, not leftover of nm2ocyccsly `t+1` alone, not
leftover of nm2sly axis-cover, not leftover of nm2axz axis-cover, not
leftover of nm2ax12z 1-in 2-out split, not leftover-empty fail, and not
exist-opposite.

Reverse oriented frame at τ1: fail
Reverse oriented frame at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Lexicographic unsigned reverse HOLDs because unsigned Orient at `A` is
`+1` and at `B` is `+1`. Unique signed reverse fails because unique signed
Orient at `B` is fail. Opposite-pair leftover-axis reverse fails because
that Orient at `A` is fail. Lex-one signed reverse fails because those
signs are `−1,+1`. Lex-largest cyclic reverse on this seed HOLDs with
`−1,−1`. nm2oricyccz reverse HOLDs with `+1,+1`. Leftover-empty reverse
fails because leftover of the union is empty at `A` and at `B`. Leftover
of `M` reverse HOLDs because leftover of `M` at `A` is `{e_2, e_3}` and at
`B` is `{e_2, e_3}`: nonempty and equal. Leftover of `O` reverse HOLDs
because leftover of `O` at `A` is `{e_1}` and at `B` is `{e_1}`.
Exist-opposite reverse of signed `M` fails. Exist-opposite reverse of
signed `O` holds. Presence of an opposite pair in `O` fails at `A` and
HOLDs at `B`. Those leftovers are not this display.

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
At `τ1`, `Orient(C)=+1` and `Orient(D)` is fail. Face fails. At `τ2`,
`Orient(C)=+1` and `Orient(D)` is fail. Face fails.

Face oriented frame at τ1: fail
Face oriented frame at τ2: fail

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Cyclic lex-smallest oriented face fails because Orient
at `D` is fail, not a `±1` sign. Lex-one signed face fails because lex-one
Orient at `D` is fail. Lexicographic unsigned face fails because unsigned
Orient at `D` is fail. Unique signed face fails. Opposite-pair leftover-axis
face fails. Lex-largest cyclic face fails with `+1` at `C` and fail at `D`.
Cover and split do not score handedness. Presence of an opposite pair in
`O` HOLDs at `C` and fails at `D`. On the 1-axis same-lock two-site seed,
cover face HOLDs while split face fails at `D` from 2-in 1-out, and Orient
at `D` is fail, not UNDEFINED. This two-axis member is not leftover of
that 1-axis reverse hold. The four z-probes of this same seed give cyclic
Orient fail at `A` and `−1` at `C` and at `D`, so oriented z-face HOLDs
while this y-face fails. The four x-probes give oriented reverse fail and
oriented face fail; those columns are not these y-probe columns.
Leftover-empty face fails because leftover of the union is empty at `C`
and `{e_2}` at `D`. Leftover of `M` at `C` is `{e_1, e_3}` and leftover of
`M` at `D` is `{e_1, e_2}`: nonempty and unequal. Leftover of `O` at `C`
is `{e_2}` and leftover of `O` at `D` is `{e_2, e_3}`: nonempty and
unequal. Exist-opposite face of signed `M` fails. Exist-opposite face of
signed `O` HOLDs, while this face fails. Cyclic lex-smallest oriented face
fails at both cuts.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover reverse HOLDs from complementary axes at `A` and
at `B`. Cover fails at `D` and split fails at `D`. Orient at `D` is fail
because the cyclic prev side on `e_2` is empty, not because `D` is
unformed. Orient at `A` is `−1` from cyclic `(+e_2,−e_3)`.

Reverse fails at both cuts. Face fails at both cuts.

## Theorem 3 — composition of Orient at `τ1` versus `τ2`

Composition HOLDs if and only if `Orient` at `τ1` equals `Orient` at `τ2`
at `A,B,C,D`. `Orient(A,τ1)=Orient(A,τ2)=−1`,
`Orient(B,τ1)=Orient(B,τ2)=+1`, `Orient(C,τ1)=Orient(C,τ2)=+1`,
`Orient(D,τ1)=Orient(D,τ2)=fail`. Composition HOLDs.

Composition of Orient: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

The reverse-fail and face-fail cyclic lex-smallest orientation of this
same-lock member at `t+1` freezes at `t+2`: the four reports are
unchanged. That freeze is the present letter. It is not leftover of
nm2ocyccsly, which scores only one cut on these y-probes. It is not
leftover of nm2oricyccz, which scores only one cut on the opposite seed
with reverse HOLD. It is not leftover of nm2oricyclslz, which scores
lex-largest on this seed at `t+1` alone with reverse HOLD from equal
`−1`. It is not leftover of nm2simt2z, which scores equality of `M` and
of `O` rather than equality of Orient. On this member `M` and `O` also
freeze, so simultaneous freeze HOLDs as a leftover; the scored object
remains the four Orient reports. Bit-stability of reverse fail and face
fail is a leftover predicate: those bits can agree while a probe sign
flips, which composition of Orient would fail. Composition of Orient at
`τ=t` versus `τ=t+1` fails because Orient is fail at formation at every
probe and `−1` at `A` at `t+1`. Do not score `τ=t`.

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
- It does not replace Orient by nm2orionez lex-one axis-order letters.
- It does not replace Orient by nm2oricyclz lex-largest cyclic next/prev.
- It does not replace Orient by nm2oricyclslz lex-largest on this same-lock seed.
- It does not replace Orient by opposite-pair leftover-axis orientation.
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
- It does not reprint nm2orionez lex-one reverse fail face hold as this
  oriented display.
- It does not reprint nm2oricyclz lex-largest cyclic reverse hold face hold
  with `−1,−1,+1,+1` as this oriented display.
- It does not reprint nm2oricyclslz lex-largest reverse fail face hold with
  `fail,−1,+1,+1` as this oriented display.
- It does not reprint nm2ocyccsly cyclic lex-smallest orientation at `t+1`
  alone.
- It does not reprint nm2oricyccz cyclic lex-smallest orientation at `t+1`
  alone.
- It does not reprint nm2simt2z simultaneous `M` and `O` freeze as this
  Orient composition.
- It does not reprint the 1-axis same-lock two-site seed as this member.
- It does not reprint the two-axis opposite seed as this member.
- It does not score the z-probes or the x-probes as this letter.
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
two-axis same-lock seed process, cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1`
versus `t+2`, reverse/face at each cut, and composition of Orient are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ1` and at `τ2` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ1` and at `τ2` | Theorem 1; outgoing dual `{+e_2,−e_3}` at `A`, freeze |
| unique signed `m`, cyclic `i`, lex-smallest `(o_next,o_prev)` | Theorem 1; singleton `M`; cyclic pair defined at `A`,`B`,`C`; empty prev at `D` |
| integer `det(m,o_next,o_prev)` at both cuts | Theorem 1; `-1`, `1`, `1`, fail at each cut |
| Orient at `τ1` | Theorem 1; `−1`, `+1`, `+1`, fail |
| Orient at `τ2` | Theorem 1; `−1`, `+1`, `+1`, fail |
| reverse from oriented frame at `τ1` and at `τ2` | Theorem 2; `fail` at each cut |
| face from oriented frame at `τ1` and at `τ2` | Theorem 2; `fail` at each cut |
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
| leftover of nm2slz axis-cover | not this oriented display |
| leftover of nm2axz axis-cover HOLD | not this oriented display |
| leftover of nm2ax12z 1-in 2-out split HOLD | not this oriented display |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz opposite-pair leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one axis-order | not this oriented display |
| leftover of nm2oricyclz lex-largest cyclic next/prev | not this oriented display |
| leftover of nm2oricyclslz lex-largest on this seed | not this freeze letter |
| leftover of nm2ocyccsly `t+1` alone | not this freeze letter |
| leftover of nm2oricyccz `t+1` alone | not this freeze letter |
| leftover of nm2simt2z `M` and `O` freeze | not this Orient composition |
| leftover of opposite-pair presence in `O` | not this oriented display |
| z-probe or x-probe Orient on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis same-lock two-site seed | not this display |
| leftover of the two-axis opposite seed | not this display |
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
| V1 | It answers the first-display question: does the reverse-fail and face-fail cyclic lex-smallest orientation of nm2ocyccsly freeze from `t+1` to `t+2` on the four y-probes of the two-axis same-lock seed. |
| V2 | Current main has no landed cyclic-next-prev-lex-smallest-outgoing-determinant reverse/face composition of timed `M` and `O` at `t+1` versus `t+2` on these four y-probes of the two-axis same-lock seed. |
| V3 | Orient reports at two cuts, the reverse/face bits at each cut, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at two local cuts and reports that reverse fails from unequal `−1,+1` signs, face fails from Orient fail at `D`, and the four reports freeze, while cover reverse HOLDs, unsigned reverse HOLDs with `+1,+1`, leftover of `M` reverse HOLDs, exist-opposite reverse of `O` HOLDs, nm2oricyccy opposite y reverse HOLDs, nm2oricyccz opposite z reverse HOLDs, and nm2simt2z scores lock-set equality rather than Orient equality. |
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
nm2orionez lex-one, does not replace Orient by nm2oricyclz lex-largest,
does not replace Orient by nm2oricyclslz lex-largest on this seed, does
not replace Orient by nm2orichz opposite-pair leftover-axis, does
not replace Orient by nmcover axis-cover, does not replace Orient by
nm2slz axis-cover, does not replace Orient by nm2axz axis-cover, does not
replace Orient by nm2ax12z 1-in 2-out split, does not replace this freeze
by nm2ocyccsly `t+1` alone, does not replace this freeze by nm2oricyccz
`t+1` alone, does not replace Orient composition by nm2simt2z `M` and `O`
freeze, does not identify this display with the 1-axis same-lock two-site
seed, does not identify it with the two-axis opposite seed, and does not
identify it with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2ocyccsly `t+1` alone | reuse reverse fail and face fail at one cut | that letter has no `t+2` cut and no Orient composition | ATTEMPTED |
| nm2oricyccz `t+1` alone | reuse reverse hold and face hold at one cut | that letter has no `t+2` cut, no Orient composition, and reverse HOLDs on the opposite seed | ATTEMPTED |
| nm2oricyclslz lex-largest same-lock | reuse lex-largest reverse hold at `t+1` | lex-largest reverse HOLDs from equal `−1` at these y-probes; cyclic lex-smallest reverse fails from `−1,+1` | ATTEMPTED |
| nm2simt2z `M` and `O` freeze | score equality of lock sets | simultaneous freeze HOLDs here as leftover; composition of this letter is equality of Orient reports | ATTEMPTED |
| reverse/face bit-stability | score reverse and face bits equal across cuts | those bits can agree while a probe sign flips; composition of Orient would then fail | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse hold | unsigned reverse HOLDs with `+1,+1` while this reverse fails with `−1,+1` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed at `A` is `−1` matching cyclic, but unique signed at `B` fails while cyclic Orient at `B` is `+1` | ATTEMPTED |
| nm2orionez lex-one axis-order | reuse lex-one reverse fail | lex-one reverse fails matching these bits; at `C` lex-one is `−1` while cyclic is `+1` | ATTEMPTED |
| nm2oricyclz lex-largest cyclic next/prev | reuse lex-largest reverse hold and face hold | opposite-seed lex-largest reverse HOLDs with `−1,−1`; this reverse fails | ATTEMPTED |
| nm2orichz opposite-pair leftover-axis | reuse leftover-axis reverse and face | leftover-axis reverse fails from no opposite pair in `O(A)` | ATTEMPTED |
| nm2sly axis-cover | reuse cover reverse hold and cover face fail | cover reverse HOLDs while this reverse fails; cover does not report signed det | ATTEMPTED |
| nm2axz axis-cover | reuse opposite-seed cover reverse hold and cover face hold | nm2axz HOLDs reverse and face on opposite z-probes; this y-probe reverse fails | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse opposite-seed split reverse hold and split face hold | opposite split HOLDs reverse and face; here split reverse HOLDs while Orient reverse fails; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails and leftover face fails matching these bits from empty leftover at `A,B,C` and `{e_2}` at `D`; unique signed `O={+e_1,+e_3}` has empty leftover and Orient `+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` reverse HOLDs from equal `{e_2,e_3}` at `A` and at `B`; this reverse fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` reverse HOLDs from equal `{e_1}` at `A` and at `B`; this reverse fails | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` holds while Orient reverse fails; exist-opposite face of signed `O` holds while this face fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence fails at `A` and HOLDs at `B`; exist-opposite of `O` across probes HOLDs from `−e_3` at `A` and `+e_3` at `B` | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ1)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `−1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | unsigned reverse HOLDs with `+1,+1`; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` fails from incomplete cover, not from 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis same-lock two-site seed | reuse `t(B)=2`, `t(D)=3`, Orient `+1` at `A`, reverse hold | different seed; second pair is a new seed, not a formed child; here `t(B)=1`, `t(D)=2`, and Orient at `A` is `−1` | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe reverse fails and z-face HOLDs; this letter is the four y-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails from Orient fail at `A`; this letter is the four y-probes | ATTEMPTED |
| score at `τ=t` | compose Orient at formation versus `t+1` | leftover of nmot2opp; Orient is fail at `t` and `−1/+1/+1/fail` at `t+1`; Do not score `τ=t` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-smallest outgoing determinant orientation of own incoming and outgoing at `t+1` versus `t+2` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail at both cuts on the two-axis same-lock seed | ATTEMPTED |
| 1-axis same-lock two-site reuse | reuse `+e_1/+e_1` alone | different seed; this member is two disjoint same-lock pairs | ATTEMPTED |
| two-axis opposite seed | reuse `+e_1/−e_1` and `+e_2/−e_2` | different seed; neither pair is opposite; here `O(A)={+e_2,−e_3}` | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_2−e_3` while Orient at `A` is `−1` | ATTEMPTED |
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
missing identification of Orient with nm2orionez lex-one, missing
identification of Orient with nm2oricyclz lex-largest cyclic next/prev,
missing identification of Orient with nm2oricyclslz lex-largest on this seed,
missing identification of Orient with nm2orichz opposite-pair leftover-axis,
missing identification of Orient with nmcover axis-cover, missing
identification of Orient with nm2slz axis-cover, missing identification of
Orient with nm2axz axis-cover, missing identification of Orient with
nm2ax12z 1-in 2-out split, missing identification of this freeze
with nm2oricyccz `t+1` alone, missing identification of Orient composition
with nm2simt2z `M` and `O` freeze, missing identification of this seed with
the 1-axis same-lock two-site seed, missing identification of this seed with
the two-axis opposite seed, and missing Record identification of
Orient reverse are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ1=t+1`
and `τ2=t+2`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, unique signed `m` when
split HOLDs, cyclic `e_next` and `e_prev` of the axis of `m`, lex-smallest
signed outgoing letter on each cyclic slot under `+e < −e`, integer
determinant sign, empty `O_next` or empty `O_prev` as Orient fail not
`UNDEFINED`, split fail as Orient fail not `UNDEFINED`, four y-probes with
seed `A`, second pair as a new seed not a formed child, mixed remains a
set, and composition as equality of Orient at the two cuts are declared.
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
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports at `t+1` and `t+2`, reverse/face at each cut, composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, a later cut `t+3`, and a physical selector among 1-in
2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse fail and face fail are only leftover of
nm2ocyccsly at `t+1`; they are only leftover of nm2oricyccz cyclic
lex-smallest on opposite z; they are only leftover of nm2oricyclslz
lex-largest on this seed; they are only leftover of nm2orionez lex-one on
this seed; they are only leftover of nm2sly cover; nm2chiralz unsigned
`o1,o2` already answers mixed `O`; unique signed `|O_i|=1` already answers
mixed `O`; cover reverse and split reverse already answer the three-axis
occupation; leftover of `M` alone already answers reverse; leftover of
`O` alone already answers reverse; exist-opposite of signed `O` already
answers reverse; opposite-pair leftover-axis already answers handedness;
mixed #7188 already reported fail/fail; the second pair is only the formed
child `(0,0,1)` of the 1-axis seed; unique outgoing letters should be
required; unsigned incoming axis already gives the same signs because each
`M` letter is the positive unit; because `M` and `O` freeze, composition
is nm2simt2z; because reverse fail and face fail at both cuts, composition
is only bit-stability; and nm2ocyccsly already answered reverse-and-face
orientation.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Orient reverse fails because `Orient(A)=−1` and
`Orient(B)=+1`. Orient face fails because `Orient(D)` is fail. Cover and
split HOLD reverse and fail face on this member and do not score that
signed pair at `A` and at `B`. nm2ocyccsly scores only `τ=t+1` on these
y-probes. nm2oricyccz on the opposite z-probes has `Orient(A)=+1` with
split HOLD and reverse HOLDs; here `Orient(A)=−1` and reverse fails.
nm2oricyclslz lex-largest reverse HOLDs from equal `−1` at these y-probes;
this reverse fails. nm2orionez lex-one reverse fails matching these bits,
but at `C` lex-one is `−1` while cyclic is `+1`. nm2sly cover reverse HOLDs
and does not report `−1` at `A`. Lexicographic unsigned `o1,o2` reverse
HOLDs with `+1,+1`; unsigned Orient at `A` is `+1` while cyclic Orient at
`A` is `−1`. Unique signed `|O_i|=1` reverse fails because unique signed
at `B` fails while cyclic Orient at `B` is `+1`. Opposite-pair leftover-axis
reverse fails from no opposite pair in `O(A)`. Presence of an opposite pair
in `O` fails at `A`. Leftover of `M` alone at `A` is `{e_2,e_3}` and at
`B` is `{e_2,e_3}`: nonempty equal, so leftover-of-`M` reverse HOLDs while
this reverse fails. Leftover of `O` alone at `A` is `{e_1}` and at `B` is
`{e_1}`, so leftover-of-`O` reverse HOLDs. Exist-opposite reverse of signed
`O` holds while Orient reverse fails. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(A)` and mixed `O(B)`; this Orient at `A` is `−1`
and at `B` is `+1`. On unique signed `O={+e_1,+e_3}` leftover is empty
while Orient is `+1`, so leftover-empty fail is not this predicate. Mixed
#7188 is a different z-symmetric process with mixed `M`. The second pair
is a new seed, not a formed child: `(0,0,1)` is recorded at tick 0 with
lock `+e_2`, whereas the 1-axis child forms at tick 1 with lock `+e_3`.
nm2oricyccz scores only `τ=t+1` on the opposite seed. nm2simt2z scores
equality of `M` and of `O`. Reverse/face bit-stability can HOLD while a
probe sign flips. Reverse oriented frame is HOLD iff equal `±1` signs at
`A` and at `B` at that cut, not leftover of nm2ocyccsly `t+1` alone and
not leftover of nm2sly axis-cover. Composition of Orient: hold.

### N8 — cross-cycle echo

nm2sly axis-cover on this two-axis same-lock y-probes reported cover HOLD
at `A`,`B`,`C`, cover fail at `D`, reverse hold, and face fail. nm2ocyccsly
cyclic lex-smallest at `t+1` on these y-probes reported Orient `−1,+1,+1`,
fail, reverse fail, and face fail. nm2oricyccz cyclic lex-smallest on the
two-axis opposite seed reported `Orient(A)=+1` with split HOLD, reverse
hold, and face hold at `t+1` alone. nm2oricyclslz lex-largest cyclic on
these y-probes reported reverse hold from equal `−1`. nm2orionez lex-one
reported reverse fail from `−1,+1`. nm2axz cover on the opposite seed
reported cover HOLD at each of the four z-probes, reverse hold, and face
hold. nm2ax12z 1-in 2-out split on the opposite seed reported split HOLD
at each of the four z-probes, reverse hold, and face hold. Leftover axis
reported empty leftover at `A,B,C` and `{e_2}` at `D`, leftover reverse
fail, and leftover face fail. The four z-probes of this same seed reported
cyclic Orient fail at `A` and `−1` at `C` and at `D`, so z-reverse fails
and z-face HOLDs. This note is not those displays: it reports cyclic
next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out
frame of `M` and `O` at `τ1=t+1` versus `τ2=t+2` on the two-axis
same-lock seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=2`, `Orient`
`−1`,`+1`,`+1`,fail at both cuts, reverse fail at both cuts, face fail at
both cuts, and composition hold. Cover and split do not score handedness.

**Gate disposition:** PASS for the cyclic-next-prev-lex-smallest-outgoing-determinant `t+1` versus `t+2`
reverse/face reports and displayed composition above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals leftover-empty fail,” “the predicate equals leftover
of `M` alone,” “the predicate equals leftover of `O` alone,” “the
predicate equals exist-opposite HOLD,” “the predicate equals opposite-pair
presence in `O`,” “the predicate equals nm2chiralz lexicographic unsigned
`o1,o2` HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orionez lex-one HOLD,” “the predicate equals
nm2oricyclz lex-largest HOLD,” “the predicate equals nm2oricyclslz
lex-largest HOLD,” “the predicate equals nm2orichz opposite-pair
leftover-axis HOLD,” “the predicate equals nmcover axis-cover HOLD,” “the
predicate equals nm2sly axis-cover HOLD,” “the predicate equals nm2axz
axis-cover HOLD,” “the predicate equals nm2ax12z 1-in 2-out split HOLD,”
“the predicate equals nm2ocyccsly `t+1` alone,” “the predicate equals
nm2oricyccz `t+1` alone,” “the predicate equals nm2simt2z `M` and `O`
freeze,” “the predicate equals the 1-axis same-lock two-site seed,” “the
predicate equals the two-axis opposite seed,” “the predicate equals
nmunopp union,” “bits are Admissibility,” “split fail is UNDEFINED,”
“empty `O_next` or empty `O_prev` is UNDEFINED,” “reverse oriented frame
holds,” “face oriented frame holds,” or “composition of Orient fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
`t+2`, reports split of the pair, reports the unique signed incoming letter,
the cyclic axis index, and the lex-smallest `o_next` and `o_prev`, reports
the integer determinant and its sign at both cuts, lists new records in
`B_3(0)` between `t` and `t+1` and between `t+1` and `t+2` that meet a
probe's six-neighbors, and checks Theorems 1--3. It also checks that Orient
is `−1`,`+1`,`+1`,fail at `A,B,C,D` at both cuts, that reverse fails at
both cuts and face fails at both cuts while leftover-empty reverse fails,
that composition HOLDs, that split fail is Orient fail not `UNDEFINED`,
that empty `O_next` or empty `O_prev` is Orient fail not `UNDEFINED`, that
nm2oricyccz opposite-seed z-probe Orient at `A` is `+1` while this Orient
at `A` is `−1` and that opposite reverse HOLDs while this reverse fails,
that nm2oricyccy opposite y-probe reverse HOLDs while this reverse fails,
that the 1-axis same-lock two-site seed is a different member with Orient
`+1` at `A` and reverse HOLD, that leftover-empty fail is a different
predicate, that leftover of `M` alone and leftover of `O` alone HOLD
reverse while this reverse fails, that mixed sets remain sets, that
unique-letter Orient is `UNDEFINED` at mixed `O`, that lexicographic
unsigned Orient at `A` is `+1` while this Orient at `A` is `−1`, that
lex-one at `C` is `−1` while this Orient at `C` is `+1`, that unique
signed at `B` fails while this Orient at `B` is `+1`, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that the second pair is a new seed not
a formed child, that neither pair is opposite, that the z-probes and
x-probes of this seed are not this letter, that `τ=t` is not scored, and
that the display is not the two-tick lock-count clock composition. No
runner cache is written.
