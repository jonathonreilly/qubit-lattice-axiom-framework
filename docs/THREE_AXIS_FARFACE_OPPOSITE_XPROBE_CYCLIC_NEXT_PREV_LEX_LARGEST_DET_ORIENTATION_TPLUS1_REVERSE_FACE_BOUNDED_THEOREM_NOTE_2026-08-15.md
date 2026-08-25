---
claim_id: three_axis_farface_opposite_xprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic lex-largest orientation of the 1-in 2-out frame at t+1 on the four x-probes of the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_xprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Cyclic Next/Prev Lex-Largest Outgoing Determinant Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four X-Probes Of The Three-Axis Far-Face Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-largest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that sign, on the
four x-probes of the three-axis far-face opposite seed in `B_3(0)={n:n·n<=9}`.
x-probes as nm2axx. Orient as nm2oricyclz: cyclic next/prev of `Axis(M)`
with lex-largest signed letter in each outgoing slot. Let `t(q)` be the formation tick of probe `q`. Let
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
with `1−1→3`. `O_next = O ∩ {±e_next}`. `O_prev = O ∩ {±e_prev}`. If
either slot is empty, Orient fails, not `UNDEFINED`. Order `+e < −e`.
`o_next` is the lex-largest vector in `O_next` (hence `−e` if both signs).
`o_prev` likewise. `Orient(q)` is the sign of the integer determinant of
the 3×3 matrix with columns `m`, `o_next`, `o_prev`. If split fails,
Orient fails, not `UNDEFINED`. Reverse HOLDs if and only if
`Orient(A)=Orient(B)` both `±1`. Face HOLDs if and only if
`Orient(C)=Orient(D)` both `±1`. Cover and split do not score handedness.
This is not leftover of nm2axx axis-cover. This is not leftover of nm2ax12x
1-in 2-out split. This is not leftover of lexicographic `o1,o2`. This is
not leftover of cyclic lex-smallest. This is not leftover of nm2orionex
lex-one signed outgoing. This is not leftover of nm2orilefx signed leftover
axis. This is not leftover of nm2orichx unsigned leftover `+ℓ`. This is
not leftover of leftover-of-`M` alone. This is not leftover of leftover-of-`O`
alone. This is not leftover-empty fail of leftover axis. This is not leftover
of nmunopp union. This is not leftover of nmt2opp `M` frozen at `t`. This is
not leftover of nmot2opp two-tick composition. This is not leftover of
nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188
fail/fail. This is not leftover of the 1-axis opposite two-site seed.
This is not leftover of the same-lock two-site seed. This is not leftover
of the two-axis opposite seed. This is not leftover of nm2oricyclz
two-axis z-probe reverse hold. This is not leftover of nm2oricycl3fz far-face
z-probe reverse hold and face hold. This is not leftover of the three-axis
opposite seed whose third pair sits at `(2,0,0)/(2,1,0)`. This is not the
two-tick lock-count clock composition. The third pair is a new seed, not a
formed child, and sits on the `−z` face opposite the z-probes. Uniqueness
is not required. Mixed remains a set.
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_xprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_xprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev lex-largest
oriented frame is the integer sign of `det(m,o_next,o_prev)` with unique
signed incoming letter `m`, cyclic next and previous axes of `Axis(M)`, and
the lex-largest signed vector of `O` on each of those axes under `+e < −e`.
Reverse and face are scored on equal `±1` signs at the paired probes.
Named signs `{+,−}` of locks are a coarser readout and are not used as the
object. A singleton unique outgoing lock letter is a different readout and
is not used as the object. Lex-smallest on the same cyclic slots is a
different readout and is not used. Lexicographic unsigned outgoing 2-plane
`(o1,o2)` in axis order is a different readout and is not used. Lex-one
signed outgoing letters per `Axis(O)` in axis order, not cyclic from
`Axis(M)`, are a different readout and are not used. Signed leftover-axis
`det(m,e_pair,o_ℓ)` is a different readout and is not used. Unsigned leftover
unit `+ℓ` is a different readout and is not used. Existential opposite of
signed locks is a different readout and is not used. Axis-cover without the
frame sign is a different readout and is not used. 1-in 2-out split without
the frame sign is a different readout and is not used. Leftover-empty fail of
unsigned leftover axis sets is a different readout and is not used. A `Z^3`
sum of those locks is a different readout and is not used. Occupancy of sites
is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the three-axis far-face opposite seed, Orient fail,-1,+1,fail, reverse fail and face fail from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_xprobe_cyclic_next_prev_lex_largest_det_orientation_tplus1_reverse_face
target_blocker_text: "display cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame reverse/face on the four x-probes of the three-axis far-face opposite seed, not cyclic lex-smallest, not lex-one, not leftover-axis, not cover, not split, not two-axis"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to cyclic lex-smallest, do not reduce to lexicographic o1,o2, do not reduce to nm2orionex lex-one, do not reduce to signed leftover axis, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by presence of an opposite pair in O, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, do not reduce to the two-axis opposite seed, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic next/prev lex-largest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four x-probes of the three-axis far-face opposite seed and reverse/face from that sign; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose
cyclic next/prev lex-largest outgoing determinant orientation of `M` and `O`
is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. `C` is a formed child, not a seed. x-probes as nm2axx. On the
near three-axis opposite member, `C` is the third-pair seed `(2,0,0)`. Here
the third pair sits on the `−z` face, so `(2,0,0)` forms at tick 3.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(0,0,−1)` locks `+e_3`. Site `(0,1,−1)`
locks `−e_3`. The second pair is a new seed, not a formed child of the
first pair. The third pair is a new seed, not a formed child, and sits on
the `−z` face opposite the z-probes: on the two-axis opposite seed those
sites form at tick 1 locking `−e_3`. This seed is not the two-axis opposite
seed of nm2oricyclz. This seed is not the three-axis opposite seed whose
third pair sits at `(2,0,0)/(2,1,0)`. This seed is not the 1-axis opposite
two-site seed `{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the
perp two-site seed `+e_1/+e_2`. This seed is not the same-lock two-site
seed `+e_1/+e_1`. This seed is not the z-symmetric three-site seed
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

## Named cyclic next/prev lex-largest 1-in 2-out frame of `M` and `O` at `τ=t+1`

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

Cyclic next/prev lex-largest oriented frame at the same cut:

```text
When split HOLDs, m is unique in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1 -> 1.
e_prev = e_{i-1} with 1-1 -> 3.
O_next = O intersect {±e_next}.
O_prev = O intersect {±e_prev}.
If either slot is empty, Orient fails, not UNDEFINED.
Order +e < −e.
o_next is the lex-largest vector in O_next (hence −e if both signs).
o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
If split fails, Orient fails, not UNDEFINED.
UNDEFINED if M or O is UNDEFINED.
```

Unique outgoing letters are not required. Mixed opposite signs occupy a
cyclic slot as a two-element set; lex-largest then selects `−e`. A vanishing
determinant is fail. Sign of a nonzero integer determinant is `+1` or `−1`.
Split HOLD required: 2-in 1-out is Orient fail, not UNDEFINED. An empty
cyclic slot is Orient fail, not UNDEFINED, and is not repaired by picking
lex-smallest `+e`. Lex-one signed letters in axis order `e1<e2<e3` of
`Axis(O)` are a different column order and a different sign choice.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse fails with this reverse because
cover fails at `A`, and cover does not report `Orient(B)=−1`. Identifying
split reverse with this reverse is refused on the same ground. Identifying
leftover-empty fail with this reverse is refused: leftover-empty fail
scores empty leftover as reverse fail, which matches this reverse bit,
but leftover of the union at `A` is `{e_2}` while Orient at `A` is fail
from mixed `M`. Identifying lexicographic `o1,o2` orientation with this
reverse is refused: lexicographic reverse fails with this reverse from
fail versus `+1`, but unsigned Orient at `B` is `+1` while this Orient at
`B` is `−1`, and unsigned face at `C` is `+1` matching this Orient at `C`
while lex-one and lex-smallest at `C` are `−1`. Identifying cyclic
lex-smallest with this letter is refused: lex-smallest Orient at `B` is
`+1` while this Orient at `B` is `−1`, and lex-smallest Orient at `C` is
`−1` while this Orient at `C` is `+1`. Identifying nm2orionex
lex-one signed outgoing with this Orient is refused: lex-one reverse fails
with this reverse, but lex-one Orient at `B` is `+1` and at `C` is `−1`
while this Orient is `−1` at `B` and `+1` at `C`. Identifying nm2orilefx
signed leftover axis with this Orient is refused: leftover Orient at `B`
and at `C` matches this Orient, but leftover-axis is a different column
order. Identifying nm2orichx unsigned leftover `+ℓ`
with this Orient is refused: unsigned leftover at `C` is `−1` while this
Orient at `C` is `+1`. Identifying leftover of `M` alone with this reverse is
refused: leftover-of-`M` reverse fails with this reverse, and leftover of
`M` does not report Orient fail versus `−1`.
Identifying presence of an opposite pair in `O`
with this reverse is refused: pair-presence reverse fails because `A` has
no opposite pair while `B` has `±e_3`, without reading Orient fail versus
`−1`. Identifying a named sign of those locks with reverse or face is
refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, `i`, `o_next`, `o_prev`, and Orient at `τ=t+1`

On this process the four x-probes form. Compare to leftover axis: leftover
of the union is `{e_2}` at `A` and at `D` and empty at `B` and at `C`,
leftover reverse fail and leftover face fail. Compare to nm2axx axis-cover
and nm2ax12x 1-in 2-out split: both fail reverse and fail face on this
member because cover and split fail at `A`. Compare to lexicographic
`o1,o2`: that readout scores Orient fail at `A` and `+1` at `B`, so
lexicographic reverse fails with this reverse, but unsigned Orient at `B`
is `+1` while this Orient at `B` is `−1`. Compare to cyclic lex-smallest
on the same slots: that readout scores Orient fail, `+1`, `−1`, fail,
reverse fail, and face fail, and lex-smallest at `B` is `+1` while this
Orient at `B` is `−1`, and lex-smallest at `C` is `−1` while this Orient
at `C` is `+1`. Compare to nm2orionex lex-one signed outgoing: lex-one at
`B` is `+1` and at `C` is `−1`, while this Orient is `−1` at `B` and `+1`
at `C`. Compare to nm2orilefx signed leftover axis: leftover Orient at
`B` is `−1` matching this Orient at `B`, leftover Orient at `C` is `+1`
matching this Orient at `C`, but leftover Orient at `A` is fail from no
opposite pair in `O` as this Orient at `A` is fail from mixed `M`. Compare
to the two-axis opposite x-probes: that member scores the same ticks
`t(A)=2`, `t(C)=3`, `t(D)=2` and the same reverse fail face fail, but
`M(A)={−e_3}` is a singleton while this `M(A)={+e_3,−e_3}` is mixed.
Compare to the near three-axis opposite x-probes whose third pair is
`(2,0,0)/(2,1,0)`: that letter scores `t(A)=1`, `t(C)=0`, Orient
`−1,+1,+1`, fail. Compare to the four z-probes of this same seed: that
letter scores Orient `−1,−1,+1,+1`, reverse hold, and face hold. Compare
to the four y-probes of this same seed: that letter scores `t(A)=0`,
Orient `+1,−1,−1`, fail, reverse fail, and face fail. This display reads
cyclic next/prev of `Axis(M)` with lex-largest signed `O` on each slot:

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ) = {+e_3, −e_3}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {+e_3, −e_3}
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
det(A) = fail
Orient(A) = fail
i(B) = 1
o_next(B) = +e_2
o_prev(B) = −e_3
det(B) = -1
Orient(B) = −1
i(C) = 1
o_next(C) = −e_2
o_prev(C) = −e_3
det(C) = 1
Orient(C) = +1
i(D) = fail
o_next(D) = fail
o_prev(D) = fail
det(D) = fail
Orient(D) = fail
```

`C` is a formed child at tick 3 locking `+e_1`, not a seed. `A` is a
formed child at tick 2 with mixed earliest incoming `{+e_3,−e_3}`. Mixed
remains a set: `M(A,τ)` has two incoming steps, `O(B,τ)` has three
outgoing steps, and `O(C,τ)` has three outgoing steps. Unique incoming
letters would assign `UNDEFINED` at mixed `M(A)`. Unique outgoing letters
would assign `UNDEFINED` at mixed `O(B)` and mixed `O(C)`. Here uniqueness
is not required. At `A`, split fails from cover fail: `Axis(M)={e_3}` and
`Axis(O)={e_1}` miss `e_2`, leftover of the union is `{e_2}`, and mixed
`M` has no unique `m`, so Orient fails, not `UNDEFINED`. At `B`, split
HOLDs, `i=1`, `O_next={+e_2}` and mixed `O_prev={±e_3}`; lex-largest
selects `o_prev=−e_3`, and `det(+e_1,+e_2,−e_3)=−1`. Lex-smallest and
lex-one on those same outgoing axes pick `+e_3` and score `+1`. At `C`,
split HOLDs, `i=1`, cyclic slots are `e_2` then `e_3`, singleton `{−e_2}`
and mixed `{±e_3}`, lex-largest selects `−e_2` and `−e_3`, and
`det(+e_1,−e_2,−e_3)=+1`. Lex-one in axis order of `Axis(O)` picks `−e_2`
then `+e_3` and scores `det(+e_1,−e_2,+e_3)=−1`. Lex-smallest on the same
cyclic slots also picks `+e_3` on `e_prev` and scores `−1`. At `D`, `M` is
mixed `{±e_3}` so unique `m` fails, cover fails from leftover `{e_2}`,
split fails, and Orient fails, not `UNDEFINED`. Cover and split fail
reverse on this member because they fail at `A`; they do not score that
Orient at `B` is `−1` and at `C` is `+1`. O is not M.

On the 1-axis opposite two-site seed, `A` forms at tick 3, `B` at tick 2,
`C` at tick 4, and `D` at tick 3, cover face HOLDs, split face fails,
cyclic lex-largest Orient at `A` is fail and at `B` is `−1` so reverse
fails, and Orient at `D` is fail, not UNDEFINED. That is leftover of the
first pair. On the two-axis opposite seed, `t(A)=2`, `t(C)=3`, `t(D)=2`,
and `M(A)={−e_3}`. On the near three-axis opposite seed, `(2,0,0)` and
`(2,1,0)` are seeds of a third opposite pair, `t(A)=1`, `t(C)=0`, and
`M(A)={−e_1}` because `A` forms from that third-pair seed. Here those
sites are formed children: `t(C)=3` and `M(C)={+e_1}`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(2,0,0)` is
not a seed: it forms at tick 3 and is a new 6-NN of `A`. Site `(2,1,0)`
forms at tick 3 and is a new 6-NN of `D`. Site `(0,0,−1)` is a seed, so it
is not a new 6-NN of any x-probe at these cuts:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `B`, and
`C`. At `D`, `O` at `t` is `{−e_1}` and grows to `{+e_1, −e_1}` at
`t+1`. Orient at `t` is fail, not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)` is fail and `Orient(B)=−1`. Reverse fails. This is HOLD
iff equal `±1` signs, not leftover of cyclic lex-smallest, not leftover of
nm2orionex lex-one signed outgoing, not leftover of lexicographic `o1,o2`,
not leftover of nm2orilefx signed leftover axis, not leftover of nm2axx
axis-cover, not leftover of nm2ax12x 1-in 2-out split, not leftover-empty
fail, not leftover of `M` alone, not the two-axis opposite x-probes, not
the near three-axis opposite x-probes, not the four z-probes of this seed,
not the four y-probes of this seed, and not exist-opposite.

Reverse oriented frame at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at `A`. Split reverse fails because split fails at
`A`. Cover and split do not score handedness. Lexicographic reverse fails
because lexicographic `Orient(A)` is fail and `Orient(B)=+1`. Cyclic
lex-smallest reverse fails because lex-smallest at `A` is fail and at `B`
is `+1`. Lex-one reverse fails because lex-one at `A` is fail and at `B`
is `+1`. Cyclic lex-largest reverse fails because Orient at `A` is fail
and at `B` is `−1`. On the two-axis opposite x-probes the same letter
fails reverse from Orient fail at `A` with singleton `M(A)={−e_3}` and
lex-largest at `B` selecting `−e_3`; this `M(A)` is mixed `{±e_3}`. Signed
leftover-axis reverse fails because leftover Orient at `A` is fail from no
opposite pair in `O`. Leftover-empty reverse fails because leftover of the
union is `{e_2}` at `A` and empty at `B`. Leftover of `M` reverse fails
because leftover of `M` at `A` is `{e_1, e_2}` and at `B` is `{e_2, e_3}`:
nonempty and unequal. Leftover of `O` reverse fails because leftover of
`O` at `A` is `{e_2, e_3}` and at `B` is `{e_1}`: nonempty and unequal.
Exist-opposite reverse of signed `M` fails. Exist-opposite reverse of
signed `O` fails. Presence of an opposite pair in `O` fails at `A` and
HOLDs at `B`, so pair-presence reverse fails with this reverse bit,
without reading fail versus `−1`. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=+1` and `Orient(D)` is fail. Face fails.

Face oriented frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Cyclic lex-largest oriented face fails because Orient
HOLDs at `C` from `det(+e_1,−e_2,−e_3)=+1` and fails at `D` from mixed
`M={±e_3}` so unique `m` fails and leftover of the union is `{e_2}`.
Cyclic lex-smallest face also fails, with Orient `−1` at `C`. Lex-one face
fails, with Orient `−1` at `C`. Pair face HOLDs while this face fails:
pair HOLDs at `C` and at `D` from mixed `±e_3` in `O(C)` and mixed `±e_1`
in `O(D)`. On the 1-axis opposite two-site seed, cover face HOLDs while
split face fails, Orient at `A` is fail, Orient at `B` is `−1`, Orient at
`C` is `+1`, and Orient at `D` is fail, not UNDEFINED. This far-face
member is not leftover of that 1-axis split face fail: here `t(C)=3`,
`t(D)=2`, and `M(D)` is mixed `{±e_3}`. On the two-axis opposite
x-probes, reverse fails, `t(A)=2`, and `t(C)=3`, with singleton
`M(A)={−e_3}`. The four z-probes of this same seed give cyclic
lex-largest Orient `−1,−1,+1,+1`, reverse hold, and face hold. The four
y-probes give Orient `+1,−1,−1`, fail, reverse fail, and face fail, with
`t(A)=0`. Those probe-direction readouts are not this x-probe display.
Leftover-empty face fails because leftover of the union is empty at `C`
and `{e_2}` at `D`. Leftover of `M` at `C` is `{e_2, e_3}` and leftover of
`M` at `D` is `{e_1, e_2}`: nonempty and unequal. Leftover of `O` at `C`
is `{e_1}` and leftover of `O` at `D` is `{e_2, e_3}`: nonempty and
unequal. Exist-opposite face of signed `M` fails. Exist-opposite face of
signed `O` fails. Unique signed face fails. Unsigned leftover face fails
because unsigned leftover at `C` is `−1` while this Orient at `C` is
`+1`. Lexicographic face fails. Lex-one oriented face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `A` and at `D`. Split fails at `A` and
at `D`. Pair fails at `A` and HOLDs at `D`. Orient at `A` is fail and
Orient at `D` is fail from mixed `M`, not from an empty cyclic slot.

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
- It does not replace Orient by cyclic lex-smallest on the same slots.
- It does not replace Orient by unsigned leftover unit `+ℓ`.
- It does not replace Orient by nm2orilefx signed leftover axis.
- It does not replace Orient by nm2orionex lex-one signed outgoing.
- It does not replace Orient by lexicographic `o1,o2` orientation.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
- It does not treat an empty cyclic slot as `UNDEFINED`.
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
- It does not reprint lexicographic `o1,o2` reverse fail face fail as this
  oriented display.
- It does not reprint cyclic lex-smallest reverse fail face fail as this
  oriented display.
- It does not reprint nm2orichx unsigned leftover `+ℓ` as this column order.
- It does not reprint nm2orilefx signed leftover axis reverse fail face
  fail as this oriented display.
- It does not reprint nm2orionex lex-one signed outgoing reverse fail face
  fail as this oriented display.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not reprint the two-axis opposite seed as this member.
- It does not score the z-probes or the y-probes as this letter.
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
three-axis far-face opposite seed process, cyclic next/prev lex-largest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1`, and
the reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-axis far-face opposite seed `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; fail at `A,D`, HOLD at `B,C` |
| unique signed `m`, cyclic index `i`, lex-largest `o_next`, `o_prev` | Theorem 1; mixed `M` at `A,D`; `i=` fail,`1`,`1`, fail |
| integer `det(m,o_next,o_prev)` | Theorem 1; fail, `-1`, `+1`, fail |
| Orient at `τ` | Theorem 1; fail, `−1`, `+1`, fail |
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
| leftover of lexicographic `o1,o2` | not this oriented display |
| leftover of cyclic lex-smallest | not this oriented display |
| leftover of nm2orichx unsigned leftover `+ℓ` | not this column order |
| leftover of nm2orilefx signed leftover axis | not this oriented display |
| leftover of nm2orionex lex-one signed outgoing | not this oriented display |
| leftover of opposite-pair presence in `O` | not this oriented display |
| z-probe or y-probe Orient on this seed | not this letter |
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
| leftover of the near three-axis opposite seed | not this display |
| leftover of nm2oricycl3fz far-face z-probe HOLD | not this letter |
| leftover of the same-lock two-site seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| empty cyclic slot scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: cyclic next/prev of `Axis(M)` with lex-largest signed `O` on each slot, not lex-smallest and not leftover axis, of the 1-in 2-out frame of `M` and `O` at `t+1` on the four x-probes of the three-axis far-face opposite seed, and reverse/face from that sign. |
| V2 | Current main has no landed cyclic next/prev lex-largest reverse/face of timed `M` and `O` on these four x-probes of the three-axis far-face opposite seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the integer sign of `det(m,o_next,o_prev)` from lex-largest cyclic slots at the same `t+1` cut, reverse fails from fail versus `−1`, z-probe reverse HOLDs on this same seed, Orient at `B` is `−1` while lex-one at `B` is `+1`, Orient at `C` is `+1` while lex-one at `C` is `−1`, and `M(A)` is mixed `{±e_3}` while two-axis `M(A)` is singleton `{−e_3}`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by lexicographic `o1,o2`, does not replace Orient by cyclic
lex-smallest, does not replace Orient by nm2orichx unsigned leftover `+ℓ`,
does not replace Orient by nm2orilefx signed leftover axis, does not
replace Orient by nm2orionex lex-one, does not replace Orient by nmcover
axis-cover, does not replace Orient by nm2axx axis-cover, does not replace
Orient by nm2ax12x 1-in 2-out split, does not identify this display with the
1-axis opposite two-site seed, does not identify it with the two-axis
opposite seed, and does not identify it with nmunopp union.
No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| cyclic lex-smallest | reuse cyclic axes with `+e` if both signs | lex-smallest Orient at `C` is `−1` while this Orient at `C` is `+1`; on this seed's z-probes lex-smallest at `A` is `+1` while lex-largest at `A` is `−1` | ATTEMPTED |
| lexicographic `o1,o2` | reuse unsigned reverse fail | lexicographic reverse fails with this reverse; unsigned columns at `C` are not cyclic `o_next,o_prev` | ATTEMPTED |
| nm2orichx unsigned leftover `+ℓ` | reuse leftover unit `+ℓ` as the third column | unsigned leftover at `C` is `−1`; this Orient at `C` is `+1` | ATTEMPTED |
| nm2orilefx signed leftover axis | reuse `det(m,e_pair,o_ℓ)` | leftover Orient at `B` and at `C` matches this Orient; leftover-axis is a different column order | ATTEMPTED |
| nm2orionex lex-one signed outgoing | reuse lex-one reverse fail and face fail | lex-one reverse fails with this reverse; lex-one Orient at `C` is `−1` while this Orient at `C` is `+1` | ATTEMPTED |
| unique signed `|O_i|=1` plane | fail mixed slots instead of lex-largest | unique signed fails at `C`; this Orient is `+1` at `C` | ATTEMPTED |
| nm2axx axis-cover | reuse cover reverse hold and cover face fail on these x-probes | cover reverse fails with this reverse; cover does not report `−1` at `B` | ATTEMPTED |
| nm2ax12x 1-in 2-out split | reuse split reverse hold and split face fail | split reverse fails with this reverse; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with this reverse bit; leftover of the union at `A` is `{e_2}` while Orient at `A` is fail | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` reverse fails with this reverse; leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}` | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` reverse fails with this reverse; leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}` | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold of `M` and of `O` | exist-opposite reverse of signed `O` fails with this reverse; exist-opposite face of signed `O` fails with this face | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence reverse fails without reading `−1` versus `+1` | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of signed incoming and lex-largest cyclic outgoing vectors | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(C,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is `+1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `A` and `D` fail cover from leftover `{e_2}` with mixed `M={±e_3}` | ATTEMPTED |
| empty cyclic slot as `UNDEFINED` | treat empty cyclic `O` slot as unformed | empty slot is Orient fail, not UNDEFINED; this `A` and `D` fail from mixed `M`, not from an empty cyclic slot | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(B)=2`, `t(D)=3`, mixed `M(D)`, cover face HOLD | different seed; second pair is a new seed, not a formed child; here `t(D)=2` and cover face fails | ATTEMPTED |
| two-axis opposite seed | reuse `t(A)=2`, `t(C)=3`, mixed `O(B)`, reverse fail | different seed; third pair is a new seed at `(0,0,−1)` locking `+e_3`; two-axis `M(A)={−e_3}` while this `M(A)={±e_3}` | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe cyclic lex-largest reverse HOLDs and face HOLDs with Orient `−1,−1,+1,+1`; this reverse fails and this face fails | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe cyclic lex-largest reverse fails with `t(A)=0`; this reverse fails with `t(A)=2` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic lex-largest orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports Orient fail, `−1`, `+1`, fail on the three-axis far-face opposite seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is three disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(C)` sums to `−e_2` while cyclic lex-largest Orient is `+1` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with cyclic lex-smallest, missing identification of
Orient with unsigned leftover unit `+ℓ`, missing identification of Orient
with nm2orilefx signed leftover axis, missing identification of Orient with
nm2orionex lex-one signed outgoing, missing identification of Orient with
lexicographic `o1,o2`, missing identification of Orient with nmcover
axis-cover, missing identification of Orient with nm2axx axis-cover, missing
identification of Orient with nm2ax12x 1-in 2-out split, missing
identification of this seed with the 1-axis opposite two-site seed, missing
identification of this seed with the two-axis opposite seed, and
missing Record identification of Orient reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite seed pairs `+e_1/−e_1`,
`+e_2/−e_2`, and `+e_3/−e_3`, perpendicular step rule, incoming-step lock,
own incoming set and own outgoing dual from records with tick `<= τ`,
per-probe `τ=t+1`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, unique signed `m` when
split HOLDs, cyclic next and previous axes of the axis index of `m`,
lex-largest signed vector of `O` on each cyclic slot under `+e < −e`, empty
cyclic slot as Orient fail not `UNDEFINED`, integer determinant sign, split
fail as Orient fail not `UNDEFINED`, four x-probes with formed child `C`,
third pair as a new seed not a formed child on the `−z` face opposite the
z-probes, and mixed remains a set are declared. No uniqueness of
outgoing locks, no six-neighbor lock union as the scored object, no
lock-count clock, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | unique signed incoming letter, cyclic next/prev axes of `Axis(M)`, lex-largest signed `O` vector on each cyclic slot | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse fail and face fail are only leftover-empty fail,
or only presence of an opposite pair in `O`; leftover of `M` alone already
answers reverse; leftover of `O` alone already answers reverse;
exist-opposite of signed `O` already answers reverse; lexicographic
`o1,o2` already answers handedness; cyclic lex-smallest already answers
cyclic slots; nm2orionex lex-one already answers signed outgoing; nm2orilefx
signed leftover already answers reverse because reverse and face bits agree;
the four z-probes already displayed this letter; mixed #7188 already reported
fail/fail; the four y-probes already displayed this letter; the third
pair is only the formed child of the two-axis seed; unique outgoing letters
should be required; and unsigned incoming axis already gives the same signs.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. This reverse fails from Orient fail at `A` versus `−1` at
`B`, and leftover of the union at `A` is `{e_2}` while Orient at `A` is
fail from mixed `M={±e_3}`. Cover and split fail reverse on this member
because they fail at `A`, and they do not score that Orient at `B` is
`−1`. Lexicographic `o1,o2` reverse fails with fail versus `+1`; unsigned
Orient at `B` is `+1` while this Orient at `B` is `−1`. Cyclic
lex-smallest reverse fails with this reverse, but lex-smallest Orient at
`B` is `+1` and at `C` is `−1` while this Orient is `−1` at `B` and `+1`
at `C`. Lex-one reverse fails; lex-one Orient at `C` is `−1` while this
Orient at `C` is `+1`. Signed leftover-axis Orient at `B` and at `C`
matches this Orient, but leftover-axis is a different column order.
Unsigned leftover `+ℓ` at `C` is `−1` while this Orient at `C` is `+1`.
Presence of an opposite pair in `O` fails at `A` and HOLDs at `B`, so
pair-presence reverse fails without reading fail versus `−1`. Leftover of
`M` alone at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`: leftover-of-`M`
reverse fails with this reverse. Leftover of `O` alone at `A` is
`{e_2,e_3}` and at `B` is `{e_1}`. Exist-opposite reverse of signed `O`
fails with this reverse. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(C)`; this Orient is `+1`, not `UNDEFINED`. The four
z-probes of this same seed score cyclic lex-largest reverse hold and face
hold with Orient `−1,−1,+1,+1`; this letter is the four x-probes, which
fail reverse from fail versus `−1` and fail face from Orient fail at `D`.
The four y-probes fail reverse. Mixed #7188 is a different z-symmetric
process with mixed `M`. The third pair is a new seed, not a formed child:
`(0,0,−1)` is recorded at tick 0 with lock `+e_3` and `(0,1,−1)` is
recorded at tick 0 with lock `−e_3`, and x-probe `C` is a formed child at
tick 3, not that seed. Reverse oriented frame is HOLD iff equal `±1`
signs at `A` and at `B`, not leftover-empty fail and not leftover of `M`
alone.

### N8 — cross-cycle echo

nm2axx cover on this far-face seed reports cover fail at `A` and at `D`,
cover HOLD at `B` and at `C`, reverse fail, and face fail. nm2ax12x 1-in
2-out split on this same seed reports split fail at `A` and at `D`, split
HOLD at `B` and at `C`, reverse fail, and face fail. Two-axis x-probe
cyclic lex-largest reverse fails from fail versus `−1` with `t(A)=2` and
singleton `M(A)={−e_3}`. Lexicographic `o1,o2` on these x-probes reports
Orient fail, `+1`, `+1`, fail, reverse fail, and face fail. Cyclic
lex-smallest on these slots reports Orient fail, `+1`, `−1`, fail, reverse
fail, and face fail. nm2orichx unsigned leftover `+ℓ` on these x-probes
reports Orient fail, `−1`, `−1`, fail. nm2orilefx signed leftover axis
reports Orient fail at `A` and `+1` at `C`. nm2orionex lex-one signed
outgoing reports Orient fail, `+1`, `−1`, fail, reverse fail, and face
fail. Leftover axis reports leftover `{e_2}` at `A` and at `D` and empty
leftover at `B` and at `C`, leftover reverse fail, and leftover face fail.
The four z-probes of this same seed report cyclic lex-largest reverse hold
and face hold. The four y-probes report reverse fail and face fail. The
near three-axis opposite x-probes report `t(A)=1`, `t(C)=0`, Orient
`−1,+1,+1`, fail. This note is not those displays: it reports cyclic
next/prev lex-largest outgoing determinant orientation of the 1-in 2-out
frame of `M` and `O` at `τ=t+1` on the three-axis far-face opposite seed,
with `t(A)=2`, `t(B)=1`, `t(C)=3`, and `t(D)=2`, `Orient(A)=fail`,
`Orient(B)=−1`, `Orient(C)=+1`, `Orient(D)=fail`, reverse fail, and face
fail. Cover and split do not score handedness.

**Gate disposition:** PASS for the cyclic next/prev lex-largest `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals cyclic lex-smallest HOLD,” “the predicate
equals unsigned leftover unit `+ℓ`,” “the predicate equals nm2orilefx
signed leftover HOLD,” “the predicate equals nm2orionex lex-one HOLD,”
“the predicate equals lexicographic `o1,o2` HOLD,” “the predicate equals
nmcover axis-cover HOLD,” “the predicate equals nm2axx axis-cover HOLD,”
“the predicate equals nm2ax12x 1-in 2-out split HOLD,” “the predicate
equals the 1-axis opposite two-site seed,” “the predicate equals the
two-axis opposite seed,” “the predicate equals nmunopp union,” “bits are
Admissibility,” “split fail is UNDEFINED,” “empty cyclic slot is UNDEFINED,”
“reverse oriented frame holds,” or “face oriented frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis far-face
opposite perp-step incoming-lock process, reads each probe's own earliest
incoming set and own outgoing dual from the record prefix at that probe's
`t+1`, reports split of the pair, reports the unique signed incoming
letter, the cyclic axis index `i`, lex-largest `o_next` and `o_prev`,
reports the integer determinant and its sign, lists new records in
`B_3(0)` between `t` and `t+1` that meet a probe's six-neighbors, and
checks Theorems 1--3. It also checks that Orient is fail, `−1`, `+1`, fail
at `A,B,C,D`, that reverse fails and face fails, that leftover-of-`M`
reverse fails with this reverse, that exist-opposite reverse fails with
this reverse, that cover reverse fails with this reverse, that
leftover-axis Orient at `C` is `+1` matching this Orient at `C` while
unsigned leftover at `C` is `−1`, that lex-one Orient at `C` is `−1`
while this Orient at `C` is `+1`, that split fail is Orient fail not
`UNDEFINED`, that an empty cyclic slot is Orient fail not `UNDEFINED`,
that the 1-axis opposite two-site seed is a different member with
`t(D)=3`, that the two-axis opposite seed is a different member with
singleton `M(A)={−e_3}` and reverse fail, that the near three-axis
opposite seed is a different member with `t(A)=1` and `t(C)=0`, that
leftover-empty fail is a different predicate, that leftover of `M` alone
and leftover of `O` alone are different objects, that mixed sets remain
sets, that unique-letter Orient is `UNDEFINED` at mixed `O`, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that the third pair is a new seed not
a formed child on the `−z` face, that the z-probes of this seed HOLD
reverse and HOLD face and are not this letter, that the y-probes of this
seed fail reverse and are not this letter, and that the display is not
the two-tick lock-count clock composition. No runner cache is written.
