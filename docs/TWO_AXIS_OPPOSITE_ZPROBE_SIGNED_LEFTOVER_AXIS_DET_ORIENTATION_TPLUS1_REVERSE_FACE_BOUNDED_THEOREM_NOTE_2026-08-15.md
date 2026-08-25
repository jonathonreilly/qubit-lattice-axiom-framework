---
claim_id: two_axis_opposite_zprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Signed leftover-axis determinant orientation of the 1-in 2-out frame at t+1 on the four z-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_zprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Signed Leftover-Axis Determinant Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four Z-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** signed leftover-axis determinant orientation of the 1-in 2-out
frame of simultaneous earliest incoming set `M` and outgoing dual `O` at
each probe's `τ=t+1`, and reverse/face from that sign, on the four
z-probes of the two-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same
process and z-probes as nm2axz. `M` and `O` as nm2ax12z. Let `t(q)` be
the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set
of earliest incoming nearest-neighbor steps at `q` using only records
with tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the
outgoing dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that
`q+e` is formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is
`UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Axis of a defined lock
set `S` is `Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and
only if `Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union
`Axis(O)` equals `{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover
HOLDs and `|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required. When
split HOLDs and `O` contains some `e` and `−e`, let `e_pair` be that `e`
of smallest axis index. Leftover axis `ℓ` is the unique Axis not in
`{axis(m), axis(e_pair)}`. Let `O_ℓ = O ∩ {± unit of ℓ}`. If `|O_ℓ|≠1`,
Orient fails, not `UNDEFINED`. Else let `o_ℓ` be that signed vector.
`Orient(q)` is the sign of the integer determinant of the 3×3 matrix
with columns `m`, `e_pair`, `o_ℓ`. If no opposite pair or split fails,
Orient fails, not `UNDEFINED`. Reverse HOLDs if and only if
`Orient(A)=Orient(B)` both `±1`. Face HOLDs if and only if
`Orient(C)=Orient(D)` both `±1`. Cover and split do not score handedness.
This is not leftover of nm2orichz unsigned leftover `+ℓ`. This is not
leftover of nm2orionez lex-one signed outgoing. This is not leftover of
nm2chiralz lexicographic `o1,o2` orientation. This is not leftover of
nm2axz axis-cover. This is not leftover of nm2ax12z 1-in 2-out split.
This is not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover-empty fail of leftover axis.
This is not leftover of nmunopp union. This is not leftover of nmt2opp
`M` frozen at `t`. This is not leftover of nmot2opp two-tick composition.
This is not leftover of nmoutopp untimed eventual-`O`. This is not
leftover of mixed #7188 fail/fail. This is not leftover of the 1-axis
opposite two-site seed. This is not leftover of the same-lock two-site
seed. The second pair is a new seed, not a formed child. Uniqueness is
not required. Mixed remains a set. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_zprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_zprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. The signed leftover-axis
oriented frame is the integer sign of `det(m,e_pair,o_ℓ)` with unique
signed incoming letter `m`, signed exist-opposite pair unit `e_pair` of
smallest axis index in `O`, leftover axis `ℓ` the unique Axis not in
`{axis(m), axis(e_pair)}`, and the unique signed vector `o_ℓ` in
`O ∩ {± unit of ℓ}`. Reverse and face are scored on equal `±1` signs at
the paired probes. Named signs `{+,−}` of locks are a coarser readout and
are not used as the object. A singleton unique outgoing lock letter is a
different readout and is not used as the object. Presence of an opposite
pair in `O` without the determinant sign is a different readout and is
not used. Unsigned leftover unit `+ℓ` is a different readout and is not
used. Lex-one signed outgoing letters per `Axis(O)` are a different
readout and are not used. Lexicographic unsigned outgoing 2-plane
`(o1,o2)` in axis order is a different readout and is not used.
Existential opposite of signed locks across probes is a different readout
and is not used. Axis-cover without the frame sign is a different readout
and is not used. 1-in 2-out split without the frame sign is a different
readout and is not used. Leftover-empty fail of unsigned leftover axis
sets is a different readout and is not used. A `Z^3` sum of those locks
is a different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four z-probes of the two-axis opposite seed, Orient at A,B,C,D, reverse hold and face fail from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_zprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face
target_blocker_text: "display leftover axis with the signed O vector on that axis, not unsigned +l, reverse/face on the four z-probes of the two-axis opposite seed, not lex-one, not cover, not split"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to unsigned leftover +l, do not reduce to lex-one signed outgoing, do not reduce to lexicographic o1,o2, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by presence of an opposite pair in O, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four z-probes of the two-axis opposite seed and reverse/face from that sign; displayed, not adopted"
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
signed leftover-axis 1-in 2-out frame of `M` and `O` is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second opposite pair. Same process and
z-probes as nm2axz.

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

## Named signed leftover-axis 1-in 2-out frame of `M` and `O` at `τ=t+1`

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

Signed leftover-axis oriented frame at the same cut:

```text
When split HOLDs and O contains some e and −e,
e_pair is that e of smallest axis index.
leftover axis ℓ is the unique Axis not in {axis(m), axis(e_pair)}.
O_ℓ = O ∩ {± unit of ℓ}.
If |O_ℓ|≠1, Orient fails, not UNDEFINED.
Else o_ℓ is that signed vector.
Orient(q) = sign of the integer determinant of columns (m, e_pair, o_ℓ).
If no opposite pair or split fails, Orient fails, not UNDEFINED.
UNDEFINED if M or O is UNDEFINED.
```

The opposite-pair unit is the positive lattice unit of the smallest-index
axis on which `O` contains both signs. The leftover letter is the unique
signed vector of `O` on leftover axis `ℓ`, not the unsigned unit `+ℓ`.
If leftover axis carries both signs, `|O_ℓ|=2` and Orient fails. Unique
outgoing letters are not required. Mixed opposite signs occupy the pair
axis as the pair. A vanishing determinant is fail. Sign of a nonzero
integer determinant is `+1` or `−1`. Split HOLD required: 2-in 1-out is
Orient fail, not UNDEFINED, even if `O` contains an opposite pair.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse and face while this face
fails. Identifying split reverse with this reverse is refused: split HOLDs
reverse and face while this face fails. Identifying leftover-empty fail
with this reverse is refused: leftover-empty fail scores empty leftover as
reverse fail, while this reverse HOLDs. Identifying lexicographic
`o1,o2` orientation with this reverse is refused: lexicographic reverse
fails with `Orient_lex(A)=−1` and `Orient_lex(B)=+1`, while this reverse
HOLDs. Identifying nm2orionez lex-one signed outgoing with this reverse is
refused: lex-one reverse fails and lex-one face HOLDs, while this reverse
HOLDs and this face fails. Identifying nm2orichz unsigned leftover `+ℓ`
with this Orient is refused: unsigned leftover at `C` and at `D` is `+e_2`
and yields `Orient=+1,−1`, while signed leftover is `−e_2` and yields
`Orient=−1,+1`. Reverse and face bits of unsigned leftover agree with
this member and do not make the leftover vector unsigned. Identifying
presence of an opposite pair in `O` with this face is refused: each of
`C` and `D` has an opposite pair in `O`, so pair-presence face HOLDs
while this face fails. Identifying a named sign of those locks with
reverse or face is refused: named-sign lettering lost the axis.

## Theorem 1 — ticks, `M`, `O`, split, pair, signed leftover, and Orient at `τ=t+1`

On this process the four z-probes form. Compare to leftover axis: that
leftover reports empty leftover at each probe and leftover reverse fail
and leftover face fail. Compare to nm2axz cover and nm2ax12z split: both
HOLD reverse and face on this member. Compare to nm2chiralz lexicographic
`o1,o2` orientation: reverse fails and face HOLDs on this member. Compare
to nm2orionez lex-one signed outgoing: reverse fails and face HOLDs on
this member. Compare to nm2orichz unsigned leftover `+ℓ`: reverse HOLDs
and face fails, matching the reverse/face bits here, while leftover at
`C` and at `D` is unsigned `+e_2` and Orient is `+1,−1`. This display
reads leftover axis with the signed `O` vector on that axis:

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
pair(A) = +e_1
leftover(A) = +e_3
det(A) = −1
Orient(A) = −1
m(B) = +e_1
pair(B) = +e_3
leftover(B) = +e_2
det(B) = −1
Orient(B) = −1
m(C) = +e_3
pair(C) = +e_1
leftover(C) = −e_2
det(C) = −1
Orient(C) = −1
m(D) = +e_1
pair(D) = +e_3
leftover(D) = −e_2
det(D) = +1
Orient(D) = +1
```

`A` is a seed at tick 0 with seed letter `+e_2`. Mixed remains a set:
`O(A,τ)` has three outgoing steps and `O(D,τ)` has three outgoing steps.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Here the
opposite pair in `O` is the signed exist-opposite pair of smallest axis
index, leftover axis is the remaining Axis, and leftover letter is the
unique signed vector of `O` on that axis, so mixed opposite signs occupy
the pair axis as the pair and Orient is defined. `M` is a singleton at
each probe, so the unique signed `m` exists. At each probe split HOLDs,
`O` contains an opposite pair, and `|O_ℓ|=1`, so Orient is the nonzero
integer sign of `det(m,e_pair,o_ℓ)`, not fail. Cover and split HOLD at
each probe and do not score that `Orient(C)` and `Orient(D)` are
opposite. Unsigned leftover `+ℓ` at `C` and at `D` is `+e_2` and yields
`+1` and `−1`; signed leftover is `−e_2` and yields `−1` and `+1`.
Lexicographic `o1,o2` at `B` and at `D` uses axis order `(e_2,e_3)` and
yields `+1`; this pair at `B` and at `D` is `+e_3` with signed leftover
`+e_2` at `B` and `−e_2` at `D`. If leftover axis carried both signs,
`|O_ℓ|≠1` and Orient would fail; that does not occur on these four
z-probes. O is not M.

On the 1-axis opposite two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and `C` is 2-in 1-out, so split fails at `C` and
Orient at `C` is fail, not UNDEFINED, even if one asks only for an
opposite pair in `O`. That is leftover of the first pair. Here both
`(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a second
axis. On the y-probes of this same seed, split HOLDs at `A` while `O(A)`
has no opposite pair, so signed leftover-axis Orient fails, not
UNDEFINED, while lexicographic `o1,o2` at that y-probe is defined.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`:

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
`±1`. `Orient(A)=−1` and `Orient(B)=−1`. Reverse HOLDs. This is HOLD iff
equal `±1` signs, not leftover of nm2orichz unsigned leftover `+ℓ`, not
leftover of nm2orionez lex-one signed outgoing, not leftover of
nm2chiralz lexicographic `o1,o2`, not leftover of nm2axz axis-cover, not
leftover of nm2ax12z 1-in 2-out split, not leftover-empty fail, and not
exist-opposite.

Reverse oriented frame at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Lexicographic reverse fails because lexicographic `Orient(A)=−1` and
`Orient(B)=+1`. Lex-one reverse fails because lex-one `Orient(A)=−1` and
`Orient(B)=+1`. Signed leftover-axis reverse HOLDs because both signs are
`−1`. Unsigned leftover reverse also HOLDs on this member because
`Orient` at `A` and at `B` is unchanged when leftover is `+ℓ`; that
agreement of reverse bits is not identity of leftover vectors.
Leftover-empty reverse fails because leftover of the union is empty at `A`
and at `B`. Leftover of `M` reverse fails because leftover of `M` at `A`
is `{e_1, e_3}` and at `B` is `{e_2, e_3}`: nonempty and unequal. Leftover
of `O` reverse fails because leftover of `O` at `A` is `{e_2}` and at `B`
is `{e_1}`: nonempty and unequal. Exist-opposite reverse of signed `M`
fails. Exist-opposite reverse of signed `O` holds. Presence of an
opposite pair in `O` at `A` and at `B` HOLDs. Those leftovers are not
this display.

Reverse holds.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)=−1` and `Orient(D)=+1`. Face fails.

Face oriented frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. Signed leftover-axis oriented face
fails because the two frame signs are opposite. Unsigned leftover `+ℓ`
face also fails, with opposite signs `+1` and `−1` rather than `−1` and
`+1`. Lexicographic face HOLDs because both lexicographic signs are `+1`.
Lex-one face HOLDs because both lex-one signs are `−1`. Cover and split
do not score handedness. Presence of an opposite pair in `O` HOLDs at `C` and at `D`,
so pair-presence face HOLDs while this face fails. On the 1-axis opposite
two-site seed, cover face HOLDs while split face fails at `C` from 2-in
1-out, and Orient at `C` is fail, not UNDEFINED. This two-axis member is
not leftover of that 1-axis split face fail. The four y-probes of this
same seed give Orient fail at `A` from no opposite pair in `O` and Orient
fail at `D` from split fail, so oriented face fails. The four x-probes
give oriented reverse fail and oriented face fail. Those probe-direction
readouts are not this z-probe display. Leftover-empty face fails because
leftover of the union is empty at `C` and at `D`. Leftover of `M` at `C`
is `{e_1, e_2}` and leftover of `M` at `D` is `{e_2, e_3}`: nonempty and
unequal. Leftover of `O` at `C` is `{e_3}` and leftover of `O` at `D` is
`{e_1}`: nonempty and unequal. Exist-opposite face of signed `M` fails.
Exist-opposite face of signed `O` fails. Signed leftover-axis oriented
face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover HOLDs at `D` and split HOLDs at `D`. Orient at `D`
is `+1`. Unsigned leftover at `D` is `+e_2` and Orient unsigned is `−1`.

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
- It does not replace Orient by unsigned leftover unit `+ℓ`.
- It does not replace Orient by nm2orionez lex-one signed outgoing.
- It does not replace Orient by lexicographic `o1,o2` orientation.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
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
- It does not reprint nm2chiralz lexicographic `o1,o2` reverse fail face
  hold as this oriented display.
- It does not reprint nm2orichz unsigned leftover `+ℓ` as this leftover
  vector.
- It does not reprint nm2orionez lex-one signed outgoing reverse fail face
  hold as this oriented display.
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
two-axis opposite seed process, signed leftover-axis determinant
orientation of the 1-in 2-out frame of `M` and `O` at `t+1`, and the
reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at each probe |
| unique signed `m`, opposite pair in `O`, signed leftover `o_ℓ` | Theorem 1; singleton `M`, smallest-index pair, unique signed leftover |
| integer `det(m,e_pair,o_ℓ)` | Theorem 1; `−1,−1,−1,+1` |
| Orient at `τ` | Theorem 1; `−1,−1,−1,+1` |
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
| leftover of nmcover axis-cover HOLD | not this oriented display |
| leftover of nm2axz axis-cover HOLD | not this oriented display |
| leftover of nm2ax12z 1-in 2-out split HOLD | not this oriented display |
| leftover of nm2chiralz lexicographic `o1,o2` | not this oriented display |
| leftover of nm2orichz unsigned leftover `+ℓ` | not this leftover vector |
| leftover of nm2orionez lex-one signed outgoing | not this oriented display |
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
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: leftover axis with the signed `O` vector on that axis, not unsigned `+ℓ`, of the 1-in 2-out frame of `M` and `O` at `t+1` on the four z-probes of the two-axis opposite seed, and reverse/face from that sign. |
| V2 | Current main has no landed signed leftover-axis reverse/face of timed `M` and `O` on these four z-probes of the two-axis opposite seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the integer sign of `det(m,e_pair,o_ℓ)` from the unique signed leftover vector in `O` at the same `t+1` cut, reverse HOLDs while lex-one reverse fails, face fails while lex-one face HOLDs, and Orient at `C` and at `D` differs from unsigned leftover `+ℓ`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by unsigned leftover unit `+ℓ`, does not replace Orient by
nm2orionez lex-one signed outgoing, does not replace Orient by nm2chiralz
lexicographic `o1,o2`, does not replace Orient by
nmcover axis-cover, does not replace Orient by nm2axz axis-cover, does not
replace Orient by nm2ax12z 1-in 2-out split, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2chiralz lexicographic `o1,o2` | reuse lexicographic reverse fail and face hold | lexicographic reverse fails (`−1,+1`) while this reverse HOLDs (`−1,−1`); lexicographic face HOLDs while this face fails | ATTEMPTED |
| nm2orionez lex-one signed outgoing | reuse lex-one reverse fail and face hold | lex-one reverse fails and lex-one face HOLDs while this reverse HOLDs and this face fails | ATTEMPTED |
| nm2orichz unsigned leftover `+ℓ` | reuse leftover unit `+ℓ` as the third column | unsigned leftover at `C` and at `D` is `+e_2` and Orient is `+1,−1`; signed leftover is `−e_2` and Orient is `−1,+1`; reverse/face bits agree and do not make leftover unsigned | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold on these z-probes | cover face HOLDs while Orient face fails: `Orient(C)=−1` and `Orient(D)=+1` | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse hold and split face hold | split face HOLDs while Orient face fails; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails while Orient reverse HOLDs; leftover face fails with Orient face | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal; leftover reverse fails while Orient reverse HOLDs | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`, nonempty unequal; leftover reverse fails while Orient reverse HOLDs | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` fails while Orient reverse HOLDs; exist-opposite is a cross-probe boolean, not `det(m,e_pair,o_ℓ)` | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence HOLDs at `C` and at `D`, so that face HOLDs while Orient face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of signed incoming, pair unit, and signed leftover vector | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; pair is `+e_1`, leftover is `+e_3`, and Orient is `−1` | ATTEMPTED |
| leftover axis with both signs | treat `|O_ℓ|=2` as defined by picking `+ℓ` | `|O_ℓ|≠1` is Orient fail, not UNDEFINED; unsigned leftover would still pick `+ℓ` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member they agree because each `M` letter is the positive unit; flipping `m` at `A` to `−e_2` flips Orient to `+1` while unsigned axis stays `e_2` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| no opposite pair as `UNDEFINED` | treat missing `e` and `−e` in `O` as unformed | missing opposite pair is Orient fail, not UNDEFINED; y-probe `A` of this seed is the witness | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, Orient fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and Orient at `C` is `−1` | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe Orient fails at `A` from no opposite pair in `O`; this letter is the four z-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four z-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores the signed leftover-axis oriented frame of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports Orient `−1,−1,−1,+1`, reverse hold, and face fail | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(A)` sums to `+e_3` while the pair is `+e_1` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with unsigned leftover unit `+ℓ`, missing
identification of Orient with nm2orionez lex-one signed outgoing, missing
identification of Orient with nm2chiralz lexicographic `o1,o2`, missing
identification of Orient with nmcover axis-cover, missing identification of
Orient with nm2axz axis-cover, missing identification of Orient with
nm2ax12z 1-in 2-out split, missing identification of this seed with the
1-axis opposite two-site seed, and missing Record identification of Orient
reverse are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, smallest-index
opposite pair in `O` when present, leftover axis the unique Axis not in
`{axis(m), axis(e_pair)}`, leftover letter the unique signed vector of `O`
on that axis, `|O_ℓ|≠1` as Orient fail not `UNDEFINED`, integer determinant
sign, missing opposite pair as Orient fail not `UNDEFINED`, split fail as
Orient fail not `UNDEFINED`, four z-probes with seed `A`, second pair as a
new seed not a formed child, and mixed remains a set are declared. No
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
| per element | signed incoming letter, smallest-index opposite pair in `O`, signed leftover `O` vector on leftover axis | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports, reverse/face from equal `±1` signs | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out frames. None
is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse hold is only cover reverse, only split reverse,
or only presence of an opposite pair in `O`; lexicographic `o1,o2` already
answers handedness; nm2orionez lex-one already answers signed leftover;
nm2orichz unsigned leftover `+ℓ` already answers reverse because reverse
and face bits agree; leftover-empty fail already answers reverse; leftover
of `M` alone already answers reverse; leftover of `O` alone already answers
reverse; exist-opposite of signed `O` already answers reverse; the second
pair is only the formed child `(0,0,1)` of the 1-axis seed; unique outgoing
letters should be required; and unsigned incoming axis already gives the
same signs because each `M` letter is the positive unit.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Orient reverse HOLDs because `Orient(A)=−1` and
`Orient(B)=−1`, while Orient face fails because `Orient(C)=−1` and
`Orient(D)=+1`. Cover and split HOLD reverse and face on this member and
do not score that opposite face signs. Lexicographic `o1,o2` reverse fails
with `−1,+1` and face HOLDs with `+1,+1`; this reverse HOLDs and this face
fails. Lex-one reverse fails and lex-one face HOLDs; this reverse HOLDs
and this face fails. Unsigned leftover `+ℓ` at `C` and at `D` is `+e_2`
and yields `+1` and `−1`; signed leftover is `−e_2` and yields `−1` and
`+1`. Reverse and face bits of unsigned leftover agree with this member
and do not make leftover unsigned. Presence of an opposite pair in `O`
HOLDs at each of the four z-probes, so pair-presence reverse and face both
HOLD, while this face fails. Leftover of `M` alone at `A` is `{e_1,e_3}`
and at `B` is `{e_2,e_3}`: nonempty unequal, so leftover-of-`M` reverse
fails while Orient reverse HOLDs. Leftover of `O` alone at `A` is `{e_2}`
and at `B` is `{e_1}`: leftover-of-`O` reverse fails. Exist-opposite reverse
of signed `O` holds with this reverse, but exist-opposite is a cross-probe
boolean, not `det(m,e_pair,o_ℓ)`. Unique outgoing letters would assign
`UNDEFINED` at mixed `O(A)`; the pair unit is `+e_1` and leftover is
`+e_3`. Unsigned incoming axis agrees on this member because each unique
`m` is the positive unit, and flipping `m` at `A` to `−e_2` flips Orient
to `+1` while `Axis(M)` stays `{e_2}`. The second pair is a new seed, not
a formed child: `(0,0,1)` is recorded at tick 0 with lock `+e_2`, whereas
the 1-axis child forms at tick 1 with lock `+e_3`. Reverse oriented frame
is HOLD iff equal `±1` signs at `A` and at `B`, not leftover of
nm2orichz unsigned leftover `+ℓ`.

### N8 — cross-cycle echo

nm2axz cover on this two-axis seed reported cover HOLD at each of the four
z-probes, reverse hold, and face hold. nm2ax12z 1-in 2-out split on the
same seed reported split HOLD at each of the four z-probes, reverse hold,
and face hold. nm2chiralz lexicographic `o1,o2` on the same seed reported
Orient `−1,+1,+1,+1`, reverse fail, and face hold. nm2orionez lex-one
signed outgoing reported Orient `−1,+1,−1,−1`, reverse fail, and face
hold. nm2orichz unsigned leftover `+ℓ` reported Orient `−1,−1,+1,−1`,
reverse hold, and face fail. Leftover axis reported empty leftover at
each of four z-probes, leftover reverse fail, and leftover face fail. The
four y-probes of this same seed reported split reverse hold and split
face fail, and signed leftover-axis Orient fail at `A` from no opposite
pair in `O`. This note is not those displays: it reports signed
leftover-axis determinant orientation of the 1-in 2-out frame of `M` and
`O` at `τ=t+1` on the two-axis opposite seed, with `t(A)=0`, `t(B)=1`,
`t(C)=1`, and `t(D)=1`, `Orient(A)=−1`, `Orient(B)=−1`, `Orient(C)=−1`,
`Orient(D)=+1`, reverse hold, and face fail. Cover and split do not score
handedness.

**Gate disposition:** PASS for the signed leftover-axis `t+1` reverse/face
reports above. FAIL / DO NOT SHIP for “the predicate equals the named
sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals unsigned leftover unit `+ℓ`,” “the predicate
equals nm2orionez lex-one HOLD,” “the predicate equals nm2chiralz
lexicographic `o1,o2` HOLD,” “the predicate equals nmcover axis-cover
HOLD,” “the predicate equals nm2axz axis-cover HOLD,” “the predicate
equals nm2ax12z 1-in 2-out split HOLD,” “the predicate equals the 1-axis
opposite two-site seed,” “the predicate equals nmunopp union,” “bits are
Admissibility,” “split fail is UNDEFINED,” “no opposite pair is
UNDEFINED,” “`|O_ℓ|≠1` is UNDEFINED,” “reverse oriented frame fails,” or
“face oriented frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the unique signed incoming letter, the
smallest-index opposite pair in `O`, leftover axis, and signed leftover
vector `o_ℓ`, reports the integer determinant and its sign, lists new
records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that Orient is
`−1,−1,−1,+1` at `A,B,C,D`, that reverse HOLDs while leftover reverse
fails, lexicographic reverse fails, and lex-one reverse fails, that face
fails while cover face, split face, pair-presence face, and lex-one face
HOLD, that unsigned leftover `+ℓ` differs at `C` and at `D`, that
`|O_ℓ|≠1` is Orient fail not `UNDEFINED`, that split fail is Orient fail
not `UNDEFINED`, that no opposite pair in `O` is Orient fail not
`UNDEFINED`, that the 1-axis opposite two-site seed is a different member
with Orient fail at `C`, that leftover-empty fail is a different reverse,
that leftover of `M` alone and leftover of `O` alone are different
objects, that mixed sets remain sets, that unique-letter Orient is
`UNDEFINED` at mixed `O`, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not
attached, that the second pair is a new seed not a formed child, that the
y-probes and x-probes of this seed are not this letter, and that the
display is not the two-tick lock-count clock composition. No runner cache
is written.
