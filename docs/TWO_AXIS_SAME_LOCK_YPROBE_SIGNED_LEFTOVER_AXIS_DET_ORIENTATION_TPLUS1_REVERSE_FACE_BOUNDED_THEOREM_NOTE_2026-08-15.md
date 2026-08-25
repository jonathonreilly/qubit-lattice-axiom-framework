---
claim_id: two_axis_same_lock_yprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Signed leftover-axis det orientation at t+1 on the four y-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py
---

# Signed Leftover-Axis Determinant Orientation Of The 1-In 2-Out Frame At t+1 Reverse And Face On Four Y-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** signed leftover-axis det orientation of the 1-in 2-out frame of
simultaneous earliest incoming set `M` and outgoing dual `O` at each
probe's `τ=t+1`, and reverse/face from that sign, on the four y-probes of
the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same process and
y-probes as nm2slo. Orient as nm2orilefz. Let `t(q)` be the formation tick
of probe `q`. Let `τ(q)=t+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set
of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required. When `M` is
singleton `{m}` and `O` contains some `e` and `−e`, let `e_pair` be that
`e` of smallest axis index. Leftover axis `ℓ` is the unique Axis not in
`{axis(m), axis(e_pair)}`. Let `O_ℓ = O ∩ {± unit of ℓ}`. If `|O_ℓ| ≠ 1`,
Orient fails, not `UNDEFINED`. Else let `o_ℓ` be that signed vector.
`Orient(q)` is the sign of the integer determinant of the 3×3 matrix with
columns `m`, `e_pair`, `o_ℓ`. If no opposite pair in `O`, fail, not
`UNDEFINED`. Else fail, not `UNDEFINED`, if split fails. Reverse HOLDs if
and only if `Orient(A)=Orient(B)` both `±1`. Face HOLDs if and only if
`Orient(C)=Orient(D)` both `±1`. Cover and split do not score handedness.
This is not leftover of nm2slo exist-opposite of `O`. This is not leftover
of nm2orilefy opposite-seed leftover-axis Orient. This is not leftover of
nm2ax axis-cover. This is not leftover of nm2ax12 1-in 2-out split. This
is not leftover of lexicographic `o1,o2`. This is not leftover of
nm2orichy unsigned leftover `+ℓ`. This is not leftover of nm2orioney
lex-one signed outgoing. This is not leftover of leftover-of-`M` alone.
This is not leftover of leftover-of-`O` alone. This is not leftover-empty
fail of leftover axis. This is not leftover of nmunopp union. This is not
leftover of nmt2opp `M` frozen at `t`. This is not leftover of nmot2opp
two-tick composition. This is not leftover of nmoutopp untimed
eventual-`O`. This is not leftover of mixed #7188 fail/fail. This is not
leftover of the 1-axis same-lock two-site seed. This is not leftover of
the two-axis opposite seed. This is not the two-tick lock-count clock
composition. The second pair is a new seed, not a formed child.
Uniqueness is not required. Mixed remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face_2026_08_15.py)

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
Split is cover together with `|Axis(M)|=1`. The signed leftover-axis
oriented frame is the integer sign of `det(m,e_pair,o_ℓ)` with unique signed
incoming letter `m`, signed exist-opposite pair unit `e_pair` of smallest
axis index in `O`, and the unique signed leftover vector of `O` on leftover
axis. Reverse and face are scored on equal `±1` signs at the paired probes.
Named signs `{+,−}` of locks are a coarser readout and are not used as the
object. A singleton unique outgoing lock letter is a different readout and
is not used as the object. Unsigned leftover unit `+ℓ` is a different
readout and is not used. Lexicographic unsigned outgoing 2-plane `(o1,o2)`
in axis order is a different readout and is not used. Lex-one signed
outgoing letters per `Axis(O)` are a different readout and are not used.
Existential opposite of signed locks is a different readout and is not
used. Axis-cover without the frame sign is a different readout and is not
used. 1-in 2-out split without the frame sign is a different readout and is
not used. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four y-probes of the two-axis same-lock seed, Orient fail,-1,fail,fail, reverse fail and face fail from equal +/-1 signs; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yprobe_signed_leftover_axis_det_orientation_tplus1_reverse_face
target_blocker_text: "display signed leftover-axis determinant orientation of the 1-in 2-out frame reverse/face on the four y-probes of the two-axis same-lock seed, not unsigned leftover +l, not lex-one, not cover, not split, not nm2slo exist-opposite"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 displayed; do not write Orient into Admissibility, do not reduce to unsigned leftover +l, do not reduce to lexicographic o1,o2, do not reduce to nm2orioney lex-one, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by presence of an opposite pair in O, do not replace Orient by existential opposite of signed locks, do not replace Orient by nm2slo exist-opposite of O, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for signed leftover-axis determinant orientation of the 1-in 2-out frame of M and O at t+1 on the four y-probes of the two-axis same-lock seed and reverse/face from that sign; displayed, not adopted"
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
signed leftover-axis determinant orientation of `M` and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nm2slo.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `+e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `+e_2`. Neither pair is opposite. The second pair is
a new seed, not a formed child of the first pair. This seed is not the
1-axis same-lock two-site seed `{0,(0,1,0)}` with only `+e_1/+e_1`. This
seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`. This seed is not the
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

## Named signed leftover-axis 1-in 2-out frame of `M` and `O` at `τ=t+1`

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

Signed leftover-axis oriented frame at the same cut:

```text
When M is singleton {m} and O contains some e and −e,
e_pair is that e of smallest axis index.
leftover axis ℓ is the unique Axis not in {axis(m), axis(e_pair)}.
O_ℓ = O intersect {± unit of ℓ}.
If |O_ℓ| != 1, Orient fails, not UNDEFINED.
Else o_ℓ is that unique signed vector.
Orient(q) = sign of the integer determinant of columns (m, e_pair, o_ℓ).
If no opposite pair in O, fail, not UNDEFINED.
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The opposite-pair unit is the positive lattice unit of the smallest-index
axis on which `O` contains both signs. Unique outgoing letters are not
required. Mixed opposite signs occupy that axis as the pair. A vanishing
determinant is fail. Sign of a nonzero integer determinant is `+1` or `−1`.
Split HOLD required: 2-in 1-out is Orient fail, not UNDEFINED, even if `O`
contains an opposite pair. Missing opposite pair is Orient fail, not
UNDEFINED. Leftover axis carrying both signs, `|O_ℓ|≠1`, is Orient fail,
not UNDEFINED, and is not repaired by picking unsigned `+ℓ`.

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` and both
signs are `±1`. Face oriented frame holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover HOLDs reverse while this reverse fails.
Identifying split reverse with this reverse is refused: split HOLDs reverse
while this reverse fails. Identifying leftover-empty fail with this reverse
is refused: leftover-empty fail scores empty leftover as reverse fail, and
those reverse bits agree here, but leftover of the union at `B` is empty
while `Orient(B)=−1`. Identifying lexicographic `o1,o2` orientation with
this reverse is refused: lexicographic reverse HOLDs with `+1,+1` while this
reverse fails. Identifying nm2orioney lex-one signed outgoing with this
reverse is refused: lex-one reverse HOLDs while this reverse fails.
Identifying nm2orichy unsigned leftover `+ℓ` with this Orient is refused:
unsigned leftover at `C` is `+e_3` and yields `Orient=−1`, while signed
leftover fails from `|O_ℓ|=2`. Reverse and face bits of unsigned leftover
agree with this member and do not make leftover unsigned. Identifying
nm2slo exist-opposite of `O` with this reverse or face is refused:
exist-opposite reverse of `O` HOLDs and exist-opposite face of `O` HOLDs,
while this reverse fails and this face fails. Identifying presence of an
opposite pair in `O` with this face is refused: `C` has an opposite pair
in `O` while `D` does not, so pair-presence face fails with this face, and
pair presence at `C` is not Orient at `C`. Identifying a named sign of
those locks with reverse or face is refused: named-sign lettering lost the
axis.

## Theorem 1 — ticks, `M`, `O`, split, pair, signed leftover, and Orient at `τ=t+1`

On this process the four y-probes form. Compare to leftover axis: leftover
of the union is empty at `A`, `B`, and `C`, leftover `{e_2}` at `D`,
leftover reverse fail and leftover face fail. Compare to nm2ax axis-cover
and nm2ax12 1-in 2-out split: both HOLD reverse and fail face on this
member. Compare to lexicographic `o1,o2`: that readout scores
`Orient(A)=+1` and `Orient(B)=+1` from the unsigned outgoing 2-plane, so
lex reverse HOLDs. Compare to nm2orichy unsigned leftover `+ℓ`: that
readout scores Orient fail, `−1`, `−1`, fail, matching reverse fail and
face fail, while leftover at `C` is unsigned `+e_3` and Orient at `C` is
`−1`. Compare to nm2slo exist-opposite of `O`: that readout HOLDs reverse
and HOLDs face. Compare to nm2orilefy opposite-seed leftover-axis Orient:
there `M(A)={−e_1}` and `O(D)` includes `−e_1`. This display reads leftover
axis with the signed `O` vector on that axis:

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
m(A) = +e_1
pair(A) = fail
leftover(A) = fail
det(A) = fail
Orient(A) = fail
m(B) = +e_1
pair(B) = +e_3
leftover(B) = +e_2
det(B) = −1
Orient(B) = −1
m(C) = +e_2
pair(C) = +e_1
leftover(C) = fail
det(C) = fail
Orient(C) = fail
m(D) = −e_3
pair(D) = fail
leftover(D) = fail
det(D) = fail
Orient(D) = fail
```

`A` is a seed at tick 0 with seed letter `+e_1`. Mixed remains a set:
`O(A,τ)` has two outgoing steps and `O(B,τ)` has three outgoing steps.
Unique outgoing letters would assign `UNDEFINED` at mixed `O`. Here
uniqueness is not required. At `A`, split HOLDs and `O` has no opposite
pair, so signed leftover-axis Orient fails, not `UNDEFINED`. At `B`, split
HOLDs, `O` has opposite pair `±e_3`, leftover axis is `e_2`, `|O_ℓ|=1` with
`o_ℓ=+e_2`, and `det(+e_1,+e_3,+e_2)=−1`. At `C`, split HOLDs, pair HOLDs
on `{+e_1,−e_1}`, leftover axis is `e_3`, and `|O ∩ {±e_3}|=2`, so signed
leftover fails, not `UNDEFINED`, while unsigned leftover `+ℓ` would pick
`+e_3` and score `det(+e_2,+e_1,+e_3)=−1`. At `D`, pair fails because
`O(D)={+e_1}` has no opposite, and split fails from cover fail with
leftover `{e_2}` (1-in 1-out). Split HOLD is required, so Orient at `D` is
fail, not `UNDEFINED`. Cover and split HOLD reverse on this member and do
not score that Orient at `A` is fail. O is not M.

On the 1-axis same-lock two-site seed, `B` forms at tick 2 and `D` at tick
3, `O(A,τ)` includes `+e_3` because `(0,1,1)` is then a formed child rather
than a seed, signed leftover-axis Orient at `A` is `−1`, and `D` is 2-in
1-out, so split fails at `D` and Orient at `D` is fail, not UNDEFINED. That
is leftover of the first pair. Here both `(0,0,1)` and `(0,1,1)` are seeds
of a second same-lock pair on a second axis, `t(D)=2`, and Orient at `A` is
fail from no opposite pair.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

`M` is frozen from `t` to `t+1`. At `t`, `O` is empty at `A`, `B`, `C`, and
`D`. Orient at `t` is fail, not UNDEFINED.

## Theorem 2 — reverse from oriented frame at `τ`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. `Orient(A)` is fail and `Orient(B)=−1`. Reverse fails. This is HOLD
iff equal `±1` signs, not leftover of nm2orichy unsigned leftover `+ℓ`, not
leftover of nm2orioney lex-one signed outgoing, not leftover of
lexicographic `o1,o2`, not leftover of nm2ax axis-cover, not leftover of
nm2ax12 1-in 2-out split, not leftover-empty fail, not leftover of nm2slo
exist-opposite of `O`, and not leftover of nm2orilefy.

Reverse oriented frame at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse HOLDs
because cover HOLDs at `A` and at `B`. Split reverse HOLDs because split
HOLDs at `A` and at `B`. Cover and split do not score handedness.
Lexicographic reverse HOLDs because lexicographic `Orient(A)=+1` and
`Orient(B)=+1`. Lex-one reverse HOLDs. Signed leftover-axis reverse fails
because Orient at `A` is fail from no opposite pair in `O`. Unsigned
leftover reverse also fails on this member because leftover at `A` still
has no pair; that agreement of reverse bits is not identity of leftover
vectors. Leftover-empty reverse fails because leftover of the union is
empty at `A` and at `B`. Leftover of `M` reverse HOLDs because leftover of
`M` at `A` and at `B` is `{e_2, e_3}`: nonempty and equal. Leftover of `O`
reverse HOLDs because leftover of `O` at `A` and at `B` is `{e_1}`:
nonempty and equal. Exist-opposite reverse of signed `M` fails: both
`M(A,τ)` and `M(B,τ)` are `{+e_1}`. Exist-opposite reverse of signed `O`
holds: `−e_3` in `O(A,τ)` against `+e_3` in `O(B,τ)`. That nm2slo reverse
HOLD is not this reverse. Presence of an opposite pair in `O` fails at `A`
and HOLDs at `B`, so pair-presence reverse fails with this reverse. Those
leftovers are not this display.

Reverse fails.

## Theorem 3 — face from oriented frame at `τ`

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
`Orient(C)` is fail and `Orient(D)` is fail. Face fails.

Face oriented frame at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face fails because cover fails at `D`. Split face fails because
split fails at `D`. Signed leftover-axis oriented face fails because Orient
fails at `C` from `|O_ℓ|=2` and at `D` from split fail and missing pair.
Unsigned leftover `+ℓ` face also fails, with Orient `−1` at `C` rather than
fail. Pair face fails with this face: `D` has no opposite pair in `O`.
nm2slo exist-opposite face HOLDs from `−e_1` in `O(C,τ)` against `+e_1` in
`O(D,τ)` while this face fails. On the 1-axis same-lock two-site seed,
cover face HOLDs while split face fails, Orient at `A` is `−1`, and Orient
at `D` is fail, not UNDEFINED. This two-axis member is not leftover of that
1-axis split face fail: here `t(D)=2`, `M(D)` is singleton `{−e_3}`, and
Orient at `A` is fail. The four z-probes of this same seed give signed
leftover-axis reverse fail and face fail, with Orient at `D` equal to `+1`.
The four x-probes give reverse fail and face fail. Those probe-direction
readouts are not this y-probe display. Leftover-empty face fails because
leftover of the union is empty at `C`. Leftover of `M` at `C` is
`{e_1, e_3}` and leftover of `M` at `D` is `{e_1, e_2}`: nonempty and
unequal. Leftover of `O` at `C` is `{e_2}` and leftover of `O` at `D` is
`{e_2, e_3}`: nonempty and unequal. Exist-opposite face of signed `M`
fails. Exist-opposite face of signed `O` holds. Unique signed face fails.
Unsigned leftover face fails. Lexicographic face fails. Lex-one oriented
face fails.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `D` and split fails at `D`. Pair fails at
`D`. Orient at `D` is fail. Unsigned leftover at `C` is `+e_3` and Orient
unsigned is `−1`.

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
- It does not replace Orient by nm2orioney lex-one signed outgoing.
- It does not replace Orient by lexicographic `o1,o2` orientation.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not replace Orient by nm2slo exist-opposite of `O`.
- It does not treat split fail as `UNDEFINED`.
- It does not treat missing opposite pair as `UNDEFINED`.
- It does not treat `|O_ℓ|≠1` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace Orient by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmcover axis-cover reverse hold face fail as this
  oriented display.
- It does not reprint nm2ax axis-cover reverse hold face fail as this
  oriented display.
- It does not reprint nm2ax12 1-in 2-out split reverse hold face fail as
  this oriented display.
- It does not reprint lexicographic `o1,o2` reverse hold face fail as this
  oriented display.
- It does not reprint nm2orichy unsigned leftover `+ℓ` as this leftover
  vector.
- It does not reprint nm2orioney lex-one signed outgoing reverse hold face
  fail as this oriented display.
- It does not reprint nm2slo exist-opposite reverse hold face hold as this
  oriented display.
- It does not reprint nm2orilefy opposite-seed leftover-axis Orient as this
  member.
- It does not reprint the 1-axis same-lock two-site seed as this member.
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
two-axis same-lock seed process, signed leftover-axis determinant
orientation of the 1-in 2-out frame of `M` and `O` at `t+1`, and the
reverse/face bits from that sign are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock seed `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| split at `τ` | Theorem 1; HOLD at `A,B,C`, fail at `D` |
| unique signed `m`, opposite pair in `O`, signed leftover `o_ℓ` | Theorem 1; singleton `M`; pair fail at `A` and at `D`; `|O_ℓ|=1` only at `B` |
| integer `det(m,e_pair,o_ℓ)` | Theorem 1; fail, `−1`, fail, fail |
| Orient at `τ` | Theorem 1; fail, `−1`, fail, fail |
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
| leftover of nm2slo exist-opposite HOLD | not this oriented display |
| leftover of nmcover axis-cover HOLD | not this oriented display |
| leftover of nm2ax axis-cover HOLD | not this oriented display |
| leftover of nm2ax12 1-in 2-out split HOLD | not this oriented display |
| leftover of lexicographic `o1,o2` | not this oriented display |
| leftover of nm2orichy unsigned leftover `+ℓ` | not this leftover vector |
| leftover of nm2orioney lex-one signed outgoing | not this oriented display |
| leftover of opposite-pair presence in `O` | not this oriented display |
| leftover of nm2orilefy opposite seed | not this letter |
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
| no opposite pair scored as `UNDEFINED` | refused; Orient fail |
| `|O_ℓ|≠1` scored as `UNDEFINED` | refused; Orient fail |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: leftover axis with the signed `O` vector on that axis, not unsigned `+ℓ`, of the 1-in 2-out frame of `M` and `O` at `t+1` on the four y-probes of the two-axis same-lock seed, and reverse/face from that sign. |
| V2 | Current main has no landed signed leftover-axis reverse/face of timed `M` and `O` on these four y-probes of the two-axis same-lock seed. |
| V3 | Orient reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the integer sign of `det(m,e_pair,o_ℓ)` from the unique signed leftover vector in `O` at the same `t+1` cut, reverse fails while leftover of `M` reverse HOLDs and while lex reverse HOLDs and while nm2slo exist-opposite reverse HOLDs, and Orient at `C` is fail while unsigned leftover `+ℓ` is `−1`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by lexicographic `o1,o2`, does not replace Orient by nm2orichy
unsigned leftover `+ℓ`, does not replace Orient by nm2orioney lex-one,
does not replace Orient by nmcover axis-cover, does not replace Orient by
nm2ax axis-cover, does not replace Orient by nm2ax12 1-in 2-out split,
does not replace Orient by nm2slo exist-opposite of `O`, does not identify
this display with the 1-axis same-lock two-site seed, does not identify it
with nm2orilefy, and does not identify it with nmunopp union. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| lexicographic `o1,o2` | reuse unsigned reverse hold | lexicographic Orient at `A` is `+1` and at `B` is `+1`, so lex reverse HOLDs, while this Orient at `A` is fail and this reverse fails | ATTEMPTED |
| nm2orichy unsigned leftover `+ℓ` | reuse leftover unit `+ℓ` as the third column | unsigned leftover at `C` is `+e_3` and Orient is `−1`; signed leftover fails from `|O_ℓ|=2`; reverse/face bits agree and do not make leftover unsigned | ATTEMPTED |
| nm2orioney lex-one signed outgoing | reuse lex-one reverse hold and face fail | lex-one reverse HOLDs while this reverse fails; lex-one Orient at `A` is not fail | ATTEMPTED |
| nm2ax axis-cover | reuse cover reverse hold and cover face fail on these y-probes | cover reverse HOLDs while Orient reverse fails; cover does not report fail at `A` from no pair | ATTEMPTED |
| nm2ax12 1-in 2-out split | reuse split reverse hold and split face fail | split reverse HOLDs while Orient reverse fails; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with this reverse, but leftover of the union at `B` is empty while `Orient(B)=−1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` is `{e_2,e_3}`, leftover-of-`M` reverse HOLDs while Orient reverse fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` is `{e_1}`, leftover-of-`O` reverse HOLDs while Orient reverse fails | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse of `M` and of `O` | exist-opposite reverse of signed `M` fails with this reverse; exist-opposite reverse of signed `O` HOLDs while Orient reverse fails; exist-opposite face of signed `O` HOLDs while Orient face fails | ATTEMPTED |
| nm2slo exist-opposite of `O` | reuse exist-opposite reverse hold and face hold | nm2slo reverse HOLDs and face HOLDs; this reverse fails and this face fails | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence reverse fails with this reverse at `A`; pair HOLDs at `C` while Orient at `C` fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of signed incoming, pair unit, and signed leftover vector | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter Orient is `UNDEFINED` while this Orient is fail | ATTEMPTED |
| leftover axis with both signs | treat `|O_ℓ|=2` as defined by picking `+ℓ` | `|O_ℓ|≠1` is Orient fail, not UNDEFINED; unsigned leftover would still pick `+ℓ` at `C` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member they agree at the four probes; flipping `m` at `B` to `−e_1` flips Orient to `+1` while unsigned axis stays `e_1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `D` is 1-in 1-out cover fail | ATTEMPTED |
| no opposite pair as `UNDEFINED` | treat missing `e` and `−e` in `O` as unformed | missing opposite pair is Orient fail, not UNDEFINED; y-probe `A` is the witness | ATTEMPTED |
| 1-axis same-lock two-site seed | reuse `t(B)=2`, `t(D)=3`, mixed `M(D)`, cover face HOLD | different seed; second pair is a new seed, not a formed child; here `t(D)=2`, cover face fails, and Orient at `A` is fail | ATTEMPTED |
| two-axis opposite leftover | lock the pairs as `+e_1/−e_1` and `+e_2/−e_2` | that leftover of nm2orilefy has `M(A)={−e_1}` and `O(D)` includes `−e_1`; here `M(A)={+e_1}` and `O(D)={+e_1}` | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe signed leftover reverse fails and face fails, with Orient at `D` equal to `+1`; this letter is the four y-probes | ATTEMPTED |
| x-probe Orient | score the four x-probes on this seed | x-probe reverse fails and face fails; this letter is the four y-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores signed leftover-axis orientation of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports Orient fail, `−1`, fail, fail on the two-axis same-lock seed | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` without the second pair | different seed; this member is two disjoint same-lock pairs | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; mixed `O(B)` sums to `+e_2` while signed leftover Orient is `−1` | ATTEMPTED |
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
identification of Orient with nm2orioney lex-one signed outgoing, missing
identification of Orient with lexicographic `o1,o2`, missing identification
of Orient with nmcover axis-cover, missing identification of Orient with
nm2ax axis-cover, missing identification of Orient with nm2ax12 1-in 2-out
split, missing identification of Orient with nm2slo exist-opposite of `O`,
missing identification of this seed with the 1-axis same-lock two-site
seed, missing identification with nm2orilefy, and missing Record
identification of Orient reverse are distinct open premises. This note
claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, smallest-index
opposite pair in `O` when present, leftover axis the unique Axis not in
`{axis(m), axis(e_pair)}`, leftover letter the unique signed vector of `O`
on that axis, `|O_ℓ|≠1` as Orient fail not `UNDEFINED`, integer determinant
sign, missing opposite pair as Orient fail not `UNDEFINED`, split fail as
Orient fail not `UNDEFINED`, four y-probes with seed `A`, second pair as a
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
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
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
exist-opposite of signed `O` already answers reverse and face; lexicographic
`o1,o2` already answers handedness; nm2orioney lex-one already answers
signed leftover; nm2orichy unsigned leftover `+ℓ` already answers reverse
because reverse and face bits agree; mixed #7188 already reported
fail/fail; the second pair is only the formed child of the 1-axis seed;
unique outgoing letters should be required; and unsigned incoming axis
already gives the same signs.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Those reverse bits agree here, but leftover of the union at
`B` is empty while `Orient(B)=−1` from `det(+e_1,+e_3,+e_2)`. Cover and
split HOLD reverse on this member and do not score that Orient at `A` is
fail. Lexicographic `o1,o2` reverse HOLDs with `+1,+1`; this reverse fails
from fail at `A`. Lex-one reverse HOLDs; this reverse fails. Unsigned
leftover `+ℓ` at `C` is `+e_3` and yields `−1`; signed leftover fails from
`|O_ℓ|=2`. Reverse and face bits of unsigned leftover agree with this
member and do not make leftover unsigned. Presence of an opposite pair in
`O` fails at `A` and HOLDs at `C` and fails at `D`. Leftover of `M` alone
at `A` and at `B` is `{e_2,e_3}`: leftover-of-`M` reverse HOLDs while
Orient reverse fails. Leftover of `O` alone at `A` and at `B` is `{e_1}`:
leftover-of-`O` reverse HOLDs. Exist-opposite reverse of signed `M` fails
with this reverse; exist-opposite reverse of signed `O` HOLDs while this
reverse fails; exist-opposite face of signed `O` HOLDs while this face
fails. Unique outgoing letters would assign `UNDEFINED` at mixed `O(A)`;
this Orient is fail, not `UNDEFINED`. Unsigned incoming axis agrees on this
member at the four probes, and flipping `m` at `B` to `−e_1` flips Orient
to `+1` while `Axis(M)` stays `{e_1}`. Mixed #7188 is a different
z-symmetric process with mixed `M`. The second pair is a new seed, not a
formed child: `(0,0,1)` is recorded at tick 0 with lock `+e_2`. Reverse
oriented frame is HOLD iff equal `±1` signs at `A` and at `B`, not leftover
of nm2orichy unsigned leftover `+ℓ`, and not leftover of nm2slo.

### N8 — cross-cycle echo

nm2ax cover on a two-axis seed reported cover HOLD at `A,B,C`, cover fail
at `D`, reverse hold, and face fail. nm2ax12 1-in 2-out split reported
split HOLD at `A,B,C`, split fail at `D`, reverse hold, and face fail.
Lexicographic `o1,o2` on these same-lock y-probes reported Orient
`+1,+1,−1`, fail, reverse hold, and face fail. nm2orichy unsigned leftover
`+ℓ` on these y-probes reported Orient fail, `−1`, `−1`, fail, reverse
fail, and face fail. nm2slo exist-opposite of own `O` on these y-probes
reported reverse hold and face hold. nm2orilefy signed leftover-axis on
the opposite seed reported the same Orient fail, `−1`, fail, fail, reverse
fail, and face fail, with `M(A)={−e_1}` and `O(D)={+e_1,−e_1}`. Leftover
axis reported empty leftover at `A,B,C`, leftover `{e_2}` at `D`, leftover
reverse fail, and leftover face fail. The four z-probes of this same seed
reported signed leftover-axis reverse fail and face fail. This note is not
those displays: it reports signed leftover-axis determinant orientation of
the 1-in 2-out frame of `M` and `O` at `τ=t+1` on the two-axis same-lock
seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=2`, `Orient(A)=fail`,
`Orient(B)=−1`, `Orient(C)=fail`, `Orient(D)=fail`, reverse fail, and face
fail. Cover and split do not score handedness.

**Gate disposition:** PASS for the signed leftover-axis `t+1` reverse/face
reports above. FAIL / DO NOT SHIP for “the predicate equals the named
sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals opposite-pair presence in
`O`,” “the predicate equals unsigned leftover unit `+ℓ`,” “the predicate
equals nm2orioney lex-one HOLD,” “the predicate equals lexicographic
`o1,o2` HOLD,” “the predicate equals nmcover axis-cover HOLD,” “the
predicate equals nm2ax axis-cover HOLD,” “the predicate equals nm2ax12
1-in 2-out split HOLD,” “the predicate equals nm2slo exist-opposite HOLD,”
“the predicate equals nm2orilefy,” “the predicate equals the 1-axis
same-lock two-site seed,” “the predicate equals nmunopp union,” “bits are
Admissibility,” “split fail is UNDEFINED,” “no opposite pair is
UNDEFINED,” “`|O_ℓ|≠1` is UNDEFINED,” “reverse oriented frame holds,” or
“face oriented frame holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports split of the pair, reports the unique signed incoming letter, the
smallest-index opposite pair in `O`, leftover axis, and signed leftover
vector `o_ℓ`, reports the integer determinant and its sign, lists new
records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that Orient is
fail, `−1`, fail, fail at `A,B,C,D`, that reverse fails while leftover of
`M` reverse HOLDs and lex reverse HOLDs and nm2slo exist-opposite reverse
HOLDs, that face fails, that unsigned leftover at `C` is `−1` while this
Orient at `C` is fail, that split fail is Orient fail not `UNDEFINED`, that
no opposite pair is Orient fail not `UNDEFINED`, that `|O_ℓ|≠1` is Orient
fail not `UNDEFINED`, that the 1-axis same-lock two-site seed is a
different member with `t(D)=3` and Orient at `A` equal to `−1`, that
leftover-empty fail is a different predicate, that leftover of `M` alone
and leftover of `O` alone are different objects, that mixed sets remain
sets, that unique-letter Orient is `UNDEFINED` at mixed `O`, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that the second pair is a new seed not
a formed child, that the z-probes and x-probes of this seed are not this
letter, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
