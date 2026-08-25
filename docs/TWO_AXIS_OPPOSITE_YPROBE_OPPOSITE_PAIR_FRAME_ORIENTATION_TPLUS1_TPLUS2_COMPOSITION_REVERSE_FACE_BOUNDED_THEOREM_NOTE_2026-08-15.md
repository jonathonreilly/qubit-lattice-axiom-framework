---
claim_id: two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Opposite-pair orientation at t+1 versus t+2 on the four y-probes of the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Opposite-Pair Orientation Freeze t+1 Versus t+2 Reverse And Face On Four Y-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** opposite-pair orientation of the 1-in 2-out frame of simultaneous
earliest incoming set `M` and outgoing dual `O` at each probe's `τ1=t+1`
and `τ2=t+2`, reverse/face from that sign at each cut, and composition of
Orient, on the four y-probes of the two-axis opposite seed in
`B_3(0)={n:n·n<=9}`. Same process and y-probes as nm2axo. Orient as
nm2orichz at each cut. Uniqueness is not required. Let `t(q)` be the
formation tick of probe `q`. Cuts are local: `τ1=t+1`, `τ2=t+2`.
There is no global T. Do not score τ=t. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick
`<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing dual
of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)`
equals `{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required. When `M` is
singleton `{m}` and `O` contains some `e` and `−e`, let `o_pair` be that
`e` of smallest axis index, leftover axis `ℓ` the unique Axis not in
`{axis(m), axis(e)}`, oriented as the unit `+ℓ`. `Orient(q,τ)` is the
sign of the integer determinant of the 3×3 matrix with columns `m`, `e`,
`+ℓ`. If no opposite pair in `O`, fail, not `UNDEFINED`. Else fail, not
`UNDEFINED`, if split fails. Reverse HOLDs if and only if
`Orient(A)=Orient(B)` both `±1` at that cut. Face HOLDs if and only if
`Orient(C)=Orient(D)` both `±1` at that cut. Composition HOLDs if and
only if `Orient` at `τ1` equals `Orient` at `τ2` at `A,B,C,D`. Cover and
split do not score handedness. This is not leftover of nm2orichy
opposite-pair orientation at `t+1` alone. This is not leftover of
nm2orichz z-probe opposite-pair orientation. This is not leftover of
nm2orioney lex-one signed-outgoing det orientation. This is not leftover
of nm2simt2y simultaneous `M` and `O` freeze. This is not leftover of
nm2oricht2z z-probe freeze. This is not leftover of lexicographic
`o1,o2` orientation. This is not leftover of nm2axo axis-cover. This is
not leftover of 1-in 2-out split.
This is not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover-empty fail of leftover axis.
This is not leftover of nmunopp union. This is not leftover of nmt2opp
`M` frozen at `t`. This is not leftover of nmot2opp two-tick composition.
This is not leftover of nmoutopp untimed eventual-`O`. This is not
leftover of mixed #7188 fail/fail. This is not leftover of the 1-axis
opposite two-site seed. This is not leftover of the same-lock two-site
seed. This is not the two-tick lock-count clock composition. The second
pair is a new seed, not a formed child. Uniqueness is not required. Mixed
remains a set. Displayed, not adopted. Do not write into Admissibility.
Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

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
and `Axis(O)`. Split is cover together with `|Axis(M)|=1`. The opposite-pair
oriented frame is the integer sign of `det(m,e,+ℓ)` with unique signed
incoming letter `m`, signed exist-opposite pair unit `e` of smallest axis
index in `O`, and leftover unit `+ℓ`. Reverse and face are scored on equal
`±1` signs at the paired probes at each cut. Composition is equality of
those four Orient reports across the two cuts. Named signs `{+,−}` of locks
are a coarser readout and are not used as the object. A singleton unique
outgoing lock letter is a different readout and is not used as the object.
Presence of an opposite pair in `O` without the determinant sign is a
different readout and is not used. Lexicographic unsigned outgoing 2-plane
`(o1,o2)` in axis order is a different readout and is not used.
Existential opposite of signed locks across probes is a different readout
and is not used. Axis-cover without the frame sign is a different readout
and is not used. 1-in 2-out split without the frame sign is a different
readout and is not used. Simultaneous `M` and `O` freeze is a different
readout and is not used. Leftover-empty fail of unsigned leftover axis
sets is a different readout and is not used. A `Z^3` sum of those locks
is a different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of opposite-pair orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 on the four y-probes of the two-axis opposite seed, Orient at A,B,C,D at each cut, reverse fail and face fail at each cut, composition hold; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_opposite_pair_frame_orientation_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display opposite-pair orientation freeze t+1 versus t+2 reverse/face composition on the four y-probes of the two-axis opposite seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep opposite-pair orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 displayed; do not write Orient into Admissibility, do not reduce to nm2orichy t+1 alone, do not reduce to nm2orichz z-probes, do not reduce to nm2orioney, do not reduce to nm2simt2y M-and-O freeze, do not reduce to lexicographic o1,o2, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by presence of an opposite pair in O, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for opposite-pair orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 on the four y-probes of the two-axis opposite seed, reverse/face at each cut, and composition; displayed, not adopted"
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
opposite-pair 1-in 2-out frame of `M` and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nm2axo.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
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

## Named opposite-pair 1-in 2-out frame of `M` and `O` at `τ1` and `τ2`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
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

Opposite-pair oriented frame at a cut, as nm2orichz:

```text
When M is singleton {m} and O contains some e and −e,
o_pair is that e of smallest axis index.
leftover axis ℓ is the unique Axis not in {axis(m), axis(e)},
oriented as the unit +ℓ.
Orient(q,τ) = sign of the integer determinant of columns (m, e, +ℓ).
If no opposite pair in O, fail, not UNDEFINED.
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The opposite-pair unit is the positive lattice unit of the smallest-index
axis on which `O` contains both signs. Unique outgoing letters are not
required. Mixed opposite signs occupy that axis as the pair. A vanishing
determinant is fail. Sign of a nonzero integer determinant is `+1` or `−1`.
Split HOLD required: 2-in 1-out is Orient fail, not UNDEFINED, even if `O`
contains an opposite pair.

Reverse oriented frame at a cut holds if and only if `Orient(A)=Orient(B)`
and both signs are `±1`. Face oriented frame at a cut holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Composition holds if and only if `Orient(q,τ1)=Orient(q,τ2)` at each of
`A,B,C,D`. Either side `UNDEFINED` is `UNDEFINED`. Else if the four signs
agree across the two cuts, composition HOLDs. Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse while this reverse fails.
Identifying split reverse with this reverse is refused: split HOLDs
reverse while this reverse fails. Identifying leftover-empty fail with
this reverse is refused: leftover-empty fail scores empty leftover as
reverse fail, agreeing with these bits, while leftover of `M` reverse
HOLDs. Identifying lexicographic `o1,o2` orientation with this reverse is
refused: lexicographic reverse fails with `Orient_lex(A)=−1` and
`Orient_lex(B)=+1`, while this reverse fails from fail and `−1`.
Identifying presence of an opposite pair in `O` with this face is
refused: each of `C` and `D` has an opposite pair in `O`, so pair-presence
face HOLDs while this face fails. Identifying nm2simt2y `M` and `O` freeze
with this composition is refused: that letter is equality of lock sets,
not equality of `det(m,e,+ℓ)` reports. Identifying a named sign of those
locks with reverse or face is refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, and Orient at `τ1` and `τ2`

On this process the four y-probes form. Compare to leftover axis: leftover
of the union is empty at `A`, `B`, and `C` and nonempty `{e_2}` at `D`,
so leftover reverse fail and leftover face fail. Compare to cover and
split: cover and split HOLD reverse and fail face. Compare to
lexicographic `o1,o2`: reverse fails from `−1,+1` and face fails from
`−1` and fail at `D`. Compare to nm2orichy: that letter is the `t+1` cut
alone. Compare to nm2orichz: that letter is the four z-probes. Compare to
nm2orioney: that letter is a different det orientation with reverse HOLD
and face fail. This display reads the opposite-pair oriented frame of
those same timed sets at both cuts:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ1) = {−e_1}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_2}
M(D, τ1) = {−e_3}
O(A, τ1) = {+e_2, −e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ1) = {+e_1, −e_1}
Orient(A, τ1) = fail
Orient(B, τ1) = −1
Orient(C, τ1) = −1
Orient(D, τ1) = fail
M(A, τ2) = {−e_1}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_2}
M(D, τ2) = {−e_3}
O(A, τ2) = {+e_2, −e_3}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ2) = {+e_1, −e_1}
Orient(A, τ2) = fail
Orient(B, τ2) = −1
Orient(C, τ2) = −1
Orient(D, τ2) = fail
```

`A` is a seed at tick 0 with seed letter `−e_1`. Mixed remains a set:
`O(A,τ1)` has two outgoing steps and `O(B,τ1)` has three outgoing steps.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Here
uniqueness is not required. At `A`, split HOLDs and pair fails because
`O(A)` has `+e_2` and `−e_3` with no common axis, so Orient at `A` is fail,
not `UNDEFINED`. At `B`, split HOLDs, pair HOLDs on `{+e_3,−e_3}`, leftover
unit is `+e_2`, and `det(+e_1,+e_3,+e_2)=−1`. At `C`, split HOLDs, two
opposite pairs sit in `O`, smallest axis index is `e_1`, leftover unit is
`+e_3`, and `det(+e_2,+e_1,+e_3)=−1`. At `D`, pair HOLDs on `{+e_1,−e_1}`
and leftover unit is `+e_2`, but split fails from cover fail with leftover
`{e_2}` (1-in 1-out). Split HOLD is required, so Orient at `D` is fail, not
`UNDEFINED`, and `det(D)` is fail. Cover and split HOLD reverse on this
member and do not score that `Orient(A)` is fail. Lexicographic `o1,o2` at
`A` is `−1` while opposite-pair Orient at `A` is fail. O is not M.

On the 1-axis opposite two-site seed, `A` is still a seed at tick 0, `B`
forms at tick 2, `C` at tick 1, and `D` at tick 3 with mixed `M`, so split
fails at `D` and Orient at `D` is fail, not UNDEFINED. Cover face HOLDs on
that 1-axis member. That is leftover of the first pair. Here both
`(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a second
axis, and `t(D)=2`. On the z-probes of this same seed, opposite-pair Orient
is `−1,−1,+1,−1` with reverse HOLD and face fail at both cuts.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`. The `t+2` neighbors of `A` form with
earliest incoming `−e_3`, so `+e_1` and `−e_1` do not enter `O(A,τ2)`:

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
empty at `A`, `B`, and `C`. At `D`, `O` at `t` is `{−e_1}` and grows to
`{+e_1, −e_1}` at `t+1`. Split fails at `t` at each probe, and Orient is
fail, not UNDEFINED. Do not score `τ=t`.

## Theorem 2 — reverse and face from oriented frame at `τ1` and `τ2`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. At `τ1`, `Orient(A)` is fail and `Orient(B)=−1`. Reverse fails. At
`τ2`, `Orient(A)` is fail and `Orient(B)=−1`. Reverse fails. This is HOLD
iff equal `±1` signs, not leftover of lexicographic `o1,o2`, not leftover
of axis-cover, not leftover of 1-in 2-out split, not leftover-empty fail,
and not exist-opposite.

Reverse oriented frame at τ1: fail
Reverse oriented frame at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Lexicographic reverse fails because lexicographic `Orient(A)=−1` and
`Orient(B)=+1`, a different pair of values than fail and `−1`.
Opposite-pair reverse fails because `Orient(A)` is fail. Leftover-empty
reverse fails because leftover of the union is empty at `A` and at `B`.
Leftover of `M` reverse HOLDs because leftover of `M` at `A` and at `B` is
`{e_2, e_3}`: nonempty and equal. Leftover of `O` reverse HOLDs because
leftover of `O` at `A` and at `B` is `{e_1}`: nonempty and equal.
Exist-opposite reverse of signed `M` holds. Exist-opposite reverse of
signed `O` holds. Presence of an opposite pair in `O` fails at `A` and
HOLDs at `B`, so pair reverse fails. Those leftovers are not this
display.

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
At `τ1`, `Orient(C)=−1` and `Orient(D)` is fail. Face fails. At `τ2`,
`Orient(C)=−1` and `Orient(D)` is fail. Face fails.

Face oriented frame at τ1: fail
Face oriented frame at τ2: fail

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Opposite-pair oriented face fails because Orient fails
at `D` from split fail, even though pair HOLDs at `C` and at `D`. Pair
face HOLDs while Orient face fails: split HOLD is required. Lexicographic
face fails from `Orient(C)=−1` and Orient fail at `D`. On the 1-axis
opposite two-site seed, cover face HOLDs while split face fails at `D`,
and Orient at `D` is fail, not UNDEFINED. This two-axis member is not
leftover of that 1-axis cover face HOLD. The four z-probes of this same
seed give opposite-pair reverse hold and opposite-pair face fail. The
four x-probes give oriented reverse fail and oriented face fail. Those
probe-direction readouts are not this y-probe display. Leftover-empty
face fails because leftover of the union is empty at `C` and nonempty at
`D`. Leftover of `M` at `C` is `{e_1, e_3}` and leftover of `M` at `D` is
`{e_1, e_2}`: nonempty and unequal. Leftover of `O` at `C` is `{e_2}` and
leftover of `O` at `D` is `{e_2, e_3}`: nonempty and unequal.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed
`O` holds. Opposite-pair oriented face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `D` and split fails at `D`. Pair HOLDs at
`D`. Orient at `D` is fail at both cuts.

Reverse fails at both cuts. Face fails at both cuts.

## Theorem 3 — composition of Orient at `τ1` versus `τ2`

Composition HOLDs if and only if `Orient` at `τ1` equals `Orient` at `τ2`
at `A,B,C,D`. `Orient(A,τ1)=Orient(A,τ2)=fail`,
`Orient(B,τ1)=Orient(B,τ2)=−1`, `Orient(C,τ1)=Orient(C,τ2)=−1`,
`Orient(D,τ1)=Orient(D,τ2)=fail`. Composition HOLDs.

Composition of Orient: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

The reverse-fail face-fail orientation of nm2orichy at `t+1` freezes at
`t+2`: the four reports are unchanged. That freeze is the present letter.
It is not leftover of nm2orichy, which scores only one cut. It is not
leftover of nm2orichz, which scores the four z-probes. It is not leftover
of nm2orioney, which scores a different det orientation with reverse HOLD
and face fail. It is not leftover of nm2oricht2z, which scores reverse
HOLD, face fail, and composition HOLD on the z-probes. It is not leftover
of nm2simt2y, which scores equality of `M` and of `O` rather than equality
of Orient. On this member `M` and `O` also freeze, so simultaneous freeze
HOLDs as a leftover; the scored object remains the four Orient reports.
Bit-stability of reverse fail and face fail is a leftover predicate: those
bits can agree while a probe report flips, which composition of Orient
would fail. Composition of Orient at `τ=t` versus `τ=t+1` fails because
Orient is fail at formation at `B` and at `C` and `−1` at `t+1`. Do not
score `τ=t`.

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
- It does not replace Orient by lexicographic `o1,o2` orientation.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not replace Orient composition by nm2simt2y `M` and `O` freeze.
- It does not treat split fail as `UNDEFINED`.
- It does not treat missing opposite pair as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace Orient by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmcover axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2axo axis-cover reverse hold face fail as this
  oriented display.
- It does not reprint 1-in 2-out split reverse hold face fail as this
  oriented display.
- It does not reprint lexicographic `o1,o2` reverse fail face fail as this
  opposite-pair display.
- It does not reprint nm2orichy opposite-pair orientation at `t+1` alone.
- It does not reprint nm2orichz z-probe opposite-pair reverse hold face
  fail as this y-probe freeze.
- It does not reprint nm2orioney lex-one signed-outgoing reverse hold face
  fail as this opposite-pair freeze.
- It does not reprint nm2oricht2z z-probe reverse hold face fail
  composition hold as this y-probe letter.
- It does not reprint nm2simt2y simultaneous `M` and `O` freeze as this
  Orient composition.
- It does not reprint the 1-axis opposite two-site seed as this member.
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
two-axis opposite seed process, opposite-pair orientation of the 1-in 2-out
frame of `M` and `O` at `t+1` versus `t+2`, reverse/face at each cut, and
composition of Orient are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ1` and at `τ2` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ1` and at `τ2` | Theorem 1; HOLDING outgoing dual, freeze |
| unique signed `m`, opposite pair in `O`, leftover `+ℓ` | Theorem 1; singleton `M`; pair fail at `A`; leftover unit at `B,C,D` |
| integer `det(m,e,+ℓ)` at both cuts | Theorem 1; fail at `A` and at `D`; `−1` at `B` and at `C` |
| Orient at `τ1` | Theorem 1; `fail,−1,−1,fail` |
| Orient at `τ2` | Theorem 1; `fail,−1,−1,fail` |
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
| leftover of nm2axo axis-cover HOLD reverse fail face | not this oriented display |
| leftover of 1-in 2-out split HOLD reverse fail face | not this oriented display |
| leftover of lexicographic `o1,o2` | not this oriented display |
| leftover of nm2orichy `t+1` alone | not this freeze letter |
| leftover of nm2orichz z-probe `t+1` | not this y-probe freeze |
| leftover of nm2orioney reverse HOLD | not this opposite-pair Orient |
| leftover of nm2oricht2z z-probe freeze | not this y-probe letter |
| leftover of nm2simt2y `M` and `O` freeze | not this Orient composition |
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
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the same-lock two-site seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| score at `τ=t` | refused |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: does the opposite-pair orientation of nm2orichz freeze from `t+1` to `t+2` on the four y-probes of the two-axis opposite seed. |
| V2 | Current main has no landed opposite-pair-frame reverse/face composition of timed `M` and `O` at `t+1` versus `t+2` on these four y-probes of the two-axis opposite seed. |
| V3 | Orient reports at two cuts, the reverse/face bits at each cut, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the integer sign of `det(m,e,+ℓ)` at two local cuts and reports that reverse fails, face fails, and the four reports freeze, while cover/split reverse HOLD, leftover of `M` reverse HOLDs, leftover of `O` reverse HOLDs, pair-presence face HOLDs, nm2orioney reverse HOLDs, and nm2simt2y scores lock-set equality rather than Orient equality. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by lexicographic `o1,o2`, does not replace Orient by nmcover
axis-cover, does not replace Orient by nm2axo axis-cover, does not replace
Orient by 1-in 2-out split, does not replace this freeze by nm2orichy
`t+1` alone, does not replace this freeze by nm2orichz z-probes, does not
replace this freeze by nm2orioney reverse HOLD, does not replace this
freeze by nm2oricht2z, does not replace Orient composition by nm2simt2y
`M` and `O` freeze, does not identify this display with the 1-axis opposite
two-site seed, and does not identify it with nmunopp union. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2orichy `t+1` alone | reuse reverse fail and face fail at one cut | that letter has no `t+2` cut and no Orient composition | ATTEMPTED |
| nm2orichz z-probes | reuse reverse hold and face fail on z-probes | z-probe reverse HOLDs; this y-probe reverse fails | ATTEMPTED |
| nm2oricht2z z-probe freeze | reuse reverse hold, face fail, composition hold | that letter is the four z-probes with reverse HOLD | ATTEMPTED |
| nm2orioney lex-one det | reuse reverse hold and face fail | orioney reverse HOLDs; this opposite-pair reverse fails | ATTEMPTED |
| nm2simt2y `M` and `O` freeze | score equality of lock sets | simultaneous freeze HOLDs here as leftover; composition of this letter is equality of Orient reports | ATTEMPTED |
| reverse/face bit-stability | score reverse and face bits equal across cuts | those bits can agree while a probe report flips; composition of Orient would then fail | ATTEMPTED |
| lexicographic `o1,o2` | reuse lexicographic reverse fail and face fail | lexicographic reverse fails (`−1,+1`) while this reverse fails from fail and `−1`; same bits, different values | ATTEMPTED |
| nm2axo axis-cover | reuse cover reverse hold and cover face fail on these y-probes | cover reverse HOLDs while Orient reverse fails: `Orient(A)` is fail | ATTEMPTED |
| 1-in 2-out split | reuse split reverse hold and split face fail | split reverse HOLDs while Orient reverse fails; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with Orient reverse; leftover of `M` reverse HOLDs while Orient reverse fails | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` is `{e_2,e_3}`, nonempty equal; leftover reverse HOLDs while Orient reverse fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` is `{e_1}`, nonempty equal; leftover reverse HOLDs while Orient reverse fails | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` HOLDs while Orient reverse fails; exist-opposite is a cross-probe boolean, not `det(m,e,+ℓ)` | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at `C` and at `D`, so that face HOLDs while Orient face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of signed incoming, pair unit, and leftover unit | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; pair fails at `A` and Orient is fail | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member they agree at `B` and at `C`; flipping `m` at `B` to `−e_1` flips Orient to `+1` while unsigned axis stays `e_1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` is 1-in 1-out cover fail | ATTEMPTED |
| no opposite pair as `UNDEFINED` | treat missing `e` and `−e` in `O` as unformed | missing opposite pair is Orient fail, not UNDEFINED; y-probe `A` of this seed is the witness | ATTEMPTED |
| score at `τ=t` | compose Orient at formation versus `t+1` | leftover of nmot2opp; Orient is fail at `t` at `B` and at `C` and `−1` at `t+1`; Do not score `τ=t` | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(B)=2`, `t(D)=3`, mixed `M(D)`, Orient fail at `D` | different seed; second pair is a new seed, not a formed child; here `t(D)=2` and cover face fails | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe reverse HOLDs; this letter is the four y-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails; this letter is the four y-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores the opposite-pair oriented frame of own incoming and outgoing at `t+1` versus `t+2` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports Orient `fail,−1,−1,fail`, reverse fail, face fail, and composition hold | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(B)` sums to `+e_2` while the pair is `+e_3` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with lexicographic `o1,o2`, missing
identification of Orient with nmcover axis-cover, missing identification of
Orient with nm2axo axis-cover, missing identification of Orient with
1-in 2-out split, missing identification of this freeze with nm2orichy
`t+1` alone, missing identification of this freeze with nm2orichz
z-probes, missing identification of this freeze with nm2orioney, missing
identification of Orient composition with nm2simt2y `M` and `O` freeze,
missing identification of this seed with the 1-axis opposite two-site
seed, and missing Record identification of Orient reverse are distinct
open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ1=t+1`
and `τ2=t+2`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, unique signed `m` when
split HOLDs, smallest-index opposite pair in `O` when present, leftover
unit `+ℓ`, integer determinant sign, missing opposite pair as Orient fail
not `UNDEFINED`, split fail as Orient fail not `UNDEFINED`, four y-probes
with seed `A`, second pair as a new seed not a formed child, mixed remains
a set, and composition as equality of Orient at the two cuts are declared.
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
| per element | signed incoming letter, smallest-index opposite pair in `O`, leftover `+axis` among `{e_1,e_2,e_3}` at a probe's `t+1` and `t+2` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports at `t+1` and `t+2`, reverse/face at each cut, composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, a later cut `t+3`, and a physical selector among 1-in
2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse fail is only leftover-empty fail, only pair
fail at `A`, or only lexicographic reverse fail; leftover of `M` alone
already answers reverse; leftover of `O` alone already answers reverse;
exist-opposite of signed `O` already answers reverse; cover reverse and
split reverse already answer reverse; nm2orioney reverse HOLD already
answers y-probe orientation; the second pair is only the formed child
`(0,0,1)` of the 1-axis seed; unique outgoing letters should be required;
unsigned incoming axis already gives the same reports; because `M` and
`O` freeze, composition is nm2simt2y; because reverse fail and face fail
at both cuts, composition is only bit-stability; and nm2orichy already
answered reverse-fail face-fail orientation.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail, agreeing with these bits while leftover of `M` reverse
HOLDs. Orient reverse fails because `Orient(A)` is fail and `Orient(B)=−1`,
while Orient face fails because `Orient(C)=−1` and `Orient(D)` is fail, at
both cuts. Cover and split HOLD reverse on this member and do not score
that `Orient(A)` is fail. Lexicographic `o1,o2` reverse fails with `−1,+1`
and face fails with `−1` and fail; this reverse fails from fail and `−1`.
Presence of an opposite pair in `O` fails at `A` and HOLDs at `C` and at
`D`, so pair-presence reverse fails with this reverse while pair-presence
face HOLDs and this face fails. Leftover of `M` alone at `A` and at `B` is
`{e_2,e_3}`: nonempty equal, so leftover-of-`M` reverse HOLDs while Orient
reverse fails. Leftover of `O` alone at `A` and at `B` is `{e_1}`:
leftover-of-`O` reverse HOLDs. Exist-opposite reverse of signed `O` holds,
but exist-opposite is a cross-probe boolean, not `det(m,e,+ℓ)`. Unique
outgoing letters would assign `UNDEFINED` at mixed `O(A)`; pair fails at
`A`. Unsigned incoming axis agrees on this member at `B` and at `C`, and
flipping `m` at `B` to `−e_1` flips Orient to `+1` while `Axis(M)` stays
`{e_1}`. The second pair is a new seed, not a formed child: `(0,0,1)` is
recorded at tick 0 with lock `+e_2`, whereas the 1-axis child forms at
tick 1 with lock `+e_3`. nm2orichy scores only `τ=t+1`. nm2orioney reverse
HOLDs. nm2simt2y scores equality of `M` and of `O`. Reverse/face
bit-stability can HOLD while a probe report flips. Reverse oriented frame
is HOLD iff equal `±1` signs at `A` and at `B` at that cut, not leftover
of lexicographic `o1,o2`. Composition of Orient: hold.

### N8 — cross-cycle echo

nm2axo cover on this two-axis seed reported cover HOLD at `A`, `B`, and
`C` and cover fail at `D`, reverse hold, and face fail. 1-in 2-out split
on the same seed reported split HOLD at `A`, `B`, and `C` and split fail
at `D`, reverse hold, and face fail. Lexicographic `o1,o2` on the same
seed reported Orient `−1,+1,−1,fail`, reverse fail, and face fail.
nm2orichy reported opposite-pair Orient `fail,−1,−1,fail`, reverse fail,
and face fail at `t+1` alone. nm2orichz reported opposite-pair Orient
`−1,−1,+1,−1`, reverse hold, and face fail at `t+1` on the z-probes.
nm2orioney reported reverse hold and face fail from a different det.
nm2oricht2z reported reverse hold, face fail, and composition hold on the
z-probes. Leftover of `M` reverse HOLDs on these y-probes. This note is
not those displays: it reports opposite-pair orientation of the 1-in 2-out
frame of `M` and `O` at `τ1=t+1` versus `τ2=t+2` on the two-axis opposite
seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=2`,
`Orient=fail,−1,−1,fail` at both cuts, reverse fail at both cuts, face
fail at both cuts, and composition hold. Cover and split do not score
handedness.

**Gate disposition:** PASS for the opposite-pair-frame `t+1` versus `t+2`
reverse/face reports and displayed composition above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals leftover-empty fail,” “the predicate equals leftover
of `M` alone,” “the predicate equals leftover of `O` alone,” “the
predicate equals exist-opposite HOLD,” “the predicate equals opposite-pair
presence in `O`,” “the predicate equals lexicographic `o1,o2` HOLD,” “the
predicate equals nmcover axis-cover HOLD,” “the predicate equals nm2axo
axis-cover HOLD,” “the predicate equals 1-in 2-out split HOLD,” “the
predicate equals nm2orichy `t+1` alone,” “the predicate equals nm2orichz
z-probes,” “the predicate equals nm2orioney reverse HOLD,” “the predicate
equals nm2oricht2z,” “the predicate equals nm2simt2y `M` and `O` freeze,”
“the predicate equals the 1-axis opposite two-site seed,” “the predicate
equals nmunopp union,” “bits are Admissibility,” “split fail is
UNDEFINED,” “no opposite pair is UNDEFINED,” “reverse oriented frame
holds,” “face oriented frame holds,” or “composition of Orient fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
`t+2`, reports the unique signed incoming letter, the smallest-index
opposite pair in `O`, leftover unit `+ℓ`, the integer determinant and its
sign at both cuts, lists new records in `B_3(0)` between `t` and `t+1` and
between `t+1` and `t+2` that meet a probe's six-neighbors, and checks
Theorems 1--3. It also checks that Orient is `fail,−1,−1,fail` at
`A,B,C,D` at both cuts, that reverse fails at both cuts while cover
reverse and split reverse HOLD and leftover of `M` reverse HOLDs, that
face fails at both cuts while pair-presence face HOLDs, that composition
HOLDs, that split fail is Orient fail not `UNDEFINED`, that no opposite
pair in `O` is Orient fail not `UNDEFINED`, that the 1-axis opposite
two-site seed is a different member with Orient fail at `D` and cover
face HOLD, that leftover of `M` alone and leftover of `O` alone are
different objects, that mixed sets remain sets, that unique-letter Orient
is `UNDEFINED` at mixed `O`, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not
attached, that the second pair is a new seed not a formed child, that the
z-probes and x-probes of this seed are not this letter, that `τ=t` is not
scored, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
